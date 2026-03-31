---
title: Military Eye Vision Injury Version 1 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: 
app_code: ROEV
app_name: "Registry: Military Eye Vision Injury (MEVIR)"
section: CLI
app_status: active
pkg_ns: ROEV
patch_ver: 1
patch_id: ROEV*1
group_key: "ROEV:ROEV:1"
file_numbers: []
security_keys: []
menu_options: 0
description: > The Department of Veterans Affairs (VA) established the VA Eye Injury Data Store (VA EIDS) (formerly called the Military Eye Injury Registry, or MEVIR) in 2012 to transfer Veteran eye injury data into the Defense and Veterans Eye Injury and Vision Registry (DVEIVR). DVEIVR was developed by the Dep
audience: 
keywords: 
  - strong
  - table
  - blockquote
  - contents
  - military
  - injury
  - guide
  - encounter
  - vision
  - version
page_count: 0
word_count: 6837
section_count: 29
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2015
revision_count: 2
revision_newest: 08/27/2015
revision_oldest: 08/24/2015
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg_Mil_Eye_Vision_Injury_(MEVIR)/va_eidsv2_userguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg_Mil_Eye_Vision_Injury_(MEVIR)/va_eidsv2_userguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=216"
---

# VA Eye Injury Data Store (VA EIDS) User Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [VA Eye Injury Data Store (VA EIDS) User Guide](#va-eye-injury-data-store-va-eids-user-guide)
    - [Department of Veterans Affairs](#department-of-veterans-affairs)
    - [August 2015](#august-2015)
    - [Revision History](#revision-history)
- [Introduction](#introduction)
  - [Purpose](#purpose)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [References and Resources](#references-and-resources)
  - [National Service Desk and Organizational Contacts](#national-service-desk-and-organizational-contacts)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
  - [System Menu](#system-menu)
  - [Navigation](#navigation)
  - [Changing User ID and Password](#changing-user-id-and-password)
  - [Exit System](#exit-system)
  - [Caveats and Exceptions](#caveats-and-exceptions)
- [Data Abstractor Views](#data-abstractor-views)
  - [My Tasks](#my-tasks)
  - [Finding/Opening an Encounter](#findingopening-an-encounter)
  - [Adding a New Encounter](#adding-a-new-encounter)
  - [Updating an Encounter](#updating-an-encounter)
    - [General Tab](#general-tab)
    - [Provider Tab](#provider-tab)
    - [Chief Complaint Tab](#chief-complaint-tab)
    - [History Tab](#history-tab)
    - [Exam Tab](#exam-tab)
    - [Diagnosis Tab](#diagnosis-tab)
    - [Procedures Tab](#procedures-tab)
  - [Submitting an Encounter for Review](#submitting-an-encounter-for-review)
  - [Updating an Encounter after Review](#updating-an-encounter-after-review)
- [Medical Professional (Quality Reviewer) Views](#medical-professional-quality-reviewer-views)
  - [My Tasks](#my-tasks-1)
  - [Adding Review Comments](#adding-review-comments)
  - [Approving Changes after Review](#approving-changes-after-review)
  - [Submitting Encounters to DVEIVR](#submitting-encounters-to-dveivr)
  - [Additional Operations](#additional-operations)
    - [![](military-eye-vision-injury-version-1-user-guide/166.png)Finding/Opening an Encounter](#military-eye-vision-injury-version-1-user-guide166pngfindingopening-an-encounter)
    - [Adding a New Encounter](#adding-a-new-encounter-1)
- [Administrator Views](#administrator-views)
  - [My Tasks](#my-tasks-2)
    - [Workload Reassignment Tab](#workload-reassignment-tab)
    - [Change Encounter Status Tab](#change-encounter-status-tab)
  - [Assigning / Reassigning Tasks](#assigning-reassigning-tasks)
  - [Adding a New Encounter](#adding-a-new-encounter-2)
  - [Reporting](#reporting)
  - [Adding System Users](#adding-system-users)
- [Troubleshooting](#troubleshooting)
![](military-eye-vision-injury-version-1-user-guide/001.png)

### Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

### August 2015

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Software Version 2.0

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Date   | Revision | Description | Author                         |
|------------|--------------|-----------------|------------------------------------|
| 08/24/2015 | 1.0          | Initial Version | <span class="mark">REDACTED</span> |
| 08/27/2015 | 2.0          | Updated Version | <span class="mark">REDACTED</span> |
1.  [Introduction 5](#introduction)
    1.  [Purpose 5](#purpose)
        1.  [Assumptions 5](#assumptions)
        2.  [Coordination 6](#coordination)
        3.  [References and Resources 6](#references-and-resources)
    2.  [National Service Desk and Organizational Contacts 6](#national-service-desk-and-organizational-contacts)
2.  [System Summary 6](#system-summary)
    1.  [System Configuration 7](#system-configuration)
    2.  [Data Flows 8](#data-flows)
    3.  [User Access Levels 8](#user-access-levels)
    4.  [Continuity of Operation 9](#continuity-of-operation)
3.  [Getting Started 9](#getting-started)
    1.  [Logging On 9](#logging-on)
    2.  [System Menu 9](#system-menu)
    3.  [Navigation 10](#navigation)
    4.  [Changing User ID and Password 11](#changing-user-id-and-password)
    5.  [Exit System 11](#exit-system)
    6.  [Caveats and Exceptions 11](#caveats-and-exceptions)
4.  [Data Abstractor Views 11](#data-abstractor-views)
    1.  [My Tasks 11](#my-tasks)
    2.  [Finding/Opening an Encounter 12](#findingopening-an-encounter)
    3.  [Adding a New Encounter 13](#adding-a-new-encounter)
    4.  [Updating an Encounter 14](#updating-an-encounter)
        1.  [General Tab 14](#general-tab)
        2.  [Provider Tab 15](#provider-tab)
        3.  [Chief Complaint Tab 16](#chief-complaint-tab)
        4.  [History Tab 17](#history-tab)
        5.  [Exam Tab 18](#exam-tab)
            1.  [Adding, Editing and Deleting Events 18](#adding-editing-and-deleting-events)
        6.  [Diagnosis Tab 26](#diagnosis-tab)
        7.  [Procedures Tab 28](#procedures-tab)
    5.  [Submitting an Encounter for Review 30](#submitting-an-encounter-for-review)
    6.  [Updating an Encounter after Review 30](#updating-an-encounter-after-review)
5.  [Medical Professional (Quality Reviewer) Views 32](#medical-professional-quality-reviewer-views)
    1.  [My Tasks 32](#my-tasks-1)
    2.  [Adding Review Comments 32](#adding-review-comments)
    3.  [Approving Changes after Review 33](#approving-changes-after-review)
    4.  [Submitting Encounters to DVEIVR 34](#submitting-encounters-to-dveivr)
    5.  [Additional Operations 34](#additional-operations)
        1.  [Finding/Opening an Encounter 34](#findingopening-an-encounter-1)
        2.  [Adding a New Encounter 35](#adding-a-new-encounter-1)
6.  [Administrator Views 37](#administrator-views)
    1.  [My Tasks 37](#my-tasks-2)
        1.  [Workload Reassignment Tab 37](#workload-reassignment-tab)
        2.  [Change Encounter Status Tab 38](#change-encounter-status-tab)
    2.  [Assigning / Reassigning Tasks 38](#assigning-reassigning-tasks)
    3.  [Adding a New Encounter 39](#adding-a-new-encounter-2)
    4.  [Reporting 41](#reporting)
    5.  [Adding System Users 43](#adding-system-users)
7.  [Troubleshooting 44](#troubleshooting)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Department of Veterans Affairs (VA) established the VA Eye Injury Data Store (VA EIDS) (formerly called the Military Eye Injury Registry, or MEVIR) in 2012 to transfer Veteran eye injury data into the Defense and Veterans Eye Injury and Vision Registry (DVEIVR). DVEIVR was developed by the Department of Defense (DoD) as the first ocular registry designed to be shared by the VA and DoD.

> The VA EIDS is currently the primary data source of ocular and related data for Veterans of Operation Enduring Freedom, Operation Iraqi Freedom and Operation New Dawn (OEF/OIF/OND) being treated in VA medical and rehabilitation facilities. The VA EIDS collects and analyzes information from the Corporate Data Warehouse (CDW), including clinical data regarding ocular and related diagnoses, medical and surgical interventions, other treatments, rehabilitation, and restoration outcomes.

> The VA EIDS enhancements effort provides improvements to better support the harmonization of data between VA and DoD and to enhance data entry by data abstractors. The system improvements ensure that the same data format is used by DoD and VA. The improvements also support eligibility determinations in relevant encounters, add new data fields (e.g., low vision and blind rehabilitation care), automate data transmission on a regular schedule, add the ability to filter records and create reports, and support accuracy in system reporting. The enhancements will also allow the DoD/VA Vision Center of Excellence (VCE) to develop initiatives to improve visual readiness, enhance treatments and outcomes, guide research, establish guidelines for care, and inform policy.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this user guide is to familiarize users with the features and navigational elements of the enhanced VA EIDS application.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The enhanced VA EIDS allows access by authenticated users on the Compensation and Pension Record Interchange (CAPRI) system, consisting of data abstractors, medical professionals (aka quality reviewers), subject matter experts (SMEs) and database administrators (DBAs). The intended users are assumed to have an educational level sufficient for daily duties and activities, with moderate to low technical expertise. The design of the enhancements will be user friendly per business owner input while still conforming to the Converged Registries Solution (CRS) framework and Veterans Health Administration (VHA) Office of Information & Technology (OI&T) standards, and will not warrant any additional technical acumen.

> The intended users of the enhanced VA EIDS are described in the table below.

> Table 1: User Access Levels

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Intended User(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>System Proficiency</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Background</strong></p>
<p><strong>/ Experience</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Technical Support / Maint Expertise</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Access Privileges</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Data Abstractors</td>
<td>Varies</td>
<td>High</td>
<td>Low</td>
<td>Varies</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Intended User(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>System Proficiency</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Background</strong></p>
<p><strong>/ Experience</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Technical Support / Maint Expertise</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Access Privileges</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Medical Professionals (Quality Reviewers)</td>
<td>Varies</td>
<td>High</td>
<td>Low</td>
<td>Varies</td>
</tr>
<tr class="even">
<td>Subject Matter Experts</td>
<td>Varies</td>
<td>High</td>
<td>Low</td>
<td>Varies</td>
</tr>
<tr class="odd">
<td>Database Administrators</td>
<td>High</td>
<td>High</td>
<td>High</td>
<td>Full</td>
</tr>
</tbody>
</table>

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The organizations that require coordination for VA EIDS include the Registries Sustainment team and the Austin Information Technology Center (AITC).

> Security measures are upheld by AITC. The schedule of coordination activities is the timeframe of the VA EIDS enhancements warranty and VA EIDS sustainment activities.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The formal documentation for the enhanced VA EIDS is located in the Technical Service Project Repository (TSPR) project notebook:

<span class="mark">REDACTED</span>

## National Service Desk and Organizational Contacts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Help desk services are provided by the National Service Desk (NSD).

> Calls to the NSD should state that the user is working with the Converged Registries Solution and the VA Eye Injury Data Store. The NSD will then direct the trouble ticket to AITC, who will use established procedures to direct the problem to the CRS sustainment team.

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The user interface for the enhanced VA EIDS is a standard Web interface that provides optimized data abstraction and reporting tools with a variety of filtering and sorting capabilities, including the following features:

- VA EIDS My Tasks Dashboard
- VA EIDS Referrals
- VA EIDS Reporting Tools
- VA EIDS Administration

> These features are described in detail in this User Guide.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The enhanced VA EIDS Registry, residing on the CRS platform, consists of three system environments: Development (Dev), Pre-Production (Pre-Prod, including Staging and SQA) and Production (Prod). These environments are located at AITC, whose system administrators and IT specialists, service, administer, and maintain the hardware and software.

> The figure below describes the VA Wide Area Network (WAN) Infrastructure.

> ![](military-eye-vision-injury-version-1-user-guide/002.png)![](military-eye-vision-injury-version-1-user-guide/003.png)![](military-eye-vision-injury-version-1-user-guide/004.png)![](military-eye-vision-injury-version-1-user-guide/005.png)![](military-eye-vision-injury-version-1-user-guide/006.png)![](military-eye-vision-injury-version-1-user-guide/007.png)![](military-eye-vision-injury-version-1-user-guide/008.png)![](military-eye-vision-injury-version-1-user-guide/009.png)![](military-eye-vision-injury-version-1-user-guide/010.png)![](military-eye-vision-injury-version-1-user-guide/011.png)![](military-eye-vision-injury-version-1-user-guide/012.png)![](military-eye-vision-injury-version-1-user-guide/013.png)![](military-eye-vision-injury-version-1-user-guide/014.png)![](military-eye-vision-injury-version-1-user-guide/015.png)![](military-eye-vision-injury-version-1-user-guide/016.png)![](military-eye-vision-injury-version-1-user-guide/017.png)![](military-eye-vision-injury-version-1-user-guide/018.png)![](military-eye-vision-injury-version-1-user-guide/019.png)![](military-eye-vision-injury-version-1-user-guide/020.png)![](military-eye-vision-injury-version-1-user-guide/021.png)![](military-eye-vision-injury-version-1-user-guide/022.png)![](military-eye-vision-injury-version-1-user-guide/023.png)![](military-eye-vision-injury-version-1-user-guide/024.png)![](military-eye-vision-injury-version-1-user-guide/025.png)![](military-eye-vision-injury-version-1-user-guide/026.png)![](military-eye-vision-injury-version-1-user-guide/027.png)![](military-eye-vision-injury-version-1-user-guide/028.png)![](military-eye-vision-injury-version-1-user-guide/029.png)![](military-eye-vision-injury-version-1-user-guide/030.png)![](military-eye-vision-injury-version-1-user-guide/031.png)![](military-eye-vision-injury-version-1-user-guide/032.png)![](military-eye-vision-injury-version-1-user-guide/033.png)![](military-eye-vision-injury-version-1-user-guide/034.png)![](military-eye-vision-injury-version-1-user-guide/035.png)![](military-eye-vision-injury-version-1-user-guide/036.png)![](military-eye-vision-injury-version-1-user-guide/037.png)![](military-eye-vision-injury-version-1-user-guide/038.png)![](military-eye-vision-injury-version-1-user-guide/039.png)![](military-eye-vision-injury-version-1-user-guide/040.png)![](military-eye-vision-injury-version-1-user-guide/041.png)![](military-eye-vision-injury-version-1-user-guide/042.png)![](military-eye-vision-injury-version-1-user-guide/043.png)![](military-eye-vision-injury-version-1-user-guide/044.png)![](military-eye-vision-injury-version-1-user-guide/045.png)![](military-eye-vision-injury-version-1-user-guide/046.png)![](military-eye-vision-injury-version-1-user-guide/047.png)![](military-eye-vision-injury-version-1-user-guide/048.png)![](military-eye-vision-injury-version-1-user-guide/049.png)![](military-eye-vision-injury-version-1-user-guide/050.png)![](military-eye-vision-injury-version-1-user-guide/051.png)![](military-eye-vision-injury-version-1-user-guide/052.png)![](military-eye-vision-injury-version-1-user-guide/053.png)![](military-eye-vision-injury-version-1-user-guide/054.png)![](military-eye-vision-injury-version-1-user-guide/055.png)![](military-eye-vision-injury-version-1-user-guide/056.png)![](military-eye-vision-injury-version-1-user-guide/057.png)![](military-eye-vision-injury-version-1-user-guide/058.png)![](military-eye-vision-injury-version-1-user-guide/059.png)![](military-eye-vision-injury-version-1-user-guide/060.png)![](military-eye-vision-injury-version-1-user-guide/061.png)![](military-eye-vision-injury-version-1-user-guide/062.png)![](military-eye-vision-injury-version-1-user-guide/063.png)![](military-eye-vision-injury-version-1-user-guide/064.png)![](military-eye-vision-injury-version-1-user-guide/065.png)CDW LAN

> Registry Servers

> Business process support, Reporting for Center-of-Excellence staff

> CDW Servers NDS SSIS processes

> Consolidation and national roll-up

> CDW Extractor: Region 1 nightly, Others at max. monthly

> ![](military-eye-vision-injury-version-1-user-guide/066.png)![](military-eye-vision-injury-version-1-user-guide/067.png)![](military-eye-vision-injury-version-1-user-guide/068.png)![](military-eye-vision-injury-version-1-user-guide/069.png)![](military-eye-vision-injury-version-1-user-guide/070.png) ![](military-eye-vision-injury-version-1-user-guide/071.png)![](military-eye-vision-injury-version-1-user-guide/072.png)![](military-eye-vision-injury-version-1-user-guide/073.png)![](military-eye-vision-injury-version-1-user-guide/074.png)![](military-eye-vision-injury-version-1-user-guide/075.png)![](military-eye-vision-injury-version-1-user-guide/076.png)![](military-eye-vision-injury-version-1-user-guide/077.png)

> ![](military-eye-vision-injury-version-1-user-guide/078.png)![](military-eye-vision-injury-version-1-user-guide/079.png)![](military-eye-vision-injury-version-1-user-guide/080.png)![](military-eye-vision-injury-version-1-user-guide/081.png)NDS Workstations

> After HDR / MPI data received at CDW, use SSIS to consolidate with SAS data, and extract Patient, Provider, InPatient, OutPatient

> VA WAN

> VistA

> Back-end database architecture to support CPRS application at individual VA Medical centers

> Figure 1: WAN Infrastructure

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The figure below shows the VA EIDS business process and data flow.

![](military-eye-vision-injury-version-1-user-guide/082.png)

> Figure 2: VA EIDS Business Process & Data Flow

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The enhanced VA EIDS allows access by authenticated users on the Compensation and Pension Record Interchange (CAPRI) system, consisting of data abstractors, medical professionals (aka quality reviewers), subject matter experts (SMEs) and database administrators (DBAs). The intended users are assumed to have an educational level sufficient for daily duties and activities, with moderate to low technical expertise. The design of the enhancements will be user friendly per business owner input while still conforming to the Converged Registries Solution (CRS) framework and Veterans Health Administration (VHA) Office of Information & Technology (OI&T) standards, and will not warrant any additional technical acumen.

> The intended users of the enhanced VA EIDS are described in the table below.

> Table 2: User Access Levels

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Intended User(s)</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>System Proficiency</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Background</strong></p>
<p><strong>/ Experience</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Technical Support / Maint Expertise</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Access Privileges</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Data Abstractors</td>
<td>Varies</td>
<td>High</td>
<td>Low</td>
<td>Varies</td>
</tr>
<tr class="even">
<td>Medical Professionals (Quality Reviewers)</td>
<td>Varies</td>
<td>High</td>
<td>Low</td>
<td>Varies</td>
</tr>
<tr class="odd">
<td>Subject Matter Experts</td>
<td>Varies</td>
<td>High</td>
<td>Low</td>
<td>Varies</td>
</tr>
<tr class="even">
<td>Database Administrator</td>
<td>High</td>
<td>High</td>
<td>High</td>
<td>Full</td>
</tr>
</tbody>
</table>

> CRS further provides for the following three layers of access:

- Enterprise Access: To be granted to users requiring reports and information on an enterprise level. Enterprise access will also include access to the VISN local levels.
- VISN Access: To be granted to users requiring reports and information on a VISN- specific level. The access will be restricted to reports and information from that user’s assigned VISN. VISN level access will also include local level functionality for sites within the VISN.
- Local Level: To be granted to users requiring reports and information on a local level. Users with local access will be restricted to reports and information for their assigned location. Local users will not have access to VISN or enterprise reports or information. Local level is the most restrictive level of access.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Continuity of operations in the event of an emergency, disaster, or accident is handled by AITC procedures.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA EIDS is a Web-based intranet registry that allows access to authenticated users on the CRS architectural platform. No separate login procedure is required once the user has been given access to the VA EIDS intranet site application.

> VA EIDS requires Internet Explorer (IE) versions 6.0 or higher.

## System Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](military-eye-vision-injury-version-1-user-guide/083.png)The main system menu is found at the top of the VA EIDS landing page (My Tasks).

## Navigation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As a Web-based application, VA EIDS provides easy browser-based navigation between tabs and pages.

- To navigate directly to a top-level page from any other location, click the corresponding menu link at the top of the page.

![](military-eye-vision-injury-version-1-user-guide/084.png)

> ![](military-eye-vision-injury-version-1-user-guide/085.png)Navigation is also aided by the breadcrumb trail at the top of each view. Click the desired link to navigate to that level.

> Clicking the browser Back and Next buttons will navigate back and forth between the previous and next page.

> ![](military-eye-vision-injury-version-1-user-guide/086.png)VA EIDS also provides easy grid navigation using the mouse or keyboard.

- Press Ctrl+Y to select the grid, and press the Tab or arrow keys to navigate between items.
- Click the Previous ![](military-eye-vision-injury-version-1-user-guide/087.png) and Next ![](military-eye-vision-injury-version-1-user-guide/088.png) buttons to go back and forth between pages sequentially, or click the desired page number to open it.
- Click the First ![](military-eye-vision-injury-version-1-user-guide/089.png) and Last ![](military-eye-vision-injury-version-1-user-guide/090.png) buttons to jump to the first or last page.
- To set the number of rows to display on one page, make the selection from the Page Size

> ![](military-eye-vision-injury-version-1-user-guide/091.png)list:

- A grid can be sorted by column in ascending or descending order by clicking the column.

## Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As a Web-based VA intranet registry application, users log in with their VA network credentials. User IDs and passwords are not administered by VA EIDS, and thus no specific procedures for changing the User IDs and passwords are required.

## Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- To exit the system, simply close the browser window.

## Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

# Data Abstractor Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA EIDS users with the role of Data Abstractor have the ability to search for and update assigned encounters, create new encounters, and submit encounters for review. These operations are outlined in this section.

## My Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The My Tasks page is the landing page for VA EIDS. This page allows the data abstractor to view currently assigned tasks and to filter them by status.

> Data Abstractor Tasks: This grid shows the current list of encounters assigned to the data abstractor.

![](military-eye-vision-injury-version-1-user-guide/092.png)

> To filter the list of encounters: Select the desired status from the Encounter Status list (default setting = All). The status fields are as follows:

- ![](military-eye-vision-injury-version-1-user-guide/093.png)New: A newly assigned, unprocessed record.
- In Progress: A record that is currently being processed and is not yet ready for review.
- Ready for Review: A record that has been submitted for review and is now read only. This signifies that the record has been moved to the quality reviewer’s queue and cannot be edited by the data abstractor.
- Returned: A record that has been returned by the quality

> reviewer with comments. The data abstractor will then go back into the record, address the comments, and re-submit for review.

- Ready to Send: A read-only record that has been reviewed and approved, and put into the queue for transmission to DVEIVR.
- Completed: A read-only record that has been transferred to DVEIVR.

## Finding/Opening an Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To open and update an encounter that has already been assigned, click the corresponding Select

> link in the Data Abstractor Tasks grid.

> -Or-

> ![](military-eye-vision-injury-version-1-user-guide/094.png)If the encounter hasn’t been assigned yet, search for it as follows:

1.  Click Referrals in the main menu.
2.  Apply the corresponding filters:
    - VISN: Select the VISN from the drop-down list.
    - Facility: Select the Facility from the drop-down list.
    - Patient Name or SSN: Type all or part of the name of the patient or their Social Security number.
    - Status: Select the status from the drop-down list.
3.  ![](military-eye-vision-injury-version-1-user-guide/095.png)Click Search. The grid will display the list of matching patients.
4.  Click the corresponding Select link to open the Encounters for Referral page for that patient. This view displays two tabs: Encounters and Problem List.
    - The Encounters grid displays the list of all encounters recorded for the patient, while the Problem List is a read-only list of health issues recorded for the patient.
    - If the encounter is a new, unassigned record, the Assigned To field will be blank.
5.  Click the corresponding Select link to open the encounter.

> ![](military-eye-vision-injury-version-1-user-guide/096.png)

> NOTE: Once an encounter is saved, it becomes assigned to the data abstractor who saved it, and the encounter will be added to the list of tasks on the My Tasks page.

## Adding a New Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](military-eye-vision-injury-version-1-user-guide/097.png)The Encounters for Referral page described on the previous page also allows users to add a new encounter for the current patient.

#### To add an encounter

1.  Click Add Encounter on the Filters/Actions menu.
2.  Complete the following fields:
    - Referral ID: This ID is used by the VA EIDS application and is automatically assigned.
    - Institution (required): Select the VISN and Facility from the drop-down list.
    - Visit Date (required): Enter the date of the encounter, in M/D/YYYY format, followed by the time (standard or military). The date can be spelled out, but it will revert to numerical format. Military time will revert to standard.

> -Or-

> ![](military-eye-vision-injury-version-1-user-guide/098.png)Use the Date and Time ![](military-eye-vision-injury-version-1-user-guide/099.png) pickers to select the date and time.

- Encounter Type (required): Select the visit type, Outpatient or Inpatient.

![](military-eye-vision-injury-version-1-user-guide/100.png)

3.  Click Save to save the changes, or Cancel to exit without saving.

## Updating an Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Upon opening an encounter, the record will display seven (7) tabbed pages, while the Encounter Actions menu allows the data abstractor to Save or Cancel any changes made to the record. The menu also allows the data abstractor to submit an updated record for review.

> Note: Updates must be saved by clicking the Save button on the Encounter Actions menu before navigating to a new tab.

![](military-eye-vision-injury-version-1-user-guide/101.png)

### General Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](military-eye-vision-injury-version-1-user-guide/102.png)The General tab provides general information about the date of the encounter, as well as the facility, outpatient/inpatient status, and the original referral date.

#### To edit General information

1.  Set the following fields:
    - Date: Enter the date of the encounter, in M/D/YYYY format, followed by the time (standard or military). The date can be spelled out, but it will revert to numerical format. Military time will revert to standard.

> -Or-

> ![](military-eye-vision-injury-version-1-user-guide/103.png)Use the Date and Time ![](military-eye-vision-injury-version-1-user-guide/104.png) pickers to select the date and time.

- Facility: Select the facility from the drop-down list.
- Encounter Type (required): Select the visit type, Outpatient (default setting) or Inpatient from the drop-down list.
2.  Click Save to save the changes.

### Provider Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](military-eye-vision-injury-version-1-user-guide/105.png)The Provider tab allows the data abstractor to add or remove providers, and to designate a provider as the Primary.

#### To add a Provider

3.  Click Add Provider. This will open the Provider Information page.

![](military-eye-vision-injury-version-1-user-guide/106.png)

4.  Set the following fields:
    - Facility: Select the facility from the drop-down list.
    - Provider: Select the provider from the drop-down list, or type all or part of the provider’s name in the text box to bring up matches.
    - Is Primary Provider: Select the check box to designate this provider as the primary provider. The check box will not be selectable if another provider has already been designated as the primary.
5.  Click Add Provider to save the provider information, or click Cancel to return to the Provider Information page with no changes.

#### To remove a provider

- Click the corresponding Delete link, and then click OK to confirm, or Cancel to cancel out.

#### To designate a provider as the primary provider

- Click the corresponding Make Primary link.

### Chief Complaint Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Chief Complaint tab allows the data abstractor to enter information about the patient’s chief complaint, or main reason for making the visit.

![](military-eye-vision-injury-version-1-user-guide/107.png)

#### To enter information:

1.  Complete the following fields, where applicable:
    - Chief Complaint: Enter the patient’s main reason for the visit in the free text field.
    - Current Symptoms: Select all check boxes that correspond to the patient’s current symptoms.
    - Comments: Type additional comments related to the encounter in the free text field.
2.  Click Save to save the information, or Cancel to cancel out.

### History Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](military-eye-vision-injury-version-1-user-guide/108.png)The History tab allows the data abstractor to record information about the patient’s medical history and/or injuries.

#### To enter patient history

3.  Select from the following drop-down lists, where applicable:
    - History: Select the corresponding condition and click Add.
    - Injury: Select the corresponding injury and click Add.

![](military-eye-vision-injury-version-1-user-guide/109.png)![](military-eye-vision-injury-version-1-user-guide/110.png)

4.  To remove an item, click the corresponding Delete link.

### Exam Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](military-eye-vision-injury-version-1-user-guide/111.png)The Exam tab allows the data abstractor to add, edit, or delete medical events and procedures associated with the patient visit.

#### Adding, Editing and Deleting Events

> To add a new event

1.  Select the event from the Event Type list.

![](military-eye-vision-injury-version-1-user-guide/112.png)

2.  Enter the corresponding information for the event. The available fields differ depending on the event, as shown in Table 3.
3.  Click Save to save the event details.

#### To edit an event

1.  Click the corresponding Edit link.
2.  Make the necessary revisions by selecting from the drop-down fields. The available fields differ depending on the event, as shown in Table 3.
3.  Click Update to apply the edits, or Cancel to exit without saving.

#### To delete an event

- Click the corresponding Delete link, and then click Yes when prompted to confirm.

> Table 3: Exam Tab Events and Fields

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Event</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Angle Recession Anterior Chamber Brow</p>
<p>Confrontation Visual Fields Conjunctiva</p>
<p>Cornea</p>
<p>Depth Perception Functional Testing Field Globe</p></td>
<td><p><strong>Laterality</strong>: Select the affected eye, i.e., left, right, both, or not specified.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/113.png)</p>
</blockquote>
<p><strong>Was the Test Performed</strong>? Select Yes, No, or Not Documented.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Event</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Intraocular Pressure Iris</p>
<p>Kinetic Visual Fields Lens</p>
<p>Lids</p>
<p>Motility Extraocular Muscles Optic Disc</p>
<p>Orbit Pupil</p>
<p>Relative Afferent Pupil Defect Retina</p>
<p>Scelera</p>
<p>Static Threshold Perimetry Visual Acuity</p>
<p>Vitreous</p></td>
<td><blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/114.png)</p>
</blockquote>
<p>Selecting “Yes” will display the Test Result and Visit Data fields:</p>
<p><strong>Test Result</strong>: Select the result, i.e., Normal or Abnormal.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/115.png)</p>
</blockquote>
<p><strong>Visit Data</strong>: Select the corresponding test data from the drop-down list and click <strong>Add</strong>.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/116.png)</p>
</blockquote>
<p><strong>Comments</strong>: Type additional clinical comments in the free text field.</p>
<p>Some events provide additional data fields, as outlined further in this table.</p></td>
</tr>
<tr class="even">
<td>Angle Recession</td>
<td><p><strong>Visit Data</strong> <em>(visible when the “Was the Test Performed?” field is set to Yes)</em></p>
<p>Select the event detail from the drop-down list.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/117.png)</p>
</blockquote>
<p><strong>Clock Hours</strong>: Select the number of clock hours (1 – 12) of angle recession from the two drop-down lists.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/118.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Event</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Color Vision</td>
<td><p><strong>What Test was Performed / Additional Details</strong>: Select the corresponding test and type any additional details in the free text field.</p>
<p><strong>Number Correct / Total Number</strong>: Type the corresponding numbers in the text fields.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/119.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Depth Perception</td>
<td><p><strong>Depth Perception</strong> <em>(visible when the “Was the Test Performed?” field is set to Yes)</em></p>
<p><strong>Randot Fly / Verboeff Stereopter</strong>: Type information related to the corresponding test types in the free text fields.</p>
<p><strong>Angle of Stereopsis</strong>: Select the test results, in seconds of arc, from the corresponding drop-down lists.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/120.png)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Functional Testing Field</td>
<td><p><strong>Functional Testing Field</strong> <em>(visible when the “Was the Test Performed?” field is set to Yes)</em></p>
<p>Enter the Functional Testing field results in the indicated formats.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Event</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/121.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Imaging Ancillary Testing</td>
<td><p><strong>Imaging Ancillary Testing</strong></p>
<p><strong>Imaging Methodology</strong>: Select the imaging methodology from the drop down list.</p>
<p><strong>Test Date</strong>: Enter the test date in M/D/YYYY format. The date can be spelled out, but it will revert to numerical format.</p>
<p>-Or-</p>
<p>Use the <strong>Date</strong> selector to select the test date.</p>
<p><strong>Test Result</strong>: Type the information about the test result in the free text field.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/122.png)</p>
</blockquote>
<p>Click the <strong>Add</strong> link to add the record to the image testing list.</p></td>
</tr>
<tr class="odd">
<td>Intraocular Pressure</td>
<td><p><strong>Intraocular Pressure</strong> <em>(visible when the “Was the Test Performed?” field is set to Yes)</em></p>
<p>Type the corresponding information into the free text fields, i.e., Method, Comments, Number (0-99).</p>
<p>Type the time into the text field (standard time will be converted to military), or use the clock to select the time.</p></td>
</tr>
</tbody>
</table>

![](military-eye-vision-injury-version-1-user-guide/123.png)![](military-eye-vision-injury-version-1-user-guide/124.png)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Event</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/125.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Kinetic Visual Fields</td>
<td><p><strong>Kinetic Visual Fields</strong></p>
<p><strong>Methodology</strong>: Select the field kinetic testing methodology from the drop down list.</p>
<p><strong>Result</strong>: Type the information about the test result in the free text field.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/126.png)</p>
</blockquote>
<p>Click the <strong>Add</strong> link to add the record to the test method list.</p></td>
</tr>
<tr class="odd">
<td>Motility Extraocular Muscles</td>
<td><p><strong>Motility Extraocular Detail</strong> <em>(visible when the “Was the Test Performed?” field is set to Yes)</em></p>
<p>Select the corresponding eye movement details from the drop-down lists. If “Abnormal” is selected for Saccades, this enables a free text area for additional comments.</p>
<p>To add additional records, select the corresponding condition from the Motility and Cranial Nerve lists and click <strong>Add t</strong>o add the record to the list.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/127.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Prosthetic Devices Ordered</td>
<td><p><strong>Prosthetic Devices Ordered</strong></p>
<p><strong>Laterality</strong>: Select the affected eye from the drop-down list.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Event</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/128.png)</p>
</blockquote>
<p><strong>Options</strong>: Select the type of prosthesis from the drop-down list and click Add to add it to the list of devices.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/129.png)</p>
</blockquote>
<p><strong>Implant Types</strong>: Select the implant type from the drop-down list and click <strong>Add</strong> to add it to the list of implants.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/130.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Pupil</td>
<td><p><strong>Pupil</strong> <em>(visible when the “Was the Test Performed?” field is set to Yes)</em></p>
<p><strong>Size</strong>: Type the pupil size (1-10) in the text field.</p>
<p><strong>Alterations in Shape</strong>: Type additional information into this free text field.</p>
<p><strong>PERRL or PERRLA / Reactive</strong>: Select the corresponding assessment and reactive setting.</p>
<p><strong>Adie’s / Argyll-Robertson</strong>: Click <strong>Yes</strong> or <strong>No</strong> for the presence of Adie’s syndrome or Argyll-Robertson pupil.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Event</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/131.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Relative Afferent Pupil Defect</td>
<td><p><em>(Visible when the “Was the Test Performed?” field is set to Yes)</em></p>
<p><strong>Relative Afferent Pupil Defect</strong>: Select Yes or No for the presence of the condition.</p>
<p><strong>ADP</strong>: Select the ADP status, i.e., Negative or Positive.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/132.png)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Static Threshold Perimetry</td>
<td><p><strong>Static Threshold Perimetry</strong> <em>(visible when the “Was the Test Performed?” field is set to Yes)</em></p>
<p><strong>Reference Scale</strong>: Select the reference scale from the list.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/133.png)</p>
</blockquote>
<p><strong>Deviation / Fixation Losses</strong>: Type the mean and pattern standard deviations, as well as the fixation losses in the indicated format.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/134.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Symptoms</td>
<td><p><strong>Visit Data</strong>: Select the symptom data and click <strong>Add</strong> to add it to the list.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/135.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Event</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Fields</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Visual Acuity</td>
<td><p><strong>Visual Acuity</strong> <em>(visible when the “Was the Test Performed?” field is set to Yes)</em></p>
<p><strong>Scale</strong>: Select the standard of measurement from the drop-down list.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/136.png)</p>
</blockquote>
<p>Enter the corresponding information for the selected scale. The exact selections differ depending on which scale is chosen, but all scales show areas for Scale, Refraction and Qualifiers. The example below shows selections for the Jaeger scale.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/137.png)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Visual Functioning Questionnaire</td>
<td><p><strong>Questionnaire / Score</strong>: Select the visual functioning questionnaire and enter the corresponding score.</p>
<blockquote>
<p>![](military-eye-vision-injury-version-1-user-guide/138.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Diagnosis Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Diagnosis tab allows the data abstractor to add, edit, and delete information about the patient diagnosis, and to indicate whether the patient is in vision rehabilitation.

![](military-eye-vision-injury-version-1-user-guide/139.png)

#### To set the status of vision rehabilitation

- Click the Yes, No or Unknown button.

![](military-eye-vision-injury-version-1-user-guide/140.png)

#### To add a diagnosis

1.  Click Add Diagnosis.
2.  Use the following fields:
    - Laterality: Select the laterality, i.e., Left Eye, Right Eye, Both or Not Specified.

![](military-eye-vision-injury-version-1-user-guide/141.png)

- ICD Code / Description: Type the ICD-9 or ICD-10 code in the text field.

![](military-eye-vision-injury-version-1-user-guide/142.png)

3.  Click Add Diagnosis to add the diagnosis to the list, or Cancel to exit without retaining the settings.
4.  Click Save on the Encounter Actions menu to save, or Cancel to exit without saving.

#### To edit a diagnosis

1.  Click the corresponding Edit button
2.  Edit the fields as described above.
3.  Click Update to apply the revisions, or Cancel to exit without retaining the settings.
4.  Click Save on the Encounter Actions menu to save, or Cancel to exit without saving.

#### To remove a diagnosis

- Click the corresponding Delete link, and then click OK when prompted to confirm.

### Procedures Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Procedures tab allows the data abstractor to add, edit, and delete information about any procedures that were performed.

![](military-eye-vision-injury-version-1-user-guide/143.png)

#### To add a procedure

1.  Click Add Procedure.
2.  Use the following fields:
    - Laterality: Select the laterality, i.e., Left Eye, Right Eye, Both or Not Specified.

![](military-eye-vision-injury-version-1-user-guide/144.png)

- CPT Code: Type the CPT code in the free text field.
- Short / Long Description: Type the Name and Description in the free text fields.

![](military-eye-vision-injury-version-1-user-guide/145.png)

3.  Click Add Procedure to add the procedure to the list, or Cancel to exit without retaining the settings.
4.  Click Save on the Encounter Actions menu to save, or Cancel to exit without saving.

#### To edit a procedure

5.  Click the corresponding Edit button
6.  Edit the fields as described above.
7.  Click Update to apply the revisions, or Cancel to exit without retaining the settings.
8.  Click Save on the Encounter Actions menu to save, or Cancel to exit without saving.

#### To remove a procedure

- Click the corresponding Delete link, and then click OK when prompted to confirm.

## Submitting an Encounter for Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once all the relevant encounter information has been entered into the record, the encounter is ready for review.

#### To submit an encounter for review

- Click the Send for Review link on the Encounter Actions menu.

> The Encounter Status will now be marked as Ready for Review in the My Tasks grid. The encounter cannot be edited when marked as Ready for Review.

## Updating an Encounter after Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the quality reviewer returns an encounter to the data abstractor for revision, the Encounter Status will be marked as Returned in the My Tasks grid.

#### To update an encounter after review

1.  Click the corresponding Select link.
2.  Go to the General tab to view the Review Comments grid. This grid will list all the comments that were added by the quality reviewer, including the tab where the comment can be located.

![](military-eye-vision-injury-version-1-user-guide/146.png)

3.  Click the corresponding Select link to go directly to the location where the review comment was added. The comment will be visible at the top of the page.

![](military-eye-vision-injury-version-1-user-guide/147.png)

- To expand the comment if it is not visible, click the Expand ![](military-eye-vision-injury-version-1-user-guide/148.png)button.
- To close the comment, click the Close ![](military-eye-vision-injury-version-1-user-guide/149.png) button.
- To save the comment, click the Save ![](military-eye-vision-injury-version-1-user-guide/150.png) button.
- NOTE: Any changes made to the Review Comments area will not be saved unless the Save ![](military-eye-vision-injury-version-1-user-guide/151.png) button is clicked. That is, clicking the Save button on the Encounter Actions menu will not save these changes.
4.  Make the necessary revisions to the encounter based on the review comment.
5.  Once the comment has been addressed, click (select) the Resolved check box and click the Save ![](military-eye-vision-injury-version-1-user-guide/152.png) button to save the changes.
6.  When all comments have been addressed and the encounter is ready to be re-submitted, click the Send for Review link on the Encounter Actions menu.
7.  The quality reviewer will review the encounter, locating each comment and marking off the Approved check box for each revision that is approved.

> The status of all comments will be visible in the Is Resolved and Is Approved columns of the Review Comments grid.

# Medical Professional (Quality Reviewer) Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users with the role of Medical Professional have all the same permissions and abilities as users in the Data Abstractor role. That is, they can search for and create new encounters, edit encounters, and perform all the functions outlined in Section 4.

> Users with the role of Medical Professional have the additional ability to review and approve encounters that have been submitted for review; add comments to encounters and return them to the data abstractor for further processing; and submit completed, approved encounters to DVEIVR. All of these operations are outlined in this section.

## My Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The My Tasks page is the landing page for VA EIDS. This page allows the medical professional/quality reviewer to view tasks.

> Reviewer Tasks: This grid shows the current list of encounters that are ready for review. These encounters have an Encounter Status of “Ready for Review” and can be reviewed by any quality reviewer.

![](military-eye-vision-injury-version-1-user-guide/153.png)

## Adding Review Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Review comments can be added in the following tabs: Chief Complaint, History, Exam, and Diagnosis.

> If a review comment can be added, three comment buttons will be visible over the corresponding field.

![](military-eye-vision-injury-version-1-user-guide/154.png)

- To open the review comment box, click the Expand ![](military-eye-vision-injury-version-1-user-guide/155.png)button.
- To close the review comment box, click the Close ![](military-eye-vision-injury-version-1-user-guide/156.png) button.
- To save a review comment, click the Save ![](military-eye-vision-injury-version-1-user-guide/157.png) button.
- NOTE: The review comment will not be saved unless the Save ![](military-eye-vision-injury-version-1-user-guide/158.png) button is clicked. That is, clicking the Save button on the Encounter Actions menu will not save the review comment.

#### To add comments

1.  Click the corresponding Select link for the encounter in the Reviewer Tasks grid.
    - The selected encounter can now be reviewed and edited by navigating through the tabs as described in Section 4.
2.  Go to the area where the comment will be added and click the Expand ![](military-eye-vision-injury-version-1-user-guide/159.png) button to open the review comments box.

![](military-eye-vision-injury-version-1-user-guide/160.png)

3.  Type the comment in the free text field and click the Save ![](military-eye-vision-injury-version-1-user-guide/161.png) button. (The comment will not be saved unless this button is clicked.)
4.  When all comments have been added, click the Return to Abstractor link in the Encounter Actions menu to return the record for further processing. This will remove the encounter from the Reviewer Tasks grid until the data abstractor re-submits the record for review.

## Approving Changes after Review

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the data abstractor has addressed the review comments, marked each comment as Resolved, and re-submitted the record for review, the encounter is now ready to be reviewed again.

#### To approve changes

1.  Click the corresponding Select link for the encounter in the Reviewer Tasks grid.
2.  Go to the General tab to view the list of review comments. The Is Resolved column will be checked (selected), signifying that the comment was resolved by the data abstractor.

![](military-eye-vision-injury-version-1-user-guide/162.png)

3.  Click the corresponding Select link to jump directly to the location where the comment was added/resolved.
5.  ![](military-eye-vision-injury-version-1-user-guide/163.png)If the review comment was addressed satisfactorily, click the Approved check box to select it, and then click the Save ![](military-eye-vision-injury-version-1-user-guide/164.png) button. (The setting will not be saved unless this button is clicked.)
6.  Repeat this procedure for all resolved comments.

> ![](military-eye-vision-injury-version-1-user-guide/165.png)After all comments have been approved, the Review Comments grid in the General Tab will show the Is Approved check boxes as selected.

## Submitting Encounters to DVEIVR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To submit an encounter to DVEIVR

1.  Click Save on the Encounter Actions menu to save the completed, approved encounter.
2.  Click the Send to DVEIVR link on the Encounter Actions menu. This will place the encounter in the queue for submission to DVEIVR the next time DVEIVR requests the data.

## Additional Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ![](military-eye-vision-injury-version-1-user-guide/166.png)Finding/Opening an Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click Referrals in the main menu.
2.  Apply the corresponding filters:
    - VISN: Select the VISN from the drop-down list.
    - Facility: Select the Facility from the drop-down list.
    - Patient Name or SSN: Type all or part of the name of the patient or their Social Security number.
    - Status: Select the status from the drop-down list.
3.  ![](military-eye-vision-injury-version-1-user-guide/167.png)Click Search. The grid will display the list of matching patients.
4.  Click the corresponding Select link to open the Encounters for Referral page for that patient. This view displays two tabs: Encounters and Problem List.
    - The Encounters grid displays the list of all encounters recorded for the patient, while the Problem List is a read-only list of health issues recorded for the patient.
5.  Click the corresponding Select link to open the encounter.

![](military-eye-vision-injury-version-1-user-guide/168.png)

### Adding a New Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](military-eye-vision-injury-version-1-user-guide/169.png)The Encounters for Referral page described on the previous page also allows users to add a new encounter for the current patient.

#### To add an encounter

4.  Click Add Encounter on the Filters/Actions menu.
5.  Complete the following fields:
    - Referral ID: This ID is used by the VA EIDS application and is automatically assigned.
    - Institution (required): Select the VISN and Facility from the drop-down list.
    - Visit Date (required): Enter the date of the encounter, in M/D/YYYY format, followed by the time (standard or military). The date can be spelled out, but it will revert to numerical format. Military time will revert to standard.

> -Or-

> ![](military-eye-vision-injury-version-1-user-guide/170.png)Use the Date and Time ![](military-eye-vision-injury-version-1-user-guide/171.png) pickers to select the date and time.

- Encounter Type (required): Select the visit type, Outpatient or Inpatient.

![](military-eye-vision-injury-version-1-user-guide/172.png)

6.  Click Save to save the changes, or Cancel to exit without saving.

# Administrator Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA EIDS users with the role of Administrator have the ability to add users to the system, assign and re-assign tasks, and generate reports.

## My Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The My Tasks page is the landing page for VA EIDS. The Administrator Tasks area shows two tabs: Workload Reassignment and Change Encounter Status.

![](military-eye-vision-injury-version-1-user-guide/173.png)

### Workload Reassignment Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Workload Reassignment tab allows Administrators to re-assign tasks.

#### To reassign tasks

1.  Select the data abstractor who is currently assigned to the task from the Data Abstractor list. This will display the Abstractor Workload grid, which list of all tasks assigned to that person.

![](military-eye-vision-injury-version-1-user-guide/174.png)

2.  Click the Reassign link corresponding to the encounter to be reassigned.
3.  Select the new data abstractor from the list and click Assign User. Click OK to confirm.

> The task will now be removed from the original data abstractor’s workload and added to the new data abstractor’s list of tasks on the My Tasks page.

> Another way to reassign tasks is described in Section 6.2.

### Change Encounter Status Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Change Encounter Status tab allows the Administrator to move an encounter to a specified status, i.e., from “Completed” to “Ready to Send” for resending a corrected record to DVEIVR.

#### To change encounter status

4.  Type the Encounter ID into the text field and click Search. This will bring up the corresponding record.
5.  Select the new encounter status from the list and click Update Encounter Status, or

> Cancel to exit without saving. Click OK to confirm.

![](military-eye-vision-injury-version-1-user-guide/175.png)

## Assigning / Reassigning Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA EIDS administrators have the ability to assign new tasks to data abstractors, and to re-assign tasks (in addition to the method described in Section 6.1.1).

#### To assign / reassign an encounter

> Find/search for the encounter as follows:

1.  Click Referrals in the main menu.
2.  Apply the corresponding filters:
    - VISN: Select the VISN from the drop-down list.
    - Facility: Select the Facility from the drop-down list.
    - Patient Name or SSN: Type all or part of the name of the patient or their Social Security number.
    - Status: Select the status from the drop-down list.
3.  ![](military-eye-vision-injury-version-1-user-guide/176.png)Click Search. The grid will display the list of matching patients.
4.  Click the corresponding Select link to open the Encounters for Referral page for that patient. This view displays two tabs: Encounters and Problem List.
    - The Encounters grid displays the list of all encounters recorded for the patient, while the Problem List is a read-only list of health issues recorded for the patient.
    - If the encounter is a new, unassigned record, the Assigned To field will display the Assign Encounter link.
5.  Click the Assign Encounter link.

![](military-eye-vision-injury-version-1-user-guide/177.png)

6.  Select the data abstractor from the User drop-down list.

![](military-eye-vision-injury-version-1-user-guide/178.png)

7.  Click Assign User. This will add the data abstractor to the Assigned To field. The new task will be visible in their My Tasks page.
8.  ![](military-eye-vision-injury-version-1-user-guide/179.png)To re-assign the task to a different data abstractor, click the Change link and repeat steps 6 and 7.

## Adding a New Encounter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](military-eye-vision-injury-version-1-user-guide/180.png)The Encounters for Referral page described on the previous page also allows users to add a new encounter for the current patient.

#### To add an encounter

7.  Click Add Encounter on the Filters/Actions menu.
8.  Complete the following fields:
    - Referral ID: This ID is used by the VA EIDS application and is automatically assigned.
    - Institution (required): Select the VISN and Facility from the drop-down list.
    - Visit Date (required): Enter the date of the encounter, in M/D/YYYY format, followed by the time (standard or military). The date can be spelled out, but it will revert to numerical format. Military time will revert to standard.

> -Or-

> ![](military-eye-vision-injury-version-1-user-guide/181.png)Use the Date and Time ![](military-eye-vision-injury-version-1-user-guide/182.png) pickers to select the date and time.

- Encounter Type (required): Select the visit type, Outpatient or Inpatient.

![](military-eye-vision-injury-version-1-user-guide/183.png)

9.  Click Save to save the changes, or Cancel to exit without saving.

## Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Reporting page allows administrators to generate a variety of reports and to export them to other file formats, such as Excel and Word.

#### To generate a report

1.  Click Reporting on the VA EIDS main menu.
2.  ![](military-eye-vision-injury-version-1-user-guide/184.png)Select the desired report from the report menu.
3.  Apply the corresponding filters:

> For the Patient Overview and Annual Completion reports:

- VISN: Select the VISN (all VISNs selected by default).
- Report Year Definition: Select the preference for Calendar or Fiscal year.
- Report Year: Select the Year(s) to include in the report.

![](military-eye-vision-injury-version-1-user-guide/185.png)

> For the User Event Log (which reports the activity of individual data abstractors):

- Username: Select the name of the data abstractor from the list.
- Referral / Encounter ID: Enter the optional Referral ID and/or Encounter ID
- ![](military-eye-vision-injury-version-1-user-guide/186.png)Date From / Date To: Enter the required date range, or click the Calendar icon to select the date range from the date picker.

![](military-eye-vision-injury-version-1-user-guide/187.png)

> For the DoD Interface Transfer report:

- ![](military-eye-vision-injury-version-1-user-guide/188.png)Date From / Date To: Enter the required date range, or click the Calendar icon to select the date range from the date picker.

![](military-eye-vision-injury-version-1-user-guide/189.png)

> (The Unique Patient report requires no filter setting.)

4.  Click Run Report, or Reset to reset the filters.

#### To export a report

- Upon generating the report, click the Export Word or Export Excel button and either click Open to open the file, or Save/Save As to save it to the hard drive.

## Adding System Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### To add users

1.  Click Administration in the VA EIDS main menu.

![](military-eye-vision-injury-version-1-user-guide/190.png)

> This opens the current list of users. From here, the administrator can edit the user’s contact information, edit their role, or remove them from the list.

![](military-eye-vision-injury-version-1-user-guide/191.png)

2.  Click Add User, and then enter the NT (VA) username into the search field:

![](military-eye-vision-injury-version-1-user-guide/192.png)

3.  Enter the user’s domain, full name, first and last name, and any other desired information into the text fields, and click Save to add the user. Click Close to return to the user list.

#### To view or edit user roles

1.  ![](military-eye-vision-injury-version-1-user-guide/193.png)Click Edit Roles
2.  Select the check box corresponding to each role to assign to the user.

![](military-eye-vision-injury-version-1-user-guide/194.png)

3.  Click Save to save the changes. Click Close to return to the user list.

#### To remove a user

- Click the corresponding Remove button, and then click OK to confirm.

#### To view/export the role matrix

1.  Click Role Matrix.
2.  The role matrix can be exported to Excel by clicking Download to Excel.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As a VA intranet Web site, VA EIDS troubleshooting procedures will usually involve contacting the VA EIDS network administrators or the NSD.

> Calls to the NSD should state that the user is working with the Converged Registries Solution and the VA Eye Injury Data Store. The NSD will then direct the trouble ticket to AITC, who will use established procedures to direct the problem to the CRS sustainment team..