---
title: PSJ*5*253/254 Release Notes-Allergy and Alerts
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Allergy and Alerts
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*253
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document provides a brief description of new features of the Allergy and Alerts for Inpatient Medications V.5.0 project for patches PSJ\5\253 and PSJ\5\254.
audience: 
keywords: 
  - order
  - table
  - contents
  - current
  - provider
  - inpatient
  - interventions
  - cprs
  - drug
  - overrides
page_count: 0
word_count: 790
section_count: 5
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p253_p254_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p253_p254_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

![](psj-5-253-254-release-notes-allergy-and-alerts/001.png)

Inpatient Medications

Allergy and ALERTS

Release Notes

PSJ\*5\*253, PSJ\*5\*254

January 2012

Product Development

Table of Contents

# *(This page included for two-sided copying.)*


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [Introduction](#introduction)
- [PSJ\5\253](#psj5253)
  - [Features](#features)
- [PSJ\5\254](#psj5254)
  - [Enhancements](#enhancements)
- [Additional Information](#additional-information)
  - [New Application Program Interface (API) provided to BCMA](#new-application-program-interface-api-provided-to-bcma)
  - [Inpatient Medications Custodial Integration Agreements](#inpatient-medications-custodial-integration-agreements)
- [Hardware Interfaces](#hardware-interfaces)
- [Software Interfaces](#software-interfaces)
- [User Documentation](#user-documentation)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document provides a brief description of new features of the Allergy and Alerts for Inpatient Medications V.5.0 project for patches PSJ\*5\*253 and PSJ\*5\*254.

# PSJ\*5\*253

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: PSJ\*5\*225 and PSJ\*5\*245 must be installed before PSJ\*5\*253.

> IMPORTANT: Patches PSJ\*5\*254 and PSB\*3\*58 must be installed immediately after installation of this patch. Patch PSB\*3\*58 contains changes that will not function until patch PSJ\*5\*254 is installed. The following patches should be installed at the same time, in the following sequence:

> PSJ\*5\*253, PSJ\*5\*254, PSB\*3\*58

## Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Corrects an issue in Bar Code Medication Administration (BCMA) V. 3.0, in which orders do not display on the Virtual Due List (VDL) if the order's Schedule Type is Continuous or Fill on Request, and the order contains a Schedule defined in the Administration Schedule File (#51.1) with a Schedule Type of On Call.
- Corrects an issue in Inpatient Medications V. 5.0, in which changing a Non-Verified order's Schedule Type to On Call automatically changes the name of the order's Schedule to On Call without alerting the user.

############################### Associated Files and Fields

| Files                       | Fields             | New/Modified/Deleted |
|-----------------------------|--------------------|----------------------|
| Non-Verified Orders (#53.1) | Schedule Type (#7) | Modified             |

############################### Patient Safety Issues

| Issue    | Problem                                        |
|----------|------------------------------------------------|
| PSPO1765 | ON CALL, FILL on REQUEST does not show in BCMA |

############################### Remedy Tickets

| Remedy Ticket | Problem                                                         | Resolution                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HD415492      | ON CALL, FILL on REQUEST does not show in BCMA.                 | Inpatient Medications will send orders to BCMA as schedule type “ON CALL” if the order contains a schedule that is defined in the Administration Schedule File (#51.1) as type “ON CALL,” and the order itself has a schedule type of “Continuous” or “Fill on Request.” If the order has a schedule type of “ONE TIME,” “PRN,” or “ON CALL,” the order's schedule type will always determine the type displayed in BCMA. |
| HD414275      | Schedule is Automatically Converted if Schedule Type is On Call | The code performing the automatic change of an order's Schedule will be removed. The fix for HD415492 in this patch removes the requirement for a Continuous or Fill on Request order's schedule to be equal to “ON CALL” for the order to display as an On Call order in BCMA.                                                                                                                                           |

# PSJ\*5\*254

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: PSJ\*5\*181, PSJ\*5\*209, PSJ\*5\*225, PSJ\*5\*241, and PSJ\*5\*253 must be installed before PSJ\*5\*254.

> IMPORTANT: Patch PSB\*3\*58 must be installed immediately after the installation of this patch. Patch PSJ\*5\*253 must be installed immediately before this patch.

> Patch PSB\*3\*58 contains changes that will not function until patch PSJ\*5\*254 is installed. The following patches should be installed at the same time, in the following sequence:

> PSJ\*5\*253, PSJ\*5\*254, PSB\*3\*58

> WARNING: If your facility has the Pyxis/Omnicell/McKesson interface from Informatix Laboratory Corporation (ILC), this patch will overwrite any local modifications in routines PSGOEE and PSGOETO. This could affect certain orders being sent across this interface. The modifications will have to be reintroduced following installation of this patch.

> Patch PSJ\*5\*254 adds functionality in Inpatient Medications that retrieves and displays Computerized Patient Record System (CPRS) V. 1.0 provider override reasons and the order checks that were overridden, as well as pharmacist intervention information from Inpatient Medications V.5.0 when at least one overridden critical drug-drug interaction and/or allergy/Adverse Drug Reaction (ADR) interaction is associated with an Inpatient order. An Application Programming Interface (API) has also been added to supply this information to BCMA V. 3.0.

## Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Functionality has been implemented to utilize the Order Check Instances (#100.05) file to retrieve and display CPRS provider override reasons and the order checks that were overridden when at least one critical drug-drug interaction and/or allergy/ADR interaction is associated with an Inpatient order.
- When a user selects 9 OTHER at the Intervention Recommendation prompt, the Other For Recommendation word processing field becomes available for unlimited user input. The “OTHER FOR RECOMMENDATION” word processing field is best used for the Pharmacist reason for overriding the order check(s). For critical drug-drug and allergy/ADR interactions, this information will display when the OCI ‘Hidden Action’ is used in Inpatient Medications. It will also be available for the nurse to view in the BCMA Display Order detail report.
- Added an Order Checks/Interventions indicator “\<OCI\>” to denote a current CPRS provider override or current pharmacy intervention of at least one critical drug-drug interaction and/or allergy/ADR interaction exists for the current order.
- Added an "OCI" hidden action to display current and historical CPRS provider overrides and pharmacist interventions associated with an order. If Historical Overrides/Interventions exist for an order, the user is prompted to display them.
- The following describes when Provider Overrides and Pharmacist Interventions are displayed:
- When finishing an order, if current CPRS Order Checks/Provider Overrides exist, they automatically display.
- When editing a field marked with an asterisk (\*), (except when editing the orderable item) if current CPRS Provider Overrides and/or Pharmacy Interventions exist for the order, the user will be prompted to display them.
- When editing an orderable item in Inpatient Medications, if current CPRS Provider Overrides and/or Pharmacist Interventions exist for the order, the user will be prompted to display them. If the orderable item is changed, new order checks are performed, and upon accepting the order, the current overrides/interventions are moved to historical.
- When renewing an order, if current CPRS Provider Overrides and/or Pharmacy Interventions exist for the order, the user will be prompted to display them.
- CPRS Provider Override information displays as follows:

> Heading information

> A summary of the Current CPRS Order Checks overridden by the Provider

> Overriding Provider, plus title

> Override Entered By, plus title

> Date/Time Entered

> Override Reason.

- Pharmacist Intervention information displays as follows:

> Heading

> Intervention Date/Time

> Provider

> Pharmacist

> Drug

> Instituted By

> Intervention

> Recommendation

> Originating Package

> If populated, the following Pharmacist Intervention information also displays:

> Was Provider Contacted

> Provider Contacted

> Recommendation Accepted

> Agree With Provider

> Rx \#

> Division

> Financial Cost

> Other For Intervention

> Other For Recommendation

> Reason For Intervention

> Action Taken

> Clinical Impact

> Financial Impact

- The OCI indicator and hidden action have been added to the Detailed Order List Manager screens when utilizing the following options:
  - Inpatient Order Entry \[PSJ OE\]
  - Non-Verified/Pending Orders \[PSJU VBW\]
  - Order Entry \[PSJU NE\]
  - Order Entry (IV) \[PSJI ORDER\]
- Created a link from the Order file to current and historical interventions created in response to critical drug-drug and/or Allergy/ADR interactions.
- Created a flag that will enable the display of an indicator on the BCMA VDL and send the current Provider Override and Pharmacist Intervention information to BCMA.

############################### Associated Files and Fields

| Files                       | Fields                                        | New/Modified/Deleted |
|-----------------------------|-----------------------------------------------|----------------------|
| Non-Verified Orders (#53.1) | Schedule Type (#7)                            | Modified             |
| Pharmacy Patient (#55)      | Unit Dose (#62)(Multiple) Intervention (#132) | Modified             |
|                             | IV (#100) (Multiple) Intervention (#153)      | Modified             |

############################### New Field Details

| Field Name                                                                                                                                    | Field Description                                                                                                                                                                                      |
|-----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INTERVENTION multiple in NON-VERIFIED ORDERS (#53.1) file                                                                                     | Interventions logged during Inpatient Order Entry in response to drug-drug or drug-allergy order checks. Only interventions associated with a specific Inpatient Order will be stored with that order. |
| INTERVENTION (#.01) field in INTERVENTION (#130) multiple in NON-VERIFIED ORDERS (#53.1) file                                                 | Pointer to Pharmacy INTERVENTION (#9009032.4) file                                                                                                                                                     |
| INTERVENTION (#132) multiple in the UNIT DOSE (#62) multiple in the PHARMACY PATIENT (#55) file                                               | Pointer to APSP INTERVENTION (#9009032.4) file                                                                                                                                                         |
| INTERVENTION (#.01) field in the INTERVENTION (#132) multiple in the UNIT DOSE (#62) multiple in the NON-VERIFIED ORDERS (#53.1) file         | Pointer to APSP Intervention (#9009032.4) file                                                                                                                                                         |
| INTERVENTION DATE/TIME (#1) field in the INTERVENTION (#132) multiple in the UNIT DOSE (#62) multiple in the NON-VERIFIED ORDERS (#53.1) file | INTERVENTION DATE/TIME                                                                                                                                                                                 |
| INTERVENTION (#153) multiple in the IV (#100) multiple in the PHARMACY PATIENT (#55) file                                                     | Pharmacy Interventions associated with the Inpatient order.                                                                                                                                            |
| INTERVENTION (#.01) field in the INTERVENTION (#153) multiple in the IV (#100) multiple in the PHARMACY PATIENT (#55) file                    | Pointer to APSP INTERVENTION (#9009032.4) file                                                                                                                                                         |
| INTERVENTION DATE/TIME (#1) field in the INTERVENTION (#153) multiple in the IV (#100) multiple in the PHARMACY PATIENT (#55) file            | The Date/Time the Intervention was logged in response to Order Checks that occurred during Inpatient Order Entry.                                                                                      |

# Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Application Program Interface (API) provided to BCMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PSGSICH1 - The entry point GETPROVL^PSGSICH1 is provided by the Inpatient Medications package to return CPRS Provider Overrides associated with a specific Inpatient Medications order. Entry point INTRDIC^PSGSICH1 is provided by the Inpatient Medications package to return Pharmacist Interventions associated with a specific Inpatient Medications order.

## Inpatient Medications Custodial Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 5653 NAME: RETURN CPRS ORDER CHECKS AND OVERRIDES TO BCMA

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

> SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: GETPROVL^PSGSICH1

> 5654 NAME: INPATIENT INTERVENTIONS TO BCMA

> CUSTODIAL PACKAGE: INPATIENT MEDICATIONS Birmingham

> SUBSCRIBING PACKAGE: BAR CODE MED ADMIN Birmingham

> ROUTINE: INTRDIC^PSGSICH1

# Hardware Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Inpatient Medications interfaces directly with printers for labels and reports.

> Inpatient Medications functions on the following standard server platforms used in VA Medical Center (VAMC)s:

- Open M V. 4.0 route 43 and MS Windows 2000, NT, XP and VMS

# Software Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Inpatient Medications requires the following versions (or higher) of VA software packages for proper implementation. The software listed in the table below is not included in this build and must be installed for the build to be completely functional.

| Package              | Version |
|--------------------------|-------------|
| BCMA                     | 3.0         |
| Inpatient Medications    | 5.0         |
| Kernel                   | 8.0         |
| MailMan                  | 8.0         |
| Nursing                  | 4.0         |
| CPRS                     | 1.0         |
| Pharmacy Data Management | 1.0         |
| RPC Broker (32-bit)      | 1.1         |
| Toolkit                  | 7.3         |
| VA FileMan               | 22.0        |
| Vitals/Measurements      | 5.0         |

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> User documentation for Inpatient Medications V.5.0 provides detailed information on the functionality, and can be found on the [VistA Document Library](http://www.va.gov/vdl/application.asp?appid=88) (VDL). Inpatient Medications documents available are listed below:

> Nurse's User Manual

> Nurse's User Manual Change Pages

> Pharmacist's User Manual V. 5.0

> Pharmacist's User Manual Change Pages

> Technical Manual/Security Guide V. 5.0

> Technical Manual/Security Guide Change Pages

> Release Notes