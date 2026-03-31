---
title: PSX*2*50  PSO*7*157 Release Notes - Combat Veteran Phase II
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: PSO*7*157  - Combat Veteran Phase II
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2*50
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - copay
  - prescription
  - table
  - contents
  - status
  - outpatient
  - combat
  - pharmacy
  - order
  - veteran
page_count: 0
word_count: 1565
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/pso_7_157_and_psx_2_p50_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/pso_7_157_and_psx_2_p50_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

![](psx-2-50-pso-7-157-release-notes-combat-veteran-phase-ii/001.png)

COMBAT VETERAN phase II

OUTPATIENT PHARMACY

Consolidated Mail OutPatient Pharmacy (CMOP)

Release Notes

May 2004

V*IST*A Health Systems Design & Development
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [New Features, Functions, and Enhancements](#new-features-functions-and-enhancements)
- [Options](#options)
    - [Outpatient Pharmacy (Patch PSO\7\157)](#outpatient-pharmacy-patch-pso7157)
    - [CMOP (Patch PSX\2\50)](#cmop-patch-psx250)
  - [Actions](#actions)
- [Reports and Profiles](#reports-and-profiles)
- [Files and Fields](#files-and-fields)
- [Other Functionality](#other-functionality)
- [Impacts to Other Packages](#impacts-to-other-packages)
In September 2002, the Department of Veterans Affairs (VA) issued VHA Directive 2002-049 *“Combat Veterans Are Eligible For Medical Services For 2-Years After Separation From Military Service Notwithstanding Lack Of Evidence For Service Connection,”* which iterates the VA's policy to provide medical care and other medical services to combat veterans despite the absence of proof of service connection. The Chief Business Office (CBO) requested modifications to the Veterans Health Information Systems and Technology Architecture (V*IST*A) packages to support implementation of this Directive.
Health Systems Design and Development (HSD&D) has been tasked to create an interim software solution in which, by modifying onlyV*IST*A software, veterans eligible for Combat Veteran services can be identified, treated, and billed as described in VHA Directive 2002-049. This solution will alleviate some of the burden currently placed on VA Medical Centers (VAMCs).
Software to support the combat veteran initiative is being developed and introduced in a phased implementation strategy due to the complexity of the functionality and the number of product line dependencies. Phase I, Combat Veteran Interim Solution (CVIS), was a V*IST*A-only solution that involved development in the Integrated Billing (IB) and Registration/Enrollment product lines. It provided the logic to identify those veterans who met the criteria for the combat veteran eligibility and provided billing reports cross-referenced against this identifier to aid in the copayment billing process. Phase II of this initiative involves multiple product lines and additional V*IST*A-only development. The main goal of Phase II is to fully automate the copayment billing processing of combat veterans based on episode of care by providing the appropriate questions at check-out as supplied by CPRS and/or Outpatient Pharmacy. This includes release through Outpatient Pharmacy and Consolidated Mail Outpatient Pharmacy (CMOP) options, or background processes. The same checks will be applied whenever a prescription label is printed.
The response to the Combat Veteran (CV) medication copay exemption question asked during medication order entry will be stored with each prescription record. The stored value will be carried over whenever a presciption is renewed or copied, or a new prescription is created based on a change to an existing order.
See the updated Outpatient Pharmacy V. 7.0 Technical Manual and User Manual for more detailed information.
*(This page included for two-sided copying.)*

# New Features, Functions, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The addition of CV medication copay exemption is established for outpatient medications prescribed to treat veterans who have served in a theatre of hostility.

The same checks that are currently performed to determine copay status at the time a new prescription is entered will also be performed at release. This includes release through Outpatient Pharmacy, CMOP options, or background processes.

The same checks performed to determine copay status at release are applied whenever a prescription label is printed in order to display the current copay status of the prescription.

*(This page included for two-sided copying.)*

# Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Outpatient Pharmacy (Patch PSO\*7\*157)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]</u><u>Transitional Pharmacy Benefit (TPB) Rx entry \[PSO TPB RX ENTRY\]</u>

When a new or renewal order is placed, the software is modified to perform checks for CV status. All prescription renewal processes (regular, speed, and barcode) will be modified to incorporate the CV values, as necessary.

<u>Complete Orders from OE/RR \[PSO LMOE FINISH\]</u>

The current order placed in CPRS is modified to include the provider response to the CV question. This data shall be passed to the Outpatient Pharmacy application and provided as the CV answer to the pharmacist during the prescription finishing process in the Complete Orders from OE/RR option.

<u>Barcode Batch Prescription Entry \[PSO BATCH BARCODE\]</u>

When a renewal order is placed, the software is modified to perform checks for CV status.

<u>Editing an Existing Medication Order</u>

The editing process is modified to incorporate the new CV medication copay exemption change, as necessary. If the patient is CV eligible, all appropriate questions will be asked and values stored.

<u>Copying an Existing Medication Order</u>

The copying process is modified to incorporate the new medication copay exemption change, as necessary.

<u>Release of a Fill/Refill</u>

During the release of a fill/refill, various checks (patient eligibility, copay exemption status, etc.) are performed to determine the copay status of a prescription. In certain circumstances, applicable medication copay exemptions will be used to evaluate the copay status of the prescription.

<u>Prescription Labels</u>

The software is modified to perform checks for CV status. All prescription label print processes (regular and laser) were modified to incorporate the CV values, as necessary.

<u>Reset Copay Status/Cancel Charges</u> \[PSOCP RESET COPAY STATUS\]

The Reset Copay Status/Cancel Charges \[PSOCP RESET COPAY STATUS\] option is modified to include the CV status as necessary.

> **NOTE:** The existing functionality will not change for any of these options; the software is only modified to accommodate the CV prompt.

<u>Medical Exemption Prompts</u>

To minimize the number of prompts to which a pharmacist needs to respond when a patient meets more than one of the medication exemption criteria, the software will present the service connection and copay exemption prompts in the following order wherever they are asked in the Outpatient Pharmacy software (i.e., Order renewed, finished or a new order via Back door Pharmacy, an edited order, etc.).

- Combat Veteran (CV)
- Vietnam-era herbicide (agent orange)-exposed veterans (AO)
- Radiation-exposed veterans (IR)
- Veterans exposed to environmental contaminants during Persian Gulf War service (EC)
- Military Sexual Trauma (MST)
- Head and/or Neck Cancer (HNC)

<u>Hui Modifications (External Interface)</u>

The pharmacy orders entered via an external interface are sent to CPRS before being filed in the PENDING OUTPATIENT ORDERS (#52.41). This data is modified to include the CV copay exemption status.

### CMOP (Patch PSX\*2\*50)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When evaluating the copay nature of a prescription during CMOP transmission, the current copay exemption check is extended to include the CV entry.

## Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A MailMan message is currently sent to PSORPH keyholders if an Rx Patient Status is set as exempt from copayment. A MailMan message will be sent to PSO COPAY keyholders if any change is made using the *Exempt Rx Patient Status from Copayment* \[PSOCP EXEMPTION\] option.

The copay status of a prescription is reevaluated whenever a prescription label prints in order to display accurate copay status information on the fill document.

# Reports and Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Copay Activity Log is modified to include Combat Veteran code 44 as the reason for the activity. This log can be viewed through the Activity Logs (AL) hidden action in the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option or through the *View Prescriptions* \[PSO VIEW\] option in the *Rx (Prescriptions)* \[PSO RX\] menu.

# Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Files</u>

No files are added or deleted with these patches.

> <u>New Fields</u>

> The following new fields are added to the PRESCRIPTION file (#52) and the PENDING OUTPATIENT ORDERS file (#52.41).

<u>PRESCRIPTION file (#52):</u>

The COMBAT VETERAN field (#122) identifies whether the prescription is being used to potentially treat a Combat Veteran (CV). This field is the 7<sup>th</sup> piece of node “IBQ.”

<u>PENDING OUTPATIENT ORDERS file (#52.41)</u>

The COMBAT VETERAN field (#110.1) identifies whether the prescription is being used to potentially treat a Combat Veteran.

*(This page included for two-sided copying.)*

# Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Labels

The copay status of a prescription will be reevaluated whenever a prescription label is printed or reprinted to minimize the possibility of an incorrect copay status displaying on a label.

# Impacts to Other Packages 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Interactions with Clinician Order Entry through CPRS

Outpatient Pharmacy software provides CPRS with the previously entered medication copay exemption responses to be displayed as defaults to the provider on renewals. It also identifies which medication copay exemptions questions the clinician should be asked when entering or renewing an outpatient medication order through CPRS.

Interactions with Integrated Billing (IB)

Integrated Billing identifies copay charges that have been cancelled and potential charges that have not been billed due to the annual copay cap. Whenever specific actions are taken (e.g., removal of a copay charge) that result in the veteran’s annual medication copayments falling below the cap, IB will initiate a copay charge for a fill that was identified as a potential charge. This activity is logged in the new Copay Activity Log.

Interactions with Patient Information Management System (PIMS)

PIMS provides the identification of veterans to whom the new Combat Veteran medication copay exemption applies. Outpatient Pharmacy software displays these as questions to the pharmacist on outpatient medication order entry or renewal.

*(This page included for two-sided copying.)*