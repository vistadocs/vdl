---
consolidated_title: "user manual change pages"
app_code: PSX
doc_type: UM
master_source: "PSX*2*74 User Manual Change Pages"
master_pub_date: November 2013
consolidated_from: 4 versions
prior_versions:
  - "PSX*2*65 User Manual Change Pages"
  - "PSX*2*68 User Manual Change Pages"
  - "PSX*2*76 User Manual Change Pages"
---

Department of Veterans AffairsCONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP)

USER MANUAL

![](psx-2-74-user-manual-change-pages/001.png)

Version 2.0PSX\*2\*2\*74(November 2013)Office of Information and Technology (OIT)Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
    - [Released and Unreleased Prescription Report](#released-and-unreleased-prescription-report)
  - [Rx (Prescriptions)](#rx-prescriptions)
    - [Barcode Rx Menu](#barcode-rx-menu)
    - [Cancel Prescriptions](#cancel-prescriptions)
    - [### ### TRADENAME – Currently able to be edited at each fill level.](#tradename-currently-able-to-be-edited-at-each-fill-level)
    - [### Hold Features](#hold-features)
    - [Delete a Prescription](#delete-a-prescription)
  - [Suspense Functions](#suspense-functions)
    - [Change Suspense Date](#change-suspense-date)
    - [Delete From Suspense File](#delete-from-suspense-file)
    - [Print From Suspense File](#print-from-suspense-file)
  - [Third Party Electronic Claims Submission of CMOP Prescriptions](#third-party-electronic-claims-submission-of-cmop-prescriptions)
Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All”, replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 21%" />
<col style="width: 15%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2013</td>
<td><p>Throughout (minor nonsubstantive changes).</p>
<p>iii, 26, 27, 28, 31, 32, 34, 35, 43, 44, 45, 46, 47, 51, 129a, 130</p></td>
<td>PSX*2*74</td>
<td><p>Electronic Data Interchange (EDI) New Standards and Operating Rules – VHA Provider-side Technical Compliance Requirements TAC-12-03366 Project.</p>
<p>Cosmetic changes (standardized fonts). Changed all references from version 6 to version 7 (including iii, Preface) and standardized wording for blank pages (without using change pages).</p>
<p>Edited Revision History, p. 47 verbiage. Updated p.50 to add patch-specific functionality. Added 129a, 129b to include conditions under which the prescription will rejected.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>11/2009</td>
<td>137a-b</td>
<td>PSX*2*68</td>
<td><p>Alerts for a discontinued CMOP prescription</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>07/2009</td>
<td>i-ii, 50a-50b</td>
<td>PSX*2*65</td>
<td><p>ePharmacy Iteration II – Phase 4 project:</p>
<p>Updated revision history, ¾ days supply functionality, and host error functionality.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/2006</td>
<td><p>v-viii,</p>
<p>30, 41-42, 46-50,</p>
<p>50a-b, 126, 137</p></td>
<td>PSX*2*48</td>
<td><p>HIPAA NCPDP Global Project:</p>
<p>Updated Table of Contents;</p>
<p>Updated “Functionality for Returning Med to Stock” verbiage;</p>
<p>Updated View Prescriptions Example to include ECME Activity and Reject Logs; Updated Print from Suspense options and reflowed text onto following pages;</p>
<p>Added Third Party Electronic Claims Submission of CMOP Prescriptions;</p>
<p>Added ECME transmission to the Flow Chart for Processing a CMOP Transmission in Appendix D;</p>
<p>Added example of an “e-Pharmacy CMOP Not Transmitted Rx List Message” to Appendix E.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>10/2003</td>
<td>24, 24a</td>
<td>PSX*2*41</td>
<td>Updated example for scheduling of auto-transmissions.</td>
</tr>
<tr class="even">
<td>09/2002</td>
<td><p>Title Page;</p>
<p>i-(ii);</p>
<p>65-66.</p></td>
<td>PSX*2*34</td>
<td><p>Updated Title Page and Revision History; modified description of Unreleased Rx’s Report to include new sort and print options.</p>
<p>Formatting change unrelated to the patch: Header for example of Rejected Messages Report moved to same page as body of report.</p></td>
</tr>
<tr class="odd">
<td>05/2002</td>
<td><p>Title Page;</p>
<p>i-viii;</p>
<p>(61)-62;</p>
<p>67-(68).</p></td>
<td>PSX*2*32</td>
<td><p>Updated Title page; added Revision History page and renumbered Preface and Table of Contents pages; added new CMOP DRUG Cost Missing report; and amended Facility Activity Report description to add time range.</p>
<p>Screen captures on updated pages re-formatted to new standards.</p></td>
</tr>
<tr class="even">
<td>12/1997</td>
<td></td>
<td></td>
<td>Original Released User Manual.</td>
</tr>
</tbody>
</table>
Preface
> Version 2.0 of Consolidated Mail Outpatient Pharmacy (CMOP) software processes and automatically transmits prescription data from a Veterans Affairs Medical Center to a CMOP host facility. The CMOP host facility then mails prescriptions from an integrated and highly automated outpatient prescription dispensing system. This CMOP user manual is intended for pharmacists and pharmacy technicians who are familiar with the functionality of Outpatient Pharmacy Version 7.0.
*(This page included for two-sided copying.)*
Table of Contents
*(This page included for two-sided copying.)*
> The following menu contains the options for the outpatient pharmacy manager.
> *Archiving ...*
> *Autocancel Rx’s on Admission*
> *Bingo Board ...*
> *Clozapine Pharmacy Manager ...*
> *Copay Menu ...*
> *\*† Drug Enter/Edit*
> *Drug Interactions Menu ...*
> *DUE Supervisor ...*
> *Label/Profile Monitor Reprint*
> *\* Maintenance (Outpatient Pharmacy) ...*
> *Medication Profile*
> *\* Output Reports ...*
> *Pharmacy Intervention Menu ...*
> *\* Release Medication*
> *\* Return Medication to Stock*
> *\* Rx (Prescriptions) ...*
> *\* Supervisor Functions ...*
> *\* Suspense Functions ...*
> \Update Patient Record*
> *Verification ...*
> \*These options from the Outpatient Pharmacy V. 7.0 package have been modified or contain suboptions which have been modified for CMOP.
> †This option has been modified for CMOP and can be found on the *OutpatientPharmacy Manager* menu, the *Maintenance (Outpatient Pharmacy)* menu, and the *Supervisor Functions* menu of Outpatient Pharmacy V. 7.0.
> Drug Enter/Edit
> By using the *Drug Enter/Edit* option the pharmacy supervisor can add new drugs to the file, edit existing drugs, and inactivate drugs. This option can be found on the *OutpatientPharmacy Manager* menu, the *Maintenance(Outpatient Pharmacy)* menu, and the *Supervisor Functions* menu of Outpatient Pharmacy V. 7.0.
*CMOP Functionality for the Drug Enter/Edit Option*
> When an entry in the DRUG file (#50) has been marked for CMOP, the GENERIC NAME and DISPENSE UNIT fields cannot be edited. If editing of these fields is necessary, the entry must be unmarked for CMOP using the *CMOP Mark/Unmark(Single drug)* option. Once editing is completed, the drug must be re-marked for CMOP using the *CMOP Mark*/*Unmark(Single drug)* option.
> The QUANTITY DISPENSE MESSAGE field does not display in the Outpatient Pharmacy *Drug Enter/Edit* option. It is recommended that the user enter or edit drugs through the *CMOP Drug/Item Management* menu.
Output Reports
> The *Output Reports* menu generates a variety of management reports. These reports contain current medication profiles, utilization, cost, and workload information which help management maintain the highest level of patient care.
> *Action Profile (132 COLUMN PRINTOUT)*
> *Alpha Drug List and Synonyms*
> *AMIS Report*
> *Commonly Dispensed Drugs*
> *Cost Analysis Reports ...*
> *Daily AMIS Report*
> *Drug List By Synonym*
> *Inactive Drug List*
> *Management Reports Menu ...*
> *Monthly Drug Cost*
> *Narcotic Prescription List*
> *Non-Formulary List*
> *Poly Pharmacy Report*
> *\* Released and Unreleased Prescription Report*
> \*This option from Outpatient Pharmacy V. 7.0 has been modified for CMOP.

### Released and Unreleased Prescription Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates a report of released and unreleased or only unreleased prescriptions by date range. The default start date is T-30. If the package was installed less than 30 days ago, the default date will be the date the package was installed. The end date default will be the current date.
*CMOP Functionality for Released and Unreleased Prescription Report*
> This option has been modified by adding a column to indicate if the prescription is a CMOP prescription and a column to indicate the CMOP status.

## Rx (Prescriptions)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Rx (Prescriptions)* menu allows the pharmacist to manipulate information that pertains to prescriptions. When a screen profile is displayed for any of the following options the letter (R) will appear next to the last fill date for any prescriptions that have been returned to stock.

> The options in this menu are listed below.

> *\* Barcode Rx Menu ...*

> *\* Barcode Batch Prescription Entry*

> *Check Quality of Barcode*

> *\* Cancel Prescription*

> *\* Edit Prescriptions*

> *Hold Features ...*

> *\* Hold Rx*

> *List Prescriptions on Hold*

> *\* Unhold Rx*

> *List One Patient’s* Arc*hived Rx’s*

> *\* New Prescription Entry*

> *\* Partial Prescription*

> *\* Refill Prescriptions*

> *\* Reprint an Outpatient Label*

> *\* View Prescriptions*

> \*These options or suboptions from Outpatient Pharmacy V. 7.0 have been modified for CMOP.

### Barcode Rx Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This *Barcode Rx Menu* contains options that allow batch barcoding for refills and renewals of prescriptions and an option to check the quality of the barcode print.

> *\* Barcode Batch Prescription Entry*

> *Check Quality of Barcode*

> \*This option has been modified for CMOP and can be found under the *Barcode Rx Menu* on the *Rx (Prescriptions)* menu of Outpatient Pharmacy V. 7.0.

#### Barcode Batch Prescription Entry

> This option is used to enter refills or renewals using barcodes in a batch entry.

> *CMOP Functionality for Barcode Batch Prescription Entry*

> Prescriptions entered using this option will be screened and suspended for CMOP transmission if all the CMOP criteria are met.

### Cancel Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Cancel Prescription* option allows the pharmacist to either discontinue a prescription without deleting its records from the files, or reinstate a cancelled prescription. A cancelled prescription remains on the patient profile and an entry in the activity log for the cancellation is made. The cancelled prescription will carry a status of Cancelled or C and cannot be refilled or reprinted.

> The label can be entered or wanded if you are cancelling or reinstating the prescription by the prescription number or the patient name.

*CMOP Functionality for Cancel Prescription*

> CMOP functionality for *Cancel Prescription* is the same as Outpatient Pharmacy V. 7.0. for all Rx’s. Reinstate screens all Rx’s for the CMOP criteria. If the Rx meets the criteria it is suspended for CMOP transmission and a message is displayed indicating the suspense date. If the fill date of a CMOP Rx is in the past, the prescription is reinstated, but not suspended for transmission. If the fill date is today or in the future, the CMOP Rx is suspended for CMOP processing for that date.

### ### ### TRADENAME – Currently able to be edited at each fill level.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A CMOP Rx entered with a tradename will not be sent to CMOP:

  If deleting a tradename and the last fill is in suspense, change the entry to “Queued for Transmission” to the CMOP.

  *View Prescriptions* will look odd, but the CMOP group stated this was acceptable.

  CRITERIA FOR EDITING OTHER FIELDS -
- If Rx released, no editing of

  ISSUE DATE

  FILL DATE
- If fill being edited has been transmitted, no editing of

  QUANTITY

  DAYS SUPPLY

  \# OF REFILLS
- The following fields may be edited:

  PATIENT STATUS

  PROVIDER

  CLINIC

  SIG

  COPIES

  METHOD OF PICKUP

  REMARKS

  DIVISION

  PHARMACIST

  LOT \# (LOT \# field in OP V. 7.0)

  If a medication error is discovered on a CMOP transmitted prescription, the user should contact the CMOP and request the prescription be cancelled on the vendor system.

### ### Hold Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *HoldFeatures* menu contains the options listed below for the hold features. When using this menu the user can place a prescription on hold, generate a list of prescriptions on hold, or remove a prescription from hold.

*\* Hold RxList Prescriptions on Hold\* Unhold Rx*\*These options have been modified for CMOP and can be found on the *Rx (Prescriptions)* menu of Outpatient Pharmacy V. 7.0.

#### Hold Rx

This function allows the pharmacist to place a prescription on hold.

*CMOP Functionality for Hold Rx*

CMOP Rx’s cannot be placed on hold during CMOP transmission.

#### Unhold Rx

This suboption allows the pharmacist to move a prescription from a Hold status and place it in an Active status.

*CMOP Functionality for Unhold Rx*

The *UnholdRx* option screens the Rx for CMOP criteria. If the criteria are met, the Rx is suspended for transmission to the CMOP and a message is displayed indicating the suspense date. The screening for CMOP is performed after the “MAIL/WINDOW” prompt and response.

Supervisor Functions

The *Supervisor Functions* menu contains seventeen options that the package coordinator uses for implementation as well as maintenance of the various files for the basic running of the Outpatient Pharmacy software.

*Add New ProvidersDaily Cost Compilation\* Delete a Prescription\*† Drug Enter/EditDrug/Drug Interaction Functions...Edit ProviderInitialize Cost StatisticsInter-Divisional ProcessingInventory MenuLookup Clerk by CodeMark/Unmark Lab Monitor DrugsMedication Instruction File Add/EditMonthly Cost CompilationPharmacist Enter/EditRecompile AMIS DataSite Parameter Enter/EditView Provider*\* These options from the Outpatient Pharmacy V. 7.0 *Supervisor Functions* menu have been modified for CMOP.

† An example of this option can be found under the *CMOP Drug/Item Management* menu and the *Outpatient Pharmacy Manager* menu in this manual. This option has been modified for CMOP and can be found on the *OutpatientPharmacy Manager* menu, the *Maintenance (Outpatient Pharmacy)* menu, and the *Supervisor Functions* menu of Outpatient Pharmacy V. 7.0.

### Delete a Prescription

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pharmacy manager uses this option to change a prescription status to Deleted. Deleted prescriptions do not appear on any profiles.

In Outpatient Pharmacy V. 7.0 a released prescription can only be deleted after it has been returned to stock.

*CMOP Functionality for Delete a Prescription*

A CMOP prescription cannot be deleted if the status is Transmitted or Dispensed.

## Suspense Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Suspense Functions* option produces a menu that allows the user to print or delete various entries in the RX SUSPENSE file (#52.5) and print out statistics about entries in the RX SUSPENSE file (#52.5). This file contains prescription labels that have been suspended for printing at a later time. Each prescription label has an associated suspense date which is the fill or refill date.

Copayment only affects this option in the “background”. If a prescription has a copayment charge and is placed in the RX SUSPENSE file (#52.5), the copayment document is printed and a charge is generated when the label prints.

*\*Change Suspense DateCount of Suspended Rx’s by Day\*Delete From Suspense FileLog of Suspended Rx’s by Day (this Division)\*Print From Suspense File\*Pull Early From Suspense\*Reset and Print Again*\* These options from Outpatient Pharmacy V. 7.0 have been modified for CMOP.

### Change Suspense Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the pharmacist to change the suspense date for a specific prescription. The new suspense date becomes the fill/refill date automatically. With this option the pharmacist is also able to delete a specific prescription from suspense.

*CMOP Functionality for Change Suspense Date*

For CMOP prescriptions, suspense dates are changed, the Rx is “unmarked” for transmission for the original date, and then “marked” for transmission for the new suspense date. The user is not notified that the suspense date change was for a CMOP Rx.

### Delete From Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the manager to delete from the RX SUSPENSE file (#52.5) the records of all the prescriptions which have already been printed prior to the user specified number of days. This specified number of days must be set from 7 to 90 days at the “DAYS PRINTED RX STAYS IN 52.5” prompt in the *Site Parameter Enter/Edit* option. The task is set to run every 7 days at the user specified time. The user may also requeue or dequeue this task using this option. Once a prescription is deleted from suspense, it cannot be reset for reprinting.

*CMOP Functionality for Delete From Suspense File*

CMOP prescriptions will not be deleted from the RX SUSPENSE file (#52.5) during the data transmission process.

### Print From Suspense File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the pharmacy manager or pharmacist to print labels for the RX SUSPENSE file (#52.5). Labels are printed through the designated date plus the site parameter specified number of days to be pulled from suspense. There must be at least one prescription to be printed for that patient on or before the print date.

A short profile for every patient for whom you are printing a label for a new prescription is also printed if your site parameters are set for this profile.

*CMOP Functionality for Print From Suspense File*

A date range is selected and “scanned ahead” for a pre-selected number of days to collect all entries on patients for this transmission. “Days to print from suspense” is currently a site parameter in Outpatient Pharmacy Version 7.0.

Selecting the *Print From Suspense File* option displays the following for users who hold the CMOP security keys, PSXCMOPMGR and PSX XMIT:

1 – Initiate Standard CMOP Transmission

2 – Initiate CS CMOP Transmission

3 – Print Current Division – Standard CMOP from Suspense

4 – Print Current Division – CS CMOP from Suspense

5 – Standard Print from Suspense

Select (1, 2, 3, 4, 5):

1-Initiate Standard CMOP Transmission will gather (Non‑Controlled Substances) CMOP data “Queued for Transmission” for the selected date range and transmit to the CMOP. The sender will receive a “Transmission Confirmation” message via MailMan when the data transmission is completed.

Prior to transmitting, the data will be screened for exceptions (window, tradename, non-CMOP, Refill-Too-Soon/DUR rejects, Reject Resolution Required rejects, etc.). (See CMOP Transmission Process for additional information.)

2-Initiate CS CMOP Transmission will gather Controlled Substances CMOP data “Queued for Transmission” for the selected date range and transmit to the CMOP. The sender will receive a “Transmission Confirmation” message via MailMan when the data transmission is completed.

Prior to transmitting, the data will be screened for exceptions (window, tradename, non-CMOP, Refill-Too-Soon/DUR rejects, Reject Resolution Required rejects, etc.). (See CMOP Transmission Process for additional information.)

3-Print Current Division - Standard CMOP from Suspense gathers Non-Controlled Substances data for the selected date range and prints the labels. NO DATA will TRANSMIT to the CMOP. Drugs or items for all labels printed should be filled locally. All usual outpatient prompts will be displayed.

The entries are automatically sorted by Patient name and the “SORT BY PATIENT NAME OR ID#: (P/I)” prompt is not displayed.

4-Print Current Division - CS CMOP from Suspense gathers Controlled Substances data for the selected date range and prints the labels. NO DATA will TRANSMIT to the CMOP. Drugs or items for all labels printed should be filled locally. All usual outpatient prompts will be displayed.

The entries are automatically sorted by Patient name and the “SORT BY PATIENT NAME OR ID#: (P/I)” prompt is not displayed.

5-Standard Print from Suspense will print all labels for Rx's NOT 'Queued to Send' for the selected date range. All usual outpatient prompts will be displayed.

Combinations of the selections presented above are allowed with the exception of 1,2 or 2,1.

## Third Party Electronic Claims Submission of CMOP Prescriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSX\*2\*48 modifies the CMOP application to submit electronic claims for prescriptions that are transmitted to CMOP centers to be filled and dispensed remotely. All the prescriptions that are ready to be included on the batch to be transmitted to CMOP are first transmitted to the third party insurance. Once this first step is completed, the system waits 60 seconds before starting the actual transmission to CMOP. This process will affect the existing CMOP functionality in two ways:

1)  If a response from the third party payer is not received by the time the prescription is about to be transmitted to CMOP, it is skipped and remains in the queue for the next CMOP transmission. A MailMan message containing all the prescriptions that were skipped and that remain in the queue is generated at the end of the process and is transmitted to all the holders of the PSXMAIL security key. If no users on the system have this key, the message is sent to all the users holding the PSXCMOPMGR security key.
2)  Under certain conditions, the prescription is not sent to CMOP and remains in the queue to be transmitted after the third party reject is resolved:
- The third party payer rejects the claim due to a DUR or a Refill Too Soon finding.
- The patient eligibility is TRICARE or CHAMPVA and the third party payer rejects the claim for any reason.
- The patient eligibility is VETERAN, the prescription is an original fill that is unreleased, the third party payer rejects the claim due to a Reject Resolution Required reject, and the total gross amount of the prescription is at or above the user defined threshold amount for the Reject Resolution Required reject.

The prescription will not be transmitted to CMOP until the reject is resolved by the user through the Outpatient Pharmacy V. 7.0 application. Two options have been created for the pharmacy users to resolve these rejects:

> *Third Party Payer Rejects – Worklist \[PSO REJECTS WORKLIST\]*

> *Third Party Payer Rejects – View/Process \[PSO REJECTS VIEW/PROCESS\]*

> The above options reside in the *ePharmacy Menu* \[PSO EPHARMACY MENU\] option, which can be found under the *Rx (Prescriptions)* \[PSO RX\] option.

Patch PSX\*2\*65 modifies the CMOP application to prevent ePharmacy prescriptions from being pulled early from suspense until 3/4 of the days supply of the Rx/fill has elapsed. The system will not hold a prescription for 3/4 days supply when the:

- Previous fill was not ECME billable
- Rx is flagged for SC or EI
- DEA special Handling code is non-billable (i.e., has M or 0 (zero) or (I, S, N, and/or 9)) without an E.
- Patient does not currently have insurance.

![](psx-2-74-user-manual-change-pages/002.png)

Transmission Job is Queued

Xmit Status in CMOP SYSTEM file (#550) = Transmitting Data

Select All Rx’s Queued for Transmission from Rx Suspense

Send/Transmit selected Rx’s to ECME for electronic billing

Wait to receive response from payer

(15 seconds for each e-billable Rx; 2 hours max.)

(e.g., 300 e-billable Rx’s = 4500 seconds/3600 = 1.25 hrs)

From the selected Rx’s, filter Rx’s that have:

The third party payer rejects the claim due to a DUR or a Refill Too Soon finding

The patient eligibility is TRICARE or CHAMPVA and the

third party payer rejects the claim for any reason

The patient eligibility is VETERAN, the prescription is an original fill that is unreleased,

the third party payer rejects the claim due to a Reject Resolution Required reject,

and the total gross amount of the prescription is at or above the user defined threshold amount

for the Reject Resolution Required reject.

From the remaining list, filter Rx’s for which the 3<sup>rd</sup> party payer has not responded

A MailMan message is generated and sent to PSXMAIL keyholders

Mark Selected Rx’s CMOP Indicator = Loading for Transmission

Rescreens Data for CMOP Transmission

Builds Transmission Data in CMOP RX QUEUE file (#550.1)

CMOP Error Encountered Message Created for Rx’s which

Were Selected, but not Transmitted

Creates Transmission Number in CMOP TRANSMISSION file (#550.2)

Creates MailMan Message for Transmission Data and Sends to the Host CMOP Server

Transmission Confirmation Message Generated

Creates Transmission Entry in the CMOP EVENT MULTIPLE

Subfile of PRESCRIPTION file (#52) Marking the Entry as Transmitted

An Entry Is Made in the ACTIVITY LOG Subfile in PRESCRIPTION file (#52) as Transmitted to CMOP

CMOP Indicator in File \#52.5 for All Transmitted Rx’s = Transmission Completed

*(This page included to retain page 130 numbering.)*

# #
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSX*2*76 User Manual Change Pages

### Drug Enter/Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](psx-2-76-user-manual-change-pages/002.png) PSXCMOPMGR
> With this option the user adds new drugs to the file, edits existing drugs, and inactivates drugs. When an entry in DRUG file (#50) is marked for CMOP, the GENERIC NAME and DISPENSE UNIT fields cannot be edited. If editing of these fields is necessary, the entry must be unmarked for CMOP using the *CMOP Mark/Unmark(Single drug)* option. Once editing is completed, the drug must be re-marked for CMOP using the *CMOP Mark/Unmark(Single drug)* option.
> <span id="p17" class="anchor"></span>
Example: Drug Enter/Edit
Select OPTION NAME: PSS DRUG ENTER/EDIT Drug Enter/Edit
Drug Enter/Edit
Select DRUG GENERIC NAME: AMOXAPIN
Lookup: GENERIC NAME
1 AMOXAPINE 100MG TAB CN601
2 AMOXAPINE 25MG TAB CN601
3 AMOXAPINE 50MG TAB CN601
CHOOSE 1-3: 1 AMOXAPINE 100MG TAB CN601
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
This entry is marked for the following PHARMACY packages:
Outpatient
Unit Dose
Non-VA Med
GENERIC NAME: AMOXAPINE 100MG TAB// \<RET\>
VA CLASSIFICATION: CN601// \<RET\>
DEA, SPECIAL HDLG: 6P// \<RET\>
DAW CODE: \<RET\>
NATIONAL FORMULARY INDICATOR: NO
LOCAL NON-FORMULARY: N/F// \<RET\>
VISN NON-FORMULARY: V-N/F// \<RET\>
Select DRUG TEXT ENTRY: \<RET\>
Select FORMULARY ALTERNATIVE: NORTRIPTYLINE HCL 25MG CAP
// \<RET\>
Select SYNONYM: 4037// \<RET\>
SYNONYM: 4037// \<RET\>
INTENDED USE: QUICK CODE// \<RET\>
NDC CODE: \<RET\>
Select SYNONYM: \<RET\>
MESSAGE: NATL N/F (IEN)// \<RET\>
RESTRICTION: \<RET\>
FSN: \<RET\>
NDC: 52544-0381-01// \<RET\>
INACTIVE DATE: \<RET\>
WARNING LABEL SOURCE is 'NEW'.
The following WARNING LABEL may continue to be used for a limited time for some
external interfaces.
WARNING LABEL: 1,9,11,33// \<RET\>
Current Warning labels for AMOXAPINE 100MG TAB
No warnings from the new data source exist for this drug.
Verify that the drug is matched to the National Drug File.
Labels will print in the order in which they appear for local and CMOP fills:
1 -MAY CAUSE DROWSINESS- Alcohol may intensify this effect. USE CARE when
driving or when operating dangerous machinery.
9 DO NOT TAKE non-prescription drugs without medical advice.
11 Avoid prolonged exposure to SUNLIGHT and finish all this medication unless
otherwise directed by prescriber.
33 SEE MEDICATION INFORMATION SHEET FOR DRUG INFO
Pharmacy fill card display: DRUG WARNING 1,9,11,33
NEW WARNING LABEL LIST: 1,9,11,33
Would you like to edit this list of warnings? N// \<RET\>
ORDER UNIT: BT// \<RET\>
PRICE PER ORDER UNIT: 68.82// \<RET\>
DISPENSE UNIT: TAB// \<RET\>
DISPENSE UNITS PER ORDER UNIT: 100// \<RET\>
NCPDP DISPENSE UNIT: EACH// \<RET\>
NCPDP QUANTITY MULTIPLIER: 1// \<RET\>
PRICE PER DISPENSE UNIT: 0.688
points to AMOXAPINE 100MG TAB in the National Drug file.
This drug has already been matched and classified with the National Drug
file. In addition, if the dosage form changes as a result of rematching,
you will have to match/rematch to Orderable Item.
This drug has also been marked to transmit to CMOP.
If you choose to rematch it, the drug will be marked NOT TO TRANSMIT to CMOP.
Do you wish to match/rematch to NATIONAL DRUG file? No// \<RET\>
Just a reminder...you are editing AMOXAPINE 100MG TAB.
Strength from National Drug File match =\> 100 MG
Strength currently in the Drug File =\> 100 MG
Strength =\> 100 Unit =\> MG
POSSIBLE DOSAGES:
DISPENSE UNITS PER DOSE: 1 DOSE: 100MG PACKAGE: IO
DISPENSE UNITS PER DOSE: 2 DOSE: 200MG PACKAGE: IO
LOCAL POSSIBLE DOSAGES:
Do you want to edit the dosages? N// \<RET\>
\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*
This entry is marked for the following PHARMACY packages:
Outpatient
Unit Dose
Non-VA Med
MARK THIS DRUG AND EDIT IT FOR:
O - Outpatient
C - Controlled Substances
X - Non-VA Med
Enter your choice(s) separated by commas : \<RET\>
\*\* You are NOW in the ORDERABLE ITEM matching for the dispense drug. \*\*
AMOXAPINE 100MG TAB is already matched to
AMOXAPINE TAB
Do you want to match to a different Orderable Item? NO// \<RET\>
*(This page included for two-sided copying.)*
