---
title: QUASAR Version 3 User Manual (Updated ACKQ*3*21)
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: (Updated ACKQ*3*21)
app_code: ACKQ
app_name: Quality Audiology and Speech Analysis and Reporting (QUASAR)
section: CLI
app_status: active
pkg_ns: ACKQ
patch_ver: 3
patch_id: ACKQ*3
group_key: "ACKQ:ACKQ:3"
file_numbers: 
  - 2
  - 200
security_keys: []
menu_options: 3
description: "Quality: Audiology and Speech Analysis and Reporting (QUASAR) is a VISTA software package written for the Audiology and Speech Pathology Service. QUASAR is used to enter, edit, and retrieve data for each episode of care."
audience: 
keywords: 
  - class
  - date
  - visit
  - patient
  - table
  - print
  - contents
  - strong
  - code
  - audiogram
page_count: 0
word_count: 33597
section_count: 40
table_count: 7
figure_count: 0
appendix_count: 9
has_toc: False
is_stub: False
pub_date: February 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=97"
---

---
title: |
  <span id="_Toc361666135" class="anchor"></span>Quality Audiology and Speech Analysis and Reporting (QUASAR)

  <span id="_Toc361666136" class="anchor"></span>User Manual
---

![](quasar-version-3-user-manual-updated-ackq-3-21/001.png)

February 2000

Office of Information and Technology (OIT)

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Implementing & Maintaining the QUASAR Package](#implementing-maintaining-the-quasar-package)
  - [Implementation Checklist (Virgin Installations Only)](#implementation-checklist-virgin-installations-only)
  - [Implementation Checklist (Installations over V. 2.0)](#implementation-checklist-installations-over-v-20)
  - [Menu Option Assignment](#menu-option-assignment)
    - [A&SP Supervisor Menu](#asp-supervisor-menu)
    - [Audiology & Speech Visit Tracking System](#audiology-speech-visit-tracking-system)
    - [A&SP Reports](#asp-reports)
  - [Key Assignment](#key-assignment)
  - [Options for Implementing and Maintaining the Package](#options-for-implementing-and-maintaining-the-package)
    - [Set Up/Maintenance Menu](#set-upmaintenance-menu)
- [Entering and Viewing Clinic Visit Data](#entering-and-viewing-clinic-visit-data)
  - [Audiology & Speech Visit Tracking System](#audiology-speech-visit-tracking-system-1)
    - [Appointment Management and PCE Interfaces](#appointment-management-and-pce-interfaces)
    - [Avoiding Mismatches between QUASAR and PCE](#avoiding-mismatches-between-quasar-and-pce)
    - [Data Mismatch between PCE and QUASAR](#data-mismatch-between-pce-and-quasar)
    - [New Clinic Visits](#new-clinic-visits)
    - [Edit an Existing Visit](#edit-an-existing-visit)
    - [Inquire - A&SP Patient](#inquire-asp-patient)
    - [A&SP Reports](#asp-reports-1)
- [Generating Management Reports](#generating-management-reports)
  - [Management Reports A&SP](#management-reports-asp)
    - [Generate A&SP Service CDR](#generate-asp-service-cdr)
    - [Print A&SP Service CDR](#print-asp-service-cdr)
    - [Compile A&SP Capitation Data](#compile-asp-capitation-data)
    - [Print A&SP Capitation Report](#print-asp-capitation-report)
- [Adequating a C&P Exam](#adequating-a-cp-exam)
  - [C&P Exam Adequation](#cp-exam-adequation)
- [Deleting a Clinic Visit](#deleting-a-clinic-visit)
  - [Delete an A&SP Clinic Visit](#delete-an-asp-clinic-visit)
- [Creating Tailor-Made Reports](#creating-tailor-made-reports)
  - [Introduction](#introduction-1)
  - [Data Dictionaries](#data-dictionaries)
    - [A&SP Patient file \#509850.2](#asp-patient-file-5098502)
    - [A&SP Clinic Visit file \#509850.6](#asp-clinic-visit-file-5098506)
  - [VA FileMan Sort and Print Options](#va-fileman-sort-and-print-options)
  - [Writing Your Own Tailor-Made Reports](#writing-your-own-tailor-made-reports)
  - [Examples of Tailor-Made A&SP Reports](#examples-of-tailor-made-asp-reports)
    - [Report \#1: Student Cost Distribution Report](#report-1-student-cost-distribution-report)
    - [Report \#2: Patient Addresses](#report-2-patient-addresses)
    - [Report \#3: Visit Report (Provider/Time Spent/Diagnostic Code)](#report-3-visit-report-providertime-spentdiagnostic-code)
    - [Report \#4: Visit Report (Procedure Code/Cost)](#report-4-visit-report-procedure-codecost)
    - [Report \#5: Visit Report (Procedure Time)](#report-5-visit-report-procedure-time)
    - [Report \#6: C&P Examinations](#report-6-cp-examinations)
    - [Report \#7: Visit Report (Procedure Codes/Date and Provider)](#report-7-visit-report-procedure-codesdate-and-provider)
    - [Report \#8: ASHA Data on Trainees](#report-8-asha-data-on-trainees)
    - [Report \#9: Procedure Time Report](#report-9-procedure-time-report)
    - [Report \#10: Clinic Management Report](#report-10-clinic-management-report)
- [Introduction](#introduction-2)
  - [Related Documentation](#related-documentation)
  - [Conventions Used](#conventions-used)
  - [Monitor/Keyboard Placement](#monitorkeyboard-placement)
- [What’s New in Audiogram Module Patch ACKQ\3.0\13](#whats-new-in-audiogram-module-patch-ackq3013)
- [Accessing the Audiogram Module](#accessing-the-audiogram-module)
- [Audiogram Edit Window](#audiogram-edit-window)
  - [File Menu](#file-menu)
  - [Device Menu](#device-menu)
  - [Options/Graph Menu](#optionsgraph-menu)
  - [Help Menu](#help-menu)
  - [Status Bar](#status-bar)
- [Configuration of the Audiometer](#configuration-of-the-audiometer)
  - [Configure the Audiometer for the First Time](#configure-the-audiometer-for-the-first-time)
  - [Verify the Connection of the Audiometer](#verify-the-connection-of-the-audiometer)
- [Audiogram Entry](#audiogram-entry)
  - [Audiogram Entry Fields](#audiogram-entry-fields)
  - [Audiogram Entry/Date Signed](#audiogram-entrydate-signed)
- [Pure Tones](#pure-tones)
  - [Pure Tones Fields – Right and Left Ears](#pure-tones-fields-right-and-left-ears)
  - [Pure Tones - Air and Bone Conduction Values](#pure-tones-air-and-bone-conduction-values)
  - [Importing Pure Tones Data Points](#importing-pure-tones-data-points)
- [Speech Audiometry](#speech-audiometry)
  - [Speech Audiometry Fields: Right and Left Ears](#speech-audiometry-fields-right-and-left-ears)
  - [Speech Audiometry - Speech Reception and Word Recognition Values](#speech-audiometry-speech-reception-and-word-recognition-values)
  - [Importing SRT and WRT Data Points](#importing-srt-and-wrt-data-points)
- [Acoustic Immittance](#acoustic-immittance)
  - [Acoustic Immittance Fields: Right and Left Ears](#acoustic-immittance-fields-right-and-left-ears)
  - [Acoustic Immittance Values](#acoustic-immittance-values)
- [Graph Display](#graph-display)
  - [Graph Display Values](#graph-display-values)
  - [Graph Display in Separate View](#graph-display-in-separate-view)
  - [Graph Display in Overlap View](#graph-display-in-overlap-view)
  - [Graph Display in Tabular View](#graph-display-in-tabular-view)
  - [VA form 10-2364 Fields](#va-form-10-2364-fields)
- [Glossary](#glossary)
- [Appendix A: Black Box Audiometer](#appendix-a-black-box-audiometer)
- [Appendix B: Accessing Audiogram Display](#appendix-b-accessing-audiogram-display)
- [Appendix C: Determining Series Values to Place on the Graph](#appendix-c-determining-series-values-to-place-on-the-graph)
- [Appendix D: Calculation of PB Max and RI (or PI/PB)](#appendix-d-calculation-of-pb-max-and-ri-or-pipb)
- [Appendix E: Access to Multiple Broker Environments](#appendix-e-access-to-multiple-broker-environments)
- [Appendix F: Calculation of Pure Tone Averages](#appendix-f-calculation-of-pure-tone-averages)
- [Appendix G: VA FileMan Date/Time Formats](#appendix-g-va-fileman-datetime-formats)
- [Appendix H: Message Box Errors](#appendix-h-message-box-errors)
- [Appendix I: Shortcut Keys](#appendix-i-shortcut-keys)
- [Index](#index)
<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 48%" />
<col style="width: 10%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Page</strong></th>
<th><strong>Author/Manager</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>August 2014</td>
<td><p>ACKQ*3*21</p>
<ul>
<li><p>Updated Revision History to reference most recent changes at the beginning of the table.</p></li>
<li><p>Updated Table of Contents</p></li>
<li><p>Added (Procedure Code List) to “Print A&amp;SP File Entries” section title.</p></li>
<li><p>Added “Print A&amp;SP Diagnostic Condition List” example.</p></li>
<li><p>Updated Patient Inquiry Summary Example</p></li>
<li><p>Added note for CDR obsolescence in VistA.</p></li>
<li><p>Changed “ICD-9-CM code” references to “ICD code.”</p></li>
<li><p>Added Visits by Diagnosis example</p></li>
<li><p>Added ICD-10-CM to Glossary</p></li>
<li><p>Corrected spacing of Appendix I</p></li>
<li><p>Blank page added at end of manual for double sided printing</p></li>
<li><p>Added Note for CDR Obsolescence to page 38 per N. Smith and updated screen capture for ICD-10 activation date.</p></li>
</ul></td>
<td><p>iii-viii</p>
<p>ix-x</p>
<p><a href="#print-asp-file-entries-procedure-code-list">10</a></p>
<p><a href="#print-asp-diagnostic-condition-list">11-12</a></p>
<p><a href="#p21_19">19-22</a></p>
<p><a href="#ICDp23">25</a>, <a href="#p21_38">38</a></p>
<p><a href="#p21_21">23</a>, <a href="#p21_36">38</a>, <a href="#p21_40">40</a>, <a href="#p21_53">54</a>, <a href="#p21_68">69</a></p>
<p><a href="#p21_38_2">40-41</a></p>
<p><a href="#ICDp119">119</a></p>
<p><a href="#p21_138">139-140</a></p>
<p>144</p>
<p>19-25</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>November 2010</td>
<td><p>ACKQ*3*16</p>
<ul>
<li><p>Adding two more prompts: “Was care related to Head and/or Neck Cancer ?” and “Was care related to COMBAT ?” to the New Clinic Visits [ACKQAS VISIT ENTRY] option.</p></li>
</ul>
<p>ACKQ*3*17</p>
<ul>
<li><p>Changes to Staff (Enter/Edit) [ACKQAS CLINICIAN ENTRY] option to synchronize the A&amp;SP STAFF (#509850.3) file names with the NEW PERSON (#200) file names.</p></li>
</ul></td>
<td><p>22-23</p>
<p>6</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2007</td>
<td><ul>
<li><p>ACKQAG03 is modified to suppress the MailMan notification sent to the user when an AUDIOMETRIC EXAM DATA file (#509850.9) record is transmitted to the Denver ALC.</p></li>
<li><p>ACKQAG05 is modified to replace DDC with DALC in the subject of the MailMan message that confirms the deletion of an AUDIOMETRIC EXAM DATA file (#509850.9) record from the local and DALC databases.</p></li>
</ul>
<p>Remote procedure call ACKQAUD1 is added to the ACKQROES3E option to register the call to the Graph Display tab. The following remote procedure calls are removed from the ACKQROES3E option: XUS GET USER INFO, XUS INTRO MSG, XWB CREATE CONTEXT, XWB GET VARIABLE VALUE, and XWB GET BROKER INFO.</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>July 2007</td>
<td><p>ACKQ*3.0*13</p>
<ul>
<li><p>Removed Sections IX, X, and XI from the historical version of the user manual.</p></li>
<li><p>Configure one of three audiometric instruments, GSI61 (Grason-Stadler), Madsen-Aurical (GN Otometrics), and AC40 (Interacoustics).</p></li>
<li><p>Check and monitor the status of the audiometer connection.</p></li>
<li><p>Import audiometric data from the audiometer to the Audiogram Module, point by point or batch mode.</p></li>
<li><p>Reset values in audiometers capable of being reset and clear any buffers or memory used in the construction or passing of information.</p></li>
<li><p>Incorporate the graph (Audiogram Display component) as a tab in the Audiogram Edit window. The graphic display is updated in real time with data from the device.</p></li>
<li><p>The following items are added or modified to display within the surrounding area of the audiogram display (graph).</p></li>
</ul>
<ol type="a">
<li><p>Air Conduction averages</p></li>
<li><p>Audiogram symbol key, No Response, Rollover Index text boxes, and SRT, IAR, and CAR grids</p></li>
</ol>
<ul>
<li><p>Desktop access to the application is removed. The Audiogram Module can be configured and accessed only through the Computerized Patient Record System (CPRS) Tools menu.</p></li>
<li><p>The algorithm for <em>points to plot on the graph</em> uses the Retest value if there is no Final value.</p></li>
<li><p>The third row label on the Pure Tones tab changed from Final or Masked to Masked.</p></li>
<li><p>The Flip Tabs option is removed from the File menu.</p></li>
<li><p>A 1500 Hz column is added to the Pure Tones tab for Bone Conduction.</p></li>
<li><p>VA form 10-2364 is modified to conform to VA standards.</p></li>
</ul></td>
<td><p><a href="#report-10-clinic-management-report">77</a></p>
<p><a href="#configure-the-audiometer-for-the-first-time">89</a></p>
<p><a href="#verify-the-connection-of-the-audiometer">92</a></p>
<p><a href="#importing-pure-tones-data-points">102</a></p>
<p><a href="#importing-srt-and-wrt-data-points">106</a></p>
<p><a href="#pure-tones">99</a></p>
<p><a href="#speech-audiometry">103</a></p>
<p><a href="#graph-display">111</a></p>
<p><a href="#graph-display-in-separate-view">113</a></p>
<p><a href="#graph-display-in-overlap-view">114</a></p>
<p><a href="#accessing-the-audiogram-module">83</a></p>
<p><a href="#appendix-c-determining-series-values-to-place-on-the-graph">125</a></p>
<p><a href="#pure-tones">99</a></p>
<p><a href="#file-menu">85</a></p>
<p><a href="#pure-tones">99</a></p>
<p><a href="#graph-display-in-tabular-view">115</a></p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 2007</td>
<td><p>Combine, format, and update the QUASAR and the Audiogram Module User Manuals.</p>
<p>Historical version: Quality: Audiology and Speech Analysis Reporting (QUASAR)</p>
<p>GUI version: QUASAR Audiogram Module</p></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>February 2006</td>
<td><p>ACKQ*3.0*10</p>
<p>New message, <em>Patient died on mm/dd/yy</em>, prevents creating a new clinic visit for a deceased patient</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>October 2004</td>
<td><p>ACKQ*3.0*8</p>
<ul>
<li><p>Only allow the display of the correct version of ICD-9 and CPT modifiers code descriptions</p></li>
<li><p>Display the correct version of ICD-9 code description (ACKQAS PAT INQ)</p></li>
<li><p>Send the correct version of ICD-9 code description (ACKQAS VISIT ENTRY and ACKQAS VISIT EDIT)</p></li>
<li><p>Display the correct version of ICD-9 code description (ACKQAS VISITS BY DIAG)</p></li>
<li><p>Display the correct version of CPT code description (ACKQAS PRINT COST COMPARE)</p></li>
<li><p>Display the correct version of CPT code description (ACKQAS PROC STATS)</p></li>
<li><p>Display the correct version of the CPT modifier code description (ACKQAS UPDATE CPT MODIFIERS)</p></li>
<li><p>Display the correct version of CPT code description (ACKQAS COST ENTRY)</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>July 2003</td>
<td><p>ACKQ*3.0*7</p>
<p>Fixed problems related to the updating of the PCE problem list with diagnosis codes when entering or editing A&amp;SP clinic visits</p></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>September 2003</td>
<td><p>ACKQ*3.0*6</p>
<ul>
<li><p>Only allow the correct version of CPT codes (ACKQAS VISIT ENTRY and ACKQAS VISIT EDIT)</p></li>
<li><p>Only allow the entry of the correct version of ICD codes (ACKQAS VISIT ENTRY and ACKQAS VISIT EDIT)</p></li>
<li><p>Only allow the correct version of CPT codes (ACKQAS VACO DIRECTIVE)</p></li>
<li><p>Only allow the entry of the correct version of ICD codes (ACKQAS VACO DIRECTIVE)</p></li>
<li><p>Do not allow the entry of EC codes that have invalid CPT counterparts (ACKQAS VISIT ENTRY and ACKQAS VISIT EDIT)</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>March 2003</td>
<td><p>ACKQ*3.0*5</p>
<ul>
<li><p>Corrected the updating of patient diagnostic histories when using the inquire-A&amp;SP patient option</p></li>
<li><p>Stopped sending students as secondary providers - PCE rejected students because of a missing person class</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>March 2003</td>
<td><p>ACKQ*3.0*4</p>
<ul>
<li><p>File internal value of CPT code (not external)</p></li>
<li><p>Allow users to edit site parameters for the entry of event capture codes</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>November 2003</td>
<td><p>ACKQ*3.0*3</p>
<p>Release of the GUI interface, Audiogram Module with two components: Audiogram Edit and Audiogram Display</p></td>
<td></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>April 2001</td>
<td><p>ACKQ*3.0*2</p>
<ul>
<li><p>Remove integer only check of DFN within new clinic visit option</p></li>
<li><p>Convert A&amp;SP staff members’ IEN to corresponding IEN in file #200</p></li>
<li><p>Clear completed adequated visits from waiting adequation list</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>January 2001</td>
<td><p>ACKQ*3.0*1</p>
<ul>
<li><p>Update the PCE problem list when sending encounter data to PCE</p></li>
<li><p>Suppress PCE credit encounters for telephone clinics</p></li>
<li><p>Correct display of V codes with QUASAR’s Capitation report</p></li>
<li><p>Incorporate military sexual trauma functionality</p></li>
<li><p>Warning if a QUASAR staff member’s USR membership entry has been deleted</p></li>
<li><p>Warning if running PCE Exception report prior to install of version 3.0</p></li>
<li><p>Send examining physician to AMIE when adequating QUASAR visits</p></li>
<li><p>Add ability to choose between event capture codes and CPT codes</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>February 2000</td>
<td>QUASAR 3.0: original version</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
*This page intentionally left blank for double-sided printing.  
*
Table of Contents
Quality: Audiology and Speech Analysis and Reporting  
(QUASAR) V 3.0

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Quality: Audiology and Speech Analysis and Reporting (QUASAR) is a VISTA software package written for the Audiology and Speech Pathology Service. QUASAR is used to enter, edit, and retrieve data for each episode of care.

- QUASAR provides transmission of visit data to the Patient Care Encounter (PCE) program in order to incorporate QUASAR Visit Data in ACRP Workload Reporting, as well as to the Decision Support System (DSS).
- QUASAR produces a variety of reports useful to local managers, medical center management, and central planners.
- QUASAR contains a VA FileMan function that permits users to generate customized reports using data from QUASAR's A&SP Clinic Visit file (#509850.6) or A&SP Patient file (#509850.2).
- QUASAR produces an automated Cost Distribution RCS 10-0141 Report (CDR) and has an option for generating and processing audiology compensation and pension examinations through an agreement with the Automated Medical Information Exchange (AMIE) package.
- For current coding guidance, refer to the Audiology website: [VA Speech Pathology Services - Audiology and Speech Pathology Service](http://vaww1.va.gov/audiospeech/page.cfm?pg=4)

*This page intentionally left blank for double-sided printing*

# Implementing & Maintaining the QUASAR Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Implementation Checklist (Virgin Installations Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each of the following steps is described in greater detail within this chapter.

Assign menu options to users.

Assign the ACKQ ADHOC key to those users who will be designing reports using the Tailor-Made A&SP Reports option.

Add appropriate A&SP staff to the USR Class Membership file \# 8930.3 and assign a User Class to each. After staff is added to the USR Class Membership file, add the same A&SP staff to the A&SP Staff file \#509850.3. Also ensure that each A&SP staff member has an appropriate Person Class entry within the New Person file \#200.

Define site parameters using the A&SP Site Parameters option.

(Optional) Use the Update Files per CO Directive to add diagnoses to the A&SP Diagnostic Condition file and procedures to the A&SP Procedure Code file.

(Optional) Apply local cost amounts to each procedure using the Enter Cost Information Procedure option. You may use locally developed cost data, DSS product costs, community fees, insurance reasonable rates, or Medicare reasonable rates.

## Implementation Checklist (Installations over V. 2.0)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Define site parameters using the A&SP Site Parameters option.

Make sure each entry in the A&SP Staff file \#509850.3 also has an appropriate Person Class entry within the New Person file \#200.

(Optional) Use the Update Files per CO Directive to make any required changes to the A&SP Diagnostic Condition file and the A&SP Procedure Code file.

(Optional) Apply local cost amounts to each procedure using the Enter Cost Information Procedure option.

## Menu Option Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A&SP Supervisor Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The A&SP Supervisor Menu \[ACKQAS SUPER\] option is assigned to supervisory personnel. It is the main menu and contains options for setting up and maintaining the QUASAR package, entering clinic visit data, generating management reports, and adequating Compensation and Pension (C&P) exams.

#### Set Up/Maintenance 

- Staff (Enter/Edit)
- A&SP Site Parameters
- Update Files per CO Directive
- Print A&SP File Entries
- Enter Cost Information for Procedures
- Update CPT Modifiers per CO Directive

#### Audiology & Speech Visit Tracking System

- New Clinic Visits
- Edit an Existing Visit
- Inquire - A&SP Patient
- A&SP Reports
1.  Visits by Diagnosis
2.  Patients by City
3.  Statistics by Procedure
4.  Cost Comparison Report
5.  Tailor-Made A&SP Reports \*\*Locked: ACKQ ADHOC\*\*
6.  PCE Exception Report
7.  Workload Report

#### Management Reports A&SP

- Generate A&SP Service CDR
- Print A&SP Service CDR
- Compile A&SP Capitation Data
- Print A&SP Capitation Report

#### C&P Exam Adequation

#### Delete an A&SP Clinic Visit

### Audiology & Speech Visit Tracking System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiology & Speech Visit Tracking System \[ACKQAS MASTER\] menu option is assigned to personnel who will be entering clinic visit data and generating reports.

- New Clinic Visits
- Edit an Existing Visit
- Inquire - A&SP Patient
- A&SP Reports
1.  Visits by Diagnosis
3.  Patients by City
4.  Statistics by Procedure
5.  Cost Comparison Report
6.  Tailor-Made A&SP Reports \*\*Locked: ACKQ ADHOC\*\*
7.  PCE Exception Report
8.  Workload Report

### A&SP Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The A&SP Reports \[ACKQAS REPORTS\] menu contains only report options. This menu can be assigned to users who may not enter or modify any of the data, but need to be able to see the data generated by these reports.

- Visits by Diagnosis
- Patients by City
- Statistics by Procedure
- Cost Comparison Report
- Tailor-Made A&SP Reports \*\*Locked: ACKQ ADHOC\*\*
- PCE Exception Report
- Workload Report

## Key Assignment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Give the ACKQ ADHOC key to all users who will be creating/designing reports using the option Tailor-Made A&SP Reports. This option uses VA FileMan to sort and print data from the A&SP Clinic Visit (#509850.6) and A&SP Patient (#509850.2) files.

## Options for Implementing and Maintaining the Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Set Up/Maintenance Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Set Up/Maintenance menu \[ACKQAS SET UP MENU\] can be accessed by anyone assigned the A&SP Supervisor menu. It contains the options needed to implement the package and maintain or update the data used by the package.

- Staff (Enter/Edit) \[ACKQAS CLINICIAN ENTRY\]
- A&SP Site Parameters \[ACKQAS SITE PARAMS\]
- Enter Cost Information for Procedures \[ACKQAS COST ENTRY\] (Only A&SP staff designated as supervisors can access this option.)
- Update Files per CO Directive \[ACKQAS VACO DIRECTIVE\] (Only A&SP staff designated as supervisors can access this option.)
- Print A&SP File Entries \[ACKQAS FILE PRINT\]
- Update CPT Modifiers per CO Directive \[ACKQAS UPDATE CPT MODIFIERS\]

#### Staff (Enter/Edit)

\[ACKQAS CLINICIAN ENTRY\]

The Staff (Enter/Edit) option allows you to enter data for clinicians, fee-basis personnel, other providers (e.g., health technicians), and students into the A&SP STAFF file (#509850.3). The information includes the staff person’s name, activation and inactivation dates, status, an ID number for sites that choose to use code numbers, and whether or not the person is designated as a supervisor. Entering this option will automatically synchronize the A&SP STAFF file (#509850.3) member’s NAME with their NEW PERSON file (#200) NAME.

> **NOTE:** Staff members should never be deleted because entries in the A&SP Clinic Visit file (#509850.6) reference them. This option is used to activate and inactivate staff members as appropriate.

A&SP Staff Name: Names added to the A&SP STAFF file (#509850.3) must be in the New Person file (#200). The A&SP Service Chief should contact IRM if an entry needs to be made to the New Person file.

Status: Assign one of the following statuses to each staff member entry:

> S STUDENT

> C CLINICIAN

> F FEE BASIS CLINICIAN

> O OTHER PROVIDER

Activation Date: An activation date is required to associate the staff member with a clinic visit. The activation date is the date the staff member became an active member. For the staff member to receive credit for a patient visit, he or she must have been active on or before the visit date.

Inactivation Date: Enter a date when the staff member is no longer active.

ID Number: The ID Number field is used at stations that use code numbers in lieu of provider names. QUASAR provides a sequential default number starting with 0001, but any unique four digit number is accepted.

Supervisor: Selected clinicians can be designated as supervisors. Supervisors have access to certain functionality that is not available to other staff members (e.g., adequating any C&P exam).

#### A&SP Site Parameters

\[ACKQAS SITE PARAMS\]

The A&SP Site Parameters option allows you to enter data into the A&SP Site Parameters file (#509850.8). The parameters define how you want the program to run at your site and at each division within your site.

Site Name: Enter your station name or number. Only one entry is allowed in the A&SP Site Parameters file.

Interface with PCE: If you want QUASAR to send visit data to PCE, answer YES. If you check out patients via PCE and wish to continue to do so, answer NO. This parameter determines whether or not to activate the interface with PCE. If this parameter is set to NO, data will not be sent to PCE. If set to YES, visit data will be transmitted to PCE for each division that has its Send To PCE parameter also set to YES.

Division: Even if you are a single division site, enter that division here. This allows for workload crediting by division. At this point, you need to define all the following parameters for each Division using this program.

> Division Status: Enter ACTIVE. If the division should become inactive, change the status at that time to INACTIVE. No new visits can be added to an Inactive division.

> Send to PCE: If you want data for this division sent to PCE, the INTERFACE TO PCE parameter for the Site (see above) must be set to YES and you must also set this parameter (SEND TO PCE) for the division to YES. When a new visit is entered, or an existing visit is edited or deleted, the system looks at the SEND TO PCE parameter for the division to determine whether the visit data should be transmitted to PCE. A multi-divisional site has the choice of sending visit data to PCE for some divisions and not for others.

> Note: Data is transmitted to PCE as soon as you exit the record.

> PCE Interface Start Date: Enter the first Visit Date to be sent to PCE. QUASAR will only send Visits for this Division if the Visit Date falls on or after the PCE INTERFACE START DATE.

> If you enter the 1st of the next calendar month for instance, you may continue to enter, edit, or delete visits for the current calendar month and QUASAR will not transmit them to PCE. Once new Visits are entered for the new month they will automatically be transmitted to PCE.

> If you enter a date in the past, QUASAR will not automatically transmit visits that are already on file, even if their Visit Date is after the PCE INTERFACE START DATE. These visits will be reported on the PCE Exception Report and must be edited in QUASAR to initiate transfer to PCE.

> Update PCE Problem List: No//:[^1] This is a new field within the A&SP Site Parameters file (509850.8). This field can be edited.

> The default setting is No. If you answer with a No, there are no changes to the prompts that you will view. You will continue with the “Use ASP Clinic File Number” prompt. The PCE Problem list is not updated.

> If you answer with a Yes, a Diagnosis Code will be sent to PCE. This prompt occurs in the New Visit and Edit Visit options for each Diagnostic code that is entered, but only if the PCE Interface is active for the Division.

> If you select to update the PCE Problem List, you will be asked who the Diagnosis Provider was. Currently, when data is transferred to PCE, a PCE Encounter is created using the QUASAR visit data. However, if you answer Yes to the “Update the PCE Problem List” prompt, the system will also attempt to update the PCE Problem List with all selected Diagnosis Codes and their associated Providers.

> Use ASP Clinic File Number: For those sites that have existing LOCAL (not medical center) file numbers associated with their Audiology and Speech Pathology patients and wish to continue using these numbers, answer YES. By doing this, you can cross-reference QUASAR visit entries to your current file numbering system.

> Use C&P: Answer YES if you wish to use QUASAR’s AMIE/C&P interface. If you use a different reporting procedure and do not wish to use the AMIE/C&P interface, answer NO.

> If you answer YES to use the AMIE/C&P interface, staff involved must have an electronic signature. An electronic signature can be established using the Edit Electronic Signature Code option in the User’s Toolbox menu.

> The AMIE linkage feature allows:

- Entry of text and audiometric data in the AMIE format,
- Adequation of the results, and
- Hand-off of the report to the AMIE Compensation and Pension package.

> If this functionality is enabled, QUASAR checks to see if an audiology C&P exam is scheduled. When an entry is made for the patient, the user is asked “Is this a C&P exam?” If the user responds yes, in addition to the usual QUASAR information, narrative data is requested for generating the AMIE report.

> If the C&P exam prompt does not appear:

1.  The patient entered is not a C&P patient,
2.  Veterans Affairs Regional Office (VARO) did not request an AUDIO exam (see Form 2507),
3.  The patient’s C&P claim has been closed by the C&P Unit. Users should contact their C&P Unit.

> See Forcing the C&P Prompt for procedure to force the C&P prompt.

> Bypass Audiometrics: Certain diagnosis codes (i.e., hearing loss codes) are flagged to require audiometric data to be entered when those codes are used for a visit. By answering YES for the Bypass Audiometrics field, you allow users to bypass the entry of that data. If you answer NO, users are not allowed to bypass the entry of audiometric data.

> Event Capture Codes[^2]: Supervisors can set up a Division to use Event Capture Codes instead of the Procedure Codes (CPT) as a prompt to be displayed for the coming DSS extract period. In the Event Capture mode, answer “Yes” if you want the Division to use Event Capture Codes or “No” if you want this Division to use CPT codes.

> The Division can be set up with this option to change the mode in Site Parameters within a two-week window from September 17-30 each year. The last day to change the mode is September 30 at midnight. Supervisors can re-edit this field within this time period, but all values after September 30 will be final for the approaching Fiscal Year.

> When a mode has been changed to use the Event Capture Code field, an automatic MailMan message is sent to all active Supervisors within the Division.

> Clinic Location: The only clinics that may be entered for a division are clinics for Audiology (Stop Code 203), Speech Pathology (Stop Code 204), and Telephone/Rehab and Support (Stop Code 216) that reside in the Hospital Location file (#44) at your site. There must be at least one clinic entered for this field.

Audiology DSS Unit Link and Speech Pathology DSS Unit Link: The last two fields are pointers to the DSS Unit file (#724) from Event Capture. These fields create linkage between QUASAR and a specific DSS unit in order to define data needed by the QUASAR/DSS extract. Enter the DSS units for these links.

> **NOTE:** These are not division specific.

#### Enter Cost Information for Procedures

\[ACKQAS COST ENTRY\]

The Enter Cost Information for Procedures option allows you to enter cost data for each procedure code in the A&SP Procedure Code file (#509850.4). You can select a single CPT-4 code, or you can edit all procedure codes. If you choose to edit all procedures, each procedure is displayed consecutively, and the current approximate private sector cost can be entered. You can obtain fee schedules from public or private sector clinics and hospitals, calculate their real costs, or use insurance reimbursement rates (e.g., Medicare/Medicaid or insurance UCRs).

Procedure cost information is used in generating the Cost Comparison Report on the A&SP Reports menu.

#### Update Files per CO Directive

\[ACKQAS VACO DIRECTIVE\]

> **NOTE:** In order to use this option, you must be designated as an active supervisor in the A&SP Staff file (#509850.3). Use the Staff (Enter/Edit) option to make this designation.

The Update Files per CO Directive option is to be used with extreme caution. Data in the CDR Account file (#509850), the A&SP Diagnostic Condition file (#509850.1), and the A&SP Procedure Code file (#509850.4) are standardized for roll-up to central data bases (e.g., DSS). File entries should be added or modified ONLY by directive from the Director, Audiology and Speech Pathology Service (VAHQ).

After selecting the file you wish to edit, you can choose to inactivate selected entries or add data for a new entry. When a new entry is added, all fields for that entry must be answered in order to maintain database integrity. If data is incomplete, the entry is automatically deleted.

#### Print A&SP File Entries (Procedure Code List)

\[ACKQAS FILE PRINT\]

The Print A&SP File Entries option lists the file entries from the CDR Account file, the A&SP Procedure Code file, or the A&SP Diagnostic Condition file. Select the file you want to print and enter a printer name.

  
Example

A&SP PROCEDURE CODE LIST OCT 14,1999 09:53 PAGE 1

CODE PROCEDURE COST ACTIVE

MODIFIER

DESCRIPTION COST

---------------------------------------------------------------------------------------------------------------------------------------

NNNNN PROCEDURE \$\$.00 ACTIVE

NNNNN PROCEDURE \$\$.00 INACTIVE

...

#### Print A&SP Diagnostic Condition List

\[ACKQAS FILE PRINT\]

Example

A&SP DIAGNOSTIC CONDITION LIST JUL 24,2012 10:29 PAGE 1

ICD-9

CODE DIAGNOSIS ACTIVE

DESCRIPTION

-----------------------------------------------------------------------------

141.9 MALIG NEO TONGUE NOS ACTIVE

306.1 PSYCHOGENIC RESPIR DIS INACTIVE

306.9 PSYCHOGENIC DISORDER NOS ACTIVE

307.9 SPECIAL SYMPTOM NEC/NOS ACTIVE

OTHER/UNSPECIFIED SPEECH PROBLEM

WITHIN NORMAL & FUNCTIONAL LIMITS

315.02 DEVELOPMENTAL DYSLEXIA ACTIVE

315.31 EXPRESSIVE LANGUAGE DIS ACTIVE

369.4 LEGAL BLINDNESS-USA DEF ACTIVE

380.4 IMPACTED CERUMEN ACTIVE

381.7 PATULOUS EUSTACHIAN TUBE ACTIVE

385.23 DISLOCATION EAR OSSICLE ACTIVE

386.11 BENIGN PARXYSMAL VERTIGO ACTIVE

386.2 CENTRAL ORIGIN VERTIGO ACTIVE

….

A&SP DIAGNOSTIC CONDITION LIST JUL 24,2012 10:31 PAGE 1

ICD-10

CODE DIAGNOSIS ACTIVE

DESCRIPTION

-----------------------------------------------------------------------------

S01.301A Unspecified open wound of right ear, initial encounter ACTIVE

F07.0 Personality change due to known physiological ACTIVE

F07.81 Postconcussional syndrome ACTIVE

F07.89 Oth personality & behavrl disord due to known ACTIVE

F80.1 Expressive language disorder ACTIVE

F80.2 Mixed receptive-expressive language disorder ACTIVE

F80.4 Speech and language development delay due to h ACTIVE

F80.9 Developmental disorder of speech and language, ACTIVE

F81.0 Specific reading disorder ACTIVE

F81.2 Mathematics disorder ACTIVE

F81.81 Disorder of written expression ACTIVE

F81.89 Other developmental disorders of scholastic sk ACTIVE

F81.9 Developmental disorder of scholastic skills, u ACTIVE

F98.5 Adult onset fluency disorder ACTIVE

G31.84 Mild cognitive impairment, so stated ACTIVE

#### #### Update CPT Modifiers per CO Directive

\[ACKQAS UPDATE CPT MODIFIERS\]

This option allows you to select any modifier already defined in the A&SP Procedure Modifier file (#509850.5) and either activate or inactivate it. The option also allows you to add active CPT or HCPCS modifiers from the CPT Modifier file (#81.3) to the A&SP Procedure Modifier file. Modifiers cannot be deleted from the A&SP Modifier file; a modifier is removed from user selection lists by setting the status of the modifier to Inactive.

The following modifiers were exported with this release:

22 UNUSUAL PROCEDURAL SERVICES

26 PROFESSIONAL COMPONENT

50 BILATERAL PROCEDURE

51 MULTIPLE PROCEDURES

52 REDUCED SERVICES

53 DISCONTINUED PROCEDURE

59 DISTINCT PROCEDURAL SERVICE

76 REPEAT PROCEDURE BY SAME PHYSICIAN

77 REPEAT PROCEDURE BY ANOTHER PHYSICIAN

99 MULTIPLE MODIFIERS

TC TECHNICAL COMPONENT

# Entering and Viewing Clinic Visit Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main function of the package is to add visit information to the program. This is done using options from the Audiology & Speech Visit Tracking System menu. Visit data can be viewed using the A&SP Reports menu.

## Audiology & Speech Visit Tracking System 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS MASTER\]

- New Clinic Visits \[ACKQAS VISIT ENTRY\]
- Edit an Existing Visit \[ACKQAS VISIT EDIT\]
- Inquire - A&SP Patient \[ACKQAS PAT INQ\]
- A&SP Reports \[ACKQAS REPORTS\]
1.  Visits by Diagnosis \[ACKQAS VISITS BY DIAG\]
9.  Patients by City \[ACKQAS PAT BY CITY\]
10. Statistics by Procedure \[ACKQAS PROC STATS\]
11. Cost Comparison Report \[ACKQAS PRINT COST COMPARE\]
12. Tailor-Made A&SP Reports \[ACKQAS ADHOC\]
13. PCE Exception Report \[ACKQAS PCE EXCEPTION REPORT\]
14. Workload Report \[SDCLINIC WORKLOAD\]

### Appointment Management and PCE Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### How Does It Work?

After entering the clinic, date and patient name in the New Clinic Visits option, the program searches Appointment Management, QUASAR, and PCE to see if there is already a visit/appointment on file. The following discusses how the program works under different circumstances (no existing QUASAR visits as opposed to existing visits). This discussion assumes PCE is active.

#### No Existing QUASAR Visits

The following assumes there are no existing visits in QUASAR for the clinic, date, and patient entered.

1.  First, QUASAR checks for matching appointments in Appointment Management. If there are none, the program drops immediately to the Patient Inquiry screen and you may add new visit data.

> **NOTE:** Sites are strongly warned not to enter encounter data for appointments that do not exist in Appointment Management. If a patient presents to the clinic without a scheduled appointment (walk-ins), the patient MUST be entered into Appointment Management in accordance with the facility's policy prior to entering encounter data for the patient into QUASAR.

> If Appointment Management is not used and a visit is added in QUASAR, it will not appear in Appointment Management, although it will exist in PCE. The data will transmit to the NPCDB. However, if there is a problem with the data, the clinic will not know that the encounter is in ACTION REQUIRED status. An incomplete encounter warning will come back to MAS, but they will not be able to find the offending encounter since it does not appear in Appointment Management. This is not strictly a QUASAR problem. Any appointment generated outside Appointment Management (e.g., CPRS, ECS) will not appear in Appointment Management.

2.  If there are existing appointments in Appointment Management, then they are displayed.

> Example

\- APPOINTMENT LIST -

Name : QUASARPATIENT,ONE SSN : 000-00-0001

Date : 11/03/99 Clinic : AUDIOLOGY

Appt Date/Time Status Appointment Type

1\. NOV 3,1999 08:00 NO ACTION TAKEN REGULAR

Select Appointment (1-1) or (N)ew Visit : 1//

1.  If you select an existing appointment, then you are returned to QUASAR and shown the Patient Inquiry screen. You may begin entering visit data. The Appointment Time will be the same as that in Appointment Management and it is not editable in QUASAR.
15. If you select New Visit, a warning message displays.

> Example

WARNING -

You are Creating a Visit that does not exist within Appointment Management.

This Visit will not be displayed within Appointment Management.

Do you want to Continue ? NO//

> **NOTE:** Data should NOT be entered into QUASAR without having an appointment in the Appointment Management package. If, however, you should still elect to continue, you must enter a time different from that in Appointment Management.

#### Existing QUASAR Visits

Regardless of whether or not the appointment is already in Appointment Management, if there is an existing QUASAR visit for the clinic, date, and patient entered, the program displays that QUASAR visit for selection first.

> Example

One visit has already been entered for this date and patient.

1\. NOV 19, 1999 9:35 AM AUDIOLOGY

Is the appointment shown here the one you wish to edit? No//

1.  If the existing QUASAR visit is selected, then you are dropped immediately to the Patient Inquiry screen and may edit the existing visit data.
3.  If the existing QUASAR visit is not selected, then you are shown any existing encounters in PCE which should include the visit already displayed from the QUASAR package and any others that may have been added to PCE through the Scheduling package.

    Example

Ok, adding another visit for this patient/date.

No. DATE TIME HOSPITAL LOCATION CATEGORY UNIQUE I D

END OF LIST

PAT/SEX/AGE/SSN: QUASARPATIENT,ONE MALE 86 Years 000-00-0001

ENCOUNTERS: ...Select an ENCOUNTER .....

\- - 1 E N C O U N T E R S - -

No. DATE TIME HOSPITAL LOCATION CATEGORY UNIQUE I D

1 NOV 19, 1999 09:35 AUDIOLOGY PRIMARY 14GG-TEST

2 NOV 19, 1999 07:00 AUDIOLOGY PRIMARY 14CW-TEST

END OF LIST

'RETURN' to continue or '-' for previous screen

Select ITEM No. or 'A' to ADD an Encounter:

> You may select one of these encounters, add a new encounter, or press the \<ret\> key.

1.  If an encounter is selected from this screen that is not already in QUASAR, then QUASAR will copy the Visit Time Eligibility data and all Diagnosis, Procedure and Provider information from PCE and you will be presented with the Patient Inquiry screen. If you select the same visit that is already in QUASAR, then you will receive an Error message.

> Example

ERROR - A visit already exists in QUASAR with the following details.

Visit Date: NOV 19, 1999 Appointment Time: 9:35 AM

Clinic: AUDIOLOGY

Patient: QUASARPATIENT,TWO

If you choose to continue you must enter a different Appointment Time.

> **NOTE:** QUASAR will not allow two visits for the same Patient and Clinic to have the exact same date and time. Also, since duplicate entry of workload data will affect the Capitation Statistics, DSS Extract, and ACRP Workload Reports, it is important that the same visit is not entered twice.

16. If you elect to ADD an Encounter and there are no existing appointments, you get a warning message.

Example

WARNING –

You are Creating a Visit that does not exist within Appointment Management.

This Visit will not be displayed within Appointment Management.

Do you want to Continue ? NO//

17. If you press the \<ret\> key and there are appointments in Appointment Management, then you get one last chance to select an appointment in Appointment Management.

> Example

– APPOINTMENT LIST –

Name : QUASARPATIENT,ONE SSN : 000-00-0001

Date : 11/19/99 Clinic : AUDIOLOGY

Appt Date/Time Status Appointment Type

1\. NOV 19,1999 07:00 NO ACTION TAKEN REGULAR

2\. NOV 19,1999 09:35 NO ACTION TAKEN REGULAR

Select Appointment (1-2) or (N)ew Visit : 1//

4.  If you do not select an existing QUASAR visit, PCE encounter, or Appointment or add a new encounter, then you are returned to the beginning of the option.

### Avoiding Mismatches between QUASAR and PCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### When is PCE Interface Active?

The PCE Interface is considered Active for the current Visit if all the following are true:

- The PCE Interface parameter for the Site is set to YES.
- The Send to PCE parameter for the Division is set to YES.
- The Visit Date falls on or after the PCE Interface Start Date for the Division.

> **NOTE:** If data is entered or edited in QUASAR for a date which is PRIOR to the PCE INTERFACE START DATE initially set in the site parameters, data mismatches will be reported in the PCE exception report.

#### Preferred Workflow

The general workflow should be from Appointment Management to QUASAR to PCE and back to Appointment Management to check out the appointment. If this workflow pattern is followed, you will have few or no instances of mismatched data between PCE and QUASAR.

![](quasar-version-3-user-manual-updated-ackq-3-21/002.png)

### Data Mismatch between PCE and QUASAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Any data entered into QUASAR is automatically transmitted to PCE when the interface is Active; data entered first into QUASAR assumes the same data in PCE.

If there is mismatched data:

- The data in PCE was entered before that in QUASAR through Scheduling or Progress Notes.
- The data was altered in PCE following transmission of the data from QUASAR.
- The PCE interface was not active when the visit was entered into QUASAR and different values were entered into QUASAR and PCE.

If there is a mismatch, the fields with mismatches are displayed whenever you select a record to edit. The mismatch check is done on the Clinic Location, Visit Date, Appointment Time, and Patient Name fields. If there is a mismatch, only the mismatched fields display.

Example

The following fields within the PCE Visit entry linked to this Quasar visit no longer match.

CLINIC LOCATION

PATIENT

VISIT DATE

Due to this mismatch the link between this Quasar visit and the PCE visit will be broken.

> **NOTE:** You should routinely run the PCE Exception Report and correct any problems found.

### New Clinic Visits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS VISIT ENTRY\]

The New Clinic Visits option allows you to enter A&SP clinic visits into the computer.

#### Required Data

When entering a new visit, if all required information is not typed in, the entire visit is deleted. This is done to eliminate errors caused by incomplete data. Each of the following six fields must contain data for the visit to be filed in QUASAR:

|                |                      |
|----------------|----------------------|
| 1\. DIVISION   | 4\. PATIENT NAME     |
| 2\. CLINIC     | 5\. APPOINTMENT TIME |
| 3\. VISIT DATE | 6\. CDR ACCOUNT      |

If all the above are present, the program checks for data in the following additional fields that are considered required but do not prevent the visit from being filed in QUASAR.

If the PCE interface is not active for the visit:

|                       |               |                      |
|-----------------------|---------------|----------------------|
| 7\. PRIMARY DIAGNOSIS | 8\. PROCEDURE | 9\. PRIMARY PROVIDER |

If the PCE interface is active for the visit:

|                         |                                     |                        |
|-------------------------|-------------------------------------|------------------------|
| 7\. VISIT ELIGIBILITY   | 10\. RADIATION EXPOSURE\*\*         | 12\. PRIMARY DIAGNOSIS |
| 8\. SERVICE CONNECTED\* | 11\. ENVIRONMENTAL CONTAMINANTS\*\* | 13\. PRIMARY PROVIDER  |
| 9\. AGENT ORANGE\*\*    |                                     | 14\. PROCEDURE         |

\* field required only if it applies to the Patient

\*\* field required only if it applies to the Patient and the Visit is NOT Service Connected

The following prompts may or may not appear depending on the patient and the way the site parameters are defined:

Division: If this is a multi-divisional site and there is more than one Active Division defined in the A&SP Site Parameters, select the Division associated with the visit. If there is only one active Division, you will not see this prompt.

Clinic: If there is more than one Clinic location for the Division, identify the Clinic location for this visit.

Visit Date: Enter the visit date. QUASAR defaults to today’s date and will accept any date format except a future date.

Patient Name: Enter the patient’s name. If a new name is entered (i.e., a name not previously in the A&SP Patient file (#509850.2)), QUASAR asks if you want to add the new patient to the file.

> Once you select a clinic, date, and patient, the program searches QUASAR, Appointment Management, and PCE for existing visits/appointments.

> **NOTE:** For more information, refer to [*Appointment Management and PCE Interfaces*](#appointment-management-and-pce-interfaces) on page [13](#appointment-management-and-pce-interfaces).

> \[Display of patient details\]

> Next, the system displays a Patient Inquiry summary/screen of the Patient you selected. The display includes the Division and Clinic selected for this visit, the Patient Name, Date of Birth, Social Security Number, Eligibility, and Initial Visit Date. If the patient is currently an Inpatient, the patient's ward, room and treating specialty also display.

> <span id="p21_19" class="anchor"></span>Example

D ^XUP

Setting up programmer environment

This is a TEST account.

Access Code: \*\*\*\*\*\*\*\*\*

Terminal Type set to: C-VT100

Select OPTION NAME: ACKQAS VI

     1   ACKQAS VISIT EDIT       Edit an Existing Visit

     2   ACKQAS VISIT ENTRY       New Clinic Visits

     3   ACKQAS VISITS BY DIAG       Visits by Diagnosis

CHOOSE 1-3: 1  ACKQAS VISIT EDIT     Edit an Existing Visit

Edit an Existing Visit

This option is used to modify an existing clinic visit when the data is

incorrect, incomplete, or needs to be updated.

Select A&SP CLINIC VISIT DATE: ??

   

   Choose from:

   JAN 26, 2012     9:00 AM. xxxxxxxxxxxxxxxxxxxx      SPEECH PATH - CHRISTY   

   MAR 13, 2012     8:00 AM. xxxxxxxxxxxxxxxxxxxxxx    SPEECH PATH - CHRISTY   

   MAR 27, 2012    12:00 AM                            SPEECH PATH - CHRISTY   

   APR 18, 2012     8:20 AM  xxxxxxxxxxxxxxxxxxxx      SPEECH PATH - CHRISTY   

   MAY 11, 2012    12:00 AM                            SPEECH PATH - CHRISTY   

   MAY 11, 2012     8:00 AM                            SPEECH PATH - CHRISTY   

   MAY 11, 2012     8:00 AM                            SPEECH PATH - CHRISTY   

   MAY 11, 2012     8:00 AM. xxxxxxxxxxxxxxxxxxxxxx    SPEECH PATH - CHRISTY   

   MAY 11, 2012    10:00 AM. xxxxxxxxxxxxxxxxxxxxxx    SPEECH PATH - CHRISTY   

   MAY 11, 2012    12:30 PM. xxxxxxxxxxxxxxxxxxxxxx    SPEECH PATH - CHRISTY   

   MAY 11, 2012     8:00 AM  xxxxxxxxxxx               SPEECH PATH - CHRISTY   

   MAY 11, 2012     4:00 PM  xxxxxxxxxxx               SPEECH PATH - CHRISTY   

   MAY 11, 2012     4:30 PM. xxxxxxxxxxx               SPEECH PATH - CHRISTY   

   MAY 15, 2012     9:00 AM. xxxxxxxxxxxxxxxxxxxxxx    SPEECH PATH - CHRISTY   

   MAY 21, 2012    10:00 AM. xxxxxxxxxxxxx             QUASAR                  

   AUG 01, 2012     8:00 AM. xxxxxxxxxxxxx             SPEECH PATH - CHRISTY   

   AUG 07, 2012     9:00 AM. xxxxxxxxxxxxxxxxxxxxxx    QUASAR                  

   AUG 10, 2012     9:00 AM. xxxxxxxxxxxxxxxxxxxxxx    SPEECH PATH - CHRISTY   

   MAY 29, 2014     8:00 AM. xxxxxxxxxxxxxxxxxxxxxxx   QUASAR                   

                

Select A&SP CLINIC VISIT DATE: 5 29 14   MAY 29, 2014    8:00 AM. xxxxxxxxxxx

DATE: MAY 29, 2014//

                          QUASAR V.3.  EDIT VISIT ENTRY

CLINIC: QUASAR                               DIVISION: NASHVILLE

PATIENT: xxxxxxxxxxxxxxxxx              DOB: xxxxxxxxxx   SSN: xxx-xx-xxxx

ELIGIBILITY: NSC                             INITIAL VISIT DATE: 03/13/12

Patient is not currently an inpatient.

Patient Diagnostic History

Mr. xxxxxxxxxxxxxxxxx has been seen for the following:

                                                                        DATE

DIAGNOSIS                                                               ENTERED

-------------------------------------------------------------------------------

ICD-9-CM

141.9     MALIG NEO TONGUE NOS                                         03/13/12

306.9     PSYCHOGENIC DISORDER NOS                                     03/13/12

307.9     SPECIAL SYMPTOM NEC/NOS                                      03/13/12

315.02    DEVELOPMENTAL DYSLEXIA                                       03/13/12

315.31    EXPRESSIVE LANGUAGE DIS                                      03/13/12

380.4     IMPACTED CERUMEN                                             03/13/12

381.7     PATULOUS EUSTACHIAN TUBE                                     03/13/12

386.2     CENTRAL ORIGIN VERTIGO                                       03/13/12

386.54    HYPOACT LABYRINTH BILAT                                      05/11/12

386.56    LOSS LABYRIN REACT BILAT                                     05/11/12

387.9     OTOSCLEROSIS NOS                                             05/11/12

388.01    PRESBYACUSIS                                                 03/13/12

388.11    ACOUSTIC TRAUMA                                              05/15/12

388.12    HEARING LOSS D/T NOISE                                       08/07/12

388.2     SUDDEN HEARING LOSS NOS                                      03/13/12

388.9     DISORDER OF EAR NOS                                          03/13/12

519.9     RESP SYSTEM DISEASE NOS                                      03/13/12

804.45    CL SKUL/OTH FX-DEEP COMA                                     08/10/12

290.0     SENILE DEMENTIA UNCOMP                                       08/10/12

291.0     DELIRIUM TREMENS                                             08/10/12

292.0     DRUG WITHDRAWAL                                              03/13/12

293.0     DELIRIUM D/T OTHER COND                                      03/13/12

307.0     ADULT ONSET FLNCY DISORD                                     08/10/12

388.30    TINNITUS NOS                                                 03/13/12

388.70    OTALGIA NOS                                                  08/07/12

783.0     ANOREXIA                                                     03/13/12

784.60    SYMBOLIC DYSFUNCTION NOS                                     02/27/13

V41.2     PROBLEMS WITH HEARING                                        05/11/12

V41.4     VOICE PRODUCTION PROBLEM                                     03/13/12

V41.6     PROBLEM W SWALLOWING                                         03/13/12

V52.8     FITTING PROSTHESIS NEC                                       03/13/12

ICD-10-CM

F80.9     DEVELOPMENTAL DISORDER OF SPEECH AND LANGUAGE,               10/01/15

          UNSPECIFIED

F81.0     SPECIFIC READING DISORDER                                    10/01/15

H60.331   SWIMMER'S EAR, RIGHT EAR                                     10/01/15

H60.332   SWIMMER'S EAR, LEFT EAR                                      10/01/15

H60.339   SWIMMER'S EAR, UNSPECIFIED EAR                               10/19/15

H61.312   ACQUIRED STENOSIS OF L EXT EAR CANAL SECONDARY TO TRAUMA     10/30/15

H90.71    MIX CNDCT/SNRL HEAR LOSS,UNI,R EAR,W UNRESTR HEAR CNTRA      10/30/15

          SIDE

H91.01    OTOTOXIC HEARING LOSS, RIGHT EAR                             11/08/15

I69.023   FLUENCY DISORDER FOLLOWING NTRM SUBARACHNOID HEMORRHAGE      11/07/15

J38.3     OTHER DISEASES OF VOCAL CORDS                                11/18/15

S01.339D  PUNCTURE WOUND WITHOUT FOREIGN BODY OF UNSP EAR, SUBS        11/30/15

          ENCNTR

Z82.2     FAMILY HISTORY OF DEAFNESS AND HEARING LOSS                  11/30/15

> If there have been previous visits, the patient's A&SP problem list will also be displayed.

Appointment Time: You are asked for an Appointment Time if an appointment or PCE visit was not selected or if there is a mismatch in appointment times between PCE and QUASAR. If this is the first recorded visit for the patient, you are also asked to enter the Initial Visit Date.

If the Use ASP Clinic File Number site parameter is set to YES, you will get the following prompt next:

> ASP File Number: Enter the patient’s ASP File Number or press the \<ret\> key to accept the default.

If you are using QUASAR’s AMIE/C&P interface and an Audiology C&P exam is scheduled through AMIE for the patient, the following appears:

> Is this a C&P Visit?: Answer YES to this prompt to link the QUASAR clinic visit to the appropriate AMIE entry.

> If the C&P exam prompt does not appear:

- The patient entered is not a C&P patient.
- Veterans Affairs Regional Office (VARO) did not request an AUDIO exam (see Form 2507).
- The patient’s C&P claim has been closed by the C&P Unit. Contact your C&P Unit if necessary.

> It is permissible to force the "Is this a C&P exam?" prompt and there are occasions when this is acceptable. To force the C&P prompt, enter "^C AND P" after the patient identifying information (e.g., at the "Select DIAGNOSTIC CODE:" prompt). A facility not using the AMIE/C&P interface might force the prompt to keep an accurate count of C&P exams. A facility using the AMIE/C&P interface might force the prompt in order to produce the C&P report for an allied war veteran with a C&P appointment. The allied war veteran’s report would be signed manually, because only C&P exams requested through VARO can be adequated through QUASAR.

Diagnostic Code: Enter a diagnostic code (<span id="p21_21" class="anchor"></span>ICD code).

> Evaluations: The disease codes are those conditions found to exist after evaluation or are determined to exist based on observation or case history. Previously noted conditions are not listed unless they are relevant to the management of the patient.

> Treatment and Therapy Visits: The disease codes are those conditions which are treated. Conditions previously noted to exist but are not relevant to the management of the patient or are not treated during the visit are not entered. Disease codes are added to the A&SP problem list for the patient.

> **NOTE:** To see a list of previously entered diagnostic codes, enter a ? at the "Select DIAGNOSTIC CODE:" prompt.

> Is this the Primary Diagnosis ?: YES: This prompt appears until one of the Diagnostic Codes entered is designated as the Primary Diagnosis. If you don't define a Primary Diagnosis, the program will remind you and send you back to designate one as the primary.

> Update PCE Problem List with Diag. Code?:[^3] This is a new conditional field within the New Visit option. This prompt displays only when you answer Yes to the “Update PCE Problem List?” prompt. This prompt exists for the Diagnosis Provider prompt, which displays after this prompt.

> Diagnosis Provider:[^4] If you select to update the PCE Problem List, you will be asked who the Diagnosis Provider was. For each diagnosis added, you will need to add a Provider. The valid providers are also the same providers as on the “Secondary Provider” prompt.

> Currently, when data is transferred to PCE, a PCE Encounter is created using the QUASAR visit data. However, if you answer Yes to the “Update the PCE Problem List” prompt, the system will also attempt to update the PCE Problem List with all selected Diagnosis Codes and their associated Providers.

Eligibility for this Appointment: This prompt only appears if the patient is Service Connected. The classification is displayed and you are asked to select the eligibility for the appointment. NSC is always a possible selection because the eligibility for the appointment might not be covered by the patient's service classification.

> Example

Service Classifications

SERVICE-CONNECTED

This Patient has other Entitled Eligibilities

NSC NON-SERVICE CONNECTED

PRISONER OF WAR PRISONER OF WAR

Enter the Eligibility for this Appointment: SERVICE CONNECTED 50% to 100%

// ??

Only Eligibilities associated with the visit are valid for entry.

Choose from:

NSC

PRISONER OF WAR

SERVICE CONNECTED 50% to 100%

Enter the Eligibility for this Appointment: SERVICE CONNECTED 50% to 100%

//

> If the patient is Service Connected and has been exposed to Agent Orange, Environmental Contaminants, and/or Radiation, then the service connection and all exposures are listed and you are asked to enter the eligibility for the appointment.

> Example

Service Classifications

SERVICE-CONNECTED AGENT-ORANGE

This Patient has other Entitled Eligibilities

NSC NON-SERVICE CONNECTED

PRISONER OF WAR PRISONER OF WAR

Enter the Eligibility for this Appointment: SERVICE CONNECTED 50% to 100%

//

Was the Care for a SC Condition?: If the patient is Service Connected, this prompt also appears. Indicate here whether or not the visit is Service Connected.

The next prompt, "Was care related to ... Exposure", only appears:

- If you answer NO at the "Was the Care for a SC Condition?" prompt, and the patient has been exposed to Agent Orange, Radiation or Environmental Contaminants, or
- If the patient is not service connected but has been exposed to Agent Orange, Radiation, or Environmental Contaminants.

Was care related to ... Exposure: If the patient is not Service Connected but has been exposed to Agent Orange, Environmental Contaminants, and/or Radiation, then the classification is not displayed but you are asked to designate whether or not the care given during the visit was related to the exposure(s). This prompt does not appear if:

- The patient is Service Connected
- The patient is not service connected and has not been exposed to Agent Orange, Environmental Contaminants, or Radiation.

  Was care related to Head and/or Neck Cancer ?: This prompt indicates whether the patient’s visit was related to Head and/or Neck Cancer. This prompt will only appear if the patient is classified with Environment Factors: (4) N/T Radium (VERIFIED).

  Was care related to COMBAT ?: This prompt indicates whether the patient’s visit was related to Combat. This prompt will only appear if the patient is classified with combat related information.

Was care related to MST?[^5] This prompt indicates whether the patient’s visit was related to Military Sexual Trauma. This prompt displays because the patient is registered on the MST file and the QUASAR Visit Date falls after the MST Active date.

> If the Division is set up in Site Parameters to transmit data to PCE, and the above conditions exist and the answer of Yes or No to this prompt is included in the data that gets sent to PCE.

> If the Division is not set up in Site Parameters to transmit data to PCE, then this prompt will not display.

CDR Account: QUASAR determines the CDR cost account. The program checks for inpatient/outpatient status and treating specialty to determine the CDR cost account. All outpatient workload is distributed to CDR account 2611.00 (Rehabilitative and Supportive Services). If the CDR account presented is correct, accept the default answer by pressing the return key (\<RET\>).

> Audiometric Scores and the associated word processing fields (Review of Medical Records, Medical History, Physical Examination, Diagnostic and Clinical Tests, and Diagnosis) only appear when entering C&P Exam data. At least one of the diagnostic codes entered for the visit must be related to hearing loss.

<span id="ICDp23" class="anchor"></span>Note: CDR and audiometric fields in VistA QUASAR are obsolete. CDR is no longer used and the audiometric functionality was replaced by GUI QUASAR (audiometric module).

Audiometric Scores: The program displays the patient's previous audiometric scores if either of the following conditions is true:

- The visit is a C&P Exam and the patient has previous audiometric scores.
- At least one of the diagnostic codes entered for the visit is defined as being Hearing Loss, the Bypass Audiometric site parameter is set to NO for the division, and the patient has previous audiometric scores.

> If one of the above conditions is met, the program displays the patient's previous scores and asks if you want to use those scores. If not, prompts appear for audiometric thresholds and word recognition scores. Enter a whole number between -10 and 105. No response at the limits of the audiometer is coded as 105.

> **NOTE:** The A&SP Program Office prohibits presentation of audiometric stimuli exceeding 105 dB HL.

> Audiometric scores are required if one of the following conditions is met:

- The visit is a C&P exam and the patient does not have previous scores.
- The visit is a C&P exam and the patient has previous scores but you have chosen not to use them.
- One or more of the diagnosis codes for the visit is defined as constituting hearing loss, the Bypass Audiometric site parameter for the division is set to NO, and the patient does not have previous scores.
- One or more of the diagnosis codes for the visits is defined as constituting hearing Loss, the Bypass Audiometric site parameter for the division is set to NO, the patient has previous scores, but you have chosen not to use them.

> Review of Medical Records: Indicate whether the C-file was reviewed. You should state that the C-file was not reviewed or was not available for review.

Medical History: Comment on:

1.  Chief complaint.
2.  Situation of greatest difficulty.
3.  Pertinent service history.
4.  History of military, occupational, and recreational noise exposure.
5.  Tinnitus - If present, state:
1.  Date and circumstances of onset.
2.  Whether it is unilateral or bilateral.
3.  Whether it is recurrent (indicate frequency and duration).
4.  The most likely etiology of the tinnitus, and specifically, if hearing loss is present, whether the tinnitus is due to the same etiology (or causative factor) as the hearing loss.

> Physical Examination: Enter the Objective Findings.

1.  Measure pure tone thresholds in decibels at the indicated frequencies (air conduction):

==========RIGHT EAR=============================LEFT EAR==============

A\* B C D E \*\* A\* B C D E \*\*

500 1000 2000 3000 4000 average 500 1000 2000 3000 4000 average

\* The pure tone threshold at 500 Hz is not used in determining the  
evaluation but is used in determining whether or not a ratable  
hearing loss exists.

\*\* The average of B, C, D, and E.

2.  Speech Recognition Score:

    Maryland CNC word list \_\_\_\_\_\_% right ear \_\_\_\_\_% left ear
3.  When only pure tone results should be used to evaluate hearing loss, the examiner, who must be a state-licensed audiologist, should certify that language difficulties or other problems (specify what the problems are) make the combined use of pure tone average and speech discrimination inappropriate.

> Diagnostic and Clinical Tests:

1.  Report middle-ear status, confirm type of loss, and indicate need for medical follow-up. In cases where there is poor inter-test reliability and/or positive Stenger test results, obtain and report estimates of hearing thresholds using a combination of behavioral testing, Stenger interference levels, and electrophysiological tests.
4.  Include results of all diagnostic and clinical tests conducted in the examination report.

> Diagnosis:

1.  Summary of audiologic test results. Indicate type and degree of hearing loss for the frequency range from 500 to 4000 Hz. For type of loss, indicate whether it is normal, conductive, sensorineural, central, or mixed. For degree, indicate whether it is mild (26-40 dB HL), moderate (41-54 dB HL), moderately-severe (55-69 dB HL), severe (70-89 dB HL), or profound (90+ dB HL). For VA purposes, impaired hearing is considered to be a disability when the auditory threshold in any of the frequencies 500, 1000, 2000, 3000, and 4000 Hz is 40 dB HL or greater; or when the auditory thresholds for at least three of these frequencies are 26 dB HL or greater; or when speech recognition scores are less than 94%.
5.  Note whether, based on audiologic results, medical follow-up is needed for an ear or hearing problem, and whether there is a problem that, if treated, might cause a change in hearing threshold levels.

Primary Provider, Secondary Provider, Student: Next, you are prompted for Primary Provider, Secondary Provider, and Student.

1.  The Primary Provider field is required and contains the name of the primary A&SP clinician who participated in the exam.
6.  You may enter more than one Secondary Provider. This is the same as a Diagnosis Provider prompt. If more than one provider was involved in the exam, the name(s) of the Secondary Provider should be entered here. In order to enter a provider in this field, the provider must already exist in the A&SP Staff file (#509850.3) and the Activation Date and the Inactivation Date must indicate that the selected provider is active on the date of the exam. This field can also be left blank.
7.  You can only select providers and students who are active on the exam visit date.

> Event Capture Codes:[^6] Conditional prompt that displays only if Event Capture Codes was set up in Site Parameters for a Division. You can enter Event Capture Codes instead of the Procedure Codes (CPT) for the Division at this prompt. A list will display for you to select an Event Capture Code. Multiple entries can be made.

> Volume:[^7] Conditional prompt that displays only if Event Capture Codes was set up in the Site Parameters for the Division. This prompt denotes the number of times that the procedure was performed with the visit.

> EC Procedure Provider:[^8] Conditional prompt that displays only if Event Capture Codes was set up in the Site Parameters for the Division. You can select a provider/clinician that performed the procedure at this prompt. The selection defaults to the same person as the “Primary Provider” if they were selected for the Encounter. It is also the same person as the CPT Procedure Provider and Diagnosis Provider.

Procedure Code: Enter all applicable procedure codes (CPT-4 codes).

> **NOTE:** There are times when the same procedure is done more than once during a visit. In that case, enter the procedure once and at the next Procedure Code prompt, enter the same procedure in quotes.

Example

Select PROCEDURE CODE: 92565 \<RET\> STENGER TEST, PURE TONE

Select CPT MODIFIER: \<RET\>

VOLUME: 1// \<RET\>

PROCEDURE PROVIDER: QUASARPROVIDER1,SIX// \<RET\> JS

Select PROCEDURE CODE: "92565" \<RET\> STENGER TEST, PURE TONE

> [^9]If a Supervisor answers “No” to the Event Capture Code prompt for a Division, then the Procedure Codes (CPT) prompt will be displayed instead of the Event Capture Codes. This prompt contains CPT procedure codes for this exam. QUASAR accepts multiple CPT-4 codes to be entered more than once if the second and subsequent codes are enclosed in quotation marks (e.g., “92507”). If this is not done, QUASAR assumes that the entry is a mistake and displays the entered code followed by double slant bars (e.g., 92507//). This is a signal that this code has already been entered for this visit.

> CPT Modifier: You are prompted for modifiers when a modifiable CPT code is entered. Enter as many as apply.

> Volume: The default volume is one because most Audiology and Speech Pathology procedures are complexity-based, not time-based.

> Complexity-Based Procedures: The volumes for codes that are complexity-based are always "one". For example, if you provide treatment (92507), one code is entered regardless of how much time is spent with the patient. If the time spent exceeds the typical time for that procedure, you should enter CPT Modifier 22 to show that the complexity of procedure was unusual.

> Time-Based Procedures: Some procedure (CPT) codes are time-based (e.g., 97703, 96105). One code is entered for each specified time period. For example, code 97703 has a period of 15 minutes. If the procedure was performed for 30 minutes, then a volume of "two" would be entered.

> Repeated Procedures: If a procedure is repeated, the volume is not entered as "two". When the procedure is repeated by the same provider, modifier 76 is entered. If the procedure is repeated by another provider, modifier 77 is used.

> The typical times associated with various procedures can be found in the A&SP Product Code Manual, on the A&SP Website at <span class="mark">REDACTED</span> or from your local DSS Office.

> Procedure Provider: The default is the Primary Provider. You may accept the default entry or enter a new provider.

Time Spent (minutes): Enter the total time spent during the clinic visit. Time is recorded in minutes and is to include direct (e.g., face-to-face) and indirect time (e.g., report writing, progress note writing, decision making, record review, and/or coordination of care). The chief use of procedure time data is the CDR. You can sort, tabulate, and print procedure time by clinic or provider using the Tailor-Made A&SP Reports option.

If all the required data has been entered and you are using the AMIE/C&P interface, the program allows you to sign off on the exam.

Are you ready to sign off this exam? No// y (Yes)

SIGNATURE CODE: (Enter your signature code)

Ok...

#### Entering Visit Data for a New QUASAR Patient

In this example:

- The Send to PCE site parameter is set to YES.
- The patient is Service Connected.
- The patient has been exposed to Agent Orange and Radiation.
- The Use ASP Clinic File Number site parameter is set to YES.

> Example

New Clinic Visits

This option is used to enter new A&SP clinic visits. Existing clinic

visits should be updated with the Edit an Existing Visit option.

Select DIVISION CIOFO HINES DEV Station Number : 14100

Select CLINIC: AUDIOLOGY

Clinic: AUDIOLOGY Stop Code: 203

Enter Visit Date: TODAY// \<RET\> (OCT 26, 1999)

Select A&SP PATIENT NAME: QUASARPATIENT,FOUR 01-10-44 321456733 YES

SC VETERAN

\- APPOINTMENT LIST -

Name : QUASARPATIENT,FOUR SSN : 000-00-0004

Date : 10/26/99 Clinic : AUDIOLOGY

Appt Date/Time Status Appointment Type

1\. OCT 26,1999 09:35 NO ACTION TAKEN REGULAR

Select Appointment (1-1) or (N)ew Visit : 1// \<RET\>

QUASAR V.3. NEW VISIT ENTRY

Patient Inquiry

CLINIC: AUDIOLOGY DIVISION: CIOFO HINES DEV

PATIENT: QUASARPATIENT,FOUR DOB: JAN 10,1944 SSN: 000-00-0004

ELIGIBILITY: SC LESS THAN 50% INITIAL VISIT DATE:

Patient is currently an inpatient.

WARD: 4AS ROOM/BED: TREATING SPEC:NEUROLOGY

This visit's Treatment:

---------------------------------------------------------------------------------------------------------------------------------------

Related to AGENT ORANGE ? : UNKNOWN Service Connected ? : UNKNOWN

Related to RADIATION EXPOSURE ? : UNKNOWN

Patient Diagnostic History

Ms. QUASARPATIENT,FOUR has been seen for the following:

DIAGNOSIS DATE ENTERED

---------------------------------------------------------------------------------------------------------------------------------------

No A&SP Diagnostic Data for this Patient

APPOINTMENT TIME: 9:35 AM (Uneditable)

INITIAL VISIT DATE: OCT 26, 1999// \<RET\> (OCT 26, 1999)

ASP FILE NUMBER: TINY123

^

Select DIAGNOSTIC CODE: 784.3 APHASIA

...OK? Yes// \<RET\> (Yes)

784.3 APHASIA

We have no previous record of diagnostic condition 784.3 for Ms. QUASARPATIENT,FOUR.

Ok, I've added this code to her permanent record !

Is this the Primary Diagnosis ?: Y YES

Select DIAGNOSTIC CODE: \<RET\>

Service Classifications

SERVICE-CONNECTED AGENT-ORANGE RADIATION

This Patient has other Entitled Eligibilities

NSC NON-SERVICE CONNECTED

PRISONER OF WAR PRISONER OF WAR

Enter the Eligibility for this Appointment: SC LESS THAN 50%

// NSC

Was care for SC Condition ?: N NO

Was care related to AO Exposure ?: N NO

Was care related to IR Exposure ?: Y YES

Suggested CDR Account :1111.00 NEUROLOGY

CDR ACCOUNT: 1111.00// \<RET\> NEUROLOGY

PRIMARY PROVIDER: QUASARPROVIDER,ONE AG AUDIOLOGY AND SPEECH PATH

SECONDARY PROVIDER: \<RET\>

STUDENT: \<RET\>

Select PROCEDURE CODE: 92506 SPEECH & HEARING EVALUATION

Select CPT MODIFIER: ?

You may enter a new CPT MODIFIER, if you wish

Enter a Modifier code(s) for the selected Procedure.

Only valid Modifiers for the selected Procedure that are marked as

active on the A&SP CPT Modifiers File are available for selection.

Answer with A&SP PROCEDURE MODIFIER

Do you want the entire A&SP PROCEDURE MODIFIER List? Y (Yes)

Choose from:

22 UNUSUAL PROCEDURAL SERVICES CPT

26 PROFESSIONAL COMPONENT CPT

51 MULTIPLE PROCEDURES CPT

52 REDUCED SERVICES CPT

53 DISCONTINUED PROCEDURE CPT

59 DISTINCT PROCEDURAL SERVICE CPT

76 REPEAT PROCEDURE BY SAME PHYSICIAN CPT

77 REPEAT PROCEDURE BY ANOTHER PHYSICIAN CPT

99 MULTIPLE MODIFIERS CPT

TC TECHNICAL COMPONENT HCPCS

Select CPT MODIFIER: \<RET\>

VOLUME: 1// \<RET\>

PROCEDURE PROVIDER: QUASARPROVIDER,ONE// \<RET\>

Select PROCEDURE CODE: \<RET\>

TIME SPENT (minutes): 30

#### Entering Audiometry Scores

If the USE C&P site parameter is answered YES, you are utilizing the AMIE/C&P interface. Staff involved in the C&P process must have an electronic signature. An electronic signature can be established using the Edit Electronic Signature Code option in the User’s Toolbox menu.

The AMIE linkage feature allows entry of text and audiometric data in the AMIE format, adequation of the results, and hand-off of the report to the AMIE Compensation and Pension package. When an entry is made for the patient, you are asked "Is this a C&P exam?” If you respond YES, in addition to the usual QUASAR information, narrative data is requested for generating the AMIE report. When the exam is signed and adequated, the rating narrative, and audiometric data are transmitted to the AMIE system.

The C&P exam prompt may not appear for the following reasons:

1.  The patient is not a C&P patient. The chief reason for this event is that VARO did not request an AUDIO exam (see Form 2507) or the examining physician requests an audiological assessment not requested by VARO. You should contact the C&P Unit to have AUDIO added to the selected exam list.
8.  The patient’s C&P claim has been closed by the C&P Unit. This event occurs when users do not use QUASAR to process rating summaries (i.e., the AMIE link is disabled) and QUASAR visit data are entered significantly after the visit date. You should contact your C&P Unit to see if the exam has been closed out.

If you are using the AMIE/C&P interface, QUASAR prompts for the AMIE rating summary fields. These fields may be filled by entering text through the line or text editor or by pasting text into the summary field from commercial word-processing software. If the AMIE/C&P interface is not enabled, the text fields do not appear.

> **NOTE:** Procedures differ from clinic to clinic. The example below is for demonstration purposes only and is not intended to represent the official format for rating summaries.

..........

Is this a C&P Visit ?: YES// \<RET\> YES

Select DIAGNOSTIC CODE: 388.2 SUDDEN HEARING LOSS NOS

388.2 SUDDEN HEARING LOSS NOS

We have no previous record of diagnostic condition 388.2 for Mr. QUASARPATIENT,FIVE.

Ok, I've added this code to his permanent record !

Is this the Primary Diagnosis ?: Y YES

Select DIAGNOSTIC CODE: \<RET\>

Service Classifications

SERVICE-CONNECTED

This Patient has other Entitled Eligibilities

NSC NON-SERVICE CONNECTED

Enter the Eligibility for this Appointment: SERVICE CONNECTED 50% to 100%

// NSC

Was care for SC Condition ?: N NO

Suggested CDR Account :2611.00 REHABILITATIVE & SUPPORTIVE SERVICES

CDR ACCOUNT: 2611.00// \<RET\> REHABILITATIVE & SUPPORTIVE SERVICES

Enter Audiometrics :

TONE R500: 30

TONE R1000: 35

TONE R2000: 75

TONE R3000: 75

TONE R4000: 75

TONE L500: 30

TONE L1000: 30

TONE L2000: 75

TONE L3000: 75

TONE L4000: 75

CNC R: 85

CNC L: 80

W22 R: 1

W22 L: 1

Compensation and Pension Examination

For AUDIO

\#1305 Worksheet

> An examination of hearing impairment must be conducted by a state-licensed

> audiologist and must include a controlled speech discrimination test

> (specifically, the Maryland CNC recording) and a pure tone audiometry test in

> a sound isolated booth that meets American National Standards Institute

> standards (ANSI S3.1.1991) for ambient noise.

> Measurements will be reported at the frequencies of 500, 1000, 2000, 3000,

> and 4000 Hz. The examination will include the following tests: pure tone

> audiometry by air conduction at 250, 500, 1000, 2000, 3000, 4000 Hz, and 8000

> Hz; and by bone conduction at 250, 500, 1000, 2000, 3000, and 4000 Hz;

> spondee thresholds; speech recognition using the recorded Maryland CNC Test;

> tympanometry; and acoustic reflex tests, and, when necessary, Stenger tests.

> Bone conduction thresholds are measured when the air conduction thresholds

> are poorer than 15 dB HL. A modified Hughson-Westlake procedure will be used

> with appropriate masking. A Stenger test must be administered whenever pure

> tone air conduction thresholds at 500, 1000, 2000, 3000, and 4000 Hz

> differ by 20 dB or more between the two ears.

Press RETURN to continue:

Compensation and Pension Examination

For AUDIO

\#1305 Worksheet (Continued)

> Maximum speech recognition will be reported with the 50-word VA-approved

> recording of the Maryland CNC test. When speech recognition is 92% or less,

> a performance intensity function will be obtained with a starting

> presentation level of 40dB re SRT. If necessary, the starting level will be

> adjusted upward to obtain a level at least 5 dB above the threshold at 2000

> Hz. The examination will be conducted without the use of hearing aids. Both

> ears must be examined for hearing impairment even if hearing loss in only one

> ear is at issue.

REVIEW OF MEDICAL RECORDS: Indicate whether the C-file was reviewed. If

the C-file was not reviewed or was not available for review, the examiner

should so state.

REVIEW OF MEDICAL RECORDS:

1\>ENTER THE TEXT.

2\> \<RET\>

EDIT Option: \<RET\>

MEDICAL HISTORY (SUBJECTIVE COMPLAINTS):

Comment on:

1\. Chief Complaint.

2\. Situation of greatest difficulty.

3\. Pertinent service history.

4\. History of military, occupational, and recreational noise exposure.

5\. Tinnitus - If present, state:

a\. date and circumstances of onset

b\. whether it is unilateral or bilateral

c\. whether it is recurrent (indicate frequency and duration)

d\. State the most likely etiology of the tinnitus, and

specifically, if hearing loss is present, whether the tinnitus

is due to the same etiology (or causative factor) as the hearing

loss.

MEDICAL HISTORY:

1\>ENTER THE TEXT

2\> \<RET\>

EDIT Option: \<RET\>

PHYSICAL EXAMINATION (OBJECTIVE FINDINGS):

1\. Measure pure tone thresholds in decibels at the indicated

frequencies (air conduction):

==========RIGHT EAR=============================LEFT EAR===============

A\* B C D E \*\* A\* B C D E \*\*

500 1000 2000 3000 4000 average 500 1000 2000 3000 4000 average

\*The pure tone threshold at 500 Hz is not used in determining the

evaluation but is used in determining whether or not a ratable

hearing loss exists.

\*\*The average of B, C, D, and E.

2\. Speech Recognition Score:

Maryland CNC word list \_\_\_\_\_\_% right ear \_\_\_\_\_% left ear

3\. When only pure tone results should be used to evaluate hearing

loss, the examiner, who must be a state-licensed audiologist, should

certify that language difficulties or other problems (specify what

the problems are) make the combined use of pure tone average and

speech discrimination inappropriate.

PHYSICAL EXAMINATION:

1\>ENTER THE TEXT.

2\> \<RET\>

EDIT Option: \<RET\>

DIAGNOSTIC AND CLINICAL TESTS:

1\. Report middle-ear status, confirm type of loss, and indicate need for

medical follow-up. In cases where there is poor inter-test

reliability and/or positive Stenger test results, obtain and report

estimates of hearing thresholds using a combination of behavioral

testing, Stenger interference levels, and electrophysiological tests.

2\. Include results of all diagnostic and clinical tests conducted in the

examination report.

DIAGNOSTIC AND CLINICAL TESTS:

1\>ENTER THE TEXT

2\> \<RET\>

EDIT Option: \<RET\>

DIAGNOSIS:

1\. Summary of audiologic test results. Indicate type and degree of

hearing loss for the frequency range from 500 to 4000 Hz. For type of

loss, indicate whether it is normal, conductive, sensorineural,

central, or mixed. For degree, indicate whether it is mild (26-40 dB

HL), moderate (41-54 dB HL), moderately-severe (55-69 dB HL), severe

(70-89 dB HL), or profound (90+ dB HL). For VA purposes, impaired

hearing is considered to be a disability when the auditory threshold

in any of the frequencies 500, 1000, 2000, 3000, and 4000 Hz is 40 dB

HL or greater; or when the auditory thresholds for at least three of

these frequencies are 26 dB HL or greater; or when speech recognition

scores are less than 94%.

2\. Note whether, based on audiologic results, medical follow-up is needed

for an ear or hearing problem, and whether there is a problem that, if

treated, might cause a change in hearing threshold levels.

DIAGNOSIS:

1\>ENTER THE TEXT

2\> \<RET\>

EDIT Option: \<RET\>

#### Forcing the C&P Prompt

(Not Using the AMIE/C&P Interface or Audiometric Data for Hearing Loss Codes).

It is permissible to force the "Is this a C&P exam?" prompt and there are occasions when this is acceptable. To force the C&P prompt, enter "^C AND P" after the patient identifying information (e.g., at the "Select DIAGNOSTIC CODE:" prompt). A facility not using the AMIE/C&P interface might force the prompt to keep an accurate count of C&P exams. A facility using the AMIE/C&P interface might force the prompt in order to produce the C&P report for an allied war veteran with a C&P appointment. The allied war veteran’s report would be signed manually, because only C&P exams requested through VARO can be adequated through QUASAR.

If your facility uses the AMIE/C&P interface, you must keep in mind that forcing the "Is this a C&P exam?" prompt DOES NOT create the required linkage information between QUASAR and AMIE. If the C&P question does not appear during data input, you should confer with your C&P Unit to determine the cause.

> **NOTE:** Exams with forced C&P prompts cannot be adequated and may not be available to the AMIE package.

The example below presumes the AMIE/C&P interface is inactivated and the facility has the BYPASS AUDIOMETRICS site parameter set to YES. The facility uses QUASAR to track the number of C&P exams.

\[Patient Inquiry screen\]

Select DIAGNOSTIC CODE: ^C

1 C AND P

2 CDR ACCOUNT

3 CLINICIAN

4 CNC L

5 CNC R

CHOOSE 1-5: 1

Is this a C&P visit? : YES// \<ret\> YES

#### Deleting a Non-Hearing Loss Code to Obtain Audiometric Display

Certain diagnosis codes (i.e., hearing loss codes) are flagged to require audiometric data to be entered when those codes are used for a visit. If the Bypass Audiometrics site parameter is answered NO, you are asked to enter audiometric data.

After audiometric data is entered for a patient’s visit, you may wish to edit the audiometric fields. When a non-hearing loss code is the last <span id="p21_36" class="anchor"></span>ICD CM code entered, the audiometric fields are not displayed for editing. In order to edit, follow these steps.

1.  Delete the non-hearing loss code from the record.
9.  Edit the audiometric data field(s).
10. Re-enter the deleted non-hearing loss code using the ^ (shift-6) key to skip to the diagnostic code field.

<span id="p21_38" class="anchor"></span>Note: CDR and audiometric fields in VistA QUASAR are obsolete. CDR is no longer used and the audiometric functionality was replaced by GUI QUASAR (audiometric module).

#### Delete the non-hearing loss code:

Select DIAGNOSTIC CODE: 388.9// @

SURE YOU WANT TO DELETE THE ENTIRE DIAGNOSTIC CODE? Y (Yes)

Select DIAGNOSTIC CODE: 389.10// \<ret\>

DIAGNOSTIC CODE: 389.10// \<ret\>

Select DIAGNOSTIC CODE: \<ret\>

Suggested CDR Account: 2611.00 REHABILITATIVE & SUPPORTIVE SERVICES

CDR ACCOUNT: 2611.00// \<ret\>

Audiometric testing for this patient last completed 09/17/94.

PURE TONE RESULTS:

R500: 30 L500: 30

R1000: 35 L1000: 30

R2000: 75 L2000: 75

R3000: 75 L3000: 75

R4000: 75 L4000: 75

R AVG: 65 L AVG: 63

CNC R: 85 CNC L: 80

W22 R: 10 W22 L: 10

#### Edit the audiometric data field(s): 

Do you wish to use these scores? NO

Enter Audiometrics:

TONE R500: 30// ^TONE L1000

TONE L1000: 30// 35

TONE L2000: 75// ^DIAGNOSTIC CODE

#### Re-enter the deleted non-hearing loss code:

Select DIAGNOSTIC CODE: 389.10// 388.9 DISORDER OF EAR NOS

...OK? Yes// \<ret\> (Yes)

Are you adding '388.9' as a new DIAGNOSTIC CODE (the 2ND for this A&SP CLINIC

VISIT)? Y (Yes)

Select DIAGNOSTIC CODE: ^

### Edit an Existing Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS VISIT EDIT\]

The Edit an Existing Visit option is used to modify an existing clinic visit when the data is incorrect, incomplete, or needs to be updated. This option is not to be used to enter a new visit. Fields in this option appear as shown in the New Clinic Visits option.

Notes:

1.  If you want to delete a visit entered in error, use the option: Delete an A&SP Clinic Visit.
2.  The “Appointment Time” prompt is NOT an editable field.

### Inquire - A&SP Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS PAT INQ\]

The Inquire - A&SP Patient option displays demographic information for an A&SP patient which includes date of birth, social security number, eligibility, service connected status, and initial visit date. Additionally the option shows inpatient status and diagnostic history. Output can be sent to a printer.

After selecting the A&SP patient’s name, you are given an opportunity to update the diagnostic history. The problem list is recompiled using this logic: All clinic visits for the patient are examined. Unique diagnostic codes and the earliest date for each code are determined. The A&SP Patient file is updated with these codes and dates. Also, the earliest diagnostic date found becomes the Initial Visit Date.

### A&SP Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS REPORTS\]

The A&SP Reports menu contains options to print Audiology and Speech Pathology reports. This menu can be assigned to users who do not enter or modify A&SP data, but require read only access.

> Visits by Diagnosis \[ACKQAS VISITS BY DIAG\]

> Patients by City \[ACKQAS PAT BY CITY\]

> Statistics by Procedure \[ACKQAS PROC STATS\]

> Cost Comparison Report \[ACKQAS PRINT COST COMPARE\]

> Tailor-Made A&SP Reports \[ACKQAS ADHOC\] \*\*Locked with ACKQ ADHOC\*\*

> PCE Exception Report \[ACKQAS PCE EXCEPTION REPORT\]

> Workload Report \[SDCLINIC WORKLOAD\]

#### Visits by Diagnosis

\[ACKQAS VISITS BY DIAG\]

The Visits by Diagnosis report is printed by selected Division(s) and a date range. You can print the report for Audiology (includes Telephone Audiology) only, Speech Pathology (includes Telephone Speech) only, or both Audiology and Speech Pathology.

You can choose to print the report for one or all clinician(s), other provider(s), or student(s).

The report lists clinic visits for the date range and selected Division(s) sorted by <span id="p21_40" class="anchor"></span>ICD CM diagnostic codes. Since the diagnostic code field is a multiple field, the visit shows up once under each diagnostic code entered for that visit.

<span id="p21_38_2" class="anchor"></span>Example

Audiology & Speech Pathology

Diagnostic Code Statistics

for

XXXXXXX

Covering Visits from 01/01/99 to 07/24/12

For Division: NASHVILLE

--------------------------------------------------------------------------------

STOP CODE: SPEECH PATHOLOGY

CLINIC: SPEECH PATH - CHRISTY

CLINICIAN: XXXXXX

141.9 MALIG NEO TONGUE NOS COUNT: 3

386.54 HYPOACT LABYRINTH BILAT COUNT: 1

387.9 OTOSCLEROSIS NOS COUNT: 1

V41.2 PROBLEMS WITH HEARING COUNT: 1

V53.2 ADJUSTMENT HEARING AID COUNT: 2

V57.3 SPEECH-LANGUAGE THERAPY COUNT: 1

V70.5 HEALTH EXAM-GROUP SURVEY COUNT: 1

Enter RETURN to continue or '^' to exit:

Printed: 07/24/12 at 10:36 Page: 2

Audiology & Speech Pathology

Diagnostic Code Statistics

For Division: NASHVILLE

Summary

--------------------------------------------------------------------------------

STOP CODE: SPEECH PATHOLOGY

141.9 MALIG NEO TONGUE NOS COUNT: 3

386.54 HYPOACT LABYRINTH BILAT COUNT: 1

387.9 OTOSCLEROSIS NOS COUNT: 1

F07.0 Personality change due to known

physiological Condition COUNT: 1

G31.84 Mild cognitive impairment, so stated COUNT: 1

V41.2 PROBLEMS WITH HEARING COUNT: 1

V53.2 ADJUSTMENT HEARING AID COUNT: 2

V57.3 SPEECH-LANGUAGE THERAPY COUNT: 1

V70.5 HEALTH EXAM-GROUP SURVEY COUNT: 1

Total For SPEECH PATHOLOGY 10

Total For Division: NASHVILLE 12

.

#### Patients by City

\[ACKQAS PAT BY CITY\]

The Patients by City option generates a patient count report by selected Division(s) and date range. The report shows the number of patients seen, sorted by city of residence.

Example

Audiology & Speech Pathology

Unique Patients by City

Visits from 11/01/99 to 11/30/99

For Division: CIOFO HINES DEV

---------------------------------------------------------------------------------------------------------------------------------------

CLINIC: AUDIOLOGY

STOP CODE: AUDIOLOGY

CHICAGO, IL: 13 patients

MAYWOOD, IL: 4 patients

MELROSE PARK, IL: 2 patients

...

*Statistics by Event Capture Procedure*

\[ACKQAS EC PROC STATS\]

The Statistics by Event Capture Procedure[^10] report is printed by selected Division(s) and a date range. You can print the report for Audiology (includes Telephone Audiology) only, Speech Pathology (includes Telephone Speech Pathology) only, or both Audiology and Speech Pathology.

You can choose to print the report for one or all clinician(s), other provider(s), or student(s).

The report lists clinic visits for the date range and selected Division(s) sorted by Event Capture codes.

Example

Audiology & Speech Pathology

EC Procedure Statistics

for

All Clinicians

Covering Visits from 10/02/00 to 11/21/00

For Division: CIOFO HINES DEV

---------------------------------------------------------------------------------------------------------------------------------------

STOP CODE: AUDIOLOGY

CLINIC: AUDIOLOGY AND SPEECH PATHOLOGY

CLINICIAN: QUASARPROVIDER1,SIX

SP002 SPCH LOUDNESS TOLERANCE TEST COUNT: 2

SP010 SPEECH/LANGUAGE SCREENING COUNT: 2

SP025 HEARING TREATMENT NEC COUNT: 1

SP053 INSTRUM STUDY OF NASAL FUNCTION COUNT: 1

SP104 HEARING AID EVALUATION BIN COUNT: 1

SP106 HEARING AID CHECK/REPAIR/ADJUST, BIN COUNT: 3

SP110 EAR CANAL PROBE MEASUREMENT, BIN COUNT: 1

SP128 SPECIAL SUPPLIES COUNT: 44

...

#### Statistics by Procedure

\[ACKQAS PROC STATS\]

The Statistics by Procedure report is printed by selected Division(s) and a date range. You can print the report for Audiology (includes Telephone Audiology) only, Speech Pathology (includes Telephone Speech Pathology) only, or both Audiology and Speech Pathology.

You can choose to print the report for one or all clinician(s), other provider(s), or student(s).

The report lists clinic visits for the date range and selected Division(s) sorted by CPT-4 procedure codes. Since the procedure code field is a multiple field, the visit shows up once under each procedure code entered for that visit.

Example

Audiology & Speech Pathology

Procedure Statistics

for

Provider, QUASARPROVIDER,ONE

Covering Visits from 11/27/99 to 11/29/99

For Division: CIOFO HINES DEV

--------------------------------------------------------------------------------------------------------------------------------------

STOP CODE: SPEECH PATHOLOGY

CLINIC: SPEECH

CLINICIAN: PROVIDER, QUASARPROVIDER,ONE

31505 DIAGNOSTIC LARYNGOSCOPY COUNT: 1

...

#### #### Cost Comparison Report

\[ACKQAS PRINT COST COMPARE\]

The Cost Comparison Report option produces a report of all CPT-4 procedure codes and their associated costs used within a selected date range. The cost linked to a CPT code is based upon approximate private sector cost. Cost is entered by local A&SP supervisors using the Enter Cost Information for Procedures option on the Set Up/Maintenance menu.

The following example is for demonstration purposes only and is not meant to reflect actual costs.

Example

Procedure Cost Comparison

for Date Range

08/21/99 to 11/29/99

For Division: CIOFO HINES DEV

QUAN CODE DESCRIPTION COST TOTAL

---------------------------------------------------------------------------------------------------------------------------------------

STOP CODE: Speech Pathology

1 31505 DIAGNOSTIC LARYNGOSCOPY \$ 60.00 \$ 60.00

1 31575 DIAGNOSTIC LARYNGOSCOPY \$ 60.00 \$ 60.00

2 92506 SPEECH & HEARING EVALUATION \$ 60.00 \$ 120.00

7 92508 SPEECH/HEARING THERAPY \$ 60.00 \$ 420.00

5 92511 NASOPHARYNGOSCOPY \$100.00 \$ 500.00

3 92512 NASAL FUNCTION STUDIES \$ 60.00 \$ 180.00

Speech Pathology Total: \$1340.00

...

#### Tailor-Made A&SP Reports

\[ACKQAS ADHOC\] \*\*Locked: ACKQ ADHOC\*\*

The Tailor-Made A&SP Reports option allows you to design reports using the VA FileMan sort and print functionality. Reports can be generated from the A&SP Clinic Visit file (#509850.6) or the A&SP Patient file (#509850.2). You must be familiar with VA FileMan’s Print and Sort functions as well as the structure of the file from which the data is printed.

Access to this option is controlled by the ACKQ ADHOC security key. Allocation of this key is at the discretion of the IRM chief. The option may not be available at all sites. If available, this option can provide various statistical reports from the QUASAR package. However, its indiscriminate use could have a negative impact on system performance. Complicated sorts or reports that could be expected to impact system performance should be queued to run during off-hours.

Refer to the chapter, [Creating Tailor-Made Reports](#creating-tailor-made-reports), for additional information. This section contains tips and examples on how to generate your own tailor-made reports.

> **NOTE:** Check all sort and print routines created in the previous version for field name changes.

#### PCE Exception Report

\[ACKQAS PCE EXCEPTION REPORT\]

This report lists all A&SP Clinic Visits from the date range selected for the Division that have not been successfully updated in PCE. See [Required Data](#required-data), for those fields that pass data to PCE.

#### Reasons for Exceptions

A Visit will be included on the report if it falls into one of the following categories:

1.  The last time QUASAR attempted to send the Visit to PCE, the Visit was rejected. In this case, the report will include the error messages returned by the PCE Interface.

> Example

Audiology & Speech Pathology

PCE Exception Report

For Division: CIOFO HINES DEV

---------------------------------------------------------------------------------------------------------------------------------------

Clinic: SPEECH PATHOLOGY

Visit Date: MAY 01, 1999 Patient: QUASARPATIENT,SIX

Appnt. Time: 5:00 AM SSN: OOO-OO-OOO6

PRIMARY PROVIDER – QUASARPROVIDER,TWO

The Provider does not have an ACTIVE person class!

Visit Date: AUG 30, 1999 Patient: QUASARPATIENT,SEVEN

Appnt. Time: 8:00 PM SSN: 000-00-0007

PCE VISIT -

Unable to Delete PCE Visit

Visit Date: SEP 30, 1999 Patient: QUASARPATIENT,EIGHT

Appnt. Time: 12:00 AM SSN: 000-00-0008

ENC D/T - SEP 30, 1999

You are missing the TIME of the visit in FileManager internal format.Unless this is an HISTORICAL encounter, you must have the time.

11. The Visit was edited in QUASAR but the new Visit data was not sent to PCE because the PCE Interface was switched off. In this case the report will show the date/time of the last QUASAR update versus the date/time of the last time the Visit was sent to PCE.

    Example

Audiology & Speech Pathology

PCE Exception Report

For Division: CIOFO HINES DEV

---------------------------------------------------------------------------------------------------------------------------------------

Visit Date: SEP 22, 1999 Patient: QUASARPATIENT,NINE

Appnt. Time: 2:00 PM SSN: 000-00-0009

Last Edit in QSR: SEP 22, 1999@16:35:22 PCE time is before QSR time

Last Sent to PCE: SEP 22, 1999@14:00:20

Visit Date: SEP 23, 1999 Patient:

Appnt. Time: 12:00 AM SSN:

Last Edit in QSR: SEP 23, 1999@10:46:49 No PCE time

Last Sent to PCE:

To remove a Visit from the Exception report, the PCE Interface must be activated for the Site, and for the Division in which the Visit took place, and then correct the error.

1.  Errors may include data missing in non-QUASAR files such as the New Person file \#200 or the USR Class Membership file \# 8930.3. In that situation, you may need to contact IRM for assistance. Once corrected, you must edit the visit again using the option Edit an Existing Visit to send the corrected data to PCE.
12. If the errors are in QUASAR:
- In files other that the A&SP Clinic Visit file, make the corrections and then use the option Edit an Existing Visit to send the corrected data to PCE.
- In the A&SP Clinic Visit file, use the option Edit an Existing Visit to edit the data and send the corrected information to PCE.
13. If you delete a visit and it still exists in PCE ("Unable to Delete PCE Visit"), use PCE to delete the visit.

Once the Visit data is the same in both systems (QUASAR and PCE), the visit is removed from the PCE Exception Report.

Warning Message:[^11]

You will be prompted to enter a Beginning Date and Ending Date for the PCE Exception Report date range. When entering a Beginning Date prior to March 17, 2000, which was the date that Version 3.0 of QUASAR was installed, a WARNING message will display.

Example

QUASAR - PCE Exception Report

This option produces a report listing all the A&SP Clinic Visits that have been

reported as an exception by PCE.

Select DIVISION: ALL

Beginning Date: T-2000 (MAY 27, 1995)

Ending Date: T

Warning - You are running a report using a start date that falls either on orbefore the installation of Version 3.0 of Quasar.Quasar Version 3.0 was installed on - MAR 17, 2000Note that all PCE related functionality was developed within Quasar version 3.0.It is recommended that this report be run using start dates that fall after theinstallation date.

Do you want to Continue ? NO//

#### Workload Report

\[SDCLINIC WORKLOAD\]

The Workload Report is not a QUASAR option. It is on the A&SP Reports menu with permission from the Scheduling package. This option displays daily patient appointment transactions by division for a selected date range. It allows you to determine the relative activity within a clinic during specified periods and allows you to compare activity for selected clinics for the previous year. You may want to print the report only for Audiology (203), Speech Pathology (204), and/or Telephone/Rehab and Support (216) Stop Code.

> **CAUTION:** The default Stop Code for this report is ALL. This means that all Stop Codes will be reported. Be careful to enter only Stop Code/DSS identifier 203, 204, or 216. See example below:

Select division: ALL// HINES ISC 578

Select another division:

\*\*\*\* Date Range Selection \*\*\*\*

Beginning DATE : 9/1/99 (SEP 01, 1999)

Ending DATE : 9/30/99 (SEP 30, 1999)

Will now check if outpatient encounter dates have been updated...

......

> **NOTE:** To obtain accurate statistics, this workload report should

be run again after the outpatient encounter status update

process has been completed for these dates.

Totals by (C)LINIC or (S)TOP CODE?: C//STOP CODE

Enter Stop Code: ALL//203

AUDIOLOGY 203

Enter Stop Code: 204

SPEECH PATHOLOGY 204

Enter Stop Code: 216

TELEPHONE/REHAB AND SUPPORT 216

Enter Stop Code: \<RET\>

Do you want to include add/edits? No// \<RET\> (No)

Brief or Expanded Report? E// \<RET\> EXPANDED

(D)ETAIL BY DAY or (S)UMMARY BY MONTH?: D// \<RET\> DETAIL BY DAY

Do you want to see patient names? No// \<RET\> (No)

Do you want to compare this data to the same period in the previous year? No//

# Generating Management Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Management Reports A&SP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS MANAGEMENT REPORTS\]

The Management Reports A&SP menu allows you to generate the Audiology and Speech Pathology CDR, and to compile and print the A&SP Capitation report. This data is stored in the A&SP Workload file (#509850.7).

- Generate A&SP Service CDR \[ACKQAS CDR\]
- Print A&SP Service CDR \[ACKQAS CDR PRINT\]
- Compile A&SP Capitation Data \[ACKQAS WKLD GEN MAN\]
- Print A&SP Capitation Report \[ACKQAS WKLD VERIFY\]

### Generate A&SP Service CDR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS CDR\]

The Generate A&SP Service CDR option generates and prints the RCS 10-0141 report for Audiology and Speech Pathology by Division.

Once each month you should run and save a CDR report. It is saved in the A&SP Workload file (#509850.7). If you choose to save the CDR, it must be run for a single entire month. If you choose not to save the report, you can run the CDR for any date range.

You must enter the month for which the report is to be generated. The total number of clinic visit hours and instructional support (.12) hours for the month is displayed. You are prompted for the total number of paid hours.

You can enter a flat number of hours to be distributed among all administrative support (.13), continuing education (.14), and research (.21 and .22) accounts or you can enter hours for each account individually. You are then asked for pass through account hours. When entering hours for these accounts, keep in mind the number of clinic visit hours. Do not let the number of hours remaining go below the total number of clinic visit hours.

The A&SP CDR is an 80-column report which displays only the CDR accounts with activity during the date range.

### Print A&SP Service CDR 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS CDR PRINT\]

The Print A&SP Service CDR option prints the RCS 10-014 report for Audiology and Speech Pathology. Use this option to reprint the CDR report that you created using the Generate A&SP Service CDR option. If your CDR is reported by Division, you must select the Division(s) to be printed. Then enter the month that you wish to print. The report will print the CDR for the month and Divisions that have been generated.

### Compile A&SP Capitation Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS WKLD GEN MAN\]

The Compile A&SP Capitation Data option is used to generate capitation data by Division for a selected month. If data has previously been compiled for the month selected, you are asked if you wish to continue. If you do so, the previously compiled data is deleted and the information is recalculated. The compilation takes place in the background, and you are notified by an e-mail message when the task is finished. You can use the Print A&SP Capitation Report to review the data.

### Print A&SP Capitation Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS WKLD VERIFY\]

When the Compile A&SP Capitation Data option has generated information for selected Division(s) and a selected month, you are notified by an e-mail message. You can then use the Print A&SP Capitation Report to review the data. This option produces a three-part report by Division that includes demographic, diagnostic, procedure data. This is followed by a summary (not separated by Division) that includes demographic, diagnostic and procedure data.

# Adequating a C&P Exam

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## C&P Exam Adequation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS CP ADEQ\]

This option allows you to adequate a C&P exam. Only exams that are complete (i.e., having a status of AWAITING ADEQUATION) and signed off on can be adequated.

When an audiologist provides his or her electronic signature to a C&P exam, the chief adequator sees a list of exams waiting to be adequated. He or she can review, print, or edit the report using the Edit an Existing Visit option. Finally, he or she can provide an electronic signature using the C&P Exam Adequation option to release the report to the AMIE package. Entering the electronic signature to adequate an exam causes all exam results to be transferred to the AMIE C&P package and the exam is marked CLOSED. The results are made available to the regional office. Non-supervisory clinicians can adequate their own C&P exams. A clinician designated as a supervisor in the A&SP Staff file (#509850.3) can adequate other clinicians’ C&P exams.

# Deleting a Clinic Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Delete an A&SP Clinic Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[ACKQAS DELETE VISIT\]

This option allows you to delete an A&SP Clinic Visit that has been entered in error. If the selected visit was sent to PCE, then this function will also attempt to delete the visit from PCE. If the PCE deletion fails, you will see a warning message displayed.

Warning - This QUASAR Visit is linked to a PCE Visit but the PCE Interface is not active. If you delete this visit, it will be deleted from QUASAR but the corresponding PCE VISIT will remain. To delete the visit from PCE you must use the PCE package options.

or

ERROR: The PCE Visit linked to this QUASAR Visit could not be deleted.

If you choose to continue, the QUASAR visit will be deleted but the PCE Visit will remain. Corrective action to the PCE Visit will be required using the PCE system.

You may then choose to continue or abort the deletion. If you continue, the Quasar Visit will be deleted but you will have to use the PCE package to delete the same visit from PCE.

*This page intentionally left blank for double-sided printing*

# Creating Tailor-Made Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix provides instruction on sorting data and printing reports using the option Tailor-Made A&SP Reports. Any of the QUASAR data fields and some of the data fields contained in the patient file \# 2 can be sorted and printed. The Tailor-Made A&SP Reports option is a restricted version of VA FileMan. It permits sorting, basic arithmetic operations, Boolean logic, saving of sort logic, and customized formatting of reports. Users are encouraged to contact their IRM Service to obtain training and training materials on VA FileMan report generation.

Access to the Tailor-Made A&SP Reports option is controlled by the ACKQ ADHOC security key. Allocation of this key is at the discretion of the IRM Chief. Therefore, Tailor-Made A&SP Reports may not available at all sites.

> **IMPORTANT:** Indiscriminate use of VA FileMan may have a negative impact on system performance. Complicated sorting routines or reports should be queued to run during off-hours.

VA FileMan functions like an index card filing system. Any data entered in QUASAR data fields can be accessed, sorted, and printed as can data in any "pointed to" file (e.g., Patient file \#2).

## Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A&SP Patient file \#509850.2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The A&SP Patient file contains identifying, demographic, and other clinical information for all patients seen in the Audiology and Speech Pathology clinics.

| Field \# | Label                | Description                                                                                                                                                                                                |
|--------------|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| .01          | Name                     | The NAME field contains the name of the patient seen in the Audiology and Speech Pathology clinics.                                                                                                            |
| .03          | ASP File Number          | The ASP FILE NUMBER field contains an existing LOCAL file number associated with this Audiology and Speech Pathology patient.                                                                                  |
| 1            | Initial Visit Date       | The INITIAL VISIT DATE field contains the date (if known) of this patient's first visit to the Audiology and/or Speech Pathology clinic at this site. This field can be left blank.                            |
| 2            | Diagnostic Condition     | The DIAGNOSTIC CONDITION field contains the <span id="p21_53" class="anchor"></span>ICD CM diagnostic condition code for the A&SP patient. Disease codes listed in this field appear in the A&SP Problem List. |
|              | .01 Diagnostic Condition | The DIAGNOSTIC CONDITION field contains the ICD CM diagnostic condition code for the A&SP patient. Disease codes listed in this field appear in the A&SP Problem List.                                         |
|              | 1 Date Condition Entered | The DATE CONDITION ENTERED field contains the date the DIAGNOSTIC CONDITION was entered for the A&SP patient. This field appears in the A&SP Problem List.                                                     |

### A&SP Clinic Visit file \#509850.6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The A&SP Clinic Visit file contains all data specific to each patient encounter. This includes the patient, the providers and students involved, the diagnostic and procedure codes, the date of the visit, procedure time, and the CDR cost account.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 23%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field #</strong></th>
<th><strong>Label</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.01</td>
<td>Name</td>
<td>The DATE field contains the encounter date or date and time.</td>
</tr>
<tr class="even">
<td>.07</td>
<td>Time Spent (minutes)</td>
<td>The TIME SPENT field is used to record the TOTAL number of minutes that were used during this clinic visit.</td>
</tr>
<tr class="odd">
<td>.08</td>
<td>Linked C&amp;P Exam</td>
<td>For C&amp;P exams, the LINKED C&amp;P EXAM field is automatically filled in by the QUASAR package. It provides a means of linking this QUASAR visit with a specific AMIE C&amp;P request. If the visit is not a C&amp;P exam this field is left blank.</td>
</tr>
<tr class="even">
<td>.09</td>
<td>C and P Status</td>
<td><p>The C AND P STATUS field indicates the status of the C&amp;P exam (if any).</p>
<p>0 stands for NOT A C&amp;P EXAM,</p>
<p>1 stands for NOT SIGNED OFF,</p>
<p>2 stands for AWAITING ADEQUATION, and</p>
<p>3 stands for COMPLETE.</p></td>
</tr>
<tr class="odd">
<td>.25</td>
<td>Secondary Provider</td>
<td>This is a multiple. If more than one provider was involved in this exam, the name(s) of the SECONDARY PROVIDER should be entered here. The SECONDARY PROVIDER field can be left blank.</td>
</tr>
<tr class="even">
<td>.27</td>
<td>*Lead Role</td>
<td>This field is starred for deletion.</td>
</tr>
<tr class="odd">
<td>1</td>
<td>Patient Name</td>
<td>The PATIENT NAME field contains the name of the patient seen during this clinic visit. This is a pointer to the Patient file #2.</td>
</tr>
<tr class="even">
<td>1.5</td>
<td>Age on Appointment</td>
<td>This is the patient's age.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Patient Eligibility Code</td>
<td>This is the Primary Eligibility of the patient.</td>
</tr>
<tr class="even">
<td>2.5</td>
<td>C and P</td>
<td>The C AND P field contains 0 or NO if this is not a C&amp;P exam. The field contains 1 or YES if this is a C&amp;P exam.</td>
</tr>
<tr class="odd">
<td>2.6</td>
<td>Clinic Location</td>
<td>The CLINIC LOCATION field is a pointer to the HOSPITAL LOCATION file (#44).</td>
</tr>
<tr class="even">
<td>2.7</td>
<td>Secondary Provider</td>
<td>This is the provider(s) not considered the primary provider.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Diagnostic Code</td>
<td>The DIAGNOSTIC CODE field is a pointer to the A&amp;SP DIAGNOSTIC CONDITION file (#509850.1).</td>
</tr>
<tr class="even">
<td></td>
<td>.01 Diagnostic Code</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>.12 Primary Diagnosis</td>
<td>YES or NO</td>
</tr>
<tr class="even">
<td></td>
<td>.15 *Modifier</td>
<td>This field starred for deletion.</td>
</tr>
<tr class="odd">
<td>4</td>
<td>Clinic Stop Code</td>
<td>The CLINIC STOP CODE field contains A for Audiology, S for Speech Pathology, AT for an Audiology Telephone visit and ST for Speech Telephone visit.</td>
</tr>
<tr class="even">
<td>4.01</td>
<td>Tone R500</td>
<td>The TONE R500 field indicates the patient's pure tone threshold at 500Hz.</td>
</tr>
<tr class="odd">
<td>4.02</td>
<td>Tone R1000</td>
<td>The TONE R1000 field indicates the pure tone threshold (Right) at 1000Hz for this patient.</td>
</tr>
<tr class="even">
<td>4.03</td>
<td>Tone R2000</td>
<td>The TONE R2000 field indicates the pure tone threshold (Right) at 2000Hz for this patient.</td>
</tr>
<tr class="odd">
<td>4.04</td>
<td>Tone R3000</td>
<td>The TONE R3000 field indicates the pure tone threshold (Right) at 3000Hz for this patient.</td>
</tr>
<tr class="even">
<td>4.05</td>
<td>Tone R4000</td>
<td>The TONE R4000 field indicates the pure tone threshold (Right) at 4000Hz for this patient.</td>
</tr>
<tr class="odd">
<td>4.06</td>
<td>Tone R Average</td>
<td>The TONE R AVERAGE field is the average pure tone threshold for this patient's right ear.</td>
</tr>
<tr class="even">
<td>4.07</td>
<td>Tone L500</td>
<td>The TONE L500 field indicates the patient's pure tone threshold at 500Hz.</td>
</tr>
<tr class="odd">
<td>4.08</td>
<td>Tone L1000</td>
<td>The TONE L1000 field indicates the pure tone threshold (Left) at 1000Hz for this patient.</td>
</tr>
<tr class="even">
<td>4.09</td>
<td>Tone L2000</td>
<td>The TONE L2000 field indicates the pure tone threshold (Left) at 2000Hz for this patient.</td>
</tr>
<tr class="odd">
<td>4.1</td>
<td>Tone L3000</td>
<td>The TONE L3000 field indicates the pure tone threshold (Left) at 3000Hz for this patient.</td>
</tr>
<tr class="even">
<td>4.11</td>
<td>Tone L4000</td>
<td>The TONE L4000 field indicates the pure tone threshold (Left) at 4000Hz for this patient.</td>
</tr>
<tr class="odd">
<td>4.12</td>
<td>Tone L Average</td>
<td>The TONE L AVERAGE field is the average pure tone threshold for this patient's left ear.</td>
</tr>
<tr class="even">
<td>4.13</td>
<td>CNC R</td>
<td>The CNC R field contains the patient's (Right) word recognition score for Maryland CNC material. This score is a percentage between 0 and 100.</td>
</tr>
<tr class="odd">
<td>4.14</td>
<td>CNC L</td>
<td>The CNC L field contains the patient's (Left) word recognition score for Maryland CNC material. This score is a percentage between 0 and 100.</td>
</tr>
<tr class="even">
<td>4.15</td>
<td>W22 R</td>
<td>The W22 R field contains the patient's (Right) word recognition score for CID W-22 material. This score is a percentage between 0 and 100.</td>
</tr>
<tr class="odd">
<td>4.16</td>
<td>W22 L</td>
<td>The W22 L field contains the patient's (Left) word recognition score for CID W-22 material. This score is a percentage between 0 and 100.</td>
</tr>
<tr class="even">
<td>4.17</td>
<td>Signature</td>
<td>For C&amp;P exams, the SIGNATURE field contains the electronic signature of the audiologist who completed the exam. When the exam is signed, it is released for adequation by the supervisor.</td>
</tr>
<tr class="odd">
<td>4.18</td>
<td>Date Signed</td>
<td>For C&amp;P exams, the DATE SIGNED field contains the date that the electronic signature was entered, thereby releasing the C&amp;P exam for adequation.</td>
</tr>
<tr class="even">
<td>4.19</td>
<td>Adequated By</td>
<td>The ADEQUATED BY field contains the electronic signature of the audiologist who adequated the clinic visit.</td>
</tr>
<tr class="odd">
<td>4.2</td>
<td>Date Adequated</td>
<td>The DATE ADEQUATED field contains the date that the electronic signature was entered for the adequation of this C&amp;P exam.</td>
</tr>
<tr class="even">
<td>4.23</td>
<td>Date of Audiometric Testing</td>
<td>When audiometric data are pulled from a past visit (i.e., testing is not done on the current date), the DATE OF AUDIOMETRIC TESTING field is filled with the date when actual testing was done.</td>
</tr>
<tr class="odd">
<td>4.24</td>
<td>Completer Title</td>
<td>For C&amp;P exams, the COMPLETER TITLE field contains the title of the audiologist who completed the exam.</td>
</tr>
<tr class="even">
<td>4.25</td>
<td>Adequator Title</td>
<td>For C&amp;P exams, the ADEQUATOR TITLE field contains the title of the audiologist who adequated the clinic visit.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>CDR Account</td>
<td>The CDR ACCOUNT field contains the CDR account number to be credited with this clinic visit.</td>
</tr>
<tr class="even">
<td>6</td>
<td>Primary Provider</td>
<td>The PRIMARY PROVIDER field contains the name of the primary A&amp;SP Provider who participated in this exam.</td>
</tr>
<tr class="odd">
<td>6.5</td>
<td>PCE Error</td>
<td>This multiple contains any error messages returned by PCE when this visit was transmitted via the Interface to PCE.</td>
</tr>
<tr class="even">
<td></td>
<td>.01 PCE Error</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>.02 PCE Field Name</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>.03 PCE Field Internal Value</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>.04 PCE Field External Value</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>1 PCE Error Message</td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Student</td>
<td>If a student or trainee participated in this exam, the name of the STUDENT should be entered here.</td>
</tr>
<tr class="even">
<td>8</td>
<td>*Other Provider</td>
<td>This field is starred for deletion.</td>
</tr>
<tr class="odd">
<td>8</td>
<td>*Disposition</td>
<td>This field is starred for deletion.</td>
</tr>
<tr class="even">
<td>10</td>
<td>Procedure Code</td>
<td>The PROCEDURE CODE field contains CPT-4 procedure codes and modifiers, if any, for this exam.</td>
</tr>
<tr class="odd">
<td></td>
<td>.01 Procedure</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>.02 *Modifier</td>
<td>Starred for deletion.</td>
</tr>
<tr class="odd">
<td></td>
<td>.03 Volume</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>.04 CPT Modifier</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>.05 Procedure Provider</td>
<td></td>
</tr>
<tr class="even">
<td>20</td>
<td>Service Connected</td>
<td>This prompt allows the user to indicate if the visit is Service Connected or not.</td>
</tr>
<tr class="odd">
<td>25</td>
<td>Agent Orange</td>
<td>Y or N indicates whether the visit is related to Agent Orange Exposure.</td>
</tr>
<tr class="even">
<td>30</td>
<td>Radiation</td>
<td>Y or N indicates whether the visit is related to Radiation Exposure.</td>
</tr>
<tr class="odd">
<td>35</td>
<td>Environmental Contaminants</td>
<td>Y or N indicates whether the visit is related to Environmental Contaminants Exposure.</td>
</tr>
<tr class="even">
<td>55</td>
<td>Appointment Time</td>
<td>The time the visit took place.</td>
</tr>
<tr class="odd">
<td>60</td>
<td>Division</td>
<td>This is the division at which the visit took place.</td>
</tr>
<tr class="even">
<td>80</td>
<td>Visit Eligibility</td>
<td>Only Eligibilities associated with the visit are valid for entry.</td>
</tr>
<tr class="odd">
<td>100</td>
<td>Review of Medical Records</td>
<td>Word Processing field.</td>
</tr>
<tr class="even">
<td>101</td>
<td>Medical History</td>
<td>Word Processing field.</td>
</tr>
<tr class="odd">
<td>102</td>
<td>Physical Examination</td>
<td>Word Processing field.</td>
</tr>
<tr class="even">
<td>103</td>
<td>Diagnostic and Clinical Tests</td>
<td>Word Processing field.</td>
</tr>
<tr class="odd">
<td>104</td>
<td>Diagnosis</td>
<td>Word Processing field.</td>
</tr>
<tr class="even">
<td>125</td>
<td>PCE Visit IEN</td>
<td>This is the IEN of the PCE visit passed back by the send to PCE processing.</td>
</tr>
<tr class="odd">
<td>135</td>
<td>Last Sent to PCE</td>
<td>The Date/Time that the system last attempted to send this data to PCE.</td>
</tr>
<tr class="even">
<td>140</td>
<td>Last Edited in QUASAR</td>
<td>This date is the date when the visit record was last edited in Quasar.</td>
</tr>
<tr class="odd">
<td>900</td>
<td>Exception Date</td>
<td>Set to NOW whenever the system determines that the Visit has become a PCE Exception.</td>
</tr>
</tbody>
</table>

## VA FileMan Sort and Print Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Print Options

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 20%" />
<col style="width: 28%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Formatting Codes</strong></th>
<th><strong>Examples</strong></th>
<th><strong>Explanations</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C</td>
<td>Column Assignment</td>
<td>FIRST PRINT FIELD: NAME;C10</td>
<td>Print NAME starting in Column 10</td>
</tr>
<tr class="even">
<td>S</td>
<td>Skip Lines</td>
<td>FIRST PRINT FIELD: NAME;S1</td>
<td>Skip 1 line before printing the next NAME</td>
</tr>
<tr class="odd">
<td>L</td>
<td>Left Justify</td>
<td>FIRST PRINT FIELD: PROVIDER;L8</td>
<td>Print only the first 8 characters of the PROVIDER name.</td>
</tr>
<tr class="even">
<td>R</td>
<td>Right Justify</td>
<td>FIRST PRINT FIELD: DATE;R30</td>
<td>Right justify the DATE 30 columns from the end of the last value plus 2 column spacers</td>
</tr>
<tr class="odd">
<td>W</td>
<td>Word Wrap</td>
<td>FIRST PRINT FIELD: MEDICAL HISTORY;W20</td>
<td>Wrap after 20 columns of text but will not split words</td>
</tr>
<tr class="even">
<td>D</td>
<td>Decimal Points</td>
<td>FIRST PRINT FIELD: COST;D2</td>
<td>Use two decimal places</td>
</tr>
<tr class="odd">
<td>N</td>
<td>No Repeat</td>
<td>FIRST PRINT FIELD: NAME;N</td>
<td>Will not repeat consecutive occurrence of the same name</td>
</tr>
<tr class="even">
<td>Y</td>
<td>Start at Row</td>
<td>FIRST PRINT FIELD: NAME;Y10</td>
<td>Start printing 10 rows from top of page</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>FIRST PRINT FIELD: NAME;Y-10</td>
<td>Start printing 10 rows from bottom of page</td>
</tr>
<tr class="even">
<td>@</td>
<td>Suppress Heading</td>
<td>HEADING: A&amp;SP… Replace @</td>
<td>Suppress the entire Heading (from the dash line up)</td>
</tr>
<tr class="odd">
<td>X</td>
<td>Suppress Spacing</td>
<td><p>FIRST PRINT FIELD: .01 NAME</p>
<p>THEN PRINT FIELD: SSN;X</p></td>
<td>Suppress spacing between the name and the SSN</td>
</tr>
<tr class="even">
<td>T</td>
<td>Print Title</td>
<td>FIRST PRINT FIELD: TIME SPENT;T</td>
<td>Print title (Time Spent in Minutes) as column header instead of label</td>
</tr>
<tr class="odd">
<td>" "</td>
<td>Print Different Header</td>
<td>FIRST PRINT FIELD: TIME SPENT;"Time"</td>
<td>Print Time as a column header rather than TIME SPENT</td>
</tr>
<tr class="even">
<td>_</td>
<td>Concatenate (Join)</td>
<td>FIRST PRINT FIELD: ADEQUATED BY_", "_ADEQUATOR TITLE</td>
<td>Joins field values with literals or other fields, i.e.… JOHN DOE, CHIEF</td>
</tr>
<tr class="odd">
<td>:</td>
<td>Forward Pointing</td>
<td><p>FIRST PRINT FIELD: NAME:</p>
<p>THEN PRINT PATIENT FIELD: SSN</p></td>
<td>Follows the NAME pointer field from the A&amp;SP Patient File to the Patient File to get the SSN</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Arithmetic Operators</strong></td>
<td><strong>Examples</strong></td>
<td><strong>Explanations</strong></td>
</tr>
<tr class="odd">
<td>!</td>
<td>Counts Any Field</td>
<td>FIRST PRINT FIELD: !NAME</td>
<td>Counts the entries that have values in the NAME field</td>
</tr>
<tr class="even">
<td>&amp;</td>
<td>Totals Numerics</td>
<td>FIRST PRINT FIELD: &amp;TIME SPENT/60;D1</td>
<td>Totals numeric fields; totals TIME SPENT and divides by 60 with 1 decimal place</td>
</tr>
<tr class="odd">
<td>+</td>
<td>Totals, Count &amp; Mean</td>
<td>FIRST PRINT FIELD: +TIME SPENT</td>
<td>Totals and Counts fields and provides a mean value</td>
</tr>
<tr class="even">
<td>#</td>
<td>Totals, Count, Mean, Minimum, Maximum, &amp; Standard Division</td>
<td>FIRST PRINT FIELD: #TIME SPENT</td>
<td>Totals and Counts fields and provides a minimum value and a maximum value found with the average value and standard deviation</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Binary Operators</strong></td>
<td><strong>Examples</strong></td>
<td><strong>Explanations</strong></td>
</tr>
<tr class="even">
<td>+</td>
<td>Addition</td>
<td>FIRST PRINT FIELD: &amp;TIME SPENT+600</td>
<td>Add 10 hours to the total TIME SPENT</td>
</tr>
<tr class="odd">
<td>-</td>
<td>Subtract</td>
<td>FIRST PRINT FIELD: &amp;TIME SPENT-600</td>
<td>Subtract 10 hours from total TIME SPENT</td>
</tr>
<tr class="even">
<td>*</td>
<td>Multiply</td>
<td>FIRST PRINT FIELD: &amp;TIME SPENT*.25</td>
<td>Multiply total TIME SPENT by .25</td>
</tr>
<tr class="odd">
<td>/</td>
<td>Divide</td>
<td>FIRST PRINT FIELD: &amp;TIME SPENT/60;D1</td>
<td>Divide total TIME SPENT by 60 to get total hours to 1 decimal place</td>
</tr>
<tr class="even">
<td>\</td>
<td>Integer Division</td>
<td>FIRST PRINT FIELD: &amp;TIME SPENT\60</td>
<td>Divide the TIME SPENT by 60 leaving off all remainders</td>
</tr>
</tbody>
</table>

#### Sort Options

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 19%" />
<col style="width: 29%" />
<col style="width: 46%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2"><strong>Formatting Codes</strong></td>
<td><strong>Examples</strong></td>
<td><strong>Explanations</strong></td>
</tr>
<tr class="even">
<td>C</td>
<td>Column Assignment</td>
<td>SORT BY: DATE;C30</td>
<td>Print DATE sub-header in column 30</td>
</tr>
<tr class="odd">
<td>S</td>
<td>Skip Lines</td>
<td>SORT BY: DATE;S2</td>
<td>Skip 2 lines before printing the next DATE sub-header</td>
</tr>
<tr class="even">
<td>L</td>
<td>Left Justify</td>
<td>SORT BY: PRIMARY PROVIDER;L10</td>
<td>Print only the first 10 characters of the PRIMARY PROVIDER as the sub-header</td>
</tr>
<tr class="odd">
<td>" "</td>
<td>Print Your Header</td>
<td>SORT BY: PRIMARY PROVIDER;"Provider: "</td>
<td>Prints Provider: as a sub-header rather than PRIMARY PROVIDER</td>
</tr>
<tr class="even">
<td>@</td>
<td>Suppress Sub-Header</td>
<td>SORT BY: @DATE</td>
<td>Sorts by the selected Field (DATE) but suppresses the sub-header</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Sort Functions</strong></td>
<td><strong>Examples</strong></td>
<td><strong>Explanations</strong></td>
</tr>
<tr class="even">
<td>!</td>
<td>Ranking Numbers</td>
<td>SORT BY: !DATE</td>
<td>Items printed under DATE sub-header will have ranking numbers</td>
</tr>
<tr class="odd">
<td>+</td>
<td>Sub Totals</td>
<td>SORT BY: +NAME</td>
<td>All print fields with !,&amp;,+,or # will be sub-totaled at each new NAME</td>
</tr>
<tr class="even">
<td>#</td>
<td>Form Feed</td>
<td>SORT BY: #PRIMARY PROVIDER</td>
<td>A form feed will be generated for each new PRIMARY PROVIDER</td>
</tr>
<tr class="odd">
<td>-</td>
<td>Reverse Order</td>
<td>SORT BY: -DATE</td>
<td>Will reverse order of print from lowest-highest to highest-lowest order</td>
</tr>
<tr class="even">
<td>'</td>
<td>Select Entries</td>
<td>SORT BY: 'DATE</td>
<td>Select items only, rather than selects and sorts</td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Special Features</strong></td>
<td><strong>Examples</strong></td>
<td><strong>Explanations</strong></td>
</tr>
<tr class="even">
<td>@</td>
<td>at START WITH prompt</td>
<td><p>SORT BY: DATE SIGNED</p>
<p>START WITH DATE SIGNED: @</p></td>
<td>Prints all entries with a value in the DATE SIGNED field first followed by null values for that field</td>
</tr>
<tr class="odd">
<td>@</td>
<td>at the START WITH and GO TO prompt</td>
<td><p>SORT BY: DATE SIGNED</p>
<p>START WITH DATE SIGNED: @</p>
<p>GO TO DATE SIGNED: @</p></td>
<td>Prints only entries with null values in the DATE SIGNED field</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Templates</strong></td>
<td><strong>Examples</strong></td>
<td><strong>Explanations</strong></td>
</tr>
<tr class="odd">
<td>]</td>
<td>Forces FileMan to offer a template prompt</td>
<td><p>SORT BY: ]</p>
<p>FIRST PRINT FIELD: ]</p></td>
<td>Forces FileMan to offer you a template</td>
</tr>
<tr class="even">
<td>[</td>
<td>Used to call a template</td>
<td><p>SORT BY: [A&amp;SP ...</p>
<p>FIRST PRINT FIELD: [A&amp;SP ...</p></td>
<td>Calls a previously created template; i.e. sort or print template named A&amp;SP ...</td>
</tr>
<tr class="odd">
<td>[?</td>
<td>Will show all templates available to the user</td>
<td><p>SORT BY: [?</p>
<p>FIRST PRINT FIELD: [?</p></td>
<td>Shows all sort or print templates</td>
</tr>
<tr class="even">
<td>^</td>
<td>Inserts</td>
<td><p>THEN PRINT FIELD: PATIENT NAME//^SSN</p>
<p>THEN PRINT FIELD: PATIENT NAME//</p></td>
<td>Inserts a field before another field</td>
</tr>
<tr class="odd">
<td>@</td>
<td>Deletes</td>
<td>THEN PRINT FIELD: SSN//@</td>
<td>Deletes a field</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Boolean Logic</strong></td>
<td><strong>Examples</strong></td>
<td><strong>Explanations</strong></td>
</tr>
<tr class="odd">
<td>=</td>
<td>Equal</td>
<td>SORT BY: PROCEDURE CODE=92507</td>
<td>Finds all instances of PROCEDURE CODE equal to 92507</td>
</tr>
<tr class="even">
<td>&gt;</td>
<td>Greater Than</td>
<td>SORT BY: TIME SPENT&gt;30</td>
<td>Finds all instances where TIME SPENT was greater than 30 minutes</td>
</tr>
<tr class="odd">
<td>&lt;</td>
<td>Less Than</td>
<td>SORT BY: TIME SPENT&lt;30</td>
<td>Finds all instances where TIME SPENT was less than 30 minutes</td>
</tr>
<tr class="even">
<td>[</td>
<td>Contains</td>
<td>SORT BY: PATIENT NAME["AR"</td>
<td>Finds all patients with AR in their names</td>
</tr>
<tr class="odd">
<td>]</td>
<td>Follows</td>
<td>SORT BY: PATIENT NAME]"ST"</td>
<td>Finds all patients whose names begin with ST to the end of the alphabet</td>
</tr>
<tr class="even">
<td>!</td>
<td>OR</td>
<td>SORT BY: TIME SPENT&lt;10!(TIME SPENT&gt;60)</td>
<td>Finds all instances where TIME SPENT was less than 10 minutes OR greater than 60 minutes</td>
</tr>
<tr class="odd">
<td>&amp;</td>
<td>AND</td>
<td>SORT BY: PRIMARY PROVIDER="ACKQ,PROVIDER1"&amp;(TIME SPENT&gt;120)</td>
<td>Finds all instances where PRIMARY PROVIDER ACKQ, PROVIDER1 spent greater than 2 hours on a visit.</td>
</tr>
<tr class="even">
<td>'</td>
<td>NEGATE</td>
<td>SORT BY: 'TIME SPENT&gt;30</td>
<td>Finds all instances where TIME SPENT is NOT greater than 30</td>
</tr>
</tbody>
</table>

## Writing Your Own Tailor-Made Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tailor-Made A&SP Reports is an option on the A&SP Reports menu in the Audiology & Speech Visit Tracking System menu. The option prompts you to sort from the A&SP Patient file (#905850.2) or the A&SP Clinic Visit file (#905850.6). VA FileMan defaults are always followed by the // symbol. The default file is the A&SP CLINIC VISIT file. See [Data Dictionaries](#data-dictionaries) for a listing of the fields in the two files.

You can enter the field name or number in sort or print logic. When performing some arithmetic operations, you must specify the field name. For example, if you want to convert TIME SPENT (minutes) into hours, you would write TIME SPENT/60. Dividing the field number (.07) by 60 will not work.

Tailor-Made A&SP Reports allows you to store your sort logic in templates. VA FileMan prompts you for a template name when you enter new sorting logic. The saved template can be called up by entering the template name enclosed in brackets (e.g., \[PATIENT LIST\]) at the first “SORT BY:” prompt. The list of stored templates can be called up by entering \[?. Print logic cannot be stored by the Tailor-Made A&SP Reports option. Print logic must be entered each time the report is run. Neither the sort logic nor the print logic can be edited. If you make a mistake while entering sort logic, exit by pressing the ^ key (shift-6). If you want to change the sort logic after you have saved a template, a new template can be saved with the same or a different template name. If you save a template with a template name that already exists, VA FileMan will warn you that the template exists and will ask if you wish to overwrite the existing template.

VA FileMan also allows you to specify ranges for sorted data. Ranges permit flexibility and repeated use of the same sort logic when using templates. A FileMan will prompt you for those data fields for which you want to enter ranges. For example, if you sort by DATE, you will be asked:

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO//

In most cases, you should enter a range for each sort value during the initial run of the sorting routine. This will force VA FileMan to ask if you want the user to" be asked a 'From – To' range" when using the template. If you want a range for the data, answer YES to the prompt; otherwise answer NO.

## Examples of Tailor-Made A&SP Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains some examples of tailor-made reports. In the following examples, text to be entered is highlighted in boldface type. Explanatory information is italicized and enclosed in brackets \[ \]. Data fields followed by slant bars // are defaults. The symbol \<RET\> means press the return or enter key. If you specify visit date by its field name, DATE, you will be shown four date fields from which to select. DATE is the clinic visit date. The visit date is uniquely specified by its field number, .01.

Notes:

1.  There are several fields for capturing provider (Primary Provider, Secondary Provider, Student, and Procedure Provider). If you want the Primary Provider for the visit, use the Primary Provider field. If you want to capture discrete data on providers for each procedure done during the visit, use the Procedure Provider field found under the Procedure multiple. Examples of the use of providers from both fields follow.
2.  Data can be obtained by Division if your site parameters are set up by Division. You may want to sort by Division at the beginning of each report to get only data from your Division.
3.  Some fields have been changed or added since the last release. If you created any sort or print templates, you should review those for any necessary changes.

### Report \#1: Student Cost Distribution Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To print out procedure time by CDR account for each student. This program returns the procedure time by date and student for each CDR account and totals the procedure time. You must calculate subtotals of CDR accounts (e.g., 1100-series, 1200-series) for entry into the QUASAR A&SP Service CDR.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// +CDR ACCOUNT

START WITH CDR ACCOUNT: FIRST// \<RET\>

WITHIN CDR ACCOUNT, SORT BY: STUDENT

START WITH STUDENT: FIRST// \<RET\>

WITHIN STUDENT, SORT BY: DATE

1 DATE

2 DATE ADEQUATED

3 DATE OF AUDIOMETRIC TESTING

4 DATE SIGNED

CHOOSE 1-4: 1 DATE

START WITH DATE: FIRST// \[Enter beginning date of range\]

GO TO DATE: LAST// \[Enter ending date of range\]

WITHIN DATE, SORT BY: \<RET\>

STORE IN 'SORT' TEMPLATE: \[Enter a name for your template\]

Are you adding 'TEMPLATE NAME' as

a new SORT TEMPLATE? No// \<RET\> (Yes)

DESCRIPTION:

1\> You may enter a description of the template here.

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO// YES

FIRST PRINT FIELD: CDR ACCOUNT;C1;L10;N

THEN PRINT FIELD: STUDENT;C13;L15;N

THEN PRINT FIELD: .01;C31;L12;N DATE

THEN PRINT FIELD: +(TIME SPENT/60);C46;L6;"TIME (HRS)"

THEN PRINT FIELD: \<RET\>

DEVICE: \[Select a print device\]

Notes:

1.  If you want to display procedure time in minutes, the last print command should be entered as: +.07;C46;L6;"TIME (MIN)".
2.  A&SP Service CDR requires that you add all student hours for each of the 1100-series, 1200-series, 1300-series, 1400-series, 1600-series, and 2800-series accounts. The cost account totals are the training (.12) data required by the QUASAR A&SP Service CDR .
3.  The Student CDR assumes 100% supervision.

> Example

A&SP CLINIC VISIT STATISTICS NOV 13,1995 13:27 PAGE 1

CDR TIME

ACCOUNT STUDENT DATE (HRS)

---------------------------------------------------------------------------------------------------------------------------------------

1110.00 QUASARPROVIDER,THREE OCT 6,1995 .25

OCT 14,1995 .75

OCT 21,1995 1.5

OCT 30,1995 .5

QUASARPROVIDER,FOUR OCT 13,1995 1

OCT 14,1995 .5

OCT 17,1995 .5

OCT 23,1995 1

OCT 26,1995 .5

QUASARPROVIDER,FIVE OCT 6,1995 2

OCT 13,1995 .5

OCT 14,1995 .5

OCT 17,1995 .75

OCT 18,1995 .5

.75

OCT 23,1995 1.5

------

SUBTOTAL 13

SUBCOUNT 16

SUBMEAN 0.81

1111.00 QUASARPROVIDER,THREE OCT 19,1995 .75

------

SUBTOTAL .75

SUBCOUNT 1

SUBMEAN 0.75

1211.00 OCT 15,1995 1

QUASARPROVIDER,FOUR OCT 5,1995 .5

.5

OCT 7,1995 2

OCT 9,1995 .75

OCT 10,1995 2

75

OCT 12,1995 .75

------

SUBTOTAL 8.25

SUBCOUNT 8

SUBMEAN 1.03

------

TOTAL 22

COUNT 25

MEAN 0.88

### Report \#2: Patient Addresses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To print names and addresses of patients for database or mailing purposes.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// @DATE

1 DATE

2 DATE ADEQUATED

3 DATE OF AUDIOMETRIC TESTING

4 DATE SIGNED

CHOOSE 1-4: 1 DATE

START WITH DATE: FIRST// \[Instead of accepting the default, specify a date range if you always would like to be asked for a range\]

GO TO DATE: LAST// \[Enter an ending date\]

WITHIN DATE, SORT BY: @CLINIC STOP CODE

START WITH CLINIC STOP CODE: FIRST// ??

The CLINIC STOP CODE field contains A for Audiology, S for Speech

Pathology, AT for an Audiology Telephone visit and ST for Speech

Telephone visit.

Choose from:

A AUDIOLOGY

S SPEECH

AT TELEPHONE AUDIOLOGY

ST TELEPHONE SPEECH

START WITH CLINIC STOP CODE: FIRST// A AUDIOLOGY

GO TO CLINIC STOP CODE: LAST// A AUDIOLOGY

WITHIN CLINIC STOP CODE, SORT BY:

STORE IN 'SORT' TEMPLATE: \[Enter a name for your template\]

DESCRIPTION:

1\> Enter a description.

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO// \<RET\>YES

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'CLINIC STOP CODE'? NO// \<RET\>YES

FIRST PRINT FIELD: PATIENT NAME:

THEN PRINT A&SP PATIENT FIELD: NAME:

THEN PRINT PATIENT FIELD: NAME;S1;"";C35

THEN PRINT PATIENT FIELD: STREET ADDRESS \[LINE 1\];C35;""

THEN PRINT PATIENT FIELD: CITY\_", "\_STATE\_" "\_ZIP CODE;C35;""

THEN PRINT PATIENT FIELD: \<RET\>

THEN PRINT A&SP PATIENT FIELD: \<RET\>

THEN PRINT FIELD: \<RET\>

DEVICE: \[Select Print Device\]

> **NOTE:** This routine makes use of forward pointing commands to extract patient data from the MAS Patient file (#2). Because the patient’s name is identified, some patient data not entered into QUASAR may be accessed, sorted, and printed.

Example

A&SP CLINIC VISIT LIST NOV 13,1995 13:12 PAGE 1

---------------------------------------------------------------------------------------------------------------------------------------

QUASARPATIENT,TEN

666 ANY DRIVE

ANYWHERE, ILLINOIS 60611

QUASARPATIENT1,ONE

10 ANY LANE

SOMEWHERE, ILLINOIS 60623

### Report \#3: Visit Report (Provider/Time Spent/Diagnostic Code)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To print a list of patient names, primary provider, procedure times, and <span id="p21_68" class="anchor"></span>ICD CM codes by visit date.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// \<RET\>

START WITH DATE: FIRST// \[Enter a beginning date\]

GO TO DATE: LAST// \[Enter an ending date\]

WITHIN DATE, SORT BY: PATIENT NAME

START WITH PATIENT NAME: FIRST// \<RET\>

WITHIN PATIENT NAME, SORT BY: \<RET\>

FIRST PRINT FIELD: PATIENT NAME;L20;S1

THEN PRINT FIELD: .01;C24;L15 DATE

THEN PRINT FIELD: PRIMARY PROVIDER;C42;L20

THEN PRINT FIELD: TIME SPENT;C65;L3 (minutes)

THEN PRINT FIELD: DIAGNOSTIC CODE (multiple)

THEN PRINT DIAGNOSTIC CODE SUB-FIELD: DIAGNOSTIC CODE;C71;L8

THEN PRINT DIAGNOSTIC CODE SUB-FIELD: \<RET\>

THEN PRINT FIELD: \<RET\>

DEVICE: \[Select Print Device\]

> Example

A&SP CLINIC VISIT LIST NOV 22,1999 13:22 PAGE 1

TIME

SPENT

PATIENT NAME DATE PRIMARY PROVIDER (minutes)

DIAGNOSTIC

CODE

---------------------------------------------------------------------------------------------------------------------------------------

QUASARPATIENT1,TWO AUG 16,1999 QUASARPROVIDER,SIX 30 388.12

QUASARPATIENT1,THREE AUG 16,1999 QUASARPROVIDER,SIX 25 388.1

### Report \#4: Visit Report (Procedure Code/Cost)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To print a list of patient names, CPT-4 codes, and costs by clinic stop and date. Report also calculates the total cost, number of procedures, and the mean procedure cost.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// \<RET\>

START WITH DATE: FIRST// \[Enter a beginning date\]

GO TO DATE: LAST// \[Enter an ending date\]

WITHIN DATE, SORT BY: PROCEDURE CODE (multiple)

PROCEDURE CODE SUB-FIELD: PROCEDURE CODE:

A&SP PROCEDURE CODE FIELD: CLINIC STOP

START WITH CLINIC STOP: FIRST// \<RET\>

WITHIN CLINIC STOP, SORT BY: PATIENT NAME

START WITH PATIENT NAME: FIRST// \<RET\>

WITHIN PATIENT NAME, SORT BY: \<RET\>

STORE IN 'SORT' TEMPLATE: \[Enter a template name\]

Are you adding 'TEMPLATE NAME' as

a new SORT TEMPLATE? No// Y (Yes)

DESCRIPTION:

1\>\<RET\>

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO// \<RET\>YES

FIRST PRINT FIELD: PROCEDURE CODE (multiple)

FIRST PRINT PROCEDURE CODE SUB-FIELD: PROCEDURE CODE:

THEN PRINT A&SP PROCEDURE CODE FIELD: CLINIC STOP;N

THEN PRINT A&SP PROCEDURE CODE FIELD: \<RET\>

THEN PRINT PROCEDURE CODE SUB-FIELD: \<RET\>

THEN PRINT FIELD: PATIENT NAME;C20;L20

THEN PRINT FIELD: DATE;C43;L14

1 DATE

2 DATE ADEQUATED

3 DATE OF AUDIOMETRIC TESTING

4 DATE SIGNED

CHOOSE 1-4: 1 DATE

THEN PRINT FIELD: PROCEDURE CODE (multiple)

THEN PRINT PROCEDURE CODE SUB-FIELD: PROCEDURE CODE;C60;L7

THEN PRINT PROCEDURE CODE SUB-FIELD: PROCEDURE CODE:

THEN PRINT A&SP PROCEDURE CODE FIELD: +COST;C70

THEN PRINT A&SP PROCEDURE CODE FIELD: \<RET\>

THEN PRINT PROCEDURE CODE SUB-FIELD: \<RET\>

THEN PRINT FIELD: \<RET\>

DEVICE: \[Enter a device\]

> Example

A&SP CLINIC VISIT STATISTICS NOV 13,1995 15:15 PAGE 1

CLINIC PROCEDURE

STOP PATIENT NAME DATE CODE COST

---------------------------------------------------------------------------------------------------------------------------------------

AUDIOLOGY QUASARPATIENT1,FOUR OCT 5,1995 92557 80.00

92599 20.00

QUASARPATIENT1,FIVE OCT 6,1995 92557 80.00

92567 30.00

92568 30.00

SPEECH QUASARPATIENT1,SIX OCT 20,1995 92507 75.00

QUASARPATIENT1,SEVEN OCT 10,1995 74230 225.00

--------

TOTAL 540.00

COUNT 7

MEAN 77.14

### Report \#5: Visit Report (Procedure Time)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To print a list of procedure times by provider and date. Report also calculates total procedure time for all providers.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// PROCEDURE CODE (multiple)

PROCEDURE CODE SUB-FIELD: PROCEDURE PROVIDER;S

START WITH PROCEDURE PROVIDER: FIRST// \<RET\>

WITHIN PROCEDURE PROVIDER, SORT BY: DATE

1 DATE

2 DATE ADEQUATED

3 DATE OF AUDIOMETRIC TESTING

4 DATE SIGNED

CHOOSE 1-4: 1 DATE

START WITH DATE: FIRST// \[Enter a beginning date\]

GO TO DATE: LAST// \[Enter an ending date\]

WITHIN DATE, SORT BY: \<RET\>

STORE IN 'SORT' TEMPLATE: \[Enter a template name\]

Are you adding 'TEMPLATE NAME' as a new SORT TEMPLATE? No// Y (Yes)

DESCRIPTION:

No existing text

Edit? NO// \<RET\>

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO// YES

FIRST PRINT FIELD: PROCEDURE CODE (multiple)

FIRST PRINT PROCEDURE CODE SUB-FIELD: PROCEDURE PROVIDER;N

THEN PRINT PROCEDURE CODE SUB-FIELD: \<RET\>

THEN PRINT FIELD: DATE

1 DATE

2 DATE ADEQUATED

3 DATE OF AUDIOMETRIC TESTING

4 DATE SIGNED

CHOOSE 1-4: 1 DATE

THEN PRINT FIELD: &TIME SPENT;"TIME" (minutes)

THEN PRINT FIELD: \<RET\>

DEVICE: \[Enter a device\]

> Example

A&SP CLINIC VISIT STATISTICS NOV 23,1999 10:18 PAGE 1

PROCEDURE PROVIDER DATE TIME

---------------------------------------------------------------------------------------------------------------------------------------

QUASARPROVIDER,SEVEN NOV 10,1999 30

NOV 10,1999 30

NOV 10,1999 30

NOV 15,1999 30

NOV 18,1999 90

NOV 22,1999 60

QUASARPROVIDER,EIGHT NOV 19,1999 30

QUASARPROVIDER,NINE NOV 10,1999 30

NOV 10,1999 30

NOV 22,1999 60

QUASARPROVIDER,TEN NOV 18,1999 60

NOV 18,1999 90

QUASARPROVIDER1,ONE NOV 22,1999 60

----

TOTAL 630

### Report \#6: C&P Examinations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To provide a list of patients seen for C&P exams by date and primary provider.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// C AND P

1 C AND P

2 C AND P STATUS

CHOOSE 1-2: 1 C AND P

START WITH C AND P: FIRST// \<RET\>

WITHIN C AND P, SORT BY: DATE

1 DATE

2 DATE ADEQUATED

3 DATE OF AUDIOMETRIC TESTING

4 DATE SIGNED

CHOOSE 1-4: 1 DATE

START WITH DATE: FIRST// \[Enter a beginning date\]

GO TO DATE: LAST// \[Enter an ending date\]

WITHIN DATE, SORT BY: PATIENT NAME

START WITH PATIENT NAME: FIRST// \<RET\>

WITHIN PATIENT NAME, SORT BY: PRIMARY PROVIDER

START WITH PRIMARY PROVIDER: FIRST// \<RET\>

WITHIN PRIMARY PROVIDER, SORT BY: \<RET\>

STORE IN 'SORT' TEMPLATE: \[Enter a template name\]

Are you adding 'TEMPLATE NAME' as a new SORT TEMPLATE? No// Y (Yes)

DESCRIPTION:

1\>\<RET\>

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO// \<RET\>YES

FIRST PRINT FIELD: PRIMARY PROVIDER;L20;N

THEN PRINT FIELD: .01;C25 DATE

THEN PRINT FIELD: PATIENT NAME;C40;L25

THEN PRINT FIELD: !C AND P;C70;"C&P"

THEN PRINT FIELD: \<RET\>

DEVICE: \[Enter a device\]

> Example

A&SP CLINIC VISIT STATISTICS NOV 23,1999 12:20 PAGE 1

PRIMARY PROVIDER DATE

PATIENT NAME C&P

---------------------------------------------------------------------------------------------------------------------------------------

QUASARPROVIDER,NINE AUG 16,1999 QUASARPATIENT2,EIGHT YES

AUG 31,1999 QUASARPATIENT2,NINE YES

OCT 7,1999 QUASARPATIENT2,TEN YES

QUASARPROVIDER1,TWO OCT 12,1999 QUASARPATIENT2,EIGHT YES

QUASARPROVIDER,NINE OCT 22,1999 QUASARPATIENT3,ONE YES

NOV 18,1999 QUASARPATIENT3,TWO YES

NOV 18,1999 QUASARPATIENT2,EIGHT YES

---

COUNT 7

### Report \#7: Visit Report (Procedure Codes/Date and Provider)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To print patient names, primary providers, and procedure code by date. This report is useful for validating data and for searching the QUASAR database for procedure codes or patients which were entered in error or missed.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// \<RET\>

START WITH DATE: FIRST// \[Enter a beginning date\]

GO TO DATE: LAST// \[Enter an ending date\]

WITHIN DATE, SORT BY: PATIENT NAME

START WITH PATIENT NAME: FIRST// \<RET\>

WITHIN PATIENT NAME, SORT BY: PRIMARY PROVIDER

START WITH PRIMARY PROVIDER: FIRST// \<RET\>

WITHIN PRIMARY PROVIDER, SORT BY: \<RET\>

STORE IN 'SORT' TEMPLATE: \[Enter a template name\]

Are you adding 'TEMPLATE NAME' as a new SORT TEMPLATE? No// Y (Yes)

DESCRIPTION:

1\>\<RET\>

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO// \<RET\>YES

FIRST PRINT FIELD: PATIENT NAME;C1;S1;L20

THEN PRINT FIELD: PRIMARY PROVIDER;C25;L20;N

THEN PRINT FIELD: .01;C50;N DATE

THEN PRINT FIELD: PROCEDURE CODE (multiple)

THEN PRINT PROCEDURE CODE SUB-FIELD: PROCEDURE CODE;C70

THEN PRINT PROCEDURE CODE SUB-FIELD: \<RET\>

THEN PRINT FIELD: \<RET\>

DEVICE: \[Enter a device\]

> Example

A&SP CLINIC VISIT LIST NOV 23,1999 12:31 PAGE 1

PROCEDURE

PATIENT NAME PRIMARY PROVIDER DATE CODE

---------------------------------------------------------------------------------------------------------------------------------------

QUASARPATIENT1,EIGHT QUASARPROVIDER,SIX AUG 16,1999 92511

QUASARPATIENT1,NINE 92511

QUASARPATIENT1,TEN 92511

QUASARPATIENT2,ONE 92511

QUASARPATIENT2,TWO 92511

QUASARPATIENT2,THREE 92511

QUASARPATIENT2,FOUR QUASARPROVIDER,NINE 92506

### Report \#8: ASHA Data on Trainees

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To print a list of procedure times by student and date.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// \#STUDENT

START WITH STUDENT: FIRST// \<RET\>

WITHIN STUDENT, SORT BY: DATE

1 DATE

2 DATE ADEQUATED

3 DATE OF AUDIOMETRIC TESTING

4 DATE SIGNED

CHOOSE 1-4: 1 DATE

START WITH DATE: FIRST// \[Enter a beginning date\]

GO TO DATE: LAST// \[Enter an ending date\]

WITHIN DATE, SORT BY: \<RET\>

STORE IN 'SORT' TEMPLATE: \[Enter a template name\]

Are you adding 'TEMPLATE NAMES' as a new SORT TEMPLATE? No// Y (Yes)

DESCRIPTION:

1\>\<RET\>

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO// \<RET\>YES

FIRST PRINT FIELD: STUDENT;C1;N;L20

THEN PRINT FIELD: .01;C25 DATE

THEN PRINT FIELD: DIAGNOSTIC CODE (multiple)

THEN PRINT DIAGNOSTIC CODE SUB-FIELD: DIAGNOSTIC CODE;C40

THEN PRINT DIAGNOSTIC CODE SUB-FIELD: \<RET\>

THEN PRINT FIELD: PROCEDURE CODE (multiple)

THEN PRINT PROCEDURE CODE SUB-FIELD: PROCEDURE CODE;C50

THEN PRINT PROCEDURE CODE SUB-FIELD: \<RET\>

THEN PRINT FIELD: TIME SPENT;C65 (minutes)

THEN PRINT FIELD: \<RET\>

DEVICE: \[Enter a device\]

> Example

A&SP CLINIC VISIT LIST NOV 13,1995 09:54 PAGE 1

STUDENT DATE DIAGNOSTIC

CODE TIME

PROCEDURE SPENT

CODE (minutes)

---------------------------------------------------------------------------------------------------------------------------------------

QUASARPROVIDER1,THREE OCT 6,1995 389.10 92557 90

92567

92568

92599

### Report \#9: Procedure Time Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To print a list of procedure times for a specified procedure. The report also provides descriptive statistics on procedure times. This report is useful for analyzing product lines and standardizing procedure times for DSS.

> **NOTE:** This report is designed to analyze procedure time for a single specified procedure code. It uses the Primary Provider instead of the Procedure Provider field.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// @DATE

1 DATE

2 DATE ADEQUATED

3 DATE OF AUDIOMETRIC TESTING

4 DATE SIGNED

CHOOSE 1-4: 1 DATE

START WITH DATE: FIRST// \[Enter a beginning date\]

GO TO DATE: LAST// \[Enter an ending date\]

WITHIN DATE, SORT BY: PROCEDURE CODE (multiple)

PROCEDURE CODE SUB-FIELD: PROCEDURE CODE

START WITH PROCEDURE CODE: FIRST// \[Enter code to be sorted\]

GO TO PROCEDURE CODE: LAST// \[Enter same code\]

WITHIN PROCEDURE CODE, SORT BY: START WITH DATE: FIRST// \[Enter a beginning date\]

GO TO DATE: LAST// \[Enter an ending date\]

STORE IN 'SORT' TEMPLATE: \[Enter a template name\]

Are you adding 'TEMPLATE NAMES' as a new SORT TEMPLATE? No// Y (Yes)

DESCRIPTION:

1\>\<RET\>

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO// YES

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'PROCEDURE CODE'? NO// YES

FIRST PRINT FIELD: PROCEDURE CODE (multiple)

FIRST PRINT PROCEDURE CODE SUB-FIELD: PROCEDURE CODE;C1

THEN PRINT PROCEDURE CODE SUB-FIELD: \<RET\>

THEN PRINT FIELD: PRIMARY PROVIDER;C20;N

THEN PRINT FIELD: \#TIME SPENT;C40 (minutes)

THEN PRINT FIELD: \<RET\>

DEVICE: \[Enter a device\]

> Example

A&SP CLINIC VISIT STATISTICS NOV 13,1995 10:28 PAGE 1

PROCEDURE PRIMARY PROVIDER TIME

CODE SPENT

(minutes)

---------------------------------------------------------------------------------------------------------------------------------------

92507 QUASARPROVIDER1,FOUR 30

92507 30

92507 30

92507 45

92507 45

92507 QUASARPROVIDER1,FIVE 45

92507 45

----

TOTAL 270

COUNT 7

MEAN 39

MINIMUM 30

MAXIMUM 45

DEV. 8

### Report \#10: Clinic Management Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Objective: To provide a report of patient names, procedures, and procedure times by provider.

Select A&SP Reports Option: Tailor-Made A&SP Reports

Print From Which File: (P/V): V// \<RET\>isit

SORT BY: DATE// @DATE

1 DATE

2 DATE ADEQUATED

3 DATE OF AUDIOMETRIC TESTING

4 DATE SIGNED

CHOOSE 1-4: 1 DATE

START WITH DATE: FIRST// {Enter a beginning date\]

GO TO DATE: LAST// \[Enter an ending date\]

WITHIN DATE, SORT BY: @CLINIC LOCATION

START WITH CLINIC LOCATION: FIRST// \[Enter a clinic location\]

GO TO CLINIC LOCATION: LAST// \[Enter the same clinic location\]

WITHIN CLINIC LOCATION, SORT BY: \<RET\>

STORE IN 'SORT' TEMPLATE: \[Enter a template name\]

Are you adding 'TEMPLATE NAME' as a new SORT TEMPLATE? No// Y (Yes)

DESCRIPTION:

1\>\<RET\>

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'DATE'? NO// YES

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'CLINIC LOCATION'? NO// YES

FIRST PRINT FIELD: PRIMARY PROVIDER;C1;L20

THEN PRINT FIELD: PATIENT NAME;C30

THEN PRINT FIELD: PROCEDURE CODE (multiple)

THEN PRINT PROCEDURE CODE SUB-FIELD: PROCEDURE CODE;C55

THEN PRINT PROCEDURE CODE SUB-FIELD: \<RET\>

THEN PRINT FIELD: TIME SPENT;C65 TIME SPENT (minutes)

THEN PRINT FIELD: \<RET\>

DEVICE: \[Enter a device\]

> Example

A&SP CLINIC VISIT LIST NOV 23,1999 13:51 PAGE 1

PRIMARY PROVIDER PATIENT NAME

TIME

PROCEDURE SPENT

CODE (minutes)

---------------------------------------------------------------------------------------------------------------------------------------

QUASARPROVIDER,NINE QUASARPATIENT2,FIVE 92506 30

QUASARPROVIDER1,EIGHT QUASARPATIENT2,SIX 92506 100

QUASARPATIENT2,SIX 92506 120

QUASARPROVIDER,NINE QUASARPATIENT2,SEVEN 92511 10<span id="_Toc156098055" class="anchor"></span>

QUASAR Audiogram Module

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

QUASAR (Quality: Audiology and Speech Analysis and Reporting) is a VistA software package written for the Audiology and Speech Pathology Service (ASPS). QUASAR is used to enter, edit, and retrieve data for each audiometric exam of a patient and provides for the transmission of this data to various programs.

Patch ACKQ\*3.0\*13 adds the ability to retrieve data directly from certain audiometric devices, and combines the Edit and Display components into one application. Recommended users (not doing data entry or capture), can use the Graph Display tab to view a graphic display of a record.

The QUASAR Audiogram Module is a Windows-based GUI interface, developed to simplify and enhance the entry, display, and use of information obtained during an audiometric exam of a patient.

The Audiogram Edit component (ACKQROES3E.exe) is a Windows-based software application that allows clinicians to enter, edit, and view a patient's audiometric exam record and a patient's audiogram graph. You access the component from the Computerized Patient Record System (CPRS) Tools menu.

The QUASAR Audiogram Module includes components that reside on two systems: the local facility VistA system and the Denver Acquisition & Logistics Center (Denver ALC) system. The local facility components include a VistA file, 'M' routines and options, remote procedure calls, and a Delphi executable. The Denver ALC ROES\*3.0 (Remote Order Entry System) order processing application incorporates patient-specific audiometric information that is taken from data transmitted to a national database from the QUASAR Audiogram Module. The information is used by vendors to produce customized hearing related items.

## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Related documentation is located in the VistA Document Library:

<http://www.va.gov/vdl/>

*QUASAR Audiogram Module Release Notes* for Patch ACKQ\* 3.0\*13

*QUASAR Audiogram Module Installation and Implementation Guid*e for Patch ACKQ\* 3.0\*13

*QUASAR Audiogram Module Technical Manual and Package Security Guide* for  
Patch ACKQ\* 3.0\*13

## Conventions Used

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The QUASAR GUI uses a Microsoft Windows-style graphical interface with typical navigation and conventions[^12].

- Altered data is used in all screen captures in the user manual; this includes the names of patients and providers, patient information, and audiometric test results. The examples are representative of the features of the application.
- Use the Tab-key, right and left arrows, or mouse point/click to navigate the fields on each tab.
- You can access editable fields, tab pages and menu options using shortcut key combinations, such as Alt +, Ctrl +, and F-key + in combination with an additional key.
- The slide bar on the right side of the window allows you to adjust the view of the screen.
- The Audiogram Edit window includes five tabs: Audiogram Entry, Pure Tones, Speech Audiometry, Acoustic Immittance, and Graph Display.
- Disabled fields cannot be edited.
- Tab-key moves through the editable fields in a logical sequence, from left to right, and right-ear fields first and left-ear fields second.
- To bypass the Tab-key sequence, click the mouse in a specific field.

> **NOTE:** The Tab key and the mouse do not allow access to the disabled fields.

- Calculated fields display as disabled, because the system automatically populates them.
- A hint with acceptable values displays when you pause the cursor over an editable field.
1.  To enable/disable the hints, click File and select Enable/No Hints.
2.  Hints are not available, once the record is signed.

## Monitor/Keyboard Placement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch ACKQ\*3.0\*13 requires attention be given to the placement of the keyboard and monitor[^13].

- PC keyboard and PC monitor must be connected (cable) to the PC running the Audiogram Module.
- Locate the keyboard adjacent to or directly below the audiometer device controls.
- Locate the PC monitor in a physical position, so that the clinician can comfortably view and analyze the data imported to the Audiogram Module.

# What’s New in Audiogram Module Patch ACKQ\*3.0\*13

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch ACKQ\*3.0\*13 enhances the functionality of the Audiogram Module[^14].

- Audiogram Display is integrated into Audiogram Edit as a new tab, Graph Display.
- The Audiogram Module Interface allows the transfer of data, point by point, from the audiometer device to the grids in the Pure Tones and Speech Audiometry tabs of the Audiogram Edit window.
- A black box audiometer transfers all data at once (dump) from its associated software to the Audiogram Module at the end of a testing session. The Madsen Aurical is an example of a black box audiometer. For information regarding the use of the Audiogram Module with a black box audiometer, refer to Appendix A: Black Box Audiometer, page [121](#appendix-a-black-box-audiometer).
- To pass data from an audiometer to the Audiogram Module, an audiometer must be configured for the first time, Configure Audiometer. Each ensuing time the Audiogram Module is started, the configured audiometer is *remembered*. You can import data from the audiometer for all subsequent sessions.
- During subsequent uses of an audiometer, you can verify connection without reconfiguring, Check Audiometer.
- Within the Pure Tones tab, all Final or Masked field labels are changed to Masked.
- Within the Speech Audiometry tab under Rollover, Applied Max drop-down list boxes are added for the left and right ear. You can select the Word Recognition test (default, 1, 2, 3, 4, or 5) to use to calculate the PB Max value.
- For an audiometer capable of being reset, each time the Audiogram Module is opened, the data stored in the audiometer’s local repository is cleared or set to default, in preparation for a new patient. For an audiometer not capable of being reset, you must manually reset it.
- The graph display reflects imported data dynamically.
- Value boundary validation is part of data imports. When a value is outside the upper range of acceptable, valid values, the highest permitted value for a field displays with + (plus sign) to the right of it.
- On the Graph Display tab, for the Overlap and Separate views of the audiogram, Rollover Index for R and L, and Pure Tone Averages for R and L/Two/Three/Four are added to the display.
- On the Graph Display tab, for the Overlap view of the audiogram, IAR and CAR for R and L, and Right and Left for SRT-1 and 2, Mask-1 and 2, MCL, and UCL are added to the display.
- To import data from an audiometer successfully with F10, the Audiogram Edit window must be in focus and active.
- Frequency 1500 is added to the Pure Tones tab in the Bone Conduction section.
- To indicate no response (NR), add the + to the right of the no response (NR) data when the system does not automatically place it.

# Accessing the Audiogram Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You access the Audiogram Module[^15] through CPRS.

1.  From the Patient Selection pop-up, select a patient and click OK.
14. Click Tools and select Audiogram Edit. The Confirm pop-up displays.

![](quasar-version-3-user-manual-updated-ackq-3-21/003.png)

15. To create a new audiogram, click Yes. The Enter EXAM Date AND Time for NEW entry pop-up displays.

![](quasar-version-3-user-manual-updated-ackq-3-21/004.png)

16. Type the date and time that the exam takes place in the New Exam Date and Time: text box and click OK.  
    A new record is set up in the file and the age of the patient is calculated.
1.  You can type Now or n in the New Exam Date and Time: text box and the current date and time displays.
2.  Use any of the standard VA FileMan date/time formats. For more information, refer to Appendix G on page [133](#appendix-g-va-fileman-datetime-formats).
17. Click OK. The Audiogram Edit for \<patient\> as seen on \<date\> window displays with the Audiogram Entry tab open.
18. Continue with steps for the Audiogram Entry tab on page [95](#audiogram-entry).
19. To edit, view, or delete an audiogram (signed or unsigned), click No. The Find Patient Audiogram pop-up displays.

![](quasar-version-3-user-manual-updated-ackq-3-21/005.png)

20. Select an audiogram from the list box and click OK. The Audiogram Edit for \<patient\> as seen on \<date\> window displays with the Audiogram Entry tab open.
21. Continue with steps for the Audiogram Entry tab on page [95](#audiogram-entry).

# Audiogram Edit Window

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiogram Edit window contains the procedures and functional features applying to the navigation and data entry of a patient's audiometric exam readings; it is where you create a new audiometric record or edit an existing audiometric record for a patient.

The Audiogram Edit window has four menus: File, Device, Options/Graph, and Help. The window has five tabs: Audiogram Entry, Pure Tones, Speech Audiometry, Acoustic Immittance, and Graph Display. The Audiogram Edit window displays with the Audiogram Entry tab open.

![](quasar-version-3-user-manual-updated-ackq-3-21/006.png)

## File Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The File drop-down menu allows you to get a new record, save data, print the screen, view an audiogram, retransmit a record, delete a record, enable/disable hints, hide/show the Import Data button[^16], and exit the module.

![](quasar-version-3-user-manual-updated-ackq-3-21/007.png) ![](quasar-version-3-user-manual-updated-ackq-3-21/008.png)

- Use Get New Record to loop through existing audiometric records without re-entering codes and to go to another record for a patient, if accessing through CPRS or select a new patient/record, if accessing from the desktop.
- Use Save to retain data. Save is disabled until a value is added or changed.
- Use Delete Record to flag a local, signed audiogram for deletion (flag an erroneous record) and automatically send a message to the Denver ALC to delete the signed audiogram from the national database. You receive a confirmation message.
- Use No/Enable Hints to disable/enable the acceptable values displayed when you pause your cursor over an editable field.
- Use Hide/Show Import Button to enable/disable the import data button on the Audiogram Edit window.
- Use Retransmit Record to resend signed records transmitted only with air and speech results or for some reason did not make it to the Denver ALC. The retransmission date displays on the Audiogram Entry tab. When the original record is sent to the Denver ALC, the Retransmit Record is enabled.

## Device Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Device drop-down menu[^17] allows you to configure an audiometer, check an audiometer, and import data. All of the options of which the device is capable, display enabled when a device is configured, bidirectional and connected.

![](quasar-version-3-user-manual-updated-ackq-3-21/009.png)

Configure Audiometer is used to:

- Set up an audiometer for the first time.
- Disconnect an audiometer (None).
- Change the audiometer used for importing data.

Check Audiometer is used subsequently to:

- Connect to an audiometer.
- Verify connection status.
- Check for a dropped connection.

Use Import Data to transfer data from the audiometer to the Audiogram Module.

- Click the Device menu and select Import Data,
- Press F10 on the PC keyboard (the Audiogram Edit window must be in focus and active), or
- Click the Import Data button on the Audiogram Edit window.

## Options/Graph Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Options/Graph menu[^18] allows you to view the audiometric data in a graph or tabular format. As a data point is imported, it displays on the graph in the appropriate location and with the proper symbol. The test results are viewed as a single graph with the left ear and right ear results overlapping or as separate graphs, one graph for the left ear and one graph for the right ear. The VA form 10-2364 is a standard tabular form and displays only the last saved test data from the file.

![](quasar-version-3-user-manual-updated-ackq-3-21/010.png)

## Help Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Help menu[^19] displays at the top of all tabs. The Page Help option display tab-specific Help text.

![](quasar-version-3-user-manual-updated-ackq-3-21/011.png)

## Status Bar

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](quasar-version-3-user-manual-updated-ackq-3-21/012.png)

The status bar[^20] displays at the bottom of each tab and shows information about the audiometer:

Pane 1 – displays the model of the configured audiometer.

Pane 2 – displays the connection status of the configured audiometer: audiometer not configured, connected, or not connected.

Pane 3 – displays messages regarding the configured audiometer, such as indicating the data is out of range for the selected frequency. The message displays only for a few seconds. Also, an audible sound is produced for a message.

# Configuration of the Audiometer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to import data from the device to the Audiogram Module, the audiometer must be configured in the Audiogram Module[^21].

## Configure the Audiometer for the First Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first time you use an audiometer, you must configure it in the Audiogram Module.

1.  From the Patient Selection pop-up, select a patient and click OK.
2.  Click Tools and select Audiogram Edit. The Confirm pop-up displays.
3.  To create a new audiogram, click Yes. The Enter EXAM Date AND Time for NEW… pop-up displays.

> **NOTE:** When you open Audiogram Edit and click Yes to create a new audiogram, QUASAR creates a *skeleton* record in the QUASAR file for the previously selected patient in CPRS. If you do not add or change the patient’s record in the Audiogram Edit window, when you exit Audiogram Edit, a warning pop-up displays.

![](quasar-version-3-user-manual-updated-ackq-3-21/013.png)

1.  Click Yes, to remove the *skeleton* record from the QUASAR file.
2.  Click No, to retain the *skeleton* record.
4.  Type the date and time of the appointment and click OK.

> **NOTE:** Type Now (n) to use the current date and time.

> The Audiogram Edit window displays with the Audiogram Entry tab open. The message in the status bar indicates the audiometer is not configured. (The Import Data button is disabled.)

![](quasar-version-3-user-manual-updated-ackq-3-21/014.png)

5.  Click Device. The Device drop-down menu displays with only the Configure Audiometer option enabled.

![](quasar-version-3-user-manual-updated-ackq-3-21/015.png)

6.  Select Configure Audiometer. The Select Audiometer window displays.

![](quasar-version-3-user-manual-updated-ackq-3-21/016.png)

> **NOTE:** The list of available audiometers varies, depending on the models used at your site.

7.  Select an audiometer and click Select.

> The Audiogram Edit window displays with the Audiogram Entry tab open. The message in the status bar indicates the audiometer is connected. (The Import Data button is enabled.)

![](quasar-version-3-user-manual-updated-ackq-3-21/017.png)

8.  Click Device. The Device menu drop-down displays with options enabled for the specific configured and connected audiometer.

![](quasar-version-3-user-manual-updated-ackq-3-21/018.png)

## Verify the Connection of the Audiometer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can verify the connection[^22] of the audiometer at any time.

1.  In the Audiogram Module, the Audiogram Edit window displays with the Audiogram Entry tab open. The message in the status bar indicates the audiometer is connected. (The Import Data button is enabled.)

![](quasar-version-3-user-manual-updated-ackq-3-21/019.png)

22. Click Device. The Device drop-down menu displays with only Configure Audiometer, Check Audiometer, and Import Data enabled.

![](quasar-version-3-user-manual-updated-ackq-3-21/020.png)

23. Select Configure Audiometer. The Select Audiometer pop-up displays and indicates the current audiometer connected to a specific port.

![](quasar-version-3-user-manual-updated-ackq-3-21/021.png)

> **NOTE:** The port number (COM1) may vary.

*This page intentionally left blank for double-sided printing.*

# Audiogram Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Audiogram Entry tab allows you to collect and display basic patient and visit information. After the Date Signed is entered and saved, the data is transmitted to the Denver ALC and can no longer be edited.

If a patient is registered in the Denver ALC ROES system, audiometric data transmitted to the Denver ALC is available for viewing, in a tabular format, from the Denver ALC ROES Patient Information screen.

![](quasar-version-3-user-manual-updated-ackq-3-21/022.png)

## Audiogram Entry Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Date/Time of Visit</td>
<td><p>Date and time of visit are recorded when the patient record is created.<br />
This field cannot be edited.</p>
<p><strong>Note:</strong> The date and time entered in the Enter EXAM Date AND Time for NEW… pop-up, automatically populate the <strong>Date/Time of Visit</strong> text box of the Audiogram Entry tab.</p></td>
</tr>
<tr class="even">
<td>Patient</td>
<td><p>The patient name automatically populates the <strong>Patient</strong> text box from CPRS (current patient selected).</p>
<p>You cannot edit the patient field. If the wrong patient is selected, you must delete the record and repeat the process of creating a new record.</p></td>
</tr>
<tr class="odd">
<td>Examining Audiologist</td>
<td><p>Type the first few characters of the person’s last name or select from the drop-down list box.</p>
<p>Examining Audiologist is taken from the NEW PERSON file (#200).</p></td>
</tr>
<tr class="even">
<td>Referral Source</td>
<td><p>For referral source, type the first few letters of the location or select from the drop-down list box.</p>
<ul>
<li><p>Referral source pulls from the local HOSPITAL LOCATION file (#44).</p></li>
<li><p>Names for the locations vary from facility to facility.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Age at Visit</td>
<td>The age of the patient <strong>at the time of the visit</strong> is calculated by the system, which looks at the date of birth in the Patient file when the record is created.<br />
This field cannot be edited.</td>
</tr>
<tr class="even">
<td>Transducer Type</td>
<td><p>Method by which the sounds are transmitted:</p>
<ul>
<li><p>Earphones</p></li>
<li><p>Inserts</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Type of Visit</td>
<td><p>Three types of visits: C&amp;P (Compensation and Pension), Audiologist Referral, and Other.</p>
<p><strong>Note:</strong> Select <strong>Other</strong> and you can enter free text of 2-26 characters in the <strong>Other</strong> text box. The text is stored in the record and displays on VA form 10-2364.</p></td>
</tr>
<tr class="even">
<td>Claim Number</td>
<td><p>Type a number in the <strong>Claim Number</strong> text box.</p>
<p><strong>Note:</strong> The number is saved in the record and displays on VA form 10-2364.</p></td>
</tr>
<tr class="odd">
<td>NOT ADEQUATE FOR RATING PURPOSES’ into Comments check box</td>
<td><p>Select the <strong>NOT ADEQUATE FOR RATING PURPOSES’ into Comments</strong> check box when:</p>
<ul>
<li><p>Thresholds cannot be used for rating C&amp;P claims.</p></li>
<li><p>Testing was not done according to C&amp;P protocols.</p></li>
<li><p>Thresholds are not reliable for a C&amp;P exam.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Comments</td>
<td><p>Type a comment in the <strong>Comments</strong> text box. Up to 300 characters (approximately three lines of text).can be saved to appear in the national record and on the VA form 10-2364.</p>
<ul>
<li><p>If the form is not saved, you can use the check box to insert the phrase: NOT ADEQUATE FOR RATING PURPOSES. Once the phrase is inserted, the check box is disabled.</p></li>
<li><p>The phrase is the first 33 characters of your 300-character <strong>Comments</strong>.</p></li>
<li><p>To remove the phrase, highlight it, press <strong>Delete</strong>, and exit the Comments text box. This also removes the check from the check box.</p></li>
<li><p>To wrap the text in the Comments text box to accommodate 300 characters, press <strong>Ctrl + Enter</strong>.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Date Signed</td>
<td><p>The date the information is verified as accurate.</p>
<ul>
<li><p>Once a date is entered in the <strong>DATE SIGNED</strong> text box, the record is considered final and approved; the values are transmitted to the Denver ALC national database.</p></li>
<li><p>Once the record is sent to the Denver ALC, the <strong>Retransmit</strong> option is activated. Records at the Denver ALC are updated with additional information.</p></li>
<li><p>Once retransmitted, the retransmission date displays next to the date signed; a message displays if you try to retransmit a second time.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Audiogram Entry/Date Signed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After a date is entered and saved in the DATE SIGNED text box, all fields are locked and you cannot make any changes to the record. If after signing, you find the data was entered for the wrong patient or the wrong data was entered for a patient, delete the record and repeat the process for creating a new record.

- To delete an audiogram containing erroneous data, after a date is entered and saved in the DATE SIGNED text box, click File and select Delete Record.
- A deletion message is transmitted to the Denver ALC (Denver Acquisition & Logistics Center), if the record was signed, and it is removed from the national database. You receive a confirmation message.
- Completed and signed records are stored in a local QUASAR global. They are transmitted to the Denver ALC through the VistA MailMan system for inclusion with orders for hearing aids and repairs, when ordered through the VistA Remote Order Entry System (ROES) package.
- If you Exit without signing the audiogram, a pop-up displays reminding you that the audiogram is not signed and will not be sent to the Denver ALC.

![](quasar-version-3-user-manual-updated-ackq-3-21/023.png)

# Pure Tones

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pure Tones tab allows you to enter pure tone threshold values across a standard range of frequencies, as a measure of hearing loss. For an audiometer capable of being reset, each time the Audiogram Module is opened, the data stored in the audiometer’s repository is reset, in preparation for a new patient. For an audiometer not capable of being reset, you must manually reset it.

The audiogram (graphic display) is constructed with appropriate symbols, based on the data entered into the Pure Tones fields. Review the imported data to make sure that the fields are appropriately populated before saving.

![](quasar-version-3-user-manual-updated-ackq-3-21/024.png)

## Pure Tones Fields – Right and Left Ears

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 44%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
<th><strong>Valid Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Air Conduction</strong></td>
<td></td>
<td><strong>250 Hz-8000 Hz</strong></td>
</tr>
<tr class="even">
<td>Initial</td>
<td>First data value obtained during testing for Air Conduction, unmasked.</td>
<td>-10 to 105dB<br />
+, NR, CNT, DNT, blank</td>
</tr>
<tr class="odd">
<td>Retest</td>
<td>Only <em>unmasked</em> threshold for retested (second, third, fourth, and so on) frequencies.</td>
<td>-10 to 105dB<br />
+, NR</td>
</tr>
<tr class="even">
<td>Masked<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td>Masked threshold.</td>
<td>-10 to 105dB<br />
+, NR</td>
</tr>
<tr class="odd">
<td>Masking Level</td>
<td>Masking level value.</td>
<td>0 to 105dB<br />
CNM, blank</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Bone Conduction</strong></td>
<td>Frequency 1500 is added to the Pure Tones tab.<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></td>
<td><strong>250 Hz-4000 Hz</strong></td>
</tr>
<tr class="even">
<td>Initial</td>
<td>First data value obtained during testing for Bone Conduction, unmasked.</td>
<td>-10 to 80dB<br />
+, NR, CNT, DNT, blank</td>
</tr>
<tr class="odd">
<td>Retest</td>
<td>Only <em>unmasked</em> threshold for retested (second, third, fourth, and so on) frequencies.</td>
<td>-10 to 80dB<br />
+, NR</td>
</tr>
<tr class="even">
<td>Masked</td>
<td>Masked threshold.</td>
<td>-10 to 80dB<br />
+, NR</td>
</tr>
<tr class="odd">
<td>Masking Level</td>
<td>Masking level value.</td>
<td>0 to 105dB<br />
CNM, blank</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Inter Test Consistency</strong></td>
<td>Select a description from each drop-down list box, one for the right ear and one for the left ear.</td>
<td>Good, Fair, Poor</td>
</tr>
<tr class="even">
<td><strong>Pure Tone Averages</strong></td>
<td>Automatically calculated when sufficient information is entered. For more information, refer to Appendix F: Calculation of Pure Tone Averages on page <a href="#appendix-f-calculation-of-pure-tone-averages">131</a>.</td>
<td>Read-only fields</td>
</tr>
<tr class="odd">
<td><strong>SRT (Masking Level)</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Initial</td>
<td>First data value obtained during testing for Speech Reception Threshold.</td>
<td>-10 to 100dB<br />
CNT, DNT, blank</td>
</tr>
<tr class="odd">
<td>(Masking Level 1)</td>
<td>Masking level value for initial SRT.</td>
<td>0 to 105dB<br />
CNM, blank</td>
</tr>
<tr class="even">
<td>Final</td>
<td>Last data value obtained during testing for Speech Reception Threshold.</td>
<td>-10 to 100dB</td>
</tr>
<tr class="odd">
<td>(Masking level 2)</td>
<td>Masking level value for final SRT.</td>
<td>0 to 105dB<br />
CNM, blank</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>On the Pure Tones tab, Final or Masked is changed to Masked.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>On the Pure Tones tab, a column for frequency 1500 is added.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

## Pure Tones - Air and Bone Conduction Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- You can edit any data manually. After the data is edited, it can be overwritten by a new reading imported from the audiometer.
- Duplicate data entry text boxes exist for both the right and left ears. Keyboard navigation moves first through all of the right ear text boxes, then through all of the left ear text boxes.
- If a data point is outside the upper range of acceptable, valid values for a field, the system enters the highest permitted value for the field followed by the + sign, such as 105+.
- Masking values below the acceptable minimum are converted to zero for Air and Bone Conduction. A message displays in Pane 3.
- Manual entry is required for Could Not Test (CNT/c/C), Did Not Test (DNT/d/D), Could Not Mask (CNM/c/C), and No Response (n/N) values.[^23]
- When CNT (Could Not Test), DNT (Did Not Test), or NR (No Response) is entered in an Initial field, the Retest field for that frequency and ear is disabled.
- All fields are considered unmasked, unless a non-zero numeric value is entered in the Masking Level text box; CNM (Could Not Mask) is a valid response.
- When you retest without masking, the value from the retest is stored in the Retest text box. Values for subsequent retests overwrite the value stored in the Retest text box, as long as the Initial text box is populated.
- For each frequency, values for masked pure tones are stored in the Masked text box and the masking levels are stored in the Masking Level text box for the associated frequency.
- When you retest with masking, the subsequent masked data imported, overwrites the previous data in the Masked text box and the Masking Level text box with the new threshold dB and masking level.
- Indicate No Response by manually entering + with the numeric value or N. This is converted to the highest acceptable value followed by the + sign.
- Type + and it converts to maximum value for the frequency with a +.

## Importing Pure Tones Data Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can import values[^24] from the audiometer to the Audiogram Module. Values can be imported point by point or all at once (data dump), depending on the device configured. The clinician can transfer the data values appropriately without having the specific tab for that test open, as long as the Audiogram Module has the appropriate focus.

1.  In the Audiogram Module, click the Pure Tones tab.
24. Set your audiometer: Air Conduction or Bone Conduction and Right or Left ear.
25. Set the decibel threshold level (Hz) on the audiometer.
26. Set the masking level, if masking is required.
27. Conduct the testing.
28. To pass the dB value:
- Press F10 on the PC keyboard,
- Press the Import Data button on the Audiogram Edit window, or
- Click the Device menu and select Import Data.
29. Complete importing all test data collected in the Pure Tones, Speech Audiometry, and Acoustic Immittance tabs.
30. Complete viewing, editing, and confirming the imported data.
31. Save the data to the QUASAR file, click File and select Save. Save All Changes pop-up displays.

![](quasar-version-3-user-manual-updated-ackq-3-21/025.png)

- Click Yes to save changes
- Click No to discard changes.

# Speech Audiometry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Speech Audiometry tab allows you to enter Speech Reception Threshold (SRT) values for comfort levels, effective masking levels, and Word Recognition information. Calculated pure tone averages display automatically and are read-only. For an audiometer capable of being reset, each time the Audiogram Module is opened, the data stored in the audiometer’s local repository is reset, in preparation for a new patient. For audiometers not capable of being reset, you must manually reset it.

For information (including word lists) about the VA Speech Recognition & Identification Materials CD version 2.0, refer to the website: <span class="mark">REDACTED</span>

![](quasar-version-3-user-manual-updated-ackq-3-21/026.png)

## Speech Audiometry Fields: Right and Left Ears

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 44%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
<th><strong>Valid Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Speech Comfort Levels</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>MCL<br />
(Most Comfortable Level)</td>
<td>Manual entry</td>
<td>50 to 105dB</td>
</tr>
<tr class="odd">
<td>UCL (Uncomfortable Level)</td>
<td>Manual entry</td>
<td>50 to 105dB</td>
</tr>
<tr class="even">
<td>Initial SRT<br />
(Speech Reception Threshold)</td>
<td>First data value obtained during testing for Speech Reception Threshold (SRT)</td>
<td>-10 to 100dB<br />
CNT, DNT, blank</td>
</tr>
<tr class="odd">
<td>Masking Level</td>
<td>Masking level for the Initial SRT.</td>
<td>0 to 105dB<br />
CNM, blank</td>
</tr>
<tr class="even">
<td>Final SRT</td>
<td>Last data value obtained during testing for Speech Reception Threshold (SRT)</td>
<td>-10 to 100dB</td>
</tr>
<tr class="odd">
<td>Masking Level</td>
<td>Masking level for the Final SRT.</td>
<td>0 to 105dB<br />
CNM, blank</td>
</tr>
<tr class="even">
<td><strong>Pure Tone Averages</strong></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Two, Three, Four</td>
<td>Automatically calculated</td>
<td>Read-only fields</td>
</tr>
<tr class="even">
<td><strong>Rollover</strong></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PB Max<br />
(Phonetically-balanced Maximum)</td>
<td><p>Automatically populated</p>
<p>Refer to Appendix D: Calculation of PB Max and RI (or PI/PB) on page <a href="#appendix-d-calculation-of-pb-max-and-ri-or-pipb">127</a> for PB Max information.</p></td>
<td>Read-only fields</td>
</tr>
<tr class="even">
<td>RI<br />
(Rollover Index)</td>
<td><p>Automatically calculated</p>
<p>Refer to Appendix D: Calculation of PB Max and RI (or PI/PB) on page <a href="#appendix-d-calculation-of-pb-max-and-ri-or-pipb">127</a> for the RI formula.</p></td>
<td>Read-only fields</td>
</tr>
<tr class="odd">
<td>Applied Max<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td>Select a test series to use for the Applied Max.</td>
<td>Default, Test 1, Test 2, Test 3, Test 4, Test 5</td>
</tr>
<tr class="even">
<td><strong>Word Recognition</strong></td>
<td>1, 2, 3, 4, 5</td>
<td></td>
</tr>
<tr class="odd">
<td>Material</td>
<td><p>Most commonly used lists, both 25- and 50-word, which apply to all the word tests.</p>
<p>Select a material for both ears from the <strong>Material</strong> drop-down list box.</p></td>
<td>NU6-25/NU6-50<br />
W22-25/W22-50<br />
CNC-25/CNC-50<br />
Other</td>
</tr>
<tr class="even">
<td>Presentation</td>
<td><p>Delivery method of the material, which apply to all word tests.</p>
<p>Select a delivery method for both ears from the <strong>Presentation</strong> drop-down list box.</p></td>
<td>Recorded (CDs and tapes) and MLV (Monitored Live Voice)</td>
</tr>
<tr class="odd">
<td>% (Percent Correct)</td>
<td>Percent of words correctly recognized.</td>
<td>0 to 100<br />
%, CNT, DNT, blank</td>
</tr>
<tr class="even">
<td>HL (Hearing Level)</td>
<td></td>
<td>0 to 100, blank</td>
</tr>
<tr class="odd">
<td>EM (Effective Masking)</td>
<td></td>
<td>0 to 105 dB<br />
CNM, blank</td>
</tr>
<tr class="even">
<td>List</td>
<td>Manual Entry</td>
<td><p>Maryland CNC: 1, 3, 4, 6, 7, 9, 10; 1-1, 1-3, 1-4, 1-6, 1-7, 1-9, 1-10; blank</p>
<p>CID W-22: 1A to 4A, 1B to 4B, 1C to 4C, 1D to 4D, 1E to 4E, 1F to 4F, blank</p>
<p>NU-6: 1A to 4A, 1B to 4B, 1C to 4C, 1D to 4D, blank</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Applied Max is added to the Rollover section to allow the user to select a WRT test to use for PB Max.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

## Speech Audiometry - Speech Reception and Word Recognition Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- If a data point is outside the upper range of acceptable, valid values for a field, the system enters the highest permitted value for the field followed by the + sign, such as 105+.
- You can edit any data manually and the data is not be overwritten by data imported from the audiometer; unless the imported data is the result of a new reading after the data was edited. The system ensures that the most recent value displays.
- The PB Max and RI fields are automatically populated when sufficient information is entered. For more information, refer to Appendix D: Calculation of PB Max and RI (or PI/PB) on page [127](#appendix-d-calculation-of-pb-max-and-ri-or-pipb).
- You can select the Word Recognition test (default, 1, 2, 3, 4, or 5) to use for the PB Max value.
- You can import the Word Recognition HL, EM, and % values from audiometers capable of collecting these values.
- Manual entry is required for Could Not Test (CNT/c/C), Did Not Test (DNT/d/D), and Could Not Mask (CNM/c/C) values.[^25]
- Initial SRT is the first SRT value obtained during testing.
- CNT (Could Not Test) or DNT (Did Not Test) can only be entered in an Initial SRT text box. The Masking and Final SRT fields are disabled for that ear, when you enter CNT or DNT in the Initial SRT field.
- Type + and converts to maximum value with a +.
- If there is data in both the Initial and Final fields, the Final SRT value displays on the audiogram (graph display) data is in both fields, the final data displays on the graphic audiogram.
- Place values obtained after masking, re-instructing the patient, or retesting for reliability, in the Final SRT text box.
- The masking level value for a masked SRT test is stored in the Masking Level text box of the SRT test.
- The masking level value for a masked Word Recognition test is stored in the EM text box.
- When you retest SRT without masking, the value from the retest is stored in the Final SRT text box with no value in the Masking Level text box. Values for subsequent retests overwrite the value stored in the Final SRT text box.
- When you retest SRT with masking, the retest masked data is stored in the Final SRT text box and the Final Masking Level text box. Values for subsequent retests, overwrite the values stored in the Final SRT text box and the Final Masking Level text box.
- The first Word Recognition test series populates column 1. As you retest, values populate column 2, then column 3, then column 4, and last column 5. For retest 6 and up, the values overwrite the values in column 5.
- For WRT the first CNT/DNT value the system finds is replaced moving from Test 1 through Test 5.
- Selections in Material apply to all of the word tests and include both the 25- and 50- word lists that are most commonly used.
- Selections in the Presentation drop-down list box apply to all of the word tests and include Recorded (CD or tape recordings) and MLV (Monitored Live Voice).

## Importing SRT and WRT Data Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can import values[^26] from the audiometer to the Audiogram Module, point by point. Values can be imported to the SRT (Speech Reception Threshold) and WRT (Word Recognition Testing) grids while one of the other tabs is open.

#### Speech Reception Threshold

1.  In the Audiogram Module, click the Speech Audiometry tab.
32. Set your audiometer: Speech Reception Threshold and Right or Left ear.
33. Set the decibel threshold level (Hz) on the audiometer.
34. Set the masking level, if masking is required.
35. To pass the dB value:
- Save the reading on the audiometer.
- Press F10 on the PC keyboard,
- Press the Import Data button on the Audiogram Edit window, or
- Click the Device menu and select Import Data.
36. Complete importing the test data collected in the Pure Tones and Speech Audiometry tabs, and enter data in the Acoustic Immittance tab.
37. Complete viewing, editing, and confirming the imported data.
38. Save the data to the QUASAR file, click File and select Save. Save All Changes pop-up displays.

![](quasar-version-3-user-manual-updated-ackq-3-21/027.png)

- Click Yes to save changes
- Click No to discard changes.

#### Word Recognition Testing

1.  In the Audiogram Module, click the Speech Audiometry tab.
39. Set your audiometer: Word Recognition and Right or Left ear.
40. Perform your Word Recognition testing
41. To pass the dB value to the Audiogram Module:
- Save the reading on the audiometer.
- Press F10 on the PC keyboard,
- Press the Import Data button, or
- Click the Device menu and select Import Data.
42. Complete importing the test data collected in the Pure Tones and Speech Audiometry tabs, and enter data in the Acoustic Immittance tab.
43. Complete viewing, editing, and confirming the imported data.
44. Save the data to the QUASAR file, click File and select Save. Save All Changes pop-up displays.

![](quasar-version-3-user-manual-updated-ackq-3-21/028.png)

- Click Yes to save changes
- Click No to discard changes.

# Acoustic Immittance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Acoustic Immittance tab allows you to enter values for Tympanometry, Acoustic Reflex Thresholds, Contralateral Reflex Decay, and Other Tests, such as, Weber, Rinne, Stenger. All values collected for the Acoustic Immittance tab must be entered manually.

> **NOTE:** Some audiologists use A (absent) or NR (no response). Because this does not indicate the level used, the audiologist is not protected from accusations by the patient that the presentation level was injurious. The level must be documented on the Audiogram Module screen. When there is no response at the maximum permissible level or the patient's comfort level, enter the value followed by +, (105+).

![](quasar-version-3-user-manual-updated-ackq-3-21/029.png)

## Acoustic Immittance Fields: Right and Left Ears

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 44%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><strong>Description</strong></th>
<th><strong>Valid Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Tympanometry</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Middle Ear Pressure</td>
<td></td>
<td>-600 to +400 daPa<br />
CNT, DNT, blank</td>
</tr>
<tr class="odd">
<td>Ear Canal Volume</td>
<td></td>
<td>.1 to 10 cc</td>
</tr>
<tr class="even">
<td>Peak Immittance 226</td>
<td></td>
<td>.01 to 15.00 mmhos<br />
blank</td>
</tr>
<tr class="odd">
<td>Peak Immittance 678</td>
<td></td>
<td>.01 to 15.00 mmhos<br />
blank</td>
</tr>
<tr class="even">
<td>Tympanogram Type</td>
<td>Drop-down list box</td>
<td>As, Ad, A, B, C, Flat (no peak), blank</td>
</tr>
<tr class="odd">
<td><strong>Acoustic Reflex Thresholds</strong></td>
<td></td>
<td><strong>Probe Right, Probe Left:<br />
500 Hz to 4000 Hz and BBN</strong></td>
</tr>
<tr class="even">
<td>Stm Left/Stm Right</td>
<td>Contralateral</td>
<td>50 to 105 dB HL<br />
CNT, DNT, blank</td>
</tr>
<tr class="odd">
<td>Stm Right/Stm Left</td>
<td>Ipsilateral</td>
<td>50 to 105 dB HL<br />
CNT, DNT, blank</td>
</tr>
<tr class="even">
<td><strong>Contralateral Reflex Decay</strong></td>
<td></td>
<td><p><strong>Probe Right, Probe Left:</strong></p>
<p><strong>500 Hz and 1000 Hz</strong></p></td>
</tr>
<tr class="odd">
<td>Stm Left/Stm Right</td>
<td>Reflex Decay</td>
<td>+ (positive) or – (negative)<br />
CNT, DNT, blank</td>
</tr>
<tr class="even">
<td></td>
<td>Reflex Half-life</td>
<td>0 to 10 seconds<br />
CNT, DNT, blank</td>
</tr>
<tr class="odd">
<td><strong>Other Tests</strong></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Weber</td>
<td></td>
<td>R, L, ML, CNT, DNT, blank</td>
</tr>
<tr class="odd">
<td>PT Stenger</td>
<td>Pure Tones Stenger</td>
<td>+, -, CNT, DNT, blank</td>
</tr>
<tr class="even">
<td>Rinne</td>
<td></td>
<td>+, -, CNT, DNT, blank</td>
</tr>
<tr class="odd">
<td>Other</td>
<td></td>
<td>10-character limit or blank</td>
</tr>
</tbody>
</table>

## Acoustic Immittance Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The maximum allowed hearing level for an acoustic reflex threshold, both the probe ear and stimulus ear, is 105 dB.
- When CNT (Could Not Test) or DNT (Did Not Test) is entered in a Middle Ear Pressure field, the Retest field for that frequency and ear is disabled.
- On the audiogram (graphic display) for no response (NR), the no response reflex symbol ![](quasar-version-3-user-manual-updated-ackq-3-21/030.png), displays at the specified frequency level.
- On the tabular audiogram, VA form 10-2364, the numeric value displays as well as, CNT (Could Not Test) and DNT (Did Not Test).

# Graph Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Graph Display[^27] tab allows you to view procedures and functional features applying to the patient's audiometric exam readings in graph format. Graph Display displays audiometric data for both ears in a graphic format and a tabular format (VA form 10-2364, version 2005). The default view is data overlapping for the right and left ears.

The graph in the Audiogram Module reflects the data most recently transferred from the audiometer or data manually entered. Graph Display displays values before they are saved in the QUASAR file. You collect a data point, import it, and view the data point on the Graph Display. Graph Display automatically refreshes to reflect the most recent data.

![](quasar-version-3-user-manual-updated-ackq-3-21/031.png)

## Graph Display Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Data on the graph display is read-only; the data cannot be edited on the graph.
- The frequency is represented in Hertz (Hz).
- Frequency displays logarithmically on the horizontal axis (abscissa) in values from 125 to 8000 Hz.
- The dashed lines for 750, 1500, 3000, and 6000 Hz are placed logarithmically on the graph.
- The hearing level (HL) is represented in decibels (dB). Hearing level displays on the vertical axis (ordinate) in values from -10 to 120 dB.
- Values entered in the Pure Tones Masked fields display on the audiogram graph.
- When there is data in both Speech Audiometry SRT text boxes, the retest data displays on the audiogram graph.
- If a Masking Level field is enabled and a value is entered in that text box, the final value on the audiogram graph displays as *masked*.
- If a final value is not entered and a value for Masking Level is entered, the lower non-zero value in the Initial and Retest text boxes displays as *masked*.
- On the audiogram (graphic display) for no response (NR), the no response reflex symbol ![](quasar-version-3-user-manual-updated-ackq-3-21/032.png), displays at the specified frequency level.
- Pure Tone symbols display so that the midpoint of the symbol centers on the vertical ruling and the horizontal axis are at the appropriate hearing level. Additional symbols are offset from the Pure Tone symbols.
- Bone Conduction symbols display adjacent to, but not touching the frequency coordinate ruling, and centered vertically at the hearing level.
- The symbol for the left ear is placed to the *right* of the vertical ruling and the symbol for the right ear is to the *left* of the vertical ruling.
- NR (No Response) values do not connect on the graph.
- Appendix C: Determining Series Values to Place on the Graph on page [125](#appendix-c-determining-series-values-to-place-on-the-graph), explains how values from an audiometric record are selected to display on the audiogram graph when more than one reading is entered for a field, such as, Initial, Retest and Final.
- Appendix F: Calculation of Pure Tone Averages on page [131](#appendix-f-calculation-of-pure-tone-averages), provides additional information about the automatic calculation of pure tone averages.

## Graph Display in Separate View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The right ear and left ear graphs can be viewed separately[^28] for each ear. The left ear graph displays on the right side and the right ear graph displays on the left side, consistent with the tabular format (VA Form 10-2364) audiogram. The Graph Display tab with the Separate view of the audiogram displayed includes the Rollover Index for R and L, and Pure Tone Averages for R and L/Two/Three/Four.

![](quasar-version-3-user-manual-updated-ackq-3-21/033.png)

Use the Options/Graph menu to select Separate to view the graphs of the right and left ears separately, select VA form 10-2364 to view a tabular format (VA Form 10-2364) audiogram, and select Overlap to return to the default view.

## Graph Display in Overlap View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Graph Display default view is right ear and left ear series overlapping[^29] on a graph. The right ear series displays in red and the left ear series displays in blue. The Graph Display tab with the Overlap view of the audiogram displayed includes R and L values for IAR and CAR, and Right and Left values for SRT-1and 2, Mask-1and 2, MCL, and UCL, as well as R and L values for Rollover Index and Pure Tone Averages, Two/Three/Four.

Use the Options/Graph menu to select Separate to view the graphs of the right and left ears separately and select VA form 10-2364 to view a tabular format (VA Form 10-2364) audiogram.

![](quasar-version-3-user-manual-updated-ackq-3-21/034.png)

## Graph Display in Tabular View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The tabular view[^30] presents a computer-generated VA Standard form 10-2364 (version 2005), containing only the saved values from the selected audiogram. The values on the form are intended only for printing or viewing.

Use the Options/Graph menu to select Separate to view the graphs of the right and left ears separately and select Overlap to return to the default view.

![](quasar-version-3-user-manual-updated-ackq-3-21/035.png)

## VA form 10-2364 Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA form 10-2364 is the summation of all the tests performed with patient information. The audiogram must be saved, in order for the current data to display on the VA form 10-2364.

- The Comment is pulled from the database to the database and you cannot edit it on VA form 10-2364.
- The Referral Reason is pulled from the Type of Visit field on the Audiogram Entry tab.
- CNT (Could Not Test) and DNT (Did Not Test) are not used in the VA form 10-2364.
- With the cursor over the form, press the right button on the mouse. A pop-up displays allowing you to print, copy, or exit VA form 10-2364.

![](quasar-version-3-user-manual-updated-ackq-3-21/036.png)

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Word/Acronym</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>API</td>
<td>Application Programmer Interface</td>
</tr>
<tr class="even">
<td>Application/Package</td>
<td>Computer programs, files, and documentation developed specifically to meet the requirements of a user or a group of users and support a specific function within VistA: software and documentation that support the automation of a service, such as ROES.</td>
</tr>
<tr class="odd">
<td>AC</td>
<td>Air Conduction</td>
</tr>
<tr class="even">
<td>AR</td>
<td>Acoustic Reflex</td>
</tr>
<tr class="odd">
<td>ARD</td>
<td>Acoustic Reflex Decay</td>
</tr>
<tr class="even">
<td>ASPS/A&amp;SP</td>
<td>Audiology and Speech Pathology Service</td>
</tr>
<tr class="odd">
<td>BBN</td>
<td>Broad Band Noise</td>
</tr>
<tr class="even">
<td>BC</td>
<td>Bone Conduction</td>
</tr>
<tr class="odd">
<td>Black Box Audiometer</td>
<td>Audiometer that requires proprietary software for conducting audiometric measurements. It lacks physical buttons, sliders, and dials. It relies on proprietary software to accomplish control and interfacing tasks.</td>
</tr>
<tr class="even">
<td>C&amp;P</td>
<td>Compensation and Pension</td>
</tr>
<tr class="odd">
<td>CAPRI</td>
<td>Compensation and Pension Records Interchange</td>
</tr>
<tr class="even">
<td>CAR</td>
<td>Contralateral Acoustic Reflex</td>
</tr>
<tr class="odd">
<td>cc</td>
<td>Cubic Centimeter</td>
</tr>
<tr class="even">
<td>CDR</td>
<td>Cost Distribution Report</td>
</tr>
<tr class="odd">
<td>CNC</td>
<td>Consonant Nucleus Consonant</td>
</tr>
<tr class="even">
<td>CNM</td>
<td>Could Not Mask</td>
</tr>
<tr class="odd">
<td>CNT</td>
<td>Could Not Test</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Record System</td>
</tr>
<tr class="odd">
<td>CPT Codes</td>
<td>Codes listed in the Physicians Current Procedural Terminology Handbook</td>
</tr>
<tr class="even">
<td>daPa</td>
<td>decaPascal</td>
</tr>
<tr class="odd">
<td>dB</td>
<td>Decibel</td>
</tr>
<tr class="even">
<td>Denver ALC</td>
<td>Denver Acquisition &amp; Logistics Center<br />
A part of the Department of Veteran's Affairs, Office of Acquisition and Logistics, located in Denver, Colorado.</td>
</tr>
<tr class="odd">
<td>DFN</td>
<td>The internal number of the patient in the PATIENT file (#2).</td>
</tr>
<tr class="even">
<td>DLL</td>
<td>Dynamic Link Library</td>
</tr>
<tr class="odd">
<td>DNT</td>
<td>Did Not Test</td>
</tr>
<tr class="even">
<td>DSS</td>
<td>Decision Support System</td>
</tr>
<tr class="odd">
<td>EM</td>
<td>Effective Masking</td>
</tr>
<tr class="even">
<td>FA</td>
<td>Frequency Average</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphical User Interface<br />
A Windows environment that allows users to interact using a mouse or keyboard.</td>
</tr>
<tr class="even">
<td>HCFA</td>
<td>Health Care Financing Administration</td>
</tr>
<tr class="odd">
<td>HCPCS</td>
<td>HCFA Common Procedure Coding System</td>
</tr>
<tr class="even">
<td>HL</td>
<td>Hearing Level</td>
</tr>
<tr class="odd">
<td>Hz</td>
<td>Hertz</td>
</tr>
<tr class="even">
<td>IAR</td>
<td>Ipsilateral Acoustic Reflex</td>
</tr>
<tr class="odd">
<td>ICD-9-CM</td>
<td>International Classification of Diseases, Ninth Edition, with Clinical Modifications</td>
</tr>
<tr class="even">
<td><span id="ICDp119" class="anchor"></span>ICD-10-CM</td>
<td>International Classification of Diseases, Tenth Edition, with Clinical Modifications</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>Information Resource Management</td>
</tr>
<tr class="even">
<td>KERNEL</td>
<td>A set of VistA software routines that function as an intermediary between the host operating system and the VistA application package, such as ROES.</td>
</tr>
<tr class="odd">
<td>Listener</td>
<td>In ROES, it is the RPC Broker on the workstation and the server.</td>
</tr>
<tr class="even">
<td>MCL</td>
<td>Most Comfortable Loudness</td>
</tr>
<tr class="odd">
<td>ML</td>
<td>Masking Level</td>
</tr>
<tr class="even">
<td>MMHO</td>
<td>Millimho<br />
mho is a measure of acoustic admittance</td>
</tr>
<tr class="odd">
<td>Module</td>
<td>GUI part of QUASAR, covering a single topic.</td>
</tr>
<tr class="even">
<td>NR</td>
<td>No Response</td>
</tr>
<tr class="odd">
<td>Package/Application</td>
<td>Computer programs, files, and documentation developed specifically to meet the requirements of a user or a group of users and support a specific function within VistA: software and documentation that support the automation of a service, such as ROES.</td>
</tr>
<tr class="even">
<td>PB</td>
<td>Phonetically Balanced</td>
</tr>
<tr class="odd">
<td>pc</td>
<td>Piece</td>
</tr>
<tr class="even">
<td>PCE</td>
<td>Patient Care Encounter</td>
</tr>
<tr class="odd">
<td>PCMM</td>
<td>Patient Care Management Module</td>
</tr>
<tr class="even">
<td>PI/PB</td>
<td>Performance Intensity-Phonetically Balanced</td>
</tr>
<tr class="odd">
<td>Pr-L</td>
<td>Probe Left</td>
</tr>
<tr class="even">
<td>Pr-R</td>
<td>Probe Right</td>
</tr>
<tr class="odd">
<td>PSAS</td>
<td>Prosthetics and Sensory Aids Service</td>
</tr>
<tr class="even">
<td>PTA</td>
<td>Pure Tone Average</td>
</tr>
<tr class="odd">
<td>QUASAR</td>
<td>Quality: Audiology and Speech Analysis and Reporting</td>
</tr>
<tr class="even">
<td>RI</td>
<td>Rollover Index</td>
</tr>
<tr class="odd">
<td>ROES</td>
<td>Remote Order Entry System<br />
A package for ordering various supplies from the Denver ALC.</td>
</tr>
<tr class="even">
<td>SAT</td>
<td>Speech Awareness Threshold</td>
</tr>
<tr class="odd">
<td>SRT</td>
<td>Speech Reception Threshold</td>
</tr>
<tr class="even">
<td>SSN</td>
<td>Social Security Number</td>
</tr>
<tr class="odd">
<td>UCL</td>
<td>Uncomfortable Loudness</td>
</tr>
<tr class="even">
<td>UNC</td>
<td>Universal Naming Convention</td>
</tr>
<tr class="odd">
<td>VACO</td>
<td>Veterans Affairs Central Office</td>
</tr>
<tr class="even">
<td>VARO</td>
<td>Veterans Affairs Regional Office</td>
</tr>
<tr class="odd">
<td>Vea</td>
<td>Acoustic Equivalent Volume<br />
Same as Equivalent Ear Canal Volume Vec)</td>
</tr>
<tr class="even">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
</tbody>
</table>
*This page intentionally left blank for double-sided printing.*

# Appendix A: Black Box Audiometer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The import of data from the software of a black box audiometer[^31] to the QUASAR Audiogram Module occurs at the completion of a testing session. The data points collected during the testing assessment are imported all at once into the QUASAR Audiogram Module as a data dump. Information provided in the User Manual applies to the placement and display of the testing data.

The DLL file for the audiometer must be installed in the appropriate directory.

For assistance with the black box audiometer software, refer to the reference guide of the audiometer.

#### Importing Data

1.  Open CPRS.
45. Select a patient from the Patients list box and click OK.
46. Click Tools and select ROES Audiogram Enter/Edit.
47. Create a new audiogram. Click Yes.
48. Type Now in the New Exam DATE and TIME text box and click OK. In ROES Audiogram Enter/Edit, the Audiogram Edit window displays with the Audiogram Entry tab open.
49. Click Device
50. Select Check Audiometer.
51. Click Cancel.

> **NOTE:** The port number (COM1) may vary. In ROES Audiogram Enter/Edit, the status bar indicates that the black box audiometer is connected.

52. Open the black box audiometer software and perform your testing.
53. Continue collecting data points, until you complete your testing session.
54. In ROES Audiogram Enter/Edit, press Import Data. All the data points transfer to the appropriate fields in the Audiogram Module–data dump is complete.
55. Manually edit any necessary fields.
56. In ROES Audiogram Enter/Edit, on the Audiogram Entry tab
1.  Enter the date in the DATE SIGNED text box.
2.  Save and send the record to the Denver ALC. The record is sent to the Denver ALC.

![](quasar-version-3-user-manual-updated-ackq-3-21/037.png)

57. Exit the Audiogram Module.
58. Exit CPRS.

# Appendix B: Accessing Audiogram Display 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any doctor with access to the local system can view the Audiogram Display within the application to aid in treatment and diagnosis decisions. They can continue to view the display as assigned in patch ACKQ\*3.0\*12. For information on Audiogram Display, refer to *User Manual - Audiometric Exam Module*, November 2005 in the VistA Document Library.

> <http://www.va.gov/vdl/documents/Clinical/Qual_Audio_Speech_Anal_(QUASAR)/ackq3_0_p12um.pdf>

1.  From the Patient Selection pop-up, select a patient and click OK.
59. Click Tools and select Audiogram Display. The Find Patient Audiogram window displays with a list of audiograms available for the patient.
60. Select an audiogram and click OK. The Audiogram Display window displays with the selected audiogram for the patient  
    Lookup for exams for the patient is done in the AUDIOMETRIC EXAM DATA file (#509850.9).

![](quasar-version-3-user-manual-updated-ackq-3-21/038.png)

61. If no audiogram is available and you click OK, the ROES3 Audiogram Display message pop-up displays.

![](quasar-version-3-user-manual-updated-ackq-3-21/039.png)

62. Click OK. Audiogram Display closes.

*This page intentionally left blank for double-sided printing.*

# Appendix C: Determining Series Values to Place on the Graph

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are some key rules for preparing series values for display on the audiogram graph.

The *initial*, *retest* and *final* thresholds, as well as the *final masking* level are obtained, using these rules.

The rules are checked in the following order, until a point is obtained.

Only the final reading contains the *masking* level, if one exits.

1.  If the *initial* value is CNT (Could Not Test) or DNT (Did Not Test), there is no point on the graph.
63. If the *final* reading has a value including +, it is used.
64. If the *retest* value is “”, the *initial* value is used.
65. If the *initial* value is “”, the *retest* value is used.
66. If the *initial value* contains + and the *retest* value does not, the *retest* value is used.
67. If the *initial* value does not contain + and the *retest* value does, the *initial* value is used.
68. If the *initial* value is less than the *retest* value, the *initial* value is used.
69. If a value is in a *retest* field, it is used.
70. If the selected point indicates a *No Response* (+), the symbol appears but does not connect to adjoining values on the display.

    The Points to Plot on the Graph[^32] flowchart indicates the how-to of determining the points to plot on the audiogram graph. It follows on the next page.

![](quasar-version-3-user-manual-updated-ackq-3-21/040.png)

# Appendix D: Calculation of PB Max and RI (or PI/PB)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Calculation of the Rollover Index (RI), or Performance Intensity-Phonetically Balanced (PI/PB), value in the Audiogram Module is based on specific profession-standard formulas established for these measurements. Basic descriptions of some of these formulas are as follows:

- PB Max is the default maximum percentage from the word recognition testing. In patch ACKQ\*3.0\*13 the ability to select a PB Max was added for the display of PB Max only. The default PB Max is always used in the RI calculation.
- PB Min is the minimum percentage from the word recognition testing.
- RI or PI/PB is an indicator of possible retrocochlear pathology.  
  RI or PI/PB = (PB Max - PB Min) / (PB Max)  
  The Rollover Index is significant when it exceeds .40.
- The RI or PI/PB index assesses multiple scores and levels in one ear. The calculation occurs only when a second score obtained at a higher presentation level, is poorer than a prior score at a lower presentation level. The result is always a value less than 1.0.

*This page intentionally left blank for double-sided printing.*

# Appendix E: Access to Multiple Broker Environments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have access to multiple broker environments, (such as, training and development), you need to select an environment on the Connect To pop-up. Your local IRM or ADPAC can provide you with the correct server name.

![](quasar-version-3-user-manual-updated-ackq-3-21/041.png)

Select the correct environment from the Connect To drop-down list box and click OK.

*This page intentionally left blank for double-sided printing.*

# Appendix F: Calculation of Pure Tone Averages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pure Tone Averages (PTA) displayed in the Audiogram Module are automatically calculated and supplied when sufficient information is entered. At each level, the numbers used are the ones that display on the graph for that level. There are three Frequency Average (FA) formulas.

#### Frequency Average (FA) Formulas

- 2FA (PTA2) = average of the lowest two readings from 500, 1000, and 2000 Hz
- 3FA (PTA3) = average of the readings from 500, 1000 and 2000 Hz
- 4FA (PTA4) = average of the readings from 1000, 2000, 3000 and 4000 Hz

#### Rounding Fives

When a result is exactly midway between two whole numbers (such as, 3.5 is exactly half way between 3.0 and 4.0), it makes just as much sense to round down as it does to round up. Usually there is no harm in using the *always round up* rule, which is often taught in schools and used by computer programs. However, this rounding rule can cause problems when adding a very large number of values (such as, in accounting). The sum can be a little bigger than it ought to be.

The Audiogram Module uses the *odd-even* rule.

- If the five is the last significant digit and the round-off digit (digit to the left of the .5) is odd, round up.
- If the five is the last significant digit and the round-off digit (digit to the left of the .5) is even, do not round up.

> **NOTE:** The Audiogram Module and the CPRS audiogram use the same rounding rules for decimal fractions 0-4 and 6-9. The two systems differ on rounding decimals exactly equal to .5. The rounding rule used in this program is: if the average is exactly halfway between two whole numbers, the result rounds to the even number. This method of rounding is often called *Banker’s Rounding*.

*This page intentionally left blank for double-sided printing.*

# Appendix G: VA FileMan Date/Time Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Examples of valid dates:

JAN 20 1957 or 20 JAN 57 or 1/20/57 or 012057

T (TODAY), T+1 (TOMORROW), T+2, T+7, and so on

T-1 (YESTERDAY), T-3W (3 WEEKS AGO), and so on

- If the year is omitted, the system uses current year.
- A two-digit year assumes no more than 20 years in the future or 80 years in the past.
- If only the time is entered, the system assumes current date.
- The date is followed by a time, such as JAN 20@10, T@10AM, 10:30, and so on.
- Enter time as NOON, MIDNIGHT or NOW.
- Enter NOW+3’ for current date and time plus 3 (minutes apostrophe).

> **NOTE:** Time is REQUIRED for the Date/Time of Exam field in order to establish the entry.

*This page intentionally left blank for double-sided printing.*

# Appendix H: Message Box Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of error messages[^33] that display for the listed reason.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Error</strong></th>
<th><strong>Reason</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><em>A needed RPC XXXXXXXX is not available.</em></td>
<td><p>Contact your IRM.</p>
<p>The 'XWB IS RPC AVAILABLE' remote procedure call returned FALSE for RPC XXXXXXXXX. IRM needs to install this RPC in order for the action to be workable.</p></td>
</tr>
<tr class="even">
<td><em>A problem was encountered accessing VistA, RPC XXXXX.</em></td>
<td><p>Contact your IRM Service.</p>
<p>The Broker call to remote procedure XXXXX failed.</p></td>
</tr>
<tr class="odd">
<td><em>A problem was encountered communicating with the server.</em></td>
<td>The RPCBroker call to the server was tried for a remote procedure, but it failed.</td>
</tr>
<tr class="even">
<td><em>A problem with the RPC call - no data to graph.</em></td>
<td>The expected data for the selected entry was not returned by the remote procedure call.</td>
</tr>
<tr class="odd">
<td><em>Application Canceled. Or unable to access RPCBroker.</em></td>
<td>Broker.Connected returned False.</td>
</tr>
<tr class="even">
<td><em>Cannot continue without Patient.</em></td>
<td>Patient identification number DFN is undefined or nil.</td>
</tr>
<tr class="odd">
<td><em>Broker Server could not be determined.</em></td>
<td>The program did not pick up the name of the broker server or the port.</td>
</tr>
<tr class="even">
<td><em>Connection to Broker Server could not be established.</em></td>
<td>The server and port selected could not be activated.</td>
</tr>
<tr class="odd">
<td><em>No Charts to Show! Audiogram Terminating.</em></td>
<td>Called the View Audiogram option for a patient that has no data in file 509850.9.</td>
</tr>
<tr class="even">
<td><em>No Patient to lookup.</em></td>
<td>An attempt was made to continue without a patient selected. (DFN undefined or nil).</td>
</tr>
<tr class="odd">
<td><em>Patient not selected.</em></td>
<td>An attempt was made to continue without a patient selected.</td>
</tr>
<tr class="even">
<td><em>Problem encountered in setting up message - no data sent!</em></td>
<td>XMZ &lt; 1 was returned from the MailMan setup call.</td>
</tr>
<tr class="odd">
<td><em>Problem saving entries for Acoustic Immittance!</em></td>
<td>A change on the Acoustic Immittance tab was not saved because the database would not accept it. Exiting and coming back to the page causes the faulty entry to be missing.</td>
</tr>
<tr class="even">
<td><em>Problem saving entries for Left Ear!</em></td>
<td>A change to the Left Ear was not saved because the database would not accept it. Exiting and coming back to the page causes the faulty entry to be missing.</td>
</tr>
<tr class="odd">
<td><em>Problem saving entries for Right Ear!</em></td>
<td>A change to the Right Ear was not saved because the database would not accept it.</td>
</tr>
<tr class="even">
<td><em>Record NOT sent to</em> Denver ALC<em>.</em></td>
<td>The setup of the transfer message failed after entering a DATE SIGNED. Another attempt could be made by having IRM remove the entry in the DATE SIGNED field in 509850.9. Then use the GUI again to sign the audiogram edit.</td>
</tr>
<tr class="odd">
<td><em>The Audiogram Option is not approved for this user.</em></td>
<td>Someone is attempting to access option ACKQROES3E when it is not on their menu tree.</td>
</tr>
<tr class="even">
<td><em>The XXXXXXXX program[option name] could not be accessed.</em></td>
<td><p>Terminating application.</p>
<p>The CreateContext for the application failed - not in user's menu tree.</p></td>
</tr>
<tr class="odd">
<td><em>There was a problem deleting the record.</em></td>
<td>The delete button was pressed, but the DIK call returned an error.</td>
</tr>
<tr class="even">
<td><em>User identification could not be established.</em></td>
<td>The DUZ was not defined, or the XUS GET USER INFO RPC returned an error</td>
</tr>
<tr class="odd">
<td><em>You are not authorized to use the Audiogram Enter/Edit program [ACKQROES3E]. Terminating application…</em></td>
<td>Someone is attempting to access option ACKQROES3E when it is not on their menu tree.</td>
</tr>
<tr class="even">
<td><em>Users station not added. Station in record is blank.</em></td>
<td>The program picked up an invalid pointer to the Institution file.</td>
</tr>
</tbody>
</table>

# Appendix I: Shortcut Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of shortcut keys[^34] for the QUASAR Audiogram Module GUI.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 27%" />
<col style="width: 16%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>Window</th>
<th>Option/Text</th>
<th>Shortcut</th>
<th>Action/Opens</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Audiogram Edit</strong></td>
<td><strong>File</strong> menu</td>
<td>Alt, F</td>
<td>Opens the File menu</td>
</tr>
<tr class="odd">
<td></td>
<td>Get New Record</td>
<td>Ctrl, G</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Save</td>
<td>Ctrl, S</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Print</td>
<td>Ctrl, P</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Retransmit Record</td>
<td>Ctrl, T</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Delete Record</td>
<td>Ctrl, D</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>No Hints/Enable Hints</td>
<td>Ctrl, N</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Hide Import Button/<br />
Show Import Button</td>
<td>Ctrl, B</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Flip Tabs</td>
<td>Ctrl, F</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Exit</td>
<td>Ctrl, E</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Device</strong> menu</td>
<td>Alt, D</td>
<td>Opens the Device menu</td>
</tr>
<tr class="even">
<td></td>
<td>Configure Audiometer</td>
<td>Ctrl, C</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Check Audiometer</td>
<td>Ctrl, H</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Import Data</td>
<td>F10 or<br />
Ctrl, I</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>Options/Graph</strong> menu</td>
<td>Alt, O</td>
<td>Opens the Options/Graph menu</td>
</tr>
<tr class="odd">
<td></td>
<td>Overlap</td>
<td>Ctrl, O</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Separate</td>
<td>Ctrl, S</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>VA form 10-2364</td>
<td>Ctrl, V</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><strong>Help</strong> menu</td>
<td>Alt, H</td>
<td>Opens the Help menu</td>
</tr>
<tr class="even">
<td><span id="p21_138" class="anchor"></span></td>
<td>About</td>
<td>Ctrl, A</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Page Help</td>
<td>Ctrl, H</td>
<td>Click a tab and press F1</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Audiogram Entry</strong> tab</td>
<td></td>
<td>Click Tab<br />
Ctrl, E<br />
Alt + E</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Tab</td>
<td>Move from field to field</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Pure Tones</strong> tab</td>
<td></td>
<td>Click Tab<br />
Ctrl, T<br />
Alt + T</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Tab</td>
<td>Move from field to field</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Speech Audiometry</strong> tab</td>
<td></td>
<td>Click Tab<br />
Ctrl, A<br />
Alt + A</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Tab</td>
<td>Move from field to field</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Acoustic Immittance</strong> tab</td>
<td></td>
<td>Click Tab<br />
Ctrl + I<br />
Alt + I</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>Tab</td>
<td>Move from field to field</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Graph Display</strong> tab</td>
<td></td>
<td>Click Tab<br />
Ctrl, G<br />
Alt + G</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Tab</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><strong>VA form 10-2364</strong></td>
<td>Right-click mouse on form to access options</td>
<td>Opens the VA form 10-2364</td>
</tr>
<tr class="odd">
<td></td>
<td>Print</td>
<td>Ctrl + P</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Copy</td>
<td>Ctrl + C</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Exit</td>
<td>Ctrl + X</td>
<td>Close the VA form 10-2364</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
A&SP Reports 37
A&SP Reports menu 5
A&SP Site Parameters 7
ACKQ ADHOC key 3, 5
ACKQ\*3.0\*13, new in 81
ACKQROES3E 79
Acoustic Immittance
Fields 109
PT Stenger 110
Rinne 110
Tab 109
Values 110
Weber 110
Acoustic Reflex Threshold 110
Air condiuction
Retest 100
Air conduction
Initial 99
Masked 100
Masking level 100
Appointment time 20
ASP file number 20
Audiogram
Existing 83
New 83
Audiogram Display
Component 123
Audiogram edit 79
Audiogram Edit window 85
Audiogram Entry
Date signed 97
Fields 95
Tab 95
Audiology & Speech Visit Tracking System 13
Audiology & Speech Visit Tracking System menu 4, 5
Audiometric exam data file 123
Audiometric scores 23
B
Black box audiometer 121
Bone conduction
Initial 100
Masked 100
Masking level 100
Retest 100
Bypass Audiometrics 9
C
C & P 96
C&P Exam Adequation 49
CDR account 23
CDR report 47
Check audiometer 87
Clinic 19
Clinic Location 9
Compensation and Pension 96
Compile A&SP Capitation Data 48
Configure audiometer 86
Configure audiometer for first time 89
Connect audiometer, verify 92
Contralateral Reflex Decay 110
Cost Comparison Report 41
CPRS 79
CPT modifier 26
D
Delete an A&SP Clinic Visit 51
Demographic data record 89
Device menu 86
Diagnostic code 21
Division 19
Inactivate 7
E
Edit an Existing Visit 37
Eligibility for this appointment 21
Enter Cost Information for Procedures 10
Error messages 135
F
File menu 85
Forcing the C&P Prompt 35
Frequency on graph 111
G
Generate A&SP Service CDR 47
Get New Record 86
Graph Display
Layer view 114
Separate view 113
Series values 125
Tab 111
Tabular view 115
VA form 10-2364 115
VA form 10-2364 Fields 116
Values 111
Values to place on graph 125
H
Hearing level on graph 112
Help menu 87
Hints 80
Enable 86
No 86
I
Import button
Hide 86
Show 86
Import data 87
Import Data button
Disabled 90, 92
Enabled 91
Inquire - A&SP Patient 37
Interface with PCE 7
Inter-test consistency 100
K
Key Assignment 5
M
Management Reports A&SP 47
Management Reports A&SP menu 4
Manual entry
CNM Could Not Mask 101, 106
CNT Could not test 101
CNT Could Not Test 106
DNT Did Not Test 101, 106
Masked values 101
Masking level 101
Menu
Device 86
File 85
Help 87
Options/Graph 87
Multiple broker environment
Access 129
N
New Clinic Visits 18
Not Using the AMIE/C&P Interface or Audiometric Data for Hearing Loss Codes 35
O
Options/Graph menu 87
P
Patient eligibility 21
Patient name 19
Patients by City 38
PB Max 127
Calculation 127
PB Min 127
PCE interface
trouble shooting mismatched data 18
PI/PB
Calculation 127
Index 127
Primary diagnosis 21
Print A&SP Capitation Report 48
Print A&SP File Entries 10
Print A&SP Service CDR 47
Procedure code 26
CPT modifier 26
procedure provider 27
Volume 26
Pure Tones
Air conduction values 101
Bone conduction values 101
Fields 99
Importing data points 102
Tab 99
Pure Tones Averages
Banker's rounding 131
Calculation 131
Frequency average formula 131
Rounding fives 131
Q
QUASAR 79
QUASAR audiogram module 79
R
Retest SRT with masking 106
Retest with masking 101
Retest without masking 101
ROES 79
Rollover
Applied Max 104
PB Max 104
RI 104
S
Save 86
Send to PCE 7
Service connected condition 22
Set Up/Maintenance menu 4
Shortcut keys 137
Skeleton record 89
Speech Audiometry
Fields 103
Importing SRT data points 107
Importing Word Recognition data points 107
Speech Reception values 105
Tab 103
Word Recognition values 105
Speech Comfort Level
Final SRT 104
Initial SRT 104
Masking level 104
Masking Level 104
MCL Most Comfortable Level 103
UCL Uncomfortable Level 104
Staff (Enter/Edit)
A&SP Staff file 6
USR Class Membership file 6
Staff setup
A&SP Staff file 3
USR Class Membership file 3
Statistics by Event Capture Procedure 39
Statistics by Procedure 40
Status bar 87
Supervisors, staff 7
T
Tab
Acoustic Immittance 109
Audiogram Entry 95
Graph Display 111
Pure Tones 99
Speech Audiometry 103
Tailor-Made A&SP Reports 41
Tympanometry 109
U
Update Files per CO Directive 10
Use ASP Clinic File Number 8
Use C&P 8
V
VA FileMan cheat sheet 58
Value range, outside 101, 105
Visit
Appointment eligibility 21
Appointment time 20
ASP file number 20
Audiometric scores 23
C&P 20
Care for SC condition 22, 23
Care related to exposure 22
Care related to MST 23
CDR account 23
Clinic 19
CPT modifier 26
Diagnosis 25
Diagnosis provider 21
Diagnostic and clinical tests 25
Diagnostic code 21
Division 19
Event capture codes 26
Medical history 24
New QUASAR patient 27
Patient name 19
Physical examination 24
Primary diagnosis 21
Primary provider 25
Procedure code 26
Procedure provider 27
Review medical records 24
Secondary provider 25
Student 25
Time spent 27
Update PCE problem list 21
Visit date 19
Volume 26
Visit date 19
Visits by Diagnosis 38
VistA document library 79
Volume
complexity based procedure 26
Repeated procedures 27
time based procedure 27
W
Was care related to ... exposure 22
Was the care for a SC condition 22
Word Recognition
% Percent correct 105
EM Effective Masking 105
HL Hearing level 105
Initial SRT 104
List 105
Material 104
Presentation 105
Test series 106
Workload Report 44
*This page intentionally left blank for double-sided printing.*
[^1]: This is a new field contained in Patch ACKQ\*3.0\*1.
[^2]: This is a new field contained in Patch ACKQ\*3.0\*1.
[^3]: This is a new field contained in Patch ACKQ\*3.0\*1.
[^4]: This is a new field contained in Patch ACKQ\*3.0\*1.
[^5]: This is a new field contained in Patch ACKQ\*3.0\*1.
[^6]: This is a new field contained in Patch ACKQ\*3.0\*1.
[^7]: This is a new field contained in Patch ACKQ\*3.0\*1.
[^8]: This is a new field contained in Patch ACKQ\*3.0\*1.
[^9]: This is an updated field contained in Patch ACKQ\*3.0\*1.
[^10]: New Report included in Patch ACKQ\*3.0\*1.
[^11]: New Warning Message included in Patch ACKQ\*3.0\*1.
[^12]: Modified conventions used in the Audiogram Module.
[^13]: Section added on the placement of the monitor and keyboard.
[^14]: List of enhancements associated with the Audiogram Module GUI.
[^15]: Audiogram Module is accessed through CPRS only. Access steps are updated to reflect this.
[^16]: Import Data button is added to the File menu; Flip Tabs is removed from the File menu.
[^17]: Device menu is added to the Audiogram Edit window.
[^18]: Options/Graph menu is added to the Audiogram Edit window.
[^19]: Options in the Help menu are rearranged.
[^20]: Status Bar is added to the Audiogram Edit window.
[^21]: Section added for configuring an audiometer.
[^22]: Section added on verifying the connection of an audiometer.
[^23]: Abbreviations are acceptable for could not test, did not test, and no response, such as CNT/c/C for could not test.
[^24]: Section added for importing pure tones data points.
[^25]: Abbreviations are accepted for could not test, did not test, and no response, such as CNT/c/C for could not test.
[^26]: Section added for importing SRT and WRT data points.
[^27]: Section added on the Graph Display tab.
[^28]: Section added on the separate view of the graph display.
[^29]: Section added on the overlap view of the graph display.
[^30]: Section added on the tabular view (VA form 10-2364) of the graph display. The form is modified to conform with VA standards.
[^31]: Appendix added about the black box audiometer.
[^32]: Added the Points to Plot on the Graph flowchart to *Determining Series Values to Place on the Graph*.
[^33]: Message Box Errors appendix is moved from the technical manual to the user manual.
[^34]: Section added on shortcut keys.
