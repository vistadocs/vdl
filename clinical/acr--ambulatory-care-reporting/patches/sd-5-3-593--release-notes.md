---
title: SD*5.3*593 ACR Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: ACR
app_name: Ambulatory Care Reporting
section: CLI
app_status: active
pkg_ns: SD
patch_ver: 5.3
patch_id: SD*5.3*593
group_key: "ACR:SD:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - report
  - date
  - diagnosis
  - table
  - contents
  - range
  - selection
  - code
  - codes
  - outpatient
page_count: 0
word_count: 2814
section_count: 18
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Ambulatory_Care_Reporting/acr_icd-10_rn_sd_5_3_593.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Ambulatory_Care_Reporting/acr_icd-10_rn_sd_5_3_593.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=116"
---

ICD-10 Follow On Class 1 Software Remediation Project

Ambulatory Care Reporting (ACR)

Release Notes

SD\*5.3\*593

![](sd-5-3-593-acr-release-notes/001.png)

August 2014

Office of Information and Technology

Product Development

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
  - [Documentation](#documentation)
  - [Dependencies](#dependencies)
- [ACRP Ad Hoc Report Option](#acrp-ad-hoc-report-option)
  - [Report Perspective – Diagnosis Selection](#report-perspective-diagnosis-selection)
  - [Report Limitations – Date Range Selection](#report-limitations-date-range-selection)
  - [Report Limitations – Diagnosis Selection](#report-limitations-diagnosis-selection)
  - [Report Limitations – Pre-Execution Date Diagnosis Check](#report-limitations-pre-execution-date-diagnosis-check)
- [Most Frequent 50 IP ICD Diagnosis Codes (IP7) / Most Frequent 50 ICD Diagnosis Codes (OP7)](#most-frequent-50-ip-icd-diagnosis-codes-ip7-most-frequent-50-icd-diagnosis-codes-op7)
- [Encounter Activity Report](#encounter-activity-report)
  - [Date Range Selection](#date-range-selection)
- [Outpatient Diagnosis/Procedure Frequency Report](#outpatient-diagnosisprocedure-frequency-report)
  - [Date Range Selection](#date-range-selection-1)
- [Outpatient Diagnosis/Procedure Code Search](#outpatient-diagnosisprocedure-code-search)
  - [Date Range Selection](#date-range-selection-2)
  - [Diagnosis Selection](#diagnosis-selection)
- [Ambulatory Care Nightly Transmission to NPCDB](#ambulatory-care-nightly-transmission-to-npcdb)
  - [HL7 Diagnosis Segment - DG1-2 & DG1-4](#hl7-diagnosis-segment-dg1-2-dg1-4)
  - [Error Code Display Text Update – ICD](#error-code-display-text-update-icd)
- [Technical Information](#technical-information)
  - [Integration Control Registration](#integration-control-registration)
  - [Data Dictionary Changes](#data-dictionary-changes)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements related to ICD-10 to the Ambulatory Care Reporting (ACR) package contained in patch SD\*5.3\*593.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 activation date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                 | ICD-10-CM                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Character 1 is alpha; character 2 is numeric;                                 |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                             |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                              |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1.                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character. |
| Decimal after first 2 characters | Does not contain decimals                                                                                                              |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patch SD\*5.3\*593 makes the following changes to the ACR application:

- Added modifications for the following reports:
  - ACRP Ad Hoc Report \[SCRPW AD HOC REPORT\], primarily within the Report Perspective and Report Limitations.
  - Most Frequent 50 IP ICD Diagnosis Codes (IP7) \[SCRPW DVM IP DX FREQUENCY\] and Most Frequent 50 ICD Diagnosis Codes (OP7) \[SCRPW DVM DX FREQUENCY\]
  - Encounter Activity Report \[SCRPW ENCOUNTER ACTIVITY RPT\] and Outpatient Diagnosis/Procedure Frequency Report \[SCRPW DX/CPT FREQUENCY REPORT\]
  - Outpatient Diagnosis/Procedure Code Search \[SCRPW DX/PROCEDURE CODE SEARCH\]
  - Encounter 'Action Required' Report \[SCRPW ACTION REQUIRED REPORT\]
  - Ambulatory Care Nightly Transmission to NPCDB \[SCDX AMBCAR NIGHTLY XMIT\]
- Updated field sizes of HL7 DG-1 segment for longer ICD-10 diagnosis description in the Ambulatory Care Nightly Transmission to NPCDB \[SCDX AMBCAR NIGHTLY XMIT\] option
- ICD-10-CM replaces ICD-9-CM as the diagnostic coding system for outpatient encounters with an encounter date on or after the ICD-10 activation date and inpatient treatment episodes with a discharge date on or after the ICD-10 activation date.

For a period of time, the VHA requires the use of dual code sets (ICD-9-CM, ICD-10-CM) to accommodate outpatient dates of service and inpatient discharge dates prior to and following the ICD-10 activation date as well as for reporting and research purposes.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ACR manuals are posted on the VistA Documentation Library (VDL) [Ambulatory Care Reporting](http://www.va.gov/vdl/application.asp?appid=116) page. (Note that the PIMS Technical Manual and the User Manual - Ambulatory Care Reporting are posted on the VDL [Scheduling](http://www.va.gov/vdl/application.asp?appid=100) page.)

The following ACR user manuals are updated with changes for SD\*5.3\*593:

- Appendix - IEMM Error Table
- Ambulatory Care Reporting Menu (same as User Manual - Ambulatory Care Reporting)
- PIMS Technical Manual

The following manuals are not updated with changes for SD\*5.3\*593:

- ACRP Interface Toolkit
- IEMM Installation Guide

The following manual does not exist for this package:

- Security Guide

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following must be installed before installing Patch SD\*5.3\*593:

- SD\*5.3\*171
- SD\*5.3\*409
- SD\*5.3\*442
- SD\*5.3\*466
- SD\*5.3\*474
- SD\*5.3\*556
- LEX\*2\*80
- ICD\*18\*57
- DG\*5.3\*850
- SD\*5.3\*576 (Please see note below)

> **NOTE:** Patch SD\*5.3\*576 incorporates the ICD-10 changes in overlapping routine SCRPW24.

# ACRP Ad Hoc Report Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes ICD-10 enhancements to the ACRP Ad Hoc Report executed with the following option: *ACRP Ad Hoc Report* \[SCRPW AD HOC RPT MENU\].

## Report Perspective – Diagnosis Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If diagnoses are selected as the Report Perspective criteria, the system initially asks you to select either the ICD-9 or ICD-10 code set prior to diagnosis entry.

> **NOTE:** The default selection is the current code set valid on the date the report is run.

Ad Hoc Report

--------------------- R E P O R T P E R S P E C T I V E ----------------------

GH GAF SCORE (HISTORICAL)

GC GAF SCORE (CURRENT)

Select DIAGNOSIS category: pd PRIMARY DIAGNOSIS

Select one of the following:

L LIST

N NULL (NO DATA VALUE)

Limit this factor by: LIST

Select one of the following:

9 ICD-9 (PRIOR TO OCT 1, 2015)

10 ICD-10 (OCT 1, 2015 AND AFTER)

Select coding system: 10//

The prompt to select code set does not display if the Report Perspective is re-edited and additional diagnoses are added to a list of pre-existing diagnoses. In such cases, the list of selectable diagnoses is automatically limited to the code set that matches the diagnoses already selected.

Ad Hoc Report

--------------------- R E P O R T P E R S P E C T I V E ----------------------

GH GAF SCORE (HISTORICAL)

GC GAF SCORE (CURRENT)

Select DIAGNOSIS category: PRIMARY DIAGNOSIS// pd PRIMARY DIAGNOSIS

Select one of the following:

L LIST

N NULL (NO DATA VALUE)

Limit this factor by: LIST// l LIST

Items currently selected:

V70.0XX0A Driver of bus injured in collision w ped/anmi nontraf, init

\*\*\*ITEM LIST SELECTION\*\*\*

Select ICD Diagnosis:

## Report Limitations – Date Range Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A restriction has been implemented such that report date ranges entered within Report Limitations cannot span the ICD-10 implementation date. If such a date range is entered, the user will be presented with an error and required to select a different range.

--------------------- R E P O R T L I M I T A T I O N S -------------

\*\*\*Date Range Selection\*\*\*

Starting date: 9/1/2015 (SEP 01, 2015)

Ending date: 11/1/2015 (NOV 01, 2015)

Starting and Ending dates must both be prior to OCT 1, 2015 (ICD-9) or both be on or after OCT 1, 2015 (ICD-10).

Starting date: SEP 1, 2015

## Report Limitations – Diagnosis Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you select your Report Limitation date range, even if you add additional diagnoses for either List and Range, you are restricted to the corresponding code set for the originally selected Report Limitation date range.

--------------------- R E P O R T L I M I T A T I O N S -------------

Select ICD Diagnosis: V70

27 matches found

1\. V70.0XXA Driver of bus injuried in collision w ped/anml

Nontraf, init (10/01/2015) (Pending)

2\. V70.0XXD Driver of bus injuried in collision w ped/anml

nontraf, subs (10/01/2015) (Pending)

3\. V70.0XXS Driver of bus injuried in collision w ped/anml nontraf,

sequela (10/01/2015) (Pending)

4\. V70.1XXA Driver of bus injuried in collision w ped/anml nontraf,

init (10/01/2015) (Pending)

5\. V70.1XXD Driver of bus injuried in collision w ped/anml nontraf,

subs (10/01/2015) (Pending)

Press \<RETURN\> for more, '^' to exit, or Select 1-5:

This modification to restrict diagnosis selection by date range does not apply if Report Limitations are re-edited. In such cases, the list of selectable diagnoses is automatically limited to the code set that matches the diagnoses already selected.

--------------------- R E P O R T L I M I T A T I O N S ---------------------

Select item to edit: (1-1): 1

Select one of the following:

L LIST

R RANGE

N NULL (NO DATA VALUE)

Limit this factor by: LIST// l LIST

Items currently selected:

V70.0XX0A Driver of bus injured in collision w ped/anml nontraf, init

\*\*\*ITEM LIST SELECTION\*\*\*

Select ICD Diagnosis:

<span id="_Toc318189352" class="anchor"></span>

## Report Limitations – Pre-Execution Date Diagnosis Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system performs a final check across both Report Perspective and Report Limitation data to validate the following:

- All entered diagnoses are consistent in code set.
- All selected diagnoses are of the correct code set for the selected date range.
- If discrepancies are detected, an error displays and execution of the report is stopped. You then need to correct the Report Perspective / Report Limitation selections in order to execute the report.

ICD-9 Code Selected for Report Perspective

------------- S e l e c t e d R e p o r t P a r a m e t e r s--------------

--------------------------- R E P O R T F O R M A T ------------------------

Report output format: DETAILED

Type of detail: ENCOUNTER/VISIT/UNIQUE LIST

List activity detail by: ENCOUNTER

Produce output as: FORMATTED TEXT

--------------------- R E P O R T P E R S P E C T I V E --------------------

Perspective category: DIAGNOSIS

Perspective sub-category: PRIMARY DIAGNOSIS

Detail list: V70.0 ROUTINE MEDICAL EXAM

-------------------- R E P O R T L I M I T A T I O N S ---------------------

Enter RETURN to continue or '^' to exit:

ICD-10 Date Range and Code Set Selected for Report Limitations

------------- S e l e c t e d R e p o r t P a r a m e t e r s--------------

--------------------- R E P O R T L I M I T A T I O N S ---------------------

Starting date: OCT 29, 2015

Ending date: NOV 28, 2015

Addl. limitation category: DIAGNOSIS

Addl. limitation sub-category: PRIMARY DIAGNOSIS

Include range – from: V70.0XXA Driver of bus injured in

Collision w ped/anml nontraf, init

To: V72.0XXA Driver of bus injured in clsn w

2/3-whl mv nontraf, init

--------------------- R E P O R T P R I N T O R D E R ---------------------

Output order: ALPHABETIC

-----------------------------------------------------------------------------

Enter RETURN to continue or '^' to exit:

System Detected Selected Date Range Inconsistent with Originally Selected Report Perspective –ICD-9 Diagnosis

------------- S e l e c t e d R e p o r t P a r a m e t e r s--------------

-----------------------------------------------------------------------------

Report Action

Select one of the following:

C CONTINUE

E EDIT PARAMETERS

R RE-DISPLAY PARAMETERS

P PRINT PARAMETERS

Q QUIT

Select report action: continue// \<enter\>

The Report Limitation dates must be before OCT 1, 2015 to match the (ICD-9-CM) diagnoses specified in the Report Perspective.

Unable to continue with queuing!

# Most Frequent 50 IP ICD Diagnosis Codes (IP7) / Most Frequent 50 ICD Diagnosis Codes (OP7)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes ICD-10 enhancements to the Most Frequent 50 IP ICD-9-CM Codes (IP7) report and Most Frequent 50 ICD-9-CM Codes (OP7) report, executed with the following options:

- Most Frequent 50 IP ICD Codes (IP7) \[SCRPW DVM IP DX FREQUENCY\]
- Most Frequent 50 ICD-9-CM Codes (OP7) \[SCRPW DVM DX FREQUENCY\]

All Display Instances of ‘ICD-9-CM’ in Report Titles Display ‘ICD’

Select Data Validation Menu Option: ?

IP0 Enc. By IP DSS ID/DSS ID by Freq. (IP0, IP1, IP2)

IP3 Means Test IP Visits & Uniques (IP3, IP4, IP5)

IP6 Most Frequent 50 IP CPT Codes (IP6)

IP7 Most Frequent 50 IP ICD Codes (IP7)

IP8 Most Frequent 20 IP Practicioner Types (IP8)

IP9 Visits and Unique IP SSNs by County (IP9)

OP0 Enc. By IP DSS ID/DSS ID by Freq. (OP0, OP1, OP2)

OP3 Means Test IP Visits & Uniques (OP3, OP4, OP5)

OP6 Most Frequent 50 IP CPT Codes (OP6)

OP7 Most Frequent 50 IP ICD Codes (OP7)

OP8 Most Frequent 20 IP Practicioner Types (OP8)

OP9 Visits and Unique IP SSNs by County (OP9)

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Data Validation Menu Option:

All Display Instances of “ICD-9-CM” in Report Now Display “ICD”

![](sd-5-3-593-acr-release-notes/002.png)

# Encounter Activity Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes ICD-10 enhancements to the Encounter Activity Report, executed with the following option:

> *Encounter Activity Report* \[SCRPW ENCOUNTER ACTIVITY RPT\]

## Date Range Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Report date ranges entered within Report Limitations cannot span the ICD-10 activation date. If such a date range is entered, you receive an error and are required to select a different range.

Encounter Activity Report

\*\*\*Date Range Selection\*\*\*

Starting date: 9/1/2015 (SEP 01, 2015)

Ending date: 11/1/2015 (NOV 01, 2015)

Starting and Ending dates must both be prior to OCT 1, 2015 (ICD-9) or both be on or after OCT 1, 2015 (ICD-10).

Starting date: SEP 1, 2015

# Outpatient Diagnosis/Procedure Frequency Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes ICD-10 enhancements to the Outpatient Diagnosis/Procedure Frequency Report, executed with the following option:

Outpatient Diagnosis/Procedure Frequency Report \[SCRPW DX/CPT FREQUENCY REPORT\]

## Date Range Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Report date ranges entered within Report Limitations cannot span the ICD-10 activation date. If such a date range is entered, you receive an error and are required to select a different range.

Outpatient Diagnosis/Procedure Frequency Report

\*\*\*Date Range Selection\*\*\*

Starting date: 9/1/2015 (SEP 01, 2015)

Ending date: 11/1/2015 (NOV 01, 2015)

Starting and Ending dates must both be prior to OCT 1, 2015 (ICD-9) or both be on or after OCT 1, 2015 (ICD-10).

Starting date: SEP 1, 2015

# Outpatient Diagnosis/Procedure Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes ICD-10 enhancements to the Outpatient Diagnosis/Procedure Code Search, executed with the following option:

Outpatient Diagnosis/Procedure Code Search \[SCRPW DX/PROCEDURE CODE SEARCH\]

## Date Range Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Report date ranges entered within Report Limitations cannot span the ICD-10 activation date. If such a date range is entered, you receive an error and are required to select a different range.

Outpatient Diagnosis/Procedure Search

\*\*\*Date Range Selection\*\*\*

Starting date: 9/1/2015 (SEP 01, 2015)

Ending date: 11/1/2015 (NOV 01, 2015)

Starting and Ending dates must both be prior to OCT 1, 2015 (ICD-9) or both be on or after OCT 1, 2015 (ICD-10).

Starting date: SEP 1, 2015

## Diagnosis Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A modification has been made such that when diagnoses are selected, for both List and Range, the user is restricted to entry of diagnoses of the code set that corresponds to the previously selected date range.

Outpatient Diagnosis/Procedure Search

\*\*\*Date Range Selection\*\*\*

Starting date: 10/1/2015 (OCT 01, 2015)

Ending date: 11/1/2015 (NOV 01, 2015)

\*\*\*\* Report Search Criteria Selection (Element 'A') \*\*\*\*

Select one of the following:

DL DIAGNOSIS LIST

DR DIAGNOSIS RANGE

PL PROCEDURE LIST

PR PROCEDURE RANGE

Specify criteria type for search element 'A': dl DIAGNOSIS LIST

Select ICD Diagnosis:

# Ambulatory Care Nightly Transmission to NPCDB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes ICD-10 enhancements to the Ambulatory Care Nightly Transmission to the National Patient Care Database (NPCDB) HL7 interface and its counterpart Encounter ‘Acton Required’ Report. They are executed with the following options:

Ambulatory Care Nightly Transmission to NPCDB \[SCDX AMBCAR NIGHTLY XMIT\]

Encounter ‘Action Required’ Report \[SCRPW ACTION REQUIRED REPORT\]

## HL7 Diagnosis Segment - DG1-2 & DG1-4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When diagnoses are transmitted to the NPCDB, the DG1-2 segment-field of outgoing HL7 messages supports the identifier “I10” for ICD-10 diagnoses as well as the pre-existing “I9” identifier for ICD-9 diagnoses.

Additionally, the diagnosis description transmitted in DG1-4 contains the short description of ICD diagnoses and the 60 characters for ICD-10 codes.

> **NOTE:** The short description of ICD-10 codes has been defined to be 60 characters or less.

## Error Code Display Text Update – ICD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Encounter ‘Action Required’ Report, all display instances of “ICD-9-CM” are replaced with “ICD” in the Transmitted Outpatient Encounter Error Code (File \#409.76) records.

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Integration Control Registration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new Integration Control Registration (ICR) \#5747 was introduced by DRG GROUPER. The API \$\$ICDDATA^ICDXCODE was replaced by \$\$ICDDX^ICDEX.

| Name/signature of the component | Provider application | Consumer application      | ICR | ICD related? |
|---------------------------------|----------------------|---------------------------|-----|--------------|
| \$\$CSI^ICDEX                   | DRG GROUPER          | AMBULATORY CARE REPORTING | Yes |              |
| \$\$ICDDX^ICDEX                 | DRG GROUPER          | AMBULATORY CARE REPORTING | Yes |              |
| \$\$IMP^ICDEX                   | DRG GROUPER          | AMBULATORY CARE REPORTING | Yes |              |
| \$\$GETDX^SDOE                  | SCHEDULING           | AMBULATORY CARE REPORTING |     | Yes          |
| EN^VAFHLDG1                     | REGISTRATION         | AMBULATORY CARE REPORTING | Yes | Yes          |

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error codes 500 and 5000  were modified in the TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE File (#409.76) by replacing the text “ICD-9” with “ICD”.