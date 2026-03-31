---
title: PSJ*5*134 Release Notes-CPRS V27 Project
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: CPRS V27 Project
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*134
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - cprs
  - pharmacy
  - changes
  - order
  - medications
  - schedule
  - inpatient
  - patient
  - outpatient
  - orders
page_count: 0
word_count: 1303
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_pso_7_pss_1_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_pso_7_pss_1_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

![](psj-5-134-release-notes-cprs-v27-project/001.png)

Pharmacy Changes to Support Computerized Patient Record System (CPRS) GUI Version 27.0

Release Notes

PSJ\*5\*134, PSO\*7\*225, PSS\*1\*94

August 2008

VistA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Inpatient Medications Changes](#inpatient-medications-changes)
- [Pharmacy Data Management Changes](#pharmacy-data-management-changes)
- [Outpatient Pharmacy Changes](#outpatient-pharmacy-changes)
The Computerized Patient Record System (CPRS) V. 27.0 Medication Ordering Enhancements project provides modifications and new functionality for the following Pharmacy applications:
- Inpatient Medications V. 5.0
- Pharmacy Data Management (PDM) V. 1.0
- Outpatient Pharmacy V. 7.0
The scope of this project includes software packages that interact to track medications from ordering to pharmacy dispensing and finally administration to the patient. The changes in these packages are defined as a team to provide safe transmission for medication orders from provider to pharmacist to nurse to patient.
The CPRS V. 27.0 enhancements support the overall efforts of the Veterans Health Administration (VHA) to enhance patient safety, in conjunction with the establishment of the National Center for Patient Safety (NCPS) and computerized initiatives. The CPRS V. 27.0 enhancements address user issues as identified by Inpatient Medications workgroups, the CPRS technical team, the CPRS Clinical workgroup, CPRS test sites and other user groups. These functional workgroups, comprised of nurses, physicians, and pharmacists, reviewed the findings, intended to provide stakeholders with requested functionality to enhance safety and provide patient care.
The following patches are included in this CPRS V. 27.0 release:
- PSJ\*5\*134-Provides updated functionality for Inpatient Medications V. 5.0
- PSS\*1\*94-Provides updated functionality for PDM V. 1.0
- PSO\*7\*225-Provides updated functionality for Outpatient Pharmacy V. 7.0

# Inpatient Medications Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inpatient Medications changes consist of the following features:

- The Medication Route provided by CPRS is applied as the default when finishing an IV order. The system also transmits any updates to a specific order’s Medication Route to CPRS using current HL7 messaging strategies.
- Standard HL7 field delimiters represented by the “~ , &, \| ” (tilde, ampersand, pipe) characters as well as the commonly used VistA “^” (caret) are sometimes needed by users of Inpatient Medications in various fields to provide complete information about a patient or order. The use of these characters can cause sending and receiving software to format HL7 messages incorrectly, and/or construct/deconstruct the information incorrectly. Data loss can also occur if data is truncated at one of the special delimiter characters.

> To correct this issue, special escaping characters are provided by the Inpatient Medications package to allow users to complete the ordering process. See the *Inpatient Medications Technical Manual/ Security Guide* for details.

- The following Inpatient Medications IV Type changes for infusion orders received from CPRS have been made:
  - Inpatient Medications accepts infusion rates from CPRS in both ML/HOUR and as INFUSE OVER TIME.
  - In the order view screen for an order with an IV Type that is considered Intermittent, the infusion rate displays as “INFUSE OVER” followed by the time (For example, infuse over 30 minutes). When the order is for an IV Type that is considered Continuous, the infusion rate displays as the rate of infusion.
  - Inpatient Medications transmits schedule changes to CPRS for IV orders using current HL7 messaging strategy.
  - Inpatient Medications accepts the IV Type from CPRS using current HL7 messaging strategy.
  - When IV type of Continuous is received, Inpatient Medications defaults to an IV type of Admixture.
  - When IV type of Intermittent is received, Inpatient Medications defaults to an IV type of Piggyback.
  - Inpatient Medications sends updates to IV Type to CPRS using current HL7 messaging strategy.
- When a pharmacist attempts to discontinue a pending renewal, the following message displays.

> This order is in a pending status. If this pending order is discontinued, the original order will still be active

> When a pending renewal is discontinued, the order returns to its previous status.

- An expected first dose for an order containing a schedule with a schedule type of ONE-TIME no longer displays. The system also no longer displays an expected first dose for an order containing a schedule with a schedule type of ON-CALL. Order entries now permit the entry of a Day-of-Week schedule in the following format.

days@schedule name (e.g. MO-WE-FR@BID, TU@Q6H)

The translated schedule displays to the pharmacist while processing pending orders.

- The schedule is translated into appropriate administration times. (For example, MO-WE-FR@BID is translated to MO-WE-FR@10-22.)
- The abbreviation for Millimole has been changed from MM to MMOL.

# Pharmacy Data Management Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PDM changes consist of the following features:

- Pharmacy Data Management Medication Route Changes
- PDM provides a list to CPRS of medication routes for use with IVs following the logic described below.

> If there is one and only one orderable item in the IV order, the PHARMACY ORDERABLE ITEM file (#50.7) will be checked to see if there is a default med route. Additionally, any med route defined for the dosage form of the orderable item will be checked. Duplicate entries will be filtered by Inpatient Medications. The list of possible med routes sent back to CPRS will include the default med route (if defined), as well as any other med routes defined for the dosage form.

> If there is more than one orderable item on the IV order, the PHARMACY ORDERABLE ITEM file (#50.7) will be checked for each orderable item to see if a default is defined. This default will be pooled with the other possible med routes for each dosage form for each orderable item. Duplicates will be filtered by Inpatient Medications. Regardless of whether all orderable item defaults match or not, a default med route will not be marked as a default if there is more than one orderable item on the order. The list of possible med routes returned to CPRS will include only those med routes that every orderable item in the order shares in common.

- Administration Schedule
- If there is a duplicate schedule, and if one of them contains ward-specific administration times for the ward location of the patient, the schedule returned for inclusion in the array of selectable schedules in CPRS will be the one with the ward-specific administration times.
- If no duplicate has ward-specific administration times for the ward location of the patient, the schedule with the lowest IEN number will be returned. If both (or more than one) duplicate schedules have ward-specific administration times for the ward location of the patient, the schedule with the lowest IEN number in the ADMINISTRATION SCHEDULE file (#51.1) will be the schedule in the array returned to CPRS.

# Outpatient Pharmacy Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Pharmacy changes consist of the following features:

- A new Environmental Indicator (EI), Shipboard Hazard and Defense (SHAD), called Project 112/SHAD has been added. If a patient is found eligible for SHAD, then the prompt “Was treatment related to PROJ 112/SHAD?” will be presented to the pharmacist.
- The EI, “Environmental Contaminant” has been changed to read “Southwest Asia Conditions.”
- The flag/un-flag functionality is now available for Outpatient Pharmacy use on new pending orders only.
- To improve communication between the provider and the pharmacist, Outpatient Pharmacy now sends the actual comments made by the pharmacist to CPRS when a prescription is put on Hold, Discontinued, and Returned to Stock, replacing the generic "per pharmacy request" text.
- When a pending renewal order is discontinued, Outpatient Pharmacy verifies if there is an active prescription for the same drug. If an active prescription is found, you are prompted with the following message.

> There is an active Rx for this pending order, Discontinue both (Y/N).

> Now you can discontinue both the pending order and the active order if you respond YES, or only the pending order if you respond NO.

- The original provider comments are no longer carried over to any renewals in Outpatient Pharmacy following through with CPRS changes.
- Standard HL7 field delimiters represented by the “~ , &, \| ” (tilde, ampersand, pipe) characters, as well as the commonly used VistA “^” (caret), are sometimes needed by users of Outpatient Pharmacy in various fields to provide complete information about a patient or order. The use of these characters can cause sending and receiving software to format HL7 messages incorrectly, and/or construct/deconstruct the information incorrectly. Data loss can also occur if data is truncated at one of the special delimiter characters.

> To correct this issue, special escaping characters are provided by the Outpatient Medication package to allow users to complete the ordering process. See the *Outpatient Pharmacy Technical Manual/Security Guide* for details.

- The following flagging functionality has been added:
- CPRS will be enhanced to allow transmission of HL7 messages related to flag/un-flag any Outpatient Pharmacy pending orders to the backdoor pharmacy.
- A new “FL-Flag” action will be added to the list of the ListManager actions for the pending orders.
- The flag action will be available to alert the users that the pending order is incomplete or needs clarification.
- When the user flags the order, an alert will be sent to the specified user defining the information that is needed to process the medication order. The specified user can send a return alert with the needed information.
- This action will only be available to those users who hold the PSORPH key.
- When a flagged order appears on the order view, the order number column will be highlighted in reverse video.
- The Complete Orders from OERR \[PSO LMOE FINISH\] option will be modified to allow processing of flagged pending orders using the “FL” selection.
- The Complete Orders from OERR \[PSO LMOE FINISH\] option will be modified to restrict processing of pending flagged orders through options other than the “FL” option.