---
title: Incomplete Records Tracking (IRT) Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: DGJ
app_name: Incomplete Records Tracking (IRT)
section: CLI
app_status: active
pkg_ns: DGJ
patch_ver: 1
patch_id: DGJ*1
group_key: "DGJ:DGJ:1"
file_numbers: []
security_keys: []
menu_options: 0
description: There are no major changes in this version from PIMS V. 5.3. The purpose of this version is to create Incomplete Records Tracking into its own namespace (DGJ) separate from the Registration package (DG).
audience: 
keywords: 
  - install
  - package
  - records
  - installation
  - incomplete
  - tracking
  - distribution
  - control
  - routine
  - medical
page_count: 0
word_count: 1213
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Incomplete_Records_Tracking(IRT)/dgj1_0_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Incomplete_Records_Tracking(IRT)/dgj1_0_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=124"
---

![](incomplete-records-tracking-irt-version-1-installation-guide/001.png)

Incomplete Records Tracking (IRT)Installation Guide

April 2002

V*IST*A Software Design & Development

Table of Contents

Introduction 1

Package Integration 2

Installation 3

Installation Dialogue 5

Routines 10

> Routine List 10

> Routine Checksums 11

Introduction

There are no major changes in this version from PIMS V. 5.3. The purpose of this version is to create Incomplete Records Tracking into its own namespace (DGJ) separate from the Registration package (DG).

This version does send out one new parameter - Default Medical Record Type field (#100.3) - found in the Medical Center Division file (#40.8). Populating this field may be done through the Set Up IRT Parameters option and will be useful at integrated sites with different names for their Medical Record file rooms.

Package Integration

The following package versions (or higher) MUST be installed PRIOR to loading this version of Incomplete Records Tracking.

<u>Package</u> <u>Version</u>

PIMS 5.3

Installation

<u>Step</u> <u>Description</u>

1 The files containing the KIDS installation file and documentation can be found on the ANONYMOUS.SOFTWARE directory:

DGJ1_0_IG.PDF DGJ1_0_TM.PDF DGJ1_0_UM.PDF DGJ1_0.KID

2 Print out/review the existing IRT parameters for each division. These are fields (#100.01-100.09, 100.1, and 100.2) found in the Medical Center Division (#40.8) file. Print out/review the IRT Short Form List Group (mail group) (#513) field found in the MAS Parameters (#43) file.

3 Backup system(s).

4 In order to minimize the impact of protocol \[DGPM MOVEMENT EVENTS\], install during a non-peak time, disabling the Bed Control \[DG BED CONTROL\] option. Advise your users not to do any admission, discharges, or transfers during the short time the package is installed.

5 Sign into UCI where package is to be loaded. (Use 28k partition for MSM.)

6 Prior to loading the Incomplete Records Tracking V. 1.0 host file, it is important to delete the Additional Prefix 'DGJ' entry from the Registration package. (See Installation Dialogue Section of this documentation for description.)

7 Load Incomplete Records Tracking V. 1.0 host file. (See Installation Dialogue Section of this document for description.)

8 Verify that DUZ, DT, DTIME, and U are defined and DUZ(0)="@". DUZ variable must be defined as an active user number and DUZ(0) variable must equal "@" in order to initialize.

9 Please answer all initialization questions carefully. We also recommend you slave print the initialization processes. Data that is printed out during the post-inits should be reviewed.

10 Move DGJ\* routines to all systems, as appropriate.

11 Bring systems back on line.

<u>Step</u> <u>Description</u>

12 (Optional) Running the Build Primary Menu Trees option on the Menu Management Menu after the install may improve system performance during the first day of operation.

13 Review the IRT Parameters and IRT Short Form List Group entries from Step 2.

14 (Optional) Populate the DEFAULT MEDICAL RECORD TYPE (#100.3) field in the MEDICAL CENTER DIVISION (#40.8) file. This may also be done through the Set Up IRT Parameters option. If the field is left blank, MEDICAL RECORDS record type will be used (compatible with pre-installation functionality). This field will be useful to integrated sites which may have different names for the Medical Records departments.

Installation Dialogue

Select OPTION NAME:

\>D P^DI

VA FileMan 22.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: PACKAGE//

EDIT WHICH FIELD: ALL// ADDITIONAL PREFIXES (multiple)

EDIT WHICH ADDITIONAL PREFIXES SUB-FIELD: ALL//

THEN EDIT FIELD:

Select PACKAGE NAME: REGISTRATION DG

Select ADDITIONAL PREFIXES: VIC// DGJ

ADDITIONAL PREFIXES: DGJ// @

SURE YOU WANT TO DELETE THE ENTIRE 'DGJ' ADDITIONAL PREFIXES? Y (Yes)

Select ADDITIONAL PREFIXES:

Select PACKAGE NAME:

Select OPTION:

\>S DUZ(0)="@"

\>ZW

%H=58694,54947

DT=3010912

DTIME=9999

DUZ=100884

DUZ(0)=@

DUZ(1)=

DUZ(2)=500

DUZ("AG")=V

DUZ("BUF")=1

DUZ("LANG")=

IO(0)=\_TNA1436:

U=^

MNT,VBB\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT320

You have 1 new message.

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Select Kernel Installation & Distribution System Option: Installation

Select Installation Option: Load a Distribution

Enter a Host File: DGJ1_0.KID;1

KIDS Distribution saved on Mar 12, 2002@09:11:56

Comment: Incomplete Records Tracking (DGJ) V.1.0

This Distribution contains Transport Globals for the following Package(s):

DGJ 1.0

Distribution OK!

Want to Continue with Load? YES// \<ret\>

Loading Distribution...

Build DGJ 1.0 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES// \<ret\>

DGJ 1.0

Will first run the Environment Check Routine, DGJ1INIT

Environment check complete and okay.

Use INSTALL NAME: DGJ 1.0 to install this Distribution.

Select Installation Option: Verify Checksums in Transport Global

Select INSTALL NAME: DGJ 1.0 Loaded from Distribution 3/12/02@09:15:23

=\> Incomplete Records Tracking (DGJ) V.1.0 ;Created on Mar 12, 2002@09:11:56

This Distribution was loaded on Mar 12, 2002@09:15:23 with header of

Incomplete Records Tracking (DGJ) V.1.0 ;Created on Mar 12, 2002@09:11:56

It consisted of the following Install(s):

DGJ 1.0

DEVICE: HOME// UCX/TELNET

PACKAGE:DGJ1.0 Mar 12,2002 4:25pm PAGE 1

37 Routine checked, 0 failed.

Select Installation Option: Install Package(s)

Select INSTALL NAME: DGJ 1.0 Loaded from Distribution 3/12/02@09:15:23

=\> Incomplete Records Tracking (DGJ) V.1.0 ;Created on Mar 12, 2002@09:11:56

This Distribution was loaded on Mar 12, 2002@09:15:23 with header of

Incomplete Records Tracking (DGJ) V.1.0 ;Created on Mar 12, 2002@09:11:56

It consisted of the following Install(s):

DGJ 1.0

Checking Install for Package DGJ 1.0

Will first run the Environment Check Routine, DGJ1INIT

\>\> Environment check complete and okay.

Install Questions for DGJ 1.0

Incoming Files:

40.8 MEDICAL CENTER DIVISION (Partial Definition)

> **NOTE:** You already have the 'MEDICAL CENTER DIVISION' File.

43 MAS PARAMETERS (Partial Definition)

> **NOTE:** You already have the 'MAS PARAMETERS' File.

393 INCOMPLETE RECORDS

> **NOTE:** You already have the 'INCOMPLETE RECORDS' File.

393.1 MAS SERVICE

> **NOTE:** You already have the 'MAS SERVICE' File.

393.2 IRT STATUS

> **NOTE:** You already have the 'IRT STATUS' File.

393.3 IRT TYPE OF DEFICIENCY

> **NOTE:** You already have the 'IRT TYPE OF DEFICIENCY' File.

393.41 TYPE OF CATEGORY

> **NOTE:** You already have the 'TYPE OF CATEGORY' File.

405 PATIENT MOVEMENT (Partial Definition)

> **NOTE:** You already have the 'PATIENT MOVEMENT' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// \<ret\>

Enter options you wish to mark as 'Out Of Order': DGJ IRT MENU Incomplete Records Tracking Menu

Enter options you wish to mark as 'Out Of Order': DG BED CONTROL

1 DG BED CONTROL Bed Control Menu

2 DG BED CONTROL EXTENDED Extended Bed Control

3 DG BED CONTROL MOVEMENT EDIT Edit Bed Control Movement Types

CHOOSE 1-3: 1 DG BED CONTROL Bed Control Menu

Enter options you wish to mark as 'Out Of Order':

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<select printer\>

Install Started for DGJ 1.0 :

Mar 12, 2002@09:17:38

Build Distribution Date: Mar 12, 2002

Installing Routines:

Mar 12, 2002@09:17:59

Installing Data Dictionaries:

Mar 12, 2002@09:17:45

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing INPUT TEMPLATE

Installing PROTOCOL

Installing LIST TEMPLATE

Installing OPTION

Mar 12, 2002@09:17:56

Running Post-Install Routine: POST^DGJ1INIT

Updating PACKAGE File...

SHORT DESCRIPTION field complete.

DESCRIPTION field complete.

FILE field complete.

FIELD field complete.

Updating Routine file...

The following Routines were created during this install:

DGJXE

DGJXE1

DGJXE2

DGJXE3

DGJXE4

DGJXE5

DGJ 1.0

────────────────────────────────────────────────────────────────────────

DGJXE6

DGJXE7

DGJXA

DGJXA1

DGJXA2

DGJXA3

DGJXA4

DGJXA5

DGJXA6

DGJXA7

DGJXA8

Updating KIDS files...

DGJ 1.0 Installed.

Mar 12, 2002@09:18:03

Install Message sent \#346465

────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

Routines

Routine List

DGJ1INIP DGJ1INIT DGJBGJ DGJBGJ1 DGJHELP DGJOPRT DGJOPRT1 DGJOPRT2

DGJOPRT3 DGJOTP DGJOTP1 DGJOTP2 DGJOTP3 DGJOTPUL DGJPAR DGJPAR1

DGJPDEF DGJPDEF1 DGJPDEF2 DGJPDEF3 DGJSUM DGJTADD DGJTDEL DGJTEE

DGJTEE1 DGJTEE2 DGJTEE3 DGJTEVT DGJTHLP DGJTHLP1 DGJTUDIS DGJTUTL

DGJTVW DGJTVW1 DGJTVW2 DGJTVW3 DGJUTQ

37 routines

#### Routine Checksums

Before Checksums After Checksums

Routine Name Registration V.5.3 Incomplete Records Tracking V.1.0

========== ============= ==========================

DGJ1INIP NA 3661951

DGJ1INIT NA 2927055

DGJBGJ 17101435 17762236

DGJBGJ1 2253965 5098676

DGJHELP NA 366520

DGJOPRT 7505571 7513428

DGJOPRT1 17222524 17414780

DGJOPRT2 17969394 18118175

DGJOPRT3 12014305 12015556

DGJOTP 12136251 12149351

DGJOTP1 21768333 21783529

DGJOTP2 12122814 12122814

DGJOTP3 16936956 16936956

DGJOTPUL 9915514 9915514

DGJPAR 186014 186014

DGJPAR1 14281443 14281443

DGJPDEF 13686744 13695852

DGJPDEF1 20529386 20545218

DGJPDEF2 18436653 18831133

DGJPDEF3 16267378 16267378

DGJSUM 8005282 8005282

DGJTADD 2567747 2567747

DGJTDEL 4511597 4511597

DGJTEE 19305246 19309237

DGJTEE1 12655066 12655066

DGJTEE2 12161478 12161478

DGJTEE3 14306643 14306643

DGJTEVT 11333449 11333449

DGJTHLP 9134861 9134861

DGJTHLP1 8799972 8799972

DGJTUDIS 4651950 4651950

DGJTUTL 16684941 16684941

DGJTVW 5612957 5612957

DGJTVW1 17594153 17687460

DGJTVW2 8809719 8809719

DGJTVW3 12907948 13001255

DGJUTQ NA 4363497