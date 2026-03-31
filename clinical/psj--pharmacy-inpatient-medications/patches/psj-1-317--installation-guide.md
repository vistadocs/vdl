---
title: Inpatient Medications Pharmacy Interface Automation Version 1 Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Install Guide
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 1
patch_id: PSJ*1*317
group_key: "PSJ:PSJ:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - routine
  - table
  - contents
  - pade
  - before
  - after
  - routines
  - patch
  - back
  - installation
page_count: 0
word_count: 3089
section_count: 20
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2016
revision_count: 5
revision_newest: 4/25/16
revision_oldest: 9/15/15
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p317_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p317_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

Inpatient Medications Pharmacy Interface Automation (PIA)

Installation Guide

![](inpatient-medications-pharmacy-interface-automation-version-1-install-guide/001.png)

September 2016

Revision History

| Date     | Version | Description                             | Author                             |
|----------|---------|-----------------------------------------|------------------------------------|
| 4/25/16  | 0.5     | Updated Back out and Rollback sections. | <span class="mark">REDACTED</span> |
| 1/5/16   | 0.4     | Technical edit.                         | <span class="mark">REDACTED</span> |
| 12/31/15 | 0.3     | Added Inbound Configuration.            | <span class="mark">REDACTED</span> |
| 11/24/15 | 0.2     | Added Disaster Recovery section.        | <span class="mark">REDACTED</span> |
| 9/15/15  | 0.1     | Initial draft.                          | <span class="mark">REDACTED</span> |

Revision History includes date of changes, version number, description of changes, and author of revisions.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [System Requirements](#system-requirements)
  - [Pre-Installation](#pre-installation)
  - [Patch Installation](#patch-installation)
  - [Download and Extract Procedure](#download-and-extract-procedure)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Implementation](#implementation)
- [Back-out Procedure](#back-out-procedure)
  - [Back-out Strategy](#back-out-strategy)
  - [Back-out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-out Criteria](#back-out-criteria)
  - [Back-out Risks](#back-out-risks)
  - [Authority for Back-out](#authority-for-back-out)
  - [Back-out Procedure](#back-out-procedure-1)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
- [Disaster Recovery and Continuity of Operations](#disaster-recovery-and-continuity-of-operations)
This document provides installation instructions for Clinical Ancillary Services (CAS) Development Delivery of Pharmacy enhancements (DDPE) Pharmacy Interface Automation (PIA).

# System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are software elements for Inpatient Medications.

> Inpatient Medications Software Elements

| Application                        | Version |
|----------------------------------------|-------------|
| Adverse Reaction Tracking              | 4.0         |
| Decision Support System                | 3.0         |
| Inpatient Medications                  | 5.0         |
| Kernel                                 | 8.0         |
| Laboratory                             | 5.2         |
| Mailman                                | 8.0         |
| National Drug File                     | 4.0         |
| Nursing                                | 4.0         |
| Order Entry/Results Reporting          | 3.0         |
| Outpatient Pharmacy                    | 7.0         |
| Patient Information Management Systems | 5.3         |
| Pharmacy Data Management               | 1.0         |
| RPC Broker (32-bit)                    | 1.1         |
| Toolkit                                | 7.3         |
| VA FileMan                             | 22.0        |

## Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following two patches are provided for this project and should be installed in the order listed below, as the logical link, PSJ PADE that is used for this project is transported in the PSJ patch.

PSJ\*5\*317 - Inpatient Medications V. 5.0

PSS\*1\*193 - Pharmacy Data Management V. 1.0

The associated patches for PSJ\*5\*317 are the following:

PSJ\*5\*191

PSJ\*5\*228

PSJ\*5\*244

PSJ\*5\*281

PSJ\*5\*285

PSJ\*5\*316

The associated patch for PSS\*1\*193 is PSS\*1\*180.

## Patch Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of the Pharmacy Interface Automation Project (PIA) will provide a new standard bi-directional HL7 interface to the Pharmacy Automated Dispensing Equipment (PADE) located at the point of care areas such as Inpatient wards, Outpatient Clinics etc. Depending on the PADE setup, outbound HL7 messages will be sent to the respective PADE via the VistA Interface Engine (VIE), when the following event happens:

- In Inpatient Medications, when orders are verified, edited, renewed, discontinued, reinstated, put on hold/removed from hold etc.
- In Computerized Patient Record System (CPRS), when orders are discontinued.
- In the REGISTRATION package when patients are admitted, discharged, transferred, cancel admit, cancel discharge, cancel transfer, bed switch etc.
- In the Scheduling package when patients are checked in.
- In Pharmacy Data Management, when new drugs are entered or modified.
- Options to schedule nightly jobs to run daily to send patient clinic appointments or surgery cases.
- Options to send medication orders for a single patient or by clinics or by wards.

Installation InstructionsPSJ\*5\*317 - Inpatient Medications V. 5.0.

This patch should be installed with users off the system during off-peak

hours. Installation takes less than five minutes.

1\. Use the INSTALL/CHECK MESSAGE option on the PackMan menu.

2\. From the Kernel Installation & Distribution System menu, select the

Installation menu.

3\. From this menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter PSJ\*5.0\*317)

a\. Backup a Transport Global - this option will create a backup

message of any routines exported with the patch. It will NOT

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - this option will

allow you to view all changes that will be made when the patch

is installed. It compares all components of the patch (routines,

DDs, templates, etc.).

c\. Verify Checksums in Transport Global - this option will ensure

the integrity of the routines that are in the transport global.

4\. Use the Install Package(s) option and select the package PSJ\*5.0\*317.

5\. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of

Install? NO//" respond NO.

6\. When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//"

respond NO.

7\. When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//" respond NO.

Routine Information:

====================

The second line of each of these routines now looks like:

;;5.0;INPATIENT MEDICATIONS;\*\*\[Patch List\]\*\*;16 DEC 97;Build 125

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: PSGBRJ

Before: B19761653 After: B21011842 \*\*12,50,244,317\*\*

Routine Name: PSGOE7

Before: B30726260 After: B40214304 \*\*9,26,34,52,55,50,87,111,181,

254,267,260,288,281,317\*\*

Routine Name: PSGOE82

Before: B21878874 After: B33061347 \*\*2,35,50,67,58,81,127,168,181,

276,317\*\*

Routine Name: PSGOE92

Before: B30935948 After: B43137679 \*\*2,35,50,58,81,110,215,237,

276,316,317\*\*

Routine Name: PSGOEF1

Before: B28843982 After: B36069326 \*\*2,7,35,39,45,47,50,63,67,58,

95,110,186,181,267,317\*\*

Routine Name: PSGPEN

Before: B39805137 After: B57109712 \*\*30,37,50,58,115,110,127,129,317\*\*

Routine Name: PSGPLR

Before: B39066813 After: B40061443 \*\*10,50,67,119,129,191,317\*\*

Routine Name: PSJ317P

Before: n/a After: B6017554 \*\*317\*\*

Routine Name: PSJHLU

Before: B45959307 After: B50964072 \*\*1,56,72,102,134,181,267,285,317\*\*

Routine Name: PSJLMPRU

Before: B14898207 After: B19398098 \*\*16,58,85,110,185,181,267,317\*\*

Routine Name: PSJLMUDE

Before: B66391198 After: B84078277 \*\*7,47,50,63,64,58,80,116,110,

111,164,175,201,181,254,267,

228,317\*\*

Routine Name: PSJO

Before: B28881243 After: B32312057 \*\*31,58,110,181,267,275,317\*\*

Routine Name: PSJO2

Before: B20134007 After: B21667076 \*\*58,317\*\*

Routine Name: PSJPAD50

Before: n/a After:B143814904 \*\*317\*\*

Routine Name: PSJPAD70

Before: n/a After:B193106268 \*\*317\*\*

Routine Name: PSJPAD7I

Before: n/a After: B91989090 \*\*317\*\*

Routine Name: PSJPAD7U

Before: n/a After:B183953635 \*\*317\*\*

Routine Name: PSJPADE

Before: n/a After: B87815402 \*\*317\*\*

Routine Name: PSJPADIT

Before: n/a After:B213276051 \*\*317\*\*

Routine Name: PSJPADPT

Before: n/a After: B74411481 \*\*317\*\*

Routine Name: PSJPADSI

Before: n/a After:B207002155 \*\*317\*\*

Routine Name: PSJPDAPP

Before: n/a After: B26391444 \*\*317\*\*

Routine Name: PSJPDCL

Before: n/a After: B58778000 \*\*317\*\*

Routine Name: PSJPDCLA

Before: n/a After:B123299808 \*\*317\*\*

Routine Name: PSJPDCLU

Before: n/a After:B182392496 \*\*317\*\*

Routine Name: PSJPDRIN

Before: n/a After:B220627483 \*\*317\*\*

Routine Name: PSJPDRIP

Before: n/a After: B92189032 \*\*317\*\*

Routine Name: PSJPDRTP

Before: n/a After:B164565338 \*\*317\*\*

Routine Name: PSJPDRTR

Before: n/a After:B204379013 \*\*317\*\*

Routine Name: PSJPDRU1

Before: n/a After:B195220461 \*\*317\*\*

Routine Name: PSJPDRUT

Before: n/a After:B233191952 \*\*317\*\*PSS\*1\*193 – Pharmacy Data Management V. 1.0.

This patch should be installed with users off the system during off-peak

hours. Installation takes less than two minutes.

1\. Use the INSTALL/CHECK MESSAGE option on the PackMan menu.

2\. From the Kernel Installation & Distribution System menu, select the

Installation menu.

3\. From this menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter PSS\*1.0\*193)

a\. Backup a Transport Global - this option will create a backup

message of any routines exported with the patch. It will NOT

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - this option will

allow you to view all changes that will be made when the patch

is installed. It compares all components of the patch (routines,

DDs, templates, etc.).

c\. Verify Checksums in Transport Global - this option will ensure

the integrity of the routines that are in the transport global.

4\. Use the Install Package(s) option and select the package PSS\*1.0\*193.

5\. When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//"

respond NO.

6\. When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//" respond NO.

Routine Information:

====================

The second line of each of these routines now looks like:

;;1.0;PHARMACY DATA MANAGEMENT;\*\*\[Patch List\]\*\*;9/30/97;Build 17

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: PSSDEE

Before: B98607664 After:B110481507 \*\*3,5,15,16,20,22,28,32,34,33,

38,57,47,68,61,82,90,110,155,

156,180,193\*\*

Routine Name: PSSHLDFS

Before: n/a After: B33701533 \*\*193\*\*

Routine Name: PSSMSTR

Before: B1853023 After: B51317382 \*\*82,193\*\*

## Download and Extract Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Outbound

Outbound to PADE setup will be configured in VistA to send the information to the appropriate PADE. The main purpose of the Outbound setup is to map the send areas to the location of the cabinets in the wards, clinics, and/or operating rooms.

Please refer to the [Pharmacy Interface Automation Startup and Troubleshooting Guide](http://vaww.esm.infoshare.va.gov/sites/hps/PS_CA/CASDDPEA/PIAIDTS/PIAIPTS/Project%20Documentation/Forms/AllItems.aspx) for more details.

2.  Inbound

The PADE Inbound HL7 interface must be configured prior to first use. The Inbound HL7 interface does not require the PADE Outbound HL7 interface. However, the inbound interface does require an entry in the outbound system file PADE SYSTEM SETUP (#58.7) before it can be activated.

Please refer to the [Pharmacy Interface Automation Startup and Troubleshooting Guide](http://vaww.esm.infoshare.va.gov/sites/hps/PS_CA/CASDDPEA/PIAIDTS/PIAIPTS/Project%20Documentation/Forms/AllItems.aspx) for more details.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PIA Implementation Plan specifies how the Pharmacy Interface Automation project will be evaluated and subsequently deployed within the Office of Enterprise Development (OED).

The PIA Implementation Plan:

1.  Describes the phased implementation for the implementation
2.  States objectives for the implementation
3.  Addresses risks associated with implementation

    Refer to the [PIA Implementation Plan](http://vaww.esm.infoshare.va.gov/sites/hps/PS_CA/CASDDPEA/PIAIDTS/PIAIPTS/Project%20Documentation/Forms/AllItems.aspx) for more detailed information.

# Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section details the back-out procedure for PIA.

## Back-out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 4.6 for more details.

## Back-out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To be determined

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing is in progress.

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The project is canceled and the implemented features are no longer wanted by the stake holders.

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To be determined

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority would come from the IPT and the VA project manager.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event that the Pharmacy Interface Automation enhancements must be backed out, the modified routines must have been backed-up during patch installation using the following option:

Backup a Transport Global \[XPD BACKUP\]

This option creates a MailMan message of any routines exported with this patch. (If you need to preserve components that are not routines, you must back them up separately.)

Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 5 Backup a Transport Global

select INSTALL NAME: *Backup of Patch_XXXXX* 12/5/15@13:29:01

> =\> *Backup of Patch_XXXXX*

This Distribution was loaded on Feb 05, 2013@13:29:01 with header of Patch_XXXXX Test Version

It consisted of the following Install(s): Patch_XXXXX Test Version

> Subject: Backup of Patch_XXXXX install on Feb 05, 2013

> Replace

> Loading Routines for XXXXX

> Routine YYYY1

> Routine YYYY2

> Routine YYYY3

> Send mail to: ADPAC,ONE// ADPAC,ONE

> Select basket to send to: IN// BACKUP PATCH (Folder for FORUM)

> And Send to:

<u>Restore Pre-Patch Routines (MailMan)</u>

Go to the Backup of Patch_XXXXX message in Mailman.

At the <u>Enter message action</u> prompt, enter “X” to “Xtract PackMan”

At the <u>Select PackMan Function</u> prompt enter the number 6 to *Install/Check Message*

At the end of this process the pre-patch routines are restored.

> **NOTE:** See header “Install the Patch Backup” for detail

<u>Install the Patch Backup</u>BACKUP PATCH Basket, 144 messages (1-144), 117 new

\*=New/!=Priority.....Subject....................................From...

>   141. Backup of Patch_XXXXX install on Oct 01, 2015   ADPAC,ONE

IN Basket Message: 1// 141

Subj: Backup of XXXXX install on Oct 01, 2015  \[#000000\] 10/01/15@11:14

2016 lines

From: ADPAC,ONE In 'IN' basket.   Page 1

-----------------------------------------------------------------------

\$TXT PACKMAN BACKUP Created on Thursday, 10/1/15 at 11:14:50 by ADPAC,ONE

Enter message action (in IN basket): Ignore// Xtract PackMan

Select PackMan function: 6  INSTALL/CHECK MESSAGE

> **WARNING:** Installing this message will cause a permanent update of globals

and routines.

Do you really want to do this? NO// YES

Routines are the only parts that are backed up.  NO other parts

are backed up, not even globals.  You may use the 'Summarize Message'

option of PackMan to see what parts the message contains.

Those parts that are not routines should be backed up separately

if they need to be preserved.

Shall I preserve the routines on disk in a separate back-up message? YES// NO

No backup message built.

Line 123  Message \#000000  Unloading Routine Routine_Name1 (PACKMAN_BACKUP)

Line 345  Message \#000000  Unloading Routine Routine_Name2 (PACKMAN_BACKUP)

Line 567  Message \#000000  Unloading Routine Routine_Name3 (PACKMAN_BACKUP)

Line 789  Message \#000000  Unloading Routine Routine_Name4 (PACKMAN_BACKUP)

====================================================================<u>New Routine(s)</u>

New routines implemented by the patches can be deleted/removed by using the following option:

Delete Routines \[XTRDEL\]

This option can be found under the Routine Tools menu

Select OPTION NAME: XUPROG Programmer Options

KIDS Kernel Installation & Distribution System ...

NTEG Build an 'NTEG' routine for a package

PG Programmer mode

Calculate and Show Checksum Values

Delete Unreferenced Options

Error Processing ...

Global Block Count

List Global

Map Pointer Relations

Number base changer

Routine Tools ...

Test an option not in your menu

Verifier Tools Menu ...

Select Programmer Options \<TEST ACCOUNT\> Option: ROUTINE Tools

%Index of Routines

Check Routines on Other CPUs

Compare local/national checksums report

Compare routines on tape to disk

Compare two routines

Delete Routines

First Line Routine Print

Flow Chart Entire Routine

Flow Chart from Entry Point

Group Routine Edit

Input routines

List Routines

Load/refresh checksum values into ROUTINE file

Output routines

Routine Edit

Routines by Patch Number

Variable changer

Version Number Update

Select Routine Tools \<TEST ACCOUNT\> Option: DELEte Routines

ROUTINE DELETE

All Routines? No =\> No

Routine: ROUT999

Routine:

1 routine

1 routines to DELETE, OK: NO// YES

ROUT999

Done.<u>Other Components</u>

Data dictionary and template modifications must be removed using a follow-up patch.

<u>File Name (#) Field Name (#) New/Modified/Deleted</u>

PADE SYSTEM SETUP (#58.7) All fields New

PADE SEND AREA (#58.71) All fields New

PADE OUTBOUND MESSAGES (#58.72) All fields New

PADE DISPENSING DEVICE (#58.63) All fields New

PADE INBOUND TRANSACTIONS (#58.6) All fields New

PADE INVENTORY SYSTEM (#58.601) All fields New

PADE USER (#58.64) All fields New

INPATIENT WARD PARAMETERS (#59.6) DEFAULT 0 ON PADE New

PRE-EXCHANGE (#8)

<u>Kernel Parameters New/Modified/Deleted</u>

PSJ PADE OE BALANCES New

<u>Mail Group New/Modified/Deleted</u>

PSJ PADE DISPENSE ALERTS New

<u>Options New/Modified/Deleted</u>

Unit Dose Medications \[PSJU MGR\] Modified Menu

PADE Main Menu \[PSJ PADE MAIN MENU\] New Menu

PADE Send Area Setup \[PSJ PADE SEND AREA SETUP\] New Option

PADE System Setup \[PSJ PADE SETUP\] New Option

PADE Inventory Setup \[PSJ PADE INVENTORY MENU\] New Menu

Inventory System Setup \[PSJ PADE INVENTORY SYSTEM\] New Option

Dispensing Device Setup \[PSJ PADE DEVICE SETUP\] New Option

PADE Send Surgery Cases \[PSJ PADE SEND SURGERY CASES\] New Option

PADE Surgery Task \[PSJ PADE SURGERY TASK\] New Option

PADE Reports \[PSJ PADE REPORTS MENU\] New Menu

PADE On-Hand Amounts \[PSJ PADE INVENTORY REPORT\] New Option

PADE Transaction Report \[PSJ PADE TRANSACTION REPORT\] New Option

PADE System Division Setup \[PSJ PADE DIVISION SETUP\] New Option

PADE Send Patient Orders \[PSJ PADE SEND ORDERS\] New Option

PSJ PADE Appointment Task \[PSJ PADE APPOINTMENT TASK\] New Option

Send Drug File Entries to External Interface Modified Option

\[PSS MASTER FILE ALL\]

<u>Protocols New/Modified/Deleted</u>

PSJ ADT-A01 CLIENT New

PSJ ADT-A01 ROUTER New

PSJ ADT-A01 SERVER New

PSJ ADT-A02 SERVER New

PSJ ADT-A02 CLIENT New

PSJ ADT-A03 SERVER New

PSJ ADT-A03 CLIENT New

PSJ ADT-A11 SERVER New

PSJ ADT-A11 CLIENT New

PSJ ADT-A12 SERVER New

PSJ ADT-A12 CLIENT New

PSJ ADT-A13 SERVER New

PSJ ADT-A13 CLIENT New

PSJ SIU-SDAM ROUTER New

PSJ SIU-S12 SERVER New

PSJ SIU-S12 CLIENT New

PSJ RDEO11 SERVER New

PSJ RDEO11 CLIENT New

PSJ PADE OMS-O05 EVENT New

PSJ PADE OMS-O05 SUB New

PSJ PADE OMS-O05 EVENT 2.3 New

PSJ PADE OMS-O05 SUB 2.3 New

PSJ LM PADE ACTIVITY New

PSJ LM PROFILE HIDDEN ACTIONS Modified

PSS MFNM01 SERVER New

PSS MFNM01 CLIENT New

<u>Security Keys New/Modified/Deleted</u>

PSJ PADE ADV New

PSJ PADE MGR New

PSS PADE INIT New

<u>Templates New/Modified/Deleted</u>

PSJ PADE SYSTEM Input 58.7 New

PSJ PADE INVENTORY Input 58.601 New

PSJ PADE DISPENSING DEVICE Input 58.63 New

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections detail the rollback procedure for PIA.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A follow-up patch would be needed to remove new data entries established by the data dictionary. Specific rollback details will be incorporated in subsequent versions, but a patch would only be created if necessary.

> **NOTE:** These new data entries are the result of a new field added to the data dictionary or the modification of an existing field in the data dictionary.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <u>back-out</u> of PHARMACY INTERFACE AUTOMATION (PIA) patches that modified existing fields, and established new fields would be justification for rollback.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority would come from the IPT and the VA project manager.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A follow-up patch for each namespace would be needed to delete/modify that namespace’s data dictionary entries that were added/modified  and other non-routine components added/modified by this projects patches and would follow the basic logic flow below.

<u>Logic flow using FileMan API calls as much as possible for the below actions</u>

1.  New data fields would need to be erased that were likely populated by the new functionality, while the new data fields are still valid in the data dictionary.
2.  New file cross references would now need to be deleted.
3.  New fields need to be deleted out of the data dictionary.
4.  Modified data dictionary fields would need to be restored.
5.  New SECURITY KEY file (#19.1) entries needs to be deleted.
6.  Existing PROTOCOL file (#101) entries would need to be restored while new file entries  would be deleted from the site.
7.  Existing OPTION file (#19) entries would need to be restored while new file entries would be deleted from the site.
8.  Existing PARAMETERS file (#8989.5) entries would need to be restored while new file entries would be erased and then deleted from the Kernel Parameter Definition file at the site.
9.  Existing PARAMETER DEFINITION file (#8989.51) entries would need to be restored while new file entries would be erased and then deleted from the PARAMETER DEFINITION file at the site.
10. New INPUT TEMPLATES file (.402) entries need to be deleted.
11. New HL LOGICAL LINK file (#870) entry needs to be deleted.
12. New HL7 APPLICATION PARAMETER file (#771) entries needs to be deleted.

# Disaster Recovery and Continuity of Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each VistA facility as well as regional data centers are responsible for their own disaster recovery (DR) and Continuity of Operations (COOP). Please refer to the VistA Disaster Recovery and Continuity of Operations Plans at the specific facility. Most of these documents are considered confidential in that information that could disrupt any of these facilities DR or COOP could cause catastrophic data loss. Therefore the following link is just an example:

<span class="mark">REDACTED</span>