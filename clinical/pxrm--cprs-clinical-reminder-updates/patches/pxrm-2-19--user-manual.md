---
title: PXRM*2*19 Home Telehealth User Manual
doc_type: UM
doc_label: User Manual
doc_layer: patch
doc_subject: Home Telehealth
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
menu_options: 9
description: > The purpose of this project is to release new national reminders, reminder dialogs, and TIU progress note titles that will be used by Care Coordinators managing patients enrolled in HT programs.
audience: 
keywords: 
  - blockquote
  - strong
  - table
  - class
  - contents
  - template
  - style
  - width
  - home
  - care
page_count: 0
word_count: 10492
section_count: 24
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_19_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_19_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> Home Telehealth

# Clinical Reminders and Dialogs User Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Clinical Reminders and Dialogs User Guide](#clinical-reminders-and-dialogs-user-guide)
    - [Department of Veterans Affairs](#department-of-veterans-affairs)
- [Introduction](#introduction)
    - [1.1.1.Web Sites](#111web-sites)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
- [Fundamentals](#fundamentals)
  - [Completing a Note](#completing-a-note)
  - [Using Templates for Documentation](#using-templates-for-documentation)
    - [Dialog Templates](#dialog-templates)
    - [Reminder Dialog Templates](#reminder-dialog-templates)
    - [Encounter/CPT Codes](#encountercpt-codes)
    - [Encounter Form Completion:](#encounter-form-completion)
    - [Completing an Encounter](#completing-an-encounter)
    - [Data Objects](#data-objects)
    - [Health Factors](#health-factors)
    - [HT Education Topics](#ht-education-topics)
  - [HT Clinical Reminders](#ht-clinical-reminders)
  - [Clinical Reminder Process](#clinical-reminder-process)
    - [How to satisfy Clinical Reminders](#how-to-satisfy-clinical-reminders)
  - [How to Run a “Reminders Due” Report](#how-to-run-a-reminders-due-report)
- [Getting Started](#getting-started)
  - [Complete the New Mini-template for Previously Enrolled HT patients](#complete-the-new-mini-template-for-previously-enrolled-ht-patients)
- [Templates and Program Enrollment](#templates-and-program-enrollment)
  - [Home Telehealth Consult Request.](#home-telehealth-consult-request)
    - [Completing the HT SCREENING CONSULT note from the CPRS consult tab](#completing-the-ht-screening-consult-note-from-the-cprs-consult-tab)
    - [Completing the HT SCREENING CONSULT note from the CPRS Notes tab](#completing-the-ht-screening-consult-note-from-the-cprs-notes-tab)
  - [TECH EDUCATION AND INSTALLATION](#tech-education-and-installation)
  - [ASSESSMENT TREATMENT PLAN](#assessment-treatment-plan)
  - [CONTINUUM OF CARE FORM (CCF)](#continuum-of-care-form-ccf)
  - [CAREGIVER RISK ASSESSMENT](#caregiver-risk-assessment)
  - [INTERVENTION NOTE](#intervention-note)
  - [MONTHLY MONITOR NOTE](#monthly-monitor-note)
  - [PERIODIC EVALUATION](#periodic-evaluation)
  - [EMERGENCY MANAGEMENT CLASSIFICATION](#emergency-management-classification)
  - [DISCHARGE TEMPLATE](#discharge-template)
  - [Other:](#other)
  - [VIDEO VISIT](#video-visit)
- [a. Acronyms and Abbreviations](#a-acronyms-and-abbreviations)
![](pxrm-2-19-home-telehealth-user-manual/001.png)
> July 2017

### Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)
> Revision History
> NOTE: The revision history cycle begins once changes or enhancements are requested after the document has been baselined.
<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 45%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revision</strong></p>
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
<p>06/29/2017</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>Revised to reflect content as of Tv13 of patch bundle</p>
</blockquote></td>
<td><blockquote>
<p>Development Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>01/05/2016</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Initial</p>
</blockquote></td>
<td><blockquote>
<p>C2/Booz Allen, PMO Support</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this project is to release new national reminders, reminder dialogs, and TIU progress note titles that will be used by Care Coordinators managing patients enrolled in HT programs.

> The Office of Connected Care (OCC) has been working to develop a comprehensive, user- friendly, and accurate delivery model for documentation in the Computerized Patient Record System (CPRS) for use by all Home Telehealth (HT) staff. It is vitally important to have documentation standardized for appropriate delivery of care to the Veterans, ability to pull accurate data, and ease of quality management and chart reviewing. For that reason, the national templates should not be edited or revised at the local or VISN level to maintain the integrity of the data collected as well as ensure any further national revisions or updates are appropriately captured and standardized.

> Two Master Preceptor-led committees spearheaded the work in creating this standardized documentation system. One was tasked with standardizing the Clinic Location titles and use of Stop Codes- both Primary and Secondary as well as developing a group of note titles that would intuitively reflect the work done by HT staff. The second committee was tasked with creating templates to be attached to the appropriate note titles. This again was to ensure that a standardized, high quality of care was delivered to the Veteran population, that the same information was being obtained, and that documentation was made as streamlined as possible.

### 1.1.1.Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<p>Contains manuals, PowerPoint presentations, and other information about</p>
<p>Clinical Reminders</p>
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
<p>This committee directs the development of new and revised national reminders</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA Document Library</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals for nationally released software in use across VHA, such as: Clinical Reminders, CPRS,</p>
<p>Consults/Request Tracking, and Text Integration Utilities</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Office of Connected Care (OCC) requested a comprehensive, integrated template set in use at all VA facilities caring for Home Telehealth patients. These templates are the replacements for the earlier set of templates posted on the web site (VA Intranet): [<u>http://vaww.telehealth.intranet.dev.webops.va.gov/</u>](http://vaww.telehealth.intranet.dev.webops.va.gov/) .Those templates were either not used at all by sites, or significantly modified. A group of representative HT clinicians from around the Country did a bi-monthly series of teleconferences, revising the content of the templates. Several Pilots were performed over a couple of years to produce the final product.

> The templates were converted to reminder dialogs for the special features the reminder dialogs provide, such as:

- Linked health factors \* (See Health Factor section below)
  - for data capture; these will be incorporated into the existing HT VSSC data cubes
  - for the ability to use as data objects for display back in the templates
- Ability to put boxes around items (enhanced visual appeal & end user navigation)
- Ability to suppress checkboxes for items in order to require a response
- A specific “required items missing” message
- Ability to send alternate text into the progress note (text different from that in the template)
- Ability to have embedded orders
- Ability to send ICD-10 (Diagnosis) and CPT (Procedure) codes to the GUI Encounter Form
- Ability to trigger and satisfy a clinical reminder even if in the TEMPLATES drawer

> If you have questions about the templates or documentation process, you may contact your HT Program Lead.

> If you have technical problems with the CPRS application or technical (computer) problems with accessing/launching/signing the templates, please contact your site CAC (Clinical Application Coordinator).

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are THREE distinct items to grasp in this new Documentation process:

1.  <span id="_bookmark4" class="anchor"></span>Clinic Location- gives the correct coding for workload. Choosing the correct Clinic Location to identify the activity is critical. This is how the data is created for reports in the VHA Support Service Center (VSSC) Cube such as 683, Monthly Notes, or 371, Screening Consult.
2.  <span id="_bookmark5" class="anchor"></span>Note Title- The choice of the correct title identifies the activity, and in most cases the correct Template will automatically be attached.
3.  <span id="_bookmark6" class="anchor"></span>Template- As noted above, these are generally attached to the appropriate Note Title. These templates are explained at length later in this document. Templates are mandatory and provide Health Factor data. The HT Templates are comprehensive, yet very user friendly and support the minimum documentation standards. They have many options and free text so take advantage of these and populate the template to reflect a complete and accurate description of the topic being covered. Any updates to these templates will be made and approved at the National level.

> Crosswalk: Titles and Stop Codes Option 1 and 2, See appendices.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This guide was written with the following assumed experience/skills of the audience:

1.  User has working knowledge of CPRS GUI, including, but not limited to, using Clinical Reminder dialogs to process and document patient encounters,
2.  User has been provided the appropriate active roles, menus, and security keys required for the software.
3.  User has validated access to the software.
4.  User has completed any prerequisite training.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Table 2: Deployment Roles and Responsibilities

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 29%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Team</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Phase / Role</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Tasks</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Development team and test sites</p>
</blockquote></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td><blockquote>
<p>Test for operational readiness</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Development team and National product support</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Execute deployment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Regional PM/ Field Implementation Services (FIS)/ Office of Policy and Planning (OPP) PM</p>
</blockquote></td>
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td><blockquote>
<p>Plan and schedule installation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Site CACs &amp; Clinical Staff, Nat’l Education &amp; Training</p>
</blockquote></td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
<td><blockquote>
<p>Post-installation readiness and training</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

> This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

> The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each project establishes a release baseline of critical information prior to the Project Management Accountability System (PMAS) MS1 review. This is the information that enters into change control at deployment. A subset of this information accompanies the product release to the field. This is referred to as the release package, which includes the product build (software and hardware specifications) along with the body of user and technical documentation that support the install, operations, training, and support of the product as well as authorizations required for deployment. The Release Package includes the following ProPath documents:

- System Design Document (SDD)
- Version Description Document (VDD)
- Operational Acceptance Plan (OAP)
- Project Management Plan (PMP)
- Production Operations Manual (POM)
- Authority to Operate (ATO)
- Installation Guide and Back-Out/Rollback Plan
- Deployment Plan
- Operational Readiness Review (ORR) Checklist Submission Documents (Business Requirements Document, Requirements Specification Document, Test Evaluation Summary, Requirements Traceability Matrix, User Guide, Technical Manual, etc.)

> Additionally, end user training will be provided by the Office of Connected Care, Implementation Team. All user training materials developed by the team will be made available in My Telehealth and in the HT Web Site; HT Master Document Library SharePoint [http://vaww.telehealth.va.gov/pgm/ht/index.asp.](http://vaww.telehealth.va.gov/pgm/ht/index.asp)

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Home Telehealth Clinical Reminders and Dialogs User Guide

> Found in the clinical reminder section of [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/) Home Telehealth Installation and Setup Guide

> Found in the clinical reminder section of [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/)

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Support will be performed by the National Service Desk – Tuscaloosa (NSD) (Tier 1 Support), Enterprise Program Management Office (EPMO) Health Product Support Team (Tier 2 Support), and the National VistA Maintenance Support Group (Tier 3 Support).

> Tier 1 Support will be provided by the NSD utilizing the CA Service Desk Management (SDM) system. Home Telehealth users (or their designee), with problems that cannot be resolved locally, will call the NSD to open a CA SDM ticket. Issues not resolved by the Tier 1 Support Team will be assigned to Tier 2 Support in CA SDM. Tier 2 Support for Home Telehealth Clinical Reminders, Health Summary, and Text Integration Utilities will include assistance from the respective EPMO Health Product Support Team. Issues not resolved by the Tier 2 Support Team will be assigned to Tier 3 Support in CA SDM. Tier 3 Support is the highest level of support for VistA applications, which includes business analysts, software testers, system administrators, developers, and database administrators who have specialized technical knowledge of VistA. Tier 3 Support will provide services, such as, issue resolution and defect management on all issues/defects that have not been resolved by the Tier 1 and 2 Support Teams. Any defect found will be logged in CA SDM and also in Rational ClearQuest (as required).

> [Table 1](#_bookmark15) outlines the incident priority levels and the time frame for response:

> <span id="_bookmark15" class="anchor"></span>Table 1: Incident Priority Levels and Time Frame for Response

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 16%" />
<col style="width: 32%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Priority Level</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Call Received</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Time Frame for Response</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Priority Level Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p><strong>Urgent</strong></p>
</blockquote></td>
<td><blockquote>
<p>During business hours</p>
</blockquote></td>
<td><blockquote>
<p>Requester will be directly contacted by Service Provider</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>An urgent incident is a catastrophic incident of an operating environment where production systems are severely impacted, down or not functioning. Under this scenario, one of the following situations may exist:</p>
</blockquote>
<ul>
<li><p>Loss of production data and no procedural work around exists.</p></li>
<li><p>Patient care and/or safety are at risk or damage is incurred.</p></li>
<li><p>Complete loss of a core organizational or</p></li>
</ul>
<blockquote>
<p>business process where work cannot reasonably continue.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>During non- business hours</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p><strong>High</strong></p>
</blockquote></td>
<td><blockquote>
<p>During business hours</p>
</blockquote></td>
<td><blockquote>
<p>Requester will be directly contacted by Service Provider</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>A high incident is a problem where a system is functioning but in a severely reduced capacity. The situation is causing:</p>
</blockquote>
<ul>
<li><p>Significant impact to portions of the business operations and productivity.</p></li>
<li><p>No loss of production data and / or a procedural work around exists.</p></li>
<li><p>The system is exposed to potential loss or interruption of service. Includes incidents that significantly impact development</p></li>
</ul>
<blockquote>
<p>and/or production, but where an alternative operation is available.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>During non- business hours</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Medium</strong></p>
</blockquote></td>
<td><blockquote>
<p>During business hours</p>
</blockquote></td>
<td><blockquote>
<p>Average of two (2) business hours or less</p>
</blockquote></td>
<td><blockquote>
<p>A medium incident is a medium-to-low impact problem which involves partial non-critical</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 16%" />
<col style="width: 32%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Priority Level</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Call Received</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Time Frame for Response</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Priority Level Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>During non- business hours</p>
</blockquote></td>
<td><blockquote>
<p>No After Hours Coverage will be provided</p>
</blockquote></td>
<td><blockquote>
<p>functionality loss. A medium incident impairs some operations but allows the user or an application to continue to function. This may be a minor incident with limited loss or no loss of functionality or impact to the user's operation and incidents in which there is an easy circumvention or avoidance by the end user.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p><strong>Low</strong></p>
</blockquote></td>
<td><blockquote>
<p>During business hours</p>
</blockquote></td>
<td><blockquote>
<p>Average of eight (8) business hours or less</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>A low incident has no impact on the quality, performance, or functionality of the system. Low incidents have minimal organizational or business impact.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>During non- business hours</p>
</blockquote></td>
<td><blockquote>
<p>No After Hours Coverage will be provided</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *NOTE: If you require further technical assistance, please notify your local IT support to log a national CA Service Desk Manager (SDM) ticket (previously a Remedy™ ticket) or contact the <span class="mark">REDACTED</span> and have them submit a national CA ticket to the Incident Area: NTL.APP.VISTA.CLINICAL REMINDERS 2_0 and we will contact you*

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To provide a means to add the HT ENROLLMENT STARTING DATE to the patient’s electronic record, a health factor that is needed.
2.  To provide a means to trigger the HT CONTINUUM OF CARE (FOLLOW-UP) clinical reminder every 6 months after the HT CONTINUUM OF CARE (INITIAL) has been done, if the patient remains on NIC (Non-Institutional Care) or Chronic Care Management (CCM) criteria.
3.  To meet our VERA requirements both NIC and CCM require q6 month CCF updates.
4.  While in the normal workday, to be able to update the note titles, and templates for clinician’s activity with the patients.
5.  To complete the consult request using the HT SCREENING CONSULT note title.
6.  To be properly integrated with VistA and *ACTIVATE* a patient via VistA Integration any time after a consult has been initiated.
7.  To check Reminder Status correctly after processing a reminder in the SAME CPRS GUI session.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The clinical reminders, reminder dialog templates, TIU note titles, and other supporting components are all elements in the established configuration of VistA and CPRS GUI. Users access CPRS from personal and shared workstations. CPRS operates against centralized instances of the VistA database.

> If desired, more specific technical information for each application may be obtained from the following locations.

> CPRS Technical Manual(s)

> [<u>http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys\_(CPRS)/cprslmtm.pdf</u>](http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprslmtm.pdf) [<u>http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys\_(CPRS)/cprsguitm.pdf</u>](http://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/cprsguitm.pdf) Clinical Reminders 2.0 Technical Manual

> [<u>http://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_4_tm.pdf</u>](http://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_4_tm.pdf) TIU Technical Manual

> [<u>http://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility\_(TIU)/tiutm.pdf</u>](http://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiutm.pdf) Health Summary Technical Manual

> [<u>http://www.va.gov/vdl/documents/Clinical/CPRS-Health_Summary/hsum_2_7_104_tm.pdf</u>](http://www.va.gov/vdl/documents/Clinical/CPRS-Health_Summary/hsum_2_7_104_tm.pdf)

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The templates described in this manual are used within the confines of CPRS GUI and VistA, both of which are well-documented elsewhere. These templates do not alter existing data flows and therefore are not discussed here.

# Fundamentals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_bookmark20" class="anchor"></span>Knowledge of encounters, reminders, and Text Integrated Utilities (TIU) is critical to make use of the products in this patch. This section provides a basic understanding of the fundamentals of these packages within CPRS and VistA. For additional information see the documents listed in section 2.1, System Configuration.

## Completing a Note

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The templates in this patch must be accessed through the Notes tab in CPRS.

1.  To create a note in CPRS, select the notes tab and click the NEW NOTE button:

![](pxrm-2-19-home-telehealth-user-manual/002.png)

2.  The 'location for current activities' window will appear, and it defaults to the CLINIC APPT tab:

> ![](pxrm-2-19-home-telehealth-user-manual/003.png)

3.  ![](pxrm-2-19-home-telehealth-user-manual/004.png)Change to the NEW VISIT tab and select the appropriate HT clinic location. Click OK to close the window. If writing a note on a patient without any contact with that patient, either phone, office or home (HBPC), then mark this visit “historical”. This has to be done at the time the note is initiated.
4.  Select a HT note title by typing “HT”. Select the appropriate HT note title. Click OK.

> ![](pxrm-2-19-home-telehealth-user-manual/005.png)

5.  The correct template will launch after clicking “OK” on the correct note title.
    1.  Two types of templates are included with the HT documentation patch. For a description and tips for each type see the next section of this guide.
6.  ![](pxrm-2-19-home-telehealth-user-manual/006.png)Once the template is completed always read and make edits before signing.
7.  Sign the note with your electronic signature, then click OK:

> CPRS Tips:

- Know the default for CPRS timing out. If CPRS times out while completing a template, the information entered into the template will be lost.
- You cannot go into another patient’s chart while working on a template, you will lose it. If you need to go into another chart before you have finished the template, open a second CPRS.

> This patch updates the name of several TIU progress note titles released by the Office of Connected Care several years ago. Below is a list of note titles released in this patch. Each should have a National template linked, so that once the note title is opened in CPRS the template will automatically open. The templates must be linked by local CACs. If a template is not displaying appropriately contact the local CAC for help.

- HT Screening Consult
- HT Assessment Treatment Plan
- HT Tech Education
- HT Intervention
- HT Monthly Monitor
- HT Periodic Evaluation
- HT Continuum of Care
- HT Caregiver Assessment
- HT Video Visit
- HT Discharge
- HT Note
- HT Telephone Case Management (not used)

## Using Templates for Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Home Telehealth notes use two types of templates, dialog templates (sometimes called flat templates or txml templates) and reminder dialog templates (sometimes called dialogs or reminders). Each type has distinct features. Below are tips for each type.

### Dialog Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In a dialog template if a required field is missed a NON-SPECIFIC required item missing message will pop up once the template is complete; shown below on the right. There are

> \(3\) of these types of templates in the HT template set.

2.  Dialog templates display “Template” in the top blue title bar.
3.  These templates are only stored as text within the patient’s record and do not have health factors or orders embedded in the template.

> ![](pxrm-2-19-home-telehealth-user-manual/007.png)

### Reminder Dialog Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reminder Dialogs are another type of template in the CPRS GUI. A reminder dialog has an alarm clock icon in front of the name (example):

![](pxrm-2-19-home-telehealth-user-manual/008.png)

4.  Reminder dialogs have three windows:
    1.  The top window is the template form (you can stretch it vertically to see and work on more items, but DO NOT COVER the 'FINISH button")
    2.  The middle window is a preview of the completed note.
    3.  The bottom window displays the specific data items to be stored in the encounter VistA (apart from the note text) once the FINISH button is selected.

> ![](pxrm-2-19-home-telehealth-user-manual/009.png)

5.  Reminder dialogs display “reminder dialog template” in the top blue title bar.
6.  With these types of templates, there is a window below the template which provides a preview of the completed note (left of the blue arrow below). When you have finished populating the template click the finish button to send the information to the unsigned progress note. You need to accurately populate information while in the template. Editing information after leaving the template will not place health factors into CPRS or will populate exactly what you entered. If for some reason your Veteran decides not be enrolled and you have begun your template, do not “cancel” you will want to “DELETE THE NOTE” otherwise health factors will be captured.

> ![](pxrm-2-19-home-telehealth-user-manual/010.png)

7.  If all REQUIRED items (noted with an asterisk) have not been addressed, A specific “required items missing” message will display to help identify which sections to go back to answer (example below). These boxes have several formats, some tell the missing and some will not). The required fields must be addressed before the FINISH button can be clicked to finish the note successfully.

![](pxrm-2-19-home-telehealth-user-manual/011.png)

8.  One advantage of reminder dialogs is that they can be resized and moved on the screen, so that you can read another note:

> ![](pxrm-2-19-home-telehealth-user-manual/012.png)

### Encounter/CPT Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An encounter is a professional contact between a patient and a health care provider vested with responsibility for diagnosing, evaluating, and treating the patient’s condition. Encounters occur in both the outpatient and inpatient setting.

9.  Contact can include face-to-face interactions or those accomplished via telecommunications technology.
10. Secure Messaging was implemented in 2012 in Primary Care, Specialty Medicine and Surgical Care. Secure Messaging can substitute for other types of communication and encounters and may improve the quality of in-person visits. See the following website for details: [<u>http://vaww.va.gov/MYHEALTHEVET/Secure_Messaging.asp</u>](http://vaww.va.gov/MYHEALTHEVET/Secure_Messaging.asp)
11. Encounters are neither occasions of service nor activities incidental to an encounter for a provider visit. For example, the following activities are considered part of the encounter itself however do not constitute encounters on their own: taking vital signs, documenting chief complaint, giving injections, pulse oximetry, etc.
12. A telephone contact between a health care provider and a patient is only considered an encounter if the telephone contact is documented and that documentation include the appropriate elements of a face-to-face encounter, namely history and clinical decision- making. Telephone encounters must be associated with a clinic, that is assigned one of the DSS Identifier telephone codes and are to be designated as count clinics. NOTE: Count refers to workload meeting the definition of an encounter or an occasion of service.
13. Program Support staff cannot enter encounters in CPRS for workload credit. They can document using the HT Tech Education Note which is a non-count clinic; or use HT Note and mark it Historical.

> Crosswalk for Clinic Location and CPT Codes, see Appendences

### Encounter Form Completion:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The Encounter Form is very important for capturing clinical work.
2.  Any clinical activity that involves professional contact (as described above) with the Veteran should be recorded in an encounter.
3.  Elements to be completed in the encounter:
    1.  Service Connection
    2.  Diagnosis
    3.  Procedure – CPT codes
4.  Professional contact can be either face to face or via telecommunications.
    1.  When a note is written related to interaction with the Veteran/Caregiver you are required to do an encounter unless the clinic is non-count.
    2.  When you do not have professional contact with the Veteran you must use the correct note title but you must click Historical to indicate that the note does not meet the requirements of an encounter.
5.  CPT Codes specific to HT activities need to be selected in the encounter form.

### Completing an Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Complete the type of visit. Choose the appropriate selection for that visit under section name. Be sure to answer the Veteran Service Connection question under the “Visit Related To” box when appropriate.

![](pxrm-2-19-home-telehealth-user-manual/013.png)

2.  Complete encounter information be selecting the appropriate tab(s) and completing the section.

![](pxrm-2-19-home-telehealth-user-manual/014.png)

### Data Objects

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Home Telehealth templates include data objects. Data objects allow for information to be pulled into the note from another part of the patient’s record.

> The new HT data objects (in the HT templates) are listed below:

- ADMISSIONS PAST YEAR
- CONSULTS PAST(6M)
- GEC IADLS (LAST)
- GEC BASIC ADLS (LAST)
- HT BARRIERS TO LEARNING
- HT BASIC ADLS
- HT CAREGIVER
- HT CATEGORY OF CARE LAST
- HT CONTINUUM OF CARE LAST
- HT EMERGENCY PRIORITY RATING
- HT ENROLLMENT START
- HT IADLS
- HT MED RECON
- HT NIC/CCM RATING LAST
- HT REMINDERS DUE
- HT VETERAN’S GOAL
- ![](pxrm-2-19-home-telehealth-user-manual/015.png)NEXT OF KIN
- OUTPT APPTS PAST YR

> The data objects are shown in the appendix; in the screen shots of the templates to the right – they are circled in *RED*.

### Health Factors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reminder Dialog Templates include over 200 health factors. Health factors allow storage of pieces of health information in the patient’s record. They are organized into categories, which can be seen on Health Summaries and in data object displays in templates.

> They can be extracted and used for reporting on reminder completion rates, performance, and workload. They are also extracted and located in the VSSC data cubes (also known as Pyramid) which allow reports to be created.

> Health factors are linked to options in reminder dialogs. Once that item is selected, the health factor is placed in the encounter form. They are displayed in the bottom window of reminder dialogs/reminder templates (example below)

> The national templates should not be edited or revised at the local or VISN level to maintain the integrity of the data collected as well as ensure any further national revisions or updates are appropriately captured and standardized. There can be changes made to the templates after their release but changes will be done at the National level for all templates. This too ensures the integrity of data pulled.

> ![](pxrm-2-19-home-telehealth-user-manual/016.png)

### HT Education Topics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Education topics are similar to health factors, except they are used to capture information specifically regarding patient education. Five new Education Topics (a parent topic and four sub- topics) are deployed in this patch linked to specific items across the new HT template set.

> VA-HOME TELEHEALTH (HT)

> VA-HOME TELEHEALTH-IN HOME MONITORING

> VA-HOME TELEHEALTH-DISEASE MGMT/PATIENT SELF-MGMT VA-HOME TELEHEALTH-MEDICATION MANAGEMENT

> VA-HOME TELEHEALTH-CAREGIVER EDUCATION/SUPPORT

> These were developed with guidance from the HT leadership. These items are stored in VISTA and would automatically display on your site's PATIENT EDUCATION Health Summary (if your site has one). Here's a sample at Puget Sound:

> ![](pxrm-2-19-home-telehealth-user-manual/017.png)

> These education topics also have an OPTIONAL rating in the template, so that you can rate the patient/caregiver’s LEVEL OF UNDERSTANDING for a specific education topic. The small LOWEST window in a reminder template shows the patient education item (2<sup>nd</sup> circle in *red* on the image below). Example:

![](pxrm-2-19-home-telehealth-user-manual/018.png)

> The selections in the “Level of Understanding” drop-down picklist are:

![](pxrm-2-19-home-telehealth-user-manual/019.png)

## HT Clinical Reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Four new CLINICAL REMINDERS for Home Telehealth are included in this patch. Each will display in the “Clinical Reminders” section of the CPRS cover sheet when it comes due.

1.  HT Continuum of Care *(Initial Continuum of Care) *(CCF, Continuum of Care Form)

> The trigger for this reminder to become “DUE” is the HT ASSESSMENT TREATMENT PLAN template which includes the enrollment start date.

- This reminder is inactivated if the patient is discharged from HT or expires (<u>the HT Discharge template must be used for discharging the patient from HT</u>).
- This reminder is resolved by completing the HT CONTINUUM OF CARE template and selecting “INITIAL” at the top of the template.
- This reminder is due only ONCE in a course of HT care (enrollment through discharge).

#### HT Continuum of Care (Follow-Up) – (triggers with a 2-week lead time)

> This reminder becomes DUE two weeks before the 6-month period for a patient that is still a HT-enrolled Veteran and who continues to meet NIC (Non-Institutional Care) criteria or CCM (Chronic Care Management) when the previous Continuum of Care was done.

- This reminder is inactivated if the patient is discharged from HT or expires (<u>the HT Discharge template must be used for discharging the patient from HT</u>).
- This reminder is inactivated if the patient is *reassessed* via use of the HT CONTINUUM OF CARE TEMPLATE and is rated DOES NOT MEET NIC CRITERIA or CCM CRITERIA, even though the patient is still enrolled in HT. If a Veteran has a change in their status and is now NIC or CCM, or if they were classified HPDP due to partial responding and their response rates improves, a new CCF will need to be done which will re-set the clinical reminder.
- This reminder is resolved by completing the HT CONTINUUM OF CARE template and selecting the "FOLLOW-UP" item at the top of the template.

#### HT Caregiver Assessment

> This reminder is triggered after the HT CONTINUUM OF CARE (INITIAL) template has been done <u>and</u> if the patient has an UNPAID CAREGIVER (an item with a health factor that is in that template).

- This reminder is inactivated if the patient is discharged from HT or expires (<u>the HT Discharge template must be used for discharging the patient from HT</u>).
- This reminder is resolved by completing the HT Caregiver Assessment template (the Caregiver Risk Assessment section, which is the set of 4 questions with 5 answers each).

#### HT Periodic Evaluation (triggers with a 2-week lead time)

> This reminder becomes DUE 166 days after the patient has a HT ENROLLMENT START DATE filed in VISTA (*that template item is in the HT ASSESSMENT TREATMENT PLAN templat*e) and can be reset by your CAC as previously noted to coincide with program polices.

- This reminder is set to trigger every 166 (or per program policy) days if the Veteran remains enrolled in HT.
- This reminder is inactivated if the patient is discharged from HT or expires (<u>the HT Discharge template must be used for discharging the patient from HT</u>).
- This reminder is resolved by completing the HT PERIODIC EVALUATION template.

## Clinical Reminder Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### How to satisfy Clinical Reminders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  A reminder will display in the “Clinical Reminders” section of the CPRS cover sheet when it becomes due. The status will display as:
    1.  “DUE NOW” indicating the intervention is due for the patient.
    2.  A date indicating the intervention is past due and was due on that date.
    3.  “DUE SOON” indicating the intervention should be addressed soon.

![](pxrm-2-19-home-telehealth-user-manual/020.png)

2.  Clicking on a reminder on the cover sheet displays the details of the reminder and the health factor that established the reminder timeline.

![](pxrm-2-19-home-telehealth-user-manual/021.png)

3.  To complete the reminder, go to the notes section, select new note, then select the appropriate clinic and progress note and then complete the assessment due. (see below example)

![](pxrm-2-19-home-telehealth-user-manual/022.png)

## How to Run a “Reminders Due” Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Reminder Due reports are reports which use the reminder logic to display a list of patients who have the reminder due for the specified timeframe in the report.

1.  Request that the facility CAC assign the appropriate staff the 6 reminders due report templates.
2.  Reminder Due reports are run from VistA, not CPRS.
3.  At the “Select” menu option, type “^Reminders due report” or access the reminder due reports option by following instructions from local CACs.

> ![](pxrm-2-19-home-telehealth-user-manual/023.png)

4.  At the Select Report Template: type in HT

![](pxrm-2-19-home-telehealth-user-manual/024.png)

5.  Your HT reminder templates will be displayed. Indicate the number of the report you wish to run.

> Select REPORT TEMPLATE:

1.  HT (4) REMINDERS SUMMARY
2.  HT C/G RISK ASSESSMENT
3.  HT CCF FOLLOW-UP
4.  HT CCF INITIAL 2
5.  HT PERIODIC EVALUATION

> Selecting number 1 will give you a summary report of all the reminders due. Numbers 2-5 will give you a report for that specific reminder.

> ![](pxrm-2-19-home-telehealth-user-manual/025.png) HT Leads: Contact your designated CAC (whoever created your reminder due report templates) at your facility when a NEW HT clinic is created, as the reminder templates are configured to HT clinics that were created by individual name when the CAC built the reminder report template.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Complete the New Mini-template for Previously Enrolled HT patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There is a new, small template for HT use only. This template is to be used ONLY on patients who are CURRENTLY ENROLLED in Home Telehealth before the new HT National Templates were installed and activated at your VA facility. This template has three purposes:

1.  To provide a means to add the HT ENROLLMENT STARTING DATE to the patient’s electronic record. This added health factor is needed:
    1.  to provide the data object for HT ENROLLMENT STARTING DATE in the HT DISCHARGE TEMPLATE (*otherwise it’ll be ‘No data available’)*
2.  To trigger the HT PERIODIC EVALUATION clinical reminder.
    1.  *CoP requires this evaluation/documentation to be done no later than 180 days from the previous evaluation however programs can set their own policies for when this is due as long as it does not exceed 180 days. The clinical reminder in the patch is currently set for 160 days to provide a lead time. CACs can adjust the default to correspond with local policies i.e. every 90 days.*
3.  To provide a means to trigger the HT CONTINUUM OF CARE (FOLLOW-UP) clinical reminder every 6 months after the HT CONTINUUM OF CARE (INITIAL) has been done, if the patient continues to meet NIC (Non-Institutional Care) or Chronic Care Management (CCM) criteria.

> The local CAC will notify the site Lead or Program Manager when the patch is loaded and ready for use. It should be used to enter the appropriate information and date for the three items requested.

> Staff should notify the HT site Lead when this template has been completed for ALL Home Telehealth patients currently enrolled for which the HT ASSESSMENT TREATMENT PLAN TEMPLATE was not documented. This template will be phased out (removed) when all patients that need this documentation has been done. The local CAC will need to remove this template from the shared folder in CPRS.

> Programs should devise a system to determine which patients the template has been completed. A TIU report for the 3 health factors can be created by the local CAC. Veterans being enrolled when the templates come out will not need the mini template (as long as the NEW Template that captures the information is in use.)

> Staff should use the "HT Note" title to enter this template in CPRS. MARK IT HISTORICAL. Staff will not need to complete an encounter for this one time note.

1.  Find and open the template named <u>HT Template for Previously Enrolled Patients</u> from the Notes tab in CPRS. Contact the local CAC to identify where the template is located within CPRS.

![](pxrm-2-19-home-telehealth-user-manual/026.png)

2.  First item in the template is documentation of the date the veteran was enrolled in Home Telehealth

![](pxrm-2-19-home-telehealth-user-manual/027.png)

- Make sure to fill out the DAY of the month as well as the correct month and year.
3.  The second item opens to the NIC/CCM categorization. The “YES” answers have a required fill-in for the date. The “NO” answer doesn’t expand. If no, they are likely classified HPDP, and the CCF does not have to be repeated unless there is a change in their condition.

![](pxrm-2-19-home-telehealth-user-manual/028.png)

> ![](pxrm-2-19-home-telehealth-user-manual/029.png)

- If it is a newly enrolled patient, enter their date of admission when the initial Continuum of Care form was completed.
- Make sure to fill out the DAY of the month as well as the correct month and year.
- To meet our VERA requirements both NIC and CCM require CCF updates every 6 months.
4.  The 3<sup>rd</sup> item asks when the LAST periodic evaluation was done which will trigger the HT PERIODIC EVALUATION clinical reminder on the appropriate date.
1.  If a newly enrolled patient is not yet due for a periodic evaluation because they have been in the program less than the number of days required for review per policy (90, 120, 180 days etc.), still answer YES and enter the enrollment date as the date of last periodic review.
2.  If “No” is documented here, a clinical reminder will automatically populate that a Periodic Evaluation is due now – despite the fact the patient has only been in the program less than the required number of days for review. The ‘no’ item does not expand any further.
3.  The local site CAC can adjust the time frame the HT PERIODIC EVALUATION clinical reminder is due depending on your local policy.

![](pxrm-2-19-home-telehealth-user-manual/030.png)

- Make sure to fill out the DAY of the month as well as the correct month and year.

![](pxrm-2-19-home-telehealth-user-manual/031.png)

> 10\. When done, click the FINISH button at the bottom of the form. If you still have questions about this template, please contact your site’s HT Lead.

> X WRONG NOTE/WRONG PATIENT: If a template is documented on the wrong patient make sure data cleanup occurs, so encounter data as well as the note is removed from the patient record. Notify your HIMS (Health Information Management Service) to do this cleanup.

# Templates and Program Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HT program services begin when consults are completed and Veterans are screened. The “HT Screening Consult” note is completed and if the Veteran is enrolled, the Care Coordinator proceeds with the enrollment process and required documentation using the templates and note titles covered in this user guide. VISN and local program leadership should ensure staff have been properly trained on choosing the appropriate clinic location, note title, and

> template. Training is also provided by the Implementation Team.

> Below are the new templates with guidance on their use. They appear in order of the enrollment process.

## Home Telehealth Consult Request.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new template will be embedded in the local consult order for Home Telehealth services. The provider will click on the consult order and launch the template: (Sites have found it helpful to inform their Providers that they will see a new version of the HT Consult.)

> Below is the Enrollment Consult Template

> ![](pxrm-2-19-home-telehealth-user-manual/032.png)

![](pxrm-2-19-home-telehealth-user-manual/033.png)

> ![](pxrm-2-19-home-telehealth-user-manual/034.png)

> The consult should be completed by HT staff using the HT SCREENING CONSULT note title; this title generates the progress note and is used to CLOSE the consult.

> There are two ways to access the consult request for consult completion:

1.  Completing the HT SCREENING CONSULT note from the Consult tab in CPRS
2.  Completing the HT SCREENING CONSULT note from the Notes tab in CPRS

### Completing the HT SCREENING CONSULT note from the CPRS consult tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you are certain that your patient does not meet the enrollment criteria, do not open the template that closes the consult because this will use your time unnecessarily. We recommend that you cancel the consult (or follow local guidance) and add comments to the provider why the Veteran is not a candidate for enrollment.

1.  If processing a “new consult” alert, the CONSULTS tab will open on that specific consult request or the consult can be accessed by clicking on the CONSULTS tab, then select the HT consult request.
    1.  The local consult may have a different name than displayed in the screenshots

![](pxrm-2-19-home-telehealth-user-manual/035.png)

2.  Click on ACTION, then drop down to CONSULT RESULTS, then mouse over to “COMPLETE/UPDATE Results”:

![](pxrm-2-19-home-telehealth-user-manual/036.png)

3.  Select the appropriate Visit, Clinic Location (was the encounter by phone, in clinic or Veterans’ home), and date/time (if veteran isn't an inpatient). Click “OK”.
4.  Select the “HT SCREENING CONSULT Note” note title.
    1.  This is the only note title that should be used to complete/close the consult. ![](pxrm-2-19-home-telehealth-user-manual/037.png) You can set this single HT consults note title as a DEFAULT note title on the CONSULTS tab. Here's how to do this:
1.  ![](pxrm-2-19-home-telehealth-user-manual/038.png)Go to TOOLS, then OPTIONS (Each VA site will have a different list of TOOLS menu items, but all have OPTIONS):
2.  Go to the NOTES tab and click the “Document Titles” button:

![](pxrm-2-19-home-telehealth-user-manual/039.png)

3.  Under “Document class”, select CONSULTS from the drop-down pick list:

![](pxrm-2-19-home-telehealth-user-manual/040.png)

4.  Select the HT SCREENING CONSULT Note title.
5.  Click the ADD (the ADD button is an option prior to adding the document title) button to move that note title to the RIGHT window ('your list of titles').

> The Note Title will move to the right window.

![](pxrm-2-19-home-telehealth-user-manual/041.png)

6.  To set it as the DEFAULT note title on the CONSULTS tab (so that it is automatically preselected as the title to close your consult requests), click on the title in the right-hand window, and then click the 'SET AS DEFAULT' button.

![](pxrm-2-19-home-telehealth-user-manual/042.png)

7.  Now click the OK button to save your changes.

> (If you want to *REMOVE* a title, simply select it so it is highlighted in the right-hand window, and then click the *REMOVE* button.)

### Completing the HT SCREENING CONSULT note from the CPRS Notes tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select the NOTES tab
2.  Click on NEW NOTE

![](pxrm-2-19-home-telehealth-user-manual/043.png)

3.  Select the correct clinic location. The correct clinic to select would be the HT Screening Office or Telephone or Home; depending on where the vet was screened.
4.  Select the HT SCREENING CONSULT note title, as it is the ONLY HT Note Title that links to a consult request. Once the note title is selected, a list of consult requests for that patient will display.
    1.  Any consult for that patient that the author has authorization to complete will display, so other consults may be in the list. Ensure to only select the Home Telehealth consult.

![](pxrm-2-19-home-telehealth-user-manual/044.png)

5.  Highlight the consult request and then click OK to make the link to the consult and then close the window.

![](pxrm-2-19-home-telehealth-user-manual/045.png)

6.  The template will open.

![](pxrm-2-19-home-telehealth-user-manual/046.png)

> ![](pxrm-2-19-home-telehealth-user-manual/047.png)

> ![](pxrm-2-19-home-telehealth-user-manual/048.png)

> ![](pxrm-2-19-home-telehealth-user-manual/049.png)

## TECH EDUCATION AND INSTALLATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below are the Tech Education and Installation Template

> ![](pxrm-2-19-home-telehealth-user-manual/050.png)This template incorporates what is usually discussed with Veterans/Caregivers at enrollment related to technology use. It can be used by support staff.

> ![](pxrm-2-19-home-telehealth-user-manual/051.png)

## ASSESSMENT TREATMENT PLAN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below is the Assessment Treatment Plan Template

> The screen shots taken below are in sequence to how the Template flows.

![](pxrm-2-19-home-telehealth-user-manual/052.png)

> ![](pxrm-2-19-home-telehealth-user-manual/053.png)Boxes will open and may ask additional information for example, when you hit the box “Veteran consents to participate in the HT Program this is what you will see:

> The template training provided by the Implementation Team discusses various items of interest in the templates such as what goes in the “Discussion details” box and why.

> Note: The Joint Commission requires all providers to do an assessment of oxygen safety. This is included above noted by the arrow.

> ![](pxrm-2-19-home-telehealth-user-manual/054.png)Next is the following

> As stated previously, some fields are optional, and remember to add detail in text boxes.

> ![](pxrm-2-19-home-telehealth-user-manual/055.png)

> Medication Interventions is located after Medication Management which ties the topics together in one place

![](pxrm-2-19-home-telehealth-user-manual/056.png)

> ![](pxrm-2-19-home-telehealth-user-manual/057.png)

> Living Arrangements/Environmental Safety is mostly about environmental safety, not living arrangements. The CCF (Continuum of Care Form) identifies some of this information; you may decide to go over living arrangements and the Veterans support system in your summary.

![](pxrm-2-19-home-telehealth-user-manual/058.png)

> Note: The CCF template can be launched here or can be a free-standing note. If you put it here the note can be very long. If you do not include it here, you will need to ensure clinical information located in the form is discussed in your assessment in order to be comprehensive and identify problems the Veteran is facing. Screen shots of the CCF are below.

> The Caregiver Risk Assessment is linked to the Zarit Burden Scale if there is an unpaid caregiver. This template can also be done as a free-standing note.

> Referrals for Caregiver/Veteran assistance opens to many choices related to assistance that might be needed for the Veteran and or Caregiver

> ![](pxrm-2-19-home-telehealth-user-manual/059.png)

> Please refer to the Continuity of Operations Guidance (CooP) located on the HT Web page [<u>http://vaww.telehealth.va.gov/pgm/ht/index.asp</u>](http://vaww.telehealth.va.gov/pgm/ht/index.asp) . The template not only includes determining a level of priority for contacting a Veteran after a disaster but also includes discussing disaster planning with them which is also part of CooP.

> ![](pxrm-2-19-home-telehealth-user-manual/060.png)

> This completes the Admission Assessment Template. If you hit “Phone” on “Type of encounter” it populates your encounter for you.

#### Edit your note in CPRS before signing it.

> You can paste your own sub-templates at this time into the document but this should not replace completing required fields in the template as health factors are imbedded.

## CONTINUUM OF CARE FORM (CCF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below is the Continuum of Care Form Template

> ![](pxrm-2-19-home-telehealth-user-manual/061.png)For help completing the CCF refer to the Continuum of Care Guidance and Patient Participation Guidance documents on the HT Home page [<u>http://vaww.telehealth.va.gov/pgm/ht/index.asp</u>](http://vaww.telehealth.va.gov/pgm/ht/index.asp)

> Pay attention to “Assessment type”, you only choose “Initial assessment” one time, the rest are follow up. The date you complete the CCF updates the clinical reminder.

> Note: if you have Veterans classified HPDP due to partial respondering you will not get a clinical reminder for the CCF however if their response rates improve to over 70% in a 3 month period do a CCF (NOT INITIAL..IT IS STILL A FOLLOW UP) to identify the classification to NIC or CCM (change it in Vendor software too so they get counted for VERA reimbursement).

> The CCF template pulls in the Next of Kin from CPRS for your convenience. Although the template allows you to update the information, it does NOT update the change in CPRS. You should follow local procedures for updating demographics.

![](pxrm-2-19-home-telehealth-user-manual/062.png)

> ![](pxrm-2-19-home-telehealth-user-manual/063.png)

> ![](pxrm-2-19-home-telehealth-user-manual/064.png)

> ![](pxrm-2-19-home-telehealth-user-manual/065.png)

> ![](pxrm-2-19-home-telehealth-user-manual/066.png)

> ![](pxrm-2-19-home-telehealth-user-manual/067.png)

## CAREGIVER RISK ASSESSMENT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below is the Caregiver Assessment Template:

> The Zarit Caregiver Burden Scale is embedded in the Caregiver Risk Assessment template.

> ![](pxrm-2-19-home-telehealth-user-manual/068.png)![](pxrm-2-19-home-telehealth-user-manual/069.png)The Caregiver Risk Assessment MUST be completed if the Veteran has an unpaid caregiver. Sometimes staff members have found that the caregiver feels uncomfortable answering these questions in front of the Veteran. You can be creative and have this already printed out for the caregiver to complete while you are talking with the veteran, or even perhaps mail this to the caregiver with a self-addressed stamped envelope.

> Note: This clinical reminder is different. The reminder is active when you hit the radial button “Unable to screen” but does not show up in CPRS for 7 days allowing you time to try and reach the caregiver. If you do not complete the screening, the clinical reminder stays on until you do.

> (Note: other staff doing the Zarit Burden, use the same template so there is a possibility the clinical reminder will be completed by someone other than HT staff, most likely Social Workers)

> ![](pxrm-2-19-home-telehealth-user-manual/070.png)The intent here is to assess how our caregivers are doing, not just completing a form. Anytime you sense a caregiver is not doing well you can complete the Zarit Burden and make a referral to Social Work.

## INTERVENTION NOTE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following is the HT Intervention Note (684).

> The intervention note is used anytime an intervention is made based on out of range responses received from the Veteran’s technology.

![](pxrm-2-19-home-telehealth-user-manual/071.png)

> Any subjective or objective information that is not a measurement would go into the additional information text box. Clinicians then document (in the assessment text box) their assessment based upon any of the above information. The “Intervention/Plan:” section is what the care coordinator did, suggest, or recommends. It should include Veterans input and responses.

> Documentation should also include communication and collaboration with other staff or programs, updates, or revisions to the Veteran’s plan of care and/or services.

## MONTHLY MONITOR NOTE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below is the Monthly Monitor Note.

> This note does not require provider cosigning and should not have clinical information. This is the (683) note for counting enrollees nationwide, is required for VERA reimbursement, and allows staff to get work load credit for time spent reviewing Veteran alerts to their daily session received from technology.

![](pxrm-2-19-home-telehealth-user-manual/072.png)

> This is not like other templates; it is a boiler plate which is populated. Most programs use a “Group Note” to enter this on all their Veterans. It is to be entered near the end of the month. There used to be guidance that a Diagnosis is required in this note however National HIMS (Health Information Management Service) guidance has exempted this for HT since there is no billing associated with this. Follow your local guidance if different.

> Contact your local “Group Note” specialist if you do not know how to use “Group Notes”.

## PERIODIC EVALUATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Two full templates are embedded in the Periodic Evaluation Template:

1.  HT Caregiver High Risk Screen *(optional section)*
2.  HT Caregiver/Veteran Referral template *(optional section)*

> The Periodic Evaluation Template is used to re-assess/evaluate the Veterans status and update the Veteran’s provider and plan of care. It has to be completed no later than every 180 days. A

> program that’s polices call for reevaluation at a different time frame i.e. every 90 days, can have the reminders set accordingly (but NOT to exceed 180 days).

> ![](pxrm-2-19-home-telehealth-user-manual/073.png)Below is the Periodic Evaluation

> Note: at the top, it will display if there are clinical reminders due and the date last HT CCF was completed. THERE IS NO LINK TO THE CCF FROM THIS TEMPLATE.

> The first question you come to is “Veterans Current HT Category of Care”. If the CCF is due, in order to accurately answer this question, you will need to complete the form before you populate the template. Some options include: you can complete the CCF template using the CCF Form

> ![](pxrm-2-19-home-telehealth-user-manual/074.png)note title and mark the encounter historical; you can make it an addendum to the Periodic Note as long as you have the accurate information to identify the current level of care.

> This template has "Veteran Health Education". This box opens to extensive options for education related to Home Telehealth-specific, or General Topics, see below.

> This was not put in the Admission Assessment Treatment Plan due to its length; it is expected the initial clinical summary and plan of care will identify education given upon admission.

> ![](pxrm-2-19-home-telehealth-user-manual/075.png)Including this sub template in the Periodic template accounts for more time to have worked with the Veteran and cover education provided during the review period and beyond.

> The above “Caregiver utilization of referrals” is only used if a referral has been previously submitted. Also, please note at this point you need to revisit the caregiver risk assessment and referral if the Veteran has an unpaid caregiver.

## EMERGENCY MANAGEMENT CLASSIFICATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Emergency Management Classification is re-addressed in every periodic evaluation or according to program polices.

> The Disaster Plan is also completed reflecting information or assistance extended to the Veteran or Caregiver.

![](pxrm-2-19-home-telehealth-user-manual/076.png)

## DISCHARGE TEMPLATE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below is the Discharge Template

> This is to be completed when the Veteran is discharged from the program. Remember, doing this note turns off all clinical reminders. For this reason if you end up re enrolling a Veteran, even within 30 days, an Admission Assessment and Treatment Plan Template will need to be completed.

> ![](pxrm-2-19-home-telehealth-user-manual/077.png)

> ![](pxrm-2-19-home-telehealth-user-manual/078.png)

## Other:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VIDEO VISIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below is the Video Visit Template

> Video visits have not occurred in HT during the previous contract with Vendors (prior to June 2017). With the new 2017 contract, Video Visits is (or will be, depending on the Vendor) an

> ![](pxrm-2-19-home-telehealth-user-manual/079.png)option. However National Telehealth guidance has not been provided at the time of this manuals publication.

> ![](pxrm-2-19-home-telehealth-user-manual/080.png)

> Troubleshooting

> *N/A*

# a. Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><em><strong>Abbreviation</strong></em></p>
</blockquote></th>
<th><blockquote>
<p><em><strong>Definition</strong></em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CoP</p>
</blockquote></td>
<td><blockquote>
<p>Conditions of Participation</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CPT</p>
</blockquote></td>
<td><blockquote>
<p>Current Procedural Terminology</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GEC</p>
</blockquote></td>
<td><blockquote>
<p>Geriatric E Care</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td><blockquote>
<p>Health Summary (VistA software package)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GUI</p>
</blockquote></td>
<td><blockquote>
<p>Graphical User Interface</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT</p>
</blockquote></td>
<td><blockquote>
<p>Home Telehealth</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICD-9</p>
</blockquote></td>
<td><blockquote>
<p>International Classification of Diseases</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OCC</p>
</blockquote></td>
<td><blockquote>
<p>Office of Connected Care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TIU</p>
</blockquote></td>
<td><blockquote>
<p>Text Integration Utilities (Vista software package)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Appendix

> Crosswalk Note Titles, Stop Codes, and Definitions Option 1 programs

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 29%" />
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
<p>685</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>371</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>HT Screening Consult</p>
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
<p>686</p>
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
<p>686</p>
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
<p><strong>NOTE:</strong> Use <strong>ONLY</strong> to</p>
<p>document patient encounters in response to alerts from vendor data- not to be used as generic note, and not to be used with</p>
<p>VIDEO visit.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 29%" />
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
<p>685</p>
</blockquote></th>
<th><blockquote>
<p><strong>HT Monthly Monitor Note</strong></p>
</blockquote></th>
<th><blockquote>
<p>HT Monthly Monitor Template</p>
</blockquote></th>
<th><blockquote>
<p>This progress note contains information about the monthly monitoring of patients assigned non-video messaging devices.</p>
<p><strong>NOTE:</strong> To be completed for patients to capture workload for daily review of HT data. Please see the HT Operations manual for more detailed instructions on how to properly use this encounter.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>HT VIDEO VISIT</strong></p>
</blockquote></td>
<td><blockquote>
<p>685</p>
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
<p><strong>NOTE:</strong> Must meet certain documentation requirements of replicating a face-to-face visit or it can’t be coded as 179</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT ASSESS TX PLAN HM</strong></p>
</blockquote></td>
<td><blockquote>
<p>Home 118</p>
</blockquote></td>
<td rowspan="2"><blockquote>
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
<td><blockquote>
<p>TC 686</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT ASSESS TX PLAN OF</strong></p>
<p><strong>or</strong></p>
<p><strong>HT ASSESS TX PLAN OFC</strong></p>
</blockquote></td>
<td><blockquote>
<p>Clinic 685</p>
</blockquote></td>
<td></td>
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
<p>686</p>
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
<p>685</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT VISIT HM</strong></p>
</blockquote></td>
<td><blockquote>
<p>118</p>
</blockquote></td>
<td><blockquote>
<p>685</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 13%" />
<col style="width: 1%" />
<col style="width: 11%" />
<col style="width: 1%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3" rowspan="5"><blockquote>
<p><strong>SECOND, select a Note Title/Template (right) to pair with the clinic location (above)</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>HT Discharge Note</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>HT</p>
<p>Discharge Template</p>
</blockquote></th>
<th><blockquote>
<p>This Document contains closure of the patients’ case and discharge from the HT program. Basically, this note is a discharge summary.</p>
<p>NOTE: Designed to facilitate closing the case of a HT patient. May have an encounter attached to it if the discharge is done by telephone or office visit. Will not have an encounter if patient is not present.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>HT Note</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>N/A</p>
</blockquote></th>
<th><blockquote>
<p>Generic Note title to encompass all other HT activities. This note title does not have a template.</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>HT Periodic Evaluation Note</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>HT Periodic Evaluation Template</p>
</blockquote></th>
<th><blockquote>
<p>Periodic review and upgrade of the plan of care</p>
<p>NOTE: Summarization of care for a period of time. Interval dependent on VISN/Program.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>HT Continuum of Care Note</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>HT</p>
<p>Continuum of Care Template</p>
</blockquote></th>
<th><blockquote>
<p>Note title to be used with the Continuum of Care clinical reminder dialog</p>
<p>NOTE: Initial CCF will be included in the Assessment Treatment Plan template. This note title to be used thereafter.</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>HT Caregiver Assessment</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>HT</p>
<p>Caregiver Assessment Template</p>
</blockquote></th>
<th><blockquote>
<p>NOTE: Will combine both the High-risk Screen &amp; referral for assistance in one note title and template.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="8"><blockquote>
<p>Additional Note Titles in the Patch</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT CASE MGMT TC</strong></p>
<p><strong>or</strong></p>
<p><strong>HT CASE MGMT PHONE</strong></p>
<p><strong>or</strong></p>
<p><strong>HT CASE MGMT PH</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>HT</p>
<p>Telephone Case Management</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>N/A</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>This note title is no longer approved by the Office of Connected Care. If they are available through the patch, do not use them. Use the HT Note title</p>
<p>.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT CASE MGMT OFC</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>HT</p>
<p>Telephone Case Management</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>N/A</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>This note title is no longer approved by the Office of Connected Care. If they are available through the patch, do not use them. Use the HT Note title</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Crosswalk Note Titles, Stop Codes, and Definitions Option 2 programs

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 29%" />
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
</blockquote></th>
<th><blockquote>
<p><strong>HT Monthly Monitor Note</strong></p>
</blockquote></th>
<th><blockquote>
<p>HT Monthly Monitor Template</p>
</blockquote></th>
<th><blockquote>
<p>This progress note contains information about the monthly monitoring of patients assigned non-video messaging devices.</p>
<p><strong>NOTE:</strong> To be completed for patients to capture workload for daily review of HT data. Please see the HT Operations manual for more detailed instructions on how to properly use this encounter.</p>
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
<td>179</td>
<td><blockquote>
<p>HT Video Visit Note</p>
</blockquote></td>
<td><blockquote>
<p>HT Video Visit Template</p>
</blockquote></td>
<td><blockquote>
<p>This document contains information about any visit over a video device (tele-Monitor/ Videophone) that meets required criteria for secondary Stop Code xxx179</p>
<p><strong>NOTE:</strong> Must meet certain documentation requirements of replicating a face-to-face visit or it can’t be coded as 179</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT ASSESS TX PLAN HM</strong></p>
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
<td>685</td>
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
<td>685</td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT VISIT HM</strong></p>
</blockquote></td>
<td><blockquote>
<p>118 or Prog Dep</p>
</blockquote></td>
<td>685</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3" rowspan="5"><blockquote>
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
<p>NOTE: Designed to facilitate closing the case of a HT patient. May have an encounter attached to it if the discharge is done by telephone or office visit. Will not have an encounter if patient is not present.</p>
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
<p>Generic Note title to encompass all other HT activities. This note title does not have a template.</p>
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
<p>NOTE: Initial CCF will be included in the Assessment Treatment Plan template. This note title to be used thereafter.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>HT</p>
<p>Caregiver Assessment</p>
</blockquote></th>
<th><blockquote>
<p>HT</p>
<p>Caregiver Assessment</p>
<p>Template</p>
</blockquote></th>
<th><blockquote>
<p>NOTE: Will combine both the High-risk Screen &amp; referral for</p>
<p>assistance in one note title and template.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="6"><blockquote>
<p>Additional Note Titles</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HT CASE MGMT TC</strong></p>
<p><strong>or</strong></p>
<p><strong>HT CASE MGMT PHONE</strong></p>
<p><strong>or</strong></p>
<p><strong>HT CASE MGMT PH</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>HT</p>
<p>Telephone Case Management</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>This note title is no longer approved by the Office of Connected Care. If they are available through the patch, do not use them. Use the HT Note title.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HT CASE MGMT OFC</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>HT</p>
<p>Telephone Case Management</p>
</blockquote></td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
<td><blockquote>
<p>This note title is no longer approved by the Office of Connected Care. If they are available through the patch, do not use them. Use the HT Note title</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Clinic Location</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>MD/NP/PA CPT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>RN CPT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>SW CPT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>CPT Comments</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Note Title / Template</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>HT ASSESS TX PLAN OFC</p>
</blockquote></td>
<td><blockquote>
<p>Face to Face</p>
</blockquote></td>
<td><blockquote>
<p>Face to Face</p>
</blockquote></td>
<td><blockquote>
<p>Face to Face</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Records clinical activities with patient by licensed practitioner</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>HT Assessment Treatment Plan</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>99201 – 99215</p>
</blockquote></td>
<td><blockquote>
<p>99211</p>
</blockquote></td>
<td><blockquote>
<p>99499</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="5"><blockquote>
<p>HT ASSESS TX PLAN TC (PHONE)</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p>HT is one of the programs under the Office of Patient Care Services that is exempt from the time elements as follows:</p>
<p>The codes can be used when a call is initiated by a provider and the time elements will not apply - such as a visit within past seven (7) days - many of our programs require multiple calls within a seven (7) day period.</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p>HT Assessment Treatment Plan</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>99441 – 99443</p>
</blockquote></td>
<td><blockquote>
<p>98966, 98967,</p>
<p>98968</p>
</blockquote></td>
<td><blockquote>
<p>98966, 98967,</p>
<p>98968</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>99441: 5-10</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98966: 5-10</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98966: 5-10</p>
<p>mins. of medical discussion</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>99442: 11 -20</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98967: 11 -20</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98967: 11 -20</p>
<p>mins. of medical discussion</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>99443: 21 -30</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98968: 21 -30</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98968: 21 -30</p>
<p>mins. of medical discussion</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT TECH EDUCATION</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC.</p>
</blockquote></td>
<td><blockquote>
<p>HT Tech Education</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>HT INTERVENTION</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Records clinical activities with patient by licensed practitioner (See</p>
<p>above)</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>HT Intervention</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>99441 – 99443</p>
</blockquote></td>
<td><blockquote>
<p>98966, 98967,</p>
<p>98968</p>
</blockquote></td>
<td><blockquote>
<p>98966, 98967,</p>
<p>98968</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT MONTHLY MONITOR</p>
</blockquote></td>
<td><blockquote>
<p>99091</p>
</blockquote></td>
<td><blockquote>
<p>99091</p>
</blockquote></td>
<td><blockquote>
<p>99091</p>
</blockquote></td>
<td><blockquote>
<p>Analysis and interpretation of physiologic data by the physician or other qualified health care professional. The data (e.g., blood pressure) is stored digitally and may be transmitted by the patient and/or the</p>
<p>caregiver to the</p>
</blockquote></td>
<td><blockquote>
<p>HT Monthly Monitor</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th></th>
<th></th>
<th><blockquote>
<p>physician.</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT VIDEO VISIT</p>
</blockquote></td>
<td><blockquote>
<p>99201 – 99215</p>
<p>GT</p>
</blockquote></td>
<td><blockquote>
<p>99211 GT</p>
</blockquote></td>
<td><blockquote>
<p>99499 GT</p>
</blockquote></td>
<td><blockquote>
<p>The CPT code</p>
<p>used when this service is delivered face to face is used along with the modifier to denote the telecomm delivery of care</p>
<p>GT = interactive telecomm</p>
</blockquote></td>
<td><blockquote>
<p>HT Video Visit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VISIT TC (PHONE)</p>
</blockquote></td>
<td><blockquote>
<p>Telephone99441</p>
<p>– 99443</p>
</blockquote></td>
<td><blockquote>
<p>Telephone98966, 98967, 98968</p>
</blockquote></td>
<td><blockquote>
<p>Telephone98966, 98967, 98969</p>
</blockquote></td>
<td><blockquote>
<p>CPT Codes are dependent on what is done, face to face in the office, in the home, or on the telephone.</p>
</blockquote></td>
<td><blockquote>
<p>HT Note (no template)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VISIT OFC</p>
</blockquote></td>
<td><blockquote>
<p>99201 – 99215</p>
</blockquote></td>
<td><blockquote>
<p>99211</p>
</blockquote></td>
<td><blockquote>
<p>99499</p>
</blockquote></td>
<td><blockquote>
<p>These are real face to face visits in the office.</p>
</blockquote></td>
<td><blockquote>
<p>HT Note (no template)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VISIT HOME</p>
</blockquote></td>
<td><blockquote>
<p>99341 – 99350</p>
</blockquote></td>
<td><blockquote>
<p>G0154</p>
</blockquote></td>
<td><blockquote>
<p>G0155</p>
</blockquote></td>
<td><blockquote>
<p>These are real face to face visits in the home.</p>
</blockquote></td>
<td><blockquote>
<p>HT Note</p>
<p>(no template)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"></td>
<td></td>
<td></td>
<td></td>
<td rowspan="2"></td>
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
<td><blockquote>
<p>HT CAREGIVER ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>TBD</p>
</blockquote></td>
<td><blockquote>
<p>TBD</p>
</blockquote></td>
<td><blockquote>
<p>In development. Recommended that these be captured as collateral and not</p>
<p>under the patient.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> 2<sup>nd</sup> CPT Crosswalk without added column with note titles, easier formatting

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Clinic Location *</strong></p>
</blockquote></th>
<th><strong>MD/NP/PA CPT</strong></th>
<th><blockquote>
<p><strong>RN CPT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>SW CPT</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>CPT Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>HT ASSESS TX PLAN OFC</p>
</blockquote></td>
<td><blockquote>
<p>Face to Face</p>
</blockquote></td>
<td><blockquote>
<p>Face to Face</p>
</blockquote></td>
<td><blockquote>
<p>Face to Face</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Records clinical activities with patient by licensed practitioner</p>
</blockquote></td>
</tr>
<tr class="even">
<td>99201 – 99215</td>
<td><blockquote>
<p>99211</p>
</blockquote></td>
<td><blockquote>
<p>99499</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="5"><blockquote>
<p>HT ASSESS TX PLAN TC (PHONE)</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p>CCHT is one of the programs under the Office of Patient Care Services that is exempt from the time elements as follows:</p>
<p>The codes can be used when a call is initiated by a provider and the time elements will not apply - such as a visit within past seven (7) days - many of our programs require multiple calls within a seven</p>
<p>(7) day period.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>99441 – 99443</td>
<td><blockquote>
<p>98966, 98967,</p>
<p>98968</p>
</blockquote></td>
<td><blockquote>
<p>98966, 98967,</p>
<p>98968</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>99441: 5-10</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98966: 5-10</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98966: 5-10</p>
<p>mins. of medical discussion</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>99442: 11 -20</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98967: 11 -20</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98967: 11 -20</p>
<p>mins. of medical discussion</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>99443: 21 -30</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98968: 21 -30</p>
<p>mins. of medical discussion</p>
</blockquote></td>
<td><blockquote>
<p>98968: 21 -30</p>
<p>mins. of medical discussion</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT TECH EDUCATION</p>
</blockquote></td>
<td colspan="4"><blockquote>
<p>NO ENCOUNTER FORM ATTACHED TO NON-COUNT CLINIC.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>HT INTERVENTION</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td><blockquote>
<p>Telephone</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Records clinical activities with patient by licensed practitioner (See above)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>99441 – 99443</td>
<td><blockquote>
<p>98966, 98967,</p>
<p>98968</p>
</blockquote></td>
<td><blockquote>
<p>98966, 98967,</p>
<p>98968</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT MONTHLY MONITOR</p>
</blockquote></td>
<td><blockquote>
<p>99091</p>
</blockquote></td>
<td><blockquote>
<p>99091</p>
</blockquote></td>
<td><blockquote>
<p>99091</p>
</blockquote></td>
<td><blockquote>
<p>Analysis and interpretation of physiologic data by the physician or other qualified health care professional. The data (e.g., blood pressure) is stored digitally and may be transmitted by the patient and/or the</p>
<p>caregiver to the physician.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HT VIDEO VISIT</p>
</blockquote></th>
<th><blockquote>
<p>99201 – 99215</p>
<p>GT</p>
</blockquote></th>
<th><blockquote>
<p>99211 GT</p>
</blockquote></th>
<th><blockquote>
<p>99499 GT</p>
</blockquote></th>
<th><blockquote>
<p>The CPT code used when this service is delivered face to face is used along with the modifier to denote the telecomm delivery of care</p>
<p>GT = interactive telecomm</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>HT VISIT TC (PHONE)</p>
</blockquote></td>
<td><blockquote>
<p>Telephone99441</p>
<p>– 99443</p>
</blockquote></td>
<td><blockquote>
<p>Telephone98966, 98967, 98968</p>
</blockquote></td>
<td><blockquote>
<p>Telephone98966, 98967, 98969</p>
</blockquote></td>
<td><blockquote>
<p>Phone definition noted above.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HT VISIT OFC</p>
</blockquote></td>
<td><blockquote>
<p>99201 – 99215</p>
</blockquote></td>
<td><blockquote>
<p>99211</p>
</blockquote></td>
<td><blockquote>
<p>99499</p>
</blockquote></td>
<td><blockquote>
<p>These are real face to face visits in the office.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HT VISIT HOME</p>
</blockquote></td>
<td><blockquote>
<p>99341 – 99350</p>
</blockquote></td>
<td><blockquote>
<p>G0154</p>
</blockquote></td>
<td><blockquote>
<p>G0155</p>
</blockquote></td>
<td><blockquote>
<p>These are real face to face visits in the home.</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"></td>
<td></td>
<td></td>
<td></td>
<td rowspan="2"></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TBD</p>
</blockquote></td>
<td><blockquote>
<p>CCHT CAREGIVER ASSESSMENT</p>
</blockquote></td>
<td><blockquote>
<p>TBD</p>
</blockquote></td>
<td><blockquote>
<p>TBD</p>
</blockquote></td>
<td><blockquote>
<p>In development. Recommended that these be captured as collateral and not under the patient.</p>
</blockquote></td>
</tr>
</tbody>
</table>