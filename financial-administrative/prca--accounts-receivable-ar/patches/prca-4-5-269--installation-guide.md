---
title: PRCA*4.5*269 AR ePayments Release Notes and Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: AR ePayments Release Notes and
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5*269
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - prca
  - install
  - patch
  - changes
  - distribution
  - vista
  - patches
page_count: 0
word_count: 1636
section_count: 8
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2011
revision_count: 1
revision_newest: 08/01/2011
revision_oldest: 08/01/2011
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p269_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p269_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

Account Receivable

ePayments

![](prca-4-5-269-ar-epayments-release-notes-and-installation-guide/001.png)

Release Notes and Installation Guide

PRCA\*4.5\*269

August 2011

Veterans Affairs

Product Development (PD)

*(This page included for two-sided copying.)*

Revision History

| Date       | Version | Description | Author   |
|------------|---------|-------------|----------|
| 08/01/2011 | 1.0     | Initial     | REDACTED |
|            |         |             |          |

*(This page included for two-sided copying.)*

######## Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Hardware Compatibility](#hardware-compatibility)
  - [System Specifications](#system-specifications)
- [Overview](#overview)
  - [Modifications included with Patch PRCA\4.5\269](#modifications-included-with-patch-prca45269)
    - [HIPAA 5010 changes](#hipaa-5010-changes)
    - [Other Changes](#other-changes)
  - [Documentation Retrieval](#documentation-retrieval)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Pre-Installation Considerations](#pre-installation-considerations)
  - [Installation Instructions](#installation-instructions)
    - [Post-Installation Instructions](#post-installation-instructions)
- [Support Information](#support-information)
The Chief Business Office (CBO) requested enhancements to the Veterans Health Administration (VHA)'s Veterans Health Integrated Systems Technology Architecture (VistA) Third Party Electronic Data Interchange (EDI) Lockbox module ePayments Enhancement project to increase timely and accurate processing of payments in compliance with Healthcare Insurance Portability and Accountability Act (HIPAA) and VHA fiscal accounting policies.
Currently to fulfill the Accounts Receivable functions, Veterans Administration Medical Center (VAMC) staff is performing manual workarounds to address limitations of the existing software tools. Addressing ePayments software issues will enable compliance with HIPAA security and administrative regulations as well as VHA Fiscal Accounting policy.

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special hardware considerations.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special system considerations.

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The project has two patches (PRCA\*4.5\*269 and IB\*2\*431) which are being released in the Kernel Installation and Distribution System (KIDS) multi build distribution EPAYMENTS 5010.KID.

APPLICATION/VERSION PATCH INSTALL_ORDER

ACCOUNTS RECEIVABLE (PRCA) V. 4.5 PRCA\*4.5\*269 1

INTEGRATED BILLING (IB) V. 2.0 IB\*2.0\*431 2

Changes made to the ACCOUNTS RECEIVABLE application and installation steps are described below. See IB\*2.0\*431 for changes made to INTEGRATED BILLING application.

## Modifications included with Patch PRCA\*4.5\*269 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HIPAA 5010 changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifications are made to the EDI Lockbox menu to allow VistA to receive process and display ERA, EFT and EEOB data from FSC in HIPAA 5010 compatible format. Backward compatibility is supported to allow VistA to also receive messages in the existing HIPAA 4010 format.

The data content of ERA, EFT and EOB messages is modified to meet HIPAA 5010 standard. Existing EFT/ERA Payer Name, Trace \#, Contact Numbers, Rendering Provider and Adjustment Reference fields are extended in length and a new ERA field 'Payer Web Site Address' is also introduced.

These expanded fields in the 835 messages are also stored in VistA and this requires a reorganization of the database. . The following fields are unchanged but have been moved to new locations in the VistA database to make space for the extended fields:

ERA - Check \#, Rendering Provider Comment and Adjustment Text fields

EFT - ACH Trace \# and Manual TR Document fields

This data reorganization is performed as part of the post install routine for this patch.

### Other Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional system modifications (outside of HIPAA 5010) are included which will enable automation of the labor intensive workarounds and minimize costly system errors.

1)  The PRCA NIGHTLY PROCESS batch job auto matches EFT and ERA transactions and updates receipts for the AR package. This process includes a purge of receipts which is extended by this release from one year's retention to seven years.
2)  The process for receiving EFT messages is modified to verify on date as well as ticket number. This allows 469 and 569 3rd Party ticket number ranges to be reused without being treated as duplicates.
3)  ERA numbers are no longer truncated in Worklist but are now displayed as the full 10 digits.
4)  'Patient Charge Maintenance' option in the Worklist/Research Menu is replaced by the 'Administrative Charge Adjustment' option.
5)  Within TPJI (menu option \[IBJ THIRD PARTY JOINT INQUIRY\]) the Comment History sub option is modified to display contact details (including the new Payer Web Site field).

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may retrieve documentation in one of the following ways:

 

 1.  The preferred method is to FTP the files from REDACTED, which will transmit the files from the first available FTP server.
 2.  Sites may also elect to retrieve documentation directly from a specific server as follows:

 

     Albany          REDACTED

     Hines           [REDACTED](ftp://ftp.fo-hines.med.va.gov)

     Salt Lake City  [REDACTED](ftp://ftp.fo-slc.med.va.gov)
 3.  Documentation can also be retrieved from the VistA Documentation Library (VDL) on the Internet at the following address, <http://www.va.gov/vdl/application.asp?appid=29> and <http://www.va.gov/vdl/application.asp?appid=45>

 

The documentation distribution includes:

| FILE NAME ON ANONYMOUS DRIVE     | DESCRIPTION       |
|--------------------------------------|-----------------------|
| IB_2_P431_RN.PDF                     | Release Notes         |
| PRCA_4_5_P269\_ RN.PDF               | Release Notes         |
| EPAYMENTS_USER_GUIDE_EDI_LOCKBOX.PDF | ePayments User Manual |

# Installation 

 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch will be released to the field as a combined host file with patch IB\*2.0\*431.

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before PRCA\*4.5\*269

> PRCA\*4.5\*169

> PRCA\*4.5\*222

> PRCA\*4.5\*244

> PRCA\*4.5\*252

> PRCA\*4.5\*255

> PRCA\*4.5\*258

> PRCA\*4.5\*264

> XU\*8\*539

## Pre-Installation Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

THIS PATCH MUST BE LOADED AFTER NORMAL WORKING HOURS. Extensive changes are made to Accounts Receivable so it should not be in use during the install.

The install should take approximately 10 minutes.

Make sure all Accounts Receivable users are logged off the system and deactivate the following menu options:

Clerk's AR Menu \[PRCA CLERK MENU\] option

Supervisor's AR Menu \[PRCAF SUPERVISOR MENU\] option

EDI Lockbox \[RCDPE EDI LOCKBOX MENU\] option

MRA Management \[IBCE MRA MANAGEMENT\] option

Return Message Filing Exceptions \[IBCE RETURN MSG PROCESSING\] option

Be sure that the following background task is not running when you install this patch:

Accounts Receivable Nightly Process Background Job \[PRCA NIGHTLY PROCESS\]

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. OBTAIN PATCHES

Obtain the host file EPAYMENTS_5010.KID, which contains the following two patch installs:

PRCA\*4.5\*269

IB\*2.0\*431

Sites can retrieve VistA software from the following FTP addresses. The preferred method is to FTP the files from: REDACTED

This will transmit the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

The EPAYMENTS_5010.KID host file is located in the anonymous.software directory. Use ASCII Mode when downloading the file.

2\. START UP KIDS

Start up the Kernel Installation and Distribution System Menu option

\[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INStallation

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

From the Installation menu, select the Load a Distribution option.

When prompted for "Enter a Host File:", enter the full directory path where you saved the host file EPAYMENTS_5010.KID (e.g., SYS\$SYSDEVICE:\[ANONYMOUS\]EPAYMENTS_5010.KID).

When prompted for "OK to continue with Load? NO//", enter "YES."

The following will display:

Loading Distribution...

PRCA IB BUNDLE 1.0

PRCA\*4.5\*269

IB\*2.0\*431

Use INSTALL NAME: PRCA IB BUNDLE 1.0 to install this Distribution.

4\. RUN OPTIONAL INSTALLATION OPTIONS FOR MULTI-BUILD

From the Installation menu, you may select to use the following options:

(When prompted for the INSTALL NAME, enter PRCA IB BUNDLE 1.0)

1)  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2)  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3)  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

5\. INSTALL MULTI-BUILD

This is the step to start the installation of this KIDS patches.

1)  Choose the Install Package(s) option to start the patch install.
2)  When prompted for the "Select INSTALL NAME:", enter PRCA IB BUNDLE 1.0
3)  When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond NO.
4)  When prompted to DISABLE Scheduled Options, Menu Options, and Protocols YES//', respond NO.

### Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enable the options disabled at the beginning of the INSTALLATION INSTRUCTIONS.

The Post-Install routines are not deleted after the patches are installed.

Post-Install routines

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Patch</strong></th>
<th><strong>Routine</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IB*2.0*431 </td>
<td>^IBP431</td>
<td>Moves fields in EOB file (#361.1) and sends completion mail message to installer.</td>
</tr>
<tr class="even">
<td>PRCA*4.5*269  </td>
<td>^PRCAP269</td>
<td><p>Moves fields in EFT file (#344.3) and ERA file (#344.4) and sends message to installer</p>
<p>Then sends install notification to CBO mail group <a href="mailto:G.VHACBOEPAY5010@VA.GOV">REDACTED</a></p>
<p>(On receiving this message CBO notifies FSC that the VistA site has installed and is ready to receive 5010 format messages)</p></td>
</tr>
</tbody>
</table>

# Support Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing, these patches will be supported by the Office of Enterprise Development, the development team. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any issues that arrive related to these patches. At the end of this 30 day period, assistance with issues related to these patches will be addressed through the Help Desk and the submittal of Remedy tickets if needed.