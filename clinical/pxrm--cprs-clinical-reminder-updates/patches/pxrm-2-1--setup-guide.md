---
title: PXRM*2*1 Integration with Women's Health Reminders Installation and Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: Integration with Women's Health Reminders Installation and
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*1
group_key: "PXRM:PXRM:2"
file_numbers: 
  - 71
  - 100
  - 790
security_keys: []
menu_options: 1
description: ![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/001.png)
audience: 
keywords: 
  - blockquote
  - strong
  - reminder
  - class
  - mammogram
  - table
  - style
  - width
  - health
  - colgroup
page_count: 0
word_count: 21596
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 7
has_toc: False
is_stub: False
pub_date: February 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_1_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_1_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/001.png)

> Clinical Reminders

> CPRS: Integration with Women’s Health

## Patches: PXRM\*2.0\*1 WV\*1.0\*16 LR\*5.2\*311 OR\*3.0\*210

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> INSTALLATION and SETUP GUIDE

> February 2005

> Updated March 2005

#### Health Data Systems

> V*IST*A HSD&D

#### Department of Veterans Affairs

> Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 24%" />
<col style="width: 57%" />
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
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>March 25,</p>
<p>2005</p>
</blockquote></td>
<td><blockquote>
<p><u>15</u></p>
</blockquote></td>
<td><blockquote>
<p>Modified step 9, to remove printing to a printer. Added the following text:</p>
<p>“Do not queue the installation. Because the installation contains questions requiring responses, queuing will stop the installation.”</p>
</blockquote></td>
</tr>
</tbody>
</table>

This Manual and Related Documentation 6

1.  [Set up Women’s Health Package 22](#Set_up_Women’s_Health_Package)
2.  [Map local findings to the national Reminder Terms. 37](#Map_terms)
3.  [Run the Reminder Test option after term definition mapping is completed 47](#_bookmark15)
4.  [Use the Reminder Dialog options to edit the national (exported) dialogs. 48](#Edit_Dialogs)
5.  [Verify that the reminders function properly 52](#Test_Reminders)
6.  [Add the nationally distributed reminders to the CPRS Cover Sheet 54](#_bookmark18)
7.  [Set up entries in the WV Notification Purpose file 56](#_bookmark19)
8.  [Determine how and where letters will be printed. 56](#_bookmark19)
9.  [Verify that the dialogs function properly 57](#Test_Dialogs)
10. [Activate alerts 61](#Activate_Alerts)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Introduction" class="anchor"></span><strong>Overview of the WH Reminders Project</strong></p>
</blockquote>
<p>This WH Reminders project provides a combined build consisting of the following Install(s):</p>
<p>WV*1.0*16 LR*5.2*311 OR*3.0*210 PXRM*2.0*1</p></th>
<th><blockquote>
<p><strong>Background to “CPRS: Integration with Women’s Health” Project</strong></p>
<p>The CPRS: Integration with Women’s Health project has been designed to fulfill the following VHA policy.</p>
<p>“It is VHA policy to provide a nationwide tracking system to ensure that consistent mammography and cervical screening follow-up is achieved and that patients have been properly notified of the test results.”</p>
<p>To meet the data requirements of this policy, the Women’s Health software was developed (Indian Health Service software was modified to be consistent with VA policy and VistA architecture). However, none of the information contained within the WH software interfaces with CPRS.</p>
<p>Therefore, it is the goal of the Women’s Veterans Health Program to enable CPRS, in its existing Clinical Reminders package, to interface with the Women’s Health VistA package. CPRS: Integration with Women’s Health (referred to in this manual as WH Reminders) accomplishes this goal.</p>
<p><strong>Benefits:</strong></p>
</blockquote>
<ul>
<li><p>Enables capture of a greater percentage of data than is currently entered into the Women’s Health VistA package.</p></li>
<li><blockquote>
<p>Eliminates the duplication of entering the identical data into both systems, while still allowing the Women’s Health package to perform its tracking and notification functions.</p>
</blockquote></li>
<li><blockquote>
<p>Significantly reduces discrepancies between WH data and data collected by Clinical Reminders.</p>
</blockquote></li>
<li><blockquote>
<p>Results in a signed progress note documenting the WH Mammogram and Pap Smear-related care and patient notifications.</p>
</blockquote></li>
</ul>
<blockquote>
<p>The data captured will be used to automatically update the Women’s Health package, which allows continuation of Women’s Health Software reporting functionality.</p>
<p>The Mammogram Screening reminder replaces the following national reminders relating to mammograms and breast cancer screening:</p>
<p>VA-*BREAST CANCER SCREEN - rescinded 12/15/2003</p>
<p>VA-MAMMOGRAM - rescinded 12/15/2003</p>
<p>The Pap Screening reminder replaces the following national reminders relating to PAP smears and cervical cancer screening:</p>
<p>VA-*CERVICAL CANCER SCREEN VA-PAP SMEAR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Description of patches in build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### CPRS: Integration with Women’s Health is distributed in a combined build that consists of the following patches: PXRM\*2.0\*1, WV\*1.0\*16, LR\*5.2\*311, and OR\*3.0\*210.

> PXRM\*2.0\*1 adds four new reminders and dialogs, several new/revised taxonomies, and many new reminder terms, health factors, and computed findings to support the CPRS Integration with Women’s Health project. There are also several new entries for the WV NOTIFICATION PURPOSE file that need to be installed so references to these notifications can be resolved during reminder installation.

> The patch installation takes advantage of the reminder exchange utility and installs the reminders into the host system “silently.” During reminder installation, you may be prompted for orders – you will need to substitute your local quick orders. See the table in the setup section for quick orders that are needed.

> WV\*1.0\*16

> This patch adds functionality that allows the Women's Health (WH) package to send data to the Clinical Reminders (CR) package to resolve Mammogram and Pap Smear reminders. Also, the CR package will be able to send data to the WH package to update the WH database.

> Patch 16 introduces a new option, Link Pap Smear with SNOMED Codes \[WV PAP SMEAR SNOMED CODES\], which is added to the File Maintenance Menu, and also modifies several options: Edit Site Parameters \[WV EDIT SITE PARAMETERS\] option adds two new prompts: Update Result/Dx Field? and Update Treatment Needs? The Add/Edit a Notification Purpose & Letter \[WV ADD/EDIT NOT PURPOSE&LETTER\] option is modified to add four new prompts.

> See Appendix D for complete details about the changes introduced by Patch 16.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NOTE: All alerts are exported in a disabled state; sites will need to go into the CPRS Manager Menu (CPRS Configuration (Clin Coord)/Notification Mgmt Menu) to enable these alerts – at a system, site, location, or individual level.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Description of patches in build, cont’d</strong></p>
<p><strong>LR*5.2*311</strong></p>
</blockquote>
<ol type="1">
<li><p>Currently the ADD^LRWOMEN utility notifies a Women's Health package utility whenever a Cytology or Surgical Pathology report is verified for a female patient. This functionality was provided with LR*5.2*231.</p></li>
</ol>
<blockquote>
<p>After installation of patch LR*5.2*311, the ADD^LRWOMEN utility will also notify a new CPRS utility (LAB^ORB3LAB) for all patients, not just female patients. Integration Agreement #4287 grants the LABORATORY package permission to call the ORB3LAB routine.</p>
</blockquote>
<ol start="2" type="1">
<li><p>The code in the MOVE entry point of the LRWOMEN routine was replaced with a QUIT command. With the release of LR*5.2*259, this entry point is no longer called. The entry point will be deleted in a future patch.</p></li>
</ol>
<blockquote>
<p><strong>OR*3.0*210</strong> adds three new notification/alerts:</p>
<p>#69 - Mammogram Results #70 - Pap Smear Results</p>
<p>#71 - Anatomic Pathology Results</p>
<p>All three alerts are informational (no follow-up action). Alerts 69 and 70 are sent to providers and/or designated recipients when radiology and lab results are available. Alert 71 (Anatomic Pathology Results) will be sent to the practitioner requesting the AP procedure if that user has the notification/alert enabled (turned on). Alerts 69 and 70 are triggered within the Women's Health package and are intended to support that package. Alert 71 is triggered within the Lab package.</p>
<p>These notification/alerts are exported with a deletion parameter value of “Individual Recipient.” This means the alert will be deleted for each recipient individually.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="_bookmark2" class="anchor"></span>These steps are described in more detail in the Setup section of this manual</p>
</blockquote></th>
<th><blockquote>
<p><strong>Impact on Sites</strong></p>
</blockquote>
<ul>
<li><p><strong>Setup and implementation by local team</strong></p></li>
</ul>
<blockquote>
<p>The following steps are required after the reminders have been installed on the system:</p>
</blockquote>
<ol type="1">
<li><p>Sites will need to determine if the review reminders should be released to the field. If a site is not set up for automatic update of WH, these reminders will not come due, so releasing the review reminders and dialogs might be confusing.</p></li>
</ol>
<blockquote>
<p>The VA-WH PAP SMEAR REVIEW RESULTS reminder</p>
<p>will only come due if all of the following are true:</p>
</blockquote>
<ul>
<li><p>PAP smear results are recorded and verified in VistA Lab package</p></li>
<li><p>VistA Lab package uses SNOMED codes</p></li>
<li><p>WH package has SNOMED codes mapped to the codes used by the VistA Lab package</p></li>
<li><p>WH parameters are set up to automatically receive VistA Lab results when the PAP smear procedure is verified and released</p></li>
</ul>
<blockquote>
<p>The VA-WH MAMMOGRAM REVIEW RESULTS reminder</p>
<p>will only come due if all of the following are true:</p>
</blockquote>
<ul>
<li><p>Mammogram results are recorded and verified in VistA Radiology package</p></li>
<li><p>WH parameters are set up to automatically receive VistA Radiology results when the mammogram procedure is verified and released, and status of received mammogram result is set to OPEN</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>These steps are described in more detail in the Setup section of this manual.</p>
<p><strong>TIP:</strong></p>
<p>We strongly</p>
</blockquote>
<p> recommend that you complete the</p>
<blockquote>
<p>Pre-Installation Worksheet on Page 12 before installing the software.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Impact on Sites</strong></p>
</blockquote>
<ul>
<li><p><strong>Setup and implementation by local team, cont’d</strong></p>
<ol start="2" type="1">
<li><p>Clinicians and CPRS/Reminder CACs will need to be informed about the new reminders and dialogs, the procedure clinical interpretation updates, and new patient notification tracking features.</p></li>
<li><p>Reminder CACs will need to map certain national Reminder Terms to identify local processing for documenting Pap Smears and Mammograms in PCE.</p></li>
<li><p>Reminder CACs will need to create quick orders for PAP smears and Mammograms, if needed. If these orders are created prior to reminder installation, sites will be able to associate their local orders with the dialogs at the time of installation. If the orders are not created before, sites will have to edit the reminder dialogs after installation to add references to local orders.</p></li>
<li><p>The Women’s Health Case Manager will need to understand the impact on WH files and the impact on the case manager’s normal work processing due to WH data entered from the CPRS GUI. This project updates some data in the WH package, not all of it. A case manager will be required to set up parameters and to monitor printing of notifications.</p></li>
<li><p>Reminder CACs and Women’s Health Case Managers will need to agree on notification methods, printers, etc., and set these up, as needed.</p></li>
</ol></li>
</ul>
<blockquote>
<p>See the Pre-Installation Worksheet on Page 12; this should be completed before installing the combined build for this project.</p>
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
<p><span id="_bookmark3" class="anchor"></span><strong>Purpose of This Guide</strong></p>
</blockquote></th>
<th><blockquote>
<p>This Installation and Setup Guide is designed to help you prepare your site for the installation and implementation of the Women’s Health Reminders. It includes detailed information such as system requirements, installation time estimates and instructions, and procedures that will get you up and running with this project.</p>
<p><strong>Our Target Audience</strong></p>
<p>We have developed this guide for the following individuals, who are responsible for installing, supporting, maintaining, and testing this package:</p>
</blockquote>
<ul>
<li><p>Information Resources Management (IRM)</p></li>
<li><p>Clinical Application Coordinator (CAC)</p></li>
<li><p>Enterprise <strong>V</strong><em>IST</em><strong>A</strong> Support (EVS)</p></li>
<li><p>Software Quality Assurance (SQA)</p></li>
</ul>
<blockquote>
<p><strong>Documentation Retrieval</strong></p>
<p>Your site can retrieve the Clinical Reminders V. 2.1 documentation from the Anonymous directories. The preferred method is to “FTP” the files from <a href="ftp://ftp.fo-slc.med.va.gov/"><strong>download.vista.med.va.gov</strong></a>. This location automatically transmits files from the first available FTP Server to the appropriate directory on your system. Use binary mode.</p>
<p><strong>Note:</strong> If you prefer, you can retrieve the software <em>directly</em> from one of the FTP Servers, listed below, under the FTP Address column.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Other Sources of Information</strong></p>
</blockquote></td>
<td><blockquote>
<p>You can also retrieve documentation from the following websites: <a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a> Clinical Reminders Main Web page. <a href="http://www.va.gov/vdl"><u>http://www.va.gov/vdl</u></a> the <strong>V</strong><em>IST</em><strong>A</strong> Documentation Library (VDL).</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/002.png)![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/003.png)![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/004.png)![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/005.png)![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/006.png)![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/007.png)FTP Addresses Available for Downloading Clinical Reminders Documentation

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 40%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>OI Field Office</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FTP Address</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Directory</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Albany</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/008.png)

# Pre-Installation Information 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Patches: PXRM\2.0\1 WV\1.0\16 LR\5.2\311 OR\3.0\210](#patches-pxrm201-wv1016-lr52311-or30210)
  - [Description of patches in build](#description-of-patches-in-build)
- [Pre-Installation Information](#pre-installation-information)
  - [Pre-Install Worksheet](#pre-install-worksheet)
    - [Pap Smear Terms](#pap-smear-terms)
    - [VA FileMan Print from the Reminder Term File](#va-fileman-print-from-the-reminder-term-file)
- [Appendix B: Key Points to WH Reminders Installation and Setup](#appendix-b-key-points-to-wh-reminders-installation-and-setup)
- [Appendix C: Reminders Installation with Reminder Exchange Utility](#appendix-c-reminders-installation-with-reminder-exchange-utility)
- [Appendix E: Setting up Notification Letters](#appendix-e-setting-up-notification-letters)
    - [Step 1 – Edit default letter (one time only)](#step-1-edit-default-letter-one-time-only)
    - [Step 2 – Edit/customize each individual notification letter (at least one time for each letter)](#step-2-editcustomize-each-individual-notification-letter-at-least-one-time-for-each-letter)
    - [Adding a new Dialog Element/Purpose of Notification](#adding-a-new-dialog-elementpurpose-of-notification)
<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Minimum Required Packages</strong></p>
</blockquote></th>
<th><blockquote>
<p>Before installing the WH Reminders build, make sure that your system includes the following software packages and versions (those listed or higher).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>
> ![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/009.png)Minimum Required Packages and Versions
<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 20%" />
<col style="width: 28%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>MINIMUM VERSION NEEDED</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Required Patches</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Clinical Reminders</strong></p>
</blockquote></td>
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td>2.0</td>
<td><blockquote>
<p>PXRM*1.5*12</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>CPT</strong></p>
</blockquote></td>
<td><blockquote>
<p>ICPT</p>
</blockquote></td>
<td><blockquote>
<p>6</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>HL7</strong></p>
</blockquote></td>
<td><blockquote>
<p>HL</p>
</blockquote></td>
<td>1.6</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>ICD</strong></p>
</blockquote></td>
<td><blockquote>
<p>ICD</p>
</blockquote></td>
<td><blockquote>
<p>18</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Kernel</strong></p>
</blockquote></td>
<td></td>
<td>8.0</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Lexicon</strong></p>
</blockquote></td>
<td><blockquote>
<p>LEX</p>
</blockquote></td>
<td>2.0</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>MailMan</strong></p>
</blockquote></td>
<td><blockquote>
<p>XM</p>
</blockquote></td>
<td>8.0</td>
<td><blockquote>
<p>XM*8.0*16 –</p>
<p>Mailman/HL7 Messaging</p>
<p>XM*DBA*154</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Order Entry</strong></p>
<p><strong>/Results Reporting</strong></p>
</blockquote></td>
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td>3.0</td>
<td><blockquote>
<p>OR*3.0*195</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Radiology/Nuclear Medicine</strong></p>
</blockquote></td>
<td><blockquote>
<p>RA</p>
</blockquote></td>
<td>5.0</td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Text Integration Utilities</strong></p>
</blockquote></td>
<td><blockquote>
<p>TIU</p>
</blockquote></td>
<td>1.0</td>
<td><blockquote>
<p>TIU*1.0*112</p>
<p>TIU*1.0*113</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA FileMan</strong></p>
</blockquote></td>
<td><blockquote>
<p>DI</p>
</blockquote></td>
<td>22.0</td>
<td></td>
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
<p><strong>Installation Time Estimates</strong></p>
<p>NOTE: You should</p>
</blockquote>
<p> install and test the CPRS-WH combined</p>
<blockquote>
<p>build in your test accounts <em><strong>before</strong></em> installing in your production accounts.</p>
</blockquote></th>
<th><blockquote>
<p>On average, it takes approximately fifteen minutes to install PXRM V. 2.0*1 and the combined build. This estimate was provided by a few of our beta test sites. Actual times may vary, depending on how your site is using its system resources.</p>
<p>Suggested time to install: non-peak requirement hours. During the install process, Clinical Reminders users should not be accessing the Software.</p>
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
<p><span id="Files_Required_to_Run_the_WH_Reminders_a" class="anchor"></span><strong>Files Required to Run the WH Reminders application</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Files installed</strong></p>
<p>790.02 WV SITE PARAMETER</p>
<p>790.1 WV PROCEDURE</p>
<p>790.2 WV PROCEDURE TYPE</p>
<p>790.404 WV NOTIFICATION PURPOSE</p>
<p>100.9 OE/RR NOTIFICATIONS</p>
</blockquote>
<ol start="41" type="1">
<li><p>REMINDER DIALOG</p></li>
<li><blockquote>
<p>REMINDER GUI PROCESS</p>
</blockquote></li>
</ol>
<blockquote>
<p>801.45 REMINDER FINDING TYPE PARAMETER</p>
<p>811.8 REMINDER EXCHANGE FILE</p>
<p>Note: You can learn more about these files by generating a list with file attributes using VA FileMan.</p>
<p><strong>Pre and Post-Install Routines Installed</strong></p>
<p>PXRMCWH PXRMWHPI PXRMWHEV</p>
<p>PXRMWHPI has both the pre and post-install calls: PRE-INIT ROUTINE : PRE^PXRMWHPI</p>
<p>POST-INIT ROUTINE : POST^PXRMWHPI</p>
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
<p><span id="Routines_Installed" class="anchor"></span><strong>Routines Installed</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Note:</strong> You can use the <em>Kernel First Line Routine Print</em> [XU FIRST LINE PRINT] option to print a list containing the first line of each PXRM routine.</p>
<p><strong>Routine Mapping</strong></p>
<p>At this time, we do <em>not</em> offer any recommendations for routine mapping. However, if you choose to map the Clinical Reminders V.</p>
<p>2.0 package routines, you will need to bring your system down, and then restart it to load the new routines into memory.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Pre-Install Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> During the installation of the combined build, you will be prompted for many Order Dialog names, since these can’t be installed via KIDS. To make this easier, we recommend that you complete the worksheet below prior to the install. Fill in the blanks with Order Dialog names – either ones that already exist at your site, or placeholders until you can create appropriate order dialog elements. Coordination among ADPACs, CACs, and representatives from Radiology, Women’s Health, and Clinical Reminders will help facilitate this.

> Suggestion: You may want to create one dummy quick order, use it for every quick order prompt during the installation, and then replace the dummy orders with actual quick orders later.

> The WV Notification Purpose file should be installed before the reminders (i.e., so the dialogs can find the entries they need at load time.

> Example prompt

> Pre-Install Worksheet

> This chart should be used as a worksheet by the CAC prior to the installation.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 32%" />
<col style="width: 20%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Reminder</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Dialog Element</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>File Reference for Entry</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Your dialog entry</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>VA-WH MAMMOGRAM</strong></p>
<p><strong>REVIEW RESULTS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Q.WH BREAST ULTRASOUND- UNILATERAL</p>
</blockquote></td>
<td><blockquote>
<p>Quick Order in Order file #100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Q.WH BREAST ULTRASOUND - BILATERAL</p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Q.WH MAMMOGRAM -</p>
<p>UNILATERAL</p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Q.WH MAMMOGRAM -</p>
<p>BILATERAL</p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-WH MAMMOGRAM</strong></p>
<p><strong>SCREENING</strong></p>
</blockquote></td>
<td><blockquote>
<p>RP.MAMMOGRAM BILAT</p>
</blockquote></td>
<td><blockquote>
<p>Rad/Nuc Med Procedure file #71</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>RP.MAMMOGRAM BILAT</p>
<p>SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>Rad/Nuc Med</p>
<p>Procedure file #71</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>RP.MAMMOGRAM UNILAT</p>
</blockquote></td>
<td><blockquote>
<p>Rad/Nuc Med Procedure file #71</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>RP.MAMMOGRAM BILAT</p>
</blockquote></td>
<td><blockquote>
<p>Rad/Nuc Med</p>
<p>Procedure file #71</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>RP.MAMMOGRAM UNILAT</p>
</blockquote></td>
<td><blockquote>
<p>Rad/Nuc Med</p>
<p>Procedure file #71</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Q.WH REFER TO WOMEN'S HEALTH CLINIC</p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Q.WH MAMMOGRAM -</p>
<p>UNILATERAL</p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>Q.WH MAMMOGRAM - BILATERAL</p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Q.WH MAMMOGRAM –</p>
<p>BILATERAL <u>SCREEN</u></p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-WH PAP SMEAR REVIEW RESULTS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Q.WH CERVICAL ORDERS</p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Q.WH PAP SMEAR REPEAT CONSULT</p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td><blockquote>
<p><strong>Consult – repeat PAP smear</strong></p>
<p><strong>Consult – colposcopy</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-WH PAP SMEAR SCREENING</strong></p>
</blockquote></td>
<td><blockquote>
<p>Q.WH REFER TO WOMEN'S</p>
<p>HEALTH CLINIC</p>
</blockquote></td>
<td><blockquote>
<p>Order file #100</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="Installation" class="anchor"></span>Installation Order:

> Install the software in this order:

> PXRM\*1.5\*12 CR Index Global

> PXRM\*2.0 Clinical Reminders v2.0 WV_PXRM_CPRS_INTEGRATION.KID Combined build

> This Global Transport contains patches: WV\*1.0\*16

> LR\*5.2\*311 OR\*3.0\*210 PXRM\*2.0\*1

> *The install needs to be done by a person with DUZ(0) set to "@."*

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Installation_Instructions" class="anchor"></span><strong>Installation Instructions</strong></p>
<p><strong>IMPORTANT:</strong></p>
<p>You should install and test Clinical Reminders 2.0..1 in your test accounts <em><strong>before</strong></em> installing in your production accounts.</p>
</blockquote></th>
<th><blockquote>
<p>Perform the steps that follow to download the combined build, WV_PXRM_CPRS_INTEGRATION.KID from an FTP Server. Then you will be ready to use this section for loading the Kernel Installation &amp; Distribution System (KIDS) Distribution file, and for installing PXRM V. 2.0 on to the VISTA Server.</p>
<p><strong>Task 1: Download WV_PXRM_CPRS_INTEGRATION Software</strong></p>
<p><strong>1.</strong> Download the Host File WV_PXRM_CPRS_INTEGRATION.KID from an FTP Server using an address listed in the table below.</p>
</blockquote>
<p>The preferred method is to “FTP” the files from <mark>REDACTED</mark></p>
<blockquote>
<p>. This location automatically transmits files from the <em>first</em> available FTP Server. (See the order listed below under the FTP Address column).</p>
</blockquote>
<ul>
<li><p>.EXE or .PDF files need to be FTP in BINARY.</p></li>
<li><p>KIDS Build needs to be FTP in ASCII.</p></li>
</ul>
<blockquote>
<p><strong>Note:</strong> If you prefer, you can retrieve the software <em>directly</em> from one of the FTP Servers, listed below, under the FTP Address column.</p>
<p><strong>2.</strong> Move the files to the appropriate directory on your system.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/010.png)![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/011.png)Example: FTP Addresses Available for Downloading WV_PXRM_CPRS_INTEGRATION.KID Software

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 40%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>OI Field Office</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FTP Address</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Directory</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Albany</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
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
<p><span id="Task_2:_Load_the_KIDS_Distribution_File" class="anchor"></span><strong>V</strong><em>IST</em><strong>A Server Installation Instructions (cont.)</strong></p>
<p>Suggested time to install: non-peak requirement hours.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Task 2: Load the KIDS Distribution File</strong></p>
<p>Perform the steps listed below to load the KIDS Distribution file.</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Sign in to the UCI where the KIDS Distribution file will be loaded and PXRM V. 2.0*1 will be installed.</p>
</blockquote></li>
<li><blockquote>
<p>At the “Select OPTION NAME:” prompt, type <strong>XPD MAIN</strong>, and then press <strong>ENTER</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>At the “Select Kernel Installation &amp; Distribution System Option:” prompt, type <strong>INSTALL</strong>ation, and then press <strong>ENTER</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>At the “Select Installation Option:” prompt, type <strong>Load a Distribution,</strong> and then press <strong>ENTER</strong> to prepare for loading the KIDS Distribution file.</p>
</blockquote></li>
<li><p>At the “Enter a Host File:” prompt, type <strong>the directory where you have stored the Host File</strong>, followed by <strong>WV_PXRM_CPRS_INTEGRATION.KID</strong>. Then press <strong>ENTER</strong>.</p></li>
<li><blockquote>
<p>At the “Want to Continue with Load YES//?” prompt, press</p>
</blockquote></li>
</ol>
<blockquote>
<p><strong>ENTER</strong>. The system then loads the file to this location.</p>
<p><strong>Task 3: Install WV_PXRM_CPRS_INTEGRATION</strong></p>
<p>During the install process, Clinical Reminders users should not be accessing the software.</p>
</blockquote>
<ol type="1">
<li><p>Request that all Clinical Reminders users log off CPRS.</p></li>
<li><p>Review mapped sets for PXRM* namespaces.</p></li>
<li><p>If the routines are mapped, remove them from the mapped set at this time.</p></li>
<li><p>Back up your system. This step is optional, but recommended.</p></li>
<li><p>At the “Select INSTALL NAME:” prompt, type WV*1.0*16 and then press enter to install the combined build.</p></li>
</ol></th>
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
<p><strong>Installation Instructions (cont.)</strong></p>
<p><strong>NOTE:</strong></p>
<p><strong>Do NOT queue the installation!</strong></p>
<p><strong>Because this installation contains questions requiring responses, queuing will stop the installation.</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Task 3: Install WV_PXRM_CPRS_INTEGRATION (cont.)</strong></p>
</blockquote>
<ol start="6" type="1">
<li><p>At the “Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//” prompt, type NO, and then press enter.</p></li>
<li><p>At the “Want KIDS to INHIBIT LOGONs during the install? YES//” prompt, type NO, and then press enter.</p></li>
<li><p>At the “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” prompt, type YES.</p></li>
</ol>
<blockquote>
<p>When asked what options to put out of order, respond with: GMTS*</p>
<p>PXRM*</p>
<p>IBDF PRINT*</p>
<p>OR CPRS GUI CHART</p>
<p>ORS HEALTH SUMMARY</p>
<p>When asked what protocols to place out of order, respond with: ORS AD HOC HEALTH SUMMARY</p>
<p>ORS HEALTH SUMMARY</p>
<p>PXRM PATIENT DATA CHANGE</p>
</blockquote>
<ol start="9" type="1">
<li><p>At the “DEVICE:” prompt, press enter to use the default device HOME (the screen) for printing the Installation message.</p></li>
</ol>
<blockquote>
<p>10 If routines were unmapped as part of the installation process, return them to the mapped set once the installation of PXRM* 2.0*1 is completed.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### NOTE See Appendix C for an example of installing missing reminders or dialogs through Reminders Exchange

2.  Using the Term Inquiry option on the Term Management Menu, verify that the following terms are on your system:

> Mammogram Terms

1.  VA-TERMINAL CANCER PATIENT
2.  VA-WH BILATERAL MASTECTOMY
3.  VA-WH BREAST CARE ORDER HEALTH FACTOR
4.  VA-WH HX BREAST CANCER/ABNORMAL MAM
5.  VA-WH MAMMOGRAM ORDER
6.  VA-WH MAMMOGRAM PENDING REVIEW
7.  VA-WH MAMMOGRAM SCREEN DEFER
8.  VA-WH MAMMOGRAM SCREEN DONE
9.  VA-WH MAMMOGRAM SCREEN FREQ - 1Y
10. VA-WH MAMMOGRAM SCREEN FREQ - 2Y
11. VA-WH MAMMOGRAM SCREEN FREQ - 4M
12. VA-WH MAMMOGRAM SCREEN FREQ - 6M
13. VA-WH MAMMOGRAM SCREEN IN RAD PKG
14. VA-WH MAMMOGRAM SCREEN IN WH PKG
15. VA-WH MAMMOGRAM SCREEN NOT INDICATED
16. VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG

### Pap Smear Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VA-WH HX CERVICAL CANCER/ABNORMAL PAP
2.  VA-WH HYSTERECTOMY
3.  VA-WH PAP SMEAR DONE
4.  VA-WH PAP SMEAR OBTAINED
5.  VA-WH PAP SMEAR ORDER
6.  VA-WH PAP SMEAR ORDER HEALTH FACTOR
7.  VA-WH PAP SMEAR PENDING REVIEW
8.  VA-WH PAP SMEAR SCREEN DEFER
9.  VA-WH PAP SMEAR SCREEN FREQ - 1Y
10. VA-WH PAP SMEAR SCREEN FREQ - 2Y
11. VA-WH PAP SMEAR SCREEN FREQ - 3Y
12. VA-WH PAP SMEAR SCREEN FREQ - 4M
13. VA-WH PAP SMEAR SCREEN FREQ - 6M
14. VA-WH PAP SMEAR SCREEN IN LAB PKG
15. VA-WH PAP SMEAR SCREEN IN WH PKG
16. VA-WH PAP SMEAR SCREEN NOT INDICATED

### VA FileMan Print from the Reminder Term File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### You can also run a VA FileMan Print from the Reminder Term File (#811.5) that sorts by name, and then prints name, finding, and condition. This is a useful list, especially when needing to map many tests and you're not sure what values have been defined.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>c. (cont’d) Verify that the WH dialogs are installed on your system.</strong></p>
<p><strong>NOTE</strong>: Do not autogenerate dialogs for the reminders. Dialogs are included with the packed reminder installation.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p><strong>Dialog List</strong> Jan 23, 2004@09:59:11 Page: 12 of 13 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)</p>
<p>+Item Reminder Dialog Name Source Reminder Status</p>
</blockquote>
<ol start="189" type="1">
<li><p>VA-WH MAMMOGRAM REVIEW RESULTS VA-WH MAMMOGRAM REVIEW RE Linked</p></li>
<li><p>VA-WH MAMMOGRAM SCREENING VA-WH MAMMOGRAM SCREENING Linked</p></li>
<li><p>VA-WH PAP SMEAR REVIEW RESULTS VA-WH PAP SMEAR REVIEW RE Linked</p></li>
<li><p>VA-WH PAP SMEAR SCREENING VA-WH PAP SMEAR SCREENING Linked</p></li>
<li><p>VA-WV TEST ORDERS ZZ-WH ABNORMAL PAP SMEAR</p></li>
<li><p>VIAGRA (SILDENAFIL) INITIATION Test Linked</p></li>
<li><p>WPBTEST WPBTEST <u>Disabled</u></p></li>
</ol></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><strong>+ Enter ?? for more actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Find Next ‘VA WH’? Yes// <strong>no</strong></p>
</blockquote></td>
</tr>
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
<p><span id="Setup_Guide" class="anchor"></span><strong>Setup Overview</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Project Goals</strong></p>
</blockquote>
<ul>
<li><blockquote>
<p>Enable CPRS GUI to interface with the Women’s Health (WH) VistA package</p>
</blockquote></li>
<li><blockquote>
<p>Update Pap Smear and Mammogram screening reminders</p>
</blockquote></li>
<li><blockquote>
<p>Provide review reminders that store clinical review results in the WH package.</p>
</blockquote></li>
</ul>
<blockquote>
<p>Review reminders will only work if the data automatically updates WH from the Lab and Radiology package (requires setup in WH package). Procedures entered manually into WH will not make the review reminders due.</p>
</blockquote>
<ul>
<li><blockquote>
<p>Provide dialogs for the screening and review reminders clinicians can use to document PAP &amp; mammogram procedures</p>
</blockquote></li>
</ul>
<blockquote>
<p>The VA-WH reminders have been developed to interface with the Women’s Health package. The associated reminder dialogs will update the WH package at the same time that clinical care is recorded in CPRS GUI, thus eliminating the need for dual data entry.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

####### February 2005 CPRS: Integration with Women’s Health Installation Guide 20

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Package</strong></p>
<p><strong>NOTE:</strong></p>
<p>Your site can choose whether to include the Print Now checkbox on review reminder dialogs. This can be set with a new option on the CPRS Reminder Configuration menu: PXRM WH PRINT NOW</p>
<p>The default will be not to display the Print Now checkbox.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Overview of Women’s Health Package</strong></p>
<p><em>Patient Management</em> - manage individual patient care</p>
</blockquote>
<ul>
<li><p>Maintain date of the next procedure (PAP smear &amp; mammogram)</p></li>
<li><p>Track the patient's individual procedures: the date performed, the provider and clinic, the results or diagnosis</p></li>
<li><p>Track notifications (letters, in person, phone calls)</p></li>
<li><p>Maintain a file of form letters that may be edited and personalized for a clinic's particular needs</p></li>
<li><p>Queue reminder letters months in advance of a future appointment, print and mail shortly before the tentative appointment</p></li>
</ul>
<blockquote>
<p><em>Manager’s Functions</em> - provide the ADPAC with a set of utilities for configuring the software to the specific needs of the site</p>
</blockquote>
<ul>
<li><p>Maintain site-specific parameters</p></li>
<li><p>Maintain the text of form letters and notifications</p></li>
<li><p>Print notification letters</p></li>
<li><p>Determine how and when letters get printed</p></li>
<li><p>Map SNOMED codes to those SNOMED codes used by the VistA Lab package for PAP smear procedures</p></li>
</ul>
<blockquote>
<p><em>Print Now versus Queue to Print during next Batch Run</em> – Default is to print during next batch run in WH unless Print Now is selected.</p>
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
<th></th>
<th rowspan="3"><ol type="1">
<li><p><span id="Set_up_Women’s_Health_Package" class="anchor"></span><strong>Set up Women’s Health Package</strong></p></li>
</ol>
<blockquote>
<p>In order for reminders to interface with the Women's Health (WH) package, the WH package must be installed and maintained. Specific features of WH that must be in place in order for these reminders to work as designed include the following:</p>
<p>On the File Maintenance Menu [WV MENU-FILE MAINTENANCE]:</p>
</blockquote>
<ol type="1">
<li><p>Add at least one case manager (<strong>Required</strong>) Option: <em>Add/Edit Case Managers</em></p></li>
<li><blockquote>
<p>Add your facility (<strong>Required</strong>)</p>
</blockquote></li>
<li><blockquote>
<p>Identify the default case manager. This person is someone you added via the Add/Edit Case Manager option (#1) (<strong>Required</strong>)</p>
</blockquote></li>
<li><blockquote>
<p>If you are going to really use the WH package, answer the other prompts on page 1 also. You must reply “yes” to both ‘Update Result/Dx Field?’ and ‘Update Treatment Needs?’ prompts. This will allow the Reminder Dialogs to update the WH package.</p>
</blockquote></li>
<li><blockquote>
<p>On page 2, answer 'Yes' to the 'Import Mammograms from Radiology' and 'Import Tests from Laboratory’ prompts. This turns on the link to the radiology/NM and Lab packages. You also need to set ‘Status Given to Imported Mammograms’ to “OPEN.” (See note below) This ensures that you get results at least for veterans. (<strong>Required</strong>)</p>
</blockquote></li>
</ol>
<blockquote>
<p>Option: <em>Edit Site Parameters</em> (Required)</p>
</blockquote>
<ol start="6" type="1">
<li><blockquote>
<p>Add the Morphology and Topography codes that your Lab uses to result pap smears.</p>
</blockquote></li>
</ol>
<blockquote>
<p>Option: <em>Link Pap Smear with SNOMED Codes</em> (<strong>Required</strong>)</p>
</blockquote>
<ol start="7" type="1">
<li><blockquote>
<p>Create and customize the letters you want to send to your patients (<strong>Optional</strong>)</p>
</blockquote></li>
</ol>
<blockquote>
<p>Option: <em>Add/Edit a Notification Purpose &amp; Letter</em></p>
<p><strong>Note</strong>: A mammogram procedure in the WH package with the status of “Open” will cause the MAMMOGRAM REVIEW reminder to be due. This will prompt the clinician to review the results and document them in a progress note. If the status is set to “Closed” when the results are entered into the WH package, the MAMMO- GRAM REVIEW reminder will not be due. Note that the WH mammogram review reminder will not be due if the WH package is set up to assign a diagnostic code to a mammogram as it is loaded from Radiology. The WH package sees a procedure as “Pending” review (which triggers the review reminder) if the status is OPEN and the Result/Diagnosis field is blank.</p>
<p>If Result/Diagnosis is filled in when the mammogram is loaded into WH, then WH thinks it has been reviewed and won’t send Reminders the “Pending” status.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p><strong>NOTE: If your site doesn’t use the Women’s Health package:</strong></p>
<p>Only the screening reminders can be used; you won’t be able to use the review reminders.</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>The WH package should be installed and WH SNOMED codes should be mapped to SNOMED codes used by the VistA Lab package to represent PAP smear results. This is required for the new Lab computed finding to resolve the VA-WH PAP SMEAR SCREENING</p>
<p>reminder.</p>
<p>NOTE: Lab entries must have SNOMED codes entered in the TOPOGRAPHY multiple for the WH code to process correctly and receive an alert. If SNOMED codes are not entered in the TOPOGRAPHY multiple, WH will process the lab entry the old way by sending a MailMan message to the WH user - no CPRS alert is sent.</p>
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
<p><strong>WH Package Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Alternate Setup</strong></p>
<p>For sites who would like to use the Notification functionality and receive alerts without actively using the WH package, the following actions need to take place:</p>
</blockquote>
<ul>
<li><p>Have the WH package activated and populated with women veterans.</p></li>
<li><p>Assign a phony name for the WH Coordinator</p></li>
<li><p>Set the parameters in the WH package as in the example below.</p></li>
</ul>
<blockquote>
<p>By taking this action, the “Next Need” field doesn’t get set, but the notification letter is still sent to be printed at the location identified under “Print Now.” If “Print Now” is not selected, the letter is sent to the WH queue for printing and the progress note indicates the letter was sent to the WH package for printing.</p>
<p>To receive “Alerts” – Based on the changes made in the parameters set above, the results will be sent to the phony name created and to the “Provider” requesting the result.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: To receive alerts without using the WH package

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Women’s Health File Maintenance Menu</strong></p>
<p>Options used to set up parameters related to the CPRS/Reminders integration are highlighted in yellow.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Women’s Health File Maintenance Menu

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>1a. Edit Site Parameters</strong></p>
<p>The highlighted fields are required for Review Reminders</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ESP Edit Site Parameters

<table>
<colgroup>
<col style="width: 86%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"> * EDIT SITE PARAMETERS FOR SALT LAKE CITY HCS  *</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Default Case Manager: <strong>CRPROVIDER,TWO</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Ask Case Manager: <strong>YES</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Autoqueue Normal PAP Letters: NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>PAP Result Normal Letter: <strong>PAP result NEM, next PAP 3Y</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Autoqueue Normal MAM Letters: NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>MAM Result Normal Letter: <strong>MAM result NEM, next MAM 2Y</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Default #days to print letter: <strong>30</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Update Result/Dx Field?: <strong>YES</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Update Treatment Needs?: <strong>YES</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2">(PAGE 1 OF 6)</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COMMAND: Press &lt;PF1&gt;H for help</p>
<p> * EDIT SITE PARAMETERS FOR SALT LAKE CITY HCS  *</p>
<p>RADIOLOGY: Import Mammograms from Radiology: <strong>YES</strong></p>
<p>Status Given to Imported Mammograms: <strong>OPEN</strong> Include ALL Non-Veterans(Y/N)?: YES</p>
<p>ELIGIBILITY CODE(S):</p>
<p>LABORATORY: Import Tests from Laboratory: <strong>YES</strong> Include ALL Non-Veterans(Y/N)?: <strong>YES</strong></p>
<p>ELIGIBILITY CODE(S):</p>
</blockquote>
<p>(PAGE 2 OF 6)</p>
<blockquote>
<p>COMMAND: Press &lt;PF1&gt;H for help</p>
</blockquote></td>
<td><blockquote>
<p>Insert</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
<p>NOTE: After all letter modifications have been made, determine where letters will print and who will be responsible for retrieving and mailing these.</p>
</blockquote></th>
<th><blockquote>
<p><strong>1b. Set up Notification Letters</strong></p>
<p>See Appendix E for an example of all the steps for customizing notification letters.</p>
<p><strong>Edit Generic Letter in WV Letter File</strong></p>
<p>The generic letter needs to be customized locally. This is done through file #790.6, WV Letter. Each facility needs to add its local site address and case manager information. Once this is done, you can edit letters for each of the Notification Purposes through the option AEP Add/Edit a Notification Purpose &amp; Letter.</p>
<p>Go into VA FileMan, Enter or Edit File Entries, and select file 790.6. When prompted for letter, enter Generic.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
</blockquote></th>
<th colspan="3"><blockquote>
<p><strong>1b. Notification letter setup, cont’d</strong></p>
<p><strong>Edit Generic Letter in WV Letter File, cont’d</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><blockquote>
<p>18&gt;</p>
<p>19&gt; This will be filled in when you</p>
<p>20&gt; print the letter.</p>
<p>21&gt;- - - -</p>
<p>22&gt;</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>23&gt; Dear Ms. |$P(NAME,",",1)|,</p>
<p>24&gt;</p>
<p>25&gt; The results of your recent Pap smear are something, somethin 26&gt; This is the body of the letter and should be edited to say w 27&gt; you want for this Purpose of Notification.</p>
<p>28&gt;</p>
<p>29&gt; It may go on to say: Your next something will be due one year 30&gt; now. At that time we will mail you a reminder letter, or you 31&gt; schedule the appointment yourself by calling our Family Medi</p>
</blockquote></td>
<td><blockquote>
<p>This text is modified through the option Add/Edit Notification letters</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>32&gt; Clinic at 777-7777 or our Women's Clinic at 777-7777.</p>
<p>33&gt;</p>
<p>34&gt; Sincerely,</p>
<p>35&gt;</p>
<p>36&gt;</p>
<p>37&gt; Modify this text in FileMan –</p>
<p>38&gt; WHProvider, THREE, LPN #790.6 WV Letter</p>
<p>39&gt; Women's Health Program</p>
<p>40&gt; phone: 666-7777</p>
<p>41&gt;</p>
<p>42&gt;</p>
<p>43&gt; printed: |NOW|</p>
<p>EDIT Option:</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>1b. Notification Letter Setup, cont’d Add and Edit Notification Letters</strong></p>
<p>Each letter (Notification Purpose) needs to be customized locally. The first time you use this option to edit each letter, enter Yes, to load your edited generic sample letter at the following prompt:</p>
<p>Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?</p>
<p>Enter Yes or No: NO// <strong>Yes</strong></p>
<p>For subsequent letter-editing, enter No.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> AEP Add/Edit a Notification Purpose & Letter Example

> To edit the letter, tab to the “+” sign and press Enter.

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>1b. Notification Letter Setup, cont’d</strong></p>
<p><strong>Modify Default Letter Format to Customize for this Notification Purpose, cont’d</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>1b. Notification Letter Setup, cont’d</strong></p>
<p><strong>New Purposes of Notification (letter types) added with this patch</strong></p>
<p>Letters for each of these Purposes of Notification need to be customized for local use.</p>
<p>See instructions in Appendix E for adding new Purposes as dialog elements.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> CPRS UPDATE PAP TX NEED 4M

> CPRS UPDATE PAP TX NEED 6M

> CPRS UPDATE PAP TX NEED 3Y CPRS UPDATE PAP TX NEED 2Y CPRS UPDATE PAP TX NEED 1Y CPRS UPDATE MAM TX NEED 1Y CPRS UPDATE MAM TX NEED 2Y CPRS UPDATE MAM TX NEED 6M CPRS UPDATE MAM TX NEED 4M

> MAM result NEM, next MAM 1Y MAM result NEM, next MAM 2Y MAM result NEM, next MAM 4M MAM result NEM, next MAM 6M

> MAM result abnormal, F/U MAM 4M MAM result abnormal, F/U MAM 6M PAP result NEM, next PAP 1Y

> PAP result NEM, next PAP 2Y PAP result NEM, next PAP 3Y PAP result NEM, next PAP 4M PAP result NEM, next PAP 6M

> PAP result abnormal, F/U PAP 4M PAP result abnormal, F/U PAP 6M MAM unsatisfactory, need repeat Pap unsatisfactory, need repeat

> PAP result NEM, further screening not required MAM result NEM, further screening not required

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>1c</strong>. <strong>Link Pap Smear with SNOMED Codes</strong></p>
<p>NOTE: Your site may use different codes from the Morphology and Topography SNOMED codes listed here.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select File Maintenance Menu Option: <strong>PAP</strong> Link Pap Smear with SNOMED Codes Select a MORPHOLOGY SNOMED CODE: <strong>?</strong></p>
<p>Answer with MORPHOLOGY SNOMED CODE Choose from:</p>
<p>UNSATISFACTORY SPECIMEN If codes other than the ones</p>
<p>ABNORMAL APPEARANCE listed here appear, link the NEGATIVE FOR MALIGNANT CELLS appropriate ones to the Pap NO EVIDENCE OF MALIGNANCY Smear.</p>
<p>SUSPICIOUS FOR MALIGNANT CELLS CERVICAL MUCOUS ARBORIZATION VAGINA, SECRETORY ALTERATION</p>
<p>You may enter a new MORPHOLOGY SNOMED CODE, if you wish Answer with MORPHOLOGY FIELD NAME</p>
<p>Do you want the entire 3609-Entry MORPHOLOGY FIELD List? UNSA??</p>
<p>Answer with 'Yes' or 'No': <strong>N</strong> (No)</p>
<p>Select a MORPHOLOGY SNOMED CODE: <strong>UNSATISFACTORY SPECIMEN</strong> 09010</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>MORPHOLOGY SNOMED CODE: UNSATISFACTORY SPECIMEN// <strong>&lt;Enter&gt;</strong></p>
<p>DIAGNOSIS: Unsatisfactory// <strong>&lt;Enter&gt;</strong></p>
<p>Select a MORPHOLOGY SNOMED CODE: <strong>&lt;Enter&gt;</strong></p>
<p>Select a TOPOGRAPHY SNOMED CODE: <strong>?</strong></p>
<p>Answer with TOPOGRAPHY SNOMED CODE</p>
<p>Choose from: Your site may use different codes from VAGINAL-CERVICAL CYTOLOGIC MATERIAL these. These should only be related to VAGINAL CYTOLOGIC MATERIAL PAP smears.</p>
<p>CERVICAL CYTOLOGIC MATERIAL</p>
<p>You may enter a new TOPOGRAPHY SNOMED CODE, if you wish Answer with TOPOGRAPHY FIELD NAME</p>
<p>Do you want the entire 8575-Entry TOPOGRAPHY FIELD List? <strong>N</strong> (No)</p>
<p>Select a TOPOGRAPHY SNOMED CODE: <strong>CERVICAL CYTOLOGIC MATERIAL</strong> 8X310</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>TOPOGRAPHY SNOMED CODE: CERVICAL CYTOLOGIC MATERIAL</p>
<p>// <strong>&lt;Enter&gt;</strong></p>
<p>Select a TOPOGRAPHY SNOMED CODE: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Women’s Health Patient Management Menu</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>WOMEN'S HEALTH: * PATIENT MANAGEMENT MENU * SALT LAKE CITY HCS</p>
<p>PC Edit/Print Patient Case Data</p>
<p>PP Patient Profile You can manually add a</p>
<p>FS Print Patient Demographic Info (Face Sheet) patient to the WH package BD Browse Patients With Needs Past Due with Edit/Print Patient Case LAB Save Lab Test as Procedure Data, if you don’t use the</p>
<p>AP Add a NEW Procedure Automatically Load</p>
<p>EP Edit a Procedure Patients option. Also,</p>
<p>HS Health Summary patients will be</p>
<p>BP Browse Procedures automatically added if lab</p>
<p>PR Print a Procedure or radiology results are</p>
<p>HIS Add an HISTORICAL Procedure sent by those applications.</p>
<p>RA Add a Refusal of Treatment RE Edit a Refusal of Treatment AN Add a New Notification</p>
<p>EN Edit a Notification BN Browse Notifications</p>
<p>PL Print Individual Letters PQ Print Queued Letters</p>
<p>Select Patient Management Option:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> 1c. Women’s Health Patient Profile (brief)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 2%" />
<col style="width: 10%" />
<col style="width: 2%" />
<col style="width: 33%" />
<col style="width: 19%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><blockquote>
<p>* CONFIDENTIAL PATIENT INFORMATION *</p>
<p> * Patient Profile  * Run Date: SEP 16, 2003 14:14</p>
<p>Patient Name: WHPATIENT,ONE (56y/o) SSN: 666-33-5525</p>
<p>Case Manager: WHPROVIDER,ONE Facility: SALT LAKE CITY HCS Cx Tx Need : Routine PAP (by 09/09/04) Cx Facility:</p>
<p>PAP Regimen : Undetermined (began NO DATE) Pr Provider: UNKNOWN Br Tx Need : Mammogram, Screening (by 04/11/04)Br Facility:</p>
<p>Hx of BR CA : &gt;1 1st degree relatives</p>
<p>Elig Code : Veteran: Yes</p>
<p>MST : Unknown, not screened CST:</p>
<p>================================================================================ DATE PROCEDURE RESULTS/DIAGNOSIS STATUS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1) 04/30/03</td>
<td></td>
<td><blockquote>
<p>PAP</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>No Evidence of Malignancy</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CLOSED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2) 04/11/03</td>
<td></td>
<td><blockquote>
<p>PAP</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>No Evidence of Malignancy</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CLOSED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3) 04/11/03</td>
<td></td>
<td><blockquote>
<p>MAMB</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NOT ENTERED</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>OPEN</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4) 04/10/03</td>
<td></td>
<td><blockquote>
<p>BRUL</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>NOT ENTERED</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DELINQ</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Women’s Health Setup, cont’d

> Women’s Health Patient Profile (detailed)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
<p><strong>NOTE:</strong> The WH</p>
<p>mammogram review reminder will not be due if the WH package is set up to assign a diagnostic code to a mammograms as it is loaded from Radiology.</p>
<p>The WH package sees a procedure as "Pending" review (which triggers our review reminder) if the status is OPEN and the Result/Diagnosis field is blank.</p>
<p>If Result/Diagnosis is filled in when the mammogram is loaded into WH, then WH thinks it's been reviewed and won't send us the "Pending" status.</p>
</blockquote></th>
<th><blockquote>
<p><strong>Status Given to Imported Mammograms</strong></p>
<p>The WH package can be set up to receive mammogram results from the Radiology package. This is controlled by the WH site parameters and diagnostic code translation options under Management Functions/File Maintenance:</p>
<p>ESP Edit Site Parameters</p>
<p>EDX Edit Diagnostic Code Translation File PDX Print Diagnostic Code Translation File</p>
<p>The Mammogram Review reminder will only be due with this combination of settings:</p>
</blockquote>
<ul>
<li><p>Status Given to Imported Mammograms: OPEN</p></li>
<li><p><strong>Diagnostic code translations are not assigned, so there is nothing entered into Result/Diagnosis field and the WH Patient Profile shows NOT ENTERED</strong></p></li>
</ul>
<blockquote>
<p>The Mammogram Review reminder will not be due if any of these settings combinations exist instead:</p>
</blockquote>
<ul>
<li><p><strong>Diagnostic code translations assigned so something is entered into the Result/Diagnosis field</strong></p></li>
<li><p>Status Given to Imported Mammograms: CLOSED</p></li>
<li><p>Diagnostic code translations are or are not assigned</p></li>
</ul>
<blockquote>
<p>The "Status Given to Imported Mammograms" is entered on the second page of Edit Site Parameters and can be set to "OPEN" or "CLOSED"</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p> * EDIT SITE PARAMETERS FOR SALT LAKE CITY HCS  *</p>
<p>RADIOLOGY: Import Mammograms from Radiology: YES <strong>Status Given to Imported Mammograms: OPEN</strong> Include ALL Non-Veterans(Y/N)?: YES</p>
<p>ELIGIBILITY CODE(S):</p>
<p>. . . (PAGE 2 OF 6)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 65%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="3"><blockquote>
<p><strong>Women’s Health Setup, cont’d</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Status Given to Imported Mammograms</strong></p>
<p>Diagnostic codes from the Radiology package can be translated into a Result/Diagnosis code.</p>
<p>This is what a diagnostic codes report looks like when diagnostic codes have not been assigned using WH option PDX Print Diagnostic Code Translation File:</p>
</blockquote></th>
</tr>
<tr class="odd">
<th colspan="2"><blockquote>
<p>WV DIAGNOSTIC CODE TRANSLATION LIST DEC 20,2004 09:40 PAGE 1</p>
<p>* NO RECORDS TO PRINT *</p>
</blockquote></th>
</tr>
<tr class="header">
<th colspan="2"><blockquote>
<p>This is what you see if you decide to edit diagnostic code translations for the first time using WH option EDX Edit Diagnostic Code Translation File:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p> * WOMEN’S HEALTH: EDIT WV DIAGNOSTIC CODE TRANSLATION FILE  *</p>
<p>Select RESULT/DIAGNOSIS: ?</p>
<p>You may enter a new WV DIAGNOSTIC CODE TRANSLATION, if you wish Choose the women's health results/diagnosis code you wish to match to a radiology diagnostic code.</p>
<p>Only Results/Diagnoses that apply to Mammograms may be selected.</p>
<p>Answer with WV RESULTS/DIAGNOSIS</p>
<p>Do you want the entire WV RESULTS/DIAGNOSIS List? y (Yes)Choose from:</p>
<p>Abnormal 90</p>
<p>Assessment Is Incomplete 2</p>
<p>Benign Finding, Negative 5</p>
<p>Highly Sug of Malig, Tk Action 1</p>
<p>Indicated, But Not Performed 5</p>
<p>Negative 90</p>
<p>No Evidence of Malignancy 90</p>
<p>Not Indicated 50</p>
<p>Prbly Benign, Short Int F/U 4</p>
<p>Suspicious Abnorm, Consider Bx 1</p>
<p>Unsatisfactory for Dx 2</p>
<p>Select RESULT/DIAGNOSIS:</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### <table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Map_terms" class="anchor"></span>TIP:</p>
<p>Coordination between CACs and Women’s Health Case Managers will help the mapping process</p>
</blockquote></th>
<th><ol start="2" type="1">
<li><p><strong>Map local findings to the national Reminder Terms.</strong></p></li>
</ol>
<blockquote>
<p><em>Option: Reminder Term Management</em> on the <em>Reminder Management Menu.</em></p>
<p>Before using WH reminders, map the local findings your site uses to represent the national reminder terms, if necessary.</p>
</blockquote>
<ul>
<li><p>Prepare a list of your local findings – health factors, taxonomies, etc. that you use to represent WH terms.</p></li>
<li><p>Review the national term definitions (use the options on the Reminder Term Management menu), to compare these to what you are using locally to represent WH terms.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Term Mapping Recommendations

> Mammogram Terms

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
<p><em>Patient Cohort Findings</em></p>
</blockquote></td>
<td><blockquote>
<p><em>The following reminder terms determine whether the reminder applies to the patient.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-TERMINAL CANCER PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>No mapping necessary. Use the VA- TERMINAL CANCER PATIENTS reminder</p>
<p>taxonomy that has been previously distributed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH BILATERAL MASTECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>This term will use the VA-WH BILATERAL MASTECTOMY taxonomy to find coded bilateral mastectomies. The health factor WH</p>
<p>BILATERAL MASTECTOMY distributed with this term may be used or add any local health factor that</p>
<p>represents the patient had a bilateral mastectomy and no longer needs mammogram screening.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Mammogram Terms, cont’d

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
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
<p><em>Resolution Findings</em></p>
</blockquote></td>
<td><blockquote>
<p><em>The following are reminder terms that resolve the reminder. Function Findings use these findings to determine whether a result is the most recent finding or whether a short-term resolution finding is the most recent finding. If the most recent finding is a short-term resolution finding, the reminder will be due based on one of the following Function Finding frequency periods: 4 months or 6 months. If the result is the most recent finding, the baseline age/frequency is used. However, the baseline frequency will be overridden if the Functional</em></p>
<p><em>Findings determine that an information finding exists which alters the baseline frequency to 1 or 2 years.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN IN WH PKG</p>
</blockquote></td>
<td><blockquote>
<p>No mapping necessary. This term uses the pre-mapped computed finding: VA-WH MAMMOGRAM IN WH PKG to find mammogram screening findings in the</p>
<p>Women's Health Package.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN IN RAD PKG</p>
</blockquote></td>
<td><blockquote>
<p>Mapping is needed. This term represent Mammogram results documented in the Radiology package. Map local radiology procedures that represent the following procedures:</p>
<p>MAMMOGRAM BILAT MAMMOGRAM UNILAT MAMMOGRAM SCREEN</p>
<p>Each finding should have a condition added to exclude unsatisfactory results.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN DONE</p>
</blockquote></td>
<td><blockquote>
<p>Some mapping may be appropriate. This reminder term will use the previously distributed VA- MAMMOGRAM/SCREEN taxonomy to find ICD DIAGNOSIS or CPT coded results.</p>
<p>Use the new WH MAMMOGRAM OUTSIDE health factor to document Mammogram results completed outside the VA when the Mammogram results are not documented in Radiology, Women's Health or Consult packages.</p>
<p>Map local findings, such as consult orders related to Mammogram Screening. Use appropriate condition logic to indicate Mammogram screening has been completed.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Mammogram Terms, cont’d

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
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
<p>VA-WH MAMMOGRAM SCREEN NOT INDICATED</p>
</blockquote></td>
<td><blockquote>
<p>Use the findings distributed with this reminder term or map any local findings that indicate a Mammogram screen is not indicated for this patient.</p>
<p>This term is distributed with mapping to the following health factors:</p>
<p>INACTIVATE BREAST CANCER SCREEN</p>
<p>(distributed with the first version of the Clinical Reminder package in 1996 to inactivate the BREAST CANCER reminder).</p>
<p>WH PAP MAMMOGRAM SCREEN NOT INDICATED VA LIMITED LIFE EXPECTANCY</p>
<p>Use in National VA-WH MAMMOGRAM SCREENING reminder:</p>
<p>This term is used in WH reminders to inactivate the Mammogram screening reminder. A clinician can <strong>reactivate the reminder</strong> by selecting one of the frequencies from the screening reminder dialog. The 4M, 6M, 1Y, and 2Y health factors are used by function findings to set the reminder frequency.</p>
<p>Begin date <strong>of T-6M</strong> has been added to HF.VA LIMITED LIFE EXPECTANCY and TX.VA-TERMINAL</p>
<p>CANCER PATIENTS so screening will come due again if the patient lives longer than expected or if the patient has been misdiagnosed.</p>
<p>Sites may prefer to use local LIMITED LIFE EXPECTANCY health factors and add their health factors to other reminder terms, which cause the Mammogram Screening reminder to be due without requiring a clinician to select a finding to reactivate the reminder. (E.g., Add the local life expectancy health factor for "local LIFE EXPECTANCY 6M" to the VA- WH MAMMOGRAM SCREEN NOT INDICATED</p>
<p>term.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Mammogram Terms, cont’d

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
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
<p>VA-WH BREAST CARE ORDER HEALTH FACTOR</p>
</blockquote></td>
<td><blockquote>
<p>Use the health factors distributed with the reminder term if they are appropriate for your facility to track breast care orders. This reminder term represents the action taken from the dialog to indicate the clinician intends to place an order related to mammogram screening. The health factor date will be used to calculate the resolution frequency, instead of the Start date related to the order actually placed.</p>
<p>Health factors distributed with this term:</p>
</blockquote>
<ul>
<li><p>WH ORDER MAMMOGRAM SCREEN HF (Use this if an order menu is referenced as the quick order, or use for a quick order for mammogram screening to radiology or consults)</p></li>
<li><p>WH ORDER MAMMOGRAM BILAT HF (Use when quick order is for bilateral mammogram)</p></li>
<li><p>WH ORDER MAMMOGRAM UNILAT HF (Use when quick order is for unilateral mammogram)</p></li>
</ul></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN DEFER</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH MAMMOGRAM DEFERRED or WH</p>
<p>MAMMOGRAM DECLINED health factors distributed with this term or add any local health factor representing that mammogram screening should be satisfied for one</p>
<p>week.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG</p>
</blockquote></td>
<td><blockquote>
<p>Mapping will be necessary. This term represent Mammogram results documented in the Radiology package. Map local radiology procedures that represent the following procedures:</p>
<p>MAMMOGRAM BILAT MAMMOGRAM UNILAT MAMMOGRAM SCREEN</p>
<p>Each finding should have a condition that checks for unsatisfactory results. No mapping is necessary for the WH package. Use the VA-WH MAMMOGRAM IN WH PKG computed finding and the value</p>
<p>UNSATISFACTORY" to find unsatisfactory results documented in the WH package.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH MAMMOGRAM PENDING REVIEW</p>
</blockquote></td>
<td><blockquote>
<p>No mapping necessary. New VA-WH MAMMOGRAM REVIEW computed finding will be installed with this reminder. This computed findings will make the VA-WH MAMMOGRAM REVIEW reminder due when the condition is: I V="Pending". It will then return mammogram results pending clinician review from the</p>
<p>WH package.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Mammogram Terms, cont’d

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
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
<p><em>Information Findings</em></p>
</blockquote></td>
<td><blockquote>
<p><em>The following are information reminder terms that are used in Function Findings to alter the baseline Age/Frequency. If the most recent resolution finding is a documented result, the frequency for the next Mammogram screen will be based on these reminder</em></p>
<p><em>terms.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN FREQ - 4M</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH MAMMOGRAM SCREEN FREQ - 4M</p>
<p>health factor distributed with this reminder term, or add any local findings that indicate mammogram screening should occur every 4 months.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN FREQ - 6M</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH MAMMOGRAM SCREEN FREQ - 6M</p>
<p>health factor distributed with this reminder term, or add any local findings that indicate mammogram screening</p>
<p>should occur every 6 months.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN FREQ - 1Y</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH MAMMOGRAM SCREEN FREQ – 1Y</p>
<p>health factor distributed with this reminder term, or add any local findings that indicate mammogram screening should occur every 1 year.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN FREQ - 2Y</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH MAMMOGRAM SCREEN FREQ - 2Y</p>
<p>health factor distributed with this term or add any local</p>
<p>health factor that represents mammogram screening should occur every two years</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>Information Only</em></p>
</blockquote></td>
<td><blockquote>
<p><em>The following reminder terms are "information only" terms that are not used to alter the frequency, but provide</em></p>
<p><em>information that may be helpful to the clinician.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH HX BREAST CANCER/ABNORMAL MAM</p>
</blockquote></td>
<td><blockquote>
<p>Use the previously distributed VA-BREAST TUMOR and VA-MASTECTOMY taxonomies mapped to this term. This term uses computed finding VA-WH MAMMOGRAM ABNORMAL IN WH PKG to search</p>
<p>for the existence of any abnormal results in the WH Package.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH MAMMOGRAM ORDER</p>
</blockquote></td>
<td><blockquote>
<p>Map local orderable items that represent mammogram related orders (e.g., Consult order to Women's Health Clinic). Use the conditions that indicate the order is not completed, discontinued, or cancelled. This reminder term represents orders pending completion.</p>
<p>This term can also be used to indicate the patient is being followed by a gynecologist.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Pap Smear Reminder Terms

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
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
<p><em>Patient Cohort Findings</em></p>
</blockquote></td>
<td><blockquote>
<p><em>The following reminder terms determine whether the reminder applies to the patient.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-TERMINAL CANCER PATIENT</p>
</blockquote></td>
<td><blockquote>
<p>No mapping necessary. Use the VA-TERMINAL CANCER PATIENTS reminder taxonomy that has</p>
<p>been previously distributed.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH HYSTERECTOMY W/CERVIX REMOVAL</p>
</blockquote></td>
<td><blockquote>
<p>No mapping necessary. Use the VA-WH HYSTERECTOMY W/CERVIX REMOVED</p>
<p>reminder taxonomy distributed with this term. Note the VA-CERVICAL CA/ABNORMAL PAP reminder</p>
<p>taxonomy is now used for information only and should not be mapped to this reminder term since it contains codes where the cervix may not have been removed.</p>
<p>This reminder term is also mapped to the new health</p>
<p>factor WH HYSTERECTOMY W/CERVIX REMOVED.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><em>Resolution Findings</em></p>
</blockquote></td>
<td><blockquote>
<p><em>The following reminder terms resolve the reminder. These resolution terms are defined with a "Use in Resolution Logic,” but no Frequency. Frequency for this reminder will be determined by Function Findings (FF) logic, which examines the most recent findings:</em></p>
</blockquote>
<ul>
<li><p><em>If Function Findings determine that the most recent finding is a result, the baseline age and frequency will be used.</em></p></li>
<li><p><em>If Function Findings determine that an information finding exists that alters the baseline frequency to 4M, 6M, 1Y, 2Y or 3Y, the baseline frequency will be overridden.</em></p></li>
</ul></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH PAP SMEAR SCREEN IN WH PKG</p>
</blockquote></td>
<td><blockquote>
<p>No mapping necessary. This term represents PAP Smear results documented in the Women's Health (WH) Package. Use the new VA-WH PAP SMEAR IN WH PKG computed finding distributed with this reminder term. This computed finding looks for PAP</p>
<p>smear results in the Women's Health Package.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Pap Smear Reminder Terms, cont’d

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
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
<p>VA-WH PAP SMEAR SCREEN IN LAB PKG</p>
</blockquote></td>
<td><blockquote>
<p>No mapping necessary. This term represents PAP Smear results documented in the Laboratory package. Use the new VA-WH PAP SMEAR IN LAB PKG computed finding distributed with this reminder term. This computed finding looks for PAP smear results in the Laboratory package.</p>
<p>This computed finding will only work if the Women's Health WV PROCEDURE TYPE file entry for PAP SMEAR has SNOMED codes defined that are used for PAP Smear results at your facility. The SNOMED codes</p>
<p>need to be defined regardless of whether the Women's Health Package is being used.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH PAP SMEAR DONE</p>
</blockquote></td>
<td><blockquote>
<p>No mapping necessary. Use the new VA-WH PAP SMEAR DONE CODES taxonomy distributed with this reminder term. This taxonomy is similar to the VA- CERVICAL CANCER SCREEN taxonomy distributed to the field with the first reminder package distribution. The new taxonomy should be used because it does not include codes such as Q0091, which represents PAP smears obtained by the clinician.</p>
<p>Use the new WH PAP SMEAR OUTSIDE health factor to document PAP Smear results completed outside the VA when the PAP Smear results are not documented in Lab, Women's Health or Consult packages.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH PAP SMEAR OBTAINED</p>
</blockquote></td>
<td><blockquote>
<p>No mapping is necessary. Use the new taxonomy VA-</p>
<p>WH PAP SMEAR OBTAINED. This term represents the clinician's actions taken to obtain the PAP smear.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH PAP SMEAR ORDER HEALTH FACTOR</p>
</blockquote></td>
<td><blockquote>
<p>The following health factors are distributed with this term:</p>
</blockquote>
<ul>
<li><p>WH ORDER PAP SMEAR SCREEN HF (for use when an order menu with a PAP Smear Screen order is used from the reminder dialog).</p></li>
<li><p>WH ORDER REFER WH CLINIC GYN CARE HF (for use when a quick order is used for WH CLINIC GYN CARE referral in reminder dialogs).</p></li>
<li><p>WH ORDER REFER GYNECOLOGIST HF (for use when a quick order is used for GYNECOLOGY referral in reminder dialogs).</p></li>
</ul>
<blockquote>
<p>This reminder term represents the action taken from the dialog to indicate the clinician selected an element that could generate an order for PAP Smear. The health factor</p>
<p>date will be used to calculate the resolution frequency, instead of using the Order's Start date.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Pap Smear Reminder Terms, cont’d

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
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
<p>VA-WH PAP SMEAR SCREEN NOT INDICATED</p>
</blockquote></td>
<td><blockquote>
<p>Use the findings distributed with this reminder term or map any local findings that indicate a PAP smear screen is not</p>
<p>indicated for this patient. This term is distributed with mapping to the following health factors:</p>
<p>INACTIVATE CERVIX CANCER SCREEN (distributed with the first version of the Clinical Reminder package in 1996 to inactivate the CERVICAL CANCER reminder).</p>
<p>WH PAP SMEAR SCREEN NOT INDICATED VA LIMITED LIFE EXPECTANCY</p>
<p>and the following taxonomy:</p>
<p>VA-TERMINAL CANCER PATIENTS</p>
<p>This term is used in WH reminders to inactivate the PAP Smear Screening reminder. A clinician can reactivate the reminder by selecting one of the frequencies from the screening reminder dialog. The 4M, 6M, 1Y, 2Y, and 3Y health factors are used by function findings to set the reminder frequency.</p>
<p>Begin date <strong>of T-6M</strong> has been added to HF.VA LIMITED LIFE EXPECTANCY and TX.VA-TERMINAL CANCER PATIENTS so</p>
<p>screening will come due again if the patient lives longer than expected or if the patient has been misdiagnosed.</p>
<p>Sites may prefer to use local LIMITED LIFE EXPECTANCY health factors and add their health factors to other reminder terms which cause the PAP Smear Screening reminder to be due without requiring a clinician to</p>
<p>select a finding to reactivate the reminder. (E.g., Add the local life expectancy</p>
<p>health factor for "local LIFE EXPECTANCY 6M” to the VA-WH PAP SCREEN NOT INDICATED term.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH PAP SMEAR SCREEN DEFER</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH PAP SMEAR DECLINED and/or WH PAP SMEAR</p>
<p>DEFERRED health factors distributed with this term, or add any local health factors representing that PAP smear screening should be deferred.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH PAP SMEAR UNSATISFACTORY IN LAB/WH PKG</p>
</blockquote></td>
<td><blockquote>
<p>No mapping necessary. This term represents unsatisfactory \ PAP Smear results documented in the Laboratory package. Use the new VA-WH PAP SMEAR IN LAB PKG computed finding</p>
<p>distributed with this reminder term. This computed finding looks for PAP smear results in the Laboratory package where the Result Status that is "Unsatisfactory"</p>
<p><strong>This computed finding will only work if the Women's Health WV PROCEDURE TYPE file entry for PAP SMEAR has SNOMED codes defined that are used by your local Lab Service to document PAP Smear results in the Lab Package. The SNOMED codes need to be defined regardless of whether the Women's Health</strong></p>
<p><strong>Package is being used.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> Pap Smear Reminder Terms, cont’d

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
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
<p><em>Information Findings:</em></p>
</blockquote></td>
<td><blockquote>
<p><em>Function Findings (FF) will be used to determine the frequency of these reminders. The following are information reminder terms that are used in Function Findings to alter the baseline Age/Frequency. If the most recent resolution finding is a documented result, the frequency for the next PAP Smear will be based on these reminder terms. If more than one of the frequency findings is recorded at the same date/time, the finding that makes</em></p>
<p><em>the reminder due most often will prevail.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH PAP SMEAR SCREEN FREQ – 4M</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH PAP SMEAR SCREEN - FREQ 4M health factor distributed with this reminder term, or add any local findings that indicate PAP smear screening should occur every 4 months.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH PAP SMEAR SCREEN FREQ – 6M</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH PAP SMEAR SCREEN FREQ - 6M health factor distributed with this reminder term or add any local findings</p>
<p>that indicate PAP smear screening should occur every 6 months.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH PAP SMEAR SCREEN FREQ – 1Y</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH PAP SMEAR SCREEN FREQ - 1Y health factor</p>
<p>distributed with this reminder term, or add any local findings that indicate PAP smear screening should occur every year.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VA-WH PAP SMEAR SCREEN FREQ – 2Y</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH PAP SMEAR SCREEN FREQ - 2Y health factor distributed with this reminder term, or add any local findings that</p>
<p>indicate the PAP smear screening should occur every 2 years.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH PAP SMEAR SCREEN FREQ – 3Y</p>
</blockquote></td>
<td><blockquote>
<p>Use the WH PAP SMEAR SCREEN FREQ - 3Y health factor distributed with this reminder term, or add any local findings that indicate PAP smear screening should occur every 3 years.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><em>Information Only</em></p>
</blockquote></td>
<td><blockquote>
<p><em>The following reminder terms are "information only" terms that are not used to alter the frequency, but provide information that may be helpful to the clinician.</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH HYSTERECTOMY</p>
</blockquote></td>
<td><blockquote>
<p>This reminder term represents hysterectomy related procedures. It is pre-mapped to use the VA-HYSTERECTOMY taxonomy, which was distributed, to the field in 1996. It is not used to alter the patient cohort because it contains hysterectomy codes that indicate the patient’s cervix may or may not have been removed.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Pap Smear Reminder Terms, cont’d

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
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
<p>VA-WH HX CERVICAL CANCER/ABNORMAL PAP</p>
</blockquote></td>
<td><blockquote>
<p>This reminder term is mapped to the taxonomy VA-CERVICAL CA/ABNORMAL PAP findings. This term represents ICD9, ICD0, and CPT codes that indicate the patient has a history of cervical cancer or a diagnosis for abnormal PAP. Sites may choose to only use documented diagnosis and procedure codes removing mapping to Women's Health.</p>
<p>This reminder term is also mapped to the computed finding</p>
<p>VA-WH PAP SMEAR SCREEN IN WH PKG with a condition check for "Abnormal" used for the search. If PAP smear results are documented in the Women's Health package, the computed finding VA-WH PAP SMEAR SCREEN IN WH PKG will find the most recent PAP Smear entry that has an "Abnormal" result. <strong>Sites can remove this mapped item if they are not using the Women's Health package to store PAP results.</strong></p>
<p>The reminder term may also be mapped to the computed finding VA-WH PAP SMEAR SCREEN IN LAB PKG with a condition check for "Abnormal" Result Type. The Result Type is based on Procedure definitions in the Women's Health Package.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA-WH PAP SMEAR ORDER</p>
</blockquote></td>
<td><blockquote>
<p>Map local orderable items that represent PAP smear related orders (e.g., Consult order to Women's Health Clinic).</p>
<p>Use the conditions that indicate the order is not completed,</p>
<p>discontinued, or cancelled. This reminder term represents orders pending completion.</p>
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
<p><span id="_bookmark15" class="anchor"></span><strong>Test the reminders</strong></p>
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
<p>Select Reminder: VA-WH MAMMOGRAM SCREENING</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 1%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Edit_Dialogs" class="anchor"></span><strong>Do not edit these dialog elements: VA-WH MAMMOGRAM RESULTS and VA-WH PAP SMEAR</strong></p>
<p><strong>RESULTS.</strong> These dialog elements do not have finding items associated with them in Dialog Management. The finding items and the text that appear in the elements are set when the dialogs are being loaded into CPRS.</p>
<p>NOTE: Do not install and release the PAP review reminder to the field if PAP cytology results are not recorded in the VistA Lab package and are not updating WH package.</p>
<p>TIP</p>
<p>Coordination between CACs and Women’s Health Case Managers will help the dialog edit process</p>
</blockquote></th>
<th></th>
<th><ol start="4" type="1">
<li><p><strong>Use the Reminder Dialog options to edit the national (exported) dialogs.</strong></p></li>
</ol>
<blockquote>
<p>After mapping local findings to the national terms, determine whether to use local findings as the data elements that are captured, or the national findings that are already mapped to the national terms. Review dialog elements in the national reminder dialog and change any national health factors to local health factors, if necessary. It is not unusual for local findings to be used in your national dialogs. Any local findings used in the national dialogs should be mapped to the appropriate national reminder term.</p>
</blockquote>
<ul>
<li><p>If using local findings, edit the reminder dialog by identifying the element that allows for that data element to be collected. Change the finding item for that element to the local finding.</p></li>
</ul>
<blockquote>
<p>Alternatively, use the Reminder Dialog options to copy the national dialog, dialog elements, and dialog groups to make local changes.</p>
</blockquote>
<ul>
<li><p>Add local dialog elements with local Order Dialogs for additional ordering options for the clinicians. Some sites have clinicians order a consult to a service that provides PAP smears. If your site does this, copy the reminder dialog to a local reminder dialog and then add the local dialog element for the consult order to the reminder dialog so this practice can continue.</p></li>
<li><p>Some sites have local entries in the Women's Health WV Notification Purpose file. If your site does this, copy the reminder dialog to a local reminder dialog, then add or modify the notifications so this practice can continue. Under reminder findings, use the new "WH" finding type to point to the entries.</p></li>
<li><p>If your site chooses not to send letters via the WH package, copy the appropriate national dialog components to local components and remove the findings related to WH notifications.</p></li>
</ul>
<blockquote>
<p>The national reminders and dialogs can <em><strong>only</strong></em> be changed by changing the finding item in the nationally distributed elements to use your local finding item instead of the nationally distributed one.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

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
<p>a. Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI) and Change View (CV) to see the</p>
<p>Dialog view:</p>
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
<p>Search for: <strong>V-WH</strong></p>
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

5.  Two new forced values are included with this project.

#### PXRM WH NOTIFICATION TYPE

- PXRM WH UPDATE TREATMENT NEED

> Note: These forced values are only used with the VA-WH MAMMOGRAM REVIEW and VA-WH PAP SMEAR REVIEW

> reminders and dialogs.

> PXRM WH NOTIFICATION TYPE is a forced value that allows sites to identify a notification type that will update the Women’s Health package. For this forced value to work properly, you must set it equal to one or more of three codes “L”, “I”, or “P” and must separate multiple codes by a colon (i.e. L:I or L:P:I)

> Notification type definitions:

> “L” stands for Letter notification type = letter will notify Patient. The WH package is updated to send a result letter, which will be printed with the next WH batch run.

> “I” stands for In-Person notification type = patient was notified of results in person. The WH package is updated with this information.

> “P” stands for Phone Call notification type = patient was notified of results by phone. The WH package is updated with this information.

> This forced value will also update the progress note. PXRM WH UPDATE TREATMENT NEED

> This forced value is used with the “CPRS UPDATE” notification purposes. It updates the WH treatment need information, but does not generate a letter. This forced value must be set to “CPRS.”

> Ordering a Consult:

> If your site wants to be able to order consults from the screening reminders to a service that does pap smears or mammograms, you need to create a quick order for the consult or a menu and put it in the finding item field indicated below:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Test_Reminders" class="anchor"></span><strong>Test Reminders</strong></p>
</blockquote></th>
<th><ol start="5" type="1">
<li><p><strong>Verify that the reminders function properly.</strong></p>
<ol type="a">
<li><p>Run a Reminders Due Report to determine if the WH Clinical Reminder statuses reported are correct.</p></li>
</ol></li>
</ol>
<blockquote>
<p><em>Option: Reminders Due</em> on the <em>Reminder Reports menu</em></p>
<p>This report can be displayed at the beginning of the day for patients being seen that day. Reminder reports offer a way to review how the mapping and the local data will potentially be viewed by the extracts that will be sent to the Austin database from the reminders.</p>
</blockquote>
<ul>
<li><p>Each of the reminders can be used in a reminder report to evaluate clinics or stop codes on their adherence/compliance with that reminder.</p></li>
<li><p>The reports can be run to list individual patient names for chart review on reasons that the guideline was not or could not be achieved.</p></li>
<li><p>Clinics, stop codes, or divisions can be identified by summary reports using these reminders where there are differences in compliance or poor adherence to the guideline.</p></li>
</ul>
<ol start="2" type="a">
<li><blockquote>
<p>Use the Reminder Test option to test the reminders.</p>
</blockquote></li>
</ol>
<blockquote>
<p><em>Option: Reminders Test</em> on the <em>Reminder Management menu</em></p>
<p>1. Select a patient who had a mammogram screening done within the past year.</p>
<p>Run the Reminder Test option on the VA-WH MAMMOGRAM SCREENING reminder definition.</p>
<p>The status of the reminder should be “RESOLVED.” Alternatively, use the clinical maintenance view in the CPRS GUI. The status of the reminder should be “RESOLVED.”</p>
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
<p><strong>Test Reminders</strong></p>
</blockquote></th>
<th><ol start="2" type="1">
<li><p>If you use the WH package, select a patient whose most recent mammogram in the WH package has a RESULTS/DIAGNOSIS that is blank and a STATUS that is OPEN.</p></li>
</ol>
<blockquote>
<p>Run the Reminder Test option on the VA-WH MAMMOGRAM REVIEW RESULTS reminder definition.</p>
<p>The status of the reminder should be “DUE.”</p>
<p>Alternatively, use the clinical maintenance view in the CPRS GUI. The status of the reminder should be “DUE.”</p>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>Select a patient whose most recent mammogram screening took place within the past year and the results have been recorded. Run the Reminder Test option on VA-WH MAMMOGRAM SCREENING reminder definition.</p>
</blockquote></li>
</ol>
<blockquote>
<p>The status of the reminder should be “Applicable.”</p>
<p>Use the clinical maintenance view in the CPRS GUI. The status of the reminder should be "Applicable."</p>
</blockquote>
<ol start="4" type="1">
<li><blockquote>
<p>Repeat steps 1-3 for the PAP Reminders.</p>
</blockquote></li>
</ol></th>
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
<p><span id="_bookmark18" class="anchor"></span><strong>Add Reminders to CPRS Cover Sheet</strong></p>
</blockquote></th>
<th><ol start="6" type="1">
<li><p><strong>Add the nationally distributed reminders to the CPRS Cover Sheet.</strong></p></li>
</ol>
<blockquote>
<p>(NOTE: Make sure that New Reminders Parameter on the CPRS Configuration Menu is set to Yes. This is required in order to use the “Edit Cover Sheet Reminder List” functionality.)</p>
</blockquote>
<ol type="a">
<li><p>Open a patient chart, click on the reminders clock, and when the available Reminders window opens, click on Action, and then select “Edit Cover Sheet Reminder List.”</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/012.png)

![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/013.png)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Add Reminders to CPRS Cover Sheet</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Adding Reminders to Cover Sheet, cont’d</strong></p>
</blockquote>
<ol start="2" type="a">
<li><p>When the Cover Sheet Reminder List opens, set the Cover sheet parameter level. Click on the System, Division, Service, User Class, and/or User buttons, as appropriate for your site.</p></li>
<li><blockquote>
<p>Locate and click on the VA-WH MAMMOGRAM SCREENING reminder; click the Add button (or double-click the reminder).</p>
</blockquote></li>
<li><blockquote>
<p>Click on the VA-WH MAMMOGRAM REVIEW RESULTS reminder and click the Add button (or double-click the reminder).</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>CRPROVIDER,ONE</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CRPROVIDER,ONE</strong></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>CRPROVIDER,ONE</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>CRPROVIDER,ONE</strong></p>
</blockquote></td>
</tr>
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
<p><span id="_bookmark19" class="anchor"></span><strong>WV Notification Setup</strong></p>
<p><strong>NOTE:</strong></p>
<p>Your site can choose whether to include the Print Now button on screening reminder dialogs. This can be set with a new option on the CPRS Reminder Configuration menu: PXRM WH PRINT NOW</p>
</blockquote></th>
<th><ol start="7" type="1">
<li><p><strong>Set up entries in the WV Notification Purpose file</strong></p></li>
</ol>
<blockquote>
<p>Use the AEP Add/Edit a Notification Purpose &amp; Letter manager option in the Women's Health package to customize letters in the WV Notification Purpose file for each PAP and mammogram entry installed as part of this project. The breast or cervical treatment need and due date should be set and the default letter text should be modified to explain the reason for the letter.</p>
<p><em>See Step 1c and Appendix E in this manual for examples.</em></p>
<p><strong>NOTE:</strong> If your site chooses not to send letters via the WH package, copy the appropriate national dialog components to local components and remove the findings related to WH notifications.</p>
<p><strong>NOTE</strong>: Several entries beginning with “CPRS UPDATE” were made in the WV Notification Purpose file as part of the WH installation. These notification purposes are used by the screening reminders dialogs to set screening frequency and should not be modified.</p>
</blockquote>
<ol start="8" type="1">
<li><p><strong>Determine how and where letters will be printed.</strong></p></li>
</ol>
<blockquote>
<p>Your site needs to determine if letters will be queued to the WH package and will be printed in the Case Manager’s office, or if the clinician will use the Print Now option, to print and mail the letters from the clinician’s office.</p>
<p><strong>Print Now flag</strong>: The “Print Now” selection is optional. A parameter can be set (at the system level) to allow the “Print Now” button to be added to the dialog. By default “Print Now” is turned off: the CPRS Reminder Configuration Option called WH Print Now Active is released with a Value of NO. If the value is changed to YES, the “Print Now” button will appear on the dialog. Whether the “Print Now” button is added to the dialog or not, the default will always be that the letter is queued to the WH package.</p>
<p>The text in the progress note will be one of the following:</p>
<p>Print Now Active/<strong>Yes</strong>: Letter queued to print at Device Name on finish Date/Time</p>
<p>Print Now Active/<strong>No</strong>: Letter queued to WH package Date/Time</p>
<p><strong>If your site chooses No, identify where letters will print and who will be responsible for retrieving and mailing these.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><span id="Test_Dialogs" class="anchor"></span><strong>Test Dialogs</strong></p>
</blockquote></th>
<th><ol start="9" type="1">
<li><p><strong>Verify that the dialogs function properly</strong></p></li>
</ol>
<blockquote>
<p>Test the WH Reminder dialogs in CPRS, using either the exported dialogs or your locally created dialogs. Using point-and-click reminder resolution processing through CPRS GUI, verify the following:</p>
</blockquote>
<ul>
<li><p>Correct Progress Note text is posted</p></li>
<li><p>Finding Item gets sent to PCE</p></li>
<li><p>Reminder is satisfied</p></li>
</ul>
<blockquote>
<p>Check the Clinical Maintenance component display in CPRS after testing dialogs to ensure that all the activities are tested are reflected in the clinical maintenance display.</p>
<p><em><strong>Steps to test dialogs:</strong></em></p>
</blockquote>
<ol type="1">
<li><p>On the cover sheet, click on the Reminders icon.</p></li>
<li><p>Click on reminders in the Reminders box to see details of a reminder.</p></li>
<li><blockquote>
<p>Open the Notes tab and select New Note. Enter a title.</p>
</blockquote></li>
<li><p>Open the Reminders drawer and review the contents.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Test Dialogs</strong></p>
</blockquote></th>
<th><ol start="8" type="1">
<li><p><strong>(cont’d) Verify that the dialogs function properly</strong></p></li>
</ol>
<blockquote>
<p><em><strong>Steps to test dialogs:</strong></em></p>
</blockquote>
<ol start="5" type="1">
<li><p>Locate the VA-WH Mammogram Screening reminder dialog and open it.</p></li>
<li><p>In the dialog box, check relevant actions.</p></li>
<li><p>Finish the reminder processing.</p></li>
<li><blockquote>
<p>Review the text added to the note to assure its correctness.</p>
</blockquote></li>
<li><p>Ensure that the reminder can be satisfied by the individual finding items that were mapped to the reminder terms.</p></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Example: Mammogram Screening Dialog

![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/014.png)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Test Dialogs</strong></p>
</blockquote></th>
<th><ol start="9" type="1">
<li><p><strong>(cont’d) Verify that the dialogs function properly</strong></p></li>
<li><blockquote>
<p>Check the Clinical Maintenance component display in Health Summaries and CPRS after the reminder dialog is complete.</p>
</blockquote></li>
<li><blockquote>
<p>Repeat steps 5-10 for all the dialogs.</p>
</blockquote></li>
</ol></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> ![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/015.png)Example: Mammogram Screening Clinical Maintenance Display

> Setup Guide – Testing Dialogs

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Test Dialogs</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>9. (cont’d) Verify that the dialogs function properly</strong></p>
<p><strong>NOTE: Remember to “refresh” the screen after completing a dialog, if you want to see the updated status immediately. This is especially critical if you’re doing the screening reminder and want to see if the screening reminder has been resolved.</strong></p>
<p>Also remember to save notes and change the visit date between tests to simulate a normal process. <strong>To test features like change in frequency</strong>, you may need to enter a series of historical entries. Some findings resolve the reminder for up to 9 months, while others make the reminder due again in 4 or 6 months, 1, 2 or 3 years. You will need to create visits within these time frames of 4 -6 months or 1-2-3 years in order to see the results.</p>
<p><strong>To test the PAP smear review reminder</strong>, you will need to enter a PAP smear into the VistA Lab package. Once the results are verified and released, results will be added to WH if the WH parameters have been set up to receive them. See page 12. If the patient is not in the WH package, a WH patient record will be added; then the results will be loaded and the PAP reminder will be due.</p>
<p><strong>To test the mammogram review reminder</strong>, you will need to enter mammogram results into the VistA Radiology package. Once the results are verified and released, results will be added to WH if the WH parameters have been set up to receive them. See page 12. If the patient is not in the WH package, a WH patient record will be added; then the results will be loaded and the mammogram reminder will be due.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><span id="Activate_Alerts" class="anchor"></span><strong>10. Activate alerts</strong></p>
<p>Three new information alerts are exported with this software. They notify clinicians or designated users when radiology and lab results are available.</p>
<p>All new notifications/alerts are exported in a "disabled" state. This allows sites to selectively enable them when they are ready and the users have been forewarned. CACs enable notifications/alerts as follows:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Select OPTION NAME: <strong>ORMGR</strong> CPRS Manager Menu menu</p>
<p>Select CPRS Manager Menu Option: <strong>PE</strong> CPRS Configuration (Clin Coord) Select CPRS Configuration (Clin Coord) Option: <strong>NO</strong> Notification Mgmt Menu Select Notification Mgmt Menu Option: <strong>1</strong> Enable/Disable Notifications</p>
<p>Set PROCESSING FLAG Parameters for Notifications Processing Flag may be set for the following:</p>
</blockquote>
<ol type="1">
<li><p>User USR [choose from NEW PERSON]</p></li>
<li><p>Team (OE/RR) OTL [choose from OE/RR LIST]</p></li>
<li><p>Service SRV [choose from SERVICE/SECTION]</p></li>
<li><p>Location LOC [choose from HOSPITAL LOCATION]</p></li>
<li><p>Division DIV [choose from INSTITUTION]</p></li>
<li><blockquote>
<p>System SYS [xxx] Enter selection: <strong>6</strong> System</p>
</blockquote></li>
</ol>
<blockquote>
<p>------- Setting Processing Flag for System: DEVCUR.FO-SLC.MED.VA.GOV -------</p>
<p>Select Notification: <strong>ANATOMIC PATHOLOGY RESULTS</strong></p>
<p>Notification: ANATOMIC PATHOLOGY RESULTS// <strong>&lt;Enter&gt;</strong> ANATOMIC PATHOLOGY RESULTS ANATOMIC PATHOLOGY RESULTS</p>
<p>Value: Disabled// <strong>Enabled</strong></p>
<p>Select Notification: <strong>MAMMOGRAM RESULTS</strong></p>
<p>Are you adding MAMMOGRAM RESULTS as a new Notification? Yes//<strong>&lt;Enter&gt;</strong> YES</p>
<p>Notification: MAMMOGRAM RESULTS//<strong>&lt;Enter&gt;</strong> MAMMOGRAM RESULTS MAMMOGRAM RESULTS</p>
<p>Value: <strong>Enabled</strong></p>
<p>Select Notification: <strong>PAP SMEAR RESULTS</strong></p>
<p>Are you adding PAP SMEAR RESULTS as a new Notification? Yes//<strong>&lt;Enter&gt;</strong> YES</p>
<p>Notification: PAP SMEAR RESULTS// <strong>&lt;Enter&gt;</strong> PAP SMEAR RESULTS PAP SMEAR RESULTS</p>
<p>Value: <strong>Enabled</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="Appendix_A:_KIDS_Installation_Example" class="anchor"></span>Install Package(s)

> Select INSTALL NAME: wv\*1.0\*16 Loaded from Distribution Loaded from Distribution 2/5/05@16:08:06

> =\> WV\*1.0\*16, LR\*5.2\*311, OR\*3.0\*210, PXRM\*2.0\*1 ;Created on Feb 04, 200

> This Distribution was loaded on Feb 05, 2005@16:08:06 with header of

> WV\*1.0\*16, LR\*5.2\*311, OR\*3.0\*210, PXRM\*2.0\*1 ;Created on Feb 04, 2005@17:17

> :36

> It consisted of the following Install(s):

> WV\*1.0\*16 LR\*5.2\*311 OR\*3.0\*210 PXRM\*2.0\*1

> Checking Install for Package WV\*1.0\*16 Install Questions for WV\*1.0\*16 Incoming Files:

> 790.02 WV SITE PARAMETER (Partial Definition) Note: You already have the 'WV SITE PARAMETER' File.

1.  WV PROCEDURE (Partial Definition) Note: You already have the 'WV PROCEDURE' File.
2.  WV PROCEDURE TYPE

> Note: You already have the 'WV PROCEDURE TYPE' File.

> 790.404 WV NOTIFICATION PURPOSE (Partial Definition) Note: You already have the 'WV NOTIFICATION PURPOSE' File.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// n NO Checking Install for Package LR\*5.2\*311

> Install Questions for LR\*5.2\*311

> Checking Install for Package OR\*3.0\*210 Install Questions for OR\*3.0\*210 Incoming Files:

> 100.9 OE/RR NOTIFICATIONS (including data) Note: You already have the 'OE/RR NOTIFICATIONS' File. I will OVERWRITE your data with mine.

> Checking Install for Package PXRM\*2.0\*1

> Will first run the Environment Check Routine, PXRMWHEV Environment check passed, ok to install PXRM\*2.0\*1 Install Questions for PXRM\*2.0\*1

> Incoming Files:

41. REMINDER DIALOG (including data) Note: You already have the 'REMINDER DIALOG' File. I will OVERWRITE your data with mine.
42. REMINDER GUI PROCESS (including data) Note: You already have the 'REMINDER GUI PROCESS' File. I will REPLACE your data with mine.

> 801.45 REMINDER FINDING TYPE PARAMETER (including data) Note: You already have the 'REMINDER FINDING TYPE PARAMETER' File. I will OVERWRITE your data with mine.

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will REPLACE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? YES// n NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// n NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// 0;80;99999 TELNET WV\*1.0\*16

> Install Started for WV\*1.0\*16 :

> Feb 05, 2005@16:22:38

> Build Distribution Date: Feb 04, 2005 Installing Routines:

> Feb 05, 2005@16:22:39

> Installing Data Dictionaries:

> Feb 05, 2005@16:22:39

> Installing PACKAGE COMPONENTS:

> Installing FORM

> Feb 05, 2005@16:22:41

> Running Post-Install Routine: ^WV16PST

> Will build new 'AC' x-ref on FILE 790.1 in background job \#2272

> Updating Routine file... Updating KIDS files...

> WV\*1.0\*16 Installed.

> Feb 05, 2005@16:22:42

> Install Message sent \#432 \[1;1H LR\*5.2\*311 Install Started for LR\*5.2\*311 :

> Feb 05, 2005@16:22:43

> Build Distribution Date: Feb 04, 2005 Installing Routines:

> Feb 05, 2005@16:22:43

> Running Post-Install Routine: EN^LR311PST Creating index definition ...

> Creating index definition ... Updating Routine file...

> Updating KIDS files...

> LR\*5.2\*311 Installed.

> Feb 05, 2005@16:22:45

> Install Message sent \#433 OR\*3.0\*210 Install Started for OR\*3.0\*210 :

> Feb 05, 2005@16:22:45

> Build Distribution Date: Feb 04, 2005 Installing Routines:

> Feb 05, 2005@16:22:45

> Installing Data Dictionaries:

> Feb 05, 2005@16:22:45

> Installing Data:

> Feb 05, 2005@16:22:46

> Running Post-Install Routine: POST^ORY210 Updating Routine file...

> Updating KIDS files...

> OR\*3.0\*210 Installed.

> Feb 05, 2005@16:22:46

> Install Message sent \#434 PXRM\*2.0\*1 Install Started for PXRM\*2.0\*1 :

> Feb 05, 2005@16:22:46

> Build Distribution Date: Feb 04, 2005 Installing Routines:

> Feb 05, 2005@16:22:47

> Running Pre-Install Routine: PRE^PXRMWHPI Installing Data Dictionaries:

> Feb 05, 2005@16:22:49

> Installing Data:

> Feb 05, 2005@16:22:51

> Running Post-Install Routine: POST^PXRMWHPI Installing reminder VA-WH MAMMOGRAM REVIEW RESULTS

> ADDITIONAL FINDING entry Q.WH BREAST ULTRASOUND - UNILATERAL does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> ADDITIONAL FINDING entry Q.WH BREAST ULTRASOUND - BILATERAL does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> ADDITIONAL FINDING entry Q.WH MAMMOGRAM - UNILATERAL does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> ADDITIONAL FINDING entry Q.WH MAMMOGRAM - BILATERAL does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> Installing reminder VA-WH MAMMOGRAM SCREENING

> Finding RP.MAMMOGRAM BILAT SCREEN does not exist; input a replacement or ^ to quit the install.

> Select RAD/NUC MED PROCEDURES NAME: chest

1.  chest 2 views pa&lat CHEST 2 VIEWS PA&LAT (RAD Detailed) CPT:71020
2.  chest 4 views CHEST 4 VIEWS (RAD Detailed) CPT:71030
3.  chest apical lordotic CHEST APICAL LORDOTIC (RAD Detailed) CPT:71021
4.  chest include fluoro CHEST INCLUDE FLUORO (RAD Detailed) CPT:71034
5.  chest oblique projections CHEST OBLIQUE PROJECTIONS (RAD Detailed) CPT:71022

> Press \<RETURN\> to see more, '^' to exit this list, OR

> CHOOSE 1-5: 1 CHEST 2 VIEWS PA&LAT (RAD Detailed) CPT:71020

> Finding RP.MAMMOGRAM BILAT SCREEN does not exist; input a replacement or ^ to quit the install.

> Select RAD/NUC MED PROCEDURES NAME: chest

1.  chest 2 views pa&lat CHEST 2 VIEWS PA&LAT (RAD Detailed) CPT:71020
2.  chest 4 views CHEST 4 VIEWS (RAD Detailed) CPT:71030
3.  chest apical lordotic CHEST APICAL LORDOTIC (RAD Detailed) CPT:71021
4.  chest include fluoro CHEST INCLUDE FLUORO (RAD Detailed) CPT:71034
5.  chest oblique projections CHEST OBLIQUE PROJECTIONS (RAD Detailed) CPT:71022

> Press \<RETURN\> to see more, '^' to exit this list, OR

> CHOOSE 1-5: 2 CHEST 4 VIEWS (RAD Detailed) CPT:71030 ADDITIONAL FINDING entry Q.WH REFER TO WOMEN'S HEALTH CLINIC does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> ADDITIONAL FINDING entry Q.WH MAMMOGRAM - UNILATERAL does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> ADDITIONAL FINDING entry Q.WH MAMMOGRAM - BILATERAL does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> ADDITIONAL FINDING entry Q.WH MAMMOGRAM - BILATERAL does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> Installing reminder VA-WH PAP SMEAR REVIEW RESULTS

> ADDITIONAL FINDING entry Q.WH CERVICAL ORDERS does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> ADDITIONAL FINDING entry Q.WH PAP SMEAR REPEAT CONSULT does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> Installing reminder VA-WH PAP SMEAR SCREENING

> FINDING entry Q.WH REFER TO WOMEN'S HEALTH CLINIC does not exist.

> Select one of the following:

> D Delete (from the reminder/dialog)

> P Replace (in the reminder/dialog) with an existing entry Q Quit the install

> Enter response: p Replace (in the reminder/dialog) with an existing entry Select ORDER DIALOG NAME: zzPRE-OP

> UPDATING FORCE VALUE: PXRM WH UPDATE TREATMENT NEED UPDATING FORCE VALUE: PXRM WH NOTIFICATION TYPE

> Updating Routine file... Updating KIDS files...

> PXRM\*2.0\*1 Installed.

> Feb 05, 2005@16:23:37

> Install Message sent \#435 Install Completed

# Appendix B: Key Points to WH Reminders Installation and Setup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PAP and Mammogram screening and review reminders will be installed as part of the patch.

1.  The Screening reminders replace prior national screening reminders
2.  All four reminders have new dialogs to assist with data entry
1.  To satisfy the PAP smear screening reminder, completed PAP Smears must be recorded in the patient record as one of the following:
    1.  Laboratory package Cytology or Surgical Pathology SNOMED results
    2.  Women's Health package procedure with results
    3.  Health Factor (Historical outside results)
    4.  PCE CPT procedure code
    5.  Completed consult order for outside procedure
2.  To satisfy the mammogram screening reminder, completed mammograms must be recorded in the patient record as one of the following:
    1.  Verified results in the Radiology package
    2.  Women's Health package procedure with results
    3.  Health Factor (Historical outside results)
    4.  PCE CPT procedure code
    5.  Completed consult order for outside procedure
3.  PAP review reminder will only come due if:
    1.  WH is automatically updated with procedure results from the VistA Lab package
    2.  If this does not take place, do not release the PAP review reminder
4.  Mammogram review reminder will only come due if:
    1.  WH is automatically updated with procedure results from the VistA Radiology package & status for imported mammograms is set to “OPEN”
    2.  If this does not take place, do not release the Mammogram review reminder
5.  If your site does not record PAP smear results in the VistA Lab package:
    1.  You could change procedures at your site so PAP smear results are entered into the VistA Lab package
    2.  Recording and verifying/releasing results in the VistA Lab package will automatically satisfy the PAP screening reminder
    3.  Recording results in the WH package will automatically satisfy the PAP screening reminder
    4.  Automatically updating WH from the Vista Lab package will allow sites to use the PAP Review reminder
    5.  If your site does not automatically update WH from Lab, the PAP smear review reminder will not come due, and you might choose not to release it.
6.  If your site does not record mammogram results in the VistA Radiology package:
    1.  You could change procedures at your site so mammogram results are entered into the VistA Radiology package
    2.  Recording and verifying results in the VistA Radiology package will automatically satisfy the mammogram screening reminder
    3.  Recording results in the WH package will automatically satisfy the mammogram screening reminder
    4.  Automatically updating WH from the Vista Radiology package will allow sites to use the mammogram review reminder.
    5.  If your site does not automatically update WH from Radiology, the mammogram review reminder will not come due, and you might choose not to release it.
7.  Apply updates to WV NOTIFICATION PURPOSE file before installing reminders:
    1.  Several new entries created to work with the screening and review reminders
    2.  Review reminders reference these entries and will be resolved if they have been added to the file
    3.  Sites will have to go back after the install and manually enter each item into the dialogs if the file is not updated first,
8.  Update Notification boilerplate text with your site address and content:
    1.  If necessary, edit your WH default notification letter so it contains your site’s address and phone number
    2.  Copy your default WH notification into each of the new notifications and customize the text of each new notification to fit the needs of your site, using WH option “AEP -Add/Edit a Notification Purpose & Letter”
    3.  Once you set up the letter you want, respond with “NO” when asked if you want to replace the custom letter with the default letter
9.  For the new Lab computed finding to work, sites must use the WH option

> “PAP-Link Pap Smear with SNOMED Codes” to map Lab SNOMED codes to WH

10. New Functional Finding logic is used to alter reminder frequency, so frequency is not specified on the findings.
11. Enable new alerts through CPRS Manager menu, so that informational alerts about lab pap smears and radiology mammogram results are sent to clinicians.

# Appendix C: Reminders Installation with Reminder Exchange Utility 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The post-install routine, POST^PXRMV2I, installs the packed reminders into your Exchange File. If you discover that the reminder didn’t get installed, you can use the Exchange options on the Reminders Manager Menu to install the “packed” reminders. The following examples can guide you in doing this.

1.  Select Reminder Exchange from the Reminder Managers Menu. From the Reminder Exchange actions, select IFE for the reminder that contains the dialog that is not installed. You may need to press enter one or more times (or use the Search List action) to locate the correct entry.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Clinical Reminder Exchange Jul 15, 2004@13:32:42 Page: 1 of 8</p>
<p>Exchange File Entries.</p>
<p>Entry Source Date Packed</p>
</blockquote>
<ol type="1">
<li><p>AGP DIALOG GROUP TEST CRPROVIDER@SALT LAKE 07/01/2004@11:00:03</p></li>
<li><p>AGP INSTALL TEST CRPROVIDER@SALT LAKE 06/30/2004@12:55:48</p></li>
<li><p>BDI II RESULT GROUP CRPROVIDER@SALT LAKE 04/13/2004@15:53:47</p></li>
<li><p>CDUE CRPROVIDER@SALT LAKE 08/08/2003@10:59:52</p></li>
<li><p>CHA UNVESTED PATIENTS CRUSER@CHARLESTON,S 09/26/2001@13:00:59</p></li>
<li><p>CODE SET TEST CRPROVIDER@SALT LAKE 06/26/2003@12:17:02</p></li>
<li><p>CONDTEST CRPROVIDER@SALT LAKE 08/18/2003@12:02:18</p></li>
<li><p>Dialog Transport Reminder CRUSER@DURHAM 12/16/2002@15:37:51</p></li>
<li><p>FFTEST CRPROVIDER@SALT LAKE 09/10/2003@15:14:21</p></li>
<li><p>GMTSMHV CRPROVIDER@SALT LAKE 07/06/2004@15:06:21</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CFE Create Exchange File Entry IH Installation History CHF Create Host File LHF Load Host File</p>
<p>CMM Create MailMan Message LMM Load MailMan Message</p>
<p>DFE Delete Exchange File Entry LR List Reminder Definitions IFE Install Exchange File Entry RI Reminder Definition Inquiry Select Action: Next Screen// <strong>IFE</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  When you are prompted for the entry number, select the number for the dialog.

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 41%" />
<col style="width: 2%" />
<col style="width: 19%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Clinical Reminder Exchange Jul 15, 2004@13:36:59</p>
</blockquote></th>
<th>Page: 8 of 8</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Exchange File Entries.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>+ Entry Source</p>
</blockquote></td>
<td><blockquote>
<p>Date Packed</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>45 TIU*1*112 20040325 CRDeveloper@ALBANY</p>
</blockquote></td>
<td>03/25/2004@14:20:47</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>46 TIU512 TEST CRPROVIDER@SALT LAKE</p>
</blockquote></td>
<td>07/26/2002@06:48:34</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>47 VA-*IHD 412 ELEVATED LDL RE CRPROVIDER@SALT LAKE</p>
</blockquote></td>
<td>05/11/2004@11:30:33</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>48 VA-*IHD 412 LIPID PROFILE R CRPROVIDER@SALT LAKE</p>
</blockquote></td>
<td>05/11/2004@11:32:04</td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>49 VA-*IHD ELEVATED LDL REPORT CRPROVIDER@SALT LAKE</p>
</blockquote></td>
<td>05/11/2004@11:27:07</td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>50 VA-*IHD LIPID PROFILE REPOR CRPROVIDER@SALT LAKE</p>
</blockquote></td>
<td>05/11/2004@11:28:42</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p><strong>+ Next Screen - Prev Screen</strong></p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>?? More Actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>CFE</td>
<td><blockquote>
<p>Create Exchange File Entry</p>
</blockquote></td>
<td><blockquote>
<p>IH</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Installation History</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>CHF Create Host File LHF Load Host File</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>CMM Create MailMan Message LMM Load MailMan Message</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DFE</td>
<td><blockquote>
<p>Delete Exchange File Entry</p>
</blockquote></td>
<td><blockquote>
<p>LR</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>List Reminder Definitions</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IFE</td>
<td><blockquote>
<p>Install Exchange File Entry</p>
</blockquote></td>
<td><blockquote>
<p>RI</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Reminder Definition Inquiry</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>Select Action: Quit// IFE Install Exchange File Entry</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>Select Entry(s): (45-50): <strong>47</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  When the dialog screen comes up select IA.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Exchange File Components Jul 15, 2004@13:46:52 Page: 1 of 4</p>
<p>Component Category Exists</p>
<p>Reminder: VA-*IHD 412 ELEVATED LDL REPORTING Source: CRPROVIDER,THREE at SALT LAKE CITY OIFO</p>
<p>Date Packed: 05/11/2004@11:30:33</p>
<p>Description:</p>
<p>Compliance reporting measures the management of IHD patients with an ICD-9 412.nn diagnosis, whose most recent LDL is greater than or equal to 120mg/dl as defined by the VA External Peer Review Program (EPRP) performance measure and the maximum guideline recommended below:</p>
<p>The VHA/DOD Clinical Practice Guideline for Management of Dyslipidemia recommends an LDL goal of &lt;120 mg/dl for patients with Ischemic Heart Disease; and the NCEP Adult Treatment Panel II recommends a more stringent goal of &lt;100 mg/dl.</p>
<p>This national IHD 412 Elevated LDL Reporting reminder is used monthly</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ Enter ?? for more actions</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IA Install all Components IS Install Selected Component Select Action: Next Screen// <strong>IA</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

4.  If you are prompted for items that are missing, either replace or delete the item. Do not select quit. This should install the dialog.

> <span id="Appendix_D:_WV*1*16_Description" class="anchor"></span><u>Appendix D: WV\*1\*16 Description</u>

> DHCP Patch Display Page: 1

> =============================================================================

> Run Date: SEP 30, 2004 Designation: WV\*1\*16 TEST v9

> Package : WOMEN'S HEALTH Priority : MANDATORY

> Version : 1 Status : UNDER DEVELOPMENT

> =============================================================================

> Associated patches: (v)WV\*1\*9 \<\<= must be installed BEFORE \`WV\*1\*16' (v)WV\*1\*10 \<\<= must be installed BEFORE \`WV\*1\*16' (v)WV\*1\*15 \<\<= must be installed BEFORE \`WV\*1\*16' (v)WV\*1\*17 \<\<= must be installed BEFORE \`WV\*1\*16'

> Subject: WH-CLINICAL REMINDERS LINK

> Category: ROUTINE

> DATA DICTIONARY ENHANCEMENT OTHER INFORMATIONAL

> Description:

> ===========

> Associated NOIS: \<None\> Associated E3Rs: 18684

> Test Sites:

> ===========

> Northern California HCS Loma Linda

> Washington D.C.

> This patch is part of a multi-KIDS build that includes PXRM\*2\*1 (Clinical Reminders), LR\*5.2\*311 (Laboratory) and OR\*3\*210 (CPRS). Please see the patch description for PXRM\*2\*1 for information on retrieving the host file containing these patches.

> The Technical Integration approval has been received for the data dictionary changes.

> This patch is an enhancement. It adds functionality that allows the Women's Health (WH) package to send data to the Clinical Reminders (CR) package to resolve Mammogram and Pap Smear reminders. Also, the CR package will be able to send data to the WH package to update the WH database.

1)  The following APIs are added:
    1.  GETPARAM^WVSITE returns WH site parameters for the facility indicated. It is documented in Integration Agreement (IA) 4101.

> GETPARAM(.RESULT,IEN)

> <u>Input:</u>

> .RESULT = Array name to return data in. (Required) IEN = INSTITUTION file (#4) IEN. (Required)

> Output:

> RESULT(0)=1st piece is 1 (for Success) or -1 (Failure) 2nd piece is the reason for failure

> RESULT(1)=1st piece is 1 (for Yes) or 0 (for No or null).

> This is the value of the UPDATE RESULTS/DX (#.11) field in the WV SITE PARAMETER (#790.02) file.

> 2nd piece is 1 (for Yes) or 0 (for No or null).

> This is the value of the UPDATE TREATMENT NEEDS (#.12) field in the WV SITE PARAMETER (#790.02) file.

> Example:

- D GETPARAM(.RESULT,499) ZW RESULT
- RESULT(0)=1^
- RESULT(1)=1^1
  1.  RESULTS^WVALERTS returns an array with data for the WV PROCEDURE (#790.1) file entry specified. It is documented in IA 4102.

> RESULTS(.RESULT,IEN)

> Input:

> .RESULT = Array name to return data in. (Required)

> IEN = The internal entry number of a WV PROCEDURE (#790.1) file entry. (Required)

> Output:

> RESULT(0) = piece1^piece2^piece3^piece4^piece5^piece6^piece7^piece8

> ^piece9^piece10

> where: piece1 = WV PROCEDURE (#790.1) file entry number piece2 = patient DFN

> piece3 = 'Breast Ultrasound', 'Mammogram' or 'Pap Smear' piece4 = Date of procedure (FileMan internal format) piece5 = Radiology procedure name

> piece6 = Primary radiology diagnosis

> piece7 = One or more radiology modifiers separated by tildes (~)

> piece8 = Lab package test date (external format) piece9 = Lab accession number

> piece10 = Lab specimen text

> If the entry is not found, piece 1 will contain '-1' and piece 3 will contain an error message.

> If the entry is a Pap Smear, then pieces 5 through 7 are null.

> If the entry is a Mammogram or Breast Ultrasound, then pieces 8 through 10 are not returned.

> Example of a Pap Smear:

- D RESULTS(.RESULT,313) ZW RESULT
- RESULT(0)=313^94^Pap Smear^3030131^^^^01/31/2003^CY 03 6^PAP SMEAR

> Example of a Mammogram:

- D RESULTS(.RESULT,314) ZW RESULT
- RESULT(0)=314^94^Mammogram^3030321^MAMMOGRAM SCREENING^NORMAL

> ^LEFT~RIGHT

1.  LETTER^WVRPCNO1 returns the letter text for the WV NOTIFICATION PURPOSE (#790.404) file entry specified. It is documented in IA 4103.

> LETTER(.RESULT,IEN)

> Input:

> .RESULT = Array name to return data in. (Required)

> IEN = WV NOTIFICATION PURPOSE (#790.404) file IEN. (Required)

> Output:

> RESULT(0) = Blank if the entry exists \<OR\> -1^error message RESULT(n) = Lines of letter text where 'n' is a sequential number

> Example:

- D LETTER(.RESULT,1) ZW RESULT
- RESULT(0)=
- RESULT(1)=
- RESULT(2)=
- RESULT(3)= Women's Health Clinic
- RESULT(4)=
- RESULT(5)= 123 Main Street
- RESULT(6)=
- RESULT(7)= CHICAGO, IL 60612
- RESULT(n)= ...
  1.  NEW^WVRPCNO is used to update a procedure result in File 790.1, create a notification entry in FILE 790.4, print a notification and update a patient's treatment needs. It is documented in IA 4104.

> NEW(.RESULT,.NOTIF)

> Input:

> RESULT = This is an array that identifies what FILE 790.1 entries will be updated and the result code to use. (Optional) RESULT(n)=FILE 790.1 IEN^"A", "N" or "U"

> Where: n is a number greater than zero.

> The first piece is the WV PROCEDURE (790.1) file IEN.

> The second piece is a one character code that identifies the diagnosis. 'A' stands for Abnormal, 'N' stands for Normal and 'U' stands for Unsatisfactory (e.g., 1234^N).

> NOTIF = This is an array that identifies the notification purposes to use to create entries in the WV NOTIFICATION (790.4) file. (Optional)

> NOTIF(FILE 790.404 IEN,n) = FILE 790.1 IEN^Type^FILE 3.5

> NAME^DFN

> Where: The first array subscript is a FILE 790.404 internal entry number (IEN).

> The second subscript is a sequential number starting with 1.

> The first piece of data in the node is the FILE

> 790.1 IEN which identifies the procedure performed.

> The second piece is a one character code that identifies the type of notification. 'I' stands for In-person, 'L' stands for Letter and 'P' stands for "Phone".

> The third piece identifies the print device. It consists of the FILE 3.5 IEN, a semi-colon and the .01 value of the entry (e.g., 5;HPLASERJET).

> The fourth piece is the patient IEN (i.e., DFN) from FILE 2.

> Output: A notification letter for a patient may be printed based on the input parameter values. However, no values are sent back to the calling routine.

> Example:

- S RESULT(1)="313^N"
- S NOTIF(20,1)="313^L^5;HPLASERJET^94"
- D NEW(.RESULT,.NOTIF)

> One new field is added to the WV PROCEDURE (#790.1) file. It is:

> .16 PROCESSED Y/N?

1.  LATEST^WVRPCPR returns a list of entries for Pap Smear, Mammogram or Breast Ultrasound in reverse chronological order for the search criteria identified in the input parameters. It is documented in IA 4105.

> LATEST(.RESULT,DFN,TYPE,DATES,MAX,DX)

> Input:

> .RESULT = Array name for return values. (Required) DFN = Patient DFN. (Required)

> TYPE = A set of codes where "P" stands for Pap Smear, "M" for Mammogram or "U" for Breast Ultrasound. (Required)

> DATES = A date range in FileMan internal format separated by an uparrow (e.g., 3020101^3021231). (Optional).

> The default is the previous 3 years.

> MAX = The maximum number of entries to return. (Optional) The default value is 10.

> DX = A set of codes that identify a category of results where "N" stands for Normal, "A" stands for Abnormal, "P" stands for Pending and "\*" (asterisk) stands for everything. (Optional)

> The default is "\*". It returns entries that

> are marked as "Unsatisfactory for DX" as well as Normal, Abnormal and Pending.

> Output:

> RESULT(0) = Number of matches

> RESULT(n) = IEN^DFN^DATE^TYPE^DX CATEGORY^DX Result^RAD/LAB link

> ^STATUS

> where n = A sequential number starting with 1 IEN = FILE 790.1 internal entry number

> DFN = FILE 2 internal entry number

> DATE = Procedure date in FileMan format TYPE = Procedure name (from FILE 790.2)

> DX Category = 'Normal', 'Abnormal' or 'Pending' DX Result = FILE 790.31, Field .01 value

> RAD/LAB LINK = 0 stands for no link to radiology

> or lab package

> 1 stands for link to radiology or lab package

> STATUS = FILE 790.1 entry status. 'OPEN' or 'CLOSED'

> If no matches were found, RESULT(0)=-1^error message.

> Example:

- D LATEST(.RESULT,94,"M","3030101^3031231",10,"\*") ZW RESULT
- RESULT(0)=1^
- RESULT(1)=314^94^3030321^MAMMOGRAM SCREENING^Normal^Negative^1^OPEN
  1.  RESULTS^WVALERTF returns any report text for a pap smear, mammogram or breast ultrasound for the WV PROCEDURE (#790.1) file entry identified. It is documented in IA 4106.

> RESULTS(.RESULT,IEN)

> Input:

> RESULT = Array name that will identify the global reference containing the report text (Required).

> IEN = The internal entry number of the FILE 790.1 entry to return data on (Required).

> Output:

> ^TMP("WV RPT",\$J,n,0) = report text

> where n is a sequential number starting with 1.

> If the entry is not found, the first node of the global array is returned with a '-1' in the first piece and an error message

> in the third piece:

> ^TMP("WV RPT",557902502,1,0) = -1^^Entry not found.

> Example of report text found:

- D RESULTS(.RESULT,313) ZW RESULT
- RESULT=^TMP("WV RPT",557902502)
- D ^%G
- ^TMP("WV RPT",557902502,1,0) = DAY-CASE \#: 032103-1515
- ^TMP("WV RPT",557902502,2,0) = EXAM DATE/TIME: MAR 21, 2003@13:30
- ^TMP("WV RPT",557902502,3,0) = VERIFYING PHYSICIAN: TAYLOR,FRANK
- ^TMP("WV RPT",557902502,4,0) = PROCEDURE: MAMMOGRAM SCREENING
- ...
- ...
2)  A new option, Link Pap Smear with SNOMED Codes \[WV PAP SMEAR SNOMED CODES\], is added to the File Maintenance Menu \[WV MENU-FILE MAINTENANCE\]. With this option facilities can identify SNOMED codes used by their Lab Service when coding a Lab test that is a Pap Smear. The SNOMED codes

> identified here can be matched to the SNOMED codes used in a Lab report to determine if that test is a Pap Smear. Currently, the WH user must look at the lab test and decide whether the lab test is a pap smear. After this patch is installed and the SNOMED codes are entered here, the WH software can make that determination automatically.

> Several new fields are added to the WV PROCEDURE TYPE (#790.2) file. They are: 1 MORPHOLOGY SNOMED CODE (subfile \#790.21)

> .01 MORPHOLOGY SNOMED CODE

> 1 DIAGNOSIS

> 2 TOPOGRAPHY SNOMED CODE (subfile \#790.22)

> .01 TOPOGRAPHY SNOMED CODE

3)  The Edit Site Parameters \[WV EDIT SITE PARAMETERS\] option is modified to add two new prompts:
    1.  "Update Result/Dx Field?:" - If set to YES, the data sent from CR will be used to update the patient's procedure data in FILE 790.1. If set to NO or null, no updating will be done.

> The value for this response is stored in a new field, UPDATE RESULTS/DX (.11), in the WV SITE PARAMETER (#790.02) file.

2.  "Update Treatment Needs?:" - If set to YES, the data sent from CR will be used to update the patient's treatment needs in FILE 790. If set to NO or null, no updating will be done.

> The value for this response is stored in a new field, UPDATE TREATMENT NEEDS (.12), in the WV SITE PARAMETER (#790.02) file.

4)  The Add/Edit a Notification Purpose & Letter \[WV ADD/EDIT NOT PURPOSE&LETTER\] option is modified to add four new prompts:
    1.  "Breast Treatment Need:" - This prompt is for a new field, BR

> TX NEED (.07), in the WV NOTIFICATION PURPOSE (#790.404) file. This

> field points to FILE 790.51 and shows the choices related to breast treatment needs.

2.  "Breast Treatment Due Date:" - This prompt is for a new field, BR TX DUE DATE (.08), in the WV NOTIFICATION PURPOSE (#790.404) file. This field is the amount of time to add to a procedure

> date or the current date to calculate a new breast treatment due date. The value should be a number followed by "D", "M" or "Y" (without the quotes). D indicates days. M indicates months. Y indicates years. For example, "90D" means add 90 days to the procedure date or current date to calculate the new breast treatment due date. This new treatment date will be automatically assigned to the patient in the WV PATIENT file (#790).

3.  "Cervical Treatment Need:" - This prompt is for a new field, CX

> TX NEED (.09), in the WV NOTIFICATION PURPOSE (#790.404) file. This

> field points to FILE 790.5 and shows the choices related to cervical treatment needs.

4.  "Cervical Treatment Due Date:" - This prompt is for a new field, CX TX DUE DATE (.1), in the WV NOTIFICATION PURPOSE (#790.404) file. This field is the amount of time to add to procedure date or the current date to calculate a new cervical treatment due date. The value should be a number followed by "D", "M" or "Y" (without the quotes). D indicates days. M indicates months. Y indicates years. For example, "90D" means add 90 days to the procedure date or current date to calculate the new cervical treatment due date. This new treatment date will be automatically assigned to the patient in the WV PATIENT file (#790).

> If the "Update Treatment Needs?" parameter (3b above) is set to Yes and there are values in fields a-d, the software will use these values to update the patient's treatment needs in the WV PATIENT (#790) file.

5)  The Print Notification Purpose & Letter File \[WV PRINT NOTIF PURPOSE&LETTER\] option is modified to display in the report output the values of the four new fields identified in \#4 above.
6)  The following new entries are added to the WV NOTIFICATION PURPOSE (#790.404) file:

> CPRS UPDATE PAP TX NEED 4M CPRS UPDATE PAP TX NEED 6M CPRS UPDATE PAP TX NEED 3Y CPRS UPDATE PAP TX NEED 2Y CPRS UPDATE PAP TX NEED 1Y CPRS UPDATE MAM TX NEED 1Y CPRS UPDATE MAM TX NEED 2Y CPRS UPDATE MAM TX NEED 6M CPRS UPDATE MAM TX NEED 4M

> MAM result NEM, next MAM 1Y MAM result NEM, next MAM 2Y MAM result NEM, next MAM 4M MAM result NEM, next MAM 6M

> MAM result abnormal, F/U MAM 4M MAM result abnormal, F/U MAM 6M PAP result NEM, next PAP 1Y

> PAP result NEM, next PAP 2Y PAP result NEM, next PAP 3Y PAP result NEM, next PAP 4M PAP result NEM, next PAP 6M

> PAP result abnormal, F/U PAP 4M PAP result abnormal, F/U PAP 6M MAM unsatisfactory, need repeat Pap unsatisfactory, need repeat

> PAP result NEM, further screening not required MAM result NEM, further screening not required

> Facilities may customize these entries and use them when resolving Pap Smears and Mammograms or continue to use the entries they created locally. Use the Add/Edit a Notification Purpose & Letter \[WV ADD/EDIT NOT PURPOSE&LETTER\] option to customize these new entries.

7)  The following entries are added or modified in the WV RESULTS/DIAGNOSIS (#790.31) file:
    1.  No Evidence of Malignancy - This is a new entry that can be used to result a mammogram, pap smear or breast ultrasound.
    2.  Abnormal - This is a new entry that can be used to result a mammogram, pap smear or breast ultrasound.
    3.  Unsatisfactory for DX - This is an existing entry that is modified to result a breast ultrasound, too.
8)  A new-style Index is added to the WV PROCEDURE (#790.1) file. The 'AC' index will provide a quicker search for entries needed by CR. A post-installation routine will index the existing entries in the file. The format of the index node is: ^WV(790.1,"AC",DFN,DATE,DA)=""

> where: DFN = is the FILE 2 IEN of the patient

> DATE = the date of procedure (FileMan internal format) DA = the FILE 790.1 IEN

9)  Before this patch, a mail message was sent to the patient's WH Case Manager when a mammogram was added to the WH database by the link with the Radiology/NM package or when a lab report was verified by the Lab package.

> After this patch is installed, the WH package will tell the CPRS package to send a CPRS alert notification to the WH Case Manager and to the provider associated with the procedure.

# Appendix E: Setting up Notification Letters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Step 1 – Edit default letter (one time only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Use FileMan to edit the default WH letter template in WV LETTER file \#790.6. Edit all the parts that will be common to all letters:

> Site address

> Site phone number Greeting Signature

> WH looks for the name GENERIC SAMPLE LETTER.

####### This should be done by a CAC or ADPAC, not by the end user.

> \>\>D P^DI

> VA FileMan 22.0

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES INPUT TO WHAT FILE: WV LETTER//

> EDIT WHICH FIELD: ALL//

> Note: This site has more than one default letter, but WH will only use the one named GENERIC SAMPLE LETTER.

> Select WV LETTER: ?

> Answer with WV LETTER Choose from:

> GENERIC SAMPLE LETTER

> OLD GENERIC SAMPLE LETTER TEST GENERIC LETTER

> You may enter a new WV LETTER, if you wish

> NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH PUNCTUATION

> Note: The letter templates contain objects that will be used to pull in patient information. This text is from page 2.3 of the WH User Manual:

> The patient’s name, address, and SSN will appear automatically within the letter at the places demarcated by the vertical bars “\|\|” (e.g., \|SSN\|) when the letter is printed. This information is obtained from the WV PATIENT file (#790). If you do not wish to have a certain piece of information displayed in the letter, you should edit the text of the letter and remove that field name (e.g., SSN) and the vertical bars that surround it.

> Other information that appears in the letter is the clinic name and address. This information is typed within quotes. You should edit the text between the quotes to display the correct clinic name and address (Note: Leave the quotes). If you plan on printing your letters on paper that

> contains a letterhead you will want to remove altogether the lines containing the clinic name and address.

> The field \|NOWRAP\| should be left as is. This permits the text of the letter to be printed as it appears on the terminal screen. Other fields may be deleted if not desired. For example,

> \|TODAY\| and \|NOW\| will print out the current date and date/time respectively. Future appointments may be included to print in a notification letter by typing the text “\|APPOINTMENTS\|” (without the quotes) in the text of the letter.

> Because of the specific syntax of the fields and the possibility of corrupting them during edits, a recovery utility has been provided. The program to edit a purpose of notification always asks first if you wish to replace the existing form letter with a ‘generic sample letter’. Answering ‘Yes’ to that question will replace the existing form with a generic sample letter, which includes all of the original fields in their proper syntax.

> Select WV LETTER: generIC SAMPLE LETTER

> LETTER: GENERIC SAMPLE LETTER Replace

> LETTER TEXT:. . .

> . . .

> Person’s Name, title Your clinic

> Your phone number: nnn-nnnn

> printed: \|NOW\| Edit? NO// y YES

> Note: Now editing GENERIC SAMPLE LETTER – change items that are highlighted Before the default GENERIC SAMPLE LETTER is edited:

> ==\[ WRAP \]==\[ INSERT \]=============\< LETTER TEXT \>===========\[ \<PF1\>H=Help \]====

> \|NOWRAP\|

> \|CENTER("Women's Health Clinic")\|

> \|CENTER("Your Street")\|

> \|CENTER("Your City, ST Zip Code")\|

> \|TODAY\|

> \|\$E(SSN#,6,9)\|

> \|\$P(NAME,",",2)\| \|\$P(NAME,",")\|

> \|COMPLETE ADDRESS\|

> \- - - -

> Dear Ms. \|\$P(NAME,",",1)\|,

> This is the body of the letter and should be edited to say what you want for this Purpose of Notification.

> Sincerely,

######## Person’s Name, title Your clinic

> Your phone number: nnn-nnnn

> printed: \|NOW\|

> \<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

> After the default GENERIC SAMPLE LETTER has been edited:

> ==\[ WRAP \]==\[ INSERT \]=============\< LETTER TEXT \>===========\[ \<PF1\>H=Help \]====

> \|NOWRAP\|

> \|CENTER("Women's Health Clinic")\|

> \|CENTER("123 Clinic Street")\|

> \|CENTER("Clinic City, SS 77777")\|

> \|TODAY\|

> \|\$E(SSN#,6,9)\|

> \|\$P(NAME,",",2)\| \|\$P(NAME,",")\|

> \|COMPLETE ADDRESS\|

> \- - - -

> Dear Ms. \|\$P(NAME,",",1)\|,

> This is the body of the letter and should be edited to say what you want for this Purpose of Notification.

> Sincerely,

######## WHNURSE, ONE, LPN

> Women's Health Program Phone: 777-7777

> printed: \|NOW\|

> \<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

### Step 2 – Edit/customize each individual notification letter (at least one time for each letter)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the WH option AEP Add/Edit a Notification Purpose & Letter to edit each individual notification letter in the WV NOTIFICATION PURPOSE file \# 790.404.

#### MF Manager's Functions ...

> FM File Maintenance Menu ...

> AEP Add/Edit a Notification Purpose & Letter

> Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?

> Enter Yes or No: NO//

> Reply “YES” to this question the first time you edit each individual notification letter, to copy the GENERIC SAMPLE LETTER from WV LETTER file into the letter you are editing. When you save the customized letter, it will be saved in the WV NOTIFICATION PURPOSE file.

> Reply “NO” to this question if you need to further customize a letter that has already been customized. Otherwise, by replying “YES” again, you will replace the customized letter with the default letter and lose all your former customized text. This may be desirable if some of the special coding has been corrupted and needs to be replaced so the letter will pull in the patient data correctly.

> DVF,DEV\>D ^XUP

> Select OPTION NAME: women'S HEALTH MENU WVMENU Women's Health Menu menu Women's Health Main Menu v1.0 SALT LAKE CITY HCS

> PM Patient Management ... MR Management Reports ... MF Manager's Functions ...

> Select Women's Health Menu Option: mf Manager's Functions

> WOMEN'S HEALTH: \* MANAGER'S FUNCTIONS \* SALT LAKE CITY HCS

> FM File Maintenance Menu ... PQ Print Queued Letters

> MPM Manager's Patient Management ... LDE Lab Data Entry Menu ...

> Select Manager's Functions Option: fm File Maintenance Menu

> WOMEN'S HEALTH: \* FILE MAINTENANCE MENU \* SALT LAKE CITY HCS

> AEP Add/Edit a Notification Purpose & Letter PPL Print Notification Purpose & Letter File ESN Edit Synonyms for Notification Types

> OUT Add/Edit Notification Outcomes ESP Edit Site Parameters

> CM Add/Edit Case Managers

> TR Transfer a Case Manager's Patients AUTO Automatically Load Patients

> RAD Import Radiology/NM Exams PRD Print Results/Diagnosis File

> ESR Edit Synonyms for Results/Diagnoses PSR Print Synonyms for Results/Diagnoses EDX Edit Diagnostic Code Translation File PDX Print Diagnostic Code Translation File RS Add/Edit to Referral Source File

> PAP Link Pap Smear with SNOMED Codes

> Select File Maintenance Menu Option: aep Add/Edit a Notification Purpose & Letter

> \* \* \* WOMEN'S HEALTH: EDIT NOTIFICATION PURPOSE & LETTER FILE \* \* \*

> Select WV NOTIFICATION PURPOSE: pap result nem

1.  PAP RESULT NEM, FURTHER SCREEN PAP result NEM, further screening not r equired ROUTINE
2.  PAP RESULT NEM, NEXT PAP 1Y PAP result NEM, next PAP 1Y PN1Y ROUTI

> NE

3.  PAP RESULT NEM, NEXT PAP 2Y PAP result NEM, next PAP 2Y PN2Y ROUTI

> NE

4.  PAP RESULT NEM, NEXT PAP 3Y PAP result NEM, next PAP 3Y PN3Y ROUTI

> NE

5.  PAP RESULT NEM, NEXT PAP 4M PAP result NEM, next PAP 4M PN4M ROUTI

> NE

> Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 2 PAP result NEM, next PAP 1Y PN1Y ROUTINE

> First edit: Enter “YES” to copy the GENERIC SAMPLE LETTER to start a brand new letter or to replace an existing letter

> Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?

> Enter Yes or No: NO// YES

> Additional edits: Enter “NO” if you want to edit the text of an existing letter and DO NOT want to replace existing letter content with the GENERIC SAMPLE LETTER:

> Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?

> Enter Yes or No: NO// NO

> Tab to the FORM LETTER (WP) field and hit RETURN key:

> \* \* \* EDIT NOTIFICATION PURPOSE & LETTER \* \* \*

> Purpose of Notification: PAP result NEM, next PAP 1Y

> Active: YES Synonym: PN1Y

Priority: ROUTINE FORM LETTER (WP): +

> Result or Reminder Letter: RESULT Associate with BR or CX Tx: CERVICAL

> Breast Treatment Need: Breast Treatment Due Date:

> Cervical Treatment Need: Routine PAP

> Cervical Treatment Due Date: 1Y

> After the GENERIC SAMPLE LETTER has been copied into the FORM LETTER for the

> PAP result NEM, next PAP 1Y notification letter and before this individual notification letter has been customized:

> ==\[ WRAP \]==\[ INSERT \]=============\< LETTER TEXT \>===========\[ \<PF1\>H=Help \]====

> \|NOWRAP\|

> \|CENTER("Women's Health Clinic")\|

> \|CENTER("123 Clinic Street")\|

> \|CENTER("Clinic City, SS 77777")\|

> \|TODAY\|

> \|\$E(SSN#,6,9)\|

> \|\$P(NAME,",",2)\| \|\$P(NAME,",")\|

> \|COMPLETE ADDRESS\|

> \- - - -

> Dear Ms. \|\$P(NAME,",",1)\|,

######## This is the body of the letter and should be edited to say what you want for this Purpose of Notification.

> Sincerely,

> WHNURSE, ONE, LPN

> Women's Health Program Phone: 777-7777

> printed: \|NOW\|

> \<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

> After the individual notification letter has been customized:

> ==\[ WRAP \]==\[ INSERT \]=============\< LETTER TEXT \>===========\[ \<PF1\>H=Help \]====

> \|NOWRAP\|

> \|CENTER("Women's Health Clinic")\|

> \|CENTER("123 Clinic Street")\|

> \|CENTER("Clinic City, SS 11111")\|

> \|TODAY\|

> \|\$E(SSN#,6,9)\|

> \|\$P(NAME,",",2)\| \|\$P(NAME,",")\|

> \|COMPLETE ADDRESS\|

> \- - - -

> Dear Ms. \|\$P(NAME,",",1)\|,

######## The results of your latest PAP smear are NEM (No Evidence of Malignancy).

> We would like to see you again in 1 year for your regular PAP smear screening. We will mail you a reminder letter in advance of that date, or you may schedule the appointment yourself by calling our Family Medicine Clinic at 777-7777 or our Women's Clinic at 777-7777.

> Sincerely,

> WHNURSE, ONE

> Women's Health Program Phone: 555-7777

> printed: \|NOW\|

> \<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

### Adding a new Dialog Element/Purpose of Notification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Steps

#### Create a new note in WH

1.  Create a dialog element that includes WH.note, HF.health factor, and prompt PXRM WH NOTE TYPE
2.  Copy National reminder dialog to a local reminder dialog
3.  Add your new dialog element to the local copy of reminder dialog

> Create dialog element

> The items added are bold, and the things that are necessary are underlined. Screen shots follow.

> ![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/016.png)

> ![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/017.png)

> In Women’s Health package:

> Women's Health Main Menu v1.0

> MF Manager's Functions ...

> FM File Maintenance Menu ...

> AEP Add/Edit a Notification Purpose & Letter

> Select WV NOTIFICATION PURPOSE: LET'S DO LUNCH ASAP

#### Do you wish to delete the old letter for this Purpose of Notification and replace it with the generic sample letter?

> Enter Yes or No: NO//

> <span id="Appendix_F:_Local_Dialog_Modification_to" class="anchor"></span>Appendix F: Local Dialog Modification to Trigger Order <u>Menu </u>

![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/018.png)

> Then when the Finish button is clicked, the order menu comes up:

> ![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/019.png)

> <span id="Appendix_G:_How_to_customize_WH_reminder" class="anchor"></span>Appendix G: How to customize WH reminders and <u>dialogs after installation </u>

#### During testing at the Washington D.C. VA, we had some problems. Here is what we did to fix them. We hope this information helps sites fix problem reminders and reminder dialogs

> The clinician noticed these problems with the VA-WH Mammogram Screening reminder and reminder dialog:

1.  Order selection item Mammogram – screening was linked to the wrong quick order

#### Selection item for other mammogram orders were not linked to any quick order and needed to be removed

2.  Selection item for Order – refer to Women’s Health Provider did not apply to this site and should be removed

![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/020.png)

#### These are the changes that were made to the dialog, using options on the PXRM MANAGERS MENU:

1.  Copy the national reminder dialog to create a local reminder dialog
    1.  National dialog: VA-WH MAMMOGRAM SCREENING Print name: Mammogram Screening
    2.  Local dialog: DC VA-WH MAMMOGRAM SCREENING Print name: Mammogram Screening – Local
2.  Order mammogram is a group, so you need to copy the national group over to a local group
    1.  National group: VA-WH GP ORDERS - MAMMOGRAM SCREEN
    2.  Local group: DC VA-WH GP ORDERS - MAMMOGRAM SCREEN
3.  This is what the new group DC VA-WH GP ORDERS - MAMMOGRAM SCREEN looks like:
1.  Group: DC VA-WH GP ORDERS - MAMMOGRAM SCREEN
2.  5 Element: VA-WH OR MAMMOGRAM SCREENING
3.  10 Element: VA-WH OR MAMMOGRAM BILAT
4.  15 Element: VA-WH OR MAMMOGRAM UNILAT

#### Edit the local group DC VA-WH GP ORDERS - MAMMOGRAM SCREEN and remove selection options 3 & 4 from the dialog group and this is what the group will look like when you’re done:

1.  Group: DC VA-WH GP ORDERS - MAMMOGRAM SCREEN
2.  5 Element: VA-WH OR MAMMOGRAM SCREENING
4.  Order mammogram is also part of a group Screening, so you need to copy this national group over to a local group:

#### National group: VA-WH GP MAMMOGRAM SCREENING

1.  Local group: DC VA-WH GP MAMMOGRAM SCREENING
5.  This is what the new group DC VA-WH GP ORDERS - MAMMOGRAM SCREEN looks like:

######## Group: DC VA-WH GP MAMMOGRAM SCREENING

1.  5 Group: VA-WH GP ORDERS - MAMMOGRAM SCREEN
2.  5.5 Element: VA-WH OR MAMMOGRAM SCREENING
3.  5.10 Element: VA-WH OR MAMMOGRAM BILAT
4.  5.15 Element: VA-WH OR MAMMOGRAM UNILAT
5.  10 Element: VA-WH MAMMOGRAM DONE OUTSIDE

#### Edit the local group DC VA-WH GP ORDERS - MAMMOGRAM SCREEN and remove selection options 3 & 4 from the dialog group and this is what the group will look like when you’re done:

######## Group: DC VA-WH GP MAMMOGRAM SCREENING

1.  5 Group: DC VA-WH GP ORDERS - MAMMOGRAM SCREEN
2.  5.5 Element: VA-WH OR MAMMOGRAM SCREENING

> i\. 10 Element: VA-WH MAMMOGRAM DONE OUTSIDE

#### Edit the local dialog DC VA-WH MAMMOGRAM SCREENING and replace the national group with the local group:

1.  National group: VA-WH GP ORDERS - MAMMOGRAM SCREEN
2.  Local group: DC VA-WH GP ORDERS - MAMMOGRAM SCREEN
6.  Edit the local dialog DC VA-WH MAMMOGRAM SCREENING and remove this selection options
    1.  Order – refer to Women’s Health Provider
7.  Create a quick order for mammogram screening if your site does not already have one using option ORCM QUICK ORDERS Enter/edit quick orders
8.  Edit the national element VA-WH OR MAMMOGRAM SCREENING to point ADDITIONAL FINDINGS to the correct quick order:

> Select ADDITIONAL FINDINGS: Q.GMRCZ

> <u>1 GMRCZ CARDIOLOGY CONSULT</u>

2.  GMRCZ DIETICIAN
3.  GMRCZ EEG
4.  GMRCZ MAMMOGRAM
5.  GMRCZ PT FOR PNEUMONIA

> Press \<RETURN\> to see more, '^' to exit this list, OR CHOOSE 1-5: 5 GMRCZ MAMMOGRAM

> Select ADDITIONAL FINDINGS: ?

> Answer with ADDITIONAL FINDINGS:

> GMRCZ MAMMOGRAM

> IRM noticed these problems during installation:

#### Finding items for Radiology mammogram procedures could not be mapped because all mammograms are done off site and VistA Radiology package did not have procedures for mammograms.

1.  When the order selections were removed from the dialog, it left health factor findings in the reminder that needed to be removed.

> These are the changes that needed to be made to the reminder:

1.  Copy the national Mammogram Screening reminder to a local reminder
    1.  National: VA-WH MAMMOGRAM SCREENING
    2.  Local: DC VA-WH MAMMOGRAM SCREENING
2.  Edit the print name so you will be able to tell it from the national reminder
    1.  National: Mammogram Screening
    2.  Local: Mammogram Screening - Local
3.  Copy this national reminder term to local reminder term and remove all the finding items for Radiology. Also edit the description of the term to explain why you are removing the findings.
    1.  National: VA-WH MAMMOGRAM SCREEN IN RAD PKG
    2.  Local: DC VA-WH MAMMOGRAM SCREEN IN RAD PKG

> ---- Begin: DC VA-WH MAMMOGRAM SCREEN IN RAD PKG (FI(5)=RT(462)) -------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Mapped Findings:

######## Mapped Finding Item: RP.MAMMOGRAM BILAT

> Condition: I V("PDX")'\["UNSATISFACTORY"&(V("SDX","\*")'\["UNSATISFACTORY")

######## Mapped Finding Item: RP.MAMMOGRAM BILAT

> Condition: I V("PDX")'\["UNSATISFACTORY"&(V("SDX","\*")'\["UNSATISFACTORY")

######## Mapped Finding Item: RP.MAMMOGRAM UNILAT

> Condition: I V("PDX")'\["UNSATISFACTORY"&(V("SDX","\*")'\["UNSATISFACTORY")

> ---- End: DC VA-WH MAMMOGRAM SCREEN IN RAD PKG ------------------------

#### Copy this national reminder term to a local reminder term and remove all the finding items for Radiology (RP.)

3.  National: VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG
4.  Local: DC VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG

> ---- Begin: VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG (FI(10)=RT(473))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Mapped Findings:

######## Mapped Finding Item: RP.MAMMOGRAM BILAT

> Condition: I V("PDX")\["UNSATISFACTORY"&(V("SDX","\*")\["UNSATISFACTORY")

######## Mapped Finding Item: RP.MAMMOGRAM BILAT

> Condition: I V("PDX")\["UNSATISFACTORY"&(V("SDX","\*")\["UNSATISFACTORY")

######## Mapped Finding Item: RP.MAMMOGRAM UNILAT

> Condition: I V("PDX")\["UNSATISFACTORY"&(V("SDX","\*")\["UNSATISFACTORY")

> Mapped Finding Item: CF.VA-WH MAMMOGRAM IN WH PKG Condition: I (V("VALUE")="Unsatisfactory")

> Condition Case Sensitive: NO

> ---- End: VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH PKG ----------------

#### Copy this national reminder term to local reminder term and remove the finding items for the two health factors belonging to the orders we removed from the dialog:

5.  National: VA-WH BREAST CARE ORDER HEALTH FACTOR
6.  Local: DC VA-WH BREAST CARE ORDER HEALTH FACTOR

> ---- Begin: VA-WH BREAST CARE ORDER HEALTH FACTOR (FI(7)=RT(471)) -----

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Beginning Date/Time: T-9M

> Mapped Findings:

> Mapped Finding Item: HF.WH ORDER MAMMOGRAM SCREEN HF Health Factor Category: WH MAMMOGRAM

######## Mapped Finding Item: HF.WH ORDER MAMMOGRAM BILAT HF

> Health Factor Category: WH MAMMOGRAM

######## Mapped Finding Item: HF.WH ORDER MAMMOGRAM UNILAT HF

> Health Factor Category: WH MAMMOGRAM

> ---- End: VA-WH BREAST CARE ORDER HEALTH FACTOR -----------------------

#### Edit the local Mammogram Screening reminder and replace the three national reminder terms with the three local terms:

> Reminder Definition Findings Choose from:

<table style="width:100%;">
<colgroup>
<col style="width: 4%" />
<col style="width: 57%" />
<col style="width: 12%" />
<col style="width: 17%" />
<col style="width: 3%" />
<col style="width: 3%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RT</strong></th>
<th><blockquote>
<p><strong>DC VA-WH BREAST CARE ORDER HEALTH FACTOR</strong></p>
</blockquote></th>
<th></th>
<th><strong>Finding</strong></th>
<th><strong>#:</strong></th>
<th><blockquote>
<p><strong>7</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>RT</strong></td>
<td><blockquote>
<p><strong>DC VA-WH MAMMOGRAM SCREEN IN RAD PKG</strong></p>
</blockquote></td>
<td></td>
<td><strong>Finding</strong></td>
<td><strong>#:</strong></td>
<td><blockquote>
<p><strong>5</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>RT</strong></td>
<td><blockquote>
<p><strong>DC VA-WH MAMMOGRAM UNSATISFACTORY IN RAD/WH</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>PKG</strong></p>
</blockquote></td>
<td><strong>Finding</strong></td>
<td><strong>#:</strong></td>
<td><blockquote>
<p><strong>10</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RT</td>
<td><blockquote>
<p>VA-TERMINAL CANCER PATIENT</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RT</td>
<td><blockquote>
<p>VA-WH BILATERAL MASTECTOMY</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RT</td>
<td><blockquote>
<p>VA-WH HX BREAST CANCER/ABNORMAL MAM</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>15</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RT</td>
<td><blockquote>
<p>VA-WH MAMMOGRAM ORDER</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>16</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RT</td>
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN DEFER</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>9</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RT</td>
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN DONE</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>6</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RT</td>
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN FREQ - 1Y</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>13</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RT</td>
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN FREQ - 2Y</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>14</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RT</td>
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN FREQ - 4M</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>11</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RT</td>
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN FREQ - 6M</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>12</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>RT</td>
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN IN WH PKG</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RT</td>
<td><blockquote>
<p>VA-WH MAMMOGRAM SCREEN NOT INDICATED</p>
</blockquote></td>
<td></td>
<td>Finding</td>
<td>#:</td>
<td><blockquote>
<p>8</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### This is the result of the dialog changes:

![](pxrm-2-1-integration-with-women-s-health-reminders-installation-and-setup-guide/021.png)

> <span id="Index" class="anchor"></span><u>Index</u>

#### Activate alerts, 61

> Add and Edit Notification Letters, 28 Add Reminders to CPRS Cover Sheet, 54 Add/Edit Case Managers, 22

> alerts, 3, 23, 61

> APPENDIX A: KIDS Load & Installation Example, 62

> APPENDIX B: Key Points to WH Reminders Installation and Setup, 68

> APPENDIX C: Reminders Installation with Reminder Exchange Utility, 70

> Appendix D: WV\*1\*16 Description, 72 Appendix E: Setting up Notification Letters,

> 80

> Appendix F – Local Dialog Modification to trigger order menu, 91

> Appendix G: How to customize WH reminders and dialogs after installation, 93

> Benefits, 1

> case manager, 22

> CPRS GUI, 20

> CPT, 7

> Default Case Manager, 25 Diagnostic Code, 35

> dialogs, 18

> dummy quick order, 10

> Edit Diagnostic Code Translation File:, 35 Edit Site Parameters, 25

> Editing Dialogs, 48

> Exchange Utility, 70

> File Maintenance Menu, 24 Files, 8

> forced values, 51

> FTP, 13

> FTP Addresses, 13

> HL7, 7

> ICD, 7

> Import Mammograms from Radiology, 25 Import Tests from Laboratory, 25 Installation Example, 62

> Installation Instructions, 13

> Installation Order, 12

> Installation Time, 7

> Installation with Reminder Exchange Utility, 70

> interface with the Women's Health, 22

> Kernel, 7

> Key Points to WH Reminders Installation and Setup, 68

> KIDS, 14

> LABORATORY, 25

> letters, 56

> Lexicon, 7

> Link Pap Smear with SNOMED Codes, 31 Local Dialog Modification to trigger order

> menu, 91

> LR\*5.2\*311, 3

> MailMan, 7

> Mammogram Review, 34 Mammogram Screening Dialog, 58 Mammogram Terms, 37

> Mapping, 37

> Notification, 23

> Notification Letters, 26, 80

> Notification Purpose, 29 Notification type definitions, 51 notification/alerts, 3

> options to put out of order, respond with:, 15 OR\*3.0\*210, 3

> Order Dialog, 10

> Order Entry/Results Reporting, 7 order menu, 91

> Ordering a Consult, 51 Overview, 1

> packed reminders, 16 patches in build, 2 POST^PXRMWHP, 16

> Post-Installation Procedures, 16 Pre and Post-Install Routines, 8 Pre-Install Worksheet, 10, 11

> Print Diagnostic Code Translation File, 35 Print Now flag, 56

> Project Goals, 20

> PXRM WH UPDATE TREATMENT NEED, 51

> queued, 56

> queued letters, 56

> quick orders, 5

> RADIOLOGY, 25

> refresh” the screen, 60

> Reminder Term Management, 37 Reminder Test, 47

> Required Packages, 7

> rescinded, 1

> Result/Diagnosis code, 35

> Routine Mapping, 9

> Routines, 9

> Set up entries in the WV Notification Purpose file, 56

> Setup Overview, 20

> SNOMED, 4, 22

> Status Given to Imported Mammograms, 34, 35

> Term Mapping Recommendations, 37 terms, 17

> Test Dialogs, 57

> Testing Reminders, 53 Text Integration Utilities, 7 TOPOGRAPHY, 22

> VA FileMan, 7

> VA FileMan Print from the Reminder Term File, 17

> VA-\*BREAST CANCER SCREEN, 1

> VHA policy, 1

> Web sites, 6

> WH dialogs, 19

> Women’s Health Case Manager, 5 Women’s Health Package, 21 WV\*1\*16 Description, 72

> WV\*1.0\*16, 2