---
title: IB*2*384 HIPAA NCPDP IB Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: HIPAA NCPDP IB
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*384
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - date
  - patient
  - billing
  - drug
  - claims
  - bill
  - tracking
  - ecme
  - edit
  - ibpatient
page_count: 0
word_count: 3020
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_384_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_384_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

> ![](ib-2-384-hipaa-ncpdp-ib-release-notes/001.png)

Healthcare Insurance Portability and Accountability Act (HIPAA)National Council for Prescription Drug Programs (NCPDP)

####### INTEGRATED BILLING (IB) 

####### RELEASE NOTES

IB\*2\*384

July 2009

V*IST*A Health  
Systems Design & Development

Table of Contents

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Integrated Billing Patch IB\2\384](#integrated-billing-patch-ib2384)
  - [Functional Changes](#functional-changes)
    - [New Options](#new-options)
    - [Modified Options](#modified-options)
    - [Modified Actions](#modified-actions)
    - [Technical Modifications](#technical-modifications)
The Healthcare Insurance Portability and Accountability Act (HIPAA) National Council for Prescription Drug Programs (NCPDP) Connection for Electronic Data Interchange (EDI) Pharmacy project, commonly referred to as HIPAA NCPDP or e-Pharmacy, is a collection of upgrades to Pharmacy Data Management V. 1.0, Integrated Billing (IB) V. 2.0, and Accounts Receivable (AR) V. 4.5 Veterans Health Information Systems and Technology Architecture (V*IST*A) software packages and a release for the new Electronic Claims Management Engine (ECME) V. 1.0 V*IST*A package. The goal of the HIPAA NCPDP project is to allow the V*IST*A software applications to electronically transmit outpatient pharmacy prescription claims to payers. It will also receive claim responses (which include drug utilization responses and warnings) on a real-time basis and in accordance with HIPAA NCPDP mandated format standards, specifically NCPDP Telecommunication Standard V. 5.1.
This patch has enhancements which extend the capabilities of the V*IST*A ePharmacy billing system. Below is a list of all the applications involved in this project along with their patch number:
Integrated Billing (IB) V. 2.0 IB\*2\*384
Electronic Claims Management Engine (ECME) V. 1.0 BPS\*1\*7
Outpatient Pharmacy (OP) V. 7.0 PSO\*7\*289
Pharmacy Data Management (PDM) V. 1.0 PSS\*1\*131
Consolidated Mail Outpatient Pharmacy (CMOP) PSX\*2\*65

# Integrated Billing Patch IB\*2\*384

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Functional Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Patient Release of Information (ROI) \[IBCNR RELEASE OF INFORMATION\]

For third party reimbursement, a Patient Release of Information (ROI) is required before submission of claims that indicate a sensitive diagnosis. The Patient Release of Information (ROI) option supports the tracking and editing of active ROIs on file by checking for drugs that contains the new Release of Information Identifier "U" in the DEA SPECIAL HDLG field. If a claim contains a drug with the ROI Identifier, and an active ROI is not on file, then the claim will not be electronically submitted and will be marked as unbillable in Claims Tracking.. A new CLAIMS TRACKING ROI file(#356.25) documents whether an ROI is on file for a patient. The option may be invoked from the e-Pharmacy Menu with the synonym ROI.

The following file management actions are supported with the new option with examples below:

- Adding new ROIs
- Viewing existing ROIs
- Editing ROIs

Example – Add New ROI

Select Patient Insurance Menu Option: EPH e-Pharmacy Menu

EHNF Edit HIPAA NCPDP FLAG

ENP Edit NCPDP PROCESSOR APPLICATION Sub-file

EPAY Edit PAYER APPLICATION Sub-file

EPBM Edit PBM APPLICATION Sub-file

EPLA Edit PLAN APPLICATION Sub-file

EVNT ECME Billing Events Report

MGP Match Group Plan to a Pharmacy Plan

MMGP Match Multiple Group Plans to a Pharmacy Plan

MTPS Match Test Payer Sheet to a Pharmacy Plan

NON Drugs non covered report

PSI Group Plan Status Inquiry

PSR Group Plan Status Report

RGPW Group Plan Worksheet Report

ROI Patient Release of Information (ROI)

RPP Pharmacy Plan Report

Select e-Pharmacy Menu Option: ROI Patient Release of Information (ROI)

Select PATIENT NAME: IBPATIENT,TWO IBPATIENT,TWO 1-1-44 666011111

YES SC VETERAN

Enrollment Priority: GROUP 3 Category: IN PROCESS End Date: 10/09/2007

Patient ROI Management Jul 28, 2008@11:32:45 Page: 1 of 1

ROI Management for Patient: IBPATIENT,TWO I1111

S Drug Insurance Co. Eff Date Exp Date

-- No ROI's on file for patient --

Enter ?? for more actions

AR Add ROI

VR ROI View/Edit

Select Action: Quit// A Add ROI

CLAIMS TRACKING ROI DRUG: FENOPROFEN 300MG CAP MS102

CLAIMS TRACKING ROI INSURANCE COMPANY: IBINSUR1 123 ANYWHERE ST

ANYTOWN VIRGINIA Y

CLAIMS TRACKING ROI EFFECTIVE DATE: 6/1/2008 (JUN 01, 2008)

CLAIMS TRACKING ROI EXPIRATION DATE: 5/31/2009 (MAY 31, 2009)

CLAIMS TRACKING ROI COMMENT: TESTING

Patient ROI Management Jul 28, 2008@11:41:18 Page: 1 of 1

ROI Management for Patient: IBPATIENT,TWO I1111

S Drug Insurance Co. Eff Date Exp Date

1 FENOPROFEN 300MG CAP IBINSUR1 06/01/08 thru 05/31/09

Enter ?? for more actions

AR Add ROI

VR ROI View/Edit

Select Action: Quit//

Example – Viewing an Active ROI

Select Action: Quit// VR ROI View/Edit

Patient ROI Information Jul 28, 2008@11:56:41 Page: 1 of 1

ROI Management for Patient: IBPATIENT,TWO I1111

IBPATIENT,TWO has the following ROI on file:

Drug: FENOPROFEN 300MG CAP

Insurance Company: IBINSUR1

Effective Date: 06/01/08

Expiration Date: 05/31/09

Status: Active

Comment: TESTING

Date ROI Added: 07/28/08

User Adding Entry: IBUSER,ONE

Date ROI Last Updated: 07/28/08

User Last Updating: IBUSER,ONE Date Last Used: 07/28/08

Enter ?? for more actions

Edit ROI

Select Action: Quit//

Example – Editing an ROI

An example of changing the status of a n ROI from active to inactive.

Select Action: Quit// E Edit ROI

EFFECTIVE DATE: JUN 1,2008//

EXPIRATION DATE: MAY 31,2009//

ACTIVE?: YES// N NO

COMMENT: TESTING//

Patient ROI Information Jul 28, 2008@12:47:09 Page: 1 of 1

ROI Management for Patient: IBPATIENT,TWO I1111

IBPATIENT,TWO has the following ROI on file:

Drug: FENOPROFEN 300MG CAP

Insurance Company: IBINSUR1

Effective Date: 06/01/08

Expiration Date: 05/31/09

Status: Inactive

Comment: TESTING

Date ROI Added: 07/28/08

User Adding Entry: IBUSER,ONE

Date ROI Last Updated: 07/28/08

User Last Updating: IBUSER,ONE

Date Last Used: 07/28/08

Enter ?? for more actions

Edit ROI

Select Action: Quit// QUIT

Patient ROI Management Jul 28, 2008@12:47:14 Page: 1 of 1

ROI Management for Patient: IBPATIENT,TWO I1111

S Drug Insurance Co. Eff Date Exp Date

1 I FENOPROFEN 300MG CAP IBINSUR1 06/01/08 thru 05/31/09

Enter ?? for more actions

AR Add ROI

VR ROI View/Edit

Select Action: Quit//

#### Service Connected Determination Change Report \[IB SC DETERMINATION CHANGE RPT\]

The Service Connected Determination Change Report \[IB SC DETERMINATION CHANGE RPT\] was added to the Patient Billing Reports Menu \[IB OUTPUT PATIENT REPORT MENU\]. This option creates a report with patients that have prescriptions and Service Connected determination changes for a specific time period to assist with copay resets. The report can be generated for Service Connected (SC) to Non-Service Connected (NSC), NSC to SC, or both types of service connection changes. The user can also select a specific timeframe of service connected activity for one patient or all patients. Based on the user’s input to these prompts, the report will determine if there were any prescriptions ordered for the patient during the timeframe selected and will display relevant information to the user to assist with determining if a copay reset is necessary.

Example:

Select Patient Billing Reports Menu Option: SC Service Connected Determination

Change Report

Select one of the following:

S SC to NSC

N NSC to SC

B Both

Select Change Type or (B)oth: B// oth

Select Activity Timeframe Days: (1-999): 30// 999

Select one of the following:

P ONE PATIENT

A ALL

Display One (P)atient or (A)ll: A// LL

DEVICE: HOME// ;80;999 UCX/TELNET

================================================================================

SERVICE CONNECTED STATUS CHANGES for period 9/1/05 - 5/27/08 Page: 1

================================================================================

Patient Effective Service Eligibility SC Enrollment

Date connected code %% priority

RX# Fill# DOS Bill# ECME# Copay/Insurance

--------------------------------------------------------------------------------

IBSCDC,ONE 2222 1/1/08 Y SC LESS THAN 50% 25 GROUP 3

2/7/08 N NSC GROUP 8

100500 0 2/7/08 K8000ECe 406 p-OPINSUR1

100506 0 2/12/08 K8000GNe 412 p-OPINSUR1

100540 0 2/27/08 K8000H9 449 p-OPINSUR1

100546 0 2/27/08 K8000GPe 456 p-OPINSUR1

100549 0 2/27/08 K8000H9 459 p-OPINSUR1

IBSCDC,TWO 2828 12/29/07 Y SC LESS THAN 50% 20 GROUP 3

12/29/07 N NSC GROUP 8

100505A 1 2/26/08 K8000H5 413 p-IBINSUR1

100524 0 2/14/08 K8000GJe 431 p-IBINSUR1

100525 0 2/14/08 K8000GKe 432 p-IBINSUR1

100531 1 2/26/08 K8000H5 438 p-IBINSUR1

100532 0 2/20/08 K8000GLe 439 p-IBINSUR1

100533 0 2/20/08 K8000GIe 440 p-IBINSUR1

100538 0 2/26/08 K8000H5 445 p-IBINSUR1

IBSCDC,THREE 9999 2/27/08 N NSC GROUP 8

3/3/08 Y SC LESS THAN 50% 25 GROUP 3

100553 0 3/3/08 K8000H8e 463 p-DEVELOPMENT INS

100666 0 3/26/08 K8000RB 585 Copay

### Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Enter/Edit Billing Information \[IB EDIT BILLING INFO\]

The software supporting this option was modified to support ROI tracking.

#### ROI Identifier on Screen 7

When Autobiller creates a claim or if a claim is manually created and the

DEA Special Handling field of the Drug has the "U" indicator, the Sensitive

Flag will automatically be changed to YES on Screen 7 of the Billing

Screen.

#### Prevent Bill Authorization

If a bill has the Sensitive Diagnosis question answered YES and the ROI form completed is not YES, an error will display in the National Edits error listing when the user is attempting to complete the bill. Authorization of the bill will not be allowed in this case until those fields are updated.

Example

IBPATIENT,ONE 666-26-9877 BILL#: K8000NC - Outpat/UB04 SCREEN \<7\>

================================================================================

BILLING - GENERAL INFORMATION

\[1\] Bill Type : 131 Loc. of Care: HOSPITAL - INPT OR OPT (INCLU

Covered Days: UNSPECIFIED Bill Classif: OUTPATIENT

Non-Cov Days: UNSPECIFIED Timeframe: ADMIT THRU DISCHARGE

Charge Type : INSTITUTIONAL Disch Stat:

Form Type : UB-04 Division: ANYVAMC

Div. Taxonomy: UNSPECIFIED

\[2\] Sensitive? : YES Assignment: YES

R.O.I. Form : NOT COMPLETED

\[3\] Bill From : MAR 30, 2008 Bill To: MAR 30, 2008

\[4\] OP Visits : UNSPECIFIED

\[5\] Rev. Code :

OFFSET : \$0.00 \[NO OFFSET RECORDED\]

BILL TOTAL : \$0.00

\[6\] Rate Sched : (re-calculate charges)

\[7\] Prior Claims: UNSPECIFIED

Run the National IB Edits:

... Executing national IB edits

ERROR/WARNING OUTPUT DEVICE: HOME// UCX/TELNET Right Margin: 80//

\*\*Warnings\*\*:

Taxonomy for the Division has no value

Taxonomy for the Billing Provider has no value

No source of admission: '2 - CLINIC REFERRAL' will be used

No discharge status: '01 - DISCHARGED TO HOME OR SELF CARE' will be used

\*\*Errors\*\*:

Total Charges for Bill missing or equals zero.

Attending/rendering provider name is missing

No ICD-9 diagnosis.

ROI form required for sensitive record

Do you wish to edit the inconsistencies now? NO//

If the drugs that contain the new Release of Information Identifier "U" in the DEA SPECIAL HDLG field are entered as part of a bill, and no ROI has been entered for them, the bill will not be authorized. The drugs will be listed in the National IB Edits as warnings and the ROI requirement will be listed as an error.

Example

PRESCRIPTIONS IN DATE RANGE

===============================================================================

1\) 100981 FENOPROFEN 300MG CAP 04/13/08 ORG

2\) 100982 DIPYRIDAMOLE 25MG TAB 04/13/08 ORG

SELECT NEW RX FILLS TO ADD THE BILL: (1-2): 1,2

YOU HAVE SELECTED 1,2, TO BE ADDED TO THE BILL IS THIS CORRECT? YES// y YES..

----------------- Existing Prescriptions on Bill -----------------

3) 100981 FENOPROFEN 300MG CAP 04/13/08 ORG

IBEMPLOYEE,ONE (Rx Procedure Missing Rev Code Missing)4) 100982 DIPYRIDAMOLE 25MG TAB 04/13/08 ORG

IBEMPLOYEE,ONE (Rx Procedure Missing Rev Code Missing)

Select RX FILL:

Removing old Revenue Codes and Rate Schedules...

IBPATIENT,ONE 666-26-9877 BILL#: K8000NY - Outpat/UB04 SCREEN \<5\>

================================================================================

EVENT - OUTPATIENT INFORMATION

\<1\> Event Date : APR 13, 2008

\[2\] Prin. Diag.: UNSPECIFIED \[NOT REQUIRED\]

\[3\] OP Visits : UNSPECIFIED

\[4\] Cod. Method: UNSPECIFIED \[NOT REQUIRED\]

\[5\] Rx. Refills: FENOPROFEN 300MG CAP Apr 13, 2008

DIPYRIDAMOLE 25MG TAB Apr 13, 2008

\[6\] Pros. Items: UNSPECIFIED \[NOT REQUIRED\]

\[7\] Occ. Code : UNSPECIFIED \[NOT REQUIRED\]

\[8\] Cond. Code : UNSPECIFIED \[NOT REQUIRED\]

\[9\] Value Code : UNSPECIFIED \[NOT REQUIRED\]

... Executing national IB edits

ERROR/WARNING OUTPUT DEVICE: HOME// UCX/TELNET Right Margin: 80//

\*\*Warnings\*\*:

Taxonomy for the Division has no value

Taxonomy for the Billing Provider has no value

No source of admission: '2 - CLINIC REFERRAL' will be used

No discharge status: '01 - DISCHARGED TO HOME OR SELF CARE' will be used

ROI not on file for prescription 100981ROI not on file for prescription 100982

\*\*Errors\*\*:

Total Charges for Bill missing or equals zero.

Attending/rendering provider name is missing

No ICD-9 diagnosis.

ROI form required for sensitive record

Do you wish to edit the inconsistencies now? NO//

#### Prompt for ROI Tracking Data When Entering or Editing a Bill

When entering billing information using the menu option Enter/Edit Billing

Information, if the drug has a DEA Special Handling field of "U" and no ROI

tracking data is on file for the drug, the user will be prompted to enter

the data from screen seven of the billing edit screens when the user is

indicating that ROI forms have been completed. The data is entered into the new CLAIMS TRACKING ROI file to be used for subsequent billing determinations.

Example

\<RET\> to CONTINUE, 1-7 to EDIT, '^N' for screen N, or '^' to QUIT: 2

IS THIS A SENSITIVE RECORD?: NO// y (YES)

R.O.I. FORM(S) COMPLETED?: Y (YES)

This drug requires a Release of Information(ROI)for:PATIENT: IBPATIENT,ONEDRUG: FENOPROFEN 300MG CAPINSURANCE COMPANY: IBINSUR1FILL DATE: 04/13/08Do you want to add a new ROI for this patient? ? NO// YESEnter the ROI effective date for the ROI: 4/13 (APR 13, 2008)Enter the ROI expiration date for the ROI: 4/13 (APR 13, 2008)CLAIMS TRACKING ROI Comment:This drug requires a Release of Information(ROI)for:PATIENT: IBPATIENT,ONEDRUG: DIPYRIDAMOLE 25MG TABINSURANCE COMPANY: IBINSUR1FILL DATE: 04/13/08Do you want to add a new ROI for this patient? ? NO// YESEnter the ROI effective date for the ROI: 4/13 (APR 13, 2008)Enter the ROI expiration date for the ROI: 4/13 (APR 13, 2008)CLAIMS TRACKING ROI Comment:

ASSIGNMENT OF BENEFITS: YES//

IBPATIENT,ONE 666-26-9877 BILL#: K8000NY - Outpat/UB04 SCREEN \<7\>

================================================================================

BILLING - GENERAL INFORMATION

\[1\] Bill Type : 131 Loc. of Care: HOSPITAL - INPT OR OPT (INCLU

Covered Days: UNSPECIFIED Bill Classif: OUTPATIENT

Non-Cov Days: UNSPECIFIED Timeframe: ADMIT THRU DISCHARGE

Charge Type : INSTITUTIONAL Disch Stat:

Form Type : UB-04 Division: ANYVAMC

Div. Taxonomy: UNSPECIFIED

\[2\] Sensitive? : YES Assignment: YES

R.O.I. Form : COMPLETED

\[3\] Bill From : APR 13, 2008 Bill To: APR 13, 2008

\[4\] OP Visits : UNSPECIFIED

\[5\] Rev. Code :

OFFSET : \$0.00 \[NO OFFSET RECORDED\]

BILL TOTAL : \$0.00

\[6\] Rate Sched : (re-calculate charges)

\[7\] Prior Claims: UNSPECIFIED

#### Generate ECME Rx Bills \[IB GENERATE ECME RX BILLS\]

The Generate ECME Rx Bills option within the Billing Clerk's Menu adds manual back-billing capability for electronic pharmacy bills. It allows the IB user to submit/re-submit the Rx claim electronically to the ECME for claims submission. When using the option and the drug has a DEA Special Handling field of "U" and no ROI Tracking data is on file for the drug, the user will be prompted to enter the data related to the ROI.

Example

Select Billing Clerk's Menu Option: ERX Generate ECME Rx Bills

Select one of the following:

P SINGLE (P)ATIENT

R SINGLE (R)X

SINGLE (P)ATIENT, SINGLE (R)X: P// R SINGLE (R)X

Select PRESCRIPTION RX \#: 100985 FENOPROFEN 300MG CAP

1 100985 0 APR 16, 2008 FENOPROFEN 300MG CAP

Submit the selected RX(s) to ECME for electronic billing? NO// YES

Submitting Rx# 100985 (original fill) ...

This drug requires a Release of Information(ROI)for:

PATIENT: IBPATIENT,ONEDRUG: FENOPROFEN 300MG CAPINSURANCE COMPANY: IBINSUR1FILL DATE: 04/16/08

Do you want to add a new ROI for this patient? ? NO// YES

Enter the ROI effective date for the ROI: 4/16 (APR 11, 2008)

Enter the ROI expiration date for the ROI: 4/16 (APR 10, 2009)

CLAIMS TRACKING ROI Comment:

Prescription 100985 successfully submitted to ECME for claim generation.

Request: 108779458

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Building the claim

IN PROGRESS-Preparing for transmit

IN PROGRESS-Transmitting

IN PROGRESS-Parsing response

E PAYABLE

Sent through ECME

The selected Rx(s) have been submitted to ECME

for electronic billing

Press RETURN to continue:

### Modified Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Submit Claim to ECME

When using the Claims Tracking action Submit Claim to ECME and the Drug has a DEA Special Handling field of “U” and no ROI Tracking data is on file for the drug, the user is prompted to enter the data related to the ROI.

Example

BI Billing Info Edit TA Treatment Auth. EX Exit

RI Review Info SE Submit Claim to ECME

Select Action:Next Screen// SE Submit Claim to ECME

This option sends electronic Pharmacy Claims to the Payer

This drug requires a Release of Information(ROI) for:

PATIENT: IBPATIENT,ONE

DRUG: FENOPROFEN 300MG CAP

INSURANCE COMPANY: IBINSUR1

FILL DATE: 06/02/08

Do you want to add a new ROI for this patient? ? NO// YES

Enter the ROI effective date for the ROI: 6/1 (JUN 01, 2008)

Enter the ROI expiration date for the ROI: 7/1 (JUL 01, 2008)

CLAIMS TRACKING ROI COMMENT: TESTING

Submit the Rx# 101279 to ECME for electronic billing? NO// YES

Submitting Rx# 101279 ...

### Technical Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Submitted to IB for Billing Determination

When submitted to IB for billing determination, if it is determined that an active ROI is not in the new CLAIMS TRACKING ROI file for a claim that has a DEA Special Handling field of "U", then the claim will be returned non-billable with a Non-Billable Reason of NO ACTIVE ROI ON FILE.

Example

Select Action: Next Screen// NO New Order

Eligibility: SC LESS THAN 50% SC%: 25

RX PATIENT STATUS: OPT NSC//

DRUG: FENOPRO

Lookup: GENERIC NAME

FENOPROFEN 300MG CAP MS102

...OK? Yes// (Yes)

-------------------------------------------------------------------------------

Duplicate Drug FENOPROFEN 300MG CAP in Prescription: 100885

Status: Active Issued: 04/03/08

SIG: ONE MOUTH EVERY DAY

QTY: 90 \# of refills: 3

Provider: IBPROVIDER,ONE Refills remaining: 3

Last filled on: 04/04/08

Days Supply: 90

-------------------------------------------------------------------------------

Discontinue RX \# 100885? YES

Duplicate Drug will be discontinued after the acceptance of the new order.

Now doing drug interaction and allergy checks. Please wait...

VERB:

Available Dosage(s)

1\. 300MG

2\. 600MG

Select from list of Available Dosages, Enter Free Text Dose

or Enter a Question Mark (?) to view list: 1 300MG

You entered 300MG is this correct? Yes// YES

DISPENSE UNITS PER DOSE: 1// 1

Dosage Ordered: 300MG

NOUN:

ROUTE: PO// ORAL PO MOUTH

Schedule: QD (EVERY DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION:

PATIENT INSTRUCTIONS:

(ONE MOUTH EVERY DAY)

DAYS SUPPLY: (1-90): 90//

QTY ( ) : 90// 90 Below Reorder Level.

COPIES: 1// 1

\# OF REFILLS: (0-3): 3//

PROVIDER: IBPROVIDER,ONE

CLINIC: MEDICAL CLINIC

MAIL/WINDOW: WINDOW// WINDOW

METHOD OF PICK-UP:

REMARKS:

ISSUE DATE: TODAY// 4/4 (APR 04, 2008)

FILL DATE: (4/4/2008 - 4/5/2009): TODAY// 4/5 (APR 05, 2008)

Nature of Order: WRITTEN// W

WAS THE PATIENT COUNSELED: NO// NO

Do you want to enter a Progress Note? No// NO

Rx \# 100886 04/05/08

IBPATIENT,ONE \#90

ONE MOUTH EVERY DAY

FENOPROFEN 300MG CAP

IBPROVIDER,ONE IBPROVIDER,ONE

\# of Refills: 3

SC Percent: 25%

Disabilities:

OSTEOMYELITIS 29% - SERVICE CONNECTED

Was treatment for Service Connected condition? NO

Is this correct? YES//

-Rx 100885 has been discontinued...

NOT BILLABLE, NO ROI - NO ACTIVE ROI ON FILE

Another New Order for IBPATIENT,ONE? YES//

#### ### The Post-install Procedure

#### Claims Tracking Non-Billable Reasons List

The ECME selectable list of non-billable reasons, contained in the Claims Tracking Non-Billable Reasons List file(#356.8), has been expanded to include the following set of Service Connected/Environmental indicators.

1.  Agent Orange
2.  Ionizing Radiation
3.  SC Treatment
4.  Southwest Asia
5.  Military Sexual Trauma
6.  Head/Neck Cancer
7.  Combat Veteran
8.  Project 112/SHAD

These Non-Billable Reasons will be added to the NAME field (#.01) of the CLAIMS TRACKING NON-BILLABLE REASONS file (#356.8). If the above non-billable reasons already exist at the site, they will not be added. The ECME FLAG field (#.02) will be populated with "1" (external value ='YES') in the CLAIMS TRACKING NON-BILLABLE REASONS file (#356.8). This will enable their selection by the user when closing a claim in the ECME package.