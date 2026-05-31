---
title: Surgery Version 3 User Manual (Updated SR*3*184)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: (Updated SR*3*184)
app_code: SR
app_name: MailMan
section: CLI
app_status: archive
pkg_ns: SR
patch_ver: 3
patch_id: SR*3
group_key: SR:SR:3
file_numbers:
- '17'
- '139.2'
security_keys:
- PROVIDER
- SR CODER
- SR RISK ASSESSMENT
- SRCOORD
- SROAMIS
- SROANES
- SROCOMP
- SROPER
- SROREP
- SROREQ
- SROSCH
- SROWAIT
menu_options: 1
description: '> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the...'
audience: End users (clinical / administrative, per package)
keywords: []
page_count: 0
word_count: 73339
section_count: 133
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: July 1993
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_um_r1115.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Surgery_Archive/sr_3_um_r1115.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=403
audit_applied: '2026-05-31'
master_source: Surgery Version 3 User Manual (Updated SR*3*184)
master_pub_date: July 1993
consolidated_from: 3 versions
prior_versions:
- Surgery User Manual (SR*3.0*200)
- Surgery User Manual (SR*3.0*205)
consolidated_title: surgery user manual
---

#### ![](surgery-version-3-user-manual-updated-sr-3-184/001.png)

SURGERY

> USER MANUAL

> Version 3.0

> July 1993

#### (Revised November 2015)

> Department of Veterans Affairs Product Development

> Revision History

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists "All," replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>11/15</p>
</blockquote></td>
<td><blockquote>
<p>i-viii, 9, 30, 32-33, 37,</p>
<p>38, 40-41, 42, 43, 44,</p>
<p>46, 47-48, 50-52, 65,</p>
<p>67-68, 72-73, 76-77,</p>
<p>79-80, 95, 98-99, 101-</p>
<p>102a, 105, 108-110</p>
<p>111-113, 117, 118, 123,</p>
<p>124, 124a, 124b, 140-</p>
<p>147, 150-152b, 212e,</p>
<p>219a, 219b, 432-433,</p>
<p>449-451, 458, 459, 465,</p>
<p>467-469, 470a-472,</p>
<p>473, 479-479a, 481-</p>
<p>482a, 484, 486-486c,</p>
<p>489, 491, 493, 495-499,</p>
<p>501, 502a, 502c, 502e,</p>
<p>502g, 507, 510, 512,</p>
<p>527-556</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*184</p>
</blockquote></td>
<td><blockquote>
<p>Updated definitions, added new data fields, made changes to data entry screens, reports, surgery risk management assessment transmissions. For more details, see the Annual Surgery Updates – VASQIP 2015, Release Notes.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>09/14</p>
</blockquote></td>
<td><blockquote>
<p>i, ia, iii-vii, 6-9, 11, 13,</p>
<p>14, 28, 31-33, 37, 38,</p>
<p>40-44, 46-48, 50-52, 59,</p>
<p>64, 66-68, 72-73, 76,</p>
<p>77, 79-83, 99-105, 107-</p>
<p>111, 114, 116, 117,</p>
<p>119-120a, 122-124a,</p>
<p>131, 140, 140a, 142-</p>
<p>147, 149, 151-152a,</p>
<p>165, 180, 180a, 189-</p>
<p>191, 218-219a, 285,</p>
<p>346, 349, 358, 360,</p>
<p>394a, 394b, 426-428,</p>
<p>449, 449a, 455-458,</p>
<p>467, 468, <a href="#cardiac-procedures-operative-data-enteredit">473</a>-474b,</p>
<p>482-484, 507, 510, 512,</p>
<p>519, 549, 549a, 551-</p>
<p>556</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*182</p>
</blockquote></td>
<td><blockquote>
<p>Updated definitions, added new data fields, made changes to data entry screens, reports, surgery risk management assessment transmissions. For more details, see the Annual Surgery Updates – VASQIP 2014, Release Notes.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### November 2015 Surgery V. 3.0 User Manual i

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>07/14</p>
</blockquote></td>
<td><blockquote>
<p>i-iib, 212a, 212d-212g, 238, 273, 405, 437, 480,</p>
<p>525, 526</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*177</p>
</blockquote></td>
<td><blockquote>
<p>Updated examples to reflect ICD-10 Diagnosis Codes. Changed File Download Option 2 from "ICD9" to "ICD."</p>
<p>Made ICD-9 references generic to ICD. Added ICD-10-CM Diagnosis Code Search. Updated Warning Message to Surgeon.</p>
<p>Updated MailMan Messages for ICD-9 and ICD-10 codes.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/12</p>
</blockquote></td>
<td><blockquote>
<p>i-iid, v, vii, <a href="#_bookmark8">6-11,</a> <a href="#_bookmark41">81-83,</a></p>
<p>120, 120a-120b, <a href="#_bookmark69">140</a>,</p>
<p><a href="#_bookmark70">144-145, 145a-145b,</a></p>
<p><a href="#_bookmark71">146,</a> <a href="#_bookmark72">151-152, 152a</a>,</p>
<p><a href="#_bookmark90">178,</a> <a href="#_bookmark104">207-209,</a> <a href="#_bookmark107">212c,</a></p>
<p><a href="#_bookmark107">212f,</a> <a href="#_bookmark109">213, 215, 217</a>-</p>
<p><a href="#_bookmark111">219, 219a-219b,</a> <a href="#_bookmark114">220,</a></p>
<p><a href="#_bookmark114">222, 224, 226, 228, 230,</a></p>
<p><a href="#_bookmark114">232, 234, 236, 239, 241,</a></p>
<p><a href="#_bookmark114">243, 245, 247,</a> <a href="#_bookmark129">276,</a></p>
<p><a href="#_bookmark141">327c,</a> <a href="#_bookmark142">394c,</a> <a href="#_bookmark143">395-396,</a></p>
<p><a href="#_bookmark143">397a,</a> <a href="#_bookmark144">397c-397d,</a> <a href="#_bookmark156">411,</a></p>
<p><a href="#_bookmark164">432,</a> <a href="#_bookmark175">449-450,</a> <a href="#_bookmark181">461,</a> <a href="#_bookmark184">464</a>,</p>
<p><a href="#_bookmark189">467-468,</a> 474b, <a href="#_bookmark200">482,</a></p>
<p><a href="#_bookmark200">484,</a> <a href="#_bookmark201">486, 486a,</a> <a href="#_bookmark212">523,</a></p>
<p><a href="#chapter-seven-code-set-versioning">525,</a> <a href="#_bookmark215">527,</a> <a href="#chapter-nine-glossary">549,</a> 553-554</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*176</p>
</blockquote></td>
<td><blockquote>
<p>Updated definitions, added new data fields, made changes to existing fields, data entry screens, reports, surgery risk assessment transmissions and transplant components of the VistA Surgery application. For more details, see the <em>Annual Surgery Updates – VASQIP 2011, Increment 2, Release Notes.</em></p>
<p>Chapter Seven: "CoreFLS/Surgery Interface" has been removed.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>09/11</p>
</blockquote></th>
<th><blockquote>
<p>i-iib, iii-iv, vi, 64, 66,</p>
<p>70, 98-101, 101a-101b,</p>
<p>109-112, 114-118, 122-</p>
<p>124, 124a-124b, 142-</p>
<p>152, 152a-152b, 176,</p>
<p>178, 180, 183-184,</p>
<p>184a-184f, 244, 246,</p>
<p>248, 325-326, 326a-</p>
<p>326b, 327, 327a-327d,</p>
<p>368, 394a-394b, 394c-</p>
<p>394d, 395-397, 397a-</p>
<p>397d, 432-433, 441,</p>
<p>449-450, 458-459, 461,</p>
<p>464a, 471-474, 474a-</p>
<p>474b, 475, 477, 480a,</p>
<p>482, 486-486a,</p>
<p>509,519, 521, 522a,</p>
<p>522c, 527, 534-535,</p>
<p>550, 552-556</p>
</blockquote></th>
<th><blockquote>
<p>SR*3*175</p>
</blockquote></th>
<th><blockquote>
<p>Updated definitions and made minor modifications to the non-cardiac, cardiac and transplant components of the VistA Surgery application. For more details, see the <em>Annual Surgery Updates – VASQIP 2011, Increment 1, Release Notes.</em></p>
<p><mark>REDACTED</mark></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>12/10</p>
</blockquote></th>
<th><blockquote>
<p>i-iib, 372, 376, 449-450,</p>
<p>458, 467-468, 468b,</p>
<p>471-474, 474a-474b,</p>
<p>479, 479a, 482, 486,</p>
<p>486a, 522c-522d</p>
</blockquote></th>
<th><blockquote>
<p>SR*3*174</p>
</blockquote></th>
<th><blockquote>
<p>Updated the data entry options for the non-cardiac and cardiac risk management sections; these options have been changed to match the software. For more details, see the <em>Annual Surgery Updates – VASQIP 2010 Release Notes.</em></p>
<p><mark>REDACTED</mark></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>11/08</p>
</blockquote></td>
<td><blockquote>
<p>vii-viii, 527-556</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*167</p>
</blockquote></td>
<td><blockquote>
<p>New chapter added for transplant assessments. Changed Glossary to Chapter 10, and renumbered the Index.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>04/08</p>
</blockquote></td>
<td><blockquote>
<p>iii-iv, vi, 160, 165, 168,</p>
<p>171-172, 296-298, 443,</p>
<p>447, 449-450, 459, 471-</p>
<p>473, 479-479a, 482,</p>
<p>486-486a, 489, 491,</p>
<p>493- 495, 497, 499,</p>
<p>501-502a, 502c, 502d-</p>
<p>502h, 513-517, 522c-</p>
<p>522d, 529, 534</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*166</p>
</blockquote></td>
<td><blockquote>
<p>Updated the data entry options for the non-cardiac and cardiac risk management sections; these options have been changed to match the software. For more details, see the <em>Surgery NSQIP-CICSP Enhancements 2008 Release Notes.</em></p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11/07</p>
</blockquote></td>
<td><blockquote>
<p>479-479a, 486a</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*164</p>
</blockquote></td>
<td><blockquote>
<p>Updated the <em>Resource Data Enter/Edit</em> and the <em>Print a Surgery Risk Assessment</em> options to reflect the new cardiac field for CT Surgery Consult Date.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>09/07</p>
</blockquote></td>
<td><blockquote>
<p>125, 371, 375, 382</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*163</p>
</blockquote></td>
<td><blockquote>
<p>Updated the Service Classification section regarding environmental indicators, unrelated to this patch.</p>
<p>Updated the Quarterly Report to reflect updates to the numbers and names of specific specialties in the NATIONAL SURGICAL SPECIALTY file.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/07</p>
</blockquote></td>
<td><blockquote>
<p>35, 210, 212b</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*159</p>
</blockquote></td>
<td><blockquote>
<p>Updated screens to reflect change of the environmental indicator "Environmental Contaminant" to "SWAC" (e.g., SouthWest Asia).</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>06/07</p>
</blockquote></td>
<td><blockquote>
<p>176-180, 180a, 184c-d,</p>
<p>327c-d, 372, 375-376,</p>
<p>446, 449-450, 452-453,</p>
<p>455-456, 458, 461, 468,</p>
<p>470, 472, 479-479a,</p>
<p>482-484, 486a, 489,</p>
<p>491, 493, 495, 497, 499,</p>
<p>501, 502a-d, 504-506,</p>
<p>509-512, 519</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*160</p>
</blockquote></td>
<td><blockquote>
<p>Updated the data entry options for the non-cardiac and cardiac risk management sections; these options have been changed to match the software. For more details, see the <em>Surgery NSQIP-CICSP Enhancements 2007 Release Notes.</em></p>
<p>Updated data entry screens to match software; changes are unrelated to this patch.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>11/06</p>
</blockquote></td>
<td><blockquote>
<p>10-12, 14, 21-22, 139-</p>
<p>141, 145-150, 152, 219,</p>
<p>438</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*157</p>
</blockquote></td>
<td><blockquote>
<p>Updated data entry options to display new fields for collecting sterility information for the Prosthesis Installed field; updated the Nurse Intraoperative Report section with these required new fields. For more details, see the <em>Surgery-Tracking Prosthesis Items Release Notes</em>.</p>
<p>Updated data entry screens to match software; changes are unrelated to this patch.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>08/06</p>
</blockquote></td>
<td><blockquote>
<p>6-9, 14, 109-112, 122-</p>
<p>124, 141-149, 151-152,</p>
<p>176, 178-180, 180a-b,</p>
<p>181-184, 184a-d, 185-</p>
<p>186, 218-219, 326-327,</p>
<p>327a-d, 328-329, 373,</p>
<p>377, 449-450, 452-456,</p>
<p>459, 461-462, 467-468,</p>
<p>468b, 469-470, 470a,</p>
<p>473-474, 474a-474b,</p>
<p>475, 477, 481-486,</p>
<p>486a-b, 489-502, 502a-</p>
<p>b, 503-504, 509-512</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*153</p>
</blockquote></td>
<td><blockquote>
<p>Updated the data entry options for the non-cardiac and cardiac risk management sections; these options have been changed to match the software.</p>
<p>Updated data entry options to incorporate renamed/new Hair Removal documentation fields. Updated the Nurse Intraoperative Report and Quarterly Report to include these fields.</p>
<p>For more details, see the <em>Surgery NSQIP/CICSP Enhancements 2006 Release Notes.</em></p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/06</p>
</blockquote></td>
<td><blockquote>
<p>28-32, 40-50, 64-80,</p>
<p>101-102</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*144</p>
</blockquote></td>
<td><blockquote>
<p>Updated options to reflect new required fields (Attending Surgeon and Principal Preoperative Diagnosis) for creating a surgery case.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>06/06</p>
</blockquote></td>
<td><blockquote>
<p>vi, 34-35, 125, 210, 212b, 522a-b</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*152</p>
</blockquote></td>
<td><blockquote>
<p>Updated Service Classification screen example to display new PROJ 112/SHAD prompt.</p>
<p>This patch will prevent the PRIN PRE-OP ICD DIAGNOSIS CODE field of the Surgery file from being sent to the Patient Care Encounter (PCE) package.</p>
<p>Added the new Alert Coder Regarding Coding Issues option to the Surgery Risk Assessment Menu option. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04/06</p>
</blockquote></td>
<td><blockquote>
<p>445, 464a-b, 465,</p>
<p>480a-b</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*146</p>
</blockquote></td>
<td><blockquote>
<p>Added the new <em>Alert Coder Regarding Coding Issues</em></p>
<p>option to the Assessing Surgical Risk chapter.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

> November 2015 Surgery V. 3.0 User Manual iib

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>04/06</p>
</blockquote></td>
<td><blockquote>
<p>6-8, 29, 31-32, 37-38,</p>
<p>40, 43-44, 46-48, 50,</p>
<p>52, 65-67, 71-73, 75-77,</p>
<p>79, 100, 102, 109-112,</p>
<p>117-120, 122-123, 125-</p>
<p>127, 189-191, 195b,</p>
<p>209-212, 212a-h, 219a,</p>
<p>224-231, 238-242, 273-</p>
<p>277, 311-313, 315-317,</p>
<p>369, 379- 392, 410,</p>
<p>449-464, 467-468,</p>
<p>468a-b, 469-470, 470a,</p>
<p>471-474, 474a-b, 475-</p>
<p>479, 479a-b, 480, 483-</p>
<p>484, 489-502, 507, 519</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*142</p>
</blockquote></td>
<td><blockquote>
<p>Updated the data entry screens to reflect renaming of the Planned Principal CPT Code field and the Principal Pre-op ICD Diagnosis Code field. Updated the <em>Update/Verify Procedure/Diagnosis Coding</em> option to reflect new functionality. Updated Risk Assessment options to remove CPT codes from headers of cases displayed. Updated reports related to the coding option to reflect final CPT codes.</p>
<p>For more specific information on changes, see the <em>Patient Financial Services System (PFSS) – Surgery Release Notes</em> for this patch.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/05</p>
</blockquote></td>
<td><blockquote>
<p>9, 109-110, 144, 151,</p>
<p>218</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*147</p>
</blockquote></td>
<td><blockquote>
<p>Updated data entry screens to reflect renaming of the Preop Shave By field to Preop Hair Clipping By field. <mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>08/05</p>
</blockquote></td>
<td><blockquote>
<p>10, 14, 99-100, 114,</p>
<p>119-120, 124, 153-154,</p>
<p>162-164, 164a-b, 190,</p>
<p>192, 209-212f, 238-242</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*119</p>
</blockquote></td>
<td><blockquote>
<p>Updated the Anesthesia Data Entry Menu section (and other data entry options) to reflect new functionality for entering multiple start and end times for anesthesia. Updated examples for Referring Physician updates (e.g., capability to automatically look up physician by name). Updated the PCE Filing Status Report section.</p>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>08/04</p>
</blockquote></td>
<td><blockquote>
<p>iv-vi, 187-189, 195,</p>
<p>195a-195b, 196, 207-</p>
<p>208, 219a-b, 527-528</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*132</p>
</blockquote></td>
<td><blockquote>
<p>Updated the Table of Contents and Index to reflect added options. Added the new <em>Non-OR Procedure Information</em> option and the <em>Tissue Examination Report</em></p>
<p>option (unrelated to this patch) to the Non-OR Procedures section.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>08/04</p>
</blockquote></td>
<td><blockquote>
<p>31, 43, 46, 66, 71-72,</p>
<p>75-76, 311</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*127</p>
</blockquote></td>
<td><blockquote>
<p>Updated screen captures to display new text for ICD-9 and CPT codes.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revised Pages</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch Number</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>08/04</p>
</blockquote></td>
<td><blockquote>
<p>vi, 441, 443, 445-456,</p>
<p>458-459, 461 463, 465,</p>
<p>467-468, 468a-b, 469-</p>
<p>470, 470a-b, 471, 473-</p>
<p>474, 474a-b, 474-479,</p>
<p>479a-b, 480-486, 486a-</p>
<p>b, 519, 531-534</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*125</p>
</blockquote></td>
<td><blockquote>
<p>Updated the Table of Contents and Index. Clarified the location of the national centers for NSQIP and CICSP. Updated the data entry options for the non- cardiac and cardiac risk management sections; these options have been changed to match the software and new options have been added. For an overview of the data entry changes, see the <em>Surgery NSQIP/CICSP Enhancements 2004 Release Notes.</em> Added the <em>Laboratory Test Result (Enter/Edit)</em> option and the <em>Outcome Information (Enter/Edit)</em> option to the <em>Cardiac Risk Assessment Information (Enter/Edit)</em> menu section. Changed the name of the <em>Cardiac Procedures Requiring CPB (Enter/Edit</em>) option to <em>Cardiac Procedures Operative Data (Enter/Edit)</em> option. Removed the <em>Update Operations as Unrelated/Related to Death</em> option from the <em>Surgery Risk Assessment Menu</em>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>08/04</p>
</blockquote></td>
<td><blockquote>
<p>6-10, 14, 103, 105-107,</p>
<p>109-112, 114-120, 122-</p>
<p>124, 141-152, 218-219,</p>
<p>284-287, 324, 370-377</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*129</p>
</blockquote></td>
<td><blockquote>
<p>Updated examples to include the new levels for the Attending Code (or Resident Supervision). Also updated examples to include the new fields for ensuring Correct Surgery. For specific options affected by each of these updates, please see the</p>
<p><em>Resident Supervision/Ensuring Correct Surgery Phase II Release Notes.</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>04/04</p>
</blockquote></td>
<td><blockquote>
<p>All</p>
</blockquote></td>
<td><blockquote>
<p>SR*3*100</p>
</blockquote></td>
<td><blockquote>
<p>All pages were updated to reflect the most recent Clinical Ancillary Local Documentation Standards and the changes resulting from the Surgery Electronic Signature for Operative Reports project, SR*3*100. For more information about the specific changes, see the patch description or the <em>Surgery Electronic Signature for Operative Reports Release Notes</em>.</p>
</blockquote></td>
</tr>
</tbody>
</table>
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Overview](#overview)
- [Documentation Conventions](#documentation-conventions)
  - [![](surgery-version-3-user-manual-updated-sr-3-184/002.png)![](surgery-version-3-user-manual-updated-sr-3-184/003.png)![](surgery-version-3-user-manual-updated-sr-3-184/004.png)![](surgery-version-3-user-manual-updated-sr-3-184/005.png)Getting Help and Exiting](#surgery-version-3-user-manual-updated-sr-3-184002pngsurgery-version-3-user-manual-updated-sr-3-184003pngsurgery-version-3-user-manual-updated-sr-3-184004pngsurgery-version-3-user-manual-updated-sr-3-184005pnggetting-help-and-exiting)
- [Using Screen Server](#using-screen-server)
  - [Introduction](#introduction-1)
  - [Navigating](#navigating)
  - [Basics of Screen Server](#basics-of-screen-server)
  - [Entering Data](#entering-data)
  - [Editing Data](#editing-data)
  - [Turning Pages](#turning-pages)
  - [Entering or Editing a Range of Data Elements](#entering-or-editing-a-range-of-data-elements)
  - [Working with Multiples](#working-with-multiples)
  - [Word Processing](#word-processing)
- [Chapter One: Booking Operations](#chapter-one-booking-operations)
- [Introduction](#introduction-2)
  - [Key Vocabulary](#key-vocabulary)
  - [Exiting an Option or the System](#exiting-an-option-or-the-system)
  - [Option Overview](#option-overview)
- [Maintain Surgery Waiting List](#maintain-surgery-waiting-list)
    - [\[SROWAIT\]](#srowait)
  - [Print Surgery Waiting List](#print-surgery-waiting-list)
    - [\[SRSWL2\]](#srswl2)
  - [Enter a Patient on the Waiting List](#enter-a-patient-on-the-waiting-list)
    - [\[SROW-ENTER\]](#srow-enter)
  - [Edit a Patient on the Waiting List](#edit-a-patient-on-the-waiting-list)
    - [\[SROW-EDIT\]](#srow-edit)
  - [Delete a Patient from the Waiting List](#delete-a-patient-from-the-waiting-list)
    - [\[SROW-DELETE\]](#srow-delete)
- [Request Operations Menu](#request-operations-menu)
    - [\[SROREQ\]](#sroreq)
  - [Display Availability](#display-availability)
    - [\[SRODISP\]](#srodisp)
  - [Make Operation Requests](#make-operation-requests)
    - [\[SROOPREQ\]](#sroopreq)
    - [Updating an Operation Request with Service Classification Information](#updating-an-operation-request-with-service-classification-information)
  - [Delete or Update Operation Requests](#delete-or-update-operation-requests)
    - [\[SRSUPRQ\]](#srsuprq)
  - [Make a Request from the Waiting List](#make-a-request-from-the-waiting-list)
    - [\[SRSWREQ\]](#srswreq)
  - [Make a Request for Concurrent Cases](#make-a-request-for-concurrent-cases)
    - [\[SRSREQCC\]](#srsreqcc)
  - [Review Request Information](#review-request-information)
    - [\[SROREQV\]](#sroreqv)
  - [Operation Requests for a Day](#operation-requests-for-a-day)
    - [\[SROP REQ\]](#srop-req)
  - [Requests by Ward](#requests-by-ward)
    - [\[SROWRQ\]](#srowrq)
- [List Operation Requests](#list-operation-requests)
    - [\[SRSRBS\]](#srsrbs)
- [Schedule Operations](#schedule-operations)
    - [\[SROSCHOP\]](#sroschop)
  - [Display Availability](#display-availability-1)
    - [\[SRODISP\]](#srodisp-1)
  - [Schedule Requested Operation](#schedule-requested-operation)
    - [\[SRSCHD1\]](#srschd1)
  - [Schedule Unrequested Operations](#schedule-unrequested-operations)
    - [\[SROSRES\]](#srosres)
  - [Schedule Unrequested Concurrent Cases](#schedule-unrequested-concurrent-cases)
    - [\[SRSCHDC\]](#srschdc)
  - [Reschedule or Update a Scheduled Operation](#reschedule-or-update-a-scheduled-operation)
    - [\[SRSCHUP\]](#srschup)
  - [Cancel Scheduled Operation](#cancel-scheduled-operation)
    - [\[SRSCAN\]](#srscan)
  - [Update Cancellation Reason](#update-cancellation-reason)
    - [\[SRSUPC\]](#srsupc)
  - [Schedule Anesthesia Personnel](#schedule-anesthesia-personnel)
    - [\[SRSCHDA\]](#srschda)
  - [Create Service Blockout](#create-service-blockout)
    - [\[SRSBOUT\]](#srsbout)
  - [Delete Service Blockout](#delete-service-blockout)
    - [\[SRSBDEL\]](#srsbdel)
  - [Schedule of Operations](#schedule-of-operations)
    - [\[SROSCH\]](#srosch)
- [List Scheduled Operations](#list-scheduled-operations)
    - [\[SRSCD\]](#srscd)
- [Chapter Two: Tracking Clinical Procedures](#chapter-two-tracking-clinical-procedures)
  - [Exiting an Option or the System](#exiting-an-option-or-the-system-1)
  - [Option Overview](#option-overview-1)
- [Operation Menu](#operation-menu)
    - [\[SROPER\]](#sroper)
  - [Abort/Cancel Operation](#abortcancel-operation)
    - [\[SROABRT\]](#sroabrt)
  - [Operation Information](#operation-information)
    - [\[SROMEN-OPINFO\]](#sromen-opinfo)
  - [Surgical Staff \[SROMEN-STAFF\]](#surgical-staff-sromen-staff)
  - [Operation Startup](#operation-startup)
    - [\[SROMEN-START\]](#sromen-start)
  - [Operation](#operation)
    - [\[SROMEN-OP\]](#sromen-op)
  - [Post Operation](#post-operation)
    - [\[SROMEN-POST\]](#sromen-post)
  - [Enter PAC(U) Information](#enter-pacu-information)
    - [\[SROMEN-PACU\]](#sromen-pacu)
  - [Operation (Short Screen)](#operation-short-screen)
    - [\[SROMEN-OUT\]](#sromen-out)
  - [Time Out Verified Utilizing Checklist](#time-out-verified-utilizing-checklist)
    - [\[SROMEN-VERF\]](#sromen-verf)
  - [Surgeon's Verification of Diagnosis & Procedures](#surgeons-verification-of-diagnosis-procedures)
    - [\[SROVER\]](#srover)
  - [Anesthesia for an Operation Menu](#anesthesia-for-an-operation-menu)
    - [\[SROANES\]](#sroanes)
  - [Operation Report](#operation-report)
    - [\[SROSRPT\]](#srosrpt)
  - [Anesthesia Report](#anesthesia-report)
    - [\[SROARPT\]](#sroarpt)
  - [Nurse Intraoperative Report](#nurse-intraoperative-report)
    - [\[SRONRPT\]](#sronrpt)
  - [Tissue Examination Report](#tissue-examination-report)
    - [\[SROTRPT\]](#srotrpt)
  - [Enter Referring Physician Information](#enter-referring-physician-information)
    - [\[SROMEN-REFER\]](#sromen-refer)
  - [Enter Irrigations and Restraints](#enter-irrigations-and-restraints)
    - [\[SROMEN-REST\]](#sromen-rest)
  - [Medications (Enter/Edit)](#medications-enteredit)
    - [\[SROANES MED\]](#sroanes-med)
  - [Blood Product Verification](#blood-product-verification)
    - [\[SR BLOOD PRODUCT VERIFICATION\]](#sr-blood-product-verification)
- [Anesthesia Menu](#anesthesia-menu)
  - [\[SROANES1\]](#sroanes1)
  - [Prerequisites](#prerequisites)
  - [Anesthesia Data Entry Menu](#anesthesia-data-entry-menu)
    - [\[SROANES-D\]](#sroanes-d)
  - [Anesthesia Information (Enter/Edit)](#anesthesia-information-enteredit)
    - [\[SROMEN-ANES\]](#sromen-anes)
  - [Anesthesia Technique (Enter/Edit)](#anesthesia-technique-enteredit)
    - [\[SROMEN-ANES TECH\]](#sromen-anes-tech)
  - [Medications (Enter/Edit)](#medications-enteredit-1)
    - [\[SROANES MED\]](#sroanes-med-1)
  - [Anesthesia Report](#anesthesia-report-1)
    - [\[SROARPT\]](#sroarpt-1)
  - [Schedule Anesthesia Personnel](#schedule-anesthesia-personnel-1)
    - [\[SRSCHDA\]](#srschda-1)
- [Perioperative Occurrences Menu](#perioperative-occurrences-menu)
    - [\[SRO COMPLICATIONS MENU\]](#sro-complications-menu)
  - [Key Vocabulary](#key-vocabulary-1)
  - [Intraoperative Occurrences (Enter/Edit)](#intraoperative-occurrences-enteredit)
    - [\[SRO INTRAOP COMP\]](#sro-intraop-comp)
  - [Postoperative Occurrences (Enter/Edit)](#postoperative-occurrences-enteredit)
    - [\[SRO POSTOP COMP\]](#sro-postop-comp)
  - [Non-Operative Occurrence (Enter/Edit)](#non-operative-occurrence-enteredit)
    - [\[SROCOMP\]](#srocomp)
  - [Update Status of Returns Within 30 Days](#update-status-of-returns-within-30-days)
    - [\[SRO UPDATE RETURNS\]](#sro-update-returns)
  - [Morbidity & Mortality Reports](#morbidity-mortality-reports)
    - [\[SROMM\]](#sromm)
- [Non-O.R. Procedures](#non-or-procedures)
    - [\[SRONOP\]](#sronop)
    - [\[SRONOP-ENTER\]](#sronop-enter)
  - [Edit Non-O.R. Procedure](#edit-non-or-procedure)
    - [\[SRONOP-EDIT\]](#sronop-edit)
  - [Procedure Report (Non-O.R.)](#procedure-report-non-or)
    - [\[SR NON-OR REPORT\]](#sr-non-or-report)
  - [Tissue Examination Report](#tissue-examination-report-1)
    - [\[SROTRPT\]](#srotrpt-1)
  - [Non-OR Procedure Information](#non-or-procedure-information)
    - [\[SR NON-OR INFO\]](#sr-non-or-info)
  - [Annual Report of Non-O.R. Procedures](#annual-report-of-non-or-procedures)
    - [\[SRONOP-ANNUAL\]](#sronop-annual)
  - [Report of Non-O.R. Procedures](#report-of-non-or-procedures)
    - [\[SRONOR\]](#sronor)
- [Comments Option](#comments-option)
    - [\[SROMEN-COM\]](#sromen-com)
- [CPT/ICD Coding Menu](#cpticd-coding-menu)
    - [\[SRCODING MENU\]](#srcoding-menu)
    - [\[SRCODING UPDATE/VERIFY MENU\]](#srcoding-updateverify-menu)
  - [Update/Verify Procedure/Diagnosis Codes](#updateverify-procedurediagnosis-codes)
    - [\[SRCODING EDIT\]](#srcoding-edit)
  - [Operation/Procedure Report](#operationprocedure-report)
    - [\[SRCODING OP REPORT\]](#srcoding-op-report)
  - [Nurse Intraoperative Report](#nurse-intraoperative-report-1)
    - [\[SRCODING NURSE REPORT\]](#srcoding-nurse-report)
  - [Non-OR Procedure Information](#non-or-procedure-information-1)
    - [\[SR NON-OR INFO\]](#sr-non-or-info-1)
  - [Cumulative Report of CPT Codes](#cumulative-report-of-cpt-codes)
    - [\[SROACCT\]](#sroacct)
  - [Report of CPT Coding Accuracy](#report-of-cpt-coding-accuracy)
  - [List Completed Cases Missing CPT Codes](#list-completed-cases-missing-cpt-codes)
    - [\[SRSCPT](#srscpt)
  - [List of Operations](#list-of-operations)
    - [\[SROPLIST\]](#sroplist)
  - [List of Operations (by Surgical Specialty)](#list-of-operations-by-surgical-specialty)
    - [\[SROPLIST1\]](#sroplist1)
  - [Report of Daily Operating Room Activity](#report-of-daily-operating-room-activity)
    - [\[SROPACT\]](#sropact)
  - [PCE Filing Status Report](#pce-filing-status-report)
    - [\[SRO PCE STATUS\]](#sro-pce-status)
  - [Report of Non-O.R. Procedures](#report-of-non-or-procedures-1)
    - [\[SRONOR\]](#sronor-1)
- [Chapter Three: Generating Surgical Reports Introduction](#chapter-three-generating-surgical-reports-introduction)
  - [Exiting an Option or the System](#exiting-an-option-or-the-system-2)
  - [Option Overview](#option-overview-2)
- [Surgery Reports](#surgery-reports)
    - [\[SRORPTS\]](#srorpts)
    - [\[SR MANAGE REPORTS\]](#sr-manage-reports)
    - [\[SROSCH\]](#srosch-1)
    - [\[SROARSP\]](#sroarsp)
    - [\[SROPLIST\]](#sroplist-1)
    - [List of Operations (by Postoperative Disposition)](#list-of-operations-by-postoperative-disposition)
    - [List of Operations (by Surgical Specialty)](#list-of-operations-by-surgical-specialty-1)
    - [Report of Surgical Priorities](#report-of-surgical-priorities)
    - [Report of Daily Operating Room Activity](#report-of-daily-operating-room-activity-1)
    - [PCE Filing Status Report](#pce-filing-status-report-1)
    - [Outpatient Encounters Not Transmitted to NPCD](#outpatient-encounters-not-transmitted-to-npcd)
  - [Surgery Staffing Reports](#surgery-staffing-reports)
    - [\[SR STAFFING REPORTS\]](#sr-staffing-reports)
    - [\[SROATT\]](#sroatt)
    - [\[SROSUR\]](#srosur)
    - [\[SRONSR\]](#sronsr)
    - [\[SROSNR\]](#srosnr)
    - [\[SROCNR\]](#srocnr)
  - [Anesthesia Reports](#anesthesia-reports)
    - [\[SR ANESTH REPORTS\]](#sr-anesth-reports)
    - [\[SROANP\]](#sroanp)
    - [\[SROADOC\]](#sroadoc)
  - [CPT Code Reports](#cpt-code-reports)
    - [\[SR CPT REPORTS\]](#sr-cpt-reports)
    - [\[SROACCT\]](#sroacct-1)
    - [\[SR CPT ACCURACY\]](#sr-cpt-accuracy)
    - [\[SRSCPT\]](#srscpt-1)
- [Laboratory Interim Report](#laboratory-interim-report)
    - [\[SRO-LRRP\]](#sro-lrrp)
- [Chapter Four: Chief of Surgery Reports Introduction](#chapter-four-chief-of-surgery-reports-introduction)
  - [Option Overview](#option-overview-3)
- [Chief of Surgery Menu](#chief-of-surgery-menu)
    - [\[SROCHIEF\]](#srochief)
    - [\[SROMEN-M&M\]](#sromen-mm)
  - [Management Reports](#management-reports)
    - [\[SRO-CHIEF REPORTS\]](#sro-chief-reports)
    - [\[SROMM\]](#sromm-1)
    - [\[SRO M&M VERIFICATION REPORT\]](#sro-mm-verification-report)
    - [\[SROPPC\]](#sroppc)
    - [\[SRO DEL MENU\]](#sro-del-menu)
    - [Report of Delayed Operations](#report-of-delayed-operations)
    - [Report of Delay Reasons](#report-of-delay-reasons)
    - [Report of Delay Time](#report-of-delay-time)
    - [Report of Cancellations](#report-of-cancellations)
    - [Report of Cancellation Rates](#report-of-cancellation-rates)
    - [\[SROUNV\]](#srounv)
    - [\[SRORET\]](#sroret)
    - [\[SROPACT\]](#sropact-1)
    - [\[SROSPEC\]](#srospec)
    - [\[SROICU\]](#sroicu)
    - [\[SR OR UTL1\]](#sr-or-utl1)
    - [\[SROWC\]](#srowc)
    - [\[SR BLOOD PRODUCT VERIFY AUDIT\]](#sr-blood-product-verify-audit)
    - [\[SROQ MISSING DATA\]](#sroq-missing-data)
    - [\[SROQADM\]](#sroqadm)
    - [Deaths Within 30 Days of Surgery](#deaths-within-30-days-of-surgery)
  - [Unlock a Case for Editing](#unlock-a-case-for-editing)
    - [\[SRO-UNLOCK\]](#sro-unlock)
  - [Update Status of Returns Within 30 Days](#update-status-of-returns-within-30-days-1)
    - [\[SRO UPDATE RETURNS\]](#sro-update-returns-1)
  - [Update Cancelled Cases](#update-cancelled-cases)
    - [\[SRO UPDATE CANCELLED CASE\]](#sro-update-cancelled-case)
  - [Update Operations as Unrelated/Related to Death](#update-operations-as-unrelatedrelated-to-death)
    - [\[SRO DEATH RELATED\]](#sro-death-related)
  - [Update/Verify Procedure/Diagnosis Codes](#updateverify-procedurediagnosis-codes-1)
    - [\[SRCODING EDIT\]](#srcoding-edit-1)
- [Chapter Five: Managing the Software Package Introduction](#chapter-five-managing-the-software-package-introduction)
  - [Option Overview](#option-overview-4)
- [Surgery Package Management Menu](#surgery-package-management-menu)
    - [\[SRO PACKAGE MANAGEMENT\]](#sro-package-management)
    - [\[SROPARAM\]](#sroparam)
  - [Operating Room Information (Enter/Edit)](#operating-room-information-enteredit)
    - [\[SRO-ROOM\]](#sro-room)
  - [Surgery Utilization Menu](#surgery-utilization-menu)
    - [\[SR OR UTIL\]](#sr-or-util)
    - [\[SR UTIL EDIT ROOM\]](#sr-util-edit-room)
    - [\[SR NORMAL HOURS\]](#sr-normal-hours)
    - [\[SR OR UTL1\]](#sr-or-utl1-1)
    - [How the Percent Utilization is Derived](#how-the-percent-utilization-is-derived)
    - [\[SR OR HOURS\]](#sr-or-hours)
    - [\[SR PURGE UTILIZATION\]](#sr-purge-utilization)
  - [Person Field Restrictions Menu](#person-field-restrictions-menu)
    - [\[SROKEY MENU\]](#srokey-menu)
    - [\[SROKEY ENTER\]](#srokey-enter)
    - [\[SROKEY REMOVE\]](#srokey-remove)
  - [Update O.R. Schedule Devices](#update-or-schedule-devices)
    - [\[SR UPDATE SCHEDULE DEVICE\]](#sr-update-schedule-device)
  - [Update Staff Surgeon Information](#update-staff-surgeon-information)
    - [\[SROSTAFF\]](#srostaff)
  - [Flag Drugs for Use as Anesthesia Agents](#flag-drugs-for-use-as-anesthesia-agents)
    - [\[SROCODE\]](#srocode)
  - [Update Site Configurable Files](#update-site-configurable-files)
    - [\[SR UPDATE FILES\]](#sr-update-files)
  - [Surgery Interface Management Menu](#surgery-interface-management-menu)
    - [\[SRHL INTERFACE\]](#srhl-interface)
    - [\[SRHL INTERFACE FLDS\]](#srhl-interface-flds)
    - [\[SRHL DOWNLOAD INTERFACE FILES\]](#srhl-download-interface-files)
    - [\[SRHL DOWNLOAD SET OF CODES\]](#srhl-download-set-of-codes)
    - [\[SRHL DOWNLOAD SET OF CODES\]](#srhl-download-set-of-codes-1)
  - [Make Reports Viewable in CPRS](#make-reports-viewable-in-cprs)
    - [\[SR VIEW HISTORICAL REPORTS\]](#sr-view-historical-reports)
- [Chapter Six: Assessing Surgical Risk Introduction](#chapter-six-assessing-surgical-risk-introduction)
- [Surgery Risk Assessment Menu](#surgery-risk-assessment-menu)
    - [\[SROA RISK ASSESSMENT\]](#sroa-risk-assessment)
- [Non-Cardiac Risk Assessment Information (Enter/Edit)](#non-cardiac-risk-assessment-information-enteredit)
    - [\[SROA ENTER/EDIT\]](#sroa-enteredit)
  - [Editing an Incomplete Risk Assessment](#editing-an-incomplete-risk-assessment)
  - [Preoperative Information (Enter/Edit)](#preoperative-information-enteredit)
    - [\[SROA PREOP DATA\]](#sroa-preop-data)
  - [Laboratory Test Results (Enter/Edit)](#laboratory-test-results-enteredit)
    - [\[SROA LAB\]](#sroa-lab)
  - [Operation Information (Enter/Edit)](#operation-information-enteredit)
    - [\[SROA OPERATION DATA\]](#sroa-operation-data)
  - [Patient Demographics (Enter/Edit)](#patient-demographics-enteredit)
    - [\[SROA DEMOGRAPHICS\]](#sroa-demographics)
  - [Intraoperative Occurrences (Enter/Edit)](#intraoperative-occurrences-enteredit-1)
    - [\[SRO INTRAOP COMP\]](#sro-intraop-comp-1)
  - [Postoperative Occurrences (Enter/Edit)](#postoperative-occurrences-enteredit-1)
    - [\[SRO POSTOP COMP\]](#sro-postop-comp-1)
  - [Update Status of Returns Within 30 Days](#update-status-of-returns-within-30-days-2)
    - [\[SRO UPDATE RETURNS\]](#sro-update-returns-2)
  - [Update Assessment Status to 'Complete'](#update-assessment-status-to-complete)
    - [\[SROA COMPLETE ASSESSMENT\]](#sroa-complete-assessment)
  - [Alert Coder Regarding Coding Issues](#alert-coder-regarding-coding-issues)
    - [\[SROA CODE ISSUE\]](#sroa-code-issue)
- [Cardiac Risk Assessment Information (Enter/Edit)](#cardiac-risk-assessment-information-enteredit)
    - [\[SROA CARDIAC ENTER/EDIT\]](#sroa-cardiac-enteredit)
  - [Creating a New Risk Assessment](#creating-a-new-risk-assessment)
  - [Clinical Information (Enter/Edit)](#clinical-information-enteredit)
    - [\[SROA CLINICAL INFORMATION\]](#sroa-clinical-information)
  - [Laboratory Test Results (Enter/Edit)](#laboratory-test-results-enteredit-1)
    - [\[SROA LAB-CARDIAC\]](#sroa-lab-cardiac)
  - [Enter Cardiac Catheterization & Angiographic Data](#enter-cardiac-catheterization-angiographic-data)
    - [\[SROA CATHETERIZATION\]](#sroa-catheterization)
  - [Operative Risk Summary Data (Enter/Edit)](#operative-risk-summary-data-enteredit)
    - [\[SROA CARDIAC OPERATIVE RISK\]](#sroa-cardiac-operative-risk)
  - [Cardiac Procedures Operative Data (Enter/Edit)](#cardiac-procedures-operative-data-enteredit)
    - [\[SROA CARDIAC PROCEDURES\]](#sroa-cardiac-procedures)
  - [Intraoperative Occurrences (Enter/Edit)](#intraoperative-occurrences-enteredit-2)
    - [\[SRO INTRAOP COMP\]](#sro-intraop-comp-2)
  - [Postoperative Occurrences (Enter/Edit)](#postoperative-occurrences-enteredit-2)
    - [\[SRO POSTOP COMP\]](#sro-postop-comp-2)
  - [Resource Data (Enter/Edit)](#resource-data-enteredit)
    - [\[SROA CARDIAC RESOURCE\]](#sroa-cardiac-resource)
  - [Update Assessment Status to 'COMPLETE'](#update-assessment-status-to-complete-1)
    - [\[SROA COMPLETE ASSESSMENT\]](#sroa-complete-assessment-1)
  - [Alert Coder Regarding Coding Issues](#alert-coder-regarding-coding-issues-1)
    - [\[SROA CODE ISSUE\]](#sroa-code-issue-1)
- [Print a Surgery Risk Assessment](#print-a-surgery-risk-assessment)
    - [\[SROA PRINT ASSESSMENT\]](#sroa-print-assessment)
- [Update Assessment Completed/Transmitted in Error](#update-assessment-completedtransmitted-in-error)
    - [\[SROA TRANSMITTED IN ERROR\]](#sroa-transmitted-in-error)
- [List of Surgery Risk Assessments](#list-of-surgery-risk-assessments)
    - [\[SROA ASSESSMENT LIST\]](#sroa-assessment-list)
- [Print 30 Day Follow-up Letters](#print-30-day-follow-up-letters)
    - [\[SROA REPRINT LETTERS\]](#sroa-reprint-letters)
- [Exclusion Criteria (Enter/Edit)](#exclusion-criteria-enteredit)
    - [\[SR NO ASSESSMENT REASON\]](#sr-no-assessment-reason)
- [Monthly Surgical Case Workload Report](#monthly-surgical-case-workload-report)
    - [\[SROA MONTHLY WORKLOAD REPORT\]](#sroa-monthly-workload-report)
- [M&M Verification Report](#mm-verification-report)
    - [\[SRO M&M VERIFICATION REPORT\]](#sro-mm-verification-report-1)
- [Update 1-Liner Case](#update-1-liner-case)
    - [\[SROA ONE-LINER UPDATE\]](#sroa-one-liner-update)
- [Queue Assessment Transmissions](#queue-assessment-transmissions)
    - [\[SROA TRANSMIT ASSESSMENTS\]](#sroa-transmit-assessments)
- [Alert Coder Regarding Coding Issues](#alert-coder-regarding-coding-issues-2)
    - [\[SROA CODE ISSUE\]](#sroa-code-issue-2)
- [Risk Model Lab Test](#risk-model-lab-test)
    - [\[SROA LAB TEST EDIT\]](#sroa-lab-test-edit)
- [Chapter Seven: Code Set Versioning](#chapter-seven-code-set-versioning)
- [Chapter Nine: Glossary](#chapter-nine-glossary)
- [Index](#index)
> This section provides an overview of the Surgery package, and also provides documentation conventions used in this *Surgery V. 3.0 User Manual*. This section also discusses the use of the Screen Server in the Surgery package.

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery package is designed to be used by Surgeons, Surgical Residents, Anesthetists, Operating Room Nurses and other surgical staff. The Surgery package is part of the patient information system that stores data on the Department of Veterans Affairs (VA) patients who have, or are about to undergo, surgical procedures. This package integrates booking, clinical, and patient data to provide a variety of administrative and clinical reports.

> The *Surgery V. 3.0 User Manual* is designed to acquaint the user with the various Surgery options and to offer specific guidance on the use of the Surgery package. Documentation concerning the Surgery package, including any subsequent change pages affecting this documentation, can be found at the Veterans Health Information Systems and Technology Architecture (VistA) Documentation Library (VDL) on the Internet at [<u>http://www.va.gov/vdl/</u>.](http://www.va.gov/vdl/)

> *(This page included for two-sided copying.)*

# Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This *Surgery V. 3.0 User Manual* includes documentation conventions, also known as notations, which are used consistently throughout this manual. Each convention is outlined below.

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Convention</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Example</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Menu option text is italicized.</p>
</blockquote></td>
<td><blockquote>
<p>The <em>Print Surgery Waiting List</em> option generates the long form surgery Waiting List for the surgical service(s) selected.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Screen prompts are denoted with quotation marks around them.</p>
</blockquote></td>
<td><blockquote>
<p>The "Puncture Site:" prompt will display next.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Responses in bold face indicate user input.</p>
</blockquote></td>
<td><blockquote>
<p>Needle Size: <strong>25G</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Text centered between bent parentheses represents a keyboard key that needs to be pressed for the system to capture a user response or move the cursor to another field.</p>
<p><strong>&lt;Enter&gt;</strong> indicates that the Enter key (or Return key on some keyboards) must be pressed.</p>
<p><strong>&lt;Tab&gt;</strong> indicates that the Tab key must be pressed.</p>
</blockquote></td>
<td><blockquote>
<p>Type <strong>Y</strong> for Yes or <strong>N</strong> for No and press</p>
<p><strong>&lt;Enter&gt;</strong>.</p>
<p>Press <strong>&lt;Tab&gt;</strong> to move the cursor to the next field.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Indicates especially important or helpful information.</p>
</blockquote></td>
<td><blockquote>
<p>If the user attempts to reschedule a case after the schedule close time for the date of operation,</p>
<p>only the time, and not the date, can be changed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Indicates that options are locked with a particular security key. The user must hold the</p>
<p>particular security key to be able to perform the menu option.</p>
</blockquote></td>
<td><blockquote>
<p>Without the SROAMIS key the</p>
<p><em>Anesthesia AMIS</em> option cannot be accessed.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## ![](surgery-version-3-user-manual-updated-sr-3-184/002.png)![](surgery-version-3-user-manual-updated-sr-3-184/003.png)![](surgery-version-3-user-manual-updated-sr-3-184/004.png)![](surgery-version-3-user-manual-updated-sr-3-184/005.png)Getting Help and Exiting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ?, ??, ??? One, two or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions, and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

> Typing an up arrow ^ (caret or a circumflex) and pressing \<Enter\> can be used to exit the current option.

> *(This page included for two-sided copying.)*

# Using Screen Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides information about using the Screen Server utility with the Surgery software.

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Screen Server is a screen-based data entry utility. It allows the user to display and select data elements for entering, editing, and deleting information. The format is designed to display a number of data fields at one time on a menu. With Screen Server, a number of data elements are displayed at one time on a menu and the user is able to choose on which element to work.

> This section contains a description of the Screen Server format and gives examples of how to respond to the unique Screen Server prompts. The screen facsimiles used in the examples are taken from the Surgery software; however, these screens may not display on the terminal monitor exactly as they display in this manual, because the Surgery package is subject to enhancements and local modifications. In this document, the different ways to respond to the Screen Server prompt, to perform a task, and to utilize shortcuts are explained. The shortcuts are listed below:

- Enter data
- Edit data
- Move between pages
- Enter/edit a range of data elements
- Multiples
- Multiple screen shortcuts
- Word processing

> The user should be familiar with VistA conventions. In the examples, the user's response is presented in bold face text.

## Navigating

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user can press the Return key to move through a prompt and go to the next page or item. To return directly to the *Surgery Menu* options, the user can enter an up-arrow (^), unless he or she is in a multiple field. To exit a multiple field, enter two up-arrows (^^).

## Basics of Screen Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each Screen Server arrangement consists of three basic parts: a header, data elements, and an action prompt. These items are defined in the following table.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Header</p>
</blockquote></td>
<td><blockquote>
<p>The screen heading contains information specific to the record with which you are</p>
<p>working. This can include the patient name or case number. The information in the heading is programmed and cannot be easily changed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Data Elements</p>
</blockquote></td>
<td><blockquote>
<p>Each Screen Server display contains from 1 to 15 data elements (or fields). If information has been entered for any of the data elements defined, it will display to the right of the element. Some data elements are multiple fields, meaning they can contain more than one piece of information. These multiple fields are distinguished by the word "Multiple" next to the data element. If the multiple fields contain</p>
<p>information, the word "Data" will be next to the data element.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Prompt</p>
</blockquote></td>
<td><blockquote>
<p>The action prompt is at the bottom of each screen. From the prompt "Enter Screen Server Functions:" you can enter, edit, or delete information from the data elements. The possible responses to this prompt are explained in more detail on the following</p>
<p>pages. Enter a question mark (?), for help text with possible prompt responses.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following is an example of a Screen Server display with help text.

## Entering Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To enter or edit data, the user can type the item number corresponding with the data element for which he/she is entering information and press the \<Enter\> key. In the following example, we typed the number 10 at the prompt and pressed the \<Enter\> key. A new prompt appeared allowing us to enter the data. The software immediately processed this information and produced an updated menu screen and another action prompt.

> The software processes the information and produces an update.

## Editing Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Changing an existing entry is similar to entering. Once again, the user can type in the number for the data element he/she wants to change and press \<Enter\>. In the following example, the number 3 was entered to change the surgeon name. A new prompt appeared containing the existing value for the data element in a default format. We entered the new value, "SURSURGEON,TWO." The software immediately processed this information and produced an updated screen.

> The software processes the information and produces an update.

## Turning Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No more than 15 data elements will fit on a single Screen Server formatted page, but there can be as many pages as needed. Because many screens contain more than one page of data elements, the screen server provides the ability to move between the pages. Pages are numbered in the heading. To go back one page, enter minus one (-1) at the action prompt. To go forward, enter plus one (+1) or press \<Enter\>. The user can move more than one page by combining the minus or plus sign with the number of pages needed to go backward or forward.

## Entering or Editing a Range of Data Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Colons and semicolons are used as delineators for ranges of item numbers. This allows the user to respond to two or more data elements on the same page of a screen at one time. Typing a colon and/or semicolon between the item numbers at the prompt tells the software what elements to display for editing.

> Colons are used when the user wants to respond to all numbers within a sequence (for example, 2:5 means items 2, 3, 4, and 5). Semicolons are used to separate the item numbers for non-sequential items (e.g., 2; 5; 9; 11 means items 2, 5, 9 and 11). To respond to all the data elements on the page, enter "A" for all.

> Example 1: Colon

> Example 2: Semicolon

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 21%" />
<col style="width: 31%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p> STARTUP </p>
</blockquote></th>
<th><blockquote>
<p>CASE #24 SURPATIENT,TWO</p>
</blockquote></th>
<th><blockquote>
<p>PAGE 1 OF 3</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>HEIGHT:</p>
</blockquote></td>
<td><blockquote>
<p>58 INCHES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>WEIGHT:</p>
</blockquote></td>
<td><blockquote>
<p>264 LBS.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>DATE OF OPERATION:</p>
</blockquote></td>
<td><blockquote>
<p>APR 19, 2006 AT 800</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><ol start="4" type="1">
<li><p>PRINCIPAL PRE-OP DIAGNOSIS: DEGENERATIVE JOINT DISEASE</p></li>
<li><p>PRIN PRE-OP ICD DIAGNOSIS CODE (ICD9):</p></li>
<li><p>OTHER PREOP DIAGNOSIS: (MULTIPLE)</p></li>
<li><p>OP ROOM PROCEDURE PERFORMED: OR4</p></li>
<li><p>SURGERY SPECIALTY: ORTHOPEDICS</p></li>
<li><p>PLANNED POSTOP CARE: WARD</p></li>
<li><blockquote>
<p>CASE SCHEDULE TYPE: ELECTIVE</p>
</blockquote></li>
<li><blockquote>
<p>REQ ANESTHESIA TECHNIQUE: GENERAL</p>
</blockquote></li>
<li><p>PATIENT EDUCATION/ASSESSMENT: YES</p></li>
<li><blockquote>
<p>DELAY CAUSE: (MULTIPLE)</p>
</blockquote></li>
<li><blockquote>
<p>ASA CLASS:</p>
</blockquote></li>
<li><blockquote>
<p>PREOP MOOD:</p>
</blockquote></li>
</ol>
<blockquote>
<p>Enter Screen Server Function: <strong>7;9;</strong></p>
<p>Operating Room Procedure Performed: OR4// <strong>OR2</strong></p>
<p>Planned Postop Care: WARD//<strong>OUTPATIENT/DISCHARGE</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Working with Multiples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The notation MULTIPLE indicates a data element that can have more than one answer. Some multiple fields have several layers of screens from which to respond. Navigating through the layers may seem tedious at first, but the user will soon develop speed. Remember, the user can press \<Enter\> at the prompt to go back to the main menu screen, or enter an up-arrow (^) to go back to the previous screen.

> In the following examples, there are other screens after the initial (also called top-level) screen. With the multiple screens, a new menu list is built with each entry.

> Example: Multiples

> Notice the three user responses entered above. The first response, 12, told the software that we want to enter data in the PROSTHESIS INSTALLED field. Then, at the next screen, we entered "1" because we wanted to make a new prosthesis entry for this case. The third response, MANDIBULAR PLATES, told the software the kind of prosthesis being installed. The software echoed back the full prosthesis name "MANDIBULAR PLATES" and we accepted it by pressing \<Enter\>.

> Because the PROSTHESIS INSTALLED field can contain multiple answers, a new screen immediately appeared as follows:

> The first response, 2:10, corresponds to data elements 2 through 10. We entered data for these elements one-by-one and the software processed the information and produced this update:

> Pressing \<Enter\> will now bring back the top-level screen and allow us to make another entry. As many as 15 prostheses can be added to this list. If we were to add more prostheses, the N and R shortcuts discussed on the next two pages would come in handy, but it is a good idea to practice the steps just covered before attempting the shortcuts.

> Multiple Screen Shortcuts

> The help text for a multiple field mentions the N and R functions. The user can enter a question mark (?) to view the help text at the prompt, as displayed in the following example.

> N Function

> The N function allows the user to enter new entries without going beyond the top level screen, whereas the R function allows the user to repeat a previous top level response. In the following example we will build entries by entering the data element number and the letter N:

> The software processes the information and produces an update.

> R Function

> The R function saves the user from typing in the top-level information again. In this example, we have the same anesthesia technique but different anesthesia agents. By entering the element number we want to repeat, and the letter R, we avoid having to enter the top-level data again. This feature can also be useful in cases where the same medication is repeated at different times. After the user enters the item and the letter R, the software responds with a default prompt. The user can press \<Enter\> to accept the default.

> The software processes the information and produces an update.

> The software processes the information and produces an update.

> The updating continues through to the top layer.

## Word Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The phrase "Word Processing" in the menu means that the user can enter as much data as needed to complete the entry.

> Following is an example of how we entered text on a Screen Server word processing field. Notice that we pressed \<Enter\> after each line of text as there is no automatic word-wrap:

> The software processes the information and produces an update.

# Chapter One: Booking Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options described in this chapter facilitate the scheduling of surgical procedures. Automated scheduling provides better operating room use and greater ease in distributing the operating room schedule. These options help accomplish the following tasks.

- Track patients on a waiting list
- Track operation requests
- Chart operating room availability
- Designate operating rooms for a surgical service
- Schedule operations by assigning operating rooms and time slots
- Generate operating room schedules on any designated printer in the medical center
- Reschedule or cancel any operative procedures

> Whether or not the user is booking a case from the Waiting List, *Request Operations* menu, or *Schedule Operations* menu, he/she will be asked to provide preoperative information about the case. Some of the preoperative information is mandatory and must be entered immediately to proceed with the option, while other information can be entered later. It is advisable to enter as much information as possible and update or correct it later. If a prompt cannot be answered, the user can press the \<Enter\> key to move to the next item.

## Key Vocabulary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following terms are used in this chapter.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Concurrent Case</p>
</blockquote></td>
<td><blockquote>
<p>The patient undergoes two operations, by two different specialties, at the</p>
<p>same time in the same operating room.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Cutoff Time</p>
</blockquote></td>
<td><blockquote>
<p>An institution might have a daily cutoff time for entering requests. After the cutoff time, the user is prohibited from booking a request for an operation to take place through midnight of the following day. The user may still book</p>
<p>requests two or more days in advance.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Outstanding Requests</p>
</blockquote></td>
<td><blockquote>
<p>Requests that have been entered but not scheduled. When the patient name is</p>
<p>entered, the software will list the outstanding requests for this patient.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Screen Server</p>
</blockquote></td>
<td><blockquote>
<p>After the data concerning the operation has been entered, the terminal display device will clear and then present a two-page Screen Server summary. The Screen Server summary organizes the information entered and gives the user</p>
<p>another opportunity to enter or edit data.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Exiting an Option or the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user can type the up-arrow (^) at any prompt to stop the line of questioning and return to the previous level in the routine. To completely exit from the system, the user should continue entering up-arrows.

## Option Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The main options included in this menu are listed below. Each of these options, except the *List Operation Requests* option and *List Scheduled Operations* option, contain submenus. To the left of the option name is the shortcut synonym that the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p><em>Maintain Surgery Waiting List</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Request Operations</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LR</p>
</blockquote></td>
<td><blockquote>
<p><em>List Operation Requests</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p><em>Schedule Operations</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LS</p>
</blockquote></td>
<td><blockquote>
<p><em>List Scheduled Operations</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Maintain Surgery Waiting List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROWAIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options within the *Maintain Surgery Waiting List* menu allow surgeons to develop waiting lists for selected surgery specialties. The patient can remain on the Waiting List until sufficient information is available to book the operation for a specific date (see *Make a Request from the Waiting List* option).

> ![](surgery-version-3-user-manual-updated-sr-3-184/006.png) This option is locked with the SROWAIT key.

> The *Maintain Surgery Waiting List* menu contains the following options. To the left is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p><em>Print Surgery Waiting List</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>E</p>
</blockquote></td>
<td><blockquote>
<p><em>Enter a Patient on the Waiting List</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p><em>Edit a Patient on the Waiting List</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Delete a Patient from the Waiting List</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Print Surgery Waiting List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSWL2\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Resident surgeons use the *Print Surgery Waiting List* option to print the waiting list for one or more surgical specialties. The Waiting List includes the names of patients waiting to have an operation and the type of operation. Cases entered on the Waiting List are not assigned an operating room or a date of operation.

> The report can be sorted in several different ways. First, the user can sort the report by one or more surgical specialties. Then, the user can choose to sort the report either alphabetically by patient name, by the tentative date of the operation, or by the date the case was entered on the waiting list. A brief form can be requested, as in Example 1, or a long form report, as in Example 2. The long form report includes the procedure name, comments, referring physician, tentative admission date, patient address, and phone numbers.

> This report has an 80-column format and can be viewed on a software terminal or copied to a printer. When the screen is full the user will be prompted to press the Return key to continue viewing the list.

> Example 1: Print the Surgery Waiting List, Brief Form, Sort By T

> *printout follows*

> Surgery Waiting List for GENERAL (OR WHEN NOT DEFINED BELOW) Printed JUN 28, 2001 at 14:10

> Date Entered Patient Operative Procedure

> ================================================================================ JAN 19, 2001 SURPATIENT,FIVE Bunionectomy

> Tentative Admission: JAN 23, 2001 Tentative Date of Operation: JAN 23, 2001

> JAN 21, 2001 SURPATIENT,SIX REPAIR INGUINAL HERNIA

> Tentative Admission: JAN 28, 2001 Tentative Date of Operation: JAN 29, 2001

> NOV 29, 1999 SURPATIENT,SEVEN ARTHROSCOPY, RIGHT SHOULDER

> Tentative Admission: DEC 29, 1999

> Tentative Date of Operation: None Specified

> Example 2: Print the long form, Sort by D

#### printout follows 

> Surgery Waiting List for GENERAL (OR WHEN NOT DEFINED BELOW) Printed JAN 20, 2001 at 14:11

> ================================================================================ Patient: SURPATIENT,SEVEN (000-84-0987)

> Date Entered: DEC 28, 2001 09:08 Procedure: ARTHROSCOPY, RIGHT SHOULDER

> Tentative Admission Date: JAN 29, 2001

> Home Phone: (555) 555-5877 Work Phone: NOT ENTERED Address:

> Referring Physician/Institution:

> DR. SURSURGEON Phone: 555-555-0987

> 122 1ST AVE.

> TUSCALOOSA, ALABAMA 35205

> Patient: SURPATIENT,FIVE (000-58-7963)

> Date Entered: JAN 19, 2001 15:17 Procedure: Bunionectomy

> Tentative Admission Date: JAN 23, 2001 Tentative Date of Operation: JAN 23, 2001

> Home Phone: NOT ENTERED Work Phone: NOT ENTERED Address:

> Referring Physician/Institution:

> Four Sursurgeon Phone:

> Sylacauga OPC

> Patient: SURPATIENT,SIX (000-09-8797)

> Date Entered: JAN 21, 2001 13:48 Procedure: REPAIR INGUINAL HERNIA

> Tentative Admission Date: JAN 28, 2001 Tentative Date of Operation: JAN 29, 2001

> Comments:

> Bland Diet

> Home Phone: 555-555-1233 Work Phone: NOT ENTERED Address: 117TH SO 40TH ST

> BIRMINGHAM, ALABAMA 35217

> Referring Physician/Institution:

> SURSURGEON Phone: 555-555-8900

> Jefferson OPC

## Enter a Patient on the Waiting List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROW-ENTER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Resident surgeons use the *Enter a Patient on the Waiting List* option to enter a patient on the waiting list for a selected surgical specialty.

> First, identify the surgical specialty to which the patient will be assigned. To add a new case to the waiting list, the user must enter the patient name and the procedure name. Comments, referring physician name and address, tentative admission date, and tentative operation date can also be added. This information will appear on the *Waiting List Report*. Patient names stay on the Waiting List until the data is used to make a request or until it is deleted.

> Example: Enter a Patient on the Waiting List

> Select Maintain Surgery Waiting List Option: E Enter a Patient on the Waiting List

## Edit a Patient on the Waiting List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROW-EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Edit a Patient on the Waiting List* option is used to edit information collected for a patient who is already on the waiting list. The user enters the patient's name first. The user should be certain that the correct patient has been entered and that the right entry (there can be more than one) has been selected. Information can then be updated by simply typing in the new data at each prompt. If there is no change for a response, press the \<Enter\> key and the cursor will go to the next prompt.

> This option allows changes to the procedure name, the referring physician information, comments, tentative admission date, and/or the tentative operation date. A patient's name cannot be edited. A patient's name will stay on the Waiting List until the data is used to make a request or until it is deleted.

> Example: Edit Waiting List

> Select Maintain Surgery Waiting List Option: U Edit a Patient on the Waiting List

## Delete a Patient from the Waiting List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROW-DELETE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Delete a Patient from the Waiting List* option is used to delete a patient's procedure from the Surgery Waiting List. Enter the patient's name and select the procedure from the list of procedures and his or her entry will be deleted. The software will provide a message that the procedure has been deleted.

> Example: Delete Patient From Waiting List

> Select Maintain Surgery Waiting List Option: D Delete a Patient from the Waiting List

> *(This page included for two-sided copying.)*

# Request Operations Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROREQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Request Operations* menu contains several functions that the surgeons and resident surgeons use to book an operation. Options within the *Request Operations* menu are used to book an operation for a certain day. The surgeon can request, via the software, the operation(s) for a patient on a specific day and then enter additional information concerning the upcoming operation.

> ![](surgery-version-3-user-manual-updated-sr-3-184/007.png) This option is locked with the SROREQ key.

> To request an operation, the user must have a patient name, an operative procedure to perform, and a date to book it. Also required are the Surgeon, Surgical Specialty, and the Indications for Operations. If the user does not know the anticipated date of surgery, the user can enter the patient on the Waiting List. If there is enough information to book the operation for a specific time and operating room, the user can use the *Schedule Unrequested Operations* option on the *Schedule Operation* menu to schedule the operation.

> The information gathered is collated by the software and used to produce reports. The person in charge of scheduling (scheduling manager) arranges the operation requests according to the hospital's Surgical Service protocols and schedules the operation by assigning the case an operating room and a time slot.

> The options included in the *Request Operations* menu option are listed below. To the left of the option name is the shortcut character(s) the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Display Availability</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Make Operation Requests</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Delete or Update Operation Requests</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>W</p>
</blockquote></td>
<td><blockquote>
<p><em>Make a Request from the Waiting List</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CC</p>
</blockquote></td>
<td><blockquote>
<p><em>Make a Request for Concurrent Cases</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>V</p>
</blockquote></td>
<td><blockquote>
<p><em>Review Request Information</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation Requests for a Day</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WR</p>
</blockquote></td>
<td><blockquote>
<p><em>Requests by Ward</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Display Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRODISP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Display Availability* option is used to check on the availability of an operating room before booking an operation. This option allows the user to view the availability of operating rooms on a blockout graph. This screen is "read-only" with no editing capabilities.

> Scheduled operations display on the graph as an equal sign (=) followed by the letter X. The equal sign before the X indicates the beginning of a scheduled operation. Surgical specialty blockouts are indicated by an abbreviation for the service (for more information on service blockouts, a function of the Scheduling menu, see the *Create Service Blockouts* option).

> After entering this option, the user has a choice of viewing the room availability on the blockout graph in two ways. The user can either view all rooms for a particular date (as in Example 1) or view a particular operating room for a range of dates (Example 2). Notice, in the first example, that the user can also list requests, if any have been made.

> Condensed Characters

> If the display terminal can print condensed characters, a 24-hour graph will display on the screen. If not, the user will be prompted to select one of three graphs representing different chunks of that day.

> Example 1: All O.R.S For One Day

> Select Request Operations Option: A Display Availability

> Example 2: One O.R. for a Date Range

## Make Operation Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROOPREQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Make Operation Requests* option allows the resident surgeon or scheduling manager to request an operation for a patient on a specific day. To request an operation the user must know the patient name, the operative procedure to be performed, and the date on which to book the procedure.

> This option also asks for detailed information concerning the upcoming operation. First, the user will be prompted to enter required information, including the Date of Operation, Surgeon, Surgical Specialty, Principal Procedure, and indications for the operation. Facilities can set up additional required fields using the *Surgery Site Parameters (Enter/Edit)* option within the *Surgery Package Management* menu. Then, the user will be prompted to enter procedure information, such as the estimated case length, blood product information, and other information about the operation.

> The user should enter as much information as possible when making the request. Later, more information can be added or corrections can be made by using the *Delete or Update Operation Requests* option.

> About Outstanding Requests

> When the patient name is entered, the software will list any requests that have been made but not scheduled. These requests are called outstanding requests. If the user discovers that the request being entered has already been made, he or she should respond YES to the prompt "Do you want to update the outstanding request? " Answering YES allows the user to view the information and make changes (see the following example).

> If the user is entering a new, separate request for the same patient, he or she should respond NO to this prompt.

> Example: Making an Operation Request

> Prompts that require a response before the user can continue with the option include the following.

> "Make a Request for which Date ?" "Primary Surgeon:"

> "Attending Surgeon:" "Surgical Specialty:"

> "Principal Operative Procedure:" "Principal Preoperative Diagnosis:"

> Entering Preoperative Information

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>At this prompt:</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>The user should do this:</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Principal Preoperative Diagnosis</p>
</blockquote></td>
<td><blockquote>
<p>Type in the reason this procedure is being performed. The user must enter information into this field prompt before the option can be completed. The information entered in this field will automatically populate the Indications for Operations field, which can be edited through the Screen Server.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Planned Principal Procedure Code (CPT)</p>
</blockquote></td>
<td><blockquote>
<p>Type in the Current Procedural Terminology (CPT) identifying code for each procedure. If the code number is not known, the user can enter the type of operation (i.e., appendectomy) or a body organ and select from a list of codes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Estimated Case Length (HOURS:MINUTES)</p>
</blockquote></td>
<td><blockquote>
<p>Either accept the default answer by pressing the <strong>&lt;Enter&gt;</strong> key, or enter a number for the length of time needed for this procedure. If a CPT Code is entered, the software will display the average length of time for the procedure based on the Surgical Specialty and CPT Code.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Brief Clinical History</p>
</blockquote></td>
<td><blockquote>
<p>This information will display on the Tissue Examination Report. It should contain any information relevant to the specimens being sent to the laboratory. This is a word-processing field.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### chart continues 

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>At this prompt:</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>The user should do this:</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Select REQ BLOOD KIND</p>
</blockquote></td>
<td><blockquote>
<p>Enter the type of blood product that will be needed for the operation.</p>
<p>The package coordinator can select a default response to this prompt when installing the package. If the default product is not what is wanted for a case, it can be deleted by entering the at-sign (@) at this prompt. The user can then select the preferred blood product (enter two question marks for a list of blood products).</p>
<p>If no blood products are needed, do not enter <strong>NO</strong> or <strong>NONE</strong>. Instead, press the <strong>&lt;Enter&gt;</strong> key to bypass this prompt.</p>
<p>To order more than one product for the same case, use the screen server summary that concludes the option and select item 9, REQ BLOOD KIND. This is a multiple field; as many blood products as needed may be entered.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Requested Preoperative X-Rays</p>
</blockquote></td>
<td><blockquote>
<p>Enter the types of preoperative x-ray films and reports required for delivery to the operating room before the operation. This field may be left blank if the user does not intend to order any x-ray products.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Preoperative Infection</p>
</blockquote></td>
<td><blockquote>
<p>Enter the letter code "<strong>C</strong>" for clean or "<strong>D</strong>" for contaminated or "S" for 'SPECIAL CONSIDERATIONS' or type in the first few letters of either word. This information allows the scheduling manager to determine how</p>
<p>much time is needed between operations for sanitizing a room.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example: Make Operation Requests

> Select Request Operations Option: R Make Operation Requests

> After entering the request information, the Screen Server redisplays all fields, providing an opportunity to the user to update the information.

> Service Classifications

> The Surgery software allows the user to associate a patient's Service Classification status when entering or editing a surgical case or Non-OR procedure. Service Classifications can be designated for a surgical case *only* if the veteran is first registered with these designations.

> The Service Classifications that the user selects for the case also apply to the principal diagnosis.

> ![](surgery-version-3-user-manual-updated-sr-3-184/008.png) These classifications default to each Other Postop Diagnosis as they are added to the case.

### Updating an Operation Request with Service Classification Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the user selects the patient and enters the required data, a screen displays with questions about the Service Classifications.

> ![](surgery-version-3-user-manual-updated-sr-3-184/009.png)If the patient is not enrolled, or his/her status is not populated in enrollment, the software displays the text "*SC/NSC status not found, N will be defaulted into all SC/EI categories*." The software defaults N into all Service Connected/Environmental Indicator fields related to the case.

> If the user changes the SC/EI classifications at the case level, the software prompts the user with the message *"Update all 'OTHER POSTOP DIAGNOSIS' Eligibility and Service Connected Conditions with these values?"*

> The following example depicts Service Classification status change when the user updates a case.

> The user can also edit diagnosis classification status individually using the *Surgeon's Verification of Diagnosis & Procedures* option or the *Update/Verify Procedure/Diagnosis Codes* option.

> Example: Make an Operation Request with Service Classification Information

## Delete or Update Operation Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSUPRQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Delete or Update Operation Requests* option is used to delete a request, to update information, or to change the date of a requested operation. When a user enters this option and selects a patient's name and case, he or she can choose one of the three functions. The three functions are explained below and the next few pages contain examples of how to use them.

> The prompts differ for concurrent cases (operations performed by two different specialties at the same time on the same patient), as illustrated in Examples 4, 5, and 6. Whenever a user makes a change or updates information for one of the concurrent cases, the software wants to know if the other case is affected.

> The three functions available in this option are also available in the *Request Operations* option when the user selects an outstanding request.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>With this function:</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>The user can:</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Delete</p>
</blockquote></td>
<td><blockquote>
<p>Permanently remove an operation request from the software files (Examples 1 and 4). Example 4 shows the deletion of one operation in a set of</p>
<p>concurrent cases.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Update Request Information</p>
</blockquote></td>
<td><blockquote>
<p>Change the length of the operation and edit other data fields that were entered earlier (Example 2). The software can automatically update each case in a set</p>
<p>of two concurrent cases (Example 5).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Change the Request Date</p>
</blockquote></td>
<td><blockquote>
<p>Alter the operation date of the request (Examples 3 and 6). For a set of</p>
<p>concurrent cases to remain concurrent, the user must change the request date for both operations (Example 6).</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example 1: Delete a Request

> Example 2: Update Request Information

> Example 3: Change the Request Date

> Deleting or Updating Requests for Concurrent Cases

> Any changes made to one concurrent case can affect the other case. When one of the concurrent cases is deleted, a prompt will ask if the user wishes to delete the other case also. If the user responds with NO, the remaining operation will stay in the records as a single case. When the user changes the date of one operation of a concurrent case, the user must simultaneously change the date for the other operation, otherwise the operations will no longer be considered concurrent.

> When updating a response to a prompt or group of related prompts, the software will ask if the user wants to store (meaning duplicate) the information in the other case. This saves time by storing the information into the other case so that it does not have to be entered again. If the user does not want the prompt response duplicated for the other case, enter N or NO.

> Example 4: Delete a Request for Concurrent Cases

> Example 5: Update Request Information for a Concurrent Case

> Example 6: Change the Request Date of Concurrent Cases

## Make a Request from the Waiting List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSWREQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Make a Request from the Waiting List* option uses data from the Waiting List to make an operation request. It can save time by moving data from the Waiting List to the request (simultaneously removing it from the waiting list). As with any request, a date for the surgery is required.

> After the user enters the patient name, the software will list any operations on the Waiting List for that patient. The user then selects the operative procedure wanted. The software will advise if the patient selected has any outstanding requests.

> Each institution might have a daily cutoff time for entering requests. After the cutoff time for a particular day, the users are prohibited from booking a request for an operation to take place through midnight of that day.

> When a request is made, the user is asked to provide preoperative information about the case. It is best to enter as much information as available.

> Example: Making A Request From the Waiting List

## Make a Request for Concurrent Cases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSREQCC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Make a Request for Concurrent Cases* option is used to book concurrent operations. Concurrent cases are two operations performed on the same patient by different surgical specialties simultaneously, or

> back-to-back in the same room. A request may be made for each case at one time with this option. As usual, whenever a request is entered, the user is asked to provide preoperative information about the case. It is best to enter as much information as possible and update it later if necessary.

> Mandatory Prompts

> After the patient name has been entered, the user will be prompted to enter some required information about the first case (the mandatory prompts include the date of operation, procedure, surgeon and attending surgeon, principal preoperative diagnosis, and time needed). If a mandatory prompt is not answered, the software will not book the operation and will return the user to the *Request Operations* menu. After answering the prompts for the first case, the user is prompted to answer the same questions about the second case. Then, the software will provide a message that the two requests have been entered and simultaneously prompt the user to select one of the cases for entering detailed information. If the user does not want to enter detailed preoperative information at this time, pressing the \<Enter\> key will send the user to the *Request Operations* menu. In Example 1, detailed information is entered for the first case only.

> Storing the Request Information

> After most prompts, the software will ask if the user wants to store (meaning duplicate) this information in the concurrent, or other, case. This saves time by storing the information into the other case so that information does not have to be entered again. If the user does not want the prompt response duplicated for the other case, he or she should enter N or NO.

> Finally, the software will display the Screen Server summary and store any duplicated information into the other case. At this point, the software will provide another message that the two requests have been entered and again prompt the user to select either case for entering detailed information. This whole process may be repeated with the other case by selecting the number for it, or pressing the \<Enter\> key to get back to the *Request Operations* menu.

> Updating the Preoperative Information Later

> Use the *Delete or Update Operation Requests* option to change or update any of the information entered for either or both concurrent cases (Example 2).

> Example 1: Make a Request for Concurrent Cases

> Planned Principal Procedure Code: 35526 REPAIR OF ANOMALOUS CORONARY ARTERY FROM PULMONARY

> ARTERY ORIGIN; BY LIGATION

> BYPASS GRAFT, WITH VIEN; AORTOSUBCLAVIAN, AORTOINNOMINATE, OR AORTOCAROTID

> Example 2: Update Request Information for a Concurrent Case

## Review Request Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROREQV\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgeons and nurses use the *Review Request Information* option to edit or review the preoperative information that was entered when the case was requested. This option can be accessed after the case has been scheduled.

> Example: Review Request Information

## Operation Requests for a Day

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROP REQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operation Requests for a Day* option allows the scheduling manager to display or print a list of operation requests. The information from all surgical requests is collected by the software and made available by date. There are no editing capabilities for this feature. The user has a choice of printing a cursory short form or a long form encompassing all the request fields.

> This report prints in an 80-column format and can be viewed on the screen.

> Example 1: Print Operation Requests for a Day, Short Form

> *printout follows*

> OPERATION REQUESTS FOR GENERAL(OR WHEN NOT DEFINED BELOW) 03/15/99

1.  Case Number: 173 Operation Date: 03/15/99 Patient: SURPATIENT,TWENTY Ward:

> ID#: 000-45-4886 Surgeon: SURSURGEON,ONE Procedure: CHOLECYSTECTOMY (URGENT ADD TODAY)

> Estimated Case Length: 2:30 Requested Anesthesia: GENERAL

2.  Case Number: 180 Operation Date: 03/15/99 Patient: SURPATIENT,FOURTEEN Ward: 1 SOUTH ID#: 000-45-7212 Surgeon: SURSURGEON,TWO Procedure: REPAIR DIAPHRAGMATIC HERNIA (STANDBY)

> Estimated Case Length: 2:00 Requested Anesthesia: GENERAL

> Press RETURN to continue \<Enter\>

> Example 2: Long Form

#### printout follows 

> ============================================================================== OPERATION REQUESTS FOR GENERAL(OR WHEN NOT DEFINED BELOW)

> ON MAR 15, 1999

> Patient: SURPATIENT,TWENTY ID \#: 000-45-4886

> Age: 51 Ward: NOT ENTERED

> Surgeon: SURSURGEON,ONE Attending: SURSURGEON,ONE Preoperative Diagnosis: CHOLELITHIASIS

> Principal Procedure: CHOLECYSTECTOMY

> Other Procedures: INTRAOPERATIVE CHOLANGIOGRAM Estimated Case Length: 2:30

> Req. Anesthesia Technique: GENERAL

> Blood Requested: CPDA-1 WHOLE BLOOD UNITS

> FRESH FROZEN PLASMA, CPDA-1 2 UNITS

> Restraints: SAFETY STRAP

> Requested by: SURNURSE,ONE on JAN 7, 1999 13:45

> Press \<Enter\> to continue, or '^' to quit: \<Enter\>

> ============================================================================== OPERATION REQUESTS FOR GENERAL(OR WHEN NOT DEFINED BELOW)

> ON MAR 15, 1999

> Patient: SURPATIENT,FOURTEEN ID \#: 000-45-7212

> Age: 48 Ward: 1 SOUTH

> Surgeon: SURSURGEON,TWO Attending: SURSURGEON,TWO Preoperative Diagnosis: ACUTE DIAPHRAGMATIC HERNIA

> Principal Procedure: REPAIR DIAPHRAGMATIC HERNIA Estimated Case Length: 2:00

> Req. Anesthesia Technique: GENERAL

> Blood Requested: CPDA-1 WHOLE BLOOD 2 UNITS Restraints: SAFETY STRAP

> Requested by: SURNURSE,ONE on JAN 13, 1999 14:39

> Press RETURN to continue \<Enter\>

## Requests by Ward

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROWRQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users can utilize the *Requests by Ward* option to print request information for patients in all wards or a specific ward. The first prompt asks if the user wants to print the requests for all wards. If not, accept the NO default and the next prompt will ask "Print schedule for which ward?". If the user enters a question mark (?), the help screen will list the ward names from which to choose. Patients not assigned to a ward are listed under the category "Outpatient."

> This report prints in an 80-column format and can be viewed on the screen.

> Example: Print Requests by Ward

> *printout follows*

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Requests for Operations</p>
<p>============================================================================== Ward: 2 WEST</p>
<p>============================================================================== Patient: SURPATIENT,TWELVE (000-41-8719) Case Number: 178</p>
<p>Date of Operation: 03/15/99 Case Order: 1 Requested Anesthesia: GENERAL</p>
<p>Operation(s): CAROTID ARTERY ENDARTERECTOMY</p>
<p>Comments:</p>
<p>Concurrent Case Number: 179</p>
<p>Procedure: AORTO CORONARY BYPASS GRAFT</p>
<p>Comments:</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Patient: SURPATIENT,TWELVE (000-41-8719) Case Number: 179</p>
<p>Date of Operation: 03/15/99 Case Order: 1 Requested Anesthesia: GENERAL</p>
<p>Operation(s): AORTO CORONARY BYPASS GRAFT</p>
<p>Comments:</p>
<p>Concurrent Case Number: 178</p>
<p>Procedure: CAROTID ARTERY ENDARTERECTOMY</p>
<p>Comments:</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Press RETURN to continue or '^' to quit. <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Requests for Operations</p>
<p>==============================================================================</p>
<p>Ward: OUTPATIENT</p>
<p>============================================================================== Patient: SURPATIENT,FIFTEEN (000-98-1234) Case Number: 172</p>
<p>Date of Operation: 03/25/99 Case Order: Requested Anesthesia:</p>
<p>Operation(s): HEMMORHOIDECTOMY</p>
<p>Comments:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Patient: SURPATIENT,TWENTY (000-45-4886) Case Number: 173</p>
<p>Date of Operation: 03/15/99 Case Order: Requested Anesthesia: GENERAL</p>
<p>Operation(s): CHOLECYSTECTOMY, INTRAOPERATIVE CHOLANGIOGRAM</p>
<p>Comments:</p>
</blockquote></td>
<td rowspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient: SURPATIENT,SIXTEEN (000-11-1111) Case Number: 175</p>
<p>Date of Operation: 03/14/99 Case Order: Requested Anesthesia: LOCAL</p>
<p>Operation(s): REMOVE BUNION</p>
<p>Comments:</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
</tr>
</tbody>
</table>

# List Operation Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSRBS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users can use the *List Operation Requests* option to produce a list of requested cases, including cases on the Waiting List. This report sorts by ward or surgical specialty.

> This report prints in an 80-column format and can be viewed on the screen.

> Example 1: List Operation Requests, by Specialty

> *printout follows*

> Operative Requests for GENERAL(OR WHEN NOT DEFINED BELOW)

> Date Patient Ward Location Case Number Operative Procedure

> ========================================================================

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 13%" />
<col style="width: 40%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>APR 180</th>
<th>4, 1999</th>
<th><blockquote>
<p>SURPATIENT,FOUR 000-45-7212 REMOVE MOLE</p>
</blockquote></th>
<th><blockquote>
<p>1 SOUTH</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>JUN 178</td>
<td>1, 1999</td>
<td><blockquote>
<p>SURPATIENT,SEVENTEEN 000-45-5119</p>
<p>REPAIR DIAPHRAGMATIC HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>1 SOUTH</p>
</blockquote></td>
</tr>
<tr class="even">
<td>AUG 145</td>
<td>15, 1999</td>
<td><blockquote>
<p>SURPATIENT,NINE 000-34-5555 CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>1 NORTH</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Press RETURN to continue

> Example 2: List Operation Requests, by Ward

#### printout follows 

> Operative Requests for 1 SOUTH

> Date Patient Surgical Specialty Case Number Operative Procedure

> ========================================================================

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>APR 179</th>
<th><blockquote>
<p>4, 1999</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,FOUR 000-45-7212</p>
<p>ARTHROSCOPY, RIGHT KNEE</p>
</blockquote></th>
<th><blockquote>
<p>ORTHOPEDICS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>APR 180</td>
<td><blockquote>
<p>4, 1999</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,THREE 000-21-2453 REMOVE MOLE</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>JUN 178</td>
<td><blockquote>
<p>1, 1999</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SEVENTEEN 000-45-5119</p>
<p>REPAIR DIAPHRAGMATIC HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>JUN 181</td>
<td><blockquote>
<p>1, 1999</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWELVE 000-41-8719</p>
<p>CAROTID ARTERY ENDARTERECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERAL VASCULAR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>JUN 182</td>
<td><blockquote>
<p>1, 1999</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,NINE 000-34-5555</p>
<p>AORTO CORONARY BYPASS GRAFT</p>
</blockquote></td>
<td><blockquote>
<p>THORACIC SURGERY</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Press RETURN to continue

# Schedule Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROSCHOP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The options contained within the *Schedule Operations* menu are designed to be used by surgeons or the Scheduling Manager to book an operation when the date, time, and operating room are determined. The scheduling manager may schedule an already requested operation using the *Schedule Requested Operation* option. On the other hand, the scheduling manager may book an operation that has not been previously requested if the date, time and operating room are known. In this case, the *Request Operations* option can be skipped and the operation can be scheduled using the *Schedule Unrequested Operations* option.

> ![](surgery-version-3-user-manual-updated-sr-3-184/010.png) This option is locked with the SROSCH key.

> Whether a user is booking a case from the Waiting List, *Request Menu*, *Scheduling Menu*, or as a new surgery, he or she will be asked to provide preoperative information about the case. It is advisable to enter as much information as possible. Later, the information can be updated.

> The information gathered by the *Request Operations* options is collated by the software and used to produce reports. The person in charge of scheduling (scheduling manager) arranges the requests according to the hospital's Surgical Service protocols and schedules the operation by assigning the case an operating room and a time slot. The information gathered by the *Schedule Operations* menu is collated by the software and is used to produce reports for the scheduling manager.

> ![](surgery-version-3-user-manual-updated-sr-3-184/011.png) Local restrictions can be applied to the scheduling of procedures. For example, a facility can require CPT codes be entered before a surgical case is scheduled. The *Surgery Site Parameters* (Enter/Edit) option is used to select required fields.

> The options included in the *Schedule Operation* menu are listed below. To the left of the option name is the shortcut synonym that the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Display Availability</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SR</p>
</blockquote></td>
<td><blockquote>
<p><em>Schedule Requested Operations</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SU</p>
</blockquote></td>
<td><blockquote>
<p><em>Schedule Unrequested Operations</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CON</p>
</blockquote></td>
<td><blockquote>
<p><em>Schedule Unrequested Concurrent Cases</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Reschedule or Update Scheduled Operations</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p><em>Cancel Scheduled Operation</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UC</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Cancellation Reason</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AN</p>
</blockquote></td>
<td><blockquote>
<p><em>Schedule Anesthesia Personnel</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p><em>Create Service Blockout</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DB</p>
</blockquote></td>
<td><blockquote>
<p><em>Delete Service Blockout</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p><em>Schedule of Operations</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Display Availability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRODISP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A user can view the availability of operating rooms on a blockout graph before booking an operation with the *Display Availability* option. A user might also use this option to check a booking or service blockout. This feature is the same as the *Display Availability* option available on the *Request Operations* menu option.

> Scheduled operations show up on the graph as an equal sign (=) followed by the letter X. The equal sign before the X indicates the beginning of a scheduled operation. Surgical specialty blockouts are indicated by an abbreviation for the service. For more information on service blockouts, a function of the scheduling menu, see the *Create Service Blockout* option.

> If the facility has a display terminal that can print condensed characters, a 24-hour graph will display on the screen. If not, the user will be prompted to select one of three graphs representing different chunks of that day.

> Example: Display all O.R.s for One Day

## Schedule Requested Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSCHD1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users utilize the *Schedule Requested Operation* option to schedule a previously requested operation when enough information is available to assign an operating room and time slot. The user will also be prompted to provide anesthesia personnel information. The information entered here is reflected in the Schedule of Operations report. This option is designed for the scheduling manager to expeditiously schedule any or all requests on a specific date.

> First, the user enters the patient to be scheduled. The software will automatically display all requests for that patient. The user then picks the request he or she wishes to schedule and assigns the operating room, beginning and end times, and anesthesia personnel for the case. The user can then choose another patient to schedule, or press the \<Enter\> key to leave the option.

> The prompts that require a response before the user can continue with this option include the following. "Schedule a Case for which Operating Room ?"

> "Reserve from what time ? (24HR:NEAREST 15 MIN):" "Reserve to what time ? (24HR:NEAREST 15 MIN):"

> Scheduling a Concurrent Case

> A concurrent case occurs when a patient undergoes two operations by different surgical specialties simultaneously, or back-to-back in the same operating room. Example 2 demonstrates scheduling a requested concurrent case. When a user schedules a concurrent case, he or she must answer the prompt "There is a concurrent case associated with this operation. Do you want to schedule it for the same time? (Y/N) ". If the answer is NO, the two cases will no longer be considered concurrent. The user can enter anesthesia personnel information for each case.

> ![](surgery-version-3-user-manual-updated-sr-3-184/012.png)The user should allow enough time for both surgeries when he or she answers the prompts, "Reserve from what time ? (24HR:NEAREST 15 MIN):" and "Reserve to what time ? (24HR:NEAREST 15 MIN):".

> Example 1: Schedule a Requested Operation

> Example 2: Schedule Operation for a Concurrent Case

## Schedule Unrequested Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROSRES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users can use the *Schedule Unrequested Operations* option to schedule an operation that has not been requested. To schedule an operation, the user must determine the date, time, and operating room. The information entered in this option is reflected in the Schedule of Operations Report.

> Whenever a new case is booked, the user is asked to provide preoperative information about the case. Enter as much information as possible. Later, the information can be updated or corrected.

> Prompts that require a response before the user can continue with this option are listed below. "Schedule Procedure for which Date ?"

> "Select Patient:"

> "Schedule a case for which operating Room ?"

> "Reserve from what time ? (24HR:NEAREST 15 MIN):" "Reserve to what time ? (24HR:NEAREST 15 MIN):" "Desired Procedure Date:"

> "Primary Surgeon:" "Attending Surgeon:" "Surgical Specialty:"

> "Principal Operative Procedure:" "Principal Preoperative Diagnosis:"

> Entering Preoperative Information

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>At this prompt:</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>The user should do this:</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Planned Principal Procedure Code (CPT)</p>
</blockquote></td>
<td><blockquote>
<p>Enter the Current Procedural Terminology (CPT) identifying code for each procedure. If the code number is not known, the user can enter the type of operation (i.e., appendectomy) or a body organ and select from a list of codes.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Principal Preoperative Diagnosis</p>
</blockquote></td>
<td><blockquote>
<p>Type in the reason this procedure is being performed. The user must enter information into this field prompt before the option can be completed. The information entered in this field will automatically populate the Indications for Operations field,</p>
<p>which can be edited through the Screen Server.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Brief Clinical History</p>
</blockquote></td>
<td><blockquote>
<p>Enter any information relevant to the specimens being sent to the laboratory. This is an open-text word-processing field. This</p>
<p>information will display on the Tissue Examination Report.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select REQ BLOOD KIND</p>
</blockquote></td>
<td><blockquote>
<p>Enter the type of blood product needed for the operation.</p>
<p>If no blood products are needed, do not enter <strong>NO</strong> or <strong>NONE</strong>; instead, press the <strong>&lt;Enter&gt;</strong> key to bypass this prompt.</p>
<p>The package coordinator at each facility can select a default response to this prompt when installing the package. If the default product is not what is wanted for a case, it can be deleted by entering the at-sign (@) at this prompt. Then, the user can select the preferred blood product. (Enter two question marks for a list of blood products.)</p>
<p>To order more than one product for the same case, use the screen server summary that concludes the option. On page two of the summary, select item 7, REQ BLOOD KIND, to enter as many blood products as needed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Requested Preoperative X-Rays</p>
</blockquote></td>
<td><blockquote>
<p>Enter the types of preoperative x-ray films and reports required for delivery to the operating room before the operation. If the user does not intend to order any x-ray products, this field</p>
<p>should be left blank.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Preoperative Infection</p>
</blockquote></td>
<td><blockquote>
<p>Enter the letter code "<strong>C</strong>" for clean or "<strong>D</strong>" for contaminated or "S" for 'SPECIAL CONSIDERATIONS' or type in the first few letters of either word. This information allows the</p>
<p>scheduling manager to determine how much time is needed between operations for sanitizing a room.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example: Schedule an Unrequested Operation

## Schedule Unrequested Concurrent Cases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSCHDC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Schedule Unrequested Concurrent Cases* option is used to schedule concurrent cases that have not been requested. A concurrent case is when a patient undergoes two operations by different surgical specialties simultaneously, or back to back in the same room. The user can schedule both cases with this one option. As usual, whenever the user enters a request, he or she is asked to provide preoperative information about the case. It is best to enter as much information as possible and update it later if necessary.

> Required Prompts

> After the patient name is entered, the user will be prompted to enter some required information about the first case. The mandatory prompts include the date, procedures, surgeon and attending surgeon, principal preoperative diagnosis, and time needed. If a mandatory prompt is not answered, the software will not book the operation and will return the cursor to the *Schedule Operations* menu. After answering the prompts for the first case, the user will be asked to answer the same prompts for the second case. The software will then provide a message stating that the two requests have been entered. The user can then select a case for entering detailed preoperative information. If the user does not want to enter details at this time, he or she should press the \<Enter\> key and the cursor will return to the *Schedule Operations* menu. In the example, detailed information for the first case has been entered.

> Storing the Request Information

> After every prompt or group of related prompts, the software will ask if the user wants to store (meaning duplicate) the answers in the concurrent case. This saves time by storing the information into the other case so that it does not have to be typed again. The software will then display the screen server summary and store any duplicated information into the other case. Finally, the software will inform the user that the two requests have been entered and prompt to select either case for entering detailed information. The user can select a case or press the \<Enter\> key to get back to the *Schedule Operations* menu.

> Updating the Preoperative Information Later

> Use the *Reschedule or Update a Scheduled Operation* option to change or update any of the information entered for either of the concurrent cases.

> Example: Schedule Unrequested Concurrent Cases

## Reschedule or Update a Scheduled Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSCHUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Reschedule or Update a Scheduled Operation* option has three uses: 1) to add a concurrent case, 2) to reschedule an operation for another date, time, and/or operating room, 3) to update the preoperative information that was entered earlier.

> Adding a Concurrent Case (See Example 1)

> After the case is selected, the software will ask whether the user wishes to add a concurrent case. If the response is YES, the software will prompt for information on the second case. To add the case, the user must enter a surgeon and attending surgeon, a surgical specialty, the principal operative procedure, and a principal preoperative diagnosis. The software will then inform the user that the case has been added. The user can then select another case or the same case for entering detailed preoperative information, or the user can press the \<Enter\> key to return to the *Schedule Operations* menu.

> Changing the Date, Time, or Operating Room (See Example 2)

> If a user does not wish to add a concurrent case, the software will prompt to change the date, time or operating room. If the user enters YES, the software will erase the old date, time, and operating room and prompt to re-enter this information. The user will be prompted to select a new date, but if the \<Enter\> key is pressed, the software will default to the original date and allow the user to change the room and time. The software supplies a blockout graph to help with rescheduling.

> ![](surgery-version-3-user-manual-updated-sr-3-184/013.png)If the user attempts to reschedule a case after the schedule close time for the date of operation, only the time, and not the date, can be changed.

> Updating the Preoperative Info (See Example 3)

> To update the preoperative information that was entered earlier, the user should respond NO to the prompt asking if the user wishes to change the date, time or operating room. The terminal display screen will clear and present a two-page Screen Server summary. Any of the data fields may be changed, as in Example 2.

> ![](surgery-version-3-user-manual-updated-sr-3-184/014.png)Example 3 also shows the user how to order more than one blood product for a case.

> Example 1: How to Add a Concurrent Case to a Scheduled Operation

> Example 2: How to Reschedule an Operation, Change the Date, Time, or Operating Room

> Example 3: How to Update a Scheduled Operation

## Cancel Scheduled Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSCAN\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a scheduled operation is cancelled, the *Cancel Scheduled Operation* option will remove that case from the list of scheduled operations. <span id="_bookmark41" class="anchor"></span>A cancellation will remain in the system as a cancelled case and will be used in computing the facility's cancellation rate.

> Enter the patient name and select the operation to be deleted from the choices listed. The "Primary Cancellation Reason:" prompt is a mandatory prompt. Enter a question mark for a list of primary cancellation reasons from which to select. If a mistake is made, or the user finds out later that the primary cancellation reason was not correct, the *Update Cancellation Reason* option allows the primary cancellation reason to be edited.

> If there is a concurrent case associated with the operation being cancelled, the software will ask if the user wants to cancel it also.

> Example 1: Cancel a Single Scheduled Operation

> Example 2: Cancel a Scheduled Concurrent Case

## Update Cancellation Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSUPC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Cancellation Reason* option is used to update the cancellation date and reason previously entered for a selected surgical case.

> Example: Update Cancellation Reason

## Schedule Anesthesia Personnel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSCHDA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Schedule Anesthesia Personnel* option allows anesthesia staff to assign, or change, anesthesia personnel for surgery cases. The scheduling manager may have already assigned some personnel to a case using other menu selections. For the user's convenience, the software will default to any previously entered data.

> ![](surgery-version-3-user-manual-updated-sr-3-184/015.png)This option is locked with the SROANES key and will not appear on the menu if the user does not have this key.

> This option is used to enter the names of the principal anesthetist, the supervisor, and anesthesia techniques for cases scheduled on a specific date. The user should first enter the date, and then select an operating room. The software will display all cases scheduled in that room. After scheduling personnel for any or all cases in one operating room, the user can do the same for other operating rooms without leaving this option.

> ![](surgery-version-3-user-manual-updated-sr-3-184/016.png) This option also appears on the *Anesthesia* menu.

> Example: Schedule Anesthesia Personnel

<table>
<colgroup>
<col style="width: 58%" />
<col style="width: 6%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Scheduled Operations for OR2</p>
<p>Case # 14 Patient: SURPATIENT,THREE From: 13:00 To: 18:00</p>
<p>SHOULDER ARTHROPLASTY</p>
<p>Requested Anesthesia Technique: GENERAL// <strong>&lt;Enter&gt;</strong></p>
<p>Principal Anesthetist: SURANESTHETIST,ONE// <strong>&lt;Enter&gt;</strong> OS 112G Anesthesiologist Supervisor: <strong>SURANESTHETIST,TWO</strong> TS</p>
<p>Press RETURN to continue, or '^' to quit <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Would you like to continue with another operating room ?</p>
<p>Schedule Anesthesia Personnel for which Operating Room ?</p>
</blockquote></td>
<td><blockquote>
<p>YES//</p>
<p><strong>OR1</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>There are no cases scheduled for this operating room. Press RETURN to continue <strong>&lt;Enter&gt;</strong></p>
<p>Would you like to continue with another operating room ?</p>
</blockquote></td>
<td><blockquote>
<p>YES//</p>
</blockquote></td>
<td><blockquote>
<p><strong>N</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Create Service Blockout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSBOUT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At times, the surgical staff may need to set aside an operating room for a particular service on a recurring basis. The *Create Service Blockout* option is used by the scheduling manager to blockout the operating room(s) on a graph.

> The resulting service blockout is automatically charted on a graph that can be viewed from the *Display Availability* option. This service blockout does not restrict the operating room to the service, but can assist the scheduling manager when assigning operating rooms.

> The scheduling manager can create the service blockouts by following the example provided on the following page. The required data fields are listed in the following table.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>At this prompt:</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>The user should do this:</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>For what service?</p>
</blockquote></td>
<td><blockquote>
<p>Enter a three or four letter abbreviation for the surgical service the room is being reserved (for example, card for cardiology, gen for general surgery).</p>
<p>Do not use the letter X or an equal sign (=).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Operating Room</p>
</blockquote></td>
<td><blockquote>
<p>Enter the operating room name or code. The operating room must already exist in the HOSPITAL LOCATION file and the OPERATING ROOM file. The user should enter a question mark to get a list of operating rooms already included in these files. The supervisor or package coordinator can add an</p>
<p>operating room to these files.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select Starting Date</p>
</blockquote></td>
<td><blockquote>
<p>The user should enter the date for the blockout to begin.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reserve from what time?</p>
</blockquote></td>
<td><blockquote>
<p>Enter the times for which this room will be blocked-out for a particular service. A room may be reserved at any time during the 24-hour cycle to the</p>
<p>nearest 15 minutes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Reserve to what time?</p>
</blockquote></td>
<td><blockquote>
<p>Enter the end time for the service blockout.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example: Create a Service Blockout

> After the service blockout has been created, it will appear on the operating room availability graph display, as shown below.

## Delete Service Blockout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSBDEL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following example shows how to remove a service blockout from the blockout graph. A service blockout can be deleted for just one date or for all the reserved dates.

> After starting this option, if the user decides not to delete a service blockout, he or she can enter an up- arrow (^) to exit.

> Example: Delete Service Blockout

## Schedule of Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROSCH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Schedule of Operations* option generates the Operating Room Schedule used by the OR nurses, surgeons, anesthetists and other hospital services. The report lists operations and patients scheduled for a particular date. It sorts by operating room and includes the procedure(s), blood products requested, and any preoperative x-rays requested. The schedule also provides anesthesia information and surgeon names.

> This report has a 132-column format and is designed to be copied to a printer.

> ![](surgery-version-3-user-manual-updated-sr-3-184/017.png)By setting up default printers in the SURGERY SITE PARAMETERS file, this report can be queued to print in various locations simultaneously. Please see "Chapter 5: Managing the Software Package" for more information.

> Example: Print Schedule of Operations

> *printout follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE

> SCHEDULE OF OPERATIONS SIGNATURE OF CHIEF: DR. ONE SURSURGEON

PRINTED: SEP 07, 1999 11:12 FOR: SEP 08, 1999

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 31%" />
<col style="width: 27%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>DISPOSITION</p>
</blockquote></th>
<th><blockquote>
<p>PREOPERATIVE DIAGNOSIS</p>
</blockquote></th>
<th><blockquote>
<p>REQ ANESTHESIA</p>
</blockquote></th>
<th><blockquote>
<p>SURGEON</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID#</p>
</blockquote></td>
<td><blockquote>
<p>AGE START TIME</p>
</blockquote></td>
<td><blockquote>
<p>OPERATION(S)</p>
</blockquote></td>
<td><blockquote>
<p>ANESTHESIOLOGIST</p>
</blockquote></td>
<td><blockquote>
<p>FIRST ASST.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td><blockquote>
<p>END TIME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>PRIN. ANESTHETIST</p>
</blockquote></td>
<td><blockquote>
<p>ATT SURGEON</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ==================================================================================================================================== OPERATING ROOM: OR1

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 4%" />
<col style="width: 10%" />
<col style="width: 32%" />
<col style="width: 23%" />
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,ONE</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>WARD</p>
</blockquote></th>
<th><blockquote>
<p>CARPAL TUNNEL SYNDROME</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th></th>
<th>SURSURGEON,</th>
<th>O</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-44-7629</p>
</blockquote></td>
<td><blockquote>
<p>46</p>
</blockquote></td>
<td><blockquote>
<p>07:30</p>
</blockquote></td>
<td><blockquote>
<p>REVISE MEDIAN NERVE</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>F</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TO BE ADMITTED</p>
<p>Case # 143</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>09:30</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>O</td>
</tr>
</tbody>
</table>

> PREOPERATIVE XRAYS: CARPAL TUNNEL, R WRIST

> OPERATING ROOM: OR2

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 30%" />
<col style="width: 26%" />
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,FOURTEEN</p>
</blockquote></th>
<th><blockquote>
<p>WARD</p>
</blockquote></th>
<th><blockquote>
<p>CHOLELITHIASIS</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th></th>
<th>SURSURGEON,</th>
<th>O</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-45-7212 48</p>
</blockquote></td>
<td><blockquote>
<p>06:30</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>T</td>
</tr>
<tr class="even">
<td><blockquote>
<p>HICU 212-B</p>
</blockquote></td>
<td><blockquote>
<p>08:00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>O</td>
</tr>
</tbody>
</table>

> Case \# 141 REQUESTED BLOOD COMPONENTS: TYPE & CROSSMATCH CPDA-1 RED BLOOD CELLS - 2 UNITS

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 35%" />
<col style="width: 20%" />
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></th>
<th><blockquote>
<p>WARD</p>
</blockquote></th>
<th><blockquote>
<p>ACUTE DIAPHRAGMATIC HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th></th>
<th>SURSURGEON,</th>
<th>T</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-41-8719 71</p>
</blockquote></td>
<td><blockquote>
<p>08:00</p>
</blockquote></td>
<td><blockquote>
<p>REPAIR DIAPHRAGMATIC HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>O</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TO BE ADMITTED</p>
<p>Case # 142</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>09:30</p>
<p>REQUESTED BLOOD COMPONENTS: TYPE &amp; CROSSMATCH CPDA-1 RED BLOOD CELLS - 2 UNITS</p>
<p>PREOPERATIVE XRAYS: ABDOMEN</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>T</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,THIRTY</p>
</blockquote></td>
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td><blockquote>
<p>CAROTID ARTERY STENOSIS</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
<td></td>
<td>SURSURGEON,</td>
<td>O</td>
</tr>
<tr class="even">
<td><blockquote>
<p>000-82-9472 48</p>
</blockquote></td>
<td><blockquote>
<p>11:15</p>
</blockquote></td>
<td><blockquote>
<p>CAROTID ARTERY ENDARTERECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>F</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TO BE ADMITTED</p>
</blockquote></td>
<td><blockquote>
<p>16:00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>O</td>
</tr>
</tbody>
</table>

> \*\* Concurrent Case \#157 AORTO CORONARY BYPASS GRAFT

> Case \# 150 REQUESTED BLOOD COMPONENTS: TYPE & CROSSMATCH CPDA-1 RED BLOOD CELLS - UNITS NOT ENTERED CPDA-1 WHOLE BLOOD - 2 UNITS

> PREOPERATIVE XRAYS: DOPPLER STUDIES

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 3%" />
<col style="width: 11%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,THIRTY</p>
</blockquote></th>
<th><blockquote>
<p>WARD CORONARY ARTERY DISEASE</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th></th>
<th>SURSURGEON,</th>
<th>T</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-82-9472 48</p>
</blockquote></td>
<td><blockquote>
<p>11:15 AORTO CORONARY BYPASS GRAFT</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>F</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TO BE ADMITTED</p>
<p>Case # 157</p>
</blockquote></td>
<td><blockquote>
<p>16:00</p>
<p> Concurrent Case #150 CAROTID ARTERY ENDARTERECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,</p>
</blockquote></td>
<td><blockquote>
<p>O</p>
</blockquote></td>
<td>SURSURGEON,</td>
<td>T</td>
</tr>
</tbody>
</table>

> TOTAL CASES SCHEDULED: 5

> *(This page included for two-sided copying.)*

# List Scheduled Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSCD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *List Scheduled Operations* option provides a short form listing of scheduled cases for a given date. It will sort by surgical specialty, operating room, or ward location.

> This report is in 80-column format and can be viewed on the screen.

> Example: List Scheduled Operations

> *printout follows*

# Chapter Two: Tracking Clinical Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark50" class="anchor"></span>Introduction

> The options described in this chapter provide on-line access to medical administration and laboratory information and provide tracking of operative procedures. They allow the following:

- Entry of information specific to an individual surgical case (for example, staff, times, diagnoses, complications, anesthesia).
- On-line entry of data inside the operating room during the actual operative procedure.
- Generation of patient records and reports.

> <span id="_bookmark51" class="anchor"></span>Key Vocabulary

> The following terms are used in this chapter.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Concurrent Case</p>
</blockquote></td>
<td><blockquote>
<p>The patient undergoes two operations, by two different specialties, at the</p>
<p>same time in the same operating room.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Screen Server</p>
</blockquote></td>
<td><blockquote>
<p>After the data concerning the operation has been entered, the terminal display device will clear and then present a two-page Screen Server summary. The Screen Server summary organizes the information entered and gives the user</p>
<p>another opportunity to enter or edit data.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Exiting an Option or the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user should enter an up-arrow (^) to stop what he or she is currently doing. The user can use the up- arrow at almost any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering up-arrows to completely exit the system.

## Option Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The main options included in this chapter are listed in the following table. The *Operation Menu* option, *Anesthesia Menu* option, and the *Non-O.R.. Procedures* menu contain submenus. To the left of the option name is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation Menu</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Menu</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PO</p>
</blockquote></td>
<td><blockquote>
<p><em>Perioperative Occurrences Menu</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NON</p>
</blockquote></td>
<td><blockquote>
<p><em>Non-O.R. Procedures</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p><em>Comments</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Operation Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROPER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operation Menu* provides operating room personnel with on-line access to medical administration and laboratory information and generates post-operative reports, including the Nurse Intraoperative Report and the Operation Report. The menu options provide the opportunity to delete, edit, or review a patient's operation history or to enter information concerning a new surgery. The *Operation Menu* allows the user to select an area on which to concentrate data entry or review, such as post operation or anesthesia information. It is designed for operating room nurses, surgeons, and anesthetists to use before, during, and after surgery. The Screen Server utility is used extensively to provide quick access to relevant information.

> ![](surgery-version-3-user-manual-updated-sr-3-184/018.png) This option is locked with the SROPER key.

> The *Operation Menu* contains the following options. To the left is the keyboard shortcut the user can enter to select the option. A restricted option, such as the *Anesthesia Menu*, will not display if the user does not have security clearance for that option.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation Information</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SS</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgical Staff</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OS</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation Startup</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PO</p>
</blockquote></td>
<td><blockquote>
<p><em>Post Operation</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PAC</p>
</blockquote></td>
<td><blockquote>
<p><em>Enter PAC(U) Information</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OSS</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation (Short Screen)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>V</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgeon's Verification of Diagnosis &amp; Procedures</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Menu</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AR</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Report</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NR</p>
</blockquote></td>
<td><blockquote>
<p><em>Nurse Intraoperative Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TR</p>
</blockquote></td>
<td><blockquote>
<p><em>Tissue Examination Report</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Enter Referring Physician Information</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RP</p>
</blockquote></td>
<td><blockquote>
<p><em>Enter Irrigations and Restraints</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p><em>Medications (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AB</p>
</blockquote></td>
<td><blockquote>
<p><em>Abort/Cancel Operation</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p><em>Blood Product Verification</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark55" class="anchor"></span>Using the Operation Menu Options

> This section provides information on the following:

- accessing the *Operation Menu* option
- entering information
- reviewing information
- deleting a surgery case
- entering a new surgical case

> Accessing the Operation Menu

> To use one of the *Operation Menu* options, the user must first identify the patient and case on which he or she is currently working. When the *Operation Menu* option is selected, the user will be prompted to enter a patient name. The software will then list all the cases on record for the patient, including scheduled or requested cases and any operations that have been started or completed. Each case will have one of the following designations.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Designation</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>REQUESTED</p>
</blockquote></td>
<td><blockquote>
<p>The procedure is booked for a particular day but the time of surgery and the</p>
<p>operating room are not yet confirmed.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SCHEDULED</p>
</blockquote></td>
<td><blockquote>
<p>The procedure is booked for both an operating room and a day, and the starting</p>
<p>time of the surgery is scheduled.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NOT COMPLETE</p>
</blockquote></td>
<td><blockquote>
<p>The start time of the operation is recorded and the patient is still in the operating</p>
<p>room.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>COMPLETE</p>
</blockquote></td>
<td><blockquote>
<p>The operation is completed and the patient has left the operating room.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ABORTED</p>
</blockquote></td>
<td><blockquote>
<p>The patient entered the operating room, but the operation had to be cancelled.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Following is an example of how the software lists existing cases on record for a patient.

> The user can select from the case(s) listed or, as in an emergency situation, enter a new surgical case. When the existing case is selected, the software will ask whether the user wants to:

1.  enter information for the case,
2.  review the information already entered, or
3.  delete the case.

> Entering Information

> First, the user selects the patient name. The Surgery software will then list all the cases on record for the patient, including scheduled or requested cases and any operations that have been started or completed. Then, the user selects the appropriate case.

> Example: Enter Information

> After the case is displayed, the user will press the \<Enter\> key or enter the number 1 to enter information for the case.

> Now the user can select any of the *Operation Menu* options.

> Reviewing Information

> The user enters the number 2 to access this feature. This feature displays a two-page summary of the case. The user cannot edit from this feature. Press the \<Enter\> key at the "Enter Screen Server Function:" prompt to move to the next page, or enter +1 or -1 to move forward or backward one page.

> Example: Review Information

> Deleting a Surgery Case

> The user enters the number 3 to access this feature. The *Delete Surgery Case* feature will permanently remove all information on the operative procedure from the records; however, only cases that are not completed can be deleted.

> Example: How to Delete A Case

## Abort/Cancel Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROABRT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Abort/Cancel Operation* option is used to Abort or Cancel a previously entered surgical case.

> This menu option should only be used if the patient has been taken to the operating room and no incision has been made. If an incision is made, the case should be completed and the discontinued procedure indicated in the record. Cancellation of future surgical cases should not use this option.

> Example: Abort Operation

> Select Schedule Operations Option: AB Abort/Cancel Operation

> SURPATIENT,ELEVEN (666-00-0785) Case \#21814 – JUN 22, 2015

> Case Aborted?: N// Y

1.  YES-PRE ANESTHESIA
2.  YES-POST ANESTHESIA Choose 1-2: 1 YES-PRE ANESTHESIA

> Time Patient In the O.R.: JUN 22,2015@0730 (JUN 22, 2015@07:30)

> Time Patient Out of the O.R.: JUN 22,2015@0800 (JUN 22, 2015@08:00) Primary Cancellation Reason: 1 PATIENT RELATED ISSUE 1

> Cancellation Date/Time: JUN 22,2015@0810 (JUN 22, 2015@08:10) Cancellation Avoidable: N NO

> Aborting Surgery case \#21814

> Enter RETURN to continue or '^' to exit: \<Enter\>

> Example: Cancel Operation

#### Time Patient In the

> O.R. and Time Patient Out of the O.R. will only be asked if they weren't previously

> Entering a New Surgical Case

> A new surgical case is a case that has not been previously requested or scheduled. This option is designed primarily for entering emergency cases. Be aware that a surgical case entered in the records without being booked through scheduling will not appear on the operating room schedule or as an operative request.

> At the "Select Operation:" prompt the user enters the number corresponding to the ENTER NEW SURGICAL CASE field. He or she will then be prompted to supply preoperative information concerning the case.

> After the user has entered data concerning the operation, the screen will clear and present a two-page Screen Server summary and provide another opportunity to enter or edit data.

> Prompts that require a response include:

> "Select the Date of Operation:"

> "Desired Procedure Date:"

> "Enter the Principal Operative Procedure:" "Principal Preoperative Diagnosis:" "Select Primary Surgeon:"

> "Attending Surgeon:" "Select Surgical Specialty:"

> "Planned Principal Procedure Code:"

> Example: Entering a New Surgical Case

## Operation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-OPINFO\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgeons and other members of the surgical staff use the *Operation Information* option for a quick reference on a case. It produces a report that touches on the more important areas of interest recorded for the case. The report can be viewed on screen but cannot be edited from this option.

> An asterisk indicates the principal diagnosis for the case, since some cases have more than one diagnosis. Notice that the INTRAOP OCCURRENCES field and the POSTOP OCCURRENCES field indicate if there are occurrences; however, the occurrences will not be defined, as access to this information is restricted.

> Example: Operation Information

> Select Operation Menu Option: I Operation Information

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Patient: SURPATIENT,SIX (000-09-8797) Operation Date: MAR 9, 1999</p>
<p>Primary Surgeon: SURSURGEON,SIXTEEN</p>
<p>Attending Surgeon: SURSURGEON,FOUR Operation Time: 45 Minutes Operation(s):</p>
<p>APPENDECTOMY</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Postop Diagnosis: Intraop Occurrences: YES</p>
<p>* APPENDICITIS Postop Occurrences: YES</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Anesthesia Technique: Anesthetist: SURANESTHETIST,THREE INHALATION</p>
<p>ENFLURANE 125ML</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Wound Classification: Intraoperative Blood Loss: 100 CC'S</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Press RETURN to continue</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Surgical Staff \[SROMEN-STAFF\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Surgical Staff* option allows the operating room nurse or scheduling manager to enter or edit the names of the surgical team prior to the operation. Some data fields may be automatically filled in based on previous responses. The names entered will be reflected in the Nurse Intraoperative Report and other staffing reports.

> At the "Enter Screen Server Function:" prompt, the user may choose the field(s) to be edited or press the

> \<Enter\> key to continue. Some of the data fields are "multiple" and may contain more than one value. When a field labeled "multiple" is selected, a new screen is generated so that the user can enter data related to that multiple. For example, the CIRC SUPPORT, SCRUB SUPPORT, and SCRUBBED ASSISTANT fields generate new screens that allow the user to add the TIME ON, TIME OFF, REASON FOR RELIEF, and STATUS. The TIME ON and TIME OFF fields also generate additional screens so that the user may enter more than one TIME ON/OFF for the same operation as some assistants must enter and exit more than once.

> ![](surgery-version-3-user-manual-updated-sr-3-184/019.png)If entering times on a day other than the day of surgery, enter both the date and the time. Entering only a time will default the date to the current date.

> Field Information

> The following are fields that correspond to the Surgical Staff entries.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ATTENDING/RES SUP CODE</p>
</blockquote></td>
<td><blockquote>
<p>This field corresponds to the highest level of supervision provided by the attending staff surgeon during the procedure. Enter a question mark <strong>(?)</strong> to retrieve the list of codes.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OTHER SCRUBBED ASSISTANTS</p>
</blockquote></td>
<td><blockquote>
<p>If there are more than two assistants scrubbed for this case, they</p>
<p>can be entered here.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OTHER PERSONS IN O.R.</p>
</blockquote></td>
<td><blockquote>
<p>This fields includes any observers, such as equipment vendors, in</p>
<p>the operating room.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 104 Surgery V. 3.0 User Manual November 2015

> Example: Entering Surgical Staff

#### November 2015 Surgery V. 3.0 User Manual 105

> 106 Surgery V. 3.0 User Manual November 2015

> November 2015 Surgery V. 3.0 User Manual 107

## Operation Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-START\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The nurse or other operating room staff uses the *Operation Startup* option to enter data concerning the patient's preparation for the surgery (for example, diagnosis, delays, skin prep, and position aids). Some data fields may be automatically filled in based on previous responses.

> Some of the data fields are "multiple fields" and can have more than one value. For example, a patient can have more than one diagnosis or restraint/position aid. When a multiple field is selected, a new screen is generated so that the user can enter data related to that multiple. At the "Enter Screen Server Function:" prompt, the user can choose the field(s) to be edited, or press the \<Enter\> key to go to the next item or page.

> Field Information

> The following are fields that correspond to the Operation Startup entries.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DELAY CAUSE:</p>
</blockquote></td>
<td><blockquote>
<p>If the actual start time of the surgery is significantly delayed (15 minutes or more, depending on the institution's policy) it is necessary to select a reason at the "Delay Cause:" prompt. Type in a question mark <strong>(?)</strong> at this prompt to select from a list of delay</p>
<p>causes.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RESTR &amp; POSITION AIDS:</p>
</blockquote></td>
<td><blockquote>
<p>A safety strap is automatically included as a restraint.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 108 Surgery V. 3.0 User Manual November 2015

> Example: Operation Startup

14. RESTR & POSITION AIDS: (MULTIPLE)(DATA)
15. ELECTROGROUND POSITION:

#### November 2015 Surgery V. 3.0 User Manual 109

> 110 Surgery V. 3.0 User Manual November 2015

> November 2015 Surgery V. 3.0 User Manual 111

> *(This page included for two-sided copying.)*

> 112 Surgery V. 3.0 User Manual November 2015

## Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-OP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgeons and nurses use the *Operation* option to enter data relating to the operation during or immediately following the actual procedure. It is very important to record the time of the patient's entrance into the hold area and operating room, the time anesthesia is administered, and the operation start time.

> Many of the data fields are "multiple fields" and can have more than one value. For example, a patient can have more than one diagnosis or procedure done per operation. When a multiple field is selected, a new screen is generated so that the user can enter data related to that multiple. The up-arrow (^) can be used to exit from any multiple field. Enter a question mark (?) for software- assisted instruction.

> Field Information

> The following are fields that correspond to the Operation entries.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TIME OPERATION BEGAN</p>
</blockquote></td>
<td><blockquote>
<p>The user should check his or her institution's policy concerning an operation's start time. In some institutions, this may be the</p>
<p>time of first incision.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](surgery-version-3-user-manual-updated-sr-3-184/020.png)If entering times on a day other than the day of surgery, enter both the date and the time. Entering only a time will default the date to the current date.

> November 2015 Surgery V. 3.0 User Manual 113

> Example: Operation Option: Entering Information

#### Surgery V. 3.0 User Manual November 2015

> November 2015 Surgery V. 3.0 User Manual 115

#### Surgery V. 3.0 User Manual November 2015

> November 2015 Surgery V. 3.0 User Manual 117

> 118 Surgery V. 3.0 User Manual November 2015

## Post Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-POST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Post Operation* option concerns the close of the operation, discharge, and post anesthesia recovery. It is important to enter the operation and anesthesia end times, as well as the time the patient leaves the operation room, as these fields affect many reports.

> Field Information

> The following are fields that correspond to the *Post Operation* option entries.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TIME PAT OUT OR</p>
</blockquote></td>
<td><blockquote>
<p>Entry of this field generates an alert notifying the circulating</p>
<p>nurse that the Nurse Intraoperative Report is ready for signature.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ANES CARE TIME BLOCK</p>
</blockquote></td>
<td><blockquote>
<p>Entry of this multiple generates an alert notifying the anesthetist</p>
<p>that the Anesthesia Report is ready for signature.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example: Post Operation

> Select Operation Menu Option: PO Post Operation

#### November 2015 Surgery V. 3.0 User Manual 119

> 120 Surgery V. 3.0 User Manual November 2015

> *(This page included for two-sided copying.)*

## Enter PAC(U) Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-PACU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Personnel in the Post Anesthesia Care Unit (PACU) use the *Enter PAC(U) Information* option to enter the admission and discharge times and scores.

> Example: Entering PAC(U) Information

> Select Operation Menu Option: PAC Enter PAC(U) Information

## Operation (Short Screen)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-OUT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operation (Short Screen)* option provides a three-page screen of information concerning a surgical procedure performed on a patient. The *Operation (Short Screen)* option allows the nurse or surgeon to easily enter data relating to the operation during, and shortly after, the actual procedure. This time-saving option can replace the *Operation Startup* option, the *Operation* option, and the *Post Operation* option for minor surgeries.

> When only one anesthesia technique is entered, the software will assume that it is the principal anesthesia technique for the case. Some data fields may be automatically pre-populated if the case was booked in advance.

> Example: Operation Short Screen

> Select Operation Menu Option: OSS Operation (Short Screen)

## Time Out Verified Utilizing Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-VERF\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to enter information related to the Time Out Verified Utilizing Checklist.

> Example: Time Out Verified Utilizing Checklist

> Select Operation Menu Option: Time Out Verified Utilizing Checklist

> If the PLANNED PRIN PROCEDURE CODE field for the case is one of the following CPT codes Time Out Checklist-2 will be displayed: 32851, 32852,3 2853, 32854, 33935, 33945, 44135, 44136, 47135,

> 47136, 48160, 48554, 50360, 50365.

> Example: Time Out Verified Utilizing Checklist-2

## Surgeon's Verification of Diagnosis & Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROVER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgeons use this option to verify that the stated procedure(s), diagnosis, and occurrences are correct for a case. With this option, the surgeon can update the Operation Name, Planned CPT Code, Diagnosis, and Intraoperative Occurrences before verifying the case. If the case has already been verified, the user will be asked whether to re-verify it.

> If the user responds YES to the prompt "Do you need to update the information above ?" the software will provide a summary for editing.

> ![](surgery-version-3-user-manual-updated-sr-3-184/021.png)If there are no occurrences, the INTRAOP OCCURRENCES field should be left blank. Do not

> enter NO or NONE.

> The procedure and diagnosis codes are the codes captured with clinical data, and are supplied as defaults to the Coder when entering the final codes that will be sent to PCE.

> Service Classifications

> Information relating to a patient's status of Service Connected (SC) and Environmental Indicators (EI) are captured during patient registration. The Surgery software receives this data from enrollment and displays it when the user creates a case.

> In the Surgery software, the patient's Service Classification status is determined at the case level when the case is created. The user can further refine status designations, not only per case, but also per diagnosis.

> The system defaults the case-level Service Classification indicators into each Other Postop Diagnosis field as the user adds the Other Postop Diagnoses. The system allows the user to edit these fields if the user determines that the defaulted value is incorrect.

> Example: Surgeon's Verification of Diagnosis & Procedures

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 10%" />
<col style="width: 2%" />
<col style="width: 7%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Select Operation Menu Option: <strong>V</strong> Surgeon's Verification</p>
<p>SURPATIENT,ONE (000-44-7629)</p>
<p>Operation Date: JUN 5, 2005</p>
</blockquote></th>
<th><blockquote>
<p>of</p>
</blockquote></th>
<th><blockquote>
<p>Diagnosis</p>
</blockquote></th>
<th><blockquote>
<p>&amp;</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>Procedures</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><ol type="1">
<li><p>Indications for Operation: Swelling in the inguinal region.</p></li>
<li><p>Planned Principal CPT Code: 00830</p></li>
</ol>
<blockquote>
<p>Assoc. DX: 1. 550.02 BILAT ING HERNIA W GANG</p>
</blockquote>
<ol start="3" type="1">
<li><p>Principal Procedure: REMOVE HERNIA</p></li>
<li><p>Other Procedures:</p></li>
<li><p>Postoperative Diagnosis: INGUINAL HERNIA</p></li>
<li><p>Intraoperative Occurrences: NO OCCURRENCES HAVE BEEN ENTERED</p></li>
<li><p>Principal Pre-OP Diagnosis: HERNIA</p></li>
<li><p>Principal Pre-OP Diagnosis Code: 550.02 BILAT ING HERNIA W GANG</p></li>
</ol></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Do you need to update the information above ? Select Information to Edit: <strong>2:3</strong></p>
</blockquote></td>
<td><blockquote>
<p>NO//</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p><strong>Y</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,ONE (000-44-7629)</p>
</blockquote></th>
<th rowspan="16"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Operation Date: JUN 5, 2005</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>1. Indications for Operation:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Swelling in the inguinal region.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>2. Planned Principal CPT Code: 49521</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>REPAIR RECURRENT INGUINAL HERNIA, ANY AGE; INCARCERATED OR STRANGULATED</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Modifiers: -59</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>3. Principal Procedure: REPAIR INGUINAL HERNIA</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>4. Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>5. Postoperative Diagnosis: INGUINAL HERNIA</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>6. Intraoperative Occurrences: NO OCCURRENCES HAVE BEEN ENTERED</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>7. Principal Pre-OP Diagnosis: HERNIA</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>8. Principal Pre-OP Diagnosis Code: 550.02 BILAT ING HERNIA W GANG</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Do you need to update the information above ? NO// <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Will you verify that the information on your screen is correct ? YES// <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Press RETURN to continue</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Anesthesia for an Operation Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROANES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](surgery-version-3-user-manual-updated-sr-3-184/022.png)The *Anesthesia for an Operation Menu* option is restricted to anesthesia personnel and is locked with the SROANES key.

> This option is designed for convenient entry of data pertaining to the anesthesia agents, personnel and techniques. When the user selects this option from the *Operation Menu* option, he or she is given a submenu of five options.

> The options included in this menu are listed below. To the left of the option name is the shortcut synonym that may be entered to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Information (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>T</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Technique (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p><em>Medications (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p><em>Schedule Anesthesia Personnel</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Prerequisites

> To use any of these options, other than the *Schedule Anesthesia Personnel* option*,* the user must first select a patient case. For the *Schedule Anesthesia Personnel* option, a date and then an operating room must first be selected.

> These options can also be accessed from the main *Surgery Menu*.

> Information related to these options is contained in "Chapter Two: Tracking Clinical Procedures," in the Anesthesia Menu section.

## Operation Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROSRPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operation Report* option displays the dictated Operation Report for the patient case selected. This report contains the surgeon's dictation regarding the surgical procedure. The Operation Report is not electronically signed in the Surgery package. After the dictated Operation Report is uploaded into the Text Integration Utilities (TIU) package, it is then available for electronic signature through the Computerized Patient Record System (CPRS) Surgery tab.

> ![](surgery-version-3-user-manual-updated-sr-3-184/023.png)When electronically signed, the Operation Report is also viewable through CPRS. The electronically signed Operation Report replaces VA Form 516. If the Operation Report has not been electronically signed, then CPRS will only display a stub for that document.

> After the dictated Operation Report is transcribed and uploaded into TIU, the TIU software sends an alert to the surgeon responsible for electronically signing the report.

> Until the Operation Report is signed, if the *Operation Report* option is selected, the following text displays:

> "The Operation Report for this case is not yet available."

> If the Operation Report has been signed, the *Operation Report* option will display the signed document. (See the example.)

#### printout follows 

> Example: A signed Operation Report

> Page: 1

> SURPATIENT,TEN 000-12-3456 OPERATION REPORT NOTE DATED: 07/29/2003 15:15 OPERATION REPORT

> VISIT: 07/29/2003 15:15 SURGERY OP REPORT NON-COUNT SUBJECT: Case \#: 73285

> PREOPERATIVE DIAGNOSIS: Visually significant cataract, right eye POSTOPERATIVE DIAGNOSIS: Visually significant cataract, right eye PROCEDURE: Phacoemulsification with intraocular lens placement, right eye

> CLINICAL INDICATIONS: This 64-year-old gentleman complains of decreased vision in the right eye affecting his activities of daily living. Best corrected visual acuity is counting fingers at 6 feet, associated with a 2-3+ nuclear sclerotic and 4+ posterior subcapsular cataract in that eye.

> ANESTHESIA: Local monitoring with topical Tetracaine and 1% preservative free Lidocaine.

> DESCRIPTION OF THE PROCEDURE: After the risks, benefits and alternatives of the procedure were explained to the patient, informed consent was obtained. The patient's right eye was dilated with Phenylephrine, Mydriacyl and Ocufen. He was brought to the Operating Room and placed on anesthetic monitors. Topical Tetracaine was given. He was prepped and draped in the usual sterile fashion for eye surgery. A Lieberman lid speculum was placed.

> A Supersharp was used to create a superior paracentesis port. The anterior chamber was irrigated with 1% preservative free Lidocaine. The anterior chamber was filled with Viscoelastic. The diamond groove maker and diamond keratome were used to create a clear corneal tunneled incision at the temporal limbus. The cystotome was used to initiate a continuous capsulorrhexis, which was then completed using Utrata forceps. Balanced salt solution was used to hydrodissect and hydrodelineate the lens.

> Phacoemulsification was used to remove the lens nucleus and epinucleus in a non-stop horizontal chop fashion. Cortex was removed using irrigation and aspiration. The capsular bag was filled with Viscoelastic. The wound was enlarged with a 69 blade. An Alcon model MA60BM posterior chamber intraocular lens with a power of 24.0 diopters, serial \#588502.064, was folded and inserted with the leading haptic placed into the bag. The trailing haptic was dialed into the bag with the Lester hook. The wound was hydrated. The anterior chamber was filled with balanced salt solution. The wound was tested and found to be self-sealing. Subconjunctival antibiotics were given, and an eye shield was placed. The patient was taken in good condition to the Recovery Room. There were no complications.

> KJC/PSI

> DATE DICTATED: 07/29/03 DATE TRANSCRIBED: 07/29/03 JOB: 629095

> Signed by: /es/ FOURTEEN SURSURGEON, M.D.

> 07/30/2003 10:31

## Anesthesia Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROARPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Anesthesia Report details anesthesia information for the patient case selected. This option provides the capability to view/print the report, edit information contained in the report, and electronically sign the report. This option can also be accessed from the *Anesthesia Menu* option located on the *Operation Menu*, as well as on the main *Surgery Menu*.

> Anesthesia Report (Unsigned)

> Upon selecting this option, if the Anesthesia Report is not signed the report will begin displaying. The Anesthesia Report displays key fields on the first page. Several of these fields are required before the software will allow the user to electronically sign the report. If any of these fields are left blank, a warning will appear prompting the user to provide the missing information. The ANES CARE TIME field, PRINCIPAL ANETHESIA TECHNIQUE (primary) field, ANESTHESIA TECHNIQUE field, ASA CLASS field, OP DISPOSITION field, and the PRINC ANESTHETIST field must all be completed before the Anesthesia Report can be electronically signed.

> ![](surgery-version-3-user-manual-updated-sr-3-184/024.png)Entering the information into the ANES CARE END TIME field triggers an alert that is sent to the anesthetist responsible for signing the report. By responding to the alert, the user is taken to the *Anesthesia Report* option.

> At the bottom of the first screen is the prompt, "Press \<return\> to continue, 'A' to access Anesthesia Report functions or '^' to exit:". The *Anesthesia Report* functions, accessed by entering A at the prompt, allow the user to edit the report, to view or print the report, or to electronically sign the report.

> Example: First page of an Anesthesia Report

> After entering an A at the prompt, the Anesthesia functions are displayed. The following examples demonstrate how these three functions are accessed and how they operate.

> If the user enters a 1, the Anesthesia Report data can be edited.

> Example: Edit Report Information

> If the user enters a 2, the Anesthesia Report can be printed.

> Example: Print the Anesthesia Report

> *printout follows*

> SURPATIENT,TEN 000-12-3456 ANESTHESIA REPORT NOTE DATED: 02/12/2004 08:00 ANESTHESIA REPORT

> SUBJECT: Case \#: 267226

> Operating Room: WX OR3

> Anesthetist: SURANESTHETIST,SEVEN Relief Anesth:

> Anesthesiologist: SURANESTHESIOLOGIST,ONE Assist Anesth: SURANESTHETIST,FIVE Attending Code: LEVEL 3. ATTENDING NOT PRESENT IN O.R. SUITE, IMMEDIATE

> LY AVAILABLE.

> Anes Begin: FEB 12, 2004 08:00 Anes End: FEB 12, 2004 12:10 ASA Class: \* NOT ENTERED \*

> Operation Disposition: SICU

> Anesthesia Technique(s):

> GENERAL (PRINCIPAL)

> Agent: ISOFLURANE FOR INHALATION 100ML

> Intubated: YES Trauma: NONE

> Min Intraoperative Temp: 35

> Intraoperative Blood Loss: 800 ml Urine Output: 750 ml Operation Disposition: SICU

> PAC(U) Admit Score: PAC(U) Discharge Score: Postop Anesthesia Note Date/Time:

> To electronically sign the report, the user enters a 3.

> Example: Sign the Report Electronically

> In this case, a key field, the ASA CLASS field, has been omitted. The system will prompt the user to supply the missing information before allowing the report to be electronically signed.

> ![](surgery-version-3-user-manual-updated-sr-3-184/025.png)The Anesthesia Report cannot be signed if the ASA CLASS field, or any other key field information, is missing.

> Responding YES to the, "Do you want to enter this information?" prompt allows the user to enter or correct fields on the Anesthesia Report.

> Example: Entering or Correcting a Field on the Anesthesia Report prior to Signature

> After any necessary edits have been made, the report can be electronically signed.

> Example: Electronically signing the Anesthesia Report

> Once an Anesthesia Report has been signed, a warning informing the user that the Anesthesia Report has already been signed will display on screen and an addendum will be required for any future changes.

> Anesthesia Report (Signed)

> After an Anesthesia Report has been signed, any changes to the signed report will require a signed addendum.

> Example: Editing the Signed Report

> Select Operation Menu Option: AR Anesthesia Report

> ![](surgery-version-3-user-manual-updated-sr-3-184/026.png)If the Anesthesia Report and/or the Nurse Intraoperative Report has already been signed, the following warning will be displayed. If any data on either signed report is edited, an addendum to the Anesthesia Report and/or to the Nurse Intraoperative Report will be required.

> Example: Warning

> The user can proceed to edit the report and sign the required addendum or simply exit.

> Example: Editing the Signed Report

> ![](surgery-version-3-user-manual-updated-sr-3-184/027.png)If the user elects to exit these options prior to signing the addendum, all fields on the report revert back to the values entered when electronically signed.

<table>
<colgroup>
<col style="width: 71%" />
<col style="width: 10%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Addendum for Case #267226 - FEB 12,2004 Patient: SURPATIENT,TEN (000-12-3456)</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>The Operating Room field was changed from WX OR3</p>
<p>to BO OR1</p>
<p>Addendum Comment: OPERATING ROOM NUMBER WAS CORRECTED.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Enter RETURN to continue or '^' to exit: <strong>&lt;Enter&gt;</strong></p>
<p>Enter your Current Signature Code: <strong>XXX</strong> SIGNATURE VERIFIED Press RETURN to continue... <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>When typing the electronic signature code, no characters will display on screen.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> The *Print/View report from beginning* function can then be used to view or print the report with the addendum.

> Example: Print/View Report With Addendum

> *printout follows*

> SURPATIENT,TEN 000-12-3456 ANESTHESIA REPORT NOTE DATED: 02/12/2004 08:00 ANESTHESIA REPORT

> SUBJECT: Case \#: 267226

> Operating Room: WX OR3

> Anesthetist: SURANESTHETIST,SEVEN Relief Anesth:

> Anesthesiologist: SURANESTHESIOLOGIST,ONE Assist Anesth: SURANESTHETIST,FIVE Attending Code: 3. STAFF ASSISTING C.R.N.A.

> Anes Begin: FEB 12, 2004 08:00 Anes End: FEB 12, 2004 12:10 ASA Class: 1-NO DISTURB.

> Operation Disposition: SICU

> Anesthesia Technique(s):

> GENERAL (PRINCIPAL)

> Agent: ISOFLURANE FOR INHALATION 100ML

> Enter RETURN to continue or '^' to exit:

> Intubated: YES Trauma: NONE

> Procedure(s) Performed:

> Principal: MVR

> Min Intraoperative Temp: 35

> Intraoperative Blood Loss: 800 ml Urine Output: 750 ml Operation Disposition: SICU

> PAC(U) Admit Score: PAC(U) Discharge Score: Postop Anesthesia Note Date/Time:

Signed by: /es/ SEVEN SURANESTHETIST

> 03/04/2004 10:59

> 03/04/2004 11:04 ADDENDUM

> The Operating Room field was changed from WX OR3

> to BO OR1

Addendum Comment: OPERATING ROOM NUMBER WAS CORRECTED.

Signed by: /es/ SEVEN SURANESTHETIST

> 03/04/2004 11:04

## Nurse Intraoperative Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRONRPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Nurse Intraoperative Report details case information relating to nursing care provided for the patient during the operative case selected. This option provides the capability to view and print the report, edit information contained in the report, and electronically sign the report.

> With the *Surgery Site Parameters* option located on the *Surgery Package Management Menu*, the user can select one of two different formats for this report. One format includes all field names whether or not information has been entered. The other format only includes fields that have actual data.

> Electronically signed reports may be viewed through CPRS for completed operations.

> Nurse Intraoperative Report - Before Electronic Signature

> Upon selecting the *Nurse Intraoperative Report* option, if the Nurse Intraoperative Report is not signed, the report will begin displaying on the screen. The Nurse Intraoperative Report displays key fields on the first page. Several of these fields are required before the software will allow the user to electronically sign the report. If any required fields are left blank, a warning will appear prompting the user to provide the missing information.

> The following fields are required before electronic signature of the Nurse Intraoperative Report:

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>TIME PAT IN OR</p></li>
</ul></th>
<th><ul>
<li><p>TIME PAT OUT OR</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>HAIR REMOVAL METHOD</p></li>
</ul></td>
<td><ul>
<li><p>MARKED SITE CONFIRMED</p></li>
</ul></td>
</tr>
<tr class="even">
<td><ul>
<li><p><span id="_bookmark69" class="anchor"></span>CORRECT PATIENT IDENTITY</p></li>
<li><p>SITE OF PROCEDURE</p></li>
<li><p>CONFIRM PATIENT POSITION</p></li>
<li><p>ANTIBIOTIC PROPHYLAXIS</p></li>
<li><p>BLOOD AVAILABILITY</p></li>
<li><p>CHECKLIST COMMENT</p></li>
<li><p>TIME-OUT COMPLETED</p></li>
</ul></td>
<td><ul>
<li><p>PREOPERATIVE IMAGING CONFIRMED</p></li>
<li><p>PROCEDURE TO BE PERFORMED</p></li>
<li><p>CONFIRM VALID CONSENT</p></li>
<li><p>CORRECT MEDICAL IMPLANTS</p></li>
<li><p>APPROPRIATE DVT PROPHYLAXIS</p></li>
<li><p>AVAILABILITY OF SPECIAL EQUIP</p></li>
<li><p>PROSTHESIS INSTALLED</p></li>
</ul></td>
</tr>
</tbody>
</table>

> The WOUND SWEEP and INTRAOPERATIVE-XRAY will be required to sign the NIR if any of the count fields (SPONGE FINAL COUNT CORRECT, SHARPS FINAL COUNT CORRECT, and INSTRUMENT FINAL COUNT CORRECT) is answered with "NO".

> If the COUNT VERIFIER field has been entered, the following fields are required:

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>SPONGE FINAL COUNT CORRECT</p></li>
</ul></th>
<th><ul>
<li><p>SHARPS FINAL COUNT CORRECT</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>INSTRUMENT FINAL COUNT CORRECT</p></li>
</ul></td>
<td><ul>
<li><p>SPONGE, SHARPS, &amp; INST COUNTER</p></li>
<li><p>POSSIBLE ITEM RETENTION</p></li>
</ul></td>
</tr>
</tbody>
</table>

> The ANESTHESIA TECHNIQUE field is made mandatory in order for the NIR report to be signed.

> If the PROSTHESIS INSTALLED field has an item (or items) entered, the following fields are required for each item:

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>IMPLANT STERILITY CHECKED</p></li>
</ul></th>
<th><ul>
<li><p>STERILITY EXPIRATION DATE</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>RN VERIFIER</p></li>
<li><p>SERIAL NUMBER</p></li>
</ul></td>
<td><ul>
<li><p>LOT NUMBER</p></li>
<li><p>PROVIDER READ BACK PERFORMED</p></li>
</ul></td>
</tr>
</tbody>
</table>

> If the PLANNED PRIN PROCEDURE CODE field for the case is matches one of these CPT codes 32851, 32852,3 2853, 32854, 33935, 33945, 44135, 44136, 47135, 47136, 48160, 48554, 50360, 50365;

> the following fields are required:

- ORGAN TO BE TRANSPLANTED
- UNOS NUMBER
- DONOR SEROLOGY HCV
- DONOR SEROLOGY HBV
- DONOR SEROLOGY CMV
- DONOR SEROLOGY HIV
- DONOR ABO TYPE
- RECEIPIENT ABO TYPE
- BLOOD BANK ABO VERIFICATION
- BLOOD BANK ABO VER COMMENTS
- D/T BLOOK BANK ABO VERIF
- OR ABO VERIFICATION
- D/T OR ABO VERIF
- SURGEON VERIFYING UNET
- UNET VERIF BY SURGEON
- ORGAN VER PRE-ANESTHESIA
- SURGEON VER ORGAN PRE-ANES
- SURGEON VER DONOR ORG PRE-ANES
- DONOR ORG VER PRE-ANES
- ORGAN VER PRE-TRANSPLANT
- SURGEON VER ORG PRE-TRANSPLANT
- DONOR VESSEL UNOS ID
- DONOR VESSEL USAGE
- DONOR VESSEL DISPOSITION

> ![](surgery-version-3-user-manual-updated-sr-3-184/028.png)Entering the TIME PAT OUT OR field triggers an alert that is sent to the nurse responsible for signing the report. By acting on the alert, the nurse accesses the *Nurse Intraoperative Report* option to electronically sign the report.

> At the bottom of the first screen is the prompt, "Press \<return\> to continue, 'A' to access Nurse Intraoperative Report functions, or '^' to exit:". The *Nurse Intraoperative Report* functions, accessed by entering A at the prompt, allow the user to edit the report, to view or print the report, or to electronically sign the report.

> Example: First page of the Nurse Intraoperative Report

> Select Operation Menu Option: NR Nurse Intraoperative Report

> After the user enters an A at the prompt, the *Nurse Intraoperative Report* functions are displayed. The following examples demonstrate how these three functions are accessed and how they operate.

> If the user enters a 1, the Nurse Intraoperative Report data can be edited.

> Example: Editing the Nurse Intraoperative Report

> At the *Nurse Intraoperative Report* functions, the report can be printed if the user enters a 2.

> Example: Printing the Nurse Intraoperative Report

> *printout follows*

> SURPATIENT,TEN 000-12-3456 NURSE INTRAOPERATIVE REPORT NOTE DATED: 07/12/2004 08:00 NURSE INTRAOPERATIVE REPORT

> SUBJECT: Case \#: 267226

> Operating Room: BO OR1 Surgical Priority: ELECTIVE

> Patient in Hold: JUL 12, 2004 07:30 Patient in OR: JUL 12, 2004 08:00

> Operation Begin: JUL 12, 2004 08:58 Operation End: JUL 12, 2004 12:10

> Surgeon in OR: JUL 12, 2004 07:55 Patient Out OR: JUL 12, 2004 12:45

> Major Operations Performed:

> Primary: MVR

> Wound Classification: CONTAMINATED Operation Disposition: SICU Discharged Via: ICU BED

> Primary Surgeon: SURSURGEON,THREE First Assist: SURSURGEON,FOUR Attending Surgeon: SURSURGEON,THREE Second Assist: N/A Anesthetist: SURANESTHETIST,SEVEN Assistant Anesth: N/A

> Other Scrubbed Assistants: N/A OR Support Personnel:

> Scrubbed Circulating

SURNURSE,ONE (FULLY TRAINED) SURNURSE,FIVE (FULLY TRAINED)

SURNURSE,FOUR (FULLY TRAINED)

> Other Persons in OR: N/A

> Preop Mood: ANXIOUS Preop Consc: ALERT-ORIENTED

> Preop Skin Integ: INTACT Preop Converse: N/A

> --- Time Out Checklist ---

> Confirm Correct Patient Identity: YES Confirm Procedure to be Performed: YES

> Confirm Site of the Procedure, including laterality: YES Confirm Valid Consent: YES, i-MED

> Confirm Patient Position: YES

> Confirm Proc. Site has been Marked Appropriately and that the Site of the Mark is Visible After Prep and Draping: YES

> Pertinent Medical Images have been Confirmed: YES Correct Medical Implant(s) is available: YES Availability of Special Equipment: YES Appropriate Antibiotic Prophylaxis: YES Appropriate Deep Vein Thrombosis Prophylaxis: YES Blood Availability: YES

> Checklist Comment: NO COMMENTS ENTERED

> Time-Out Document Completed By: SURNURSE,FIVE Time-Out Completed: 07/12/2004@0800

> Skin Prep By: SURNURSE,FOUR Skin Prep Agent: BETADINE SCRUB Skin Prep By (2): SURNURSE,FIVE 2nd Skin Prep Agent: POVIDONE IODINE

> Preop Surgical Site Hair Removal by: SURNURSE,FIVE Surgical Site Hair Removal Method: OTHER

> Hair Removal Comments: SHAVING AND DEPILATORY COMBINATION USED.

> Surgery Position(s):

> SUPINE Placed: N/A

> Restraints and Position Aids:

> SAFETY STRAP Applied By: N/A

> ARMBOARD Applied By: N/A

> FOAM PADS Applied By: N/A

> KODEL PAD Applied By: N/A

> STIRRUPS Applied By: N/A

> <span id="_bookmark70" class="anchor"></span>Immediate Use Steam Sterilization Episodes: Contamination: 0

> SPS Processing/OR Management Issues: 0 Emergency Case: 0

> No Better Option: 0

> Loaner or Short Notice Instrument: 0

> Decontamination of Instruments Contaminated During the Case: 0

> Electrocautery Unit: 8845,5512 ESU Coagulation Range: 50-35

> ESU Cutting Range: 35-35

Electroground Position(s): RIGHT BUTTOCK

LEFT BUTTOCK

> Material Sent to Laboratory for Analysis:

> Specimens:

1.  MITRAL VALVE Cultures: N/A

> Anesthesia Technique(s):

> GENERAL (PRINCIPAL)

> Tubes and Drains:

> \#16FOLEY, \#18NGTUBE, \#36 &2 \#32RA CHEST TUBES

> Tourniquet: N/A Thermal Unit: N/A Prosthesis Installed:

> Item: MITRAL VALVE

> Implant Sterility Checked (Y/N): YES Sterility Expiration Date: DEC 15, 2004 RN Verifier: SURNURSE,ONE

> Vendor: BAXTER EDWARDS

> Model: 6900

> Lot Number: T87-12321 Serial Number: 945673WRU Sterile Resp: SPD

> Size: LG Quantity: 2

> Medications: N/A Irrigation Solution(s):

> HEPARINIZED SALINE NORMAL SALINE

> COLD SALINE

> Blood Replacement Fluids: N/A

> Possible Item Retention: YES Sponge Final Count Correct:

> Sharps Final Count Correct: YES Instrument Final Count Correct: NOT APPLICABLE Wound Sweep: \* NOT ENTERED \* Wound Sweep Comment: NO COMMENTS ENTERED

> Intra-Operative X-Ray: \* NOT ENTERED \*

> Intra-Operative X-Ray Comment: NO COMMENTS ENTERED Counter: SURNURSE,FOUR

> Counts Verified By: SURNURSE,FIVE

> Dressing: DSD, PAPER TAPE, MEPORE

> Packing: NONE

> Blood Loss: 800 ml Urine Output: 750 ml Postoperative Mood: RELAXED

> Postoperative Consciousness: ANESTHETIZED Postoperative Skin Integrity: SUTURED INCISION

> Postoperative Skin Color: N/A Laser Performed: N/A

> Sequential Compression Device: NO Cell Saver(s): N/A

> Devices: N/A

> Transplant Information:

> Organ to be Transplanted: \* NOT ENTERED \* UNOS Identification Number of Donor:

> Donor Serology Hepatitis C virus (HCV): \* NOT ENTERED \* Donor Serology Hepatitis B Virus (HBV): \* NOT ENTERED \* Donor Serology Cytomegalovirus (CMV): \* NOT ENTERED \* Donor Serology HIV: \* NOT ENTERED \*

> Donor ABO Type: \* NOT ENTERED \* Recipient ABO Type: \* NOT ENTERED \*

> Blood Bank Verification of ABO Type: \* NOT ENTERED \* Blood Bank ABO Verification Comments:

> Date/Time of Blood Bank ABO Verification: \* NOT ENTERED \* OR Verification of ABO Type: \* NOT ENTERED \*

> OR ABO Verification Comments:

> Date/Time OR ABO Verification: \* NOT ENTERED \* Surgeon Performing UNET Verification: \* NOT ENTERED \* UNET Verification by Surgeon: \* NOT ENTERED \*

> Organ Verification Prior to Anesthesia: \* NOT ENTERED \* Surgeon Verifying Organ Prior to Anesthesia: \* NOT ENTERED \*

> Surgeon Verifying Organ Prior to Donor Anesthesia: \* NOT ENTERED \* Donor Organ Verification Prior to Anesthesia: \* NOT ENTERED \* Organ Verification Prior to Transplant: \* NOT ENTERED \*

> Surgeon Verifying the Organ Prior to Transplant: \* NOT ENTERED \* Donor Vessel Usage: \* NOT ENTERED \*

> Donor Vessel Disposition if not used:

> Donor Vessel UNOS ID:

> Immediate Use Steam Sterilization Episodes: Contamination: 0

> SPS Processing/OR Management Issues: 0 Emergency Case: 0

> No Better Option: 0

> Loaner or Short Notice Instrument: 0

> Decontamination of Instruments Contaminated During the Case: 0

> Nursing Care Comments:

> PATIENT STATES HE IS ALLERGIC TO PCN. ALL WRVAMC INTRAOPERATIVE NURSING STANDARDS WERE MONITORED THROUGHOUT THE PROCEDURE. VANCYMYCIN PASTE WAS APPLIED TO STERNUM.

#### (This page included for two-sided copying.)

> To electronically sign the report, the user enters a 3 at the *Nurse Intraoperative Report* functions prompt.

> Example: Signing the Nurse Intraoperative Report

> The Nurse Intraoperative Report may only be signed by a circulating nurse on the case. At the time of electronic signature, the software checks for data in key fields. The nurse will not be able to sign the report if the following fields are not entered:

> TIME PATIENT IN OR TIME PATIENT OUT OF OR

> MARKED SITE CONFIRMED CORRECT PATIENT IDENTITY PREOPERATIVE IMAGING CONFIRMED HAIR REMOVAL METHOD PROCEDURE TO BE PERFORMED SITE OF THE PROCEDURE CONFIRM VALID CONSENT CONFIRM PATIENT POSITION CORRECT MEDICAL IMPLANTS ANTIBIOTIC PROPHYLAXIS APPROPRIATE DVT PROPHYLAXIS BLOOD AVAILABILITY AVAILABILITY OF SPECIAL EQUIP CHECKLIST COMMENT

> TIME-OUT COMPLETED

> The WOUND SWEEP and INTRAOPERATIVE X-XRAY fields will be required to sign the NIR if any of the count fields (SPONGE FINAL COUNT CORRECT, SHARPS FINAL COUNT CORRECT, and INSTRUMENT FINAL COUNT CORRECT) is answered with "NO"

> ![](surgery-version-3-user-manual-updated-sr-3-184/029.png)If the COUNT VERIFIER field is entered, the other counts related fields must be populated. These count fields include the following:

> SPONGE FINAL COUNT CORRECT SHARPS FINAL COUNT CORRECT INSTRUMENT FINAL COUNT CORRECT SPONGE, SHARPS, & INST COUNTER POSSIBLE ITEM RETENTION

> The ANESTHESIA TECHNIQUE field is made mandatory in order for the NIR report to be signed.

> If the PROSTHESIS INSTALLED field has an item (or items) entered, the following fields are required for each item:

> IMPLANT STERILITY CHECKED (Y/N) STERILITY EXPIRATION DATE RN VERIFIER <span id="_bookmark71" class="anchor"></span>LOT NUMBER

> SERIAL NUMBER PROVIDER READ BACK PERFORMED

> If the PLANNED PRIN PROCEDURE CODE field is one of the following codes 32851,32852,32853,32854,33935,33945,44135,44136,47135,47136,48160,48554,50360,50365

> the following fields are required:

> ORGAN TOBE TRANSPLANED SURGEON VERIFYING UNET UNOS NUMBER UNET VERIF BY SURGEON

> DONOR SEROLOGY HCV ORGAN VER PRE-ANESTHESIA

> DONOR SEROLOGY HBV SURGEON VER ORGAN PRE-ANES

> DONOR SEROLOGY CMV SURGEON VER DONOR PRE-ANES

> DONOR SEROLOGY HIV DONOR ORG VER PRE-ANES

> DONOR ABO TYPE ORGAN VER PRE-TRANSPLANT

> RECIPIENT ABO TYPE SURGEON VER ORG PRE-TRANSPLANT BLOOD BANK ABO VERIFICATION DONOR VESSEL UNOS ID

> BLOOD BANK ABO VER COMMENTS DONOR VESSEL USAGE

> D/T BLOOD BANK ABO VERIF DONOR VESSEL DISPOSITION OR ABO VERIFICATION

> OR ABO VER COMMENTS D/T OR ABO VERIF

> If any of the key fields are missing, the software will require them to be entered prior to signature. In the following example, the final sponge count must be entered before the nurse is allowed to electronically sign the report.

> Example: Missing Field Warning

> ![](surgery-version-3-user-manual-updated-sr-3-184/030.png)If any of the Time Out Verified Utilizing Checklist fields is answered with "NO", then the user is prompted to enter information in the CHECKLIST COMMENT field. Entry in the CHECKLIST COMMENT field is required in such cases where "NO" has been entered before the user can electronically sign the Nurse Intraoperative Report.

> Nurse Intraoperative Report - After Electronic Signature

> After the report has been signed, any changes to the report will require a signed addendum.

> Example: Editing the Signed Nurse Intraoperative Report

> ![](surgery-version-3-user-manual-updated-sr-3-184/031.png)If the Anesthesia Report and/or the Nurse Intraoperative Report is already signed, the following warning will be displayed. If any data on either signed report is edited, an addendum to the Anesthesia Report and/or to the Nurse Intraoperative Report will be required.

> First, the user makes the edits to the desired field.

> An addendum is required before the edit can be made to the signed report.

> Before the addendum is signed, comments may be added.

> Example: Signing the Addendum

> Comment: OPERATION END TIME WAS CORRECTED.

> Addendum for Case \#267226 - JUL 12,2004 Patient: SURPATIENT,TEN (000-12-3456)

> The Time-Out Document Completed By field was changed from SURNURSE,FOUR

> to SURNURSE,FIVE

> Addendum Comment: OPERATION END TIME WAS CORRECTED.

> Enter RETURN to continue or '^' to exit:

> Enter your Current Signature Code: XXXXXX SIGNATURE VERIFIED.. Press RETURN to continue... \<Enter\>

> Example: Printing the Nurse Intraoperative Report

> When typing the electronic signature code, no characters will display on screen.

> *----------------------------------------------------------printout follows-----------------------------------------------*

> SURPATIENT,TEN 000-12-3456 NURSE INTRAOPERATIVE REPORT

> NOTE DATED: 07/12/2004 08:00 NURSE INTRAOPERATIVE REPORT SUBJECT: Case \#: 267226

> Operating Room: BO OR1 Surgical Priority: ELECTIVE

> Patient in Hold: JUL 12, 2004 07:30 Patient in OR: JUL 12, 2004 08:00

> Operation Begin: JUL 12, 2004 08:58 Operation End: JUL 12, 2004 12:30

> Surgeon in OR: JUL 12, 2004 07:55 Patient Out OR: JUL 12, 2004 12:45

> Major Operations Performed:

> Primary: MVR

> Wound Classification: CONTAMINATED Operation Disposition: SICU Discharged Via: ICU BED

> Primary Surgeon: SURSURGEON,THREE First Assist: SURSURGEON,FOUR Attending Surgeon: SURSURGEON,THREE Second Assist: N/A

> Anesthetist: SURANESTHETIST,SEVEN Assistant Anesth: N/A Other Scrubbed Assistants: N/A

> OR Support Personnel:

> Scrubbed Circulating

SURNURSE,ONE (FULLY TRAINED) SURNURSE,FIVE (FULLY TRAINED)

SURNURSE,FOUR (FULLY TRAINED)

> Other Persons in OR: N/A

> Preop Mood: ANXIOUS Preop Consc: ALERT-ORIENTED

> Preop Skin Integ: INTACT Preop Converse: N/A

> --- Time Out Checklist ---

> Confirm Correct Patient Identity: YES Confirm Procedure to be Performed: YES

> Confirm Site of the Procedure, including laterality: YES Confirm Valid Consent: YES, i-MED

> Confirm Patient Position: YES

> Confirm Proc. Site has been Marked Appropriately and that the Site of the Mark is Visible After Prep and Draping: YES

> Pertinent Medical Images have been Confirmed: YES Correct Medical Implant(s) Is Available: YES Availability of Special Equipment: YES Appropriate Antibiotic Prophylaxis: YES Appropriate Deep Vein Thrombosis Prophylaxis: YES Blood Availability: YES

> Checklist Comment: NO COMMENTS ENTERED

> Time-Out Document Completed By: SURNURSE,FOUR Time-Out Completed:07/12/2004@0800

> Skin Prep By: SURNURSE,FOUR Skin Prep Agent: BETADINE SCRUB Skin Prep By (2): SURNURSE,FIVE 2nd Skin Prep Agent: POVIDONE IODINE

> Preop Surgical Site Hair Removal by: SURNURSE,FIVE Surgical Site Hair Removal Method: OTHER

> Hair Removal Comments: SHAVING AND DEPILATORY COMBINATION USED.

> Surgery Position(s):

> SUPINE Placed: N/A

> Restraints and Position Aids:

> SAFETY STRAP Applied By: N/A

> ARMBOARD Applied By: N/A

> FOAM PADS Applied By: N/A

> KODEL PAD Applied By: N/A

> STIRRUPS Applied By: N/A

> <span id="_bookmark72" class="anchor"></span>Immediate Use Steam Sterilization Episodes:

> Contamination: 0

> SPS Processing/OR Management Issues: 0 Emergency Case: 0

> No Better Option: 0

> Loaner or Short Notice Instrument: 0

> Decontamination of Instruments Contaminated During the Case: 0

> Electrocautery Unit: 8845,5512 ESU Coagulation Range: 50-35

> ESU Cutting Range: 35-35

Electroground Position(s): RIGHT BUTTOCK

LEFT BUTTOCK

> Material Sent to Laboratory for Analysis:

> Specimens:

> 1\. MITRAL VALVE Cultures: N/A Anesthesia Technique(s):

> GENERAL (PRINCIPAL)

> Tubes and Drains:

> \#16FOLEY, \#18NGTUBE, \#36 &2 \#32RA CHEST TUBES

> Tourniquet: N/A Thermal Unit: N/A Prosthesis Installed:

> Item: MITRAL VALVE

> Implant Sterility Checked (Y/N): YES Sterility Expiration Date: DEC 15, 2004 RN Verifier: SURNURSE,ONE

> Vendor: BAXTER EDWARDS

> Model: 6900

> Lot Number: T87-12321 Serial Number: 945673WRU Sterile Resp: SPD

> Size: LG

> Provider Read Back Performed: YES Quantity: 2 Medications: N/A

> Irrigation Solution(s): HEPARINIZED SALINE NORMAL SALINE

> COLD SALINE

> Blood Replacement Fluids: N/A Possible Item Retention: YES Sponge Count: YES

> Sharps Count: YES

> Instrument Count: NOT APPLICABLE

> Wound Sweep: \* NOT ENTERED \* Wound Sweep Comment: NO COMMENTS ENTERED Intra-Operative X-Ray: \* NOT ENTERED \*

> Intra-Operative X-Ray Comment: NO COMMENTS ENTERED Counter: SURNURSE,FOUR

> Counts Verified By: SURNURSE,FIVE

> Dressing: DSD, PAPER TAPE, MEPORE

> Packing: NONE

> Blood Loss: 800 ml Urine Output: 750 ml Postoperative Mood: RELAXED

> Postoperative Consciousness: ANESTHETIZED Postoperative Skin Integrity: SUTURED INCISION Postoperative Skin Color: N/A

> Laser Performed: (Multiple) Sequential Compression Device: NO

> Cell Saver(s): N/A Devices: N/A

> Transplant Information:

> Organ to be Transplanted: \* NOT ENTERED \* UNOS Identification Number of Donor:

> Donor Serology Hepatitis C virus (HCV): \* NOT ENTERED \* Donor Serology Hepatitis B Virus (HBV): \* NOT ENTERED \* Donor Serology Cytomegalovirus (CMV): \* NOT ENTERED \* Donor Serology HIV: \* NOT ENTERED \*

> Donor ABO Type: \* NOT ENTERED \* Recipient ABO Type: \* NOT ENTERED \*

> Blood Bank Verification of ABO Type: \* NOT ENTERED \* Blood Bank ABO Verification Comments:

> Date/Time of Blood Bank ABO Verification: \* NOT ENTERED \* OR Verification of ABO Type: \* NOT ENTERED \*

> OR ABO Verification Comments:

> Date/Time OR ABO Verification: \* NOT ENTERED \* Surgeon Performing UNET Verification: \* NOT ENTERED \* UNET Verification by Surgeon: \* NOT ENTERED \*

> Organ Verification Prior to Anesthesia: \* NOT ENTERED \* Surgeon Verifying Organ Prior to Anesthesia: \* NOT ENTERED \*

> Surgeon Verifying Organ Prior to Donor Anesthesia: \* NOT ENTERED \* Donor Organ Verification Prior to Anesthesia: \* NOT ENTERED \* Organ Verification Prior to Transplant: \* NOT ENTERED \*

> Surgeon Verifying the Organ Prior to Transplant: \* NOT ENTERED \* Donor Vessel Usage: \* NOT ENTERED \*

> Donor Vessel Disposition if not used:

> Donor Vessel UNOS ID:

> Immediate Use Steam Sterilization Episodes: Contamination: 0

> SPS Processing/OR Management Issues: 0 Emergency Case: 0

> No Better Option: 0

> Loaner or Short Notice Instrument: 0

> Decontamination of Instruments Contaminated During the Case: 0 Nursing Care Comments:

> PATIENT STATES HE IS ALLERGIC TO PCN. ALL WRVAMC INTRAOPERATIVE NURSING STANDARDS WERE MONITORED THROUGHOUT THE PROCEDURE. VANCYMYCIN PASTE WAS APPLIED TO STERNUM.

> Signed by: /es/ FIVE SURNURSE

> 07/13/2004 10:41

> 07/17/2004 16:42 ADDENDUM

> The Time-Out Document Completed By field was changed from SURNURSE,FOUR to SURNURSE,FIVE

> Addendum Comment: OPERATION END TIME WAS CORRECTED.

> Signed by: /es/ FIVE SURNURSE

> 07/17/2004 16:42

> *(This page included for two-sided copying.)*

## Tissue Examination Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROTRPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Tissue Examination Report* option is used to generate the Tissue Examination Report that contains information about cultures and specimens sent to the laboratory.

> This report prints in an 80-column format and can be viewed on the screen.

> Example: Tissue Examination Report

> *printout follows*

> MEDICAL RECORD \| TISSUE EXAMINATION

> Specimen Submitted By: Obtained: MAR 09, 1999 OR1, SURGERY CASE \# 187

> Specimen(s):

> Brief Clinical History:

> Subscapular pain for 3 days. Nausea and vomiting. Increased serum amylase.

> Operative Procedure(s):

> CHOLECYSTECTOMY, INTRAOPERATIVE CHOLANGIOGRAM

> Preoperative Diagnosis:

> CHOLECYSTITIS

> Operative Findings:

> THE GALLBLADDER HAD A FEW ADHESIONS EASILY REMOVED AND WAS FOUND TO BE FIRMLY DISTENDED WITH STONES.

> Postoperative Diagnosis: Signature and Title CHOLECYSTITIS SURSURGEON,TWO

> Attending Surgeon: SURSURGEON,ONE

> PATHOLOGY REPORT

> Name of Laboratory Accession Number(s)

Gross Description, Histologic Examination and Diagnosis

(Continue on reverse side)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 21%" />
<col style="width: 15%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>PATHOLOGIST'S SIGNATURE</th>
<th></th>
<th></th>
<th><blockquote>
<p>DATE:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SURPATIENT,NINE ETHNICITY: NOT HISPANIC RACE: WHITE, ASIAN WARD:</td>
<td><blockquote>
<p>AGE: 48</p>
<p>ROOM-BED:</p>
</blockquote></td>
<td><blockquote>
<p>SEX: MALE</p>
</blockquote></td>
<td><blockquote>
<p>ID # 000-34-5555 REGISTER NO.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VAMC: MAYBERRY, NC</td>
<td></td>
<td></td>
<td><blockquote>
<p>REPLACEMENT FORM 515</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Enter Referring Physician Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-REFER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Enter Referring Physician Information* option allows the surgical staff to enter the name, address, and phone number of the individual or institution that referred the patient. The scheduling manager usually enters referring physician information when the operation is booked. This information shows up on many reports.

> First, users identify the surgical specialty to which the patient will be assigned. To add a new case to the waiting list, the user must enter the patient's name and the procedure name. The user can also add comments, referring physician name and address, tentative admission date, and tentative operation date. This information will appear on the *Waiting List Report*. Patient names stay on the waiting list until the data is used to make a request or until the data is deleted.

> After entering a Referring Physician name or partial name, the system prompts, "Is this a VA Physician from this facility? (Y/N): \<Y\>". If the user answers Y, a list of VA physician names displays that matches the data entered. The user selects from those listed. The physician's address and telephone number are also copied into the corresponding fields if the data is available. If no selection is made, the system accepts the information entered as free text.

> If the referring physician is not from that VA facility, then the system uses the information already entered as the Referring Physician name, or the user can enter the appropriate name.

> Example: Enter Referring Physician Information

> Select Operation Menu Option: R Enter Referring Physician Information

## Enter Irrigations and Restraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-REST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Enter Irrigations and Restraints* option is designed to allow the nurse to quickly document the irrigation solutions or the restraint and positioning devices used in a case. The list of solutions or devices can be different at each facility.

> At the "Select Number:" prompt, the user should choose the number corresponding to the solution or device. For more than one choice, numbers are separated with a comma. If an item has been selected before, a default prompt will appear. The user can enter an at-sign (@) to delete the selection, as in Example 3.

> Example 1: Entering Irrigations

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 12%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1. AEROSP/PXYN</p>
</blockquote></th>
<th><blockquote>
<p>2.</p>
</blockquote></th>
<th><blockquote>
<p>BACITRACIN SOLUTION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3. BETADINE SOLUTION</p>
</blockquote></td>
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><blockquote>
<p>HEPARIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5. HEPARINIZED SALINE</p>
</blockquote></td>
<td><blockquote>
<p>6.</p>
</blockquote></td>
<td><blockquote>
<p>ICED SALINE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7. KANTREX SOLUTION</p>
</blockquote></td>
<td><blockquote>
<p>8.</p>
</blockquote></td>
<td><blockquote>
<p>KEFLEX SOLUTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9. NEOMYCIN</p>
</blockquote></td>
<td><blockquote>
<p>10.</p>
</blockquote></td>
<td><blockquote>
<p>NEOMYCIN SOLUTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11. NORMAL SALINE</p>
</blockquote></td>
<td><blockquote>
<p>12.</p>
</blockquote></td>
<td><blockquote>
<p>POVODINE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13. SORBITAL</p>
</blockquote></td>
<td><blockquote>
<p>14.</p>
</blockquote></td>
<td><blockquote>
<p>STERILE WATER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15. VEIN GRAFT SOLUTION</p>
</blockquote></td>
<td><blockquote>
<p>16.</p>
</blockquote></td>
<td><blockquote>
<p>THROMBIN</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example 2: Restraints and Positioning Aids

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 15%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1. ARMSHEET</p>
</blockquote></th>
<th><blockquote>
<p>2.</p>
</blockquote></th>
<th><blockquote>
<p>SAFETY STRAP</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3. ARMBOARD</p>
</blockquote></td>
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><blockquote>
<p>VAC PAC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5. FOAM PADS</p>
</blockquote></td>
<td><blockquote>
<p>6.</p>
</blockquote></td>
<td><blockquote>
<p>PILLOW</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7. AXILLARY ROLL</p>
</blockquote></td>
<td><blockquote>
<p>8.</p>
</blockquote></td>
<td><blockquote>
<p>ADHESIVE TAPE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9. SURGERY ARMBOARD</p>
</blockquote></td>
<td><blockquote>
<p>10.</p>
</blockquote></td>
<td><blockquote>
<p>KIDNEY REST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11. SANDBAG</p>
</blockquote></td>
<td><blockquote>
<p>12.</p>
</blockquote></td>
<td><blockquote>
<p>OVERHEAD ARMREST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13. ROLLED SHEET</p>
</blockquote></td>
<td><blockquote>
<p>14.</p>
</blockquote></td>
<td><blockquote>
<p>LEG HOLDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15. FOOT EXTENSION</p>
</blockquote></td>
<td><blockquote>
<p>16.</p>
</blockquote></td>
<td><blockquote>
<p>STIRRUPS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>17. FRACTURE TABLE</p>
</blockquote></td>
<td><blockquote>
<p>18.</p>
</blockquote></td>
<td><blockquote>
<p>OTHER</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example 3: Deleting Restraints and Positioning Aids

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 15%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1. ARMSHEET</p>
</blockquote></th>
<th><blockquote>
<p>2.</p>
</blockquote></th>
<th><blockquote>
<p>SAFETY STRAP</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3. ARMBOARD</p>
</blockquote></td>
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><blockquote>
<p>VAC PAC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5. FOAM PADS</p>
</blockquote></td>
<td><blockquote>
<p>6.</p>
</blockquote></td>
<td><blockquote>
<p>PILLOW</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7. AXILLARY ROLL</p>
</blockquote></td>
<td><blockquote>
<p>8.</p>
</blockquote></td>
<td><blockquote>
<p>ADHESIVE TAPE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9. SURGERY ARMBOARD</p>
</blockquote></td>
<td><blockquote>
<p>10.</p>
</blockquote></td>
<td><blockquote>
<p>KIDNEY REST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11. SANDBAG</p>
</blockquote></td>
<td><blockquote>
<p>12.</p>
</blockquote></td>
<td><blockquote>
<p>OVERHEAD ARMREST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13. ROLLED SHEET</p>
</blockquote></td>
<td><blockquote>
<p>14.</p>
</blockquote></td>
<td><blockquote>
<p>LEG HOLDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15. FOOT EXTENSION</p>
</blockquote></td>
<td><blockquote>
<p>16.</p>
</blockquote></td>
<td><blockquote>
<p>STIRRUPS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>17. FRACTURE TABLE</p>
</blockquote></td>
<td><blockquote>
<p>18.</p>
</blockquote></td>
<td><blockquote>
<p>OTHER</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Medications (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROANES MED\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Medications (Enter/Edit)* option allows the user to enter all the medications administered on a case. It is designed to aid in quickly entering many different medications for a case.

> In one entry, the user can enter the medication, dosage, route, and time given with the use of slashes between these categories. After one medication has been entered, the software will return the cursor to the beginning prompt so that the user can enter another medication for the case. When the user is finished entering medications for the case, he or she should press the \<Enter\> key to return to the menu.

> About the prompts

> "ENTER MEDICATION/DOSE(MG)/ROUTE/TIME:" Respond to this prompt with the medication, dosage, route, and time given separated by slashes. If the software needs more specific information about the medication, the user will be prompted. In the example below, the software reads "Valium" and then asks the user to select from the Valiums on file. A question mark can be entered in place of one of the categories in order to get help or more information. In the example, a question mark was entered in place of the route. Then, in response to the question mark, the software offered a list of acceptable routes.

> Example: Entering Medication

## Blood Product Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR BLOOD PRODUCT VERIFICATION\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Blood Product Verification* option is used for transfusion error risk management. This option is used in conjunction with a bar code reader to confirm that the blood product is assigned to the patient. The functionality provided by this option is meant as an additional check for proper patient identification and should never be relied upon as the primary check.

> This option prompts the user to scan the blood product unit ID, after which the software checks the Blood Bank files for an association with the patient identified. If there are multiple entries with the unit ID scanned, these entries will be listed along with the Blood Component, Patient Associated, and Expiration Date. The user will then be prompted to select the one that matches the blood product about to be administered. If the selected product is not associated with the patient identified, a warning message will be displayed.

> There are certain valid scenarios that are internal to the Blood Bank that may result in a blood component not being readable using the scanner and therefore may give an unexpected response. There will be some rare instances in which this option may not produce an expected result. After verifying proper patient identification, the option may be attempted again; however, it is recommended that the unit ID be typed in manually rather than be scanned in these cases.

> Blood product manufacturers are required to label all units of blood in a consistent manner. The barcode that is to be scanned at the "Enter Blood Product Identifier:" prompt will always be the barcode in the upper-left portion of the blood product label. Since this label can be in close proximity to the ABO/Rh label, care should be taken not to read both labels during a scan. One way to accomplish this would be to use a finger or some other convenient object to cover the label that the user does not wish to have read during the scanning process. The light emitted from the scanner itself will cause no harm to skin, latex, or any other object with which it comes in contact.

> Example: Option displayed with no discrepancies

> Example: Option displayed with discrepancies

# Anesthesia Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## \[SROANES1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](surgery-version-3-user-manual-updated-sr-3-184/032.png)The *Anesthesia Menu* is restricted to Anesthesia personnel and is locked with the SROANES key. It is designed for the convenient entry of data pertaining to the anesthesia agents and

> techniques used in a surgery.

> The main options included in this menu are listed below. The *Anesthesia Data Entry Menu* contains sub- options. To the left of the option name is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>E</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Data Entry Menu</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p><em>Schedule Anesthesia Personnel</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To use the *Anesthesia Data Entry Menu* or the *Anesthesia Report* option, the user must first select a patient case. The user must select an operating room to use the *Schedule Anesthesia Personnel* option.

## Anesthesia Data Entry Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROANES-D\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Anesthesia Data Entry Menu* allows the user to enter anesthesia data pertinent to a selected case. The information entered in these sub-options is reflected on the Anesthesia Report.

> To use any option within the *Anesthesia Data Entry Menu*, the user must first enter a patient name and choose a patient case, as shown below.

> Example: How to Select a Case for the Data Entry Menu

## Anesthesia Information (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-ANES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Anesthesia staff uses this option to enter anesthesia related information for a given case. The first group of prompts affects the Anesthesia AMIS Report. Some of the data fields may be automatically filled in from previous responses.

> At the "Enter Screen Server Function:" prompt, the user can choose the field(s) to be edited, or press the

> \<Enter\> key to continue. Some of the data fields are "multiple" and may contain more than one value. When a multiple field is selected, a new screen is generated so that the user can enter data related to that multiple. For instance, the MONITORS field generates a new screen for adding the device, time installed, and time removed. The TIME INSTALLED field and TIME REMOVED field generate additional screens so that the user may enter more than one time installed/removed for the same operation.

> About the prompts

> The prompts are described as follows:

- "Is this the Principal Technique (Y/N): " — Asks if the user has entered a technique that is the primary anesthesia technique for the case. The user is required to establish the principal technique as this information affects many reports.
- "Would you like to enter additional anesthesia related information ? " — If the user wants to enter more detailed information concerning the case, he or she must answer YES to this prompt. Two Screen Server-formatted pages are then provided for entering more anesthesia information for the case.
- "Does this entry complete all start and end times for this case? "— The user should answer YES only if the block of time just completed is the final block of time for the case that he or she is documenting.

> An Anesthesia Care Questionnaire will be added to allow a more complete capture of clinical data, which will support coding and billing efforts. The results of the questionnaire are crucial for a coder to use in order to select the proper modifier. Modifiers are required for reimbursement for all anesthesia services.

> This information can be accessed through the Anesthesia menu, specifically through the Anesthesia Data Entry Menu. The user selects a patient and surgical case and completes the anesthesia information.

> After completion, the user is prompted with the question, "Would you like to enter additional anesthesia related information? " The questions associated with the Anesthesia Care Questionnaire (shown as numbers 8-12 on the last screen display in this section) are located on page two of the anesthesia information sheet.

> Example: Entering Anesthesia Information

> *(This page included for two-sided copying.)*

## Anesthesia Technique (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-ANES TECH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Anesthesia Technique (Enter/Edit)* option is used to enter information concerning the anesthesia technique. More than one anesthesia technique can be entered for a case. When the user is finished entering the first technique, he or she should select this option again to start entering another anesthesia technique.

> The Surgery software recognizes the following anesthesia techniques, each with different sets of prompts. G *GENERAL*

#### M MONITORED ANESTHESIA CARE

> S *SPINAL*

#### E EPIDURAL

> L *LOCAL*

> R *REGIONAL*

> Note: The selection of 'OTHER' is no longer available for selection.

> Another choice for an anesthesia technique is NO ANESTHESIA. This selection does not include any additional prompts.

> About the prompts

> "Diagnostic/ Therapeutic (Y/N):" The user should answer Y or YES if the anesthesia procedure is itself a surgical procedure. The user will then have an opportunity to define the surgical (operative) procedure.

> "Is this the Principal Technique (Y/N):" This prompt asks the user whether or not the technique being entered is the primary anesthesia technique for the case. For the technique being entered to appear on the Anesthesia AMIS Report, answer this prompt with a Y or YES.

> "Select ANESTHESIA AGENTS:" The user can enter more than one anesthesia agent for a case by using the up-arrow (^) to jump to the "Select ANESTHESIA AGENTS:" prompt.

> Example 1: General Technique

> More than one anesthesia agent may be entered for each technique.

> ![](surgery-version-3-user-manual-updated-sr-3-184/033.png)The ANESTHESIA AGENT field uses entries from the institution's local DRUG file. Prior to using the Surgery package, drugs that will be used as anesthesia agents must be flagged (using the Chief of Surgery Menu) by the user's package coordinator. If the user experiences problems entering an agent, it is likely that the drug being chosen has not been flagged.

> Example 2: Monitored Anesthesia Care Technique

> Example 3: Spinal Technique

> Example 4: Epidural Technique

> Example 5: Local Technique

> Example 6: Regional Technique

## Medications (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROANES MED\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Anesthesia staff members use the *Medications (Enter/Edit)* option to enter medications administered on a case. This is the last sub-option of the *Anesthesia Data Entry Menu*.

> This option is designed to help the user quickly enter many different medications for a case. In one entry, the user can enter the medication, dosage, route, and time given with the use of slashes between these categories. (This is a different type of prompt response from what has been used elsewhere). After the user has finished entering one medication, the software will return the cursor to the beginning prompt so that he or she can enter another medication for the case. When the user finishes entering medications for the case, he or she should press the \<Enter\> key to return to the *Anesthesia Data Entry Menu*.

> About the prompts

> "ENTER MEDICATION/DOSE(MG)/ROUTE/TIME:" Respond to this prompt with the medication, dosage, route, and time given separated by slashes. If the software needs more specific information about the medication, the user will be prompted. In the example, the software reads "Valium" and then asks the user to select from the Valiums on file. A question mark can be entered in place of one of the categories in order to get help or more information. In the following example, a question mark was entered in place of the route. Then, in response to the question mark, the software offered a list of acceptable routes.

> Example: Entering a Medication

> Select Anesthesia Data Entry Menu Option: M Medications (Enter/Edit)

> ENTER MEDICATION/DOSE(MG)/ROUTE/TIME:

## Anesthesia Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROARPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Anesthesia staff uses the *Anesthesia Report* option to print all the anesthesia information entered for a case. When a hard copy of this report is made, space is provided for the Anesthetist's signature. This option is located on the *Anesthesia Menu* option. It can also be accessed from the *Operation Menu* option.

> For more information, see the Anesthesia Report section in the Operation Menu section of this manual.

> Page 171 has been deleted. The *Anesthesia AMIS* option has been removed.

> Page 172 has been deleted. The *Anesthesia AMIS* option has been removed.

## Schedule Anesthesia Personnel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSCHDA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Anesthesia staff uses the *Schedule Anesthesia Personnel* option to assign or change anesthesia personnel for surgery cases. The Scheduling Manager can also assign personnel to the selected case using other menu options.

> ![](surgery-version-3-user-manual-updated-sr-3-184/034.png) This *Schedule Anesthesia Personnel* option is locked with the SROANES key and will not appear on the menu if the user does not have this key.

> With this option, the user can enter an anesthesia technique and the names of the principal anesthetist and supervisor. When an operating room is selected, the software will present all cases scheduled for that room. After scheduling personnel for cases in one operating room, the user can do the same for other operating rooms without leaving this option. For convenience, the software will default to the anesthetist and anesthesiologist supervisor previously scheduled for that room.

> Example: Scheduling Anesthesia Personnel

> Would you like to continue with another operating room ? YES// N

# Perioperative Occurrences Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO COMPLICATIONS MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgeons use options within the *Perioperative Occurrences Menu* option to enter or edit occurrences that occur before, during, and/or after a surgical procedure. It is also possible to enter occurrences for a patient who did not have a surgical procedure performed. The user can enter more than one occurrence per patient.

> ![](surgery-version-3-user-manual-updated-sr-3-184/035.png) This option is locked with the SROCOMP key.

> Occurrences will be included on the Chief of Surgery's Morbidity & Mortality Reports.

> ![](surgery-version-3-user-manual-updated-sr-3-184/036.png)Please review specific institution policy to determine what is considered an occurrence for any category.

> The options included in this menu are listed below. To the left of the option name is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p><em>Intraoperative Occurrences (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p><em>Postoperative Occurrences (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p><em>Non-Operative Occurrences (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Status of Returns Within 30 Days</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p><em>Morbidity &amp; Mortality Reports</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Key Vocabulary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following terms are used in this section.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Intraoperative Occurrence</p>
</blockquote></td>
<td><blockquote>
<p>Occurrence that occurs during the procedure.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Postoperative Occurrence</p>
</blockquote></td>
<td><blockquote>
<p>Occurrence that occurs after the procedure.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Non-Operative Occurrence</p>
</blockquote></td>
<td><blockquote>
<p>Occurrence that develops before a surgical procedure is performed.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Intraoperative Occurrences (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO INTRAOP COMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Intraoperative Occurrences (Enter/Edit)* option is used to add information about an occurrence that occurs during the procedure. The user can also use this option to change the information. Occurrence information will be reflected in the Chief of Surgery's Morbidity & Mortality Report.

> First, the user should select an operation. The software will then list any occurrences already entered for that operation. The user may edit a previously entered occurrence or can type the word NEW and press the \<Enter\> key to enter a new occurrence.

> At the prompt "Enter a New Intraoperative Occurrence:" the user can enter two question marks (??) to get a list of categories. Be sure to enter a category for all occurrences to satisfy Surgery Central Office reporting needs.

> Example: Entering Intraoperative Occurrences

> Select Perioperative Occurrences Menu Option: I Intraoperative Occurrences (Enter/Edit)

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,FIFTY (000-45-9999) Case #213</p>
<p>JUN 30,2006 CHOLECYSTECTOMY</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>Occurrence Category: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted:</p></li>
<li><p>Outcome to Date:</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>4:5</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,FIFTY (000-45-9999) Case #213</p>
<p>JUN 30,2006 CHOLECYSTECTOMY</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>Occurrence Category: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted: CPR</p></li>
<li><p>Outcome to Date: IMPROVED</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Postoperative Occurrences (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO POSTOP COMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Postoperative Occurrences (Enter/Edit)* option is used to add information about an occurrence that occurs after the procedure. The user can also utilize this option to change the information. Occurrence information will be reflected in the Chief of Surgery's Morbidity & Mortality Report.

> First, the user selects an operation. The software will then list any occurrences already entered for that operation. The user can choose to edit a previously entered occurrence or type the word NEW and press the \<Enter\> key to enter a new occurrence.

> At the prompt "Enter a New Postoperative Complication:" the user can enter two question marks (??) to get a list of categories. Be sure to enter a category for all occurrences in order to satisfy Surgery Central Office reporting needs.

> Example: Entering a Postoperative Occurrence

> Select Perioperative Occurrences Menu Option: P Postoperative Occurrence (Enter/Edit)

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN (000-45-5119) Case #202 MAR 18,2007 REPAIR INCARCERATED INGUINAL HERNIA</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: ACUTE RENAL FAILURE</p></li>
<li><p>Occurrence Category: ACUTE RENAL FAILURE</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted:</p></li>
<li><p>Outcome to Date:</p></li>
<li><p>Date Noted:</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>4:6</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN R. (000-45-5119) Case #202 MAR 18,2007 REPAIR INCARCERATED INGUINAL HERNIA</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: ACUTE RENAL FAILURE</p></li>
<li><p>Occurrence Category: ACUTE RENAL FAILURE</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted: DIALYSIS</p></li>
<li><p>Outcome to Date: IMPROVED</p></li>
<li><p>Date Noted: 03/20/07</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Non-Operative Occurrence (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROCOMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Non-Operative Occurrence (Enter/Edit)* option is used to enter or edit occurrences that are not related to surgical procedures. A non-operative occurrence is an occurrence that develops before a surgical procedure is performed.

> At the "Occurrence Category:" prompt, the user can enter two question marks (??) to get a list of categories. Be sure to enter a category for each occurrence in order to satisfy Surgery Central Office reporting needs.

> Example: Entering a Non-Operative Occurrence

> *(This page included for two-sided copying.)*

## Update Status of Returns Within 30 Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO UPDATE RETURNS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Status of Returns Within 30 Days* option will define a case as related or unrelated to another case. When a new surgical case is entered into the software, the user is asked whether it is related to any previous cases within the past 30 days. This option is designed to update that information.

> The user should first enter the patient name and select a case. The software will list any cases that occurred within 30 days prior to the selected case and will indicate if the listed cases have been flagged as related or unrelated. At this point the user may update the status of the cases listed.

> Example: Updating Status of Returns Within 30 days

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
<p>JUN 23,1999 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th><blockquote>
<p>Case #62192</p>
</blockquote></th>
<th><blockquote>
<p>RETURNS</p>
</blockquote></th>
<th><blockquote>
<p>TO</p>
</blockquote></th>
<th><blockquote>
<p>SURGERY</p>
</blockquote></th>
<th></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>1. 07/06/99</p>
</blockquote></th>
<th><blockquote>
<p>REPAIR INGUINAL</p>
</blockquote></th>
<th><blockquote>
<p>HERNIA - UNRELATED</p>
</blockquote></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="3"></th>
</tr>
<tr class="header">
<th><blockquote>
<p>2. 06/25/99</p>
</blockquote></th>
<th><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></th>
<th><blockquote>
<p>- UNRELATED</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select Number:</p>
</blockquote></th>
<th><blockquote>
<p><strong>2</strong></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
<p>JUN 23,1999 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th></th>
<th>Case</th>
<th><blockquote>
<p>#62192</p>
</blockquote></th>
<th><blockquote>
<p>RETURNS</p>
</blockquote></th>
<th><blockquote>
<p>TO</p>
</blockquote></th>
<th><blockquote>
<p>SURGERY</p>
</blockquote></th>
<th></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>2. 06/25/99 CHOLECYSTECTOMY</p>
</blockquote></th>
<th><blockquote>
<p>-</p>
</blockquote></th>
<th>UNRELATED</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th rowspan="2"></th>
</tr>
<tr class="header">
<th colspan="7"><blockquote>
<p>This return to surgery is currently defined as UNRELATED to the case selected. Do you want to change this status ? NO// <strong>Y</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
<p>JUN 23,1999 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th><blockquote>
<p>Case #62192</p>
</blockquote></th>
<th><blockquote>
<p>RETURNS</p>
</blockquote></th>
<th><blockquote>
<p>TO</p>
</blockquote></th>
<th><blockquote>
<p>SURGERY</p>
</blockquote></th>
<th></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>07/06/99 REPAIR INGUINAL</p></li>
<li><p>06/25/99 CHOLECYSTECTOMY</p></li>
</ol></th>
<th><blockquote>
<p>HERNIA - UNRELATED (- RELATED</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th rowspan="2"></th>
</tr>
<tr class="header">
<th colspan="5"><blockquote>
<p>Select Number:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Morbidity & Mortality Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Morbidity & Mortality Reports* option generates two reports: the Perioperative Occurrences Report and the Mortality Report. The Perioperative Occurrences Report includes all cases that have occurrences, both intraoperatively and postoperatively, and can be sorted by specialty, attending surgeon, or occurrence category. The Mortality Report includes all cases performed within the selected date range that had a death within 30 days after surgery, and sort by specialty within a date range. Each surgical specialty will begin on a separate page.

> After the user enters the date range, the software will ask whether to generate both reports. If the user answers NO, the software will ask the user to select from the Perioperative Occurrences Report or the Mortality Report.

> These reports have a 132-column format and are designed to be copied to a printer.

> Example 1: Printing the Perioperative Occurrences Report – Sorted by Specialty

> Select Perioperative Occurrences Menu Option: M Morbidity & Mortality Reports

> *report follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE REVIEWED BY: PERIOPERATIVE OCCURRENCES-INTRAOP/POSTOP DATE REVIEWED:

> FROM: JUL 1,2006 TO: JUL 31,2006 DATE PRINTED: AUG 22,2006

> PATIENT ATTENDING SURGEON OCCURRENCE(S) - (DATE) OUTCOME

> ID# PRINCIPAL OPERATION TREATMENT OPERATION DATE

> ==================================================================================================================================== GENERAL(OR WHEN NOT DEFINED BELOW)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 34%" />
<col style="width: 42%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE</p>
<p>000-41-8719</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,THREE</p>
<p>REPAIR DIAPHRAGMATIC HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>MYOCARDIAL INFARCTION</p>
<p>ASPIRIN THERAPY</p>
</blockquote></th>
<th>I</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>JUL 07, 2006@07:15</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>URINARY TRACT INFECTION * (07/09/06)</p>
</blockquote></td>
<td>I</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>IV ANTBIOTICS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,FOURTEEN 000-45-7212</p>
<p>JUL 31, 2006@09:00</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FIVE CHOLECYSTECTOMY, APPENDECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SUPERFICIAL WOUND INFECTION * (08/02/06) ANTIBIOTICS</p>
</blockquote></td>
<td>I</td>
</tr>
</tbody>
</table>

> OUTCOMES: U - UNRESOLVED, I - IMPROVED, W - WORSE, D - DEATH

> '\*' Represents Postoperative Occurrences

> Example 2: Printing the Perioperative Occurrences Report – Sorted by Attending Surgeon

> Select Perioperative Occurrences Menu Option: M Morbidity & Mortality Reports

#### report follows 

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE REVIEWED BY: PERIOPERATIVE OCCURRENCES-INTRAOP/POSTOP DATE REVIEWED:

> FROM: JUL 1,2006 TO: JUL 31,2006 DATE PRINTED: AUG 22,2006

> PATIENT SURGICAL SPECIALTY OCCURRENCE(S) - (DATE) OUTCOME

> ID# PRINCIPAL OPERATION TREATMENT OPERATION DATE

> ====================================================================================================================================

> ATTENDING: SURGEON,ONE

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 36%" />
<col style="width: 40%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE</p>
<p>000-41-8719</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW)</p>
<p>REPAIR DIAPHRAGMATIC HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>MYOCARDIAL INFARCTION</p>
<p>ASPIRIN THERAPY</p>
</blockquote></th>
<th>I</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>JUL 07, 2006@07:15</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>URINARY TRACT INFECTION * (07/09/06)</p>
</blockquote></td>
<td>I</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>IV ANTBIOTICS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,THREE 000-21-2453</p>
<p>JUL 22, 2006@10:00</p>
</blockquote></td>
<td><blockquote>
<p>CARDIAC SURGERY CABG</p>
</blockquote></td>
<td><blockquote>
<p>REPEAT VENTILATOR SUPPORT W/IN 30 DAYS *</p>
</blockquote></td>
<td>I</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,FOURTEEN 000-45-7212</p>
<p>JUL 31, 2006@09:00</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW) CHOLECYSTECTOMY, APPENDECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SUPERFICIAL WOUND INFECTION * (08/02/06) ANTIBIOTICS</p>
</blockquote></td>
<td>I</td>
</tr>
</tbody>
</table>

> OUTCOMES: U - UNRESOLVED, I - IMPROVED, W - WORSE, D - DEATH

> '\*' Represents Postoperative Occurrences

> Example 3: Printing the Perioperative Occurrences Report – Sorted by Occurrence Category

> Select Perioperative Occurrences Menu Option: M Morbidity & Mortality Reports

#### report follows 

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE REVIEWED BY: PERIOPERATIVE OCCURRENCES-INTRAOP/POSTOP DATE REVIEWED:

> FROM: JUN 1,2007 TO: JUN 30,2007 DATE PRINTED: AUG 22,2007

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 31%" />
<col style="width: 37%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>ATTENDING SURGEON</p>
</blockquote></th>
<th><blockquote>
<p>OCCURRENCE(S) - (DATE)</p>
</blockquote></th>
<th><blockquote>
<p>OUTCOME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID#</p>
</blockquote></td>
<td><blockquote>
<p>SURGICAL SPECIALTY</p>
</blockquote></td>
<td><blockquote>
<p>TREATMENT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OPERATION DATE</p>
</blockquote></td>
<td><blockquote>
<p>PRINCIPAL OPERATION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> CATEGORY: ACUTE RENAL FAILURE

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 36%" />
<col style="width: 32%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></th>
<th><blockquote>
<p>SURGEON,TWO</p>
</blockquote></th>
<th><blockquote>
<p>ACUTE RENAL FAILURE</p>
</blockquote></th>
<th>I</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JUN 18, 2007@07:15</p>
</blockquote></td>
<td><blockquote>
<p>REPAIR INCARCERATED INGUINAL HERNIA</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> OUTCOMES: U - UNRESOLVED, I - IMPROVED, W - WORSE, D - DEATH

> '\*' Represents Postoperative Occurrences

#### (This page included for two-sided copying.)

> Example 4: Printing the *Mortality Report*

> Select Perioperative Occurrences Menu Option: M Morbidity & Mortality Reports

#### report follows 

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 42%" />
<col style="width: 20%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>MAYBERRY, NC</p>
<p>SURGICAL SERVICE</p>
</blockquote></th>
<th><blockquote>
<p>REVIEWED BY:</p>
</blockquote></th>
<th><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>MORTALITY REPORT</p>
</blockquote></td>
<td><blockquote>
<p>DATE REVIEWED:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>FROM: JAN 1,2006 TO: JUL 31,2006</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DATE PRINTED: AUG 22,2006</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OPERATION DATE</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ID#</p>
</blockquote></td>
<td><blockquote>
<p>PRINCIPAL OPERATIVE PROCEDURE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DATE OF DEATH AUTOPSY (Y/N)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> OTORHINOLARYNGOLOGY (ENT)

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 23%" />
<col style="width: 51%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>JAN 22, 2006</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,SIXTEEN 000-11-1111</p>
</blockquote></th>
<th><blockquote>
<p>LARYNGOSCOPY, BRONCHOSCOPY, ESOPHAGOGASTROSCOPY</p>
</blockquote></th>
<th><blockquote>
<p>FEB 09, 2006 NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>JAN 27, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWO 000-45-1982</p>
</blockquote></td>
<td><blockquote>
<p>BRONCHOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>FEB 26, 2006 NOT AVAILABLE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JAN 29, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTEEN 000-11-1111</p>
</blockquote></td>
<td><blockquote>
<p>BILATERAL NECK DISECTION, LARYNGECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>FEB 09, 2006 NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FEB 08, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTEEN 000-11-1111</p>
</blockquote></td>
<td><blockquote>
<p>LIGATION LT INTERNAL JUGLAR , EXPLORATORY LAPARATOMY</p>
</blockquote></td>
<td><blockquote>
<p>FEB 09, 2006 NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEB 19, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TEN 000-12-3456</p>
</blockquote></td>
<td><blockquote>
<p>TRACH</p>
</blockquote></td>
<td><blockquote>
<p>FEB 21, 2006 NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JUL 20, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FORTY 000-77-7777</p>
</blockquote></td>
<td><blockquote>
<p>LARYNGOSCOPY W/ BX, ESOPHAGOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>NOV 01, 2006 NOT AVAILABLE</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Non-O.R. Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRONOP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](surgery-version-3-user-manual-updated-sr-3-184/037.png)The *Non-O.R. Procedures* option, located in the main *Surgery Menu* and locked with the SROPER key, is designed for documenting and reviewing Non-O.R. Procedures.

> A Non-O.R. Procedure is any procedure not performed in an operating room, but which still involves surgical or anesthesia providers. Any procedures involving anesthesia providers will display on the Anesthesia AMIS Report.

> The main options included in this menu are listed below. The first option, *Non-O.R.. Procedures (Enter Edit)*, contains options to enter or update cases. To the left of the option name is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>E</p>
</blockquote></td>
<td><blockquote>
<p><em>Non-O.R.. Procedures (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Annual Report of Non-O.R.. Procedures</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Non-O.R.. Procedures</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark95" class="anchor"></span>Non-O.R. Procedures (Enter/Edit)

### \[SRONOP-ENTER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Non-O.R. Procedures (Enter/Edit)* option allows the user to enter, edit, or delete information related to a Non-O.R. Procedure. The editing feature branches to another submenu that allows the user to enter or edit anesthesia information for a procedure. To use one of the *Non-O.R. Procedures (Enter/Edit)* options, the user must first identify the patient on which he or she is working.

> Accessing the Non-O.R. Procedures Menu

> When the *Non-O.R. Procedures (Enter/Edit)* option is selected, the user will be prompted to enter a patient name. The Surgery software will then list all non-O.R. procedures on record for the patient.

> The user can select from the procedure(s) listed or enter a new procedure. When selecting an existing procedure, the software will ask whether the user wants to 1) edit information for the case, or 2) delete the procedure, as follows.

> If the user enters 2 to delete, the software will permanently remove the procedure from the records. On the other hand, if the user accepts the default answer, 1, to edit the existing procedure, the software will display the *Non-O.R. Procedures (Enter/Edit)* menu option. The user will see the following options.

> Three of these sub-options, the *Anesthesia Information (Enter/Edit)* option, the *Medications (Enter/Edit)* option, and the *Anesthesia Technique (Enter/Edit)* option, are the same as the sub-options of the same name on the *Anesthesia Menu* option.

## Edit Non-O.R. Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRONOP-EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Edit Non-O.R. Procedure* option on the *Non-O.R. Procedures* menu allows the user to enter or edit data on the selected procedure.

> The DICTATED SUMMARY EXPECTED field is used to determine whether a dictated summary will be required for this Non-O.R. Procedure case. If NO is entered into the DICTATED SUMMARY EXPECTED field, no alerts will be generated and no report information will be displayed. If YES is entered into the DICTATED SUMMARY EXPECTED field, an alert will be sent to the appropriate provider when the dictated summary is uploaded, informing him or her that the Procedure Summary is ready for signature.

> ![](surgery-version-3-user-manual-updated-sr-3-184/038.png)The DICTATED SUMMARY EXPECTED field is used to determine whether a dictated summary will be required for a Non-O.R. Procedure case.

> Example: Setting the DICTATED SUMMARY EXPECTED field to YES

> If the user wishes to edit information in the Procedure Report (Non-O.R.), the *Edit Non-O.R.. Procedure*

> option on the *Non-O.R.. Procedures* menu can be used.

> Example: Using the Edit Non-O.R. Procedure option

## Procedure Report (Non-O.R.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR NON-OR REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Procedure Report (Non-O.R..)* option details operation information for the patient case selected. This report includes the Procedure Summary section. The Procedure Summary is dictated by the provider after completing the Non-O.R. procedure and then is electronically signed.

> Prior to Signature

> The *Edit Non-O.R. Procedure* option on the *Non-O.R. Procedures* menu is used to enter the non-O.R. procedure data. The DICTATED SUMMARY EXPECTED field is used to determine whether a dictated summary will be required for this non-O.R. procedure. This field is a required entry when creating a new non-O.R. procedure and may be edited using the *Edit Non-O.R. Procedure* option. Entering YES in this field allows a Procedure Summary to be uploaded and signed in TIU, making a Procedure Report (Non- O.R.) available for this procedure.

> ![](surgery-version-3-user-manual-updated-sr-3-184/039.png)The DICTATED SUMMARY EXPECTED field is used to determine whether a dictated summary will be required for a Non-O.R. Procedure case.

> After the Procedure Summary has been electronically signed, the Procedure Report (Non-O.R..) is viewable through CPRS. If the Procedure Summary has not been electronically signed, the following displays:

> "\* \* A Non-O.R. Procedure Summary is not available. \* \*"

> ![](surgery-version-3-user-manual-updated-sr-3-184/040.png)After the Procedure Summary is transcribed and uploaded into TIU, the TIU software sends an alert to the provider responsible for electronically signing the report. The provider can then sign using CPRS options or the List Manager.

> After Electronic Signature

> After electronic signature, the report is available for viewing.

> Example 1: Printing a Procedure (Non-O.R.) Report when the Procedure Summary has been signed

> *report follows*

> SURPATIENT,ONE 000-44-7629 PROCEDURE REPORT NOTE DATED: 02/13/2002 00:00 PROCEDURE REPORT

> SUBJECT: Case \#: 267236

> PREOPERATIVE DIAGNOSIS: RESPIRATORY FAILURE, PROLONGED TRACHEAL INTUBATION

> AND FAILURE TO WEAN POSTOPERATIVE DIAGNOSIS: SAME

> PROCEDURE PERFORMED: OPEN TRACHEOSTOMY PROVIDER: DR. SURSURGEON

> ASSISTANT PROVIDER:

> ANESTHESIA: GENERAL ENDOTRACHEAL ANESTHESIA ESTIMATED BLOOD LOSS: MINIMAL COMPLICATIONS: NONE

> INDICATIONS FOR PROCEDURE: The patient is a sixty-four-year-old gentleman with a rather extensive past surgical history, mostly significant for status post esophagogastrectomy and presented to the hospital approximately three weeks ago with abdominal pain. Diagnostic evaluation consisted of an abdominal CT scan, liver function tests and right upper quadrant ultrasound, all of which were consistent with a diagnosis of acalculus cholecystitis. Because of these findings, the patient was brought to the operating room approximately

> three weeks ago where an open cholecystectomy was performed. The patient subsequent to that has had a very rocky postoperative course, most significantly focusing around persistently spiking fevers with sources significant for an E-coli sinusitis as well as a Staphylococcus E-coli pneumonia with no evidence of bacteremia. As a result of all of this sepsis and persistent spiking fevers, the patient has had a pneumonia, the patient has had a rather difficult time weaning from the ventilator and because of the

> almost three week period since his last operation with persistent endotracheal tube in place, the patient was brought to the operating room for an open tracheostomy procedure.

> DESCRIPTION OF PROCEDURE: After appropriate consent was obtained from the patient's next of kin and the risks and benefits were explained to her, the patient was then brought to the operating room where general endotracheal anesthesia was induced. The area was prepped and draped in the usual fashion with a towel roll under the patient's scapula and the neck extended.

> A longitudinal incision of approximately 2 cm was made just below the cricoid cartilage. The strap muscles were taken down using Bovee electrocautery. The isthmus of the thyroid was clamped and tied off using 2-0 silk x two.

> Hemostasis was assured. The thyroid cartilage was carefully dissected directly onto it. The window in the third ring of the trachea was opened after placement of retraction sutures of 0 silk, The hatch was cut open using a hatch box shape. This opening was then dilated using the tracheal dilator. The endotracheal tube was pulled back. A \#7 Tracheostomy tube was placed with ease. Breath sounds were assured. The patient was oxygenating well and the stay sutures were placed. The patient tolerated the procedure well. The skin was closed with 0 silk and trachea tip was applied. The patient tolerated the procedure well. The endotracheal tube was finally removed. He was brought to the Surgical Intensive Care Unit in stable, but critical condition.

> Three Sursurgeon, M.D.

> TS/jer:jw J#: 514 DD: 02-13-02 DT: 02-13-02

> Signed by: /es/ THREE SURSURGEON

> 02/13/2002 16:40

> Enter RETURN to continue or '^' to exit: ^

## Tissue Examination Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROTRPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Tissue Examination Report* option is used to generate the Tissue Examination Report that contains information about cultures and specimens sent to the laboratory for a non-OR procedure.

> This report prints in an 80-column format and can be viewed on the screen.

> Example: Tissue Examination Report

> *printout follows*

> MEDICAL RECORD \| TISSUE EXAMINATION

> Specimen Submitted By: Obtained: AUG 13, 2004 OR1, SURGERY CASE \# 267260

> Specimen(s): BIOPSY OF STOMACH LINING

> Brief Clinical History:

> The patient has had a pneumonia, and had a rather difficult time weaning from the ventilator and because of the almost three week period since his last operation with persistent endotracheal tube in place, the

> patient was brought to the operating room for an open tracheostomy procedure.

> Operative Procedure(s):

> OPEN TRACHEOSTOMY

> Preoperative Diagnosis:

> RESPIRATORY FAILURE, PROLONGED TRACHEAL INTUBATION AND FAILURE TO WEAN

> Operative Findings:

> Postoperative Diagnosis: Signature and Title FOREIGN BODY IN TRACHEA SURSURGEON,TWO

> Attending Surgeon: SURSURGEON,ONE

> PATHOLOGY REPORT

> Name of Laboratory Accession Number(s)

Gross Description, Histologic Examination and Diagnosis

(Continue on reverse side)

> PATHOLOGIST'S SIGNATURE DATE:

> SURPATIENT,FIFTEEN (000-98-1234) Age: 64 SEX: MALE ID \# 000-98-1234 ETHNICITY: NOT HISPANIC REGISTER NO.

> RACE: WHITE, ASIAN

> WARD: ROOM-BED:

> VAMC: MAYBERRY, NC REPLACEMENT FORM 515

> Press RETURN to continue

## Non-OR Procedure Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR NON-OR INFO\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Non-OR Procedure Information* option displays information on the selected non-OR procedure, with the exception of the provider's dictated summary.

> This report prints in an 80-column format and can be viewed on the screen.

> Example: Non-OR Procedure Information Report

> *printout follows*

> SURPATIENT,FIFTEEN (000-98-1234) Age: 64 PAGE 1 NON-O.R. PROCEDURE - CASE \#267260 Printed: AUG 13, 2004@14:40

> Med. Specialty: PULMONARY, NON-TB Location: NON OR

> Principal Diagnosis:

> FAILURE TO WEAN

> Provider: SURSURGEON,TWO Patient Status: INPATIENT Attending: SURSURGEON,FIFTEEN

> Attending Code: LEVEL F: NON-OR PROCEDURE DONE IN THE OR, ATTENDING IDENTIFIED

> Attend Anesth: N/A

> Anesthesia Supervisor Code: N/A Anesthetist: N/A

> Anesthesia Technique(s): N/A

> Proc Begin: AUG 13, 2004 09:00 Proc End: AUG 13, 2004 10:00

> Procedure(s) Performed: Principal: OPEN TRACHEOSTOMY

> Indications for Procedure: FOREIGN BODY IN TRACHEA.

> Brief Clinical History:

> The patient is a sixty-four-year-old gentleman with a rather extensive past surgical history, mostly significant for status post esophagogastrectomy and presented to the hospital approximately three weeks ago with abdominal pain.

> Diagnostic evaluation consisted of an abdominal CT scan, liver function tests and right upper quadrant ultrasound, all of which were consistent with a diagnosis of acalculus cholecystitis. Because of these findings,

> the patient was brought to the operating room approximately three weeks ago where an open cholecystectomy was performed.

> Specimens: BIOPSY OF STOMACH LINING.

> Dictated Summary Expected: YES

> Enter RETURN to continue or '^' to exit:

## Annual Report of Non-O.R. Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRONOP-ANNUAL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Annual Report of Non-O.R.. Procedures* option generates the Annual Report of Non-O.R. Procedures. It displays the total number of non-O.R. procedures within the selected date range based on CPT code.

> This report prints in an 80-column format and can be viewed on the screen.

> Example: Annual Report of Non-O.R. Procedures

> Select Non-O.R. Procedures Option: A Annual Report of Non-O.R. Procedures

> *report follows*

## Report of Non-O.R. Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRONOR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report chronologically lists non-O.R. procedures, and can be sorted by specialty, provider, or location.

> This report prints in a 132-column format and must be copied to a printer.

> Example 1: Report of Non-O.R. Procedures by Specialty

> Select Non-O.R. Procedures Option: Report of Non-O.R. Procedures

> *report follows*

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY: REPORT OF NON-O.R. PROCEDURES DATE REVIEWED:

> FROM: MAR 1,1999 TO: MAR 31,1999

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT (ID#)</p>
</blockquote></th>
<th><blockquote>
<p>PROVIDER</p>
</blockquote></th>
<th>START TIME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>LOCATION (IN/OUT-PAT STATUS)</p>
</blockquote></td>
<td><blockquote>
<p>PROCEDURE(S)</p>
</blockquote></td>
<td>FINISH TIME</td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> \*\*\* SPECIALTY: CARDIOLOGY \*\*\*

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 32%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/02/92</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
<th>03/02/92 13:05</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>501</p>
</blockquote></td>
<td><blockquote>
<p>AMBULATORY SURGERY (OUTPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td>03/02/92 14:10</td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/13/92</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td>03/13/92 14:00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>500</p>
</blockquote></td>
<td><blockquote>
<p>ICU (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td>03/13/92 14:25</td>
</tr>
</tbody>
</table>

> Example 2: Report of Non-O.R. Procedures by Provider

#### report follows 

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY: REPORT OF NON-O.R. PROCEDURES DATE REVIEWED:

> FROM: MAR 1,1999 TO: MAR 31,1999

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT (ID#)</p>
</blockquote></th>
<th><blockquote>
<p>SPECIALTY</p>
</blockquote></th>
<th>START TIME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>LOCATION (IN/OUT-PAT STATUS)</p>
</blockquote></td>
<td><blockquote>
<p>PROCEDURE(S)</p>
</blockquote></td>
<td>FINISH TIME</td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

\*\*\* PROVIDER SURSURGEON,SIXTEEN \*\*\*

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 35%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/12/92</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TWO (000-45-1982)</p>
</blockquote></th>
<th><blockquote>
<p>PSYCHIATRY</p>
</blockquote></th>
<th>03/12/92 08:00</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>195</p>
</blockquote></td>
<td><blockquote>
<p>PAC(U) - ANESTHESIA (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>ELECTROCONVULSIVE THERAPY</p>
</blockquote></td>
<td>03/12/92 09:00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/23/92</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,NINE (000-34-5555)</p>
</blockquote></td>
<td><blockquote>
<p>PSYCHIATRY</p>
</blockquote></td>
<td>03/23/92 08:10</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>240</p>
</blockquote></td>
<td><blockquote>
<p>PAC(U) - ANESTHESIA (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>ELECTROCONVULSIVE THERAPY</p>
</blockquote></td>
<td>03/23/92 08:40</td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/25/92</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOURTEEN (000-45-7212)</p>
</blockquote></td>
<td><blockquote>
<p>PSYCHIATRY</p>
</blockquote></td>
<td>03/12/92 09:30</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>266</p>
</blockquote></td>
<td><blockquote>
<p>PAC(U) - ANESTHESIA (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>ELECTROCONVULSIVE THERAPY</p>
</blockquote></td>
<td>03/12/92 10:15</td>
</tr>
</tbody>
</table>

> Example 3: Report of Non-O.R. Procedures by Location

#### report follows 

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY: REPORT OF NON-O.R. PROCEDURES DATE REVIEWED:

> FROM: MAR 1,1999 TO: MAR 31,1999

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 33%" />
<col style="width: 32%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT (ID#)</p>
</blockquote></th>
<th><blockquote>
<p>PROVIDER</p>
</blockquote></th>
<th>START TIME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>SPECIALTY (IN/OUT-PAT STATUS)</p>
</blockquote></td>
<td><blockquote>
<p>PROCEDURE(S)</p>
</blockquote></td>
<td>FINISH TIME</td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> \*\*\* LOCATION: AMBULATORY SURGERY \*\*\*

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 35%" />
<col style="width: 33%" />
<col style="width: 17%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/02/92</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
<th>03/02/92</th>
<th><blockquote>
<p>13:05</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>201</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOLOGY (OUTPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td>03/02/92</td>
<td><blockquote>
<p>14:10</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/06/92</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWENTY (000-45-4886)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td>03/07/92</td>
<td><blockquote>
<p>16:30</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>198</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(ACUTE MEDICINE) (OUTPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>EXCISION OF SKIN LESION</p>
</blockquote></td>
<td>03/07/92</td>
<td><blockquote>
<p>17:08</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/09/92</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTY (000-45-9999)</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,ONE</p>
</blockquote></td>
<td>03/09/92</td>
<td><blockquote>
<p>09:45</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>193</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(ACUTE MEDICINE) (OUTPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>STELLATE NERVE BLOCK</p>
</blockquote></td>
<td>03/09/92</td>
<td><blockquote>
<p>10:21</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/13/92</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td>03/13/92</td>
<td><blockquote>
<p>14:00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOLOGY (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td>03/13/92</td>
<td><blockquote>
<p>14:25</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/17/92</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,EIGHTEEN (000-22-3334)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td>03/17/92</td>
<td><blockquote>
<p>13:30</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>191</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL SURGERY (OUTPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>EXCISION OF SKIN LESION</p>
</blockquote></td>
<td>03/17/92</td>
<td><blockquote>
<p>14:42</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Comments Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROMEN-COM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgeons use the *Comments* option to respond to the GENERAL COMMENTS field for a surgical case or non-O.R. procedure. This option is designed to give surgeons an opportunity to directly add general comments after a case has been booked. The GENERAL COMMENTS field may already contain information added by the person booking the operation.

> After selecting the patient case, the surgeon can add the general comments using the VA FileMan word- processing device, demonstrated below. The surgeon must press the \<Enter\> key at the end of each line with this type of word processing. The surgeon would press the \<Enter\> key again when he or she is through with the comments.

> Example: Enter General Comments

> Select Surgery Menu Option: C Comments

> *(This page included for two-sided copying.)*

# CPT/ICD Coding Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRCODING MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery *CPT/I*<span id="_bookmark104" class="anchor"></span>*CD Coding Menu* option was developed to help assure access to the most accurate source documentation and to provide a means for efficient coding entry and validation. It provides coders with special, limited access to the VistA Surgery package.

> From the menu, coders have ready access to the Operation Report, which is dictated by the surgeon postoperatively and contains the most comprehensive and accurate description of the procedure(s) actually performed. Coders can also view the Nurse Intraoperative Report, which is often an important supplementary source of data.

> Using the same menu, coders can add and edit procedures, CPT codes, diagnoses, and International Classification of Diseases (ICD) codes, without having to rely on a paper-based system. Options are available to assist surgery staff and others who perform coding validation, as are several commonly used reports.

> The *Surgery CPT/ICD Coding Menu* contains the following options. To the left is the shortcut synonym the user can enter to select the option:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>EDIT CPT/ICD</p>
</blockquote></td>
<td><blockquote>
<p><em>Update/Verify Menu</em> ...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p><em>Cumulative Report of CPT Codes</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of CPT Coding Accuracy</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p><em>List Completed Cases Missing CPT Codes</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Operations</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LS</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Operations (by Surgical Specialty)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Undictated Operations</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Daily Operating Room Activity</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PS</p>
</blockquote></td>
<td><blockquote>
<p><em>PCE Filing Status Report</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Non-O.R. Procedures</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark105" class="anchor"></span>CPT/ICD Update/Verify Menu

### \[SRCODING UPDATE/VERIFY MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](surgery-version-3-user-manual-updated-sr-3-184/041.png) The *CPT/ICD Update/Verify Menu* is locked with the SR CODER security key. This option provides coding personnel with access to review and edit procedure and diagnosis information. It also provides access to the Operation Report and Nurse Intraoperative Report for operations and to the Procedure Report (Non-O.R.) for non-O.R. procedures.

> The *CPT/ICD Update/Verify Menu* contains the following options. To the left is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>UV</p>
</blockquote></td>
<td><blockquote>
<p><em>Update/Verify Procedure/Diagnosis Codes</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation/Procedure Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NR</p>
</blockquote></td>
<td><blockquote>
<p><em>Nurse Intraoperative Report</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PI</p>
</blockquote></td>
<td><blockquote>
<p><em>Non-OR Procedure Information</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> To access the *CPT/ICD Update/Verify Menu*, the user must first identify the patient and case. When the user selects EDIT for the *CPT/ICD Update/Verify Menu* from the *CPT/ICD Coding Menu*, the user will be prompted to enter a patient name. The software will then list all the cases on record for the patient, including any operations that are completed or are in progress and any non-O.R. procedures.

> From this point, the user can select any of the *CPT/ICD Update/Verify Menu* options.

## Update/Verify Procedure/Diagnosis Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRCODING EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update/Verify Procedure/Diagnosis Codes* option allows the user to enter the final codes and associated information required for PCE upon completion of a Surgery case.

> ![](surgery-version-3-user-manual-updated-sr-3-184/042.png)The procedure and diagnoses codes entered/edited through this option will be the coded information that is sent to the Patient Care Encounter (PCE) package. After the case is coded, the user will select to send the information to PCE.

> When the user first edits a case through this option, the values will be pre-populated, using the values for planned codes entered by the nurse or surgeon. If there is no Planned Principal Procedure Code or no Principal Pre-op Diagnosis Code, then the Surgery software will prompt for the final CPT and ICD codes.

> Because a case can have more than one procedure and/or diagnosis, the user can associate one or more diagnosis with each procedure. The Surgery software displays the diagnoses in the order in which the user entered them in the case. The user can then associate and reorder the relevant diagnoses to each procedure.

> The user can also edit the service classifications for the Postoperative Diagnoses.

> The following examples depict using the *Update/Verify Procedure/Diagnosis Codes* option to edit a Bronchoscopy, with no planned CPT or ICD codes entered by a clinician.

> Example: Entering Required Information

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 17%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719) Case #10062</p>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote>
<ol type="1">
<li><p>Principal Postop Diagnosis Code: NOT ENTERED</p></li>
<li><p>Other Postop Diagnosis Code: NOT ENTERED</p></li>
<li><blockquote>
<p>Principal CPT Code: NOT ENTERED Assoc. DX:</p>
</blockquote></li>
</ol>
<blockquote>
<p>NO Assoc. DX ENTERED</p>
</blockquote>
<ol start="4" type="1">
<li><p>Other CPT Code: NOT ENTERED</p></li>
</ol></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>The following information is required before continuing.</p>
<p>Principal Postop Diagnosis Code (ICD):<strong>934.0</strong> 934.0 FOREIGN BODY IN TRACHEA</p>
<p>...OK? Yes// (Yes) &lt;Enter&gt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Because the patient has a service-connected status, the Surgery software displays a service-connected prompt:

> Note that when a Postop Diagnosis Code is entered, it is automatically associated to a Principal CPT code, even if a CPT code is not entered.

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 17%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719) Case #10062</p>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th rowspan="5"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><ol type="1">
<li><p>Principal Postop Diagnosis Code: 934.0 FOREIGN BODY IN TRACHEA</p></li>
<li><p>Other Postop Diagnosis Code: NOT ENTERED</p></li>
<li><p>Principal CPT Code: NOT ENTERED</p></li>
</ol>
<blockquote>
<p>Assoc. DX: 934.0 -FOREIGN BODY IN TRACHEA</p>
</blockquote>
<ol start="4" type="1">
<li><p>Other CPT Code: NOT ENTERED</p></li>
</ol></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>The following information is required before continuing.</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Principal Procedure Code (CPT): <strong>31622</strong> DX BRONCHOSCOPE/WASH BRONCHOSCOPY, RIGID OR FLEXIBLE, WITH OR WITHOUT FLUOROSCOPIC DIAGNOSTIC, WITH OR WITHOUT CELL WASHING (SEPARATE PROCEDURE)</p>
<p>Modifier: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
<th>GUIDANCE;</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#10062</p>
</blockquote></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>1. Principal Postop Diagnosis Code: 934.0 FOREIGN</p>
</blockquote></th>
<th><blockquote>
<p>BODY</p>
</blockquote></th>
<th><blockquote>
<p>IN</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TRACHEA</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>2. Other Postop Diagnosis Code: NOT ENTERED</p>
</blockquote></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>3. Principal CPT Code: 31622 DX BRONCHOSCOPE/WASH</p>
</blockquote></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Assoc. DX: 934.0 FOREIGN BODY IN TRACHEA</p>
</blockquote></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>4. Other CPT Code: NOT ENTERED</p>
</blockquote></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>Enter number of item to edit (1-4):</p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Because all required information is now entered, the user can select to automatically send the information to PCE, or wait until other information is entered.

> Example: Editing the Principal CPT Code

<table style="width:100%;">
<colgroup>
<col style="width: 36%" />
<col style="width: 15%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
</blockquote></th>
<th colspan="4" rowspan="2"></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#10062</p>
</blockquote></th>
<th rowspan="9"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th colspan="7"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>1. Principal Postop Diagnosis Code: 934.0 FOREIGN</p>
</blockquote></th>
<th><blockquote>
<p>BODY</p>
</blockquote></th>
<th><blockquote>
<p>IN</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TRACHEA</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>2. Other Postop Diagnosis Code: NOT ENTERED</p>
</blockquote></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>3. Principal CPT Code: 31622 DX BRONCHOSCOPE/WASH</p>
</blockquote></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Assoc. DX: 934.0 FOREIGN BODY IN TRACHEA</p>
</blockquote></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>4. Other CPT Code: NOT ENTERED</p>
</blockquote></th>
<th></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Enter number of item to edit (1-4):</p>
</blockquote></th>
<th colspan="4"><blockquote>
<p><strong>3</strong></p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](surgery-version-3-user-manual-updated-sr-3-184/043.png)Editing or deleting any diagnosis or procedures may cause any associated diagnoses to be incorrect; the software prompts the user to check any diagnosis to procedure associations. The user can select to delete all associated diagnoses, or keep all associations.

> Example: Entering a New Other Procedure CPT Code

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 20%" />
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th colspan="3"></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#10062</p>
</blockquote></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>1. Principal Postop Diagnosis Code: 934.0 FOREIGN BODY</p>
</blockquote></th>
<th><blockquote>
<p>IN</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TRACHEA</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>2. Other Postop Diagnosis Code: NOT ENTERED</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>3. Principal CPT Code: 31623 DX BRONCHOSCOPE/BRUSH</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Assoc. DX: 934.0 FOREIGN BODY IN TRACHEA</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>4. Other CPT Code: NOT ENTERED</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Enter number of item to edit (1-4):</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>4</strong></p>
</blockquote></th>
<th colspan="2"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 31%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
</blockquote></th>
<th><blockquote>
<p>Case #10062</p>
</blockquote></th>
<th rowspan="9"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>1. Enter NEW Other Procedure</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Enter selection: (1-1): <strong>1</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Enter new OTHER PROCEDURE CPT code: <strong>43200</strong> ESOPHAGUS ENDOSCOPY</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>ESOPHAGOSCOPY, RIGID OR FLEXIBLE; DIAGNOSTIC, WITH OR WITHOUT COLLECTION</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>OF SPECIMEN(S) BY BRUSHING OR WASHING (SEPARATE PROCEDURE)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Modifier: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> All procedures must be associated with a diagnosis; the Surgery software allows the user to associate any or all available diagnoses to a single procedure. If more than one diagnosis if available, then the user enters the associations sequentially for the association.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 31%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th><blockquote>
<p>Case #10062</p>
</blockquote></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>1. CPT Code: 43200 ESOPHAGUS ENDOSCOPY Modifiers: NOT ENTERED</p>
<p>Assoc. DX: NOT ENTERED</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Only the following ICD Diagnosis Codes can be associated:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>1. 934.0-FOREIGN BODY IN TRACHEA</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Select the number(s) of the Diagnosis Code to associate to the procedure selected: 1// <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 31%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
</blockquote></th>
<th><blockquote>
<p>Case #10062</p>
</blockquote></th>
<th rowspan="7"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>1. CPT Code: 43200 ESOPHAGUS ENDOSCOPY</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Assoc. DX: 934.0-FOREIGN BODY IN TRACHE</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>2. Enter NEW Other Procedure Code</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Enter selection: (1-2): <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 31%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th><blockquote>
<p>Case #10062</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><ol type="1">
<li><p>Principal Postop Diagnosis Code: 934.0 FOREIGN BODY IN TRACHEA</p></li>
<li><p>Other Postop Diagnosis Code: NOT ENTERED</p></li>
<li><blockquote>
<p>Principal CPT Code: 31623 DX BRONCHOSCOPE/BRUSH Assoc. DX: 934.0-FOREIGN BODY IN TRACHE</p>
</blockquote></li>
<li><blockquote>
<p>Other CPT Code: 43200 ESOPHAGUS ENDOSCOPY Assoc. DX: 934.0-FOREIGN BODY IN TRACHE</p>
</blockquote></li>
</ol></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Enter number of item to edit (1-4):</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Editing Service Connected/Environmental Indicators (SC/EIs)

> To edit service connected or environmental indicators, the user selects either the Principal Postop Diagnosis Code or the Other Postop Diagnosis Code. The Principal Postop Diagnosis Code and Other Postop Diagnosis Code fields indicate ICD-9 or ICD-10 codes.

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PTFPATIENT,TEST MALE (000-00-1234) Case #33</p>
<p>OCT 04, 2013 REMOVE FOOT</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote>
<ol type="1">
<li><p>Principal Postop Diagnosis Code (ICD10): R44.0 Auditory hallucinations</p></li>
<li><p>Other Postop Diagnosis Code (ICD10): G20. Parkinson's disease</p></li>
<li><blockquote>
<p>Principal CPT Code: 20838 REPLANTATION FOOT COMPLETE Assoc. DX(ICD10): R44.0-Auditory hallucination</p>
</blockquote></li>
<li><p>Other CPT Code: NOT ENTERED</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Enter number of item to edit (1-4): <strong>1</strong></p>
<p>PTFPATIENT,TEST MALE (000-00-1234) Case #33</p>
<p>OCT 04, 2013 REMOVE FOOT</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Principal Postop Diagnosis:</p>
<p>ICD10 Code: R44.0 Auditory hallucinations SC:N</p>
<p>Select one of the following:</p>
</blockquote>
<ol type="1">
<li><p>Update Principal Postop Diagnosis Code</p></li>
<li><blockquote>
<p>Update Service Connected/Environmental Indicators only Enter selection (1 or 2): 1// <strong>1 Update Principal Postop Diagnosis Code</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Principal Postop Diagnosis Code (ICD10): R44.0// TRACHAE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The information displayed for this patient show Service Connected status of less than 50%, and the Agent Orange Exposure and Ionizing Radiation indicators associated with the diagnosis. The software gives the user the option to update all diagnoses with the same service-connected indicators simultaneously.

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 31%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>JUN 08, 2005 BRONCHOSCOPY</p>
</blockquote></th>
<th><blockquote>
<p>Case #10062</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><ol type="1">
<li><p>Principal Postop Diagnosis Code: 934.0 FOREIGN BODY IN TRACHEA</p></li>
<li><p>Other Postop Diagnosis Code: NOT ENTERED</p></li>
<li><blockquote>
<p>Principal CPT Code: 31623 DX BRONCHOSCOPE/BRUSH Assoc. DX: 934.0-FOREIGN BODY IN TRACHE</p>
</blockquote></li>
<li><blockquote>
<p>Other CPT Code: 43200 ESOPHAGUS ENDOSCOPY Assoc. DX: 934.0-FOREIGN BODY IN TRACHE</p>
</blockquote></li>
</ol></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Enter number of item to edit (1-4):</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The following examples depict using the *Update/Verify Procedure/Diagnosis Codes* option to edit a cardiac procedure (CABG), with clinician-entered Planned CPT and IC<span id="_bookmark107" class="anchor"></span>D codes.

> Example: Editing Final Codes and Sending the Case to PCE

> Because the nurse or surgeon entered a Planned Principal CPT Code and a Preoperative Diagnosis Code, the corresponding fields pre-fill with those clinician-entered values when the user accesses the case through the *Update/Verify Procedure/Diagnosis Codes* option.

> The user can either accept the codes that have been pre-operatively entered, or the user can edit the codes as necessary. In this example, the codes will be adjusted to accurately reflect the procedures by adding Other Postop Diagnosis Codes and Other CPT Codes.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 15%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 10%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN JUL 15, 2005 CABG</p>
</blockquote></th>
<th>(000-45-5119)</th>
<th></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>#314</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="9"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="5"><ol type="1">
<li><p>Principal Postop Diagnosis Code: 402.01 HYP HEART</p></li>
<li><p>Other Postop Diagnosis Code: NOT ENTERED</p></li>
<li><blockquote>
<p>Principal CPT Code: 33510 CABG, VEIN, SINGLE Assoc. DX: 402.01-HYP HEART DIS MALIGN</p>
</blockquote></li>
<li><p>Other CPT Code: NOT ENTERED</p></li>
</ol></th>
<th><blockquote>
<p>DIS</p>
</blockquote></th>
<th><blockquote>
<p>MALIGN</p>
</blockquote></th>
<th><blockquote>
<p>WITH</p>
</blockquote></th>
<th><blockquote>
<p>FAIL</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Enter number of item</p>
</blockquote></th>
<th>to edit (1-4):</th>
<th><blockquote>
<p><strong>2</strong></p>
</blockquote></th>
<th></th>
<th colspan="5"></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The ICD Code fields below indicate ICD-9 or ICD-10 codes.

> Example: ICD-9 Code

> Now the Other CPT Code will be entered.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 15%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 33%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN JUL 15, 2005 CABG</p>
</blockquote></th>
<th>(000-45-5119)</th>
<th></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#314</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="5"><ol type="1">
<li><p>Principal Postop Diagnosis Code: 402.01 HYP HEART DIS MALIGN WITH FAIL</p></li>
<li><p>Other Postop Diagnosis Code: 599.0 URIN TRACT INFECTION NOS</p></li>
<li><blockquote>
<p>Principal CPT Code: 33510 CABG, VEIN, SINGLE Assoc. DX: 402.01-HYP HEART DIS MALIGN</p>
</blockquote></li>
<li><p>Other CPT Code: NOT ENTERED</p></li>
</ol></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Enter number of item</p>
</blockquote></th>
<th>to edit (1-4):</th>
<th><blockquote>
<p><strong>4</strong></p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 41%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></th>
<th><blockquote>
<p>(000-45-5119)</p>
</blockquote></th>
<th><blockquote>
<p>Case #314</p>
</blockquote></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUL 15, 2005 CABG</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>1. Enter NEW Other Procedure Code</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Enter selection: (1-1): <strong>1</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Enter new OTHER PROCEDURE CPT code: <strong>33510</strong> CABG, VEIN, SINGLE</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>CORONARY ARTERY BYPASS, VEIN ONLY; SINGLE CORONARY VENOUS GRAFT</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Modifier: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: ICD-10 Code

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SRPATIENTA, ONE (000-12-3456) Case #45731</p>
<p>FEB 27, 2014 HEART TRANSPLANT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Other Postop Diagnosis:</p>
</blockquote>
<ol type="1">
<li><p>ICD10 Code:E83.41 Hypermagnesemia</p></li>
<li><blockquote>
<p>ICD10 Code: V72. 1XXD Passenger on bus injured in clsn w 2/3-whl mv momtraf, Subs</p>
</blockquote></li>
<li><blockquote>
<p>Enter NEW Other Postop Diagnosis Code Enter selection: (1-3): 1</p>
</blockquote></li>
</ol>
<blockquote>
<p>SRPATIENTA, ONE (xxx-xx-xxxx) Case #45731 FEB 27, 2014 HEART TRANSPLANT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Other Postop Diagnosis:</p>
</blockquote>
<ol type="1">
<li><p>ICD10 Code: E83.41 Hypermagnesemia Select one of the following</p>
<ol type="1">
<li><p>Update Other Postop Diagnosis Code</p></li>
<li><blockquote>
<p>Update Service Connected/Environmental Indicators only Enter selection (1 or 2): 1//</p>
</blockquote></li>
</ol></li>
</ol></td>
</tr>
</tbody>
</table>

> When additional diagnoses and procedure codes are entered, the user should review the procedure to diagnosis associations to ensure that the associations are correct. In this example, additional associations will be assigned.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 41%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN JUL 15, 2005 CABG</p>
</blockquote></th>
<th><blockquote>
<p>(000-45-5119)</p>
</blockquote></th>
<th><blockquote>
<p>Case #314</p>
</blockquote></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>1. CPT Code: 33510 CABG, VEIN, SINGLE Modifiers: NOT ENTERED</p>
<p>Assoc. DX: NOT ENTERED</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Only the following ICD Diagnosis Codes can be associated:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><ol type="1">
<li><p>402.01-HYP HEART DIS MALIGN WITH FAIL</p></li>
<li><p>599.0-URIN TRACT INFECTION NOS</p></li>
</ol></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Select the number(s) of the Diagnosis Code to associate to the procedure selected: 1// <strong>1,2</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN (000-45-5119) Case #314</p>
</blockquote></th>
<th rowspan="7"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUL 15, 2005 CABG</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>1. CPT Code: 33510 CABG, VEIN, SINGLE</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Assoc. DX: 402.01-HYP HEART DIS MALIGN 599.0-URIN TRACT INFECTION N</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>2. Enter NEW Other Procedure Code</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Enter selection: (1-2): <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The Surgery case displays the updated values.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 41%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN JUL 15, 2005 CABG</p>
</blockquote></th>
<th><blockquote>
<p>(000-45-5119)</p>
</blockquote></th>
<th><blockquote>
<p>Case #314</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><ol type="1">
<li><p>Principal Postop Diagnosis Code: 402.01 HYP HEART DIS MALIGN WITH FAIL</p></li>
<li><p>Other Postop Diagnosis Code: 599.0 URIN TRACT INFECTION NOS</p></li>
<li><blockquote>
<p>Principal CPT Code: 33510 CABG, VEIN, SINGLE Assoc. DX: 402.01-HYP HEART DIS MALIGN</p>
</blockquote></li>
<li><p>Other CPT Code: 33510 CABG, VEIN, SINGLE</p></li>
</ol>
<blockquote>
<p>Assoc. DX: 402.01-HYP HEART DIS MALIGN 599.0-URIN TRACT INFECTION N</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Enter number of item to edit (1-4): <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Because the coding for the case is completed, the user can select to stop editing the case and send the case to PCE.

> Prior to sending the case to PCE, the Surgery software checks to see if a specific code, 065.0

> ![](surgery-version-3-user-manual-updated-sr-3-184/044.png)CRIMEAN HEMORRHAGIC FEV, is entered as a diagnosis code. If it is entered, the software prompts the user to make sure that the code is correct for the specified case. This check is added to prevent the inadvertent assignment of code 065.0 when "CHF" is entered for the Principal or Other ICD Diagnosis codes.

> After the case has been sent to PCE, any changes made to the case through the Update/Verify Procedure/Diagnosis Codes option will be automatically sent to PCE.

> Example: Editing a Case After Sending to PCE

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 41%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN JUL 15, 2005 CABG</p>
</blockquote></th>
<th><blockquote>
<p>(000-45-5119)</p>
</blockquote></th>
<th><blockquote>
<p>Case #314</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><ol type="1">
<li><p>Principal Postop Diagnosis Code: 402.01 HYP HEART DIS MALIGN WITH FAIL</p></li>
<li><p>Other Postop Diagnosis Code: 599.0 URIN TRACT INFECTION NOS</p></li>
<li><blockquote>
<p>Principal CPT Code: 33510 CABG, VEIN, SINGLE Assoc. DX: 402.01-HYP HEART DIS MALIGN</p>
</blockquote></li>
<li><p>Other CPT Code: 33510 CABG, VEIN, SINGLE</p></li>
</ol>
<blockquote>
<p>Assoc. DX: 402.01-HYP HEART DIS MALIGN 599.0-URIN TRACT INFECTION N</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Enter number of item to edit (1-4): <strong>4</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN (000-45-5119) Case #314</p>
</blockquote></th>
<th rowspan="7"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUL 15, 2005 CABG</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>1. CPT Code: 33510 CABG, VEIN, SINGLE</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Assoc. DX: 402.01-HYP HEART DIS MALIGN 599.0-URIN TRACT INFECTION N</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>2. Enter NEW Other Procedure Code</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Enter selection: (1-2): <strong>1</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 41%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN JUL 15, 2005 CABG</p>
</blockquote></th>
<th><blockquote>
<p>(000-45-5119)</p>
</blockquote></th>
<th><blockquote>
<p>Case #314</p>
</blockquote></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>1. CPT Code: 33517 CABG, ARTERY-VEIN, SINGLE Modifiers: NOT ENTERED</p>
<p>Assoc. DX: NOT ENTERED</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Only the following ICD Diagnosis Codes can be associated:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><ol type="1">
<li><p>402.01-HYP HEART DIS MALIGN WITH FAIL</p></li>
<li><p>599.0-URIN TRACT INFECTION NOS</p></li>
</ol></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Select the number(s) of the Diagnosis Code to associate to the procedure selected: 1// <strong>1,2</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN (000-45-5119) Case #314</p>
</blockquote></th>
<th rowspan="7"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUL 15, 2005 CABG</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Other Procedures:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>1. CPT Code: 33517 CABG, ARTERY-VEIN, SINGLE</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Assoc. DX: 402.01-HYP HEART DIS MALIGN 599.0-URIN TRACT INFECTION N</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>2. Enter NEW Other Procedure Code</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Enter selection: (1-2): <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 18%" />
<col style="width: 41%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN JUL 15, 2005 CABG</p>
</blockquote></th>
<th><blockquote>
<p>(000-45-5119)</p>
</blockquote></th>
<th><blockquote>
<p>Case #314</p>
</blockquote></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Surgery Procedure PCE/Billing Information:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><ol type="1">
<li><p>Principal Postop Diagnosis Code: 402.01 HYP HEART DIS MALIGN WITH FAIL</p></li>
<li><p>Other Postop Diagnosis Code: 599.0 URIN TRACT INFECTION NOS</p></li>
<li><blockquote>
<p>Principal CPT Code: 33510 CABG, VEIN, SINGLE Assoc. DX: 402.01-HYP HEART DIS MALIGN</p>
</blockquote></li>
<li><p>Other CPT Code: 33517 CABG, ARTERY-VEIN, SINGLE</p></li>
</ol>
<blockquote>
<p>Assoc. DX: 402.01-HYP HEART DIS MALIGN 599.0-URIN TRACT INFECTION N</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Enter number of item to edit (1-4): <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>Coding completed and sent to PCE.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Press Enter/Return key to continue</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Operation/Procedure Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRCODING OP REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operation/Procedure Report* option is used by the coders to print the Operation Report for an operation or the Procedure Report (Non-O.R.) for a non-O.R. procedure.

> Any user may print this report, which prints in an 80-column format and can be viewed on the screen or copied to a printer.

> Example 1: Operation Report

> *printout follows*

Page: 1

> SURPATIENT,TEN 000-12-3456 OPERATION REPORT NOTE DATED: 07/29/2003 15:15 OPERATION REPORT

> VISIT: 07/29/2003 15:15 SURGERY OP REPORT NON-COUNT SUBJECT: Case \#: 73285

> PREOPERATIVE DIAGNOSIS: Visually significant cataract, right eye POSTOPERATIVE DIAGNOSIS: Visually significant cataract, right eye PROCEDURE: Phacoemulsification with intraocular lens placement, right eye

> CLINICAL INDICATIONS: This 64-year-old gentleman complains of decreased vision in the right eye affecting his activities of daily living. Best corrected visual acuity is counting fingers at 6 feet, associated with a 2-3+ nuclear sclerotic and 4+ posterior subcapsular cataract in that eye.

> ANESTHESIA: Local monitoring with topical Tetracaine and 1% preservative free Lidocaine.

> DESCRIPTION OF THE PROCEDURE: After the risks, benefits and alternatives of the procedure were explained to the patient, informed consent was obtained. The patient's right eye was dilated with Phenylephrine, Mydriacyl and Ocufen. He was brought to the Operating Room and placed on anesthetic monitors. Topical Tetracaine was given. He was prepped and draped in the usual sterile fashion for eye surgery. A Lieberman lid speculum was placed.

> A Supersharp was used to create a superior paracentesis port. The anterior chamber was irrigated with 1% preservative free Lidocaine. The anterior chamber was filled with Viscoelastic. The diamond groove maker and diamond keratome were used to create a clear corneal tunneled incision at the temporal limbus. The cystotome was used to initiate a continuous capsulorrhexis, which was then completed using Utrata forceps. Balanced salt solution was used to hydrodissect and hydrodelineate the lens.

> Phacoemulsification was used to remove the lens nucleus and epinucleus in a non-stop horizontal chop fashion. Cortex was removed using irrigation and aspiration. The capsular bag was filled with Viscoelastic. The wound was enlarged with a 69 blade. An Alcon model MA60BM posterior chamber intraocular lens with a power of 24.0 diopters, serial \#588502.064, was folded and inserted with the leading haptic placed into the bag. The trailing haptic was dialed into the bag with the Lester hook. The wound was hydrated. The anterior chamber was filled with balanced salt solution. The wound was tested and found to be self-sealing. Subconjunctival antibiotics were given, and an eye shield was placed. The patient was taken in good condition to the Recovery Room. There were no complications.

> KJC/PSI

> DATE DICTATED: 07/29/03 DATE TRANSCRIBED: 07/29/03 JOB: 629095

> Signed by: /es/ FOURTEEN SURSURGEON, M.D.

> 07/30/2003 10:31

> Example 2: Procedure Report (Non-OR)

#### printout follows 

> SURPATIENT,ONE 000-44-7629 PROCEDURE REPORT NOTE DATED: 02/13/2002 00:00 PROCEDURE REPORT

> SUBJECT: Case \#: 267236

> PREOPERATIVE DIAGNOSIS: RESPIRATORY FAILURE, PROLONGED TRACHEAL INTUBATION

> AND FAILURE TO WEAN POSTOPERATIVE DIAGNOSIS: SAME

> PROCEDURE PERFORMED: OPEN TRACHEOSTOMY SURGEON: DR. SURSURGEON

> ASSISTANT SURGEON:

> ANESTHESIA: GENERAL ENDOTRACHEAL ANESTHESIA ESTIMATED BLOOD LOSS: MINIMAL COMPLICATIONS: NONE

> INDICATIONS FOR PROCEDURE: The patient is a forty-nine-year-old gentleman with a rather extensive past surgical history, mostly significant for status post esophagogastrectomy and presented to the hospital approximately three weeks ago with abdominal pain. Diagnostic evaluation consisted of an abdominal CT scan, liver function tests and right upper quadrant ultrasound, all of which were consistent with a diagnosis of acalculus cholecystitis. Because of these findings, the patient was brought to the operating room approximately

> three weeks ago where an open cholecystectomy was performed. The patient subsequent to that has had a very rocky postoperative course, most significantly focusing around persistently spiking fevers with sources significant for an E-coli sinusitis as well as a Staphylococcus E-coli pneumonia with no evidence of bacteremia. As a result of all of this sepsis and persistent spiking fevers, the patient has had a pneumonia, the patient has had a rather difficult time weaning from the ventilator and because of the

> almost three week period since his last operation with persistent endotracheal tube in place, the patient was brought to the operating room for an open tracheostomy procedure.

> DESCRIPTION OF PROCEDURE: After appropriate consent was obtained from the patient's next of kin and the risks and benefits were explained to her, the patient was then brought to the operating room where general endotracheal anesthesia was induced. The area was prepped and draped in the usual fashion with a towel roll under the patient's scapula and the neck extended.

> A longitudinal incision of approximately 2 cm was made just below the cricoid cartilage. The strap muscles were taken down using Bovee electrocautery. The isthmus of the thyroid was clamped and tied off using 2-0 silk x two.

> Hemostasis was assured. The thyroid cartilage was carefully dissected directly onto it. The window in the third ring of the trachea was opened after placement of retraction sutures of 0 silk, The hatch was cut open using a hatch box shape. This opening was then dilated using the tracheal dilator. The endotracheal tube was pulled back. A \#7 Tracheostomy tube was placed with ease. Breath sounds were assured. The patient was oxygenating well and the stay sutures were placed. The patient tolerated the procedure well. The skin was closed with 0 silk and trachea tip was applied. The patient tolerated the procedure well. The endotracheal tube was finally removed. He was brought to the Surgical Intensive Care Unit in stable, but critical condition.

> Three Sursurgeon, M.D.

> TS/jer:jw J#: 514 DD: 02-13-02 DT: 02-13-02

> Signed by: /es/ THREE SURSURGEON

> 02/13/2002 16:40

> Enter RETURN to continue or '^' to exit: ^

## Nurse Intraoperative Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRCODING NURSE REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Nurse Intraoperative Report* option is used by the coders to print the Nurse Intraoperative Report for an operation. This report is not available for non-O.R. procedures.

> This report prints in an 80-column format and can be viewed on the screen or copied to a printer.

> Example: Nurse Intraoperative Report

> *printout follows*

> SURPATIENT,TEN 000-12-3456 NURSE INTRAOPERATIVE REPORT NOTE DATED: 02/12/2004 08:00 NURSE INTRAOPERATIVE REPORT

> SUBJECT: Case \#: 267226

> Operating Room: BO OR1 Surgical Priority: ELECTIVE Patient in Hold: JUL 12, 2004 07:30 Patient in OR: JUL 12, 2004 08:00

> Operation Begin: JUL 12, 2004 08:58 Operation End: JUL 12, 2004 12:10

> Surgeon in OR: JUL 12, 2004 07:55 Patient Out OR: JUL 12, 2004 12:15

> Major Operations Performed:

> Primary: MVR

> Other: ATRIAL SEPTAL DEFECT REPAIR

> Other: TEE

> Wound Classification: CONTAMINATED

> Operation Disposition: SICU Discharged Via: ICU BED

> Primary Surgeon: SURSURGEON,THREE First Assist: SURSURGEON,FOUR Attending Surgeon: SURSURGEON,THREE Second Assist: N/A Anesthetist: SURANESTHETIST,SEVEN Assistant Anesth: N/A

> Other Scrubbed Assistants: N/A OR Support Personnel:

> Scrubbed Circulating

SURNURSE,ONE (FULLY TRAINED) SURNURSE,FIVE (FULLY TRAINED)

SURNURSE,FOUR (FULLY TRAINED)

> Other Persons in OR: N/A

> Preop Mood: ANXIOUS Preop Consc: ALERT-ORIENTED

> Preop Skin Integ: INTACT Preop Converse: N/A

> Valid Consent/ID Band Confirmed By: SURSURGEON,FOUR Mark on Surgical Site Confirmed: YES

> Marked Site Comments: NO COMMENTS ENTERED

> Preoperative Imaging Confirmed: YES

> Imaging Confirmed Comments: NO COMMENTS ENTERED

> Time Out Verification Completed: YES

> Time Out Verified Comments: NO COMMENTS ENTERED

> Skin Prep By: SURNURSE,FOUR Skin Prep Agent: BETADINE SCRUB Skin Prep By (2): SURNURSE,FIVE 2nd Skin Prep Agent: POVIDONE IODINE

> Preop Surgical Site Hair Removal by: SURNURSE,FIVE Surgical Site Hair Removal Method: OTHER

> Hair Removal Comments: SHAVING AND DEPILATORY COMBINATION USED.

> Surgery Position(s):

> SUPINE Placed: N/A

> Restraints and Position Aids:

> SAFETY STRAP Applied By: N/A

> ARMBOARD Applied By: N/A

> FOAM PADS Applied By: N/A

> KODEL PAD Applied By: N/A

> STIRRUPS Applied By: N/A

> Immediate Use Steam Sterilization Episodes: Contamination: 0

> SPS Processing/OR Management Issues: 0 Emergency Case: 0

> No Better Option: 0

> Loaner or Short Notice Instrument: 0

> Decontamination of Instruments Contaminated During the Case: 0

> Electrocautery Unit: 8845,5512 ESU Coagulation Range: 50-35

> ESU Cutting Range: 35-35

Electroground Position(s): RIGHT BUTTOCK

LEFT BUTTOCK

> Material Sent to Laboratory for Analysis:

> Specimens:

1.  MITRAL VALVE Cultures: N/A

> Anesthesia Technique(s):

> GENERAL (PRINCIPAL)

> Tubes and Drains:

> \#16FOLEY, \#18NGTUBE, \#36 &2 \#32RA CHEST TUBES

> Tourniquet: N/A Thermal Unit: N/A Prosthesis Installed:

> Item: MITRAL VALVE

> Implant Sterility Checked (Y/N): YES Sterility Expiration Date: DEC 15, 2004 RN Verifier: SURNURSE,ONE

> Vendor: BAXTER EDWARDS

> Model: 6900

> <span id="_bookmark111" class="anchor"></span>Lot Number: T87-12321 Serial Number: 945673WRU Sterile Resp: MANUFACTURER Size: LG

> Provider Read Back Performed: YES Quantity: 2 Medications: N/A

> Irrigation Solution(s): HEPARINIZED SALINE NORMAL SALINE

> COLD SALINE

> Blood Replacement Fluids: N/A

> Possible Item Retention: YES Sponge Final Count Correct: YES Sharps Final Count Correct: YES

> Instrument Final Count Correct: NOT APPLICABLE Wound Sweep: \* NOT ENTERED \* Wound Sweep Comment: NO COMMENTS ENTERED

> Intra-Operative X-Ray: \* NOT ENTERED \*

> Intra-Operative X-Ray Comment: NO COMMENTS ENTERED Counter: SURNURSE,FOUR

> Counts Verified By: SURNURSE,FIVE

> Dressing: DSD, PAPER TAPE, MEPORE

> Packing: NONE

> Blood Loss: 800 ml Urine Output: 750 ml Postoperative Mood: RELAXED

> Postoperative Consciousness: ANESTHETIZED Postoperative Skin Integrity: SUTURED INCISION Postoperative Skin Color: N/A

> Laser Performed: (Multiple) Sequential Compression Device: NO Cell Saver(s): N/A

> Devices: N/A

> Signed by: /es/ FIVE SURNURSE

> 03/04/2004 10:41

## Non-OR Procedure Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR NON-OR INFO\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Non-OR Procedure Information* option displays information on the selected non-OR procedure, with the exception of the provider's dictated summary.

> This report prints in an 80-column format and can be viewed on the screen.

> Example: Non-OR Procedure Information

> *printout follows*

> SURPATIENT,FIFTEEN (000-98-1234) Age: 60 PAGE 1 NON-O.R. PROCEDURE - CASE \#267260 Printed: AUG 04, 2004@14:40

> Med. Specialty: GENERAL Location: NON OR Principal Diagnosis: LARYNGEAL/TRACHEAL BURN

> Provider: SURSURGEON,FIFTEEN Patient Status: NOT ENTERED Attending:

> Attending Code:

> Attend Anesth: N/A

> Anesthesia Supervisor Code: N/A Anesthetist: N/A

> Anesthesia Technique(s): N/A

> Proc Begin: JAN 14, 2004 08:00 Proc End: JAN 14, 2004 09:00

> Procedure(s) Performed: Principal: BRONCHOSCOPY

> Dictated Summary Expected: YES

> Enter RETURN to continue or '^' to exit:

## Cumulative Report of CPT Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROACCT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Cumulative Report of CPT Codes* option counts and reports the number of times a procedure was performed (based on CPT codes) during a specified date range. There is also a column showing how many times it was in the Other Operative Procedure category.

> After the user enters the date range, the software will ask if the user wants the Cumulative Report of CPT Codes to include only operating room surgical procedures, non-O.R. procedures, or both.

> These reports have a 132-column format and are designed to be copied to a printer.

> Example 1: Print the Cumulative Report of CPT Codes for only OR Surgical Procedures

> Select CPT/IC<span id="_bookmark114" class="anchor"></span>D Coding Menu Option: C Cumulative Report of CPT Codes

> *printout follows*

> O.R. SURGICAL PROCEDURES

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY

> CUMULATIVE REPORT OF CPT CODES DATE REVIEWED: FROM: MAR 28,1999 TO: APR 3,1999

> CPT CODE - SHORT DESCRIPTION TOTAL PROCEDURES TOTAL PRINCIPAL PROCEDURES TOTAL OTHER PROCEDURES

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 29%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>10060</th>
<th><blockquote>
<p>DRAINAGE OF SKIN ABSCESS</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11440</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11441</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11641</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="even">
<td>24075</td>
<td><blockquote>
<p>REMOVE ARM/ELBOW LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>26989</td>
<td><blockquote>
<p>HAND/FINGER SURGERY</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>30520</td>
<td><blockquote>
<p>REPAIR OF NASAL SEPTUM</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>31231</td>
<td><blockquote>
<p>NASAL ENDOSCOPY, DX</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>45315</td>
<td><blockquote>
<p>PROCTOSIGMOIDOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>45330</td>
<td><blockquote>
<p>SIGMOIDOSCOPY, DIAGNOSTIC</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>45333</td>
<td><blockquote>
<p>SIGMOIDOSCOPY &amp; POLYPECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>45378</td>
<td><blockquote>
<p>DIAGNOSTIC COLONOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>45385</td>
<td><blockquote>
<p>COLONOSCOPY, LESION REMOVAL</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>47600</td>
<td><blockquote>
<p>REMOVAL OF GALLBLADDER</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>49000</td>
<td><blockquote>
<p>EXPLORATION OF ABDOMEN</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>49505</td>
<td><blockquote>
<p>REPAIR INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>66984</td>
<td><blockquote>
<p>REMOVE CATARACT, INSERT LENS</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>68801</td>
<td><blockquote>
<p>DILATE TEAR DUCT OPENING</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example 2: Print the Cumulative Report of CPT Codes for only Non-OR Procedures

> Select CPT/ICD Coding Menu Option: C Cumulative Report of CPT Codes

#### printout follows 

> NON-O.R. PROCEDURES

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY

> CUMULATIVE REPORT OF CPT CODES DATE REVIEWED: FROM: JUL 1,1999 TO: DEC 31,1999

> CPT CODE - SHORT DESCRIPTION TOTAL PROCEDURES TOTAL PRINCIPAL PROCEDURES TOTAL OTHER PROCEDURES

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 29%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>10060</th>
<th><blockquote>
<p>DRAINAGE OF SKIN ABSCESS</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10061</td>
<td><blockquote>
<p>DRAINAGE OF SKIN ABSCESS</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11040</td>
<td><blockquote>
<p>DEBRIDE SKIN PARTIAL</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11042</td>
<td><blockquote>
<p>DEBRIDE SKIN/TISSUE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11100</td>
<td><blockquote>
<p>BIOPSY OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11402</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11420</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11620</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11640</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11730</td>
<td><blockquote>
<p>REMOVAL OF NAIL PLATE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11750</td>
<td><blockquote>
<p>REMOVAL OF NAIL BED</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12001</td>
<td><blockquote>
<p>REPAIR SUPERFICIAL WOUND(S)</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12011</td>
<td><blockquote>
<p>REPAIR SUPERFICIAL WOUND(S)</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>14060</td>
<td><blockquote>
<p>SKIN TISSUE REARRANGEMENT</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>15782</td>
<td><blockquote>
<p>ABRASION TREATMENT OF SKIN</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17340</td>
<td><blockquote>
<p>CRYOTHERAPY OF SKIN</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>20550</td>
<td><blockquote>
<p>INJ TENDON/LIGAMENT/CYST</p>
</blockquote></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>29799</td>
<td><blockquote>
<p>CASTING/STRAPPING PROCEDURE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>46083</td>
<td><blockquote>
<p>INCISE EXTERNAL HEMORRHOID</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Report of CPT Coding Accuracy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Report of CPT Coding Accuracy lists cases sorted by the CPT code used in the PRINCIPAL PROCEDURES field and OTHER OPERATIVE PROCEDURES field entered by the coder. This option is designed to help check the accuracy of the coding procedures.

> About the prompts

> "Do you want to print the Report of CPT Coding Accuracy for all CPT Codes ?" The user should reply NO to this prompt to produce the report for only one CPT code. The user will then be prompted to enter the CPT code or category.

> "Do you want to sort the Report of CPT Coding Accuracy by Surgical Specialty ?" The user should press the \<Enter\> key if he or she wants to sort the report by specialty. Enter NO to sort the report by date only.

> "Do you want to print the Report to Check Coding Accuracy for all Surgical Specialties ?" The user can enter the code or name of the surgical service he or she wants the report to be based on. Or, the user can press the \<Enter\> key to print the report for all surgical specialties.

> Example 1: Print the Report of CPT Coding Accuracy for OR Surgical Procedures, sorted by Surgical Specialty

> Select CPT/ICD Coding Menu Option: A Report of CPT Coding Accuracy

> *printout follows*

> O.R. SURGICAL PROCEDURES

> MAYBERRY, NC PAGE

> SURGICAL SERVICE 1

> REPORT OF CPT CODING ACCURACY REVIEWED BY: FOR GENERAL(OR WHEN NOT DEFINED BELOW) DATE REVIEWED:

> FROM: OCT 8,2004 TO: OCT 8,2004

PROCEDURE DATE PATIENT PROCEDURES SURGEON/PROVIDER

CASE \# ID# ATTEND SURG/PROV

> ====================================================================================================================================

> 47600 REMOVAL OF GALLBLADDER PRINCIPAL PROCEDURES

> DESCRIPTION: CHOLECYSTECTOMY;

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 24%" />
<col style="width: 32%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>10/08/04 07:00</th>
<th><blockquote>
<p>SURPATIENT,EIGHTEEN</p>
</blockquote></th>
<th><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></th>
<th>SURSURGEON,TWO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63072</p>
</blockquote></td>
<td><blockquote>
<p>000-22-3334</p>
</blockquote></td>
<td></td>
<td>SURSURGEON,FOUR</td>
</tr>
</tbody>
</table>

> CPT Codes: 47600-22

> ====================================================================================================================================

> 47605 REMOVAL OF GALLBLADDER OTHER PROCEDURES

> DESCRIPTION: CHOLECYSTECTOMY; WITH CHOLANGIOGRAPHY

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 23%" />
<col style="width: 41%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>10/08/04 10:00</th>
<th><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></th>
<th><blockquote>
<p>INGUINAL HERNIA , OTHER OPERATIONS:</p>
</blockquote></th>
<th>SURSURGEON,FOUR</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63077</p>
</blockquote></td>
<td><blockquote>
<p>000-41-8719</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td>SURSURGEON,FOUR</td>
</tr>
</tbody>
</table>

> CPT Codes: 49521, 47605-22

> ====================================================================================================================================

> 49505 REPAIR INGUINAL HERNIA PRINCIPAL PROCEDURES

> DESCRIPTION: REPAIR INITIAL INGUINAL HERNIA, AGE 5 YEARS OR OVER; REDUCIBLE

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 23%" />
<col style="width: 34%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>10/08/04 06:00</th>
<th><blockquote>
<p>SURPATIENT,FOUR</p>
</blockquote></th>
<th><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63071</p>
</blockquote></td>
<td><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,SIXTEEN</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CPT Codes: 49505

> ====================================================================================================================================

> Example 2: Print the Report of CPT Coding Accuracy for OR Surgical Procedures, sorted by Date

> Select CPT/ICD Coding Menu Option: A Report of CPT Coding Accuracy

#### printout follows 

> O.R. SURGICAL PROCEDURES

> MAYBERRY, NC PAGE

> SURGICAL SERVICE 1

> REPORT OF CPT CODING ACCURACY REVIEWED BY:

> FROM: OCT 1,2004 TO: OCT 7,2004 DATE REVIEWED:

PROCEDURE DATE PATIENT PROCEDURES SURGEON/PROVIDER

CASE \# ID# ATTEND SURG/PROV

> SPECIALTY

> ====================================================================================================================================

> 31365 REMOVAL OF LARYNX PRINCIPAL PROCEDURES

> DESCRIPTION: LARYNGECTOMY; TOTAL, WITH RADICAL NECK DISSECTION

> 10/03/04 07:00 SURPATIENT,NINETEEN PULMONARY LOBECTOMY SURSURGEON,SEVENTEEN

> 63059 000-28-7354 SURSURGEON,FOUR

> THORACIC SURGERY (INC. CARDIAC SURG.)

> CPT Codes: 31365

> ====================================================================================================================================

> 32440 REMOVAL OF LUNG PRINCIPAL PROCEDURES

> DESCRIPTION: REMOVAL OF LUNG, TOTAL PNEUMONECTOMY;

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 31%" />
<col style="width: 27%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>10/03/04 10:00</th>
<th><blockquote>
<p>SURPATIENT,TWENTY</p>
</blockquote></th>
<th><blockquote>
<p>PULMONARY LOBECTOMY</p>
</blockquote></th>
<th>SURSURGEON,FOUR</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63060</p>
</blockquote></td>
<td><blockquote>
<p>000-45-4886</p>
</blockquote></td>
<td></td>
<td>SURSURGEON,FOUR</td>
</tr>
<tr class="even">
<td>10/04/04 06:00</td>
<td><blockquote>
<p>THORACIC SURGERY (INC. CARDIAC SURG.)</p>
<p>SURPATIENT,TEN</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 32440</p>
<p>PULMONARY LOBECTOMY</p>
</blockquote></td>
<td>SURSURGEON,TWO</td>
</tr>
</tbody>
</table>

> 63069 000-12-3456 SURSURGEON,TWO

> THORACIC SURGERY (INC. CARDIAC SURG.)

> CPT Codes: 32440

> ====================================================================================================================================

> Example 3: Print the Report of CPT Coding Accuracy for Non-OR Procedures, sorted by CPT Code and Medical Specialty

> Select CPT/ICD Coding Menu Option: A Report of CPT Coding Accuracy

#### printout follows 

> NON-O.R. PROCEDURES

> MAYBERRY, NC PAGE

> SURGICAL SERVICE 1

> REPORT OF CPT CODING ACCURACY REVIEWED BY: FOR MEDICINE DATE REVIEWED:

> FROM: JAN 1,2005 TO: AUG 31,2005

PROCEDURE DATE PATIENT PROCEDURES SURGEON/PROVIDER

CASE \# ID# ATTEND SURG/PROV

> ====================================================================================================================================

> 92960 HEART ELECTROCONVERSION PRINCIPAL PROCEDURES

> DESCRIPTION: CARDIOVERSION, ELECTIVE, ELECTRICAL CONVERSION OF ARRHYTHMIA, EXTERNAL

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 27%" />
<col style="width: 32%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>01/24/05</th>
<th><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></th>
<th><blockquote>
<p>CARDIOVERSION</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15499</td>
<td><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 92690</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>02/09/05</td>
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15701</td>
<td><blockquote>
<p>000-34-5555</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 92960</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>03/29/05</td>
<td><blockquote>
<p>SURPATIENT,FIFTEEN</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15912</td>
<td><blockquote>
<p>000-98-1234</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 92960</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>08/04/05</td>
<td><blockquote>
<p>SURPATIENT,SIX</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>16669</td>
<td><blockquote>
<p>000-09-8797</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 92960</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/25/05</td>
<td><blockquote>
<p>SURPATIENT,TWO</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>16828</td>
<td><blockquote>
<p>000-45-1982</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 92960</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
</tbody>
</table>

## List Completed Cases Missing CPT Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRSCPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *List Completed Cases Missing CPT Codes* option generates a report of completed cases that are missing the Principal CPT code for a specified date range. Only procedures that have CPT codes will be counted on the Annual Report of Surgical Procedures.

> After the user enters the date range, the software will ask whether the user wants the Cumulative Report of CPT Codes to include: 1) only operating room surgical procedures, 2) non-O.R. procedures, or 3) both.

> This report is in an 80-column format and can be viewed on the screen.

> Example: List Completed Cases Missing CPT Codes

> Select CPT/ICD Coding Menu Option: M List Completed Cases Missing CPT Codes

> *printout follows*

> MAYBERRY, NC

> Completed Cases Missing CPT Codes

> O.R. Surgical Procedures From: FEB 1,2005 To: APR 30,2005

> Specialty: GENERAL(OR WHEN NOT DEFINED BELOW)

> Operation Date Patient (ID#) Surgeon/Provider Case \#

> ================================================================================

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 50%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>FEB 01, 2005</th>
<th><blockquote>
<p>SURPATIENT,TWO (000-45-1982)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>53708</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXC LEFT PREAURICULAR LESION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>FEB 08, 2005</td>
<td><blockquote>
<p>SURPATIENT,FIVE (000-58-7963)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>53747</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXCISION LESIONS SCALP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* N/A (CPT: MISSING)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>MAR 12, 2005</td>
<td><blockquote>
<p>SURPATIENT,SEVEN (000-84-0987)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>53973</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* COLONOSCOPY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>MAR 23, 2005</td>
<td><blockquote>
<p>SURPATIENT,FORTYONE (000-43-2109)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>54030</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* COLONOSCOPY/ATTEMPTED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>APR 27, 2005</td>
<td><blockquote>
<p>SURPATIENT,THIRTY (000-82-9472)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,SEVENTEEN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>54325</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXCISION RT FOREARM LESIONS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXC LESION, RT EAR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXC LESION, RT FOREHEAD</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXC LESION RT SCALP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* RXC LESION, NOSE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXC LESION, LEFT EAR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXC LESION, LEFT FOREARM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXC LESION, TOP OF HEAD</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXC LESION, LEFT NECK</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

## List of Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROPLIST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List of Operations report contains general information for completed cases within a specified date range. It sorts the cases by date and includes the procedure(s), surgical service, length of actual operation, surgeons, and anesthesia technique. This report also includes aborted cases.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: List of Operations

> *printout follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE REVIEWED BY:

> LIST OF OPERATIONS DATE REVIEWED:

> FROM: OCT 8,1999 TO: OCT 8,1999 DATE PRINTED: OCT 20,1999

=

## List of Operations (by Surgical Specialty)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROPLIST1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List of Operations (by Surgical Specialty) report contains general information for completed cases within a selected date range. It sorts the cases by surgical specialty and case number.

> This report includes information on case type, length of actual operation, surgeon names, and anesthesia technique. The user can request a list for all specialties or a selected specialty.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: List of Operations by Surgical Specialty

> Select CPT/ICD Coding Menu Option: LS List of Operations (by Surgical Specialty)

> *printout follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE DATE REVIEWED: LIST OF OPERATIONS BY SERVICE REVIEWED BY:

> FROM: OCT 4,1999 TO: OCT 8,1999 DATE PRINTED: SEP 20,1999

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 31%" />
<col style="width: 32%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>OPERATION(S)</p>
</blockquote></th>
<th>PRIMARY SURGEON</th>
<th>ANESTHESIA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>ID#</p>
</blockquote></td>
<td></td>
<td>FIRST ASSISTANT</td>
<td>TECHNIQUE</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PRIORITY</p>
</blockquote></td>
<td></td>
<td>SECOND ASSISTANT</td>
<td></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> \*GENERAL(OR WHEN NOT DEFINED BELOW)\*

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 18%" />
<col style="width: 34%" />
<col style="width: 23%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>10/04/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,THREE</p>
</blockquote></th>
<th><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63066</p>
</blockquote></td>
<td><blockquote>
<p>000-21-2453</p>
<p>STANDBY</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,TWO SURSURGEON,ONE</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 40 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/04/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,EIGHT</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63067</p>
</blockquote></td>
<td><blockquote>
<p>000-37-0555</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 50 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/04/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,ONE</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63068</p>
</blockquote></td>
<td><blockquote>
<p>000-44-7629</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 45 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/07/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63070</p>
</blockquote></td>
<td><blockquote>
<p>000-56-7821</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 45 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/08/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63071</p>
</blockquote></td>
<td><blockquote>
<p>000-17-0555</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 50 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/08/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,EIGHTEEN</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63072</p>
</blockquote></td>
<td><blockquote>
<p>000-22-3334</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 50 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/08/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA, CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63077</p>
</blockquote></td>
<td><blockquote>
<p>000-41-8719</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
<p>SURSURGEON,THREE</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 63 MIN.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TOTAL GENERAL(OR WHEN NOT DEFINED BELOW): 7

## Report of Daily Operating Room Activity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROPACT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of Daily Operating Room Activity* option generates a report listing cases started between 6:00 AM on the date selected and 5:59 AM of the following day for all operating rooms.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: Print the Report of Daily Operating Room Activity

> Select CPT/ICD Coding Menu Option: D Report of Daily Operating Room Activity

> *printout follows*

> MAYBERRY, NC SURGICAL SERVICE

> DAILY REPORT OF OPERATING ROOM ACTIVITY FOR: MAR 09, 1999

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 31%" />
<col style="width: 27%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th>TIME IN OR</th>
<th><blockquote>
<p>POSTOPERATIVE DIAGNOSIS</p>
</blockquote></th>
<th>ANESTHESIOLOGIST</th>
<th><blockquote>
<p>SURGEON</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID #</p>
</blockquote></td>
<td>AGE TIME OUT OR</td>
<td><blockquote>
<p>PROCEDURE(S)</p>
</blockquote></td>
<td>PRIN. ANESTHETIST</td>
<td><blockquote>
<p>FIRST ASST.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td>CASE NUMBER</td>
<td></td>
<td></td>
<td><blockquote>
<p>ATT SURGEON</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OPERATING ROOM: OR1</p>
</blockquote></th>
<th colspan="4"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></td>
<td><blockquote>
<p>03/09 08:00</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHESIOLOGIST,O</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,E</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>000-41-8719 61</p>
<p>1 NORTH 161-1</p>
</blockquote></td>
<td><blockquote>
<p>03/09 09:10</p>
<p>194</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,F</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,O SURSURGEON,T</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OPERATING ROOM: OR3</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td><blockquote>
<p>03/09 09:15</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTITIS</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHESIOLOGIST,T</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,T</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>000-34-5555 48</p>
<p>OUTPATIENT</p>
</blockquote></td>
<td><blockquote>
<p>03/09 12:40</p>
<p>187</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY, INTRAOPERATIVE CHOLANGIOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,O</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,F SURSURGEON,T</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OPERATING ROOM: OR5</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,SIX</p>
</blockquote></td>
<td><blockquote>
<p>03/09 19:56</p>
</blockquote></td>
<td><blockquote>
<p>APPENDICITIS</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHESIOLOGIST,T</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,S</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>000-09-8797 50</p>
<p>1 WEST 101-1</p>
</blockquote></td>
<td><blockquote>
<p>03/09 21:05</p>
<p>188</p>
</blockquote></td>
<td><blockquote>
<p>APPENDECTOMY, COLONOSCOPY, CHOLECYSTECTOMY, CRAIN</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,F</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,F</p>
<p>SURSURGEON,F</p>
</blockquote></td>
</tr>
</tbody>
</table>

## PCE Filing Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO PCE STATUS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *PCE Filing Status Report* option provides a report of the Patient Care Encounter (PCE) filing status of completed cases performed during the selected date range in accordance with the site parameter controlling PCE updates. If this site parameter is turned off, the report will show no cases. The report may be printed for O.R. surgical cases, non-O.R. procedures or both. The report may also be printed for all specialties or for a single specialty only.

> This report is intended to be used as a tool in the review of Surgery case information that is passed to PCE. The report uses 2 status categories:

1)  FILED - This status indicates that case information has already been filed with PCE.
2)  NOT FILED - This status indicates that the case information has not been filed with PCE. The case may or may not be missing information needed to file with PCE.

> Two forms of the report are available: the short and the long forms. The short form uses an 80-column format and does not include surgeon/provider, attending, principal post-op diagnosis, and CPT and ICD code information. The totals printed at the end will show only the total cases for each status.

> The long form uses a 132-column format and prints case information including the surgeon/provider, the attending, the specialty, the principal post-op diagnosis, and the principal procedure. If the PCE filing status is FILED, the CPT codes and ICD diagnosis codes will be printed. If the filing status is NOT FILED, information fields needed for PCE filing that do not contain data will be printed. At the end of the report, the number of cases in each PCE filing status will be printed, plus the number of CPT and ICD codes for cases with a status of FILED.

> The PCE Filing Status report will display missing clinical indicator data information, per encounter. This indicates to the user what information is missing. The report displays CPT codes that do not have an associated diagnostic code, and textual diagnoses that do not have a corresponding ICD diagnosis code.

> Example 1: PCE Filing Status Report (Short Form)

> Select CPT/ICD Coding Menu Option: PS PCE Filing Status Report

> *printout follows*

> ALBANY

> PCE FILING STATUS REPORT PAGE 1

> For Completed O.R. Surgical Procedures From: JUN 8,2005 To: JUN 10,2005

> Report Printed: JUL 19,2005@10:40

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 28%" />
<col style="width: 26%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE OF OPERATION CASE #</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT NAME SPECIALTY</p>
<p>PRINCIPAL PROCEDURE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT ID (AGE)</p>
</blockquote></th>
<th><blockquote>
<p>FILING STATUS SCHED STATUS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>================================================================================</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JUN 8,2005@07:00</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></td>
<td><blockquote>
<p>045-14-6822 (80)</p>
</blockquote></td>
<td><blockquote>
<p>NOT FILED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>277</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>TURP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Missing Information:

1.  CLASSIFICATION INFORMATION
2.  PRINCIPAL PROCEDURE CODE
3.  PRIN PROCEDURE CODE MISSING ASSOCIATED DIAGNOSIS CODE

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 29%" />
<col style="width: 17%" />
<col style="width: 8%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>JUN 10,2005@07:00 292</th>
<th><blockquote>
<p>SURPATIENT,NINETYONE GENERAL(OR WHEN NOT APPENDECTOMY</p>
</blockquote></th>
<th><blockquote>
<p>604-06-1451P</p>
</blockquote></th>
<th><blockquote>
<p>(53)</p>
</blockquote></th>
<th><blockquote>
<p>FILED</p>
<p>&lt;NONE&gt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>JUN 10,2005@10:00 295</td>
<td><blockquote>
<p>SURPATIENT,FORTYONE GENERAL(OR WHEN NOT REMOVE THYROID CYST</p>
</blockquote></td>
<td><blockquote>
<p>104-04-0550P</p>
</blockquote></td>
<td><blockquote>
<p>(55)</p>
</blockquote></td>
<td><blockquote>
<p>FILED</p>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

| FILED:       | 2   |
|--------------|-----|
| NOT FILED:   | 1   |
| TOTAL CASES: | 3   |

> Example 2: PCE Filing Status Report (Long Form)

> Select CPT/ICD Coding Menu Option: PS PCE Filing Status Report

#### printout follows 

> ALBANY

> PCE FILING STATUS REPORT PAGE 1

> For Completed O.R. Surgical Procedures From: JUN 8,2005 To: JUN 10,2005

> Report Printed: JUL 19,2005@08:19

=

> Missing Information:

1.  CLASSIFICATION INFORMATION
2.  PRINCIPAL PROCEDURE CODE
3.  PRIN PROCEDURE CODE MISSING ASSOCIATED DIAGNOSIS CODE

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 31%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>JUN 9,2005@15:00</th>
<th><blockquote>
<p>SURPATIENT,FIFTEEN</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW)</p>
</blockquote></th>
<th><blockquote>
<p>NOT FILED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>280</td>
<td><blockquote>
<p>000-98-1234 (60)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
<td><blockquote>
<p>HERNIA, INGUINAL</p>
</blockquote></td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>HERNIA REPAIR</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Missing Information:

1.  PRIN PROCEDURE CODE MISSING ASSOCIATED DIAGNOSIS CODE
2.  OTHER PROCEDURE CPT MISSING ASSOCIATED DIAGNOSIS ICD CODE

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 31%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>JUN 10,2005@07:00</th>
<th><blockquote>
<p>SURPATIENT,NINETYONE</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW)</p>
</blockquote></th>
<th><blockquote>
<p>FILED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>292</td>
<td><blockquote>
<p>000-06-1451 (53)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
<td><blockquote>
<p>NOT ENTERED</p>
</blockquote></td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>APPENDECTOMY</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> CPT Code: 44950 APPENDECTOMY ICD Diagnosis Code: 540.1 ABSCESS OF APPENDIX ICD Diagnosis Code: 560.31 GALLSTONE ILEUS

> JUN 10,2005@10:00 SURPATIENT,FORTYONE SURSURGEON,THREE GENERAL(OR WHEN NOT DEFINED BELOW) FILED

> 295 000-04-0550 (55) SURSURGEON,THREE THYROID CYST \<NONE\> REMOVE THYROID CYST

> CPT Code: 60200 REMOVE THYROID LESION ICD Diagnosis Code: 246.2 CYST OF THYROID

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 3%" />
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 3%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"></th>
<th>CPT</th>
<th></th>
<th>ICD</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FILED:</td>
<td><p>CASES</p>
<p>2</p></td>
<td></td>
<td><p>CODES</p>
<p>2</p></td>
<td></td>
<td><p>CODES</p>
<p>2</p></td>
<td></td>
</tr>
<tr class="even">
<td>NOT FILED:</td>
<td>2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>TOTAL:</td>
<td>3</td>
<td></td>
<td>2</td>
<td></td>
<td>2</td>
<td></td>
</tr>
</tbody>
</table>

## Report of Non-O.R. Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRONOR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of Non-O.R. Procedures* option chronologically lists non-O.R. procedures sorted by surgical specialty or surgeon. This report can be sorted by specialty, provider, or location.

> This report prints in a 132-column format and must be copied to a printer.

> Example 1: Report of Non-O.R. Procedures by Specialty

> Select CPT/ICD Coding Menu Option: R Report of Non-O.R. Procedures

> *printout follows*

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY: REPORT OF NON-O.R. PROCEDURES DATE REVIEWED:

> FROM: MAR 1,1999 TO: MAR 31,1999

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 33%" />
<col style="width: 36%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT (ID#)</p>
</blockquote></th>
<th><blockquote>
<p>PROVIDER</p>
</blockquote></th>
<th>START TIME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>LOCATION (IN/OUT-PAT STATUS)</p>
</blockquote></td>
<td><blockquote>
<p>PRINCIPAL ANESTHETIST</p>
</blockquote></td>
<td>FINISH TIME</td>
</tr>
</tbody>
</table>

> ANESTHESIOLOGIST SUPERVISOR PROCEDURE(S)

> ====================================================================================================================================

> \*\*\* SPECIALTY: CARDIOLOGY \*\*\*

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/02/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
<th>03/02/99 13:05</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>501</p>
</blockquote></td>
<td><blockquote>
<p>AMBULATORY SURGERY (OUTPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p><strong>SURANESTHETIST,TWO</strong></p>
</blockquote></td>
<td>03/02/99 14:10</td>
</tr>
</tbody>
</table>

####### SURANESTHETIST,ONE

> CARDIOVERSION

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 32%" />
<col style="width: 34%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/13/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
<th>03/13/99 14:00</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>500</p>
</blockquote></td>
<td><blockquote>
<p>ICU (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p><strong>SURANESTHETIST,FOUR</strong></p>
</blockquote></td>
<td>03/13/99 14:25</td>
</tr>
</tbody>
</table>

####### SURANESTHETIST,ONE

> CARDIOVERSION

> Example 2: Report of Non-O.R. Procedures by Provider

> Select CPT/ICD Coding Menu Option: R Report of Non-O.R. Procedures

#### printout follows 

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY: REPORT OF NON-O.R. PROCEDURES DATE REVIEWED:

> FROM: MAR 1,1999 TO: MAR 31,1999

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 33%" />
<col style="width: 36%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT (ID#)</p>
</blockquote></th>
<th><blockquote>
<p>SPECIALTY</p>
</blockquote></th>
<th>START TIME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>LOCATION (IN/OUT-PAT STATUS)</p>
</blockquote></td>
<td><blockquote>
<p>PRINCIPAL ANESTHETIST</p>
</blockquote></td>
<td>FINISH TIME</td>
</tr>
</tbody>
</table>

> ANESTHESIOLOGIST SUPERVISOR PROCEDURE(S)

> ====================================================================================================================================

\*\*\* PROVIDER SURSURGEON,SIXTEEN \*\*\*

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/12/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TWO (000-45-1982)</p>
</blockquote></th>
<th><blockquote>
<p>PSYCHIATRY</p>
</blockquote></th>
<th>03/12/99 08:00</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>195</p>
</blockquote></td>
<td><blockquote>
<p>PAC(U) - ANESTHESIA (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,TWO</p>
</blockquote></td>
<td>03/12/99 09:00</td>
</tr>
</tbody>
</table>

> SURANESTHETIST,ONE ELECTROCONVULSIVE THERAPY

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/23/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,NINE (000-34-5555)</p>
</blockquote></th>
<th><blockquote>
<p>PSYCHIATRY</p>
</blockquote></th>
<th>03/23/99 08:10</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>240</p>
</blockquote></td>
<td><blockquote>
<p>PAC(U) - ANESTHESIA (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,SIX</p>
</blockquote></td>
<td>03/23/99 08:40</td>
</tr>
</tbody>
</table>

> SURANESTHETIST,ONE ELECTROCONVULSIVE THERAPY

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 32%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/25/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,FOURTEEN (000-45-7212)</p>
</blockquote></th>
<th><blockquote>
<p>PSYCHIATRY</p>
</blockquote></th>
<th>03/12/99 09:30</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>266</p>
</blockquote></td>
<td><blockquote>
<p>PAC(U) - ANESTHESIA (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,TWO</p>
</blockquote></td>
<td>03/12/99 10:15</td>
</tr>
</tbody>
</table>

> SURANESTHETIST,ONE ELECTROCONVULSIVE THERAPY

> Example 3: Report of Non-O.R. Procedures by Location

> Select CPT/ICD Coding Menu Option: R Report of Non-O.R. Procedures

#### printout follows 

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY: REPORT OF NON-O.R. PROCEDURES DATE REVIEWED:

> FROM: MAR 1,1999 TO: MAR 31,1999

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 33%" />
<col style="width: 36%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT (ID#)</p>
</blockquote></th>
<th><blockquote>
<p>PROVIDER</p>
</blockquote></th>
<th>START TIME</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>SPECIALTY (IN/OUT-PAT STATUS)</p>
</blockquote></td>
<td><blockquote>
<p>PRINCIPAL ANESTHETIST</p>
</blockquote></td>
<td>FINISH TIME</td>
</tr>
</tbody>
</table>

> ANESTHESIOLOGIST SUPERVISOR PROCEDURE(S)

> ====================================================================================================================================

> \*\*\* LOCATION: AMBULATORY SURGERY \*\*\*

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 19%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/02/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
<th>03/02/99</th>
<th><blockquote>
<p>13:05</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>201</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOLOGY (OUTPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,FOUR</p>
</blockquote></td>
<td>03/02/99</td>
<td><blockquote>
<p>14:10</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SURANESTHETIST,ONE CARDIOVERSION

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 33%" />
<col style="width: 18%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/06/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TWENTY (000-45-4886)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></th>
<th>03/07/99</th>
<th><blockquote>
<p>16:30</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>198</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(ACUTE MEDICINE) (OUTPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,FIVE</p>
</blockquote></td>
<td>03/07/99</td>
<td><blockquote>
<p>17:08</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>SURANESTHETIST,ONE EXCISION OF SKIN LESION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/09/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTY (000-45-9999)</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,ONE</p>
</blockquote></td>
<td>03/09/99</td>
<td><blockquote>
<p>09:45</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>193</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL (ACUTE MEDICINE) (OUTPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,FIVE</p>
</blockquote></td>
<td>03/09/99</td>
<td><blockquote>
<p>10:21</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SURANESTHETIST,SEVEN STELLATE NERVE BLOCK

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 32%" />
<col style="width: 33%" />
<col style="width: 19%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/13/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
<th>03/13/99</th>
<th><blockquote>
<p>14:00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOLOGY (INPATIENT)</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,TWO</p>
</blockquote></td>
<td>03/13/99</td>
<td><blockquote>
<p>14:25</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SURANESTHETIST,ONE CARDIOVERSION

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 19%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/17/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,EIGHTEEN (000-22-3334)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></th>
<th>03/17/99</th>
<th><blockquote>
<p>13:30</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>194</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL SURGERY (OUTPATIENT)</p>
</blockquote></td>
<td>SURANESTHETIST,SIX</td>
<td>03/17/99</td>
<td><blockquote>
<p>14:42</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>SURANESTHETIST,SEVEN</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> EXCISION OF SKIN LESION

# Chapter Three: Generating Surgical Reports Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgery package integrates clinical and patient data to provide a variety of reports for Surgery Service management. This chapter describes reports that are generated for Surgical Service staff. Among the reports generated are the Annual Report of Surgical Procedures, Anesthesia AMIS, Attending Surgeons Report, and Nurse Staffing Report.

## Exiting an Option or the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user can enter an up-arrow (^) to stop what he or she is doing. The up-arrow can be used at almost any prompt to stop the line of questioning and return to the previous level in the option. The user should continue entering up-arrows to completely exit the system.

## Option Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The main options included in this chapter are listed below. The *Surgery Reports* menu contains submenus. To the left of the option name is the shortcut synonym the user can enter to select the option. A restricted option (such as the *Surgery Reports* menu) will not display if the user does not have security clearance for that option.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SR</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgery Reports</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p><em>Laboratory Interim Report</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Surgery Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRORPTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Chief of Surgery and staff members use the *Surgery Reports* menu to select various reports for the Surgical Service. Among the reports generated are the Annual Report of Surgical Procedures, Anesthesia AMIS, Attending Surgeons Report, and Nurse Staffing Report.

> ![](surgery-version-3-user-manual-updated-sr-3-184/045.png) This menu is locked with the SROREP key.

> All of the menu items below contain sub-options. To the left of the menu name is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p><em>Management Reports</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgery Staffing Reports</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Reports</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPT</p>
</blockquote></td>
<td><blockquote>
<p><em>CPT Code Reports</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark127" class="anchor"></span>Management Reports

### \[SR MANAGE REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Management Reports* menu provides access to several *Management Reports* options. These options generate reports on completed cases, meaning cases that have an entry for the TIME PAT OUT OR field.

> The options included in this menu are listed below. To the left of the option name is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p><em>Schedule of Operations</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Annual Report of Surgical Procedures</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Operations</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LD</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Operations (by Postoperative Disposition)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LS</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Operations (by Surgical Specialty)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LP</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Operations (by Surgical Priority)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Surgical Priorities</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Undictated Operations</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Daily Operating Room Activity</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PS</p>
</blockquote></td>
<td><blockquote>
<p><em>PCE Filing Status Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NOX</p>
</blockquote></td>
<td><blockquote>
<p><em>Outpatient Encounters Not Transmitted to NPCD</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Schedule of Operations

### \[SROSCH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Schedule of Operations* option generates the Operating Room Schedule used by the operating room nurses, surgeons, anesthetists, and other hospital services. The report lists operations and patients scheduled for a particular date. It sorts by operating room and includes the procedure(s), blood products requested, and any preoperative x-rays requested. The schedule also provides anesthesia information and surgeon names.

> This report can be printed on multiple printers simultaneously. Use the options included within the *Surgery Package Management Menu* option to enter the name of all printers on which the schedule will print.

> This report has a 132-column format and is designed to be copied to a printer with wide paper.

> Example: Print Schedule of Operations

> Select Management Reports Option: S Schedule of Operations

> *printout follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE

> SCHEDULE OF OPERATIONS SIGNATURE OF CHIEF: DR. MOE HOWARD

PRINTED: SEP 07, 1999 11:12 FOR: SEP 08, 1999

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 30%" />
<col style="width: 26%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>DISPOSITION</p>
</blockquote></th>
<th><blockquote>
<p>PREOPERATIVE DIAGNOSIS</p>
</blockquote></th>
<th><blockquote>
<p>REQ ANESTHESIA</p>
</blockquote></th>
<th><blockquote>
<p>PRIMARY SURGEON</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID#</p>
</blockquote></td>
<td><blockquote>
<p>AGE START TIME</p>
</blockquote></td>
<td><blockquote>
<p>OPERATION(S)</p>
</blockquote></td>
<td><blockquote>
<p>ANESTHESIOLOGIST</p>
</blockquote></td>
<td><blockquote>
<p>FIRST ASST.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td><blockquote>
<p>END TIME</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>PRIN. ANESTHETIST</p>
</blockquote></td>
<td><blockquote>
<p>ATT SURGEON</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ==================================================================================================================================== OPERATING ROOM: OR1

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 4%" />
<col style="width: 10%" />
<col style="width: 32%" />
<col style="width: 28%" />
<col style="width: 9%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,ONE</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>WARD</p>
</blockquote></th>
<th><blockquote>
<p>CARPAL TUNNEL SYNDROME</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,</p>
</blockquote></th>
<th>O</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-44-7629</p>
</blockquote></td>
<td><blockquote>
<p>46</p>
</blockquote></td>
<td><blockquote>
<p>07:30</p>
</blockquote></td>
<td><blockquote>
<p>REVISE MEDIAN NERVE</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHESIOLOGIST,O</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>F</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TO BE ADMITTED</p>
<p>Case # 143</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>09:30</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURANESTHETIST, T</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>O</td>
</tr>
</tbody>
</table>

> PREOPERATIVE XRAYS: CARPAL TUNNEL, R WRIST

> OPERATING ROOM: OR2

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 35%" />
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,FOURTEEN</p>
</blockquote></th>
<th><blockquote>
<p>WARD</p>
</blockquote></th>
<th><blockquote>
<p>CHOLELITHIASIS</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,</p>
</blockquote></th>
<th>O</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-45-7212 48</p>
</blockquote></td>
<td><blockquote>
<p>06:30</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHESIOLOGIST,F</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>T</td>
</tr>
<tr class="even">
<td><blockquote>
<p>HICU 212-B</p>
</blockquote></td>
<td><blockquote>
<p>08:00</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURANESTHETIST, O</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>O</td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p>Case # 141 REQUESTED BLOOD COMPONENTS: TYPE &amp; CROSSMATCH</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>CPDA-1 RED BLOOD CELLS - 2 UNITS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>PREOPERATIVE XRAYS: ABDOMIN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WARD ACUTE DIAPHRAGMATIC HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>T</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>000-41-8719 60</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08:00 REPAIR DIAPHRAGMATIC HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHESIOLOGIST,T</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>O</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TO BE ADMITTED</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>09:30</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST, O</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>T</td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p>Case # 142 REQUESTED BLOOD COMPONENTS: TYPE &amp; CROSSMATCH</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>CPDA-1 RED BLOOD CELLS - 2 UNITS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>PREOPERATIVE XRAYS: ABDOMEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,THIRTY</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>WARD CAROTID ARTERY STENOSIS</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>O</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>000-82-9472 48</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>11:15 CAROTID ARTERY ENDARTERECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHESIOLOGIST,T</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>F</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TO BE ADMITTED</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>16:00</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST, F</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,</p>
</blockquote></td>
<td>O</td>
</tr>
</tbody>
</table>

> \*\* Concurrent Case \#157 AORTO CORONARY BYPASS GRAFT

> Case \# 150 REQUESTED BLOOD COMPONENTS: TYPE & CROSSMATCH CPDA-1 RED BLOOD CELLS - UNITS NOT ENTERED CPDA-1 WHOLE BLOOD - 2 UNITS

> PREOPERATIVE XRAYS: DOPPLER STUDIES

> SURPATIENT,THIRTY WARD CORONARY ARTERY DISEASE GENERAL SURSURGEON, T 000-82-9472 48 11:15 AORTO CORONARY BYPASS GRAFT SURANESTHESIOLOGIST,O SURSURGEON, F TO BE ADMITTED 16:00 SURANESTHETIST, O SURSURGEON, T

> \*\* Concurrent Case \#150 CAROTID ARTERY ENDARTERECTOMY

> Case \# 157

> TOTAL CASES SCHEDULED: 5

> Annual Report of Surgical Procedures

### \[SROARSP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Annual Report of Surgical Procedures* option is used to generate the Annual Report of Surgical Procedures required by VA Central Office. This report counts the number of times a procedure was performed, based on the CPT code entry, within a surgical specialty.

> The report includes only cases that have not been cancelled and that have an entry for the TIME PAT OUT OR field. Procedures without CPT codes are not included in this report.

> This report can be generated for any date range, not only annually.

> The report has a 132-column format and is designed to be copied to a printer.

> Example: Annual Report of Surgical Procedures

> Select Management Reports Option: A Annual Report of Surgical Procedures

> *printout follows*

> MAYBERRY, NC PAGE: 1

> SURGICAL SERVICE REVIEWED BY: ANNUAL REPORT OF SURGICAL PROCEDURES DATE REVIEWED:

> FROM: SEP 1,2001 TO: SEP 30,2001 DATE PRINTED: OCT 20,2001

> MAJOR MINOR

<table style="width:100%;">
<colgroup>
<col style="width: 32%" />
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CPT CODE - OPERATION</p>
</blockquote></th>
<th><blockquote>
<p>TOTAL</p>
</blockquote></th>
<th>STAFF</th>
<th><blockquote>
<p>RESIDENT</p>
</blockquote></th>
<th><blockquote>
<p>TOTAL</p>
</blockquote></th>
<th><blockquote>
<p>STAFF</p>
</blockquote></th>
<th><blockquote>
<p>RESIDENT</p>
</blockquote></th>
<th><blockquote>
<p>TOTAL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>NEUROSURGERY</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>61304 OPEN SKULL FOR EXPLORATION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>1</td>
<td>0</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>61680 INTRACRANIAL VESSEL SURGERY</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>0</td>
<td>1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTALS FOR NEUROSURGERY:</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>1</td>
<td>0</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>ORTHOPEDICS</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>27130 TOTAL HIP REPLACEMENT</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>1</td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>27236 REPAIR OF THIGH FRACTURE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTALS FOR ORTHOPEDICS:</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>2</td>
<td>3</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>OTORHINOLARYNGOLOGY</td>
<td><blockquote>
<p>(ENT)</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>31365 REMOVAL OF LARYNX</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>0</td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTALS FOR OTORHINOLARYNGOLOGY (ENT):</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>0</td>
<td>2</td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p>THORACIC SURGERY (INC. CARDIAC SURG.)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>32480 PARTIAL REMOVAL OF LUNG</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>1</td>
<td>2</td>
</tr>
<tr class="even">
<td><blockquote>
<p>32500 PARTIAL REMOVAL OF LUNG</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33510 CABG, VEIN, SINGLE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>TOTALS FOR THORACIC SURGERY (INC. CARDIAC SURG.): 4</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>2</td>
<td>4</td>
</tr>
<tr class="odd">
<td colspan="8"><blockquote>
<p>====================================================================================================================================</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL OPERATIONS:</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td>1</td>
<td>0</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> List of Operations

### \[SROPLIST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *List of Operations* option contains general information for completed cases within a specified date range. It sorts the cases by date and includes the procedure(s), surgical service, length of actual operation, surgeons, and anesthesia technique. This report also includes aborted cases.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: List of Operations

> Select Management Reports Option: L List of Operations

> *printout follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE REVIEWED BY:

> LIST OF OPERATIONS DATE REVIEWED:

> FROM: OCT 8,2001 TO: OCT 8,2001 DATE PRINTED: SEP 20,2001

=

### List of Operations (by Postoperative Disposition)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *List of Operations (by Postoperative Disposition)* option contains general information for completed cases within a selected date range. It sorts the cases by postoperative disposition and by case number.

> Reports may also be sorted by specialty.

> This report includes information on case type, length of actual operation, surgeon names, and anesthesia technique.

> This report has a 132-column format and is designed to be copied to a printer.

> Example 1: List of Operations by Postoperative Disposition (All Dispositions)

> Select Management Reports Option: LD List of Operations (by Postoperative Disposition)

> *printout follows*

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 44%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2" rowspan="2"></th>
<th><blockquote>
<p>MAYBERRY, NC</p>
</blockquote></th>
<th>PAGE</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SURGICAL SERVICE</p>
<p>LIST OF OPERATIONS BY POSTOP DISPOSITION FROM: OCT 8,2001 TO: OCT 8,2001</p>
<p>POSTOP DISPOSITION: WARD</p>
</blockquote></th>
<th><p>1</p>
<blockquote>
<p>DATE PRINTED: OCT 20,2001 REVIEWED BY:</p>
<p>DATE REVIEWED:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DATE CASE #</td>
<td><blockquote>
<p>PATIENT ID#</p>
</blockquote></td>
<td><blockquote>
<p>OPERATION(S)</p>
</blockquote></td>
<td><blockquote>
<p>PRIMARY SURGEON ANESTHESIA TECH</p>
<p>1ST ASST IN/OUT-PAT STATUS</p>
<p>2ND ASST OP TIME</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>&gt;&gt; GENERAL(OR WHEN NOT DEFINED BELOW) &lt;&lt;</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> 10/08/01 SURPATIENT,EIGHTEEN CHOLECYSTECTOMY SURSURGEON,TWO GENERAL

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 36%" />
<col style="width: 25%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>63072</p>
</blockquote></th>
<th><blockquote>
<p>000-22-3334</p>
</blockquote></th>
<th></th>
<th>SURSURGEON,FOUR</th>
<th><blockquote>
<p>OUTPATIENT</p>
<p>50 MIN.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>10/08/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA, CHOLECYSTECTOMY</p>
</blockquote></td>
<td>SURSURGEON,FOUR</td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63077</p>
</blockquote></td>
<td><blockquote>
<p>000-41-8719</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
<p>SURSURGEON,THREE</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
<p>63 MIN.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/08/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td>SURSURGEON,FOUR</td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63071</p>
</blockquote></td>
<td><blockquote>
<p>000-17-0555</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
<p>50 MIN.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TOTAL GENERAL(OR WHEN NOT DEFINED BELOW): 3

> Example 2: List of Operations by Postoperative Disposition (A Specific Disposition)

> Select Management Reports Option: LD List of Operations (by Postoperative Disposition)

#### printout follows 

> MAYBERRY, NC PAGE

> SURGICAL SERVICE 1

> LIST OF OPERATIONS BY POSTOP DISPOSITION DATE PRINTED: OCT 20,2001 FROM: OCT 4,2001 TO: OCT 8,2001 REVIEWED BY:

> POSTOP DISPOSITION: OUTPATIENT DATE REVIEWED:

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 28%" />
<col style="width: 29%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>DATE CASE #</th>
<th><blockquote>
<p>PATIENT ID#</p>
</blockquote></th>
<th><blockquote>
<p>OPERATION(S)</p>
</blockquote></th>
<th><blockquote>
<p>PRIMARY SURGEON 1ST ASST</p>
<p>2ND ASST</p>
</blockquote></th>
<th><blockquote>
<p>ANESTHESIA TECH IN/OUT-PAT STATUS OP TIME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>10/04/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,THREE</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63066</p>
</blockquote></td>
<td><blockquote>
<p>000-21-2453 (GENERAL)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,TWO SURSURGEON,ONE</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
<p>40 MIN.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/04/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,EIGHT</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63067</p>
</blockquote></td>
<td><blockquote>
<p>000-37-0555 (GENERAL)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
<p>50 MIN.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/04/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63068</p>
</blockquote></td>
<td><blockquote>
<p>000-17-0555 (GENERAL)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
<p>45 MIN.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/07/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63070</p>
</blockquote></td>
<td><blockquote>
<p>000-56-7821 (GENERAL)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
<p>45 MIN.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/08/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63071</p>
</blockquote></td>
<td><blockquote>
<p>000-17-0555</p>
<p>(GENERAL)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
<p>50 MIN.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TOTAL OUTPATIENT: 5

> Example 3: List of Operations by Postoperative Disposition (No Disposition Entered)

> Select Management Reports Option: LD List of Operations (by Postoperative Disposition)

#### printout follows 

> MAYBERRY, NC PAGE

> SURGICAL SERVICE 1

> LIST OF OPERATIONS BY POSTOP DISPOSITION DATE PRINTED: SEP 20,2001 FROM: OCT 4,2001 TO: OCT 8,2001 REVIEWED BY:

> POSTOP DISPOSITION: DISPOSITION NOT ENTERED DATE REVIEWED:

> DATE PATIENT OPERATION(S) PRIMARY SURGEON ANESTHESIA TECH

> CASE \# ID# 1ST ASST IN/OUT-PAT STATUS

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 29%" />
<col style="width: 27%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"></th>
<th><blockquote>
<p>2ND ASST</p>
</blockquote></th>
<th><blockquote>
<p>OP TIME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>10/04/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TEN</p>
</blockquote></td>
<td><blockquote>
<p>PULMONARY LOBECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63069</p>
</blockquote></td>
<td><blockquote>
<p>000-12-3456</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,FIVE</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>(THORACIC SURGERY )</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
<td><blockquote>
<p>60 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>10/08/01 SURPATIENT,FIFTYONE INTRAOCCULAR LENS, CHOLECYSTECTOMY SURSURGEON,FOUR SPINAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63073</p>
</blockquote></td>
<td><blockquote>
<p>000-23-3221</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>(OPHTHALMOLOGY)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>50 MIN.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10/08/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOURTEEN</p>
</blockquote></td>
<td><blockquote>
<p>TURP</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63076</p>
</blockquote></td>
<td><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>OUTPATIENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>(UROLOGY)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>45 MIN.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TOTAL DISPOSITION NOT ENTERED: 3

### List of Operations (by Surgical Specialty)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *List of Operations (by Surgical Specialty)* option contains general information for completed cases within a selected date range. It sorts the cases by surgical specialty and case number.

> This report includes information on case type, length of actual operation, surgeon names, and anesthesia technique. The user can request a list for all specialties or a selected specialty.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: List of Operations by Surgical Specialty

> Select Management Reports Option: LS List of Operations (by Surgical Specialty)

> *printout follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE DATE REVIEWED: LIST OF OPERATIONS BY SERVICE REVIEWED BY:

> FROM: OCT 4,2001 TO: OCT 8,2001 DATE PRINTED: SEP 20,2001

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 31%" />
<col style="width: 32%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>OPERATION(S)</p>
</blockquote></th>
<th>PRIMARY SURGEON</th>
<th>ANESTHESIA</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>ID#</p>
</blockquote></td>
<td></td>
<td>FIRST ASSISTANT</td>
<td>TECHNIQUE</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>PRIORITY</p>
</blockquote></td>
<td></td>
<td>SECOND ASSISTANT</td>
<td></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> \*GENERAL(OR WHEN NOT DEFINED BELOW)\*

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 18%" />
<col style="width: 34%" />
<col style="width: 23%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>10/04/01</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,THREE</p>
</blockquote></th>
<th><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63066</p>
</blockquote></td>
<td><blockquote>
<p>000-21-2453</p>
<p>STANDBY</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,TWO SURSURGEON,ONE</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 40 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/04/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,EIGHT</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63067</p>
</blockquote></td>
<td><blockquote>
<p>000-37-0555</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 50 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/04/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TEN</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63068</p>
</blockquote></td>
<td><blockquote>
<p>000-12-3456</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 45 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/07/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63070</p>
</blockquote></td>
<td><blockquote>
<p>000-56-7821</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 45 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/08/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63071</p>
</blockquote></td>
<td><blockquote>
<p>000-17-0555</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 50 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/08/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,EIGHTEEN</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63072</p>
</blockquote></td>
<td><blockquote>
<p>000-22-3334</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 50 MIN.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10/08/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIVE</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA, CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63077</p>
</blockquote></td>
<td><blockquote>
<p>000-58-7963</p>
<p>ELECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
<p>SURSURGEON,TWO</p>
</blockquote></td>
<td><blockquote>
<p>OP TIME: 63 MIN.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TOTAL GENERAL(OR WHEN NOT DEFINED BELOW): 7

> <span id="_bookmark128" class="anchor"></span>List of Operations (by Surgical Priority)

> The *List of Operations (by Surgical Priority)* option generates a report containing general information for completed cases within a selected date range. It sorts the cases by surgical priority and surgical specialty.

> This report includes information on case type, length of actual operation, surgeon names, and anesthesia technique. The user can request a list for all priorities or a selected priority. One or more surgical specialties can also be specified.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: List of Operations by Surgical Priority

> Select Management Reports Option: LP List of Operations (by Surgical Priority)

> *printout follows*

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 40%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2" rowspan="2"></th>
<th><blockquote>
<p>ISC-BIRMINGHAM, AL</p>
</blockquote></th>
<th>PAGE:</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>SURGICAL SERVICE</p>
<p>LIST OF OPERATIONS BY SURGICAL PRIORITY FROM: AUG 1,2001 TO: SEP 30,2001</p>
<p>SURGICAL PRIORITY: STANDBY</p>
</blockquote></th>
<th><p>1</p>
<blockquote>
<p>DATE PRINTED: OCT 20,2001 REVIEWED BY:</p>
<p>DATE REVIEWED:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DATE CASE #</td>
<td><blockquote>
<p>PATIENT ID#</p>
</blockquote></td>
<td><blockquote>
<p>OPERATION(S)</p>
</blockquote></td>
<td><blockquote>
<p>PRIMARY SURGEON ANESTHESIA TECH 1ST ASST</p>
<p>2ND ASST</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>&gt;&gt; THORACIC SURGERY (INC. CARDIAC SURG.) &lt;&lt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>08/21/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,THREE</p>
</blockquote></td>
<td><blockquote>
<p>PULMONARY LOBECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>62901</p>
</blockquote></td>
<td><blockquote>
<p>000-21-2453</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,TWO OP TIME: 170 MIN. SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>09/02/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td><blockquote>
<p>PULMONARY LOBECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63002</p>
</blockquote></td>
<td><blockquote>
<p>000-34-5555</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,TWO OP TIME: 95 MIN.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>09/29/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOURTEEN</p>
</blockquote></td>
<td><blockquote>
<p>PULMONARY LOBECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63042</p>
</blockquote></td>
<td><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURSURGEON,FOUR OP TIME: 90 MIN.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TOTAL THORACIC SURGERY (INC. CARDIAC SURG.): 3

### Report of Surgical Priorities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of Surgical Priorities* option provides the total number of completed surgical cases for each surgical priority, such as elective, emergency, and urgent within a date range. The user can sort the report by all surgical specialties, one surgical specialty (Example 1), or by all operations within a date range (Example 2).

> This report has an 80-column format and can be viewed on your terminal display screen.

> Example 1: Print Report of Surgical Priorities for a specialty

> Select Management Reports Option: P Report of Surgical Priorities

> *printout follows*

> MAYBERRY, NC SURGICAL SERVICE

> TOTAL OPERATIONS BY SURGICAL PRIORITY FROM: MAR 1,2001 TO: MAR 26,2001

> GENERAL(OR WHEN NOT DEFINED BELOW)

<table>
<colgroup>
<col style="width: 84%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1. ELECTIVE</p>
</blockquote></th>
<th>1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2. URGENT</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>3. EMERGENCY</p>
</blockquote></td>
<td>2</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4. ADD ON (NON-EMERGENT)</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>5. STANDBY</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL SURGICAL CASES:</p>
</blockquote></td>
<td>5</td>
</tr>
</tbody>
</table>

> Example 2: Print Report of Surgical Priorities for all Operations

> Select Management Reports Option: P Report of Surgical Priorities

#### printout follows 

> MAYBERRY, NC SURGICAL SERVICE

> TOTAL OPERATIONS BY SURGICAL PRIORITY FROM: MAR 1,2001 TO: MAR 26,2001

<table>
<colgroup>
<col style="width: 66%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1. ELECTIVE</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2. URGENT</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3. EMERGENCY</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4. ADD ON (NON-EMERGENT)</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5. STANDBY</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6. PRIORITY NOT ENTERED</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL SURGICAL CASES:</p>
</blockquote></td>
<td><blockquote>
<p>15</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Report of Daily Operating Room Activity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of Daily Operating Room Activity* option generates a report listing cases started between 6:00 AM on the date selected and 5:59 AM of the following day for all operating rooms.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: Print the Report of Daily Operating Room Activity

> Select Management Reports Option: D Report of Daily Operating Room Activity

> *printout follows*

> MAYBERRY, NC SURGICAL SERVICE

> DAILY REPORT OF OPERATING ROOM ACTIVITY FOR: MAR 09, 2001

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 31%" />
<col style="width: 27%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th>TIME IN OR</th>
<th><blockquote>
<p>POSTOPERATIVE DIAGNOSIS</p>
</blockquote></th>
<th>ANESTHESIOLOGIST</th>
<th><blockquote>
<p>SURGEON</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID #</p>
</blockquote></td>
<td>AGE TIME OUT OR</td>
<td><blockquote>
<p>PROCEDURE(S)</p>
</blockquote></td>
<td>PRIN. ANESTHETIST</td>
<td><blockquote>
<p>FIRST ASST.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td>CASE NUMBER</td>
<td></td>
<td></td>
<td><blockquote>
<p>ATT SURGEON</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ==================================================================================================================================== OPERATING ROOM: OR1

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></th>
<th><blockquote>
<p>03/09 08:00</p>
</blockquote></th>
<th><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>SURANESTHESIOLOGIST,O</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,E</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-41-8719 62</p>
<p>1 NORTH 161-1</p>
</blockquote></td>
<td><blockquote>
<p>03/09 09:10</p>
<p>194</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,F</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,O SURSURGEON,T</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OPERATING ROOM: OR3</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td>03/09 09:15</td>
<td><blockquote>
<p>CHOLECYSTITIS</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHESIOLOGIST,T</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,T</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>000-34-5555 48</p>
<p>OUTPATIENT</p>
</blockquote></td>
<td><blockquote>
<p>03/09 12:40</p>
<p>187</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY, INTRAOPERATIVE CHOLANGIOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,O</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,F SURSURGEON,T</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OPERATING ROOM: OR5</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,SIX</p>
</blockquote></td>
<td>03/09 19:56</td>
<td><blockquote>
<p>APPENDICITIS</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHESIOLOGIST,T</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,S</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>000-09-8797 50</p>
<p>1 WEST 101-1</p>
</blockquote></td>
<td><blockquote>
<p>03/09 21:05</p>
<p>188</p>
</blockquote></td>
<td><blockquote>
<p>APPENDECTOMY, COLONOSCOPY, CHOLECYSTECTOMY, CRAIN</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,F</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,F</p>
<p>SURSURGEON,F</p>
</blockquote></td>
</tr>
</tbody>
</table>

### PCE Filing Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *PCE Filing Status Report* option provides a report of the Patient Care Encounter (PCE) filing status of completed cases performed during the selected date range in accordance with the site parameter controlling PCE updates. If this site parameter is turned off, the report will show no cases. The report may be printed for O.R. surgical cases, non-O.R. procedures or both. The report may also be printed for all specialties or for a single specialty only.

> This report is intended to be used as a tool in the review of Surgery case information that is passed to PCE. The report uses 2 status categories:

1)  FILED - This status indicates that case information has already been filed with PCE.
2)  NOT FILED - This status indicates that the case information has not been filed with PCE. The case may or may not be missing information needed to file with PCE.

> Two forms of the report are available: the short and the long forms. The short form uses an 80-column format and does not include surgeon/provider, attending, principal post-op diagnosis, and CPT and ICD code information. The totals printed at the end will show only the total cases for each status.

> The long form uses a 132-column format and prints case information including the surgeon/provider, the attending, the specialty, the principal post-op diagnosis, and the principal procedure. If the PCE filing status is FILED, the CPT codes and ICD diagnosis codes will be printed. If the filing status is NOT FILED, information fields needed for PCE filing that do not contain data will be printed. At the end of the report, the number of cases in each PCE filing status will be printed, plus the number of CPT and ICD codes for cases with a status of FILED.

> The PCE Filing Status report will display missing clinical indicator data information, per encounter. This indicates to the user what information is missing. The report displays CPT codes that do not have an associated diagnostic code, and textual diagnoses that do not have a corresponding ICD diagnosis code.

> Example 1: PCE Filing Status Report (Short Form)

> Select Management Reports Option: PS PCE Filing Status Report

> *printout follows*

> ALBANY

> PCE FILING STATUS REPORT PAGE 1

> For Completed O.R. Surgical Procedures From: JUN 8,2005 To: JUN 10,2005

> Report Printed: JUL 19,2005@10:40

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 28%" />
<col style="width: 26%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE OF OPERATION CASE #</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT NAME SPECIALTY</p>
<p>PRINCIPAL PROCEDURE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT ID (AGE)</p>
</blockquote></th>
<th><blockquote>
<p>FILING STATUS SCHED STATUS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>================================================================================</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JUN 8,2005@07:00</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></td>
<td><blockquote>
<p>000-14-6822 (80)</p>
</blockquote></td>
<td><blockquote>
<p>NOT FILED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>277</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>TURP</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Missing Information:

1.  CLASSIFICATION INFORMATION
2.  PRINCIPAL PROCEDURE CODE
3.  PRIN PROCEDURE CODE MISSING ASSOCIATED DIAGNOSIS CODE

<table style="width:100%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 29%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>JUN 10,2005@07:00 292</th>
<th><blockquote>
<p>SURPATIENT,NINETYONE GENERAL(OR WHEN NOT APPENDECTOMY</p>
</blockquote></th>
<th><blockquote>
<p>000-06-1451</p>
</blockquote></th>
<th><blockquote>
<p>(53)</p>
</blockquote></th>
<th><blockquote>
<p>FILED</p>
<p>&lt;NONE&gt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>JUN 10,2005@10:00 295</td>
<td><blockquote>
<p>SURPATIENT,FORTYONE GENERAL(OR WHEN NOT REMOVE THYROID CYST</p>
</blockquote></td>
<td><blockquote>
<p>000-04-0550</p>
</blockquote></td>
<td><blockquote>
<p>(55)</p>
</blockquote></td>
<td><blockquote>
<p>FILED</p>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

| FILED:       | 2   |
|--------------|-----|
| NOT FILED:   | 1   |
| TOTAL CASES: | 3   |

> Example 2: PCE Filing Status Report (Long Form)

> Select <span id="_bookmark129" class="anchor"></span>CPT/ICD Coding Menu Option: PS PCE Filing Status Report

#### printout follows 

> ALBANY

> PCE FILING STATUS REPORT PAGE 1

> For Completed O.R. Surgical Procedures From: JUN 8,2005 To: JUN 10,2005

> Report Printed: JUL 19,2005@08:19

=

> Missing Information:

1.  CLASSIFICATION INFORMATION
2.  PRINCIPAL PROCEDURE CODE
3.  PRIN PROCEDURE CODE MISSING ASSOCIATED DIAGNOSIS CODE

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 31%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>JUN 9,2005@15:00</th>
<th><blockquote>
<p>SURPATIENT,FIFTEEN</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW)</p>
</blockquote></th>
<th><blockquote>
<p>NOT FILED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>280</td>
<td><blockquote>
<p>000-98-1234 (60)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
<td><blockquote>
<p>HERNIA, INGUINAL</p>
</blockquote></td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>HERNIA REPAIR</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Missing Information:

1.  PRIN PROCEDURE CODE MISSING ASSOCIATED DIAGNOSIS CODE
2.  OTHER PROCEDURE CPT MISSING ASSOCIATED DIAGNOSIS ICD CODE

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 31%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>JUN 10,2005@07:00</th>
<th><blockquote>
<p>SURPATIENT,NINETYONE</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW)</p>
</blockquote></th>
<th><blockquote>
<p>FILED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>292</td>
<td><blockquote>
<p>000-06-1451 (53)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
<td><blockquote>
<p>NOT ENTERED</p>
</blockquote></td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>APPENDECTOMY</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> CPT Code: 44950 APPENDECTOMY ICD Diagnosis Code: 540.1 ABSCESS OF APPENDIX ICD Diagnosis Code: 560.31 GALLSTONE ILEUS

> JUN 10,2005@10:00 SURPATIENT,FORTYONE SURSURGEON,THREE GENERAL(OR WHEN NOT DEFINED BELOW) FILED

> 295 000-04-0550 (55) SURSURGEON,THREE THYROID CYST \<NONE\> REMOVE THYROID CYST

> CPT Code: 60200 REMOVE THYROID LESION ICD Diagnosis Code: 246.2 CYST OF THYROID

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 3%" />
<col style="width: 1%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 3%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"></th>
<th>CPT</th>
<th></th>
<th>ICD</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FILED:</td>
<td><p>CASES</p>
<p>2</p></td>
<td></td>
<td><p>CODES</p>
<p>2</p></td>
<td></td>
<td><p>CODES</p>
<p>2</p></td>
<td></td>
</tr>
<tr class="even">
<td>NOT FILED:</td>
<td>2</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>TOTAL:</td>
<td>3</td>
<td></td>
<td>2</td>
<td></td>
<td>2</td>
<td></td>
</tr>
</tbody>
</table>

### Outpatient Encounters Not Transmitted to NPCD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Outpatient surgical and non-O.R. procedures that are filed as encounters in the PCE package without an active count clinic identified for each encounter are not transmitted to the National Patient Care Database (NPCD) as workload. The *Outpatient Encounters Not Transmitted to NPCD* option may be used as a tool for identifying these encounters that represent uncounted workload so that corrective actions may be taken in the Surgery package to insure these procedures are associated with an active count clinic. After corrections are made, these encounters may be re-filed with PCE to be transmitted to NPCD.

> This option provides functionality:

- To count and/or list surgical cases and non-O.R. procedures that have entries in PCE but have no matching entries in the OUTPATIENT ENCOUNTER file or have matching entries that are non- count encounters or encounters requiring action.
- To re-file with PCE the cases identified as having no matching entries in the OUTPATIENT ENCOUNTER file or having matching entries that are non-count encounters or encounters requiring action.

> Both the report and the re-filing process may be run for O.R. surgical cases, non-O.R. procedures or both. The report and the re-filing process may be run for a specific specialty or for all specialties and may be run for a selected date range.

> Example 1: Print List of Cases

> *printout follows*

> MAYBERRY, NC

> Outpatient Surgery Encounters Not Transmitted to NPCD Page 1 For Completed O.R. Surgical Procedures

> From: MAY 1,2001 To: MAY 15,2001

> Report Printed: MAY 20,2001@06:44

> DATE OF OPERATION CASE \# SPECIALTY SCHED STATUS PATIENT NAME PRINCIPAL PROCEDURE

> PATIENT ID (AGE)

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 15%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>MAY 1,2001@09:00 SURPATIENT,FOURTEEN</th>
<th><blockquote>
<p>63028</p>
<p>CHOLECYSTECTOMY</p>
</blockquote></th>
<th>GENERAL(OR WHEN NOT</th>
<th><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>000-45-7212 (50)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>MAY 3,2001@05:45</td>
<td><blockquote>
<p>63092</p>
</blockquote></td>
<td>GENERAL(OR WHEN NOT</td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SURPATIENT,SIXTY</td>
<td><blockquote>
<p>CHOLEDOCHOTOMY</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>000-56-7821 (42)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MAY 7,2001@07:15</td>
<td><blockquote>
<p>63142</p>
</blockquote></td>
<td>GENERAL(OR WHEN NOT</td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><p>SURPATIENT,TWELVE REPAIR DIAPHRAGMATIC HERNIA</p>
<p>000-41-8719 (73)</p></td>
</tr>
<tr class="odd">
<td>MAY 12,2001@06:00</td>
<td><blockquote>
<p>63191</p>
</blockquote></td>
<td>GENERAL(OR WHEN NOT</td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SURPATIENT,NINE</td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>000-34-5555 (64)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>MAY 14,2001@06:00</td>
<td><blockquote>
<p>63208</p>
</blockquote></td>
<td>GENERAL(OR WHEN NOT</td>
<td><blockquote>
<p>ACTION REQUIRED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SURPATIENT,TWELVE</td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>000-41-8719 (73)</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MAY 15,2001@06:01</td>
<td><blockquote>
<p>63180</p>
</blockquote></td>
<td>GENERAL(OR WHEN NOT</td>
<td><blockquote>
<p>&lt;NONE&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SURPATIENT,SIXTY</td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>000-56-7821 (42)</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> SPECIALTY: GENERAL(OR WHEN NOT DEFINED BELOW)

| Total with NO status:       | 5   |
|-----------------------------|-----|
| Total with NON-COUNT:       | 0   |
| Total with ACTION REQUIRED: | 1   |
| Total cases identified:     | 6   |

> Example 2: Print Total Number of Cases Only

#### printout follows 

> MAYBERRY, NC

> Outpatient Surgery Encounters Not Transmitted to NPCD Page 1 For Completed O.R. Surgical Procedures

> From: MAY 1,2001 To: MAY 15,2001

> Report Printed: MAY 20,2001@07:25

> ================================================================================ SPECIALTY: GENERAL(OR WHEN NOT DEFINED BELOW)

| Total with NO status:       | 5   |
|-----------------------------|-----|
| Total with NON-COUNT:       | 0   |
| Total with ACTION REQUIRED: | 1   |
| Total cases identified:     | 6   |

> Example 3: Re-File Cases in PCE

## Surgery Staffing Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR STAFFING REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Surgery Staffing Reports* menu provides access to several staffing related report options.

> The options included in this submenu are listed below. To the left of the option name is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Attending Surgeon Reports</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgeon Staffing Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgical Nurse Staffing Report</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NS</p>
</blockquote></td>
<td><blockquote>
<p><em>Scrub Nurse Staffing Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NC</p>
</blockquote></td>
<td><blockquote>
<p><em>Circulating Nurse Staffing Report</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Attending Surgeon Reports

### \[SROATT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Attending Surgeon Reports* option generates the Attending Surgeon Report, which provides staffing information for completed cases (Example 1). The Attending Surgeon Cumulative Report is a table with cumulative totals for each attending code (Example 2). You can print these reports separately or you can print both reports at one time.

> The Attending Surgeon Report can be sorted by surgical specialty. They can also be generated for an individual surgeon, or for all attending surgeons.

> The Attending Surgeon Report has a 132-column format and is designed to be copied to a printer. The Attending Surgeon Cumulative Report has an 80-column format and can be viewed on the screen.

> Example 1: Print the Attending Surgeon Report

> Select Surgery Staffing Reports Option: A Attending Surgeon Reports

> *printout follows*

> MAYBERRY, NC PAGE: 1

> ==================================================================================================================================== GENERAL(OR WHEN NOT DEFINED BELOW)

> ==================================

> ATTENDING SURGEON: SURSURGEON,TWO

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 7%" />
<col style="width: 42%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>06/17/04</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>SURPATIENT,FOURTEEN</p>
</blockquote></th>
<th><blockquote>
<p>CHOLELITHIASIS</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>203</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>LEVEL B: ATTENDING IN O.R., SCRUBBED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/18/04</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></td>
<td><blockquote>
<p>INCARCERATED INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>202</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td><blockquote>
<p>REPAIR INCARCERATED INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>LEVEL B: ATTENDING IN O.R., SCRUBBED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/09/04</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></td>
<td><blockquote>
<p>INCARCERATED INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>494</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>000-41-8719</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td colspan="2"><blockquote>
<p>ATTENDING CODE NOT ENTERED</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p>ATTENDING SURGEON: SURSURGEON,ONE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>06/10/04</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURPATIENT,FIFTYONE</p>
</blockquote></td>
<td><blockquote>
<p>RUPTURED TUBOOVARIAN ABSCESS</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>189</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>000-23-3221</p>
</blockquote></td>
<td><blockquote>
<p>DRAINAGE OF OVARIAN CYST</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>LEVEL E: EMERGENCY CARE, ATTENDING CONTACTED ASAP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/09/04</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CHOLECYSTITIS</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>187</p>
</blockquote></td>
<td><blockquote>
<p>000-34-5555</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CHOLECYSTECTOMY, INTRAOPERATIVE CHOLANGIOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>LEVEL C: ATTENDING IN O.R.,</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NOT SCRUBBED</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p>ATTENDING SURGEON: SURSURGEON,FOUR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>06/09/04</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIX</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>APPENDICITIS</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,SIX</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>188</p>
</blockquote></td>
<td><blockquote>
<p>000-09-8797</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>APPENDECTOMY, COLONOSCOPY, CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
</tbody>
</table>

> LEVEL D: ATTENDING IN O.R. SUITE, IMMEDIATELY AVAILABLE

> Example 2: Print the Attending Surgeon Cumulative Report

> Select Surgery Staffing Reports Option: A Attending Surgeon Reports

#### printout follows 

> MAYBERRY, NC SURGICAL SERVICE

> ATTENDING SURGEON CUMULATIVE REPORT FROM: JUN 9,2004 TO: JUN 18,2004

> ==============================================================================

> GENERAL(OR WHEN NOT DEFINED BELOW)

ATTENDING CODE TOTAL CASES

> LEVEL B: ATTENDING IN O.R., SCRUBBED 2

> LEVEL C: ATTENDING IN O.R., NOT SCRUBBED 1

> LEVEL D: ATTENDING IN O.R. SUITE, IMMEDIATELY AVAILABLE 1

> LEVEL E: EMERGENCY CARE, ATTENDING CONTACTED ASAP 1

> \* ATTENDING CODE NOT ENTERED 1

> TOTAL CASES FROM 06/09/04 TO 06/18/04 6

> Surgeon Staffing Report

### \[SROSUR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Surgeon Staffing Report* option lists completed cases sorted by the surgeon and his or her role (i.e., attending, first assistant) for each case. The report provides the procedure, diagnosis and operation date/time.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: Print Surgeon Staffing Report

> Select Surgery Staffing Reports Option: S Surgeon Staffing Report

> *printout follows*

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 38%" />
<col style="width: 24%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">MAYBERRY, NC</th>
<th></th>
<th><blockquote>
<p>PAGE: 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3">SURGICAL SERVICE</td>
<td><blockquote>
<p>REVIEWED BY:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>SURGEON STAFFING REPORT</p>
</blockquote></td>
<td><blockquote>
<p>DATE REVIEWED:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>FROM: MAR 2,2001 TO: MAR 31,2001 DATE PRINTED: APR 20,2001</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DATE/TIME</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>OPERATION(S)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIAGNOSIS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>ID #</p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> \*\* SURSURGEON,ONE \*\* ROLE: ATTENDING SURGEON

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 37%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MAR 187</p>
</blockquote></th>
<th>09, 2001@09:15</th>
<th><blockquote>
<p>SURPATIENT,NINE 000-34-5555</p>
</blockquote></th>
<th><blockquote>
<p>CHOLECYSTECTOMY, INTRAOPERATIVE CHOLANGIOGRAM</p>
</blockquote></th>
<th><blockquote>
<p>CHOLECYSTITIS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MAR 189</p>
</blockquote></td>
<td>10, 2001@07:00</td>
<td><blockquote>
<p>SURPATIENT,FIFTYONE 000-23-3221</p>
</blockquote></td>
<td><blockquote>
<p>DRAINAGE OF OVARIAN CYST</p>
</blockquote></td>
<td><blockquote>
<p>APPENDICITIS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAR 200</p>
</blockquote></td>
<td>10, 2001@14:00</td>
<td><blockquote>
<p>SURPATIENT,FIFTY 000-45-9999</p>
</blockquote></td>
<td><blockquote>
<p>HEMORRHOIDECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>EXTERNAL HEMORRHOIDS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>ROLE: SURGEON</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAR 199</p>
</blockquote></td>
<td>10, 2001@08:00</td>
<td><blockquote>
<p>SURPATIENT,TWO 000-45-1982</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY WITH CHOLANGIOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>CHOLELITHIASIS WITH BILIARY COLIC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAR 203</p>
</blockquote></td>
<td>17, 2001@12:55</td>
<td><blockquote>
<p>SURPATIENT,FOURTEEN 000-45-7212</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>CHOLELITHIASIS</p>
</blockquote></td>
</tr>
</tbody>
</table>

> MAR 18, 2001@07:30 SURPATIENT,SEVENTEEN REPAIR INCARCERATED INGUINAL HERNIA INCARCERATED INGUINAL HERNIA 202 000-45-5119

> Surgical Nurse Staffing Report

### \[SRONSR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates the Surgical Nurse Staffing Report that lists completed cases within a specified date range. It provides the names of the scrub nurse, the circulating nurse, and the operation times.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: Print Surgical Nurse Staffing Report

> Select Surgery Staffing Reports Option: N Surgical Nurse Staffing Report

> *printout follows*

> MAYBERRY, NC PAGE: 1

> SURGICAL SERVICE REVIEWED BY: SURGICAL NURSE STAFFING REPORT DATE REVIEWED:

> FROM: MAR 9,2001 TO: MAR 10,2001 DATE PRINTED: MAR 20,2001

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 31%" />
<col style="width: 26%" />
<col style="width: 13%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>OPERATION(S)</p>
</blockquote></th>
<th><blockquote>
<p>SCRUB NURSE</p>
</blockquote></th>
<th><blockquote>
<p>CIRC. NURSE</p>
</blockquote></th>
<th><blockquote>
<p>TIME IN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>ID#</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TIME OUT</p>
</blockquote></td>
</tr>
</tbody>
</table>

ELAPSED (MINS)

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 17%" />
<col style="width: 39%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/09/01</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></th>
<th><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>SURNURSE,TWO</p>
</blockquote></th>
<th><blockquote>
<p>SURNURSE,FIVE</p>
</blockquote></th>
<th>08:00</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>194</p>
</blockquote></td>
<td><blockquote>
<p>000-41-8719</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>09:10</p>
<p>70</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/09/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY, INTRAOPERATIVE CHOLANGIOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>09:15</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>187</p>
</blockquote></td>
<td><blockquote>
<p>000-34-5555</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>12:40</p>
<p>205</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/09/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIX</p>
</blockquote></td>
<td><blockquote>
<p>APPENDECTOMY, COLONOSCOPY, CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,SIX</p>
</blockquote></td>
<td>19:56</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>188</p>
</blockquote></td>
<td><blockquote>
<p>000-09-8797</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>21:05</p>
<p>69</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/10/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTYONE</p>
</blockquote></td>
<td><blockquote>
<p>DRAINAGE OF OVARIAN CYST</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,SEVEN</p>
</blockquote></td>
<td>07:00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>189</p>
</blockquote></td>
<td><blockquote>
<p>000-23-3221</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>08:54</p>
<p>114</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/10/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWO</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY WITH CHOLANGIOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,TWO</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,FIVE</p>
</blockquote></td>
<td>08:00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>199</p>
</blockquote></td>
<td><blockquote>
<p>000-45-1982</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>10:08</p>
<p>128</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/10/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTY</p>
</blockquote></td>
<td><blockquote>
<p>HEMORRHOIDECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>14:00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>000-45-9999</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>14:55</p>
<p>55</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Scrub Nurse Staffing Report

### \[SROSNR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Scrub Nurse Staffing Report* option lists each operating room scrub nurse and the completed cases they are assigned to within a specified date range. It also provides the circulating nurses, other scrub nurses, and operation times.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: Print Scrub Nurse Staffing Report

> Select Surgery Staffing Reports Option: NS Scrub Nurse Staffing Report

> *printout follows*

> MAYBERRY, NC PAGE: 1

> SURGICAL SERVICE REVIEWED BY: SCRUB NURSE STAFFING REPORT DATE REVIEWED:

> FROM: MAR 8,2001 TO: MAR 20,2001 DATE PRINTED: MAR 22,2001

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>OPERATION(S)</p>
</blockquote></th>
<th><blockquote>
<p>SCRUB NURSE</p>
</blockquote></th>
<th><blockquote>
<p>CIRC. NURSE</p>
</blockquote></th>
<th><blockquote>
<p>TIME IN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>ID#</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TIME OUT</p>
</blockquote></td>
</tr>
</tbody>
</table>

ELAPSED (MINS)

> ====================================================================================================================================

> \*\* SURNURSE,SEVEN \*\*

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 20%" />
<col style="width: 39%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/18/01</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></th>
<th><blockquote>
<p>REPAIR INCARCERATED INGUINAL HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></th>
<th><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></th>
<th>07:30</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>202</p>
</blockquote></td>
<td><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURNURSE,SEVEN</p>
</blockquote></td>
<td></td>
<td><p>09:03</p>
<p>93</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p> SURNURSE,THREE </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/09/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY, INTRAOPERATIVE CHOLANGIOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>09:15</td>
</tr>
<tr class="even">
<td><blockquote>
<p>187</p>
</blockquote></td>
<td><blockquote>
<p>000-34-5555</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><p>12:40</p>
<p>205</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/09/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIX</p>
</blockquote></td>
<td><blockquote>
<p>APPENDECTOMY, COLONOSCOPY, CHOLECYSTECTOMY,</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td></td>
<td>19:56</td>
</tr>
<tr class="even">
<td><blockquote>
<p>188</p>
</blockquote></td>
<td><blockquote>
<p>000-09-8797</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><p>21:05</p>
<p>69</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/10/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTYONE</p>
</blockquote></td>
<td><blockquote>
<p>DRAINAGE OF OVARIAN CYST</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,SEVEN</p>
</blockquote></td>
<td>07:00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>189</p>
</blockquote></td>
<td><blockquote>
<p>000-23-3221</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><p>08:54</p>
<p>114</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/10/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTY</p>
</blockquote></td>
<td><blockquote>
<p>HEMORRHOIDECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>14:00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>000-45-9999</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><p>14:55</p>
<p>55</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/17/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOURTEEN</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>12:55</td>
</tr>
<tr class="even">
<td><blockquote>
<p>203</p>
</blockquote></td>
<td><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><p>14:30</p>
<p>95</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/18/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></td>
<td><blockquote>
<p>REPAIR INCARCERATED INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>07:30</td>
</tr>
<tr class="even">
<td><blockquote>
<p>202</p>
</blockquote></td>
<td><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURNURSE,SEVEN</p>
</blockquote></td>
<td></td>
<td><p>09:03</p>
<p>93</p></td>
</tr>
</tbody>
</table>

> Circulating Nurse Staffing Report

### \[SROCNR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Circulating Nurse Staffing Report* option provides nurse staffing information, sorted by the circulating nurse's name. It lists the circulating nurses and the completed cases they are assigned to within a specified date range. The report includes the scrub nurse, other circulating nurses, and operation times.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: Print Circulating Nurse Staffing Report

> Select Surgery Staffing Reports Option: NC Circulating Nurse Staffing Report

> *printout follows*

> MAYBERRY, NC PAGE: 1

> SURGICAL SERVICE REVIEWED BY: CIRCULATING NURSE STAFFING REPORT DATE REVIEWED:

> FROM: MAR 2,2001 TO: MAR 31,2001 DATE PRINTED: APR 21,2001

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 15%" />
<col style="width: 30%" />
<col style="width: 25%" />
<col style="width: 13%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>OPERATION(S)</p>
</blockquote></th>
<th><blockquote>
<p>SCRUB NURSE</p>
</blockquote></th>
<th><blockquote>
<p>CIRC. NURSE</p>
</blockquote></th>
<th>TIME IN</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>ID#</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>TIME OUT</td>
</tr>
</tbody>
</table>

ELAPSED (MINS)

> ====================================================================================================================================

> \*\* SURNURSE,SEVEN \*\*

<table style="width:100%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 17%" />
<col style="width: 39%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/10/01</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,FIFTYONE</p>
</blockquote></th>
<th><blockquote>
<p>DRAINAGE OF OVARIAN CYST</p>
</blockquote></th>
<th><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></th>
<th><blockquote>
<p>SURNURSE,SEVEN</p>
</blockquote></th>
<th>07:00</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>189</p>
</blockquote></td>
<td><blockquote>
<p>000-23-3221</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><p>08:54</p>
<p>114</p></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p> SURNURSE,ONE </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/09/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY, INTRAOPERATIVE CHOLANGIOGRAM</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>09:15</td>
</tr>
<tr class="even">
<td><blockquote>
<p>187</p>
</blockquote></td>
<td><blockquote>
<p>000-34-5555</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><p>12:40</p>
<p>205</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/10/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTY</p>
</blockquote></td>
<td><blockquote>
<p>HEMORRHOIDECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>14:00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>000-45-9999</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><p>14:55</p>
<p>55</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/17/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOURTEEN</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>12:55</td>
</tr>
<tr class="even">
<td><blockquote>
<p>203</p>
</blockquote></td>
<td><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><p>14:30</p>
<p>95</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>03/18/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></td>
<td><blockquote>
<p>REPAIR INCARCERATED INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,ONE</p>
</blockquote></td>
<td>07:30</td>
</tr>
<tr class="even">
<td><blockquote>
<p>202</p>
</blockquote></td>
<td><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SURNURSE,SEVEN</p>
</blockquote></td>
<td></td>
<td><p>09:03</p>
<p>93</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> SURNURSE,TWO </p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/03/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY</p>
</blockquote></td>
<td><blockquote>
<p>REMOVE CATARACTS, RETRO BULBAR BLOCK</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,THREE</p>
</blockquote></td>
<td><blockquote>
<p>SURNURSE,TWO</p>
</blockquote></td>
<td>09:00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>205</p>
</blockquote></td>
<td><blockquote>
<p>000-56-7821</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td>09:20</td>
</tr>
</tbody>
</table>

## Anesthesia Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR ANESTH REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Anesthesia Reports* menu provides options for printing various anesthesia reports.

> The options included in this menu are listed below. To the left of the option name is the shortcut synonym the user can enter to select the option:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Anesthetic Procedures</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Anesthesia Provider Report</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Page 297 has been deleted. The *Anesthesia AMIS* option has been removed.

> Page 298 has been deleted. The *Anesthesia AMIS* option has been removed.

> List of Anesthetic Procedures

### \[SROANP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *List of Anesthetic Procedures* option generates a report listing each completed case within the date range selected. It sorts by date order and provides the anesthesia personnel. This report also provides the anesthesia start, end, and elapsed times for each case.

> After the user enters the date range, the software will ask whether the user wants the List of Anesthetic Procedures to include 1) only operating room surgical procedures, 2) non-O.R. procedures, or 3) both.

> These reports have a 132-column format and are designed to be copied to a printer.

> Example 1: Print the List of Anesthetic Procedures for only O.R. Surgical Procedures

> Select Anesthesia Reports Option: P List of Anesthetic Procedures

> *printout follows*

> MAYBERRY, NC PAGE: 1

> SURGICAL SERVICE REVIEWED BY: LIST OF ANESTHETIC PROCEDURES DATE REVIEWED:

> O.R. SURGICAL PROCEDURES FROM: AUG 8,2001 TO: AUG 25,2001 DATE PRINTED: SEP 21,2001

> DATE PATIENT PRINCIPAL DIAGNOSIS PRIN ANESTHETIST START TIME

> CASE \# ID# PROCEDURE(S) ANESTH TECHNIQUE END TIME ASA CLASS ANESTH AGENT ELAPSED

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 18%" />
<col style="width: 43%" />
<col style="width: 21%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>08/08/01 08:00</p>
<p>63085</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,NINE 000-34-5555</p>
</blockquote></th>
<th><blockquote>
<p>ABDOMINAL WOUND DEHISCENSE CLOSURE ABDOMINAL DEHISCENSE</p>
</blockquote></th>
<th><blockquote>
<p>SURANESTHETIST,ONE GENERAL</p>
</blockquote></th>
<th><blockquote>
<p>08:00</p>
<p>10:30</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><blockquote>
<p>MILD DISTURB. DESFLURANE 240ML BTL 90</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>08/12/01 08:30</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIX</p>
</blockquote></td>
<td><blockquote>
<p>CA OF LARYNX</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>08:35</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63090</p>
</blockquote></td>
<td><blockquote>
<p>000-09-8797</p>
</blockquote></td>
<td><blockquote>
<p>LARYNGECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
<td><blockquote>
<p>10:35</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>SEVERE DISTURB. SUFENTANIL CITRATE 5 120</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>08/16/01 08:00</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOURTEEN</p>
</blockquote></td>
<td><blockquote>
<p>LESION RT EAR LOBE</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,ONE</p>
</blockquote></td>
<td><blockquote>
<p>08:05</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63094</p>
</blockquote></td>
<td><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td><blockquote>
<p>EXC LESION LESIO RT EAR LOBE</p>
</blockquote></td>
<td><blockquote>
<p>LOCAL</p>
</blockquote></td>
<td><blockquote>
<p>08:30</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>NO DISTURB.</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>LIDOCAINE 2% (20MG/M 25</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>08/21/01 06:00</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FORTYONE</p>
</blockquote></td>
<td><blockquote>
<p>DIAGNOSTIC COLONOSCOPY</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURANESTHETIST,TWO 06:00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63100</p>
</blockquote></td>
<td><blockquote>
<p>000-43-2109</p>
</blockquote></td>
<td><blockquote>
<p>COLONOSCOPY</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>GENERAL 07:05</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MILD DISTURB.</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>PROPOFOL 20ML INJ 65</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>08/21/01 07:00</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,THREE</p>
</blockquote></td>
<td><blockquote>
<p>PARATHYROID ADENOMA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURANESTHETIST,FOUR 07:00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63104</p>
</blockquote></td>
<td><blockquote>
<p>000-21-2453</p>
</blockquote></td>
<td><blockquote>
<p>PARATHYROID EXPLORATION AND EXCISION ADENOMA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>GENERAL 09:00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>SEVERE DISTURB.</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>SUFENTANIL CITRATE 5 120</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>08/22/01 10:10</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTYTWO</p>
</blockquote></td>
<td><blockquote>
<p>HX OF POLYP</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURANESTHETIST,ONE 10:15</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63106</p>
</blockquote></td>
<td><blockquote>
<p>000-99-8888</p>
</blockquote></td>
<td><blockquote>
<p>COLONOSCOPY, POLYPECTOMY</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>GENERAL 11:15</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MILD DISTURB.</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>PROPOFOL 20ML INJ 60</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>08/22/01 09:56</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTITIS</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURANESTHETIST,TWO 10:00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63110</p>
</blockquote></td>
<td><blockquote>
<p>000-56-7821</p>
</blockquote></td>
<td><blockquote>
<p>LAP CHOLE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>GENERAL 11:55</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>MILD DISTURB.</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>DESFLURANE 240ML BTL 115</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>08/24/01 14:55</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOURTEEN</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURANESTHETIST,FOUR 14:55</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63115</p>
</blockquote></td>
<td><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td><blockquote>
<p>INGUINAL HERNIA REPAIR</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>GENERAL 16:05</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>MILD DISTURB.</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>PROPOFOL 20ML INJ 70</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example 2: Print the List of Anesthetic Procedures for only Non-OR Procedures

> Select Anesthesia Reports Option: P List of Anesthetic Procedures

#### printout follows 

> MAYBERRY, NC PAGE: 1

> SURGICAL SERVICE REVIEWED BY: LIST OF ANESTHETIC PROCEDURES DATE REVIEWED:

> NON-O.R. PROCEDURES FROM: JAN 1,2001 TO: JAN 7,2001 DATE PRINTED: JAN 15,2001

> DATE PATIENT PRINCIPAL DIAGNOSIS PRIN ANESTHETIST START TIME

> CASE \# ID# PROCEDURE(S) ANESTH TECHNIQUE END TIME ASA CLASS ANESTH AGENT ELAPSED

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 22%" />
<col style="width: 35%" />
<col style="width: 27%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>01/02/01</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,SIXTEEN</p>
</blockquote></th>
<th><blockquote>
<p>TB</p>
</blockquote></th>
<th><blockquote>
<p>SURANESTHETIST,ONE</p>
</blockquote></th>
<th>09:43</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>51051</p>
</blockquote></td>
<td><blockquote>
<p>000-11-1111</p>
<p>MILD DISTURB.</p>
</blockquote></td>
<td><blockquote>
<p>BRONCHOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
<p>PHENOBARBITAL SODIUM</p>
</blockquote></td>
<td><blockquote>
<p>10:25</p>
<p>42</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/02/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTEEN</p>
</blockquote></td>
<td><blockquote>
<p>ILEITIS</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,TWO</p>
</blockquote></td>
<td>10:00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51053</p>
</blockquote></td>
<td><blockquote>
<p>000-11-1111</p>
<p>MILD DISTURB.</p>
</blockquote></td>
<td><blockquote>
<p>COLONSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>OTHER</p>
<p>FENTANYL 250MCG/5ML</p>
</blockquote></td>
<td><blockquote>
<p>11:10</p>
<p>70</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/02/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SEVEN</p>
</blockquote></td>
<td><blockquote>
<p>ESOPHAGEAL VARICES</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,FOUR</p>
</blockquote></td>
<td>13:10</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51057</p>
</blockquote></td>
<td><blockquote>
<p>000-84-0987</p>
<p>NO DISTURB.</p>
</blockquote></td>
<td><blockquote>
<p>ESOPHAGOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
<p>PROPOFOL 20ML INJ</p>
</blockquote></td>
<td><blockquote>
<p>13:45</p>
<p>35</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/04/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY</p>
</blockquote></td>
<td><blockquote>
<p>HISTOPLASMOSIS</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,THREE</p>
</blockquote></td>
<td>08:20</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51169</p>
</blockquote></td>
<td><blockquote>
<p>000-56-7821</p>
<p>MILD DISTURB.</p>
</blockquote></td>
<td><blockquote>
<p>BRONCHOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>OTHER</p>
<p>FENTANYL 250MCG/5ML</p>
</blockquote></td>
<td><blockquote>
<p>09:15</p>
<p>55</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/04/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FORTY</p>
</blockquote></td>
<td><blockquote>
<p>CARDIAC ARRYTHMIA</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,TWO</p>
</blockquote></td>
<td>18:50</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>88</p>
</blockquote></td>
<td><blockquote>
<p>000-77-7777</p>
<p>NO DISTURB.</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
<p>PHENOBARBITAL 30MG/7</p>
</blockquote></td>
<td><blockquote>
<p>19:25</p>
<p>35</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/07/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TEN</p>
</blockquote></td>
<td><blockquote>
<p>HISTOPLASMOSIS</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,THREE</p>
</blockquote></td>
<td>10:05</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51181</p>
</blockquote></td>
<td><blockquote>
<p>000-12-3456</p>
<p>MILD DISTURB.</p>
</blockquote></td>
<td><blockquote>
<p>BRONCHOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>OTHER</p>
<p>FENTANYL 250MCG/5ML</p>
</blockquote></td>
<td><blockquote>
<p>11:05</p>
<p>60</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/07/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,EIGHT</p>
</blockquote></td>
<td><blockquote>
<p>CHRONIC DEPRESSION</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,TWO</p>
</blockquote></td>
<td>13:10</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51185</p>
</blockquote></td>
<td><blockquote>
<p>000-37-0555</p>
<p>MILD DISTURB.</p>
</blockquote></td>
<td><blockquote>
<p>ELECTROCONVULSIVE THERAPY</p>
</blockquote></td>
<td><blockquote>
<p>OTHER</p>
<p>MIDAZOLAM 1MG/1ML 2M</p>
</blockquote></td>
<td><blockquote>
<p>13:35</p>
<p>25</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Anesthesia Provider Report

### \[SROADOC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Anesthesia Provider Report* option provides information concerning the anesthesia staff and techniques for completed cases within a selected date range. This report can be generated for all anesthesia providers or the user can specify one. It sorts the cases by the principal anesthetist and includes information on anesthesia personnel, technique, agent, level of supervision, and elapsed anesthesia time.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: Print the Anesthesia Provider Report

> Select Anesthesia Reports Option: D Anesthesia Provider Report

> *printout follows*

> MAYBERRY, NC PAGE: 1

> SURGICAL SERVICE REVIEWED BY: ANESTHESIA PROVIDER REPORT DATE REVIEWED:

> FROM: MAR 23,2001 TO: MAR 24,2001 DATE PRINTED: MAR 29,2001

> DATE PATIENT PROCEDURE(S) SUPERVISOR ASA CLASS LEVEL OF SUPERVISION

> CASE \# ID# RELIEF ANESTH PRINCIPAL TECHNIQUE ELAPSED ANES TIME ASST ANESTH ANESTHESIA AGENT

> ====================================================================================================================================

> \*\*\*\*\* SURANESTHETIST,ONE \*\*\*\*\*

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 38%" />
<col style="width: 13%" />
<col style="width: 18%" />
<col style="width: 4%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/23/01</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,</p>
</blockquote></th>
<th><blockquote>
<p>O</p>
</blockquote></th>
<th><blockquote>
<p>ESS, SEPTO,WITH LEFT TURBINECTOMY SCAR REVISION</p>
</blockquote></th>
<th>SURANESTHETIST,T</th>
<th><blockquote>
<p>MILD DISTURB.</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>54014</p>
</blockquote></td>
<td><blockquote>
<p>000-44-7629</p>
</blockquote></td>
<td></td>
<td></td>
<td>SURANESTHETIST,F</td>
<td><blockquote>
<p>GENERAL</p>
<p>DESFLURANE 240ML BTL</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>105 MINS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/23/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,</p>
</blockquote></td>
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p>COLONOSCOPY/ATTEMPTED</p>
</blockquote></td>
<td>SURANESTHETIST,T</td>
<td><blockquote>
<p>MILD DISTURB.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54020</p>
</blockquote></td>
<td><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td></td>
<td></td>
<td>SURANESTHETIST,S</td>
<td><blockquote>
<p>GENERAL</p>
<p>DESFLURANE 240ML BTL</p>
</blockquote></td>
<td>55</td>
<td><blockquote>
<p>MINS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/23/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,</p>
</blockquote></td>
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p>CYSTO, RETROGRADE, STENT</p>
</blockquote></td>
<td>SURANESTHETIST,T</td>
<td><blockquote>
<p>MILD DISTURB.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54050</p>
</blockquote></td>
<td><blockquote>
<p>000-34-5555</p>
</blockquote></td>
<td></td>
<td></td>
<td>SURANESTHETIST,F</td>
<td><blockquote>
<p>GENERAL</p>
<p>DESFLURANE 240ML BTL</p>
</blockquote></td>
<td>45</td>
<td><blockquote>
<p>MINS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/24/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,</p>
</blockquote></td>
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p>COLONOSCOPY/POLYPECTOMY</p>
</blockquote></td>
<td>SURANESTHETIST,T</td>
<td><blockquote>
<p>SEVERE DISTURB.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54023</p>
</blockquote></td>
<td><blockquote>
<p>000-58-7963</p>
</blockquote></td>
<td></td>
<td></td>
<td>SURANESTHETIST,S</td>
<td><blockquote>
<p>GENERAL</p>
<p>PROPOFOL 20ML INJ</p>
</blockquote></td>
<td>50</td>
<td><blockquote>
<p>MINS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/24/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,</p>
</blockquote></td>
<td><blockquote>
<p>E</p>
</blockquote></td>
<td><blockquote>
<p>COLONOSCOPY</p>
</blockquote></td>
<td>SURANESTHETIST,T</td>
<td><blockquote>
<p>MILD DISTURB.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54025</p>
</blockquote></td>
<td><blockquote>
<p>000-37-0555</p>
</blockquote></td>
<td></td>
<td></td>
<td>SURANESTHETIST,F</td>
<td><blockquote>
<p>GENERAL</p>
<p>DESFLURANE 240ML BTL</p>
</blockquote></td>
<td>65</td>
<td><blockquote>
<p>MINS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/24/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,</p>
</blockquote></td>
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td>SURANESTHETIST,T</td>
<td><blockquote>
<p>SEVERE DISTURB.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54024</p>
<p>NON-OR</p>
</blockquote></td>
<td><blockquote>
<p>000-56-7821</p>
</blockquote></td>
<td></td>
<td></td>
<td>SURANESTHETIST,S</td>
<td><blockquote>
<p>GENERAL</p>
<p>MIDAZOLAM 1MG/1ML 2M</p>
</blockquote></td>
<td>35</td>
<td><blockquote>
<p>MINS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/24/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,</p>
</blockquote></td>
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p>HEMORRHOIDECTOMY</p>
</blockquote></td>
<td>SURANESTHETIST,T</td>
<td><blockquote>
<p>SEVERE DISTURB.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54058</p>
</blockquote></td>
<td><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td></td>
<td></td>
<td>SURANESTHETIST,F</td>
<td><blockquote>
<p>SPINAL</p>
<p>BUPIVACAINE 0.25%</p>
</blockquote></td>
<td>45</td>
<td><blockquote>
<p>MINS.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>03/24/01</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,</p>
</blockquote></td>
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p>EXPL LAP, LYSIS OF ADHESIONS</p>
</blockquote></td>
<td>SURANESTHETIST,T</td>
<td><blockquote>
<p>SEVERE DIST.-EMERG</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>54079</p>
</blockquote></td>
<td><blockquote>
<p>000-99-8888</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>SURANESTHETIST,F</p>
<p>SURANESTHETIST,S</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
<p>DESFLURANE 240ML BTL</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>120 MINS.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## CPT Code Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR CPT REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *CPT Code Reports* menu contains reports based on CPT codes.

> The options included in this menu are listed below. To the left of the option name is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p><em>Cumulative Report of CPT Codes</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of CPT Coding Accuracy</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p><em>List Completed Cases Missing CPT Codes</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Cumulative Report of CPT Codes

### \[SROACCT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Cumulative Report of CPT Codes* option counts and reports the number of times a procedure was performed (based on CPT codes) during a specified date range. There is also a column showing how many times the procedure was in the Principal Procedure category, and how many times it was in the Other Operative Procedure category.

> After the date range is entered, the software will ask if the user wants the Cumulative Report of CPT Codes to include 1) only operating room surgical procedures, 2) non-O.R. procedures, or 3) both.

> These reports have a 132-column format and are designed to be copied to a printer.

> Example 1: Print the Cumulative Report of CPT Codes for only OR Surgical Procedures

> Select CPT Code Reports Option: C Cumulative Report of CPT Codes

> *printout follows*

> O.R. SURGICAL PROCEDURES

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY

> CUMULATIVE REPORT OF CPT CODES DATE REVIEWED: FROM: MAR 28,2001 TO: APR 3,2001

> CPT CODE - SHORT DESCRIPTION TOTAL PROCEDURES TOTAL PRINCIPAL PROCEDURES TOTAL OTHER PROCEDURES

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 29%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>10060</th>
<th><blockquote>
<p>DRAINAGE OF SKIN ABSCESS</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11440</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11441</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11641</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="even">
<td>24075</td>
<td><blockquote>
<p>REMOVE ARM/ELBOW LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>26989</td>
<td><blockquote>
<p>HAND/FINGER SURGERY</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>30520</td>
<td><blockquote>
<p>REPAIR OF NASAL SEPTUM</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>31231</td>
<td><blockquote>
<p>NASAL ENDOSCOPY, DX</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>45315</td>
<td><blockquote>
<p>PROCTOSIGMOIDOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>45330</td>
<td><blockquote>
<p>SIGMOIDOSCOPY, DIAGNOSTIC</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>45333</td>
<td><blockquote>
<p>SIGMOIDOSCOPY &amp; POLYPECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>45378</td>
<td><blockquote>
<p>DIAGNOSTIC COLONOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>45385</td>
<td><blockquote>
<p>COLONOSCOPY, LESION REMOVAL</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>47600</td>
<td><blockquote>
<p>REMOVAL OF GALLBLADDER</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>49000</td>
<td><blockquote>
<p>EXPLORATION OF ABDOMEN</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>49505</td>
<td><blockquote>
<p>REPAIR INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>66984</td>
<td><blockquote>
<p>REMOVE CATARACT, INSERT LENS</p>
</blockquote></td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>68801</td>
<td><blockquote>
<p>DILATE TEAR DUCT OPENING</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example 2: Print the Cumulative Report of CPT Codes for only Non-O.R. Procedures

> Select CPT Code Reports Option: C Cumulative Report of CPT Codes

#### printout follows 

> NON-O.R. PROCEDURES

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY

> CUMULATIVE REPORT OF CPT CODES DATE REVIEWED: FROM: JUL 1,2001 TO: DEC 31,2001

> CPT CODE - SHORT DESCRIPTION TOTAL PROCEDURES TOTAL PRINCIPAL PROCEDURES TOTAL OTHER PROCEDURES

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 29%" />
<col style="width: 17%" />
<col style="width: 20%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>10060</th>
<th><blockquote>
<p>DRAINAGE OF SKIN ABSCESS</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10061</td>
<td><blockquote>
<p>DRAINAGE OF SKIN ABSCESS</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11040</td>
<td><blockquote>
<p>DEBRIDE SKIN PARTIAL</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11042</td>
<td><blockquote>
<p>DEBRIDE SKIN/TISSUE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11100</td>
<td><blockquote>
<p>BIOPSY OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11402</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11420</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11620</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11640</td>
<td><blockquote>
<p>REMOVAL OF SKIN LESION</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11730</td>
<td><blockquote>
<p>REMOVAL OF NAIL PLATE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>11750</td>
<td><blockquote>
<p>REMOVAL OF NAIL BED</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12001</td>
<td><blockquote>
<p>REPAIR SUPERFICIAL WOUND(S)</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>12011</td>
<td><blockquote>
<p>REPAIR SUPERFICIAL WOUND(S)</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>14060</td>
<td><blockquote>
<p>SKIN TISSUE REARRANGEMENT</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>15782</td>
<td><blockquote>
<p>ABRASION TREATMENT OF SKIN</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>17340</td>
<td><blockquote>
<p>CRYOTHERAPY OF SKIN</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>20550</td>
<td><blockquote>
<p>INJ TENDON/LIGAMENT/CYST</p>
</blockquote></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>29799</td>
<td><blockquote>
<p>CASTING/STRAPPING PROCEDURE</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>46083</td>
<td><blockquote>
<p>INCISE EXTERNAL HEMORRHOID</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Report of CPT Coding Accuracy

### \[SR CPT ACCURACY\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of CPT Coding Accuracy* option lists cases sorted by the CPT code used in the PRINCIPAL PROCEDURES field and OTHER OPERATIVE PROCEDURES field. This option is designed to help check the accuracy of the coding procedures.

> About the prompts

> "Do you want to print the Report of CPT Coding Accuracy for all CPT Codes ?" The user should reply NO to this prompt to produce the report for only one CPT code. The software will then prompt the user to enter the CPT code or category.

> "Do you want to sort the Report of CPT Coding Accuracy by Surgical Specialty ?" The user should press the \<Enter\> key if he or she wants to sort the report by specialty. The user would enter NO to sort the report by date only.

> "Do you want to print the Report to Check Coding Accuracy for all Surgical Specialties ?" The user can enter the code or name of the surgical service he or she wants the report to be based on or can press the

> \<Enter\> key to print the report for all surgical specialties.

> Example 1: Print the Report of CPT Coding Accuracy for OR Surgical Procedures, sorted by Surgical Specialty

> Select CPT Code Reports Option: A Report of CPT Coding Accuracy

> *printout follows*

> O.R. SURGICAL PROCEDURES

> MAYBERRY, NC PAGE

> SURGICAL SERVICE 1

> REPORT OF CPT CODING ACCURACY REVIEWED BY: FOR GENERAL(OR WHEN NOT DEFINED BELOW) DATE REVIEWED:

> FROM: OCT 8,2001 TO: OCT 8,2001

PROCEDURE DATE PATIENT PROCEDURES SURGEON/PROVIDER

CASE \# ID# ATTEND SURG/PROV

> ====================================================================================================================================

> 47600 REMOVAL OF GALLBLADDER PRINCIPAL PROCEDURES

> DESCRIPTION: CHOLECYSTECTOMY;

> 10/08/01 07:00 SURPATIENT,EIGHTEEN CHOLECYSTECTOMY SURSURGEON,TWO

> 63072 000-22-3334 CPT Codes:47600-22 SURSURGEON,FOUR

> ==================================================================================================================================== 47605 REMOVAL OF GALLBLADDER

> OTHER PROCEDURES DESCRIPTION: CHOLECYSTECTOMY;

> WITH CHOLANGIOGRAPHY

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 23%" />
<col style="width: 41%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><p>10/08/01 10:00</p>
<blockquote>
<p>63077</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TWELVE 000-41-8719</p>
</blockquote></th>
<th><blockquote>
<p>INGUINAL HERNIA, OTHER OPERATIONS: CHOLECYSTECTOMY (</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,FOUR SURSURGEON,FOUR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>CPT Codes: 49521, 47605-22</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> 49505 REPAIR INGUINAL HERNIA PRINCIPAL PROCEDURES

> DESCRIPTION: REPAIR INITIAL INGUINAL HERNIA, AGE 5 YEARS OR OVER; REDUCIBLE

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 23%" />
<col style="width: 34%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>10/08/01 06:00</th>
<th><blockquote>
<p>SURPATIENT,FOUR</p>
</blockquote></th>
<th><blockquote>
<p>INGUINAL HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63071</p>
</blockquote></td>
<td><blockquote>
<p>000-45-7212</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 49505</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,SIXTEEN</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> Example 2: Print the Report of CPT Coding Accuracy for OR Surgical Procedures, sorted by Date

> Select CPT Code Reports Option: A Report of CPT Coding Accuracy

#### printout follows 

> O.R. SURGICAL PROCEDURES

> MAYBERRY, NC PAGE

> SURGICAL SERVICE 1

> REPORT OF CPT CODING ACCURACY REVIEWED BY:

> FROM: OCT 1,2001 TO: OCT 7,2001 DATE REVIEWED:

PROCEDURE DATE PATIENT PROCEDURES SURGEON/PROVIDER

CASE \# ID# ATTEND SURG/PROV

> SPECIALTY

> ====================================================================================================================================

> 31365 REMOVAL OF LARYNX PRINCIPAL PROCEDURES

> DESCRIPTION: LARYNGECTOMY; TOTAL, WITH RADICAL NECK DISSECTION

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 31%" />
<col style="width: 27%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>10/03/01 07:00</th>
<th><blockquote>
<p>SURPATIENT,NINETEEN</p>
</blockquote></th>
<th><blockquote>
<p>PULMONARY LOBECTOMY</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,SEVENTEEN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63059</p>
</blockquote></td>
<td><blockquote>
<p>000-28-7354</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 31365</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>THORACIC SURGERY (INC. CARDIAC SURG.)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ==================================================================================================================================== 32440 REMOVAL OF LUNG

> PRINCIPAL PROCEDURES DESCRIPTION: REMOVAL OF LUNG, TOTAL PNEUMONECTOMY;

10/03/01 10:00 SURPATIENT,TWENTY PULMONARY LOBECTOMY SURSURGEON,FOUR

63060 000-45-4886 CPT Codes: 32440 SURSURGEON,FOUR

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 33%" />
<col style="width: 28%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>10/04/01 06:00</p>
</blockquote></th>
<th><blockquote>
<p>THORACIC SURGERY (INC. CARDIAC SURG.)</p>
<p>SURPATIENT,TEN</p>
</blockquote></th>
<th><blockquote>
<p>PULMONARY LOBECTOMY</p>
</blockquote></th>
<th>SURSURGEON,TWO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63069</p>
</blockquote></td>
<td><blockquote>
<p>000-12-3456</p>
<p>THORACIC SURGERY (INC. CARDIAC SURG.)</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 32440</p>
</blockquote></td>
<td>SURSURGEON,TWO</td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> 32480 PARTIAL REMOVAL OF LUNG PRINCIPAL PROCEDURES

> DESCRIPTION: REMOVAL OF LUNG, OTHER THAN TOTAL PNEUMONECTOMY; SINGLE LOBE (LOBECTOMY)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 31%" />
<col style="width: 27%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>10/03/01 06:00</th>
<th><blockquote>
<p>SURPATIENT,TWELVE</p>
</blockquote></th>
<th><blockquote>
<p>PULMONARY LOBECTOMY</p>
</blockquote></th>
<th>SURSURGEON,TWO</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63049</p>
</blockquote></td>
<td><blockquote>
<p>000-41-8719</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes: 32480</p>
</blockquote></td>
<td>SURSURGEON,ONE</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>THORACIC SURGERY (INC. CARDIAC SURG.)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 10/03/01 07:00 SURPATIENT,SEVENTEEN PULMONARY LOBECTOMY SURSURGEON,TWO

> 63050 000-45-5119 CPT Codes: 32480 SURSURGEON,TWO THORACIC SURGERY (INC. CARDIAC SURG.)

> Example 3: Print the Report of CPT Coding Accuracy for Non-O.R. Procedures, sorted by CPT Code and Medical Specialty

> Select CPT Code Reports Option: A Report of CPT Coding Accuracy

#### printout follows 

> NON-O.R. PROCEDURES

> MAYBERRY, NC PAGE

> SURGICAL SERVICE 1

> REPORT OF CPT CODING ACCURACY REVIEWED BY: FOR MEDICINE DATE REVIEWED:

> FROM: JAN 1,2001 TO: AUG 31,2001

PROCEDURE DATE PATIENT PROCEDURES SURGEON/PROVIDER

CASE \# ID# ATTEND SURG/PROV

> ====================================================================================================================================

> 92960 HEART ELECTROCONVERSION PRINCIPAL PROCEDURES

> DESCRIPTION: CARDIOVERSION, ELECTIVE, ELECTRICAL CONVERSION OF ARRHYTHMIA, EXTERNAL

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 27%" />
<col style="width: 33%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th>01/24/95</th>
<th><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></th>
<th><blockquote>
<p>CARDIOVERSION</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15499</td>
<td><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes (92960)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>02/09/95</td>
<td><blockquote>
<p>SURPATIENT,NINE</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15701</td>
<td><blockquote>
<p>000-34-5555</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes (92960)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>03/29/95</td>
<td><blockquote>
<p>SURPATIENT,FIFTEEN</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>15912</td>
<td><blockquote>
<p>000-98-1234</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes (92960)</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>08/04/95</td>
<td><blockquote>
<p>SURPATIENT,SIX</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION (</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>16669</td>
<td><blockquote>
<p>000-09-8797</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes (92960)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>08/25/95</td>
<td><blockquote>
<p>SURPATIENT,TWO</p>
</blockquote></td>
<td><blockquote>
<p>CARDIOVERSION</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>16828</td>
<td><blockquote>
<p>000-45-1982</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes (92960)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> List Completed Cases Missing CPT Codes

### \[SRSCPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *List Completed Cases Missing CPT Codes* option generates a report of completed cases that are missing the Principal CPT code for a specified date range. Only procedures that have CPT codes will be counted on the Annual Report of Surgical Procedures.

> After the date range has been entered, the software will ask if the user wants the Cumulative Report of CPT Codes to include: 1) only operating room surgical procedures, 2) non-O.R. procedures, or 3) both.

> This report is in an 80-column format and can be viewed on the screen.

> Example: List Completed Cases Missing CPT Codes

> Select CPT Code Reports Option: M List Completed Cases Missing CPT Codes

> *printout follows*

> MAYBERRY, NC

> Completed Cases Missing CPT Codes

> O.R. Surgical Procedures From: FEB 1,2005 To: APR 30,2005

> Specialty: GENERAL(OR WHEN NOT DEFINED BELOW)

> Operation Date Patient (ID#) Surgeon/Provider Case \#

> ================================================================================

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 50%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>FEB 01, 2005</th>
<th><blockquote>
<p>SURPATIENT,TWO (000-45-1982)</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>53708</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXC LEFT PREAURICULAR LESION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>FEB 08, 2005</td>
<td><blockquote>
<p>SURPATIENT,FIVE (000-58-7963)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>53747</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXCISION LESIONS SCALP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>MAR 12, 2005</td>
<td><blockquote>
<p>SURPATIENT,SEVEN (000-84-0987)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>53973</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* COLONOSCOPY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>MAR 23, 2005</td>
<td><blockquote>
<p>SURPATIENT,FORTYONE (000-43-2109)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>54030</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* COLONOSCOPY/ATTEMPTED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>APR 27, 2005</td>
<td><blockquote>
<p>SURPATIENT,THIRTY (000-82-9472)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,SEVENTEEN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>54325</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXCISION RT FOREARM LESIONS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXC LESION, RT EAR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXC LESION, RT FOREHEAD</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXC LESION RT SCALP</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* RXC LESION, NOSE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXC LESION, LEFT EAR</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXC LESION, LEFT FOREARM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>* EXC LESION, TOP OF HEAD</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>* EXC LESION, LEFT NECK</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Laboratory Interim Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO-LRRP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Laboratory Interim Report* option accesses the Laboratory Package to show what lab tests the patient has had. This option will print or display interim reports for a selected patient, within a given time period. The printout will go in inverse date order. This report will output all tests for the time period specified.

> This option only prints verified results and does not output the microbiology reports.

> Example: Print Laboratory Interim Report

> Select Surgery Menu Option: L Laboratory Interim Report

> *printout follows*

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 14%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SIXTY</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>09/21/2001 1:21 pm</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SSN: 000-56-7821</p>
</blockquote></td>
<td><blockquote>
<p>SEX: F</p>
</blockquote></td>
<td><blockquote>
<p>AGE:</p>
</blockquote></td>
<td><blockquote>
<p>42</p>
</blockquote></td>
<td><blockquote>
<p>LOC: LRC</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Provider: SURSURGEON,FOUR

> Specimen: SERUM

> Accession \[UID\]: CH 0513 1 \[3471330001\]

> 05/13/1997 07:00

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 24%" />
<col style="width: 17%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Test name</p>
</blockquote></th>
<th>Result</th>
<th><blockquote>
<p>units</p>
</blockquote></th>
<th>Ref. range</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GLUCOSE</p>
</blockquote></td>
<td>87</td>
<td><blockquote>
<p>mg/dL</p>
</blockquote></td>
<td>60 - 123</td>
</tr>
<tr class="even">
<td><blockquote>
<p>UREA NITROGEN</p>
</blockquote></td>
<td>22</td>
<td><blockquote>
<p>mg/dL</p>
</blockquote></td>
<td>11 - 24</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CREATININE</p>
</blockquote></td>
<td>1.8</td>
<td><blockquote>
<p>mg/dl</p>
</blockquote></td>
<td>1 - 2.1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>POTASSIUM</p>
</blockquote></td>
<td>4.4</td>
<td><blockquote>
<p>meq/L</p>
</blockquote></td>
<td>3.5 - 4.8</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SODIUM</p>
</blockquote></td>
<td>143</td>
<td><blockquote>
<p>meq/L</p>
</blockquote></td>
<td>135 - 145</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CHLORIDE</p>
</blockquote></td>
<td>103</td>
<td><blockquote>
<p>meq/L</p>
</blockquote></td>
<td>95 - 105</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CO2</p>
</blockquote></td>
<td>27.0</td>
<td><blockquote>
<p>meq/L</p>
</blockquote></td>
<td>20 - 32</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CALCIUM</p>
</blockquote></td>
<td>8.7</td>
<td><blockquote>
<p>mg/dL</p>
</blockquote></td>
<td>8.5 - 11</td>
</tr>
</tbody>
</table>

> ==============================================================================

> KEY: "L"=Abnormal low, "H"=Abnormal high, "\*"=Critical value SURPATIENT,SIXTY 000-56-7821 09/21/2001 1:21 pm PRESS '^' TO STOP

# Chapter Four: Chief of Surgery Reports Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes options and reports for the exclusive use of the Surgical Service Chief, or his or her designee. The Chief has access to lists of cancellations, the Morbidity and Mortality Report, and Patient Occurrences.

> <span id="_bookmark136" class="anchor"></span>Exiting an Option or the System

> The user should enter an up-arrow (^) to stop what he or she is doing. The up-arrow can be used at almost any prompt to terminate the line of questioning and return to the previous level in the routine. Continuing to enter up-arrows will cause the user to completely exit the system.

## Option Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The main options included in this chapter are listed below. To the left of the option name is the shortcut synonym that the user can enter to select the option. The *Chief of Surgery Menu* option will not display if the user does not have proper security clearance.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CH</p>
</blockquote></td>
<td><blockquote>
<p><em>Chief of Surgery Menu</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Chief of Surgery Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROCHIEF\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Chief of Surgery Menu* is a restricted option (locked with the SROCHIEF key), allowing access to various management reports and functions. It is designed for the Chief of Surgery and his or her designees. The options available from this menu are shown in the following table.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option or Menu Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>V</p>
</blockquote></td>
<td><blockquote>
<p><em>View Patient Perioperative Occurrences</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p><em>Management Reports</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p><em>Unlock a Case for Editing</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RET</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Status of Returns Within 30 Days</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CAN</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Cancelled Case ...</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Operations as Unrelated/Related to Death</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td><blockquote>
<p><em>Update/Verify Procedure/Diagnosis Codes</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark139" class="anchor"></span>View Patient Perioperative Occurrences

### \[SROMEN-M&M\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *View Patient Perioperative Occurrences* option is designed to provide a quick view of any occurrences for a particular case. This report can be viewed on a screen.

> Example: View Patient Perioperative Occurrences

## Management Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO-CHIEF REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Management Reports* menu is designed to give the Chief of Surgery various management reports. The reports contained on this menu are listed below. To the left of the option/report name is the shortcut synonym that the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>MM</p>
</blockquote></td>
<td><blockquote>
<p><em>Morbidity &amp; Mortality Reports</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MV</p>
</blockquote></td>
<td><blockquote>
<p><em>M&amp;M Verification Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CD</p>
</blockquote></td>
<td><blockquote>
<p><em>Comparison of Preop and Postop Diagnosis</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Delay and Cancellation Reports ...</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>V</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Unverified Surgery Cases</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RET</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Returns to Surgery</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Daily Operating Room Activity</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NS</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Cases Without Specimens</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICU</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Unscheduled Admissions to ICU</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td><blockquote>
<p><em>Operating Room Utilization Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>WC</p>
</blockquote></td>
<td><blockquote>
<p><em>Wound Classification Report</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>BA</p>
</blockquote></td>
<td><blockquote>
<p><em>Print Blood Product Verification Audit Log</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KEY</p>
</blockquote></td>
<td><blockquote>
<p><em>Key Missing Surgical Package Data</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OC</p>
</blockquote></td>
<td><blockquote>
<p><em>Admitted w/in 14 days of Out Surgery If Postop</em></p>
<p><em>Occ</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DS</p>
</blockquote></td>
<td><blockquote>
<p><em>Death Within 30 Days of Surgery</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Morbidity & Mortality Reports

### \[SROMM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Morbidity & Mortality Reports* option generates two reports: the Perioperative Occurrences Report and the Mortality Report. The Perioperative Occurrences Report includes all cases that have occurrences, both intraoperatively and postoperatively, and can be sorted by specialty, attending surgeon, or occurrence category. The Mortality Report includes all cases performed within the selected date range that had a death within 30 days after surgery, and sort by specialty within a date range. Each surgical specialty will begin on a separate page.

> After the user enters the date range, the software will ask whether to generate both reports. If the user answers NO, the software will ask the user to select from the Perioperative Occurrences Report or the Mortality Report.

> These reports have a 132-column format and are designed to be copied to a printer.

> Example 1: Printing the Perioperative Occurrences Report – Sorted by Specialty

> Select Perioperative Occurrences Menu Option: M Morbidity & Mortality Reports

> *report follows*

> *(This page included for two-sided copying.)*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE REVIEWED BY: PERIOPERATIVE OCCURRENCES-INTRAOP/POSTOP DATE REVIEWED:

> FROM: JUL 1,2006 TO: JUL 31,2006 DATE PRINTED: AUG 22,2006

> PATIENT ATTENDING SURGEON OCCURRENCE(S) - (DATE) OUTCOME

> ID# PRINCIPAL OPERATION TREATMENT OPERATION DATE

> ==================================================================================================================================== GENERAL(OR WHEN NOT DEFINED BELOW)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 34%" />
<col style="width: 42%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE</p>
<p>000-41-8719</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,THREE</p>
<p>REPAIR DIAPHRAGMATIC HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>MYOCARDIAL INFARCTION</p>
<p>ASPIRIN THERAPY</p>
</blockquote></th>
<th>I</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>JUL 07, 2006@07:15</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>URINARY TRACT INFECTION * (07/09/06)</p>
</blockquote></td>
<td>I</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>IV ANTBIOTICS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,FOURTEEN 000-45-7212</p>
<p>JUL 31, 2006@09:00</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FIVE CHOLECYSTECTOMY, APPENDECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SUPERFICIAL WOUND INFECTION * (08/02/06) ANTIBIOTICS</p>
</blockquote></td>
<td>I</td>
</tr>
</tbody>
</table>

> OUTCOMES: U - UNRESOLVED, I - IMPROVED, W - WORSE, D - DEATH

> '\*' Represents Postoperative Occurrences

> Example 2: Printing the Perioperative Occurrences Report – Sorted by Attending Surgeon

> Select Perioperative Occurrences Menu Option: M Morbidity & Mortality Reports

#### report follows 

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE REVIEWED BY: PERIOPERATIVE OCCURRENCES-INTRAOP/POSTOP DATE REVIEWED:

> FROM: JUL 1,2006 TO: JUL 31,2006 DATE PRINTED: AUG 22,2006

> PATIENT SURGICAL SPECIALTY OCCURRENCE(S) - (DATE) OUTCOME

> ID# PRINCIPAL OPERATION TREATMENT OPERATION DATE

> ====================================================================================================================================

> ATTENDING: SURGEON,ONE

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 36%" />
<col style="width: 40%" />
<col style="width: 4%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE</p>
<p>000-41-8719</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW)</p>
<p>REPAIR DIAPHRAGMATIC HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>MYOCARDIAL INFARCTION</p>
<p>ASPIRIN THERAPY</p>
</blockquote></th>
<th>I</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>JUL 07, 2006@07:15</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>URINARY TRACT INFECTION * (07/09/06)</p>
</blockquote></td>
<td>I</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>IV ANTBIOTICS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,THREE 000-21-2453</p>
<p>JUL 22, 2006@10:00</p>
</blockquote></td>
<td><blockquote>
<p>CARDIAC SURGERY CABG</p>
</blockquote></td>
<td><blockquote>
<p>REPEAT VENTILATOR SUPPORT W/IN 30 DAYS *</p>
</blockquote></td>
<td>I</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,FOURTEEN 000-45-7212</p>
<p>JUL 31, 2006@09:00</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW) CHOLECYSTECTOMY, APPENDECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SUPERFICIAL WOUND INFECTION * (08/02/06) ANTIBIOTICS</p>
</blockquote></td>
<td>I</td>
</tr>
</tbody>
</table>

> OUTCOMES: U - UNRESOLVED, I - IMPROVED, W - WORSE, D - DEATH

> '\*' Represents Postoperative Occurrences

> Example 3: Printing the Perioperative Occurrences Report – Sorted by Occurrence Category

> Select Perioperative Occurrences Menu Option: M Morbidity & Mortality Reports

#### report follows 

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE REVIEWED BY: PERIOPERATIVE OCCURRENCES-INTRAOP/POSTOP DATE REVIEWED:

> FROM: JUN 1,2007 TO: JUN 30,2007 DATE PRINTED: AUG 22,2007

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 31%" />
<col style="width: 37%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>ATTENDING SURGEON</p>
</blockquote></th>
<th><blockquote>
<p>OCCURRENCE(S) - (DATE)</p>
</blockquote></th>
<th><blockquote>
<p>OUTCOME</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID#</p>
</blockquote></td>
<td><blockquote>
<p>SURGICAL SPECIALTY</p>
</blockquote></td>
<td><blockquote>
<p>TREATMENT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OPERATION DATE</p>
</blockquote></td>
<td><blockquote>
<p>PRINCIPAL OPERATION</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> CATEGORY: ACUTE RENAL FAILURE

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 36%" />
<col style="width: 32%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></th>
<th><blockquote>
<p>SURGEON,TWO</p>
</blockquote></th>
<th><blockquote>
<p>ACUTE RENAL FAILURE</p>
</blockquote></th>
<th>I</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
<td><blockquote>
<p>DIALYSIS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JUN 18, 2007@07:15</p>
</blockquote></td>
<td><blockquote>
<p>REPAIR INCARCERATED INGUINAL HERNIA</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> OUTCOMES: U - UNRESOLVED, I - IMPROVED, W - WORSE, D - DEATH

> '\*' Represents Postoperative Occurrences

> Example 4: Print the Mortality Report

> Select Management Reports Option: MM Morbidity & Mortality Reports

#### printout follows 

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 42%" />
<col style="width: 20%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>MAYBERRY, NC SURGICAL SERVICE</p>
</blockquote></th>
<th><blockquote>
<p>REVIEWED BY:</p>
</blockquote></th>
<th><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>MORTALITY REPORT</p>
</blockquote></td>
<td><blockquote>
<p>DATE REVIEWED:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>FROM: JAN 1,2006 TO: JUL 31,2006</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DATE PRINTED: AUG 22,2006</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OPERATION DATE</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ID#</p>
</blockquote></td>
<td><blockquote>
<p>PRINCIPAL OPERATIVE PROCEDURE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DATE OF DEATH AUTOPSY (Y/N)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> OTORHINOLARYNGOLOGY (ENT)

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 23%" />
<col style="width: 51%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>JAN 22, 2006</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,SIXTEEN 000-11-1111</p>
</blockquote></th>
<th><blockquote>
<p>LARYNGOSCOPY, BRONCHOSCOPY, ESOPHAGOGASTROSCOPY</p>
</blockquote></th>
<th><blockquote>
<p>FEB 09, 2006 NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>JAN 27, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWO 000-45-1982</p>
</blockquote></td>
<td><blockquote>
<p>BRONCHOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>FEB 26, 2006 NOT AVAILABLE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JAN 29, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTEEN 000-11-1111</p>
</blockquote></td>
<td><blockquote>
<p>BILATERAL NECK DISECTION, LARYNGECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>FEB 09, 2006 NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FEB 08, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTEEN 000-11-1111</p>
</blockquote></td>
<td><blockquote>
<p>LIGATION LT INTERNAL JUGLAR , EXPLORATORY LAPARATOMY</p>
</blockquote></td>
<td><blockquote>
<p>FEB 09, 2006 NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FEB 19, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TEN 000-12-3456</p>
</blockquote></td>
<td><blockquote>
<p>TRACH</p>
</blockquote></td>
<td><blockquote>
<p>FEB 21, 2006 NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JUL 20, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FORTY 000-77-7777</p>
</blockquote></td>
<td><blockquote>
<p>LARYNGOSCOPY W/ BX, ESOPHAGOSCOPY</p>
</blockquote></td>
<td><blockquote>
<p>NOV 01, 2006 NOT AVAILABLE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> M&M Verification Report

### \[SRO M&M VERIFICATION REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *M&M Verification Report* option produces the M&M Verification Report that may be useful for (1) reviewing occurrences and their assignments to operations and (2) reviewing deaths unrelated/related assignments to operations

> Two varieties of this report are available. The first variety provides a report of all patients who had operations within the selected date range and experienced intraoperative occurrences, postoperative occurrences, or death within 90 days of surgery. The second variety provides a similar report for all risk- assessed operations that are in a completed state but have not yet been transmitted to the national database.

> Variety \#1: Report information is printed patient-by-patient, listing all operations for the patient that occurred during the selected date range, as well as any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some operations that were performed prior to the selected date range, and, if printed by specialty, may include operations performed by other specialties. For every operation that is listed, the intraoperative and postoperative occurrences are also listed. The report also includes information about whether the operation was unrelated or related to death as well as the risk assessment type and status (if assessed). The report may be printed for a selected list of surgical specialties.

> Variety \#2: Report information is printed patient-by-patient in a format similar to Variety \#1. This report lists all risk-assessed operations that are in a completed state but have not yet been transmitted to the national database and that have intraoperative occurrences, postoperative occurrences, or death within 90 days of surgery. The report includes any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some other operations that may or may not be risk assessed, and, if risk assessed, may have any risk assessment status (incomplete, complete, or transmitted). Every patient listed on this report will have at least one operation with a risk assessment status of "complete."

> Example 1: Generate an M&M Verification Report (Full Report)

> Select Management Reports Option: MV M&M Verification Report

> *printout follows*

> MAYBERRY, NC Page 1

> M&M Verification Report

> From: DEC 31,2001 To: JAN 31,2002 Reviewed By:

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 27%" />
<col style="width: 10%" />
<col style="width: 28%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="6"><blockquote>
<p>Report Generated: FEB 21,2002 Date Reviewed:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Op Date</p>
</blockquote></td>
<td><blockquote>
<p>Specialty</p>
</blockquote></td>
<td><blockquote>
<p>Procedure(s)</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Death</p>
<p>Related Occurrence(s) - (Date)</p>
</blockquote></td>
<td><blockquote>
<p>Assessment</p>
<p>Type/Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>====================================================================================================================================</p>
<p>&gt;&gt;&gt; SURPATIENT,THIRTY (000-82-9472) - DIED 02/27/02</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>01/06/02</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
<td><blockquote>
<p>TOTAL LARYNGECTOMY</p>
</blockquote></td>
<td>NO</td>
<td></td>
<td>NON-CARD/T</td>
</tr>
<tr class="even">
<td><blockquote>
<p>12/29/01</p>
</blockquote></td>
<td><blockquote>
<p>THORACIC</p>
</blockquote></td>
<td><blockquote>
<p>CABG, VEIN, SIX+</p>
</blockquote></td>
<td>NO</td>
<td></td>
<td>CARDIAC/I</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11/20/01</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERAL</p>
</blockquote></td>
<td><blockquote>
<p>LT CAROTID ENDOARTERECTOMY</p>
</blockquote></td>
<td>N/A</td>
<td><blockquote>
<p>OTHER OCCURRENCE (11/20/01)</p>
</blockquote></td>
<td>NON-CARD/T</td>
</tr>
</tbody>
</table>

> ICD: 998.4 FB LEFT DURING PROCEDURE URINARY TRACT INFECTION \* (12/08/01)

> ICD: 599.0 URIN TRACT INFECTION NOS OTHER RESPIRATORY OCCURRENCE \* (11/25/01)

> ICD: 478.25 EDEMA PHARYNX/NASOPHARYX OTHER OCCURRENCE \* (NO DATE)

> ICD: 530.1 ESOPHAGITIS

> 11/02/01 PERIPHERAL EVACUATION OF HEMATOMA LT.THIGH YES DVT/THROMBOPHLEBITIS \* (11/06/01) NON-CARD/I

> ICD: 453.8 VENOUS THROMBOSIS NEC BLEEDING/TRANSFUSIONS \* (11/04/01) BLEEDING/TRANSFUSIONS \* (11/06/01) BLEEDING/TRANSFUSIONS \* (11/06/01)

> Occurrences(s): '\*' Denotes Postop Occurrence Assessment Status - I:Incomplete, C:Complete, T:Transmitted

> Example 2: Generate an M&M Verification Report (Pre-Transmission Report)

> Select Management Reports Option: MV M&M Verification Report

#### printout follows 

MAYBERRY, NC Page 1

> M&M Verification Report

> Pre-Transmission Report for Completed Assessments Reviewed By: Report Generated: DEC 31,2002 Date Reviewed:

Death Assessment

Op Date Specialty Procedure(s) Related Occurrence(s) - (Date) Type/Status

====================================================================================================================================

> \>\>\> SURPATIENT,FOUR (000-17-0555) - DIED 12/30/02@07:16

12/24/02 UROLOGY CYSTOSCOPY YES EXCLUDED/C

> \>\>\> SURPATIENT,FIFTYTWO (000-99-8888) - DIED 03/02/02@13:20

> 01/31/02 GENERAL LEFT BKA STUMP DEBRIDEMENT & REVISION ? URINARY TRACT INFECTION \* (02/09/02) EXCLUDED/C

> ICD: 599.0 URIN TRACT INFECTION NOS PNEUMONIA \* (02/15/02)

> ICD: 485. BRONCOPNEUMONIA ORG NOS

> \>\>\> SURPATIENT,ONE (000-44-7629) - DIED 08/13/02@19:00

> 08/05/02 PERIPHERAL LEFT LEG ABOVE KNEE AMPUTATION, RIGHT NO EXCLUDED/C LEG ABOVE KNEE AMPUTATION

> \>\>\> SURPATIENT,SIXTEEN (000-11-1111) - DIED 10/01/02

> 08/21/02 PERIPHERAL OMEGAPORT PLACEMENT ? EXCLUDED/C

> \>\>\> SURPATIENT,FIVE (000-58-7963) - DIED 04/08/02

> 03/14/02 GENERAL HICKMAN CATH PLACMENT NO EXCLUDED/C

> Occurrences(s): '\*' Denotes Postop Occurrence Assessment Status - I:Incomplete, C:Complete, T:Transmitted

> Comparison of Preop and Postop Diagnosis

### \[SROPPC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Comparison of Preop and Postop Diagnosis* option generates a list of completed cases in which the principal preoperative and principal postoperative diagnoses are different.

> Example: Print Comparison of Preop and Postop Diagnosis Report

> Select Management Reports Option: CD Comparison of Preop and Postop Diagnosis

> *report follows*

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY: COMPARISON OF PREOP AND POSTOP DIAGNOSIS DATE REVIEWED:

> FROM: MAR 1,2002 TO: MAR 31,2002 DATE PRINTED: APR 22,2002

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 30%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>DATE CASE #</th>
<th><blockquote>
<p>PATIENT ID #</p>
<p>SURGICAL SPECIALTY</p>
</blockquote></th>
<th><blockquote>
<p>PREOPERATIVE DIAGNOSIS</p>
</blockquote></th>
<th><blockquote>
<p>POSTOPERATIVE DIAGNOSIS</p>
</blockquote></th>
<th><blockquote>
<p>WOUND CLASS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>03/03/02</td>
<td><blockquote>
<p>SURPATIENT,ONE</p>
</blockquote></td>
<td><blockquote>
<p>APPENDICITIS</p>
</blockquote></td>
<td><blockquote>
<p>ACUTE APPENDICITIS</p>
</blockquote></td>
<td><blockquote>
<p>D</p>
</blockquote></td>
</tr>
<tr class="even">
<td>63064</td>
<td><blockquote>
<p>000-44-7629</p>
<p>GENERAL</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>03/04/02</td>
<td><blockquote>
<p>SURPATIENT,THREE</p>
</blockquote></td>
<td><blockquote>
<p>BILATERAL INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>BILATERAL INGUINAL HERNIA, WITH</p>
</blockquote></td>
<td><blockquote>
<p>GANGRENE C</p>
</blockquote></td>
</tr>
<tr class="even">
<td>63066</td>
<td><blockquote>
<p>000-21-2453</p>
<p>GENERAL</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>03/04/02</td>
<td><blockquote>
<p>SURPATIENT,TEN</p>
</blockquote></td>
<td><blockquote>
<p>BILATERAL INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>BILAT INGUINAL HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
</tr>
<tr class="even">
<td>63068</td>
<td><blockquote>
<p>000-12-3456</p>
<p>GENERAL</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>03/08/02</td>
<td><blockquote>
<p>SURPATIENT,EIGHTEEN</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTITIS</p>
</blockquote></td>
<td><blockquote>
<p>CHOLECYSTITIS WITH OBSTRUCTION</p>
</blockquote></td>
<td><blockquote>
<p>C</p>
</blockquote></td>
</tr>
<tr class="even">
<td>63072</td>
<td><blockquote>
<p>000-22-3334</p>
<p>GENERAL</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> WOUND CLASSIFICATION CODES:

> C: CLEAN, CC: CLEAN/CONTAMINATED, D: CONTAMINATED, I: INFECTED

> Delay and Cancellation Reports

### \[SRO DEL MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Delay and Cancellation Reports* menu provides access to various reports used to track delays and cancellations. The reports on this menu are listed below. To the left of the option/report name is the shortcut synonym the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Delayed Operations</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Delay Reasons</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>T</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Delay Time</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Cancellations</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>A</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Cancellation Rates</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Report of Delayed Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SRODELA\]

> The *Report of Delayed Operations* option will list all cases that have been delayed within a specified date range. The report sorts by surgical service and includes both the delay cause and delay time.

> This report is in a 132-column format and should be copied to a printer with wide paper.

> Example: Report of Delayed Operations

> Select Delay and Cancellation Reports Option: D Report of Delayed Operations

> *report follows*

> MAYBERRY, NC PAGE: 1

> SURGICAL SERVICE REVIEWED BY: REPORT OF DELAYED OPERATIONS DATE REVIEWED:

> NEUROSURGERY

> FROM: JUL 1,1999 TO: JUL 31,1999 DATE PRINTED: AUG 13,1999

> ==================================================================================================================================== OPERATING SURGEON NOT PRESENT

> 07/13/99 SURPATIENT,SEVENTEEN SURSURGEON,THREE

> 30 MINS. 000-45-5119 L3-4 LUMBAR LAMINECTOMY WITH PARTIAL FACETECTOMY AND LEFT NEUROFORAMINOTOMY, ADDITIONAL L4-5

> STAFF SURGEON NOT PRESENT

> 07/28/99 SURPATIENT,SIXTY SURSURGEON,TWO WEDNESDAY UNIVERSITY MEETING

> 45 MINS. 000-56-7821 RT. MEDIAN NERVE DECOMPRESSION AT WRIST

### Report of Delay Reasons

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SROREAS\]

> The *Report of Delay Reasons* option lists reasons for delays, and the number of occurrences for delayed operations, within a specified date range.

> This report is in an 80-column format and can be viewed on your screen.

> Example: Report of Delay Reasons

> Select Delay and Cancellation Reports Option: R Report of Delay Reasons

> *printout follows*

> REPORT OF DELAY REASONS FROM 03/01/99 TO 03/31/99

> GENERAL(OR WHEN NOT DEFINED BELOW)

> ANESTHETIST NOT PRESENT 1

> SPECIAL EQUIPMENT NOT READY 1

> OTHER 1

> TOTAL DELAYS FOR GENERAL(OR WHEN NOT DEFINED BELOW) 3

> OTORHINOLARYNGOLOGY (ENT)

> OPERATING SURGEON NOT PRESENT 1

> TOTAL DELAYS FOR OTORHINOLARYNGOLOGY (ENT) 1

> Press RETURN to continue, or '^' to quit: \<Enter\>

> REPORT OF DELAY REASONS FROM 03/01/99 TO 03/31/99

> ================================================================================

> OPERATING SURGEON NOT PRESENT 1

> ANESTHETIST NOT PRESENT 1

> SPECIAL EQUIPMENT NOT READY 1

> OTHER 1

> TOTAL DELAY REASONS 4

> Press RETURN to continue \<Enter\>

### Report of Delay Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SRO DELAY TIME\]

> The *Report of Delay Time* option provides the total amount of delay time for each delay reason for a specified date range. The report sorts by surgical specialty.

> This report is in an 80-column format and can be viewed on a screen.

> Example: Report of Delay Time

> Select Delay and Cancellation Reports Option: T Report of Delay Time

> *printout follows*

> MAYBERRY, NC PAGE 1

> Report of Delay Times From 03/01/99 To 03/31/99

\# OF MINUTES

SURGICAL SPECIALTY DELAYS DELAYED

> ================================================================================

> \>\> Delay Reason: OPERATING SURGEON NOT PRESENT \<\< OTORHINOLARYNGOLOGY (ENT) 1 15

> \>\> Delay Reason: ANESTHETIST NOT PRESENT \<\< GENERAL(OR WHEN NOT DEFINED BE 1 30

> \>\> Delay Reason: SPECIAL EQUIPMENT NOT READY \<\< GENERAL(OR WHEN NOT DEFINED BE 1 10

> Press RETURN to continue, or '^' to quit. \<Enter\>

> MAYBERRY, NC PAGE 2

> Report of Delay Times From 03/01/99 To 03/31/99

\# OF MINUTES

SURGICAL SPECIALTY DELAYS DELAYED

> ================================================================================

> \>\> Delay Reason: OTHER \<\< GENERAL(OR WHEN NOT DEFINED BE 1 15

> Press RETURN to continue, or '^' to quit. \<Enter\>

> MAYBERRY, NC PAGE 3

> Report of Delay Times From 03/01/99 To 03/31/99

\# OF MINUTES

DELAY REASON DELAYS DELAYED

> ================================================================================

> TOTAL 4 70

> Press RETURN to continue \<Enter\>

### Report of Cancellations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SROCAN\]

> The *Report of Cancellations* option is designed to provide information for cases that have been scheduled and cancelled.

> This report is in a 132-column format and must be copied to a printer.

> Example: Print Report of Cancellations

> Select Delay and Cancellation Reports Option: C Report of Cancellations

> *printout follows*

> MAYBERRY, NC PAGE: 1

> REPORT OF CANCELLATIONS REVIEWED BY:

> PRINTED: MAR 23, 1999 FROM 03/01/99 TO 03/03/99 DATE REVIEWED:

> DATE PATIENT OPERATION(S) CANCEL DATE

> CASE \# ID# PRIMARY REASON

> ====================================================================================================================================

> \>\> SURGICAL SPECIALTY: OPHTHALMOLOGY \<\<

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 20%" />
<col style="width: 44%" />
<col style="width: 15%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MAR 01, 1999</p>
<p>31725</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,FIVE 000-58-7963</p>
</blockquote></th>
<th><blockquote>
<p>* PHACEOMULSIFICATION, LENS IMPLANT OS</p>
</blockquote></th>
<th><blockquote>
<p>MAR 01, 1999 MEDICAL</p>
</blockquote></th>
<th><blockquote>
<p>11:00</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>&gt;&gt; SURGICAL SPECIALTY: ORTHOPEDICS &lt;&lt;</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAR 01, 1999</p>
<p>32066</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIVE 000-58-7963</p>
</blockquote></td>
<td><blockquote>
<p>LT. TOTAL KNEE ARTHROPLASTY</p>
</blockquote></td>
<td><blockquote>
<p>MAR 01, 1999 MEDICAL</p>
</blockquote></td>
<td><blockquote>
<p>08:01</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAR 03, 1999</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,THREE</p>
</blockquote></td>
<td><blockquote>
<p>HARDWARE REMOVAL RT. ANKLE</p>
</blockquote></td>
<td><blockquote>
<p>MAR 03, 1999</p>
</blockquote></td>
<td><blockquote>
<p>12:49</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 32143 000-21-2453 ADMINISTRATIVE CANCELLATION

> \>\> SURGICAL SPECIALTY: PLASTIC SURGERY (INCLUDES HEAD AND NECK) \<\<

> MAR 01, 1999 SURPATIENT,TEN DEBRIDMENT OF BACK, NECK WOUNDS, GOLDWEIGHT TO MAR 01, 1999 07:36 32089 000-12-3456 RT. EYE, RT. LATERAL CANTHOPLASTY SURGEON

> MAR 03, 1999 SURPATIENT,TEN PRIMARY CLOSURE LT. CHEEK, SKIN GRAFT VS SKIN APR 02, 1999 08:21

> 32141 000-12-3456 FLAP PATIENT NOT NPO

> \>\> SURGICAL SPECIALTY: THORACIC SURGERY (INC. CARDIAC SURG.) \<\<

> MAR 01, 1999 SURPATIENT,FORTY LT. THORACOTOMY, LOBECTOMY, PNEUMONECTOMY MAR 01, 1999 07:35

> 32013 000-77-7777 MEDICAL

> \>\> SURGICAL SPECIALTY: UROLOGY \<\<

> MAR 03, 1999 SURPATIENT,NINETEEN TRANSURETHRAL RESECTION OF BLADDER TUMOR MAR 19, 1999 08:00

> 32119 000-28-7354 PATIENT/GUARDIAN REFUSES

> \>\> SURGICAL SPECIALTY: PODIATRY \<\<

> MAR 02, 1999 SURPATIENT,SEVENTEEN 1ST METATARSL REMODELING RT. FOOT, REMOVAL OF MAR 29, 1999 08:52 31865 000-45-5119 SOFT TISSUE NODULE RT. FOOT MEDICAL

### Report of Cancellation Rates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SROCRAT\]

> The *Report of Cancellation Rates* option generates a report on the calculations of cancellation rates. This report can be printed for one or a few surgical specialties (Example 1), or for all surgical specialties (Example 2). Emergency cases are not included in this report.

> This report is in an 80-column format and can be viewed on your screen.

> How the Cancellation Rates Are Calculated

> Cancellation Rate for Scheduled Cases = (Total Cancels / Total Scheduled) x 100

> Avoidable Cancellation Rate for Scheduled Cases = (Total Avoidable Cancels / Total Scheduled) x 100

> Avoidable Cancellation rate for all Cancelled Cases = (Total Avoidable Cancels / Total Cancels) x 100

> Example 1: View for Individual Surgical Specialties

> Select Delay and Cancellation Reports Option: A Report of Cancellation Rates

> *printout follows*

> \*\* GENERAL(OR WHEN NOT DEFINED BELOW) \*\*

> TOTAL SCHEDULED SURGICAL CASES: 18 CANCELLATION RATE FOR SCHEDULED CASES: 17 %

> AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 0 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 0 %

> PRIMARY CANCELLATION REASON TOTAL CANCELS TOTAL AVOIDABLE PREV. CASE LENGTH 3 0

> TOTAL CANCELLATIONS 3 0

> Press RETURN to continue, or '^' to quit: \<Enter\>

> \*\* ORTHOPEDICS \*\* TOTAL SCHEDULED SURGICAL CASES: 23

> CANCELLATION RATE FOR SCHEDULED CASES: 26 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 9 %

> AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 33 %

<table style="width:100%;">
<colgroup>
<col style="width: 54%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 2%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>PRIMARY CANCELLATION REASON</th>
<th></th>
<th><blockquote>
<p>TOTAL CANCELS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>TOTAL AVOIDABLE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADMINISTRATIVE CANCELLATION</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>MEDICAL</td>
<td>4</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>SCHEDULING ERROR</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>TOTAL CANCELLATIONS</td>
<td>6</td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue, or '^' to quit: \<Enter\>

> \*\* PLASTIC SURGERY (INCLUDES HEAD AND NECK) \*\* TOTAL SCHEDULED SURGICAL CASES: 10

> CANCELLATION RATE FOR SCHEDULED CASES: 30 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 20 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 67 %

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PRIMARY CANCELLATION REASON</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TOTAL CANCELS</p>
</blockquote></th>
<th><blockquote>
<p>TOTAL AVOIDABLE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PATIENT NOT NPO</p>
</blockquote></td>
<td>1</td>
<td colspan="2">1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREV. CASE LENGTH</p>
</blockquote></td>
<td>1</td>
<td colspan="2">0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURGEON</p>
</blockquote></td>
<td>1</td>
<td colspan="2">1</td>
</tr>
<tr class="even">
<td></td>
<td>-----</td>
<td colspan="2"><blockquote>
<p>-----</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL CANCELLATIONS</p>
</blockquote></td>
<td>3</td>
<td colspan="2">2</td>
</tr>
</tbody>
</table>

> Press RETURN to continue, or '^' to quit: \<Enter\>

> Example 2: View for All Specialties

> Select Delay and Cancellation Reports Option: A Report of Cancellation Rates

#### printout follows 

> \*\* GENERAL(OR WHEN NOT DEFINED BELOW) \*\* TOTAL SCHEDULED SURGICAL CASES: 18

> CANCELLATION RATE FOR SCHEDULED CASES: 17 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 0 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 0 %

<table style="width:100%;">
<colgroup>
<col style="width: 54%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 2%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>PRIMARY CANCELLATION REASON</th>
<th></th>
<th><blockquote>
<p>TOTAL CANCELS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>TOTAL AVOIDABLE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PREV. CASE LENGTH</td>
<td>3</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>TOTAL CANCELLATIONS</td>
<td>3</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue, or '^' to quit: \<Enter\>

> \*\* NEUROSURGERY \*\* TOTAL SCHEDULED SURGICAL CASES: 8

> CANCELLATION RATE FOR SCHEDULED CASES: 25 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 13 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 50 %

<table style="width:100%;">
<colgroup>
<col style="width: 57%" />
<col style="width: 2%" />
<col style="width: 16%" />
<col style="width: 2%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>PRIMARY CANCELLATION REASON</th>
<th></th>
<th><blockquote>
<p>TOTAL CANCELS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>TOTAL AVOIDABLE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OPERATING ROOM</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>PATIENT NO-SHOW</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>TOTAL CANCELLATIONS</td>
<td>2</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>Press RETURN to continue, or '^' to quit: <strong>&lt;Enter&gt;</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> \*\* ORTHOPEDICS \*\* TOTAL SCHEDULED SURGICAL CASES: 23

> CANCELLATION RATE FOR SCHEDULED CASES: 26 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 9 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 33 %

<table style="width:100%;">
<colgroup>
<col style="width: 54%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 2%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>PRIMARY CANCELLATION REASON</th>
<th></th>
<th><blockquote>
<p>TOTAL CANCELS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>TOTAL AVOIDABLE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADMINISTRATIVE CANCELLATION</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>MEDICAL</td>
<td>4</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>SCHEDULING ERROR</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>TOTAL CANCELLATIONS</td>
<td>6</td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue, or '^' to quit: \<Enter\>

> \*\* OTORHINOLARYNGOLOGY (ENT) \*\*

> TOTAL SCHEDULED SURGICAL CASES: 18 CANCELLATION RATE FOR SCHEDULED CASES: 6 %

> AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 6 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 100 %

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 2%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>PRIMARY CANCELLATION REASON</th>
<th></th>
<th><blockquote>
<p>TOTAL CANCELS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>TOTAL AVOIDABLE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SCHEDULING ERROR</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>TOTAL CANCELLATIONS</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue, or '^' to quit: \<Enter\>

> \*\* PERIPHERAL VASCULAR \*\* TOTAL SCHEDULED SURGICAL CASES: 16

> CANCELLATION RATE FOR SCHEDULED CASES: 25 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 6 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 25 %

<table style="width:100%;">
<colgroup>
<col style="width: 54%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 2%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>PRIMARY CANCELLATION REASON</th>
<th></th>
<th><blockquote>
<p>TOTAL CANCELS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>TOTAL AVOIDABLE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MEDICAL</td>
<td>2</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>PREV. CASE LENGTH</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>SCHEDULING ERROR</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>TOTAL CANCELLATIONS</td>
<td>4</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue, or '^' to quit: \<Enter\>

> \*\* PLASTIC SURGERY (INCLUDES HEAD AND NECK) \*\* TOTAL SCHEDULED SURGICAL CASES: 10

> CANCELLATION RATE FOR SCHEDULED CASES: 30 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 20 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 67 %

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PRIMARY CANCELLATION REASON</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TOTAL CANCELS</p>
</blockquote></th>
<th><blockquote>
<p>TOTAL AVOIDABLE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PATIENT NOT NPO</p>
</blockquote></td>
<td>1</td>
<td colspan="2">1</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREV. CASE LENGTH</p>
</blockquote></td>
<td>1</td>
<td colspan="2">0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURGEON</p>
</blockquote></td>
<td>1</td>
<td colspan="2">1</td>
</tr>
<tr class="even">
<td></td>
<td>-----</td>
<td colspan="2"><blockquote>
<p>-----</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOTAL CANCELLATIONS</p>
</blockquote></td>
<td>3</td>
<td colspan="2">2</td>
</tr>
</tbody>
</table>

> Press RETURN to continue, or '^' to quit: \<Enter\>

> \*\* PODIATRY \*\* TOTAL SCHEDULED SURGICAL CASES: 14

> CANCELLATION RATE FOR SCHEDULED CASES: 7 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 0 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 0 %

> PRIMARY CANCELLATION REASON TOTAL CANCELS TOTAL AVOIDABLE MEDICAL 1 0

> ----- -----

> TOTAL CANCELLATIONS 1 0

> Press RETURN to continue, or '^' to quit: \<Enter\>

> \*\* UROLOGY \*\*

> TOTAL SCHEDULED SURGICAL CASES: 11

> CANCELLATION RATE FOR SCHEDULED CASES: 18 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 0 % AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 0 %

<table style="width:100%;">
<colgroup>
<col style="width: 54%" />
<col style="width: 5%" />
<col style="width: 16%" />
<col style="width: 2%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>PRIMARY CANCELLATION REASON</th>
<th></th>
<th><blockquote>
<p>TOTAL CANCELS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>TOTAL AVOIDABLE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MEDICAL</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>PATIENT/GUARDIAN REFUSES</td>
<td>1</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td>TOTAL CANCELLATIONS</td>
<td>2</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Press RETURN to continue, or '^' to quit: \<Enter\>

> TOTAL SURGICAL CASES SCHEDULED FOR MAYBERRY, NC: 118 CANCELLATION RATE FOR SCHEDULED CASES: 19 % AVOIDABLE CANCELLATION RATE FOR SCHEDULED CASES: 6 %

> AVOIDABLE CANCELLATION RATE FOR CANCELLED CASES: 32 %

> PRIMARY CANCELLATION REASON TOTAL CANCELS TOTAL AVOIDABLE

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 26%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>ADMINISTRATIVE CANCELLATION</th>
<th>1</th>
<th>1</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MEDICAL</td>
<td>8</td>
<td>1</td>
</tr>
<tr class="even">
<td>OPERATING ROOM</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td>PATIENT NO-SHOW</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="even">
<td>PATIENT NOT NPO</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td>PATIENT/GUARDIAN REFUSES</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="even">
<td>PREV. CASE LENGTH</td>
<td>5</td>
<td>0</td>
</tr>
<tr class="odd">
<td>SCHEDULING ERROR</td>
<td>3</td>
<td>2</td>
</tr>
<tr class="even">
<td>SURGEON</td>
<td>1</td>
<td>1</td>
</tr>
<tr class="odd">
<td></td>
<td>-----</td>
<td><blockquote>
<p>-----</p>
</blockquote></td>
</tr>
<tr class="even">
<td>TOTAL CANCELLATIONS</td>
<td>22</td>
<td>7</td>
</tr>
</tbody>
</table>

> Press RETURN to continue, or '^' to quit: \<Enter\>

> PERCENT AVOIDABLE CANCELLATIONS

> SURGICAL SPECIALTY SCHEDULED CASES CANCELLED CASES

> ================================================================================

<table>
<colgroup>
<col style="width: 60%" />
<col style="width: 21%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW)</p>
</blockquote></th>
<th>0 %</th>
<th>0 %</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NEUROSURGERY</p>
</blockquote></td>
<td>13 %</td>
<td>50 %</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORTHOPEDICS</p>
</blockquote></td>
<td>9 %</td>
<td>33 %</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OTORHINOLARYNGOLOGY (ENT)</p>
</blockquote></td>
<td>6 %</td>
<td>100 %</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PERIPHERAL VASCULAR</p>
</blockquote></td>
<td>6 %</td>
<td>25 %</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PLASTIC SURGERY (INCLUDES HEAD AND NECK)</p>
</blockquote></td>
<td>20 %</td>
<td>67 %</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PODIATRY</p>
</blockquote></td>
<td>0 %</td>
<td>0 %</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UROLOGY</p>
<p>Press RETURN to continue <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
<td>0 %</td>
<td>0 %</td>
</tr>
</tbody>
</table>

> List of Unverified Surgery Cases

### \[SROUNV\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *List of Unverified Surgery Cases* option will generate a list of all completed surgery cases that have not had the procedure, diagnosis, and complications verified. The user can verify a case using the

> *Surgeon's Verification of Diagnosis & Procedures* option in the *Operation Menu*. This list can be compiled for one or all surgical specialties.

> This report is in an 80-column format and can be viewed on your screen.

> Example: List of Unverified Surgery Cases

> Select Management Reports Option: V List of Unverified Surgery Cases

> *printout follows*

> List of Unverified Cases for GENERAL(OR WHEN NOT DEFINED BELOW)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 42%" />
<col style="width: 8%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Operation Date</p>
</blockquote></th>
<th><blockquote>
<p>Patient (Case #)</p>
<p>Patient ID #</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>Surgeon</p>
<p>Attending Surgeon</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>================================================================================</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAR 9, 1999</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIX (15188)</p>
<p>000-09-8797</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURSURGEON,SIXTEEN SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>APPENDECTOMY * CPT CODE MISSING</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>*</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAR 10, 1999</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTYONE (15189)</p>
<p>000-23-3221</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURSURGEON,FOUR SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>DRAINAGE OF OVARIAN CYST * CPT CODE MISSING *</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAR 10, 1999</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWO (15199)</p>
<p>000-45-1982</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURSURGEON,ONE NOT ENTERED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>CHOLECYSTECTOMY WITH CHOLANGIOGRAM * CPT CODE MISSING *</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAR 17, 1999</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURPATIENT,FOURTEEN (15203)</p>
<p>000-45-7212</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>CHOLECYSTECTOMY * CPT CODE MISSING *</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAR 18, 1999</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURPATIENT,SEVENTEEN (15202)</p>
<p>000-45-5119</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> REPAIR INCARCERATED INGUINAL HERNIA \* CPT CODE MISSING \*

> Press RETURN to continue, or '^' to quit:. \<Enter\>

> Report of Returns to Surgery

### \[SRORET\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of Returns to Surgery* option lists cases that have had related surgical procedures performed within 30 days of the date of the operation. The user must enter the date range by which the software will sort.

> This report has a 132-column format and must be copied to a printer with wide paper.

> Example: Print the Report of Returns to Surgery

> Select Management Reports Option: RET Report of Returns to Surgery

> *printout follows*

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY: REPORT OF RETURNS TO SURGERY DATE REVIEWED:

> FROM: JUL 1,1999 TO: JUL 14,1999 DATE PRINTED: AUG 27,1999

> OPERATION DATE PATIENT (ID#) PRINCIPAL OPERATIVE PROCEDURE

> ====================================================================================================================================

> JUL 03, 1999 SURPATIENT,SEVENTEEN (000-45-5119) REPAIR GASTRIC PERFORATION RETURNS TO SURGERY:

> JUL 07, 1999 EXPLORATORY LAPAROTOMY

> JUL 06, 1999 SURPATIENT,FIVE (000-21-2453) ATTEMPTED REVISION OF LEFT ARM A-V FISTULA WITH GRAFT RETURNS TO SURGERY:

> JUL 15, 1999 CREATION OF A-V FISTULA W/VASCULAR GRAFT, RT ARM

> JUL 06, 1999 SURPATIENT,TWO (000-45-1982) EXCISION OF GRANULATION TISSUE RT. FOOT RETURNS TO SURGERY:

> AUG 03, 1999 STSG FROM RT. THIGH TO RIGHT FOOT

> JUL 06, 1999 SURPATIENT,FORTY (000-77-7777) IRRIGATION AND DEBRIDEMENT OF LT. FOOT RETURNS TO SURGERY:

> JUL 14, 1999 IRRIGATION AND DEBRIDEMENT OF LT. FOOT

> JUL 07, 1999 SURPATIENT,FORTYONE (000-43-2109) EXPLORATORY LAPAROTOMY RETURNS TO SURGERY:

> AUG 05, 1999 TRACHEOSTOMY

> JUL 10, 1999 SURPATIENT,ONE (000-44-7629) RIGHT LOWER QUADRANT EXPLORATION RETURNS TO SURGERY:

> JUL 13, 1999 SIGMOID COLECTOMY

> Report of Daily Operating Room Activity

### \[SROPACT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of Daily Operating Room Activity* option provides a list of completed cases started between 6:00 AM on the date selected and 5:59 AM of the following day for all operating rooms.

> Example: Print the Report of Daily Operating Room Activity

> Select Management Reports Option: A Report of Daily Operating Room Activity

> *printout follows*

> MAYBERRY, NC SURGICAL SERVICE

> DAILY REPORT OF OPERATING ROOM ACTIVITY FOR: JUL 01, 1999

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 20%" />
<col style="width: 31%" />
<col style="width: 27%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th>TIME IN OR</th>
<th><blockquote>
<p>POSTOPERATIVE DIAGNOSIS</p>
</blockquote></th>
<th>ANESTHESIOLOGIST</th>
<th><blockquote>
<p>SURGEON</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>ID #</p>
</blockquote></td>
<td>AGE TIME OUT OR</td>
<td><blockquote>
<p>PROCEDURE(S)</p>
</blockquote></td>
<td>PRIN. ANESTHETIST</td>
<td><blockquote>
<p>FIRST ASST.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>WARD</p>
</blockquote></td>
<td>CASE NUMBER</td>
<td></td>
<td></td>
<td><blockquote>
<p>ATT SURGEON</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 40%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OPERATING ROOM: CYSTO1</p>
</blockquote></th>
<th colspan="4"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,SIX</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>14:00</p>
</blockquote></td>
<td><blockquote>
<p>GROSS HEMATURIA</p>
</blockquote></td>
<td>SURSANESTHESIOLOGIST,O SURSURGEON,F</td>
</tr>
<tr class="even">
<td><blockquote>
<p>000-09-8797 69</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>16:05</p>
</blockquote></td>
<td><blockquote>
<p>CYSTOURETHROSCOPY WITH BLADDER BIOPSY,</p>
</blockquote></td>
<td><blockquote>
<p>SURANESTHETIST,F</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OUTPATIENT</p>
</blockquote></td>
<td>33536</td>
<td></td>
<td><blockquote>
<p>TRANSURETHRAL RESECTION OF BLADDER TUMOR</p>
</blockquote></td>
<td>SURSURGEON,O</td>
</tr>
<tr class="even">
<td><blockquote>
<p>OPERATING ROOM: OR1</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SURPATIENT,NINETEEN</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>08:00</p>
</blockquote></td>
<td><blockquote>
<p>LEFT COLD FOOT</p>
</blockquote></td>
<td>SURSANESTHESIOLOGIST,O SURSURGEON,T</td>
</tr>
<tr class="even">
<td><blockquote>
<p>000-28-7354 59</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>16:30</p>
</blockquote></td>
<td><blockquote>
<p>LEFT FEMORO-TIB TO TIB PERONEAL TRUNK</p>
</blockquote></td>
<td>SURANESTHETIST,F SURSURGEON,F</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OUTPATIENT</p>
</blockquote></td>
<td>33512</td>
<td></td>
<td><blockquote>
<p>SAPHENOUS,IN-SITU, TIBIAL-PERONEAL EMBOLECTOMY, EXCLUSION OF POPLITEAL ANEURYSM, COMPLETION ANGIOGRAPHY, COMPLETION DUPLEX</p>
</blockquote></td>
<td>SURSURGEON,O</td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>09:10</p>
</blockquote></td>
<td><blockquote>
<p>RT. CAROTID STENOSIS</p>
</blockquote></td>
<td>SURSANESTHESIOLOGIST,T SURSURGEON,F</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>000-45-5119 73</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>13:00</p>
</blockquote></td>
<td><blockquote>
<p>RT. CAROTID ENDARTERECTOMY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OUTPATIENT</p>
</blockquote></td>
<td>33521</td>
<td></td>
<td></td>
<td>SURSURGEON,S</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OPERATING ROOM: OR2</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,TEN</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>06:00</p>
</blockquote></td>
<td><blockquote>
<p>APPENDICITIS</p>
</blockquote></td>
<td>SURSANESTHESIOLOGIST,O SURSURGEON,F</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>000-12-3456 60</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>07:35</p>
</blockquote></td>
<td><blockquote>
<p>APPENDECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>SURSANESTHESIOLOGIST,O</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OUTPATIENT</p>
</blockquote></td>
<td>33519</td>
<td></td>
<td></td>
<td>SURSURGEON,S</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OPERATING ROOM: OR4</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,FIVE</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>07:45</p>
</blockquote></td>
<td><blockquote>
<p>RT. EAR,RT. EYELID BASAL CELL CA</p>
</blockquote></td>
<td><blockquote>
<p>SURSANESTHESIOLOGIST,O SURSURGEON,S</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>000-58-7963 75</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>12:00</p>
</blockquote></td>
<td><blockquote>
<p>EXCISION OF RT. UPPER EYELID BASAL CELL CA,</p>
</blockquote></td>
<td><blockquote>
<p>SURSANESTHESIOLOGIST,O</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OUTPATIENT</p>
</blockquote></td>
<td>33409</td>
<td></td>
<td><blockquote>
<p>EXCISION OF RT. EAR BASAL CELL CA</p>
</blockquote></td>
<td>SURSURGEON,F</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OPERATING ROOM: OR5</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SURPATIENT,SIXTEEN</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>07:50</p>
</blockquote></td>
<td><blockquote>
<p>SINUSITIS ,RHNOPHYMA,NASAL OBSTRUCTION</p>
</blockquote></td>
<td>SURSANESTHESIOLOGIST,O SURSURGEON,F</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>000-11-1111 96</p>
</blockquote></td>
<td>07/01</td>
<td><blockquote>
<p>10:27</p>
</blockquote></td>
<td><blockquote>
<p>SEPTOPLASTY, TURBINECTOMY, INTERNAL INTRA NASAL</p>
</blockquote></td>
<td><blockquote>
<p>SURSANESTHESIOLOGIST,O</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OUTPATIENT</p>
</blockquote></td>
<td>33399</td>
<td></td>
<td><blockquote>
<p>SYNOIDECTOMY, LASER RESURFACE OF NOSE, NASAL</p>
<p>POLYECTOMY RT., NASAL POLYPECTOMY LT.</p>
</blockquote></td>
<td>SURSURGEON,S</td>
</tr>
</tbody>
</table>

> Report of Cases Without Specimens

### \[SROSPEC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of Cases Without Specimens* option lists all completed cases in which there were no specimens taken from the operative site. The report can be printed for an individual surgical specialty, if it is needed.

> This report is in a 132-column format and must be copied to a printer with wide paper.

> Example: Print the Report of Cases without Specimens

> Select Management Reports Option: NS Report of Cases Without Specimens

> *printout follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE REVIEWED BY: CASES WITHOUT SPECIMENS DATE REVIEWED:

> FROM: JUL 12,1999 TO: JUL 14,1999 DATE PRINTED: JUL 27,1999

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 23%" />
<col style="width: 40%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>SURGICAL SPECIALTY</p>
</blockquote></th>
<th><blockquote>
<p>PRIMARY SURGEON</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ID</p>
</blockquote></td>
<td><blockquote>
<p>POSTOPERATIVE DIAGNOSIS</p>
</blockquote></td>
<td><blockquote>
<p>ATTENDING SURGEON</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>OPERATIVE PROCEDURE</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 22%" />
<col style="width: 46%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>07/12/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,TEN</p>
</blockquote></th>
<th><blockquote>
<p>PERIPHERAL VASCULAR</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,THREE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>33613</p>
</blockquote></td>
<td><blockquote>
<p>000-12-3456</p>
</blockquote></td>
<td><blockquote>
<p>RENAL FAILURE</p>
<p>PLACEMENT OF LEFT FEMORAL DIALYSIS TESSIO-CATHETER</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/12/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOUR</p>
</blockquote></td>
<td><blockquote>
<p>OTORHINOLARYNGOLOGY (ENT)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33616</p>
</blockquote></td>
<td><blockquote>
<p>000-17-0555</p>
</blockquote></td>
<td><blockquote>
<p>NASAL OBSTRUCTION</p>
<p>LEFT LATERAL RHINOTOMY WITH RECONSTRUCTION OF NASAL VESTIBULE</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/12/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTEEN</p>
</blockquote></td>
<td><blockquote>
<p>UROLOGY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33659</p>
</blockquote></td>
<td><blockquote>
<p>000-11-1111</p>
</blockquote></td>
<td><blockquote>
<p>SIGMOID CA</p>
<p>CYSTOURETOROSCOPY, RETROGRADE PYELOGRAPHY, BILATERAL URETERAL STENT PLACEMENT</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/12/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SEVENTEEN</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33653</p>
</blockquote></td>
<td><blockquote>
<p>000-45-5119</p>
</blockquote></td>
<td><blockquote>
<p>PROLONGED ANTIBOTIC THERAPHY PLACEMENT OF HICKMAN CATHETER</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,SEVEN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/13/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTY</p>
</blockquote></td>
<td><blockquote>
<p>OPHTHALMOLOGY</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33554</p>
</blockquote></td>
<td><blockquote>
<p>000-45-9999</p>
</blockquote></td>
<td><blockquote>
<p>CATARACT OS</p>
<p>PHACEOMULSIFICATION, LENS IMPLANT OS</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/14/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TEN</p>
</blockquote></td>
<td><blockquote>
<p>PLASTIC SURGERY (INCLUDES HEAD AND NECK)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33598</p>
</blockquote></td>
<td><blockquote>
<p>000-12-3456</p>
</blockquote></td>
<td><blockquote>
<p>MOH'S DEFECT LT. UPPER LIP</p>
<p>FLAP CLOSURE OF MOHS DEFECT LEFT UPPER LIP</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/14/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,EIGHTEEN</p>
</blockquote></td>
<td><blockquote>
<p>PLASTIC SURGERY (INCLUDES HEAD AND NECK)</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,SIX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33645</p>
</blockquote></td>
<td><blockquote>
<p>000-22-3334</p>
</blockquote></td>
<td><blockquote>
<p>INFECTED DIABETIC FOOT</p>
<p>DEBRIDEMENT RIGHT FOOT, SKIN GRAFT RT THIGH TO RT FOOT</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL CASES WITHOUT</p>
</blockquote></td>
<td><blockquote>
<p>SPECIMENS: 7</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Report of Unscheduled Admissions to ICU

### \[SROICU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of Unscheduled Admissions to ICU* option lists all unscheduled admissions to the Intensive Care Unit (ICU) based on the requested (expected) postoperative care and actual postoperative disposition.

> This report is in a 132-column format and must be copied to a printer with wide paper.

> Example: Print Report of Unscheduled Admissions to ICU

> Select Management Reports Option: ICU Report of Unscheduled Admissions to ICU

> *printout follows*

> MAYBERRY, NC

> SURGICAL SERVICE REVIEWED BY: UNSCHEDULED ADMISSIONS TO ICU DATE REVIEWED:

> FROM 07/01/99 TO 07/31/99

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 33%" />
<col style="width: 32%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>SURGICAL SPECIALTY</p>
</blockquote></th>
<th><blockquote>
<p>PRIMARY SURGEON</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>PATIENT ID</p>
</blockquote></td>
<td><blockquote>
<p>POSTOPERATIVE DIAGNOSIS</p>
</blockquote></td>
<td><blockquote>
<p>ATTENDING SURGEON</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>REQ DISPOSITION/POSTOP DISPOSITION</p>
</blockquote></td>
<td><blockquote>
<p>OPERATIVE PROCEDURE(S)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 28%" />
<col style="width: 44%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>07/01/99</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,EIGHTEEN 000-22-3334</p>
<p>PACU (RECOVERY ROOM)/SICU</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW) APPENDICITIS</p>
<p>APPENDECTOMY</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,ONE SURSURGEON,THREE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>07/06/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TEN 000-12-3456 WARD/SICU</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW) INABILITY TO TAKE ORAL OR USE NG TUBE PLACEMENT OF G-TUBE</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/08/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWELVE 000-41-8719 WARD/MICU</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW) GANGRENE LT. FOOT</p>
<p>LT. BELOW KNEE AMPUTATION</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,THREE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>07/23/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TEN 000-12-3456 WARD/SICU</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERAL VASCULAR IV ACCESS</p>
<p>PLACEMENT OF HICKMAN CATHATER, INTRODUCTION OF DOBHOFF TUBE</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,FOUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>07/27/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FORTY 000-77-7777 WARD/MICU</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW) RT BUTTOCK ABCESS</p>
<p>I AND D OF RIGHT BUTTOCK ABSCESS</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>07/29/99</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FOUR 000-17-0555</p>
<p>WARD/MICU</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW) INCARCERATED EPIGASTRIC HERNIA</p>
<p>REPAIR OF INCARCERATED EPIGASTRIC HERNIA</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,ONE SURSURGEON,TWO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Operating Room Utilization Report

### \[SR OR UTL1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operating Room Utilization Report* option prints utilization information for a selected date range for all operating rooms or for a single operating room. The report displays the percent utilization, the number of cases, the total operation time and the time worked outside normal hours for each operating room individually and all operating rooms collectively.

> How the Percent Utilization is Derived

> The percent utilization is derived by dividing the total operation time for all operations (including total time patients were in OR, plus the cleanup time allowed for each case) by the total functioning time, as defined in the SURGERY UTILIZATION file. The quotient is then multiplied by 100.

> This report must be copied to a printer with wide paper

> Example: Print the Operating Room Utilization Report

> Select Management Reports Option: OR Operating Room Utilization Report

> *printout follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE OPERATING ROOM UTILIZATION REPORT

> FOR ALL OPERATING ROOMS FROM: MAR 8,1999 TO: MAR 9,1999 DATE PRINTED: MAR 17,1999

> ====================================================================================================================================

> OPERATING ROOM PERCENT UTILIZATION NUMBER OF CASES TOTAL OPERATION TIME TIME WORKED OUTSIDE NORMAL HRS

> (INCLUDING OR MAINTENANCE)

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>OR1</th>
<th><blockquote>
<p>70%</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>17 hrs and 35 mins</p>
</blockquote></th>
<th><blockquote>
<p>6 hrs and 20 mins</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR2</td>
<td><blockquote>
<p>39%</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>7 hrs and 25 mins</p>
</blockquote></td>
<td><blockquote>
<p>1 hr and 10 mins</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OR3</td>
<td><blockquote>
<p>133%</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>23 hrs and 42 mins</p>
</blockquote></td>
<td><blockquote>
<p>2 hrs and 30 mins</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OR4</td>
<td><blockquote>
<p>29%</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>4 hrs and 41 mins</p>
</blockquote></td>
<td>-</td>
</tr>
<tr class="even">
<td>OR5</td>
<td><blockquote>
<p>84%</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>18 hrs and 50 mins</p>
</blockquote></td>
<td><blockquote>
<p>5 hrs and 25 mins</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OR6</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td>OR7</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td>TOTAL UTILIZATION FOR ALL ROOMS</td>
<td><blockquote>
<p>63%</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>72 hrs and 13 mins</p>
</blockquote></td>
<td><blockquote>
<p>15 hrs and 25 mins</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> Wound Classification Report

### \[SROWC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Wound Classification Report* option generates a report showing the total number of surgical cases in each of the various wound classifications for a specified date range. The report is sorted by surgical service.

> After selecting a date range, the user has the choice of printing one of three reports.

- Wound Classification Report: The user enters the number 1 to print this summary of wound classifications entered for surgical cases performed during the date range.
- List of Operations by Wound Classification: The user enters the number 2 to print this list of operations sorted by wound classification and by surgical specialty performed during the date range.
- Clean Wound Infection Summary: The user enters the number 3 to print this summary of clean wound infections.

> These reports are in an 80-column format and can be viewed on the screen.

> Example 1: Wound Classification Report (Summary)

> Select Management Reports Option: WC Wound Classification Report

> *printout follows*

> WOUND CLASSIFICATION REPORT FROM: JUL 1,1999 TO: JUL 15,1999

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 11%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 13%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURGICAL SERVICE</p>
</blockquote></th>
<th>CLEAN</th>
<th><blockquote>
<p>CLEAN CONTAMINATED</p>
</blockquote></th>
<th><blockquote>
<p>CONTAMINATED</p>
</blockquote></th>
<th><blockquote>
<p>INFECTED</p>
</blockquote></th>
<th><blockquote>
<p>NO CLASS ENTERED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
<td>9</td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORTHOPEDICS</p>
</blockquote></td>
<td>9</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SUB TOTAL:</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td>4</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL: 35</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> CLEAN WOUND INFECTION RATE: 0.0%

> Press RETURN to continue \<Enter\>

> Example 2: List of Operations by Wound Classification

> Select Management Reports Option: WC Wound Classification Report

#### printout follows 

> List of Surgical Cases by Wound Classification Page: FROM: JUL 8,1999 TO: JUL 8,1999 1

> Wound Classification: CLEAN

> DATE PRINTED: JUL 27,1999

> Operation Date Patient Surgeon/Provider Case \# ID \#

> ==============================================================================

> \>\> GENERAL(OR WHEN NOT DEFINED BELOW) \<\<

> JUL 08, 1999 SURPATIENT,TEN SURSURGEON,ONE

> 33280 000-12-3456

- RT. INGUINAL HERNIA REPAIR

> JUL 08, 1999 SURPATIENT,FOUR SURSURGEON,FOUR

> 33629 000-17-0555

- INCARCERATED UMBILICAL HERNIA REPAIR

> Press RETURN to continue, or '^' to quit: \<Enter\>

> List of Surgical Cases by Wound Classification Page: FROM: JUL 8,1999 TO: JUL 8,1999 2

> Wound Classification: CLEAN

> DATE PRINTED: JUL 27,1999

> Operation Date Patient Surgeon/Provider Case \# ID \#

> ==============================================================================

> \>\> PERIPHERAL VASCULAR \<\<

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 42%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><p>JUL 08, 1999</p>
<p>33478</p></th>
<th><blockquote>
<p>SURPATIENT,FORTY 000-77-7777</p>
</blockquote>
<ul>
<li><p>LEFT CAROTID ENDARTERECTOMY</p></li>
<li><p>REOPERATION LEFT CAROTID</p></li>
</ul></th>
<th><blockquote>
<p>SURSURGEON,ONE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>JUL 08, 1999</p>
<p>33575</p></td>
<td><blockquote>
<p>SURPATIENT,TWO 000-45-1982</p>
</blockquote></td>
<td><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></td>
</tr>
</tbody>
</table>

- LT. A-V FISTULA WITH LOOP VEIN GRAFT

> Press RETURN to continue \<Enter\>

> Example 3: Clean Wound Infection Summary

> Select Management Reports Option: WC Wound Classification Report

#### ----------------------------------------------------------printout follows----------------------------------------------

> MAYBERRY, NC SURGICAL SERVICE

> CLEAN WOUND INFECTION SUMMARY FROM: JUN 1,1999 TO: JUN 30,1999 DATE PRINTED: JUL 18,1999

REVIEWED BY: DATE REVIEWED:

> SURGICAL SERVICE CLEAN WOUNDS INFECTIONS INFECTION RATE

> ==============================================================================

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 21%" />
<col style="width: 22%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th>21</th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th>4.8%</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GYNECOLOGY</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NEUROSURGERY</p>
</blockquote></td>
<td>11</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OPHTHALMOLOGY</p>
</blockquote></td>
<td>30</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORTHOPEDICS</p>
</blockquote></td>
<td>20</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td>5.0%</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OTORHINOLARYNGOLOGY</p>
</blockquote></td>
<td>6</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PLASTIC SURGERY</p>
</blockquote></td>
<td>7</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PROCTOLOGY</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>THORACIC SURGERY</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UROLOGY</p>
</blockquote></td>
<td>2</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORAL SURGERY</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PODIATRY</p>
</blockquote></td>
<td>14</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PERIPHERAL VASCULAR</p>
</blockquote></td>
<td>28</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CARDIAC SURGERY</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TRANSPLANTATION</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ANESTHESIOLOGY</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>RHEUMATOLOGY</p>
</blockquote></td>
<td>1</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PULMONARY</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>GASTROENTEROLOGY</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NO SPECIALTY ENTERED</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>0.0%</td>
</tr>
<tr class="even">
<td><blockquote>
<p>TOTAL</p>
</blockquote></td>
<td>142</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td>1.4%</td>
</tr>
</tbody>
</table>

> Pages 368-392 have been deleted. The Quarterly Report Menus have been removed.

> Print Blood Product Verification Audit Log

### \[SR BLOOD PRODUCT VERIFY AUDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Blood Product Verification Audit Log* option is used to print the KERNEL audit log for the *Blood Product Verification* option.

> Prior to printing entries from the KERNEL audit log for the *Blood Product Verification* option (located on the *Operation Menu*), the audit function must be turned on either through the *System Manager Menu* option or by invoking the *Establish System Audit Parameters* option in KERNEL, as shown in the following example.

> Example: Establish System Audit Parameters

> Example: Print Blood Product Verification Audit Log

> Select Management Reports Option: BA Print Blood Product Verification Audit Log

> *printout follows*

> MENU OPTION AUDIT LOG APR 2,1999 3:04 PM PAGE 1

> \*\*\* OPTION: SR BLOOD PRODUCT VERIFICATION USER: SURSURGEON,TWO

> DATE/TIME (ENTRY): MAR 5,1999 09:24 (EXIT): MAR 5,1999 09:24 CPU: VAA DEVICE: \_LTA8720: JOB: 541070010

> \*\*\* OPTION: SR BLOOD PRODUCT VERIFICATION USER: SURSURGEON,SIX

> DATE/TIME (ENTRY): MAR 5,1999 09:24 (EXIT): MAR 5,1999 09:24 CPU: VAA DEVICE: \_LTA8720: JOB: 541070010

> \*\*\* OPTION: SR BLOOD PRODUCT VERIFICATION USER: SURSURGEON,ONE

> DATE/TIME (ENTRY): MAR 6,1999 13:06 (EXIT): MAR 6,1999 13:07 CPU: VAA DEVICE: \_LTA1411: JOB: 541072157

> \*\*\* OPTION: SR BLOOD PRODUCT VERIFICATION USER: SURSURGEON,ONE

> DATE/TIME (ENTRY): MAR 6,1999 13:10 (EXIT): MAR 6,1999 13:11 CPU: VAA DEVICE: \_LTA1411: JOB: 541072157

> \*\*\* OPTION: SR BLOOD PRODUCT VERIFICATION USER: SURSURGEON,ONE

> DATE/TIME (ENTRY): MAR 6,1999 13:20 (EXIT): MAR 6,1999 13:20 CPU: VAA DEVICE: \_LTA1411: JOB: 541072157

> Key Missing Surgical Package Data

### \[SROQ MISSING DATA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Key Missing Surgical Package Data* option generates a list of surgical cases performed within the selected date range that are missing key information. This report includes surgical cases with an entry in the TIME PAT IN OR field and does not include aborted cases.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: Key Missing Surgical Package Data

> Select Management Reports Option: KEY Key Missing Surgical Package Data

> *printout follows*

#### 394a Surgery V. 3.0 User Manual November

> MAYBERRY, NC

> Report of Key Missing Surgical Package Data PAGE 1

> From: APR 1,2005 To: APR 30,2005

> Report Printed: MAY 11,2005@15:09

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 24%" />
<col style="width: 34%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DATE OF OPERATION</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT NAME</p>
</blockquote></th>
<th><blockquote>
<p>SURGICAL SPECIALTY</p>
</blockquote></th>
<th><blockquote>
<p>MISSING ITEMS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ID (AGE)</p>
</blockquote></td>
<td><blockquote>
<p>PRINCIPAL PROCEDURE</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 28%" />
<col style="width: 47%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>APR 6,2005@07:40 32474</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,ONE 000-44-7629 (46)</p>
</blockquote></th>
<th><blockquote>
<p>OPHTHALMOLOGY</p>
<p>PHACHOEMULSIFICATION, LENS IMPLANT OD</p>
</blockquote></th>
<th>D</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>APR 12,2005@12:00 32508</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FORTYONE 000-43-2109 (78)</p>
</blockquote></td>
<td><blockquote>
<p>OPHTHALMOLOGY</p>
<p>PHACOEMULSIFICATION, LENS IMPLANT OS</p>
</blockquote></td>
<td>D</td>
</tr>
<tr class="even">
<td><blockquote>
<p>APR 12,2005@13:50 32534</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,ONE 000-44-7629 (46)</p>
</blockquote></td>
<td><blockquote>
<p>PLASTIC SURGERY (INCLUDES HEAD AND NECK) EXCISION OF RT. WRIST MASS</p>
</blockquote></td>
<td>D</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APR 12,2005@14:00 32544</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,THIRTY 000-82-9472 (48)</p>
</blockquote></td>
<td><blockquote>
<p>OPHTHALMOLOGY PHACOEMULSIFICATION OD</p>
</blockquote></td>
<td>D</td>
</tr>
<tr class="even">
<td><blockquote>
<p>APR 13,2005@09:20 32513</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTYTWO 000-99-8888 (79)</p>
</blockquote></td>
<td><blockquote>
<p>OPHTHALMOLOGY</p>
<p>PHACOEMULSIFICATION, LENS IMPLANT OD</p>
</blockquote></td>
<td>D</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APR 15,2005@13:05 32351</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTY 000-45-9999 (44)</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BELOW) EXCISIONAL BIOPSY MASS RT. BREAST</p>
</blockquote></td>
<td>D</td>
</tr>
<tr class="even">
<td><blockquote>
<p>APR 19,2005@13:00 32580</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SEVENTEEN 000-45-5119 (71)</p>
</blockquote></td>
<td><blockquote>
<p>OPHTHALMOLOGY</p>
<p>PHACOEMULSIFICATION LENS IMPLANT OD</p>
</blockquote></td>
<td>D</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APR 27,2005@13:15 32684</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY 000-56-7821 (40)</p>
</blockquote></td>
<td><blockquote>
<p>OPHTHALMOLOGY TRABECULECTOMY OD</p>
</blockquote></td>
<td>F</td>
</tr>
</tbody>
</table>

> TOTAL CASES MISSING DATA: 8

> MISSING ITEMS CODES: A-HOSPITAL ADMISSION STATUS, B-MAJOR/MINOR, C-CASE SCHEDULE TYPE, D-ATTENDING CODE, E-TIME PAT OUT OR, F-WOUND CLASSIFICATION, G-ASA CLASS, H-CPT CODE (PRINCIPAL)

> Admitted w/in 14 days of Out Surgery If Postop Occ

### \[SROQADM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Admitted w/in 14 days of Out Surgery If Postop Occ* option displays a list of patients with completed outpatient surgical cases that resulted in at least one postoperative occurrence and a hospital admission within 14 days of the surgery.

> This report has a 132-column format and is designed to be copied to a printer with wide paper.

> Example: Report of Admitted w/in 14 days of Out Surgery If Postop Occ

> *printout follows*

#### 394c Surgery V. 3.0 User Manual November

> MAYBERRY, NC

> OUTPATIENT CASES WITH POSTOP OCCURRENCES AND ADMISSIONS WITHIN 14 DAYS PAGE 1 From: SEP 1,2004 To: DEC 31,2004

> Report Printed: FEB 12,2005@13:44

> DATE OF OPERATION PATIENT NAME SURGICAL SPECIALTY ANESTHESIA TECHNIQUE DATE OF ADMISSION CASE \# PATIENT ID (AGE) PROCEDURE(S) PERFORMED

> \*OCCURRENCE - (DATE)

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 30%" />
<col style="width: 13%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SEP 24,2004@12:30</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,FORTY</p>
</blockquote></th>
<th><blockquote>
<p>THORACIC SURGERY (INC. CARDIAC</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th><blockquote>
<p>OCT 3,2004@14:11</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>30395</p>
</blockquote></td>
<td><blockquote>
<p>000-77-7777 (72)</p>
</blockquote></td>
<td><blockquote>
<p>MEDIASTINOSCOPY WITH NODE BIOPSY</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*OTHER OCCURRENCE -</p>
</blockquote></td>
<td><blockquote>
<p>(10/03/04)</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 21%" />
<col style="width: 28%" />
<col style="width: 13%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SEP 25,2004@14:30</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,EIGHTEEN</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL(OR WHEN NOT DEFINED BE</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th><blockquote>
<p>SEP 28, 2004@10:06</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>30544</p>
</blockquote></td>
<td><blockquote>
<p>000-22-3334 (71)</p>
</blockquote></td>
<td><blockquote>
<p>LEFT INGUINAL HERNIORRAPHY</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>*OTHER OCCURRENCE -</p>
</blockquote></td>
<td><blockquote>
<p>(09/28/04)</p>
</blockquote></td>
<td><blockquote>
<p>HYDROCELECTOMY</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 28%" />
<col style="width: 13%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NOV 18,2004@09:45</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,FIFTEEN</p>
</blockquote></th>
<th><blockquote>
<p>PLASTIC SURGERY (INCLUDES HEAD</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th><blockquote>
<p>NOV 28, 2004@12:51</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>31034</p>
</blockquote></td>
<td><blockquote>
<p>000-98-1234 (55)</p>
</blockquote></td>
<td><blockquote>
<p>GANGLION CYST LT. WRIST</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> \*SUPERFICIAL WOUND INFECTION - (11/28/04) INCLUSION OF CYST INDEX FINGER LT.

> EXCISION OF LIPOMA OF LT. FOOT APPLICATION SHORT ARM SPLINT

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 20%" />
<col style="width: 22%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DEC 9,2004@13:35</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,EIGHT</p>
</blockquote></th>
<th><blockquote>
<p>ORTHOPEDICS</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
<th><blockquote>
<p>DEC 9, 2004@17:55</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>31242</p>
</blockquote></td>
<td><blockquote>
<p>000-37-0555 (64)</p>
</blockquote></td>
<td><blockquote>
<p>ORIF RT ULNA</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> \*SUPERFICIAL WOUND INFECTION - (12/29/04) REPAIR RT. DISTALRADIOULNAR FX (

> DEC 31,2004@07:30 SURPATIENT,FIFTYONE OTORHINOLARYNGOLOGY (ENT) GENERAL DEC 31, 2004@18:02 31277 000-23-3221 (31) NASAL SINUS SURGERY WITH BIL SPENOETHMOID POLYPECTOMY (CPT Code: 31205)

> \*OTHER CNS OCCURRENCE - (01/05/03) BILATERAL ANTROSTOMY BILATERAL TURBINECTOMY

> TOTAL CASES: 5

### Deaths Within 30 Days of Surgery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[SROQD\]

> The *Deaths Within 30 Days of Surgery* option lists patients who had surgery within the selected date range, died within 30 days of surgery. Two separate reports are available through this option.

1.  Total Cases Summary: This report may be printed in one of three ways.
    1.  All Cases

> The report will list all patients who had surgery within the selected date range and who died within 30 days of surgery, along with all of the patients' operations that were performed during the selected date range.

2.  <span id="_bookmark143" class="anchor"></span>Outpatient Cases Only

> The report will list only the surgical cases that are associated with deaths that are counted as outpatient (ambulatory) deaths.

3.  Inpatient Cases Only

> The report will list only the surgical cases that are associated with deaths that are counted as inpatient deaths.

2.  Specialty Procedures: This report will list the surgical cases that are associated with deaths that are counted for the national surgical specialty linked to the local surgical specialty. Cases are listed by national surgical specialty.

> These reports have a 132-column format and are designed to be copied to a printer.

> Example 1: Deaths Within 30 Days of Surgery - Total Cases Summary

> Select Management Reports Option: DS Deaths Within 30 Days of Surgery

> *printout follows*

> MAYBERRY, NC

> DEATHS WITHIN 30 DAYS OF SURGERY PAGE 1

> FOR SURGERY PERFORMED FROM: APR 1,2005 TO: APR 30,2005

> Report Printed: MAY 18,2005@12:09

> DEATH

> OP DATE CASE \# IN/OUT SURGICAL SPECIALTY PROCEDURE(S) RELATED

> ====================================================================================================================================

> \>\>\> SURPATIENT,FORTY (000-77-7777) - DIED 05/12/05 AGE: 70

> 04/13/05 32571 INPAT GENERAL(OR WHEN NOT DEFINED BELOW) EXPLORATORY LAPAROTOMY UNRELATED

> RIGHT HEMICOLECTOMY ILEOSTOMY

> MUCOUS FISTULA OF COLON

> 04/24/05 32693 INPAT GENERAL(OR WHEN NOT DEFINED BELOW) CLOSURE OF ABDOMINAL WALL FASCIA UNRELATED

> \>\>\> SURPATIENT,TEN (000-12-3456) - DIED 05/12/05 AGE: 68

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 28%" />
<col style="width: 34%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>04/26/05 32702</p>
</blockquote></th>
<th><blockquote>
<p>INPAT</p>
</blockquote></th>
<th><blockquote>
<p>THORACIC SURGERY (INC. CARDIAC SURG</p>
</blockquote></th>
<th><blockquote>
<p>RIGHT THORACOTOMY WITH LUNG BIOPSY</p>
</blockquote></th>
<th><blockquote>
<p>UNRELATED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DIAPHRAGM BIOPSY</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> \>\>\> SURPATIENT,SIXTY (000-56-7821) - DIED 04/30/05 AGE: 40

> 04/21/05 32567 INPAT THORACIC SURGERY (INC. CARDIAC SURG ESOPHAGECTOMY RELATED

> ESOPHAGOSCOPY BRONCHOSCOPY

> FEEDING TUBE JEJUNOSTOMY

> TOTAL DEATHS: 3

> Example 2: Deaths Within 30 Days of Surgery - Specialty Procedures

#### printout follows 

> MAYBERRY, NC

> DEATHS WITHIN 30 DAYS OF SURGERY LISTED FOR SPECIALTY PROCEDURES PAGE 1 FOR SURGERY PERFORMED FROM: APR 1,2005 TO: APR 30,2005

Report Printed: MAY 18,2005@12:38

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 23%" />
<col style="width: 16%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>OP DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT NAME</p>
</blockquote></th>
<th>DATE OF DEATH</th>
<th><blockquote>
<p>LOCAL SPECIALTY</p>
</blockquote></th>
<th><blockquote>
<p>IN/OUT</p>
</blockquote></th>
<th><blockquote>
<p>DEATH RELATED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CASE #</p>
</blockquote></td>
<td><blockquote>
<p>PATIENT ID# (AGE)</p>
</blockquote></td>
<td>PROCEDURE(S)</td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> \>\>\> GENERAL SURGERY \<\<\<

> 04/24/05 SURPATIENT,FORTY 05/12/05 GENERAL(OR WHEN NOT DEFINED BELOW) INPAT UNRELATED

> 32693 000-77-7777 (70) CLOSURE OF ABDOMINAL WALL FASCIA

> TOTAL DEATHS FOR GENERAL SURGERY: 1

> \>\>\> THORACIC SURGERY \<\<\<

> 04/26/05 SURPATIENT,TEN 05/12/05 THORACIC SURGERY (INC. CARDIAC SURG.) INPAT UNRELATED

> 32702 000-12-3456 (68) RIGHT THORACOTOMY WITH LUNG BIOPSY

> DIAPHRAGM BIOPSY

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 34%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>04/21/05</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,SIXTY</p>
</blockquote></th>
<th><blockquote>
<p>04/30/05</p>
</blockquote></th>
<th><blockquote>
<p>THORACIC SURGERY (INC. CARDIAC SURG.)</p>
</blockquote></th>
<th><blockquote>
<p>INPAT</p>
</blockquote></th>
<th><blockquote>
<p>RELATED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>32567</p>
</blockquote></td>
<td><blockquote>
<p>000-56-7821 (40)</p>
</blockquote></td>
<td><blockquote>
<p>ESOPHAGECTOMY</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p>ESOPHAGOSCOPY</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p>BRONCHOSCOPY</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> FEEDING TUBE JEJUNOSTOMY

> TOTAL DEATHS FOR THORACIC SURGERY: 2

> TOTAL FOR ALL SPECIALTIES: 3

> <span id="_bookmark144" class="anchor"></span>Pages 397c and 397d have been deleted.

> *(This page included for two-sided copying.)*

## Unlock a Case for Editing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO-UNLOCK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Chief of Surgery, or a designee, uses the *Unlock a Case for Editing* option to unlock a case so that it can be edited. A case that has been completed will automatically lock within a specified time after the date of operation. When a case is locked, the data cannot be edited.

> With this option, the selected case will be unlocked so that the user can use another option (such as in the *Operation Menu* option or *Anesthesia Menu* option) to make changes. The case will automatically re-lock in the evening. The package coordinator has the ability to set the automatic lock times.

> Although the case may be unlocked to allow editing, any field that is included in an electronically signed report, for example in the Nurse Intraoperative Report, will require the creation of an addendum to the report before the edit can be completed.

> Example: Unlock a Case for Editing

> Select Chief of Surgery Menu Option: Unlock a Case for Editing

## Update Status of Returns Within 30 Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO UPDATE RETURNS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Status of Returns Within 30 Days* option is used to update the status of Returns to Surgery within 30 days of a surgical case.

> Example: Update Status of Returns

## Update Cancelled Cases

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO UPDATE CANCELLED CASE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](surgery-version-3-user-manual-updated-sr-3-184/046.png)This option is locked with the SROCHIEF key and will not appear on the menu if the user does not have this key.

> Normally, a cancelled case cannot be accessed for editing. However, the restricted *Update Cancelled Cases* option allows the Chief of Surgery to edit a cancelled case.

> When the user enters this option, the software will allow access to the *Operations Menu* option.

> Example: Update a Cancelled Case

> Select Chief of Surgery Menu Option: CAN Update Cancelled Case

## Update Operations as Unrelated/Related to Death

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO DEATH RELATED\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Operations as Unrelated/Related to Death* option is used to update the status of operations performed within 90 days prior to death. The status is either UNRELATED or RELATED TO DEATH. With this option the user can add comments to further document the review of death.

> Example: Updating an Operation as Related to Death

## Update/Verify Procedure/Diagnosis Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRCODING EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update/Verify Procedure/Diagnosis Codes* option is used to edit and/or verify the CPT and ICD-9 codes for an operation or non-O.R. procedure.

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>Operation Date: FEB 18, 1999@08:45 Case #124</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Principal Procedure: TRACHEOSTOMY</p></li>
<li><p>Principal CPT Code: NOT ENTERED</p></li>
<li><p>Other Procedures:  INFORMATION ENTERED </p></li>
<li><p>Postoperative Diagnosis: FOREIGN BODY IN TRACHEA</p></li>
<li><p>Principal Diagnosis Code: NOT ENTERED</p></li>
<li><p>Other Postop Diagnosis:  INFORMATION ENTERED </p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Information to Edit: <strong>?</strong></p>
<p>Enter the number corresponding to the information you want to update. You may enter 'ALL' to update all the information displayed on this screen, or a range of numbers separated by a ':' to update more than one item.</p>
<p>Select Information to Edit: <strong>2</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 41%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>Operation Date: FEB 18, 1999@08:45</p>
</blockquote></th>
<th><blockquote>
<p>Case #124</p>
</blockquote></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Principal Procedure Code (CPT): <strong>31600</strong> INCISION OF WINDPIPE TRACHEOSTOMY, PLANNED (SEPARATE PROCEDURE);</p>
<p>Modifier: <strong>59</strong> DISTINCT PROCEDURAL SERVICE</p>
<p>Modifier: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>Operation Date: FEB 18, 1999@08:45 Case #124</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><ol type="1">
<li><p>Principal Procedure: TRACHEOSTOMY</p></li>
<li><blockquote>
<p>Principal CPT Code: 31600 INCISION OF WINDPIPE TRACHEOSTOMY, PLANNED (SEPARATE PROCEDURE);</p>
</blockquote></li>
</ol>
<blockquote>
<p>Modifiers: -59</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>3. Other Procedures:  INFORMATION ENTERED </p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><ol start="4" type="1">
<li><p>Postoperative Diagnosis: FOREIGN BODY IN TRACHEA</p></li>
<li><p>Principal Diagnosis Code: NOT ENTERED</p></li>
</ol></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>6. Other Postop Diagnosis:  INFORMATION ENTERED </p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Select Information to Edit: <strong>3</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 7%" />
<col style="width: 34%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>Operation Date: FEB 18, 1999@08:45</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#124</p>
</blockquote></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th colspan="3"><ol type="1">
<li><p>Principal Procedure: TRACHEOSTOMY</p></li>
<li><blockquote>
<p>Principal CPT Code: 31600 INCISION OF WINDPIPE TRACHEOSTOMY, PLANNED (SEPARATE PROCEDURE);</p>
</blockquote></li>
</ol>
<blockquote>
<p>Modifiers: -59</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>3. Other Procedures:  INFORMATION ENTERED </p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><ol start="4" type="1">
<li><p>Postoperative Diagnosis: FOREIGN BODY IN TRACHEA</p></li>
<li><p>Principal Diagnosis Code: NOT ENTERED</p></li>
</ol></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>6. Other Postop Diagnosis:  INFORMATION ENTERED </p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Select Information to Edit: <strong>5</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 6%" />
<col style="width: 4%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 3%" />
<col style="width: 12%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>Operation Date: FEB 18, 1999@08:45</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th>#124</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Prin Pre-OP ICD Diagnosis Code: <strong>934.0</strong></p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
<th><blockquote>
<p>934.0</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>FOREIGN</p>
</blockquote></th>
<th><blockquote>
<p>BODY</p>
</blockquote></th>
<th><blockquote>
<p>IN</p>
</blockquote></th>
<th><blockquote>
<p>TRACHEA</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 7%" />
<col style="width: 34%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>Operation Date: FEB 18, 1999@08:45</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#124</p>
</blockquote></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th colspan="3"><ol type="1">
<li><p>Principal Procedure: TRACHEOSTOMY</p></li>
<li><blockquote>
<p>Principal CPT Code: 31600 INCISION OF WINDPIPE TRACHEOSTOMY, PLANNED (SEPARATE PROCEDURE);</p>
</blockquote></li>
</ol>
<blockquote>
<p>Modifiers: -59</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>3. Other Procedures:  INFORMATION ENTERED </p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><ol start="4" type="1">
<li><p>Postoperative Diagnosis: FOREIGN BODY IN TRACHEA</p></li>
<li><p>Principal Diagnosis Code: 934.0 FOREIGN BODY IN TRACHEA</p></li>
</ol></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>6. Other Postop Diagnosis:  INFORMATION ENTERED </p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Select Information to Edit: <strong>6</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 41%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
</blockquote></th>
<th></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Operation Date: FEB 18, 1999@08:45</p>
</blockquote></th>
<th><blockquote>
<p>Case #124</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Other Postop Diagnosis:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>1. Enter NEW Other Postop Diagnosis</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Enter selection: (1-1): <strong>1</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Enter new OTHER POSTOP DIAGNOSIS: LARYNGEAL/TRACHEAL BURN</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>ICD DIAGNOSIS CODE: <strong>947.1</strong> 947.1 BURN LARYNX/TRACHEA/LUNG</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The ICD Code field below indicates ICD-9 or ICD-10 codes:

> Example: ICD-9 Code:

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 7%" />
<col style="width: 34%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719)</p>
<p>Operation Date: FEB 18, 1999@08:45</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#124</p>
</blockquote></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th colspan="3"><ol type="1">
<li><p>Principal Procedure: TRACHEOSTOMY</p></li>
<li><blockquote>
<p>Principal CPT Code: 31600 INCISION OF WINDPIPE TRACHEOSTOMY, PLANNED (SEPARATE PROCEDURE);</p>
</blockquote></li>
</ol>
<blockquote>
<p>Modifiers: -59</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>3. Other Procedures:  INFORMATION ENTERED </p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><ol start="4" type="1">
<li><p>Postoperative Diagnosis: FOREIGN BODY IN TRACHEA</p></li>
<li><p>Principal Diagnosis Code: 934.0 FOREIGN BODY IN TRACHEA</p></li>
</ol></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>6. Other Postop Diagnosis:  INFORMATION ENTERED </p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Select Information to Edit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: ICD-10 Code:

> *(This page included for two-sided copying.)*

# Chapter Five: Managing the Software Package Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter describes options designed for the exclusive use of the Surgery package coordinator. The package coordinator can configure certain Surgery package fields to conform to a facility's needs.

> <span id="_bookmark152" class="anchor"></span>Exiting an Option or the System

> The user should enter an up-arrow (^) to stop what he or she is doing. The up-arrow can be used at almost any prompt to terminate the line of questioning and return to the previous level in the routine. The user would continue entering up-arrows to completely exit the system.

## Option Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The main option included in this menu is listed below. To the left of the option name is the shortcut synonym that the user can enter to select the option. This is a restricted option and only users with the SRCOORD security key have access.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgery Package Management Menu</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Surgery Package Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO PACKAGE MANAGEMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Surgery Package Management Menu* provides access to options that are used to manage the Surgery software. Each option is discussed in the rest of this chapter.

> The options included in this menu are listed below. To the left of the option name is the shortcut synonym that the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>S</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgery Site Parameters (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td><blockquote>
<p><em>Operating Room Information (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SU</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgery Utilization Menu ..</em>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KEY</p>
</blockquote></td>
<td><blockquote>
<p><em>Person Field Restrictions Menu ...</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SD</p>
</blockquote></td>
<td><blockquote>
<p><em>Update O.R. Schedule Devices</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Staff Surgeon Information</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Flag Drugs for Use as Anesthesia Agents</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Site Configurable Files</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SI</p>
</blockquote></td>
<td><blockquote>
<p><em>Surgery Interface Management Menu ...</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>V</p>
</blockquote></td>
<td><blockquote>
<p><em>Make Reports Viewable in CPRS</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark155" class="anchor"></span>Surgery Site Parameters (Enter/Edit)

### \[SROPARAM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgical Service managers use this option to create or update local site parameters for the Surgery package.

> A question mark or two can be entered to access the help text at any prompt.

> Example: Enter Surgery Site Parameters

## Operating Room Information (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO-ROOM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operating Room Information (Enter/Edit)* option is used to enter or edit information pertinent to a selected operating room, including start and end times, and cleaning time.

> At the TYPE field, the user can enter two question marks (??) to get a list of operating room types from which to select. If an operating room is not in service, the user can enter "YES" at the INACTIVE field to make the operating room inactive and prevent its use by other people using the Surgery software.

> Example: Entering Operating Room Information

## Surgery Utilization Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR OR UTIL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Surgery Utilization Menu* contains options designed to help determine operating room use. With this menu, Surgery Service managers can schedule the normal operating hours for an operating room, as well as the actual hours an operating room was in use. Operating rooms can also be inactivated. A report can be generated to see what percentage of available hours an operating room was in use and to see if an O.R. was used outside normal hours.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>E</p>
</blockquote></td>
<td><blockquote>
<p><em>Operating Room Utilization (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p><em>Normal Daily Hours (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Operating Room Utilization Report</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>H</p>
</blockquote></td>
<td><blockquote>
<p><em>Report of Normal Operating Room Hours</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p><em>Purge Utilization Information</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Operating Room Utilization (Enter/Edit)

### \[SR UTIL EDIT ROOM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operating Room Utilization (Enter/Edit)* option is used to update the actual start and end times for operating rooms on a selected date, one operating room at a time. This information is used when generating the operating room utilization reports.

> The user first enters the date, then the name of the operating room. The software will default to the start and end times and allow the times to be edited. There is also a prompt for inactivating a room. If the user does not want to edit an entry, pressing the \<Enter\> key will display the next prompt.

> When the user is finished entering or editing times for an operating room, he or she will be prompted for the name of the next operating room. If the user does not wish to edit times for any more operating rooms on this date, he or she should press the \<Enter\> key. The software will then prompt for a new date and the cycle begins again. When the user is finished editing times, he or she can press the \<Enter\> key or enter an up-arrow (^) to exit this option.

> Example: Enter and Edit Operating Room Times

> Select Surgery Utilization Menu Option: E Operating Room Utilization (Enter/Edit)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 3%" />
<col style="width: 16%" />
<col style="width: 5%" />
<col style="width: 2%" />
<col style="width: 24%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Operating Room Utilization</p>
</blockquote></th>
<th><blockquote>
<p>on</p>
</blockquote></th>
<th>NOV 3, 2003</th>
<th></th>
<th></th>
<th></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Update Start and End Times</p>
</blockquote></th>
<th><blockquote>
<p>for</p>
</blockquote></th>
<th><blockquote>
<p>which Operating</p>
</blockquote></th>
<th><blockquote>
<p>Room</p>
</blockquote></th>
<th><blockquote>
<p>?</p>
</blockquote></th>
<th><blockquote>
<p><strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Normal Daily Hours (Enter/Edit)

### \[SR NORMAL HOURS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Normal Daily Hours (Enter/Edit)* option is used to schedule the normal start and end times of an operating room for each day of the week, one operating room at a time. The information is used to help determine operating room use on a weekly basis.

> First, the user enters the name of the operating room. Beginning with Sunday, the software will provide an editing schedule for each day of the week and prompt for normal start and end times for each day.

> There is also a prompt for inactivating a room. When the schedules for the week have been completed, the user will be prompted for the name of the next operating room for which to enter times. When the use finishes editing times, he or she can press the \<Enter\> key or enter an up-arrow (^) to exit this option.

> At the "Select information to edit:" prompt, the user can 1) enter the letter A to update all the information on the schedule, 2) enter a number to update information in the corresponding field, 3) enter a range of numbers separated by a colon (:), or 4) press the \<Enter\> key to move to the next day's schedule. To edit the schedule for a particular day, the user enters an up-arrow followed by a day of the week. For example, to edit Friday's schedule, ^Friday would be entered. This is demonstrated in the following example.

> ![](surgery-version-3-user-manual-updated-sr-3-184/047.png)The start and end times must be in military time. Also, use a leading zero when the hour is a single digit (e.g., 7 AM is 07:00).

> Example: Enter Normal Start and End Times for an Operating Room

> Select Surgery Utilization Menu Option: N Normal Daily Hours (Enter/Edit)

> Operating Room Utilization Report

### \[SR OR UTL1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operating Room Utilization Report* option prints utilization information, within a selected date range, for all operating rooms or for a single operating room. The report displays the percent utilization, the number of cases, the total operation time and the time worked outside normal hours for each operating room individually and all operating rooms collectively.

### How the Percent Utilization is Derived

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The percent utilization is derived by dividing the total operation time for all operations (including total time patients were in O.R., plus the cleanup time allowed for each case) by the total functioning time as defined in the SURGERY UTILIZATION file. The quotient is then multiplied by 100.

> This report has a 132-column format and is designed to be copied to a printer.

> Example: Print the Operating Room Utilization Report

> *printout follows*

> MAYBERRY, NC PAGE 1

> SURGICAL SERVICE OPERATING ROOM UTILIZATION REPORT

> FOR ALL OPERATING ROOMS FROM: MAR 8,2003 TO: MAR 9, 2003 DATE PRINTED: MAR 17,2003

> ====================================================================================================================================

> OPERATING ROOM PERCENT UTILIZATION NUMBER OF CASES TOTAL OPERATION TIME TIME WORKED OUTSIDE NORMAL HRS

> (INCLUDING OR MAINTENANCE)

> ====================================================================================================================================

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>OR1</th>
<th><blockquote>
<p>70%</p>
</blockquote></th>
<th><blockquote>
<p>3</p>
</blockquote></th>
<th><blockquote>
<p>17 hrs and 35 mins</p>
</blockquote></th>
<th><blockquote>
<p>6 hrs and 20 mins</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR2</td>
<td><blockquote>
<p>39%</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>7 hrs and 25 mins</p>
</blockquote></td>
<td><blockquote>
<p>1 hr and 10 mins</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OR3</td>
<td><blockquote>
<p>133%</p>
</blockquote></td>
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>23 hrs and 42 mins</p>
</blockquote></td>
<td><blockquote>
<p>2 hrs and 30 mins</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OR4</td>
<td><blockquote>
<p>29%</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>4 hrs and 41 mins</p>
</blockquote></td>
<td>-</td>
</tr>
<tr class="even">
<td>OR5</td>
<td><blockquote>
<p>84%</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>18 hrs and 50 mins</p>
</blockquote></td>
<td><blockquote>
<p>5 hrs and 25 mins</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OR6</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>-</td>
<td>-</td>
</tr>
<tr class="even">
<td>OR7</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td>-</td>
<td>-</td>
</tr>
<tr class="odd">
<td>TOTAL UTILIZATION FOR ALL ROOMS</td>
<td><blockquote>
<p>63%</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>72 hrs and 13 mins</p>
</blockquote></td>
<td><blockquote>
<p>15 hrs and 25 mins</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ====================================================================================================================================

> Report of Normal Operating Room Hours

### \[SR OR HOURS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Report of Normal Operating Room Hours* option provides the start time and the end time of the normal working hours for all operating rooms or for the selected operating room for each date within the specified date range. The total time of the normal working day is displayed for each operating room for each date.

> Example: Print Operating Room Normal Working Hours Report

> Select Surgery Utilization Menu Option: H Report of Normal Operating Room Hours

> *printout follows*

> OPERATING ROOM NORMAL WORKING HOURS FROM 03/01/99 TO 03/12/99

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 30%" />
<col style="width: 23%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>OPERATING ROOM</th>
<th><blockquote>
<p>START TIME</p>
</blockquote></th>
<th><blockquote>
<p>END TIME</p>
</blockquote></th>
<th>TOTAL TIME</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 1, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR2 OR3 OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
<p> INACTIVE </p>
<p> INACTIVE  17:00</p>
</blockquote></td>
<td><blockquote>
<p>8 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 2, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td><blockquote>
<p>mins</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OR3 OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
<p> INACTIVE  17:00</p>
</blockquote></td>
<td><blockquote>
<p>8 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 3, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR3</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>13:30</p>
<p>17:00</p>
</blockquote></td>
<td><blockquote>
<p>6 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 4, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR3</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>13:30</p>
<p>17:00</p>
</blockquote></td>
<td><blockquote>
<p>6 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 5, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR3</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>13:30</p>
<p>17:00</p>
</blockquote></td>
<td><blockquote>
<p>6 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 6, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR3</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>13:30</p>
<p>17:00</p>
</blockquote></td>
<td><blockquote>
<p>6 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 7, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td><blockquote>
<p>mins</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
</tbody>
</table>

> OPERATING ROOM NORMAL WORKING HOURS FROM 03/01/99 TO 03/12/99

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 30%" />
<col style="width: 23%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>OPERATING ROOM</th>
<th><blockquote>
<p>START TIME</p>
</blockquote></th>
<th><blockquote>
<p>END TIME</p>
</blockquote></th>
<th>TOTAL TIME</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 7, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OR3 OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p> INACTIVE </p>
<p> INACTIVE  17:00</p>
</blockquote></td>
<td><blockquote>
<p>10 hrs</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 8, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR2 OR3 OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
<p> INACTIVE </p>
<p> INACTIVE  17:00</p>
</blockquote></td>
<td><blockquote>
<p>8 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 9, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR3 OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
<p> INACTIVE  17:00</p>
</blockquote></td>
<td><blockquote>
<p>8 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 10, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR3</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>13:30</p>
<p>17:00</p>
</blockquote></td>
<td><blockquote>
<p>6 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 11, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR3</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR4 OR5</td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>13:30</p>
<p>17:00</p>
</blockquote></td>
<td><blockquote>
<p>6 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><blockquote>
<p> MAR 12, 1999 </p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OR1</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td>OR2</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="odd">
<td>OR3</td>
<td><blockquote>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>15:30</p>
</blockquote></td>
<td>8 hrs and 30</td>
<td>mins</td>
</tr>
<tr class="even">
<td><p>OR4</p>
<p>OR5</p></td>
<td><blockquote>
<p>07:00</p>
<p>07:00</p>
</blockquote></td>
<td><blockquote>
<p>13:30</p>
<p>17:00</p>
</blockquote></td>
<td><blockquote>
<p>6 hrs and 30</p>
<p>10 hrs</p>
</blockquote></td>
<td>mins</td>
</tr>
</tbody>
</table>

> Purge Utilization Information

### \[SR PURGE UTILIZATION\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Purge Utilization Information* option is used to purge utilization information for a selected date range. After selecting a starting date, the user can purge all utilization information for dates prior to, and including, that specified starting date.

> Example: Purge Utilization Information

> Select Surgery Utilization Menu Option: P Purge Utilization Information

## Person Field Restrictions Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROKEY MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Person Field Restrictions Menu* contains options used by the package coordinator to maintain restrictions applied to person-type fields (meaning a field that points to the NEW PERSON field) in files.

> The options included in this menu are listed below. To the left of the option name is the shortcut synonym the user can enter to select the option. None of these options will display if the user does not have proper security clearance.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>E</p>
</blockquote></td>
<td><blockquote>
<p><em>Enter Restrictions for 'Person' Fields</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Remove Restrictions on 'Person' Fields</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter Restrictions for 'Person' Fields

### \[SROKEY ENTER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Enter Restrictions for 'Person' Fields* option allows IRM personnel to assign a key to a specific person-type field (meaning any field that points to the NEW PERSON field) in a file or sub-file.

> A key limits the acceptable responses to a field. The Surgery software can be tailored to limit acceptable responses in the field to only those people assigned one of the keys used to restrict the field. For example, a prompt asking for the name of the attending surgeon can be modified to accept only the names of surgeons. Additionally, a field can have more than one key assigned to it; thus, the ATTENDING SURGEON field can be modified to accept the names of surgeons and other surgical staff.

> Example 1 below shows how to enter the surgeon key for the SURGEON field in the SURGERY file. Example 2 shows how to enter the surgeon, nurse, and anesthetist keys for a sub-field in the SURGERY file.

> Keys can be removed using the *Remove Restrictions on 'Person' Fields* option.

> The user can enter one or two question marks to access the on-line help if assistance is needed while interacting with the software. A question mark can also be entered at the "Select Additional Key:" prompt for a list of keys from which to select.

> Example 1: Enter Restrictions

> Select Person Field Restrictions Menu Option: E Enter Restrictions for 'Person' Fields

> Example 2: Enter Restrictions

> Select Person Field Restrictions Menu Option: E Enter Restrictions for 'Person' Fields

> Remove Restrictions on 'Person' Fields

### \[SROKEY REMOVE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Remove Restrictions on 'Person' Fields* option allows IRM personnel to remove a key to a specific person-type field in a specific file. A key limits the acceptable responses to a field; removing a key removes a restriction on the acceptable responses.

> In the example below, the key that permits the name of an anesthetist is removed from the RESTRAINTS & POSITION AIDS field, leaving the nurse and surgeon keys intact. All of the keys can be removed at one time by entering ALL at the "Select Number or 'ALL':" prompt.

> Example: Remove Restrictions

> Select Person Field Restrictions Menu Option: R Remove Restrictions on 'Person' Fields

> Select Person Field Restrictions Option:

## Update O.R. Schedule Devices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR UPDATE SCHEDULE DEVICE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update O.R. Schedule Devices* option is used to update the list of devices that will print the Schedule of Operations when printing to all pre-defined printers.

> Example: Add a New Schedule Device

> Select Surgery Package Management Menu Option: SD Update O.R. Schedule Devices

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 3%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Update O.R. Schedule Devices</p>
</blockquote></th>
<th colspan="10"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Select OR SCHEDULE DEVICES: ARE YOU ADDING 'SPD PTR '</p>
<p>SITE PARAMETERS)? <strong>Y</strong> (YES)</p>
<p>Select OR SCHEDULE DEVICES:</p>
</blockquote></td>
<td><p><strong>SPD</strong></p>
<blockquote>
<p>AS</p>
</blockquote></td>
<td><blockquote>
<p><strong>PTR</strong></p>
<p>A NEW</p>
</blockquote></td>
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td><blockquote>
<p>SCHEDULE</p>
</blockquote></td>
<td><blockquote>
<p>DEVICES</p>
</blockquote></td>
<td><blockquote>
<p>(THE</p>
</blockquote></td>
<td><blockquote>
<p>1ST</p>
</blockquote></td>
<td><blockquote>
<p>FOR</p>
</blockquote></td>
<td><blockquote>
<p>THIS</p>
</blockquote></td>
<td><blockquote>
<p>SURGERY</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Update Staff Surgeon Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROSTAFF\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Staff Surgeon Information* option allows the designation of a user as a staff surgeon by assigning a security key called SR STAFF SURGEON. The Annual Report of Surgical Procedures will count cases performed by holders of this security key as having been performed by "staff." All other cases will be counted as performed by "resident."

> Example 1: Designate a Staff Surgeon

> Select Surgery Package Management Menu Option: U Update Staff Surgeon Information

> Example 2: Remove Staff Surgeon Designation

> Select Surgery Package Management Menu Option: U Update Staff Surgeon Information

## Flag Drugs for Use as Anesthesia Agents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROCODE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Surgery Service managers use the *Flag Drugs for Use as Anesthesia Agents* option to mark drugs for use as anesthesia agents. If the drug is not flagged, the user will not be able to select it as an entry for the ANESTHESIA AGENT data field.

> To flag a drug, it must already be listed in the Pharmacy DRUG file. To add a drug to this file, the user should contact the facility's Pharmacy Package Coordinator.

> Example: Flag Drugs Used as Anesthesia Agents

> Enter the name of the drug you wish to flag:

## Update Site Configurable Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR UPDATE FILES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Site Configurable Files* option is designed for the package coordinator to add, edit, or inactivate file entries for the site-configurable files.

> The software provides a numbered list of site-configurable files. The user should enter the number corresponding to the file that he or she wishes to update. The software will default to any previously entered information on the entry and provide a chance to edit it. The last prompt asks whether the user wants to inactivate the entry; answering Yes or 1 will inactivate the entry.

> Example 1: Add a New Entry to a Site-Configurable File

> Select Surgery Package Management Menu Option: F Update Site Configurable Files

> Example 2: Re-Activate an Entry

> Select Surgery Package Management Menu Option: F Update Site Configurable Files

## Surgery Interface Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRHL INTERFACE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Surgery Interface Management Menu* contains options that allow the user to set up certain interface parameters that control the processing of Health Level 7 (HL7) messages. The interface adheres to the HL7 protocol and forms the basis for the exchange of health care information between the VistA Surgery package and any ancillary system.

> Currently, there are four options on the *Surgery Interface Management Menu*.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>I</p>
</blockquote></td>
<td><blockquote>
<p><em>Flag Interface Fields</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p><em>File Download</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>T</p>
</blockquote></td>
<td><blockquote>
<p><em>Table Download</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Interface Parameter Field</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Flag Interface Fields

### \[SRHL INTERFACE FLDS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Flag Interface Fields* option allows the package coordinator to set the INTERFACE field in the SURGERY INTERFACE file. The categories listed on the first screen correspond to entries in SURGERY INTERFACE file. These categories are listed in the Surgery HL7 Interface Specifications document as being the OBR (Observation Request) text identifiers. Each identifier corresponds to several fields in the VistA Surgery package. This allows the user to control the flow of data between the VistA Surgery package and the ancillary system on a field-by-field basis.

> The option lists each identifier and its current setting. To receive the data coming from the ancillary system for a category, the flag the flag should be set to R for receive. To ignore the data, the flag should be set to N for not receive. To see a second underlying layer of OBX (Observation/Result) text identifiers (the SURGERY file fields) and their settings, the OBR (Observation Request) text identifier should be set to R for receive. The option will allow the user to toggle the settings for a range of items or for individual items.

> Example: Flagging Operation Information to be Received

> Select Surgery Interface Management Menu Option: I Flag Interface Fields

> File Download

### \[SRHL DOWNLOAD INTERFACE FILES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *File Download* option is used to download Surgery interface files to the Automated Anesthesia Information System (AAIS). The process is currently being done by a screen capture to a file. In the future, this will be changed to a background task that can be queued to send HL7 master file updates.

> Example: Downloading Interface Files

> Select Surgery Interface Management Menu Option: F File Download

> Table Download

### \[SRHL DOWNLOAD SET OF CODES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Table Download* option downloads the SURGERY file set of codes to the AAIS. This process is currently being done by a screen capture to a file. In the future, this will be changed to a background task that can be queued to send HL7 master file updates.

> Example: Downloading Surgery Set of Codes

> Select Surgery Interface Management Menu Option: T Table Download

> Update Interface Parameter Field

### \[SRHL DOWNLOAD SET OF CODES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Interface Parameter Field* option may be used to edit the parameter that determines which Surgery HL7 interface will be used, the interface compatible with HL7 V. 1.6 or the older one compatible with HL7 V. 1.5.

> If applications communicating with the Surgery HL7 interface must use the interface designed for use with HL7 V. 1.5, YES should be entered. Otherwise, NO should be entered or this field should be left blank.

> Example: Updating Interface Parameter Field

## Make Reports Viewable in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR VIEW HISTORICAL REPORTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows Operation Reports, Nurse Intraoperative Reports, Anesthesia Reports, and Procedure Reports (Non-O.R.*)* for historical cases to be moved into TIU as "electronically unsigned" to make them viewable on the CPRS Surgery tab. This option lets the user move reports by division, if necessary.

# Chapter Six: Assessing Surgical Risk Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Unadjusted surgical mortality and morbidity rates can vary dramatically from hospital to hospital in the VA hospital system, as well as in the private sector. This can be the result of differences in patient mix, as well as differences in quality of care. Studies are being conducted to develop surgical risk assessment models for many of the major surgical procedures done in the VA system. It is hoped that these models will correct differences in patient mix between the hospitals so that remaining differences in adjusted mortality and morbidity might be an indicator of differences in quality of care. The objective of this module is to facilitate data entry and transmission to the national centers in Denver, Colorado, where the data is analyzed. The Veterans Affairs Surgery Quality Improvement Program (VASQIP) Executive Committee oversees the overall direction of the Surgery Risk Assessment program.

> This Risk Assessment part of the Surgery software provides medical centers a mechanism to track information related to surgical risk and operative mortality. It gives surgeons an on-line method of evaluating and tracking patient probability of operative mortality. For example, a patient with a history of chronic illness may be more "at risk" than a patient with no prior illness.

> <span id="_bookmark169" class="anchor"></span>Exiting an Option or the System

> To get out of an option, the user should enter an up-arrow (^). The up-arrow can be entered at almost any prompt to terminate the line of questioning and return to the previous level in the routine. To completely exit the system, the user continues entering up-arrows.

> *(This page included for two-sided copying.)*

# Surgery Risk Assessment Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA RISK ASSESSMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Surgery Risk Assessment Menu* option provides the designated Surgical Clinical Nurse Reviewer with on-line access to medical information. The menu options provide the opportunity to edit, list, print, and update an existing assessment for a patient or to enter information concerning a new risk assessment.

> ![](surgery-version-3-user-manual-updated-sr-3-184/048.png) This option is locked with the SR RISK ASSESSMENT key.

> This chapter follows the main menu of the Risk Assessment module and contains descriptions of the options and sub-options needed to maintain a Risk Assessment, transmit data, and create reports. The options are organized to follow a logical workflow sequence. Each option description is divided into two main parts: an overview and a detailed example.

> The top-level options included in this menu are listed in the following table. To the left is the shortcut synonym that the user can enter to select the option.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>N</p>
</blockquote></td>
<td><blockquote>
<p><em>Non-Cardiac Assessment Information (Enter/Edit) ...</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>C</p>
</blockquote></td>
<td><blockquote>
<p><em>Cardiac Risk Assessment Information (Enter/Edit) ...</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>P</p>
</blockquote></td>
<td><blockquote>
<p><em>Print a Surgery Risk Assessment</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Assessment Completed/Transmitted in Error</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>L</p>
</blockquote></td>
<td><blockquote>
<p><em>List of Surgery Risk Assessments</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>F</p>
</blockquote></td>
<td><blockquote>
<p><em>Print 30 Day Follow-up Letters</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Exclusion Criteria (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>M</p>
</blockquote></td>
<td><blockquote>
<p><em>Monthly Surgical Case Workload Report</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>V</p>
</blockquote></td>
<td><blockquote>
<p><em>M&amp;M Verification Report</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p><em>Update 1-Liner Case</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>T</p>
</blockquote></td>
<td><blockquote>
<p><em>Queue Assessment Transmissions</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td><blockquote>
<p><em>Alert Coder Regarding Coding Issues</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ERM</p>
</blockquote></td>
<td><blockquote>
<p><em>Risk Model Lab Test (Enter/Edit)</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Non-Cardiac Risk Assessment Information (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA ENTER/EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The nurse reviewer uses the *Non-Cardiac Risk Assessment Information (Enter/Edit)* option to enter a new risk assessment for a non-cardiac patient. This option is also used to make changes to an assessment that has already been entered. Cardiac cases are evaluated differently from non-cardiac cases and are entered into the software from different options. See the section, "Cardiac Risk Assessment Information (Enter/Edit)" for more information about risk assessments for cardiac cases.

> The following options are available from this option, and let the user add in-depth data for a case. To the left is the shortcut synonym that the user can enter to select the option.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRE</p>
</blockquote></td>
<td><blockquote>
<p><em>Preoperative Information (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LAB</p>
</blockquote></td>
<td><blockquote>
<p><em>Laboratory Test Results (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>O</p>
</blockquote></td>
<td><blockquote>
<p><em>Operation Information (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>D</p>
</blockquote></td>
<td><blockquote>
<p><em>Patient Demographics (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IO</p>
</blockquote></td>
<td><blockquote>
<p><em>Intraoperative Occurrences (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PO</p>
</blockquote></td>
<td><blockquote>
<p><em>Postoperative Occurrences (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RET</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Status of Returns Within 30 Days</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Assessment Status to 'COMPLETE'</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td><blockquote>
<p><em>Alert Coder Regarding Coding Issues</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> The following example demonstrates how to create a new risk assessment for non-cardiac patients and how to get to the sub-option menu below.

> <span id="_bookmark172" class="anchor"></span>Creating a New Risk Assessment

1.  The user is prompted to select either a patient name or a case. Selecting by case lets the user enter a specific surgery case number. Selecting by patient will display any previously entered assessments for a patient. An asterisk (\*) indicates cardiac cases. The user can then choose to create a new assessment or edit one of the previously entered assessments.
2.  After choosing an operation on which to report, the user should respond YES to the prompt, "Are you sure that you want to create a Risk Assessment for this surgical case ? " The user must answer YES (or press the \<Enter\> key to accept the YES default) to get to any of the sub-options. If the answer is NO, the case created in step 1 will not be considered an assessment, although it can appear on some lists, and the software will return the user to the "Select Patient:" prompt.
3.  Preoperative, operative, postoperative, and lab information is entered and edited using the sub- option(s).

> If assistance is needed while interacting with the software, the user should enter one or two question marks (??) to access the on-line help.

> Example: Creating a New Risk Assessment (Non-Cardiac)

> When selecting a case to be assessed, if coding is completed for the case, and only excluded CPT codes are assigned, the software warns the Nurse Reviewer with the message:

> ![](surgery-version-3-user-manual-updated-sr-3-184/049.png)"Based on the CPT Codes assigned for this case, this case should be excluded." This is only a warning. The Nurse Reviewer may still create the assessment.

> When selecting a case to be assessed, if no CPT codes have been assigned to the case, the software warns the Nurse Reviewer with the message:

> "No CPT Codes have been assigned for this case."

> This is only a warning. The Nurse Reviewer may still create the assessment.

> To enter information for the risk assessment, use the sub-options from this menu option. These options are described in the following sections. For example, to enter operation information, select the *Operation Information Enter/Edit* option.

## Editing an Incomplete Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To edit an incomplete risk assessment, the user can either select the assessment by patient or by surgery case number.

> Example: Using the Select by Case Number Function to Edit an Incomplete Assessment

> These options are described in the following sections.

## Preoperative Information (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA PREOP DATA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Preoperative Information (Enter/Edit)* option is used to enter or edit preoperative assessment information. The software will present two pages. At the bottom of each page is a prompt to select one or more preoperative items to edit. If the user does not want to edit any items on the page, pressing the

> \<Enter\> key will advance to the next page or, if the user is already on page two, will exit the option.

> About the "Select Preoperative Information to Edit:" Prompt

> At this prompt the user enters the item number he or she wishes to edit. Entering A for ALL allows the user to respond to every item on the page, or a range of numbers separated by a colon (:) can be entered to respond to a range of items. Number-letter combinations can also be used, such as 2C, to update a field within a group, such as CURRENT PNEUMONIA.

> Each prompt at the category level allows for an entry of YES or NO. If NO is entered, each item under that category will automatically be answered NO. On the other hand, responding YES at the category level allows the user to respond individually to each item under the main category.

> For instance, if number 2 is chosen, and the "PULMONARY:" prompt is answered YES, the user will be asked if the patient is ventilator dependent, has a history of COPD, and has pneumonia. If the "PULMONARY:" prompt is answered NO, the software will place a NO response in all the fields of the Pulmonary group. The majority of the prompts in this option are designed to accept the letters Y, N, or NS for YES, NO, and NO STUDY.

> After the information has been entered or edited, the terminal display screen will clear and present a summary. The summary organizes the information entered and provides another chance to enter or edit data.

> This functionality allows the nurse reviewer to duplicate preoperative information from an earlier operation within 60 days of the date of operation on the same patient.

> Example 1: Enter/Edit Preoperative Information

<table style="width:100%;">
<colgroup>
<col style="width: 41%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 2%" />
<col style="width: 3%" />
<col style="width: 2%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (666-00-0787) Case</p>
</blockquote></th>
<th><blockquote>
<p>#10146</p>
</blockquote></th>
<th><blockquote>
<p>PAGE:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>OF</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th rowspan="22"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>APR 6,2007 APPENDECTOMY</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p><span id="_bookmark175" class="anchor"></span>1. GENERAL: C. Current Pneumonia:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>A. Height: 58 INCHES 3. HEPATOBILIARY:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>B. Weight: A. Ascites:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>C. Diabetes - Long Term:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>D. Diabetes - 2 Wks Preop: 4. GASTROINTESTINAL:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>E. Tobacco Use: A. Esophageal Varices:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>F. Tobacco Use Timeframe: NOT APPLICABLE</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>G. ETOH &gt; 2 Drinks/Day: 5. CARDIAC:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>H. Positive Drug Screening: A. Congestive Heart Failure: 1</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>I. Dyspnea: B. Prior MI:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>J. Preop Sleep Apnea: LEVEL 3 C. PCI:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>K. Sleep Apnea-Compliance: &gt; OR EQUAL D. Prior Heart Surgery:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>L. DNR Status: E. Angina Severity:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>M. Functional Status: PARTIAL DEPENDENT F. Angina Timeframe:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>N. Current Residence: LONG TERM CARE G. Hypertension:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>O. Ambulation Device: AMB W/CANE</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>2. PULMONARY: 6. VASCULAR:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="6"><blockquote>
<p>A. Ventilator Dependent: A. PAD:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="6"><blockquote>
<p>B. History of Severe COPD: B. Rest Pain/Gangrene:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select Preoperative Information to Edit:</p>
</blockquote></th>
<th><blockquote>
<p><strong>A</strong></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 44%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
<p>JUN 23,1998 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th><blockquote>
<p>Case #63592</p>
</blockquote></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>GENERAL: <strong>YES</strong></p>
<p>Patient's Height 65 INCHES//: <strong>62</strong></p>
<p>Patient's Weight 140 POUNDS//: <strong>175</strong></p>
<p>Diabetes Mellitus: Chronic, Long-Term Management: <strong>I</strong> INSULIN Diabetes Mellitus: Management Prior to Surgery: <strong>I</strong> INSULIN Tobacco Use: <strong>2</strong> NO USE IN LAST 12 MOS</p>
<p>Tobacco Use Timeframe: NOT APPLICABLE// <strong>&lt;enter&gt;</strong></p>
<p>ETOH &gt;2 Drinks Per Day in the Two Weeks Prior to Admission: <strong>N</strong> NO Positive Drug Screening:</p>
<p>Dyspnea: <strong>N</strong></p>
</blockquote>
<ol type="1">
<li><p>NO</p></li>
<li><blockquote>
<p>NO STUDY Choose 1-2: 1 <strong>NO</strong></p>
</blockquote></li>
</ol>
<blockquote>
<p>Preoperative Sleep Apnea: LEVEL 1// 3 SLEEP APNEA CONFIRMED – LEVEL 3 Sleep Apnea-Compliance: ?</p>
<p>Enter the level of the patient's reported compliance with sleep apnea Treatment.</p>
<p>Choose from:</p>
</blockquote>
<ol type="1">
<li><p>NIGHTLY</p></li>
<li><p>&gt; OR EQUAL 4 TIMES A WEEK</p></li>
<li><p>&lt; 4 TIMES A WEEK</p></li>
<li><p>NOT DOCUMENTED</p></li>
</ol>
<blockquote>
<p>Sleep Apnea-Compliance: <strong>4</strong> NOT DOCUMENTED DNR Status (Y/N): <strong>N</strong> NO</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Functional Status at Evaluation for Surgery: <strong>1</strong> INDEPENDENT</p>
<p>Current Residence (w/in 30 days prior to surgery): LONG TERM CARE// <strong>&lt;Enter&gt;</strong></p>
<p>Ambulation Device: AMBULATES W/OUT ASSISTIVE DEVICE// <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>PULMONARY: <strong>NO</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>HEPATOBILIARY: <strong>NO</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>GASTRONINTESTINAL: <strong>NO</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>CARDIAC: <strong>NO</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>VASCULAR: <strong>NO</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821) Case #63592 PAGE: 2 OF 2</p>
<p>JUN 23,1998 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>RENAL: 3. NUTRITIONAL/IMMUNE/OTHER:</p>
<ol type="A">
<li><p>Acute Renal Failure: A. Disseminated Cancer:</p></li>
<li><p>Currently on Dialysis: B. Open Wound:</p></li>
<li><blockquote>
<p>Steroid Use for Chronic Cond.:</p>
</blockquote></li>
</ol></li>
<li><p>CENTRAL NERVOUS SYSTEM: D. Weight Loss &gt; 10%:</p>
<ol type="A">
<li><p>Impaired Sensorium: E. Bleeding Disorders: YES</p></li>
<li><p>Coma: F. Bleeding Risk Due to Medication</p></li>
<li><p>Hemiplegia: G. Transfusion &gt;4 RBC Units:</p></li>
<li><p>CVD Repair/Obstruct: H. Chemo for Malig Last 90 Days:</p></li>
<li><p>History of CVD: I. Radiotherapy W/I 90 Days:</p></li>
<li><p>Tumor Involving CNS: J. Preoperative Sepsis:</p></li>
<li><p>Impaired Cognitive Function K. Pregnancy</p>
<ol start="12" type="A">
<li><p>History of Cancer:</p></li>
<li><p>History of Radiation Therapy:</p></li>
<li><p>Num of Prior Surg in Same Op:</p></li>
</ol></li>
</ol></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Preoperative Information to Edit: 3E</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Laboratory Test Results (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA LAB\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the *Laboratory Test Results (Enter/Edit)* option to enter or edit preoperative and postoperative lab information for an individual risk assessment. The option is divided into the three features listed below. The first two features allow the user to merge (also called "capture" or "load") lab information into the risk assessment from the VistA software. The third feature provides a two-page summary of the lab profile and allows direct editing of the information.

1.  Capture Preoperative Laboratory Information
2.  Capture Postoperative Laboratory Information
3.  Enter, Edit, or Review Laboratory Test Results

> To "capture" preoperative lab data, the user must provide both the date and time the operation began. Likewise, to capture postoperative lab data, the user must provide both the date and time the operation was completed. If this information has already been entered, the system will not prompt for it again.

> If assistance is needed while interacting with the software, entering one or two question marks (??) will access the on-line help.

> Example 1: Capture Preoperative Laboratory Information

> Example 2: Capture Postoperative Laboratory Information

> Example 3: Enter, Edit, or Review Laboratory Test Results

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,FORTY (000-77-7777) Case #68112 PAGE: 1 OF 2 LATEST PREOP LAB RESULTS IN 90 DAYS PRIOR TO SURGERY UNLESS OTHERWISE SPECIFIED SEP 19,2003 CHOLEDOCHOTOMY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1. Anion Gap (in 48 hrs.): 12 (SEP 18,2003)</p>
<p>2. Serum Sodium: 139 (SEP 18,2003)</p>
<p>3. BUN: 13 (SEP 18,2003)</p>
</blockquote>
<ol start="4" type="1">
<li><p>Serum Creatinine: 1 (SEP 18,2003)</p></li>
<li><p>Serum Albumin: 4 (SEP 18,2003)</p></li>
<li><p>Total Bilirubin: .8 (SEP 18,2003)</p></li>
</ol>
<blockquote>
<p>7. SGOT: 29 (SEP 18,2003)</p>
<p>8. Alkaline Phosphatase: 120 (SEP 18,2003) 9. WBC: 12.8 (SEP 18,2003)</p>
<p>10. Hematocrit: 45.7 (SEP 18,2003)</p>
</blockquote>
<ol start="11" type="1">
<li><p>Platelet Count: NS</p></li>
<li><p>PTT: NS</p></li>
<li><p>PT: NS</p></li>
<li><p>INR: NS</p></li>
<li><p>Hemoglobin A1c (1000 days): NS</p></li>
</ol></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Preoperative Laboratory Information to Edit: <strong>11:13</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,FORTY (000-77-7777) Case #68112 PAGE: 1 OF 2 LATEST PREOP LAB RESULTS IN 90 DAYS PRIOR TO SURGERY UNLESS OTHERWISE SPECIFIED SEP 19,2003 CHOLEDOCHOTOMY</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1. Anion Gap (in 48 hrs.): 12 (SEP 18,2003)</p>
<p>2. Serum Sodium: 139 (SEP 18,2003)</p>
<p>3. BUN: 13 (SEP 18,2003)</p>
</blockquote>
<ol start="4" type="1">
<li><p>Serum Creatinine: 1 (SEP 18,2003)</p></li>
<li><p>Serum Albumin: 4 (SEP 18,2003)</p></li>
<li><p>Total Bilirubin: .8 (SEP 18,2003)</p></li>
</ol>
<blockquote>
<p>7. SGOT: 29 (SEP 18,2003)</p>
<p>8. Alkaline Phosphatase: 120 (SEP 18,2003) 9. WBC: 12.8 (SEP 18,2003)</p>
<p>10. Hematocrit: 45.7 (SEP 18,2003)</p>
<p>11. Platelet Count: 289 (SEP 18,2003)</p>
<p>12. PTT: 33.7 (SEP 18,2003)</p>
<p>13. PT: 11.8 (SEP 18,2003)</p>
</blockquote>
<ol start="14" type="1">
<li><p>INR: NS</p></li>
<li><p>Hemoglobin A1c (1000 days): NS</p></li>
</ol></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Preoperative Laboratory Information to Edit: <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 64%" />
<col style="width: 10%" />
<col style="width: 2%" />
<col style="width: 2%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,FORTY (000-77-7777) Case #68112 POSTOP LAB RESULTS WITHIN 30 DAYS AFTER SURGERY SEP 19,2003 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th><blockquote>
<p>PAGE:</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>OF 2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><ol type="1">
<li><p>Highest Anion Gap: 12 (SEP 20,2003)</p></li>
<li><p>Highest Serum Sodium: 139 (SEP 20,2003)</p></li>
<li><p>Lowest Serum Sodium: 135 (SEP 20,2003)</p></li>
<li><p>Highest Potassium: 4.4 (SEP 20,2003)</p></li>
<li><p>Lowest Potassium: 3.4 (SEP 20,2003)</p></li>
<li><p>Highest Serum Creatinine: 1.2 (SEP 20,2003)</p></li>
<li><p>Highest CPK: NS</p></li>
<li><p>Highest CPK-MB Band: NS</p></li>
<li><p>Highest Total Bilirubin: NS</p></li>
</ol>
<blockquote>
<p>10. Highest WBC: 11.8 (SEP 20,2003)</p>
</blockquote>
<ol start="11" type="1">
<li><p>Lowest Hematocrit: 40.3 (SEP 20,2003)</p></li>
<li><p>Highest Troponin I: 10.18 (SEP 24,2003)</p></li>
<li><p>Highest Troponin T: 12.13 (SEP 24,2003)</p></li>
</ol></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Select Postoperative Laboratory Information to Edit: <strong>2</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 1%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,FORTY (000-77-7777) POSTOP LAB RESULTS WITHIN 30 DAYS SEP 19,2003 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>Case #68112 AFTER SURGERY</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>PAGE:</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>2 OF 2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1. Highest Anion Gap:</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>20,2003)</p>
</blockquote></td>
<td rowspan="13"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2. Highest Serum Sodium:</p>
</blockquote></td>
<td><blockquote>
<p>144</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>21,2003)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3. Lowest Serum Sodium:</p>
</blockquote></td>
<td><blockquote>
<p>135</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>20,2003)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4. Highest Potassium:</p>
</blockquote></td>
<td><blockquote>
<p>4.4</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>20,2003)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5. Lowest Potassium:</p>
</blockquote></td>
<td><blockquote>
<p>3.4</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>20,2003)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ol start="6" type="1">
<li><p>Highest Serum Creatinine:</p></li>
<li><p>Highest CPK:</p></li>
</ol></td>
<td><blockquote>
<p>1.2</p>
<p>NS</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>20,2003)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8. Highest CPK-MB Band:</p>
</blockquote></td>
<td><blockquote>
<p>NS</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9. Highest Total Bilirubin:</p>
</blockquote></td>
<td><blockquote>
<p>NS</p>
</blockquote></td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10. Highest WBC:</p>
</blockquote></td>
<td><blockquote>
<p>11.8</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>20,2003)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11. Lowest Hematocrit:</p>
</blockquote></td>
<td><blockquote>
<p>40.3</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>20,2003)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12. Highest Troponin I:</p>
</blockquote></td>
<td><blockquote>
<p>10.18</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>24,2003)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13. Highest Troponin T:</p>
</blockquote></td>
<td><blockquote>
<p>12.13</p>
</blockquote></td>
<td>(SEP</td>
<td colspan="3"><blockquote>
<p>24,2003)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p>Select Postoperative Laboratory Information to Edit:</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Operation Information (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA OPERATION DATA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operation Information (Enter/Edit)* option is used to enter or edit information related to the operation. At the bottom of each page is a prompt to select one or more operative items to edit. If the user does not want to edit any items on the page, pressing the \<Enter\> key will exit the option. If they are not already there, it is important that the operation's beginning and ending times be entered so that the user can later enter postoperative information.

> About the "Select Operative Information to Edit:" Prompt

> The user should first enter the item number to edit at the "Select Operative Information to Edit:" prompt. To respond to every item on the page, the user should enter A for ALL or enter a range of numbers separated by a colon (:) to respond to a range of items.

> After the information has been entered or edited, the display will clear and present a summary. The summary organizes the information entered and provides another chance to enter or edit data. If information has been entered for the OTHER PROCEDURES field or the CONCURRENT PROCEDURES field, the summary will display \*\*\*INFORMATION ENTERED\*\*\* to the right of the items.

> If assistance is needed while interacting with the software, the user should enter one or two question marks (??) to receive on-line help.

> Example: Enter/Edit Operation Information

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 44%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (000-37-0555)</p>
</blockquote></th>
<th><blockquote>
<p>Case #264</p>
</blockquote></th>
<th rowspan="7"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Primary Surgeon: SURSURGEON,ONE</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>JUN 7,2005 ARTHROSCOPY, LEFT KNEE</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Wound Classification: CLEAN// <strong>CL</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>1 CLEAN</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>2 CLEAN/CONTAMINATED</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Choose 1-2: <strong>2</strong> CLEAN/CONTAMINATED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 19%" />
<col style="width: 23%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (000-37-0555)</p>
<p>Primary Surgeon: SURSURGEON,ONE JUN 7,2005 ARTHROSCOPY, LEFT KNEE</p>
</blockquote></th>
<th><blockquote>
<p>Case #264</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAGE: 1 OF 2</p>
<p>&gt;&gt; Coding Complete &lt;&lt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>Postop Diagnosis Code (ICD9): NOT ENTERED</p>
</blockquote>
<ol type="1">
<li><p>Surgical Specialty: ORTHOPEDICS</p></li>
<li><p>Principal Operation: ARTHROSCOPY, LEFT KNEE</p></li>
<li><p>CPT Codes (view only): 29873-LT</p></li>
<li><p>Other Procedures:</p></li>
<li><p>Concurrent Procedure:</p></li>
<li><p>PGY of Primary Surgeon:</p></li>
<li><p>Surgical Priority: ELECTIVE</p></li>
<li><p>Wound Classification: CLEAN/CONTAMINATED</p></li>
<li><p>ASA Classification: 2-MILD DISTURB.</p></li>
<li><p>Princ. Anesthesia Technique: GENERAL</p></li>
<li><p>RBC Units Transfused:</p></li>
<li><p>Intraop Disseminated Cancer: NO</p></li>
<li><p>Intraoperative Ascites NO</p></li>
</ol></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Operative Information to Edit:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 37%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 2%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (000-37-0555)</p>
<p>Primary Surgeon: SURSURGEON,ONE</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#264</p>
</blockquote></th>
<th rowspan="2"></th>
<th><blockquote>
<p>PAGE:</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>OF</p>
</blockquote></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th rowspan="10"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUN 7,2005 ARTHROSCOPY, LEFT KNEE</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>1. Patient in Room (PIR): JUN 07, 2005</p>
</blockquote></th>
<th><blockquote>
<p>07:00</p>
</blockquote></th>
<th rowspan="7"></th>
<th rowspan="7"></th>
<th rowspan="7"></th>
<th rowspan="7"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>2. Procedure/Surgery Start Time (PST): JUN 07, 2005</p>
</blockquote></th>
<th><blockquote>
<p>07:10</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>3. Procedure/Surgery Finish (PF): JUN 07, 2005</p>
</blockquote></th>
<th><blockquote>
<p>08:15</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>4. Patient Out of Room (POR): JUN 07, 2005</p>
</blockquote></th>
<th><blockquote>
<p>08:40</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>5. Anesthesia Start (AS): JUN 07, 2005</p>
</blockquote></th>
<th><blockquote>
<p>06:30</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>6. Anesthesia Finish (AF): JUN 07, 2005</p>
</blockquote></th>
<th><blockquote>
<p>09:00</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="3"><blockquote>
<p>7. Discharge from PACU (DPACU):</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="8"><blockquote>
<p>Select Operative Information to Edit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Patient Demographics (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA DEMOGRAPHICS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The surgical clinical nurse reviewer uses the *Patient Demographics (Enter/Edit)* option to capture patient demographic information from the Patient Information Management System (PIMS) record. The nurse reviewer can also enter, edit, and review this information. The demographic fields captured from PIMS are Race, Ethnicity, Hospital Admission Date, Hospital Discharge Date, Admission/Transfer Date, Discharge/Transfer Date, Observation Admission Date, Observation Discharge Date, and Observation Treating Specialty. With this option, the nurse reviewer can also edit the length of postoperative hospital stay, hospital admission status, and transfer status.

> ![](surgery-version-3-user-manual-updated-sr-3-184/050.png)The Race and Ethnicity information is displayed, but cannot be updated within this or any other Surgery package option.

> Example: Entering Patient Demographics

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 38%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (000-37-0555)</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#264</p>
</blockquote></th>
<th rowspan="17"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUN 7,2005 ARTHROSCOPY, LEFT</p>
</blockquote></th>
<th><blockquote>
<p>KNEE</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>1. Transfer Status: NOT TRANSFERRED</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>2. Observation Admission Date/Time: NA</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>3. Observation Discharge Date/Time: NA</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>4. Observation Treating Specialty: NA</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>5. Hospital Admission Date/Time: JUN 06, 2005@14:15</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>6. Admit/Transfer to Surgical Svc.: JUN 06, 2005@08:30</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>7. Discharge/Transfer to Chronic Care: JUN 21, 2005@11:32</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>8. DC/REL Destination:</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>9. Length of Postop Hospital Stay: 15 Days</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>10. Hospital Admission Status:: ADMISSION</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>11. Patient's Ethnicity: NOT HISPANIC OR LATINO</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>12. Patient's Race: AMERICAN INDIAN OR ALASKA NATIVE, ASIAN</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>13. Date of Death: NA</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>14. 30-Day Death: NO</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="4"><blockquote>
<p>Select number of item to edit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Intraoperative Occurrences (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO INTRAOP COMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The nurse reviewer uses the *Intraoperative Occurrences (Enter/Edit)* option to enter or change information related to intraoperative occurrences (called complications in earlier versions). Every occurrence entered must have a corresponding occurrence category. For a list of occurrence categories, enter a question mark (?) at the "Enter a New Intraoperative Occurrence:" prompt.

> After an occurrence category has been entered or edited, the screen will clear and present a summary. The summary organizes the information entered and provides another chance to enter or edit data.

> Example: Enter an Intraoperative Occurrence

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (000-37-0555) Case #264 JUN 7,2005 ARTHROSCOPY, LEFT KNEE</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>Occurrence Category: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted:</p></li>
<li><p>Outcome to Date:</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>4:5</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (000-37-0555) Case #264 JUN 7,2005 ARTHROSCOPY, LEFT KNEE</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>Occurrence Category: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted: CPR</p></li>
<li><p>Outcome to Date: IMPROVED</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Postoperative Occurrences (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO POSTOP COMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The nurse reviewer uses the *Postoperative Occurrences (Enter/Edit)* option to enter or change information related to postoperative occurrences (called complications in earlier versions). Every occurrence entered must have a corresponding occurrence category. For a list of occurrence categories, the user should enter a question mark (?) at the "Enter a New Postoperative Occurrence:" prompt.

> After an occurrence category has been entered or edited, the screen will clear and present a summary. The summary organizes the information entered and provides another chance to enter or edit data.

> Example: Enter a Postoperative Occurrence

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (000-37-0555) Case #264 JUN 7,2005 ARTHROSCOPY, LEFT KNEE</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: ACUTE RENAL FAILURE</p></li>
<li><p>Occurrence Category: ACUTE RENAL FAILURE</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted:</p></li>
<li><p>Outcome to Date:</p></li>
<li><p>Date Noted:</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>4</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 36%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (000-37-0555) JUN 7,2005 ARTHROSCOPY, LEFT</p>
</blockquote></th>
<th><blockquote>
<p>KNEE</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#264</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>Treatment Instituted: <strong>DIALYSIS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,EIGHT (000-37-0555) Case #264 JUN 7,2005 ARTHROSCOPY, LEFT KNEE</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: ACUTE RENAL FAILURE</p></li>
<li><p>Occurrence Category: ACUTE RENAL FAILURE</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted: DIALYSIS</p></li>
<li><p>Outcome to Date:</p></li>
<li><p>Date Noted:</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Update Status of Returns Within 30 Days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO UPDATE RETURNS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Status of Returns Within 30 Days* option is used to update the status of Returns to Surgery within 30 days of a surgical case.

> Example: Update Status of Returns

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
<p>JUN 23,2005 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th><blockquote>
<p>Case #62192</p>
</blockquote></th>
<th><blockquote>
<p>RETURNS</p>
</blockquote></th>
<th><blockquote>
<p>TO</p>
</blockquote></th>
<th><blockquote>
<p>SURGERY</p>
</blockquote></th>
<th></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>1. 07/06/05</p>
</blockquote></th>
<th><blockquote>
<p>REPAIR INGUINAL</p>
</blockquote></th>
<th><blockquote>
<p>HERNIA - UNRELATED</p>
</blockquote></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="2"></th>
<th rowspan="3"></th>
</tr>
<tr class="header">
<th><blockquote>
<p>2. 06/25/05</p>
</blockquote></th>
<th><blockquote>
<p>CHOLECYSTECTOMY</p>
</blockquote></th>
<th><blockquote>
<p>- UNRELATED</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select Number:</p>
</blockquote></th>
<th><blockquote>
<p><strong>2</strong></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
<p>JUN 23,2005 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th></th>
<th>Case</th>
<th><blockquote>
<p>#62192</p>
</blockquote></th>
<th><blockquote>
<p>RETURNS</p>
</blockquote></th>
<th><blockquote>
<p>TO</p>
</blockquote></th>
<th><blockquote>
<p>SURGERY</p>
</blockquote></th>
<th></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>2. 06/25/05 CHOLECYSTECTOMY</p>
</blockquote></th>
<th><blockquote>
<p>-</p>
</blockquote></th>
<th>UNRELATED</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th rowspan="2"></th>
</tr>
<tr class="header">
<th colspan="7"><blockquote>
<p>This return to surgery is currently defined as UNRELATED to the case selected. Do you want to change this status ? NO// <strong>Y</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 8%" />
<col style="width: 1%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,SIXTY (000-56-7821)</p>
<p>JUN 23,2005 CHOLEDOCHOTOMY</p>
</blockquote></th>
<th><blockquote>
<p>Case #62192</p>
</blockquote></th>
<th><blockquote>
<p>RETURNS</p>
</blockquote></th>
<th><blockquote>
<p>TO</p>
</blockquote></th>
<th><blockquote>
<p>SURGERY</p>
</blockquote></th>
<th></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>07/06/05 REPAIR INGUINAL</p></li>
<li><p>06/25/05 CHOLECYSTECTOMY</p></li>
</ol></th>
<th><blockquote>
<p>HERNIA - UNRELATED</p>
<p>- RELATED</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th rowspan="2"></th>
</tr>
<tr class="header">
<th colspan="5"><blockquote>
<p>Select Number:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Update Assessment Status to 'Complete'

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA COMPLETE ASSESSMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the *Update Assessment Status to 'Complete'* option to upgrade the status of an assessment to Complete. A complete assessment has enough information for it to be transmitted to the centers where data are analyzed. Only complete assessments are transmitted. This option also notifies the user if procedure (CPT) and diagnosis (ICD) coding has not been completed.

> After updating the status, the user can print the patient's entire Surgery Risk Assessment Report. This report can be copied to a screen or to a printer.

> Example : Update Assessment Status to COMPLETE

## Alert Coder Regarding Coding Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA CODE ISSUE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the nurse reviewer to send an alert to the coder when there may be an issue with the CPT codes or the Postoperative Diagnosis codes for a Surgery case. When this option is selected, the nurse reviewer can enter a free-text message that will be sent to the coder on record, as well as to a pre- defined mail group identified in the Surgery Site Parameter titled CODE ISSUE MAIL GROUP. The message will not be sent if there is no coder, or if the mail group is not defined.

> Example : Alert Coder Regarding Coding Issues

> *(This page included for two-sided copying.)*

# Cardiac Risk Assessment Information (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA CARDIAC ENTER/EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgical Clinical Nurse Reviewer uses the options within the *Cardiac Risk Assessment Information (Enter/Edit)* menu to create a new risk assessment for a cardiac patient. Cardiac cases are evaluated differently from non-cardiac cases, and the prompts are different. This option is also used to make changes to an assessment that has already been entered.

> The example below demonstrates how to create a new risk assessment for cardiac patients and get to the sub-option menu as follows.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Shortcut</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Option Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CLIN</p>
</blockquote></td>
<td><blockquote>
<p><em>Clinical Information (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LAB</p>
</blockquote></td>
<td><blockquote>
<p><em>Laboratory Test Results (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CATH</p>
</blockquote></td>
<td><blockquote>
<p><em>Enter Cardiac Catheterization &amp; Angiographic Data</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OP</p>
</blockquote></td>
<td><blockquote>
<p><em>Operative Risk Summary Data (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CARD</p>
</blockquote></td>
<td><blockquote>
<p><em>Cardiac Procedures Operative Data (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IO</p>
</blockquote></td>
<td><blockquote>
<p><em>Intraoperative Occurrences (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PO</p>
</blockquote></td>
<td><blockquote>
<p><em>Postoperative Occurrences (Enter/Edit)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>R</p>
</blockquote></td>
<td><blockquote>
<p><em>Resource Data</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>U</p>
</blockquote></td>
<td><blockquote>
<p><em>Update Assessment Status to 'COMPLETE'</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CODE</p>
</blockquote></td>
<td><blockquote>
<p><em>Alert Coder Regarding Coding Issues</em></p>
</blockquote></td>
</tr>
</tbody>
</table>

> These sub-options are used for entering more in-depth data for a case, and are described in this chapter.

## Creating a New Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Enter either the patient's name/patient ID (for example, SURPATIENT,NINETEEN) or the surgical case assessment number preceded by \# (for example, \#47063). If the patient has any previous assessments, they will be displayed. An asterisk (\*) indicates a cardiac case. The user can now choose to create a new assessment or edit one of the previously entered assessments.
2.  After choosing an operation on which to report, the user should respond YES to the prompt "Are you sure that you want to create a Risk Assessment for this surgical case ?" The user must answer YES (or press the \<Enter\> key to accept the YES default) to get to any of the sub-options. If the answer given is NO, the case created in step 1 will not be considered an assessment, although it can appear on some lists, and the software will return the user to the "Select Patient:" prompt.
3.  The screen will clear and present the sub-options menu. The user can select a sub-option now to enter more in-depth information for the case, or press the \<Enter\> key to return to the main menu.

> Example: Creating A New Risk Assessment (Cardiac)

## Clinical Information (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA CLINICAL INFORMATION\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Clinical Information (Enter/Edit)* option is used to enter the clinical information required for a cardiac risk assessment. The software will present one page; at the bottom of the page is a prompt to select one or more items to edit. If the user does not want to edit any items on the page, pressing the

> \<Enter\> key will advance the user to another option.

> About the "Select Clinical Information to Edit:" Prompt

> At the "Select Clinical Information to Edit:" prompt, the user should enter the item number to edit. The user can then enter an A for ALL to respond to every item on the page, or enter a range of numbers separated by a colon (:) to respond to a range of items.

> After the information has been entered or edited, the terminal display screen will clear and present a summary. The summary organizes the information entered and provides another chance to enter or edit data. If assistance is needed while interacting with the software, the user can enter one or two question marks (??) to receive on-line help.

> Example: Enter Clinical Information

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#60183</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAGE: 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><ol type="1">
<li><p><span id="_bookmark189" class="anchor"></span>Height: 70 in 17. PAD: NO</p></li>
<li><p>Weight: 185 lb 18. CVD Repair/Obstruct: NO CVD</p></li>
<li><p>Diabetes - Long Term: NO 19. History of CVD: NO CVD</p></li>
<li><p>Diabetes - 2 Wks Preop: NO 20. Angina Severity: NONE</p></li>
<li><p>COPD: NO 21. Angina Timeframe:W/N 14 DAY OF SU</p></li>
<li><p>FEV1: 9.3 liters 22. Congestive Heart Failure: 0</p></li>
<li><p>Cardiomegaly (X-ray): YES 23. Current Diuretic Use: NO</p></li>
<li><p>Tobacco Use: NEVER USED TOBACCO 24. IV NTG within 48 Hours: NO</p></li>
<li><p>Tobacco Use Timeframe: NOT APPLICABLE 25. Preop Circulatory Device: NONE</p></li>
<li><p>Positive Drug Screening: NOT DONE 26. Hypertension: NO</p></li>
<li><p>Active Endocarditis: NO 27. Preop Atrial Fibrillation: NO</p></li>
<li><p>Functional Status: INDEPENDENT 28. Preop Sleep Apnea: LEVEL 1</p></li>
<li><p>PCI: NONE 29. Sleep Apnea-Compliance:</p></li>
<li><p>Prior MI: UNKNOWN 30. Impaired Cognitive Func: 1</p></li>
<li><p>Num Prior Heart Surgeries:NONE</p></li>
<li><p>Prior Heart Surgery: NONE</p></li>
</ol></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Clinical Information to Edit:</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p><strong>A</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183 PAGE: 1 JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p>Height: 70 in 17. PAD: NO</p></li>
<li><p>Weight: 185 lb 18. CVD Repair/Obstruct: NO CVD</p></li>
<li><p>Diabetes - Long Term: NO 19. History of CVD: NO CVD</p></li>
<li><p>Diabetes - 2 Wks Preop: NO 20. Angina Severity: NONE</p></li>
<li><p>COPD: NO 21. Angina Timeframe: W/N 14</p></li>
<li><p>FEV1: 9.3 liters 22. Congestive Heart Failure: 0</p></li>
<li><p>Cardiomegaly (X-ray): YES 23. Current Diuretic Use: NO</p></li>
<li><p>Tobacco Use: NEVER USED TOBACCO 24. IV NTG within 48 Hours: NO</p></li>
<li><p>Tobacco Use Timeframe: NOT APPLICABLE 25. Preop Circulatory Device: NONE</p></li>
<li><p>Positive Drug Screening: NOT DONE 26. Hypertension: NO</p></li>
<li><p>Active Endocarditis: NO 27. Preop Atrial Fibrillation: NO</p></li>
<li><p>Functional Status: INDEPENDENT 28. Preop Sleep Apnea: LEVEL 3</p></li>
<li><p>PCI: NONE 29. Sleep Apnea-Compliance: &gt; OR EQUAL</p></li>
<li><p>Prior MI: UNKNOWN 30. Impaired Cognitive Func: 1</p></li>
<li><p>Num Prior Heart Surgeries:NONE</p></li>
<li><p>Prior Heart Surgeries: NONE</p></li>
</ol></td>
<td rowspan="2">DAY OF SU</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Clinical Information to Edit:</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Laboratory Test Results (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA LAB-CARDIAC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Laboratory Test Results (Edit/Edit)* option is used to enter or edit preoperative laboratory test results for an individual cardiac risk assessment. The option is divided into the two features listed below. The first feature allows the user to merge (also called "capture" or "load") lab information into the risk assessment from the VistA software. The second feature provides a two-page summary of the lab profile and allows direct editing of the information.

1.  Capture Laboratory Information
2.  Enter, Edit, or Review Laboratory Test Results

> To "capture" preoperative lab data, the user must provide both the date and time the operation began. If this information has already been entered, the system will not prompt for it again.

> If assistance is needed while interacting with the software, entering one or two question marks (??) allows the user to access the on-line help.

> About the "Select Laboratory Information to Edit:" Prompt

> At this prompt the user enters the item number to edit. Entering A for ALL allows the user to respond to every item on the page, or a range of numbers separated by a colon (:) can be entered to respond to a range of items.

> After the information has been entered or edited, the terminal display screen will clear and present a summary. The summary organizes the information entered and provides another chance to enter or edit data.

> Example: Enter Laboratory Test Results

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) PREOPERATIVE LABORATORY RESULTS</p>
<p>JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#60183</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAGE: 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1. HDL:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
<td rowspan="11"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2. LDL:</p>
</blockquote></td>
<td>168</td>
<td>(JAN</td>
<td colspan="3"><blockquote>
<p>2004)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3. Total Cholesterol:</p>
</blockquote></td>
<td>321</td>
<td>(JAN</td>
<td colspan="3"><blockquote>
<p>2004)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><ol start="4" type="1">
<li><p>Serum Triglyceride:</p></li>
<li><p>Serum Potassium:</p></li>
</ol></td>
<td><blockquote>
<p>&gt;70</p>
<p>NS</p>
</blockquote></td>
<td>(JAN</td>
<td colspan="3"><blockquote>
<p>2004)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6. Serum Bilirubin:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7. Serum Creatinine:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8. Serum Albumin:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9. Hemoglobin:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10. Hemoglobin A1c:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11. BNP:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td colspan="6"><blockquote>
<p>Select Laboratory Information to Edit: <strong>1</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 22%" />
<col style="width: 15%" />
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) PREOPERATIVE LABORATORY RESULTS</p>
<p>JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#60183</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAGE: 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HDL (mg/dl): NS// <strong>177</strong></p>
<p>HDL, Date: <strong>JAN, 2005</strong></p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>(JAN 2005)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 26%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) PREOPERATIVE LABORATORY RESULTS</p>
<p>JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#60183</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAGE: 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1. HDL:</p>
</blockquote></td>
<td>177</td>
<td>(JAN</td>
<td colspan="3"><blockquote>
<p>2005)</p>
</blockquote></td>
<td rowspan="12"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2. LDL:</p>
</blockquote></td>
<td>168</td>
<td>(JAN</td>
<td colspan="3"><blockquote>
<p>2004)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3. Total Cholesterol:</p>
</blockquote></td>
<td>321</td>
<td>(JAN</td>
<td colspan="3"><blockquote>
<p>2004)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4. Serum Triglyceride:</p>
</blockquote></td>
<td>&gt;70</td>
<td>(JAN</td>
<td colspan="3"><blockquote>
<p>2004)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5. Serum Potassium:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6. Serum Bilirubin:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7. Serum Creatinine:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8. Serum Albumin:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9. Hemoglobin:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10. Hemoglobin A1c:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11. BNP:</p>
</blockquote></td>
<td>NS</td>
<td></td>
<td colspan="3"></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>Select Laboratory Information to Edit:</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Enter Cardiac Catheterization & Angiographic Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA CATHETERIZATION\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Enter Cardiac Catheterization & Angiographic Data* option is used to enter or edit cardiac catheterization and angiographic information for a cardiac risk assessment. The software will present one page. At the bottom of the page is a prompt to select one or more items to edit. If the user does not want to edit any items on the page, pressing the \<Enter\> key will advance the user to another option.

> About the "Select Cardiac Catheterization and Angiographic Information to Edit:" Prompt

> At this prompt the user enters the item number to edit. Entering A for ALL allows the user to respond to every item on the page, or a range of numbers separated by a colon (:) can be entered to respond to a range of items.

> After the information has been entered or edited, the screen will clear and present a summary. The summary organizes the information entered and provides another chance to enter or edit data.

> Example: Enter Cardiac Catheterization & Angiographic Data

<table>
<colgroup>
<col style="width: 70%" />
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 2%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183 JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>PAGE:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th rowspan="3">OF 2</th>
</tr>
<tr class="odd">
<th colspan="4"><ol type="1">
<li><p>Procedure:</p></li>
<li><p>LVEDP:</p></li>
<li><p>Aortic Systolic Pressure:</p></li>
</ol>
<blockquote>
<p>For patients having right heart cath</p>
</blockquote>
<ol start="4" type="1">
<li><p>PA Systolic Pressure:</p></li>
<li><p>PAW Mean Pressure:</p></li>
<li><p>LV Contraction Grade (from contrast</p></li>
</ol>
<blockquote>
<p>or radionuclide angiogram or 2D echo):</p>
</blockquote>
<ol start="7" type="1">
<li><p>Mitral Regurgitation:</p></li>
<li><p>Aortic Stenosis:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Cardiac Catheterization and Angiographic Information to Edit:</p>
</blockquote></th>
<th><blockquote>
<p><strong>A</strong></p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 13%" />
<col style="width: 3%" />
<col style="width: 3%" />
<col style="width: 20%" />
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 2%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183 JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>PAGE:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th>OF 2</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p>Procedure:</p></li>
<li><p>LVEDP:</p></li>
<li><p>Aortic Systolic Pressure:</p></li>
</ol></td>
<td><blockquote>
<p>NS NS NS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p>For patients having right heart cath</p>
</blockquote>
<ol start="4" type="1">
<li><p>PA Systolic Pressure: NS</p></li>
<li><p>PAW Mean Pressure: NS</p></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>6. LV Contraction Grade (from contrast or radionuclide angiogram or 2D echo):</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>LV</p>
</blockquote></td>
<td><blockquote>
<p>STUDY</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="7" type="1">
<li><p>Mitral Regurgitation:</p></li>
<li><p>Aortic Stenosis:</p></li>
</ol></td>
<td><blockquote>
<p>NS NS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>Select Cardiac Catheterization and Angiographic Information to Edit:</p>
</blockquote></td>
<td><blockquote>
<p><strong>A</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 2%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#60183</p>
</blockquote></th>
<th><blockquote>
<p>PAGE:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>OF 2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li><p>Procedure:</p></li>
<li><p>LVEDP:</p></li>
<li><p>Aortic Systolic</p></li>
</ol></td>
<td><blockquote>
<p>Pressure:</p>
</blockquote></td>
<td><blockquote>
<p>Cath</p>
<p>56 mm</p>
<p>120 mm</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>Hg Hg</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p>For patients having right heart cath</p>
</blockquote>
<ol start="4" type="1">
<li><p>PA Systolic Pressure: 30 mm Hg</p></li>
<li><p>PAW Mean Pressure: 15 mm Hg</p></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="8"><blockquote>
<p>6. LV Contraction Grade (from contrast</p>
<p>or radionuclide angiogram or 2D echo): IIIa 0.40-0.44 MODERATE DYSFUNCTION A</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="8"><ol start="7" type="1">
<li><p>Mitral Regurgitation: MODERATE</p></li>
<li><p>Aortic Stenosis: MILD</p></li>
</ol></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="8"><blockquote>
<p>Select Cardiac Catheterization and Angiographic Information to Edit: <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 70%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183 JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th></th>
<th colspan="2"><blockquote>
<p>PAGE: 2 of 2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>----- Native Coronaries -----</p>
</blockquote></td>
<td rowspan="9"></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>1. Left main stenosis: NS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>2. LAD Stenosis: NS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>3. Right coronary stenosis: NS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>4. Circumflex Stenosis: NS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Cardiac Catheterization and Angiographic Information to Edit:</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>3</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Right Coronary Artery Stenosis: NS// <strong>?</strong></p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Enter the percent (0-100) stenosis.</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Right Coronary Artery Stenosis: NS// <strong>30</strong></p>
</blockquote></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th><blockquote>
<p>Case</p>
</blockquote></th>
<th><blockquote>
<p>#60183</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PAGE: 2 of 2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>----- Native Coronaries -----</p>
</blockquote></td>
<td colspan="4"></td>
<td rowspan="6"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1. Left main stenosis:</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>NS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2. LAD Stenosis:</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>NS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3. Right coronary stenosis:</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>30</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4. Circumflex Stenosis:</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>NS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>Select Cardiac Catheterization and Angiographic Information to Edit:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *(This page included for two-sided copying.)*

## Operative Risk Summary Data (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA CARDIAC OPERATIVE RISK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Operative Risk Summary Data (Enter/Edit)* option is used to enter or edit operative risk summary data for the cardiac surgery risk assessments. This option records the physician's subjective estimate of operative mortality. To avoid bias, this should be completed preoperatively. The software will present one page. At the bottom of the page is a prompt to select one or more items to edit. If the user does not want to edit any of the items, the \<Enter\> key can be pressed to proceed to another option.

> About the "Select Operative Risk Summary Information to Edit:" prompt

> At this prompt the user enters the item number to edit. Entering A for ALL allows the user to respond to every item on the page, or a range of numbers separated by a colon (:) can be entered to respond to a range of items.

> Example: Operative Risk Summary Data

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 3%" />
<col style="width: 15%" />
<col style="width: 6%" />
<col style="width: 1%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183</p>
</blockquote></th>
<th></th>
<th></th>
<th><blockquote>
<p>PAGE:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th rowspan="10"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>&gt;&gt; Coding Complete &lt;&lt;</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>1. ASA Classification: 1-NO DISTURB.</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>2. Surgical Priority:</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>3. Preoperative Risk Factors: NONE</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th></th>
<th></th>
<th><blockquote>
<p>This information</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>4. CPT Codes (view only): 33510</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>cannot be edited.</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
<tr class="header">
<th><blockquote>
<p>5. Wound Classification: CLEAN</p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Select Operative Risk Summary Information to Edit:</p>
</blockquote></th>
<th><blockquote>
<p><strong>1:3</strong></p>
</blockquote></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 4%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 1%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) JUN 18,2005 CORONARY ARTERY BYPASS</p>
<p>&gt;&gt; Coding Complete &lt;&lt;</p>
</blockquote></th>
<th>Case</th>
<th><blockquote>
<p>#60183</p>
</blockquote></th>
<th>PAGE:</th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="5"><ol type="1">
<li><p>ASA Classification: 3-SEVERE DISTURB.</p></li>
<li><p>Surgical Priority: EMERGENT (ONGOING ISCHEMIA)</p></li>
</ol>
<blockquote>
<p>A. Date/Time Collected: JUN 18,2005@18:15</p>
</blockquote>
<ol start="3" type="1">
<li><p>CPT Codes (view only): 33736</p></li>
<li><p>Wound Classification: CLEAN</p></li>
</ol></th>
</tr>
<tr class="header">
<th colspan="5"><blockquote>
<p>* NOTE: D/Time of Surgical Priority should be &lt; the D/Time Patient in OR.*</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="5"><blockquote>
<p>Select Operative Risk Summary Information to Edit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The Surgery software performs data checks on the following fields:

> ![](surgery-version-3-user-manual-updated-sr-3-184/051.png)The Date/Time Collected field for Physician's Preoperative Estimate of Operative Mortality should be earlier than the Time Pat In OR field. This field is no longer auto-populated.

> The Date/Time Collected field for Surgical Priority should be earlier than the Time Pat In OR field. This field is no longer auto-populated.

> If the date entered does not conform to the specifications, then the Surgery software displays a warning at the bottom of the screen.

## Cardiac Procedures Operative Data (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA CARDIAC PROCEDURES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Cardiac Procedures Operative Data (Enter/Edit)* option is used to enter or edit information related to cardiac procedures requiring cardiopulmonary bypass (CPB). The software will present two pages. At the bottom of the page is a prompt to select one or more items to edit. If the user does not want to edit any items on the page, pressing the \<Enter\> key will advance the user to another option.

> About the "Select Operative Information to Edit:" prompt

> At this prompt, the user enters the item number to edit. Entering A for ALL allows the user to respond to every item on the page, or a range of numbers separated by a colon (:) can be entered to respond to a range of items. You can also use number-letter combinations, such as 11B, to update a field within a group, such as VSD Repair.

> Each prompt at the category level allows for an entry of YES or NO. If NO is entered, each item under that category will automatically be answered NO. On the other hand, responding YES at the category level allows the user to respond individually to each item under the main category.

> After the information has been entered or edited, the terminal display screen will clear and present a summary. The summary organizes the information entered and provides another chance to enter or edit data.

> Example: Enter Cardiac Procedures Operative Data

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 50%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>Select Cardiac Risk Assessment Information (Enter/Edit) Option: <strong>CARD</strong> Cardiac Procedures Operative Data (Enter/Edit)</p>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183 PAGE: 1 JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Operative Data details:</p>
</blockquote></td>
<td rowspan="2">N/A (began on-pump/ stayed on-pump)</td>
<td rowspan="3"></td>
</tr>
<tr class="even">
<td><ol type="1">
<li><p>Bridge to Transplant:</p></li>
<li><p>Total CPB Time:</p></li>
<li><p>Total Ischemic Time:</p></li>
<li><p>Incision Type:</p></li>
<li><p>Convert Off Pump to CPB:</p></li>
</ol></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Select Operative Information to Edit:</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Page 474a removed.

> Page 474b has been deleted based on SR\*3\*184.

## Intraoperative Occurrences (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO INTRAOP COMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The nurse reviewer uses the *Intraoperative Occurrences (Enter/Edit)* option to enter or change information related to intraoperative occurrences. Every occurrence entered must have a corresponding occurrence category. For a list of occurrence categories, the user can enter a question mark (?) at the "Enter a New Intraoperative Occurrence:" prompt.

> After an occurrence category has been entered or edited, the screen will clear and present a summary. The summary organizes the information entered and provides another opportunity to enter or edit data.

> Example: Enter an Intraoperative Occurrence

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183 JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>Occurrence Category: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted:</p></li>
<li><p>Outcome to Date:</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>2:5</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 40%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354)</p>
</blockquote></th>
<th><blockquote>
<p>Case #60183</p>
</blockquote></th>
<th rowspan="8"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Occurrence Category: CARDIAC ARREST REQUIRING CPR</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>// <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>ICD Diagnosis Code: <strong>102.8</strong> 102.8 LATENT YAWS</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>...OK? YES// &lt;Enter&gt; (YES)</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Type of Treatment Instituted: <strong>CPR</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Outcome to Date: <strong>I</strong> IMPROVED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183 JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>Occurrence Category: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>ICD Diagnosis Code: 102.8</p></li>
<li><p>Treatment Instituted: CPR</p></li>
<li><p>Outcome to Date: IMPROVED</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 40%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354)</p>
</blockquote></th>
<th><blockquote>
<p>Case #60183</p>
</blockquote></th>
<th rowspan="6"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Enter/Edit Intraoperative Occurrences</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>1. CARDIAC ARREST REQUIRING CPR</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>Category: CARDIAC ARREST REQUIRING CPR</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>Select a number (1), or type 'NEW' to enter another occurrence:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Postoperative Occurrences (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO POSTOP COMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The nurse reviewer uses the *Postoperative Occurrences (Enter/Edit)* option to enter or change information related to postoperative occurrences. Every occurrence entered must have a corresponding occurrence category. For a list of occurrence categories, the user can enter a question mark (?) at the "Enter a New Postoperative Occurrence:" prompt.

> After an occurrence category has been entered or edited, the screen will clear and present a summary. The summary organizes the information entered and provides another opportunity to enter or edit data.

> Example: Enter a Postoperative Occurrence

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183 JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>Occurrence Category: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted:</p></li>
<li><p>Outcome to Date:</p></li>
<li><p>Date Noted:</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>4:6</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINETEEN (000-28-7354) Case #60183 JUN 18,2005 CORONARY ARTERY BYPASS</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Occurrence: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>Occurrence Category: CARDIAC ARREST REQUIRING CPR</p></li>
<li><p>ICD Diagnosis Code:</p></li>
<li><p>Treatment Instituted: CPR</p></li>
<li><p>Outcome to Date: IMPROVED</p></li>
<li><p>Date Noted: 06/19/05</p></li>
<li><p>Occurrence Comments:</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Occurrence Information: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Resource Data (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA CARDIAC RESOURCE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The nurse reviewer uses the *Resource Data (Enter/Edit)* option to enter, edit, or review risk assessment and cardiac patient demographic information such as hospital admission, discharge dates, and other information related to the surgical episode.

> Example: Resource Data (Enter/Edit)

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TEN (000-12-3456) Case #49413 PAGE: 1 OF 2 OCT 18,2007 CABG X3 USING LSVG TO OMB,LV EXT. OF RCA,LIMA TO LAD</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Transfer Status: NON-VAMC ACUTE CARE HOSPITAL</p></li>
<li><p>Hospital Admission Date:</p></li>
<li><p>Hospital Discharge Date:</p></li>
<li><p>DC/REL Destination: ACUTE CARE FACIL TRANSFER VA/NON-VA</p></li>
<li><p>Cardiac Catheterization Date: MAY 14, 2015@12:07</p></li>
<li><p>Time Patient In OR: OCT 03, 2007@08:00</p></li>
<li><p>Date/Time Operation Began: OCT 03, 2007@09:00</p></li>
<li><p>Date/Time Operation Ended: OCT 03, 2007@10:00</p></li>
<li><p>Time Patient Out OR: OCT 03, 2007@12:30</p></li>
<li><blockquote>
<p>Date/Time Patient Extubated: OCT 03, 2007@14:35 Postop Intubation Hrs: +2.1</p>
</blockquote></li>
<li><p>Date/Time Discharged from ICU:</p></li>
<li><p>Homeless: NO</p></li>
<li><p>Employment Status Preoperatively: NOT EMPLOYED</p></li>
<li><p>Date of Death: NA</p></li>
<li><p>30-Day Death: NO</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TEN (000-12-3456) Case #49413 PAGE: 2 OF 2 OCT 18,2007 CABG X3 USING LSVG TO OMB,LV EXT. OF RCA,LIMA TO LAD</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Current Residence: ACUTE CARE FACILITY</p></li>
<li><p>Ambulation Device: AMBULATES W/OUT ASSISTIVE DEVICE</p></li>
<li><p>History of Cancer: NO</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 30%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><ol start="4" type="1">
<li><p>History of Radiation</p></li>
<li><p>Num of Prior Surg in</p></li>
</ol></th>
<th><blockquote>
<p>Therapy: Same OP:</p>
</blockquote></th>
<th><blockquote>
<p>YES</p>
<p>&gt;5 PREVIOUS</p>
</blockquote></th>
<th><blockquote>
<p>SURGERIES</p>
</blockquote></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th colspan="4"><blockquote>
<p>Select Resource Information to Edit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The Surgery software performs data checks on the following fields:

> ![](surgery-version-3-user-manual-updated-sr-3-184/052.png)The Date/Time Patient Extubated field should be later than the Time Patient Out OR field, and earlier than the Date/Time Discharged from ICU field.

> The Date/Time Discharged from ICU field should be later than the Date/Time Patient Extubated field, and equal to or earlier than the Hospital Discharge Date field.

> If the date entered does not conform to the specifications, then the Surgery software displays a warning at the bottom of the screen.

> *(This page included for two-sided copying.)*

## Update Assessment Status to 'COMPLETE'

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA COMPLETE ASSESSMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Assessment Status to 'COMPLETE'* option is used to upgrade the status of an assessment to "Complete." A complete assessment has enough information for it to be transmitted to the centers where data are analyzed. Only complete assessments are transmitted. This option also notifies the user if procedure (CPT) and diagnosis (ICD) coding has not been completed.

> After updating the status, the user can print the patient's entire Surgery Risk Assessment Report. This report can be copied to a screen or to a printer.

> Example: Update Assessment Status to COMPLETE

## Alert Coder Regarding Coding Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA CODE ISSUE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the nurse reviewer to send an alert to the coder when there may be an issue with the CPT codes or the Postoperative Diagnosis codes for a Surgery case. When this option is selected, the nurse reviewer can enter a free-text message that will be sent to the coder on record, as well as to a pre- defined mail group identified in the Surgery Site Parameter titled CODE ISSUE MAIL GROUP. The message will not be sent if there is no coder, or if the mail group is not defined.

> Example : Alert Coder Regarding Coding Issues

> *(This page included for two-sided copying.)*

# Print a Surgery Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA PRINT ASSESSMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Print a Surgery Risk Assessment* option prints an entire Surgery Risk Assessment Report for an individual patient. This report can be displayed temporarily on a screen. As the report fills the screen, the user will be prompted to press the \<Enter\> key to go to the next page. A permanent record can be made by copying the report to a printer. When using a printer, the report is formatted slightly differently from the way it displays on the terminal.

> Example 1: Print Surgery Risk Assessment for a Non-Cardiac Case

> Select Surgery Risk Assessment Menu Option: P Print a Surgery Risk Assessment

> *printout follows*

> VA NON-CARDIAC RISK ASSESSMENT Assessment: 236 PAGE 1 FOR SURPATIENT,FORTY 000-77-7777 (COMPLETED)

> ================================================================================

> Medical Center: ALBANY

> Age: 81 Operation Date: JAN 09, 2006

> Sex: MALE Ethnicity: NOT HISPANIC OR LATINO Race: AMERICAN INDIAN OR ALASKA

> NATIVE, NATIVE HAWAIIAN OR OTHER PACIFIC ISLANDER, WHITE

> Transfer Status: NOT ENTERED

> Observation Admission Date: NA

> Observation Discharge Date: NA

> Observation Treating Specialty: NA

> Hospital Admission Date: NOV 27,2007 13:11 Hospital Discharge Date:

> Admitted/Transferred to Surgical Service: Discharged/Transferred to Chronic Care:

> DC/REL Destination: NOT ENTERED Hospital Admission Status:

> Assessment Completed by: SURNURSE,SEVEN PREOPERATIVE INFORMATION

> GENERAL: YES HEPATOBILIARY: YES

> Height: Ascites: YES Weight:

> <span id="_bookmark200" class="anchor"></span>Diabetes - Long Term: GASTROINTESTINAL:

> Diabetes - 2 Wks Preop: Esophageal Varices: NO Tobacco Use:

> Tobacco Use Timeframe: NOT APPLICABLE

> ETOH \> 2 Drinks/Day: NO CARDIAC:

> Positive Drug Screening: Congestive Heart Failure: N CARD DX, CHF Dyspnea: NO Prior MI:

> Preop Sleep Apnea: LEVEL 3 PCI:

> Sleep Apnea-Compliance: \> OR EQUA

> DNR Status: Prior Heart Surgery:

> Functional Status: Angina Severity: Current Residence: ACUTE CARE FACILITY Angina Timeframe: Ambulation Device: Hypertension:

> PULMONARY:

> Ventilator Dependent: VASCULAR:

> History of Severe COPD: PAD:

> Current Pneumonia: Rest Pain/Gangrene: PREOPERATIVE INFORMATION

> RENAL: NUTRITIONAL/IMMUNE/OTHER:

> Acute Renal Failure: Disseminated Cancer:

> Currently on Dialysis: Open Wound:

> Steroid Use for Chronic Cond.:

> CENTRAL NERVOUS SYSTEM: Weight Loss \> 10%:

> Impaired Sensorium: Bleeding Disorders: Bleeding Due To Med:

> Coma: Transfusion \> 4 RBC Units:

> Hemiplegia: Chemo for Malig Last 90 Days:

> CVD Repair/Obstruct: Radiotherapy W/I 90 Days:

> History of CVD: Preoperative Sepsis:

> Tumor Involving CNS: Pregnancy: NOT APPLICABLE Impaired Cognitive Function: History of Cancer: YES

> History of Radiation Therapy: Y Prior Surg in Same Operative:

> OPERATION DATE/TIMES INFORMATION

> Patient in Room (PIR): JUL 20,2007 07:00 Procedure/Surgery Start Time (PST): JUL 20,2007 07:30 Procedure/Surgery Finish (PF): JUL 20,2007 08:30 Patient Out of Room (POR): JUL 20,2007 08:40

> Anesthesia Start (AS): Anesthesia Finish (AF): Discharge from PACU (DPACU):

> Page 482a removed

> VA NON-CARDIAC RISK ASSESSMENT Assessment: 236 PAGE 2 FOR SURPATIENT,FORTY 000-77-7777 (COMPLETED)

> ================================================================================ OPERATIVE INFORMATION

> Surgical Specialty: GENERAL(OR WHEN NOT DEFINED BELOW)

> Principal Operation: APPENDECTOMY Procedure CPT Codes: 44950

> Concurrent Procedure:

> CPT Code: PGY of Primary Surgeon: 0

> Emergency Case (Y/N): NO

> Wound Classification: CONTAMINATED

> ASA Classification: 3-SEVERE DISTURB. Principal Anesthesia Technique: GENERAL

> RBC Units Transfused: 0 Intraop Disseminated Cancer: NO

> Intraoperative Ascites: NO

> PREOPERATIVE LABORATORY TEST RESULTS

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>Anion Gap:</th>
<th><blockquote>
<p>12</p>
</blockquote></th>
<th>(JAN</th>
<th><blockquote>
<p>7,2006)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Serum Sodium:</td>
<td><blockquote>
<p>144.6</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Serum Creatinine:</td>
<td><blockquote>
<p>.9</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>BUN:</td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Serum Albumin:</td>
<td><blockquote>
<p>3.5</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Total Bilirubin:</td>
<td><blockquote>
<p>.9</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SGOT:</td>
<td><blockquote>
<p>46</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Alkaline Phosphatase:</td>
<td><blockquote>
<p>34</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>White Blood Count:</td>
<td><blockquote>
<p>15.9</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Hematocrit:</td>
<td><blockquote>
<p>43.4</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Platelet Count:</td>
<td><blockquote>
<p>356</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PTT:</td>
<td><blockquote>
<p>25.9</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PT:</td>
<td><blockquote>
<p>12.1</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>INR:</td>
<td><blockquote>
<p>1.54</p>
</blockquote></td>
<td>(JAN</td>
<td><blockquote>
<p>7,2006)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Hemoglobin A1c:</td>
<td><blockquote>
<p>NS</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> POSTOPERATIVE LABORATORY RESULTS

> \* Highest Value

> \*\* Lowest Value

\* Anion Gap: 11 (JAN 7,2006)

\* Serum Sodium: 148 (JAN 12,2006)

\*\* Serum Sodium: 144.2 (FEB 2,2006)

\* Potassium: 4.5 (JAN 12,2006)

\*\* Potassium: 4.5 (JAN 12,2006)

\* Serum Creatinine: 1.4 (FEB 2,2006)

\* CPK: 88 (JAN 12,2006)

\* CPK-MB Band: \<1 (JAN 12,2006)

\* Total Bilirubin: 1.3 (JAN 12,2006)

\* White Blood Count: 12.2 (JAN 12,2006)

\*\* Hematocrit: 42.9 (JAN 12,2006)

\* Troponin I: 1.42 (JAN 12,2006)

> \* Troponin T: NS

> Page 483a removed.

> Example 2: Print Surgery Risk Assessment for a Cardiac Case

> Select Surgery Risk Assessment Menu Option: P Print a Surgery Risk Assessment

> *printout follows*

2.  <span id="_bookmark201" class="anchor"></span>CLINICAL DATA

> Gender: MALE Age: 67

> Height: 70 in Prior MI: UNKNOWN

> Weight: 185 lb Number of prior heart surgeries: NONE Diabetes - Long Term: NO Prior heart surgery: NONE Diabetes - 2 Wks Preop: NO PAD: NO COPD: NO CVD Repair/Obstruct: NO CVD

> FEV1: 9.3 liters History of CVD: NO CVD

> Cardiomegaly (X-ray): YES Angina Severity: NONE Tobacco Use: NEVER USED TOBACCO Angina Timeframe: W/N 14 DAY OF SURG Tobacco Use Timeframe: NOT APPLICABLE Congestive Heart Failure: 0-N CARD DX Positive Drug Screening: NOT DONE Current Diuretic Use: NO Active Endocarditis: NO IV NTG 48 Hours Preceding Surgery: NO Functional Status: INDEPENDENT Preop Circulatory Device: NONE PCI: NONE Hypertension: NO Preop Sleep Apnea: LEVEL 1 Preoperative Atrial Fibrillation: NO Sleep Apnea-Compliance: Impaired Cognitive Function: YES-DOCUMEN

3.  DETAILED LABORATORY INFO - PREOPERATIVE VALUES

> Creatinine: mg/dl (NS) T. Cholesterol: mg/dl (NS) Hemoglobin: mg/dl (NS) HDL: mg/dl (NS)

> Albumin: g/dl (NS) LDL: mg/dl (NS) Triglyceride: mg/dl (NS) Hemoglobin A1c: % (NS) Potassium: mg/L (NS) BNP: mg/dl (NS)

> T. Bilirubin: mg/dl (NS)

4.  CARDIAC CATHETERIZATION AND ANGIOGRAPHIC DATA Cardiac Catheterization Date:

> Procedure: Native Coronaries:

> LVEDP: mm Hg Left Main Stenosis: Aortic Systolic Pressure: mm Hg LAD Stenosis:

> Right Coronary Stenosis: For patients having right heart cath: Circumflex Stenosis:

> PA Systolic Pressure: mm Hg

> PAW Mean Pressure: mm Hg If a Re-do, indicate stenosis

> in graft to: LAD:

> Right coronary (include PDA): Circumflex:

> LV Contraction Grade (from contrast or radionuclide angiogram or 2D Echo): Grade Ejection Fraction Range Definition

> Mitral Regurgitation:

> Aortic stenosis:

5.  OPERATIVE RISK SUMMARY DATA ASA Classification:

> Surgical Priority:

> Principal CPT Code: CPT Code Missing Other Procedures CPT Codes:

> Wound Classification:

> *(This page included for two-sided copying.)*

# Update Assessment Completed/Transmitted in Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA TRANSMITTED IN ERROR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update Assessment Completed/Transmitted in Error* option is used to change the status of a completed or transmitted assessment that contains errors or has been entered in error. The status will change from Completed or Transmitted to Incomplete so that the user can edit the assessment.

> Transmitted assessments will be re-transmitted if they are re-completed within 14 days of the original transmission date.

> Example: Update Assessment Completed/Transmitted in Error

> *(This page included for two-sided copying.)*

# List of Surgery Risk Assessments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA ASSESSMENT LIST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *List of Surgery Risk Assessments* option is used to print lists of assessments within a date range. Lists of assessments in different phases of completion (for example, incomplete, completed, or transmitted) or a list of all surgical cases entered in the Surgery Risk Assessment software can be printed. The user can also request that the list be sorted by surgical service. The software will prompt for a beginning date and an ending date. The examples in this section illustrate printing assessments in the following formats.

1.  List of Incomplete Assessments
2.  List of Completed Assessments
3.  List of Transmitted Assessments
4.  List of Non-Assessed Major Surgical Cases
5.  List of All Major Surgical Cases
6.  List of All Surgical Cases
7.  List of Completed/Transmitted Assessments Missing Information
8.  List of 1-Liner Cases Missing Information
9.  List of Eligible Cases
10. List of Cases With No CPT Codes
11. Summary List of Assessed Cases

> Example 1: List of Incomplete Assessments

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

> printout follows

> INCOMPLETE RISK ASSESSMENTS PAGE 1

> MAYBERRY, NC

> SURGERY SERVICE DATE REVIEWED: FROM: JAN 1,2006 TO: JUN 30,2006 REVIEWED BY:

> ASSESSMENT \# PATIENT OPERATIVE PROCEDURE(S) ANESTHESIA TECHNIQUE OPERATION DATE SURGEON

> ====================================================================================================================================

> \*\* SURGICAL SPECIALTY: CARDIAC SURGERY \*\*

> 28519 SURPATIENT,NINE 000-34-5555 \* CABG X3 (2V,1A) GENERAL JAN 05, 2006 SURSURGEON,ONE

> CPT Codes: 33736

> \*\* SURGICAL SPECIALTY: GENERAL(OR WHEN NOT DEFINED BELOW) \*\*

> 63063 SURPATIENT,ONE 000-44-7629 INGUINAL HERNIA SPINAL

> JUN 09, 2006 SURSURGEON,TWO

> CPT Codes: 49521

> \*\* SURGICAL SPECIALTY: NEUROSURGERY \*\*

> 63154 SURPATIENT,EIGHT 000-37-0555 CRANIOTOMY NOT ENTERED

> JUN 24, 2006 SURSURGEON,FOUR

> CPT Codes: NOT ENTERED

> Example 2: List of Completed Assessments

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

> *printout follows*

> COMPLETED RISK ASSESSMENTS PAGE 1

> MAYBERRY, NC

> SURGERY SERVICE DATE REVIEWED: FROM: JAN 1,2006 TO: JUN 30,2006 REVIEWED BY:

> ASSESSMENT \# PATIENT DATE COMPLETED ANESTHESIA TECHNIQUE OPERATION DATE OPERATIVE PROCEDURE

> ====================================================================================================================================

> \*\* SURGICAL SPECIALTY: GENERAL(OR WHEN NOT DEFINED BELOW) \*\*

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 37%" />
<col style="width: 29%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>92</p>
<p>FEB 23, 2006</p>
</blockquote></th>
<th><blockquote>
<p>SURPATIENT,SIXTY 000-56-7821</p>
<p>CHOLEDOCHOTOMY</p>
</blockquote></th>
<th><blockquote>
<p>FEB 28, 2006</p>
</blockquote></th>
<th>GENERAL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CPT Code: 47420</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63045</p>
<p>MAR 01, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FORTYONE 000-43-2109 INGUINAL HERNIA</p>
<p>CPT Code: 49521</p>
</blockquote></td>
<td><blockquote>
<p>MAR 29, 2006</p>
</blockquote></td>
<td>GENERAL</td>
</tr>
</tbody>
</table>

> \*\* SURGICAL SPECIALTY: OPHTHALMOLOGY \*\*

> 1898 SURPATIENT,FORTYONE 000-43-2109 MAY 28, 2006 GENERAL

> APR 28, 2006 INTRAOCCULAR LENS

> CPT Codes: NOT ENTERED

> Example 3: List of Transmitted Assessments

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

#### printout follows 

> TRANSMITTED RISK ASSESSMENTS PAGE 1

> MAYBERRY, NC

> SURGERY SERVICE DATE REVIEWED: OPERATION DATES FROM: JAN 1,2006 TO: JUN 30,2006 REVIEWED BY:

> ASSESSMENT \# PATIENT TRANSMISSION DATE ANESTHESIA TECHNIQUE OPERATION DATE PRINCIPAL OPERATIVE PROCEDURE

> ====================================================================================================================================

> \*\* SURGICAL SPECIALTY: GENERAL(OR WHEN NOT DEFINED BELOW) \*\*

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 32%" />
<col style="width: 25%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><p>63076</p>
<p>JAN 08, 2006</p></th>
<th><blockquote>
<p>SURPATIENT,FOURTEEN 000-45-7212</p>
<p>INGUINAL HERNIA</p>
</blockquote></th>
<th><blockquote>
<p>FEB 12, 2006</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CPT Codes: 49521</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>63077</p>
<p>FEB 08, 2006</p></td>
<td><blockquote>
<p>SURPATIENT,FIVE 000-58-7963 INGUINAL HERNIA, OTHER PROC1 CPT Codes: NOT ENTERED</p>
</blockquote></td>
<td><blockquote>
<p>FEB 30, 2006</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>63103</p>
<p>MAR 27, 2006</p></td>
<td><blockquote>
<p>SURPATIENT,NINE 000-34-5555 INGUINAL HERNIA</p>
<p>CPT Codes: 49521</p>
</blockquote></td>
<td><blockquote>
<p>APR 09, 2006</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>63171</p>
<p>MAY 17, 2006</p></td>
<td><blockquote>
<p>SURPATIENT,FIFTYTWO 000-99-8888 CHOLECYSTECTOMY</p>
<p>CPT Codes: 47600</p>
</blockquote></td>
<td><blockquote>
<p>JUN 05, 2006</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example 4: List of Non-Assessed Major Surgical Cases

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

> Page 496 has been deleted. *The List of Non-Assessed Major Surgical Cases* has been removed with patch SR\*3\*184.

> Example 5: List of All Major Surgical Cases

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

> Page 498 has been deleted. The *List of All Major Surgical Cases* has been removed with patch SR\*3\*184.

> Example 6: List of All Surgical Cases

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

#### printout follows 

> ALL SURGICAL CASES BY SURGICAL SPECIALTY PAGE 1 MAYBERRY, NC

> SURGERY SERVICE DATE REVIEWED: FROM: JAN 1,2006 TO: JUN 30,2006 REVIEWED BY:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 32%" />
<col style="width: 29%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CASE #</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
</blockquote></th>
<th><blockquote>
<p>ASSESSMENT STATUS</p>
</blockquote></th>
<th><blockquote>
<p>ANESTHESIA TECHNIQUE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OPERATION DATE</p>
</blockquote></td>
<td><blockquote>
<p>PRINCIPAL OPERATIVE PROCEDURE</p>
</blockquote></td>
<td><blockquote>
<p>EXCLUSION CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>SURGEON</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ==================================================================================================================================== SURGICAL SPECIALTY: GENERAL(OR WHEN NOT DEFINED BELOW)

> 63110 SURPATIENT,SIXTY 000-56-7821 COMPLETED GENERAL

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 35%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>JAN 23, 2006</p>
</blockquote></th>
<th><blockquote>
<p>CHOLEDOCHOTOMY CPT Code: 47420</p>
</blockquote></th>
<th><blockquote>
<p>10% RULE</p>
</blockquote></th>
<th><blockquote>
<p>SURSURGEON,TWO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>63079</p>
<p>APR 02, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTYTWO 000-99-8888 INGUINAL HERNIA</p>
<p>CPT Codes: NOT ENTERED</p>
</blockquote></td>
<td><blockquote>
<p>INCOMPLETE</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL SURSURGEON,ONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63131</p>
<p>APR 21, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTYTWO 000-99-8888 PERINEAL WOUND EXPLORATION</p>
<p>CPT Codes: NOT ENTERED</p>
</blockquote></td>
<td><blockquote>
<p>NO ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>GENERAL SURSURGEON,NINE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63180</p>
<p>JUN 23, 2006</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,SIXTY 000-56-7821 CHOLECYSTECTOMY</p>
<p>CPT Codes: 47600</p>
</blockquote></td>
<td><blockquote>
<p>NO ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>NOT ENTERED SURSURGEON,ONE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TOTAL GENERAL(OR WHEN NOT DEFINED BELOW): 4

> Example 7: List of Completed/Transmitted Assessments Missing Information

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

#### printout follows 

COMPLETED/TRANSMITTED ASSESSMENTS MISSING INFORMATION PAGE 1

> MAYBERRY, NC

> FROM: JAN 1,2006 TO: JUN 30,2006 DATE PRINTED: JUL 13,2006

> \*\* GENERAL(OR WHEN NOT DEFINED BELOW)

<table style="width:100%;">
<colgroup>
<col style="width: 20%" />
<col style="width: 44%" />
<col style="width: 18%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>ASSESSMENT #</p>
<p>OPERATION DATE</p>
</blockquote></th>
<th><blockquote>
<p>PATIENT</p>
<p>OPERATION(S)</p>
</blockquote></th>
<th><blockquote>
<p>TYPE</p>
</blockquote></th>
<th><blockquote>
<p>STATUS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>================================================================================</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>63172</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,FIFTYTWO 000-99-8888</p>
</blockquote></td>
<td><blockquote>
<p>NON-CARDIAC</p>
</blockquote></td>
<td><blockquote>
<p>TRANSMITTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MAY 17, 2006</p>
</blockquote></td>
<td><blockquote>
<p>REPAIR ARTERIAL BLEEDING</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> CPT Code: 33120

> Missing information:

1.  The final coding for Procedure and Diagnosis is not complete.
2.  Anesthesia Technique

> 63185 SURPATIENT,SIXTEEN 000-11-1111 NON-CARDIAC TRANSMITTED

> APR 17, 2006 INGUINAL HERNIA, CHOLECYSTECTOMY

> Missing information:

1.  The final coding for Procedure and Diagnosis is not complete.
2.  Concurrent Case
3.  History of COPD (Y/N)
4.  Ventilator Dependent Greater than 48 Hrs (Y/N)
5.  Weight Loss \> 10% of Usual Body Weight (Y/N)
6.  Transfusion Greater than 4 RBC Units this Admission (Y/N)

> 63080 SURPATIENT,THIRTY 000-82-9472 EXCLUDED COMPLETE

> JAN 03, 2006 TURP

> Missing information:

> 1\. The final coding for Procedure and Diagnosis is not complete.

> TOTAL FOR GENERAL(OR WHEN NOT DEFINED BELOW): 3 TOTAL FOR ALL SPECIALTIES: 3

> Example 8: List of 1-Liner Cases Missing Information

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

> Print the List of Assessments to which Device: \[Select Print Device\]

> printout follows -

> 1-LINER CASES MISSING INFORMATION PAGE 1 MABERRY, NC

> FROM: FEB 27,2006 TO: JUN 30,2006 DATE PRINTED: JUN 30,2006

> \*\* UROLOGY

> CASE \# PATIENT TYPE STATUS OP DATE OPERATION(S)

> ================================================================================

> 317 SURPATIENT,FOURTEEN 000-45-7212 CARDIAC COMPLETE APR 10, 2006 Vasectomy

> CPT Codes: NOT ENTERED

> Missing information:

1.  The final coding for Procedure and Diagnosis is not complete.
2.  Attending Code
3.  Wound Classification
4.  ASA Class

> TOTAL FOR UROLOGY: 1

> Example 9: List of Eligible Cases

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

> Print the List of Assessments to which Device: \[Select Print Device\]

> *printout follows*

> \>\>\> CARDIAC SURGERY

> CASES ELIGIBLE FOR ASSESSMENT PAGE 1 MAYBERRY, NC

> FROM: JUN 1,2006 TO: JUN 30,2007 DATE PRINTED: JUN 30,2007

> '\*' Denotes Eligible CPT Code

> \>\>\> Final CPT Coding is not complete. CPT Codes: \*33510, \*33511

> ===

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 43%" />
<col style="width: 20%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><p>10084</p>
<p>JUL 08, 2006</p></th>
<th><blockquote>
<p>SURPATIENT,NINE 000-34-5555 CABG</p>
</blockquote></th>
<th><blockquote>
<p>CARDIAC</p>
</blockquote></th>
<th><blockquote>
<p>COMPLETE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4">CPT Codes: *33502, 11402</td>
</tr>
<tr class="even">
<td><p>10380</p>
<p>FEB 06, 2007</p></td>
<td><blockquote>
<p>SURPATIENT,THREE 000-21-2453 CORONARY ARTERY BYPASS</p>
</blockquote></td>
<td><blockquote>
<p>NOT LOGGED</p>
</blockquote></td>
<td><blockquote>
<p>COMPLETE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4">CPT Codes: NOT ENTERED</td>
</tr>
<tr class="even">
<td><p>10383</p>
<p>FEB 08, 2007</p></td>
<td><blockquote>
<p>SURPATIENT,ONE 000-44-7629 STENT</p>
</blockquote></td>
<td><blockquote>
<p>NON-CARDIAC</p>
</blockquote></td>
<td><blockquote>
<p>COMPLETE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CPT Codes: NOT ENTERED

> TOTAL FOR CARDIAC SURGERY: 4

> \>\>\> GENERAL SURGERY

===

> \>\>\> Final CPT Coding is not complete. CPT Codes: \*44955, \*38100

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 44%" />
<col style="width: 17%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>10079</th>
<th><blockquote>
<p>SURPATIENT,SEVENTY 000-00-0125</p>
</blockquote></th>
<th><blockquote>
<p>EXCLUDED</p>
</blockquote></th>
<th><blockquote>
<p>COMPLETE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MAR 31, 2007</td>
<td><blockquote>
<p>HERNIA</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> \>\>\> Final CPT Coding is not complete. CPT Codes: \*49521, \*49521

> TOTAL FOR GENERAL SURGERY: 2

> Example 10: List of Cases With No CPT Codes

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

#### printout follows 

> \>\>\> CARDIAC SURGERY

> CASES WITHOUT CPT CODES PAGE 1 ALBANY - ALL DIVISIONS

> FROM: JAN 1,2007 TO: JAN 23,2008 DATE PRINTED: JAN 23,2008

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 42%" />
<col style="width: 19%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CASE # OP DATE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>PATIENT OPERATION(S)</p>
</blockquote></th>
<th><blockquote>
<p>TYPE</p>
</blockquote></th>
<th><blockquote>
<p>STATUS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><blockquote>
<p>================================================================================</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10429</p>
<p>FEB 12,</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TEN 666-12-3456 CABG</p>
</blockquote></td>
<td><blockquote>
<p>CARDIAC</p>
</blockquote></td>
<td><blockquote>
<p>COMPLETE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10420</p>
<p>FEB 12,</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,F. 666-00-0804 CABG</p>
</blockquote></td>
<td><blockquote>
<p>CARDIAC</p>
</blockquote></td>
<td><blockquote>
<p>TRANSMITTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10423</p>
<p>MAR 12,</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,TWO 666-45-1982</p>
<p>cabg</p>
</blockquote></td>
<td><blockquote>
<p>CARDIAC</p>
</blockquote></td>
<td><blockquote>
<p>INCOMPLETE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10430</p>
<p>MAR 18,</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,EIGHT 666-37-0555 CABG X3</p>
</blockquote></td>
<td><blockquote>
<p>CARDIAC</p>
</blockquote></td>
<td><blockquote>
<p>INCOMPLETE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10374</p>
<p>MAY 10,</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td><blockquote>
<p>SURPATIENT,NINE 666-34-5555</p>
<p>CABG X 3</p>
</blockquote></td>
<td><blockquote>
<p>NOT LOGGED</p>
</blockquote></td>
<td><blockquote>
<p>NO ASSESSMENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TOTAL FOR CARDIAC SURGERY: 5 TOTAL FOR ALL SPECIALTIES: 5

> Example 11: Summary List of Assessed Cases

> Select Surgery Risk Assessment Menu Option: L List of Surgery Risk Assessments

> SUMMARY LIST OF ASSESSED CASES PAGE 1 ALBANY

> FROM: JAN 1,2001 TO: JAN 23,2008 DATE PRINTED: JAN 23,2008

> SURGICAL SPECIALTY INCOMPLETE \| COMPLETE \| TRANSMITTED \| EXCLUDED

> ================================================================================

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 19%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 15%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CARDIAC SURGERY</p>
</blockquote></th>
<th></th>
<th>8</th>
<th>1</th>
<th>1</th>
<th>0</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GENERAL SURGERY</p>
</blockquote></td>
<td></td>
<td>17</td>
<td>1</td>
<td>1</td>
<td>6</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NEUROSURGERY</p>
</blockquote></td>
<td></td>
<td>1</td>
<td>0</td>
<td>1</td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OPHTHALMOLOGY</p>
</blockquote></td>
<td></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORTHOPEDICS</p>
</blockquote></td>
<td></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OTORHINOLARYNGOLOGY</p>
</blockquote></td>
<td><blockquote>
<p>(ENT)</p>
</blockquote></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PLASTIC SURGERY (INCLUDES HEAD</p>
</blockquote></td>
<td>2</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>TWO GENERAL</p>
</blockquote></td>
<td>1</td>
<td>0</td>
<td>0</td>
<td>0</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>UROLOGY</p>
</blockquote></td>
<td>0</td>
<td>0</td>
<td>0</td>
<td>1</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>TOTAL FOR ALL SPECIALTIES:</p>
</blockquote></td>
<td>34</td>
<td>2</td>
<td>3</td>
<td>7</td>
</tr>
</tbody>
</table>

# Print 30 Day Follow-up Letters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA REPRINT LETTERS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Surgical Clinical Nurse Reviewer uses the *Print 30 Day Follow-up Letters* option to automatically print a letter, or a batch of letters, addressed to a specific patient or patients.

> About the "Do you want to print the letter for a specific assessment?" Prompt

> The user responds YES to this prompt in order to print a follow-up letter for a single assessment. The software will ask the user to select the patient and case for which the letter will be printed. See Example 1 below.

> The user responds NO to this prompt if he or she wants to print a batch of follow-up letters for surgical cases within a data range. The software will ask for the beginning and ending dates of the date range for which the letters will be printed. See Example 2 on the following pages.

> ![](surgery-version-3-user-manual-updated-sr-3-184/053.png)If the patient has died, the software notifies the user of the death, and will not print the letter. Also, if a patient has not been discharged, the follow up letter will not print.

> Example 1: Print a Single Follow-up Letter

> *printout follows*

> NINETEEN SURPATIENT JUL 18, 2006

> Operation Date: 06/18/06 Specialty: GENERAL SURGERY

> Dear Mr. Surpatient,

> One month ago, you had an operation at the VA Medical Center. We are interested in how you feel. Have you had any health problems since your operation ? We would like to hear from you. Please take a few minutes to answer these questions and return this letter in the self-addressed stamped envelope.

> Have you been to a hospital or seen a doctor for any reason since your operation ? Yes No

> If you answered NO, you do not need to answer any more questions. Please return this sheet in the self-addressed stamped envelope.

> If you have answered YES, please answer the following questions.

1.  Have you been seen in an outpatient clinic or doctor's office ?

> Yes No

> Why did you go to the clinic or doctor's office ?

> Where ? (name and location) Date ?

> Who was your doctor ?

2.  Were you admitted to a hospital ? Yes No

> Why did you go to the hospital ?

> Where ? (name and location) Date ?

> Who was your doctor ?

> Please return this letter whether or not you have had any medical problems. Your health and opinion are important to us. Thank you.

> Sincerely,

> Surgical Clinical Nurse Reviewer

> Example 2: Print Letters Within a Date Range

> Select Surgery Risk Assessment Menu Option: P Print 30 Day Follow-up Letters

#### printout follows 

> FORTYONE SURPATIENT JUN 02, 2007

> 87 NORTH STREET Operation Date: 05/08/07

> PHILADELPHIA, PA 91776 Specialty: GENERAL SURGERY

> Dear Mr. Surpatient,

> One month ago, you had an operation at the VA Medical Center. We are interested in how you feel. Have you had any health problems since your operation ? We would like to hear from you. Please take a few minutes to answer these questions and return this letter in the self-addressed stamped envelope.

> Have you been to a hospital or seen a doctor for any reason since your operation ? Yes No

> If you answered NO, you do not need to answer any more questions. Please return this sheet in the self-addressed stamped envelope.

> If you have answered YES, please answer the following questions.

1)  Have you been seen in an outpatient clinic or doctor's office ?

> Yes No

> Why did you go to the clinic or doctor's office ?

> Where ? (name and location) Date ?

> Who was your doctor ?

2)  Were you admitted to a hospital ? Yes No

> Why did you go to the hospital ?

> Where ? (name and location) Date ?

> Who was your doctor ?

> Please return this letter whether or not you have had any medical problems. Your health and opinion are important to us. Thank You.

> Sincerely,

> Surgical Clinical Nurse Reviewer

# Exclusion Criteria (Enter/Edit)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SR NO ASSESSMENT REASON\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Exclusion Criteria (Enter/Edit)* option is used to flag major cases that will not have a surgery risk assessment due to certain exclusion criteria. At the prompt "Reason an Assessment was not Created:" enter a question mark (?) to see a list of reasons.

> Example: Enter Reason for No Assessment

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,NINE (000-34-5555) Case #63159</p>
<p>Transmission Status: QUEUED TO TRANSMIT NOV 1,2004 TURP (CPT Code: 52601-59)</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Exclusion Criteria: 10% RULE</p></li>
<li><p>Surgical Priority: ELECTIVE</p></li>
<li><p>Surgical Specialty: UROLOGY</p></li>
<li><p>Principal Anesthesia Technique: GENERAL</p></li>
<li><p>Major or Minor: MAJOR</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select Excluded Case Information to Edit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Monthly Surgical Case Workload Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA MONTHLY WORKLOAD REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Monthly Surgical Case Workload Report* option generates the Monthly Surgical Case Workload Report that may be printed and/or transmitted to the VASQIP national database. The report can be printed for a specific month, or for a range of months.

> Example: Monthly Surgical Case Workload Report – Single Month

> Select Surgery Risk Assessment Menu Option: M Monthly Surgical Case Workload Report

> *printout follows*

> MAYBERRY, NC

> REPORT OF MONTHLY SURGICAL CASE WORKLOAD FOR MAY 2007

<table>
<colgroup>
<col style="width: 75%" />
<col style="width: 8%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>TOTAL CASES PERFORMED</p>
</blockquote></th>
<th><blockquote>
<p>=</p>
</blockquote></th>
<th><blockquote>
<p>249</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TOTAL ELIGIBLE CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>227</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CASES MEETING EXCLUSION CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>114</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NON-SURGEON CASE</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>55</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EXCEEDS MAX. ASSESSMENTS</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EXCEEDS MAXIMUM TURPS</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>INCLUSION CRTA NOT MET</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>59</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10% RULE</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CONCURRENT CASE</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EXCEEDS MAXIMUM HERNIAS</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ABORTED</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ASSESSED CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>135</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NOT LOGGED ELIGIBLE CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CARDIAC CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NON-CARDIAC CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>119</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ASSESSED CASES PER DAY</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td><blockquote>
<p>6.75</p>
</blockquote></td>
</tr>
</tbody>
</table>

> NUMBER OF INCOMPLETE ASSESSMENTS REMAINING FOR PAST YEAR

> CARDIAC NON-CARDIAC TOTAL

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 25%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MAY</p>
</blockquote></th>
<th><blockquote>
<p>2006</p>
</blockquote></th>
<th>0</th>
<th></th>
<th>0</th>
<th></th>
<th><blockquote>
<p>0</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>JUN</p>
</blockquote></td>
<td><blockquote>
<p>2006</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JUL</p>
</blockquote></td>
<td><blockquote>
<p>2006</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AUG</p>
</blockquote></td>
<td><blockquote>
<p>2006</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SEP</p>
</blockquote></td>
<td><blockquote>
<p>2006</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OCT</p>
</blockquote></td>
<td><blockquote>
<p>2006</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NOV</p>
</blockquote></td>
<td><blockquote>
<p>2006</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEC</p>
</blockquote></td>
<td><blockquote>
<p>2006</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JAN</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FEB</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAR</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>APR</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>0</td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MAY</p>
</blockquote></td>
<td><blockquote>
<p>2007</p>
</blockquote></td>
<td>15</td>
<td></td>
<td>82</td>
<td></td>
<td><blockquote>
<p>97</p>
</blockquote></td>
</tr>
</tbody>
</table>

15 82 97

> Example: Monthly Surgical Case Workload Report – Range of Months

> Select Surgery Risk Assessment Menu Option: M Monthly Surgical Case Workload Report

#### printout follows 

> ALBANY - ALL DIVISIONS REPORT OF SURGICAL CASE WORKLOAD

> FOR OCT 2005 THROUGH MAY 2006

<table>
<colgroup>
<col style="width: 75%" />
<col style="width: 8%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>TOTAL CASES PERFORMED</p>
</blockquote></th>
<th><blockquote>
<p>=</p>
</blockquote></th>
<th>30</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>TOTAL ELIGIBLE CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>5</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CASES MEETING EXCLUSION CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NON-SURGEON CASE</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ANESTHESIA TYPE</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EXCEEDS MAX. ASSESSMENTS</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EXCEEDS MAXIMUM TURPS</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>INCLUSION CRTA NOT MET</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>10% RULE</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>1</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CONCURRENT CASE</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>EXCEEDS MAXIMUM HERNIAS</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ABORTED</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ASSESSED CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>20</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NOT LOGGED ELIGIBLE CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>0</td>
</tr>
<tr class="even">
<td><blockquote>
<p>CARDIAC CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>4</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NON-CARDIAC CASES</p>
</blockquote></td>
<td><blockquote>
<p>=</p>
</blockquote></td>
<td>16</td>
</tr>
</tbody>
</table>

# M&M Verification Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SRO M&M VERIFICATION REPORT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *M&M Verification Report* option produces the M&M Verification Report, which may be useful for:

- reviewing occurrences and their assignment to operations
- reviewing death unrelated/related assignments to operations

> The full report includes all patients who had operations within the selected date range who experienced intraoperative occurrences, postoperative occurrences or death within 90 days of surgery. The pre- transmission report is similar but includes operations with completed risk assessments that have not yet transmitted to the national database.

> Full Report

> Information is printed by patient, listing all operations for the patient that occurred during the selected date range, plus any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some operations that were performed prior to the selected date range and, if printed by specialty, may include operations performed by other specialties. For every operation listed, the intraoperative and postoperative occurrences are listed. The report indicates if the operation was flagged as unrelated or related to death and the risk assessment type and status. The report may be printed for a selected list of surgical specialties.

> Pre-Transmission Report

> Information is printed in a format similar to the full report. This report lists all completed risk assessed operations that have not yet transmitted to the national database and that have intraoperative occurrences, postoperative occurrences, or death within 90 days of surgery. The report includes any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some operations that may or may not be risk assessed, and, if risk assessed, may have a status other than 'complete'. However, every patient listed on this report will have at least one operation with a risk assessment status of 'complete'.

> Example 1: Generate an M&M Verification Report (Full Report)

> Select Surgery Risk Assessment Menu Option: V M&M Verification Report

> *printout follows*

> ALBANY - ALL DIVISIONS Page 1

> M&M Verification Report

> From: MAR 1,2007 To: MAR 30,2007 REVIEWED BY:

> Report Generated: APR 23,2007 DATE REVIEWED:

> OP DATE CASE \# SURGICAL SPECIALTY ASSESSMENT TYPE STATUS DEATH RELATED PRINCIPAL PROCEDURE

> ====================================================================================================================================

> \>\>\> SURPATIENT,FIVE (666-58-7963)

> 03/01/07 10401 GENERAL SURGERY NON-CARDIAC TRANSMITTED N/A APPENDECTOMY

> CPT Codes: 44970

> Occurrences: ACUTE RENAL FAILURE \*\* POSTOP \*\* (03/02/07)

> \>\>\> SURPATIENT,ONE (666-44-7629)

> 03/07/07 10421 GENERAL SURGERY NON-CARDIAC TRANSMITTED N/A APPENDECTOMY, CHOLECYSTECTOMY

> CPT Codes: 44950, 47610

> Occurrences: URINARY TRACT INFECTION \*\* POSTOP \*\* (03/09/07) ACUTE RENAL FAILURE \*\* POSTOP \*\* (03/10/07)

> OTHER RESPIRATORY OCCURRENCE \*\* POSTOP \*\* (03/10/07) ICD: 478.25 EDEMA PHARYNX/NASOPHARYX

> \>\>\> SURPATIENT,TWO (666-45-1982)

> 03/07/07 10422 NEUROSURGERY NON-CARDIAC TRANSMITTED N/A LAMINECTOMY

> CPT Codes: 22630

> Occurrences: OTHER OCCURRENCE (03/07/07)

> ICD: 415.19 OTH PULM EMB & INFARC

> \>\>\> SURPATIENT,ELEVEN (666-00-0748) - DIED 03/10/07@14:50

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 32%" />
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>03/10/07</p>
</blockquote></th>
<th><blockquote>
<p>10100</p>
</blockquote></th>
<th><blockquote>
<p>GENERAL SURGERY</p>
</blockquote></th>
<th><blockquote>
<p>NON-CARDIAC</p>
</blockquote></th>
<th><blockquote>
<p>INCOMPLETE</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>REMOVAL OF</p>
</blockquote></td>
<td><blockquote>
<p>GALLBLADDER</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> CPT Codes: 47600

> Occurrences: PULMONARY EMBOLISM \*\* POSTOP \*\* (03/10/07)

> \>\>\> Comments:

> Patient complained of chest pain and shortness of breath. Heparin was administered immediately by IV. Date of Death: 03/10/07@14:50

> Review of Death Comments: Patient expired from large pulmonary embolus before anticoagulant treatment could take effect.

> Patient's obesity and prolonged immobilization were likely contributing factors.

> Example 2: Generate an M&M Verification Report (Pre-Transmission Report)

#### printout follows 

> ALBANY - ALL DIVISIONS Page 1

> M&M Verification Report

> PRE-TRANSMISSION REPORT FOR COMPLETED ASSESSMENTS REVIEWED BY:

> Report Generated: OCT 23,2007 DATE REVIEWED:

> OP DATE CASE \# SURGICAL SPECIALTY ASSESSMENT TYPE STATUS DEATH RELATED PRINCIPAL PROCEDURE

> ====================================================================================================================================

> \>\>\> SURPATIENT,TWELVE (666-00-0762)

> 09/21/07 45466 PLASTIC SURGERY NON-CARDIAC COMPLETE N/A RHINOPLASTY

> CPT Codes: 30410

> Occurrences: DEEP INCISIONAL SSI \*\* POSTOP \*\* (09/23/07)

> \>\>\> SURPATIENT,FIFTEEN (666-00-0194)

> 09/16/07 45475 EAR, NOSE, THROAT (ENT) NON-CARDIAC COMPLETE N/A LARYNGECTOMY (TOTAL)

> CPT Codes: 31360

> Occurrences: BLEEDING/TRANSFUSIONS \*\* POSTOP \*\* (09/17/07)

> \>\>\> Comments:

> Esophageal varices were the source of bleeding.

> \>\>\> SURPATIENT,FORTY (666-00-4174)

> 09/19/07 45499 GENERAL SURGERY NON-CARDIAC COMPLETE N/A INGUINAL HERNIA

> CPT Codes: 49505

> Occurrences: URINARY TRACT INFECTION \*\* POSTOP \*\* (09/21/07)

> *(This page included for two-sided copying.)*

# Update 1-Liner Case

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA ONE-LINER UPDATE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Update 1-Liner* option may be used to enter missing data for the 1-liner cases (major cases marked for exclusion from assessment, minor cases, and cardiac-assessed cases that transmit to the VASQIP database as a single line or two of data). Cases edited with this option will be queued for transmission to the VASQIP database at Chicago.

> Example: Update 1-Liner Case

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719) Case #142</p>
<p>Transmission Status: QUEUED TO TRANSMIT &gt;&gt; Coding Complete &lt;&lt; AUG 7,2004 REPAIR DIAPHRAGMATIC HERNIA (CPT Code: 39540)</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th><ol type="1">
<li><p>Hospital Admission Status: SAME DAY</p></li>
<li><p>Surgical Specialty: GENERAL(OR WHEN NOT DEFINED BELOW)</p></li>
<li><p>Surgical Priority: STANDBY</p></li>
<li><p>Attending/Res Sup Code: LEVEL A. ATTENDING DOING THE OPERATION</p></li>
<li><p>ASA Class: 2-MILD DISTURB.</p></li>
<li><p>Wound Classification:</p></li>
<li><p>Principal Anesthesia Technique: GENERAL</p></li>
<li><p>CPT Codes (view only): 39540</p></li>
<li><p>Other Procedures: *NONE ENTERED*</p></li>
</ol></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select number of item to edit: <strong>6</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Wound Classification: <strong>C</strong> CLEAN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 81%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>SURPATIENT,TWELVE (000-41-8719) Case #142</p>
</blockquote></th>
<th rowspan="13"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Transmission Status: QUEUED TO TRANSMIT &gt;&gt; Coding Complete &lt;&lt;</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>AUG 7,2004 REPAIR DIAPHRAGMATIC HERNIA (CPT Code: 39540)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>1. Hospital Admission Status: SAME DAY</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>2. Surgical Specialty: GENERAL(OR WHEN NOT DEFINED BELOW)</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>3. Surgical Priority: STANDBY</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>4. Attending/Res Sup LEVEL A. ATTENDING DOING THE OPERATION</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>5. ASA Class: 2-MILD DISTURB.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>6. Wound Classification: CLEAN</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>7. Principle Anesthesia Technique: GENERAL</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>8. CPT Codes (view only): 39540</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>9. Other Procedures: *NONE ENTERED*</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Select number of item to edit:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> *(This page included for two-sided copying.)*

# Queue Assessment Transmissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA TRANSMIT ASSESSMENTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The *Queue Assessment Transmissions* option may be used to manually queue the VASQIP transmission process to run at a selected time. The VASQIP transmission process is a part of the nightly maintenance and cleanup process.

> Example: Queue Assessment Transmissions

> *(This page included for two-sided copying.)*

# Alert Coder Regarding Coding Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA CODE ISSUE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows the nurse reviewer to send an alert to the coder when there may be an issue with the CPT codes or the Postoperative Diagnosis codes for a Surgery case. When this option is selected, the nurse reviewer can enter a free-text message that will be sent to the coder on record, as well as to a pre- defined mail group identified in the Surgery Site Parameter titled CODE ISSUE MAIL GROUP. The message will not be sent if there is no coder, or if the mail group is not defined.

> Example : Alert Coder Regarding Coding Issues

> *(This page included for two-sided copying.)*

# Risk Model Lab Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \[SROA LAB TEST EDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to assist the nurse reviewer, in the *Surgery Risk Assessment Menu* is the *Risk Model Lab Test (Enter/Edit)* option, which allows the nurse to map VASQIP data in the RISK MODEL LAB TEST file (#139.2). The option synonym is ERM.

> <span id="_bookmark212" class="anchor"></span>Page 523 has been deleted. Chapter Seven: CoreFLS/Surgery Interface has been removed.

> *(This page included for two-sided copying.)*

# Chapter Seven: Code Set Versioning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Code Set Versioning enhancement to the Surgery package ensures that only CPT codes, CPT modifiers, and ICD codes that are active for the operation or procedure date will be available for selection by the user, regardless of when the CPT entry or edit is made. Also, when a future operation or procedure date is entered, only active codes will be available.

> It is possible that a new code set will be loaded between the time that an operation or procedure is scheduled and the time the operation or procedure occurs. Re-validation of the codes and modifiers occurs when the date and time that a patient enters the operating room is entered in the Surgery package. If the code (CPT or ICD) or CPT modifier is invalid — inactive for the date of operation or procedure — the inactive codes or modifiers will be deleted. Then, these two actions transpire:

1.  A warning message displays on the screen, corresponding to the specific code or modifier that is inactive.
2.  A MailMan message is sent to the surgeon (or provider), attending surgeon of record, and to the user who edited the record. The MailMan message contains the patient's name, date of operation, case number, free-text operation or procedure name, CPT or ICD codes, CPT modifiers deleted (if any), and the reason for deletion.

> The first sample warning message shows an inactive CPT code, its modifiers, and ICD-10 codes, and the second warning message is for a Non-O.R. procedure.

> Example: Warning Message to Surgeon

> Example: Warning Message to Provider

> The following sample MailMan message is sent to the surgeon, attending surgeon of record, and to the user who edited the record. The sample shows ICD codes, CPT codes, and CPT modifiers that are inactive.

> Example: MailMan Message to Surgeon ICD-9 Code

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Subj: ICD-9 OR CPT CODE DELETION [#208145] 05/06/14@09:56</p>
<p>From: SURGERY PACKAGE In 'IN' basket. Page 1 *New*</p>
</blockquote></th>
<th><blockquote>
<p>11 lines</p>
</blockquote></th>
<th rowspan="4"></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>Patient: SRPATIENTA,ONE Case #: 45804</p>
<p>Operation Date: MAY 06, 2014@11:11 OBS</p>
<p>The following codes are no longer active and were deleted for this case when the Time Patient in OR was entered.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>PRIN DIAGNOSIS CODE (ICD9):</p>
</blockquote></th>
<th><blockquote>
<p>600.01</p>
</blockquote></th>
<th></th>
</tr>
<tr class="odd">
<th colspan="3"><blockquote>
<p>New active codes must be re-entered.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: MailMan Message to Surgeon ICD-10 Code

> ![](surgery-version-3-user-manual-updated-sr-3-184/054.png)For Non-O.R. procedures, the MailMan message is sent to the provider and attending provider.

> Example: MailMan Message to Provider

> The following options allow for re-validation of the ICD and CPT codes and modifiers when the TIME PAT IN OR field or TIME PROCEDURE BEGAN field is entered.

#### Operation

- *Operation (Short Screen)*

#### Edit Non-O.R. Procedure

- *Operation Information (Enter/Edit)*

#### Resource Data

> <span id="_bookmark215" class="anchor"></span>Pages 527-547 have been deleted. The *Transplant Assessment Menu* has been removed with patch SR\*3\*184.

# Chapter Nine: Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table contains terms that are used throughout the *Surgery V.3.0 User Manual,* and will aid the user in understanding the use of the Surgery package.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Aborted</p>
</blockquote></td>
<td><blockquote>
<p>Case status indicating the case was cancelled after the patient entered the operating room. The Cases shall be considered "ABORTED" if the TIME PAT OUT OR field (#.205) and/or TIME PAT IN OR field (#.232) and</p>
<p>CANCEL DATE field (#17), and the CASE ABORTED field entered with "YES".</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ASA Class</p>
</blockquote></td>
<td><blockquote>
<p>This is the American Society of Anesthesiologists classification relating to the patient's physiologic status. Numbers followed by an 'E' indicate an</p>
<p>emergency.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Attending Code</p>
</blockquote></td>
<td><blockquote>
<p>Code that corresponds to the highest level of supervision provided by the</p>
<p>attending staff surgeon during the procedure.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Blockout Graph</p>
</blockquote></td>
<td><blockquote>
<p>Graph showing the availability of operating rooms.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Cancelled Case</p>
</blockquote></td>
<td><blockquote>
<p>Case status indicating that an entry has been made in the CANCEL DATE field, CANCELLATION TIMEFRAME and/or the PRIMARY CANCEL</p>
<p>REASON field without the patient entering the operating room.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCSHS</p>
</blockquote></td>
<td><blockquote>
<p>VA Center for Cooperative Studies in Health Services located at Hines,</p>
<p>Illinois.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CICSP</p>
</blockquote></td>
<td><blockquote>
<p>Continuous Improvement in Cardiac Surgery Program.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Completed Case</p>
</blockquote></td>
<td><blockquote>
<p>Case status indicating that an entry has been made in the TIME PAT OUT</p>
<p>OR field.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Concurrent Case</p>
</blockquote></td>
<td><blockquote>
<p>A patient undergoing two operations by different surgical specialties at the</p>
<p>same time, or back to back, in the same operating room.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPT Code</p>
</blockquote></td>
<td><blockquote>
<p>Also called Operation Code. CPT stands for Current Procedural</p>
<p>Terminology.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CRT</p>
</blockquote></td>
<td><blockquote>
<p>Cathode ray tube display. A display device that uses a cathode ray tube.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Intraoperative</p>
<p>Occurrence</p>
</blockquote></td>
<td><blockquote>
<p>Perioperative occurrence during the procedure.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Major</p>
</blockquote></td>
<td><blockquote>
<p>Any operation performed under general, spinal, or epidural anesthesia plus</p>
<p>all inguinal herniorrhaphies and carotid endarterectomies regardless of anesthesia administered.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Minor</p>
</blockquote></td>
<td><blockquote>
<p>All operations not designated as Major.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>New Surgical Case</p>
</blockquote></td>
<td><blockquote>
<p>A surgical case that has not been previously requested or scheduled such as an emergency case. A surgical case entered in the records without being booked through scheduling will not appear on the Schedule of Operations or</p>
<p>as an operative request.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Non-Operative</p>
<p>Occurrence</p>
</blockquote></td>
<td><blockquote>
<p>Occurrence that develops before a surgical procedure is performed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Not Complete</p>
</blockquote></td>
<td><blockquote>
<p>Case status indicating one of the following two situations with no entry in the TIME PAT OUT OR field (#.232).</p>
</blockquote>
<ol type="1">
<li><p>Case has entry in TIME PAT IN OR field (#.205).</p></li>
<li><p>Case has not been requested or scheduled.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p>NSQIP</p>
</blockquote></td>
<td><blockquote>
<p>National Surgical Quality Improvement Program.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Operation Code</p>
</blockquote></th>
<th><blockquote>
<p>Identifying code for reporting medical services and procedures performed by</p>
<p>physicians. See CPT Code.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PACU</p>
</blockquote></td>
<td><blockquote>
<p>Post Anesthesia Care Unit.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Postoperative</p>
<p>Occurrence</p>
</blockquote></td>
<td><blockquote>
<p>Perioperative occurrence following the procedure.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Procedure Occurrence</p>
</blockquote></td>
<td><blockquote>
<p>Occurrence related to a non-O.R. procedure.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Requested</p>
</blockquote></td>
<td><blockquote>
<p>Operation has been slotted for a particular day but the time and operating</p>
<p>room are not yet firm.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Risk Assessment</p>
</blockquote></td>
<td><blockquote>
<p>Part of the Surgery software that provides medical centers a mechanism to track information related to surgical risk and operative mortality. Completed assessments are transmitted to the VASQIP national database for statistical</p>
<p>analysis.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Scheduled</p>
</blockquote></td>
<td><blockquote>
<p>Operation has both an operating room and a scheduled starting time, but the</p>
<p>operation has not yet begun.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Screen Server</p>
</blockquote></td>
<td><blockquote>
<p>A format for displaying data on a cathode ray tube display. Screen Server is</p>
<p>designed specifically for the Surgery Package.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Screen Server</p>
<p>Function</p>
</blockquote></td>
<td><blockquote>
<p>The Screen Server prompt for data entry.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Service Blockouts</p>
</blockquote></td>
<td><blockquote>
<p>The reservation of an operating room for a particular service on a recurring</p>
<p>basis. The reservation is charted on a blockout graph.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Transplant Assessments</p>
</blockquote></td>
<td><blockquote>
<p>Part of the Surgery software that provides medical centers a mechanism to track information related to transplant risk and operative mortality.</p>
<p>Completed assessments are transmitted to the VASQIP national database for statistical analysis. The <em>Transplant Assessment Menu</em> has been removed</p>
<p>with patch SR*3*184.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VASQIP</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Affairs Surgery Quality Improvement Program.</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A
> AAIS, 437, 438
> anesthesia agents, 128, 160
> entering data, 161
> printing information, 170
> staff, 162
> techniques, 160 anesthesia agents flagging a drug, 431
> anesthesia personnel, 61, 128
> assigning, 173
> scheduling, 84 anesthesia technique
> entering information, 165, 173 assessment
> changing existing, 465 changing status of, 487 creating new, 465 upgrading status of, 464
> Automated Anesthesia Information System (AAIS), 437, 438
> B
> bar code reader, 158
> blockout an operating room, 85 blockout graph, 60
> Blood Bank, 158 blood product label, 158
> verification, 158 book an operation, 25
> book concurrent operation, 45 C
> cancellation rates calculations, 347 case
> cancelled, 345
> cardiac, 465
> delayed, 338
> designation, 96
> editing cancelled, 400 list of requested, 57 scheduled, 96, 345
> updating the cancellation date, 83 updating the cancellation reason, 83 verifying, 352
> Chief of Surgery, 178, 251, 398 Code Set Versioning, 525 coding
> checking accuracy of procedures, 310 entry, 207
> validation, 207 comments adding, 205
> completed cases, 355, 357
> PCE filing status of, 238, 273
> report of, 232, 234, 257, 265, 267
> reports on, 252
> staffing information for, 284 surgical priority, 269
> complications, 93, 459
> concurrent case, 93
> adding, 74
> defined, 15
> scheduling, 61
> scheduling unrequested operations, 69 condensed characters, 26
> count clinic active, 278
> CPT codes, 59, 207, 220, 224, 255, 525
> CPT modifiers, 525
> cultures, 153, 196
> cutoff time, 15, 42 D
> deaths reviewing, 330
> within 30 days of surgery, 183, 326
> within 90 days of surgery, 330 delays
> reasons for, 340
> devices, 155 updating list of, 429
> diagnosis, 113, 208, 238, 273
> dosage, 157, 169
> downloading Surgery set of codes, 438 E
> electronically signing a report Anesthesia Report, 131, 134 Nurse Intraoperative Report, 2
> F
> flag a drug, 431 G
> Glossary, 549 H
> HL7, 434, 435, 439
> master file updates, 437, 438 I
> ICD-10 codes, 207, 525
> interim reports, 319 intraoperative occurrence entering, 459, 475
> irrigation solutions, 155 K
> KERNEL audit log, 393 L
> laboratory information, 95
> entering, 451
> Laboratory Package, 319 list of requested cases, 57
> M
> medical administration, 95
> medications, 157, 169
> mortality and morbidity rates, 183, 326
> multiple fields, 108 N
> new surgical case, 101 non-count encounters, 278
> non-O.R. procedure, 187
> deleting data, 188
> editing data, 188
> entering data, 188
> NSQIP, 509, 519, 550
> NSQIP transmission process, 521 nurse staffing information, 294 nursing care, 140
> O
> occurrence, 180
> adding information about a postoperative, 178 editing, 176
> entering, 176
> intraoperative, 330, 459, 475 adding information about an, 176 M&M Verification Report, 330
> number of for delayed operations, 340 postoperative, 330, 461
> reviewing, 330
> viewing, 324 Operating Room
> determining use of, 414 entering information, 413
> percent utilization, 361
> rescheduling, 74
> reserving on a recurring basis, 85 utilization reports, 415
> viewing availability of, 26 viewing availability of, 60
> Operating Room Schedule, 88, 253
> operation
> book concurrent, 45
> booking, 25, 59
> canceling scheduled, 81
> close of, 119
> delayed, 108, 338, 340
> discharge, 119
> outstanding requests, 28
> patient preparation, 108
> post anesthesia recovery, 119 requesting, 25
> rescheduling, 74
> scheduled, 26
> scheduled by surgical specialty, 91 scheduling requested, 59
> scheduling unrequested, 64
> starting time, 113 operation information entering or editing, 455 operation request deleting, 36
> printing a list, 53 Options
> Admissions Within 14 Days of Outpatient Surgery, 0
> Anesthesia Data Entry Menu, 161 Anesthesia for an Operation Menu, 128 Anesthesia Information (Enter/Edit), 162 Anesthesia Menu, 160
> Anesthesia Provider Report, 303 Anesthesia Report, 131, 170
> Anesthesia Reports, 296
> Anesthesia Technique (Enter/Edit), 165 Annual Report of Non-O.R. Procedures, 196 Annual Report of Surgical Procedures, 255 Attending Surgeon Reports, 284
> Blood Product Verification, 158 Cancel Scheduled Operation, 81
> Cardiac Procedures Requiring CPB (Enter/Edit), 473
> Chief of Surgery, 323
> Chief of Surgery Menu, 321 Circulating Nurse Staffing Report, 294 Clinical Information (Enter/Edit), 467 Comments Option, 205
> Comparison of Preop and Postop Diagnosis, 335 CPT Code Reports, 305
> CPT/ICD-10 Coding Menu, 207 CPT/ICD-10 Update/Verify Menu, 208 Create Service Blockout, 85
> Cumulative Report of CPT Codes, 220, 306
> Deaths Within 30 Days of Surgery, 395 Delay and Cancellation Reports, 337 Delete a Patient from the Waiting List, 23 Delete or Update Operation Requests, 36 Delete Service Blockout, 87
> Display Availability, 26, 60
> Edit a Patient on the Waiting List, 22 Edit Non-O.R. Procedure, 189
> Enter a Patient on the Waiting List, 21
> Enter Cardiac Catheterization & Angiographic Data, 469
> Enter Irrigations and Restraints, 155 Enter PAC(U) Information, 121, 125
> Enter Referring Physician Information, 154 Enter Restrictions for 'Person' Fields, 426 Exclusion Criteria (Enter/Edit), 507
> File Download, 437
> Flag Drugs for Use as Anesthesia Agents, 431 Flag Interface Fields, 435
> Intraoperative Occurrences (Enter/Edit), 176, 459, 475
> Laboratory Interim Report, 319
> Laboratory Test Results (Enter/Edit), 451, 470 List Completed Cases Missing CPT Codes, 230,
> 316
> List of Anesthetic Procedures, 299 List of Operations, 232, 257
> List of Operations (by Postoperative Disposition), 259
> List of Operations (by Surgical Priority), 267 List of Operations (by Surgical Specialty), 234,
> 265
> List of Surgery Risk Assessments, 489 List of Unverified Surgery Cases, 352 List Operation Requests, 57
> List Scheduled Operations, 91 M&M Verification Report, 330, 513
> Maintain Surgery Waiting List menu, 17 Make a Request for Concurrent Cases, 45 Make a Request from the Waiting List, 42 Make Operation Requests, 28
> Make Reports Viewable in CPRS, 440 Management Reports, 252, 325
> Medications (Enter/Edit), 157, 169
> Monthly Surgical Case Workload Report, 509 Morbidity & Mortality Reports, 183, 326 Non-Cardiac Risk Assessment Information
> (Enter/Edit), 445
> Non-O.R. Procedures, 187
> Non-O.R. Procedures (Enter/Edit), 188
> Non-Operative Occurrence (Enter/Edit), 180
> Normal Daily Hours (Enter/Edit), 417 Nurse Intraoperative Report, 140, 217
> Operating Room Information (Enter/Edit), 413 Operating Room Utilization (Enter/Edit), 415 Operating Room Utilization Report, 361, 419
> Operation, 113
> Operation (Short Screen), 122 Operation Information, 103
> Operation Information (Enter/Edit), 455 Operation Menu, 95
> Operation Report, 129
> Operation Requests for a Day, 53 Operation Startup, 108
> Operation/Procedure Report, 213
> Operative Risk Summary Data (Enter/Edit), 471 Outpatient Encounters Not Transmitted to
> NPCD, 278
> Patient Demographics (Enter/Edit), 457 PCE Filing Status Report, 238, 273 Perioperative Occurrences Menu, 175 Person Field Restrictions Menu, 425 Post Operation, 119
> Postoperative Occurrences (Enter/Edit), 178, 461, 477
> Print 30 Day Follow-up Letters, 503 Print a Surgery Risk Assessment, 481
> Print Blood Product Verification Audit Log, 393 Print Surgery Waiting List, 18
> Procedure Report (Non-O.R.), 193 Purge Utilization Information, 424 Queue Assessment Transmissions, 521
> Remove Restrictions on 'Person' Fields, 428 Report of Cancellation Rates, 347
> Report of Cancellations, 345
> Report of Cases Without Specimens, 357 Report of CPT Coding Accuracy, 224, 310 Report of Daily Operating Room Activity, 236,
> 271, 355
> Report of Delay Reasons, 340 Report of Delay Time, 342
> Report of Delayed Operations, 338
> Report of Missing Quarterly Report Data, 0 Report of Non-O.R. Procedures, 198, 243 Report of Normal Operating Room Hours, 421 Report of Returns to Surgery, 353
> Report of Surgical Priorities, 269
> Report of Unscheduled Admissions to ICU, 359 Request Operations menu, 25
> Requests by Ward, 55
> Reschedule or Update a Scheduled Operation, 74
> Resource Data (Enter/Edit), 479 Review Request Information, 52 Risk Assessment, 465
> Schedule Anesthesia Personnel, 84, 173
> Schedule of Operations, 88, 253
> Schedule Operations, 59
> Schedule Requested Operation, 61
> Schedule Unrequested Concurrent Cases, 69 Schedule Unrequested Operations, 64
> Scrub Nurse Staffing Report, 292 Surgeon Staffing Report, 288 Surgeon's Verification of Diagnosis &
> Procedures, 125
> Surgery Interface Management Menu, 434 Surgery Package Management Menu, 409 Surgery Reports, 251
> Surgery Site Parameters (Enter/Edit), 410 Surgery Staffing Reports, 283
> Surgery Utilization Menu, 414 Surgical Nurse Staffing Report, 290 Surgical Staff, 104
> Table Download, 438
> Tissue Examination Report, 153 Unlock a Case for Editing, 398 Update 1-Liner Case, 519
> Update Assessment Completed/Transmitted in Error, 487
> Update Assessment Status to 'Complete', 464, 0 Update Assessment Status to 'COMPLETE',
> 481
> Update Cancellation Reason, 83 Update Cancelled Cases, 400
> Update Interface Parameter Field, 439 Update O.R. Schedule Devices, 429 Update Operations as Unrelated/Related to
> Death, 401
> Update Site Configurable Files, 432 Update Staff Surgeon Information, 430
> Update Status of Returns Within 30 Days, 181, 399, 463
> Update/Verify Procedure/Diagnosis Codes, 209, 402
> View Patient Perioperative Occurrences, 324 Wound Classification Report, 363
> Options:, 196, 197, 221 outstanding requests defined, 15
> P
> PACU, 121
> PCE filing status, 238, 273
> percent utilization, 361, 419
> person-type field assigning a key, 426 removing a key, 426, 428
> Pharmacy Package Coordinator, 431 positioning devices, 155
> Post Anesthesia Care Unit (PACU), 121 postoperative occurrence
> entering, 461, 474, 477 preoperative assessment entering information, 448
> preoperative information, 15
> editing, 52
> entering, 29, 65
> reviewing, 52
> updating, 74
> Preoperative Information (Enter/Edit), 448 principal diagnosis, 103
> P
> procedure deleting, 23
> dictating a summary, 189 editing data for non-O.R., 189 entering data for non-O.R., 189 filed as encounters, 278 summary for non-O.R., 193
> purging utilization information, 424 Q
> quick reference on a case, 103 R
> Referring physician information, 154 reporting
> tracking cancellations, 337
> tracking delays, 337 reports
> Admissions Within 14 Days of Outpatient Surgery Report, 0
> Anesthesia Provider Report, 303 Anesthesia Report, 131
> Annual Report of Non-O.R. Procedures, 196 Annual Report of Surgical Procedures, 255 Attending Surgeon Cumulative Report, 284, 286 Attending Surgeon Report, 284
> Cases Without Specimens, 357 Circulating Nurse Staffing Report, 294 Clean Wound Infection Summary, 367
> Comparison of Preop and Postop Diagnosis, 335 Completed Cases Missing CPT Codes, 230, 316 Cumulative Report of CPT Codes, 220, 222,
> 306, 308
> Daily Operating Room Activity, 236 Daily Operating Room Activity, 271
> Daily Operating Room Activity, 325 Daily Operating Room Activity, 355 Daily Operating Room Activity, 355 Deaths Within 30 Days of Surgery, 396, 0 Laboratory Interim Report, 319
> List of Anesthetic Procedures, 299, 301
> List of Operations, 232, 257
> List of Operations (by Surgical Specialty), 234 List of Operations by Postoperative Disposition,
> 259, 261, 263
> List of Operations by Surgical Priority, 267 List of Operations by Surgical Specialty, 265
> List of Operations by Wound Classification, 365 List of Unverified Cases, 352
> M&M Verification Report, 330, 333, 513, 516 Missing Quarterly Report Data, 0
> Monthly Surgical Case Workload Report, 509, 511
> Mortality Report, 183, 326, 328 Nurse Intraoperative Report, 141
> Operating Room Normal Working Hours Report, 421
> Operating Room Utilization Report, 419 Operation Report, 130, 213
> Operation Requests, 57 Operation Requests for a Day, 53
> Outpatient Surgery Encounters Not Transmitted to NPCD, 278, 280
> PCE Filing Status Report, 239, 241, 274, 276
> Perioperative Occurrences Report, 183, 326
> Procedure Report (Non-O.R.), 195, 216 Procedure Report (Non-OR), 215
> Re-Filing Cases in PCE, 282
> Report of Cancellation Rates, 347, 349 Report of Cancellations, 345
> Report of CPT Coding Accuracy, 224, 310, 312,
> 314
> Report of CPT Coding Accuracy for OR Surgical Procedures, 226, 228
> Report of Daily Operating Room Activity, 271 Report of Delay Time, 342
> Report of Delayed Operations, 338
> Report of Non-O.R. Procedures, 198, 200, 202,
> 243, 245, 247
> Report of Returns to Surgery, 353 Report of Surgical Priorities, 269, 270 Requests by Ward, 55
> Schedule of Operations, 88 Scheduled Operations, 91
> Scrub Nurse Staffing Report, 292 Surgeon Staffing Report, 288
> Surgery Risk Assessment, 481, 485 Surgery Waiting List, 18
> Surgical Nurse Staffing Report, 290 Tissue Examination Report, 153, 196 Unscheduled Admissions to ICU, 359 Wound Classification Report, 363 request an operation, 25
> restraint, 108, 155
> risk assessment, 330
> changing, 445
> creating, 445, 544
> creating cardiac, 465
> entering non-cardiac patient, 445
> entering the clinical information for cardiac case, 467
> Risk Assessment, 481, 550 Risk Assessment module, 443 Risk Model Lab Test, 574 route, 157, 169
> S
> schedule an unrequested operation, 64 scheduled, 79, 84, 98, 550
> scheduling a concurrent case, 61 Screen Server, 93
> data elements, 6
> Defined, 5
> editing data, 8
> entering a range of elements, 9 entering data, 7
> header, 6
> multiple screen shortcut, 12 multiples, 10
> Navigation, 5
> prompt, 6
> turning pages, 8
> word processing, 14
> service blockout, 60
> creating, 85
> removing, 87
> short form listing of scheduled cases, 91 site-configurable files, 432
> specimens, 153, 196 staff surgeon
> designating a user as, 430 surgeon key, 426
> Surgery case cancelled, 400
> unlocking, 398
> Surgery package coordinator, 407 Surgery Site parameters
> entering, 410
> Surgical Service Chief, 321 Surgical Service managers, 410 surgical specialty, 21, 57, 74, 234
> Surgical staff, 104 T
> time given, 157, 169 transfusion
> error risk management, 158 U
> utilization information, 361, 419
> purging, 424 V
> VA Central Office, 255
> W
> Waiting List
> adding a new case, 21 deleting a procedure, 23 editing a patient on the, 22 entering a patient, 21 printing, 18
> waiting lists, 17 workload report, 509
> uncounted, 278
> wound classification, 363

#### (This page blank to preserve original page numbering)


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Surgery User Manual (SR*3.0*200)

## ![](surgery-user-manual-sr-3-0-200/002.png)![](surgery-user-manual-sr-3-0-200/003.png)![](surgery-user-manual-sr-3-0-200/004.png)![](surgery-user-manual-sr-3-0-200/005.png)Getting Help and Exiting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ?, ??, ??? One, two or three question marks can be entered at any of the prompts for on-line help. One question mark elicits a brief statement of what information is appropriate for the prompt. Two question marks provide more help, plus the hidden actions, and three question marks will provide more detailed help, including a list of possible answers, if appropriate.

> Typing an up arrow ^ (caret or a circumflex) and pressing \<Enter\> can be used to exit the current option.

> *(This page included for two-sided copying.)*
