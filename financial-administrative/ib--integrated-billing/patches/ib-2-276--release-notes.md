---
title: IB*2*276/PRCA*4.5*230 HIPAA NCPDP IB/AR Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*276
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - ecme
  - plan
  - pharmacy
  - group
  - claims
  - status
  - billing
  - claim
  - bill
  - report
page_count: 0
word_count: 4873
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_prca_4_5_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_prca_4_5_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

> ![](ib-2-276-prca-4-5-230-hipaa-ncpdp-ib-ar-release-notes/001.png)

HIPAA NCPDP

####### INTEGRATED BILLING (IB)

####### ACCOUNTS RECEIVABLE (AR)

####### RELEASE NOTES

IB\*2\*276

PRCA\*4.5\*230

April 2006

V*IST*A Health  
Systems Design & Development

Table of Contents

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Integrated Billing Patch IB\2\276](#integrated-billing-patch-ib2276)
  - [Functional Changes](#functional-changes)
    - [New Options](#new-options)
    - [Modified Options](#modified-options)
  - [Technical Changes](#technical-changes)
    - [Enhancements to the IB-ECME API](#enhancements-to-the-ib-ecme-api)
    - [New Purge Routine](#new-purge-routine)
    - [The Post-install Procedure](#the-post-install-procedure)
- [Accounts Receivable Patch PRCA\4.5\230](#accounts-receivable-patch-prca45230)
  - [Functional Changes](#functional-changes-1)
    - [ECME Matching Procedure](#ecme-matching-procedure)
    - [Screen Out EEOBs Related to e-Pharmacy Rejects](#screen-out-eeobs-related-to-e-pharmacy-rejects)
The Healthcare Insurance Portability and Accountability Act (HIPAA) National Council for Prescription Drug Programs (NCPDP) Connection for Electronic Data Interchange (EDI) Pharmacy project, commonly referred to as HIPAA NCPDP or e-Pharmacy, is a collection of upgrades to Pharmacy Data Management V. 1.0, Integrated Billing (IB) V. 2.0, and Accounts Receivable (AR) V. 4.5 Veterans Health Information Systems and Technology Architecture (V*IST*A) software packages and a release for the new Electronic Claims Management Engine (ECME) V. 1.0 V*IST*A package. The goal of the HIPAA NCPDP project is to allow the V*IST*A software applications to electronically transmit outpatient pharmacy prescription claims to payers. It will also receive claim responses (which include drug utilization responses and warnings) on a real-time basis and in accordance with HIPAA NCPDP mandated format standards, specifically NCPDP Telecommunication Standard V. 5.1.
This is the second phase of the Electronic Claims Management Engine (ECME) package (in the BPS namespace), also known as the active build.
Following is a list of the software packages and patches involved in the HIPAA NCPDP project.
Integrated Billing (IB) V. 2.0 IB\*2\*276
Accounts Receivable (AR) V. 4.5 PRCA\*4.5\*230
Electronic Claims Management Engine (ECME) V. 1.0 BPS\*1\*1
Outpatient Pharmacy (OP) V. 7.0 PSO\*7\*148
Pharmacy Data Management (PDM) V. 1.0 PSS\*1\*90
Consolidated Mail Outpatient Pharmacy (CMOP) PSX\*2\*48
This build introduces functionality supporting Point of Service Outpatient Pharmacy claims and billing processing, by collecting billing and clinical information within the prescription fill workflow process. This build will create real-time electronic claims and send claim data to adjudicating payers from the new VistA ECME via the VistA HL7 module (using the PSO NCPDP link) to the Vitria server at the FSC in Austin, TX in a HIPAA compliant (NCPDP V. 5.1) format. Vitria will then store and forward these transactions to Emdeon (formerly WebMD) for final submission to the payer on a real-time basis. Payer responses will be received and returned to VistA in the appropriate manner (i.e., claim transactions sent to IB, Drug Utilization responses and warnings sent to the Outpatient Pharmacy V. 7.0 package and rejections made available to the appropriate personnel for review and analysis).
Within VistA, throughout this process, constant bi-directional communication between Outpatient Pharmacy, Integrated Billing, and ECME will process and generate these claim and billing transactions at the appropriate trigger points within the standard VA process workflow.

# Integrated Billing Patch IB\*2\*276

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Functional Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ECME Billing Events Report \[IB ECME Billing Events\]

The ECME Billing Events Report captures and displays dataflow between the ECME and IB packages and can be used to resolve potential issues related to electronic claims processing. The report displays the time and data passed for the following types of ECME-IB interaction events: FINISH (billable status check on Finish Prescription), SUBMIT, RELEASED, BILLING, CLOSED, and REVERSED.

This report is an important tool used to resolve potential issues related to ECME processing. It is accessed from the e-Pharmacy Menu and can be invoked with the synonym, EVNT.

The following data may be included in this report:

- Activity for a single patient, a single prescription, a single ECME \#, or all activity;
- ECME billable claims, non-ECME claims, or both;
- MAIL, WINDOW, CMOP (Consolidated Mail Outpatient Pharmacy), or ALL outpatient pharmacy prescription claims.

Example

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

PSI Group Plan Status Inquiry

PSR Group Plan Status Report

RGPW Group Plan Worksheet Report

RPP Pharmacy Plan Report

Select e-Pharmacy Menu Option: EVNT ECME Billing Events Report

START WITH DATE: TODAY //T-30 (AUG 27, 2005)

GO TO DATE: TODAY// \<RET\> (SEP 26, 2005)

Select one of the following:

P SINGLE PATIENT

R SINGLE RX

E SINGLE ECME \#

A ALL ACTIVITY

SINGLE (P)ATIENT, SINGLE (R)X, SINGLE (E)CME \#, (A)LL ACTIVITY: ALL// \<RET\>

Select one of the following:

E ECME BILLABLE

N NON ECME BILLABLE

B BOTH

(E)CME BILLABLE;(N)ON ECME BILLABLE;(B)OTH: BOTH// \<RET\>

Select one of the following:

M MAIL

W WINDOW

C CMOP

A ALL

(M)AIL, (W)INDOW, (C)CMOP, (A)LL: ALL// \<RET\>

Select one of the following:

S SUMMARY REPORT

D DETAILED REPORT

(S)UMMARY REPORT, (D)ETAILED REPORT: SUMMARY REPORT// \<RET\>

DEVICE: HOME// \<RET\> IP network

97 909936 0 08/30/05 IBpatient,ONE AMOXICILLIN 250MG CAP

FINISH 08/30/05 11:23a Status:ECME Billable

SUBMIT 08/30/05 11:23a Status:OK

REVERSAL 09/08/05 3:10p Status:ECME Claim reversed, no Bill to cancel

CLOSE 09/08/05 3:10p Status:OK

FINISH 09/09/05 8:43a Status:ECME Billable

SUBMIT 09/09/05 8:53a Status:OK

RELEASE 09/09/05 11:01a Status:OK

CLOSE 09/21/05 11:43a Status:OK

--------------------------------------------------------------------------------

98 909937 0 08/30/05 IBpatient,ONE BAND-AID 1IN X 3IN

FINISH 08/30/05 11:24a Status:ECME Billable

SUBMIT 08/30/05 11:24a Status:OK

--------------------------------------------------------------------------------

99 909938 0 08/30/05 IBpatient,ONE DIAZEPAM 5MG TAB

FINISH 08/30/05 11:49a Status:ECME Billable

SUBMIT 08/30/05 11:49a Status:OK

CLOSE 09/08/05 3:09p Status:OK

FINISH 09/09/05 9:45a Status:ECME Billable

SUBMIT 09/09/05 9:46a Status:OK

RELEASE 09/09/05 11:03a Status:OK

BILLING 09/09/05 11:03a Status:Bill# K400KFS created

#### Generate ECME Rx Bills

The Generate ECME Rx Bills option adds manual back-billing capability for electronic pharmacy bills. It allows the IB user to submit/re-submit the Rx claim electronically to the ECME for claims submission. If there is an existing non-cancelled bill, it will not submit/re-submit the claim.

This option is available from the Billing Clerk’s Menu, and can be invoked with the synonym, ERX.

Example

Select Billing Clerk's Menu Option: Generate ECME Rx Bills

Select one of the following:

P SINGLE (P)ATIENT

R SINGLE (R)X

SINGLE (P)ATIENT, SINGLE (R)X: P// \<RET\> SINGLE (P)ATIENT

Select PATIENT NAME: IBpatient,One 5-4-66 000111222 NO NSC VETERAN

START WITH DATE: TODAY//t-90 (SEP 09, 2005)

GO TO DATE: TODAY// \<RET\> (DEC 08, 2005)

Select one of the following:

U UNBILLED

A ALL RX

(U)NBILLED, (A)LL RX: U// a ALL RX

1 910038 0 OCT 13, 2005 DIAZEPAM 5MG TAB K400KGX

2 910039 0 OCT 13, 2005 TAMOXIFEN CITRATE 10MG TAB K400KH2

3 910040 0 OCT 13, 2005 IMIPRAMINE HCL 50MG TAB K400KGZ

4 910041 0 OCT 13, 2005 PROTAMINE SULFATE 5ML INJ K400KH0(canc)

5 910061 0 OCT 13, 2005 BENZOCAINE 20% OTIC DROPS K400KHV

6 910053 0 OCT 14, 2005 REBETRON 1000/PEN PKT (1258-02

7 910056 0 OCT 13, 2005 CLINDAMYCIN 600MG/4ML INJ K400KHY

8 910062 0 OCT 14, 2005 DEXTROSE 5% 1000ML INJ K400KHZ

9 910059 0 OCT 13, 2005 ERGONOVINE 0.2MG 1ML INJ K400KIR

10 383209 0 NOV 29, 2005 ATENOLOL 50MG TAB K400KJ6

11 383210 0 NOV 30, 2005 PYRIMETHAMINE 25MG TAB

Enter Line Item(s) to submit to ECME or (A)LL :11

Submit the Rx# 909954 to ECME for electronic billing? NO// y YES

Submitting Rx# 909954 ...

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Waiting for packet build

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

E PAYABLE

Following are examples of other possible results when attempting to submit claims to ECME.

Attempting to send a claim to ECME that contains a valid Bill#.

This option sends electronic Pharmacy Claims to the Payer

Rx# 383209 was previously billed.

Please manually cancel the bill# K400KJ0 before submitting claim to ECME.

Cannot submit to ECME. Press RETURN to continue:

Attempting to send a claim to ECME where the Rx is NOT Released (i.e., not yet billable)

This option sends electronic Pharmacy Claims to the Payer

The Prescription is not released.

Cannot submit to ECME. Press RETURN to continue:

Attempting to send a claim to ECME that has already been processed in ECME.

This option sends electronic Pharmacy Claims to the Payer

Submit the Rx# 909954 to ECME for electronic billing? NO// y YES

Submitting Rx# 909954 ...

Previously billed through ECME: E REJECTED

Not sent through ECME.

\*\*\* ECME returned status: No billing through ECME

Press RETURN to continue:

Attempting to send a claim to ECME that has already been processed in ECME and was stranded. (Note: “Stranded” refers to the claim’s transmission status. A stranded claim is one that has been in an incomplete (processing) state for more than 30 minutes.)

Submit the selected RX(s) to ECME for electronic billing? NO// y YES

Submitting Rx# 910053 (original fill) ...

Previous ECME claim is stranded, claim needs to be unstranded

Not sent

\*\*\* ECME returned status: No billing through ECME

Press RETURN to continue:

#### Group Plan Status Report \[IBCNR PLAN STATUS REPORT\]

The Group Plan Status Report option may be selected from the IBCNR E-Pharmacy Menu screen, using synonym, PSR.

The NCPDP process requires that users match Group Plans to Pharmacy Plans. This report will assist users in evaluating the GROUP INSURANCE PLAN file (#355.3) entries that have INACTIVE plans or need to be matched to Pharmacy Plans. The system will search through the GROUP INSURANCE PLAN file (#355.3) for group plans that are linked to an insurance company.

The system will do a preliminary search through the INSURANCE COMPANY file (#36) and compile a list of valid Insurances companies.

Only companies that meet the following conditions will be included.

1.  The INACTIVE field (#.05) of the INSURANCE COMPANY file (#36) must be set to NO.
2.  The REIMBURSE? field (#1) of the INSURANCE COMPANY file (#36) must be set to YES.
3.  The insurance must be associated to a group in the GROUP INSURANCE PLAN file (#355.3).
4.  The INACTIVE field (#.11) of the GROUP INSURANCE PLAN file (#355.3) must be set to NO.
5.  The GROUP INSURANCE PLAN file (#355.3) must have PHARMACY coverage set up in the PLAN COVERAGE LIMITATIONS file (#355.32).
6.  The Pharmacy Plan coverage Limitation, COVERAGE STATUS, must be set to COVERED.

Example

ePHARM GROUP PLAN STATUS REPORT

NCPDP process requires that the users match Group Plans to Pharmacy Plans.

This report will assist users in matching Group Insurance Plans to Pharmacy

Plans by searching through GIPF file for Group Plans that

are linked to an Insurance with active Pharmacy Plan coverage.

Current Insurance company list compiled on: 10/18/2005@14:51:06

Do you want to use the existing compiled file? YES// n NO

\*\*\* COMPILING ......

Run Report for (S)PECIFIC insurance companies or a (R)ANGE: RANGE// \<RET\> RANGE

Start with INSURANCE COMPANY: FIRST// \<RET\>

Go to INSURANCE COMPANY: LAST// \<RET\>

Select one of the following:

A All Group Plans

M Matched Group Plans

Select the type of Group Plans you want to see for Insurance selected.: A// m

Matched Group Plans

DEVICE: HOME// \<RET\> IP network

ePHARM GROUP PLAN STATUS REPORT Oct 26, 2005@14:42:48 Page: 1

Report for Matched Group Plans for ADVANCE PCS ADVANCE PCS

Group Name Group \# Plan Type Plan ID Pln Stat

===============================================================================

TESTPLAN1 000939 PRESCRIPTION VA98438 ACTIVE

Plan Active

-------------------------------------------------------------------------------

TESTPLAN2 000786 COMPREHENSIVE VA99390 ACTIVE

Plan Active

-------------------------------------------------------------------------------

TESTPLAN3 0004444 PRESCRIPTION T00010 ACTIVE

Plan Active

-------------------------------------------------------------------------------

TESTPLAN4 0002222 PRESCRIPTION T00010 ACTIVE

Plan Active

-------------------------------------------------------------------------------

#### Group Plan Status Inquiry \[IBCNR PLAN STATUS INQUIRY\]

The Group Plan Status Inquiry option may be selected from the IBCNR E-Pharmacy Menu screen, using synonym, PSI.

The NCPDP process requires that users match group plans to pharmacy plans. This option, along with the Group Plan Status Report will assist users in evaluating GROUP INSURANCE PLAN file (#355.3) entries that have inactive plans or need to be matched to pharmacy plans.

Example

Select e-Pharmacy Menu Option: psi Group Plan Status Inquiry

Select INSURANCE COMPANY: IBGROUP1 555 MAIN STREET ANYCITY TENN

ESSEE Y

Select one of the following:

A All Group Plans

P Pharmacy Group Plans

M Matched Group Plans

Select the type of Group Plans you want to see: M// \<RET\> atched Group Plans

SH Show details for a Group Plan status

Group Plan Status Inquiry Mar 02, 2006@10:46:01 Page: 1 of 1

All Plans for: IBGROUP1 Phone: 1-888-882-8800

555 MAIN STREET Precerts: \<not filed\>

ANYCITY, TN 99999

For: Matched Group Plans.

Group Name Group Number Type of Plan Plan ID Pln Stat

1 IBGROUP1 GROUP1 PRESCRIPTION T00010 ACTIVE

2 IBGROUP2 GROUP2 PRESCRIPTION T00010 ACTIVE

3 IBGROUP3 GROUP3 PRESCRIPTION T00010 ACTIVE

Enter ?? for more actions

SH Show details for a Group Plan status

Select Action:Quit// SH=1 Show details for a Group Plan status

ePHARM GROUP PLAN STATUS INQUIRY Mar 02, 2006@10:50 Page: 1

Report for Matched Group Plans for WEBMD

Group Name Group \# Plan Type Plan ID Pln Stat

===============================================================================

IBGROUP1 GROUP1 PRESCRIPTION T00010 ACTIVE

Plan Active

Enter RETURN to continue or '^' to exit:.

### Modified Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Copy and Cancel \[IB COPY AND CANCEL\] and IB Cancel Bill \[IB CANCEL BILL\]

The software supporting these two options was modified to prevent the cancellation of an ECME bill, if a reversal through the ECME package was not performed. If the software interprets that the user has not yet performed the ECME reversal on the bill, a warning message is displayed to the user, indicating that the bill needs to be cancelled by performing a reversal using the ECME package, and the process terminates. If the software interprets the user has performed the reversal through ECME, then the software is mapped to the existing cancellation algorithm.

Example

Select OPTION NAME: IB CANCEL BILL Cancel Bill

Cancel Bill

Enter BILL NUMBER or Patient NAME: K400KJU IBpatient,Two 07-27-05

Outpatient REIMBURSABLE INS. PRNT/TX

This bill was created by the Electronic Claims Management Engine (ECME).

Cancellation needs to occur in the ECME package by submitting a REVERSAL to the Payer.

Has a REVERSAL for this e-Claim already been submitted to the payer via the ECME package (Y/N)? NO// y YES

ARE YOU SURE YOU WANT TO CANCEL THIS BILL? No// y (Yes)

LAST CHANCE TO CHANGE YOUR MIND...

CANCEL BILL?: y (YES)

Example:

Select OPTION NAME: IB CANCEL BILL Cancel Bill

Cancel Bill

Enter BILL NUMBER or Patient NAME: K400KJU IBpatient,Two 07-27-05

Outpatient REIMBURSABLE INS. PRNT/TX

This bill was created by the Electronic Claims Management Engine (ECME).

Cancellation needs to occur in the ECME package by submitting a REVERSAL to the Payer.

Has a REVERSAL for this e-Claim already been submitted to the payer via the ECME package (Y/N)? NO// n NO

\<PLEASE SUBMIT A REVERSAL USING THE APPROPRIATE OPTION IN THE ECME PACKAGE\>

Example:

Select OPTION NAME: COPY AND CANCEL IB COPY AND CANCEL Copy and Cancel

Copy and Cancel

Enter BILL NUMBER or Patient NAME: K400KIQ IBpatient,One 11-21-05

Outpatient REIMBURSABLE INS. PRNT/TX

This bill was created by the Electronic Claims Management Engine (ECME).

Cancellation needs to occur in the ECME package by submitting a REVERSAL to the Payer.

Has a REVERSAL for this e-Claim already been submitted to the payer via the ECME package (Y/N)? NO// y YES

ARE YOU SURE YOU WANT TO CANCEL THIS BILL? No// y (Yes)

LAST CHANCE TO CHANGE YOUR MIND...

CANCEL BILL?: y (YES)

Example:

Select OPTION NAME: IB CANCEL BILL Cancel Bill

Cancel Bill

Enter BILL NUMBER or Patient NAME: K400KJU IBpatient,Two 07-27-05

Outpatient REIMBURSABLE INS. PRNT/TX

This bill was created by the Electronic Claims Management Engine (ECME).

Cancellation needs to occur in the ECME package by submitting a REVERSAL to the Payer.

Has a REVERSAL for this e-Claim already been submitted to the payer via the ECME package (Y/N)? NO// n NO

\<PLEASE SUBMIT A REVERSAL USING THE APPROPRIATE OPTION IN THE ECME PACKAGE\>

#### Move Subscribers to a Different Plan \[IBCN MOVE SUBSCRIB TO PLAN\]

This option is located on the Patient Insurance Menu, and may be used to move a group of subscribers from a selected Pharmacy Benefits Management (PBM) plan to another. The plans may be associated with the same Insurance Company or a different one. Plan and annual benefit information may be moved as well.

New capability has been added to apply a new plan Effective Date. When this new effective date is entered, the previous insurance information remains in the Patient Profile, but shows as expired as of the new plan effective date. This can be used when insurance groups change PBMs for processing electronic Pharmacy claims. By leaving the old plan information intact, the user will be able to monitor PBM changes that affect the electronic pharmacy claims.

A mail bulletin will be sent to the user and members of the IB NEW INSURANCE Mail Group.

Example

Do you want to EXPIRE the old plan by entering the new plan Effective date? NO// y YES

Effective Date of the new Plan: t (OCT 26, 2005)

You selected to move 1 subscribers and EXPIRE the old plan in the patient

profile.

FROM Insurance Company CompanyOne

Plan Name PlanOne Number 666072

TO Insurance Company CompanyTwo

Plan Name PlanTwo Number 666001

BY switching to the new Insurance/Plan

with Effective Date OCT 26, 2005

Please Note that the old insurance group plan will be EXPIRED in the patient

profile!

Okay to continue? y YES

Moving subscribers .

Done. All subscribers were moved as requested!

The Bulletin was sent to you and members of 'IB NEW INSURANCE' Mail Group.

#### Claims Tracking Edit

The CLAIMS TRACKING EDIT list manager screen has been modified to allow users to submit ECME claims from the following menu options.

Claims Tracking Edit \[IBT EDIT TRACKING ENTRY\]

Claims Tracking Edit \[IBT EDIT BI TRACKING ENTRY\]

The user's screen now displays the actual NDC number for the prescription. Previously, the CT screen displayed the NDC Number from the DRUG file. The NDC Number is now pulled from the PRESCRIPTION file to correctly reflect the user's changes.

The capability has also been added which allows you to electronically re-submit prescriptions associated with the Claims Tracking record, and it is possible to submit the Rx electronically, if the CT record has a non-billable record "NEEDS SC DETERMINATION".

Example

<u>Claims Tracking Editor Dec 08, 2005@13:55 Page: 1 of 3</u>

Claims Tracking Entries for: IBpatient,One K5551

for Visits beginning on: 12/08/04 to 12/22/05

<u>Type Urgent Date Ins. UR ROI Bill Ward</u>

1 RxFill NO 12/01/05 YES NO

2 RxFill NO 11/29/05 YES YESe

3 RxFill NO 11/29/05 YES YESe

4 RxFill NO 11/02/05 YES NO

5 RxFill NO 11/01/05 YES NO

6 RxFill NO 10/14/05 YES YESe

7 RxFill NO 10/14/05 YES NO

8 RxFill NO 10/13/05 YES YESe

9 RxFill NO 10/13/05 YES YESe

10 RxFill NO 10/13/05 YES YESe

11 RxFill NO 10/13/05 YES YES

<u>12 RxFill NO 10/13/05 YES NO</u>

<u>+ Service Connected: NO \>\>\></u>

BI Billing Info Edit CP Change Patient EX Exit

VE View/Edit Episode CD Change Date Range

SC SC Conditions VP View Pat. Ins.

Select Action: Next Screen// ve=2

<u>  
Expanded Claims Tracking Entry Dec 08, 2005@13:56:50 Page: 1 of 3</u>

Expanded Claims Tracking Info for: IBpatient,One K5551 ROI:

For: PRESCRIPTION REFILL on 11/29/05

Visit InformationTreatment Authorization Info

Visit Type: PRESCRIPTION REFILL Authorization \#:

Prescription \#: 383209 No. Days Approved: 0

Fill Date: Nov 29, 2005 Second Opinion Required:

Drug: ATENOLOL 50MG TAB Second Opinion Obtained:

Quantity: 33

Days Supply: 90 Review Information

2 NDC#: 00310-0105-10 Insurance Claim: YES

Physician: IBphysician,One MD Follow-up Type:

Random Sample:

Special Condition:

Local Addition:

Ins. Reviewer:

<u>Hospital Reviewer:</u>

<u>+ Enter ?? for more actions</u>

BI Billing Info Edit TA Treatment Auth. EX Exit

RI Review Info SE Submit Claim to ECME

Select Action: Next Screen// SE

This option sends electronic Pharmacy Claims to the Payer

Submit the Rx# 909954 to ECME for electronic billing? NO// y YES

Submitting Rx# 909954 ...

Claim Status:

IN PROGRESS-Waiting to start

IN PROGRESS-Waiting for packet build

IN PROGRESS-Waiting for transmit

IN PROGRESS-Transmitting

E PAYABLE

Following are examples of some possible results when “SE Submit Claim to ECME” is selected.

Attempting to send a claim to ECME that contains a valid Bill#.

This option sends electronic Pharmacy Claims to the Payer

Rx# 383209 was previously billed.

Please manually cancel the bill# K400KJ0 before submitting claim to ECME.

Cannot submit to ECME. Press RETURN to continue:

Attempting to send a claim to ECME where the Rx is NOT Released (i.e., not yet billable)

This option sends electronic Pharmacy Claims to the Payer

The Prescription is not released.

Cannot submit to ECME. Press RETURN to continue:

Attempting to send a claim to ECME that has already been processed in ECME.

This option sends electronic Pharmacy Claims to the Payer

Submit the Rx# 909954 to ECME for electronic billing? NO// y YES

Submitting Rx# 909954 ...

Previously billed through ECME: E REJECTED

Not sent through ECME.

\*\*\* ECME returned status: No billing through ECME

Press RETURN to continue:

Attempting to send a claim to ECME that has already been processed in ECME and was stranded.

Submit the selected RX(s) to ECME for electronic billing? NO// y YES

Submitting Rx# 910053 (original fill) ...

Previous ECME claim is stranded, claim needs to be unstranded

Not sent

\*\*\* ECME returned status: No billing through ECME

Press RETURN to continue:

## Technical Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enhancements to the IB-ECME API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following enhancements are added to the IB-ECME API.

- When the pharmacy user closes an ECME Claim, they are prompted for a Close Reason, which is passed to IB. Depending on the user's response, the respective Claims Tracking record will be marked as Billable or Non-billable with a corresponding non-billable reason. The CLOSE REASON is stored in the REASON NOT BILLABLE field (#.19) of the CLAIMS TRACKING File (#356).
- When a user closes a claim in the ECME package, they will be able to enter a free text comment at the Comment prompt. The free text comment is passed to IB from ECME in the CLOSE COMMENT array element. The CLOSE COMMENT is stored in the ADDITIONAL COMMENT field (#1.08) of the CLAIMS TRACKING File (#356).
- When the payer rejects the ECME claim, or the claim is closed by the OPECC, IB will automatically pass the held first party charges to Accounts Receivable.
- IB will not allow ECME to send electronic claims if the AutoBiller already created the bill, unless the AutoBiller bill is cancelled.
- The new parameter, DIVISION has been added to the INPUT array, which contains a pointer value from an entry I the MEDICAL CENTER DIVISION file (#40.8). This DIVISION value is associated with the facility form which the Rx was filled.
- IB API has been modified to return non ECME-billable status if the DEA parameter is not defined.
- IB API has been modified to avoid billing problems causing Incomplete Bills when attempting to create an e-Pharmacy Bill for a patient who does not have insurance for the current date.

### New Purge Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new purge routine, ^IBEVNTP, was created to enable IRM to remove ^XTMP subscripts that were built by the IB package, if space for ^XTMP becomes an issue. The data at subscripts, "IBNCPDP-"\_date, are referenced and reported by the IB ECME Billing Events report generated by the ECME Billing Events Report option \[IB ECME BILLING EVENTS\].

This purge should only be executed by IRM, and therefore will not be accessible by a Kernel menu option. IRM should coordinate this purge operation with the appropriate billing/accounts receivable staff to determine how much data should be purged.

Please note that the purge will automatically keep 35 consecutive days (from the current date) worth of data. To invoke the purge, IRM should enter D EN^IBEVNTP at the programmer prompt.

The ECME Billing Events Report option \[IB ECME BILLING EVENTS\] must be disabled before running the purge.

Example:

\>D EN^IBEVNTP

The software supporting the Integrated Billing (IB) option, ECME Billing Events Report, references the ^XTMP temporary global array. The subscript, and associated descendent nodes, that this report references are at ^XTMP("IBNCPDP-"\_date) where date is equal to the (fileman) date that the global was created. This program will enable the IRM staff to remove the subscripts if space for ^XTMP becomes an issue.

Please coordinate this purge with the appropriate staff that work with the IB and Accounts Receivable packages before executing this program. You will need to determine how many days worth of data the staff wish to keep.

The system has subscripts dating from Sep 07, 2005 to Mar 06, 2006.

The purge will BEGIN at this date: Sep 07, 2005 and can STOP at this date: Jan 30, 2006. You can change the STOP date to an earlier date, but not a later date (e.g.,STOP date \< Jan 30, 2006).

Enter purge STOP date: 9/8/05 (SEP 08, 2005)

Are you sure? Y/N? NO// YES

Starting ...

The system has removed subscripts dating from Sep 07, 2005 to Sep 08, 2005.

### The Post-install Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Edit HIPAA NCPDP Flag Option

The post-install procedure of this patch enables the IBCNR EDIT HIPAA NCPDP FLAG menu option, which was distributed by patch IB\*2.0\*251, but was previously “Out of Order”.

The Edit HIPAA NCPDP Flag option allows users to edit the HIPAA NCPDP ACTIVE FLAG field (11.01) of the IB SITE PARAMETERS file (350.9), which is the master switch to control e-Pharmacy NCPDP transactions.

IBCNR E-PHARMACY MENU e-Pharmacy Menu

ECMP ECME CMOP Report

EHNF Edit HIPAA NCPDP FLAG

ENP Edit NCPDP PROCESSOR APPLICATION Sub-file

EPAY Edit PAYER APPLICATION Sub-file

EPBM Edit PBM APPLICATION Sub-file

EPLA Edit PLAN APPLICATION Sub-file

EVNT ECME Billing Events Report

MGP Match Group Plan to a Pharmacy Plan

MMGP Match Multiple Group Plans to a Pharmacy Plan

MTPS Match Test Payer Sheet to a Pharmacy Plan

RGPW Group Plan Worksheet Report

RPP Pharmacy Plan Report

Select \<V15 West\> e-Pharmacy Menu Option: EHNF Edit HIPAA NCPDP FLAG

Edit HIPAA NCPDP ACTIVE FLAG

(master switch to control e-Pharmacy NCPDP transactions)

350.9 IB SITE PARAMETERS File

11.01 HIPAA NCPDP ACTIVE FLAG Field

HIPAA NCPDP ACTIVE FLAG: Inactive// Active

#### The PLAN File

Entries in the PLAN file (#366.03) have been modified to change the default status of the LOCAL ACTIVE? field (#.03) of the APPLICATION subfile (#366.033) from Active to Inactive. This will impact only those plans never edited by the user after installation of patch IB\*2.0\*251; and Plans last edited by the HL7 Automated User. These plans will need to be activated manually after the HIPAA NCPDP product deliverable is installed.

#### IB NON-BILLABLE REASONS

The post installation procedure installs the following new IB NON-BILLABLE REASONS.

1.  90 DAY RX FILL NOT COVERED
2.  NOT A CONTRACTED PROVIDER
3.  INVALID MULTIPLES PER DAY SUPP
4.  REFILL TOO SOON
5.  INVALID NDC FROM CMOP

These Non-Billable Reasons, required for processing NCPDP-related claims, will be added to the NAME field (#.01) of the CLAIMS TRACKING NON-BILLABLE REASONS file (#356.8). If the above non-billable reasons already exist at the site, they will not be added.

The ECME FLAG field (#.02) will be populated with "1" (external value ='YES') to specific entries in the CLAIMS TRACKING NON-BILLABLE REASONS file (#356.8). This will enable their selection by the user when closing a claim in the ECME package.

The following Non-Billable Reasons will be marked to be used as ECME Close Claim Reasons.

1.  NOT INSURED
2.  SERVICE NOT COVERED
3.  COVERAGE CANCELED
4.  INVALID PRESCRIPTION ENTRY
5.  PRESCRIPTION DELETED
6.  PRESCRIPTION NOT RELEASED
7.  DRUG NOT BILLABLE
8.  90 DAY RX FILL NOT COVERED
9.  NOT A CONTRACTED PROVIDER
10. INVALID MULTIPLES PER DAY SUPP
11. REFILL TOO SOON
12. INVALID NDC FROM CMOP
13. OTHER

The following Close Reasons will allow OPECC to pass the prescription to the AutoBiller.

1.  DRUG NOT BILLABLE
2.  90 DAY RX FILL NOT COVERED
3.  NOT A CONTRACTED PROVIDER
4.  OTHER

# Accounts Receivable Patch PRCA\*4.5\*230

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Functional Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch represents the Accounts Receivable portion of Phase III of the NCPDP-Pharmacy Connection project. It modifies the EDI Lockbox functionality by adding the ability to manually process Electronic Explanation of Benefits (EEOBs) related to NCPDP claims.

There are no changes to the existing user interface introduced by this patch. All changes are related to internal EDI Lockbox processing of the Health Care Claim Payment/Advice (835) transaction, also referred to as the Electronic Remittance Advice (ERA), related to the NCPDP electronic pharmacy claims. The 835 transaction is sent to VistA from the AAC in a flat file message via Mailman.

### ECME Matching Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enhancements have been made to the ECME matching procedure. Previously, as implemented in patch PRCA\*4.5\*202, AR used the Statement Date (Segment 05 Piece 9) to find a matching IB/AR bill. With this patch, AR will use the Service Date for matching purposes.

### Screen Out EEOBs Related to e-Pharmacy Rejects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EDI LockBox AR functionality has been modified to screen out EEOBs related to e-Pharmacy rejects. When VistA submits an NCPDP electronic Pharmacy claim and gets a reject, a bill is not created in IB/AR; and therefore VistA does not receive EEOBs in response to those claims. VistA is also unable to process those reject-related EEOBs.

Previously, these reject-related EEOBs were displayed on the EDI LOCKBOX EXCEPTIONS user screen of the EDI Lockbox 3rd Party Exceptions option \[RCDPE EXCEPTION PROCESSING\], and required manual resolution. With this patch, AR will be able to recognize such EEOBs and disregard them. This means that they are not stored in the ELECTRONIC REMITTANCE ADVICE file (#344.4), and will not be displayed on the EDI LOCKBOX EXCEPTIONS screen.