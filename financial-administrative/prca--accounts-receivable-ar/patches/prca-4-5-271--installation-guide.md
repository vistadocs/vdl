---
title: PRCA*4.5*271 AR ePharmacy Phase V Release Notes and Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: AR ePharmacy Phase V Release Notes and
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5*271
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - prca
  - patch
  - installation
  - table
  - contents
  - distribution
  - install
  - pharmacy
  - version
  - number
page_count: 0
word_count: 1820
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p271_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p271_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

![](prca-4-5-271-ar-epharmacy-phase-v-release-notes-and-installation-guide/001.png)

ePharmacy

PHASE VAccounts Receivable (PRCA)

Release Notes

PRCA\*4.5\*271

October 2011

Product Development

Table of Contents

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
  - [Technical Modifications](#technical-modifications)
    - [Change to Maximum Length of ECME Number](#change-to-maximum-length-of-ecme-number)
  - [Issue Resolutions](#issue-resolutions)
    - [New Service Requests (NSRs)](#new-service-requests-nsrs)
    - [Remedy Tickets](#remedy-tickets)
This patch has enhancements that extend the capabilities of the Veterans Health Information Systems and Technology Architecture (VistA) electronic pharmacy (ePharmacy) billing system. Below is a list of all the applications involved in this project along with their patch number:
<u>APPLICATION/VERSION PATCH</u>
Outpatient Pharmacy (OP) V. 7.0 PSO\*7\*359
Integrated Billing (IB) V. 2.0 IB\*2\*435
Electronic Claims Management Engine (ECME) V. 1.0 BPS\*1\*10
Accounts Receivable (PRCA) V. 4.5 PRCA\*4.5\*271
The four patches (PSO\*7\*359, IB\*2\*435, BPS\*1\*10, and PRCA\*4.5\*271) are being released in the Kernel Installation and Distribution System (KIDS) multi-build distribution BPS PSO IB PRCA BUNDLE 6.0. For more specific instructions please refer to the installation steps provided in each of the patches.
For the pharmacy claims that are processed electronically, the ePharmacy module is currently compliant with the National Council for Prescription Drug Programs (NCPDP) industry standards for version 5.1. NCPDP version D.0 Level 1 compliance (completion of internal testing) must be in place by January 1, 2011, and it must have completed external testing with payers and be in production as of January 1, 2012. Meeting the deliverable dates is essential to VHA meeting this legislative mandate and for continued business with pharmacy payers. As part of these changes, VHA should also have backwards compatibility to the NCPDP version 5.1 to allow for continued revenue and processing of VHA pharmacy claims.
This combined build will allow the processing and release of prescriptions for patients with Insurance payers that use the new NCPDP version D.0 format for electronic claims processing as well as the current NCPDP version 5.1 format.

## Documentation Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation distribution includes:

FILE NAME DESCRIPTION

---------------------------------------------------------------------

PRCA_4_5_P271_RN.PDF AR Release Notes

 

*(This page included for two-sided copying.)*

# Patch Description and Installation Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DHCP Patch Display Page: 1

=============================================================================

Run Date: SEP 13, 2011 Designation: PRCA\*4.5\*271

Package : ACCOUNTS RECEIVABLE Priority : MANDATORY

Version : 4.5 Status : RELEASED

=============================================================================

Associated patches: (v)PRCA\*4.5\*247\<\<= must be installed BEFORE \`PRCA\*4.5\*271'

(v)PRCA\*4.5\*268\<\<= must be installed BEFORE \`PRCA\*4.5\*271'

(v)PRCA\*4.5\*269\<\<= must be installed BEFORE \`PRCA\*4.5\*271'

Subject: ePharmacy Phase 5 - NCPDP D.0

Category: ROUTINE

ENHANCEMENT

OTHER

Description:

===========

This patch has enhancements that extend the capabilities of the Veterans

Health Information Systems and Technology Architecture (VistA) electronic

pharmacy (ePharmacy) billing system. Below is a list of all the

applications involved in this project along with their patch number:

APPLICATION/VERSION PATCH

--------------------------------------------------------------

OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*359

INTEGRATED BILLING (IB) V. 2.0 IB\*2\*435

ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*10

ACCOUNTS RECEIVABLE (PRCA) V. 4.5 PRCA\*4.5\*271

The four patches (PSO\*7\*359, IB\*2\*435, BPS\*1\*10, and PRCA\*4.5\*271) are

being released in the Kernel Installation and Distribution System (KIDS)

multi-build distribution BPS PSO IB PRCA BUNDLE 6.0. For more specific

instructions please refer to the installation steps provided in each of

the patches.

For the pharmacy claims that are processed electronically, the ePharmacy

module is currently compliant with the National Council for Prescription

Drug Programs (NCPDP) industry standards for version 5.1. NCPDP version

D.0 Level 1 compliance (completion of internal testing) must be in place

by January 1, 2011, and it must have completed external testing with

payers and be in production as of January 1, 2012. Meeting the deliverable

dates is essential to VHA meeting this legislative mandate and for

continued business with pharmacy payers. As part of these changes, VHA

should also have backwards compatibility to the NCPDP version 5.1 to allow

for continued revenue and processing of VHA pharmacy claims.

The combined build will allow the processing and release of prescriptions

for patients with Insurance payers that use the new NCPDP version D.0

format for electronic claims processing as well as the current NCPDP

version 5.1 format.

This specific patch contains the following functionality:

---------------------------------------------------------

1\. The ECME number has been expanded to be 12 digits in length. This

patch makes modifications to AR routines to accommodate a longer

ECME number.

This patch addresses the following New Service Request (NSR):

-------------------------------------------------------------

Request Name: e-Pharmacy Phase 5: FY09

Request ID: 20080103

This patch addresses the following Remedy Tickets:

--------------------------------------------------

There are no Remedy Tickets associated with this patch.

Components Sent With Patch

--------------------------

The following is a list of files included in this patch:

UP SEND DATA USER

DATE SEC. COMES SITE RSLV OVER

FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

--------------------------------------------------------------------------

344 AR BATCH PAYMENT YES YES NO NO

The following is a list of fields included in this patch:

Field Name (Number) File Name (Number)

Subfile Name (Number)

------------------- ---------------------

PATIENT NAME OR BILL NUMBER (.09) AR BATCH PAYMENT (344)

-TRANSACTION (sub-file) (344.01)

Documentation Retrieval:

------------------------

Sites may retrieve documentation in one of the following ways:

1\. The preferred method is to FTP the files from

REDACTED which will transmit the files from the

first available FTP server.

2\. Sites may also elect to retrieve documentation directly from a

specific server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

3\. Documentation can also be retrieved from the VistA Documentation

Library (VDL) on the Internet at the following address,

http://www.va.gov/vdl.

The documentation distribution includes:

FILE NAME DESCRIPTION

---------------------------------------------------------------------

PRCA_4_5_P271_RN.PDF AR Release Notes

Test Sites:

-----------

VA Heartland East - St. Louis

Birmingham

Louisville

Loma Linda

Richmond

Phoenix

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not queue the installation of this patch.

To avoid disruptions, these patches should be installed during non-peak

hours when there is minimal activity on the system. Avoid times when ECME

claims are being transmitted. Of particular concern would be the options

below.

1\. \[BPS NIGHTLY BACKGROUND JOB\]

Do not install the patch when ECME claims are being generated

by the BPS Nightly Background Job option. Wait for this job to

finish or complete the installation before this job starts.

2\. \[PSXR SCHEDULED CS TRANS\] and

\[PSXR SCHEDULED NON-CS TRANS\]

Do not install the patch when prescriptions are being

transmitted to CMOP. Wait for the CMOP transmissions to finish

or complete the installation before the transmissions start. Both

the CS (Controlled Substances) and the non-CS CMOP transmission

options should be checked. Check with Pharmacy Service or your

Pharmacy ADPAC to find out when CMOP transmissions occur.

Install Time

------------

The installation will take between 10 and 90 minutes depending upon how

many entries your site has in the BPS CLAIMS file (9002313.02) and in the

BPS RESPONSES file (9002313.03). Data conversions will be run in both

files and all entries will be checked during the installation of BPS\*1\*10.

1\. OBTAIN PATCHES

--------------

Obtain the host file BPS_1_10_PSO_IB_PRCA.KID, which contains the

following patches:

BPS\*1.0\*10

PSO\*7.0\*359

IB\*2.0\*435

PRCA\*4.5\*271

Sites can retrieve VistA software from the following FTP addresses.

The preferred method is to FTP the files from:

REDACTED

This will transmit the files from the first available FTP server.

Sites may also elect to retrieve software directly from a specific

server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

The BPS_1_10_PSO_IB_PRCA.KID host file is located in the

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

where you saved the host file BPS_1_10_PSO_IB_PRCA.KID (e.g.,

SYS\$SYSDEVICE:\[ANONYMOUS\]BPS_1_10_PSO_IB_PRCA.KID).

When prompted for "OK to continue with Load? NO//", enter "YES."

The following will display:

Loading Distribution...

BPS PSO IB PRCA BUNDLE 6.0

BPS\*1.0\*10

PSO\*7.0\*359

IB\*2.0\*435

PRCA\*4.5\*271

Use INSTALL NAME: BPS PSO IB PRCA BUNDLE 6.0 to install this

Distribution.

4\. RUN OPTIONAL INSTALLATION OPTIONS FOR MULTI-BUILD

-------------------------------------------------

From the Installation menu, you may select to use the following

options (when prompted for the INSTALL NAME, enter

BPS PSO IB PRCA BUNDLE 6.0):

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. INSTALL MULTI-BUILD

-------------------

This is the step to start the installation of this KIDS patch. This

will need to be run for the BPS PSO IB PRCA BUNDLE 6.0.

a\. Choose the Install Package(s) option to start the patch

install.

b\. When prompted for the "Select INSTALL NAME:", enter BPS PSO IB

PRCA BUNDLE 6.0.

c\. For the PRCA\*4.5\*271 patch, when prompted "Want KIDS to Rebuild

Menu Trees Upon Completion of Install? YES//" enter YES unless

your system does this in a nightly TaskMan process.

d\. When prompted "Want KIDS to INHIBIT LOGONs during the

install? YES//" enter NO.

e\. When prompted " Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//" enter NO.

f\. When prompted "Device: Home//" respond with the correct device

but do not queue this install.

Routine Information:

====================

The second line of each of these routines now looks like:

;;4.5;Accounts Receivable;\*\*\[Patch List\]\*\*;Mar 20, 1995;Build 29

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: RCDPBTLM

Before: B46607011 After: B47109458 \*\*114,148,153,168,169,198,247,271\*\*

Routine Name: RCDPESR1

Before: B48522676 After: B50545484 \*\*173,214,208,202,271\*\*

Routine Name: RCDPESR2

Before: B84144020 After: B85277265 \*\*173,216,208,230,252,264,269,271\*\*

Routine Name: RCDPESR4

Before: B76222786 After: B77733360 \*\*173,216,208,230,269,271\*\*

Routine Name: RCDPESR6

Before: B43157350 After: B43409269 \*\*173,214,208,230,252,269,271\*\*

Routine Name: RCDPURED

Before: B35857327 After: B37216500 \*\*114,169,174,196,202,244,268,271\*\*

Routine list of preceding patches: 247, 268, 269

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Change to Maximum Length of ECME Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ECME number has been expanded to be 12 digits in length. This patch makes modifications to AR routines to accommodate a longer ECME number.

## Issue Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch addresses the following New Service Request (NSR):

> -------------------------------------------------

> Request Name: e-Pharmacy Phase 5: FY09

> Request ID: 20080103

### Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no Remedy Tickets associated with this patch.