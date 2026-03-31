---
title: Accounts Receivable Version 4.5 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 8
description: 
audience: 
keywords: 
  - blockquote
  - prcai
  - class
  - installation
  - even
  - table
  - style
  - width
  - contents
  - instructions
page_count: 0
word_count: 4984
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/45instal.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/45instal.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

> Department of Veterans Affairs Decentralized Hospital Computer Program

ACCOUNTS RECEIVABLE INSTALLATION GUIDE

> Version 4.5 March 1995

> Information Systems Center Washington, D.C.

[INTRODUCTION 1](#introduction)

[PRE-INSTALLATION INSTRUCTION S 3](#pre-installation-instructions)

> [DESCRIPTION 3](#pre-installation-instructions)

[PRE-INSTALLATION PROCEDUR E 4](#Pre-Installation_Procedure)

[INSTALLATION INSTRUCTION S 5](#installation-instructions)

> [RUN-TIME ESTIMATES 5](#Run-Time_Estimates)

> [DESCRIPTION 6](#Installation_Procedure)

> [ROUTINE LIST 21](#routine-list)

> [RECOMPILED TEMPLATES 23](#recompiled-templates)

> March 1995 AR V. 4.5 Installation Guide i

> ii AR V. 4.5 Installation Guide March 1995

> Revision History

> Initiated on 12/29/04

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 34%" />
<col style="width: 26%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Date</p>
</blockquote></th>
<th><blockquote>
<p>Description (Patch # if applic.)</p>
</blockquote></th>
<th><blockquote>
<p>Project Manager</p>
</blockquote></th>
<th><blockquote>
<p>Technical Writer</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>12/29/04</p>
</blockquote></td>
<td><blockquote>
<p>Updated to comply with SOP 192-</p>
<p>352 Displaying Sensitive Data.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12/29/04</p>
</blockquote></td>
<td><blockquote>
<p>Pdf file checked for accessibility to</p>
<p>readers with disabilities.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pre-Installation Instructions](#pre-installation-instructions)
  - [DESCRIPTION](#description)
  - [PRE-INSTALLATION PROCEDURE](#pre-installation-procedure)
- [Installation Instructions](#installation-instructions)
  - [RUN-TIME ESTIMATES](#run-time-estimates)
  - [EXAMPLE OF INSTALLATION](#example-of-installation)
  - [POST-INSTALLATION PROCEDURE](#post-installation-procedure)
- [Routine List](#routine-list)
- [Recompiled Templates](#recompiled-templates)
    - [Recompile Templates on all Systems; if the routines in the UCI where the PRCAINITS were run are not reachable by other UCIs, it is necessary to recompile all templates using the routine PRCACV10.](#recompile-templates-on-all-systems-if-the-routines-in-the-uci-where-the-prcainits-were-run-are-not-reachable-by-other-ucis-it-is-necessary-to-recompile-all-templates-using-the-routine-prcacv10)
> Accounts Receivable (AR) Version 4.5 is designed as an enhancement to AR Version 4.0. Its purpose is to incorporate the software necessary for integration with the new Financial Management System (FMS) that is replacing CALM.
> Follow the Pre-Installation and the Installation procedures closely to guarantee correct installation of AR V.4.5. Each section of instructions is an actual installation procedure, which displays the computer dialogue occurring during the installation.
> March 1995 AR V. 4.5 Installation Guide 1
> Introduction
> 2 AR V.4.5 Installation Guide March 1995

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DESCRIPTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Pre-Installation routine examines the current AR system for a clean installation of AR V.4.5.

> Among other functions, the Pre-Installation routine removes CALM Identifiers from files 430 and 433. Secondly, the Pre- Installation routine searches the option file and removes all entry and exit actions and routine entries for the PRCA namespaced options. This will insure a clean installation of the new options. Thirdly, the Pre-Installation deletes obsolete menus and options. These include:

> PRCAT PAT REF NUMBER PRCA APPROPRIATION/GL PRCA GECS BATCH

> PRCA GECS BATCHES STATUS PRCA GECS CODE EDIT

> PRCA GECS DELETE PRCA GECS MAIN MENU PRCA GECS PURGE PRCA GECS REBATCH

> PRCA GECS RETRANSMIT PRCA GECS TRANSMIT PRCA GECS USER MENU PRCAT RX CO-PAY PROCESS PRCAT ACCRUAL AMT

> PRCAT CREATE CALM

> PRCAF BILL COMMON SERIES PRCA GECS BATCH EDIT

> PRCA GECS BATCHES WAITING TRAN PRCA GECS CREATE

> PRCA GECS KEYPUNCH

> PRCA GECS MAINTENANCE USER MENU PRCA GECS READY FOR BATCHING LIST PRCA GECS REPORTS MENU

> PRCA GECS REVIEW CODE SHEET PRCA GECS TRANSMIT USER PRCAD REV TOTALS BY RATE TYPE PRCAT LIST NEW TRANSACTION RCNR NATIONAL ROOLLUP REPORT

> After installation each site will need to use VA Kernel options to remove dangling pointers from the option file. See Post- Installation instructions. Finally, the Pre-Installation routine will delete the data dictionary for files 344.1, which is now the AR Deposit file and 430.4.

> The following mailgroups should already be setup from previous versions of Accounts Receivable or from IFCAP installation. If they have not been, they need to be created for proper usage of version 4.5.

- PRCA Adjustment Trans
- IRS
- PRCA ERROR
- FMS

> March 1995 AR V. 4.5 Installation Guide 3

> <span id="Pre-Installation_Procedure" class="anchor"></span>Pre-Installation Instructions

## PRE-INSTALLATION PROCEDURE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following steps should be followed for Pre-Installation of Accounts Receivable Version 4.5:

> NOTE: READ INSTALLATION GUIDE IN ITS ENTIRETY BEFORE PERFORMING ANY INSTALLATION

> <u>PROCEDURES.</u>

1.  Ensure that all Cashier Receipts have been approved and posted.
2.  Ensure that all AR bills with the status of “NEW BILL” are processed in AR, accounting, and CALM or returned to the service.
3.  Ensure that all AR transactions with the status of “PENDING CALM CODE” are processed in accounting.
4.  Ensure all AR bills in “REFUND REVIEW” status are processed in AR, accounting and CALM.
5.  Verify the post conversion for AR V. 4.0 has been completed. Use the VA FileManager inquiry option into file 412. If the file is missing, the conversion has been completed.
6.  Ensure that the following are currently running:
    - KERNEL Version 7.1
    - VA FileMan Version 20
    - MAS Version 5.3 (PIMS)
    - IFCAP Version 5.0
    - IB Version 2.0
    - Generic Code Sheet 2.0.

> 4 AR V. 4.5 Installation Guide March 1995

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains run-time values for installation, a brief description of the Installation routine, and step-by-step instructions for performing the installation along with an example of these instructions.

> OPERATING SPECIFICS

> *Sizing Information*

> AR test sites were asked to provide the number of entries made in the three main files for Accounts Receivable using VA FileMan. In addition, the sites ran %ZTBKC to obtain the block count for the associated globals. These files represent the most active and fastest growing AR files. As a result, it is estimated that AR will require the following (note that block sizes are for DSM-11):

> ^RCD(340 - 1/5 block per entry (AR Debtor)

> ^PRCA(430 - 1/2 block per entry (Accounts Receivable)

> ^PRCA(433 - 1/4 block per entry (AR Transaction)

> ^RC(341 - 1/4 block per entry(AR Event)

> Please note these are an estimate of what is necessary for only a subset of the dynamic files of AR.

> To get the estimate of the number of Accounts Receivable transactions, contact your Fiscal Service.

> NOTE: Please be aware that Fiscal is required to have access to

> <u>this information for 6 to 10 years to meet legal requirements.</u>

> *Recommended Equipment*

> <u>Fiscal</u>

> 1 CRT per Accounting Technician

> 1 CRT per Accounts Receivable Clerk 1 CRT for Agent Cashier

> 1 CRT for Application Coordinator

> 1 132 column Dot Matrix Printer (for printing free-form bills, pre­ printed UB-82 forms, reports, and patien t statements)

> 1 Letter Quality Printer (reports and letters)

> 1 Letter Quality Printer (for printing collection letters)

> March 1995 AR V. 4.5 Installation Guide 5

> Post Installation Instructions

> There are three default printer locations associated with the AR package. These printers will be associated with a device number on your DHCP system. You may be able to use the same printer for multiple types of outputs. Please consult with your Application Coordinators as to what outputs may be sent to "shared" printers, and where these printers should be located within the Fiscal Service.

> *Translation Tables*

> The following is a list of globals that should be translated to allow access in a distributed operating system environment. All globals are accessed by all users and all AR data is stored in

> <span id="Run-Time_Estimates" class="anchor"></span>^PRC\* and RC\*.

> RCD - This global contains the AR Debtor file (#340). PRCA - This global contains the Accounts Receivable files.

> NOTE: The PRCAK, PRCA, and RC

> globals may grow very large.

> <u>(See the Sizing Information).</u>

> RC - Debtor.

> RCY - Batch payment. PRCAK - Archive Purge

## RUN-TIME ESTIMATES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Platform</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File</strong></p>
</blockquote></th>
<th><strong>Entries</strong></th>
<th><blockquote>
<p><strong>Run-Time Estimates</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>System</strong></p>
<p><strong>Resource Usage</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Blocks Used</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VAX-DSM</p>
</blockquote></td>
<td><blockquote>
<p>430</p>
</blockquote></td>
<td>280,083</td>
<td>30 min</td>
<td><blockquote>
<p>LIGHT</p>
</blockquote></td>
<td><blockquote>
<p>10,000</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MSM-PC</p>
</blockquote></td>
<td><blockquote>
<p>430</p>
</blockquote></td>
<td>106,000</td>
<td>15 min</td>
<td><blockquote>
<p>LIGHT</p>
</blockquote></td>
<td><blockquote>
<p>3,500</p>
</blockquote></td>
</tr>
</tbody>
</table>

> DESCRIPTION

> The Installation routine adds the FMS accounting fields to AR files 340, 430, 433, and the new file 347.

> 6 AR V. 4.5 Installation Guide March 1995

<span id="Installation_Procedure" class="anchor"></span>Installation Instructions

> INSTALLATION PROCEDURE

> The following steps should be followed when installing Accounts Receivable Version 4.5.

1.  Contact MCCR/Fiscal and make sure that all UB 92s, Patient Statements, and Follow-up Letters have printed for the day.
2.  Backup system(s).
3.  Discontinue all Pharmacy labeling and Accounts Receivable activity, e.g. Fiscal, Billing, and Integrated Billing.
4.  Confirm that the Agent Cashier has reconciled and posted all payments. This will ensure that the Agent Cashier Reconciliation Report queued task is completed.
5.  Dequeue all AR tasks that would conflict with the Installation routine. These would be tasks that are scheduled to run during the time of day that the Installation routine will be running. An example might be a report that would print at the same time the installation would be running.
6.  Make sure all messages queued for the domain REDACTED.VA.GOV have been transmitted.
7.  Ensure IFCAP V. 5.0 and Generic Code sheet V. 2.0 have been or will be installed *before* using AR V. 4.5.
8.  Sign into UCI where package is to be loaded.
9.  Delete all PRCA\*, and RC\* routines on all systems.
10. Load the Accounts Receivable V.4.5 (PRCA\* and RC\*) routines in production UCI.
11. Verify that all system variables (DTIME, U, IO, IOST, etc.) are defined and the variable DUZ(0)="@". The DUZ variable must be defined as an active user number and DUZ(0) variable must equal "@" in order to initialize. To do this, perform the following steps at the MUMPS system prompt:

> March 1995 AR V. 4.5 Installation Guide 7

> Post Installation Instructions

12. Set up the programmer environment:

#### \>KILL

#### \>D ^XUP

> Setting Up Programmer Environment Access Code: \[Access Code\] Terminal Type set to: C-VT220

> Select OPTION NAME: \<ret\>

#### \>D Q^DI

> VA FileMan 20.0

> Select OPTION: \<ret\>

13. Install AR V. 4.5 by running the installation routine; see Example of Installation section in this manual. In programmer mode: ^PRCAINST.
14. Move PRCA\*, and RC\* routines to all systems.
15. Recompile all PRCA\* templates on all systems other than where the inits were run; see Recompiled Templates section, page 23.
16. Review and rebuild your routine map sets to include the new AR routines. You must recompile your routine map sets for the new AR routines to ensure that you do not enable old map sets; see the Mapped Routine section of the Technical Manual.
17. Ensure that the PRCA Nightly Process option is queued to run daily at 2:00am using the Schedule option under Task Manager. An output device is not required because the background job prints several reports and looks at the AR Site Parameter file for the printer.
18. Add users to the FMS mail group. The recipients should include any AR or accounting personnel responsible for AR data.
19. Since the installation process removed some obsolete options, you need to run the Kernel option Fix Option File Pointers under the Menu Management option. This will remove any pointers to these obsolete options that may have existed under local menus.

> 8 AR V. 4.5 Installation Guide March 1995

<span id="Example_of_Installation" class="anchor"></span>Installation Instructions

## EXAMPLE OF INSTALLATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is an example of a successful installation of the Accounts Receivable software package, installed in an account where the AR package was implemented.

#### \>D ^PRCAINST

> Accounts Receviable Version 4.5 can only be installed at those sites converting

> to FMS.

> Before installing AR 4.5 insure that IFCAP V5.0 and Generic Code Sheet V2.0

> IS or WILL BE installed PRIOR to using AR 4.5.

> If this process stops you can restart it by redoing the INIT process (D ^PRCAINST).

> DO YOU WANT TO CONTINUE? YES BEGINNING INSTALLATION

> This version (#4.5V6) of 'PRCAINIT' was created on 03-MAR-1995 (at WASH-ISC @ ALTOONA, PA, by VA FileMan V.20.0)

> I AM GOING TO SET UP THE FOLLOWING FILES:

340. AR DEBTOR

> Note: You already have the 'AR DEBTOR' File.

341. AR EVENT

> Note: You already have the 'AR EVENT' File.

1.  AR EVENT TYPE (including data) Note: You already have the 'AR EVENT TYPE' File. I will OVERWRITE your data with mine.
342. AR SITE PARAMETER

> Note: You already have the 'AR SITE PARAMETER' File.

1.  AR GROUP

> Note: You already have the 'AR GROUP' File.

2.  AR GROUP TYPE (including data) Note: You already have the 'AR GROUP TYPE' File. I will OVERWRITE your data with mine.
343. AR FORM LETTER (including data) Note: You already have the 'AR FORM LETTER' File. I will OVERWRITE your data with mine.
344. AR BATCH PAYMENT

> Note: You already have the 'AR BATCH PAYMENT' File.

1.  AR DEPOSIT

> \*BUT YOU ALREADY HAVE ‘AR NATIONAL DATA BASE CRITERIA’ AS FILE \#344.1!

> Shall I change the NAME of the file to AR DEPOSIT? NO// YES

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 27%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>347</p>
</blockquote></th>
<th>AR</th>
<th>FMS</th>
<th><blockquote>
<p>DOCUMENT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>347.1</p>
</blockquote></td>
<td>AR</td>
<td>FMS</td>
<td><blockquote>
<p>DOCUMENT TYPE</p>
</blockquote></td>
<td><blockquote>
<p>(including data)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>347.2</p>
</blockquote></td>
<td>AR</td>
<td>FMS</td>
<td><blockquote>
<p>NDB TOTALS</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> March 1995 AR V. 4.5 Installation Guide 9

> Post Installation Instructions

3.  REVENUE SOURCE CODE (including data)
4.  AR/FMS DOCUMENTS (including data)
348. AR NATIONAL DATA BASE CRITERIA (including data)
     1.  BAD DEBT ALLOWANCE

> 430 ACCOUNTS RECEIVABLE

> Note: You already have the 'ACCOUNTS RECEIVABLE' File.

2.  ACCOUNTS RECEIVABLE CATEGORY (including data) Note: You already have the 'ACCOUNTS RECEIVABLE CATEGORY' File. I will OVERWRITE your data with mine.
3.  ACCOUNTS RECEIVABLE TRANS.TYPE (including data) Note: You already have the 'ACCOUNTS RECEIVABLE TRANS.TYPE' File.

> I will OVERWRITE your data with mine.

> 430.6 AR DEBT LIST

> Note: You already have the 'AR DEBT LIST' File.

> 430.8 AR ARCHIVE

> Note: You already have the 'AR ARCHIVE' File.

> 433 AR TRANSACTION

> Note: You already have the 'AR TRANSACTION' File.

> SHALL I WRITE OVER FILE SECURITY CODES? NO// (NO)

> NOTE: This package also contains BULLETINS

> SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME?

> YES// (YES)

> NOTE: This package also contains SORT TEMPLATES

> SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> NOTE: This package also contains INPUT TEMPLATES

> SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// (YES)

> NOTE: This package also contains PRINT TEMPLATES

> SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// (YES)

> NOTE: This package also contains FUNCTIONS

> SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME?

> YES// (YES)

> NOTE: This package also contains SECURITY KEYS

> SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME?

> YES// (YES)

> NOTE: This package also contains OPTIONS

> SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES//

> (YES)

> ARE YOU SURE EVERYTHING'S OK? NO// Y (YES) Beginning PRE-INITIALIZATION...

> Deleting obsolete options... PRCAT ACCRUAL AMT

> PRCAT PAT REF NUMBER PRCAT CREATE CALM

> PRCAT LIST NEW TRANSACTION PRCA APPROPRIATION/GL PRCAF BILL COMMON SERIES PRCA GECS BATCH

> PRCA GECS BATCH EDIT PRCA GECS BATCHES STATUS

> PRCA GECS BATCHES WAITING TRAN PRCA GECS CODE EDIT

> 10 AR V. 4.5 Installation Guide March 1995

Installation Instructions

> PRCA GECS CREATE PRCA GECS DELETE PRCA GECS KEYPUNCH PRCA GECS MAIN MENU

> PRCA GECS MAINTENANCE USER MENU PRCA GECS PURGE

> PRCA GECS READY FOR BATCHING LIST PRCA GECS REBATCH

> PRCA GECS REPORTS MENU PRCA GECS RETRANSMIT

> PRCA GECS REVIEW CODE SHEET PRCA GECS TRANSMIT

> PRCA GECS TRANSMIT USER PRCA GECS USER MENU PRCAT RX CO-PAY PROCESS

> RCNR NATIONAL ROLLUP REPORT PRCAD REV TOTALS BY RATE TYPE

> Finished.

> Deleting obsolete options... PRCAT ACCRUAL AMT

> PRCAT PAT REF NUMBER PRCAT CREATE CALM

> PRCAT LIST NEW TRANSACTION PRCA APPROPRIATION/GL PRCAF BILL COMMON SERIES PRCA GECS BATCH

> PRCA GECS BATCH EDIT PRCA GECS BATCHES STATUS

> PRCA GECS BATCHES WAITING TRAN PRCA GECS CODE EDIT

> PRCA GECS CREATE PRCA GECS DELETE PRCA GECS KEYPUNCH PRCA GECS MAIN MENU

> PRCA GECS MAINTENANCE USER MENU PRCA GECS PURGE

> PRCA GECS READY FOR BATCHING LIST PRCA GECS REBATCH

> PRCA GECS REPORTS MENU PRCA GECS RETRANSMIT

> PRCA GECS REVIEW CODE SHEET PRCA GECS TRANSMIT

> PRCA GECS TRANSMIT USER PRCA GECS USER MENU PRCAT RX CO-PAY PROCESS

> RCNR NATIONAL ROLLUP REPORT PRCAD REV TOTALS BY RATE TYPE

> Finished.

> Deleting obsolete Input templates... PRCA AR DEV

> PRCA AR2 AMIS 243-249 PRCA AR2 AMIS 251-254 PRCA AR2 AMIS 294-296 PRCA AR2 AMIS MEDIGAP PRCA AR2 AMIS MEDIGAP VM PRCABILLVEN

> PRCAF COMMON SERIES

> RCMS GROUP 1 THRU RCMS GROUP 8

> Finished.

> Deleting obsolete Print Templates... PRCAT DISP GL

> Finished.

> Cleaning up entry and routine actions on A/R options...

> March 1995 AR V. 4.5 Installation Guide 11

> Post Installation Instructions

> Finished with the options.

> Deleting old 344.1 file... File 344.1 deleted...

> Deleting old 430.4 file... File 430.4 deleted...

> PRE-INIT finished. INITIALIZATION Continues...

> ...EXCUSE ME, THIS MAY TAKE A FEW MOMENTS..........................................................

> .................................................................

> .................................................................

> .................................................................

> .................

> 'PRCA NIGHTLY PROCESS ABORT' BULLETIN FILED -- Remember to add

> mail groups for new bulletins........................................................

> .................................................................

> .................................................................

> ............

> 'PRCA AGENCY LOCATION' Option Filed

> 'PRCA ACCOUNT CHECK' Option Filed

> 'PRCA ACCOUNT INFORMATION' Option Filed 'PRCA ACCOUNT MANAGEMENT' Option Filed

> 'PRCA BIL AGENCY' Option Filed 'PRCA BIL AMEND' Option Filed 'PRCA BIL APPROVE' Option Filed 'PRCA BIL CANCEL' Option Filed 'PRCA BIL EDIT' Option Filed 'PRCA BIL ENTER' Option Filed 'PRCA BIL PRNT' Option Filed 'PRCA BILL' Option Filed

> 'PRCA BILL COMMENT' Option Filed

> 'PRCA BILL STATUS LISTING' Option Filed

> 'PRCA CLERK MENU' Option Filed

> 'PRCA CO-PAY WAIVER REPORT' Option Filed 'PRCA CONFIRM DEPOSIT' Option Filed 'PRCA CREATE DEPOSIT' Option Filed

> 'PRCA DEACTIVATE GROUP' Option Filed 'PRCA DEBTOR COMMENT' Option Filed 'PRCA DEPOSIT MGR' Option Filed 'PRCA DEPOSIT MONEY' Option Filed 'PRCA DISC LIST' Option Filed

> 'PRCA EDIT A DEPOSIT' Option Filed 'PRCA FMS ACCT EDIT' Option Filed 'PRCA FMS BD REGEN' Option Filed 'PRCA FMS BILL INQ' Option Filed 'PRCA FMS CAF LIST' Option Filed 'PRCA FMS CASH RECEIPT' Option Filed

> 'PRCA FMS DOC/RECPT COMPAR' Option Filed 'PRCA FMS DOCUMENT INQUIRY' Option Filed

> 'PRCA FMS MBD REGEN' Option Filed 'PRCA FMS NDB REGEN' Option Filed

> 'PRCA FMS OBR MANUAL TRANS' Option Filed 'PRCA FMS REGENERATION' Option Filed

> 'PRCA FMS SBOC' Option Filed 'PRCA FMS TRANS INQ' Option Filed

> 'PRCA FMS UNPROCESSED LIST' Option Filed

> 'PRCA FMS UTILTIES' Option Filed 'PRCA FMS WRITE-OFF' Option Filed

> 'PRCA FMS-CONV ACCOUNTING' Option Filed 'PRCA FMS-CONV DECREASE ADJ' Option Filed 'PRCA FMS-CONV INCREASE ADJ' Option Filed

> 'PRCA FMS-CONV MENU' Option Filed

> 12 AR V. 4.5 Installation Guide March 1995

Installation Instructions

> 'PRCA FMS-CONV SETUP BILL' Option Filed 'PRCA FOLLOW-UP REPORTS' Option Filed 'PRCA FORWARD IRS OFFSETS' Option Filed

> 'PRCA IRS OFFSET' Option Filed 'PRCA IRS PARAMETERS' Option Filed 'PRCA LAST ACTIVITY' Option Filed 'PRCA LIST ALL BILLS' Option Filed 'PRCA MANAGER MENU' Option Filed

> 'PRCA MARK INVALID TRANS.' Option Filed 'PRCA NIGHTLY PROCESS' Option Filed

> 'PRCA NOTIFICATION PARAMETERS' Option Filed 'PRCA NR NATIONAL ROLLUP REPORT' Option Filed 'PRCA NRNR BAD DEBT ACCR. EDIT' Option Filed 'PRCA PAYMENT TRANS HISTORY' Option Filed 'PRCA PAYMENTS WITH WRITE-OFFS' Option Filed

> 'PRCA PREPAY POST' Option Filed 'PRCA PROCESS DEPOSIT' Option Filed

> 'PRCA RECEIPT LIST' Option Filed 'PRCA REFUND REVIEW' Option Filed

> 'PRCA REFUND REVIEW LIST' Option Filed 'PRCA SITE PARAMETER' Option Filed 'PRCA SUMMARY DEPOSIT' Option Filed 'PRCA TRAN TYPE HISTORY' Option Filed

> 'PRCA TRANS HISTORY' Option Filed 'PRCA VEN BIL' Option Filed

> 'PRCA VIEW A BILL' Option Filed 'PRCA VIEW A DEPOSIT' Option Filed 'PRCAA AMEND AUDIT' Option Filed 'PRCAA AUDIT' Option Filed

> 'PRCAA INCOMPLETE' Option Filed 'PRCAA OLD BILL' Option Filed 'PRCAA OLD EDIT' Option Filed 'PRCAA OLD SETUP' Option Filed

> 'PRCAA SET/AUDIT NEW BILL' Option Filed

> 'PRCAA SETUP BILL' Option Filed 'PRCAB PRINT BILLS' Option Filed

> 'PRCAB PRINT OTHER BILLS' Option Filed 'PRCAB REPRINT OTHER BILL' Option Filed

> 'PRCAC 3RD DATA' Option Filed 'PRCAC BILL RESULTING' Option Filed

> 'PRCAC CHANGE' Option Filed 'PRCAC COWC REFER' Option Filed

> 'PRCAC DCDOJ ACTION MENU' Option Filed 'PRCAC DCDOJ COMPROMISE' Option Filed

> 'PRCAC DCDOJ DEBIT' Option Filed 'PRCAC DCDOJ REFER' Option Filed 'PRCAC DCDOJ REREFER' Option Filed 'PRCAC DCDOJ RETURNED' Option Filed

> 'PRCAC DCDOJ TERM' Option Filed 'PRCAC DCDOJ WAIVER' Option Filed 'PRCAC LOCATE DEBTOR' Option Filed 'PRCAC PRINT STATEMENT' Option Filed

> 'PRCAC PROFILE' Option Filed

> 'PRCAC PROFILE REPAYMENT' Option Filed 'PRCAC REPAYMENT MENU' Option Filed 'PRCAC REPRINT STATEMENT' Option Filed 'PRCAC SET REPAYMENT' Option Filed 'PRCAC TR ADJUSTMENT' Option Filed 'PRCAC TR ADM' Option Filed

> 'PRCAC TR DECREASE' Option Filed 'PRCAC TR INCREASE' Option Filed

> 'PRCAC TR RE-ESTABLISH BILL' Option Filed

> 'PRCAC TR SUSPENDED' Option Filed 'PRCAC TR TERM-COMPROMISE' Option Filed 'PRCAC TR TERM-FISCAL' Option Filed 'PRCAC TR TERMINATION' Option Filed

> 'PRCAC TR WAIVED' Option Filed

> March 1995 AR V. 4.5 Installation Guide 13

> Post Installation Instructions

> 'PRCAC TRANS PROFILE' Option Filed 'PRCAC TRANSACTION' Option Filed 'PRCAC WAIVED FULL' Option Filed 'PRCAC WAIVED PART' Option Filed 'PRCAD CONTINGENT 3RD' Option Filed

> 'PRCAD COWC LIST' Option Filed 'PRCAD DC COLLECT' Option Filed

> 'PRCAD DCDOJ COLLECTION' Option Filed 'PRCAD DOJ COLLECTION' Option Filed

> 'PRCAD MANAGEMENT REPORT MENU' Option Filed

> 'PRCAD MAS COMPLETE' Option Filed 'PRCAD MAS INCOMPLETE' Option Filed

> 'PRCAD MAS REPORT' Option Filed 'PRCAD R 3RD' Option Filed 'PRCAD R DC' Option Filed

> 'PRCAD R DELINQUENT MENU' Option Filed

> 'PRCAD R DOJ' Option Filed 'PRCAD R INT RATE' Option Filed 'PRCAD RDL 180' Option Filed 'PRCAD RDL 365' Option Filed 'PRCAD RDL 90' Option Filed 'PRCAD RDL ALL' Option Filed

> 'PRCAD RDL OVER 365' Option Filed 'PRCAD RECON CASH RECEIPT' Option Filed 'PRCAD RECON CASHIER' Option Filed 'PRCAD RECON MAS' Option Filed

> 'PRCAD RECONCILE MENU' Option Filed

> 'PRCAD REPORT MENU' Option Filed 'PRCAD REV CODE TOTALS' Option Filed

> 'PRCAE FOLLOW-UP' Option Filed 'PRCAE IRS OFFSET' Option Filed 'PRCAE L HOLD' Option Filed 'PRCAE LET REL' Option Filed 'PRCAE LIST HOLD' Option Filed 'PRCAE PR LETTERS' Option Filed 'PRCAE PR STATEMENT' Option Filed

> 'PRCAE REPRINT LETTERS' Option Filed

> 'PRCAE REPRINT UB' Option Filed 'PRCAF ADJ ADMIN' Option Filed 'PRCAF EDIT BILL FROM' Option Filed 'PRCAF PURGE UNPROC' Option Filed 'PRCAF RETURN BILL' Option Filed 'PRCAF SUPERVISOR MENU' Option Filed

> 'PRCAF TR DELETE' Option Filed 'PRCAF U ADMIN.RATE' Option Filed 'PRCAF U FORM ED' Option Filed 'PRCAF U FORM MENU' Option Filed 'PRCAF U PRINT FORM' Option Filed 'PRCAK AR SUPERVISOR' Option Filed 'PRCAK ARCHIVE' Option Filed

> 'PRCAK ARCHIVE MARK PRINT' Option Filed

> 'PRCAK BUILD TEMP' Option Filed 'PRCAK MARK FOR ARCHIVE' Option Filed

> 'PRCAK PURGE TEMP' Option Filed 'PRCAK REMOVE AR RECORD' Option Filed 'PRCAK UNMARK ARCHIVE' Option Filed

> 'PRCAL LIST MENU' Option Filed 'PRCAL OTHER LIST' Option Filed 'PRCAL REFER DC' Option Filed 'PRCAL REFER DOJ' Option Filed 'PRCAL STATUS LIST' Option Filed 'PRCAT FMS OP REGEN' Option Filed 'PRCAT USER' Option Filed

> 'PRCAX CO-PAY EXEMPTION REPORT' Option Filed 'PRCAY ACCOUNT PROFILE' Option Filed

> 'PRCAY APPROVE BATCH' Option Filed 'PRCAY CANCEL PAYMENT' Option Filed

> 14 AR V. 4.5 Installation Guide March 1995

Installation Instructions

> 'PRCAY CASH PAYMENT' Option Filed 'PRCAY CHECK/MO PAYMENT' Option Filed

> 'PRCAY CREDIT CARD PAYMENT' Option Filed 'PRCAY DEPOSIT MANAGEMENT' Option Filed 'PRCAY EDIT A RECEIPT' Option Filed 'PRCAY FULL ACCOUNT PROFILE' Option Filed 'PRCAY LIST RECEIPTS' Option Filed

> 'PRCAY MASTER' Option Filed

> 'PRCAY MOVE A PAYMENT' Option Filed 'PRCAY OTHER PAYMENT' Option Filed 'PRCAY POST TRANS' Option Filed 'PRCAY PRINT 215' Option Filed

> 'PRCAY RECEIPT MANAGEMENT' Option Filed 'PRCAY RELEASE HOLDS' Option Filed 'PRCAY REPRINT A RECEIPT' Option Filed 'PRCAY SUMMARY OF CURRENT' Option Filed 'PRCAY VOID A DEPOSIT' Option Filed 'PRCAY VOID A RECEIPT' Option

> Filed.............................................

> .................................................................

> ..............................................

> Compiling PRCA BATCH PAYMENT input template of File 433.....

> 'PRCATB' ROUTINE FILED....

> 'PRCATB1' ROUTINE FILED

> Compiling PRCA OLD SET input template of File 430...

> 'PRCATA' ROUTINE FILED....

> 'PRCATA1' ROUTINE FILED.........

> 'PRCATA2' ROUTINE FILED....

> 'PRCATA3' ROUTINE FILED.........

> 'PRCATA5' ROUTINE FILED....

> 'PRCATA4' ROUTINE FILED

> Compiling PRCA SET input template of File 430...

> 'PRCATE' ROUTINE FILED...

> 'PRCATE1' ROUTINE FILED.........

> 'PRCATE2' ROUTINE FILED.....

> 'PRCATE3' ROUTINE FILED.. 'PRCATE4' ROUTINE FILED

> Compiling PRCASV REL input template of File 430....

> 'PRCATSE' ROUTINE FILED.....

> 'PRCATSE1' ROUTINE FILED. 'PRCATSE2' ROUTINE FILED

> Compiling PRCA 3RD PROFILE print template of File 430........................................................

> 'PRCATP5' ROUTINE FILED...............

> Compiling PRCA DISP ADJ print template of File 433..............................

> 'PRCATO4' ROUTINE FILED......

> Compiling PRCA DISP AUDIT print template of File 430.................................

> 'PRCATO2' ROUTINE FILED............

> Compiling PRCA DISP CARE print template of File 433...................

> 'PRCATO5' ROUTINE FILED...

> Compiling PRCA FMS STATUS print template of File 347......................

> 'PRCATF1' ROUTINE FILED......

> March 1995 AR V. 4.5 Installation Guide 15

> Post Installation Instructions

> Compiling PRCA FMS TRANS STAT print template of File 347......................

> 'PRCATF2' ROUTINE FILED......

> Compiling PRCA MEANS PROFILE print template of File 430..................................

> 'PRCATP2' ROUTINE FILED.........

> Compiling PRCA OTHER PROFILE print template of File 430.............................

> 'PRCATP4' ROUTINE FILED........

> Compiling PRCA PROFILE print template of File 430............................

> 'PRCATP1' ROUTINE FILED........

> Compiling PRCA TRANS PROFILE print template of File 433.............................

> 'PRCATR3' ROUTINE FILED.......

> Compiling PRCA VENDOR PROFILE print template of File 430.............................................

> 'PRCATP3' ROUTINE FILED..............

> Compiling PRCAA AMEND AUDIT print template of File 430........................

> 'PRCATR2' ROUTINE FILED.........

> Compiling PRCAC TR LIST print template of File 433..........

> 'PRCATW1' ROUTINE FILED.

> Compiling PRCAP CARE WV print template of File 433.................

> 'PRCATW3' ROUTINE FILED...

> Compiling PRCAP COST print template of File 433........................

> 'PRCATO3' ROUTINE FILED.....

> Compiling PRCAP DEBTOR LOCATE print template of File 430.......................................

> 'PRCATO9' ROUTINE FILED.......

> Compiling PRCAP REPAYMENT print template of File 430..........................

> 'PRCATR1' ROUTINE FILED.....

> Compiling PRCAP RETURN BILL print template of File 430............................

> 'PRCATP6' ROUTINE FILED.......

> Compiling PRCAP WAIVED print template of File 433..................

> 'PRCATW2' ROUTINE FILED....

> Compiling PRCARFD print template of File 430......

> 'PRCATRF' ROUTINE FILED.

> Compiling PRCAT DISP CP print template of File 430......................

> 'PRCATO8' ROUTINE FILED....

> Compiling PRCAT NEW AR print template of File 430..............................

> 'PRCATP7' ROUTINE FILED.....

> 16 AR V. 4.5 Installation Guide March 1995

Installation Instructions

> Compiling PRCAT NEW TRANS print template of File 433..........................

> 'PRCATP9' ROUTINE FILED.......

> OK, I'M DONE.

> NO SECURITY-CODE PROTECTION HAS BEEN MADE

> March 1995 AR V. 4.5 Installation Guide 17

> Post Installation Instructions

> 18 AR V. 4.5 Installation Guide March 1995

> <span id="Post_Installation_Instructions" class="anchor"></span>Post-Installation Instructions

> After AR V. 4.5 has been installed, the following will insure that AR is setup correctly and insure a smooth transition from CALM to FMS.

## POST-INSTALLATION PROCEDURE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Upon receipt of the FMS Conversion Accounting Fields (CAF) Report from Austin, received as a mail message to the G.FMS mailgroup, use the menu PRCA FMS-CONV MENU to establish bills in AR which are on FMS but not on local AR. Use this menu to adjust local AR records with FMS to correct discrepancies.
2.  Edit the AR Site Parameter File to enter the Group Parameters for bank deposit, site deposit, and hospital site information. The bank deposit is the information for the depository used by fiscal service. Site deposit data is the information that is normally typed on the pre-printed SF 215 fiscal receives from Dept. of Treasury. From the Site Parameter Edit Menu Option:

> Select Site Parameter Edit Option: GROUP Parameters

> Select AR GROUP NAME: BANK DEPOSIT *(May have to add as a group name.)*

> TYPE: BANK (DEPOSIT)

> NAME: BANK DEPOSIT//

> STREET ADDRESS \#1: MELLON BANK (CENTRAL)

> STREET ADDRESS \#2: P.O. BOX 1234

> STREET ADDRESS \#3:

> CITY: ANYTOWN

> STATE: PA

> ZIP CODE: 15543

> PHONE NUMBER: 814 555-1212

> Select AR GROUP NAME: SITE DEPOSIT *(May have to add as a group name.)*

> TYPE: SITE (DEPOSIT)

> STREET ADDRESS \#1: YOUR VA MEDICAL CENTER

> STREET ADDRESS \#2: P.O. BOX 4321

> STREET ADDRESS \#3:

> CITY: ANYTOWN

> March 1995 AR V. 4.5 Installation Guide 19

> Post Installation Instructions

> STATE: CA

> ZIP CODE: 50134

> PHONE NUMBER: 310-555-1212

> Select AR GROUP NAME: HOSPITAL *(May have to add as a group name.)*

> TYPE: SITE

> NAME: HOSPITAL//

> STREET ADDRESS \#1: YOUR VA MEDICAL CENTER

> STREET ADDRESS \#2: P.O. BOX 1234 *(REQUIRED FOR FMS)*

> STREET ADDRESS \#3:

> CITY: ANYTOWN

> STATE: PA

> ZIP CODE: 15543

> PHONE NUMBER: 814 555-1212

#### \*NOTE: STREET ADDRESS \#2 IS REQUIRED FOR FMS DOCUMENTS...

3.  Edit the agency location code for recording deposits. Contact your Fiscal service for this code.

> From the Supervisors Menu:

> Select Supervisor's AR Menu Option: AGENcy Location Code (Deposits)

> ALC (DEPOSITS): 1090000-1

4.  Using the Kernel Menu Management option:

> Select Menu Management Option: FIX Option File Pointers

> Do you want to remove any 'Dangling Pointers' from your OPTION File? Y//

> PLEASE WAIT while I check this out . . . Your OPTION File is OK (no bad pointers).

5.  Delete PRCAI\* routines.
6.  Restore routine mapping.

> 20 AR V. 4.5 Installation Guide March 1995

# Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a list of the routines distributed with the Accounts Receivable software package Version 4.5.

<table style="width:100%;">
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PRCAACC</p>
</blockquote></th>
<th><blockquote>
<p>PRCAADBO</p>
</blockquote></th>
<th><blockquote>
<p>PRCAADIN</p>
</blockquote></th>
<th><blockquote>
<p>PRCAAPR</p>
</blockquote></th>
<th><blockquote>
<p>PRCAAPR1</p>
</blockquote></th>
<th><blockquote>
<p>PRCAATR</p>
</blockquote></th>
<th><blockquote>
<p>PRCABD</p>
</blockquote></th>
<th><blockquote>
<p>PRCABIL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRCABIL1</p>
</blockquote></td>
<td><blockquote>
<p>PRCABIL2</p>
</blockquote></td>
<td><blockquote>
<p>PRCABIL3</p>
</blockquote></td>
<td><blockquote>
<p>PRCABJ</p>
</blockquote></td>
<td><blockquote>
<p>PRCABJ1</p>
</blockquote></td>
<td><blockquote>
<p>PRCABJV</p>
</blockquote></td>
<td><blockquote>
<p>PRCABP1</p>
</blockquote></td>
<td><blockquote>
<p>PRCABP2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCABPF</p>
</blockquote></td>
<td><blockquote>
<p>PRCACLM</p>
</blockquote></td>
<td><blockquote>
<p>PRCACM</p>
</blockquote></td>
<td><blockquote>
<p>PRCACOL</p>
</blockquote></td>
<td><blockquote>
<p>PRCACV10</p>
</blockquote></td>
<td><blockquote>
<p>PRCADCDJ</p>
</blockquote></td>
<td><blockquote>
<p>PRCADCJ1</p>
</blockquote></td>
<td><blockquote>
<p>PRCADEL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCADIN</p>
</blockquote></td>
<td><blockquote>
<p>PRCADJ</p>
</blockquote></td>
<td><blockquote>
<p>PRCADR</p>
</blockquote></td>
<td><blockquote>
<p>PRCADR1</p>
</blockquote></td>
<td><blockquote>
<p>PRCADR2</p>
</blockquote></td>
<td><blockquote>
<p>PRCADR3</p>
</blockquote></td>
<td><blockquote>
<p>PRCAEA</p>
</blockquote></td>
<td><blockquote>
<p>PRCAEA1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAEIN</p>
</blockquote></td>
<td><blockquote>
<p>PRCAEOL</p>
</blockquote></td>
<td><blockquote>
<p>PRCAEXM</p>
</blockquote></td>
<td><blockquote>
<p>PRCAFBD</p>
</blockquote></td>
<td><blockquote>
<p>PRCAFBD1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAFBDM</p>
</blockquote></td>
<td><blockquote>
<p>PRCAFBDU</p>
</blockquote></td>
<td><blockquote>
<p>PRCAFDCT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAFN</p>
</blockquote></td>
<td><blockquote>
<p>PRCAFN1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAFOR</p>
</blockquote></td>
<td><blockquote>
<p>PRCAFUT</p>
</blockquote></td>
<td><blockquote>
<p>PRCAFWO</p>
</blockquote></td>
<td><blockquote>
<p>PRCAG</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGD</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGDR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAGDT</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGF</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGF1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGP</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGS</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGST</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGST1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGST2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAGT</p>
</blockquote></td>
<td><blockquote>
<p>PRCAGU</p>
</blockquote></td>
<td><blockquote>
<p>PRCAHIS</p>
</blockquote></td>
<td><blockquote>
<p>PRCAHIS1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAHOL</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI001</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI002</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI003</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI004</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI005</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI006</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI007</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI008</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI009</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00A</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00B</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI00C</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00D</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00E</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00F</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00G</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00H</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00I</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00J</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI00K</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00L</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00M</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00N</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00O</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00P</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00Q</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00R</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI00S</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00T</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00U</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00V</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00W</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00X</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00Y</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI00Z</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI010</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI011</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI012</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI013</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI014</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI015</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI016</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI017</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI018</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI019</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01A</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01B</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01C</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01D</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01E</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01F</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI01G</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01H</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01I</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01J</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01K</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01L</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01M</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01N</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI01O</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01P</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01Q</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01R</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01S</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01T</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01U</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01V</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI01W</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01X</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01Y</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI01Z</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI020</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI021</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI022</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI023</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI024</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI025</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI026</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI027</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI028</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI029</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02A</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02B</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI02C</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02D</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02E</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02F</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02G</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02H</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02I</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02J</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI02K</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02L</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02M</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02N</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02O</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02P</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02Q</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02R</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI02S</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02T</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02U</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02V</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02W</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02X</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02Y</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI02Z</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI030</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI031</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI032</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI033</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI034</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI035</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI036</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI037</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI038</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI039</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03A</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03B</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03C</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03D</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03E</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03F</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI03G</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03H</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03I</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03J</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03K</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03L</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03M</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03N</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI03O</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03P</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03Q</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03R</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03S</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03T</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03U</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03V</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI03W</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03X</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03Y</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI03Z</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI040</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI041</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI042</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI043</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI044</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI045</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI046</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI047</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI048</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI049</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04A</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04B</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI04C</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04D</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04E</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04F</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04G</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04H</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04I</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04J</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI04K</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04L</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04M</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04N</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04O</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04P</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04Q</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04R</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI04S</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04T</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04U</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04V</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04W</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04X</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04Y</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI04Z</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI050</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI051</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI052</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI053</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI054</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI055</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI056</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI057</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI058</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI059</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05A</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05B</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05C</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05D</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05E</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05F</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAI05G</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05H</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05I</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05J</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05K</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05L</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05M</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05N</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAI05O</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05P</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05Q</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05R</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05S</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05T</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05U</p>
</blockquote></td>
<td><blockquote>
<p>PRCAI05V</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAINI1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAINI2</p>
</blockquote></td>
<td><blockquote>
<p>PRCAINI3</p>
</blockquote></td>
<td><blockquote>
<p>PRCAINI4</p>
</blockquote></td>
<td><blockquote>
<p>PRCAINI5</p>
</blockquote></td>
<td><blockquote>
<p>PRCAINIS</p>
</blockquote></td>
<td><blockquote>
<p>PRCAINIT</p>
</blockquote></td>
<td><blockquote>
<p>PRCAINS1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAINST</p>
</blockquote></td>
<td><blockquote>
<p>PRCAKBT</p>
</blockquote></td>
<td><blockquote>
<p>PRCAKBT1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAKM</p>
</blockquote></td>
<td><blockquote>
<p>PRCAKMR</p>
</blockquote></td>
<td><blockquote>
<p>PRCAKS</p>
</blockquote></td>
<td><blockquote>
<p>PRCAKTP</p>
</blockquote></td>
<td><blockquote>
<p>PRCAKUN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCALET</p>
</blockquote></td>
<td><blockquote>
<p>PRCALM</p>
</blockquote></td>
<td><blockquote>
<p>PRCALST</p>
</blockquote></td>
<td><blockquote>
<p>PRCALST1</p>
</blockquote></td>
<td><blockquote>
<p>PRCALT2</p>
</blockquote></td>
<td><blockquote>
<p>PRCAMARK</p>
</blockquote></td>
<td><blockquote>
<p>PRCAMAS</p>
</blockquote></td>
<td><blockquote>
<p>PRCAMESG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAMRKC</p>
</blockquote></td>
<td><blockquote>
<p>PRCANRU</p>
</blockquote></td>
<td><blockquote>
<p>PRCANRU0</p>
</blockquote></td>
<td><blockquote>
<p>PRCANTE0</p>
</blockquote></td>
<td><blockquote>
<p>PRCANTE1</p>
</blockquote></td>
<td><blockquote>
<p>PRCANTEG</p>
</blockquote></td>
<td><blockquote>
<p>PRCAOFF</p>
</blockquote></td>
<td><blockquote>
<p>PRCAOFF1</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAOFF2</p>
</blockquote></td>
<td><blockquote>
<p>PRCAOFF3</p>
</blockquote></td>
<td><blockquote>
<p>PRCAOLD</p>
</blockquote></td>
<td><blockquote>
<p>PRCAPAT</p>
</blockquote></td>
<td><blockquote>
<p>PRCAPAT1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAPAY</p>
</blockquote></td>
<td><blockquote>
<p>PRCAPAY1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAPAY2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAPAY3</p>
</blockquote></td>
<td><blockquote>
<p>PRCAPCL</p>
</blockquote></td>
<td><blockquote>
<p>PRCAPRO</p>
</blockquote></td>
<td><blockquote>
<p>PRCAPTR</p>
</blockquote></td>
<td><blockquote>
<p>PRCAQUE</p>
</blockquote></td>
<td><blockquote>
<p>PRCAREP</p>
</blockquote></td>
<td><blockquote>
<p>PRCAREPT</p>
</blockquote></td>
<td><blockquote>
<p>PRCARETN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCARFD</p>
</blockquote></td>
<td><blockquote>
<p>PRCARFD1</p>
</blockquote></td>
<td><blockquote>
<p>PRCARFD2</p>
</blockquote></td>
<td><blockquote>
<p>PRCARFD3</p>
</blockquote></td>
<td><blockquote>
<p>PRCARFP</p>
</blockquote></td>
<td><blockquote>
<p>PRCARFU</p>
</blockquote></td>
<td><blockquote>
<p>PRCARPS</p>
</blockquote></td>
<td><blockquote>
<p>PRCARPS1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCASER</p>
</blockquote></td>
<td><blockquote>
<p>PRCASER1</p>
</blockquote></td>
<td><blockquote>
<p>PRCASET</p>
</blockquote></td>
<td><blockquote>
<p>PRCASIG</p>
</blockquote></td>
<td><blockquote>
<p>PRCASVC</p>
</blockquote></td>
<td><blockquote>
<p>PRCASVC1</p>
</blockquote></td>
<td><blockquote>
<p>PRCASVC3</p>
</blockquote></td>
<td><blockquote>
<p>PRCASVC6</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PRCAUDT</p>
</blockquote></td>
<td><blockquote>
<p>PRCAUDT1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAUPD</p>
</blockquote></td>
<td><blockquote>
<p>PRCAUT1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAUT2</p>
</blockquote></td>
<td><blockquote>
<p>PRCAUT3</p>
</blockquote></td>
<td><blockquote>
<p>PRCAUTL</p>
</blockquote></td>
<td><blockquote>
<p>PRCAWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PRCAWO1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAWOF</p>
</blockquote></td>
<td><blockquote>
<p>PRCAWREA</p>
</blockquote></td>
<td><blockquote>
<p>PRCAWV</p>
</blockquote></td>
<td><blockquote>
<p>PRCAX</p>
</blockquote></td>
<td><blockquote>
<p>PRCAX1</p>
</blockquote></td>
<td><blockquote>
<p>PRCAXP</p>
</blockquote></td>
<td><blockquote>
<p>RCAM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RCAMADD</p>
</blockquote></td>
<td><blockquote>
<p>RCAMDTH</p>
</blockquote></td>
<td><blockquote>
<p>RCAMFN01</p>
</blockquote></td>
<td><blockquote>
<p>RCAMLET</p>
</blockquote></td>
<td><blockquote>
<p>RCCPW</p>
</blockquote></td>
<td><blockquote>
<p>RCCPW1</p>
</blockquote></td>
<td><blockquote>
<p>RCDPCON</p>
</blockquote></td>
<td><blockquote>
<p>RCDPCRE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RCDPDEP</p>
</blockquote></td>
<td><blockquote>
<p>RCDPDRV1</p>
</blockquote></td>
<td><blockquote>
<p>RCDPEDT</p>
</blockquote></td>
<td><blockquote>
<p>RCDPFMS</p>
</blockquote></td>
<td><blockquote>
<p>RCDPFN01</p>
</blockquote></td>
<td><blockquote>
<p>RCDPLST</p>
</blockquote></td>
<td><blockquote>
<p>RCDPUT</p>
</blockquote></td>
<td><blockquote>
<p>RCDPVDP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RCDPVW</p>
</blockquote></td>
<td><blockquote>
<p>RCEVDD1</p>
</blockquote></td>
<td><blockquote>
<p>RCEVDRV1</p>
</blockquote></td>
<td><blockquote>
<p>RCEVGEN</p>
</blockquote></td>
<td><blockquote>
<p>RCEVUTL</p>
</blockquote></td>
<td><blockquote>
<p>RCEVUTL1</p>
</blockquote></td>
<td><blockquote>
<p>RCFMCAF</p>
</blockquote></td>
<td><blockquote>
<p>RCFMDRV1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RCFMFN02</p>
</blockquote></td>
<td><blockquote>
<p>RCFMOBR</p>
</blockquote></td>
<td><blockquote>
<p>RCFMPUR</p>
</blockquote></td>
<td><blockquote>
<p>RCFMUDL</p>
</blockquote></td>
<td><blockquote>
<p>RCFN01</p>
</blockquote></td>
<td><blockquote>
<p>RCMSDD1</p>
</blockquote></td>
<td><blockquote>
<p>RCMSFN01</p>
</blockquote></td>
<td><blockquote>
<p>RCMSITE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RCMSNUM</p>
</blockquote></td>
<td><blockquote>
<p>RCNR4</p>
</blockquote></td>
<td><blockquote>
<p>RCNR4A</p>
</blockquote></td>
<td><blockquote>
<p>RCNR4P</p>
</blockquote></td>
<td><blockquote>
<p>RCNR4T</p>
</blockquote></td>
<td><blockquote>
<p>RCNRBD</p>
</blockquote></td>
<td><blockquote>
<p>RCNRBD1</p>
</blockquote></td>
<td><blockquote>
<p>RCNRSUM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RCNRSUM1</p>
</blockquote></td>
<td><blockquote>
<p>RCTRAN</p>
</blockquote></td>
<td><blockquote>
<p>RCTRAN1</p>
</blockquote></td>
<td><blockquote>
<p>RCY</p>
</blockquote></td>
<td><blockquote>
<p>RCY215</p>
</blockquote></td>
<td><blockquote>
<p>RCY21A</p>
</blockquote></td>
<td><blockquote>
<p>RCY21B</p>
</blockquote></td>
<td><blockquote>
<p>RCYAPP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RCYCPAY</p>
</blockquote></td>
<td><blockquote>
<p>RCYDD1</p>
</blockquote></td>
<td><blockquote>
<p>RCYDD2</p>
</blockquote></td>
<td><blockquote>
<p>RCYE</p>
</blockquote></td>
<td><blockquote>
<p>RCYHLP</p>
</blockquote></td>
<td><blockquote>
<p>RCYLT</p>
</blockquote></td>
<td><blockquote>
<p>RCYPT</p>
</blockquote></td>
<td><blockquote>
<p>RCYPT2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RCYPT3</p>
</blockquote></td>
<td><blockquote>
<p>RCYPT4</p>
</blockquote></td>
<td><blockquote>
<p>RCYREC</p>
</blockquote></td>
<td><blockquote>
<p>RCYTRA</p>
</blockquote></td>
<td><blockquote>
<p>RCYUT</p>
</blockquote></td>
<td><blockquote>
<p>RCYVOI</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>414 routines.</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> March 1995 AR V. 4.5 Installation Guide 21

> Routine List

> 22 AR V. 4.5 Installation Guide March 1995

# Recompiled Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Recompile Templates on all Systems; if the routines in the UCI where the PRCAINITS were run are not reachable by other UCIs, it is necessary to recompile all templates using the routine PRCACV10.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### \>D ^PRCACV10

> Select Routine Size: (3000-5000): 4000//

> Template PRCA BATCH PAYMENT Compiling to Routine PRCATB Compiling PRCA BATCH PAYMENT input template of File 433.....

> 'PRCATB' ROUTINE FILED....

> 'PRCATB1' ROUTINE FILED

> Template PRCASV REL Compiling to Routine PRCATSE Compiling PRCASV REL input template of File 430....

> 'PRCATSE' ROUTINE FILED....

> 'PRCATSE1' ROUTINE FILED.

> Template PRCA OLD SET Compiling to Routine PRCATA Compiling PRCA OLD SET input template of File 430...

> 'PRCATA' ROUTINE FILED....

> 'PRCATA1' ROUTINE FILED.........

> 'PRCATA2' ROUTINE FILED....

> 'PRCATA4' ROUTINE FILED..........

> 'PRCATA3' ROUTINE FILED...

> Template PRCA SET Compiling to Routine PRCATE Compiling PRCA SET input template of File 430...

> 'PRCATE' ROUTINE FILED...

> 'PRCATE1' ROUTINE FILED.........

> 'PRCATE2' ROUTINE FILED.....

> 'PRCATE3' ROUTINE FILED....

> Template PRCA 3RD PROFILE Compiling to routine PRCATP5

> Compiling PRCA 3RD PROFILE print template of File 430............

> ........................................... 'PRCATP5' ROUTINE FILED..............

> Template PRCA DISP ADJ Compiling to routine PRCATO4

> Compiling PRCA DISP ADJ print template of File 433...............

> 'PRCATO4' ROUTINE FILED......

> Template PRCA DISP AUDIT Compiling to routine PRCATO2

> Compiling PRCA DISP AUDIT print template of File 430.............

> .......................... 'PRCATO2' ROUTINE FILED............

> Template PRCA DISP CARE Compiling to routine PRCATO5

> Compiling PRCA DISP CARE print template of File 433..............

> 'PRCATO5' ROUTINE FILED...

> March 1995 AR V. 4.5 Installation Guide 23

> Recompiled Templates

> Template PRCA FMS STATUS Compiling to routine PRCATF

> Compiling PRCA FMS STATUS print template of File 347..............

> 'PRCATF' ROUTINE FILED...

> Template PRCA FMS TRANS STAT Compiling to routine PRCATF2

> Compiling PRCA FMS TRANS STAT print template of File 347..............

> 'PRCATF2' ROUTINE FILED...

> Template PRCA MEANS PROFILE Compiling to routine PRCATP2 Compiling PRCA MEANS PROFILE print template of File 430..........

> 'PRCATP2' ROUTINE FILED.........

> Template PRCA OTHER PROFILE Compiling to routine PRCATP4 Compiling PRCA OTHER PROFILE print template of File 430..........

> 'PRCATP4' ROUTINE FILED.......

> Template PRCA PROFILE Compiling to routine PRCATP1

> Compiling PRCA PROFILE print template of File 430................

> 'PRCATP1' ROUTINE FILED........

> Template PRCA TRANS PROFILE Compiling to routine PRCATR3 Compiling PRCA TRANS PROFILE print template of File 433..........

> 'PRCATR3' ROUTINE FILED.......

> Template PRCA VENDOR PROFILE Compiling to routine PRCATP3 Compiling PRCA VENDOR PROFILE print template of File 430.........

> ............................. 'PRCATP3' ROUTINE FILED.............

> Template PRCAA AMEND AUDIT Compiling to routine PRCATR2

> Compiling PRCAA AMEND AUDIT print template of File 430...........

> 'PRCATR2' ROUTINE FILED.........

> Template PRCAC TR LIST Compiling to routine PRCATW1 Compiling PRCAC TR LIST print template of File 433..........

> 'PRCATW1' ROUTINE FILED.

> Template PRCAP CARE WV Compiling to routine PRCATW3

> Compiling PRCAP CARE WV print template of File 433..............

> 'PRCATW3' ROUTINE FILED...

> Template PRCAP COST Compiling to routine PRCATO3

> Compiling PRCAP COST print template of File 433..................

> 'PRCATO3' ROUTINE FILED.....

> Template PRCAP DEBTOR LOCATE Compiling to routine PRCATO9 Compiling PRCAP DEBTOR LOCATE print template of File 430.........

> ............................. 'PRCATO9' ROUTINE FILED.......

> Template PRCAP REPAYMENT Compiling to routine PRCATR1

> Compiling PRCAP REPAYMENT print template of File 430.............

> 'PRCATR1' ROUTINE FILED.....

> 24 AR V. 4.5 Installation Guide March 1995

Recompiled Templates

> Template PRCAP RETURN BILL Compiling to routine PRCATP6

> Compiling PRCAP RETURN BILL print template of File 430.............

> 'PRCATP6' ROUTINE FILED.....

> Template PRCAP WAIVED Compiling to routine PRCATW2

> Compiling PRCAP WAIVED print template of File 433................

> 'PRCATW2' ROUTINE FILED....

> Template PRCARFD Compiling to routine PRCATRF

> Compiling PRCARFD print template of File 430................

> 'PRCATRF' ROUTINE FILED....

> Template PRCAT DISP CP Compiling to routine PRCATO8

> Compiling PRCAT DISP CP print template of File 430...............

> 'PRCATO8' ROUTINE FILED....

> Template PRCAT NEW AR Compiling to routine PRCATP7

> Compiling PRCAT NEW AR print template of File 430................

> .............

> 'PRCATP7' ROUTINE FILED.....

> Template PRCAT NEW TRANS Compiling to routine PRCATP9

> Compiling PRCAT NEW TRANS print template of File 433.............

> 'PRCATP9' ROUTINE FILED.......

> \>

> March 1995 AR V. 4.5 Installation Guide 25

> Recompiled Templates

> 26 AR V. 4.5 Installation Guide March 1995