---
title: FB*3.5*116 Release Notes and Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Release Notes and
app_code: FB
app_name: Fee Basis
section: FIN
app_status: active
pkg_ns: FB
patch_ver: 3.5
patch_id: FB*3.5*116
group_key: "FB:FB:3.5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - payment
  - batch
  - table
  - contents
  - line
  - zero
  - dollar
  - patch
  - invoices
  - items
page_count: 0
word_count: 2648
section_count: 8
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fb_35_116_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fb_35_116_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=40"
---

Fee Basis

Report Zero Dollar Line Items

![](fb-3-5-116-release-notes-and-installation-guide/001.png)

Release Notes and Installation Guide

FB\*3.5\*116

February 2011

Veterans Affairs

Product Development (PD)

######## Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Overview](#overview)
  - [Patch FB\3.5\116 includes the following modifications:](#patch-fb35116-includes-the-following-modifications)
    - [Allow zero dollar line items to be exported to Central Fee.](#allow-zero-dollar-line-items-to-be-exported-to-central-fee)
    - [EDI invoices are sent to FPPS only when payment results are received](#edi-invoices-are-sent-to-fpps-only-when-payment-results-are-received)
    - [Include the payment lines that have \$0.00 amount paid in the payment line count of a given batch](#include-the-payment-lines-that-have-000-amount-paid-in-the-payment-line-count-of-a-given-batch)
    - [Prevent Medical Fee and Pricer Exempt Civil Hospital payment batches from being closed when zero dollar (\$0.00) amount paid invoice(s) exist on the batch](#prevent-medical-fee-and-pricer-exempt-civil-hospital-payment-batches-from-being-closed-when-zero-dollar-000-amount-paid-invoices-exist-on-the-batch)
    - [Prevent Pricer Non-Exempt Civil Hospital payment batches being released when zero dollar (\$0.00) amount paid invoice(s) exist on the batch.](#prevent-pricer-non-exempt-civil-hospital-payment-batches-being-released-when-zero-dollar-000-amount-paid-invoices-exist-on-the-batch)
    - [Prevent batch assignment to Pharmacy invoices that have been entered as zero dollar (\$0.00) amount paid](#prevent-batch-assignment-to-pharmacy-invoices-that-have-been-entered-as-zero-dollar-000-amount-paid)
    - [Prompt so that the user can identify if the payment lines are to be subject to interest penalty payments](#prompt-so-that-the-user-can-identify-if-the-payment-lines-are-to-be-subject-to-interest-penalty-payments)
    - [An environment check routine will prevent the patch being installed if batches with \$0 invoices exist](#an-environment-check-routine-will-prevent-the-patch-being-installed-if-batches-with-0-invoices-exist)
    - [Overview of New Service Request (NSR)](#overview-of-new-service-request-nsr)
    - [Overview of Remedy Tickets](#overview-of-remedy-tickets)
  - [Documentation Retrieval](#documentation-retrieval)
  - [Test Sites](#test-sites)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Installation Instructions](#installation-instructions)
- [Enhancements](#enhancements)
- [Technical Modifications](#technical-modifications)
  - [A. Files and Fields](#a-files-and-fields)
    - [Components Sent With Patch:](#components-sent-with-patch)
The Chief Business Office (CBO) is requesting an enhancement to the VistA Fee Basis package that will report zero dollar line items at local Fee and national systems. Although VistA Fee Basis captures lines items that are not reimbursed (zero line items), these line items are not transmitted to national financial processing systems as these systems have not been designed to process zero dollar line items.  Consequently, these line items are not included in workload reporting; and since the remittance advice and explanation of benefits provided to non-VA health care providers does not include zero dollar line items, they are not HIPAA compliant.
Enhancements to the existing VistA Fee Basis software application will allow for transmittal of payment line items that have \$0.00 AMOUNT PAID.  The Central Fee system located at the Austin Information Technology Center (AITC) and the Fee Payment Processing System (FPPS) located at the Health Administration Center (HAC) are the external systems that will need to be able to receive and process the zero dollar line items.
> **WARNING:** If your site is using the Fee Basis Claims System (FBCS), you must install DSIF\*3.2\*10 immediately after installing FB\*3.5\*116 to avoid application/processing errors.  If your site is not using FBCS there is no need to install the FBCS patch.

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although the pre-patch FB\*3.5\*116 version of Fee Basis allows payment entry of \$0.00 payment line items, the \$0.00 line items are not exported to Austin. Once a site installs FB\*3.5\*116 (and DSIF\*3.2\*10 if FBCS is installed), the payment of \$0.00 line items will be allowed to continue, and additionally (with the new enhancements) local Fee will begin to export \$0.00 payment lines to Austin. However, even though an invoice can have a subset of zero dollar payment lines the entire invoice needs to be greater than \$0.00 amount paid. This is due to the fact that Central Fee in Austin will not process invoices that total \$0.00 (as these are considered denied claims). To prevent transmission of payment batches that have invoices totaling \$0.00, the Fee enhancements include preventing a batch to be released or closed if \$0.00 invoices exist.

## Patch FB\*3.5\*116 includes the following modifications:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Allow zero dollar line items to be exported to Central Fee.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Queue Data for Transmission \[FBAA QUEUE DATA FOR TRANS.\] - transmits to Central Fee in Austin FEE payments and Master Record Adjustments (MRA) using Mailman.  The software that supports this option was modified to remove the software that prevented the zero dollar amount paid line items being exported to Central Fee.

### EDI invoices are sent to FPPS only when payment results are received

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Release a Batch \[FBAA SUPERVISOR RELEASE\] - Releases a payment batch that is ready to be transmitted to Central Fee.  Since the systematic queue of EDI invoices with \$0.00 line items gets performed when VistA receives the payment confirmation/cancellation results from Central Fee, the Release a Batch software was modified to no longer queue EDI invoices with a total amount paid of \$0.00 to the FPPS QUEUED INVOICES file (#163.5).

### Include the payment lines that have \$0.00 amount paid in the payment line count of a given batch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As there are restrictions on the size of a batch that Central Fee can receive and process, the software that supports the payment processing options was modified to include the payment lines that have \$0.00 amount paid in the payment line count of a given batch.  The count value is populated in the PAYMENT LINE COUNT field (#161.7, 10) of the FEE BASIS BATCH file.

### Prevent Medical Fee and Pricer Exempt Civil Hospital payment batches from being closed when zero dollar (\$0.00) amount paid invoice(s) exist on the batch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Close-out Batch \[FBAA CLOSE-OUT BATCH\] option was modified to prevent Medical Fee and Pricer Exempt Civil Hospital payment batches from being closed when zero dollar (\$0.00) amount paid invoice(s) exist on the batch. The batch will remain in the "OPEN" status until the zero dollar invoice(s) have been removed from the batch or corrected to reflect non-zero dollar line items.

### Prevent Pricer Non-Exempt Civil Hospital payment batches being released when zero dollar (\$0.00) amount paid invoice(s) exist on the batch.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Release a Batch \[FBAA SUPERVISOR RELEASE\] option was modified to prevent Pricer Non-Exempt Civil Hospital payment batches being released when zero dollar (\$0.00) amount paid invoice(s) exist on the batch. The batch will remain in the "ASSIGNED PRICE" status until the zero dollar invoice(s) have been removed from the batch or corrected to reflect non-zero dollar line items.

### Prevent batch assignment to Pharmacy invoices that have been entered as zero dollar (\$0.00) amount paid 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Closeout Pharmacy Invoice \[FBAA CLOSE OUT INVOICE\] option was be modified to prevent batch assignment to Pharmacy invoices that have been entered as zero dollar (\$0.00) amount paid. The Line Item Status on the Pharmacy invoice will remain in "Pending Payment Process" until the zero dollar amount paid line item(s) are removed from the invoice or is corrected to reflect non-zero dollar.

### Prompt so that the user can identify if the payment lines are to be subject to interest penalty payments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The payment software issues a prompt so that the user can identify if the payment lines are to be subject to interest penalty payments. The options that process the entry and edit of Medical Fee payments and Ancillary payments were modified to no longer gather interest indicators at the payment line level. This means that the user interface prompt, "Is this line item for a contracted service?", will no longer be issued for each payment line. Line items for contracted services will now reflect the interest indicator as it was answered at the invoice level. The PROMPT PAY TYPE field (#34) of the FEE BASIS PAYMENT (#162) file will get populated with the interest indicator value captured at the invoice level for proper processing at the Central Fee system and the Financial Management System (FMS).

### An environment check routine will prevent the patch being installed if batches with \$0 invoices exist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Fee Basis patch FB\*3.5\*116 has an environment check routine that checks for batches that are "in-process". Batches with a status of ‘CLERK CLOSED', 'SUPERVISOR CLOSED' and 'REVIEWED AFTER PRICER' are examined to determine if zero dollar (\$0.00) amount paid invoices exist. If it is determined that "in-process" batches exist, then the installation of FB\*3.5\*116 will terminate; an abort message is generated and displayed to the installer of the patch; a Mailman bulletin will be generated that will identify the batches with \$0.00 invoices; and the bulletin will be sent to the FEE mail group. Until further action is performed by the Fee staff, the patch cannot be installed.

Please refer to the instructions in the pre/post installation section to apply the proper action to the batches identified in the Mailman bulletin.

### Overview of New Service Request (NSR)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

20090614 - Fee Basis \$0.00 Line Item Data Enhancement

### Overview of Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Remedy tickets have been addressed as part of patch FB\*3.5\*116

## Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may retrieve documentation in one of the following ways:

 

 1.  The preferred method is to FTP the files from REDACTED, which will transmit the files from the first available FTP server.
 2.  Sites may also elect to retrieve documentation directly from a specific server as follows:

 

     Albany          REDACTED

     Hines           REDACTED

     Salt Lake City  REDACTED

| FILE NAME               | DESCRIPTION |
|-----------------------------|-----------------|
| fb_35_116_rn.pdf            | Release Notes   |
| fb_35_um1_revised_feb11.pdf | User Manual     |
| fb_35_um2_revised_feb11.pdf | User Manual     |
| fb_35_um3_revised_feb11.pdf | User Manual     |

 3.  Documentation can also be retrieved from the VistA Documentation Library (VDL) on the Internet at the following address, <http://www.va.gov/vdl/application.asp?appidequals40>.

 

The documentation distribution includes:

 

| FILE NAME    | DESCRIPTION |
|------------------|-----------------|
| fb_35_116_rn.pdf | Release Notes   |
| fb_35_um1.doc    | User Manual     |
| fb_35_um2.doc    | User Manual     |
| fb_35_um3.doc    | User Manual     |

## Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installation 

 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before FB\*3.5\*116

> FB\*3.5\*67

> FB\*3.5\*77

> FB\*3.5\*79

> FB\*3.5\*98

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An environmental check routine is executed before the patch is installed and will report any \$0.00 invoices that exist. As well, the installation of the patch will not be performed until these batches are resolved. The following steps provide instruction on how to resolve the batches with the 0.00 invoices.

1.  Run the Queue Data for Transmission \[FBAA QUEUE DATA FOR TRANS.\] option to transmit any pending payment batches.
2.  Before installing the patch confirm you are enrolled in the FEE mail group.
3.  Install the patch. 
4.  If the patch gets installed successfully then there were no \$0.00 invoices found so further action is not necessary and you can stop here.
5.  If there are \$0.00 invoices in the system the patch installation will terminate and a Mailman bulletin that identifies the batches with \$0.00 invoices is sent to the recipients of the FEE mail group.
6.  Use the Status of Batch \[FBAA BATCH STATUS\] option to examine each batch listed in the Mailman bulletin and take <u>one</u> of the following actions to resolve:  
1.  If the batch STATUS equals CLERK CLOSED then use the Re-Open Batch \[FBAA REOPEN BATCH\] option to change the STATUS to OPEN and move on to the next batch. Note that the security key FBAASUPERVISOR is needed to re-open a batch if you are not the clerk that originally opened it.
2.  If the batch STATUS equals SUPERVISOR CLOSED, and TOTAL DOLLARS equals 0, and the batch is not a civil hospital non-exempt batch then use FILEMAN ENTER/EDIT to change the STATUS to OPEN and move on to the next batch. Note: A civil hospital non-exempt batch will have TYPE equals CH/CNH and CONTRACT HOSPITAL BATCH equals yes and BATCH EXEMPT not equal YES.
3.  If the batch STATUS equals REVIEWED AFTER PRICER and the TOTAL DOLLARS equals 0 then use FILEMAN ENTER/EDIT to change the STATUS to ASSIGNED PRICE and move on to the next batch.
7.  It should be possible to install the patch after the above steps are taken to resolve any issues reported by the environment check. 
8.  After the patch is installed, inform fee staff of any changes made to batch statuses so those batches can be appropriately processed.
9.  Fee staff should take appropriate action to edit or remove the \$0 invoices and process the payment batches.

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If installed during the normal workday, it is recommended that the following selection(s) in the OPTION (#19) file be disabled to prevent possible conflicts while running the KIDS Install. Other VISTA users will not be affected.

 

> Payment Process Menu \[FBCH PAYMENT MENU\]

> Payment menu \[FBAA PAYMENT MENU\]

> Payments for Unauthorized Claims \[FBUC PAYMENTS\]

> Batch Main Menu - CH \[FBCH BATCH OPTIONS\]

> Batch Main Menu \[FBAA BATCH MENU\]

> Batch Menu - Pharmacy \[FBAA PHARMACY BATCH OPTIONS\]

> Release a Batch \[FBAA SUPERVISOR RELEASE\]

> Queue Data for Transmission \[FBAA QUEUE DATA FOR TRANS.\]

 

Install Time - less than 5 minutes

 

*1.  LOAD TRANSPORT GLOBAL*

    Choose the PackMan message containing this patch and invoke the

 

    INSTALL/CHECK MESSAGE PackMan option.

 

*2.  START UP KIDS*

    Start up the Kernel Installation and Distribution System Menu

 

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

 

*3.  Select Installation Option:*

> **NOTE:** The following are OPTIONAL - (When prompted for the INSTALL NAME, enter FB\*3.5\*116):

 

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed.  It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

*4. Select Installation Option: Install Package(s)*

\*\*This is the step to start the installation of this KIDS patch:

1.  Choose the Install Package(s) option to start the patch install.
2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' Answer NO if your system does this in a nightly TaskMan process. (Answering YES can increase the installation time.)
3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO
4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//' answer YES
5.  When prompted 'Enter options you wish to mark as 'Out Of Order':' Enter the following options:

> Payment Process Menu \[FBCH PAYMENT MENU\]

> Payment menu \[FBAA PAYMENT MENU\]

> Payments for Unauthorized Claims \[FBUC PAYMENTS\]

> Batch Main Menu - CH \[FBCH BATCH OPTIONS\]

> Batch Main Menu \[FBAA BATCH MENU\]

> Batch Menu - Pharmacy \[FBAA PHARMACY BATCH OPTIONS\]

> Release a Batch \[FBAA SUPERVISOR RELEASE\]

> Queue Data for Transmission \[FBAA QUEUE DATA FOR TRANS\]

6.  When prompted 'Enter protocols you wish to mark as 'Out Of Order':' press \<return\>.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

.

The following enhancements are delivered with FB\*3.5\*116:

- Payment line items having an amount approved of zero dollars are exported to the financial systems in Austin.
- Payment line items for contracted services will now reflect the interest indicator at the invoice level.

# Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## A. Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Components Sent With Patch:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software supporting the following options was modified:

 

Queue Data for Transmission \[FBAA QUEUE DATA FOR TRANS\]

Release a Batch \[FBAA SUPERVISOR RELEASE\]

Enter Payment \[FBAA ENTER PAYMENT\]

C&P/Multiple Patient Payment Entry \[FBAA C&P ENTER PAYMENT\]

Multiple Ancillary Payments \[FBCH MULTIPLE PAYMENTS\]

Multiple Payment Entry \[FBAA MULTIPLE PAYMENT ENTRY\]

Payments for Unauthorized Claims \[FBUC PAYMENTS\]

Close-out Batch \[FBAA CLOSE BATCH\]

Closeout Pharmacy Invoice \[FBAA CLOSE OUT INVOICE\]

List Items in Batch \[FBAA LIST BATCH\]

Ancillary Contract Hosp/CNH Payment \[FBCH ANCILLARY PAYMENT\]

Edit Ancillary Payment \[FBCH EDIT ANCILLARY PAYMENT\]

Edit Payment \[FBAA EDIT PAYMENT\]