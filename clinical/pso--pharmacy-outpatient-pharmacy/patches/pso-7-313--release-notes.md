---
title: PSO*7*313 Titration/Maintenance Rx Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Titration/Maintenance Rx
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*313
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - titration
  - table
  - maintenance
  - contents
  - prescription
  - order
  - dose
  - patient
  - complex
  - duration
page_count: 0
word_count: 2197
section_count: 16
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p313_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p313_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-313-titration-maintenance-rx-release-notes/001.png)

Titration/Maintenance RxPatch PSO\*7\*313Release Notes

August 2014

Product Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Enhancements](#enhancements)
    - [Complex Orders Duration Field](#complex-orders-duration-field)
    - [Titration/Maintenance Rx](#titrationmaintenance-rx)
  - [New Files and Fields](#new-files-and-fields)
  - [New Protocols](#new-protocols)
  - [New Routines](#new-routines)
  - [Patient Safety Issues](#patient-safety-issues)
  - [Remedy Tickets](#remedy-tickets)
  - [Forms](#forms)
  - [New Service Requests (NSRs)](#new-service-requests-nsrs)
  - [Mail Group](#mail-group)
  - [Options](#options)
  - [Security Keys](#security-keys)
  - [New Templates](#new-templates)
  - [# Additional Information](#additional-information)
  - [Documentation](#documentation)
Outpatient Pharmacy Patch PSO\*7\*313 has been created to address two enhancements to the Outpatient Pharmacy (OP) application. These enhancements are detailed in the following sections.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release notes document provides a brief description of the new features and functions of the Complex Orders Duration Field and Titration/Maintenance Rx enhancements. More detailed information on the functionality can be found in the application user and technical manuals found on the Virtual Documentation Library (VDL).

## Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy Patch PSO\*7\*313 addresses two enhancements to the Outpatient Pharmacy (OP) application:

- Complex Orders Duration Field – this is in relation to Patient Safety Issue PSI-07-167 and Remedy Ticket \# 203088.
- Titration/Maintenance Rx - modified to accommodate Titration/Maintenance prescription functionality.

### Complex Orders Duration Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Enhancement is related to Patient Safety Issue PSI-07-167 and Remedy Ticket \# 203088.

The Outpatient Pharmacy application currently allows the entry of a complex order, which contains a "THEN" conjunction. This type of order is allowed to leave the Duration field preceding the "THEN" conjunction as null. This null duration field is causing issues when the Outpatient Pharmacy order was being transferred to an Inpatient Medication Order(s).

The default stop dates were for thirty (30) days for the two (2) new inpatient orders created, and the Start/Stop dates in the sequence were incorrect. The pharmacist did not notice the incorrect dates and finished off the orders. Upon transfer of a complex order from Outpatient Pharmacy to Inpatient Medication order(s), the resulting order will start at the first step rather than continue at the step the patient was at as an Outpatient. It looks like a new complex order to the finishing pharmacist

since the Start date is populated with the date of finishing so that the patient would be started on the first step, which may not be correct. This would pertain to complex orders that taper or titrate doses up or

down and potentially impacts patients by receiving too much or too little medication.

The Outpatient Pharmacy application is being modified by patch PSO\*7\*313 to require the entry of a duration for a dose preceding a THEN conjunction if the schedule for such dose is not a ONE-TIME type schedule. If the dose preceding the THEN conjunction is a ONE-TIME type schedule, the software will continue to allow the Duration field to be left blank (optional). The corresponding change to CPRS will be done in a future CPRS patch.

The following is an example of an acceptable SIG ('NOW' is ONE-TIME type schedule):

--------------------------------------------------------------

TAKE ONE TABLET BY MOUTH NOW THEN TAKE TWO TABLETS EVERY 8 HOURS

No longer acceptable SIG ('Q4H' is not ONE-TIME type schedule):

--------------------------------------------------------------

TAKE ONE TABLET BY MOUTH EVERY 4 HOURS THEN TAKE TWO TABLETS EVERY 8 HOURS

> **NOTE:** The SIG above is not acceptable because it does not have Duration for the first dose. In order to be acceptable, the SIG above would have to have duration as follows:

TAKE ONE TABLET BY MOUTH EVERY 4 HOURS FOR 3 DAYS THEN TAKE TWO

TABLETS EVERY 8 HOURS

The Duration field is not required for the dose following the last "THEN"conjunction.

The following is an example of a complex order being entered via Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\].

: :

VERB: APPLY

ROUTE: PO// PO ORAL

Schedule: QD (EVERY DAY)

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

CONJUNCTION: THEN

Duration field required for the dosage entered prior to this THEN conjunction.

LIMITED DURATION (IN DAYS, HOURS OR MINUTES):

: :

### Titration/Maintenance Rx

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Enhancement is related to PSI-06-176 and Remedy Ticket \#168928.

The Outpatient Pharmacy (OP) application was modified to accommodate Titration/Maintenance prescription functionality. The existing software presented patient safety risks when prescriptions dispensed with a titrating dose followed by a maintenance dose were being copied, renewed, or refilled.

The issue was that refills, as well as the new prescriptions (derived from copy,

Renewals, or edits), automatically carried over the initial titrating dose into the new fill/prescription, which was not always the user's intention.

The new functionality provides two steps for processing Titration/ Maintenance prescriptions.

First, the user will have the ability to mark prescriptions as 'Titration to Maintenance' when finishing prescriptions from CPRS as well as via the Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option by invoking the new hidden action 'TM' - Mark Rx as Titration. This action will result in preventing the following actions to be taken on the prescription: Refill, Renewal (including

via CPRS), Copy and editing of any field that requires a new Rx to be created. This action will also set the new field TITRATION RX FLAG (#45.3) in the PRESCRIPTION File (#52) as well as the new field

TITRATION DOSE RX (#45.1) in the PRESCRIPTION File (#52). Prescriptions that are marked as Titration/Maintenance will have the letter 't' postfix to the RX \# as seen below:

: : :

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------ACTIVE-------------------------------

1 100005024t AMOXAPINE 50MG TAB 30 S 09-26 09-26 2 30

2 100005022 AMOXICILLIN 250MG CAP 30 A 08-18 08-18 11 30

3 100005035 KALETRA 3 A 09-29 09-29 0 3

: : :

> **NOTE:** A prescription can be unmarked as Titration/Maintenance by

invoking the same TM action on an already marked prescription.

There is also a hidden action, TR (Convert Titration Rx), in the Patient Prescription Processing \[PSO LM BACKDOOR TITRATION RX REFILL\] option. This action populates the MAINTENANCE DOSE RX (#45.2) field in the PRESCRIPTION File (#52). When a titration to maintenance prescription needs to be refilled so the patient can continue on the Maintenance Dose, this option allows the users to create a new prescription with the maintenance dose only. This process works similar to copying an existing prescription; however, it can only be used on prescriptions with the following characteristics:

\- Rx is a complex order with a THEN conjunction

\- Rx is released

\- Rx status is ACTIVE

\- Rx does not have refills previously ordered

\- Rx \# Of Refills is greater than 0 (zero)

Before the new Maintenance Rx can be accepted, the user is prompted to validate the QTY field for the new Rx, which may or may not be automatically re-calculated. Only the last dose from the original

prescription is carried over to the new Maintenance Rx, and the \# of Refills field is decreased by 1 because the new Maintenance Rx counts as a fill.

Once a user verifies the information for the Maintenance Rx is accurate, they can accept the Maintenance Rx. This action triggers a Duplicate Drug check against the original complex order, which must be discontinued before the new Maintenance Rx can be accepted. After the new Maintenance Rx is accepted, it will have the new indicator 'm' on the right side of the Rx \# in the patient's Medication Profile.

: : :

ISSUE LAST REF DAY

\# RX \# DRUG QTY ST DATE FILL REM SUP

-------------------------------ACTIVE-------------------------------

1 100005436m AMOXAPINE 50MG TAB 30 S 09-26 09-26 1 30

2 100005022 AMOXICILLIN 250MG CAP 30 A 08-18 08-18 11 30

3 100005035 KALETRA 3 A 09-29 09-29 0 3

: : :

The new Titration/Maintenance indicator (t/m) will be included in the following menu options where the prescription number is displayed:

View Prescriptions \[PSO VIEW\]

Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]

Complete Orders from OERR \[PSO LMOE FINISH\]

ePharmacy Medication Profile (View Only) \[PSO PMP\]

Medication Profile \[PSO P\]

External refill requests, such as from AudioFax and Internet, will not be processed for Titration/Maintenance marked prescriptions.

Subj: ALBANY External Application Refills: Not processed List \[#101509\]

01/28/09@13:52 11 lines

From: POSTMASTER In 'IN' basket. Page 1

-------------------------------------------------------------------------

Refills Not Processed Report for the ALBANY Division.

The following refill requests were not processed:

Patient: OPPATIENT,TWO (9999)

Rx \#: 100005122 (REF \#1) Qty: 55

Drug: ZINC SULFATE 66MG TAB

Reason: 'Titration/Maintenance Rx' cannot be refilled.

CPRS refill requests will not be automatically processed for Titration/Maintenance marked prescriptions. The refill request will remain in the patient's Medication Profile as PENDING, and a mailman message (as shown in the above example) will also be sent to PSOAUTRF security key holders.

The activity logs for both Titration and Maintenance Rx's will record the corresponding Titration and Maintenance Rx \# if they exist as seen in the following:

Titration Rx:

------------

\# Date Reason Rx Ref Initiator of Activity

======================================================================

1 09/29/08 EDIT ORIGINAL OPUSER,ONE Comments: Maintenance

Dose Rx: 100005130

Maintenance Rx:

--------------

\# Date Reason Rx Ref Initiator of Activity

======================================================================

1 09/29/08 EDIT ORIGINAL OPUSER,TWO Comments: Titration

Dose Rx: 100005392

The VistA Integration Control Registration (ICR) \#2398 provided to Computerized Patient Record System V. 1.0 (CPRS) was modified to prevent the renewal of a Titration dose order with the following message:

"Prescription was marked as Titration to Maintenance Dose by Pharmacy

and cannot be renewed. To repeat the titration, enter a new prescription

or copy the prior titration order. To continue the maintenance dose, refill

this prescription if refills are available or enter a new prescription for

the maintenance dose."

When using the Barcode Batch Prescription Entry option \[PSO BATCH BARCODE\], if the prescription has been marked as a Titration/Maintenance Rx, and the user attempts to renew or refill the prescription, the following message will display:

For a renewal:

"Rx# XXXXXX is marked as Titration Rx and cannot be renewed."

For a refill:

"Rx# XXXXXX is marked as Titration Rx and cannot be refilled."

The PSO HIDDEN ACTIONS Protocol in the PROTOCOL File (#101) will be modified to include the two new Hidden Actions introduced by this enhancement. PSO LM BACKDOOR MARK AS TITRATION and PSO LM BACKDOOR TITRATION RX REFILL are both new protocols added to the PROTOCOL File (#101).

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* IMPORTANT \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

The enhancements related to Titration/Maintenance dose Rx are made only

for Outpatient Pharmacy package. The corresponding changes to CPRS package

are not included at this time. Therefore, the CPRS Order Copy and Order

Change functionalities will continue to function as is. Furthermore, there

will be no indication of a Titration/Maintenance order in the CPRS

application.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

## New Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Name          | Field Name                  | New/Modified/Deleted |
|--------------------|-----------------------------|----------------------|
| PRESCRIPTION (#52) |                             | New                  |
|                    | TITRATION DOSE RX (#45.1)   | New                  |
|                    | MAINTENANCE DOSE RX (#45.2) | New                  |
|                    | TITRATION RX FLAG (#45.3)   | New                  |

## New Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Protocol Name                       | New/Modified/Deleted | Action                      |
|-------------------------------------|----------------------|-----------------------------|
| PSO HIDDEN ACTIONS                  | Modified             | Use as a link for Menu/Item |
| PSO LM BACKDOOR MARK AS TITRATION   | New                  | Send to site                |
| PSO LM BACKDOOR TITRATION RX REFILL | New                  | Send to site                |

## New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- PSOOTMRX

## Patient Safety Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- PSI-07-167 PSI-06-176

## Remedy Tickets

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Remedy Ticket</strong></th>
<th><strong>Overview</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>203088</td>
<td>Outpt complex order (using then) was transferred to Inpt, and start/stop dates are one month apart.</td>
</tr>
<tr class="even">
<td>168928</td>
<td>Means of allowing two (2) active RXs for same dispense drug needed to accommodate titration regimens.</td>
</tr>
<tr class="odd">
<td>1022059</td>
<td><p>Duplicate prescriptions created. Patch PSO*7*313 fixes an issue that could create duplicate prescriptions on a patient profile.</p>
<p>When a complex order is copied and the duration field is edited, upon accepting the order, the message to discontinue the original order is not triggered. This causes duplicate prescriptions to appear on the patient profile.</p>
<p>Patch PSO*7*313 corrects this problem by prompting the user to discontinue the original order.</p></td>
</tr>
</tbody>
</table>

## Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No forms have been added or modified by PSO\*7\*313.

## New Service Requests (NSRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No service requests (NSR) have been added or modified by PSO\*7\*313.

## Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No mail groups have been added or modified by PSO\*7\*313.

## Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No options have been added or modified by PSO\*7\*313.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No security keys have been added or modified by PSO\*7\*313.

## New Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No templates have been added or modified by PSO\*7\*313.

*(This page included for two-sided copying.)*

## # Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ICR \#2398 was modified to prevent the renewal of a Titration dose order with the following message:

"Prescription was marked as Titration to Maintenance Dose  by Pharmacy and cannot be renewed. To repeat the titration, enter a new prescription or copy the prior titration order. To continue the maintenance dose, refill  this prescription if refills are available or enter a new prescription for the maintenance dose."

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this patch is available.

The preferred method is to FTP the files from <ftp://download.vista.med.va.gov/>

This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

| Albany         | ftp.fo-albany.med.va.gov | \<ftp://ftp.fo-albany.med.va.gov\> |
|----------------|--------------------------|------------------------------------|
| Hines          | ftp.fo-hines.med.va.gov  | \<ftp://ftp.fo-hines.med.va.gov\>  |
| Salt Lake City | ftp.fo-slc.med.va.gov    | \<ftp://ftp.fo-slc.med.va.gov\>    |

The documentation will be in the form of Adobe Acrobat files (PDFs).

| File Description                                           | File Name               | FTP Mode |
|------------------------------------------------------------|-------------------------|----------|
| Outpatient Pharmacy V. 7.0 Manager's User Manual           | PSO_7_MAN_UM_R0814.PDF  | Binary   |
| Outpatient Pharmacy V. 7.0 Pharmacist’s User Manual        | PSO_7_PHAR_UM_R0814.PDF | Binary   |
| Outpatient Pharmacy V. 7.0 Technician's User Manual        | PSO_7_TECH_UM_R0814.PDF | Binary   |
| Outpatient Pharmacy V. 7.0 Technical Manual/Security Guide | PSO_7_TM_R0814.PDF      | Binary   |
| Release Notes for Titration/Maintenance Rx                 | PSO_7_P313_RN.PDF       | Binary   |

Documentation can also be retrieved from the VA Software Documentation Library (VDL) on the Internet at the following address:

<http://www4.va.gov/vdl>