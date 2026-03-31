---
title: IB*2*451 ePayments II Release Notes/Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: ePayments II Release Notes/
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*451
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - changes
  - installation
  - party
  - third
  - options
  - patch
  - joint
  - inquiry
page_count: 0
word_count: 1305
section_count: 10
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_0_p451_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_0_p451_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

ePayments II

Release Notes and Installation Guide

IB\*2\*451

![](ib-2-451-epayments-ii-release-notes-installation-guide/001.png)

January 2012

Veterans Affairs

Product Development (PD)

*(This page included for two-sided copying.)*

Revision History

| Date         | Version | Description | Project Manager | Technical Writer |
|--------------|---------|-------------|-----------------|------------------|
| January 2012 | 1.0     | Initial     | REDACTED        | REDACTED         |

*(This page included for two-sided copying.)*

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Hardware Compatibility](#hardware-compatibility)
  - [System Specifications](#system-specifications)
- [Installation and Configuration](#installation-and-configuration)
  - [Pre-Installation Considerations](#pre-installation-considerations)
  - [Installation Procedure](#installation-procedure)
  - [Documentation Retrieval](#documentation-retrieval)
- [Release Changes and Enhancements](#release-changes-and-enhancements)
  - [Changes on Third Party Joint Inquiry (TPJI)](#changes-on-third-party-joint-inquiry-tpji)
  - [Changes on the EDI Lockbox Menu](#changes-on-the-edi-lockbox-menu)
  - [Changes on Bill Charges Screen of TPJI](#changes-on-bill-charges-screen-of-tpji)
  - [Changes on Individual Report Options](#changes-on-individual-report-options)
- [Support Information](#support-information)
The Chief Business Office (CBO) in the Veterans Health Administration (VHA), requested enhancements to the Integrated Billing system software in order to augment payment processing efficiencies at individual VA medical center accounts. The changes distributed with this patch affect reporting options used daily in the delivery of benefits and services provided to the patient population.
Improvements to management reporting and additional automation of business process will support VHA performance measures and compliance policies to ensure fiscal accuracy and accountability.
The project has two patches (IB\*2.0\*451 and PRCA\*4.5\*276) which are being released in the Kernel Installation and Distribution System (KIDS) using single build distributions. These patches affect the Accounts Receivable (AR) and Integrated Billing (IB) applications
> **NOTE:** Patch IB\*2.0\*451 must be installed BEFORE PRCA\*4.5\*276.

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special hardware considerations.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special system considerations.

# Installation and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Installation Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Associated patches that must be installed BEFORE IB\*2\*451

IB\*2\*133 IB\*2\*227 IB\*2\*356

IB\*2\*384 IB\*2\*431 IB\*2\*433

> **NOTE:** Patch IB\*2.0\*451 must be installed BEFORE PRCA\*4.5\*276.

APPLICATION/VERSION PATCH INSTALL ORDER

INTEGRATED BILLING (IB) V. 2.0 IB\*2.0\*451 1

ACCOUNTS RECEIVABLE (PRCA) V. 4.5 PRCA\*4.5\*276 2

Integrated Billing users should not be on the system while this patch is being installed. This patch should take less than 5 minutes to install.

Make sure all Integrated Billing users are logged off the system and disable the following menu options:

> First Party Follow-Up Report \[IBJD FOLLOW-UP FIRST PARTY\]

> List All Bills For a Patient \[IB LIST ALL BILLS FOR PAT\]

> Insurance Payment Trend Report \[IB OUTPUT TREND REPORT\]

> Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]

## Installation Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc311758133" class="anchor"></span>

1.  Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following option. When prompted for the INSTALL enter the patch \#

PRCA\*4.5\*276:

a\. Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

4\. From the Installation Menu, select the Install Package(s) option and choose the patch to install.

5\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' answer NO if this is done as a nightly job

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// answer YES

8\. Enter options you wish to mark as 'Out Of Order':

> First Party Follow-Up Report \[IBJD FOLLOW-UP FIRST PARTY\]

> List All Bills For a Patient \[IB LIST ALL BILLS FOR PAT\]

> Insurance Payment Trend Report \[IB OUTPUT TREND REPORT\]

> Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]

9\. Enter protocols you wish to mark as 'Out Of Order': press RETURN

10\. Delay Install (Minutes): (0-60): 0//

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may retrieve documentation in one of the following ways:

1.  The preferred method is to FTP the files from REDACTED which will transmit the files from the first available FTP server.
2.  Sites may also elect to retrieve documentation directly from a specific server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

 

3.  Documentation can also be retrieved from the VistA Documentation Library (VDL) on the Internet at the following address:

<http://www.va.gov/vdl>.

The documentation distribution includes:

<u>TITLE</u> <u>FILE NAME</u>

ePayments User Guide (EDI Lockbox) EPAYMENTS_USER_GUIDE_EDI_LOCKBOX_R0112.PDF

IB ePayments II Release Notes/Installation Guide (IB\*2.0\*451) IB_2_0_P451_RN.PDF

IB Technical Manual/Security Guide (IB\*2.0\*451) IB_2_0_TM_R0112.PDF

> **NOTE:** Use ASCII mode when transferring the .KID file.

> Use Binary mode when transferring the .PDF file.  The .PDF files can be read on a PC using the Adobe Acrobat Reader program. The VistA Documentation Library \[VDL\] contains all end-user manuals.

# Release Changes and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes made to the INTEGRATED BILLING application and installation steps are described below. See PRCA\*4.5\*276 for changes made to the ACCOUNTS RECEIVABLE application.

## Changes on Third Party Joint Inquiry (TPJI)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Integrated Billing application has been enhanced to display the Trace Number and ERA (Electronic Remittance Advice) Number on the TPJI screen when viewing the Electronic Explanation of Benefits (EEOB). This change is applicable to the option Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\].

## Changes on the EDI Lockbox Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new option EEOB Move/Copy \[RCDPE EEOB MOVE/COPY\], which is part of the EDI (Electronic Data Interchange) Lockbox menu \[RCDPE EDI LOCKBOX MENU\], provides new functionality to enable the user to move an EEOB to another claim, and to copy an EEOB and clone it to several claims. The routine IBCEOB4 is being released to support this new functionality in Accounts Receivable.

## Changes on Bill Charges Screen of TPJI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The screen Bill Charges found in the option Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\] which is shared with Accounts Receivable has been enhanced to display the following new fields from the Explanation of Benefits (EOB) file (#361.1) as a result of a move or copy of a claim:

DATE/TIME EOB MOVED

EOB MOVE/COPY BY

MOVE/COPY REASON

ORIGINAL BILL NUMBER

OTHER CLAIM NUMBERS (multiple)

Additionally, the Accounts Receivable and Integrated Billing systems have been enhanced to display the details of the Move or Copy transaction within the following screen options:

Bill Charges screen of TPJI

Comment History screen of TPJI

View/Print EEOB screen of the EEOB Worklist

View/Print ERA screen of the EEOB Worklist

## Changes on Individual Report Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifications are made to Integrated Billing report options that will show the character '%' next to the bill number to indicate that there is a payment in the Explanation of Benefits file (#361.1). The following report options are modified by this patch:

First Party Follow-Up Report \[IBJD FOLLOW-UP FIRST PARTY\]

List All Bills For a Patient \[IB LIST ALL BILLS FOR PAT\]

Insurance Payment Trend Report \[IB OUTPUT TREND REPORT\]

Bill Charges \[IBJ THIRD PARTY JOINT INQUIRY\]

Third Party Active Bills \[IBJ THIRD PARTY JOINT INQUIRY\]

Third Party Inactive Bills \[IBJ THIRD PARTY JOINT INQUIRY\]

Third Party Follow-Up Report \[IBJD FOLLOW-UP THIRD PARTY\]

# Support Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing, these patches will be supported by the Office of Enterprise Development, the development team. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any issues that arrive related to these patches. At the end of this 30 day period, assistance with issues related to these patches will be addressed through the Help Desk and the submittal of Remedy tickets if needed.