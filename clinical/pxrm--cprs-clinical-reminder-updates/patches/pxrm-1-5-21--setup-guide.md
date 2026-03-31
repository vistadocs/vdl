---
title: PXRM*1.5*21 Iraq and Afghan Post-Deployment Screen Reminder Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: Iraq and Afghan Post-Deployment Screen Reminder
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 1.5
patch_id: PXRM*1.5*21
group_key: "PXRM:PXRM:1.5"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - blockquote
  - reminder
  - strong
  - class
  - dialog
  - iraq
  - health
  - style
  - width
  - table
page_count: 0
word_count: 5941
section_count: 3
table_count: 1
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: January 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_1_5_21_setup.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_1_5_21_setup.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/001.png)

# Iraq & Afghan Post-Deployment Screen Reminder


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Iraq & Afghan Post-Deployment Screen Reminder](#iraq-afghan-post-deployment-screen-reminder)
    - [PXRM\1.5\21](#pxrm1521)
    - [January 2004 Updated: 12/04](#january-2004-updated-1204)
  - [Introduction](#introduction)
  - [Setup and Maintenance](#setup-and-maintenance)
    - [Q & A – Helpful Hints](#q-a-helpful-hints)
- [<u>Appendices</u>](#uappendicesu)

### PXRM\*1.5\*21

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> SETUP GUIDE

### January 2004 Updated: 12/04

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs
> V*IST*A HSD&D
2.  Iraq & Afghan Post-Deployment Screen Reminder Setup Guide 12/16/2004
> <u>Contents</u>
1.  [Verify correct installation of the reminders definition, terms, and dialog. 7](#_bookmark4)
2.  [Map local findings to the national Reminder Terms. 9](#_bookmark5)
3.  [Run the Reminder Test option after term definition mapping is completed. 13](#3.__Run_the_Reminder_Test_option_after_t)
4.  [Use the Reminder Dialog options to edit the national (exported) dialog. 13](#3.__Run_the_Reminder_Test_option_after_t)
5.  [Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude health factors from the electronic encounter forms. 16](#_bookmark7)
6.  [Verify that the reminder functions properly. 17](#_bookmark8)
7.  [Add the nationally distributed reminders to the CPRS Cover Sheet 18](#_bookmark9)
8.  [Verify that the dialog functions properly 19](#verify-that-the-dialog-functions-properly)
3.  Iraq & Afghan Post-Deployment Screen Reminders Setup Guide 12/16/2004

## Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Purpose of Project

> Distribute a new Clinical Reminder, *Iraq & Afghan Post-Deployment Screen,* which identifies veterans of Operation Enduring Freedom in Afghanistan and Operation Iraqi Freedom*,* and tracks and documents when care has been delivered.

#### Background

> Shortly after September 11, 2001, military personnel began deploying to Southwest Asia to liberate Afghanistan. In late 2002, additional military personnel were deployed to this region to liberate Iraq. Operation Enduring Freedom in Afghanistan and Operation Iraqi Freedom produced a new generation of war veterans, who are at increased risk of both medical and psychological illnesses due to complex deployment-related exposures. It is therefore important to screen these war veterans for unique health risks.

> Because VA is in the forefront of electronic medical record keeping, computer-driven “clinical reminders” are an ideal approach to provide targeted health care to the veterans of recent conflicts in Southwest Asia. Clinical reminders are clinical decision support tools that assist healthcare providers in complying with recommended care. VA’s Computerized Patient Record System (CPRS) supports automated clinical reminders that assist clinical decision-making and instruct providers about appropriate care by providing links to educational materials. Electronic clinical reminders additionally improve documentation and follow-up by allowing providers to easily view when certain tests or evaluations were performed, as well as track and document when care has been delivered.

> There are a number of benefits to creating nationally mandated clinical reminders. National reminders help standardize health care and ensure that experts have had input into how clinical care is delivered. Furthermore, national reminders facilitate system-wide assessment of performance and quality of care, because of reporting mechanisms built into the CPRS clinical reminder system.

> A newly developed national clinical reminder – *Iraq & Afghan Post-Deployment Screen* – is designed to aid VA health care providers who are evaluating veterans of the recent conflicts in Southwest Asia. This clinical reminder will help to provide new combat veterans with ongoing, high quality health care in an environment structured to their unique needs and status. Although Iraqi Freedom veterans are eligible for the Gulf War Registry, clinical registries only assess veterans on the one occasion when they volunteer for a special examination. A much better approach is to assure that all members of a unique group of veterans receive specialized care from the time they first present to a VA health care facility.

#### Guidance

1.  Identifying Veterans for the Afghanistan and Iraq Clinical Reminder

> Reminders are designed to apply to a given population and appear on a patient’s CPRS screen, based on patient criteria found in a definable data field within CPRS VistA. Once the Afghanistan and Iraq clinical reminder software patch is installed and the reminder is activated at a local facility, it will appear on the CPRS cover sheet for veterans presenting to a VA health care facility who served in the U.S. military after September 11, 2001.

> Identified veterans will then be asked specifically whether they served on the ground, nearby coastal waters, or in the air over Afghanistan and/or Iraq after September 11, 2001, when these deployments began. If the veteran answers yes, the rest of the reminder dialog will appear on the computer screen for completion by the health care provider.

2.  Preventing duplication

> Because of increasingly widespread use of electronic clinical reminders across VA, there is concern that continued implementation of new reminders will cause undue burden to health care providers. To prevent duplication and unnecessary work, a health factor will be available that allows this Afghanistan and Iraq clinical reminder to be completed just once in the lifetime of a veteran. Importantly, the *Iraq & Afghan Post-Deployment Screen* will satisfy current clinical reminders for depression, alcohol abuse, and PTSD until the scheduled interval lapses for re-administration of these reminders. Consequently, veterans will not be asked the same questions again soon after the completion of this clinical reminder.

3.  Resolving the *Iraq & Afghan Post-Deployment Screen*
    1.  Once a reminder is generated, it needs to be resolved or it will remain active. Reminders designate specific tasks or evaluations that need to be done or specific information that needs to be provided, and designate what information, evaluation, or test results will turn off the reminder. Consequently, the reminder may trigger the ordering of additional tests. Alternately, information provided as a result of the reminder may be sufficient to resolve it. This is the case for the Iraq and Afghanistan clinical reminder, which only involves specific screening questions. However, positive responses to these questions should direct the health care provider to perform a more extensive clinical evaluation or, in some cases, to order additional diagnostic tests.
    2.  For the Iraq and Afghanistan clinical reminder, all questions in the reminder will have to be answered before it is resolved. The questions in this reminder address long-term medical and psychological health risks among veterans of recent conflicts in Afghanistan and Iraq. Reminders are programmed so that when they are resolved, specific information from the reminder is automatically downloaded into a progress note.

#### Patch 21 (PXRM\*1.5\*21)

> PXRM\*1.5\*21 releases one new NATIONAL reminder, dialog, and computed finding required for the Iraq & Afghan project. They will be placed in the REMINDER EXCHANGE file (#811.8).

> Installation of the patch will employ the Reminder Exchange functionality to automatically install these reminders/dialog and their components.

> Reminder Exchange will automatically overwrite any identical components. Documentation for related guidelines can be found at:

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Guideline</strong></th>
<th><strong>Address</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA/DOD Guidelines - Office of Quality and Performance</td>
<td><blockquote>
<p><a href="http://www.oqp.med.va.gov/cpg/cpg.htm"><u>http://www.oqp.med.va.gov/cpg/cpg.htm</u></a></p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA/DOD Depression Guideline</td>
<td><blockquote>
<p><a href="http://www.oqp.med.va.gov/cpg/MDD/MDD_Base.htm"><u>http://www.oqp.med.va.gov/cpg/MDD/MDD_Base.htm</u></a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA/DOD Medically Unexplained Symptoms: Pain and Fatigue</td>
<td><blockquote>
<p><a href="http://www.oqp.med.va.gov/cpg/cpgn/mus/mus_base.htm"><u>http://www.oqp.med.va.gov/cpg/cpgn/mus/mus_base.htm</u></a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>Post Deployment Health Evaluation and</p>
<p>Management</p></td>
<td><blockquote>
<p><a href="http://www.oqp.med.va.gov/cpg/PDH/PDH_base.htm"><u>http://www.oqp.med.va.gov/cpg/PDH/PDH_base.htm</u></a></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA/DOD Substance Abuse Guideline</td>
<td><blockquote>
<p><a href="http://www.oqp.med.va.gov/cpg/SUD/SUD_Base.htm"><u>http://www.oqp.med.va.gov/cpg/SUD/SUD_Base.htm</u></a></p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA Environmental Agents Service</td>
<td><blockquote>
<p><a href="http://vaww.va.gov/environagents/"><u>http://vaww.va.gov/environagents/</u></a></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Impact on Sites

> Setup and implementation by local team

> The following steps may be required after the reminders patch PXRM\*1.5\*21 has been installed on the system:

1.  Clinicians and CPRS/Reminder CACs will need to be informed about the new reminder and dialog.
2.  Reminder CACs may need to map certain national Reminder Terms to identify local processing for documenting the Iraq & Afghan Post Deployment screen.

> As with all National Reminders, the Iraq & Afghan Post Deployment screen reminder is built with reminder terms instead of individual health factors or other finding types. This allows a site to continue to use findings that already exist on the host system as data elements and to relate these local findings to the national terms. The individual health factors that match the reminder term are also distributed with the patch, so that a site that does not have a local finding can use the nationally distributed health factors to collect data.

3.  Edit the reminder dialog, if necessary.

> After you have mapped the local findings to the national terms, you can continue to use

> your local findings as the data elements that are captured *or* use the national findings that are already mapped to the national terms.

> To use your local findings, edit the reminder dialog by first identifying the elements that allow that data element to be collected, and then changing the finding item for that element to the local finding. Directions are provided later in this manual.

> NOTE: The only way national reminders and dialogs can be modified is by changing the finding items in the nationally distributed elements to use your local finding items instead of the nationally distributed ones. You can also copy and rename the national reminder and dialog, as long as terms are correctly mapped to the national ones.

#### NOTE: It isn’t necessary to autogenerate a dialog for this reminder, as the dialog is included in the packed reminder. You only need to activate/link the dialog.

#### Potential Issues

- On initial intake, these patients will have this reminder and any local reminders for Depression, Alcohol, and PTSD screening also due and displayed.
  - Duplication potential.
- AUDIT-C cannot be made mandatory.
  - If a patient refuses to take the AUDIT C, the reminder will remain due.
- Template field text is deleted by the software if additional reminders are processed after the one with the template field. This is a known bug in the software, which we hope will be fixed soon.
  - In the meantime, clinicians should be instructed to click the Finish Button only and not click on Next or Back. Clicking the Next or Back button is where the text in the progress note gets lost. Do not edit the dialog to remove the template fields unless this becomes a major problem.

#### Use of Questionnaire

- Many sites use paper-based questionnaires to collect data from patients.
- This may be more efficient than having the staff sit with the patient and read questions to the patient.
- A sample is posted on the Clinical Reminders web page.
- Data entry issues – data may be entered before the patient sees the provider, and the provider may not be aware of positive responses.

## Setup and Maintenance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After installing the Iraq & Afghan Post Deployment screen reminder, follow the steps beginning on the next page to implement the reminder and dialog for this project.

#### Reminder Summary

> COHORT: Veterans with separation date after 9/11/01. This finding is part of the reminder term: IRAQ/AFGHAN PERIOD OF SERVICE and is determined by a computed finding.

> RESOLUTION: Entry of a health factor for NO IRAQ/AFGHAN SERVICE, which is found in the reminder term IRAQ/AFGHAN SERVICE NO, will resolve the reminder. If the veteran served in Iraq or Afghanistan (IRAQ/AFGHAN SERVICE), then all the other items are required to resolve the reminder:

1)  Screen for PTSD,
2)  Screen for depression,
3)  Screen for alcohol use,
4)  All 4 screening questions related to infectious diseases and other symptoms.

> An entry of IRAQ/AFGHAN SERVICE on the reminder dialog then requires all of the screening questions to be answered.

> All of the individual elements of the screening tool are exported with attached health factors and reminder terms. The national health factors and reminder terms for the 2-question depression screen are used for the depression screening.

> The reminder dialog for alcohol screening allows the use of the standard AUDIT-C tool from the Mental Health package or entry of a refusal or entry of a health factor for no alcohol in the past year. The reminder term for ALCOHOL USE SCREEN contains the AUDIT-C and CAGE from the Mental Health package, the health factor for no alcohol use in the past year, and the health factor for refusal.

> Additional health factors are included for PTSD screening and for the Infectious Diseases/Chronic symptoms screening. If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder term (PTSD SCREEN) that is exported with this reminder.

> The Health Factors for all of these screens should be entered in the site parameters as ones that cannot be added outside of a reminder dialog. Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude these from the electronic encounter forms. Entry of these health factors should ONLY occur during reminder dialog use.

> <span id="_bookmark4" class="anchor"></span>Setup Steps

#### Verify correct installation of the reminders definition, terms, and dialog.

1.  Using *Inquire about Reminder Definition* on the Reminder Management Menu, ensures that the Iraq & Afghan Post Deployment Screen reminder definition has been installed. Review the reminder. (Reviewing the reminder definition will help you understand how it uses reminder terms.) *Do not make any changes to these reminders.* If necessary for local usage, you may copy the national reminder and create a local reminder; then make any desired changes to the local copy.
2.  Using the Term Inquiry option on the Term Management Menu, verify that the following terms are on your system:
    - ALCOHOL USE SCREEN
    - DEPRESSION SCREEN NEGATIVE
    - DEPRESSION SCREEN POSITIVE
    - GI SYMPTOMS (IRAQ/AFGHANISTAN)
    - IRAQ/AFGHAN PERIOD OF SERVICE
    - IRAQ/AFGHAN SERVICE
    - IRAQ/AFGHAN SERVICE NO
    - OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
    - PERSISTENT RASH (IRAQ/AFGHANISTAN)
    - PTSD SCREEN
    - UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

#### VA FileMan Print from the Reminder Term File

> You can also run a VA FileMan Print from the Reminder Term File (#811.5) that sorts by name, and then prints name, finding, and condition. This is a useful list, especially when needing to map many tests and you're not sure what values have been defined.

#### Example

3.  Verify that the reminder dialog is installed on your system. Use CV, Change View, to see dialogs.

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Select Reminder Dialog Management Option: <strong>DI</strong> Reminder Dialogs</p>
<p><strong>Dialog List</strong> Dec 04, 2003@09:51:20 Page: 12 of 13 REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<p>Item Reminder Name Linked Dialog Name &amp; Dialog Status</p>
<p>14 BLOOD PRESSURE CHECK COPY OF BLOOD PRESSURE CHEC Disabled</p>
<p>16 CFTEST CFTEST Disabled</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p><strong>&gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AR All reminders LR Linked Reminders CV Change View RN Name/Print Name Select Item: Next Screen// <strong>CV</strong></p>
<p><strong>Search for: Iraq</strong></p>
<p>...searching for 'Iraq'.</p>
</blockquote></td>
<td><blockquote>
<p>QU</p>
</blockquote></td>
<td><blockquote>
<p>Quit</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark5" class="anchor"></span><strong>Dialog List</strong> Dec 04, 2003@09:51:20 Page: 12 of 13 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)</p>
<p>+Item Reminder Dialog Name Source Reminder Status</p>
</blockquote>
<ol start="179" type="1">
<li><p>VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT S VA-IRAQ &amp; AFGHAN POST-DEP Linked</p></li>
<li><p>VA-MST SCREENING *NONE* Linked</p></li>
<li><p>VA-PNEUMOVAX VA-PNEUMOVAX Linked</p></li>
<li><p>VA-PPD VA-PPD Disabled</p></li>
<li><p>VA-PSA VA-PSA Disabled</p></li>
<li><p>VA-SEATBELT EDUCATION VA-SEATBELT EDUCATION Disabled</p></li>
<li><p>VA-WH MAMMOGRAM REVIEW RESULTS VA-WH MAMMOGRAM REVIEW RE Linked</p></li>
<li><p>VA-WH MAMMOGRAM SCREENING VA-WH MAMMOGRAM SCREENING Linked</p></li>
<li><p>VA-WH PAP SMEAR REVIEW RESULTS VA-WH PAP SMEAR REVIEW RE Linked</p></li>
<li><p>VA-WH PAP SMEAR SCREENING VA-WH PAP SMEAR SCREENING Linked</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Find Next 'Iraq'? Yes// n NO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> NOTE: Do not autogenerate dialogs for the reminder. A Dialog is included with the packed reminder installation.

#### Map local findings to the national Reminder Terms.

> *Option: Reminder Term Management* on the *Reminder Management Menu.*

> Before using the reminder, map the local findings your site uses to represent the national reminder terms, if necessary.

- Prepare a list of your local findings – health factors, taxonomies, etc. that you use to represent terms.
- Review the national term definitions (see Appendix C or use the options on the Reminder Term Management menu), to compare these to what you are using locally to represent terms.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Purpose of National Terms</strong></p>
</blockquote>
<ul>
<li><p>Terms are used to define a general concept that can be used on a national level</p></li>
<li><p>Terms allow sites the ability to link existing local or VISN findings to the national term.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Term Mapping

> These are the only terms that are included in the reminders and all of the exported health factors and education topics fall into one of these terms.

- ALCOHOL USE SCREEN
- DEPRESSION SCREEN NEGATIVE
- DEPRESSION SCREEN POSITIVE
- GI SYMPTOMS (IRAQ/AFGHANISTAN)
- IRAQ/AFGHAN PERIOD OF SERVICE
- IRAQ/AFGHAN SERVICE
- IRAQ/AFGHAN SERVICE NO
- OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
- PERSISTENT RASH (IRAQ/AFGHANISTAN)
- PTSD SCREEN
- UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

> If desired, add local Health Factors or education topics representing these terms.

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Mapping</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ALCOHOL USE SCREEN</td>
<td><p>Add: Any local health factors for AUDT-C, refusal of alcohol screening, or no alcohol in the past year.</p>
<p>The Mental Health tests for AUDIT-C and CAGE are already included in this term. If your site uses the 10 question AUDIT, then this should also be added to this term.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DEPRESSION SCREEN NEGATIVE</p>
</blockquote></td>
<td><p>Should already be mapped based on the national MH reminders. The national health factor is included in this term as well as all of the appropriate Mental Health tests. Any local health factors for negative depression screening should have already been mapped to this term when the national MH reminders were installed.</p>
<p>Do not include any health factors that represent non-specific results of depression screening. For example, a health factor of ‘Depression Screen Done’ is NOT appropriate to add to this term.</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DEPRESSION SCREEN POSITIVE</p>
</blockquote></td>
<td><p>Should already be mapped based on the national MH reminders. The national health factor is included in this term as well as all of the appropriate Mental Health tests. Any local health factors for positive depression screening should have already been mapped to this term when the national MH reminders were installed.</p>
<p>Do not include any health factors that represent non-specific results of depression screening. For example, a health factor of ‘Depression Screen Done’ is NOT appropriate to add to this term.</p></td>
</tr>
<tr class="even">
<td>GI SYMPTOMS (IRAQ/AFGHANISTAN)</td>
<td><p>This term represents the information collected from the reminder dialog that the question related to GI symptoms has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this</p>
<p>term.</p></td>
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
<th><strong>Term</strong></th>
<th><strong>Mapping</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>IRAQ/AFGHAN PERIOD OF SERVICE</p>
</blockquote></td>
<td>This term contains a computed finding that determines if the patient’s most recent service separation date was after 9/11/01. The computed finding is included to define the cohort of patients who need to be asked about service in the combat arena.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>IRAQ/AFGHAN SERVICE</p>
</blockquote></td>
<td><p>This term contains the health factor that is entered from the dialog if the patient did, in fact, serve in the combat arena (on the ground, in the air or at</p>
<p>sea).</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IRAQ/AFGHAN SERVICE NO</p>
</blockquote></td>
<td><p>This term contains the health factor that is entered from the dialog if the patient did not serve in the combat arena (on the ground, in the air or at sea).</p>
<p>This health factor resolves the reminder.</p></td>
</tr>
<tr class="even">
<td>OTHER SYMPTOMS (IRAQ/AFGHANISTAN)</td>
<td><p>This term represents the information collected from the reminder dialog that the question related to fatigue, headaches, etc. has been answered.</p>
<p>Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.</p></td>
</tr>
<tr class="odd">
<td>PERSISTENT RASH (IRAQ/AFGHANISTAN)</td>
<td><p>This term represents the information collected from the reminder dialog that the question related to persistent rashes or skin ulcers has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or</p>
<p>items should be added to this term.</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PTSD SCREEN</p>
</blockquote></td>
<td><p>If your site does PTSD screening, map any local health factors or exams that represent positive or</p>
<p>negative screens for PTSD</p></td>
</tr>
<tr class="odd">
<td>UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)</td>
<td><p>This term represents the information collected from the reminder dialog that the question related to unexplained fever has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional</p>
<p>health factors or items should be added to this term.</p></td>
</tr>
</tbody>
</table>

> NOTE: It isn’t necessary to enter an Effective Period when mapping terms, as this is already in the reminder definition. Entry of an Effective Period on a Reminder Term will override the Effective Period defined on the Reminder Definition.

#### Example: Mapping a Local Health Factor Finding to the National Reminder Term

1.  <span id="3.__Run_the_Reminder_Test_option_after_t" class="anchor"></span>Run the Reminder Test option after term definition mapping is completed. Review the results of patient data with each of the findings mapped to the term. *Option: Reminders Test* on the *Reminder Managers Menu*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Reminder Managers Menu Option: <strong>RT</strong> Reminder Test</p>
<p>Select Patient: <strong>CRPATIENT,ONE</strong> 4-30-44 666680999 YES EMPLOYEE</p>
<blockquote>
<p>Enrollment Priority: GROUP 5 Category: IN PROCESS End Date:</p>
</blockquote>
<p>Select Reminder: <strong>Iraq &amp; Afghan Post Deployment Screen</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> NOTE: See the Clinical Reminders Manager Manual for descriptions of the different elements of the test output.

#### Use the Reminder Dialog options to edit the national (exported) dialog.

> Once you have mapped the local findings to the national terms, you can then decide if you want to continue to use your local findings as the data elements that are captured, or if you want to use the national findings that are already mapped to the national terms.

> If you want to continue to use your local findings, then be sure to edit the reminder dialog by identifying the element that allows for that data element to be collected. Change the finding item for that element to the local finding. The national reminders and dialogs can *only* be changed by changing the finding item in the nationally distributed elements to use your local finding item instead of the nationally distributed one.

#### Steps to add or edit dialog elements:

1.  Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Reminder Managers Menu Option: <strong>DM</strong> Reminder Dialog Management</p>
<p>DP Dialog Parameters ... DI Reminder Dialogs</p>
<p>Select Reminder Dialog Management Option: <strong>DI</strong> Reminder Dialogs</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 59%" />
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p><strong>Dialog List Nov 20, 2003@08:40:01 Page:</strong></p>
<blockquote>
<p>REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<p>Item Reminder Name Linked Dialog Name &amp; Dialog</p>
</blockquote>
<ol type="1">
<li><p>757 NUR ALCOHOL USE SCREEN 757 ALCOHOL USE SCREEN</p></li>
<li><p>757 NUR SEATBELT &amp; ACCIDENT AVOID 757 SEATBELT AND ACCIDENT A</p></li>
<li><p>A A BLOOD EXPOSURE</p></li>
<li><p>A A PAIN VITAL SIGN VA-PAIN SCREEN AND HX</p></li>
</ol></th>
<th><blockquote>
<p><strong>1 of</strong></p>
</blockquote>
<p>Status</p></th>
<th><blockquote>
<p><strong>21</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>+ Enter ?? for more actions</strong></td>
<td></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>&gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>AR All reminders LR Linked Reminders CV Change View RN Name/Print Name</p>
<p>Select Item: Next Screen//</p></td>
<td><blockquote>
<p>QU</p>
</blockquote></td>
<td><blockquote>
<p>Quit</p>
</blockquote></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

1.  Change the view (CV) to Reminder Dialogs.

<table>
<colgroup>
<col style="width: 58%" />
<col style="width: 7%" />
<col style="width: 16%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4">Select Item: Next Screen// cv</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Select one of the following:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>D Reminder Dialogs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>E Dialog Elements</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>F Forced Values</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>G Dialog Groups</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>P Additional Prompts</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>R Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>RG Result Group (Mental Health)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>RE Result Element (Mental Health)</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4">TYPE OF VIEW: R// d Reminder Dialogs</td>
</tr>
<tr class="odd">
<td colspan="4"><strong>Dialog List</strong> Dec 04, 2003@09:51:20 Page: 12 of 13</td>
</tr>
<tr class="even">
<td colspan="4">DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Item Reminder Dialog Name Source Reminder Status</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>1 571B SMOKING CESSATION EDUCATI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>2 571a SMOKING CESSATION EDUCATI</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>3 757 ALCOHOL USE SCREEN 757 NUR ALCOHOL USE SCREE Linked</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>4 757 SEATBELT AND ACCIDENT AVOIDANCE 757 NUR SEATBELT &amp; ACCIDE Linked</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>5 A A PAIN SCREEN AND INTERVENTION *NONE*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>6 A A SG PAIN HISTORY DIA ZZPJH REMINDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>+ Enter ?? for more actions</strong></td>
<td></td>
<td></td>
<td><blockquote>
<p><strong>&gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>AD Add Reminder Dialog PT List/Print All CV Change View RN Name/Print Name <strong>Select Item: Next Screen// SL</strong></p>
<p>Search for: <strong>Iraq</strong></p>
<p>...searching for ‘Iraq’.</p></td>
<td><blockquote>
<p>QU</p>
</blockquote></td>
<td><blockquote>
<p>Quit</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

2.  Enter SL for Search List, to jump to the Iraq dialog. Select the dialog number to see details.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog List</strong> Dec 04, 2003@09:51:20 Page: 12 of 13 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)</p>
<p>+Item Reminder Dialog Name Source Reminder Status</p>
</blockquote>
<ol start="179" type="1">
<li><p>VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT S VA-IRAQ &amp; AFGHAN POST-DEP Linked</p></li>
<li><p>VA-MST SCREENING *NONE* Linked</p></li>
<li><p>VA-PNEUMOVAX VA-PNEUMOVAX Linked</p></li>
<li><p>VA-PPD VA-PPD Disabled</p></li>
<li><p>VA-PSA VA-PSA Disabled</p></li>
<li><p>VA-SEATBELT EDUCATION VA-SEATBELT EDUCATION Disabled</p></li>
<li><p>VA-WH MAMMOGRAM REVIEW RESULTS VA-WH MAMMOGRAM REVIEW RE Linked</p></li>
<li><p>VA-WH MAMMOGRAM SCREENING VA-WH MAMMOGRAM SCREENING Linked</p></li>
<li><p>VA-WH PAP SMEAR REVIEW RESULTS VA-WH PAP SMEAR REVIEW RE Linked</p></li>
<li><p>VA-WH PAP SMEAR SCREENING VA-WH PAP SMEAR SCREENING Linked</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Find Next 'Iraq'? Yes// <strong>n</strong> NO Select Item: Next Screen<strong>// 179</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog Edit List</strong> Dec 16, 2003@10:01:04 Page: 1 of 5</p>
<p>REMINDER DIALOG NAME: VA-IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN [NATIONAL] *L</p>
<p>Item Seq. Dialog Details/Findings Type</p>
</blockquote>
<ol type="1">
<li><p>5 TEXT OIF INTRO AND WEB element Finding: *NONE*</p></li>
<li><p>20 GP OIF COMBAT SERVICE YES/NO group Finding: *NONE*</p></li>
<li><blockquote>
<p>20.5 GP OIF COMBAT SERVICE NO group Finding: NO IRAQ/AFGHAN SERVICE (HEALTH FACTOR)</p>
</blockquote></li>
<li><blockquote>
<p>20.10 GP OIF COMBAT SERVICE YES group Finding: IRAQ/AFGHAN SERVICE (HEALTH FACTOR)</p>
</blockquote></li>
<li><blockquote>
<p>20.10.25 GP OIF PTSD group</p>
</blockquote></li>
</ol>
<blockquote>
<p>Finding: *NONE*</p>
</blockquote>
<ol start="6" type="1">
<li><blockquote>
<p>20.10.25.15 GP OIF PTSD QUESTIONS group Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>20.10.25.15.5 TEXT OIF PTSD QUESTIONS element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>20.10.25.15.10 GP OIF PTSD SCREEN RESULTS group</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CO Copy Dialog DT Dialog Text RI Reminder Inquiry DD Detailed Display ED Edit/Delete Dialog QU Quit</p>
<p>DP Progress Note Text INQ Inquiry/Print Select Sequence: Next Screen// <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Make edits, as needed, by entering the dialog element number.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 32%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p><strong>Dialog Edit List</strong> Dec 16, 2003@10:01:04 Page: REMINDER DIALOG NAME: IRAQ &amp; AFGHANISTAN POST DEPLOYMENT SCREEN</p>
<p>+Item Seq. Dialog Summary</p>
</blockquote>
<ol start="9" type="1">
<li><p>20.10.25.15.10.5 Element: VA-HF OIF PTSD NEGATIVE</p></li>
<li><p>20.10.25.15.10.10 Element: VA-HF OIF PTSD POSITIVE</p></li>
<li><p>20.10.35 Group: VA-GP OIF DEPRESSION SCREEN</p></li>
<li><p>20.10.35.10 Group: VA-GP DEP SCREEN PRIME MD</p></li>
<li><p>20.10.35.10.5 Element: VA-HF DEP 2 QUESTION NEG</p></li>
<li><p>20.10.35.10.10 Element: VA-HF DEP 2 QUESTION POS</p></li>
<li><p>20.10.45 Group: VA-GP OIF ALCOHOL SCREEN</p></li>
</ol></th>
<th><blockquote>
<p>2</p>
</blockquote></th>
<th>of</th>
<th><blockquote>
<p>5</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>+ Next Screen</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>- Prev Screen</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>?? More Actions</strong></p>
</blockquote></td>
<td colspan="3"><blockquote>
<p><strong>&gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>CO Copy Dialog DO Dialog Overview QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>DD Detailed Display DT Dialog Text</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>DP Progress Note Text ED Edit/Delete Dialog</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>Select Item: Next Screen// <strong>9</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>Select one of the following:</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>E Edit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>C Copy and Replace current element</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>D Delete element from this dialog</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>Select Dialog Element Action: E// <strong>&lt;Enter&gt;</strong> dit</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>Dialog Element Type: E//<strong>&lt;Enter&gt;</strong> lement</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>Current dialog element/group name: VA-HF OIF PTSD NEGATIVE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>Used by: VA-GP OIF PTSD SCREEN RESULTS (Dialog Group)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark7" class="anchor"></span>FINDING ITEM: PTSD SCREEN NEGATIVE// ZZPTSD</p>
<p>Searching for a EDUCATION TOPICS Searching for a IMMUNIZATION Searching for a SKIN TEST Searching for a EXAM</p>
<p>Searching for a HEALTH FACTOR ZZPTSD SCREEN NEGATIVE</p>
<p>...OK? Yes// &lt;Enter&gt; (Yes) Select ADDITIONAL FINDINGS:</p>
<p>Input your edit comments.</p>
<p>Edit? NO// &lt;Enter&gt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude health factors from the electronic encounter forms.

> Enter the Health Factors for all of the screens in the site parameters as ones that cannot be added outside of a reminder dialog. Entry of these health factors should ONLY occur during reminder dialog use.

- ALCOHOL USE SCREEN
- DEPRESSION SCREEN NEGATIVE
- DEPRESSION SCREEN POSITIVE
- GI SYMPTOMS (IRAQ/AFGHANISTAN)
- IRAQ/AFGHAN PERIOD OF SERVICE
- IRAQ/AFGHAN SERVICE
- IRAQ/AFGHAN SERVICE NO
- OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
- PERSISTENT RASH (IRAQ/AFGHANISTAN)
- PTSD SCREEN
- UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

> This parameter is on the general parameter tool menu (XPAR), available on the CPRS Configuration (IRM) option.

> NOTE: Since this is a Kernel option, some sites assign the menu separately from CPRS, or it may only be available to IRM staff. If you don’t have access to it, check with your IRM office.

#### Verify that the reminder functions properly.

1.  Run a Reminders Due Report to determine if the Iraq Clinical Reminder statuses reported are correct.

> *Option: Reminders Due* on the *Reminder Reports menu*

> This report can be displayed at the beginning of the day for patients being seen that day.

- The reminder can be used in a reminder report to evaluate clinics or stop codes on their adherence/compliance with that reminder.
- Reports can be run to list individual patient names for chart review on reasons that the guideline was not or could not be achieved.
- Clinics, stop codes, or divisions can be identified by summary reports using these reminders where there are differences in compliance or poor adherence to the guideline.
2.  Use the Reminder Test option to test the reminders.

> *Option: Reminders Test* on the *Reminder Management menu*

3.  <span id="_bookmark9" class="anchor"></span>Use the clinical maintenance view in the CPRS GUI to ensure that the status of the reminder is appropriate.

#### Add the nationally distributed reminders to the CPRS Cover Sheet

4.  Open a patient chart, click on the reminders clock, and when the available Reminders window opens, click on Action, and then select “Edit Cover Sheet Reminder List.”
5.  ![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/002.png)When the Cover Sheet Reminder List opens, set the Cover sheet parameter level.
6.  Locate the Iraq & Afghan Post Deployment Screen reminder and click the Add button (or double-click the reminder).

> ![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/003.png)

#### Verify that the dialog functions properly

> Test the Iraq & Afghan Post Deployment Screen Reminder dialog in CPRS, using either the exported dialog or your locally created dialog. Using point-and-click reminder resolution processing through CPRS GUI, verify the following:

- Correct Progress Note text is posted
- Finding Item gets sent to PCE
- Reminder is satisfied

> Check the Clinical Maintenance component display in CPRS after testing dialogs to ensure that all the activities are tested are reflected in the clinical maintenance display.

> *Steps to test dialogs:*

1.  On the cover sheet, click on the Reminders icon.
2.  Click on reminders in the Reminders box to see details of a reminder
3.  Open the Notes tab and select New Note. Enter a title.
4.  Open the Reminders drawer and review the contents.
5.  Locate the Iraq & Afghan Post Deployment Screen reminder dialog and open it.
6.  Check all the boxes, in different combinations, to see what happens.

> ![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/004.png)

7.  Perform as many of the following as possible:
- Click on the boxes for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms.
- Enter a positive depression screen.
- Enter a positive alcohol screen.
- Perform the AUDC, checking appropriate boxes.
- Click Finish.
- Verify that all elements are required.
- Click on the Refresh button in the Action menu.
- Verify that entry of the alcohol screen and the depression screen in the Iraq/Afghan reminder dialog also resolves any local reminders for depression screening and alcohol screening.
- Verify that any local reminders for f/u of positive screens for depression or alcohol became due.
- If the national depression screening reminder was not applicable for the patient above, select a new patient who has a status of Due or Applicable for depression screening.
- Open the dialog IRAQ & AFGHANISTAN POST DEPLOYMENT SCREEN.
- Check the appropriate boxes for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms.
- Enter a positive depression screen.
- Click Finish.
- Verify that the national depression screening reminder is resolved.
- If the national alcohol screening reminder was not applicable for the patient above, select a new patient who has a status of Due or Applicable for alcohol screening.
- Open the dialog IRAQ & AFGHANISTAN POST DEPLOYMENT SCREEN.
- Check the appropriate boxes for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms.
- Enter a positive alcohol screen.
- Click Finish.
- Verify that the national alcohol screening reminder is resolved.
- Repeat any of the steps above to try different dialog entries and to observe the results in the progress note text and reminder statuses.
- Select a new patient with a separation date before 9/11/01.
- Check the Cover Sheet and Clinical Maintenance box to verify that the reminder is not due or applicable.

#### NOTE: Remember to “refresh” the screen after completing a dialog, if you want to see the updated status immediately.

### Q & A – Helpful Hints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Q: What is a National Reminder?

> A: National reminders are clinical reminders and reminder dialogs that have gone through an approval process for national distribution. Some national reminders are related to statutory, regulatory, or Central Office mandates such as Hepatitis C, MST, or Pain. Other national reminders are being developed under the guidance of the VA National Clinical Practice Guideline Council (NCPGC).

> Guideline-related reminders are being developed for two reasons:

1.  To provide reminders for sites that don’t have reminders in place for a specific guideline (e.g., HTN, HIV).
2.  To provide a basic set of reminders to all sites to improve clinical care, and also allow roll-up data for measurement of guideline implementation and adherence (e.g., IHD, Mental Health).

#### Q: Can national reminders or dialogs ever be locally modified?

> A: The only way national reminders and dialogs can be modified is by changing the finding item in the nationally distributed dialog elements to use your local finding item instead of the nationally distributed one. You can copy the national reminder to create a local reminder, but you should map your health factors, education topics, and other findings to the national exported terms.

#### Q: Is the Iraq & Afghan Post Deployment Screen national reminder mandated for use? A: No.

> Q: What should we do if we already have Depression Screening, Alcohol Screening, or PTSD reminders?

> A: If you choose to continue using your local reminder and dialog, you need to make sure that your local reminder is consistent with the VA/DOD National Clinical Practice Guideline. You should map your local findings to the national reminder terms in case you want to use the National reminders in the future for display in CPRS or for reporting.

> There are currently no plans to use these reminders to roll up data to any national reports on Iraq.

> Q: This patch contains template fields in the PTSD screen—if providers using this reminder click next or back, they lose the text in the progress note. What do you suggest...should we edit the dialog to remove the template fields?

> A: This is a long-standing problem with reminders; it is on our list to fix after the release of CRv2.0. In the meantime, clinicians should be instructed to click the Finish Button only and not click on Next or Back. Clicking the Next or Back button is where the text in the progress

> note gets lost. Do not edit the dialog to remove the template fields unless this becomes a major problem.

#### Q: How can we check parameters to see if anyone sees the reminders?

> A: The simplest way to view whether an individual is seeing the reminders is to open the reminder cover sheet editor by clicking on the reminder clock in CPRS, picking Action, and then choosing “Edit Cover Sheet Reminders.” A button on the dialog allows you to view the entire list of reminders that are seen by an individual user.

# <u>Appendices</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Appendix A: Iraq & Afghan Post Deployment Reminder Definition Appendix B: Iraq & Afghan Post Deployment Reminder Dialog Appendix C: Reminder Term Descriptions

> Appendix D: Reminder Health Factors

#### Appendix A: Reminder Definition

> REMINDER DEFINITION INQUIRY Dec 19, 2003 12:26:28 pm Page 1

> VA-IRAQ & AFGHAN POST-DEPLOY SCREEN No. 568022

> Print Name: Iraq&Afghan Post-Deployment Screen

> Class: NATIONAL

> Sponsor:

> Review Date:

> Usage: CPRS, REPORTS

> Related VA-\* Reminder:

> Reminder Dialog: VA-IRAQ & AFGHANISTAN POST DEPLOYMENT SCREEN

> Priority:

> Reminder Description:

> Patients who served in combat in either Iraq (Operation Iraqi Freedom) or in Afghanistan (Operation Enduring Freedom) should be screened for illnesses related to their service. Screening for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms should be part of the initial evaluation of these Veterans.

> COHORT: veterans with separation date after 9/11/01. This finding is part of the reminder term: IRAQ/AFGHAN PERIOD OF SERVICE and is determined by a computed finding.

> RESOLUTION: entry of a health factor for NO IRAQ/AFGHAN SERVICE which is found in the reminder term IRAQ/AFGHAN SERVICE NO will resolve the reminder. If the veteran served in Iraq or Afghanistan (IRAQ/AFGHAN SERVICE) then all the other items are required to resolve the reminder:

1.  screen for PTSD,
2.  screen for depression,
3.  screen for alcohol use,
4.  all 4 screening questions related to infectious diseases and other symptoms.

> An entry of IRAQ/AFGHAN SERVICE on the reminder dialog then requires all of the screening questions to be answered.

> All of the individual elements of the screening tool are exported with attached health factors and reminder terms. The national health factors and reminder terms for the 2 question depression screen are used for the depression screening. The reminder dialog for alcohol screening allows the use of the standard AUDIT-C tool from the Mental Health package or entry of a refusal or entry of a health factor for no alcohol in the past year. The reminder term for ALCOHOL USE SCREEN contains the AUDIT-C and CAGE from the Mental Health package, the health factor for no alcohol use in the past year and the health factor for refusal. Additional health factors are included for PTSD screening and for the Infectious Diseases/Chronic symptoms screening. If your site does PTSD screening, then you will need to map your local health factors to the national PTSD reminder term (PTSD SCREEN) that is exported with this reminder.

> The HFs for all of these screens should be entered in the site parameters as ones that cannot be added outside of a reminder dialog. Use the parameter ORWPCE EXCLUDE HEALTH FACTORS to exclude these from the electronic encounter forms. Entry of these health factors should ONLY occur during reminder dialog use.

> Technical Description:

> Baseline Frequency:

> Do In Advance Time Frame: Wait until actually DUE Sex Specific:

> Ignore on N/A:

> Frequency for Age Range: 99Y - Once for all ages Match Text:

> No Match Text:

> Findings:

> ---- Begin: IRAQ/AFGHAN SERVICE NO (FI(1)=RT(489)) ----------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Mapped Findings:

> Mapped Finding Item: HF.NO IRAQ/AFGHAN SERVICE

> End: IRAQ/AFGHAN SERVICE NO

> ---- Begin: IRAQ/AFGHAN PERIOD OF SERVICE (FI(2)=RT(490)) ---------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND

> Beginning Date/Time: SEP 11, 2001

> Mapped Findings:

> Mapped Finding Item: CF.VA-IRAQ & AFGHAN SEP. DATE Beginning Date/Time: SEP 11, 2001

> End: IRAQ/AFGHAN PERIOD OF SERVICE

> ---- Begin: IRAQ/AFGHAN SERVICE (FI(3)=RT(568012)) ----------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.IRAQ/AFGHAN SERVICE

> End: IRAQ/AFGHAN SERVICE

> ---- Begin: DEPRESSION SCREEN NEGATIVE (FI(4)=RT(80)) -------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.DEP SCREEN 2 QUESTION NEG

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

> End: DEPRESSION SCREEN NEGATIVE

> ---- Begin: DEPRESSION SCREEN POSITIVE (FI(5)=RT(81)) -------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.DEP SCREEN 2 QUESTION POS

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

> End: DEPRESSION SCREEN POSITIVE

> ---- Begin: ALCOHOL USE SCREEN (FI(6)=RT(488)) --------------------------

> Finding Type: REMINDER TERM

> Not Found Text: Screening for at risk alcohol use using the AUDIT-C screening tool should be performed yearly for any patient who has consumed alcohol in the past year. No record of prior screening for alcohol use was found in this patient's record.

> Mapped Findings:

| Mapped | Finding | Item: | MH.AUDC                                |
|--------|---------|-------|----------------------------------------|
| Mapped | Finding | Item: | MH.CAGE                                |
| Mapped | Finding | Item: | HF.NON-DRINKER (NO ALCOHOL FOR \>1 YR) |
| Mapped | Finding | Item: | HF.REFUSED ALCOHOL USE SCREENING       |
| Mapped | Finding | Item: | MH.AUDIT                               |

> End: ALCOHOL USE SCREEN

> ---- Begin: PTSD SCREEN (FI(7)=RT(568013)) ------------------------------

> Finding Type: REMINDER TERM Not Found Text: Screen for PTSD.

> Mapped Findings:

> Mapped Finding Item: HF.PTSD SCREEN NEGATIVE

> Mapped Finding Item: HF.PTSD SCREEN POSITIVE

> End: PTSD SCREEN

> ---- Begin: UNEXPLAINED FEVER (IRAQ/AFGHANISTAN) (FI(8)=RT(568015)) -----

> Finding Type: REMINDER TERM

> Not Found Text: Screen for unexplained fevers that might

> represent occult malaria or infection with leishmaniasis.

> Mapped Findings:

> Mapped Finding Item: HF.UNEXPLAINED FEVERS SCREEN NEGATIVE

> Mapped Finding Item: HF.UNEXPLAINED FEVERS SCREEN POSITIVE

> ---- End: UNEXPLAINED FEVER (IRAQ/AFGHANISTAN) ---------------------------

> ---- Begin: OTHER SYMPTOMS (IRAQ/AFGHANISTAN) (FI(9)=RT(568017)) --------

> Finding Type: REMINDER TERM

> Not Found Text: Screen for symptoms of fatigue, headaches, muscle or joint pains, or forgetfulness that have lasted 3 months or longer and have interfered with daily activities.

> NEGATIVE

> Mapped Findings:

> Mapped Finding Item: HF.OTHER PHYSICAL SYMPTOMS SCREEN

> Mapped Finding Item: HF.OTHER PHYSICAL SYMPTOMS SCREEN

> POSITIVE

> ---- End: OTHER SYMPTOMS (IRAQ/AFGHANISTAN) ------------------------------

> ---- Begin: GI SYMPTOMS (IRAQ/AFGHANISTAN) (FI(10)=RT(568014)) ----------

> Finding Type: REMINDER TERM

> Not Found Text: Screen for diarrhea or other GI complaints that might suggest giardia, amoebiasis or other GI infection.

> Mapped Findings:

> Mapped Finding Item: HF.GI SYMPTOMS SCREEN NEGATIVE

> Mapped Finding Item: HF.GI SYMPTOMS SCREEN POSITIVE

> End: GI SYMPTOMS (IRAQ/AFGHANISTAN)

> ---- Begin: PERSISTENT RASH (IRAQ/AFGHANISTAN) (FI(11)=RT(568016)) ------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.SKIN LESION SCREEN NEGATIVE Mapped Finding Item: HF.SKIN LESION SCREEN POSITIVE

> ---- End: PERSISTENT RASH (IRAQ/AFGHANISTAN) -----------------------------

> General Patient Cohort Found Text:

> Patients who served in combat in either Iraq (Operation Iraqi Freedom) or in Afghanistan (Operation Enduring Freedom) should be screened for illnesses related to their service. Screening for PTSD, depression, problem alcohol use, infectious diseases, and chronic symptoms should be part of the initial evaluation of these Veterans.

> General Patient Cohort Not Found Text:

> General Resolution Found Text:

> General Resolution Not Found Text:

> Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient: (SEX)&(AGE)&FI(2)

> Expanded Patient Cohort Logic:

> (SEX)&(AGE)&FI(IRAQ/AFGHAN PERIOD OF SERVICE)

> Customized RESOLUTION LOGIC defines findings that resolve the Reminder: FI(1)!((FI(4)!FI(5))&FI(6)&FI(7)&FI(8)&FI(9)&FI(10)&FI(11))

> Expanded Resolution Logic:

> FI(IRAQ/AFGHAN SERVICE NO)!((FI(DEPRESSION SCREEN NEGATIVE)! FI(DEPRESSION SCREEN POSITIVE))&FI(ALCOHOL USE SCREEN)&FI(PTSD SCREEN)& FI(UNEXPLAINED FEVER (IRAQ/AFGHANISTAN))&

> FI(OTHER SYMPTOMS (IRAQ/AFGHANISTAN))&FI(GI SYMPTOMS (IRAQ/AFGHANISTAN))& FI(PERSISTENT RASH (IRAQ/AFGHANISTAN)))

> Web Sites:

> Web Site URL: <http://www.oqp.med.va.gov/cpg/cpg.htm>

> Web Site Title: VA/DOD Guidelines - Office of Quality and Performance

> Web Site URL: <http://www.oqp.med.va.gov/cpg/MDD/MDD_Base.htm>

> Web Site Title: VA/DOD Depression Guideline

> Web Site URL: <http://www.oqp.med.va.gov/cpg/cpgn/mus/mus_base.htm>

> Web Site Title: VA/DOD Medically Unexplained Symptoms: Pain and Fatigue

> Web Site URL: <http://www.oqp.med.va.gov/cpg/PDH/PDH_base.htm>

> Web Site Title: Post Deployment Health Evaluation and Management

#### ![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/005.png)Appendix B: Reminder Dialog Opening Screen

> ![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/006.png)

> ![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/007.png)

> ![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/008.png)

> ![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/009.png)

> ![](pxrm-1-5-21-iraq-and-afghan-post-deployment-screen-reminder-setup-guide/010.png)

> <span id="Appendix_C:_Reminder_Terms" class="anchor"></span>Appendix C: Reminder Terms

- ALCOHOL USE SCREEN
- DEPRESSION SCREEN NEGATIVE
- DEPRESSION SCREEN POSITIVE
- GI SYMPTOMS (IRAQ/AFGHANISTAN)
- IRAQ/AFGHAN PERIOD OF SERVICE
- IRAQ/AFGHAN SERVICE
- IRAQ/AFGHAN SERVICE NO
- OTHER SYMPTOMS (IRAQ/AFGHANISTAN)
- PERSISTENT RASH (IRAQ/AFGHANISTAN)
- PTSD SCREEN
- UNEXPLAINED FEVER (IRAQ/AFGHANISTAN)

> REMINDER TERM INQUIRY Nov 21, 2003 9:59:48 am Page 1

> ALCOHOL USE SCREEN No.133

> Class: LOCAL

> Sponsor:

> Date Created:

> Review Date:

> Description:

> Any local health factors for AUDT-C, refusal of alcohol screening, or no alcohol in the past year.

> The Mental Health tests for AUDIT-C and CAGE are already included in this term. If your site uses the 10 question AUDIT, then this should also be added to this term.

> Findings:

> Finding Item: AUDC (FI(1)=MH(208)) Finding Type: MENTAL HEALTH INSTRUMENT

> Finding Item: CAGE (FI(2)=MH(226)) Finding Type: MENTAL HEALTH INSTRUMENT

> DEPRESSION SCREEN NEGATIVE No.82

> Class: NATIONAL

> Sponsor:

> Date Created:

> Review Date:

> Description:

> Any health factors or MH instrument scores that indicate that depression screening has been done and is negative should be mapped to this reminder term.

> Depression Screen Neg (PRIME-MD, CES-D, DOM80, Ham-D) MH: DOM80=0

> MH: DOMG\<4 MH: CRS\<10 MH: BDI\<10 MH:Zung\<33

> Findings:

> Finding Item: DEP SCREEN 2 QUESTION NEG (FI(1)=HF(105))

> Finding Type: HEALTH FACTOR

> Finding Item: DOM80 (FI(2)=MH(229)) Finding Type: MENTAL HEALTH INSTRUMENT

> Condition: I V=0

> Finding Item: DOMG (FI(3)=MH(232)) Finding Type: MENTAL HEALTH INSTRUMENT

> Condition: I V\<4

> Finding Item: CRS (FI(4)=MH(19)) Finding Type: MENTAL HEALTH INSTRUMENT

> MH Scale: 1 Condition: I V\<10

> Finding Item: BDI (FI(5)=MH(223)) Finding Type: MENTAL HEALTH INSTRUMENT

> MH Scale: 1 Condition: I V\<10

> Finding Item: ZUNG (FI(6)=MH(87)) Finding Type: MENTAL HEALTH INSTRUMENT

> MH Scale: 1 Condition: I V\<33

> DEPRESSION SCREEN POSITIVE No.83

> Class: NATIONAL

> Sponsor:

> Date Created:

> Review Date:

> Description:

> Any health factors or MH instrument scores that indicate that depression screening has been done and is positive should be mapped to this reminder term.

> Depression Screen Pos (PRIME-MD, CES-D, DOM80, Ham-D) MH: DOM80=1

> MH: DOMG\>3 MH: CRS\>9 MH: BDI\>9

> MH:Zung\>32

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 26%" />
<col style="width: 35%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Findings:</th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Finding Item: Finding Type:</p>
</blockquote></td>
<td>DEP SCREEN 2 QUESTION POS HEALTH FACTOR</td>
<td>(FI(1)=HF(106))</td>
</tr>
<tr class="even">
<td></td>
<td>Finding Item: Finding Type: Condition:</td>
<td>DOM80 (FI(2)=MH(229)) MENTAL HEALTH INSTRUMENT I V=1</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Finding Item: Finding Type: Condition:</td>
<td>DOMG (FI(3)=MH(232)) MENTAL HEALTH INSTRUMENT I V&gt;3</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Finding Item: Finding Type:</p>
<p>MH Scale: Condition:</p>
</blockquote></td>
<td><p>CRS (FI(4)=MH(19)) MENTAL HEALTH INSTRUMENT 1</p>
<p>I V&gt;9</p></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Finding Item: Finding Type:</p>
<p>MH Scale: Condition:</p>
</blockquote></td>
<td><p>BDI (FI(5)=MH(223)) MENTAL HEALTH INSTRUMENT 1</p>
<p>I V&gt;9</p></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Finding Item: Finding Type:</p>
<p>MH Scale: Condition:</p>
</blockquote></td>
<td><p>ZUNG (FI(6)=MH(87)) MENTAL HEALTH INSTRUMENT 1</p>
<p>I V&gt;32</p></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>GI SYMPTOMS</strong></td>
<td><strong>(IRAQ/AFGHANISTAN)</strong></td>
<td></td>
<td><strong>No.568014</strong></td>
</tr>
</tbody>
</table>

> Class: NATIONAL

> Sponsor:

> Date Created:

> Review Date:

> Description:

> This term represents the information collected from the reminder dialog that the question related to GI symptoms has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 8%" />
<col style="width: 25%" />
<col style="width: 12%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>Findings:</th>
<th colspan="5"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Finding Finding</p>
</blockquote></td>
<td>Item: Type:</td>
<td>GI SYMPTOMS SCREEN HEALTH FACTOR</td>
<td>NEGATIVE</td>
<td>(FI(1)=HF(127))</td>
</tr>
<tr class="even">
<td></td>
<td>Finding</td>
<td>Item:</td>
<td>GI SYMPTOMS SCREEN</td>
<td>POSITIVE</td>
<td>(FI(2)=HF(126))</td>
</tr>
<tr class="odd">
<td></td>
<td>Finding</td>
<td>Type:</td>
<td>HEALTH FACTOR</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> IRAQ/AFGHAN PERIOD OF SERVICE No.135

> Class: NATIONAL

> Sponsor:

> Date Created:

> Review Date:

> Description:

> This term contains a computed finding that determines if the patient's most recent service separation date was after 9/11/01. The computed finding is included to define the cohort of patients who need to be asked about service in the combat arena.

> Findings:

> Finding Item: VA-IRAQ & AFGHAN SEP. DATE (FI(1)=CF(578006)) Finding Type: REMINDER COMPUTED FINDING

> IRAQ/AFGHAN SERVICE No.568012

> Class: NATIONAL

> Sponsor:

> Date Created:

> Review Date:

> Description:

> This term contains the health factor that is entered from the dialog if the patient did, in fact, serve in the combat arena (on the ground, in the air or at sea).

> Findings:

> Finding Item: IRAQ/AFGHAN SERVICE (FI(1)=HF(125))

> Finding Type: HEALTH FACTOR

> IRAQ/AFGHAN SERVICE NO No.134

> Class: NATIONAL

> Sponsor:

> Date Created:

> Review Date:

> Description: This term contains the health factor that is entered from the dialog if the patient did not serve in the combat arena (on the ground, in the air

> or at sea). This health factor resolves the reminder.

> Findings:

> Finding Item: NO IRAQ/AFGHAN SERVICE (FI(2)=HF(122))

> Finding Type: HEALTH FACTOR

> OTHER SYMPTOMS (IRAQ/AFGHANISTAN) No.568017

> Class: NATIONAL

> Sponsor:

> Date Created:

> Review Date:

> Description:

> This term represents the information collected from the reminder dialog that the question related to fatigue, headaches, etc. has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.

> Findings:

> (FI(1)=HF(131))

> (FI(2)=HF(130))

> Finding Item: OTHER PHYSICAL SYMPTOMS SCREEN NEGATIVE

> Finding Type: HEALTH FACTOR

> Finding Item: OTHER PHYSICAL SYMPTOMS SCREEN POSITIVE

> Finding Type: HEALTH FACTOR

> PERSISTENT RASH (IRAQ/AFGHANISTAN) No.568016

> Class: NATIONAL

> Sponsor:

> Date Created:

> Review Date:

> Description:

> This term represents the information collected from the reminder dialog that the question related to persistent rashes or skin ulcers has been answered. Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 19%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th>Findings:</th>
<th colspan="6"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Finding Finding</p>
</blockquote></td>
<td>Item: Type:</td>
<td>SKIN LESION SCREEN HEALTH FACTOR</td>
<td>NEGATIVE</td>
<td colspan="2">(FI(1)=HF(132))</td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Finding Finding</p>
</blockquote></td>
<td>Item: Type:</td>
<td>SKIN LESION SCREEN HEALTH FACTOR</td>
<td>POSITIVE</td>
<td colspan="2">(FI(2)=HF(124))</td>
</tr>
<tr class="odd">
<td><strong>PTSD SCREEN</strong></td>
<td colspan="2"></td>
<td colspan="3"><strong>No.568013</strong></td>
<td></td>
</tr>
<tr class="even">
<td><p>Class: Sponsor:</p>
<p>Date Created: Review Date:</p></td>
<td colspan="2"><blockquote>
<p>NATIONAL</p>
</blockquote></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="odd">
<td>Description:</td>
<td colspan="2"></td>
<td colspan="3"></td>
<td></td>
</tr>
</tbody>
</table>

> If your site does PTSD screening, map any local health factors or exams that represent positive or negative screens for PTSD

> Findings:

> Finding Item: PTSD SCREEN NEGATIVE (FI(1)=HF(612599))

> Finding Type: HEALTH FACTOR

> Finding Item: PTSD SCREEN POSITIVE (FI(2)=HF(612598))

> Finding Type: HEALTH FACTOR

> UNEXPLAINED FEVER (IRAQ/AFGHANISTAN) No.568015

> Class: NATIONAL

> Sponsor:

> Date Created:

> Review Date:

> Description:

> This term represents the information collected from the reminder dialog that the question related to unexplained fever has been answered.

> Separate health factors representing positive and negative answers to the question are included in this term. Unless a site is already asking the specific question included in this reminder dialog, NO additional health factors or items should be added to this term.

> Findings:

> Finding Item: UNEXPLAINED FEVERS SCREEN NEGATIVE (FI(1)=HF(129))

> Finding Type: HEALTH FACTOR

> Finding Item: UNEXPLAINED FEVERS SCREEN POSITIVE (FI(2)=HF(128))

> Finding Type: HEALTH FACTOR

#### Appendix D: Health Factors

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Health Factor Group</strong></th>
<th><strong>Health Factor</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ALCOHOL USE</td>
<td><p>BINGE DRINKING DRINKING ALONE</p>
<p>DRIVING UNDER THE INFLUENCE FAMILY HX OF ALCOHOL ABUSE HEAVY DRINKER (3 OR MORE/DAY) HISTORY OF AN ALCOHOL PROBLEM LEGAL COMPLICATIONS</p>
<p>MODERATE DRINKER NON-DRINKER</p>
<p>NON-DRINKER (NO ALCOHOL FOR &gt;1 PREV. SCREEN ETOH PROBLEM REFUSED ALCOHOL ABUSE SCREENIN REFUSED ALCOHOL USE SCREENING</p></td>
</tr>
<tr class="even">
<td>IRAQ/AFGHAN</td>
<td><p>GI SYMPTOMS SCREEN NEGATIVE GI SYMPTOMS SCREEN POSITIVE IRAQ/AFGHAN SERVICE</p>
<p>NO IRAQ/AFGHAN SERVICE</p>
<p>OTHER PHYSICAL SYMPTOMS SCREEN OTHER PHYSICAL SYMPTOMS SCREEN SKIN LESION SCREEN NEGATIVE</p>
<p>SKIN LESION SCREEN POSITIVE</p>
<p>UNEXPLAINED FEVERS SCREEN NEGA UNEXPLAINED FEVERS SCREEN POSI</p></td>
</tr>
<tr class="odd">
<td>MENTAL HEALTH</td>
<td><p>CURRENT F/U OR RX FOR DEPRESSI DEP SCREEN 2 QUESTION NEG</p>
<p>DEP SCREEN 2 QUESTION POS DEPRESSION ASSESS INCONCLUSIVE DEPRESSION ASSESS NEGATIVE (NO DEPRESSION ASSESS POSITIVE (MD DEPRESSION TO BE MANAGED IN PC NO DEPRESSIVE SX NEED INTERVEN PT REFUSES TO TAKE ANTIPSYCHOT PTSD SCREEN NEGATIVE</p>
<p>PTSD SCREEN POSITIVE REFERRAL TO MENTAL HEALTH REFUSED AIM EVALUATION</p>
<p>REFUSED DEPRESSION ASSESSMENT REFUSED DEPRESSION RX/INTERVEN REFUSED DEPRESSION SCREENING UNABLE TO SCREEN-ACUTE MED CON UNABLE TO SCREEN-CHRONIC MED C ZZPTSD SCREEN NEGATIVE</p></td>
</tr>
</tbody>
</table>