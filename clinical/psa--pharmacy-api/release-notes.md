---
title: Drug Accountability/Inventory Interface Version 3 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: PSA
app_name: "Pharmacy: Drug Accountability"
section: CLI
app_status: active
pkg_ns: PSA
patch_ver: 3
patch_id: PSA*3
group_key: "PSA:PSA:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - drug
  - invoice
  - price
  - invoices
  - order
  - reorder
  - location
  - unit
page_count: 0
word_count: 1885
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Drug_Accountability/da_3_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Drug_Accountability/da_3_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=87"
---

![](drug-accountability-inventory-interface-version-3-release-notes/001.png)

DRUG ACCOUNTABILITY/INVENTORY INTERFACE(DA)RELEASE NOTES

October 1997

Office of Chief Information Officer

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Intranet](#intranet)
- [New Functionality](#new-functionality)
  - [New Options](#new-options)
    - [Upload and Process Prime Vendor Invoice Data](#upload-and-process-prime-vendor-invoice-data)
    - [Process Uploaded Prime Vendor Invoice Data](#process-uploaded-prime-vendor-invoice-data)
    - [\[PSA PROCESS PRIME VENDOR DATA\]](#psa-process-prime-vendor-data)
    - [Verify Invoices](#verify-invoices)
    - [\[PSA VERIFY INVOICES\]](#psa-verify-invoices)
    - [Print Orders](#print-orders)
    - [\[PSA PRINT ORDERS\]](#psa-print-orders)
    - [Credit Resolution](#credit-resolution)
    - [\[PSA CREDIT RESOLUTION\]](#psa-credit-resolution)
    - [### Enter/Edit Stock and Reorder Levels](#enteredit-stock-and-reorder-levels)
    - [\[PSA STOCK AND REORDER LEVELS\]](#psa-stock-and-reorder-levels)
    - [Transfer Drugs Between Pharmacies](#transfer-drugs-between-pharmacies)
    - [\[PSA TRANSFER DRUGS\]](#psa-transfer-drugs)
  - [Modified Options](#modified-options)
    - [Set Up/Edit a Pharmacy Location](#set-upedit-a-pharmacy-location)
    - [\[PSA LOCATION EDIT\]](#psa-location-edit)
    - [Receiving Directly into Drug Accountability](#receiving-directly-into-drug-accountability)
    - [\[PSA RECEIVING\]](#psa-receiving)
  - [Modified Reports](#modified-reports)
    - [Balance Adjustments History](#balance-adjustments-history)
    - [\[PSA BALANCE ADJUSTMENTS REPORT\]](#psa-balance-adjustments-report)
    - [Drug Balances by Location](#drug-balances-by-location)
    - [\[PSA DISPLAY LOCATION\]](#psa-display-location)
    - [Drug Transaction History](#drug-transaction-history)
    - [\[PSA DRUG DISPLAY\]](#psa-drug-display)
    - [Monthly Summary](#monthly-summary)
    - [\[PSA MONTHLY SUMMARY\]](#psa-monthly-summary)
  - [New Report](#new-report)
    - [Transfer Signature Sheet](#transfer-signature-sheet)
    - [\[PSA TRANSFER SIGNATURE SHEET\]](#psa-transfer-signature-sheet)
  - [New Prime Vendor Interface Reports](#new-prime-vendor-interface-reports)
    - [Invoice Cost Summary](#invoice-cost-summary)
    - [\[PSA INVOICE COST SUMMARY\]](#psa-invoice-cost-summary)
    - [Outstanding Credits](#outstanding-credits)
    - [\[PSA OUTSTANDING CREDITS\]](#psa-outstanding-credits)
    - [Processor and Verifier](#processor-and-verifier)
    - [\[PSA PROCESSOR AND VERIFIER\]](#psa-processor-and-verifier)
    - [Stock and Reorder Level](#stock-and-reorder-level)
    - [\[PSA STOCK & REORDER LEVEL RPT\]](#psa-stock-reorder-level-rpt)
- [New MailMan Messages](#new-mailman-messages)
    - [Drug Transfer Between Pharmacies](#drug-transfer-between-pharmacies)
    - [Unprocessed Invoices Due to Expire in \# days](#unprocessed-invoices-due-to-expire-in-days)
    - [Drug Balances Below Reorder Level](#drug-balances-below-reorder-level)
  - [Modified Mail Message](#modified-mail-message)
    - [DRUG file Price/NDC Update](#drug-file-pricendc-update)
> These release notes provide a brief description of the changes in Version 3.0 of the Drug Accountability/Inventory Interface (DA) software package. In addition to the release notes, it is highly recommended that you also read the User Manual, Installation Guide, and Technical Manual/Security Guide provided with Version 3.0. These manuals have been rewritten to include essential information related to the enhancements and modifications described here.
> This version of the Drug Accountability/Inventory Interface software package can only be run with a standard MUMPS operating system. It also requires the following VA software applications.
> <u>Application</u> <u>Minimum Version Required</u>
Controlled Substances 3.0 (Must be patched
up to and including
Patch PSD\*3.0\*6)
Kernel 8.0
Kernel Toolkit 7.3
MailMan 7.1
VA FileMan 21.0
National Drug File (NDF) 3.16
Pharmacy Data Management (PDM) 1.0
Inpatient Medications 4.5 (Must be patched up to and including Patch PSJ\*4.5\*44)
Automatic Replenishment/Ward Stock 2.3
Outpatient Pharmacy 6.0 (Must be patched up to and including Patch PSO\*6.0\*155)
If the site will be setting up an Inpatient and/or Combined (Inpatient/
Outpatient) pharmacy location, these software packages must be installed to collect unit dose and IV dispensing data.
If the site will be setting up an Outpatient and/or Combined (Inpatient/
outpatient) pharmacy location, this software package must be installed to collect prescription data.
<u>Commercial Software Package</u><u>Required Version</u>
<span class="smallcaps">procomm plus®</span> 2.01
> The <span class="smallcaps">procomm plus®</span> software is not included in this package. It MUST BE INSTALLED to ensure complete functionality of the prime vendor interface.

# Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Documentation for this product can now be found on the intranet. You will find it at the following address:

> http://www.vista.med.va.gov/softserv/clin_bro.ad/index.html

> This address will take you to the Clinical Products page where you will find a listing of all the clinical software manuals. Click on the Drug Accountability Prime Vendor Interface (DA) link and it will take you to the DA Homepage. You can also get there by going straight to the following address:

> http://www.vista.med.va.gov/softserv/clin_nar.row/pharmda/index.html

> ![](drug-accountability-inventory-interface-version-3-release-notes/002.png) Remember to bookmark this site for future reference.

# New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Orders Menu*

> *1 Upload and Process Prime Vendor Invoice Data*

> *2 Process Uploaded Prime Vendor Invoice Data*

> *3 Verify Invoices*

> *4 Print Orders*

> *5 Credit Resolution*

### Upload and Process Prime Vendor Invoice Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSA UPLOAD PRIME VENDOR DATA\]

> The invoice data received from the prime vendor is placed on Pharmacy’s prime vendor PC. This new option *must* be executed on Pharmacy’s prime vendor PC while using <span class="smallcaps">procomm plus®</span> for DOS V. 2.01. It uploads the invoice data into V*IST*A. If no problems are found, the invoice data is deleted from the prime vendor Personal Computer (PC). After the data is uploaded, the user may process the data now or exit the option and process it through the *Process Uploaded Prime Vendor Invoice Data* \[PSA PROCESS PRIME VENDOR DATA\] option. It also allows the user to print all invoices that are not processed immediately following the upload and immediately following the processing.

### Process Uploaded Prime Vendor Invoice Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA PROCESS PRIME VENDOR DATA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The uploaded invoices are given their first quality control pass. The software automatically matches the invoice line items to drugs in the DRUG file (#50) using its National Drug Code (NDC). If no match exists, the NATIONAL DRUG file (#50.6) is searched for the NDC. If it is found, the VA product name for the NDC is located. The DRUG file (#50) is then searched for all drugs with that VA product name. The drugs are displayed for user selection. If none are selected, the user may select one from the DRUG file (#50) or enter the name of the supply item. Supply items are items that will never be in the DRUG file (#50) such as Rx bottles. All line item data is verified to be correct or the user enters an adjustment. The user can choose to change the invoice’s status to “Processed” or wait until he/she is sure all line items are correct. Once the status has been changed, it is forwarded to a verifier.

### Verify Invoices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA VERIFY INVOICES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The processed invoices are verified by a person holding the PSA ORDERS key. This person cannot be the same person who processed the invoice. Also, if the invoice contains at least one drug marked as a controlled substance, the verifier must also hold the PSJ RPHARM key. The verifier is ultimately responsible for the correctness of the invoice. He/she verifies the processed data is correct and basically signs off on the invoice. When the invoices are verified, the drug balances are updated in the pharmacy location and/or master vault.

> **IMPORTANT:** Once verified, the drug balances are incremented in the pharmacy location and/or master vault. The invoiced drug’s order unit is compared to the ORDER UNIT field (#12) in the DRUG file (#50) and the dispense units per order unit is compared to the DISPENSE UNITS PER ORDER UNIT field (#15) in the DRUG file (#50). If the order unit and dispense units per order unit are the same, the NDC (#31), price per order unit (#13), and price per dispense unit (#16) fields in the DRUG file (#50) may be updated.

The following condition must be met to update the NDC field (#31).

- If the invoice NDC is different from the NDC field (#31), the NDC field (#31) is overwritten with the invoiced NDC.

  The following condition must be met to update the price per order unit field (#13) and price per dispense unit field (#16).
- If the invoiced price per order unit is different than the price per order unit field (#13), the price per order unit field (#13) is overwritten with the new prorated price per order unit. The price per dispense unit field (#16) is also overwritten with the new prorated price per dispense unit.

### Print Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA PRINT ORDERS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Invoices can be printed by selecting the order number, invoice number, or invoice status. If there are more invoices for the order, they are not printed. If the invoice has not been processed, the PRIME VENDOR UPLOAD REPORT prints. If the invoice has been processed, the PRIME VENDOR ORDER REPORT prints.

- If the order number is selected, all invoices for that order print.
- If the invoice number is selected, both the order and invoice numbers must be entered. The same invoice number may be assigned to many order numbers by the prime vendor. Only the selected invoice is printed.
- If the invoice status is selected, the user may print all invoices with either a status of “Uploaded” (unprocessed) or “Processed.”

### Credit Resolution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA CREDIT RESOLUTION\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When an invoice is received, it is checked against what was actually received. If there is missing or damaged items, incorrect items, etc., the vendor will need to issue a credit. When the credit memo is received, it can be entered into DA and the outstanding credit will be removed.

### ### Enter/Edit Stock and Reorder Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA STOCK AND REORDER LEVELS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pharmacy locations or master vaults can be flagged to maintain stock and reorder levels for all their drugs. The stock level is the ideal number of dispense units the pharmacy location or master vault is to have on its shelf. The reorder level is the least number of dispense units to be kept on the shelf. When a drug reaches the reorder level, it is time to place an order for more. By setting the flag and entering the stock and reorder levels, the holders of the PSA ORDERS key will receive the “Drug Balances Below Reorder Level” mail message every morning. It lists the pharmacy locations’ and master vaults’ drugs that are less than their reorder levels. It also lists each of these drugs’ current balance, reorder level, and number of dispense units that need to be ordered to bring the balance up to the stock level. The flag may be set in the *Set Up/Edit aPharmacy Location* \[PSA LOCATION EDIT\] or *Enter/Edit Stock and Reorder Levels* \[PSA STOCK AND REORDER LEVELS\] option. The stock and reorder levels may be entered through the *Enter/Edit Stock and Reorder Levels* \[PSA STOCK AND REORDER LEVELS\] option or when prompted during processing and verification. For a master vault, only pharmacist holding the PSJ RPHARM key can set the flag, set the stock and reorder levels, and receive controlled substances data on the mail message.

### Transfer Drugs Between Pharmacies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA TRANSFER DRUGS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Drugs may now be transferred between pharmacy locations by a pharmacist holding the PSAMGR and PSJ RPHARM keys. The number of dispense units to be moved is subtracted from the dispensing pharmacy location and added to the receiving pharmacy location. A DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET may be printed after all transfers are completed.

## Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Set Up/Edit a Pharmacy Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA LOCATION EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Functionality has been added to this option depending on which interface the site is using.

> <u>New GIP and Prime Vendor Interface Functionality:</u>

- Links IV rooms to an outpatient pharmacy location. IV statistics are collected in a nightly job.
- Enters or deletes the date the pharmacy location is inactivated.

  <u>New Prime Vendor Interface ONLY:</u>
- Enters the “Maintain reorder levels” flag.
- Enters the number of days to keep invoice data in the DRUG ACCOUNTABILITY ORDERS file (#58.811).

### Receiving Directly into Drug Accountability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA RECEIVING\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Receiving prime vendor Integrated Funds Distribution, Control Point Activity, Accounting and Procurement (IFCAP), or non-traditional IFCAP receipts has added functionality.

> **IMPORTANT:** Once received, the drug balances are incremented in the pharmacy location and/or master vault. The invoiced drug’s order unit is compared to the ORDER UNIT field (#12) in the DRUG file (#50) and the dispense units per order unit is compared to the DISPENSE UNITS PER ORDER UNIT field (#15) in the DRUG file (#50). If the order unit and dispense units per order unit are the same, the NDC (#31), price per order unit (#13), and price per dispense unit (#16) fields in the DRUG file (#50) may be updated.

The following condition must be met to update the NDC field (#31).

- If the invoice NDC is different from the NDC field (#31), the NDC field (#31) is overwritten with the invoiced NDC.

  The following condition must be met to update the price per order unit field (#13) and price per dispense unit field (#16).
- If the invoiced price per order unit is different than the price per order unit field (#13), the price per order unit field (#13) is overwritten with the new prorated price per order unit. The price per dispense unit field (#16) is also overwritten with the new prorated price per dispense unit.

## Modified Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Balance Adjustments History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA BALANCE ADJUSTMENTS REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The “HISTORY OF ADJUSTMENTS AND TRANSFERS” report that is available in the *Balance Adjustment* \[PSA BALANCE ADJUSTMENTS\] option is also available in this option on the *Maintenance Reports Menu* \[PSA PV MAINTENANCE RPT MENU\] and \[PSA GIP MAINTENANCE RPT MENU\]. The “HISTORY OF BALANCE ADJUSTMENTS” report was modified to include the drug transfer history. It lists the adjustment/transfer date and time, quantity, transactor, and reason.

### Drug Balances by Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA DISPLAY LOCATION\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The “DRUG BALANCES BY LOCATION REPORT” has been modified to include the total number of dispense units for a drug that is on the system. This figure is taken from the CURRENT INVENTORY field (#50) in the DRUG file (#50).

### Drug Transaction History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA DRUG DISPLAY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The “HISTORY OF DRUG TRANSACTIONS” report was modified to list the Inpatient and Outpatient dispensing separately. Drug transfers are now listed in the adjustment column. The adjusted item’s reason allows the user to distinguish if the item is an adjustment or a transfer. If the history shows a receipt, the order number is printed. The total receipts, total dispensed by Inpatient Medications, total dispensed by Outpatient Pharmacy, and total adjustments and transfers are printed for each drug.

### Monthly Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA MONTHLY SUMMARY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The “MONTHLY SUMMARY” report was modified to include transfer data. The user is asked if a summary report for the selected drugs should be printed.

- If so, the detailed report prints and is followed by a summary report. The summary report includes the drug name, total receipts, total dispensed, total adjusted, and total transferred for each drug in all selected pharmacy locations. At the end of the summary report, a grand total line prints the grand total receipts, dispensed, adjusted, and transferred.
- If no, the detailed report prints.

## New Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Transfer Signature Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA TRANSFER SIGNATURE SHEET\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The “DRUG TRANSFER BETWEEN PHARMACIES SIGNATURE SHEET” contains a list of all transferred drugs within a specific date range. This sheet is used to record the signature of the person who received the drugs or to review transfer history. The sheet contains the dispensing and receiving pharmacy location names, transfer date, number of dispense units transferred, drug transferred, new balance in the dispensing pharmacy locations, person from the dispensing site who transferred the drug, and a line for the person’s signature who received the transferred drug.

## New Prime Vendor Interface Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Invoice Cost Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA INVOICE COST SUMMARY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The “INVOICE COST SUMMARY REPORT” contains invoice cost data for a selected date range. It lists the order number with each invoice number, invoice date, total invoice cost, total adjusted cost, and cost difference.

### Outstanding Credits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA OUTSTANDING CREDITS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The “OUTSTANDING CREDITS REPORT” prints invoice data if the invoice has an outstanding credit. A detailed or summary report may be printed.

- The detailed report lists the order number, total order credit amount, and invoice(s) data that generated the credit. The invoice data consists of the invoice number, invoice date, adjusted cost, received credits, outstanding credits, and line item data that generated the credits. The line item data is the line item’s number, drug, adjusted field, invoiced value, adjusted value, and reason for the adjustment. A total outstanding credit dollar amount prints for each order. A grand total outstanding credits dollar amount prints.
- The summary report lists the same data as the detailed report, except it does not list the line item data.

### Processor and Verifier

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA PROCESSOR AND VERIFIER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The “PROCESSOR AND VERIFIER REPORT” displays who processed and verified invoices for a selected date range. It lists the order number, invoice number, invoice date, processor's name, process date, verifier's name, and verification date.

### Stock and Reorder Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[PSA STOCK & REORDER LEVEL RPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The “STOCK AND REORDER LEVEL REPORT” prints the current stock and reorder level of each drug in pharmacy location and/or master vault. The report contains the drug name, stock level, and reorder level. Only pharmacists holding the PSJ RPHARM key can print the stock and reorder levels of drugs in a master vault.

> ![](drug-accountability-inventory-interface-version-3-release-notes/003.png) Each pharmacy location may contain all drugs in the DRUG file (#50). Therefore, this report could be very long. It is advised to queue the report to run during non-critical hours.

# New MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Drug Transfer Between Pharmacies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a drug is transferred between pharmacy locations, people who hold the PSAMGR key will receive the following notification mail message.

Subj: Drug Transfer Between Pharmacies \[#9414\] 30 Jun 97 15:04 10 Lines

From: Drug Accountability System in 'IN' basket. Page 1

-----------------------------------------------------------------------------

Drug: DIPHENOXYLATE HCL W/ATROPINE SULFATETTT

Date: JUN 30,1997

Quantity (TAB): 100

Pharmacist: DAPHARMACIST50,THREE

Transferred from:

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

Transferred and Added to:

OUTPATIENT: PELHAM OP SITE (OP)

### Unprocessed Invoices Due to Expire in \# days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The prime vendor interface loads invoices into temporary file that will remain on the system for 21 calendar days. If no new data has been uploaded and the existing data has not been processed, the data is removed after 21 days. If the data in the temporary file is going to be deleted within 4 days, a warning mail message is sent to holders of PSA ORDERS. A message will be sent every night until either more data is uploaded, data is processed, or the data is deleted.

Subj: Unprocessed Invoices Due to Expire in 3 days \[#9561\] 07 Aug 97 13:56

3 Lines

From: Drug Accountability System in 'IN' basket. Page 1

-----------------------------------------------------------------------------

There are 2 invoices that have been uploaded and not processed. If these

invoices are not processed in four calendar days or if more invoices are not

uploaded in four calendar days, the 2 invoices will be deleted.

### Drug Balances Below Reorder Level

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A nightly job determines if a drug’s balance has reached its reorder level. If so, holders of the PSA ORDERS key will a mail message listing the pharmacy locations’ and/or master vaults’ drugs that are less than their reorder levels. Only pharmacist holding the PSJ RPHARM and PSA ORDERS keys will receive master vault data on the mail message.

Subj: Drug Balances Below Reorder Level \[#9684\] 05 Sep 97 15:56 20 Lines

From: Drug Accountability System in 'IN' basket. Page 1

-----------------------------------------------------------------------------

COMBINED (IP/OP): ALABASTER VAMC IP (IP) ALABASTER VAMC OP (OP)

Stock Current Amount to

Drug Name: Level Balance Order

-----------------------------------------------------------------------------

ACETAMINOPHEN W/CODEINE 15MG TAB 1000 35 965

ACETYLCYSTEINE 20% INH SOLN 10ML 500 190 310

AMPICILLIN 250MG CAP 1200 300 900

DEXTROSE 50% 500ML INJ 30 4 26

DICYCLOMINE HCL 10MG CAP 1000 80 920

DOXEPIN 50MG CAP 600 10 590

DRESSING OPSITE-WOUND 5&1/2IN BY 4IN 200 24 176

GENTAMICIN 0.1% CR 15GM 25 12 13

## Modified Mail Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### DRUG file Price/NDC Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When drugs are received through the Generic Inventory Package (GIP) or prime vendor interface, a check is done to determine if the received drug’s price and/or National Drug Code (NDC) has changed. If the order unit and dispense units in the DRUG file (#50) are the same as the received drug’s, the price per dispense unit and NDC are compared. If either has changed, a mail message is sent to holders of the PSAMGR key.

Subj: DRUG file Price/NDC Update \[#9689\] 06 Sep 97 10:36 17 Lines

From: Price & NDC Updater in 'IN' basket. Page 1

-----------------------------------------------------------------------------

DICHLORPHENAMIDE 50MG TAB

Old price: \$0.054 New price: \$ 0.062

Old NDC : 999999-9999-99 New NDC: 008290-0084-04

NIACIN 500MG TAB

Old NDC : 0075-2850-01 New NDC: 008290-3294-65