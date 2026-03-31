---
title: Beneficiary Travel  Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: DGBT
app_name: Beneficiary Travel
section: CLI
app_status: active
pkg_ns: DGBT
patch_ver: 1
patch_id: DGBT*1
group_key: "DGBT:DGBT:1"
file_numbers: []
security_keys: []
menu_options: 0
description: There are no major changes in this version from PIMS V. 5.3. The purpose of this version is to create Beneficiary Travel into its own namespace (DGBT) separate from the Registration package (DG).
audience: 
keywords: 
  - dgbt
  - beneficiary
  - travel
  - install
  - installation
  - dgbtoa
  - package
  - distribution
  - routine
  - journaling
page_count: 0
word_count: 884
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
docx_url: "https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt1_0_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Beneficiary_Travel/dgbt1_0_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=123"
---

![](beneficiary-travel-version-1-installation-guide/001.png)

Beneficiary TravelInstallation Guide

April 2002

V*IST*A Software Design & Development

Table of Contents

Introduction 1

Package Integration 2

Installation 3

Installation Dialogue 4

Routines 8

Journaling 9

Introduction

There are no major changes in this version from PIMS V. 5.3. The purpose of this version is to create Beneficiary Travel into its own namespace (DGBT) separate from the Registration package (DG).

Package Integration

The following package versions (or higher) MUST be installed PRIOR to loading this version of Beneficiary Travel.

<u>Package</u> <u>Version</u>

PIMS 5.3

Installation

<u>Step</u> <u>Description</u>

1 The files containing the KIDS installation file and documentation can be found on the ANONYMOUS.SOFTWARE directory:

DGBT1_0_IG.PDF DGBT1_0_TM.PDF DGBT1_0_UM.PDF DGBT1_0.KID

2 Print out/review the existing Beneficiary Travel parameters under the Beneficiary Travel menu.

3 Backup system(s).

4 Installation should be done at a non-peak time. The Beneficiary Travel Main menu should be disabled during the installation with Beneficiary Travel users off the system.

5 Sign into UCI where package is to be loaded. (Use 28k partition for MSM.)

6 Load Beneficiary Travel V. 1.0 host file. (See Installation Dialogue Section of this document for description.)

7 Verify that DUZ, DT, DTIME, and U are defined and DUZ(0)="@". DUZ variable must be defined as an active user number and DUZ(0) variable must equal "@" in order to initialize.

8 Please answer all initialization questions carefully. We also recommend you slave print the initialization processes. Data that is printed out during the post-inits should be reviewed.

9 Move DGBT\* routines to all systems.

10 Bring systems back on line.

11 (Optional) Running the Build Primary Menu Trees option on the Menu Management Menu after the install may improve system performance during the first day of operation.

12 Review the parameter entries from Step 2.

13 Journaling of the ^DGBT global is mandatory. Verify that journaling on this global is Enabled. (See Journaling Section of this document for description.)

Installation Dialogue

Select OPTION NAME:

\>D P^DI

VA FileMan 22.0

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

Select Installation Option: LOad a Distribution

Enter a Host File: DGBT1_0.KID;1

KIDS Distribution saved on Mar 19, 2002@10:33:17

Comment: Beneficiary Travel V.1.0

This Distribution contains Transport Globals for the following Package(s):

DGBT 1.0

Distribution OK!

Want to Continue with Load? YES// YES

Loading Distribution...

Build DGBT 1.0 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES// YES

DGBT 1.0

Will first run the Environment Check Routine, DGBT1PRE

\>\> Environment check complete and okay.

Use INSTALL NAME: DGBT 1.0 to install this Distribution.

Select Installation Option: Install Package(s)

Select INSTALL NAME: DGBT 1.0 Loaded from Distribution 3/28/02@10:48:02

=\> Beneficiary Travel V.1.0 ;Created on Mar 19, 2002@10:33:17

This Distribution was loaded on Mar 28, 2002@10:48:02 with header of

Beneficiary Travel V.1.0 ;Created on Mar 19, 2002@10:33:17

It consisted of the following Install(s):

DGBT 1.0

Checking Install for Package DGBT 1.0

Will first run the Environment Check Routine, DGBT1PRE

\>\> Environment check complete and okay.

Install Questions for DGBT 1.0

Incoming Files:

43 MAS PARAMETERS (Partial Definition)

> **NOTE:** You already have the 'MAS PARAMETERS' File.

43.1 MAS EVENT RATES (Partial Definition)

> **NOTE:** You already have the 'MAS EVENT RATES' File.

392 BENEFICIARY TRAVEL CLAIM

> **NOTE:** You already have the 'BENEFICIARY TRAVEL CLAIM' File.

392.1 BENEFICIARY TRAVEL DISTANCE

> **NOTE:** You already have the 'BENEFICIARY TRAVEL DISTANCE' File.

392.2 BENEFICIARY TRAVEL CERTIFICATION

> **NOTE:** You already have the 'BENEFICIARY TRAVEL CERTIFICATION' File.

392.3 BENEFICIARY TRAVEL ACCOUNT

> **NOTE:** You already have the 'BENEFICIARY TRAVEL ACCOUNT' File.

392.4 BENEFICIARY TRAVEL MODE OF TRANSPORTATION

> **NOTE:** You already have the 'BENEFICIARY TRAVEL MODE OF TRANSPORTATION' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// YES

Enter options you wish to mark as 'Out Of Order': DGBT BENE TRAVEL MENU

Beneficiary Travel Menu

Enter options you wish to mark as 'Out Of Order':

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Chose your output printer\>

Install Started for DGBT 1.0 :

Mar 28, 2002@10:50:04

Build Distribution Date: Mar 19, 2002

Installing Routines:

Mar 28, 2002@10:50:05

Running Pre-Install Routine: PRE^DGBT1PRE

Installing Data Dictionaries: .

Mar 28, 2002@10:50:09

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing PRINT TEMPLATE

DGBT 1.0

────────────────────────────────────────────────────────────────────────

Installing SORT TEMPLATE

Installing INPUT TEMPLATE

Installing OPTION

Mar 28, 2002@10:50:12

Running Post-Install Routine: POST^DGBT1PRE

Updating PACKAGE File...

SHORT DESCRIPTION field complete.

DESCRIPTION field complete.

FILE field complete.

FIELD field complete.

Updating Routine file...

Updating KIDS files...

DGBT 1.0 Installed.

Mar 28, 2002@10:50:15

Install Message sent \#347703

────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

Routines

Routine List

DGBT1 DGBT1POS DGBT1PRE DGBT2 DGBTCD DGBTCE DGBTCE1 DGBTCR

DGBTCR1 DGBTCR2 DGBTDIST DGBTDIV DGBTDST1 DGBTE DGBTE1 DGBTE1A

DGBTEE DGBTEE1 DGBTEE2 DGBTEF DGBTEF1 DGBTEND DGBTHELP DGBTOA1

DGBTOA2 DGBTOA3 DGBTOA4 DGBTOA5 DGBTOA6 DGBTR DGBTSRCH DGBTUTL

DGBTUTQ

33 routines

Routine Checksums

Before Checksums After Checksums

Routine Name Registration V.5.3 Beneficiary Travel V.1.0

========== ============= ==================

DGBT1 8480857 8480857

DGBT1POS NA 2709650

DGBT1PRE NA 2236658

DGBT2 12774416 12774416

DGBTCD 13829532 13829532

DGBTCE 14541136 14541136

DGBTCE1 5419607 5419607

DGBTCR 12006227 11746140

DGBTCR1 8137574 8137574

DGBTCR2 12956592 12956592

DGBTDIST 8481729 8481729

DGBTDIV NA 774135

DGBTDST1 2237098 2237098

DGBTE 8229618 8229618

DGBTE1 9272372 9272372

DGBTE1A 6223890 6223890

DGBTEE 8387933 8387933

DGBTEE1 11811803 11811803

DGBTEE2 8101499 8132955

DGBTEF 15591466 14955495

DGBTEF1 8927678 8937627

DGBTEND 12830346 12830346

DGBTHELP NA 367129

DGBTOA1 14177005 14205362

DGBTOA2 11981540 11984900

DGBTOA3 15389059 15389059

DGBTOA4 15019918 15019918

DGBTOA5 3360676 3360676

DGBTOA6 8208248 8208248

DGBTR 9324442 9324442

DGBTSRCH 10574383 10574383

DGBTUTL 1356611 1356611

DGBTUTQ NA 4368386

Journaling

DSM Systems

- Locate the Volume Set where ^DGBT is translated
- Run ^%GLOMAN

> \>D ^%GLOMAN

> Global Management Utility

> Global \> ^DGBT

> ^DGBT is currently defined

> 1\. Show GLOBAL Characteristics

> 2\. Change Access Privileges

> 3\. Change Journaling Capability

> 4\. Change DATA GROWTH AREA

> Enter option \> 3

> Journaling \[E=Enabled/D=Disabled\] \<E\>

Cache Systems

- Locate the Namespace where ^DGBT is translated. This will display whether journaling is enabled or not.

> \>D ^%GD

> Device: Right margin: 80=\>

> Show detail? No =\> Yes

> Global Directory Display of VAH

> 9:33 AM Apr 05 2002

> Global Vacant Own Grp Wld Net Growth 1st PB Jrn

> ^%Z RWD R R RWD 3296 325 Y

> Data Location: y:\rou\\

> Lock Location: y:\rou\\

> Replications:

> Collation: Cache standard

> ^DGBT RWD N N RWD 10296 128 Y

> Data Location: w:\vaa\\

> Lock Location: w:\vaa\\

> Replications:

> Collation: Cache standard

- If journaling (Jrn) is N, change to the namespace where ^DGBT is located and enable journaling.

> VAH\>D ^%CD

> Namespace: ^^W:\VAA

> You're in namespace ^^w:\vaa\\

> Default directory is w:\vaa\\

> ^^w:\vaa\\D ^%JOURNAL

> Enable or Disable journaling of a set of globals.

> Do you want to Enable or Disable journaling? (E or D) E=\>

> All Globals? No =\> No

> Global ^DGBT

> 1 item selected from

> 194 available globals

> Global ^

> Global ^DGBT Done.

> ^^w:\vaa\\

> ^^w:\vaa\\D ^%CD

> Namespace: VAH

> You're in namespace VAH

> Default directory is y:\rou\\

> VAH\>