---
title: PIMS Version 5.3 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: PIMS v5.3 sends out the Order Parameters for Registration and Scheduling set to NULL. Before installing PIMS v5.3, the values in the Order Parameters file (#100.99), PACKAGE PARAMETERS field multiple (#5), ON field (#1) should be reviewed and saved. After the installation is completed, the parameter
audience: 
keywords: 
  - filed
  - valm
  - dgini
  - protocol
  - routine
  - added
  - edit
  - sdini
  - namespace
  - located
page_count: 0
word_count: 16885
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/pimsig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

Decentralized Hospital Computer Program

PIMSPATIENT INFORMATIONMANAGEMENT SYSTEM(formerly MAS)installation guide

August 1993

Information Systems Center

Albany, New York

Table of Contents

PIMS Installation

> PIMS Introduction 1

> PIMS Package Integration 3

> PIMS Installation 5

> PIMS Installation Dialogues 9

> DPTINIT Sample 9

> DGINIT Sample 11

> SDINIT Sample 39

> PIMS Routine List 49

> PIMS Resource Requirements 53

List Manager Installation

> List Manager Introduction 55

> List Manager Package Integration 55

> List Manager Installation 57

> List Manager Installation Dialogues 59

> Site has Order Entry v2.5 Installed 59

> Site does not have Order Entry v2.5 Installed 63

> List Manager Routine List 67

> List Manager - XQOR Patches 69

PIMS Introduction

PIMS v5.3 sends out the Order Parameters for Registration and Scheduling set to NULL. Before installing PIMS v5.3, the values in the Order Parameters file (#100.99), PACKAGE PARAMETERS field multiple (#5), ON field (#1) should be reviewed and saved. After the installation is completed, the parameters should be restored to the correct values.

It is recommended that the inits are accomplished in the following order.

> VALMINIT List Manager

> DPTINIT Patient file

> DGINIT Registration/ADT/PTF/IRT/Bene Travel

> SDINIT Scheduling

PIMS Package Integration

1\. The following package versions (or higher) MUST be installed PRIOR to loading this version of PIMS.

DRG v9.0

Generic Code Sheet v1.5

Kernel v7.0

VA FileMan v19.0

Order Entry v1.96

Health Level Seven v1.5

Integrated Billing v1.5

Co-Pay Exemption Patch IB\*1.5\*9, DG\*5.2\*22, SD\*5.2\*9, and PRCA\*3.7\*8

2\. As part of the DGINIT post-init, the following routines will be installed when appropriate.

Routine Package Patch \#

IBACKIN Integrated Billing IB\*1.5\*14

IBECEA3 Integrated Billing IB\*1.5\*14

IBCNSP2 Integrated Billing IB\*1.5\*14

IBCNSC Integrated Billing IB\*1.5\*14

IBOVOP1 Integrated Billing IB\*1.5\*14

DGCRNS Integrated Billing IB\*1.5\*14

DVBHS1 HINQ DVB\*4\*11

DVBHS2 HINQ DVB\*4\*11

DVBHS5 HINQ DVB\*4\*11

DVBHS6 HINQ DVB\*4\*11

These routines contain modifications necessary to run with PIMS v5.3. If a routine has already been installed via the patch, it will not be loaded as part of the install.

3\. The VALMINIT inits will install the version of the XQOR\* routines that were distributed as part of Order Entry v2.5. If Order Entry v2.5 has already been installed, the post-init process will not load the XQOR\* routines.

4\. Note: The IB, DVB, and XQOR\* routines mentioned above must be moved to all systems after the install is completed.

5\. Also included in this release are a number of cross-references on fields in the PATIENT file (#2) needed by the Income Verification Match (IVM) package. However, you do not need to have IVM installed to install PIMS v5.3.

6\. Event Driven Reporting (EDR) v1.5 was recently released in the EDR namespace. This software is now part of PIMS v5.3 in the VAFED namespace. Along with the old functionality in EDR v1.5, there is new functionality to capture outpatient events. A protocol is placed on the PIMS outpatient event driver which will collect all outpatient events. This information will then be bundled into an Health Leven Seven (HL7) message and sent to the Central System.

PIMS Installation

<u>Step</u> <u>Description</u>

1 Transmit Closed/Released PTF records.

PTF edit checks have been changed and enhanced as part of PIMS v5.3. As a result, a PTF record closed under v5.2 may not transmit after v5.3 is installed. (Before a PTF record is transmitted, it is processed through the edit checker one additional time.)

If the record is not transmitted and the edit checker does find a problem, the PTF record will be reopened. It will need to be closed and released again under the new edit checks of v5.3.

The PTF Transmission option of the PTF Menu should be used to transmit PTF records. Contact your MAS ADPAC.

2 Get users off system(s).

3 Backup system(s).

4 Disable routine mapping (DSM). Disable journalling.

There is one new global, ^SCE. The ^SCE global contains the OUTPATIENT ENCOUNTER file (#409.68). This global MUST be placed with the appropriate protection assigned to it before running the SDINIT inits. If possible, the ^SCE global should be placed on the same system where most appointments are made.

> **NOTE:** For MSM systems, SET ^SCE="" on the desired system and then use %GCH to set proper protection on the new global.

5 Sign into UCI where package is to be loaded.

(Use 28k partition for MSM)

6 Review queued jobs to avoid possible delays or conflicts.

7 Sites who wish to delete PIMS routines prior to loading should do so now. The PIMS namespaces are DPT, DG, SD, and VA.

> **IMPORTANT:** Do not delete the following routines.

PRCA\* routines distributed with prior versions of MAS.

DGCR\* routines used for Integrated Billing.

DGYE\* routines required for External Peer Review.

DGYP\* routines for PIMS v5.3 Pre-Packet.

DGYA\* routines used for CPT update.

VAQ\* routines used by Patient Data Exchange - PDX.

VAMP\* routines used by Minimal Patient Dataset - MPD.

A1B2\* routines used for ODS package.

Load PIMS v5.3 tape.

(See PIMS Routine List Section for distributed routine list.)

8 Verify that DUZ, DT, DTIME, and U are defined and DUZ(0)="@". DUZ variable must be defined as an active user number and DUZ(0) variable must equal "@" in order to initialize.

9 Please answer all initialization questions carefully.

We strongly recommend you say NO to all "Want my data merged with yours?" and "Want my data to overwrite yours?" questions during the DPTINIT, DGINIT, and SDINIT processes. These files are only sent with data for those sites installing in a virgin account. Time estimates are based on our recommendation that NO be answered to all of these questions. We also recommend you slave print the initialization processes. Data that is printed out during the post-inits should be reviewed.

10 D ^VALMINIT - List Manager

(See List Manager Installation Dialogues Section.)

11 D ^DPTINIT - Patient File Module

Please answer all questions carefully. Answer NO to all "Want my data merged with yours?" questions. Follow PIMS Installation Dialogues Section, \#1 for DPTINIT responses.

12 D ^DGINIT - Registration/ADT/IRT/PTF/BT Modules

Answer NO to all "Want my data merged with yours?" and "Want my data to overwrite yours?" questions. Follow PIMS Installation Dialogues Section, \#2, for DGINIT responses.

13 D ^SDINIT - Scheduling Module

Answer NO to all "Want my data merged with yours?" and "Want my data to overwrite yours?" questions.

The ^SCE global MUST be placed with the appropriate protection before the inits can be run.

Follow PIMS Installation Dialogues Section, \#3, for SDINIT responses.

14 Delete appropriate routines such as DPTIN\*, DGINI\*, SDINI\*, DGON\* and

SDON\*. However, do NOT delete DPTINITY, DGINITY, and SDINITY. In addition, you may use DEL^DGVPT1 to delete all routines that are obsolete with this release.

15 Move PIMS routines to all systems.

16 Move Other Packages' Routines

Move the IB, DVB, and XQOR\* routines mentioned in the PIMS Package Integration Section of this install guide to all CPUs.

17 Recompile all templates and file cross-references on all CPUs using the same routine size. These routines can be moved to other systems by tape or other sequential medium.

D ALL^DGUTL1 for PIMS templates and file cross-references.

18 Rebuild Map Set.

We recommend the following PIMS routines be mapped.

> DG10\* DGINP DGINPW DGLOCK\* DGMTR

> DGMTA\* DGMTDD\* DGMTE\* DGMTP\* DGMTSC\*

> DGMTU\* DGMTX\* DGPMDD DGPMDD1 DGPMDD2

> DGPMDDCN DGPMLOS DGPMV\* DGPTF DGPTF1

> DGPTF2 DGPTF4\* DGPTFD DGPTFJ DGPTFTR

> DGPTICD DGPTR\* DGPTSU\* DGPTTS\* DGREG\*

> DGRP\* DGSEC DGUTL DPTDUP DPTLK\*

> SDDIV SDROUT\* VADPT\* DGPTX\* SDM\*

> DGPMX\* DGPMBS\* DGPMGL\* SDACS\* SDBT\*

> SDM1T\* SDX\* DGJX\* DGRPDD1 SDAM\*

> SDUL\* SDCO\* SDVSIT\* DGMTCOR DGMTCOU\*

> VAFEDCAP VAFEDG

The following routines are obsolete with PIMS v5.3 and were previously recommended for mapping: none for this release. For a complete list of obsolete routines, please see the PIMS Release Notes.

19 Bring systems back on line.

20 (Optional) Running the Build Primary Menu Trees option on the Menu Management Menu after the install may improve system performance during the first day of operation.

21 D EN^DGV53PTS to convert the OPTION/PROTOCOL USED field (#3) of the DATE/TIME RECORD ACCESSED multiple (#50) of the DG SECURITY LOG file (#38.1).

This field previously pointed to the OPTION file. However, if a restricted patient record was accessed using a protocol, the protocol used was not recorded. The field has been changed to free-text. This conversion will change all the pointers to option's MENU TEXT. At the end of the process, a MailMan message will be sent to the user indicating that the conversion has completed.

22 Please see the following chart for package initialization time estimates for the installation times of PIMS v5.3 at our test sites.

> MSMVAX

> VALMINIT 2 min. 3 min.

> DPTINIT 3 min. 6 min.

> DGINIT 5 hours 6 hours

> SDINIT 8 min. 6 min.

PIMS Installation Dialogues

1\. DPTINIT Sample

\>D ^DPTINIT

This version (#5.3) of 'DPTINIT' was created on 08-JUN-1993

(at ALBANY ISC VAX DEVELOPMENT, by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

I AM GOING TO SET UP THE FOLLOWING FILES:

2 PATIENT

> **NOTE:** You already have the 'PATIENT' File.

5 STATE (including data)

> **NOTE:** You already have the 'STATE' File.

Want my data merged with yours? NO

48 MAS RELEASE NOTES (including data)

> **NOTE:** You already have the 'MAS RELEASE NOTES' File.

I will OVERWRITE your data with mine.

48.5 MAS MODULE (including data)

> **NOTE:** You already have the 'MAS MODULE' File.

I will OVERWRITE your data with mine.

391 TYPE OF PATIENT (including data)

> **NOTE:** You already have the 'TYPE OF PATIENT' File.

Want my data merged with yours? NO

SHALL I WRITE OVER FILE SECURITY CODES? NO// (NO)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

...HMMM, I'M WORKING AS FAST AS I CAN.........................................

..............................................................................

..............................................................................

........................

Compiling DG CONSISTENCY CHECKER input template of File 2...

'DGRPXC' ROUTINE FILED..

'DGRPXC1' ROUTINE FILED

Compiling DG LOAD EDIT SCREEN 7 input template of File 2...

'DGRPXX7' ROUTINE FILED........

'DGRPXX71' ROUTINE FILED...

'DGRPXX72' ROUTINE FILED..

'DGRPXX73' ROUTINE FILED....

'DGRPXX74' ROUTINE FILED....

'DGRPXX75' ROUTINE FILED..

'DGRPXX77' ROUTINE FILED.

'DGRPXX76' ROUTINE FILED..

'DGRPXX78' ROUTINE FILED

Compiling DGRP COLLATERAL REGISTER input template of File 2..

'DGRPXCR' ROUTINE FILED.

'DGRPXCR1' ROUTINE FILED

NO SECURITY-CODE PROTECTION HAS BEEN MADE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Changing name of 'IRT TYPE OF RECORD' file (#393.3)

to 'IRT TYPE OF DEFICIENCY'...

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Initialization of Version 5.3 of DPT Complete.

2\. DGINIT Sample

\>D ^DGINIT

This version (#5.3) of 'DGINIT' was created on 08-JUN-1993

(at ALBANY ISC VAX DEVELOPMENT, by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

At this point, a number of environmental checks are made (e.g., whether the CopayExemption patches are loaded and if the FileMan compiled routine size parameter isset to 4000 or greater).

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Checking IRT parameters needed for IRT conversion in the post-init!

\*\*\*ALL IRT PARAMETERS ARE UPDATED!

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

I AM GOING TO SET UP THE FOLLOWING FILES:

8 ELIGIBILITY CODE (including data)

> **NOTE:** You already have the 'ELIGIBILITY CODE' File.

Want my data merged with yours? NO

8.1 MAS ELIGIBILITY CODE (including data)

> **NOTE:** You already have the 'MAS ELIGIBILITY CODE' File.

I will OVERWRITE your data with mine.

8.2 IDENTIFICATION FORMAT (including data)

> **NOTE:** You already have the 'IDENTIFICATION FORMAT' File.

I will MERGE your data with mine.

10 RACE (including data)

> **NOTE:** You already have the 'RACE' File.

Want my data merged with yours? NO

11 MARITAL STATUS (including data)

> **NOTE:** You already have the 'MARITAL STATUS' File.

Want my data merged with yours? NO

13 RELIGION (including data)

> **NOTE:** You already have the 'RELIGION' File.

Want my data merged with yours? NO

21 PERIOD OF SERVICE (including data)

> **NOTE:** You already have the 'PERIOD OF SERVICE' File.

Want my data merged with yours? NO

22 POW PERIOD (including data)

> **NOTE:** You already have the 'POW PERIOD' File.

Want my data to overwrite yours? NO

23 BRANCH OF SERVICE (including data)

> **NOTE:** You already have the 'BRANCH OF SERVICE' File.

Want my data merged with yours? NO

25 TYPE OF DISCHARGE (including data)

> **NOTE:** You already have the 'TYPE OF DISCHARGE' File.

Want my data merged with yours? NO

30 DISPOSITION LATE REASON (including data)

> **NOTE:** You already have the 'DISPOSITION LATE REASON' File.

Want my data to overwrite yours? NO

35 OTHER FEDERAL AGENCY (including data)

> **NOTE:** You already have the 'OTHER FEDERAL AGENCY' File.

Want my data merged with yours? NO

36 INSURANCE COMPANY

> **NOTE:** You already have the 'INSURANCE COMPANY' File.

37 DISPOSITION (including data)

> **NOTE:** You already have the 'DISPOSITION' File.

I will OVERWRITE your data with mine.

38.1 DG SECURITY LOG

> **NOTE:** You already have the 'DG SECURITY LOG' File.

38.5 INCONSISTENT DATA

> **NOTE:** You already have the 'INCONSISTENT DATA' File.

38.6 INCONSISTENT DATA ELEMENTS (including data)

> **NOTE:** You already have the 'INCONSISTENT DATA ELEMENTS' File.

I will OVERWRITE your data with mine.

39.1 EMBOSSED CARD TYPE (including data)

> **NOTE:** You already have the 'EMBOSSED CARD TYPE' File.

Want my data merged with yours? NO

39.2 EMBOSSING DATA (including data)

> **NOTE:** You already have the 'EMBOSSING DATA' File.

Want my data merged with yours? NO

39.3 EMBOSSER EQUIPMENT FILE

> **NOTE:** You already have the 'EMBOSSER EQUIPMENT FILE' File.

40.8 MEDICAL CENTER DIVISION

> **NOTE:** You already have the 'MEDICAL CENTER DIVISION' File.

41.1 SCHEDULED ADMISSION

> **NOTE:** You already have the 'SCHEDULED ADMISSION' File.

41.9 CENSUS

> **NOTE:** You already have the 'CENSUS' File.

42 WARD LOCATION

> **NOTE:** You already have the 'WARD LOCATION' File.

42.4 SPECIALTY (including data)

> **NOTE:** You already have the 'SPECIALTY' File.

Want my data merged with yours? NO

42.5 WAIT LIST

> **NOTE:** You already have the 'WAIT LIST' File.

42.55 PRIORITY GROUPING (including data)

> **NOTE:** You already have the 'PRIORITY GROUPING' File.

Want my data to overwrite yours? NO

42.6 AMIS 334-341

> **NOTE:** You already have the 'AMIS 334-341' File.

42.7 AMIS 345&346

> **NOTE:** You already have the 'AMIS 345&346' File.

43 MAS PARAMETERS

> **NOTE:** You already have the 'MAS PARAMETERS' File.

43.1 MAS EVENT RATES

> **NOTE:** You already have the 'MAS EVENT RATES' File.

43.11 MAS AWARD (including data)

> **NOTE:** You already have the 'MAS AWARD' File.

Want my data to overwrite yours? NO

43.4 VA ADMITTING REGULATION (including data)

> **NOTE:** You already have the 'VA ADMITTING REGULATION' File.

Want my data to overwrite yours? NO

43.5 G&L CORRECTIONS

> **NOTE:** You already have the 'G&L CORRECTIONS' File.

43.61 G&L TYPE OF CHANGE (including data)

I will OVERWRITE your data with mine.

43.7 ADT TEMPLATE (including data)

> **NOTE:** You already have the 'ADT TEMPLATE' File.

Want my data to overwrite yours? NO

45 PTF

> **NOTE:** You already have the 'PTF' File.

45.1 SOURCE OF ADMISSION (including data)

> **NOTE:** You already have the 'SOURCE OF ADMISSION' File.

I will OVERWRITE your data with mine.

45.2 PTF TRANSFERRING FACILITY

> **NOTE:** You already have the 'PTF TRANSFERRING FACILITY' File.

45.3 SURGICAL SPECIALTY (including data)

> **NOTE:** You already have the 'SURGICAL SPECIALTY' File.

Want my data merged with yours? NO

45.4 PTF DIALYSIS TYPE (including data)

> **NOTE:** You already have the 'PTF DIALYSIS TYPE' File.

Want my data merged with yours? NO

45.5 PTF MESSAGE

> **NOTE:** You already have the 'PTF MESSAGE' File.

45.6 PLACE OF DISPOSITION (including data)

> **NOTE:** You already have the 'PLACE OF DISPOSITION' File.

Want my data merged with yours? NO

45.61 PTF ABUSED SUBSTANCE (including data)

> **NOTE:** You already have the 'PTF ABUSED SUBSTANCE' File.

I will OVERWRITE your data with mine.

45.62 PTF ARCHIVE/PURGE HISTORY FILE

45.64 PTF AUSTIN ERROR CODES (including data)

I will OVERWRITE your data with mine.

45.7 FACILITY TREATING SPECIALTY

> **NOTE:** You already have the 'FACILITY TREATING SPECIALTY' File.

45.81 STATION TYPE (including data)

> **NOTE:** You already have the 'STATION TYPE' File.

Want my data merged with yours? NO

45.82 CATEGORY OF BENEFICIARY (including data)

> **NOTE:** You already have the 'CATEGORY OF BENEFICIARY' File.

Want my data merged with yours? NO

45.83 PTF RELEASE

> **NOTE:** You already have the 'PTF RELEASE' File.

45.84 PTF CLOSE OUT

> **NOTE:** You already have the 'PTF CLOSE OUT' File.

45.85 CENSUS WORKFILE

> **NOTE:** You already have the 'CENSUS WORKFILE' File.

45.86 PTF CENSUS DATE

> **NOTE:** You already have the 'PTF CENSUS DATE' File.

45.87 PTF TRANSACTION REQUEST LOG

> **NOTE:** You already have the 'PTF TRANSACTION REQUEST LOG' File.

45.88 PTF EXPANDED CODE CATEGORY (including data)

> **NOTE:** You already have the 'PTF EXPANDED CODE CATEGORY' File.

I will OVERWRITE your data with mine.

45.89 PTF EXPANDED CODE (including data)

> **NOTE:** You already have the 'PTF EXPANDED CODE' File.

I will OVERWRITE your data with mine.

45.9 PAF

> **NOTE:** You already have the 'PAF' File.

45.91 RUG-II

> **NOTE:** You already have the 'RUG-II' File.

47 MAS FORMS AND SCREENS (including data)

> **NOTE:** You already have the 'MAS FORMS AND SCREENS' File.

I will OVERWRITE your data with mine.

81 CPT

> **NOTE:** You already have the 'CPT' File.

81.1 CPT CATEGORY (including data)

> **NOTE:** You already have the 'CPT CATEGORY' File.

Want my data to overwrite yours? NO

81.2 CPT COPYRIGHT (including data)

> **NOTE:** You already have the 'CPT COPYRIGHT' File.

I will OVERWRITE your data with mine.

389.9 STATION NUMBER (TIME SENSITIVE)

> **NOTE:** You already have the 'STATION NUMBER (TIME SENSITIVE)' File.

391.1 AMIS SEGMENT

> **NOTE:** You already have the 'AMIS SEGMENT' File.

392 BENEFICIARY TRAVEL CLAIM

> **NOTE:** You already have the 'BENEFICIARY TRAVEL CLAIM' File.

392.1 BENEFICIARY TRAVEL DISTANCE

> **NOTE:** You already have the 'BENEFICIARY TRAVEL DISTANCE' File.

392.2 BENEFICIARY TRAVEL CERTIFICATION

> **NOTE:** You already have the 'BENEFICIARY TRAVEL CERTIFICATION' File.

392.3 BENEFICIARY TRAVEL ACCOUNT (including data)

> **NOTE:** You already have the 'BENEFICIARY TRAVEL ACCOUNT' File.

Want my data to overwrite yours? NO

392.4 BENEFICIARY TRAVEL MODE OF TRANSPORTATION

> **NOTE:** You already have the 'BENEFICIARY TRAVEL MODE OF TRANSPORTATION'

File.

393 INCOMPLETE RECORDS

> **NOTE:** You already have the 'INCOMPLETE RECORDS' File.

393.1 MAS SERVICE (including data)

> **NOTE:** You already have the 'MAS SERVICE' File.

I will OVERWRITE your data with mine.

391.51 PIMS EDR EVENT

393.2 IRT STATUS (including data)

> **NOTE:** You already have the 'IRT STATUS' File.

I will OVERWRITE your data with mine.

393.3 IRT TYPE OF DEFICIENCY (including data)

> **NOTE:** You already have the 'IRT TYPE OF DEFICIENCY' File.

I will MERGE your data with mine.

393.41 TYPE OF CATEGORY (including data)

I will OVERWRITE your data with mine.

405 PATIENT MOVEMENT

> **NOTE:** You already have the 'PATIENT MOVEMENT' File.

405.1 FACILITY MOVEMENT TYPE (including data)

> **NOTE:** You already have the 'FACILITY MOVEMENT TYPE' File.

Want my data merged with yours? NO

405.2 MAS MOVEMENT TYPE (including data)

> **NOTE:** You already have the 'MAS MOVEMENT TYPE' File.

I will OVERWRITE your data with mine.

405.3 MAS MOVEMENT TRANSACTION TYPE (including data)

> **NOTE:** You already have the 'MAS MOVEMENT TRANSACTION TYPE' File.

I will OVERWRITE your data with mine.

405.4 ROOM-BED

> **NOTE:** You already have the 'ROOM-BED' File.

405.5 MAS OUT-OF-SERVICE (including data)

> **NOTE:** You already have the 'MAS OUT-OF-SERVICE' File.

I will OVERWRITE your data with mine.

405.6 ROOM-BED DESCRIPTION

> **NOTE:** You already have the 'ROOM-BED DESCRIPTION' File.

406.41 LODGING REASON (including data)

> **NOTE:** You already have the 'LODGING REASON' File.

I will MERGE your data with mine.

407.7 TRANSMISSION ROUTERS (including data)

> **NOTE:** You already have the 'TRANSMISSION ROUTERS' File.

Want my data merged with yours? NO

408 DISCRETIONARY WORKLOAD

> **NOTE:** You already have the 'DISCRETIONARY WORKLOAD' File.

408.11 RELATIONSHIP (including data)

> **NOTE:** You already have the 'RELATIONSHIP' File.

I will OVERWRITE your data with mine.

408.12 PATIENT RELATION

> **NOTE:** You already have the 'PATIENT RELATION' File.

408.13 INCOME PERSON

> **NOTE:** You already have the 'INCOME PERSON' File.

408.21 INDIVIDUAL ANNUAL INCOME

> **NOTE:** You already have the 'INDIVIDUAL ANNUAL INCOME' File.

408.22 INCOME RELATION

> **NOTE:** You already have the 'INCOME RELATION' File.

408.31 ANNUAL MEANS TEST

> **NOTE:** You already have the 'ANNUAL MEANS TEST' File.

408.32 MEANS TEST STATUS (including data)

> **NOTE:** You already have the 'MEANS TEST STATUS' File.

I will OVERWRITE your data with mine.

408.33 TYPE OF TEST (including data)

> **NOTE:** You already have the 'TYPE OF TEST' File.

I will OVERWRITE your data with mine.

408.41 MEANS TEST CHANGES

> **NOTE:** You already have the 'MEANS TEST CHANGES' File.

408.42 MEANS TEST CHANGES TYPE (including data)

> **NOTE:** You already have the 'MEANS TEST CHANGES TYPE' File.

I will OVERWRITE your data with mine.

SHALL I WRITE OVER FILE SECURITY CODES? NO// (NO)

> **NOTE:** This package also contains BULLETINS

SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains FUNCTIONS

SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Saving times for queued jobs...will be restored in post-init to original

values..

'DG G&L RECALCULATION AUTO'....Queued to run : JAN 28,1993@00:11:34

Device for Output : NONE SELECTED

Rescheduling Freq. : 24H

'DG RUG BACKGROUND JOB'........Queued to run : JAN 27,1993@23:50

Device for Output : A74

Rescheduling Freq. : 1D

'DG RUG SEMI ANNUAL - TASKED'..Queued to run : APR 2,1993@00:30

Device for Output : A113

Rescheduling Freq. : 6M

'DG PTF BACKGROUND JOB'........Queued to run : JAN 28,1993@01:30

Device for Output : NONE SELECTED

Rescheduling Freq. : 1D

'DGJ IRT UPDATE (Background)'..No such option on file...

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> The current data dictionary for the BENEFICIARY TRAVEL DISTANCE

file (#392.1) is being removed in order to delete the Mileage

identifier before the new data dictionary is installed.

\>\>\> Completed.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Deleting PTF EXPANDED CODE file (#45.89).

The PTF EXPANDED CODE file (#45.89) will be re-installed

during the init process.

\>\>\> Completed.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

...SORRY, LET ME THINK ABOUT THAT A MOMENT....................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

........................................................................

Compiling Cross-Reference routine.............

...SORRY, THIS MAY TAKE A FEW MOMENTS...

DGPTXX1 routine filed

DGPTXX2 routine filed

DGPTXX3 routine filed

DGPTXX4 routine filed

DGPTXX5 routine filed

DGPTXX6 routine filed

DGPTXX7 routine filed

DGPTXX8 routine filed

DGPTXX9 routine filed

DGPTXX10 routine filed

DGPTXX routine filed.................

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

DGPMXX1 routine filed

DGPMXX2 routine filed

DGPMXX3 routine filed

DGPMXX routine filed.....

Compiling Cross-Reference routine.............

...SORRY, I'M WORKING AS FAST AS I CAN...

DGMTXX11 routine filed

DGMTXX12 routine filed

DGMTXX1 routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, JUST A MOMENT PLEASE...

DGMTXX21 routine filed

DGMTXX22 routine filed

DGMTXX2 routine filed

Compiling Cross-Reference routine.............

...HMMM, I'M WORKING AS FAST AS I CAN...

DGMTXX31 routine filed

DGMTXX32 routine filed

DGMTXX3 routine filed........

'DG CONSISTENCY' BULLETIN FILED -- Remember to add mail groups for new

bulletins

'DG EMBOSSER' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'DG EMBOSSER1' BULLETIN FILED -- Remember to add mail groups for new

bulletins.

'DG SENSITIVITY' BULLETIN FILED -- Remember to add mail groups for new bulletins

'DG UNVERIFIED ELIG' BULLETIN FILED -- Remember to add mail groups for new bulletins.....................................................................

..............................................................................

..............................................................................

..............................................................

'DG ABSENCE OUTPUT' Option Filed

'DG ADMIT PATIENT' Option Filed

'DG AMIS 334-341' Option Filed

'DG AMIS 345-346' Option Filed

'DG AMIS 400 PENDING' Option Filed

'DG AMIS 401-420' Option Filed

'DG AMIS REPORTS' Option Filed

'DG ASIH LIST' Option Filed

'DG BED AVAILABILITY' Option Filed

'DG BED CONTROL' Option Filed

'DG BED CONTROL EXTENDED' Option Filed

'DG BED CONTROL MOVEMENT EDIT' Option Filed

'DG BED SWITCH' Option Filed

'DG BULLETIN LOCAL' Option Filed

'DG CO-PAY TEST ADD' Option Filed

'DG CO-PAY TEST DELETE' Option Filed

'DG CO-PAY TEST EDIT' Option Filed

'DG CO-PAY TEST FUTURE LIST' Option Filed

'DG CO-PAY TEST INCOMPLETE' Option Filed

'DG CO-PAY TEST SUPERVISOR MENU' Option Filed

'DG CO-PAY TEST USER MENU' Option Filed

'DG CO-PAY TEST VIEW EDITING' Option Filed

'DG CO-PAY TEST VIEW TEST' Option Filed

'DG COLLATERAL PATIENT' Option Filed

'DG CONSISTENCY CHECK' Option Filed

'DG CONSISTENCY PATIENT' Option Filed

'DG CONSISTENCY PRINT' Option Filed

'DG CONSISTENCY PURGE' Option Filed

'DG CONSISTENCY REBUILD' Option Filed

'DG CONSISTENCY SUPERVISOR MENU' Option Filed

'DG CONSISTENCY UPDATE' Option Filed

'DG DEATH ENTRY' Option Filed

'DG DEVICE SELECTION' Option Filed

'DG DISCHARGE PATIENT' Option Filed

'DG DISPOSITION APPLICATION' Option Filed

'DG DISPOSITION EDIT' Option Filed

'DG DISPOSITION LOG' Option Filed

'DG DISPOSITION OUTPUT MENU' Option Filed

'DG DISPOSITION SUMMARY' Option Filed

'DG DISPOSITION TIME STATS' Option Filed

'DG DRG CALCULATION' Option Filed

'DG DRG TRIM POINT ENTRY' Option Filed

'DG ELIG CODE ENTER/EDIT' Option Filed

'DG ELIG ID FORMAT EDIT' Option Filed

'DG ELIG ID FORMAT RESET' Option Filed

'DG ELIG ID RESET' Option Filed

'DG ELIG MAINTENANCE' Option Filed

'DG ELIG PRI ELIG RESET' Option Filed

'DG ELIG RESET ALL' Option Filed

'DG ELIG RESET PATIENT' Option Filed

'DG ELIGIBILITY VERIFICATION' Option Filed

'DG FEMALE CURRENT INPT LIST' Option Filed

'DG FEMALE HISTORICAL' Option Filed

'DG G&L CHANGES VIEW' Option Filed

'DG G&L INIT' Option Filed

'DG G&L RECALC' Option Filed

'DG G&L RECALCULATION AUTO' Option Filed

'DG G&L SHEET' Option Filed

'DG GECS BATCH' Option Filed

'DG GECS BATCH EDIT' Option Filed

'DG GECS BATCH MENU' Option Filed

'DG GECS BATCHES STATUS' Option Filed

'DG GECS BATCHES WAITING TRANS' Option Filed

'DG GECS CODE EDIT' Option Filed

'DG GECS CREATE' Option Filed

'DG GECS DELETE' Option Filed

'DG GECS GENERATE' Option Filed

'DG GECS KEYPUNCH' Option Filed

'DG GECS MAIN MENU' Option Filed

'DG GECS PRINT' Option Filed

'DG GECS PURGE' Option Filed

'DG GECS READY FOR BATCH LIST' Option Filed

'DG GECS REBATCH' Option Filed

'DG GECS RETRANSMIT' Option Filed

'DG GECS REVIEW CODE SHEET' Option Filed

'DG GECS TRANSMIT' Option Filed

'DG GECS TRANSMIT MENU' Option Filed

'DG GECS USER MENU' Option Filed

'DG INPATIENT HISTORICAL' Option Filed

'DG INPATIENT INQUIRY EXTENDED' Option Filed

'DG INPATIENT LIST' Option Filed

'DG INPATIENT REPORTS' Option Filed

'DG INPATIENT ROSTER' Option Filed

'DG INSTITUTION EDIT' Option Filed

'DG INSURANCE COMPANY EDIT' Option Filed

'DG INSURANCE LIST' Option Filed

'DG INTEGRITY CHECKER' Option Filed

'DG LOAD PATIENT DATA' Option Filed

'DG MANAGER MENU' Option Filed

'DG MEANS TEST ADD' Option Filed

'DG MEANS TEST ADJUDICATE' Option Filed

'DG MEANS TEST AUDIT' Option Filed

'DG MEANS TEST CHANGE' Option Filed

'DG MEANS TEST COMPLETE' Option Filed

'DG MEANS TEST DEDUCTIBLE' Option Filed

'DG MEANS TEST DELETE' Option Filed

'DG MEANS TEST EDIT' Option Filed

'DG MEANS TEST EVENTS' Option Filed

'DG MEANS TEST FUTURE LIST' Option Filed

'DG MEANS TEST HARDSHIP REVIEW' Option Filed

'DG MEANS TEST OUTPUTS' Option Filed

'DG MEANS TEST PREV THRESHOLD' Option Filed

'DG MEANS TEST REQUIRED' Option Filed

'DG MEANS TEST SUPERVISOR MENU' Option Filed

'DG MEANS TEST THRESHOLD EDIT' Option Filed

'DG MEANS TEST USER MENU' Option Filed

'DG MEANS TEST VIEW EDITING' Option Filed

'DG MEANS TEST VIEW TEST' Option Filed

'DG OERR TREATING TRANSFER' Option Filed

'DG OUTPUTS MENU' Option Filed

'DG PARAMETER ENTRY' Option Filed

'DG PATIENT ELIGIBILITY INQUIRY' Option Filed

'DG PATIENT INQUIRY' Option Filed

'DG PATIENT TYPE PARAMETER EDIT' Option Filed

'DG PT EXPANDED CODE LIST' Option Filed

'DG PTF 099 TRANSMISSION' Option Filed

'DG PTF BACKGROUND JOB' Option Filed

'DG PTF BATCH REPORTS' Option Filed

'DG PTF BREAK EVEN ENTER' Option Filed

'DG PTF BREAKEVEN' Option Filed

'DG PTF CODING CLERK REPORT' Option Filed

'DG PTF CODING REPORT' Option Filed

'DG PTF COMPREHENSIVE INQUIRY' Option Filed

'DG PTF COMPREHENSIVE REPORT' Option Filed

'DG PTF CREATE' Option Filed

'DG PTF DELETE' Option Filed

'DG PTF DRG ALOS' Option Filed

'DG PTF DRG INDEX' Option Filed

'DG PTF DRG INFORMATION OUTPUT' Option Filed

'DG PTF DRG REPORTS' Option Filed

'DG PTF FEE BASIS ADD' Option Filed

'DG PTF FREQUENCY REPORT' Option Filed

'DG PTF ICD DIAGNOSTIC SEARCH' Option Filed

'DG PTF ICD SURGICAL SEARCH' Option Filed

'DG PTF MEANS TEST OF 'U'' Option Filed

'DG PTF MENU' Option Filed

'DG PTF MESSAGE CHECK' Option Filed

'DG PTF MESSAGE ENTER' Option Filed

'DG PTF MESSAGE INQUIRE' Option Filed

'DG PTF MOVE TRIM' Option Filed

'DG PTF NO ADMISSION' Option Filed

'DG PTF OPEN CLOSED RECORD' Option Filed

'DG PTF OPEN RECORD LIST' Option Filed

'DG PTF OPEN RECORD OUTPUT' Option Filed

'DG PTF OPEN RELEASED' Option Filed

'DG PTF OUTPUT MENU' Option Filed

'DG PTF PURGE BREAKEVEN' Option Filed

'DG PTF QUICK LOAD' Option Filed

'DG PTF RAM COST ENTRY' Option Filed

'DG PTF RELEASE RECORD' Option Filed

'DG PTF SCREEN' Option Filed

'DG PTF SUMMARY DIAG/OP OUTPUT' Option Filed

'DG PTF TRANSMISSION VADATS' Option Filed

'DG PTF TRANSMITTED RECORDS' Option Filed

'DG PTF TRIM REPORT' Option Filed

'DG PTF UPDATE DRG INFO' Option Filed

'DG PTF UPDATE TRANSFER DRG'S' Option Filed

'DG PTF VALIDITY CHECK' Option Filed

'DG REGISTER PATIENT' Option Filed

'DG REGISTRATION 10/10 REPRINT' Option Filed

'DG REGISTRATION DELETE' Option Filed

'DG REGISTRATION MENU' Option Filed

'DG REGISTRATION VIEW' Option Filed

'DG RELEASE COMMENTS' Option Filed

'DG RELEASE NOTES' Option Filed

'DG RELIGION LIST' Option Filed

'DG RUG BACKGROUND JOB' Option Filed

'DG RUG CLOSE' Option Filed

'DG RUG CREATE' Option Filed

'DG RUG DELETE' Option Filed

'DG RUG ENTER/EDIT' Option Filed

'DG RUG GROUPER' Option Filed

'DG RUG INCOMPLETE' Option Filed

'DG RUG INDEX' Option Filed

'DG RUG MENU' Option Filed

'DG RUG OPEN' Option Filed

'DG RUG OUTPUTS' Option Filed

'DG RUG PAI RANGE' Option Filed

'DG RUG PAI SINGLE' Option Filed

'DG RUG SEMI ANNUAL - TASKED' Option Filed

'DG RUG SEMI ANNUAL BGJ' Option Filed

'DG RUG STATUS' Option Filed

'DG RUG TEST GROUPER' Option Filed

'DG RUG TRANSMISSION' Option Filed

'DG RUG WWU' Option Filed

'DG SCHED ADMIT' Option Filed

'DG SCHED ADMIT CANCEL' Option Filed

'DG SCHED ADMIT ENTRY' Option Filed

'DG SCHED ADMIT PRINT' Option Filed

'DG SCHED ADMIT PURGE' Option Filed

'DG SCHED ADMIT STATS' Option Filed

'DG SECURITY DISPLAY LOG' Option Filed

'DG SECURITY ENTER/EDIT' Option Filed

'DG SECURITY OFFICER MENU' Option Filed

'DG SECURITY PURGE LOG' Option Filed

'DG SECURITY PURGE PATIENTS' Option Filed

'DG SERIOUSLY ILL ENTRY' Option Filed

'DG SERIOUSLY ILL LIST' Option Filed

'DG SHOW STATUS' Option Filed

'DG SUPERVISOR MENU' Option Filed

'DG SYSTEM DEFINITION MENU' Option Filed

'DG TEMPLATE LOCAL' Option Filed

'DG THIRD PARTY ADMIT REVIEW' Option Filed

'DG THIRD PARTY OUTPUT MENU' Option Filed

'DG THIRD PARTY PATIENT REVIEW' Option Filed

'DG THIRD PARTY REIMBURSEMENT' Option Filed

'DG TRANSFER PATIENT' Option Filed

'DG TRANSMISSION ROUTER EDIT' Option Filed

'DG TREATING PRINT' Option Filed

'DG TREATING SETUP' Option Filed

'DG TREATING TRANSFER' Option Filed

'DG VBC ADMISSION' Option Filed

'DG VBC MENU' Option Filed

'DG VBC PATIENT' Option Filed

'DG WAITING LIST DELETE' Option Filed

'DG WAITING LIST ENTRY' Option Filed

'DG WAITING LIST PRINT' Option Filed

'DG WARD DEFINITION' Option Filed

'DGBT BENE TRAVEL ACCOUNT' Option Filed

'DGBT BENE TRAVEL CERTIFICATION' Option Filed

'DGBT BENE TRAVEL DISTANCES' Option Filed

'DGBT BENE TRAVEL MENU' Option Filed

'DGBT BENE TRAVEL RATES' Option Filed

'DGBT BENE TRAVEL REPORT' Option Filed

'DGBT BENE TRAVEL REPRINT' Option Filed

'DGBT BENE TRAVEL SCREEN' Option Filed

'DGBT BENE TRAVEL VIEW' Option Filed

'DGJ ADD/EDIT DEFICIENCY' Option Filed

'DGJ INCOMPLETE EVENT' Option Filed

'DGJ IRT DELETE' Option Filed

'DGJ IRT EDITCOMP' Option Filed

'DGJ IRT ENTER/EDIT' Option Filed

'DGJ IRT INCOMPLETE' Option Filed

'DGJ IRT MENU' Option Filed

'DGJ IRT PARAMETERS' Option Filed

'DGJ IRT PRINT' Option Filed

'DGJ IRT TRANS PROD' Option Filed

'DGJ IRT UNDICTATED' Option Filed

'DGJ IRT UPDATE (Background)' Option Filed

'DGJ IRT UPDATE STD. DEFIC.' Option Filed

'DGJ PHYS DEFICIENCY REPORT' Option Filed

'DGMGR' Option Filed

'DGOERR ADMIT' Option Filed

'DGOERR BED SWITCH' Option Filed

'DGOERR DISCHARGE' Option Filed

'DGOERR NOTE' Option Filed

'DGOERR PATIENT INQUIRY' Option Filed

'DGOERR SCHED ADMIT' Option Filed

'DGOERR TRANSFER' Option Filed

'DGPM BED ENTRY/EDIT' Option Filed

'DGPM CHECK-IN' Option Filed

'DGPM CHECK-OUT' Option Filed

'DGPM CURRENT LODGERS OUTPUT' Option Filed

'DGPM EDIT OOS BEDS' Option Filed

'DGPM G&L PARAMETER EDIT' Option Filed

'DGPM LODGERS FOR DATE RANGE' Option Filed

'DGPM LODGING REASONS ENTRY' Option Filed

'DGPM MOVEMENT EVENTS' Option Filed

'DGPM PATIENT MOVEMENT LIST' Option Filed

'DGPM PROVIDER CHANGE' Option Filed

'DGPM TREATING SPECIALTY EVENT' Option Filed

'DGPM TS INPATIENT INFORMATION' Option Filed

'DGPM WARD OOS EDIT' Option Filed

'DGPT ARCHIVE/PURGE' Option Filed

'DGPT CDR INQUIRY' Option Filed

'DGPT CENSUS 099 TRANSACTION' Option Filed

'DGPT CENSUS CLOSED FOR CENSUS' Option Filed

'DGPT CENSUS CODER' Option Filed

'DGPT CENSUS CODING CLERK RPT' Option Filed

'DGPT CENSUS CODING REPORT' Option Filed

'DGPT CENSUS DATE EDIT' Option Filed

'DGPT CENSUS INQUIRE' Option Filed

'DGPT CENSUS MENU' Option Filed

'DGPT CENSUS OPEN RECORD' Option Filed

'DGPT CENSUS OPEN RELEASED' Option Filed

'DGPT CENSUS OUTPUT MENU' Option Filed

'DGPT CENSUS RECORD REPORT' Option Filed

'DGPT CENSUS REGEN WORKFILE' Option Filed

'DGPT CENSUS RELEASE RECORD' Option Filed

'DGPT CENSUS STATUS REPORT' Option Filed

'DGPT CENSUS SUPERVISOR' Option Filed

'DGPT CENSUS TRANSMIT' Option Filed

'DGPT CENSUS TRANSMITTED' Option Filed

'DGPT CENSUS UNRELEASED' Option Filed

'DGPT SET XMIT FLAG' Option Filed

'DGPT TOOL RPO' Option Filed

'DGPT TOOL TRANSACTION PRINT' Option Filed

'DGPT TOOL TRANSACTION PURGE' Option Filed

'DGPT TOOLS MENU' Option Filed

'DGQE DATA CARD' Option Filed

'DGQE DATA CARD EDIT' Option Filed

'DGQE DATA CARD FREE' Option Filed

'DGQE DATA CARD HOLD' Option Filed

'DGQE DATA CARD Q' Option Filed

'DGQE EDIT EMBOSSER FILES' Option Filed

'DGQE EMBOSSER DEVICE EDIT' Option Filed

'VAFED EDR PROCESS EVENTS' Option Filed......................................

..............................................................................

........................

Compiling DG PTF ADD MESSAGE input template of File 45.5....

'DGPTXMS' ROUTINE FILED

Compiling DG PTF CREATE PTF ENTRY input template of File 45...

'DGPTXC' ROUTINE FILED..

'DGPTXC1' ROUTINE FILED.

'DGPTXC2' ROUTINE FILED

Compiling DG PTF POST CREATE input template of File 45..

'DGPTXCA' ROUTINE FILED

Compiling DG101 input template of File 45......

'DGPTX1' ROUTINE FILED..

'DGPTX11' ROUTINE FILED......

'DGPTX13' ROUTINE FILED....

'DGPTX12' ROUTINE FILED...

'DGPTX14' ROUTINE FILED...

'DGPTX15' ROUTINE FILED...

'DGPTX16' ROUTINE FILED.

'DGPTX17' ROUTINE FILED

Compiling DG401 input template of File 45.

'DGPTX4' ROUTINE FILED.....

'DGPTX41' ROUTINE FILED...

'DGPTX42' ROUTINE FILED..

'DGPTX43' ROUTINE FILED..

'DGPTX44' ROUTINE FILED

Compiling DG501 input template of File 45.

'DGPTX5' ROUTINE FILED...

'DGPTX51' ROUTINE FILED...

'DGPTX52' ROUTINE FILED..

'DGPTX53' ROUTINE FILED..

'DGPTX54' ROUTINE FILED...

'DGPTX55' ROUTINE FILED...

'DGPTX56' ROUTINE FILED.....

'DGPTX57' ROUTINE FILED.

'DGPTX58' ROUTINE FILED

Compiling DG501F input template of File 45.

'DGX5F' ROUTINE FILED...

'DGX5F1' ROUTINE FILED....

'DGX5F2' ROUTINE FILED...

'DGX5F3' ROUTINE FILED..

'DGX5F4' ROUTINE FILED...

'DGX5F5' ROUTINE FILED...

'DGX5F6' ROUTINE FILED.....

'DGX5F7' ROUTINE FILED.

'DGX5F8' ROUTINE FILED

Compiling DG701 input template of File 45...

'DGPTX7' ROUTINE FILED...

'DGPTX71' ROUTINE FILED...

'DGPTX72' ROUTINE FILED..

'DGPTX73' ROUTINE FILED...

'DGPTX74' ROUTINE FILED...

'DGPTX75' ROUTINE FILED.

'DGPTX76' ROUTINE FILED

Compiling DGJ EDIT IRT RECORD input template of File 393...

'DGJXE' ROUTINE FILED....

'DGJXE1' ROUTINE FILED...

'DGJXE2' ROUTINE FILED..

'DGJXE3' ROUTINE FILED...

'DGJXE4' ROUTINE FILED..

'DGJXE5' ROUTINE FILED.

'DGJXE6' ROUTINE FILED...

'DGJXE7' ROUTINE FILED

Compiling DGJ ENTER IRT RECORD input template of File 393.....

'DGJXA' ROUTINE FILED.....

'DGJXA1' ROUTINE FILED..

'DGJXA2' ROUTINE FILED...

'DGJXA3' ROUTINE FILED...

'DGJXA4' ROUTINE FILED..

'DGJXA5' ROUTINE FILED

Compiling DGMT ENTER/EDIT ANNUAL INCOME input template of File 408.21...

'DGMTXI' ROUTINE FILED....

'DGMTXI1' ROUTINE FILED...

'DGMTXI2' ROUTINE FILED

Compiling DGMT ENTER/EDIT COMPLETION input template of File 408.31...

'DGMTXC' ROUTINE FILED......

'DGMTXC1' ROUTINE FILED.....

'DGMTXC2' ROUTINE FILED...

'DGMTXC3' ROUTINE FILED

Compiling DGMT ENTER/EDIT DEPENDENTS input template of File 408.22...

'DGMTXD' ROUTINE FILED..

'DGMTXD1' ROUTINE FILED

Compiling DGMT ENTER/EDIT EXPENSES input template of File 408.21...

'DGMTXE' ROUTINE FILED

Compiling DGMT ENTER/EDIT MARITAL STATUS input template of File 408.22..

'DGMTXM' ROUTINE FILED..

'DGMTXM1' ROUTINE FILED

Compiling DGMT ENTER/EDIT NET WORTH input template of File 408.21....

'DGMTXN' ROUTINE FILED.

'DGMTXN1' ROUTINE FILED

Compiling DGPM ADMIT input template of File 405.

'DGPMX1' ROUTINE FILED...

'DGPMX11' ROUTINE FILED...

'DGPMX12' ROUTINE FILED....

'DGPMX13' ROUTINE FILED

Compiling DGPM ASIH ADMIT input template of File 405.

'DGPMXAS' ROUTINE FILED...

'DGPMXAS1' ROUTINE FILED.....

'DGPMXAS2' ROUTINE FILED

Compiling DGPM CHECK-IN LODGER input template of File 405.

'DGPMX4' ROUTINE FILED..

'DGPMX41' ROUTINE FILED...

'DGPMX42' ROUTINE FILED..

'DGPMX43' ROUTINE FILED....

'DGPMX44' ROUTINE FILED

Compiling DGPM DISCHARGE input template of File 405.

'DGPMX3' ROUTINE FILED..

'DGPMX31' ROUTINE FILED.....

'DGPMX32' ROUTINE FILED.

'DGPMX33' ROUTINE FILED

Compiling DGPM LODGER CHECK-OUT input template of File 405.

'DGPMX5' ROUTINE FILED..

'DGPMX51' ROUTINE FILED...

'DGPMX52' ROUTINE FILED

Compiling DGPM SPECIALTY TRANSFER input template of File 405.

'DGPMX6' ROUTINE FILED..

'DGPMX61' ROUTINE FILED...

'DGPMX62' ROUTINE FILED...

'DGPMX63' ROUTINE FILED

Compiling DGPM TRANSFER input template of File 405.

'DGPMX2' ROUTINE FILED..

'DGPMX21' ROUTINE FILED...

'DGPMX22' ROUTINE FILED...

'DGPMX23' ROUTINE FILED...

'DGPMX24' ROUTINE FILED..

'DGPMX25' ROUTINE FILED

Compiling DGRP ENTER/EDIT ANNUAL INCOME input template of File 408.21....

'DGRPXIS' ROUTINE FILED....

'DGRPXIS1' ROUTINE FILED..

'DGRPXIS2' ROUTINE FILED

Compiling DGTS input template of File 40.8.

'DGXTS' ROUTINE FILED...

'DGXTS1' ROUTINE FILED.....

'DGXTS2' ROUTINE FILED

Compiling DG PTF PT BRIEF LIST print template of File 45.....

'DGPTXB' ROUTINE FILED.

Compiling DGPT QUICK PROFILE print template of File 45.86................

'DGPTXCP' ROUTINE FILED..

NO SECURITY-CODE PROTECTION HAS BEEN MADE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

This version of 'DGONIT' was created on 08-JUN-1993

(at ALBANY ISC VAX DEVELOPMENT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please............................

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace...

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace...

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace.......

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace...

Located in the DG (REGISTRATION) namespace...

Located in the DG (REGISTRATION) namespace..

Located in the DG (REGISTRATION) namespace..

Located in the IB (INTEGRATED BILLING) namespace.

'DG CO-PAY TEST STATUS' Protocol Filed

'DG MEANS TEST AUDIT' Protocol Filed

'DG MEANS TEST DOM' Protocol Filed

'DG MEANS TEST EVENTS' Protocol Filed

'DG MEANS TEST REQUIRED' Protocol Filed

DG MEANS TEST REQUIRED added as item to SDAM APPOINTMENT EVENTS.

'DG OERR TREATING TRANSFER' Protocol Filed

'DGJ ALL GROUP EDIT' Protocol Filed

'DGJ CHNG PAT' Protocol Filed

'DGJ COMPLETE EDIT MENU' Protocol Filed

DGJ IRT EXP added as item to DGJ COMPLETE EDIT MENU.

DGJ EDIT COMP SUPER2 added as item to DGJ COMPLETE EDIT MENU.

'DGJ DELETE DEFICIENCY' Protocol Filed

'DGJ DELETE MENU' Protocol Filed

DGJ IRT EXP added as item to DGJ DELETE MENU.

DGJ DELETE SUPER2 added as item to DGJ DELETE MENU.

'DGJ DELETE SUPER' Protocol Filed

'DGJ DELETE SUPER2' Protocol Filed

'DGJ EDIT COMP IRT SINGLE' Protocol Filed

'DGJ EDIT COMP IRT SUPER' Protocol Filed

'DGJ EDIT COMP SUPER2' Protocol Filed

'DGJ EDIT SUMMARY/REPORT' Protocol Filed

DGJ DELETE DEFICIENCY added as item to DGJ EDIT SUMMARY/REPORT.

'DGJ ENTER/EDIT DEFICIENCY MENU' Protocol Filed

DGJ IRT EDIT DEFICIENCY added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

DGJ IRT ENTER DEFICIENCY added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

DGJ IRT EXP added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

DGJ CHNG PAT added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

DGJ TS UPDATE added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

DGJ EDIT COMP IRT SUPER added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

DGJ DELETE SUPER added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

DGJ JUMP CATEG added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

DGJ IRT COMPLETE DEF added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

'DGJ ENTER/EDIT RECORDS MENU' Protocol Filed

DGJ IRT EXP added as item to DGJ ENTER/EDIT RECORDS MENU.

DGJ CHNG PAT added as item to DGJ ENTER/EDIT RECORDS MENU.

DGJ IRT ENTER RECORD added as item to DGJ ENTER/EDIT RECORDS MENU.

DGJ IRT EDIT RECORD added as item to DGJ ENTER/EDIT RECORDS MENU.

DGJ TS UPDATE added as item to DGJ ENTER/EDIT RECORDS MENU.

DGJ EDIT COMP IRT SUPER added as item to DGJ ENTER/EDIT RECORDS MENU.

DGJ DELETE SUPER added as item to DGJ ENTER/EDIT RECORDS MENU.

DGJ JUMP CATEG added as item to DGJ ENTER/EDIT RECORDS MENU.

'DGJ GROUP 2 EDIT' Protocol Filed

'DGJ GROUP 3 EDIT' Protocol Filed

'DGJ GROUP 4 EDIT' Protocol Filed

'DGJ INCOMPLETE EVENT' Protocol Filed

'DGJ IRT ADD DEF. PARMS' Protocol Filed

'DGJ IRT COMPLETE DEF' Protocol Filed

'DGJ IRT EDIT DEFICIENCY' Protocol Filed

'DGJ IRT EDIT PARMS' Protocol Filed

'DGJ IRT EDIT RECORD' Protocol Filed

'DGJ IRT ENTER DEFICIENCY' Protocol Filed

'DGJ IRT ENTER RECORD' Protocol Filed

'DGJ IRT EXP' Protocol Filed

'DGJ IRT PARM ENTER/EDIT MENU' Protocol Filed

DGJ IRT ADD DEF. PARMS added as item to DGJ IRT PARM ENTER/EDIT MENU.

DGJ IRT EDIT PARMS added as item to DGJ IRT PARM ENTER/EDIT MENU.

DGJ JUMP CATEG added as item to DGJ IRT PARM ENTER/EDIT MENU.

'DGJ IRT SUMMARIES' Protocol Filed

DGJ EDIT SUMMARY/REPORT added as item to DGJ IRT SUMMARIES.

DGJ GROUP 2 EDIT added as item to DGJ IRT SUMMARIES.

DGJ GROUP 3 EDIT added as item to DGJ IRT SUMMARIES.

DGJ GROUP 4 EDIT added as item to DGJ IRT SUMMARIES.

DGJ ALL GROUP EDIT added as item to DGJ IRT SUMMARIES.

'DGJ JUMP CATEG' Protocol Filed

'DGJ TS UPDATE' Protocol Filed

'DGOERR ADMIT' Protocol Filed

'DGOERR BED SWITCH' Protocol Filed

'DGOERR DISCHARGE' Protocol Filed

'DGOERR NOTE' Protocol Filed

'DGOERR PATIENT INQUIRY' Protocol Filed

'DGOERR SCHED ADMIT' Protocol Filed

'DGOERR TRANSFER' Protocol Filed

'DGPM MOVEMENT EVENTS' Protocol Filed

'DGPM TREATING SPECIALTY EVENT' Protocol Filed

'DGPT A/P ARCHIVE' Protocol Filed

'DGPT A/P EDIT TMP' Protocol Filed

DGPT REMOVE A/P added as item to DGPT A/P EDIT TMP.

DGPT SELECT A/P added as item to DGPT A/P EDIT TMP.

DGPT DETAILED INQUIRY added as item to DGPT A/P EDIT TMP.

'DGPT A/P MAIN' Protocol Filed

DGPT ADD A/P TEMPLATE added as item to DGPT A/P MAIN.

DGPT DEL A/P TEMPLATE added as item to DGPT A/P MAIN.

DGPT EDIT A/P TEMPLATE added as item to DGPT A/P MAIN.

DGPT A/P ARCHIVE added as item to DGPT A/P MAIN.

DGPT A/P PURGE added as item to DGPT A/P MAIN.

'DGPT A/P PURGE' Protocol Filed

'DGPT ADD A/P TEMPLATE' Protocol Filed

'DGPT DEL A/P TEMPLATE' Protocol Filed

'DGPT DETAILED INQUIRY' Protocol Filed

'DGPT EDIT A/P TEMPLATE' Protocol Filed

'DGPT REMOVE A/P' Protocol Filed

'DGPT SELECT A/P' Protocol Filed

'IBDF DELETE GROUP' Protocol Filed

'VAFED EDR INPATIENT CAPTURE' Protocol Filed

'VAFED EDR INPATIENT CAPTURE' added as item to DGPM MOVEMENT EVENTS.

'VAFED EDR OUTPATIENT CAPTURE' Protocol Filed

'VAFED EDR OUTPATIENT CAPTURE' added as item to SDAM APPOINTMENT EVENTS.

'VALM BLANK 1' Protocol Filed

VALM BLANK 1 added as item to DGJ ENTER/EDIT RECORDS MENU.

VALM BLANK 1 added as item to DGJ IRT PARM ENTER/EDIT MENU.

VALM BLANK 1 added as item to DGJ IRT SUMMARIES.

'VALM BLANK 2' Protocol Filed

VALM BLANK 2 added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

VALM BLANK 2 added as item to DGJ ENTER/EDIT RECORDS MENU.

VALM BLANK 2 added as item to DGJ IRT PARM ENTER/EDIT MENU.

VALM BLANK 2 added as item to DGJ IRT SUMMARIES.

'VALM BLANK 3' Protocol Filed

VALM BLANK 3 added as item to DGJ ENTER/EDIT DEFICIENCY MENU.

VALM BLANK 3 added as item to DGJ ENTER/EDIT RECORDS MENU.

VALM BLANK 3 added as item to DGJ IRT PARM ENTER/EDIT MENU.

VALM BLANK 3 added as item to DGJ IRT SUMMARIES.

OK, Protocol Installation is Complete.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> List Template installation...

'DGJ COMP EDIT SINGLE' List Template...Filed.

'DGJ COMP EDIT SUPER' List Template...Filed.

'DGJ DEF EDIT' List Template...Filed.

'DGJ DEFICIENCY LIST' List Template...Filed.

'DGJ DELETE DEFICIENCY' List Template...Filed.

'DGJ DELETE RECORD' List Template...Filed.

'DGJ DELETE SINGLE' List Template...Filed.

'DGJ DELETE SUPER' List Template...Filed.

'DGJ ENTER/EDIT DEF. PARMS.' List Template...Filed.

'DGJ EXP ENTRY' List Template...Filed.

'DGJ IRT REC EDIT' List Template...Filed.

'DGJ IRT REC ENTER' List Template...Filed.

'DGJ IRT RECORD LIST' List Template...Filed.

'DGPT A/P EDIT TEMPLATE' List Template...Filed.

'DGPT A/P MAIN SELECT' List Template...Filed.

'DGPT CLOSE-OUT ERROR' List Template...Filed.

'DGPT DETAILED INQUIRY' List Template...Filed.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Provider Conversion Started on JUN 09, 1993@08:51:52

Files : 2, 41.1, 44, 45, 45.7, 392 and 405

\>\>\> Provider Conversion for the PATIENT (#2) file :

Started on JUN 09, 1993@08:51:52.........................................

..............................................................................

..............................................................................

..............................................................................

...............................................

All entries converted.

\>\>\> Provider Conversion for the PATIENT (#2) file :

Completed on JUN 09, 1993@09:48:54

You will be receiving a Mail Message indicating records whose

monetary benefit amount fields can not be converted into the

TOTAL ANNUAL VA CHECK AMOUNT field

You will be receiving a Mail Message regarding the formatting

of your Claim Folder Location fields in the Patient File.....

\>\>\> Provider Conversion for the PATIENT MOVEMENT (#405) file :

Started on JUN 09, 1993@09:51:35.........................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

............

\>\>\> Provider Conversion for the PATIENT MOVEMENT (#405) file :

Completed on JUN 09, 1993@10:14:08

\>\>\> Provider Conversion for the FACILITY TREATING SPECIALTY (#45.7) file :

Started on JUN 09, 1993@10:14:08

All entries converted.

\>\>\> Provider Conversion for the FACILITY TREATING SPECIALTY (#45.7) file :

Completed on JUN 09, 1993@10:14:09

\>\>\> Provider Conversion for the BENEFICIARY TRAVEL CLAIM (#392) file :

Started on JUN 09, 1993@10:14:09.........................................

..............................................................................

...............................................

All entries converted.

\>\>\> Provider Conversion for the BENEFICIARY TRAVEL CLAIM (#392) file :

Completed on JUN 09, 1993@10:15:11

\>\>\> Provider Conversion for the SCHEDULED ADMISSION (#41.1) file :

Started on JUN 09, 1993@10:15:11............

All entries converted.

\>\>\> Provider Conversion for the SCHEDULED ADMISSION (#41.1) file :

Completed on JUN 09, 1993@10:15:32

\>\>\> Provider Conversion for the PTF (#45) file :

Started on JUN 09, 1993@10:15:32.........................................

..............................................................................

..............................................................................

..............................................................................

All entries converted.

\>\>\> Provider Conversion for the PTF (#45) file :

Completed on JUN 09, 1993@10:26:52

\>\>\> Provider Conversion Completed on JUN 09, 1993@10:26:52

\>\>\> Generating mail message for Provider Conversion.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\*\*\*ALL IRT PARAMETERS ARE UPDATED, THE IRT CONVERSION WILL START!

\>POPULATING THE PHYSICIAN FOR DEFICIENCY FIELD FOR INCOMPLETE

RECORDS TRACKING

\>UPDATING ATTENDING PHYSICIAN IF FACILITY USES ATTENDING PHYSICIAN

AS A DEFAULT

\>\>\>IRT CONVERSION RUNNING.....................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

.............

\>\>\>IRT CONVERSION COMPLETE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Inconsitent Data file clean up started: JUN 9, 1993@10:29:59

\>\>\> Deleting old inconsistencies from Inconsistent Data file.......

\>\>\> Inconsitent Data file clean up complete at JUN 9, 1993@10:30

Elapse time for loop was: 0 Hours, 0 Minutes, 1 Seconds

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Beginning conversion of BENEFICIARY TRAVEL DISTANCE file, (#392.1)

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

\>\>\> Beginning check and conversion

of BENEFICIARY TRAVEL DISTANCE file, (#392.1)

............................................................

\>\>\> BENEFICIARY TRAVEL DISTANCE file (#392.1) conversion complete.

606 Cities in the BENEFICIARY TRAVEL DISTANCE file (#392.1) have been converted.

...EXCUSE ME, HOLD ON...

\>\>\> Re-Indexing BENEFICIARY TRAVEL DISTANCE file (#392.1). This could take awhile.......

\>\>\> Re-Indexing complete.

INCOMPLETE INFORMATION FOUND DURING THE POST-INIT CONVERSION OF THE

BENEFICIARY TRAVEL DISTANCE FILE, (#392.1)

\>\>\> WARNING!

4 CITIES WITH INCOMPLETE MILEAGE INFORMATION

WERE FOUND, A LISTING HAS BEEN SENT TO THE MAS ADPAC.

\>\>\> WARNING!

286 CITIES WITH INCOMPLETE ZIP CODE INFORMATION

WERE FOUND, A LISTING HAS BEEN SENT TO THE MAS ADPAC.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Will now load in routines for other packages, if appropriate...

o Installing IBACKIN routine from DGVPTIB1 routine...

IBACKIN...filed

o Installing IBECEA3 routine from DGVPTIB2 routine...

IBECEA3...filed

o Installing IBCNSP2 routine from DGVPTIB3 routine...

IBCNSP2...filed

o Installing IBCNSC routine from DGVPTIB4 routine...

IBCNSC...filed

o Installing IBOVOP1 routine from DGVPTIB5 routine...

IBOVOP1...filed

o Installing DVBHS5 routine from DGVPTDV1 routine...

DVBHS5...filed

o Installing DVBHS1 routine from DGVPTDV2 routine...

DVBHS1...filed

o Installing DVBHS2 routine from DGVPTDV3 routine...

DVBHS2...filed

o Installing DVBHS6 routine from DGVPTDV4 routine...

DVBHS6...filed

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> You will need to recompile the following input templates on

all CPU's using the routine ^DIEZ. These templates contain

patient fields that have had cross references added for IVM.

Please ensure that the same routine size is used on each system.

Template Routine

-------- -------

DVBHINQ UPDATE DVBHCE

IB SCREEN1 IBXSC1

DVBC ADD 2507 PAT DVBAXA

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Updating STATE File (#5) Alaska County data ...

FOUND MATCH ON NAME. IEN= 4 FOR SKAGWAY-YAKUTAT-ANGOON-231

...CHANGING COUNTY SKAGWAY-YAKUTAT-ANGOON-231 TO SKAGWAY-HOONAH-ANGOON-232

FOUND MATCH ON NAME. IEN= 24 FOR SKAGWAY-YAKUTAT-ANGOON-231

...CHANGING COUNTY SKAGWAY-YAKUTAT-ANGOON-231 TO SKAGWAY-HOONAH-ANGOON-232

FOUND MATCH ON NAME. IEN= 2 FOR ALEUTIAN WEST-010

...CHANGING COUNTY ALEUTIAN WEST-010 TO ALEUTIANS WEST-016

FOUND NO DENALI BOROUGH-068 (OLD COUNTY NAME-CODE)

...NEW COUNTY DENALI BOROUGH-068 ADDED

FOUND NO YAKUTAT-282 (OLD COUNTY NAME-CODE)

...NEW COUNTY YAKUTAT-282 ADDED

...STATE File update completed.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Converting EDR data from file \#705 to file \#391.51...completed.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Restoring queued jobs to original state...

'DG G&L RECALCULATION AUTO'....Queued to run : JAN 28,1993@00:11:34

Device for Output : NONE SELECTED

Rescheduling Freq. : 24H

'DG RUG BACKGROUND JOB'........Queued to run : JAN 27,1993@23:50

Device for Output : A74

Rescheduling Freq. : 1D

'DG RUG SEMI ANNUAL - TASKED'..Queued to run : APR 2,1993@00:30

Device for Output : A113

Rescheduling Freq. : 6M

'DG PTF BACKGROUND JOB'........Queued to run : JAN 28,1993@01:30

Device for Output : NONE SELECTED

Rescheduling Freq. : 1D

'DGJ IRT UPDATE (Background)'.Queued to run : NOT QUEUED

Device for Output : NONE SELECTED

Rescheduling Freq. : NONE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Setting standard output template defaults...

'DGSCHAD' template filed for 'Scheduled Admissions'.

'DG SI LIST' template filed for 'Seriously ill list'.

'DG FEMALE INPATIENTS' template filed for 'Female Inpatient List'.

'DG FEMALE HISTORICAL' template filed for 'Historical Female Inpatient List'.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Checking to see if any PIMS files are unprotected...

PATIENT (#2) has no LAYGO,READ,WRITE.

ELIGIBILITY CODE (#8) has no LAYGO,READ,WRITE.

MAS ELIGIBILITY CODE (#8.1) has no DD,DELETE,LAYGO,READ,WRITE.

IDENTIFICATION FORMAT (#8.2) has no DD,DELETE,LAYGO,READ,WRITE.

RACE (#10) has no READ.

MARITAL STATUS (#11) has no READ.

RELIGION (#13) has no READ.

PERIOD OF SERVICE (#21) has no READ.

POW PERIOD (#22) has no READ.

BRANCH OF SERVICE (#23) has no READ.

TYPE OF DISCHARGE (#25) has no READ.

OTHER FEDERAL AGENCY (#35) has no READ.

INSURANCE COMPANY (#36) has no READ.

EMBOSSER EQUIPMENT FILE (#39.3) has no DD,DELETE,LAYGO,READ,WRITE.

MEDICAL CENTER DIVISION (#40.8) has no DD,DELETE,LAYGO,WRITE.

SPECIALTY (#42.4) has no DD,DELETE,LAYGO,READ,WRITE.

PRIORITY GROUPING (#42.55) has no DD,DELETE,LAYGO,READ,WRITE.

MAS EVENT RATES (#43.1) has no DD,DELETE,LAYGO,READ,WRITE.

MAS AWARD (#43.11) has no DD,DELETE,LAYGO,READ,WRITE.

G&L TYPE OF CHANGE (#43.61) has no DD,DELETE,LAYGO,READ,WRITE.

ADT TEMPLATE (#43.7) has no DD,DELETE,LAYGO,READ,WRITE.

SOURCE OF ADMISSION (#45.1) has no DD,DELETE,LAYGO,READ,WRITE.

PTF ABUSED SUBSTANCE (#45.61) has no DD,DELETE,LAYGO,READ,WRITE.

PTF ARCHIVE/PURGE HISTORY FILE (#45.62) has no

DD,DELETE,LAYGO,READ,WRITE.

PTF AUSTIN ERROR CODES (#45.64) has no DD,DELETE,LAYGO,READ,WRITE.

STATION TYPE (#45.81) has no DD,DELETE,LAYGO,READ,WRITE.

CENSUS WORKFILE (#45.85) has no DD,DELETE,LAYGO,READ,WRITE.

PTF CENSUS DATE (#45.86) has no DD,DELETE,LAYGO,READ,WRITE.

PTF TRANSACTION REQUEST LOG (#45.87) has no

DD,DELETE,LAYGO,READ,WRITE.

PTF EXPANDED CODE CATEGORY (#45.88) has no

DD,DELETE,LAYGO,READ,WRITE.

PTF EXPANDED CODE (#45.89) has no DD,DELETE,LAYGO,READ,WRITE.

PAF (#45.9) has no LAYGO,WRITE.

CPT (#81) has no DD,DELETE,LAYGO,READ,WRITE.

CPT CATEGORY (#81.1) has no DD,DELETE,LAYGO,READ,WRITE.

STATION NUMBER (TIME SENSITIVE (#389.9) has no

DD,DELETE,LAYGO,READ,WRITE.

TYPE OF PATIENT (#391) has no DD,DELETE,LAYGO,READ,WRITE.

AMIS SEGMENT (#391.1) has no DD,DELETE,LAYGO,READ,WRITE.

BENEFICIARY TRAVEL CLAIM (#392) has no DD,DELETE,LAYGO,READ,WRITE.

BENEFICIARY TRAVEL DISTANCE (#392.1) has no

DD,DELETE,LAYGO,READ,WRITE.

BENEFICIARY TRAVEL CERTIFICATI (#392.2) has no

DD,DELETE,LAYGO,READ,WRITE.

BENEFICIARY TRAVEL ACCOUNT (#392.3) has no DELETE,READ.

BENEFICIARY TRAVEL MODE OF TRA (#392.4) has no

DD,DELETE,LAYGO,READ,WRITE.

INCOMPLETE RECORDS (#393) has no DD,DELETE,LAYGO,READ,WRITE.

MAS SERVICE (#393.1) has no DD,DELETE,LAYGO,READ,WRITE.

IRT STATUS (#393.2) has no DD,DELETE,LAYGO,READ,WRITE.

IRT TYPE OF DEFICIENCY (#393.3) has no DD,DELETE,LAYGO,READ,WRITE.

TYPE OF CATEGORY (#393.41) has no DD,DELETE,LAYGO,READ,WRITE.

PATIENT MOVEMENT (#405) has no DD,DELETE,LAYGO,READ,WRITE.

FACILITY MOVEMENT TYPE (#405.1) has no DD,DELETE,LAYGO,READ,WRITE.

MAS MOVEMENT TYPE (#405.2) has no DD,DELETE,LAYGO,READ,WRITE.

MAS MOVEMENT TRANSACTION TYPE (#405.3) has no

DD,DELETE,LAYGO,READ,WRITE.

ROOM-BED (#405.4) has no DD,DELETE,LAYGO,READ,WRITE.

MAS OUT-OF-SERVICE (#405.5) has no DD,DELETE,LAYGO,READ,WRITE.

ROOM-BED DESCRIPTION (#405.6) has no DD,DELETE,LAYGO,READ,WRITE.

LODGING REASON (#406.41) has no DD,DELETE,LAYGO,READ,WRITE.

TRANSMISSION ROUTERS (#407.7) has no DD,DELETE,LAYGO,READ,WRITE.

DISCRETIONARY WORKLOAD (#408) has no DD,DELETE,LAYGO,READ,WRITE.

RELATIONSHIP (#408.11) has no DD,DELETE,LAYGO,READ,WRITE.

PATIENT RELATION (#408.12) has no DD,DELETE,LAYGO,READ,WRITE.

INCOME PERSON (#408.13) has no DD,DELETE,LAYGO,READ,WRITE.

INDIVIDUAL ANNUAL INCOME (#408.21) has no DD,DELETE,LAYGO,READ,WRITE.

INCOME RELATION (#408.22) has no DD,DELETE,LAYGO,READ,WRITE.

ANNUAL MEANS TEST (#408.31) has no DD,DELETE,LAYGO,READ,WRITE.

MEANS TEST STATUS (#408.32) has no DD,DELETE,LAYGO,READ,WRITE.

TYPE OF TEST (#408.33) has no DD,DELETE,LAYGO,READ,WRITE.

MEANS TEST CHANGES (#408.41) has no DD,DELETE,LAYGO,READ,WRITE.

MEANS TEST CHANGES TYPE (#408.42) has no DD,DELETE,LAYGO,READ,WRITE.

\>\>\> Please note that this information is provided for informational purposes

only. Lack of file protection does not necessarily indicate a problem

since need and level of protection is determined by the local facility.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Remember to recompile the following templates on all CPU's...

Template Routine Type Routine Used to Recompile

-------- ------- ---- -------------------------

DGPM ADMIT DGPMX1 INPUT DIEZ

DGPM TRANSFER DGPMX2 INPUT DIEZ

DGPM DISCHARGE DGPMX3 INPUT DIEZ

DGPM CHECK-IN LODGER DGPMX4 INPUT DIEZ

DGPM LODGER CHECK-OUT DGPMX5 INPUT DIEZ

DGPM SPECIALTY TRANSFER DGPMX6 INPUT DIEZ

DGPM ASIH ADMIT DGPMXAS INPUT DIEZ

DG PTF ADD MESSAGE DGPTXMS INPUT DIEZ

DG PTF CREATE PTF ENTRY DGPTXC INPUT DIEZ

DG PTF POST CREATE DGPTXCA INPUT DIEZ

DG101 DGPTX1 INPUT DIEZ

DG401 DGPTX4 INPUT DIEZ

DG501 DGPTX5 INPUT DIEZ

DG501F DGX5F INPUT DIEZ

DG701 DGPTX7 INPUT DIEZ

DG CONSISTENCY CHECKER DGRPXC INPUT DIEZ

DG LOAD EDIT SCREEN 7 DGRPXX7 INPUT DIEZ

DGRP COLLATERAL REGISTER DGRPXCR INPUT DIEZ

DG PTF PT BRIEF LIST DGPTXB PRINT DIPZ

DGPT QUICK PROFILE DGPTXCP PRINT DIPZ

DGJ EDIT IRT RECORD DGJXE INPUT DIEZ

DGJ ENTER IRT RECORD DGJXA INPUT DIEZ

DGMT ENTER/EDIT ANNUAL INCOME DGMTXI INPUT DIEZ

DGMT ENTER/EDIT COMPLETION DGMTXC INPUT DIEZ

DGMT ENTER/EDIT DEPENDENTS DGMTXD INPUT DIEZ

DGMT ENTER/EDIT EXPENSES DGMTXE INPUT DIEZ

DGMT ENTER/EDIT MARITAL STATUS DGMTXM INPUT DIEZ

DGRP ENTER/EDIT ANNUAL INCOME DGRPXIS INPUT DIEZ

DGMT ENTER/EDIT NET WORTH DGMTXN INPUT DIEZ

DGTS DGXTS INPUT DIEZ

DVBHINQ UPDATE DVBHCE INPUT DIEZ

DVBC ADD 2507 PAT DVBCDAT INPUT DIEZ

\>\>\> Remember to recompile the cross-references for the following files

on all CPU's...

File Routine Type Routine Used to Recompile

---- ------- ---- -------------------------

PTF (#45) DGPTXX X-REF DIKZ

PATIENT MOVEMENT (#405) DGPMXX X-REF DIKZ

INDIVIDUAL ANNUAL INCOME (#408.21) DGMTXX1 X-REF DIKZ

INCOME RELATION (#408.22) DGMTXX2 X-REF DIKZ

ANNUAL MEANS TEST (#408.31) DGMTXX3 X-REF DIKZ

> **NOTE:** To recompile all PIMS compiled templates and compiled

cross-references you can call ALL^DGUTL1.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> The following routines are considered obsolete with this release and may

be removed from your system when time permits. They are no longer

supported by the development ISC.

DGV52PC DGV52PC1 DGV52PP DGV52PR DGV52PT DGV52PT1

DGV52PT2 DGV52PT3 DPTV52PP DPTV52PR DPTV52PT SDV52PP SDV52PT

DGMTC0 DGMTC1 DGMTC2 DGMTCQ SDPP1 DGJTECOM EDRGEN

EDRGEN1 EDRIPOST EDRNTEG DGYPGL DGYPGL1 DGYPGLI1 DGYPGLI2

DGYPGLO DGYPGLO1 DGYPGLO2 DGYPGLO3 DGYPBT1 SDACS0 SDACS1

> **NOTE:** If you would like to have the module automatically delete these routines, you can call DEL^DGVPT1 after initialization of this version is

completed.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Updating Census Dates...Done.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Deleting/repointing 'DG' options in OPTION file as necessary.

DG MEANS TEST AUDIT

-------------------

REMOVED from 'DG MEANS TEST EVENTS' menu...

'Means Test Audit Event' REMOVED from OPTION file...

DG MEANS TEST EVENTS

--------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'Means Test Event Driver' REMOVED from OPTION file...

DG OERR TREATING TRANSFER

-------------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'TRANSFER SPECIALTY' REMOVED from OPTION file...

DGJ INCOMPLETE EVENT

--------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'Incomplete Records Event Driver' REMOVED from OPTION file...

DGJ IRT VIEW

------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'View an IRT Record' REMOVED from OPTION file...

DGOERR ADMIT

------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'ADMIT PATIENT' REMOVED from OPTION file...

DGOERR BED SWITCH

-----------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'SWITCH BED' REMOVED from OPTION file...

DGOERR DISCHARGE

----------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'DISCHARGE PATIENT' REMOVED from OPTION file...

DGOERR NOTE

-----------

REMOVED from 'DGPM MOVEMENT EVENTS' menu...

'MAS Notifications' REMOVED from OPTION file...

DGOERR PATIENT INQUIRY

----------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'PATIENT INQUIRY' REMOVED from OPTION file...

DGOERR SCHED ADMIT

------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'SCHEDULE ADMISSION' REMOVED from OPTION file...

DGOERR TRANSFER

---------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'TRANSFER PATIENT' REMOVED from OPTION file...

DGPM MOVEMENT EVENTS

--------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'MOVEMENT EVENTS v 5.0' REMOVED from OPTION file...

DGPM TREATING SPECIALTY EVENT

-----------------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'TREATING SPECIALTY EVENT' REMOVED from OPTION file...

DGYP BT DIST CHECK

-------------------

REMOVED from 'DGYP ADPAC MENU' menu...

'Incomplete BT Distance Data' REMOVED from OPTION file...

DGYP GL/BSR/TSR INPT INFO

-------------------------

REMOVED from 'DGP ADPAC MENU' menu...

'Treating Specialty Inpatient Information Printouts' REMOVED from OPTION file...

\>\>\> Deleting/repointing 'VA' options in OPTION file as necessary.

VA STATION NUMBER MAINT.

------------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'Station Number (time sensitive) Enter/Edit' REMOVED from OPTION file...

\>\>\> Deleting/repointing 'EDR' options in OPTION file as necessary.

EDR PROCESS EVENTS

------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'Process MAS Events for EDR' REMOVED from OPTION file...

\>\>\> Initialization of Version 5.3 of DG Complete.

After you've been up and running for about a week or so, we would appreciate it if you would utilize the Transmit/Generate Release Comments option of the PIMS package to provide us with your (and your users) initial impression of this release. Thank you.

3\. SDINIT Sample

\>D ^SDINIT

This version (#5.3) of 'SDINIT' was created on 08-JUN-1993

(at ALBANY ISC VAX DEVELOPMENT, by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

I AM GOING TO SET UP THE FOLLOWING FILES:

31 DISABILITY CONDITION

> **NOTE:** You already have the 'DISABILITY CONDITION' File.

40.1 OPC

> **NOTE:** You already have the 'OPC' File.

40.15 OPC ERRORS

> **NOTE:** You already have the 'OPC ERRORS' File.

40.7 CLINIC STOP (including data)

> **NOTE:** You already have the 'CLINIC STOP' File.

Want my data merged with yours? NO

40.9 LOCATION TYPE (including data)

> **NOTE:** You already have the 'LOCATION TYPE' File.

Want my data to overwrite yours? NO

44 HOSPITAL LOCATION

> **NOTE:** You already have the 'HOSPITAL LOCATION' File.

407.5 LETTER

> **NOTE:** You already have the 'LETTER' File.

407.6 LETTER TYPE (including data)

> **NOTE:** You already have the 'LETTER TYPE' File.

Want my data to overwrite yours? NO

409.1 APPOINTMENT TYPE (including data)

> **NOTE:** You already have the 'APPOINTMENT TYPE' File.

Want my data to overwrite yours? NO

409.2 CANCELLATION REASONS (including data)

> **NOTE:** You already have the 'CANCELLATION REASONS' File.

Want my data to overwrite yours? NO

409.3 AMBULATORY PROCEDURE GROUPS (including data)

> **NOTE:** You already have the 'AMBULATORY PROCEDURE GROUPS' File.

Want my data merged with yours? NO

409.41 OUTPATIENT CLASSIFICATION TYPE (including data)

I will OVERWRITE your data with mine.

409.42 OUTPATIENT CLASSIFICATION

409.43 OUTPATIENT DIAGNOSIS

409.44 OUTPATIENT PROVIDER

409.45 OUTPATIENT CLASSIFICATION STOP CODE EXCEPTION (including data)

409.5 SCHEDULING VISITS

> **NOTE:** You already have the 'SCHEDULING VISITS' File.

409.62 APPOINTMENT GROUP (including data)

> **NOTE:** You already have the 'APPOINTMENT GROUP' File.

I will OVERWRITE your data with mine.

409.63 APPOINTMENT STATUS (including data)

> **NOTE:** You already have the 'APPOINTMENT STATUS' File.

I will OVERWRITE your data with mine.

409.65 APPOINTMENT STATUS UPDATE LOG

> **NOTE:** You already have the 'APPOINTMENT STATUS UPDATE LOG' File.

409.66 APPOINTMENT TRANSACTION TYPE (including data)

> **NOTE:** You already have the 'APPOINTMENT TRANSACTION TYPE' File.

I will OVERWRITE your data with mine.

409.68 OUTPATIENT ENCOUNTER

409.71 AMBULATORY PROCEDURE (including data)

> **NOTE:** You already have the 'AMBULATORY PROCEDURE' File.

Want my data to overwrite yours? NO

409.72 AMBULATORY PROCEDURE TIME SENSITIVE DATA (including data)

> **NOTE:** You already have the 'AMBULATORY PROCEDURE TIME SENSITIVE DATA' File.

Want my data merged with yours? NO

409.81 RAM GROUP (including data)

> **NOTE:** You already have the 'RAM GROUP' File.

Want my data to overwrite yours? NO

409.82 RAM REIMBURSEMENT

> **NOTE:** You already have the 'RAM REIMBURSEMENT' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// N (NO)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains FUNCTIONS

SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Saving times for queued jobs...will be restored in post-init to original

values..

'SDAM BACKGROUND JOB'....Queued to run : NOT QUEUED

Device for Output : NONE SELECTED

Rescheduling Freq. : 24H

...SORRY, THIS MAY TAKE A FEW MOMENTS.........................................

..............................................................................

..............................................................................

..............................................................................

.......................................................

'SD AMB PROC CHECK LIST PRINT' Option Filed

'SD AMB PROC EDIT' Option Filed

'SD AMB PROC GROUP EDIT' Option Filed

'SD AMB PROC LIST' Option Filed

'SD AMB PROC MANAGEMENT REPORT' Option Filed

'SD AMB PROC RAM DATA EDIT' Option Filed

'SD AMBULATORY PROC' Option Filed

'SD APPT STATUS' Option Filed

'SD CANCEL APPOINTMENT' Option Filed

'SD DISPLAY AVAIL REPORT' Option Filed

'SD INACTIVATE' Option Filed

'SD NOSHOW REPORT' Option Filed

'SD OERR CANCEL APPT' Option Filed

'SD OERR MAKE APPT' Option Filed

'SD OPC DV OUTPUT' Option Filed

'SD OPC STOP CODE' Option Filed

'SD OPCDEL' Option Filed

'SD PARM PARAMETERS' Option Filed

'SD PURGE' Option Filed

'SD REACT' Option Filed

'SD SDCLK' Option Filed

'SD UNIQUE SSN' Option Filed

'SDACS CGATLIST' Option Filed

'SDACS CGBUPDATE' Option Filed

'SDACS CGEDIT' Option Filed

'SDACS CGMENU' Option Filed

'SDACS CGSCLIST' Option Filed

'SDADDEDIT' Option Filed

'SDAM APPT CHECK IN/OUT' Option Filed

'SDAM APPT MGT' Option Filed

'SDAM APPT UPDATE' Option Filed

'SDAM APPT UPDATE MENU' Option Filed

'SDAM APPT UPDATE PRINT' Option Filed

'SDAM APPT UPDATE PURGE' Option Filed

'SDAM APPT UPDATE VIEW' Option Filed

'SDAM BACKGROUND JOB' Option Filed

'SDAM PROVIDER/DIAGNOSIS REPORT' Option Filed

'SDAM RPT MANAGEMENT' Option Filed

'SDAM RPT RETROACTIVE LIST' Option Filed

'SDAMEN' Option Filed

'SDAMIS' Option Filed

'SDAMISUSPENSELIST' Option Filed

'SDAPP' Option Filed

'SDAPP INPT' Option Filed

'SDAPPEND' Option Filed

'SDBUILD' Option Filed

'SDCANCEL' Option Filed

'SDCHART' Option Filed

'SDCLINIC' Option Filed

'SDCLINIC ASSIGNMENT' Option Filed

'SDCLINIC WORKLOAD' Option Filed

'SDCLINLIST' Option Filed

'SDCONVERTTO3060' Option Filed

'SDCRSSDAU' Option Filed

'SDCRSSRECS' Option Filed

'SDD' Option Filed

'SDDELANCIL' Option Filed

'SDDISCHARGE' Option Filed

'SDDISPPEND' Option Filed

'SDDISSUR' Option Filed

'SDEDITAMISERRS' Option Filed

'SDEDLET' Option Filed

'SDENRGREATERTHANX' Option Filed

'SDENROLL' Option Filed

'SDFILEROOM' Option Filed

'SDGENAMISSAMP' Option Filed

'SDHOLIDAY' Option Filed

'SDI' Option Filed

'SDLIST' Option Filed

'SDM' Option Filed

'SDMGR' Option Filed

'SDMULTIBOOK' Option Filed

'SDMULTICLINIC' Option Filed

'SDNEXT' Option Filed

'SDNOSHOW' Option Filed

'SDOPC TRANSMISSION' Option Filed

'SDOUTPUT' Option Filed

'SDPATIENT' Option Filed

'SDPRAMISERRS' Option Filed

'SDPRDISPEN' Option Filed

'SDPRLETTERS' Option Filed

'SDRESTORE' Option Filed

'SDREVIEWDATE' Option Filed

'SDRFC' Option Filed

'SDROUT' Option Filed

'SDSUP' Option Filed

'SDSURMEN' Option Filed

'SDUSER' Option Filed

'SDVADSTAT' Option Filed

'SDWARD' Option Filed............................

Compiling SD ENCOUNTER ENTRY input template of File 409.68.....

'SDAMXOE' ROUTINE FILED....

'SDAMXOE1' ROUTINE FILED..

'SDAMXOE2' ROUTINE FILED

Compiling SDAMBT input template of File 409.5.

'SDXA' ROUTINE FILED....

'SDXA1' ROUTINE FILED......

'SDXA2' ROUTINE FILED

Compiling SDB input template of File 44.....

'SDBT' ROUTINE FILED........

'SDBT1' ROUTINE FILED.....

'SDBT2' ROUTINE FILED......

'SDBT3' ROUTINE FILED.......

'SDBT6' ROUTINE FILED......

'SDBT8' ROUTINE FILED.

'SDBT10' ROUTINE FILED..

'SDBT4' ROUTINE FILED..

'SDBT5' ROUTINE FILED.

'SDBT7' ROUTINE FILED.

'SDBT9' ROUTINE FILED

Compiling SDM1 input template of File 2...

'SDM1T' ROUTINE FILED...

'SDM1T1' ROUTINE FILED..

'SDM1T2' ROUTINE FILED

Compiling SDXACSE input template of File 409.5.

'SDXACSE' ROUTINE FILED...

'SDXACSE1' ROUTINE FILED....

'SDXACSE2' ROUTINE FILED...

'SDXACSE3' ROUTINE FILED

Compiling SD-AMB-PROC-DISPLAY print template of File 409.71.....................

..............

'SDXAMB' ROUTINE FILED.......

Compiling SD-AMB-PROC-LIST print template of File 409.72...............

'SDXLST' ROUTINE FILED......

Compiling SD-AMB-RAM-DISPLAY print template of File 409.81...................

'SDXRAM' ROUTINE FILED....

Compiling SDAMVLD print template of File 409.65...................

'SDAMXLD' ROUTINE FILED.....

NO SECURITY-CODE PROTECTION HAS BEEN MADE

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

This version of 'SDONIT' was created on 08-JUN-1993

(at ALBANY ISC VAX DEVELOPMENT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please..................................

......................

Located in the SD (SCHEDULING) namespace....

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace...........

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace...

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace.

'SD APPT STATUS' Protocol Filed

'SD OERR CANCEL APPT' Protocol Filed

'SD OERR MAKE APPT' Protocol Filed

'SD PARM EDIT DIVISION' Protocol Filed

'SD PARM EDIT PARAMETERS' Protocol Filed

'SD PARM PARAMETERS MENU' Protocol Filed

SD PARM EDIT PARAMETERS added as item to SD PARM PARAMETERS MENU.

SD PARM EDIT DIVISION added as item to SD PARM PARAMETERS MENU.

'SDAM ADD EDIT' Protocol Filed

'SDAM ANCILLARY ADD/EDITS' Protocol Filed

'SDAM APPOINTMENT EVENTS' Protocol Filed

'SDAM APPT CANCEL' Protocol Filed

'SDAM APPT CHECK IN' Protocol Filed

'SDAM APPT MAKE' Protocol Filed

'SDAM APPT NO-SHOW' Protocol Filed

'SDAM APPT UNSCHEDULED' Protocol Filed

'SDAM BLANK 1' Protocol Filed

'SDAM BLANK 2' Protocol Filed

'SDAM BLANK 3' Protocol Filed

'SDAM BLANK 4' Protocol Filed

'SDAM BLANK 5' Protocol Filed

'SDAM BLANK 6' Protocol Filed

'SDAM BLANK 7' Protocol Filed

'SDAM CLASSIFICATION' Protocol Filed

'SDAM CLINIC CHANGE' Protocol Filed

'SDAM DATE CHANGE' Protocol Filed

'SDAM DELETE CHECK OUT' Protocol Filed

'SDAM DIAGNOSIS' Protocol Filed

'SDAM DISCHARGE CLINIC' Protocol Filed

'SDAM LATE ENTRY' Protocol Filed

'SDAM LIST ALL' Protocol Filed

'SDAM LIST CANCELLED' Protocol Filed

'SDAM LIST CHECKED IN' Protocol Filed

'SDAM LIST CHECKED OUT' Protocol Filed

'SDAM LIST FUTURE' Protocol Filed

'SDAM LIST INPATIENT' Protocol Filed

'SDAM LIST MENU' Protocol Filed

SDAM LIST CHECKED OUT added as item to SDAM LIST MENU.

'SDAM LIST NO ACTION' Protocol Filed

'SDAM LIST NO SHOWS' Protocol Filed

'SDAM LIST NON-COUNT' Protocol Filed

'SDAM MENU' Protocol Filed

SDAM APPT CHECK IN added as item to SDAM MENU.

SDAM LIST MENU added as item to SDAM MENU.

SDAM PATIENT CHANGE added as item to SDAM MENU.

SDAM CLINIC CHANGE added as item to SDAM MENU.

SDAM DATE CHANGE added as item to SDAM MENU.

SDAM APPT UNSCHEDULED added as item to SDAM MENU.

SDAM APPT MAKE added as item to SDAM MENU.

SDAM APPT NO-SHOW added as item to SDAM MENU.

SDAM APPT CANCEL added as item to SDAM MENU.

SDCO APPT CHECK OUT added as item to SDAM MENU.

SDAM ADD EDIT added as item to SDAM MENU.

SDAM RT MENU added as item to SDAM MENU.

SDAM PROVIDER added as item to SDAM MENU.

SDAM DIAGNOSIS added as item to SDAM MENU.

SDAM PATIENT DEMOGRAPHICS added as item to SDAM MENU.

SDAM CLASSIFICATION added as item to SDAM MENU.

SDAM DISCHARGE CLINIC added as item to SDAM MENU.

SDAM DELETE CHECK OUT added as item to SDAM MENU.

'SDAM PATIENT CHANGE' Protocol Filed

'SDAM PATIENT DEMOGRAPHICS' Protocol Filed

'SDAM PROVIDER' Protocol Filed

'SDAM RT MAS-CHART-PROFILE' Protocol Filed

'SDAM RT MAS-CHART-REQUEST' Protocol Filed

'SDAM RT MAS-FILL-NEXT' Protocol Filed

'SDAM RT MAS-RE-CHARGE' Protocol Filed

'SDAM RT MENU' Protocol Filed

SDAM RT MAS-FILL-NEXT added as item to SDAM RT MENU.

SDAM RT MAS-CHART-PROFILE added as item to SDAM RT MENU.

SDAM RT MAS-RE-CHARGE added as item to SDAM RT MENU.

SDAM RT MAS-CHART-REQUEST added as item to SDAM RT MENU.

'SDCO ADD EDIT NEW' Protocol Filed

'SDCO APPT CHECK OUT' Protocol Filed

'SDCO CHECK OUT DATE' Protocol Filed

'SDCO CLASSIFICATION' Protocol Filed

'SDCO CLINIC APPT' Protocol Filed

'SDCO DIAGNOSIS' Protocol Filed

'SDCO DISCHARGE CLINIC' Protocol Filed

'SDCO INTERVIEW' Protocol Filed

'SDCO MENU' Protocol Filed

SDCO PROVIDER added as item to SDCO MENU.

SDCO CLASSIFICATION added as item to SDCO MENU.

SDCO CLINIC APPT added as item to SDCO MENU.

SDCO DIAGNOSIS added as item to SDCO MENU.

SDCO DISCHARGE CLINIC added as item to SDCO MENU.

SDCO ADD EDIT NEW added as item to SDCO MENU.

SDCO PATIENT DEMOGRAPHICS added as item to SDCO MENU.

SDCO INTERVIEW added as item to SDCO MENU.

SDAM RT MENU added as item to SDCO MENU.

SDCO CHECK OUT DATE added as item to SDCO MENU.

'SDCO PATIENT DEMOGRAPHICS' Protocol Filed

'SDCO PROVIDER' Protocol Filed

'SDPP PATIENT PROFILE CHANGE DATE' Protocol Filed

'SDPP PATIENT PROFILE CHANGE PATIENT' Protocol Filed

'SDPP PATIENT PROFILE DISPLAY ADD/EDITS' Protocol Filed

'SDPP PATIENT PROFILE DISPLAY ALL' Protocol Filed

'SDPP PATIENT PROFILE DISPLAY APPOINTMENTS' Protocol Filed

'SDPP PATIENT PROFILE DISPLAY DISPOSITIONS' Protocol Filed

'SDPP PATIENT PROFILE DISPLAY ENROLLMENTS' Protocol Filed

'SDPP PATIENT PROFILE DISPLAY INFO MENU' Protocol Filed

SDPP PATIENT PROFILE DISPLAY ADD/EDITS added as item to SDPP PATIENT PROFILE DISPLAY INFO MENU.

SDPP PATIENT PROFILE DISPLAY APPOINTMENTS added as item to SDPP PATIENT PROFILE DISPLAY INFO MENU.

SDPP PATIENT PROFILE DISPLAY ENROLLMENTS added as item to SDPP PATIENT PROFILE DISPLAY INFO MENU.

SDPP PATIENT PROFILE DISPLAY DISPOSITIONS added as item to SDPP PATIENT PROFILE DISPLAY INFO MENU.

SDPP PATIENT PROFILE DISPLAY MEANS TEST added as item to SDPP PATIENT PROFILE DISPLAY INFO MENU.

SDPP PATIENT PROFILE DISPLAY ALL added as item to SDPP PATIENT PROFILE DISPLAY INFO MENU.

'SDPP PATIENT PROFILE DISPLAY MEANS TEST' Protocol Filed

'SDPP PATIENT PROFILE MENU' Protocol Filed

SDPP PATIENT PROFILE DISPLAY INFO MENU added as item to SDPP PATIENT PROFILE MENU.

SDPP PATIENT PROFILE CHANGE PATIENT added as item to SDPP PATIENT PROFILE MENU

.

SDPP PATIENT PROFILE CHANGE DATE added as item to SDPP PATIENT PROFILE MENU.

'SDUL BLANK 1' Protocol Filed

'SDUL BLANK 2' Protocol Filed

'SDUL BLANK 3' Protocol Filed

'SDUL BLANK 4' Protocol Filed

'SDUL BLANK 5' Protocol Filed

'SDUL BLANK 6' Protocol Filed

'SDUL BLANK 7' Protocol Filed

'SDUL DISPLAY' Protocol Filed

'SDUL DISPLAY W/EXPAND' Protocol Filed

'SDUL DOWN A LINE' Protocol Filed

'SDUL EXPAND' Protocol Filed

'SDUL FIRST SCREEN' Protocol Filed

'SDUL LAST SCREEN' Protocol Filed

'SDUL NEXT SCREEN' Protocol Filed

'SDUL PREVIOUS SCREEN' Protocol Filed

'SDUL PRINT LIST' Protocol Filed

'SDUL PRINT SCREEN' Protocol Filed

'SDUL QUIT' Protocol Filed

'SDUL REFRESH' Protocol Filed

'SDUL SEARCH LIST' Protocol Filed

'SDUL TURN ON/OFF MENUS' Protocol Filed

'SDUL UP ONE LINE' Protocol Filed

'VALM EXPAND' Protocol Filed

VALM EXPAND added as item to SDAM MENU.

OK, Protocol Installation is Complete.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> List Template installation...

'SD PARM PARAMETERS' List Template...Filed.

'SDAM APPT MGT' List Template...Filed.

'SDAM APPT PROFILE' List Template...Filed.

'SDCO CHECK OUT' List Template...Filed.

'SDPP PATIENT PROFILE' List Template...Filed.

'SDPP PATIENT PROFILE ALL' List Template...Filed.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Remember to recompile the following templates on all CPU's...

Template Routine Type Routine Used to Recompile

-------- ------- ---- -------------------------

SDB SDBT INPUT DIEZ

SDM1 SDM1T INPUT DIEZ

SDAMBT SDXA INPUT DIEZ

SDXACSE SDXACSE INPUT DIEZ

SD ENCOUNTER ENTRY SDAMXOE INPUT DIEZ

SD-AMB-PROC-DISPLAY SDXAMB PRINT DIPZ

SD-AMB-PROC-LIST SDXLST PRINT DIPZ

SD-AMB-RAM-DISPLAY SDXRAM PRINT DIPZ

SDAMVLD SDAMXLD PRINT DIPZ

SDUL LIST TEMPLATE SDULXP PRINT DIPZ

> **NOTE:** To recompile all PIMS compiled templates and compiled

cross-references you can call ALL^DGUTL1.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Adding new clinic stops to CLINIC STOP FILE (#40.7)...

\[NOTE: These stop codes CANNOT be used UNTIL 10/1/93\]

...RADIONUCLIDE THERAPY (144) added...

...PHARM/PHYSIO NMP STUDIES (145) added...

...PET (146) added...

...SCI HOME CARE PROGRAM (215) added...

...GERIATRIC EVAL. & MGMT. (GEM)(319) added...

...ALZHEIMER'S/DEMENTIA CLINIC (320) added...

...GI ENDOSCOPY (321) added...

...WOMEN'S CLINIC (322) added...

...PROSTHETIC SERVICES (423) added...

...SEXUAL TRAUMA COUNSELING (524) added...

...INCENTIVE THERAPY (573) added...

...COMPENSATED WORK THERAPY (574) added...

...VOCATIONAL ASSISTANCE (575) added...

...DOMICILIARY OUTREACH SERVCIES(725) added...

...DOM AFTERCARE - COMMUNITY (726) added...

...DOMICILIARY AFTERCARE - VA (727) added...

\>\>\> Inactivating clinic stops in CLINIC STOP CODE FILE (#40.7)...

\[NOTE: These stop codes CANNOT be used AFTER 9/30/93\]

...NEUROBEHAVIORAL-INDIVIDUAL (511) inactivated as of 10/1/93...

...NEUROBEHAVIORAL-GROUP (559) inactivated as of 10/1/93...

\>\>\> Changing clinic stop names in CLINIC STOP CODE FILE (#40.7)...

...RECREATION SERVICE (202) changed to

RECREATION THERAPY SERVICE...

...INCENTIVE THERAPY (207) changed to

RMS INCENTIVE THERAPY...

...COMPENSATED WORK THERAPY (208) changed to

RMS COMPENSATED WORK THERAPY...

...VOCATIONAL ASSISTANCE (213) changed to

RMS VOCATIONAL ASSISTANCE...

...CORRECTIVE THERAPY (214) changed to

KINESIOTHERAPY...

...CWT/ILH INDIVIDUAL (515) changed to

CWT/TR-HCMI...

...CWT/ILH SUBSTANCE ABUSE (518) changed to

CWT/TR-SUBSTANCE ABUSE...

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Restoring queued jobs to original state...

'SDAM BACKGROUND JOB'.........Queued to run : NOT QUEUED

Device for Output : NONE SELECTED

Rescheduling Freq. : 24H

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Deleting/repointing 'SD' options in OPTION file as necessary.

SD APPT STATUS

--------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'Appointment Status Update in Event Driver' REMOVED from OPTION file...

SD OERR CANCEL APPT

-------------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'CANCEL CLINIC APPT' REMOVED from OPTION file...

SD OERR MAKE APPT

-----------------

NOT ATTACHED TO ANY MENUS AS AN ITEM...NOTHING TO REPOINT OR DELETE!

'SCHEDULE CLINIC APPT' REMOVED from OPTION file...

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\>\>\> Initialization of Version 5.3 of SD Complete.

\>

PIMS Routine List

A1B2ADM A1B2BGJ A1B2MAIN A1B2MSP A1B2MUT A1B2MUT1 A1B2NTEG A1B2OLC

A1B2OSR A1B2OSR1 A1B2OSR2 A1B2OSR3 A1B2OSR4 A1B2PRE A1B2PST A1B2Q

A1B2Q1 A1B2STAT A1B2SUP A1B2T1 A1B2T2 A1B2T3 A1B2T4 A1B2UTL

A1B2XFR DG10 DG1010P DG1010P0 DG1010P1 DG1010P2 DG1010P3 DG1010P4

DG1010P5 DG1010P6 DG1010P7 DG1010PA DG1010PX DG1010S1 DG1010S2 DG3PR

DG3PR0 DG3PR1 DG3PR2 DGA400 DGA4001 DGA4002 DGA4003 DGA4004

DGA4005 DGA4006 DGA4007 DGABUL DGAINP DGAINP0 DGAINP1 DGAINP2

DGAINP3 DGAINP4 DGANHD DGANHD1 DGANHD2 DGANHD3 DGANHD4 DGBLRV

DGBT1 DGBT2 DGBTCD DGBTCE DGBTCE1 DGBTCR DGBTCR1 DGBTCR2

DGBTDIST DGBTDST1 DGBTE DGBTE1 DGBTE1A DGBTEE DGBTEE1 DGBTEE2

DGBTEF DGBTEF1 DGBTEND DGBTOA1 DGBTOA2 DGBTOA3 DGBTOA4 DGBTOA5

DGBTOA6 DGBTR DGBTSRCH DGBTUTL DGBUL DGCOL DGDDC DGDEATH

DGDIS DGDIS1 DGDISPL DGDISS DGDIST DGDIST1 DGFI DGGECS

DGGECSA DGGECSB DGGECSR DGHELP DGIN DGINI001 DGINI002 DGINI003

DGINI004 DGINI005 DGINI006 DGINI007 DGINI008 DGINI009 DGINI010 DGINI011

DGINI012 DGINI013 DGINI014 DGINI015 DGINI016 DGINI017 DGINI018 DGINI019

DGINI020 DGINI021 DGINI022 DGINI023 DGINI024 DGINI025 DGINI026 DGINI027

DGINI028 DGINI029 DGINI030 DGINI031 DGINI032 DGINI033 DGINI034 DGINI035

DGINI036 DGINI037 DGINI038 DGINI039 DGINI040 DGINI041 DGINI042 DGINI043

DGINI044 DGINI045 DGINI046 DGINI047 DGINI048 DGINI049 DGINI050 DGINI051

DGINI052 DGINI053 DGINI054 DGINI055 DGINI056 DGINI057 DGINI058 DGINI059

DGINI060 DGINI061 DGINI062 DGINI063 DGINI064 DGINI065 DGINI066 DGINI067

DGINI068 DGINI069 DGINI070 DGINI071 DGINI072 DGINI073 DGINI074 DGINI075

DGINI076 DGINI077 DGINI078 DGINI079 DGINI080 DGINI081 DGINI082 DGINI083

DGINI084 DGINI085 DGINI086 DGINI087 DGINI088 DGINI089 DGINI090 DGINI091

DGINI092 DGINI093 DGINI094 DGINI095 DGINI096 DGINI097 DGINI098 DGINI099

DGINI100 DGINI101 DGINI102 DGINI103 DGINI104 DGINI105 DGINI106 DGINI107

DGINI108 DGINI109 DGINI110 DGINI111 DGINI112 DGINI113 DGINI114 DGINI115

DGINI116 DGINI117 DGINI118 DGINI119 DGINI120 DGINI121 DGINI122 DGINI123

DGINI124 DGINI125 DGINI126 DGINI127 DGINI128 DGINI129 DGINI130 DGINI131

DGINI132 DGINI133 DGINI134 DGINI135 DGINI136 DGINI137 DGINI138 DGINI139

DGINI140 DGINI141 DGINI142 DGINI143 DGINI144 DGINI145 DGINI146 DGINI147

DGINI148 DGINI149 DGINI150 DGINI151 DGINI152 DGINI153 DGINI154 DGINI155

DGINI156 DGINI157 DGINI158 DGINI159 DGINI160 DGINI161 DGINI162 DGINI163

DGINI164 DGINI165 DGINI166 DGINI167 DGINI168 DGINI169 DGINI170 DGINI171

DGINI172 DGINI173 DGINI174 DGINI175 DGINI176 DGINI177 DGINI178 DGINI179

DGINI180 DGINI181 DGINI182 DGINI183 DGINI184 DGINI185 DGINI186 DGINI187

DGINI188 DGINI189 DGINI190 DGINI191 DGINI192 DGINI193 DGINI194 DGINI195

DGINI196 DGINI197 DGINI198 DGINI199 DGINI200 DGINI201 DGINI202 DGINI203

DGINI204 DGINI205 DGINI206 DGINI207 DGINI208 DGINI209 DGINI210 DGINI211

DGINI212 DGINI213 DGINI214 DGINI215 DGINI216 DGINI217 DGINI218 DGINI219

DGINI220 DGINI221 DGINI222 DGINI223 DGINI224 DGINI225 DGINI226 DGINI227

DGINI228 DGINI229 DGINI230 DGINI231 DGINI232 DGINI233 DGINI234 DGINI235

DGINI236 DGINI237 DGINI238 DGINI239 DGINI240 DGINI241 DGINI242 DGINI243

DGINI244 DGINI245 DGINI246 DGINI247 DGINI248 DGINI249 DGINI250 DGINI251

DGINI252 DGINI253 DGINI254 DGINI255 DGINI256 DGINI257 DGINI258 DGINI259

DGINI260 DGINI261 DGINI262 DGINI263 DGINI264 DGINI265 DGINI266 DGINI267

DGINI268 DGINI269 DGINI270 DGINI271 DGINI272 DGINI273 DGINI274 DGINI275

DGINI276 DGINI277 DGINI278 DGINI279 DGINI280 DGINI281 DGINI282 DGINI283

DGINI284 DGINI285 DGINI286 DGINI287 DGINI288 DGINI289 DGINI290 DGINI291

DGINI292 DGINI293 DGINI294 DGINI295 DGINI296 DGINI297 DGINI298 DGINI299

DGINI300 DGINI301 DGINI302 DGINI303 DGINI304 DGINI305 DGINI306 DGINI307

DGINI308 DGINI309 DGINI310 DGINI311 DGINI312 DGINI313 DGINI314 DGINI315

DGINI316 DGINI317 DGINI318 DGINI319 DGINI320 DGINI321 DGINI322 DGINI323

DGINI324 DGINI325 DGINI326 DGINI327 DGINI328 DGINI329 DGINI330 DGINI331

DGINI332 DGINI333 DGINI334 DGINI335 DGINI336 DGINI337 DGINI338 DGINI339

DGINI340 DGINI341 DGINI342 DGINI343 DGINI344 DGINI345 DGINI346 DGINI347

DGINI348 DGINI349 DGINI350 DGINI351 DGINI352 DGINI353 DGINI354 DGINI355

DGINI356 DGINI357 DGINI358 DGINI359 DGINI360 DGINI361 DGINI362 DGINI363

DGINI364 DGINI365 DGINI366 DGINI367 DGINI368 DGINI369 DGINI370 DGINI371

DGINI372 DGINI373 DGINI374 DGINI375 DGINI376 DGINI377 DGINI378 DGINI379

DGINI380 DGINI381 DGINI382 DGINI383 DGINI384 DGINIT DGINIT0 DGINIT1

DGINIT2 DGINIT3 DGINIT4 DGINITY DGINP DGINPW DGINS DGJBGJ

DGJBGJ1 DGJOPRT DGJOPRT1 DGJOPRT2 DGJOPRT3 DGJOTP DGJOTP1 DGJOTP2

DGJOTP3 DGJOTPUL DGJPAR DGJPAR1 DGJPDEF DGJPDEF1 DGJPDEF2 DGJPDEF3

DGJSUM DGJTADD DGJTDEL DGJTEE DGJTEE1 DGJTEE2 DGJTEE3 DGJTEVT

DGJTHLP DGJTUDIS DGJTUTL DGJTVW DGJTVW1 DGJTVW2 DGJTVW3 DGL

DGLOCK DGLOCK1 DGLOCK2 DGLOCK3 DGMTA DGMTAUD DGMTAUD1 DGMTCOM

DGMTCOR DGMTCOST DGMTCOU DGMTCOU1 DGMTDD DGMTDD1 DGMTDD2 DGMTDD3

DGMTDEL DGMTDOM DGMTE DGMTEO DGMTEVT DGMTLK DGMTM DGMTO

DGMTO1 DGMTOFA DGMTOFA1 DGMTOHD DGMTOPYT DGMTOREQ DGMTP DGMTP1

DGMTP2 DGMTP3 DGMTP4 DGMTR DGMTREQB DGMTSC DGMTSC1 DGMTSC11

DGMTSC2 DGMTSC3 DGMTSC31 DGMTSC4 DGMTSCC DGMTSCR DGMTSCU DGMTSCU1

DGMTSCU2 DGMTSCU3 DGMTU DGMTU1 DGMTU11 DGMTU2 DGMTU21 DGMTU22

DGMTU23 DGMTUB DGMTUTL DGMTV DGNOTE DGNTEG DGNTEG0 DGNTEG01

DGNTEG02 DGNTEG03 DGOASIH DGODASK DGODCV DGODDEL DGODMT DGODNP1

DGODNP2 DGODNSM DGODNSM1 DGODOP1 DGODOP2 DGODOSM DGODOSM1 DGODTOT

DGODUTL DGOERNOT DGOIL DGOIL1 DGOIL2 DGOIL3 DGOINPT DGOINPT1

DGOINS DGOINS1 DGONI001 DGONI002 DGONI003 DGONI004 DGONI005 DGONI006

DGONI007 DGONI008 DGONI009 DGONIT DGONIT1 DGONIT2 DGONIT3 DGOPATM

DGOREL DGOREL1 DGOVBC DGOVBC1 DGOVBC2 DGPAR DGPAR1 DGPAR2

DGPASS DGPATN DGPATV DGPMBSAB DGPMBSAR DGPMBSG DGPMBSG1 DGPMBSG2

DGPMBSG3 DGPMBSP DGPMBSP1 DGPMBSP2 DGPMBSP3 DGPMBSP4 DGPMBSP5 DGPMBSP6

DGPMBSR DGPMBSR1 DGPMBSR2 DGPMBSR3 DGPMBSR4 DGPMDD DGPMDD1 DGPMDD2

DGPMDDCF DGPMDDCN DGPMDDLD DGPMDDOS DGPMDDRB DGPMDEF DGPMEVT DGPMEX

DGPMGL DGPMGL1 DGPMGL2 DGPMGL5 DGPMGL51 DGPMGLC DGPMGLG DGPMGLG1

DGPMGLG2 DGPMGLG3 DGPMGLP DGPMGLP1 DGPMHST DGPMLOS DGPMOLD DGPMOLD1

DGPMRB DGPMRBA DGPMRBA1 DGPMSTAT DGPMTS DGPMTSI DGPMTSI1 DGPMTSI2

DGPMTSO DGPMTSO1 DGPMTSO2 DGPMTSO3 DGPMTSR DGPMTSR1 DGPMTSR2 DGPMUTL

DGPMV DGPMV0 DGPMV1 DGPMV10 DGPMV2 DGPMV20 DGPMV21 DGPMV22

DGPMV3 DGPMV30 DGPMV300 DGPMV31 DGPMV32 DGPMV321 DGPMV322 DGPMV33

DGPMV331 DGPMV35 DGPMV36 DGPMVBM DGPMVBUL DGPMVBUR DGPMVDD DGPMVDL

DGPMVDL1 DGPMVODS DGPT101 DGPT101P DGPT10CB DGPT10S1 DGPT401 DGPT501

DGPT501P DGPT50DI DGPT50MS DGPT535 DGPT601 DGPT60PR DGPT701 DGPT701P

DGPT702 DGPT70DI DGPT70DX DGPTAE DGPTAE01 DGPTAE02 DGPTAE03 DGPTAE04

DGPTAEE DGPTAEE1 DGPTAEE2 DGPTAPA DGPTAPA1 DGPTAPA2 DGPTAPA3 DGPTAPA4

DGPTAPP DGPTAPP1 DGPTAPSL DGPTBE1 DGPTBE2 DGPTBEP DGPTC DGPTC1

DGPTC2 DGPTCO DGPTCO1 DGPTCO2 DGPTCR DGPTCR1 DGPTDRG DGPTEXPR

DGPTF DGPTF099 DGPTF09X DGPTF1 DGPTF2 DGPTF4 DGPTF41 DGPTF5

DGPTFCR DGPTFD DGPTFDEL DGPTFFB DGPTFIC DGPTFJ DGPTFJC DGPTFM

DGPTFM0 DGPTFM1 DGPTFM1A DGPTFM4 DGPTFM5 DGPTFM6 DGPTFM7 DGPTFM71

DGPTFM8 DGPTFMO DGPTFMO1 DGPTFOU DGPTFQWK DGPTFREL DGPTFTR DGPTFTR0

DGPTFTR1 DGPTFTR2 DGPTFTR3 DGPTFUP DGPTFVC DGPTFVC1 DGPTFVC2 DGPTFVC3

DGPTICD DGPTLMU1 DGPTLMU2 DGPTLMU3 DGPTLMU4 DGPTLMU5 DGPTLMU6 DGPTMOVE

DGPTMSG DGPTMSG1 DGPTMSGD DGPTOD0 DGPTOD1 DGPTOD2 DGPTOD3 DGPTODA1

DGPTODA2 DGPTODB1 DGPTODB2 DGPTODF1 DGPTODF2 DGPTODI1 DGPTODI2 DGPTODI3

DGPTODI4 DGPTODR DGPTODT1 DGPTODT2 DGPTOLC1 DGPTOLC2 DGPTOM1 DGPTOM2

DGPTOOL DGPTOTRL DGPTR0 DGPTR1 DGPTR2 DGPTR3 DGPTR4 DGPTRAM

DGPTRPO DGPTRPP DGPTSC01 DGPTSCAN DGPTSPQ DGPTSUD1 DGPTSUDO DGPTTRIM

DGPTTS DGPTTS0 DGPTTS1 DGPTTS2 DGPTTS3 DGPTUTL DGPTUTL1 DGQEMA

DGQEMA1 DGQEMP DGQEMPS DGREG DGREG0 DGREG00 DGREGDD DGREGDD1

DGREGDEL DGREGE DGREGG DGRP DGRP1 DGRP10 DGRP11 DGRP12

DGRP13 DGRP14 DGRP2 DGRP3 DGRP4 DGRP5 DGRP6 DGRP7

DGRP8 DGRP9 DGRPC DGRPC1 DGRPC2 DGRPCB DGRPCE DGRPCE1

DGRPCF DGRPCF1 DGRPCK DGRPCP DGRPCP1 DGRPCR DGRPCS DGRPCU

DGRPD DGRPDB DGRPDD DGRPDD1 DGRPE DGRPE1 DGRPEIS DGRPEIS1

DGRPEIS2 DGRPH DGRPP DGRPP1 DGRPU DGRPU1 DGRPV DGRUG

DGRUG1 DGRUG16 DGRUGBGJ DGRUGC DGRUGC1 DGRUGDR DGRUGFY DGRUGGR

DGRUGIX DGRUGIX1 DGRUGPI DGRUGPP DGRUGPP1 DGRUGS DGRUGSA DGRUGTG

DGRUGV DGRUGV16 DGSCHAD DGSCHAD1 DGSCHAD2 DGSCHAD3 DGSEC DGSEC1

DGSEC2 DGSEC3 DGSILL DGSTAT DGSWITCH DGTEMP DGTSSET DGUTL

DGUTL1 DGUTL2 DGUTQ DGV53PP DGV53PP1 DGV53PR DGV53PT DGV53PT1

DGV53PT2 DGV53PT3 DGV53PT4 DGV53PT5 DGV53PT6 DGV53PTA DGV53PTB DGV53PTC

DGV53PTE DGV53PTI DGV53PTS DGVLT DGVLT1 DGVLT2 DGVLT3 DGVPP

DGVPR DGVPR1 DGVPT DGVPT1 DGVPT2 DGVPT3 DGVPTDV1 DGVPTDV2

DGVPTDV3 DGVPTDV4 DGVPTIB1 DGVPTIB2 DGVPTIB3 DGVPTIB4 DGVPTIB5 DGVPTIB6

DGVREL DGVREL1 DGVREL2 DGVREL3 DGVREL4 DGWAIT DGWIN DGYPREG

DGYPREG1 DGYPREG2 DGYPREG3 DGYPREG4 DGYPREG5 DGYZODS DPTDUP DPTIN001

DPTIN002 DPTIN003 DPTIN004 DPTIN005 DPTIN006 DPTIN007 DPTIN008 DPTIN009

DPTIN010 DPTIN011 DPTIN012 DPTIN013 DPTIN014 DPTIN015 DPTIN016 DPTIN017

DPTIN018 DPTIN019 DPTIN020 DPTIN021 DPTIN022 DPTIN023 DPTIN024 DPTIN025

DPTIN026 DPTIN027 DPTIN028 DPTIN029 DPTIN030 DPTIN031 DPTIN032 DPTIN033

DPTIN034 DPTIN035 DPTIN036 DPTIN037 DPTIN038 DPTIN039 DPTIN040 DPTIN041

DPTIN042 DPTIN043 DPTIN044 DPTIN045 DPTIN046 DPTIN047 DPTIN048 DPTIN049

DPTIN050 DPTIN051 DPTIN052 DPTIN053 DPTIN054 DPTIN055 DPTIN056 DPTIN057

DPTIN058 DPTIN059 DPTIN060 DPTIN061 DPTIN062 DPTIN063 DPTIN064 DPTIN065

DPTIN066 DPTIN067 DPTIN068 DPTIN069 DPTIN070 DPTIN071 DPTIN072 DPTIN073

DPTIN074 DPTIN075 DPTIN076 DPTIN077 DPTIN078 DPTIN079 DPTIN080 DPTIN081

DPTIN082 DPTIN083 DPTIN084 DPTIN085 DPTIN086 DPTIN087 DPTIN088 DPTIN089

DPTIN090 DPTIN091 DPTIN092 DPTIN093 DPTIN094 DPTIN095 DPTIN096 DPTIN097

DPTIN098 DPTIN099 DPTIN100 DPTIN101 DPTIN102 DPTIN103 DPTIN104 DPTIN105

DPTIN106 DPTIN107 DPTIN108 DPTIN109 DPTIN110 DPTIN111 DPTIN112 DPTIN113

DPTIN114 DPTIN115 DPTIN116 DPTIN117 DPTIN118 DPTIN119 DPTIN120 DPTIN121

DPTIN122 DPTIN123 DPTIN124 DPTIN125 DPTIN126 DPTIN127 DPTIN128 DPTIN129

DPTIN130 DPTIN131 DPTIN132 DPTIN133 DPTIN134 DPTIN135 DPTIN136 DPTIN137

DPTIN138 DPTIN139 DPTIN140 DPTIN141 DPTIN142 DPTIN143 DPTIN144 DPTIN145

DPTIN146 DPTIN147 DPTIN148 DPTIN149 DPTIN150 DPTIN151 DPTIN152 DPTIN153

DPTINIT DPTINIT0 DPTINIT1 DPTINIT2 DPTINIT3 DPTINIT4 DPTINITY DPTLK

DPTLK1 DPTLK2 DPTLK3 DPTNTEG DPTV53PP DPTV53PR DPTV53PT DPTVPP

DPTVPR DPTVPT SD SDA223AN SDA223N SDA223N1 SDACS SDACS0

SDACS1 SDACSCG SDACSCGB SDACSCGP SDAL SDAL0 SDAM SDAM1

SDAM10 SDAM2 SDAM3 SDAM5 SDAMBAE SDAMBAE0 SDAMBAE1 SDAMBAE2

SDAMBAE3 SDAMBAE4 SDAMBAE5 SDAMBAE6 SDAMBCL SDAMBEE SDAMBMR SDAMBMR1

SDAMBMR2 SDAMBMR3 SDAMC SDAMEP SDAMEP1 SDAMEP2 SDAMEP3 SDAMEP4

SDAMEVT SDAMEVT0 SDAMEVT1 SDAMEVT2 SDAMEVT3 SDAMEVT4 SDAMEX SDAMEX1

SDAMLD SDAMN SDAMO SDAMO0 SDAMO1 SDAMO11 SDAMO2 SDAMODO

SDAMODO1 SDAMODO2 SDAMODO3 SDAMOL SDAMOL1 SDAMOLP SDAMOS SDAMOS0

SDAMOS1 SDAMOSP SDAMQ SDAMQ1 SDAMQ2 SDAMQ3 SDAMQ4 SDAMQ5

SDAMU SDAMWI SDAMWI1 SDAPP SDASEE SDASEE1 SDASEE2 SDASEP

SDASO SDAUT1 SDAUT2 SDB SDB0 SDB1 SDC SDC0

SDC1 SDC2 SDC3 SDC4 SDCAN SDCCP SDCD SDCI

SDCIAL SDCLAS SDCLAS0 SDCLAS1 SDCLAV SDCLAV0 SDCLAV1 SDCLDOW

SDCLK SDCNL SDCNP SDCNP0 SDCNP1 SDCNP1A SDCNP2 SDCO

SDCO0 SDCO1 SDCO2 SDCO20 SDCO21 SDCO22 SDCO23 SDCO3

SDCO31 SDCO4 SDCO41 SDCO5 SDCO6 SDCO7 SDCO8 SDCOAM

SDCODD SDCODEL SDCOM SDCOU SDCOU1 SDCOU2 SDCOUR SDCP

SDCSSD SDCVP SDCWL SDCWL1 SDCWL2 SDCWL3 SDD SDD0

SDDADT SDDADT0 SDDIV SDDPA SDDSO SDDSSA SDDSSA0 SDDSSA1

SDF SDF1 SDHOL SDINI001 SDINI002 SDINI003 SDINI004 SDINI005

SDINI006 SDINI007 SDINI008 SDINI009 SDINI010 SDINI011 SDINI012 SDINI013

SDINI014 SDINI015 SDINI016 SDINI017 SDINI018 SDINI019 SDINI020 SDINI021

SDINI022 SDINI023 SDINI024 SDINI025 SDINI026 SDINI027 SDINI028 SDINI029

SDINI030 SDINI031 SDINI032 SDINI033 SDINI034 SDINI035 SDINI036 SDINI037

SDINI038 SDINI039 SDINI040 SDINI041 SDINI042 SDINI043 SDINI044 SDINI045

SDINI046 SDINI047 SDINI048 SDINI049 SDINI050 SDINI051 SDINI052 SDINI053

SDINI054 SDINI055 SDINI056 SDINI057 SDINI058 SDINI059 SDINI060 SDINI061

SDINI062 SDINI063 SDINI064 SDINI065 SDINI066 SDINI067 SDINI068 SDINI069

SDINI070 SDINI071 SDINI072 SDINI073 SDINI074 SDINI075 SDINI076 SDINI077

SDINI078 SDINI079 SDINI080 SDINI081 SDINI082 SDINI083 SDINI084 SDINI085

SDINI086 SDINI087 SDINI088 SDINI089 SDINI090 SDINI091 SDINI092 SDINI093

SDINI094 SDINI095 SDINI096 SDINI097 SDINI098 SDINI099 SDINI100 SDINI101

SDINI102 SDINI103 SDINI104 SDINI105 SDINI106 SDINI107 SDINI108 SDINI109

SDINI110 SDINI111 SDINI112 SDINI113 SDINI114 SDINI115 SDINI116 SDINI117

SDINI118 SDINI119 SDINI120 SDINI121 SDINI122 SDINI123 SDINI124 SDINI125

SDINI126 SDINI127 SDINI128 SDINI129 SDINI130 SDINI131 SDINI132 SDINI133

SDINI134 SDINI135 SDINI136 SDINI137 SDINI138 SDINI139 SDINI140 SDINI141

SDINI142 SDINI143 SDINI144 SDINI145 SDINI146 SDINI147 SDINI148 SDINI149

SDINI150 SDINI151 SDINI152 SDINI153 SDINI154 SDINI155 SDINI156 SDINI157

SDINI158 SDINI159 SDINI160 SDINI161 SDINI162 SDINI163 SDINI164 SDINI165

SDINI166 SDINI167 SDINI168 SDINI169 SDINI170 SDINI171 SDINI172 SDINI173

SDINI174 SDINIT SDINIT0 SDINIT1 SDINIT2 SDINIT3 SDINIT4 SDINITY

SDKILL SDL1 SDLT SDLTE SDLTP SDM SDM0 SDM1

SDM1A SDM2 SDM3 SDM4 SDMEAN SDMM SDMM1 SDMT

SDMULT SDMULT0 SDMULT1 SDN SDN0 SDN1 SDN2 SDNACT

SDNACT1 SDNDIS SDNEXT SDNOS SDNOS0 SDNOS1 SDNOS1A SDNOS2

SDNP SDNTEG SDNTEG0 SDONI001 SDONI002 SDONI003 SDONI004 SDONI005

SDONI006 SDONI007 SDONI008 SDONI009 SDONI010 SDONI011 SDONIT SDONIT1

SDONIT2 SDONIT3 SDOPC SDOPC0 SDOPC1 SDOPC2 SDOPC3 SDOPC4

SDOPC5 SDOPCDEL SDOUTPUT SDPARM SDPARM1 SDPARM2 SDPP SDPPADD1

SDPPALL SDPPAPP1 SDPPAPP2 SDPPAT1 SDPPAT2 SDPPDIS1 SDPPDIS2 SDPPENR1

SDPPHLP SDPPMT1 SDPPMT2 SDPPSEL SDPSDR SDPSDR1 SDPURG SDPURG1

SDPURG2 SDREACT SDREV SDRFC SDROUT SDROUT0 SDROUT1 SDROUT2

SDSCE SDSCP SDSCP1 SDST SDSTAT SDSTP SDSTP1 SDSTP2

SDSTP3 SDSURMEN SDTRAN SDTRAN1 SDTRAN3 SDTRAN4 SDTRAND1 SDTRAND2

SDTRANDV SDUL SDUL0 SDUL1 SDUL2 SDUL4 SDUL40 SDUNC

SDUNC1 SDUTL SDUTL1 SDUTL2 SDV53PP SDV53PR SDV53PT SDVADAT

SDVADS SDVER SDVLT SDVPP SDVPR SDVPT SDVSIT SDVSIT0

SDVSIT2 SDWARD VACPT VADATE VADPT VADPT0 VADPT1 VADPT2

VADPT3 VADPT30 VADPT31 VADPT32 VADPT4 VADPT5 VADPT6 VADPT60

VADPT61 VADPT62 VAFADDR VAFEDCAP VAFEDG VAFEDG1 VAFEDOHL VAFEDUTL

VAFHLFNC VAFHLPID VAFHLZCT VAFHLZDP VAFHLZEL VAFHLZEM VAFHLZGD VAFHLZIC

VAFHLZMT VAFHLZPD VAFHLZTA VALM VALM0 VALM00 VALM1 VALM10

VALM11 VALM2 VALM4 VALM40 VALMD VALMI001 VALMI002 VALMI003

VALMI004 VALMI005 VALMI006 VALMI007 VALMI008 VALMI009 VALMINI0 VALMINI1

VALMINI2 VALMINI3 VALMINI4 VALMINIT VALMINIY VALML VALMNTEG VALMO001

VALMO002 VALMO003 VALMO004 VALMO005 VALMONI1 VALMONI2 VALMONI3 VALMONIT

VALMPP VALMPRE VALMPT VALMPT1 VALMW VALMW1 VALMW2 VALMW3

VALMW4 VALMW5 VALMWB VALMXQ01 VALMXQ02 VALMXQ03 VALMXQ04 VALMXQ05

VALMXQ06 VALMXQ07 VALMXQ08 VALMXQ09 VALMXQ10 VALMXQ11 VALMXQ12 VALMXQ13

VALMXQ14 VALMXQ15 VASITE VASITE0 VASITE1 VATRAN VATREDIT VAUQWK

VAUTL VAUTOMA

1762 routines

PIMS Resource Requirements

Algorithms

65.1 ADT TU

(#101.2/13,750)

(Patients Treated/13,750)

65.2 ADT DISK

(#101.2/1000) + (#14.11/10)

(Patients Treated/1000) + (Wards/10)

66.1 REG TU

MAX(#14.2/125,000,.04)

(Applications/125,000) (minimum .04)

66.2 REG DISK

MAX(#14.2/200,1)

(Applications/200) (minimum 1 MB)

67.1 SCH TU

\#103/215,000

(Outpatient Visits/215,000)

67.2 SCH DISK

(#14.42\*12) + (#103\*1.7)/1000

((Clinics\*12) + (Outpatient Visits\*1.5)/1000)

64.1 PTF TU

\$S(#101.2:MAX(101.2/65,000,.05,1:0)

(Patients Treated/65,000) (minimum .05)

64.2 PTF DISK

(#101.2/1700)

(Patients Treated/1700)

List Manager Introduction

The List Manager was originally released as part of MAS v5.2. It was distributed in the SDUL namespace. However, the data dictionaries, templates, and protocols were bundled in the Scheduling package inits as part of SDINI\* routines.

Since the initial distribution, other packages, outside of PIMS, have showed interest in using the utility. As a result, List Manager has been separated from the Scheduling package and placed in the VALM namespace as its own package. Numerous enhancements have been made in this VALM version that will not be included in the SDUL version. By making List Manager a stand-alone package, it will be easier to enhance and distribute.

The SDUL will still be distributed with the Scheduling package of PIMS for backwards compatibility. Other packages have already distributed software that utilizes the SDUL version. The SDUL will eventually be phased out completely as these other packages convert to VALM. During this interim phase, however, the functionality of the SDUL version will remain fixed.

List Manager Package Integration

The following package versions (or higher) MUST be installed PRIOR to loading this version of List Manager.

> Kernel v7.0

> VA FileMan v19.0

> Order Entry v1.96

The VALMINIT inits will install the version of the XQOR\* routines that were distributed as part of Order Entry v2.5. If Order Entry v2.5 has already been installed, the post-init process will not load the XQOR\* routines. (Please note that the version numbers on the XQOR\* routines will be 6.7 even though they were released with version 2.5 of Order Entry.)

Finally, the XQOR\* routines distributed as part of List Manager contain changes introduced in patches OR\*2.5\*14 and OR\*2.5\*15. These patches affect routines XQOR1 and XQORO. (See the XQOR Patches section of this manual for a copy of these patches.)

List Manager Installation

<u>Step</u> <u>Description</u>

1 Get users off system(s).

2 Backup system(s).

3 Disable routine mapping, if applicable. Disable journalling.

4 Sign into UCI where package is to be loaded.

(Use 28k partition for MSM)

5 Verify that DUZ, DT, DTIME and U are defined and DUZ(0)="@". DUZ variable must be defined as an active user number and DUZ(0) variable must equal "@" in order to initialize.

6 D ^VALMINIT -- List Manager

Follow List Manager Installation Dialogues Section for List Manager install dialogues.

7 Rebuild map set. We recommend the following MAS routines be mapped.

VALM VALM0 VALM00 VALM1 VALM10 VALM11 VALM2

VALM4 VALM40

8 Bring systems back on line.

9 Please see the following chart for List Manager initialization time estimates for the installation times at our test sites.

MSM VAX

VALMINIT 2 min. 3 min.

10 In order to effectively use the List Manager, the following terminal type attributes should be defined.

> Attribute Value for a VT-100 terminal

> Form Feed: \#,\$C(27,91,50,74,27,91,72)

> XY CRT W \$C(27,91),DY+1,\$C(59),DX+1,\$C(72)

> Erase to End of Page \$C(27,91,74)

> Insert Line \$C(27,"\[1L")

> Underline On \$C(27,91,52,109)

> Underline Off \$C(27,91,109)

> High Intensity (Bold) \$C(27,91,49,109)

> Normal Intensity (Reset) \$C(27,91,109)

> Save Cursor \$C(27,55)

> Restore Cursor \$C(27,56)

> Set Top/Bottom Margins \$C(27,\*91)\_(+IOTM)\_\$C(59)\_(+IOBM)\_\$C(114)

> SGR Attributes Off \$C(27,91,109)

11 Move XQOR\* and VALMX\* Routines.

If the XQOR\* routines were loaded as part of the post-init process, you will need to move XQOR\* to all systems.

The VALMX\* routines contain compiled print and input templates. Currently, there is only one print template being compiled and no input templates.

List Manager Installation Dialogues

1\. If the site has Order Entry v2.5 installed, the List Manager install will be similar to the following.

\>D ^VALMINIT

This version (#1) of 'VALMINIT' was created on 08-JUN-1993

(at ALBANY ISC VAX DEVELOPMENT, by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

\>\>\> Checking the version of XQOR\*...ok.

I AM GOING TO SET UP THE FOLLOWING FILES:

409.61 LIST TEMPLATE

> **NOTE:** You already have the 'LIST TEMPLATE' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// (NO)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

...SORRY, LET ME PUT YOU ON 'HOLD' FOR A SECOND.................

'VALM DEMO APPLICATION' Option Filed..........

Compiling VALM LIST TEMPLATE print template of File 409.61......................

...........

'VALMXP' ROUTINE FILED

'VALMXP1' ROUTINE FILED.....................

NO SECURITY-CODE PROTECTION HAS BEEN MADE

This version of 'VALMONIT' was created on 08-JUN-1993

(at ALBANY ISC VAX DEVELOPMENT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please.........

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace.

'VALM BLANK 1' Protocol Filed

'VALM BLANK 2' Protocol Filed

'VALM BLANK 3' Protocol Filed

'VALM BLANK 4' Protocol Filed

'VALM BLANK 5' Protocol Filed

'VALM BLANK 6' Protocol Filed

'VALM CAPTION EDIT' Protocol Filed

'VALM CHANGE LIST' Protocol Filed

'VALM DEMO CHANGE PACKAGE' Protocol Filed

'VALM DEMO DESC' Protocol Filed

'VALM DEMO MENU' Protocol Filed

VALM DEMO PROTOCOL EDIT added as item to VALM DEMO MENU.

VALM EXPAND added as item to VALM DEMO MENU.

VALM DEMO DESC added as item to VALM DEMO MENU.

VALM DEMO CHANGE PACKAGE added as item to VALM DEMO MENU.

'VALM DEMO PRINT' Protocol Filed

'VALM DEMO PROTOCOL EDIT' Protocol Filed

'VALM DEMOGRAPHICS' Protocol Filed

'VALM DISPLAY' Protocol Filed

'VALM DISPLAY W/EXPAND' Protocol Filed

VALM EXPAND added as item to VALM DISPLAY W/EXPAND.

'VALM DOWN A LINE' Protocol Filed

'VALM EDIT ALL' Protocol Filed

VALM DEMOGRAPHICS added as item to VALM EDIT ALL.

VALM LIST REGION EDIT added as item to VALM EDIT ALL.

VALM PROTOCOL INFORMATION added as item to VALM EDIT ALL.

VALM MUMPS CODE EDIT added as item to VALM EDIT ALL.

VALM OTHER FIELDS added as item to VALM EDIT ALL.

VALM CAPTION EDIT added as item to VALM EDIT ALL.

'VALM EDITOR' Protocol Filed

'VALM EXPAND' Protocol Filed

'VALM FIRST SCREEN' Protocol Filed

'VALM GOTO PAGE' Protocol Filed

'VALM HIDDEN ACTIONS' Protocol Filed

VALM NEXT SCREEN added as item to VALM HIDDEN ACTIONS.

VALM PREVIOUS SCREEN added as item to VALM HIDDEN ACTIONS.

VALM UP ONE LINE added as item to VALM HIDDEN ACTIONS.

VALM DOWN A LINE added as item to VALM HIDDEN ACTIONS.

VALM REFRESH added as item to VALM HIDDEN ACTIONS.

VALM PRINT SCREEN added as item to VALM HIDDEN ACTIONS.

VALM PRINT LIST added as item to VALM HIDDEN ACTIONS.

VALM RIGHT added as item to VALM HIDDEN ACTIONS.

VALM LEFT added as item to VALM HIDDEN ACTIONS.

VALM TURN ON/OFF MENUS added as item to VALM HIDDEN ACTIONS.

VALM SEARCH LIST added as item to VALM HIDDEN ACTIONS.

VALM QUIT added as item to VALM HIDDEN ACTIONS.

VALM LAST SCREEN added as item to VALM HIDDEN ACTIONS.

VALM FIRST SCREEN added as item to VALM HIDDEN ACTIONS.

VALM GOTO PAGE added as item to VALM HIDDEN ACTIONS.

VALM BLANK 2 added as item to VALM HIDDEN ACTIONS.

VALM BLANK 3 added as item to VALM HIDDEN ACTIONS.

VALM BLANK 4 added as item to VALM HIDDEN ACTIONS.

'VALM INPUT TEMPLATE EDIT' Protocol Filed

'VALM LAST SCREEN' Protocol Filed

'VALM LEFT' Protocol Filed

'VALM LIST ENTRY' Protocol Filed

VALM DEMOGRAPHICS added as item to VALM LIST ENTRY.

VALM PROTOCOL INFORMATION added as item to VALM LIST ENTRY.

VALM LIST REGION EDIT added as item to VALM LIST ENTRY.

VALM OTHER FIELDS added as item to VALM LIST ENTRY.

VALM MUMPS CODE EDIT added as item to VALM LIST ENTRY.

VALM CAPTION EDIT added as item to VALM LIST ENTRY.

VALM CHANGE LIST added as item to VALM LIST ENTRY.

VALM EDIT ALL added as item to VALM LIST ENTRY.

VALM PROTOCOL EDIT added as item to VALM LIST ENTRY.

VALM RUN LIST added as item to VALM LIST ENTRY.

VALM INPUT TEMPLATE EDIT added as item to VALM LIST ENTRY.

'VALM LIST REGION EDIT' Protocol Filed

'VALM MUMPS CODE EDIT' Protocol Filed

'VALM NEXT SCREEN' Protocol Filed

'VALM OTHER FIELDS' Protocol Filed

'VALM PREVIOUS SCREEN' Protocol Filed

'VALM PRINT LIST' Protocol Filed

'VALM PRINT SCREEN' Protocol Filed

'VALM PROTOCOL EDIT' Protocol Filed

'VALM PROTOCOL INFORMATION' Protocol Filed

'VALM QUIT' Protocol Filed

'VALM REFRESH' Protocol Filed

'VALM RIGHT' Protocol Filed

'VALM RUN LIST' Protocol Filed

'VALM SEARCH LIST' Protocol Filed

'VALM TURN ON/OFF MENUS' Protocol Filed

'VALM UP ONE LINE' Protocol Filed

'VALM WORKBENCH' Protocol Filed

VALM DEMOGRAPHICS added as item to VALM WORKBENCH.

VALM PROTOCOL INFORMATION added as item to VALM WORKBENCH.

VALM LIST REGION EDIT added as item to VALM WORKBENCH.

VALM OTHER FIELDS added as item to VALM WORKBENCH.

VALM MUMPS CODE EDIT added as item to VALM WORKBENCH.

VALM CAPTION EDIT added as item to VALM WORKBENCH.

VALM CHANGE LIST added as item to VALM WORKBENCH.

VALM EDIT ALL added as item to VALM WORKBENCH.

VALM PROTOCOL EDIT added as item to VALM WORKBENCH.

VALM RUN LIST added as item to VALM WORKBENCH.

VALM INPUT TEMPLATE EDIT added as item to VALM WORKBENCH.

VALM EDITOR added as item to VALM WORKBENCH.

OK, Protocol Installation is Complete.

\>\>\> List Template installation...

'VALM DEMO APPLICATION' List Template...Filed.

'VALM WORKBENCH' List Template...Filed.

2\. If the site has NOT installed Order Entry v2.5, the List Manager install dialogue will be similar to the following.

\>D ^VALMINIT

This version (#1) of 'VALMINIT' was created on 08-JUN-1993

(at ALBANY ISC VAX DEVELOPMENT, by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

\>\>\> Checking the version of XQOR\*...The current version of XQOR\* is 6.5.List Manager requires version 6.7 or greater.As part of the post-init, version 6.7 will be installed.Continue with the installation? No// YES

I AM GOING TO SET UP THE FOLLOWING FILES:

409.61 LIST TEMPLATE

> **NOTE:** You already have the 'LIST TEMPLATE' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// (NO)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

...SORRY, LET ME PUT YOU ON 'HOLD' FOR A SECOND.................

'VALM DEMO APPLICATION' Option Filed..........

Compiling VALM LIST TEMPLATE print template of File 409.61......................

...........

'VALMXP' ROUTINE FILED

'VALMXP1' ROUTINE FILED.....................

NO SECURITY-CODE PROTECTION HAS BEEN MADE

This version of 'VALMONIT' was created on 08-JUN-1993

(at ALBANY ISC VAX DEVELOPMENT, by OE/RR V.2.5)

PROTOCOL INSTALLATION

...OK, this may take a while, hold on please.........

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace..

Located in the VALM (LIST MANAGER) namespace.

'VALM BLANK 1' Protocol Filed

'VALM BLANK 2' Protocol Filed

'VALM BLANK 3' Protocol Filed

'VALM BLANK 4' Protocol Filed

'VALM BLANK 5' Protocol Filed

'VALM BLANK 6' Protocol Filed

'VALM CAPTION EDIT' Protocol Filed

'VALM CHANGE LIST' Protocol Filed

'VALM DEMO CHANGE PACKAGE' Protocol Filed

'VALM DEMO DESC' Protocol Filed

'VALM DEMO MENU' Protocol Filed

VALM DEMO PROTOCOL EDIT added as item to VALM DEMO MENU.

VALM EXPAND added as item to VALM DEMO MENU.

VALM DEMO DESC added as item to VALM DEMO MENU.

VALM DEMO CHANGE PACKAGE added as item to VALM DEMO MENU.

'VALM DEMO PRINT' Protocol Filed

'VALM DEMO PROTOCOL EDIT' Protocol Filed

'VALM DEMOGRAPHICS' Protocol Filed

'VALM DISPLAY' Protocol Filed

'VALM DISPLAY W/EXPAND' Protocol Filed

VALM EXPAND added as item to VALM DISPLAY W/EXPAND.

'VALM DOWN A LINE' Protocol Filed

'VALM EDIT ALL' Protocol Filed

VALM DEMOGRAPHICS added as item to VALM EDIT ALL.

VALM LIST REGION EDIT added as item to VALM EDIT ALL.

VALM PROTOCOL INFORMATION added as item to VALM EDIT ALL.

VALM MUMPS CODE EDIT added as item to VALM EDIT ALL.

VALM OTHER FIELDS added as item to VALM EDIT ALL.

VALM CAPTION EDIT added as item to VALM EDIT ALL.

'VALM EDITOR' Protocol Filed

'VALM EXPAND' Protocol Filed

'VALM FIRST SCREEN' Protocol Filed

'VALM GOTO PAGE' Protocol Filed

'VALM HIDDEN ACTIONS' Protocol Filed

VALM NEXT SCREEN added as item to VALM HIDDEN ACTIONS.

VALM PREVIOUS SCREEN added as item to VALM HIDDEN ACTIONS.

VALM UP ONE LINE added as item to VALM HIDDEN ACTIONS.

VALM DOWN A LINE added as item to VALM HIDDEN ACTIONS.

VALM REFRESH added as item to VALM HIDDEN ACTIONS.

VALM PRINT SCREEN added as item to VALM HIDDEN ACTIONS.

VALM PRINT LIST added as item to VALM HIDDEN ACTIONS.

VALM RIGHT added as item to VALM HIDDEN ACTIONS.

VALM LEFT added as item to VALM HIDDEN ACTIONS.

VALM TURN ON/OFF MENUS added as item to VALM HIDDEN ACTIONS.

VALM SEARCH LIST added as item to VALM HIDDEN ACTIONS.

VALM QUIT added as item to VALM HIDDEN ACTIONS.

VALM LAST SCREEN added as item to VALM HIDDEN ACTIONS.

VALM FIRST SCREEN added as item to VALM HIDDEN ACTIONS.

VALM GOTO PAGE added as item to VALM HIDDEN ACTIONS.

VALM BLANK 2 added as item to VALM HIDDEN ACTIONS.

VALM BLANK 3 added as item to VALM HIDDEN ACTIONS.

VALM BLANK 4 added as item to VALM HIDDEN ACTIONS.

'VALM INPUT TEMPLATE EDIT' Protocol Filed

'VALM LAST SCREEN' Protocol Filed

'VALM LEFT' Protocol Filed

'VALM LIST ENTRY' Protocol Filed

VALM DEMOGRAPHICS added as item to VALM LIST ENTRY.

VALM PROTOCOL INFORMATION added as item to VALM LIST ENTRY.

VALM LIST REGION EDIT added as item to VALM LIST ENTRY.

VALM OTHER FIELDS added as item to VALM LIST ENTRY.

VALM MUMPS CODE EDIT added as item to VALM LIST ENTRY.

VALM CAPTION EDIT added as item to VALM LIST ENTRY.

VALM CHANGE LIST added as item to VALM LIST ENTRY.

VALM EDIT ALL added as item to VALM LIST ENTRY.

VALM PROTOCOL EDIT added as item to VALM LIST ENTRY.

VALM RUN LIST added as item to VALM LIST ENTRY.

VALM INPUT TEMPLATE EDIT added as item to VALM LIST ENTRY.

'VALM LIST REGION EDIT' Protocol Filed

'VALM MUMPS CODE EDIT' Protocol Filed

'VALM NEXT SCREEN' Protocol Filed

'VALM OTHER FIELDS' Protocol Filed

'VALM PREVIOUS SCREEN' Protocol Filed

'VALM PRINT LIST' Protocol Filed

'VALM PRINT SCREEN' Protocol Filed

'VALM PROTOCOL EDIT' Protocol Filed

'VALM PROTOCOL INFORMATION' Protocol Filed

'VALM QUIT' Protocol Filed

'VALM REFRESH' Protocol Filed

'VALM RIGHT' Protocol Filed

'VALM RUN LIST' Protocol Filed

'VALM SEARCH LIST' Protocol Filed

'VALM TURN ON/OFF MENUS' Protocol Filed

'VALM UP ONE LINE' Protocol Filed

'VALM WORKBENCH' Protocol Filed

VALM DEMOGRAPHICS added as item to VALM WORKBENCH.

VALM PROTOCOL INFORMATION added as item to VALM WORKBENCH.

VALM LIST REGION EDIT added as item to VALM WORKBENCH.

VALM OTHER FIELDS added as item to VALM WORKBENCH.

VALM MUMPS CODE EDIT added as item to VALM WORKBENCH.

VALM CAPTION EDIT added as item to VALM WORKBENCH.

VALM CHANGE LIST added as item to VALM WORKBENCH.

VALM EDIT ALL added as item to VALM WORKBENCH.

VALM PROTOCOL EDIT added as item to VALM WORKBENCH.

VALM RUN LIST added as item to VALM WORKBENCH.

VALM INPUT TEMPLATE EDIT added as item to VALM WORKBENCH.

VALM EDITOR added as item to VALM WORKBENCH.

OK, Protocol Installation is Complete.

\>\>\> List Template installation...

'VALM DEMO APPLICATION' List Template...Filed.

'VALM WORKBENCH' List Template...Filed.

\>\>\> Installing XQOR\* routines from VALMXQ\* routines...XQOR...filedXQOR1...filedXQOR2...filedXQOR3...filedXQOR4...filedXQORD...filedXQORD1...filedXQORM...filedXQORM1...filedXQORM2...filedXQORM3...filedXQORM4...filedXQORM5...filedXQORMX...filedXQORO...filed

\>

List Manager Routine List

VALM VALM0 VALM00 VALM1 VALM10 VALM11

VALM2 VALM4 VALM40 VALMD VALMI001 VALMI002

VALMI003 VALMI004 VALMI005 VALMI006 VALMI007 VALMI008

VALMI009 VALMINI0 VALMINI1 VALMINI2 VALMINI3 VALMINI4

VALMINIT VALMINIY VALML VALMNTEG VALMO001 VALMO002

VALMO003 VALMO004 VALMO005 VALMONI1 VALMONI2 VALMONI3

VALMONIT VALMPP VALMPRE VALMPT VALMPT1 VALMW

VALMW1 VALMW2 VALMW3 VALMW4 VALMW5 VALMWB

VALMXQ01 VALMXQ02 VALMXQ03 VALMXQ04 VALMXQ05 VALMXQ06

VALMXQ07 VALMXQ08 VALMXQ09 VALMXQ10 VALMXQ11 VALMXQ12

VALMXQ13 VALMXQ14 VALMXQ15

63 routines restored

List Manager - XQOR Patches

DHCP Patch Display Page: 1

=============================================================================

Run Date: AUG 2, 1993 Designation: OR\*2.5\*14

Package : OR - ORDER ENTRY/RESULTS RE Priority : MANDATORY

Version : 2.5 SEQ \#8 Status : VERIFIED

=============================================================================

Subject: Incompatibility with Kernel 7.1

Category: ROUTINE

Description:

===========

INSTALLATION: This patch may be installed prior to loading Kernel 7.1. Users

need not be off the system when applying this patch; however, it should be

done during off-peak times since there is always a chance that someone might

be errored off the system because they were using an option that invoked the

routine being edited.

SPECIAL NOTE: Two of the four routines included in this patch are XQOR

namespaced. The XQOR\* routines are a set of utilities for the Protocol file

\(101\) and are released as part of the Order Entry/Results Reporting (OR)

package. They were released with a version number of 6.7 and may become part

of the Kernel package at a later date. For the time being any patches to

XQOR namespaced routines will be released under the OE/RR package.

PREVIOUS PATCHES:

The routine OR4 has previously been patched with OR\*2.5\*2 and OR\*2.5\*6

PROBLEM: There is an incompatability between OERR 2.5 and Kernel 7.1. Since

the release of OERR 2.5, the code was changed in the Kernel 7.1 %ZOSV routine

for system capacity checking. A different variable than what was expected is

returned from the call to %ZOSV resulting in an undefined error.

This patch makes the changes needed to check for the variable XQXFLG.

Routine Information:

====================

Routine Name: OR4

Description of Changes:

Line: ORUP+2

r XUCMP

w XQXFLG

r XUCMP

w \$P(XQXFLG,"^",2)=1

Line now looks like:

. I \$L(\$T(LOGRSRC^%ZOSV)) D:'\$D(XQXFLG) ABT^XQ12 D:\$P(XQXFLG,"^",2)=1 LOGRSRC^)

Line: ORUP+5

r XUCMP

w XQXFLG

r XUCMP

w \$P(XQXFLG,"^",2)=1

DHCP Patch Display Page: 2

=============================================================================

Run Date: AUG 2, 1993 Designation: OR\*2.5\*14

Package : OR - ORDER ENTRY/RESULTS RE Priority : MANDATORY

Version : 2.5 SEQ \#8 Status : VERIFIED

=============================================================================

Line now looks like:

. I \$L(\$T(LOGRSRC^%ZOSV)) D:'\$D(XQXFLG) ABT^XQ12 D:\$P(XQXFLG,"^",2)=1 LOGRSRC^)

Routine Checksum:

15197207

Routine Name: ORF32

Description of Changes:

Line: ACT+4

r XUCMP

w XQXFLG

r XUCMP

w \$P(XQXFLG,"^",2)=1

Line now looks like:

. I \$L(\$T(LOGRSRC^%ZOSV)) D:'\$D(XQXFLG) ABT^XQ12 D:\$P(XQXFLG,"^",2)=1 LOGRSRC^)

Line: ACT+7

r XUCMP

w XQXFLG

r XUCMP

w \$P(XQXFLG,"^",2)=1

Line now looks like:

. I \$L(\$T(LOGRSRC^%ZOSV)) D:'\$D(XQXFLG) ABT^XQ12 D:\$P(XQXFLG,"^",2)=1 LOGRSRC^)

Routine Checksum:

5305497

Routine Name: XQOR1

Description of Changes:

Line: LOOP+5

r XUCMP

w XQXFLG

r XUCMP

w \$P(XQXFLG,"^",2)=1

Line now looks like:

. I \$L(\$T(LOGRSRC^%ZOSV)),\$G(^TMP("XQORS",\$J,XQORS,"REF"))\["ORD(101,",\$P(@(^("(

^(0),"^") D:'\$D(XQXFLG) ABT^XQ12 D:\$P(XQXFLG,"^",2)=1 LOGRSRC^%ZOSV("\*"\_ORX)

Line: LOOP+7

r XUCMP

w XQXFLG

r XUCMP

w \$P(XQXFLG,"^",2)=1

Line now looks like:

DHCP Patch Display Page: 3

=============================================================================

Run Date: AUG 2, 1993 Designation: OR\*2.5\*14

Package : OR - ORDER ENTRY/RESULTS RE Priority : MANDATORY

Version : 2.5 SEQ \#8 Status : VERIFIED

=============================================================================

I \$L(\$T(LOGRSRC^%ZOSV)),\$G(^TMP("XQORS",\$J,XQORS,"REF"))\["ORD(101,",\$P(@(^("RE(

0),"^") D:'\$D(XQXFLG) ABT^XQ12 D:\$P(XQXFLG,"^",2)=1 LOGRSRC^%ZOSV("\*"\_ORX)

Routine Checksum:

12743758

Routine Name: XQORO

Description of Changes:

Line: ENTRY+5

r XUCMP

w XQXFLG

r XUCMP

w \$P(XQXFLG,"^",2)=1

Line now looks like:

I \$L(\$T(LOGRSRC^%ZOSV)),XQORNOD\["ORD(101,",\$P(^ORD(101,+XQORNOD,0),"^",4)'="M"F

LG,"^",2)=1 S ORPRFRM="\*"\_\$P(^ORD(101,+XQORNOD,0),"^") D LOGRSRC^%ZOSV("\*"\_ORPR)

Line: EXIT+6

r XUCMP

w XQXFLG

r XUCMP

w \$P(XQXFLG,"^",2)=1

Line now looks like:

I \$D(ORPRFRM),\$L(\$T(LOGRSRC^%ZOSV)) D:'\$D(XQXFLG) ABT^XQ12 D:\$P(XQXFLG,"^",2)=M

Routine Checksum:

11401832

=============================================================================

User Information:

Entered By : ANDRUS,RUSTY Date Entered : JUL 15,1993

Completed By: FROMMATER,RANDAL A Date Completed: JUL 27,1993

Verified By : DEFA,TANA Date Verified : JUL 29,1993

=============================================================================

DHCP Patch Display Page: 1

=============================================================================

Run Date: AUG 2, 1993 Designation: OR\*2.5\*15

Package : OR - ORDER ENTRY/RESULTS RE Priority : MANDATORY

Version : 2.5 SEQ \#9 Status : VERIFIED

=============================================================================

Subject: Backwards Incompatibility

Category: ROUTINE

Description:

===========

INSTALLATION:

Users need not be off the system when applying this patch; however, it

should be done during off-peak time since there is always a chance that

someone might be errored off the system because they were using an option

that called the routine being edited.

SPECIAL NOTE: The XQOR\* routines are a set of utilities for the Protocol

file (101) and are released as part of Order Entry/Results Reporting (OR)

package. They were released with a version number of 6.7 and may become part

of the kernel package at a later date. For the time being any patches to

XQOR namespaced routines will be released under the OE/RR package.

PREVIOUS PATCHES:

The routine XQORO has previously been patched with OR\*2.5\*14

PROBLEM: Backwards incompatibility with OE/RR 1.96. The new release of PIMS

5.3 requires the new functionality provided in the XQOR version 6.7 routines

that were released with OE/RR version 2.5. Since PIMS 5.3 does not require

OE/RR 2.5 to be installed, they are exporting the XQOR routines with their

release to be loaded if OE/RR 2.5 is not present. It is then possible to

have version 6.7 of XQOR routines and version 1.96 of OE/RR routines. The

incompatibility occurs because the routine XQORO references the routine OR4

that does not exist in 1.96.

This patch corrects the incompatibility by calling an entry point in OR1.

Routine Information:

====================

Routine Name: XQORO

Description of Changes:

Line: EXIT+3

r OR4

w OR1

Line now looks like:

D RSTR,AFT^OR1,RSTR K ^TMP("XQORS",\$J,0,"CTXT","ADD"),^TMP("XQORS",\$J,XQORS,"C"

Routine Checksum:

11401787

DHCP Patch Display Page: 2

=============================================================================

Run Date: AUG 2, 1993 Designation: OR\*2.5\*15

Package : OR - ORDER ENTRY/RESULTS RE Priority : MANDATORY

Version : 2.5 SEQ \#9 Status : VERIFIED

=============================================================================

=============================================================================

User Information:

Entered By : ANDRUS,RUSTY Date Entered : JUL 15,1993

Completed By: FROMMATER,RANDAL A Date Completed: JUL 28,1993

Verified By : DEFA,TANA Date Verified : JUL 29,1993

=============================================================================