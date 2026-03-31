---
consolidated_title: "controlled substances pharmacist's user manual"
app_code: PSD
doc_type: UM
master_source: "Controlled Substances Version 3 Pharmacist's User Manual (Updated PSD*3*84)"
master_pub_date: March 1997
consolidated_from: 2 versions
prior_versions:
  - "Controlled Substances Pharmacist's User Manual (Updated PSD*3.0*92)"
---

<!-- image -->

# CONTROLLED SUBSTANCES (CS)

PHARMACIST’S USER MANUAL


March 1997

(Revised November 2018)

<!-- image -->

Product Development

########### Revision History

The table below lists changes made since the initial release of this manual. Use the Change Pages document to update an existing manual or use the entire updated manual.

| **Date**   | **Revised Pages**           | **Patch Number**   | **Description**                                                                                                                                                                                                              |
|------------|-----------------------------|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 11/2018    | 15  -  17                   | PSD*3*84           | Added balance discrepancy modification to the Outpatient Rx’s [PSD OUTPATIENT] option section.  REDACTED                                                                                                                     |
| 08/2018    | 2                           | XU*8.0*679         | Added note regarding Electronic Signature Block restrictions.  REDACTED                                                                                                                                                      |
| 06/2018    | 43                          | PSD*3*82           | Added NAOU Usage Report [PSD NAOU USAGE] option to the PSD TECH ADV key.  REDACTED                                                                                                                                           |
| 09/2017    | 27                          | PSD*3*81           | Updated “Receipt of Controlled Substance from Pharmacy”  [PSD REC GS] Note and option example to describe dispense unit added to controlled substance dispense drug being electronically received with this option. REDACTED |
| 05/2013    | i, 44-47  45a  47-49  50-52 | PSD*3*76           | Updated Glossary with description of patch’s new security key PSDRPH  Page 45a was unnecessary and has been removed  Updated Index  Pages 50 through 52 were unnecessary and have been removed  REDACTED                     |
| 04/2011    | 44-45a                      | PSD*3*71           | Clarified description of PSD TECH ADV key. Corrected option name in PSD TRAN entry.  REDACTED                                                                                                                                |
| 05/2010    | 44-45, 50                   | PSD*3*69           | Added description of patch’s new security key PSD TECH ADV, and PSD TECH key.  PSD TECH and PSD TECH ADV entries added to the Index  REDACTED                                                                                |
| 03/1997    |                             |                    | Original Released Pharmacist’s Guide.                                                                                                                                                                                        |

&lt;This page is intentionally left blank.&gt;

Preface

The Controlled Substances (CS) software package is one segment of the Veterans Health Information Systems and Technology Architecture ( **V** *IST* **A** ) installed at VA medical centers. The Controlled Substances module provides functionality to monitor and track the receipt, inventory, and dispensing of all controlled substances. This module provides the pharmacy with the capability to define a controlled substance location and a list of controlled substances to maintain a perpetual inventory.

This software provides the capability for pharmacy personnel to receive a Controlled Substances order, automatically update the quantity on hand, and view a receipt history. Nursing personnel are provided with the ability to request orders for Controlled Substances via on-demand requests. Pharmacy may dispense controlled substances via the software automating all necessary documents (VA FORMS 10-2321 and 10-2638) to complete an order request. The software provides functionality to record AMIS and Cost data, address returns to stock, destructions, order cancellations, transfers between locations, and log outpatient prescriptions.

Monthly (or more frequent) inspections can be conducted by management, with discrepancies in stock levels automatically identified.

Controlled Substances (CS) Version 3.0 will provide many new enhancements for both pharmacy and nursing users.

A list of the new additions and modifications to existing options that will be discussed in this document follows:

Batch Order Entry process

Electronic Signature

HL7 Interface to Narcotic Dispensing Equipment

Electronic Error &amp; Enhancement Requests (E3Rs)

Green Sheets now print on plain paper

Other Enhancements

This software is continually being enhanced to provide additional options and capabilities. The CS Development Team encourages you to send to them questions and comments about the completeness and accuracy of this manual and suggestions for its improvement. Electronic mail messages can be sent to REDACTED.

&lt;This page is intentionally left blank.&gt;

## **Table of Contents**

CONTROLLED SUBSTANCES (CS)	i

PHARMACIST’S USER MANUAL	i

Pharmacist User Manual	1

Orientation	2

Electronic Signature	2

Intranet	3

Receipts Into Pharmacy	4

Receiving	4

Purchase Order Review	5

Control Point Transaction Review	5

Drug Receipt History	5

Invoice Review (Prime Vendor)	5

Dispensing Menu	6

Print CS Dispensing Worksheet	6

Fill/Dispense CS Orders from Worksheet	6

Dispensing/Receiving Report (VA FORM 10-2321)	8

Green Sheet—Print (VA FORM 10-2638)	8

Reprint Reports Menu	9

Reprint Disp/Receiving Report (VA FORM 10-2321)	9

Green Sheet Reprint (VA FORM 10-2638)	9

Dispensing Worksheet Reprint	9

Label Reprint for Dispensing Drug	10

Reprint Transfer Between NAOUs (VA FORM 10-2321)	10

Pharmacy Dispense without (VA FORM 10-2638)	11

Label for Dispensing (Barcode)	11

Narcotic Dispensing Equipment Orders	12

Complete Green Sheet	13

Outpatient Rx’s	15

Transfer Drugs between Dispensing Sites	18

Infusion Order Processing Menu	19

Infusion Order Entry	19

Transfer Green Sheet and Drug to another NAOU	20

Destructions Menu	21

Hold a CS Drug (No Inventory Update)	21

Non—VA Drug Placed on Hold for Destruction	21

Destroy a Controlled Substances Drug	21

CS Order Entry For Ward	22

Receipt of Controlled Substances from Pharmacy	24

Load Software and Inventory into TRAKKER	25

Send Vault TRAKKER Inventory Data to DHCP	28

Manufacturer, Lot #, and Exp. Date—Enter/Edit	30

Glossary	31

Index	39

## ## Pharmacist User Manual

########### 

## Orientation

Within the terminal dialogues used as examples in this manual, the user’s input is underlined and bolded. Whenever the Return/Enter key should be pressed, you will see the symbol **&lt;RET&gt;** . Whenever you see the underline and bold representing the user’s input, you can assume the Return/Enter key was pressed.

## Electronic Signature

In Controlled Substances, the Electronic Signature functionality will be used for identification for pharmacy personnel, nursing personnel, and narcotic inspectors.

Identification will be used to reconfirm the identity of the user at the keyboard before proceeding with the next step in a critical process.

In the documentation, when your Electronic Signature Code is to be entered, it is represented as **XXXXXX** .

If you have not previously been issued an Electronic Signature code you can assign yourself one at any menu option by entering TBOX and then choosing Edit Electronic Signature Code. You can also enter “EDIT E and follow the prompts as shown below.

**Note:** If the SIGNATURE BLOCK PRINTED NAME and SIGNATURE BLOCK TITLE fields are disabled at your site, contact your supervisor to request entry of your name and title.

Electronic Signature Codes

This option is designed to permit you to enter or change your

Initials, Signature Block Information and Office Phone number.

In addition, you are permitted to enter a new Electronic Signature Code

or to change an existing code.

INITIAL: **OAC**

SIGNATURE BLOCK PRINTED NAME: **ONE A. CSNURSE**

SIGNATURE BLOCK TITLE: **R.N.**

OFFICE PHONE: **555-7101**

ENTER NEW SIGNATURE CODE: **XXXXXX** (Signature Code will not appear on screen)

RE-ENTER SIGNATURE CODE FOR VERIFICATION: **XXXXXX**

DONE

*TIP: It may help to use your access code as your Electronic Signature Code, this will help eliminate the possibility of forgetting it!*

## Intranet

We are now on the intranet, come visit us. REDACTEDThis address will take you to the Clinical Products page where you will find a listing of all the clinical software manuals and other software manuals. Click on the Controlled Substances (CS) link and it will take you to the CS Homepage. You can also get there by going straight to REDACTED. (don’t forget to bookmark it!)

In addition, both of these homepages have a Software Service Homepage link. Simply click on this link and then follow the links to the manuals you would like to see.

## Receipts Into Pharmacy

Use this option to process receipts for purchase orders, control point transactions, and Prime Vendors.

########### Receiving

The processing of receipts for Prime Vendor and IFCAP purchase orders are handled slightly different.

First a Master Vault must be flagged as eligible for Prime Vendor receipts. The option will enable pharmacy personnel to acknowledge whether the receipt is from a Prime Vendor.

If it is, the system will default to the Control Point Transaction number and the purchase order number (1358 obligation number) currently stored for that Master Vault.

If the entry that is being entered does not coincide with the current month’s activity, the user can correct the entry. When all the data has been entered, the files will be updated and the receipt posted.

**Example:**

Select Receipts Into Pharmacy Option: **REC** eiving

Select Dispensing Site: MAST VAU// &lt;RET&gt;

Is this a Prime Vendor receipt? Yes// **&lt;RET&gt;** YES

Current Prime Vendor P.O.#: 521-A00016  Date Assigned: JUN 19,1995@16:02

Select Pharmacy Purchase Order Number: 521-A00016// **&lt;RET&gt;** 06-19-95  ST   Order Not Completely Prepared     FCP: 023     $ 0.00

Select Pharmacy Transaction number: 521-95-3-023-0013// **&lt;RET&gt;** OBL  MEAD JOHNSON A00016     KASLKJSADFLDSA

Please enter the Prime Vendor Invoice number: &lt;RET&gt;

Enter your Current Signature Code: **XXXXXX** SIGNATURE VERIFIED

Select MAST VAU drug: **&lt;RET&gt;**

########### Purchase Order Review

All receiving history for a selected Purchase Order number can be reviewed or printed. Each drug receipt will be listed along with the date, drug, quantity, and receiver.

########### Control Point Transaction Review

This option will allow you to print the receiving history for a selected Control Point Transaction. Each drug receipt will be listed with the date, drug, quantity, received by within receiving site.

########### Drug Receipt History

By using this option you can see the receiving history for a selected drug or pharmaceutical. You may view or print the information which will list the drug, date, quantity, received by, Purchase Order number, Transaction number, and Invoice number within receiving site.

########### Invoice Review (Prime Vendor)

This option will list all receipts by date, drug, quantity, and received by within receiving site that have been posted for a selected Prime Vendor invoice number.

## Dispensing Menu

This menu contains access to all options associated with the dispensing of Controlled Substances drugs.

########### Print CS Dispensing Worksheet

This option will sort and print all Controlled Substances pending request/orders for a Dispensing site. If orders were previously printed on a worksheet and NOT PROCESSED they will print on every subsequent worksheet printed regardless of what you selected.

The worksheet MUST be printed prior to a pharmacist dispensing a Controlled Substances order. Each time this report is run, a new worksheet will be built and all new CS orders will be included. The printed sequence of CS orders will change with each new worksheet.

The Pharmacy Dispensing Worksheet Summary List will **always** print in drug name then NAOU sequence regardless of the sort selection made.

########### Fill/Dispense CS Orders from Worksheet

This option is used by Pharmacy personnel to process and verify Controlled Substances orders. The information required to process this option is obtained from the Print CS Dispensing Worksheet. Therefore it is imperative that you have a current worksheet list in front of you when using this option.

**Example:**

Select Dispensing Menu Option: **FIL** L/Dispense CS Orders from Worksheet

Select Primary Dispensing Site: MAST VAU// &lt;RET&gt;

Dispensing Method:  (W/R): **W** orksheet

Enter your Current Signature Code: **XXXXXX** SIGNATURE VERIFIED

Accessing worksheet information...

*screen displayt follows*

Controlled Substance Order Request

Pharmacy Dispensing #:

Requested by    : CSPROVIDER,ONE                     Request Date: JAN 4,1997

------------------------------------------------------------------------------

Drug            : ACETAMINOPHEN W/CODEINE 15MG TAB      Quantity: 50

Dispensed by    : CSNURSE,TWO                     Dispensed Date:

Disp. Location  : MAST VAU

Manufacturer    : JOHNSON

# : 6789

Exp. Date       : SEP 1994

Ord. Location   : WEST 4

Order Status    : ORDERED - NOT PROCESSED

Comments:

SAMPLE

Old Balance: 605                   New Balance: 555

ACTION (V DC E B S): **V** ERIFY

Assigning Pharmacy Dispensing #...

PHARMACY DISPENSING # 499

Accessing the order...

Old Balance : 605                  New Balance :555

Updating the transaction...vault activity...worksheet...order...done.

This order is now FILLED - NOT DELIVERED.

Press &lt;RET&gt; to continue **&lt;RET&gt;** *[If you press return here you will be shown order after order until you either uparrow (^) out or cycle through all of the orders]*

########### Dispensing/Receiving Report (VA FORM 10-2321)

This report lists all the CS orders with an order status of “Filled not Delivered.” It will list by one, some, or All Narcotic Areas of Use. Signature(s) are required for the pharmacist who fills/dispenses the CS drugs and the nurse receiving the CS drugs. The technician delivering the CS drugs is required to sign the vault copy.

The report format has been modified for the vault copy only to: print a drug balance under the drug name and print an asterisk next to quantity and balance, but only if the original quantity ordered has been edited. A legend will now print at the bottom of the page.

The report can reflect more than one order being delivered to an NAOU and is retained by pharmacy.

########### 

########### Green Sheet—Print (VA FORM 10-2638)

This option will enable pharmacy personnel to print a single Green Sheet or a range of Green Sheets that have not been previously printed.

**Note:** Make sure that IRMS has updated your device settings (these are 	documented in the Controlled Substances Technical Manual in the 	Resource Requirements section) so that Green sheets will be properly 	formatted on plain paper.

########### 

########### Reprint Reports Menu

This menu allows various narcotic reports and forms to be reprinted. To ensure drug accountability, certain Controlled Substances documents should only be printed once. This option allows the reprinting of these controlled records.

################################ Reprint Disp/Receiving Report (VA FORM 10-2321)

The Dispensing/Receiving Report (in lieu of the VA FORM 10-2321) can be reprinted for a single Green Sheet or NAOUs.

The report format has been modified for the vault copy only to: print a drug balance under the drug name and print an asterisk next to quantity and balance, but only if the original quantity ordered has been edited. A legend will now print at the bottom of the page.

If you select **N** for NAOU, you will be prompted for a start and end date and time. Enter the original date and time of the report. If you select **G** for Green Sheet #, you will not be prompted for the date and time of the report.

This report will require the signature of the dispensing pharmacist, the nurse receiving the report, and the technician delivering the orders will be required to sign the vault copy.

################################ Green Sheet Reprint (VA FORM 10-2638)

Pharmacy uses this option to reprint a single Green Sheet.

################################ Dispensing Worksheet Reprint

This option will reprint a dispensing worksheet. The previously printed dispensing worksheet, for a given site is utilized in reprinting this worksheet listing.

These orders are sequenced by the sort selected during the original printing of the worksheet. If an order has been processed by pharmacy since the original worksheet was printed, the ws# (worksheet number) will display an asterisk (*).

The reprinting process will not generate a new worksheet, that is new orders will not be added to the reprinted worksheet.

################################ Label Reprint for Dispensing Drug

This option enables pharmacy to reprint the dispensing drug barcode label. The labels may be printed by selecting a range of Green Sheet numbers; i.e., dispensing numbers. After being reprinted this label should be affixed to the drug package delivered to the NAOU.

################################ Reprint Transfer Between NAOUs (VA FORM 10-2321)

Pharmacy personnel will be ONLY able to reprint a copy of the VA FORM 2321 for Green Sheets transferred from one NAOU to another NAOU, but have not yet been received on the transferred to NAOU.

The report will show that it is a ***REPRINT*** and print the message ***TRANSFERRED BETWEEN NAOUs*** from NAOU to NAOU.

########### Pharmacy Dispense without (VA FORM 10-2638)

With this option pharmacy can dispense the Controlled Substances drugs from a dispensing site without generating the VA FORM 10-2638. Drugs dispensed using this option **will not** be displayed on the Inspector’s log or usage reports for the NAOUs. These will be included on the Pharmacy Dispensing Report and the Daily Activity Log.

########### Label for Dispensing (Barcode)

This option enables pharmacy to print the dispensing drug barcode label. The labels may be printed by selecting NAOU(s) or a range of Green Sheet numbers; i.e., dispensing numbers. After being printed, this label should be affixed to the drug package delivered to the NAOU.

**Note:** Labels can be printed three across on sheet fed labels or one label 	across, 15/16" high x 2-1/2" wide on pin fed labels.

Dispensing labels may be printed for an order only once. You must use the Label Reprint for Dispensing Drug to reprint labels.

########### Narcotic Dispensing Equipment Orders

This option is for dispensing from Pharmacy to narcotic dispensing equipment systems.

**Example:**

Select Dispensing Menu Option: **NAR** cotic Dispensing Equipment Orders

Enter Controlled Substances Inpatient Site Name: **SITE NAME**

Select Default Dispensing Site: MAST VAU

For now this option is the same as dispense w/o green sheet.

Select Primary Dispensing Site: MAST VAU// &lt;RET&gt;

Select DRUG: **LORAZEPAM 2MG** TAB U/D

Select NAOU: WARD 10

QUANTITY DISPENSED (TAB/20): 20// **&lt;RET&gt;** 20

MANUFACTURER: ROXANE// **&lt;RET&gt;** ROXANE

#: 5235// **&lt;RET&gt;** 5235

EXPIRATION DATE: JUL 17,1996// **&lt;RET&gt;** (JUL 17, 1996)

Is this OK? ? YES// **&lt;RET&gt;**

Creating a dispensing transaction...vault activity

Updating on-hand quantity...done.

Old Balance : 99489                New Balance: 99469

Updating your transaction history...still updating...done.

## Complete Green Sheet

This option enables pharmacy personnel to complete a Green Sheet that has the status of COMPLETE GS PICK UP or DELIVERED ACTIVELY ON NAOU.

All Green Sheets must pass a manual review before entering them into this process. For each Green Sheet number entered the user must select a completion status.

The order status will be updated according to the completion status selected for each Green Sheet.

When the completion status is:

NO DISCREPANCY

RETURNED TO STOCK

TURN IN FOR DESTRUCTION

the order status of the Green Sheet will be updated to COMPLETE - REVIEWED.

When the completion status is:

GREEN SHEET NOT SIGNED BY NURSE

MATH ERROR

OTHER - REFERRED TO PHARMACY SUPERVISOR

the order status of the Green Sheet will be updated to COMPLETE - PENDING PROBLEM RESOLUTION.

If the completion status entered is RETURNED TO STOCK or TURNED IN FOR DESTRUCTION a VA-FORM 10-2321 Narcotic Dispensing/Receiving Report will be generated.

**Example:**

Select Pharmacist Menu Option: **COM** plete Green Sheet

Enter your Current Signature Code: **XXXXXX** SIGNATURE VERIFIED

Select Primary Dispensing Site: MAST VAU// &lt;RET&gt;

Complete a Green Sheet

Select the Green Sheet #: **192** LORAZEPAM 2MG TAB U/D     WEST 4

This Green Sheet is still ACTIVE on the NAOU.

Do you want to continue? **Y** YES

Select Completion Status: **??**

Choose from:

GREEN SHEET NOT SIGNED BY NURSE

MATH ERROR

NO DISCREPANCY

OTHER - REFERRED TO PHARMACY SUPERVISOR

RETURNED TO STOCK

TURN IN FOR DESTRUCTION

Select Completion Status: **TUR** N IN FOR DESTRUCTION

Is this OK? YES// **&lt;RET&gt;**

Quantity of TAB Turned in for Destruction: **2**

RETURNED BY NURSE: **CSNURSE,T** WO

REASON TURN IN FOR DESTROY: **FELL ON FLOOR**

Is this OK? YES// **&lt;RET&gt;**

Accessing Green Sheet information...

Updating your records...nursing records now...done.

*** The status of your Green Sheet #192 ***

COMPLETED - REVIEWED TURN IN FOR DESTRUCTION

Accessing your transaction history...

Creating an entry in the Destruction file...

Your Destruction Holding number is 386

NURSE RETURNING DRUG: **CSNURSE,T** WO // **&lt;RET&gt;**

NO. OF CONTAINERS: 1// **&lt;RET&gt;**

UNIT: TAB// **&lt;RET&gt;**

Number of copies of VA FORM 10-2321? **2**

This report is designed for a 132 column format.

You may queue this report to print at a later time.

DEVICE: *[Select Print Device]*

## Outpatient Rx’s

This option will enable pharmacy personnel to release outpatient prescriptions from their Controlled Substances dispensing vault. For the first release of a prescription in this option, the Outpatient Site parameters must be identified. A controlled substances prescription is initiated in the Outpatient Pharmacy package.

When the pharmacist enters an outpatient prescription the software will display the most recently filled RX (new, refilled, or partial). The RX entered is then scanned for the status to determine if it can be filled and released. An Rx with any of the following statuses: **DELETED** , **HOLD** , **NON-VERIFIED** , **PENDING DUE TO DRUG INTERACTIONS** , **CANCELLED** , and **SUSPENDED** will not be filled and released and a notification message will be issued. Refer to the glossary for an explanation of the statuses.

The pharmacist has the option of using a barcode reader to wand the barcode label for the prescription, manually key in the number that is below the barcode label, or enter the prescription number. The barcode number should follow the format NNN-NNNNNNN.

If the BALANCE DISCREPANCY CHECK field (#37) in the DRUG ACCOUNTABILITY STATS file (#58.8) has been set to "ON" for the dispensing site, the "Enter the remaining balance (^ to quit):" prompt is displayed to record the on-hand count of the remaining balance. If the entry does not match the VistA system count, the user is presented with a second and third opportunity to enter the on-hand count. If the incorrect balance is entered on the third attempt, the user is given the opportunity to enter a comment. After pressing Enter, a message that includes the balance discrepancy information and user's comment is sent to the CS BALANCE DISCREPANCY mail group. After the message is sent, normal processing continues and the user is asked to release the prescription fill. If the user decides to quit during the balance confirmation process, no transaction is recorded. If the correct balance is entered during any of the three entry opportunities, the old and new balances are displayed and the user is prompted to confirm release of the prescription fill.

- **Note:** The CS BALANCE DISCREPANCY mail group should be populated with pharmacy personnel at the site who have access to the Balance Adjustments [PSD BALANCE ADJUSTMENTS] menu to investigate the discrepancy.

- **Note:** The functionality to check the remaining balances can be turned on or off for each dispensing site. To turn the functionality on, a user with access to the Create/Edit the Narcotic Area of Use [PSD NAOU EDIT] option must enter "ON" or "1" at the "BALANCE DISCREPANCY CHECK:" prompt. This prompt only appears when editing a Master Vault dispensing site.

**Example (when Balance Discrepancy Check is ON):**

Select OPTION NAME: PSD OUTPATIENT       Rx's

Outpatient Rx's

Controlled Substances Inpatient Site Name: CHEYENNE

Select Default Dispensing Site:    OUTPATIENT CART

Enter your Current Signature Code:    SIGNATURE VERIFIED

Select Primary Dispensing Site: OUTPATIENT CART//

Please identify Pharmacist for Outpatient Release: ONE,PHARMACIST//   PO

PHARMACIST

Enter/Wand PRESCRIPTION number: 891675

Accessing the prescription history...

Select one of the following:

1         Original

Enter response: 1  Original

View Controlled Substances Rx # 891675

SEP 4,2018

---------------------------------------------------------------------------

Location: OUTPATIENT CART                           Original

Drug:     OXYCODONE 5MG &amp; ACETAMINOPHEN 325MG TAB   Quantity: 1

Patient:  ONE,PATIENT  (0123)                       Original Date: 09/04/18

Enter the remaining balance (^ to quit):

This is a required response. Enter '^' to exit

Enter the remaining balance (^ to quit):  12

Sorry the remaining balance you entered does not match the balance

on record in the CS package.

Please check to ensure you have dispensed the right drug and

dispensed the correct quantity.

Enter the remaining balance (^ to quit):  23

This will be the last entry in the remaining balance check.

If the entry still does not match a message will be sent to the

appropriate person for review.  You may proceed if you have dispensed the

correct drug in the correct quantity.  Thank you.

Enter the remaining balance (^ to quit):  422

Enter a comment (^ to quit): TESTING SWITCH ON

Message sent to the CS BALANCE DISCREPANCY Mail Group

You entered a remaining balance of 422

Old Balance: 1650        New Balance: 1649

Is this OK? YES//

Creating an Outpatient Transaction...updating...vault activity...done.

Outpatient Pharmacy software - Version 7.0

The Rx (Prescription) Outpatient Dispensing Report is available from the *Production Reports* Option (this is documented in the Controlled Substances Supervisor’s User Manual).

- **Note:** You will not be able to release a prescription before a label has been 	printed.

- **Note:** All prescription labels are printed in the Outpatient Pharmacy package if 	the prescription is to be filled and released.

- **Note:** The Outpatient Rx’s option prevents the releasing a controlled substance prescription if the CMOP status is transmitted, dispensed or retransmitted. Controlled substance prescriptions with the status of ‘Not dispensed’ shall be releasable.

## Transfer Drugs between Dispensing Sites

With this option pharmacy personnel are able to transfer Controlled Substances between dispensing sites, the inventory balances are updated at this time within each dispensing site.

**Note** : When drug(s) are being transferred from one dispensing site into 	another, a MailMan message will be generated to the pharmacy supervisor 	holding the PSDMGR security key, only if the receiving dispensing site 	does not normally stock a particular drug(s).

To obtain a listing of these transfers use the *Transfer Drugs between Dispensing Sites* option on the *Production Report Menu* .

**Example:**

Select Pharmacist Menu Option: **TRA** nsfer Drugs between Dispensing Sites

Enter your Current Signature Code: **XXXXXX** SIGNATURE VERIFIED

Transfer from Dispensing Site: **WEST** 26

Select DRUG From west 26: **ACET**

1   ACETAMINOPHEN W/CODEINE 15MG TAB             CN101

2   ACETAMINOPHEN W/CODEINE 30MG TAB             CN101

CHOOSE 1-2: 2

Breakdown Unit:               Package Size:

Enter Quantity to Transfer:  (1-1): **1**

Transfer to Dispensing Site: SOUTH 3

** SOUTH 3 does not stock ACETAMINOPHEN W/CODEINE 30MG TAB! **

Do you want to continue? **Y** YES

Transferring: 1 ()

From: west 26    To: SOUTH 3

Is this OK? NO// **Y** YES

Updating vault on-hand balances now...west 26...

Still updating...SOUTH 3...

Still updating...done!

........

## Infusion Order Processing Menu

This menu contains the infusion order/entry and transferring a Green Sheet options associated with the IV pharmacist processing a Controlled Substances infusion order.

########### Infusion Order Entry

The IV pharmacist uses this option to electronically request Controlled Substances drugs used in IV orders. Only infusion orders requiring the VA FORM 10-2638 should be requested using this option.

**Order Entry Steps**

1.  Set up IV room as an NAOU.

2.  Enter Drugs as stock items that will be used.

(Orders placed through Inpatient Meds IV order process requiring a Controlled Substance will use this next process.)

3.  IV pharmacist will be placing orders through Infusion Order Entry

option.

4.  Orders will now be processed through normal Controlled Substances 	process at this point.

5.  The drugs, along with the dispensing receiving report (in lieu of VA

FORM 10-2321), and the Green Sheet VA FORM 10-2638 will be delivered 	to the IV pharmacist.

6.  The IV pharmacist will log any unused portion of the Controlled

Substances as wasted on the Green Sheet.

7.  IV pharmacist will then transfer the Green Sheet and drug to the

requesting NAOU.

########### Transfer Green Sheet and Drug to another NAOU

This option will enable nurses to transfer Controlled Substances drugs and their associated Green Sheets to another NAOU. The transfer of Controlled Substances drugs between NAOUs requires two processing steps.

Step 1 - The Green Sheet and Drug must be transferred to an NAOU.

Step 2 - The Green Sheet and Drug must then be received on that NAOU.

## Destructions Menu

This menu allows pharmacy supervisors to maintain the necessary records when destroying a Controlled Substances drug.

########### Hold a CS Drug (No Inventory Update)

This option allows pharmacy supervisors to place a Controlled Substances VA drug, from the DRUG file (#50), on hold for destruction. When using this option, the Controlled Substances inventory balance will not be updated. A CS DESTRUCTION file (#58.86) entry is made and is now able to be traced through the CS software. A 60 character comments field has been added enabling pharmacy to enter a reason for drugs returned.

########### Non—VA Drug Placed on Hold for Destruction

This option allows the pharmacy supervisors to place a non—VA drug, not existing in the DRUG file (#50), on hold for destruction. A CS DESTRUCTIONS file (#58.86) entry is made and traceable through the CS software.

########### Destroy a Controlled Substances Drug

This option provides the supervisor with the ability to enter the destruction information for any Controlled Substances drug being destroyed.

########### 

## CS Order Entry For Ward

This option enables pharmacy personnel to electronically enter manual Controlled Substances requests from the nursing wards that require the VA FORM 10-2638. You will be shown any pending orders and will be asked to approve or delete them before being able to enter a new one.

These order requests entered by pharmacy personnel are not restricted to the ordering multiples established by the package size.

**Example:**

Select Pharmacist Menu Option: **CS O** rder Entry For Ward

Select Ordering NAOU: WARD 10

THIS IS THE ORDER ENTRY BANNER

Scheduled Delivery or Unscheduled Pick Up (S/U): **SCH** eduled Delivery//

Searching for TWO SCNURSE’S pending requests..

Accessing pending requests for TWO CSNURSE...

THIS IS THE ORDER ENTRY BANNER

The following request(s) may be approved or deleted:

# DATE ORDERED     DRUG                               QUANTITY

1  FEB 26,1997  ACETAMINOPHEN W/CODEINE 30MG TAB                           1

Approve or Delete (A/D): Approve// **&lt;RET&gt;**

Enter your Current Signature Code: **XXXXXX** SIGNATURE VERIFIED

Processing your request #1 now...  No pending requests.

Select DRUG: **ACETAMINOPH** EN W/CODEINE 30MG TAB

Searching for pending orders...

Orders pending: 5  Quantity Ordered (TAB): 22

Do you wish to cancel any pending orders? NO// **&lt;RET&gt;**

No orders cancelled.  Continue processing your order.

Maximum quantity per order:  100 TAB

QUANTITY (TAB/1): 1// **&lt;RET&gt;**

processing now...

COMMENTS:

1&gt; **NEED FOR PATIENT**

2&gt; **&lt;RET&gt;**

EDIT Option: **&lt;RET&gt;**

Select DRUG: **&lt;RET&gt;**

Accessing pending requests for TWO CSNURSE...

THIS IS THE ORDER ENTRY BANNER

The following request(s) may be approved or deleted:

# DATE ORDERED     DRUG                                         QUANTITY

1  FEB 26,1997  ACETAMINOPHEN W/CODEINE 30MG TAB                           1

Approve or Delete (A/D): Approve// **&lt;RET&gt;**

Enter your Current Signature Code: **XXXXXX** SIGNATURE VERIFIED

Processing your request #1 now...

########### 

## Receipt of Controlled Substances from Pharmacy

This option enables pharmacy personnel to electronically receive CS orders for the nursing wards.

**Note:** Patch PSD*3.0*81 modifies the “Receipt of Controlled Substance from Pharmacy” [PSD REC GS] option to include the dispense unit (ML, TAB, CAP, etc) of the controlled substance dispense drug being electronically received into the Narcotic Area of Use (NAOU).

**Example:**

Select Pharmacist Menu Option: **REC** eipt of Controlled Substance from Pharmacy

Receive Controlled Substances Orders and Green Sheet

Enter your Current Signature Code: **XXXXXX** SIGNATURE VERIFIED

Select NAOU: WEST 4

Select the Green Sheet #: **458** LORAZEPAM 2MG TAB U/D     WEST 4

Accessing LORAZEPAM 2MG TAB U/D information...

QUANTITY RECEIVED (TAB): 20// **&lt;RET&gt;** 20

Updating your records now...done.

*** Your Green Sheet #458 is now DELIVERED - PERPETUAL INVENTORY ***

Select the Green Sheet #: **&lt;RET&gt;**

Barcode TRAKKER for Inventory

This menu contains the options associated with performing narcotic vault inventories using the barcode TRAKKER device.

########### Load Software and Inventory into TRAKKER

This option enables pharmacy personnel to download an IRL program to the TRAKKER, download the vault drug balances to the TRAKKER, and perform the inventory via the TRAKKER.

**Example :**

Turn the TRAKKER on and the following will be displayed

Select Pharmacist Menu Option: **BAR** code TRAKKER for Inventory

Load Software and Inventory into TRAKKER

Send Vault TRAKKER Inventory Data to DHCP

Select Barcode TRAKKER for Inventory: **LO** ad Software and Inventory into TRAKKER

Select Dispensing site to Inventory: INPATIENT// **&lt;RET&gt;**

*[You will only be asked this question if you have more than one dispensing vault defined for your site. If you select a default dispensing site upon entering your Controlled Substances menu, it will be offered as a default.]*

Compiling inventory data...

DEVICE: **TRAKKERSL**

TRAKKER information follows

*[You will see the IRL program scroll as it is being downloaded to the TRAKKER.]*

*[After the IRL program has been downloaded the following message will appear on your terminal:]*

Awaiting TRAKKER signal

printout follows

*[After the data has been downloaded the following message will appear on your terminal]*

You can now disconnect the TRAKKER.

*[At this point the TRAKKER will go back and display the two available options.]*

*[When you enter a 1, the system will ask you to identify yourself (scan your ID badge) and to identify the drug (scan the drug label).]*

*[The system will check the files for a match. If no match is found, the system will inform the user that this drug is not in the files. If a match is found, the drug*

*name and quantity will be displayed as follows]*

*[Scan your user ID barcode]*

*[At this point you have the option to enter an N to adjust the count.]*

########### 

########### Send Vault TRAKKER Inventory Data to DHCP

This option enables pharmacy personnel to upload the inventory data from the TRAKKER to .

**Example :**

Load Software and Inventory into TRAKKER

Send Vault TRAKKER Inventory Data to DHCP

Select Barcode TRAKKER for Inventory: **SEN** d Vault TRAKKER Inventory Data to DHCP

*[Use the Send data to DHCP option on the TRAKKER at this time]*

*[When you press F1 the data will print across your terminal screen]*

P123-45-6767^&gt;94/08/22:10:23:44*12

P123-45-6767^614^DIAZEPAM 2MG TAB^337^^^^335^^^^&gt;94/08/22:10:24:07

P123-45-6767^614^DIAZEPAM 2MG TAB^335^^^^^^^^&gt;94/08/22:10:24:22

P123-45-6767^615^DIAZEPAM 10MG TAB^421^^^^^^^^&gt;94/08/22:10:24:22

**Note:** *[You will get conformation on your TRAKKER that the information was sent, press the 	return key on your terminal and you should see this message]*

Updating DHCP now...done

*[Anyone holding the appropriate security key {PSD ERROR] will also receive a MailMan message on the adjustment.]*

**Example: MailMan message**

Subj: CS PHARM TRAKKER ADJUSTMENT  [#3194] 22 Aug 94 13:23  7 Lines

From: CONTROLLED SUBSTANCES PHARMACY  in 'IN' basket.   Page 1

------------------------------------------------------------------------------

CS PHARM TRAKKER adjustment/error has been filed.

Adjustment/Error Date/Time: AUG 22,1994@13:23:46

Dispensing Site: INPATIENT

Drug: DIAZEPAM 2MG TAB

Quantity Adjusted: -3

Adjusted by: PHARMACIST,JOE Q.

**Note:** Data should be cleared out or deleted from the TRAKKER to avoid

duplication of inventory information.

After the upload is completed you should clear the TRAKKER’s data files. To accomplish this, press [Ctrl]-[enter]-[E] to end the IRL session, then press

[Ctrl]-[enter]-[C], you will be asked if you want to clear the data files, enter **Y** (YES).

To restart the IRL session press [Ctrl]-[enter]-[B].

## Manufacturer, Lot #, and Exp. Date—Enter/Edit

Use this option to edit the Manufacturer,  #, and Expiration date for stocked drug(s) in the Drug Accountability Stats file. The drug must first have been added through the *Stock CS Drugs—Enter/Edit* option. This field, when defined, will be printed on the Pharmacy Dispensing Report and displayed on the CS request orders to pharmacy.

## ## Glossary

**Action Prompt** There are two action prompts that occur during the 	pharmacy dispensing process. The action codes 	used with these prompts will appear in ( ). The 	following codes are valid:

**V** Verify or Dispense the order (Displayed

only to the dispensing pharmacist).

**P** Process or Fill the order (Displayed only 	to the pharmacy technician or pharmacist

filling but not dispensing the order).

**DC** Cancel the order.

**E** Edit the order.

**B** Bypass the order.

**S** Show the order.

**Completion Status** A review status is attached to each Controlled 	Substances Green Sheet returned to pharmacy. 	The following are valid:

**NO DISCREPANCY—** No discrepancy found.

**TURN IN FOR DESTRUCTION—** CS drug turned in to be destroyed.

**RETURNED TO STOCK** —CS Drug returned to stock. The dispensing site inventory balance will be updated.

**MATH ERROR** —CS drug discrepancy found.

**GREEN SHEET NOT SIGNED BY NURSE** —GS missing nurse’s signature.

**OTHER—REFERRED TO PHARMACY SUPERVISOR** —CS drug discrepancy referred to supervisor for resolution.

**Daily Activity Log** The Daily Activity Log lists data, within a 	selected date range, associated with the VA FORM 	2320 for a dispensing site.

**Dispensing Number** Control number assigned by pharmacy when 	dispensing a Controlled Substances drug. This 	number is used to track the Green Sheet and drug.

Also referred to as the Disp #, Green Sheet #, GS #, 	or transaction # throughout the CS package.

**Dispensing/Receiving Report** This report can be printed in lieu of VA FORM

**(in lieu of VA FORM 10-2321)** 2321 and lists all Controlled Substances orders 	dispensed to an NAOU. The signatures of the 	dispensing pharmacist and the nurse receiving the 	drug are required.

**Dispensing Site** An NAOU set up as a pharmacy vault that 	dispenses Controlled Substances drugs.

**Dispensing Worksheet** This worksheet compiles a list of all pending 	Controlled Substances request orders for a 	selected dispensing site. A worksheet number, 	drug name, quantity ordered, requesting NAOU, 	ordered by, comments, and blanks for pharmacy 	dispensing number, manufacturer, lot number, 	and expiration date are listed on the worksheet.

**Drug Address Code** A code that represents the location of

**(Location Code)** a drug in the NAOU. For example, if TYLOX is 	stored in an NAOU on the second set of shelves, 	third shelf from the top, its drug address code could 	be expressed as S,2,3. The address code can consist 	of up to three levels separated by a comma. Each 	level should further define the exact location. The 	code is associated with an expansion code for 	clarity.

**Drug Address Code** Text used to clarify the meaning of a drug

**Expansion** address code. For example, the code S would be

expanded and printed as shelf. (These codes and

expansions are locally created terms.)

**Green Sheet** The CONTROLLED SUBSTANCE 	ADMINISTRATION RECORD (VA FORM 10-2638) 	is referred to as a Green Sheet or GS throughout 	the CS package. Pharmacy dispensing number, 	drug name, expiration date, quantity dispensed, 	lot number, ordered by, dispensed by, and ward 	(NAOU) are printed on the form.

**Green Sheet number** Control number assigned by pharmacy when 	dispensing a Controlled Substances drug. This 	number is used to track the Green Sheet and 	drug. It is also referred to as the GS #, 	dispensing #, or disp #, or transaction # 	throughout the CS package.

**Interactive Reader** The Interactive Reader Language (IRL) is a

**Language (IRL)** language used to write programs on barcode 	readers that allow the readers to interact with the 	user.

**Intranet** A company wide computer network available via 	modem that connects users.

**Inpatient Site** Inpatient Site must be defined for each NAOU. 	The Controlled Substances software utilizes this 	data to distinguish multi-divisional sites.

**Inspector’s Log** This report lists all active Green Sheets by NAOU.

It includes the following information: Green Sheet

#, drug name, date dispensed, quantity dispensed,

expiration date (if available), blanks for quantity

on hand, and a signature blank for verification.

**Master Vault** An NAOU set up as your primary dispensing site.

**NAOU - Narcotic Area** A Narcotic Area of Use (NAOU) is a place where

**of Use** commonly stocked Controlled Substances drugs 	are stored for use by pharmacy, wards or 	treatment areas. There are three types of NAOUs: 	1) Master Vault, 2) Satellite Vault, and 3) Narcotic 	Locations.

**NAOU Inventory Group** An NAOU Inventory Group is defined by 	pharmacy to represent the Narcotic Areas of Use 	which are inventoried together as a group. By 	grouping the commonly inventoried NAOUs under 	an easy to remember group name, the elements of 	the inventory are established, and do not have to 	be redefined every time an inventory is scheduled.

**Narcotic Location** An NAOU set up for the nursing wards, 	pharmacy IV room, or a pharmacy working stock 	area. **Order Entry Banner** Provides a free text field as a site parameter to 	appear upon Nursing CS Order Entry. When the 	user accesses the following 3 options, the free text 	field will be displayed:

1) Nursing Order Entry

2) Pharmacy Order Entry from Nursing

3) Infusion Order Entry

**Order Status** A processing status is attached to each Controlled 	Substances request order. The following are valid:

**REQUESTED—NOT ORDERED**

Requests created by batch processing but not yet approved.

ORDERED—NOT PROCESSED

Ordered by nursing but not processed by pharmacy.

**PROCESSED—NOT DISPENSED** Processed  (filled) by pharmacy but not yet dispensed.

**FILLED—NOT DELIVERED** Dispensed and verified by pharmacy but not delivered to the requesting NAOU.

**DELIVERED—ACTIVELY ON NAOU** Drug stored on the NAOU.

**COMPLETED—GREEN SHEET READY FOR PICKUP** Nursing has flagged the Green Sheet ready for pharmacy pickup.

**COMPLETED—GREEN SHEET PICKED UP** Green Sheet returned to pharmacy but not yet reviewed.

**COMPLETED—REVIEWED** Pharmacy has reviewed the Green Sheet .

**COMPLETED—PENDING PROBLEM**

**RESOLUTION** Pharmacy has reviewed the Green Sheet and a problem exists

**CANCELLED** Order cancelled.

**TRANSFERRED TO ANOTHER NAOU** Order and drug transferred to another NAOU.

**UNDER REVIEW BY INSPECTOR** Order and drug pulled from NAOU by CS Inspector for review.

**LOGGED BY TRAKKER** All drug doses from this order have been logged out to patients using the TRAKKER. (Not currently used in Version 2.0.)

**Prescription Status** A prescription can have one of the following status.

**CANCELLED** This term is now referred to throughout the software as Discontinued.(See Discontinued.)

**DELETED** This status is used when a prescription is deleted. Prescriptions are no longer physically deleted from the system, but marked as deleted. Once a prescription is marked deleted no access is allowed other than view.

**HOLD** A prescription that was placed on hold due to reasons determined by the pharmacist.

**NON-VERIFIED** There are two types of non-verified statuses. Depending on a site parameter, prescriptions entered by a technician do not become active until they are reviewed by a pharmacist. Until such review, they remain non-verified and cannot be printed, canceled or edited except through the Verification menu.

The second non-verified status is given to prescriptions when a drug/drug interaction is encountered during the new order entry or editing of a prescription.

**PENDING** A prescription which has been entered through OERR.

**SUSPENDED** A prescription which will be filled at some future date.

**PSD ERROR** This key should be allocated to pharmacy 	supervisors responsible for maintaining the 	narcotic vault. This key controls access to reports 	listing various error and exception conditions 	generated when entries are filed from the barcode 	TRAKKER. Also, the holders of this key will 	receive electronic mail messages created by using 	the TRAKKER.

**PSD NURSE** This key should be allocated to nurses, usually LPNs, who may only receive and administer controlled substances but cannot place the order requests.

**PSD PARAM** This key should be allocated **only** to the Inpatient 	Pharmacy Package Coordinator(s). This lock 	controls the printing of the Green Sheets and the 	range of automated dispensing numbers for a 	dispensing site (vault).

**PSD TECH** Allocate this key to control substance technicians. This key controls access to the *List On-Hand Amounts* [PSD ON-HAND TECH], *Transfer Drugs between Dispensing Sites Report* [PSD PRINT VAULT TRANSFERS TECH], and the *Daily Activity Log (in lieu of VA FORM 10-2320)* [PSD DAILY LOG TECH] options on the Technician (CS Pharmacy) Menu [PSD PHARM TECH].

**PSD TECH ADV** Allocate this key to specific control substance technicians who perform advance functions. This key controls access to the *Receipts Into Pharmacy* [PSD RECEIPTS MENU], *Dispensing Menu* [PSD DISPENSING MENU], *Destructions Menu* [PSD DESTROY MENU], *Manufacturer, Lot #, and Exp. Date - Enter/Edit* [PSD MFG/LOT/EXP], *Outpatient Rx's* [PSD OUTPATIENT], *Complete Green Sheet* [PSD COMPLETE GS], *Destroyed Drugs Report* [PSD DEST DRUGS REPORT], *DEA Form 41 Destroyed Drugs Report* [PSD DESTROY DEA41], *Destructions Holding Report* [PSD DESTRUCTION HOLDING], *Add Existing Green Sheets at Setup* [PSD EXISTING GS], *Green Sheet Transfer Between NAOUs Report* [PSD GS TRANSFER (NAOU) REPORT], NAOU Usage Report [PSD NAOU USAGE], *Transfer Drugs between Dispensing Sites* [PSD TRANSFER VAULT DRUGS] options on the *Technician (CS Pharmacy) Menu* [PSD PHARM TECH]. The CS technician may perform all functions of the *Outpatient Rx’s* [PSD OUTPATIENT] option except releasing prescriptions.

**PSD TRAN** This key should be allocated to the Inpatient 	Pharmacy Coordinator(s). This key controls the 	access to the *NAOU to NAOU Transfer Stock	Entries* [PSD TRANSFER NAOU] option. Users	can copy stock entries from one NAOU into another	NAOU or from an AR/WS AOU into an NAOU.

**PSDMGR** This key should be allocated to the Inpatient 	Pharmacy Supervisor and Package Coordinator(s) 	or his/her designee. This lock controls the editing of 	CS files for package set up. This key locks the *Supervisor’s 	Menu* options [PSD MGR].

**PSDRPH** This key authorizes pharmacists to verify and dispense controlled substance prescription(s). The PSDRPH security key should be given to registered pharmacists working on controlled substances to honor Drug Enforcement Administration (DEA) regulations and should not be given to non-pharmacists except in cases where the package coordinator (ADPAC) is not a registered pharmacist.

**PSJ PHARM TECH** This key should be allocated to pharmacy technicians handling narcotic orders.

**PSJ RNURSE** This key should be allocated to nurses who request 	narcotic orders, receive, and administer 	controlled substances on the wards.

**PSJ RPHARM** This key should be given to pharmacists 	dispensing and receiving narcotic orders.

**Satellite Vault** An NAOU set up as a secondary dispensing site.

**Stock Drug** A drug (from the drug file) stored in an NAOU.

**Stock Level** The quantity of a drug stocked in a specific NAOU.

**TRAKKER** A barcode collection system utilized by scanning 		barcode labels or by pressing the key pad on the 		barcode reader device.

**V** ***IST*** **A** Veterans Health Information Systems and 	Technology Architecture

**Ward (for Drug)** The name of the ward or wards that will use this 	particular drug. It is important to accurately 	answer this prompt because this is the link 	between the Unit Dose package and the Controlled 	Substances package. The Unit Dose package looks 	at this field to know if the drug is a Controlled 	Substances stocked drug.

## Index

1358 obligation number, 4

Barcode TRAKKER for Inventory, 28

COMPLETE - PENDING PROBLEM RESOLUTION., 14

COMPLETE - REVIEWED, 14

Complete Green Sheet, 14

Control Point Transaction number, 4

Control Point Transaction Review, 5

CS Order Entry For Ward, 25

Destroy a Controlled Substances Drug, 23

Destructions Menu, 23

Dispensing Menu, 6

Dispensing/Receiving Report (VA FORM 10-2321), 8

Drug Receipt History, 5

Electronic Signature, 2

Electronic Signature Codes, 2

Fill/Dispense CS Orders from Worksheet, 6

G.Controlled Substances Team@ISC-BIRM, iii

GREEN SHEET NOT SIGNED BY NURSE, 14

Green Sheet Reprint (VA FORM 10-2638), 9

Green Sheet—Print (VA FORM 10-2638), 8

Hold a CS Drug (No Inventory Update), 23

IFCAP purchase orders, 4

Infusion Order Entry, 21

Infusion Order Processing Menu, 21

Intranet, 3

Invoice Review (Prime Vendor), 5

Label for Dispensing (Barcode), 11

Label Reprint for Dispensing Drug, 10

Load Software and Inventory into TRAKKER, 28

Manufacturer, Lot #, and Exp. Date—Enter/Edit, 34

Master Vault, 4

MATH ERROR, 14

Narcotic Dispensing Equipment Orders, 12

NO DISCREPANCY, 14

Non—VA Drug Placed on Hold for Destruction, 23

Order Entry Banner, 41

ORDER ENTRY BANNER, 25

**Order Entry Steps** , 21

OTHER - REFERRED TO PHARMACY SUPERVISOR, 14

Outpatient RX’s, 16

Pharmacy Dispense without (VA FORM 10-2638), 11

Prime Vendor receipts, 4

Print CS Dispensing Worksheet, 6

*PSD ERROR* , 32, 43

**PSD NURSE** , 43

**PSD PARAM** , 43

**PSD TECH** , 43

**PSD TECH ADV** , 43

**PSD TRAN** , 44

PSDMGR, 19, 44

**PSDRPH** , 44

**PSJ PHARM TECH** , 44

**PSJ RNURSE** , 44

**PSJ RPHARM** , 44

purchase order number, 4

Purchase Order Review, 5

Receipt of Controlled Substances from Pharmacy, 27

Receipts Into Pharmacy, 4

Receiving, 4

REPRINT, 10

Reprint Disp/Receiving Report (VA FORM 10-2321), 9

Reprint Reports Menu, 9

Reprint Transfer Between NAOUs (VA FORM 10-2321), 10

RETURNED TO STOCK, 14

Send Vault TRAKKER Inventory Data to DHCP, 31

Transfer Drugs between Dispensing Sites, 19

Transfer Green Sheet and Drug to another NAOU, 22

TRANSFERRED BETWEEN NAOUs, 10

TURN IN FOR DESTRUCTION, 14

TURNED IN FOR DESTRUCTION, 14

VA, 21

VA FORM 10-2321, 9, 39

VA FORM 10-2638, 11, 21, 39

VA FORM 10-2638., 25

VA FORM 2320, 38

VA FORM 2321, 10

VA-FORM 10-2321, 14

**V** *IST* **A** , iii

## ## B

## C

## D

## E

## F

## G

## H

## I

## L

## M

## N

## O

## P

## R

## S

## T

## V

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Controlled Substances Pharmacist's User Manual (Updated PSD*3.0*92)

## References

Documentation for the Controlled Substances package may be found on the VA Software Document Library (VDL), located on the Internet at:

[https://www.va.gov/vdl/application.asp?appid=86](https://www.va.gov/vdl/application.asp?appid=86)
