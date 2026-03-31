---
title: Bed Management Solution Version 5.0 Admin Guide
doc_type: AG
doc_label: Administrator's Guide
doc_layer: anchor
doc_subject: Admin Guide
app_code: BMS
app_name: Bed Management Solution
section: FIN
app_status: active
pkg_ns: BMS
patch_ver: 5.0
patch_id: BMS*5.0
group_key: "BMS:BMS:5.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - span
  - class
  - admin
  - management
  - guide
  - figure
  - solution
  - version
  - report
  - anchor
page_count: 0
word_count: 28889
section_count: 7
table_count: 39
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: February 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Bed_Management_Solution_(BMS)/bms_5_0_ag.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Bed_Management_Solution_(BMS)/bms_5_0_ag.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=205"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Bed Management Solution (BMS)

  Admin Guide
---

![](bed-management-solution-version-5-0-admin-guide/001.png)

February 2026

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc205380062" class="anchor"></span>Table 2 - BMS Facility Site User Parameters</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 51%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/2025</td>
<td>5.5</td>
<td><p>Updated for BMS Patch WEBB-5-5</p>
<p>The following sections/figures were updated:</p>
<p>Figure 173 – new Regional Board DevExpress grid</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>08/2025</td>
<td>5.2</td>
<td><p>Updated for BMS patch version 5.2.</p>
<p>The following sections were updated:</p>
<p><strong>2.1.3</strong> – Orderable Items</p>
<p>The following figures were updated:</p>
<p><strong>Figure 265</strong> - User Access Report Results</p>
<p>The following tables were updated:</p>
<p><strong>Table 43</strong> - User Access Report Parameters</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>08/2025</td>
<td>5.3</td>
<td><p>Updated for BMS patch version 5.3.</p>
<p>The following sections were updated:</p>
<p><strong>2.1.5.1</strong> – Ward Whiteboard Kiosk URL Settings</p>
<p><strong>2.1.5.2</strong> – EMS Mobile URL Settings</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>07/2025</td>
<td>5.1</td>
<td><p>Updated for BMS patch version 5.1.</p>
<p>The following sections were added:</p>
<p><strong>2.1.20</strong> – Bed Level Management</p>
<p>The following sections were updated:</p>
<p><strong>1.2</strong> – Intended Audience</p>
<p><strong>2.1</strong> – Facility Administrator Users</p>
<p><strong>2.1.18</strong> – Reset SUMMARY Report Out-Of-Service/Do-Not-Display</p>
<p><strong>2.2.14</strong> – National Bed Tracking Levels</p>
<p>The following tables were updated:</p>
<p><strong>Table 44</strong> – National Bed Tracking Levels Parameters</p>
<p><strong>Table 45</strong> – Acronyms/Abbreviations</p>
<p>The following figures were added:</p>
<p><strong>Figure 272</strong> – National Bed Tracking Levels In Use Bed Level</p>
<p><strong>Figure 273</strong> – National Bed Tracking Levels “(INACTIVE)” Bed Level</p>
<p>The following figures were updated:</p>
<p><strong>Figure 1</strong> - Bed Board Site Configuration Page</p>
<p><strong>Figure 2</strong> - Selecting Site Options</p>
<p><strong>Figure 3</strong> - Selecting BMS User Add/Edit</p>
<p><strong>Figure 7</strong> - Selecting Site Options</p>
<p><strong>Figure 8</strong> - Selecting BMS User Add/Edit</p>
<p><strong>Figure 12</strong> - Selecting Site Options</p>
<p><strong>Figure 13</strong> - Selecting BMS User Add/Edit</p>
<p><strong>Figure 18</strong> - Selecting Site Options</p>
<p><strong>Figure 19</strong> - Selecting VistA Ward Add/Edit Page</p>
<p><strong>Figure 21</strong> - Selecting Site Options</p>
<p><strong>Figure 22</strong> - Selecting VistA Ward Add/Edit Page</p>
<p><strong>Figure 25</strong> - Selecting Site Options</p>
<p><strong>Figure 26</strong> - Selecting VistA Ward Add/Edit Page</p>
<p><strong>Figure 29</strong> - Selecting BMS Orderable Items Add/Delete</p>
<p><strong>Figure 31</strong> - Selecting Site Options</p>
<p><strong>Figure 32</strong> - Selecting BMS Orderable Items Add/Delete</p>
<p><strong>Figure 37</strong> - Selecting Site Options</p>
<p><strong>Figure 38</strong> - Selecting EMS Notification Add/Edit</p>
<p><strong>Figure 42</strong> - Selecting Site Options</p>
<p><strong>Figure 43</strong> - Selecting EMS Notification Add/Edit</p>
<p><strong>Figure 46</strong> - Selecting Site Options</p>
<p><strong>Figure 47</strong> - Selecting EMS Notification Add/Edit</p>
<p><strong>Figure 51</strong> - Selecting Facility Settings Add/Edit</p>
<p><strong>Figure 55</strong> - Selecting Site Options</p>
<p><strong>Figure 56</strong> - Selecting EMS Portal Access</p>
<p><strong>Figure 59</strong> - Selecting Site Options</p>
<p><strong>Figure 60</strong> - Selecting EMS Portal Access</p>
<p><strong>Figure 63</strong> - Selecting Site Options</p>
<p><strong>Figure 64</strong> - Selecting EMS Portal Access</p>
<p><strong>Figure 69</strong> - Selecting Site Options</p>
<p><strong>Figure 70</strong> - Selecting Unavailable Reason Add/Edit</p>
<p><strong>Figure 72</strong> - Selecting Site Options</p>
<p><strong>Figure 73</strong> - Selecting Unavailable Reason Add/Edit</p>
<p><strong>Figure 76</strong> - Selecting Site Options</p>
<p><strong>Figure 77</strong> - Selecting Unavailable Reason Add/Edit</p>
<p><strong>Figure 80</strong> - Selecting Discharge Appointment Clinics Add/Delete</p>
<p><strong>Figure 82</strong> - Selecting Site Options</p>
<p><strong>Figure 83</strong> - Selecting Discharge Appointment Clinics Add/Delete</p>
<p><strong>Figure 85</strong> - Selecting Event Notification Add/Edit</p>
<p><strong>Figure 87</strong> - Selecting Site Options</p>
<p><strong>Figure 88</strong> - Selecting Event Notification Add/Edit</p>
<p><strong>Figure 91</strong> - Selecting Site Options</p>
<p><strong>Figure 92</strong> - Selecting Event Notification Add/Edit</p>
<p><strong>Figure 95</strong> - Selecting Site Options</p>
<p><strong>Figure 96</strong> - Selecting Event Notification Add/Edit</p>
<p><strong>Figure 99</strong> - Selecting Site Configurable Icons Add/Edit</p>
<p><strong>Figure 102</strong> - Selecting Background Processors Add/Edit</p>
<p><strong>Figure 105</strong> - Selecting Site Options</p>
<p><strong>Figure 106</strong> - Selecting Waiting Area Add/Delete</p>
<p><strong>Figure 108</strong> - Selecting Site Options</p>
<p><strong>Figure 109</strong> - Selecting Waiting Area Add/Edit</p>
<p><strong>Figure 112</strong> - Selecting Site Options</p>
<p><strong>Figure 113</strong> - Selecting Waiting Area Add/Delete</p>
<p><strong>Figure 117</strong> - Selecting Site Options</p>
<p><strong>Figure 118</strong> - Selecting Waiting Area Add/Delete</p>
<p><strong>Figure 121</strong> - Facility Home Page</p>
<p><strong>Figure 122</strong> - Selecting Icon Usage Report</p>
<p><strong>Figure 125</strong> - BMS Bed Board Site Configuration BMS Icon Legend Screen</p>
<p><strong>Figure 127</strong> - BMS Bed Board Site Configuration / View Audit Log Screen</p>
<p><strong>Figure 141</strong> - Facility Home Page Site Options</p>
<p><strong>Figure 142</strong> - Bed Board Site Configuration Page Contingency Settings</p>
<p><strong>Figure 144</strong> - Evacuation On/Off</p>
<p><strong>Figure 146</strong> - Reset SUMMARY Report Out</p>
<p><strong>Figure 149</strong> - Community Care Sites link</p>
<p><strong>Figure 199</strong> <strong>(now 201)</strong> - Facility Home Page</p>
<p><strong>Figure 200 (now 202)</strong> - Facility Site Options Page</p>
<p><strong>Figure 204 (now 206)</strong> - Facility Site Options Page</p>
<p><strong>Figure 265</strong> <strong>(now 267)</strong> – National Bed Tracking Levels Text Field and Add Button</p>
<p><strong>Figure 266</strong> <strong>(now 268)</strong> - National Bed Tracking Levels Confirmation Screen</p>
<p><strong>Figure 267</strong> <strong>(now 269)</strong> - National Bed Tracking Levels Edit Link</p>
<p><strong>Figure 268 (now 270)</strong> - National Bed Tracking Levels Display Order Value Update</p>
<p><strong>Figure 269</strong> <strong>(now 271)</strong> - National Bed Tracking Levels Reordered Bed Level</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>01/2025</td>
<td>4.6</td>
<td><p>Updated for BMS patch version 4.6.</p>
<p>The following sections were added:</p>
<p><strong>2.2.1.4</strong> – National Bed Tracking Levels</p>
<p>The following sections were updated:</p>
<p><strong>Figure 172</strong> – Administration Section Page</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>06/2024</td>
<td>4.2</td>
<td><p>Updated for BMS patch version 4.2.</p>
<p>The following sections were updated:</p>
<p><strong>Title Page</strong> – Version number</p>
<p><strong>Page Footer</strong> – Version number</p>
<p>Note: Revision number (example: “4.2”) in this document’s Revision History table will represent the specific patch for a version of BMS.</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>04/2024</td>
<td>4.1</td>
<td>Created for BMS patch version 4.1.</td>
<td>Booz Allen Hamilton</td>
</tr>
</tbody>
</table>

<span id="_Toc205380062" class="anchor"></span>Table 2 - BMS Facility Site User Parameters

Table of Contents

List of Figures

List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Intended Audience](#intended-audience)
  - [Documentation Orientation](#documentation-orientation)
    - [Organization of the Manual](#organization-of-the-manual)
    - [Assumptions](#assumptions)
    - [Coordination](#coordination)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
- [Using the Software](#using-the-software)
  - [Facility Administrator Users](#facility-administrator-users)
    - [Bed Board Site Configuration Main Page](#bed-board-site-configuration-main-page)
    - [VistA Ward Add/Edit Page](#vista-ward-addedit-page)
    - [Bed Board BMS Orderable Items Configuration Page](#bed-board-bms-orderable-items-configuration-page)
    - [EMS Bed Notification Page](#ems-bed-notification-page)
    - [Facility Setting Page](#facility-setting-page)
    - [EMS Portal Access Page](#ems-portal-access-page)
    - [Bed Board Site Unavailable Reason Page](#bed-board-site-unavailable-reason-page)
    - [Bed Board Discharge Appointment Clinic Configuration Page](#bed-board-discharge-appointment-clinic-configuration-page)
    - [Events Notifications Page](#events-notifications-page)
    - [Site Configurable Icons Page](#site-configurable-icons-page)
    - [Background Processors Page](#background-processors-page)
    - [Patient Waiting Areas Page](#patient-waiting-areas-page)
    - [Icon Usage Report](#icon-usage-report)
    - [Bed Management Board Icons Page](#bed-management-board-icons-page)
    - [Audit Log Report Page](#audit-log-report-page)
    - [Contingency Settings](#contingency-settings)
    - [Evacuation On/Off](#evacuation-onoff)
    - [Reset SUMMARY Report Out-Of-Service/Do-Not-Display](#reset-summary-report-out-of-servicedo-not-display)
    - [Community Care Sites](#community-care-sites)
    - [Bed Level Management](#bed-level-management)
  - [Support Users](#support-users)
    - [Log in to the Administration Section Page](#log-in-to-the-administration-section-page)
    - [Maintain Marquee Text Page](#maintain-marquee-text-page)
    - [Add/Edit BMS User Page](#addedit-bms-user-page)
    - [Edit BMS Facility Settings Page](#edit-bms-facility-settings-page)
    - [Edit Sister Sites Page](#edit-sister-sites-page)
    - [Add/Edit Icon Page](#addedit-icon-page)
    - [View Audit Log Page – Support](#view-audit-log-page-support)
    - [Treating Specialty/NUMA/HAvBED Edit Page](#treating-specialtynumahavbed-edit-page)
    - [National Waiting Area](#national-waiting-area)
    - [National Unavailable Reason](#national-unavailable-reason)
    - [Background Processors Page](#background-processors-page-1)
    - [Application Parameters](#application-parameters)
    - [User Access Report](#user-access-report)
    - [National Bed Tracking Levels](#national-bed-tracking-levels)
- [Troubleshooting](#troubleshooting)
  - [BMS Self-Help Troubleshooting Guide](#bms-self-help-troubleshooting-guide)
- [Appendix A. Acronyms and Abbreviations](#appendix-a-acronyms-and-abbreviations)
- [Index](#index)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is designed to provide sufficient information about the Bed Management Solution (BMS) application to site admin and support users so that they can set up new logins and utilize the software.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides instructions on how to configure and how to use the Bed Management Solution (BMS) software. Typical audience for this manual will be local ADPAC staff who are asked to configure BMS logins, or support staff who need to configure BMS menus, background processors, etc. For additional technical information, refer to the Bed Management Solution Technical Manual. For general information on BMS, refer to the Bed Management Solution (BMS) User Guide, Community Care Tracking List User Guide or Bed Level Management User Guide.

## Documentation Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Organization of the Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Introduction – Explains BMS software and how it is used.
- System Summary - Provides a general description of the system written in non-technical terminology and the purpose for which it is intended.
- Getting Started - Provides a general walkthrough of the system from initiation through exit.
- Using the Software - Categorizes information and chapter titles by function and role of the software.
- Troubleshooting - Problems, issues, or items that a user may need assistance with and provide guidance to the extent possible.
- Acronyms and Abbreviations - Provides a list of the acronyms and abbreviations used in this document and the meaning of each.
- Index – A directory of the User Guide

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide was written with the following assumed experience/skills of the audience:

- User has basic knowledge of the operating system (such as the use of commands, menu options, and navigation tools).
- User has been provided the appropriate active roles, required for BMS.
- User has validated access to BMS.
- User has completed any prerequisite training.

### Coordination

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Bed Management Solutions business team will have two calls per month with end users and one call per month with the VISN teams to discuss upcoming changes and new functionality.
- OIT SPM HSP VFO HDSO BMS – T3 Sustainment Team, OIT EPMO HPS BMS Tier 2– T2 Support Team, BMS OERHM Project Lead and the BMS Cloud Migration Project Manager will be notified of all upcoming enhancements and release dates.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified*.*

#### Documentation Disclaimer

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual uses several methods to highlight different aspects of the material.

Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

<span id="_Toc205380061" class="anchor"></span>Table 1 - Documentation Symbols and Descriptions

| Symbol                                                                                                                                                              | Description                                                         |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| ![](bed-management-solution-version-5-0-admin-guide/002.png)                                  | The notepad icon emphasizes noteworthy information.                 |
| ![](bed-management-solution-version-5-0-admin-guide/003.png) | The warning icon indicates items of critical importance.            |
| ![](bed-management-solution-version-5-0-admin-guide/004.png)                              | The information icon refers the reader to additional documentation. |

<span id="_Toc48906492" class="anchor"></span>Table 20 - Whiteboard Patient Icon Usage Report Parameters

- Bold type indicates application elements (views, panes, links, buttons, and text boxes, for example) and key names.
- Italicized text indicates special emphasis.

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no COTS Product documentation required.

# Using the Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BMS users described in this user setup and admin guide can be grouped in the following types:

- Administrator Users
- Support Users

The following sections present the BMS pages that can be accessed by an Admin User or Support User, with a step-by-step description of each action.

![](bed-management-solution-version-5-0-admin-guide/005.png)For information on Site User, EMS User/Supervisor User, VISN User, Regional User, National User and Guest User functionality, see the Bed Management Solution User Guide.

![](bed-management-solution-version-5-0-admin-guide/006.png)For information on Community Care User, Community Care Transfer User and Community Care Admin functionality, see the BMS Community Care Tracking List guide.

## Facility Administrator Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrator users can customize the generic BMS settings according to the needs of a specific facility. This is done from the Bed Board Site Configuration (Site Options) page of the BMS facility site.

Administrator users can access the following pages:

- Vistal Ward Add/Edit page
- BMS Orderable Items Configuration page
- EMS Bed Notification Add/Edit page
- Facility Settings
- EMS Portal Access page
- Discharge Appointment Clinic Add/Edit page
- Events Notification Add/Edit page
- Site Configurable Icons page
- BMS User Add/Edit page
- Background Processors page
- Waiting Area Add/Delete page
- Icon Usage Report
- BMS Icon Legend page
- View Audit Log page
- Contingency Settings Page
- Community Care Sites
- Bed Level Management
- Unavailable Reason Add/Edit\*

![](bed-management-solution-version-5-0-admin-guide/007.png) Must be a support user to see this option

### Bed Board Site Configuration Main Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The configuration of the VA facility site—including the ability to configure BMS logins—is done using the options available in the page Bed Board Site Configuration that can be accessed by clicking the Site Options button on the facility home page.

The Bed Board Site Configuration page is displayed as in the following image.

<span id="_Toc205379788" class="anchor"></span>Figure 1 - Bed Board Site Configuration Page

![](bed-management-solution-version-5-0-admin-guide/008.png)

The Bed Board Site Configuration page allows the administrator user to configure several parameters for the site. Click the corresponding link to access the desired page.

The Evacuation ON/OFF option can be used in case of emergency and allows the administrator user to organize the evacuation process. For details, see the section [<u>Evacuation On/Off</u>.](\l)

In the lower part of the page the system provides information about the date and time of the workstation, the date and time of the facility site as well as the VISN, and the region where the current facility resides.

For details on the options available see the sections below.

#### Adding a BMS User to the Current Facility Site

To add a BMS user to the current facility site*,* follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc205379789" class="anchor"></span>Figure 2 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/009.png)

The Bed Board Site Configuration page is displayed as in the image below.

<span id="_Toc205379790" class="anchor"></span>Figure 3 - Selecting BMS User Add/Edit

![](bed-management-solution-version-5-0-admin-guide/010.png)

Select the BMS User Add/Edit link to display the page in the following image:

<span id="_Toc205379791" class="anchor"></span>Figure 4 - User Configuration Page

![](bed-management-solution-version-5-0-admin-guide/011.png)

Click the button Select Existing NT User Name (the user must have an account in VA’s Active Directory) click this button to display the following screen:

<span id="_Toc205379792" class="anchor"></span>Figure 5 - Select User

![](bed-management-solution-version-5-0-admin-guide/012.png)

From the Domain field select the domain to which the user currently belongs. Enter part of the name of the user in the User Name field then press the Find button to locate the user.

From the list in the central part of the screen select the user to whom you want to grant access to the current BMS facility site then press the Add/Edit Single User button. The following screen is displayed:

<span id="_Toc205379793" class="anchor"></span>Figure 6 - Customize BMS Facility Site User Rights

![](bed-management-solution-version-5-0-admin-guide/013.png)

The following parameters can be set for a user of a facility site:

<table>
<caption><p><span id="_Toc52890034" class="anchor"></span>Table 22 - Whiteboard Comments Usage Report Parameters</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NT User Name</td>
<td>NT user who will be given access rights to the facility site.</td>
</tr>
<tr class="even">
<td>Admin User?</td>
<td>If the new user will have access to the Administration section page.</td>
</tr>
<tr class="odd">
<td>Audit Log User?</td>
<td>If the new user will have access to the Audit Log function.</td>
</tr>
<tr class="even">
<td>Site User?</td>
<td>If the user will have access to the current facility site.</td>
</tr>
<tr class="odd">
<td>EMS User?</td>
<td>If the new user is part of EMS group.</td>
</tr>
<tr class="even">
<td>EMS Dispatcher?</td>
<td>If the new user is an EMS dispatcher.</td>
</tr>
<tr class="odd">
<td>EMS Supervisor User?</td>
<td>If the new user has EMS supervisor rights.</td>
</tr>
<tr class="even">
<td>Community Care User?</td>
<td>If the new user will have access to the Community Care Tracking List page. ![](bed-management-solution-version-5-0-admin-guide/014.png) The Admin User role will always inherit the Community Care User role’s permissions.</td>
</tr>
<tr class="odd">
<td>Community Care Transfer User?</td>
<td><p>If the new user will have access to both the Community Care Tracking List page and the Add to PPBPL function on the CCTL. In addition, this role allows edit access to the Transfer Out Reason and Transfer Out Type fields within a Community Care Tracking List record.</p>
<p>![](bed-management-solution-version-5-0-admin-guide/015.png)The Admin User role will always inherit the Community Care Transfer User role’s permissions. In addition, the Community Care Transfer User role includes the Community Care User role permissions by default.</p></td>
</tr>
<tr class="even">
<td>Community Care Admin?</td>
<td><p>If the new user will have site favorite configuration access on the Community Care Sites page.</p>
<p>![](bed-management-solution-version-5-0-admin-guide/016.png)The Admin User role will always inherit the Community Care Admin role’s permissions.</p>
<p>![](bed-management-solution-version-5-0-admin-guide/017.png)Note: To add, edit or delete Community Care facilities from the Community Care Sites page, an Admin User role is required.</p></td>
</tr>
<tr class="odd">
<td>Default Region</td>
<td>This field displays the name of the current region (where the current VISN belongs to).</td>
</tr>
<tr class="even">
<td>Default VISN</td>
<td>This field displays the current VISN (to which the current facility site belongs).</td>
</tr>
<tr class="odd">
<td>DefaultSite</td>
<td>The default site which is displayed when the new user logs into the system.</td>
</tr>
<tr class="even">
<td>READ Access</td>
<td>If the selected user has READ rights on the sites in the selected Region/VISN.</td>
</tr>
<tr class="odd">
<td>WRITE Access</td>
<td><p>If the selected user has WRITE rights on the sites in the selected Region/VISN.</p>
<p>![](bed-management-solution-version-5-0-admin-guide/018.png)The WRITE Access role does not apply to adding, editing or removing Community Care Tracking List records.</p></td>
</tr>
<tr class="even">
<td>Whiteboard Only Access</td>
<td>If the selected user has Whiteboard access only.</td>
</tr>
</tbody>
</table>

<span id="_Toc52890034" class="anchor"></span>Table 22 - Whiteboard Comments Usage Report Parameters

After setting the desired parameters for the selected user, click the Submit button to enter the data into the system.

![](bed-management-solution-version-5-0-admin-guide/019.png) For additional configurations available to Support Users, see the [Add/Edit BMS User Page](#addedit-bms-user-page) section located within this guide.

#### Editing BMS User Rights for the Current Facility Site

To edit the rights of a BMS user for the current facility site*,* follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc205379794" class="anchor"></span>Figure 7 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/020.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc205379795" class="anchor"></span>Figure 8 - Selecting BMS User Add/Edit

![](bed-management-solution-version-5-0-admin-guide/021.png)

Select the BMS User Add/Edit link to display the page in the following image:

<span id="_Toc205379796" class="anchor"></span>Figure 9 - BMS User Configuration Page

![](bed-management-solution-version-5-0-admin-guide/022.png)

Click the button Select Existing NT User Name to display the following screen:

<span id="_Toc205379797" class="anchor"></span>Figure 10 - Select User

![](bed-management-solution-version-5-0-admin-guide/023.png)

From the Domain field select the domain to which the user currently belongs. Enter part of the name of the user in the User Name field then press the Find button to locate the user.

From the list in the central part of the screen select the user whose rights for the current facility site you want to edit then press the Select button. The following screen is displayed:

<span id="_Toc205379798" class="anchor"></span>Figure 11 - Customize BMS Facility Site User Rights

![](bed-management-solution-version-5-0-admin-guide/024.png)

Modify the existing selections then click the Submit button to enter the new data into the system.

#### Deleting a BMS User for the Current Facility Site

To delete a BMS user (cancel his/her rights) for the current facility site, follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc205379799" class="anchor"></span>Figure 12 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/025.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc205379800" class="anchor"></span>Figure 13 - Selecting BMS User Add/Edit

![](bed-management-solution-version-5-0-admin-guide/026.png)

Select the BMS User Add/Edit link to display the page in the following image:

<span id="_Toc205379801" class="anchor"></span>Figure 14 - BMS User Configuration Page

![](bed-management-solution-version-5-0-admin-guide/027.png)

Click the button Select Existing NT User Name to display the following screen:

<span id="_Toc205379802" class="anchor"></span>Figure 15 - Select User

![](bed-management-solution-version-5-0-admin-guide/028.png)

From the Domain field select the domain to which the user currently belongs. Enter part of the name of the user in the User Name field then press the Find button to locate the user.

From the list in the central part of the screen select the user whose rights for the current facility site you want to edit then press the Select button. The following screen is displayed:

<span id="_Toc205379803" class="anchor"></span>Figure 16 - Customize BMS Facility Site User Rights

![](bed-management-solution-version-5-0-admin-guide/029.png)

Select “No” for all the available options the press the Submit button to enter the data into the system.

### VistA Ward Add/Edit Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Bed Board Site Configuration page, click the VistA Ward Add/Edit link to display the Bed Board Ward Configuration (Facility name) page as in the following image.<span id="_Toc52889540" class="anchor"></span>

Figure 17 - Add/Edit Ward Page

![](bed-management-solution-version-5-0-admin-guide/030.png)

The options available in this screen allow the administrator user to organize the wards retrieved from VistA according to the specific needs of the current facility.

The list of VistA wards already grouped according to the needs of the current organization is displayed in the list Current VistA Wards, in the center portion of the screen, while Combined Wards, if any, will be displayed at the bottom of the screen.

Clicking the header fields in the Current VistA Wards table (e.g., VistA Ward Name, VistA Specialty, BMS Type Group, etc.) allows administrator users to sort the ward group list according to those criteria. Group treating specialties together into one physical ward. For example, 2A-MED, 2A-SURGICAL, 2A-OBSERVATION will all have the same Ward Group name 2A so that all the beds will appear only once for the ward.

For each entry in the list, the following data is available:

<span id="_bookmark32" class="anchor"></span>Table 3 - Ward Group Parameters

| Column                      | Description                                                                                                                 |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Internal Entry Number (IEN) | The VistA Internal Entry Number for the primary lookup key in the Ward Location \#42 file.                                  |
| VistA Ward Name             | The name of the ward retrieved from VistA.                                                                                  |
| VistA Ward Specialty        | The specialty associated to the selected ward in VistA.                                                                     |
| BMS Type Group              | The specialty assigned to the ward group from the specialties defined for the current facility. (The BMS Type Group field.) |
| BMS Ward Group Text         | The ward group assigned for the needs of the current facility.                                                              |
| Census Categories           | The category the with which the ward is associated.                                                                         |
| Display Specialty           | Display(s) in which the ward appears.                                                                                       |
| Combined Ward               | The combined ward wherein a ward can become a member.                                                                       |

<span id="_Toc205380083" class="anchor"></span>Table 23 - Community Care Sites Parameters

The Edit and Delete links to the left of each ward group in the Current VistA Wards area allow the user either to modify the details of a ward group or to delete the ward group.

Combined Wards, if any, will be displayed in a table below the Current Wards.

The link Return to the Admin Main Page in the upper left corner of the page allows the user to go back to the Bed Board Site Configuration page on the large screen displays.

#### Adding a VistA Ward to the Ward Groups Defined for the Current Facility

To add a VistA ward to the ward groups defined for the current facility follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc51235901" class="anchor"></span>Figure 18 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/031.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235902" class="anchor"></span>Figure 19 - Selecting VistA Ward Add/Edit Page

![](bed-management-solution-version-5-0-admin-guide/032.png)

Click the VistA Ward Add/Edit link to display the corresponding page as in the image below:

<span id="_Toc51235903" class="anchor"></span>Figure 20 - Adding/Editing Ward

![](bed-management-solution-version-5-0-admin-guide/033.png)

- In the ADD Ward area at the top of the screen, choose a Type of VistA or Combined Ward.
- Click the arrow button of the VistA Ward Name field to display the list of VistA wards and select the one you want to add to the ward groups defined for the current facility.
- In the BMS Type Group field enter the name of one of the ward groups defined for the current facility or the name of a new ward group.
- In the Ward Group Text field enter a customized ward group name. Select Census Category as appropriate, as well as Display Specialty. The Ward can also become a member of a Combined Ward if desired.

Clicking the Save button will enter the data into the system. The new ward group will be displayed in the Current VistA Wards list in the lower part of the screen. Users can also utilize the Alt + B keyboard shortcut to perform the same functions as the Save button.

#### Editing a Ward Group

To edit one of the ward groups defined for the current facility follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc51235904" class="anchor"></span>Figure 21 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/034.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235905" class="anchor"></span>Figure 22 - Selecting VistA Ward Add/Edit Page

![](bed-management-solution-version-5-0-admin-guide/035.png)

Click the VistA Ward Add/Edit link to display the corresponding page as in the image below:

<span id="_Toc51235906" class="anchor"></span>Figure 23 - Selecting a Ward Group to Edit

![](bed-management-solution-version-5-0-admin-guide/036.png)

Click the Edit link to the left of an existing ward group. The ward group details will be displayed in the fields in the EDIT Ward area as in the following image:

<span id="_Toc51235907" class="anchor"></span>Figure 24 - Editing a Ward Group

![](bed-management-solution-version-5-0-admin-guide/037.png)

Make the desired changes then press the Save button to enter the data into the system. The modified ward group will be displayed in the Current VistA Wards list.

#### Deleting a Ward Group

To delete a ward group, follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc51235908" class="anchor"></span>Figure 25 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/038.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc205379813" class="anchor"></span>Figure 26 - Selecting VistA Ward Add/Edit Page

![](bed-management-solution-version-5-0-admin-guide/039.png)

Click the VistA Ward Add/Edit link to display the corresponding page as in the image below:

<span id="_Toc51235910" class="anchor"></span>Figure 27 - Deleting a VistA Ward Group

![](bed-management-solution-version-5-0-admin-guide/040.png)

Click the Delete link to the left of the ward group you want to delete. A confirmation screen is displayed as in the following image:

<span id="_Toc51235911" class="anchor"></span>Figure 28 - Confirm Deletion of VistA Ward Group

![](bed-management-solution-version-5-0-admin-guide/041.png)

Click the Delete button to delete the ward group defined.

### Bed Board BMS Orderable Items Configuration Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Bed Board Site Configuration page is displayed as in the image below.

<span id="_Toc51235912" class="anchor"></span>Figure 29 - Selecting BMS Orderable Items Add/Delete

![](bed-management-solution-version-5-0-admin-guide/042.png)

From the Bed Board Site Configuration page, click the BMS Orderable Items Add/Delete link to display the following page:

<span id="_Toc52889553" class="anchor"></span>Figure 30 - Bed Board BMS Orderable Items Configuration Page

![](bed-management-solution-version-5-0-admin-guide/043.png)

The Bed Board BMS Orderable Items Configuration page allows the user to map the orderable items coming from VistA with orderable items adapted to the needs of their facility/organization.

The drop-down fields in the upper part of the screen allow administrator users to select the orderable items for mapping. However, only three types of orderable items are mapped: admission, discharges and transfers.

The lower part of the screen displays the list of orderable items already mapped. The Delete links associated to each entry allow the administrator user to remove an entry from the list.

For Integrated sites, it is important that a particular Orderable Item, especially for the Admission Type, is uniquely mapped (via Orderable Item Number) to a single facility. Otherwise, it is possible that Admission Orders could be associated to more than one facility and thus, show on more than one facilities’ Admission Orders reports.

For each entry in the list, the following data is available:<span id="_bookmark47" class="anchor"></span>

Table 4 - Orderable Items Parameters

| Column                | Description                                                           |
|-----------------------|-----------------------------------------------------------------------|
| (Orderable item code) | The code of the VistA orderable item.                                 |
| Orderable Item        | The name of the orderable item retrieved from VistA.                  |
| Type                  | The name of the orderable item for the needs of the current facility. |

<span id="_Toc205380096" class="anchor"></span>Table 36 - Whiteboard Patient Icon Usage Report Parameters

The link Return to the Admin Main Page in the upper left corner of the page allows the administrator user to go back to the Bed Board Site Configuration page.

#### Adding/Deleting an Orderable Item - Mapping

To add a new orderable item mapping to the system, follow the instructions below.

From the facility home page, click the Site Options button.

<span id="_Toc51235914" class="anchor"></span>Figure 31 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/044.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235915" class="anchor"></span>Figure 32 - Selecting BMS Orderable Items Add/Delete

![](bed-management-solution-version-5-0-admin-guide/045.png)

Click the BMS Orderable Items Add/Delete link to display the following page:

<span id="_Toc51235916" class="anchor"></span>Figure 33 - Adding/Editing BMS Orderable Items

![](bed-management-solution-version-5-0-admin-guide/046.png)

Use the arrow button of the field CPRS BMS Orderable Item to display a list of orderable items existing in VistA and select the one you want to add/map (=rename for use in the current facility. Different facilities may use different names for Orderable Items). From the field Orderable Item Type select the orderable item type you want to use for your facility then click the Add button. The newly added (mapped) orderable item will be displayed in the list. You can use the Delete link to remove an entry (mapping) from the system.

<span id="_Toc51235917" class="anchor"></span>Figure 34 - BMS Orderable Items - Add

![](bed-management-solution-version-5-0-admin-guide/047.png)

<span id="_Toc51235918" class="anchor"></span>Figure 35 - BMS Orderable Items – Delete

![](bed-management-solution-version-5-0-admin-guide/048.png)

### EMS Bed Notification Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Bed Board Site Configuration page, click the EMS Notification Add/Edit link to display the following page:

<span id="_Toc51235919" class="anchor"></span>Figure 36 - EMS Bed Notification Page

![](bed-management-solution-version-5-0-admin-guide/049.png)

The options available in this page allow the administrator user to manage the EMS notifications.

![](bed-management-solution-version-5-0-admin-guide/050.png)Note: Notifications can also be sent by printer, pager and cell phones as well as email.

In the ADD Location Name area, the options allow the administrator user to add a new EMS Bed notification in the system.

The list in the lower part of the screen presents the locations for which EMS notifications have already been defined in the system.

For each entry in the list, the following data is available:

<span id="_bookmark55" class="anchor"></span>Table 5 - EMS Bed Notification Parameters

| Column                           | Description                                                                |
|----------------------------------|----------------------------------------------------------------------------|
| Name                             | The name of the BMS Ward Group which the EMS notification has been set up. |
| Send Notification/EMS Group      | The event that triggers the notification for the EMS group.                |
| Send Notification/Bed Controller | The event that triggers the notification for the bed controller.           |
| Send Notification/Other          | The event that triggers the notification for other personnel.              |

<span id="_Toc205380098" class="anchor"></span>Table 38 - Whiteboard Comments Usage Report Parameters

The links Edit and Delete to the left of each entry allow the administrator user to modify the details of a notification or to delete it.

The link Return to the Admin Main Page in the upper left corner of the page allows the administrator user to go back to the Site Options page.

#### Adding an EMS Bed Notification

To add an EMS bed notification, follow the instructions below.

From the facility home page, click the Site Options button:

<span id="_Toc471462924" class="anchor"></span>Figure 37 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/051.png)

The Bed Board Site Configuration page is displayed as in the image below.

<span id="_Toc51235921" class="anchor"></span>Figure 38 - Selecting EMS Notification Add/Edit

![](bed-management-solution-version-5-0-admin-guide/052.png)

Click the EMS Notification Add/Edit link to display the corresponding page as in the image below:

<span id="_Toc51235922" class="anchor"></span>Figure 39 - EMS Bed Notification – Add Location Name

![](bed-management-solution-version-5-0-admin-guide/053.png)

Click the arrow button of the Select a Ward Group field to display a list of locations defined in the system then click the Add button to enter the details of the notification.

The following page is displayed:<span id="_Toc52889563" class="anchor"></span>

Figure 40 - Notifications Add – Edit Parameters

![](bed-management-solution-version-5-0-admin-guide/054.png)

The name of the selected location is displayed in the page header. In the EDIT Parameters area, enter the email addresses, text pagers, text-compatible cell phones and/or printer where you want to send the current notification: EMS email, Bed Controller email, and Other. From the Notification Event area, select the events that trigger the current notification. Usually a bed clean request will trigger a notification to be sent to the bed controller.

![](bed-management-solution-version-5-0-admin-guide/055.png)Note: There is a 150-character limit. (FORMAT: name@address,name@address)

When you have selected the desired parameters for the current notification click the Submit button to enter the data into the system. A confirmation message is displayed and then you return to the main EMS Bed Notification page where the new notification is displayed in the list.

<span id="_Toc51235924" class="anchor"></span>Figure 41 - EMS Bed Notification Added

![](bed-management-solution-version-5-0-admin-guide/056.png)

#### Editing an EMS Bed Notification

To edit an existing EMS bed notification, follow the instructions below. From the facility home page, click the Site Options button.<span id="_Toc52889565" class="anchor"></span>

Figure 42 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/057.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc52889566" class="anchor"></span>Figure 43 - Selecting EMS Notification Add/Edit

![](bed-management-solution-version-5-0-admin-guide/058.png)

Click the EMS Notification Add/Edit link to display the corresponding page as in the image below:

<span id="_Toc52889567" class="anchor"></span>Figure 44 - EMS Bed Notification – Select Notification for Edit

![](bed-management-solution-version-5-0-admin-guide/059.png)

Click the Edit link to the left of an EMS Bed notification. The EMS Bed Notification Edit page is displayed as in the image below:

<span id="_Toc51235928" class="anchor"></span>Figure 45 - Notifications Add – Edit Parameters

![](bed-management-solution-version-5-0-admin-guide/060.png)

![](bed-management-solution-version-5-0-admin-guide/061.png)Note: There is a 150-character limit. (FORMAT: name@address,name@address)

Make the desired changes then click the Submit button to enter the data into the system.

#### Deleting an EMS Bed Notification

To delete an EMS bed notification, follow the instructions below. From the facility home page, click the Site Options button.<span id="_Toc52889569" class="anchor"></span>

Figure 46 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/062.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235930" class="anchor"></span>Figure 47 - Selecting EMS Notification Add/Edit

![](bed-management-solution-version-5-0-admin-guide/063.png)

Click the EMS Notification Add/Edit link to display the corresponding page as in the image below:

<span id="_Toc51235931" class="anchor"></span>Figure 48 - EMS Bed Notification – Delete notification

![](bed-management-solution-version-5-0-admin-guide/064.png)

Click the Delete link to the left of an EMS Bed notification. A confirmation screen is displayed as in the following image:

<span id="_Toc51235932" class="anchor"></span>Figure 49 - EMS Bed Notification – Confirm Notification Deletion

![](bed-management-solution-version-5-0-admin-guide/065.png)

Click the Delete Record button to delete the notification. A message is displayed in the following image:

<span id="_Toc51235933" class="anchor"></span>Figure 50 - EMS Bed Notification – Notification Deletion

![](bed-management-solution-version-5-0-admin-guide/066.png)

### Facility Setting Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235934" class="anchor"></span>Figure 51 - Selecting Facility Settings

![](bed-management-solution-version-5-0-admin-guide/067.png)

From the Bed Board Site Configuration page, click the Facility Setting link to display the following page:

<span id="_Toc205379839" class="anchor"></span>Figure 52 - Facility Configuration Page – Integrated Facility

![](bed-management-solution-version-5-0-admin-guide/068.png)

<span id="_Toc51235936" class="anchor"></span>Figure 53 - Facility Configuration Page – Non-Integrated Facility

![](bed-management-solution-version-5-0-admin-guide/069.png)

The following parameters can be configured:

<span id="_bookmark73" class="anchor"></span>Table 6 - VA Facility Configuration Parameters

<table>
<caption><p><span id="_bookmark458" class="anchor"></span>Table 45 - Acronyms/Abbreviations</p></caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BMS Server Time Zone</td>
<td>The time zone of the BMS server where the current facility is connected.</td>
</tr>
<tr class="even">
<td>Facility Site Time Zone</td>
<td>The time zone of the facility site.</td>
</tr>
<tr class="odd">
<td>Auto-Removal Patient Pending Bed Placement List?</td>
<td>If patients are automatically removed from the local facility Patients Pending Bed Placement List when they are assigned a Room/Bed.</td>
</tr>
<tr class="even">
<td>Auto-Removal Edis Patients from Pending Bed Placement List?</td>
<td>If Emergency Department Integration Software (EDIS) patients are automatically removed from the local facility Pending Bed Placement List when they are assigned a Room/Bed.</td>
</tr>
<tr class="odd">
<td>Auto Placement of Transfers onto PPBP List?</td>
<td>If patients are automatically placed on the local facility Patients Pending Bed Placement List when they are transferred.</td>
</tr>
<tr class="even">
<td>Integrated Facility?</td>
<td>If the current facility is integrated with others (sister sites).</td>
</tr>
<tr class="odd">
<td>Allowed Access – Integrated Sites: (All users can see these sites also).</td>
<td><p>This field will only become visible after you have selected a sister sites list from the Integrated Site List field, pressed the <strong>Submit</strong> button and returned to the Facility Configuration page.</p>
<p>A list of sites integrated with the current site is displayed; select the sites where the users of the current facility will have access.</p></td>
</tr>
<tr class="even">
<td>Medical Center ID #</td>
<td>The ID number of the medical center associated to the current facility.</td>
</tr>
<tr class="odd">
<td>Ward Prefix</td>
<td>A prefix used for all the wards defined for the current facility.</td>
</tr>
<tr class="even">
<td>Ward Suffix</td>
<td>A suffix used for all the wards defined for the current facility.</td>
</tr>
<tr class="odd">
<td>ADT Prefix</td>
<td>This is the unique identifier that is the leading part of the ADT (Admission/Discharge/Transfer Orderable Item) and is used to filter the list of ADT OIs that will be displayed. For example, “BO-” for Boston.</td>
</tr>
<tr class="even">
<td>ADT Suffix</td>
<td>This is the unique identifier that is the trailing part of the ADT (Admission/Discharge/Transfer Orderable Item) and is used to filter the list of ADT OIs that will be displayed. For example, “BO-” for Boston.</td>
</tr>
<tr class="odd">
<td>Facility Name</td>
<td>The full name of the current facility.</td>
</tr>
<tr class="even">
<td>Facility Address 1</td>
<td>The main address of the facility.</td>
</tr>
<tr class="odd">
<td>Facility Address 2</td>
<td>If applicable, any secondary address of the facility.</td>
</tr>
<tr class="even">
<td>Facility Point-of-Contact:</td>
<td>The facility point of contact, which can be the triage room, the front desk or others.</td>
</tr>
<tr class="odd">
<td>Facility POC email:</td>
<td>The email for the point of contact with the facility.</td>
</tr>
<tr class="even">
<td>Facility POC Telephone:</td>
<td>The telephone of the point of contact.</td>
</tr>
<tr class="odd">
<td>Local Time Adjust:</td>
<td>The difference between the local time and the server time.</td>
</tr>
<tr class="even">
<td>EMS Default User Name:</td>
<td>The BMS Service Account ID needed to load the EMS Mobile Page for Mobile Devices.</td>
</tr>
<tr class="odd">
<td>EMS Password:</td>
<td>The BMS Service Account ID password needed to load the EMS Mobile Page for Mobile Devices.</td>
</tr>
<tr class="even">
<td>EMS Password confirm:</td>
<td>The confirmation of the password.</td>
</tr>
<tr class="odd">
<td>Whiteboard Kiosk Default User Name:</td>
<td>The BMS Service Account ID, along with the fully qualified domain name in front of the BMS Service Account ID, needed to load the Whiteboard URL in Kiosk Mode. (Example: v16.med.va.gov\VHAHOUxxx)</td>
</tr>
<tr class="even">
<td>Whiteboard Kiosk Password:</td>
<td>The BMS Service Account ID password needed to load the Whiteboard URL in Kiosk Mode.</td>
</tr>
<tr class="odd">
<td>Whiteboard Kiosk Password confirm:</td>
<td>The confirmation of the password.</td>
</tr>
</tbody>
</table>

<span id="_bookmark458" class="anchor"></span>Table 45 - Acronyms/Abbreviations

#### Ward Whiteboard Kiosk URL Settings

The Ward Whiteboard URL is needed in order to display the information in the Ward Whiteboard page on the screens available on the wall(s) at the hospitals.

In order to run the following URL, a Whiteboard Kiosk Default User and password need to be defined in the Site Options -\> Facility Settings page. The user should be setup as a Service Account and needs to be granted the EMS USER role level of access. See the BMS Technical Manual for additional information.

Below is an example of the URL that should be added to the browser:

Description and available values of the page parameters:

<u>https://\<bms-url\>.gov/KioskWhiteboard/Index?facilityCode=BRK&wardName=All&splitScreen=No&displayPTCode=LastName&genderColorCode=None&displayFooterCensus=No&displayStaffAttending=Staff</u>

<span id="_bookmark74" class="anchor"></span>Table 7 - Ward Whiteboard URL Configuration Parameters

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 48%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Short Description</th>
<th>Options</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>facilityCode</td>
<td>Code of facility (e.g., BROCKTON = BRK).</td>
<td>Enter the 3 character facility ID.</td>
</tr>
<tr class="even">
<td>wardName</td>
<td>Name of BMS Ward Name. To see all the wards the value that needs to be configured is ALL.</td>
<td>These are the BMS WARDS as defined in the Facility, Site Options, VistA Ward Add/Edit. The Ward name value should match the "BMS WARD GROUP TEXT". A single ward can be entered or the value "ALL" to display all the wards at the facility.</td>
</tr>
<tr class="odd">
<td>splitScreen</td>
<td>To split the page in two tables enters the value "Yes".</td>
<td>Yes No</td>
</tr>
<tr class="even">
<td>displayPTCode</td>
<td>How should be displayed the patient under the column "Patient" (full name or 1st+Last 4).<br />
![](bed-management-solution-version-5-0-admin-guide/070.png)<strong>Note: LastName is required for Kiosk mode due to Privacy regulations</strong>.</td>
<td>FirstAndLast4 LastName</td>
</tr>
<tr class="odd">
<td>genderColorCode</td>
<td>To change the background color for the row according with patient’s gender.</td>
<td>Blue/Pink None</td>
</tr>
<tr class="even">
<td>displayFooterCensus</td>
<td>To view the footer census.</td>
<td>Yes No</td>
</tr>
<tr class="odd">
<td>displayStaffAttending</td>
<td>What column is displayed in the table? (Staff column, Attending column or both).</td>
<td><p>Staff and Attending Staff</p>
<p>Attending</p></td>
</tr>
<tr class="even">
<td>scrollRate</td>
<td>The timer interval will affect the scrolling speed. This parameter can be absent. (If specified then it represents seconds).</td>
<td>Null or an integer value.</td>
</tr>
</tbody>
</table>

#### EMS Mobile URL Settings

The EMS Mobile URL is needed in order to display the information in the EMS Mobile page on portable devices used by EMS Staff.

In order to run the following URL, an EMS Default User and password need to be defined in the Site Options \> Facility Settings page. The user should be setup as a Service Account and needs to be assigned to the EMS USER role. See the BMS Technical Manual for additional information. This can be the same account that is used for the BMS Kiosk Default User.

Below is an example of the URL that should be added to the browser:

<u>https://\<bms-url\>.gov/EMSMobile/Index?Code=BRK</u>

Description and available values of the page parameters:

<span id="_Toc205380068" class="anchor"></span>Table 8 - EMS Mobile URL Configuration Parameters

| Parameter | Short Description                        | Options                            |
|-----------|------------------------------------------|------------------------------------|
| Code      | Code of facility (e.g., BROCKTON = BRK). | Enter the 3 character facility ID. |

### EMS Portal Access Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Bed Board Site Configuration page, click the EMS Portal Access link to display the following page.

<span id="_Toc51235937" class="anchor"></span>Figure 54 - EMS Portal Access

![](bed-management-solution-version-5-0-admin-guide/071.png)

This page allows the administrator user to add, edit or delete EMS user accounts and their associated PINs. These EMS user accounts can then be used to access the EMS Staff Page for Mobile Devices.

![](bed-management-solution-version-5-0-admin-guide/072.png)For details see the section “EMS Staff Page for Mobile Devices” within the Bed Management Solution (BMS) User Guide. The EMS users added from this page will be available when a bed clean operation has to be assigned.

![](bed-management-solution-version-5-0-admin-guide/073.png)Note: It is recommended that each facility define at least one default EMS Staff User. This verifies that beds can always be assigned to a cleaner.

#### Adding an EMS User

To add an EMS user for the EMS Staff Page for Mobile Devices, follow the instructions below.

From the facility home page, click the Site Options button.

<span id="_Toc52889578" class="anchor"></span>Figure 55 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/074.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235939" class="anchor"></span>Figure 56 - Selecting EMS Portal Access

![](bed-management-solution-version-5-0-admin-guide/075.png)

Click the EMS Portal Access link to display the corresponding page as in the image below:

<span id="_Toc52889580" class="anchor"></span>Figure 57 - EMS Portal Access

![](bed-management-solution-version-5-0-admin-guide/076.png)

Click the Add EMS User button to display the following page:

<span id="_Toc51235941" class="anchor"></span>Figure 58 - EMS Portal Access Page – Add Users

![](bed-management-solution-version-5-0-admin-guide/077.png)

The VA Account field will display a list of all the EMS users who already have an account and for whom the current facility is the default facility. Select a name from the list and then enter a PIN number in the PIN field. The selected EMS user will be able to access the EMS Staff Page for Mobile Devices with their current user name and the PIN set in this page.

The second Non-VA Account field allows the administrator user to create an account for EMS users who do not have an account, and to assign a PIN code for this account. The EMS user will then be able to access the EMS Staff Page for Mobile Devices using this account, view information and make changes in that page.

#### Editing an EMS User

To edit the details of an EMS user for the EMS Staff Page for Mobile Devices follow the instructions below.

From the facility home page, click the Site Options button.

<span id="_Toc51235942" class="anchor"></span>Figure 59 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/078.png)

The Bed Board Site Configuration page is displayed as in the image below.

<span id="_Toc52889583" class="anchor"></span>Figure 60 - Selecting EMS Portal Access

![](bed-management-solution-version-5-0-admin-guide/079.png)

Click the EMS Portal Access link to display the corresponding page as in the image below:

<span id="_Toc51235944" class="anchor"></span>Figure 61 - Select EMS Staff Account/User to Edit

![](bed-management-solution-version-5-0-admin-guide/080.png)

Click the Edit link to the left of the EMS user name in the list. The EMS Portal Edit page is displayed.

<span id="_Toc51235945" class="anchor"></span>Figure 62 - Edit EMS Staff Account/User

![](bed-management-solution-version-5-0-admin-guide/081.png)

Change the PIN assigned to the EMS user, then press the Submit button to enter the data into the system.

#### Deleting an EMS User

To delete an EMS user for the EMS Staff Page for Mobile Devices follow the instructions below.

From the facility home page, click the Site Options button.

<span id="_Toc51235946" class="anchor"></span>Figure 63 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/082.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235947" class="anchor"></span>Figure 64 - Selecting EMS Portal Access

![](bed-management-solution-version-5-0-admin-guide/083.png)

Click the EMS Portal Access link to display the corresponding page as in the image below:

<span id="_Toc52889588" class="anchor"></span>Figure 65 - Selecting EMS Staff Account/User for Deletion

![](bed-management-solution-version-5-0-admin-guide/084.png)

Click the Delete link to the left of an EMS user in the list: a confirmation screen is displayed as in the following image.

<span id="_Toc51235949" class="anchor"></span>Figure 66 - Delete EMS Staff Account/User

![](bed-management-solution-version-5-0-admin-guide/085.png)

Click the Delete Record button to delete the EMS User from the list.

### Bed Board Site Unavailable Reason Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Bed Board Site Unavailable Reason page is displayed using the link below:

<span id="_Toc51235950" class="anchor"></span>Figure 67 - Selecting Unavailable Reason Add/Edit

![](bed-management-solution-version-5-0-admin-guide/086.png)

![](bed-management-solution-version-5-0-admin-guide/087.png)Note: This option is only available for users with the Support User role.

From the Bed Board Site Configuration page, click the Unavailable Reason Add/Edit link to display the following page:

<span id="_Toc51235951" class="anchor"></span>Figure 68 - Bed Board Unavailable Reason Page

![](bed-management-solution-version-5-0-admin-guide/088.png)

The page presents the list of default *unavailable* reasons defined in the system.

The options in this page allow the administrator user to add a new *unavailable* reason for the beds in the current facility.

For each entry in the list, the following data is available:

<span id="_bookmark92" class="anchor"></span>Table 9 - Unavailable Reason Parameters

| Column             | Description                               |
|--------------------|-------------------------------------------|
| Unavailable Reason | The reason why a bed is made unavailable. |
| Type               | The type of reason.                       |

The links Edit and Delete allow the administrator user to modify the details of a reason or delete it from the system.

The link Return to the Admin Main Page in the upper left corner of the page allows the administrator user to go back to the Site Options page.

#### Adding an Unavailable Reason

To add an *unavailable* reason*,* follow the instructions below. From the home page, click the Site Options button.

<span id="_Toc51235952" class="anchor"></span>Figure 69 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/089.png)

The Bed Board Site Configuration page is displayed as in the image below.

<span id="_Toc51235953" class="anchor"></span>Figure 70 - Selecting Unavailable Reason Add/Edit

![](bed-management-solution-version-5-0-admin-guide/090.png)

Select the Unavailable Reason Add/Edit link to display the page in the following image.

<span id="_Toc52889594" class="anchor"></span>Figure 71 - Adding an Unavailable Reason

![](bed-management-solution-version-5-0-admin-guide/091.png)

In the Text field enter the explanation, the reason for the bed unavailability, then from the Type field select the type of reason, and click the Add button.

In the Type field, four types of ‘unavailable’ reasons can be selected:

- Information (no icon appears on the whiteboard)
- Isolation (isolation icon appears on the whiteboard)
- Do Not Display (bed does not appear on the whiteboard)
- Out of Service (bed is colored RED on the whiteboard)

The newly defined reason will be added to list of existing reasons.

You can use the Edit link to modify either the text or the type of the reason. Use the Delete link to remove the link from the list.

#### Editing an Unavailable Reason

To edit an unavailable reason, follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc52889595" class="anchor"></span>Figure 72 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/092.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235956" class="anchor"></span>Figure 73 - Selecting Unavailable Reason Add/Edit

![](bed-management-solution-version-5-0-admin-guide/093.png)

Select the Unavailable Reason Add/Edit link to display the page in the following image:

<span id="_Toc51235957" class="anchor"></span>Figure 74 - Selecting an Unavailable Reason for Edit

![](bed-management-solution-version-5-0-admin-guide/094.png)

Click the Edit link associated to the unavailable reason that you want to modify. The following page is displayed:

<span id="_Toc51235958" class="anchor"></span>Figure 75 - Editing an Unavailable Reason

![](bed-management-solution-version-5-0-admin-guide/095.png)

Operate the desired changes in the Text and/or Type fields then press the Submit button to enter the data into the system.

#### Deleting an Unavailable Reason

To delete an unavailable reason*,* follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc52889599" class="anchor"></span>Figure 76 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/096.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235960" class="anchor"></span>Figure 77 - Selecting Unavailable Reason Add/Edit

![](bed-management-solution-version-5-0-admin-guide/097.png)

Select the Unavailable Reason Add/Edit link to display the page in the following image:

<span id="_Toc51235961" class="anchor"></span>Figure 78 - Select an Unavailable Reason for Deletion

![](bed-management-solution-version-5-0-admin-guide/098.png)

Click the Delete link associated with the unavailable reason that you want to delete. A confirmation screen is displayed as in the following image:

<span id="_Toc51235962" class="anchor"></span>Figure 79 - Delete an Unavailable Reason

![](bed-management-solution-version-5-0-admin-guide/099.png)

Click the Delete Record button to delete the unavailable reason from the list.

### Bed Board Discharge Appointment Clinic Configuration Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Bed Board Discharge Appointment Clinic Configuration page is displayed using the link below:

<span id="_Toc52889603" class="anchor"></span>Figure 80 - Selecting Discharge Appt Clinics Add/Delete

![](bed-management-solution-version-5-0-admin-guide/100.png)

From the Bed Board Site Configuration page, click the Discharge Appt Clinics Add/Delete link to display the following page:

<span id="_Toc51235964" class="anchor"></span>Figure 81 - Discharge Appointment Clinics Add/Edit Page

![](bed-management-solution-version-5-0-admin-guide/101.png)

The options in this screen allow the administrator user to define the discharge clinics used to assist with patient discharges (if part of the facility’s processes). In addition, the defining of Discharge Appointment Clinics will allow the automated assignment of the Anticipated Discharge (“A”) icon on the facility’s Whiteboard.

The options in the upper part of the screen allow the administrator user to define/add a new discharge appointment clinic in the system.

The list in the lower part of the screen presents the discharge appointment clinics already defined in the system. The Delete link to the left of each entry in the list allows the user to delete the clinic from the system.

To go back to the Bed Board Site Configuration page, click the link Return to the Admin Main Page in the upper left corner of the page.

#### Adding/Deleting a Discharge Appointment Location

To add a discharge appointment location, follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc52889605" class="anchor"></span>Figure 82 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/102.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_bookmark107" class="anchor"></span>Figure 83 - Selecting Discharge Appointment Clinics Add/Delete

![](bed-management-solution-version-5-0-admin-guide/103.png)

Select the Discharge Appt Clinics Add/Delete link to display the page in the following image:

<span id="_Toc51235967" class="anchor"></span>Figure 84 - Selecting a Discharge Clinic Location

![](bed-management-solution-version-5-0-admin-guide/104.png)

Use the arrow button of the field Discharge Clinic Location to display the available locations and select the one you want to add then press the Add button. The newly added discharge clinic location will be added to the list. To delete an entry from the list, use the associated Delete link.

### Events Notifications Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Events Notifications configuration page is displayed using the link below:

<span id="_Toc51235968" class="anchor"></span>Figure 85 - Selecting Event Notification Add/Edit

![](bed-management-solution-version-5-0-admin-guide/105.png)

From the Bed Board Site Configuration page, click the Event Notification Add/Edit page link to display the following page:

<span id="_Toc51235969" class="anchor"></span>Figure 86 - Events Notifications Page

![](bed-management-solution-version-5-0-admin-guide/106.png)

The options available in this screen allow the administrator user to manage the event notifications in the system.

![](bed-management-solution-version-5-0-admin-guide/107.png)Note: Notifications can also be sent by printer, pager and cell phones as well as email.

For each notification in the list, the following data is available:<span id="_bookmark111" class="anchor"></span>

Table 10 - Event Notification Parameters

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Column</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Current Locations</td>
<td>The location for which the event notification has been defined.</td>
</tr>
<tr class="even">
<td>Event Type</td>
<td>The event type, which triggers the notification.</td>
</tr>
<tr class="odd">
<td>Admission Order</td>
<td>Is there a physician admission order?</td>
</tr>
<tr class="even">
<td>Anticipated Discharge Order</td>
<td>Is there an Anticipated Discharge order?</td>
</tr>
<tr class="odd">
<td>Discharge Appointment</td>
<td>Is there a discharge appointment?</td>
</tr>
<tr class="even">
<td>Discharge Order</td>
<td>Is there a physician discharge order?</td>
</tr>
<tr class="odd">
<td>Transfer Order</td>
<td>Is there a physician transfer order?</td>
</tr>
<tr class="even">
<td>Bed Out of Service (OOS)</td>
<td>Is there a bed OOS?</td>
</tr>
<tr class="odd">
<td>Bed Switch</td>
<td><p>Is there a bed switch? This occurs when a patient moves from one bed to another within the same ward. (Example: patient movement from Cardio Wing Bed 1 to Cardio Wing Bed 2).</p>
<p>![](bed-management-solution-version-5-0-admin-guide/108.png)Do not confuse bed switch with “transfer” which occurs when a patient moves to a bed on a different ward.</p></td>
</tr>
</tbody>
</table>

The link Edit to the left of each entry in the list allows the user to modify the details of an event notification. A notification can be deleted using the adjacent Delete link.

To go back to the Bed Board Site Configuration page, click the link Return to the Admin Main Page in the upper left corner of the page.

#### Adding an Events Notification

To add an events notification, follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc52889610" class="anchor"></span>Figure 87 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/109.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235971" class="anchor"></span>Figure 88 - Selecting Event Notification Add/Edit

![](bed-management-solution-version-5-0-admin-guide/110.png)

Select the Event Notification Add/Edit link to display the page as in the following image:

<span id="_Toc51235972" class="anchor"></span>Figure 89 - Selecting the Location of the Events

![](bed-management-solution-version-5-0-admin-guide/111.png)

Click the arrow button of the Location field to display the list of ward groups defined in the system then click the ADD button. The following page is displayed:

<span id="_Toc51235973" class="anchor"></span>Figure 90 - Edit Event Notification Parameters

![](bed-management-solution-version-5-0-admin-guide/112.png)

The name of the selected location is displayed in the upper part of the screen and a list of events is presented. In the Bed Controller/Other field associated to an event enter the email addresses, text pagers, text-compatible cell phones and/or printer where you want to send the notification. From the drop-down fields in the Notify column, set whether the new notification will actually be sent or not then click the Submit button to enter the data into the system.

#### Editing an Events Notification

To edit the details of an event notification, follow the steps below.

From the facility home page, click the Site Options button.

<span id="_Toc52889614" class="anchor"></span>Figure 91 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/113.png)

The Bed Board Site Configuration page is displayed as in the image below.

<span id="_Toc51235975" class="anchor"></span>Figure 92 - Selecting Event Notification Add/Edit

![](bed-management-solution-version-5-0-admin-guide/114.png)

Select the Event Notification Add/Edit link to display the page in the following image:

<span id="_Toc51235976" class="anchor"></span>Figure 93 - Selecting Event Notification for Edit

![](bed-management-solution-version-5-0-admin-guide/115.png)

Click the Edit link associated to the event notification you want to modify. The following page is displayed:

<span id="_Toc51235977" class="anchor"></span>Figure 94 - Modifying Parameters for an Event Notification

![](bed-management-solution-version-5-0-admin-guide/116.png)

Modify the desired settings then press the Submit button to enter the data into the system. The modified event notification will be displayed in the event notifications list with the new settings.

#### Deleting an Events Notification

To delete an event notification, follow the steps below. From the facility home page, click the Site Options button:

<span id="_Toc51235978" class="anchor"></span>Figure 95 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/117.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51235979" class="anchor"></span>Figure 96 - Selecting Event Notification Add/Edit

![](bed-management-solution-version-5-0-admin-guide/118.png)

Select the Event Notification Add/Edit link to display the page as in the following image:<span id="_Toc51235980" class="anchor"></span>

Figure 97 - Selecting Event Notification for Deletion

![](bed-management-solution-version-5-0-admin-guide/119.png)

Click the Delete link associated with the events notification that you want to delete. A confirmation screen is displayed as in the following image:

<span id="_Toc51235981" class="anchor"></span>Figure 98 - Delete an Event Notification

![](bed-management-solution-version-5-0-admin-guide/120.png)

Click the Delete Record button to delete the events notification from the list.

### Site Configurable Icons Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ICON LIBRARY – SITE CONFIGURABLE ICONS page is displayed using the link below:

<span id="_Toc51235982" class="anchor"></span>Figure 99 - Selecting Site Configurable Icons

![](bed-management-solution-version-5-0-admin-guide/121.png)

From the Bed Board Site Configuration page, click the Site Configurable Icons link to display the following page.

![](bed-management-solution-version-5-0-admin-guide/122.png) NOTE: Users are discouraged from using the words DNR/DNI in the comment of the Ward Whiteboard or using any icon to represent DNR/DNI on the Ward Whiteboard.

<span id="_Toc51235983" class="anchor"></span>Figure 100 - Icon Library – Site Configurable Icons Page

![](bed-management-solution-version-5-0-admin-guide/123.png)

A list of site configurable icons is displayed. These icons can only be used on the site of the current facility.

Colored icons are active and can be used to convey information on the Whiteboard; grayed icons are inactive and cannot be used on the Whiteboard. The user can edit the details of an icon.

To go back to the Bed Board Site Configuration page, click the link Return to the Admin Main Page in the upper left corner of the page.

#### Editing an Icon

In the Icon Library – Site Configurable Icons page click the Edit link to the left of the icon you want to edit to display the following screen:

<span id="_Toc51235984" class="anchor"></span>Figure 101 - Icon Library – Edit Icon Page

![](bed-management-solution-version-5-0-admin-guide/124.png)

The following parameters can be set for an icon:

<span id="_bookmark127" class="anchor"></span>Table 11 - Icon Parameters

| Column                    | Description                                                                           |
|---------------------------|---------------------------------------------------------------------------------------|
| Active Yes/No             | If the icon is active or not.                                                         |
| Isolation Yes/No          | If the icon is associated with an isolation area or not.                              |
| Patient/Bed/Room          | If the icon is to be attached to a patient or to a bed/room.                          |
| Facility Icon Name        | Mandatory field, the name of the icon.                                                |
| Facility Icon Description | Mandatory field, the description of the icon.                                         |
| Facility Comment          | Any relevant additional info about the icon.                                          |
| Facility Mouse Over Text  | Mandatory field, the text to be displayed when the mouse cursor hovers over the icon. |

![](bed-management-solution-version-5-0-admin-guide/125.png)The fields will only be mandatory if the icon is active.

After you have defined the desired parameters for the icon click the Save button to enter the data into the system.

![](bed-management-solution-version-5-0-admin-guide/126.png) NOTE: Once an icon has been used to flag a patient or a bed, it cannot be inactivated. In order to be able to make the icon inactive the user will have to remove the icon from Whiteboard where it has been used.

### Background Processors Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Background Processors page is displayed using the link below:

<span id="_Toc51236002" class="anchor"></span>Figure 102 - Selecting Background Processors

![](bed-management-solution-version-5-0-admin-guide/127.png)

From the Bed Board Site Configuration page, click the Background Processors link to display the following page:

<span id="_Toc51236003" class="anchor"></span>Figure 103 - Facility Background Processors

![](bed-management-solution-version-5-0-admin-guide/128.png)

The options available in this screen allow the administrator user to manage the schedulers which collect data for the Whiteboard report and for the Patients Pending Bed Placement list.

In the Whiteboard report area, the Current Scheduler field will display the name of the scheduler that is currently used to collect data for the Whiteboard report. To select another scheduler, use the arrow button for the Add/Update Scheduler field to display the available schedulers, select the one you want to use and press the Save Scheduler button.

In the Patients Pending Bed Placement list area the Current Scheduler field will display the name of the scheduler that is currently used to generate the local Facility Patients Pending Bed Placement List entries for the VistA Scheduled Admissions due for the current day. To select a new scheduler, use the arrow button of the Add/Update Scheduler drop down to display the available schedulers. Select the one you want to use and click the Save Scheduler button. Under normal circumstances this is only scheduled to run once a day in the morning.

If your facility does not want VistA Scheduled Admissions automatically added to the Facility Patients Pending Bed Placement list, use the arrow button of the Add/Update Scheduler drop down and select “Delete Scheduler”, and click the Save Scheduler button.

<span id="_Toc51236004" class="anchor"></span>Figure 104 - Facility Background Processors

![](bed-management-solution-version-5-0-admin-guide/129.png)

### Patient Waiting Areas Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the facility home page, click the Site Options button.

<span id="_Toc52889645" class="anchor"></span>Figure 105 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/130.png)

The Patient Waiting Areas page is displayed using the link below:

<span id="_Toc52889646" class="anchor"></span>Figure 106 - Selecting Waiting Area Add/Delete

![](bed-management-solution-version-5-0-admin-guide/131.png)

Select the Waiting Area Add/Delete link to display the Patient Waiting Areas page as in the following image:

<span id="_Toc51236007" class="anchor"></span>Figure 107 - Patient Waiting Areas

![](bed-management-solution-version-5-0-admin-guide/132.png)

This is where you will add the locations for patients pending bed placement. You may decide to list only outside facilities. Some sites have chosen to list internal areas like the Emergency Room, Recovery or Procedure Area, and Clinic.

The options in the upper part of the screen allow the administrator user to define/add a new waiting area in the system and to decide whether the patients waiting in the new area will appear in the national list of patients pending bed placement (the National option top center of the page). Non-editable waiting areas will be pre-defined for national tracking.

The list in the lower part of the screen presents the waiting areas already defined in the system. The links Edit and Delete to the left of each entry in the list allow the administrator user to modify the name of the selected waiting area or to delete the entry from the system.

To go back to the Bed Board Site Configuration page, click the link Return to the Admin Main Page in the upper left corner of the page.

#### Adding a Waiting Area

To add a waiting area, follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc51236008" class="anchor"></span>Figure 108 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/133.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc205379896" class="anchor"></span>Figure 109 - Selecting Waiting Area Add/Delete

![](bed-management-solution-version-5-0-admin-guide/134.png)

Select the Waiting Area Add/Edit link to display the Patient Waiting Areas screen as in the following image:

<span id="_Toc52889650" class="anchor"></span>Figure 110 - Adding a Waiting Area

![](bed-management-solution-version-5-0-admin-guide/135.png)

In the Text field from the ADD Area enter the name of the new waiting area then press the Add button. A confirmation message is displayed, and the newly added waiting area is displayed in the Current Waiting Areas list.

<span id="_Toc51236011" class="anchor"></span>Figure 111 - Waiting Area Added to the List

![](bed-management-solution-version-5-0-admin-guide/136.png)

#### Editing a Waiting Area

To edit the name of an existing waiting area*,* follow the instructions below. From the facility home page, click the Site Options button.

<span id="_Toc52889652" class="anchor"></span>Figure 112 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/137.png)

The Bed Board Site Configuration page is displayed as in the image below.

<span id="_Toc52889653" class="anchor"></span>Figure 113 - Selecting Waiting Area Add/Delete

![](bed-management-solution-version-5-0-admin-guide/138.png)

Select the Waiting Area Add/Delete link to display the Patient Waiting Areas page as in the following image:

<span id="_Toc51236014" class="anchor"></span>Figure 114 - Selecting Waiting Area for Edit

![](bed-management-solution-version-5-0-admin-guide/139.png)

Selecting the Edit link will display the Waiting Areas edit page as in the following image:

<span id="_Toc51236015" class="anchor"></span>Figure 115 - Edit Waiting Area Name

![](bed-management-solution-version-5-0-admin-guide/140.png)

In the CHANGE TO: field, enter the new name for the waiting area then press the Submit button. A confirmation message will be displayed and the waiting area with the new name will be displayed in the Current Waiting Areas list.

<span id="_Toc51236016" class="anchor"></span>Figure 116 - Waiting Area Edited

![](bed-management-solution-version-5-0-admin-guide/141.png)

#### Deleting a Waiting Area

To delete a waiting area defined for the current facility, follow the instructions below.

From the facility home page, click the Site Options button.

<span id="_Toc52889657" class="anchor"></span>Figure 117 - Selecting Site Options

![](bed-management-solution-version-5-0-admin-guide/142.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51236018" class="anchor"></span>Figure 118 - Selecting Waiting Area Add/Delete

![](bed-management-solution-version-5-0-admin-guide/143.png)

Select the Waiting Area Add/Delete link to display the page as in the following image:

<span id="_Toc52889659" class="anchor"></span>Figure 119 - Select a Waiting Area for Deletion

![](bed-management-solution-version-5-0-admin-guide/144.png)

Click the Delete link associated to the waiting area that you want to delete. A confirmation screen is displayed as in the following image:

<span id="_Toc51236020" class="anchor"></span>Figure 120 - Deleting a Waiting Area

![](bed-management-solution-version-5-0-admin-guide/145.png)

Click the Delete Record button to delete the waiting area from the list.

### Icon Usage Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Icon Usage Report presents information about any and all modifications users have made for Icon Assignments. This report provides a drill down capability of seeing overall icon usage as well as individual bed or patient record assignments.

From the facility home page, click the Site Options button.

<span id="_Toc52889661" class="anchor"></span>Figure 121 - Facility Home Page - Site Options

![](bed-management-solution-version-5-0-admin-guide/146.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc52889662" class="anchor"></span>Figure 122 - Selecting Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/147.png)

Select the Icon Usage Report link to display the Icon Usage Report page as in the following image:

<span id="_Toc52889663" class="anchor"></span>Figure 123 - Icon Usage Report Parameters

![](bed-management-solution-version-5-0-admin-guide/148.png)

Select the Region, VISN and Site and press the View Report button. The image below presents an example of the Icon Usage Report.

<span id="_Toc52889664" class="anchor"></span>Figure 124 - Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/149.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc52890025" class="anchor"></span>Table 12 - Icon Usage Report Parameters

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>COLUMN</th>
<th>DESCRIPTION</th>
</tr>
<tr class="odd">
<th>Site Name</th>
<th>The Facility in which the Icon assignment was made.</th>
</tr>
<tr class="header">
<th>Icon Image</th>
<th>The Icon’s graphical representation.</th>
</tr>
<tr class="odd">
<th>Icon Name</th>
<th>The Name of the Icon, with a drill-down selection represented as “+/-“ indicating collapse/expand.</th>
</tr>
<tr class="header">
<th>Facility Active (Y/N)</th>
<th>Indication of whether the facility is active or not.</th>
</tr>
<tr class="odd">
<th>Associated with a Patient Record (Y/N)?</th>
<th>Indication and (count) of whether the Icon Update is associated with a patient record.</th>
</tr>
<tr class="header">
<th>Associated with a Bed Record (Y/N)?</th>
<th>Indication and (count) of whether the Icon Update is associated with a bed record.</th>
</tr>
<tr class="odd">
<th><blockquote>
<p><strong>Sub Headers</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>These column headers display in bold when an icon audit record is expanded</strong></p>
</blockquote></th>
</tr>
<tr class="header">
<th>Patient/Bed Record</th>
<th>Patient/Bed Record indicator</th>
</tr>
<tr class="odd">
<th>Ward</th>
<th>Ward name</th>
</tr>
<tr class="header">
<th>Bed</th>
<th>Bed Name/number</th>
</tr>
<tr class="odd">
<th>Patient</th>
<th>Patient First Initial, LastName, “-“, and last 4 of SSN</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### Bed Management Board Icons Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Bed Board Site Configuration page, click the BMS Icon Legend link to display the following page:

<span id="_Toc205379912" class="anchor"></span>Figure 125 - BMS Bed Board Site Configuration BMS Icon Legend Screen

![](bed-management-solution-version-5-0-admin-guide/150.png)

<span id="_Toc52889666" class="anchor"></span>Figure 126 - Bed Management Board Icon Legend Page

![](bed-management-solution-version-5-0-admin-guide/151.png)

The page presents the icons that can be used throughout the application, their corresponding significance and the application element to which they can be attached (patient, room/bed).

The icons are grouped according to the area of the application where they are likely to be used and the type of information they convey: Application Icons (System and Bed Cleaning Status), Ward Whiteboard Status Icons (Standard and Emergency Management) and Site Configurable Icons.

### Audit Log Report Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Bed Board Site Configuration page, click the Audit Log Report link to display the following page.<span id="_Toc52889667" class="anchor"></span>

Figure 127 - BMS Bed Board Site Configuration / View Audit Log Screen

![](bed-management-solution-version-5-0-admin-guide/152.png)

<span id="_Toc51236028" class="anchor"></span>Figure 128 - Audit Log Report

![](bed-management-solution-version-5-0-admin-guide/153.png)

The Audit Log reports present information about what users have performed what actions in different areas of the application (such as icons, pending bed placements, staff assignment or whiteboard usage). See the following sections for details on each report.

#### Site Configurable Icons Report

The Site Configurable Icons Report presents information about the usage of the site configurable icons within the system.

In the Audit Log Report page use the Select Report field to select the Site Icons report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of a Site Configurable Icons Report:

<span id="_Toc205379916" class="anchor"></span>Figure 129 - Site Configurable Icons Report

![](bed-management-solution-version-5-0-admin-guide/154.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_bookmark178" class="anchor"></span>Table 13 - Site Configurable Icons Report Parameters

| Column                   | Description                                                                                 |
|--------------------------|---------------------------------------------------------------------------------------------|
| Icon Category            | The type of icon: can only be Site Configurable Icon.                                       |
| Facility                 | The name of the facility for which the icon has been configured and used.                   |
| (Icon image)             | The icon image.                                                                             |
| Image Name               | The name of the image entered in the Image Name field in the Edit Icon page.                |
| Icon Name                | The name assigned to the icon.                                                              |
| Active                   | If the icon is active.                                                                      |
| Published                | If the icon has been published.                                                             |
| Type: Patient or RoomBed | If the icon is used to flag a patient or a room or a bed.                                   |
| Description              | The description of the icon as entered in the Icon Description field in the Edit Icon page. |
| Comment                  | Any comment entered in the Comments field in the Edit Icon page.                            |
| Mouse Over Text          | The text entered in the Mouse Over Text field in the Edit Icon page.                        |
| Created By               | The name of the user who performed the current operation on the icon.                       |
| Date                     | The date and time when the current operation has been performed on the icon.                |
| Event Type               | The type of operation that has been performed on the icon.                                  |

#### Facility Patient Pending Bed Placement List Report

The Facility Patient Pending Bed Placement List Report presents information about what users have performed what actions on a facility pending bed placement list.

In the Audit Log Report page use the Select Report field to select the Facility Pending Bed Placement List report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of a Facility Patient Pending Bed Placement List Report:

<span id="_Toc51236030" class="anchor"></span>Figure 130 - Facility Patient Pending Bed Placement List Report

![](bed-management-solution-version-5-0-admin-guide/155.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_bookmark180" class="anchor"></span>Table 14 - Facility Patient Pending Bed Placement List Report Parameters

| COLUMN           | DESCRIPTION                                                       |
|------------------|-------------------------------------------------------------------|
| Facility         | The name of the VA facility.                                      |
| Patient          | The code of the patient.                                          |
| Problem          | The problem for which the patient needed treatment.               |
| Bed              | The bed assigned to the patient.                                  |
| Req Bed Date     | The date when the bed was requested for the patient.              |
| Type of Bed Ward | The type of bed/ward requested for the patient.                   |
| Waiting Area     | The waiting area where the patient has been placed.               |
| Fee Disposition  | The fee disposition associated to the patient.                    |
| Contract Fee     | The contract fee.                                                 |
| Auth. Fee        | The authorization to use the fee.                                 |
| Serv. Rec.       | The type of service requested according to the patient’s problem. |
| Reason           | The reason for using the fee.                                     |
| Comments         | Any comments entered in the Comments field.                       |
| Created by       | The user who created the event.                                   |
| Date             | The date and time when the event was created.                     |
| Event Type       | The type of event.                                                |

#### VISN Patient Pending Bed Placement List Report

The VISN Patient Pending Bed Placement List Report presents information about what users have performed what actions on a VISN pending bed placement list.

In the Audit Log Report page use the Select Report field to select the VISN Patient Pending Bed Placement List report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of a VISN Patient Pending Bed Placement List Report.

<span id="_Toc52889671" class="anchor"></span>Figure 131 - VISN Patient Pending Bed Placement List Report

![](bed-management-solution-version-5-0-admin-guide/156.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_bookmark182" class="anchor"></span>Table 15 - VISN Patient Pending Bed Placement List Report Parameters

| COLUMN             | DESCRIPTION                                                                         |
|--------------------|-------------------------------------------------------------------------------------|
| Facility           | The name of the VA facility.                                                        |
| VISN               | The VISN where the VA facility is located.                                          |
| Patient            | The code of the patient.                                                            |
| ERA                | The period of service that the patient served.                                      |
| Contract           | Whether or not the VA facility has a contract with the selected community hospital. |
| Diagnosis          | The diagnosis for which the patient requests admission to the community hospital.   |
| Current location   | The name of the community hospital where the patient is currently being treated.    |
| Location Adm. Date | The date when the patient has been admitted in the selected location.               |
| Comments           | Any comments entered in the Comments field.                                         |
| Specialty          | The treating specialty corresponding to the type of need.                           |
| Req. Adm. Date     | The date when the patient should be able to be admitted to the VA facility.         |
| Created by         | The name of the user who created the event.                                         |
| Date               | The date and time when the event has been created.                                  |
| Event Type         | The type of the event.                                                              |

#### Staff Assignment Report

The Staff Assignment Report presents information about what users have assigned staff personnel to the beds in the wards of a facility.

In the Audit Log Report page use the Select Report field to select the Staff Assignment report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of a Staff Assignment Report.

<span id="_Hlk64277562" class="anchor"></span>Figure 132 - Staff Assignment Report

![](bed-management-solution-version-5-0-admin-guide/157.png)

For each entry the following data is available:

<span id="_Toc471462840" class="anchor"></span>Table 16 - Staff Assignment Report Parameters

| COLUMN     | DESCRIPTION                                        |
|------------|----------------------------------------------------|
| Ward       | The ward where the bed is.                         |
| Bed        | The code of the bed.                               |
| Staff      | The name of the person assigned to the bed.        |
| Patient    | The code of the patient occupying the bed.         |
| Created by | The name of the user who created the event.        |
| Date       | The date and time when the event has been created. |
| Event Type | The type of the event.                             |

#### Bed History Report

The Bed History Report presents information about what users have performed what actions on a bed.

In the Audit Log Report page use the Select Report field to select the Bed History Report, then Region, VISN,Site, and then select From Date/To Date determine the time interval for the report and press the View Report button. The image below presents an example of a Bed History Report.

<span id="_Toc205379920" class="anchor"></span>Figure 133 - Bed History Report

![](bed-management-solution-version-5-0-admin-guide/158.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc205380077" class="anchor"></span>Table 17 - Bed History Report Parameters

| COLUMN         | DESCRIPTION                                 |
|----------------|---------------------------------------------|
| Bed Name       | The bed number.                             |
| Edited Date    | The date and time the bed was edited.       |
| Reason         | The reason the bed is being edited.         |
| Type           | The type of edit reason.                    |
| Edited By      | The name of the user editing the bed.       |
| Cleared By     | The name of the user who cleared the edits. |
| Completed Date | The date the bed was cleared of all edits.  |

#### PPBP Usage (VISN) Report

The PPBP Usage (VISN) Report presents information about any and all modifications users have made from the Patient Pending Bed Placement (PPBP) view.

In the Audit Log Report page use the Select Report field to select the PPBP Usage (VISN) report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of the PPBP Usage (VISN) Report.

<span id="_Toc52889673" class="anchor"></span>Figure 134 - PPBP Usage (VISN) Report

![](bed-management-solution-version-5-0-admin-guide/159.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc471462842" class="anchor"></span>Table 18 - PPBP Usage (VISN) Report Parameters

| COLUMN               | DESCRIPTION                                                                           |
|----------------------|---------------------------------------------------------------------------------------|
| Entered D/T          | The Date/Time of the modification to the Whiteboard.                                  |
| Requested D/T        | The Date/Time the placement on the board was requested.                               |
| Removed D/T          | The Date/Time the entry was removed.                                                  |
| Edit Event D/T       | The Date/Time the event was deleted.                                                  |
| User                 | The BMS User who made the modification.                                               |
| Patient Name         | The patient’s last name and last 4 digits of the SSN.                                 |
| Transaction          | The type of operation performed on the record, such as Update, New Record, or Delete. |
| Transaction Updates  | The updates made to the Whiteboard, not including comments                            |
| Transaction Comments | Any comments made for the transaction performed by the user.                          |

#### PPBP Usage (Facility) Report

The PPBP Usage (Facility) Report presents information about any and all modifications users have made from the Patient Pending Bed Placement (PPBP) view.

In the Audit Log Report page use the Select Report field to select the Whiteboard Usage report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of the PPBP Usage (Facility) Report:

<span id="_Toc51236034" class="anchor"></span>![](bed-management-solution-version-5-0-admin-guide/160.png)Figure 135 - PPBP Usage (Facility) Report

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc471462843" class="anchor"></span>Table 19 - PPBP Usage (Facility) Report Parameters

| COLUMN               | DESCRIPTION                                                                           |
|----------------------|---------------------------------------------------------------------------------------|
| Entered D/T          | The Date/Time of the modification to the Whiteboard.                                  |
| Requested D/T        | The Date/Time the placement on the board was requested.                               |
| Removed D/T          | The Date/Time the entry was removed.                                                  |
| Edit Event D/T       | The Date/Time the event was deleted.                                                  |
| User                 | The BMS User who made the modification.                                               |
| Patient Name         | The patient’s last name and last 4 digits of the SSN.                                 |
| Transaction          | The type of operation performed on the record, such as Update, New Record, or Delete. |
| Transaction Updates  | The updates made to the Whiteboard, not including comments.                           |
| Transaction Comments | Any comments made for the transaction performed by the user.                          |

#### Whiteboard Patient Icon Usage Report

The Whiteboard Patient Icon Usage Report presents information about modifications users have made to patients from the whiteboard.

In the Audit Log Report page use the Select Report field to select the Whiteboard Patient Icon Usage report, then select the Region, VISN and Site, then the From Date/To Date to determine the time interval for the report and press the View Report button.

<span id="_Toc52889675" class="anchor"></span>Figure 136 - Selecting Whiteboard Patient Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/161.png)

The image below presents an example of the Whiteboard Patient Icon Usage Report:

<span id="_Toc49154693" class="anchor"></span>Figure 137 - Whiteboard Patient Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/162.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

| COLUMN              | DESCRIPTION                                                                           |
|---------------------|---------------------------------------------------------------------------------------|
| Entered D/T         | The Date/Time the entry was created.                                                  |
| User                | The BMS User who made the entry.                                                      |
| Bed                 | The bed assigned to the patient.                                                      |
| Patient Name        | The last name, first name and last 4 digits of the patient’s SSN.                     |
| Transaction         | The type of operation performed on the record, such as Update, New Record, or Delete. |
| Transaction Updates | Any updates made for the transaction performed by the user.                           |

#### Whiteboard Bed Icon Usage Report

The Whiteboard Bed Icon Usage Report presents information about modifications users have made to icons from the whiteboard.

In the Audit Log Report page use the Select Report field to select the Whiteboard Bed Icon Usage report, then select the Region, VISN and Site, then the From Date/To Date to determine the time interval for the report and press the View Report button.

<span id="_Toc52889677" class="anchor"></span>Figure 138 - Selecting Whiteboard Bed Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/163.png)

The image below presents an example of the Whiteboard Bed Icon Usage Report:

<span id="_Toc52889678" class="anchor"></span>Figure 139 - Whiteboard Bed Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/164.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc52890033" class="anchor"></span>Table 21 - Whiteboard Bed Icon Usage Report Parameters

| COLUMN              | DESCRIPTION                                                                            |
|---------------------|----------------------------------------------------------------------------------------|
| Entered D/T         | The Date/Time the entry was created.                                                   |
| User                | The BMS User who made the entry.                                                       |
| Bed                 | The bed assigned to the patient.                                                       |
| Transaction         | The type of operation performed on the record, such as Update, New Record, or Deleted. |
| Transaction Updates | Any updates made for the transaction performed by the user.                            |

#### Whiteboard Comments Usage Report

The Whiteboard Comments Usage Report presents information about any and all modifications users have made from the whiteboard.

In the Audit Log Report page use the Select Report field to select the Whiteboard Comments Usage report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of the Whiteboard Usage Report:

<span id="_Ref52781303" class="anchor"></span>Figure 140 - Whiteboard Comments Usage Report

![](bed-management-solution-version-5-0-admin-guide/165.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

| COLUMN               | DESCRIPTION                                                                                                                       |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Created D/T          | The Date/Time the comment was created.                                                                                            |
| Created by User      | The BMS User who created the comment.                                                                                             |
| Edited D/T           | The Date/Time of the modification to the Whiteboard.                                                                              |
| Edited by User       | The BMS User who made the modification.                                                                                           |
| Update Type          | The type of update made to the Whiteboard, such as Bed Reason Comment, Bed Unavailable, Icon Assignment, or Bed Staff Assignment. |
| Bed                  | The bed record affected by the modification.                                                                                      |
| Transaction          | The type of operation performed on the record, such as Update, New Record, or Delete.                                             |
| Transaction Comments | Any comments made for the transaction performed by the user.                                                                      |

### Contingency Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Contingency Settings page allows the user to set up a network storage area to backup an image of the current Ward Whiteboard for BMS contingency planning.

From the facility home page, click the Site Options button.

<span id="_Toc51236035" class="anchor"></span>Figure 141 - Facility Home Page Site Options

![](bed-management-solution-version-5-0-admin-guide/166.png)

The Bed Board Site Configuration page is displayed as in the image below:

<span id="_Toc51236036" class="anchor"></span>Figure 142 - Bed Board Site Configuration Page Contingency Settings

![](bed-management-solution-version-5-0-admin-guide/167.png)

Select the Contingency Settings link to display the page as in the following image:

<span id="_Toc52889682" class="anchor"></span>Figure 143 - Contingency Settings Page

![](bed-management-solution-version-5-0-admin-guide/168.png)

A list of wards defined for the current facility is displayed. Enter the path for the Whiteboard Report then press the Save button.

![](bed-management-solution-version-5-0-admin-guide/169.png)Note: If a ward selected for the Whiteboard Contingency Report has any of the following special characters, then these special characters will be replaced with a “\_” in the saved file : ( / \\ : \* ? " \< \> \| )

![](bed-management-solution-version-5-0-admin-guide/170.png) Note: The Whiteboard Report Path must be a valid network share with the correct rights/permissions assigned. If you have questions, contact your local facility IS administrator for help. For detailed instructions on setting up a shared network storage area, see the BMS Technical Manual (WHITEBOARD SNAPSHOT CONFIGURATION section).

### Evacuation On/Off

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Bed Board Site Configuration page, the option Evacuation On/Off is available as in the following image:

<span id="_Toc52889683" class="anchor"></span>Figure 144 - Evacuation On/Off

![](bed-management-solution-version-5-0-admin-guide/171.png)

In case of emergency the user can set the Evacuation option to ON. This will cause the facility home page to be displayed as in the following image:

<span id="_Toc51236039" class="anchor"></span>Figure 145 - Facility Home Page - Evacuation On

![](bed-management-solution-version-5-0-admin-guide/172.png)

All the patients admitted in the current facility and for whom the Evacuation Patient option has been selected will be placed in the Pending Bed Placement List.

### Reset SUMMARY Report Out-Of-Service/Do-Not-Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within the Bed Board Site Configuration page, the Reset SUMMARY Report Out-Of-Service/Do-Not-Display option lets the site admin clear the Reason and Comments fields of either Unavailable/Out Of Service or Do Not Display beds.

<span id="_Toc205379933" class="anchor"></span>Figure 146 - Reset SUMMARY Report Out-Of-Service/Do-Not-Display

![](bed-management-solution-version-5-0-admin-guide/173.png)

In the example above, any out of service beds in ward MED_SURG have had their Reason and Comments fields cleared, and have been returned to service.

<span id="_Toc205379934" class="anchor"></span>Figure 147 - Facility Home Page – Beds Back in Service

![](bed-management-solution-version-5-0-admin-guide/174.png)

![](bed-management-solution-version-5-0-admin-guide/175.png)The next ADT job will clear the visual elements from the whiteboard.

<span id="_Toc205379935" class="anchor"></span>Figure 148 - Cleared Reason and Comments fields for bed back in service

![](bed-management-solution-version-5-0-admin-guide/176.png)

### Community Care Sites 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Community Care Sites Configuration page allows the admin user to set up a VAMC-specific list of nearby non-VA facilities commonly used by veterans in the community. This list of “favorite” community facilities is seen by BMS site users when designating a patient on the PPBPL as a Community Care Patient (that is, “Did the transfer request or completed transfer originate from the community?” value of ‘Yes’), or by Community Care Users when working with Community Care Tracking List records.

![](bed-management-solution-version-5-0-admin-guide/177.png) For more information refer to the Bed Management Solution (BMS) Community Care Tracking List User Guide.

From the Bed Board Site Configuration page, locate the Community Care Sites link:

<span id="_Toc205379936" class="anchor"></span>Figure 149 - Community Care Sites link

![](bed-management-solution-version-5-0-admin-guide/178.png)

Select the Community Care Sites link to display the page as in the following image:

<span id="_Toc205379937" class="anchor"></span>Figure 150 - Community Care Sites page

![](bed-management-solution-version-5-0-admin-guide/179.png)

#### Adding Community Care Site Favorites 

To add or update the drop-down list of community facilities users see when adding patients to this facility’s Patient Pending Bed Placement List (PPBPL) or Community Care Tracking List (CCTL), click in the Type to search field underneath the Community Care Sites header. Then type a Facility Name, Address, City, State or ZIP code number which brings back search results immediately.

![](bed-management-solution-version-5-0-admin-guide/180.png)Search results are based on a 300 mile radius of the VAMC’s physical address—note that multiple VAMCs can have access to the same community facility record based on overlapping radii.

![](bed-management-solution-version-5-0-admin-guide/181.png)Your search term must be at least 2 characters in length. There is also a limit of 200 results per search. National Provider Identifier (NPI) is not searchable.

<span id="_Toc205379938" class="anchor"></span>Figure 151 - Community Care Sites page search

![](bed-management-solution-version-5-0-admin-guide/182.png)

When you find the relevant facility from the search results, select the Add link:

<span id="_Toc205379939" class="anchor"></span>Figure 152 - Community Care Sites Add Link

![](bed-management-solution-version-5-0-admin-guide/183.png)

<span id="_Toc205379940" class="anchor"></span>Figure 153 - Community Care Sites favorite addition

![](bed-management-solution-version-5-0-admin-guide/184.png)

BMS users adding or editing patients on the facility Patient Pending Bed Placement List (PPBPL), or on the facility Community Care Tracking List (CCTL), will immediately see this Community Care facility within the Community Care Facility drop-down menu:

<span id="_Toc205379941" class="anchor"></span>Figure 154 - PPBPL Community Care Facility Menu new favorite

![](bed-management-solution-version-5-0-admin-guide/185.png)

#### Removing Community Care Site Favorites

To remove one or more Community Care facilities from the ‘Community Care Facility’ drop-down menu, click the Remove link within the Community Care Site Favorites For *VAMC* table.

<span id="_Toc205379942" class="anchor"></span>Figure 155 - Community Care Sites Configuration favorite removal

![](bed-management-solution-version-5-0-admin-guide/186.png)

![](bed-management-solution-version-5-0-admin-guide/187.png) Note that ‘TBD’ will always appear within the Community Care Site Favorites list. This is the default Community Care Facility value when adding someone to the Community Care Tracking List.

As with adding community facilities to a VAMC’s favorites list, removing one or more Community facilities from the favorites list is seen immediately by your users.

<span id="_Toc205379943" class="anchor"></span>Figure 156 - PPBPL Community Care Facility Menu removed favorites

![](bed-management-solution-version-5-0-admin-guide/188.png)

Note that within the PPBPL or CCTL Community Care Facility field, your users are also able to search the database directly, should the community facility in question not be listed as a “favorite”. To search for nearby community care facilities you wish to apply to your PPBPL or CCTL patient record, select the “…” option:

<span id="_Toc205379944" class="anchor"></span>Figure 157 - PPBPL Community Care Facility Menu search option

![](bed-management-solution-version-5-0-admin-guide/189.png)

Once the user selects the ‘…’ option, a new Community Care Facility Search window appears:

<span id="_Toc205379945" class="anchor"></span>Figure 158 - PPBPL Community Care Facility Search

![](bed-management-solution-version-5-0-admin-guide/190.png)

Similar to the Community Care Sites Configuration screen, click in the search bar underneath the Community Care Facility Search header. Then type a Facility Name, Address, City, State or ZIP code number for your search of community facilities within a 300 mile radius of the VAMC. Note that your search term must be at least 2 characters in length. There is also a limit of 200 results per search; National Provider Identifier (NPI) is not searchable.

<span id="_Toc205379946" class="anchor"></span>Figure 159 - PPBPL Community Care Facility Search results

![](bed-management-solution-version-5-0-admin-guide/191.png)

Use the scroll bar if necessary to find the facility in question, then select the record and press the Confirm Selection button.

<span id="_Toc205379947" class="anchor"></span>Figure 160 - PPBPL Community Care Facility Search selection

![](bed-management-solution-version-5-0-admin-guide/192.png)

Once the selection is confirmed, the PPBPL record’s Community Care Facility field is populated with the facility in question.

<span id="_Toc205379948" class="anchor"></span>Figure 161 - PPBPL Community Care Facility value

![](bed-management-solution-version-5-0-admin-guide/193.png)

#### Adding Community Care Facilities Manually

Within the Community Care Sites Configuration screen, it is also possible for an Admin User role or higher to add new community facility records *manually*, should your site users not be able to find a specific community facility. To do this, you will need to use the Add Facility link from the Community Care Sites Configuration screen:

From the Community Care Sites Configuration page, select the Add Facility link to display the page in the following image:

<span id="_Toc205379949" class="anchor"></span>Figure 162 - Community Care Sites Configuration Add Facility link

![](bed-management-solution-version-5-0-admin-guide/194.png)

Upon selecting the Add Facility link an Add Edit Community Care Site for VAMC screen will appear. Each of the fields is required prior to saving the new community facility record:

<span id="_Toc205379950" class="anchor"></span>Figure 163 - Add Edit Community Care Site for VAMC new facility creation

![](bed-management-solution-version-5-0-admin-guide/195.png)

![](bed-management-solution-version-5-0-admin-guide/196.png) If the National Provider Identifier of the facility is unknown, use “0”.

If the NPI entered is already in use, when pressing Save there will display a list of duplicate NPI results. This Matching Facilities for NPI list reveals any related Community Care facility records which can help prevent duplicate records. Press the Save Anyway button to continue creating a Community Care facility with a non-unique NPI.

<span id="_Toc205379951" class="anchor"></span>Figure 164 - Add Edit Community Care Site Matching Facilities for NPI

![](bed-management-solution-version-5-0-admin-guide/197.png)

![](bed-management-solution-version-5-0-admin-guide/198.png)Editing an existing CC Facility requires two or more facilities with the same NPI, for matching results to be returned.

Pressing the Save (or Save Anyway) button will not only add the new community facility record to the database, but also automatically apply the facility record to the “favorites” list:

<span id="_Toc205379952" class="anchor"></span>Figure 165 - Community Care Sites Configuration new facility record

![](bed-management-solution-version-5-0-admin-guide/199.png)

![](bed-management-solution-version-5-0-admin-guide/200.png)Note that a newly added community facility record is only seen by your VAMC’s site users. If another VAMC needs this same facility record, a VAMC admin user for that VA facility (or a user with a higher-level Support or National role) would need to follow the above steps to create the same community facility for this other VAMC.

#### Editing and Removing Community Care Facilities Manually

Admin users can also edit and delete (literally, “inactivate”) Community Care Facility records from the database, using the Edit and Delete links respectively. Because a community facility might be needed by another VAMC (delivered Community Care Facilities are often shared between nearby VAMCs), BMS will allow for VAMC-specific deletions of delivered community facility records, as well as the ability to reactivate facilities using a report.

![](bed-management-solution-version-5-0-admin-guide/201.png)Deleted Community Care facility records can be reactivated using the Facilities to Reactivate report, located within the Community Care Tracking List. For more information, refer to the BMS Community Care Tracking List guide.

To edit a community facility record directly, select the Edit link.

<span id="_Toc205379953" class="anchor"></span>Figure 166 - Community Care Sites Configuration Edit option

![](bed-management-solution-version-5-0-admin-guide/202.png)

Make any necessary changes to Facility Name, Address, City, State, Postal (ZIP) Code or National Provider Identifier (NPI), then press Save.

<span id="_Toc205379954" class="anchor"></span>Figure 167 - Add Edit Community Care Site for VAMC facility edit

![](bed-management-solution-version-5-0-admin-guide/203.png)

![](bed-management-solution-version-5-0-admin-guide/204.png) If editing a delivered community facility record, the original facility record will get reimported to BMS the next time the PPMS job runs. See the Background Processors section of this guide for more information.

To delete a community facility record, select the Delete link:

<span id="_Toc205379955" class="anchor"></span>Figure 168 - Community Care Sites Configuration facility record removal

![](bed-management-solution-version-5-0-admin-guide/205.png)

![](bed-management-solution-version-5-0-admin-guide/206.png)Deleting a facility record will “inactivate” the record so that it isn’t searchable from the Community Care Sites page or the Community Care Facility field; however, specific PPBPL or CCTL records tied to the deleted community care facility will continue to display the deleted facility in question.

When deleting a facility record, you will first see a prompt to delete the record only for your VAMC.

<span id="_Toc205379956" class="anchor"></span>Figure 169 - Community Care Sites Configuration Delete for current VAMC button

![](bed-management-solution-version-5-0-admin-guide/207.png)

![](bed-management-solution-version-5-0-admin-guide/208.png)Only logins with the National User or Support User role will be able to use the Delete for all VAMCs button.

After choosing the Delete for current VAMC button, you will see a confirmation prompt prior to deletion. Press the OK button if you are sure you wish to inactivate the community facility record within the database.

<span id="_Toc205379957" class="anchor"></span>Figure 170 - Community Care Sites Configuration facility record deletion confirmation

![](bed-management-solution-version-5-0-admin-guide/209.png)

| COLUMN        | DESCRIPTION                                                        |
|---------------|--------------------------------------------------------------------|
| Facility Name | The name of the community facility.                                |
| Address       | The physical address of the community facility.                    |
| City          | The city where the community facility is located.                  |
| State         | The state where the community facility is located.                 |
| Postal Code   | The zip code of the community facility.                            |
| NPI           | The National Provider Identifier number of the community facility. |

### Bed Level Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bed Management Solution (BMS) now includes a bed type update tool within the BMS application itself. This Bed Level Management screen uses facility-based Ward Group searching to display individual beds editable one-by-one or in batch.

<span id="_Toc200036101" class="anchor"></span>Figure 171 - Bed Level Management - Main Screen

![](bed-management-solution-version-5-0-admin-guide/210.png)

![](bed-management-solution-version-5-0-admin-guide/211.png) For more information on using Bed Level Management, refer to the Bed Management Solution (BMS) Bed Level Management User Guide.

<span id="_Toc205379959" class="anchor"></span>Figure 172 - Bed Level Management Link

![](bed-management-solution-version-5-0-admin-guide/212.png)

![](bed-management-solution-version-5-0-admin-guide/213.png) For more information on configuring Bed Levels used within the BLM interface, refer to the National Bed Tracking Levels section of this admin guide.

## Support Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The support users can access the following pages:

- Administration Section page
- Maintain Marquee Text page
- Add/Edit BMS User page
- Edit BMS Facility Settings page
- Edit Sister Sites page
- Add/Edit Icon page
- View Audit Log page
- Treating Specialty/NUMA/HAvBED Edit page
- National Waiting Area page
- National Unavailable Reason page
- Background Processors page
- User Access Report
- National Bed Tracking Levels page

### Log in to the Administration Section Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After logging in the BMS solution use the links Return to VISN Network and Return to Regional Page (in the upper left corner of the page) to display the National/Regional page as in the following image:

<span id="_Toc52889867" class="anchor"></span>Figure 173 - Accessing Administration Section Page from National/Regional page

![](bed-management-solution-version-5-0-admin-guide/214.png)

Click the BMS Admin link to access the Administration Section as in the following image:

<span id="_Toc51236178" class="anchor"></span>Figure 174 - Administration Section Page

![](bed-management-solution-version-5-0-admin-guide/215.png)

### Maintain Marquee Text Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the main Administration section page, click the Maintain Marquee Text link to access the page as in the following image:

<span id="_Toc51236179" class="anchor"></span>Figure 175 - Add/ Edit Marquee Text

![](bed-management-solution-version-5-0-admin-guide/216.png)

BMS Allows you to maintain 5 different marquee messages. The current marquee text in use is selected by clicking the radio button next to the message text box. Enter the text in any of these 5 fields, select the appropriate marquee message, then press the Submit button. You can change this text at any time according to the organization needs.

### Add/Edit BMS User Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the main Administration section page, click the Add/Edit BMS User link to access the page as in the following image:

<span id="_Toc51236180" class="anchor"></span>Figure 176 - Administration Section – User Add/Edit Page

![](bed-management-solution-version-5-0-admin-guide/217.png)

In this page the system administrator can add a new user to the list of users who have access to a certain site. Also the administrator can edit the rights granted to an existing user.

#### Adding a User

To add a single user or to Bulk Activate users at one of the existing facility sites, in the Administration Section – User Add/Edit page click the button Select Existing NT User Name (the user must have an account in VA’s Active Directory). Click this button to display the following screen:

<span id="_Ref47956962" class="anchor"></span>Figure 177 - Select User to Activate

![](bed-management-solution-version-5-0-admin-guide/218.png)

From the Local field select the domain to which the user currently belongs. Enter part of the name of the user in the User Name field then press the Find button to locate the user.

From the list in the central part of the screen select the user(s) to whom grant access to the BMS system then press the Select button. The following screen is displayed:

<span id="_Toc52889872" class="anchor"></span>Figure 178 - Customize BMS user rights

![](bed-management-solution-version-5-0-admin-guide/219.png)

The following parameters can be set for a user of the BMS system:<span id="_bookmark380" class="anchor"></span>

Table 24 - BMS User Parameters

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>COLUMN</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NT User Name</td>
<td>NT user who will be given access rights to the BMS system.</td>
</tr>
<tr class="even">
<td>Support User?</td>
<td>If the new user will have to perform support tasks.</td>
</tr>
<tr class="odd">
<td>National User?</td>
<td>If the new user will have access to the national sites.</td>
</tr>
<tr class="even">
<td>Regional User?</td>
<td>If the new user will have access to the regional sites.</td>
</tr>
<tr class="odd">
<td>VISN User?</td>
<td>If the new user will have access to other VISN sites.</td>
</tr>
<tr class="even">
<td>Admin User?</td>
<td>If the new user will have access to the Administration section page.</td>
</tr>
<tr class="odd">
<td>Audit Log User?</td>
<td>If the new user will have access to the Audit Log function.</td>
</tr>
<tr class="even">
<td>Site User?</td>
<td>These are the facility level read and write users. This gives the user access to specific sites.</td>
</tr>
<tr class="odd">
<td>EMS User?</td>
<td>If the new user is part of EMS group.</td>
</tr>
<tr class="even">
<td>EMS Dispatcher?</td>
<td>If the new user is an EMS Dispatcher.</td>
</tr>
<tr class="odd">
<td>EMS Supervisor User?</td>
<td>If the new user has EMS supervisor rights.</td>
</tr>
<tr class="even">
<td>Community Care User?</td>
<td>If the new user will have access to the Community Care Tracking List page. ![](bed-management-solution-version-5-0-admin-guide/220.png) The Admin User role will always inherit the Community Care User role’s permissions.</td>
</tr>
<tr class="odd">
<td>Community Care Transfer User?</td>
<td><p>If the new user will have access to both the Community Care Tracking List page and the Add to PPBPL function on the CCTL. In addition, this role allows edit access to the Transfer Out Reason and Transfer Out Type fields within a Community Care Tracking List record.</p>
<p>![](bed-management-solution-version-5-0-admin-guide/221.png)The Admin User role will always inherit the Community Care Transfer User role’s permissions. In addition, the Community Care Transfer User role includes the Community Care User role permissions by default.</p></td>
</tr>
<tr class="even">
<td>Community Care Admin?</td>
<td><p>If the new user will have site favorite configuration access on the Community Care Sites page.</p>
<p>![](bed-management-solution-version-5-0-admin-guide/222.png)The Admin User role will always inherit the Community Care Admin role’s permissions.</p>
<p>![](bed-management-solution-version-5-0-admin-guide/223.png)Note: To add, edit or delete Community Care facilities from the Community Care Sites page, an Admin User role is required.</p></td>
</tr>
<tr class="odd">
<td>Guest User?</td>
<td>If the new user will only have access to the National Bed Availability report.</td>
</tr>
<tr class="even">
<td>Default Region?</td>
<td>The default region to be displayed when the new user logs into the system.</td>
</tr>
<tr class="odd">
<td>Default VISN?</td>
<td>The default VISN to be displayed when the new user logs into the system.</td>
</tr>
<tr class="even">
<td>DefaultSite</td>
<td>The default site to be displayed when the new user logs into the system.</td>
</tr>
<tr class="odd">
<td>READ Access</td>
<td>If the selected user has READ rights on the sites in the selected Region/VISN.</td>
</tr>
<tr class="even">
<td>WRITE Access</td>
<td><p>If the selected user has WRITE rights on the sites in the selected Region/VISN.</p>
<p>![](bed-management-solution-version-5-0-admin-guide/224.png)The WRITE Access role does not apply to adding, editing or removing Community Care Tracking List records.</p></td>
</tr>
<tr class="odd">
<td>Whiteboard Only Access</td>
<td>If the user only has access to view the whiteboard.</td>
</tr>
<tr class="even">
<td>Display only the facilities with permissions</td>
<td>This option is selected by default. To see all the facilities in the system de-select this checkbox.</td>
</tr>
</tbody>
</table>

The list in the lower part of the screen will be updated according to the selections made in the fields in the upper part of the screen. For example, if in the National User field you select the option *No* and from the Regional User field the option *Yes,* then the list will display only the facilities in the region selected from the field Default Region.

<span id="_Toc205379966" class="anchor"></span>Figure 179 - Region-specific facilities based on Regional User role and Default Region

![](bed-management-solution-version-5-0-admin-guide/225.png)

For each facility displayed in the list in the lower part of the screen you can define READ/WRITE/Whiteboard Only Access rights.

After setting the desired parameters for the selected user, click the Submit button to enter the data into the system.

#### Editing User Rights

To edit the rights granted to a user of a facility site in the Administration Section – User Add/Edit page, click the button Select Existing NT User Name. Clicking this button will display the following screen:

<span id="_Toc51236183" class="anchor"></span>Figure 180 - Select User

![](bed-management-solution-version-5-0-admin-guide/226.png)

From the Local field select the domain to which the user currently belongs to. Enter part of the name of the user in the User Name field then press the Find button to locate the user.

From the list in the central part of the screen select the user whose access rights you want to edit then press the Select button. The following screen is displayed:

<span id="_Toc51236184" class="anchor"></span>Figure 181 - Edit BMS user rights

![](bed-management-solution-version-5-0-admin-guide/227.png)

Make the appropriate changes then press the Submit button to enter the data into the system. See [Adding a User](#adding-a-user) for details.

#### Deleting a User

To delete the rights granted to a single user or to bulk deactivate users of a facility site, in the Administration Section – User Add/Edit page click the button Select Existing NT User Name. Clicking this button displays the following screen:

<span id="_Toc51236185" class="anchor"></span>Figure 182 - Find User Name

![](bed-management-solution-version-5-0-admin-guide/228.png)

Enter part of the name of the user in the User Name field then press the Find button to locate the user.

<span id="_Toc51236186" class="anchor"></span>Figure 183 - Select User to Delete

![](bed-management-solution-version-5-0-admin-guide/229.png)

From the list in the central part of the screen select the user whose access rights you want to delete, then press the Add/Edit Single User button. The following screen is displayed:

<span id="_Toc205379971" class="anchor"></span>Figure 184 - Customize BMS user rights

![](bed-management-solution-version-5-0-admin-guide/230.png)

Select No for all the parameters then press the Submit button.

### Edit BMS Facility Settings Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the main Administration section page, click the Edit BMS Facility Settings link to access the page as in the following image:

<span id="_Toc52889878" class="anchor"></span>Figure 185 - Edit BMS Site

![](bed-management-solution-version-5-0-admin-guide/231.png)

In this page the user can edit the settings of a BMS facility site. Select Facility Name, then click the arrow button of this field to display a list of existing facilities. The following parameters can be set for a Facility in the BMS system:

<span id="_bookmark387" class="anchor"></span>Table 25 - BMS Site Parameters

| Column                                                                 | Description                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Facility Site ID                                                       | A unique ID number assigned to each facility.                                                                                                                                                                                                               |
| Full Facility Name                                                     | The full name of the facility.                                                                                                                                                                                                                              |
| Facility Point-of-Contact:                                             | The facility point of contact, this can be the triage room, or the front desk.                                                                                                                                                                              |
| Facility POC email:                                                    | The email for the point of contact with the facility.                                                                                                                                                                                                       |
| Facility POC Telephone:                                                | The telephone of the point of contact.                                                                                                                                                                                                                      |
| Facility Address 1:                                                    | The main address of the facility.                                                                                                                                                                                                                           |
| Facility Address 2:                                                    | If applicable, any secondary address of the facility.                                                                                                                                                                                                       |
| Facility City/State/ZIP:                                               | The ZIP code, city, and state where the facility is.                                                                                                                                                                                                        |
| User Operations                                                        | The users who can access the facility site and the read/write permissions granted to these users.                                                                                                                                                           |
| VISN                                                                   | The VISN to which the facility belongs.                                                                                                                                                                                                                     |
| Region:                                                                | The region to which the facility belongs.                                                                                                                                                                                                                   |
| BMS Active/Live Site?                                                  | If the site is active for use in BMS.                                                                                                                                                                                                                       |
| Allow Admin to Access Inactive Site?                                   | If the site is inactive, allows Admin to access site.                                                                                                                                                                                                       |
| Integrated Facility?                                                   | If the facility has an integrated VistA instance?                                                                                                                                                                                                           |
| Integrated Site List:                                                  | This is the list of integrated sites that are sharing the same VistA instance.                                                                                                                                                                              |
| Ward Prefix                                                            | The prefix used for the wards in the current integrated facility.                                                                                                                                                                                           |
| Ward Suffix                                                            | The suffix used for the wards in the current integrated facility.                                                                                                                                                                                           |
| EMS Mail Sender                                                        | This is the “FROM” user/group used to send EMS emails via the SMTP server                                                                                                                                                                                   |
| Site Alias                                                             | This is the alternate 3-char identifier for a site that may be used instead of its own, i.e. West Las Angeles (WLA) is an Alias for Greater Las Angeles (GLA), both names are the same site, and users could possibly log in as VHAGLAxxxxx or VHAWLAxxxxx. |
| EMS Default User Name:                                                 | The BMS Service Account ID needed to load the EMS Mobile Page for Mobile Devices.                                                                                                                                                                           |
| EMS Password:                                                          | The BMS Service Account ID password needed to load the EMS Mobile Page for Mobile Devices.                                                                                                                                                                  |
| EMS Password confirm:                                                  | The confirmation of the password.                                                                                                                                                                                                                           |
| Whiteboard Kiosk Default User Name:                                    | The BMS Service Account ID, along with the fully qualified domain name in front of the BMS Service Account ID, needed to load the Whiteboard URL in Kiosk Mode. (Example: v16.med.va.gov\VHAHOUxxx)                                                         |
| Whiteboard Kiosk Password:                                             | The BMS Service Account ID password needed to load the Whiteboard URL in Kiosk Mode.                                                                                                                                                                        |
| Whiteboard Kiosk Password confirm:                                     | The confirmation of the password.                                                                                                                                                                                                                           |
| BMS Server Time Zone                                                   | The time zone of the BMS server.                                                                                                                                                                                                                            |
| Facility Site Time Zone                                                | The time zone of the facility.                                                                                                                                                                                                                              |
| Auto-Removal Pending Bed Placement List?                               | If patients in the list Patients at the facility level are automatically removed from the Pending Bed Placement List when they are assigned a Room/Bed.                                                                                                     |
| Auto Placement of Transfers onto PPBP List?                            | If the patients are automatically placed on Pending Bed Placement List if their transfer status is appropriate.                                                                                                                                             |
| Medical Center ID#?                                                    | The ID \# of the medical center.                                                                                                                                                                                                                            |
| Allowed Access – Integrated Sites (All users can see these sites also) | The list of integrated sites is displayed; select the sites where the users of the current facility have access.                                                                                                                                            |
| ADT Prefix:                                                            | This is the unique identifier that is the leading part of the ADT (Admission/Discharge/Transfer Orderable Item) and is used to filter the list of ADT OIs that will be displayed. For example, “BO-” for Boston.                                            |
| ADT Suffix:                                                            | This is the unique identifier that is the trailing part of the ADT (Admission/Discharge/Transfer Orderable Item) and is used to filter the list of ADT OIs that will be displayed. For example, “-BO” for Boston.                                           |
| Event Mail Sender:                                                     | This is the “FROM” user/group used to send Event emails via the SMTP server.                                                                                                                                                                                |
| Site Alias:                                                            | This is the alternate 3-char identifier for a site that may be used instead of its own, i.e. West Las Angeles (WLA) is an Alias for Greater Las Angeles (GLA), both names are the same site, and users could possibly log in as VHAGLAxxxxx or VHAWLAxxxxx. |
| Local Time Adjust:                                                     | The difference between the local time and the server time.                                                                                                                                                                                                  |

After setting the desired parameters for the selected user, click the Submit button to enter the data into the system.

#### Deactivate and Reactivate Sites

In the main Administration section page, click the Edit BMS Facility Settings link to access the page in the following image:

<span id="_Toc205379973" class="anchor"></span>Figure 186 - Administration Section – Facility Edit Screen

![](bed-management-solution-version-5-0-admin-guide/232.png)

Under the Select Facility Name section, choose the Facility you would like to deactivate.

<span id="_Toc205379974" class="anchor"></span>Figure 187 - Administration Section – Facility Edit Screen

![](bed-management-solution-version-5-0-admin-guide/233.png)

Select No from the BMS Active/Live Site field to make the Facility inactive.

<span id="_Toc205379975" class="anchor"></span>Figure 188 - Facility Edit Screen – Active/Live Site

![](bed-management-solution-version-5-0-admin-guide/234.png)

Choose Yes or No from the Allow Admin to Access Inactive Site field.

<span id="_Toc205379976" class="anchor"></span>Figure 189 - Facility Edit Screen – Admin Access to Inactive Site

![](bed-management-solution-version-5-0-admin-guide/235.png)

Once you have made your changes, press Submit. A screen is displayed that the Facility has been updated.

<span id="_Toc205379977" class="anchor"></span>Figure 190 - VISN Network Bed Board Page

![](bed-management-solution-version-5-0-admin-guide/236.png)

To view that the Facility was inactivated, return to the Regional Page and choose the VISN in which the Facility is located, and you will see that the Facility was inactivated and does not show in the Facility List.

#### Auto-Remove EDIS Patients from PPBP List

In the main Administration section page, click the Edit BMS Facility Settings link to access the page in the following image.

<span id="_Toc205379978" class="anchor"></span>Figure 191 - Administration Section – Facility Edit Screen

![](bed-management-solution-version-5-0-admin-guide/237.png)

Under the Select Facility Name section, choose the Facility you would like to Auto-Remove EDIS Patients from PPBP list.

<span id="_Toc205379979" class="anchor"></span>Figure 192 - Administration Section – Facility Edit Screen

![](bed-management-solution-version-5-0-admin-guide/238.png)

Select Yes from the Auto-Remove EDIS Patients from Pending Bed Placement List field to Auto-remove patients.

<span id="_Toc205379980" class="anchor"></span>Figure 193 - Facility Edit Screen – Auto-Remove EDIS patients from Pending Bed Placement List

![](bed-management-solution-version-5-0-admin-guide/239.png)

Once you have made your changes, press Submit. A screen is displayed that the Facility has been updated.

### Edit Sister Sites Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the main Administration Section page, click the Edit Sister Sites link to access the page as in the following image:

<span id="_Toc51236189" class="anchor"></span>Figure 194 - Edit BMS Sister Sites

![](bed-management-solution-version-5-0-admin-guide/240.png)

In this page the user can define a list of sister sites or can edit one of the existing sister sites lists.

#### Adding a Sister Sites List

In the Administration Section – Sister Site Add/Edit page, to define a list of sister sites enter a Record No. Then in the BMS Sister Sites? Field enter the abbreviation of the sites sharing the same VistA instance, separated by comma. Press the Submit button to enter the data into the system. The defined list will be available in the dropdown field Select Existing Sister Sites.

The following parameters can be set:

<span id="_bookmark390" class="anchor"></span>Table 26 - BMS Sister Site Parameters

| COLUMN            | DESCRIPTION                                                                |
|-------------------|----------------------------------------------------------------------------|
| Record No         | Unique record number for the particular record.                            |
| BMS Sister Sites? | This is the list of sister sites that are sharing the same VistA instance. |

After setting the desired parameters, click the Submit button to enter the data into the system.

#### Editing a Sister Sites List

In the Administration Section – Sister Site Add/Edit page, to edit an existing list of sister sites click the arrow button of the field Select Existing Sister Sites to display existing sister sites lists. Select the one for which you want to modify parameters. The BMS Sister Sites? field will display the list of abbreviations for the sister sites in the list. Add or remove the desired abbreviation(s) then click the Submit button.

### Add/Edit Icon Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the main Administration Section page, click the Add/Edit Icon link to access the page in the following image.

> **NOTE:** ![](bed-management-solution-version-5-0-admin-guide/241.png) Users are discouraged from using the words DNR/DNI in the comment of the Ward Whiteboard or using any icon to represent DNR/DNI on the Ward Whiteboard.

<span id="_Toc52889880" class="anchor"></span>Figure 195 - Administration Section – Icon Add/Edit

![](bed-management-solution-version-5-0-admin-guide/242.png)

![](bed-management-solution-version-5-0-admin-guide/243.png)

The following icon types are available: Application icons (System icons and Bed Cleaning Status icons) and Ward Whiteboard Status Icons (Standard icons, Emergency Management Icons and Site Configurable icons).

In this page the user can perform the following actions: modify the position of an icon in any of the icon lists available, edit the details of an icon in any of the icons list, add an icon to one of the existing icon lists, search for an icon, or generate a report on the icon usage within a facility site.

#### Modifying the position of an icon in the icon list

To modify the position of an icon in the list simply click and drag the icon to its appropriate position.

<span id="_Toc51236191" class="anchor"></span>Figure 196 - Administration Section – Change Icon Position in the Icon List

![](bed-management-solution-version-5-0-admin-guide/244.png)

#### Editing the details of an icon in the icon list

To edit the details of an icon in the list click the Edit link to the left of the icon image.The following page is displayed:

<span id="_Toc51236192" class="anchor"></span>Figure 197 - Administration Section – Edit Icon

![](bed-management-solution-version-5-0-admin-guide/245.png)

To select another image for the icon, click the Browse button of the Image Name field then, locate the file containing the new image and select it. Make the desired changes in the rest of the fields then press the Save button to apply the changes. The fields marked with the asterisk sign “\*” are mandatory.

#### Adding an icon to the icon list

To add an icon to an icon list, click the Add Icon link in the top left corner of an icon list. The following page is displayed:

<span id="_Toc51236193" class="anchor"></span>Figure 198 - Administration Section – Add Icon

![](bed-management-solution-version-5-0-admin-guide/246.png)

Click the Browse button to locate the file containing the icon image and select it.

<span id="_Toc52889884" class="anchor"></span>Figure 199 - Selecting an Icon Image File

![](bed-management-solution-version-5-0-admin-guide/247.png)

After selecting the file, a preview of the selected icon image will be displayed to the left of the screen.

<span id="_Toc205380087" class="anchor"></span>Table 27 - Add/Edit Icon Page Parameters

| COLUMN    | DESCRIPTION                                                                                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------|
| Active    | If an icon is not active it will appear grayed in the icon list.                                                                               |
| Published | If an icon is not published it will not appear in the facility Bed Management Board Icons page or in the Site Configurable Icons page. |
| Patient   | This option indicates whether the icon is used to flag a patient.                                                                              |
| Bed/Room  | This option indicates whether the icon is used to flag a room/bed.                                                                             |

![](bed-management-solution-version-5-0-admin-guide/248.png)NOTE: Once an icon has been used to flag a patient or a bed, it cannot be inactivated. In order to be able to make the icon inactive the user will have to remove the icon from Whiteboard where it has been used. Use the Search link in the upper right corner of the Administration Section – Icon Add/Edit page to locate the facility site where an icon has been used. For details see the section [<u>Searching an icon</u>](\l).

Enter the required information in the fields marked with the asterisk sign“\*”. The fields marked with the asterisk sign “\*” are mandatory. (Note: The fields will only be mandatory if the icon is active.)

Press the Save button to add the new icon the icon list.

#### Configuring Auto-Icons for use in BMS

First, a National Administrator must create/assign the icon and make it selectable as an Orderable Icon. The administrator will assign the image name, icon name, descriptions, VistA Orderable Item, and mouse over text, but also make sure to make the Orderable Icon “Activated”.

![](bed-management-solution-version-5-0-admin-guide/249.png)NOTE: The icon MUST be a “Standard” Icon and the actual Vista Orderable Item must contain the same portion of text as the Orderable Item selection within the Facility Admin. In the example below, we added “Acetaminophen” where the Orderable Item selection listed “Acetaminophen To (01/24/2019)…”. This is what is meant by “pattern matching.”

<span id="_Toc51236195" class="anchor"></span>Figure 200 - National Administrator Edit Icon Page

![](bed-management-solution-version-5-0-admin-guide/250.png)

Next, the Site Admin can configure their Auto-Icon by performing the following steps:

<span id="_Toc52889886" class="anchor"></span>Figure 201 - Facility Home Page and Site Options Button

![](bed-management-solution-version-5-0-admin-guide/251.png)

From the Facility Home Page, click Site Options. Then click BMS Orderable Items Add/Delete.

<span id="_Toc52889887" class="anchor"></span>Figure 202 - Facility Site Options Page and BMS Orderable Items Add/Delete Link

![](bed-management-solution-version-5-0-admin-guide/252.png)

<span id="_Toc52889888" class="anchor"></span>Figure 203 - BMS Orderable Items Add/Delete Page

![](bed-management-solution-version-5-0-admin-guide/253.png)

The CPRS BMS Orderable Item list highlighted above is a very large record set. It may take a while to load this list for selection. Please be patient selecting the Orderable item from the list.<span id="_Toc52889889" class="anchor"></span>

Figure 204 - Selection of Orderable Item and Item Type

![](bed-management-solution-version-5-0-admin-guide/254.png)

For this example, we’ve selected “ACETAMINOPHEN TAB” as the Orderable Item and “AUTO-ICON” as the Orderable Item Type. Next, click Add.

You should see a confirmation that the new Orderable Item configuration has been added, as below:

<span id="_Toc52889890" class="anchor"></span>Figure 205 - Orderable Item Configuration Addition Confirmation

![](bed-management-solution-version-5-0-admin-guide/255.png)

The next step is to Return to the Facility Site Options page and click on Site Configurable Icons.

<span id="_Toc51236201" class="anchor"></span>Figure 206 - Facility Site Options Page and Site Configurable Icons Link

![](bed-management-solution-version-5-0-admin-guide/256.png)

The Site Admin should now scroll down to the section and be able to see the new Icon and Orderable item listing. Click the Active checkbox, then Save the configuration.

<span id="_Toc51236202" class="anchor"></span>Figure 207 - Site Configurable Icons Screen, showing Automatic VistA Orderable Item Icons

![](bed-management-solution-version-5-0-admin-guide/257.png)

Your Auto-Icon is now configured for use and will begin to appear when that orderable item is retrieved from VistA.

#### Searching an Icon

To search an icon, click the Search link to the top right corner of the Administration Section – Add/Edit page. The following screen is displayed:

<span id="_Toc52889893" class="anchor"></span>Figure 208 - Administration Section – Icon Search

![](bed-management-solution-version-5-0-admin-guide/258.png)

Select the icon(s) which you want to locate then press the Search button to display the page with the search results as in the following image:

<span id="_Toc51236204" class="anchor"></span>Figure 209 - Site Configurable Icon Search Result

![](bed-management-solution-version-5-0-admin-guide/259.png)

The search results will present the code of the facility where the icon is used, the icon name and the description given to the icon on the facility site.

#### Generating an Icon Usage Report

To generate an icon usage report, click the Report link in the top right corner of the Administration Section – Add/Edit page. The following screen is displayed:

<span id="_Toc51236205" class="anchor"></span>Figure 210 - Administration Section – Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/260.png)

By default, Icon Type, Images, and VISNs have all options selected, but can be changed by selecting the drop-down. Use the drop-down for Facility to select which facility or facilities and the date range you want to generate the Icon Usage report for, then press the View Report button. The report is displayed as in the following image:

<span id="_Toc51236206" class="anchor"></span>Figure 211 - Administration Section – Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/261.png)

Also note that this report is a drill-down report, in which the rows can be collapsed/expanded to drill into the individual patient or bed records that have had the icon associated with it within the date range selected.

<span id="_Toc51236207" class="anchor"></span>Figure 212 - Administration Section – Icon Usage Report Drill-Down Feature

![](bed-management-solution-version-5-0-admin-guide/262.png)

For each entry the following data is available:

<span id="_bookmark402" class="anchor"></span>Table 28 - Icon Usage Report

| Column                                  | Description                                                                         |
|-----------------------------------------|-------------------------------------------------------------------------------------|
| Site Name                               | The Facility site where the icon has been used.                                     |
| Icon Short Description for Facility     | The short description of the icon.                                                  |
| Icon Name                               | The icon name.                                                                      |
| Facility Active? (Y/N)                  | If the icon is active on the facility site.                                         |
| Associated with a Patient Record? (Y/N) | If the icon is currently associated with a patient record.                          |
| Associated with a bed record? (Y/N)     | If the icon is currently associated with a bed record.                              |
| Drill-Down Columns                      | These additional columns are revealed once you “drill-into” the appropriate record. |
| Patient/Bed Record                      | Indicator of whether the record is a P(atien)T record or a BED record               |
| Ward                                    | The name of the ward for the PT/BED that the icon is associated to.                 |
| Bed                                     | The name of the bed the icon is associated to.                                      |
| Patient                                 | The name of the patient the icon is associated to.                                  |

### View Audit Log Page – Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Administration Section page click the View Audit Log link to access the page as in the following image.

<span id="_Toc51236210" class="anchor"></span>Figure 213 - Administration Section – Audit Log Report Types

![](bed-management-solution-version-5-0-admin-guide/263.png)

The reports available from the National Admin Audit Log Page follow below:

#### Standard Icons

This is a report of the standard icons modified for the specified Region, VISN, Site, and Date Range.

<span id="_Toc51236211" class="anchor"></span>Figure 214 - Standard Icons

![](bed-management-solution-version-5-0-admin-guide/264.png)

#### Site Configurable Icons Report

The Site Configurable Icons Report presents information about the usage of the site configurable icons within the system.

In the Audit Log Report page use the Select Report field to select the Site Icons report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of a Site Configurable Icons Report.

<span id="_Toc205380002" class="anchor"></span>Figure 215 - Site Configurable Icons Report

![](bed-management-solution-version-5-0-admin-guide/265.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc205380089" class="anchor"></span>Table 29 - Site Configurable Icons Report Parameters

| Column                   | Description                                                                                 |
|--------------------------|---------------------------------------------------------------------------------------------|
| Icon Category            | The type of icon: can only be Site Configurable Icon.                                       |
| Facility                 | The name of the facility for which the icon has been configured and used.                   |
| (Icon image)             | The icon image.                                                                             |
| Image Name               | The name of the image entered in the Image Name field in the Edit Icon page.                |
| Icon Name                | The name assigned to the icon.                                                              |
| Active                   | If the icon is active.                                                                      |
| Published                | If the icon has been published.                                                             |
| Type: Patient or RoomBed | If the icon is used to flag a patient or a room or a bed.                                   |
| Description              | The description of the icon as entered in the Icon Description field in the Edit Icon page. |
| Comment                  | Any comment entered in the Comments field in the Edit Icon page.                            |
| Mouse Over Text          | The text entered in the Mouse Over Text field in the Edit Icon page.                        |
| Created By               | The name of the user who performed the current operation on the icon.                       |
| Date                     | The date and time when the current operation has been performed on the icon.                |
| Event Type               | The type of operation that has been performed on the icon.                                  |

#### Facility Patient Pending Bed Placement List Report

The Facility Patient Pending Bed Placement List Report presents information about what users have performed what actions on a facility pending bed placement list.

In the Audit Log Report page use the Select Report field to select the Facility Pending Bed Placement List report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of a Facility Patient Pending Bed Placement List Report.

<span id="_Toc205380003" class="anchor"></span>Figure 216 - Facility Patient Pending Bed Placement List Report

![](bed-management-solution-version-5-0-admin-guide/266.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc205380090" class="anchor"></span>Table 30 - Facility Patient Pending Bed Placement List Report Parameters

| COLUMN           | DESCRIPTION                                                       |
|------------------|-------------------------------------------------------------------|
| Facility         | The name of the VA facility.                                      |
| Patient          | The code of the patient.                                          |
| Problem          | The problem for which the patient needed treatment.               |
| Bed              | The bed assigned to the patient.                                  |
| Req Bed Date     | The date when the bed was requested for the patient.              |
| Type of Bed Ward | The type of bed/ward requested for the patient.                   |
| Waiting Area     | The waiting area where the patient has been placed.               |
| Fee Disposition  | The fee disposition associated to the patient.                    |
| Contract Fee     | The contract fee.                                                 |
| Auth. Fee        | The authorization to use the fee.                                 |
| Serv. Rec.       | The type of service requested according to the patient’s problem. |
| Reason           | The reason for using the fee.                                     |
| Comments         | Any comments entered in the Comments field.                       |
| Created by       | The user who created the event.                                   |
| Date             | The date and time when the event was created.                     |
| Event Type       | The type of event.                                                |

#### VISN Patient Pending Bed Placement List Report

The VISN Patient Pending Bed Placement List Report presents information about what users have performed what actions on a VISN pending bed placement list.

In the Audit Log Report page use the Select Report field to select the VISN Patient Pending Bed Placement List report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of a VISN Patient Pending Bed Placement List Report.

<span id="_Toc205380004" class="anchor"></span>Figure 217 - VISN Patient Pending Bed Placement List Report

![](bed-management-solution-version-5-0-admin-guide/267.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc205380091" class="anchor"></span>Table 31 - VISN Patient Pending Bed Placement List Report Parameters

| COLUMN             | DESCRIPTION                                                                         |
|--------------------|-------------------------------------------------------------------------------------|
| Facility           | The name of the VA facility.                                                        |
| VISN               | The VISN where the VA facility is located.                                          |
| Patient            | The code of the patient.                                                            |
| ERA                | The period of service that the patient served.                                      |
| Contract           | Whether or not the VA facility has a contract with the selected community hospital. |
| Diagnosis          | The diagnosis for which the patient requests admission to the community hospital.   |
| Current location   | The name of the community hospital where the patient is currently being treated     |
| Location Adm. Date | The date when the patient has been admitted in the selected location.               |
| Comments           | Any comments entered in the Comments field.                                         |
| Specialty          | The treating specialty corresponding to the type of need.                           |
| Req. Adm. Date     | The date when the patient should be able to be admitted to the VA facility.         |
| Created by         | The name of the user who created the event.                                         |
| Date               | The date and time when the event has been created.                                  |
| Event Type         | The type of the event.                                                              |

#### Staff Assignment Report

The Staff Assignment Report presents information about what users have assigned staff personnel to the beds in the wards of a facility.

In the Audit Log Report page use the Select Report field to select the Staff Assignment report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of a Staff Assignment Report.

<span id="_Toc205380005" class="anchor"></span>Figure 218 - Staff Assignment Report

![](bed-management-solution-version-5-0-admin-guide/268.png)

For each entry the following data is available:

<span id="_Toc205380092" class="anchor"></span>Table 32 - Staff Assignment Report Parameters

| COLUMN     | DESCRIPTION                                        |
|------------|----------------------------------------------------|
| Ward       | The ward where the bed is.                         |
| Bed        | The code of the bed.                               |
| Staff      | The name of the person assigned to the bed.        |
| Patient    | The code of the patient occupying the bed.         |
| Created by | The name of the user who created the event.        |
| Date       | The date and time when the event has been created. |
| Event Type | The type of the event.                             |

#### Bed History Report

The Bed History Report presents information about what users have performed what actions on a bed.

In the Audit Log Report page use the Select Report field to select the Bed History Report, then Region, VISN,Site, and then select From Date/To Date determine the time interval for the report and press the View Report button. The image below presents an example of a Bed History Report:

<span id="_Toc205380006" class="anchor"></span>Figure 219 - Bed History Report

![](bed-management-solution-version-5-0-admin-guide/269.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc205380093" class="anchor"></span>Table 33 - Bed History Report Parameters

| COLUMN         | DESCRIPTION                                 |
|----------------|---------------------------------------------|
| Bed Name       | The bed number.                             |
| Edited Date    | The date and time the bed was edited.       |
| Reason         | The reason the bed is being edited.         |
| Type           | The type of edit reason.                    |
| Edited By      | The name of the user editing the bed.       |
| Cleared By     | The name of the user who cleared the edits. |
| Completed Date | The date the bed was cleared of all edits.  |

#### PPBP Usage (VISN) Report

The PPBP Usage (VISN) Report presents information about any and all modifications users have made from the Patient Pending Bed Placement (PPBP) view.

In the Audit Log Report page use the Select Report field to select the PPBP Usage (VISN) report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of the PPBP Usage (VISN) Report:

<span id="_Toc205380007" class="anchor"></span>Figure 220 - PPBP Usage (VISN) Report

![](bed-management-solution-version-5-0-admin-guide/270.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc205380094" class="anchor"></span>Table 34 - PPBP Usage (VISN) Report Parameters

| COLUMN               | DESCRIPTION                                                                           |
|----------------------|---------------------------------------------------------------------------------------|
| Entered D/T          | The Date/Time of the modification to the Whiteboard.                                  |
| Requested D/T        | The Date/Time the placement on the board was requested.                               |
| Removed D/T          | The Date/Time the entry was removed.                                                  |
| Edit Event D/T       | The Date/Time the event was deleted.                                                  |
| User                 | The BMS User who made the modification.                                               |
| Patient Name         | The patient’s last name and last 4 digits of the SSN.                                 |
| Transaction          | The type of operation performed on the record, such as Update, New Record, or Delete. |
| Transaction Updates  | The updates made to the Whiteboard, not including comments.                           |
| Transaction Comments | Any comments made for the transaction performed by the user.                          |

#### PPBP Usage (Facility) Report

The PPBP Usage (Facility) Report presents information about any and all modifications users have made from the Patient Pending Bed Placement (PPBP) view.

In the Audit Log Report page use the Select Report field to select the Whiteboard Usage report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of the PPBP Usage (Facility) Report:

<span id="_Toc205380008" class="anchor"></span>Figure 221 - PPBP Usage (Facility) Report

![](bed-management-solution-version-5-0-admin-guide/271.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc205380095" class="anchor"></span>Table 35 - PPBP Usage (Facility) Report Parameters

| COLUMN               | DESCRIPTION                                                                           |
|----------------------|---------------------------------------------------------------------------------------|
| Entered D/T          | The Date/Time of the modification to the Whiteboard.                                  |
| Requested D/T        | The Date/Time the placement on the board was requested.                               |
| Removed D/T          | The Date/Time the entry was removed.                                                  |
| Edit Event D/T       | The Date/Time the event was deleted.                                                  |
| User                 | The BMS User who made the modification.                                               |
| Patient Name         | The patient’s last name and last 4 digits of the SSN.                                 |
| Transaction          | The type of operation performed on the record, such as Update, New Record, or Delete. |
| Transaction Updates  | The updates made to the Whiteboard, not including comments.                           |
| Transaction Comments | Any comments made for the transaction performed by the user.                          |

#### Whiteboard Patient Icon Usage Report

The Whiteboard Patient Icon Usage Report presents information about modifications users have made to Patients from the Whiteboard.

In the Audit Log Report page use the Select Report field to select the Whiteboard Patient Icon Usage report, then select the Region, VISN and Site, then the From Date/To Date to determine the time interval for the report and press the View Report button.

<span id="_Toc205380009" class="anchor"></span>Figure 222 - Selecting Whiteboard Patient Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/272.png)

The image below presents an example of the Whiteboard Patient Icon Usage Report:

<span id="_Toc205380010" class="anchor"></span>Figure 223 - Whiteboard Patient Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/273.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

| COLUMN              | DESCRIPTION                                                                           |
|---------------------|---------------------------------------------------------------------------------------|
| Entered D/T         | The Date/Time the entry was created.                                                  |
| User                | The BMS User who made the entry.                                                      |
| Bed                 | The bed assigned to the patient.                                                      |
| Patient Name        | The last name, first name and last 4 digits of the patient’s SSN.                     |
| Transaction         | The type of operation performed on the record, such as Update, New Record, or Delete. |
| Transaction Updates | Any updates made for the transaction performed by the user.                           |

#### Whiteboard Bed Icon Usage Report

The Whiteboard Bed Icon Usage Report presents information about modifications users have made to Icons from the Whiteboard.

In the Audit Log Report page use the Select Report field to select the Whiteboard Bed Icon Usage report, then select the Region, VISN and Site, then the From Date/To Date to determine the time interval for the report and press the View Report button.

<span id="_Toc205380011" class="anchor"></span>Figure 224 - Selecting Whiteboard Bed Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/274.png)

The image below presents an example of the Whiteboard Bed Icon Usage Report:

<span id="_Toc205380012" class="anchor"></span>Figure 225 - Whiteboard Bed Icon Usage Report

![](bed-management-solution-version-5-0-admin-guide/275.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc205380097" class="anchor"></span>Table 37 - Whiteboard Bed Icon Usage Report Parameters

| COLUMN              | DESCRIPTION                                                                            |
|---------------------|----------------------------------------------------------------------------------------|
| Entered D/T         | The Date/Time the entry was created.                                                   |
| User                | The BMS User who made the entry.                                                       |
| Bed                 | The bed assigned to the patient.                                                       |
| Transaction         | The type of operation performed on the record, such as Update, New Record, or Deleted. |
| Transaction Updates | Any updates made for the transaction performed by the user.                            |

#### Whiteboard Comments Usage Report

The Whiteboard Comments Usage Report presents information about any and all modifications users have made from the Whiteboard.

In the Audit Log Report page use the Select Report field to select the Whiteboard Comments Usage report, then select Date from/Date to determine the time interval for the report, the Region, VISN and Site and press the View Report button. The image below presents an example of the Whiteboard Usage Report:

<span id="_Toc205380013" class="anchor"></span>Figure 226 - Whiteboard Comments Usage Report

![](bed-management-solution-version-5-0-admin-guide/276.png)

The title of the report is displayed in the upper part of the page. Navigation and display tools are available in the toolbar displayed across the screen. Place the mouse cursor over a button to display the corresponding tooltip.

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

| COLUMN               | DESCRIPTION                                                                                                                       |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Created D/T          | The Date/Time the comment was created.                                                                                            |
| Created by User      | The BMS User who created the comment.                                                                                             |
| Edited D/T           | The Date/Time of the modification to the Whiteboard.                                                                              |
| Edited by User       | The BMS User who made the modification.                                                                                           |
| Update Type          | The type of update made to the Whiteboard, such as Bed Reason Comment, Bed Unavailable, Icon Assignment, or Bed Staff Assignment. |
| Bed                  | The bed record affected by the modification.                                                                                      |
| Transaction          | The type of operation performed on the record, such as Update, New Record, or Delete.                                             |
| Transaction Comments | Any comments made for the transaction performed by the user.                                                                      |

### Treating Specialty/NUMA/HAvBED Edit Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Administration Section page click the Treating Specialty/NUMA/HAvBED Edit link to access the page as in the following image.

<span id="_Toc52889902" class="anchor"></span>Figure 227 - Administration Section – Treating Specialty/NUMA/HAvBED Edit

![](bed-management-solution-version-5-0-admin-guide/277.png)

In this page the user can add, edit and delete Nursing Unit Mapping Application (NUMA) and Hospital Available Beds for Emergencies & Disasters (HAvBED) treating specialties. Also, the user can map the defined VistA specialties with the NUMA and HAvBED treating specialties.

#### Adding a NUMA Specialty

In the Administration Section page click the Treating Specialty/NUMA/HAvBED Edit link to display the page in the following image:

<span id="_Toc52889903" class="anchor"></span>Figure 228 - Administration Section – Treating Specialty/NUMA/HAvBED Edit

![](bed-management-solution-version-5-0-admin-guide/278.png)

A list of NUMA specialties already defined is available.

To add a NUMA specialty, enter the name of the new NUMA specialty in the NUMA field then press the Save button. The newly added specialty will be displayed in the NUMA list.

#### Adding a HAvBED Specialty

In the Administration Section page click the Treating Specialty/NUMA/HAvBED Edit link to display the page in the following image:

<span id="_Toc52889904" class="anchor"></span>Figure 229 - Administration Section – Treating Specialty/NUMA/HAvBED Edit

![](bed-management-solution-version-5-0-admin-guide/279.png)

A list of HAvBED specialties already defined is available. To add a HAvBED specialty enter the name of the new HAvBED specialty in the HAvBED field then press the Save button. The newly added specialty will be displayed in the HAvBED list.

#### Editing a NUMA/HavBED Specialty

To edit an existing NUMA specialty, in the Administration Section - Treating specialty/NUMA/HAvBED Edit page click the Edit link associated to the NUMA specialty you want to edit. Its name will be displayed in the NUMA field at the top of the list. Make the desired changes then press the Save button. The NUMA Categories list will display the modified NUMA specialty.

To edit an existing a HAvBED specialty, in the Administration Section - Treating specialty/NUMA/HAvBED Edit page click the Edit link associated to the HAvBED specialty you want to edit. Its name will be displayed in the a HAvBED field at the top of the list. Make the desired changes then press the Save button. The HAvBED Categories list will display the modified a HAvBED specialty.

#### Deleting a NUMA/HavBED Specialty

To delete an existing NUMA specialty, in the Administration Section - Treating specialty/NUMA/HAvBED Edit page click the Delete link associated to the NUMA specialty you want to delete. The NUMA Categories list will be updated to reflect the change.

To delete an existing HAvBED specialty, in the Administration Section - Treating specialty/NUMA/HAvBED Edit page click the Delete link associated to the HAvBED specialty you want to delete. The HAvBED Categories list will be updated to reflect the change.

#### Mapping a VistA specialty with a NUMA/HavBED Specialty

In the Administration Section page click the Treating Specialty/NUMA/HAvBED Edit link to display the page in the following image. (Use the scroll bar to display the VistA Specialty Crosswalk section.)<span id="_Toc51236215" class="anchor"></span>

Figure 230 - Mapping A VistA Specialty with NUMA/HAvBED Specialty

![](bed-management-solution-version-5-0-admin-guide/280.png)

A list of VistA specialties is displayed with existing NUMA and/or HAvBED specialties mappings. To associate a VistA Specialty with a NUMA/HAvBED specialty, click the Edit link to the left of the VistA specialty to which you want to associate NUMA/HAvBED specialties.

The name of the selected VistA specialty will be displayed in the VistA Specialty field. From the NUMA and HAvBED fields select the desired specialties then press the Save button. The association defined will be displayed in the VistA Specialty Crosswalk list.

Also note that the Vista Specialty Crosswalk provides the ability to hide specialties by selecting the appropriate “Hidden” checkboxes as in the screenshot below:

<span id="_Toc52889906" class="anchor"></span>Figure 231 - Hiding a NUMA/HAvBED Specialty

![](bed-management-solution-version-5-0-admin-guide/281.png)

### National Waiting Area

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the National Waiting Area page, in the Administration Section page click the National Waiting Area link.

The National Waiting Area Add/Edit page is displayed as in the following image:

<span id="_Toc51236217" class="anchor"></span>Figure 232 - National Waiting Areas

![](bed-management-solution-version-5-0-admin-guide/282.png)

This is where you will add the locations for patients pending bed placement. These entries will appear on all sites and cannot be edited or deleted.

The options in the upper part of the screen allow the support user to define/add a new national waiting area in the system.

The list in the lower part of the screen presents the national waiting areas already defined in the system.

The links Edit and Delete to the left of each entry in the list allow the support user to modify the name of the selected waiting area or to delete the entry from the system.

To go back to the Administration Section page, click the link Admin Menu in the upper left corner of the page.

#### Adding a National Waiting Area

To add a national waiting area*,* follow the instructions below. From the Administration Section page, click the National Waiting Area link.The National Waiting Area page is displayed as in the image below:

<span id="_Toc51236218" class="anchor"></span>Figure 233 - Adding a Waiting Area

![](bed-management-solution-version-5-0-admin-guide/283.png)

In the Text field from the ADD Area enter the name of the new waiting area, then press the Add button. A confirmation message is displayed and the newly added waiting area is displayed in the Waiting Area list.

<span id="_Toc52889909" class="anchor"></span>Figure 234 - Waiting Area Added to the List

![](bed-management-solution-version-5-0-admin-guide/284.png)

#### Editing a National Waiting Area

To edit the name of an existing national waiting area*,* follow the instructions below. From the Administration Section page, click the National Waiting Area link.

<span id="_Toc51236220" class="anchor"></span>Figure 235 - Selecting National Waiting Area

![](bed-management-solution-version-5-0-admin-guide/285.png)

The National Waiting Area page is displayed as in the image below:

<span id="_Toc51236221" class="anchor"></span>Figure 236 - Selecting Waiting Area for Edit

![](bed-management-solution-version-5-0-admin-guide/286.png)

Selecting the Edit link will display the page as in the following image:

<span id="_Toc51236222" class="anchor"></span>Figure 237 - Edit Waiting Area Name

![](bed-management-solution-version-5-0-admin-guide/287.png)

In the CHANGE TO: field, enter the new name for the national waiting area then press the Submit button. A confirmation message will be displayed and the national waiting area with the new name will be displayed in the Waiting Area list.

<span id="_Toc52889913" class="anchor"></span>Figure 238 - Waiting Area Edited

![](bed-management-solution-version-5-0-admin-guide/288.png)

#### Deleting a Waiting Area

To delete a national waiting area defined for the current facility*,* follow the instructions below. From the Administration Section page, click the National Waiting Area link.<span id="_Toc51236224" class="anchor"></span>

Figure 239 - Selecting National Waiting Area

![](bed-management-solution-version-5-0-admin-guide/289.png)

The National Waiting Area page is displayed as in the image below:

<span id="_Toc51236225" class="anchor"></span>Figure 240 - Select a National Waiting Area for Deletion

![](bed-management-solution-version-5-0-admin-guide/290.png)

Click the Delete link associated to the waiting area that you want to delete. A confirmation screen is displayed as in the following image:

<span id="_Toc51236226" class="anchor"></span>Figure 241 - Deleting a National Waiting Area

![](bed-management-solution-version-5-0-admin-guide/291.png)

Click the Delete Record button to delete the national waiting area from the list.

### National Unavailable Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the National Unavailable Reason page, in the Administration Section page click the National Unavailable Reason link.

The National Unavailable Reason page is displayed as in the following image:

<span id="_Toc51236227" class="anchor"></span>Figure 242 - National Unavailable Reason Page

![](bed-management-solution-version-5-0-admin-guide/292.png)

The options in this page allow the support user to add a new national unavailable reason.

The list in the lower part of the screen presents the national unavailable reasons already defined in the system.

For each entry in the list, the following data is available:

<span id="_bookmark429" class="anchor"></span>Table 39 - Unavailable Reason Parameters

| COLUMN             | DESCRIPTION                               |
|--------------------|-------------------------------------------|
| Unavailable Reason | The reason why a bed is made unavailable. |
| Type               | The type of reason.                       |

The links Edit and Delete allow the support user to modify the details of a reason or delete it from the system.

The link Admin Menu in the upper left corner of the page allows the support user to go back to the Administration Section page.

#### Adding a National Unavailable Reason

To add a national unavailable reason*,* follow the instructions below.

From the Administration Section page, click the National Unavailable Reason link.

The National Unavailable Reason page is displayed as in the following image:

<span id="_Toc51236228" class="anchor"></span>Figure 243 - Adding a National Unavailable Reason

![](bed-management-solution-version-5-0-admin-guide/293.png)

In the Text field enter the explanation and the reason for the bed unavailability. Then from the Type field select the type of reason, and click the Add button.

In the Type field, four types of ‘unavailable’ reasons can be selected:

<span id="_Toc205380100" class="anchor"></span>Table 40 - Unavailable Reason Types

| COLUMN         | DESCRIPTION                               |
|----------------|-------------------------------------------|
| Information    | No icon appears on the whiteboard.        |
| Isolation      | Isolation icon appears on the whiteboard. |
| Do Not Display | Bed does not appear on the whiteboard.    |
| Out of Service | Bed is colored RED on the whiteboard.     |

The newly defined reason will be added to list of existing reasons.

You can use the Edit link to modify either the text or the type of the reason. Use the Delete link to remove the link from the list.

#### Editing a National Unavailable Reason

To edit a national unavailable reason*,* follow the instructions below.

From the Administration Section page, click the National Unavailable Reason link. The National Unavailable Reason page is displayed as in the following image:

<span id="_Toc51236229" class="anchor"></span>Figure 244 - Selecting Unavailable Reason for Edit

![](bed-management-solution-version-5-0-admin-guide/294.png)

Click the Edit link associated to the national unavailable reason that you want to modify. The following page is displayed:<span id="_Toc51236230" class="anchor"></span>

Figure 245 - Editing an Unavailable Reason

![](bed-management-solution-version-5-0-admin-guide/295.png)

Enter the desired changes in the Text and/or Type fields then press the Submit button.

#### Deleting a National Unavailable Reason

To delete a national unavailable reason*,* follow the instructions below.

From the Administration Section page, click the National Unavailable Reason link. The National Unavailable Reason page is displayed as in the following image:

<span id="_Toc51236231" class="anchor"></span>Figure 246 - Selecting a National Unavailable Reason for Deletion

![](bed-management-solution-version-5-0-admin-guide/296.png)

Click the Delete link associated to the national unavailable reason that you want to delete. A confirmation screen is displayed as in the following image:<span id="_Toc51236232" class="anchor"></span>

Figure 247 - Delete a National Unavailable Reason

![](bed-management-solution-version-5-0-admin-guide/297.png)

Click the Delete Record button to delete the national unavailable reason from the list.

### Background Processors Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is used to determine which are the VA facility sites sharing the same VistA instance, to set up the Schedulers, to determine the Categories which will be affected by the Schedulers’ action (VistA Integration), to set up the scope of the Audit action, to schedule NUMI and Whiteboard report processes, and to configure the Provider Profile Management System (PPMS) job for keeping Community Care Facilities up to date.

The Background Processors page is displayed as in the following image:

<span id="_Toc52889923" class="anchor"></span>Figure 248 - Background Processors Page

![](bed-management-solution-version-5-0-admin-guide/298.png)

Seven tabs are available in the Background Processors page: VistA Sites, Schedulers, VistA Integration, Audit, NUMI, Whiteboard Report and PPMS. The following sections contain the detailed description of the options available in each tab.

#### VistA Sites

The VistA Sites page allows the user to view the list of VA facility sites sharing the same VistA instance, and to add a new VA facility to a VistA instance.

To add a VA facility site to a VistA instance, follow the steps presented below.

From the Background Processors page select VistA Sites to display the page shown in the following figure:

<span id="_Toc52889924" class="anchor"></span>Figure 249 - Background Processors Page – Adding a VistA Site

![](bed-management-solution-version-5-0-admin-guide/299.png)

A list of VA facility sites is displayed in the column to the left of the page.

Click the Add new VistA site link then from the VistA Site area, use the Name field to select the site you want to add to the current VistA instance then select the Time Zone.

Press Save to enter new data into the system.

The newly added site will be added in the sites list to the left of the screen.

#### Schedulers

The Schedulers page displays a list of defined schedulers and allows the support user to add new ones.

![](bed-management-solution-version-5-0-admin-guide/300.png)NOTE: In this page you can only define the schedulers. To actually run the defined schedulers you have to use the VistA Integration tab. See the [VistA Integration](\l) section for details.

The Schedulers page is displayed as in the following image:

<span id="_Toc51236235" class="anchor"></span>Figure 250 - Schedulers page

![](bed-management-solution-version-5-0-admin-guide/301.png)

#### Adding a New Scheduler

To add a new scheduler, follow the steps presented below.

From the Background Processors page select the Schedulers tab. In the Schedulers tab fill in the following data:

<span id="_bookmark443" class="anchor"></span>Table 41 - New Scheduler Parameters

| COLUMN                      | DESCRIPTION                |
|-----------------------------|----------------------------|
| Name                        | The name of the scheduler. |
| Recurs every                | The frequency.             |
| Occurs once at/Occurs every | The frequency values.      |

After you have set the desired frequency for the new scheduler do not forget to press the Save button to enter the data into the system.

#### VistA Integration

The VistA Integration tab is used to run (automatically or manually) the defined schedulers and to select which data categories will be affected by a scheduler’s action.

The VistA Integration tab is displayed as in the following image:

<span id="_Toc51236236" class="anchor"></span>Figure 251 - VistA Integration Tab

![](bed-management-solution-version-5-0-admin-guide/302.png)

From the field in the upper part of the page, first select the VistA site where the scheduler(s) will run. To setup a scheduler for any of these jobs, click one data category from the column on the left (its name will appear in the Data field) and then select a schedule in the Schedulers fields in the Details area and click the Save button. This will cause the selected scheduler to run at the time set for it in the Schedulers tab and to retrieve the data from VistA for the selected category.

<span id="_Toc205380039" class="anchor"></span>Figure 252 - VistA Integration Tab – ADT data gathering job for specific VistA

![](bed-management-solution-version-5-0-admin-guide/303.png)

Here is a brief description of the VistA data gathering jobs:

- ADT: the job will query from VistA ADT data (Orders, Movements, Scheduled Admissions, Patient Appointments) dated since the last run. Typically, this job should be scheduled to run at least every 5 minutes. The movements are processed into BMS and are reconciled back the number of days governed by a configuration setting in BMS. Currently this configuration setting is set to reconcile back 60 days.
- Patient Pending Bed Placement List: the job will look into the Scheduled Admission VistA file and extracts all the entries that have the “reservation date” field due for the current day. For these items the job adds associated entries into the facility patients pending bed placement list. Typically, if a facility chooses to run this job it would be scheduled once a day in the early morning.

Vocabularies:

- Orderable Items: the job will look into the Orderable Items VistA file and gets into BMS all the modifications discovered in VistA (items newly added and items updated). Typically, this job should be scheduled to run once a day at Midnight.
- Specialty: the job will look into the Specialty VistA file and gets into BMS all the modifications discovered in VistA (items newly added and items updated). Typically, this job should be scheduled to run once a day at Midnight.
- Treating Specialty: the job will look into the Treating Specialty VistA file and gets into BMS all the modifications discovered in VistA (items newly added and items updated). Typically, this job should be scheduled to run once a day at Midnight.
- Facility Movement Type: the job will look into the Facility Movement Type VistA file and gets into BMS all the modifications discovered in VistA (items newly added and items updated). Typically, this job should be scheduled to run once a day at Midnight.

Entities:

- Hospital Location: the job will look into the Hospital Location VistA file and gets into BMS all the modifications discovered in VistA (items newly added and items updated). Also, for the items that are Wards, the Ward list in BMS is updated accordingly. Typically, this job should be scheduled to run once a day at Midnight.
- Patient: the job will look into the Patient file and gets all the patients that have been added since the last run (they are filtered by the “date entered into file” field). Typically, this job should be scheduled to run at least every 5 minutes.
- Room Bed: the job will look into the Room Bed VistA file and gets into BMS all the modifications discovered in VistA (items newly added and items updated, also Beds Set Out of Service or Returned into Service. Typically, this job should be scheduled to run at least every 15 minutes.
- Ward Location: the job will look into the Ward Location VistA file and gets into BMS all the modifications discovered in VistA (items newly added and items updated). Typically, this job should be scheduled to run at least every 15 minutes.
- Medical Center Division: the job will look into the Ward Location VistA file and gets into BMS all the modifications discovered in VistA (items newly added and items updated). Typically, this job should be scheduled to run once a day at Midnight.

To Execute/Run any of the data jobs, select any of the data categories using the checkboxes, set the Start time/End time, and click the Run button. This will cause the selected scheduler to run using the selected method and retrieve the data from VistA for the selected data categories.

![](bed-management-solution-version-5-0-admin-guide/304.png)This functionality is available for National Support Users Only.

![](bed-management-solution-version-5-0-admin-guide/305.png)NOTE: To run a patient movement sync for a specific patient for missing or changed movements in VistA (in the Patient to Synchronize field after entering the Start Time and End Time and the patient IEN) click on the Run Patient Movement Synchronizer button.

<span id="_Toc205380040" class="anchor"></span>Figure 253 - VistA Integration Tab – Run Patient Movement Synchronizer for specific VistA and patient IEN

![](bed-management-solution-version-5-0-admin-guide/306.png)

#### Audit

The Audit tab displays the results of the operations performed in the VistA Integration tab. The Audit tab is displayed as in the following image:

<span id="_Toc51236237" class="anchor"></span>Figure 254 - Audit Page

![](bed-management-solution-version-5-0-admin-guide/307.png)

The options to the left of the page allow the user to determine the filter criteria for the generated audit reports. The options to the right of the screen allow the user to select the type of operation to be captured by the audit report as well as the time interval for the audit.

After you have selected the desired criteria click the Filter By button to display the page as in the following image:<span id="_Toc51236238" class="anchor"></span>

Figure 255 - View Audit Results

![](bed-management-solution-version-5-0-admin-guide/308.png)

![](bed-management-solution-version-5-0-admin-guide/309.png)To see audit logging of manual "Patient Movement Synchronizer" jobs, selecting the ADT Data Types checkbox.

A list of operations is displayed, for each entry the following data is available:

Table 76 - VistA Audit

| Column      | Description                                                                 |
|-------------|-----------------------------------------------------------------------------|
| VistA       | The VistA site where the audit action has been performed.                   |
| Data        | The type of data retrieved by the VistA integration operation.              |
| Rows No     | The number of operations of the selected type captured by the audit action. |
| Start Date  | The start date of the retrieval operation.                                  |
| End Date    | The end date of the retrieval operation.                                    |
| Launch Type | The way the audit action has been launched.                                 |
| Parameters  | The start date and time and the end date and time of the audit operation.   |
| Status      | The status of the VistA integration action.                                 |
| Details     | Clicking this link will display the number of entries in the report.        |

#### NUMI

The NUMI tab is used to select the scheduler that will connect to the NUMI server and will retrieve data for a certain VistA site.

The NUMI tab is displayed as in the following image.

<span id="_Toc51236239" class="anchor"></span>Figure 256 - NUMI Page

![](bed-management-solution-version-5-0-admin-guide/310.png)

From the Schedulers field select the scheduler created to retrieve the NUMI data then click the Add button, as displayed in the image above.

![](bed-management-solution-version-5-0-admin-guide/311.png) Note: It is not recommended that any VistA Site Schedule the NUMI Background process to run more frequently than every 2 hours. Doing so may reduce overall system performance.

<span id="_Toc52889930" class="anchor"></span>Figure 257 - Selecting the VistA Site for Which to Gather NUMI Data

![](bed-management-solution-version-5-0-admin-guide/312.png)

Select the VistA site for which the selected scheduler will retrieve NUMI data then press the Save button. Use the Edit link to select a different site for which the scheduler should retrieve NUMI data.

#### Whiteboard Tab

The Whiteboard Tab is used to select the scheduler that will gather data for the Whiteboard report.

The Whiteboard Tab is displayed as in the following image:

<span id="_Toc51236241" class="anchor"></span>Figure 258 - Whiteboard Tab

![](bed-management-solution-version-5-0-admin-guide/313.png)

From the Schedulers field select one of the schedulers defined then press the Add button to display the following image.

<span id="_Toc205380046" class="anchor"></span>Figure 259 - Selecting the Facility Site Where to Run the Scheduler for the Whiteboard

![](bed-management-solution-version-5-0-admin-guide/314.png)

The name of the selected scheduler is displayed in the upper part of the screen. Also, a list of VistA sites is displayed. Select the site(s) where you want the scheduler to run then press the Save button.

#### PPMS

The PPMS tab is for scheduling an extract of in-network Community Care Facilities from an external Provider Profile Management System. These facility records are visible from the Community Care Facility field located in a Patients Pending Bed Placement or Community Care Tracking List record, and can be reviewed via [Community Care Sites](#community-care-sites).

The PPMS job can be scheduled to run as frequently as monthly (or on-demand), but is recommended to run on a quarterly basis.

The PPMS tab is displayed as in the following image:

<span id="_Toc205380047" class="anchor"></span>Figure 260 - PPMS page

![](bed-management-solution-version-5-0-admin-guide/315.png)

If necessary, make changes to the Recurs every, Start Time and Time Zone fields, then press the Save button. If an ad-hoc run of the PPMS job is necessary, select the Run Today checkbox, then press the Save button.

![](bed-management-solution-version-5-0-admin-guide/316.png) The Run Today option kicks off the PPMS job within 5 minutes.

![](bed-management-solution-version-5-0-admin-guide/317.png) Pressing the Clear Schedule button will remove the Next Run Date and Job Status information.

<span id="_Toc205380102" class="anchor"></span>Table 42 - PPMS Parameters

| Column        | Description                                                                                           |
|---------------|-------------------------------------------------------------------------------------------------------|
| Recurs every  | Frequency of PPMS job run by number of months.                                                        |
| Start Time    | Hour and minute when the next PPMS job is schedule to run.                                            |
| Time Zone     | The time zone of the Start Time.                                                                      |
| Run Today     | A checkbox for running the PPMS job one hour after pressing the Save button.                          |
| Next Run Date | The date and time when the PPMS job is scheduled to run.                                              |
| Last Run Date | The date and time when the PPMS job last ran.                                                         |
| Job Status    | The status of the previous PPMS job. Possible values are Not Yet Run, Running, Successful and Failed. |

### Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To access the Application Parameters page, in the Administration Section page click the Application Parameters link.

<span id="_Toc205380048" class="anchor"></span>Figure 261 - Application Parameters Link

![](bed-management-solution-version-5-0-admin-guide/318.png)

The Application Parameters page is displayed as in the following image:

<span id="_Toc52889933" class="anchor"></span>Figure 262 - Application Parameters Page

![](bed-management-solution-version-5-0-admin-guide/319.png)

This page allows the creation and editing of the Clinical Inventory Link and the VHA BMS Nation Patient Placement Alert. Make appropriate changes and press the Submit button.

### User Access Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Administration Section page click the User Access Report link to display BMS logins permissions information.

<span id="_Toc205380050" class="anchor"></span>Figure 263 - User Access Report Link

![](bed-management-solution-version-5-0-admin-guide/320.png)

Within the User Access Report page, use the Visn Ids and Facility fields to narrow your search of qualifying BMS logins. Then press the View Report button.

<span id="_Toc205380051" class="anchor"></span>Figure 264 - User Access Report

![](bed-management-solution-version-5-0-admin-guide/321.png)

The image below presents an example of User Access Report results.

<span id="_Toc205380052" class="anchor"></span>Figure 265 - User Access Report Results

![](bed-management-solution-version-5-0-admin-guide/322.png)

The report can be exported to a series of formats available when clicking the Save button. Once exported, the Print button allows the site user to send the generated report to a printer.

For each entry the following data is available:

<span id="_Toc205380103" class="anchor"></span>Table 43 - User Access Report Parameters

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th>COLUMN</th>
<th>DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>User Name</td>
<td>Windows user who will be given access rights to the BMS system.</td>
</tr>
<tr class="even">
<td>Read</td>
<td>Whether or not the BMS login has Read access assigned.</td>
</tr>
<tr class="odd">
<td>Write</td>
<td>Whether or not the BMS login has Write access assigned.</td>
</tr>
<tr class="even">
<td>REGION NAME</td>
<td>The VA Region associated with the BMS login.</td>
</tr>
<tr class="odd">
<td>VISN NAME</td>
<td>The VISN associated with the BMS login.</td>
</tr>
<tr class="even">
<td>FACILITY NAME</td>
<td>The VA Facility associated with the BMS login.</td>
</tr>
<tr class="odd">
<td>Account Activated Date</td>
<td>The date and time when the account was given BMS role permissions.</td>
</tr>
<tr class="even">
<td>Last Login Date</td>
<td><p>The date and time when the account last logged in to BMS.</p>
<ul>
<li><p>Green – Signifies the account has logged in to BMS within the last 6 months.</p></li>
<li><p><strong>Orange</strong> – Signifies the account has not logged in to BMS between 5-6 months.</p></li>
<li><p><strong>Red</strong> – Signifies the account has not logged into BMS in over 6 months.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Support</td>
<td>Whether or not the BMS login is assigned the Support User role.</td>
</tr>
<tr class="even">
<td>National</td>
<td>Whether or not the BMS login is assigned the National User role.</td>
</tr>
<tr class="odd">
<td>Regional</td>
<td>Whether or not the BMS login is assigned the Regional User role.</td>
</tr>
<tr class="even">
<td>VISN</td>
<td>Whether or not the BMS login is assigned the VISN User role.</td>
</tr>
<tr class="odd">
<td>Admin</td>
<td>Whether or not the BMS login is assigned the Admin User role.</td>
</tr>
<tr class="even">
<td>Audit Log</td>
<td>Whether or not the BMS login is assigned the Audit Log User role.</td>
</tr>
<tr class="odd">
<td>Site</td>
<td>Whether or not the BMS login is assigned the Site User role.</td>
</tr>
<tr class="even">
<td>EMS</td>
<td>Whether or not the BMS login is assigned the EMS User role.</td>
</tr>
<tr class="odd">
<td>EMS Supervisor</td>
<td>Whether or not the BMS login is assigned the EMS Supervisor User role.</td>
</tr>
<tr class="even">
<td>EMS Dispatcher</td>
<td>Whether or not the BMS login is assigned the EMS Dispatcher role.</td>
</tr>
<tr class="odd">
<td>EMS Portal</td>
<td>Whether or not the BMS login only has access to the EMS portal.</td>
</tr>
<tr class="even">
<td>Whiteboard Only Access</td>
<td>Whether or not the BMS login only has access to view the whiteboard.</td>
</tr>
</tbody>
</table>

![](bed-management-solution-version-5-0-admin-guide/323.png)For more information on user roles and configuring BMS logins, refer to the section *Add/Edit BMS User Page* located within this guide.

### National Bed Tracking Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Administration Section page, click the National Bed Tracking Levels link to display and configure unit/ward-based Bed Levels available within the Bed Level Management screen.

<span id="_Toc205380053" class="anchor"></span>Figure 266 – National Bed Tracking Levels Link

![](bed-management-solution-version-5-0-admin-guide/324.png)

![](bed-management-solution-version-5-0-admin-guide/325.png)For more information on Bed Level Management, refer to the Bed Management Solution (BMS) Bed Level Management User Guide. Bed Level Management is intended to replace the 3<sup>rd</sup> party BMS Bed Type Update Tool (also known as the “BED TYPE CROSSWALK”).

Within the National Bed Tracking Levels page, use the Text field and Bed Type mapping drop-down menu to add a new Bed Level. Then press the Add button.

For example, a ‘MED/SURG_TELE’ unit mapped to the MED/SURG Bed Type:

<span id="_Toc205380054" class="anchor"></span>Figure 267 – National Bed Tracking Levels Text Field, Bed Type Mapping and Add Button

![](bed-management-solution-version-5-0-admin-guide/326.png)

<span id="_Toc205380055" class="anchor"></span>Figure 268 – National Bed Tracking Levels Confirmation Screen

![](bed-management-solution-version-5-0-admin-guide/327.png)

Select Return to Listing to go back to the list of Bed Levels. To change the Display Order of a Bed Level value (both in this screen and in the Bed Level Management interface), first click the Edit link:

<span id="_Toc205380056" class="anchor"></span>Figure 269 – National Bed Tracking Levels Edit Link

![](bed-management-solution-version-5-0-admin-guide/328.png)

Then input a number within the DISPLAY ORDER field to numerically sort this Bed Level within the entire Bed Level list.

<span id="_Toc205380057" class="anchor"></span>Figure 270 – National Bed Tracking Levels Display Order Value Update

![](bed-management-solution-version-5-0-admin-guide/329.png)

For example, if you want to order this entry to the bottom of the list, refer to the Display Order value of the last entry (for example, “200” for REHAB MED_PMR-TR), and then use the DISPLAY ORDER field to enter a slightly higher number for the Bed Level in question (e.g., “210” for MED/SURG_TELE).

Press Submit to save your change then Return to Listing to go back to the list of Bed Levels.

<span id="_Toc205380058" class="anchor"></span>Figure 271 – National Bed Tracking Levels Reordered Bed Level

![](bed-management-solution-version-5-0-admin-guide/330.png)

There is also a Delete option per Bed Level. Note that deleting a bed level makes the value unavailable to *all* facilities nationwide. If a Bed Level is in use by one or more beds, an “In Use” message displays in lieu of the Delete link.

<span id="_Toc192005442" class="anchor"></span>Figure 272 – National Bed Tracking Levels In Use Bed Level

![](bed-management-solution-version-5-0-admin-guide/331.png)

![](bed-management-solution-version-5-0-admin-guide/332.png)In rare cases a Bed Level tied to a specific bed could be deleted. In this situation, an “(INACTIVE)” label will display for the bed record in question:

<span id="_Toc205380060" class="anchor"></span>Figure 273 – National Bed Tracking Levels “(INACTIVE)” Bed Level on Bed Level Management Screen

![](bed-management-solution-version-5-0-admin-guide/333.png)

For each entry the following data is available:

<span id="_Toc205380104" class="anchor"></span>Table 44 - National Bed Tracking Levels Parameters

| COLUMN           | DESCRIPTION                                                                                                                                                                                                                                                                     |
|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Level Name       | The unit/ward associated with a bed. Commonly called “bed type”. Can be potential (“Available Bed Level(s)”), normal (“Primary Bed Level”) or current (“Current Bed Level”) unit/ward.                                                                                          |
| Display Order    | A numeric value that determines where a specific Bed Level is ordered within the complete list of Bed Levels. Allows support staff to manually order a Bed Level higher or lower (as opposed to alphabetical ordering) based on importance or frequency of usage, for instance. |
| Bed Type Mapping | The Bed Type associated with the Bed Level. Used for enhanced reporting.                                                                                                                                                                                                        |

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BMS project team is working to develop a frequently asked questions (FAQs) section for this Admin Guide, which will contain user-related troubleshooting tips, known issues, and anomalies. This section will be made available as those items are realized and documented.

## BMS Self-Help Troubleshooting Guide 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BMS Self-Help Troubleshooting Guide is an online resource for BMS application users. This system provides troubleshooting assistance to help end users determine if they are able to resolve their issues independently or if they need to enter a ticket to reach the BMS Sustainment Team or another group. Content will be added and updated as needed to suit the needs of BMS application users at all levels. To use, select an issue category and choose a listed issue to see potential solutions. If a YourIT helpdesk request is required, wording for the specific issue is listed.

[BMS Self-Help Troubleshooting Guide](https://dvagov.sharepoint.com/sites/VHAQPS/OQSV/QPS-SR/SRD/cfmprogram/BMSII/BMSImplement/Lists/BMS/AllItems.aspx)

[User Guide for BMS Self-Help Troubleshooting Guide](https://dvagov.sharepoint.com/sites/VHAQPS/OQSV/QPS-SR/SRD/cfmprogram/BMSII/BMSImplement/bmsselfhelp/Shared%20Documents/BMS_Self-Help-User-Guide_20190905.pdf#search=BMS%5FSelf%2DHelp%2DUser%2DGuide%5F20190905%2Epdf)

1.  

# Appendix A. Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the acronyms defined below, more definitions can be found on the OI&T Master Glossary.

| TERM               | DEFINITION                                                      |
|--------------------|-----------------------------------------------------------------|
| ADT                | Admission, Discharge, and Transfer                              |
| BLM                | Bed Level Management                                            |
| BMS                | Bed Management Solution                                         |
| BN                 | Business Need                                                   |
| BRD                | Business Requirements Document                                  |
| CCTL               | Community Care Tracking List                                    |
| CFM                | Comprehensive Flow Management                                   |
| CH/CL              | Community Hospital / Current Location                           |
| CHF                | Congestive Heart Failure                                        |
| CLC                | Community Living Center                                         |
| COW                | Computer on Wheels                                              |
| CPRS               | Computerized Patient Record System                              |
| CCTL               | Community Care Tracking List                                    |
| D/C                | Discharge                                                       |
| DM                 | Diabetes Mellitus                                               |
| DOB                | Date of Birth                                                   |
| DOM                | Domiciliary                                                     |
| DRG                | Diagnostic Related Group                                        |
| DUSH               | Deputy Under Secretary for Health                               |
| ED                 | Emergency Department                                            |
| EMS                | Environmental Management Service                                |
| EMSHG              | Emergency Management Strategic Healthcare Group                 |
| ERR                | Enterprise Requirements Repository                              |
| FAQs               | Frequently Asked Questions                                      |
| FIPS               | Federal Information Processing Standard                         |
| GUI                | Graphical User Interface                                        |
| HAvBED             | Hospital Available Beds for Emergencies & Disasters             |
| HVAC               | House Veterans Affairs Committee                                |
| ICU                | Intensive Care Unit                                             |
| IEN                | Internal Entry Number. The primary keys for VistA files.        |
| IT                 | Information Technology                                          |
| LOS                | Length of Stay                                                  |
| MDWS               | Medical Domain Web Service                                      |
| M (MUMPS)          | Massachusetts General Hospital Utility Multi-Programming System |
| NIST               | National Institute of Standards and Technology                  |
| NUMA               | Nursing Unit Mapping Application                                |
| NUMI               | National Utilization Management Integration                     |
| ODBC               | Open Database Connectivity                                      |
| OED                | Office of Enterprise Development                                |
| OOS                | Out of Service                                                  |
| OI&T               | Office of Information and Technology                            |
| PICC               | Peripherally Inserted Central Catheter                          |
| PPMS               | Provider Profile Management System                              |
| PT                 | Patient                                                         |
| SSN                | Social Security Number                                          |
| Service Era or ERA | The period of service that the patient served.                  |
| STAT               | Indicates an emergent or extremely urgent situation             |
| TAG                | Flow Improvement Technical Advisory Group                       |
| UM                 | Utilization Management                                          |
| VA                 | Department of Veterans Affairs                                  |
| VAMC               | VA Medical Center                                               |
| VHA                | Veterans Health Administration                                  |
| VDIF               | Veterans Data Integration and Federation                        |
| VIA                | VistA Integration Adapter                                       |
| VISN               | Veterans Integrated Service Network                             |
| VistA              | Veterans Health Information Systems and Technology Architecture |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add/Edit BMS User Page 108
Add/Edit Icon Page 121
Audit Log Report Page 73
Background Processors Page 60
Bed Board BMS Orderable Items Configuration Page 21
Bed Board Discharge Appointment Clinic Configuration Page 48
Bed Board Site Unavailable Reason Page 41
Bed Management Board Icons Page 72
Contingency Settings 87
Edit BMS Facility Settings Page 113
Edit Sister Sites Page 120
EMS Portal Access Page 36
Evacuation On/Off 89, 90
Events Notifications Page 51
Icon Usage Report 70
Log in to the Administration Section Page 106
Maintain Marquee Text Page 107
National Unavailable Reason 155
National Waiting Area 150
Site Configurable Icons Page 58
Treating Specialty/NUMA/HAvBED Edit Page 146
View Audit Log Page – Support 132
VistA Ward Add/Edit Page 14
