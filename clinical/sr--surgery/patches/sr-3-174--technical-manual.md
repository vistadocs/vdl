---
title: SR*3*174  Surgery VASQIP 2010 Technical Manual/Security Guide Change Pages
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: Surgery VASQIP 2010 /Security Guide Change Pages
app_code: SR
app_name: Surgery
section: CLI
app_status: active
pkg_ns: SR
patch_ver: 3
patch_id: SR*3*174
group_key: "SR:SR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: > ![](sr-3-174-surgery-vasqip-2010-technical-manual-security-guide-change-pages/001.png)
audience: 
keywords: 
  - table
  - contents
  - surgery
  - strong
  - report
  - technical
  - manual
  - security
  - guide
  - style
page_count: 0
word_count: 276
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 1993
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr_3_p174_tm_cp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Surgery/sr_3_p174_tm_cp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=103"
---

> ![](sr-3-174-surgery-vasqip-2010-technical-manual-security-guide-change-pages/001.png)

SURGERY

> TECHNICAL MANUAL/ SECURITY GUIDE

> Version 3.0

> July 1993

> (Revised December 2010)

> Department of Veterans Affairs Office of Enterprise Development

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
<td>12/10</td>
<td>i, 27</td>
<td><blockquote>
<p>SR*3*174</p>
</blockquote></td>
<td><p>Change in definition of List of Surgery Risk Assessments report.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
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

December 2010 Surgery V. 3.0 Technical Manual/Security Guide i

> SR\*3\*174

> Introduction 1

> Overview 1

> Organization 1

> Requesting and Scheduling 1

> Tracking Clinical Procedures 1

> Generating Surgical Reports 2

> Chief of Surgery Reporting 2

> Managing the Software Package 2

> Assessing Surgical Risk 2

> Assessing Surgical Transplants 2

> Documentation Conventions 3

> Getting Help and Exiting 3

## Technical Manual 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Implementation and Maintenance 7

> Installation 7

> Site Specific Parameters 7

> Files 14

> File Descriptions 16

> Routines 18

> Exported Options 20

> Options Listed by Name 20

> Option Descriptions 22

> Templates 40

> Input Templates 40

> Sort Template 40

> Editing Input Templates 41

> Globals in the Surgery Package 42

> Journaling Globals 42

> Archiving And Purging 44

> Archiving 44

> Purging 44

> Callable Routines 46

> External Relations 48

> Packages Needed to Run Surgery 48

> Calls Made by Surgery 48

> Database Integration Agreements 52

> Internal Relations 54

> Package-Wide Variables 56

## Security Guide 58

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ii Surgery V. 3.0 Technical Manual/Security Guide November 2008

> *List Operation Requests* \[SRSRBS\]

> This option is designed to list requested cases, including those patients on the waiting list. It will print all future requests, sorted by ward location or surgical specialty.

> *List Scheduled Operations* \[SRSCD\]

> This option is designed to provide a short form listing of scheduled cases for a given date. It will sort by surgical specialty, operating room, or ward location and is designed to be displayed on the user’s CRT.

> *List of Anesthetic Procedures* \[SROANP\]

> This option generates the List of Anesthetic Procedures for a specified date range.

> *List of Invasive Diagnostic Procedures* \[SROQIDP\]

> This option provides a report listing the completed surgical cases that were performed during the selected date range and that have a principal CPT code on the list defined by Surgical Service at VHA Headquarters as invasive diagnostic procedures.

> *List of Operations* \[SROPLIST\]

> This report contains general information for completed cases within a selected date range. It includes the procedure(s), surgical service, surgeons and case type.

> *List of Operations (by Postoperative Disposition)* \[SRO CASES BY DISPOSITION\] This report will list completed cases for a selected date range sorted by postoperative disposition and by surgical specialty.

> *List of Operations (by Surgical Priority)* \[SRO CASES BY PRIORITY\] This report will list completed cases for a specified date range sorted by the surgical priority (elective, emergent, etc.). The patient name, patient social security number (SSN), date of operation, operative procedure, and surgical specialty will be displayed for each case.

> *List of Operations (by Surgical Specialty)* \[SROPLIST1\]

> This report contains general information for completed cases within a selected date range, sorted by surgical specialty. It includes procedure(s), surgical specialty, surgeons and case type.

> *List of Operations Included on Quarterly Report* \[SROQ LIST OPS\]

> This option generates a list of completed operations that are included in the totals displayed on the Quarterly Report. The report displays the data fields that are checked by the Quarterly Report.

> *List of Surgery Risk Assessments* \[SROA ASSESSMENT LIST\]

> This option is used to print the List of Surgery Risk Assessments reports.

> *List of Transplant Assessments* \[SRTP ASSESSMENT LIST\]

> This option is used to print the List of Transplant Assessments. It will provide summary information for assessments within the sort parameters selected.

December 2010 Surgery V. 3.0 Technical Manual/Security Guide 27

> SR\*3\*174

# List of Unverified Surgery Case \[SROUNV\]


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Technical Manual 5](#technical-manual-5)
  - [Security Guide 58](#security-guide-58)
- [List of Unverified Surgery Case \[SROUNV\]](#list-of-unverified-surgery-case-srounv)
  - [Full Report:](#full-report)
  - [Pre-Transmission Report:](#pre-transmission-report)
- [Make a Request from the Waiting List \[SRSWREQ\]](#make-a-request-from-the-waiting-list-srswreq)
> This option will generate a list of all completed surgery cases that have not had the procedure, diagnosis and complications verified.
> *M&M Verification Report* \[SRO M&M VERIFICATION REPORT\]
> The *M&M Verification Report* option produces the M&M Verification Report, which may be useful for:
- reviewing occurrences and their assignment to operations
- reviewing death unrelated/related assignments to operations
> The full report includes all patients who had operations within the selected date range who experienced intraoperative occurrences, postoperative occurrences or death within 90 days of surgery. The pre- transmission report is similar but includes operations with completed risk assessments that have not yet transmitted to the national database.

## Full Report:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Information is printed by patient, listing all operations for the patient that occurred during the selected date range, plus any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some operations that were performed prior to the selected date range and, if printed by specialty, may include operations performed by other specialties. For every operation listed, the intraoperative and postoperative occurrences are listed. The report indicates if the operation was flagged as unrelated or related to death and the risk assessment type and status. The report may be printed for a selected list of surgical specialties.

## Pre-Transmission Report:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Information is printed in a format similar to the full report. This report lists all completed risk assessed operations that have not yet transmitted to the national database and that have intraoperative occurrences, postoperative occurrences, or death within 90 days of surgery. The report includes any operations that may have occurred within 30 days prior to any postoperative occurrences or within 90 days prior to death. Therefore, this report may include some operations that may or may not be risk assessed, and, if risk assessed, may have a status other than 'complete'. However, every patient listed on this report will have at least one operation with a risk assessment status of 'complete'.

> *Maintain Surgery Waiting List* \[SROWAIT\]

> This menu contains options to enter, edit, and delete patients on the surgery waiting list. It also includes an option to print the list.

> *Make Operation Requests* \[SROOPREQ\]

> This option is used to “book” operations for a selected date. This request will in turn be scheduled for a specific operating room at a specific time on that date.

> *Make a Request for Concurrent Cases* \[SRSREQCC\]

> This option is used to request concurrent operative procedures.

# Make a Request from the Waiting List \[SRSWREQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option is used to “book” a patient for surgery that has been entered on the waiting list. The operative procedure and specialty will be stuffed automatically.

> 28 Surgery V. 3.0 Technical Manual/Security Guide November 2008