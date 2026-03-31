---
title: LR*5.2*421 Laboratory EPI Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Laboratory EPI
app_code: EPI
app_name: "Laboratory: Emerging Pathogens Initiative"
section: CLI
app_status: active
pkg_ns: LR
patch_ver: 5.2
patch_id: LR*5.2*421
group_key: "EPI:LR:5.2"
file_numbers: 
  - 69
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - table
  - class
  - contents
  - pathogen
  - colspan
  - protocol
  - fptf
  - active
  - lrepi
page_count: 0
word_count: 3310
section_count: 15
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/icd-10_rn_lr_5_2_421.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Emerging_Pathogens_Initiative/icd-10_rn_lr_5_2_421.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=118"
---

ICD-10 Follow On Class 1 Software RemediationLaboratory: Emerging Pathogens Initiative (EPI)Application Version 5.2Release NotesLR\*5.2\*421

![](lr-5-2-421-laboratory-epi-release-notes/001.png)

### July 2014

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Department of Veterans Affairs Office of Information and Technology Product Development
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [July 2014](#july-2014)
    - [Department of Veterans Affairs Office of Information and Technology Product Development](#department-of-veterans-affairs-office-of-information-and-technology-product-development)
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
  - [Documentation](#documentation)
- [Modified Screens](#modified-screens)
  - [Laboratory Search/Extract Parameters Input Screen](#laboratory-searchextract-parameters-input-screen)
  - [Enter/Edit Local Pathogens Menu Option](#enteredit-local-pathogens-menu-option)
  - [Pathogen Inquiry Screen](#pathogen-inquiry-screen)
- [Modified Reports](#modified-reports)
  - [PRT LAB EPI Print Local Report/Spreadsheet](#prt-lab-epi-print-local-reportspreadsheet)
  - [Detailed Verification Report](#detailed-verification-report)
  - [Report Transmission to Cincinnati Group](#report-transmission-to-cincinnati-group)
- [ICD-10 Searches](#icd-10-searches)
  - [ICD-10-CM Diagnosis Code Search](#icd-10-cm-diagnosis-code-search)
- [Technical Information](#technical-information)
  - [Routines](#routines)
  - [HL7 Messages](#hl7-messages)
  - [Online Help for ICD-10 Codes](#online-help-for-icd-10-codes)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The purpose of these Release Notes is to identify enhancements to the Emerging Pathogens Initiative (EPI) package contained in patch LR 5\*2\*421.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service or dates of discharge for inpatients that occur on or after the ICD-10 Activation Date.

#### The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9- CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

#### ICD-9-CM and ICD-10-CM Comparison

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ICD-9-CM</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ICD-10-CM</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>13,000 codes (approximately)</p>
</blockquote></td>
<td><blockquote>
<p>68,000 codes (approximately)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3-5 characters</p>
</blockquote></td>
<td><blockquote>
<p>3-7 characters (not including the decimal)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Character 1 is numeric or alpha (E or V)</p>
</blockquote></td>
<td><blockquote>
<p>Character 1 is alpha; character 2 is numeric</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Characters 2 - 5 are numeric</p>
</blockquote></td>
<td><blockquote>
<p>Characters 3–7 are alpha or numeric (alpha characters are not case sensitive)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Decimal after first 3 characters</p>
</blockquote></td>
<td><blockquote>
<p>Same</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### ICD-9-CM and ICD-10-PCS Comparison

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>ICD-9-CM Procedure Codes</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>ICD-10-PCS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3-4 characters</p>
</blockquote></td>
<td><blockquote>
<p>7 alphanumeric characters</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>All characters are numeric</p>
</blockquote></td>
<td><blockquote>
<p>Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>All characters are numeric</p>
</blockquote></td>
<td><blockquote>
<p>Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Decimal after first 2 characters</p>
</blockquote></td>
<td><blockquote>
<p>Does not contain decimals</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### NOTE: Existing ICD-9 functionality has not changed.

#### Patch LR\* 5.2\*421 makes the following changes to the Emerging Pathogens Initiative (EPI) application:

#### The following fields and screens have been updated to refer to “ICD” rather than “ICD9”:

#### Laboratory Search/Extract Parameters Input screens

#### Enter/Edit Local Pathogens screens

#### Detailed Verification Report

#### Help text

#### Within the Enter/Edit Local Pathogens and Laboratory Search/Extract Parameters Input screens, users are prompted to specify a code set on which to search prior to entering an ICD code. Based on this input, the system will only allow ICD-9 entry or ICD-10 entry.

#### The Pathogen Inquiry option has been modified to list both ICD-9 and ICD-10 codes.

#### The Generate Local Report/Spreadsheet option has been modified to include both the Diagnosis Code Set Designation and the Diagnosis Code.

#### HL7 Reports that are sent to AITC have been modified to include ICD-10 Codes and Descriptions, which are included in the DG1 HL7 Segments.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The EPI manuals are posted on the VistA Documentation Library (VDL) page: [<u>http://www.va.gov/vdl/application.asp?appid=118</u>.](http://www.va.gov/vdl/application.asp?appid=118)

#### The following EPI user manuals are updated with changes for LR 5\*2\*421:

#### Rollup Modifications Technical and User Manual

#### Technical and User Guide

#### Hepatitis C and EPI Technical and User Guide

#### Search/Extract Technical and User Guide The following manual does not exist for this package:

#### Security Guide

> NOTE: Security Information is contained within the *Search/Extract Technical and User Guide and Rollup Modifications Technical and User Manual*.

# Modified Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The following screens have been modified:

#### Laboratory Search/Extract Parameters Input

#### Enter/Edit Local Pathogens Menu Option

## Laboratory Search/Extract Parameters Input Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The following modifications have been made to the Laboratory Search/Extract Parameters Input Screen:

#### A new prompt “ICD Coding System \[ICD-9 or ICD-10\]? (9/10):” has been added so that users must specify an ICD-9 or ICD-10 code set on which to search.

#### A “CD Set” column header, which indicates the ICD code set (ICD-9 or ICD-10), has been added.

#### Two column headers have been modified so that they refer generically to “ICD” rather than indicate an ICD code set (ICD-9 or ICD-10):

#### ICD Code

#### ICD Description

#### Example of Updated Lab Search/Extract Parameters Input Screen

## Enter/Edit Local Pathogens Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Enter/Edit Local Pathogens screen has been modified from “ICD9” to “ICD DIAGNOSIS” and a “CODING SYSTEM:” field has been added to indicate whether the ICD Diagnosis is based on the ICD-9 and/or ICD-10 coding system.

#### Example of Updated Enter/Edit Local Pathogens Menu Screen

## Pathogen Inquiry Screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Pathogen Inquiry screen has been modified from “ICD9” to “ICD DIAGNOSIS” and a “CODING SYSTEM:” field has been added to indicate whether the ICD Diagnosis is based on the ICD-9 or ICD-10 coding system.

#### Example of Updated Pathogen Inquiry Screen

# Modified Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PRT LAB EPI Print Local Report/Spreadsheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### o The LAB EPI Local Report/Spreadsheet option has been modified so that they each include the Diagnosis Code Set Designation (ICD-9 or ICD-10) as a prefix to the Diagnosis Code.

#### o

#### Example of Updated PRT LAB EPI Print Local Report/Spreadsheet (On-Screen Report Display)

#### o

#### Example of Updated PRT LAB EPI Print Local Report/Spreadsheet (Spreadsheet Output)

## Detailed Verification Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The Detailed Verification Report of EPI Extracted Data has been modified so that the code set (ICD-9 or ICD-10) is not indicated. Rather, the description refers generically to an “ICD coded diagnosis.”

#### Example of Updated Detailed Verification Report of EPI Extracted Data

## Report Transmission to Cincinnati Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The VistA Laboratory Emerging Pathogens Initiative shall retain the ability to transmit diagnosis codes and ICD code set designation within the LREPISERVER Data Server triggered report option for the Cincinnati mail group [<span class="mark">REDACTED</span>.](mailto:G.EPI-SITE@CINCINNATI.VA.GOV)

#### Example of Cincinnati Report

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active HEPATITIS C ANTIBODY POS 2 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active PEN-RES PNEUMOCOCCUS 3 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active CLOSTRIDIUM DIFFICILE 4 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active TUBERCULOSIS 5 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active STREPTOCOCCUS GROUP A 6 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active LEGIONELLA 7 M 15 LREPI 1 0

> Lab Test Indicator Value

Etiology LEGIONELLA BOZEMANII LEGIONELLA DUMOFFII LEGIONELLA MICDADEI

LEGIONELLA PNEUMOPHILIA LEGIONELLA SP

> ICD

482.80 (ICD-9)

A48.1 (ICD-10)

A48.2 (ICD-10)

A48.8 (ICD-10)

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 42%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Pathogen CANDIDA</p>
<p>Lab Test</p>
<p>Etiology</p>
</blockquote></th>
<th><blockquote>
<p>Ref# Cy LD Protocol FPTF Active</p>
<p>8 M 15 LREPI 1 0</p>
</blockquote>
<p>Indicator</p></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>CANDIDA ALBICANS CANDIDA GUILLIERMONDII CANDIDA KRUSEI</p>
<p>CANDIDA PARAPSILOSIS CANDIDA PSEUDOTROPICALIS CANDIDA SKIN TEST ANTIGEN CANDIDA STELLATOIDEA CANDIDA TROPICALIS CANDIDA, NOS</p>
<p>ICD</p>
<p>Microbial Susceptibility Indicator Value</p>
<p>*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pathogen CRYPTOSPORIDIUM</p>
<p>Lab Test</p>
</blockquote></td>
<td><blockquote>
<p>Ref# Cy LD Protocol FPTF Active</p>
<p>9 M 15 LREPI 1 0</p>
</blockquote>
<p>Indicator</p></td>
<td><blockquote>
<p>Value</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### July 2014 ICD-10 Follow On Class 1 Software Remediation Release Notes 7

#### LR\*5.2\*421

> Etiology ICD

007.8 (ICD-9)

A07.2 (ICD-10)

A07.9 (ICD-10)

IEN \# 9 damaged. (No ICD)

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

E. COLI 0157:H7 10 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 23%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Pathogen MALARIA</p>
<p>Lab Test Etiology</p>
<p>ICD</p>
</blockquote></th>
<th><blockquote>
<p>Ref# Cy LD 11 M 15</p>
</blockquote></th>
<th><blockquote>
<p>Protocol FPTF Active LREPI 1 0</p>
<p>Indicator</p>
</blockquote></th>
<th><blockquote>
<p>Value</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>084.0</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>084.1</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>084.2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>084.3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>084.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>084.5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>084.6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>084.7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>084.8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>084.9</p>
<p>B50.0 B50.8 B50.9 B51.0 B51.8 B51.9 B52.0 B52.8 B52.9 B53.0 B53.1 B53.8 B54.</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
</blockquote>
<p>Microbial Susceptibility</p></td>
<td colspan="2"><blockquote>
<p>Indicator</p>
</blockquote></td>
<td><blockquote>
<p>Value</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*= Pathogen Ref# Cy LD Protocol FPTF Active</p>
<p>DENGUE 12 M 15 LREPI 1 0</p>
<p>Lab Test Indicator</p>
<p>Etiology</p>
</blockquote></td>
<td><blockquote>
<p>Value</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>ICD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>065.4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
<td colspan="2"></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>061. A90. A91. A93.8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>(ICD-9)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
<p>(ICD-10)</p>
</blockquote>
<p>Microbial Susceptibility</p></td>
<td colspan="2"><blockquote>
<p>Indicator</p>
</blockquote></td>
<td><blockquote>
<p>Value</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*= Pathogen Ref# Cy LD Protocol FPTF Active CREUTZFELDT-JAKOB DISEASE 13 M 15 LREPI 1 0</p>
<p>Lab Test Indicator</p>
<p>Etiology</p>
</blockquote></td>
<td><blockquote>
<p>Value</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>ICD</p>
<p>046.1 (ICD-9)</p>
<p>A81.00 (ICD-10)</p>
<p>A81.01 (ICD-10)</p>
<p>A81.09 (ICD-10)</p>
<p>A81.1 (ICD-10)</p>
<p>A81.2 (ICD-10)</p>
<p>A81.81 (ICD-10)</p>
<p>A81.82 (ICD-10)</p>
<p>A81.83 (ICD-10)</p>
<p>A81.89 (ICD-10)</p>
</blockquote></td>
<td colspan="4"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td></td>
<td colspan="4"><blockquote>
<p>ICD-10 Follow On Class 1 Software Remediation Release Notes July 2014</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="4"><blockquote>
<p>LR* 5.2*421</p>
</blockquote></td>
</tr>
</tbody>
</table>

A81.9 (ICD-10)

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

LEISHMANIASIS 14 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

085.0 (ICD-9)

085.1 (ICD-9)

085.2 (ICD-9)

085.3 (ICD-9)

085.4 (ICD-9)

085.5 (ICD-9)

085.9 (ICD-9)

B55.0 (ICD-10)

B55.1 (ICD-10)

B55.2 (ICD-10)

B55.9 (ICD-10)

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active HEPATITIS C ANTIBODY NEG 15 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active HEPATITIS A ANTIBODY POS 16 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

HEPATITIS B POS 17 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active VANC-RES COAG NEG STAPH 21 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology

STAPHYLOCOCCUS (COAGULASE NEGATIVE) STAPHYLOCOCCUS EPIDERMIDIS STAPHYLOCOCCUS HAEMOLYTICUS STAPHYLOCOCCUS SAPROPHYTICUS STAPHYLOCOCCUS SALIVARIUS STAPHYLOCOCCUS SIMULANS

0

> ICD

> Microbial Susceptibility Indicator Value

> VANCMCN Unknown

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

ALL STREP PNEUMO 22 M 15 LREPI 1 0

> Lab Test Indicator Value

Etiology STREPTOCOCCUS PNEUMONIAE

> ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

ALL ENTEROCOCCI 23 M 15 LREPI 1 0

> Lab Test Indicator Value

> Etiology

0

0

ENTEROCOCCUS (STREPT. FAECALIS-GROUP D)

#### July 2014 ICD-10 Follow On Class 1 Software Remediation Release Notes 9

#### LR\*5.2\*421

STREPTOCOCCUS FAECALIS STREPTOCOCCUS FAECIUM

> ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

METH-RES STAPH AUREUS 19 M 15 LREPI 1 0

> Lab Test Indicator Value

Etiology STAPHYLOCOCCUS AUREUS

> ICD

> Microbial Susceptibility Indicator Value

> OXACILLIN Unknown

> NAFCILLIN Unknown

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

ALL STAPH AUREUS 18 M 15 LREPI 1 0

> Lab Test Indicator Value

Etiology STAPHYLOCOCCUS AUREUS

> ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

VANC-RES STAPH AUREUS 20 M 15 LREPI 1 0

> Lab Test Indicator Value

Etiology STAPHYLOCOCCUS AUREUS

> ICD

> Microbial Susceptibility Indicator Value

> VANCMCN Unknown

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

ADD THIS ONE!10 100 LREPI 0

> Lab Test Indicator Value

> Etiology ICD

500\. (ICD-9)

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

NEWEXAMPLE10 101 LREPI 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

EXAMPLEPATHOGEN10 102 LREPI 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

EXAMPLEPATHOGEN01010 103 LREPI 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

ADD ANOTHER10 104 LREPI 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

LEG10 105 LREPI 0

> Lab Test Indicator Value

> Etiology

> ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

EXAMPLEPATHOGEN1010 106 LREPI 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

ADD SOME TEXT 999 D 1 LREPI 0

> Lab Test Indicator Value

25 OH VITAMIN D Contains 0

> Etiology

1(1-NAPHTHYL)-2-THIOUREA ICD

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 31%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>100.0</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>(ICD-9)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>800.04</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>200.01</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>250.00</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>(ICD-9)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>F17.203</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>(ICD-10)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Microbial Susceptibility</p>
<p>AMIKACN</p>
</blockquote></td>
<td><blockquote>
<p>Indicator</p>
<p>Unknown</p>
</blockquote></td>
<td><blockquote>
<p>Value</p>
</blockquote></td>
</tr>
</tbody>
</table>

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active IEN \# 108 damaged. (No Protocol)

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active IEN \# 109 damaged. (No Protocol)

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active IEN \# 110 damaged. (No Protocol)

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

TESTROB10 111 LREPI 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*=\*= Pathogen Ref# Cy LD Protocol FPTF Active

ADD SOME TEXT10 112 LREPI 0

> Lab Test Indicator Value

> Etiology ICD

> Microbial Susceptibility Indicator Value

# ICD-10 Searches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The EPI package provides the ability to search on ICD-10-CM diagnosis codes.

#### NOTE: Existing ICD-9 functionality has not changed.

## ICD-10-CM Diagnosis Code Search

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The EPI ICD-10 diagnosis code search functionality allows the end user to select a single, valid ICD-10 diagnosis code and also display its coding system and description. The EPI user interface prompts the user for input, invokes the Lexicon utility to get data, and then presents that data to the end user.

#### ICD-10-CM diagnosis code search highlights include:

#### Text-based search using one or more words as search terms, finding matches based on full descriptions, synonyms, key words, and shortcuts associated with ICD-10-CM diagnosis codes, which are inherently built into the Lexicon coding system.

#### The more refined the search criteria used (i.e., the more descriptive the search terms), the more streamlined the process of selecting the correct valid ICD-10 diagnosis code will be.

#### Short descriptions for the valid ICD-10-CM codes display.

#### Partial code searches are also possible, as is full ICD-10-CM code entry, for situations where all or part of the code is known.

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Some EPI routines were modified to replace direct global reads and old APIs with new Standards and Terminology Services (STS) APIs and Lexicon APIs wherever possible. The following new routines are added:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Routine Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Function</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>LR421P</p>
</blockquote></td>
<td><blockquote>
<p>ICD-10 Post Install Routine. (Populates new ICD-10 coding system fields for current records in the EPI Extract File (File # 69.5).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LREPICD</p>
</blockquote></td>
<td><blockquote>
<p>ICD-10 determines coding system (9 or 10) for extract parameter.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LREPIXDG</p>
</blockquote></td>
<td><blockquote>
<p>Called to pull in ICD Description and Code Set information for Enter/Edit Local Pathogens and Lab EPI Parameter Setup screens.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## HL7 Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The DG1segment of HL7 Messages has been updated to include an ICD-9 or ICD-10 code set indicator.

#### Example: HL7 MailMan Message

## Online Help for ICD-10 Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Help text (?) and extended help text (??) is included for prompts related to ICD-10 codes. Example: Help Text with 1 and 2 Question Marks (? and ??)