---
title: SR*3*175 Surgery VASQIP 2011 Technical Manual/Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Surgery VASQIP 2011 /Security Guide Change Pages
app_code: SR
app_name: Surgery
section: CLI
app_status: active
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*175
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: > ![](sr-3-175-surgery-vasqip-2011-technical-manual-security-guide-change-pages/001.png)
audience: 
keywords: 
  - blockquote
  - class
  - table
  - even
  - contents
  - surgery
  - style
  - width
  - strong
  - report
page_count: 0
word_count: 7579
section_count: 22
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: July 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr_3_p175_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr_3_p175_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=103"
---

> ![](sr-3-175-surgery-vasqip-2011-technical-manual-security-guide-change-pages/001.png)

SURGERY

> TECHNICAL MANUAL/ SECURITY GUIDE

> Version 3.0

> July 1993

### (Revised September 2011)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs Product Development

> Revision History

> Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revised Pages</strong></th>
<th><strong>Patch Number</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/11</td>
<td><blockquote>
<p>i, 13, 18-19, 20-22,</p>
<p>24-29, 34-36, 38,</p>
<p>40, 67, 69, 78-79</p>
</blockquote></td>
<td>SR*3*175</td>
<td><p>Change in definitions. Routine SRTOVRF added to the list of routines. Options description list updated.</p>
<p>Quarterly Report Menu removed. References to CICSP and NSQIP removed from the Glossary.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>12/10</td>
<td>i, 27</td>
<td><blockquote>
<p>SR*3*174</p>
</blockquote></td>
<td><p>Change in definition of List of Surgery Risk Assessments report.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>11/08</td>
<td>All</td>
<td><blockquote>
<p>SR*3*167</p>
</blockquote></td>
<td><p>Updated to provide the Surgery Transplant Assessment module information. Additions necessitated a document reissue.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>
# Files


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [(Revised September 2011)](#revised-september-2011)
- [Files](#files)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Options Listed by Name](#options-listed-by-name)
- [Option Descriptions](#option-descriptions)
  - [Admissions w/in 14 days of Out Surgery if Postop Occ \[SROQADM\]](#admissions-win-14-days-of-out-surgery-if-postop-occ-sroqadm)
  - [Annual Report of Surgical Procedures \[SROARSP\]](#annual-report-of-surgical-procedures-sroarsp)
  - [Circulating Nurse Staffing Report \[SROCNR\]](#circulating-nurse-staffing-report-srocnr)
  - [Comparison of Preop and Postop Diagnosis \[SROPPC\]](#comparison-of-preop-and-postop-diagnosis-sroppc)
    - [This option is used to block out times on the Operating Room Schedule by surgical specialty.](#this-option-is-used-to-block-out-times-on-the-operating-room-schedule-by-surgical-specialty)
  - [Deaths Within 30 Days of Surgery \[SROQD\]](#deaths-within-30-days-of-surgery-sroqd)
  - [Delete or Update Operation Requests \[SRSUPRQ\]](#delete-or-update-operation-requests-srsuprq)
  - [Flag Drugs for Use as Anesthesia Agents \[SROCODE\]](#flag-drugs-for-use-as-anesthesia-agents-srocode)
  - [List Completed Cases Missing CPT Codes \[SRSCPT\]](#list-completed-cases-missing-cpt-codes-srscpt)
  - [List of Invasive Diagnostic Procedures \[SROQIDP\]](#list-of-invasive-diagnostic-procedures-sroqidp)
  - [List of Unverified Surgery Case \[SROUNV\]](#list-of-unverified-surgery-case-srounv)
  - [Make a Request from the Waiting List \[SRSWREQ\]](#make-a-request-from-the-waiting-list-srswreq)
  - [Morbidity & Mortality Reports \[SROMM\]](#morbidity-mortality-reports-sromm)
  - [Non-Operative Occurrences (Enter/Edit) \[SROCOMP\]](#non-operative-occurrences-enteredit-srocomp)
  - [Operating Room Information (Enter/Edit) \[SRO-ROOM\]](#operating-room-information-enteredit-sro-room)
  - [Report of Daily Operating Room Activity \[SROPACT\]](#report-of-daily-operating-room-activity-sropact)
  - [Report of Unscheduled Admissions to ICU \[SROICU\]](#report-of-unscheduled-admissions-to-icu-sroicu)
  - [Reschedule or Update a Scheduled Operation \[SRSCHUP\]](#reschedule-or-update-a-scheduled-operation-srschup)
  - [Schedule Unrequested Concurrent Cases \[SRSCHDC\]](#schedule-unrequested-concurrent-cases-srschdc)
  - [Surgeon's Verification of Diagnosis & Procedures \[SROVER\]](#surgeons-verification-of-diagnosis-procedures-srover)
  - [Surgery Risk Assessment - Site Update Server \[SROASITE\]](#surgery-risk-assessment-site-update-server-sroasite)
    - [This option is used to update the cancellation date and reason previously entered for a selected surgical case.](#this-option-is-used-to-update-the-cancellation-date-and-reason-previously-entered-for-a-selected-surgical-case)
  - [Wound Classification Report \[SROWC\]](#wound-classification-report-srowc)
- [Templates](#templates)
- [Input Templates](#input-templates)
- [Sort Template](#sort-template)
- [Glossary](#glossary)
- [APPENDIX A: Surgery Source Data Elements for PFSS](#appendix-a-surgery-source-data-elements-for-pfss)
- [Surgery Request Consult Data Source for Get Account](#surgery-request-consult-data-source-for-get-account)
> Each entry in the SURGERY file (#130) contains information regarding a surgery case, consisting of an operative procedure, or multiple operative procedures, for a patient. The file includes the information necessary for creating the Nurse Intraoperative Report, the Operation Report, and the Anesthesia Report.
> The following files are exported with the Surgery package.
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 43%" />
<col style="width: 12%" />
<col style="width: 22%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>File #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Update DD</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Data Comes With File</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>User Override</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>130</td>
<td>SURGERY</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>131</td>
<td><blockquote>
<p>PERSON FIELD RESTRICTION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES (MERGE)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>131.01</td>
<td>SURGERY TRANSPORTATION DEVICES</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>131.25</td>
<td>OPERATION TIMES</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>131.6</td>
<td>SURGERY DISPOSITION</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
</tr>
<tr class="even">
<td>131.7</td>
<td>OPERATING ROOM</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>131.8</td>
<td>SURGERY UTILIZATION</td>
<td>YES</td>
<td>NO</td>
<td>YES</td>
</tr>
<tr class="even">
<td>131.9</td>
<td>PROSTHESIS</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>NO</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>132</td>
<td><blockquote>
<p>SURGERY POSITION</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES (MERGE)</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>132.05</td>
<td>RESTRAINTS AND POSITIONAL AIDS</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>132.4</td>
<td>SURGICAL DELAY</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES (MERGE)</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>132.8</td>
<td>ASA CLASS</td>
<td>YES</td>
<td>YES (OVERWRITE)</td>
<td>NO</td>
</tr>
<tr class="odd">
<td>132.9</td>
<td>ATTENDING CODES</td>
<td>YES</td>
<td>YES</td>
<td>NO</td>
</tr>
<tr class="even">
<td>132.95</td>
<td>ANESTHESIA SUPERVISOR CODES</td>
<td>YES</td>
<td>YES (OVERWRITE)</td>
<td>NO</td>
</tr>
<tr class="odd">
<td>133</td>
<td><blockquote>
<p>SURGERY SITE PARAMETERS</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>NO (OVERWRITE)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>133.2</td>
<td><blockquote>
<p>SURGERY INTERFACE PARAMETER</p>
</blockquote></td>
<td>YES</td>
<td>YES</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>133.4</td>
<td>MONITORS</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES (MERGE)</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>133.6</td>
<td>IRRIGATION</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>133.7</td>
<td>SURGERY REPLACEMENT FLUIDS</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>133.8</td>
<td>SURGERY WAITING LIST</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>NO</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>134</td>
<td><blockquote>
<p>OPERATING ROOM TYPE</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES (OVERWRITE)</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>135</td>
<td><blockquote>
<p>SURGERY CANCELLATION REASON</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>YES (MERGE)</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>135.1</td>
<td>SKIN PREP AGENTS</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>135.2</td>
<td>SKIN INTEGRITY</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="odd">
<td>135.3</td>
<td>PATIENT MOOD</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>135.4</td>
<td>PATIENT CONSCIOUSNESS</td>
<td>YES</td>
<td>YES (MERGE)</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>136</td>
<td><blockquote>
<p>SURGERY PROCEDURE/DIAGNOSIS CODES</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td>NO</td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>136.5</td>
<td>PERIOPERATIVE OCCURRENCE CATEGORY</td>
<td>YES</td>
<td>YES (OVERWRITE)</td>
<td>NO</td>
</tr>
<tr class="odd">
<td>137</td>
<td><blockquote>
<p>CPT EXCLUSIONS</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>137.45</p>
</blockquote></td>
<td><blockquote>
<p>LOCAL SURGICAL SPECIALTY</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES (OVERWRITE)</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>138</p>
</blockquote></td>
<td><blockquote>
<p>ELECTROGROUND POSITIONS</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>YES (MERGE)</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
</tbody>
</table>
> *(This page included for two-sided copying.)*

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is the list of routines used in the Surgery package. This list excludes all initialization routines, protocol installation routines, and routines exported with patches that performed a one-time function. The first line of each routine contains a brief description of the general function of the routine. Use the Kernel *First Line Routine Print* \[XU FIRST LINE PRINT\] option to print a list of just the first line of each routine in the SR- namespace.

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>SRBL</th>
<th><blockquote>
<p>SRBLOOD</p>
</blockquote></th>
<th>SRCHL7A</th>
<th>SRCHL7U</th>
<th><blockquote>
<p>SRCUSS</p>
</blockquote></th>
<th><blockquote>
<p>SRCUSS0</p>
</blockquote></th>
<th><blockquote>
<p>SRCUSS1</p>
</blockquote></th>
<th><blockquote>
<p>SRCUSS2</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SRCUSS3</td>
<td><blockquote>
<p>SRCUSS4</p>
</blockquote></td>
<td>SRCUSS5</td>
<td>SRENSCS</td>
<td><blockquote>
<p>SRHLDW</p>
</blockquote></td>
<td><blockquote>
<p>SRHLDW1</p>
</blockquote></td>
<td><blockquote>
<p>SRHLENV</p>
</blockquote></td>
<td><blockquote>
<p>SRHLMFN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRHLOORU</td>
<td><blockquote>
<p>SRHLORU</p>
</blockquote></td>
<td>SRHLQRY</td>
<td>SRHLSCRN</td>
<td><blockquote>
<p>SRHLU</p>
</blockquote></td>
<td><blockquote>
<p>SRHLUI</p>
</blockquote></td>
<td><blockquote>
<p>SRHLUO</p>
</blockquote></td>
<td><blockquote>
<p>SRHLUO1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRHLUO2</td>
<td><blockquote>
<p>SRHLUO3</p>
</blockquote></td>
<td>SRHLUO4</td>
<td>SRHLUO4C</td>
<td><blockquote>
<p>SRHLVOOR</p>
</blockquote></td>
<td><blockquote>
<p>SRHLVORU</p>
</blockquote></td>
<td><blockquote>
<p>SRHLVQRY</p>
</blockquote></td>
<td><blockquote>
<p>SRHLVU</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRHLVUI</td>
<td><blockquote>
<p>SRHLVUI2</p>
</blockquote></td>
<td>SRHLVUO</td>
<td>SRHLVUO1</td>
<td><blockquote>
<p>SRHLVUO2</p>
</blockquote></td>
<td><blockquote>
<p>SRHLVUO4</p>
</blockquote></td>
<td><blockquote>
<p>SRHLVZIU</p>
</blockquote></td>
<td><blockquote>
<p>SRHLVZQR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRHLVZSQ</td>
<td><blockquote>
<p>SRHLXTMP</p>
</blockquote></td>
<td>SRHLZIU</td>
<td>SRHLZQR</td>
<td><blockquote>
<p>SRO1L</p>
</blockquote></td>
<td><blockquote>
<p>SRO1L1</p>
</blockquote></td>
<td><blockquote>
<p>SROA30</p>
</blockquote></td>
<td><blockquote>
<p>SROABCH</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROAC</td>
<td><blockquote>
<p>SROAC1</p>
</blockquote></td>
<td>SROAC2</td>
<td>SROACAR</td>
<td><blockquote>
<p>SROACAR1</p>
</blockquote></td>
<td><blockquote>
<p>SROACAT</p>
</blockquote></td>
<td><blockquote>
<p>SROACC</p>
</blockquote></td>
<td><blockquote>
<p>SROACC0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROACC1</td>
<td><blockquote>
<p>SROACC2</p>
</blockquote></td>
<td>SROACC3</td>
<td>SROACC4</td>
<td><blockquote>
<p>SROACC5</p>
</blockquote></td>
<td><blockquote>
<p>SROACC6</p>
</blockquote></td>
<td><blockquote>
<p>SROACCM</p>
</blockquote></td>
<td><blockquote>
<p>SROACCR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROACCT</td>
<td><blockquote>
<p>SROACL1</p>
</blockquote></td>
<td>SROACL2</td>
<td>SROACLN</td>
<td><blockquote>
<p>SROACMP</p>
</blockquote></td>
<td><blockquote>
<p>SROACMP1</p>
</blockquote></td>
<td><blockquote>
<p>SROACOD</p>
</blockquote></td>
<td><blockquote>
<p>SROACOM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROACOM1</td>
<td><blockquote>
<p>SROACOP</p>
</blockquote></td>
<td>SROACPM</td>
<td>SROACPM1</td>
<td><blockquote>
<p>SROACPM2</p>
</blockquote></td>
<td><blockquote>
<p>SROACR1</p>
</blockquote></td>
<td><blockquote>
<p>SROACR2</p>
</blockquote></td>
<td><blockquote>
<p>SROACRC</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROACS</td>
<td><blockquote>
<p>SROACTH</p>
</blockquote></td>
<td>SROACTH1</td>
<td>SROADEL</td>
<td><blockquote>
<p>SROADOC</p>
</blockquote></td>
<td><blockquote>
<p>SROADOC1</p>
</blockquote></td>
<td><blockquote>
<p>SROADX</p>
</blockquote></td>
<td><blockquote>
<p>SROADX1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROADX2</td>
<td><blockquote>
<p>SROAERR</p>
</blockquote></td>
<td>SROAEX</td>
<td>SROAL1</td>
<td><blockquote>
<p>SROAL11</p>
</blockquote></td>
<td><blockquote>
<p>SROAL2</p>
</blockquote></td>
<td><blockquote>
<p>SROAL21</p>
</blockquote></td>
<td><blockquote>
<p>SROALAB</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROALC</td>
<td><blockquote>
<p>SROALCP</p>
</blockquote></td>
<td>SROALCS</td>
<td>SROALCSP</td>
<td><blockquote>
<p>SROALDP</p>
</blockquote></td>
<td><blockquote>
<p>SROALEC</p>
</blockquote></td>
<td><blockquote>
<p>SROALEN</p>
</blockquote></td>
<td><blockquote>
<p>SROALESS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROALET</td>
<td><blockquote>
<p>SROALL</p>
</blockquote></td>
<td>SROALLP</td>
<td>SROALLS</td>
<td><blockquote>
<p>SROALLSP</p>
</blockquote></td>
<td><blockquote>
<p>SROALM</p>
</blockquote></td>
<td><blockquote>
<p>SROALMN</p>
</blockquote></td>
<td><blockquote>
<p>SROALN1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROALN2</td>
<td><blockquote>
<p>SROALN3</p>
</blockquote></td>
<td>SROALNC</td>
<td>SROALNO</td>
<td><blockquote>
<p>SROALOG</p>
</blockquote></td>
<td><blockquote>
<p>SROALSL</p>
</blockquote></td>
<td><blockquote>
<p>SROALSS</p>
</blockquote></td>
<td><blockquote>
<p>SROALSSP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROALST</td>
<td><blockquote>
<p>SROALSTP</p>
</blockquote></td>
<td>SROALT</td>
<td>SROALTP</td>
<td><blockquote>
<p>SROALTS</p>
</blockquote></td>
<td><blockquote>
<p>SROALTSP</p>
</blockquote></td>
<td><blockquote>
<p>SROAMAN</p>
</blockquote></td>
<td><blockquote>
<p>SROAMEAS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROAMIS</td>
<td><blockquote>
<p>SROAMIS1</p>
</blockquote></td>
<td>SROANEST</td>
<td>SROANEW</td>
<td><blockquote>
<p>SROANIN</p>
</blockquote></td>
<td><blockquote>
<p>SROANP</p>
</blockquote></td>
<td><blockquote>
<p>SROANP1</p>
</blockquote></td>
<td><blockquote>
<p>SROANR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROANR0</td>
<td><blockquote>
<p>SROANR1</p>
</blockquote></td>
<td>SROANT</td>
<td>SROANTP</td>
<td><blockquote>
<p>SROANTS</p>
</blockquote></td>
<td><blockquote>
<p>SROANTSP</p>
</blockquote></td>
<td><blockquote>
<p>SROAO</p>
</blockquote></td>
<td><blockquote>
<p>SROAOP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROAOP1</td>
<td><blockquote>
<p>SROAOP2</p>
</blockquote></td>
<td>SROAOPS</td>
<td>SROAOSET</td>
<td><blockquote>
<p>SROAOTH</p>
</blockquote></td>
<td><blockquote>
<p>SROAOUT</p>
</blockquote></td>
<td><blockquote>
<p>SROAPAS</p>
</blockquote></td>
<td><blockquote>
<p>SROAPC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROAPCA</td>
<td><blockquote>
<p>SROAPCA0</p>
</blockquote></td>
<td>SROAPCA1</td>
<td>SROAPCA2</td>
<td><blockquote>
<p>SROAPCA3</p>
</blockquote></td>
<td><blockquote>
<p>SROAPCA4</p>
</blockquote></td>
<td><blockquote>
<p>SROAPIMS</p>
</blockquote></td>
<td><blockquote>
<p>SROAPM</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROAPR1A</td>
<td><blockquote>
<p>SROAPR2</p>
</blockquote></td>
<td>SROAPRE</td>
<td>SROAPRE1</td>
<td><blockquote>
<p>SROAPRE2</p>
</blockquote></td>
<td><blockquote>
<p>SROAPRT1</p>
</blockquote></td>
<td><blockquote>
<p>SROAPRT2</p>
</blockquote></td>
<td><blockquote>
<p>SROAPRT3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROAPRT4</td>
<td><blockquote>
<p>SROAPRT5</p>
</blockquote></td>
<td>SROAPRT6</td>
<td>SROAPRT7</td>
<td><blockquote>
<p>SROAPS1</p>
</blockquote></td>
<td><blockquote>
<p>SROAPS2</p>
</blockquote></td>
<td><blockquote>
<p>SROAR</p>
</blockquote></td>
<td><blockquote>
<p>SROAR1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROAR2</td>
<td><blockquote>
<p>SROARET</p>
</blockquote></td>
<td>SROARPT</td>
<td>SROASITE</td>
<td><blockquote>
<p>SROASS</p>
</blockquote></td>
<td><blockquote>
<p>SROASS1</p>
</blockquote></td>
<td><blockquote>
<p>SROASSE</p>
</blockquote></td>
<td><blockquote>
<p>SROASSN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROASSP</td>
<td><blockquote>
<p>SROAT0P</p>
</blockquote></td>
<td>SROAT0T</td>
<td>SROAT1P</td>
<td><blockquote>
<p>SROAT1T</p>
</blockquote></td>
<td><blockquote>
<p>SROAT2P</p>
</blockquote></td>
<td><blockquote>
<p>SROAT2T</p>
</blockquote></td>
<td><blockquote>
<p>SROATCM</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROATCM1</td>
<td><blockquote>
<p>SROATCM2</p>
</blockquote></td>
<td>SROATCM3</td>
<td>SROATM1</td>
<td><blockquote>
<p>SROATM2</p>
</blockquote></td>
<td><blockquote>
<p>SROATM3</p>
</blockquote></td>
<td><blockquote>
<p>SROATM4</p>
</blockquote></td>
<td><blockquote>
<p>SROATMIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROATMNO</td>
<td><blockquote>
<p>SROATT</p>
</blockquote></td>
<td>SROATT0</td>
<td>SROATT1</td>
<td><blockquote>
<p>SROATT2</p>
</blockquote></td>
<td><blockquote>
<p>SROAUTL</p>
</blockquote></td>
<td><blockquote>
<p>SROAUTL0</p>
</blockquote></td>
<td><blockquote>
<p>SROAUTL1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROAUTL2</td>
<td><blockquote>
<p>SROAUTL3</p>
</blockquote></td>
<td>SROAUTL4</td>
<td>SROAUTLC</td>
<td><blockquote>
<p>SROAWL</p>
</blockquote></td>
<td><blockquote>
<p>SROAWL1</p>
</blockquote></td>
<td><blockquote>
<p>SROAX</p>
</blockquote></td>
<td><blockquote>
<p>SROBLOD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROCAN</td>
<td><blockquote>
<p>SROCAN0</p>
</blockquote></td>
<td>SROCANUP</td>
<td>SROCASE</td>
<td><blockquote>
<p>SROCCAT</p>
</blockquote></td>
<td><blockquote>
<p>SROCD</p>
</blockquote></td>
<td><blockquote>
<p>SROCD0</p>
</blockquote></td>
<td><blockquote>
<p>SROCD1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROCD2</td>
<td><blockquote>
<p>SROCD3</p>
</blockquote></td>
<td>SROCD4</td>
<td>SROCDX</td>
<td><blockquote>
<p>SROCDX1</p>
</blockquote></td>
<td><blockquote>
<p>SROCDX2</p>
</blockquote></td>
<td><blockquote>
<p>SROCL1</p>
</blockquote></td>
<td><blockquote>
<p>SROCLAB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROCMP</td>
<td><blockquote>
<p>SROCMP1</p>
</blockquote></td>
<td>SROCMP2</td>
<td>SROCMPD</td>
<td><blockquote>
<p>SROCMPED</p>
</blockquote></td>
<td><blockquote>
<p>SROCMPL</p>
</blockquote></td>
<td><blockquote>
<p>SROCMPS</p>
</blockquote></td>
<td><blockquote>
<p>SROCNR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROCNR1</td>
<td><blockquote>
<p>SROCNR2</p>
</blockquote></td>
<td>SROCODE</td>
<td>SROCOM</td>
<td><blockquote>
<p>SROCOMP</p>
</blockquote></td>
<td><blockquote>
<p>SROCON</p>
</blockquote></td>
<td><blockquote>
<p>SROCON1</p>
</blockquote></td>
<td><blockquote>
<p>SROCOND</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROCPT</td>
<td><blockquote>
<p>SROCPT0</p>
</blockquote></td>
<td>SROCRAT</td>
<td>SROCVER</td>
<td><blockquote>
<p>SRODATE</p>
</blockquote></td>
<td><blockquote>
<p>SRODEL76</p>
</blockquote></td>
<td><blockquote>
<p>SRODELA</p>
</blockquote></td>
<td><blockquote>
<p>SRODEV</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRODIS</td>
<td><blockquote>
<p>SRODIS0</p>
</blockquote></td>
<td>SRODLA1</td>
<td>SRODLA2</td>
<td><blockquote>
<p>SRODLAY</p>
</blockquote></td>
<td><blockquote>
<p>SRODLT</p>
</blockquote></td>
<td><blockquote>
<p>SRODLT0</p>
</blockquote></td>
<td><blockquote>
<p>SRODLT1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRODLT2</td>
<td><blockquote>
<p>SRODPT</p>
</blockquote></td>
<td>SRODTH</td>
<td>SROERR</td>
<td><blockquote>
<p>SROERR0</p>
</blockquote></td>
<td><blockquote>
<p>SROERR1</p>
</blockquote></td>
<td><blockquote>
<p>SROERR2</p>
</blockquote></td>
<td><blockquote>
<p>SROERRPO</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROES</td>
<td><blockquote>
<p>SROESAD</p>
</blockquote></td>
<td>SROESAD1</td>
<td>SROESAR</td>
<td><blockquote>
<p>SROESAR0</p>
</blockquote></td>
<td><blockquote>
<p>SROESAR1</p>
</blockquote></td>
<td><blockquote>
<p>SROESAR2</p>
</blockquote></td>
<td><blockquote>
<p>SROESARA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROESHL</td>
<td><blockquote>
<p>SROESL</p>
</blockquote></td>
<td>SROESNR</td>
<td>SROESNR0</td>
<td><blockquote>
<p>SROESNR1</p>
</blockquote></td>
<td><blockquote>
<p>SROESNR2</p>
</blockquote></td>
<td><blockquote>
<p>SROESNR3</p>
</blockquote></td>
<td><blockquote>
<p>SROESNRA</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROESPR</td>
<td><blockquote>
<p>SROESPR1</p>
</blockquote></td>
<td>SROESPR2</td>
<td>SROESTV</td>
<td><blockquote>
<p>SROESUTL</p>
</blockquote></td>
<td><blockquote>
<p>SROESX</p>
</blockquote></td>
<td><blockquote>
<p>SROESX0</p>
</blockquote></td>
<td><blockquote>
<p>SROESXA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROESXP</td>
<td><blockquote>
<p>SROFILE</p>
</blockquote></td>
<td>SROFLD</td>
<td>SROGMTS</td>
<td><blockquote>
<p>SROGMTS0</p>
</blockquote></td>
<td><blockquote>
<p>SROGMTS1</p>
</blockquote></td>
<td><blockquote>
<p>SROGMTS2</p>
</blockquote></td>
<td><blockquote>
<p>SROGTSR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROHIS</td>
<td><blockquote>
<p>SROICD</p>
</blockquote></td>
<td>SROICU</td>
<td>SROICU1</td>
<td><blockquote>
<p>SROICU2</p>
</blockquote></td>
<td><blockquote>
<p>SROINQ</p>
</blockquote></td>
<td><blockquote>
<p>SROIRR</p>
</blockquote></td>
<td><blockquote>
<p>SROKEY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROKEY1</td>
<td><blockquote>
<p>SROKRET</p>
</blockquote></td>
<td>SROLABS</td>
<td>SROLOCK</td>
<td><blockquote>
<p>SROMED</p>
</blockquote></td>
<td><blockquote>
<p>SROMENU</p>
</blockquote></td>
<td><blockquote>
<p>SROMOD</p>
</blockquote></td>
<td><blockquote>
<p>SROMOD0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROMOR</td>
<td><blockquote>
<p>SROMORT</p>
</blockquote></td>
<td>SRONAN</td>
<td>SRONAN1</td>
<td><blockquote>
<p>SRONASS</p>
</blockquote></td>
<td><blockquote>
<p>SRONBCH</p>
</blockquote></td>
<td><blockquote>
<p>SRONEW</p>
</blockquote></td>
<td><blockquote>
<p>SRONIN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRONITE</td>
<td><blockquote>
<p>SRONON</p>
</blockquote></td>
<td>SRONOP</td>
<td>SRONOP1</td>
<td><blockquote>
<p>SRONOR</p>
</blockquote></td>
<td><blockquote>
<p>SRONOR1</p>
</blockquote></td>
<td><blockquote>
<p>SRONOR2</p>
</blockquote></td>
<td><blockquote>
<p>SRONOR3</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRONOR4</td>
<td><blockquote>
<p>SRONOR5</p>
</blockquote></td>
<td>SRONOR6</td>
<td>SRONOR7</td>
<td><blockquote>
<p>SRONOR8</p>
</blockquote></td>
<td><blockquote>
<p>SRONP</p>
</blockquote></td>
<td><blockquote>
<p>SRONP0</p>
</blockquote></td>
<td><blockquote>
<p>SRONP1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRONP2</td>
<td><blockquote>
<p>SRONPEN</p>
</blockquote></td>
<td>SRONRPT</td>
<td>SRONRPT0</td>
<td><blockquote>
<p>SRONRPT1</p>
</blockquote></td>
<td><blockquote>
<p>SRONRPT2</p>
</blockquote></td>
<td><blockquote>
<p>SRONRPT3</p>
</blockquote></td>
<td><blockquote>
<p>SRONUR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRONUR1</td>
<td><blockquote>
<p>SRONUR2</p>
</blockquote></td>
<td>SRONXR</td>
<td>SROOPRM</td>
<td><blockquote>
<p>SROOPRM1</p>
</blockquote></td>
<td><blockquote>
<p>SROP</p>
</blockquote></td>
<td><blockquote>
<p>SROP1</p>
</blockquote></td>
<td><blockquote>
<p>SROPAC0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROPAC1</td>
<td><blockquote>
<p>SROPACT</p>
</blockquote></td>
<td>SROPAT</td>
<td>SROPCE</td>
<td><blockquote>
<p>SROPCE0</p>
</blockquote></td>
<td><blockquote>
<p>SROPCE0A</p>
</blockquote></td>
<td><blockquote>
<p>SROPCE0B</p>
</blockquote></td>
<td><blockquote>
<p>SROPCE1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROPCEP</td>
<td><blockquote>
<p>SROPCEU</p>
</blockquote></td>
<td>SROPCEU0</td>
<td>SROPCEX</td>
<td><blockquote>
<p>SROPDEL</p>
</blockquote></td>
<td><blockquote>
<p>SROPECS</p>
</blockquote></td>
<td><blockquote>
<p>SROPECS1</p>
</blockquote></td>
<td><blockquote>
<p>SROPER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROPFSS</td>
<td><blockquote>
<p>SROPLIS</p>
</blockquote></td>
<td>SROPLIST</td>
<td>SROPLST1</td>
<td><blockquote>
<p>SROPLSTS</p>
</blockquote></td>
<td><blockquote>
<p>SROPPC</p>
</blockquote></td>
<td><blockquote>
<p>SROPREQ</p>
</blockquote></td>
<td><blockquote>
<p>SROPRI</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>SROPRI1</th>
<th><blockquote>
<p>SROPRI2</p>
</blockquote></th>
<th>SROPRIN</th>
<th><blockquote>
<p>SROPRIO</p>
</blockquote></th>
<th><blockquote>
<p>SROPRIT</p>
</blockquote></th>
<th><blockquote>
<p>SROPROC</p>
</blockquote></th>
<th><blockquote>
<p>SROPRPT</p>
</blockquote></th>
<th><blockquote>
<p>SROPS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>SROPS1</td>
<td><blockquote>
<p>SROPSEL</p>
</blockquote></td>
<td>SROPSN</td>
<td><blockquote>
<p>SROQ</p>
</blockquote></td>
<td><blockquote>
<p>SROQ0</p>
</blockquote></td>
<td><blockquote>
<p>SROQ0A</p>
</blockquote></td>
<td><blockquote>
<p>SROQ1</p>
</blockquote></td>
<td><blockquote>
<p>SROQ1A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROQ2</td>
<td><blockquote>
<p>SROQADM</p>
</blockquote></td>
<td>SROQD</td>
<td><blockquote>
<p>SROQD0</p>
</blockquote></td>
<td><blockquote>
<p>SROQD1</p>
</blockquote></td>
<td><blockquote>
<p>SROQIDP</p>
</blockquote></td>
<td><blockquote>
<p>SROQIDP0</p>
</blockquote></td>
<td><blockquote>
<p>SROQL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROQM</td>
<td><blockquote>
<p>SROQM0</p>
</blockquote></td>
<td>SROQM1</td>
<td><blockquote>
<p>SROQN</p>
</blockquote></td>
<td><blockquote>
<p>SROQT</p>
</blockquote></td>
<td><blockquote>
<p>SROR</p>
</blockquote></td>
<td><blockquote>
<p>SRORACE</p>
</blockquote></td>
<td><blockquote>
<p>SRORAT1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRORAT2</td>
<td><blockquote>
<p>SRORATA</p>
</blockquote></td>
<td>SRORATP</td>
<td><blockquote>
<p>SRORATS</p>
</blockquote></td>
<td><blockquote>
<p>SROREA</p>
</blockquote></td>
<td><blockquote>
<p>SROREA1</p>
</blockquote></td>
<td><blockquote>
<p>SROREA2</p>
</blockquote></td>
<td><blockquote>
<p>SROREAS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROREQ</td>
<td><blockquote>
<p>SROREQ1</p>
</blockquote></td>
<td>SROREQ2</td>
<td><blockquote>
<p>SROREQ3</p>
</blockquote></td>
<td><blockquote>
<p>SROREQ4</p>
</blockquote></td>
<td><blockquote>
<p>SROREST</p>
</blockquote></td>
<td><blockquote>
<p>SRORESV</p>
</blockquote></td>
<td><blockquote>
<p>SRORET</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRORHRS</td>
<td><blockquote>
<p>SRORHRS0</p>
</blockquote></td>
<td>SRORIN</td>
<td><blockquote>
<p>SRORTRN</p>
</blockquote></td>
<td><blockquote>
<p>SRORUT</p>
</blockquote></td>
<td><blockquote>
<p>SRORUT0</p>
</blockquote></td>
<td><blockquote>
<p>SRORUT1</p>
</blockquote></td>
<td><blockquote>
<p>SRORUT2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROSCH</td>
<td><blockquote>
<p>SROSCH1</p>
</blockquote></td>
<td>SROSCH2</td>
<td><blockquote>
<p>SROSNR</p>
</blockquote></td>
<td><blockquote>
<p>SROSNR1</p>
</blockquote></td>
<td><blockquote>
<p>SROSNR2</p>
</blockquote></td>
<td><blockquote>
<p>SROSPC1</p>
</blockquote></td>
<td><blockquote>
<p>SROSPEC</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROSPLG</td>
<td><blockquote>
<p>SROSPLG1</p>
</blockquote></td>
<td>SROSPLG2</td>
<td><blockquote>
<p>SROSPSS</p>
</blockquote></td>
<td><blockquote>
<p>SROSRPT</p>
</blockquote></td>
<td><blockquote>
<p>SROSTAFF</p>
</blockquote></td>
<td><blockquote>
<p>SROSTOP</p>
</blockquote></td>
<td><blockquote>
<p>SROSUR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROSUR1</td>
<td><blockquote>
<p>SROSUR2</p>
</blockquote></td>
<td>SROTHER</td>
<td><blockquote>
<p>SROTIUD</p>
</blockquote></td>
<td><blockquote>
<p>SROTRIG</p>
</blockquote></td>
<td><blockquote>
<p>SROTRPT</p>
</blockquote></td>
<td><blockquote>
<p>SROTRPT0</p>
</blockquote></td>
<td><blockquote>
<p>SROUNV</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROUNV1</td>
<td><blockquote>
<p>SROUNV2</p>
</blockquote></td>
<td>SROUTC</td>
<td><blockquote>
<p>SROUTED</p>
</blockquote></td>
<td><blockquote>
<p>SROUTIN</p>
</blockquote></td>
<td><blockquote>
<p>SROUTL</p>
</blockquote></td>
<td><blockquote>
<p>SROUTL0</p>
</blockquote></td>
<td><blockquote>
<p>SROUTL1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROUTLN</td>
<td><blockquote>
<p>SROUTUP</p>
</blockquote></td>
<td>SROVAR</td>
<td><blockquote>
<p>SROVER</p>
</blockquote></td>
<td><blockquote>
<p>SROVER1</p>
</blockquote></td>
<td><blockquote>
<p>SROVER2</p>
</blockquote></td>
<td><blockquote>
<p>SROVER3</p>
</blockquote></td>
<td><blockquote>
<p>SROWC</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SROWC1</td>
<td><blockquote>
<p>SROWC2</p>
</blockquote></td>
<td>SROWC3</td>
<td><blockquote>
<p>SROWL</p>
</blockquote></td>
<td><blockquote>
<p>SROWL0</p>
</blockquote></td>
<td><blockquote>
<p>SROWRQ</p>
</blockquote></td>
<td><blockquote>
<p>SROWRQ1</p>
</blockquote></td>
<td><blockquote>
<p>SROXPR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SROXR1</td>
<td><blockquote>
<p>SROXR2</p>
</blockquote></td>
<td>SROXR4</td>
<td><blockquote>
<p>SROXREF</p>
</blockquote></td>
<td><blockquote>
<p>SROXRET</p>
</blockquote></td>
<td><blockquote>
<p>SRSAVG</p>
</blockquote></td>
<td><blockquote>
<p>SRSAVL</p>
</blockquote></td>
<td><blockquote>
<p>SRSAVL1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSBD1</td>
<td><blockquote>
<p>SRSBDEL</p>
</blockquote></td>
<td>SRSBLOK</td>
<td><blockquote>
<p>SRSBOUT</p>
</blockquote></td>
<td><blockquote>
<p>SRSBUTL</p>
</blockquote></td>
<td><blockquote>
<p>SRSCAN</p>
</blockquote></td>
<td><blockquote>
<p>SRSCAN0</p>
</blockquote></td>
<td><blockquote>
<p>SRSCAN1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRSCAN2</td>
<td><blockquote>
<p>SRSCD</p>
</blockquote></td>
<td>SRSCDS</td>
<td><blockquote>
<p>SRSCDS1</p>
</blockquote></td>
<td><blockquote>
<p>SRSCDW</p>
</blockquote></td>
<td><blockquote>
<p>SRSCDW1</p>
</blockquote></td>
<td><blockquote>
<p>SRSCG</p>
</blockquote></td>
<td><blockquote>
<p>SRSCHAP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSCHC</td>
<td><blockquote>
<p>SRSCHC1</p>
</blockquote></td>
<td>SRSCHC2</td>
<td><blockquote>
<p>SRSCHCA</p>
</blockquote></td>
<td><blockquote>
<p>SRSCHCC</p>
</blockquote></td>
<td><blockquote>
<p>SRSCHD</p>
</blockquote></td>
<td><blockquote>
<p>SRSCHD1</p>
</blockquote></td>
<td><blockquote>
<p>SRSCHD2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRSCHDA</td>
<td><blockquote>
<p>SRSCHDC</p>
</blockquote></td>
<td>SRSCHK</td>
<td><blockquote>
<p>SRSCHOR</p>
</blockquote></td>
<td><blockquote>
<p>SRSCHUN</p>
</blockquote></td>
<td><blockquote>
<p>SRSCHUN1</p>
</blockquote></td>
<td><blockquote>
<p>SRSCHUP</p>
</blockquote></td>
<td><blockquote>
<p>SRSCONR</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSCOR</td>
<td><blockquote>
<p>SRSCPT</p>
</blockquote></td>
<td>SRSCPT1</td>
<td><blockquote>
<p>SRSCPT2</p>
</blockquote></td>
<td><blockquote>
<p>SRSCRAP</p>
</blockquote></td>
<td><blockquote>
<p>SRSDIS1</p>
</blockquote></td>
<td><blockquote>
<p>SRSDISP</p>
</blockquote></td>
<td><blockquote>
<p>SRSDT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRSGRPH</td>
<td><blockquote>
<p>SRSIND</p>
</blockquote></td>
<td>SRSKILL</td>
<td><blockquote>
<p>SRSKILL1</p>
</blockquote></td>
<td><blockquote>
<p>SRSKILL2</p>
</blockquote></td>
<td><blockquote>
<p>SRSMREQ</p>
</blockquote></td>
<td><blockquote>
<p>SRSPUT0</p>
</blockquote></td>
<td><blockquote>
<p>SRSPUT1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSPUT2</td>
<td><blockquote>
<p>SRSRBS</p>
</blockquote></td>
<td>SRSRBS1</td>
<td><blockquote>
<p>SRSRBW</p>
</blockquote></td>
<td><blockquote>
<p>SRSRBW1</p>
</blockquote></td>
<td><blockquote>
<p>SRSREQ</p>
</blockquote></td>
<td><blockquote>
<p>SRSREQUT</p>
</blockquote></td>
<td><blockquote>
<p>SRSRQST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRSRQST1</td>
<td><blockquote>
<p>SRSTCH</p>
</blockquote></td>
<td>SRSTIME</td>
<td><blockquote>
<p>SRSUP1</p>
</blockquote></td>
<td><blockquote>
<p>SRSUPC</p>
</blockquote></td>
<td><blockquote>
<p>SRSUPRG</p>
</blockquote></td>
<td><blockquote>
<p>SRSUPRQ</p>
</blockquote></td>
<td><blockquote>
<p>SRSUTIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSUTL</td>
<td><blockquote>
<p>SRSUTL2</p>
</blockquote></td>
<td>SRSWL</td>
<td><blockquote>
<p>SRSWL1</p>
</blockquote></td>
<td><blockquote>
<p>SRSWL10</p>
</blockquote></td>
<td><blockquote>
<p>SRSWL11</p>
</blockquote></td>
<td><blockquote>
<p>SRSWL12</p>
</blockquote></td>
<td><blockquote>
<p>SRSWL13</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRSWL14</td>
<td><blockquote>
<p>SRSWL15</p>
</blockquote></td>
<td>SRSWL2</td>
<td><blockquote>
<p>SRSWL3</p>
</blockquote></td>
<td><blockquote>
<p>SRSWL4</p>
</blockquote></td>
<td><blockquote>
<p>SRSWL5</p>
</blockquote></td>
<td><blockquote>
<p>SRSWL6</p>
</blockquote></td>
<td><blockquote>
<p>SRSWL7</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRSWL8</td>
<td><blockquote>
<p>SRSWL9</p>
</blockquote></td>
<td>SRSWLST</td>
<td><blockquote>
<p>SRSWREQ</p>
</blockquote></td>
<td><blockquote>
<p>SRTOVRF</p>
</blockquote></td>
<td><blockquote>
<p>SRTPASS</p>
</blockquote></td>
<td><blockquote>
<p>SRTPCOM</p>
</blockquote></td>
<td><blockquote>
<p>SRTPDONR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRTPHRT1</td>
<td><blockquote>
<p>SRTPHRT2</p>
</blockquote></td>
<td>SRTPHRT3</td>
<td><blockquote>
<p>SRTPHRT4</p>
</blockquote></td>
<td><blockquote>
<p>SRTPHRT5</p>
</blockquote></td>
<td><blockquote>
<p>SRTPHRT6</p>
</blockquote></td>
<td><blockquote>
<p>SRTPKID1</p>
</blockquote></td>
<td><blockquote>
<p>SRTPKID2</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRTPKID3</td>
<td><blockquote>
<p>SRTPKID4</p>
</blockquote></td>
<td>SRTPKID6</td>
<td><blockquote>
<p>SRTPLIV1</p>
</blockquote></td>
<td><blockquote>
<p>SRTPLIV2</p>
</blockquote></td>
<td><blockquote>
<p>SRTPLIV3</p>
</blockquote></td>
<td><blockquote>
<p>SRTPLIV4</p>
</blockquote></td>
<td><blockquote>
<p>SRTPLIV5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRTPLIV6</td>
<td><blockquote>
<p>SRTPLIV7</p>
</blockquote></td>
<td>SRTPLS</td>
<td><blockquote>
<p>SRTPLST</p>
</blockquote></td>
<td><blockquote>
<p>SRTPLSTP</p>
</blockquote></td>
<td><blockquote>
<p>SRTPLUN1</p>
</blockquote></td>
<td><blockquote>
<p>SRTPLUN2</p>
</blockquote></td>
<td><blockquote>
<p>SRTPLUN3</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRTPLUN5</td>
<td><blockquote>
<p>SRTPNEW</p>
</blockquote></td>
<td>SRTPPAS</td>
<td><blockquote>
<p>SRTPRACE</p>
</blockquote></td>
<td><blockquote>
<p>SRTPRH</p>
</blockquote></td>
<td><blockquote>
<p>SRTPRH1</p>
</blockquote></td>
<td><blockquote>
<p>SRTPRH2</p>
</blockquote></td>
<td><blockquote>
<p>SRTPRK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRTPRK1</td>
<td><blockquote>
<p>SRTPRK2</p>
</blockquote></td>
<td>SRTPRK3</td>
<td><blockquote>
<p>SRTPRLI</p>
</blockquote></td>
<td><blockquote>
<p>SRTPRLI1</p>
</blockquote></td>
<td><blockquote>
<p>SRTPRLI2</p>
</blockquote></td>
<td><blockquote>
<p>SRTPRLU</p>
</blockquote></td>
<td><blockquote>
<p>SRTPRLU1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SRTPRLU2</td>
<td><blockquote>
<p>SRTPSITE</p>
</blockquote></td>
<td>SRTPSS</td>
<td><blockquote>
<p>SRTPTM1</p>
</blockquote></td>
<td><blockquote>
<p>SRTPTM2</p>
</blockquote></td>
<td><blockquote>
<p>SRTPTMIT</p>
</blockquote></td>
<td><blockquote>
<p>SRTPTRAN</p>
</blockquote></td>
<td><blockquote>
<p>SRTPUTL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SRTPUTL4</td>
<td><blockquote>
<p>SRTPUTLC</p>
</blockquote></td>
<td>SRTPVAN</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 635 routines

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section contains information about the Surgery package options; first, the exported options are listed by name, and then they are provided alphabetically, with a description of the option.

# Options Listed by Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table contains a list of all of the options in the Surgery package, listed alphabetically by name.

| SR ANESTH REPORTS           | SR BLOOD PRODUCT VERIFICATION | SR BLOOD PRODUCT VERIFY AUDIT |
|-----------------------------|-------------------------------|-------------------------------|
| SR CPT ACCURACY             | SR CPT REPORTS                | SR MANAGE REPORTS             |
| SR NO ASSESSMENT REASON     | SR NON-OR INFO                | SR NON-OR REPORT              |
| SR NORMAL HOURS             | SR OR HOURS                   | SR OR UTIL                    |
| SR OR UTL1                  | SR PURGE UTILIZATION          | SR STAFFING REPORTS           |
| SR SURGERY REQUEST          | SR TRANSPLANT ASSESSMENT      | SR TRANSPLANT ENTER/EDIT      |
| SR TRANSPLANT PARAMETERS    | SR UPDATE FILES               | SR UPDATE SCHEDULE DEVIC      |
| SR UTIL EDIT ROOM           | SR VIEW HISTORICAL REPORTS    | SRCODING EDIT                 |
| SRCODING MENU               | SRCODING NURSE REPORT         | SRCODING OP REPORT            |
| SRCODING UPDATE/VERIFY MENU | SRHL DOWNLOAD INTERFACE FILES | SRHL DOWNLOAD SET OF CODES    |
| SRHL INTERFACE              | SRHL INTERFACE FLDS           | SRHL PARAMETER                |
| SRO CASES BY DISPOSITION    | SRO CASES BY PRIORITY         | SRO COMPLICATIONS MENU        |
| SRO DEATH RELATED           | SRO DEL MENU                  | SRO DELAY TIME                |
| SRO ECS COMPLIANCE          | SRO INTRAOP COMP              | SRO M&M VERIFICATION REPORT   |
| SRO PACKAGE MANAGEMENT      | SRO PCE NOTRANS               | SRO PCE STATUS                |
| SRO POSTOP COMP             | SRO QUARTERLY REPORT          | SRO SURGICAL PRIORITY         |
| SRO UPDATE CANCELLED CASE   | SRO UPDATE RETURNS            |                               |
| SRO-CHIEF REPORTS           | SRO-LRRP                      | SRO-ROOM                      |
| SRO-UNLOCK                  | SROA ASSESSMENT LIST          | SROA CARDIAC COMPLICATIONS    |
| SROA CARDIAC ENTER/EDIT     | SROA CARDIAC OPERATIVE RISK   | SROA CARDIAC PROCEDURES       |
| SROA CARDIAC RESOURCE       | SROA CARDIAC-OUTCOMES         | SROA CATHETERIZATION          |
| SROA CLINICAL INFORMATION   | SROA CODE ISSUE               | SROA COMPLETE ASSESSMENT      |
| SROA DEMOGRAPHICS           | SROA ENTER/EDIT               | SROA LAB                      |
| SROA LAB TEST EDIT          | SROA LAB-CARDIAC              | SROA MONTHLY WORKLOAD REPORT  |

| SROA ONE-LINER UPDATE | SROA OPERATION DATA       | SROA OUTCOMES             |
|-----------------------|---------------------------|---------------------------|
| SROA PREOP DATA       | SROA PRINT ASSESSMENT     | SROA REPRINT LETTERS      |
| SROA RISK ASSESSMENT  | SROA TRANSMIT ASSESSMENTS | SROA TRANSMITTED IN ERROR |
| SROACCT               | SROADOC                   | SROAMIS                   |
| SROANES               | SROANES MED               | SROANES-D                 |
| SROANES1              | SROANP                    | SROARPT                   |
| SROARSP               | SROASITE                  | SROATT                    |
| SROCAN                | SROCHIEF                  | SROCNR                    |
| SROCODE               | SROCOMP                   | SROCRAT                   |
| SRODELA               | SRODISP                   | SROERR BACKFILL           |
| SROICU                | SROKEY ENTER              | SROKEY MENU               |
| SROKEY REMOVE         | SROMEN-ANES               | SROMEN-ANES TECH          |
| SROMEN-COM            | SROMEN-M&M                | SROMEN-OP                 |
| SROMEN-OPINFO         | SROMEN-OUT                | SROMEN-PACU               |
| SROMEN-POST           | SROMEN-REFER              | SROMEN-REST               |
| SROMEN-STAFF          | SROMEN-VERF               | SROMEN-START              |
| SROMENU               | SROMM                     | SRONOP                    |
| SRONOP-ANNUAL         | SRONOP-EDIT               | SRONOP-ENTER              |
| SRONOR                | SRONOR-CODERS             | SRONRPT                   |
| SRONSR                | SROOPREQ                  | SROP REQ                  |
| SROPACT               | SROPARAM                  | SROPER                    |
| SROPLIST              | SROPLIST1                 | SROPPC                    |
| SROQ LIST OPS         | SROQ MENU                 | SROQ MISSING DATA         |
| SROQADM               | SROQD                     | SROQIDP                   |
| SROREAS               | SROREQ                    | SROREQV                   |
| SRORET                | SRORPTS                   | SROSCH                    |
| SROSCHOP              | SROSNR                    | SROSPEC                   |
| SROSRES               | SROSRPT                   | SROSTAFF                  |
| SROSUR                | SROTRPT                   | SROUNV                    |
| SROVER                | SROW-DELETE               | SROW-EDIT                 |
| SROW-ENTER            | SROWAIT                   | SROWC                     |
| SROWRQ                | SRSBDEL                   | SRSBOUT                   |
| SRSCAN                | SRSCD                     | SRSCHD1                   |
| SRSCHDA               | SRSCHDC                   | SRSCHUP                   |
| SRSCPT                | SRSRBS                    | SRSREQCC                  |
| SRSUPC                | SRSUPRQ                   | SRSWL2                    |
| SRSWREQ               | SRTASK-NIGHT              | SRTP ASSESSMENT LIST      |
| SRTP PRINT ASSESSMENT |                           |                           |

# Option Descriptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides an alphabetical listing of Surgery options, and includes a brief description of each option.

## Admissions w/in 14 days of Out Surgery if Postop Occ \[SROQADM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option provides a list of patients with completed outpatient surgical cases which resulted in at least one postoperative occurrence AND a hospital admission within 14 days of the surgery.

> *Alert Coder Regarding Coding Issues* \[SROA CODE ISSUE\]

> This option is used to provide the Risk Assessment Nurse Reviewers an electronic method to notify coders of potential coding issues or concerns. The message sent will include the basic Surgery case information and comments specifically added by the Nurse Reviewer.

> *Anesthesia AMIS* \[SROAMIS\]

> This report generates the Anesthesia AMIS Report required by Central Office (C.O.).

> *Anesthesia Data Entry Menu* \[SROANES-D\]

> This menu contains options used to enter or edit anesthesia related information.

> *Anesthesia Information (Enter/Edit)* \[SROMEN-ANES\]

> This option is used to enter Anesthesia related information for a given case.

> *Anesthesia Menu* \[SROANES1\]

> This menu contains the various options used to enter and display information related to the anesthesia technique and personnel.

> *Anesthesia Provider Report* \[SROADOC\]

> This report provides information concerning the Anesthesia staff and technique for completed cases. It will sort the cases by the principal anesthetist.

> *Anesthesia Report* \[SROARPT\]

> This option, locked by the SROANES security key, generates the Anesthesia Report containing anesthesia information for a surgical case. Before the report is electronically signed, the option displays information directly from the SURGERY file (#130) with the choice to edit the information on the report, to print/view the report from the beginning, and to sign the report electronically, if appropriate for the user. After the report is electronically signed, this option allows the signed report to be edited by updating the information in the SURGERY file (#130) and by creating addenda. This option also allows the report to be viewed or printed.

> *Anesthesia Reports* \[SR ANESTH REPORTS\] This menu contains various Anesthesia Reports, including the Anesthesia AMIS Report and List of Anesthetic Procedures.

> *Anesthesia Technique (Enter/Edit)* \[SROMEN-ANES TECH\]

> This option is used to enter information for the anesthesia technique used. Depending on what technique was used, a different set of fields may be entered.

> *Anesthesia for an Operation Menu* \[SROANES\]

> This menu contains the various Anesthesia related options used to input and display anesthesia staff and technique information.

> *Annual Report of Non-O.R. Procedures* \[SRONOP-ANNUAL\]

> This option is used to generate the Annual Report of Non-OR Procedures. It will display the total number of procedures based on CPT code.

## Annual Report of Surgical Procedures \[SROARSP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to generate the Annual Report of Surgical Procedures. It will count procedures within Surgical Specialties.

> *Attending Surgeon Reports* \[SROATT\]

> This option generates the Attending Surgeon Reports that displays staffing information for completed cases along with cumulative totals for each attending code. It can be sorted by surgical specialty and can be generated for an individual surgeon.

> *Blood Product Verification* \[SR BLOOD PRODUCT VERIFICATION\]

> The user can access this option through the *Operation Menu* \[SROPER\] option. After scanning the blood unit ID, the software will check for an association with the patient identified. If there are multiple entries with the Unit ID scanned, these entries will be listed along with the Blood Component, Patient Associated, and Expiration Date. The user will then be prompted to select the one that matches the blood product about to be administered. If the selected product is not associated with the patient identified, the warning message will be displayed.

> *CPT Code Reports* \[SR CPT REPORTS\]

> This menu contains reports based on CPT Codes. It includes the Cumulative Report of CPT Codes, Report of CPT Coding Accuracy, and the Report of Cases Missing CPT Codes.

> *CPT/ICD9 Coding Menu* \[SRCODING MENU\]

> This menu provides functionality for reviewing operations and non-OR procedures and for editing operation and non-OR procedure CPT and ICD-9 codes.

> *CPT/ICD9 Update/Verify Menu* \[SRCODING UPDATE/VERIFY MENU\] This menu contains options to be used by those responsible for entering CPT and ICD-9 codes for operations and non-OR procedures.

> *Cancel Scheduled Operation* \[SRSCAN\]

> This option is used to cancel a scheduled operation on a given date. When a scheduled case is cancelled, a new request is automatically generated for that case on the same date.

> *Cardiac Procedures Operative Data (Enter/Edit)* \[SROA CARDIAC PROCEDURES\] This option is used to enter or edit information related to cardiac procedures requiring cardiopulmonary bypass for the cardiac surgery risk assessments.

> *Cardiac Risk Assessment Information (Enter/Edit)* \[SROA CARDIAC ENTER/EDIT\]

> This menu contains options to enter or edit assessment information for the cardiac risk assessments.

> *Chief of Surgery Menu* \[SROCHIEF\]

> This menu contains the various options designed for use by the Chief of Surgery and his package coordinator.

## Circulating Nurse Staffing Report \[SROCNR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides nurse-staffing information, sorted by the circulating nurses’ name.

> *Clinical Information (Enter/Edit)* \[SROA CLINICAL INFORMATION\]

> This option is used to enter the clinical information required for the cardiac surgery risk assessments.

> *Comments* \[SROMEN-COM\]

> This option is used to enter general comments about a case.

## Comparison of Preop and Postop Diagnosis \[SROPPC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report contains completed cases in which the principal preoperative and principal postoperative diagnoses are different.

> *Create Service Blockout* \[SRSBOUT\]

### This option is used to block out times on the Operating Room Schedule by surgical specialty.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Cumulative Report of CPT Codes* \[SROACCT\]

> This report displays the total number of each CPT code entered for the date range selected. It also breaks down the totals into two categories, principal procedures and other operative procedures.

## Deaths Within 30 Days of Surgery \[SROQD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option lists patients who had surgery within the selected date range, who died within 30 days of surgery and whose deaths are included on the Quarterly/Summary Report. Three separate reports are available through this option corresponding to the three sections of the Quarterly Report that include death totals.

#### Total Cases Summary

> This report can be printed in one of three ways.

- All Cases: The report lists all patients who had surgery within the selected date range and who died within 30 days of surgery, along with all of the patients’ operations that were performed during the selected date range. These patients are included in the postoperative deaths totals on the Quarterly Report.
- Outpatient Cases Only: The report lists only the surgical cases that are associated with deaths that are counted as outpatient (ambulatory) deaths on the Quarterly Report.
- Inpatient Cases Only: The report lists only the surgical cases that are associated with deaths that are counted as inpatient deaths. Although the count of deaths associated with inpatient cases is not a part of the Quarterly Report, this report is provided to help with data validation.

#### Specialty Procedures

> This report will list the surgical cases that are associated with deaths that are counted for the national surgical specialty linked to the local surgical specialty. Cases are listed by national surgical specialty.

#### Index Procedures

> This report lists the surgical cases that are associated with deaths that are counted in the Index Procedures section of the Quarterly Report.

> *Delay and Cancellation Reports* \[SRO DEL MENU\]

> This menu contains various reports used to track delays and cancellations.

> *Delete Service Blockout* \[SRSBDEL\]

> This option is used to delete service blockouts already existing on a schedule.

> *Delete a Patient from the Waiting List* \[SROW-DELETE\]

> This option is used to delete a patient currently on the surgery waiting list for a selected service.

## Delete or Update Operation Requests \[SRSUPRQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to delete, change the date, or update the information entered on a requested operation.

> *Display Availability* \[SRODISP\]

> This option provides a graph of the availability of operating rooms. Times that are unavailable will be marked by “X”s.

> *Edit Non-O.R. Procedure* \[SRONOP-EDIT\]

> This option allows the editing of information on the pre-selected non-OR procedure.

> *Edit a Patient on the Waiting List* \[SROW-EDIT\]

> This option is used to edit a patient already on the waiting list for a selected surgical specialty.

> *Enter/Edit Transplant Assessments* \[SR TRANSPLANT ENTER/EDIT\]

> This option is used to enter the information required for the transplant assessments.

> *Enter Cardiac Catheterization & Angiographic Data* \[SROA CATHETERIZATION\] This option is used to enter or edit cardiac catheterization and angiographic information for cardiac surgery risk assessments.

> *Enter Irrigations and Restraints* \[SROMEN-REST\]

> This option is used to stuff in multiple restraints and positioning aids.

> *Enter PAC(U) Information* \[SROMEN-PACU\]

> This option is used to enter or edit recovery room scores and times.

> *Enter Referring Physician Information* \[SROMEN-REFER\]

> This option is used to enter the name, phone number, and address of the referring physician or institution.

> *Enter Restrictions for 'Person' Fields* \[SROKEY ENTER\]

> This option is used to enter restrictions on person fields. It will allow the user to add keys to existing entries in the PERSON FIELD RESTRICTION file (#131). If the field to be restricted has not already been entered in the PERSON FIELD RESTRICTION file (#131), the user may enter it along with the restricting keys through this option.

> *Enter a Patient on the Waiting List* \[SROW-ENTER\]

> This option is used to enter a patient on the waiting list for a selected surgical specialty.

> *Ensuring Correct Surgery Compliance Report* \[SRO ECS COMPLIANCE\]

> \*\* Not used after patch SR\*3\*175 \*\*

> This option produces the Ensuring Correct Surgery Compliance Report. This report is a two-part report:

1)  the compliance summary and (2) the list of non-compliant cases. The report is printed for a selected date range and may be sorted by surgical specialty. This report is a tool for reviewing compliance with the documentation process for ensuring correct surgery.

> *Exclusion Criteria (Enter/Edit)* \[SR NO ASSESSMENT REASON\] This option is used to flag major cases that will not have a surgery risk assessment due to certain exclusion criteria.

> *File Download* \[SRHL DOWNLOAD INTERFACE FILES\]

> This option is used to download Surgery interface files to the Automated Anesthesia Information System (AAIS). The process is currently being done by a screen capture to a file. In the future, this will be changed to a background task that can be queued to send Health Level 7 (HL7) master file updates.

## Flag Drugs for Use as Anesthesia Agents \[SROCODE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to flag drugs for use as anesthesia agents. Only those drugs that are flagged will be available when selecting anesthesia agents.

> *Flag Interface Fields* \[SRHL INTERFACE FLDS\]

> This option allows the package coordinator to set the INTERFACE field in the SURGERY INTERFACE file (#133.2). The categories listed on the first screen correspond to entries in the SURGERY INTERFACE file (#133.2). These categories are listed in the Surgery Health Level 7 Interface Specifications document as being the OBR (Observation Request) text identifiers. Each identifier corresponds to several fields in the VistA Surgery package. This allows the user to control the flow of data between the VistA Surgery package and the ancillary system on a field-by-field basis.

> The option lists each identifier and its current setting. To receive the data coming from the ancillary system for a category, set the flag to R for receive. To ignore the data, set the flag to N for not receive. To see a second underlying layer of OBX (Observation Information) text identifiers (fields in SURGERY file (#130) and their settings), set the OBR text identifier to RR for receive. The option will allow the user to toggle the settings for a range or for individual items.

> *Intraoperative Occurrences (Enter/Edit)* \[SRO INTRAOP COMP\]

> This option is used to enter or edit intraoperative occurrences. Every occurrence entered must have a corresponding perioperative occurrence category.

> *Key Missing Surgical Package Data* \[SROQ MISSING DATA\]

> This option generates a list of surgical cases performed within the selected date range that are missing key information. This report includes surgical cases with an entry in the TIME PAT IN OR field and does not include aborted cases.

> *Laboratory Interim Report* \[SRO-LRRP\]

> This option will print or display interim reports for a selected patient, within a given time period. The printout will go in inverse date order. This report will output all tests for the time period specified. If no results are available, the option will ask for another patient. This option will only print verified results and at present does not output the microbiology reports.

> *Laboratory Test Results (Enter/Edit)* \[SROA LAB\]

> This option is used to enter or edit laboratory information for an individual risk assessment.

> *Laboratory Test Results (Enter/Edit)* \[SROA LAB-CARDIAC\]

> This option is used to enter or edit laboratory information for an individual Cardiac risk assessment.

## List Completed Cases Missing CPT Codes \[SRSCPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The List Completed Cases Missing CPT Codes option generates a report of completed cases that are missing the Principal CPT code for a specified date range. It is important to note that only procedures that have CPT codes will be counted on the Annual Report of Surgical Procedures.

> *List Operation Requests* \[SRSRBS\]

> This option is designed to list requested cases, including those patients on the waiting list. It will print all future requests, sorted by ward location or surgical specialty.

> *List Scheduled Operations* \[SRSCD\]

> This option is designed to provide a short form listing of scheduled cases for a given date. It will sort by surgical specialty, operating room, or ward location and is designed to be displayed on the user’s CRT.

> *List of Anesthetic Procedures* \[SROANP\]

> This option generates the List of Anesthetic Procedures for a specified date range.

## List of Invasive Diagnostic Procedures \[SROQIDP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\* Not used after patch SR\*3\*175 \*\*

> This option provides a report listing the completed surgical cases that were performed during the selected date range and that have a principal CPT code on the list defined by Surgical Service at VHA Headquarters as invasive diagnostic procedures.

> *List of Operations* \[SROPLIST\]

> This report contains general information for completed cases within a selected date range. It includes the procedure(s), surgical service, surgeons and case type.

> *List of Operations (by Postoperative Disposition)* \[SRO CASES BY DISPOSITION\] This report will list completed cases for a selected date range sorted by postoperative disposition and by surgical specialty.

> *List of Operations (by Surgical Priority)* \[SRO CASES BY PRIORITY\] This report will list completed cases for a specified date range sorted by the surgical priority (elective, emergent, etc.). The patient name, patient social security number (SSN), date of operation, operative procedure, and surgical specialty will be displayed for each case.

> *List of Operations (by Surgical Specialty)* \[SROPLIST1\]

> This report contains general information for completed cases within a selected date range, sorted by surgical specialty. It includes procedure(s), surgical specialty, surgeons and case type.

> *List of Operations Included on Quarterly Report* \[SROQ LIST OPS\]

> \*\* Not used after patch SR\*3\*175 \*\*

> This option generates a list of completed operations that are included in the totals displayed on the Quarterly Report. The report displays the data fields that are checked by the Quarterly Report.

> *List of Surgery Risk Assessments* \[SROA ASSESSMENT LIST\]

> This option is used to print the List of Surgery Risk Assessments reports.

> *List of Transplant Assessments* \[SRTP ASSESSMENT LIST\]

> This option is used to print the List of Transplant Assessments. It will provide summary information for assessments within the sort parameters selected.

## List of Unverified Surgery Case \[SROUNV\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will generate a list of all completed surgery cases that have not had the procedure, diagnosis and complications verified.

> *M&M Verification Report* \[SRO M&M VERIFICATION REPORT\]

> The *M&M Verification Report* option produces the M&M Verification Report, which may be useful for:

- reviewing occurrences and their assignment to operations
- reviewing death unrelated/related assignments to operations

> The full report includes all patients who had operations within the selected date range who experienced intraoperative occurrences, postoperative occurrences or death within 90 days of surgery. The pre- transmission report is similar but includes operations with completed risk assessments that have not yet transmitted to the national database.

#### Full Report:

> Information is printed by patient, listing all operations for the patient that occurred during the selected date range, plus any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some operations that were performed prior to the selected date range and, if printed by specialty, may include operations performed by other specialties. For every operation listed, the intraoperative and postoperative occurrences are listed. The report indicates if the operation was flagged as unrelated or related to death and the risk assessment type and status. The report may be printed for a selected list of surgical specialties.

#### Pre-Transmission Report:

> Information is printed in a format similar to the full report. This report lists all completed risk assessed operations that have not yet transmitted to the national database and that have intraoperative occurrences, postoperative occurrences, or death within 90 days of surgery. The report includes any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some operations that may or may not be risk assessed, and, if risk assessed, may have a status other than 'complete'. However, every patient listed on this report will have at least one operation with a risk assessment status of 'complete'.

> *Maintain Surgery Waiting List* \[SROWAIT\]

> This menu contains options to enter, edit, and delete patients on the surgery waiting list. It also includes an option to print the list.

> *Make Operation Requests* \[SROOPREQ\]

> This option is used to “book” operations for a selected date. This request will in turn be scheduled for a specific operating room at a specific time on that date.

> *Make a Request for Concurrent Cases* \[SRSREQCC\]

> This option is used to request concurrent operative procedures.

## Make a Request from the Waiting List \[SRSWREQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to “book” a patient for surgery that has been entered on the waiting list. The operative procedure and specialty will be stuffed automatically.

> *Make Reports Viewable in CPRS* \[SR VIEW HISTORICAL REPORTS\] This option allows Operation Reports, Nurse Intraoperative Reports, Anesthesia Reports and Procedure Reports (Non-O.R.) for historical cases to be moved into TIU as "electronically unsigned" to make them viewable through the Computerized Patient Record System (CPRS).

> *Management Reports* \[SR MANAGE REPORTS\]

> This menu contains various management type reports used by the surgical service.

> *Management Reports* \[SRO-CHIEF REPORTS\]

> This menu contains various management reports to be generated by the Chief of Surgery.

> *Medications (Enter/Edit)* \[SROANES MED\]

> This option is used to enter or edit medications given during the operative procedure.

> *Monthly Surgical Case Workload Report* \[SROA MONTHLY WORKLOAD REPORT\] This option generates the Monthly Surgical Case Workload Report that may be printed and/or transmitted to the VASQIP national database.

## Morbidity & Mortality Reports \[SROMM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates the Morbidity and Mortality Reports to be used by the Chief of Surgery. This option includes the Mortality Report and Perioperative Occurrences Report.

> *Non-Cardiac Assessment Information (Enter/Edit)* \[SROA ENTER/EDIT\]

> This menu contains options used to enter and edit information related to individual risk assessments.

> *Non-O.R. Procedure Info* \[SR NON-OR INFO\]

> This option displays information on the selected non-OR procedure except the provider’s dictated summary. This information may be printed or reviewed on the screen.

> *Non-O.R. Procedures* \[SRONOP\]

> This menu contains options related to non-O.R. procedures.

> *Non-O.R. Procedures (Enter/Edit)* \[SRONOP-ENTER\]

> This option is used to enter, update, or delete information related to non-OR procedures.

## Non-Operative Occurrences (Enter/Edit) \[SROCOMP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to enter or edit occurrences that are not related to surgical procedures.

> *Normal Daily Hours (Enter/Edit)* \[SR NORMAL HOURS\]

> This option is used to enter or edit the daily start and end times for each operating room. The information is used to set up the start and end times, for operating room utilization, on a weekly basis.

> *Nurse Intraoperative Report* \[SRONRPT\]

> This option generates the Nurse Intraoperative Report, which contains surgical case information documented by nursing staff. Before the report is electronically signed, the option displays information directly from the SURGERY file (#130), giving the user choices to edit the information on the report, to print/view the report from the beginning, and to sign the report electronically if appropriate for the user. After the report is electronically signed, this option allows the signed report to be edited by updating the information in the SURGERY file (#130) and by creating addenda. This option also allows the signed report to be viewed or printed.

> *Nurse Intraoperative Report* \[SRCODING NURSE REPORT\] Coders use this option to print the Nurse Intraoperative Report for an operation. If the report is not electronically signed, the option displays information directly from the SURGERY file (#130), giving the choice to edit the information on the report, to print/view the report from the beginning, and to sign the report electronically if appropriate for the user. After the report is electronically signed, this option allows the signed report to be edited by updating the information in the SURGERY file (#130) and by creating addenda. This option also allows the signed report to be viewed or printed. This report is not available for non-OR procedures.

## Operating Room Information (Enter/Edit) \[SRO-ROOM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to enter or edit information pertinent to each operating room, including start and end times, and the cleaning time.

> *Operating Room Utilization (Enter/Edit)* \[SR UTIL EDIT ROOM\]

> This option is used to enter or edit start and end times for operating rooms on a selected date.

> *Operating Room Utilization Report* \[SR OR UTL1\]

> This report prints utilization information for a selected date range for all operating rooms or for a single operating room. The report displays the percent utilization, the number of cases, the total operation time and the time worked outside normal hours for each operating room individually and all operating rooms collectively.

> The percent utilization is derived by dividing the total operation time for all operations (including total time patients were in OR, plus the cleanup time allowed for each case, plus one hour allowance for startup and shutdown daily for each OR that had at least one case) by the total OR functioning time as defined in the SURGERY UTILIZATION file (#131.8). The quotient is then multiplied by 100.

> *Operation* \[SROMEN-OP\]

> This option is used to enter or edit information determined during the operative procedure.

> *Operation (Short Screen)* \[SROMEN-OUT\]

> This screen is designed for surgical procedures performed on outpatient or ambulatory patients with local anesthesia.

> *Operation Information* \[SROMEN-OPINFO\]

> This one page display allows the user to quickly reference primary information for a given case. There are no editing capabilities in this option.

> *Perioperative Complications (Enter/Edit)* \[SROA CARDIAC COMPLICATIONS\]

> This option is used to enter or edit perioperative complication information for cardiac surgery risk assessments.

> *Perioperative Occurrences Menu* \[SRO COMPLICATIONS MENU\] This menu contains options used to enter, edit, and display perioperative occurrence information. It is only accessible to those users that hold the SROCOMP security key.

> *Person Field Restrictions Menu* \[SROKEY MENU\]

> This menu contains options used to maintain restrictions applied to "person" type fields in files. One or more keys may be entered so that only those who have at least one of them may be entered in a particular field.

> *Post Operation* \[SROMEN-POST\]

> This option is used to enter or edit information obtained after the operation.

> *Postoperative Occurrences (Enter/Edit)* \[SRO POSTOP COMP\]

> This option is used to enter or edit information related to postoperative occurrences.

> *Preoperative Information (Enter/Edit)* \[SROA PREOP DATA\]

> The nurse reviewer uses this option to enter or edit preoperative assessment information.

> *Print 30 Day Follow-up Letters* \[SROA REPRINT LETTERS\] This option is used to print 30-day follow up letters. When using this option, letters can be printed for a specific assessment or all assessments within a selected date range.

> *Print Blood Product Verification Audit Log* \[SR BLOOD PRODUCT VERIFY AUDIT\] This option is used to print the KERNEL audit log for the Surgery *Blood Product Verification* \[SRBLOOD PRODUCT VERIFICATION\] option.

> *Print Surgery Waiting List* \[SRSWL2\]

> This option generates the long-form surgery waiting list for the surgical service(s) selected.

> *Print a Surgery Risk Assessment* \[SROA PRINT ASSESSMENT\]

> This option is used to print an entire Surgery Risk Assessment for an individual patient.

> *Print Transplant Assessment* \[SRTP PRINT ASSESSMENT\]

> This option is used to print a Surgery Transplant Assessment for an individual patient.

> *Procedure Report (Non-O.R.)* \[SR NON-OR REPORT\]

> This option generates the Procedure Report (Non-O.R.). This report consists of the electronically signed procedure summary (provider’s dictation) stored in the Text Integration Utilities (TIU) software.

> *Purge Utilization Information* \[SR PURGE UTILIZATION\] This option is used to purge utilization information for a selected date range. After selecting a starting date, the user may purge all utilization information for dates prior to, and including, that starting date.

> *Quarterly Report - Surgical Service* \[SRO QUARTERLY REPORT\]

> \*\* Not used after patch SR\*3\*175 \*\*

> This option will generate the Quarterly Report to be submitted to the Surgical Service, Central Office. The option also provides the flexibility to print the summary report for selected date ranges.

> Quarterly Report Menu \[SROQ MENU\]

> \*\* Not used after patch SR\*3\*175 \*\*

> This menu contains the option to generate the Quarterly Report and the associated options that may be helpful in validating information on the Quarterly Report.

> *Queue Assessment Transmissions* \[SROA TRANSMIT ASSESSMENTS\] This option may be used to manually queue the VASQIP transmission process to run at a selected time. The VASQIP transmission process is a part of the nightly maintenance and cleanup process.

> *Remove Restrictions on 'Person' Fields* \[SROKEY REMOVE\]

> This option is used to delete keys that have been assigned to a field to restrict entries. Using this option the user may delete one specific key, or all keys.

> *Report of CPT Coding Accuracy* \[SR CPT ACCURACY\]

> This report prints cases sorted by the CPT code used for principal and other operative procedures. It is designed as a tool to check the accuracy of coding procedures.

> *Report of Cancellation Rates* \[SROCRAT\]

> This option generates the Report of Cancellation Rates. The report can be printed for an individual Surgical Specialty, or the entire medical center. The report shows the following three rates:

1.  The cancellation percentage of all scheduled cases, calculated as follows: (TOTAL CANCELS / TOTAL SCHEDULED) x 100
2.  The avoidable cancellation percentage of all scheduled cases, calculated as follows: (TOTAL AVOIDABLE CANCELS / TOTAL SCHEDULED) x 100
3.  The avoidable cancellation percentage of all cancelled cases, calculated as follows: (TOTAL AVOIDABLE CANCELS / TOTAL CANCELS) x 100

> *Report of Cancellations* \[SROCAN\]

> This report provides information for cases that have been scheduled and cancelled.

> *Report of Cases Without Specimens* \[SROSPEC\]

> This report lists all completed cases in which there were no specimens taken from the operative site. It can be printed for an individual surgical specialty if desired.

## Report of Daily Operating Room Activity \[SROPACT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report provides a list of cases started between 6:00 AM on the date selected and 5:59 AM of the following day for all operating rooms.

> *Report of Delay Reasons* \[SROREAS\]

> This option prints the Report of Delay Reasons. This report will display the total number of times each reason was used for the date range selected. It can be sorted by surgical specialty or displayed for an individual surgical specialty.

> *Report of Delay Time* \[SRO DELAY TIME\]

> This report provides the total amount of delay time for each delay reason over a specified range of dates.

> *Report of Delayed Operations* \[SRODELA\]

> This report displays all cases that have been delayed. It will display both the delay cause and delay time.

> *Report of Non-O.R. Procedures* \[SRONOR\]

> This report lists chronologically Non-OR Procedures sorted by Medical Specialty, by provider, or by location.

> *Report of Non-O.R. Procedures* \[SRONOR-CODERS\]

> This report lists chronologically Non-OR Procedures sorted by Medical Specialty, by provider or by location.

> *Report of Normal Operating Room Hours* \[SR OR HOURS\]

> This report outputs the start time and the end time of the normal working hours for all operating rooms or for the selected operating room for each date within the specified date range. The total time of the normal working day is displayed for each operating room for each date.

> *Report of Returns to Surgery* \[SRORET\]

> This option generates a report listing information related to cases that have related surgical procedures within 30 days of the date of the operation.

> *Report of Surgical Priorities* \[SRO SURGICAL PRIORITY\]

> This report provides the total number of surgical cases for each Surgical Priority (i.e. Elective, Emergent, Urgent). It can be sorted by Surgical Specialty and printed for a specific specialty.

## Report of Unscheduled Admissions to ICU \[SROICU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report lists all unscheduled admissions to the ICU based on the requested (expected) postoperative care and actual postoperative disposition.

> *Request Operations* \[SROREQ\]

> This menu contains the various options used to make, delete, update and display requested operations.

> *Requests by Ward* \[SROWRQ\]

> This option prints request information for all wards, or a specific ward.

## Reschedule or Update a Scheduled Operation \[SRSCHUP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to change the date, time or operating room for which a case is scheduled. It may also be used to update information entered when the case was requested or scheduled.

> *Resource Data* \[SROA CARDIAC RESOURCE\] This option is used to enter, edit or review risk assessment cardiac patient demographic information such as hospital admission and discharge dates and other information related to this surgical episode.

> *Review Request Information* \[SROREQV\]

> This option is used to review or edit request information for an individual case.

> *Risk Model Lab Test (Enter/Edit)* \[SROA LAB TEST EDIT\]

> This option is used to allow the nurse to map VASQIP data in the Risk Model Lab Test (#139.2) file.

> *Schedule Anesthesia Personnel* \[SRSCHDA\]

> This option is used to schedule anesthesia personnel for surgery cases.

> *Schedule Operations* \[SROSCHOP\]

> This menu contains the various options used to schedule, update, cancel and display scheduled operations.

> *Schedule Requested Operations* \[SRSCHD1\]

> This option is used to schedule cases that have been previously “booked” for the selected date.

## Schedule Unrequested Concurrent Cases \[SRSCHDC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to schedule concurrent cases that have not been requested.

> *Schedule Unrequested Operations* \[SROSRES\]

> This option is used to schedule cases that have not been previously “booked.” The user will be asked to enter some initial information regarding this case as well as the operating room and date/time for it to be scheduled.

> *Schedule of Operations* \[SROSCH\]

> This option generates the Operating Room Schedule to be used by the OR nurses, surgeons and anesthetists.

> *Scrub Nurse Staffing Report* \[SROSNR\]

> This report contains general information for completed cases, sorted by the Operating Room Scrub Nurse.

> *Surgeon Staffing Report* \[SROSUR\]

> This report prints completed cases, sorted by the surgeon and his role (i.e. attending, first assistant) for each case. It includes the procedure, diagnosis and operation date/time.

## Surgeon's Verification of Diagnosis & Procedures \[SROVER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to verify that the procedure(s), diagnosis and complications are correct for the case. It is intended for use by the Surgeon, not the OR nurses.

> *Surgery Interface Management Menu* \[SRHL INTERFACE\]

> This menu contains options that allow the user to set up certain interface parameters that control the processing of HL7 messages. The interface adheres to the Health Level 7 (HL7) protocol and forms the basis for the exchange of health care information between the VistA Surgery package and any ancillary system.

> *Surgery Menu* \[SROMENU\]

> This is the main menu for the Surgery package.

> *Surgery Nightly Cleanup and Updates* \[SRTASK-NIGHT\]

> This option is queued to run daily. It initiates a number of background tasks to clean up the surgery database and update all appropriate information. Among the tasks done are calculation of average procedure times, cleanup of outstanding requests, update expected start and end times for operating rooms and surgical specialties, and locking cases.

> *Surgery Package Management Menu* \[SRO PACKAGE MANAGEMENT\] This menu contains options used to manage the Surgery package. It includes options to maintain site- configurable information within the package.

> *Surgery Reports* \[SRORPTS\]

> This menu contains the various reports used in the Surgery package. Those reports that are restricted to the Chief of Surgery do not appear within this menu.

> *Surgery Request* \[SR SURGERY REQUEST\]

> This protocol allows the entry and editing of operation requests through OE/RR.

## Surgery Risk Assessment - Site Update Server \[SROASITE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This server is used to update Surgery Risk Assessments that have been successfully transmitted to the Surgery Risk Assessment National Database. This server updates two fields, ASSESSMENT STATUS (#235) and DATE TRANSMITTED (#260). These fields are updated at the site from the message sent by the database servers only if the messages were processed successfully into the national database.

> *Surgery Risk Assessment Menu* \[SROA RISK ASSESSMENT\]

> This menu contains options used to create, maintain, and transmit surgery risk assessments.

> *Surgery Site Parameters (Enter/Edit)* \[SROPARAM\]

> This option is used to create or update local site parameters for the Surgery package.

> *Surgery Staffing Reports* \[SR STAFFING REPORTS\] This menu contains surgical staffing reports for surgeons and nurses.

> *Surgery Transplant Assessment - Site Update Server* \[SRTPSITE\]

> This server is used to update Surgery Transplant Assessments that have been successfully transmitted to the Surgery Risk Assessment National Database at the Chicago ISC. This server updates two fields, ASSESSMENT STATUS (#181) and DATE TRANSMITTED (#184). These fields are updated at the site from the message sent by the database servers at Chicago only if the messages were processed successfully into the national database.

> *Surgery Utilization Menu* \[SR OR UTIL\]

> This menu contains various Operating Room Utilization reports.

> *Surgical Nurse Staffing Report* \[SRONSR\]

> This option generates the Surgical Nurse Staffing Report for a specified date range.

> *Surgical Staff* \[SROMEN-STAFF\]

> This option is used to enter the staff (surgeons, nurses, anesthetists) for a given case. It includes everyone in the operating room for this case.

> *Table Download* \[SRHL DOWNLOAD SET OF CODES\]

> This option downloads the SURGERY file (#130) set of codes to the Automated Anesthesia Information System (AAIS). This process is currently being done by a screen capture to a file. In the future, this will be changed to a background task that can be queued to send HL7 master file updates.

> *Time Out Verified Utilizing Checklist* \[SROMEN-VERF\]

> This option is used to enter information related to Time Out Verified Utilizing Checklist.

> *Tissue Examination Report* \[SROTRPT\]

> This option is used to generate the Tissue Examination Report that contains culture and specimens sent to the laboratory.

> *Transplant Assessment Menu* \[SR TRANSPLANT ASSESSMENT\] This menu contains options to enter or edit transplant assessment information, print transplant assessments, list transplant assessments, and manage transplant assessments.

> *Transplant Assessment Parameters (Enter/Edit)* \[SR TRANSPLANT PARAMETERS\] This option is used to update local site parameters for the Surgery Transplants Assessment module. Each site can identify which type of organ transplant is performed or assessed by their Transplant Coordinator. Identification of the type of organ transplants done at your facility will streamline selections when doing data entry.

> *Unlock a Case for Editing* \[SRO-UNLOCK\]

> The Chief of Surgery (or a person designated by the Chief) uses this option to unlock a case that has been completed and locked.

> *Update 1-Liner Case* \[SROA ONE-LINER UPDATE\]

> This option may be used to enter missing data for the 1-liner cases (major cases marked for exclusion from assessment, minor cases and cardiac assessed cases that transmit to the VASQIP database as a single line or two of data). Cases edited with this option will be queued for transmission to the VASQIP database at Chicago.

> *Update Assessment Completed/Transmitted in Error* \[SROA TRANSMITTED IN ERROR\] This option is used to update the status of a completed or transmitted assessment that has been entered in error. The status will change from “COMPLETED” or “TRANSMITTED” to “INCOMPLETE” so that editing may occur.

> *Update Assessment Status to 'COMPLETE'* \[SROA COMPLETE ASSESSMENT\] This option is used to update the status of a risk assessment entry from “INCOMPLETE” to “COMPLETE.” Only completed assessments can be transmitted.

> *Update Cancellation Reason* \[SRSUPC\]

### This option is used to update the cancellation date and reason previously entered for a selected surgical case.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 38 Surgery V. 3.0 Technical Manual/Security Guide September 2011

> *Update Cancelled Case* \[SRO UPDATE CANCELLED CASE\]

> This option allows the Chief of Surgery to update information on a cancelled case.

> *Update Interface Parameter Field* \[SRHL PARAMETER\]

> This option may be used to edit the site parameter that determines which Surgery HL7 interface is used, the interface compatible with VistA HL7 V. 1.6 or the older one compatible with VistA HL7 V. 1.5.

> If applications communicating with the Surgery HL7 interface must use the interface designed for use with HL7 V. 1.5, enter YES. Otherwise, enter NO or leave this field blank.

> *Update O.R. Schedule Devices* \[SR UPDATE SCHEDULE DEVICE\] This option is used to update the list of O.R. Schedule Devices in the SURGERY SITE PARAMETERS file (#133).

> *Update Operations as Unrelated/Related to Death* \[SRO DEATH RELATED\]

> This option is used to update the status of operations performed within 90 days prior to death as unrelated or related to death, allowing comments to be entered to further document the review of death.

> *Update Site Configurable Files* \[SR UPDATE FILES\]

> This option is used to add, edit, or delete information in the site configurable files contained within the Surgery package.

> File entries that are not to be used should be made inactive and should not be deleted from the file.

> *Update Staff Surgeon Information* \[SROSTAFF\]

> This option allows the designation of a user as a staff surgeon by assigning the security key “SR STAFF SURGEON.” The Annual Report of Surgical Procedures counts cases performed by holders of this security key as performed by “STAFF.” All other cases are counted as performed by 'RESIDENT'.

> *Update Status of Returns Within 30 Days* \[SRO UPDATE RETURNS\]

> This option is used to update the status of Returns to Surgery within 30 days of a surgical case.

> *Update/Verify Procedure/Diagnosis Codes* \[SRCODING EDIT\]

> This option is used to edit and/or verify the final CPT and final ICD-9 codes for an operation or non-OR procedure.

> *View Patient Perioperative Occurrences* \[SROMEN-M&M\]

> This option displays perioperative occurrence information for a given case.

## Wound Classification Report \[SROWC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option generates a report for the selected date range showing the total number of surgical cases with each of the various wound classifications broken down by surgical service.

# Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section lists the templates provided with the Surgery package.

# Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following are input templates included with the Surgery package.

> SREQUEST file \#130

> SRISK-MISC file \#130

> SRISK-NOCARD file \#130

> SRISK-NOCOMP file \#130

> SRNON-OR file \#130

> SRNORRPT file \#130

> SRO-NOCOMP file \#130

> SROANES-AMIS file \#130

> SROARPT file \#130

> SROCOMP file \#130

> SROMEN-ANES file \#130 SROMEN-ANES TECH file \#130 SROMEN-COMP file \#130

> SROMEN-OPER file \#130

> SROMEN-OUT file \#130

> SROMEN-PACU file \#130

> SROMEN-POST file \#130

> SROMEN-REFER file \#130

> SROMEN-STAFF file \#130

> SROMEN-START file \#130

> SROMEN-VERF file \#130

> SRONRPT file \#130

> SROSRPT file \#130

> SROTHER file \#130

> SROVER file \#130

> SRPARAM file \#133

> SRSCHED-UNREQUESTED file \#130

> SRSREQV file \#130

> SRSRES-ENTRY file \#130

> SRSRES-SCHED file \#130

> SRSRES1 file \#130

> SROALAB file \#139.2

> SR TRANSPLANT file \#133

# Sort Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> One sort template is included:

> SR BLOOD PRODUCT VERIFICATION file \#19.081

#### List Scheduled Operations

> Operation Menu Locked with SROPER

> Operation Information Surgical Staff Operation Startup Operation

> Post Operation

> Enter PAC(U) Information Operation (Short Screen)

> Time Out Verified Utilizing Checklist

> Surgeon's Verification of Diagnosis & Procedures Locked with SROEDIT Anesthesia for an Operation Menu Locked with SROANES Anesthesia Information (Enter/Edit) Locked with SROANES

> Anesthesia Technique (Enter/Edit) Locked with SROANES

> Medications (Enter/Edit)

Anesthesia Report Locked with SROANES

> Schedule Anesthesia Personnel Operation Report

Anesthesia Report Locked with SROANES

> Nurse Intraoperative Report Tissue Examination Report

> Enter Referring Physician Information Locked with SROEDIT

> Enter Irrigations and Restraints Locked with SROEDIT

> Medications (Enter/Edit) Blood Product Verification

Anesthesia Menu Locked with SROANES

> Anesthesia Data Entry Menu Locked with SROANES

> Anesthesia Information (Enter/Edit) Locked with SROANES

> Anesthesia Technique (Enter/Edit) Locked with SROANES

> Medications (Enter/Edit)

Anesthesia Report Locked with SROANES

> Schedule Anesthesia Personnel

Perioperative Occurrences Menu Locked with SROCOMP

> Intraoperative Occurrences (Enter/Edit) Postoperative Occurrences (Enter/Edit)

> Non-Operative Occurrences (Enter/Edit) Locked with SROSURG

> Update Status of Returns Within 30 Days Morbidity & Mortality Reports

> Non-O.R. Procedures Locked with SROPER

> Non-O.R. Procedures Menu (Enter/Edit) Locked with SROPER

> Edit Non-O.R. Procedure Anesthesia Information (Enter/Edit) Medications (Enter/Edit) Anesthesia Technique (Enter/Edit) Procedure Report (Non-O.R.) Tissue Examination Report

> Non-OR Procedure Information

> Annual Report of Non-O.R. Procedures Locked with SROREP

> Report of Non-O.R. Procedures Locked with SROREP Comments Locked with SROPER

> Surgery Reports Locked with SROREP

> Management Reports

> Schedule of Operations (132 CRT) Annual Report of Surgical Procedures List of Operations

> List of Operations (by Postoperative Disposition) List of Operations (by Surgical Specialty)

> List of Operations (by Surgical Priority) Report of Surgical Priorities

> Report of Daily Operating Room Activity PCE Filing Status Report

> Outpatient Encounters Not Transmitted to NPCD Surgery Staffing Reports

> Attending Surgeon Reports Surgeon Staffing Report Surgical Nurse Staffing Report Scrub Nurse Staffing Report

> Circulating Nurse Staffing Report CPT Code Reports

> Cumulative Report of CPT Codes Report of CPT Coding Accuracy

> List Completed Cases Missing CPT Codes Missing Codes Report

#### Laboratory Interim Report

> Chief of Surgery Menu Locked with SROCHIEF

> View Patient Perioperative Occurrences Management Reports

> Morbidity & Mortality Reports M&M Verification Report

> Comparison of Preop and Postop Diagnosis Delay and Cancellation Reports

> Report of Delayed Operations Report of Delay Reasons Report of Delay Time

> Report of Cancellations Report of Cancellation Rates

> List of Unverified Surgery Cases Report of Returns to Surgery

> Report of Daily Operating Room Activity Report of Cases Without Specimens Report of Unscheduled Admissions to ICU Operating Room Utilization Report Wound Classification Report

> Print Blood Product Verification Audit Log Key Missing Surgical Package Data

> Admissions w/in 14 days of Out Surgery If Postop Occ Deaths Within 30 Days of Surgery

> Unlock a Case for Editing

> Update Status of Returns Within 30 Days

> Update Cancelled Case Locked with SROCHIEF

> Update Operations as Unrelated/Related to Death

> September 2011 Surgery V. 3.0 Technical Manual/Security Guide 69

> Surgery Package Management Menu Locked with SRCOORD

> Surgery Site Parameters (Enter/Edit) Operating Room Information (Enter/Edit)

> Surgery Utilization Menu Locked with SRCOORD

> Operating Room Utilization (Enter/Edit) Normal Daily Hours (Enter/Edit) Operating Room Utilization Report Report of Normal Operating Room Hours Purge Utilization Information

> Person Field Restrictions Menu

> Enter Restrictions for 'Person' Fields Remove Restrictions for 'Person' Fields

> Update O.R. Schedule Devices Update Staff Surgeon Information

> Flag Drugs for Use as Anesthesia Agents Update Site Configurable Files

> Backfill Order File with Surgical Cases Locked with SRCOORD

> Surgery Interface Management Menu Flag Interface Fields

> File Download Table Download

> Update Interface Parameter Field Make Reports Viewable in CPRS

> Surgery Risk Assessment Menu Locked with SR RISK ASSESSMENT

> Non-Cardiac Risk Assessment Information (Enter/Edit) Preoperative Information (Enter/Edit) Laboratory Test Results (Enter/Edit)

> Operation Information (Enter/Edit) Patient Demographics (Enter/Edit) Intraoperative Occurrences (Enter/Edit) Postoperative Occurrences (Enter/Edit) Update Status of Returns Within 30 Days

> Update Assessment Status to ‘COMPLETE’ Alert Coder Regarding Coding Issues

> Cardiac Risk Assessment Information (Enter/Edit) Clinical Information (Enter/Edit) Laboratory Test Results (Enter/Edit)

> Enter Cardiac Catheterization & Angiographic Data Operative Risk Summary Data (Enter/Edit)

> Cardiac Procedures Operative Data (Enter/Edit) Intraoperative Occurrences (Enter/Edit) Postoperative Occurrences (Enter/Edit) Outcome Information (Enter/Edit)

> Resource Data

> Update Assessment Status to ‘COMPLETE’ Alert Coder Regarding Coding Issues

> *(This page included for two-sided copying.)*

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table provides definitions for common terms used in this manual.
<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term/Acronym</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Aborted</td>
<td>Case status indicating the case was cancelled after the patient entered the operating room. Cases with ABORTED status must contain entries in the TIME PAT OUT OR field (#.232) and/or the TIME PAT IN OR field (#.205), plus the CANCEL DATE field (#17) and/or the CANCEL REASON field (#18).</td>
</tr>
<tr class="even">
<td>ASA Class</td>
<td>This is the American Society of Anesthesiologists’ classification relating to the patient’s physiologic status. Numbers followed by an “E” indicate an emergency.</td>
</tr>
<tr class="odd">
<td>Attending Code</td>
<td>Code that corresponds to the highest level of supervision provided by the attending staff surgeon during the procedure.</td>
</tr>
<tr class="even">
<td>Blockout Graph</td>
<td>Graph showing the availability of operating rooms.</td>
</tr>
<tr class="odd">
<td>Cancelled Case</td>
<td>Case status indicating that an entry has been made in the CANCEL DATE field (#17) and/or the CANCEL REASON field (#18) without the patient entering the operating room.</td>
</tr>
<tr class="even">
<td>CCSHS</td>
<td>VA Center for Cooperative Studies in Health Services located at Hines, Illinois.</td>
</tr>
<tr class="odd">
<td>Completed Case</td>
<td>Case status indicating that an entry has been made in the TIME PAT OUT OR (#.232) field.</td>
</tr>
<tr class="even">
<td>Concurrent Case</td>
<td>A patient undergoing two operations by different surgical specialties at the same time, or back-to-back, in the same operating room.</td>
</tr>
<tr class="odd">
<td>CPT Code</td>
<td>Current Procedural Terminology; also known as Operation Code.</td>
</tr>
<tr class="even">
<td>CRT</td>
<td>Cathode ray tube display. A display device that uses a cathode ray tube.</td>
</tr>
<tr class="odd">
<td>Enter</td>
<td>To type in information on a keyboard and press the Enter key (or the Return key for some keyboards) to send the information to the computer.</td>
</tr>
<tr class="even">
<td>Intraoperative Occurrence</td>
<td>Perioperative occurrence during the procedure.</td>
</tr>
<tr class="odd">
<td>Major</td>
<td>Any operation performed under general, spinal, or epidural anesthesia plus all inguinal herniorrhaphies and carotid endarterectomies, regardless of anesthesia administered.</td>
</tr>
<tr class="even">
<td>Minor</td>
<td>All operations not designated as Major.</td>
</tr>
<tr class="odd">
<td>New Surgical Case</td>
<td>A surgical case that has not been previously requested or scheduled such as an emergency case. A surgical case entered in the records without being booked through scheduling will not appear on the Schedule of Operations or as an operative request.</td>
</tr>
<tr class="even">
<td>Non-Operative Occurrence</td>
<td>Occurrence that develops before a surgical procedure is performed.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term/Acronym</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Not Complete</td>
<td><p>Case status indicating one of the following two situations with no entry in the TIME PAT OUT OR field (#.232):</p>
<ol type="1">
<li><p>Case has entry in TIME PAT IN OR field (#.205).</p></li>
<li><p>Case has not been requested or scheduled.</p></li>
</ol></td>
</tr>
<tr class="even">
<td>Operation Code</td>
<td>Identifying code for reporting medical services and procedures performed by physicians. See CPT Code.</td>
</tr>
<tr class="odd">
<td>PACU</td>
<td>Post Anesthesia Care Unit.</td>
</tr>
<tr class="even">
<td>Postoperative Occurrence</td>
<td>Perioperative occurrence following the procedure.</td>
</tr>
<tr class="odd">
<td>Procedure Occurrence</td>
<td>Occurrence related to a non-OR procedure.</td>
</tr>
<tr class="even">
<td>Requested</td>
<td>Operation has been slotted for a particular day but the time and operating room are not yet firm.</td>
</tr>
<tr class="odd">
<td>Risk Assessment</td>
<td>A module of the Surgery software that provides medical centers a mechanism to track information related to surgical risk and operative mortality. Completed assessments are transmitted to the NSQIP or the CICSP national database for statistical analysis.</td>
</tr>
<tr class="even">
<td>Scheduled</td>
<td>Operation has both an operating room and a scheduled starting time, but the operation has not yet begun.</td>
</tr>
<tr class="odd">
<td>Screen</td>
<td>An illuminated display surface on which display images are presented.</td>
</tr>
<tr class="even">
<td>Screen Server</td>
<td>A format for displaying data on a cathode ray tube display. Screen Server is designed specifically for the Surgery Package.</td>
</tr>
<tr class="odd">
<td>Screen Server Function</td>
<td>The Screen Server prompt for data entry.</td>
</tr>
<tr class="even">
<td>Service Blockouts</td>
<td>The reservation of an operating room for a particular service on a recurring basis. The reservation is charted on a blockout graph.</td>
</tr>
<tr class="odd">
<td>Transplant Assessment</td>
<td>A module of the Surgery software that provides medical centers a mechanism to track information related to surgical transplant risk and operative mortality. Completed assessments are transmitted to the NSQIP or the CICSP national database for statistical analysis.</td>
</tr>
<tr class="even">
<td>VASQIP</td>
<td>VA Surgical Quality Improvement Program.</td>
</tr>
</tbody>
</table>

# APPENDIX A: Surgery Source Data Elements for PFSS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Patient Financial Services System (PFSS) project required the addition of the GET ACCOUNT call (e.g., \$\$GETACCT^IBBAPI) to the Surgery package. This appendix provides information regarding the data that is sent from Surgery to other applications during these Surgery functions using the GET ACCOUNT call:

- Surgery Consult
- Surgery Case Creation
- Surgery Case Update
- Surgery Case Deleted/Cancelled
- Send Case to PCE

# Surgery Request Consult Data Source for Get Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This table displays the information that the Surgery package sends when making the Get Account call during a consult request for Surgery. When a “surgery request” consult is created in the Consults package, the Surgery package will process the GET ACCOUNT call.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 27%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Surgery Request Get Account Data Element</strong></th>
<th><strong>Attributes</strong></th>
<th><strong>Source File and Field</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patient</td>
<td>IEN</td>
<td>From the 4th piece of the PID segment of the consult message received by Surgery. Pointer to the PATIENT file (#2).</td>
</tr>
<tr class="even">
<td>Account number reference</td>
<td>Hard coded “G”</td>
<td></td>
</tr>
<tr class="odd">
<td>HL7 Message Type</td>
<td>Hard Coded “A05”</td>
<td></td>
</tr>
<tr class="even">
<td>Account number reference Location</td>
<td>Null</td>
<td></td>
</tr>
<tr class="odd">
<td>Patient Class</td>
<td>"O" = Outpatient</td>
<td>Always defaulted to "O" = Outpatient for the Surgery Request Consult.</td>
</tr>
<tr class="even">
<td>Patient Location</td>
<td>Pointer to the HOSPITAL LOCATION file (#44)</td>
<td>From the 4<sup>th</sup> piece of the PV1 segment of the consult message received by Surgery. Pointer to the HOSPITAL LOCATION file (#44).</td>
</tr>
<tr class="odd">
<td>Planned Date/Time of Operation</td>
<td>Free Text</td>
<td>From the free text consult string; use today’s date and time if date/time cannot be found.</td>
</tr>
<tr class="even">
<td>Surgeon</td>
<td><p>IEN of the NEW PERSON</p>
<p>file (#200), or null</p></td>
<td>Surgery will attempt to resolve the free text provider name against the NEW PERSON file (#200) to obtain the IEN. If the IEN cannot be found, Surgery will pass a null value in this field. IDX will add a generic provider in CBO when creating the visit in IDX.</td>
</tr>
<tr class="odd">
<td>Attending Surgeon</td>
<td><p>IEN of the NEW PERSON</p>
<p>file (#200), or null</p></td>
<td>Surgery will attempt to resolve the free text provider name against the NEW PERSON file (#200) to obtain the IEN. If the IEN cannot be found, Surgery will pass a null value in this field. IDX will add a generic provider in CBO when creating the visit in IDX.</td>
</tr>
</tbody>
</table>