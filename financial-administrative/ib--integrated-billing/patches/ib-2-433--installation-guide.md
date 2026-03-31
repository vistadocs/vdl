---
title: IB*2*433/PRCA*4.5*270 eBilling - Preserve Claim Number When Cloning Release Notes/ Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*433
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 5
description: 
audience: 
keywords: 
  - bill
  - table
  - contents
  - claim
  - span
  - correct
  - patient
  - cancel
  - number
  - class
page_count: 0
word_count: 1930
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_20_433_prca_45_270_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_20_433_prca_45_270_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

eBilling – Preserve Claim Number When Cloning

Patch IB\*2\*433

Patch PRCA\*4.5\*270

Release Notes and Installation Guide

![](ib-2-433-prca-4-5-270-ebilling-preserve-claim-number-when-cloning-release-notes-/001.png)

May 2011

Veterans Affairs

Product Development (PD)

*This page included for two-sided copying.)*

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 38%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
<tr class="odd">
<th>05/04/2011</th>
<th>1.0</th>
<th>Initial</th>
<th><p>REDACTED</p>
<p>REDACTED</p>
<p>REDACTED</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

*This page included for two-sided copying.)*

Table of Contents

*This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Hardware Compatibility](#hardware-compatibility)
  - [System Specifications](#system-specifications)
  - [Installation and Configuration Notes](#installation-and-configuration-notes)
  - [Supported Functionality](#supported-functionality)
- [Release Changes and Enhancements](#release-changes-and-enhancements)
  - [New Option](#new-option)
    - [UB82](#ub82)
    - [CSA](#csa)
    - [MRW](#mrw)
    - [CRD](#crd)
  - [Modified Option](#modified-option)
- [SUPPORT INFORMATION](#support-information)
Release Date: May 2011
Patch Release: IB\*2\*433 PRCA\*4.5\*270
Initial Release Version: 1.0
The purpose of these patches are to provide the ability for sites to correct claims that have been either rejected at some stage in the processing of the claim or adjudicated by the payer and denied for some reason, a correctable reason, and to have the corrected version of the claim maintain the original claim number. Once corrected, the site can then resubmit the claim, electronically or by mail, to the payer for reprocessing.
The changes are primarily to the Integrated Billing (IB) module, Patch IB\*2\*433. Because there is a correlation between claim numbers in IB and claim numbers in Accounts Receivable (AR), the accompanying AR patch, Patch PRCA\*4.5\*270 modifies the BILL NUMBER field of the ACCOUNTS RECEIVABLE file to support adding the iteration number to the claim number of the original claim once it has been cancelled via the new correction process.
These changes result from business needs identified by the Chief Business Office (CBO). The ability to resubmit a rejected or denied claim with the original claim number is the normal process for most of the industry. This capability will also provide the ability to better track the processing of claims as it will provide the ability to follow claims through the resubmission process and to track the changes that were required as a result of a rejections or denials.

## Hardware Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special hardware considerations.

## System Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches are enhancements to existing VistA legacy modules and require no special system considerations.

## Installation and Configuration Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PRCA\*4.5\*270 and IB\*2\*433 should be installed together, with PRCA\*4.5\*270 being installed first. PRCA\*4.5\*270 makes some modifications to the ACCOUNTS RECEIVABLE file (#430), BILL NO. field (#.01), specifically the field description and D cross-reference. IB\*2\*433 contains the new Correct Rejected/Denied Claim menu option and protocol, as well as the routines to support this new function. In addition, it also adds a new security key, IB CLON, which locks the Copy and Cancel \[IB COPY AND CANCEL\] menu option to limit future use of this existing option. The IB patch also decreases the bottom margin of the LIST TEMPLATE: IBCEM MRA MANAGEMENT, to allow for the addition of the new CR (Correct Bill) action to the MRW \[IBCE MRA MANAGEMENT\] menu option.

The patches are to be installed using the KIDS Installation 6 (Install package) option.

Because the IB\*2\*433 patch includes new and modified menu options, if your system does NOT automatically rebuild menu trees as part of a nightly tasked option, it is recommended that you answer YES at the following prompt:

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

There are no pre or post-installation or configuration activities associated with this install.

## Supported Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release will provide a new IB option that will allow users to correct rejected or denied claims to third party insurance companies while maintaining the original claim number.

# Release Changes and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new option, Correct Rejected/Denied Bill \[IB CORRECT REJECTED/DENIED\] will be added to the following locations:

UB82 - Third Party Billing Menu ... \[IB THIRD PARTY BILLING MENU\]

CSA - Claims Status Awaiting Resolution \[IBCE CLAIMS STATUS AWAITING\]

MRW - MRA Management WorkList \[IBCE MRA MANAGEMENT\]

This new option cannot be used on claims with the following Billing Rate Types:

- INTERAGENCY
- SHARING AGREEMENT
- TRICARE or TRICARE REIMB.
- WORKMAN’S COMP. – Varies with which AR Fund the Workman’s Compensation claim is associated

When users attempt to use the CRD Correct Rejected/Denied Bill option to correct a rejected or denied claim which has an excluded Billing Rate Type, they will be warned that they must use the existing CLON Copy and Cancel option.

Select Third Party Billing Menu Option: <span class="mark">CRD</span> Correct Rejected/Denied Bill

Enter BILL NUMBER or Patient NAME: K600XXX IB,PATIENT1 XX-XX-XX

Outpatient REIMBURSABLE INS. PRNT/TX

<span class="mark">This option cannot be used to correct some Billing Rate Types (Example: TRICARE).</span>

<span class="mark">Use Copy and Cancel (CLON) to correct this bill.</span>

### UB82

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Billing Supervisor Menu Option: ub82 Third Party Billing Menu

ADPR Print Bill Addendum Sheet

AUTH Authorize Bill Generation

BILL Enter/Edit Billing Information

CANC Cancel Bill

CLA Multiple CLAIMSMANAGER Claim Send

CLON Copy and Cancel

CPST Copy for Secondary/Tertiary Bill

<span class="mark">CRD Correct Rejected/Denied Bill</span>

DLST Delete Auto Biller Results

GEN Print Bill

INQU Patient Billing Inquiry

LIST Print Auto Biller Results

PRNT Print Authorized Bills

RETN Return Bill Menu ...

VIEW View Bills Pending Transmission

VIST Outpatient Visit Date Inquiry

### CSA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Claims Status Awaiting Jul 14, 2010@15:51:06 Page: 1 of 1

CLAIMS STATUS AWAITING RESOLUTION-DETAIL

Message Status = NOT REVIEWED

Bill \# Payer Name Patient Name SSN Svc Date Curr Bal

K700XXX MEDICARE (WNR) IB,PATIENT 1 XXXX XX/XX/XX \$3298.15

Svc Loc: HOSPITAL Division: ANYSITE VAMROC

Biller Name: IB,CLERK 3 Days Pending: 1250

Date Rec'd: XX/XX/XX@08:31 Dt Generated: XX/XX/XX@06:38

Message Text:

Error CODE NOT RECOGNIZED BY OPPS; ALTERNATE CODE FOR SAME SERVICE

MAY BE AVAILABLE.

Patient: IB,P

Service Dates: XX/XX/XX – XX/XX/XX

Source: Sent by non-payer (RTP)

Enter ?? for more actions

Cancel Bill Process COB Print Bill

<span class="mark">Correct Bill</span> Retransmit Bill Exit

EDI History Display Review Status

Enter/Edit Comments Third Party Joint Inq.

Select Action: Quit//

### MRW

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MRA Management WorkList Jul 14, 2010@15:55:24 Page: 1 of 11

Bill \# Svc Date Patient Name SSN Pt Resp Bill Amt Care/Form

BILLER: IB,CLERK 45

1 442-K602XXX XX/XX/XX IB,PATIENT 33 XXXX 8.42 299.47 OP/1500

Insurers: MEDICARE (WNR), UNITEDHEALTHCARE

MRA Status: PROCESSED, Feb 28, 2007

2 442-K700XXX XX/XX/XX IB,PATIENT56 XXXX 0.00 60.07 OP/1500

Insurers: MEDICARE (WNR), UNITED COMMERCIAL TRAVELERS

MRA Status: DENIED, Oct 25, 2006

3 442-K700XXX XX/XX/XX IB,PATIENT 2 XXXX 109.91 109.91 OP/1500

Insurers: MEDICARE (WNR), AMERICAN REPUBLIC INSURANCE CO

MRA Status: DENIED, Nov 20, 2006

4 442-K700XXX XX/XX/XX IB,PATIENT 6 XXXX 0.00 341.46 OP/UB-04

Insurers: MEDICARE (WNR), MUTUAL OF OMAHA

MRA Status: DENIED, Dec 05, 2006

5 442-K700XXX XX/XX/XX IB,PATIENT 58 XXXX 0.00 76.36 OP/UB-04

Insurers: MEDICARE (WNR), BLUE CROSS/BS NE (65+WY)

\+ Enter ?? for more actions

PC  Process COB           VC  View Comments         PM  Print MRA

VE  View an EOB           CB  Cancel Bill           TP  Third Party Joint Inq.

SU  Summary MRA Info      CR  Correct Bill          Q   Exit

EC  Enter Comments        CC  Cancel/Clone A Bill

RS  Review Status         VB  View Bill

Select Action: Quit//

This new option will function in a manner similar to the existing Copy and Cancel option. It should be used to correct claims that have been rejected at any stage in the claims processing (FSC, Emdeon or Insurance Company) or denied by the Insurance Company. The old claim will be cancelled and renamed with the original claim number plus an incremental number, KXXXXXX-01. A new claim, which is a copy of the original claim, will be created and will maintain the original claim number.

### CRD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Third Party Billing Menu Option: CRD Correct Rejected/Denied Bill

Enter BILL NUMBER or Patient NAME: K701XXX IB,PATIENT T 06-22-10

Outpatient REIMBURSABLE INS. PRNT/TX

ARE YOU SURE YOU WANT TO CANCEL THIS BILL? No// y (Yes)

LAST CHANCE TO CHANGE YOUR MIND...

CANCEL BILL?: y (YES)

REASON CANCELLED: Testing

...Bill has been cancelled...

\>\> The receivable associated with the claim was cancelled.

IB,PATIENT T (XXX-XX-XXXX) DOB: XXX XX,XXXX

================================================================================

Rate Type : REIMBURSABLE INS.

Event Date : XXX XX,XXXX

Sensitive : NO

Responsible : INSURANCE CARRIER (Specify CARRIER on SCREEN 3)

Loc of Care : HOSPITAL (INCLUDES CLINIC) - INPT. OR OPT.

Event Source : Outpatient

Timeframe : ADMIT THRU DISCHARGE

(Specify actual bill type fields on SCREENs 6/7)

Bill From : XXX XX,XXXX

Bill To : XXX XX,XXXX

<span class="mark">Initial Bill# : K701XXX</span>

<span class="mark">Copied Bill# : K701XXX-01</span>

Please verify the above information for the bill you just entered. Once this

information is accepted it will no longer be editable and you will be required

to CANCEL THE BILL if changes to this information are necessary.

IS THE ABOVE INFORMATION CORRECT AS SHOWN? Yes//

Before the new claim is Authorized, the history will be displayed.

... Executing A/R edits

No A/R errors found

<span class="mark">Entered : JUL 14, XXXX by IB,CLERK 1</span>

<span class="mark">Copied : Jul 14, XXXX by IB,CLERK 2</span>

<span class="mark">Copied From : K701XXX-01</span>

<span class="mark">Reason Copied : Testing</span>

WANT TO EDIT SCREENS? NO//

THIS BILL WILL BE TRANSMITTED ELECTRONICALLY

WANT TO AUTHORIZE BILL AT THIS TIME? No//

The history will be available from the following locations:

TPJI - Third Party Joint Inquiry \[IBJ THIRD PARTY JOINT INQUIRY\]

INQ - Patient Billing Inquiry \[IB OUTPUT FULL INQ BY BILL NO\]

BILL - Enter/Edit Billing Information \[IB EDIT BILLING INFO\]

This option can NOT be used to correct a claim if any payment has been posted to the claim in Accounts Receivable (AR). If any payment has been posted, then the old option Copy and Cancel option must be used.

Enter BILL NUMBER or Patient NAME: K600XXX IB,PATIENT 20 XX-XX-XXXX Outpatient REIMBURSABLE INS. PRNT/TX

<span class="mark">Please note a PAYMENT of \*\*\$45\*\* has been POSTED to this bill. Copy and cancel</span>

<span class="mark">(CLON) must be used to correct this bill.</span>

Enter BILL NUMBER or Patient NAME:

## Modified Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The existing option, Copy and Cancel \[IB COPY AND CANCEL\] will be locked with a new Security Key, IB CLON.

# SUPPORT INFORMATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During Field Testing, these patches will be supported by the Office of Enterprise Development, the development team. For the first 30 days following National Release, the development team will work with the Product Support team to assist with any issues that arrive related to these patches. At the end of this 30 day period, assistance with issues related to these patches will be addressed through the Help Desk and the submittal of Remedy tickets if needed.