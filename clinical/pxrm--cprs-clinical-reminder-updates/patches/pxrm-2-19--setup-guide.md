---
title: PXRM*2*19 Home Telehealth Install and Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: Home Telehealth Install and
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*19
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > The purpose of this project is to release new national reminders and reminder dialogs that will be used by Care Coordinators (Nurses, Social Workers, Rehab Specialists, Dietitians, Pharmacists and Psychologists) managing patients enrolled in HT programs.
audience: 
keywords: 
  - blockquote
  - class
  - ccht
  - even
  - caregiver
  - last
  - care
  - colspan
  - style
  - width
page_count: 0
word_count: 62943
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 11
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_19_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_19_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-19-home-telehealth-install-and-setup-guide/001.png)

Home Telehealth (HT)

> PXRM\*2\*19 TIU\*1\*258 GMTS\*2.7\*98INSTALLATION and SETUP GUIDEJuly 2017

> Department of Veterans Affairs Office of Information & Technology (OI&T)

> Enterprise Program Management Office (EPMO)

> <u>Contents</u>

3.  [Load the distribution. 14](#load-the-distribution.)
    1.  [Backup a Transport Global 14](#backup-a-transport-global)
    2.  [Compare Transport Global to Current System 15](#compare-transport-global-to-current-system)
    3.  [Verify Checksums in Transport Global 15](#verify-checksums-in-transport-global)
    4.  [Print Transport Global (optional) 15](#print-transport-global-optional)
4.  [Install the build. 15](#install-the-build.)
5.  [Install File Print 15](#install-file-print)
6.  [Build File Print 16](#build-file-print)
7.  [Post-Install Routines 16](#post-install-routines)
8.  [Deletion of init routines 17](#deletion-of-init-routines)
1.  [Create a new user class in for your HT clinicians 26](#create-a-new-user-class-in-for-your-ht-clinicians.)
2.  [Edit your “CCHT TEMPLATES” folder in SHARED TEMPLATES to be HT TEMPLATES 26](#edit-your-ccht-templates-folder-in-shared-templates-to-be-ht-templates.)
3.  [Expand the HT_TXML_TEMPLATES.ZIP file to a known location. 26](#_bookmark26)
4.  [Create GUI dialogs for the HT reminder dialogs 26](#create-gui-dialogs-for-the-ht-reminder-dialogs-in-the-document-titles-drawer-and-follow-the-instructions-for-linking-the-dialogs-to-the-correct-note-titles)
5.  [Verify that the four new HT clinical reminders launch (reminder dialogs linked) from the Reminders drawer 29](#_bookmark28)
6.  [Create/edit the consult quick order to HOME TELEHEALTH ENROLLMENT OUTPT 31](#createedit-the-consult-quick-order-to-home-telehealth-enrollment-outpt)
7.  [Configure two new Health Summary types for the CPRS GUI Reports tab. 33](#configure-two-new-health-summary-types-for-the-cprs-gui-reports-tab.)
8.  [Assign the TIU HT MENU and (optional) PXRM HT DEFINITION EDIT to CAC(s) 33](#assign-the-tiu-ht-menu-and-optional-pxrm-ht-definition-edit-to-cacs.)
9.  [Link the HT templates to NOTE TITLES 33](#link-the-ht-templates-to-note-titles-after-making-sure-that-the-nine-reminder-dialogs-and-two-txml-templates-are-tested-and-ready-to-go.)
10. [(Optional for all sites) If you need to change the FREQUENCY of the HT PERIODIC EVALUATION. 35](#_bookmark34)
11. [Build the 5 reminder report templates and do sample runs of each, with a short date range. 36](#build-the-5-reminder-report-templates-and-do-sample-runs-of-each-with-a-short-date-range.)

7/12/2017 Home Telehealth Templates Installation Guide iii

#### Introduction 

> The purpose of this project is to release new national reminders and reminder dialogs that will be used by Care Coordinators (Nurses, Social Workers, Rehab Specialists, Dietitians, Pharmacists and Psychologists) managing patients enrolled in HT programs.

> The National Office of Connected Care (10P8) wishes to have a comprehensive, integrated template set in use at all VA facilities caring for Home Telehealth patients.

#### NOTE: These national patches and subsequent template set originated as the Care Coordination Home Telehealth (CCHT) Phase III Pilot program executed over several years at a small number of VA Medical Centers. As such, there are some steps in this document that should only apply to former pilot sites and some steps that apply only to non-pilot sites. These steps are marked accordingly.

> This document is an Installation and Setup guide. The intended audience is both IT patch installers and facility CACs. IT installers should ensure that CAC partners receive a copy of this guide and work closely with CACs before, during, and after the installation.

> The HT project is being distributed as a bundled build containing the following patches:

> PXRM\*2\*19 installs the new national reminders and dialogs, queues a report to run and sends MailMan output to the Clinical Reminders mail group.

> The pre-install will disable PXRM options and protocols; run two routines that will rename any program-specific HEALTH FACTORS or EDUCATION TOPICS found at CCHT Pilot sites where those entries are installed at National IENs; and remove any previous version of the Reminder Exchange file used by the patch install.

> The post-install will re-enable the options and protocols; invoke the Reminder Exchange utility to install the Clinical Reminders content; prompt for recipients and then queue the MailMan report; attempt to set the ORWPCE EXCLUDE HEALTH FACTORS and TIU TEMPLATE REMINDER DIALOGS parameters for the relevant entries; and send an install message to the local Clinical Reminders mail group.

> PXRM Inventory

> Reminder Definitions

> VA-HT CAREGIVER RISK ASSESSMENT

> VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT CONTINUUM OF CARE (INITIAL)

> VA-HT OBJ BARRIERS TO LEARNING

> VA-HT OBJ CAREGIVER NAME/RELATIONSHIP VA-HT OBJ CATEGORY OF CARE LAST

> VA-HT OBJ CCM RATING LAST

> VA-HT OBJ CONTINUUM OF CARE LAST DONE VA-HT OBJ EDUCATION TOPICS ALL

> VA-HT OBJ EMERGENCY PRIORITY RATING LAST VA-HT OBJ MEDICATION RECONCILIATION

> VA-HT OBJ NIC/CCM RATING LAST VA-HT PERIODIC EVALUATION

> Reminder Dialogs

> VA-HT ASSESSMENT TREATMENT PLAN TEMPLATE VA-HT CAREGIVER ASSESSMENT TEMPLATE

> VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL VA-HT CONTINUUM OF CARE TEMPLATE

> VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT CONTINUUM OF CARE (INITIAL)

> VA-HT DISCHARGE TEMPLATE VA-HT INTERVENTION TEMPLATE VA-HT PERIODIC EVALUATION

> VA-HT SCREENING CONSULT TEMPLATE

> VA-HT TECH EDUCATION & INSTALLATION TEMPLATE VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS VA-HT VIDEO VISIT TEMPLATE

> Reminder Terms

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>VA-HT BL GEC BASIC ADLS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-HT BL GEC IADLS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT BL HT BASIC ADLS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT BL HT IADLS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT BL NIC/CCM CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT CAREGIVER RELATIONSHIP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT CAREGIVER RISK ASSESSMENT DONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT CATEGORY OF CARE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT CCF DOES NOT MEET CCM CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT CCF DOES NOT MEET NIC CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT CCF FOLLOW-UP ASSESSMENT COMPLETED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT CCF INITIAL ASSESSMENT COMPLETED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT CCF MEETS CHRONIC CARE MGMT CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT CCF MEETS NIC CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT CCF UNPAID CAREGIVER-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT CCM (CHRONIC CARE MGMT) CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT DISCHARGE REASONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT EMERGENCY PRIORITY RATINGS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT ENROLLMENT-START DATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT ENROLLMENT-START DATE (PREV ENROLL)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT MEDICATIONS VIA NON-PROVIDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT PERIODIC EVALUATION COMPLETED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT PT/CAREGIVER LIST OF ACTIVE MEDICATIONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT PT/CAREGIVER QUESTIONS ON MEDICATIONS</p>
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
<p>VA-HT SUPPRESS FOR AGE &lt;75</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-HT UNABLE TO SCREEN CAREGIVER</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Reminder Taxonomies

> VA-HT ENCOUNTER PHONE 21 VA-HT ENCOUNTER PHONE 11 VA-HT ENCOUNTER PHONE 5

> New Health Factors

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT (HOME TELEHEALTH)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT BARRIERS TO LEARNING</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT BATHING HELP/SUPRVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT BATHING HELP/SUPRVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT BED MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT BED MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER ASSESSMENT SCREEN COMPLETED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL BEREAVE SUPPORT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL C/G SUPPORT GRP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL EDUC/TRAINING</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL FAMILY COUNSEL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL INDIVID COUNSEL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL MEDICAL EVAL,F/U</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL OTHER SERVICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL SOCIAL WORK</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL SVCS IN PLACE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REVIEW OF WRITTEN MATERIALS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER STATES ESSENTIAL CONCEPTS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CATEGORY OF CARE-ACUTE CARE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CATEGORY OF CARE-CHRONIC CARE MGMT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CATEGORY OF CARE-HEALTH PROMOTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CATEGORY OF CARE-NON INSTITUTIONAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CATEGORY OF CARE-OTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF 1 OR MORE BEHAV/COGN PROBLEMS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF 12 OR MORE CLINIC STOPS PAST YR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF 2 OR MORE ADL DEFICITS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF AGE 75 OR GREATER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF AGITATED/DISORIENTED-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF AGITATED/DISORIENTED-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER ACCESSIBLE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER CAN INCREASE HELP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER CAN'T INCREASE HELP</p>
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
<p>HT CCF CAREGIVER LIVES WITH PT-NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER LIVES WITH PT-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER NOT ACCESSIBLE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-ADL HELP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-CHILD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-EMOTIONAL SUPPORT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-FRIEND/NEIGHBOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-IADL HELP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-OTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER'S CITY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER'S NAME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER'S PHONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER'S STATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER'S STREET ADDRESS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER'S ZIP CODE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-SPOUSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF COMPLEXITY TOO GREAT-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF COMPLEXITY TOO GREAT-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DELUSIONS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DELUSIONS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DIFFIC REASONABLE DECISIONS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DIFFIC REASONABLE DECISIONS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DOES NOT MEET CCM CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DOES NOT MEET NIC CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF FLARE UP CHRONIC CONDITION-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF FLARE UP CHRONIC CONDITION-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF FOLLOW-UP ASSESSMENT COMPLETED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF GROUP SETTING NON RELATIVES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-AUDITORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-NONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-OLFACTORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-SENSORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-TACTILE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-VISUAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF INITIAL ASSESSMENT COMPLETED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIFE EXPECTANCY &lt; 6 MO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES ALONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES ALONE IN COMMUNITY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES AT OTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES BOARD AND CARE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES DOMICILIARY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES HOMELESS</p>
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
<p>HT CCF LIVES HOMELESS SHELTER</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES NURSING HOME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES PRIVATE HOME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES WITH ADULT CHILD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES WITH CHILD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES WITH OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES WITH SPOUSE &amp; OTHERS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES WITH SPOUSE ONLY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF MEETS CHRONIC CARE MGMT CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF MEETS NIC CATEGORY A CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF MEETS NIC CATEGORY B CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF MEETS NIC CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF MOOD DISORDER DEPRESSION-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF MOOD DISORDER DEPRESSION-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF MOOD DISORDER MANIC-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF MOOD DISORDER MANIC-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF NIC CRITERIA NO-ACUTE CARE MGMT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF NIC CRITERIA NO-HLTH PROMOTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF PHYSICALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF PHYSICALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF POTENTIAL FOR INCR INDEP-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF POTENTIAL FOR INCR INDEP-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF PROBLEMS WITH 3 OR MORE ADLS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF PROBLEMS WITH 3 OR MORE IADL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF PTSD/OTHER ANXIETY-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF PTSD/OTHER ANXIETY-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF RECOMMEND REFERRAL-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF RECOMMEND REFERRAL-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF RESISTING CARE-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF RESISTING CARE-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF SERVICES IN PLACE-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF SERVICES IN PLACE-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF SUBST ABUSE/DEPENDENCE-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF SUBST ABUSE/DEPENDENCE-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF UNPAID CAREGIVER-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF UNPAID CAREGIVER-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF VERBALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF VERBALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF WANDERING-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF WANDERING-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CG/VETERAN REFERRAL COMPLETED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CG/VETERAN REFERRAL(S) NOT UTILIZED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CLINICAL REASON FOR ENROLLMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CONSULTS/REFERRALS RECOMMENDED</p>
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
<p>HT CONTINUUM OF CARE (CCF)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT MANAGING MEDS/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT MANAGING MEDS/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT MNG FINANCES/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT MNG FINANCES/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT PREPARE MEALS/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT PREPARE MEALS/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT TRANSPORTATION/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT TRANSPORTATION/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT USING PHONE LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT USING PHONE LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT W/ HOUSEWORK/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT W/ HOUSEWORK/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT WITH SHOPPING/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT WITH SHOPPING/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-ADMITTED TO NURSING HOME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-ALL ISSUES ADDRESSED(NO)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-ALL ISSUES ADDRESSED(YES)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-HAS MET GOALS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-NO RESPONSE TO PROGRAM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-NO VA PRIMARY CARE SVCS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-OTHER FOLLOW-UP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-PATIENT IS DECEASED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-PROLONGED HOSPITALIZATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-PROVIDER REQUESTS DC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-PT/CG REQUEST DC SERVICES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO HOSPICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO MENTAL HEALTH</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO NEW LOCATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO PRIMARY CARE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO SOCIAL WORK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-RELOCATED OUT OF SVC AREA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-UNABLE TO OPERATE DEVICES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-COPD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-DEPRESSION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-DIABETES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-HEART FAILURE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-HYPERTENSION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-OBESITY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-PTSD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-SUBSTANCE ABUSE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 6 Home Telehealth Templates Install and Setup Guide 7/12/2017

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT DISINTERESTED/LACKS MOTIVATION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT DRESSING HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DRESSING HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EATING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EATING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EMERG PRIORITY HIGH-IMMEDIATE EVAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EMERG PRIORITY LOW-HAS RESOURCES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EMERG PRIORITY MOD-SVCS AFTER 3-7D</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT ENROLLMENT-ENDING DATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT ENROLLMENT-START DATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT ENROLLMENT-START DATE (PREV ENROLL)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EQUIP INSTALLED BY OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EQUIP INSTALLED BY SUPPORT STAFF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EQUIP INSTALLED BY VETERAN/CAREGIVER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT GETS MEDS VIA NON-VA PROVIDER-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT GETS MEDS VIA NON-VA PROVIDER-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT HEALTH EDUCATION PLAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT HEALTH EDUCATION RESPONSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT INDICATIONS-# OUTPT VISITS PAST YR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT INDICATIONS-DISTANCE (HOURS)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT INDICATIONS-DISTANCE (MILES)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT INDICATIONS-HX HIGH COST/HIGH USE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT INDICATIONS-HX HOSPITALIZATONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-ANGRY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-ANXIETY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-APHASIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-COGNITIVE IMPAIRMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-CULTURAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-HEARING IMPAIRED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-HOMELESS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-IMPAIRED MEMORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-NONE IDENTIFIED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-NOT MOTIVATED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-OVERWHELMED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-PAIN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-PHYSICAL LIMITATIONS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-POOR CONCENTRATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-UNABLE TO READ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-UNABLE TO WRITE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-VISUALLY IMPAIRED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT MEALS PREPARED BY OTHER/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT MEALS PREPARED BY OTHER/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT MEETS TELEHEALTH CRITERIA(NO)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT MEETS TELEHEALTH CRITERIA(YES)</p>
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
<p>HT MOVE INDOOR HELP/SUPERV LAST 7D-NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT MOVE INDOOR HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT NEEDS REINFORCEMENT/REVIEW/FOLLOW-UP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT NO EVIDENCE OF LEARNING</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT NO FOLLOW-UP NEEDED/INDICATED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PERIODIC EVALUATION COMPLETED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT PLAN-MED DISCREP SENT TO PROVIDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PLAN-REVIEWED LIST OF CURRENT MEDS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT PT/CG HAS LIST OF ACTIVE MEDS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PT/CG HAS LIST OF ACTIVE MEDS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT PT/CG HAS QUESTIONS ON MEDS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PT/CG HAS QUESTIONS ON MEDS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REASON FOR NON-ENROLLMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT RECENT CHANGE IN FUNCTION-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT RECENT CHANGE IN FUNCTION-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT REFERRAL-CONSULT COMPLETION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REFERRALS FOR VETERAN/CAREGIVER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT REFERRALS-CAREGIVER NOT SATISFIED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REFERRALS-CAREGIVER SATISFIED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT REPEAT DEMONSTRATION NEXT VISIT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TEACH CAREGIVER/FAMILY/SIGNIF OTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TOILET HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TOILET HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TRANSFERS HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TRANSFERS HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT UNABLE TO SCREEN CAREGIVER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VET NOT INTERESTED TELEHEALTH PROGRAM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VET/CAREGIVER VIEW VIDEOS/HEALTH TV</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN REFERRAL EDUC/TRAINING</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN REFERRAL OTHER SERVICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN REFERRAL SVCS IN PLACE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN REVIEW OF WRITTEN MATERIALS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN STATES ESSENTIAL CONCEPTS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN'S GOAL FOR ENROLLMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT W/C MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT W/C MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

> New Education Topics

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT</p>
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
<p>VA-HOME TELEHEALTH-IN HOME MONITORING</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-HOME TELEHEALTH-MEDICATION MANAGEMENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TIU Template Fields

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>BLANK SPACE1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OPTIONAL TEXT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OTHER(REQ-DISP ONLY)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TEXT (1-60 CHARACTERS) REQ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT EDIT50</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT SPECIFY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT VITAL SIGNS MODE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT W-P2LINES(R)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT W-P4LINES(R)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-HT W-P6LINES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-HT W-P6LINES(R)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> TIU\*1.0\*258 deploys the twelve official titles for the Home Telehealth (HT) program, and will ensure compliance with the HT program’s TIU Document Definitions Hierarchy. The end result from the TIU installation should be a document class named HOME TELEHEALTH NOTES installed under the PROGRESS NOTES document class. Contained in HOME TELEHEALTH NOTES will be the titles for HT. They are:

> HT ASSESSMENT TREATMENT PLAN NOTE HT CAREGIVER ASSESSMENT NOTE

> HT CONTINUUM OF CARE NOTE HT DISCHARGE NOTE

> HT INTERVENTION NOTE HT NOTE

> HT PERIODIC EVALUATION NOTE

> HT SCREENING CONSULT (will be installed under CONSULTS document class) HT SUMMARY OF EPISODE NOTE

> HT TECH EDUCATION NOT

> HT TELEPHONE CASE MANAGEMENT NOTE HT VIDEO VISIT NOTE

> The patch has an environment check routine, TIUP258E, which searches for several items and scenarios:

- CLINICAL COORDINATOR user class
- Document Classes:
  - CARE COORDINATION HOME TELEHEALTH NOTES
  - HOME TELEHEALTH NOTES
  - CONSULTS
- Pre-existing “CCHT” or “HT” named local titles (e.g. “CCHT NOTE” or “HT NOTE”)

> If CLINICAL COORDINATOR or CONSULTS are missing, the installation will abort and cannot continue until the issue is corrected.

> For any pre-existing “CCHT” or “HT” local titles, the environment check is only concerned with titles that have a name match to an incoming national title and are not part of CONSULTS, CARE COORDINATION HOME TELEHEALTH NOTES, or HOME TELEHEALTH NOTES.

> If any local titles meet these criteria, a list of each title along with the IEN from TIU DOCUMENT DEFINITION (#9825.1) will be displayed on the screen and the installation will abort.

> For example, if a site already has a title named HT NOTES but that title is \*not\* sitting under a document class of CARE COORDINATION HOME TELEHEALTH NOTES, or HOME

> TELEHEALTH NOTES, then this title will be displayed on the installer’s screen and the install will abort. Alternatively, if a title named HT PERIODIC EVALUATION is found under HOME TELEHEALTH NOTES, this will not trigger an abort condition for the installation.

> Example display from a test installation

> The TIU pre-install routine will prepare the TIU environment to receive the new HT titles. For CCHT pilot sites, this means inactivating the CARE COORDINATION HOME TELEHEALTH NOTES document class and renaming it to HOME TELEHEALTH NOTES. After that, the relevant “CCHT” note titles will be renamed to “HT” equivalents provided the titles are a member of the HOME TELEHEALTH NOTES document class (or CONSULTS document class in the case of CCHT SCREENING CONSULT). For a given title, if a name match is found, but that title is found in a different document class than expected, a new HT title will be created (during post-install) in lieu of renaming the CCHT title.

> For sites that did not participate in the CCHT pilot program, the pre-install routine will inactivate and rename the CARE COORDINATION HOME TELEHEALTH NOTES document class. Any pre-existing local title(s) with will be renamed (“CCHT” to “HT”) but only if the title(s) are found in the expected document class.

> The post-install routine will complete the document definition installations; map the newly introduced HT titles to the HT Enterprise Standard Titles; and if possible, activate the new titles. If the mapping or activation fails for a given title, those tasks can be accomplished locally via TIU package options.

> GMTS\*2.7\*98 adds two new Health Summary reports for display on the CPRS Reports tab. These reports will display both local and remote data.

> This patch contains an environment check routine, GMTSPI98, that will run when the KIDS build is first loaded. This routine checks for the presence of any file entries at IEN 5000018 and 5000019 in the ^GMT(142 global. These IENs should be undefined/empty as the 5000000+ IEN range is reserved for new National remote health summary types. If an entry is found at either location, the install will abort. If this occurs, the site should contact the National Help Desk for assistance with the Health Summary package and moving the existing entry(ies) to a different IEN in the ^GMT(142 global. Once this has been corrected, the site may then re-load and re- install the bundle.

> The pre-install will remove any previous version of the Reminder Exchange file used to create the two new remote Health Summary Types. The post-install will create a stub entry in HEALTH SUMMARY TYPE (#142) for each of the two remote Health Summary Types and then call the Reminder Exchange utility to populate the stub entries with the content for each Health Summary Type. All other Health Summary items are installed via Reminder Exchange by the PXRM\*2.0\*19 patch.

#### Web Sites

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 36%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Site</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>URL</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>National Clinical Reminders site</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals, PowerPoint</p>
<p>presentations, and other information about Clinical Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>National Clinical Reminders Committee</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncrc</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>public/default.aspx</u></a></p>
</blockquote></td>
<td><blockquote>
<p>This committee directs the development of new and revised</p>
<p>national reminders</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA Software</p>
<p>Document Library</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals for Clinical</p>
<p>Reminders and related applications.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Getting Help

> If you require further technical assistance, please notify your local IT support to log a national CA Service Desk Manager (SDM) ticket (previously a Remedy™ ticket) or contact the VA Service Desk at 1-888-596-4357 and have them submit a national CA ticket to the Incident Area: NTL.APP.VISTA.CLINICAL REMINDERS 2_0 and we will contact you.

#### Pre-Installation 

> This manual describes how to install the bundled patches, PXRM\*2\*19, GMTS\*2.7\*98, and TIU\*1\*258.

#### Required Software for PXRM\*2\*19

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package/Patch</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Clinical Reminders</p>
</blockquote></td>
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td><blockquote>
<p>2.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEN. MED. REC. – VITALS</p>
<p>GMRV*5*25</p>
</blockquote></td>
<td><blockquote>
<p>GMRV</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Health Summary</p>
</blockquote></td>
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td><blockquote>
<p>2.7</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HL7</p>
</blockquote></td>
<td><blockquote>
<p>HL</p>
</blockquote></td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Kernel</p>
</blockquote></td>
<td><blockquote>
<p>XU</p>
</blockquote></td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MailMan</p>
</blockquote></td>
<td><blockquote>
<p>XM</p>
</blockquote></td>
<td><blockquote>
<p>7.1</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NATIONAL DRUG FILE</p>
<p>PSN*4.0*176</p>
</blockquote></td>
<td><blockquote>
<p>PSN</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pharmacy Data Management</p>
<p>PSS*1.0*133</p>
</blockquote></td>
<td><blockquote>
<p>PSS</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Outpatient Pharmacy</p>
<p>PSO*7.0*299</p>
</blockquote></td>
<td><blockquote>
<p>PSO</p>
</blockquote></td>
<td><blockquote>
<p>7.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RADIOLOGY/NUCLEAR MEDICINE</p>
<p>RA*5*56</p>
</blockquote></td>
<td><blockquote>
<p>RA</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOOLKIT</p>
<p>XT*7.3*111</p>
</blockquote></td>
<td><blockquote>
<p>XT</p>
</blockquote></td>
<td><blockquote>
<p>7.3</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA FileMan</p>
</blockquote></td>
<td><blockquote>
<p>DI</p>
</blockquote></td>
<td><blockquote>
<p>22.2</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Estimated Installation Time: approximately 20 minutes

#### NOTE: We recommend that a Clinical Reminders Manager or CAC be present during the install, so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

> Pre-Installation Instructions

1.  Please review the setup steps beginning on page [<u>18</u>](#set-up) before starting the installation. The installation will do the following:
    - Disable PXRM menu options and protocols.
    - Delete any previous version of the associated Reminder Exchange entry.
    - At pilot program sites, converts a subset of the pre-existing local HT components to National components.
2.  *Pilot sites.* Inspect and remove any pre-existing “CCHT” or “HT” entries at the SYSTEM level for the following parameters: ORWPCE EXCLUDE HEALTH FACTORS. Use the General Parameter Tools menu \[XPAR MENU TOOLS\] to clean up these parameter entries.

Select OPTION NAME: XPAR MENU TOOLS General Parameter Tools menu

> LV List Values for a Selected Parameter LE List Values for a Selected Entity

> LP List Values for a Selected Package LT List Values for a Selected Template EP Edit Parameter Values

> ET Edit Parameter Values with Template EK Edit Parameter Definition Keyword

> Select General Parameter Tools \<TEST ACCOUNT\> Option: EP Edit Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: ORWPCE EXCLUDE HEALTH FACTORS Excluded Health

> Factors

> ORWPCE EXCLUDE HEALTH FACTORS may be set for the following:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 8%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>User</p>
</blockquote></th>
<th>USR</th>
<th>[choose</th>
<th><blockquote>
<p>from</p>
</blockquote></th>
<th><blockquote>
<p>NEW PERSON]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>Location</p>
</blockquote></td>
<td>LOC</td>
<td>[choose</td>
<td><blockquote>
<p>from</p>
</blockquote></td>
<td><blockquote>
<p>HOSPITAL LOCATION]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>SRV</td>
<td>[choose</td>
<td><blockquote>
<p>from</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE/SECTION]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td>[choose</td>
<td><blockquote>
<p>from</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
<td colspan="3"><blockquote>
<p>[DVF.FO-SLC.MED.VA.GOV]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>Package</p>
</blockquote></td>
<td>PKG</td>
<td colspan="3"><blockquote>
<p>[ORDER ENTRY/RESULTS REPORTING]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter selection: 5 System DVF.FO-SLC.MED.VA.GOV

> -- Setting ORWPCE EXCLUDE HEALTH FACTORS for System: DVF.FO-SLC.MED.VA.GOV --

> Select Sequence: ?

> Sequence Value

2.  CCHT ASSESSMENT/TREATMENT PLAN
3.  CCHT CAREGIVER RISK ASSESSMENT SCREEN
4.  CCHT CONTINUUM OF CARE
5.  CCHT DISCHARGE
6.  CCHT REFERRALS FOR VETERAN/CAREGIVER
7.  CCHT TELEHEALTH DELIVERY/INSTALL MODE
8.  CCHT TELEHEALTH DEMOGRAPHICS

> Select Sequence: 2

> Sequence: 2// 2

> Health Factor: CCHT ASSESSMENT/TREATMENT PLAN// HT ASSESSMENT/TREATMENT PLAN

3.  Before beginning the installation, the IT person who will install the patch bundle should determine the individuals and/or mail group(s) at the local facility that should receive the queued MailMan report generated by the post-install. This report should be shared with local Clinical Reminders support/configuration staff and/or any other local staff as deemed appropriate by each facility.
4.  Facility CACs: Review local TIU titles for any titles that may present conflicts as explained in the TIU\*1.0\*258 section of the Introduction. Doing this task before IT

> attempts the installation will avoid delay if conflicts are found and the patch install is aborted.

# Installation 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Installation](#installation)
- [Set-up](#set-up)
    - [Appendix C: HT Queued MailMan Report](#appendix-c-ht-queued-mailman-report)
    - [Appendix D: Contents of the Packed Reminder Export HT Templates/Reminders Set](#appendix-d-contents-of-the-packed-reminder-export-ht-templatesreminders-set)
    - [Appendix F: Installation Example](#appendix-f-installation-example)
    - [Appendix G: FileMan Searches for HT Pilot Sites](#appendix-g-fileman-searches-for-ht-pilot-sites)
    - [Appendix H: Health Factors](#appendix-h-health-factors)
    - [Appendix J: Education Topics](#appendix-j-education-topics)
  - [Appendix K: Acronyms and Glossary](#appendix-k-acronyms-and-glossary)
> This build can be installed with users on the system, but it should be done during non-peak hours.
> *The installation needs to be done by a person with DUZ(0) set to "@."*
1.  <span id="_bookmark8" class="anchor"></span>Retrieve host file containing the multi-package build and zip file containing new TXML templates.
> Use sftp to access the build from one of the following locations:
> The name of the host file is HT_TEMPLATES_1_0.KID
> The name of the zip file is HT_TXML_TEMPLATES.ZIP – send this file to the Clinical Reminders CAC at the site for which you are installing.
2.  <span id="_bookmark9" class="anchor"></span>Install the build first in a training or test account.
> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

#### Load the distribution.

> In programmer mode, type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and HT_TEMPLATES_1.0.KID at the Host File prompt.

#### Example

> From the Installation menu, you may elect to use the following options:

#### Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

#### Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

#### Verify Checksums in Transport Global

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.
> Retrieve the file again from the anonymous directory (in case there was corruption in transferring) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

#### Print Transport Global (optional)

> This option will allow you to view the components of the KIDS build.

#### Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build xxx and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.
> Answer "NO" to the following prompts:
> Want KIDS to INHIBIT LOGONs during install? NO// NO
> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// NO
> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO
> NOTE: DO NOT QUEUE THE INSTALLATION, because this installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries.

#### Installation Example

> [<u>See Appendix</u>](#appendix-f-installation-example) <u>G</u>.

#### Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

#### Build File Print

> Use the KIDS Build File Print option to print out the build components.

#### Post-Install Routines

> Following successful installation of the KIDS build, the post-install routine invokes the Reminders Exchange Utility's silent installer to correctly install the HT Document Definition hierarchy, maps the newly introduced HT titles to the HT Enterprise Standard Titles, and if possible, activates the new titles.
- The installation will place the following major file entries in the Reminder Exchange file \#811.8 (full contents of the Reminder Exchange file are in [<u>Appendix D</u>](#appendix-d-contents-of-the-packed-reminder-export-ht-templatesreminders-set)):
> REMINDER DIALOG
> VA-HT ASSESSMENT TREATMENT PLAN TEMPLATE VA-HT CAREGIVER ASSESSMENT TEMPLATE
> VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL VA-HT CONTINUUM OF CARE TEMPLATE
> VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT CONTINUUM OF CARE (INITIAL)
> VA-HT DISCHARGE TEMPLATE VA-HT INTERVENTION TEMPLATE VA-HT PERIODIC EVALUATION
> VA-HT SCREENING CONSULT TEMPLATE
> VA-HT TECH EDUCATION & INSTALLATION TEMPLATE VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS VA-HT VIDEO VISIT TEMPLATE
> REMINDER DEFINITION
> VA-HT CAREGIVER RISK ASSESSMENT
> VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT CONTINUUM OF CARE (INITIAL)
> VA-HT OBJ BARRIERS TO LEARNING
> VA-HT OBJ CAREGIVER NAME/RELATIONSHIP VA-HT OBJ CATEGORY OF CARE LAST
> VA-HT OBJ CCM RATING LAST
> VA-HT OBJ CONTINUUM OF CARE LAST DONE VA-HT OBJ EDUCATION TOPICS ALL
> VA-HT OBJ EMERGENCY PRIORITY RATING LAST VA-HT OBJ MEDICATION RECONCILIATION
> VA-HT OBJ NIC/CCM RATING LAST VA-HT PERIODIC EVALUATION
- If you need to change the frequency of the HT PERIODIC EVALUATION reminder to a value other than the exported 180 days, use the PXRM HT DEFINITION EDIT option. This option has been created expressly to allow sites to edit the frequency for the HT PERIODIC EVALUATION reminder. The option should be assigned as a secondary menu item to the user(s) responsible for maintaining the Home Telehealth reminder definitions.
- The post-init of this GMTS patch will install the new entries in the HEALTH SUMMARY TYPE file (#142). They are:
> REMOTE HT CLINICAL REMINDERS REMOTE HT TRACKING
> The stub entries in the ^GMT(142 global during pre-install are then populated by the Reminder Exchange file GMTS HS TYPE FOR VA-HT which is silently installed via the Reminder Exchange utility.

#### Deletion of init routines

> PXRMP19B, PXRMP19I, TIUP258, and GMTSPI98 can safely be deleted from the system once installation is successful and all HT reminders, reminder dialogs, and associated templates have been verified to be complete and working as expected. Local IT staff should consider keeping a copy of these routines as they may prove useful in the event of any unexpected issues with this patch. PXRMP19A should remain on the system until such time as Clinical Reminder CACs and or Home Telehealth staff determine that the MailMan report described in Appendix C is no longer necessary. At that time, PXRMP19A, may also be deleted from the system.

#### Assign TIU HT MENU

> The TIU HT MENU includes options to facilitate implementation of the TIU support for Home Telehealth. It should be assigned to individuals tasked with such activities.

# Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Overview

> Installation of the multi-package build does the following:

- Enables PXRM options and protocols,
- Installs the associated Reminder Exchange entries.
- Queues a single report to run and sends output via MailMan message to recipients selected during installation.

> The TIU patch exports a new menu with two options: TIU HT MENU

> This menu includes options to facilitate implementation of the TIU support for Home Telehealth.

> TIU HT TITLE MAPPINGS

> This option prints a list of all HT Titles, with their Status and VHA Enterprise Standard Titles. This will allow you to verify that the appropriate titles were installed, renamed, and mapped by patch TIU\*1\*258.

> TIU HT VERIFY TITLES

> This option prints a list of all HT Titles, with their Status and Print Names. This will allow you to verify that the appropriate titles were installed, renamed, or inactivated by patch TIU\*1\*258.

#### Background – Design Logic

> For the reminders module imports:

> There are three variations of the HT CONTINUUM OF CARE reminder dialog/template:

- Two are linked to reminder definitions
  - VA-HT CONTINUUM OF CARE (INITIAL) *(has a non-interactive HF for initial assessment)*
  - VA-HT CONTINUUM OF CARE (FOLLOW-UP) *(has a non-interactive HF for f/u assessment)*
- One template, the HT CONTINUUM OF CARE template, has an interactive required item for initial/follow-up at the top of the template. This template is attached to a note title of same name and is also stand-alone in Shared Templates.

> These reminder dialogs will be linked to note titles of the same name: HT ASSESSMENT TREATMENT PLAN NOTE

> HT CAREGIVER ASSESSMENT NOTE HT CONTINUUM OF CARE NOTE

> HT DISCHARGE NOTE

> HT INTERVENTION NOTE HT NOTE

> HT PERIODIC EVALUATION NOTE HT TECH EDUCATION

> HT TELEPHONE CASE MANAGEMENT NOTE HT VIDEO VISIT NOTE

> Of the 13 reminder definitions:

- Four of the packed reminder exports are true “clinical reminders” in the Reminders drawer: *(Displayed here in order of how they will fire during a Veteran’s course of HT care):*
  - VA-HT CONTINUUM OF CARE (INITIAL)
  - VA-HT CAREGIVER RISK ASSESSEMENT
  - VA-HT PERIODIC EVALUATION
  - VA-HT CONTINUUM OF CARE (FOLLOW-UP)
- Nine reminder definitions are used to evaluate data objects:
  - VA-HT OBJ BARRIERS TO LEARNING
  - VA-HT OBJ CAREGIVER NAME/RELATIONSHIP
  - VA-HT OBJ CATEGORY OF CARE LAST
  - VA-HT OBJ CCM RATING LAST
  - VA-HT OBJ CONTINUUM OF CARE LAST DONE
  - VA-HT OBJ EDUCATION TOPICS ALL
  - VA-HT OBJ EMERGENCY PRIORITY RATING LAST
  - VA-HT OBJ MEDICATION RECONCILIATION
  - VA-HT OBJ NIC/CCM RATING LAST

> Three of the reminder dialogs will be “stand-alone” in the SHARED TEMPLATES HT folder:

- VA-HT CONTINUUM OF CARE TEMPLATE
- VA-HT CAREGIVER ASSESSMENT TEMPLATE
- VA-HT TECH EDUCATION & INSTALLATION TEMPLATE

#### For the two GUI dialog templates (.txml files):

- VA-HOME TELEHEALTH SCREENING is linked to the CONSULT SERVICE (file \#123.5) HOME TELEHEALTH ENROLLMENT OUTPT in the CPRS GUI Template Editor. It will be used in a consult QUICK ORDER to order the consult. (NOTE: It should be named HOME TELEHEALTH ENROLLMENT OUTPT in your file. This new naming does not affect the template in any way nor VistA Integration).

#### VA-HT MONTHLY MONITOR:

- will be linked to a note title of the same name (this is a text paragraph only and is non-interactive)
- will be “stand-alone” in SHARED TEMPLATES in the HT folder

> There are full HT templates embedded within other templates:

> The HT ASSESSMENT TREATMENT PLAN template has three collapsed (optional) templates embedded:

> VA-HT CONTINUUM OF CARE TEMPLATE VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL

> The HT CAREGIVER ASSESSMENT template contains two collapsed (optional) templates:

> VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL

> The HT PERIODIC EVALUATION template contains two collapsed (optional) templates:

> VA-HT CAREGIVER RISK ASSESSMENT VA-HT CAREGIVER/VETERAN REFERRAL

> VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS

> This template is intended for use by non-pilot sites to sweep up HT currently enrolled patients for the 4 new national HT clinical reminders where note documentation had been done without the standardized national HT reminder dialogs with health factors to trigger the new HT reminders when they should be due. It is for ONE-TIME use on current HT patients. This template should be used on each patient in order to set the health factors associated with the date of enrollment, date of last periodic evaluation, and the non-institutional care status. Once the health factors are set, the HT clinical reminders will now be applicable to each of these patients.

> The template should be added to the HT Templates folder within the Shared Templates folder of the CPRS GUI editor. Your site will create a GUI template dialog linked to the VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS. You will then link this template to the generic HT NOTE title.

> This template should be used soon after installation of the HT Templates bundle. The CAC should notify the HT Lead that the template is available for use. Once Care Coordinators have used the template on all HT currently enrolled patients, the HT Lead should notify the CAC that the GUI dialog template can be removed from service.

> *In summary*, this is a rather complex configuration, done for the convenience of HT clinicians at various sites who have different preferences.

> Since all of the four clinical reminders exist as templates on note titles and some are additionally stand-alone in CPRS’ Shared Templates, it’s possible that many HT clinicians may not go to the actual clinical reminders (Reminders drawer) to resolve their clinical reminders

> If HT clinicians are timely with their documentation, these four HT clinical reminders (which are basically 'documentation benchmarks') are most beneficial for HT site leads who would be running reminder report templates as they deem desirable, in order to check HT clinical reminder status across the enrolled patients at any point in time, for oversight and monitoring of timely documentation:

- A summary report of all four (4) HT clinical reminders (no individual patient data) with raw numbers and percentages of HT reminders due versus resolved
- Four (4) reminder report templates for EACH of the four (4) HT clinical reminders, for the user running the report to easily determine and communicate to other HT staff which individual patients have reminders past due with date.

> Four (4) reminder report templates for EACH of the (4) HT clinical reminders, for the user running the report to easily determine and communicate to other HT staff which individual patients have reminders past due with date.

> HT staff will now have an easy method of checking HT reminder status on individual patients, through the new Health Summary on the CPRS GUI Reports tab, as well as new data objects in templates that display reminder status.

> <span id="_bookmark21" class="anchor"></span>Setup Instructions – Summary Steps

> The following is a summary of the setup steps, with hyperlinks to detailed instructions and examples that follow.

1.  Map any local findings to the appropriate reminder terms
    1.  VA-HT ENROLLMENT-START DATE

> This term is released the health factor HT ENROLLMENT DATE.

> Map any local finding(s) representing the home telehealth enrollment date for the patient.

2.  VA-HT CCF INITIAL ASSESSMENT COMPLETED

> This term is released the health factor HT CCF INITIAL ASSESSMENT COMPLETED. Map any local finding(s) representing completion of the initial home telehealth continuum of care assessment.

3.  VA-HT CCF MEETS NIC CRITERIA

> This term is released the health factor HT CCF MEETS NIC CRITERIA.

> Map any local finding(s) representing the Non-Institutional Care criteria is met by the patient.

4.  VA-HT CCF DOES NOT MEET NIC CRITERIA

> This term is released the health factor HT CCF DOES NOT MEET NIC CRITERIA. Map any local finding(s) representing the Non-Institutional Care criteria is not met by the patient.

5.  VA-HT DISCHARGE REASONS

> This term is released with several health factors representing a patient’s discharge from home telehealth along with the specific reason.

> Map any local finding(s) representing the intent of this term.

6.  VA-HT ENROLLMENT-START DATE (PREV ENROLL)

> This term is released with the health factor HT ENROLLMENT-START DATE (PREV ENROLL).

> Map any local finding(s) representing documentation of an historical start date for home telehealth.

7.  VA-HT CCF FOLLOW-UP ASSESSMENT COMPLETED

> This term is released with the health factor HT CCF FOLLOW-UP ASSESSMENT COMPLETED.

> Map any local finding(s) representing completion of a follow-up home telehealth continuum of care assessment.

8.  VA-HT CCF MEETS CHRONIC CARE MGMT CRITERIA

> This term is released with the health factor HT CCF MEETS CHRONIC CARE MGMT CRITERIA.

> Map any local finding(s) representing the Chronic Care Management criteria is met by the patient.

9.  VA-HT CCF DOES NOT MEET CCM CRITERIA

> This term is released with the health factor HT CCF DOES NOT MEET CCM CRITERIA. Map any local finding(s) representing the Chronic Care Management criteria is not met by the patient.

10. VA-HT PERIODIC EVALUATION COMPLETED

> This term is released with the health factor HT PERIODIC EVALUATION COMPLETED. Map any local finding(s) representing the completion of the home telehealth periodic evaluation.

11. VA-HT CCF UNPAID CAREGIVER-YES

> This term is released with the health factor HT CCF UNPAID CAREGIVER-YES. Map any local finding(s) representing the Veteran has an unpaid caregiver on file for the current HT enrollment.

12. VA-HT UNABLE TO SCREEN CAREGIVER

> This term is released with the health factor HT UNABLE TO SCREEN CAREGIVER. Map any local finding(s) representing the inability to complete the Zarit caregiver risk Assessment.

13. VA-HT CAREGIVER RISK ASSESSMENT DONE

> This term is released with the MH finding for the Zarit Caregiver Risk Assessment . Map any local finding(s) representing then completion of the Zarit caregiver risk Assessment.

2.  Optional: [<u>Create a user class if your site wishes to restrict certain aspects TIU usage and/or</u> <u>implement business rules</u>](#create-a-new-user-class-in-for-your-ht-clinicians.).
3.  Create or edit folder in Shared Templates to house the HT Templates

> PILOT SITES: [<u>Edit the name of your “CCHT TEMPLATES” folder in SHARED</u>](#edit-your-ccht-templates-folder-in-shared-templates-to-be-ht-templates.) [<u>TEMPLATES to be "HT TEMPLATES".</u>](#edit-your-ccht-templates-folder-in-shared-templates-to-be-ht-templates.)

> NON-PILOT SITE:

1.  Create a folder named “HT TEMPLATES” in the SHARED TEMPLATES section of the CPRS GUI Template Editor.
2.  Create a GUI dialog in the HT TEMPLATES folder for the VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS. This template will be linked to the HT NOTE title. This template is used to set historical data for HT patients so that the HT clinical reminders will be triggered appropriately.
3.  When notified by the HT Lead, the CAC should remove the associated GUI template from service.
4.  [<u>Extract the contents of the “HT_TXML_TEMPLATES.ZIP” file to a location of your</u> <u>choosing. From that location, import the two txml files (shown below) into the CPRS GUI</u> <u>Template Editor, into your PERSONAL templates.</u>](#_bookmark26)
    1.  HT MONTHLY MONITOR.TXML
    2.  HT PROVIDER CONSULT.TXML
5.  [<u>Create GUI dialogs for the HT reminder dialogs in the DOCUMENT TITLES drawer</u>](#create-gui-dialogs-for-the-ht-reminder-dialogs-in-the-document-titles-drawer-and-follow-the-instructions-for-linking-the-dialogs-to-the-correct-note-titles) and link these items to the associated note.
    1.  HT ASSESSMENT TREATMENT PLAN TEMPLATE
    2.  HT CAREGIVER ASSESSMENT TEMPLATE
    3.  HT CONTINUUM OF CARE TEMPLATE
    4.  HT DISCHARGE TEMPLATE
    5.  HT INTERVENTION TEMPLATE
    6.  HT PERIODIC EVALUATION TEMPLATE
    7.  HT SCREENING CONSULT TEMPLATE
    8.  HT TECH EDUCATION & INSTALLATION TEMPLATE
    9.  HT VIDEO VISIT TEMPLATE
6.  [<u>Set the four new HT clinical reminders at the user level (yourself first) and verify that they</u> <u>launch (reminder dialogs linked) in the Reminders drawer.</u>](#_bookmark28) (They will be in the “All Evaluated” folder, no matter what the status is of each reminder for a patient.)
7.  [<u>Create/edit the consult quick order to HOME TELEHEALTH ENROLLMENT</u>](#createedit-the-consult-quick-order-to-home-telehealth-enrollment-outpt) <u>OUTPT</u>
8.  [<u>Configure the two new Health Summary types for the CPRS GUI Reports tab.</u>](#configure-two-new-health-summary-types-for-the-cprs-gui-reports-tab.)
9.  [<u>Assign the new TIU and PXRM menu options to CAC(s) responsible for managing HT</u> <u>Clinical Reminders.</u>](#assign-the-tiu-ht-menu-and-optional-pxrm-ht-definition-edit-to-cacs.)
10. [<u>After testing all templates (the nine reminder dialogs \[step \#3\] and the two TXML templates</u> <u>\[step \#2\]), link them to note titles</u>](#link-the-ht-templates-to-note-titles-after-making-sure-that-the-nine-reminder-dialogs-and-two-txml-templates-are-tested-and-ready-to-go.).
11. (optional) [<u>Change the frequency of the HT PERIODIC EVALUATION reminder</u>](#_bookmark34) if you wish to have a value other than the exported 180 days,
12. [<u>Build the five reminder report templates and do a sample run of each with a short date</u> range.](#build-the-5-reminder-report-templates-and-do-sample-runs-of-each-with-a-short-date-range.)

#### After completing the above steps, we recommend the following:

- Preview the HOME TELEHEALTH SCREENING dialog to ensure that the two data objects are working without any errors.
- Review what your site does for the consult order to HT/Home Telehealth.
  - PILOT SITES ONLY – Re-pointing of HEALTH FACTORS and/or EDUCATION TOPICS: All pilot sites will need to check to see if they need to go through a process with FileMan to replace the “CCHT” health factor and/or education topics entries in the associated files with the corresponding “HT” entries. See [Appendix A “File Entry Delete and Pointer Update”](#_bookmark41) for detailed explanation and steps. This same process/issue is applicable for the five new EDUCATION TOPICS included in the bundle. The post-install will handle any HT renaming as

> long as the topics are installed at a low Internal Entry Number (IEN). If the IEN is high, the same manual re-pointing will need to occur.

> “Low” and “high” refer to the number range associated with a given health factor. Each health factor in the file has an associated IEN. If the IEN is less than 100,000 this is considered “low” and is reserved for nationally released health factors. IENs greater than 100,000 are considered “high” and are health factors that have been created locally by the facility.

> <span id="_bookmark22" class="anchor"></span>Setup Instructions – Detailed Steps

#### Create a new user class in for your HT clinicians.

> If your site wishes to restrict certain aspects of TIU usage or implement specific business rules pertaining to HT, then a new user class may be created for this purpose.

> NOTE: your site may already have a user class called “HT NURSE” (for Home Telehealth Nurse), or HT NURSE, or HT CLINICIAN, or HT STAFF, because of an earlier Home Telehealth project called VistA Integration for Home Telehealth..

> ![](pxrm-2-19-home-telehealth-install-and-setup-guide/002.png) The documentation for that project (Home Telehealth Technical Installation Guide) is on the VDL (VistA Documentation Library) at [<u>http://www4.va.gov/vdl/application.asp?appid=154</u>](http://www4.va.gov/vdl/application.asp?appid=154) and the specific page that refers to user class is section \#12 on page 14 of the Home Telehealth Technical Install Guide.

#### Edit your “CCHT TEMPLATES” folder in SHARED TEMPLATES to be HT TEMPLATES.

> Use your site’s naming conventions, and locate this folder according to your site’s conventions and where your HT clinicians will find it.

![](pxrm-2-19-home-telehealth-install-and-setup-guide/003.png)

1.  <span id="_bookmark26" class="anchor"></span>Expand the HT_TXML_TEMPLATES.ZIP file to a known location. From that location, import the two .txml files into the CPRS GUI Template Editor, into your PERSONAL templates.
    1.  HT MONTHLY MONITOR.TXML
    2.  HT PROVIDER CONSULT.TXML

#### Create GUI dialogs for the HT reminder dialogs in the DOCUMENT TITLES drawer and follow the instructions for linking the dialogs to the correct note titles

- First, ensure that the TIU TEMPLATE REMINDER DIALOG parameter is set at the SYSTEM level for the HT reminder dialogs template. PXRM\*2.0\*19 tries to do this automatically during installation, but sometimes manual intervention is necessary.
  - Reminder Managers Menu \[PXRM MANAGER\]
    - CPRS Reminder Configuration
      - TIU Template Reminder Dialog Parameter
      - Choose System and enter a ? at the Select Display Sequence prompt. This will show a list of all reminder dialogs that can be used as templates in CPRS GUI.
      - Ensure all HT reminder dialogs are in this list. If not, add them.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 2%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>1</th>
<th colspan="3"><blockquote>
<p>User</p>
</blockquote></th>
<th>USR</th>
<th>[choose</th>
<th><blockquote>
<p>from</p>
</blockquote></th>
<th><blockquote>
<p>NEW PERSON]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td colspan="3"><blockquote>
<p>Team (OE/RR)</p>
</blockquote></td>
<td>OTL</td>
<td>[choose</td>
<td><blockquote>
<p>from</p>
</blockquote></td>
<td><blockquote>
<p>OE/RR LIST]</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td colspan="3"><blockquote>
<p>Service</p>
</blockquote></td>
<td>SRV</td>
<td>[choose</td>
<td><blockquote>
<p>from</p>
</blockquote></td>
<td><blockquote>
<p>SERVICE/SECTION]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td colspan="3"><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td>[choose</td>
<td><blockquote>
<p>from</p>
</blockquote></td>
<td><blockquote>
<p>INSTITUTION]</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="8"><blockquote>
<p>5 System SYS [DVF.FO-SLC.MED.VA.GOV] Enter selection: 5 System DVF.FO-SLC.MED.VA.GOV</p>
<p>Setting Reminder Dialogs allowed as Templates for System: ABC.SYSTEM.MED.VA.GOV Select Display Sequence: ?</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Display Sequence</p>
</blockquote></td>
<td></td>
<td>Value</td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>51</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>ASSESSMENT TREATMENT PLAN TEMPLATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>52</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>CAREGIVER ASSESSMENT TEMPLATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>53</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>CONTINUUM OF CARE TEMPLATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>54</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>DISCHARGE TEMPLATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>55</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>INTERVENTION TEMPLATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>56</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>PERIODIC EVALUATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>57</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>SCREENING CONSULT TEMPLATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>58</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>TECH EDUCATION &amp; INSTALLATION TEMPLATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>59</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>60</p>
</blockquote></td>
<td></td>
<td>VA-HT</td>
<td colspan="4"><blockquote>
<p>VIDEO VISIT TEMPLATE</p>
</blockquote></td>
</tr>
</tbody>
</table>

- Next, go to DOCUMENT TITLES in the CPRS GUI Template Editor.
- Create a new HT TITLES folder in the DOCUMENT TITLES drawer.
- One at a time, create a NEW TEMPLATE for each of these templates in the HT TITLES folder:

> HT ASSESSMENT TREATMENT PLAN template HT CAREGIVER ASSESSMENT template

> HT CONTINUUM OF CARE template HT DISCHARGE template

> HT INTERVENTION template

> HT PERIODIC EVALUATION template

> HT SCREENING CONSULT template HT TECH EDUCATION template

> HT VIDEO VISIT template

- To link a reminder template to a note title, select the template from the ‘reminder dialog’ picklist, and then select the note title in the ‘associated title’ field. This example is shown using the HT Caregiver Assessment.

> ![](pxrm-2-19-home-telehealth-install-and-setup-guide/004.png)

- When you click the APPLY button, the template name will change to upper-case and take on the name of the note title:

![](pxrm-2-19-home-telehealth-install-and-setup-guide/005.png)

> The HT templates all have the same name as the note title. The CPRS GUI template link uses the

> .01-NAME field in the ‘associated title’ field

> When done, your list of linked templates to note titles should look like this (9 reminder dialog templates and 1 text template):

> ![](pxrm-2-19-home-telehealth-install-and-setup-guide/006.png)

<table>
<colgroup>
<col style="width: 70%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>TITLE (.01 NAME)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HAS TEMPLATE</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT ASSESSMENT TREATMENT PLAN NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER ASSESSMENT NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CONTINUUM OF CARE NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT INTERVENTION NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT NOTE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PERIODIC EVALUATION NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT SCREENING CONSULT</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT SUMMARY OF EPISODE NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (TXML)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TECH EDUCATION NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TELEPHONE CASE MANAGEMENT NOTE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VIDEO VISIT NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> RD = Reminder Dialog

2.  <span id="_bookmark28" class="anchor"></span>Verify that the four new HT clinical reminders launch (reminder dialogs linked) from the Reminders drawer. (They will be in the “All Evaluated” folder, no matter what the status is of each reminder for a patient.) You may choose to either add the four reminders for yourself at the User level or, you could add yourself to the user class referenced in step \#1 and then turn on the reminders for the member of that user class.

> Do not add the VA-HT CONTINUUM OF CARE (INITIAL) to any level for now. Additional logic will be added to this reminder and sent in an PXRM update later.

#### Turning on the four new HT Clinical Reminders for users:

> Click the alarm clock or "?" in the CPRS GUI header, then click on ACTION, then “EDIT COVER SHEET REMINDER LIST”:

![](pxrm-2-19-home-telehealth-install-and-setup-guide/007.png)

> When the next window appears, select level = USER CLASS and HT STAFF for the user class, Use the  to move the HT reminders from the LOWER LEFT window (active reminders) to the LOWER RIGHT window so that they are configured for the USER CLASS. Then set the padlock on each one to lock this reminder configuration.

![](pxrm-2-19-home-telehealth-install-and-setup-guide/008.png)

> The four new HT clinical reminders can be found in the “ALL EVALUATED” folder for any patient. Preview each one of them to ensure the reminder dialog loads.

#### Create/edit the consult quick order to HOME TELEHEALTH ENROLLMENT OUTPT:

> Use your site’s naming convention and following VHA Consult Business Rules. OCC recommends creating a HOME TELEHEALTH ENROLLMENT OUTPT sub-service under CARE COORDINATION HOME TELEHEALTH SCREENING\*. If you already have a

> quick order to CARE COORDINATION HOME TELEHEALTH SCREENING, you can review your configuration (others may have to create a new quick order). Reminder: The consult service CARE COORDINATION HOME TELEHEALTH SCREENING

#### cannot be renamed as other VistA software depends on the presence of that exact name.

> QO Enter/edit quick orders

> Select QUICK ORDER NAME: GMRCT HOME TELEHEALTH ENROLLMENT

> Are you adding 'GMRCT HOME TELEHEALTH ENROLLMENT' as a new ORDER DIALOG? No// Y (Yes)

> TYPE OF QUICK ORDER: CONSULTS

> NAME: GMRCT HOME TELEHEALTH ENROLLMENT Replace

> DISPLAY TEXT: Home Telehealth Enrollment Consult

> VERIFY ORDER: y YES DESCRIPTION:

> No existing text Edit? NO//\<ENTER\>

> Consult to Service/Specialty: HOME TELEHEALTH ENROLLMENT OUTPT

> Consult Type:

> Reason for Request:

> Initial Screening for Home Telehealth services. Edit? No// y (Yes)

> ==\[ WRAP \]==\[ INSERT \]=========\< Reason for Request \>========\[ \<PF1\>H=Help \]==

> \<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>====

> Category:

> Urgency: ROUTINE//

> Place of Consultation: CONSULTANT'S CHOICE Attention:

> Provisional Diagnosis:

> Consult to Service/Specialty: HOME TELEHEALTH ENROLLMENT OUTPT

> Urgency: ROUTINE

> Place of Consultation: Consultant's Choice

> (P)lace, (E)dit, or (C)ancel this quick order? PLACE// Auto-accept this order? NO//

> \*Set CARE COORDINATION HOME TELEHEALTH SCREENING service’s Service

> Usage to Grouper Only and then create the HOME TELEHEALTH ENROLLMENT OUTPT service as a sub-service of CARE COORDINATION HOME TELEHEALTH SCREENING. Reference the Consult/Request Tracking User Manual if you need explicit instructions for editing/creating consult services. [(http://www.va](http://www.va.gov/vdl)).[gov/vdl)](http://www.va.gov/vdl))

#### Linking the consult request template to the HOME TELEHEALTH ENROLLMENT OUTPT consult service

- Go into the GUI Template Editor to EDIT Shared Templates, and select the CONSULTS drawer:

![](pxrm-2-19-home-telehealth-install-and-setup-guide/009.png)

- Copy the HT PROVIDER CONSULT GUI dialog template imported in Step \#3 into the CONSULT REASONS FOR REQUEST folder. LINK the HT consult service to the template in the 'associated consult service' field. Click APPLY and note that the GUI dialog template name will change to match that of the associated consult service.

![](pxrm-2-19-home-telehealth-install-and-setup-guide/010.png)![](pxrm-2-19-home-telehealth-install-and-setup-guide/011.png)

- Make sure that this consult quick order is on an order menu for your ordering providers when you are ready to begin the pilot. Launch this quick order from a menu as a verification step, so that you are assured that the template loads and the order is working.

#### Configure two new Health Summary types for the CPRS GUI Reports tab.

- Follow your facility’s rules and conventions for configuring these health summary types.
- Sequencing new Health Summary types is done in the GUI Parameters option.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 23%" />
<col style="width: 18%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>2</p>
</blockquote></th>
<th><blockquote>
<p>User</p>
</blockquote></th>
<th>USR</th>
<th>[choose from NEW PERSON]</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
<td>[PUGET-SOUND.MED.VA.GOV]</td>
</tr>
</tbody>
</table>

#### Assign the TIU HT MENU and (optional) PXRM HT DEFINITION EDIT to CAC(s).

- Use Menu Management options to assign TIU HT MENU to the CAC(s) responsible for managing Home Telehealth Documents and/or Clinical Reminders. Depending on your facility’s IT support structure, this may be handled at a facility level or by Regional IT support.

#### Link the HT templates to NOTE TITLES (after making sure that the nine reminder dialogs and two TXML templates are tested and ready to go).

- Go to DOCUMENT TITLES in the CPRS GUI Template Editor.
- Create a new HT TITLES folder in the DOCUMENT TITLES drawer.
- One at a time, create a NEW TEMPLATE for each of these templates in the HT TITLES folder:

> HT ASSESSMENT TREATMENT PLAN template HT CAREGIVER ASSESSMENT template

> HT CONTINUUM OF CARE template HT DISCHARGE template

> HT INTERVENTION template

> HT PERIODIC EVALUATION template

> HT SCREENING CONSULT template

> HT TECH EDUCATION template HT VIDEO VISIT template

- To link a reminder template to a note title, select the template from the ‘reminder dialog’ picklist, and then select the note title in the ‘associated title’ field. This example is shown using the HT Caregiver Assessment.

![](pxrm-2-19-home-telehealth-install-and-setup-guide/012.png)

- When you click the APPLY button, the template name will change to upper-case and take on the name of the note title:

![](pxrm-2-19-home-telehealth-install-and-setup-guide/013.png)

> The HT templates all have the same name as the note title. The CPRS GUI template link uses the

> .01-NAME field in the ‘associated title’ field

> When done, your list of linked templates to note titles should look like this (9 reminder dialog templates and 1 text template):

> ![](pxrm-2-19-home-telehealth-install-and-setup-guide/014.png)

<table>
<colgroup>
<col style="width: 70%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>TITLE (.01 NAME)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HAS TEMPLATE</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT ASSESSMENT TREATMENT PLAN NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER ASSESSMENT NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CONTINUUM OF CARE NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT INTERVENTION NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT NOTE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PERIODIC EVALUATION NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT SCREENING CONSULT</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT SUMMARY OF EPISODE NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (TXML)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TECH EDUCATION NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TELEPHONE CASE MANAGEMENT NOTE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VIDEO VISIT NOTE</p>
</blockquote></td>
<td><blockquote>
<p>YES (RD)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> RD = Reminder Dialog

3.  <span id="_bookmark34" class="anchor"></span>(Optional for all sites) If you need to change the FREQUENCY of the HT PERIODIC EVALUATION. (This example uses 180 days – set the frequency to whatever time period is needed at your site.)

#### Build the 5 reminder report templates and do sample runs of each, with a short date range.

> [<u>HT CCF INITIAL</u>](#a.-example-creating-the-ht-ccf-initial-reminder-report-template)

> [<u>HT CCF FOLLOW-UP</u>](#b.-example-creating-the-ht-ccf-follow-up-reminder-report-template) [<u>HT C/G ASSESSMENT</u>](#c.-example-creating-the-ht-caregiver-assessment-reminder-report-template)

> [<u>HT PERIODIC EVALUATION</u>](#d.-example-creating-the-ht-periodic-evaluation-reminder-report-template)

> <u>CREATING THE NEW HT CATEGORY (this should be done first, before</u> <u>starting to build the 5 report templates)</u> (used in the (5) REMINDERS SUMMARY’)

> [<u>HT (4) REMINDERS SUMMARY</u>](#f-example-creating-the-reminder-report-template-that-is-a)

#### 11a. Example: CREATING THE HT CCF INITIAL reminder report template

> Select one of the following:

> HA All Outpatient Locations

> HAI All Inpatient Locations

> HS Selected Hospital Locations

> CA All Clinic Stops(with encounters) CS Selected Clinic Stops

> GS Selected Clinic Groups

> Determine encounter counts for: HS// CS Selected Clinic Stops

> Select CLINIC STOP: 179 HOME TELEVIDEO CARE

> Select another CLINIC STOP: 371 HT SCREENING

> Select another CLINIC STOP: 683 HT NON-VIDEO MONITORING Select another CLINIC STOP: 684 HT NON-VIDEO INTRVNTION Select another CLINIC STOP: 685 CARE OF HT PROGRAM PATIENTS Select another CLINIC STOP: 686 PHONE CONTACT BY CC STAFF

> Select another CLINIC STOP:

> Select one of the following:

> P Previous Encounters

> F Future Appointments

> PREVIOUS ENCOUNTERS OR FUTURE APPOINTMENTS: P// Previous Encounters

> Enter ENCOUNTER BEGINNING DATE: T-30 (MAY 31, 2009) Enter ENCOUNTER ENDING DATE: T (JUN 30, 2009)

> Enter EFFECTIVE DUE DATE: Jun 30, 2009// (JUN 30, 2009)

> Select SERVICE CATEGORIES: A,I// ?

> The possible service categories for the report are: A AMBULATORY

8.  HOSPITALIZATION
9.  IN HOSPITAL

> C CHART REVIEW

> T TELECOMMUNICATIONS

> N NOT FOUND

> S DAY SURGERY

> O OBSERVATION

> E EVENT (HISTORICAL)

> R NURSING HOME

> D DAILY HOSPITALIZATION DATA

> X ANCILLARY PACKAGE DAILY DATA

> Select SERVICE CATEGORIES: A,I// A,H,I,T,E,R

> Select one of the following:

> D Detailed

> S Summary

> TYPE OF REPORT: S// Detailed

> Combined report for all Clinic Stops : N// YES

> Display All Future Appointments: N// O

> Sort by Next Appointment date: N// O

> Print full SSN: N// O

#### 11b. Example: CREATING THE HT CCF FOLLOW-UP reminder report template

> Select Reminder Reports Option: Reminders Due Report Select an existing REPORT TEMPLATE or return to continue:

> Select one of the following:

> I Individual Patient

> R Reminder Patient List

> L Location

15. OE/RR Team
16. PCMM Provider

> T PCMM Team

> PATIENT SAMPLE: L// l Location Select FACILITY: Boise, ID 531

> Select another FACILITY: BOISE-RO ID 347

> Select another FACILITY:

> Combined report for all Facilities : N// YES Select one of the following:

> HA All Outpatient Locations

> HAI All Inpatient Locations

> HS Selected Hospital Locations

> CA All Clinic Stops(with encounters) CS Selected Clinic Stops

> GS Selected Clinic Groups

> Determine encounter counts for: HS// CS Selected Clinic Stops

> Select CLINIC STOP: 179 HOME TELEVIDEO CARE

> Select another CLINIC STOP: 371 HT SCREENING

> Select another CLINIC STOP: 683 HT NON-VIDEO MONITORING Select another CLINIC STOP: 684 HT NON-VIDEO INTRVNTION Select another CLINIC STOP: 685 CARE OF HT PROGRAM PATIENTS Select another CLINIC STOP: 686 PHONE CONTACT BY CC STAFF

> Select another CLINIC STOP:

> Select one of the following:

> P Previous Encounters

> F Future Appointments

> PREVIOUS ENCOUNTERS OR FUTURE APPOINTMENTS: P// Previous Encounters

> Enter ENCOUNTER BEGINNING DATE: T-30 (MAY 31, 2009) Enter ENCOUNTER ENDING DATE: T (JUN 30, 2009)

> Enter EFFECTIVE DUE DATE: Jun 30, 2009// (JUN 30, 2009)

> Select SERVICE CATEGORIES: A,I// A,H,I,T,E,R

> Select one of the following: D Detailed

> S Summary

> TYPE OF REPORT: S// Detailed

> Combined report for all Clinic Stops : N// YES Display All Future Appointments: N// O

> Sort by Next Appointment date: N// O Print full SSN: N// O

> Print locations with no patients? YES// NO

> Select individual REMINDER: HT CONTINUUM OF CARE (FOLLOW-UP) VISN

> Create a new report template: N// YES

#### 11c. Example: CREATING THE HT CAREGIVER ASSESSMENT reminder report template

> TYPE OF REPORT: S// Detailed

> Combined report for all Clinic Stops : N// YES Display All Future Appointments: N// O

> Sort by Next Appointment date: N// O Print full SSN: N// O

> Print locations with no patients? YES// NO

> Select individual REMINDER: HT CAREGIVER ASSESSMENT VISN

> Create a new report template: N// YES

> STORE REPORT LOGIC IN TEMPLATE NAME: HT CAREGIVER ASSESSMENT

> Are you adding 'HT CAREGIVER ASSESSMENT' as

> a new REMINDER REPORT TEMPLATE (the 202ND)? No// Y (Yes)

> REMINDER REPORT TEMPLATE REPORT TITLE: HT Caregiver Assessment Changes to template 'HT CAREGIVER ASSESSMENT' have been saved

> Print delimited output only: N// O

> Include deceased patients on the list? N// O Include test patients on the list? N// O Save due patients to a patient list: N// O DEVICE: HOME// ;80;9999 HOME (CRT)

> Building Hospital Locations List Done

> Elapsed time for building hospital locations: 0 secs Building patient listDone

> Elapsed time for building patient list: 0 secs

> Calling the scheduling package to gather appointment data \| Elapsed time for call to the Scheduling Package: 0 secs Sorting SDAMA301 Output Done

> Elapsed time for sorting SDAMA301 output: 0 secs

> Elapsed time for removing invalid encounter(s): 0 secDone Elapsed time for reminder evaluation: 0 secs done

#### 11d. Example: CREATING THE HT PERIODIC EVALUATION reminder report template

> Select SERVICE CATEGORIES: A,I// A,H,I,T,E,R

> Select one of the following: D Detailed

> S Summary

> TYPE OF REPORT: S// Detailed

> Combined report for all Clinic Stops : N// YES Display All Future Appointments: N// O

> Sort by Next Appointment date: N// O Print full SSN: N// O

> Print locations with no patients? YES// NO

> Select individual REMINDER: HT PERIODIC EVALUATION VISN Create a new report template: N// YES

> STORE REPORT LOGIC IN TEMPLATE NAME: HT PERIODIC EVALUATION

> Are you adding 'HT PERIODIC EVALUATION' as

> a new REMINDER REPORT TEMPLATE (the 204TH)? No// Y (Yes) REMINDER REPORT TEMPLATE REPORT TITLE: HT Periodic Evaluation

> Changes to template 'HT PERIODIC EVALUATION' have been saved

> Print delimited output only: N// O

> Include deceased patients on the list? N// O Include test patients on the list? N// O Save due patients to a patient list: N// O DEVICE: HOME// ;80;9999 HOME (CRT)

> Building Hospital Locations List Done

> Elapsed time for building hospital locations: 0 secs Building patient listDone

> Elapsed time for building patient list: 0 secs

> Calling the scheduling package to gather appointment data \| Elapsed time for call to the Scheduling Package: 0 secs Sorting SDAMA301 Output Done

> Elapsed time for sorting SDAMA301 output: 0 secs

> Elapsed time for removing invalid encounter(s): 0 secDone Elapsed time for reminder evaluation: 0 secs done

> Jun 30, 2009 6:23:48 pm Page 1

> Clinical Reminders Due Report - Detailed Report Report Title: HT Periodic Evaluation

> Patient Sample: Location

> Location: Selected Clinic Stops (Prior Encounters) HOME TELEVIDEO CARE 179

> HT NON-VIDEO MONITORING 683 HT NON-VIDEO INTRVNTION 684 HT SCREENING 371

> CARE OF HT PROGRAM PATIENTS 685 PHONE CONTACT BY CC STAFF 686

> Reminder: HT PERIODIC EVALUATION

> Appointments: Next Appointment only

> Date Range: 5/31/2009 to 6/30/2009 Effective Due Date: 6/30/2009

> Date run: 6/30/2009 6:22:43 pm Template Name: HT PERIODIC EVALUATION

> Combined report: Combined Facility and Combined Locations Service categories: A,H,I,T,E,R

> A - AMBULATORY

> H - HOSPITALIZATION I - IN HOSPITAL

> T - TELECOMMUNICATIONS E - EVENT (HISTORICAL)

#### 11e. Example CREATING THE NEW HT CATEGORY - 4 HT CLINICAL REMINDERS

> Select Reminder Managers Menu Option: cp CPRS Reminder Configuration Select CPRS Reminder Configuration Option: ?

> CA Add/Edit Reminder Categories CL CPRS Lookup Categories

> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active PN Progress Note Headers

> RA Reminder GUI Resolution Active

> TIU TIU Template Reminder Dialog Parameter DL Default Outside Location

> PT Position Reminder Text at Cursor NP New Reminder Parameters

> GEC GEC Status Check Active WH WH Print Now Active

> Select CPRS Reminder Configuration Option: CA Add/Edit Reminder Categories

> Selection List Jun 30, 2009@19:02:05 Page: 1 of 1

> Reminder Categories Item Reminder Category

1.  CHRONIC DISEASE
2.  DEPRESSION

> 11 VISN PC MEASURES FY09

> \+ Next Screen - Prev Screen ?? More Actions \>\>\> AD Add PT List/Print All QU Quit

> Select Item: Quit// AD Add

> Select new REMINDER CATEGORY name: HT

> Are you adding 'HT2' as a new REMINDER CATEGORY (the 12TH)? No// y (Yes)

> NAME: HT// DESCRIPTION:

> No existing text Edit? NO// y YES

> ==\[ WRAP \]==\[ INSERT \]=============\< DESCRIPTION \>===========\[ \<PF1\>H=Help \]====

> 4 HT (Home Telehealth) reminders

> \<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

> Select INDIVIDUAL REMINDERS: HT CONTINUUM OF CARE (INITIAL) VISN

> Are you adding 'HT CONTINUUM OF CARE (INITIAL)' as

> a new INDIVIDUAL REMINDERS (the 1ST for this REMINDER CATEGORY)? No// Y (Yes) DISPLAY ORDER: 1

> Select INDIVIDUAL REMINDERS: HT CONTINUUM OF CARE (FOLLOW-UP) VISN Are you adding 'HT CONTINUUM OF CARE (FOLLOW-UP)' as

> a new INDIVIDUAL REMINDERS (the 2ND for this REMINDER CATEGORY)? No// Y (Yes) DISPLAY ORDER: 2

> Select INDIVIDUAL REMINDERS: HT CAREGIVER ASSESSMENT VISN

> Are you adding 'HT CAREGIVER ASSESSMENT' as

> a new INDIVIDUAL REMINDERS (the 3RD for this REMINDER CATEGORY)? No// Y (Yes) DISPLAY ORDER: 3

> Select INDIVIDUAL REMINDERS: HT CAREGIVER/VETERAN REFERRAL VISN Select INDIVIDUAL REMINDERS: HT PERIODIC EVALUATION VISN

#### 11f: Example: CREATING THE REMINDER REPORT TEMPLATE THAT IS A

> SUMMARY REPORT OF THE (4) HT REMINDERS (Here’s where you use the HT ‘category’)

> Select

> Reminder Reports \<PUG TST\> Option: d Reminders Due Report

> Select an existing REPORT TEMPLATE or return to continue: Select one of the following:

> I Individual Patient

> R Reminder Patient List

> L Location

15. OE/RR Team
16. PCMM Provider

> T PCMM Team

> PATIENT SAMPLE: L// l Location

> Select FACILITY: PUGET SOUND HCS/

> Select another FACILITY:

> Select one of the following:

> HA All Outpatient Locations

> HAI All Inpatient Locations

> HS Selected Hospital Locations

> CA All Clinic Stops(with encounters) CS Selected Clinic Stops

> GS Selected Clinic Groups

> Determine encounter counts for: HS// \<ENT\> LOCATION: HT NON VIDEO INTERVENTION

> Select another LOCATION: \<Enter all your HT clinic locations until done\>\>

> Select one of the following:

> P Previous Encounters

> F Future Appointments

> PREVIOUS ENCOUNTERS OR FUTURE APPOINTMENTS: P// revious Encounters

> Enter ENCOUNTER BEGINNING DATE: 3/1/10 (MAR 01, 2010) Enter ENCOUNTER ENDING DATE: 3/5/10 (MAR 05, 2010)

> Enter EFFECTIVE DUE DATE: May 24, 2010// (MAY 24, 2010)

> Select SERVICE CATEGORIES: A,I//

> Select one of the following: D Detailed

> S Summary

> TYPE OF REPORT: S// ummary

> Print locations with no patients? YES// n NO

> Print percentages with the report output? NO// y YES Select a REMINDER CATEGORY: HT

> ...OK? Yes// (Yes)

> Select another REMINDER CATEGORY: \<ENT\> Select individual REMINDER: \<ENT\>

> Create a new report template: N// y YES

> STORE REPORT LOGIC IN TEMPLATE NAME: HT (4) REMINDERS,SUMMARY

> Are you adding 'HT (4) REMINDERS,SUMMARY' as

> a new REMINDER REPORT TEMPLATE (the 235TH)? No// Y (Yes)

#### 11g. Example: GRANT ACCESS TO THE REMINDER REPORT TEMPLATES TO YOURSELF AND YOUR HT SITE LEAD

> 11h. Example: RUNNING THE REMINDER REPORT TEMPLATES

> <span id="_bookmark41" class="anchor"></span><u>Appendix A: File Entry Delete and Pointer Update</u>

> OVERVIEW

> This procedure is only *potentially* necessary at sites that participated in the CCHT pilot program.

> The following is an example of how to delete a HEALTH FACTORS file entry and then update any pointers to a new entry. This same procedure can be used to delete and update any local EDUCATION TOPICS file entries.

> If you are a CCHT pilot site, you can determine the need to follow this procedure by examining the entries in the HEALTH FACTORS and EDUCATION TOPICS files. PXRM\*2.0\*19 exports entries to both of those files. Internal Entry Numbers (IENs) less than 100,000 in these files are intended for National entries. During installation, if the “CCHT” health factors and “HOME TELEHEALTH” education topics are found at IENs \< 100,000, the patch will rename these entries to “HT…” for health factors and “VA-HOME TELEHEALTH…” for education topics. If these entries are found to be at IENs \> 100,000 (i.e. Local), PXRM\*2.0\*19 will install new National entries at low IENs and your site will need to perform the delete/pointer update process below.

#### WARNING! A LOCAL “CCHT” HEALTH FACTOR OR EDUCATION TOPIC SHOULD ONLY BE DELETED AND HAVE POINTERS UPDATED AFTER CONFIRMING THAT THE LOCAL “CCHT” HEALTH FACTOR HAS BEEN SUPERSEDED BY A NATIONAL “HT” HEALTH FACTOR.

> The process described below involves using FileMan to delete entries in a given file, and subsequently updating any other files that pointed to the deleted entry to now point to a new entry. This is a manual process and is not technically possible to be automatically performed as part of a post-install routine.

> EDUCATION TOPICS

> Check to see if the education topics exported in the reminder exchange file have been installed at national IENs and if any local education topics need to be replaced.

> Perform a FileMan search of the EDUCATION TOPICS file. Look for topics that have “HOME TELEHEALTH” in the NAME. Output the NAME and NUMBER. If an education topic has a “VA-“ entry at an IEN of less than 100,000 AND a non “VA-“ entry then that non “VA-“ entry is a candidate for the delete and re-point process.

> Enter or Edit File Entries Print File Entries

> Search File Entries Modify File Attributes Inquire to File Entries Utility Functions ...

> Data Dictionary Utilities ... Transfer Entries

> Other Options ...

> Select VA FileMan \<TEST ACCOUNT\> Option: search File Entries

> OUTPUT FROM WHAT FILE: EDUCATION TOPICS//

> -A- SEARCH FOR EDUCATION TOPICS FIELD: NAME

> -A- CONDITION: CONTAINS

> -A- CONTAINS: HOME TELEHEALTH

> -B- SEARCH FOR EDUCATION TOPICS FIELD:

> IF: A// NAME CONTAINS (case-insensitive) "HOME TELEHEALTH" STORE RESULTS OF SEARCH IN TEMPLATE:

> SORT BY: NAME//

> START WITH NAME: FIRST// FIRST PRINT FIELD: NAME THEN PRINT FIELD: NUMBER THEN PRINT FIELD:

> Heading (S/C): EDUCATION TOPICS SEARCH Replace DEVICE: ;;9999 HOME

> EDUCATION TOPICS SEARCH MAR 20,2013 07:51 PAGE 1 NAME

> NUMBER

> VA-HOME TELEHEALTH (HT) 37

> VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT 19

> VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT 21

> VA-HOME TELEHEALTH-IN HOME MONITORING 18

> VA-HOME TELEHEALTH-MEDICATION MANAGEMENT 20

> In this sample search, only the VA-HOME TELEHEALTH education topics are present. If a search result returned a local entry of HOME TELEHEALTH IN HOME MONITORING at IEN 660124, that entry would be a candidate for being deleted from EDUCATION TOPICS and any pointers should be updated to point to the national entry, VA-HOME TELEHEALTH IN HOME MONITORING. Refer to the document “File Entry Delete and Pointer Update” for details of this process.

> HEALTH FACTORS

> Check to see if the health factors exported in the reminder exchange file have been installed at national IENs and if any local health factors need to be replaced.

> Perform a FileMan search of the HEALTH FACTORS file. Look for health factors that have “HT ” in the FACTOR field. Output the FACTOR and NUMBER. If a health factor has an “HT “ entry at an IEN of less than 100,000 AND a “CCHT “ entry, then that “CCHT ” entry is a candidate for the delete and re-point process.

> Select VA FileMan \<TEST ACCOUNT\> Option: Search File Entries

> OUTPUT FROM WHAT FILE: EDUCATION TOPICS// HEALTH FACTORS

> (3440 entries)

> -A- SEARCH FOR HEALTH FACTORS FIELD: FACTOR

> -A- CONDITION: CONTAINS

> -A- CONTAINS: HT NOTE: type a space after the T

> -B- SEARCH FOR HEALTH FACTORS FIELD:

> IF: A FACTOR CONTAINS (case-insensitive) "HT " STORE RESULTS OF SEARCH IN TEMPLATE:

> SORT BY: FACTOR//

> START WITH FACTOR: FIRST// FIRST PRINT FIELD: FACTOR THEN PRINT FIELD: NUMBER THEN PRINT FIELD:

> Heading (S/C): HEALTH FACTORS SEARCH Replace

> DEVICE: ;;9999 HOME  SUGGEST QUEUEING OUTPUT TO MAILMAN AS SEARCH WILL TAKE A LONG TIME TO COMPLETE

> HEALTH FACTORS SEARCH MAR 20,2013 07:58 PAGE 1 FACTOR NUMBER

<table>
<colgroup>
<col style="width: 79%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>CCHT TEST ONE</th>
<th><blockquote>
<p>660012</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CCHT VETERAN REFERRAL SOCIAL WORK</td>
<td><blockquote>
<p>660014</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HT VETERAN REFERRAL SOCIAL WORK</td>
<td><blockquote>
<p>820</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HT VETERAN REFERRAL SVCS IN PLACE</td>
<td><blockquote>
<p>822</p>
</blockquote></td>
</tr>
<tr class="even">
<td>HT VETERAN REFERRAL TRANSPORTATION</td>
<td><blockquote>
<p>831</p>
</blockquote></td>
</tr>
</tbody>
</table>

> In this sample search, the VETERAN REFERRAL SOCIAL WORK factor has a “CCHT “ entry and an “HT “ entry at IEN less than 100,000. Note that the names are an exact match (excluding “CC”). The “CCHT “ entry would be a candidate for the delete and re-point process with any associated pointers being updated to reference the HT VETERAN REFERRAL SOCIAL WORK entry.

> DELETE AND REPOINT EXAMPLE

> The following is an example of deleting a HEALTH FACTOR file entry and updating the pointers associated with that entry to reference a new HEALTH FACTOR file entry. When a delete/repoint is made, the output will contain a list of files that point to the HEALTH FACTORS (or EDUCATION TOPICS) file. For each file there with either be a listing of the entries that were updated or a “NO RECORDS TO PRINT” message indicating no pointers needed updating.

> VA FileMan Version 22.0

> Enter or Edit File Entries Print File Entries

> Search File Entries Modify File Attributes Inquire to File Entries Utility Functions ...

> Data Dictionary Utilities ... Transfer Entries

> Other Options ...

> Select VA FileMan \<TEST ACCOUNT\> Option: Enter or Edit File Entries

> INPUT TO WHAT FILE: HEALTH FACTORS//

> EDIT WHICH FIELD: ALL//

> Select HEALTH FACTORS: CCHT VETERAN REFERRAL SOCIAL WORK

> FACTOR: CCHT TEST ENTRY// @

> SURE YOU WANT TO DELETE THE ENTIRE 'CCHT TEST ENTRY' HEALTH FACTORS? YES

> (Yes)

> SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO' BY ENTRIES IN THE 'HEALTH SUMMARY TYPE' FILE, ETC.,

> DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// Y

> (Yes)

> WHICH DO YOU WANT TO DO? --

1)  DELETE ALL SUCH POINTERS
2)  CHANGE ALL SUCH POINTERS TO POINT TO A DIFFERENT 'HEALTH FACTORS' ENTRY

> CHOOSE 1) OR 2): 2

> THEN PLEASE INDICATE WHICH ENTRY SHOULD BE POINTED TO Select HEALTH FACTORS: HT VETERAN REFERRAL SOCIAL WORK

> (RE-POINTING WILL OCCUR WHEN YOU LEAVE 'ENTER/EDIT' OPTION)

> Select HEALTH FACTORS:

> ...EXCUSE ME, JUST A MOMENT PLEASE... DEVICE: HOME// ;;9999 HOME

> HEALTH SUMMARY TYPE entries whose 'SELECTION ITEM' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> REMINDER DIALOG entries whose 'FINDING ITEM' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> REMINDER DIALOG entries whose 'ADDITIONAL FINDINGS' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> REMINDER FINDING ITEM PARAMETER entries whose 'FINDING ITEM' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> HEALTH FACTOR RESOLUTION entries whose 'NAME' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> REMINDER EXTRACT SUMMARY entries whose 'FINDING ITEM' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> REMINDER EXTRACT SUMMARY entries whose 'FINDING ITEM' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> REMINDER TERM entries whose 'FINDING ITEM' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

REMINDER DEFINITION entries whose 'FINDING ITEM' pointers have been changed

MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> NUPA PCE INFO entries whose 'HAD HEALTH FACTOR' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> NUPA PCE INFO entries whose 'RECEIVED PREV HEALTH FACTOR' pointers have been cha nged

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> NUPA PCE INFO entries whose 'DECLINED HEALTH FACTOR' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> NUPA PCE INFO entries whose 'N/A HEALTH FACTOR' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> V HEALTH FACTORS entries whose 'HEALTH FACTOR' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> 660204 CRPATIENT,TWO NOV 8,2011@08:00

> HEALTH FACTORS entries whose 'CATEGORY' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> HEALTH FACTORS entries whose 'NOT USED WITH' pointers have been changed

> MAR 19,2013 10:04 PAGE 1

> \*\*\* NO RECORDS TO PRINT \*\*\*

> Enter or Edit File Entries Print File Entries

> Search File Entries Modify File Attributes Inquire to File Entries Utility Functions ...

> Data Dictionary Utilities ... Transfer Entries

> Other Options ...

> <span id="_bookmark43" class="anchor"></span>Appendix B: Crosswalk from CCHT Pilot to National <u>Release </u>

> This is a table is intended to help sites know what data is being installed into their systems and also assist with any local decisions to inactivate unused/unwanted health factors. The table shows a comparison between the health factors distributed in the VA-HT PROJECT reminder exchange file (installed by PXRM\*2.0\*19) to corresponding entries from the CCHT Phase 3 Pilot Program.

> The HT TEMPLATES 1.0 column is the authoritative list of health factors being used by the Home Telehealth clinical reminders content. Health factor category names appear in bold text. If the only difference between two health factor names is “HT” vs. “CCHT”, those items will appear on the same row. Such as:

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>HT TEMPLATES 1.0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PILOT PHASE 3</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL BEREAVE SUPPORT</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL BEREAVE SUPPORT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> New health factors will not have an equivalent Pilot entry.

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>HT TEMPLATES 1.0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PILOT PHASE 3</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CATEGORY OF CARE-ACUTE CARE</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Pilot health factors no longer used in the HT Templates will not have an equivalent HT entry.

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>HT TEMPLATES 1.0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PILOT PHASE 3</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 0</p>
</blockquote></td>
</tr>
</tbody>
</table>

> There are 271 new HT-specific health factors included in the VA-HT PROJECT reminder exchange file. The “GEC” health factors being exported are VA national, already exist at VA sites, and are not included in this table.

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>HT TEMPLATES 1.0</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>PILOT PHASE 3</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>CCHT (CARE COORDINATION HOME TELEHEALTH)</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT (HOME TELEHEALTH)</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT APPROX DELIVERY DATE FOR EQUIPMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT ASSESSMENT TX PLAN TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT ASSESSMENT/TREATMENT PLAN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>CCHT ASSESSMENT/TREATMENT PLAN</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT BARRIERS TO LEARNING</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT BATHING HELP/SUPRVISION LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT BATHING HELP/SUPRVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT BATHING HELP/SUPRVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT BATHING HELP/SUPRVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT BED MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT BED MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT BED MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT BED MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT C/G RISK ASSESSMENT DIALOG USED</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT C/G RISK SCREEN TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER ASSESSMENT SCREEN DONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER ASSESSMENT TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>HT CAREGIVER ASSESSMENT SCREEN COMPLETED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL BEREAVE SUPPORT</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL BEREAVE SUPPORT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL C/G SUPPORT GRP</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL C/G SUPPORT GRP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL EDUC/TRAINING</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL EDUC/TRAINING</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL FAMILY COUNSEL</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL FAMILY COUNSEL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL INDIVID COUNSEL</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL INDIVID COUNSEL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL MEDICAL EVAL,F/U</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL MEDICAL EVAL,F/U</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL OTHER SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL OTHER SERVICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL SVCS IN PLACE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL SVCS IN PLACE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 10</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 11</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 12</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 13</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 14</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 15</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 2</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 3</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 4</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 5</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 7</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCORE 9</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>HT CAREGIVER REVIEW OF WRITTEN MATERIALS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT CAREGIVER RISK ASSESSMENT SCREEN</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>CCHT CAREGIVER RISK ASSESSMENT SCREEN</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER STATES ESSENTIAL CONCEPTS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CATEGORY-ACUTE CARE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CATEGORY-CHRONIC CARE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CATEGORY-HEALTH PROMOTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CATEGORY-NON INSTITUTIONAL CARE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CATEGORY OF CARE-ACUTE CARE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>HT CATEGORY OF CARE-CHRONIC CARE MGMT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CATEGORY OF CARE-HEALTH PROMOTION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CATEGORY OF CARE-NON INSTITUTIONAL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CATEGORY OF CARE-OTHER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CATEGORY-TELEPHONE CASE MANAGEMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF 1 OR MORE BEHAV/COGN PROBLEMS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF 1 OR MORE BEHAV/COGN PROBLEMS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF 12 OR MORE CLINIC STOPS PAST YR</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF 12 OR MORE CLINIC STOPS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF 2 OR MORE ADL DEFICITS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF 2 OR MORE ADL DEFICITS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF AGE 75 OR GREATER</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF AGE 75 OR GREATER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF AGITATED/DISORIENTED-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF AGITATED/DISORIENTED-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF AGITATED/DISORIENTED-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF AGITATED/DISORIENTED-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER ACCESSIBLE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER ACCESSIBLE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER CAN INCREASE HELP</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER CAN INCREASE HELP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER CAN'T INCREASE HELP</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER CAN'T INCREASE HELP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER LIVES WITH PT-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER LIVES WITH PT-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER LIVES WITH PT-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER LIVES WITH PT-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER NOT ACCESSIBLE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER NOT ACCESSIBLE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER SAME NAME AS PT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-ADL HELP</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER-ADL HELP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-CHILD</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER-CHILD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-EMOTIONAL SUPPORT</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER-EMOTIONAL SUPPORT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-FRIEND/NEIGHBOR</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER-FRIEND/NEIGHBOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-IADL HELP</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER-IADL HELP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-OTHER</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER-OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER'S CITY</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER'S CITY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER'S NAME</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER'S NAME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER'S PHONE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER'S PHONE</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT CCF CAREGIVER'S STATE</p>
</blockquote></th>
<th><blockquote>
<p>CCHT CCF CAREGIVER'S STATE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER'S STREET ADDRESS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER'S STREET ADDRESS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER'S ZIP CODE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER'S ZIP CODE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-SPOUSE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF CAREGIVER-SPOUSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF COMPLEXITY TOO GREAT-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF COMPLEXITY TOO GREAT-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF COMPLEXITY TOO GREAT-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF COMPLEXITY TOO GREAT-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DELUSIONS-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF DELUSIONS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DELUSIONS-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF DELUSIONS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF DIFFIC MAKE SELF UNDERSTOOD-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF DIFFIC MAKE SELF UNDERSTOOD-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DIFFIC REASONABLE DECISIONS-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF DIFFIC REASONABLE DECISIONS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DIFFIC REASONABLE DECISIONS-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF DIFFIC REASONABLE DECISIONS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DOES NOT MEET CCM CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF DOES NOT MEET CCM CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DOES NOT MEET NIC CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF DOES NOT MEET NIC CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF FLARE UP CHRONIC CONDITION-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF FLARE UP CHRONIC CONDITION-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF FLARE UP CHRONIC CONDITION-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF FLARE UP CHRONIC CONDITION-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF FOLLOW-UP ASSESSMENT COMPLETED</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF FOLLOW-UP ASSESSMENT DONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF GROUP SETTING NON RELATIVES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF GROUP SETTING NON RELATIVES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-AUDITORY</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF HALLUCINATIONS-AUDITORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-NONE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF HALLUCINATIONS-NONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-OLFACTORY</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF HALLUCINATIONS-OLFACTORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-SENSORY</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF HALLUCINATIONS-SENSORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-TACTILE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF HALLUCINATIONS-TACTILE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-VISUAL</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF HALLUCINATIONS-VISUAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF INITIAL ASSESSMENT COMPLETED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CCF INITIAL ASSESSMENT DONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIFE EXPECTANCY &lt; 6 MO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIFE EXPECTANCY &lt; 6 MO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES ALONE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES ALONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES ALONE IN COMMUNITY</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES ALONE IN COMMUNITY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES AT OTHER</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES AT OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES BOARD AND CARE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES BOARD AND CARE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES DOMICILIARY</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES DOMICILIARY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES HOMELESS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES HOMELESS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES HOMELESS SHELTER</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES HOMELESS SHELTER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES NURSING HOME</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES NURSING HOME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES PRIVATE HOME</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES PRIVATE HOME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES WITH ADULT CHILD</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES WITH ADULT CHILD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES WITH CHILD</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES WITH CHILD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES WITH OTHER</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES WITH OTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES WITH SPOUSE &amp; OTHERS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES WITH SPOUSE &amp; OTHERS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES WITH SPOUSE ONLY</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF LIVES WITH SPOUSE ONLY</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT CCF MEETS CHRONIC CARE MGMT CRITERIA</p>
</blockquote></th>
<th><blockquote>
<p>CCHT CCF MEETS CCM CRITERIA</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CCF MEETS NIC CATEGORY A CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF MEETS NIC CATEGORY A CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF MEETS NIC CATEGORY B CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF MEETS NIC CATEGORY B CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF MEETS NIC CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF MEETS NIC CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF MOOD DISORDER DEPRESSION-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF MOOD DISORDER DEPRESSION-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF MOOD DISORDER DEPRESSION-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF MOOD DISORDER DEPRESSION-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF MOOD DISORDER MANIC-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF MOOD DISORDER MANIC-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF MOOD DISORDER MANIC-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF MOOD DISORDER MANIC-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF NIC CRITERIA NO-ACUTE CARE MGMT</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF NIC CRITERIA NO-ACUTE CARE MGMT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF NIC CRITERIA NO-HLTH PROMOTION</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF NIC CRITERIA NO-HLTH PROMOTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF PHYSICALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF PHYSICALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF PHYSICALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF PHYSICALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF POTENTIAL FOR INCR INDEP-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF POTENTIAL FOR INCR INDEP-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF POTENTIAL FOR INCR INDEP-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF POTENTIAL FOR INCR INDEP-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF PROBLEMS WITH 3 OR MORE ADLS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF PROBLEMS IN 3 OR MORE ADLS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF PROBLEMS WITH 3 OR MORE IADL</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF PROBLEMS WITH 3 OR MORE IADL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF PTSD/OTHER ANXIETY-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF PTSD/OTHER ANXIETY-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF PTSD/OTHER ANXIETY-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF PTSD/OTHER ANXIETY-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF RECOMMEND REFERRAL-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF RECOMMEND REFERRAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF RECOMMEND REFERRAL-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF RECOMMEND REFERRAL-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF RESISTING CARE-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF RESISTING CARE-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF RESISTING CARE-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF RESISTING CARE-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF SERVICES IN PLACE-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF SERVICES IN PLACE-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF SERVICES IN PLACE-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF SERVICES IN PLACE-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF SUBST ABUSE/DEPENDENCE-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF SUBST ABUSE/DEPENDENCE-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF SUBST ABUSE/DEPENDENCE-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF SUBST ABUSE/DEPENDENCE-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF UNPAID CAREGIVER-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF UNPAID CAREGIVER-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF UNPAID CAREGIVER-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF UNPAID CAREGIVER-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF VERBALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF VERBALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF VERBALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF VERBALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF WANDERING-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF WANDERING-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF WANDERING-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CCF WANDERING-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CG/VETERAN REFERRAL COMPLETED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CG/VET REFER DIALOG/TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CG/VETERAN REFERRAL TEMPLATE DONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CG/VETERAN REFERRAL TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CG/VETERAN REFERRAL(S) NOT UTILIZED</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CG/VETERAN REFERRAL(S) NOT UTILIZED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CLINICAL REASON FOR ENROLLMENT</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CLINICAL REASON FOR ENROLLMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CONSULTS/REFERRALS RECOMMENDED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT CONT OF CARE TITLE/TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT CONT OF CARE(EMBEDDED)TEMPLATE USED</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT CONTACT MADE FOR EQUIP RETURN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>CCHT CONTINUUM OF CARE</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT CONTINUUM OF CARE (CCF)</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT MANAGING MEDS/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT MANAGING MEDS/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT MANAGING MEDS/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT MANAGING MEDS/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT MNG FINANCES/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT MNG FINANCES/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT MNG FINANCES/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT MNG FINANCES/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT PREPARE MEALS/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT PREPARE MEALS/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT PREPARE MEALS/LAST 7D-YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT TRANSPORTATION/LAST 7D-NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT TRANSPORTATION/LAST 7D-YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT DIFFICULT TRANSPRTATION/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT DIFFICULT TRANSPRTATION/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT USING PHONE LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT USING PHONE LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT USING PHONE LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT USING PHONE LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT W/ HOUSEWORK/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT W/ HOUSEWORK/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT W/ HOUSEWORK/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT W/ HOUSEWORK/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT WITH SHOPPING/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT WITH SHOPPING/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT WITH SHOPPING/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DIFFICULT WITH SHOPPING/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT DIGITAL CAMERA SERIAL #</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT DISCHARGE</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>CCHT DISCHARGE</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT DISCHARGE TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-ADMITTED TO NURSING HOME</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-ADMITTED TO NURSING HOME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT DISCHARGE-ALL EQUIP RETURNED (NO)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT DISCHARGE-ALL EQUIP RETURNED (YES)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-ALL ISSUES ADDRESSED(NO)</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-ALL ISSUES ADDRESSED(NO)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-ALL ISSUES ADDRESSED(YES)</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-ALL ISSUES ADDRESSED(YES)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT DISCHARGE-EQUIP RETURN (OTHER)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-HAS MET GOALS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-HAS MET GOALS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-NO RESPONSE TO PROGRAM</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-NO RESPONSE TO PROGRAM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-NO VA PRIMARY CARE SVCS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-NO VA PRIMARY CARE SVCS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-OTHER FOLLOW-UP</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-OTHER FOLLOW-UP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-PATIENT IS DECEASED</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-PATIENT IS DECEASED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-PHONE,ELECT SVCS UNAVAIL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-PROLONGED HOSPITALIZATION</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-PROLONGED HOSPITALIZATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-PROVIDER REQUESTS DC</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-PROVIDER REQUESTS DC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-PT/CG REQUEST DC SERVICES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-PT/CG REQUEST DC SERVICES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO HOSPICE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-REFERRED TO HOSPICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO MENTAL HEALTH</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-REFERRED TO MENTAL HEALTH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO NEW LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-REFERRED TO NEW LOCATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO PRIMARY CARE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-REFERRED TO PRIMARY CARE</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT DISCHARGE-REFERRED TO SOCIAL WORK</p>
</blockquote></th>
<th><blockquote>
<p>CCHT DISCHARGE-REFERRED TO SOCIAL WORK</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-RELOCATED OUT OF SVC AREA</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-RELOCATED OUT OF SVC AREA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-UNABLE TO OPERATE DEVICES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISCHARGE-UNABLE TO OPERATE DEVICES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT DISEASE INDICATIONS-CHF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-COPD</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISEASE INDICATIONS-COPD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-DEPRESSION</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISEASE INDICATIONS-DEPRESSION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-DIABETES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISEASE INDICATIONS-DIABETES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-HEART FAILURE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-HYPERTENSION</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISEASE INDICATIONS-HYPERTENSION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-OBESITY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-OTHER</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISEASE INDICATIONS-OTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-PTSD</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DISEASE INDICATIONS-PTSD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-SUBSTANCE ABUSE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT DISEASE INDICATIONS-SUBST ABUSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISINTERESTED/LACKS MOTIVATION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DRESSING HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DRESSING HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DRESSING HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT DRESSING HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EATING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT EATING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EATING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT EATING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT EDUC ON EQUIP-CARE COORDINATOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT EDUC ON EQUIP-CONTRACT VENDOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT EDUC ON EQUIP-SUPPORT STAFF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EMERG PRIORITY HIGH-IMMEDIATE EVAL</p>
</blockquote></td>
<td><blockquote>
<p>CCHT EMERG PRIORITY HIGH-IMMEDIATE EVAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EMERG PRIORITY LOW-HAS RESOURCES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT EMERG PRIORITY LOW-HAS RESOURCES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EMERG PRIORITY MOD-SVCS AFTER 3-7D</p>
</blockquote></td>
<td><blockquote>
<p>CCHT EMERG PRIORITY MOD-SVCS AFTER 3-7D</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT ENROLLMENT-ENDING DATE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT ENROLLMENT-ENDING DATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT ENROLLMENT-START DATE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT ENROLLMENT-START DATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT ENROLLMENT-START DATE (PREV ENROLL)</p>
</blockquote></td>
<td><blockquote>
<p>CCHT ENROLLMENT-START DATE (PREV ENROLL)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EQUIP INSTALLATION MODE-OTHER</p>
</blockquote></td>
<td><blockquote>
<p>CCHT EQUIP INSTALLATION MODE-OTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT EQUIP INSTALLED BY CARE COORDINATOR</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT EQUIP INSTALLED BY CONTRACT VENDOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EQUIP INSTALLED BY SUPPORT STAFF</p>
</blockquote></td>
<td><blockquote>
<p>CCHT EQUIP INSTALLED BY SUPPORT STAFF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EQUIP INSTALLED BY VETERAN/CAREGIVER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT EQUIP INSTALLED BY VETERAN/CAREGVR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT EQUIP MAILED,INSTALL BY VET/CAREGVR</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT EQUIP TAKEN HOME,INSTALL BY VET/CG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT GETS MEDS VIA NON-VA PROVIDER-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT GETS MEDS VIA NON-VA PROVIDER-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT GETS MEDS VIA NON-VA PROVIDER-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT GETS MEDS VIA NON-VA PROVIDER-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT HEALTH EDUCATION PLAN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT HEALTH EDUCATION RESPONSE</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT INDICATIONS-# OUTPT VISITS PAST YR</p>
</blockquote></th>
<th><blockquote>
<p>CCHT INDICATIONS-# OUTPT VISITS PAST YR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT INDICATIONS-DISTANCE (HOURS)</p>
</blockquote></td>
<td><blockquote>
<p>CCHT INDICATIONS-DISTANCE (HOURS)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT INDICATIONS-DISTANCE (MILES)</p>
</blockquote></td>
<td><blockquote>
<p>CCHT INDICATIONS-DISTANCE (MILES)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT INDICATIONS-HX HIGH COST/HIGH USE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT INDICATIONS-HX HIGH COST/HIGH USE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT INDICATIONS-HX HOSPITALIZATONS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT INDICATIONS-HX HOSPITALIZATONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT INTERVENTION TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-ANGRY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-ANXIETY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-APHASIA</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>HT LEARNING BARRIER-COGNITIVE IMPAIRMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-CULTURAL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-HEARING IMPAIRED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-HOMELESS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-IMPAIRED MEMORY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-LANGUAGE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT LEARNING BARRIER-LANGUAGE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-NONE IDENTIFIED</p>
</blockquote></td>
<td><blockquote>
<p>CCHT LEARNING BARRIER-NONE IDENTIFIED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-NOT MOTIVATED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-OVERWHELMED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-PAIN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-PHYSICAL LIMITATIONS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>HT LEARNING BARRIER-POOR CONCENTRATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-UNABLE TO READ</p>
</blockquote></td>
<td><blockquote>
<p>CCHT LEARNING BARRIER-UNABLE TO READ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT LEARNING BARRIER-UNABLE TO WRITE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT LEARNING BARRIER-VISUALLY IMPAIRED</p>
</blockquote></td>
<td><blockquote>
<p>CCHT LEARNING BARRIER-VISUALLY IMPAIRED</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MAKE TIME FOR SELF=FREQUENTLY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MAKE TIME FOR SELF=NEARLY ALWAYS</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MAKE TIME FOR SELF=NEVER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MAKE TIME FOR SELF=RARELY</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MAKE TIME FOR SELF=SOMETIMES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT MEALS PREPARED BY OTHER/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT MEALS PREPARED BY OTHER/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT MEALS PREPARED BY OTHER/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT MEALS PREPARED BY OTHER/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MEASURING DEVICE-OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MEDS ADAPTATIONS-NONE NEEDED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MEDS ADAPTATIONS-OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MEDS ADAPT-FOR VISUAL IMPAIRMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MEDS ADAPT-MEDS ARE COLOR CODED</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MEDS ADAPT-USES PILLBOX</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MEDS ADAPT-VA PREPARES/POURS MEDS</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MEDS SPECIAL ADAPTATIONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT MEETS TELEHEALTH CRITERIA(NO)</p>
</blockquote></td>
<td><blockquote>
<p>CCHT MEETS TELEHEALTH CRITERIA(NO)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT MEETS TELEHEALTH CRITERIA(YES)</p>
</blockquote></td>
<td><blockquote>
<p>CCHT MEETS TELEHEALTH CRITERIA(YES)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT MESSAGING DEVICE TYPE/SERIAL #</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING DEVICE-BLOOD GLUCOSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING DEVICE-BLOOD PRESSURE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING DEVICE-PULSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING DEVICE-PULSE OXIMETRY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING DEVICE-WEIGHT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING/MONITORING TYPE/SERIAL #</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING/MONITORING-BLOOD GLUCOSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING/MONITORING-BLOOD PRESSURE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING/MONITORING-OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING/MONITORING-PULSE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING/MONITORING-PULSE OXIMETRY</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING/MONITORING-SPIROMETRY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT MESSAGING/MONITORING-WEIGHT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT MOVE INDOOR HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT MOVE INDOOR HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT MOVE INDOOR HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT MOVE INDOOR HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>HT NEEDS REINFORCEMENT/REVIEW/FOLLOW-UP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT NO EVIDENCE OF LEARNING</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT NO FOLLOW-UP NEEDED/INDICATED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PERIODIC EVALUATION COMPLETED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PERIODIC EVAL DIALOG/TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PERIODIC EVALUATION DONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PERIPHERALS-BP CUFF (SERIAL #)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PERIPHERALS-GLUCOSE CABLES</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PERIPHERALS-NONE NEEDED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PERIPHERALS-OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PERIPHERALS-PULSE OX (SERIAL #)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PERIPHERALS-SPIROMETRY (SERIAL #)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PERIPHERALS-STETHOSCOPE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PERIPHERALS-WEIGHT SCALE (SERIAL #)</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PHONE-DSL LINE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PHONE-MODEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PHONE-NO FEATURES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PLAN-MED DISCREP SENT TO PROVIDER</p>
</blockquote></td>
<td><blockquote>
<p>CCHT PLAN-MED DISCREP SENT TO PROVIDER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT PLAN-REVIEWED LIST OF CURRENT MEDS</p>
</blockquote></td>
<td><blockquote>
<p>CCHT PLAN-REVIEWED LIST CURRENT MEDS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PREVIOUSLY ENROLLED TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT PT/CG HAS LIST OF ACTIVE MEDS-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT PT/CG HAS LIST OF ACTIVE MEDS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PT/CG HAS LIST OF ACTIVE MEDS-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT PT/CG HAS LIST OF ACTIVE MEDS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT PT/CG HAS QUESTIONS ON MEDS-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT PT/CG HAS QUESTIONS ON MEDS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PT/CG HAS QUESTIONS ON MEDS-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT PT/CG HAS QUESTIONS ON MEDS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PT/CG KNOWS MED INDICATIONS-NO</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT PT/CG KNOWS MED INDICATIONS-YES</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PT/CG KNOWS MED SIDE EFFECTS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PT/CG KNOWS MED SIDE EFF-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PT/CG KNOWS REFILL PROCESS-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PT/CG KNOWS REFILL PROCESS-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT PT/CG TAKES MEDS AS PRESCRIBED-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT PT/CG TAKES MEDS AS PRESCRIBED-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT REASON FOR NON-ENROLLMENT</p>
</blockquote></td>
<td><blockquote>
<p>CCHT REASON FOR NON-ENROLLMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT RECENT CHANGE IN FUNCTION-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT RECENT CHANGE IN FUNCTION-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT RECENT CHANGE IN FUNCTION-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT RECENT CHANGE IN FUNCTION-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REFERRAL-CONSULT COMPLETION</p>
</blockquote></td>
<td><blockquote>
<p>CCHT REFERRAL-CONSULT COMPLETION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT REFERRALS CAREGIVER NOT SATISFIED</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT REFERRALS CAREGIVER SATISFIED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT REFERRALS FOR VETERAN/CAREGIVER</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>CCHT REFERRALS FOR VETERAN/CAREGIVER</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REFERRALS-CAREGIVER NOT SATISFIED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT REFERRALS-CAREGIVER SATISFIED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REPEAT DEMONSTRATION NEXT VISIT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT SCREENING CONSULT TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT STRAINED WITH RELATIVES=FREQUENTLY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT STRAINED WITH RELATIVES=NEVER</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT STRAINED WITH RELATIVES=NRLY ALWAYS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT STRAINED WITH RELATIVES=RARELY</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT STRAINED WITH RELATIVES=SOMETIMES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT STRESSED WORK/FAMILY=FREQUENTLY</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT STRESSED WORK/FAMILY=NEARLY ALWAYS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT STRESSED WORK/FAMILY=NEVER</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT STRESSED WORK/FAMILY=RARELY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT STRESSED WORK/FAMILY=SOMETIMES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TEACH CAREGIVER/FAMILY/SIGNIF OTHER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT TECH EDUCATION TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TECH EDUC DEVICE ASSIGNED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT TELEHEALTH COORDINATOR (NAME)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT TELEHEALTH DELIVERY/INSTALL MODE</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>CCHT TELEHEALTH DELIVERY/INSTALL MODE</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT TELEHEALTH DEMOGRAPHICS</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>CCHT TELEHEALTH DEMOGRAPHICS</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p><strong>CCHT TELEHEALTH DEVICE(S)</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT TEMPLATE USE (PHASE 3)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TOILET HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT TOILET HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TOILET HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT TOILET HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TRANSFERS HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT TRANSFERS HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TRANSFERS HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT TRANSFERS HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT UNABLE TO SCREEN CAREGIVER</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>HT VET NOT INTERESTED TELEHEALTH PROGRAM</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT VET/CAREGIVER VIEW VIDEOS/HEALTH TV</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT UNCERTAIN WHAT TO DO=FREQUENTLY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT UNCERTAIN WHAT TO DO=NEARLY ALWAYS</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT UNCERTAIN WHAT TO DO=NEVER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT UNCERTAIN WHAT TO DO=RARELY</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT UNCERTAIN WHAT TO DO=SOMETIMES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL ADULT DAY CARE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN REFERRAL EDUC/TRAINING</p>
</blockquote></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL EDUC/TRAINING</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL EMPLOYMENT ASSIST</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL FAMILY COUNSEL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL FINANCIAL ASSIST</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL HOME HEALTH SVC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL HOMEMKR/CHORE ASST</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL HOSPICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL HOUSING</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL INDIVIDUAL COUNSEL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL LEGAL ASSIST</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL MEDICAL EVAL, F/U</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL NURS HOME PLACEMNT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN REFERRAL OTHER SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL OTHER SERVICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL RESPITE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL SOCIAL WORK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN REFERRAL SVCS IN PLACE</p>
</blockquote></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL SVCS IN PLACE</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL TRANSPORTATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
<td><blockquote>
<p>CCHT VETERAN REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN REVIEW OF WRITTEN MATERIALS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN STATES ESSENTIAL CONCEPTS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN'S GOAL FOR ENROLLMENT</p>
</blockquote></td>
<td><blockquote>
<p>CCHT VETERAN'S GOAL FOR ENROLLMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT VIDEO VISIT TEMPLATE USED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT VIDEO VISIT-AUDIO/VIDEO CONNECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CCHT VIDEOPHONE SERIAL #</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT W/C MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>CCHT W/C MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT W/C MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>CCHT W/C MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>PREFERRED HEALTHCARE LANGUAGE</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-ASL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-BRAILLE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-CHINESE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-ENGLISH</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-FRENCH</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-GERMAN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-ITALIAN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-KOREAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-OTHER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-PORTUGUESE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-RUSSIAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-SPANISH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-TAGALOG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-</p>
<p>VIETNAMESE</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

### Appendix C: HT Queued MailMan Report 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the HT TEMPLATES build is installed, a single MailMan message will be sent. Message subjects will be:

- LOCAL CCHT HFs NOT USED IN NAT’L HT REMINDER DIALOG CONTENT This report will build a list of all health factors on the system where:
  - Considered “local” (file IEN 100,000 or greater), and
    - Factor contains “CCHT” or “CARE COORDINATION HOME TELEHEALTH”, or
    - Category contains “CCHT” or “CARE COORDINATION HOME TELEHEALTH”
  - And the health factor is not used by any of the new HT clinical reminder content

> This report is automatically run as part of the post-installation process for patch PXRM\*2.0\*19. The MailMan message generated by this report is sent to the recipients chosen by the person installing the patch bundle. This first run of this report is intended as a baseline in order to assist sites with configuration and/or any necessary cleanup related to Home Telehealth health factors. NOTE: A health factor appearing in this report should only be interpreted to mean that the health factor is not part of the HT Templates build. These health factors could actually be in use outside of the National HT dialogs. Any given health factor should not be deleted/deprecated/inactivated based solely on this report. Any such decisions should be made in concert with the local facility personnel who can best determine how/where a given health factor is or is not being used.

> After any cleanup/configuration issues are resolved, the report may be run again, as needed, to verify no outstanding issues are remaining. To run the report again, you will need a programmer’s assistance. That individual will need to execute the following program:

> DEV\>D MAIN^PXRMP19A

> The program will, again, generate the MailMan message with one slight difference in delivery. When not run as part of the post-installation, the report will be sent directly to the programmer executing the code (DUZ). That person should forward the message to the appropriate points-of- contact. No new menu options were created for this report due to its temporary nature and the fact that a subsequent national patch would have been necessary to remove it from the OPTION file.

#### LOCAL CCHT HFs NOT USED IN NAT’L HT REMINDER DIALOGS CONTENT

> Purpose: Provides information to sites on status of Health Factors on system vs. National dialogs. This report attempts to find all local Health Factors that are NOT used in the National dialogs for HT. This is done via building a list of local Health Factors whose name contains “CCHT” or “HOME TELEHEALTH” and then comparing that list to the Health Factors used in the National dialogs.

#### SAMPLE

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 55%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT SCORE 2</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT SCORE 3</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT SCORE 4</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT SCORE 5</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT SCORE 6</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT SCORE 7</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT SCORE 8</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT SCORE 9</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY-ACUTE CARE</p>
<p>CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY-CHRONIC CARE</p>
<p>CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY-HEALTH PROMOTION</p>
<p>CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY-NON INSTITUTIONAL CARE CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CATEGORY-TELEPHONE CASE MANAGEMENT CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF 1 OR MORE BEHAV/COGN PROBLEMS CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF 12 OR MORE CLINIC STOPS CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF 2 OR MORE ADL DEFICITS CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF AGE 75 OR GREATER CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF AGITATED/DISORIENTED-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF AGITATED/DISORIENTED-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER ACCESSIBLE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER CAN INCREASE HELP</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 50%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>CCHT CONTINUUM OF CARE NO</p>
<p>CCHT CCF CAREGIVER CAN'T INCREASE HELP</p>
<p>CCHT CONTINUUM OF CARE NO</p>
<p>CCHT CCF CAREGIVER LIVES WITH PT-NO</p>
<p>CCHT CONTINUUM OF CARE NO</p>
<p>CCHT CCF CAREGIVER LIVES WITH PT-YES</p>
<p>CCHT CONTINUUM OF CARE NO</p>
<p>CCHT CCF CAREGIVER NOT ACCESSIBLE</p>
<p>CCHT CONTINUUM OF CARE NO</p>
<p>CCHT CCF CAREGIVER SAME NAME AS PT</p>
<p>CCHT CONTINUUM OF CARE NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER'S CITY CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER'S NAME CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER'S PHONE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER'S STATE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER'S STREET ADDRESS CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER'S ZIP CODE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-ADL HELP CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-CHILD CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-EMOTIONAL SUPPORT CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-FRIEND/NEIGHBOR CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-IADL HELP CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-OTHER CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-SPOUSE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF COMPLEXITY TOO GREAT-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF COMPLEXITY TOO GREAT-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DELUSIONS-NO</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 53%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT CONTINUUM OF CARE</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DELUSIONS-YES</p>
<p>CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DIFFIC MAKE SELF UNDERSTOOD-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DIFFIC MAKE SELF UNDERSTOOD-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DIFFIC REASONABLE DECISIONS-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DIFFIC REASONABLE DECISIONS-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DOES NOT MEET NIC CRITERIA CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF FLARE UP CHRONIC CONDITION-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF FLARE UP CHRONIC CONDITION-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF FOLLOW-UP ASSESSMENT DONE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF GROUP SETTING NON RELATIVES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-AUDITORY CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-NONE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-OLFACTORY CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-SENSORY CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-TACTILE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-VISUAL CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF INITIAL ASSESSMENT DONE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIFE EXPECTANCY &lt; 6 MO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES ALONE</p>
<p>CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES ALONE IN COMMUNITY CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES AT OTHER</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 53%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT CONTINUUM OF CARE</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES BOARD AND CARE CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES DOMICILIARY CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES HOMELESS</p>
<p>CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES HOMELESS SHELTER CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES NURSING HOME CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES PRIVATE HOME CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES WITH ADULT CHILD CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES WITH CHILD CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES WITH OTHER CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES WITH SPOUSE &amp; OTHERS CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES WITH SPOUSE ONLY CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MEETS NIC CATEGORY A CRITERIA CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MEETS NIC CATEGORY B CRITERIA CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MEETS NIC CRITERIA CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MOOD DISORDER DEPRESSION-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MOOD DISORDER DEPRESSION-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MOOD DISORDER MANIC-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MOOD DISORDER MANIC-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF NIC CRITERIA NO-ACUTE CARE MGMT CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF NIC CRITERIA NO-HLTH PROMOTION CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PHYSICALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 53%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT CONTINUUM OF CARE</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PHYSICALLY ABUSIVE BEHAVIOR-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF POTENTIAL FOR INCR INDEP-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF POTENTIAL FOR INCR INDEP-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PROBLEMS IN 3 OR MORE ADLS CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PROBLEMS WITH 3 OR MORE IADL CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PTSD/OTHER ANXIETY-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PTSD/OTHER ANXIETY-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF RECOMMEND REFERRAL CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF RECOMMEND REFERRAL-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF RESISTING CARE-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF RESISTING CARE-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF SERVICES IN PLACE-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF SERVICES IN PLACE-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF SUBST ABUSE/DEPENDENCE-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF SUBST ABUSE/DEPENDENCE-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF UNPAID CAREGIVER-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF UNPAID CAREGIVER-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF VERBALLY ABUSIVE BEHAVIOR-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF VERBALLY ABUSIVE BEHAVIOR-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF WANDERING-NO</p>
<p>CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF WANDERING-YES</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 54%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT CONTINUUM OF CARE</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CG/VETERAN REFERRAL TEMPLATE DONE CCHT REFERRALS FOR VETERAN/CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CG/VETERAN REFERRAL(S) NOT UTILIZED CCHT REFERRALS FOR VETERAN/CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL REASON FOR ENROLLMENT CCHT (HOME TELEHEALTH)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CONTACT MADE FOR EQUIP RETURN CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CONTINUUM OF CARE TEMPLATE USED CCHT TEMPLATE USE (PHASE 3)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT MANAGING MEDS/LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT MANAGING MEDS/LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT MNG FINANCES/LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT MNG FINANCES/LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT PREPARE MEALS/LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT TRANSPRTATION/LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT TRANSPRTATION/LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT USING PHONE LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT USING PHONE LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT W/ HOUSEWORK/LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT W/ HOUSEWORK/LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT WITH SHOPPING/LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT WITH SHOPPING/LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIGITAL CAMERA SERIAL # CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ADMITTED TO NURSING HOME CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ALL EQUIP RETURNED (NO)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 53%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT DISCHARGE</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ALL EQUIP RETURNED (YES) CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ALL ISSUES ADDRESSED(NO) CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ALL ISSUES ADDRESSED(YES) CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-EQUIP RETURN (OTHER) CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-HAS MET GOALS CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-NO RESPONSE TO PROGRAM CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-NO VA PRIMARY CARE SVCS CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-OTHER FOLLOW-UP CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PATIENT IS DECEASED CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PHONE,ELECT SVCS UNAVAIL CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PROLONGED HOSPITALIZATION CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PROVIDER REQUESTS DC CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PT/CG REQUEST DC SERVICES CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO HOSPICE CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO MENTAL HEALTH CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO NEW LOCATION CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO PRIMARY CARE CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO SOCIAL WORK CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-RELOCATED OUT OF SVC AREA CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-UNABLE TO OPERATE DEVICES CCHT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-CHF</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 40%" />
<col style="width: 14%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>CCHT TELEHEALTH DEMOGRAPHICS NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-COPD</p>
<p>CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-DEPRESSION CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-DIABETES CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-HYPERTENSION CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-OTHER CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-PTSD</p>
<p>CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-SUBST ABUSE CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DRESSING HELP/SUPERV LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DRESSING HELP/SUPERV LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EATING HELP/SUPERVISION LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EATING HELP/SUPERVISION LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EDUC ON EQUIP-CARE COORDINATOR CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EDUC ON EQUIP-CONTRACT VENDOR CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EDUC ON EQUIP-SUPPORT STAFF CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EMERG PRIORITY HIGH-IMMEDIATE EVAL CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EMERG PRIORITY LOW-HAS RESOURCES CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EMERG PRIORITY MOD-SVCS AFTER 3-7D CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>ENROLLMENT-ENDING DATE CCHT (HOME TELEHEALTH)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>ENROLLMENT-START DATE CCHT (HOME TELEHEALTH)</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EQUIP INSTALLATION MODE-OTHER CCHT TELEHEALTH DELIVERY/INSTALL</p>
</blockquote></td>
<td><blockquote>
<p>MODE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EQUIP INSTALLED BY CARE COORDINATOR</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 55%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EQUIP INSTALLED BY CONTRACT VENDOR CCHT TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EQUIP INSTALLED BY SUPPORT STAFF</p>
<p>CCHT TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EQUIP INSTALLED BY VETERAN/CAREGVR CCHT TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EQUIP MAILED,INSTALL BY VET/CAREGVR CCHT TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EQUIP TAKEN HOME,INSTALL BY VET/CG CCHT TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-# OUTPT VISITS PAST YR CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-DISTANCE (HOURS) CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-DISTANCE (MILES) CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-HX HIGH COST/HIGH USE CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-HX HOSPITALIZATONS CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>LEARNING BARRIER-LANGUAGE</p>
<p>CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>LEARNING BARRIER-NONE IDENTIFIED CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>LEARNING BARRIER-UNABLE TO READ CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>LEARNING BARRIER-VISUALLY IMPAIRED CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MAKE TIME FOR SELF=FREQUENTLY</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MAKE TIME FOR SELF=NEARLY ALWAYS</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MAKE TIME FOR SELF=NEVER</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MAKE TIME FOR SELF=RARELY</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MAKE TIME FOR SELF=SOMETIMES</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEALS PREPARED BY OTHER/LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEALS PREPARED BY OTHER/LAST 7D-YES</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> CCHT CONTINUUM OF CARE NO

> CCHT MEASURING DEVICE-OTHER

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MEDS ADAPT-FOR VISUAL IMPAIRMENT

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT MEDS ADAPT-MEDS ARE COLOR CODED

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT MEDS ADAPT-USES PILLBOX

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT MEDS ADAPT-VA PREPARES/POURS MEDS

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT MEDS ADAPTATIONS-NONE NEEDED

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT MEDS ADAPTATIONS-OTHER

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT MEDS SPECIAL ADAPTATIONS

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT MEETS TELEHEALTH CRITERIA(NO)

> CCHT TELEHEALTH DEMOGRAPHICS NO

> CCHT MEETS TELEHEALTH CRITERIA(YES)

> CCHT TELEHEALTH DEMOGRAPHICS NO

> CCHT MESSAGING DEVICE TYPE/SERIAL \#

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING DEVICE-BLOOD GLUCOSE

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING DEVICE-BLOOD PRESSURE

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING DEVICE-PULSE

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING DEVICE-PULSE OXIMETRY

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING DEVICE-WEIGHT

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING/MONITORING TYPE/SERIAL \#

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING/MONITORING-BLOOD GLUCOSE

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING/MONITORING-BLOOD PRESSURE

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING/MONITORING-OTHER

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT MESSAGING/MONITORING-PULSE

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 53%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></th>
<th><blockquote>
<p>NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MESSAGING/MONITORING-PULSE OXIMETRY CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MESSAGING/MONITORING-SPIROMETRY CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MESSAGING/MONITORING-WEIGHT CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MOVE INDOOR HELP/SUPERV LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MOVE INDOOR HELP/SUPERV LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIODIC EVALUATION DONE</p>
<p>CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERALS-BP CUFF (SERIAL #) CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERALS-GLUCOSE CABLES CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERALS-NONE NEEDED CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERALS-OTHER</p>
<p>CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERALS-PULSE OX (SERIAL #) CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERALS-SPIROMETRY (SERIAL #) CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERALS-STETHOSCOPE CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIPHERALS-WEIGHT SCALE (SERIAL #) CCHT TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PHONE-DSL LINE</p>
<p>CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PHONE-MODEM</p>
<p>CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PHONE-NO FEATURES</p>
<p>CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PLAN-MED DISCREP SENT TO PROVIDER CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PLAN-REVIEWED LIST CURRENT MEDS CCHT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>REASON FOR NON-ENROLLMENT CCHT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>RECENT CHANGE IN FUNCTION-NO</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 55%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p>CCHT CONTINUUM OF CARE NO</p>
<p>CCHT RECENT CHANGE IN FUNCTION-YES</p>
<p>CCHT CONTINUUM OF CARE NO</p>
<p>CCHT REFERRAL-CONSULT COMPLETION</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>CCHT (HOME TELEHEALTH)</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>REFERRALS-CAREGIVER NOT SATISFIED CCHT REFERRALS FOR VETERAN/CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>REFERRALS-CAREGIVER SATISFIED</p>
<p>CCHT REFERRALS FOR VETERAN/CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED WITH RELATIVES=FREQUENTLY CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED WITH RELATIVES=NEVER</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED WITH RELATIVES=NRLY ALWAYS CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED WITH RELATIVES=RARELY</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED WITH RELATIVES=SOMETIMES</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED WORK/FAMILY=FREQUENTLY</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED WORK/FAMILY=NEARLY ALWAYS CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED WORK/FAMILY=NEVER</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED WORK/FAMILY=RARELY</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED WORK/FAMILY=SOMETIMES</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TOILET HELP/SUPERVISION LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TOILET HELP/SUPERVISION LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TRANSFERS HELP/SUPERV LAST 7D-NO CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TRANSFERS HELP/SUPERV LAST 7D-YES CCHT CONTINUUM OF CARE</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>UNCERTAIN WHAT TO DO=FREQUENTLY</p>
<p>CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>UNCERTAIN WHAT TO DO=NEARLY ALWAYS CCHT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>UNCERTAIN WHAT TO DO=NEVER</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> CCHT CAREGIVER RISK ASSESSMENT SCREEN NO

> CCHT UNCERTAIN WHAT TO DO=RARELY

> CCHT CAREGIVER RISK ASSESSMENT SCREEN NO

> CCHT UNCERTAIN WHAT TO DO=SOMETIMES

> CCHT CAREGIVER RISK ASSESSMENT SCREEN NO

> CCHT VETERAN'S GOAL FOR ENROLLMENT

> CCHT (HOME TELEHEALTH) NO

> CCHT VIDEO VISIT-AUDIO/VIDEO CONNECTION

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT VIDEOPHONE SERIAL \#

> CCHT TELEHEALTH DEVICE(S) NO

> CCHT W/C MOBIL HELP/SUPERV LAST 7D-NO

> CCHT CONTINUUM OF CARE NO

> CCHT W/C MOBIL HELP/SUPERV LAST 7D-YES

> CCHT CONTINUUM OF CARE NO

> CCHT-CAREGIVER REFERRAL BEREAVE SUPPORT

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-CAREGIVER REFERRAL C/G SUPPORT GRP

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-CAREGIVER REFERRAL EDUC/TRAINING

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-CAREGIVER REFERRAL FAMILY COUNSEL

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-CAREGIVER REFERRAL INDIVID COUNSEL

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-CAREGIVER REFERRAL MEDICAL EVAL,F/U

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-CAREGIVER REFERRAL OTHER SERVICE

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-CAREGIVER REFERRAL SVCS IN PLACE

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-CAREGIVER REFERRAL(S) NON VA SYSTEM

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-CAREGIVER REFERRAL(S) VA SYSTEM

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-GETS MEDS VIA NON-VA PROVIDER-NO

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-GETS MEDS VIA NON-VA PROVIDER-YES

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG HAS LIST OF ACTIVE MEDS-NO

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG HAS LIST OF ACTIVE MEDS-YES

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG HAS QUESTIONS ON MEDS-NO

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG HAS QUESTIONS ON MEDS-YES

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG KNOWS MED INDICATIONS-NO

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG KNOWS MED INDICATIONS-YES

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG KNOWS MED SIDE EFF-NO

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG KNOWS MED SIDE EFFECTS-YES

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG KNOWS REFILL PROCESS-NO

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG KNOWS REFILL PROCESS-YES

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG TAKES MEDS AS PRESCRIBED-NO

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-PT/CG TAKES MEDS AS PRESCRIBED-YES

> CCHT ASSESSMENT/TREATMENT PLAN NO

> CCHT-VETERAN REFERRAL ADULT DAY CARE

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL EDUC/TRAINING

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL EMPLOYMENT ASSIST

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL FAMILY COUNSEL

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL FINANCIAL ASSIST

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL HOME HEALTH SVC

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL HOMEMKR/CHORE ASST

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL HOSPICE

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL HOUSING

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL INDIVIDUAL COUNSEL

> CCHT REFERRALS FOR VETERAN/CAREGIVER NO

> CCHT-VETERAN REFERRAL LEGAL ASSIST

### Appendix D: Contents of the Packed Reminder Export HT Templates/Reminders Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Exchange File Components Mar 02, 2017@10:10:04 Page: 1 of 1

> Component Category Exists- Source: DOE,JOHN at SALT LAKE CITY

> Date Packed: 03/02/2017@10:10:04 Package Version: 2.0P62

> Description:

> This pack is to support installation of PXRM\*2.0\*19. It contains the standardized reminder dialogs and definitions as requested by the

> VHA Office of Connected Care(10P8).

> The following Clinical Reminder items were selected for packing: REMINDER DIALOG

> VA-HT DISCHARGE TEMPLATE VA-HT VIDEO VISIT TEMPLATE

> VA-HT TECH EDUCATION & INSTALLATION TEMPLATE VA-HT CONTINUUM OF CARE TEMPLATE

> VA-HT SCREENING CONSULT TEMPLATE

> VA-HT ASSESSMENT TREATMENT PLAN TEMPLATE VA-HT CAREGIVER ASSESSMENT TEMPLATE

> VA-HT INTERVENTION TEMPLATE

> VA-HT CAREGIVER/VETERAN REFERRAL VA-HT CAREGIVER RISK ASSESSMENT VA-HT CONTINUUM OF CARE (INITIAL) VA-HT PERIODIC EVALUATION

> VA-HT CONTINUUM OF CARE (FOLLOW-UP)

> VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS

> REMINDER DEFINITION

> VA-HT PERIODIC EVALUATION

> VA-HT CAREGIVER RISK ASSESSMENT VA-HT CONTINUUM OF CARE (INITIAL)

> VA-HT OBJ EMERGENCY PRIORITY RATING LAST VA-HT OBJ EDUCATION TOPICS ALL

> VA-HT OBJ CATEGORY OF CARE LAST VA-HT OBJ NIC/CCM RATING LAST

> VA-HT OBJ MEDICATION RECONCILIATION VA-HT CONTINUUM OF CARE (FOLLOW-UP) VA-HT OBJ BARRIERS TO LEARNING

> VA-HT OBJ CCM RATING LAST

> VA-HT OBJ CONTINUUM OF CARE LAST DONE

> Non-exchangeable order dialog(s):

> Name: PSH OERR

> Type: Dialog

> Display Text: Non VA Medications

> Non-exchangeable TIU object(s):

> TIU Object: PATIENT AGE

> Object Method: S X=\$\$AGE^TIULO(DFN)

> TIU Object: PATIENT DATE OF DEATH

> Object Method: S X=\$\$DOD^TIULO(DFN)

> TIU Object: PAIN

> Object Method: S X=\$\$PAIN^TIULO(+\$G(DFN))

> TIU Object: PATIENT HEIGHT

> Object Method: S X=\$\$HEIGHT^TIULO(+\$G(DFN))

> TIU Object: PATIENT WEIGHT

> Object Method: S X=\$\$WEIGHT^TIULO(+\$G(DFN))

> TIU Object: TEMPERATURE

> Object Method: S X=\$\$TEMP^TIULO(+\$G(DFN))

> TIU Object: PULSE

> Object Method: S X=\$\$PULSE^TIULO(+\$G(DFN))

> TIU Object: RESPIRATION

> Object Method: S X=\$\$RESP^TIULO(+\$G(DFN))

> TIU Object: BLOOD PRESSURE

> Object Method: S X=\$\$BP^TIULO(+\$G(DFN))

> TIU Object: ACTIVE MEDICATIONS

> Object Method: S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",1)

> Keywords:

> HOME TELEHEALTH, PXRM\*2.0\*19, HT,

> VA-HT PROJECT,

> Components:

> ROUTINE

> ORDER

> GMRV VITAL TYPE

> PAIN X

> MH TESTS AND SURVEYS

> ZBI SCREEN X

> TIU TEMPLATE FIELD

1.  VA-HT SPECIFY X
2.  VA-HT W-P4LINES(R) X
3.  VA-HT W-P2LINES(R) X
4.  BLANK SPACE1 X
5.  OPTIONAL TEXT X
6.  VA-HT EDIT50 X
7.  OTHER(REQ-DISP ONLY) X
8.  VA-HT OTHER X
9.  TEXT (1-60 CHARACTERS) REQ X
10. VA-HT W-P6LINES(R) X
11. VA-HT W-P6LINES X
12. VA-HT VITAL SIGNS MODE X

> EDUCATION TOPICS

13. VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT X
14. VA-ALCOHOL ABUSE FOLLOW-UP X
15. VA-ALCOHOL ABUSE MEDICATIONS X
16. VA-ALCOHOL ABUSE EXERCISE X
17. VA-ALCOHOL ABUSE DIET X
18. VA-ALCOHOL ABUSE LIFESTYLE ADAPTATIONS X
19. VA-ALCOHOL ABUSE COMPLICATIONS X
20. VA-ALCOHOL ABUSE DISEASE PROCESS X
21. VA-SMOKING CESSATION X
22. VA-IMMUNIZATIONS X
23. VA-EXERCISE X
24. VA-NUTRITION/OBESITY X
25. VA-HTN NUTRITION EDUCATION X
26. VA-HTN MEDICATION ADHERENCE X
27. VA-HTN EXERCISE X
28. VA-DIABETES FOLLOW-UP X
29. VA-DIABETES MEDICATIONS X
30. VA-DIABETES FOOT CARE X
31. VA-DIABETES EXERCISE X
32. VA-DIABETES DIET X
33. VA-DIABETES LIFESTYLE ADAPTATIONS X
34. VA-DIABETES COMPLICATIONS X
35. VA-DIABETES DISEASE PROCESS X
36. VA-SAFETY/HOME/FALLS X
37. VA-ADVANCE DIRECTIVES SCREENING X
38. VA-ADVANCE DIRECTIVES X
39. VA-HOME TELEHEALTH-MEDICATION MANAGEMENT X
40. VA-HOME TELEHEALTH-IN HOME MONITORING X
41. VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT X HEALTH FACTORS

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 53%" />
<col style="width: 21%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>74</th>
<th>HT</th>
<th>CCF</th>
<th><blockquote>
<p>PTSD/OTHER ANXIETY-YES</p>
</blockquote></th>
<th colspan="2">X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>75</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>SUBST ABUSE/DEPENDENCE-NO</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>76</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>SUBST ABUSE/DEPENDENCE-YES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>77</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>MOOD DISORDER MANIC-NO</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>78</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>MOOD DISORDER MANIC-YES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>79</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>MOOD DISORDER DEPRESSION-NO</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>80</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>MOOD DISORDER DEPRESSION-YES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>81</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>DELUSIONS-NO</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>82</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>DELUSIONS-YES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>83</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>HALLUCINATIONS-TACTILE</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>84</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>HALLUCINATIONS-OLFACTORY</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>85</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>HALLUCINATIONS-VISUAL</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>86</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>HALLUCINATIONS-AUDITORY</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>87</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>HALLUCINATIONS-SENSORY</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>88</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>HALLUCINATIONS-NONE</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>89</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>POTENTIAL FOR INCR INDEP-NO</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>90</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>POTENTIAL FOR INCR INDEP-YES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td>91</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>FLARE UP CHRONIC CONDITION-NO</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td>92</td>
<td>HT</td>
<td>CCF</td>
<td><blockquote>
<p>FLARE UP CHRONIC CONDITION-YES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>93 HT RECENT CHANGE IN FUNCTION-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>94 HT RECENT CHANGE IN FUNCTION-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>95 HT CCF AGITATED/DISORIENTED-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>96 HT CCF AGITATED/DISORIENTED-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>97 HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>98 HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>99 HT CCF DIFFIC REASONABLE DECISIONS-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>100 HT CCF DIFFIC REASONABLE DECISIONS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>101 HT CCF UNPAID CAREGIVER-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>102 HT CCF CAREGIVER CAN'T INCREASE HELP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>103 HT CCF CAREGIVER CAN INCREASE HELP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>104 HT CCF CAREGIVER NOT ACCESSIBLE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>105 HT CCF CAREGIVER ACCESSIBLE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>106 HT CCF CAREGIVER-IADL HELP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>107 HT CCF CAREGIVER-ADL HELP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>108 HT CCF CAREGIVER-EMOTIONAL SUPPORT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>109 HT CCF CAREGIVER-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>110 HT CCF CAREGIVER-FRIEND/NEIGHBOR</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>111 HT CCF CAREGIVER-CHILD</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>112 HT CCF CAREGIVER-SPOUSE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>113 HT CCF CAREGIVER'S PHONE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>114 HT CCF CAREGIVER'S ZIP CODE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>115 HT CCF CAREGIVER'S STATE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>116 HT CCF CAREGIVER'S CITY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>117 HT CCF CAREGIVER'S STREET ADDRESS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>118 HT CCF CAREGIVER'S NAME</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>119 HT CCF CAREGIVER LIVES WITH PT-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>120 HT CCF CAREGIVER LIVES WITH PT-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>121 HT CCF UNPAID CAREGIVER-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>122 HT CCF LIVES HOMELESS SHELTER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>123 HT CCF LIVES HOMELESS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>124 HT CCF LIVES AT OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>125 HT CCF LIVES DOMICILIARY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>126 HT CCF LIVES NURSING HOME</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>127 HT CCF LIVES BOARD AND CARE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>128 HT CCF LIVES PRIVATE HOME</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>129 HT CCF LIVES WITH OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>130 HT CCF GROUP SETTING NON RELATIVES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>131 HT CCF LIVES WITH ADULT CHILD</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>132 HT CCF LIVES WITH CHILD</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>133 HT CCF LIVES WITH SPOUSE &amp; OTHERS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>134 HT CCF LIVES WITH SPOUSE ONLY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>135 HT CCF LIVES ALONE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>136 GEC REFERRAL IADL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 59%" />
<col style="width: 19%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>137</p>
</blockquote></th>
<th><blockquote>
<p>GEC</p>
</blockquote></th>
<th><blockquote>
<p>RECENT CHANGE IN IADL FX-YES</p>
</blockquote></th>
<th></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>138</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>RECENT CHANGE IN IADL FX-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>139</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>MEALS PREPARED BY OTHERS/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>140</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>MEALS PREPARED BY OTHERS/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>141</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY WITH SHOPPING/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>142</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY WITH SHOPPING/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>143</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY W/ HOUSEWORK/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>144</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY W/ HOUSEWORK/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>145</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY USING PHONE/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>146</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY USING PHONE/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>147</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY PREPARE MEALS/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>148</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY PREPARE MEALS/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>149</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY MNG FINANCES/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>150</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY MNG FINANCES/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>151</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY MANAGING MEDS/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>152</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULTY MANAGING MEDS/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>153</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT TRANSPORTATION/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>154</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT TRANSPORTATION/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>155</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT PREPARE MEALS/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>156</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT PREPARE MEALS/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>157</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>MEALS PREPARED BY OTHER/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>158</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>MEALS PREPARED BY OTHER/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>159</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT W/ HOUSEWORK/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>160</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT W/ HOUSEWORK/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT WITH SHOPPING/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT WITH SHOPPING/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>163</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT TRANSPORTATION/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>164</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT TRANSPORTATION/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>165</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT USING PHONE LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>166</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT USING PHONE LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>167</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT MANAGING MEDS/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>168</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT MANAGING MEDS/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>169</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT MNG FINANCES/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>170</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>DIFFICULT MNG FINANCES/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>171</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>REFERRAL BASIC ADL</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>172</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>TRANSFERS HELP/SPRVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>173</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>TRANSFERS HELP/SPRVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>174</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>TOILET HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>175</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>TOILET HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>176</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>BATHING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>177</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>RECENT CHANGE IN ADL FX-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>178</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>RECENT CHANGE IN ADL FX-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>179</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>MOVING AROUND INDOORS LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>MOVING AROUND INDOORS LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>181</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>INDEPENDENT IN WC LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>182</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>INDEPENDENT IN WC LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>183</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>EATING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>184</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>EATING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>185</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DRESS HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>186</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>DRESS HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>187</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>BED POSITIONING HELP LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>188</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>BED POSITIONING HELP LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>189</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>BATHING PHYS ASST NEEDED LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>190</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>BATHING PHYS ASST NEEDED LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>191</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>BATHING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>192</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>EATING HELP/SUPERVISION LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>193</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>EATING HELP/SUPERVISION LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>194</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>TOILET HELP/SUPERVISION LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>195</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>TOILET HELP/SUPERVISION LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>196</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>BED MOBIL HELP/SUPERV LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>197</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>BED MOBIL HELP/SUPERV LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>198</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>TRANSFERS HELP/SUPERV LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>199</p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td>TRANSFERS HELP/SUPERV LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 60%" />
<col style="width: 19%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>200</p>
</blockquote></th>
<th>HT</th>
<th><blockquote>
<p>MOVE INDOOR HELP/SUPERV LAST 7D-YES</p>
</blockquote></th>
<th></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>201</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>MOVE INDOOR HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>202</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>BATHING HELP/SUPRVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>203</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>BATHING HELP/SUPRVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>204</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DRESSING HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>205</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DRESSING HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>206</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>W/C MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>207</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>W/C MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>208</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CCF FOLLOW-UP ASSESSMENT COMPLETED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>209</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>REFERRALS FOR VETERAN/CAREGIVER</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>210</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>VETERAN REFERRAL SVCS IN PLACE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>211</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>VETERAN REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>212</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>VETERAN REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>213</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>VETERAN REFERRAL OTHER SERVICE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>214</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>VETERAN REFERRAL EDUC/TRAINING</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>215</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL SOCIAL WORK</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>216</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL SVCS IN PLACE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>217</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>218</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>219</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL BEREAVE SUPPORT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>220</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL OTHER SERVICE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>221</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL MEDICAL EVAL,F/U</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>222</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL EDUC/TRAINING</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>223</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL C/G SUPPORT GRP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>224</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL FAMILY COUNSEL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>225</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REFERRAL INDIVID COUNSEL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>226</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CG/VETERAN REFERRAL COMPLETED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>227</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>228</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>UNABLE TO SCREEN CAREGIVER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>229</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER ASSESSMENT SCREEN COMPLETED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>230</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CG/VETERAN REFERRAL(S) NOT UTILIZED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>231</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>REFERRALS-CAREGIVER NOT SATISFIED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>232</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>REFERRALS-CAREGIVER SATISFIED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>233</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>234</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CATEGORY OF CARE-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>235</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CATEGORY OF CARE-HEALTH PROMOTION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>236</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CATEGORY OF CARE-CHRONIC CARE MGMT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>237</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CATEGORY OF CARE-ACUTE CARE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>238</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CATEGORY OF CARE-NON INSTITUTIONAL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>239</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>HEALTH EDUCATION PLAN</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>240</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CONSULTS/REFERRALS RECOMMENDED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>241</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>TEACH CAREGIVER/FAMILY/SIGNIF OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>242</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>VET/CAREGIVER VIEW VIDEOS/HEALTH TV</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>243</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER REVIEW OF WRITTEN MATERIALS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>244</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>VETERAN REVIEW OF WRITTEN MATERIALS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>245</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>REPEAT DEMONSTRATION NEXT VISIT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>246</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>NO FOLLOW-UP NEEDED/INDICATED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>247</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>HEALTH EDUCATION RESPONSE</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>248</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>NO EVIDENCE OF LEARNING</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>249</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>NEEDS REINFORCEMENT/REVIEW/FOLLOW-UP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>250</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DISINTERESTED/LACKS MOTIVATION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>251</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>CAREGIVER STATES ESSENTIAL CONCEPTS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>252</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>VETERAN STATES ESSENTIAL CONCEPTS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>253</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>EMERG PRIORITY HIGH-IMMEDIATE EVAL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>254</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>EMERG PRIORITY MOD-SVCS AFTER 3-7D</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>255</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>EMERG PRIORITY LOW-HAS RESOURCES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>256</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>PLAN-MED DISCREP SENT TO PROVIDER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>257</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>PLAN-REVIEWED LIST OF CURRENT MEDS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>258</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>PT/CG HAS QUESTIONS ON MEDS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>259</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>PT/CG HAS QUESTIONS ON MEDS-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>260</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>PT/CG HAS LIST OF ACTIVE MEDS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>261</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>PT/CG HAS LIST OF ACTIVE MEDS-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>262</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>GETS MEDS VIA NON-VA PROVIDER-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 71%" />
<col style="width: 19%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>263 HT GETS MEDS VIA NON-VA PROVIDER-NO</p>
</blockquote></th>
<th></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>264 HT DISCHARGE</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>265 HT DISCHARGE-HAS MET GOALS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>266 HT DISCHARGE-PT/CG REQUEST DC SERVICES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>267 HT DISCHARGE-UNABLE TO OPERATE DEVICES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>268 HT DISCHARGE-RELOCATED OUT OF SVC AREA</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>269 HT DISCHARGE-ADMITTED TO NURSING HOME</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>270 HT DISCHARGE-NO VA PRIMARY CARE SVCS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>271 HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>272 HT DISCHARGE-REFERRED TO HOSPICE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>273 HT DISCHARGE-PATIENT IS DECEASED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>274 HT DISCHARGE-PROLONGED HOSPITALIZATION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>275 HT DISCHARGE-PROVIDER REQUESTS DC</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>276 HT DISCHARGE-NO RESPONSE TO PROGRAM</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>277 HT CCF INITIAL ASSESSMENT COMPLETED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>278 HT (HOME TELEHEALTH)</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>279 HT ENROLLMENT-START DATE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>280 HT PERIODIC EVALUATION COMPLETED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>281 HT ENROLLMENT-START DATE (PREV ENROLL)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>282 PREFERRED HEALTHCARE LANGUAGE</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>283 PREFERRED HEALTHCARE LANGUAGE-ENGLISH</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>284 PREFERRED HEALTHCARE LANGUAGE-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>285 PREFERRED HEALTHCARE LANGUAGE-ASL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>286 PREFERRED HEALTHCARE LANGUAGE-BRAILLE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>287 PREFERRED HEALTHCARE LANGUAGE-PORTUGUESE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>288 PREFERRED HEALTHCARE LANGUAGE-ITALIAN</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>289 PREFERRED HEALTHCARE LANGUAGE-RUSSIAN</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>290 PREFERRED HEALTHCARE LANGUAGE-KOREAN</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>291 PREFERRED HEALTHCARE LANGUAGE-GERMAN</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>292 PREFERRED HEALTHCARE LANGUAGE-VIETNAMESE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>293 PREFERRED HEALTHCARE LANGUAGE-TAGALOG</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>294 PREFERRED HEALTHCARE LANGUAGE-FRENCH</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>295 PREFERRED HEALTHCARE LANGUAGE-CHINESE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>296 PREFERRED HEALTHCARE LANGUAGE-SPANISH</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>297 HT BARRIERS TO LEARNING</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>298 HT LEARNING BARRIER-VISUALLY IMPAIRED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>299 HT LEARNING BARRIER-UNABLE TO WRITE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>300 HT LEARNING BARRIER-UNABLE TO READ</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>301 HT LEARNING BARRIER-PHYSICAL LIMITATIONS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>302 HT LEARNING BARRIER-PAIN</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>303 HT LEARNING BARRIER-OVERWHELMED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>304 HT LEARNING BARRIER-NOT MOTIVATED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>305 HT LEARNING BARRIER-HOMELESS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>306 HT LEARNING BARRIER-HEARING IMPAIRED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>307 HT LEARNING BARRIER-CULTURAL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>308 HT LEARNING BARRIER-POOR CONCENTRATION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>309 HT LEARNING BARRIER-IMPAIRED MEMORY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>310 HT LEARNING BARRIER-APHASIA</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>311 HT LEARNING BARRIER-COGNITIVE IMPAIRMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>312 HT LEARNING BARRIER-ANXIETY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>313 HT LEARNING BARRIER-ANGRY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>314 HT LEARNING BARRIER-NONE IDENTIFIED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>315 HT VETERAN'S GOAL FOR ENROLLMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>316 HT CLINICAL REASON FOR ENROLLMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>317 HT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>318 HT MEETS TELEHEALTH CRITERIA(YES)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>319 HT REASON FOR NON-ENROLLMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>320 HT MEETS TELEHEALTH CRITERIA(NO)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>321 HT INDICATIONS-HX HOSPITALIZATONS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>322 HT INDICATIONS-DISTANCE (HOURS)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>323 HT INDICATIONS-DISTANCE (MILES)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>324 HT INDICATIONS-# OUTPT VISITS PAST YR</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>325 HT INDICATIONS-HX HIGH COST/HIGH USE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 4%" />
<col style="width: 10%" />
<col style="width: 50%" />
<col style="width: 19%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>326</p>
</blockquote></th>
<th>HT</th>
<th><blockquote>
<p>DISEASE</p>
</blockquote></th>
<th><blockquote>
<p>INDICATIONS-OTHER</p>
</blockquote></th>
<th colspan="2">X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>327</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DISEASE</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-SUBSTANCE ABUSE</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>328</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DISEASE</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-PTSD</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>329</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DISEASE</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-DEPRESSION</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>330</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DISEASE</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-OBESITY</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>331</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DISEASE</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-DIABETES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>332</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DISEASE</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-HYPERTENSION</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>333</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DISEASE</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-COPD</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>334</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>DISEASE</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-HEART FAILURE</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>335</p>
</blockquote></td>
<td>HT</td>
<td><blockquote>
<p>VET NOT</p>
</blockquote></td>
<td><blockquote>
<p>INTERESTED TELEHEALTH PROGRAM</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>336</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>REFERRAL-CONSULT COMPLETION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>337</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>338</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>EQUIP INSTALLED BY OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>339</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>EQUIP INSTALLED BY VETERAN/CAREGIVER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>340</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>EQUIP INSTALLED BY SUPPORT STAFF</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>341</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>DISCHARGE-OTHER FOLLOW-UP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>342</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>DISCHARGE-REFERRED TO MENTAL HEALTH</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>343</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>DISCHARGE-REFERRED TO SOCIAL WORK</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>344</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>DISCHARGE-REFERRED TO NEW LOCATION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>345</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>DISCHARGE-REFERRED TO PRIMARY CARE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>346</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>DISCHARGE-ALL ISSUES ADDRESSED(NO)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>347</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>DISCHARGE-ALL ISSUES ADDRESSED(YES)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>348</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>ENROLLMENT-ENDING DATE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>349</p>
</blockquote></td>
<td>HT</td>
<td colspan="2"><blockquote>
<p>LEARNING BARRIER-LANGUAGE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
</tbody>
</table>

> REMINDER SPONSOR

350. VHA Office of Connected Care (10P8) X

> REMINDER COMPUTED FINDINGS

> VA-AGE X

> VA-FILEMAN DATE X

> REMINDER TAXONOMY

351. VA-HT ENCOUNTER PHONE 21 X
352. VA-HT ENCOUNTER PHONE 11 X
353. VA-HT ENCOUNTER PHONE 5 X

> REMINDER TERM

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 67%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>354</p>
</blockquote></th>
<th>VA-HT</th>
<th><blockquote>
<p>BL NIC/CCM CRITERIA</p>
</blockquote></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>355</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CCM (CHRONIC CARE MGMT) CRITERIA</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>356</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>SUPPRESS FOR AGE &lt;75</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>357</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>BL GEC IADLS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>358</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>BL HT IADLS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>359</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>BL GEC BASIC ADLS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>360</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>BL HT BASIC ADLS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>361</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CATEGORY OF CARE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>362</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>EMERGENCY PRIORITY RATINGS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>363</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>PT/CAREGIVER QUESTIONS ON MEDICATIONS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>364</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>PT/CAREGIVER LIST OF ACTIVE MEDICATIONS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>365</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>MEDICATIONS VIA NON-PROVIDER</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>366</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>DISCHARGE REASONS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>367</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CCF FOLLOW-UP ASSESSMENT COMPLETED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>368</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CCF INITIAL ASSESSMENT COMPLETED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>369</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CCF DOES NOT MEET CCM CRITERIA</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>370</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CCF MEETS CHRONIC CARE MGMT CRITERIA</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>371</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CCF DOES NOT MEET NIC CRITERIA</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>372</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CCF MEETS NIC CRITERIA</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>373</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>ENROLLMENT-START DATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>374</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>PERIODIC EVALUATION COMPLETED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>375</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CAREGIVER RISK ASSESSMENT DONE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>376</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>UNABLE TO SCREEN CAREGIVER</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>377</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>CCF UNPAID CAREGIVER-YES</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>378</p>
</blockquote></td>
<td>VA-HT</td>
<td><blockquote>
<p>ENROLLMENT-START DATE (PREV ENROLL)</p>
</blockquote></td>
<td>X</td>
</tr>
</tbody>
</table>

379. VA-HT CAREGIVER RELATIONSHIP X
380. VA-HT CONTINUUM OF CARE LAST X

> REMINDER DEFINITION

381. VA-HT OBJ NIC/CCM RATING LAST X
382. VA-HT OBJ CATEGORY OF CARE LAST X
383. VA-HT OBJ EMERGENCY PRIORITY RATING LAST X
384. VA-HT OBJ MEDICATION RECONCILIATION X
385. VA-HT CONTINUUM OF CARE (FOLLOW-UP) X
386. VA-HT PERIODIC EVALUATION X
387. VA-HT CAREGIVER RISK ASSESSMENT X
388. VA-HT CONTINUUM OF CARE (INITIAL) X
389. VA-HT OBJ CAREGIVER NAME/RELATIONSHIP X
390. VA-HT OBJ CONTINUUM OF CARE LAST DONE X
391. VA-HT OBJ CCM RATING LAST X
392. VA-HT OBJ BARRIERS TO LEARNING X
393. VA-HT OBJ EDUCATION TOPICS ALL X

> REMINDER DIALOG

394. VA-HT CONTINUUM OF CARE (FOLLOW-UP) X
395. VA-HT PERIODIC EVALUATION X
396. VA-HT CONTINUUM OF CARE (INITIAL) X
397. VA-HT CAREGIVER RISK ASSESSMENT X
398. VA-HT CAREGIVER/VETERAN REFERRAL X
399. VA-HT INTERVENTION TEMPLATE X
400. VA-HT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS X
401. VA-HT CAREGIVER ASSESSMENT TEMPLATE X
402. VA-HT ASSESSMENT TREATMENT PLAN TEMPLATE X
403. VA-HT SCREENING CONSULT TEMPLATE X
404. VA-HT CONTINUUM OF CARE TEMPLATE X
405. VA-HT TECH EDUCATION & INSTALLATION TEMPLATE X
406. VA-HT VIDEO VISIT TEMPLATE X
407. VA-HT DISCHARGE TEMPLATE X

> HEALTH SUMMARY COMPONENT

> CLINICAL REMINDERS FINDINGS X

> PCE HEALTH FACTORS SELECTED X

> CLINICAL REMINDERS DUE X

> NEXT OF KIN X

> MAS ADMISSIONS/DISCHARGES X

> MAS CLINIC VISITS PAST X

> HEALTH SUMMARY TYPE

408. VA-HT NIC/CCM RATING LAST X
409. VA-GEC IADLS X
410. VA-HT IADLS X
411. VA-GEC BASIC ADLS X
412. VA-HT BASIC ADLS X
413. VA-HT CATEGORY OF CARE LAST X
414. VA-HT EMERGENCY LEVEL LAST X
415. VA-HT MED RECON X
416. VA-HT REMINDERS DUE X
417. VA-HT ENROLLMENT START X
418. VA-HT CAREGIVER X
419. VA-NEXT OF KIN X
420. VA-ADMISSIONS PAST YR X
421. VA-OUTPT APPTS PAST YR X

> HEALTH SUMMARY OBJECTS

422. VA-HT NIC/CCM RATING LAST(TIU) X
423. VA-GEC IADLS(TIU) X
424. VA-HT IADLS(TIU) X
425. VA-GEC BASIC ADLS(TIU) X
426. VA-HT BASIC ADLS(TIU) X
427. VA-HT CATEGORY OF CARE(TIU) X
428. VA-HT EMERGENCY LEVELS(TIU) X
429. VA-HT MED RECON(TIU) X
430. VA-HT REMINDERS DUE(TIU) X
431. VA-HT ENROLLMENT START DATE(TIU) X
432. VA-HT CAREGIVER(TIU) X
433. VA-NEXT OF KIN(TIU) X
434. VA-ADMISSIONS PAST YR(TIU) X
435. VA-OUTPT APPTS PAST YR(TIU) X

> TIU DOCUMENT DEFINITION

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 65%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>436 HT NIC/CCM RATING LAST</p>
</blockquote></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PATIENT AGE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>437 GEC IADLS (LAST)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>438 HT IADLS LAST</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>439 GEC BASIC ADLS (LAST)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>440 HT BASIC ADLS LAST</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>441 HT CATEGORY OF CARE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>442 HT EMERGENCY PRIORITY RATING</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>443 HT MED RECON</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>ACTIVE MEDICATIONS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>444 HT REMINDERS DUE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>445 HT ENROLLMENT START DATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>446 HT CAREGIVER</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>447 NEXT OF KIN</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>BLOOD PRESSURE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PAIN</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PATIENT WEIGHT</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PATIENT HEIGHT</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>RESPIRATION</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>PULSE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>TEMPERATURE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>448 ADMISSIONS PAST YR</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>449</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>OUTPT APPTS PAST YR X</p>
<p>PATIENT DATE OF DEATH</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark46" class="anchor"></span><u>Appendix E: Clinic Crosswalk</u>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Current Clinic Location</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Prim. Stop Code</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sec. Stop Code</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Note Titles</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Templates</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>HT SCREENING OFC</strong></p>
</blockquote></td>
<td><blockquote>
<p>Prog. Dep Clinic Code</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>371</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>HT</p>
<p>Screening Consult</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>HT</p>
<p>Screening Consult Template</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>This consult document is used to document initial evaluation for enrollment WHETHER OR NOT the patient is actually enrolled.</p>
<p><strong>NOTE:</strong> Use to close consult</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT SCREENING TC</strong></p>
<p><strong>or</strong></p>
<p><strong>HT SCREENING PHONE</strong></p>
<p><strong>or</strong></p>
<p><strong>HT SCREENING PH</strong></p>
</blockquote></td>
<td><blockquote>
<p>Prog. Dep Phone Code</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT TECH EDUCATION</strong></p>
</blockquote></td>
<td><blockquote>
<p>674</p>
</blockquote></td>
<td><blockquote>
<p>685</p>
</blockquote></td>
<td><blockquote>
<p>HT Tech Education Note</p>
</blockquote></td>
<td><blockquote>
<p>HT Tech Education Template</p>
</blockquote></td>
<td><blockquote>
<p>This document contains patient education, skill validation and installation for technology on all HT patients.</p>
<p>NOTE: ALWAYS attached to the coding pair 674/685 (Non- Count)</p>
<p>Use as often as needed when re-educating the patient on technology, changing or troubleshooting technology or adding new peripheral devices. Training/Education on</p>
<p>technology only.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT INTERVENTION</strong></p>
</blockquote></td>
<td><blockquote>
<p>Prog. Dep Phone Code</p>
</blockquote></td>
<td><blockquote>
<p>684</p>
</blockquote></td>
<td><blockquote>
<p><strong>HT</strong></p>
<p><strong>Intervention Note</strong></p>
</blockquote></td>
<td><blockquote>
<p>HT</p>
<p>Intervention Template</p>
</blockquote></td>
<td><blockquote>
<p>This progress note contains information about all interventions generated from symptoms, behavior and knowledge data gathered from daily monitoring by a non-video messaging device.</p>
<p><strong>NOTE:</strong> Use <strong>ONLY</strong> to document patient encounters in response to alerts from vendor data- not</p>
<p>to be used as generic note, and not to be used with VIDEO visit.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>HT MONTHLY MONITOR</strong></p>
</blockquote></th>
<th><blockquote>
<p>683</p>
</blockquote></th>
<th><blockquote>
<p>Prog. Dep.</p>
<p><strong>Blank for HBPC</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HT Monthly Monitor Note</strong></p>
</blockquote></th>
<th><blockquote>
<p>HT Monthly Monitor Template</p>
</blockquote></th>
<th><blockquote>
<p>This progress note contains information about the monthly monitoring of patients assigned non-video messaging devices.</p>
<p><strong>NOTE:</strong> Document using this note title once each calendar month on <u>EVERY</u> messaging patient regardless of other patient interactions during the month. Not to be used for patients on video technology</p>
<p>that does not have messaging functionality.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>HT VIDEO VISIT</strong></p>
</blockquote></td>
<td><blockquote>
<p>Prog Dep</p>
</blockquote></td>
<td><blockquote>
<p>179</p>
</blockquote></td>
<td><blockquote>
<p>HT Video Visit Note</p>
</blockquote></td>
<td><blockquote>
<p>HT Video Visit Template</p>
</blockquote></td>
<td><blockquote>
<p>This document contains information about any visit over a video device (tele-Monitor/ Videophone) that meets required criteria for secondary Stop Code xxx179</p>
<p><strong>NOTE:</strong> Must meet certain documentation requirements of</p>
<p>replicating a face-to-face visit or it can’t be coded as 179</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT ASSESS TX</strong></p>
<p><strong>PLAN HM</strong></p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>Prog and Location Dep</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>685</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>HT</p>
<p>Assessment Treatment Plan</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>HT</p>
<p>Assessment Treatment Plan Template</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p>This document contains information about the visit with the patient/caregiver which includes the clinical assessment and the HT Plan of Care. Additional signature is requested by the Primary Care Provider (and others, including program staff, as appropriate).Additional time needs to be allocated in DSS upon setup for this Clinic Location</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT ASSESS TX PLAN TC</strong></p>
<p><strong>or</strong></p>
<p><strong>HT ASSESS TX PLAN PHONE</strong></p>
<p><strong>or</strong></p>
<p><strong>HT ASSESS TX PLAN PH</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT ASSESS TX PLAN OF</strong></p>
<p><strong>or</strong></p>
<p><strong>HT ASSESS TX PLAN OFC</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT VISIT TC</strong></p>
<p><strong>or</strong></p>
<p><strong>HT VISIT PHONE</strong></p>
<p><strong>or</strong></p>
<p><strong>HT VISIT PH</strong></p>
</blockquote></td>
<td><blockquote>
<p>Prog. Dep Phone Code</p>
</blockquote></td>
<td><blockquote>
<p>685</p>
</blockquote></td>
<td colspan="3" rowspan="3"><blockquote>
<p><strong>FIRST, select the HT Clinic Location (left) where the visit is taking place:</strong></p>
</blockquote>
<ol type="a">
<li><p><strong>By telephone (TC, Phone, PH)</strong></p></li>
<li><blockquote>
<p><strong>In the office (OFC)</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>At the patient's home (HM)</strong></p>
</blockquote></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT VISIT OFC</strong></p>
</blockquote></td>
<td><blockquote>
<p>Prog. Dep Clinic Code</p>
</blockquote></td>
<td><blockquote>
<p>685</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT VISIT HM</strong></p>
</blockquote></td>
<td><blockquote>
<p>118 or HBPC</p>
<p>code</p>
</blockquote></td>
<td><blockquote>
<p>685</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="5"><blockquote>
<p><strong>SECOND, select a Note Title/Template (right) to pair with the clinic location (above)</strong></p>
</blockquote></th>
<th><blockquote>
<p>HT</p>
<p>Discharge Note</p>
</blockquote></th>
<th><blockquote>
<p>HT</p>
<p>Discharge Template</p>
</blockquote></th>
<th><blockquote>
<p>This Document contains closure of the patients’ case and discharge from the HT program. Basically, this note is a discharge summary.</p>
<p>NOTE: Designed to facilitate closing the case of a HT patient. May have an encounter attached to it if the discharge is done by telephone or office visit. Will not have an encounter if patient is not</p>
<p>present.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>HT Note</p>
</blockquote></th>
<th><blockquote>
<p>N/A</p>
</blockquote></th>
<th><blockquote>
<p>Generic Note title to encompass all other HT activities. Select documentation templates from</p>
<p>the template drawer.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>HT Periodic Evaluation Note</p>
</blockquote></th>
<th><blockquote>
<p>HT Periodic Evaluation Template</p>
</blockquote></th>
<th><blockquote>
<p>Periodic review and upgrade of the plan of care</p>
<p>NOTE: Summarization of care for a period of time. Interval dependent on VISN/Program.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>HT</p>
<p>Continuum of Care Note</p>
</blockquote></th>
<th><blockquote>
<p>HT</p>
<p>Continuum of Care Template</p>
</blockquote></th>
<th><blockquote>
<p>Note title to be used with the Continuum of Care clinical reminder dialog</p>
<p>NOTE: Initial CCF will be included in the Assessment</p>
<p>Treatment Plan template. This note title to be used thereafter.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>HT</p>
<p>Caregiver Assessment</p>
</blockquote></th>
<th><blockquote>
<p>HT</p>
<p>Caregiver Assessment Template</p>
</blockquote></th>
<th><blockquote>
<p>NOTE: Will combine both the High-risk Screen &amp; referral for assistance in one note title and</p>
<p>template.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Appendix F: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Re-Install

> Select Installation \<TEST ACCOUNT\> Option: 2 Verify Checksums in Transport Global

> Select INSTALL NAME: HT TEMPLATES PROJECT 1.0 3/6/17@10:42:25

> =\> HT TEMPLATES 1.0 ;Created on Mar 06, 2017@08:31:06

> This Distribution was loaded on Mar 06, 2017@10:42:25 with header of HT TEMPLATES 1.0 ;Created on Mar 06, 2017@08:31:06

> It consisted of the following Install(s):

> HT TEMPLATES PROJECT 1.0 TIU\*1.0\*258 PXRM\*2.0\*19 GMTS\*2.7\*98

> Want each Routine Listed with Checksums: Yes// YES DEVICE: HOME// HOME

> PACKAGE: HT TEMPLATES PROJECT 1.0 Mar 06, 2017 10:42 am PAGE 1

> 0 Routine checked, 0 failed.

> PACKAGE: TIU\*1.0\*258 Mar 06, 2017 10:42 am PAGE 1

> TIUP258 Calculated 103966494

> TIUP258E Calculated 39956358

> 2 Routines checked, 0 failed.

> PACKAGE: PXRM\*2.0\*19 Mar 06, 2017 10:42 am PAGE 1

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 37%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PXRMCCHT</p>
</blockquote></th>
<th><blockquote>
<p>Calculated</p>
</blockquote></th>
<th>24334245</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PXRMHTED</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>4905599</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMP19A</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>50240117</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMP19B</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>106974297</td>
</tr>
<tr class="even">
<td><blockquote>
<p>PXRMP19E</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>1345736</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRMP19I</p>
</blockquote></td>
<td><blockquote>
<p>Calculated</p>
</blockquote></td>
<td>48601801</td>
</tr>
</tbody>
</table>

> 6 Routines checked, 0 failed.

> PACKAGE: GMTS\*2.7\*98 Mar 06, 2017 10:42 am PAGE 1

> GMTSP98E Calculated 5307666

> GMTSPI98 Calculated 14297806

> 2 Routines checked, 0 failed.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s) Select INSTALL NAME: HT TEMPLATES PROJECT 1.0 3/6/17@10:42:25

> =\> HT TEMPLATES 1.0 ;Created on Mar 06, 2017@08:31:06

> This Distribution was loaded on Mar 06, 2017@10:42:25 with header of HT TEMPLATES 1.0 ;Created on Mar 06, 2017@08:31:06

> It consisted of the following Install(s):

> HT TEMPLATES PROJECT 1.0 TIU\*1.0\*258 PXRM\*2.0\*19 GMTS\*2.7\*98

> Checking Install for Package HT TEMPLATES PROJECT 1.0 Install Questions for HT TEMPLATES PROJECT 1.0

> Checking Install for Package TIU\*1.0\*258

> Will first run the Environment Check Routine, TIUP258E Verifying installation environment...

> Checking for existing document classes...

> Document class found: CARE COORDINATION HOME TELEHEALTH NOTES Document class check complete.

> Now checking for any local titles that may conflict with new national titles. Local title check complete. No conflicts found.

> Environment check complete. Install will proceed.

> Install Questions for TIU\*1.0\*258

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// Checking Install for Package PXRM\*2.0\*19

> Install Questions for PXRM\*2.0\*19 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// Checking Install for Package GMTS\*2.7\*98

> Will first run the Environment Check Routine, GMTSP98E Verifying installation environment...

> Verification complete; environment check passed Install Questions for GMTS\*2.7\*98

> Incoming Files:

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// ;;999 HOME

> Install Started for HT TEMPLATES PROJECT 1.0 :

> Mar 06, 2017@10:44:28

> Build Distribution Date: Mar 06, 2017 Installing Routines:

> Mar 06, 2017@10:44:28

> Install Started for TIU\*1.0\*258 :

> Mar 06, 2017@10:44:28

> Build Distribution Date: Mar 06, 2017 Installing Routines:

> Mar 06, 2017@10:44:28

> Running Pre-Install Routine: PRE^TIUP258 Preparing HT Document Class & Titles for Update...

> Inactivating CARE COORDINATION HOME TELEHEALTH NOTES.

> Renaming document class CARE COORDINATION HOME TELEHEALTH NOTES as HOME TELEHEALTH NOTES.

> Inactivating HT SCREENING CONSULT. Inactivating HT INTERVENTION NOTE. Inactivating HT SUMMARY OF EPISODE NOTE. Inactivating HT DISCHARGE NOTE. Inactivating HT VIDEO VISIT NOTE.

> Inactivating HT ASSESSMENT TREATMENT PLAN NOTE. Inactivating HT CAREGIVER ASSESSMENT NOTE.

> Inactivating HT CONTINUUM OF CARE NOTE. Inactivating CCHT NOTE.

> Inactivating HT PERIODIC EVALUATION NOTE.

> Inactivating HT TECH EDUCATION NOTE. Inactivating HT TELEPHONE CASE MANAGEMENT NOTE.

> Renaming CCHT NOTE as HT NOTE.

> Installing PACKAGE COMPONENTS:

> Installing PRINT TEMPLATE Installing SORT TEMPLATE Installing OPTION

> Mar 06, 2017@10:44:29

> Running Post-Install Routine: POST^TIUP258 HT SCREENING CONSULT successfully installed HT INTERVENTION NOTE successfully installed

> HT SUMMARY OF EPISODE NOTE successfully installed HT DISCHARGE NOTE successfully installed

> HT VIDEO VISIT NOTE successfully installed

> HT ASSESSMENT TREATMENT PLAN NOTE successfully installed HT CAREGIVER ASSESSMENT NOTE successfully installed

> HT CONTINUUM OF CARE NOTE successfully installed HT NOTE successfully installed

> HT PERIODIC EVALUATION NOTE successfully installed HT TECH EDUCATION NOTE successfully installed

> HT TELEPHONE CASE MANAGEMENT NOTE successfully installed Attempting to map HT titles to VHA Enterprise Standard Titles...

> Reindexing TIU Titles......

> Updating Routine file...

> The following Routines were created during this install: TIUCTP

> TIUCTM

> Updating KIDS files...

> TIU\*1.0\*258 Installed.

> Mar 06, 2017@10:44:30

> Not a production UCI NO Install Message sent

> Install Started for PXRM\*2.0\*19 :

> Mar 06, 2017@10:44:30

> Build Distribution Date: Mar 06, 2017 Installing Routines:

> Mar 06, 2017@10:44:30

> Running Pre-Install Routine: PRE^PXRMP19I DISABLE options.

> DISABLE protocols.

> Attempting to rename CCHT Health Factors... Installing Data Dictionaries:

> Mar 06, 2017@10:44:32

> Installing Data:

> Mar 06, 2017@10:44:33

> Installing PACKAGE COMPONENTS:

> Installing OPTION

> Mar 06, 2017@10:44:33

> Running Post-Install Routine: POST^PXRMP19I ENABLE options.

> ENABLE protocols.

> Preparing to install Reminder Exchange entry VA-HT PROJECT. This is a very large entry that installs numerous components. Installation of this entry will take 10-15 minutes.

> There are 3 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry TIU TEMPLATE URL FIX
2.  Installing Reminder Exchange entry VA-HT EDUCATION TOPICS
3.  Installing Reminder Exchange entry VA-HT PROJECT

> The post-install will generate a single MailMan message: LOCAL CCHT HFs NOT USED IN NAT'L HT CLIN REMINDER CONTENT

> The installer is strongly encouraged to include the site's local Clinical Reminders support/configuration personnel/mail group as recipients.

> Send mail to: THOMPSON,WILLIAM// THOMPSON,WILLIAM

> Select basket to send to: IN// And Send to:

> Queueing post-install message... DONE - Task \#1781082

> Checking ORWPCE EXCLUDE HEALTH FACTORS at the SYSTEM level for each HT Health Factor Category

> Parameter set for HT (HOME TELEHEALTH) Parameter set for HT CONTINUUM OF CARE (CCF)

> Checking TIU TEMPLATE REMINDER DIALOGS at the SYSTEM level

> Setting Data Fields for TIU-HS Objects Setting Data Fields Complete

> Updating Routine file... Updating KIDS files...

> PXRM\*2.0\*19 Installed.

> Mar 06, 2017@10:55:50

> Not a production UCI NO Install Message sent

> Install Started for GMTS\*2.7\*98 :

> Mar 06, 2017@10:55:50

> Build Distribution Date: Mar 06, 2017 Installing Routines:

> Mar 06, 2017@10:55:50

> Running Pre-Install Routine: PRE^GMTSPI98 Installing Data Dictionaries:

> Mar 06, 2017@10:55:50

> Installing Data:

> Mar 06, 2017@10:55:50

> Running Post-Install Routine: POST^GMTSPI98

> 1\. Installing Reminder Exchange entry VA-HT REMOTE HEALTH SUMMARY TYPES Updating Routine file...

> Updating KIDS files...

> GMTS\*2.7\*98 Installed.

> Mar 06, 2017@10:55:51

> Not a production UCI NO Install Message sent

> Updating Routine file... Updating KIDS files...

> HT TEMPLATES PROJECT 1.0 Installed.

> Mar 06, 2017@10:55:51

> No link to PACKAGE file

GMTS\*2.7\*98

> Install Completed

### Appendix G: FileMan Searches for HT Pilot Sites 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>OVERVIEW</u>

> This information is for reference/use by Clinical Application Coordinator(s) (CACs) at sites that participated in the CCHT Templates Project pilot program. The nationally released version of these templates (HT Templates Project 1.0: TIU\*1\*258, PXRM\*2.0\*19, GMTS\*2.7\*98) will install a complete template set. Some files will have entries left over from the pilot program that should be manually cleaned up and/or inactivated. How to handle this cleanup is a local decision.

> The following FileMan search examples can be used at such facilities to identify unused items from the pilot program. Oftentimes, CACs either no longer have FileMan access or do not have access to all the files listed below. In these scenarios, CACs should work with either local or Region-based IT staff to assist with running these searches.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Do not use FileMan to perform edits/renaming of the following file entries. Edits should be done via the proper package options and in the case of GUI templates and/or GUI template fields, the CPRS GUI Template Editor.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> <u>REMINDER TERM</u>

> Search for terms that have “CCHT” or “CARE COORD” in the name. Terms with a CLASS of national cannot be locally edited but any term with a CLASS of VISN or LOCAL can be edited by the site. This search will likely find terms that should not be modified. Use caution when making decisions about which terms to edit.

> Select VA FileMan \<TEST ACCOUNT\> Option: Search File Entries OUTPUT FROM WHAT FILE: BUILD// REMINDER TERM (1009 entries)

> -A- SEARCH FOR REMINDER TERM FIELD: ?

> Answer with FIELD NUMBER, or LABEL

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Choose</p>
</blockquote></th>
<th><blockquote>
<p>from:</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>.01</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NAME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>.04</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DATE CREATED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DESCRIPTION (word-processing)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>FINDINGS (multiple)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>100</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CLASS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>101</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>SPONSOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>102</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REVIEW DATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>110</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>EDIT HISTORY (multiple)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> -A- SEARCH FOR REMINDER TERM FIELD: .01 NAME

> -A- CONDITION: CONTAINS

> -A- CONTAINS: CCHT

> -B- SEARCH FOR REMINDER TERM FIELD: NAME

> -B- CONDITION: CONTAINS

> -B- CONTAINS: CARE COORD

> -C- SEARCH FOR REMINDER TERM FIELD: IF:

> OR:

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>OR:</th>
<th colspan="4" rowspan="2"></th>
</tr>
<tr class="odd">
<th>STORE RESULTS OF SEARCH IN TEMPLATE:</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SORT BY: NAME//</p>
<p>START WITH NAME: FIRST// FIRST PRINT FIELD: NAME THEN PRINT FIELD: CLASS THEN PRINT FIELD:</p>
<p>Heading (S/C): REMINDER TERM SEARCH Replace DEVICE: ;;9999 HOME</p>
<p>REMINDER TERM SEARCH</p></td>
<td><blockquote>
<p>MAY</p>
</blockquote></td>
<td><blockquote>
<p>9,2013</p>
</blockquote></td>
<td><blockquote>
<p>07:48</p>
</blockquote></td>
<td><blockquote>
<p>PAGE 1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>NAME</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>CLASS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VA-GEC CARE COORDINATION COMMENTS</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>NATIONAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CCHT DISCHARGE REASONS</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>VISN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CCHT SUPPRESS FOR AGE &lt;75</td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>VISN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3 MATCHES FOUND.</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> <u>REMINDER DEFINITION</u>

> Search for definitions that have “CCHT” or “CARE COORD” in the name. Definitions with a CLASS of national cannot be locally edited but any definition with a CLASS of VISN or LOCAL can be edited by the site. This search will likely find definitions that should not be modified. Use caution when making decisions about which definitions to edit.

> Select Fileman (VA) \<TEST ACCOUNT\> Option: Search File Entries OUTPUT FROM WHAT FILE: REMINDER DEFINITION//

> -A- SEARCH FOR REMINDER DEFINITION FIELD: NAME

> -A- CONDITION: CONTAINS

> -A- CONTAINS: CARE COOR

> -B- SEARCH FOR REMINDER DEFINITION FIELD: NAME

> -B- CONDITION: CONTAINS

> -B- CONTAINS: CCHT

> -C- SEARCH FOR REMINDER DEFINITION FIELD:

> IF: A NAME CONTAINS (case-insensitive) "CARE COOR" OR: B Or NAME CONTAINS (case-insensitive) "CCHT" OR:

> STORE RESULTS OF SEARCH IN TEMPLATE:

> SORT BY: NAME//

> START WITH NAME: FIRST// FIRST PRINT FIELD: NAME THEN PRINT FIELD: CLASS THEN PRINT FIELD:

> Heading (S/C): REMINDER DEFINITION SEARCH Replace DEVICE: HOME

> REMINDER DEFINITION SEARCH MAY 9,2013 08:12 PAGE 1 NAME CLASS

> VA-GEC REFERRAL CARE COORDINATION NATIONAL

> CCHT NIC CONTINUUM OF CARE LOCAL

> CCHT PERIODIC EVALUATION VISN

> CCHT PERIODIC EVALUATION (VER2) VISN

> 4 MATCHES FOUND.

> <u>REMINDER DIALOG</u>

> Due to the numerous dialog components, site may find it more convenient to use the Reminder Dialog Management menu to locate any LOCAL or VISN reminder dialogs and associated components. This can be done using the Search List feature of dialog management.

> Select Reminder Dialog Management \<TEST ACCOUNT\> Option: DI Reminder Dialogs

> Dialog List May 09, 2013@10:17:12 Page: 1 of 51 REMINDER VIEW (ALL REMINDERS BY NAME)

> Item Reminder Name Linked Dialog Name & Dialog Status

1.  AL LUNG LESION AL LUNG LESION DIALOG
2.  AL RPT HEMOGLOBIN A1C \>9 OR MISSIN
3.  ALBANY DB PT W/LDL \> 99
4.  AVJ DDK HOME OX BAKUP HOME OXYGEN RENEWAL
5.  AVJ HOME OXYGEN RENEWAL HOME OXYGEN RENEWAL
6.  Alcohol Screen(PRL) V2 ALCOHOL SCREEN NEW
7.  BASELINE MEDICAL EVALUATION/V23
8.  BATH ACOVE FALL HISTORY BATH ACOVE FALL HISTORY DIA
9.  BATH ACOVE FUNCTIONAL STATUS REMIN BATH ACOVE KATZ DIALOG
10. BATH ACOVE POSITIVE FALL REMINDER BATH ACOVE POSITIVE FALL HI
11. BATH ACOVE POSITIVE URINARY INCONT BATH ACOVE POSITIVE URINARY
12. BATH ACOVE URINARY INCONTINENCE BATH ACOVE URINARY INCONTIN
13. BATH ALLERGY REMINDER BATH ALLERGY REVIEW DIALOG
14. BATH BRADEN SCALE FOLLOWUP VA-VANOD SKIN REASSESSMENT
15. BATH BRADEN SCALE INITIAL VA-VANOD SKIN INITIAL ASSES
16. BATH BRADEN SCALE INITIAL SCREEN

> \+ Enter ?? for more actions \>\>\>

> AR All reminders LR Linked Reminders QU Quit CV Change View RN Name/Print Name

> Select Item: Next Screen// CV Change View

> Select one of the following:

4.  Reminder Dialogs
5.  Dialog Elements
6.  Forced Values
7.  Dialog Groups

> P Additional Prompts

> R Reminders

> RG Result Group (Mental Health)

> RE Result Element (Mental Health) TYPE OF VIEW: R// D Reminder Dialogs

> Select Item: Next Screen// SL SL Search for: CCHT // CCHT

> Dialog List May 09, 2013@10:19:58 Page: 4 of 26 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)

> +Item Reminder Dialog Name Source Reminder Status

61. CCHT (3 DATA OBJECTS ONLY) \*NONE\*
62. CCHT CONTINUUM OF CARE CCHT NIC CONTINUUM OF CAR Linked
63. CHF DIALOG ZZV2 CHF MANAGEMENT Linked
64. CHF EJECTION FRACTION PROVIDER DIALOG V2 EJECTION FRACTION MISS Linked
65. CHF MEDICAL MANAGEMENT V2 CHF MEDICAL MANAGEMENT Linked
66. CHF NOT ON ACEI NOR BETA BLOCKER ZZTEST CHF NOT ON ACEI NO Linked
67. CHF ON ACEI AND BETA BLOCKER ZZTEST CHF ON ACEI AND BE Linked
68. CHF ON ACEI AND NOT BETA BLOCKER ZZTEST CHF ON ACEI BUT NO Linked
69. CHF ON BETA BLOCKER NOT ON ACEI ZZTEST CHF NOT ON ACEI ON Linked
70. CHF WEIGHT EDUCATION DIALOG V2 CHF WEIGHT EDUCATION
71. CHF WEIGHT EDUCATION DIALOG 2-27-06 V2 CHF WEIGHT EDUCATION Linked
72. CMS SUICIDE ASSESSMENT MH TOOL COL-MH SUICIDE RISK ASSES
73. CN HOME O2 CERTIFICATION DIALOG \*NONE\*
74. CN PAIN PLAN DIALOG CN PAIN PLAN REMINDER Linked
75. CN PAIN SCREEN DIALOG \*NONE\*
76. COLON CA SCREEN DIALOG (2) V2 COLON CANCER SCREEN Linked

> \+ + Next Screen - Prev Screen ?? More Actions \>\>\>

> ...searching for 'CCHT' Find Next 'CCHT'? Yes//

> As unused reminder dialogs are found, these entries can be edited. Entries could have the DISABLED field set, or names could be changed to begin with “ZZ”, which is often used to indicate an unused file entry. How a given site chooses to handle the items that are no longer used (disable, ZZ, etc.) is a local decision.

> Following the example searches above for Reminder Terms and Reminder Definitions, these files can also be searched for CCHT items. Each FileMan file name is listed with the FileMan file number in parentheses. Under each file is the FileMan Field Name(s) with the corresponding FileMan Field Number(s).

> <u>HEALTH SUMMARY TYPE (#142)</u>

> FileMan search of Health Summary Type, looking for:

> NAMEs (.01) that contain “CCHT”, or “CARE COORD” Or, TITLEs (.02) that contain “CCHT”, or “CARE COORD”

> <u>HEALTH SUMMARY OBJECT (#142.5)</u>

> FileMan search of Health Summary Object, looking for:

> NAMEs (.01) that contain “CCHT”, “CARE COORD”

> <u>TIU DOCUMENT DEFINITION (#8925.1)</u>

> FileMan search of TIU Document Definition, looking for:

> NAMEs (.01) that contain “CCHT” or “CARE COORD”

> Or, ABBREVIATIONs (.02) that contain “CCHT” or “CARE COORD”

> Or PRINT NAMEs (.03) that contain “CCHT” or “CARE COORD”

> <u>TIU TEMPLATE (#8927)</u>

> FileMan search of TIU Template, looking for NAMEs (.01) that contain “CCHT”, “CARE COORD” , or use the CPRS GUI Template Editor to find relevant template fields. Any edits must be done via the GUI Template Editor.

> <u>TIU TEMPLATE FIELD (#8927.1)</u>

> FileMan search of TIU Template Field, looking for NAMEs (.01) that contain “CCHT”, “CARE COORD”, or use the CPRS GUI Template Editor to find relevant template fields. Any edits must be done via the GUI Template Editor.

> <u>Pilot Program Reminder Exchange Reference</u>

> Below is the listing of the reminder exchange file used as part of Phase 3 of the CCHT Pilot Program. This information can be used as a guide to help identify items that may no longer be needed after installation of the HT Templates bundle. For example, this listing could be compared with the reminder exchange files distributed with the HT Templates 1.0 software bundle in order to help determine the file entries that may no longer be necessary/in use. The reminder exchange files in HT Templates 1.0 are:

> VA-HT EDUCATION TOPICS VA-HT PROJECT

> VA-HT REMOTE HEALTH SUMMARY TYPES

> Exchange File Components May 23, 2010@11:34

> Component Category Exists- Source:

> Date Packed: 05/23/2010@11:30:47 Package Version: 2.0P12 Description:

> \*\*\*\*\*\*\*\*\*\*\*\*\* BEFORE STARTING THIS INSTALL: \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

- Read the CCHT Templates Pilot CAC Installation Guide
- Build the (3) health summary types - configuration below

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> The following Clinical Reminder items were selected for packing:

> REMINDER DIALOG

> CCHT DISCHARGE TEMPLATE CCHT VIDEO VISIT TEMPLATE

> CCHT TECH EDUCATION TEMPLATE CCHT CONTINUUM OF CARE TEMPLATE CCHT SCREENING CONSULT TEMPLATE

> CCHT PERIODIC EVALUATION TEMPLATE

> CCHT ASSESSMENT TREATMENT PLAN TEMPLATE CCHT CAREGIVER ASSESSMENT TEMPLATE

> CCHT TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS CCHT INTERVENTION TEMPLATE

> CCHT (3 DATA OBJECTS ONLY)

> REMINDER DEFINITION

> CCHT BL SCREENING CONSULT CCHT BL TECH EDUCATION CCHT PERIODIC EVALUATION

> CCHT CONTINUUM OF CARE (FOLLOW-UP) CCHT CONTINUUM OF CARE (INITIAL) CCHT CAREGIVER/VETERAN REFERRAL CCHT CAREGIVER RISK ASSESSMENT

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> DEPRESSION REMINDER STATUS Health Summary type:

> For the HEALTH SUMMARY TYPE "DEPR REMINDER STATUS", you will need to ADD your site's SELECTION ITEM for your DEPRESSION SCREEN clinical reminder. Use this for the configuration:

> Create/Modify Health Summary Type

> Select Health Summary Type: DEPR REMINDER STATUS (OBJ) TITLE: Depression reminder status

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> LOCK:

> Select component: REMINDERS DUE

> SUMMARY ORDER: 5// 5

> HEADER NAME: Reminders Due//

> Select SELECTION ITEM: VI-20 DEPR

> Searching for a CLINICAL REMINDER/MAINTENANCE VI-20 DEPRESSION SCREENING (v09.1.1) VISN

> ...OK? Yes// (Yes) Select SELECTION ITEM: \<ENT\> Select COMPONENT: \<ENT\>

> HEMOGLOBIN A1C LAST Health Summary type:

> Use your site's in-house lab test(s) for the selection item for the LAB TEST SELECTED health summary component. If your site uses Health Factors to document OUTSIDE A1c values, add those into the configuration:

> NAME: A1C LAST (OBJ) OWNER: MINER,MAURI N SUPPRESS COMP WITHOUT DATA: yes

> SUMMARY ORDER: 5 COMPONENT NAME: LAB TESTS SELECTED

> OCCURRENCE LIMIT: 1 HEADER NAME: Lab Tests Selected SELECTION ITEM: HEMOGLOBIN A1c

> SUMMARY ORDER: 10 COMPONENT NAME: SELECTED HEALTH FACTORS

> OCCURRENCE LIMIT: 1

> SELECTION ITEM: OUTSIDE A1C LESS THAN 7.0 SELECTION ITEM: OUTSIDE A1C BETWEEN 7.0-9.0 SELECTION ITEM: OUTSIDE A1C BETWEEN 9.1-11.0 SELECTION ITEM: OUTSIDE A1C GREATER THAN 11.0

> SUPPRESS SENSITIVE PRINT DATA: NO SSN

> TITLE: Hemoglobin A1c last

> PULSE OXIMETRY OUTPT LAST Health Summary type:

> NAME: PULSE OX OUTPT LAST(OBJ) OWNER: MINER,MAURI N SUPPRESS COMP WITHOUT DATA: yes

> SUMMARY ORDER: 5

> COMPONENT NAME: VITAL SIGNS SELECTED OUTPAT.

> OCCURRENCE LIMIT: 1 HEADER NAME: Vital Select Outpat.

> SELECTION ITEM: PULSE OXIMETRY SUPPRESS SENSITIVE PRINT DATA: NO SSN

> TITLE: Pulse Oximetry Outpt-last

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Non-exchangeable order dialog(s):

> Name: PSH OERR

> Type: Dialog

> Display Text: Non VA Medications

> Name: GMRCT SOCIAL WORK (SEA)

> Type: Quick Order Display Text: Social Work consult

> Display Group: CONSULTS

> Package: CONSULT/REQUEST TRACKING

> Consult to Service/Specialty: SOC WRK-MEDICINE OUTPT (PCCS)

> Reason for Request: CCHT patient referred for Social Work co ...

> Category: OUTPATIENT Urgency: ROUTINE

> Place of Consultation: Consultant's Choice

> Non-exchangeable TIU object(s):

> TIU Object: PATIENT AGE

> Object Method: S X=\$\$AGE^TIULO(DFN)

> TIU Object: PATIENT DATE OF DEATH

> Object Method: S X=\$\$DOD^TIULO(DFN)

> TIU Object: ALLERGIES/ADR

> Object Method: S X=\$\$MAIN^ARJADR(DFN,0,"^TMP(""TIULADR"",\$J)",0)

> TIU Object: PATIENT HEIGHT

> Object Method: S X=\$\$HEIGHT^TIULO(+\$G(DFN))

> TIU Object: PATIENT WEIGHT

> Object Method: S X=\$\$WEIGHT^TIULO(+\$G(DFN))

> TIU Object: TEMPERATURE

> Object Method: S X=\$\$TEMP^TIULO(+\$G(DFN))

> TIU Object: PULSE

> Object Method: S X=\$\$PULSE^TIULO(+\$G(DFN))

> TIU Object: RESPIRATION

> Object Method: S X=\$\$RESP^TIULO(+\$G(DFN))

> TIU Object: BLOOD PRESSURE

> Object Method: S X=\$\$BP^TIULO(+\$G(DFN))

> TIU Object: ACTIVE MEDICATIONS

> Object Method: S X=\$\$LIST^TIULMED(DFN,"^TMP(""TIUMED"",\$J)",1)

> TIU Object: PAIN

> Object Method: S X=\$\$PAIN^TIULO(+\$G(DFN))

> Keywords:

> Components:

> ROUTINE

> 1 PXRMPDEM X

> LABORATORY TEST

> HEMOGLOBIN A1c X

> ORDER DIALOG

> GMRCT SOCIAL WORK (SEA) X

> PSH OERR X

> GMRV VITAL TYPE

> PULSE OXIMETRY X

> PAIN X

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 1%" />
<col style="width: 72%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>MH</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>TESTS AND SURVEYS</p>
<p>PHQ9</p>
</blockquote></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="2"><blockquote>
<p>PHQ-2</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>TIU</p>
</blockquote></td>
<td>TEMPLATE FIELD</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">2</td>
<td><blockquote>
<p>CCHT W-P4LINES(R)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2">3</td>
<td><blockquote>
<p>CCHT W-P2LINES(R)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2">4</td>
<td><blockquote>
<p>CCHT CHANGE TO PROVIDER-CG/VET</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2">5</td>
<td><blockquote>
<p>CCHT EDIT50</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2">6</td>
<td><blockquote>
<p>CCHT CHANGE TO PROVIDER-CG/VET EMBEDDED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2">7</td>
<td><blockquote>
<p>CCHT SPECIFY</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2">8</td>
<td><blockquote>
<p>CCHT OTHER</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2">9</td>
<td><blockquote>
<p>CCHT NEW/USED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>CCHT BL PRESSURE CUFF SIZE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>11</p>
</blockquote></td>
<td><blockquote>
<p>CCHT W-P6LINES(R)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>CCHT W-P6LINES</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>13</p>
</blockquote></td>
<td><blockquote>
<p>CCHT VITAL SIGNS MODE</p>
</blockquote></td>
<td>X</td>
</tr>
</tbody>
</table>

> EDUCATION TOPICS

14. HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT X
15. HOME TELEHEALTH-MEDICATION MANAGEMENT X
16. HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT X
17. HOME TELEHEALTH-IN HOME MONITORING X

> HEALTH FACTORS

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 8%" />
<col style="width: 15%" />
<col style="width: 19%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>18</p>
</blockquote></th>
<th><blockquote>
<p>CCHT</p>
</blockquote></th>
<th colspan="5"><blockquote>
<p>TEMPLATE USE (PHASE 3)</p>
</blockquote></th>
<th>X</th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>19</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>INTERVENTION TEMPLATE USED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>20</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CONTINUUM OF CARE</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>21</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CCF MEETS CCM CRITERIA</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CCF FOLLOW-UP ASSESSMENT DONE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>23</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CCF MEETS NIC CRITERIA</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>24</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>25</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>PERIODIC EVALUATION DONE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>(CARE COORDINATION HOME TELEHEALTH)</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>ENROLLMENT-START DATE (PREV ENROLL)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>ENROLLMENT-START DATE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>PREVIOUSLY ENROLLED TEMPLATE USED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CCF CAREGIVER-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CCF CAREGIVER-FRIEND/NEIGHBOR</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>32</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CCF CAREGIVER-CHILD</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>33</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CCF CAREGIVER-SPOUSE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>34</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>CCF CAREGIVER'S NAME</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCREEN</p>
</blockquote></td>
<td></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>36</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td><blockquote>
<p>16</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>37</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>15</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>14</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>13</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>40</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>12</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>41</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>11</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>42</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>10</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>43</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>9</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>44</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>8</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>45</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>7</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>46</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>6</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>47</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>5</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>48</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>4</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>3</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>2</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>1</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>52</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td><blockquote>
<p>RISK</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>SCORE</p>
</blockquote></td>
<td>0</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>53</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>ASSESSMENT SCREEN DONE</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>54</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>UNCERTAIN</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>WHAT TO DO=NEARLY ALWAYS</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>55</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>UNCERTAIN</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>WHAT TO DO=FREQUENTLY</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>56</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>UNCERTAIN</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>WHAT TO DO=SOMETIMES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>57</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>UNCERTAIN</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>WHAT TO DO=RARELY</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>58</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>UNCERTAIN</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>WHAT TO DO=NEVER</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>59</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED</p>
</blockquote></td>
<td colspan="4">WITH RELATIVES=NRLY ALWAYS</td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>60</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED</p>
</blockquote></td>
<td colspan="4">WITH RELATIVES=FREQUENTLY</td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>61</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED</p>
</blockquote></td>
<td colspan="4">WITH RELATIVES=SOMETIMES</td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>62</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED</p>
</blockquote></td>
<td colspan="4">WITH RELATIVES=RARELY</td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>63</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRAINED</p>
</blockquote></td>
<td colspan="4">WITH RELATIVES=NEVER</td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>64</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED</p>
</blockquote></td>
<td colspan="4">WORK/FAMILY=NEARLY ALWAYS</td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>65</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED</p>
</blockquote></td>
<td colspan="4">WORK/FAMILY=FREQUENTLY</td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>66</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED</p>
</blockquote></td>
<td colspan="4">WORK/FAMILY=SOMETIMES</td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>67</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED</p>
</blockquote></td>
<td colspan="4">WORK/FAMILY=RARELY</td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>68</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>STRESSED</p>
</blockquote></td>
<td colspan="4">WORK/FAMILY=NEVER</td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>69</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>MAKE TIME FOR SELF=NEARLY ALWAYS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>70</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>MAKE TIME FOR SELF=FREQUENTLY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>71</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>MAKE TIME FOR SELF=SOMETIMES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>72</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>MAKE TIME FOR SELF=RARELY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>73</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>MAKE TIME FOR SELF=NEVER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>74</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>C/G RISK SCREEN TEMPLATE USED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>75</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>REFERRALS FOR VETERAN/CAREGIVER</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>76</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL SOCIAL WORK</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>77</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL HOSPICE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>78</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL SVCS IN PLACE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>79</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>80</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>81</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL NURS HOME PLACEMNT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>82</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL HOUSING</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>83</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL ADULT DAY CARE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>84</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL RESPITE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>85</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL HOMEMKR/CHORE ASST</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>86</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL HOME HEALTH SVC</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>87</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="5"><blockquote>
<p>VETERAN REFERRAL TRANSPORTATION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 57%" />
<col style="width: 19%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>88</th>
<th><blockquote>
<p>CCHT</p>
</blockquote></th>
<th><blockquote>
<p>VETERAN REFERRAL EMPLOYMENT ASSIST</p>
</blockquote></th>
<th></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>89</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VETERAN REFERRAL FINANCIAL ASSIST</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>90</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VETERAN REFERRAL LEGAL ASSIST</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>91</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VETERAN REFERRAL MEDICAL EVAL, F/U</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>92</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VETERAN REFERRAL FAMILY COUNSEL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>93</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VETERAN REFERRAL INDIVIDUAL COUNSEL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>94</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VETERAN REFERRAL OTHER SERVICE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>95</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VETERAN REFERRAL EDUC/TRAINING</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>96</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL SVCS IN PLACE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>97</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>98</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>99</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL BEREAVE SUPPORT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>100</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL OTHER SERVICE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>101</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL MEDICAL EVAL,F/U</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>102</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL EDUC/TRAINING</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>103</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL C/G SUPPORT GRP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>104</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL FAMILY COUNSEL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>105</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER REFERRAL INDIVID COUNSEL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>106</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CG/VETERAN REFERRAL TEMPLATE DONE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>107</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CG/VETERAN REFERRAL TEMPLATE USED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>108</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td>109</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PT/CG REQUEST DC SERVICES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>110</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO NEW LOCATION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>111</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO MENTAL HEALTH</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>112</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO SOCIAL WORK</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>113</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO PRIMARY CARE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>114</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-REFERRED TO HOSPICE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>115</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PATIENT IS DECEASED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>116</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PHONE,ELECT SVCS UNAVAIL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>117</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-NO VA PRIMARY CARE SVCS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>118</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ADMITTED TO NURSING HOME</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>119</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-RELOCATED OUT OF SVC AREA</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>120</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-UNABLE TO OPERATE DEVICES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>121</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-HAS MET GOALS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>122</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>ENROLLMENT-ENDING DATE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>123</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF UNPAID CAREGIVER-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>124</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DOES NOT MEET CCM CRITERIA</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>125</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF INITIAL ASSESSMENT DONE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>126</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DOES NOT MEET NIC CRITERIA</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>127</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER ASSESSMENT TEMPLATE USED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>128</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PLAN-MED DISCREP SENT TO PROVIDER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>129</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PLAN-REVIEWED LIST CURRENT MEDS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>130</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG HAS QUESTIONS ON MEDS-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>131</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG HAS QUESTIONS ON MEDS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>132</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG HAS LIST OF ACTIVE MEDS-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>133</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG HAS LIST OF ACTIVE MEDS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>134</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>GETS MEDS VIA NON-VA PROVIDER-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>135</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>GETS MEDS VIA NON-VA PROVIDER-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>136</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEDS ADAPTATIONS-NONE NEEDED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>137</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEDS ADAPTATIONS-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>138</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEDS ADAPT-FOR VISUAL IMPAIRMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>139</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEDS ADAPT-VA PREPARES/POURS MEDS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>140</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEDS ADAPT-MEDS ARE COLOR CODED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>141</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEDS ADAPT-USES PILLBOX</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>142</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEDS SPECIAL ADAPTATIONS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>143</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG TAKES MEDS AS PRESCRIBED-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>144</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG TAKES MEDS AS PRESCRIBED-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>145</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG KNOWS REFILL PROCESS-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>146</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG KNOWS REFILL PROCESS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>147</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG KNOWS MED SIDE EFF-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>148</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG KNOWS MED SIDE EFFECTS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>149</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG KNOWS MED INDICATIONS-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>150</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PT/CG KNOWS MED INDICATIONS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>151</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>LEARNING BARRIER-VISUALLY IMPAIRED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>152</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>LEARNING BARRIER-LANGUAGE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>153</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>LEARNING BARRIER-UNABLE TO READ</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>154</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>LEARNING BARRIER-NONE IDENTIFIED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td>155</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CLINICAL REASON FOR ENROLLMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>156</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td>157</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td>158</td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-SUBST ABUSE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 58%" />
<col style="width: 19%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>159</p>
</blockquote></th>
<th><blockquote>
<p>CCHT</p>
</blockquote></th>
<th><blockquote>
<p>DISEASE INDICATIONS-HYPERTENSION</p>
</blockquote></th>
<th></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>160</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-PTSD</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>161</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-DEPRESSION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>162</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-DIABETES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>163</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-COPD</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>164</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISEASE INDICATIONS-CHF</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>165</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF 12 OR MORE CLINIC STOPS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>166</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIVES ALONE IN COMMUNITY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>167</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF AGE 75 OR GREATER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>168</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PROBLEMS WITH 3 OR MORE IADL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>169</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF 2 OR MORE ADL DEFICITS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>170</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MEETS NIC CATEGORY B CRITERIA</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>171</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF LIFE EXPECTANCY &lt; 6 MO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>172</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF 1 OR MORE BEHAV/COGN PROBLEMS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>173</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PROBLEMS IN 3 OR MORE ADLS</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>174</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MEETS NIC CATEGORY A CRITERIA</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>175</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF NIC CRITERIA NO-HLTH PROMOTION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>176</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF NIC CRITERIA NO-ACUTE CARE MGMT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>177</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF COMPLEXITY TOO GREAT-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>178</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF SERVICES IN PLACE-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>179</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF SERVICES IN PLACE-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>180</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF RECOMMEND REFERRAL-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>181</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF RECOMMEND REFERRAL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>182</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF COMPLEXITY TOO GREAT-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>183</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF POTENTIAL FOR INCR INDEP-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>184</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF POTENTIAL FOR INCR INDEP-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>185</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF FLARE UP CHRONIC CONDITION-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>186</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF FLARE UP CHRONIC CONDITION-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>187</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>RECENT CHANGE IN FUNCTION-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>188</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>RECENT CHANGE IN FUNCTION-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>189</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF AGITATED/DISORIENTED-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>190</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF AGITATED/DISORIENTED-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>191</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DIFFIC MAKE SELF UNDERSTOOD-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>192</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DIFFIC MAKE SELF UNDERSTOOD-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>193</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DIFFIC REASONABLE DECISIONS-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>194</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DIFFIC REASONABLE DECISIONS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>195</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF RESISTING CARE-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>196</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF RESISTING CARE-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>197</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PHYSICALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>198</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PHYSICALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>199</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF VERBALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>200</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF VERBALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>201</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF WANDERING-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>202</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF WANDERING-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>203</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PTSD/OTHER ANXIETY-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>204</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF PTSD/OTHER ANXIETY-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>205</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF SUBST ABUSE/DEPENDENCE-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>206</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF SUBST ABUSE/DEPENDENCE-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>207</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MOOD DISORDER MANIC-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>208</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MOOD DISORDER MANIC-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>209</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MOOD DISORDER DEPRESSION-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>210</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF MOOD DISORDER DEPRESSION-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>211</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DELUSIONS-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>212</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF DELUSIONS-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>213</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-TACTILE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>214</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-OLFACTORY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>215</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-VISUAL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>216</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-AUDITORY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>217</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-SENSORY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>218</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF HALLUCINATIONS-NONE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>219</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>REFERRAL IADL</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>220</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>RECENT CHANGE IN IADL FX-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>221</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>RECENT CHANGE IN IADL FX-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>222</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY MNG FINANCES/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>223</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY MNG FINANCES/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>224</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY MANAGING MEDS/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>225</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY MANAGING MEDS/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>226</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY USING PHONE/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>227</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY USING PHONE/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>228</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULT TRANSPORTATION/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>229</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULT TRANSPORTATION/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 58%" />
<col style="width: 19%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>230</p>
</blockquote></th>
<th><blockquote>
<p>GEC</p>
</blockquote></th>
<th>DIFFICULTY WITH SHOPPING/LAST 7D-NO</th>
<th></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>231</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY WITH SHOPPING/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>232</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY W/ HOUSEWORK/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>233</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY W/ HOUSEWORK/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>234</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>MEALS PREPARED BY OTHERS/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>235</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>MEALS PREPARED BY OTHERS/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>236</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY PREPARE MEALS/LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>237</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DIFFICULTY PREPARE MEALS/LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>238</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT MNG FINANCES/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>239</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT MNG FINANCES/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>240</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT MANAGING MEDS/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>241</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT MANAGING MEDS/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>242</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT USING PHONE LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>243</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT USING PHONE LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>244</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT TRANSPRTATION/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>245</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT TRANSPRTATION/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>246</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT WITH SHOPPING/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>247</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT WITH SHOPPING/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>248</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT W/ HOUSEWORK/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>249</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT W/ HOUSEWORK/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>250</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEALS PREPARED BY OTHER/LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>251</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MEALS PREPARED BY OTHER/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>252</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DIFFICULT PREPARE MEALS/LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>253</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>REFERRAL BASIC ADL</td>
<td><blockquote>
<p>X</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>254</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>RECENT CHANGE IN ADL FX-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>255</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>RECENT CHANGE IN ADL FX-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>256</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>INDEPENDENT IN WC LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>257</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>INDEPENDENT IN WC LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>258</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>MOVING AROUND INDOORS LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>259</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>MOVING AROUND INDOORS LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>260</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>TRANSFERS HELP/SPRVISION LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>261</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>TRANSFERS HELP/SPRVISION LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>262</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>BED POSITIONING HELP LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>263</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>BED POSITIONING HELP LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>264</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>TOILET HELP/SUPERVISION LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>265</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>TOILET HELP/SUPERVISION LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>266</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>EATING HELP/SUPERVISION LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>267</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>EATING HELP/SUPERVISION LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>268</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DRESS HELP/SUPERVISION LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>269</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>DRESS HELP/SUPERVISION LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>270</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>BATHING PHYS ASST NEEDED LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>271</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>BATHING PHYS ASST NEEDED LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>272</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>BATHING HELP/SUPERVISION LAST 7D-NO</td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>273</p>
</blockquote></td>
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td>BATHING HELP/SUPERVISION LAST 7D-YES</td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>274</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>W/C MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>275</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>W/C MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>276</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DRESSING HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>277</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DRESSING HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>278</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>BATHING HELP/SUPRVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>279</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>BATHING HELP/SUPRVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>280</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MOVE INDOOR HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>281</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>MOVE INDOOR HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>282</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TRANSFERS HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>283</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TRANSFERS HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>284</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>BED MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>285</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>BED MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>286</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TOILET HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>287</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TOILET HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>288</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EATING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>289</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EATING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>290</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF UNPAID CAREGIVER-NO</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>291</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER CAN'T INCREASE HELP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>292</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER CAN INCREASE HELP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>293</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER NOT ACCESSIBLE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>294</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER ACCESSIBLE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>295</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-IADL HELP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>296</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-ADL HELP</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>297</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER-EMOTIONAL SUPPORT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>298</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER'S PHONE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>299</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER'S ZIP CODE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>300</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF CAREGIVER'S STATE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 52%" />
<col style="width: 19%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>301</p>
</blockquote></th>
<th><blockquote>
<p>CCHT</p>
</blockquote></th>
<th><blockquote>
<p>CCF</p>
</blockquote></th>
<th><blockquote>
<p>CAREGIVER'S CITY</p>
</blockquote></th>
<th colspan="2">X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>302</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER'S STREET ADDRESS</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>303</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER LIVES WITH PT-NO</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>304</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER SAME NAME AS PT</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>305</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER LIVES WITH PT-YES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>306</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES HOMELESS SHELTER</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>307</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES HOMELESS</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>308</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES AT OTHER</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>309</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES DOMICILIARY</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>310</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES NURSING HOME</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>311</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES BOARD AND CARE</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>312</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES PRIVATE HOME</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>313</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES WITH OTHER</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>314</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>GROUP SETTING NON RELATIVES</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>315</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES WITH ADULT CHILD</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>316</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES WITH CHILD</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>317</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES WITH SPOUSE &amp; OTHERS</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>318</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES WITH SPOUSE ONLY</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>319</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CCF</p>
</blockquote></td>
<td><blockquote>
<p>LIVES ALONE</p>
</blockquote></td>
<td colspan="2">X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>320</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CONT OF CARE(EMBEDDED)TEMPLATE USED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>321</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EMERG PRIORITY LOW-HAS RESOURCES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>322</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EMERG PRIORITY MOD-SVCS AFTER 3-7D</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>323</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EMERG PRIORITY HIGH-IMMEDIATE EVAL</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>324</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ASSESSMENT TX PLAN TEMPLATE USED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>325</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CG/VETERAN REFERRAL(S) NOT UTILIZED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>326</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>REFERRALS CAREGIVER NOT SATISFIED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>327</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>REFERRALS CAREGIVER SATISFIED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>328</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CATEGORY-TELEPHONE CASE MANAGEMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>329</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CATEGORY-HEALTH PROMOTION</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>330</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CATEGORY-CHRONIC CARE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>331</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CATEGORY-ACUTE CARE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>332</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CATEGORY-NON INSTITUTIONAL CARE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>333</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>VETERAN'S GOAL FOR ENROLLMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>334</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PERIODIC EVAL DIALOG/TEMPLATE USED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>335</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>TELEHEALTH DEVICE(S)</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>336</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING/MONITORING TYPE/SERIAL #</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>337</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>VIDEOPHONE SERIAL #</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>338</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING DEVICE TYPE/SERIAL #</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>339</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>DIGITAL CAMERA SERIAL #</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>340</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></td>
<td>X</td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>341</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>APPROX DELIVERY DATE FOR EQUIPMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>342</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EQUIP MAILED,INSTALL BY VET/CAREGVR</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>343</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EQUIP TAKEN HOME,INSTALL BY VET/CG</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>344</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EQUIP INSTALLATION MODE-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>345</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EQUIP INSTALLED BY CONTRACT VENDOR</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>346</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>EQUIP INSTALLED BY CARE COORDINATOR</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>347</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING/MONITORING-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>348</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING/MONITORING-SPIROMETRY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>349</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING/MONITORING-WEIGHT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>350</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING/MONITORING-PULSE OXIMETRY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>351</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING/MONITORING-PULSE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>352</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING/MONITORING-BLOOD GLUCOSE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>353</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING/MONITORING-BLOOD PRESSURE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>354</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PERIPHERALS-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>355</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PERIPHERALS-GLUCOSE CABLES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>356</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PERIPHERALS-SPIROMETRY (SERIAL #)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>357</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PERIPHERALS-STETHOSCOPE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>358</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PERIPHERALS-BP CUFF (SERIAL #)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>359</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PERIPHERALS-PULSE OX (SERIAL #)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>360</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PERIPHERALS-WEIGHT SCALE (SERIAL #)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>361</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PERIPHERALS-NONE NEEDED</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>362</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING DEVICE-PULSE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>363</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MEASURING DEVICE-OTHER</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>364</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING DEVICE-WEIGHT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>365</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING DEVICE-PULSE OXIMETRY</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>366</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING DEVICE-BLOOD GLUCOSE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>367</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MESSAGING DEVICE-BLOOD PRESSURE</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>368</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MEETS TELEHEALTH CRITERIA(YES)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>369</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>REASON FOR NON-ENROLLMENT</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>370</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MEETS TELEHEALTH CRITERIA(NO)</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>371</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>PHONE-NO FEATURES</p>
</blockquote></td>
<td></td>
<td>X</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 65%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>372</p>
</blockquote></th>
<th><blockquote>
<p>CCHT</p>
</blockquote></th>
<th><blockquote>
<p>PHONE-DSL LINE</p>
</blockquote></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>373</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PHONE-MODEM</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>374</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-HX HOSPITALIZATONS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>375</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-DISTANCE (HOURS)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>376</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-DISTANCE (MILES)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>377</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-# OUTPT VISITS PAST YR</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>378</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INDICATIONS-HX HIGH COST/HIGH USE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>379</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TELEHEALTH COORDINATOR (NAME)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>380</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>SCREENING CONSULT TEMPLATE USED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>381</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>REFERRAL-CONSULT COMPLETION</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>382</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CONT OF CARE TITLE/TEMPLATE USED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>383</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EQUIP INSTALLED BY VETERAN/CAREGVR</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>384</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EQUIP INSTALLED BY SUPPORT STAFF</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>385</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EDUC ON EQUIP-CARE COORDINATOR</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>386</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EDUC ON EQUIP-SUPPORT STAFF</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>387</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>EDUC ON EQUIP-CONTRACT VENDOR</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>388</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TECH EDUCATION TEMPLATE USED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>389</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VIDEO VISIT-AUDIO/VIDEO CONNECTION</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>390</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VIDEO VISIT TEMPLATE USED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>391</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-OTHER FOLLOW-UP</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>392</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-EQUIP RETURN (OTHER)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>393</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CONTACT MADE FOR EQUIP RETURN</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>394</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ALL EQUIP RETURNED (NO)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>395</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ALL EQUIP RETURNED (YES)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>396</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ALL ISSUES ADDRESSED(NO)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>397</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-ALL ISSUES ADDRESSED(YES)</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>398</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-NO RESPONSE TO PROGRAM</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>399</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PROVIDER REQUESTS DC</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>400</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE-PROLONGED HOSPITALIZATION</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>401</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE TEMPLATE USED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>402</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CG/VET REFER DIALOG/TEMPLATE USED</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>403</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>C/G RISK ASSESSMENT DIALOG USED</p>
</blockquote></td>
<td>X</td>
</tr>
</tbody>
</table>

> REMINDER SPONSOR

404. CARE COORDINATION HOME TELEHEALTH X
405. Mental Health and Behavioral Science Strategic X Group

> REMINDER COMPUTED FINDINGS

406. VA-AGE X
407. VA-DATE OF DEATH X

> REMINDER TERM

408. CCHT DISCHARGE REASONS X
409. CCHT CAREGIVER ASSESSMENT SCORE 0-7 X
410. CCHT CAREGIVER ASSESSMENT SCORE 8 AND HIGHER X
411. CCHT SUPPRESS FOR AGE \<75 X
412. CCHT DEVICE TYPE ASSIGNED X

> REMINDER DEFINITION

413. CCHT PERIODIC EVALUATION X
414. CCHT CAREGIVER/VETERAN REFERRAL X
415. CCHT CAREGIVER RISK ASSESSMENT X
416. CCHT CONTINUUM OF CARE (FOLLOW-UP) X
417. CCHT CONTINUUM OF CARE (INITIAL) X
418. CCHT BL SCREENING CONSULT X
419. CCHT BL TECH EDUCATION X

> REMINDER DIALOG

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 69%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>420</p>
</blockquote></th>
<th><blockquote>
<p>CCHT</p>
</blockquote></th>
<th><blockquote>
<p>(3 DATA OBJECTS ONLY)</p>
</blockquote></th>
<th>X</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>421</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>INTERVENTION TEMPLATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>422</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TEMPLATE FOR PREVIOUSLY ENROLLED PATIENTS</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>423</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER ASSESSMENT TEMPLATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>424</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>ASSESSMENT TREATMENT PLAN TEMPLATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>425</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>PERIODIC EVALUATION TEMPLATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>426</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>SCREENING CONSULT TEMPLATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>427</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CONTINUUM OF CARE TEMPLATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>428</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>TECH EDUCATION TEMPLATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>429</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>VIDEO VISIT TEMPLATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="even">
<td><blockquote>
<p>430</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>DISCHARGE TEMPLATE</p>
</blockquote></td>
<td>X</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>431</p>
</blockquote></td>
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>CAREGIVER/VETERAN REFERRAL</p>
</blockquote></td>
<td>X</td>
</tr>
</tbody>
</table>

432. CCHT CAREGIVER RISK ASSESSMENT X
433. CCHT CONTINUUM OF CARE (FOLLOW-UP) X
434. CCHT CONTINUUM OF CARE (INITIAL) X

> HEALTH SUMMARY COMPONENT

> CLINICAL REMINDERS DUE X

> VITAL SIGNS SELECTED OUTPAT. X

> LAB TESTS SELECTED X

> PCE HEALTH FACTORS SELECTED X

> NEXT OF KIN X

> CONSULTS BRIEF X

> MAS ADMISSIONS/DISCHARGES X

> MAS CLINIC VISITS PAST X

> HEALTH SUMMARY TYPE

435. DEPR REMINDER STATUS (OBJ) X
436. PULSE OX OUTPT LAST(OBJ) X
437. A1C LAST (OBJ) X
438. CCHT CAREGIVER(OBJ) X
439. NEXT OF KIN(OBJ) X
440. CCHT REMINDERS DUE(OBJ) X
441. CCHT CCF NIC RATING(OBJ) X
442. GEC IADLS (OBJ) X
443. GEC BASIC ADLS(OBJ) X
444. CCHT EMERGENCY LEVELS(OBJ) X
445. CCHT CATEGORY OF CARE(OBJ) X
446. CCHT MED RECON (OBJ) X
447. CCHT VETERAN'S GOAL(OBJ) X
448. CONSULTS PAST(OBJ) X
449. CCHT ENROLLMENT START(OBJ) X
450. ADMISSIONS PAST YR(OBJ) X
451. OUTPT VISITS PAST YR(OBJ) X

> HEALTH SUMMARY OBJECTS

452. DEPRESSION REMINDER STATUS X
453. PULSE OXIMETRY OUTPT LAST X
454. A1C LAST X
455. CCHT CAREGIVER X
456. NEXT OF KIN X
457. CCHT REMINDERS DUE X
458. CCHT CCF NIC RATING LAST X
459. GEC IADLS FOR CCHT X
460. GEC BASIC ADLS X
461. CCHT EMERG LEVELS X
462. CCHT CATEGORY OF CARE X
463. CCHT MED RECON X
464. CCHT VETERAN'S GOAL X
465. CONSULTS PAST X
466. CCHT ENROLLMENT START DATE X
467. ADMISSIONS PAST YR X
468. OUTPT VISITS PAST YR X

> TIU DOCUMENT DEFINITION

469. DEPRESSION REMINDER STATUS X
470. PULSE OXIMETRY OUTPT (LAST) X
471. HEMOGLOBIN A1C (LAST) X
472. CCHT CAREGIVER X
473. NEXT OF KIN X
474. CCHT REMINDERS DUE X

> ALLERGIES/ADR X

> PAIN X

> PATIENT WEIGHT X

> PATIENT HEIGHT X

> BLOOD PRESSURE X

> RESPIRATION X

> PULSE X

> TEMPERATURE X

> ACTIVE MEDICATIONS X

475. CCHT CCF NIC RATING LAST X

PATIENT AGE X

476. GEC IADLS (LAST) X
477. GEC BASIC ADLS (LAST) X
478. CCHT EMERGENCY PRIORITY RATING X
479. CCHT CATEGORY OF CARE X
480. CCHT MED RECON X
481. CCHT VETERAN'S GOAL X
482. CONSULTS PAST X
483. CCHT ENROLLMENT START DATE X
484. ADMISSIONS PAST YR X
485. OUTPT VISITS PAST YR X

> PATIENT DATE OF DEATH X

### Appendix H: Health Factors 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GEC BATHING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></th>
<th><blockquote>
<p>GEC TOILET HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GEC BATHING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC TRANSFERS HELP/SPRVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC BATHING PHYS ASST NEEDED LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>GEC TRANSFERS HELP/SPRVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC BATHING PHYS ASST NEEDED LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT (HOME TELEHEALTH)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC BED POSITIONING HELP LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT ASSESSMENT/TREATMENT PLAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC BED POSITIONING HELP LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT BARRIERS TO LEARNING</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULT TRANSPORTATION/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT BATHING HELP/SUPRVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULT TRANSPORTATION/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT BATHING HELP/SUPRVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY MANAGING MEDS/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT BED MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULTY MANAGING MEDS/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT BED MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY MNG FINANCES/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER ASSESSMENT SCREEN COMPLETED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULTY MNG FINANCES/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL BEREAVE SUPPORT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY PREPARE MEALS/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL C/G SUPPORT GRP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULTY PREPARE MEALS/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL EDUC/TRAINING</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY USING PHONE/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL FAMILY COUNSEL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULTY USING PHONE/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL INDIVID COUNSEL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL MEDICAL EVAL,F/U</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL OTHER SERVICE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY WITH SHOPPING/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL SOCIAL WORK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULTY WITH SHOPPING/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL SVCS IN PLACE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DRESS HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DRESS HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC EATING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER REVIEW OF WRITTEN MATERIALS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC EATING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER RISK ASSESSMENT SCREEN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC INDEPENDENT IN WC LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CAREGIVER STATES ESSENTIAL CONCEPTS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC INDEPENDENT IN WC LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CATEGORY OF CARE-ACUTE CARE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC MEALS PREPARED BY OTHERS/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CATEGORY OF CARE-CHRONIC CARE MGMT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC MEALS PREPARED BY OTHERS/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CATEGORY OF CARE-HEALTH PROMOTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC MOVING AROUND INDOORS LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CATEGORY OF CARE-NON INSTITUTIONAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC MOVING AROUND INDOORS LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CATEGORY OF CARE-OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC RECENT CHANGE IN ADL FX-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF 1 OR MORE BEHAV/COGN PROBLEMS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC RECENT CHANGE IN ADL FX-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF 12 OR MORE CLINIC STOPS PAST YR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC RECENT CHANGE IN IADL FX-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF 2 OR MORE ADL DEFICITS</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GEC RECENT CHANGE IN IADL FX-YES</p>
</blockquote></th>
<th><blockquote>
<p>HT CCF AGE 75 OR GREATER</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GEC REFERRAL BASIC ADL</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF AGITATED/DISORIENTED-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC REFERRAL IADL</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF AGITATED/DISORIENTED-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC TOILET HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF CAREGIVER ACCESSIBLE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER CAN'T INCREASE HELP</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF CAREGIVER CAN INCREASE HELP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER LIVES WITH PT-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF LIVES NURSING HOME</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER LIVES WITH PT-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF LIVES PRIVATE HOME</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER NOT ACCESSIBLE</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF LIVES WITH ADULT CHILD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-ADL HELP</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF LIVES WITH CHILD</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-CHILD</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF LIVES WITH OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-EMOTIONAL SUPPORT</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF LIVES WITH SPOUSE &amp; OTHERS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-FRIEND/NEIGHBOR</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF LIVES WITH SPOUSE ONLY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-IADL HELP</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF MEETS CHRONIC CARE MGMT CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER-OTHER</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF MEETS NIC CATEGORY A CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER'S CITY</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF MEETS NIC CATEGORY B CRITERIA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER'S NAME</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF MEETS NIC CRITERIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER'S PHONE</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF MOOD DISORDER DEPRESSION-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER'S STATE</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF MOOD DISORDER DEPRESSION-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER'S STREET ADDRESS</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF MOOD DISORDER MANIC-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF CAREGIVER'S ZIP CODE</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF MOOD DISORDER MANIC-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF CAREGIVER-SPOUSE</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF NIC CRITERIA NO-ACUTE CARE MGMT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF COMPLEXITY TOO GREAT-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF NIC CRITERIA NO-HLTH PROMOTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF COMPLEXITY TOO GREAT-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF PHYSICALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DELUSIONS-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF PHYSICALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DELUSIONS-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF POTENTIAL FOR INCR INDEP-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DIFFIC MAKE SELF UNDERSTOOD-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF POTENTIAL FOR INCR INDEP-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DIFFIC MAKE SELF UNDERSTOOD-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF PROBLEMS WITH 3 OR MORE ADLS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DIFFIC REASONABLE DECISIONS-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF PROBLEMS WITH 3 OR MORE IADL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DIFFIC REASONABLE DECISIONS-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF PTSD/OTHER ANXIETY-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF DOES NOT MEET CCM CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF PTSD/OTHER ANXIETY-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF DOES NOT MEET NIC CRITERIA</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF RECOMMEND REFERRAL-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF FLARE UP CHRONIC CONDITION-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF RECOMMEND REFERRAL-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF FLARE UP CHRONIC CONDITION-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF RESISTING CARE-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF FOLLOW-UP ASSESSMENT COMPLETED</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF RESISTING CARE-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF GROUP SETTING NON RELATIVES</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF SERVICES IN PLACE-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-AUDITORY</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF SERVICES IN PLACE-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-NONE</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF SUBST ABUSE/DEPENDENCE-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-OLFACTORY</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF SUBST ABUSE/DEPENDENCE-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-SENSORY</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF UNPAID CAREGIVER-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-TACTILE</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF UNPAID CAREGIVER-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-VISUAL</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF VERBALLY ABUSIVE BEHAVIOR-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF INITIAL ASSESSMENT COMPLETED</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF VERBALLY ABUSIVE BEHAVIOR-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIFE EXPECTANCY &lt; 6 MO</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF WANDERING-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES ALONE</p>
</blockquote></td>
<td><blockquote>
<p>HT CCF WANDERING-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES ALONE IN COMMUNITY</p>
</blockquote></td>
<td><blockquote>
<p>HT CG/VETERAN REFERRAL COMPLETED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES AT OTHER</p>
</blockquote></td>
<td><blockquote>
<p>HT CG/VETERAN REFERRAL(S) NOT UTILIZED</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT CCF LIVES BOARD AND CARE</p>
</blockquote></th>
<th><blockquote>
<p>HT CLINICAL REASON FOR ENROLLMENT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES DOMICILIARY</p>
</blockquote></td>
<td><blockquote>
<p>HT CONSULTS/REFERRALS RECOMMENDED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES HOMELESS</p>
</blockquote></td>
<td><blockquote>
<p>HT CONTINUUM OF CARE (CCF)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES HOMELESS SHELTER</p>
</blockquote></td>
<td><blockquote>
<p>HT DIFFICULT MANAGING MEDS/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT MNG FINANCES/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT DIFFICULT MANAGING MEDS/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT MNG FINANCES/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT EMERG PRIORITY HIGH-IMMEDIATE EVAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT PREPARE MEALS/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT EMERG PRIORITY LOW-HAS RESOURCES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT PREPARE MEALS/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT EMERG PRIORITY MOD-SVCS AFTER 3-7D</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT TRANSPORTATION/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT ENROLLMENT-ENDING DATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT TRANSPORTATION/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT ENROLLMENT-START DATE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT USING PHONE LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT ENROLLMENT-START DATE (PREV ENROLL)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT USING PHONE LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT EQUIP INSTALLATION MODE-OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT W/ HOUSEWORK/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT EQUIP INSTALLED BY CONTRACT VENDOR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT W/ HOUSEWORK/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT EQUIP INSTALLED BY HOME TELEHEALTH</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DIFFICULT WITH SHOPPING/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT EQUIP INSTALLED BY SUPPORT STAFF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DIFFICULT WITH SHOPPING/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT EQUIP INSTALLED BY VETERAN/CAREGIVER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE</p>
</blockquote></td>
<td><blockquote>
<p>HT GETS MEDS VIA NON-VA PROVIDER-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-ADMITTED TO NURSING HOME</p>
</blockquote></td>
<td><blockquote>
<p>HT GETS MEDS VIA NON-VA PROVIDER-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-ALL ISSUES ADDRESSED(NO)</p>
</blockquote></td>
<td><blockquote>
<p>HT HEALTH EDUCATION PLAN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-ALL ISSUES ADDRESSED(YES)</p>
</blockquote></td>
<td><blockquote>
<p>HT HEALTH EDUCATION RESPONSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-HAS MET GOALS</p>
</blockquote></td>
<td><blockquote>
<p>HT INDICATIONS-# OUTPT VISITS PAST YR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-NO RESPONSE TO PROGRAM</p>
</blockquote></td>
<td><blockquote>
<p>HT INDICATIONS-DISTANCE (HOURS)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-NO VA PRIMARY CARE SVCS</p>
</blockquote></td>
<td><blockquote>
<p>HT INDICATIONS-DISTANCE (MILES)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-OTHER FOLLOW-UP</p>
</blockquote></td>
<td><blockquote>
<p>HT INDICATIONS-HX HIGH COST/HIGH USE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-PATIENT IS DECEASED</p>
</blockquote></td>
<td><blockquote>
<p>HT INDICATIONS-HX HOSPITALIZATONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-ANGRY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-PROLONGED HOSPITALIZATION</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-ANXIETY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-PROVIDER REQUESTS DC</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-APHASIA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-PT/CG REQUEST DC SERVICES</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-COGNITIVE IMPAIRMENT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO HOSPICE</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-CULTURAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO MENTAL HEALTH</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-HEARING IMPAIRED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO NEW LOCATION</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-HOMELESS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO PRIMARY CARE</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-IMPAIRED MEMORY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO SOCIAL WORK</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-LANGUAGE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-RELOCATED OUT OF SVC AREA</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-NONE IDENTIFIED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-UNABLE TO OPERATE DEVICES</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-NOT MOTIVATED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-COPD</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-OVERWHELMED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-DEPRESSION</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-PAIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-DIABETES</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-PHYSICAL LIMITATIONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-HEART FAILURE</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-POOR CONCENTRATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-HYPERTENSION</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-UNABLE TO READ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-OBESITY</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-UNABLE TO WRITE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-OTHER</p>
</blockquote></td>
<td><blockquote>
<p>HT LEARNING BARRIER-VISUALLY IMPAIRED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-PTSD</p>
</blockquote></td>
<td><blockquote>
<p>HT MEALS PREPARED BY OTHER/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-SUBSTANCE ABUSE</p>
</blockquote></td>
<td><blockquote>
<p>HT MEALS PREPARED BY OTHER/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISINTERESTED/LACKS MOTIVATION</p>
</blockquote></td>
<td><blockquote>
<p>HT MEETS TELEHEALTH CRITERIA(NO)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT DRESSING HELP/SUPERV LAST 7D-NO</p>
</blockquote></th>
<th><blockquote>
<p>HT MEETS TELEHEALTH CRITERIA(YES)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT DRESSING HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT MOVE INDOOR HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EATING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>HT MOVE INDOOR HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EATING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>HT NEEDS REINFORCEMENT/REVIEW/FOLLOW-UP</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT NO FOLLOW-UP NEEDED/INDICATED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PERIODIC EVALUATION COMPLETED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT PLAN-MED DISCREP SENT TO PROVIDER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PLAN-REVIEWED LIST OF CURRENT MEDS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT PT/CG HAS LIST OF ACTIVE MEDS-NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PT/CG HAS LIST OF ACTIVE MEDS-YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT PT/CG HAS QUESTIONS ON MEDS-NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT PT/CG HAS QUESTIONS ON MEDS-YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REASON FOR NON-ENROLLMENT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT RECENT CHANGE IN FUNCTION-NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT RECENT CHANGE IN FUNCTION-YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT REFERRAL-CONSULT COMPLETION</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REFERRALS FOR VETERAN/CAREGIVER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT REFERRALS-CAREGIVER NOT SATISFIED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REFERRALS-CAREGIVER SATISFIED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT REPEAT DEMONSTRATION NEXT VISIT</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TEACH CAREGIVER/FAMILY/SIGNIF OTHER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TECH EDUC DEVICE ASSIGNED</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TELEHEALTH DELIVERY/INSTALL MODE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TELEHEALTH DEMOGRAPHICS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TOILET HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TOILET HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TRANSFERS HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TRANSFERS HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT UNABLE TO SCREEN CAREGIVER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VET NOT INTERESTED TELEHEALTH PROGRAM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN REFERRAL EDUC/TRAINING</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN REFERRAL SVCS IN PLACE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN STATES ESSENTIAL CONCEPTS</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-ASL</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-BRAILLE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-CHINESE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-ENGLISH</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-FRENCH</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-GERMAN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-ITALIAN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-KOREAN</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-OTHER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-</p>
<p>PORTUGUESE</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-RUSSIAN</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-SPANISH</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-TAGALOG</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-VIETNAMESE</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="_bookmark50" class="anchor"></span><u>Appendix I: Health Factors (Alpha Sort w/ Category)</u>

> GEC REFERRAL BASIC ADL

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GEC BATHING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></th>
<th><blockquote>
<p>GEC INDEPENDENT IN WC LAST 7D-NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GEC BATHING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC INDEPENDENT IN WC LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC BATHING PHYS ASST NEEDED LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>GEC MOVING AROUND INDOORS LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC BATHING PHYS ASST NEEDED LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC MOVING AROUND INDOORS LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC BED POSITIONING HELP LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>GEC RECENT CHANGE IN ADL FX-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC BED POSITIONING HELP LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC RECENT CHANGE IN ADL FX-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DRESS HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>GEC TOILET HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DRESS HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC TOILET HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC EATING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>GEC TRANSFERS HELP/SPRVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC EATING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC TRANSFERS HELP/SPRVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

> GEC REFERRAL IADL

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>GEC DIFFICULT TRANSPORTATION/LAST 7D-NO</p>
</blockquote></th>
<th><blockquote>
<p>GEC DIFFICULTY USING PHONE/LAST 7D-YES</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULT TRANSPORTATION/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY MANAGING MEDS/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>GEC DIFFICULTY W/ HOUSEWORK/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULTY MANAGING MEDS/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC DIFFICULTY WITH SHOPPING/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY MNG FINANCES/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>GEC DIFFICULTY WITH SHOPPING/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULTY MNG FINANCES/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC MEALS PREPARED BY OTHERS/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY PREPARE MEALS/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>GEC MEALS PREPARED BY OTHERS/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC DIFFICULTY PREPARE MEALS/LAST 7D-YES</p>
</blockquote></td>
<td><blockquote>
<p>GEC RECENT CHANGE IN IADL FX-NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GEC DIFFICULTY USING PHONE/LAST 7D-NO</p>
</blockquote></td>
<td><blockquote>
<p>GEC RECENT CHANGE IN IADL FX-YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

> HT (HOME TELEHEALTH)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT CLINICAL REASON FOR ENROLLMENT</p>
</blockquote></th>
<th><blockquote>
<p>HT ENROLLMENT-START DATE (PREV ENROLL)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT ENROLLMENT-ENDING DATE</p>
</blockquote></td>
<td><blockquote>
<p>HT REFERRAL-CONSULT COMPLETION</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT ENROLLMENT-START DATE</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN'S GOAL FOR ENROLLMENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> HT ASSESSMENT/TREATMENT PLAN

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT CATEGORY OF CARE-ACUTE CARE</p>
</blockquote></th>
<th><blockquote>
<p>HT GETS MEDS VIA NON-VA PROVIDER-YES</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CATEGORY OF CARE-CHRONIC CARE MGMT</p>
</blockquote></td>
<td><blockquote>
<p>HT PERIODIC EVALUATION COMPLETED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CATEGORY OF CARE-HEALTH PROMOTION</p>
</blockquote></td>
<td><blockquote>
<p>HT PLAN-MED DISCREP SENT TO PROVIDER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CATEGORY OF CARE-NON INSTITUTIONAL</p>
</blockquote></td>
<td><blockquote>
<p>HT PLAN-REVIEWED LIST OF CURRENT MEDS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CATEGORY OF CARE-OTHER</p>
</blockquote></td>
<td><blockquote>
<p>HT PT/CG HAS LIST OF ACTIVE MEDS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EMERG PRIORITY HIGH-IMMEDIATE EVAL</p>
</blockquote></td>
<td><blockquote>
<p>HT PT/CG HAS LIST OF ACTIVE MEDS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EMERG PRIORITY LOW-HAS RESOURCES</p>
</blockquote></td>
<td><blockquote>
<p>HT PT/CG HAS QUESTIONS ON MEDS-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EMERG PRIORITY MOD-SVCS AFTER 3-7D</p>
</blockquote></td>
<td><blockquote>
<p>HT PT/CG HAS QUESTIONS ON MEDS-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT GETS MEDS VIA NON-VA PROVIDER-NO</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> HT CAREGIVER RISK ASSESSMENT SCREEN HT CONTINUUM OF CARE (CCF)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT CCF FOLLOW-UP ASSESSMENT COMPLETED</p>
</blockquote></th>
<th><blockquote>
<p>HT DIFFICULT USING PHONE LAST 7D-NO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CCF GROUP SETTING NON RELATIVES</p>
</blockquote></td>
<td><blockquote>
<p>HT DIFFICULT USING PHONE LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-AUDITORY</p>
</blockquote></td>
<td><blockquote>
<p>HT DIFFICULT W/ HOUSEWORK/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-NONE</p>
</blockquote></td>
<td><blockquote>
<p>HT DIFFICULT W/ HOUSEWORK/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-OLFACTORY</p>
</blockquote></td>
<td><blockquote>
<p>HT DIFFICULT WITH SHOPPING/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-SENSORY</p>
</blockquote></td>
<td><blockquote>
<p>HT DIFFICULT WITH SHOPPING/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-TACTILE</p>
</blockquote></td>
<td><blockquote>
<p>HT DRESSING HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF HALLUCINATIONS-VISUAL</p>
</blockquote></td>
<td><blockquote>
<p>HT DRESSING HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF INITIAL ASSESSMENT COMPLETED</p>
</blockquote></td>
<td><blockquote>
<p>HT EATING HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIFE EXPECTANCY &lt; 6 MO</p>
</blockquote></td>
<td><blockquote>
<p>HT EATING HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES ALONE</p>
</blockquote></td>
<td><blockquote>
<p>HT MEALS PREPARED BY OTHER/LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES ALONE IN COMMUNITY</p>
</blockquote></td>
<td><blockquote>
<p>HT MEALS PREPARED BY OTHER/LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES AT OTHER</p>
</blockquote></td>
<td><blockquote>
<p>HT MOVE INDOOR HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES BOARD AND CARE</p>
</blockquote></td>
<td><blockquote>
<p>HT MOVE INDOOR HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES DOMICILIARY</p>
</blockquote></td>
<td><blockquote>
<p>HT RECENT CHANGE IN FUNCTION-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES HOMELESS</p>
</blockquote></td>
<td><blockquote>
<p>HT RECENT CHANGE IN FUNCTION-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES HOMELESS SHELTER</p>
</blockquote></td>
<td><blockquote>
<p>HT TOILET HELP/SUPERVISION LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES NURSING HOME</p>
</blockquote></td>
<td><blockquote>
<p>HT TOILET HELP/SUPERVISION LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES PRIVATE HOME</p>
</blockquote></td>
<td><blockquote>
<p>HT TRANSFERS HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES WITH ADULT CHILD</p>
</blockquote></td>
<td><blockquote>
<p>HT TRANSFERS HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CCF LIVES WITH CHILD</p>
</blockquote></td>
<td><blockquote>
<p>HT W/C MOBIL HELP/SUPERV LAST 7D-NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CCF LIVES WITH OTHER</p>
</blockquote></td>
<td><blockquote>
<p>HT W/C MOBIL HELP/SUPERV LAST 7D-YES</p>
</blockquote></td>
</tr>
</tbody>
</table>

> HT DISCHARGE

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT DISCHARGE-ADMITTED TO NURSING HOME</p>
</blockquote></th>
<th><blockquote>
<p>HT DISCHARGE-PROVIDER REQUESTS DC</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-ALL ISSUES ADDRESSED(NO)</p>
</blockquote></td>
<td><blockquote>
<p>HT DISCHARGE-PT/CG REQUEST DC SERVICES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-ALL ISSUES ADDRESSED(YES)</p>
</blockquote></td>
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO HOSPICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-HAS MET GOALS</p>
</blockquote></td>
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO MENTAL HEALTH</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-NO RESPONSE TO PROGRAM</p>
</blockquote></td>
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO NEW LOCATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-NO VA PRIMARY CARE SVCS</p>
</blockquote></td>
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO PRIMARY CARE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-OTHER FOLLOW-UP</p>
</blockquote></td>
<td><blockquote>
<p>HT DISCHARGE-REFERRED TO SOCIAL WORK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-PATIENT IS DECEASED</p>
</blockquote></td>
<td><blockquote>
<p>HT DISCHARGE-RELOCATED OUT OF SVC AREA</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISCHARGE-PHONE,ELECT SVCS UNAVAIL</p>
</blockquote></td>
<td><blockquote>
<p>HT DISCHARGE-UNABLE TO OPERATE DEVICES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISCHARGE-PROLONGED HOSPITALIZATION</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> HT REFERRALS FOR VETERAN/CAREGIVER

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT CAREGIVER REFERRAL BEREAVE SUPPORT</p>
</blockquote></th>
<th><blockquote>
<p>HT VETERAN REFERRAL FAMILY COUNSEL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL C/G SUPPORT GRP</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL FINANCIAL ASSIST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL EDUC/TRAINING</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL HOME HEALTH SVC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL FAMILY COUNSEL</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL HOMEMKR/CHORE ASST</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL INDIVID COUNSEL</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL HOSPICE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL MEDICAL EVAL,F/U</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL HOUSING</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL OTHER SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL INDIVIDUAL COUNSEL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL SOCIAL WORK</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL LEGAL ASSISTANCE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CAREGIVER REFERRAL SVCS IN PLACE</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL MEDICAL EVAL, F/U</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT CAREGIVER REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL NURS HOME PLACEMNT</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT CAREGIVER REFERRAL(S) VA SYSTEM</p>
</blockquote></th>
<th><blockquote>
<p>HT VETERAN REFERRAL OTHER SERVICE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT CG/VETERAN REFERRAL COMPLETED</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL RESPITE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT CG/VETERAN REFERRAL(S) NOT UTILIZED</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL SOCIAL WORK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT REFERRALS-CAREGIVER NOT SATISFIED</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL SVCS IN PLACE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT REFERRALS-CAREGIVER SATISFIED</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL TRANSPORTATION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN REFERRAL ADULT DAY CARE</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL(S) NON VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VETERAN REFERRAL EDUC/TRAINING</p>
</blockquote></td>
<td><blockquote>
<p>HT VETERAN REFERRAL(S) VA SYSTEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VETERAN REFERRAL EMPLOYMENT ASSIST</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> HT TELEHEALTH DELIVERY/INSTALL MODE

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT EQUIP INSTALLATION MODE-OTHER</p>
</blockquote></th>
<th><blockquote>
<p>HT EQUIP TAKEN HOME,INSTALLED BY VET/CG</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT EQUIP INSTALLED BY SUPPORT STAFF</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT EQUIP INSTALLED BY VETERAN/CAREGIVER</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT EQUIP MAILED,INSTALL BY VET/CAREGIVER</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> HT TELEHEALTH DEMOGRAPHICS

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT DISEASE INDICATIONS-COPD</p>
</blockquote></th>
<th><blockquote>
<p>HT INDICATIONS-# OUTPT VISITS PAST YR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-DEPRESSION</p>
</blockquote></td>
<td><blockquote>
<p>HT INDICATIONS-DISTANCE (HOURS)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-DIABETES</p>
</blockquote></td>
<td><blockquote>
<p>HT INDICATIONS-DISTANCE (MILES)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-HEART FAILURE</p>
</blockquote></td>
<td><blockquote>
<p>HT INDICATIONS-HX HIGH COST/HIGH USE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-HYPERTENSION</p>
</blockquote></td>
<td><blockquote>
<p>HT INDICATIONS-HX HOSPITALIZATONS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-OBESITY</p>
</blockquote></td>
<td><blockquote>
<p>HT MEETS TELEHEALTH CRITERIA(NO)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-OTHER</p>
</blockquote></td>
<td><blockquote>
<p>HT MEETS TELEHEALTH CRITERIA(YES)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT DISEASE INDICATIONS-PTSD</p>
</blockquote></td>
<td><blockquote>
<p>HT REASON FOR NON-ENROLLMENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT DISEASE INDICATIONS-SUBSTANCE ABUSE</p>
</blockquote></td>
<td><blockquote>
<p>HT VET NOT INTERESTED TELEHEALTH PROGRAM</p>
</blockquote></td>
</tr>
</tbody>
</table>

> PREFERRED HEALTHCARE LANGUAGE

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-ENGLISH</p>
</blockquote></th>
<th><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-KOREAN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-OTHER</p>
</blockquote></td>
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-GERMAN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-ASL</p>
</blockquote></td>
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-VIETNAMESE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-BRAILLE</p>
</blockquote></td>
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-TAGALOG</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-</p>
<p>PORTUGUESE</p>
</blockquote></td>
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-FRENCH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-ITALIAN</p>
</blockquote></td>
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-CHINESE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-RUSSIAN</p>
</blockquote></td>
<td><blockquote>
<p>PREFERRED HEALTHCARE LANGUAGE-SPANISH</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Appendix J: Education Topics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA-HOME TELEHEALTH (HT)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>VA-HOME TELEHEALTH-CAREGIVER</p>
<p>EDUCATION/SUPPORT</p>
</blockquote></th>
<th><blockquote>
<p>VA-HOME TELEHEALTH-CAREGIVER</p>
<p>EDUCATION/SUPPORT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>VA-HOME TELEHEALTH-DISEASE</p>
<p>MGMT/PATIENT SELF-MGMT</p>
</blockquote></td>
<td><blockquote>
<p>VA-HOME TELEHEALTH-DISEASE</p>
<p>MGMT/PATIENT SELF-MGMT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT

> The Non-Paid Caregiver will receive both the education (via the in home messaging device, telemonitor, videophone or telephone) as well as the support necessary to enhance the care provided to the Veteran.

1.  The Care Coordinator will assign the appropriate DMP to help educate the caregiver on the disease process of the Veteran.
2.  The Care Coordinator will help coordinate the appropriate resources to support the caregiver.

> VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT

> The Veteran, upon enrollment, will be assigned the appropriate Disease Management Protocol (DMP) that will enhance the Veteran's ability to self-manage his/her chronic disease process.

1.  The Care Coordinator will assign a Disease Management Protocol (DMP) appropriate for the veteran upon enrollment.
2.  The Care Coordinator will monitor the Veteran's responses to the DMP questions to provide interventions when necessary.
3.  Interventions are designed to enhance the Veteran's ability to self-manage his/her disease process.

> VA-HOME TELEHEALTH-IN HOME MONITORING

> Veteran receives care coordination and daily monitoring via an in-home messaging/monitoring device of his/her chronic disease(s) by a Care Coordinator.

1.  The Care Coordinator monitors measurements and/or individual responses to questions directly related to the Veteran's chronic disease(s).
2.  The Care Coordinator responds/intervenes timely to alerts indicating need.
3.  The Care Coordinator updates the Veteran's provider routinely and as needed.
4.  Veteran and/or caregiver understand proper setup and procedure for in-home monitoring.
5.  Veteran and/or caregiver understand the confidentiality of health information.
6.  Veteran and/or caregiver understand that he/she must follow his/her normal emergency plan for any emergency.
7.  Veteran and/or caregiver understand that his/her in home messaging/monitoring device is not a 911 or emergency device.
8.  Veteran and/or caregiver understand how to contact Home Telehealth staff for any questions, problems with equipment, or concerns.

> VA-HOME TELEHEALTH-MEDICATION MANAGEMENT

> Veteran has provided the VA with a complete list of Non VA medications and OTC drugs & supplements.

> The Veteran understands his/her VA prescribed medications and takes his/her medications as prescribed.

1.  The Care Coordinator reviews all medications upon enrollment into the HT program and at regular intervals throughout the Veteran's active enrollment.
2.  The Care Coordinator reports any discrepancies to the Veteran's provider for reconciliation.
3.  The Care Coordinator routinely educates Veteran on his/her medications and responds timely to any question the Veteran may have about his/her medication.

## Appendix K: Acronyms and Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### National Acronym Directory:

> [<u>http://vaww1.va.gov/Acronyms/</u>](http://vaww1.va.gov/Acronyms/)

> <span id="_bookmark53" class="anchor"></span>Acronyms

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
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
<p>ASU</p>
</blockquote></td>
<td><blockquote>
<p>Authorization/Subscription Utility</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CCHT</p>
</blockquote></td>
<td><blockquote>
<p>Care Coordination Home Telehealth (former name; now called HT)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CDCO</p>
</blockquote></td>
<td><blockquote>
<p>Corporate Data Center Operations (includes AITC)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td><blockquote>
<p>Home Telehealth</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DD</p>
</blockquote></td>
<td><blockquote>
<p>Data Dictionary</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>EPMO</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Program Management Office</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ESM</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Systems Management (ESM)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>FIM</p>
</blockquote></td>
<td><blockquote>
<p>Functional Independence Measure</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SFTP</p>
</blockquote></td>
<td><blockquote>
<p>Secure File Transfer Protocol</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td><blockquote>
<p>VistA namespace for Health Summary package</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GUI</p>
</blockquote></td>
<td><blockquote>
<p>Graphic User Interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IAB</p>
</blockquote></td>
<td><blockquote>
<p>Initial Assessment &amp; Briefing</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MED REC</p>
</blockquote></td>
<td><blockquote>
<p>Medication Reconciliation</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OCC</p>
</blockquote></td>
<td><blockquote>
<p>Office of Connected Care</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OI</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OIF/OEF</p>
</blockquote></td>
<td><blockquote>
<p>Operation Iraqi Freedom/Operation Enduring Freedom</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PCS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Reminder Package namespace</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RSD</p>
</blockquote></td>
<td><blockquote>
<p>Requirements Specification Document</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TIU</p>
</blockquote></td>
<td><blockquote>
<p>Text Integration Utilities</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TIU/HS</p>
</blockquote></td>
<td><blockquote>
<p>TIU-Health Summary data objects</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TXML</p>
</blockquote></td>
<td><blockquote>
<p>Template format for CPRS GUI dialog templates</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Department of Veteran Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>USR</p>
</blockquote></td>
<td><blockquote>
<p>VistA namespace for ASU package</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information System and Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VLER</p>
</blockquote></td>
<td><blockquote>
<p>Virtual Lifetime Electronic Record</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark54" class="anchor"></span>Glossary

> Master OIT Glossary: [<u>http://vaww.oed.wss.va.gov/process/Lists/glossary/default.aspx</u>](http://vaww.oed.wss.va.gov/process/Lists/glossary/default.aspx)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Term</p>
</blockquote></th>
<th><blockquote>
<p>Definition</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Austin Information Technology Center</p>
<p>(AITC)</p>
</blockquote></td>
<td><blockquote>
<p>Austin Information Technology Center (AITC) is part of the corporate data center Operations (CDCO). The central repository for National</p>
<p>Patient Care Database is maintained at the AITC.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Care Coordinators</p>
</blockquote></td>
<td><blockquote>
<p>Care Coordinators are licensed health care professionals who help veteran patients self-manage their condition. Care Coordinators guide and support veteran patients to ensure they receive the right care, in the</p>
<p>right place, at the right time, from the right person.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Corporate Data Center Operations</p>
<p>(CDCO)</p>
</blockquote></td>
<td><blockquote>
<p>VA's integration of five national data centers, which incorporates the AITC.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Clinical Data</p>
<p>Services (CDS)</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Data Service (CDS) is the access service to patient-centric, clinical data persisted in HDR (Health Data Repository) data stores.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Clinical Context Object Workgroup</p>
<p>(CCOW)</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Context Object Workgroup (CCOW) is used to share patient and user context between applications</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Clinical Reminders</p>
</blockquote></td>
<td><blockquote>
<p>A clinical reminder is a software decision support tool that defines evaluation and resolution logic for a given clinical activity. The evaluation logic defines conditions in the database, including the presence or absence of specified criteria such as diagnoses, procedures, health factors, medications, or demographic variables (e.g., age, gender). A reminder may or may not require provider resolution, depending on its purpose and design, through a user interface, also</p>
<p>known as a reminder dialog.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Consult</p>
</blockquote></td>
<td><blockquote>
<p>Referral of a patient by a healthcare provider to another hospital service/specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments</p>
<p>the consulting specialist deems necessary to render a medical opinion.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Computerized Patient Records System (CPRS)</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Records System (CPRS) provides an integrated patient record system for clinicians, managers, quality assurance staff, and researchers. The primary goal of CPRS is to create a fast and easy- to-use product that gives physicians enough information through clinical reminders, results reporting, and expert system feedback to make better decisions regarding orders and treatment. VistA software integrated with CPRS includes Pharmacy, Lab, Radiology, Allergy Tracking, Consults, Dietetics, Progress Notes, Problem List, Patient</p>
<p>Administration, Vitals, PCE, TIU, ASU and Clinical Lexicon.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Data File Number</p>
<p>(DFN)</p>
</blockquote></td>
<td><blockquote>
<p>Patient’s Internal Entry Number (IEN)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Health Data</p>
</blockquote></td>
<td><blockquote>
<p>A data repository of clinical information that resides on one or more</p>
</blockquote></td>
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
<th><blockquote>
<p>Term</p>
</blockquote></th>
<th><blockquote>
<p>Definition</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Repository (HDR)</p>
</blockquote></td>
<td><blockquote>
<p>independent platforms and is used by clinicians and other personnel to</p>
<p>facilitate longitudinal patient-centric care.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Health Level 7 (HL7)</p>
</blockquote></td>
<td><blockquote>
<p>HL7 is an ANSI standard for electronic data exchange in healthcare environments. It is an interface specification designed to standardize the transfer of health care information between systems. HL7 is an application layer protocol for electronic data exchange in health care environments. The HL7 protocol is a collection of standard formats for health care data. This communication protocol allows healthcare institutions to exchange key sets of data between different application systems. The protocol accommodates the flexibility necessary to allow</p>
<p>compatibility for specialized data sets that have facility-specific needs.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ID</p>
</blockquote></td>
<td><blockquote>
<p>Coded Value data type</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Interface Engine (IE)</p>
</blockquote></td>
<td><blockquote>
<p>A device or software application that connects disparate system, transforms data, converts data, routes data, ensures the delivery of data and is rules based. The IE provides a consistent HL7 compliant communication environment. That is separate from the specific and individual application needs. In this environment, messages can be routed, transformed, converted and delivery guaranteed as required by</p>
<p>the application.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Integration Control Number (ICN)</p>
</blockquote></td>
<td><blockquote>
<p>The Integration Control Number (ICN) is a unique identifier assigned to patients when they are added to the Master Patient Index (MPI). ICNs fall under two categories: national and local. The ICN follows the ASTM E1714-95 standard for a universal health identifier. ICNs link patients to their records across VA systems.</p>
<p>The ICN is stored in a message using the HL7 CX format. The ID subfield is the ICN.</p>
<p>The type subfield is USVHA.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Master Patient Index (MPI)</p>
</blockquote></td>
<td><blockquote>
<p>The objectives of the Master Patient Index (MPI) are to create an index that uniquely identifies each active patient treated by the VA and to identify the sites where a patient is receiving care. This is crucial to the sharing of patient information across sites.</p>
<p>MPI manages the synchronization of patient file information between the Master Patient Index and the patient's treatment facilities to ensure that data being shared is stored in the correct patient's record.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Patient Information</p>
<p>Management System (PIMS)</p>
</blockquote></td>
<td><blockquote>
<p>This umbrella application contains the Scheduling, Registration, PCE, and Enrollment applications that relate to patient information.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Protocol</p>
</blockquote></td>
<td><blockquote>
<p>A set of procedures for establishing and controlling data transmission</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Remote Data View</p>
<p>(RDV)</p>
</blockquote></td>
<td><blockquote>
<p>A CPRS application that allows a caregiver to view patient data that is</p>
<p>stored in another VistA facility.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Telehealth</p>
</blockquote></td>
<td><blockquote>
<p>Telehealth is the use of electronic communications and information technology to provide and support health care when distance separates</p>
<p>the participants. It covers health care practitioners interacting with patients and patients interacting with other patients.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Telemedicine</p>
</blockquote></td>
<td><blockquote>
<p>Telemedicine is the provision of care by a licensed independent health</p>
</blockquote></td>
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
<th><blockquote>
<p>Term</p>
</blockquote></th>
<th><blockquote>
<p>Definition</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>care provider that directs, diagnoses, or otherwise provides clinical treatment delivered using electronic communications and information</p>
<p>technology when distance separates the provider and the patient. .</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TCP/IP</p>
</blockquote></td>
<td><blockquote>
<p>Transaction Control Protocol/Internet Protocol (TCP/IP) is a set of protocols for Layers 3 (Network) and 4 (Transport) of the OSI network model. TCP/IP has been developed over a period of 30 years under the auspices of the Department of Defense. It is a de facto standard, particularly as higher-level layers over Ethernet. TCP/IP predates the</p>
<p>OSI model; therefore, TCP/IP is not OSI-compliant.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information Systems and Technology Architecture (VistA), formerly known as Decentralized Hospital Computer Program (DHCP), encompasses the complete information environment at VA medical facilities. It consists of hardware, software packages, and comprehensive support for system-wide and station specific, clinical,</p>
<p>and administrative automation needs.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistA Interface</p>
<p>Engine (VIE)</p>
</blockquote></td>
<td><blockquote>
<p>Vitria BusinessWare software that has been configured specifically for</p>
<p>the VHA VistA environment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistAWeb</p>
</blockquote></td>
<td><blockquote>
<p>A web-based application to view patient data from various VA facilities.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VLER</p>
</blockquote></td>
<td><blockquote>
<p>Virtual Lifetime Electronic Record, a program to integrate VA, DoD,</p>
<p>and private patient records.</p>
</blockquote></td>
</tr>
</tbody>
</table>