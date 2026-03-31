---
title: DVBA*2.7*163 Workflow - Prostate Cancer
doc_type: WF
doc_label: Workflow Guide
doc_layer: patch
doc_subject: Workflow - Prostate Cancer
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
  - class
  - strong
  - prostate
  - cancer
  - veteran
  - enabled
  - span
  - does
  - table
  - treatment
page_count: 0
word_count: 9004
section_count: 16
table_count: 68
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_p163_dbq_prostatecancer_wf.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_p163_dbq_prostatecancer_wf.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=133"
---

![](dvba-2-7-163-workflow-prostate-cancer/001.png)

Compensation and Pension Record Interchange (CAPRI)

Prostate Cancer

Disability Benefits Questionnaire (DBQ)

Workflow

April 2011

Office of Enterprise Development

Management & Financial Systems

Revision History

<table>
<caption><p><span id="_Toc270513758" class="anchor"></span>Table 1: Rules: DBQ – Prostate Cancer – Name of patient/Veteran</p></caption>
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
<td>11/02/2010</td>
<td>Document created</td>
<td>REDACTED</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>4/1/2011</td>
<td>Revisions for patch DVBA*2.7*163</td>
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

<span id="_Toc270513758" class="anchor"></span>Table 1: Rules: DBQ – Prostate Cancer – Name of patient/Veteran

Table of Contents

Table of Figures and Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Overview](#overview)
- [Prostate Cancer DBQ](#prostate-cancer-dbq)
  - [Name of patient/Veteran](#name-of-patientveteran)
  - [Section 1. Diagnosis](#section-1-diagnosis)
  - [Section 2. Medical history](#section-2-medical-history)
  - [Section 3. Treatment](#section-3-treatment)
  - [Section 4. Voiding dysfunction](#section-4-voiding-dysfunction)
  - [Section 5. Urinary tract/kidney infection](#section-5-urinary-tractkidney-infection)
  - [Section 6. Erectile dysfunction](#section-6-erectile-dysfunction)
  - [Section 7. Retrograde ejaculation](#section-7-retrograde-ejaculation)
  - [Section 8. Residual conditions and/or complications](#section-8-residual-conditions-andor-complications)
  - [Section 9. Other pertinent physical findings, complications, conditions, signs and/or symptoms](#section-9-other-pertinent-physical-findings-complications-conditions-signs-andor-symptoms)
  - [Section 10. Diagnostic testing](#section-10-diagnostic-testing)
  - [Section 11. Functional impact](#section-11-functional-impact)
  - [Section 12. Remarks, if any](#section-12-remarks-if-any)
- [Prostate Cancer DBQ-AMIE Worksheet](#prostate-cancer-dbq-amie-worksheet)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides a high level overview of the contents found on the PROSTATE CANCER Disability Benefits Questionnaire (DBQ). The DBQ can be populated via an online template within the CAPRI C&P Worksheets tab and then printed OR it can be printed via AMIE (AUTOMATED MEDICAL INFORMATION EXCHANGE) and then manually populated. This document contains the edit rules for the template as well as an example of how the template will look online in CAPRI or printed from CAPRI. It also contains the layout for the AMIE worksheet to depict how it will look when printed from AMIE.

For more detailed information on standard template functionality not covered in this document, please refer to the *C&P Worksheet Tab Functionalities* section of the [CAPRI GUI User Guide](http://www4.va.gov/vdl/documents/Financial_Admin/CAPRI/capri_um.pdf).

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PROSTATE CANCER DBQ provides the ability to capture information related to Prostate Cancer and its treatment.

Each DBQ template contains a standard footer containing a note stating that “VA may request additional medical information, including additional examinations if necessary to complete VA’s review of the Veteran’s application.” (see Figure 1 and 2).

<span id="_Toc270513756" class="anchor"></span>Figure 1: Template Example: DBQ - Standard VA Note

![](dvba-2-7-163-workflow-prostate-cancer/002.png)

<span id="_Toc270513757" class="anchor"></span>Figure 2: Print Example: DBQ – Standard VA Note

|                                                                                     |
|-------------------------------------------------------------------------------------|
| NOTE: VA may request additional medical information, including additional       |
| examinations if necessary to complete VA's review of the Veteran's application. |
|                                                                                     |

<span id="_Toc290014249" class="anchor"></span>Table 2: Rules: DBQ – Prostate Cancer – 1. Diagnosis

A number of fields on the PROSTATE CANCER template are mandatory and require a response (value) prior to the exam being marked as completed. Some questions may activate a Pop-up window displaying information as to each question that needs to be answered before the template can be completed.

# Prostate Cancer DBQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Name of patient/Veteran

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

| Field/Question                                                                                                                                                                                                                         | Field Disposition | Valid Values | Format | Error Message                             |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------|------------|-----------------------------------------------|
| Prostate Cancer                                                                                                                                                                                                                        | Enabled, Read-Only    | N/A              | N/A        | N/A                                           |
| Disability Benefits Questionnaire                                                                                                                                                                                                      | Enabled, Read-Only    | N/A              | N/A        | N/A                                           |
| Name of patient/Veteran:                                                                                                                                                                                                                   | Enabled, Mandatory    | N/A              | Free Text  | Please enter the name of the patient/Veteran. |
| Your patient is applying to the U. S. Department of Veterans Affairs (VA) for disability benefits.  VA will consider the information you provide on this questionnaire as part of their evaluation in processing the Veteran’s claim.  | Enabled, Read-Only    | N/A              | N/A        | N/A                                           |

<span id="_Toc270513764" class="anchor"></span>Table 3: Rules: DBQ – Prostate Cancer – 2. Medical history

<span id="_Toc270513759" class="anchor"></span>Figure 3: Template Example: DBQ – Prostate Cancer – Name of patient/Veteran

> ![](dvba-2-7-163-workflow-prostate-cancer/003.png)

<span id="_Toc270513760" class="anchor"></span>Figure 4: Print Example: DBQ – Prostate Cancer – Name of patient/Veteran

| Prostate Cancer                                                               |
|-------------------------------------------------------------------------------|
| Disability Benefits Questionnaire                                             |
|                                                                               |
| Name of patient/Veteran:                                                      |
|                                                                               |
| Your patient is applying to the U.S. Department of Veterans Affairs (VA)      |
| for disability benefits. VA will consider the information you provide on this |
| questionnaire as part of their evaluation in processing the Veteran's claim.  |

<span id="_Toc270513767" class="anchor"></span>Table 4: Rules: DBQ – Prostate Cancer – 3. Treatment

## Section 1. Diagnosis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The question “Does the Veteran now have or has he ever been diagnosed with prostate cancer?” must be answered before the template can be completed.

- If it is answered with Yes, all other questions requiring an answer as described by the rules in this document must be answered before the template can be completed.
- If it is answered with No, the rationale supporting this is required. The remainder of the template may be completed without answering any additional questions or the user may input answers to any of the optional questions as indicated by the rules described in this document.

All questions will be printed even if they have not been answered.

If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below and must be answered before this template can be completed.

<table>
<caption><p><span id="_Toc290014252" class="anchor"></span>Table 5: Rules: DBQ – Prostate Cancer – 4. Voiding dysfunction</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 22%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 30%" />
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
<td>Does the Veteran now have or has he ever been diagnosed with prostate cancer?</td>
<td>Enabled, Mandatory; Choose one valid value</td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran now have or has he ever been diagnosed with prostate cancer?</td>
</tr>
<tr class="odd">
<td>If no, provide rationale (e.g. Veteran has never had prostate cancer):</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? =</em> <em>No</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the rationale for indicating the Veteran has not been diagnosed with prostate cancer.</td>
</tr>
<tr class="even">
<td>If yes, provide only diagnoses that pertain to prostate cancer.</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled, Read-Only</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Diagnosis #1:</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer?</em> = <em>Yes</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter a value in the 'Diagnosis #1' field.</td>
</tr>
<tr class="even">
<td>ICD code:</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer?</em> = <em>Yes</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for diagnosis #1.</td>
</tr>
<tr class="odd">
<td>Date of diagnosis:</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer?</em> = <em>Yes</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis #1.</td>
</tr>
<tr class="even">
<td>Diagnosis #2:</td>
<td>Enabled, Optional</td>
<td>N/A</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>ICD code:</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes</em> and <em>Diagnosis #2 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for diagnosis #2.</td>
</tr>
<tr class="even">
<td>Date of diagnosis:</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes</em> and <em>Diagnosis #2 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis #2.</td>
</tr>
<tr class="odd">
<td>Diagnosis #3:</td>
<td>Enabled, Optional</td>
<td>N/A</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>ICD code:</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes</em> and <em>Diagnosis #3 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for diagnosis #3.</td>
</tr>
<tr class="odd">
<td>Date of diagnosis:</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes</em> and <em>Diagnosis #3 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis #3.</td>
</tr>
<tr class="even">
<td>If there are additional diagnoses that pertain to prostate cancer, list using above format:</td>
<td>Enabled, Optional</td>
<td>N/A</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<span id="_Toc290014252" class="anchor"></span>Table 5: Rules: DBQ – Prostate Cancer – 4. Voiding dysfunction

<span id="_Toc270513762" class="anchor"></span>Figure 5: Template Example: DBQ – Prostate Cancer – 1. Diagnosis

![](dvba-2-7-163-workflow-prostate-cancer/004.png)![](dvba-2-7-163-workflow-prostate-cancer/005.png)

<span id="_Toc270513763" class="anchor"></span>Figure 6: Print Example: DBQ – Prostate Cancer – 1. Diagnosis

| 1\. Diagnosis                                                           |
|-------------------------------------------------------------------------|
| ------------                                                            |
| Does the Veteran now have or has he ever been diagnosed with prostate   |
| cancer? \[X\] Yes \[ \] No                                              |
|                                                                         |
| If no, provide rationale (e.g. Veteran has never had prostate cancer):  |
|                                                                         |
| If yes, provide only diagnoses that pertain to prostate cancer.         |
| Diagnosis \#1:                                                          |
| ICD code:                                                               |
| Date of diagnosis:                                                      |
|                                                                         |
| Diagnosis \#2:                                                          |
| ICD code:                                                               |
| Date of diagnosis:                                                      |
|                                                                         |
| Diagnosis \#3:                                                          |
| ICD code:                                                               |
| Date of diagnosis:                                                      |
|                                                                         |
| If there are additional diagnoses that pertain to prostate cancer, list |
| using above format:                                                     |

<span id="_Toc290014253" class="anchor"></span>Table 6: Rules: DBQ – Prostate Cancer – 5. Urinary tract/kidney infection

## Section 2. Medical history

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc290014254" class="anchor"></span>Table 7: Rules: DBQ – Prostate Cancer – 6. Erectile dysfunction</p></caption>
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
<td><strong><u>2.Medical history</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Describe the history (including onset and course) of the Veteran’s prostate cancer condition (brief summary):</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled, Mandatory</p>
<p>Else; Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the history, including onset and course, of the Veteran's prostate cancer condition.</td>
</tr>
<tr class="odd">
<td>b. Indicate status of disease:</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td><p>[Active;</p>
<p>Remission]</p></td>
<td>N/A</td>
<td>Please indicate the status of the disease.</td>
</tr>
</tbody>
</table>

<span id="_Toc290014254" class="anchor"></span>Table 7: Rules: DBQ – Prostate Cancer – 6. Erectile dysfunction

<span id="_Toc290014226" class="anchor"></span>Figure 7: Template Example: DBQ – Prostate Cancer – 2. Medical history

![](dvba-2-7-163-workflow-prostate-cancer/006.png)

<span id="_Toc270513766" class="anchor"></span>Figure 8: Print Example: DBQ – Prostate Cancer – 2. Medical history

| 2\. Medical history                                                    |
|------------------------------------------------------------------------|
| ------------------                                                     |
| a\. Describe the history (including onset and course) of the Veteran's |
| prostate cancer condition (brief summary):                             |
|                                                                        |
| b\. Indicate status of disease:                                        |
| \[ \] Active                                                           |
| \[ \] Remission                                                        |

<span id="_Toc290014255" class="anchor"></span>Table 8: Rules: DBQ – Prostate Cancer – 7. Retrograde ejaculation

## Section 3. Treatment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc270513770" class="anchor"></span>Table 9: Rules: DBQ – Prostate Cancer – 8. Residual conditions and/or complications</p></caption>
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
<td><strong><u>3.Treatment</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Has the Veteran completed any treatment for prostate cancer or is the Veteran currently undergoing any treatment for prostate cancer?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No, watchful waiting]</td>
<td>N/A</td>
<td>Please answer the question: Has the Veteran completed any treatment for prostate cancer or is the Veteran currently undergoing any treatment for prostate cancer?</td>
</tr>
<tr class="odd">
<td>If yes, indicate treatment type(s) (check all that apply):</td>
<td><p>If <em>the previous question</em> <em>= Yes</em>; Enabled, Mandatory, Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td><p>Treatment completed, currently in watchful waiting status;</p>
<p>Surgery:</p>
<p>Radical prostatectomy, Transurethral resection prostatectomy, Other (describe):</p>
<p>Other surgical procedure (describe),</p>
<p>Date of surgery: ;</p>
<p>Radiation therapy :</p>
<p>Date of completion of treatment or anticipated date of completion: ­­­­­­­­­­­­;</p>
<p>Brachytherapy :</p>
<p>Date of treatment: ;</p>
<p>Antineoplastic chemotherapy:</p>
<p>Date of most recent treatment:</p>
<p>Date of completion of treatment or anticipated date of completion: ­­­­­­­­­­­­;</p>
<p>Androgen Deprivation Therapy (Hormonal Therapy):</p>
<p>Date of most recent treatment: ,</p>
<p>Date of completion of treatment or anticipated date of completion: ­­­­­­­­­­­­;</p>
<p>Other therapeutic procedure and/or treatment (describe):</p>
<p>Date of procedure: ,</p>
<p>Date of completion of treatment or anticipated date of completion: ­­­­­­­­­­­­]</p></td>
<td>N/A</td>
<td>Please check all applicable treatment type(s).</td>
</tr>
<tr class="even">
<td>Other surgical procedure (describe):</td>
<td><p>If <em>treatments include Surgery and other surgical procedure</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other surgical procedure performed.</td>
</tr>
<tr class="odd">
<td>Date of surgery:</td>
<td><p>If <em>treatments include Surgery and other surgical procedure</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of surgery.</td>
</tr>
<tr class="even">
<td>Date of completion of treatment or anticipated date of completion: ­­­­­­­­­­­­</td>
<td><p>If <em>treatment = Radiation therapy</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the radiation therapy's date of completion (actual or anticipated).</td>
</tr>
<tr class="odd">
<td>Date of treatment:</td>
<td><p>If <em>treatments include Brachytherapy</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of brachytherapy treatment.</td>
</tr>
<tr class="even">
<td>Date of completion of treatment or anticipated date of completion:</td>
<td><p>If <em>treatments include Antineoplastic chemotherapy</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the antineoplastic chemotherapy treatment's date of completion (actual or anticipated).</td>
</tr>
<tr class="odd">
<td>Date of completion of treatment or anticipated date of completion: ­­­­­­­­­­­­</td>
<td><p>If <em>treatments include Androgen Deprivation Therapy (Hormonal Therapy)</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the androgen deprivation therapy (hormonal therapy) treatment's date of completion (actual or anticipated).</td>
</tr>
<tr class="even">
<td>Other therapeutic procedure and/or treatment (describe):</td>
<td><p>If <em>treatments include Other therapeutic procedure and/or treatment</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other therapeutic procedure and/or treatment performed.</td>
</tr>
<tr class="odd">
<td>Date of procedure:</td>
<td><p>If <em>treatment = Other therapeutic procedure and/or treatment</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date the other therapeutic procedure and/or treatment was performed.</td>
</tr>
<tr class="even">
<td>Date of completion of treatment or anticipated date of completion: ­­­­­­­­­­­­</td>
<td><p>If <em>treatments include Other therapeutic procedure and/or treatment</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the other therapeutic procedure and/or treatment's date of completion (actual or anticipated).</td>
</tr>
</tbody>
</table>

<span id="_Toc270513770" class="anchor"></span>Table 9: Rules: DBQ – Prostate Cancer – 8. Residual conditions and/or complications

<span id="_Toc270513768" class="anchor"></span>Figure 9: Template Example: DBQ – Prostate Cancer – 3. Treatment

> ![](dvba-2-7-163-workflow-prostate-cancer/007.png)

> ![](dvba-2-7-163-workflow-prostate-cancer/008.png)

<span id="_Toc270513769" class="anchor"></span>Figure 10: Print Example: DBQ – Prostate Cancer – 3. Treatment

| 3\. Treatment                                                         |
|-----------------------------------------------------------------------|
| ------------                                                          |
| Has the Veteran completed any treatment for prostate cancer or is the |
| Veteran currently undergoing any treatment for prostate cancer?       |
| \[X\] Yes \[ \] No; watchful waiting                                  |
|                                                                       |
| If yes, indicate the treatment type(s) (check all that apply):        |
| \[ \] Treatment completed; currently in watchful waiting status       |
| \[X\] Surgery                                                         |
| \[X\] Prostatectomy                                                   |
| \[ \] Radical prostatectomy                                           |
| \[ \] Transurethral resection prostatectomy                           |
| \[ \] Other (describe):                                               |
| \[ \] Other surgical procedure (describe):                            |
| Date of surgery:                                                      |
| \[X\] Radiation therapy                                               |
| Date of completion of treatment or anticipated date of                |
| completion:                                                           |
| \[X\] Brachytherapy                                                   |
| Date of treatment:                                                    |
| \[X\] Antineoplastic chemotherapy                                     |
| Date of completion of treatment or anticipated date of                |
| completion:                                                           |
| \[X\] Androgen deprivation therapy (hormonal therapy)                 |
| Date of completion of treatment or anticipated date of                |
| completion:                                                           |
| \[X\] Other therapeutic procedure and/or treatment (describe):        |
| Date of procedure:                                                    |
| Date of completion of treatment or anticipated date of                |
| completion:                                                           |

<span id="_Toc290014257" class="anchor"></span>Table 10: Rules: DBQ – Prostate Cancer – 9. Other pertinent physical findings, complications, conditions, signs and/or symptoms

## Section 4. Voiding dysfunction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc290014258" class="anchor"></span>Table 11: Rules: DBQ – Prostate Cancer – 10. Diagnostic testing</p></caption>
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
<td><strong><u>4.Voiding dysfunction</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran have a voiding dysfunction?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else, Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran have a voiding dysfunction?</td>
</tr>
<tr class="odd">
<td>If yes, provide etiology of voiding dysfunction:</td>
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes,</em> Enabled, Mandatory</p>
<p>Else, Disabled</p></td>
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
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes,</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the voiding dysfunction cause urine leakage?</td>
</tr>
<tr class="even">
<td>Indicate severity (check one):</td>
<td><p>If <em>Does the voiding dysfunction cause urine leakage? = Yes</em>, Enabled, Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Does not require/does not use absorbent material; Requires absorbent material that is changed less than 2 times per day; Requires absorbent material that is changed 2 to 4 times per day; Requires absorbent material that is changed more than 4 times per day; Other, describe:]</td>
<td>N/A</td>
<td>Please check the applicable statement pertaining to the voiding dysfunction causing urine leakage.</td>
</tr>
<tr class="odd">
<td>Other, Describe:</td>
<td><p>If <em>Does the voiding dysfunction cause urine leakage? = Other,</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other severity of the urine leakage.</td>
</tr>
<tr class="even">
<td>b. Does the voiding dysfunction require the use of an appliance?</td>
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes,</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else, Enabled, Optional</p></td>
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
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes,</em> Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the voiding dysfunction cause increased urinary frequency?</td>
</tr>
<tr class="odd">
<td>If yes, check all that apply:</td>
<td><p>If <em>Does the voiding dysfunction cause increased urinary frequency? = Yes;</em> Enabled, Mandatory; Choose one valid value for Daytime and one valid value for Nighttime</p>
<p>Else; Disabled</p></td>
<td>[Daytime voiding interval between 2 and 3 hours; Daytime voiding interval between 1 and 2 hours; Daytime voiding interval less than 1 hour;] AND [Nighttime awakening to void 2 times; Nighttime awakening to void 3 to 4 times; Nighttime awakening to void 5 or more times]</td>
<td>N/A</td>
<td>Please check the applicable statement(s) pertaining to the increased urinary frequency.</td>
</tr>
<tr class="even">
<td>d. Does the voiding dysfunction cause signs or symptoms of obstructed voiding?</td>
<td><p>If <em>Does the Veteran have a voiding dysfunction? = Yes,</em> Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the voiding dysfunction cause signs or symptoms of obstructed voiding?</td>
</tr>
<tr class="odd">
<td>If yes, check all signs and symptoms that apply:</td>
<td><p>If <em>Does the voiding dysfunction cause signs or symptoms of obstructed voiding? = Yes;</em> Enabled, Mandatory; Choose one or more valid values</p>
<p>Else; Disabled</p></td>
<td>[Hesitancy; Slow or weak stream; Decreased force of stream; Stricture disease requiring dilatation 1 to 2 times per year; Stricture disease requiring periodic dilatation every 2 to 3 months; Recurrent urinary tract infections secondary to obstruction; Uroflowmetry peak flow rate less than 10 cc/sec; Post void residuals greater than 150 cc; Urinary retention requiring intermittent or continuous catheterization; Urinary retention requiring continuous catheterization; Other, describe:]</td>
<td>N/A</td>
<td>Please check one or more boxes to indicate the signs and symptoms of obstructed voiding.</td>
</tr>
<tr class="even">
<td>If checked, is hesitancy marked?</td>
<td><p>If <em>Voiding dysfunction signs and symptoms include Hesitancy;</em> Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please indicate whether or not hesitancy is marked.</td>
</tr>
<tr class="odd">
<td>If checked, is stream markedly slow or weak?</td>
<td><p>If <em>Voiding dysfunction signs and symptoms include Slow or weak stream</em>; Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please indicate whether or not stream is markedly slow or weak.</td>
</tr>
<tr class="even">
<td>If checked, is force of steam markedly decreased?</td>
<td><p><em>Voiding dysfunction signs and symptoms include Decreased force of stream</em>; Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please indicate whether or not force of steam is markedly decreased.</td>
</tr>
<tr class="odd">
<td>Other, describe:</td>
<td><p>If <em>Voiding dysfunction signs and symptoms include Other;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the other signs and symptoms of obstructed voiding.</td>
</tr>
</tbody>
</table>

<span id="_Toc290014258" class="anchor"></span>Table 11: Rules: DBQ – Prostate Cancer – 10. Diagnostic testing

<span id="_Toc290014230" class="anchor"></span>Figure 11: Template Example: DBQ – Prostate Cancer – 4. Voiding dysfunction

> ![](dvba-2-7-163-workflow-prostate-cancer/009.png)

> ![](dvba-2-7-163-workflow-prostate-cancer/010.png)

> ![](dvba-2-7-163-workflow-prostate-cancer/011.png)

<span id="_Toc290014231" class="anchor"></span>Figure 12: Print Example: DBQ – Prostate Cancer – 4. Voiding dysfunction

| 4\. Voiding dysfunction                                                     |
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
| Indicate severity (check one):                                              |
| \[ \] Does not require the wearing of absorbent material                    |
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
| \[X\] Yes \[ \] No                                                          |
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

<span id="_Toc270513773" class="anchor"></span>Table 12: Rules: DBQ – Prostate Cancer – 11. Functional impact

## Section 5. Urinary tract/kidney infection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<caption><p><span id="_Toc270513776" class="anchor"></span>Table 13: Rules: DBQ – Prostate Cancer – 12. Remarks, if any</p></caption>
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
<td><strong><u>5.Urinary tract/kidney infection</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else, Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran have a history of recurrent urinary tract or kidney infections?</td>
</tr>
<tr class="odd">
<td>If yes, provide etiology:</td>
<td><p>If <em>Does the Veteran have a history of recurrent symptomatic urinary tract infections?</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the etiology of the recurrent symptomatic urinary tract or kidney infections.</td>
</tr>
<tr class="even">
<td>If the Veteran has had recurrent symptomatic urinary tract or kidney infections, indicate all treatment modalities that apply:</td>
<td><p>If <em>Does the Veteran have a history of recurrent symptomatic urinary tract or kidney infections?</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[No treatment; Long-term drug therapy; Hospitalization; Drainage; Continuous intensive management; Intermittent intensive management; Other, describe:]</td>
<td>N/A</td>
<td>Please check one or more boxes to indicate applicable treatment modalities for recurrent symptomatic urinary tract or kidney infections.</td>
</tr>
<tr class="odd">
<td>If checked, list medications used for urinary tract infection and indicate dates for courses of treatment over the past 12 months:</td>
<td><p>If <em>Treatments include Long-term drug therapy;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please list medications used for urinary tract or kidney infection and their treatment dates over the past 12 months.</td>
</tr>
<tr class="even">
<td>If checked, indicate frequency of hospitalization:</td>
<td><p>If <em>Treatments include Hospitalization;</em> Enabled, Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[1 or 2 per year; More than 2 per year]</td>
<td>N/A</td>
<td>Please indicate the frequency of hospitalization.</td>
</tr>
<tr class="odd">
<td>If checked, indicate dates when drainage performed over the past 12 months:</td>
<td><p>If <em>Treatments include Drainage;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please indicate the dates that drainage was performed over the past 12 months.</td>
</tr>
<tr class="even">
<td>If checked, indicate types of treatment and medications used over the past 12 months.</td>
<td><p>If <em>Treatments include Continuous intensive management;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the types of treatment and medications for continuous intensive management used over the past 12 months.</td>
</tr>
<tr class="odd">
<td>If checked, indicate types of treatment and medications used over past 12 months:</td>
<td><p>If <em>Treatments include Intermittent intensive management;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the types of treatment and medications for intermittent intensive management used over the past 12 months.</td>
</tr>
<tr class="even">
<td>Other, describe:</td>
<td><p>If <em>Treatments include Other;</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe other treatment modalities used for urinary tract or kidney infections.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513776" class="anchor"></span>Table 13: Rules: DBQ – Prostate Cancer – 12. Remarks, if any

<span id="_Toc290014232" class="anchor"></span>Figure 13: Template Example: DBQ – Prostate Cancer – 5. Urinary tract/kidney infection

![](dvba-2-7-163-workflow-prostate-cancer/012.png)![](dvba-2-7-163-workflow-prostate-cancer/013.png)

<span id="_Toc290014233" class="anchor"></span>Figure 14: Print Example: DBQ – Prostate Cancer – 5. Urinary tract/kidney infection

| 5\. Urinary tract/kidney infection                                     |
|------------------------------------------------------------------------|
| ---------------------------------                                      |
| Does the Veteran have a history of recurrent symptomatic urinary tract |
| infections?                                                            |
| \[X\] Yes \[ \] No                                                     |
|                                                                        |
| If yes, provide etiology:                                              |
|                                                                        |
| If the Veteran has had recurrent symptomatic urinary tract or kidney   |
| infections, indicate all treatment modalities that apply:              |
| \[ \] No treatment                                                     |
| \[X\] Long-term drug therapy                                           |
| If checked, list medications used for urinary tract infection          |
| and indicate dates for courses of treatment over the past 12           |
| months:                                                                |
| \[X\] Hospitalization                                                  |
| If checked, indicate frequency of hospitalization:                     |
| \[ \] 1 or 2 per year                                                  |
| \[ \] More than 2 per year                                             |
| \[X\] Drainage                                                         |
| If checked, indicate dates when drainage performed over past           |
| 12 months:                                                             |
| \[ \] Continuous intensive management                                  |
| If checked, indicate types of treatment and medications used           |
| over past 12 months:                                                   |
| \[X\] Intermittent intensive management                                |
| If checked, indicate types of treatment and medications used           |
| over past 12 months:                                                   |
| \[X\] Other, describe:                                                 |
|                                                                        |
|                                                                        |

## Section 6. Erectile dysfunction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
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
<td><strong><u>6. Erectile dysfunction</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have erectile dysfunction?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else, Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have erectile dysfunction?</td>
</tr>
<tr class="odd">
<td>If yes, provide etiology:</td>
<td><p>If <em>Does the Veteran have erectile dysfunction?</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the etiology of erectile dysfunction.</td>
</tr>
<tr class="even">
<td>b. If the Veteran has erectile dysfunction is it as likely as not (at least 50% probability) attributable to one of the diagnoses in Section 1, including residuals of treatment for this diagnosis?</td>
<td><p>If <em>Does the Veteran have erectile dysfunction?</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not erectile dysfunction is attributable to one of the diagnoses in Section 1, including its residuals of treatment.</td>
</tr>
<tr class="odd">
<td>If yes, specify the diagnosis to which the erectile dysfunction is as likely as not attributable:</td>
<td><p>If <em>previous question = Yes;</em> Enabled; Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please specify the diagnosis to which erectile dysfunction is as likely as not attributable.</td>
</tr>
<tr class="even">
<td>c. If the Veteran has erectile dysfunction, is he able to achieve an erection sufficient for penetration and ejaculation (without medication)?</td>
<td><p>If <em>Does the Veteran have erectile dysfunction?</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not the Veteran is able to achieve an erection sufficient for penetration and ejaculation (without medication).</td>
</tr>
<tr class="odd">
<td>If no, is the Veteran able to achieve an erection sufficient for penetration and ejaculation (with medication)?</td>
<td><p>If <em>previous question = No;</em> Enabled; Mandatory; Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not the Veteran is able to achieve an erection sufficient for penetration and ejaculation (with medication).</td>
</tr>
</tbody>
</table>

<span id="_Toc290014234" class="anchor"></span>Figure 15: Template Example: DBQ – Prostate Cancer – 6. Erectile dysfunction

![](dvba-2-7-163-workflow-prostate-cancer/014.png)

<span id="_Toc290014235" class="anchor"></span>Figure 16: Print Example: DBQ – Prostate Cancer – 6. Erectile dysfunction

| 6\. Erectile dysfunction                                                  |
|---------------------------------------------------------------------------|
| ----------------------                                                    |
| a\. Does the Veteran have erectile dysfunction?                           |
| \[X\] Yes \[ \] No                                                        |
|                                                                           |
| If yes, provide etiology:                                                 |
|                                                                           |
| b\. If the Veteran has erectile dysfunction, is it as likely as not (at   |
| least 50% probability) attributable to one of the diagnoses in Section 1, |
| including residuals of treatment for this diagnosis?                      |
| \[X\] Yes \[ \] No                                                        |
|                                                                           |
| If yes, specify the diagnosis to which the erectile dysfunction is        |
| as likely as not attributable:                                            |
|                                                                           |
| c\. If the Veteran has erectile dysfunction, is he able to achieve an     |
| erection sufficient for penetration and ejaculation (without medication)? |
| \[ \] Yes \[ \] No                                                        |
|                                                                           |
| If no, is the Veteran able to achieve an erection sufficient for          |
| penetration and ejaculation (with medication)?                            |
| \[ \] Yes \[ \] No                                                        |

## Section 7. Retrograde ejaculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
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
<td><strong><u>7. Retrograde ejaculation</u></strong></td>
<td>Enabled; Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have retrograde ejaculation?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else, Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have retrograde ejaculation?</td>
</tr>
<tr class="odd">
<td>If yes, provide etiology of retrograde ejaculation.</td>
<td><p>If <em>Does the Veteran have retrograde ejaculation?</em>= <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide the etiology of retrograde ejaculation.</td>
</tr>
<tr class="even">
<td>b. If the Veteran has retrograde ejaculation, is the retrograde ejaculation as likely as not (at least a 50% probability) attributable to prostate cancer, including treatment or residuals of treatment for prostate cancer?</td>
<td><p>If <em>Does the Veteran have retrograde ejaculation?</em>= <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not retrograde ejaculation is attributable to one of the diagnoses in Section 1, including its residuals of treatment.</td>
</tr>
<tr class="odd">
<td>If yes, specify the diagnosis to which the retrograde ejaculation is as likely as not attributable:</td>
<td><p>If <em>previous question</em> <em>= Yes</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please specify the diagnosis to which retrograde ejaculation is as likely as not attributable.</td>
</tr>
</tbody>
</table>

<span id="_Toc290014236" class="anchor"></span>Figure 17: Template Example: DBQ – Prostate Cancer –7. Retrograde ejaculation

![](dvba-2-7-163-workflow-prostate-cancer/015.png)

<span id="_Toc290014237" class="anchor"></span>Figure 18: Print Example: DBQ – Prostate Cancer – 7. Retrograde ejaculation

| 7\. Retrograde ejaculation                                                     |
|--------------------------------------------------------------------------------|
| -------------------------                                                      |
| a\. Does the Veteran have retrograde ejaculation?                              |
| \[X\] Yes \[ \] No                                                             |
|                                                                                |
| If yes, provide etiology of retrograde ejaculation:                            |
|                                                                                |
| b\. If the Veteran has retrograde ejaculation, is the retrograde ejaculation   |
| as likely as not (at least a 50% probability) attributable to prostate cancer, |
| including treatment or residuals of treatment for prostate cancer?             |
| \[X\] Yes \[ \] No                                                             |
|                                                                                |
| If yes, specify the diagnosis to which the retrograde ejaculation is           |
| as likely as not attributable:                                                 |
|                                                                                |

## Section 8. Residual conditions and/or complications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
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
<td><strong><u>8. Residuals of conditions and/or complications</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have any other residual complications of prostate cancer or treatment for prostate cancer?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else, Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have any other residual complications of prostate cancer or treatment for prostate cancer?</td>
</tr>
<tr class="odd">
<td>If yes, describe:</td>
<td><p>If <em>Does the Veteran have any other residual complications of prostate cancer or treatment for prostate cancer?= Yes,</em> Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe any other residual complications.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513771" class="anchor"></span>

Figure 19: Template Example: DBQ – Prostate Cancer – 8. Residual conditions and/or complications

> ![](dvba-2-7-163-workflow-prostate-cancer/016.png)

<span id="_Toc290014239" class="anchor"></span>Figure 20: Print Example: DBQ – Prostate Cancer – 8. Residual conditions and/or complications

| 8\. Residual conditions and/or complications                           |
|------------------------------------------------------------------------|
| -------------------------------------------                            |
| a\. Does the Veteran have any other residual complications of prostate |
| cancer or treatment for prostate cancer?                               |
| \[X\] Yes \[ \] No                                                     |
|                                                                        |
| If yes, describe:                                                      |

## Section 9. Other pertinent physical findings, complications, conditions, signs and/or symptoms

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
<td><strong><u>9. Other pertinent physical findings, complications, conditions, signs and/or symptoms</u></strong></td>
<td>Enabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>a. Does the Veteran have any scars (surgical or otherwise) related to any conditions or to the treatment of any conditions listed in the Diagnosis section above?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please indicate whether or not the Veteran has any scars (surgical or otherwise) related to any conditions (or their treatment) listed in the Diagnosis section.</td>
</tr>
<tr class="odd">
<td>If yes, are any of the scars painful and/or unstable, or is the total area of all related scars greater than 39 square cm (6 square inches)?</td>
<td><p>If <em>Does the Veteran have any scars (surgical or otherwise) related to any conditions or to the treatment of conditions listed in the Diagnosis section above? = Yes;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer whether or not any of the scars are painful and/or unstable, or if the total area of all related scars is greater than 39 square cm (6 square inches).</td>
</tr>
<tr class="even">
<td>If yes, also complete a Scars Questionnaire.</td>
<td><p>If <em>If yes, are any of the scars painful and/or unstable, or is the total area of all related scars greater than 39 square cm (6 square inches)? = Yes;</em> Enabled, Read-Only</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>b. Does the Veteran have any other pertinent physical findings, complications, conditions, signs or symptoms?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled<em>,</em> Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have any other pertinent physical findings, complications, conditions, signs or symptoms?</td>
</tr>
<tr class="even">
<td>If yes, describe (brief summary):</td>
<td><p>If <em>Does the Veteran have any other pertinent physical findings, complications, conditions, signs or symptoms</em>= <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe any other pertinent findings, complications, signs and/or symptoms.</td>
</tr>
</tbody>
</table>

<span id="_Toc290014240" class="anchor"></span>Figure 21: Template Example: DBQ – Prostate Cancer – 9. Other pertinent physical findings, complications, conditions, signs and/or symptoms

> ![](dvba-2-7-163-workflow-prostate-cancer/017.png)

<span id="_Toc290014241" class="anchor"></span>Figure 22: Print Example: DBQ – Prostate Cancer – 9. Other pertinent physical findings, complications, conditions, signs and/or symptoms

| 9\. Other pertinent physical findings, complications, conditions, signs    |
|----------------------------------------------------------------------------|
| and/or symptoms                                                            |
| ----------------------------------------------------------------------     |
| a\. Does the Veteran have any scars (surgical or otherwise) related to any |
| conditions or to the treatment of any conditions listed in the Diagnosis   |
| section above?                                                             |
| \[X\] Yes \[ \] No                                                         |
|                                                                            |
| If yes, also complete a Scars Questionnaire for each scar.                 |
|                                                                            |
| b\. Does the Veteran have any other pertinent physical findings,           |
| complications, conditions, signs and/or symptoms?                          |
| \[X\] Yes \[ \] No                                                         |
|                                                                            |
| If yes, describe (brief summary):                                          |
|                                                                            |

## Section 10. Diagnostic testing

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
<td><strong><u>10. Diagnostic testing</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>NOTE: If laboratory test results are in the medical record and reflect the Veteran’s current condition, repeat testing is not required.</td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Are there any significant diagnostic test findings and/or results?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled<em>,</em> Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Are there any significant diagnostic test findings and/or results?</td>
</tr>
<tr class="even">
<td>If yes, provide type of test or procedure, date and results (brief summary):</td>
<td><p>If <em>Are there any significant diagnostic test findings and/or results</em>= <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please provide type of test or procedure, date and results.</td>
</tr>
</tbody>
</table>

<span id="_Toc290014242" class="anchor"></span>Figure 23: Template Example: DBQ – Prostate Cancer – 10. Diagnostic testing

> ![](dvba-2-7-163-workflow-prostate-cancer/018.png)

<span id="_Toc290014243" class="anchor"></span>Figure 24: Print Example: DBQ – Prostate Cancer – 10. Diagnostic testing

| 10\. Diagnostic testing                                                    |
|----------------------------------------------------------------------------|
| ----------------------                                                     |
| NOTE: If laboratory test results are in the medical record and reflect the |
| Veteran's current condition, repeat testing is not required.               |
|                                                                            |
| Are there any significant diagnostic test findings and/or results?         |
| \[X\] Yes \[ \] No                                                         |
|                                                                            |
| If yes, provide type of test or procedure, date and results (brief         |
| summary):                                                                  |

## Section 11. Functional impact

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
<td><strong><u>11. Functional Impact</u></strong></td>
<td>Enabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran’s prostate cancer impact his ability to work?</td>
<td><p>If <em>Does the Veteran now have or has he ever been diagnosed with prostate cancer? = Yes;</em> Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran's prostate cancer impact his ability to work?</td>
</tr>
<tr class="odd">
<td>If yes, describe the impact of the Veteran’s prostate cancer, providing one or more examples:</td>
<td><p>If <em>Does the Veteran’s prostate cancer impact his ability to work?</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the impact of prostate cancer on the Veteran's ability to work, providing one or more examples.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513774" class="anchor"></span>Figure 25: Template Example: DBQ – Prostate Cancer – 11. Functional impact

> ![](dvba-2-7-163-workflow-prostate-cancer/019.png)

<span id="_Toc270513775" class="anchor"></span>Figure 26: Print Example: DBQ – Prostate Cancer – 11. Functional impact

| 11\. Functional impact                                         |
|----------------------------------------------------------------|
| -----------------                                              |
| Does the Veteran's prostate cancer impact his ability to work? |
| \[X\] Yes \[ \] No                                             |
|                                                                |
| If yes, describe the impact of the Veteran's prostate cancer,  |
| providing one or more examples:                                |

## Section 12. Remarks, if any

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below.

| Field/Question             | Field Disposition | Valid Values | Format | Error Message |
|--------------------------------|-----------------------|------------------|------------|-------------------|
| <u>12. Remarks, if any</u> | Enabled*,* Optional   | N/A              | Free Text  | N/A               |

<span id="_Toc270513777" class="anchor"></span>Figure 27: Template Example: DBQ – Prostate Cancer – 12. Remarks, if any

> ![](dvba-2-7-163-workflow-prostate-cancer/020.png)

<span id="_Toc270513778" class="anchor"></span>Figure 28: Print Example: DBQ – Prostate Cancer – 12. Remarks, if any

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>12. Remarks, if any</p>
<p>------------------</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Prostate Cancer DBQ-AMIE Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The DBQ-AMIE worksheets are accessed via the Print Blank C&P Worksheet menu \[DVBA C

> PRINT BLANK C&P WORKSHE\] option. Select the “DBQ PROSTATE CANCER” worksheet.

> DBQ-AMIE worksheets should be sent to a printer.

Prostate Cancer

Disability Benefits Questionnaire

Name of patient/Veteran: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ SSN: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Your patient is applying to the U. S. Department of Veterans Affairs

(VA) for disability benefits. VA will consider the information you

provide on this questionnaire as part of their evaluation in processing

the Veteran's claim.

1\. Diagnosis

Does the Veteran now have or has he ever been diagnosed with prostate

cancer?

\_\_\_ Yes \_\_\_ No

If no, provide rationale (e.g. Veteran has never had prostate cancer):

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If yes, provide only diagnoses that pertain to prostate cancer.

Diagnosis \#1: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Diagnosis \#2: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Diagnosis \#3: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of diagnosis: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If there are additional diagnoses that pertain to prostate cancer, list using

above format: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

2\. Medical history

a\. Describe the history (including onset and course) of the Veteran's

prostate cancer condition (brief summary): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. Indicate status of disease:

\_\_\_ Active

\_\_\_ Remission

Page: 2

Disability Benefits Questionnaire for

Prostate Cancer

3\. Treatment

Has the Veteran completed any treatment for prostate cancer or is the

Veteran currently undergoing any treatment for prostate cancer?

\_\_\_ Yes \_\_\_ No; watchful waiting

If yes, indicate treatment type(s) (check all that apply):

\_\_\_ Treatment completed; currently in watchful waiting status

\_\_\_ Surgery

\_\_\_ Prostatectomy

\_\_\_ Radical prostatectomy

\_\_\_ Transurethral resection prostatectomy

\_\_\_ Other (describe)\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other surgical procedure (describe): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of surgery: \_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Radiation therapy

Date of completion of treatment or anticipated date of

completion:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Brachytherapy

Date of treatment: \_\_\_\_\_\_\_\_\_\_

\_\_\_ Antineoplastic chemotherapy

Date of completion of treatment or anticipated date of

completion: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Androgen deprivation therapy (hormonal therapy)

Date of completion of treatment or anticipated date of

completion: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other therapeutic procedure and/or treatment (describe): \_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Date of procedure: \_\_\_\_\_\_\_\_\_\_

Date of completion of treatment or anticipated date of

completion: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 3

Disability Benefits Questionnaire for

Prostate Cancer

4\. Voiding dysfunction

Does the Veteran have a voiding dysfunction?

\_\_\_ Yes \_\_\_ No

If yes, provide etiology of voiding dysfunction: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

If the Veteran has a voiding dysfunction, complete the following questions:

a\. Does the voiding dysfunction cause urine leakage?

\_\_\_ Yes \_\_\_ No

Indicate severity (check one):

\_\_\_ Does not require the wearing of absorbent material

\_\_\_ Requires absorbent material which must be changed less than 2

times per day

\_\_\_ Requires absorbent material which must be changed 2 to 4 times

per day

\_\_\_ Requires absorbent material which must be changed more than 4

times per day

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. Does the voiding dysfunction require the use of an appliance?

\_\_\_ Yes \_\_\_ No

If yes, describe the appliance: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

c\. Does the voiding dysfunction cause increased urinary frequency?

\_\_\_ Yes \_\_\_ No

If yes, check all that apply:

\_\_\_ Daytime voiding interval between 2 and 3 hours

\_\_\_ Daytime voiding interval between 1 and 2 hours

\_\_\_ Daytime voiding interval less than 1 hour

\_\_\_ Nighttime awakening to void 2 times

\_\_\_ Nighttime awakening to void 3 to 4 times

\_\_\_ Nighttime awakening to void 5 or more times

Page: 4

Disability Benefits Questionnaire for

Prostate Cancer

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

\_\_\_ Stricture disease requiring periodic dilatation every 2 to 3

months

\_\_\_ Recurrent urinary tract infections secondary to obstruction

\_\_\_ Uroflowmetry peak flow rate less than 10 cc/sec

\_\_\_ Post void residuals greater than 150 cc

\_\_\_ Urinary retention requiring intermittent catheterization

\_\_\_ Urinary retention requiring continuous catheterization

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 5

Disability Benefits Questionnaire for

Prostate Cancer

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

treatment over the past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Hospitalization

If checked, indicate frequency of hospitalization:

\_\_\_ 1 or 2 per year

\_\_\_ \> 2 per year

\_\_\_ Drainage

If checked, indicate dates when drainage performed over past 12

months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Continuous intensive management

If checked, indicate types of treatment and medications used

over past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Intermittent intensive management

If checked, indicate types of treatment and medications used

over past 12 months: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_ Other, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 6

Disability Benefits Questionnaire for

Prostate Cancer

6\. Erectile dysfunction

a\. Does the Veteran have erectile dysfunction?

\_\_\_ Yes \_\_\_ No

If yes, provide etiology: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. If the Veteran has erectile dysfunction, is it as likely as not (at least

a 50% probability) attributable to one of the diagnoses in Section 1,

including residuals of treatment for this diagnosis?

\_\_\_ Yes \_\_\_ No

If yes, specify the diagnosis to which the erectile dysfunction is as likely

as not attributable: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

c\. If the Veteran has erectile dysfunction, is he able to achieve an erection

sufficient for penetration and ejaculation (without medication)?

\_\_\_ Yes \_\_\_ No

If no, is the Veteran able to achieve an erection sufficient for penetration

and ejaculation (with medication)?

\_\_\_ Yes \_\_\_ No

7\. Retrograde ejaculation

a\. Does the Veteran have retrograde ejaculation?

\_\_\_ Yes \_\_\_ No

If yes, provide etiology of the retrograde ejaculation: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

b\. If the Veteran has retrograde ejaculation, is it as likely as not (at

least a 50% probability) attributable to one of the diagnoses in Section 1,

including residuals of treatment for this diagnosis?

\_\_\_ Yes \_\_\_ No

If yes, specify the diagnosis to which the retrograde ejaculation is as

likely as not attributable: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

8\. Residual conditions and/or complications

a\. Does the Veteran have any other residual conditions and/or complications

due to prostate cancer or treatment for prostate cancer?

\_\_\_ Yes \_\_\_ No

If yes, describe: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 7

Disability Benefits Questionnaire for

Prostate Cancer

9\. Other pertinent physical findings, complications, conditions, signs and/or

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

complications, conditions, signs or symptoms?

\_\_\_ Yes \_\_\_ No

If yes, describe(brief summary): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

10\. Diagnostic testing

> **NOTE:** If laboratory test results are in the medical record and reflect the

Veteran's current condition, repeat testing is not required.

Are there any significant diagnostic test findings and/or results?

\_\_\_ Yes \_\_\_ No

If yes, provide type of test or procedure, date and results (brief summary):

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Page: 8

Disability Benefits Questionnaire for

Prostate Cancer

11\. Functional impact

Does the Veteran's prostate cancer impact his ability to work?

\_\_\_ Yes \_\_\_ No

If yes, describe the impact of the Veteran's prostate cancer, providing one

or more examples: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

12\. Remarks, if any: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Physician signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date: \_\_\_\_\_\_\_\_\_\_\_\_

Physician printed name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Phone: \_\_\_\_\_\_\_\_\_\_\_

Medical license \#: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Fax: \_\_\_\_\_\_\_\_\_\_\_\_\_

Physician address: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> **NOTE:** VA may request additional medical information, including additional

examinations if necessary to complete VA's review of the Veteran's

application.