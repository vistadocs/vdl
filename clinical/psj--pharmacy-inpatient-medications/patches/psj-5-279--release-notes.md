---
title: PSJ*5*279 Release Notes-IV Bag Logic/Infusion Rate T@0
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: IV Bag Logic/Infusion Rate T@0
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*279
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document provides a brief description of new features of the IV Bag Logic/Infusion Rate T@0 for Inpatient Medications V.5.0 project for patch PSJ\5\279.
audience: 
keywords: 
  - table
  - contents
  - order
  - labels
  - associated
  - orders
  - inpatient
  - resolved
  - manual
  - rate
page_count: 0
word_count: 810
section_count: 1
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p279_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p279_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

![](psj-5-279-release-notes-iv-bag-logic-infusion-rate-t-0/001.png)

Inpatient Medications

Release Notes

PSJ\*5\*279

Product Development

Table of Contents

# *(This page included for two-sided copying.)*


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [(This page included for two-sided copying.)](#this-page-included-for-two-sided-copying)
- [Introduction](#introduction)
- [Enhancements](#enhancements)
- [Menu Options](#menu-options)
- [New Fields](#new-fields)
- [Modified Fields](#modified-fields)
- [Associated Protocols](#associated-protocols)
- [Associated Mail Groups](#associated-mail-groups)
- [User Documentation](#user-documentation)
- [New Service Requests Tickets Resolved](#new-service-requests-tickets-resolved)
- [Patient Safety Issues Resolved](#patient-safety-issues-resolved)
- [Remedy Tickets Satisfied](#remedy-tickets-satisfied)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document provides a brief description of new features of the IV Bag Logic/Infusion Rate T@0 for Inpatient Medications V.5.0 project for patch PSJ\*5\*279.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The scope of the Clinic Order project is to provide software modifications to enhance the Pharmacy Inpatient Medications application to support the following functionality:

- Modified Inpatient Medications APIs allowing active clinic orders with the clinic name to be sent to the Bar Code Medication Administration (BCMA) software.
- Modified inpatient order entry so that when inpatient orders are edited, BCMA IV parameters are checked to determine if IV labels were invalidated as a result of the edit. If so, the authorized pharmacy user making the edit is informed, and a list of the invalidated IV labels is displayed. The authorized pharmacy user is given an opportunity to print replacement labels, including when no new order is created as a result of the edit.
- A new field, entitled Labels per Day, used to define the number of daily labels needed for a continuous IV order when different than the number of labels the system would have calculated based on the order’s volume and infusion rate added. The Labels per Day field is accessible in Inpatient Order Entry via the Infusion Rate field. The Labels per Day prompt displays immediately after the prompt for Infusion Rate.

> Previously released functionality allowing the entry of the number of labels directly into the Infusion Rate field via the “@” character (125@1) is retained. The number of labels entered after the “@” character automatically populates the Labels per Day field. However, the use of the “@” character for intermittent IV orders is not allowed.

> Note: While a patient is admitted to an Inpatient Ward, the Ward location will print on the patient’s IV labels, regardless of where the order originated. Clinic locations will only print on IV labels if patient is not admitted to an inpatient location and the order is associated with a clinic location.

- Modified version of the pre-exchange report allowing pre-exchange reports to be printed to devices associated with each clinic added. A new PRE-EXCHANGE REPORT DEVICE (#5) field added to the CLINIC DEFINITION (#53.46) file. The field, if populated, contains a device that will be the default print device at the “Select DEVICE for PRE-EXCHANGE UNITS REPORT:” prompt that displays after a Unit Dose order is verified.
- A new Graphical User Interface (GUI) executable file added. Installation of this GUI is required immediately after the KIDS install for the patch to function.

> **NOTE:** The following patches must be installed BEFORE PSJ\*5\*279:

- PSJ\*5\*228
- PSJ\*5\*229
- PSJ\*5\*247
- PSJ\*5\*258
- PSJ\*5\*275
- PSS\*1\*172

> **NOTE:** IMR VI Clinic Orders, Witness for High Risk/High Alert Drugs and IV Bag Logic Enhancement includes 5 patches which must be installed in the following order:

- PSS\*1\*172
- PSJ\*5\*279
- OR\*3\*266
- PSB\*3\*70
- PSB\*3\*73

# Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following existing menu options to the patient medication profile were enhanced to allow active clinic orders with the clinic names to be sent to BCMA:

- *Inpatient Order Entry* \[PSJ OE\]
- *Non*-[*Verified/Pending Orders* \[PSJU VBW\]](#PSJJU)
- *Order Entry (IV)* \[PSJI ORDER\]

# New Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following new field was added to NON-VERIFIED ORDERS (#53.1) file:

- LABELS PER DAY

> The following new fields were added to the CLINIC DEFINITON (#53.46) file:

- MISSING DOSE PRINTER
- PRE-EXCHANGE REPORT DEVICE

# Modified Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following field in the NON-VERIFIED ORDERS (#53.1) file was modified:

- INFUSION RATE

# Associated Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following protocols are associated with this patch:

- PSJ LM FINISH
- PSJU LM COPY

# Associated Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Mail Group is associated with this patch:

- PSJ CLINIC DEFINITION

# User Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> User documentation for Inpatient Medications V.5.0 provides detailed information on the functionality and can be found on the [VistA Document Library](http://www.va.gov/vdl/application.asp?appid=88) (VDL). Inpatient Medications documents available are listed below:

- Nurse's User Manual, PSJ_5_NURSE_UM_R1213.pdf
- Nurse's User Manual Change Pages, PSJ_5_P279_NURSE_UM_CP.pdf
- Pharmacist's User Manual V. 5.0, PSJ_5_PHAR_UM_R1213.pdf
- Pharmacist's User Manual Change Pages, PSJ_5_P279_PHAR_UM_CP.pdf
- Supervisor’s User Manual V.5.0, PSJ_5_SUPR_UM_R1213.pdf
- Supervisor’s User Manual Change Pages, PSJ_5_P279_SUPR_UM_CP.pdf
- Technical Manual/Security Guide V. 5.0, PSJ_5_TM_R1213.pdf
- Technical Manual/Security Guide Change Pages, PSJ_5_P279_TM_CP.pdf
- Release Notes, PSJ_5_P279_RN.pdf

# New Service Requests Tickets Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following New Service Requests are resolved with this patch:

- NSR 20010504 – Check for invalid bags, prompt to print new labels
- NSR 20070506 – Clinic Orders
- NSR 20090813 – Request separate area for IV label suppression information

# Patient Safety Issues Resolved

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Patient Safety Issues are resolved with this patch:

- PSPO 452 – Reported occurrence of patient receiving increased titration rate of morphine (HD173063).
- PSPO 1448 – Normal Saline is displaying on a Sodium Bicarbonate D5W order (HD322729, HD 278810, HD615239).
- PSPO 1855 – Inpatient Medication Orders for Outpatient orders (IMO) start date/time is the date/time of the appointment, which may not be accurate (HD178352).

# Remedy Tickets Satisfied

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HD173063 – Reported occurrence of patient receiving increased titration rate of morphine.
- HD178352 – Inpatient Medication Orders for Outpatient orders (IMO) start date/time is the date/time of the appointment, which may not be accurate.
- HD615239 – Normal Saline is displaying on a Sodium Bicarbonate D5W order.
- INC801240 – Technician entered non-verified IV order hangs.