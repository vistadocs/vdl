---
title: DVBA*2.7*164 Workflow - Kidney Conditions (Nephrology)
doc_type: WF
doc_label: Workflow Guide
doc_layer: patch
doc_subject: Workflow - Kidney Conditions (Nephrology)
app_code: CAPRI
app_name: Compensation and Pension Record Interchange
section: FIN
app_status: active
pkg_ns: DVBA
patch_ver: 2.7
patch_id: DVBA*2.7*164
group_key: "CAPRI:DVBA:2.7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - enabled
  - class
  - diagnosis
  - kidney
  - veteran
  - strong
  - mandatory
  - other
  - else
  - please
page_count: 0
word_count: 12594
section_count: 15
table_count: 72
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2011
revision_count: 2
revision_newest: 4/1/2011
revision_oldest: 1/21/2011
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_p163_dbq_kidneyconditions_wf.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_p163_dbq_kidneyconditions_wf.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=133"
---

![](dvba-2-7-164-workflow-kidney-conditions-nephrology/001.png)

Compensation and Pension Record Interchange (CAPRI)

Kidney Conditions (Nephrology)

Disability Benefits Questionnaire (DBQ)

Workflow

April 2011

Office of Enterprise Development

Management & Financial Systems

Revision History

|           |                                         |          |                  |
|-----------|-----------------------------------------|----------|------------------|
| Date      | Description (Patch \# if applicable)    | Author   | Technical Writer |
| 1/21/2011 | Document created                        | REDACTED | N/A              |
| 4/1/2011  | Revisions and corrections for patch 163 | REDACTED | N/A              |

<span id="_Toc270513758" class="anchor"></span>Table 1: Rules: DBQ – Kidney Conditions (Nephrology) – Name of patient/Veteran

Table of Contents

Table of Figures and Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Overview](#overview)
- [Kidney Conditions (Nephrology) DBQ](#kidney-conditions-nephrology-dbq)
  - [Name of patient/Veteran](#name-of-patientveteran)
  - [Section 1. Diagnosis](#section-1-diagnosis)
  - [Section 2. Medical History](#section-2-medical-history)
  - [Section 3. Renal dysfunction](#section-3-renal-dysfunction)
  - [Section 4. Urolithiasis](#section-4-urolithiasis)
  - [Section 5. Urinary tract/kidney infection](#section-5-urinary-tractkidney-infection)
  - [Section 6. Kidney transplant or removal](#section-6-kidney-transplant-or-removal)
  - [Section 7. Tumors and Neoplasms](#section-7-tumors-and-neoplasms)
  - [Section 8. Other pertinent physical findings, complications, signs and/or symptoms](#section-8-other-pertinent-physical-findings-complications-signs-andor-symptoms)
  - [Section 9. Diagnostic testing](#section-9-diagnostic-testing)
  - [Section 10. Functional impact](#section-10-functional-impact)
  - [Section 11. Remarks, if any](#section-11-remarks-if-any)
- [Kidney Conditions (Nephrology) DBQ-AMIE Worksheet](#kidney-conditions-nephrology-dbq-amie-worksheet)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides a high level overview of the contents found on the Kidney Conditions (Nephrology) Disability Benefits Questionnaire (DBQ). The DBQ can be populated via an online template within the CAPRI C&P Worksheets tab and then printed OR it can be printed via AMIE (AUTOMATED MEDICAL INFORMATION EXCHANGE) and then manually populated. This document contains the edit rules for the template as well as an example of how the template will look online in CAPRI or printed from CAPRI. It also contains the layout for the AMIE worksheet to depict how it will look when printed from AMIE.

For more detailed information on standard template functionality not covered in this document, please refer to the *C&P Worksheet Tab Functionalities* section of the [CAPRI GUI User Guide](http://www4.va.gov/vdl/documents/Financial_Admin/CAPRI/capri_um.pdf).

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kidney Conditions (Nephrology) DBQ provides the ability to capture information related to Kidney Conditions (Nephrology) and its treatment.

Each DBQ template contains a standard footer containing a note stating that “VA may request additional medical information, including additional examinations if necessary to complete VA’s review of the Veteran’s application.” (see Figure 1 and 2).

<span id="_Toc270513756" class="anchor"></span>Figure 1: Template Example: DBQ - Standard VA Note

![](dvba-2-7-164-workflow-kidney-conditions-nephrology/002.png)

<span id="_Toc270513757" class="anchor"></span>Figure 2: Print Example: DBQ – Standard VA Note

|                                                                                     |
|-------------------------------------------------------------------------------------|
| NOTE: VA may request additional medical information, including additional       |
| examinations if necessary to complete VA's review of the Veteran's application. |
|                                                                                     |

<span id="_Toc289419555" class="anchor"></span>Table 2: Rules: DBQ – Kidney Conditions (Nephrology) – 1. Diagnosis

A number of fields on the Kidney Conditions (Nephrology) template are mandatory and require a response (value) prior to the exam being marked as completed. Some questions may activate a Pop-up window displaying information as to each question that needs to be answered before the template can be completed.

# Kidney Conditions (Nephrology) DBQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Name of patient/Veteran

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

| Field/Question                                                                                                                                                                                                                         | Field Disposition | Valid Values | Format | Error Message                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------|------------|-----------------------------------------------|
| Kidney Conditions (Nephrology)                                                                                                                                                                                                         | Enabled, Read-Only    | N/A              | N/A        | N/A                                           |
| Disability Benefits Questionnaire                                                                                                                                                                                                      | Enabled, Read-Only    | N/A              | N/A        | N/A                                           |
| Name of patient/Veteran:                                                                                                                                                                                                                   | Enabled, Mandatory    | N/A              | Free Text  | Please enter the name of the patient/Veteran. |
| Your patient is applying to the U. S. Department of Veterans Affairs (VA) for disability benefits.  VA will consider the information you provide on this questionnaire as part of their evaluation in processing the Veteran’s claim.  | Enabled, Read-Only    | N/A              | N/A        | N/A                                           |

<span id="_Toc270513764" class="anchor"></span>Table 3: Rules: DBQ – Kidney Conditions (Nephrology) – 2. Medical History

<span id="_Toc270513759" class="anchor"></span>Figure 3: Template Example: DBQ – Kidney Conditions (Nephrology) – Name of patient/Veteran

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/003.png)

<span id="_Toc270513760" class="anchor"></span>Figure 4: Print Example: DBQ – Kidney Conditions (Nephrology) – Name of patient/Veteran

<table>
<caption><p><span id="_Toc270513767" class="anchor"></span>Table 4: Rules: DBQ – Kidney Conditions (Nephrology) – 3. Renal dysfunction</p></caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Kidney Conditions (Nephrology)</p>
<p>Disability Benefits Questionnaire</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Name of patient/Veteran:</td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td>Your patient is applying to the U.S. Department of Veterans Affairs (VA) for</td>
</tr>
<tr class="odd">
<td>disability benefits. VA will consider the information you provide on this</td>
</tr>
<tr class="even">
<td>questionnaire as part of their evaluation in processing the Veteran's claim.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513767" class="anchor"></span>Table 4: Rules: DBQ – Kidney Conditions (Nephrology) – 3. Renal dysfunction

## Section 1. Diagnosis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The question “Does the Veteran now have or has he/she ever been diagnosed with a kidney condition?” must be answered before the template can be completed.

- If it is answered with Yes, all other questions requiring an answer as described by the rules in this document must be answered before the template can be completed.
- If it is answered with No, the rationale is required. The remainder of the template may be completed without answering any additional questions or the user may input answers to any of the optional questions as indicated by the rules described in this document.

All questions will be printed even if they have not been answered.

If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below and must be answered before this template can be completed.

<table>
<caption><p><span id="_Toc270513770" class="anchor"></span>Table 5: Rules: DBQ – Kidney Conditions (Nephrology) – 4. Urolithiasis</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 21%" />
<col style="width: 20%" />
<col style="width: 9%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>1.Diagnosis</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran now have or has he/she ever been diagnosed with a kidney condition?</td>
<td>Enabled, Mandatory; Choose one valid value</td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran now have or has he ever been diagnosed with a kidney condition?</td>
</tr>
<tr class="odd">
<td>If no, provide rationale (e.g. Veteran does not currently have any known kidney condition(s)):</td>
<td><p>If <em>Does the Veteran now have or has he/she ever been diagnosed with a kidney condition?</em> = <em>No</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the rationale for indicating the Veteran has not been diagnosed with a kidney condition.</td>
</tr>
<tr class="even">
<td>If yes, indicate diagnoses: (check all that apply)</td>
<td><p>If <em>Does the Veteran now have or has he/she ever been diagnosed with a kidney condition? = Yes;</em> Enabled, Mandatory, Choose one or more valid values.</p>
<p>Else; Optional</p></td>
<td>[Diabetic nephropathy; Glomerulonephritis; Hydronephrosis; Interstitial nephritis; Kidney transplant; Nephrosclerosis; Nephrolithiasis; Renal artery stenosis; Ureterolithiasis; Neoplasm of the kidney; Other kidney condition(specify diagnosis, providing only diagnoses that pertain to kidney conditions.)]</td>
<td>N/A</td>
<td>Please select at least one diagnosis.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Diabetic nephropathy</em>; Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Diabetic nephropathy</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Diabetic nephropathy.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td>If <em>Diagnosis = Yes and if Diagnosis includes Diabetic nephropathy</em>; Enabled, Mandatory</td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Diabetic nephropathy.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Glomerulonephritis</em>; Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Glomerulonephritis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Glomerulonephritis.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Glomerulonephritis</em>; Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Glomerulonephritis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Glomerulonephritis.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Hydronephrosis</em>; Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Hydronephrosis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Hydronephrosis.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Hydronephrosis</em>; Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Hydronephrosis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Hydronephrosis.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Interstitial nephritis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Interstitial nephritis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Interstitial nephritis.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Interstitial nephritis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Interstitial nephritis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Interstitial nephritis.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Kidney transplant;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Kidney transplant</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Kidney transplant.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Kidney transplant;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Kidney transplant</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Kidney transplant.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Nephrosclerosis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Nephrosclerosis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Nephrosclerosis.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Nephrosclerosis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Nephrosclerosis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Nephrosclerosis.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Nephrolithiasis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Nephrolithiasis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Nephrolithiasis.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Nephrolithiasis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Nephrolithiasis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Nephrolithiasis.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Renal artery stenosis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Renal artery stenosis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Renal artery stenosis.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Renal artery stenosis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Renal artery stenosis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Renal artery stenosis.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Ureterolithiasis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Ureterolithiasis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Ureterolithiasis.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Ureterolithiasis;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Ureterolithiasis</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Ureterolithiasis.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Neoplasm of the kidney;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Neoplasm of the kidney</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Neoplasm of the kidney.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes and if Diagnosis includes Neoplasm of the kidney;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No and if Diagnosis includes Neoplasm of the kidney</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Neoplasm of the kidney.</td>
</tr>
<tr class="odd">
<td>Other diagnosis #1:</td>
<td><p>If <em>Diagnosis includes Other kidney condition</em>;</p>
<p>Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>Please enter a value in the ‘Other diagnosis #1’ field.</td>
</tr>
<tr class="even">
<td>ICD code:</td>
<td><p>If <em>Other diagnosis #1 is populated;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for other diagnosis #1.</td>
</tr>
<tr class="odd">
<td>Date of diagnosis:</td>
<td><p>If <em>Other diagnosis #1 is populated;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of other diagnosis #1.</td>
</tr>
<tr class="even">
<td>Other diagnosis #2</td>
<td><p>If <em>Diagnosis includes Other kidney condition</em>;</p>
<p>Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>ICD code:</td>
<td><p>If <em>Other diagnosis #2 is populated;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for other diagnosis #2.</td>
</tr>
<tr class="even">
<td>Date of diagnosis:</td>
<td><p>If <em>Other diagnosis #2 is populated;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date diagnosis for other diagnosis #2.</td>
</tr>
<tr class="odd">
<td>If there are additional diagnoses that pertain to kidney conditions(s), list using above format:</td>
<td>Enabled, Optional</td>
<td>N/A</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<span id="_Toc270513770" class="anchor"></span>Table 5: Rules: DBQ – Kidney Conditions (Nephrology) – 4. Urolithiasis

<span id="_Toc270513762" class="anchor"></span>Figure 5: Template Example: DBQ – Kidney Conditions (Nephrology) – 1. Diagnosis

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/004.png)![](dvba-2-7-164-workflow-kidney-conditions-nephrology/005.png)![](dvba-2-7-164-workflow-kidney-conditions-nephrology/006.png)

<span id="_Toc270513763" class="anchor"></span>Figure 6: Print Example: DBQ – Kidney Conditions (Nephrology) – 1. Diagnosis

| 1\. Diagnosis                                                             |
|---------------------------------------------------------------------------|
| ------------                                                              |
| Does the Veteran now have or has he/she ever been diagnosed with a kidney |
| condition? \[X\] Yes \[ \] No                                             |
|                                                                           |
| If no, provide rationale (e.g., Veteran has never had any known kidney    |
| condition(s)):                                                            |
|                                                                           |
| If yes, indicate diagnoses: (check all that apply)                        |
| \[ \] Diabetic nephropathy                                                |
| ICD Code: Date of Diagnosis:                                              |
| \[X\] Glomerulonephritis                                                  |
| ICD Code: Date of Diagnosis:                                              |
| \[ \] Hydronephrosis                                                      |
| ICD Code: Date of Diagnosis:                                              |
| \[ \] Interstitial nephritis                                              |
| ICD Code: Date of Diagnosis:                                              |
| \[ \] Kidney transplant                                                   |
| ICD Code: Date of Diagnosis:                                              |
| \[ \] Nephrosclerosis                                                     |
| ICD Code: Date of Diagnosis:                                              |
| \[ \] Nephrolithiasis                                                     |
| ICD Code: Date of Diagnosis:                                              |
| \[ \] Renal artery stenosis                                               |
| ICD Code: Date of Diagnosis:                                              |
| \[ \] Ureterolithiasis                                                    |
| ICD Code: Date of Diagnosis:                                              |
| \[ \] Neoplasm of the kidney                                              |
| ICD Code: Date of Diagnosis:                                              |
| \[X\] Other kidney condition (specify diagnosis, providing only diagnoses |
| that pertain to kidney conditions.)                                       |
|                                                                           |
| Other diagnosis \#1:                                                      |
| ICD code:                                                                 |
| Date of diagnosis:                                                        |
|                                                                           |
| Other diagnosis \#2: a                                                    |
| ICD code:                                                                 |
| Date of diagnosis:                                                        |
|                                                                           |
| If there are additional diagnoses that pertain to kidney conditions,      |
| list using above format:                                                  |

<span id="_Toc289419559" class="anchor"></span>Table 6: Rules: DBQ – Kidney Conditions (Nephrology) – 5. Urinary tract/kidney infection

## Section 2. Medical History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc289419560" class="anchor"></span>Table 7: Rules: DBQ – Kidney Conditions (Nephrology) – 6. Kidney transplant or removal</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 29%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>2.Medical History</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Describe the history (including cause, onset and course) of the Veteran’s kidney condition:</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the history (including onset and course) of the Veteran's kidney condition.</td>
</tr>
</tbody>
</table>

<span id="_Toc289419560" class="anchor"></span>Table 7: Rules: DBQ – Kidney Conditions (Nephrology) – 6. Kidney transplant or removal

<span id="_Toc289419534" class="anchor"></span>Figure 7: Template Example: DBQ – Kidney Conditions (Nephrology) – 2. Medical History

![](dvba-2-7-164-workflow-kidney-conditions-nephrology/007.png)

<span id="_Toc270513766" class="anchor"></span>Figure 8: Print Example: DBQ – Kidney Conditions (Nephrology) – 2. Medical History

| 2\. Medical history                                                       |
|---------------------------------------------------------------------------|
| ------------------                                                        |
| Describe the history (including cause, onset and course) of the Veteran's |
| kidney condition:                                                         |

<span id="_Toc270513773" class="anchor"></span>Table 8: Rules: DBQ – Kidney Conditions (Nephrology) – 7. Tumors and Neoplasms

## Section 3. Renal dysfunction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc270513776" class="anchor"></span>Table 9: Rules: DBQ – Kidney Conditions (Nephrology) – 8. Other pertinent physical findings, complications, signs and/or symptoms</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 21%" />
<col style="width: 27%" />
<col style="width: 9%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>3.Renal dysfunction</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have renal dysfunction?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have renal dysfunction?</td>
</tr>
<tr class="odd">
<td>If yes, does the Veteran require regular dialysis?</td>
<td><p>If <em>Does the Veteran have real dysfunction? = Yes</em>; Enabled; Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not the Veteran requires regular dialysis.</td>
</tr>
<tr class="even">
<td>b. Does the Veteran have any signs or symptoms due to renal dysfunction?</td>
<td><p>If <em>Does the Veteran have renal dysfunction? = Yes</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have any signs or symptoms due to renal dysfunction?</td>
</tr>
<tr class="odd">
<td>If yes, check all that apply:</td>
<td><p>If <em>Does the Veteran have renal dysfunction? = Yes;</em> Enabled; Optional;</p>
<p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? = Yes;</em> Enabled; Mandatory;</p>
<p>Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>[Proteinuria (albuminuria); Edema (due to renal dysfunction); Anorexia (due to renal dysfunction); Weight loss (due to renal dysfunction); Generalized poor health due to renal dysfunction; Lethargy due to renal dysfunction; Weakness due to renal dysfunction; Limitation of exertion due to renal dysfunction; Able to perform only sedentary activity, due to persistent edema caused by renal dysfunction; Markedly decreased function other organ systems, especially the cardiovascular system, caused by renal dysfunction]</td>
<td>N/A</td>
<td>Please select all applicable renal dysfunction related signs or symptoms.</td>
</tr>
<tr class="even">
<td>If checked, indicate frequency: (check all that apply)</td>
<td><p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? = Yes</em> and if <em>Renal dysfunction signs or symptoms include Proteinuria (albuminuria);</em> Enabled; Mandatory;</p>
<p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? Is not populated</em> and if <em>Renal dysfunction signs or symptoms include Proteinuria (albuminuria);</em>Enabled; Optional;</p>
<p>Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>[Recurring; Constant; Persistent]</td>
<td>N/A</td>
<td>Please indicate the frequency of Proteinuria (albuminuria).</td>
</tr>
<tr class="odd">
<td>If checked, indicate frequency: (check all that apply)</td>
<td><p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? = Yes</em> and if <em>Renal dysfunction signs or symptoms include Edema (due to renal dysfunction);</em> Enabled; Mandatory;</p>
<p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? is not populated</em> and if <em>Renal dysfunction signs or symptoms include Edema (due to renal dysfunction);</em> Enabled; Optional;</p>
<p>Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>[Some; Transient; Slight; Persistent]</td>
<td>N/A</td>
<td>Please indicate the frequency of edema (due to renal dysfunction).</td>
</tr>
<tr class="even">
<td>If checked, provide baseline weight (average weight for 2-year period preceding onset of disease):</td>
<td><p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? = Yes</em> and if <em>Renal dysfunction signs or symptoms include Weight loss (due to renal dysfunction);</em> Enabled; Mandatory;</p>
<p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? Is not populated</em> and if <em>Renal dysfunction signs or symptoms include Weight loss (due to renal dysfunction);</em> Enabled; Optional;</p>
<p>Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the baseline weight.</td>
</tr>
<tr class="odd">
<td>Provide current weight:</td>
<td><p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? = Yes</em> and if <em>Renal dysfunction signs or symptoms include Weight loss (due to renal dysfunction);</em> Enabled; Mandatory;</p>
<p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? is not populated</em> and if <em>Renal dysfunction signs or symptoms include Weight loss (due to renal dysfunction);</em> Enabled; Optional;</p>
<p>Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the current weight.</td>
</tr>
<tr class="even">
<td>If checked, describe:</td>
<td><p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? = Yes</em> and if <em>Renal dysfunction signs or symptoms include Markedly decreased function other organ systems, especially the cardiovascular system, caused by renal dysfunction;</em> Enabled; Mandatory;</p>
<p>If <em>Does the Veteran have any signs or symptoms due to renal dysfunction? is not populated</em> and if <em>Renal dysfunction signs or symptoms include Markedly decreased function other organ systems, especially the cardiovascular system, caused by renal dysfunction;</em> Enabled; Optional;</p>
<p>Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the decreased function of other organ systems caused by renal dysfunction.</td>
</tr>
<tr class="odd">
<td>c. Does the Veteran have hypertension and/or heart disease due to renal dysfunction or caused by any kidney condition?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em> and <em>Does the Veteran have renal dysfunction = Yes</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have hypertension and/or heart disease due to renal dysfunction or caused by any kidney condition?</td>
</tr>
<tr class="even">
<td>If yes, also complete the Hypertension and/or Heart Disease Questionnaire as appropriate.</td>
<td><p>If <em>Does the Veteran have hypertension and/or heart disease due to renal dysfunction or caused by any kidney condition? = Yes;</em> Enabled; Read-Only</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<span id="_Toc270513776" class="anchor"></span>Table 9: Rules: DBQ – Kidney Conditions (Nephrology) – 8. Other pertinent physical findings, complications, signs and/or symptoms

<span id="_Toc270513768" class="anchor"></span>Figure 9: Template Example: DBQ – Kidney Conditions (Nephrology) – 3. Renal dysfunction

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/008.png)![](dvba-2-7-164-workflow-kidney-conditions-nephrology/009.png)

<span id="_Toc270513769" class="anchor"></span>Figure 10: Print Example: DBQ – Kidney Conditions (Nephrology) – 3. Renal dysfunction

| 3\. Renal dysfunction                                                     |
|---------------------------------------------------------------------------|
| --------------------                                                      |
| a\. Does the Veteran have renal dysfunction?                              |
| \[X\] Yes \[ \] No                                                        |
|                                                                           |
| If yes, does the Veteran require regular dialysis?                        |
| \[X\] Yes \[ \] No                                                        |
|                                                                           |
| b\. Does the Veteran have any signs or symptoms due to renal dysfunction? |
| \[X\] Yes \[ \] No                                                        |
|                                                                           |
| If yes, check all that apply:                                             |
| \[ \] Proteinuria (albuminuria)                                           |
| If checked, indicate frequency: (check all that apply)                    |
| \[ \] Recurring \[ \] Constant \[ \] Persistent                           |
| \[ \] Edema (due to renal dysfunction)                                    |
| If checked, indicate frequency: (check all that apply)                    |
| \[ \] Some \[ \] Transient \[ \] Slight \[ \] Persistent                  |
| \[ \] Anorexia (due to renal dysfunction)                                 |
| \[ \] Weight loss (due to renal dysfunction)                              |
| If checked, provide baseline weight (average weight for 2-year            |
| period preceding onset of disease):                                       |
| Provide current weight:                                                   |
| \[ \] Generalized poor health due to renal dysfunction                    |
| \[ \] Lethargy due to renal dysfunction                                   |
| \[ \] Weakness due to renal dysfunction                                   |
| \[ \] Limitation of exertion due to renal dysfunction                     |
| \[X\] Able to perform only sedentary activity, due to persistent          |
| edema caused by renal dysfunction                                         |
| \[X\] Markedly decreased function other organ systems, especially         |
| the cardiovascular system, caused by renal dysfunction                    |
| If checked, describe:                                                     |
|                                                                           |
| c\. Does the Veteran have hypertension and/or heart disease due to renal  |
| dysfunction or caused by any kidney condition?                            |
| \[X\] Yes \[ \] No                                                        |
|                                                                           |
| If yes, also complete the Hypertension and/or Heart Disease Questionnaire |
| as appropriate.                                                           |

<span id="_Toc289419563" class="anchor"></span>Table 10: Rules: DBQ – Kidney Conditions (Nephrology) – 9. Diagnostic testing

## Section 4. Urolithiasis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc289419564" class="anchor"></span>Table 11: Rules: DBQ – Kidney Conditions (Nephrology) – 10. Functional impact</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 24%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>4. Urolithiasis</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have kidney, ureteral or bladder calculi?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have kidney, ureteral or bladder calculi?</td>
</tr>
<tr class="odd">
<td>If yes, indicate location (check all that apply)</td>
<td><p>If <em>Does the Veteran have kidney, ureteral or bladder calculi? = Yes;</em> Enabled; Mandatory, Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>[Kidney; Ureter; Bladder]</td>
<td>N/A</td>
<td>Please select all locations where calculi are found.</td>
</tr>
<tr class="even">
<td>If the Veteran has urolithiasis, complete the following:</td>
<td><p>If <em>Does the Veteran have kidney, ureteral or bladder calculi? = Yes;</em> Enabled; Read-Only</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>b. Has the Veteran had treatment for recurrent stone formation in the kidney, ureter or bladder?</td>
<td><p>If <em>Does the Veteran have kidney, ureteral or bladder calculi? = Yes;</em> Enabled; Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Has the Veteran had treatment for recurrent stone formation in the kidney, ureter or bladder?</td>
</tr>
<tr class="even">
<td>If yes, indicate treatment: (check all that apply)</td>
<td><p>If <em>Has the Veteran had treatment for recurrent stone formation in the kidney, ureter or bladder? = Yes;</em> Enabled; Mandatory; Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>[Diet therapy; Drug therapy; Invasive or non-invasive procedures]</td>
<td>N/A</td>
<td>Please select at least one treatment for recurrent stone formation in the kidney, ureter or bladder.</td>
</tr>
<tr class="odd">
<td>If checked, specify diet and dates of use:</td>
<td><p>If treatment includes <em>Diet therapy;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please specify the diet and dates of use.</td>
</tr>
<tr class="even">
<td>If checked, list medication and dates of use:</td>
<td><p>If treatment includes <em>Drug therapy;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please list the medication and dates of use.</td>
</tr>
<tr class="odd">
<td>If checked, indicate average number of times per year invasive or non-invasive procedures were required:</td>
<td><p>If treatment includes <em>Invasive or non-invasive procedures;</em> Enabled; Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[0 to 1 per year; 2 per year; &gt;2 per year]</td>
<td>N/A</td>
<td>Please indicate the average number of times per year invasive or non-invasive procedures were required for treatment of urolithiasis.</td>
</tr>
<tr class="even">
<td>Date and facility of most recent invasive or non-invasive procedure:</td>
<td><p>If treatment includes <em>Invasive or non-invasive procedures;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the most recent invasive or non-invasive procedure for treatment of urolithiasis, and the facility where it was performed.</td>
</tr>
<tr class="odd">
<td>c. Does the Veteran have signs or symptoms due to urolithiasis?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have signs or symptoms due to urolithiasis?</td>
</tr>
<tr class="even">
<td>If yes, indicate severity (check all that apply):</td>
<td><p>If <em>Does the Veteran have signs or symptoms due to urolithiasis? = Yes;</em> Enabled; Mandatory; Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>[No symptoms or attacks of colic; Occasional attacks of colic; Frequent attacks of colic; Causing voiding dysfunction; Requires catheter drainage; Causing infection (pyonephrosis); Causing hydronephrosis; Causing impaired kidney function; Other, describe:]</td>
<td>N/A</td>
<td>Please check one or more signs or symptoms due to urolithiasis.</td>
</tr>
<tr class="odd">
<td>Other, describe:</td>
<td><p>If severity includes <em>Other;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other signs or symptoms due to urolithiasis.</td>
</tr>
</tbody>
</table>

<span id="_Toc289419564" class="anchor"></span>Table 11: Rules: DBQ – Kidney Conditions (Nephrology) – 10. Functional impact

<span id="_Toc289419538" class="anchor"></span>Figure 11: Template Example: DBQ – Kidney Conditions (Nephrology) – 4. Urolithiasis

![](dvba-2-7-164-workflow-kidney-conditions-nephrology/010.png)![](dvba-2-7-164-workflow-kidney-conditions-nephrology/011.png)

<span id="_Toc289419539" class="anchor"></span>Figure 12: Print Example: DBQ – Kidney Conditions (Nephrology) – 4. Urolithiasis

| 4\. Urolithiasis                                                       |
|------------------------------------------------------------------------|
| ---------------                                                        |
| a\. Does the Veteran have kidney, ureteral or bladder calculi?         |
| \[ \] Yes \[ \] No                                                     |
|                                                                        |
| If yes, indicate location (check all that apply)                       |
| \[ \] Kidney \[ \] Ureter \[ \] Bladder                                |
|                                                                        |
| If the Veteran has urolithiasis, complete the following:               |
|                                                                        |
| b\. Has the Veteran had treatment for recurrent stone formation in the |
| kidney, ureter or bladder?                                             |
| \[ \] Yes \[ \] No                                                     |
|                                                                        |
| If yes, indicate treatment (check all that apply)                      |
| \[ \] Diet therapy                                                     |
| If checked, specify diet and dates of use:                             |
| \[ \] Drug therapy                                                     |
| If checked, list medication and dates of use:                          |
| \[ \] Invasive or non-invasive procedures:                             |
| If checked, indicate average number of times per year invasive         |
| or non-invasive procedures were required:                              |
| \[ \] 0 to 1 per year \[ \] 2 per year \[ \] \> 2 per year             |
| Date and facility of most recent invasive or non-invasive              |
| procedure:                                                             |
|                                                                        |
| c\. Does the Veteran have signs or symptoms due to urolithiasis?       |
| \[ \] Yes \[ \] No                                                     |
|                                                                        |
| If yes, indicate severity (check all that apply)                       |
| \[ \] No symptoms or attacks of colic                                  |
| \[ \] Occasional attacks of colic                                      |
| \[ \] Frequent attacks of colic                                        |
| \[ \] Causing voiding dysfunction                                      |
| \[ \] Requires catheter drainage                                       |
| \[ \] Causing infection (pyonephrosis)                                 |
| \[ \] Causing hydronephrosis                                           |
| \[ \] Causing impaired kidney function                                 |
| \[ \] Other, describe:                                                 |

<span id="_Toc289419565" class="anchor"></span>Table 12: Rules: DBQ – Kidney Conditions (Nephrology) – 11. Remarks, if any

## Section 5. Urinary tract/kidney infection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 29%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>5. Urinary tract/kidney infection</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections?</td>
</tr>
<tr class="odd">
<td>If yes, provide etiology:</td>
<td><p>If <em>Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections?= Yes;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the etiology of the recurrent symptomatic urinary tract or kidney infections.</td>
</tr>
<tr class="even">
<td>If the Veteran has had recurrent symptomatic urinary tract or kidney infections, indicate all treatment modalities that apply:</td>
<td><p>If <em>Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections?= Yes;</em> Enabled; Mandatory; Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>[No treatment; OR Long-term drug therapy; Hospitalization; Drainage; Continuous intensive management; Intermittent intensive management; Other]</td>
<td>N/A</td>
<td>Please check one or more boxes to indicate applicable treatment modalities for recurrent symptomatic urinary tract or kidney infections.</td>
</tr>
<tr class="odd">
<td>If checked, list medications used and indicate dates for courses of treatment over the past 12 months:</td>
<td><p>If treatment modalities include <em>Long-term drug therapy;</em> Enabled; Mandatory</p>
<p>Else Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please list medications used for urinary tract or kidney infections and their treatment dates over the past 12 months.</td>
</tr>
<tr class="even">
<td>If checked, indicate frequency of hospitalization:</td>
<td><p>If treatment modalities include <em>Hospitalization;</em> Enabled; Mandatory</p>
<p>Else Disabled</p></td>
<td>[1 or 2 per year; &gt;2 per year]</td>
<td>N/A</td>
<td>Please indicate the frequency of hospitalization.</td>
</tr>
<tr class="odd">
<td>If checked, indicate dates when drainage performed over past 12 months:</td>
<td><p>If treatment modalities include <em>Drainage;</em> Enabled; Mandatory</p>
<p>Else Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please indicate the dates that drainage was performed over the past 12 months.</td>
</tr>
<tr class="even">
<td>If checked, indicate types of treatments and medications used over past 12 months:</td>
<td><p>If treatment modalities include <em>Continuous intensive management;</em> Enabled; Mandatory</p>
<p>Else Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the types of treatment and medications for continuous intensive management used over the past 12 months.</td>
</tr>
<tr class="odd">
<td>If checked, indicate types of treatments and medications used over past 12 months:</td>
<td><p>If treatment modalities include <em>Intermittent intensive management;</em> Enabled; Mandatory</p>
<p>Else Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the types of treatment and medications for intermittent intensive management used over the past 12 months.</td>
</tr>
<tr class="even">
<td>Other, describe:</td>
<td><p>If treatment modalities include <em>Other;</em> Enabled; Mandatory</p>
<p>Else Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe other treatment modalities used for urinary tract or kidney infections.</td>
</tr>
</tbody>
</table>

<span id="_Toc289419540" class="anchor"></span>Figure 13: Template Example: DBQ – Kidney Conditions (Nephrology) – 5. Urinary tract/kidney infection

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/012.png)

![](dvba-2-7-164-workflow-kidney-conditions-nephrology/013.png)

<span id="_Toc289419541" class="anchor"></span>Figure 14: Print Example: DBQ – Kidney Conditions (Nephrology) – 5. Urinary tract/kidney infection

| 5\. Urinary tract/kidney infection                                        |
|---------------------------------------------------------------------------|
| ---------------------------------                                         |
| Does the Veteran have a history of recurrent symptomatic urinary tract or |
| kidney infections?                                                        |
| \[ \] Yes \[ \] No                                                        |
|                                                                           |
| If yes, provide etiology:                                                 |
|                                                                           |
| If the Veteran has had recurrent symptomatic urinary tract or kidney      |
| infections, indicate all treatment modalities that apply:                 |
| \[ \] No treatment                                                        |
| \[ \] Long-term drug therapy                                              |
| If checked, list medications used and indicate dates courses              |
| for treatment over the past 12 months:                                    |
| \[ \] Hospitalization                                                     |
| If checked, indicate frequency of hospitalization:                        |
| \[ \] 1 or 2 per year                                                     |
| \[ \] \> 2 per year                                                       |
| \[ \] Drainage                                                            |
| If checked, indicate dates when drainage performed over past              |
| 12 months:                                                                |
| \[ \] Continuous intensive management                                     |
| If checked, indicate types of treatment and medications used              |
| over past 12 months:                                                      |
| \[ \] Intermittent intensive management                                   |
| If checked, indicate types of treatment and medications used              |
| over past 12 months:                                                      |
| \[ \] Other, describe:                                                    |

## Section 6. Kidney transplant or removal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 31%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>6. Kidney transplant or removal</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Has the Veteran had a kidney removed?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Has the Veteran had a kidney removed?</td>
</tr>
<tr class="odd">
<td>If yes, provide reason:</td>
<td><p>If <em>Has the Veteran had a kidney removed? = Yes;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>[Kidney donation; Due to disease; Due to trauma or injury; Other, describe:]</td>
<td>N/A</td>
<td>Please provide the reason a kidney was removed.</td>
</tr>
<tr class="even">
<td>Other, describe:</td>
<td>If <em>Reason = Other;</em> Enabled; Mandatory</td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other reason a kidney was removed.</td>
</tr>
<tr class="odd">
<td>b. Has the Veteran had a kidney transplant?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Has the Veteran had a kidney transplant?</td>
</tr>
<tr class="even">
<td>If yes, date of admission:</td>
<td><p>If <em>Has the Veteran had a kidney transplant? = Yes;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of admission of the kidney transplant.</td>
</tr>
<tr class="odd">
<td>Date of discharge:</td>
<td><p>If <em>Has the Veteran had a kidney transplant? = Yes;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of discharge of the kidney transplant.</td>
</tr>
</tbody>
</table>

<span id="_Toc289419542" class="anchor"></span>Figure 15: Template Example: DBQ – Kidney Conditions (Nephrology) – 6. Kidney transplant or removal

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/014.png)

<span id="_Toc289419543" class="anchor"></span>Figure 16: Print Example: DBQ – Kidney Conditions (Nephrology) – 6. Kidney transplant or removal

| 6\. Kidney transplant or removal             |
|----------------------------------------------|
| -------------------------------              |
| a\. Has the Veteran had a kidney removed?    |
| \[ \] Yes \[ \] No                           |
|                                              |
| If yes, provide reason:                      |
| \[ \] Kidney donation                        |
| \[ \] Due to disease                         |
| \[ \] Due to trauma or injury                |
| \[ \] Other, describe:                       |
|                                              |
| b\. Has the Veteran had a kidney transplant? |
| \[ \] Yes \[ \] No                           |
|                                              |
| If yes, date of admission:                   |
| Date of discharge:                           |

## Section 7. Tumors and Neoplasms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>7. Tumors and Neoplasms</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section?</td>
</tr>
<tr class="odd">
<td>If yes, complete the following:</td>
<td><p>If <em>Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section? = Yes;</em> Enabled; Read-Only</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>b. Is the neoplasm</td>
<td><p>If <em>Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section? = Yes;</em> Enabled; Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Benign; Malignant]</td>
<td>N/A</td>
<td>Please indicate whether the neoplasm is benign or malignant.</td>
</tr>
<tr class="odd">
<td>c. Has the Veteran completed treatment or is the Veteran currently undergoing treatment for a benign or malignant neoplasm or metastases?</td>
<td><p>If <em>Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section? = Yes;</em> Enabled; Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No, watchful waiting]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Has the Veteran completed treatment or is the Veteran currently undergoing treatment for a benign or malignant neoplasm or metastases?</td>
</tr>
<tr class="even">
<td>If yes, indicate type of treatment the Veteran is currently undergoing or has completed (check all that apply):</td>
<td><p>If <em>Has the Veteran completed treatment or is the Veteran currently undergoing treatment for a benign or malignant neoplasm or metastases? = Yes;</em> Enabled, Mandatory, Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>[Treatment completed; currently in watchful waiting status; Surgery; Radiation therapy; Antineoplastic chemotherapy; Other therapeutic procedure; Other therapeutic treatment]</td>
<td>N/A</td>
<td>Please indicate all applicable treatment types for a benign or malignant neoplasm or metastases that the Veteran either is undergoing or has completed.</td>
</tr>
<tr class="odd">
<td>If checked, describe:</td>
<td><p>If treatments include <em>Surgery;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the surgery.</td>
</tr>
<tr class="even">
<td>Date(s) of surgery:</td>
<td><p>If treatments include <em>Surgery;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date(s) of surgery.</td>
</tr>
<tr class="odd">
<td>Date of most recent treatment:</td>
<td><p>If treatments include <em>Radiation therapy</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the most recent radiation therapy treatment.</td>
</tr>
<tr class="even">
<td>Date of completion of treatment or anticipated date of completion: ­­­­­­­­­­­­</td>
<td><p>If treatments include <em>Radiation therapy</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date (actual or anticipated) of completion of the radiation therapy treatment.</td>
</tr>
<tr class="odd">
<td>Date of most recent treatment:</td>
<td><p>If treatments include <em>Antineoplastic chemotherapy</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the most recent antineoplastic chemotherapy treatment.</td>
</tr>
<tr class="even">
<td>Date of completion of treatment or anticipated date of completion:</td>
<td><p>If treatments include <em>Antineoplastic chemotherapy</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date (actual or anticipated) of the most recent antineoplastic chemotherapy treatment.</td>
</tr>
<tr class="odd">
<td>If checked, describe procedure:</td>
<td><p>If treatments include <em>Other therapeutic procedure;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other therapeutic procedure.</td>
</tr>
<tr class="even">
<td>Date of most recent procedure:</td>
<td><p>If treatments include <em>Other therapeutic procedure;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the most recent other therapeutic procedure.</td>
</tr>
<tr class="odd">
<td>If checked, describe treatment:</td>
<td><p>If treatments include <em>Other therapeutic treatment;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other therapeutic treatment.</td>
</tr>
<tr class="even">
<td>Date of completion of treatment or anticipated date of completion:</td>
<td><p>If treatments include <em>Other therapeutic treatment;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date (actual or anticipated) of completion of the other therapeutic treatment.</td>
</tr>
<tr class="odd">
<td>d. Does the Veteran currently have any residual conditions or complications due to the neoplasm (including metastases) or its treatment other than those already documented in the report above?</td>
<td><p>If <em>Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section? = Yes;</em> Enabled; Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td></td>
<td>Please indicate whether or not the Veteran has any residual conditions or complications due to the neoplasm (including metastases) or its treatment other than those already documented.</td>
</tr>
<tr class="even">
<td>If yes, list residual conditions and complications (brief summary):</td>
<td><p>If <em>previous question = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please list the residual conditions and complications due to the neoplasm (including metastases) or its treatment.</td>
</tr>
<tr class="odd">
<td>e. If there are additional benign or malignant neoplasms or metastases related to any of the diagnoses in the Diagnosis section, describe using the above format:</td>
<td><p>If <em>Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section? = Yes;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<span id="_Toc270513774" class="anchor"></span>Figure 17: Template Example: DBQ – Kidney Conditions (Nephrology) – 7. Tumors and Neoplasms

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/015.png)![](dvba-2-7-164-workflow-kidney-conditions-nephrology/016.png)

<span id="_Toc270513775" class="anchor"></span>Figure 18: Print Example: DBQ – Kidney Conditions (Nephrology) – 7. Tumors and Neoplasms

| 7\. Tumors and neoplasms                                                      |
|-------------------------------------------------------------------------------|
| -----------------------                                                       |
| a\. Does the Veteran have a benign or malignant neoplasm or metastases        |
| related to any of the diagnoses in the Diagnosis section?                     |
| \[ \] Yes \[ \] No                                                            |
|                                                                               |
| If yes, complete the following:                                               |
|                                                                               |
| b\. Is the neoplasm                                                           |
| \[ \] Benign \[ \] Malignant                                                  |
|                                                                               |
| c\. Has the Veteran completed treatment or is the Veteran currently           |
| undergoing treatment for a benign or malignant neoplasm or metastases?        |
| \[ \] Yes \[ \] No; watchful waiting                                          |
|                                                                               |
| If yes, indicate type of treatment the Veteran is currently undergoing or     |
| has completed (check all that apply):                                         |
| \[ \] Treatment completed; currently in watchful waiting status               |
| \[ \] Surgery                                                                 |
| If checked, describe:                                                         |
| Date(s) of surgery:                                                           |
| \[ \] Radiation therapy                                                       |
| Date of most recent treatment:                                                |
| Date of completion of treatment or anticipated date of completion:            |
|                                                                               |
| \[ \] Antineoplastic chemotherapy                                             |
| Date of most recent treatment:                                                |
| Date of completion of treatment or anticipated date of completion:            |
|                                                                               |
| \[ \] Other therapeutic procedure                                             |
| If checked, describe procedure:                                               |
| Date of most recent procedure:                                                |
| \[ \] Other therapeutic treatment                                             |
| If checked, describe treatment:                                               |
| Date of completion of treatment or anticipated date of completion:            |
|                                                                               |
|                                                                               |
| d\. Does the Veteran currently have any residual conditions or complications  |
| due to the neoplasm (including metastases) or its treatment, other than those |
| already documented in the report above?                                       |
| \[ \] Yes \[ \] No                                                            |
|                                                                               |
| If yes, list residual conditions and complications (brief summary):           |
|                                                                               |
| e\. If there are additional benign or malignant neoplasms or metastases       |
| related to any of the diagnoses in the Diagnosis section, describe using the  |
| above format:                                                                 |

## Section 8. Other pertinent physical findings, complications, signs and/or symptoms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 30%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>8. Other pertinent physical findings, complications, signs and/or symptoms</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have any scars (surgical or otherwise) related to any conditions or to the treatment of any conditions listed in the Diagnosis section above?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please indicate whether or not the Veteran has any scars (surgical or otherwise) related to any conditions (or their treatment) listed in the Diagnosis section.</td>
</tr>
<tr class="odd">
<td>If yes, are any of the scars painful and/or unstable, or is the total area of all related scars greater than 39 square cm (6 square inches)?</td>
<td><p>If <em>previous question = Yes;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not any of the scars are painful and/or unstable, or if the total area of all related scars is greater than 39 square cm (6 square inches).</td>
</tr>
<tr class="even">
<td>If yes, also complete a Scars Questionnaire.</td>
<td><p>If <em>previous question = Yes;</em> Enabled, Read-Only</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>b. Does the Veteran have any other pertinent physical findings, complications, conditions, signs or symptoms?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have any other pertinent physical findings, complications, conditions, signs or symptoms?</td>
</tr>
<tr class="even">
<td>If yes, describe (brief summary):</td>
<td><p>If <em>Does the Veteran have any other pertinent physical findings, complications, conditions, signs and/or symptoms?= Yes;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe any other pertinent physical findings, complications, conditions, signs or symptoms.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513777" class="anchor"></span>Figure 19: Template Example: DBQ – Kidney Conditions (Nephrology) – 8. Other pertinent physical findings, complications, signs and/or symptoms

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/017.png)

<span id="_Toc270513778" class="anchor"></span>Figure 20: Print Example: DBQ – Kidney Conditions (Nephrology) – 8. Other pertinent physical findings, complications, signs and/or symptoms

| 8\. Other pertinent physical findings, complications, conditions, signs    |
|----------------------------------------------------------------------------|
| and/or symptoms                                                            |
| ----------------------------------------------------------------------     |
| a\. Does the Veteran have any scars (surgical or otherwise) related to any |
| conditions or to the treatment of any conditions listed in the Diagnosis   |
| section above?                                                             |
| \[ \] Yes \[ \] No                                                         |
|                                                                            |
| If yes, are any of the scars painful and/or unstable, or is the total      |
| area of all related scars greater than 39 square cm (6 square inches)?     |
| \[ \] Yes \[ \] No                                                         |
|                                                                            |
| If yes, also complete a Scars Questionnaire.                               |
|                                                                            |
| b\. Does the Veteran have any other pertinent physical findings,           |
| complications, conditions, signs or symptoms?                              |
| \[ \] Yes \[ \] No                                                         |
|                                                                            |
| If yes, describe (brief summary):                                          |

## Section 9. Diagnostic testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 27%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>9. Diagnostic testing</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>NOTE: If laboratory test results are in the medical record and reflect the Veteran’s current renal function, repeat testing is not required.</td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>a. Has the Veteran had laboratory or other diagnostic studies performed?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Has the Veteran had laboratory or other diagnostic studies performed?</td>
</tr>
<tr class="even">
<td>If yes, provide most recent results, if available:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes;</em> Enabled; Read-Only</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>b. Laboratory studies</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes;</em> Enabled; Optional; Choose one or more valid values.</p>
<p>Else; Enabled, Optional</p></td>
<td>[BUN; Creatinine; EGFR]</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td><p>BUN:</p>
<p>Date:</p></td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes</em> and If <em>Laboratory studies include BUN;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No</em> and If <em>Laboratory studies include BUN;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the BUN laboratory study.</td>
</tr>
<tr class="odd">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes</em> and If <em>Laboratory studies include BUN;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No</em> and If <em>Laboratory studies include BUN;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the result of the BUN laboratory study.</td>
</tr>
<tr class="even">
<td><p>Creatinine:</p>
<p>Date:</p></td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes</em> and If <em>Laboratory studies include Creatinine;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No</em> and If <em>Laboratory studies include Creatinine;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the creatinine laboratory study.</td>
</tr>
<tr class="odd">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes</em> and If <em>Laboratory studies include Creatinine;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No</em> and If <em>Laboratory studies include Creatinine;</em> Enabled; Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the result of the creatinine laboratory study.</td>
</tr>
<tr class="even">
<td><p>EGFR:</p>
<p>Date:</p></td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes</em> and If <em>Laboratory studies include EGFR;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No</em> and If <em>Laboratory studies include EGFR;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the EGFR laboratory study.</td>
</tr>
<tr class="odd">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes</em> and If <em>Laboratory studies include EGFR;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No</em> and If <em>Laboratory studies include EGFR;</em> Enabled; Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the result of the EGFR laboratory study.</td>
</tr>
<tr class="even">
<td>c. Urinalysis:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes;</em> Enabled; Optional; Choose one or more valid values</p>
<p>Else; Enabled, Optional</p></td>
<td>[Hyaline casts; Granular casts; RBC’s/HPF; Protein (albumin); Spot urine for protein/creatinine ratio; 24 hour protein (albumin)]</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td><p>Hyaline casts:</p>
<p>Date</p></td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes Hyaline casts;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes Hyaline casts;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the hyaline casts urinalysis.</td>
</tr>
<tr class="even">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes Hyaline casts;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes Hyaline casts;</em> Enabled; Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the result of the hyaline casts urinalysis.</td>
</tr>
<tr class="odd">
<td><p>Granular casts:</p>
<p>Date:</p></td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes Granular casts;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes Granular casts;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the granular casts urinalysis.</td>
</tr>
<tr class="even">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes Granular casts;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes Granular casts;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the results of the granular casts urinalysis.</td>
</tr>
<tr class="odd">
<td><p>RBC’s/HPF:</p>
<p>Date:</p></td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes RBC’s/HPF;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes RBC’s/HPF;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the RBC’s/HPF urinalysis.</td>
</tr>
<tr class="even">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes RBC’s/HPF;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes RBC’s/HPF;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the result of the RBC’s/HPF urinalysis.</td>
</tr>
<tr class="odd">
<td><p>Protein (albumin):</p>
<p>Date:</p></td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes Protein (albumin);</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes Protein (albumin);</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the protein (albumin) urinalysis.</td>
</tr>
<tr class="even">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes Protein (albumin);</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes Protein (albumin);</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the result of the protein (albumin) urinalysis.</td>
</tr>
<tr class="odd">
<td>Spot urine for protein/creatinine ratio: Date:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes Spot urine for protein/creatinine ratio ;</em>Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes Spot urine for protein/creatinine ratio;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of spot urine for protein/creatinine ratio urinalysis.</td>
</tr>
<tr class="even">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes Spot urine for protein/creatinine ratio;</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes Spot urine for protein/creatinine ratio;</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the result of spot urine for protein/creatinine ratio urinalysis.</td>
</tr>
<tr class="odd">
<td><p>24 hour protein (albumin):</p>
<p>Date:</p></td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes 24 hour protein (albumin);</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes 24 hour protein (albumin);</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the 24 hour protein (albumin) urinalysis.</td>
</tr>
<tr class="even">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and</em> If <em>Urinalysis includes 24 hour protein (albumin);</em> Enabled; Mandatory</p>
<p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = No and</em> If <em>Urinalysis includes 24 hour protein (albumin);</em> Enabled; Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the result of the 24 hour protein (albumin) urinalysis.</td>
</tr>
<tr class="odd">
<td>d. Urine microalbumin: Date:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and Urine microalbumin result is populated;</em> Enabled; Mandatory</p>
<p>Else; Enabled; Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the urine microalbumin test.</td>
</tr>
<tr class="even">
<td>Result:</td>
<td><p>If <em>Has the Veteran had laboratory or other diagnostic studies performed? = Yes and Urine microalbumin date is populated;</em> Enabled; Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the result of the urine microalbumin test.</td>
</tr>
<tr class="odd">
<td>e. Are there any other significant diagnostic test findings and/or results?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled; Mandatory; Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Are there any other significant diagnostic test findings and/or results?</td>
</tr>
<tr class="even">
<td>If yes, provide type of test or procedure, date and results (brief summary):</td>
<td><p>If <em>Are there any other significant diagnostic test findings and/or results? = Yes;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the type of test or procedure, date and results.</td>
</tr>
</tbody>
</table>

<span id="_Toc289419548" class="anchor"></span>Figure 21: Template Example: DBQ – Kidney Conditions (Nephrology) – 9. Diagnostic testing

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/018.png)![](dvba-2-7-164-workflow-kidney-conditions-nephrology/019.png)

<span id="_Toc289419549" class="anchor"></span>Figure 22: Print Example: DBQ – Kidney Conditions (Nephrology) – 9. Diagnostic testing

| 9\. Diagnostic testing                                                       |
|------------------------------------------------------------------------------|
| ---------------------                                                        |
| NOTE: If laboratory test results are in the medical record and reflect the   |
| Veteran's current renal function, repeat testing is not required.            |
|                                                                              |
| a\. Has the Veteran had laboratory or other diagnostic studies performed?    |
| \[ \] Yes \[ \] No                                                           |
|                                                                              |
| If yes, provide most recent results, if available:                           |
|                                                                              |
| b\. Laboratory studies                                                       |
| \[ \] BUN: Date: Result:                                                     |
| \[ \] Creatinine: Date: Result:                                              |
| \[ \] EGFR: Date: Result:                                                    |
|                                                                              |
| c\. Urinalysis:                                                              |
| \[ \] Hyaline casts: Date: Result:                                           |
| \[ \] Granular casts: Date: Result:                                          |
| \[ \] RBC's/HPF: Date: Result:                                               |
| \[ \] Protein (albumin): Date: Result:                                       |
| \[ \] Spot urine for protein/creatinine ratio:                               |
| Date: Result:                                                                |
| \[ \] 24 hour protein (albumin):                                             |
| Date: Result:                                                                |
|                                                                              |
| d\. Urine microalbumin: Date: Result:                                        |
|                                                                              |
| e\. Are there any other significant diagnostic test findings and/or results? |
| \[ \] Yes \[ \] No                                                           |
|                                                                              |
| If yes, provide type of test or procedure, date and results (brief           |
| summary):                                                                    |

## Section 10. Functional impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 30%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong><u>10. Functional impact</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran’s kidney condition(s), including neoplasms, if any, impact his or her ability to work?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis is selected in the Diagnosis section</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran’s kidney condition(s), including neoplasms, if any, impact his or her ability to work.</td>
</tr>
<tr class="odd">
<td>If yes, describe impact of each of the Veteran’s kidney conditions, providing one or more examples:</td>
<td>If <em>Does the Veteran’s kidney condition(s) impact his or her ability to work? = Yes</em>; Enabled; Mandatory</td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the impact of each of the Veteran’s kidney condition(s) (including neoplasms, if any) on his or her ability to work, providing one or more examples.</td>
</tr>
</tbody>
</table>

<span id="_Toc289419550" class="anchor"></span>Figure 23: Template Example: DBQ – Kidney Conditions (Nephrology) – 10. Functional impact

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/020.png)

<span id="_Toc289419551" class="anchor"></span>Figure 24: Print Example: DBQ – Kidney Conditions (Nephrology) – 10. Functional impact

| 10\. Functional impact                                                      |
|-----------------------------------------------------------------------------|
| ---------------------                                                       |
| Does the Veteran's kidney condition(s), including neoplasms, if any, impact |
| his or her ability to work?                                                 |
| \[X\] Yes \[ \] No                                                          |
|                                                                             |
| If yes, describe impact of each of the Veteran's kidney conditions,         |
| providing one or more examples:                                             |

## Section 11. Remarks, if any

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below.

| Field/Question             | Field Disposition | Valid Values | Format | Error Message |
|--------------------------------|-----------------------|------------------|------------|-------------------|
| <u>11. Remarks, if any</u> | Enabled*,* Optional   | N/A              | Free Text  | N/A               |

<span id="_Toc289419552" class="anchor"></span>Figure 25: Template Example: DBQ – Kidney Conditions (Nephrology) – 11. Remarks, if any

> ![](dvba-2-7-164-workflow-kidney-conditions-nephrology/021.png)

<span id="_Toc289419553" class="anchor"></span>Figure 26: Print Example: DBQ – Kidney Conditions (Nephrology) – 11. Remarks, if any

| 11\. Remarks, if any |
|----------------------|
| -------------------  |

# Kidney Conditions (Nephrology) DBQ-AMIE Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The DBQ-AMIE worksheets are accessed via the Print Blank C&P Worksheet menu \[DVBA C PRINT BLANK C&P WORKSHE\] option.  Select the “DBQ KIDNEY CONDITIONS (NEPHROLOGY)” worksheet.   DBQ-AMIE worksheets should be sent to a printer.

Kidney Conditions (Nephrology)

Disability Benefits Questionnaire

Name of patient/Veteran: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ SSN: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Your patient is applying to the U. S. Department of Veterans Affairs (VA) for

disability benefits. VA will consider the information you provide on this

questionnaire as part of their evaluation in processing the Veteran's claim.

1\. Diagnosis:

Does the Veteran now have or has he/she ever been diagnosed with a kidney

condition?

\_\_\_ Yes \_\_\_ No

If no, provide rationale (e.g., Veteran has never had any known kidney

condition(s)):\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If yes, indicate diagnoses: (check all that apply)

\_\_\_ Diabetic nephropathy ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Glomerulonephritis ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Hydronephrosis ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Interstitial nephritis ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Kidney transplant ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Nephrosclerosis ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Nephrolithiasis ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Renal artery stenosis ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Ureterolithiasis ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Neoplasm of the kidney

ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_

\_\_\_ Other kidney condition (specify diagnosis, providing only diagnoses

that pertain to kidney conditions.)

Other diagnosis \#1: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Other diagnosis \#2: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If there are additional diagnoses that pertain to kidney conditions, list

using above format: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2\. Medical history

Describe the history (including cause, onset and course) of the Veteran's

kidney condition: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 2

Disability Benefits Questionnaire for

Kidney Conditions (Nephrology)

3\. Renal dysfunction

a\. Does the Veteran have renal dysfunction?

\_\_\_ Yes \_\_\_ No

If yes, does the Veteran require regular dialysis?

\_\_\_ Yes \_\_\_ No

b\. Does the Veteran have any signs or symptoms due to renal dysfunction?

\_\_\_ Yes \_\_\_ No

If yes,check all that apply:

\_\_\_ Proteinuria (albuminuria)

If checked, indicate frequency: (check all that apply)

\_\_\_ Recurring \_\_\_ Constant \_\_\_ Persistent

\_\_\_ Edema (due to renal dysfunction)

If checked, indicate frequency: (check all that apply)

\_\_\_ Some \_\_\_ Transient \_\_\_ Slight \_\_\_ Persistent

\_\_\_ Anorexia (due to renal dysfunction)

\_\_\_ Weight loss (due to renal dysfunction)

If checked, provide baseline weight (average weight for 2-year period

preceding onset of disease): \_\_\_\_\_\_\_\_\_\_\_\_

Provide current weight: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Generalized poor health due to renal dysfunction

\_\_\_ Lethargy due to renal dysfunction

\_\_\_ Weakness due to renal dysfunction

\_\_\_ Limitation of exertion due to renal dysfunction

\_\_\_ Able to perform only sedentary activity, due to persistent edema

caused by renal dysfunction

\_\_\_ Markedly decreased function other organ systems, especially the

cardiovascular system, caused by renal dysfunction

If checked, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

c\. Does the Veteran have hypertension and/or heart disease due to renal

dysfunction or caused by any kidney condition?

\_\_\_ Yes \_\_\_ No

If yes, also complete the Hypertension and/or Heart Disease Questionnaire

as appropriate.

Page: 3

Disability Benefits Questionnaire for

Kidney Conditions (Nephrology)

4\. Urolithiasis

a\. Does the Veteran have kidney, ureteral or bladder calculi?

\_\_\_ Yes \_\_\_ No

If yes, indicate location (check all that apply)

\_\_\_ Kidney \_\_\_ Ureter \_\_\_Bladder

If the Veteran has urolithiasis, complete the following:

b\. Has the Veteran had treatment for recurrent stone formation in the kidney,

ureter or bladder?

\_\_\_ Yes \_\_\_ No

If yes, indicate treatment: (check all that apply)

\_\_\_ Diet therapy

If checked, specify diet and dates of use: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Drug therapy

If checked, list medication and dates of use: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Invasive or non-invasive procedures

If checked, indicate average number of times per year invasive or

non-invasive procedures were required:

\_\_\_ 0 to 1 per year \_\_\_ 2 per year \_\_\_ \> 2 per year

Date and facility of most recent invasive or non-invasive procedure:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

c\. Does the Veteran have signs or symptoms due to urolithiasis?

\_\_\_ Yes \_\_\_ No

If yes, indicate severity (check all that apply):

\_\_\_ No symptoms or attacks of colic

\_\_\_ Occasional attacks of colic

\_\_\_ Frequent attacks of colic

\_\_\_ Causing voiding dysfunction

\_\_\_ Requires catheter drainage

\_\_\_ Causing infection (pyonephrosis)

\_\_\_ Causing hydronephrosis

\_\_\_ Causing impaired kidney function

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 4

Disability Benefits Questionnaire for

Kidney Conditions (Nephrology)

5\. Urinary tract/kidney infection

Does the Veteran have a history of recurrent symptomatic urinary tract or

kidney infections?

\_\_\_ Yes \_\_\_ No

If yes, provide etiology: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If the Veteran has had recurrent symptomatic urinary tract or kidney

infections, indicate all treatment modalities that apply:

\_\_\_ No treatment

\_\_\_ Long-term drug therapy

If checked, list medications used and indicate dates for courses of

treatment over the past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Hospitalization

If checked, indicate frequency of hospitalization:

\_\_\_ 1 or 2 per year

\_\_\_ \> 2 per year

\_\_\_ Drainage

If checked, indicate dates when drainage performed over past 12

months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Continuous intensive management

If checked, indicate types of treatment and medications used over

past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Intermittent intensive management

If checked, indicate types of treatment and medications used over

past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

6\. Kidney transplant or removal

a\. Has the Veteran had a kidney removed?

\_\_\_ Yes \_\_\_ No

If yes, provide reason:

\_\_\_ Kidney donation

\_\_\_ Due to disease

\_\_\_ Due to trauma or injury

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. Has the Veteran had a kidney transplant?

\_\_\_ Yes \_\_\_ No

If yes, date of admission: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of discharge: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 5

Disability Benefits Questionnaire for

Kidney Conditions (Nephrology)

7\. Tumors and neoplasms

a\. Does the Veteran have a benign or malignant neoplasm or metastases

related to any of the diagnoses in the Diagnosis section?

\_\_\_ Yes \_\_\_ No

If yes, complete the following:

b\. Is the neoplasm

\_\_\_ Benign \_\_\_ Malignant

c\. Has the Veteran completed treatment or is the Veteran currently undergoing

treatment for a benign or malignant neoplasm or metastases?

\_\_\_ Yes \_\_\_ No; watchful waiting

If yes, indicate type of treatment the Veteran is currently undergoing or

has completed (check all that apply):

\_\_\_ Treatment completed; currently in watchful waiting status

\_\_\_ Surgery

If checked, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date(s) of surgery: \_\_\_\_\_\_\_\_\_

\_\_\_ Radiation therapy

Date of most recent treatment: \_\_\_\_\_\_\_\_\_\_\_

Date of completion of treatment or anticipated date of

completion: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Antineoplastic chemotherapy

Date of most recent treatment: \_\_\_\_\_\_\_\_\_\_\_

Date of completion of treatment or anticipated date of

completion: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other therapeutic procedure

If checked, describe procedure: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of most recent procedure: \_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other therapeutic treatment

If checked, describe treatment: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of completion of treatment or anticipated date of

completion: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

d\. Does the Veteran currently have any residual conditions or complications

due to the neoplasm (including metastases) or its treatment, other than those

already documented in the report above?

\_\_\_ Yes \_\_\_ No

If yes, list residual conditions and complications (brief summary): \_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

e\. If there are additional benign or malignant neoplasms or metastases

related to any of the diagnoses in the Diagnosis section, describe using the

above format: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 6

Disability Benefits Questionnaire for

Kidney Conditions (Nephrology)

8\. Other pertinent physical findings, complications, conditions, signs and/or

symptoms

a\. Does the Veteran have any scars (surgical or otherwise) related to any

conditions or to the treatment of any conditions listed in the Diagnosis

section above?

\_\_\_ Yes \_\_\_ No

If yes, are any of the scars painful and/or unstable, or is the total area

of all related scars greater than 39 square cm (6 square inches)?

\_\_\_ Yes \_\_\_ No

If yes, also complete a Scars Questionnaire.

b\. Does the Veteran have any other pertinent physical findings,

complications, conditions, signs and/or symptoms?

\_\_\_ Yes \_\_\_ No

If yes, describe (brief summary): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9\. Diagnostic testing

> **NOTE:** If laboratory test results are in the medical record and reflect the

Veteran's current renal function, repeat testing is not required.

a\. Has the Veteran had laboratory or other diagnostic studies performed?

\_\_\_ Yes \_\_\_ No

If yes, provide most recent results, if available:

b\. Laboratory studies

\_\_\_ BUN: Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Creatinine: Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ EGFR: Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

c\. Urinalysis:

\_\_\_ Hyaline casts: Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Granular casts: Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ RBC's/HPF: Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Protein (albumin): Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Spot urine for

protein/creatinine ratio: Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ 24 hour protein (albumin): Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

d\. Urine microalbumin: Date: \_\_\_\_\_\_\_\_\_\_\_ Result: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

e\. Are there any other significant diagnostic test findings and/or results?

\_\_\_ Yes \_\_\_ No

If yes, provide type of test or procedure, date and results (brief summary):

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 7

Disability Benefits Questionnaire for

Kidney Conditions (Nephrology)

10\. Functional impact

Does the Veteran's kidney condition(s), including neoplasms, if any, impact

his or her ability to work?

\_\_\_ Yes \_\_\_ No

If yes, describe impact of each of the Veteran's kidney conditions, providing

one or more examples: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

11\. Remarks, if any: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_

Physician printed name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Phone: \_\_\_\_\_\_\_\_\_\_\_

Medical license \#: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Fax: \_\_\_\_\_\_\_\_\_\_\_\_\_

Physician address: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> **NOTE:** VA may request additional medical information, including additional

examinations if necessary to complete VA's review of the Veteran's

application.