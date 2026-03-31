---
title: PSX*2*65 Release Notes - ePharmacy Phase 4 Iteration II
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: ePharmacy Phase 4 Iteration II
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2*65
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - cmop
  - table
  - contents
  - suspense
  - ecme
  - prescriptions
  - prescription
  - hold
  - fill
  - date
page_count: 0
word_count: 1422
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_p65_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_p65_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

![](psx-2-65-release-notes-epharmacy-phase-4-iteration-ii/001.png)

consolidated mail outpatient pharmacy (cMOP)

ePharmacy Phase 4 Iteration II

Release Notes

PSX\*2\*65

July 2009

Veterans Health Information Technology

*(This page included for two-sided copying.)*Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Consolidated Mail Outpatient Pharmacy V. 2.0 - PSX\2\65](#consolidated-mail-outpatient-pharmacy-v-20-psx265)
  - [Overview](#overview)
  - [Functional Enhancements](#functional-enhancements)
    - [Discontinue feature for unreleased CMOP Rx](#discontinue-feature-for-unreleased-cmop-rx)
    - [Host Errors](#host-errors)
    - [¾ Days Supply Hold](#¾-days-supply-hold)
    - [CMOP/ECME Activity Report](#cmopecme-activity-report)
    - [CMOP Prescriptions pick up after midnight](#cmop-prescriptions-pick-up-after-midnight)
This ePharmacy Phase 4 Iteration II release includes updates for PSX\*2\*65. This patch is one of five patches that enhance the ePharmacy software to provide the framework to support Outpatient Pharmacy billing.
Installation instructions are included in the patch description. Below is a list of all the applications involved in this project along with their associated patch number:
APPLICATION/VERSION PATCH
-------------------------------------------------------------------------------------- --------------
1\. CONSOLIDATED MAIL OUTPATIENT PHARMCY (CMOP) V. 2.0 PSX\*2\*65
2\. PHARMACY DATA MANAGEMENT (PDM) V. 1.0 PSS\*1\*131
3\. OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*289
4\. ELECTRONIC CLAIMS MANAGEMENT ENGINE (ECME) V. 1.0 BPS\*1\*7
5\. INTEGRATED BILLING (IB) V. 2.0 IB\*2\*384
The last three patches (PSO\*7\*289, IB\*2\*384 and BPS\*1\*7) will be released in the Kernel Installation and Distribution System (KIDS) multi-build distribution BPS PSO IB BUNDLE 3.0. Patches PSX\*2\*65 and PSS\*1\*131 will be released as stand-alone patches. Since there is an implementation dependency between the multi-build distribution and the stand-alone patches, PSX\*2\*65 and PSS\*1\*131 must be installed prior to the installation of the multi-build. For more specific instructions please
refer to the installation steps provided in each of the patches.

# Consolidated Mail Outpatient Pharmacy V. 2.0 - PSX\*2\*65

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSX\*2\*65 includes the following enhancements:

- A modification was made to not immediately reverse a claim through ECME for an unreleased CMOP fill when the prescription/fill is discontinued. Additional validations will occur.
- New functionality was added to prevent prescriptions from being filled/sent to CMOP when a host processing error occurs and the claim is submitted through ECME. The host processing errors are identified by reject codes M6, M8, NN, and 99.
- New functionality was added to the Print from Suspense File \[PSO PNDLBL\] option to prevent prescriptions from being transmitted to CMOP or printed from suspense until 3/4 of the days supply of the Rx/fill has elapsed for local mail and CMOP. This does not affect pull early from suspense functionality.
- The 'CMOP/ECME Activity Report' \[BPS RPT CMOP/ECME ACTIVITY\] has been modified to: display D for Dispensed or T for Transmitted, allow for the selection of detailed or summary view, allow for the selection of a list of patients or all patients, include a prompt for division, and other formatting changes.
- A modification was made to allow for CMOP Suspense Date Rx's picked up after midnight to be sent to ECME appropriately.

## Functional Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Discontinue feature for unreleased CMOP Rx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a prescription is transmitted to CMOP then subsequently discontinued, the third party claim will not be reversed immediately as was the case prior to this patch. When CMOP attempts to release the prescription, the system will validate the prescription for a discontinued status. The following criteria determines whether the claim is reversed:

- If it was discontinued and CMOP did not fill the prescription, the third party claim will be reversed. The following is an example of the ECME Log entry:

> 2 6/25/08@13:31:22 ORIGINAL OPPHARM,ONE

> Comments: Reversal sent to ECME: UNSUCCESSFUL CMOP RELEASE

- If the prescription was discontinued and CMOP filled the prescription, the third party claim will not be reversed.

There is no user interaction for this enhancement.

### Host Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality was added to prevent prescriptions from being filled/sent to CMOP when a host processing error occurs when a claim is submitted through ECME. Host processing errors are identified by reject codes M6, M8, NN, and 99 which are returned by the third party payer. The following conditions apply when this scenario occurs.

- The transmission of the prescription fill will be delayed 1 day in hopes that the host processing issues will be resolved by the third party payer.
- An activity log entry will be added to state the date/time along with a comment stating that the Rx/fill was left in suspense hold due to a host processing error. Example:

> 2 06/25/08 SUSPENSE ORIGINAL OPPHARM,TWO

> Comments: SUSPENSE HOLD until 6/26/08 due to host reject error.

- The Pull Early from Suspense function is not impacted by this added functionality. Users may pull these type prescriptions early from suspense.

This functionality requires no user interaction.

### ¾ Days Supply Hold

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New functionality was added to the Print from Suspense File \[PSO PNDLBL\] option to prevent ePharmacy prescriptions from being printed from suspense or transmitted to CMOP until 3/4 of the days supply of the previous fill has elapsed. Doing this helps decrease Refill-Too-Soon third party payer rejects.

The system calculates the day when ¾ of the days supply will have elapsed by first multiplying (.75) times the days supply for the fill, then calculates the hold date as previous fill date plus that value. If the hold date is greater than LAST DISPENSED DATE field (#101), the prescription is placed on EPHARMACY SUSPENSE HOLD. For renewals, the PRIOR FILL DATE field (#102.1) is used for comparison. Both comparison fields are located in PRESCRIPTION file (#52). If the prescription is to be placed on EPHARMACY SUSPENSE HOLD, the EPHARMACY SUSPENSE HOLD DATE (#86) field in PRESCRIPTION file (#52) for the fill will be defined with the hold date. This functionally takes place in the background.

An activity log entry will be added to state the date/time that the Rx will be allowed to be removed from suspense. Only the initial evaluation for the ¾ Days Supply hold functionality will create an activity log entry. The following is an example:

> Activity Log:

> \# Date Reason Rx Ref Initiator Of Activity

> ===============================================================================

> 3 06/17/08 SUSPENSE REFILL 2 OPPHARM,ONE

> Comments: RX Placed on Suspense for CMOP until 06-17-08

> 4 06/17/08 SUSPENSE REFILL 2 OPPHARM,TWO

> Comments: 3/4 of Days Supply SUSPENSE HOLD until 6/19/08.

> 5 06/19/08 PROCESSED REFILL 2 OPPHARM,ONE

> Comments: Transmitted to DALLAS CMOP

On the Suspense Hold date, the prescription will be allowed to be transmitted to CMOP and printed from suspense for locally suspended prescription fills.

Prescriptions in a Suspense Hold status can still be manually pulled early from suspense.

### CMOP/ECME Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *CMOP/ECME Activity Report* \[BPS RPT CMOP/ECME ACTIVITY\] option has been modified to provide users additional options.

- The CMOP-STATUS column will display D for Dispense and T for Transmitted instead of partially spelling out the status.
- The title and header information will be centered.
- A prompt will be added to select detailed or summary information. Detailed information will reflect what is currently displayed. Summary information will shorten the batch header section of the report and only display information from batches that have ePharmacy prescriptions.
- A prompt will be added to select a list of patients (or ^ALL). Only patients on the list will be included in the detail.
- The division prompt will be modified to be consistent with other ECME options, i.e., the selection prompt will show 'A ALL DIVISIONS' first, 'S SELECT DIVISIONS' second, and will roll into particular divisions if the user selects an 'S'.
- A prompt will be added to select released, unreleased, or all prescriptions.

The following is an example of the prompts for this option:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \*Electronic Claims Management Engine (ECME) V1.0\*

> \* ASHEVILLE VAMC \*

> \* Claim Results and Status \*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> PAY Payable Claims Report

> REJ Rejected Claims Report

> ECMP CMOP/ECME Activity Report

> REV Reversal Claims Report

> NYR Claims Submitted, Not Yet Released

> REC Recent Transactions

> DAY Totals by Date

> CLO Closed Claims Report

> Select Claim Results and Status Option: CMOP/ECME Activity Report

> ENTER BEGINNING TRANSMISSION DATE: T-30

> ENTER ENDING TRANSMISSION DATE: T

> Select one of the following:

> S Summary

> D Detail

> Display (S)ummary or (D)etail format: Detail// Summary

> You may select a single or multiple PATIENTS,

> or enter ^ALL to select all PATIENTS.

> Select PATIENT NAME: ^ALL

> SELECTION OF DIVISION(S)

> Select one of the following:

> A ALL DIVISIONS

> S SELECT DIVISIONS

> Enter response: SELECT DIVISIONS

> 1 CHEYENNE VAM&ROC

> 2 ECME PHARMACY

> 3 FORT COLLINS CLINIC

> 4 GREELEY CLINIC

> 5 OP TEST SITE \#1

> 6 OP TEST SITE \#2

> 7 SIDNEY CLINIC

> Select Division(s) : (1-7): 1

> You have selected:

> 1 CHEYENNE VAM&ROC

> Is this correct? YES//

> Select one of the following:

> R RELEASED

> N NOT RELEASED

> A ALL

> Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED// ALL

> Do you want to capture report data for an Excel document? NO//

> Select Printer:

The following is an example of a summary report for all patients:

> CMOP/ECME ACTIVITY REPORT for CHEYENNE VAM&ROC

> For JUN 30,2008 thru JUL 30,2008 Printed: Jul 30, 2008@17:22:02

> ================================================================================

> TRANSMISSION:16301 TRANSMISSION DATE/TIME: JUL 06, 2008@22:58:24

> TOTAL PATIENTS: 1 TOTAL RXS: 1

> NAME ECME#/RX#/FL# NDC SENT NDC RECVD CMOP-STAT

> DRUG INSURANCE PAY-STAT BILL# REL-DATE

> ================================================================================

> OPPATIENT,FOUR (9987) 1615001/2055123\$e/1 00168-0026-38 T

> BACITRACIN 500 UNT BLUE MOON INSUR E PAYAB

> Press RETURN to continue, '^' to exit:

> CMOP/ECME ACTIVITY REPORT for CHEYENNE VAM&ROC

> For JUN 30,2008 thru JUL 30,2008 Printed: Jul 30, 2008@17:22:04

> ================================================================================

> TRANSMISSION:16302 TRANSMISSION DATE/TIME: JUL 07, 2008@14:21:06

> TOTAL PATIENTS: 1 TOTAL RXS: 2

> NAME ECME#/RX#/FL# NDC SENT NDC RECVD CMOP-STAT

> DRUG INSURANCE PAY-STAT BILL# REL-DATE

> ================================================================================

> OPPATIENT,FIVE (7452) 1615048/2055154\$e/1 00781-1893-01 T

> BENAZEPRIL HCL 20M BLUE MOON INSUR E REJEC

> OPPATIENT,FIVE (7452) 1615100/2055201\$e/0 00026-2863-51 T

> ACARBOSE 25MG TAB BLUE MOON INSUR E PAYAB

> Press RETURN to continue, '^' to exit:

The following is an example of a detailed report for all patients:

> CMOP/ECME ACTIVITY REPORT for CHEYENNE VAM&ROC

> For JUN 30,2008 thru JUL 30,2008 Printed: Jul 30, 2008@17:23:42

> ================================================================================

> TRANSMISSION: 16299

> STATUS: TRANSMITTED

> DIVISION: CHEYENNE VAM&ROC

> CMOP SYSTEM: DALLAS

> TRANSMISSION DATE/TIME: JUL 01, 2008@22:58:26

> TOTAL PATIENTS: 1

> TOTAL RXS: 1

> NAME ECME#/RX#/FL# NDC SENT NDC RECVD CMOP-STAT

> DRUG INSURANCE PAY-STAT BILL# REL-DATE

> ================================================================================

> \*\*\*\*\*\*\*\*\* BATCH HAS NO ECME BILLABLE PRESCRIPTIONS \*\*\*\*\*\*\*

> Press RETURN to continue, '^' to exit:

> CMOP/ECME ACTIVITY REPORT for CHEYENNE VAM&ROC

> For JUN 30,2008 thru JUL 30,2008 Printed: Jul 30, 2008@17:23:43

> ================================================================================

> TRANSMISSION: 16300

> STATUS: TRANSMITTED

> DIVISION: CHEYENNE VAM&ROC

> CMOP SYSTEM: DALLAS

> TRANSMISSION DATE/TIME: JUL 02, 2008@22:58:24

> TOTAL PATIENTS: 1

> TOTAL RXS: 1

> NAME ECME#/RX#/FL# NDC SENT NDC RECVD CMOP-STAT

> DRUG INSURANCE PAY-STAT BILL# REL-DATE

> ================================================================================

> \*\*\*\*\*\*\*\*\* BATCH HAS NO ECME BILLABLE PRESCRIPTIONS \*\*\*\*\*\*\*

> Press RETURN to continue, '^' to exit:

> CMOP/ECME ACTIVITY REPORT for CHEYENNE VAM&ROC

> For JUN 30,2008 thru JUL 30,2008 Printed: Jul 30, 2008@17:23:45

> ================================================================================

> TRANSMISSION: 16301

> STATUS: TRANSMITTED

> DIVISION: CHEYENNE VAM&ROC

> CMOP SYSTEM: DALLAS

> TRANSMISSION DATE/TIME: JUL 06, 2008@22:58:24

> TOTAL PATIENTS: 1

> TOTAL RXS: 1

> NAME ECME#/RX#/FL# NDC SENT NDC RECVD CMOP-STAT

> DRUG INSURANCE PAY-STAT BILL# REL-DATE

> ================================================================================

> OPPATIENT,FOUR (9987) 1615001/2055123\$e/1 00168-0026-38 T

> BACITRACIN 500 UNT BLUE MOON INSUR E PAYAB

> Press RETURN to continue, '^' to exit:

> CMOP/ECME ACTIVITY REPORT for CHEYENNE VAM&ROC

> For JUN 30,2008 thru JUL 30,2008 Printed: Jul 30, 2008@17:23:46

> ================================================================================

> TRANSMISSION: 16302

> STATUS: TRANSMITTED

> DIVISION: CHEYENNE VAM&ROC

> CMOP SYSTEM: DALLAS

> TRANSMISSION DATE/TIME: JUL 07, 2008@14:21:06

> TOTAL PATIENTS: 1

> TOTAL RXS: 2

> NAME ECME#/RX#/FL# NDC SENT NDC RECVD CMOP-STAT

> DRUG INSURANCE PAY-STAT BILL# REL-DATE

> ================================================================================

> OPPATIENT,FIVE (7452) 1615048/2055154\$e/1 00781-1893-01 T

> BENAZEPRIL HCL 20M BLUE MOON INSUR E REJEC

> OPPATIENT,FIVE (7452) 1615100/2055201\$e/0 00026-2863-51 T

> ACARBOSE 25MG TAB BLUE MOON INSUR E PAYAB

> Press RETURN to continue, '^' to exit:

The following is an example of the report where a single patient was selected:

> Select Claim Results and Status Option: CMOP/ECME Activity Report

> ENTER BEGINNING TRANSMISSION DATE: t-30

> ENTER ENDING TRANSMISSION DATE: t

> Select one of the following:

> S Summary

> D Detail

> Display (S)ummary or (D)etail format: Detail// Summary

> You may select a single or multiple PATIENTS,

> or enter ^ALL to select all PATIENTS.

> Select PATIENT NAME: OPPAT

> 1 OPPATIENT,FIVE 10-20-50 666987452 NO NSC VETERAN

> 2 OPPATIENT,FOUR 10-20-65 666559987 NO NSC VETERAN

> 3 OPPATIENT,ONE 10-18-63 666874529 NO NSC VETERAN

> 4 OPPATIENT,THREE 10-21-55 666874598 NO NSC VETERAN

> 5 OPPATIENT,TWOL 10-18-62 666259874 NO ACTIVE DUTY

> ENTER '^' TO STOP, OR

> CHOOSE 1-5: 2 OPPATIENT,FOUR 10-20-65 666559987 NO NSC VETERA

> N

> Select PATIENT NAME:

> SELECTION OF DIVISION(S)

> Select one of the following:

> A ALL DIVISIONS

> S SELECT DIVISIONS

> Enter response: SELECT DIVISIONS

> 1 CHEYENNE VAM&ROC

> 2 ECME PHARMACY

> 3 FORT COLLINS CLINIC

> 4 GREELEY CLINIC

> 5 OP TEST SITE \#1

> 6 OP TEST SITE \#2

> 7 SIDNEY CLINIC

> Select Division(s) : (1-7): 1

> You have selected:

> 1 CHEYENNE VAM&ROC

> Is this correct? YES//

> Select one of the following:

> R RELEASED

> N NOT RELEASED

> A ALL

> Include Rxs - (R)ELEASED or (N)OT RELEASED or (A)LL: RELEASED// ALL

> Do you want to capture report data for an Excel document? NO//

> Select Printer: TELNET TERMINAL

> CMOP/ECME ACTIVITY REPORT for CHEYENNE VAM&ROC

> For JUN 30,2008 thru JUL 30,2008 Printed: Jul 30, 2008@17:25:16

> ================================================================================

> TRANSMISSION:16301 TRANSMISSION DATE/TIME: JUL 06, 2008@22:58:24

> TOTAL PATIENTS: 1 TOTAL RXS: 1

> NAME ECME#/RX#/FL# NDC SENT NDC RECVD CMOP-STAT

> DRUG INSURANCE PAY-STAT BILL# REL-DATE

> ================================================================================

> OPPATIENT,FOUR (9987) 1615001/2055123\$e/1 00168-0026-38 T

> BACITRACIN 500 UNT BLUE MOON INSUR E PAYAB

> Press RETURN to continue, '^' to exit:

> CMOP/ECME ACTIVITY REPORT for CHEYENNE VAM&ROC

> For JUN 30,2008 thru JUL 30,2008 Printed: Jul 30, 2008@17:25:18

> ================================================================================

> TRANSMISSION:16304 TRANSMISSION DATE/TIME: JUL 11, 2008@22:57:05

> TOTAL PATIENTS: 1 TOTAL RXS: 1

> NAME ECME#/RX#/FL# NDC SENT NDC RECVD CMOP-STAT

> DRUG INSURANCE PAY-STAT BILL# REL-DATE

> ================================================================================

> OPPATIENT,FOUR (9987) 1615102/2055203\$e/0 00024-0303-06 T

> DANAZOL 50MG CAP BLUE MOON INSUR E PAYAB

> Press RETURN to continue, '^' to exit:

### CMOP Prescriptions pick up after midnight

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the CMOP transmission starts, all prescriptions in suspense are evaluated to see if they should be submitted to ECME first and if so are submitted. This is done to allow ECME enough time to process third party claim submissions prior to sending the prescriptions to CMOP so that any third party rejections may be properly evaluated. Next the system re-evaluates suspended prescriptions to pull the latest list of fills to be sent to CMOP. Between the time that the ePharmacy submissions are made and the CMOP batch is built, subsequent prescriptions are filled and have not been submitted to ECME. These “in between” prescriptions were not being submitted for 3<sup>rd</sup> party claims. A code change was made to make ECME submissions for these prescriptions. .

There is no user interaction for this functionality.