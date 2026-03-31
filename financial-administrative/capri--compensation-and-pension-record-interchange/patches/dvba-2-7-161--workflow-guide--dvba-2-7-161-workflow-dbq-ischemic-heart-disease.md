---
title: DVBA*2.7*161 Workflow - DBQ Ischemic Heart Disease
doc_type: WF
doc_label: Workflow Guide
doc_layer: patch
doc_subject: Workflow - DBQ Ischemic Heart Disease
app_code: CAPRI
app_name: Compensation and Pension Record Interchange
section: FIN
app_status: active
pkg_ns: DVBA
patch_ver: 2.7
patch_id: DVBA*2.7*161
group_key: "CAPRI:DVBA:2.7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - strong
  - class
  - enabled
  - span
  - table
  - mandatory
  - please
  - blockquote
  - style
  - width
page_count: 0
word_count: 5399
section_count: 11
table_count: 52
figure_count: 2
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2011
revision_count: 7
revision_newest: 02/07/2011
revision_oldest: 08/02/2010
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_p161_dbq_ihd_wf.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/dvba_27_p161_dbq_ihd_wf.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=133"
---

![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/001.png)

Compensation and Pension Record Interchange (CAPRI)

Ischemic Heart Disease (IHD)

Disability Benefits Questionnaire (DBQ)

Workflow

February 2011

Office of Enterprise Development

Management & Financial Systems

Revision History

|            |                                                                                                                                                              |          |                  |
|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------|
| Date       | Description (Patch \# if applicable)                                                                                                                         | Author   | Technical Writer |
| 08/02/2010 | Document created for patch 154.                                                                                                                              | REDACTED | REDACTED         |
| 08/17/2010 | Added ICD codes and other misc changes for patch 154.                                                                                                        | REDACTED | REDACTED         |
| 10/12/2010 | Answering ‘No’ to Section 5: Is there evidence of cardiac hypertrophy or dilatation? Allows user to reference the source and date of the test for patch 159. | REDACTED | N/A              |
| 10/28/2010 | Changed wording in Introduction for patch 159.                                                                                                               | REDACTED | N/A              |
| 11/2/2010  | Added wording in Note in Diagnosis 1 for patch 159.                                                                                                          | REDACTED | N/A              |
| 12/28/2010 | Moved IHD Note for patch 161.                                                                                                                                | REDACTED | N/A              |
| 02/07/2011 | Change to Section 4.b. MET’s testing (Patch 161)                                                                                                             | REDACTED | N/A              |

<span id="_Toc286754192" class="anchor"></span>Table 1: Rules: DBQ – IHD – Name of patient/Veteran

  
Table of Contents

Table of Tables and Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Overview](#overview)
- [Ischemic Heart Disease (IHD) DBQ – History Tab](#ischemic-heart-disease-ihd-dbq-history-tab)
  - [Name of patient/Veteran](#name-of-patientveteran)
  - [Section 1. Diagnosis](#section-1-diagnosis)
  - [Section 2. Medical history](#section-2-medical-history)
  - [Section 3. Congestive heart failure (CHF)](#section-3-congestive-heart-failure-chf)
  - [Section 4. Cardiac functional assessment](#section-4-cardiac-functional-assessment)
  - [Section 5. Diagnostic testing](#section-5-diagnostic-testing)
  - [Section 6. Functional impact](#section-6-functional-impact)
  - [## Section 7. Remarks, if any](#section-7-remarks-if-any)
- [IHD AMIE-DBQ Worksheet](#ihd-amie-dbq-worksheet)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides a high level overview of the contents found on the Ischemic Heart Disease (IHD) Disability Benefits Questionnaire (DBQ). The DBQ can be populated via an online template within the CAPRI C&P Worksheets tab and then printed OR it can be printed via AMIE (AUTOMATED MEDICAL INFORMATION EXCHANGE) and then manually populated. This document contains the edit rules for the template as well as an example of how the template will look online in CAPRI or printed from CAPRI. It also contains the layout for the AMIE worksheet to depict how it will look when printed from AMIE.

For more detailed information on standard template functionality not covered in this document, please refer to the C&P Worksheet Tab Functionalities section of the [CAPRI GUI User Guide](http://www4.va.gov/vdl/documents/Financial_Admin/CAPRI/capri_um.pdf).

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Ischemic Heart Disease (IHD) DBQ provides the ability to capture information related to IHD and its treatment.

Each DBQ template contains a standard footer containing a note stating that “VA may request additional medical information, including additional examinations if necessary to complete VA’s review of the Veteran’s application.” (see Figure 1 and 2).

<span id="_Toc286754151" class="anchor"></span>Figure 1: Template Example: DBQ – Standard VA Note

![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/002.png)

<span id="_Toc286754152" class="anchor"></span>Figure 2: Print Example: DBQ – Standard VA Note

|                                                                                     |
|-------------------------------------------------------------------------------------|
| NOTE: VA may request additional medical information, including additional       |
| examinations if necessary to complete VA's review of the Veteran's application. |
|                                                                                     |

<span id="_Toc270513060" class="anchor"></span>Table 2: Rules: DBQ – IHD – 1. Diagnosis

A number of fields on the Ischemic Heart Disease (IHD) template are mandatory and require a response (value) prior to the exam being marked as completed. Some questions may activate a Pop-up window displaying information as to each question that needs to be answered before the template can be completed.

# Ischemic Heart Disease (IHD) DBQ – History Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Name of patient/Veteran

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section must be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

| Field/Question                                                                                                                                                                                                                         | Field Disposition | Valid Values | Format | Error Message                             |     |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|------------------|------------|-----------------------------------------------|-----|
| Disability Benefits Questionnaire                                                                                                                                                                                                          | Disabled, Read-Only   | N/A              | N/A        | N/A                                           |     |
| Ischemic Heart Disease (IHD)                                                                                                                                                                                                               | Disabled, Read-Only   | N/A              | N/A        | N/A                                           |     |
| Name of patient/Veteran                                                                                                                                                                                                                    | Enabled, Mandatory    | N/A              | Free Text  | Please enter the name of the patient/Veteran. |     |
| Your patient is applying to the U. S. Department of Veterans Affairs (VA) for disability benefits.  VA will consider the information you provide on this questionnaire as part of their evaluation in processing the Veteran’s claim.  | Disabled, Read-Only   | N/A              | N/A        | N/A                                           |     |

<span id="_Toc270513063" class="anchor"></span>Table 3: Rules: DBQ – IHD – 2. Medical history

<span id="_Toc286754153" class="anchor"></span>Figure 3: Template Example: DBQ – IHD – Name of patient/Veteran

![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/003.png)

<span id="_Toc286754154" class="anchor"></span>Figure 4: Print Example: DBQ – IHD – Name of patient/Veteran

| Disability Benefits Questionnaire                                            |
|------------------------------------------------------------------------------|
| Ischemic Heart Disease (IHD)                                                 |
|                                                                              |
| Name of patient/Veteran: Patient1, Test 1                                    |
|                                                                              |
| Your patient is applying to the U.S. Department of Veterans Affairs (VA) for |
| disability benefits. VA will consider the information you provide on this    |
| questionnaire as part of their evaluation in processing the Veteran's claim. |

<span id="_Toc270513066" class="anchor"></span>Table 4: Rules: DBQ – IHD – 3. Congestive heart failure (CHF)

## Section 1. Diagnosis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The question “Does the Veteran have ischemic heart disease (IHD)?” must be answered before this template can be completed.

- If it is answered with Yes, all other questions requiring an answer as described by the rules in this document must be answered before the template can be completed.
- If it is answered with No, the template may be completed without answering any additional questions or the user may input answers to any of the optional questions as indicated by the rules described in this document.

All questions will be printed even if they have not been answered.

If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below and must be answered before this template can be completed.

<table>
<caption><p><br />
<span id="_Toc286754196" class="anchor"></span>Table 5: Rules: DBQ – IHD – 4. Cardiac functional assessment</p></caption>
<colgroup>
<col style="width: 40%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 11%" />
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
<td><strong><u>1. Diagnosis</u></strong></td>
<td>Disabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td><p><em><strong>NOTE</strong>: IHD includes, but is not limited to, acute, subacute, and old myocardial infarction; atherosclerotic cardiovascular disease including coronary artery disease (including coronary spasm) and coronary bypass surgery; and stable, unstable and Prinzmetal’s angina<strong>.</strong> <u>IHD does not include</u> hypertension or peripheral manifestations of arteriosclerosis such as peripheral vascular disease or stroke, or any other condition that does not qualify within the generally accepted medical definition of ischemic heart disease.</em></p>
<p><em>IHD encompasses any atherosclerotic heart disease resulting in clinically significant ischemia or requiring coronary revascularization.</em></p></td>
<td>Disabled, Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Does the Veteran have ischemic heart disease (IHD)?</td>
<td>Enabled, Mandatory, Choose one valid value</td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please answer the question: Does the Veteran have ischemic heart disease (IHD)?</td>
</tr>
<tr class="even">
<td><strong>NOTE: Provide only diagnoses that pertain to IHD.</strong></td>
<td>Disabled, Read Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Diagnosis #1:</td>
<td><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter a value in the ‘Diagnosis #1’ field.</td>
</tr>
<tr class="even">
<td>ICD code:</td>
<td><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for diagnosis #1.</td>
</tr>
<tr class="odd">
<td>Date of diagnosis #1:</td>
<td><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled, Mandatory</p>
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
<td><p>If <em>Diagnosis #2 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for diagnosis #2.</td>
</tr>
<tr class="even">
<td>Date of diagnosis #2:</td>
<td><p>If <em>Diagnosis #2 is populated</em>; Enabled, Mandatory</p>
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
<td><p>If <em>Diagnosis #3 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the ICD code for diagnosis #3.</td>
</tr>
<tr class="odd">
<td>Date of diagnosis #3:</td>
<td><p>If <em>Diagnosis #3 is populated</em>; Enabled, Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of diagnosis #3.</td>
</tr>
<tr class="even">
<td>If additional diagnoses that pertain to IHD, list using above format:</td>
<td>Enabled, Optional</td>
<td>N/A</td>
<td>Free Text</td>
<td>N/A</td>
</tr>
</tbody>
</table>

  
<span id="_Toc286754196" class="anchor"></span>Table 5: Rules: DBQ – IHD – 4. Cardiac functional assessment

  
<span id="_Toc286754155" class="anchor"></span>Figure 5: Template Example: DBQ – IHD – 1. Diagnosis

> ![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/004.png)

> ![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/005.png)

<span id="_Toc270513062" class="anchor"></span>

Figure 6: Print Example: DBQ – IHD – 1. Diagnosis

| 1\. Diagnosis                                                              |
|----------------------------------------------------------------------------|
| ------------                                                               |
|                                                                            |
| NOTE: IHD includes, but is not limited to, acute, subacute, and old        |
| myocardial infarction; atherosclerotic cardiovascular disease including    |
| Coronary artery disease (including coronary spasm) and coronary bypass     |
| surgery; and stable, unstable and Prinzmetal's angina. IHD does not        |
| include hypertension or peripheral manifestations of arteriosclerosis such |
| as peripheral vascular disease or stroke, or any other condition that does |
| not qualify within the generally accepted medical definition of ischemic   |
| heart disease.                                                             |
|                                                                            |
| IHD encompasses any atherosclerotic heart disease resulting in clinically  |
| significant ischemia or requiring coronary revascularization.              |
|                                                                            |
| Does the Veteran have ischemic heart disease (IHD)? \[X\] Yes \[ \] No     |
|                                                                            |
| NOTE: Provide only diagnoses that pertain to IHD.                          |
|                                                                            |
| Diagnosis \#1: First diagnosis will be entered here                        |
| ICD code: First ICD code will be entered here                              |
| Date of diagnosis \#1: First diagnosis date will be entered here           |
|                                                                            |
| Diagnosis \#2: Second diagnosis will be entered here                       |
| ICD code: Second ICD code will be entered here                             |
| Date of diagnosis \#2: Second diagnosis date will be entered here          |
|                                                                            |
| Diagnosis \#3: Third diagnosis will be entered here                        |
| ICD code: Third ICD code will be entered here                              |
| Date of diagnosis \#3: Third diagnosis date will be entered here           |
|                                                                            |
| If additional diagnoses that pertain to IHD, list using above format:      |
| Additional diagnoses will be entered here along with ICD code and date     |

<span id="_Toc286754197" class="anchor"></span>Table 6: Rules: DBQ – IHD – 5. Diagnostic testing

## Section 2. Medical history

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below and must be answered before this template can be completed.

<table>
<caption><p><span id="_Toc270513075" class="anchor"></span>Table 7: Rules: DBQ – IHD – 6. Functional impact</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 27%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
<tr class="odd">
<th><strong><u>2. Medical history</u></strong></th>
<th>Disabled; Read-Only</th>
<th>N/A</th>
<th>N/A</th>
<th>N/A</th>
</tr>
<tr class="header">
<th>Does the Veteran's treatment plan include taking continuous medication for the diagnosed condition?</th>
<th><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please answer the question: Does the Veteran's treatment plan include taking continuous medication for the diagnosed condition?</th>
</tr>
<tr class="odd">
<th>List medications:</th>
<th><p>If preceding question = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></th>
<th>N/A</th>
<th>Free Text</th>
<th>Please list medications.</th>
</tr>
<tr class="header">
<th>Is there a History of:</th>
<th>Disabled, Read Only</th>
<th>N/A</th>
<th>N/A</th>
<th>N/A</th>
</tr>
<tr class="odd">
<th>Percutaneous coronary intervention (PCI)</th>
<th><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please answer whether or not there is a history of percutaneous coronary intervention (PCI).</th>
</tr>
<tr class="header">
<th>Percutaneous coronary intervention Treatment facility/date:</th>
<th><p>If <em>History of PCI</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></th>
<th>N/A</th>
<th>Free Text</th>
<th>Please enter the percutaneous coronary intervention (PCI) treatment facility/date.</th>
</tr>
<tr class="odd">
<th>Myocardial infarction</th>
<th><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please answer whether or not there is a history of myocardial Infarction.</th>
</tr>
<tr class="header">
<th>Myocardial infarction Treatment facility/date:</th>
<th><p>If <em>History of Myocardial infarction</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></th>
<th>N/A</th>
<th>Free Text</th>
<th>Please enter the myocardial infarction treatment facility/date.</th>
</tr>
<tr class="odd">
<th>Coronary bypass surgery</th>
<th><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please answer whether or not there is a history of coronary bypass surgery.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc270513075" class="anchor"></span>Table 7: Rules: DBQ – IHD – 6. Functional impact

<table>
<caption><p><span id="_Toc286754199" class="anchor"></span>Table 8: Rules: DBQ – IHD – 7. Remarks, if any</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
<tr class="odd">
<th>Coronary bypass surgery Treatment facility/date:</th>
<th><p>If <em>History of Coronary bypass surgery</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></th>
<th>N/A</th>
<th>Free Text</th>
<th>Please enter the coronary bypass surgery treatment facility/date.</th>
</tr>
<tr class="header">
<th>Heart transplant</th>
<th><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please answer whether or not there is a history of heart transplant.</th>
</tr>
<tr class="odd">
<th>Heart transplant Treatment facility/date:</th>
<th><p>If <em>History of Heart transplant</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></th>
<th>N/A</th>
<th>Free Text</th>
<th>Please enter the heart transplant treatment facility/date.</th>
</tr>
<tr class="header">
<th>If yes, is it as likely as not that the Veteran’s heart transplant is due to IHD?</th>
<th><p>If <em>History of Heart transplant</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please provide an answer to the question: If yes, is it as likely as not that the Veteran's heart transplant is due to IHD?</th>
</tr>
<tr class="odd">
<th>Implanted cardiac pacemaker</th>
<th><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please answer whether or not there is a history of Implanted cardiac pacemaker.</th>
</tr>
<tr class="header">
<th>Implanted cardiac pacemaker Treatment facility/date:</th>
<th><p>If <em>History of Implanted cardiac pacemaker</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></th>
<th>N/A</th>
<th>Free Text</th>
<th>Please enter the implanted cardiac pacemaker treatment facility/date.</th>
</tr>
<tr class="odd">
<th>If yes, is it as likely as not that the Veteran’s pacemaker is due to IHD?</th>
<th><p>If <em>History of Implanted cardiac pacemaker</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please provide an answer to the question: If yes, is it as likely as not that the Veteran's pacemaker is due to IHD?</th>
</tr>
<tr class="header">
<th>Implanted automatic implantable cardioverter defibrillator (AICD)</th>
<th><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please answer whether or not there is a history of implanted automatic implantable cardioverter defibrillator (AICD).</th>
</tr>
<tr class="odd">
<th><p>Implanted automatic implantable cardioverter defibrillator (AICD)</p>
<p>Treatment facility/date:</p></th>
<th><p>If <em>History of AICD</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></th>
<th>N/A</th>
<th>Free Text</th>
<th>Please enter the implanted automatic implantable cardioverter defibrillator (AICD) treatment facility/date.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc286754199" class="anchor"></span>Table 8: Rules: DBQ – IHD – 7. Remarks, if any

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field/Question</strong></th>
<th><strong>Field Disposition</strong></th>
<th><strong>Valid Values</strong></th>
<th><strong>Format</strong></th>
<th><strong>Error Message</strong></th>
</tr>
<tr class="odd">
<th>If yes, is it as likely as not that the Veteran’s AICD is due to IHD?</th>
<th><p>If <em>History of AICD</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></th>
<th>[Yes; No]</th>
<th>N/A</th>
<th>Please provide an answer to the question: If yes, is it as likely as not that the Veteran's AICD is due to IHD?</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc270513064" class="anchor"></span>Figure 7: Template Example: DBQ – IHD – 2. Medical history

> ![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/006.png)

  
<span id="_Toc286754158" class="anchor"></span>Figure 8: Print Example: DBQ – IHD – 2. Medical history

| 2. Medical history                                                          |
|---------------------------------------------------------------------------------|
| ------------------                                                          |
| Does the Veteran's treatment plan include taking continuous medication      |
| for the diagnosed condition? \[X\] Yes \[ \] No                             |
| List medication: Medication 1 will be entered here                          |
|                                                                                 |
| Medication 2 will be entered here                                           |
|                                                                                 |
| Is there a history of:                                                      |
| Percutaneous coronary intervention (PCI) \[X\] Yes \[ \] No                 |
| Treatment facility/date: facility name and date for PCI will be here        |
|                                                                                 |
| Myocardial infarction \[X\] Yes \[ \] No                                    |
| Treatment facility/date: facility name and date for infarction will be here |
|                                                                                 |
| Coronary bypass surgery \[X\] Yes \[ \] No                                  |
| Treatment facility/date: facility name and date for bypass will be here     |
|                                                                                 |
| Heart transplant \[X\] Yes \[ \] No                                         |
| Treatment facility/date: facility name and date for transplant will be here |
|                                                                                 |
| If yes, is it as likely as not that the Veteran's heart transplant is due   |
| to IHD? \[X\] Yes \[ \] No                                                  |
| Implanted cardiac pacemaker \[X\] Yes \[ \] No                              |
| Treatment facility/date: facility name and date for pacemaker will be here  |
|                                                                                 |
| If yes, is it as likely as not that the Veteran's pacemaker is due to IHD?  |
| \[ \] Yes \[X\] No                                                          |
| Implanted automatic implantable cardioverter defibrillator (AICD)           |
| \[X\] Yes \[ \] No                                                          |
| Treatment facility/date: facility name and date for AICD will be here       |
| If yes, is it as likely as not that the Veteran's ACID is due to IHD?       |
| \[ \] Yes \[X\] No                                                          |

## Section 3. Congestive heart failure (CHF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table style="width:100%;">
<colgroup>
<col style="width: 20%" />
<col style="width: 33%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 24%" />
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
<td><strong><u>3. Congestive heart failure (CHF)</u></strong></td>
<td>Disabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran have CHF?</td>
<td><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran have CHF?</td>
</tr>
<tr class="odd">
<td>Is the Veteran’s CHF chronic?</td>
<td><p>If <em>Does the Veteran have CHF</em> = <em>Yes;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Is the Veteran's CHF chronic?</td>
</tr>
<tr class="even">
<td>If the Veteran’s CHF is not chronic, has the Veteran had more than one episode of acute CHF in the past year?</td>
<td><p>If <em>Is the Veteran’s CHF chronic</em> = <em>No;</em> Enabled, Mandatory, Choose one valid value</p>
<p>Else; Disabled</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: If the Veteran's CHF is not chronic, has the Veteran had more than one episode of acute CHF in the past year?</td>
</tr>
<tr class="odd">
<td>Treatment facility/date of most recent episode of CHF:</td>
<td><p>If <em>Is the Veteran’s CHF is not chronic, has the Veteran had more than one episode of acute CHF in the past year</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the treatment facility/date of most recent episode of CHF.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513067" class="anchor"></span>Figure 9: Template Example: DBQ – IHD – 3. Congestive heart failure (CHF)

> ![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/007.png)

<span id="_Toc270513068" class="anchor"></span>Figure 10: Print Example: DBQ – IHD – 3. Congestive heart failure (CHF)

|                                                                                    |
|------------------------------------------------------------------------------------|
| 3. Congestive heart failure (CHF)                                              |
| ---------------------------------                                              |
| Does the Veteran have CHF? \[X\] Yes \[ \] No                                  |
| Is the Veteran's CHF chronic? \[ \] Yes \[X\] No                               |
| If the Veteran's CHF is not chronic, has the Veteran had more than one episode |
| of acute CHF in the past year? \[X\] Yes \[ \] No                              |
| Treatment facility/date of most recent episode of CHF: facility                |
| name and date for CHF will be here                                             |
|                                                                                    |

## Section 4. Cardiac functional assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 20%" />
<col style="width: 23%" />
<col style="width: 9%" />
<col style="width: 23%" />
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
<td><strong><u>4. Cardiac functional assessment</u></strong></td>
<td>Disabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Has a diagnostic exercise test been conducted?</td>
<td><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled, Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Has a diagnostic exercise test been conducted?</td>
</tr>
<tr class="odd">
<td>a. If yes, provide level of METs the Veteran can perform as shown by most recent diagnostic exercise testing:</td>
<td><p>If <em>Has a diagnostic exercise test been conducted</em> = <em>YES</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter a value indicating the level of METs testing the Veteran can perform as shown by diagnostic exercise testing.</td>
</tr>
<tr class="even">
<td>Date of most recent diagnostic exercise test:</td>
<td><p>If <em>Has a diagnostic exercise test been conducted</em> = <em>YES</em>; Enabled, Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the most recent diagnostic exercise test.</td>
</tr>
<tr class="odd">
<td><p>b. If exercise METs testing was not completed because it is not required as part of Veteran's treatment plan, complete the following METs test based on the Veteran's responses:</p>
<p>Lowest level of activity at which the Veteran reports symptoms (check all symptoms that apply)</p></td>
<td><p>If <em>Has a diagnostic exercise test been conducted</em> = <em>No</em>; Enabled, Mandatory, Choose one or move values</p>
<p>Else; Enabled, Optional</p></td>
<td><p>[dyspnea;</p>
<p>fatigue;</p>
<p>angina;</p>
<p>dizziness;</p>
<p>syncope]</p></td>
<td>N/A</td>
<td>Please check one or more boxes to indicate which symptoms occur.</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><p>[(1-3 Mets) This METs level has been found to be consistent with activities such as eating, dressing, taking a shower, slow walking (2 mph) for 1-2 blocks.; (&gt;3-5 Mets) This METs level has been found to be consistent with activities such as light yard work (weeding) , mowing lawn (power mower), brisk walking (4 mph).;</p>
<p>(&gt;5-7 METs) This METs level has been found to be consistent with activities such as golfing (without cart), mowing lawn (push mower), heavy yard work (digging).;</p>
<p>(&gt;7-10 METs) This METs level has been found to be consistent with activities such as climbing stairs quickly, moderate bicycling, sawing wood, jogging (6 mph).;</p>
<p>The Veteran denies experiencing above symptoms with any level of physical activity.]</p></td>
<td></td>
<td>Please check one of the boxes to indicate the METs level at which symptoms occur.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513070" class="anchor"></span>Figure 11: Template Example: DBQ – IHD – 4. Cardiac functional assessment

> ![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/008.png)

<span id="_Toc270513071" class="anchor"></span>Figure 12: Print Example: DBQ – IHD – 4. Cardiac functional assessment

|                                                                              |
|------------------------------------------------------------------------------|
| 4. Cardiac functional assessment                                         |
| --------------------------------                                         |
| Has a diagnostic exercise test been conducted? \[ \] Yes \[X\] No        |
| a. If yes, provide level of METs the Veteran can perform as shown by     |
| the most recent diagnostic exercise testing:                             |
| Date of most recent diagnostic exercise test:                            |
|                                                                              |
| b. If exercise METs testing was not completed because it is not required |
| as part of Veteran's treatment plan, complete the following METs test    |
| based on the Veteran's responses:                                        |
|                                                                              |
| Lowest level of activity at which the Veteran reports symptoms:          |
| (check all symptoms that apply)                                          |
| \[X\] dyspnea \[X\] fatigue \[X\] angina \[X\] dizziness \[X\] syncope   |
|                                                                              |
| \[ \] (1-3 METs) This METs level has been found to be consistent with    |
| activities such as eating, dressing, taking a                            |
| shower, slow walking (2 mph) for 1-2 blocks                              |
|                                                                              |
| \[ \] (\>3-5 METs) This METs level has been found to be consistent with  |
| activities such as light yard work (weeding),                            |
| mowing lawn (power mower), brisk walking (4 mph)                         |
|                                                                              |
| \[X\] (\>5-7 METs) This METs level has been found to be consistent with  |
| activities such as golfing (without cart), mowing                        |
| lawn (push mower), heavy yard work (digging)                             |
|                                                                              |
| \[ \] (\>7-10 METs) This METs level has been found to be consistent with |
| activities such as climbing stairs quickly,                              |
| moderate bicycling, sawing wood, jogging (6 mph)                         |
|                                                                              |
| \[ \] The Veteran denies experiencing above symptoms with                |
| any level of physical activity                                           |
|                                                                              |

## Section 5. Diagnostic testing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 21%" />
<col style="width: 19%" />
<col style="width: 14%" />
<col style="width: 17%" />
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
<td><strong><u>5. Diagnostic testing</u></strong></td>
<td>Disabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Determination of cardiac hypertrophy/dilatation is required; the suggested order of testing for cardiac hypertrophy/dilatation is EKG, then chest x-ray (PA and lateral), then echocardiogram. Echocardiogram is only necessary if the other two tests are negative. A limited echocardiogram, if available, is appropriate to determine if cardiac hypertrophy/dilatation is present by measuring only left ventricular dimension, wall thickness and ejection fraction.</td>
<td>Disabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Is there evidence of cardiac hypertrophy or dilatation?</td>
<td><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled, Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Is there evidence of cardiac hypertrophy or dilatation?</td>
</tr>
<tr class="even">
<td>Diagnostic test (provide most recent test only)</td>
<td><p>If previous question = Yes, Enabled, Mandatory, Choose one or more valid value</p>
<p>Else; Enabled, Optional</p></td>
<td><p>[EKG; Chest x-ray; Echocardiogram;</p>
<p>Other study (specify)]</p></td>
<td>N/A</td>
<td>Please check one or more boxes to specify the diagnostic test(s) performed.</td>
</tr>
<tr class="odd">
<td>Date of EKG</td>
<td><p>If <em>EKG = Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the most recent EKG.</td>
</tr>
<tr class="even">
<td>Date of CXR:</td>
<td><p>If <em>Chest x-ray</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the most recent CXR.</td>
</tr>
<tr class="odd">
<td>Date of echocardiogram:</td>
<td><p>If <em>echocardiogram</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the most recent echocardiogram.</td>
</tr>
<tr class="even">
<td>Name of other diagnostic test study</td>
<td><p>If <em>Other study</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please specify the name of the other diagnostic test study.</td>
</tr>
<tr class="odd">
<td>Date of other study:</td>
<td><p>If <em>Other study</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the most recent other study.</td>
</tr>
<tr class="even">
<td>Left ventricular ejection fraction (LVEF), if known:</td>
<td>Enabled<em>,</em> Optional</td>
<td>N/A</td>
<td>Free Text %</td>
<td>N/A</td>
</tr>
<tr class="odd">
<td>Date of test:</td>
<td><p>If <em>LVEF is populated</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Enabled, Optional</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please enter the date of the LVEF test.</td>
</tr>
<tr class="even">
<td><em>If LVEF testing is not of record, but available medical information sufficiently reflects the severity of the Veteran’s cardiovascular condition, LVEF testing is not required.</em></td>
<td>Disabled, Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
</tbody>
</table>

<span id="_Toc270513073" class="anchor"></span>

Figure 13: Template Example: DBQ – IHD – 5. Diagnostic testing

> ![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/009.png)

<span id="_Toc286754164" class="anchor"></span>Figure 14: Print Example: DBQ – IHD – 5. Diagnostic testing

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>5. Diagnostic testing</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>---------------------</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Determination of cardiac hypertrophy/dilatation is required; the suggested</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>order of testing for cardiac hypertrophy/dilatation is EKG, then chest x-</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>ray (PA and lateral), then echocardiogram. Echocardiogram is only necessary</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>if the other two tests are negative. A limited echocardiogram, if</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>available, is appropriate to determine if cardiac hypertrophy/dilatation is</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>present by measuring only left ventricular dimension, wall thickness and</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>ejection fraction.</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Is there evidence of cardiac hypertrophy or dilatation?</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>[X] Yes [ ] No</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Diagnostic test (provide most recent test only):</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>[X] EKG Date of EKG: EKG Date will be here</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>[X] Chest x-ray Date of CXR: CXR Date will be here</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>[X] Echocardiogram Date of echocardiogram: Echo Date will be here</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>[X] Other study (specify): Other study will be here</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Date:Other Date will be here</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Left ventricular ejection fraction (LVEF), if known: LVEF will be here %</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Date of test: Date will be here</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>If LVEF testing is not of record, but available medical information</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>sufficiently reflects the severity of the Veteran's cardiovascular</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>condition, LVEF testing is not required.</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>

## Section 6. Functional impact

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below. If all mandatory questions are not answered, the error message(s) will appear in a popup window as depicted below.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
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
<td><strong><u>6. Functional impact</u></strong></td>
<td>Disabled; Read-Only</td>
<td>N/A</td>
<td>N/A</td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Does the Veteran’s ischemic heart disease impact his or her ability to work?</td>
<td><p>If <em>diagnosis</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory, Choose one valid value</p>
<p>Else; Enabled<em>,</em> Optional</p></td>
<td>[Yes; No]</td>
<td>N/A</td>
<td>Please provide an answer to the question: Does the Veteran’s ischemic heart disease impact his or her ability to work?</td>
</tr>
<tr class="odd">
<td>If yes, describe impact, providing one or more examples:</td>
<td><p>If <em>Does the Veteran’s ischemic heart disease impact his or her ability to work</em> = <em>Yes</em>; Enabled<em>,</em> Mandatory</p>
<p>Else; Disabled</p></td>
<td>N/A</td>
<td>Free Text</td>
<td>Please describe the impact of IHD on the Veteran's ability to work, providing one or more examples.</td>
</tr>
</tbody>
</table>

<span id="_Toc270513076" class="anchor"></span>Figure 15: Template Example: DBQ – IHD – 6. Functional impact

> ![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/010.png)

<span id="_Toc270513077" class="anchor"></span>Figure 16: Print Example: DBQ – IHD – 6. Functional impact

|                                                                                  |
|----------------------------------------------------------------------------------|
| 6. Functional impact                                                         |
| --------------------                                                         |
|                                                                                  |
| Does the Veteran's ischemic heart disease impact his or her ability to work? |
| \[X\] Yes \[ \] No                                                           |
| If yes, describe impact, providing one or more examples: Impact and examples |
| will be entered here                                                         |
|                                                                                  |

## ## Section 7. Remarks, if any

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All questions in this section may be answered as described by the rules below.

| Field/Question            | Field Disposition | Valid Values | Format | Error Message |
|-------------------------------|-----------------------|------------------|------------|-------------------|
| <u>7. Remarks, if any</u> | Enabled*,* Optional   | N/A              | Free Text  | N/A               |

<span id="_Toc270513079" class="anchor"></span>Figure 17: Template Example: DBQ – IHD – 7. Remarks, if any

> ![](dvba-2-7-161-workflow-dbq-ischemic-heart-disease/011.png)

<span id="_Toc270513080" class="anchor"></span>Figure 18: Print Example: DBQ – IHD – 7. Remarks, if any

| 7. Remarks, if any           |
|----------------------------------|
| ------------------           |
| Remarks will be entered here |
|                                  |

# IHD AMIE-DBQ Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The AMIE-DBQ worksheets are accessed via the \[DVBA C PRINT BLANK C&P WORKSHE\] Print Blank C&P Worksheet DBQ-Ischemic Heart Disease menu option.

> Disability Benefits Questionnaire

> Ischemic Heart Disease (IHD)

> Name of patient/Veteran: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ SSN: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Your patient is applying to the U. S. Department of Veterans Affairs

> (VA) for disability benefits. VA will use the information you provide on

> this questionnaire to process the Veteran's claim.

> 1\. Diagnosis

> NOTE: IHD includes, but is not limited to, acute, subacute, and old

> myocardial infarction; atherosclerotic cardiovascular disease including

> coronary artery disease (including coronary spasm) and coronary bypass

> surgery; and stable, unstable and Prinzmetal's angina. IHD does not include

> hypertension or peripheral manifestations of arteriosclerosis such as

> peripheral vascular disease or stroke, or any other condition that does not

> qualify within the generally accepted medical definition of ischemic heart

> disease.

> IHD encompasses any atherosclerotic heart disease resulting in clinically

> significant ischemia or requiring coronary revascularization.

> Does the Veteran have ischemic heart disease (IHD)? \_\_\_ Yes \_\_\_ No

> NOTE: Provide only diagnoses that pertain to IHD.

> Diagnosis \#1: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Date of diagnosis \#1: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Diagnosis \#2: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Date of diagnosis \#2: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Diagnosis \#3: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> ICD code: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Date of diagnosis \#3: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> If additional diagnoses that pertain to IHD, list using above format:

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Page: 2

> Disability Benefits Questionnaire for

> Ischemic Heart Disease (IHD)

> 2\. Medical history

> Does the Veteran's treatment plan include taking continuous medication for

> the diagnosed condition? \_\_\_ Yes \_\_\_ No

> List medications: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Is there a history of:

> Percutaneous coronary intervention (PCI) \_\_\_ Yes \_\_\_ No

> Treatment facility/date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Myocardial infarction \_\_\_ Yes \_\_\_ No

> Treatment facility/date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Coronary bypass surgery \_\_\_ Yes \_\_\_ No

> Treatment facility/date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Heart transplant \_\_\_ Yes \_\_\_ No

> Treatment facility/date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> If yes, is it as likely as not that the Veteran's heart transplant is

> due to IHD? \_\_\_ Yes \_\_\_ No

> Implanted cardiac pacemaker \_\_\_ Yes \_\_\_ No

> Treatment facility/date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> If yes, is it as likely as not that the Veteran's pacemaker is due to

> IHD? \_\_\_ Yes \_\_\_ No

> Implanted automatic implantable cardioverter defibrillator (AICD)

> \_\_\_ Yes \_\_\_ No

> Treatment facility/date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> If yes, is it as likely as not that the Veteran's AICD is due to IHD?

> \_\_\_ Yes \_\_\_ No

> 3\. Congestive heart failure (CHF)

> Does the Veteran have CHF? \_\_\_ Yes \_\_\_ No

> Is the Veteran's CHF chronic? \_\_\_ Yes \_\_\_ No

> If the Veteran's CHF is not chronic, has the Veteran had more than one

> episode of acute CHF in the past year? \_\_\_ Yes \_\_\_ No

> Treatment facility/date of most recent episode of CHF: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Page: 3

> Disability Benefits Questionnaire for

> Ischemic Heart Disease (IHD)

> 4\. Cardiac functional assessment

> Has a diagnostic exercise test been conducted? \_\_\_ Yes \_\_\_ No

> a\. If yes, provide level of METs the Veteran can perform as shown by the

> most recent diagnostic exercise testing: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Date of most recent diagnostic exercise test:\_\_\_\_\_\_\_\_\_\_\_

> b\. If exercise METs testing was not completed because it is not required as

> part of Veteran's treatment plan, complete the following METs test based on

> the Veteran's responses:

> Lowest level of activity at which the Veteran reports symptoms (check all

> symptoms that apply)

> \_\_\_ dyspnea \_\_\_ fatigue \_\_\_ angina \_\_\_ dizziness \_\_\_ syncope

> \_\_\_ (1-3 METs) This METs level has been found to be consistent with

> activities such as eating, dressing, taking a shower,

> slow walking (2 mph) for 1-2 blocks

> \_\_\_ (\>3-5 METs) This METs level has been found to be consistent with

> activities such as light yard work (weeding), mowing lawn

> (power mower), brisk walking (4 mph)

> \_\_\_ (\>5-7 METs) This METs level has been found to be consistent with

> activities such as golfing (without cart), mowing lawn

> (push mower), heavy yard work (digging)

> \_\_\_ (\>7-10 METs) This METs level has been found to be consistent with

> activities such as climbing stairs quickly, moderate

> bicycling, sawing wood, jogging (6 mph)

> \_\_\_ The Veteran denies experiencing above symptoms with any level of

> physical activity

> Page: 4

> Disability Benefits Questionnaire for

> Ischemic Heart Disease (IHD)

> 5\. Diagnostic testing

> Determination of cardiac hypertrophy/dilatation is required; the suggested

> order of testing for cardiac hypertrophy/dilatation is EKG, then chest

> x-ray (PA and lateral), then echocardiogram. Echocardiogram is only

> necessary if the other two tests are negative. A limited echocardiogram, if

> available, is appropriate to determine if cardiac hypertrophy/dilatation is

> present by measuring only left ventricular dimension, wall thickness and

> ejection fraction.

> Is there evidence of cardiac hypertrophy or dilatation?

> \_\_\_ Yes \_\_\_ No

> Diagnostic test (provide most recent test only):

> \_\_\_ EKG Date of EKG: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

> \_\_\_ Chest x-ray Date of CXR: \_\_\_\_\_\_\_\_\_\_\_\_\_\_

> \_\_\_ Echocardiogram Date of echocardiogram:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> \_\_\_ Other study (specify): \_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Left ventricular ejection fraction (LVEF), if known: \_\_\_\_\_\_%

> Date of test: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> If LVEF testing is not of record, but available medical information

> sufficiently reflects the severity of the Veteran's cardiovascular condition,

> LVEF testing is not required.

> 6\. Functional impact

> Does the Veteran's ischemic heart disease impact his or her ability to work?

> \_\_\_ Yes \_\_\_ No

> If yes, describe impact, providing one or more examples: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Page: 5

> Disability Benefits Questionnaire for

> Ischemic Heart Disease (IHD)

> 7\. Remarks, if any

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Physician signature: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Date:\_\_\_\_\_\_\_\_\_\_

> Physician printed name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ Phone:\_\_\_\_\_\_\_\_\_

> Medical license \#: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Physician address: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> NOTE: VA may request additional medical information, including additional

> examinations if necessary to complete VA's review of the Veteran's

> application.