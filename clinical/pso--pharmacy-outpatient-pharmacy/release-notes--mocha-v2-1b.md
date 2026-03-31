---
title: MOCHA Version 2.1b Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: b
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 2.1
patch_id: PSO*2.1
group_key: "PSO:PSO:2.1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - order
  - table
  - contents
  - dose
  - check
  - schedule
  - pharmacy
  - mocha
  - error
  - daily
page_count: 0
word_count: 2154
section_count: 16
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_pso_7_psj_5_rn_r0218.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_pso_7_psj_5_rn_r0218.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

![](mocha-version-2-1b-release-notes/001.png)

Medication order check healthcare application (mocha) v2.1b

Release Notes

PSJ\*5\*256, PSO\*7\*402, and OR\*3\*382  
(MOCHA 2.1 Combined Build 1.0)

PSJ\*5\*347, PSO\*7\*500, and OR\*3\*469  
(MOCHA 2.1 FOLLOW UP Combined Build 1.0)

PSS\*1\*178 and PSS\*1\*206 (Stand Alone)

February 2018

Product Development

*(This page included for two-sided copying.)*Table of Contents

*  
(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Enhancements](#enhancements)
- [Menu Changes](#menu-changes)
  - [New Options](#new-options)
  - [Changed Options](#changed-options)
  - [Deleted Options](#deleted-options)
  - [New Files](#new-files)
  - [New Fields](#new-fields)
  - [Modified Fields](#modified-fields)
  - [Security Key](#security-key)
  - [Modified Templates](#modified-templates)
- [Other Functionality](#other-functionality)
  - [PSS\1\178](#pss1178)
  - [OR\3\382](#or3382)
  - [PSO\7\500](#pso7500)
  - [OR\3\469](#or3469)
  - [PSJ\5\347](#psj5347)
- [Impacts to Other Package](#impacts-to-other-package)
- [Known Anomalies](#known-anomalies)
  - [Hard Error when Editing Schedule (RTC# 655355)](#hard-error-when-editing-schedule-rtc-655355)
  - [Hard Error if User Accepts Intermittent IV Order without Schedule (RTC# 656248)](#hard-error-if-user-accepts-intermittent-iv-order-without-schedule-rtc-656248)
The goal of the Pharmacy Reengineering (PRE) project is to replace the current M-based suite of Pharmacy applications with a system that will better meet the current and expected business needs for the Department of Veterans Affairs (VA) and address the ever-changing patient safety issues. The first phase, Medication Order Check Healthcare Application (MOCHA) v1.0, implemented enhanced order checking functionality utilizing HealtheVet (HEV) compatible architecture and First Databank (FDB) MedKnowledge Framework (formerly DIF) Application Program Interfaces (APIs), and database for Drug Interaction and Duplicate Therapy order checks. MOCHA v2.0 implemented the Maximum Single Dose Order Check for simple and complex medication orders. MOCHA v2.1a released new fields, updated options and one new file that is essential to the implementation of the Max Daily Dose Order Check for simple medication orders for this MOCHA v2.1b release.
This release notes document provides a brief description of the new features and functions of the MOCHA v2.1b patches listed in the table below. More detailed information on the functionality can be found in the application user and technical manuals found on the VA Software Document Library (VDL).
| Application                                | Patch                    |
|--------------------------------------------|--------------------------|
| Outpatient Pharmacy                        | PSO\*7\*402, PSO\*7\*500 |
| Inpatient Medications                      | PSJ\*5\*256, PSJ\*5\*347 |
| Pharmacy Data Management (PDM)             | PSS\*1\*178, PSS\*1\*206 |
| Computerized Patient Records System (CPRS) | OR\*3\*382, OR\*3\*469   |
Table : Duplicate Therapy Order Checks Performed Between Order Types
Please Note: Please contact the MOCHA v2.1 deployment team <span class="mark">REDACTED</span> should you have any questions or concerns regarding software installation or implementation.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA v2.1b will provide the following enhancements:

Enhanced Order Checking Features:

- Implement Dose Range Checking with a Max Daily Dose limit for simple medication orders entered through Outpatient Pharmacy, Inpatient Medication, and CPRS.
- Display a generic error message when the Max Daily Dose Order Check cannot be performed in CPRS.
- Display an error message when the Max Daily Dose Order Check cannot be performed in CPRS with a detailed reason when height and/or weight is required, but does not exist in the Vitals application for the patient.
- Display an error message when the Max Daily Dose Order Check cannot be performed in Pharmacy with a detailed reason.
- Create a General Dosing Information message to be displayed when Dosing Checks cannot be performed.
- Correct identified daily dose errors due to frequency failure.
- Resolve miscellaneous frequency issues with incorporation of new dosing check frequency fields.
- Apply Daily Dose Check exclusion for schedule to medication orders entered through Outpatient Pharmacy, Inpatient Medications, and CPRS.
- Apply advisory note to high dose warnings and General Dosing Guidelines for medication administered through eye, ear, or nose.
- Create a customized frequency message.
- Create a Max Daily Dose Warning message for the calculated Daily Dose.
- Add FDB data elements from Dosing Order Check call to VistA side of interface.
- Modifications to the ‘Available Dosage(s)’ list when a screen break occurs during order entry through the Outpatient Pharmacy application.
- Modifications to the accompanying dialog for the ‘Available Dosage(s)’ list displayed during order entry through the Outpatient Pharmacy application.
- Modification to display the most recent Serum Creatinine value and date resulted if available, even if the CrCL cannot be calculated on the pharmacy patient demographic header.
- Display BSA and CrCL information in the headers on all Outpatient Pharmacy medication order detail screens and all Inp atient Medications and Outpatient Pharmacy patient information screens that are currently missing this information.
- Display one warning if Maximum Single Dose and Max Daily Dose Order Check warning texts are identical.
- Adjustment to the Daily Dose if a Single Dose Adjustment is made for an IV order when performing Dosing Order Checks.
- Notify user when an Old Schedule Name is used for an order during Inpatient Medications backdoor order entry for finish, verify, copy, and renew actions.
- Modify entries to the DOSE UNITS File (#51.24), see Section 4 for details.
- Modify entries to the DOSE UNIT CONVERSION File (#51.25), see Section 4 for details.
- Update *Check PEPS Services Setup* \[PSS CHECK PEPS SERVICES SETUP\] option to perform the Max Daily Dose Order Check instead of the Daily Dose Range Order Check.
- Enhance lookup functionality when entering a schedule for an outpatient medication order through the pharmacy backdoor.

# Menu Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No menu changes have been made.

## New Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new options have been created.

## Changed Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options have been changed:

- Modified the *Check PEPS Services Setup* \[PSS CHECK PEPS SERVICES SETUP\] option to perform the Max Daily Dose Order Check instead of the Daily Dose Range Order Check.

## Deleted Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No options have been deleted.

## New Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new files have been added.

## New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new fields have been added.

## Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No fields have been modified.

## Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new security keys have been created.

## Modified Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No templates have been modified.

# Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PSS\*1\*178

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*178 provides the following additional functionality:

- The POST-INIT routine POST^PSS1P178 will change the FIRST DATABANK DOSE UNIT field value for the ‘APPLICATORFUL(S)’ entry to ‘APPLICATORFUL(S)’ in the DOSE UNITS file (#51.24).
- The POST-INIT routine POST^PSS1P178 will change the FIRST DATABANK DOSE UNIT field value for the ‘SUPPOSITORY(IES)’ entry to ‘SUPPOSITORY(IES)’ in the DOSE UNITS file (#51.24).
- The POST-INIT routine POST^PSS1P178 will change the DOSE UNIT 1 value from 'SUPPOSITORY/IES' to 'SUPPOSITORY(IES)' in the DOSE UNIT CONVERSION file (#51.25).
- The POST-INIT routine POST^PSS1P178 will change the DOSE UNIT 1 value from ‘APPLICATORFUL/S’ to 'APPLICATORFUL(S)' in the DOSE UNIT CONVERSION file (#51.25).
- The POST-INIT routine POST^PSS1P178 will change the DOSE UNIT 2 value from 'SUPPOSITORY/IES' to 'SUPPOSITORY(IES)' for the DOSE UNIT 1 entry of ‘EACH’ in the DOSE UNIT CONVERSION file (#51.25).
- The POST-INIT routine POST^PSS1P178 will change the DOSE UNIT 2 value from 'APPLICATORFUL/S' to 'APPLICATORFUL(S)' for the DOSE UNIT 1 entry of ‘APPFUL’ in the DOSE UNIT CONVERSION file (#51.25).

## OR\*3\*382

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3\*382 is part of the MOCHA v2.1b COMBINED BUILD. This patch will address the following issues:

- Corrects an issue with the Application Programming Interface (API) that searches through quick orders for specific orderable items. For Infusion orders, there is a possibility of having multiple orderable items associated with an order. If the name of the Pharmacy Orderable Item was edited for an IV Additive that was contained in a quick order, a notification via MailMan message was not sent to the G. OR CACS mail group and the person that edited the IV Additive Pharmacy Orderable Item. The notification was only sent when the IV Solution Pharmacy Orderable Item was edited. A notification via MailMan message will now be sent if any of the Pharmacy Orderable Item names are edited within a quick order with multiple orderable items.
- CPRS will group together and display all dosing warnings requiring an override reason by drug.
- CPRS will group together and display all informational dosing messages by drug
- CPRS will no longer prompt for an override reason for dosing informational messages. An override reason will only be prompted for high dose warnings.

## PSO\*7\*500

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSO\*7\*500 is a part of the MOCHA v2.1b FOLLOW UP Combined Build. This patch brings in the following change:

- In order to display the patient's weight in kilograms (KG), the current conversion from pounds (LB) to KG is being done by dividing the patient weight on file by 2.2. The weight calculation conversion from LB to KG is being modified to increase the precision of the patient weight in KG by dividing it by 2.2046226 instead. This change will make the Outpatient Pharmacy consistent with Computerized Patient Record System (CPRS).

## OR\*3\*469

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3\*469 is a part of the MOCHA v2.1b FOLLOW UP Combined Build. This patch brings in the following changes:

- Eliminates the Duplicate Drug Order Check in CPRS for medications. The Duplicate Drug Order Check will only be performed for supply items in CPRS. No changes have been made in backdoor Outpatient Pharmacy.
- Duplicate Therapy Order Checks will be performed against the following types of orders summarized in the table below in CPRS. No changes were made in backdoor Pharmacy applications.

| Order Type        | Inpatient Profile | Outpatient Profile | Remote Outpatient Profile | Non-VA Med Profile | Clinic Order\* Profile |
|-------------------|-------------------|--------------------|---------------------------|--------------------|------------------------|
| Inpatient         | X                 |                    |                           |                    | X                      |
| Outpatient        |                   | X                  | X                         | X                  | X                      |
| Clinic Order\*    | X                 | X                  | X                         | X                  | X                      |
| Remote Outpatient |                   |                    |                           |                    |                        |
| Non-VA Med        |                   | X                  | X                         | X                  | X                      |

> \* Includes Clinic meds and Clinic Infusions

> X Duplicate Therapy Order Check performed

## PSJ\*5\*347

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSJ\*5\*347 is a part of the MOCHA v2.1b FOLLOW UP Combined Build. This patch brings in the following change:

- In order to display the patient's weight in kilograms (KG), the current conversion from pounds (LB) to KG is being done by dividing the patient weight on file by 2.2. The weight calculation conversion from LB to KG is being modified to increase the precision of the patient weight in KG by dividing it by 2.2046226 instead. This change will make the Inpatient Medications consistent with the Computerized Patient Record System (CPRS).

# Impacts to Other Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3\* 382 will be released in the MOCHA v2.1b combined build with PSO\*7\*402 and PSJ\*5\*256. It provides CPRS functionality for the Max Daily Dose Order Check.

# Known Anomalies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List of Outstanding Anomalies:

## Hard Error when Editing Schedule (RTC# 655355)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A hard error can occur in Outpatient Pharmacy when editing a schedule in an order for either of the following 2 scenarios:

1)  A schedule is entered that is in neither the Administration Schedule File nor the Medication Instruction File.
2)  A schedule is entered that is in either or both of these files, but the user replies ‘No’ to the prompts for which file(s) it is in. This scenario does not make sense to do, because the software logic that looks for the Outpatient expansion will still find that schedule and use its expansion data if it exists.

If this error does occur, the following workarounds can be implemented:

1)  The user can enter the schedule in either or both files, and then the user should reply ‘Yes’ when that entry is identified during the schedule look-up.
2)  The user can discontinue the current order and place a new order with that schedule, since the error will not occur during new order entry.
3)  The user can copy the order and immediately perform an edit to the schedule. If this involves a pending order, the order must first be finished and accepted as is and then the copy performed.

If this error occurs, it does not appear that any data corruption is present.

This defect will be fixed in patch PSO\*7\*515.

## Hard Error if User Accepts Intermittent IV Order without Schedule (RTC# 656248)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A hard error can occur in Inpatient Medications when accepting a new order entered through backdoor options for an intermittent IV without entering a schedule. If this error does occur, the incomplete IV order will not appear on the patient profile. Warning messages are displayed to the user before accepting the order that no schedule exists for the order and that there are no administration times defined for the order. To prevent this error, the user can enter a schedule at the accept/edit prompt when the IV order is displayed for review or the user can enter an up-caret (“^”) to exit the order at the accept/edit prompt when the IV order is displayed for review.

This defect will be fixed in patch PSJ\*5\*358 during the defect resolution period.