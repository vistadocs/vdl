---
title: PSU*4*19 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: null
app_code: PSU
app_name: 'Pharmacy: Benefits Management'
section: CLI
app_status: active
pkg_ns: PSU
patch_ver: 4
patch_id: PSU*4*19
group_key: PSU:PSU:4
file_numbers:
- '80'
- '900001'
security_keys: []
menu_options: 0
description: '- Introduction - Purpose - Background - Scope of Changes - Documentation - New Outpatient Visits Statistics Data Element - [Modified Inpatient Patient Treatment File...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 1055
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: July 2014
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/icd-10_rn_psu_4_19.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Benefits_Mgmnt_(PBM)/icd-10_rn_psu_4_19.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=91
audit_applied: '2026-05-31'
master_source: PSU*4*19 Release Notes
master_pub_date: July 2014
consolidated_from: 2 versions
prior_versions:
- PSU*4*5 Release Notes (Demographics Enhancements)
consolidated_title: release notes
---

ICD-10 Follow On Class 1 Software Remediation Project

Pharmacy: Benefits Management

Release Notes

PSU\*4\*19

![](psu-4-19-release-notes/001.png)

July 2014

Office of Information and Technology

Product Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Background](#background)
  - [Scope of Changes](#scope-of-changes)
  - [Documentation](#documentation)
- [New Outpatient Visits Statistics Data Element](#new-outpatient-visits-statistics-data-element)
- [Modified Inpatient Patient Treatment File (PTF) Data Element](#modified-inpatient-patient-treatment-file-ptf-data-element)
- [Technical Information](#technical-information)
  - [New API/Integration Control Registration (ICR \#5747)](#new-apiintegration-control-registration-icr-5747)
  - [MailMan Messages](#mailman-messages)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of these Release Notes is to identify enhancements to the Pharmacy Benefits Management (PBM) package contained in patch PSU\*4\*19.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On January 16, 2009, the Centers for Medicare & Medicaid Services (CMS) released a final rule for replacing the 30-year-old International Classification of Diseases, Ninth Revision, Clinical Modification (ICD-9-CM) code set with International Classification of Diseases, Tenth Revision, Clinical Modification (ICD-10-CM) and International Classification of Diseases, Tenth Revision, Procedure Coding System (ICD-10-PCS) with dates of service, or dates of discharge for inpatients, that occur on or after the ICD-10 Activation Date.

The classification system consists of more than 68,000 codes, compared to approximately 13,000 ICD-9-CM codes. There are nearly 87,000 ICD-10-PCS codes, while ICD-9-CM has nearly 3,800 procedure codes. Both systems also expand the number of characters allotted from five and four respectively to seven alpha-numeric characters. This value does not include the decimal point, which follows the third character for the ICD-10-CM code set. There is no decimal point in the ICD-10-PCS code set. These code sets have the potential to reveal more about quality of care, so that data can be used in a more meaningful way to better understand complications, better design clinically robust algorithms, and better track the outcomes of care. ICD-10-CM also incorporates greater specificity and clinical detail to provide information for clinical decision making and outcomes research.

ICD-9-CM and ICD-10-CM Comparison

| ICD-9-CM                                 | ICD-10-CM                                                                     |
|------------------------------------------|-------------------------------------------------------------------------------|
| 13,000 codes (approximately)             | 68,000 codes (approximately)                                                  |
| 3-5 characters                           | 3-7 characters (not including the decimal)                                    |
| Character 1 is numeric or alpha (E or V) | Character 1 is alpha; character 2 is numeric                                  |
| Characters 2 - 5 are numeric             | Characters 3–7 are alpha or numeric (alpha characters are not case sensitive) |
| Decimal after first 3 characters         | Same                                                                          |

ICD-9-CM and ICD-10-PCS Comparison

| ICD-9-CM Procedure Codes         | ICD-10-PCS                                                                                                                            |
|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| 3-4 characters                   | 7 alphanumeric characters                                                                                                             |
| All characters are numeric       | Characters can be either alpha or numeric. Letters O and I are not used to avoid confusion with the numbers 0 and 1                   |
| All characters are numeric       | Each character can be any of 34 possible values. The ten digits 0-9 and the 24 letters A-H, J-N and P-Z may be used in each character |
| Decimal after first 2 characters | Does not contain decimals                                                                                                             |

## Scope of Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Existing ICD-9 functionality has not changed.

Patch PSU\*4\*19 makes the following changes to the Pharmacy Benefits Management application:

- Adds a new Code Set Indicator data element to the PBM National Database.
- Modifies routines that extract ICD code data for inpatient and outpatient activity. These routines have been modified to use new Lexicon utilities that replace old Lexicon utilities and direct ICD global reads.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy Benefits Management manuals are posted on the VistA Documentation Library (VDL) (<http://www.va.gov/vdl/application.asp?appid=91>).

The following Pharmacy Benefits Management user manuals are updated with changes for PSU\*4\*19:

- User Manual (V. 4.0)
- Technical Manual/Security Guide (V. 4.0)

> **NOTE:** Security Information is contained within the *PBM Technical Manual/Security Guide*.

The following manual exists, but is not updated for this release:

- Installation Guide (V. 4.0)

# New Outpatient Visits Statistics Data Element

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new data element, "Code Set Indicator," has been added to the data extract. The data element is sent via MailMan to the PBM National Database. Code Set Indicator values include:

- 9 (contains ICD-9 codes only)
- 10 (contains ICD-10 codes only)
- U (contains ICD-9 and ICD-10 codes)
- "" (Null – contains no ICD-9 or ICD-10 codes)

The File \# and Field \# data fields within the Outpatient Visits Specifications are not applicable (N/A), as the new data element is called by a new API.

New Data Element within Outpatient Visits Statistics Data Field Specifications

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Element</th>
<th>File #</th>
<th>Field #</th>
<th>Piece # In Record Sent</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Code Set Indicator</p>
<p>(New)</p></td>
<td>N/A</td>
<td>N/A</td>
<td>27</td>
<td>"9","10","U",""</td>
</tr>
</tbody>
</table>

# Modified Inpatient Patient Treatment File (PTF) Data Element

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The "ICD-9 Codes – Diagnosis" data element has been renamed to "ICD Diagnosis Codes." Input PTF Records and Outpatient Visit Statistics both indicate whether the ICD code is ICD-9 or ICD-10.

Modified Data Element within Inpatient PTF Record Statistics Data Field Specifications

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Data Element</th>
<th>File #</th>
<th>Field #</th>
<th>Piece # In Record Sent</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ICD Codes – Diagnosis (Modified from "ICD-9 Codes – Diagnosis")</td>
<td><p>V POV file (#9000010.07)<br />
&amp;<br />
V CPT file (#9000010.18)</p>
<p>ICD Diagnosis file (#80)</p></td>
<td>POV field (#.01)<br />
<br />
&amp;<br />
DIAGNOSIS field (#.05)</td>
<td>7-16</td>
<td><p>Diagnosis data is pulled from the POV field (#.01) in the V POV file (#9000010.07) and from the DIAGNOSIS field (#.05) in the V CPT file (#9000010.18).</p>
<p>Number of codes is limited to 10. If over 10, they will be truncated.</p></td>
</tr>
</tbody>
</table>

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new API has been added, and the MailMan message format has been updated to accommodate ICD-10 codes and the new API.

## New API/Integration Control Registration (ICR \#5747)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new API, \$\$CSI^ICDEX(), has been added to transmit the new Code Set Indicator data element. The Code Set Indicator provides both Inpatient and Outpatient ICD-9 and ICD-10 code set statistics.

## MailMan Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following MailMan messages have been updated to include a record for the new Code Set Indicator data element:

- Outpatient Visits – Detail Report Message
- Inpatient PTF Records – Detail Report Message

Modified Outpatient Visits – Detail Report Message

Subj: V. 4.0 PBMOV 29806 1/1 0 \[#33424\] 03/02/12@11:42 23 lines

From: LASTNAME, FIRSTNAME In 'IN' basket. Page 1

-----------------------------------------------------------------------------

^0^O^3001016^xxxxxxxxx^5000000019V796730^800.00^^^^^^^^^^^^^^^^^^^^9

^0^O^3000101^xxxxxxxxx^5000000000V196703^291.9^^^^^^^^^^32160^^^^^^^^^^9

^0^O^3000101^xxxxxxxxx^5000000019V796730^800.00^^^^^^^^^^32100^^^^^^^^^^9

^0^I^3010604^xxxxxxxxx^5000000003V639492^800.00^^^^^^^^^^20924^^^^^^^^^^9

^0^O^3010606^xxxxxxxxx^^144.1^^^^^^^^^^00100^^^^^^^^^^9

^0^O^3010606^xxxxxxxxx^^850.1^^^^^^^^^^85002^^^^^^^^^^9

Modified Inpatient PTF Records – Detail Report Message

Subj: V. 4.0 PBMPTF 29806 1/1 0 \[#33425\] 03/02/12@11:42 6 lines

From: LASTNAME, FIRSTNAME In 'IN' basket. Page 1

-----------------------------------------------------------------------------

^0^04^3020802^3030113^xxxxxxxxx^5000000001V324625^E955.6^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^9

^0^06^3020830^3031006^xxxxxxxxx^5000000042V640365^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

^0^08^3040421^3061026^xxxxxxxxx^5000000001V324625^295.01^295.02^295.10^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^9

^0^014^3120227^3120227^xxxxxxxxx^5000000008V200916^K71.51^A20.7^Q27.8^V70.2XXD^^^^^^^^^^^^^^^^^0016070^0016378^^^^^^^^^^^^^^^10

*(This page included for two-sided copying.)*

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSU*4*5 Release Notes (Demographics Enhancements)

## PSJ\*5\*161, PSO\*7\*170, PSU\*4\*5, DG\*5.3\*671, PSS\*1\*99 May 2009

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Office of Enterprise Development

TABLE OF CONTENTS

> May 2009 Pharmacy Enhancements to Support Pharmacy Benefits Management Release Notes i PSJ\*5\*161, PSO\*7\*170, PSU\*4\*5, DG\*5.3\*671, PSS\*1\*99

*(This page included for two-sided copying.)*

> ii Pharmacy Enhancements to Support Pharmacy Benefits Management Release Notes May 2009 PSJ\*5\*161, PSO\*7\*170, PSU\*4\*5, DG\*5.3\*671, PSS\*1\*99

### WARNING: If your facility has the Pyxis/Omnicell/McKesson interface from ILC, this patch will overwrite any "local" modifications in routine PSGOETO. This could affect certain orders being sent across this interface. The modifications will have to be reintroduced following installation of this patch.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
