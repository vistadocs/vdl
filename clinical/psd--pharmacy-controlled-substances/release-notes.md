---
consolidated_title: "controlled substances release notes"
app_code: PSD
doc_type: RN
master_source: "Controlled Substances Version 3 Release Notes"
master_pub_date: March 1997
consolidated_from: 2 versions
prior_versions:
  - "PSD*3*89 Controlled Substances Version 3 Release Notes"
---

**Controlled Substances**

**Release Notes**


March 1997


Software Service

Clinical Ancillary Product Line

**Introduction**

The Controlled Substances (CS) software package is one segment of the Veterans Health Information Systems and Technology Architecture ( **V** *IST* **A** ) being installed at VA medical centers. The Controlled Substances software will monitor and track the receipt, inventory, and dispensing of controlled substances. Automation of the narcotic inventory process will permit pharmacists and inspectors to perform vault inventories utilizing portable barcode readers.

Monthly (or more frequent) inspections can be conducted by management, with discrepancies in stock levels automatically identified.

Controlled Substances (CS) Version 3.0 will provide many new enhancements for both pharmacy and nursing users.

A list of the new additions and modifications to existing options that will be discussed in this document follows:

Batch Order Entry process

Electronic Signature

Dispensing to Patients Recorded with a Radio Frequency (RF) Device

HL7 Interface to Narcotic Dispensing Equipment

Electronic Error &amp; Enhancement Requests (E3Rs)

Destructions

Other Enhancements

Intranet

We are now on the intranet, come visit us. REDACTEDThis address will take you to the Clinical Products page where you will find a listing of all the clinical software manuals and other software manuals. Click on the Controlled Substances (CS) link and it will take you to the CS Homepage. You can also get there by going straight to

REDACTED (don’t forget to bookmark it!)

In addition, both of these homepages have a Software Service Homepage link. Simply click on this link and then follow the links to the manuals you would like to see.

**New Features**

## Batch Order Entry

In Version 2.0, the orders are sent simultaneously to pharmacy when entered. In Version 3.0, the batch order entry process will provide nursing personnel with the ability to enter several Controlled Substances order requests, delete one or more of the requests, or append additional requests to the original list before sending the information to pharmacy. These order requests may then be batched and sent to pharmacy for processing. The ability for nursing personnel to cancel requests before pharmacy begins order processing remains the same in Version 3.0.

## Electronic Signature

In Controlled Substances, the Electronic Signature functionality will be used for identification for pharmacy personnel, nursing personnel, and narcotic inspectors.

Identification will be used to reconfirm the identity of the user at the keyboard before proceeding with the next step in a critical process.

## Dispensing to Patients Recorded with a Radio Frequency (RF) Device

Selected sites will be receiving RF devices to be used by Nursing Service to record dispensing of Controlled Substances to patients.  This functionality will replace the need to record dispensing on green sheets (VA FORM 2321).  Bar codes will be used to identify patients and drugs.

## HL7 Interface to Narcotic Dispensing Equipment System (NDES)

Health Level 7 (HL7) is the standard protocol used for electronic data exchange in the healthcare environment. The Controlled Substances Version 3.0 HL7 Interface Specifications document will identify the data record exchanges between the Veterans Health Information Systems and Technology Architecture (VISTA) and the NDES.

The VISTA system will send ADT event type HL7 messages to the CS Dispensing Equipment whenever an admission, discharge, or transfer event occurs.

## E3Rs

The following Electronic Error &amp; Enhancement Requests (E3Rs) have been approved for Controlled Substances Version 3.0.

**One-Time Order Request (#3189)**

The RN will be able to create a “One Time Request” (similar to the On-Demand in Automatic Replenishment) for an item not currently stocked on a NAOU. After issuing the drug to the NAOU, it will be inactivated. The quantity will be restricted to 1 package of the item as set up in the “Package Size” for the vault. An E-Mail message will be sent to the Pharmacy Supervisor who may elect to establish it as a permanent stock item for that NAOU.

**Dispensing Action Prompt (#3227)**

In Version 2.0, when the employee filled a controlled substance, the whole order was viewed and then shown one at a time for possible editing. The action prompt appeared only after each line had been displayed. It was recommend and accepted for Version 3.0 to place the action prompt immediately after view is shown, thus simplifying the process.

**Inventory Balance on the Disp./Receiving Report (#3311)**

In Version 2.0, the vault balance of a CS drug was shown on the screen while filling a CS. This is the only place the information was displayed during the process of filling controlled substances. In Version 3.0 the report format has been modified for the **vault copy only** on the options *Dispensing/Receiving Report (VA-FORM 10-2321) Reprint/Disp/Receiving Report (VA-FORM 2321)* and on to: print a drug balance under the drug name and print an asterisk next to the quantity and balance only if the original quantity ordered has been edited. A legend has also been added to the bottom of the report.

**Comments for Drug Destruction (#3771)**

The *Hold a CS Drug* option does not allow for enough information when logging an outpatient’s returned CS for destruction. Currently all that is asked is Drug Name and Amount. Suggest entering a comment where this information would be available if ever asked to track a particular return from a patient. A COMMENTS field of 60 characters will be added to provide a means of documenting the necessary drug products.

**Emergency Narcotic Orders (#4309, #4520, and #4586)**

1)	On the Nurses’ Menu, under the CS Order Entr *y* option, the nurse will be

able to enter scheduled or unscheduled orders.

2)	A site parameter will be added to establish a device for each dispensing 	vault which can receive notice of these unscheduled orders. The 	message will be configured so that it may print on an IV label or on a 	report printer. This message will be a means of notifying the vault 	pharmacist that there is a Priority Controlled Substances order to be 	processed.

The printer designated to receive these messages SHOULD NOT be the 	printer which prints Green Sheets or controlled substance labels.

3)	A report will be created and placed under the Pharmacy Supervisor’s 	Menu which will allow historical data for the NAOUs to be pulled 	showing the use of the Unscheduled Order function.

**Daily Activity Log Enhancements (#4483)**

The Daily Activity Log will be modified to allow the pharmacist printing the report to select:

Print All Drugs

Print selected drugs

Print for ONLY those drugs with any activity during the time frame 			selected for the report.

**Nursing Order Entry Banner (#4686)**

Provide a free text field as a site parameter to appear upon Nursing CS Order Entry. A 200 character free text field will be created to meet this need. This field will be configurable under the option *Vault Enter/Edit* . When the user accesses the following 3 options, the free text field will be displayed:

1) Nursing Order Entry

2) Pharmacy Order Entry from Nursing

3) Infusion Order Entry

**Cancel CS Drug Held for Destruction (#4990)**

Requesting the ability to cancel a destructions holding entry done in error. This could be done from the Destroy A Controlled Substanc *e* option. At the point of question: “Are you destroying this Controlled Substance? YES//” allow a NO answer here also leading to the following areas: “Was this a destructions holding entry error?” If NO then back to option. If YES---&gt; “Do you want to cancel destruction holding #xxx?” YES ---&gt; allow comments here which will update the record. Should also show this cancellation on the Destroyed CS Drugs Report under an additional column called CANCELLED BY instead of the normal “DESTROYED BY” prompt. Allow comments to show Destroyed CS Drugs Report for each cancellation. The Destroyed CS Drugs Report will show the holding number as cancelled. Comments regarding the cancellation of the holding entry will be required and will print on the Destroyed CS Drugs Report.

**Inspector’s Log by Rec’d Date (Region 2) (#5116)**

In Version 2.0, there is a column on the Inspector’s Log for Region 2 to indicate the “Amount on Hand” for each Rx#. This is not feasible for Region 2 sites which use perpetual inventory. The inspectors in Region 2 look only for the receiving date to be on the CSAR. They check bottom line balances after they have verified that all Rx numbers have been received. Eliminate the Amount on Hand column and replace it with a Date Returned column which should clarify the form for the inspectors. The Amount on Hand column will be replaced with a Date Returned column.

**Balance Adjustment Report (#5187)**

Request that the Balance Adjustment Report be expanded which will improve the ability to track trends. This new report would give you a picture of the number and type of balance adjustments which occur.

**Example:** of generating the data by a date range:

DATE	DRUG	QTY	COMMENT	RPH

3/22/94@0817	Phenobarbital 30mg UD	6	RTS RX 19444 NOT DISP	LTL

3/22/94@1017	Lorazepam 1mg tab	3	Manuf. lot 1111 short	LTL

Consider 132 column reporting so the explanation could be longer. This new report will be included in the Version 3.0.

## Destructions

The following Destruction Menu changes have been approved for Controlled Substances Version 3.0.

**Add CS Non-Inv Drug to Holding File**

This routine is used to place a drug on hold for later destruction.

A comments field was added to enter a reason for the drug being placed on hold.

A prompt for entering Patient Returning Drug has been added.

The routine changed to allow for continuous prompting of drug until all

drugs have been entered for a site.

**PSD DESTRUCTION HOLDING File Report**

The report format has been revised. The sequence of the report is now by holding number and users may select a vault name. If ^ALL is selected the site name will print in the title of the report and the vault name will print under the holding number.

The # of containers, GS#,Date, Holding#, cancelled, and Comments will print on report. Also a ( C ) will print next to the holding# if user decides to cancel the holding number.

**DESTROY a CS DRUG**

New prompts were added .

Unit and # of containers prompts were removed.

At the “Date Destroyed/Cancelled” prompt the user can enter the current date or any date prior to current date. User’s will be prompted to destroy or cancel the holding number.

**DESTROYED Drug Report**

A prompt for vault has been added.

The report format has been completely revised with new prompts.

A prompt for Cost of above Qty: has been added. The cost is calculated by price per dispense unit *Qty. A Summary total will print at the end of the report. (Any drug(s) returned by a patient are not included in the calculation).

A prompt for Comments has been added. Why a drug was placed on hold, balance adjustments made, or cancel a holding number.

## Other Enhancements

**Destruction Number Report**

To track each destruction number, a report that can be sorted by a range of transaction numbers for both the drugs on hold for destruction and the CS drugs already destroyed. This report should list all destruction transaction numbers sequentially, regardless of vault. This should meet the needs to track each transaction number.

**Green Sheet History**

Add the *Green Sheet History* option as a new submenu option on the *Inspector’s Menu* . This was requested by the Version 2.0 test sites.

**DEA Form 41**

Allow printing this form by Destruction # range. This was a request from the Version 2.0 test sites.

**Inspector’s Remove from Hold**

Provide the narcotic inspector the ability to enter a reason when returning a Green Sheet back to the ward. When removing a Green Sheet from the ward, comments are allowed. The return of the Green Sheet should allow the inspector to record findings in the software. This was a request from the Version 2.0 test sites.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSD*3*89 Controlled Substances Version 3 Release Notes

## Introduction

The Controlled Substances (CS) software package is one segment of the Veterans Health Information Systems and Technology Architecture (VistA) installed at VA medical centers. The Controlled Substances software monitors and tracks the receipt, inventory, and dispensing of controlled substances. The automated narcotic inventory process permits pharmacists and inspectors to perform vault inventories utilizing portable barcode readers.

This patch is a companion to PSO*7*617, the patch for Inbound Electronic Prescribing (eRx) Controlled Substance (CS) v5.0, which updates the current Inbound eRx 4.0 functionality to allow the VA to receive and dispense electronic prescriptions for controlled substance medications.

In support, the following CS reports were modified to include filters and an eRx ID # so that pharmacists may easily review  CPRS (Internal), eRx (External-Inbound), Electronically signed (CPRS+eRx) and Written (Backdoor Pharmacy) orders for processed and pending orders. The reports were modified accordingly to meet the needs of each filter.

1. Controlled Substance Prescriptions Report [PSD CS PRESCRIPTIONS REPORT]

2. OP CS Orders Report [PSD DIGITALLY SIGNED ORDERS]
3. OP Released Rx Report [PSD DIG. SIGNED RELEASED RX]

## Modified Menu Text

PSD DIGITALLY SIGNED ORDERS

The menu text for the menu option PSD DIGITALLY SIGNED ORDERS was changed from "Digitally Signed CS Orders Report" to "OP CS Orders Report."

PSD DIG. SIGNED RELEASED RX

The menu text for the menu option PSD DIG. SIGNED RELEASED RX was changed from "Digitally Signed OP Released Rx Report" to "OP Released Rx Report."

## Modified Reports

A new filter was added to three CS reports:

1. Controlled Substance Prescriptions Report [PSD CS PRESCRIPTIONS REPORT]
2. OP CS Orders Report [PSD DIGITALLY SIGNED ORDERS]
3. OP Released Rx Report [PSD DIG. SIGNED RELEASED RX]

The filter will allow the user to select prescriptions from CPRS, eRx, and/or written, as shown below:

Select one of the following:

C         CPRS (Internal)

E         eRx (External - Inbound)

B         Electronically Signed (CPRS+eRx)

W         Written (Backdoor Pharmacy)

A         ALL

Prescription Source: A//

In addition, the report headers for these reports were modified to show the filter selected.
