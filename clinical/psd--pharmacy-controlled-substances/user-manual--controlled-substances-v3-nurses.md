---
title: Controlled Substances Version 3 Nurse's User Manual (Updated PSD*3*82)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Nurse's  (Updated PSD*3*82)
app_code: PSD
app_name: "Pharmacy: Controlled Substances"
section: CLI
app_status: active
pkg_ns: PSD
patch_ver: 3
patch_id: PSD*3
group_key: "PSD:PSD:3"
file_numbers: []
security_keys: []
menu_options: 2
description: ![](controlled-substances-version-3-nurse-s-user-manual-updated-psd-3-82/001.png)
audience: 
keywords: 
  - naou
  - drug
  - table
  - contents
  - green
  - report
  - controlled
  - patient
  - sheet
  - ward
page_count: 0
word_count: 7642
section_count: 25
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Controlled_Substances/psd_3_nurse_um_r0818.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Controlled_Substances/psd_3_nurse_um_r0818.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=86"
---

![](controlled-substances-version-3-nurse-s-user-manual-updated-psd-3-82/001.png)

CONTROLLED SUBSTANCES (CS)

NURSE’S USER MANUAL

March 1997

(Revised August 2018)

Product Development

Preface

The Controlled Substances (CS) Nurses’ User Manual is designed to provide you with information on the CS software package. This product is one segment of the Veterans Health Information Systems and Technology Architecture (V*IST*A) installed at VA medical centers. The Controlled Substances module provides functionality to monitor and track the receipt, inventory, and dispensing of all controlled substances. This module provides the pharmacy with the capability to define a controlled substance location and a list of controlled substances to maintain a perpetual inventory.

This software provides nursing personnel with the ability to request orders for Controlled Substances via on-demand requests and to monitor and track the Green Sheets from the time of issuance from pharmacy to the time of return and review in pharmacy. Pharmacy may dispense controlled substances via the software automating all necessary documents (VA FORMS 10-2321 and 10-2638) to complete an order request. The software provides functionality to record Automated Management Information Systems (AMIS) and Cost data, address returns to stock, destructions, order cancellations, transfers between locations, and log outpatient prescriptions.

This software is continually being enhanced to provide additional options and capabilities. The CS Development Team encourages you to send questions and comments to them about the completeness and accuracy of this manual and suggestions for its improvement. Electronic mail messages can be sent to <span class="mark">REDACTED</span>.

*(This page included for two-sided copying.)*

|                      |
|----------------------|
| Revision History |

The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 63%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revised Pages</strong></td>
<td><strong>Patch Number</strong></td>
<td><blockquote>
<p><strong>Description</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/2018</td>
<td><a href="#XU_80_679"><u>1</u></a></td>
<td>XU*8.0*679</td>
<td><p>Added note regarding Electronic Signature Block restrictions.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>06/2018</td>
<td>35</td>
<td>PSD*3*82</td>
<td><p>Added NAOU Usage Report [PSD NAOU USAGE] option to the PSD TECH ADV key.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>09/2017</td>
<td>17</td>
<td>PSD*3*81</td>
<td>Updated “Receipt of Controlled Substance from Pharmacy”<br />
[PSD REC GS] section to describe dispense unit added to controlled substance dispense drug being electronically received with this option.<br />
<mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/2013</td>
<td>iii, 35-36<br />
37-39</td>
<td>PSD*3*76</td>
<td>Updated Glossary with description of patch’s new security key PSDRPH<br />
Updated Index<br />
<mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/2011</td>
<td>iii, 35-36</td>
<td>PSD*3*71</td>
<td><p>Clarified description of PSD TECH ADV key. Corrected option name in PSD TRAN entry.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>05/2010</td>
<td>34, 35, 38</td>
<td>PSD*3*69</td>
<td><p>Added description of patch’s new security key PSD TECH ADV, and PSD TECH key.</p>
<p>Added PSD TECH ADV and PSD TECH keys to Index</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>08/08</td>
<td>All</td>
<td>PSD*3*64</td>
<td><p>New menu options added to the Transfer Green Sheet Menu.</p>
<p>Reformatted to conform to national standards.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

*(This page included for two-sided copying.)*Table of Contents

# # Orientation


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Orientation](#orientation)
  - [Electronic Signature](#electronic-signature)
- [Sign Out Doses for Patients](#sign-out-doses-for-patients)
  - [Sign Out Dose for Patient](#sign-out-dose-for-patient)
  - [Activity Report](#activity-report)
  - [Patient ID List Print](#patient-id-list-print)
  - [Record Delayed Wastage](#record-delayed-wastage)
  - [<u> </u>Not Given, Return to Stock](#u-unot-given-return-to-stock)
  - [## Record Defective Dose](#record-defective-dose)
- [All about Ordering](#all-about-ordering)
  - [CS Order Entry for Ward](#cs-order-entry-for-ward)
  - [Infusion or PCA Syringe Order Entry For Patient](#infusion-or-pca-syringe-order-entry-for-patient)
  - [Pending CS Orders Report for an NAOU](#pending-cs-orders-report-for-an-naou)
  - [Orders Filled Not Delivered](#orders-filled-not-delivered)
  - [Check on Priority Orders](#check-on-priority-orders)
- [Verify Count](#verify-count)
- [All about Green Sheets](#all-about-green-sheets)
  - [Receipt of Controlled Substance from Pharmacy](#receipt-of-controlled-substance-from-pharmacy)
  - [Completing a Green Sheet - Ready for Pickup](#completing-a-green-sheet-ready-for-pickup)
  - [Green Sheet History](#green-sheet-history)
  - [Transfer Green Sheet Menu](#transfer-green-sheet-menu)
    - [Transfer Green Sheet and Drug to another NAOU](#transfer-green-sheet-and-drug-to-another-naou)
    - [Receive Green Sheet & Drug from another NAOU](#receive-green-sheet-drug-from-another-naou)
    - [Transfer GS for PCA/Infusion Signed Out to Patient](#transfer-gs-for-pcainfusion-signed-out-to-patient)
    - [Receive GS for PCA/Infusion Signed Out to Patient](#receive-gs-for-pcainfusion-signed-out-to-patient)
    - [Reprint Transfer Between NAOUs (VA FORM 10-2321)](#reprint-transfer-between-naous-va-form-10-2321)
    - [Transferred Green Sheets - Pending NAOU Receipt](#transferred-green-sheets-pending-naou-receipt)
- [Receipt of Controlled Substance from Pharmacy](#receipt-of-controlled-substance-from-pharmacy-1)
- [Ward (NAOU) Drug History](#ward-naou-drug-history)
- [Narcotic Count - Shift Report](#narcotic-count-shift-report)
- [Help Online](#help-online)
  - [<u> </u>Electronic Signature](#u-uelectronic-signature)
    - [Electronic Signature Codes](#electronic-signature-codes)
- [Nursing Supervisor Menu](#nursing-supervisor-menu)
  - [Patient ID List Print](#patient-id-list-print-1)
  - [Initialize NAOU Drug Balance](#initialize-naou-drug-balance)
  - [Delayed Sign Out Dose for Patient](#delayed-sign-out-dose-for-patient)
  - [Balance Adjustments - NAOU](#balance-adjustments-naou)
  - [Patient/Location Inquiry](#patientlocation-inquiry)
  - [Unscheduled Order Report](#unscheduled-order-report)
  - [Expiration Date Report](#expiration-date-report)
- [Steps to Prepare a Ward (NAOU) for use of a Radio Frequency Device](#steps-to-prepare-a-ward-naou-for-use-of-a-radio-frequency-device)
- [Glossary](#glossary)
- [Index](#index)
Within the terminal dialogues used as examples in this manual, the user’s input is underlined and bolded. Whenever the Return/Enter key should be pressed, you will see the symbol <u>\<ENT\></u>. Whenever you see the underline and bold representing the user’s input, you can assume the Return/Enter key was pressed.

## Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Controlled Substances, the Electronic Signature functionality will be used for identification for pharmacy personnel, nursing personnel, and narcotic inspectors.

Identification will be used to reconfirm the identity of the user at the keyboard before proceeding with the next step in a critical process. In the documentation, when your Electronic Signature Code is to be entered, it is represented as <u>XXXXXX</u>.

If you have not previously been issued an Electronic Signature code you can assign yourself one at any menu option by entering TBOX and then choosing Edit Electronic Signature Code. You can also enter “EDIT E and follow the prompts as shown below.

> Note: <span id="XU_80_679" class="anchor"></span>If the SIGNATURE BLOCK PRINTED NAME and SIGNATURE BLOCK TITLE fields are disabled at your site, contact your supervisor to request entry of your name and title.

Electronic Signature Codes

This option is designed to permit you to enter or change your Initials, Signature Block Information and Office Phone number. In addition, you are permitted to enter a new Electronic Signature Code or to change an existing code.

INITIAL: <u>OAC</u>

SIGNATURE BLOCK PRINTED NAME: <u>CSNURSE,ONE A</u>

SIGNATURE BLOCK TITLE: <u>R.N.</u>

OFFICE PHONE: <u>555-7101</u>

ENTER NEW SIGNATURE CODE: <u>XXXXXX</u>(Signature Code will not appear on screen)

RE-ENTER SIGNATURE CODE FOR VERIFICATION: <u>XXXXXX</u>

DONE

*(Page included for two-sided copying)*

# Sign Out Doses for Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A feature to the new *Sign Out Doses for Patients Menu* is that you will be asked to supply the ward that you would like to exercise these options for before you will be able to select them.

Select Ward: <u>WARD 10</u>

Sign Out Dose for Patient

Activity Report

Patient ID List Print

Record Delayed Wastage

Not Given, Return to Stock

Record Defective Dose

## Sign Out Dose for Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is designed for dispensing via a radio frequency device.

Example:

Select Sign Out Doses for Patients Option: SIGN Out Dose for Patient

Enter your Current Signature Code: XXXXXX SIGNATURE VERIFIED

Scan/Enter Patient: CSPATIENT,ONE 04-04-58 000-45-6789

Scan Drug Label or Enter Label \# or Drug: LORAZEPAM 2MG/ML TUBEX

Doses signed out in the last eight hours:

Starting Balance: 30 Correct count? Yes// NO

Correct Count: 32

You are about to adjust the balance upward.

Before you do, let's check to see if there are any orders that need receiving.

REASON: MISCOUNTED

WITNESS ACCESS CODE: XXXXXX \[The witness must be someone other than the nurse signing out the doses\]

WITNESS VERIFY CODE: XXXXXX

*\[Tip: If you type your access and verify code separated by a semicolon, they can be entered on the same line…e.g., <u>access;verify</u>\]*

Thank you, Nurse Recording transaction... ......done.

Amount given: <u>2</u>

Remaining Balance: 30 Recording transaction... done.

Scan Drug Label or Enter Label \# or Drug: <u>\<ENT\></u>

Scan/Enter Patient: <u>\<ENT\></u>

## Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides a detailed and summary listing of dispensing for a drug(s) to a Narcotic Area of Use (NAOU).

Example:

Select Sign Out Doses for Patients Option: <u>ACT</u>ivity Report

Select one of the following:

D DETAIL LISTING ONLY

S SUMMARY LISTING ONLY

Select Dispensing Report(s) to Print: <u>D</u>ETAIL LISTING ONLY

Select NAOU: <u>WARD 10</u>

You may select a single drug, several drugs,

or enter ^ALL to select all drugs.

Select DRUG: <u>LORAZEPAM 2M</u>G/ML TUBEX \*\*\* INACTIVE \*\*\*

Select DRUG: <u>\<ENT\></u>

Start with Date and Time: <u>T-35@1:00</u> (AUG 29, 1996@13:00)

End with Date and Time: <u>T@1:00</u> (OCT 03, 1996@13:00)

This report is designed for a 132 column format.

You may queue this report to print at a later time.

DEVICE: *\[Select Print Device\]printout follows*

Activity Report for WARD 10

Page: 1

Date: AUG 29, 1996@13:00 to OCT 03, 1996@13:00

=\> DRUG

DATE/TIME PATIENT QUANTITY BALANCE NURSE 1

NURSE2

------------------------------------------------------------------------------

=\> LORAZEPAM 2MG/ML TUBEX

SEP 5,1996@10:58 CSPATIENT,ONE - 4 32 CSNURSE,TWO

0

SEP 5,1996@11:50 BALANCE ADJUSTMENT -2 (2 wasted) 30 CSNURSE,TWO

NURSE,DISPENSING

DEFECTIVE DOSE

## Patient ID List Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option supports the printing of barcode labels for patient ID.

Example:

Select Sign Out Doses for Patients Menu Option: <u>PAT</u>IENT ID List Print

Select one of the following:

N NAOU

W WARD

You may select NAOU or Ward to print the Patient ID List.

Select Method: <u>W</u>ARD

Select WARD to print Patient ID List: <u>1 NORTH</u>

Select Ward to print Patient ID List:<u>\<ENT\></u>

Select one of the following:

A Alphabetical

R Room-Bed

Sort: <u>A</u>lphabetical

This report is designed to print bar codes on a printer.

You may queue this report to print at a later time.

DEVICE: *\[Select Print Device\]printout follows*

Patient ID List for 1 NORTH Printed: Feb 28, 1997 7:37:17 am Page: 1

PATIENT ROOM-BED

---------------------------------------------------------------------------

CSPATIENT,TWO (3737)

![](controlled-substances-version-3-nurse-s-user-manual-updated-psd-3-82/002.png)

CSPATIENT,THREE (5634) 160-B

![](controlled-substances-version-3-nurse-s-user-manual-updated-psd-3-82/003.png)

CSPATIENT,FOUR (3638) 160-A

![](controlled-substances-version-3-nurse-s-user-manual-updated-psd-3-82/004.png)

## Record Delayed Wastage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used when a dispensed dose needs to be wasted.

Example:

Select Sign Out Doses for Patients Menu Option: <u>REC</u>ord Delayed Wastage

Wastage can only be recorded within twelve hours after signing out a dose.

Enter your Current Signature Code: <u>XXXXXX</u> SIGNATURE VERIFIED

Please enter the ward from which the drug(s) will be signed out.

Select Ward: <u>WARD 10</u>

Wastage can only be recorded within 12 hours after signing out a dose.

(except for PCA syringes and Infusions)

Scan/Enter Patient: <u>CSPATIENT,O</u>NE 04-04-58 000-45-6789

Scan Drug Label or Enter Label \# or Drug: <u>LORAZ</u>EPAM 2MG/ML TUBEX CN302 LORAZEPAM 2MG/ML TUBEX WARD 10

Doses dispensed in the last 12 hours:

4/24/96 10:38:49 am 1 TUBEX (1 WASTED) LANSING,EMILY

dropped

4/24/96 2:28:18 pm 2 TUBEX LANSING,EMILY

Amount actually given at 4/24/96 2:28:18 pm: <u>1</u> Amount wasted: 1

REASON: <u>DROPPED ON FLOOR</u>

WITNESS ACCESS CODE: <u>XXXXXX</u> *\[Witness enters access code\]*

WITNESS VERIFY CODE: <u>XXXXXX</u> *\[Witness enters verify code\]\[Tip: If you type your access and verify code separated by a semicolon, they can be entered on the same line…e.g., <u>access;verify</u>\]*

Thank you, Nurse

## <u> </u>Not Given, Return to Stock

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a dose has not been given to a patient and must be returned to stock, the dispensing nurse MUST use this option, within the specified amount of time determined by pharmacy, of the last dispensed dose. Pharmacy is able to determine at the site level an amount of time for the information to be entered. If the nurse does not enter the information within this amount of time a balance adjustment, which is only available on the *Supervisor’s Menu*, will need to be done or a count correction can be entered next time there is a signing out of the dose.

Example:

Select Sign Out Doses for Patients Option: <u>NOT</u> Given, Return to Stock

Enter your Current Signature Code: <u>XXXXXX</u> SIGNATURE VERIFIED

Please enter the ward from which the drug(s) was signed out.

Select Ward: <u>WARD 10</u>

Returns can only be recorded within 12 hours after signing out a dose.

Scan/Enter Patient: <u>CSPATIENT,ONE</u> 04-04-58 000-45-6789

Scan Drug Label or Enter Label \# or Drug:

<u>LORAZEPAM 2MG/</u>ML TUBEX

Doses signed out in the last 12 hours:

11/18/96 9:30:49 am 2 TUBEX (1 WASTED) LANSING,EMILY

DROPPED

Starting Balance: 13

Amount actually given at 11/18/96 9:30:49 am: <u>0</u>

Amount returned: (1-2): 2// <u>\<ENT\></u>

REASON: Not given, returned to stock Replace <u>\<ENT\></u>

Balance: 15

## ## Record Defective Dose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a nurse discovers a damaged drug that cannot be dispensed to a patient, this option is used to record the wasting.

Example:

Select Sign Out Menu Option: <u>RECORD DEFECTIVE D</u>ose

Enter your Current Signature Code: <u>XXXXXX</u> SIGNATURE VERIFIED

Please enter the ward from which the defective drug(s) will be destroyed.

Select Ward: <u>WARD 10</u>

Scan Drug Label or Enter Label \# or Drug:

LORAZEPAM 2MG/ML TUBEX

Doses signed out in the last eight hours:

1/16/97 3:50:13 pm 0 TUBEX (1 WASTED) (2 RETURNED) LANSING,EMILY

Starting Balance: 10 Correct count? Yes// <u>\<ENT\></u> YES

Amount defective: <u>2</u>

WITNESS ACCESS CODE: <u>XXXXXX</u>

WITNESS VERIFY CODE: <u>XXXXXX</u>

Thank you, Nurse

Remaining Balance: 8 Recording transaction... ......done.

Scan Drug Label or Enter Label \# or Drug:<u>\<ENT\></u>

# All about Ordering

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options for ordering and checking on orders.

## CS Order Entry for Ward

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to electronically request Controlled Substances drug requiring the VA FORM 10-2638 from pharmacy.

There are three types of orders that can be entered.

> Scheduled Delivery: Orders for drugs which are input during the scheduled delivery time.

> Unscheduled Pick Up: Orders that are being requested at an unscheduled time.

> One-Time Request: Orders for drugs that are not normally stocked on an NAOU. Your orders will be limited to the package amount specified for that drug. These can be entered through the Scheduled or Unscheduled route.

The nurse is not restricted to the ordering multiples established by the package size. If the default order size is one (1) and you need to enter four (4), your order will be broken into four (4) separate orders of one (1) each. You will be prompted four (4) times for comments on each separate order.

Under Version 2.0 the nurse had to enter an order and approve it before another order could be entered. In Version 3.0 the nurse can now enter multiple orders and then approve/delete them at one time.

## Infusion or PCA Syringe Order Entry For Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is for ordering an infusion or PCA syringe for a specific patient.

Example:

Select Ordering Menu Option: <u>INFU</u>sion or PCA Syringe Order Entry

Select Ordering NAOU: <u>WARD 10</u>

THIS IS WHERE THE ORDER ENTRY BANNER WILL DISPLAY.

Scan/Enter Patient: <u>CSPATIENT,ONE</u> 04-04-58 000-45-6789

Select one of the following:

I Infusion

P PCA Syringe

Enter response: <u>I</u>nfusion

Checking for active Controlled Substance IV orders.

Select the primary Controlled Substance for this infusion: <u>MORPHINE</u>

Searching for pending orders...

Orders pending: 1 Quantity Ordered (MCH): 0

All pending orders are currently being processed. Please review the PENDING

CS ORDERS REPORT for more information.

Checking for the last order for CSPATIENT,ONE.

Dosage in MLs: <u>2</u>

Select IV SOLUTIONS PRINT NAME: <u>D5W</u> D5W 500 ML

2 ML in 500 ML of D5W

Date/time required: <u>T@2:00</u> (SEP 05, 1996@14:00)

processing now...

COMMENTS:

1\>2 ML in 500 ML of D5W

EDIT Option: <u>\<ENT\></u>

Controlled Substance \*INFUSION\* Order Request

Patient: CSPATIENT,ONE

Requested by : CSNURSE,TWO Needed by: SEP 5,1996@14:00

---------------------------------------------------------------------------

Drug : MORPHINE SULF 10MG/ML INJ

Dispensed by : N/A Dispensed Date: N/A

Disp. Location : MAST VAU

Exp. Date :

Manufacturer :

Lot \# :

Ord. Location : WARD 10

Order Status : ORDERED - NOT PROCESSED

Comments:

2 ML in 500 ML of D5W

Is this OK? YES// <u>\<ENT\></u>

Enter your Current Signature Code: <u>XXXXXX</u> SIGNATURE VERIFIED

Processing your request now... Printing on PHARMACY PRINTER...

Sent to Pharmacy...

Scan/Enter Patient:<u>\<ENT\></u>

## Pending CS Orders Report for an NAOU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to list all pending CS orders. This report may be generated for a single drug or all drugs within the NAOU.

## Orders Filled Not Delivered 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a list of all Controlled Substances orders filled from the pharmacy dispensing site (vault) but not yet delivered to the NAOUs. A summary total sorted by drug is also generated.

To receive these orders on the NAOU use the *Receipt of Controlled Substances from Pharmacy* option

## Check on Priority Orders 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will check the status of Priority Orders that Pharmacy has filled today for a selected NAOU.

# Verify Count

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used to verify and correct balances.

Example

Select Controlled Substances Nurses' (CS) Menu Option: <u>VERI</u>fy Count

Select NAOU: <u>WARD 10</u>

WITNESS ACCESS CODE: <u>XXXXXX</u>

WITNESS VERIFY CODE: <u>XXXXXX</u>

Thank you, Testy

Give me a second to alphabetize.

ACETAMINOPHEN W/CODEINE 15MG TAB

Balance: 35 TAB

Count Correct? Yes// <u>N</u>O

Package Size: 50 Breakdown Unit: TAB

Correct Count: 35// <u>40</u>

You are about to adjust the balance upward.

Before you do, let's check to see if there are any orders that need receiving.

Recording inventory in transaction history.

ACETAMINOPHEN W/CODEINE 30MG TAB

Balance: 3 TAB

Count Correct? Yes// <u>\<ENT\></u> YES

Recording inventory in transaction history.

LORAZEPAM 2MG/ML TUBEX

Balance: 13 TUBEX

Count Correct? Yes// <u>\<ENT\></u> YES

Recording inventory in transaction history.

Would you like a report of current balances? No// <u>Y</u>ES

You may queue this report to print at a later time.

DEVICE: *\[Select Print Device\]*

Give me a second or two to alphabetize.

*printout follows*

Controlled Substance Balances Page: 1

WARD 10

Nov 18, 1996@09:52:40

=\> DRUG QUANTITY

---------------------------------------------------------------------------

=\> ACETAMINOPHEN W/CODEINE 15MG TAB 40 TAB

=\> ACETAMINOPHEN W/CODEINE 30MG TAB 3 TAB

=\> LORAZEPAM 2MG/ML TUBEX 13 TUBEX

# All about Green Sheets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This menu contains options for handling Green Sheets.

## Receipt of Controlled Substance from Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After physically receiving the Green Sheet (VA FORM 10-2638) from pharmacy, it is important to update the status from “Filled not Delivered” to “Delivered-Perpetual Inventory” or “Delivered-Actively on NAOU” on your computer by using this option.

To view a list of the pending orders from pharmacy, use the option *Orders Filled Not Delivered*.

If you are receiving a Green Sheet from another NAOU, use the *Receive Green Sheet and Drug from another NAOU* option or the Receive GS for PCA/Infusion Signed Out to Patient option under the *Transfer Green Sheet Menu* so that your count is correct.

## Completing a Green Sheet - Ready for Pickup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a nurse has completed dispensing from a Green Sheet, the nurse needs to update the status of that Green Sheet to “Ready for Pick Up” by using this option.

## Green Sheet History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provides a detailed account of every transaction affecting a VA FORM 10-2638. Information shown on the reports may be different due to recent activity that has taken place on the Green Sheet number.

## Transfer Green Sheet Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this menu to transfer and receive Green Sheets between NAOUs.

### Transfer Green Sheet and Drug to another NAOU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option transfers Controlled Substances drugs and their associated Green Sheet to another NAOU. The transferring of Controlled Substances drugs between NAOUs requires two processing steps.

Step 1 - The Green Sheet and Drug must be transferred to an NAOU.

Step 2 - The Green Sheet and Drug must then be received on that NAOU.

### Receive Green Sheet & Drug from another NAOU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option receives Controlled Substances drugs and their associated Green Sheet from another NAOU. The transferring of Controlled Substances drugs between NAOUs requires two processing steps. The Green Sheet MUST be received on the NAOU in the computer for the information to be correct.

Step 1 - The Green Sheet and Drug must be transferred to an NAOU.

Step 2 - The Green Sheet and Drug must then be received on that NAOU.

### Transfer GS for PCA/Infusion Signed Out to Patient 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides nurses the ability to transfer Green Sheets with a quantity of 0 for PCA/Infusions to another NAOU. The transferring of these Green Sheets between NAOUs requires two processing steps.

Step 1 - The Green Sheet and Drug must be transferred to an NAOU.

Step 2 - The Green Sheet and Drug must then be received on that NAOU.

### Receive GS for PCA/Infusion Signed Out to Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option provides nurses the ability to receive Green Sheets with a quantity of 0 for PCA/Infusions from another NAOU. The transferring of these Green Sheets between NAOUs requires two processing steps. The Green Sheet MUST be received on the NAOU in the computer for the information to be correct.

Step 1 - The Green Sheet and Drug must be transferred to an NAOU.

Step 2 - The Green Sheet and Drug must then be received on that NAOU.

### Reprint Transfer Between NAOUs (VA FORM 10-2321)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Nurses may reprint the transfer between NAOUs form (in lieu of VA FORM 10-2321) for any Green Sheet and drug transferred from their NAOU. The form may be reprinted only if the transferred Green Sheet and drug has not been received into the NAOU receiving the transfer.

### Transferred Green Sheets - Pending NAOU Receipt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report lists all Green Sheets that have been transferred from an NAOU and are pending receipt in another NAOU.

To receive these pending Green Sheets on an NAOU use the *Receive Green Sheet & Drug from another NAOU* option.

# Receipt of Controlled Substance from Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this option to receive Controlled Substances orders with a Green Sheet (VA FORM 10-2638).

Patch PSD\*3.0\*81 modifies the “Receipt of Controlled Substance from Pharmacy”  
\[PSD REC GS\] option to include the dispense unit (ML, TAB, CAP, etc.) of the controlled substance dispense drug being electronically received into the Narcotic Area of Use (NAOU).

# Ward (NAOU) Drug History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this report to list all ACTIVE Controlled Substances orders currently on a specific NAOU.

Example:

Select Controlled Substances Nurses' (CS) Menu Option: <u>WARD</u> (NAOU) Drug History

Select NAOU: <u>WARD 10</u>

You may queue this report to print at a later time.

DEVICE: *\[Select Print Device\] \[I chose to print it to my terminal\]printout follows*

Nursing Shift Check Log for WARD 10 Page: 1

SEP 5,1996@13:37

=\> DRUG

DATE RECD

DISP \# RECD QTY BY ORDER STATUS

------------------------------------------------------------------------------

=\> LORAZEPAM 2MG/ML TUBEX

181 MAY 1,1995@09:00 10 AC DELIVERED

ACTIVELY ON NAOU

# Narcotic Count - Shift Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This report will show the balance for one or all drugs on a ward.

Example:

Select Controlled Substances Nurses' (CS) Menu Option: <u>NAR</u>cotic Count - Shift Report

Select NAOU: <u>WARD 10</u>

Select one of the following:

A All Drugs

S Single Drug

C Contingency Report

G All drugs (including green sheets)

Please select type of report: All Drugs// <u>S</u>ingle Drug

Select DRUG: <u>LORAZEPAM 2MG</u>/ML TUBEX

Balance: 30 TUBEX

# Help Online

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online Help is a new feature in Version 3.0. The Controlled Substances team hopes that this new option will help users better understand the options and what they do.

You will be able to view the help by following this example.

Example:

Select Controlled Substances Nurses’ (CS) Menu Option:<u>He</u>lp Online

Select one of the following:

1 VIEW HELP

2 PRINT HELP

Enter response: <u>1</u> VIEW HELP

............................*New Screen*.............................

ONLINE HELP FOR NURSES

All about Dispensing

Dispensing

Report of Dispensing Activity

Patient ID List Print

All about Ordering

Scheduled/Unscheduled

One Time Request

Scheduled/Unscheduled

Filled Not Delivered

All about Green Sheets

Receiving

CompletingGS HistoryTransferElectronic Signture Code

Select HELP SYSTEM action or \<return\>: <u>RECEIVING</u>

............................*New Screen*.............................

RECEIVING

After physically receiving the GS (VA FORM 0-2638, it is important to

Update the status on your computer so that your account is correct,

Select HELP SYSTEM action or \<return\>:\<ENT\>

## <u> </u>Electronic Signature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In Controlled Substances, the electronic signature functionality will be used for identification for pharmacy personnel, nursing personnel, and narcotic inspectors.

Identification will be used to reconfirm the identity of the user at the keyboard before proceeding with the next step in a critical process.

In the documentation, when your Electronic Signature Code is to be entered, it is represented as <u>XXXXXX</u>.

If you have not previously been issued an Electronic Signature code you can assign yourself one at any menu option by entering TBOX and then choosing *Edit Electronic Signature Code*. You can also enter “EDIT E and follow the prompts as shown below.

### Electronic Signature Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is designed to permit you to enter or change your Initials, Signature Block Information, and Office Phone number. In addition, you are permitted to enter a new Electronic Signature Code or to change an existing code.

Example:

INITIAL: <u>OAC</u>

SIGNATURE BLOCK PRINTED NAME: <u>ONE A CSNURSE</u>

SIGNATURE BLOCK TITLE: <u>R.N.</u>

OFFICE PHONE: <u>555-7101</u>

ENTER NEW SIGNATURE CODE: <u>XXXXXX</u>(Signature Code will not appear on screen)

RE-ENTER SIGNATURE CODE FOR VERIFICATION: <u>XXXXXX</u>

DONE

*TIP: It may help to use your access code as your Electronic Signature Code, this will help eliminate the possibility of forgetting it!*

# Nursing Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a menu containing special options to support the dispensing of Controlled Substances.

## Patient ID List Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option supports the printing of barcode labels for patient ID.

Example:

Select Nursing Supervisor Menu Option: <u>PATI</u>ent ID List Print

Select one of the following:

N Nursing Location

W Ward

You may select Nursing Location or Ward to print the Patient ID List.

Select Method: <u>W</u>ard

Select Ward to print Patient ID List: <u>1 NORTH</u>

Select Ward to print Patient ID List: <u>\<ENT\></u>

Select one of the following:

A Alphabetical

R Room-Bed

Sort: <u>A</u>lphabetical

This report is designed to print bar codes on a printer.

You may queue this report to print at a later time.

DEVICE: *\[Select Print Device\]printout follows*

Patient ID List for 1 NORTH Printed: Oct 09, 1996 9:51:51 am Page: 1

PATIENT ROOM-BED

------------------------------------------------------------------------------

CSPATIENT,TWO (5119) 1 NORTH

![](controlled-substances-version-3-nurse-s-user-manual-updated-psd-3-82/005.png)

CSPATIENT,THREE (6543) 160-B 1 NORTH

![](controlled-substances-version-3-nurse-s-user-manual-updated-psd-3-82/006.png)

## Initialize NAOU Drug Balance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used to establish beginning balances for drugs.

## Delayed Sign Out Dose for Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used when there is computer down time and it is necessary to sign out doses that were already given to patients.

Example:

Select Nursing Supervisor Menu Option: <u>DELAY</u>ed Sign Out Dose for Patient

Enter your Current Signature Code: <u>XXXXXX</u> SIGNATURE VERIFIED

Please enter the ward from which the drug(s) will be signed out.

Select Ward: <u>WARD 10</u>

Scan/Enter Patient: <u>CSPATIENT,ONE</u> 04-04-58 000-45-6789

Scan Drug Label or Enter Label \# or Drug:

<u>LORAZEPAM 2MG</u>/ML TUBEX

Doses signed out in the last eight hours:

Starting Balance: 29 Correct count? Yes// <u>N</u>O

Correct Count: <u>28</u>

REASON: <u>DROPPED ONE</u>

WITNESS ACCESS CODE: <u>XXXXXX</u>

WITNESS VERIFY CODE: <u>XXXXXX</u>

Thank you, Nurse Recording transaction... .....done.

Amount given: <u>2</u>

Date/time given: <u>NOW</u> (OCT 09, 1996@09:56)

Nurse that signed out dose: <u>CSNURSE,TWO</u>

Remaining Balance: 26 Recording transaction... done.

Scan Drug Label or Enter Label \# or Drug: <u>\<ENT\></u>

Scan/Enter Patient:<u>\<ENT\></u>

## Balance Adjustments - NAOU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used to adjust the balance of controlled substances.

## Patient/Location Inquiry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option may be used to verify the location of a patient.

## Unscheduled Order Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will print a report of unscheduled orders shown by drug or NAOU.

Example:

Select Supervisor (CS) Menu Option: <u>U</u>nscheduled Order Report

Select Date Range for NAOU Unscheduled Order Report

Start with Date: <u>T-2</u> (SEP 19, 1996)

End with Date: <u>T</u> (SEP 11, 1996)

Do you want to print a summary only? NO// <u>Y</u>ES

Select one of the following:

D DRUG/ALL NAOUS

N NAOU/ALL DRUGS

You may print by either of these sorting methods.

Select SORT ORDER for Report: <u>N</u>AOU/ALL DRUGS

You may select a single NAOU, several NAOUs,

or enter ^ALL to select all NAOUs.

Select NAOU: <u>^ALL</u>

This report is designed for a 80 column format.

You may queue this report to print at a later time.

DEVICE: *\[Select Print Device\]printout follows*

SUMMARY NAOU/DRUG UNSCHEDULED ORDER REPORT - DATE: SEP 11,1996 PAGE: 1

NAOU: WEST 4

From SEP 9, 1996 to SEP 11, 1996

=\> DRUG

TOTAL \# OF ORDERS TOTAL QUANTITY

------------------------------------------------------------------------------

=\> ACETAMINOPHEN W/CODEINE 15MG TAB

1 50

=\> ACETAMINOPHEN W/CODEINE ELIXIR

1 1

=\> CLORAZEPATE DIPOTASSIUM 11.25MG TAB

2 40

=\> CODEINE PHOSPHATE 30MG SOL TAB

1 15

=\> CODEINE PHOSPHATE 60MG SOL TAB

3 75

=\> DIPHENOXYLATE HCL W/ATROPINE SULFATETTT

2 20

=\> LORAZEPAM 2MG TAB

4 400

=\> LORAZEPAM 2MG/ML TUBEX

3 13

=\>

NAOU Subtotal \# of Orders: 17

Grand Total \# of Orders: 18

SUMMARY NAOU/DRUG UNSCHEDULED ORDER REPORT - DATE: SEP 11,1996 PAGE: 4

NAOU: WEST 8

From SEP 9, 1996 to SEP 11, 1996

=\> DRUG

TOTAL \# OF ORDERS TOTAL QUANTITY

------------------------------------------------------------------------------

=\> TYLOX CAP

1 20

=\>

NAOU Subtotal \# of Orders: 1

Grand Total \# of Orders: 18

## Expiration Date Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option will print a Controlled Substances Expiration Date Report for a single, several, or all NAOUs. This report may be sorted by DATE/DRUG/NAOU or by DATE/NAOU/DRUG.

Example:

Select Nursing Supervisor Menu Option: <u>EX</u>piration Date Report

Controlled Substances Expiration Date Report

Start with Date: <u>T-50</u> (JUL 23, 1996)

End with Date: <u>T</u> (SEP 11, 1996)

You may select a single NAOU, several NAOUs,

or enter ^ALL to select all NAOUs.

Select NAOU: <u>^ALL</u>

Select one of the following:

D DATE/DRUG/NAOU

N DATE/NAOU/DRUG

You may print by either of these sorting methods.

Select SORT ORDER for Report: <u>D</u>ATE/DRUG/NAOU

This report is designed for a 80 column format.

You may queue this report to print at a later time.

DEVICE: *\[Select Print Device\]*

CS DRUG EXPIRATION DATE REPORT Page: 1

FOR PERIOD JUL 23, 1996 TO SEP 11, 1996

PRINTED SEP 11,1996@08:43

=\> DATE

DRUG

DISP \# NAOU

------------------------------------------------------------------------------

=\> JUL 17,1996

LORAZEPAM 2MG TAB U/D

MAST VAU

381 WEST 4

427 WEST 4

428 WEST 4

OPIUM CAMPHORATED TINC

MAST VAU

=\> SEP 1996

LORAZEPAM 2MG TAB U/D

WEST 4

# Steps to Prepare a Ward (NAOU) for use of a Radio Frequency Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Converting a ward from the use of Green Sheets (VA FORM 10-2638) to the use of an RF device should be carefully coordinated between Nursing and Pharmacy. Timing is an issue and it is recommended that the conversion NOT take place in the midst of processing a large number of receipts. There are several steps to consider in order to avoid confusion and/or frustration.

1.  Pharmacy should use the Label for Dispensing (Barcode) option to print barcode labels for Controlled Substances dispensed to Wards. If labels are needed for drug already received on a ward, the reprint option should be used by Pharmacy:

Example:

Select Dispensing Menu Option: <u>RE</u>print Reports Menu

Select Reprint Reports Menu Option: <u>LA</u>bel Reprint for Dispensing Drug

Green Sheets/Transactions that have a status of FILLED - NOT DELIVERED

or DELIVERED - ACTIVELY ON NAOU will be reprinted for a given number range.

> These barcodes may then be scanned by Nursing for receiving and dispensing.

2.  Nursing should use the *Patient ID List Print* option to print barcode labels for patients currently on the ward. Readability of labels will be affected by the condition of the ribbon on the printer. For help on specific DEVICE file set up, please refer IRMS to the Controlled Substances Version 3.0 Technical Manual. These labels may then be scanned by Nursing for dispensing to Patients.
3.  If there are any drugs dispensed by Pharmacy that will always require a green sheet, such as infusions, those drugs should be flagged in the vault as follows:

Select Enter/Edit Menu Option: <u>ST</u>ock CS Drugs - Enter/Edit

Select NAOU: MAST VAU

Do you wish to ADD or EDIT stock drugs? ADD// <u>E</u>DIT

Select DRUG: MEPERIDINE HCL 100MG/ML INJ CN101

LOCATION: S15// <u>^ALW</u>AYS PRINT VA FORM 10-2638?

ALWAYS PRINT VA FORM 10-2638?: <u>??</u>

Answer "1" or "YES" to force printing a VA FORM 10-2638 even when

dispensing to a Narcotic Area of Use that is keeping a perpetual

inventory.

Choose from:

1 YES

0 NO

ALWAYS PRINT VA FORM 10-2638?: <u>Y</u> YES

4.  Pharmacy should flag any liquids using the same option so that Nursing can dispense partial doses.

Do you wish to ADD or EDIT stock drugs? ADD// <u>E</u>DIT

Select DRUG: <u>OPIUM CAMP</u>HORATED TINC

LOCATION: <u>^L</u>IQUID?

LIQUID?: <u>1</u> YES

5.  Pharmacy must set the USING PERPETUAL INVENTORY flag to YES.

Select Supervisor (CS) Menu Option: <u>SET U</u>p CS (Build Files) Menu

Select Set Up CS (Build Files) Menu Option: <u>EN</u>ter/Edit Menu

Select Enter/Edit Menu Option: <u>CREA</u>te/Edit the Narcotic Area of Use

Select NAOU: <u>WEST 4</u>

CONTROLLED SUBSTANCES SITE : <u>NAME</u>

NAOU: WEST 4// <u>^USING PER</u>PETUAL INVENTORY?

USING PERPETUAL INVENTORY?: YES// <u>??</u>

This flag is used to determine if this NAOU is using the Controlled

Substances perpetual inventory functionality. If this field is set to

"YES" or "1" the standard Controlled Substance Administration Record VA

FORM 10-2638 (Green Sheet) WILL NOT be printed and will be replaced by the

perpetual inventory method of tracking CS drugs.

6.  Nursing should then initialize the balances. If there are pending receipts for the NAOU, it is better to first initialize balances and then process the receipts.

Select Nursing Supervisor Menu Option: <u>I</u>nitialize NAOU Drug Balance

Select NAOU: <u>WEST 4</u>

This option will set all balances to zero before initializing.

Are you sure you want to proceed? <u>Y</u>ES

Give me a second to alphabetize.

ACETAMINOPHEN W/CODEINE 15MG TAB

Package Size: 50 Breakdown Unit: TAB

Initial Balance: 0// <u>100</u>

Updating beginning balance and transaction history.

LORAZEPAM 2MG TAB U/D

Package Size: 20 Breakdown Unit: TAB

Initial Balance: 0// <u>20</u>

Updating beginning balance and transaction history.

Would you like a report of current balances? Yes//<u>\<ENT\></u>

You may queue this report to print at a later time.

DEVICE:

Controlled Substance Balances Page: 1

------------------------------------------------------------------------------

WEST 4

Jun 13, 1996@10:09:46

=\> DRUG QUANTITY

--------------------------------------------------------------------------

=\> ACETAMINOPHEN W/CODEINE 15MG TAB 100 TAB

=\> LORAZEPAM 2MG TAB U/D 20 EA

*(This page included for two-sided copying)*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Completion Status A review status is attached to each Controlled Substances Green Sheet returned to pharmacy. The following are valid:
> NO DISCREPANCY—No discrepancy found.
> TURN IN FOR DESTRUCTION—CS drug turned in to be destroyed.
> RETURNED TO STOCK—CS Drug returned to stock. The dispensing site inventory balance will be updated.
> MATH ERROR—CS drug discrepancy found.
> GREEN SHEET NOT SIGNED BY NURSE—GS missing nurse’s signature.
> OTHER—REFERRED TO PHARMACY SUPERVISOR—CS drug discrepancy referred to supervisor for resolution.
Dispensing Number Control number assigned by pharmacy when dispensing a Controlled Substances drug. This number is used to track the Green Sheet and drug.
Also referred to as the Disp \#, Green Sheet \#, GS \#, or transaction \# throughout the CS package.
Dispensing/Receiving This report can be printed in lieu of VA Form
Report 2321 and lists all Controlled Substances orders
(in lieu of VA Form 10-2321) dispensed to an NAOU. The signatures of the dispensing pharmacist and the nurse receiving the drug are required.
Dispensing Site An NAOU set up as a pharmacy vault that dispenses Controlled Substances drugs.
Dispensing Worksheet This worksheet compiles a list of all pending Controlled Substances request orders for a selected dispensing site. A worksheet number, drug name, quantity ordered, requesting NAOU, ordered by, comments, and blanks for pharmacy dispensing number, manufacturer, lot number, and expiration date are listed on the worksheet.
Drug Address Code A code that represents the location of a drug in the NAOU.
(Location Code) For example, if TYLOX is stored in an NAOU on the second set of shelves, third shelf from the top, its drug address code could be expressed as S,2,3. The address code can consist of up to three levels separated by a comma. Each level should further define the exact location. The code is associated with an expansion code for clarity.
Drug Address Code Text used to clarify the meaning of a drug
Expansion address code. For example, the code S would be
expanded and printed as shelf. (These codes and
expansions are locally created terms.)
Green Sheet The CONTROLLED SUBSTANCE ADMINISTRATION RECORD (VA Form 10-2638) is referred to as a Green Sheet or GS throughout the CS package. Pharmacy dispensing number, drug name, expiration date, quantity dispensed, lot number, ordered by, dispensed by, and ward (NAOU) are printed on the form.
Green Sheet number Control number assigned by pharmacy when dispensing a Controlled Substances drug. This number is used to track the Green Sheet and drug. It is also referred to as the GS \#, dispensing \#, or disp \#, or transaction \# throughout the CS package.
Inpatient Site Inpatient Site must be defined for each NAOU. The Controlled Substances software utilizes this data to distinguish multi-divisional sites.
Inspector’s Log This report lists all active Green Sheets by NAOU.
It includes the following information: Green Sheet
\#, drug name, date dispensed, quantity dispensed,
expiration date (if available), blanks for quantity
on hand, and a signature blank for verification.
Intranet A companywide computer network available via modem that connects users.
Master Vault An NAOU set up as your primary dispensing site.
NAOU - Narcotic Area A Narcotic Area of Use (NAOU) is a place where
of Use commonly stocked Controlled Substances drugs are stored for use by pharmacy, wards or treatment areas.
There are three types of NAOUs:
1\) Master Vault,
2\) Satellite Vault, and
3\) Narcotic Locations.
NAOU Inventory Group An NAOU Inventory Group is defined by pharmacy to represent the Narcotic Areas of Use which are inventoried together as a group. By grouping the commonly inventoried NAOUs under an easy to remember group name, the elements of the inventory are established, and do not have to be redefined every time an inventory is scheduled.
Narcotic Location An NAOU set up for the nursing wards, pharmacy IV room, or a pharmacy working stock area.
Order Entry Banner Provides a free text field as a site parameter to appear upon Nursing CS Order Entry. When the user accesses the following 3 options, the free text field will be displayed:
> 1\) Nursing Order Entry
> 2\) Pharmacy Order Entry from Nursing
> 3\) Infusion Order Entry
Order Status A processing status is attached to each Controlled Substances request order. The following are valid:
> REQUESTED—NOT ORDERED
> Requests created by batch processing but not yet approved.
> ORDERED—NOT PROCESSED
> Ordered by nursing but not processed by pharmacy.
> PROCESSED—NOT DISPENSED Processed (filled) by pharmacy but not yet dispensed.
> FILLED—NOT DELIVERED Dispensed and verified by pharmacy but not delivered to the requesting NAOU.
> DELIVERED—ACTIVELY ON NAOU Drug stored on the NAOU.
> COMPLETED—GREEN SHEET READY FOR PICKUP Nursing has flagged the Green Sheet ready for pharmacy pickup.
> COMPLETED—GREEN SHEET PICKED UP Green Sheet returned to pharmacy but not yet reviewed.
> COMPLETED—REVIEWED Pharmacy has reviewed the Green Sheet .
> COMPLETED—PENDING PROBLEM
> RESOLUTION Pharmacy has reviewed the Green Sheet and a problem exists
> CANCELLED Order cancelled.
> TRANSFERRED TO ANOTHER NAOU Order and drug transferred to another NAOU.
> UNDER REVIEW BY INSPECTOR Order and drug pulled from NAOU by CS Inspector for review.
> LOGGED BY TRAKKER All drug doses from this order have been logged out to patients using the TRAKKER. (Not currently used in Version 2.0.)
PSD ERROR This key should be allocated to pharmacy supervisors responsible for maintaining the narcotic vault. This key controls access to reports listing various error and exception conditions generated when entries are filed from the barcode TRAKKER. Also, the holders of this key will receive electronic mail messages created by using the TRAKKER.
PSD NURSE This key should be allocated to nurses, usually LPNs, who may only receive and administer controlled substances but cannot place the order requests.
PSD PARAM This key should be allocated only to the Inpatient Pharmacy Package Coordinator(s). This lock controls the printing of the Green Sheets and the range of automated dispensing numbers for a dispensing site (vault).
PSD TECH Allocate this key to control substance technicians. This key controls access to the *List On-Hand Amounts* \[PSD ON-HAND TECH\], *Transfer Drugs between Dispensing Sites Report* \[PSD PRINT VAULT TRANSFERS TECH\], and the *Daily Activity Log (in lieu of VA FORM 10-2320)* \[PSD DAILY LOG TECH\] options on the Technician (CS Pharmacy) Menu \[PSD PHARM TECH\]
PSD TECH ADV Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the *Receipts Into Pharmacy* \[PSD RECEIPTS MENU\], *Dispensing Menu* \[PSD DISPENSING MENU\], *Destructions Menu* \[PSD DESTROY MENU\], *Manufacturer, Lot \#, and Exp. Date - Enter/Edit* \[PSD MFG/LOT/EXP\], *Outpatient Rx's* \[PSD OUTPATIENT\], *Complete Green Sheet* \[PSD COMPLETE GS\], *Destroyed Drugs Report* \[PSD DEST DRUGS REPORT\], *DEA Form 41 Destroyed Drugs Report* \[PSD DESTROY DEA41\], *Destructions Holding Report* \[PSD DESTRUCTION HOLDING\], *Add Existing Green Sheets at Setup* \[PSD EXISTING GS\], *Green Sheet Transfer Between NAOUs Report* \[PSD GS TRANSFER (NAOU) REPORT\], *NAOUUsage Report* \[PSD NAOU USAGE\], *Transfer Drugs between Dispensing Sites* \[PSD TRANSFER VAULT DRUGS\] options on the *Technician (CS Pharmacy) Menu* \[PSD PHARM TECH\]. The CS technician may perform all functions of the *Outpatient Rx’s* \[PSD OUTPATIENT\] option except releasing prescriptions.
PSD TRAN This key should be allocated to the Inpatient Pharmacy Coordinator(s). This key controls the access to the *NAOU to NAOU Transfer Stock Entries* \[PSD TRANSFER NAOU\] option. Users can copy stock entries from one NAOU into another NAOU or from an AR/WS AOU into an NAOU.
PSDMGR This key should be allocated to the Inpatient Pharmacy Package Coordinator(s) or his/her designee. This lock controls the editing of CS files for package set up. This key locks the Supervisor’s Menu options \[PSD MGR\].
PSDRPH This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement Administration (DEA) regulations, and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.
PSJ PHARM TECH This key should be allocated to pharmacy technicians handling narcotic orders.
PSJ RNURSE This key should be allocated to nurses who request narcotic orders, receive, and administer controlled substances on the wards.
PSJ RPHARM This key should be given to pharmacists dispensing and receiving narcotic orders.
Satellite Vault An NAOU set up as a secondary dispensing site.
Stock Drug A drug (from the drug file) stored in an NAOU.
Stock Level The quantity of a drug stocked in a specific NAOU.
V*ist*A Veterans Health Information Systems and Technology Architecture
Ward (for Drug) The name of the ward or wards that will use this particular
> drug. It is important to accurately answer this prompt because this is the link between the Unit Dose package and the Controlled Substances package. The Unit Dose package looks at this field to know if the drug is a Controlled Substances stocked drug.

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Activity Report, 4
B
Balance Adjustments - NAOU, 23
barcode labels, 5
C
Check on Priority Orders, 12
Completing a Green Sheet - Ready for Pickup, 15
CS Order Entry For Ward, 9
D
Delayed Sign Out Dose for Patient, 22
Delivered-Actively on NAOU, 15
Delivered-Perpetual Inventory, 15
E
Electronic Signature, 1, 20
E-mail, i
Expiration Date Report, 26
F
Filled not Delivered, 15
G
Green Sheet History, 15
H
Help Online, 19
I
Infusion or PCA Syringe Order Entry For Patient, 10
Initialize NAOU Drug Balance, 22
M
multiple orders, 9
N
Narcotic Count - Shift Report, 18
Not Given, Return to Stock, 7
Nursing Supervisor Menu, 21
O
One-Time Request, 9
Order Entry Banner, 33
ORDER ENTRY BANNER, 10
Orders Filled Not Delivered, 12
Orientation, 1
P
Patient ID List Print, 5, 21
Patient/Location Inquiry, 23
Pending CS Orders Report for an NAOU, 12
PSD ERROR, 34
PSD NURSE, 34
PSD PARAM, 34
PSD TECH, 34
PSD TECH ADV, 35
PSD TRAN, 35
PSDMGR, 35
PSDRPH, 35
PSJ PHARM TECH, 35
PSJ RNURSE, 36
PSJ RPHARM, 36
R
Ready for Pick Up, 15
Receipt of Controlled Substance from Pharmacy, 15, 17
*Receipt of Controlled Substances from Pharmacy*, 12
Receive Green Sheet & Drug from another NAOU, 16
Receive GS for PCA/Infusion Signed Out to Patient, 16
Record Defective Dose, 8
Record Delayed Wastage, 6
Report of Balance of drugs on NAOU, 18
Reprint Transfer Between NAOUs, 16
S
Scheduled Delivery, 9
Sign Out Doses for Patients, 3
Steps to Prepare a Ward (NAOU) for use of a Radio Frequency Device, 27
T
Transfer Green Sheet and Drug to another NAOU, 15
Transfer Green Sheet Menu, 15
Transfer GS for PCA/Infusion Signed Out to Patient, 16
Transferred Green Sheets - Pending NAOU Receipt, 16
U
Unscheduled Order Report, 23
Unscheduled Pick Up, 9
V
Verify Count, 13
W
Ward (NAOU) Drug History, 17
\< This page intentionally left blank\>
