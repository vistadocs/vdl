---
title: IB*2*431 ePayments Release Notes and Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: ePayments Release Notes and
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*431
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - installation
  - table
  - contents
  - install
  - patch
  - prca
  - distribution
  - epayments
  - patches
  - redacted
page_count: 0
word_count: 1424
section_count: 6
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2011
revision_count: 1
revision_newest: 08/01/2011
revision_oldest: 08/01/2011
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p431_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_p431_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

Integrated Billing

ePayments

![](ib-2-431-epayments-release-notes-and-installation-guide/001.png)

Release Notes and Installation Guide

IB\*2.0\*431

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
- [Overview](#overview)
  - [Patch IB\2.0\431 includes the following modifications](#patch-ib20431-includes-the-following-modifications)
  - [Documentation Retrieval](#documentation-retrieval)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Pre-Installation Considerations](#pre-installation-considerations)
  - [Installation Instructions](#installation-instructions)
    - [Post-Installation Instructions](#post-installation-instructions)
- [Support Information](#support-information)
The Chief Business Office (CBO) requested enhancements to the Veterans Health Administration (VHA)'s Veterans Health Integrated Systems Technology Architecture (VistA) Third Party Electronic Data Interchange (EDI) Lockbox module ePayments Enhancement project to increase timely and accurate processing of payments in compliance with Healthcare Insurance Portability and Accountability Act (HIPAA) and VHA fiscal accounting policies.
Currently to fulfill the Accounts Receivable functions, Veterans Administration Medical Center (VAMC) staff is performing manual workarounds to address limitations of the existing software tools. Addressing ePayments software issues will enable compliance with HIPAA security and administrative regulations as well as VHA Fiscal Accounting policy.
Additional system modifications are included which will enable automation of the labor intensive workarounds and minimize costly system errors.

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is part of the HIPAA 5010 ePayments project. The project has two patches (PRCA\*4.5\*269 and IB\*2.0\*431) which are being released in the Kernel Installation and Distribution System (KIDS) multi build distribution EPAYMENTS 5010.KID.

APPLICATION/VERSION PATCH INSTALL_ORDER

ACCOUNTS RECEIVABLE (PRCA) V. 4.5 PRCA\*4.5\*269 1

INTEGRATED BILLING (IB) V. 2.0 IB\*2.0\*431 2

Changes made to the INTEGRATED BILLING application are described below. See PRCA\*4.5\*269 for changes made to ACCOUNTS RECEIVABLE application and installation instructions.

## Patch IB\*2.0\*431 includes the following modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifications are made to allow VistA to receive, process and display ERA/EEOB and MRA EOB data from FSC in HIPAA 5010 compatible format.

Backward compatibility is supported to allow VistA to also receive messages in the existing HIPAA 4010 format.

The data content of EEOB messages is modified to meet HIPAA 5010 standard.

Existing EOB Trace \#, ICN and Contact Number fields are extended in length and new fields are added for:

Claim Received Date

Coverage Expiration Date

Corrected Priority Payer Name and ID

Other Subscriber Name

Adjustment/Payer Policy Reference

The expanded fields in the 835 messages are also stored in VistA and this requires a reorganization of the database. . The Crossed Over Name field is unchanged but is moved to new locations in the VistA database to make space for the extended fields:

This data reorganization is performed as part of the post install routine for this patch.

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may retrieve documentation in one of the following ways:

 

 1.  The preferred method is to FTP the files from REDACTED which will transmit the files from the first available FTP server.
 2.  Sites may also elect to retrieve documentation directly from a specific server as follows:

 

     Albany          REDACTED

     Hines           REDACTED

     Salt Lake City  REDACTED
 3.  Documentation can also be retrieved from the VistA Documentation Library (VDL) on the Internet at the following addresses, <http://www.va.gov/vdl/application.asp?appid=29> and <http://www.va.gov/vdl/application.asp?appid=45>

 

The documentation distribution includes:

| FILE NAME                        | DESCRIPTION       |
|--------------------------------------|-----------------------|
| IB_2_P431_RN.PDF                     | Release Notes         |
| PRCA_4_5_P269\_ RN.PDF               | Release Notes         |
| EPAYMENTS_USER_GUIDE_EDI_LOCKBOX.PDF | ePayments User Manual |

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch will be released to the field as a combined host file with patch PRCA\*4.5\*269.

 

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before IB\*2.0\*431

> IB\*2.0\*400

> IB\*2.0\*407

> IB\*2.0\*417

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

\[Cesar: we are loading a host file that contains two patches and no stand-alone patch has been installed yet. The user has no way of altering the installation order because it has already been pre-defined in the host file.\]

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
<p>Then sends install notification to CBO mail group REDACTED</p>
<p>(On receiving this message CBO notifies FSC that the VistA site has installed and is ready to receive 5010 format messages)</p></td>
</tr>
</tbody>
</table>

# Support Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing, these patches will be supported by the Office of Enterprise Development, the development team. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any issues that arrive related to these patches. At the end of this 30 day period, assistance with issues related to these patches will be addressed through the Help Desk and the submittal of Remedy tickets if needed.