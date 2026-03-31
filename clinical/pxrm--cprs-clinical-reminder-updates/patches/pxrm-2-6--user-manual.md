---
title: PXRM*2*6 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: 
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*6
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 16%\\" /> <col style=\\"width: 15%\\" /> <col style=\\"width: 33%\\" /> <col style=\\"width: 16%\\" /> <col style=\\"width: 18%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th><blockquote> <p><strong>Date</strong></p> </blockquote></th> <th><blockquote> <p><strong>Page #</stron"
audience: 
keywords: 
  - blockquote
  - strong
  - reminders
  - reminder
  - clinical
  - table
  - class
  - health
  - style
  - width
page_count: 0
word_count: 5868
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 7
has_toc: False
is_stub: False
pub_date: December 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_6_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_6_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-6-user-manual/001.png)

> <span id="_bookmark0" class="anchor"></span>Clinical Reminders

## Version 2.0 Patch PXRM\*2\*6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> User Manual

> December 2007

> Health Provider Systems Office of Information & Technology

> Department of Veterans Affairs

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
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Page #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Project Manager</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Technical Writer</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>November 07</p>
</blockquote></td>
<td><blockquote>
<p>Throughout</p>
</blockquote></td>
<td><blockquote>
<p>Edits per developer review</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>October 07</p>
</blockquote></td>
<td><blockquote>
<p>Pages <a href="#Chapter_3:_Processing_Mental_Health_Remi"><u>17</u></a>-31</p>
</blockquote></td>
<td><blockquote>
<p>Updated chapter on processing MH dialogs</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>August 07</p>
</blockquote></td>
<td><blockquote>
<p>Throughout*</p>
</blockquote></td>
<td><blockquote>
<p>Edits per development updates</p>
<p>PXRM*2*6</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>May-July 06</p>
</blockquote></td>
<td><blockquote>
<p>Throughout</p>
</blockquote></td>
<td><blockquote>
<p>Edits per development updates made in PXRM*2*4</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Apr 06</p>
</blockquote></td>
<td><blockquote>
<p>throughout</p>
</blockquote></td>
<td><blockquote>
<p>Edits per SQA review</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Feb 2006</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark19"><u>60</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Added FAQs</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Sept 2005</p>
</blockquote></td>
<td><blockquote>
<p><a href="#_bookmark0"><u>5</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Changes to GEC Referral, made in PXRM*2.0*4</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> \*NOTE: This manual has been revised extensively for PXRM\*2\*6, to focus on Mental Health- related reminders and dialogs. Chapters and appendices have been removed and new appendices have been added. For example, the chapter on the use of the IHD reminders and the appendix on GEC Reports were removed. If you need to refer to these, please look at earlier versions of the User Manual (Clinician Guide) in the VistA Document Library (VDL)

> [Clinical Reminders V. 2.0 1](#Clinical_Reminders_V._2.0_)

2.  [Using Clinical Reminders 6](#II._Using_Clinical_Reminders_)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Clinical_Reminders_V._2.0_" class="anchor"></span><strong>Purpose of This Guide</strong></p>
</blockquote></th>
<th><blockquote>
<p>This Clinician Guide is designed to help the clinical practitioner understand Clinical Reminders and to use the functionality to improve patient care and clinical processes. This guide will also give you an overview of national VA reminders/dialogs and components:</p>
<p><strong>Target Audience</strong></p>
<p>We have developed this guide for the following types of users:</p>
</blockquote>
<ul>
<li><p>Clinicians</p></li>
<li><p>Nurses</p></li>
<li><p>Clinical Application Coordinators (CAC)</p></li>
<li><p>Clinical Reminders Managers</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Other Sources of Information</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Related Documentation</strong></p>
<p>The following manuals are available from the VistA Documentation Library (VDL) <a href="http://www.va.gov/vdl"><u>http://www.va.gov/vdl</u></a>.</p>
</blockquote>
<ul>
<li><p>Clinical Reminders V2.6 Release Notes (PXRM_2_6_RN.PDF)</p></li>
<li><p>Clinical Reminders V2.6 Install and Setup Guide (PXRM_2_6_IG.PDF)</p></li>
<li><p>Clinical Reminders Technical Manual (PXRM_2_4_TM.PDF)</p></li>
<li><p>Clinical Reminders Manager Manual (PXRM_2_6_MM.PDF)</p></li>
</ul>
<blockquote>
<p>Other relevant information is also available on the Clinical Reminders website:</p>
<p><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a>/</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Benefits_ofClinical_Reminders_" class="anchor"></span><strong>Benefits of Clinical Reminders</strong></p>
</blockquote>
<p>From Harvard Innovations award:</p>
<p><em>The involvement of front-line providers, use of performance measures and universal use of electronic health records have enabled VA to set the national benchmark in quality of care. VistA's computerized system enables key decisions by checking links to automated drug distribution, leading to a significant reduction in the error rate.</em></p>
<p><em>VistA is innovative because of its unique linkage with standardized, consistent performance measurement.</em></p>
<p><em>VA's electronic health records provide patient- specific, comprehensive clinical decision support that results in a performance measurement system that encourages driven evidence- based practice.</em></p></th>
<th><blockquote>
<p><strong>Clinical Reminders Overview</strong></p>
<p>The Clinical Reminder system helps caregivers deliver higher quality care to patients for both preventive health care and management of chronic conditions, and helps ensure that timely clinical interventions are initiated.</p>
<p>Reminders assist clinical decision-making and also improve documentation and follow-up, by allowing providers to easily view when certain tests or evaluations were performed and to track and document when care has been delivered. They can direct providers to perform certain tests or other evaluations that will enhance the quality of care for specific conditions. The clinicians can then respond to the reminders by placing relevant orders or recording clinical activities on patients’ progress notes.</p>
<p>Clinical Reminders may be used for both clinical and administrative purposes. However, the primary goal is to provide relevant information to providers at the point of care, for improving care for veterans. The package benefits clinicians by providing pertinent data for clinical decision-making, reducing duplicate documenting activities, assisting in targeting patients with particular diagnoses and procedures or site- defined criteria, and assisting in compliance with VHA performance measures and with Health Promotion and Disease Prevention guidelines.</p>
<p><strong>Clinical Practice Guidelines</strong></p>
<p>The Veterans Health Administration (VHA), in collaboration with the Department of Defense (DoD) and other leading professional organizations, has been developing clinical practice guidelines since the early 1990s. Guidelines for the Rehabilitation of Stroke and Amputation and the Care Guide for Ischemic Heart Disease were among the first distributed throughout VHA in 1996 and 1997. Since that time, numerous other guidelines, including guidelines on Diabetes Mellitus, COPD, Major Depressive Disorder, Psychoses, Tobacco Use Cessation, Hypertension, have been developed and distributed for implementation throughout the system.</p>
<p>VHA defines clinical practice guidelines as recommendations for the performance or exclusion of specific procedures or services for specific disease entities. These recommendations are derived through a rigorous methodological approach that includes a systematic review of the evidence to outline recommended practice. Clinical guidelines are seen by many as a potential solution to inefficiency and inappropriate variation in care.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Benefits of Clinical Reminders</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Clinical Practice Guidelines</strong></p>
<p><strong>Purpose of Guidelines</strong></p>
</blockquote>
<ul>
<li><p>Assure that the appropriate amount of care is provided (addressing both under &amp; over-utilization)</p></li>
<li><p>Reduce errors and promote patient safety</p></li>
<li><p>Ensure predictable and consistent quality</p></li>
<li><p>Promote learning and research</p></li>
<li><p>Facilitate patient and family education</p></li>
</ul>
<blockquote>
<p><strong>Clinical Reminders, Performance Measures, and Clinical Practice Guidelines</strong></p>
<p>Each Veterans Integrated Service Networks (VISN) must comply with performance measures that address Prevention Index/Chronic Disease Index (PI/CDI), as well as with the Health Promotion And Disease Prevention Program Handbook 1120.2, which states that each VHA facility shall have a program to educate veterans with respect to health promotion and disease prevention and to provide veterans with preventive medical care that includes screening and other clinical services.</p>
<p>The Clinical Reminders package offers tools to help clinicians comply with these performance measures and guidelines on a patient-by-patient basis. The use of these tools leads to improved patient care.</p>
<p>Providers can work with their local Clinical Application Coordinators to set up customized reminders based on local and national guidelines for patient education, immunizations, skin tests, measurements, exams, laboratory tests, mental health tests, radiology procedures, and other procedures.</p>
<p>The Office of Quality and Performance oversees the VA’s performance measure plan. Each year the <a href="http://vaww.oqp.med.va.gov/committees/pmwg/pmwg.asp"><u>Performance Measurement Workgroup</u></a> (PMWG), recommends the annual Network Performance Plan to the Under Secretary for Health. The Plan is formally signed as the Network Director's annual performance appraisal. The specific details of the plan are published annually on the OQP website. <a href="http://vaww.oqp.med.va.gov/default.htm"><u>http://vaww.oqp.med.va.gov/default.htm</u></a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_Introduction_" class="anchor"></span><strong>Patch 6 Updates to Clinical Reminders</strong></p>
<p>NOTE: Most dialogs that use Mental Health tests won’t exhibit many changes until CPRS GUI V27 is released.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Clinical Reminders Patch 6</strong></p>
<p>Patch 6 contains modifications to integrate the Clinical Reminders package with the new version of the Mental Package called MHA3. The Clinical Reminders package will support use of new mental health surveys, instruments, and forms for clinical collection, reminder evaluation, patient list building and reporting. These modifications will be distributed at the same time as MHA3 (YS*5.01*85).</p>
<p>This functionality is needed so that Clinical Reminders can be used to help sites meet the Performance Measure requirements related to a standardized set of Mental Health Instruments that will be available in the YS*5.01*85 patch. The standardized instruments are AUDC, BDI2, PHQ-2, PHQ9, and PC-PTSD.</p>
<p>GMTS*2.7*77, bundled with PXRM*2.0*6, provides two new Health Summary Components to view administered mental health tests and scores: MHAL - MHA Administration List and MHAS - MHA Score.</p>
<p>In order to use all of the dialog functionality available with MHA3 and PXRM*2*6, Version 27 of the CPRS GUI will need to be installed. This version isn’t scheduled for release until Spring 2008. In this manual, we’ll show examples of dialog screens as they will appear when patch PXRM*2*6 is released and sites are still using CPRS 26, as well as examples of how they’ll appear with CPRS 27.</p>
<p>See Chapter 3 in this manual for descriptions and examples of the Mental Health dialogs.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Patch 6 Updates to

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinical Reminders

### Updates to National Reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Modified National Reminders

- Depression Screening

> PHQ-2 & PHQ9 in the dialog

- Iraq & Afghan Post Deploy Screen

> Converted to use MH tests (AUDC, PHQ-2, PC PTSD) Added more detailed branching logic

- TBI Screening

> Fixed selection problem; added done elsewhere

- MHV Influenza Vaccine Updated date for FY08

> New National Reminders

- PTSD Screen

> Uses PC PTSD

- Alcohol (Audit-C) Screen

> Uses AUDC for all alcohol screens

- Positive AUDIT-C Evaluation

> Provides a standard tool for education and counseling

- Multiple branching logic reminders

![](pxrm-2-6-user-manual/002.png)

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="II._Using_Clinical_Reminders_" class="anchor"></span><strong>Chapter 1: Clinical Using Clinical Rem</strong></p>
<p><strong>Reminders and</strong> Clinician reminders are</p>
<p><strong>CPRS Overview</strong> • Cover Sheet</p>
</blockquote>
<ul>
<li><p>Clock button</p></li>
<li><p>Notes tab</p></li>
<li><p>Reports tab (H</p></li>
</ul>
<blockquote>
<p>The cover sheet display of <strong>Cover Sheet</strong></p>
<p>reminders can be Clinical reminders that</p>
<p>customized for Site, CPRS. When you left-c</p>
<p>System, Location, or User. presented in a pop-up</p>
<p>See Appendix C, for cover sheet, you can ac</p>
<p>instructions on how to edit information.</p>
<p>cover sheet reminders.</p>
<p>More details about wha in the following pages.</p>
</blockquote></th>
<th><blockquote>
<p><strong>inders in CPRS</strong></p>
<p>accessible in CPRS in four places:</p>
</blockquote>
<p>(upper right-hand corner of each tab in CPRS) ealth Summaries)</p>
<blockquote>
<p>are due are displayed on the cover sheet of lick on a reminder, patient-related details are window. By right-clicking on a reminder on the cess the reminder definition and reference</p>
</blockquote>
<p>at’s available from the Cover Sheet are provided</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Chapter 1: CPRS and Reminders Overview

![](pxrm-2-6-user-manual/003.png)

## ![](pxrm-2-6-user-manual/004.png)Chapter 1: Clinical Reminders and CPRS Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example: Education Topic

> ![](pxrm-2-6-user-manual/005.png)

> Chapter 1: CPRS and Reminders Overview

> For detailed information on how reminders are defined, see the Clinical Reminders Manager Manual.

> Reminder Inquiry

> Clicking on reminder inquiry will produce a display of the reminder definition.

> ![](pxrm-2-6-user-manual/006.png)

> If you click on Reference Information, you will get a list of web sites that have information related to the clinical reminder. Clicking on one of them will open your web browser at that site.

> Clicking on Reminder Icon Legend will bring up a display that shows what the various reminder icons mean. These icons will appear on the CPRS header bar (referred to as the Clock button).

> Reminders Icon Legend

> ![](pxrm-2-6-user-manual/007.png)

> Chapter 1: CPRS and Reminders Overview

![](pxrm-2-6-user-manual/008.png)

> Chapter 1: CPRS and Reminders Overview

> Action Menu on Available Reminders

![](pxrm-2-6-user-manual/009.png)

> ![](pxrm-2-6-user-manual/010.png)Chapter 1: CPRS and Reminders Overview

> You or your site can determine the folder view, and whether the folders are open or closed when you first open the reminders tab (also called a drawer).

> Using a dialog to resolve a clinical reminder is discussed in Chapter 2.

> Reminder Dialog Tree View

> ![](pxrm-2-6-user-manual/011.png)

> Chapter 1: CPRS and Reminders Overview

> Reports Tab

> Health Summaries containing Clinical Reminders can be viewed from the Reports tab in CPRS. See the Health Summary section later in this guide for more information.

> The Ad hoc health summary can also be used to display selected clinical reminders using either an abbreviated display or the full clinical maintenance display. (See [<u>Chapter 5: Health Summaries and Clinical</u>](#Chapter_5:_Health_Summaries_and_Clinical) [<u>Reminders</u>](#Chapter_5:_Health_Summaries_and_Clinical))

## Chapter 2: Processing/ Resolving Clinical Reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE:

> Your site can determine the folder view – which reminders and categories/folders appear in the reminders drawer.

> Summary of Steps to Process Reminders

> These are the basic steps for processing reminders from the Notes tab in CPRS. These steps are described in more detail, as they relate to Mental Health, in Chapter 3.

1.  Start a new progress note. To process a reminder, start a new progress note. When you begin a new progress note, the reminders drawer appears.
2.  Open the reminders drawer. When you click on the reminders drawer, you see several folders containing reminders for this patient. Possible folders include Due, Applicable, Not Applicable, All Evaluated, and Other Categories. These folders may contain a hierarchy of folders and reminders within folders. The view of folders is customizable by you (see [<u>Appendix C</u>](#Appendix_C:_Edit_Cover_Sheet_Reminder_Li)). The folders and subfolders in the Reminders Drawer are sometimes called the “tree view.”
3.  Choose a reminder. Open a folder (if necessary) and click a reminder that you wish to process. At this point, you may be asked to provide the primary encounter provider, so that any PCE data entered from reminder dialog processing can be saved.

> Chapter 2: Processing/ Resolving Clinical Reminders

![](pxrm-2-6-user-manual/012.png)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 2: Resolving Clinical Reminders, cont’d</strong></p>
<p><strong>TIP:</strong></p>
<p>Use the Next or Back buttons to take you to the dialog for the next or previous reminder due in the reminders drawer.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Summary of Steps to Process Reminders, cont’d</strong></p>
</blockquote>
<ol start="5" type="1">
<li><p><strong>Complete the dialog box.</strong> The dialog box lists possible actions or interventions that may be taken to satisfy this reminder. As you make selections from the dialog box, you can see the text of the progress note in the bottom part of the screen (below the Clear, Back, and Next buttons). Below the progress note text area is the encounter information including orders and PCE, Mental Health, and Vital Sign data. The bold text in these areas applies to the specific reminder you are processing. You can process multiple reminders.</p></li>
<li><p><strong>Expanded dialog boxes.</strong> Clicking a checkbox may bring up additional choices: an area for comments, a diagnosis to choose, or other information that may satisfy the reminder.</p></li>
</ol>
<blockquote>
<p><strong>Dialog with orders.</strong> Reminder dialogs can include orders. If quick orders are included in the dialog, these are placed as soon as the reminder processing is finished and the orders are signed. If the order requires more information before releasing the order, an order dialog will appear after you click Finish, allowing you to complete the order.</p>
<p><strong>Mental health tests.</strong> Reminder dialogs can include a pre- defined set of mental health tests. PXRM*2*6 expands the number of MH tests that can be included in dialogs, and even more will be available when CPRS GUI v27 is released.</p>
<p>Progress note text can be generated based on the mental health score.</p>
</blockquote>
<ol start="7" type="1">
<li><p><strong>Finish processing the reminder and complete your note.</strong> Click on the Finish button when you have checked all the appropriate checkboxes for each reminder you wish to process. You then go back to the Note window, where you can review and edit the reminder dialog progress note text added, to have a completed progress note for the encounter.</p></li>
<li><p><strong>(Optional) Evaluate processed reminders.</strong> You can use the Action menu to select the Evaluate Processed Reminders menu item from the Reminders Available window, to ensure that the reminders are satisfied. This action will evaluate the reminders that you processed while you wait, and update the Reminders Available window and reminders drawer lists to reflect the new statuses.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="Chapter_3:_Processing_Mental_Health_Remi" class="anchor"></span>Chapter 3:

> Chapter 3: Processing Mental Health Reminders, cont’d

> Chapter 3: Processing Mental Health Reminders, *cont’d*

> Example: Depression Screening dialog initial window

![](pxrm-2-6-user-manual/013.png)

> Chapter 3:

> Processing Mental Health Reminders, *cont’d*

> PHQ-2 Example as it appears with PXRM\*2\*6 and CPRS GUI V26

![](pxrm-2-6-user-manual/014.png)

> Chapter 3: Processing Mental Health Reminders, *cont’d*

> Example: PHQ9 window in CPRS GUI 26

![](pxrm-2-6-user-manual/015.png)

> Chapter 3:

> Processing Mental Health Reminders, *cont’d*

> Example: PHQ9 test, as it will appear after CPRS GUI 27 is released

![](pxrm-2-6-user-manual/016.png)

> Chapter 3: Processing Mental Health Reminders, *cont’d*

> Example: PHQ9 cont’d

> ![](pxrm-2-6-user-manual/017.png)

> Chapter 3:

> Processing Mental Health Reminders, *cont’d*

> Example: Unable to Screen button checked

> ![](pxrm-2-6-user-manual/018.png)

> Chapter 3:

> Processing Mental Health Reminders, cont’d

> Example: Iraq & Afghan Post-Deployment Screen Dialog Initial Window

> ![](pxrm-2-6-user-manual/019.png)

> Chapter 3: Processing Mental Health Reminders, cont’d

> Iraq & Afghan Post-Deployment Screen Dialog

> ![](pxrm-2-6-user-manual/020.png)

> Chapter 3: Processing Mental Health Reminders, cont’d

> Iraq & Afghan Post-Deployment Screen

> ![](pxrm-2-6-user-manual/021.png)

> Chapter 3:

> Processing Mental Health Reminders, cont’d

> Example: TBI Screening Initial Screen

> ![](pxrm-2-6-user-manual/022.png)

> Chapter 3:

> Processing Mental Health Reminders, cont’d

> TBI Screening Example: Yes checked

> ![](pxrm-2-6-user-manual/023.png)

> Chapter 3:

> Processing Mental Health Reminders, cont’d

> TBI Screening Questions

> ![](pxrm-2-6-user-manual/024.png)

> ![](pxrm-2-6-user-manual/025.png)

> Chapter 3:

> Processing Mental Health Reminders, cont’d

> Example: Alcohol Use Screen (AUDIT-C)

> ![](pxrm-2-6-user-manual/026.png)

> Chapter 3: Processing Mental Health Reminders, cont’d

> AUDC (as seen in CPRS GUI 26)

> ![](pxrm-2-6-user-manual/027.png)

> Chapter 3: Processing Mental Health Reminders, cont’d

> AUDC as seen in CPRS GUI V27

> ![](pxrm-2-6-user-manual/028.png)

> Chapter 3: Processing Mental Health Reminders, cont’d

![](pxrm-2-6-user-manual/029.png)

> Chapter 3:

> Processing Mental Health Reminders, cont’d

> Example: Eval for Abnl Involuntary Movements

![](pxrm-2-6-user-manual/030.png)

> Chapter 3: Processing Mental Health Reminders, cont’d

> Example: AIMS Mental Health Instrument

![](pxrm-2-6-user-manual/031.png)

<table>
<colgroup>
<col style="width: 1%" />
<col style="width: 29%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><span id="Chapter_4:_Using_Reminder_Reports" class="anchor"></span><strong>Chapter 4: Using Reminder Reports</strong></p>
</blockquote>
<p><strong>TIP:</strong></p>
<blockquote>
<p>Clinicians should work with their site’s clinical reminder coordinator or Clinical Application Coordinator to design and validate reports used at their site.</p>
</blockquote>
<p>Reporting can be resource- intensive and many sites have elected to centralize the access to run reports. However, limited report templates may be available to selected clinicians who work closely with clinical reminders or QM at their site.</p></th>
<th><blockquote>
<p><strong>Chapter 4: Using Reminder Reports</strong></p>
<p>Reminder reports allow you to do large and small-scale comparisons of clinics, divisions, teams, and providers and can help in finding patients who have “slipped through the cracks.”</p>
</blockquote>
<ul>
<li><p>Find out how well your team is doing with immunizations or diabetes care or pain assessments.</p></li>
<li><p>Check on patients with appointments this week who might need pneumococcal immunization, a diabetic foot exam and education, or needs a pain assessment.</p></li>
<li><p>Look at a group of patients for a research project – patients with a creatinine between 1.5 and 5 who do not have diabetes who are under the age of 80.</p></li>
</ul>
<blockquote>
<p>Reports allow you to verify diagnoses, verify that appropriate treatment was given, identify patients requiring intervention, and validate effectiveness of care.</p>
<p>Reminder reports are very flexible. Reports can be run on:</p>
</blockquote>
<ul>
<li><p>Location(s)</p></li>
</ul>
<blockquote>
<p>-One or more inpatient hospital locations</p>
<p>-Current inpatients</p>
<p>-Patients admitted during a date range</p>
</blockquote>
<ul>
<li><p>Alphabetical</p></li>
<li><p>Sorted by ward/bed</p></li>
</ul>
<blockquote>
<p>-one or more outpatient hospital locations</p>
<p>-all hospital locations</p>
<p>-stop code(s)</p>
<p>-clinic group(s)</p>
</blockquote>
<ul>
<li><p>OERR Team(s)</p></li>
<li><p>PCMM team(s),</p></li>
<li><p>PCMM provider(s)</p></li>
<li><p>Reminder patient list(s).</p></li>
</ul>
<blockquote>
<p>Reports can be combined or kept separate for one or more facility Report results can display:</p>
</blockquote>
<ul>
<li><p>Summary results (numbers only)</p></li>
<li><p>Detailed results (patients’ names).</p></li>
</ul>
<blockquote>
<p>-Identifier: Entire social security number or last 4 numbers of social security number only</p>
<p>-Sort alphabetically or by date of the next clinic visit.</p>
<p>Reports can be run on either on patients with Past visits or with Future visits.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Chapter 4: Using Reminder Reports

> TIP:

> Reminders Due Report:

> The summary report may be run for several reminders.

> The detailed report may only be run for one reminder

> Reminder Reports

> Reminders Due Report

> For a selected reminder, the report lists any reminders that are currently due. Reports can be defined by the following criteria:

- Individual Patient
- Reminder Patient List (all patients on a patient list created through the Patient List options)
- Hospital Location (all patients with encounters)
- OE/RR Team (all patients in team)
- PCMM Provider (all practitioner patients)
- PCMM Team (all patients in team)

> Summary report: displays totals of how many patients of those selected have reminders due.

> Detailed report: displays patients (in alphabetical order) with reminders due. The report displays for each patient the date the reminder is due, the date the reminder was last done, and next appointment date. The detailed report can also list all future appointments, if specified. Detailed reports for Location or Provider may also be sorted by next appointment date.

> Reports by Hospital Location, Provider, or Team print a separate report for each Hospital Location, Provider, or Team selected.

> Reports for all Hospital Locations are not separated by individual locations. The report by Hospital Location can report either current inpatients or admissions within a selected date range.

> Chapter 4: Using Reminder Reports

> Reminder Reports

> Report templates

> The selection criteria used for the Reminders Due reports may be saved into a report template file, with a user-specified identifier, as the report is being run.

> When running the Reminder Due report, you may select from an existing template and run a new report using the parameters from the selected template. The prompts for date range and sort order are displayed, but all other parameters are taken from the previous report. If you select a print template, you may also edit the template and/or copy to a new template before running the report.

> *Scenario: How many patients are not receiving reminders who should be for Hepatitis C?*

> A report can be prepared that compares “Applicable” reminders to those that have been defined as “Due.” The difference may be a missed opportunity. This can be done by individual provider or for all providers in a location or medical center, as a quality assurance measure. The example below shows a summary report where the reminders selected are all related to Hepatitis C. This illustrates how you could use the summary report as part of a larger strategy for implementing and managing a Hepatitis C guideline using reminders.

> Example Report

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 12%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p># Patients with Reminder Applicable Due</p>
<p>Hep C Risk Factor Screen 172 16</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hep C Test for Risk</p>
</blockquote></td>
<td>30</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hep C Diagnosis Missed</p>
</blockquote></td>
<td>0</td>
<td><blockquote>
<p>0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Hep C Diagnosis</p>
</blockquote></td>
<td>36</td>
<td><blockquote>
<p>36</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hep C- Dz &amp; Trans Ed</p>
</blockquote></td>
<td>36</td>
<td><blockquote>
<p>27</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Hep C - Eval for Rx</p>
</blockquote></td>
<td>36</td>
<td><blockquote>
<p>15</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Chr Hep - Hep A Titer</p>
</blockquote></td>
<td>45</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Hepatitis A Vaccine</p>
</blockquote></td>
<td>19</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Chr Hepatitis - AFP</p>
</blockquote></td>
<td>12</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Chr Hepatitis - U/S</p>
<p>Report run on 175 patients.</p>
</blockquote></td>
<td>13</td>
<td><blockquote>
<p>6</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 0%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><span id="Chapter_5:_Health_Summaries_and_Clinical" class="anchor"></span><strong>Chapter 5: Health Health Su Summaries and</strong></p>
<p><strong>Clinical</strong> Reminder item</p>
</blockquote>
<p>summaries an</p>
<blockquote>
<p><strong>Reminders</strong> needs.</p>
</blockquote>
<p><strong>Health Summ</strong></p>
<blockquote>
<p>New Mental Health  <em>Reminders</em></p>
<p>Summary Components in due now.</p>
<p>Patch 6:  <em>Reminders</em></p>
</blockquote>
<p>the last do</p>
<ul>
<li><p><em>Reminder</em></p>
<ul>
<li><p>Deta clini</p></li>
<li><p>Tex the code and</p></li>
<li><blockquote>
<p>Fina</p>
</blockquote></li>
</ul></li>
</ul>
<blockquote>
<p>NOTE: Sta</p>
<p>reminder</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p><strong>mmaries</strong></p>
<p>s can be added to health summary displays. Health</p>
</blockquote>
<p>d reminder definitions can be tailored to suit clinicians’</p>
<blockquote>
<p><strong>ary Reminder Components</strong></p>
<p><em>Due:</em> an abbreviated component indicating only what is</p>
<p><em>Summary</em>: this provides the status, the next due date, and ne date.</p>
<p><em>Maintenance:</em> this component provides:</p>
<p>ils about what was found from searching the <strong>V</strong><em>IST</em><strong>A</strong></p>
<p>cal data:</p>
<p>t related to the findings found or not found (as defined in reminder). This includes taxonomies (ICD or CPT</p>
<p>s), health factors, and test results related to the reminder computed findings (e.g., Body Mass Index).</p>
<p>l frequency and age range used for the reminder.</p>
</blockquote>
<p>tuses include “DUE SOON,” to allow you to process a in advance, if convenient.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6"><blockquote>
<p><strong>Example of <em>Reminder Due</em> as displayed on a health summary</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Advanced Directives Education Alcohol Abuse Education</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>--STATUS-- DUE NOW</p>
<p>DUE NOW</p>
</blockquote></td>
<td><blockquote>
<p>--DUE DATE-- DUE NOW</p>
<p>DUE NOW</p>
</blockquote></td>
<td><blockquote>
<p>--LAST DONE--</p>
<p>unknown</p>
<p>unknown</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p><strong>Example of Reminder Summary as displayed on a health summary</strong></p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>--STATUS-- --DUE DATE-- --LAST DONE--</p>
<p>Mammogram RESOLVED 05/01/2003 10/01/2002</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Pap Smear</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DUE NOW</p>
</blockquote></td>
<td><blockquote>
<p>06/01/2003</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>unknown</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Diabetic Eye Exam</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DUE NOW</p>
</blockquote></td>
<td><blockquote>
<p>06/01/2003</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>06/01/2002</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Example of Reminder Maintenance as displayed on a health summary

> <span id="_bookmark13" class="anchor"></span>Chapter 5: Health Summaries, cont’d

> Example: Health Summary on CPRS Report tab

> ![](pxrm-2-6-user-manual/032.png)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark14" class="anchor"></span><strong>Chapter 5: Health My Health<em>e</em>Vet He</strong></p>
<p><strong>Summaries,</strong></p>
<p><strong>cont’d</strong> Clinical Reminders support the My Healt display of clinical rem</p>
<p>My Health<em>e</em>Vet is a</p>
<p><strong>NOTE:</strong> information and tools</p>
</blockquote>
<p>The veteran’s private maximum extent pos</p>
<p>health record will be key portions of their</p>
<blockquote>
<p>securely stored and only New health summary accessible by the veteran the technical text and and others they have component. These co identified. detailed information</p>
<p>from within My Heal</p>
<p>summaries at a facilit</p>
</blockquote></th>
<th><blockquote>
<p><strong>alth Summary</strong></p>
</blockquote>
<p>V.2.0 contains new health summary components to h<em>e</em>Vet project. These components will allow</p>
<blockquote>
<p>inder information to patients.</p>
</blockquote>
<p>Web-based system that empowers veterans with so that they can improve their health to the sible. Participating veterans are given copies of electronic health records.</p>
<blockquote>
<p>components were devised that eliminate much of code information that is contained in the CM mponents will be used to display summary and on individual patient reminders to the patients th<em>e</em>Vet. They can be also used in other health</p>
<p>y if it is useful for display to users at the site.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Chapter 5: Health Summaries, cont’d

> Example: MHVS Health Summary

> Chapter 5: Health Summaries, cont’d

> Example: MHVS Health Summary, cont’d

> <span id="_bookmark15" class="anchor"></span>Chapter 5: Health Summaries, cont’d

> Example: Health Summary with MHAL and MHAS components

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 26%" />
<col style="width: 33%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Date</p>
</blockquote></th>
<th><blockquote>
<p>Instrument</p>
</blockquote></th>
<th><blockquote>
<p>Ordered by</p>
</blockquote></th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>05/14/07 15:08</p>
</blockquote></td>
<td><blockquote>
<p>AUDC</p>
</blockquote></td>
<td><blockquote>
<p>CRPROVIDER,THREE</p>
</blockquote></td>
<td>1A(1&amp;2)</td>
</tr>
<tr class="even">
<td><blockquote>
<p>05/14/07 15:08</p>
</blockquote></td>
<td><blockquote>
<p>PHQ9</p>
</blockquote></td>
<td><blockquote>
<p>CRPROVIDER,THREE</p>
</blockquote></td>
<td>1A(1&amp;2)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>05/14/07 15:08</p>
</blockquote></td>
<td><blockquote>
<p>PHQ-2</p>
</blockquote></td>
<td><blockquote>
<p>CRPROVIDER,THREE</p>
</blockquote></td>
<td>1A(1&amp;2)</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>MHAS - MHA Score (max 10 occurrences)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 30%" />
<col style="width: 9%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Date</p>
</blockquote></th>
<th><blockquote>
<p>Instrument</p>
</blockquote></th>
<th>Raw</th>
<th>Trans Scale</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>05/14/2007 15:08</p>
</blockquote></td>
<td>PHQ-2</td>
<td>5</td>
<td>Total</td>
</tr>
<tr class="even">
<td><blockquote>
<p>05/14/2007 15:08</p>
</blockquote></td>
<td>PHQ9</td>
<td>10</td>
<td>Total</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>05/14/2007 15:08</p>
</blockquote></td>
<td>AUDC</td>
<td>2</td>
<td>Total</td>
</tr>
<tr class="even">
<td colspan="4"><ul>
<li><p>END *</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Chapter 6: VA- Geriatric Extended Care (GEC) Referral

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Important:

> This GEC screening tool is for the purpose of evaluating a patient’s needs for extended care and is not to be used as the document to refer or place a patient. The document should be part of a packet of information obtained when placing a patient.

> Four different disciplines should complete the screening, making it less burdensome on any one individual.

> VA-Geriatric Extended Care Referral

> Overview

> Clinical Reminders includes a nationally standardized computer instrument called VA Geriatric Extended Care (GEC), which replaces paper forms for evaluating veterans for extended care needs. Paper forms that facilities use include VA Form 10-7108, VA Form 10064a- Patient Assessment Instrument (PAI), and VA Form 1204-Referral for Community Nursing Home Care (others sites use various instruments including Consults).

> The GEC Referral is comprised of four reminder dialogs: VA-GEC SOCIAL SERVICES, VA-GEC NURSING ASSESSMENT, VA-GEC CARE RECOMMENDATIONS and VA-GEC CARE

> COORDINATION. These dialogs are designed for use as Text Integration Utility (TIU) templates to enter data regarding the need for extended care. Data entered via the dialogs are captured as health factors to be used for local and national reporting.

> The software also includes a new report menu that may be used for local analysis.

> Chapter 6: GEC, cont’d

> Chapter 6: GEC, cont’d

> Chapter 6: GEC, cont’d

> GEC Referral Ad hoc Health Summaries

> Two health summary components were distributed with this software:

- GEC Completed Referral Count (GECC)
- GEC Health Factor Category (GECH)

> The first displays all GEC referral data according to the occurrence and time limits identified.

> If a user should have access to these GEC reports, they must have access to the Ad Hoc Health Summary type. (This can be set using GMTS GUI HS LIST PARAMETERS.)

> GEC Referral Reports

> The software includes a new set of reports that provide a variety of GEC health factor perspectives. The reports capture data elements for reporting and tracking use of the GEC Referral Screening Tool. The reports may be generated in formatted or delimited output. The Summary (Score) report provides summary (calculated) totals from specific sections of the screening tool identified by the Office of Geriatrics Extended Care.

> Chapter 6: GEC, cont’d

> GEC Referral Reminders and Dialogs

> The GEC reminders are comprised of dialogs and health factors only. They have neither cohort nor resolution logic, and will not become due. They are intended only as TIU templates and do not need to be assigned to the CPRS Cover Sheet. Due to potential complications with reporting and duplicate entries, it is recommended that the GEC dialogs not be added to the Reminders drawer/Cover sheet.

> The Referral was designed for inter-disciplinary use with dialogs created for separate services. However, a single user may perform them all. With only a few exceptions, each section of the dialogs is mandatory and is marked with an asterisk (\*). The completion of all four dialogs constitutes a discrete episode of the GEC Referral.

> The VA-GEC REFERRAL SOCIAL SERVICES, VA-GEC REFERRAL NURSING ASSESSMENT, and VA-GEC REFERRAL

> CARE RECOMMENDATIONS dialogs comprise the clinical screening. The VA-GEC REFERRAL CARE COORDINATION dialog is used administratively to record the arrangement of and funding for extended care services. These dialogs may be performed in any order that local practices dictate. However, it is expected the screening portion will be completed prior to the coordination of services. When the screen is complete, a consult order should be placed to the service responsible for arranging services.

> GEC Consult Order

> Most sites have either an individual or a service responsible for arranging and coordinating extended care services. To accommodate local business practices and flexibility, sites may associate any consult service (or menu) they already have in place. If none exist, the sites may create a consult or establish some alternative practice to ensure that both services are arranged and that the VA-GEC REFERRAL CARE COORDINATION dialog is completed.

> Sites will need to review the privileging status of those performing the GEC Referral. The staff assigned to place the consult order associated with the GEC dialogs will require the ability to place a consult order.

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Chapter 6: GEC GEC Interdisci Usage, cont’d</strong></p>
<p>The GEC Referral dia</p>
<p>also expected that the (ID) note. The Office parent ID note title be</p>
<p><strong>NOTE:</strong> “GEC EXTE</p>
<p>Refer to Appendix C in the <strong>Steps to use the GE</strong></p>
<p>TIU/ASU Implementation</p>
<p>Guide for complete 1. In the CPRS GUI instructions about 2. Click on New No Interdisciplinary Notes 1. When the Progres</p>
<p>Title box.</p>
</blockquote>
<ol start="2" type="1">
<li><p>The list of GEC</p></li>
<li><p>Select the first on</p></li>
</ol></th>
<th><blockquote>
<p><strong>plinary Notes</strong></p>
<p>logs are intended for use as TIU templates. It is y will be used as part of a TIU Interdisciplinary of Geriatrics Extended Care requests that the</p>
<p>:</p>
<p>NDED CARE REFERRAL”</p>
<p><strong>C Dialog templates:</strong></p>
<p>, open the NOTES tab. te.</p>
<p>s Note Properties box opens, type GEC in the</p>
</blockquote>
<p>dialog templates is displayed. e to process.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Selecting GEC REFERRAL CARE COORDINATION

> ![](pxrm-2-6-user-manual/033.png)

> Chapter 6: GEC Usage, cont’d

> This is first screen shot when you select GEC REFERRAL CARE COORDINATION. When you select one type of service, the screen for that service type expands. The next screen shots show each in expanded form.

> Example: GEC REFERRAL CARE COORDINATION Opening screen

![](pxrm-2-6-user-manual/034.png)

> Chapter 6: GEC Usage, cont’d

> This is the expanded screen when you select HOME CARE SERVICES in the GEC REFERRAL CARE COORDINATION dialog.

> Note the checkbox “CHECK TO SEE REFERRAL STATUS.” This is available on all dialog boxes and lets you see a real-time view of the current Referral’s dialog-completion status. It presents information similar to that found on the GEC Referral Status Display and can be used to determine if the Referral can be finalized.

> Example: Expanded screen for HOME CARE SERVICES

![](pxrm-2-6-user-manual/035.png)

> <span id="Chapter_7:_My_HealtheVet" class="anchor"></span>Chapter 7: My Health*e*Vet

> <span id="Chapter_8:_Women’s_Veterans_Health_Remin" class="anchor"></span>Chapter 8: Women’s Veterans Health Reminders

> Chapter 8: Women’s Veterans Health Reminders

> NOTE:

> See the WH Reminders Install and Setup Guide (PXRM_2_1_IG_PDF.) for complete instructions for setting up the WH reminders application.

> Integration with Women’s Health, cont’d

> Setup and implementation by local team

> Sites will need to determine if the review reminders should be used locally. If a site is not set up for automatic update of WH, these reminders will not come due, so releasing the review reminders and dialogs might be confusing.

> The VA-WH PAP SMEAR REVIEW RESULTS reminder will only come due if all of the following are true:

- PAP smear results are recorded in the VistA Lab package.
- VistA Lab package uses SNOMED codes.
- WH package has SNOMED codes mapped to the codes used by the VistA Lab package.
- WH parameters are set up to automatically receive VistA Lab results when the PAP smear procedure is verified and released.

> The VA-WH MAMMOGRAM REVIEW RESULTS reminder will only come due if all of the following are true:

- Mammogram results are recorded and verified in the VistA Radiology package.
- WH parameters are set up to automatically receive VistA Radiology results when the mammogram procedure is verified and released, and status of received mammogram result is set to OPEN.

> Chapter 9: Women’s Veterans Health Reminders

> NOTE:

> You can see more information about the guidelines that the reminder is based on by clicking the top checkbox in the dialog.

> Steps to use dialogs:

1.  On the CPRS cover sheet, click on the Reminders icon.
2.  Click on reminders in the Reminders box to see details of a reminder.
3.  Open the Notes tab and select New Note. Enter a title.
4.  Open the Reminders drawer and review the contents.
5.  Locate the Mammogram or Pap reminder you wish to complete (e.g., VA-WH Mammogram Screening) and click to open it.
6.  In the dialog box, check relevant actions.
7.  Finish the reminder processing.
8.  Review the text added to the note to assure its correctness.
9.  Ensure that the reminder can be satisfied by the individual finding items that were mapped to the reminder terms.

> Example: Mammogram Screening Dialog

> ![](pxrm-2-6-user-manual/036.png)

> Chapter 9: Women’s Veterans Health Reminders

> The notification letter can be modified at your local site.

> Review Results Dialogs

> If your site uses the Women’s Health package, you can review the results of pap smear lab tests or mammogram procedures. You can then send notifications to patients to inform them of the results. The example below shows the Mammogram Review Results dialog and demonstrates sending a notification letter indicating that there is no evidence of malignancy. A follow-up mammogram can be scheduled.

> Review Results Dialog

> ![](pxrm-2-6-user-manual/037.png)

> <span id="_bookmark19" class="anchor"></span>Q: Are the reminders our site has already defined compatible with the new Clinical Reminders V. 2.6 patch?

> A: Yes, a conversion utility is run when the package is installed that converts your reminders to the new file structure. Some reminders may need slight adjustments to work with the new functionality so if you notice any reminders that don’t seem to be working correctly, notify your reminder manager.

> Q: If orders are included in dialogs and I check these through the Notes tab in CPRS, are the orders actually placed, or is this just recording the intention to order something?

> A: The order is actually placed, just as if you had ordered through the Orders tab. If the order is set up as a quick order, it will go through immediately (when you click the Finish button); if not a quick order, further questions will be asked to complete the order. The order will still need to be signed.

> Q: When I click on a reminder to process, I get a message saying “no dialog is defined for this reminder.” What does this mean and what do I need to do?

> A: See your CAC or Clinical Reminders manager. They need to create and link a dialog for this reminder.

> Q: What do clinicians need to learn to use Clinical Reminders functionality?

> A: The most important things to learn will be related to changes in workflow. It will be important to coordinate orders that are placed through reminder dialogs with nurses and clerks. You can work with your CACs and teams to share the responsibility for reminders so that no individual is overwhelmed with reminders. Also, learning to use reports correctly to produce meaningful data will be essential.

> Q: Is there any way to do a reminder report on an individual finding item?

> We want to add a checkbox that indicates depression is a new diagnosis. Is there a way to do a reminder report just on that one finding that will tell us how many of the patients that were seen that this was applicable for?

> A: Set up a local reminder with that one finding as a resolution finding.

> Define the reminder USAGE field as Reports, and then it will not appear on the cover sheet.

> Additional trick:

> Make the frequency to be 1 day, and put an OR for the resolution logic and AND for the COHORT logic. That then gives you output in the CM or health summary that gives the date it was last done so not only do you get a list of folks who have the finding but you also can tell when it was entered.

> Q: When Clinical Maintenance is run on a reminder that is applicable due to a problem list entry, why is today's date pulled rather than the date of problem list entry?

> A: There are two dates associated with ICD9 diagnoses found in PROBLEM LIST. There is the date entered and the date last modified. The PRIORITY field is used to determine if a problem is chronic or acute. *If the problem is chronic, Clinical Reminders will use today’s date in its date calculations; otherwise it will use the date last modified.* Note that it only uses active problems unless the field USE INACTIVE PROBLEMS is yes.

> Q: I opened the Reminders Drawer and all my reminders have disappeared, what do I do?

> A: Check your View list (Appendix D); most likely nothing will be checked. Select the reminder categories you want displayed and click on them so the checkmark is displayed.

# Appendix A: FAQS, Hints, and Tips 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Version 2.0 Patch PXRM\2\6](#version-20-patch-pxrm26)
  - [Revision History](#revision-history)
  - [Patch 6 Updates to](#patch-6-updates-to)
    - [Updates to National Reminders](#updates-to-national-reminders)
  - [![](pxrm-2-6-user-manual/004.png)Chapter 1: Clinical Reminders and CPRS Overview](#pxrm-2-6-user-manual004pngchapter-1-clinical-reminders-and-cprs-overview)
  - [Chapter 2: Processing/ Resolving Clinical Reminders](#chapter-2-processing-resolving-clinical-reminders)
  - [Chapter 6: VA- Geriatric Extended Care (GEC) Referral](#chapter-6-va-geriatric-extended-care-gec-referral)
- [Appendix A: FAQS, Hints, and Tips](#appendix-a-faqs-hints-and-tips)
- [Appendix D: Depression Screening Reminder Definition](#appendix-d-depression-screening-reminder-definition)
- [Appendix E: Iraq & Afghan Post Deploy Screen](#appendix-e-iraq-afghan-post-deploy-screen)
- [Appendix F: TBI Screening Reminder Definition](#appendix-f-tbi-screening-reminder-definition)
- [Appendix G: PTSD Screening Reminder](#appendix-g-ptsd-screening-reminder)
- [Index](#index)
> Q: I tried to run a report last night, but got this message this morning when I went to look at the task number.

#### 6294955: ^PXRMXPR, Reminder Due Report - print. Device NT_SPOOL. VAH,ROU.

> From Yesterday at 13:14, By you. Created without being scheduled.
> Does this mean that there’s an error with the report processing?
> A: No, that message doesn’t mean there’s an error. Clinical Reminders processes its reports in two tasks, one for SORT and one for PRINT. The print task will always show “created without being scheduled” until the sort task is complete.
Tips:
> Clearing a Single Reminder
> You will probably process several reminders for a single visit. If you have entered information on a reminder, but you need to start over on that reminder only, you can click Clear on the reminder from the Reminders Drawer, and then click the Clear button in the Reminders dialog box. This removes all previous dialog selections from the reminder’s dialog box and removes the related text and data from the Progress Note Text box and the PCE data box for this reminder.
> You can now start processing again.
> NOTE: Clicking Clear will remove the information from only one reminder. Be careful that you are on the correct reminder before you click Clear.
![](pxrm-2-6-user-manual/038.png)
> Canceling Out of the Processing Dialog
> If you reach the Reminders processing dialog by mistake or you wish to delete information that you have entered and start over, click Cancel.
![](pxrm-2-6-user-manual/039.png)
> <span id="Appendix_B:_Glossary" class="anchor"></span>Acronyms
> AAC Austin Automation Center
> AIMS Abnormal Involuntary Movement Scale API Application Programmer Interface.
<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CAC Clinical Application Coordinator</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CNBD Cannot Be Determined (frequency) CPRS Computerized Patient Record System. DBIA Database Integration Agreement.</p>
<p>EPRP External Peer Review Program</p>
<p>EVS Enterprise VistA Service</p>
<p>GEC Geriatric Extended Care</p>
<p>GUI Graphical User Interface.</p>
<p>HSR&amp;D Health Services Research and Development HL7 Health Level 7</p>
<p>IHD Ischemic Heart Disease</p>
<p>LDL Low-density lipo-protein</p>
<p>MDD Major Depressive Disorder</p>
<p>MH Mental Health</p>
<p>MHA3 Mental Health Assistant 3</p>
<p>MHV My HealtheVet</p>
<p>OQP Office of Quality and Performance</p>
<p>PCE Patient Care Encounter</p>
<p>QUERI Quality Enhancement Research Initiative SAS Statistical Analysis System</p>
<p>SQA Software Quality Assurance</p>
<p>SRS Software Requirements Specification</p>
<p>TIU Text Integration Utilities</p>
<p>VHA Veterans Health Administration. VISN Veterans Integrated Service Networks. <strong>V</strong>IS<em>T</em><strong>A</strong> Veterans Health Information System and</p>
<p>Technology Architecture.</p>
<p><strong>National Acronym Directory</strong></p>
<p><strong>Definitions</strong></p>
<p><strong>AAC SAS Files</strong></p>
<p>AAC SAS files contain data that is equivalent to data stored in the Reminder Extract Summary entry in the Reminder Extract Summary file. AAC manages SAS files for use by specifically defined users.</p>
<p><strong>Applicable</strong></p>
<p>The number of patients whose findings met the patient cohort reminder evaluation.</p>
</blockquote></td>
</tr>
</tbody>
</table>
> CNBD Cannot Be Determined. If a frequency can’t be determined for a patient, the Status and Due Date will both be CNBD and the frequency display that follows the status line will be “Frequency: Cannot be determined for this patient.”
> Due
> The number of patients whose reminder evaluation status is due.
> National Database
> All sites running IHD and Mental Health QUERI software transmit their data to a compliance totals database at the AAC.
> Not Applicable
> The number of patients whose findings did not meet the patient cohort reminder evaluation.
> Not Due
> The number of patients whose reminder evaluation status is not due.
> Reminder Definitions
> Reminder Definitions comprise the predefined set of finding items used to identify patient cohorts and reminder resolutions. Reminders are used for patient care and/or report extracts.
> Reminder Dialog
> Reminder Dialogs comprise a predefined set of text and findings that together provide information to the CPRS GUI, which collects and updates appropriate findings while building a progress note.
> Reminder Patient List
> A list of patients that is created from a set of List Rules and/or as a result of report processing. Each Patient List is assigned a name and is defined in the Reminder Patient List File. Reminder Patient Lists may be used as an incremental step to completing national extract processing or for local reporting needs. Patient Lists created from the Reminders Due reporting process are based on patients that met the patient cohort, reminder resolution, or specific finding extract parameters. These patient lists are used only at local facilities.
> Reminder Terms
> Predefined finding items that are used to map local findings to national findings, providing a method to standardize these findings for national use.
> Report Reminders
> Reminders may be defined specifically for national reporting. Report Reminders do not have a related Reminder Dialog in CPRS and are not used by clinicians for patient care. However, clinical reminders that are used in CPRS may also be used for national reminder reporting. All reminders targeted for national reporting are defined in Extract Parameters.
> <span id="Appendix_C:_Edit_Cover_Sheet_Reminder_Li" class="anchor"></span>You can specify which reminders will appear on the cover sheet of CPRS. This is done by using the Edit Cover Sheet Reminder List option.
1.  While on the CPRS Cover Sheet, click on the Tools menu.
2.  From the drop-down menu that appears, click on Options. This screen appears:
![](pxrm-2-6-user-manual/040.png)
3.  Click on the Clinical Reminders button to get to the editing form.
> ![](pxrm-2-6-user-manual/041.png)
4.  Highlight an item in the Reminders not being displayed field and then click the Add arrow “\>” to add it to the Reminders being displayed field. You may hold down the Control key and select more than one reminder at a time.
5.  When you have all of the desired reminders in the field, you may highlight a reminder and use the up and down buttons on the right side of the dialog to change the order in which the reminders will be displayed on the Cover Sheet.
> New Reminders Parameters (ORQQPX NEW REMINDER PARAMS)
> If you have been assigned this parameter, you can also modify the reminders view on the coversheet.
1.  Click on the reminder button next to the CWAD button in the upper right hand corner of the CPRS GUI.
![](pxrm-2-6-user-manual/042.png)
2.  Click on Action, then click on Edit Cover Sheet Reminder List.
> ![](pxrm-2-6-user-manual/043.png)
![](pxrm-2-6-user-manual/044.png)
> This form provides very extensive cover sheet list management capabilities. It consists mainly of three large list areas.
- *Cover Sheet Reminders (Cumulative List)* displays selected information on the Reminders that will be displayed on the Cover Sheet.
- *Available Reminders & Categories* lists all available Reminders and serves as a selection list.
- *User Level Reminders* displays the Reminders that have been added to or removed from the cumulative list.
> You may sort the Reminders in *Cover Sheet Reminders (Cumulative List)* by clicking on any of the column headers. Click on the Seq (Sequence) column header to view the Reminders in the order in which they will be displayed on your coversheet.

# Appendix D: Depression Screening Reminder Definition 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA-DEPRESSION SCREENING No. 104

> Print Name: Depression Screening

> Class: NATIONAL

> Sponsor: Office of Patient Care Services Review Date:

> Rescission Date:

> Usage: CPRS, REPORTS

> Related VA-\* Reminder:

> Reminder Dialog: VA-DEPRESSION SCREEN Priority:

> Reminder Description:

> Screening for Depression using a standard tool should be done on a yearly basis. A positive PHQ-2 triggers the need for a PHQ-9.

> A PHQ-2 or a PHQ-9 is required on all patients unless there is a recent diagnosis of depression entered for an outpatient visit. Patients with a diagnosis of depression need additional f/u and treatment.

> This reminder requires entry of the PHQ2 into the Mental Health package after 1/1/08. The PHQ-9 must be entered in the MH package to resolve this reminder when applicable.

> Health factors for refusal, acute illness and for chronic cognitive impairment are included in this reminder.

> A PHQ-9 should be done for any positive PHQ-2. This screening reminder requires one of the following in order to be resolved: 1. Negative PHQ-2

> 2\. Positive PHQ-2 plus a PHQ-9 done on the same day or later than the most recent positive PHQ-2 3. Refusal

> Entry of chronic cognitive impairment makes this reminder NA.

> Reminder terms for health factors that represent prior depression screening using the PHQ-2 and PHQ-9 are included. The PHQ-2 has been the only accepted depression screening tool since 12/1/06. Map any local health factors for the PHQ-2 to these terms. Do not include any health factors for other depression screening tools.

> The reminder term VA-CHRONIC COGNITIVE IMPAIRMENT contains a health factor and also the BOMC from the MH package. Use this health factor with caution since it turns this reminder off permanently.

> Technical Description:

> Baseline Frequency:

> Do In Advance Time Frame: Do if DUE within 1 month Sex Specific:

> Ignore on N/A:

> Frequency for Age Range: 1 year for all ages Match Text:

> No Match Text:

> Findings:

> ---- Begin: VA-DEPRESSION DIAGNOSIS (FI(1)=RT(77)) ----------------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND NOT

> Beginning Date/Time: T-1Y

> Mapped Findings:

> Mapped Finding Item: TX.VA-DEPRESSION DX OUTPT VISIT

> End: VA-DEPRESSION DIAGNOSIS

> ---- Begin: VA-COGNITIVE IMPAIRMENT (FI(2)=RT(806)) ---------------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND NOT

> Mapped Findings:

> Mapped Finding Item: HF.SEVERE CHRONIC COGNITIVE IMPAIRMENT

> Health Factor Category: MENTAL HEALTH Mapped Finding Item: MH.BOMC

> MH Scale: 516 - Weighted error score Condition: I +V\>10

> End: VA-COGNITIVE IMPAIRMENT

> ---- Begin: VA-DEP PHQ2 NEGATIVE (FI(3)=RT(845)) ------------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Mapped Findings:

> Mapped Finding Item: HF.PHQ-2 NEGATIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 1/1/08

> Mapped Finding Item: MH.PHQ-2

> MH Scale: 492 - Depression Condition: I +V\<3

> End: VA-DEP PHQ2 NEGATIVE

> ---- Begin: VA-DEP PHQ2 POSITIVE (FI(4)=RT(846)) ------------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.PHQ-2 POSITIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 1/1/08

> Mapped Finding Item: MH.PHQ-2

> MH Scale: 492 - Depression Condition: I +V'\<3

> End: VA-DEP PHQ2 POSITIVE

> ---- Begin: VA-REFUSED DEPRESSION SCREENING (FI(5)=RT(73)) --------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Beginning Date/Time: T-30D

> Mapped Findings:

> Mapped Finding Item: HF.REFUSED DEPRESSION SCREENING

> Health Factor Category: MENTAL HEALTH

> ---- End: VA-REFUSED DEPRESSION SCREENING --------------------------------

> ---- Begin: VA-DEP PHQ9 NEGATIVE (FI(6)=RT(847)) ------------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Mapped Findings:

> Mapped Finding Item: MH.PHQ9

> MH Scale: 419 - Total Condition: I +V\<10

> End: VA-DEP PHQ9 NEGATIVE

> ---- Begin: VA-DEP PHQ9 POSITIVE (FI(7)=RT(848)) ------------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: MH.PHQ9

> MH Scale: 419 - Total Condition: I +V\>9

> End: VA-DEP PHQ9 POSITIVE

> ---- Begin: VA-MH ACUTE ILLNESS (FI(8)=RT(612025)) ----------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Beginning Date/Time: T-30D

> Mapped Findings:

> Mapped Finding Item: HF.UNABLE TO SCREEN - ACUTE ILLNESS

> Health Factor Category: MENTAL HEALTH

> End: VA-MH ACUTE ILLNESS

> Function Findings:

> ---- Begin: FF(1)---------------------------------------------------------

> Function String: (MRD(4)\>MRD(6,7))&(MRD(4)\>MRD(3))

> Expanded Function String:

> (MRD(VA-DEP PHQ2 POSITIVE)\>MRD(VA-DEP PHQ9 NEGATIVE, VA-DEP PHQ9 POSITIVE))&(MRD(VA-DEP PHQ2 POSITIVE)\>MRD( VA-DEP PHQ2 NEGATIVE))

> Found Text: A PHQ-2 was positive and no PHQ-9 has been done. Please perform a PHQ-9.

> End: FF(1)

> ---- Begin: FF(2)---------------------------------------------------------

> Function String: MRD(6,7)'\<MRD(4) Expanded Function String:

> MRD(VA-DEP PHQ9 NEGATIVE,VA-DEP PHQ9 POSITIVE)'\<MRD( VA-DEP PHQ2 POSITIVE)

> End: FF(2)

> Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient: (SEX)&(AGE)&'FI(1)&'FI(2)

> Expanded Patient Cohort Logic:

> (SEX)&(AGE)&'FI(VA-DEPRESSION DIAGNOSIS)&'FI(VA-COGNITIVE IMPAIRMENT)

> Customized RESOLUTION LOGIC defines findings that resolve the Reminder: FI(3)!(FI(6)!FI(7)&FF(2))!FI(5)

> Expanded Resolution Logic:

> FI(VA-DEP PHQ2 NEGATIVE)!(FI(VA-DEP PHQ9 NEGATIVE)!

> FI(VA-DEP PHQ9 POSITIVE)&FF(2))!FI(VA-REFUSED DEPRESSION SCREENING)

> Web Sites:

> Web Site URL: <http://www.oqp.med.va.gov/cpg/MDD/MDD_Base.htm>

> Web Site Title: VA CPG for Depressive Disorder

> Web Site URL: <http://www.oqp.med.va.gov/cpg/MDD/G/A_Keyp.pdf>

> Web Site Title: VA CPG Key Points of Module A (PC)

> Web Site URL: <http://www.oqp.med.va.gov/cpg/MDD/G/A_Pock.pdf>

> Web Site Title: VA CPG Pocket Card for Module A (PC)

# Appendix E: Iraq & Afghan Post Deploy Screen 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> REMINDER DEFINITION INQUIRY Oct 17, 2007 9:24:16 am Page 1

> VA-IRAQ & AFGHAN POST-DEPLOY SCREEN No. 568022

> Print Name: Iraq&Afghan Post-Deployment Screen

> Class: NATIONAL

> Sponsor: Office of Public Health and Environmental Hazards Review Date:

> Rescission Date:

> Usage: CPRS, REPORTS

> Related VA-\* Reminder:

> Reminder Dialog:

> Priority:

> Reminder Description:

> Patients who served in combat in either Operation Iraqi Freedom (Iraq, Kuwait, Saudi Arabia, Turkey) or in Operation Enduring Freedom (Afghanistan, Georgia, Kyrgyzstan, Pakistan, Tajikistan, Uzbekistan, The Philippines) should be screened for illnesses related to their service. Screening for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms should be part of the initial evaluation of these Veterans.

> COHORT: veterans with separation date after 9/11/01. This finding is part of the reminder term: VA-IRAQ/AFGHAN PERIOD OF SERVICE and is determined by a computed finding.

> An additional reminder term VA-ACTIVE DUTY is also available to cause patients to be part of the cohort. This term contains a computed finding for VA-PATIENT TYPE which can be used to include active duty patients.

> Sites that do not screen active duty patients may remove the computed finding from this reminder term.

> RESOLUTION: entry of a health factor for NO IRAQ/AFGHAN SERVICE which is found in the reminder term IRAQ/AFGHAN SERVICE NO will resolve the reminder. If the veteran served in Iraq or Afghanistan (IRAQ/AFGHAN SERVICE) then

1.  the area of service by country must be answered and 2. all the other items are required to resolve the reminder and must be completed after the date of the most recent service separation:
    1.  screen for PTSD,
    2.  screen for depression,
    3.  screen for alcohol use,
    4.  all 4 screening questions related to infectious diseases and other symptoms.

> The clinical maintenance will display information on which portions of the screen are not yet completed.

> All of the individual elements of the screening tool are exported with attached health factors and reminder terms. The national health factors and reminder terms for the 2 question depression screen are used for the depression screening. The reminder dialog for alcohol screening allows the use of the standard AUDIT-C tool from the Mental Health package or entry of a refusal or entry of a health factor for no alcohol in the past year. The reminder term for ALCOHOL USE SCREEN contains the AUDIT-C and CAGE from the Mental Health package, the health factor for no alcohol use in the past year and the health factor for refusal. Additional health factors are included for PTSD screening and for the Infectious Diseases/Chronic symptoms screening. If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder terms that are exported with this reminder.

> The HFs for all of these screens should be entered in the site parameters as ones that cannot be added outside of a reminder dialog. Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude these from the electronic encounter forms. Entry of these health factors should ONLY occur during reminder dialog use.

> Technical Description:

> Baseline Frequency:

> Do In Advance Time Frame: Wait until actually DUE Sex Specific:

> Ignore on N/A:

> Frequency for Age Range: 99Y - Once for all ages Match Text:

> No Match Text:

> Findings:

> ---- Begin: VA-IRAQ/AFGHAN SERVICE NO (FI(1)=RT(489)) -------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Mapped Findings:

> Mapped Finding Item: HF.NO IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

> End: VA-IRAQ/AFGHAN SERVICE NO

> ---- Begin: VA-IRAQ/AFGHAN PERIOD OF SERVICE (FI(2)=RT(490)) ------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND

> Beginning Date/Time: SEP 11, 2001

> Mapped Findings:

> Mapped Finding Item: CF.VA-LAST SERVICE SEPARATION DATE

> Beginning Date/Time: SEP 11, 2001

> ---- End: VA-IRAQ/AFGHAN PERIOD OF SERVICE -------------------------------

> ---- Begin: VA-IRAQ/AFGHAN SERVICE (FI(3)=RT(568012)) -------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

> Beginning Date/Time: 9/11/01

> End: VA-IRAQ/AFGHAN SERVICE

> ---- Begin: VA-DEPRESSION SCREEN FY07 (FI(4)=RT(857)) -------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: MH.PHQ-2

> MH Scale: 492 - Depression

> Mapped Finding Item: MH.PHQ9

> MH Scale: 419 - Total

> Mapped Finding Item: MH.DOM80 Ending Date/Time: 11/30/06

> MH Scale: 515 - Total

> Mapped Finding Item: MH.DOMG Ending Date/Time: 11/30/06

> MH Scale: 365 - Total

> Mapped Finding Item: MH.BDI Ending Date/Time: 11/30/06

> MH Scale: 331 - DEPRESSION SCORE

> Mapped Finding Item: MH.BDI2 Ending Date/Time: 11/30/07

> MH Scale: 332 - Total

> Mapped Finding Item: HF.DEP SCREEN 2 QUESTION POS Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 11/30/06

> Mapped Finding Item: HF.DEP SCREEN 2 QUESTION NEG Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 11/30/06

> Mapped Finding Item: MH.ZUNG Ending Date/Time: 11/30/06

> MH Scale: 453 - DEPRESSION

> Mapped Finding Item: MH.CRS Ending Date/Time: 11/30/06

> MH Scale: 347 - CRS TOTAL

> Mapped Finding Item: HF.PHQ-2 NEGATIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 10/1/07

> Mapped Finding Item: HF.PHQ-2 POSITIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 10/1/07

> End: VA-DEPRESSION SCREEN FY07

> ---- Begin: VA-ALCOHOL USE SCREEN (FI(6)=RT(488)) -----------------------

> Finding Type: REMINDER TERM

> Not Found Text: Screening for at risk alcohol use using the AUDIT-C screening tool should be performed yearly for any patient who has consumed alcohol in the past year. No record of prior screening for alcohol use was found in this patient's record.

> \\

> Mapped Findings:

Mapped Finding Item: MH.AUDC

> MH Scale: 276 - Total

> Mapped Finding Item: MH.CAGE Ending Date/Time: 10/1/03

> Mapped Finding Item: HF.NON-DRINKER (NO ALCOHOL FOR \>1 YR)

> Health Factor Category: ALCOHOL USE Ending Date/Time: 10/1/07

> Mapped Finding Item: HF.REFUSED ALCOHOL USE SCREENING

> Health Factor Category: ALCOHOL USE

> Mapped Finding Item: MH.AUDIT Ending Date/Time: 10/1/07

> MH Scale: 278 - Total

> End: VA-ALCOHOL USE SCREEN

> ---- Begin: VA-PTSD SCREEN (FI(7)=RT(568013)) ---------------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN NEGATIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 10/1/07

> Mapped Finding Item: HF.PTSD SCREEN POSITIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 10/1/07

> Mapped Finding Item: MH.PC PTSD

> MH Scale: 203 - Total

> End: VA-PTSD SCREEN

> ---- Begin: VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN) (FI(8)=RT(568015)) --

> Finding Type: REMINDER TERM

> Not Found Text: Screen for unexplained fevers that might

> represent occult malaria or infection with leishmaniasis.

> \\

> Mapped Findings:

> Mapped Finding Item: HF.UNEXPLAINED FEVERS SCREEN NEGATIVE

> Health Factor Category: IRAQ/AFGHANISTAN

> Mapped Finding Item: HF.UNEXPLAINED FEVERS SCREEN POSITIVE

> Health Factor Category: IRAQ/AFGHANISTAN

> ---- End: VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN) ------------------------

> ---- Begin: VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN) (FI(9)=RT(568017)) -----

> Finding Type: REMINDER TERM

> Not Found Text: Screen for symptoms of fatigue, headaches, muscle or joint pains, or forgetfulness that have lasted 3 months or longer and have interfered with daily activities.

> \\

> NEGATIVE

> POSITIVE

> Mapped Findings:

> Mapped Finding Item: HF.OTHER PHYSICAL SYMPTOMS SCREEN

> Health Factor Category: IRAQ/AFGHANISTAN

> Mapped Finding Item: HF.OTHER PHYSICAL SYMPTOMS SCREEN

> Health Factor Category: IRAQ/AFGHANISTAN

> ---- End: VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN) ---------------------------

> ---- Begin: VA-GI SYMPTOMS (IRAQ/AFGHANISTAN) (FI(10)=RT(568014)) -------

> Finding Type: REMINDER TERM

> Not Found Text: Screen for diarrhea or other GI complaints that might suggest giardia, amoebiasis or other GI infection.

> \\

> Mapped Findings:

> Mapped Finding Item: HF.GI SYMPTOMS SCREEN NEGATIVE Health Factor Category: IRAQ/AFGHANISTAN

> Mapped Finding Item: HF.GI SYMPTOMS SCREEN POSITIVE Health Factor Category: IRAQ/AFGHANISTAN

> ---- End: VA-GI SYMPTOMS (IRAQ/AFGHANISTAN) ------------------------------

> ---- Begin: VA-PERSISTENT RASH (IRAQ/AFGHANISTAN) (FI(11)=RT(568016)) ---

> Finding Type: REMINDER TERM

> Not Found Text: Screen for persistent rash that might

> represent infection with leishmaniasis.

> \\

> Mapped Findings:

> Mapped Finding Item: HF.SKIN LESION SCREEN NEGATIVE Health Factor Category: IRAQ/AFGHANISTAN

> Mapped Finding Item: HF.SKIN LESION SCREEN POSITIVE Health Factor Category: IRAQ/AFGHANISTAN

> ---- End: VA-PERSISTENT RASH (IRAQ/AFGHANISTAN) --------------------------

> ---- Begin: VA-PTSD AVOIDANCE ALL (FI(12)=RT(617)) ----------------------

> Finding Type: REMINDER TERM Ending Date/Time: 10/1/07

> Within Category Rank: 0

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - AVOIDANCE Health Factor Category: PTSD AVOIDANCE

> Mapped Finding Item: HF.PTSD SCREEN - NO AVOIDANCE Health Factor Category: PTSD AVOIDANCE

> End: VA-PTSD AVOIDANCE ALL

> ---- Begin: VA-PTSD DETACHMENT ALL (FI(13)=RT(620)) ---------------------

> Finding Type: REMINDER TERM Within Category Rank: 0

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - DETACHED Health Factor Category: PTSD DETACHMENT

> Mapped Finding Item: HF.PTSD SCREEN - NO DETACHMENT Health Factor Category: PTSD DETACHMENT

> End: VA-PTSD DETACHMENT ALL

> ---- Begin: VA-PTSD NIGHTMARES ALL (FI(14)=RT(618)) ---------------------

> Finding Type: REMINDER TERM Ending Date/Time: 10/1/07

> Within Category Rank: 0

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - NIGHTMARES Health Factor Category: PTSD NIGHTMARES

> Mapped Finding Item: HF.PTSD SCREEN - NO NIGHTMARES Health Factor Category: PTSD NIGHTMARES

> End: VA-PTSD NIGHTMARES ALL

> ---- Begin: VA-PTSD ON GUARD ALL (FI(15)=RT(619)) -----------------------

> Finding Type: REMINDER TERM Ending Date/Time: 10/1/07

> Within Category Rank: 0

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - ON GUARD Health Factor Category: PTSD ON GUARD

> Mapped Finding Item: HF.PTSD SCREEN - NO ON GUARD Health Factor Category: PTSD ON GUARD

> End: VA-PTSD ON GUARD ALL

> ---- Begin: VA-REFUSED PTSD SCREEN (FI(16)=RT(631)) ---------------------

> Finding Type: REMINDER TERM

> Found Text: Refused PTSD Screen

> Mapped Findings:

> Mapped Finding Item: HF.REFUSED PTSD SCREEN Health Factor Category: MENTAL HEALTH

> End: VA-REFUSED PTSD SCREEN

> ---- Begin: VA-REFUSED ALCOHOL SCREENING (FI(17)=RT(568018)) ------------

> Finding Type: REMINDER TERM

> Found Text: Refused Alcohol Screening

> Mapped Findings:

> Mapped Finding Item: HF.REFUSED ALCOHOL USE SCREENING

> Health Factor Category: ALCOHOL USE

> End: VA-REFUSED ALCOHOL SCREENING

> ---- Begin: VA-REFUSED DEPRESSION SCREENING (FI(18)=RT(73)) -------------

> Finding Type: REMINDER TERM

> Found Text: Refused Depression Screening

> Mapped Findings:

> Mapped Finding Item: HF.REFUSED DEPRESSION SCREENING

> Health Factor Category: MENTAL HEALTH

> ---- End: VA-REFUSED DEPRESSION SCREENING --------------------------------

> ---- Begin: VA-ACTIVE DUTY (FI(19)=RT(568019)) --------------------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: OR

> Mapped Findings:

> Mapped Finding Item: CF.VA-PATIENT TYPE Condition: I V="ACTIVE DUTY"

> End: VA-ACTIVE DUTY

> ---- Begin: VA-REFUSED ID & OTHER SX SCREEN (FI(20)=RT(568020)) ---------

> Finding Type: REMINDER TERM Beginning Date/Time: T-1Y

> Within Category Rank: 0

> Found Text: The patient declined to answer some or all of the infectious disease and other symptom questions. Please ask these screening questions again if they remain unaddressed.

> Mapped Findings:

> Mapped Finding Item: HF.REFUSED ID & OTHER SX SCREEN Health Factor Category: IRAQ/AFGHANISTAN

> ---- End: VA-REFUSED ID & OTHER SX SCREEN --------------------------------

> Function Findings:

> ---- Begin: FF(1)---------------------------------------------------------

> Function String: MRD(1)\>MRD(2) Expanded Function String:

> MRD(VA-IRAQ/AFGHAN SERVICE NO)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Not Found Text: The patient's most recent service separation date is more recent than their last screening

> \- rescreening is needed after any new period of service.

> End: FF(1)

> ---- Begin: FF(2)---------------------------------------------------------

> Function String: MRD(7,12,13,14,15)\>MRD(2) Expanded Function String:

> MRD(VA-PTSD SCREEN,VA-PTSD AVOIDANCE ALL,VA-PTSD DETACHMENT ALL, VA-PTSD NIGHTMARES ALL,VA-PTSD ON GUARD ALL)\>MRD(

> VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Found Text: 1. PTSD Screening completed since service discharge

> Not Found Text: 1. PTSD Screen NEEDED

> End: FF(2)

> ---- Begin: FF(3)---------------------------------------------------------

> Function String: MRD(4)\>MRD(2) Expanded Function String:

> MRD(VA-DEPRESSION SCREEN FY07)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Found Text: 2. Depression Screening completed since service discharge

> Not Found Text: 2. Depression Screening NEEDED

> End: FF(3)

> ---- Begin: FF(4)---------------------------------------------------------

> Function String: MRD(6)\>MRD(2) Expanded Function String:

> MRD(VA-ALCOHOL USE SCREEN)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Found Text: 3. Alcohol Screening completed since service discharge

> Not Found Text: 3. Alcohol Screening NEEDED

> End: FF(4)

> ---- Begin: FF(5)---------------------------------------------------------

> Function String: MRD(10,20)\>MRD(2)!'(FI(2)!FI(19))

> Expanded Function String:

> MRD(VA-GI SYMPTOMS (IRAQ/AFGHANISTAN),VA-REFUSED ID & OTHER SX SCREEN)\> MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!'(FI(

> VA-IRAQ/AFGHAN PERIOD OF SERVICE)!FI(VA-ACTIVE DUTY))

> Found Text: 4A. Screen for GI symptoms done or not required.

> Not Found Text: 4A. Screen for GI symptoms NEEDED

> End: FF(5)

> ---- Begin: FF(6)---------------------------------------------------------

> Function String: MRD(8,20)\>MRD(2)!'(FI(2)!FI(19))

> Expanded Function String:

> MRD(VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN),

> VA-REFUSED ID & OTHER SX SCREEN)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!' (FI(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!FI(VA-ACTIVE DUTY))

> Found Text: 4B. Screen for Fevers done or not required.

> Not Found Text: 4B. Screen for Fevers NEEDED

> End: FF(6)

> ---- Begin: FF(7)---------------------------------------------------------

> Function String: MRD(11,20)\>MRD(2)!'(FI(2)!FI(19))

> Expanded Function String:

> MRD(VA-PERSISTENT RASH (IRAQ/AFGHANISTAN),

> VA-REFUSED ID & OTHER SX SCREEN)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!'

> (FI(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!FI(VA-ACTIVE DUTY))

> Found Text: 4C. Screen for Skin Rash done or not required.

> Not Found Text: 4C. Screen for Skin Rash NEEDED

> End: FF(7)

> ---- Begin: FF(8)---------------------------------------------------------

> Function String: MRD(9,20)\>MRD(2)!'(FI(2)!FI(19))

> Expanded Function String:

> MRD(VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN),

> VA-REFUSED ID & OTHER SX SCREEN)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!' (FI(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!FI(VA-ACTIVE DUTY))

> Found Text: 4D. Screen for Other Symptoms done or not required.

> Not Found Text: 4D. Screen for Other Symptoms NEEDED

> End: FF(8)

> ---- Begin: FF(9)---------------------------------------------------------

> Function String: MRD(2)\>MRD(1,3) Expanded Function String:

> MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)\>MRD(VA-IRAQ/AFGHAN SERVICE NO, VA-IRAQ/AFGHAN SERVICE)

> Found Text: The patient's most recent service separation date is more recent than their last screening

> \- rescreening is needed after any new period of service.

> End: FF(9)

> General Patient Cohort Found Text:

> Patients who served in combat in either Iraq (Operation Iraqi Freedom) or in Afghanistan (Operation Enduring Freedom) should be screened for illnesses related to their service. Screening for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms should be part of the initial evaluation of these Veterans.

> Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient: (SEX)&(AGE)&FI(2)!FI(19)

> Expanded Patient Cohort Logic:

> (SEX)&(AGE)&FI(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!FI(VA-ACTIVE DUTY)

> Customized RESOLUTION LOGIC defines findings that resolve the Reminder: (FI(1)&FF(1))!(FI(3)&(FF(2)!FI(16))&(FF(3)!FI(18))&(FF(4)!FI(17))&FF(5)& FF(6)&FF(7)&FF(8))

> Expanded Resolution Logic:

> (FI(VA-IRAQ/AFGHAN SERVICE NO)&FF(1))!(FI(VA-IRAQ/AFGHAN SERVICE)& (FF(2)!FI(VA-REFUSED PTSD SCREEN))&(FF(3)!

> FI(VA-REFUSED DEPRESSION SCREENING))&(FF(4)!

> FI(VA-REFUSED ALCOHOL SCREENING))&FF(5)&FF(6)&FF(7)&FF(8))

> Web Sites:

> Web Site URL: <http://www.oqp.med.va.gov/cpg/cpg.htm>

> Web Site Title: VA/DOD Guidelines - Office of Quality and Performance Web Site URL:

> <http://www.oqp.med.va.gov/cpg/MDD/MDD_Base.htm>

> Web Site Title: VA/DOD Depression Guideline

> Web Site URL: <http://www.oqp.med.va.gov/cpg/cpgn/mus/mus_base.htm>

> Web Site Title: VA/DOD Medically Unexplained Symptoms: Pain and Fatigue

> Web Site URL: <http://www.oqp.med.va.gov/cpg/PDH/PDH_base.htm>

> Web Site Title: Post Deployment Health Evaluation and Management

> Web Site URL: <http://www.oqp.med.va.gov/cpg/SUD/SUD_Base.htm>

> Web Site Title: VA/DOD Substance Abuse Guideline

> Web Site URL: <http://vaww.va.gov/environagents/>

#### Web Site Title: VA Environmental Agents Service

# Appendix F: TBI Screening Reminder Definition 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> REMINDER DEFINITION INQUIRY Oct 19, 2007 9:43:43 am Page 1

> VA-TBI SCREENING No. 793

> Print Name: TBI Screening

> Class: NATIONAL

> Sponsor: Office of Patient Care Services Review Date:

> Rescission Date:

> Usage: CPRS, DATA EXTRACT, REPORTS

> Related VA-\* Reminder:

> Reminder Dialog: VA-TBI SCREENING Priority:

> Reminder Description:

> Reminder is applicable once in a lifetime of all patients whose date of separation from the service is 9/11/01 or later and have had service in OEF/OIF. If Service Date of Separation is more recent than last TBI Screening, then reminder will be due again for patient.

> Reminder is resolved by completing the screen.

> Reminder creation requested by the Office of Patient Care Services. Designed by the TBI Screening Workgroup chaired by Dr. Barbara Sigford and based on a reminder from Minneapolis built by Ronald Patire and Dr. Brian Neil.

> Revisions June 2007:

1.  Refusal can be entered
2.  URLs added for information
3.  Screening done at another VA option added.
4.  Additional choices of for head injury added.

> Technical Description:

> Reminder is due for all patients with DOS of 9/11/01 or later. Reminder is resolved by any of the health factors associated with the responses of section 1; OR health factor for Previous TBI Diagnosis; OR health factor TBI PT Refused..

> Baseline Frequency:

> Do In Advance Time Frame: Wait until actually DUE Sex Specific:

> Ignore on N/A:

> Frequency for Age Range: 99Y - Once for all ages Match Text:

> No Match Text:

> Findings:

> ---- Begin: VA-IRAQ/AFGHAN PERIOD OF SERVICE (FI(1)=RT(490)) ------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND

> Beginning Date/Time: 09/11/2001

> Not Found Text: The patient's last service separation date is prior to 9/11/01.

> \\

> Mapped Findings:

> Mapped Finding Item: CF.VA-LAST SERVICE SEPARATION DATE

> Beginning Date/Time: SEP 11, 2001

> ---- End: VA-IRAQ/AFGHAN PERIOD OF SERVICE -------------------------------

> ---- Begin: VA-ACTIVE DUTY (FI(2)=RT(568019)) ---------------------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: OR

> Mapped Findings:

> Mapped Finding Item: CF.VA-PATIENT TYPE Condition: I V="ACTIVE DUTY"

> End: VA-ACTIVE DUTY

> ---- Begin: VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS (FI(3)=RT(824))

> Finding Type: REMINDER TERM Use in Resolution Logic: AND

> Mapped Findings:

> Mapped Finding Item: HF.TBI-SECTION I - NO Health Factor Category: TBI-SECTIONS

> Mapped Finding Item: HF.TBI-SECTION II - NO Health Factor Category: TBI-SECTIONS

> Mapped Finding Item: HF.TBI-SECTION III - NO Health Factor Category: TBI-SECTIONS

> Mapped Finding Item: HF.TBI-SECTION IV - NO Health Factor Category: TBI-SECTIONS

> Mapped Finding Item: HF.TBI-SECTION IV - YES Health Factor Category: TBI-SECTIONS

> Mapped Finding Item: HF.TBI-SCREENED PREVIOUSLY Health Factor Category: TBI-SECTIONS

> ---- End: VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS ---------------

> ---- Begin: VA-IRAQ/AFGHAN SERVICE NO (FI(4)=RT(489)) -------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Found Text: The record indicates that the patient did not serve in OEF or OIF.

> \\

> Mapped Findings:

> Mapped Finding Item: HF.NO IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

> End: VA-IRAQ/AFGHAN SERVICE NO

> ---- Begin: VA-IRAQ/AFGHAN SERVICE (FI(5)=RT(568012)) -------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

> Beginning Date/Time: 9/11/01

> End: VA-IRAQ/AFGHAN SERVICE

> ---- Begin: VA-TBI-PREVIOUS TBI DX (FI(6)=RT(828)) ----------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Beginning Date/Time: 9/11/01

> Found Text: Patient has documentation of previous TBI diagnosis on chart.

> Mapped Findings:

> Mapped Finding Item: HF.TBI-PREVIOUS TBI DX Health Factor Category: TBI-SECTIONS

> End: VA-TBI-PREVIOUS TBI DX

> ---- Begin: VA-TBI-PT REFUSAL (FI(7)=RT(829)) ---------------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Beginning Date/Time: T-30D

> Mapped Findings:

> Mapped Finding Item: HF.TBI-PT REFUSAL Health Factor Category: TBI-SECTIONS

> Beginning Date/Time: T-6M

> End: VA-TBI-PT REFUSAL

> ---- Begin: VA-LAST SERVICE SEPARATION DATE (FI(8)=CF(27)) --------------

> Finding Type: REMINDER COMPUTED FINDING

> ---- End: VA-LAST SERVICE SEPARATION DATE --------------------------------

> Function Findings:

> ---- Begin: FF(1)---------------------------------------------------------

> Function String: MRD(4)\>MRD(1) Expanded Function String:

> MRD(VA-IRAQ/AFGHAN SERVICE NO)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Not Found Text: The patient's most recent service separation date is more recent than their last screening

> \- if the patient was discharged after 9/11/01 then rescreening is needed after any new

> period of service.

End: FF(1)

> ---- Begin: FF(2)---------------------------------------------------------

> Function String: MRD(3)\>MRD(1) Expanded Function String:

> MRD(VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS)\>MRD( VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> End: FF(2)

> ---- Begin: FF(3)---------------------------------------------------------

> Function String: MRD(1)\>MRD(4,5) Expanded Function String:

> MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)\>MRD(VA-IRAQ/AFGHAN SERVICE NO, VA-IRAQ/AFGHAN SERVICE)

> Found Text: The patient's most recent service separation date is more recent than their last screening

> \- if the patient was discharged after 9/11/01 then rescreening is needed after any new period of service.

> End: FF(3)

> General Patient Cohort Found Text:

> Patients who served in combat in either Iraq (Operation Iraqi Freedom) or in Afghanistan (Operation Enduring Freedom) should be screened for Traumatic Brain Injury.

> General Patient Cohort Not Found Text:

> Patients who were discharged from the service prior to 9/11/01 or who did NOT serve in OEF or OIF do NOT need to be screened for TBI.

> Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient: (SEX)&(AGE)&FI(1)!FI(2)

> Expanded Patient Cohort Logic:

> (SEX)&(AGE)&FI(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!FI(VA-ACTIVE DUTY)

> Customized RESOLUTION LOGIC defines findings that resolve the Reminder: (FI(4)&FF(1))!(FI(3)&FF(2))!FI(6)!FI(7)

> Expanded Resolution Logic:

> (FI(VA-IRAQ/AFGHAN SERVICE NO)&FF(1))!

> (FI(VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS)&FF(2))! FI(VA-TBI-PREVIOUS TBI DX)!FI(VA-TBI-PT REFUSAL)

> Web Sites:

# Appendix G: PTSD Screening Reminder 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> REMINDER DEFINITION INQUIRY Oct 19, 2007 10:36:32 am Page 1

> VA-PTSD SCREENING No. 751

> Print Name: Screen for PTSD

> Class: NATIONAL

> Sponsor: Office of Patient Care Services Review Date:

> Rescission Date:

> Usage: CPRS, REPORTS

> Related VA-\* Reminder:

> Reminder Dialog: VA-PTSD SCREENING Priority:

> Reminder Description:

> PTSD screening due every 5 years for all patients. The reminder is set to also be due every year for the first 5 years after the last service separation date in the patient file. This facilitates repeated screening of patients after a recent period of military service.

> The reminder is not applicable to patients who have had a diagnosis of PTSD entered in the past 1 year.

> The reminder is resolved if the patient has had:

1.  An entry of a health factor that indicates that all 4 PTSD questions were answered (PTSD SCREEN NEGATIVE or PTSD SCREEN POSITIVE)
2.  Entry of health factors that indicated that all 4 questions were asked and answered.
3.  Entry of a health factor indicating that the patient declined/refused to answer the PTSD questions (resolves the reminder for

> 1 year).

4.  Entry of a PC-PTSD screen in the Mental Health package.

> This reminder is set up to require use of the Mental Health package after 1/1/08.

> Technical Description:

> Baseline Frequency:

> Do In Advance Time Frame: Do if DUE within 3 months Sex Specific:

> Ignore on N/A:

> Frequency for Age Range: 1 year for all ages Match Text:

> No Match Text:

> Findings:

> ---- Begin: VA-PTSD SCREEN (FI(1)=RT(568013)) ---------------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Occurrence Count: 4 Within Category Rank: 0

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN NEGATIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 10/1/07

> Mapped Finding Item: HF.PTSD SCREEN POSITIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 10/1/07

> Mapped Finding Item: MH.PC PTSD

> MH Scale: 203 - Total

> End: VA-PTSD SCREEN

> ---- Begin: VA-PTSD SCREEN NEGATIVE (FI(2)=RT(849)) ---------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN NEGATIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 10/1/07

> End: VA-PTSD SCREEN NEGATIVE

> ---- Begin: VA-PTSD SCREEN POSITIVE (FI(3)=RT(850)) ---------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN POSITIVE Health Factor Category: MENTAL HEALTH

> Ending Date/Time: 10/1/07

> End: VA-PTSD SCREEN POSITIVE

> ---- Begin: VA-REFUSED PTSD SCREEN (FI(4)=RT(631)) ----------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Beginning Date/Time: T-3M

> Mapped Findings:

> Mapped Finding Item: HF.REFUSED PTSD SCREEN Health Factor Category: MENTAL HEALTH

> End: VA-REFUSED PTSD SCREEN

> ---- Begin: VA-PTSD AVOIDANCE ALL (FI(5)=RT(617)) -----------------------

> Finding Type: REMINDER TERM Ending Date/Time: 1/1/08

> Occurrence Count: 2

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - AVOIDANCE Health Factor Category: PTSD AVOIDANCE

> Mapped Finding Item: HF.PTSD SCREEN - NO AVOIDANCE Health Factor Category: PTSD AVOIDANCE

> End: VA-PTSD AVOIDANCE ALL

> ---- Begin: VA-PTSD DETACHMENT ALL (FI(6)=RT(620)) ----------------------

> Finding Type: REMINDER TERM Ending Date/Time: 1/1/08 Occurrence Count: 2

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - DETACHED Health Factor Category: PTSD DETACHMENT

> Mapped Finding Item: HF.PTSD SCREEN - NO DETACHMENT Health Factor Category: PTSD DETACHMENT

> End: VA-PTSD DETACHMENT ALL

> ---- Begin: VA-PTSD NIGHTMARES ALL (FI(7)=RT(618)) ----------------------

> Finding Type: REMINDER TERM Ending Date/Time: 1/1/08 Occurrence Count: 2

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - NIGHTMARES Health Factor Category: PTSD NIGHTMARES

> Mapped Finding Item: HF.PTSD SCREEN - NO NIGHTMARES Health Factor Category: PTSD NIGHTMARES

> End: VA-PTSD NIGHTMARES ALL

> ---- Begin: VA-PTSD ON GUARD ALL (FI(8)=RT(619)) ------------------------

> Finding Type: REMINDER TERM Ending Date/Time: 1/1/08 Occurrence Count: 2

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - ON GUARD Health Factor Category: PTSD ON GUARD

> Mapped Finding Item: HF.PTSD SCREEN - NO ON GUARD Health Factor Category: PTSD ON GUARD

> End: VA-PTSD ON GUARD ALL

> ---- Begin: VA-LAST SERVICE SEPARATION DATE (FI(9)=CF(27)) --------------

> Finding Type: REMINDER COMPUTED FINDING

> Match Frequency/Age: 1 year for all ages Beginning Date/Time: T-5Y

> Found Text: The patient was recently discharged from the service. PTSD screening is due yearly for

> these patients.

> ---- End: VA-LAST SERVICE SEPARATION DATE --------------------------------

> ---- Begin: VA-LAST SERVICE SEPARATION DATE (FI(10)=CF(27)) -------------

> Finding Type: REMINDER COMPUTED FINDING

> Not Found Text: No discharge date from the service has been entered.

> ---- End: VA-LAST SERVICE SEPARATION DATE --------------------------------

> ---- Begin: VA-LIFE EXPECTANCY \<6 MONTHS (FI(11)=RT(805)) ---------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND NOT

> Beginning Date/Time: T-6M

> RT Mapped Finding: No Reminder Finding Found

> ---- End: VA-LIFE EXPECTANCY \<6 MONTHS -----------------------------------

> ---- Begin: VA-PTSD DIAGNOSIS (FI(12)=RT(858)) --------------------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND NOT

> Beginning Date/Time: T-1Y

> Mapped Findings:

> Mapped Finding Item: TX.VA-PTSD DIAGNOSIS

> End: VA-PTSD DIAGNOSIS

> ---- Begin: VA-COGNITIVE IMPAIRMENT (FI(13)=RT(806)) --------------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND NOT

> Mapped Findings:

> Mapped Finding Item: HF.SEVERE CHRONIC COGNITIVE IMPAIRMENT

> Health Factor Category: MENTAL HEALTH Mapped Finding Item: MH.BOMC

> MH Scale: 516 - Weighted error score Condition: I +V\>10

> End: VA-COGNITIVE IMPAIRMENT

> Function Findings:

> ---- Begin: FF(1)---------------------------------------------------------

> Function String: FI(10)&'FI(9) Expanded Function String:

> FI(VA-LAST SERVICE SEPARATION DATE)&'FI(VA-LAST SERVICE SEPARATION DATE)

> Match Frequency/Age: 5 years for all ages

> End: FF(1)

> ---- Begin: FF(2)---------------------------------------------------------

> Function String: FI(5)&FI(6)&FI(7)&FI(8) Expanded Function String:

> FI(VA-PTSD AVOIDANCE ALL)&FI(VA-PTSD DETACHMENT ALL)&FI( VA-PTSD NIGHTMARES ALL)&FI(VA-PTSD ON GUARD ALL)

> End: FF(2)

> Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient: (SEX)&(AGE)&'FI(11)&'FI(12)&'FI(13)

> Expanded Patient Cohort Logic:

> (SEX)&(AGE)&'FI(VA-LIFE EXPECTANCY \<6 MONTHS)&'FI(VA-PTSD DIAGNOSIS)&' FI(VA-COGNITIVE IMPAIRMENT)

> Customized RESOLUTION LOGIC defines findings that resolve the Reminder: FI(1)!FI(2)!FI(3)!FI(4)!(FF(2)&FI(8))

> Expanded Resolution Logic:

> FI(VA-PTSD SCREEN)!FI(VA-PTSD SCREEN NEGATIVE)!

> FI(VA-PTSD SCREEN POSITIVE)!FI(VA-REFUSED PTSD SCREEN)!(FF(2)& FI(VA-PTSD ON GUARD ALL))

> Web Sites:

> Web Site URL: <http://www.oqp.med.va.gov/cpg/PTSD/PTSD_Base.htm>

> Web Site Title: VA/DOD Guideline on PTSD

> Web Site URL: <http://vaww.oqp.med.va.gov/oqp_services/performance_measurement/uploads/MentalHe> alth/PCL_Primer.pdf

> Web Site Title: PCL-C Information

# Index 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AAC SAS Files, 64
> Acronyms, 64
> Appendix A: FAQS, Hints, and Tips, 61 Appendix B: Glossary, 64
> Appendix C: Edit Cover Sheet Reminder List, 67
> Appendix D: Depression Screening Reminder Definition, 70
> Appendix E: Iraq & Afghan Post Deploy Screen, 74
> Appendix F: TBI Screening Reminder Definition, 84
> Appendix G: PTSD Screening Reminder, 88 Applicable, 64
> Chapter 1: Clinical Reminders and CPRS, 7, 9
> Chapter 2: Resolving Clinical Reminders, 15 Chapter 3: Processing Mental Health
> Reminders, 18
> Chapter 4: Using Reminder Reports, 39 Chapter 5: Health Summaries and Clinical
> Reminders, 42
> Chapter 6: VA-Geriatric Extended Care, 48
> Chapter 7: My Health*e*Vet in Reminders, 56 Chapter 8: Women’s Veterans Health
> Reminders, 57, 58
> Cover Sheet Reminder List, 67 Definitions, 64
> Due, 65
> Edit Cover Sheet Reminder List, 67 FAQS, Hints, and Tips, 61
> GEC, 48
> Glossary, 64
> Mental Health Reminders, 18
> My Health*e*Vet Health Summary, 45 Not Applicable, 65
> Patient List, 65
> Reminder Definitions, 65
> Reminder Dialog, 65 Reminder Patient List, 65 Reminder Terms, 65
> Report Reminders, 66
> TIU Interdisciplinary (ID) note, 53 VA-Geriatric Extended Care, 48
> Women’s Veterans Health Reminders, 57
