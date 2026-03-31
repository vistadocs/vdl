---
title: PSO*7*264 FY07 Qtr 04 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: FY07 Qtr 04
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*264
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patient
  - report
  - internet
  - table
  - contents
  - refill
  - refills
  - cmop
  - date
  - updates
page_count: 0
word_count: 2486
section_count: 7
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p264_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p264_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

![](pso-7-264-fy07-qtr-04-release-notes/001.png)

oUTPATIENT Pharmacy FY07 Q4

Release Notes

PSO\*7\*264

PSX\*2\*58

October 2007

Veterans Health Information Technology
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Outpatient Pharmacy V. 7.0](#outpatient-pharmacy-v-70)
- [Internet Refill Automation and Reporting](#internet-refill-automation-and-reporting)
  - [Using the Automate Internet Refill Option](#using-the-automate-internet-refill-option)
  - [Using the Internet Refill Report Option](#using-the-internet-refill-report-option)
  - [Separation of Prompts for CNH and Inpatient Refills](#separation-of-prompts-for-cnh-and-inpatient-refills)
- [Local Mailouts with Foreign Addresses](#local-mailouts-with-foreign-addresses)
- [Suspense Functions Update](#suspense-functions-update)
  - [Using the Queue CMOP Prescription Option](#using-the-queue-cmop-prescription-option)
    - [Hidden Action Updates to the Medication Profile](#hidden-action-updates-to-the-medication-profile)
- [Clozapine Processing Update](#clozapine-processing-update)
- [View Provider Option Update](#view-provider-option-update)
- [Patient Information Screen Updates (HD187273)](#patient-information-screen-updates-hd187273)
- [Report Updates](#report-updates)
  - [Log of Suspended Rx's by Day (this Division) Updates](#log-of-suspended-rxs-by-day-this-division-updates)
  - [Bad Address Suspended List Updates](#bad-address-suspended-list-updates)
- [Consolidated Mail Outpatient Pharmacy (CMOP) V. 2.0](#consolidated-mail-outpatient-pharmacy-cmop-v-20)
The Outpatient Pharmacy Fiscal Year 2007 Quarter 4 (FY07 Q4) release includes updates in PSO\*7\*264 and PSX\*2\*58. Installation instructions are included in each patch description.
As part of this FY07 Q4 release, the *Outpatient Pharmacy V. 7.0 User Manual* is divided into four separate manuals:
- *Manager’s User Manual* – for options accessed through the PSO MANAGER menu
- *Pharmacist’s User Manual* – for options accessed through the PSO USER1 menu
- *Technician’s User Manual* – for options accessed through the PSO USER2 menu
- *User Manual – Supplemental* – (these were previously Appendices in the *Outpatient  
  Pharmacy V. 7.0 User Manual)(This page included for two-sided copying.)*
<span id="_Toc179943411" class="anchor"></span>

# Outpatient Pharmacy V. 7.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FY07 Q4 release includes the following enhancements:

- Internet refill automation, reporting, and MailMan messaging are added to the Outpatient Pharmacy software.
- The *Site Parameter Enter/Edit* \[PSO SITE PARAMETERS\] option is updated to include prompts for allowing refills to inpatient and Contract Nursing Home (CNH) patients.
- For Local Mailouts with foreign addresses, replace address information with \*\*\* FOREIGN ADDRESS \*\*\* on mailing labels.
- Added capability to manually queue prescriptions to Consolidated Mail Outpatient Pharmacy (CMOP) with a new option or hidden action.
- Clozapine AUTH Key and DEA# – Add YSCL AUTHORIZED key & DEA# functionality to Outpatient Pharmacy.
- Add NPI to *View Provider* \[PSO PROVIDER INQUIRE\] option.
- Add the following updates to the Patient Information (Profile) screen:
- The display of the RX Patient Status is added to the Patient Information screen.
- The work and cell phone numbers are added to the display, and editing is allowed from the Patient Update function, as well as the *Update Patient Record* \[PSO PAT\] option.
- Add a new column showing the B/D/F (Bad Address Indicator/ Do Not Mail/ Foreign Address) to the 'Log of Suspended Rx's by Day (this Division)' report.
- The *Bad Address Suspended List* \[PSO BAI SUSPENDED\] option is modified to include the prompt of either B/D/F or 'ALL' in the unprinted suspended prescriptions report.

*(This page included for two-sided copying.)*

# Internet Refill Automation and Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSO\*7\*264 provides enhancements to Internet refills, including automating processing of refills and new reporting capabilities.

## Using the *Automate Internet Refill* Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Automate Internet Refill* \[PSO AUTO REFILL INITIALIZE\] option is added to the *Maintenance (Outpatient Pharmacy)* \[PSO MAINTENANCE\] menu, allowing sites to schedule a background job for automatically processing Internet refills.

Internet refills are processed for all active divisions defined in the OUTPATIENT SITE file (#59) that have pending refill entries in the PRESCRIPTION REFILL REQUEST file (#52.43). The *Automate Internet Refill* \[PSO AUTO REFILL INITIALIZE\] option uses the same criteria (prompts) that is used for the *Process Internet Refill* \[PSO INTERNET REFILLS\] option. However, instead of the user responding to the prompts, the criteria is automatically set up by the software as follows:

| Prompt/Criteria                        | Pre-set Value                 |
|--------------------------------------------|-----------------------------------|
| FILL DATE:                                 | TODAY                             |
| MAIL/WINDOW:                               | MAIL                              |
| Will these refills be Queued or Suspended? | SUSPENDED                         |
| PROCESS AUTO REFILLS FOR INPAT?            | NO (but site parameter overrides) |
| PROCESS AUTO REFILLS FOR CNH?              | NO (but site parameter overrides) |

Users must hold the PSOAUTRF key to run this option, and the following warning is displayed if the user does not hold the key.

Example: Automate Internet Refills – no security key held

> Select Maintenance (Outpatient Pharmacy) Option: AUTOMATE Internet Refill

> You must hold the PSOAUTRF key to run this option!

Scheduling the background job includes setting a time and the job’s rescheduling frequency.

![](pso-7-264-fy07-qtr-04-release-notes/002.png)These fields should be left blank: DEVICE FOR QUEUED JOB OUTPUT, QUEUED TO RUN ON VOLUME SET, TASK PARAMETERS, and SPECIAL QUEUEING.

  
Example: Automate Internet Refills – Setting up the background job

> Select Maintenance (Outpatient Pharmacy) Option: AUTOMATE Internet Refill

> Edit Option Schedule

> Option Name: PSO AUTO REFILL

> Menu Text: Automate Internet Refill TASK ID: 173872

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> QUEUED TO RUN AT WHAT TIME: AUG 7,2007@16:40

> DEVICE FOR QUEUED JOB OUTPUT:

> QUEUED TO RUN ON VOLUME SET:

> RESCHEDULING FREQUENCY: 24H

> TASK PARAMETERS:

> SPECIAL QUEUEING:

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND:

After each background job is run, MailMan messages are generated by division to holders of the PSOAUTRF key with details of Not-Filled refills, unsuccessful runs, count of refills processed successfully, etc. For example, if the patient is marked as dead, the following message is generated.

Example: MailMan message

> Subj: <span class="mark">REDACTED</span> Internet Refills Not Processed List, \[#104161\]

> 08/10/07@09:12 11 lines

> From: POSTMASTER In 'IN' basket. Page 1 \*New\*

> ------------------------------------------------------------------

> Internet Refills Not Processed Report for the <span class="mark">REDACTED</span> Division.

> The following refill requests were not processed:

> Patient: OPPATIENT,SEVEN SSN: 0000

> Rx \#: 100002461 (REF \#1) Qty: 2

> Drug: ASPIRIN 650MG SUPPOSITORIES

> Reason: Patient Died on AUG 10, 2007

## Using the *Internet Refill Report* Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option generates a list of all Internet Refill prescriptions sorted by Patient, Date, or Result for one division or for all. This report can be printed in detail or summary format.

![](pso-7-264-fy07-qtr-04-release-notes/003.png)The report will only provide information on Internet Refills from the date the patch is installed. If the report is run to include dates prior to the patch installation no information will be included on the report for those dates.

Example: Internet Refill Report – Detailed report, sorted by patient

Select Output Reports Option: Internet Refill Report

You may select a single or multiple DIVISIONS,

or enter ^ALL to select all DIVISIONS.

DIVISION: <span class="mark">REDACTED</span> 500 <span class="mark">REDACTED</span>

ANOTHER ONE: \<Enter\>

Beginning Date: 06.27.07 (JUN 27, 2007)

Ending Date: 08.16.07 (AUG 16, 2007)

Select one of the following:

P Patient

D Date

R Result

Sort by Patient/Date/Result (P/D/R): R// Patient

Select one of the following:

D Detail

S Summary

Print Detail/Summary report (D/S): S// Detail

Do you want this report to print in 80 or 132 column format: 80// \<Enter\>

DEVICE: HOME// *\[Select Print Device\]*---------------------------------example continues---------------------------------------Example: Internet Refill Report – Detailed report, sorted by patient (continued)

INTERNET REFILL REPORT BY PATIENT - Detail AUG 16,2007 15:29:56 PAGE: 1

Not Filled - For date range JUN 27, 2007 through AUG 16, 2007 for <span class="mark">REDACTED</span>

> Patient Rx \# Date

> Reason

------------------------------------------------------------------------------

OPPATIENT,ELEVEN (0359) 100002461 08/10/07

Patient Died on AUG 10, 2007

100002461 08/21/07

Total transactions for patient = 1

OPPATIENT,NINETEEN (0000) 10064 07/26/07

Cannot refill Rx \# 10064 Rx is in DISCONTINUED status

100002419 07/20/07

Cannot refill Rx \# 100002419

100002421 08/02/07

Cannot refill Rx \# 100002421

100002422 08/03/07

Cannot refill Rx \# 100002422

Total transactions for patient = 4

OPPATIENT,FOUR (0358) 10065 07/26/07

> Cannot refill Rx \# 10065 Narcotic Drug

Total transactions for patient = 1

OPPATIENT,ONE (0285) 100002435 07/30/07

> Cannot refill Rx \# 100002435

Total transactions for patient = 1

OPPATIENT,SEVEN (0117) 100002432 07/30/07

> Cannot refill Rx \# 100002432

Total transactions for patient = 1

OPPATIENT,TWO (0270) 100002424 07/26/07

> Cannot refill Rx \# 100002424

Total transactions for patient = 1

Total transactions for date range JUN 27, 2007 through AUG 16, 2007 = 9

Press Return to continue: \<Enter\>

\*\* END OF REPORT \*\*Example: Internet Refill Report – Summary report, sorted by patient  

Select Output Reports Option: Internet Refill Report

You may select a single or multiple DIVISIONS,

or enter ^ALL to select all DIVISIONS.

DIVISION: <span class="mark">REDACTED</span> 500 <span class="mark">REDACTED</span>

ANOTHER ONE: \<Enter\>

Beginning Date: 06.27.07 (JUN 27, 2007)

Ending Date: 08.16.07 (AUG 16, 2007)

Select one of the following:

P Patient

D Date

R Result

Sort by Patient/Date/Result (P/D/R): R// Patient

Select one of the following:

D Detail

S Summary

Print Detail/Summary report (D/S): S// Summary

DEVICE: HOME// *\[Select Print Device\]*

INTERNET REFILL REPORT BY PATIENT - Summary AUG 16,2007 15:30:26 PAGE: 1

For date range JUN 27, 2007 through AUG 16, 2007 for <span class="mark">REDACTED</span>

Patient Filled Not Filled Total

------------------------------------------------------------------------------

OPPATIENT,ELEVEN (0359) 0 1 1

OPPATIENT,NINETEEN (0000) 2 4 6

OPPATIENT,FOUR (0358) 0 1 1

OPPATIENT,ONE (0285) 1 1 2

SURPATIENT,EIGHTYFIVE (0356) 1 0 1

OPPATIENT,SEVEN (0117) 0 1 1

OPPATIENT,TWO (0270) 0 1 1

COUNT: 4 9 13

Press Return to continue: \<Enter\>

\*\* END OF REPORT \*\*Example: Internet Refill Report – Detailed report, sorted by date  

> Select Output Reports Option: Internet Refill Report

> You may select a single or multiple DIVISIONS,

> or enter ^ALL to select all DIVISIONS.

> DIVISION: <span class="mark">REDACTED</span> 500 <span class="mark">REDACTED</span>

> ANOTHER ONE: \<Enter\>

> Beginning Date: 06.27.07 (JUN 27, 2007)

> Ending Date: 08.16.07 (AUG 16, 2007)

> Select one of the following:

> P Patient

> D Date

> R Result

> Sort by Patient/Date/Result (P/D/R): R// Date

> Select one of the following:

> D Detail

> S Summary

> Print Detail/Summary report (D/S): S// Detail

Do you want this report to print in 80 or 132 column format: 80// \<Enter\>

> DEVICE: HOME// *\[Select Print Device\]*

> INTERNET REFILL BY DATE - Detail AUG 16,2007@15:30 PAGE: 1

> Not Filled - For date range JUN 27, 2007 through AUG 16, 2007 for <span class="mark">REDACTED</span>

> Patient Rx \# Date

> Reason

> ------------------------------------------------------------------------------

> JUL 20, 2007

> OPPATIENT,NINETEEN (0000) 100002419

> Cannot refill Rx \# 100002419

> Count: 1

> JUL 26, 2007

> OPPATIENT,TWO (0270) 100002424

> Cannot refill Rx \# 100002424

> OPPATIENT,FOUR (0358) 10065

> Cannot refill Rx \# 10065 Narcotic Drug

> OPPATIENT,NINETEEN (0000) 10064

> Cannot refill Rx \# 10064 Rx is in DISCONTINUED status

> Count: 3

> JUL 30, 2007

> OPPATIENT,SEVEN (0117) 100002432

> Cannot refill Rx \# 100002432

> OPPATIENT,ONE (0285) 100002435

> Cannot refill Rx \# 100002435

> Count: 2

---------------------------------example continues---------------------------------------Example: Internet Refill Report – Detailed report, sorted by date (continued)  

> AUG 02, 2007

> Press Return to continue,'^' to exit: \<Enter\>

> INTERNET REFILL BY DATE - Detail AUG 16,2007@15:30 PAGE: 2

> Not Filled - For date range JUN 27, 2007 through AUG 16, 2007 for <span class="mark">REDACTED</span>

> Patient RX \# RESULT/REASON

> ------------------------------------------------------------------------------

> OPPATIENT,NINETEEN (0000) 100002421 Cannot refill Rx \# 100002421

> Cannot refill Rx \# 100002421

> Count: 1

> AUG 03, 2007

> OPPATIENT,NINETEEN (0000) 100002422 Cannot refill Rx \# 100002422

> Cannot refill Rx \# 100002422

> Count: 1

> AUG 10, 2007

> OPPATIENT,ELEVEN (0359) 100002461 Patient Died on AUG 10, 2007

> Count: 1

> Total transactions for date range JUN 27, 2007 through AUG 16, 2007 = 9

> Press Return to continue: \<Enter\>

> \*\* END OF REPORT \*\*Example: Internet Refill Report – Summary report, sorted by date

> Select Output Reports Option: Internet Refill Report

> You may select a single or multiple DIVISIONS,

> or enter ^ALL to select all DIVISIONS.

> DIVISION: <span class="mark">REDACTED</span> 500 <span class="mark">REDACTED</span>

> ANOTHER ONE:

> Beginning Date: 06.27.07 (JUN 27, 2007)

> Ending Date: 08.16.07 (AUG 16, 2007)

> Select one of the following:

> P Patient

> D Date

> R Result

> Sort by Patient/Date/Result (P/D/R): R// Date

> Select one of the following:

> D Detail

> S Summary

> Print Detail/Summary report (D/S): S// Summary

> DEVICE: HOME// *\[Select Print Device\]*

> INTERNET REFILL BY DATE - Summary AUG 16,2007@15:31 PAGE: 1

> For date range JUN 27, 2007 through AUG 16, 2007 for <span class="mark">REDACTED</span>

> Date Processed Filled Not Filled Total

> ------------------------------------------------------------------------------

> JUN 28, 2007 1 0 1

> JUL 17, 2007 1 0 1

> JUL 20, 2007 0 1 1

> JUL 23, 2007 1 0 1

> JUL 26, 2007 0 3 3

> JUL 30, 2007 0 2 2

> AUG 02, 2007 0 1 1

> AUG 03, 2007 0 1 1

> AUG 10, 2007 0 1 1

> AUG 15, 2007 1 0 1

> COUNT: 4 9 13

> Press Return to continue: \<Enter\>

> \*\* END OF REPORT \*\*Example: Internet Refill Report – Detailed report, sorted by result

> Select Output Reports Option: Internet Refill Report

> You may select a single or multiple DIVISIONS,

> or enter ^ALL to select all DIVISIONS.

> DIVISION: <span class="mark">REDACTED</span> 500 <span class="mark">REDACTED</span>

> ANOTHER ONE: \<Enter\>

> Beginning Date: 06.27.07 (JUN 27, 2007)

> Ending Date: 08.16.07 (AUG 16, 2007)

> Select one of the following:

> P Patient

> D Date

> R Result

> Sort by Patient/Date/Result (P/D/R): R// Result

> Select one of the following:

> D Detail

> S Summary

> Print Detail/Summary report (D/S): S// Detail

Do you want this report to print in 80 or 132 column format: 80// \<Enter\>

> DEVICE: HOME// *\[Select Print Device\]*

> INTERNET REFILL REPORT BY RESULT - Detail AUG 16,2007@15:31 PAGE: 1

> Not Filled - For date range JUN 27, 2007 through AUG 16, 2007 for <span class="mark">REDACTED</span>

> Patient Rx \# Date

> Reason

> ------------------------------------------------------------------------------

> OPPATIENT,SEVEN (0117) 100002432 07/30/07

> Cannot refill Rx \# 100002432

> OPPATIENT,TWO (0270) 100002424 07/26/07

> Cannot refill Rx \# 100002424

> OPPATIENT,ONE (0285) 100002435 07/30/07

> Cannot refill Rx \# 100002435

> OPPATIENT,FOUR (0358) 10065 07/26/07

> Cannot refill Rx \# 10065 Narcotic Drug

> OPPATIENT,ELEVEN (0359) 100002461 08/10/07

> Patient Died on AUG 10

---------------------------------example continues---------------------------------------Example: Internet Refill Report – Detailed report, sorted by result (continued)

> OPPATIENT,NINETEEN (0000) 10064 07/26/07

> Cannot refill Rx \# 10064 Rx is in DISCONTINUED status

> 100002419 07/20/07

> Cannot refill Rx \# 100002419

> 100002421 08/02/07

> Cannot refill Rx \# 100002421

> 100002422 08/03/07

> Cannot refill Rx \# 100002422

> Total transactions for date range JUN 27, 2007 through AUG 16, 2007 = 9

> Press Return to continue: \<Enter\>

> \*\* END OF REPORT \*\*  
Example: Internet Refill Report – Summary report, sorted by result  

> Select Output Reports Option: Internet Refill Report

> You may select a single or multiple DIVISIONS,

> or enter ^ALL to select all DIVISIONS.

> DIVISION: <span class="mark">REDACTED</span> 500 <span class="mark">REDACTED</span>

> ANOTHER ONE: \<Enter\>

> Beginning Date: 06.27.07 (JUN 27, 2007)

> Ending Date: 08.16.07 (AUG 16, 2007)

> Select one of the following:

> P Patient

> D Date

> R Result

> Sort by Patient/Date/Result (P/D/R): R// Result

> Select one of the following:

> D Detail

> S Summary

> Print Detail/Summary report (D/S): S// Summary

> DEVICE: HOME// *\[Select Print Device*

> INTERNET REFILL REPORT BY RESULT - Summary AUG 16,2007@15:31 PAGE: 1

> For date range JUN 27, 2007 through AUG 16, 2007 for <span class="mark">REDACTED</span>

> Result Count

> ------------------------------------------------------------------------------

> Filled 3

> Not Filled 9

> Total: 12

> Press Return to continue: \<Enter\>

> \*\* END OF REPORT \*\*

## Separation of Prompts for CNH and Inpatient Refills

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Barcode Batch Prescription Entry* \[PSO BATCH BARCODE\] option and the *Process Internet Refills* \[PSO INTERNET REFILLS\] option now prompt separately for inpatient and CNH refills:

Example: Barcode Batch Prescription Entry – Separation of prompts for refills

Select Barcode Rx Menu Option: Barcode Batch Prescription Entry

Select one of the following:

1 REFILLS

2 RENEWS

Batch Barcode for: REFILLS// 1 REFILLS

Please answer the following for this session of prescriptions

FILL DATE: (2/14/2007 - 12/31/2699): TODAY// \<Enter\> (AUG 13, 2007)

MAIL/WINDOW: MAIL// \<Enter\> MAIL

Will these refills be Queued or Suspended ? S// \<Enter\> USPENDED

Allow refills for inpatient ? N// \<Enter\> O

Allow refills for CNH ? N// \<Enter\> O

WAND BARCODE: *\[Scan barcode\]*Example: Process Internet Refills – Separation of prompts

Select Barcode Rx Menu Option: Process Internet Refills

Division: <span class="mark">REDACTED</span>

Please answer the following for this session of prescriptions

FILL DATE: (2/14/2007 - 12/31/2699): TODAY// \<Enter\> (AUG 13, 2007)

MAIL/WINDOW: MAIL// \<Enter\> MAIL

Will these refills be Queued or Suspended ? S// \<Enter\> USPENDED

Allow refills for inpatient ? N// \<Enter\> O

Allow refills for CNH ? N//\<Enter\> O

Process internet refill requests at this time? YES//

# Local Mailouts with Foreign Addresses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software is updated to replace a patient’s address on the label with the annotation ‘\*\*\* FOREIGN ADDRESS \*\*\*’ when the patient’s mailing address is foreign (outside the United States as designated by the DG Country Code field, available with the release of DG\*5.3\*688).

# Suspense Functions Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The suspense functions are updated to add a new option and a new hidden action for suspending mail-routed drugs for CMOP

These updates are described in further detail in the following sections.

## Using the *Queue CMOP Prescription* Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSO QUEUE CMOP\]

The new *Queue CMOP Prescription* \[PSO RX QUEUE CMOP\] option allows the users (including pharmacy technicians) to put mail-routed prescription(s) for CMOP drugs on suspense for CMOP. This option has been added to the *Suspense Functions* \[PSO PND\] menu, *Pharmacist Menu* \[PSO USER1\] and the *Pharmacy Technician’s Menu* \[PSO USER2\].

Example: Queue CMOP Prescription

Select Suspense Functions Option: QUEUE CMOP Prescription

Enter the Rx \# to queue to CMOP: 300486

If the prescription does not have a routing of mail, has already been released, or is not for a CMOP drug, and does not pass all the other normal checks for CMOP it will not be put on suspense for CMOP.

### Hidden Action Updates to the Medication Profile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users may also manually queue prescriptions to CMOP using a new hidden action, CM, while in the patient’s medication profile.

Example: Manually queue to CMOP – Hidden action

Medication Profile May 22, 2007 10:44:56 Page: 1 of 1

OPPATIENT16,ONE

PID: 000-24-6802 Ht(cm): 177.80 (02/08/2004)

DOB: APR 3,1941 (66) Wt(kg): 90.45 (02/08/2004)

AGE: 60 Non-VA Meds on File

Last entry on 01/13/03

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

------------------------------------ACTIVE----------------------------------

1 503902 ACETAMINOPHEN 500MG TAB 60 A\> 05-22 05-22 3 30

2 503886\$ DIGOXIN (LANOXIN) 0.2MG CAP 60 A\> 05-07 05-07 5 30

------------------------------------PENDING------------------------------------

3 AMPICILLIN 250MG CAP QTY: 40 ISDT: 05-29 REF: 0

------------------------NON-VA MEDS (Not dispensed by VA)-----------------------

GINKO EXT 1 TAB ONCE A DAY BY MOUTH Date Documented: 01/13/03

IBUPROFPEN 50MG TAB Date Documented: 12/10/02

TERFENADINE TAB 200 MILIGRAMS

MIX ½ CUP PDR & 6 OZ WATER & DRINK 1 MIXED CUP

Date Documented: 03/17/02

Enter ?? for more actions

PU Patient Record Update NO New Order

PI Patient Information SO Select Order

Select Action: Quit// CM

Select Orders by number: (1-3): 2

# Clozapine Processing Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software has been updated to include checks for a DEA or VA number, as well as assignment of the YSCL AUTHORIZED key.

When an order is placed, the system checks for the provider’s DEA number or VA number first. If the provider does not have either, the following warning displays:

> Provider must have a DEA# or VA# to write prescriptions for clozapine

If the provider has either the DEA number or the VA number, then the software checks for the assignment of the YSCL AUTHORIZED key. If the provider has a DEA or VA number, but does not hold the YSCL AUTHORIZED key, the following warning displays:

> Provider must hold YSCL AUTHORIZED key to write prescriptions for clozapine

![](pso-7-264-fy07-qtr-04-release-notes/004.png)

This functionality will also be included in the Computerized Patient Record System (CPRS) Graphical User Interface (GUI) v. 27 release.

*  
(This page included for two-sided copying.)*

# View Provider Option Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *View Provider* \[PSO PROVIDER INQUIRE\] option is updated to include the NPI# of the provider.

> Select Supervisor Functions Option: VIEW Provider

> Select Provider: OPPROVIDER,THREE OPPROVIDER,THREE TO PROVIDER

> Name: OPPROVIDER,THREE

> Initials: TO

> NON-VA Prescriber: No Tax ID:

> Exclusionary Check Performed: Date Exclusionary List Checked:

> On Exclusionary List:

> Exclusionary Checked By:

> Authorized to Write Orders: Yes

> Requires Cosigner: No DEA#

> Class: VA#

> Type: Unknown NPI#

> Remarks:

> Synonym(s): TO

> Service/Section: PHARMACY

> Select Provider:

*(This page included for two-sided copying.)*

# Patient Information Screen Updates (HD187273)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Patient Information screen contains the following updates:

- The patient’s RX PATIENT STATUS is displayed on the Patient Information screen, below the patient’s Eligibility.
- The “PHONE” field display is changed to “HOME PHONE”, and “CELL PHONE” and “WORK PHONE” are new additions. These can be maintained via the PATIENT UPDATE (PU) action and the *Update Patient Record* \[PSO PAT\] option.

Example: Patient Information Screen Updates

Patient Information Nov 04, 2005@09:19:26 Page: 1 of 1

OPPATIENT,FOUR \<A\>

PID: 000-01-1322P Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: JAN 13,1922 (83) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

Eligibility: NSC, VA PENSION

RX PATIENT STATUS: PENSION NSC

Disabilities:

123 ANY STREET HOME PHONE:

BIRMINGHAM CELL PHONE:

ALABAMA WORK PHONE:

Prescription Mail Delivery: Regular Mail

Allergies:

Remote: No remote data available

Adverse Reactions:

Enter ?? for more actions

EA Enter/Edit Allergy/ADR Data PU Patient Record Update

DD Detailed Allergy/ADR List EX Exit Patient List

Select Action: Quit//

*(This page included for two-sided copying.)*

# Report Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following reports are updated in PSO\*7\*264:

- Log of Suspended Rx's by Day (this Division)
- Bad Address Suspended List

These changes are further described in the following sections.

## Log of Suspended Rx's by Day (this Division) Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Log of Suspended Rx's by Day (this Division)* \[PSO PNDLOG\] option is updated to add a new column showing the B/D/F (Bad Address Indicator/ Do Not Mail/ Foreign Address) status of the prescription.

> Select Suspense Functions Option: LOG of Suspended Rx's by Day (this Division)

> Sort by Patient Name or SSN: (P/S): PATIENT NAME// \<Enter\>

> Start Date: 08.10.07 (AUG 10, 2007)

> End Date: 08.14.07 (AUG 14, 2007)

> Do you want to see only those Rx's that have NOT yet been printed? Y// \<Enter\> ES

> You are logged in under the <span class="mark">REDACTED</span> division.

> Print only those Rx's suspended for this division? Yes// \<Enter\> YES

> Do you want this report to print in 80 or 132 column format: 132// 80

> DEVICE: HOME// *\[Select Print Device\]*

> RX SUSPENSE LIST FOR AUG 10, 2007 PAGE: 1

> RX \# DRUG MW PRNT B/D/F

> ------------------------------------------------------------------------------

> Patient Name: OPPATIENT,ONE

> 100002422 PENICILLAMINE 250MG TAB M NO D

> RX SUSPENSE LIST FOR AUG 13, 2007 PAGE: 2

> RX \# DRUG MW PRNT B/D/F

> ------------------------------------------------------------------------------

> Patient Name: OPPATIENT,SEVEN

> 100002423 TERFENADINE 60MG TAB M NO B

> RX SUSPENSE LIST FOR AUG 14, 2007 PAGE: 3

> RX \# DRUG MW PRNT B/D/F

> ------------------------------------------------------------------------------

> Patient Name: OPPATIENT,FOUR

> 100002421 ACETAMINOPHEN 325MG C.T. M NO

> NOTE: B=BAD ADDRESS INDICATOR D=NO NOT MAIL F=FOREIGN ADDRESS

> \*\* END OF REPORT \*\*

## Bad Address Suspended List Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Bad Address Suspended List* \[PSO BAI SUSPENDED\] option adds prompting for Do Not Mail and Foreign addresses for the unprinted suspended prescriptions report.

Example: Bad Address Suspended List Report – new prompting

> Select Output Reports Option: Bad Address Reporting Main Menu

> Select Bad Address Reporting Main Menu Option: Bad Address Suspended List

> This option shows unprinted suspended prescriptions for the following:

> \- BAD ADDRESS INDICATOR set in the PATIENT file (#2) and no active temporary address

> \- DO NOT MAIL set in the PHARMACY PATIENT file (#55)

> \- FOREIGN ADDRESS set in the PATIENT file (#2) and no active US temporary address

> Select one of the following:

> B Bad Address Indicator

> D Do Not Mail

> F Foreign

> A All

> Print for Bad Address Indicator/Do Not Mail/Foreign/All (B/D/F/A): A// \<Enter\> All

> Ending suspense date: 08.15.07 (AUG 15, 2007)

> You are logged in under the <span class="mark">REDACTED</span> division.

> Print only those Rx's suspended for this division? Yes// \<Enter\> YES

> DEVICE: HOME// *\[Select Print Device\]*

> Suspense BAI/DO NOT MAIL/FOREIGN ADRESS report - division = <span class="mark">REDACTED</span> PAGE: 1

> for suspense dates through AUG 15, 2007 B/D/F

> -----------------------------------------------------------------------------

> OPPATIENT,NINETYFIVE (00-6666)

> AUG 13, 2007 Rx#: 100002466 AMOXICILLIN 250MG CAP D

> OPPATIENT,SEVEN (00-0175)

> JUL 02, 2007 Rx#: 100002097 PLACEBO TAB B

> NOTE: B=BAD ADDRESS INDICATOR D=NO NOT MAIL F=FOREIGN ADDRESS

> End of Report.

> Press Return to continue:

<span id="_Toc179943425" class="anchor"></span>

# Consolidated Mail Outpatient Pharmacy (CMOP) V. 2.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FY07 Q4 release also includes the following change to functionality in the CMOP package, in the PSX\*2\*58 patch:

- This patch checks for the BAD ADDRESS INDICATOR field (#.121) of the PATIENT file (#2) being set or for the patient having a foreign address when queuing transactions to CMOP. If either condition is met, the associated orders are not sent to CMOP.

*(This page included for two-sided copying.)*