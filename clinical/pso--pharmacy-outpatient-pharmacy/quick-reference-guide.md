---
title: Inpatient Medications & Outpatient Pharmacy NCC (Clozapine) Quick Reference Guide
doc_type: QRG
doc_label: Quick Reference Guide
doc_layer: plain
doc_subject: Inpatient Medications & Outpatient Pharmacy NCC (Clozapine)
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: Inpatient Medications and Outpatient Pharmacy Clozapine Changes– Quick Reference CardInpatient and Outpatient New Functionality
audience: 
keywords: 
  - override
  - clozapine
  - order
  - pharmacist
  - national
  - dispense
  - message
  - reason
  - inpatient
  - provider
page_count: 0
word_count: 1877
section_count: 0
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/MH_NCC_Proj_5_01_PSO_PSJ_QR_R0719.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/MH_NCC_Proj_5_01_PSO_PSJ_QR_R0719.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

Inpatient Medications and Outpatient Pharmacy  
Clozapine Changes– Quick Reference CardInpatient and Outpatient New Functionality

Inpatient Medications has been enabled to function in the same way as Outpatient Pharmacy for managing patients on clozapine. Both have been updated to include new functionality and to support FDA guidelines for treatment and monitoring based on Absolute Neutrophil Count (ANC). \*Note: VA continues to require the presence of a matching WBC count.

Hierarchy for Addressing Clozapine Patients Override Conditions

The table below illustrates how the system prioritizes override conditions when more than one abnormal condition exists. Only one condition can be treated for a patient – there can only be one override reason code in an ordering session. In all conditions, the patient must be actively registered with the NCCC ( National Clozapine Coordinating Center or a temporary local emergency registration number.

| Condition                                           | ANC Present? | Matching WBC? | Action                           |
|---------------------------------------------------------|------------------|-------------------|--------------------------------------|
| \*No registration (Active with NCCC or Local Temporary) | Yes/No           | Yes/No            | Address no registration first        |
| Normal ANC                                              | Yes              | Yes               | No override needed                   |
| Normal ANC                                              | Yes              | No                | Address No WBC                       |
| Mild Neutropenia                                        | Yes              | Yes               | Address Mild neutropenia             |
| Mild Neutropenia                                        | Yes              | No                | Address No WBC                       |
| Moderate to Severe                                      | Yes              | Yes               | Address Moderate/ Severe neutropenia |
| Moderate to Severe                                      | Yes              | No                | Address No WBC                       |
| No ANC                                                  | No               | Yes/No            | Address No ANC                       |

\*To use the Emergency Registration Override, the patient’s ANC in the last 7 days must be 1500/cmm or greater.

Request for Override of Pharmacy Lockout Form – National Overrides

Whenever a national override is *required* to dispense clozapine, this form must be submitted to the NCCC before the NCCC can approve the National Override.

The form documents the clinical or administrative reason for the national override request and documents blood test results.

Safety Checks

Safety checks include checking for patient registration status (active or discontinued), authorized provider, and lab results, which are based on FDA guidelines. When the pharmacist receives a pending order from CPRS, safety checks are repeated.

Pharmacist Processing Overrides

The pharmacist must have the PSOLOCKCLOZ key in order to process orders that require an override. If not authorized to dispense, this message displays:

You Are Not Authorized to Override! See Clozapine Manager with PSOLOCKCLOZ key

Approving Member of Clozapine Team for Overrides

In all conditions where an override is required, either local or national, the primary pharmacist is required to enter the name of an Approving Member of the clozapine team who also possesses the PSOLOCKCLOZ key.

Auto-notification when Override is Complete

After the pharmacist completes an order with an override, the system sends an auto-notification via VistA Alerts to both the Provider and the Approving Member that the override clozapine order was verified/completed.

New Local Override: Emergency Registration Override – temporary local authorization number

When there is an urgent need to dispense clozapine, an Emergency Registration Override allows the pharmacist to assign a temporary local authorization number, which is valid for four days until the NCCC can assign a permanent number. A written order or prescription from the provider is required and is processed only in the VistA Backdoor Pharmacy. The pharmacist sees this message:

\*\*\* This patient has no clozapine registration number \*\*\*

When the unique 7 digit temporary local authorization number (e.g., Z442001) is assigned, the system checks to ensure that the patient has an ANC result of 1500/cmm or greater. If less than 1500/cmm, the pharmacist will see this message and a hard stop will occur:

Emergency Registration Local Override for non-registered clozapine patients requires ANC levels greater than or equal to 1500.

If the ANC is normal (1500/cmm or greater) the pharmacist will see this message with the override reason:

Override reason: REGISTER NON-DUTY HR/WEEKEND (MAX 4DAY)

> **NOTE:** For an emergency registration, the pharmacist is authorized to dispense a maximum one-time, 4 day supply.

Normal ANC results (1500/cmm or greater)

The pharmacist processes the pending or written prescription or order. No override is needed. The pharmacist does not require the PSOLOCKCLOZ key for normal ANC.

Mild Neutropenia (ANC 1000-1499/cmm) (Local Override)

The pharmacist processes a pending or written prescription or order with a Local Override when the patient has Mild Neutropenia. The pharmacist sees this message:

Override reason: MILD NEUTROPENIA PRESCRIBER APPROVED

Test ANC labs 3x weekly until levels stabilize to greater than or equal to 1500

Moderate or Severe Neutropenia (National Override)

The pharmacist processes a pending or written prescription or order, which requires a National Override when the patient has Moderate or Severe Neutropenia. Note that both Moderate and Severe neutropenia are treated the same as they both have an ANC less than 1000/cmm. When the National Override is in effect, the pharmacist sees this message:

Now doing clozapine Order checks.  Please wait...

Permission to dispense clozapine has been authorized by NCCC

Test ANC labs Daily until levels stabilize to ANC greater than or equal to 1000

Override reason: NCCC AUTHORIZED

Moderate or Severe Neutropenia (No National Override)

When there is no National Override in effect, the pharmacist sees this message:

\<*Displays up to last four results in the last 30 days\>*

Permission to dispense clozapine has been denied. If the results of the latest Lab Test drawn in the past 7 days show ANC below 1000/mm3 and you wish to dispense outside the FDA and VA protocol ANC limits, document your request to Request for Override of Pharmacy Lockout (from VHA Handbook 1160.02) Director of the VA National Clozapine Coordinating Center (Phone: 214-857-0068 Fax: 214-857-0339) for a one-time override permission.  
Also make sure that the LAB test, ANC is set up correctly in the Mental Health package using the CLOZAPINE MULTI TEST LINK option.

No ANC result – National Override for non-emergency

When there is no ANC result in the last 7 days, the provider in CPRS will determine if this is an emergency or not. If they elect to get a National Override (non-emergency), the pharmacist will see this message in the pending prescription or order:

Now doing clozapine Order checks. Please wait…

Permission to dispense clozapine has been authorized by NCCC

Override reason: NCCC AUTHORIZED

> **NOTE:** If pharmacy-processing delays have caused a lockout, the Pharmacist may request a National Override for an administrative reason from the NCCC using the Request for Override of Pharmacy Lockout Form. The pharmacist can complete the pending order after the override is granted.

New Local Override: No ANC result – Special Conditions Local Override for emergency

If this is an emergency and a 4 day supply is needed for either Outpatient Special Conditions or Inpatient Special Conditions, the provider is required to provide a *written order* to the pharmacist and include one of the following applicable approved reasons:

<u>Outpatient</u>

1)  Weather-related condition
2)  Mail order delays
3)  Inpatient going on leave

<u>Inpatient</u>

IP Order Override with Outside Lab Results

No ANC result – Outpatient Special Conditions

When the written order for an Outpatient is received by the pharmacy, the pharmacist in VistA Backdoor Pharmacy sees this message:

*\<Displays up to the last 4 results within the past 30 days, if applicable\>*

\*\*\* Permission to dispense clozapine has been denied based on the available lab tests related to the clozapine treatment program. \*\*\*

For a National Override to dispense at the patient’s normal frequency, please contact the VA National Clozapine Coordinating Center to request an Override of Pharmacy Lockout (from VHA Handbook 1160.02) (Phone: 214-857-0068 Fax: 214-857-0339).

A Special Conditions Local Override for Outpatients can be approved for (1) weather-related conditions, (2) mail order delays of clozapine, or (3) inpatient going on leave. With provider’s documentation of approval, you may dispense a one-time supply not to exceed 4 days.

The pharmacist continues processing the clozapine order for Outpatient Special Conditions and sees this message:

Override reason: PRESCRIBER APPROVED 4 DAY SUPPLY

The pharmacist is required to select the approved provider reason that is included in the written order and document it during processing.

Outpatient Pre-populate Remarks field

The Outpatient Remarks field is pre-populated with the approved provider reason, for example:

Prescriber approved reason description: Weather Related Condition

The pharmacist can add additional free text up to a total of 200 characters.

No ANC result – Inpatient Special Conditions

When the written order for an Inpatient is received by the pharmacy, the pharmacist in VistA Backdoor Pharmacy sees this message:

\*\*\* Permission to dispense clozapine has been denied based on the available lab tests related to the clozapine treatment program. \*\*\*

For a National Override to dispense at the patient’s normal frequency, contact the NCCC.

A local override for an Inpatient can be approved for:  
IP Order Override with Outside Lab Results.

For a Special Conditions Local Override, a written order from the provider with documentation to the pharmacist is required to dispense a one-time 4-day supply.

The provider must record the ANC from another facility including date/time in both the Provider Progress Note and Comment field in CPRS.

The pharmacist continues processing the clozapine order for Inpatient Special Conditions and sees this message:

Override reason: PRESCRIBER APPROVED 4 DAY SUPPLY

The pharmacist is required to select the approved provider reason that is included in the written order and document it during processing.

Inpatient Pre-populate Special Instructions field

The Inpatient Special Instructions field is pre-populated with the approved provider reason:

Prescriber approved reason description: IP Order Override with Outside Lab Results

The pharmacist can add additional free text up to a total of 200 characters.

> **NOTE:** For an Inpatient Special Conditions Local Override, the pharmacist must also record the outside ANC lab results in the Special Instructions field, including date/time.

No Matching WBC – National Override in effect

A matching WBC is from the same draw date/time as the ANC. If there is no matching WBC, the system requires a National Override. The pharmacist receives a pending order from CPRS and sees this message:

Now doing clozapine Order checks. Please wait…

Permission to dispense clozapine has been authorized by NCCC

Override reason: NCCC AUTHORIZED

No Matching WBC – No National Override in effect

If the pharmacist receives a pending prescription or order and the National Override is *not* in effect (e.g., expired before processing or labs changed), the pharmacist sees this message:

\<*Displays up to the last 4 results within the last 30 days, if available*\>

Permission to dispense clozapine has been denied. The result of the latest Lab Test drawn in the past 7 days shows ANC results but No Matching WBC. If you wish to dispense outside the FDA and VA protocol ANC limits, document your request to Request for Override of Pharmacy Lockout (from VHA Handbook 1160.02) Director of the VA National Clozapine Coordinating Center (Phone: 214-857-0068 Fax: 214-857-0339) for a one-time override permission.

Total Daily Dose

The required manual calculation for Total Daily Dose is now the same in Inpatient Medications as in Outpatient Pharmacy.

Data Store and Transfer to National Clozapine Files

Once clozapine is dispensed, the patient data is stored in a temporary file for later nightly transmission to the National Clozapine data file, replacing the weekly roll-up.

Retransmission of data files

Data is retained for one year in the event it needs to be retransmitted. If the nightly batch fails or the system is down, the system will automatically resend the data when the system is restored.

Complex Clozapine Orders

When the provider creates a complex Pending order in CPRS, the Inpatient Medications pharmacist processes each child order for each dose/dispense instruction. Because of known issues within complex orders with correctly calculating the stop date for all medications, the workaround clozapine solution is to have the clozapine stop date calculated separately and presented in a warning message allowing the Inpatient Medications pharmacist to manually verify the validity of the stop date. The warning message is displayed:  

This order contains a requested duration.

Please review the system calculated stop date to confirm that it is within the allowable duration of the order based on the patient’s authorized clozapine dispense frequency.

Order stop date should not exceed MM/DD/YY

Review the entire profile to determine appropriate actions(s). 

The pharmacist is responsible to ensure that the stop date of the final child order does not exceed the stop date presented in the warning message by editing the stop date. If any of the child stop dates exceed the date calculated in the warning message, the order must be discontinued and the provider will need to create a new order.