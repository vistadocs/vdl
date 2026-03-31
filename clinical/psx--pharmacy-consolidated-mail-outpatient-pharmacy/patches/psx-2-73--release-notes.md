---
title: PSX*2*73 Release Notes - ePharmacy Claims Phase 6
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ePharmacy Claims Phase 6
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2*73
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patch
  - installation
  - table
  - contents
  - pharmacy
  - distribution
  - install
  - mail
  - cmop
  - date
page_count: 0
word_count: 1946
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_p73_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_p73_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

![](psx-2-73-release-notes-epharmacy-claims-phase-6/001.png)

ePharmacy

PHASE VIConsolidated Mail Outpatient Pharmacy (PSX)

Release Notes

PSX\*2\*73

February 2012

Office of Enterprise Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Documentation Distribution](#documentation-distribution)
- [Consolidated Mail Outpatient Pharmacy V. 2.0 - PSX\2\73](#consolidated-mail-outpatient-pharmacy-v-20-psx273)
  - [Patch Description](#patch-description)
  - [Installation Instructions](#installation-instructions)
- [Enhancements](#enhancements)
- [Issue Resolutions](#issue-resolutions)
  - [New Service Request (NSR)](#new-service-request-nsr)
  - [Remedy Tickets](#remedy-tickets)
This patch has enhancements that extend the capabilities of the Veterans Health Information Systems and Technology Architecture (VistA) electronic pharmacy (ePharmacy) billing system. Below is a list of all the applications involved in this project along with their patch number:
<u>APPLICATION/VERSION PATCH</u>
Outpatient Pharmacy (OP) V. 7.0 PSO\*7\*385
Integrated Billing (IB) V. 2.0 IB\*2\*452
Electronic Claims Management Engine (ECME) V. 1.0 BPS\*1\*11
Consolidated Mail Outpatient Pharmacy (CMOP) V. 2.0 PSX\*2\*73
The following associated patch must be installed before proceeding:
- \(v\) PSX\*2\*69 \<\<= must be installed BEFORE ‘PSX\*2\*73’.
The patches (PSO\*7\*385, IB\*2\*452, BPS\*1\*11, and PSX\*2\*73) are being released in the Kernel Installation and Distribution System (KIDS) multi-build distribution BPS PSO IB PSX BUNDLE 7.0.
The purpose of this software package is to maintain compliance with legislative and federal mandates and to address and correct gaps and inefficiencies in the current electronic pharmacy billing processes. This
will ultimately increase revenues collected by VA Medical Centers and outpatient pharmacies by reducing the volume of short pays and payment denials.
All pharmacy claims for payers that are processed electronically are compliant with the current industry standards. This software adds support for the electronic billing of the Health Administration Center (HAC) CHAMPVA payer in order to provide an automated process and to prevent manual workarounds for CHAMPVA.

## Documentation Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation distribution includes:

 

    FILE NAME                         DESCRIPTION

    ---------------------------------------------------------------------

PSX_2_P73_RN.PDF CMOP Patch Release Notes

*(This page included for two-sided copying.)*

# Consolidated Mail Outpatient Pharmacy V. 2.0 - PSX\*2\*73

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Patch Display Page: 1

=============================================================================

Run Date: JAN 19, 2012 Designation: PSX\*2\*73

Package : CMOP Priority : MANDATORY

Version : 2 Status : RELEASED

=============================================================================

Associated patches: (v)PSX\*2\*69 \<\<= must be installed BEFORE \`PSX\*2\*73'

Subject: EPHARMACY PHASE 6

Category: ENHANCEMENT

ROUTINE

Description:

===========

This patch has enhancements that extend the capabilities of the Veterans

Health Information Systems and Technology Architecture (VistA) electronic

pharmacy (ePharmacy) billing system. Below is a list of all the

applications involved in this project along with their patch number:

APPLICATION/VERSION PATCH

---------------------------------------------------------------

OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*385

INTEGRATED BILLING (IB) V. 2.0 IB\*2\*452

ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*11

CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP) V. 2.0 PSX\*2\*73

The patches (PSO\*7\*385, IB\*2\*452, BPS\*1\*11, and PSX\*2\*73) are being released

in the Kernel Installation and Distribution System (KIDS) multi-build

distribution BPS PSO IB PSX BUNDLE 7.0.

The purpose of this software package is to maintain compliance with

legislative and federal mandates and to address and correct gaps and

inefficiencies in the current electronic pharmacy billing processes. This

will ultimately increase revenues collected by VA Medical Centers and

outpatient pharmacies by reducing the volume of short pays and payment

denials.

All pharmacy claims for payers that are processed electronically are

compliant with the current industry standards. This software adds support

for the electronic billing of the Health Administration Center (HAC) CHAMPVA

payer in order to provide an automated process and to prevent manual

workarounds for CHAMPVA.

This specific patch contains the following functionality:

---------------------------------------------------------

1\. The ECME# label and data have been removed from the CMOP/ECME Activity

Report \[BPS RPT CMOP/ECME ACTIVITY\] and also from the Excel output.

2\. The background process that calculates suspense days will now round

any partial day to the next full day.

3\. The ePharmacy Date of Service Calculation no longer considers the Fill

Date as an acceptable value. The algorithm uses the release date if it

exists. If the release date does not exist, the algorithm uses the

current date.

Patch Components

================

Files & Fields Associated:

File Name (Number) Field Name (Number) New/Modified/Deleted

------------------ ------------------- --------------------

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

Additional Information:

New Service Requests (NSRs)

----------------------------

Request Name: ePharmacy Claims Phase 6 (FY10)

Request ID: 20090215

Patient Safety Issues (PSIs)

-----------------------------

N/A

Remedy Ticket(s) & Overview

---------------------------

N/A

Test Sites:

----------

Birmingham

Loma Linda

Phoenix

Richmond

Documentation Retrieval Instructions

------------------------------------

Updated documentation describing the new functionality introduced by this

patch is available.

The preferred method is to FTP the files from

<span class="mark">REDACTED</span>. This transmits the files from the first

available FTP server. Sites may also elect to retrieve software directly from

a specific server as follows:

<span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl/

Title File Name FTP Mode

-----------------------------------------------------------------------

CMOP Patch Release Notes PSX_2_P73_RN.PDF Binary

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should take up to 20 minutes to install.

DO NOT QUEUE the installation of this patch.

To avoid disruptions, these patches should be installed during non-peak

hours when there is minimal activity on the system. Avoid times when ECME

claims are being transmitted. Of particular concern would be the options

below.

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

\*\*\*\*\* IMPORTANT INSTALLATION NOTES \*\*\*\*\*

This patch bundle is changing the name of File \#52.87. The current name of

this file is 'PSO TRICARE AUDIT LOG'. The new name of this file is 'PSO AUDIT

LOG'. During the patch installation you will see the following information

presented to the screen:

52.87 PSO AUDIT LOG

\*BUT YOU ALREADY HAVE 'PSO TRICARE AUDIT LOG' AS FILE \#52.87!

Shall I write over your PSO TRICARE AUDIT LOG File? YES//

Please accept the default answer of YES to this question.

You will also be prompted to enter the coordinator for the new BPS CHAMPVA

mail group. Prior to installation, please contact your Medical Care Cost

Recovery (MCCR) business department (Facility Revenue Manager) to

determine who will be the coordinator for this new mail group. The users

in this mail group will receive bulletins related to the processing of

CHAMPVA electronic claims. After the patch is installed, members can be

added to the mail group by using the Mail Group Edit \[XMEDITMG\] option.

Pre-Installation Instructions

-----------------------------

1\. OBTAIN PATCHES

--------------

Obtain the host file BPS_1_11_PSO_IB_PSX.KID, which contains the

following patches:

BPS\*1.0\*11

PSO\*7.0\*385

IB\*2.0\*452

PSX\*2.0\*73

Sites can retrieve VistA software from the following FTP addresses.

The preferred method is to FTP the files from:

download.vista.med.va.gov

This will transmit the files from the first available FTP server.

Sites may also elect to retrieve software directly from a specific

server as follows:

<span class="mark">REDACTED</span>

The BPS_1_11_PSO_IB_PSX.KID host file is located in the

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

where you saved the host file BPS_1_11_PSO_IB_PSX.KID (e.g.,

SYS\$SYSDEVICE:\[ANONYMOUS\]BPS_1_11_PSO_IB_PSX.KID).

When prompted for "OK to continue with Load? NO//", enter "YES."

The following will display:

Loading Distribution...

BPS PSO IB PSX BUNDLE 7.0

BPS\*1.0\*11

PSO\*7.0\*385

IB\*2.0\*452

PSX\*2.0\*73

Use INSTALL NAME: BPS PSO IB PSX BUNDLE 7.0 to install this

Distribution.

4\. RUN OPTIONAL INSTALLATION OPTIONS FOR MULTI-BUILD

-------------------------------------------------

From the Installation menu, you may select to use the following

options (when prompted for the INSTALL NAME, enter

BPS PSO IB PSX BUNDLE 7.0):

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

will need to be run for the BPS PSO IB PSX BUNDLE 7.0.

a\. Choose the Install Package(s) option to start the patch

install.

b\. When prompted for the "Select INSTALL NAME:", enter BPS PSO IB

PSX BUNDLE 7.0.

c\. When prompted to "Enter the Coordinator for Mail Group 'BPS

CHAMPVA':", please respond with the appropriate person.

d\. When prompted "Shall I write over your PSO TRICARE AUDIT LOG File?

YES//", please accept the default of YES in order to change the name

of this file as instructed above.

e\. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of

Install? YES//", enter YES unless your system does this in a nightly

TaskMan process.

f\. When prompted "Want KIDS to INHIBIT LOGONs during the install?

YES//", enter NO.

g\. When prompted " Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//", enter NO.

h\. When prompted "Device: HOME//", respond with the correct device

but do not queue this install.

Post-Installation Instructions

------------------------------

N/A

Routine Information:

====================

The second line of each of these routines now looks like:

;;2.0;CMOP;\*\*\[Patch List\]\*\*;11 Apr 97;Build 24

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: PSXBPSRP

Before: B78524997 After: B77595338 \*\*63,65,73\*\*

Routine Name: PSXRPPL1

Before: B52590597 After: B51826224 \*\*3,48,62,66,65,69,73\*\*

Routine Name: PSXRPPL2

Before: B55484855 After: B55199697 \*\*65,69,73\*\*

Routine list of preceding patches: 69

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSX\*2\*73 includes the following enhancements:

- The ECME# label and data have been removed from the CMOP/ECME Activity Report \[BPS RPT CMOP/ECME ACTIVITY\] and also from the Excel output.
- The background process that calculates suspense days will now round any partial day to the next full day.
- The ePharmacy Date of Service Calculation no longer considers the Fill Date as an acceptable value. The algorithm uses the release date if it exists. If the release date does not exist, the algorithm uses the current date.

# Issue Resolutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Service Request (NSR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch addresses the following New Service Request (NSR):

> -------------------------------------------------

> Request Name: ePharmacy Claims Phase 6 (FY10)

> Request ID: 20090215

## Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no Remedy Tickets associated with this patch.