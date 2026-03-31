---
title: PSO*7*143 Clinical Indicator Data Capture Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Clinical Indicator Data Capture
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*143
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Introduction](#introduction) - [New Features, Functions, and Enhancements](#new-features-functions-and-enhancements) - [Options](#options) - [Reports and Profiles](#reports-and-profiles) - [Files and Fields](#files-and-fields) - [Other Functionality](#other-functionality) - [Impacts to Other Pa
audience: 
keywords: 
  - diagnosis
  - outpatient
  - code
  - table
  - contents
  - pharmacy
  - cidc
  - diabetes
  - copay
  - service
page_count: 0
word_count: 1709
section_count: 1
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p143_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p143_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-143-clinical-indicator-data-capture-release-notes/001.png)

CLINICAL INDICATOR DATA CAPTURE (cidc)

Outpatient Pharmacy

<span id="_Toc87424323" class="anchor"></span>RELEASE NOTES

####### 

PSO\*7.0\*143

August 2005

VistA Health Systems Design & Development
# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [New Features, Functions, and Enhancements](#new-features-functions-and-enhancements)
- [Options](#options)
- [Reports and Profiles](#reports-and-profiles)
- [Files and Fields](#files-and-fields)
- [Other Functionality](#other-functionality)
- [Impacts to Other Packages](#impacts-to-other-packages)
The Outpatient Pharmacy V. 7.0 package provides a method for managing the medications given to veterans who have visited a clinic or who have received prescriptions upon discharge from the hospital. The Outpatient Pharmacy application has been enhanced to collect and store all relevant data required to bill a service as a potential reimbursable event, thereby increasing revenue for the Veteran’s Health Administration (VHA).
The release notes provide a brief description of the new features and functions of the Outpatient Pharmacy Clinical Indicator Data Capture (CIDC) project which is provided in Patch PSO\*7.0\*143.
Outpatient Pharmacy Version 7.0 relies (minimum) on the following external packages. The following software is not included in this package and must be installed before this version of Outpatient Pharmacy is completely functional.
|                                                               |                            |
|---------------------------------------------------------------|----------------------------|
| Package                                                   | Minimum Version Needed |
| Accounts Receivable (AR)                                      | 4.5                        |
| Adverse Reaction Tracking (ART)                               | 4.0                        |
| Clinical Information Resources Network (CIRN)                 | 1.0                        |
| Consolidated Mail Outpatient Pharmacy (CMOP)                  | 2.0                        |
| Computerized Patient Record System (CPRS)                     | 25                         |
| Decision Support System (DSS)                                 | 3.0                        |
| Fee Basis                                                     | 3.5                        |
| VA FileMan                                                    | 22.0                       |
| Integrated Funds Control, Accounting, and Procurement (IFCAP) | 5.0                        |
| Inpatient Medications                                         | 5.0                        |
| Integrated Billing (IB)                                       | 2.0                        |
| Kernel                                                        | 8.0                        |
| Laboratory                                                    | 5.2                        |
| MailMan                                                       | 7.1                        |
| Master Patient Index/Patient Demographics (MPI/PD)            | 1.0                        |
| National Drug File (NDF)                                      | 4.0                        |
| Order Entry/Results Reporting (OERR)                          | 3.0                        |
| Patient Information Management System (PIMS)                  | 5.3                        |
| Pharmacy Data Management (PDM)                                | 1.0                        |
| Remote Procedure Call (RPC) Broker                            | 1.1                        |
*(This page included for two-sided copying.)*

# New Features, Functions, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>ICD-9 Diagnosis Prompts</u>

Outpatient Pharmacy will allow entry for one primary ICD-9 Diagnosis Code and up to seven secondary ICD-9 Diagnosis Codes. This ICD-9 Diagnosis Code prompts appear after the drug or orderable item prompt. For edited, copied, finished, and accepted orders from OERR, ICD-9 Diagnosis Codes may be edited by selecting the drug or orderable item. Any previously entered information appears as default answers. The user may enter a valid ICD-9 Diagnosis Code, or a look up may be performed by entering a partial diagnosis name or partial ICD-9 Diagnosis Code number.

Along with the PROVIDER key, the VistA Outpatient Pharmacy application evaluates the IBB CIDC Insurance Switch API (CIDC^IBBAPI) to determine if CIDC prompts appear, allowing the sites to choose whether to collect, or not collect CIDC data.

- A “YES” value returned by the IBB CIDC Insurance Switch API indicates the CIDC prompts will appear in the Outpatient Pharmacy application. When a ‘YES’ value is returned and the user holds the PROVIDER key, the ICD-9 Diagnosis Code prompts appear. User response to CIDC prompts is optional. If at least one ICD-9 Diagnosis Code is not entered and the nature of order is verbal or telephone, a CPRS alert will be queued to request electronic signature (e-sig) from the ordering provider and entry of the ICD-9 diagnosis information. The CPRS alert can be processed in the CPRS GUI or VistA application. If processed in the GUI, ICDs are required. If processed in VistA, only an electronic signature is required.
- If the IBB CIDC Insurance Switch API returns a ‘NO’ value, and regardless of whether the user holds the PROVIDER key, the ICD-9 Diagnosis Code prompts do not appear. In this instance, no alerts will be generated except in the case of legacy functionality where an electronic signature is required based on the nature of order being defined as verbal or telephone. Alerts generated in this manner may be processed by the ordering provider in the same manner stated previously.

Sample screen:

Patient Information Mar 23, 2004@10:14:45 Page: 1 of 2

OPPATIENT,ONE \<A\>

PID: 000-123-4567 Ht(cm): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

DOB: MAY 16,1958 (45) Wt(kg): \_\_\_\_\_\_\_ (\_\_\_\_\_\_)

SEX: MALE

Eligibility: SC LESS THAN 50% SC%: 10

Disabilities: BACK STRAIN-10% (SC), UPPER ARM CONDITION-0% (SC),

CONDITION OF THE SKELETAL SYSTEM-0% (SC),

12345 MADISON AVE

LARGO PHONE: 555-123-4567

FLORIDA 33773-1112

Prescription Mail Delivery: Regular Mail

Allergies

Verified: THEOPHYLLINE,

\+ Enter ?? for more actions

EA Enter/Edit Allergy/ADR Data PU Patient Record Update

DD Detailed Allergy/ADR List EX Exit Patient List

Select Action: Next Screen//

Select Primary ICD-9 Code: neuropathy

1 NEUROPATHY 337.1 AUT NEUROPTHY IN OTH DIS

2 NEUROPATHY 356.2 HERED SENSORY NEUROPATHY

3 NEUROPATHY 356.8 IDIO PERIPH NEURPTHY NEC

4 NEUROPATHY 356.9 IDIO PERIPH NEURPTHY NOS

5 NEUROPATHY 377.33 NUTRITION OPTC NEUROPTHY

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 3 356.8 IDIO PERIPH NEURPTHY NEC

Select Secondary ICD-9 Code: diabetes

1 DIABETES 250.01 DIABETES MELLI W/0 COMP TYP I COMPLICATION/COMORBIDITY

2 DIABETES 250.11 DIABETES W KETOACIDOSIS TYPE I COMPLICATION/COMORBIDITY

3 DIABETES 250.21 DIABETES W HYPEROSMOLAR TYPE I COMPLICATION/COMORBIDITY

4 DIABETES 250.31 DIABETES W OTHER COMA TYPE I COMPLICATION/COMORBIDITY

5 DIABETES 250.41 DIABETES W RENAL MANIFES TYP I COMPLICATION/COMORBIDITY

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5:

<u>  
Service Connected and Environmental Indicator Prompts</u>

Based on the patient’s registration/enrollment information, the user will be prompted for Service Connected (SC) and Environmental Indicator (EI) data for all patients including those greater than 50% service connected and regardless of co-payment status. The co-payment charge is not affected and remains as legacy functionality where SC\>50% are not charged a copay. Also, the SC/EI questions are always asked regardless of whether the Clinical Indicators (ICD-9 Diagnosis Codes) are entered, and there is no distinction between provider and non-provider.

The application displays the patient’s Service Connected (SC) and rated disabilities as they are entered in the Enrollment package.

Example:

SC Percent: 40%

Rated Disabilities: IMPAIRMENT OF FEMUR (30%-SC)

THIGH MUSCLE INJURY (10%-SC)

If the user copies, changes or renews an order, the Clinical Order (ICD-9 Diagnosis Code(s)), SC and EI prompts will default to those entered in the original order. This allows the user access to this information and the ability to change orders when necessary.

The mandatory entry of SC and EI information is “grand fathered” in for Outpatient Pharmacy for all users, and shall not be changed. The SC question will be prompted first before the Environmental Indicators questions in the following order:

> a\. Was treatment for a Service Connected condition?

> b\. Was treatment related to Combat?

> c\. Was treatment related to Agent Orange exposure?

> d\. Was treatment related to Ionizing Radiation exposure?

> e\. Was treatment related to Environmental Contaminant exposure?

> f\. Was treatment related to Military Sexual Trauma?

> g\. Was treatment related to Head and/or Neck Cancer?

Sample screen:

Rx \# 4149271 03/23/04

OPPATIENT,ONE \#1

TAKE ONE TABLET BY MOUTH A

PREDNISONE 1MG TAB

OPPROVIDER,ONE Pharmacist

\# of Refills: 0

SC Percent: 100%

Disabilities:

TRAUMATIC ARTHRITIS 10% - SERVICE CONNECTED

DIABETES MELLITUS 0% - SERVICE CONNECTED

Was treatment for a Service Connected condition? yes YES

Was treatment related to Combat? yes YES

Was treatment related to Agent Orange exposure? yes YES

Was treatment related to Ionizing Radiation exposure? no NO

Was treatment related to Environmental Contaminant exposure? yes YES

Was treatment related to Military Sexual Trauma? no NO

Was treatment related to Head and/or Neck Cancer? no NO

Is this correct? YES//

<u>Ordering/Referring Provider</u>

The user will continue to be prompted for the mandatory ordering/referring information prompt and it will be stored in the Outpatient Pharmacy application. The ORDERING/REFERRING PROVIDER information will be validated from the New Person file (#200) to insure physician type.

Sample screen:

DAYS SUPPLY: (1-90): 30// \<Enter\>

QTY ( TAB ) : 10// 10

COPIES: 1// 1

\# OF REFILLS: (0-5): 5// \<Enter\>

PROVIDER: OPPROVIDER,ONE // TESTING ONLY

CLINIC: 4D-104 DIAB ED CL NEW DX Replace

# Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are impacted by the added features discussed in Section 2 of this document unless otherwise stated in this section.

Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\] option

- Functions Affected:
  - New Order
  - Edit
  - Finish
  - Renew
  - Copy
  - Edit within Verification

Complete Orders From Oerr \[PSO LMOE FINISH\] option

- Functions Affected:
  - Finish
  - Edit

Reset Copay Status/Cancel Charges \[PSOCP RESET COPAY STATUS\] option

When the exemption flags (e.g., Service Connection/Environmental Indicators) are edited, the updated answers are associated and stored with any ICD-9 Diagnosis Codes defined on the new ICD node for the prescription being modified. This occurs in the background. This option is not impacted by the ICD-9 Diagnosis entry features from Section 2 of this document.

# Reports and Profiles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No modifications were made.

*(This page included for two-sided copying.)*

# Files and Fields 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>PRESCRIPTION file (#52)</u>

ICD DIAGNOSIS Multiple (#52311)

This multiple field has been added to store up to eight ICD-9 Diagnosis Codes, as well as the associated SC/EIs. The first ICD-9 code stored is always the Primary diagnosis.

<u>ICD DIAGNOSIS FILE (#80)</u>

This file is referenced for validating user entry of ICD-9 codes only and no edits/additions/or deletions are made to this file.

<u>PENDING OUTPATIENT ORDERS File (#52.41)</u>

ICD CODE Multiple field (#311)

The PENDING OUTPATIENT ORDERS file (#52.41) will be modified to include a new multiple field to store up to eight pointers (the first being the primary Diagnosis Code) and all of the associated SC/EI information for each order. This new field will be called ICD CODE MULTIPLE field (#311) and will be populated as part of CPRS order processing.

# Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Application Program Interface (API) Modification/Addition</u>

Usage of the Scheduling API (SDCO22) will facilitate the process by which all Service Connected (SC) and Environmental Indicator (EI) questions defined for the patient in the Enrollment package will be asked in Outpatient Pharmacy.

A new API was added between CPRS and Outpatient Pharmacy (PSOHLNE3). This API is called by CPRS when SC/EI/ICDs are edited in the CPRS GUI as part of the electronic signature (e-sig) process. Only the SC/EI/ICD fields in the Prescription file (#52) are updated using this new API. Any previously entered ICD/SC/EI data entered will be over written. Also, if the copay status has changed from copay to no copay and the prescription has been released, the copay charges are automatically cancelled in the background. All prescriptions with a copay change will always state RX EDITED in the copay activity log and will reflect the user name that made the change in the CPRS GUI. No additional action is taken if the copay status is changed from no copay to copay.

<span id="_Toc510894276" class="anchor"></span>A new IBB CIDC Insurance Switch API (CIDC^IBBAPI) was added to check the CIDC on/off switch and to validate the existence of third-party insurance. If the API returns a 1 (yes) and the user holds the PROVIDER key, the ICD-9 Diagnosis Code prompts appear. Otherwise, the ICD-9 Diagnosis Code prompts do not appear.

# Impacts to Other Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In some instances, Outpatient Pharmacy provides OERR with the SC/EI information to prompt the user for those answers within the ListMan functions. Service connection percentages through 100% are provided.

*(This page included for two-sided copying.)*