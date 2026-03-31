---
title: PXRM*2*18 High Risk Mental Health Patient Reminder and Flag User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: High Risk Mental Health Patient Reminder and Flag
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*18
group_key: "PXRM:PXRM:2"
file_numbers: 
  - 40
  - 44
security_keys: []
menu_options: 5
description: > ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/001.png)
audience: 
keywords: 
  - table
  - reminder
  - blockquote
  - contents
  - health
  - class
  - patient
  - mental
  - risk
  - high
page_count: 0
word_count: 8999
section_count: 7
table_count: 3
figure_count: 1
appendix_count: 5
has_toc: False
is_stub: False
pub_date: April 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/001.png)

> Clinical Reminders

> High Risk Mental Health Patient – National Reminder and Flag

# Patch 24


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Patch 24](#patch-24)
  - [April 2013](#april-2013)
  - [Revision History](#revision-history)
- [<u>Table of Contents</u>](#utable-of-contentsu)
- [<u>Introduction</u>](#uintroductionu)
    - [Related Documentation](#related-documentation)
    - [Clinical Reminders PXRM\2\24 Documentation](#clinical-reminders-pxrm224-documentation)
- [<u>Background</u>](#ubackgroundu)
- [High Risk MH Patient Process Flow Overview](#high-risk-mh-patient-process-flow-overview)
    - [![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/020.png) The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.](#pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual020png-the-new-reminder-location-list-is-consistent-with-the-national-list-of-mh-encounter-stop-codes-defined-for-sites-by-the-office-of-mental-health-services)
- [<u>High Risk Mental Health Scheduling Reports</u>](#uhigh-risk-mental-health-scheduling-reportsu)
    - [New or Revised Scheduling Reports](#new-or-revised-scheduling-reports)
    - [Assign Menu Options to MH staff](#assign-menu-options-to-mh-staff)
    - [No Show Nightly Background Job](#no-show-nightly-background-job)
    - [Examples](#examples)
    - [Example 1 – HRMH NO SHOW Nightly Report](#example-1-hrmh-no-show-nightly-report)
- [Documenting Results of Follow-up in a Reminder Dialog](#documenting-results-of-follow-up-in-a-reminder-dialog)
    - [High Risk MH No Show Follow-up Reminder](#high-risk-mh-no-show-follow-up-reminder)
    - [Steps to process reminder:](#steps-to-process-reminder)
    - [Opening screen](#opening-screen)
    - [Additional Supporting Information](#additional-supporting-information)
    - [Patient Contact made and plan put in place for ongoing care](#patient-contact-made-and-plan-put-in-place-for-ongoing-care)
    - [Patient sought urgent or emergent health care](#patient-sought-urgent-or-emergent-health-care)
    - [Three unsuccessful attempts made to contact patient](#three-unsuccessful-attempts-made-to-contact-patient)
    - [Other Outcome](#other-outcome)
    - [Suicide Attempted or Completed](#suicide-attempted-or-completed)
    - [Suicide Behavior Report (SBR) Example](#suicide-behavior-report-sbr-example)
    - [Click Finish to see the Progress Note](#click-finish-to-see-the-progress-note)
- [<u>VA-MHTC Needs Assignment Reminder Definition</u>](#uva-mhtc-needs-assignment-reminder-definitionu)
    - [![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/048.png) The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.](#pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual048png-the-new-reminder-location-list-is-consistent-with-the-national-list-of-mh-encounter-stop-codes-defined-for-sites-by-the-office-of-mental-health-services)
    - [Example of running Reminder Due Report, without saving template](#example-of-running-reminder-due-report-without-saving-template)
    - [Template Example](#template-example)
- [High Risk Mental Health Ad Hoc Scheduling Report Example](#high-risk-mental-health-ad-hoc-scheduling-report-example)
    - [Example of High Risk MH No-Show Adhoc Report](#example-of-high-risk-mh-no-show-adhoc-report)
- [High Risk Mental Health Health Summary <u>Components and Types</u>](#high-risk-mental-health-health-summary-ucomponents-and-typesu)
    - [Example: Health Summary with HRMH components](#example-health-summary-with-hrmh-components)
    - [New Health Summary Types distributed by the High Risk Mental Health Patient project:](#new-health-summary-types-distributed-by-the-high-risk-mental-health-patient-project)
- [<u>Order Entry (OR) MHTC Notification</u>](#uorder-entry-or-mhtc-notificationu)
    - [\\\Important Note\\\](#important-note)
- [Scheduling Report Examples](#scheduling-report-examples)
    - [High Risk Mental Health NO Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\]](#high-risk-mental-health-no-show-nightly-report-sd-mh-no-show-nightly-bgj)
    - [This is how the report will display to the screen when reading Mailman.](#this-is-how-the-report-will-display-to-the-screen-when-reading-mailman)
    - [Example of the High Risk Mental Health NO Show Ad Hoc report](#example-of-the-high-risk-mental-health-no-show-ad-hoc-report)
    - [Example of High Risk MH No-Show Adhoc Report by Mental Health Clinic](#example-of-high-risk-mh-no-show-adhoc-report-by-mental-health-clinic)
  - [Ad Hoc Report Examples – After reminder follow-up](#ad-hoc-report-examples-after-reminder-follow-up)
    - [Example of High Risk MH No-Show Adhoc Report by Mental Health Clinic](#example-of-high-risk-mh-no-show-adhoc-report-by-mental-health-clinic-1)
    - [NOTE: Prerequisites to writing Progress Notes in CPRS to document PRF activity](#note-prerequisites-to-writing-progress-notes-in-cprs-to-document-prf-activity)
    - [New options for key SPC or MH Professional for PRF Transmission Management](#new-options-for-key-spc-or-mh-professional-for-prf-transmission-management)
    - [Ownership of Category 1 flag](#ownership-of-category-1-flag)
    - [Transmission Management](#transmission-management)
    - [Record Flag Transmission Errors Option Description](#record-flag-transmission-errors-option-description)
    - [Example:](#example)
- [Appendix A: Clinical Reminders and CPRS Overview](#appendix-a-clinical-reminders-and-cprs-overview)
    - [Right-clicking on a Reminder](#right-clicking-on-a-reminder)
    - [Clock Button](#clock-button)
    - [Action Menu](#action-menu)
    - [Notes Tab](#notes-tab)
  - [Processing/ Resolving Clinical Reminders](#processing-resolving-clinical-reminders)
- [Appendix B: Glossary](#appendix-b-glossary)
  - [OI Master Glossary:](#oi-master-glossary)
    - [National Acronym Directory:](#national-acronym-directory)
  - [Acronyms](#acronyms)
    - [Definitions](#definitions)
- [<u>Appendix C: Edit Cover Sheet Reminder List</u>](#uappendix-c-edit-cover-sheet-reminder-listu)
- [Appendix D: Creating a Mental Health Test button for use in a Reminder Dialog](#appendix-d-creating-a-mental-health-test-button-for-use-in-a-reminder-dialog)
- [<u>Appendix E: Tips, Tricks, and FAQs</u>](#uappendix-e-tips-tricks-and-faqsu)
    - [When filling out reminder dialogs, don't click the Finish button unless you are sure that the information you've entered is correct for the patient.](#when-filling-out-reminder-dialogs-dont-click-the-finish-button-unless-you-are-sure-that-the-information-youve-entered-is-correct-for-the-patient)
    - [Tips to making sure you resolve your reminders quickly and completely:](#tips-to-making-sure-you-resolve-your-reminders-quickly-and-completely)
    - [FAQ](#faq)
    - [Follow-Up response from <span class="mark">REDACTED</span>:](#follow-up-response-from-span-classmarkredactedspan)
> User Manual

## April 2013

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs Office of Information and Technology (OIT)

> Product Development

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 33%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Page #</strong></th>
<th><strong>Description</strong></th>
<th><strong>Project Manager</strong></th>
<th><strong>Technical Writer</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>March 2013</td>
<td>Throughout</td>
<td>Updates to include most recent examples</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Oct 2012</td>
<td><a href="#_bookmark7"><u>7</u></a></td>
<td><p>Added note about changing parameter for # of days in future</p>
<p>for nightly background job report.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Sept 2012</td>
<td><a href="#_bookmark8"><u>8</u></a></td>
<td>Updates to Reminder dialogs</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Aug 2012</td>
<td><a href="#appendix-e-tips-tricks-and-faqs"><u>86</u></a></td>
<td>Added Hints, Tips, and FAQs</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 2012</td>
<td><a href="#Patient_Record_Flag_Category_I_HIGH_RISK"><u>59</u></a></td>
<td>Added info about PRF Transmission Menu</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>July 2012</td>
<td><a href="#high-risk-mental-health-health-summary-components-and-types"><u>44</u></a></td>
<td>Added info about MHTC Needs Assignment Reminder Definition</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>May 2012</td>
<td><a href="#high-risk-mental-health-ad-hoc-scheduling-report-example"><u>41</u></a></td>
<td>Updated Scheduling No-Show and Ad Hoc reports</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>May 2012</td>
<td><a href="#_bookmark8"><u>8</u></a></td>
<td><p>Updated dialog screenshots (to</p>
<p>include other dialog changes) for Phase 2 of HRMH project</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>May 2012</td>
<td><a href="#high-risk-mental-health-health-summary-components-and-types"><u>44</u></a></td>
<td>Added Health Summary info re MHTC and PRF</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>May 2012</td>
<td><a href="#1._A_patient_with_a_high_risk_for_suicid"><u>4</u></a></td>
<td>Added PRF information for Phase 2 of HRMH project</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>January 2012</td>
<td><a href="#_bookmark8"><u>8</u></a> <u>- 16</u></td>
<td>Updated dialog screenshots</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>Dec 2011</td>
<td><u><a href="#_bookmark5">6</a>, <a href="#high-risk-mental-health-ad-hoc-scheduling-report-example">41</a></u></td>
<td><p>Edited Scheduling reports, per developer changes and product</p>
<p>support review.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>Sep-Nov 11</td>
<td><a href="#high-risk-mental-health-ad-hoc-scheduling-report-example"><u>41</u></a></td>
<td>Added revised Scheduling Reports</td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>June 2011</td>
<td>Throughout</td>
<td><p>Completely revised, to document High Risk Mental Health Patient</p>
<p>Reminder and Dialog project.</p></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> April 2013 High Risk Mental Health Patient – National Reminder & Flag ii

> User Manual

# <u>Table of Contents</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table of Figures

April 2013 Clinical Reminders V. 2.0 User Manual iii

Patch PXRM\*2.0\*24

Figure 8: High Risk MH No-Show Follow-up Dialog, with Other Outcome selected

.................................................................................... 21.

# <u>Introduction</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The High Risk Mental Health Patient – National Reminder & Flag project is being released in two main phases; the first phase was released in March 2012. This manual describes functionality available in both phases.

> Phase 1 of this project provided the following:

1.  Two new Scheduling reports that identify no-show “high risk for suicide” patients that missed their MH appointments,
2.  A new national reminder and reminder dialog that will be used by providers to document results of following up with a high risk for suicide patient that missed a MH appointment, and
3.  A new health summary type with MH-specific supporting information.

> Phase 2 of this project provides the following:

1.  Registration - Patient Record Flag enhancements will support distribution of a national Category 1 HIGH RISK FOR SUICIDE PRF and tools for SPCs to automatically update patients based on the local High Risk for Suicide PRF. Scheduling, Clinical Reminders, TIU, and Health Summary enhancements will access and display national HIGH RISK FOR SUICIDE PRF patient data.
2.  The PCMM Mental Health Treatment Coordinator (MHTC) will be added to Scheduling reports, Health Summary objects, and Reminder Dialogs.
3.  An updated reminder definition, (VA-MH HIGH RISK NO-SHOW FOLLOW- UP), a new reminder definition, VA-MH HIGH RISK NO-SHOW RPT ONLY. A new computed finding (VA-PCMM MHTC), a new dialog that will display the Mental Health Treatment Coordinator (MHTC) and a new reporting

> reminder, “VA- MHTC NEEDS ASSIGNMENT,” that uses the new VA- PCMM MHTC computed finding.

4.  The MH HIGH RISK NO-SHOW FOLLOW-UP reminder dialog will include the new Mental Health Suicide Behavior Report (SBR) Instrument.

> There will also be two smaller follow-up phases known as Increments 6 and 7, which will include the following:

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/002.png)Scheduling Tool

> Reminders Due Reports enhancements for MHTCs Patient List enhancements

> Extract Reports with patient details

### Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following manuals are available from the VistA Documentation Library (VDL) [<u>http://www.va.gov/vdl</u>](http://www.va.gov/vdl):

### Clinical Reminders PXRM\*2\*24 Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Manual                   | File name    |
|------------------------------|------------------|
| Installation and Setup Guide | PXRM_2_24_IG.PDF |
| Release Notes                | PXRM_2_24_RN.PDF |
| User Manual                  | PXRM_2_UM.PDF    |
| Manager’s Manual             | PXRM_2_MM.PDF    |

> Health Summary GMTS\*2.7\*104 Documentation

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Manual</strong></th>
<th><blockquote>
<p><strong>File name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>User Manual</td>
<td><blockquote>
<p>HSUM_2_7 UM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Technical Manual</td>
<td><blockquote>
<p>HSUM_2_7 TM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TIU\*1\*265 Documentation

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Manual</strong></th>
<th><blockquote>
<p><strong>File name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Coordinator &amp; User Manual</td>
<td><blockquote>
<p>TIUUM.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Technical Manual</td>
<td><blockquote>
<p>TIUTM.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Scheduling SD\*5.3\*588 and Registration DG\*5.3\*849 Documentation

<table>
<colgroup>
<col style="width: 63%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Manual</strong></p>
</blockquote></th>
<th><strong>File name</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PIMS Technical Manual</p>
</blockquote></td>
<td>PIMSTM.PDF</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Scheduling User Manual – Outputs Menu</p>
</blockquote></td>
<td>PIMsSchOutput.pdf</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Scheduling User Manual - Menus, Intro &amp; Orientation</p>
</blockquote></td>
<td>PIMsSchIntro.pdf</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Patient Record Flag User Manual</p>
</blockquote></td>
<td>PatRecFlagUM.pdf</td>
</tr>
</tbody>
</table>

> CPRS OR\*2.0\*348 Documentation

| Manual                         | File Name |
|------------------------------------|---------------|
| CPRS User Guide: GUI Version       | CPRSGUIUM.PDF |
| CPRS Technical Manual: GUI Version | CPRSGUITM.PDF |
| CPRS Technical Manual              | CPRSLMTM.PDF  |

> Web Sites

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 32%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>SITE</strong></th>
<th><blockquote>
<p><strong>URL</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>National Clinical</p>
<p>Reminders site</p></td>
<td><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></td>
<td>Contains manuals, presentations, and information about Clinical Reminders</td>
</tr>
<tr class="even">
<td><p>National Clinical</p>
<p>Reminders Committee</p></td>
<td><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncr</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>cpublic/default.aspx</u></a></td>
<td>This group directs the development of new and revised national reminders</td>
</tr>
<tr class="odd">
<td>VistA Document Library</td>
<td><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></td>
<td><p>Contains manuals for Clinical</p>
<p>Reminders and related applications.</p></td>
</tr>
</tbody>
</table>

# <u>Background</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> High Risk Mental Health Patient Reminder and Flag

> This project addresses the New Service Request (NSR) \<\< NSR20070589 High Risk Mental Health Patient – National Reminder and Flag \>\>. The NSR was submitted by <span class="mark">REDACTED</span>, PCS, Mental Health Services and <span class="mark">REDACTED</span>, Associate Director for Education MIRECC. This project is included in the Improve Veteran Mental Health (IVMH) initiative.

> This request was submitted in support of recommendations from the Comprehensive VHA Mental Health Strategic Plan and VHA Handbook 1160.01, Uniform Mental Health Services in VA Medical Centers and Clinics, to improve continuity of care for Veterans receiving mental health services.

> Major objectives of this request include:

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/003.png) Ability to print a detailed report by date range that displays the names and other information for the high risk patients who have missed clinic appointments due to no- show, sortable by facility, clinic, patient, and date. This report is an enhancement to the Scheduling application.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/004.png) Ability to document results of the MH professional or Suicide Prevention Coordinators (SPCs) response to follow-up on the no-show MH appointment. This ability requires a MH clinician-oriented reminder definition that remains due until the MH clinician responds, using a new reminder dialog that helps them document the results of their follow-up with the patient.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/005.png) Ability to track and report on results of clinician responses to no-show appointments; for example:

1.  Contacted Patient
2.  Called for Welfare Check
3.  Suicide attempt or Suicide completed

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/006.png) Ability for MH professionals to document patients with a national (Category I) HIGH RISK FOR SUICIDE Patient Record Flag, instead of the local (Category II) High Risk for Suicide Patient Record Flag.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/007.png) Ability for the SPCs to automatically create the new national HIGH RISK FOR SUICIDE Patient Record Flag for a patient, based on the patient’s active local High Risk for Suicide Patient Record Flag.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/008.png) Ability for the CPRS Coordinator to select the Mental Health Treatment Coordinator as a default notification recipient for a particular type of notification.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/009.png) New mental health template called Suicide Behavior Report (SBR). This template is a new mental health instrument in the MH TESTS & SURVEYS file (#601.71) and was distributed nationally as an enhancement to the Mental Health Assistant 3.0 Package in 2012. This instrument will be used by MH professionals to document the High Risk for Suicide patient’s behavior. The instrument can be accessed from the High Risk MH No- Show Reminder or the Mental Health GUI application.

# High Risk MH Patient Process Flow Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is a typical sequence of steps related to working with high risk Mental Health (MH) patients and this project:

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/010.png)

> <span id="_bookmark3" class="anchor"></span>Figure 1: Example - Patient Record Flag Display on CPRS Cover sheet

1.  <span id="1._A_patient_with_a_high_risk_for_suicid" class="anchor"></span>A patient with a high risk for suicide PRF misses a Mental Health appointment.
2.  An automatic Scheduling nightly report is run that lists patients who have a MH clinic appointment with “NO-SHOW,” “NO-SHOW AUTO-REBOOK, “ or “No Action Taken” status.
3.  The Nightly report is sent in a MailMan message to recipients of the “SD MH NO SHOW NOTIFICATION” Mail Group. Recipients should be Suicide Prevention Coordinators (SPCs) and other MH professionals. (NOTE: Sites may vary in who they assign to follow up on patients in the Scheduling Message.)
4.  SPC/MH professionals’ potential actions:

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/011.png) Verify No Action Taken is actually a No-Show

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/012.png) If a scheduled appointment was kept, but just not documented, then no follow- up is necessary.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/013.png) If patient kept another MH appointment on the same day as the missed appointment, then no follow-up is necessary.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/014.png) Attempt to contact patient (minimum of three times over the next 72 hours) ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/015.png) Review Safety Plan on file before calling other contacts.

5.  The SPC/MH professional will document results of following up with the patient in the High Risk MH No-Show Follow-up Reminder dialog.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/016.png) See the section called Documenting Results of Follow-up in a Reminder Dialog for examples of items to document.

6.  <span id="_bookmark5" class="anchor"></span>Documented results are stored in the patient’s progress note and health factors are stored in PCE.
7.  SPC/MH professional can run the Ad Hoc scheduling reports and view the Results: caption to verify the No-Show appointments have been followed up on.
8.  A new reminder called VA-MHTC NEEDS ASSIGNMENT is available that can be used from CPRS to evaluate and display on the Cover Sheet’s Reminders Due section when the patient meets criteria for an MHTC assignment. In order to be an MHTC candidate, the patient must have had three completed MH appointments within the past year, and not have an MHTC assigned to the patient.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/017.png) The reminder definition uses the new VA-PCMM MHTC computed finding. ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/018.png) There is no reminder dialog related to this reminder.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/019.png) The reminder definition uses the new Reminder Term VA-MH APPTS FOR MHTC ASSIGNMENT, which uses a new Reminder Location List called VA-MHTC APPT STOP CODES LL in the Computed Finding VA- Appointments for a Patient.

### ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/020.png) The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/021.png) This reminder can also be used from Reminder Reporting options/Reminders Due Report. Reminder CACs can create a Reminders Due Report (User) template for an SPC user to get the list of patients who are scheduled for a MH appointment next week and are candidates for MHTC.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/022.png) MHTCs, SPCs, or other MH Professionals should ask their Reminders Manager or Reminders CAC to work with them to set up the Reminders Due report criteria in a template. Set up the template based on report criteria for SPC users. The report criteria should specify facility (or facilities), stop codes (e.g., 502) or hospital locations (selected Mental Health locations), future appointments or completed visits, and the VA- MHTC NEEDS ASSIGNMENT reminder.

# <u>High Risk Mental Health Scheduling Reports</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### New or Revised Scheduling Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The SD MH NO SHOW NIGHTLY BGJ and SD MH NO SHOW AD HOC REPORT

> have had some minor display enhancements to ensure the complete clinic name is visible (no truncating).

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/023.png)The SD MH NO SHOW AD HOC REPORT has been modified to include the following: PCMM Mental Health Treatment Coordinator (MHTC)

> Results of follow-up documentation related to a No-Show appointment

> The new SD MH PROACTIVE AD HOC REPORT AND SD MH PROACTIVE BGH

> REPORT options are now available for SPCs/MH professionals to see the list of patients with appointments at the beginning of each day in case proactive follow-up is needed with the patient to encourage the patient to attend their appointment.

### Assign Menu Options to MH staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IRM staff or Clinical Application Coordinators must assign the following report options to the primary or secondary menu options of your Suicide Prevention Coordinators, Mental Health Treatment Coordinator, and other Mental Health Professionals who will be tracking missed appointments for high risk for suicide patients:

| 1   | SD  | MH NO SHOW AD HOC REPORT High Risk MH No-Show Adhoc Report     |
|-----|-----|----------------------------------------------------------------|
| 2   | SD  | MH NO SHOW NIGHTLY BGJ High Risk MH No-Show Nightly Report     |
| 3   | SD  | MH PROACTIVE AD HOC REPORT High Risk MH Proactive Adhoc Report |
| 4   | SD  | MH PROACTIVE BGJ REPORT High Risk MH Proactive Nightly Report  |

> Note: The Nightly BGJ options should not be scheduled to run nightly. These reports create the same reports that the Scheduling Nightly Background job creates automatically. The Scheduling Nightly Background job runs on all VistA systems scheduled to start after midnight. The Scheduling patch modifies the Scheduling Nightly Background job to run the two Nightly BGJ jobs. The options are provided in case the SPC or MH professional wants to rerun the report after all No Action Taken appointments for the previous day have been processed.

> The [<u>Ad Hoc report</u>](#high-risk-mental-health-ad-hoc-scheduling-report-example) is described later in this manual.

### No Show Nightly Background Job

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When a patient with a high risk for suicide Patient Record Flag misses a Mental Health clinic appointment due to a no-show, an automatic nightly report is run that lists patients

> who have a MH clinic appointment with “NO-SHOW”, “NO-SHOW AUTO-REBOOK

> ,“ or “No Action Taken” status.

> The Nightly report is sent in a MailMan message to recipients of the “SD MH NO SHOW NOTIFICATION” Mail Group. Recipients should be Suicide Prevention Coordinators (SPC) and other MH professionals. Sites may vary on who should follow up on patients in the Scheduling Message.

> An option has also been created to manually run the no show background job if there was an error in running the report. It is called SD MH NO SHOW NIGHTLY BGJ (High Risk MH No-Show Nightly Report). See the appendix for an example of this report.

> The Background job lists the patients who had a status of “NO-SHOW,” “NO-SHOW AUTO-REBOOK” or “No Action Taken” for the day before, and who have a patient record flag “High Risk for Mental Health.” It will list patients for all mental health clinics/stop codes that are defined in the Remote location list ‘VA-MH NO SHOW APPT CLINICS LL’. The VA-MH NO SHOW APPT CLINICS LL location list includes clinic stop codes for MH clinics that are scheduled for face-to-face appointments.

> <span id="_bookmark7" class="anchor"></span>This report will list future scheduled appointments for 30 days in the future, unless sites change this time period, using a new parameter. See the Installation and Setup Guide for directions on using this parameter.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is how the nightly report will display to the screen when reading MailMan. The beginning of the message summarizes which division and clinics had a No-Show or No Action Taken.

> Note: Statuses are abbreviated as: NS = No Show, NSA = No Show Auto Rebook NAT = No Action Taken

### Example 1 – HRMH NO SHOW Nightly Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 27%" />
<col style="width: 23%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>Division/CLinic</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>Unique</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>NS</td>
<td>NSA</td>
<td>NAT</td>
<td>Patients</td>
</tr>
<tr class="even">
<td>ISC-SLC-A4/Mental</td>
<td>Health</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example 2 – Proactive Nightly Report

# Documenting Results of Follow-up in a Reminder Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### High Risk MH No Show Follow-up Reminder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### When will the reminder be applicable to the patient?

- The patient’s Category I or Category II High Risk for Suicide Patient Record Flag is active any time on the day of a missed MH appointment.
- The patient had a No-Show or No-Show Auto-Rebook appointment status.
- The No Action Taken status does not trigger this reminder.

#### What will resolve/not resolve the reminder?

- Resolved by an appointment that the patient kept on the same day or within 72 hours after the no-show appointment.
- Not Resolved by documenting the unsuccessful attempts to contact the patient, but will be resolved if a follow-up plan is documented.
- Resolved by documenting:
  - Patient was contacted
  - Patient received urgent or emergent care
  - Other outcome
  - Suicide attempt or completed

> NOTE: If the there are several No-show appointments for a given day, responses to resolve any of the no-show appointments on that day will resolve all of the no-show follow-ups for that day.

### Steps to process reminder:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> On the following pages are dialog screens for entering follow-up information about your patient’s missed appointment.

1.  Open CPRS and select a patient with an active High Risk for Suicide PRF; the pop-up for the patient’s active Category I and II patient record flags will appear here. Close this pop- up.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/024.png)

> Figure 2: Patient Record Flag Example

2.  If the High Risk MH No Show Follow-up reminder is due, it will appear on the CPRS Coversheet. You can get further information at this point by clicking or right-clicking on the reminder.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/025.png)

> Figure 3: High Risk MH No-Show Follow-up Reminder on CPRS Coversheet

> Clicking on the reminder will open a Reminder Resolution box for the High Risk MH No- Show Follow-up reminder, indicating what MH appointment caused the reminder to be due.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/026.png)

> Figure 4: Reminder Resolution box for High Risk MH No-Show Follow-up reminder

> 4. Start a new progress note. Select the CPRS Notes tab, select New Note, then in the Location for Current Location pop-up– either use a Telephone location if you were able to talk to the patient or use the Appointment only if the display shows the No-show status (so the encounter will not be billed).

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/027.png)

> Figure 5: Location for Current Activities pop-up

> Then select the Progress Note Title in the Progress Note Properties pop-up. This opens a new progress note and displays the reminders drawer.

> Note: The Progress Note title PATIENT RECORD FLAG CATEGORY I – HIGH RISK FOR SUICIDE is only used when documenting information about the PRF flag assignment – not a missed appointment.

3.  Open the reminders drawer. When you click on the reminders drawer, you see several folders containing reminders for this patient. Possible folders include Due, Applicable, Not Applicable, All Evaluated, and Other Categories.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/028.png)

> Figure 6: Reminders Drawer in CPRS Notes

4.  Select the High Risk MH No Show Follow-up reminder. Open a folder (if necessary) and click on this reminder to begin processing it. At this point, you will be asked to provide the primary encounter provider, so that any PCE data entered from reminder dialog processing can be saved.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/029.png)

> <span id="_bookmark11" class="anchor"></span>Figure 7- CPRS opened to Notes screen, with open Reminders drawer showing

### Opening screen

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When you click on checkboxes, more choices or boxes for entering info are opened up.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/030.png)

> <span id="_bookmark12" class="anchor"></span>Figure 8: High Risk MH No-Show Follow-up Dialog Opening Screen

### Additional Supporting Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The first highlighted box can be clicked to see Additional Supporting information including Contact information, future scheduled MH appointments, High Risk for Suicide PRF histories, and MH Treatment Provider. Use the Scroll bar to see all information if necessary. This is the same information as the VA-HIGH RISK PATIENT Health Summary selectable from the CPRS Reports tab.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/031.png)

> <span id="_bookmark13" class="anchor"></span>Figure 9: High Risk MH No-Show Follow-up Additional Information Screen

### Patient Contact made and plan put in place for ongoing care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/032.png)

> <span id="_bookmark14" class="anchor"></span>Figure 10: High Risk MH No-Show Follow-up Dialog, with Patient Contact selected

### Patient sought urgent or emergent health care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/033.png)

> <span id="_bookmark15" class="anchor"></span>Figure 11: High Risk MH No-Show Follow-up Dialog, with Patient sought urgent care selected

### Three unsuccessful attempts made to contact patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Check the kinds of unsuccessful contact attempts that were made. The only selection item that resolves this reminder is “Developed the following plan”. The other selection items require more follow-up.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/034.png)

> <span id="_bookmark16" class="anchor"></span>Figure 12: High Risk MH No-Show Follow-up Dialog, with three unsuccessful attempts selected

### Other Outcome

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter text about what the other outcome is in the Comment box. Selecting Other Outcome does resolve the reminder.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/035.png)

> Figure 13: High Risk MH No-Show Follow-up Dialog, with Other Outcome selected

### Suicide Attempted or Completed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter text about the suicide attempted or suicide completed in the Comment box.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/036.png)

> <span id="_bookmark17" class="anchor"></span>Figure 14: High Risk MH No-Show Follow-up Dialog, with Suicide attempted or completed selected

> Note: If Patient attempted suicide or Patient completed suicide is checked off, and the Finish button is clicked, then the Health Factors for MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED update PCE, which also triggers a notification to be sent to the Mental Health Treatment Coordinator and other Provider recipients set up for the SUICIDE ATTEMPTED/COMPLETED notification type. More information is in the

### Suicide Behavior Report (SBR) Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use of the Suicide Behavior Report is optional from the Reminder Dialog. If a report needs to be entered, the Mental Health GUI can be used to enter the SBR.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/037.png)

> <span id="_bookmark18" class="anchor"></span>Figure 15: High Risk MH No-Show Follow-up Dialog, with Suicide Behavior Report selected

> The following will display when the SBR button is selected. If it’s your first time entering an SBR, an information box appears.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/038.png)

> <span id="_bookmark19" class="anchor"></span>Figure 16: High Risk MH No-Show Follow-up Dialog, with Perform SBR button selected

> There are approximately 19 questions which must be completed before you can Finish the dialog. The answers won’t load into the Progress Note until all answers have been entered and the Done button is clicked.

> If you leave the patient SBR without completing each answer, the following message appears:

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/039.png)

> <span id="_bookmark20" class="anchor"></span>Figure 17: Leaving the dialog without answering all questions

> When you answer No, you will be returned to the SBR. If you answer Yes, the SBR closes with the answers you entered and returns you to the reminder dialog. But, you can’t exit the reminder dialog without completing the remaining questions. The following pop-up will appear.

> If you try to Finish the Reminder Dialog without completing the SBR questions, the following pop-up will display.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/040.png)

> You may prefer using the Mental Health GUI to complete the SBR; or plan on completing all SBR questions before you finish the reminder dialog.

> If the SBR is completed, the SBR questions and answers display in the progress note text.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/041.png)

> <span id="_bookmark21" class="anchor"></span>Figure 18: High Risk MH No-Show Follow-up Dialog, showing Progress Note text for SBR

### Click Finish to see the Progress Note

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/042.png)Each item you selected in the reminder dialog will cause text to be added to the Progress Note and related Health Factors associated with the text will display. This is an example of the Progress Note text where Suicide Attempted is the only item documented.

> Progress Note with example of text from a completed SBR

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/043.png)

> <span id="_bookmark22" class="anchor"></span>Figure 19: Results of opening the SBR button as it appears in the Progress Note

# <u>VA-MHTC Needs Assignment Reminder Definition</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This reminder determines whether a patient has been assigned a Mental Health Treatment Coordinator (MHTC) when the patient has kept three or more Mental Health appointments in the past year, where the appointment is checked out and a completed encounter has been documented.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/044.png) The reminder definition uses the new VA-PCMM MHTC computed finding to find the Mental Health Treatment Coordinator assigned to the patient.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/045.png) There is no reminder dialog related to this reminder.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/046.png) This reminder can be used from CPRS to show as due on the CPRS GUI Cover Sheet.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/047.png) This reminder uses the new Reminder Term VA-MH APPTS FOR MHTC ASSIGNMENT, which uses a new Reminder Location List called VA-MHTC APPT STOP CODES LL in the Computed Finding VA-Appointments for a Patient. This location list is used to find MH appointments kept by the patient. This is not based on documented PCE Visits to stop codes in the Reminder Location List.

### ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/048.png) The new Reminder Location List is consistent with the national list of MH Encounter Stop Codes defined for sites by the Office of Mental Health Services.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/049.png) This reminder can also be used from Reminder Reporting options/Reminders Due Report. Reminder CACs can create a Reminders Due Report (User) template for an SPC user to get the list of patients who are scheduled for a MH appointment next week and are candidates for MHTC.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/050.png) MHTC, SPC, or other MH Professional should ask their Reminders Manager or Reminders CAC to work with them to set up the Reminders Due report criteria in a template. Set up the template based on report criteria for SPC users. The report criteria should specify facility (or facilities), stop codes (e.g.,

> 502\) or hospital locations (selected Mental Health locations), future appointments or completed visits, and the VA-MHTC NEEDS ASSIGNMENT reminder.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/051.png) Assign the user the Reminder Due Report (User) option so the SPC can run the Reminder Due report for selected facility and locations or stop codes, as desired (future or past appointments).

> When the reminder status is DUE NOW, the reminder will display on the Cover Sheet if the Needs MHTC Assignment reminder is in your default list of Reminders. The list is set up using selecting Tools menu from the CPRS GUI header bar, selecting Options, clicking on the Clinical Reminders button, and then selecting the Needs MHTC Assignment from the Editing Cover Sheet Reminders for User section of the Clinical Reminders and Reminder Categories Displayed on Cover Sheet pop-up.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/052.png)

> Figure 20: CPRS option to set up Reminders that will appear on the Coversheet

> The reminder will only display on the Cover Sheet if the reminder is DUE. Clicking on the due reminder on the Cover Sheet will open the Clinical Maintenance box with the criteria that makes the reminder due.

> To see the results of the reminder when the reminder is NOT due, the alarm clock on the CPRS header can be clicked to open the Available Reminders box, select the + next to the All Evaluated Category, and scroll down to the Needs MHTC Assignment.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/053.png)

> Figure 21: Available Reminders box

> Right click on the reminder and select Clinical Maintenance to see the information found when evaluating the reminder. The following are examples of different scenarios.

> Examples of Clinical Maintenance text displayed, depending on patient information:

1)  Clinical Maintenance Output when no kept MH appointments are found:

> This N/A status reminder will not display on the Cover Sheet because the reminder is NOT due. The Reminders drawer for All Evaluated reminders can be used to see the clinical maintenance in this scenario.

2)  Clinical Maintenance Output when \<3 MH appointments and no MHTC assigned:

> --STATUS-- --DUE DATE-- --LAST DONE--

> Needs MHTC Assignment N/A Frequency: Due every 99Y - Once for all ages.

> Reminder triggered when no active MHTC is assigned for a patient with 3 MH appointments in the past year.

> Cohort:

> Patient does not have three or more MH appointments within the past year.

> Information:

> Reminder Term: VA-MH APPTS FOR MHTC ASSIGNMENT

> Computed Finding: VA-Appointments for a Patient 11/04/2011@08:45 value - TEST

> APPOINTMENT DATE/TIME: 11/04/2011@08:45 CLINIC: TEST

> APPOINTMENT STATUS: SCHEDULED/KEPT OUTPATIENT ENCOUNTER IEN: 3039

> 11/11/2011@08:45 value - TEST APPOINTMENT DATE/TIME: 11/11/2011@08:45 CLINIC: TEST

> APPOINTMENT STATUS: SCHEDULED/KEPT OUTPATIENT ENCOUNTER IEN: 3041

> Reminder Term: VA-MH HIGH RISK FOR SUICIDE PRF

> Computed Finding: VA-Patient Record Flag Information 01/31/2012@11:08:45 value - NEW ASSIGNMENT;

> Flag - HIGH RISK FOR SUICIDE(I (NATIONAL)).

> Assigned Jan 31, 2012@11:08:45 by REDINGTON,PATRICK. New record flag assignment.

> 12/21/2010@15:36:02 value - NEW ASSIGNMENT; Flag - HIGH RISK FOR SUICIDE(II (LOCAL)).

> Assigned Dec 21, 2010@15:36:02 by TROST,DEBBIE. New record flag assignment.

> Patient has an active High Risk for Suicide Patient Record Flag.

> This N/A status reminder will not display on the Cover Sheet because the reminder is NOT due. The Reminders drawer for All Evaluated reminders can be used to see the clinical maintenance in this scenario.

3)  Clinical Maintenance Output when 3 kept MH appointments were found and no MHTC is assigned:

> --STATUS-- --DUE DATE-- --LAST DONE--

> Needs MHTC Assignment DUE NOW DUE NOW unknown Frequency: Due every 99Y - Once for all ages.

> Reminder triggered when no active MHTC is assigned for a patient with 3 MH appointments in the past year.

> Cohort:

> Patient had three or more MH appointments kept within the past year.

> Information:

> Reminder Term: VA-MH APPTS FOR MHTC ASSIGNMENT

> Computed Finding: VA-Appointments for a Patient 05/14/2012@08:00 value - Mental Health

> APPOINTMENT DATE/TIME: 05/14/2012@08:00

> CLINIC: Mental Health

> APPOINTMENT STATUS: SCHEDULED/KEPT CHECK-OUT DATE/TIME: 05/22/2012@02:42 OUTPATIENT ENCOUNTER IEN: 3050

> 05/17/2012@08:00 value - Mental Health APPOINTMENT DATE/TIME: 05/17/2012@08:00

> CLINIC: Mental Health

> APPOINTMENT STATUS: SCHEDULED/KEPT CHECK-OUT DATE/TIME: 05/22/2012@03:04 OUTPATIENT ENCOUNTER IEN: 3051

> 05/17/2012@10:00 value - Mental Health APPOINTMENT DATE/TIME: 05/17/2012@10:00

> CLINIC: Mental Health

> APPOINTMENT STATUS: SCHEDULED/KEPT CHECK-OUT DATE/TIME: 05/22/2012@03:11 OUTPATIENT ENCOUNTER IEN: 3052

4)  Clinical Maintenance Output when 3 kept MH appointments are found and MHTC is defined. Done date is the date the reminder is run because the MHTC is active as of the reminder run date:

> Patient has an MHTC currently assigned.

> Information:

> Reminder Term: VA-MH APPTS FOR MHTC ASSIGNMENT

> Computed Finding: VA-Appointments for a Patient 11/04/2011@08:45 value - TEST

> APPOINTMENT DATE/TIME: 11/04/2011@08:45 CLINIC: TEST

> APPOINTMENT STATUS: SCHEDULED/KEPT OUTPATIENT ENCOUNTER IEN: 3039

> 11/08/2011@08:00 value - Mental Health APPOINTMENT DATE/TIME: 11/08/2011@08:00

> CLINIC: Mental Health

> APPOINTMENT STATUS: SCHEDULED/KEPT CHECK-OUT DATE/TIME: 11/08/2011@08:50 OUTPATIENT ENCOUNTER IEN: 3040

> 11/11/2011@08:45 value - TEST APPOINTMENT DATE/TIME: 11/11/2011@08:45 CLINIC: TEST

> APPOINTMENT STATUS: SCHEDULED/KEPT OUTPATIENT ENCOUNTER IEN: 3041

> Reminder Term: VA-MH HIGH RISK FOR SUICIDE PRF

> Computed Finding: VA-Patient Record Flag Information 01/31/2012@11:08:45 value - NEW ASSIGNMENT;

> Flag - HIGH RISK FOR SUICIDE(I (NATIONAL)).

> Assigned Jan 31, 2012@11:08:45 by REDINGTON,PATRICK. New record flag assignment.

> 12/21/2010@15:36:02 value - NEW ASSIGNMENT; Flag - HIGH RISK FOR SUICIDE(II (LOCAL)).

> Assigned Dec 21, 2010@15:36:02 by TROST,DEBBIE. New record flag assignment.

> Patient has an active High Risk for Suicide Patient Record Flag.

### Example of running Reminder Due Report, without saving template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VA-MHTC Needs Assignment reminder can be used from Reminders Due Reports to evaluate patients with future appointments that have not been assigned an MHTC. The SPC should work with the Clinical Application Coordinator to set up a Reminders Due

> Template that best meets the SPC’s needs and make sure the SPC has access to the Reminders Due Report (User) \[PXRM REMINDERS DUE (USER)\]option. If the template is never saved, the SPC will not be able to use the Reminders Due Report (User) option to print out reports.

> LOCATION: Mental Health WHPROVIDER,THIRTEEN

> Select another LOCATION:

> Select one of the following:

> P Previous Encounters

> F Future Appointments

> PREVIOUS ENCOUNTERS OR FUTURE APPOINTMENTS: P// f Future Appointments

> Enter APPOINTMENT BEGINNING DATE AND TIME: May 22, 2012// may 21, 2012 (MAY 21, 2012)

> This must be a future date. For detailed help type ??.

> Enter APPOINTMENT BEGINNING DATE AND TIME: May 22, 2012// (MAY 22, 2012) Enter APPOINTMENT ENDING DATE AND TIME: may 25,2012 (MAY 25, 2012)

> Enter EFFECTIVE DUE DATE: May 22, 2012// (MAY 22, 2012)

> Select one of the following: D Detailed

> S Summary

> TYPE OF REPORT: S// d Detailed

> Display All Future Appointments: N// y YES Display Appointment Location: N// y YES Sort by Next Appointment date: N// y YES Print full SSN: N// O

> Print locations with no patients? YES// n NO

> Print percentages with the report output? NO// y YES Select individual REMINDER: VA-MHTC??

> Select individual REMINDER: VA-MHTC NEEDS ASSIGNMENT NATIONAL

> Create a new report template: N// O Print delimited output only: N// O

> Include deceased patients on the list? N// O Include test patients on the list? N// YES Save due patients to a patient list: N// O DEVICE: HOME// ;;9999 HOME

> Building hospital locations list \|

> Elapsed time for building hospital locations list: 0 secs

> Calling the scheduling package to gather appointment data \| Elapsed time for call to the Scheduling Package: 0 secs

> The first page of output is the report criteria used to run the report. Note, once the SPC user has access to the Reminder Due Report (User) option, the criteria can be changed for any given run of the report by the SPC.

### Template Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow local guidelines for naming the reminders due report template for the SPC to use.

> Saving the entries to a template allows the SPC to run the report as needed from the Reminder Due Reports (User) option.

> Note: There are several pre-defined prompts followed by a subset of prompts that must be completed by the SPC to run the Reminder due report. The default prompts are based on the saved template.

> The following is a template example saved for an SPC to use for a VA facility:

> MH CWT/TWE FACE TO FACE 574

> MH VOCATIONAL ASSISTANCE-GRP 575 TELEPHONE/SPECIAL PSYCHIATRY 526 MENTAL HEALTH CLINIC-GROUP 550 MENTAL HEALTH TELEPHONE PRI 527 TELEPHONE/PTSD 542

> TELEPHONE/ALCOHOL DEPENDENCE 543

> TELEPHONE/DRUG DEPENDENCE 544 PHONE SUBSTNCE USE DSORDR 545

> Enter RETURN to continue or '^' to exit:

> DAY TREATMENT-INDIVIDUAL 505 WOMEN'S STRESS DISORDER TEAMS 525 TELEPHONE HCMI 528

> HCHV/HCMI INDIV 529

> TELEPHONE/HUD-VASH 530

> IPCC COMM CLN/DAY PROGRAM VST 551 MH MED PRI CARE IND 2ND TO 323 531 TELEPHONE/MHICM 546

> MH PRIMARY CARE - GROUP 563 PSYCHOGERIATRIC - INDIVIDUAL 576 PSYCHOGERIATRIC - GROUP 577 PSYCHOGERIATRIC DAY PROGRAM 578 DAY HOSPITAL-INDIVIDUAL 506

> TELEPHONE/PSYCHOGERIATRICS 579 PSYCHOSOCIAL REHAB - IND 532

> MH VOCATIONAL ASSISTANCE - IND 535 MHICM - INDIVIDUAL 552 TELEPHONE/MH VOC ASSISTANCE 536 TELEPHONE/PSYCHOSOCIAL REHAB 537 INTNSE SUB USE DSRDER GRP 547

> PCT-POST TRAUMATIC STRESS-GRP 561 PTSD DAY HOSPITAL 580

> PTSD DAY TREATMENT 581

> COMM OUTREACH HOMELESS VETS 590

> Enter RETURN to continue or '^' to exit:

> HUD/VASH GROUP 507

> MH TEAM CASE MANAGEMENT 564

> NON-ACTIVE DUTY SEXUAL TRAUMA 589 DAY TREATMENT-GROUP 553

> PSYCHOLOGICAL TESTING 538

> MH INTERVNTION BIOMED CARE IND 533 MH INTERVENTION BIOMED GRP 565

> MH RISK-FACTOR-REDUCTION ED GR 566 MHICM - GROUP 567

> MH CWT/SE FACE TO FACE 568

> MH CWT/SE NON-F TO F (MAS NONC 569 MH CWT/TWE NON-F TO F (MAS NON 570 HCHV/HCMI GROUP 508

> PRRC INDIVIDUAL 582

> DAY HOSPITAL-GROUP 554

> PRRC GROUP 583

> PRRC TELEPHONE 584

> MH INTGRTD CARE IND 534 INCARCERATED VETERANS RE-ENTRY 591 RRTP OUTREACH SERVICES 593

> RRTP AFTERCARE - COMMUNITY 594 RRTP AFTERCARE GRP 595

# High Risk Mental Health Ad Hoc Scheduling Report Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assign this report option to the primary or secondary menu options of your Suicide Prevention Coordinators, Mental Health Treatment Coordinator, and other Mental Health Professionals who will be tracking missed appointments for high risk for suicide patients:

> NOTE: The AD HOC NO SHOW report is updated in Phase 2, as follows:

1.  MHTC information now displays the name of the MHTC and the name of the care team they are assigned to in parentheses
2.  The provider now displays directly underneath the NO Show Appointment information to keep everything connected

### Example of High Risk MH No-Show Adhoc Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\* High Risk Mental Health NO SHOW Adhoc Report \*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Select Beginning Date: 05/23/12// 05/14/12 (MAY 14, 2012)

> Select Ending Date: 05/23/12// (MAY 23, 2012) Select division: ALL//

> Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M// Select Number of days to List Future Appointments: 30//

> This output requires 80 column output

> Select Device: ;;9999 HOME

> ...HMMM, THIS MAY TAKE A FEW MOMENTS...

> HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 1

> MH CLINICS for Appointments 5/14/12-5/23/12 Run: 5/23/2012@08:26

> \*STATUS: NS = No Show NA = No Show Auto Rebook NAT = No Action Taken

> \# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* DIVISION/CLINIC/STOP: ISC-SLC-A4/Mental Health/188

1.  CRPATIENT,TWO C4444 5/14/2012@08:00 Mental Health

> \*NS WHPROVIDER,THIRTEEN

> Home: (801)556-6666

> Cell: (801)222-6666

> Next of Kin:

> NOK: PRIMARY NOK CRPATIENT,TWO

> Relation: FRIEND

> Phone: (801)556-6666 Phone: (801)556-6666

> Work Phone: (801)565-6565

> Emergency Contact:

> E-Cont.: PRIMARY NOK CRPATIENT,TWO

> Relation: FRIEND

> 203 Main st

> SALT LAKE CITY, UT 84107 Phone: (801)556-6666

> Work Phone: (801)565-6565

> MHTC: MHCLINICIAN, ONE (HRMH TEST TEAM)

> Future Scheduled Appointments: NO APPOINTMENTS SCHEDULED WITHIN 30 DAYS Results:

> Resolution: Last done 05/14/2012@12:00 Reminder Term: VA-MH NOSHOW PT EMERGENT CARE

> Health Factor: MH NOSHOW PT EMERGENT CARE 05/14/2012@12:00

> Reminder Term: VA-MH SUICIDE ATTEMPTED

> Health Factor: MH SUICIDE ATTEMPTED 05/14/2012@12:00

2.  CRPATIENT,TWO C4444 5/14/2012@12:00 Mental Health

> \*NS WHPROVIDER,THIRTEEN

> Home: (801)556-6666

> Cell: (801)222-6666

> Next of Kin:

> NOK: PRIMARY NOK CRPATIENT,TWO

> Relation: FRIEND

> Phone: (801)556-6666 Phone: (801)556-6666

> Work Phone: (801)565-6565

> Emergency Contact:

> E-Cont.: PRIMARY NOK CRPATIENT,TWO

> Relation: FRIEND

> 203 Main st

> SALT LAKE CITY, UT 84107 Phone: (801)556-6666

> Work Phone: (801)565-6565

> MHTC: MHCLINICIAN,ONE (HRMH TEST TEAM)

> Future Scheduled Appointments: NO APPOINTMENTS SCHEDULED WITHIN 30 DAYS Results:

> Resolution: Last done 05/14/2012@12:00 Reminder Term: VA-MH NOSHOW PT EMERGENT CARE

> Health Factor: MH NOSHOW PT EMERGENT CARE 05/14/2012@12:00

> Reminder Term: VA-MH SUICIDE ATTEMPTED

> Health Factor: MH SUICIDE ATTEMPTED 05/14/2012@12:00

3.  CRPATIENT,TWO C4444 5/18/2012@08:00 Mental Health

> \*NS WHPROVIDER,THIRTEEN

> Home: (801)556-6666

> Cell: (801)222-6666

> Next of Kin:

# High Risk Mental Health Health Summary <u>Components and Types</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Four new Health Summary Components are available to view Mental Health High Risk data:

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/054.png)MAS MAS Contacts

> MHFV MH Clinic Future Visits MHRF MH Suicide PRF Hx

> MH MH Treatment Coordinator

### Example: Health Summary with HRMH components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CPRS GUI is able to display multiple Category 1 Patient Record Flags:

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/055.png)

> <span id="_bookmark27" class="anchor"></span>Figure 22: Patient Record Flag window

> CPRS GUI Reports Tab, VA-MH HIGH RISK PATIENT Health Summary Display updated to include Cat 1 HIGH RISK FOR SUICIDE PRF, and MHTC info

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/056.png)

> <span id="_bookmark28" class="anchor"></span>Figure 23: VA-MH HIGH RISK PATIENT Health Summary Display with Cat 1 HIGH RISK FOR SUICIDE PRF, and MHTC info

> Reminder Resolution for High Risk MH No-Show Follow-up reminder; additional information display now includes CAT 1 PRF and MHTC

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/057.png)

> <span id="_bookmark29" class="anchor"></span>Figure 24: Reminder Resolution for High Risk MH No-Show Follow-up reminder

### New Health Summary Types distributed by the High Risk Mental Health Patient project:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The two HEALTH SUMMARY TYPEs, VA-HIGH RISK PATIENT and REMOTE MH

> HIGH RISK PATIENT were originally released in GMTS\*2.7\*99. In order to view these HEALTH SUMMARY TYPES from within CPRS GUI, they must be added to the CPRS GUI Reports tab selection list. This can be set up from one of the following menu options.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/058.png) GMTS COORDINATOR

> CPRS Reports Tab 'Health Summary Types List' Menu Edit 'Health Summary Types List' Parameters

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/059.png) CPRS MANAGER MENU ORMGR CPRS Manager Menu

> PE CPRS Configuration (Clin Coord) ...

> GP GUI Parameters ...

> HS GUI Health Summary Types Allowable Health Summary Types may be set for the following:

2.  User USR \[choose from NEW PERSON\]
3.  Division DIV \[choose from INSTITUTION\]
4.  System SYS \[DVF.FO-SLC.MED.VA.GOV\]
5.  Service SRV \[choose from SERVICE/SECTION\]

> Add the new REMOTE MH HIGH RISK PATIENT - HEALTH SUMMARY TYPE to

> the appropriate list based on your local practice and procedures.

# <u>Order Entry (OR) MHTC Notification</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As part of the HRMHP project, MHTCs can now specify to be default provider recipients of certain pertinent notifications, such as for Admissions, Discharge, and Deceased Patient, to name a few. A new provider recipient, Primary Care Management Module (PCMM) Mental Health Treatment Coordinator (MHTC), has been added to the existing ORB PROVIDER RECIPIENTS parameter.

> A MHTC is defined as a liaison between the patient and the mental health system at a VA site and is the key coordinator for behavioral health services care. There is only one MHTC per patient.

> For more information about the MHTC's responsibilities, see VHA Handbook 1160.1, "Uniform Mental Health Services in VA Medical Centers for Clinics," pp 3-4. Note: In the handbook, the MHTC is called the Principal Mental Health Provider.

> A new notification is also being released with this project: SUICIDE ATTEMPTED/ COMPLETED. This informational notification is triggered by Clinical Reminders when a MH SUICIDE ATTEMPTED or MH SUICIDE COMPLETED health factor has been documented in PCE. It is exported with package parameter values set as follows:

> . ORB ARCHIVE PERIOD - 30

> . ORB DELETE MECHANISM - Individual Recipient

> . ORB FORWARD BACKUP REVIEWER - No

> . ORB FORWARD SUPERVISOR - No

> . ORB FORWARD SURROGATES - No

> . ORB PROCESSING FLAG - Disabled

> . ORB PROVIDER RECIPIENTS - MHTC and PCMM Team (CM)

> . ORB URGENCY - High

### \*\*\*Important Note\*\*\*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Notifications are processed by IEN (internal entry number) from the OE/RR NOTIFICATIONS File \#100.9. Any site-defined notifications run the risk of being over- written by new notifications that are nationally released, especially those within the number range 1-9999, which is reserved for national release. If you have locally defined notifications, you may need to renumber them before this patch will install. Specifically, IEN \#77 is being added.

> IRM will need to enable this at the System level.

1.  Assign SPC users as recipients to this notification. Note: MHTC should already be set up as a default recipient type for Suicide Attempted/Completed.
2.  Add ‘C’ (MHTC) to the default recipient list for other notification types (Admission, Discharge, …) as deemed necessary.
3.  Other Notification Types enabled on your system that are identified as appropriate to notify the patient’s assigned MHTC. (e.g., Admission, Discharge, ….) will need to be manually defined as needed.

> NOTE: An ORB PROVIDER RECIPIENT parameter value of “CM” is exported with the Suicide behavior notification. Therefore, the suicide behavior notification will be sent to the MHTC and PCMM Mental Health team if any are set up and configured at the site.

> Directions on how to set those up should be contained in a setup manual created by the sister project, Principal Mental Health Provider. See the Primary Care Management Module (PCMM) – Mental Health Treatment Coordinator (MHTC) User Manual (pcmmmhtcug.pdf) for more information.

> Here is the set of codes indicating default provider recipients of a notification by their title or relationship to the patient. Notifications can be set up with any or all of the following codes:

> Once all the set-up is done, you can verify this via the following menu:

14. Determine Recipients for a Notification
15. Display Patient Alerts and Alert Recipients
16. Enable or Disable Notification System
17. Display the Notifications a User Can Receive

> Select Notification Mgmt Menu Option: 14 Determine Recipients for a Notification

> PATIENT (req'd): MHPATIENT,ONE 5-5-55 555121255

> YES SC VETERAN

> Enrollment Priority: GROUP 1 Category: IN PROCESS End Date:

> NOTIFICATION (req'd): SUICIDE ATTEMPTED/COMPLETED

> Processing, please stand by... DEVICE: HOME// ;;9999 HOME

> DETERMINE NOTIFICATION RECIPIENTS REPORT

> Page: 1

> Processing notification: SUICIDE ATTEMPTED/COMPLETED for patient: MHPATIENT,ONE

> Default recipient users and teams: SBCUSER,ONE: ON because

> Default Recipient (USER) parameter set to Yes.

> SBCUSER,TWO: ON because

> Default Recipient (USER) parameter set to Yes.

> Recipients determined by Provider Recipient parameter: PCMM Team Position Assignments:

> PCMM Mental Health Treatment Coordinator:

> MHTCUSER,ONE: ON because

> User MHTCUSER,ONE is Enabled.

> \- End of Report -

> The following is an example of the notification that will be sent to recipients of the SUICIDE ATTEMPTED/COMPLETED notification. This example is based on a CPRS user selecting Suicide Attempted to follow-up on the High Risk MH No-Show Follow-up reminder dialog. The notification is displayed on the Patient Selection box.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/060.png)

> Figure 25: Example of notifications sent to designated recipients of SUICIDE ATTEMPTED/COMPLETED

# Scheduling Report Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following Scheduling reports are available when the HRMHP project is installed at your site.

> NOTE: None of the MH NO SHOW reports are exported onto output menus. Site ADPACS will need to attach these reports to their menus. Assign these report options to the primary or secondary menu options of your Suicide Prevention Coordinators, Mental Health Treatment Coordinator, and other Mental Health Professionals who will be tracking missed appointments for high risk for suicide patients.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>OPTIONS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DESCRIPTION</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SD MH NO SHOW AD HOC REPORT</p>
</blockquote></td>
<td><blockquote>
<p>This Scheduling option provides a MH NO SHOW Report for use by Suicide Prevention Coordinators and other Mental Health professionals.</p>
<p>This report supports following up with High Risk for Suicide patients who missed a scheduled MH appointment. It displays all patients that no-showed for their scheduled appointment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SD MH NO SHOW NIGHTLY BGJ</p>
</blockquote></td>
<td><blockquote>
<p>This Scheduling option provides a MH NO SHOW Scheduling Report. This report supports actions relating to following up with High Risk for Suicide patients that missed their MH appointment.</p>
<p>This report is generated at the end of the Scheduling Nightly Background job, and will be sent in a Mailman message to members of the SD MH NO SHOW NOTIFICATION mail group. This report may also be run by calling the option No Show Nightly Background Job [SD MH NO SHOW NIGHTLY BGJ].</p>
<p>Future appointments will list on this report. The number of days’ worth of future appointments that will list is defaulted to 30 days in the future. A new parameter SD MH NO SHOW DAYS has been added to store the number of days for which future appointments will be listed. This parameter can be edited by the user by using the option [ XPAR EDIT PARAMETER] Edit Parameter Values.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HIGH RISK MH PROACTIVE NIGHTLY REPORT [SD MH PROACTIVE BGJ REPORT]</p>
</blockquote></td>
<td><blockquote>
<p>This report is a background job that will list the daily appointments for patients with a high risk For Suicide PRF.</p>
<p>This report will be kicked off by the Scheduling nightly background Job (SDAM BACKGROUND JOB) that should already be scheduled to run nightly on your system.</p>
<p>This report is sent in a mail message to the members of the SD MH NO SHOW NOTIFICATION mail group.</p>
<p>Future appointments will list on this report. The number of days’ worth of future appointments that will list is defaulted to 30 days in the future. A new parameter SD MH PROACTIVE</p>
</blockquote></td>
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
<th></th>
<th><blockquote>
<p>DAYS has been added to store the number of days to list future appointments for. This parameter can be edited by the user by using the option Edit Parameter Values.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HIGH RISK MH PROACTIVE ADHOC REPORT [SD MH PROACTIVE AD HOC REPORT]</p>
</blockquote></td>
<td><blockquote>
<p>This Adhoc report option, SD MH PROACTIVE AD HOC REPORT, generates a proactive report that can be run by the users. This report is more flexible and allows users to refine the report to their specifications.</p>
<p>This option generates the HIGH RISK MENTAL HEALTH PROACTIVE ADHOC REPORT BY CLINIC for Appointments Report that can be sorted by all clinics or by Mental Health clinics only. This report allows users to refine their report to their specifications.</p>
<p>This report display appointments for High Risk for Suicide patients that have appointments for today, by divisions for all patients with Patient Record Flag (PRF) High Risk for Suicide that have appointments in mental health clinics today, totals to show the number of unique patients by division, list patients alphabetically by division and by date/time of the appointment, and will also display national as well as local PRF activity.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HIGH RISK MH NO-SHOW ADHOC REPORT [SD MH NO SHOW AD HOC REPORT] AND HIGH RISK MH NO-SHOW NIGHTLY REPORT [SD MH NO SHOW NIGHTLY BGJ]</p>
</blockquote></td>
<td><blockquote>
<p>This patch contains format changes to the no show reports High Risk MH No-Show Adhoc Report [SD MH NO SHOW AD HOC REPORT] and High Risk MH No-Show Nightly Report [SD MH NO SHOW NIGHTLY BGJ], and the provider now displays directly underneath the No Show Appointment information to keep everything connected.</p>
<p>The Ad Hoc No Show report includes the Mental Health Treatment Coordinator (MHTC). The report displays the name of the MHTC and the name of the care team they are assigned to in parentheses.</p>
<p>The results of the no show patient contact are also included.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### High Risk Mental Health NO Show Nightly Report \[SD MH NO SHOW NIGHTLY BGJ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report is generated at the end of the Scheduling Nightly Background job, and is sent in a Mailman message to those persons added to the mail group SD MH NO SHOW NOTIFICATION. All persons in this mail group will receive the High Risk Mental Health NO SHOW report that is generated from the scheduling nightly background job. An option to manually run the no show background job if there was an error in running the report, has also been created called SD MH NO SHOW NIGHTLY BGJ (High Risk MH No-Show Nightly Report).

> The Background job will list the patients who had a status of “NO SHOW,” “NO SHOW WITH AUTO-REBOOK,” and “No Action Taken” for the day before and who have a the patient record flag “High Risk for Mental Health.” It will list patients for all mental health clinics/stop codes that are defined in the Remote location list “VA-MH NO

> SHOW APPT CLINICS LL.” The VA-MH NO SHOW APPT CLINICS LL location list

> includes clinic stop codes for MH clinics that are scheduled for face-to-face appointments.

> Future appointments will list on this report. The number of days’ worth of future appointments that will list is defaulted to 30 days in the future. A new parameter SD MH NO SHOW DAYS has been added to store the number of days for which future appointments will be listed. This parameter can be edited by the user by using the option \[ XPAR EDIT PARAMETER\] Edit Parameter Values.

### This is how the report will display to the screen when reading Mailman.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Subj: HRMH NO SHOW NIGHTLY REPORT MESSAGE \# \[#71441\] 03/22/13@11:29 22 lines

> From: POSTMASTER In 'IN' basket. Page 1 \*New\*

> Division/Clinic Appointment Totals

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 27%" />
<col style="width: 23%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th>Division/CLinic</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th>Unique</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td>NS</td>
<td>NSA</td>
<td>NAT</td>
<td>Patients</td>
</tr>
<tr class="even">
<td>ISC-SLC-A4/Mental</td>
<td>Health</td>
<td>1</td>
<td>1</td>
<td>0</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
</tbody>
</table>

> HIGH RISK MENTAL HEALTH NO SHOW NIGHTLY REPORT PAGE 1

> By CLINIC for Appointments on 3/21/13 Run: 3/22/2013@11:29

> \*STATUS: NS = No Show NSA = No Show Auto Rebook NAT = No Action Taken

> \# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> DIVISION/CLINIC/STOP: ISC-SLC-A4/Mental Health/188

1.  CRPATIENT,ONE C2222 3/21/2013@08:00 Mental Health

> \*NS WHPROVIDER,THIRTEEN

> Future Scheduled Appointments: 3/22/2013@12:00 Mental Health

2.  CRPATIENT,TWO C4444 3/21/2013@08:30 Mental Health

> \*NSA WHPROVIDER,THIRTEEN

> Future Scheduled Appointments: 3/25/2013@08:00 Mental Health 4/1/2013@08:00 Mental Health

### Example of the High Risk Mental Health NO Show Ad Hoc report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option (SD MH NO SHOW AD HOC REPORT High Risk MH No-Show Ad hoc Report), will list by one, many or All stop codes or only Mental Health stop codes defined in the Reminder Location List file under the ‘VA-MH NO SHOW APPT CLINICS LL’ entry.

> A series of prompts will be asked of the user to refine the report.

- The user will be asked to select a beginning and ending date; this will list the report within a certain date range.
- The division will be asked of the user: The report can list by one, many or all divisions.
- The user will then be asked to choose how the report should sort: by (M)ental Health Quick List, which will list only those clinics defined in the Reminder Location list, or by (C)linics or (S)top codes both of which will further prompt the user to refine the sort. If ?, ?? is entered by the user, a help prompt will be displayed.
- If the user selects to sort by (S)top codes, a prompt asking them to select stop codes by listing (A)ll stop codes, (mental health as well as non-mental health) or (M)ental Health stop codes only (that are defined in the Reminder Location List) and are stop codes in the divisions chosen to list in this report. Both selections will allow the user to choose one, many, or all stop codes.
- A prompt asking the number of days in the future to list the Future scheduled appointment is asked and will list the future scheduled appointments that many days in the future.

> When the report displays or prints:

- The division/Stop Code Name/Number will display on the report once for all patients who have no showed for that Stop Code and division. It will display again, when the stop code or division changes.
- A totals page will be displayed at the end of the report.

> Special Note: at the Select Stop Code prompt , the stop code may be selected by the stop code file number (as an example, selecting 188 below) or by the AMIS Reporting stop code ( 500 – 599 code numbers ). An example of each is shown below.

> Ad Hoc Report Examples – Before reminder follow-up

> The Ad Hoc Report can be used to see which patients with a no-show MH appointment have not been followed up with. Look for the Results: caption to see what, if anything, has been documented related to the MH no-show appointment via the High Risk MH No- Show Follow-up reminder dialog. Appointments with \*NAT status (No Action Taken) will not have results because the reminder dialog only addresses MH No-Show appointments.

### Example of High Risk MH No-Show Adhoc Report by Mental Health Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\* High Risk Mental Health NO SHOW Adhoc Report \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Select Beginning Date: 03/22/13// 03/22/13 (MARCH 22, 2013) Select Ending Date: 03/23/13// (MARCH 23, 2013)

> Select division: ALL//

> Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M// Select Number of days to List Future Appointments: 30//

> This output requires 80 column output

> Select Device: ;;9999 HOME

> ...HMMM, THIS MAY TAKE A FEW MOMENTS...

> HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 1

> MH CLINICS for Appointments 3/22/13-3/22/13 Run: 3/23/2012@08:26

> \*STATUS: NS = No Show NA = No Show Auto Rebook NAT = No Action Taken

> \# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* DIVISION/CLINIC/STOP: ISC-SLC-A4/Mental Health/188

> 1 CRPATIENT,TWO C4444 3/22/2013@12:00 Mental Health

> \*NS WHPROVIDER,THIRTEEN

> Home: (801)556-6666

> Cell: (801)222-6666

> Next of Kin:

> NOK: PRIMARY NOK CRPATIENT,TWO

> Relation: FRIEND

> Phone: (801)556-6666 Phone: (801)556-6666

> Work Phone: (801)565-6565

> Emergency Contact:

> E-Cont.: PRIMARY NOK CRPATIENT,TWO

> Relation: FRIEND

> 203 Main St

> SALT LAKE CITY,UT 84107 Phone: (801)556-6666

> Work Phone: (801)565-6565

> MHTC: MHTCSTAFF,ONE (HRMH TEST TEAM)

> Future Scheduled Appointments: 3/23/2013@12:00 Mental Health

> Results:

## Ad Hoc Report Examples – After reminder follow-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Example of High Risk MH No-Show Adhoc Report by Mental Health Clinic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\* High Risk Mental Health NO SHOW Adhoc Report \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Select Beginning Date: 03/22/13// 03/22/13 (MARCH 22, 2013) Select Ending Date: 03/23/13// (MARCH 23, 2013)

> Select division: ALL//

> Sort report by (M)ental Health Clinic Quick List,(C)linic or (S)top Code: M// Select Number of days to List Future Appointments: 30//

> This output requires 80 column output

> Select Device: ;;9999 HOME

> ...HMMM, THIS MAY TAKE A FEW MOMENTS...

> HIGH RISK MENTAL HEALTH NO SHOW ADHOC REPORT BY PAGE 1

> MH CLINICS for Appointments 5/14/12-5/23/12 Run: 5/23/2012@08:26

> \*STATUS: NS = No Show NA = No Show Auto Rebook NAT = No Action Taken

> \# PATIENT PT ID APPT D/T CLINIC/STATUS/PROVIDER

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* DIVISION/CLINIC/STOP: ISC-SLC-A4/Mental Health/188

> 1 CRPATIENT,TWO C4444 3/22/2013@12:00 Mental Health

> \*NS WHPROVIDER,THIRTEEN

> Home: (801)556-6666

> Cell: (801)222-6666

> Next of Kin:

> NOK: PRIMARY NOK CRPATIENT,TWO

> Relation: FRIEND

> Phone: (801)556-6666 Phone: (801)556-6666

> Work Phone: (801)565-6565

> Emergency Contact:

> E-Cont.: PRIMARY NOK CRPATIENT,TWO

> Relation: FRIEND

> 203 Main St

> SALT LAKE CITY, UT 84107 Phone: (801)556-6666

> Work Phone: (801)565-6565

> MHTC: MHTCSTAFF,ONE (HRMH TEST TEAM)

> Future Scheduled Appointments: 03/23/2013@12:00 Mental Health

> Results:

> Resolution: Last done 03/22/2012@12:00

> Reminder Term: VA-MH NOSHOW PT EMERGENT CARE

> Health Factor: MH NOSHOW PT EMERGENT CARE

> 03/22/2013@12:00

> Reminder Term: VA-MH SUICIDE ATTEMPTED

> Health Factor: MH SUICIDE ATTEMPTED

> 03/22/2013@12:00

> <span id="Patient_Record_Flag_Category_I_HIGH_RISK" class="anchor"></span>Patient Record Flag Category I HIGH RISK FOR SUICIDE

> This project includes the new Category I Patient Record Flag called HIGH RISK FOR SUICIDE. The existing DGPF RECORD FLAG MANAGEMENT \[Record Flag Management\] option is used to manage the new Category I PRF.

### NOTE: Prerequisites to writing Progress Notes in CPRS to document PRF activity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before MH professionals can write progress note that documents the new Category I PRF activity, the PRF progress note titles must be set up correctly and the MH professional must be a member of a specific User Class.

> The National Category I PRF flags are distributed with a pre-defined Progress Note title so sites should not create a local progress note title.

> Each user that will be creating progress notes related to a PRF must be assigned the DGPF PATIENT RECORD FLAG MGR user class via the USR CLASS MANAGEMENT MENU \[User Class Management\] menu option.

> Before the progress note is created, a user must have assigned the flag to the patient.

> Sites must complete the following set up for users to write a progress note and correctly link the note to a PRF action:

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/061.png) Any local Category II PRF definitions must contain the progress note title that the user will use to document PRF actions. Each PRF note title can only be associated with one flag. Category I PRF definitions will be created automatically for sites during national patch installs.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/062.png) Any Category II PRF note titles added by the site should follow the naming conventions described in related directives and be descriptive enough that users can tell which note title corresponds to which flag. Category I PRF note titles will be created automatically for sites during national patch installs.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/063.png) Add the users that will be creating PRF progress notes as a member of the DGPF PATIENT RECORD FLAG MGR user class. Each site will be responsible for using the User Class Management menu option to populate membership in this user class. The user will not see the progress note title for selection in CPRS until the user is added as a member of this user class.

### New options for key SPC or MH Professional for PRF Transmission Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> One or more SPCs or MH professionals on each VistA system should be assigned the DGPF TRANSMISSION MGMT \[Record Flag Transmission Mgmt\] menu option. This option will be used to monitor errors are perform manual transmissions of PRFs between two sites. This will be a new option for SPCs and MH professionals. The Transmission management option should be reviewed weekly or an agreed upon frequency (verify with Office of Mental Health Services.

> The Record Flag Transmission Errors (on the DGPF TRANSMISSION MGMT menu) is an option that can be used with the DGPF TRANSMISSIONS key, to review and manage Rejected Status ("RJ") HL7 transmission messages that are received from Treating Facilities of the patient when trying to share Category I PRF Assignment information.

> If a new treating facility contacts the site SPC about a Category I PRF, the SPC can manually transmit the Category I flag to the new treating facility using the Record Flag Manual Query option (on the DGPF TRANSMISSION MGMT menu).

### Ownership of Category 1 flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each Category I flag assignment to a specific patient’s record is owned by a single facility. The facility that placed the Category I flag on the patient’s record would normally own and maintain the flag. The site that owns the Category I flag is the only site that can:

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/064.png)Review whether to remove or continue the flag, Edit the flag,

> Inactivate the flag, Reactivate the flag,

> Mark the flag as entered in error, Change ownership of the flag,

> Enter a Patient Record Flag Category I progress note for the flag,

> However, ownership of a Category I flag assignment can be transferred. If a patient received the majority of care at a different VA facility than the one that assigned the flag, the site giving the majority of care could request that ownership of the flag be transferred to the that site. The owning site could then change the ownership to the second site through the PRF software in List Manager.

### Transmission Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/065.png) Add the DGPF TRANSMISSION MGMT option to menus. (This option will only be assigned to a few staff at your site – it should be provided to the same person who runs the conversion).

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/066.png)Allocate the DGPF TRANSMISSIONS key to the same users as above.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/067.png) Add the same users to the DGPF HL7 TRANSMISSION ERRORS MailGroup.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/068.png)Add names to the DGPF CLINICAL HR FLAG REVIEW Mail group

### Record Flag Transmission Errors Option Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DGPF TRANSMISSIONS key description.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/069.png) DGPF CLINICAL HR FLAG REVIEW Mail group

> The MailGroup Owner of the DGPF CLINICAL HR FLAG REVIEW MailGroup (as entered during the installation process) will need to add these names after the multi- package build is installed. The MailGroup members added to this MailGroup will receive the reports and any error messages generated by the local-to-national PRF processing in a MailMan Message. This can include all facility SPCs if you’re an integrated site.

> NOTE: The DGPF CLINICAL HR FLAG REVIEW MailGroup is not used to document PRF Transmission Errors. It is only used to let MailGroup members know the patient’s PRF is due for a review.

### Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example of a transmission error logged at the site that originated the Category I flag (“owner” site) for a patient

> The “Assignment Transmitted To” will be the site that could not be updated because the Category I flag has not been installed on the site’s system.

> Messages sent to the users will need to be checked for the reject reason of “Record Flag is already assigned to patient,” so they can coordinate with the other site that is also owner of the Cat I HIGH RISK FOR SUICIDE record.

> For patients where the Category I HIGH RISK FOR SUICIDE has two sites that think they are owners:

> This scenario will continue at the sites as if each site is the Owner, until the owner sites’ SPCs or other MH professionals coordinate to determine which site will be the owner site. Then the SPC at the site that is not the owner will need to inactivate the Category I flag at their site.

# Appendix A: Clinical Reminders and CPRS Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/070.png)Clinician reminders are accessible in CPRS in four places: Cover Sheet

> Clock button (upper right-hand corner of each tab in CPRS) Notes tab

> Reports tab (Health Summaries)

> NOTE: The cover sheet display of reminders can be customized for Site, System, Location, or User.

> Cover Sheet

> Clinical reminders that are due are displayed on the cover sheet of CPRS. When you left-click on a reminder, patient-related details are presented in a pop-up window. By right-clicking on a reminder on the cover sheet, you can access the reminder definition and reference information.

> More details about what’s available from the Cover Sheet are provided in the following pages.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/071.png)

> <span id="_bookmark36" class="anchor"></span>Figure 26: CPRS Cover Sheet with Clinical Reminders box

> Clinical Maintenance View

> If you left-click on a particular reminder you will see the Clinical Maintenance output, which gives you the details of the reminder evaluation. It tells you the status, Due Date, and date Last Done.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/072.png)

> <span id="_bookmark37" class="anchor"></span>Figure 27: Clinical Maintenance View

### Right-clicking on a Reminder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you right-click on a reminder, you will see a popup menu that looks similar to this:

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/073.png)

> <span id="_bookmark38" class="anchor"></span>Figure 28: Right-clicking a Reminder on the CPRS Cover Sheet

> Clicking on Clinical Maintenance will show you the same Clinical Maintenance output you get by left- clicking.

> If the reminder contains education topics, Education Topic Definition will be selectable and clicking on it will display the education topic definitions.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/074.png)

> <span id="_bookmark39" class="anchor"></span>Figure 29: Education Topic

> Reminder Inquiry

> Clicking on Reminder Inquiry will produce a display of the reminder definition.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/075.png)

> <span id="_bookmark40" class="anchor"></span>Figure 30: Reminder Inquiry

> Reference Information

> If you click on Reference Information, you will get a list of web sites that have information related to the clinical reminder. Clicking on one of them will open your web browser at that site.

> Reminder Icon Legend

> Clicking on Reminder Icon Legend will bring up a display that shows what the various reminder icons mean. These icons will appear on the CPRS header bar (referred to as the Clock button).

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/076.png)

> <span id="_bookmark41" class="anchor"></span>Figure 31: Reminders Icon Legend

### Clock Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Another place you can interact with Clinical Reminders is by clicking on the reminders button in the upper right hand corner of the CPRS GUI. The reminders button looks like an alarm clock and corresponds to the status of the reminder, as indicated in the icon legend shown on the previous page.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/077.png)

> <span id="_bookmark43" class="anchor"></span>Figure 32: Clock Button

> This brings up the Available Reminders window, which shows the same tree view as seen in the Reminders drawer.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/078.png)

> <span id="_bookmark44" class="anchor"></span>Figure 33: Available Reminders Window

> This window has two menus: View and Action.

> View Menu

> The View menu lets you determine which categories of reminders will be displayed in the tree view. Those with a checkmark to the left of this will be displayed. You can toggle the checkmark on or off by left clicking on the icon. Note: as soon as you click on an icon the View menu will disappear and the tree will be updated to match your current selection. To make another change, left-click on View.

> The tree view you see here is identical to the one you see in the Reminders “drawer,” so whatever change you make here affects the tree you see in the Reminders drawer.

### Action Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Evaluate Reminders

> You can evaluate an individual reminder, all the reminders in a category, or a processed reminder. A processed reminder is one whose dialog has been processed by checking off items; a checkmark appears by the reminder icon. The option that is selectable out of these three options depends on what has been selected on the reminders tree. If it is an individual reminder, then Evaluate Reminder will be selectable, if it is a category, then Evaluate Category Reminders will be selectable, and if it is a processed reminder, then Evaluate Processed Reminder will be selectable.

> The other two options, Refresh Reminder Dialogs and Edit Cover Sheet Reminder List, are for use by Reminder Managers.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/079.png)

> <span id="_bookmark45" class="anchor"></span>Figure 34: Action Menu on Available Reminders

### Notes Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reminders processing takes place through the Notes tab. When you click on the Notes tab and open a new note, a Reminders tab appears.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/080.png)

> <span id="_bookmark46" class="anchor"></span>Figure 35: Reminders Drawer on Notes Tab

> When you click on the Reminders drawer, a list of reminders is displayed, categorized by Due, Applicable, Not Applicable, and Other Categories. Reminders that have an associated dialog have a special icon (see the previous Reminder Icons Legend). If you click on one of these reminders, a dialog box appears which lists possible actions or activities that may satisfy this reminder.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/081.png)

> <span id="_bookmark47" class="anchor"></span>Figure 36: Reminder Dialog Tree View

## Processing/ Resolving Clinical Reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: Your site can determine the folder view – which reminders and categories/folders appear in the reminders drawer.

> *Summary of Steps to Process Reminders*

> These are the basic steps for processing reminders from the Notes tab in CPRS.

1.  Start a new progress note. To process a reminder, start a new progress note. When you begin a new progress note, the reminders drawer appears.
2.  Open the reminders drawer. When you click on the reminders drawer, you see several folders containing reminders for this patient. Possible folders include Due, Applicable, Not Applicable, All Evaluated, and Other Categories. These folders may contain a hierarchy of folders and reminders within folders. The view of folders is site-customizable. The folders and subfolders in the Reminders Drawer are sometimes called the “tree view.”
3.  Choose a reminder. Open a folder (if necessary) and click a reminder that you wish to process. At this point, you may be asked to provide the primary encounter provider, so that any PCE data entered from reminder dialog processing can be saved. If the reminder has an associated reminder dialog, a small dialog icon is shown in the bottom-right corner of the clock icon. If you click on one of these reminders, a dialog box appears, which lists possible actions or activities that may satisfy this reminder. If this is a National reminder, the dialog was created by national developers and/or members of the Office of Quality and Performance. Otherwise, the contents of this dialog were created at your site by your Clinical Application Coordinator (CAC) or a Clinical Reminders Manager. Clinicians should be involved with defining these dialogs.

> If no dialog icon is displayed on a reminder, it means that your site hasn’t created and/or linked a dialog to the reminder. Your CAC can provide information about this. Definitions of the reminders icons are available on the Action menu of the Available Reminders window.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/082.png)

> <span id="_bookmark49" class="anchor"></span>Figure 37: Reminders Drawer with icons described

4.  Complete the dialog box. The dialog box lists possible actions or interventions that may be taken to satisfy this reminder. As you make selections from the dialog box, you can see the text of the progress note in the bottom part of the screen (below the Clear, Back, and Next buttons). Below the progress note text area is the encounter information including orders and PCE, Mental Health, and Vital Sign data. The bold text in these areas applies to the specific reminder you are processing. You can process multiple reminders.
5.  Expanded dialog boxes. Clicking a checkbox may bring up additional choices: an area for comments, a diagnosis to choose, or other information that may satisfy the reminder.

> Dialog with orders. Reminder dialogs can include orders. If quick orders are included in the dialog, these are placed as soon as the reminder processing is finished and the orders are signed. If the order requires more information before releasing the order, an order dialog will appear after you click Finish, allowing you to complete the order.

> Mental health tests. Reminder dialogs can include a pre-defined set of mental health tests. PXRM\*2\*6 expands the number of MH tests that can be included in dialogs, and even more will be available when CPRS GUI v27 is released. Progress note text can be generated based on the mental health score.

6.  Finish processing the reminder and complete your note. Click on the Finish button when you have checked all the appropriate checkboxes for each reminder you wish to process. You then go back to the Note window, where you can review and edit the reminder dialog progress note text

> added, to have a completed progress note for the encounter.

7.  (Optional) Evaluate processed reminders. You can use the Action menu to select the Evaluate Processed Reminders menu item from the Reminders Available window, to ensure that the reminders are satisfied. This action will evaluate the reminders that you processed while you wait, and update the Reminders Available window and reminders drawer lists to reflect the new statuses.

# Appendix B: Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## OI Master Glossary:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [<u>http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm</u>](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

### National Acronym Directory:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [<u>http://vaww1.va.gov/Acronyms/</u>](http://vaww1.va.gov/Acronyms/)

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AIMS</td>
<td><blockquote>
<p>Abnormal Involuntary Movement Scale</p>
</blockquote></td>
</tr>
<tr class="even">
<td>AITC</td>
<td><blockquote>
<p>Austin Information Technology Center</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>API</td>
<td><blockquote>
<p>Application Programmer Interface.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ASU</td>
<td><blockquote>
<p>Authorization/Subscription Utility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Clin4</td>
<td><blockquote>
<p>National Customer Support team that supports Clinical Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CAC</td>
<td><blockquote>
<p>Clinical Applications Coordinator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DBA</td>
<td><blockquote>
<p>Database Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DG</td>
<td><blockquote>
<p>Registration and Enrollment Package namespace</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ESM</td>
<td><blockquote>
<p>Enterprise Systems Management (ESM)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FIM</td>
<td><blockquote>
<p>Functional Independence Measure</p>
</blockquote></td>
</tr>
<tr class="even">
<td>GEC</td>
<td><blockquote>
<p>Geriatric Extended Care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>GMTS</td>
<td><blockquote>
<p>Health Summary namespace (also HSUM)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>GUI</td>
<td><blockquote>
<p>Graphic User Interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HRMH/HRMHP</td>
<td><blockquote>
<p>High Risk Mental Health Patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IAB</td>
<td><blockquote>
<p>Initial Assessment &amp; Briefing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ICD-10</td>
<td><blockquote>
<p>International Classification of Diseases, 10th Edition</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ICR</td>
<td><blockquote>
<p>Internal Control Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IHD</td>
<td><blockquote>
<p>Ischemic Heart Disease</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IOC</td>
<td><blockquote>
<p>Initial Operating Capabilities</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>LDL</td>
<td><blockquote>
<p>Low-density lipo-protein</p>
</blockquote></td>
</tr>
<tr class="even">
<td>LSSD</td>
<td><blockquote>
<p>Last Service Separation Date</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MDD</td>
<td><blockquote>
<p>Major Depressive disorder</p>
</blockquote></td>
</tr>
<tr class="even">
<td>MH</td>
<td><blockquote>
<p>Mental Health</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MHTC</td>
<td><blockquote>
<p>Mental Health Treatment Coordinator</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OHI</td>
<td><blockquote>
<p>Office of Health Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OI</td>
<td><blockquote>
<p>Office of Information</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OIF/OEF</td>
<td><blockquote>
<p>Operation Iraqi Freedom/Operation Enduring Freedom</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OIT/OI&amp;T</td>
<td><blockquote>
<p>Office of Information Technology</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OMHS</td>
<td><blockquote>
<p>Office of Mental Health Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>OQP</td>
<td><blockquote>
<p>Formerly Office of Quality and Performance, replaced by Office of Performance Measurement and Office of Quality, Safety &amp; Value</p>
</blockquote></td>
</tr>
<tr class="even">
<td>OQSV</td>
<td><blockquote>
<p>Office of Quality, Safety &amp; Value</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ORR</td>
<td><blockquote>
<p>Operational Readiness Review</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PCE</td>
<td><blockquote>
<p>Patient Care Encounter</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PCS</td>
<td><blockquote>
<p>Patient Care Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PD</td>
<td><blockquote>
<p>Product Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PIMS</td>
<td><blockquote>
<p>Patient Information Management System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PMAS</td>
<td><blockquote>
<p>Program Management Accountability System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PTM</td>
<td><blockquote>
<p>Patch Tracker Message</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PXRM</td>
<td><blockquote>
<p>Clinical Reminder Package namespace</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RSD</td>
<td><blockquote>
<p>Requirements Specification Document</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SD</td>
<td><blockquote>
<p>Scheduling Package Namespace</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SQA</td>
<td><blockquote>
<p>Software Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="even">
<td>TIU</td>
<td><blockquote>
<p>Text Integration Utilities</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>USR</td>
<td><blockquote>
<p>ASU package namespace</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA</td>
<td><blockquote>
<p>Department of Veteran Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VHA</td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VISN</td>
<td><blockquote>
<p>Veterans Integrated Service Network</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VistA</td>
<td><blockquote>
<p>Veterans Health Information System and Technology Architecture</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Applicable</td>
<td>When a patient’s findings meet the patient cohort reminder evaluation.</td>
</tr>
<tr class="even">
<td>CNBD</td>
<td><p>Cannot Be Determined. If a frequency can’t be determined for a patient, the Status and Due Date will both be CNBD and the frequency display that</p>
<p>follows the status line will be “Frequency: Cannot be determined for this patient.”</p></td>
</tr>
<tr class="odd">
<td>Clinical Reminder</td>
<td>A clinical reminder is a software decision support tool that defines evaluation and resolution logic for a given clinical activity. The evaluation logic defines conditions in the database, including the presence or absence of specified criteria such as diagnoses, procedures, health factors, medications, or demographic variables (e.g., age, gender). A reminder may or may not require provider resolution, depending on its purpose and design, through a user interface, also known as a reminder dialog. Also, in accordance with the underlying logic, reminders may be used to collect specified patient information that may or may not be related to the dialog.</td>
</tr>
<tr class="even">
<td>Component</td>
<td>A component represents the module that is presented in any given reminder.</td>
</tr>
<tr class="odd">
<td>Dialog Element</td>
<td><p>A dialog element is defined primarily to represent sentences to display in the CPRS window with a check-box. When the user checks the sentence, the FINDING ITEM in the dialog element and the ADDITIONAL FINDINGS will be added to the list of PCE updates, orders, Mental Health Notification Purposes, and mental health tests. The updates won't occur on the CPRS GUI until the user clicks on the FINISH button. Dialog elements may have components added to them. Auto-generated components will be based on the additional prompts defined in the Finding Type Parameters. Once a dialog element is auto-generated, the sites can modify them. Dialog elements may also be instructional text or a header. The FINDING ITEM and components</p>
<p>would not be defined in dialog elements.</p></td>
</tr>
<tr class="even">
<td>Dialog Group</td>
<td><p>A dialog group is similar to menu options. It groups dialog elements and dialog groups within its component. The dialog group can be defined with a finding item and a check-box. The components in the group can be hidden</p>
<p>from the CPRS GUI window until the dialog group is checked off.</p></td>
</tr>
<tr class="odd">
<td>Due</td>
<td>A reminder is DUE for a patient if the patient is in the cohort, and has not yet had the treatment, medication, education, etc., that is being searched for by the reminder.</td>
</tr>
<tr class="even">
<td>Finding Item</td>
<td><p>A Finding Item is a piece of information that can be searched by the</p>
<p>reminder.</p></td>
</tr>
<tr class="odd">
<td>Health Factors</td>
<td><p>A health factor is a computerized component that captures patient information for which no standard code exists, such as Family History of Alcohol Abuse,</p>
<p>Lifetime Non-smoker, No Risk Factors for Hepatitis C, etc.</p></td>
</tr>
<tr class="even">
<td>Mental Health Assistant</td>
<td><p>The Mental Health Assistant is a national VA software package that is used</p>
<p>for administration and scoring of standardized self-report questionnaires and tests. It is integrated with clinical reminders in that mental health assistant</p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p>instruments can be administered through a reminder dialog. Also the results of a specific instrument overall score, scale score, or specific item response can be used as a finding in reminder logic. This is the mechanism, for presenting questionnaires for screening for common mental health issues such</p>
<p>as the AUDIT-C for alcohol misuse.</p></td>
</tr>
<tr class="even">
<td>Prompt</td>
<td><p>An aid on the screen in the form of a question or statement indicating the</p>
<p>options available. Prompts are defined for PCE, MH Notification Purpose, or as locally created comment check-boxes.</p></td>
</tr>
<tr class="odd">
<td>PXRM</td>
<td>Clinical Reminder package namespace</td>
</tr>
<tr class="even">
<td>Reminder Component</td>
<td><p>A reminder component is any element, or part thereof, of a reminder, including the reminder’s definitions, dialogs, findings, terms, cohort logic or</p>
<p>resolution logic.</p></td>
</tr>
<tr class="odd">
<td>Reminder Definition</td>
<td>The reminder definition is the internal logic of the reminder. It describes the patients the reminder applies to, how often it is given, and what resolves or satisfies the reminder. It is comprised of the predefined set of finding items used to identify patient cohorts and reminder resolutions</td>
</tr>
<tr class="even">
<td>Reminder Dialog</td>
<td>The reminder dialog is the display that is seen by the user in the CPRS Graphical User Interface (GUI), when opening a reminder. Reminder dialogs are used in CPRS to allow clinicians to select actions that satisfy or resolve reminders for a patient. Information entered through reminder dialogs updates progress notes, places orders, and updates other data in the patient’s medical record. A reminder dialog is created by the assembly of components in groups into an orderly display.</td>
</tr>
<tr class="odd">
<td>Reminder Extracts</td>
<td><p>The Clinical Reminders application provides extract tools that enable sites to create extract summary reports based on an extract definition. An extract definition defines extract criteria similar to performance measure criteria. The extract definition specifies what patient lists should be created, which reminders should be run against each patient list, and what kind of totals should be accumulated. An extract run uses the extract definition to create</p>
<p>extract totals and stores these results in the Reminder Extract Summary file.</p></td>
</tr>
<tr class="even">
<td>Reminder Finding</td>
<td><p>Reminder finding is a type of data element in the Veterans Health Information</p>
<p>and Technology Architecture (VistA) that determines a reminder’s status.</p></td>
</tr>
<tr class="odd">
<td>Reminder Location List</td>
<td><p>Location Lists are a new finding type introduced in version 2.0. They provide a way to give a name to a list of locations. A Location List is built from two types of entries: Hospital Location, file #44 and Clinic Stop, file #40.7. There is a multiple for Hospital Locations and a multiple for Clinic Stops in the</p>
<p>Location List file, so when you build a list of locations, you can use Hospital Locations and/or Clinic Stops.</p></td>
</tr>
<tr class="even">
<td>Reminder Patient List</td>
<td><p>A list of patients that is created from a set of List Rules and/or as a result of report processing. Each Patient List is assigned a name and is defined in the Reminder Patient List File. Reminder Patient Lists may be used as an incremental step to completing national extract processing or for local reporting needs. Patient Lists created from the Reminders Due reporting process are based on patients that met the patient cohort, reminder resolution,</p>
<p>or specific finding extract parameters. These patient lists are used only at local facilities.</p></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Reminder Term</td>
<td><p>A reminder term is a predefined finding item(s) that are used to map local findings to national findings, providing a method to standardize these findings</p>
<p>for national use.</p></td>
</tr>
<tr class="even">
<td>Resolution</td>
<td><p>A reminder is considered RESOLVED (or SATISFIED) if the conditions defined by the reminder have been met. For example, if a reminder exists for influenza immunization, giving a flu vaccine</p>
<p>satisfies or resolves that reminder. Likewise, ordering lab tests or drugs or giving patient education can resolve a reminder.</p></td>
</tr>
<tr class="odd">
<td>Resolution Logic</td>
<td><p>Resolution logic specifies how findings are used in resolving a reminder. It is based on Mumps Boolean operators and their negations. The operators are:</p>
<p>! (OR), &amp; (AND), !’ (OR NOT), and &amp;’ (AND NOT)</p></td>
</tr>
<tr class="even">
<td>Result Element</td>
<td><p>A result element contains special logic that uses information entered during the resolution process to create a sentence to add to the progress note. The special logic contains a CONDITION that, when true, will use the ALTERNATE PROGRESS NOTE TEXT field to update the progress note. A separate result element is used for each separate sentence needed. The result element is only used with mental health test finding items. Default result elements are distributed for common mental health tests, prefixed with PXRM and the mental health test name. Sites may copy them and modify</p>
<p>their local versions as needed.</p></td>
</tr>
<tr class="odd">
<td>Result Group</td>
<td><p>A result group contains all of the result elements that need to be checked to create sentences for one mental health test finding. The dialog element for the test will have its RESULT GROUP/ELEMENT field defined with the result group. Default result groups for mental health tests are distributed with</p>
<p>the Clinical Reminders package. Sites may copy them and modify their local versions as needed.</p></td>
</tr>
<tr class="even">
<td>Term</td>
<td>A TERM is a collection of findings grouped together to make one concept.</td>
</tr>
<tr class="odd">
<td>TIU</td>
<td><p>Text Integration Utilities (TIU) simplifies the access and use of clinical documents for both clinical and administrative VAMC personnel, by standardizing the way clinical documents are managed.</p>
<p>TIU accepts document input from a variety of data capture methodologies. Those initially supported are transcription and direct entry. TIU allows</p>
<p>upload of ASCII formatted documents into VISTA.</p></td>
</tr>
</tbody>
</table>

# <u>Appendix C: Edit Cover Sheet Reminder List</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You can specify which reminders will appear on the cover sheet of CPRS. This is done by using the Edit Cover Sheet Reminder List option.

1.  While on the CPRS Cover Sheet, click on the Tools menu.
2.  From the drop-down menu that appears, click on Options. This screen appears:

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/083.png)

> <span id="_bookmark54" class="anchor"></span>Figure 38: Options menu in CPRS

3.  Click on the Clinical Reminders button to get to the editing form.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/084.png)

> <span id="_bookmark55" class="anchor"></span>Figure 39: Selecting Reminders to appear on CPRS Cover Sheet

4.  Highlight an item in the Reminders not being displayed field and then click the Add arrow

> “\>” to add it to the Reminders being displayed field. You may hold down the Control key and select more than one reminder at a time.

5.  When you have all of the desired reminders in the field, you may highlight a reminder and use the up and down buttons on the right side of the dialog to change the order in which the reminders will be displayed on the Cover Sheet.

> New Reminders Parameters (ORQQPX NEW REMINDER PARAMS)

> If you have been assigned this parameter, you can also modify the reminders view on the coversheet.

1.  Click on the reminder button next to the CWAD button in the upper right hand corner of the CPRS GUI.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/085.png)

> <span id="_bookmark56" class="anchor"></span>Figure 40: Modifying Reminders view via clock on CPRS Cover Sheet

2.  Click on Action, then click on Edit Cover Sheet Reminder List.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/086.png)

> <span id="_bookmark57" class="anchor"></span>Figure 41: Edit Cover Sheet Reminder List via Clock button

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/087.png)

> <span id="_bookmark58" class="anchor"></span>Figure 42: Cover Sheet Reminders and Categories displayed on Cover Sheet

> This form provides very extensive cover sheet list management capabilities. It consists mainly of three large list areas.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/088.png) *Cover Sheet Reminders (Cumulative List)* displays selected information on the Reminders that will be displayed on the Cover Sheet.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/089.png) *Available Reminders & Categories* lists all available Reminders and serves as a selection list.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/090.png) *User Level Reminders* displays the Reminders that have been added to or removed from the cumulative list.

> You may sort the Reminders in *Cover Sheet Reminders (Cumulative List)* by clicking on any of the column headers. Click on the Seq (Sequence) column header to view the Reminders in the order in which they will be displayed on your coversheet.

# Appendix D: Creating a Mental Health Test button for use in a Reminder Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From [<u>A Wiki for VA Health Professionals</u>](https://vaww.wiki.webdev.va.gov/index.php?title=Main_Page)

> \< [<u>CPRS Tips and Tricks</u>](https://vaww.wiki.webdev.va.gov/index.php?title=CPRS_Tips_and_Tricks) \| <u>Clinical Reminders</u>

> Create the following three components with the settings that are in Bold for the entry fields. You can then add the dialog element to a Reminder dialog to present a button to open the Mental Health test.

> Note: You will have to change view in the dialog editor to go to RG and RE for result elements and result groups.

# <u>Appendix E: Tips, Tricks, and FAQs</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When filling out reminder dialogs, don't click the Finish button unless you are sure that the information you've entered is correct for the patient.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once you click the finish button, the data is submitted to the various Vista Packages (i.e. problems, allergies, etc.) and won't be erased, even if you've deleted your unsigned note.

![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/091.png)

> <span id="_bookmark61" class="anchor"></span>Figure 43: Finish button on Reminder Dialog

1.  Recognizing inappropriate "due" reminders and how to deal with them:

> If a patient has an inappropriately due reminder, most likely it is due to an incorrect diagnosis. For example, diabetic reminders are triggered if the patient has a diagnosis of diabetes. When addressing inappropriate reminders,

> DO: select the option that states "incorrect diagnosis".

> DO NOT: Fill enter miscellaneous information into the reminder just to get rid of it. Doing so will affect patient safety, as well as document incorrect workload/encounter data, billing, and performance measures.

### Tips to making sure you resolve your reminders quickly and completely:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/092.png) When recording dates of exams and results, make sure you enter the month, day, and year of exam as close to actual time patient received them as possible. Why? The date of when the last exam/results is used to set the clock for when it will be due again.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/093.png) Whenever possible, have your support staff enter their notes and process their reminders BEFORE you start your note. Doing so will satisfy any reminders you have that shares the same resolution logic so that you don't have to do them. Make sure to refresh the patient record (File \> Refresh patient information) before starting your note. This will allow the system to display the latest information.

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/094.png) Make sure you complete ALL applicable sections of the reminder. If you skip any applicable sections, the reminder will not resolve. If the section is not applicable, make sure you select the option that allows you to say "not applicable" or "not clinically indicated". \*NOTE\* Please use "not clinically indicate" carefully.

> Examples of good reasons to use NCI:

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/095.png) Colorectal CA Screening: Life expectancy of less than 5 years but \> 6 months, patient could not tolerate follow-up colonoscopy

> ![](pxrm-2-18-high-risk-mental-health-patient-reminder-and-flag-user-manual/096.png)Diabetes Foot, Eye, HGBA1C: Limited life expectancy, blind patient

> Hepatitis C lab testing: Patient with + risk factors but with limited life expectancy and transmission potential is very low.

### FAQ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Question from Upstate NY:

> VISN 2 has installed the patch and is entering the Cat I flag and this question has come up.

> Tied to our existing Cat II flag is a reminder dialog called OMHS PRF HIGH RISK SUICIDE. I don’t recall the history on this but the Suicide Prevention Coordinators are used to calling up the title and having the attached dialog to complete. My question is should this reminder dialog be attached to the new Cat I title? If so, the verbiage needs to be changed as it references the Cat II flag. Apparently there is a key or user class that is restricting this new title because I cannot see the title in my list so I would not be able to attach the reminder dialog to the new title.

### Follow-Up response from <span class="mark">REDACTED</span>:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> With the local Cat II PRF, we distributed documentation templates that were local reminder dialog templates. These utilized health factors to designate the activation and inactivation of the flag. The health factors were used by VSSC to determine when a patient was to be included in the high risk PM.

> This will not be necessary for the national Cat I PRF.

> Sites will still need to document the activation, inactivation and continuation of the flag, but the documentation can flow clinically and will not need health factors. So the standardized documentation will not be required.

> Q: Will there be a flag note attached from VistA for new Category I Flags, as there was for Category II Flags? If so, what is the process? Will it still contain the Health Factors because that is a tool used to capture flags in a VISN 5 Warehouse program that tracks high risk flagging.

> A: The patient record flag requires that a note be attached to all PRFs. The new national Category I PRF High Risk for Suicide will use a new note title: PATIENT RECORD FLAG CATEGORY I - HIGH RISK FOR SUICIDE

> A: It is not required to use health factors with the Category I PRF—the national PRF data is extractable. However, if you want to link the existing template that captures health factors to the new TIU note title, you can do this.

> Q: The notes that were attached to the Category II flags that were transitions do not have the attached notes any longer (new assignment note, and review notes) How will providers be able to see detailed information about the flag/risk for self-harm?

> A: The old local Category II flag is inactivated in the conversion process. Progress notes that were written and attached to that flag should remain attached to that flag.

> The newly created Category I flag will have a new progress note attached to it.

> In the PRF package, entries are automatically made to the flag history to indicate an automatic inactivation of the local category II flag due to the conversion and an automatic activation of the national category I flag.

> I don’t think the history and/or notes are linked in any way, but this is a good question to evaluate further to make sure we have complete understanding of the process.

> Q: All the transitioned Flags now have the initial flag date of August 21, 2012…..How can/should we document when the old flags were originally flagged?

> A: As noted above, there is text that is included in the PRF history indicating that conversion process activated the flag on the date of the conversion

> Q: Has the flag review date also changed? Will all of these flags need to be reviewed on the same date (90 days from August 21<sup>st</sup>)?

> A: The conversion process evaluates the review date. If the old flag had a date that was less than 90 days out from the conversion date, then that date will carry over to the review date for the category I flag. If by chance, the facility had a review time that was longer than 90 days, then the review date will be set at 90 days from the conversion

> Q: Do we have to make any adjustments in SPAN regarding these changes?

> A: I would say no, but would defer to Jan—clinically the flag is still being continued and high risk status maintained. It is simply the actual flag that is changing—category II to category I

> Q: Concern: How can providers make distinctions between the Behavioral Flags (which also flash/orange) from Suicide Risk? Will our High Risk Vets mistakenly be treated with violence risk instead of compassion?

> A: There will now be 2 national category I PRFs. We are working with the national PRF advisory committee to develop and disseminate educational materials to ensure that the field understands that two distinct flags are now available in the category I national status

> Q: What are the instructions for adding, reviewing, and inactivating Category I flags?

> A: Clinically, the process is the same. Technically, you would follow the same process of selecting the flag in the PRF package, but you would now be selecting the Category I PRF rather than a Category II flag. As noted in earlier questions, the progress note title is different, but you would still attach a note. You can link the current documentation template to the new title.

> Q: Who is the point of contact at our site? Are there meeting that we (one rep from SP Team) can attend about this pilot?

> A: You can look up your Facility and VISN PCMM Coordinator contact information by clicking on the [following link: http://vssc.med.va.gov/pcmm/](http://vssc.med.va.gov/pcmm/)

> Click link “b.” in the page that appears for your specific VISN/Facility Information

> Q: Should we make changes to our policy (our policy mentions Category II flags only) to represent these changes for the pilot?

> A: There will be a letter coming from the 10N office and the PRF advisory committee is modifying the national PRF directive. Updating your local policy to reflect the new national PRF would be recommended, and something we should probably include in our education materials.