---
title: PSX*2*74 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: PSX
app_name: 'Pharmacy: Consolidated Mail Outpatient Pharmacy'
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2*74
group_key: PSX:PSX:2
file_numbers: []
security_keys: []
menu_options: 0
description: Electronic Data Interchange (EDI) New Standards and Operating Rules –VHA Provider-side Technical Compliance
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 2040
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: null
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_p74_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_p74_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=85
audit_applied: '2026-05-31'
master_source: PSX*2*74 Release Notes
master_pub_date: 'null'
consolidated_from: 3 versions
prior_versions:
- PSX*2*77 Release Notes
- PSX*2*79 Release Notes
consolidated_title: release notes
---

> ![](psx-2-74-release-notes/001.png)

Electronic Data Interchange (EDI) New Standards and Operating Rules –VHA Provider-side Technical Compliance RequirementsTAC-12-03366

ePharmacy

####### Consolidated Mail Outpatient Pharmacy (CMOP)

####### RELEASE NOTES/

####### INSTALLATION GUIDEPSX\*2\*74November 2013

*Version 1.0*

Office of Enterprise Development

Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Documentation Distribution](#documentation-distribution)
- [Patch Description and Installation Instructions](#patch-description-and-installation-instructions)
  - [Patch Description](#patch-description)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Installation Instructions](#installation-instructions)
- [Enhancements](#enhancements)
  - [Fundamental Specifications for CMOP](#fundamental-specifications-for-cmop)
    - [Background Claims Processing](#background-claims-processing)
    - [¾ Days' Supply Calculation](#¾-days-supply-calculation)
This patch has enhancements that extend the capabilities of the Veterans
Health Information Systems and Technology Architecture (VistA) electronic
pharmacy (ePharmacy) billing system. Below is a list of all the
applications involved in this project along with their patch number:
APPLICATION/VERSION PATCH
---------------------------------------------------------------
OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*421
INTEGRATED BILLING (IB) V. 2.0 IB\*2\*494
ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*15
CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP) V. 2.0 PSX\*2\*74
ACCOUNTS RECEIVABLE (PRCA) V. 4.5 PRCA\*4.5\*295
The patches (PSO\*7\*421, IB\*2\*494, BPS\*1\*15, PSX\*2\*74 and PRCA\*4.5\*295)
are being released in the Kernel Installation and Distribution System
(KIDS) multi-build distribution BPS PSO IB PSX PRCA BUNDLE 8.0.
The purpose of this software package is to ensure National Council for
Prescription Drug Programs (NCPDP) D.0 - D.9 transactions are functional
in the Electronic Data Interchange (EDI) New Standards and Operating Rules
environment and includes annual External Code List (ECL) updates into
NCPDP fields.
The package also provides the ability to alert the pharmacist at the time of
prescription processing regarding the days' supply benefit.

## Documentation Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to FTP the files from <span class="mark">REDACTED</span>.

This transmits the files from the first available FTP server. Sites may

also elect to retrieve software directly from a specific server as follows:

<span class="mark">REDACTED</span>

The documentation will be in the form of Adobe Acrobat files.

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl/

Title File Name FTP Mode

-----------------------------------------------------------------------

CMOP Patch Release Notes/ PSX_2_P74_RN.PDF Binary

Installation Guide

CMOP User Manual PSX_2_UM_R1113.PDF Binary

CMOP User Manual change pages PSX_2_P74_UM_CP.PDF Binary

*(This page included for two-sided copying.)*

# Patch Description and Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch Display Page: 1

=============================================================================

Run Date: SEP 26, 2013 Designation: PSX\*2\*74 TEST v8

Package : CMOP Priority : MANDATORY

Version : 2 Status : UNDER DEVELOPMENT

=============================================================================

Associated patches: (v)PSX\*2\*73 \<\<= must be installed BEFORE \`PSX\*2\*74'

Subject: EPHARMACY OPERATING RULES

Category: ROUTINE

Description:

===========

This patch has enhancements that extend the capabilities of the Veterans

Health Information Systems and Technology Architecture (VistA) electronic

pharmacy (ePharmacy) billing system. Below is a list of all the

applications involved in this project along with their patch number:

APPLICATION/VERSION PATCH

---------------------------------------------------------------

OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*421

INTEGRATED BILLING (IB) V. 2.0 IB\*2\*494

ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*15

CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP) V. 2.0 PSX\*2\*74

ACCOUNTS RECEIVABLE (PRCA) V. 4.5 PRCA\*4.5\*295

The patches (PSO\*7\*421, IB\*2\*494, BPS\*1\*15, PSX\*2\*74 and PRCA\*4.5\*295)

are being released in the Kernel Installation and Distribution System

(KIDS) multi-build distribution BPS PSO IB PSX PRCA BUNDLE 8.0.

The purpose of this software package is to ensure National Council for

Prescription Drug Programs (NCPDP) D.0 - D.9 transactions are functional

in the Electronic Data Interchange (EDI) New Standards and Operating Rules

environment and includes annual External Code List (ECL) updates into

NCPDP fields.

The package also provides the ability to alert the pharmacist at the time of

prescription processing regarding the days' supply benefit.

This specific patch contains the following functionality:

---------------------------------------------------------

1\. If claim rejection is received during CMOP transmission of a prescription, Processing stops by sending the prescription to the "Reject Resolution Required" section of the Third Party Payer Rejects – Worklist. If the prescription fits the following criteria: original fill, Veteran eligibility, not released, the reject is on the Reject Resolution Required list for the current division, and the total gross amount of the prescription is at or above the specified threshold. The prescription will remain on the suspense queue for CMOP.

Patch Components

================

The following is a list of field modifications included in this patch:

File Name (#) New/Modified/

Sub-File Name (#) Field Name (#) Deleted

------------------- ------------------- -------------

N/A

Forms Associated:

Form Name File \# New/Modified/Deleted

--------- ------ --------------------

N/A

Mail Groups Associated:

Mail Group Name New/Modified/Deleted

--------------- --------------------

N/A

Options Associated:

Option Name Type New/Modified/Deleted

----------- ---- --------------------

N/A

Protocols Associated:

Protocol Name New/Modified/Deleted

------------- --------------------

N/A

Security Keys Associated:

Security Key Name

-----------------

N/A

Templates Associated:

Template Name Type File Name (Number) New/Modified/Deleted

------------- ---- ------------------ --------------------

N/A

Additional Information: N/A

New Service Requests (NSRs):

-------------------------------------------------------------

20110503 - Electronic Data Interchange (EDI) New Standards and Operating

Rules (Veterans Health Administration) VHA Provider-Side TCRs.

Patient Safety Issues (PSIs)

-----------------------------

N/A

Remedy Ticket(s) & Overview:

-------------------------------------

N/A

Test Sites:

----------

Birmingham VAMC, AL

Mountain Home VAMC, TN

Richmond VAMC, VA

Little Rock VAMC, AR

Jackson VAMC, MS

Documentation Retrieval Instructions:

------------------------------------

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to FTP the files from <span class="mark">REDACTED</span>.

This transmits the files from the first available FTP server. Sites may

also elect to retrieve software directly from a specific server as follows:

<span class="mark">REDACTED</span>

The documentation will be in the form of Adobe Acrobat files.

Documentation can also be found on the VA Software Documentation Library at:

http://www4.va.gov/vdl/

Title File Name FTP Mode

-----------------------------------------------------------------------

CMOP Patch Release Notes/ PSX_2_P74_RN.PDF Binary

Installation Guide

CMOP User Manual PSX_2_UM_R1113.PDF Binary

CMOP User Manual change pages PSX_2_P74_UM_CP.PDF Binary

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should take less than a minute to install.

DO NOT QUEUE the installation of this patch.

To avoid disruptions, these patches should be installed during non-peak

hours when there is minimal activity on the system. Avoid times when ECME

claims are being transmitted. Of particular concern are the options below.

1\. BPS NIGHTLY BACKGROUND JOB \[BPS NIGHTLY BACKGROUND JOB\]

Do not install the patch when ECME claims are being generated

by the BPS Nightly Background Job option. Wait for this job to

finish or complete the installation before this job starts.

2\. Scheduled CS Transmission \[PSXR SCHEDULED CS TRANS\] and

Scheduled Non-CS Transmission \[PSXR SCHEDULED NON-CS TRANS\]

Do not install the patch when prescriptions are being

transmitted to CMOP. Wait for the CMOP transmissions to finish

or complete the installation before the transmissions start. Both

the CS (Controlled Substances) and the non-CS CMOP transmission

options should be checked. Check with Pharmacy Service or your

Pharmacy ADPAC to find out when CMOP transmissions occur.

Pre-Installation Instructions

-----------------------------

1\. OBTAIN PATCHES

--------------

Obtain the host file BPS_1_15_PSO_IB_PSX_PRCA.KID, which contains the

following patches:

BPS\*1.0\*15

PSO\*7.0\*421

IB\*2.0\*494

PSX\*2.0\*74

PRCA\*4.5\*295

Sites can retrieve VistA software from the following FTP addresses.

The preferred method is to FTP the files from: <span class="mark">REDACTED</span>

This will transmit the files from the first available FTP server.

Sites may also elect to retrieve software directly from a specific

server as follows:

<span class="mark">REDACTED</span>

The BPS_1_15_PSO_IB_PSX_PRCA.KID host file is located in the

anonymous.software directory. Use ASCII Mode when downloading the

file.

2\. START UP KIDS

-------------

Start up the Kernel Installation and Distribution System Menu option

\[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INStallation

---

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option:

3\. LOAD TRANSPORT GLOBAL FOR MULTI-BUILD

-------------------------------------

From the Installation menu, select the Load a Distribution option.

When prompted for "Enter a Host File:", enter the full directory path

where you saved the host file BPS_1_15_PSO_IB_PSX_PRCA.KID (e.g.,

SYS\$SYSDEVICE:\[ANONYMOUS\]BPS_1_15_PSO_IB_PSX_PRCA.KID).

When prompted for "OK to continue with Load? NO//", enter "YES."

The following will display:

Loading Distribution...

BPS PSO IB PSX BUNDLE 8.0

BPS\*1.0\*15

PSO\*7.0\*421

IB\*2.0\*494

PSX\*2.0\*74

PRCA\*4.5\*295

Use INSTALL NAME: BPS PSO IB PSX PRCA BUNDLE 8.0 to install this

Distribution.

4\. RUN OPTIONAL INSTALLATION OPTIONS FOR MULTI-BUILD

-------------------------------------------------

From the Installation menu, you may select to use the following

options (when prompted for the INSTALL NAME, enter

BPS PSO IB PSX PRCA BUNDLE 8.0):

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as data dictionaries or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, data dictionaries, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. INSTALL MULTI-BUILD

-------------------

This is the step to start the installation of this KIDS patch. This

will need to be run for the BPS PSO IB PSX PRCA BUNDLE 8.0.

a\. Choose the Install Package(s) option to start the patch

install.

b\. When prompted for the "Select INSTALL NAME:", enter BPS PSO IB

PSX PRCA BUNDLE 8.0.

c\. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of

Install? YES//", enter YES unless your system does this in a nightly

TaskMan process.

d\. When prompted "Want KIDS to INHIBIT LOGONs during the install?

YES//", enter NO.

e\. When prompted " Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//", enter NO.

f\. When prompted "Device: HOME//", respond with the correct device

but do not queue this install.

Post-Installation Instructions

------------------------------

N/A

Routine Information:

====================

The second line of each of these routines now looks like:

;;2.0;CMOP;\*\*\[Patch List\]\*\*;11 Apr 97;Build 11

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: PSXRPPL1

Before: B51826224 After: B53745747 \*\*3,48,62,66,65,69,73,74\*\*

Routine Name: PSXRPPL2

Before: B55199697 After: B51636489 \*\*65,69,73,74\*\*

Routine list of preceding patches: 73

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Fundamental Specifications for CMOP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Background Claims Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Add Reject Resolution Required Processing to the CMOP feature

If claim rejection is received during CMOP transmission of a prescription, Processing stops by

sending the prescription to the "Reject Resolution Required" section of the Third Party Payer

Rejects - Worklist. If the prescription fits the following criteria: original fill, Veteran eligibility,

not released, the reject is on the Reject Resolution Required list for the current division, and the

total gross amount of the prescription is at or above the specified threshold. The prescription will remain on the suspense queue for CMOP.

#### Add Reject Resolution Required Processing to the Local Suspense feature

If claim rejection is received during local suspense processing for a prescription, Processing stops by sending the prescription to the "Reject Resolution Required" section of the Third Party Payer Rejects – Worklist if the prescription fit the following criteria: original fills, Veteran eligibility, not released, the reject was on the Reject Resolution Required reject list for the current division, and the total gross amount of the prescription was at or above the specified threshold.

The prescription remained on the suspense queue for local suspense.

#### Remove "Allow All Rejects" Processing

All prescription processing that used background claims processing no longer referenced the "Allow All Rejects" flag from the ePharmacy Site Parameters Screen to send a reject to the Third Party Payer Rejects – Worklist.

This requirement pertains to decommissioned functionality.

### ¾ Days' Supply Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Round Up the Calculated Days

The VistA ePharmacy calculated suspense days by using the date of service from the most recent successfully transmitted claim and rounding any partial day to the next full day. (For example, 3.1 days became 4 days.)

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSX*2*79 Release Notes

## Documentation and Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to retrieve files from <span class="mark">REDACTED</span>.

This transmits the files from the first available server. Sites may also

elect to retrieve files directly from a specific server.

Sites may retrieve the documentation directly using Secure File Transfer

Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl

Title File Name Transfer Mode

---------------------------------------------------------------------------

Release Notes/Installation Guide PSX_2_P79_RN.PDF Binary

User Manual PSX_2_UM.PDF Binary

*(This page included for two-sided copying.)*

## Overview of Backout and Rollback Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback plan for VistA applications is complex and not able to be a "one size fits all." The general strategy for VistA rollback is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch; otherwise, the site should contact the Enterprise Program Management Office (EPMO) directly for specific solutions to their unique problems.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer can back up the modified routines using the 'Backup a Transport Global' action. The installer can restore the routines using the MailMan message that were saved prior to installing the patch. The backout procedure for global, data dictionary and other VistA components is more complex and will require issuance of a follow-up patch to ensure all components are properly removed. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with restoration of the data. This backout may need to include a database cleanup process.

Please contact the EPMO for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to backout the patch. If the installed patch that needs to be backed out includes a pre or post install routine please contact the EPMO before attempting the backout.

From the Kernel Installation and Distribution System Menu, select

the Installation Menu.  From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch \#.

    a. Backup a Transport Global - This option will create a backup

       message of any routines exported with this patch. It will not

       backup any other changes such as DD's or templates.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure for VistA patches is complicated and may require a follow-up patch to fully roll back to the pre-patch state. This is due to the possibility of Data Dictionary updates, Data updates, cross references, and transmissions from VistA to offsite data stores.

Please contact the product development team for assistance if needed.

*(This page included for two-sided copying.)*

## System Feature: Billing Determination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IB Billing Determination uses the ePharmacy Billable fields to assess billable status and the Sensitive Diagnosis Drug field to assess sensitive diagnosis instead of using the DEA, Special HDLG field.

### From: PSX*2*77 Release Notes

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Updated documentation describing the new functionality introduced by this patch is available.

> The preferred method is to FTP the files from ftp:// <span class="mark">REDACTED</span>

> /. This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

> <span class="mark">REDACTED</span>

> Documentation can also be found on the VA Software Documentation Library at: <http://www4.va.gov/vdl/>

> Title File Name FTP Mode

> Release Notes/Installation Guide PSX_2_P77_RN.PDF Binary User Manual PSX_2_UM_R0116.PDF Binary

> Technical Manual PSX_2_TM_R0116.PDF Binary

#### (This page included for two-sided copying.)

## Routine Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The second line of each of these routines now looks like:

> ;;2.0;CMOP;\*\*\[Patch List\]\*\*;11 Apr 97;Build 3

> The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

> Routine Name: PSXBPSMS

> Before: B11444984 After: B21102458 \*\*48,77\*\* Routine Name: PSXMSGS

> Before: B24952454 After: B29772543 \*\*1,2,4,24,23,27,30,41,77\*\*

> Routine list of preceding patches: 41, 48

## Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CMOP Not Transmitted Rx List Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The 'ePharmacy - CMOP Not Transmitted Rx List' Mailman bulletin was modified to ensure the body text accurately reflects the reason the CMOP prescriptions cannot be transmitted. Each prescription listed in the body text indicates the number of times an Rx was not transmitted to CMOP and the date of the first unsuccessful transmission to CMOP. In addition, the subject was modified to include the site name.

### CMOP Not Dispensed Rx List Bulletin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The 'CMOP Not Dispensed Rx List' mailman bulletin was modified to include the standard symbols denoting additional information used by Outpatient pharmacy. Prescription numbers with a corresponding ePharmacy claim shall be marked with 'e'. Prescription numbers with a first party copay shall be marked with '\$'.

## Issue Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### This patch addresses the following New Service Request (NSR):

#### - NCPDP Continuous Maintenance Standards (Phase 2, Iteration 2

### Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### There are no Remedy Tickets associated with this patch.
