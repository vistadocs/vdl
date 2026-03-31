---
title: PSO*7*612 Clozapine NCCC Override Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Clozapine NCCC Override
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*612
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - clozapine
  - patient
  - override
  - nccc
  - table
  - contents
  - pharmacy
  - number
  - release
  - authorization
page_count: 0
word_count: 1145
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_p612_ys_501_p166_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_p612_ys_501_p166_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Health Integration & Modernization (HI&M)

  Clozapine National Clozapine Coordinating Center (NCCC) Override Covid-19

  Release Notes

  Outpatient Pharmacy - PSO\*7.0\*612

  Mental Health - YS\*5.01\*166

  Inpatient Medications - PSJ\*5\*403

  ![](pso-7-612-clozapine-nccc-override-release-notes/001.png)
---

August 2020

Office of Information and Technology (OI&T)

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [This Release](#this-release)
  - [New Features and Functions Added](#new-features-and-functions-added)
  - [Enhancements and Modifications to Existing Functionality](#enhancements-and-modifications-to-existing-functionality)
  - [Known Issues](#known-issues)
- [Product Documentation](#product-documentation)
The HI&M Clozapine NCCC OVRD COVID-19 multi-build is a bundle of emergency patches to the National Clozapine Registry (NCR) software to correct defects to National Clozapine Coordinating Center (NCCC) Override functionality. The multi-build contains Mental Health patch YS\*5.01\*166 and Outpatient Pharmacy patch PSO\*7.0\*612 and is also being released with informational patch PSJ\*5\*403.
The NCR is maintained by the NCCC. The NCCC is responsible for the VA's compliance with the clozapine Risk Evaluation and Mitigation Strategy (REMS), which is mandated by the Food and Drug Administration (FDA) for tracking clozapine patients. 

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to Clozapine NCCC Override COVID-19 (consisting of patches PSO\*7.0\*612, YS\*5.01\*166, and informational patch PSJ\*5.0\*403) for this release.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document targets users and administrators of the National Clozapine Coordinating Center (NCCC), VistA Pharmacy applications, and the Vista Mental Health application. This document applies to the incremental changes made between this release and any previous release for this software.

# This Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide a summary of the new features and functions added, enhancements and modifications to the existing software, and any known issues for Clozapine NCCC Override COVID-19, consisting of patches PSO\*7.0\*612, YS\*5.01\*166, and informational patch PSJ\*5.0\*403.<span id="_Toc45605771" class="anchor"></span>

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the new features and functions added to the Clozapine NCCC Override COVID-19 release, consisting of patches PSO\*7.0\*612, YS\*5.01\*166, and informational patch PSJ\*5.0\*403.

Automate Clozapine Registration

When a new NCCC clozapine authorization number is received at the VA Medical Center and processed by the Mental Health V.5.01 application, a new process shall automatically register the new clozapine authorization number to the appropriate patient and set the clozapine status to active.

Patch PSO\*7.0\*612 - Automate Clozapine Registration API

- New Outpatient Pharmacy Application Programmer Interface (API) routine PSOCLADD was created to accept a patient identifier (DFN) and a NCCC clozapine authorization number and registers the clozapine number into the CLOZAPINE REGISTRATION NUMBER field (#53) in the PHARMACY PATIENT file (#55) for the specific patient and updates the CLOZAPINE STATUS field (#54) to 'A' for Active.
- After successfully registering the new clozapine authorization number to the patient, the new API removes any ^XTMP global associated with local clozapine overrides for the patient. This prevents an obsolete local override from interfering with the patient’s regular clozapine dispense frequency for new clozapine pharmacy orders.

Patch YS\*5.01\*166 - Automate Clozapine Registration Action Index

- Added Mumps Action Index to the CLOZAPINE PATIENT LIST file (#603.01) that invokes Outpatient Pharmacy Application Programmer Interface (API) routine PSOCLADD when a new clozapine authorization number is filed. This automates the clozapine patient registration process by automatically registering the patient when the clozapine authorization number is received from NCCC.

## Enhancements and Modifications to Existing Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the enhancements and modifications to the Clozapine NCCC Override COVID-19 release, consisting of patches PSO\*7.0\*612, YS\*5.01\*166 and informational patch PSJ\*5.0\*403.

Defect Addressed - INC9951972: COVID-19 VistA PSO defect - Clozapine National Override patient's prescription limited to 4 days. 

The following functionality was modified to resolve defect INC9951972:

- Outpatient Pharmacy v.7.0 calculation of days supply for outpatient clozapine orders.
- Inpatient Medications v.5.0 calculation of default stop date for inpatient clozapine orders. This change was made indirectly via an Application Programmer Interface (API).
- Computerized Patient Record System (CPRS) v.3.0 calculation of days supply for outpatient clozapine orders. This change was made indirectly via a Remote Procedure Call (RPC).

Patch PSO\*7.0\*612 changes to resolve defect INC9951972:

- A change was made to the Register Clozapine Patient \[PSOL REGISTER PATIENT\] option in the Clozapine Pharmacy Manager \[PSOL MANAGER\] menu to correct the lookup by patient into the CLOZAPINE PATIENT LIST file (#603.01) to allow selection of a patient with more than one clozapine authorization number on file.
- A change was made to correct the way a patient’s clozapine dispense frequency is retrieved by first checking the PHARMACY PATIENT file (#55) for the patient's active clozapine authorization number before searching the DISPENSE FREQUENCY field (#3) of the CLOZAPINE PATIENT LIST file (#603.01).
- A change was made to pharmacy order entry routines to remove the ^XTMP global record associated with the patient's local override when an active NCCC clozapine registration and valid clozapine lab results exist. This prevents an obsolete local override from interfering with the patient's regular clozapine dispense frequency for new clozapine pharmacy orders.
- A change was made to clozapine patient registration process to remove the ^XTMP global associated with the patient’s local override at the time a new NCCC clozapine authorization number is registered to the patient using the Register Clozapine Patient \[PSOL REGISTER PATIENT\] option in the Clozapine Pharmacy Manager \[PSOL MANAGER\] menu. This prevents an obsolete local override from interfering with the patient’s regular clozapine dispense frequency for new clozapine pharmacy orders.

Patch YS\*5.01\*166 changes to resolve defect INC9951972:

- A change was made to the clozapine server process responsible for filing NCCC clozapine override dates into the OVERRIDE DATE field (#3) in the CLOZAPINE PATIENT LIST file (#603.01). Previously, no clozapine authorization number match was found for the incoming clozapine authorization number when there were multiple clozapine numbers associated with the patient. This defect was corrected by searching all clozapine authorization numbers associated with the patient to find a match for the incoming clozapine authorization number, enabling the NCCC override date to file properly.
- A change was made to the clozapine server process responsible for filing NCCC clozapine override dates into the OVERRIDE DATE field (#3) in the CLOZAPINE PATIENT LIST file (#603.01) to remove the ^XTMP global associated with the patient’s local override at the time an NCCC override is successfully filed. This prevents an obsolete local override from interfering with the patient's regular clozapine dispense frequency for new clozapine pharmacy orders.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known issues specific to this release.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents apply to this release:

| Description                                                                      | File Name                   |
|--------------------------------------------------------------------------------------|---------------------------------|
| Outpatient Pharmacy (PSO) Technical Manual/Security Guide                            | pso_7_0_p612_tm.docx            |
| Outpatient Pharmacy (PSO) Manager’s User Manual                                      | pso_7_0_p612_man_um.docx        |
| Mental Health and Mental Health Assistant Version 3 Technical Manual/ Security Guide | YS_MHA_TM.pdf                   |
| Deployment, Installation, Back-out, and Rollback Guide                               | pso_7_p612_ys_501_p166_dibr.pdf |

Documentation can be found on the VA Software Documentation Library at: [<u>https://www.va.gov/vdl/</u>](https://www.va.gov/vdl/).

Documentation can also be obtained at <https://download.vista.med.va.gov/index.html/SOFTWARE>.