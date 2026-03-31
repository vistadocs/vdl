---
title: DVBA*2.7*163 Workflow - Male Reproductive System Conditions
doc_type: WF
doc_label: Workflow Guide
doc_layer: patch
doc_subject: Workflow - Male Reproductive System Conditions
app_code: CAPRI
app_name: Compensation and Pension Record Interchange
section: FIN
app_status: active
pkg_ns: DVBA
patch_ver: 2.7
patch_id: DVBA*2.7*163
group_key: "CAPRI:DVBA:2.7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - diagnosis
  - class
  - enabled
  - strong
  - mandatory
  - veteran
  - male
  - reproductive
  - else
  - please
page_count: 0
word_count: 13912
section_count: 17
table_count: 96
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_p163_dbq_malereproductive_wf.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_p163_dbq_malereproductive_wf.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=133"
---

![](dvba-2-7-163-workflow-male-reproductive-system-conditions/001.png)

Compensation and Pension Record Interchange (CAPRI)

Male Reproductive System Conditions

Disability Benefits Questionnaire (DBQ)

Workflow

April 2011

Office of Enterprise Development

Management & Financial Systems  
Revision History

<table>
<caption><p><span id="_Toc270513758" class="anchor"></span>Table 1: Rules: DBQ – Male Reproductive System Conditions – Name of patient/Veteran</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 51%" />
<col style="width: 19%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Date</td>
<td>Description (Patch # if applicable)</td>
<td>Author</td>
<td>Technical Writer</td>
</tr>
<tr class="even">
<td>2/1/2011</td>
<td>Document created</td>
<td>REDACTED</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>4/1/2011</td>
<td>Changes for patch 163</td>
<td>REDACTED</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>4/7/11</td>
<td><p>Changed mandatory logic to “Please describe the appliance used for the voiding dysfunction.”</p>
<p>Changed If yes, describe: to If yes, describe the appliance</p></td>
<td>REDACTED</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<span id="_Toc270513758" class="anchor"></span>Table 1: Rules: DBQ – Male Reproductive System Conditions – Name of patient/Veteran

  
Table of Contents

Table of Figures and Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Overview](#overview)
- [Male Reproductive System Conditions DBQ](#male-reproductive-system-conditions-dbq)
  - [Name of patient/Veteran](#name-of-patientveteran)
  - [Section 1. Diagnosis](#section-1-diagnosis)
  - [Section 2. Medical history](#section-2-medical-history)
  - [Section 3. Voiding dysfunction](#section-3-voiding-dysfunction)
  - [Section 4. Urinary tract/kidney infection](#section-4-urinary-tractkidney-infection)
  - [Section 5. Erectile dysfunction](#section-5-erectile-dysfunction)
  - [Section 6. Retrograde ejaculation](#section-6-retrograde-ejaculation)
  - [Section 7. Male reproductive organ infections](#section-7-male-reproductive-organ-infections)
  - [Section 8. Physical exam](#section-8-physical-exam)
  - [Section 9. Tumors and Neoplasms](#section-9-tumors-and-neoplasms)
  - [Section 10. Other pertinent physical findings, complications, conditions, signs and/or symptoms](#section-10-other-pertinent-physical-findings-complications-conditions-signs-andor-symptoms)
  - [Section 11. Diagnostic testing](#section-11-diagnostic-testing)
  - [Section 12. Functional impact](#section-12-functional-impact)
  - [## ## Section 13. Remarks, if any](#section-13-remarks-if-any)
- [Male Reproductive System Conditions DBQ-AMIE Worksheet](#male-reproductive-system-conditions-dbq-amie-worksheet)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides a high level overview of the contents found on the Male Reproductive System Conditions Disability Benefits Questionnaire (DBQ). The DBQ can be populated via an online template within the CAPRI C&P Worksheets tab and then printed OR it can be printed via AMIE (AUTOMATED MEDICAL INFORMATION EXCHANGE) and then manually populated. This document contains the edit rules for the template as well as an example of how the template will look online in CAPRI or printed from CAPRI. It also contains the layout for the AMIE worksheet to depict how it will look when printed from AMIE.

For more detailed information on standard template functionality not covered in this document, please refer to the *C&P Worksheet Tab Functionalities* section of the [CAPRI GUI User Guide](http://www4.va.gov/vdl/documents/Financial_Admin/CAPRI/capri_um.pdf).

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Male Reproductive System Conditions DBQ provides the ability to capture information related to Male Reproductive Organs and its treatment.

Each DBQ template contains a standard footer containing a note stating that “VA may request additional medical information, including additional examinations if necessary to complete VA’s review of the Veteran’s application.” (see Figure 1 and 2).

<span id="_Toc270513756" class="anchor"></span>Figure 1: Template Example: DBQ - Standard VA Note

![](dvba-2-7-163-workflow-male-reproductive-system-conditions/002.png)

<span id="_Toc270513757" class="anchor"></span>Figure 2: Print Example: DBQ – Standard VA Note

|                                                                                     |
|-------------------------------------------------------------------------------------|
| NOTE: VA may request additional medical information, including additional       |
| examinations if necessary to complete VA's review of the Veteran's application. |
|                                                                                     |

<span id="_Toc290013907" class="anchor"></span>Table 2: Rules: DBQ – Male Reproductive System Conditions – 1. Diagnosis

A number of fields on the Male Reproductive System Conditions DBQ are mandatory and require a response (value) prior to the exam being marked as completed. Some questions may activate a Pop-up window displaying information as to each question that needs to be answered before the template can be completed.

# Male Reproductive System Conditions DBQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Name of patient/Veteran

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

| Field/Question                                                                                                                                                                                                                       | Field Disposition | Valid Values | Format | Error Message                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------|------------|-----------------------------------------------|
| Male Reproductive System Conditions                                                                                                                                                                                                  | Enabled, Read-Only    | N/A              | N/A        | N/A                                           |
| Disability Benefits Questionnaire                                                                                                                                                                                                    | Enabled, Read-Only    | N/A              | N/A        | N/A                                           |
| Name of patient/Veteran:                                                                                                                                                                                                                 | Enabled, Mandatory    | N/A              | Free Text  | Please enter the name of the patient/Veteran. |
| Your patient is applying to the U. S. Department of Veterans Affairs (VA) for disability benefits. VA will consider the information you provide on this questionnaire as part of their evaluation in processing the Veteran’s claim. | Enabled, Read-Only    | N/A              | N/A        | N/A                                           |

<span id="_Toc270513764" class="anchor"></span>Table 3: Rules: DBQ – Male Reproductive System Conditions – 2. Medical history

<span id="_Toc270513759" class="anchor"></span>Figure 3: Template Example: DBQ – Male Reproductive System Conditions – Name of patient/Veteran

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/003.png)

<span id="_Toc270513760" class="anchor"></span>Figure 4: Print Example: DBQ – Male Reproductive System Conditions – Name of patient/Veteran

| Male Reproductive System Conditions                                           |
|-------------------------------------------------------------------------------|
| Disability Benefits Questionnaire                                             |
|                                                                               |
| Name of patient/Veteran:                                                      |
|                                                                               |
| Your patient is applying to the U.S. Department of Veterans Affairs (VA)      |
| for disability benefits. VA will consider the information you provide on this |
| questionnaire as part of their evaluation in processing the Veteran's claim.  |

<span id="_Toc270513767" class="anchor"></span>Table 4: Rules: DBQ – Male Reproductive System Conditions – 3. Voiding dysfunction

## Section 1. Diagnosis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The question “Does the Veteran now have or has he ever been diagnosed with any conditions of the male reproductive system?” must be answered before the template can be completed.

- If it is answered with Yes, all other questions requiring an answer as described by the rules in this document must be answered before the template can be completed.
- If it is answered with No, the rationale must be completed. The remainder of the template may be completed without answering any additional questions or the user may input answers to any of the optional questions as indicated by the rules described in this document.

All questions will be printed even if they have not been answered.

If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below and must be answered before this template can be completed.

<table>
<caption><p><span id="_Toc270513770" class="anchor"></span>Table 5: Rules: DBQ – Male Reproductive System Conditions – 4.Urinary tract/kidney infection</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 10%" />
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
<td>Does the Veteran now have or has he ever been diagnosed with any conditions of the male reproductive system?</td>
<td>Enabled, Mandatory; Choose one valid value</td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran now have or has he ever been diagnosed with any conditions of the male reproductive system?</td>
</tr>
<tr class="odd">
<td>If no, provide rationale (e.g., Veteran has never had any known male reproductive organ conditions):</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with any conditions of the male reproductive system?</em> = <em>No</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the rationale for indicating the Veteran has not been diagnosed with a condition of the male reproductive system.</td>
</tr>
<tr class="even">
<td>If yes, indicate diagnoses (check all that apply):</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with any conditions of the male reproductive system?</em> <em>= Yes;</em> Enabled, Mandatory; Choose one or more valid values</p>
<p>Else; Enabled, Optional</p></td>
<td>[Erectile dysfunction; Penis, deformity (e.g., Peyronie’s); Testis, atrophy, one or both; Testis, removal, one or both; Epididymitis, chronic; Epididymo-orchitis, chronic; Prostate injury; prostate hypertrophy (BPH); Prostatitis, chronic; Prostate surgical residuals (as addressed in items 3-6); Neoplasms of the male reproductive system; Other male reproductive system condition (specify diagnosis, providing only diagnoses that pertain to male reproductive system)]</td>
<td>N/A</td>
<td>Please indicate the Veteran’s male reproductive system diagnosis.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Erectile dysfunction;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and if <em>Diagnosis includes Erectile dysfunction</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Erectile dysfunction.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Erectile dysfunction;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and if <em>Diagnosis includes Erectile dysfunction</em>; Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Erectile dysfunction.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Penis, deformity (e.g. Peyronie’s);</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and if <em>Diagnosis includes Penis, deformity (e.g. Peyronie’s).;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Penis, deformity (e.g. Peyronie’s).</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Penis, deformity (e.g. Peyronie’s);</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and if <em>Diagnosis includes Penis, deformity (e.g. Peyronie’s).;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Penis, deformity (e.g. Peyronie’s).</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Testis, atrophy, one or both;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and if <em>Diagnosis includes Testis, atrophy, one or both;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Testis, atrophy, one or both.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Testis, atrophy, one or both;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and if <em>Diagnosis includes Testis, atrophy, one or both;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Testis, atrophy, one or both.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Testis, removal, one or both;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and if <em>Diagnosis includes Testis, removal, one or both;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Testis, removal, one or both.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Testis, removal, one or both;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Testis, removal, one or both;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Testis, removal, one or both.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Epididymitis, chronic;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Epididymitis, chronic;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Epididymitis, chronic.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Epididymitis, chronic;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Epididymitis, chronic;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Epididymitis, chronic.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Epididymo-orchitis, chronic;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Epididymo-orchitis, chronic;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Epididymo-orchitis, chronic.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Epididymo-orchitis, chronic;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Epididymo-orchitis, chronic;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Epididymo-orchitis, chronic.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Prostate injury;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Prostate injury;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Prostate injury.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Prostate injury;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Prostate injury;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Prostate injury.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Prostate hypertrophy (BPH);</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Prostate hypertrophy (BPH);</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Prostate hypertrophy (BPH).</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Prostate hypertrophy (BPH);</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Prostate hypertrophy (BPH);</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Prostate hypertrophy (BPH).</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Prostatitis, chronic;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Prostatitis, chronic;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Prostatitis, chronic.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Prostatitis, chronic;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Prostatitis, chronic;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Prostatitis, chronic.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Prostate surgical residuals;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Prostate surgical residuals;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Prostate surgical residuals (as addressed in items 3-6).</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Prostate surgical residuals;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Prostate surgical residuals;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis for Prostate surgical residuals (as addressed in items 3-6).</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Neoplasms of the male reproductive system;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Neoplasms of the male reproductive system;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Neoplasms of the male reproductive system.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Neoplasms of the male reproductive system;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No a</em>nd if <em>Diagnosis includes Neoplasms of the male reproductive system;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of Neoplasms of the male reproductive system.</td>
</tr>
<tr class="odd">
<td>ICD Code:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Other male reproductive system condition (specify diagnosis, providing only diagnoses that pertain to male reproductive system.);</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and if <em>Diagnosis includes Other male reproductive system condition (specify diagnosis, providing only diagnoses that pertain to male reproductive system.);</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for Other male reproductive system condition (specify diagnosis, providing only diagnoses that pertain to male reproductive system.</td>
</tr>
<tr class="even">
<td>Date of Diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and if <em>Diagnosis includes Other male reproductive system condition (specify diagnosis, providing only diagnoses that pertain to male reproductive system.);</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and if <em>Diagnosis includes Other male reproductive system condition (specify diagnosis, providing only diagnoses that pertain to male reproductive system.);</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of Other male reproductive system condition (specify diagnosis, providing only diagnoses that pertain to male reproductive system.</td>
</tr>
<tr class="odd">
<td>Other diagnosis #1:</td>
<td>Enabled, Optional</td>
<td>N/A</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>ICD code:</td>
<td><p>If <em>Diagnosis = Yes</em> and <em>Other diagnosis #1 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for other diagnosis #1.</td>
</tr>
<tr class="odd">
<td>Date of diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and <em>Other diagnosis #1 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of other diagnosis #1.</td>
</tr>
<tr class="even">
<td>Other diagnosis #2:</td>
<td>Enabled, Optional</td>
<td>N/A</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>ICD code:</td>
<td><p>If <em>Diagnosis = Yes</em> and <em>Other diagnosis #2 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for other diagnosis #2.</td>
</tr>
<tr class="even">
<td>Date of diagnosis:</td>
<td><p>If <em>Diagnosis = Yes</em> and <em>Other diagnosis #2 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of other diagnosis #2.</td>
</tr>
<tr class="odd">
<td>If there are additional diagnoses that pertain to the male reproductive organ conditions, list using above format:</td>
<td>Enabled, Optional</td>
<td>N/A</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<span id="_Toc270513770" class="anchor"></span>Table 5: Rules: DBQ – Male Reproductive System Conditions – 4.Urinary tract/kidney infection

<span id="_Toc270513762" class="anchor"></span>Figure 5: Template Example: DBQ – Male Reproductive System Conditions – 1. Diagnosis

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/004.png)![](dvba-2-7-163-workflow-male-reproductive-system-conditions/005.png)![](dvba-2-7-163-workflow-male-reproductive-system-conditions/006.png)

<span id="_Toc270513763" class="anchor"></span>Figure 6: Print Example: DBQ – Male Reproductive System Conditions – 1. Diagnosis

|                                                                             |
|-----------------------------------------------------------------------------|
| 1\. Diagnosis                                                               |
| ------------                                                                |
| Does the Veteran now have or has he ever been diagnosed with any conditions |
| of the male reproductive system? \[X\] Yes \[ \] No                         |
|                                                                             |
| If no, provide rationale (e.g., Veteran has never had any known male        |
| reproductive organ conditions):                                             |
|                                                                             |
| If yes, indicate diagnoses: (check all that apply)                          |
| \[ \] Erectile dysfunction                                                  |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Penis, deformity (e.g., Peyronie's)                                   |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Testis, atrophy, one or both                                          |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Testis, removal, one or both                                          |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Epididymitis, chronic                                                 |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Epididymo-orchitis, chronic                                           |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Prostate injury                                                       |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Prostate hypertrophy (BPH)                                            |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Prostatitis, chronic                                                  |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Prostate surgical residuals (as addressed in items 3-6)               |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Neoplasms of the male reproductive system                             |
| ICD Code: Date of Diagnosis:                                                |
| \[ \] Other male reproductive system condition (specify diagnosis,          |
| providing only diagnoses that pertain to male reproductive system.)         |
| ICD Code: Date of Diagnosis:                                                |
|                                                                             |
| Other diagnosis \#1:                                                        |
| ICD code:                                                                   |
| Date of diagnosis:                                                          |
|                                                                             |
| Other diagnosis \#2:                                                        |
| ICD code:                                                                   |
| Date of diagnosis:                                                          |
|                                                                             |
| If there are additional diagnoses that pertain to the male reproductive     |
| organ conditions, list using above format:                                  |

<span id="_Toc290013911" class="anchor"></span>Table 6: Rules: DBQ – Male Reproductive System Conditions – 5. Erectile Dysfunction

## Section 2. Medical history

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc290013912" class="anchor"></span>Table 7: Rules: DBQ – Male Reproductive System Conditions – 6. Retrograde ejaculation</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 29%" />
<col style="width: 17%" />
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
<td><strong><u>2.Medical history</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Describe the history (including onset and course) of the Veteran’s male reproductive organ condition(s) (brief summary):</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the history (including onset and course) of the Veteran’s current male reproductive organ condition(s).</td>
</tr>
<tr class="odd">
<td>b. Does the Veteran’s treatment plan include taking continuous medication for the diagnosed condition?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p>
<p>Choose one valid value.</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran’s treatment plan include taking continuous medication for the diagnosed condition?</td>
</tr>
<tr class="even">
<td>List Medications:</td>
<td><p>If <em>Diagnosis = Yes</em> and <em>Does the Veteran’s</em> <em>treatment plan include taking continuous medication for the diagnosed condition? = Yes;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and <em>Does the Veteran’s treatment plan include taking continuous medication for the diagnosed condition? = Yes;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please list continuous medications taken for the diagnosed condition.</td>
</tr>
<tr class="odd">
<td>c. Has the Veteran had an orchiectomy?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p>
<p>Choose one valid value</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Has the Veteran had an orchiectomy?</td>
</tr>
<tr class="even">
<td>Indicate testicle removed:</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section</em> and <em>Has the Veteran had an orchiectomy? = Yes;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and <em>Has the Veteran had an orchiectomy? = Yes;</em> Enabled, Optional</p>
<p>Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Right; Left; Both]</td>
<td>N/A</td>
<td>Please indicate which testicle was removed.</td>
</tr>
<tr class="odd">
<td>Indicate reason for removal:</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section</em> and <em>Has the Veteran had an orchiectomy? = Yes;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and <em>Has the Veteran had an orchiectomy? = Yes;</em> Enabled, Optional</p>
<p>Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Undescended; Congenitally underdeveloped; Other: provide reason for removal:]</td>
<td>N/A</td>
<td>Please indicate the reason for the orchiectomy.</td>
</tr>
<tr class="even">
<td>Other: provide reason for removal:</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section</em> and <em>Reason for removal = Other;</em> Enabled, Mandatory</p>
<p>If <em>Diagnosis = No</em> and <em>Has the Veteran had an orchiectomy? = Yes;</em> Enabled, Optional</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the other reason for the orchiectomy.</td>
</tr>
</tbody>
</table>

<span id="_Toc290013912" class="anchor"></span>Table 7: Rules: DBQ – Male Reproductive System Conditions – 6. Retrograde ejaculation

<span id="_Toc290013926" class="anchor"></span>Figure 7: Template Example: DBQ – Male Reproductive System Conditions – 2. Medical history

![](dvba-2-7-163-workflow-male-reproductive-system-conditions/007.png)

<span id="_Toc270513766" class="anchor"></span>Figure 8: Print Example: DBQ – Male Reproductive System Conditions– 2. Medical history

| 2\. Medical history                                                         |
|-----------------------------------------------------------------------------|
| ------------------                                                          |
| a\. Describe the history (including onset and course) of the Veteran's male |
| reproductive organ condition(s) (brief summary):                            |
|                                                                             |
| b\. Does the Veteran's treatment plan include taking continuous medication  |
| for the diagnosed condition?                                                |
| \[X\] Yes \[ \] No                                                          |
|                                                                             |
| List medications:                                                           |
|                                                                             |
| c\. Has the Veteran had an orchiectomy?                                     |
| \[X\] Yes \[ \] No                                                          |
|                                                                             |
| Indicate testicle removed:                                                  |
| \[ \] Right \[ \] Left \[ \] Both                                           |
|                                                                             |
| Indicate reason for removal:                                                |
| \[ \] Undescended                                                           |
| \[ \] Congenitally underdeveloped                                           |
| \[X\] Other: provide reason for removal:                                    |

<span id="_Toc290013913" class="anchor"></span>Table 8: Rules: DBQ – Male Reproductive System Conditions – 7. Male reproductive organ infections

## Section 3. Voiding dysfunction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc290013914" class="anchor"></span>Table 9: Rules: DBQ – Male Reproductive System Conditions – 8. Physical exam</p></caption>
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
<td><strong><u>3.Voiding dysfunction</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran have a voiding dysfunction?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled; Mandatory.</p>
<p>Else; Optional</p>
<p>Choose one valid value</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran have a voiding dysfunction?</td>
</tr>
<tr class="odd">
<td>If yes, provide etiology of voiding dysfunction:</td>
<td><p><em>Does the Veteran have a voiding dysfunction? = Yes;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the etiology of the voiding dysfunction.</td>
</tr>
<tr class="even">
<td>If the Veteran has a voiding dysfunction, complete the following questions:</td>
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes;</em> Enabled; Read-Only</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>a. Does the voiding dysfunction cause urine leakage?</td>
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes;</em> Enabled; Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the voiding dysfunction cause urine leakage?</td>
</tr>
<tr class="even">
<td>Indicate severity (check one):</td>
<td><p>If <em>Does the voiding dysfunction cause urine leakage? = Yes;</em></p>
<p>Enabled; Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Does not require/does not use absorbent material; Requires absorbent material that is changed less than 2 times per day; Requires absorbent material that is changed 2 to 4 times per day; Requires absorbent material that is changed more than 4 times per day; Other, describe:]</td>
<td>N/A</td>
<td>Please check the applicable statement pertaining to the voiding dysfunction causing urine leakage.</td>
</tr>
<tr class="odd">
<td>Other, describe:</td>
<td><p>If <em>Severity = Other,</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other voiding dysfunction which causes urine leakage.</td>
</tr>
<tr class="even">
<td>b. Does the voiding dysfunction require the use of an appliance?</td>
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes;</em> Enabled; Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the voiding dysfunction require the use of an appliance?</td>
</tr>
<tr class="odd">
<td>If yes, describe the appliance:</td>
<td><p>If <em>Does the voiding dysfunction require the use of an appliance? = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the appliance used for the voiding dysfunction.</td>
</tr>
<tr class="even">
<td>c. Does the voiding dysfunction cause increased urinary frequency?</td>
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes;</em> Enabled; Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the voiding dysfunction cause increased urinary frequency?</td>
</tr>
<tr class="odd">
<td>If yes, check all that apply:</td>
<td><p>If <em>Does the voiding dysfunction cause increased urinary frequency?= Yes;</em></p>
<p>Enabled; Mandatory; Choose one valid value for Daytime and one valid value for Nighttime.</p>
<p>Else; Disabled</p></td>
<td><p>[Daytime voiding interval between 2 and 3 hours; Daytime voiding interval between 1 and 2 hours; Daytime voiding interval less than 1 hour]</p>
<p>[Nighttime awakening to void 2 times; Nighttime awakening to void 3 to 4 times; Nighttime awakening to void 5 or more times]</p></td>
<td>N/A</td>
<td>Please check the applicable statement(s) pertaining to the voiding dysfunction causing signs and/or symptoms of urinary frequency.</td>
</tr>
<tr class="even">
<td>d. Does the voiding dysfunction cause signs or symptoms of obstructed voiding?</td>
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes;</em> Enabled; Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the voiding dysfunction cause signs or symptoms of obstructed voiding?</td>
</tr>
<tr class="odd">
<td>If yes, check all that apply:</td>
<td><p>If <em>Does the voiding dysfunction cause signs or symptoms of obstructed voiding? = Yes</em>; Enabled; Mandatory; Choose one or more valid values.</p>
<p>Else; Disabled</p></td>
<td>[Hesitancy; slow or weak stream; decreased force of stream; stricture disease requiring dilatation 1 to 2 times per year; stricture disease requiring periodic dilatation every 2 to 3 months; recurrent urinary tract infections secondary to obstruction; uroflowmetry peak flow rate less than 10 cc/sec; post void residuals greater than 150 cc; urinary retention requiring intermittent catheterization; urinary retention requiring continuous catheterization; Other, describe:]</td>
<td>N/A</td>
<td>Please check one or more boxes to indicate the signs and symptoms of obstructed voiding.</td>
</tr>
<tr class="even">
<td>If checked, is hesitancy marked?</td>
<td><p>If <em>Voiding dysfunction signs or symptoms include Hesitancy;</em> Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please indicate whether or not hesitancy is marked.</td>
</tr>
<tr class="odd">
<td>If checked, is stream markedly slow or weak?</td>
<td><p>If <em>Voiding dysfunction signs or symptoms include Slow or weak stream</em>; Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please indicate whether or not stream is markedly slow or weak.</td>
</tr>
<tr class="even">
<td>If checked, is force of stream markedly decreased?</td>
<td><p>If <em>Voiding dysfunction signs or symptoms include Decreased force of stream</em>; Enabled, Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please indicate whether or not force of stream is markedly decreased.</td>
</tr>
<tr class="odd">
<td>Other, describe:</td>
<td><p>If <em>Voiding dysfunction signs or symptoms include Other</em>; Enabled; Mandatory</p>
<p>Else Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other signs and symptoms of obstructed voiding.</td>
</tr>
</tbody>
</table>

<span id="_Toc290013914" class="anchor"></span>Table 9: Rules: DBQ – Male Reproductive System Conditions – 8. Physical exam

<span id="_Toc270513768" class="anchor"></span>Figure 9: Template Example: DBQ – Male Reproductive System Conditions – 3. Voiding dysfunction

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/008.png)

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/009.png)

<span id="_Toc270513769" class="anchor"></span>Figure 10: Print Example: DBQ – Male Reproductive System Conditions – 3. Voiding dysfunction

| 3\. Voiding dysfunction                                                     |
|-----------------------------------------------------------------------------|
| ----------------------                                                      |
| Does the Veteran have a voiding dysfunction?                                |
| \[X\] Yes \[ \] No                                                          |
|                                                                             |
| If yes, provide etiology of voiding dysfunction:                            |
|                                                                             |
| If the Veteran has a voiding dysfunction, complete the following questions: |
|                                                                             |
| a\. Does the voiding dysfunction cause urine leakage?                       |
| \[X\] Yes \[ \] No                                                          |
|                                                                             |
| Indicate severity (check one)                                               |
| \[X\] Does not require the wearing of absorbent material                    |
| \[ \] Requires absorbent material which must be changed less than 2         |
| times per day                                                               |
| \[ \] Requires absorbent material which must be changed 2 to 4              |
| times per day                                                               |
| \[ \] Requires absorbent material which must be changed more than 4         |
| times per day                                                               |
| \[ \] Other, describe:                                                      |
|                                                                             |
| b\. Does the voiding dysfunction require the use of an appliance?           |
| \[X\] Yes \[ \] No                                                          |
|                                                                             |
| If yes, describe the appliance:                                             |
|                                                                             |
| c\. Does the voiding dysfunction cause increased urinary frequency?         |
| \[ \] Yes \[X\] No                                                          |
|                                                                             |
| If yes, check all that apply:                                               |
| \[ \] Daytime voiding interval between 2 and 3 hours                        |
| \[ \] Daytime voiding interval between 1 and 2 hours                        |
| \[ \] Daytime voiding interval less than 1 hour                             |
| \[ \] Nighttime awakening to void 2 times                                   |
| \[ \] Nighttime awakening to void 3 to 4 times                              |
| \[ \] Nighttime awakening to void 5 or more times                           |
|                                                                             |
| d\. Does the voiding dysfunction cause signs or symptoms of obstructed      |
| voiding?                                                                    |
| \[X\] Yes \[ \] No                                                          |
|                                                                             |
| If yes, check all that apply:                                               |
| \[X\] Hesitancy                                                             |
| If checked, is hesitancy marked?                                            |
| \[ \] Yes \[ \] No                                                          |
| \[X\] Slow or weak stream                                                   |
| If checked, is stream markedly slow or weak?                                |
| \[ \] Yes \[ \] No                                                          |
| \[X\] Decreased force of stream                                             |
| If checked, is force of stream markedly decreased?                          |
| \[ \] Yes \[ \] No                                                          |
| \[ \] Stricture disease requiring dilatation 1 to 2 times per year          |
| \[ \] Stricture disease requiring periodic dilatation every 2 to 3          |
| months                                                                      |
| \[ \] Recurrent urinary tract infections secondary to obstruction           |
| \[ \] Uroflowmetry peak flow rate less than 10 cc/sec                       |
| \[ \] Post void residuals greater than 150 cc                               |
| \[ \] Urinary retention requiring intermittent catheterization              |
| \[ \] Urinary retention requiring continuous catheterization                |
| \[X\] Other, describe:                                                      |

<span id="_Toc290013915" class="anchor"></span>Table 10: Rules: DBQ – Male Reproductive System Conditions – 9. Tumors and Neoplasms

## Section 4. Urinary tract/kidney infection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc270513773" class="anchor"></span>Table 11: Rules: DBQ – Male Reproductive System Conditions – 10. Other pertinent physical findings, complications, conditions, signs and/or symptoms</p></caption>
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
<td><strong><u>4. Urinary tract/kidney infection</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled, Mandatory, Choose one valid value.</p>
<p>Else, Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections?</td>
</tr>
<tr class="odd">
<td>If Yes, provide etiology:</td>
<td><p>If <em>Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections?</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the etiology of the recurrent symptomatic urinary tract or kidney infections.</td>
</tr>
<tr class="even">
<td>If the Veteran has had recurrent symptomatic urinary tract or kidney infections, indicate all treatment modalities that apply:</td>
<td><p>If <em>Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections? = Yes;</em> Enabled, Mandatory, Choose one or more valid values.</p>
<p>Else; Disabled</p></td>
<td>[No treatment; OR Long-term drug therapy; Hospitalization; Drainage; Continuous intensive management; Intermittent intensive management; Other, describe:]</td>
<td>N/A</td>
<td>Please check one or more boxes to indicate applicable treatment modalities for recurrent symptomatic urinary tract or kidney infections.</td>
</tr>
<tr class="odd">
<td>If checked, list medications used and indicate dates for courses of treatment over the past 12 months:</td>
<td><p>If <em>treatment modalities include long-term drug therapy;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please list medications used for urinary tract or kidney infections and their treatment dates.</td>
</tr>
<tr class="even">
<td>If checked, indicate frequency of hospitalization:</td>
<td><p>If <em>treatment modalities include hospitalization;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[1 or 2 per year; &gt;2 per year]</td>
<td>N/A</td>
<td>Please indicate the frequency of hospitalization.</td>
</tr>
<tr class="odd">
<td>If checked, indicate dates when drainage performed over past 12 months:</td>
<td><p>If <em>treatment modalities include drainage;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please indicate the dates that drainage was performed over the past 12 months.</td>
</tr>
<tr class="even">
<td>If checked, indicate types of treatment and medications used over past 12 months:</td>
<td><p>If <em>treatment modalities include continuous intensive management;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the types of treatment and medications for continuous intensive management used over the past 12 months.</td>
</tr>
<tr class="odd">
<td>If checked, indicate types of treatment and medications used over past 12 months:</td>
<td><p>If <em>treatment modalities include intermittent intensive management;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the types of treatment and medications for intermittent intensive management used over the past 12 months.</td>
</tr>
<tr class="even">
<td>Other, describe:</td>
<td><p>If <em>treatment modalities include other;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe other treatment modalities used for urinary tract or kidney infections.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513773" class="anchor"></span>Table 11: Rules: DBQ – Male Reproductive System Conditions – 10. Other pertinent physical findings, complications, conditions, signs and/or symptoms

<span id="_Toc290013930" class="anchor"></span>Figure 11: Template Example: DBQ – Male Reproductive System Conditions – 4. Urinary tract/kidney infection

![](dvba-2-7-163-workflow-male-reproductive-system-conditions/010.png)![](dvba-2-7-163-workflow-male-reproductive-system-conditions/011.png)

<span id="_Toc290013931" class="anchor"></span>Figure 12: Print Example: DBQ – Male Reproductive System Conditions – 4. Urinary tract/kidney infection

| 4\. Urinary tract/kidney infection                                        |
|---------------------------------------------------------------------------|
| ---------------------------------                                         |
| Does the Veteran have a history of recurrent symptomatic urinary tract or |
| kidney infections?                                                        |
| \[ \] Yes \[X\] No                                                        |
|                                                                           |
| If yes, provide etiology:                                                 |
|                                                                           |
| If the Veteran has had recurrent symptomatic urinary tract or kidney      |
| infections, indicate all treatment modalities that apply:                 |
| \[ \] No treatment                                                        |
| \[ \] Long-term drug therapy                                              |
| If checked, list medications used and indicate dates for                  |
| courses of treatment over the past 12 months:                             |
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

<span id="_Toc270513776" class="anchor"></span>Table 12: Rules: DBQ – Male Reproductive System Conditions – 11. Diagnostic testing

## Section 5. Erectile dysfunction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc290013918" class="anchor"></span>Table 13: Rules: DBQ – Male Reproductive System Conditions – 12. Functional impact</p></caption>
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
<td><strong><u>5. Erectile dysfunction</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have erectile dysfunction?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled, Mandatory</p>
<p>Else, Enabled, Optional</p>
<p>Choose one valid value.</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have erectile dysfunction?</td>
</tr>
<tr class="odd">
<td>If yes, provide etiology:</td>
<td><p>If <em>Does the Veteran have erectile dysfunction? = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the etiology of erectile dysfunction.</td>
</tr>
<tr class="even">
<td>b. If the Veteran has erectile dysfunction, is it as likely as not (at least 50% probability) attributable to one of the diagnoses in Section 1, including residuals of treatment for this diagnosis?</td>
<td><p>If <em>Does the Veteran have erectile dysfunction? = Yes;</em> Enabled, Mandatory, Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not erectile dysfunction is attributable to one of the diagnoses in Section 1, including its residuals of treatment.</td>
</tr>
<tr class="odd">
<td>If yes, specify the diagnosis to which the erectile dysfunction is as likely as not attributable:</td>
<td><p>If <em>previous question = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please specify the diagnosis to which erectile dysfunction is as likely as not attributable.</td>
</tr>
<tr class="even">
<td>c. If the Veteran has erectile dysfunction, is he able to achieve an erection sufficient for penetration and ejaculation (without medication)?</td>
<td><p>If <em>Does the Veteran have erectile dysfunction? = Yes;</em> Enabled, Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not the Veteran is able to achieve an erection sufficient for penetration and ejaculation (without medication).</td>
</tr>
<tr class="odd">
<td>If no, is the Veteran able to achieve an erection sufficient for penetration and ejaculation (with medication)?</td>
<td><p>If <em>previous question = No;</em> Enabled, Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not the Veteran is able to achieve an erection sufficient for penetration and ejaculation (with medication).</td>
</tr>
</tbody>
</table>

<span id="_Toc290013918" class="anchor"></span>Table 13: Rules: DBQ – Male Reproductive System Conditions – 12. Functional impact

<span id="_Toc290013932" class="anchor"></span>Figure 13: Template Example: DBQ – Male Reproductive System Conditions –5. Erectile dysfunction

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/012.png)

<span id="_Toc290013933" class="anchor"></span>Figure 14: Print Example: DBQ – Male Reproductive System Conditions – 5. Erectile dysfunction

| 5\. Erectile dysfunction                                                    |
|-----------------------------------------------------------------------------|
| -----------------------                                                     |
| a\. Does the Veteran have erectile dysfunction?                             |
| \[ \] Yes \[ \] No                                                          |
|                                                                             |
| If yes, provide etiology:                                                   |
|                                                                             |
| b\. If the Veteran has erectile dysfunction, is it as likely as not (at     |
| least a 50% probability) attributable to one of the diagnoses in Section 1, |
| including residuals of treatment for this diagnosis?                        |
| \[ \] Yes \[ \] No                                                          |
|                                                                             |
| If yes, specify the diagnosis to which the erectile dysfunction is          |
| as likely as not attributable:                                              |
|                                                                             |
| c\. If the Veteran has erectile dysfunction, is he able to achieve an       |
| erection sufficient for penetration and ejaculation (without medication)?   |
| \[ \] Yes \[ \] No                                                          |
|                                                                             |
| If no, is the Veteran able to achieve an erection sufficient for            |
| penetration and ejaculation (with medication)?                              |
| \[ \] Yes \[ \] No                                                          |
|                                                                             |

<span id="_Toc290013919" class="anchor"></span>Table 14: Rules: DBQ – Male Reproductive System Conditions –13. Remarks, if any

## Section 6. Retrograde ejaculation

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
<td><strong><u>6. Retrograde ejaculation</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have retrograde ejaculation?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled, Mandatory</p>
<p>Else, Enabled, Optional</p>
<p>Choose one valid value</p></td>
<td>[Yes; No]</td>
<td>Free Text</td>
<td>Please provide an answer to the question: Doe the Veteran have retrograde ejaculation?</td>
</tr>
<tr class="odd">
<td>If yes, provide etiology of the retrograde ejaculation:</td>
<td><p>If <em>Does the Veteran have retrograde ejaculation? = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the etiology of retrograde ejaculation.</td>
</tr>
<tr class="even">
<td>b. If the Veteran has retrograde ejaculation, is it as likely as not (at least a 50% probability) attributable to one of the diagnoses in Section 1, including residuals of treatment for this diagnosis?</td>
<td><p>If <em>Does the Veteran have retrograde ejaculation? = Yes;</em> Enabled, Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not retrograde ejaculation is attributable to one of the diagnoses in Section 1, including its residuals of treatment.</td>
</tr>
<tr class="odd">
<td>If yes, specify the diagnosis to which the retrograde ejaculation is as likely as not attributable:</td>
<td><p>If <em>previous question = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please specify the diagnosis to which retrograde ejaculation is as likely as not attributable.</td>
</tr>
</tbody>
</table>

<span id="_Toc290013934" class="anchor"></span>Figure 15: Template Example: DBQ – Male Reproductive System Conditions –6. Retrograde ejaculation

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/013.png)

<span id="_Toc290013935" class="anchor"></span>Figure 16: Print Example: DBQ – Male Reproductive System Conditions – 6. Retrograde ejaculation

| 6\. Retrograde ejaculation                                                   |
|------------------------------------------------------------------------------|
| -------------------------                                                    |
| a\. Does the Veteran have retrograde ejaculation?                            |
| \[ \] Yes \[ \] No                                                           |
|                                                                              |
| If yes, provide etiology of the retrograde ejaculation:                      |
|                                                                              |
| b\. If the Veteran has retrograde ejaculation, is it as likely as not (at    |
| least a 50% probability ) attributable to one of the diagnoses in Section 1, |
| including residuals of treatment for this diagnosis?                         |
| \[ \] Yes \[ \] No                                                           |
|                                                                              |
| If yes, specify the diagnosis to which the retrograde ejaculation is         |
| as likely as not attributable:                                               |
|                                                                              |

## Section 7. Male reproductive organ infections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 28%" />
<col style="width: 16%" />
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
<td><strong><u>7. Male reproductive organ infections</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>b. Does the Veteran have a history of chronic epididymitis, epididymo-orchitis or prostatitis?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled, Mandatory</p>
<p>Else, Enabled, Optional</p>
<p>Choose one valid value</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have a history of chronic epididymitis, epididymo-orchitis or prostatitis?</td>
</tr>
<tr class="odd">
<td>If yes, indicate all treatment modalities that apply:</td>
<td><p>If <em>Does the Veteran have a history of chronic epididymitis, epididymo-orchitis or prostatitis? = Yes,</em> Enabled, Mandatory; Choose one or more valid values.</p>
<p>Else disabled</p></td>
<td>[No treatment; OR Long-term drug therapy; Hospitalization; Continuous intensive management; Intermittent intensive management; Other, describe:]</td>
<td>N/A</td>
<td>Please check one or more boxes to indicate applicable treatment modalities for chronic epididymitis.</td>
</tr>
<tr class="even">
<td>If checked, list medications used and indicate dates for courses of treatment over the past 12 months:</td>
<td><p>If <em>treatment modalities include Long-term drug therapy;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please list medications used for chronic epididymitis, epididymo-orchitis or prostatitis, and their treatment dates.</td>
</tr>
<tr class="odd">
<td>If checked, indicate frequency of hospitalization:</td>
<td><p>If <em>treatment modalities include hospitalization;</em> Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[1 or 2 per year; &gt; 2 per year]</td>
<td>N/A</td>
<td>Please indicate the frequency of hospitalization.</td>
</tr>
<tr class="even">
<td>If checked, indicate types of treatment and medications used over the past 12 months:</td>
<td><p>If <em>treatment modalities include continuous intensive management;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the types of treatment and medications for continuous intensive management used over the past 12 months.</td>
</tr>
<tr class="odd">
<td>If checked, indicate types of treatment and medications used over the past 12 months:</td>
<td><p>If <em>treatment modalities include intermittent intensive management;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the types of treatment and medications for intermittent intensive management used over the past 12 months.</td>
</tr>
<tr class="even">
<td>Other, describe:</td>
<td><p>If <em>treatment modalities include other;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other treatment modalities used for chronic epididymitis, epididymo-orchitis or prostatitis.</td>
</tr>
</tbody>
</table>

<span id="_Toc290013936" class="anchor"></span>Figure 17: Template Example: DBQ – Male Reproductive System Conditions –7. Male reproductive organ infections

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/014.png)![](dvba-2-7-163-workflow-male-reproductive-system-conditions/015.png)![](dvba-2-7-163-workflow-male-reproductive-system-conditions/016.png)

<span id="_Toc290013937" class="anchor"></span>Figure 18: Print Example: DBQ – Male Reproductive System Conditions – 7. Male reproductive organ infections

| 7\. Male reproductive organ infections                                      |
|-----------------------------------------------------------------------------|
| -------------------------------------                                       |
| Does the Veteran have a history of chronic epididymitis, epididymo-orchitis |
| or prostatitis?                                                             |
| \[ \] Yes \[ \] No                                                          |
|                                                                             |
| If yes, indicate all treatment modalities that apply:                       |
| \[ \] No treatment                                                          |
| \[ \] Long-term drug therapy                                                |
| If checked, list medications used and indicate dates for courses            |
| of treatment over the past 12 months:                                       |
| \[ \] Hospitalization                                                       |
| If checked, indicate frequency of hospitalization:                          |
| \[ \] 1 or 2 per year                                                       |
| \[ \] \> 2 per year                                                         |
| \[ \] Continuous intensive management                                       |
| If checked, indicate types of treatment and medications used over           |
| past 12 months:                                                             |
| \[ \] Intermittent intensive management                                     |
| If checked, indicate types of treatment and medications used over           |
| past 12 months:                                                             |
| \[ \] Other, describe:                                                      |
|                                                                             |

## Section 8. Physical exam

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
<td><strong><u>8. Physical exam</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Penis</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value</p></td>
<td>[Normal; Not examined per Veteran’s request; Not examined, penis exam not relevant to condition; Abnormal]</td>
<td>N/A</td>
<td>Please select a value from the penis exam group.</td>
</tr>
<tr class="odd">
<td>If abnormal, indicate severity:</td>
<td><p>If <em>Penis exam =Abnormal</em>, Enabled, Mandatory, Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Loss/removal of half or more of penis; Loss/removal of glans penis; Penis deformity (such as Peyronie’s disease)</td>
<td>N/A</td>
<td>Please indicate the severity of the penis abnormality.</td>
</tr>
<tr class="even">
<td>If checked, describe:</td>
<td><p>If <em>Penis exam = Penis deformity (such as Peyronie’s disease),</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe penis deformity.</td>
</tr>
<tr class="odd">
<td>b. Testes</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value.</p></td>
<td>[Normal; Not examined per Veteran’s request; Not examined, testicular exam not relevant to condition; Abnormal]</td>
<td>N/A</td>
<td>Please select a value from the testes exam group.</td>
</tr>
<tr class="even">
<td><p>If abnormal, check all that apply:</p>
<p>Right testicle:</p></td>
<td><p>If <em>Testicular exam = Abnormal AND no abnormality selected for either right or left testicle;</em> Enabled, Mandatory, Choose one or more valid values.</p>
<p>Else; Disabled</p></td>
<td>[Size 1/3 or less of normal; Size ½ to 1/3 of normal; Considerably harder than normal; Considerably softer than normal; Absent; Other abnormality]</td>
<td>N/A</td>
<td>Please indicate the testes abnormality.</td>
</tr>
<tr class="odd">
<td>Describe:</td>
<td><p>If <em>Right testicular exam includes Other abnormality;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other abnormality of the right testicle.</td>
</tr>
<tr class="even">
<td>Left:</td>
<td><p>If <em>Testicular exam = Abnormal AND no abnormality selected for either right or left testicle;</em> Enabled, Mandatory, Choose one or more valid values.</p>
<p>Else; Disabled</p></td>
<td>[Size 1/3 or less of normal; Size ½ to 1/3 of normal; Considerably harder than normal; Considerably softer than normal; Absent; Other abnormality]</td>
<td>N/A</td>
<td>Please indicate the testes abnormality.</td>
</tr>
<tr class="odd">
<td>Describe:</td>
<td><p>If <em>Left testicular exam includes Other abnormality;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other abnormality of the left testicle.</td>
</tr>
<tr class="even">
<td>c. Epididymis</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value.</p></td>
<td>[Normal; Not examined per Veteran’s request; Not examined, epididymis exam not relevant to condition; Abnormal]</td>
<td>N/A</td>
<td>Please select a value from the epididymis exam group.</td>
</tr>
<tr class="odd">
<td><p>If abnormal, check all that apply:</p>
<p>Right epididymis:</p></td>
<td><p>If <em>Epididymis exam = Abnormal AND no abnormality selected for either right or left epididymis;</em> Enabled, Mandatory; Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Tender to palpation; Other, describe]</td>
<td>N/A</td>
<td>Please indicate the epididymis abnormality.</td>
</tr>
<tr class="even">
<td>Other, describe:</td>
<td><p>If <em>Epididymis exam includes other;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other abnormality of the right epididymis.</td>
</tr>
<tr class="odd">
<td>Left epididymis:</td>
<td><p>If <em>Epididymis exam = Abnormal AND no abnormality selected for either right or left epididymis;</em> Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Tender to palpation; Other, describe]</td>
<td>N/A</td>
<td>Please indicate the epididymis abnormality.</td>
</tr>
<tr class="even">
<td>Other, describe:</td>
<td><p>If <em>Epididymis exam includes other;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other abnormality of the left epididymis.</td>
</tr>
<tr class="odd">
<td>d. Prostate</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value</p></td>
<td>[Normal; Not examined per Veteran’s request; Not examined, prostate exam not relevant to condition; Abnormal]</td>
<td>N/A</td>
<td>Please select a value from the prostate exam group.</td>
</tr>
<tr class="even">
<td>If abnormal, describe:</td>
<td><p>If <em>Prostate exam = abnormal;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the abnormality of the prostate.</td>
</tr>
</tbody>
</table>

<span id="_Toc290013938" class="anchor"></span>Figure 19: Template Example: DBQ – Male Reproductive System Conditions –8. Physical exam

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/017.png)![](dvba-2-7-163-workflow-male-reproductive-system-conditions/018.png)

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/019.png)

<span id="_Toc290013939" class="anchor"></span>Figure 20: Print Example: DBQ – Male Reproductive System Conditions – 8. Physical exam

| 8.Physical exam                                               |
|---------------------------------------------------------------|
| ---------------                                               |
| a\. Penis                                                     |
| \[ \] Normal                                                  |
| \[ \] Not examined per Veteran's request                      |
| \[ \] Not examined; penis exam not relevant to condition      |
| \[ \] Abnormal                                                |
|                                                               |
| If abnormal, indicate severity:                               |
| \[ \] Loss/removal of half or more of penis                   |
| \[ \] Loss/removal of glans penis                             |
| \[ \] Penis deformity (such as Peyronie's disease)            |
| If checked, describe:                                         |
|                                                               |
| b\. Testes                                                    |
| \[ \] Normal                                                  |
| \[ \] Not examined per Veteran's request                      |
| \[ \] Not examined; testicular exam not relevant to condition |
| \[ \] Abnormal                                                |
|                                                               |
| If abnormal, check all that apply:                            |
| Right testicle                                                |
| \[ \] Size 1/3 or less of normal                              |
| \[ \] Size 1/2 to 1/3 of normal                               |
| \[ \] Considerably harder than normal                         |
| \[ \] Considerably softer than normal                         |
| \[ \] Absent                                                  |
| \[ \] Other abnormality,                                      |
| Describe:                                                     |
|                                                               |
| Left testicle                                                 |
| \[ \] Size 1/3 or less of normal                              |
| \[ \] Size 1/2 to 1/3 of normal                               |
| \[ \] Considerably harder than normal                         |
| \[ \] Considerably softer than normal                         |
| \[ \] Absent                                                  |
| \[ \] Other abnormality,                                      |
| Describe:                                                     |
|                                                               |
| c\. Epididymis                                                |
| \[ \] Normal                                                  |
| \[ \] Not examined per Veteran's request                      |
| \[ \] Not examined; epididymis exam not relevant to condition |
| \[ \] Abnormal                                                |
|                                                               |
| If abnormal, check all that apply:                            |
| Right epididymis                                              |
| \[ \] Tender to palpation                                     |
| \[ \] Other, describe:                                        |
|                                                               |
| Left epididymis                                               |
| \[ \] Tender to palpation                                     |
| \[ \] Other, describe:                                        |
|                                                               |
| d\. Prostate                                                  |
| \[ \] Normal                                                  |
| \[ \] Not examined per Veteran's request                      |
| \[ \] Not examined; prostate exam not relevant to condition   |
| \[ \] Abnormal                                                |
|                                                               |
| If abnormal, describe:                                        |

## Section 9. Tumors and Neoplasms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 29%" />
<col style="width: 15%" />
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
<td><strong><u>9. Tumors and Neoplasms</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value.</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section?</td>
</tr>
<tr class="odd">
<td>If yes, complete the following:</td>
<td><p>If <em>Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section?? = Yes;</em> Enabled, Read-Only</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>b. Is the neoplasm</td>
<td><p>If <em>Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section? = Yes;</em> Enabled; Mandatory, Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Benign; Malignant]</td>
<td>N/A</td>
<td>Please indicate whether the neoplasm is benign or malignant.</td>
</tr>
<tr class="odd">
<td>c. Has the Veteran completed treatment or is the Veteran currently undergoing treatment for a benign or malignant neoplasm or metastases?</td>
<td><p>If <em>Does the Veteran have a benign or malignant neoplasm or metastases related to any of the diagnoses in the Diagnosis section? = Yes;</em> Enabled; Mandatory, Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No, watchful waiting]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Has the Veteran completed treatment or is the Veteran currently undergoing treatment for a benign or malignant neoplasm or metastases?</td>
</tr>
<tr class="even">
<td>If yes, indicate type of treatment the Veteran is currently undergoing or has completed (check all that apply):</td>
<td><p>If <em>Has the Veteran completed treatment or is the Veteran currently undergoing treatment for a benign or malignant neoplasm or metastases? = Yes;</em> Enabled, Mandatory, Choose one or more valid values.</p>
<p>Else; Disabled</p></td>
<td>[Treatment completed, currently in watchful waiting status; OR Surgery; Radiation therapy; Antineoplastic chemotherapy; Other therapeutic procedure; Other therapeutic treatment]</td>
<td>N/A</td>
<td>Please indicate all applicable treatment types for a benign or malignant neoplasm or metastases that the Veteran either is currently undergoing or has completed.</td>
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
<td>Please enter the date (actual or anticipated) of completion of the radiation therapy treatment,</td>
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
<td>Please enter the date (actual or anticipated) of completion of the antineoplastic chemotherapy treatment.</td>
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
<td>Please indicate whether or not the Veteran has any residual conditions or complications due to the neoplasm (including metastases) or its treatment, other than those already documented.</td>
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

<span id="_Toc290013940" class="anchor"></span>Figure 21: Template Example: DBQ – Male Reproductive System Conditions – 9. Tumors and Neoplasms

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/020.png)![](dvba-2-7-163-workflow-male-reproductive-system-conditions/021.png)

<span id="_Toc290013941" class="anchor"></span>Figure 22: Print Example: DBQ – Male Reproductive System Conditions – 9. Tumors and Neoplasms

| 9\. Tumors and neoplasms                                                      |
|-------------------------------------------------------------------------------|
| -----------------------                                                       |
| a\. Does the Veteran have a benign or malignant neoplasm or metastases        |
| related to any of the diagnoses in the Diagnosis section?                     |
| \[X\] Yes \[ \] No                                                            |
|                                                                               |
| If yes, complete the following:                                               |
|                                                                               |
| b\. Is the neoplasm                                                           |
| \[ \] Benign \[ \] Malignant                                                  |
|                                                                               |
| c\. Has the Veteran completed treatment or is the Veteran currently           |
| undergoing treatment for a benign or malignant neoplasm or metastases?        |
| \[X\] Yes \[ \] No; watchful waiting                                          |
|                                                                               |
| If yes, indicate type of treatment the Veteran is currently undergoing        |
| or has completed (check all that apply):                                      |
| \[ \] Treatment completed; currently in watchful waiting status               |
| \[X\] Surgery                                                                 |
| If checked, describe:                                                         |
| Date(s) of surgery:                                                           |
| \[X\] Radiation therapy                                                       |
| Date of most recent treatment:                                                |
| Date of completion of treatment or anticipated date of                        |
| completion:                                                                   |
| \[X\] Antineoplastic chemotherapy                                             |
| Date of most recent treatment:                                                |
| Date of completion of treatment or anticipated date of                        |
| completion:                                                                   |
| \[ \] Other therapeutic procedure                                             |
| If checked, describe procedure:                                               |
| Date of most recent procedure:                                                |
| \[ \] Other therapeutic treatment                                             |
| If checked, describe treatment:                                               |
| Date of completion of treatment or anticipated date of                        |
| completion:                                                                   |
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

## Section 10. Other pertinent physical findings, complications, conditions, signs and/or symptoms

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
<td><strong><u>10. Other pertinent physical findings, complications, conditions, signs and/or symptoms</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have any scars (surgical or otherwise) related to any conditions or to the treatment of any conditions listed in the Diagnosis section above?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value</p></td>
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
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have any other pertinent physical findings, complications, conditions, signs or symptoms?</td>
</tr>
<tr class="even">
<td>If yes, describe (brief summary):</td>
<td><p>If <em>Does the Veteran have any other pertinent physical findings, complications, conditions, signs and/or symptoms? = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe any other pertinent physical findings, complications, conditions, signs or symptoms.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513774" class="anchor"></span>Figure 23: Template Example: DBQ – Male Reproductive System Conditions – 10. Other pertinent physical findings, complications, conditions, signs and/or symptoms

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/022.png)

<span id="_Toc270513775" class="anchor"></span>Figure 24: Print Example: DBQ – Male Reproductive System Conditions – 10. Other pertinent physical findings, complications, conditions, signs and/or symptoms

| 10\. Other pertinent physical findings, complications, conditions, signs   |
|----------------------------------------------------------------------------|
| and/or symptoms                                                            |
| ----------------------------------------------------------------------     |
| a\. Does the Veteran have any scars (surgical or otherwise) related to any |
| conditions or to the treatment of any conditions listed in the Diagnosis   |
| section above?                                                             |
| \[ \] Yes \[ \] No                                                         |
|                                                                            |
| If yes, are any of the scars painful and/or unstable, or is the            |
| total area of all related scars greater than 39 square cm (6 square        |
| inches)?                                                                   |
| \[ \] Yes \[ \] No                                                         |
|                                                                            |
| If yes, also complete a Scars Questionnaire.                               |
|                                                                            |
| b\. Does the Veteran have any other pertinent physical findings,           |
| complications, conditions, signs or symptoms?                              |
| \[ \] Yes \[ \] No                                                         |
|                                                                            |
| If yes, describe:                                                          |

## Section 11. Diagnostic testing

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
<td><strong><u>11. Diagnostic testing</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>NOTE: If imaging studies, diagnostic procedures or laboratory testing has been performed and reflects the Veteran’s current condition, provide most recent results; no further studies or testing are required for this examination.</td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>a. Has the Veteran had a testicular biopsy to determine the presence of spermatozoa?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value.</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Has the Veteran had a testicular biopsy to determine the presence of spermatozoa?</td>
</tr>
<tr class="even">
<td>If yes, were spermatozoa present?</td>
<td><p>If <em>Has the Veteran had a testicular biopsy to determine the presence of spermatozoa = Yes;</em> Enabled, Mandatory, Choose one valid value.</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not spermatozoa were present in the testicular biopsy.</td>
</tr>
<tr class="odd">
<td>Date of biopsy:</td>
<td><p>If <em>Has the Veteran had a testicular biopsy to determine the presence of spermatozoa = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the testicular biopsy.</td>
</tr>
<tr class="even">
<td>b. Have any other imaging studies, diagnostic procedures or laboratory testing been performed and are the results available?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value.</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Have any other imaging studies, diagnostic procedures or laboratory testing been performed and are the results available?</td>
</tr>
<tr class="odd">
<td>If yes, provide type of test or procedure, date and results (brief summary):</td>
<td><p>If <em>Have any other imaging studies, diagnostic procedures or laboratory testing been performed and are the results available? = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the type of test or procedure, its date and the results.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513777" class="anchor"></span>Figure 25: Template Example: DBQ – Male Reproductive System Conditions – 11. Diagnostic testing

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/023.png)

<span id="_Toc270513778" class="anchor"></span>Figure 26: Print Example: DBQ – Male Reproductive System Conditions– 11. Diagnostic testing

| 11\. Diagnostic testing                                                   |
|---------------------------------------------------------------------------|
| ----------------------                                                    |
| NOTE: If imaging studies, diagnostic procedures or laboratory testing has |
| been performed and reflects the Veteran's current condition, provide most |
| recent results; no further studies or testing are required for this       |
| examination.                                                              |
|                                                                           |
| a\. Has the Veteran had a testicular biopsy to determine the presence of  |
| spermatozoa?                                                              |
| \[ \] Yes \[ \] No                                                        |
|                                                                           |
| If yes, were spermatozoa present?                                         |
| \[ \] Yes \[ \] No                                                        |
|                                                                           |
| Date of biopsy:                                                           |
|                                                                           |
| b\. Have any other imaging studies, diagnostic procedures or laboratory   |
| testing been performed and are the results available?                     |
| \[ \] Yes \[ \] No                                                        |
|                                                                           |
| If yes, provide type of test or procedure, date and results (brief        |
| summary):                                                                 |

## Section 12. Functional impact

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
<td><strong><u>12. Functional impact</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran’s male reproductive system condition(s), including neoplasms, if any, impact his ability to work?</td>
<td><p>If <em>Diagnosis</em> <em>= Yes</em> and <em>at least one diagnosis selected in the Diagnosis section;</em> Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled<em>,</em> Optional</p>
<p>Choose one valid value</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran’s male reproductive system condition(s), including neoplasms, if any, impact his ability to work?</td>
</tr>
<tr class="odd">
<td>If yes, describe the impact of each of the Veteran’s male reproductive system condition(s), providing one or more examples:</td>
<td><p>If <em>Does the Veteran’s male reproductive system condition(s), including neoplasms, if any, impact his ability to work? = Yes;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the impact of each of the Veteran’s male reproductive system conditions on his ability to work, providing one or more examples.</td>
</tr>
</tbody>
</table>

<span id="_Toc290013946" class="anchor"></span>Figure 27: Template Example: DBQ – Male Reproductive System Conditions – 12. Functional impact

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/024.png)

<span id="_Toc290013947" class="anchor"></span>Figure 28: Print Example: DBQ – Male Reproductive System Conditions – 12. Functional impact

| 12\. Functional impact                                              |
|---------------------------------------------------------------------|
| ---------------------                                               |
| Does the Veteran's male reproductive system condition(s), including |
| neoplasms, if any, impact his ability to work?                      |
| \[ \] Yes \[ \] No                                                  |
|                                                                     |
| If yes, describe the impact of each of the Veteran's male           |
| reproductive system condition(s), providing one or more examples:   |

## ## ## Section 13. Remarks, if any

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below.

| Field/Question              | Field Disposition | Valid Values | Format | Error Message |
|---------------------------------|-----------------------|------------------|------------|-------------------|
| <u>13. Remarks, if any:</u> | Enabled*,* Optional   | N/A              | Free Text  | N/A               |

<span id="_Toc290013948" class="anchor"></span>Figure 29: Template Example: DBQ – Male Reproductive System Conditions – 13. Remarks, if any

> ![](dvba-2-7-163-workflow-male-reproductive-system-conditions/025.png)

<span id="_Toc290013949" class="anchor"></span>Figure 30: Print Example: DBQ – Male Reproductive System Conditions – 13. Remarks, if any

| 13\. Remarks, if any: |
|-----------------------|
| --------------------  |
|                       |

# Male Reproductive System Conditions DBQ-AMIE Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The DBQ-AMIE worksheets are accessed via the Print Blank C&P Worksheet menu \[DVBA C PRINT BLANK C&P WORKSHE\] option.  Select the “DBQ MALE REPRODUCTIVE SYSTEM CONDITIONS” worksheet.   DBQ-AMIE worksheets should be sent to a printer.

Male Reproductive System Conditions

Disability Benefits Questionnaire

Name of patient/Veteran: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ SSN: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Your patient is applying to the U. S. Department of Veterans Affairs (VA) for

disability benefits. VA will consider the information you provide on this

questionnaire as part of their evaluation in processing the Veteran's claim.

1\. Diagnosis:

Does the Veteran now have or has he ever been diagnosed with any conditions

of the male reproductive system?

\_\_\_ Yes \_\_\_ No

If no, provide rationale (e.g., Veteran has never had any known male

reproductive organ conditions): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If yes, indicate diagnoses: (check all that apply)

\_\_\_ Erectile dysfunction ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Penis, deformity (e.g., Peyronie's)

ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Testis, atrophy, one or both

ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Testis, removal, one or both

ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Epididymitis, chronic ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Epididymo-orchitis, chronic

ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Prostate injury ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Prostate hypertrophy (BPH)

ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Prostatitis, chronic ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Prostate surgical residuals (as addressed in items 3-6)

ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Neoplasms of the male reproductive system

ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other male reproductive system condition (specify diagnosis, providing

only diagnoses that pertain to male reproductive system.)

ICD Code: \_\_\_\_\_\_ Date of Diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_

Other diagnosis \#1: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 2

Disability Benefits Questionnaire for

Male Reproductive System Conditions

Other diagnosis \#2: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If there are additional diagnoses that pertain to the male reproductive organ

conditions, list using above format: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2\. Medical history

a\. Describe the history (including onset and course) of the Veteran's male

reproductive organ condition(s) (brief summary): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. Does the Veteran's treatment plan include taking continuous medication

for the diagnosed condition?

\_\_\_ Yes \_\_\_ No List medications: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

c\. Has the Veteran had an orchiectomy?

\_\_\_ Yes \_\_\_ No

Indicate testicle removed: \_\_\_ Right \_\_\_ Left \_\_\_ Both

Indicate reason for removal:

\_\_\_ Undescended

\_\_\_ Congenitally underdeveloped

\_\_\_ Other: provide reason for removal: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

3\. Voiding dysfunction

Does the Veteran have a voiding dysfunction?

\_\_\_ Yes \_\_\_ No

If yes, provide etiology of voiding dysfunction: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If the Veteran has a voiding dysfunction, complete the following questions:

a\. Does the voiding dysfunction cause urine leakage?

\_\_\_ Yes \_\_\_ No

Indicate severity (check one):

\_\_\_ Does not require the wearing of absorbent material

\_\_\_ Requires absorbent material which must be changed less than 2 times

per day

\_\_\_ Requires absorbent material which must be changed 2 to 4 times per day

\_\_\_ Requires absorbent material which must be changed more than 4 times

per day

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 3

Disability Benefits Questionnaire for

Male Reproductive System Conditions

b\. Does the voiding dysfunction require the use of an appliance?

\_\_\_ Yes \_\_\_ No

If yes, describe the appliance: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

c\. Does the voiding dysfunction cause increased urinary frequency?

\_\_\_ Yes \_\_\_ No

If yes, check all that apply:

\_\_\_ Daytime voiding interval between 2 and 3 hours

\_\_\_ Daytime voiding interval between 1 and 2 hours

\_\_\_ Daytime voiding interval less than 1 hour

\_\_\_ Nighttime awakening to void 2 times

\_\_\_ Nighttime awakening to void 3 to 4 times

\_\_\_ Nighttime awakening to void 5 or more times

d\. Does the voiding dysfunction cause signs or symptoms of obstructed

voiding?

\_\_\_ Yes \_\_\_ No

If yes, check all that apply:

\_\_\_ Hesitancy

If checked, is hesitancy marked?

\_\_\_ Yes \_\_\_ No

\_\_\_ Slow or weak stream

If checked, is stream markedly slow or weak?

\_\_\_ Yes \_\_\_ No

\_\_\_ Decreased force of stream

If checked, is force of stream markedly decreased?

\_\_\_ Yes \_\_\_ No

\_\_\_ Stricture disease requiring dilatation 1 to 2 times per year

\_\_\_ Stricture disease requiring periodic dilatation every 2 to 3 months

\_\_\_ Recurrent urinary tract infections secondary to obstruction

\_\_\_ Uroflowmetry peak flow rate less than 10 cc/sec

\_\_\_ Post void residuals greater than 150 cc

\_\_\_ Urinary retention requiring intermittent catheterization

\_\_\_ Urinary retention requiring continuous catheterization

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 4

Disability Benefits Questionnaire for

Male Reproductive System Conditions

4\. Urinary tract/kidney infection

Does the Veteran have a history of recurrent symptomatic urinary tract

or kidney infections?

\_\_\_ Yes \_\_\_ No

If yes, provide etiology: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If the Veteran has had recurrent symptomatic urinary tract or kidney

infections, indicate all treatment modalities that apply:

\_\_\_ No treatment

\_\_\_ Long-term drug therapy

If checked, list medications used and indicate dates for courses of

treatment over the past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Hospitalization

If checked, indicate frequency of hospitalization:

\_\_\_ 1 or 2 per year

\_\_\_ \> 2 per year

\_\_\_ Drainage

If checked, indicate dates when drainage performed over past 12

months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Continuous intensive management

If checked, indicate types of treatment and medications used over past

12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Intermittent intensive management

If checked, indicate types of treatment and medications used over past

12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5\. Erectile dysfunction

a\. Does the Veteran have erectile dysfunction?

\_\_\_ Yes \_\_\_ No

If yes, provide etiology:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. If the Veteran has erectile dysfunction, is it as likely as not (at least

a 50% probability) attributable to one of the diagnoses in Section 1,

including residuals of treatment for this diagnosis?

\_\_\_ Yes \_\_\_ No

If yes, specify the diagnosis to which the erectile dysfunction is as likely

as not attributable: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 5

Disability Benefits Questionnaire for

Male Reproductive System Conditions

c\. If the Veteran has erectile dysfunction, is he able to achieve an erection

sufficient for penetration and ejaculation (without medication)?

\_\_\_ Yes \_\_\_ No

If no, is the Veteran able to achieve an erection sufficient for penetration

and ejaculation (with medication)?

\_\_\_ Yes \_\_\_ No

6\. Retrograde ejaculation

a\. Does the Veteran have retrograde ejaculation?

\_\_\_ Yes \_\_\_ No

If yes, provide etiology of the retrograde ejaculation:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. If the Veteran has retrograde ejaculation, is it as likely as not (at

least a 50% probability) attributable to one of the diagnoses in Section 1,

including residuals of treatment for this diagnosis?

\_\_\_ Yes \_\_\_ No

If yes, specify the diagnosis to which the retrograde ejaculation is as

likely as not attributable: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

7\. Male reproductive organ infections

Does the Veteran have a history of chronic epididymitis, epididymo-orchitis

or prostatitis?

\_\_\_ Yes \_\_\_ No

If yes, indicate all treatment modalities that apply:

\_\_\_ No treatment

\_\_\_ Long-term drug therapy

If checked, list medications used and indicate dates for courses of

treatment over the past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Hospitalization

If checked, indicate frequency of hospitalization:

\_\_\_ 1 or 2 per year

\_\_\_ \> 2 per year

\_\_\_ Continuous intensive management

If checked, indicate types of treatment and medications used over

past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Intermittent intensive management

If checked, indicate types of treatment and medications used over

past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 6

Disability Benefits Questionnaire for

Male Reproductive System Conditions

8\. Physical exam

a\. Penis

\_\_\_ Normal

\_\_\_ Not examined per Veteran's request

\_\_\_ Not examined; penis exam not relevant to condition

\_\_\_ Abnormal

If abnormal, indicate severity:

\_\_\_ Loss/removal of half or more of penis

\_\_\_ Loss/removal of glans penis

\_\_\_ Penis deformity(such as Peyronie's disease)

If checked, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. Testes

\_\_\_ Normal

\_\_\_ Not examined per Veteran's request

\_\_\_ Not examined; testicular exam not relevant to condition

\_\_\_ Abnormal

If abnormal, check all that apply:

Right testicle

\_\_\_ Size 1/3 or less of normal

\_\_\_ Size 1/2 to 1/3 of normal

\_\_\_ Considerably harder than normal

\_\_\_ Considerably softer than normal

\_\_\_ Absent

\_\_\_ Other abnormality,

Describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Left testicle

\_\_\_ Size 1/3 or less of normal

\_\_\_ Size 1/2 to 1/3 of normal

\_\_\_ Considerably harder than normal

\_\_\_ Considerably softer than normal

\_\_\_ Absent

\_\_\_ Other abnormality,

Describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 7

Disability Benefits Questionnaire for

Male Reproductive System Conditions

c\. Epididymis

\_\_\_ Normal

\_\_\_ Not examined per Veteran's request

\_\_\_ Not examined; epididymis exam not relevant to condition

\_\_\_ Abnormal

If abnormal, check all that apply:

Right epididymis

\_\_\_ Tender to palpation

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Left epididymis

\_\_\_ Tender to palpation

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

d\. Prostate

\_\_\_ Normal

\_\_\_ Not examined per Veteran's request

\_\_\_ Not examined; prostate exam not relevant to condition

\_\_\_ Abnormal

If abnormal, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9\. Tumors and neoplasms

a\. Does the Veteran have a benign or malignant neoplasm or metastases

related to any of the diagnoses in the Diagnosis section?

\_\_\_ Yes \_\_\_ No

If yes, complete the following:

b\. Is the neoplasm

\_\_\_ Benign \_\_\_ Malignant

Page: 8

Disability Benefits Questionnaire for

Male Reproductive System Conditions

c\. Has the Veteran completed treatment or is the Veteran currently undergoing

treatment for a benign or malignant neoplasm or metastases?

\_\_\_ Yes \_\_\_ No; watchful waiting

If yes, indicate type of treatment the Veteran is currently undergoing or

has completed (check all that apply):

\_\_\_ Treatment completed; currently in watchful waiting status

\_\_\_ Surgery

If checked, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date(s) of surgery: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Radiation therapy

Date of most recent treatment: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of completion of treatment or anticipated date of completion:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Antineoplastic chemotherapy

Date of most recent treatment: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of completion of treatment or anticipated date of completion:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other therapeutic procedure

If checked, describe procedure: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of most recent procedure: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other therapeutic treatment

If checked, describe treatment: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of completion of treatment or anticipated date of completion:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

d\. Does the Veteran currently have any residual conditions or complications

due to the neoplasm (including metastases) or its treatment, other than those

already documented in the report above?

\_\_\_ Yes \_\_\_ No

If yes, list residual conditions and complications (brief summary):

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

e\. If there are additional benign or malignant neoplasms or metastases

related to any of the diagnoses in the Diagnosis section, describe using the

above format: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 9

Disability Benefits Questionnaire for

Male Reproductive System Conditions

10\. Other pertinent physical findings, complications, conditions, signs

and/or symptoms

a\. Does the Veteran have any scars (surgical or otherwise) related to any

conditions or to the treatment of any conditions listed in the Diagnosis

section above?

\_\_\_ Yes \_\_\_ No

If yes, are any of the scars painful and/or unstable, or is the total area

of all related scars greater than 39 square cm (6 square inches)?

\_\_\_ Yes \_\_\_ No

If yes, also complete a Scars Questionnaire.

b\. Does the Veteran have any other pertinent physical findings,

complications, conditions, signs or symptoms?

\_\_\_ Yes \_\_\_ No

If yes, describe (brief summary): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

11\. Diagnostic testing

> **NOTE:** If imaging studies, diagnostic procedures or laboratory testing has

been performed and reflects the Veteran's current condition, provide most

recent results; no further studies or testing are required for this

examination.

a\. Has the Veteran had a testicular biopsy to determine the presence of

spermatozoa?

\_\_\_ Yes \_\_\_ No

If yes, were spermatozoa present?

\_\_\_ Yes \_\_\_ No

Date of biopsy: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. Have any other imaging studies, diagnostic procedures or laboratory

testing been performed and are the results available?

\_\_\_ Yes \_\_\_ No

If yes, provide type of test or procedure, date and results (brief summary):

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

12\. Functional impact

Does the Veteran's male reproductive system condition(s), including neoplasms,

if any, impact his ability to work?

\_\_\_ Yes \_\_\_ No

If yes, describe the impact of each of the Veteran's male reproductive system

condition(s), providing one or more examples: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 10

Disability Benefits Questionnaire for

Male Reproductive System Conditions

13\. Remarks, if any: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_

Physician printed name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Phone: \_\_\_\_\_\_\_\_\_\_\_

Medical license \#: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Fax: \_\_\_\_\_\_\_\_\_\_\_\_\_

Physician address: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> **NOTE:** VA may request additional medical information, including additional

examinations if necessary to complete VA's review of the Veteran's

application.