---
title: PRCA*4.5*276 AR ePayments II Release Notes/Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: AR ePayments II Release Notes/
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5*276
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - report
  - rcdpe
  - prca
  - eeob
  - installation
  - profile
  - lockbox
  - audit
page_count: 0
word_count: 2610
section_count: 16
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p276_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p276_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

ePayments II

PRCA\*4.5\*276

Release Notes and Installation Guide

![](prca-4-5-276-ar-epayments-ii-release-notes-installation-guide/001.png)

January 2012

Veterans Affairs

Product Development (PD)

*(This page included for two-sided copying.)*

Revision History

| Date         | Version | Description | Project Manager | Technical Writer |
|--------------|---------|-------------|-----------------|------------------|
| January 2012 | 1.0     | Initial     | Sookie Spence   | Berry Anderson   |
|              |         |             |                 |                  |

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
  - [## Pre-Installation Considerations](#pre-installation-considerations)
  - [Installation Procedure](#installation-procedure)
  - [Post-Installation Instructions](#post-installation-instructions)
  - [Documentation Retrieval](#documentation-retrieval)
- [Release Changes and Enhancements](#release-changes-and-enhancements)
  - [Workload Notification](#workload-notification)
  - [Linking an ERA to a Receipt](#linking-an-era-to-a-receipt)
  - [EEOB Move/Copy](#eeob-movecopy)
  - [EFT Work List](#eft-work-list)
  - [Mark ERA Returned to Payer](#mark-era-returned-to-payer)
  - [EEOB Worklist](#eeob-worklist)
  - [EDI Lockbox Report](#edi-lockbox-report)
  - [EEOB Indicator](#eeob-indicator)
  - [Negative Claim Balance](#negative-claim-balance)
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

## ## Pre-Installation Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Associated patches that must be installed before installing PRCA\*4.5\*276

PRCA\*4.5\*151 PRCA\*4.5\*218 PRCA\*4.5\*220 PRCA\*4.5\*221

PRCA\*4.5\*222 PRCA\*4.5\*226 PRCA\*4.5\*233 PRCA\*4.5\*241

PRCA\*4.5\*247 PRCA\*4.5\*269 PRCA\*4.5\*270 PRCA\*4.5\*271

IB\*2\*451

> **NOTE:** Patch IB\*2.0\*451 must be installed BEFORE PRCA\*4.5\*276.

APPLICATION/VERSION PATCH INSTALL ORDER

INTEGRATED BILLING (IB) V. 2.0 IB\*2.0\*451 1

ACCOUNTS RECEIVABLE (PRCA) V. 4.5 PRCA\*4.5\*276 2

Accounts Receivable users should not be on the system while this patch is being installed. This patch should take less than 5 minutes to install.

Make sure that all Accounts Receivable users are logged off the system before installing this patch.

The following options should be disabled:

EDI Lockbox \[RCDPE EDI LOCKBOX MENU\]

Brief Account Profile \[PRCAY ACCOUNT PROFILE\]

Full Account Profile \[PRCAY FULL ACCOUNT PROFILE\]

List All Bills \[PRCA LIST ALL BILLS\]

Claims Matching Report \[RCDP CLAIMS MATCH\]

Bill Profile \[RCDP BILL PROFILE\]

Bill Transactions \[RCDP BILL TRANSACTIONS\]

Receipt Processing RCDP RECEIPT PROCESSING\]

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

EDI Lockbox \[RCDPE EDI LOCKBOX MENU\]

Brief Account Profile \[PRCAY ACCOUNT PROFILE\]

Full Account Profile \[PRCAY FULL ACCOUNT PROFILE\]

List All Bills \[PRCA LIST ALL BILLS\]

Claims Matching Report \[RCDP CLAIMS MATCH\]

Bill Profile \[RCDP BILL PROFILE\]

Bill Transactions \[RCDP BILL TRANSACTIONS\]

Receipt Processing \[RCDP RECEIPT PROCESSING\]

9\. Enter protocols you wish to mark as 'Out Of Order': press RETURN

10\. Delay Install (Minutes): (0-60): 0//

## Post-Installation Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pre-install routine PRCAP276 is automatically removed by KIDS at the end of the installation.

The coordinator for the new mail group RCDPE AUDIT should be one of the ePayments staff.

ePayments users who will need access to the Remove Duplicate EFT Deposit option will need to be assigned the \[RCDPE REMOVE DULICATES\] security key. The ePayments supervisory staff can provide the proper group of users.

Users who will need access to the Mark ERA Returned To Payer option will need to be assigned the \[RCDPE MARK ERA\] security key. The ePayments supervisory staff can provide the proper group of users.

Assign the proper ePayments users to the RCDPE AUDIT mail group. This is the mail group that will receive the ERA and EFT bulletins. The list of proper users can be obtained from the ePayments supervisory staff.

The new option \[RCDPE WORKLOAD NOTIFICATION\] which generates the new bulletins should be scheduled in Task Manager to run weekly, biweekly, or monthly as required. Scheduling frequency should be based on the number of outstanding ERA and EFT workload and will need to be coordinated with the ePayments staff.

Production only: The following email address must be defined to the REMOTE MEMBER attribute of the RCDPE AUDIT mail group: REDACTED

The correct configuration for the RCDPE AUDIT Mail Group is:

NAME: RCDPE AUDIT                       TYPE: public

  ALLOW SELF ENROLLMENT?: NO           REFERENCE COUNT: 62

  LAST REFERENCED: SEP 15, 2011         RESTRICTIONS: UNRESTRICTED

MEMBER: xxxxx,xxxxxxx

DESCRIPTION:   This is the mail group that will receive warning bulletins produced by the ePayments Workload Notification process. Warnings for overdue EFT and ERA are sent to this group. 

  ORGANIZER: POSTMASTER

REMOTE MEMBER: REDACTED

  The Q-NPS.VA.GOV domain must exist and the field 'FLAGS' must be defined with a value of 'S'.  Example shown below. 

 

Select DOMAIN NAME: Q-NPS.VA.GOV 

NUMBER: 579                             NAME: Q-NPS.VA.GOV

  FLAGS: S                              RELAY DOMAIN: REDACTED.GOV

  DHCP ROUTING INDICATOR: NPS           DISABLE TURN COMMAND: YES

  LEVEL 1 NAME (c): GOV                 LEVEL 2 NAME (c): VA.GOV

  LEVEL 3 NAME (c): Q-NPS.VA.GOV        LEVEL 4 NAME (c): Q-NPS.VA.GOV

> **NOTE:** The bulletins do not contain any PHI therefore encryption is not necessary. Please refer to the ERA and EFT bulletin examples within the patch description.

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may retrieve documentation in one of the following ways:

1.  The preferred method is to FTP the files from REDACTED, which will transmit the files from the first available FTP server.
2.  Sites may also elect to retrieve documentation directly from a specific server as follows:

Albany REDACTED

Hines REDACTED

Salt Lake City REDACTED

3.  Documentation can also be retrieved from the VistA Documentation Library (VDL) on the Internet at the following address,

<http://www.va.gov/vdl>.

The documentation distribution includes:

TITLE FILE NAME

ePayments User Guide (EDI Lockbox) EPAYMENTS_USER_GUIDE_EDI_LOCKBOX_R0112.PDF

AR ePayments II Release Notes/ Installation Guide (PRCA\*4.5\*276) PRCA_4_5_P276_RN.PDF

AR Technical Manual/Security Guide (PRCA\*4.5\*276) AR_4_5_TM_R0112.PDF

 Note: Use ASCII mode when transferring the .KID file.

> Use Binary mode when transferring the .PDF file.  The .PDF files can be read on a PC using the Adobe Acrobat Reader program. The VistA Documentation Library \[VDL\] contains all end-user manuals.

# Release Changes and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enhancements to the ACCOUNTS RECEIVABLE application and installation steps are described below. See patch IB\*2.0\*451 for enhancements to the INTEGRATED BILLING application.

## Workload Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new Mail Group RCDPE AUDIT has been created to receive notification bulletins of ERA (Electronic Remittance Advice) over 30 days overdue and EFT (Electronic Funds Transfer) 14 days overdue.

ERA and EFT bulletins are created by a new scheduled option 'ePayments Workload Notifications' \[RCDPE WORKLOAD NOTIFICATION\]. This option should be scheduled in TaskMan to run weekly, biweekly or monthly.

Example of ERA bulletin:

------------------------

Unmatched ERA bulletin with warning message

Subj: EDI LBOX - ACTION REQUIRED-Unmatched ERAs \> 30 days \[#293527\]

05/09/11@19:34 11 lines

From: POSTMASTER In 'IN' basket. Page 1 Priority!

-----------------------------------------------------------------------

The listed ERAs were received more than 30 days ago and have not yet been matched.

Total \# of ERAs - 2

Total Dollar Amount - \$ 1,251,862.38

ERA# PAYER NAME FILE DATE AMT PAID

1009 AETNA INSURANCE COMPANY 12/12/10 1,251,762.38

1011 ABC INSURANCE COMPANY 5/8/11 100.00

Example of EFT Bulletin:

------------------------

Unmatched EFT bulletin with warning message

Subj: EDI LBOX - ACTION REQUIRED-EFTs \> 14 days \[#141174\] 05/09/11@19:45

27 lines

From: POSTMASTER In 'IN' basket. Page 1 Priority!

-------------------------------------------------------------------------

The following EFTs were received more than 14 days ago and have not yet been matched.

Total \# of EFTs - 2

Total Dollar Amount - \$ 1,251,862.38

DEPOSIT# RECEIPT# PAYER NAME EFT DATE DEPOSIT AMT

123456 1234567890 AETNA INSURANCE COMPANY 12/20/10 1,251,762.38

225152 55485542 ABC INSURANCE COMPANY 5/15/11 100.00

## Linking an ERA to a Receipt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option 'Update ERA Posted Using Paper EOB' \[RCDPE ERA POSTED BY PAPER EOB\] has been changed to include a new option to automatically search for payment receipts related to claims on the ERA. The user may then choose to link the receipt to the ERA.

A new option 'ERAs Posted with Paper EOB Audit Report' \[RCDPE ERA W/PAPER EOB REPORT\] has been added to the 'EDI Lockbox Reports Menu' \[RCDPE EDI LOCKBOX REPORTS MENU\]. This new report lists ERAs that have been linked to a receipt using the above menu option. The report is selectable by date range and division and identifies the user making the changes.

## EEOB Move/Copy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new option 'EEOB Move/Copy' \[RCDPE EEOB MOVE/COPY\] has been added to the 'EDI Lockbox Menu' \[RCDPE EDI LOCKBOX MENU\]. This new option allows EOBs that are matched to the wrong claim to be corrected. The EOB (Explanation of Benefits) may be moved to a different claim number or copied to one or more claim numbers (leaving original EOB intact). The user must enter a justification for the change.

A history of any EOB changes is recorded as AR (Accounts Receivable) Comments in the TPJI (Third Party Joint Inquiry) menu options.

A new option 'EEOB Move/Copy Audit Report' \[RCDPE EEOB MOVE/COPY REPORT\] has been added to the 'EDI Lockbox Reports Menu' \[RCDPE EDI LOCKBOX MENU\]. This new report lists EOBs that have been changed using the new 'EEOB Move/Copy' \[RCDPE EEOB MOVE/COPY\] menu option. The report is selectable by date range and division and identifies the user making the changes.

Details of EEOB Move and Copy transactions are also displayed in the following options:

View/Print ERA screen of the EEOB Worklist

View/Print EOB screen of the EEOB Worklist

Bill Charges screen of TPJI

Comment History screen of TPJI

A new Mail Group RCDPE MOVE COPY has been created to receive notification bulletins of EOB for none active claims moved or copied in the previous 24 hours. These bulletins are generated when the scheduled option 'Accounts Receivable Nightly Process Background Job' \[PRCA NIGHTLY PROCESS\] runs.

## EFT Work List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EFT Worklist has been modified to add new functionality which provides the user with the capability to select an EFT record and mark it as a duplicate so that these duplicate records are no longer reported on the EFT Worklist report. This new capability cannot be used on non-duplicates that are unmatched. To use this new functionality the user must have the new security key \[RCDPE ERA RETURNED TO PAYER\].

The EDI THIRD PARTY EFT DETAIL file (#344.31) has been modified with three new fields which record the following data each time that this option is used:

a\. Date/Time the transaction is performed.

b\. The user who performed the transaction (pointer to the NEW PERSON file (i.e. DUZ or IEN, to file \#200).

c\. A free text field that describes the justification for removing the duplicate EFT (1 to 100 characters in length).

A new option is provided in the EDI Lockbox Reports Menu, 'Duplicate EFT Audit Report' \[RCDPE EFT AUDIT REPORT\]. This option prints a report of EFTs that have been marked as removed/duplicate. The report displays the information contained in the new file \#344.31 fields mentioned above as well as the Division/Station, Payer Name of the EFT, the trace number of the EFT and the total number of duplicates removed (on the first page of the report). The justification for marking an EFT record as a duplicate is also listed on the EDI Third Party EFT Detail file.

## Mark ERA Returned to Payer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This existing option allows the user to mark the corresponding ERA as not paid/returned to payer and will remove it from the Worklist for unmatched ERAs. This existing functionality has been extended to audit the usage of this option.

## EEOB Worklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While a search for ERA records is in progress, a period (".") is displayed periodically so that the user knows that the system is still searching.

## EDI Lockbox Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Existing and new reports have been modified to have standard features as follows:

A Summary/Detail option

The ability to filter reports on Station/Division

The ability to export the report to Microsoft Excel (MS)

Sorting and printing features of MS Excel may then be used for further report processing if so desired.

The following reports where modified as per the above list:

EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]

ERA Unmatched Aging Report \[RCDPE ERA AGING REPORT\]

Unapplied EFT Deposits Report \[RCDPE UNAPPLIED EFT DEP REPORT\]

Duplicate EFT Audit Report \[RCDPE EFT AUDIT REPORT\]

ERAs Returned to Payer Audit Report \[RCDPE RETURNED ERA AUDIT\]

EEOB Move/Copy Audit report \[RCDPE EEOB MOVE/COPY REPORT\]

ERAs Posted with Paper EOB Audit Report \[RCDPE ERA W/PAPER EOB REPORT\]

## EEOB Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modifications are made to Accounts Receivable report options that will show the character '%' next to the bill number to indicate that an EEOB for the associated claim exists in the EOB file (#361.1). The following report options are modified by this patch:

Brief Account Profile \[PRCAY ACCOUNT PROFILE\]

Full Account Profile \[PRCAY FULL ACCOUNT PROFILE\]

List All Bills \[PRCA LIST ALL BILLS\]

Claims Matching Report RCDP CLAIMS MATCH\]

Bill Profile \[RCDP BILL PROFILE\]

Bill Transactions \[RCDP BILL TRANSACTIONS\]

## Negative Claim Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A problem reported by production sites has proven that the AR application allows claim balances to fall below zero. Corrections have been made to software that supports the following options and protocols to prevent a negative claim balance on the claim recorded in the Accounts Receivable file.

Options:

Receipt Processing \[RCDP RECEIPT PROCESSING\]

EEOB Worklist \[RCDPE EDI LOCKBOX WORKLIST\]

Protocols:

Process Receipt \[RCDP RECEIPT PROFILE PROCESS RECEIPT\]

Distribute Adj Amts \[RCDPE EOB WORKLIST DIST ADJ\]

# Support Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing, these patches will be supported by the Office of Enterprise Development, the development team. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any issues that arrive related to these patches. At the end of this 30 day period, assistance with issues related to these patches will be addressed through the Help Desk and the submittal of Remedy tickets if needed.