---
title: PXRM*2*5 OEF/OIF Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: OEF/OIF
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*5
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - blockquote
  - strong
  - reminder
  - dialog
  - class
  - table
  - style
  - width
  - health
  - term
page_count: 0
word_count: 6304
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_5_sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_5_sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-5-oef-oif-setup-guide/001.png)

> Clinical Reminders

> OEF/OIF

## Patch PXRM\*2.0\*5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> SETUP GUIDE

## December, 2005

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Health Data Systems VISTA HSD&D

> Department of Veterans Affairs

> Revision History

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 13%" />
<col style="width: 48%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Revision Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Page or Chapter</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>December, 2005</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Updates to accommodate Patch 5.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> [Introduction 1](#introduction)

1.  [Verify correct installation of the packed reminder. 6](#post-installation-and-setup-steps)

[Setup Steps 10](#setup-steps)

[Term Mapping 10](#setup-steps)

2.  [Map local findings to the national Reminder Terms. 11](#Mapping_terms)
3.  [Run the Reminder Test option after term definition mapping is completed. 17](#_bookmark5)
4.  [Use the Reminder Dialog options to edit the national (exported) dialogs. 18](#Editing_the_Dialog)
5.  [Use ORWPCE EXCLUDE HEALTH FACTORS. 21](#Exclude_Health_Factors_from_Encounter_Fo)
6.  [Verify that the reminders function properly. 22](#Testing_the_Reminder)
7.  [Add the OEF/OIF reminder to the CPRS Cover Sheet. 24](#Add_Reminder_to_Cover_Sheet)

[Appendix: Iran & Afghan Post-Deployment Screen Reminder Definition and](#appendix-iran-afghan-post-deployment-screen-reminder-definition-and-dialog-examples) [Dialog Examples 27](#appendix-iran-afghan-post-deployment-screen-reminder-definition-and-dialog-examples)

[Index 47](#index)

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Patch PXRM\2.0\5](#patch-pxrm205)
  - [December, 2005](#december-2005)
- [Introduction](#introduction)
- [Post-Installation and Setup Steps](#post-installation-and-setup-steps)
- [Setup Steps](#setup-steps)
    - [Map local findings to the national Reminder Terms.](#map-local-findings-to-the-national-reminder-terms)
- [Appendix: Iran & Afghan Post-Deployment Screen Reminder Definition and Dialog Examples](#appendix-iran-afghan-post-deployment-screen-reminder-definition-and-dialog-examples)
    - [Reminder Dialog Screens](#reminder-dialog-screens)
- [Index](#index)
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Purpose of This Guide</strong></p>
</blockquote></th>
<th><blockquote>
<p>This Setup Guide is designed to help you prepare your site for the implementation of the new OEF/OIF Reminder. It includes detailed information about procedures that will get you up and running with this project.</p>
<p><strong>Target Audience</strong></p>
<p>We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package:</p>
</blockquote>
<ul>
<li><p>Information Resources Management (IRM)</p></li>
<li><p>Clinical Application Coordinator (CAC)</p></li>
<li><p>Enterprise <strong>V</strong><em>IST</em><strong>A</strong> Support (EVS)</p></li>
<li><p>Software Quality Assurance (SQA)</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Sources of Information</strong></p>
</blockquote></td>
<td><blockquote>
<p>You can retrieve documentation from the following websites: <a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a> Clinical Reminders main web page <a href="http://www.va.gov/vdl"><u>http://www.va.gov/vdl</u></a> <strong>V</strong><em>IST</em><strong>A</strong> Documentation Library (VDL)</p>
</blockquote></td>
</tr>
</tbody>
</table>
> <span id="Introduction" class="anchor"></span><u>Introduction</u>
<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Overview of the Project</strong></p>
<p>The Clinical Reminder, <em>Iraq &amp; Afghan Post- Deployment Screen,</em> was originally released with Patch 21 (PXRM*1.5*21).</p></th>
<th><blockquote>
<p><strong>Operation Enduring Freedom and Operation Iraqi Freedom</strong> The Clinical Reminder, <em>Iraq &amp; Afghan Post-Deployment Screen,</em> which identified veterans of Operation Enduring Freedom in Afghanistan and Operation Iraqi Freedom<em>,</em> has</p>
<p>been enhanced to take advantage of capabilities offered by the recent release of Clinical Reminders Version 2.0. The OEF/OIF data will be rolled up for regional and national reporting purposes. Due to the fast track that this project has been placed on, the project will be completed in two phases.</p>
</blockquote>
<ul>
<li><p><strong>Phase I</strong> include modifications and enhancements to the current Afghan/Iraq reminder to better meet the needs of the field and provide the information needed for reporting purposes. In Phase I, the clinical reminder for post- deployment screening will be due for patients whose latest Separation date greater than 09/11/01. It is also due for active duty patients being seen at the VA.</p></li>
</ul>
<blockquote>
<p><strong>Phase II Extract Reports &amp; National Rollup of Data</strong></p>
</blockquote>
<ul>
<li><p>Phase II is dependent on changes being made by Management Services to improve the quality and accuracy of a patient’s OEF and OIF combat data. The OEF/OIF Enrollment SRS will define functionality that will manage OEF/OIF Combat Veteran data. Management Systems will require OEF/OIF patients to first be a combat veteran with a combat from and to date, where the combat to date ends after 10/07/01, and secondarily have an OEF or OIF indication if the patient served in the OEF or OIF theatre during the combat service period. Patient combat data will be collected by clerks during enrollment, registration, or the first VA visit. Phase II Reminder development will be coordinated with Enrollment development to use the Combat Veteran data.</p></li>
<li><p>Phase II includes distribution of the national OEF/OIF clinical reminder/dialog again.</p></li>
<li><p>In Phase II, the clinical reminder for post-deployment screening will be due for patients whose latest Separation date greater than 09/11/01, or patients whose latest combat end date was greater than 10/07/01 for service in the OEF or OIF combat theatre. The reminder will continue to also be due for active duty patients being seen at the VA.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
> <u>Introduction, cont’d</u>
- Phase II will also include new OEF/OIF national reporting reminders, which will be used for roll-up of OEF/OIF totals to the Austin Automation Center (AAC). The project is restricted to use of existing Reminder Extract and HL7 messaging tools. The national reminder data sent to AAC will be totals only. No patient information will be sent to AAC. The new OEF/OIF transmission will be coordinated with AAC development.
- AAC will store facility results from regularly scheduled automated OEF/OIF national reporting for subsequent evaluation using SAS tools.
- A Clinical Reminder patch (PXRM\*2\*6) will include changes required to support new reporting extract requirements, as well as Reminder Extract Parameters, and Reporting Reminder definitions.
> <u>Introduction, cont’d</u>
<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Overview of Patch 5</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VA-IRAQ &amp; AFGHAN POST-DEPLOY SCREEN reminder</strong></p>
<p>This patch re-releases the VA-IRAQ &amp; AFGHAN POST- DEPLOY SCREEN reminder. Some of the changes to the reminder are:</p>
</blockquote>
<ol type="1">
<li><p>Each section can now be done individually so that one user may do part and someone else may do another piece. This means that someone may do a section and the reminder will remain due until all questions are complete.</p></li>
<li><p>If a section has been done recently (past 6 months) then it will be displayed in a closed format with a message that this was done recently and the user can click to open and repeat.</p></li>
<li><p>The clinical maintenance display will always show which pieces are complete and which are still pending.</p></li>
<li><p>The PTSD screen has been changed to capture the answers to the 4 questions as individual health factors so that the users do not have to do the scoring themselves.</p></li>
<li><p>The first question has been modified to capture OEF vs. OIF service and when one of these 2 options is chosen then the user has to choose one country for the most recent service.</p></li>
<li><p>Once the OEF vs. OIF service is captured (first question answered), this question is not asked again if the reminder is re-entered to complete other sections. This section will be displayed in a 'closed' format.</p></li>
<li><blockquote>
<p>There are refusal options for all four sections.</p>
</blockquote></li>
<li><p>There is a new computed finding for VA-PATIENT TYPE. This can be used (if a site chooses) to include active duty personnel in the cohort to be screened. The CF looks at the 'TYPE' field in the patient file.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
> <u>Introduction, cont’d</u>
> Reminder Changes, cont’d
> 9\. There is a URL in the reminder dialog that links to a paper copy of the questionnaire that can be used to obtain the information from the patients without having to read the questions to them. If you want to save a copy of this MS Word document on a local server, you can change the URL in the template field to point to your local server.
> This reminder will be placed in the REMINDER EXCHANGE file (#811.8). VA-IRAQ & AFGHAN POST- DEPLOY SCREEN
> A new Reminder Sponsor "Office of Public Health and Environmental Hazards" is being released with this patch.
> A change was made to the Data Dictionary Structure for file \#811.6. This change was done to make the structure similar to the other reminder files.

# Post-Installation and Setup Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><ol type="1">
<li><p><strong>Verify correct installation of the packed reminder.</strong></p></li>
</ol>
<blockquote>
<p>The post-install routine, PXRMP5I, installs the packed reminders into your Exchange File. If you discover that the reminders didn’t get installed, you can use the Reminders Exchange options on the Reminders Manager Menu to install the “packed” reminders.</p>
</blockquote>
<ol type="a">
<li><p>Using <em>Inquire about Reminder Definition</em> on the Reminder Management Menu, ensure that the four reminder definitions have been installed. Review the reminders to become familiar with the definitions and terms.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Select Reminder Managers Menu Option: <strong>RM</strong> Reminder Definition Management</p>
<p>RL List Reminder Definitions</p>
<p>RI Inquire about Reminder Definition RE Add/Edit Reminder Definition</p>
<p>RC Copy Reminder Definition</p>
<p>RA Activate/Inactivate Reminders</p>
<p>Select Reminder Definition Management Option: <strong>RI</strong> Inquire about Reminder Definition</p>
<p>Select Reminder Definition: <strong>VA-Iraq&amp;Afghan Post-Deployment</strong></p>
<p><strong>Screen</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>You cannot make changes to this national reminder. You may copy the national reminder to a local reminder definition name and make any changes necessary.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <u>Post-Installation & Setup (cont’d)</u>

2.  Using the Term Inquiry option on the Term Management Menu, verify that the following terms are on your system:

> Terms

1.  VA-IRAQ/AFGHAN SERVICE NO
2.  VA-IRAQ/AFGHAN PERIOD OF SERVICE
3.  VA-IRAQ/AFGHAN SERVICE
4.  VA-DEPRESSION SCREEN NEGATIVE
5.  VA-DEPRESSION SCREEN POSITIVE
6.  VA-ALCOHOL USE SCREEN
7.  VA-PTSD SCREEN
8.  VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)
9.  VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
10. VA-GI SYMPTOMS (IRAQ/AFGHANISTAN)
11. VA-PERSISTENT RASH (IRAQ/AFGHANISTAN)
12. VA-PTSD AVOIDANCE ALL
13. VA-PTSD DETACHMENT ALL
14. VA-PTSD NIGHTMARES ALL
15. VA-PTSD ON GUARD ALL
16. VA-REFUSED PTSD SCREEN
17. VA-REFUSED ALCOHOL SCREENING
18. VA-REFUSED DEPRESSION SCREENING
19. VA-REFUSED ID & OTHER SX SCREEN
20. VA-ACTIVE DUTY

> VA FileMan Print from the Reminder Term File

> You can also run a VA FileMan Print from the Reminder Term File (#811.5) that sorts by name, and then prints name, finding, and condition. This is a useful list, especially when needing to map many tests and you're not sure what values have been defined.

> <u>Post-Installation & Setup (cont’d)</u>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 20%" />
<col style="width: 37%" />
<col style="width: 5%" />
<col style="width: 20%" />
<col style="width: 10%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th colspan="5"><blockquote>
<p><strong>c. Verify that the VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN dialog is installed on your system.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><blockquote>
<p>Select Reminder Managers Menu Option: <strong>DM</strong> Reminder Dialog Management DP Dialog Parameters ...</p>
<p>DI Reminder Dialogs DR Dialog Reports ...</p>
<p>IA Inactive Codes Mail Message</p>
<p>Select Reminder Dialog Management Option: <strong>DI</strong> Reminder Dialogs</p>
<p>Dialog List Sep 22, 2005@11:35:09 Page: 1 of 25 REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<p>Item Reminder Name Linked Dialog Name &amp; Dialog Status</p>
</blockquote>
<ol type="1">
<li><p>A A BLOOD EXPOSURE DIABETIC EXAM DIALOG</p></li>
<li><p>A NEW REMINDER A NEW REMINDER Disabled</p></li>
<li><p>AGETEST VA-HEPC AUTOGENERATE TEST</p></li>
<li><p>ANY CHOLESTEROL SCREEN (M) ANY CHOLESTEROL SCREEN (M</p></li>
<li><p>ANY'S ANNUAL FLU SHOOT ANY'S ANNUAL FLU SHOOT</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>+</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>Enter ?? for more actions</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p><strong>&gt;&gt;&gt;</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>AR All reminders LR Linked Reminders QU Quit CV Change View RN Name/Print Name</p>
<p>Select Item: Next Screen// <strong>CV</strong> Change View Use CV – Change View to</p>
<p>change to a Dialog view.</p>
<p>Select one of the following:</p>
</blockquote>
<ol start="4" type="A">
<li><p>Reminder Dialogs</p></li>
<li><p>Dialog Elements</p></li>
<li><p>Forced Values</p></li>
<li><p>Dialog Groups</p></li>
</ol>
<blockquote>
<p>P Additional Prompts</p>
<p>R Reminders</p>
<p>RG Result Group (Mental Health) RE Result Element (Mental Health)</p>
<p>TYPE OF VIEW: R// D Reminder Dialogs</p>
<p><strong>Dialog List</strong> Sep 22, 2005@11:35:09 Page: 1 of 13 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)</p>
<p>Item Reminder Dialog Name Source Reminder Status</p>
</blockquote>
<ol type="1">
<li><p>571B SMOKING CESSATION EDUCATI</p></li>
<li><p>Agetest Agetest Disabled</p></li>
<li><p>BLOOD PRESSURE CHECK BLOOD PRESSURE CHECK Linked</p></li>
<li><p>DIABETIC EXAM DIALOG A A BLOOD EXPOSURE Linked</p></li>
<li><p>Diabetic Foot Inspection Exam VISN 12 Diabetic Foot Ins Linked</p></li>
<li><p>EDUTEST EDUTEST Disabled</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>+</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>+ Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
<td></td>
<td><strong>&gt;&gt;&gt;</strong></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AD CV</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Add Reminder Dialog PT List/Print All QU Change View RN Name/Print Name</p>
</blockquote></td>
<td><blockquote>
<p>Quit</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>Select Item: Next Screen// <strong>SL</strong> SL</p>
<p>Search for: <strong>VA-Iraq</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Use SL-Search List to jump to the reminder dialogs.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <u>Post-Installation & Setup (cont’d)</u>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>c. (cont’d) Verify that the Iraq &amp;Afghan dialog is installed on your system.</strong></p>
<p><strong>NOTE</strong>: Do not autogenerate dialogs for the reminders. Dialogs are included with the packed reminder installation.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>Dialog List Sep 22, 2005@11:35:34 Page: 14 of 16 <u>DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)</u></strong></p>
<p><strong>+Item Reminder Dialog Name Source Reminder Status</strong></p>
</blockquote>
<ol start="219" type="1">
<li><p><strong>VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT S VA-IRAQ &amp; AFGHAN POST-DEP Linked</strong></p></li>
<li><p><strong>VA-MST SCREENING *NONE* Linked</strong></p></li>
<li><p><strong>VA-PNEUMOVAX VA-PNEUMOVAX Linked</strong></p></li>
<li><p><strong>VA-PPD VA-PPD Linked</strong></p></li>
<li><p><strong>VA-PSA VA-PSA Disabled</strong></p></li>
<li><p><strong>VA-SEATBELT EDUCATION VA-SEATBELT EDUCATION Disabled</strong></p></li>
<li><p><strong>VA-WH MAMMOGRAM REVIEW RESULTS VA-WH MAMMOGRAM REVIEW RE Linked</strong></p></li>
<li><p><strong>VA-WH MAMMOGRAM SCREENING VA-WH MAMMOGRAM SCREENING Linked</strong></p></li>
<li><p><strong>VA-WH PAP SMEAR REVIEW RESULTS VA-WH PAP SMEAR REVIEW RE Linked</strong></p></li>
<li><p><strong>VA-WH PAP SMEAR SCREENING VA-WH PAP SMEAR SCREENING Linked</strong></p></li>
</ol></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>+ Enter ?? for more actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Find Next ‘VA Iraq’? Yes// <strong>no</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Setup Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder terms that are exported with this reminder.</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Term Mapping</strong></p>
<p>All of the individual elements of the screening tool are exported with attached health factors and reminder terms.</p>
<p>The national health factors and reminder terms for the 2-question depression screen are used for the depression screening.</p>
<p>The reminder dialog for alcohol screening allows the use of the standard AUDIT-C tool from the Mental Health package or entry of a refusal or entry of a health factor for no alcohol in the past year. The reminder term for ALCOHOL USE SCREEN contains the AUDIT-C and CAGE from the Mental Health package, the health factor for no alcohol use in the past year and the health factor for refusal.</p>
<p>Additional health factors are included for PTSD screening and for the Infectious Diseases/Chronic symptoms screening. If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder terms that are exported with this reminder.</p>
<p>The Health Factors for all of these screens should be entered in the site parameters as ones that cannot be added outside of a reminder dialog. Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude these from the electronic encounter forms. Entry of these health factors should ONLY occur during reminder dialog use.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="Mapping_terms" class="anchor"></span><u>Mapping terms</u>

### Map local findings to the national Reminder Terms.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Option: Reminder Term Management* on the *Reminder Management Menu.*

> Before using the OEF/OIF reminder, map the local findings your site uses to represent the national reminder terms, if necessary.

> Exported Terms

1.  VA-ACTIVE DUTY
2.  VA-ALCOHOL USE SCREEN
3.  VA-DEPRESSION SCREEN NEGATIVE
4.  VA-DEPRESSION SCREEN POSITIVE
5.  VA-GI SYMPTOMS (IRAQ/AFGHANISTAN)
6.  VA-IRAQ/AFGHAN PERIOD OF SERVICE
7.  VA-IRAQ/AFGHAN SERVICE
8.  VA-IRAQ/AFGHAN SERVICE NO
9.  VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
10. VA-PERSISTENT RASH (IRAQ/AFGHANISTAN)
11. VA-PTSD AVOIDANCE ALL
12. VA-PTSD DETACHMENT ALL
13. VA-PTSD NIGHTMARES ALL
14. VA-PTSD ON GUARD ALL
15. VA-PTSD SCREEN
16. VA-REFUSED ALCOHOL SCREENING
17. VA-REFUSED DEPRESSION SCREENING
18. VA-REFUSED ID & OTHER SX SCREEN
19. VA-REFUSED PTSD SCREEN
20. VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

> <u>Mapping terms</u>

> If desired, add local Health Factors or education topics representing these terms.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Mapping</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-ACTIVE DUTY</p>
</blockquote></td>
<td><blockquote>
<p>This new reminder term is available to allow active duty patients to be part of the cohort. This term contains a computed finding for VA-PATIENT TYPE, which can be used to include active duty patients. Sites that do not screen</p>
<p>active duty patients may remove the computed finding from this reminder term.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-ALCOHOL USE SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Add: Any local health factors for AUDIT-C, refusal of alcohol screening, or no alcohol in the past year.</p>
<p>The Mental Health tests for AUDIT-C and CAGE are already included in this term. If your site uses the 10 question AUDIT, then this should also be added to this term.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-DEPRESSION SCREEN NEGATIVE</p>
</blockquote></td>
<td><blockquote>
<p>Should already be mapped based on the national MH reminders. The national health factor is included in this term as well as all of the appropriate Mental Health tests. Any local health factors for negative depression screening should have already been mapped to this term when the national MH reminders were installed.</p>
<p>Do not include any health factors that represent non-specific results of depression screening. For example, a health factor of ‘Depression Screen Done’ is NOT appropriate to add to this</p>
<p>term.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-DEPRESSION SCREEN POSITIVE</p>
</blockquote></td>
<td><blockquote>
<p>Should already be mapped based on the national MH reminders. The national health factor is included in this term as well as all of the appropriate Mental Health tests. Any local health factors for positive depression screening should have already been mapped to this term when the national MH reminders were installed.</p>
<p>Do not include any health factors that represent non-specific results of depression screening. For example, a health factor of ‘Depression Screen Done’ is NOT appropriate to add to this term.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-GI SYMPTOMS (IRAQ/AFGHANISTAN)</p>
</blockquote></td>
<td><blockquote>
<p>This term represents the information collected from the reminder dialog that the question related to GI symptoms has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items</p>
<p>should be added to this term.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <u>Mapping terms</u>

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Mapping</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA- IRAQ/AFGHAN PERIOD OF SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>This term contains a computed finding that determines if the patient’s most recent service separation date was after 9/11/01. The computed finding is included to define the cohort of patients who need to be asked about service in the combat</p>
<p>arena.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA- IRAQ/AFGHAN SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>This term contains the health factor that is entered</p>
<p>from the dialog if the patient did, in fact, serve in the combat arena (on the ground, in the air or at sea).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA- IRAQ/AFGHAN SERVICE NO</p>
</blockquote></td>
<td><blockquote>
<p>This term contains the health factor that is entered from the dialog if the patient did not serve in the combat arena (on the ground, in the air or at sea).</p>
<p>This health factor resolves the reminder.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA- OTHER SYMPTOMS (IRAQ/AFGHANISTAN)</p>
</blockquote></td>
<td><blockquote>
<p>This term represents the information collected from the reminder dialog that the question related to fatigue, headaches, etc. has been answered. Separate health factors representing positive and negative answers to the question are included in this term.</p>
<p>Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA- PERSISTENT RASH (IRAQ/AFGHANISTAN)</p>
</blockquote></td>
<td><blockquote>
<p>This term represents the information collected from the reminder dialog that the question related to persistent rashes or skin ulcers has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to</p>
<p>this term.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-PTSD AVOIDANCE ALL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-PTSD DETACHMENT ALL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-PTSD NIGHTMARES ALL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-PTSD ON GUARD ALL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-PTSD SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>If your site does PTSD screening, map any local health factors or exams that represent positive or</p>
<p>negative screens for PTSD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-REFUSED ALCOHOL SCREENING</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Mapping</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-REFUSED DEPRESSION SCREENING</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-REFUSED ID &amp; OTHER SX SCREEN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-REFUSED PTSD SCREEN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)</p>
</blockquote></td>
<td><blockquote>
<p>This term represents the information collected from the reminder dialog that the question related to unexplained fever has been answered. Separate health factors representing positive and negative answers to the question are included in this term.</p>
<p>Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <u>Mapping terms</u>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Example</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>2. Map local findings to the national Reminder Terms (cont’d).</strong></p>
<p><em>Option: Add/Edit Reminder Term on Reminder Term Management Menu.</em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Mapping a Local Health Factor Finding to the National Reminder Term

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 37%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Select Reminder Term Management Option: <strong>te</strong> Add/Edit Reminder Term</p>
<p>Select Reminder Term: <strong>VA-ALCOHOL USE SCREEN</strong> NATIONAL</p>
<p>...OK? Yes// (Yes)</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Select FINDING ITEM: <strong>10-Question Audit</strong></p>
</blockquote></td>
<td colspan="2" rowspan="2"><blockquote>
<p>Enter local health factors or exams that your site uses to represent positive or negative</p>
<p>screens for alcohol use.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Searching for a MENTAL HEALTH INSTRUMENT, (pointed-</p>
<p>Searching for a MENTAL HEALTH INSTRUMENT TENS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>...OK? Yes// (Yes)</p>
<p>Are you adding 'TENS' as a new FINDINGS (the 6TH for this REMINDER TERM)? No//</p>
<p><strong>Y</strong> (Yes)</p>
<p>Editing Finding Number: 6 FINDING ITEM: <strong>10-Question Audit</strong></p>
<p>EFFECTIVE PERIOD:</p>
<p>USE INACTIVE PROBLEMS: WITHIN CATEGORY RANK: EFFECTIVE DATE:</p>
<p>MH SCALE: CONDITION:</p>
<p>CONDITION CASE SENSITIVE: RX TYPE:</p>
<p>Select FINDING ITEM:</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <u>Mapping terms</u>

> ent

> ,

> <span id="_bookmark5" class="anchor"></span><u>Testing the Reminder</u>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Test the reminder</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>3. Run the Reminder Test option after term definition mapping is completed.</strong></p>
<p><strong>Review the results of patient data with each of the findings mapped to the term.</strong></p>
<p><em>Option: Reminders Test</em> on the <em>Reminder Managers Menu</em></p>
<p>Select Reminder Managers Menu Option: <strong>RT</strong> Reminder Test Select Patient: <strong>CRPATIENT,SIX</strong> 4-30-44</p>
<p>666809999 YES EMPLOYEE</p>
<p>Enrollment Priority: GROUP 5 Category: IN PROCESS End Date:</p>
<p>Select Reminder: VA-Iraq&amp;Afghan Post-deployment Screen</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="Editing_the_Dialog" class="anchor"></span> <u>Editing the Dialog</u>

4.  Use the Reminder Dialog options to edit the national (exported) dialogs.

> After mapping local findings to the national terms, determine whether to use local findings as the data elements that are captured, or the national findings that are already mapped to the national terms. Review dialog elements in the national reminder dialog and change any national health factors to local health factors, if necessary. It is not unusual for local findings to be used in your national dialogs. Any local findings used in the national dialogs should be mapped to the appropriate national reminder term.

- If using local findings, edit the reminder dialog by identifying the element that allows for that data element to be collected. Change the finding item for that element to the local finding.

> Alternatively, use the Reminder Dialog options to copy the national dialog, dialog elements, and dialog groups to make local changes.

- Add local dialog elements with local Order Dialogs for additional ordering options for the clinicians. Some sites have clinicians order a consult to a service that provides PAP smears. If your site does this, copy the reminder dialog to a local reminder dialog and then add the local dialog element for the consult order to the reminder dialog so this practice can continue.

> The national reminders and dialogs can *only* be changed by changing the finding item in the nationally distributed elements to use your local finding item instead of the nationally distributed one.

> <u>Editing the Dialog</u>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 38%" />
<col style="width: 28%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="3"><blockquote>
<p><strong>Steps to add or edit dialog elements:</strong></p>
<p>a. Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI) and Change View (CV) to see the Dialog view:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Select Reminder Managers Menu Option: <strong>DM</strong> Reminder Dialog Management DP Dialog Parameters ...</p>
<p>DI Reminder Dialogs DR Dialog Reports ...</p>
<p>IA Inactive Codes Mail Message</p>
<p>Select Reminder Dialog Management Option: <strong>DI</strong> Reminder Dialogs</p>
<p>Dialog List Mar 24, 2004@08:52:46 Page: 1 of 18 REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<p>Item Reminder Name Linked Dialog Name &amp; Dialog Status</p>
</blockquote>
<ol type="1">
<li><p>A BLOOD EXPOSURE DIABETIC EXAM DIALOG</p></li>
<li><p>A NEW REMINDER A NEW REMINDER Disabled</p></li>
<li><p>AGP ABNORMAL WH STUFF</p></li>
</ol></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
<td><strong>&gt;&gt;&gt;</strong></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>AR All reminders LR Linked Reminders QU Quit CV Change View RN Name/Print Name</p>
<p>Select Item: Next Screen// <strong>CV</strong></p>
<p>Select one of the following: Select Change View (CV) to change to the</p>
</blockquote>
<ol start="4" type="A">
<li><p>Reminder Dialogs Dialog View</p></li>
<li><p>Dialog Elements</p></li>
<li><p>Forced Values</p></li>
<li><p>Dialog Groups</p></li>
</ol>
<blockquote>
<p>P Additional Prompts</p>
<p>R Reminders</p>
<p>RG Result Group (Mental Health) RE Result Element (Mental Health)</p>
<p>TYPE OF VIEW: R// <strong>D</strong> Reminder Dialogs</p>
<p>AD Add Reminder Dialog PT List/Print All QU Quit</p>
<p>Dialog List Mar 24, 2004@08:47 Page: 1 of 14 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)</p>
<p>Item Reminder Dialog Name Source Reminder Status</p>
</blockquote>
<ol type="1">
<li><p>A NEW BP CHECK *NONE* Disabled</p></li>
<li><p>A NEW REMINDER *NONE* Disabled</p></li>
<li><p>A NEW REMINDER DIALOG *NONE*</p></li>
</ol></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
<td><strong>&gt;&gt;&gt;</strong></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2" rowspan="2"><blockquote>
<p>CV Change View RN Name/Print Name Select Item: Next Screen// <strong>SL</strong> SL</p>
<p>Search for:</p>
</blockquote></td>
<td><blockquote>
<p>Select SL (Search List) to jump to the WH dialogs</p>
</blockquote></td>
<td rowspan="2"></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>

> <u>Editing the Dialog</u>

> E

> <span id="Exclude_Health_Factors_from_Encounter_Fo" class="anchor"></span> <u>Exclude Health Factors from Encounter Forms</u>

> <span id="Testing_the_Reminder" class="anchor"></span> <u>Testing the Reminder</u>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Test Reminder</strong></p>
</blockquote></th>
<th><ol start="6" type="1">
<li><p><strong>Verify that the reminders function properly.</strong></p>
<ol type="a">
<li><p>Run a Reminders Due Report to determine if the statuses reported are correct.</p></li>
</ol></li>
</ol>
<blockquote>
<p><em>Option: Reminders Due</em> on the <em>Reminder Reports menu</em></p>
<p>This report can be displayed at the beginning of the day for patients being seen that day. Reminder reports offer a way to review how the mapping and the local data will potentially be viewed by the extracts that will be sent to the Austin database from the reminders.</p>
</blockquote>
<ul>
<li><p>The reminder can be used in a reminder report to evaluate clinics or stop codes on their adherence/compliance with that reminder.</p></li>
<li><p>The report can be run to list individual patient names for chart review on reasons that the guideline was not or could not be achieved.</p></li>
<li><p>Clinics, stop codes, or divisions can be identified by summary reports using these reminders where there are differences in compliance or poor adherence to the guideline.</p></li>
</ul>
<ol start="2" type="a">
<li><blockquote>
<p>Use the Reminder Test option to test the reminder.</p>
</blockquote></li>
</ol>
<blockquote>
<p><em>Option: Reminders Test</em> on the <em>Reminder Management menu</em></p>
<p>1. Select a patient who had a screening done within the past year. Run the Reminder Test option on the VA-IRAQ &amp; AFGHAN POST-DEPLOYMENT SCREENING reminder definition. The status of the reminder should be “RESOLVED.” Alternatively, use the clinical maintenance view in the CPRS GUI. The status of the reminder should be “RESOLVED.”</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <u>Test Reminder</u>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Test Reminder</strong></p>
</blockquote></th>
<th><blockquote>
<p>3. Select a patient whose most recent screening took place within the past year and the results have been recorded.</p>
<p>Run the Reminder Test option on VA- Iraq &amp; Afghan Post- Deployment Screen reminder definition.</p>
<p>The status of the reminder should be “Applicable.”</p>
<p>Use the clinical maintenance view in the CPRS GUI. The status of the reminder should be “Applicable.”</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> <span id="Add_Reminder_to_Cover_Sheet" class="anchor"></span><u>Add Reminder to Cover Sheet</u>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Add Reminder to</strong> <strong>CPRS Cover Sheet</strong></p>
<p>NOTE: Make sure that New Reminders Parameter on the CPRS Configuration Menu is set to Yes. This is a prerequisite for using the “Edit Cover Sheet Reminder List” functionality.</p>
</blockquote></th>
<th><ol start="7" type="1">
<li><p><strong>Add the OEF/OIF reminder to the CPRS Cover Sheet.</strong></p>
<ol type="a">
<li><p>Open a patient chart, click on the reminders clock, and when the available Reminders window opens, click on Action, and then select “Edit Cover Sheet Reminder List.”</p></li>
</ol></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](pxrm-2-5-oef-oif-setup-guide/002.png)

> ![](pxrm-2-5-oef-oif-setup-guide/003.png)<u>Setup Guide</u>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Add Reminder to CPRS Cover Sheet</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Adding Reminder to Cover Sheet, cont’d</strong></p>
</blockquote>
<ol start="2" type="a">
<li><p>When the Cover Sheet Reminder List opens, set the Cover sheet parameter level. Click on the System, Division, Service, User Class, and/or User buttons, as appropriate for your site.</p></li>
<li><blockquote>
<p>Locate and click on the VA-IRAQ &amp; AFGHAN DEPLOY SCREENING reminder; click the Add button (or double-click the reminder).</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 86%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>CRPROVIDER,ONE</strong></th>
<th rowspan="2"></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><strong>C CRPROVIDER,ONE</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>C CRPROVIDER,ONE</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>CRCRPROVIDER,ONE</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <u>Setup Guide</u>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Add Reminder to CPRS Cover Sheet</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Adding Reminder to Cover Sheet, cont’d</strong></p>
<p>d. Click on the VA-IRAQ &amp; AFGHAN POST-DEPLOYMENT SCREEN reminder and click the Add button (or double-click the reminder).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

![](pxrm-2-5-oef-oif-setup-guide/004.png)

# Appendix: Iran & Afghan Post-Deployment Screen Reminder Definition and Dialog Examples 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reminder Definition

> REMINDER DEFINITION INQUIRY Sep 20, 2005 10:39:39 am Page 1

> VA-IRAQ & AFGHAN POST-DEPLOY SCREEN No. 568022

> Print Name: Iraq&Afghan Post-Deployment Screen

> Class: NATIONAL

> Sponsor:

> Review Date:

> Rescission Date:

> Usage: CPRS, REPORTS

> Related VA-\* Reminder:

> Reminder Dialog: VA-IRAQ & AFGHANISTAN POST DEPLOYMENT SCREEN

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

> Mapped Finding Item: CF.VA-DISCHARGE DATE Beginning Date/Time: SEP 11, 2001

> ---- End: VA-IRAQ/AFGHAN PERIOD OF SERVICE -------------------------------

> ---- Begin: VA-IRAQ/AFGHAN SERVICE (FI(3)=RT(568012)) -------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

> End: VA-IRAQ/AFGHAN SERVICE

> ---- Begin: VA-DEPRESSION SCREEN NEGATIVE (FI(4)=RT(80)) ----------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.DEP SCREEN 2 QUESTION NEG Health Factor Category: MENTAL HEALTH

> Mapped Finding Item: MH.DOM80

> Condition: I V=0

> Mapped Finding Item: MH.DOMG

> Condition: I V\<4

> Mapped Finding Item: MH.CRS

> MH Scale: 1 Condition: I V\<10

> Mapped Finding Item: MH.BDI

> MH Scale: 1 Condition: I V\<10

> Mapped Finding Item: MH.ZUNG

> MH Scale: 1 Condition: I V\<33

> End: VA-DEPRESSION SCREEN NEGATIVE

> ---- Begin: VA-DEPRESSION SCREEN POSITIVE (FI(5)=RT(81)) ----------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.DEP SCREEN 2 QUESTION POS Health Factor Category: MENTAL HEALTH

> Mapped Finding Item: MH.DOM80

> Condition: I V=1

> Mapped Finding Item: MH.DOMG

> Condition: I V\>3

> Mapped Finding Item: MH.CRS

> MH Scale: 1 Condition: I V\>9

> Mapped Finding Item: MH.BDI

> MH Scale: 1 Condition: I V\>9

> Mapped Finding Item: MH.ZUNG

> MH Scale: 1 Condition: I V\>32

> End: VA-DEPRESSION SCREEN POSITIVE

> ---- Begin: VA-ALCOHOL USE SCREEN (FI(6)=RT(488)) -----------------------

> Finding Type: REMINDER TERM

> Not Found Text: Screening for at risk alcohol use using the AUDIT-C screening tool should be performed yearly for any patient who has consumed alcohol in the past year. No record of prior screening for alcohol use was found in this patient's record.

> \\

> Mapped Findings:

Mapped Finding Item: MH.AUDC

> Mapped Finding Item: MH.CAGE Ending Date/Time: 10/1/03

> Mapped Finding Item: HF.NON-DRINKER (NO ALCOHOL FOR \>1 YR)

> Health Factor Category: ALCOHOL USE

> Mapped Finding Item: HF.REFUSED ALCOHOL USE SCREENING

> Health Factor Category: ALCOHOL USE

> Mapped Finding Item: MH.AUDIT

> End: VA-ALCOHOL USE SCREEN

> ---- Begin: VA-PTSD SCREEN (FI(7)=RT(568013)) ---------------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN NEGATIVE Health Factor Category: MENTAL HEALTH

> Mapped Finding Item: HF.PTSD SCREEN POSITIVE Health Factor Category: MENTAL HEALTH

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

> Mapped Findings:

> Mapped Finding Item: HF.OTHER PHYSICAL SYMPTOMS SCREEN

> Health Factor Category: IRAQ/AFGHANISTAN

> POSITIVE

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

> Finding Type: REMINDER TERM Within Category Rank: 0

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

> Finding Type: REMINDER TERM Within Category Rank: 0

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - NIGHTMARES Health Factor Category: PTSD NIGHTMARES

> Mapped Finding Item: HF.PTSD SCREEN - NO NIGHTMARES Health Factor Category: PTSD NIGHTMARES

> End: VA-PTSD NIGHTMARES ALL

> ---- Begin: VA-PTSD ON GUARD ALL (FI(15)=RT(619)) -----------------------

> Finding Type: REMINDER TERM Within Category Rank: 0

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN - ON GUARD Health Factor Category: PTSD ON GUARD

> Mapped Finding Item: HF.PTSD SCREEN - NO ON GUARD Health Factor Category: PTSD ON GUARD

> End: VA-PTSD ON GUARD ALL

> ---- Begin: VA-REFUSED PTSD SCREEN (FI(16)=RT(631)) ---------------------

> Finding Type: REMINDER TERM Beginning Date/Time: T-6M

> Found Text: Refused PTSD Screen

> Mapped Findings:

> Mapped Finding Item: HF.REFUSED PTSD SCREEN Health Factor Category: MENTAL HEALTH

> End: VA-REFUSED PTSD SCREEN

> ---- Begin: VA-REFUSED ALCOHOL SCREENING (FI(17)=RT(568018)) ------------

> Finding Type: REMINDER TERM

> Beginning Date/Time: T-6M

> Found Text: Refused Alcohol Screening

> Mapped Findings:

> Mapped Finding Item: HF.REFUSED ALCOHOL USE SCREENING

> Health Factor Category: ALCOHOL USE

> End: VA-REFUSED ALCOHOL SCREENING

> ---- Begin: VA-REFUSED DEPRESSION SCREENING (FI(18)=RT(73)) -------------

> Finding Type: REMINDER TERM Beginning Date/Time: T-6M

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

> Finding Type: REMINDER TERM Beginning Date/Time: T-6M

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

> Found Text: 1. PTSD Screening completed Not Found Text: 1. PTSD Screen NEEDED

> End: FF(2)

> ---- Begin: FF(3)---------------------------------------------------------

> Function String: MRD(4,5)\>MRD(2) Expanded Function String:

> MRD(VA-DEPRESSION SCREEN NEGATIVE,VA-DEPRESSION SCREEN POSITIVE)\>MRD( VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Found Text: 2. Depression Screening completed Not Found Text: 2. Depression Screening NEEDED

> End: FF(3)

> ---- Begin: FF(4)---------------------------------------------------------

> Function String: MRD(6)\>MRD(2) Expanded Function String:

> MRD(VA-ALCOHOL USE SCREEN)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Found Text: 3. Alcohol Screening completed Not Found Text: 3. Alcohol Screening NEEDED

> End: FF(4)

> ---- Begin: FF(5)---------------------------------------------------------

> Function String: MRD(10,20)\>MRD(2) Expanded Function String:

> MRD(VA-GI SYMPTOMS (IRAQ/AFGHANISTAN),VA-REFUSED ID & OTHER SX SCREEN)\> MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Found Text: 4A. Screen for GI symptoms completed Not Found Text: 4A. Screen for GI symptoms NEEDED

> End: FF(5)

> ---- Begin: FF(6)---------------------------------------------------------

> Function String: MRD(8,20)\>MRD(2) Expanded Function String:

> MRD(VA-UNEXPLAINED FEVER (IRAQ/AFGHANISTAN),

> VA-REFUSED ID & OTHER SX SCREEN)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Found Text: 4B. Screen for Fevers completed Not Found Text: 4B. Screen for Fevers NEEDED

> End: FF(6)

> ---- Begin: FF(7)---------------------------------------------------------

> Function String: MRD(11,20)\>MRD(2) Expanded Function String:

> MRD(VA-PERSISTENT RASH (IRAQ/AFGHANISTAN),

> VA-REFUSED ID & OTHER SX SCREEN)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Found Text: 4C. Screen for Skin Rash completed Not Found Text: 4C. Screen for Skin Rash NEEDED

> End: FF(7)

> ---- Begin: FF(8)---------------------------------------------------------

> Function String: MRD(9,20)\>MRD(2)

> Expanded Function String:

> MRD(VA-OTHER SYMPTOMS (IRAQ/AFGHANISTAN),

> VA-REFUSED ID & OTHER SX SCREEN)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Found Text: 4D. Screen for Other Symptoms completed Not Found Text: 4D. Screen for Other Symptoms NEEDED

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

> Web Site Title: VA/DOD Guidelines - Office of Quality and Performance

> Web Site URL: <http://www.oqp.med.va.gov/cpg/MDD/MDD_Base.htm>

> Web Site Title: VA/DOD Depression Guideline

> Web Site URL: <http://www.oqp.med.va.gov/cpg/cpgn/mus/mus_base.htm>

> Web Site Title: VA/DOD Medically Unexplained Symptoms: Pain and Fatigue

### Reminder Dialog Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If the first question is answered “yes,” then the rest of the dialog opens up. If the first question is answered “no,” then the user is done.

![](pxrm-2-5-oef-oif-setup-guide/005.png)

2.  When the dialog opens for a ‘yes’ answer, the first question prompts for the location of service. OIF options are on the first screen below and OEF options are on the next screen.

![](pxrm-2-5-oef-oif-setup-guide/006.png)![](pxrm-2-5-oef-oif-setup-guide/007.png)

3.  If the first question has already been answered “yes,” then it does not need to be answered again if subsequent users open the dialog to complete other sections. Note the radio button in front of the PTSD screen. This is necessary to allow the user to choose between doing the screen and entering a refusal (next slide).

![](pxrm-2-5-oef-oif-setup-guide/008.png)

> The refusal options for PTSD, depression and alcohol are now present and consistent. The alcohol section is closed because it has been completed in the past six months.

![](pxrm-2-5-oef-oif-setup-guide/009.png)

4.  Note that questions 4B and 4D are “closed” – they have been completed in the past six months. The refusal option is available for this section.

> Entering a refusal option for any one of the sections will satisfy that section for one month. However, it will not cause that section of the dialog to be “closed” – the section will remain open but the reminder would no longer be due if all four refusal options are chosen.

![](pxrm-2-5-oef-oif-setup-guide/010.png)

5.  The hyperlinks have been moved to the bottom of the dialog display.

![](pxrm-2-5-oef-oif-setup-guide/011.png)

6.  If a user would like to re-enter data on a closed section, they would click on the checkbox for that section – PTSD in this example

![](pxrm-2-5-oef-oif-setup-guide/012.png)

> After choosing the closed PTSD section, it opens to allow completion.

![](pxrm-2-5-oef-oif-setup-guide/013.png)

> This is what the dialog would look like if a user did PTSD screening, Alcohol screening and depression screening and then clicked on FINISH – and THEN opened the OEF/OIF reminder dialog

> – those sections would be closed.

![](pxrm-2-5-oef-oif-setup-guide/014.png)

> Clicking on clinical maintenance shows which sections are needed. The display here is based on the completion of each section AFTER the service separation date. If the dates of all seven pieces listed above 1-3, 4A-D are later than the last service separation date, then the reminder is resolved.

![](pxrm-2-5-oef-oif-setup-guide/015.png)

# Index 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Add Reminders to CPRS Cover Sheet, 24 Editing Dialogs, 18
> Mapping, 11, 15, 16
> Overview, 2
> packed reminders, 6
> POST^PXRMWHP, 6
> Reminder Term Management, 11, 15, 16
> Reminder Test, 17
> terms, 7
> Testing Reminders, 23
> VA FileMan Print from the Reminder Term File, 7
