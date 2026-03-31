---
title: CMOP Version 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > The Consolidated Mail Outpatient Pharmacy (CMOP) software package establishes an interface for the electronic transfer of information between Veterans Affairs Medical Centers and the Consolidated Mail Outpatient Pharmacy host system for an integrated and highly automated outpatient prescription di
audience: 
keywords: 
  - cmop
  - table
  - contents
  - install
  - setup
  - installation
  - mail
  - device
  - host
  - server
page_count: 0
word_count: 4052
section_count: 34
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/cmop_2_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/cmop_2_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

![](cmop-version-2-installation-guide/001.png)

CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP)INSTALLATION GUIDE

April 1997

V*IST*A Software Development

Clinical Ancillary Product Line

BLANK FOR 2-SIDED COPYING

Table of ContentsCHAPTER ONE: REMOTE MEDICAL CENTER

Introduction

Pre-Installation

Routine Mapping Considerations for Install (ALPHA, DSM, VMS systems only)

Mail Group Setup

MailMan Server Option Setup

Kernel Site Parameter Setup

Resource Device Setup for Remote Medical Centers

Rx Consult List

Installation

Example of Install

Post-Installation

Journaling Globals

Security Keys Used by CMOP Remote Medical Centers

Resource Requirements

A. Hardware Requirements
B. Routines
C. Disk Storage
D. Files
E. Remote Medical Center Files

CHAPTER TWO: CMOP HOST FACILITY

Introduction

CMOP Host Facility Install for Printer

Barcodes

Pre-Installation

Pharmacists Releasing CMOP Prescriptions

Mail Group Setup

MailMan Server Option Setup

Kernel Site Parameter Setup

Resource Device Setup for Host Facility

Rx Consult List

Device Setup for Host CMOP Facility

Installation

Example of Install

Post-Installation

Journaling Globals

Security Keys Used by CMOP Host Facilities

Background Jobs

Resource Requirements

A. Hardware Requirements
B. Routines
C. Disk Storage
D. Files
E. Host Facility

# CHAPTER ONE: REMOTE MEDICAL CENTER


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [CHAPTER ONE: REMOTE MEDICAL CENTER](#chapter-one-remote-medical-center)
  - [Introduction](#introduction)
- [Pre-Installation](#pre-installation)
  - [Routine Mapping Considerations for Install (ALPHA, DSM, VMS systems only)](#routine-mapping-considerations-for-install-alpha-dsm-vms-systems-only)
  - [Mail Group Setup](#mail-group-setup)
  - [MailMan Server Option Setup](#mailman-server-option-setup)
  - [Kernel Site Parameter Setup](#kernel-site-parameter-setup)
  - [Resource Device Setup for Remote Medical Centers](#resource-device-setup-for-remote-medical-centers)
  - [Rx Consult List](#rx-consult-list)
- [Installation](#installation)
  - [Example of Install](#example-of-install)
- [Post-Installation](#post-installation)
  - [Journaling Globals](#journaling-globals)
  - [Security Keys Used by CMOP Remote Medical Centers](#security-keys-used-by-cmop-remote-medical-centers)
- [Resource Requirements](#resource-requirements)
  - [A. Hardware Requirements](#a-hardware-requirements)
  - [B. Routines](#b-routines)
  - [C. Disk Storage](#c-disk-storage)
  - [D. Files](#d-files)
  - [E. Remote Medical Center Files](#e-remote-medical-center-files)
- [CHAPTER TWO: CMOP HOST FACILITY](#chapter-two-cmop-host-facility)
  - [Introduction](#introduction-1)
- [CMOP Host Facility Install for Printer](#cmop-host-facility-install-for-printer)
  - [Barcodes](#barcodes)
- [Pre-Installation](#pre-installation-1)
  - [Pharmacists Releasing CMOP Prescriptions](#pharmacists-releasing-cmop-prescriptions)
  - [Mail Group Setup](#mail-group-setup-1)
  - [MailMan Server Option Setup](#mailman-server-option-setup-1)
  - [Kernel Site Parameter Setup](#kernel-site-parameter-setup-1)
  - [Resource Device Setup for Host Facility](#resource-device-setup-for-host-facility)
  - [Rx Consult List](#rx-consult-list-1)
  - [Device Setup for Host CMOP Facility](#device-setup-for-host-cmop-facility)
- [Installation](#installation-1)
  - [Example of Install](#example-of-install-1)
- [Post-Installation](#post-installation-1)
  - [Journaling Globals](#journaling-globals-1)
  - [Security Keys Used by CMOP Host Facilities](#security-keys-used-by-cmop-host-facilities)
  - [Background Jobs](#background-jobs)
- [Resource Requirements](#resource-requirements-1)
  - [A. Hardware Requirements](#a-hardware-requirements-1)
  - [B. Routines](#b-routines-1)
  - [C. Disk Storage](#c-disk-storage-1)
  - [D. Files](#d-files-1)
  - [E. Host Facility](#e-host-facility)
Remote Medical Center

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Consolidated Mail Outpatient Pharmacy (CMOP) software package establishes an interface for the electronic transfer of information between Veterans Affairs Medical Centers and the Consolidated Mail Outpatient Pharmacy host system for an integrated and highly automated outpatient prescription dispensing system.

> This installation guide is divided into two sections. The first section should be used by the remote medical centers for the installation of the Consolidated Mail Outpatient Pharmacy (CMOP) software. The second section is for the CMOP host facility.

> This version of the CMOP software is designed to selectively install files required for CMOP operations. This means that the host CMOP facility and the remote medical centers will have some differences in the files, routines, and options installed. It is recommended that the package first be loaded into your test account and Outpatient Pharmacy functionality tested by the users.

> However, it is not recommended that you test the prescription data transmission functionality. Doing so may cause test data to be transmitted to the HOST facility for dispensing. Once you feel comfortable with the package, the routines should be installed in the production account.

> \*\*IMPORTANT\*\*

> Outpatient Pharmacy V. 6.0 must be fully patched including recently released patch PSO\*6\*158, Seq. \#156.

> CMOP Version 1.0 (if loaded at your site), must be fully patched through PSX\*1\*11.

> For all remote medical centers installing this software, all pharmacy users should be off the system while installing the package. DUZ must be defined and valid, and DUZ(0) must be equal to “@” before installing the software. Prior to installation, all pre-installation tasks should be completed.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routine Mapping Considerations for Install (ALPHA, DSM, VMS systems only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CMOP exports fields in the Outpatient Pharmacy (OP) PRESCRIPTION file (#52) containing compiled cross references. These compiled routines in the Outpatient Pharmacy namespace (PSO) will be regenerated on installation. Therefore, prior to install, any mapped OP routines (PSO\*) must be unmapped. Once install is completed, these map sets must be rebuilt to restore routine mapping for Outpatient Pharmacy.

## Mail Group Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A public mail group must be set up with the name, CMOP MANAGERS. The mail group must have at least one active user as a member for the CMOP software to operate.

## MailMan Server Option Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This software is designed to transmit data via MailMan between the remote medical centers and the host facility. MailMan servers are used to accomplish this data transmission.

> For a server to function it must be associated with an entry in the BULLETIN file (#3.6). The selected bulletin entry must point to a mail group with at least one active user.

> The installation process will set up the OPTION (#19) and BULLETIN file (#3.6) entries as shown in the example below.

> Successful operation of the CMOP software is highly dependent on MailMan processing of the communications between the software and the user. The developer recommends that the medical centers and CMOP host facilities use the Sliding Window Protocol (SWP) for the best results.

The site must enter CMOP Managers in the MAIL GROUP field of the PSX CMOP entry in the BULLETIN file (#3.6).

> Mail messages are used extensively to relate the status of jobs, deliver reports, and advise users of data or transmission problems. The transmission mechanism for prescription data is the MailMan server option S.PSXX CMOP SERVER. MailMan delivers data to this option which queues numerous background jobs to handle processing and releasing of prescriptions. Information Resources Management (IRM) should note that problems with MailMan may directly impact on the performance of the CMOP software.

Example

VA FileMan 21.0

Select OPTION: <u>I</u>NQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: OPTION // <u>\<RET\></u> (5464 entries)

Select OPTION NAME: <u>PSXX CMOP SERVER</u> Consolidated Mail Outpatient Pharmacy Server

ANOTHER ONE: <u>\<RET\></u>

STANDARD CAPTIONED OUTPUT? YES// <u>\<RET\></u> (YES)

DISPLAY COMPUTED FIELDS? NO// <u>\<RET\></u> (NO)

DISPLAY AUDIT TRAIL? NO// <u>\<RET\></u> (NO)

NAME: PSXX CMOP SERVER

MENU TEXT: Consolidated Mail Outpatient Pharmacy Server

TYPE: server CREATOR: POSTMASTER

LOCK: PSXCMOPMGR PACKAGE: CMOP

DESCRIPTION: This server acts as the receiver for data transmissions and

other communications for the Consolidated Mail Outpatient Pharmacy system.

ROUTINE: PSXSERV SERVER BULLETIN: PSX CMOP

SERVER ACTION: RUN IMMEDIATELY SERVER MAIL GROUP: CMOP MANAGERS

SUPRESS BULLETIN: YES, SUPRESS IT

UPPERCASE MENU TEXT: CONSOLIDATED MAIL OUTPATIENT P

Select OPTION NAME: <u>\<RET\></u>

VA FileMan Version 21.0

Select OPTION: <u>I</u>nquire to File Entries

OUTPUT FROM WHAT FILE: PACKAGE// <u>BULLETIN</u> (90 entries)

Select BULLETIN NAME: <u>PSX</u> CMOP

ANOTHER ONE: <u>\<RET\></u>

STANDARD CAPTIONED OUTPUT? YES// <u>\<RET\></u> (YES)

DISPLAY COMPUTED FIELDS? NO// <u>\<RET\></u> (NO)

NAME: PSX CMOP SUBJECT: CMOP BULLETIN

MESSAGE: ----CMOP message----

MAIL GROUP: CMOP MANAGERS

DESCRIPTION: This bulletin is required by the Consolidated Mail Outpatient

Pharmacy system.

Select BULLETIN NAME: <u>\<RET\></u>

The site must enter CMOP Managers in the MAIL GROUP field of the PSX CMOP entry in the BULLETIN file (#3.6).

## Kernel Site Parameter Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MailMan patch XM\*7.1\*36 should be installed. When the patch is in place, set the field NETWORK - MAX LINES @ SEND TO to null as in the following example. This will allow larger CMOP transmissions to build without bumping into the preset Kernel site parameter limitations.

Example:

MSM\><u>D ^XUP</u>

Setting up programmer environment

terminal type set to : C-VT100

Select OPTION NAME: <u>XMKSP</u>

Kernel Site Parameters for MailMan

Select KERNEL SITE PARAMETERS DOMAIN NAME: *(Enter Your Site’s Domain Name)*

TIME ZONE: CST// <u>^NETWORK - MAX LINES @ SEND TO</u>

NETWORK - MAX LINES @ SEND TO: 15000// <u>@</u>

SURE YOU WANT TO DELETE? <u>Y</u> (Yes)

NETWORK - MAX LINES RECEIVED: 15000// <u>^</u>

Select KERNEL SITE PARAMETERS DOMAIN NAME: <u>\<RET\></u>

## Resource Device Setup for Remote Medical Centers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PSX resource device is set up to control the data transmissions to the CMOP host facility. See Resources in the Kernel Systems Manual for instructions on how to set up the PSX resource device as shown below. If this device is not set up correctly, CMOP data will not be transmitted properly.

> From the System Manager Menu Option, Select Device. From Device Management select, Edit Devices by Specific Types. From there, select the *Resource Device Edit* option to set up the resource device entry.

> Note: The device must be named PSX and set up as follows:

NAME: PSX \$I: PSX

LOCATION OF TERMINAL: NA RESOURCE SLOTS: 1

TYPE: RESOURCES

> \*\*\*WARNING\*\*\*

> You must review the entries for the RX CONSULT file (#54) which are standardized for use with the Consolidated Mail Outpatient Pharmacy system. These entries are listed on the following page. If these entries (1-20) do not match entries 1-20 of your RX CONSULT file (#54), the installation of the CMOP software will be aborted and no updating will take place.

> If your RX CONSULT file (#54) does not match, you must coordinate any necessary changes with the Outpatient Pharmacy staff to ensure all pointers, etc., to this file are resolved. Failure to validate data in this file and the respective entries in DRUG file (#50) which point to this file may cause errors on Outpatient Pharmacy (OP) prescription labels.

## Rx Consult List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RX CONSULT LIST MAY 31,1994 14:53 PAGE 1

NUMBER NAME TEXT

------------------------------------------------------------------------------

1 DROWSINESS -MAY CAUSE DROWSINESS-

Alcohol may intensify this effect.

USE CARE when driving or

when operating dangerous machinery.

2 FINISH IMPORTANT: Finish all this medication

unless otherwise directed by prescriber.

3 EMPTY STOMACH Take medication on an EMPTY STOMACH

1 hour before or 2-3 hours after a

meal unless otherwise directed by

your doctor.

4 NO DAIRY PRODUCTS Do not take antacids or iron

preparations or eat dairy products

within 1 hour of taking this medication.

5 WATER Take with plenty of WATER.

6 DISCOLORATION May cause discolored urine or feces.

7 DIURETIC K It may be advisable to drink a full

glass of orange juice or eat a banana

daily while on this medication.

8 NO ALCOHOL DO NOT DRINK ALCOHOLIC BEVERAGES

when taking this medication.

9 ADVICE DO NOT TAKE

non-prescription drugs

without medical advice.

10 WITH FOOD TAKE WITH FOOD OR MILK.

11 SUNLIGHT Avoid prolonged exposure to SUNLIGHT

and finish all this medication

unless otherwise directed by prescriber.

12 SHAKE WELL SHAKE WELL

13 EXTERNAL For external use ONLY.

14 STRENGTH NOTE DOSAGE STRENGTH

15 REFRIGERATE REFRIGERATE -DO NOT FREEZE

16 DUPLICATE This prescription CANNOT be

refilled without a written

duplicate from your physician.

17 EXPIRATION DATE Do not use after specified date.

18 NO REFILL THIS PRESCRIPTION CANNOT BE REFILLED.

19 SAME DRUG This is the same medication you

have been getting. Color, size

or shape may appear different.

20 NO TRANSFER CAUTION: Federal law prohibits the

transfer of this drug to any person

other than the patient for whom it

was prescribed.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Contact you local Customer Service for the CMOP software.

> The CMOP software can be loaded into your test or production accounts using the Kernel Installation Distribution System (KIDS) options as described in the installation example.

> This version (2.0) of Consolidated Mail Outpatient Pharmacy requires, at least, the following VA software applications. This software is not included in CMOP and must be installed (including all released patches) prior to the installation of the CMOP V. 2.0 software to ensure complete functionality.

> <u>Remote Medical Center</u> <u>Minimum Version Required</u>

> Kernel 8.0

> MailMan 7.1

> VA FileMan 21.0

> National Drug File (NDF) 3.16

> Outpatient Pharmacy (OP) 6.0 *(must have patch number PSO\*6\*158, Seq. \#156)*

> The user must receive the “Install Completed” notification before using the package.

> Version 2.0 install was created using the Kernel (8.0) Installation and Distribution System (KIDS). The KIDS installation will selectively install all options used by the CMOP software according to the type site, CMOP Host or remote medical center. The result is that the host CMOP will retain only the host functionality and the remote medical centers will retain only the remote functionality.

> MSM sites should install the software on the print server. On completion, the PSX\* routines must be moved to all compute servers.

## Example of Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site maps Outpatient Pharmacy (OP) routines, turn off mapping. Once the CMOP software is installed, you can re-map OP routines.

Select OPTION NAME: <u>EVE</u> Systems Manager Menu

Select Systems Manager Menu Option: <u>P</u>rogrammer Options

Select Programmer Options Option: <u>K</u>ernel Installation & Distribution

System

Select Kernel Installation & Distribution System Option: <u>I</u>nstallation

Select Installation Option: <u>L</u>OAD a Distribution

Enter a Host File: CMOP_2.KID

KIDS Distribution saved on Feb 21, 1997@10:52:35

Comment: CMOP 2.0

This Distribution contains Transport Globals for the following Package(s):

CMOP 2.0

OK to continue? NO// <u>Y</u>ES

Want to Continue with Load? YES// <u>\<RET\></u>

Loading Distribution...

Want to RUN the Environment Check Routine? YES// <u>\<RET\></u>

CMOP 2.0

Will first run the Environment Check Routine, PSXRENV

Consolidated Mail Outpatient Pharmacy Install for Remote Medical Center.

Validating required RX CONSULT FILE entries......

CMOPH 2.0

Will first run the Environment Check Routine, PSXHENV

CMOPH 2.0 Build will not be installed, Transport Global deleted!

Use INSTALL NAME: CMOP 2.0 to install this Distribution.

Select Installation Option: <u>VE</u>rify Checksums in Transport Global

Select INSTALL NAME: CMOP 2.0 Loaded from Distribution

2/21/97@11:02:42

=\> CMOP 2.0 ;Created on Feb 21, 1997@10:52:35

DEVICE: *\[Select Device\]*

PACKAGE: CMOP 2.0 Feb 21, 1997 11:04 am PAGE 1

--------------------------------------------------------------------------

111 Routine checked, 0 failed.

Select Installation Option: <u>IN</u>stall Package(s)

Select INSTALL NAME: CMOP 2.0 Loaded from Distribution

2/21/97@11:02:42

=\> CMOP 2.0 ;Created on Feb 21, 1997@10:52:35

This Distribution was loaded on Feb 21, 1997@11:02:42 with header of

CMOP 2.0 ;Created on Feb 21, 1997@10:52:35

It consisted of the following Install(s):

CMOP 2.0

CMOP 2.0

Will first run the Environment Check Routine, PSXRENV

Consolidated Mail Outpatient Pharmacy Install for Remote Medical Center.

*\[Medical centers that do not have a previous version of the CMOP software installed will see the following. Please enter the first letter of the CMOP facility you will be using.\] \[Sites that already have CMOP software installed will not see this part of the install.\]*

This install of the Consolidated Mail Outpatient Pharmacy

software at your medical center requires that you select the CMOP Host

Facility which will be receiving you Outpatient Pharmacy prescription

data.

Select one of the following:

B BEDFORD

D DALLAS

L LEAVENWORTH

W WEST LA

M MURFREESBORO

H HINES

Select the CMOP to RECEIVE YOUR DATA : <u>H</u>INES (Enter the first letter of

correct CMOP facility.)

You have chosen HINES CMOP to receive your transmissions.

*\[The following is common to all sites except for the “Note” following Files 550-550.2. The “Note” will only be present if these files already exist on the system.\]*

Validating required RX CONSULT FILE entries......

Install Questions for CMOP 2.0

50 DRUG (Partial Definition)

> **NOTE:** You already have the 'DRUG' File.

52 PRESCRIPTION (Partial Definition)

> **NOTE:** You already have the 'PRESCRIPTION' File.

52.5 RX SUSPENSE (Partial Definition)

> **NOTE:** You already have the 'RX SUSPENSE' File.

54 RX CONSULT (including data)

> **NOTE:** You already have the 'RX CONSULT' File.

I will MERGE your data with mine.

550 CMOP SYSTEM

> **NOTE:** You already have the 'CMOP SYSTEM' File.

550.1 CMOP RX QUEUE

> **NOTE:** You already have the 'CMOP RX QUEUE' File.

550.2 CMOP TRANSMISSION

> **NOTE:** You already have the 'CMOP TRANSMISSION' File.

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>N</u>O

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: *\[Select Print Device\]*

Install Started for CMOP 2.0 :

Feb 21, 1997@11:05:04

Installing Routines:

Feb 21, 1997@11:05:42

Installing Data Dictionaries:

Feb 21, 1997@11:06:15

Installing Data:

Feb 21, 1997@11:06:17

Installing PACKAGE COMPONENTS:

Installing BULLETIN

Installing SECURITY KEY

Installing INPUT TEMPLATE

Installing OPTION

Feb 21, 1997@12:14:23

Running Post-Initialization Routine: ^PSXPOST

Initialization complete!!

Updating Routine file...

The following Routines were created during this install:

CMOP 2.0

-------------------------------------------------------------------------

PSOXZA

PSOXZA1

PSOXZA2

PSOXZA3

PSOXZA4

PSOXZA5

PSOXZA6

PSOXZA7

PSOXZA8

Updating KIDS files...

CMOP 2.0 Installed.

Feb 21, 1997@12:14:36

Install Message sent

-------------------------------------------------------------------------

+---------------------------------------------------------------+

100% \| 25 50 75 \|

Complete +---------------------------------------------------------------+

Install Completed

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To ensure the integrity of all prescription data, the Consolidated Mail Outpatient Pharmacy software should ALWAYS function at Veterans Affairs Medical Centers (VAMCs) with the Outpatient Pharmacy VERIFICATION turned ON.

## Journaling Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Journaling of the PSX global is recommended for all Remote medical centers facilities.

## Security Keys Used by CMOP Remote Medical Centers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The security keys listed below control the access necessary to operate the CMOP software. These keys should be assigned by the Chief of Pharmacy or a designee.

> PSXCMOPMGR This security key locks the *CMOP Site Manager Menu.*

> PSX XMIT Only holders of this security key and the PSXCMOPMGR key may transmit data to the CMOP using suspense options. This key also locks the *Transmission Menu* on the *CMOP Site Manager Menu*.

> PSXRTRAN This key allows the holder to access the *Re-transmit CMOP Data* option which re-sends previously transmitted data to the CMOP.

> PSXAUTOX This security key allows users access to the *SetupAuto-transmission* option. This key in combination with the PSXCMOPMGR and PSX XMIT are required to set up the auto-transmission schedule.

> PSNMGR This security key is used to lock the *CMOP Mark/Unmark (Single drug)* and the *Loop CMOP Match to Local Drug File* options which use the NATIONAL DRUG file (#50.6) to mark and match items for CMOP dispense. This key is not exported with CMOP.

> PSXMAIL This security key enables a site manager to specify who receives the various mail messages and alerts generated by the CMOP process. The user(s) assigned this key must be active in the system. When the mail messages are generated, the software will look for users with the PSXMAIL key who are active. If there are no users with this key or there are users with this key who are inactive, then the software will send the messages to all holders with the PSXCMOPMGR key.

> PSXRESUB This security key is used to lock the *Resubmit CMOP Rx* option and enables a designated user to resubmit Rx’s to the CMOP.

# Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A. Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no additional hardware requirements for this package.

## B. Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Routine Size</u>

> PSXACK 3698

> PSXACT 4735

> PSXARC 4337

> PSXARC1 4947

> PSXARC2 2625

> PSXARPT 3239

> PSXAUTO 5208

> PSXBKD 4881

> PSXBKG 3930

> PSXBLD 4542

> PSXBLD1 3981

> PSXCH 1270

> PSXCMOP 3514

> PSXCMOP0 2157

> PSXCMOP1 3469

> PSXCOPAY 1672

> PSXCOSTU 3569

> PSXCSCMN 3683

> PSXCSDA 3436

> PSXCSDC 2288

> PSXCSDC1 3265

> PSXCSDC2 1697

> PSXCSHI 3315

> PSXCSHI1 1444

> PSXCSLG1 747

> PSXCSLOG 3696

> PSXCSMN1 3312

> PSXCSMON 3074

> PSXCSSUM 3435

> PSXCST 3205

> PSXCST1 1663

> PSXCSTPG 3380

> PSXCSUTL 3362

> PSXDENT 419

> PSXDQUE 2244

> PSXDRPT 3133

> PSXEDIT 4292

> PSXEDRG 1739

> PSXEDUTL 2754

> PSXERR 4613

> PSXERR1 1182

> PSXHENV 1795

> PSXHSYS 8523

> PSXJOB 1327

> PSXLBL 3315

> PSXLBL1 4508

> PSXLBL2 3346

> PSXLBLNR 2408

> PSXLBLPT 670

> PSXLBLT 3183

> PSXLBLU 4867

> PSXLIST 4008

> PSXLKUP 2381

> PSXLTST 653

> PSXMARK 4768

> PSXMISC 3230

> PSXMISC1 4137

> PSXMSGS 4416

> PSXMST 2697

> PSXNEW 3881

> PSXNOCMP 2096

> PSXNOTE 5235

> PSXOCMOP 2232

> PSXOPUTL 3358

> PSXPLOG 851

> PSXPOST 2494

> PSXPURG 4642

> PSXPURG1 1188

> PSXQRY 6744

> PSXQUE 4147

> PSXRACT 3202

> PSXRCVRY 3970

> PSXRECV 4332

> PSXRECV1 4449

> PSXREF 1820

> PSXREJ 3987

> PSXREL 2229

> PSXRENV 3589

> PSXRESUB 2782

> PSXRHLP 3486

> PSXRPPL 5114

> PSXRPPL1 4212

> PSXRPT 6734

> PSXRSTAT 4941

> PSXRSUS 4600

> PSXRSYU 3759

> PSXRTN 5127

> PSXRTN1 5040

> PSXRTR 2648

> PSXRTRAN 7067

> PSXRXQU 3315

> PSXRXU 3062

> PSXSERV 1850

> PSXSITE 4573

> PSXSMRY 4840

> PSXSND 3733

> PSXSTAT 5094

> PSXSTP 547

> PSXSTRT 3438

> PSXSUDCN 2987

> PSXSYS 3388

> PSXTNRPT 4667

> PSXUNHLD 2434

> PSXUNREL 2829

> PSXUTL 3156

> PSXVCK 3831

> PSXVCK1 4729

> PSXVEND 5905

> PSXVIEW 2923

> PSXVND 5420

> PSXVPN 2625

> Total routines 111 Total size 382686

## C. Disk Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This version of Consolidated Mail Outpatient Pharmacy Version 2.0 contains 111 routines. These routines require approximately 382686 disk space.

> Response Time Monitor hooks have been placed in the following routine:

> <u>Routine</u> <u>Purpose</u>

> PSXRSUS Data Transmission

## D. Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This package requires 19 files in addition to those of the Kernel and other files to which it points. Information about all files, including these can be obtained by using the VA FileMan to generate a list of file attributes.

> Please refer to the documentation for Outpatient Pharmacy V. 6.0 and National Drug File V. 3.16 for detailed information on resource requirements for these software packages.

## E. Remote Medical Center Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>File Numbers</u>; <u>File Names</u>

> 550 CMOP SYSTEM

> 550.1 CMOP RX QUEUE

> 550.2 CMOP TRANSMISSION

> 50 DRUG

> 50.6 NATIONAL DRUG

> 51.5 ORDER UNIT

> 52 PRESCRIPTION

> 52.5 RX SUSPENSE

> 54 RX CONSULT

# CHAPTER TWO: CMOP HOST FACILITY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CMOP Host Facility

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*Please Note\*\*\*

> National Drug File Version 3.16 must be installed before installing the Consolidated Mail Outpatient Pharmacy (CMOP) software.

> The Consolidated Mail Outpatient Pharmacy (CMOP) software package establishes an interface for the electronic transfer of information between Veterans Affairs Medical Centers (VAMCs) and the Consolidated Mail Outpatient Pharmacy (CMOP) host system for an integrated and highly automated outpatient prescription dispensing system.

> This installation guide is divided into two sections. The first section should be used by the remote medical centers for the installation of Consolidated Mail Outpatient Pharmacy software. The second section is for the host CMOP facility.

> This version of the CMOP software is designed to selectively install files required for CMOP operations. This means that the host CMOP facility and the remote medical centers will have some differences in the files, routines, and options installed. It is recommended that the package first be loaded into your test account and tested by the users. Once you feel comfortable with the package, the software should be installed into your production account.

> For all host facilities installing this software, all users should be off the system while installing the software. DUZ must be defined and valid, and DUZ(0) must be equal to “@” before installation. Prior to installing the software all pre-installation tasks should be completed.

> All CMOP host facilities are MSM sites. The diskette(s) containing the CMOP routines PSX\* may be loaded into your test or production account using the Kernel Installation & Distribution System options as described in the section Example of Install.

> This version (2.0) of Consolidated Mail Outpatient Pharmacy requires, at least, the following VA software applications. This software is not included in CMOP and must be installed (including all released patches) prior to the installation of the CMOP V. 2.0 software to ensure complete functionality.

> <u>Host Facility</u> <u>Minimum Version Required</u>

> Kernel 8.0

> MailMan 7.1

> VA FileMan 21.0

> National Drug File (NDF) 3.16

> Version 2.0 install was created using the Kernel (8.0) Installation and Distribution System (KIDS). The KIDS installation will selectively install all options used by the CMOP software according to the type site, CMOP Host or remote medical center. The result is that the host CMOP will retain only the host functionality and the remote medical centers will retain only the remote functionality.

> MSM sites should install the software on the print server. Once the install is finished on the print server, move all PSX\* routines to all compute servers.

# CMOP Host Facility Install for Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*IMPORTANT\*\*

> Each CMOP host facility should have a label printer(s) set up with new label stock forms for printing CMOP labels should the automated dispensing equipment fail. This will allow the CMOP to print labels for filling prescriptions manually and should only be used in an emergency situation.

> The following barcode information may be helpful in setting up barcode labels.

## Barcodes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This version of Consolidated Mail Outpatient Pharmacy includes the ability to print barcodes on the refill request form and on the multi-RX request form. The Kernel group responsible for the TERMINAL TYPE file (#3.2) has defined two new fields. To use the barcode capability, you should define new terminal types, for example, P-DS220 BARCODER and P-MT290 BARCODER. All parameters for these new types should be the same as those for the corresponding terminal type without the barcode capability. The two new fields (BAR CODE ON and BAR CODE OFF) should be entered.

<u>For the DATASOUTH 220</u>

BAR CODE ON =

\*27,"\$70s",\*97,"H",\$S('\$D(X):"04",X="M":"04",X="S":"02",X="L":"10",1:"04"),\*94,

"BDB"

> **NOTE:** The letter following the \$70 is a lower-case s.

BAR CODE OFF =\*94,"G",\*27,"\$70c"

> **NOTE:** The letter following the \$70 is a lower-case c.

<u>For the DATASOUTH XL300 DD</u>

BAR CODE ON =

\*27,"\[lw",\*27,\$s70",\*94,"H",\$S('\$D(X):"04",X="M":"04",X="S":"02",X="L":"10",1:

"04"),\*94,"BDB"

BAR CODE OFF=\*94,"G",\*27,"\$c70",\*27,"\[2w",!

<u>  
For the MT-290</u>

BAR CODE ON =

\*26,"F0",\$S('\$D(X):2,X="M":2,X="S":1,X="L":6,1:2),";000",\*25,\*20,"\*"

BAR CODE OFF = "\*",\*20,!,?\$S(\$D(X1):X1,1:0),\$S(\$D(X2):X2,1:"")

<u>For the OTC-560</u>

BAR CODE ON =\*27,"\[;",\$S('\$D(X):3,X="M":6,X="L":12,1:3),"}",\*27,"\[3t"

BAR CODE OFF = \*27,"\[0t"

<u>For the GENICOM 4440</u>

BAR CODE ON =\*27,"\[;",\$S('\$D(X):3,X="M":6,X="L":12,1:3),"}",\*27,"\[3t"

BAR CODE OFF = \*27,"\[0t"

> In the DEVICE file (#3.5), each pharmacy label printer should have the appropriate entries in both the SUBTYPE and DEFAULT SUBTYPE fields.

> On the printers, the form length must be set to 24 lines. This is feature 2 on the DS-220 and part of the main menu for the MT-290. Additionally, feature 46 on the DS-220, ESCAPE SEQUENCE DISABLE, must be set to 0 and the MT-290 must have the required barcode cartridge installed.

> Barcodes can only be printed on the four inch labels. If you are still using the older three inch labels, you can not print barcodes.

> While this section describes printing of barcodes on only the OTC-560, GENICOM-4440, DS-220, and MT-290 printers, the function is device independent and can be used with any printer which can print barcodes and which can be set for a form length of either four inches or 24 lines. The following information is intended as a guide for setting up the barcode fields for other printers.

<u>For the DATASOUTH-200</u>

BAR CODE ON=

\*27,"\[1w",\*27,"\$70s",\*94,"H",\$S('\$D(X):"04",X="M":"04",X="S":"02",X="L":"

10",1:"04"),\*94,"BDB"

BAR CODE OFF=\*94,"G",\*27,"\$70c",\*27,"\[2w",!

<u>  
For the MT-661</u>

BAR CODE ON=

\*27,"\[\<4h",\*94,\$S(\$X\<60:"T450",1:"T850"),\*94,"W9;5;1",\*94,"B1;35;1;3",\*13

BAR CODE OFF=\*13,\*10,\*27,"\[\<4l",\*27,"\[5w"

> **NOTE:** The character after the \[4 in the BAR CODE OFF above is a lower case L

<u>For the DATASOUTH A600</u>

BAR CODE OFF=\$C(94),"\*",\$C(94),"PN"

BAR CODE ON=\$C(94),"PY",\$C(94),"M",\$C(94),"H03",\$C(94),\$S(\$X\<80:"T0450"

,1:"T0850"),\$C(94),"BYB"

<u>For the DATASOUTH XL400</u>

BAR CODE OFF=\*94,"G",\*27,"\$70c"

BAR CODE ON=\*27,"\$70s",\*94,"H",\$S('\$D(X):"04",X="M":"04",X="S":"02",X="L":"1

0",1:"04"),\*94,"BDB"

<u>For the DATASOUTH PERFORMAX AS-600</u>

BAR CODE OFF=\$C(94),"\*",\$C(94),"PN"

BAR CODE ON=\$C(94),"PY",\$C(94),"M",\$C(94),"H03",\$C(94),\$S(\$X\<80:"T0450"

> Each of the two fields is the argument of a MUMPS Write command.

> Three parameters are used.

> X is the barcode height. Values can be S, M, or L. If X is undefined or not equal to one of these, the default value of S is used. S is 2/10 inch for the DS-220 and 1/6 inch for the MT-290. M is 4/10 inch for the DS-200 and 1/3 inch for the MT-290. L is one inch for both.

> X1 is the value of \$X at the left edge of the barcode. If X1 is undefined, the default value of 0 is used.

> X2 is the data to be barcoded. Remember that the code 39 character set which is being used by the VA is a limited subset of the ASCII character set containing only the numbers, upper case letters and eight punctuation characters. In most cases, any other characters are not printed. For example, the barcode for the string “123abc” will be the same as that for the string “123”.

> On most printers, printing a barcode is a graphics operation which causes the value of \$Y to be something other than the line count from the top of the page. Forms with barcodes on them must use a form feed to go to the top of the next form rather than a counted number of line feeds. This is the reason that printers being used to print barcodes on outpatient pharmacy labels must be set for a form length of 24 lines or four inches.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pharmacists Releasing CMOP Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. All users (pharmacists) who will be releasing prescriptions must be entered by IRM as users on the CMOP DHCP system through the *Add a NewUserto the System* option under the *User Management* option on the *Systems Manager* menu. Once the users are entered a VA FileMan list of the NUMBER and NAME fields from the NEW PERSON file (#200) should be printed. These internal entry numbers for the users should be entered into the vendor system as the IDs for the pharmacists. This will be the information passed back to DHCP to identify the person responsible for the prescription. If the number received by DHCP from the vendor is not a valid pharmacist, that is, the user does not hold the PSXRPH security key, release data will not be filed for the prescriptions.

> 2\. All pharmacists should be assigned the PSXRPH security key. Only pharmacists with this key will be allowed to be entered for manual release of prescriptions on the V*IST*A CMOP system. The manual release of prescriptions is necessary if V*IST*A labels are used for dispensing.

## Mail Group Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A public mail group must be set up with the name, CMOP MANAGERS. The mail group must have at lease one active user as a member for the CMOP software to operate.

## MailMan Server Option Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This software is designed to transmit data via MailMan between the remote medical centers and the host facility. MailMan servers are used to accomplish this data transmission.

> For a server to function it must be associated with an entry in the BULLETIN file (#3.6). The selected bulletin entry must point to a mail group with at least one active user.

> A mail group must be set up with the name, CMOP MANAGERS. The mail group must have at least one active user as a member for the CMOP software to operate. It is recommended that at a minimum the CMOP System Manager be a member of this mail group.

> The installation process will set up the OPTION (#19) and BULLETIN file (#3.6) entries as shown in the example below.

> Successful operation of the CMOP software is highly dependent on MailMan processing of the communications between the software and the user. The developer recommends that the medical centers and CMOP host facilities use the Sliding Window Protocol (SWP) for the best results.

The site must enter CMOP Managers in the MAIL GROUP field of the PSX CMOP entry in the BULLETIN file (#3.6).

> Mail messages are used extensively to relate the status of jobs, deliver reports, and advise users of data or transmission problems. The transmission mechanism for prescription data is the MailMan server option S.PSXX CMOP SERVER. MailMan delivers data to this option which queues numerous background jobs to handle processing and releasing of prescriptions. Information Resources Management (IRM) should note that problems with MailMan may directly impact on the performance of the CMOP software.

Example

VA FileMan 21.0

Select OPTION: <u>I</u>NQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: OPTION // <u>\<RET\></u> (5464 entries)

Select OPTION NAME: <u>PSXX CMOP SERVER</u> Consolidated Mail Outpatient Pharmacy Server

ANOTHER ONE: <u>\<RET\></u>

STANDARD CAPTIONED OUTPUT? YES// <u>\<RET\></u> (YES)

DISPLAY COMPUTED FIELDS? NO// <u>\<RET\></u> (NO)

DISPLAY AUDIT TRAIL? NO// <u>\<RET\></u> (NO)

NAME: PSXX CMOP SERVER

MENU TEXT: Consolidated Mail Outpatient Pharmacy Server

TYPE: server CREATOR: POSTMASTER

LOCK: PSXCMOPMGR PACKAGE: CMOP

DESCRIPTION: This server acts as the receiver for data transmissions and

other communications for the Consolidated Mail Outpatient Pharmacy system.

ROUTINE: PSXSERV SERVER BULLETIN: PSX CMOP

SERVER ACTION: RUN IMMEDIATELY SERVER MAIL GROUP: CMOP MANAGERS

SUPRESS BULLETIN: YES, SUPRESS IT

UPPERCASE MENU TEXT: CONSOLIDATED MAIL OUTPATIENT P

Select OPTION NAME: <u>\<RET\></u>

VA FileMan Version 21.0

Select OPTION: <u>I</u>nquire to File Entries

OUTPUT FROM WHAT FILE: PACKAGE// <u>BULLETIN</u> (90 entries)

Select BULLETIN NAME: <u>PSX</u> CMOP

ANOTHER ONE: <u>\<RET\></u>

STANDARD CAPTIONED OUTPUT? YES// <u>\<RET\></u> (YES)

DISPLAY COMPUTED FIELDS? NO// <u>\<RET\></u> (NO)

NAME: PSX CMOP SUBJECT: CMOP BULLETIN

MESSAGE: ----CMOP message----

MAIL GROUP: CMOP MANAGERS

DESCRIPTION: This bulletin required by the Consolidated Mail Outpatient

Pharmacy system.

Select BULLETIN NAME: <u>\<RET\></u>

The site must enter CMOP Managers in the MAIL GROUP field of the PSX CMOP entry in the BULLETIN file (#3.6).

## Kernel Site Parameter Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MailMan patch XM\*7.1\*36 should be installed. When patch is in place, set the fields NETWORK - MAX LINES @ SEND TO and NETWORK - MAX LINES RECEIVED to null as in the following example. This will allow larger CMOP transmissions to build without bumping into the preset Kernel site parameter limitations.

Example:

MSM\><u>D ^XUP</u>

Setting up programmer environment

terminal type set to : C-VT100

Select OPTION NAME: <u>XMKSP</u>

Kernel Site Parameters for MailMan

Select KERNEL SITE PARAMETERS DOMAIN NAME: *(Enter Your Site’s Domain Name)*

TIME ZONE: CST// <u>^NETWORK - MAX LINES @ SEND TO</u>

NETWORK - MAX LINES @ SEND TO: 15000// <u>@</u>

SURE YOU WANT TO DELETE? <u>Y</u> (Yes)

NETWORK - MAX LINES RECEIVED: 15000// <u>@</u>

SURE YOU WANT TO DELETE? <u>Y</u> (Yes)

Select KERNEL SITE PARAMETERS DOMAIN NAME: <u>\<RET\></u>

## Resource Device Setup for Host Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PSX resource device is set up to control the data transmissions to the CMOP host facility. See Resources in the Kernel Systems Manual for instructions on how to set up the PSX resource device as shown below. If this device is not set up correctly, CMOP data will not be transmitted.

> From the System Manager Menu Option, Select Device. From Device Management select, Edit Devices by Specific Types. From there, select the *Resource Device Edit* option to set up the resource device entry.

> Note: The device must be named PSX and set up as follows:

NAME: PSX \$I: PSX

LOCATION OF TERMINAL: NA RESOURCE SLOTS: 1

TYPE: RESOURCES

> \*\*\*WARNING\*\*\*

> You must review the entries for the RX CONSULT file (#54) which are standardized for use with the Consolidated Mail Outpatient Pharmacy system. These entries are listed on the following page. If these entries (1-20) do not match entries 1-20 of your RX CONSULT file (#54), the installation of the CMOP software will be aborted and no updating will take place.

> If your RX CONSULT file (#54) does not match, you must coordinate any necessary changes with the Outpatient Pharmacy staff to ensure all pointers, etc., to this file are resolved. Failure to validate data in this file and the respective entries in DRUG file (#50) which point to this file may cause errors on Outpatient Pharmacy prescription labels.

## Rx Consult List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RX CONSULT LIST MAY 31,1994 14:53 PAGE 1

NUMBER NAME TEXT

------------------------------------------------------------------------------

1 DROWSINESS -MAY CAUSE DROWSINESS-

Alcohol may intensify this effect.

USE CARE when driving or

when operating dangerous machinery.

2 FINISH IMPORTANT: Finish all this medication

unless otherwise directed by prescriber.

3 EMPTY STOMACH Take medication on an EMPTY STOMACH

1 hour before or 2-3 hours after a

meal unless otherwise directed by

your doctor.

4 NO DAIRY PRODUCTS Do not take antacids or iron

preparations or eat dairy products

within 1 hour of taking this medication.

5 WATER Take with plenty of WATER.

6 DISCOLORATION May cause discolored urine or feces.

7 DIURETIC K It may be advisable to drink a full

glass of orange juice or eat a banana

daily while on this medication.

8 NO ALCOHOL DO NOT DRINK ALCOHOLIC BEVERAGES

when taking this medication.

9 ADVICE DO NOT TAKE

non-prescription drugs

without medical advice.

10 WITH FOOD TAKE WITH FOOD OR MILK.

11 SUNLIGHT Avoid prolonged exposure to SUNLIGHT

and finish all this medication

unless otherwise directed by prescriber.

12 SHAKE WELL SHAKE WELL

13 EXTERNAL For external use ONLY.

14 STRENGTH NOTE DOSAGE STRENGTH

15 REFRIGERATE REFRIGERATE -DO NOT FREEZE

16 DUPLICATE This prescription CANNOT be

refilled without a written

duplicate from your physician.

17 EXPIRATION DATE Do not use after specified date.

18 NO REFILL THIS PRESCRIPTION CANNOT BE REFILLED.

19 SAME DRUG This is the same medication you

have been getting. Color, size

or shape may appear different.

20 NO TRANSFER CAUTION: Federal law prohibits the

transfer of this drug to any person

other than the patient for whom it

was prescribed.

## Device Setup for Host CMOP Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SETUP OF CMOP DEVICE USED FOR DATA TRANSMISSIONS TO VENDOR SYSTEM *\[The following file entry must be added to the DEVICE file (#3.5).\]*

NAME: CMOP \$I: 4

ASK PARAMETERS: NO PRIORITY AT RUN TIME: 1

VOLUME SET(CPU): PSA LOCATION OF TERMINAL: N/A

ASK HOST FILE: NO ASK HFS I/O OPERATION: NO

SUPPRESS FORM FEED AT CLOSE: YES MARGIN WIDTH: 255

FORM FEED: \# PAGE LENGTH: 66

BACK SPACE: \$C(8)

MNEMONIC: CMOP

SUBTYPE: P‑OTHER TYPE: OTHER

> The system manager should edit the AUTOEXEC.BAT file so that the mode command line reads as follows:

> either MODE COM1:96,8,N,1

> or MODE COM2:96,8,N,1

> depending on the COM port used by the CMOP device.

> In the manager account of the host CMOP PC system (MSM) the port definition of the CMOP device should be set up as follows:

<u>\>D ^%ZUCI</u>

UCI: MGR ..Switched to: MGR

<u>\>D ^SYSGEN</u>

MSM ‑ System Generation Utility

Select SYSGEN Option: <u>\<RET\></u>

1 ‑ Display Configuration Parameters

2 ‑ Create New Configuration

3 ‑ Edit Configuration Parameters

4 ‑ Rename Configuration

5 ‑ Delete Configuration

6 ‑ Set Default Startup Configuration

7 ‑ UCI Management

8 ‑ Hardware Identification

9 ‑ Buffer Pool Size

10 ‑ Database Definition

13 ‑ Mnemonic Namespaces

Select Option: <u>3</u> ‑ Edit Configuration Parameters

Select Configuration PSA: <u>\<RET\></u> PSA

Select SYSGEN Option:<u>\<RET\></u>

1 ‑ SYSGEN (step through full SYSGEN)

2 ‑ Backspace, Line Delete Character

3 ‑ Autostarts and Automounts

4 ‑ Maximum Partitions

5 ‑ Programmer Access Code

6 ‑ MSM Disk Usage

7 ‑ VIEW Command Restriction

8 ‑ Tied Terminal Table

9 ‑ Port (Terminal) Definition

10 ‑ Multi‑port I/O Card Definition

11 ‑ Automatic Partition Startup

12 ‑ Default Partition Size

13 ‑ Translation/Replication Table Maintenance

16 ‑ Tape Device Definition

17 ‑ Global Defaults

18 ‑ LOCK Table Size

19 ‑ Edit Configuration Comment

20 ‑ Mode Flags

21 ‑ Display Configuration Parameters

Select Option: <u>9</u> ‑ Port (Terminal) Definition

Terminal Configuration:

Port Port Port Tied Line Initial Initial

Number Type Addr Index Width Parms Status

‑‑‑‑‑‑ ‑‑‑‑ ‑‑‑‑‑ ‑‑‑‑‑ ‑‑‑‑‑ ‑‑‑‑‑‑ ‑‑‑‑‑‑‑

1 PC/DOS CON 80 Console /Echo/CRT

3 PC/DOS LPT1 132 Parallel /OutDev

4 PC/DOS COM1 255 9600,8B+1S /8bit/CRT/NoLog

Select Port Number: <u>4</u>

Port Types: <u>\<RET\></u>

1 ‑ PC CONSOLE

2 ‑ Serial Communication Ports (COM)

3 ‑ Parallel Printers (LPT)

4 ‑ ARNET Multiport Card

5 ‑ Quadport‑AT Card

6 ‑ AST 4 Port/XN Card

7 ‑ MCC Card

8 ‑ Console Window Devices

9 ‑ ARNET SmartPort card

10 ‑ Bios LPT device

11 ‑ LAT Port ‑ connection to a specific port and server

Select Option \<2\>: <u>\<RET\></u> 2 ‑ Serial Communication Ports (COM)

Port Address \<1\> <u>\<RET\></u> 1

Tied Terminal Index \<\>: <u>\<RET\></u>

Terminal Line Width \<255\>: <u>\<RET\></u> 255

Select Echo Option:

1 ‑ ON

2 ‑ OFF

Select Option \<ON\>: <u>OFF</u> OFF

Escape Processing Mode:

1 ‑ OFF

2 ‑ ON

Select Option \<OFF\>: <u>\<RET\></u> OFF

8‑bit Mode:

1 ‑ OFF

2 ‑ ON

Select Option \<ON\>: <u>\<RET\></u> ON

Pass All Mode:

1 ‑ OFF

2 ‑ ON

Select Option \<OFF\>: <u>\<RET\></u> OFF

Line Feed Suppression:

1 ‑ OFF

2 ‑ ON

Select Option \<OFF\>: <u>\<RET\></u> OFF

Modem Controlled:

1 ‑ NO

2 ‑ YES ‑ AUTO ANSWER (DTR ON)

3 ‑ YES ‑ NO AUTO ANSWER (DTR OFF)

Select Option \<2\>: <u>1</u> 1 ‑ NO

Upper‑Case Setup:

1 ‑ OFF

2 ‑ ON

Select Option \<OFF\>: <u>\<RET\></u> OFF

Select 'Output‑Only' Mode:

1 ‑ OFF (Input/Output Device)

2 ‑ ON (Output‑only device)

Select Option \<OFF\>: <u>\<RET\></u> OFF (Input/Output Device)

Login Allowed:

1 ‑ YES

2 ‑ NO

Select Option \<YES\>: <u>NO</u> NO

CRT Mode:

1 ‑ ON

2 ‑ OFF

Select Option \<ON\>: <u>\<RET\></u> ON

Select Initialization Option:

1 ‑ 7 Data Bits, No Parity, and 1 Stop Bit

2 ‑ 7 Data Bits, Even Parity, and 1 Stop Bit

3 ‑ 7 Data Bits, Odd Parity, and 1 Stop Bit

4 ‑ 7 Data Bits, No Parity, 2 Stop Bits

5 ‑ 7 Data Bits, Even Parity, and 2 Stop Bits

6 ‑ 7 Data Bits, Odd Parity, 2 Stop Bits

7 ‑ 8 Data Bits, No Parity, and 1 Stop Bit

8 ‑ 8 Data Bits, Even Parity, and 1 Stop Bit

9 ‑ 8 Data Bits, Odd Parity, and 1 Stop Bit

10 ‑ 8 Data Bits, No Parity, 2 Stop Bits

11 ‑ 8 Data Bits, Even Parity, and 2 Stop Bits

12 ‑ 8 Data Bits, Odd Parity, 2 Stop Bits

Select Option \<7\>: <u>\<RET\></u> 7 ‑ 8 Data Bits, No Parity, and 1 Stop Bit

Select Baud Rate: <u>\<RET\></u>

1 ‑ 50

2 ‑ 75

3 ‑ 110

4 ‑ 134.5

5 ‑ 150

6 ‑ 200

7 ‑ 300

8 ‑ 600

9 ‑ 1200

10 ‑ 1800

11 ‑ 2400

12 ‑ 4800

13 ‑ 9600

14 ‑ 19200

Select Option \<13\>: <u>\<RET\></u> 13 ‑ 9600

Flow Control:

1 ‑ ON

2 ‑ OFF

Select Port Number: <u>\<RET\></u>

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Example of Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION NAME: <u>EVE</u> Systems Manager Menu

Select Systems Manager Menu Option: <u>P</u>rogrammer Options

Select Programmer Options Option: <u>K</u>ernel Installation & Distribution

System

Select Kernel Installation & Distribution System Option: <u>IN</u>stallation

Select Installation Option: <u>LOAD</u> a Distribution

Enter a Host File: CMOP2\_.KID

KIDS Distribution saved on Feb 21, 1997@10:52:35

Comment: CMOP 2.0

This Distribution contains Transport Globals for the following Package(s):

CMOP 2.0

CMOPH 2.0

OK to continue? NO// <u>Y</u>ES

Want to Continue with Load? YES// <u>\<RET\></u>

Loading Distribution...

Want to RUN the Environment Check Routine? YES// <u>\<RET\></u>

CMOP 2.0

Will first run the Environment Check Routine, PSXRENV

CMOP 2.0 Build will not be installed, Transport Global deleted!

CMOPH 2.0

Will first run the Environment Check Routine, PSXHENV

Consolidated Mail Outpatient Pharmacy Install for Host Facility.

*\[The following is common to all sites except for the “Note” following Files 552-555. The “Note” will be present if these files already exist on the system.\]*

Use INSTALL NAME: CMOPH 2.0 to install this Distribution.

Select Installation Option: <u>VER</u>ify Checksums in Transport Global

Select INSTALL NAME: CMOPH 2.0 Loaded from Distribution

2/21/97@10:57:11

=\> CMOP 2.0 ;Created on Feb 21, 1997@10:52:35

DEVICE: *\[Select Device\]*

PACKAGE: CMOPH 2.0 Feb 21, 1997 10:58 am PAGE 1

--------------------------------------------------------------------------

110 Routine checked, 0 failed.

Select Installation Option: <u>IN</u>stall Package(s)

Select INSTALL NAME: CMOPH 2.0 Loaded from Distribution

2/21/97@10:57:11

=\> CMOP 2.0 ;Created on Feb 21, 1997@10:52:35

This Distribution was loaded on Feb 21, 1997@10:57:11 with header of

CMOP 2.0 ;Created on Feb 21, 1997@10:52:35

It consisted of the following Install(s):

CMOPH 2.0

CMOPH 2.0

Will first run the Environment Check Routine, PSXHENV

Consolidated Mail Outpatient Pharmacy Install for Host Facility.

Install Questions for CMOPH 2.0

50 DRUG (Partial Definition)

> **NOTE:** You already have the 'DRUG' File.

54 RX CONSULT (including data)

> **NOTE:** You already have the 'RX CONSULT' File.

I will MERGE your data with mine.

552 CMOP NATIONAL SITE

> **NOTE:** You already have the 'CMOP NATIONAL SITE' File.

552.1 CMOP REFERENCE

> **NOTE:** You already have the 'CMOP REFERENCE' File.

552.2 CMOP DATABASE

> **NOTE:** You already have the 'CMOP DATABASE' File.

552.3 CMOP RELEASE

> **NOTE:** You already have the 'CMOP RELEASE' File.

552.4 CMOP MASTER DATABASE

> **NOTE:** You already have the 'CMOP MASTER DATABASE' File.

552.5 CMOP COST STATS

> **NOTE:** You already have the 'CMOP COST STATS' File.

553 CMOP INTERFACE

> **NOTE:** You already have the 'CMOP INTERFACE' File.

553.1 CMOP QUERY

> **NOTE:** You already have the 'CMOP QUERY' File.

554 CMOP OPERATIONS

> **NOTE:** You already have the 'CMOP OPERATIONS' File.

555 CMOP MASTER DATABASE ARCHIVE

> **NOTE:** You already have the 'CMOP MASTER DATABASE ARCHIVE' File.

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <u>N</u>O

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// *\[Select Print Device\]*

Install Started for CMOPH 2.0 :

Feb 21, 1997@10:59:44

Installing Routines:

Feb 21, 1997@11:00:23

Installing Data Dictionaries:

Feb 21, 1997@12:19:26

Installing Data:

Feb 21, 1997@12:19:26

Installing PACKAGE COMPONENTS:

Installing BULLETIN

Installing SECURITY KEY

Installing INPUT TEMPLATE

CMOPH 2.0

------------------------------------------------------------------------

Installing OPTION

Feb 21, 1997@12:19:51

Running Post-Install Routine: ^PSXPOST

Initialization complete!!

Updating Routine file...

Updating KIDS files...

CMOPH 2.0 Installed.

Feb 21, 1997@12:20:02

Install Message sent

--------------------------------------------------------------------------

+------------------------------------------------------------+

100% \| 25 50 75 \|

Complete +------------------------------------------------------------+

Install Completed

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Journaling Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Journaling of the PSX global is recommended for all HOST facilities.

## Security Keys Used by CMOP Host Facilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The security keys listed below control the access necessary to operate the CMOP software. At the host CMOP, these keys should be assigned by the CMOP Director or a designee.

> PSXCMOPMGR This security key locks the *CMOP System Management Menu.*

> PSXCOST This key allows the holder to access the compile/recompile, initialize, update, and purge options of the *Facility Cost Management* menu.

> PSXRPH This key should only be assigned to the pharmacists who will be responsible for the release of prescriptions at the CMOP. The user must have this key to manually release Rx’s at the CMOP host facility.

> PSNMGR This security key is used to lock the *CMOP Mark/Unmark (Single drug)* and the *Loop CMOP Match to Local Drug File* options which use the NATIONAL DRUG file (#50.6) to mark and match items for CMOP dispense. This key is not exported with CMOP.

> PSXMAIL This security key enables a site manager to specify who receives the various mail messages and alerts generated by the CMOP process. The user(s) assigned this key must be active in the system. When the mail messages are generated, the software will look for users with the PSXMAIL key who are active. If there are no users with this key or there are users with this key who are inactive, then the software will send the messages to all holders with the PSXCMOPMGR key.

## Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At the host CMOP facility , it is recommended that the system manager schedule the background jobs to purge data from the CMOP DATABASE file (#552.2), the CMOP REFERENCE file (#552.1), the CMOP RELEASE file (#552.3), and the CMOP Release Acknowledgements from the CMOP OPERATIONS file (#554) on a scheduled basis.

> Both the CMOP REFERENCE file (#552.1) and the CMOP DATABASE file (#552.2) are purged by the same job. This job is scheduled by using the *Nightly Purge of CMOP Database*, \[PSX PURGE CMOP DATABASE\] under the *Operations Management* menu option on the *CMOP System Management Menu*. This job should be scheduled to run during non-peak hours to lessen the impact on system operations. Once scheduled, this job will reschedule to run again every 24 hours. This job will purge the data from the SITE TEXT field (#14) in the CMOP REFERENCE file (#552.1), and related data from the CMOP DATABASE file (#552.2) for those transmissions marked as Closed in the STATUS field (#1) of the CMOP REFERENCE file (#552.1).

> The purge of the CMOP RELEASE file (#552.3) is scheduled through the *Nightly Purge of Release Data*, \[PSX PURGE RELEASE\] option under the *Operations Management* menu on the *CMOP System Management Menu*. This job should be scheduled to run during non-peak hours to lessen the impact on system operations. Once scheduled, this job will reschedule to run every 24 hours. It will purge all data from the CMOP RELEASE file (#552.3) that is marked as Ready to Purge in the PURGE field (#1).

> The purge of the Release Data Acknowledgements from the CMOP OPERATIONS file (#554) is scheduled through the *Nightly Purge of Release Data* \[PSX PURGE RELEASE\] option under the *Operations Management* menu on the *CMOP System Management Menu*. This job should be scheduled to run during non-peak hours to lessen the impact on the system’s performance. When scheduling this job, the user is required to enter the number of days of acknowledgements to keep in the file. Once scheduled, this job will reschedule to run every 24 hours.

> These three jobs should be scheduled upon installation of the CMOP software. Only one schedule can be set up at a time for these jobs. If the system has to be shut down, these three jobs should be unscheduled first. They can be unscheduled using the same options used to set up the schedule. Once the system is brought back up, these jobs should be rescheduled again. If the system goes down, these jobs should be rescheduled once the system is restored.

# Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A. Hardware Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The host facility must support a port to port connection between the V*IST*A CMOP PC system and the vendor PC system. Label printers should be available for the V*IST*A CMOP system for use in the event of a system failure on the automated dispensing system.

## B. Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Routine Size</u>

> PSXACK 3698

> PSXACT 4735

> PSXARC 4337

> PSXARC1 4947

> PSXARC2 2625

> PSXARPT 3239

> PSXAUTO 5208

> PSXBKD 4881

> PSXBKG 3930

> PSXBLD 4542

> PSXBLD1 3981

> PSXCH 1270

> PSXCMOP 3514

> PSXCMOP0 2157

> PSXCMOP1 3469

> PSXCOPAY 1672

> PSXCOSTU 3569

> PSXCSCMN 3683

> PSXCSDA 3436

> PSXCSDC 2288

> PSXCSDC1 3265

> PSXCSDC2 1697

> PSXCSHI 3315

> PSXCSHI1 1444

> PSXCSLG1 747

> PSXCSLOG 3696

> PSXCSMN1 3312

> PSXCSMON 3074

> PSXCSSUM 3435

> PSXCST 3205

> PSXCST1 1663

> PSXCSTPG 3380

> PSXCSUTL 3362

> PSXDENT 419

> PSXDQUE 2244

> PSXDRPT 3133

> PSXEDIT 4292

> PSXEDRG 1739

> PSXEDUTL 2754

> PSXERR 4613

> PSXERR1 1182

> PSXHENV 1795

> PSXHSYS 8523

> PSXJOB 1327

> PSXLBL 3315

> PSXLBL1 4508

> PSXLBL2 3346

> PSXLBLNR 2408

> PSXLBLPT 670

> PSXLBLT 3183

> PSXLBLU 4867

> PSXLIST 4008

> PSXLKUP 2381

> PSXLTST 653

> PSXMARK 4768

> PSXMISC 3230

> PSXMISC1 4137

> PSXMSGS 4416

> PSXMST 2697

> PSXNEW 3881

> PSXNOCMP 2096

> PSXNOTE 5235

> PSXOCMOP 2232

> PSXOPUTL 3358

> PSXPLOG 851

> PSXPOST 2494

> PSXPURG 4642

> PSXPURG1 1188

> PSXQRY 6744

> PSXQUE 4147

> PSXRACT 3202

> PSXRCVRY 3970

> PSXRECV 4332

> PSXRECV1 4449

> PSXREF 1820

> PSXREJ 3987

> PSXREL 2229

> PSXRENV 3589

> PSXRESUB 2782

> PSXRHLP 3486

> PSXRPPL 5114

> PSXRPPL1 4212

> PSXRPT 6734

> PSXRSTAT 4941

> PSXRSUS 4600

> PSXRSYU 3759

> PSXRTN 5127

> PSXRTN1 5040

> PSXRTR 2648

> PSXRTRAN 7067

> PSXRXQU 3315

> PSXRXU 3062

> PSXSERV 1850

> PSXSITE 4573

> PSXSMRY 4840

> PSXSND 3733

> PSXSTAT 5094

> PSXSTP 547

> PSXSTRT 3438

> PSXSUDCN 2987

> PSXSYS 3388

> PSXTNRPT 4667

> PSXUNHLD 2434

> PSXUNREL 2829

> PSXUTL 3156

> PSXVCK 3831

> PSXVCK1 4729

> PSXVEND 5905

> PSXVIEW 2923

> PSXVND 5420

> PSXVPN 2625

> Total routines 111 Total size 382686

## C. Disk Storage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Disk storage requirements for prescription data at the host CMOP facility should be calculated based on 3-5 prescription records per block.

## D. Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This package requires 19 files in addition to those of the Kernel and other files to which it points. Information about all files, including these can be obtained by using the VA FileMan to generate a list of file attributes.

> Please refer to the documentation for Outpatient Pharmacy V. 6.0 and National Drug File V. 3.16 for detailed information on resource requirements for these software packages.

## E. Host Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>File Numbers</u>; <u>File Names</u>

> 552 CMOP NATIONAL SITE

> 552.1 CMOP REFERENCE

> 552.2 CMOP DATABASE

> 552.3 CMOP RELEASE

> 552.4 CMOP MASTER DATABASE

> 552.5 CMOP COST STATS

> 553 CMOP INTERFACE

> 553.1 CMOP QUERY

> 554 CMOP OPERATIONS

> 555 CMOP MASTER DATABASE ARCHIVE

> 50 DRUG

> 50.6 NATIONAL DRUG

> 51.5 ORDER UNIT

> 54 RX CONSULT

> The namespace for the Consolidated Mail Outpatient Pharmacy package is PSX.