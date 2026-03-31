---
title: PXRM*2*38 Lung and Prostate Cancer, Symptom Assessment Scale Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Lung and Prostate Cancer, Symptom Assessment Scale Install Guide
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*38
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: "> NOTE: Patch PXRM\2.0\38 released the documentation associated with the patch. However, after release, an error was found in the install guide where sites were instructed to map Reminder Dialog templates to a national standard title, HEMATOLOGY AND ONCOLOGY PROGRESS NOTE that was INACTIVE. This has"
audience: 
keywords: 
  - blockquote
  - strong
  - class
  - health
  - style
  - width
  - dialog
  - table
  - colspan
  - reminder
page_count: 0
word_count: 4476
section_count: 11
table_count: 0
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: December 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_38_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_38_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/001.png)

> National Oncology Program Office

> VA-Oncology Lung Cancer Reminder Dialog VA-Oncology Prostate Cancer Reminder Dialog

> VA-Symptom Assessment Scale (VSAS) Reminder Dialog

> PXRM\*2.0\*38

> INSTALLATION and SETUP GUIDE

> Product Development Department of Veterans Affairs

> December 2014

> Updated May 2015

> Product Development Department of Veterans Affairs

1.  [Retrieve the host file from one of the following locations (with the ASCII file type) 5](#retrieve-the-host-file-from-one-of-the-following-locations-with-the-ascii-file-type)
2.  [Install the patch first in a training or test account 5](#_bookmark7)
3.  [Load the distribution. 5](#load-the-distribution.)
4.  [Backup a Transport Global 6](#backup-a-transport-global)
    1.  [Compare Transport Global to Current System 6](#compare-transport-global-to-current-system)
5.  [Install the build. 6](#install-the-build.)
6.  [Install File Print 6](#install-file-print)
7.  [Build File Print 7](#build-file-print)
8.  [Post-installation routines 7](#post-installation-routines)

[VA-Oncology Lung Cancer Reminder Dialog 7](#va-oncology-lung-cancer-reminder-dialog)

[Component Inventory 7](#component-inventory)

1.  [Reminder Dialog Name 7](#reminder-dialog-name)
2.  [Branching Terms 7](#branching-terms)
3.  [Health Factors 8](#health-factors)
4.  [Patient Data Objects 8](#patient-data-objects)

[Post-Installation Set-up 8](#post-installation-set-up)

5.  [Enable the dialog 8](#enable-the-dialog)
6.  [Remove disabled from Reminder Dialog 9](#remove-disabled-from-reminder-dialog)
7.  [Creating a shared folder 10](#creating-a-shared-folder)
8.  [Creating a shared templates 11](#creating-a-shared-templates)
9.  [Creating a local progress note title 12](#creating-a-local-progress-note-title)
10. [Linking progress note to reminder dialog 14](#linking-progress-note-to-reminder-dialog)

[VA-Oncology Prostate Cancer Reminder Dialog 14](#va-oncology-prostate-cancer-reminder-dialog)

[Component Inventory 14](#_bookmark29)

1.  [Reminder Dialog Name 15](#reminder-dialog-name-1)
2.  [Branching Term 15](#branching-term)
3.  [Health Factors 15](#health-factors-1)
4.  [Patient Data Objects 15](#patient-data-objects-1)

[Post-Installation Set-up 16](#post-installation-set-up-1)

5.  [Configuring two new Health Summary types/TIU objects/health summary objects 16](#configuring-two-new-health-summary-typestiu-objectshealth-summary-objects)
6.  [Enabling the dialog 19](#enabling-the-dialog)
7.  [Remove disable from reminder dialog 20](#remove-disable-from-reminder-dialog)
8.  [Creating a shared folder 20](#creating-a-shared-folder-1)
9.  [Creating a shared template 21](#creating-a-shared-template)
10. [Creating a local progress note title 22](#creating-a-local-progress-note-title-1)

[23](#_bookmark41)

11. [Linking progress note to reminder dialog 24](#linking-progress-note-to-reminder-dialog-1)

[Component Inventory 25](#component-inventory-1)

1.  [Reminder Dialog Name 26](#reminder-dialog-name-2)
2.  [Health Factors 26](#health-factors-2)
3.  [GMRV Vital Type 26](#_bookmark46)
4.  [TIU Template Field 26](#tiu-template-field)

[Post-Installation Set-up 26](#post-installation-set-up-2)

5.  [Enabling the dialog 26](#enabling-the-dialog-1)
6.  [Remove disabled from reminder dialog 28](#remove-disabled-from-reminder-dialog-1)
7.  [Creating a shared folder 29](#creating-a-shared-folder-2)
8.  [Creating shared templates 29](#creating-shared-templates)
9.  [Creating a local progress note title 30](#creating-a-local-progress-note-title-2)
10. [Linking progress note to reminder dialog 32](#linking-progress-note-to-reminder-dialog-2)

## Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> NOTE: Patch PXRM\*2.0\*38 released the documentation associated with the patch. However, after release, an error was found in the install guide where sites were instructed to map Reminder Dialog templates to a national standard title, HEMATOLOGY AND ONCOLOGY PROGRESS NOTE that was INACTIVE. This has been corrected in this version of the Install Guide to have sites map Reminder Dialog templates to national standard title HEMATOLOGY AND ONCOLOGY NOTE. This new document, PXRM_2_0_38_IG.PDF, is being released as part of an informational patch PXRM\*2.0\*59.

> This patch releases three oncology reminder dialogs without any changes to routines, data dictionaries, or other package functions – “content” only. The reminder dialogs are:

> VA-ONCOLOGY LUNG CANCER REMINDER DIALOG, VA-ONCOLOGY PROSTATE CANCER REMINDER DIALOG, VA-SYMPTOM ASSESSMENT SCALE (VSAS) REMINDER DIALOG.

> The National Oncology Program Office seeks to provide tools to VA facilities to enable providers to format essential clinical data so that it is readily available for clinical care and to measure the quality of care in the VA in a prospective, timely, and cost-efficient manner. Using Reminder Dialogs in CPRS is one mechanism to support these goals. Reminder dialogs will include information necessary for quality assessment as defined by the National Quality Forum, ASCO's Quality Oncology Practice Initiative, and other reliable and up-to-date sources.

> Reminder dialogs will enable the standardization of clinical information necessary for quality indicators into a discrete format and obtain key elements to continuously monitor the quality of cancer care.

> These reminder dialogs were developed and are supported by the National Oncology Program Office in Specialty Care Services (part of Patient Care Services). <span class="mark">REDACTED</span>

> \*\*Please note there are 3 separate dialogs contained in this patch. Be sure you are in the correct dialog when using these instructions.

## Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Required Software for PXRM\*2\*38

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 20%" />
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
<p>NATIONAL DRUG FILE</p>
</blockquote></td>
<td><blockquote>
<p>PSN</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Pharmacy Data Management</p>
</blockquote></td>
<td><blockquote>
<p>PSS</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Outpatient Pharmacy</p>
</blockquote></td>
<td><blockquote>
<p>PSO</p>
</blockquote></td>
<td><blockquote>
<p>7.0</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA FileMan</p>
</blockquote></td>
<td><blockquote>
<p>DI</p>
</blockquote></td>
<td><blockquote>
<p>22</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Related Documentation

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Documentation</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Documentation File name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Installation and Setup Guide</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_0_38_IG.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>User Guide</p>
</blockquote></td>
<td><blockquote>
<p>PXRM*2.0*38 user guide</p>
</blockquote></td>
</tr>
</tbody>
</table>

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
<p>Contains manuals, PowerPoint presentations, and other information</p>
<p>about Clinical Reminders</p>
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
<p>This committee directs the</p>
<p>development of new and revised national reminders</p>
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
<p>Contains manuals for Clinical Reminders and</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes.

> The installation needs to be done by a person with DUZ(0) set to "@."

> We recommend that a Clinical Applications Coordinator be present during the install so that if questions occur during the install of Reminder Exchange entries, a knowledgeable person can respond to them.

#### Retrieve the host file from one of the following locations (with the ASCII file type):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Albany</p>
</blockquote></th>
<th><mark>REDACTED</mark></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

1.  <span id="_bookmark7" class="anchor"></span>Install the patch first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

#### Load the distribution.

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name. KID at the Host File prompt.

#### Example

> From the Installation menu, you may elect to use the following options:

#### Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

#### Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

#### Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*38 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE: DO NOT QUEUE THE INSTALLATION because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.

#### Installation Example

> [<u>See Appendix A</u>](#appendix-b-lung-cancer-health-factors)

#### Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in

> the multi-package build.

#### Build File Print

> Use the KIDS Build File Print option to print out the build components.

#### Post-installation routines

> After successful installation, the following init routines may be deleted:

> PXRMP38E PXRMP38I

## VA-Oncology Lung Cancer Reminder Dialog 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Component Inventory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VA-Oncology Lung Cancer Reminder Dialog contains:

- 1 dialog
- 14 branching terms
- 16 patient data objects
- 3 health factor categories
- 217 health factors

#### Reminder Dialog Name

> VA-ONCOLOGY LUNG CANCER

#### Branching Terms

> The following 14 branching reminder terms are exported with the VA-ONCOLOGY LUNG CANCER reminder. These terms already have mapped findings that are entered through the dialog. No additional mapping is required.

> VA-ONC LUNG CHEMO RT

> VA-ONC LUNG CLINICAL STAGE RT

> VA-ONC LUNG DATE OF DIAGNOSIS RT

> VA-ONC LUNG FIRST ABNORMAL RADIOLOGY RT VA-ONC LUNG FOLLOW UP RT

> VA-ONC LUNG HEADER BRANCH RT VA-ONC LUNG HISTOLOGY RT

> VA-ONC LUNG MEDIASTINOSCOPY RT

> VA-ONC LUNG MOLECULAR TESTING RT VA-ONC LUNG PERFORMANCE STATUS RT VA-ONC LUNG RADIATION THERAPY RT VA-ONC LUNG REFERRAL RT

> VA-ONC LUNG SURGERY PERFORMED RT VA-ONC LUNG TUMOR BOARD RT

#### Health Factors

> See [<u>Appendix B: Lung Cancer Health Factors</u>](#appendix-b-lung-cancer-health-factors) for complete list

#### Patient Data Objects

> Sixteen new health summary types/objects will install with this build. The health summary components are selected health factors (SHF). These objects pull ‘read only’ information from previously used health factors. No mapping is required.

> VA-ONC LUNG ABNORMAL RADIOLOGY VA-ONC LUNG CHEMOTHERAPY

> VA-ONC LUNG DIAGNOSIS DATE VA-ONC LUNG ECOG PS

> VA-ONC LUNG FOLLOW UP VA-ONC LUNG HEADER VA-ONC LUNG HEADER 2 VA-ONC LUNG HEADER 3 VA-ONC LUNG HISTOLOGY

> VA-ONC LUNG HOSPICE REFERRAL VA-ONC LUNG MEDIASTINOSCOPY VA-ONC LUNG MOLECULAR TESTS VA-ONC LUNG RADIATION THERAPY VA-ONC LUNG STAGING

> VA-ONC LUNG SURGERY PERFORMED VA-ONC LUNG TUMOR BOARD

# Post-Installation Set-up


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Introduction](#introduction)
  - [Pre-Installation](#pre-installation)
  - [Installation](#installation)
  - [VA-Oncology Lung Cancer Reminder Dialog](#va-oncology-lung-cancer-reminder-dialog)
    - [Component Inventory](#component-inventory)
- [Post-Installation Set-up](#post-installation-set-up)
  - [VA-Oncology Prostate Cancer Reminder Dialog](#va-oncology-prostate-cancer-reminder-dialog)
- [Post-Installation Set-up](#post-installation-set-up-1)
    - [Component Inventory](#component-inventory-1)
- [Post-Installation Set-up](#post-installation-set-up-2)
  - [Appendix A: Installation Example](#appendix-a-installation-example)
  - [Appendix B: Lung Cancer Health Factors](#appendix-b-lung-cancer-health-factors)
  - [Appendix C: Prostate Cancer Health Factors](#appendix-c-prostate-cancer-health-factors)
  - [Appendix D: VSAS Health Factors](#appendix-d-vsas-health-factors)
  - [Acronyms](#acronyms)
> There are several steps to complete after the patch is installed before the dialog should be deployed. Detailed instructions for each step are below.

#### Enable the dialog

> Before using the dialog in shared templates or linking to a note title you must first add into the TIU Template Reminder Dialog Parameter list.
> Adding dialog to the TIU Reminder Dialog Parameter (starting from the Reminder Manager Menu)
> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: CP CPRS Reminder Configuration
> CA Add/Edit Reminder Categories CL CPRS Lookup Categories
> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active PN Progress Note Headers
> RA Reminder GUI Resolution Active
> TIU TIU Template Reminder Dialog Parameter DL Default Outside Location
> PT Position Reminder Text at Cursor NP New Reminder Parameters
> GEC GEC Status Check Active WH WH Print Now Active
> Select CPRS Reminder Configuration \<TEST ACCOUNT\> Option: *TIU* TIU Template Reminder Dialog Parameter
> Reminder Dialogs allows as Templates may be set for the following:
> 1 User USR \[choose from NEW PERSON\]
> 3 Service SRV \[choose from SERVICE/SECTION\] 4 Division DIV \[NAME OF YOUR DIVISION\]
> 5 System SYS \[YOURSERVER.YOURSITE.MED.VA.GOV\]
> Enter selection: *5* System \[YOURSERVER.YOURSITE.MED.VA.GOV\] Setting Reminder Dialogs allows as Templates for System: YOURSERVER.YOURSITE.MED.VA.GOV
> Select Display Sequence: ? * enter ? to determine last sequence number*
> Display Sequence Value
> ---------------- ------------------- -----
1.  DAY COMBINED TOBACCO USER
2.  PATIENT EDUCATION ASSESSMENT
3.  IMMUNIZATION CLINIC DIALOG
4.  RD 580 NEU 562 DYSPHAGIA SCREENING TOOL
> ….
> 412 NON VA CARE COORDINATION NOTE (D) * last sequence number on my list yours will be different*

#### Remove disabled from Reminder Dialog

> Open reminder dialog manager, change view to ‘DIALOG’ locate VA-ONCOLOGY LUNG dialog on the list.
1.  Edit the VA-ONCOLOGY LUNG entry and remove the DISABLE field.
2.  Remember VA-ONCOLOGY LUNG will not have an associated source reminder.
> The National Oncology Program Office recommends that the VA-ONCOLOGY Lung Cancer reminder dialog be used as a template and not a standalone note, but this is a local decision.
> Collaborate with Hematology/Oncology staff to determine how dialog will be used. The National Oncology Program Office will be releasing additional reminder dialogs so it is important to establish an appropriate location. Please follow any local naming convention guidelines in place at your facility.
> =====================================================================

#### While using the TIU editors if at any time the setting do not look correct NEVER click the apply button, but instead click CANCEL, then start over

> =====================================================================

#### Creating a shared folder

> Open template editor
> Click + sign Shared Templates Click on New Template button
> Type Oncology (your site may have local naming convention guidelines that should be followed)
> Select folder in Template Type box Click Apply lower right corner
> EX: Creating Shared Folder
> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/002.png)

#### Creating a shared templates

> Open template editor Click + Shared templates
> Locate Oncology folder and click on it Click New Template button
> Type VA-ONCOLOGY (your site may have local naming convention that should be followed)
> Select Reminder Dialog in template Type box Type VA-ONCOLOGY in Reminder Dialog box Click Apply lower right corner
> EX: Creating Shared Template
> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/003.png)

#### Creating a local progress note title

> Creating Progress Note Title
> From the Document Definitions (Manager) Menu: create document definitions Type Next Level at prompt
> Enter corresponding number for Progress Notes at prompt Hit enter until you find Medicine
> Type Next Level and enter corresponding number for Medicine at prompt Type Title at prompt
> Type VA-Oncology Lung Template at prompt
> Map title to HEMATOLOGY AND ONCOLOGY NOTE
> Enter A at status prompt
> Select Action: Next Level// next Next Level
> Select CLINICAL DOCUMENTS Item (Line 2-7): 2
<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 32%" />
<col style="width: 28%" />
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th></th>
<th></th>
<th colspan="2">Type</th>
<th></th>
<th rowspan="5"></th>
</tr>
<tr class="odd">
<th>2</th>
<th><blockquote>
<p>PROGRESS NOTES</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th>CL</th>
</tr>
<tr class="header">
<th>3</th>
<th><blockquote>
<p>MEDICINE</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th>DC</th>
</tr>
<tr class="odd">
<th>4</th>
<th><blockquote>
<p>MEDICAL OBSERVATION</p>
</blockquote></th>
<th><blockquote>
<p>NOTE</p>
</blockquote></th>
<th colspan="2"></th>
<th>TL</th>
</tr>
<tr class="header">
<th>5</th>
<th><blockquote>
<p>CANCER CARE</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th>TL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>6</td>
<td colspan="2"><blockquote>
<p>CARDIAC CATH LAB PROCEDURE REPORT (T)</p>
</blockquote></td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="even">
<td>7</td>
<td colspan="2"><blockquote>
<p>CARDIAC ELECTROPHYSIOLOGY PROCEDURE REPORT</p>
</blockquote></td>
<td><blockquote>
<p>(T)</p>
</blockquote></td>
<td colspan="3">TL</td>
</tr>
<tr class="odd">
<td>8</td>
<td colspan="2"><blockquote>
<p>CARDIOLOGY ACS TEAM FOLLOW-UP NOTE</p>
</blockquote></td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="even">
<td>9</td>
<td colspan="2"><blockquote>
<p>CARDIOLOGY AICD IMPLANTATION REPORT</p>
</blockquote></td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="odd">
<td>+</td>
<td colspan="2"><blockquote>
<p><strong>?Help &gt;ScrollRight PS/PL PrintScrn/List</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>+/-</strong></p>
</blockquote></td>
<td colspan="3"><strong>&gt;&gt;&gt;</strong></td>
</tr>
</tbody>
</table>

#### Linking progress note to reminder dialog

> From Template Editor Edit Shared Template Click + Document Titles
> Click New Template button
> Type VA-Oncology Lung in Name box
> Click down arrow and Click on Reminder Dialog in Template Type Box Type VA-ONCOLOGY in Reminder Dialog box
> Type VA-Oncology Lung Template in Associated Title Box Click Apply in lower right corner

#### EX: Linking progress note to dialog

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/004.png)

## VA-Oncology Prostate Cancer Reminder Dialog 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark29" class="anchor"></span>Component Inventory

> The VA-Oncology Prostate Cancer Reminder Dialog contains:

- 1 dialog
- 1 branching terms
- 6 patient data objects
- 3 health factor categories
- 294 health factors

#### Reminder Dialog Name

> VA-ONCOLOGY PROSTATE CANCER

#### Branching Term

> The following branching reminder term is exported with the reminder. This term contains mapped findings that are entered through the dialog. No additional mapping is required.

> VA-ONCOLOGY PROSTATE HEADER RT

#### Health Factors

> See [<u>Appendix C: Prostate Cancer Health Factors</u>](#appendix-c-prostate-cancer-health-factors) for complete list

#### Patient Data Objects

> Six new health summary types/objects/TIU document definitions will install with this build. Two of these health summary types will require mapping to local terms.

> Instructions are included. No mapping is required for the other four objects.

> VA-ONC PCA POST TREATMENT VA-ONC PCA TREATMENTS

> VA-ONC PCA DIAGNOSIS

> VA-ONC PCA SURG PATH REPORT

> VA-ONC PCA TESTOSTERONE (mapping required)

> VA-ONC PCA LAST PSA (mapping required)

> NOTICE: The GMTSMGR security key is necessary for the staff responsible for mapping the health summary types.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Element/Group containing HSO</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>TIU Object Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HS Object Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HS Type Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>HS Component Type</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>VA-EL ONC PCA PROSTATE HSO</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA POST TREATMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA POST TREATMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA POST TREATMENT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>SHF (Selected Health Factor)</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-EL ONC PCA PROSTATE HSO</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA TREATMENTS</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA TREATMENTS</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA TREATMENTS</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>SHF (Selected Health Factor)</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-EL ONC PCA PROSTATE HSO</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA DIAGNOSIS</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA DIAGNOSIS</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA DIAGNOSIS</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>SHF (Selected Health Factor)</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-GP ONC PCA PATHO HSO</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA SURG PATH REPORT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA SURG PATH REPORT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA SURG PATH REPORT</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>SP (LAB SURGICAL PATHOLOGY)</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-EL ONC PCA TESTOSTERONE HSO</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA TESTOSTERONE</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA TESTOSTERONE</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA TESTOSTERONE</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>SLT (Selected Lab Test)</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-EL ONC PCA LAST PSA HSO</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA LAST PSA</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA LAST PSA</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>VA-ONC PCA LAST PSA</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>SLT (Selected Lab Test)</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

# Post-Installation Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are several steps to complete after the patch is installed before the dialog should be deployed. Detailed instructions for each step are below.

#### Configuring two new Health Summary types/TIU objects/health summary objects

> All of the TIU objects are already embedded in the dialog, but two of the six will not display information until the health summary type for each one is mapped to local lab tests. (Click here For detailed information regarding each HSO – see Excel spreadsheet in step 4.4). Before beginning, identify the following local information for each health summary type/object. Detailed instructions for editing the health summary types follow.

> HEALTH SUMMARY TYPE: VA-ONC PCA TESTOSTERONE

> a\. What are the local lab test name(s) for Testosterone?

> HEALTH SUMMARY TYPE: VA-ONC PCA LAST PSA

> a\. What are the local lab test name(s) for Prostate-Specific Antigen?

> From Health Summary Maintenance Menu

1.  Disable/Enable Health Summary Component
2.  Create/Modify Health Summary Components
3.  Edit Ad Hoc Health Summary Type
4.  Rebuild Ad Hoc Health Summary Type
5.  Resequence a Health Summary Type 6 Create/Modify Health Summary Type
7.  Edit Health Summary Site Parameters
8.  Health Summary Objects Menu ...
9.  CPRS Reports Tab 'Health Summary Types List' Menu ...
10. CPRS Health Summary Display/Edit Site Defaults ...

> Select Health Summary Maintenance Menu \<TEST ACCOUNT\> Option: 6 Create/Modify Health Summary Type

> Select Health Summary Type: VA-ONC PCA TESTOSTERONE VA-Onc PCA Testosterone has (No components)

> OK? YES//

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// y YES

> NAME: VA-ONC PCA TESTOSTERONE Replace

> TITLE: Testosterone Replace

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN

> LOCK:

> OWNER:

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES//NO

> Select COMPONENT: SLT LAB TESTS SELECTED SLT SUMMARY ORDER: 5// 5

> OCCURRENCE LIMIT: 10 TIME LIMIT:

> HEADER NAME: Lab Tests Selected//

> No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select up to 99 items.

> Select SELECTION ITEM: *Enter exact name of local TESTOSTERONE lab test. You can enter more than one at the next prompt if needed*.

> The Health Summary Type Structure should look similar to this:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th>Max</th>
<th>Hos</th>
<th><blockquote>
<p>ICD</p>
</blockquote></th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td><blockquote>
<p>Component Name</p>
</blockquote></td>
<td>Occ</td>
<td>Time Loc</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Nar</p>
</blockquote></td>
<td><blockquote>
<p>Mod Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> From Health Summary Maintenance Menu

1.  Disable/Enable Health Summary Component
2.  Create/Modify Health Summary Components
3.  Edit Ad Hoc Health Summary Type
4.  Rebuild Ad Hoc Health Summary Type
5.  Resequence a Health Summary Type
6.  Create/Modify Health Summary Type
7.  Edit Health Summary Site Parameters
8.  Health Summary Objects Menu ...
9.  CPRS Reports Tab 'Health Summary Types List' Menu ...
10. CPRS Health Summary Display/Edit Site Defaults ...

> Select Health Summary Maintenance Menu \<TEST ACCOUNT\> Option: 6 Create/Modify Health Summary Type

> Select Health Summary Type: VA-ONC PCA LAST PSA

> VA-ONC PCA LAST PSA has (No components) OK? YES//

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES NAME: VA-ONC PCA LAST PSA Replace TITLE: PSA//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN

> LOCK: OWNER:

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES//NO Select COMPONENT: SLT LAB TESTS SELECTED

> SUMMARY ORDER: 5// 5 OCCURRENCE LIMIT: 10 TIME LIMIT:

> HEADER NAME: Lab Tests Selected// No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select up to 99 items.

> Select SELECTION ITEM: *Enter exact name of local PROSTATE SPECIFIC ANTIGEN (PSA) lab test. You can enter more than one at the next prompt if needed.*

> The Health Summary Type Structure should look similar to this:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th>Max</th>
<th>Hos</th>
<th><blockquote>
<p>ICD</p>
</blockquote></th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td><blockquote>
<p>Component Name</p>
</blockquote></td>
<td>Occ</td>
<td>Time Loc</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Nar</p>
</blockquote></td>
<td><blockquote>
<p>Mod Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Enabling the dialog

> Before using the dialog in shared templates or linking to a note title you must first add into the TIU Template Reminder Dialog Parameter list. Adding dialog to the TIU Reminder Dialog Parameter (starting from the Reminder Manager Menu)

> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: CP CPRS Reminder Configuration

> CA Add/Edit Reminder Categories CL CPRS Lookup Categories

> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active

> PN Progress Note Headers

> RA Reminder GUI Resolution Active

> TIU TIU Template Reminder Dialog Parameter DL Default Outside Location

> PT Position Reminder Text at Cursor NP New Reminder Parameters

> GEC GEC Status Check Active WH WH Print Now Active

> Select CPRS Reminder Configuration \<TEST ACCOUNT\> Option: TIU TIU Template Reminder Dialog Parameter

> Reminder Dialogs allows as Templates may be set for the following:

> 1 User USR \[choose from NEW PERSON\]

> 3 Service SRV \[choose from SERVICE/SECTION\] 4 Division DIV \[NAME OF YOUR DIVISION\]

> 5 System SYS \[YOURSERVER.YOURSITE.MED.VA.GOV\]

> Enter selection: *5* System \[YOURSERVER.YOURSITE.MED.VA.GOV\]

> Setting Reminder Dialogs allows as Templates for System: YOURSERVER.YOURSITE.MED.VA.GOV

> Select Display Sequence: ? * enter ? to determine last number in sequence*

> Display Sequence Value

> ---------------- -----

1.  DAY COMBINED TOBACCO USER
2.  PATIENT EDUCATION ASSESSMENT
3.  IMMUNIZATION CLINIC DIALOG
4.  RD 580 NEU 562 DYSPHAGIA SCREENING TOOL
5.  DAY DISCHARGE INSTRUCTIONS DIALOG

> ….

> 412 NON VA CARE COORDINATION NOTE (D) * last sequence number on my*

> *list yours will be different*

> Select Display Sequence: *413*

> Are you adding 413 as a new Display Sequence? Yes// YES Display Sequence: 413// 413

> Clinical Reminder Dialog*: VA-ONCOLOGY PROSTATE* reminder dialog NATIONAL

> ...OK? Yes// (Yes)

#### Remove disable from reminder dialog

> Open reminder dialog manager, change view to ‘DIALOG’ locate VA-ONCOLOGY PROSTATE dialog on the list.

1.  Edit the VA-ONCOLOGY PROSTATE entry and remove the DISABLE field.
2.  Remember VA-ONCOLOGY PROSTATE will not have an associated source reminder.

> The National Oncology Program Office recommends that the VA Oncology Prostate Cancer reminder dialog be used as a template and not a standalone note, but this is a local decision. Collaborate with Hematology/Oncology staff to determine how dialog will be used. The National Oncology Program Office will be releasing additional reminder dialogs so it is important to establish an appropriate location. Please follow any local naming convention guidelines in place at your facility.

> ====================================================================================

> While using the TIU editors if at any time the setting do not look correct NEVER click the apply button, but instead click CANCEL, then start over

> =====================================================================================

#### Creating a shared folder

> Open template editor

> Click + sign Shared Templates Click on NEW TEMPLATE button

> Type ONCOLOGY (this is only a suggestion-your site may have local naming convention guidelines that should be followed)

> Select FOLDER in Template Type box

> Click APPLY lower right corner

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/005.png)Ex: Creating Shared Folder

#### Creating a shared template

> Open template editor Click + Shared templates

> Locate ONCOLOGY folder and click on it Click NEW TEMPLATE button

> Type ONCOLOGY PROSTATE –this is a suggestion the naming convention is a local decision

> Select REMINDER DIALOG in template Type box

> Type VA-ONCOLOGY PROSTATE in Reminder Dialog box Click APPLY lower right corner

> EX: Creating Shared Template

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/006.png)

#### Creating a local progress note title

> From the Document Definitions (Manager) Menu: create document definitions Type Next Level at prompt

> Enter corresponding number for Progress Notes at prompt Hit enter until you find Medicine

> Type Next Level and enter corresponding number for Medicine at prompt Type Title at prompt

> Type VA-Oncology Prostate Template at prompt Map title to VHA ENTERPRISE STANDARD TITLE: HEMATOLOGY AND ONCOLOGY NOTE

> Enter A at status prompt EX: Creating Note Title

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 56%" />
<col style="width: 29%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><span id="_bookmark41" class="anchor"></span>Name</th>
<th></th>
<th>Type</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p><strong>CLINICAL DOCUMENTS</strong></p>
</blockquote></td>
<td></td>
<td>CL</td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td><blockquote>
<p><strong>PROGRESS NOTES</strong></p>
</blockquote></td>
<td></td>
<td><strong>CL</strong></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>ADDENDUM</p>
</blockquote></td>
<td></td>
<td>DC</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>DISCHARGE SUMMARY</p>
</blockquote></td>
<td></td>
<td>CL</td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>CLINICAL PROCEDURES</p>
</blockquote></td>
<td></td>
<td>CL</td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>LR LABORATORY REPORTS</p>
</blockquote></td>
<td></td>
<td>CL</td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>SURGICAL REPORTS</p>
</blockquote></td>
<td></td>
<td>CL</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 32%" />
<col style="width: 28%" />
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th></th>
<th></th>
<th colspan="2">Type</th>
<th></th>
<th rowspan="5"></th>
</tr>
<tr class="odd">
<th>2</th>
<th><blockquote>
<p>PROGRESS NOTES</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th>CL</th>
</tr>
<tr class="header">
<th>3</th>
<th><blockquote>
<p>MEDICINE</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th>DC</th>
</tr>
<tr class="odd">
<th>4</th>
<th><blockquote>
<p>MEDICAL OBSERVATION</p>
</blockquote></th>
<th><blockquote>
<p>NOTE</p>
</blockquote></th>
<th colspan="2"></th>
<th>TL</th>
</tr>
<tr class="header">
<th>5</th>
<th><blockquote>
<p>CANCER CARE</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th>TL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>6</td>
<td colspan="2"><blockquote>
<p>CARDIAC CATH LAB PROCEDURE REPORT (T)</p>
</blockquote></td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="even">
<td>7</td>
<td colspan="2"><blockquote>
<p>CARDIAC ELECTROPHYSIOLOGY PROCEDURE REPORT</p>
</blockquote></td>
<td><blockquote>
<p>(T)</p>
</blockquote></td>
<td colspan="3">TL</td>
</tr>
<tr class="odd">
<td>8</td>
<td colspan="2"><blockquote>
<p>CARDIOLOGY ACS TEAM FOLLOW-UP NOTE</p>
</blockquote></td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="even">
<td>9</td>
<td colspan="2"><blockquote>
<p>CARDIOLOGY AICD IMPLANTATION REPORT</p>
</blockquote></td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="odd">
<td>+</td>
<td colspan="2"><blockquote>
<p><strong>?Help &gt;ScrollRight PS/PL PrintScrn/List</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>+/-</strong></p>
</blockquote></td>
<td colspan="3"><strong>&gt;&gt;&gt;</strong></td>
</tr>
</tbody>
</table>

#### Linking progress note to reminder dialog

> From Template Editor Edit Shared Template Click + Document Titles

> Click NEW TEMPLATE button

> Type ONCOLOGY PROSTATE in Name box

> Click down arrow and Click on REMINDER DIALOG in Template Type Box Type VA-ONCOLOGY in Reminder Dialog box

> Type ONCOLOGY PROSTATE Template in Associated Title Box Click APPLY in lower right corner

> EX: Linking Progress Note Title to Dialog

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/007.png)

#### Testing the patient data objects

> Open the VA-ONCOLOGY PROSTATE dialog and check-open the LABORATORY TESTS section.

![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/008.png)

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/009.png)Example 1-patient with no previous TESTOSTERONE/PSA lab test results

> Example 2-patient w/previous TESTSOTERONE/PSA lab test results

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/010.png)

> VA-Oncology Symptom Assessment Scale (VSAS) Reminder Dialog

### Component Inventory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VA-Oncology Symptom Assessment Scale Reminder Dialog contains:

- 1 dialog
- 13 health factor categories
- 143 health factors
- 1 GMRV Vital type
- 1 TIU template field

#### Reminder Dialog Name

> VA-ONCOLOGY SYMPTOM ASSESSMENT SCALE

#### Health Factors

> See [Appendix D: VSAS Health Factors](#appendix-d-vsas-health-factors) for complete list

1.  <span id="_bookmark46" class="anchor"></span>GMRV Vital Type

> The VSAS reminder dialog contains the GMRV vital type

> PAIN

#### TIU Template Field

> The VSAS reminder dialog contains one template field that is required if clicked open.

> VA-ONC WP 4 LINES (REQ)

# Post-Installation Set-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are several steps to complete after the patch is installed before the dialog should be deployed. Detailed instructions for each step are below.

#### Enabling the dialog

> Adding dialog to the TIU Reminder Dialog Parameter (starting from the Reminder Manager Menu)

> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: CP CPRS Reminder Configuration

> CA Add/Edit Reminder Categories CL CPRS Lookup Categories

> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active

> PN Progress Note Headers

> RA Reminder GUI Resolution Active

> TIU TIU Template Reminder Dialog Parameter DL Default Outside Location

> PT Position Reminder Text at Cursor NP New Reminder Parameters

> GEC GEC Status Check Active WH WH Print Now Active

> Select CPRS Reminder Configuration \<TEST ACCOUNT\> Option: TIU TIU Template Reminder Dialog Parameter

> Reminder Dialogs allows as Templates may be set for the following:

> 1 User USR \[choose from NEW PERSON\]

> 3 Service SRV \[choose from SERVICE/SECTION\] 4 Division DIV \[NAME OF YOUR DIVISION\]

> 5 System SYS \[YOURSERVER.YOURSITE.MED.VA.GOV\]

> Enter selection: 5 System \[YOURSERVER.YOURSITE.MED.VA.GOV\] Setting Reminder Dialogs allows as Templates for System: YOURSERVER.YOURSITE.MED.VA.GOV

> Select Display Sequence: ?  enter ? to determine last sequence number

#### Remove disabled from reminder dialog

> Open reminder dialog manager, change view to ‘DIALOG’ locate VA-ONCOLOGY SYMPTOM ASSESSMENT SCALE dialog on the list.

1.  Edit the VA-ONCOLOGY SYMPTOM ASSESSMENT SCALE entry and remove the DISABLE field.
2.  Remember VA-ONCOLOGY SYMPTOM ASSESSMENT SCALE will not have an associated source reminder.

> The National Oncology Program Office recommends that the VSAS reminder dialog be used as a template and not a standalone note, but this is a local decision. Collaborate with Hematology/Oncology staff to determine how dialog will be used. The National Oncology Program Office will be releasing additional reminder dialogs so it is important to establish an appropriate location. Please follow any local naming convention guidelines in place at your facility.

> ====================================================================

> While using the TIU editors if at any time the setting does not look correct,

> NEVER click the apply button, but instead click CANCEL, then start over

#### Creating a shared folder

> Open template editor

> Click + sign Shared Templates Click on New Template button

> Type Oncology – this is a suggestion - the folder name is a local decision Select folder in Template Type box

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/011.png)Click Apply lower right corner EX: Creating Shared Folder

#### Creating shared templates

> Open template editor Click + Shared templates

> Locate Oncology folder and click on it Click New Template button

> Type ONCOLOGY SYMPTOM ASSESSMENT SCALE – the template name is a local decision

> Select Reminder Dialog in template Type box

> Type VA-ONCOLOGY SYMPTOM ASSESSMENT SCALE in Reminder Dialog box Click Apply lower right corner

> EX: Creating Shared Template

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/012.png)

#### Creating a local progress note title

> From the Document Definitions (Manager) Menu: create document definitions

> Type Next Level at prompt

> Enter corresponding number for Progress Notes at prompt Hit enter until you find Medicine

> Type Next Level and enter corresponding number for Medicine at prompt Type Title at prompt

> Type Oncology Symptom Assessment Scale at prompt – this is a suggestion - your site may have a local naming convention that should be followed

> Map title to VHA STANDARD ENTERPRISE TITLE: HEMATOLOGY AND ONCOLOGY NOTE

> Enter A at status prompt

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 32%" />
<col style="width: 28%" />
<col style="width: 10%" />
<col style="width: 13%" />
<col style="width: 4%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th></th>
<th></th>
<th colspan="2">Type</th>
<th></th>
<th rowspan="5"></th>
</tr>
<tr class="odd">
<th>2</th>
<th><blockquote>
<p>PROGRESS NOTES</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th>CL</th>
</tr>
<tr class="header">
<th>3</th>
<th><blockquote>
<p>MEDICINE</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th>DC</th>
</tr>
<tr class="odd">
<th>4</th>
<th><blockquote>
<p>MEDICAL OBSERVATION</p>
</blockquote></th>
<th><blockquote>
<p>NOTE</p>
</blockquote></th>
<th colspan="2"></th>
<th>TL</th>
</tr>
<tr class="header">
<th>5</th>
<th><blockquote>
<p>CANCER CARE</p>
</blockquote></th>
<th></th>
<th colspan="2"></th>
<th>TL</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>6</td>
<td colspan="2"><blockquote>
<p>CARDIAC CATH LAB PROCEDURE REPORT (T)</p>
</blockquote></td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="even">
<td>7</td>
<td colspan="2"><blockquote>
<p>CARDIAC ELECTROPHYSIOLOGY PROCEDURE REPORT</p>
</blockquote></td>
<td><blockquote>
<p>(T)</p>
</blockquote></td>
<td colspan="3">TL</td>
</tr>
<tr class="odd">
<td>8</td>
<td colspan="2"><blockquote>
<p>CARDIOLOGY ACS TEAM FOLLOW-UP NOTE</p>
</blockquote></td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="even">
<td>9</td>
<td colspan="2"><blockquote>
<p>CARDIOLOGY AICD IMPLANTATION REPORT</p>
</blockquote></td>
<td></td>
<td colspan="3">TL</td>
</tr>
<tr class="odd">
<td>+</td>
<td colspan="2"><blockquote>
<p><strong>?Help &gt;ScrollRight PS/PL PrintScrn/List</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>+/-</strong></p>
</blockquote></td>
<td colspan="3"><strong>&gt;&gt;&gt;</strong></td>
</tr>
</tbody>
</table>

#### Linking progress note to reminder dialog

> From Template Editor Edit Shared Template Click + Document Titles

> Click New Template button

> Type Oncology Symptom Assessment Scale in Name box - or the specific template name you created Step 9

> Click down arrow and Click on Reminder Dialog in Template Type Box Type VA-Oncology Symptom Assessment Scale in Reminder Dialog box Type Oncology Symptom Assessment Scale in Associated Title Box Click Apply in lower right corner

#### EX: Linking Progress Note to Dialog

> ![](pxrm-2-38-lung-and-prostate-cancer-symptom-assessment-scale-install-guide/013.png)

## Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution Enter a Host File: \<*your directory*\> PXRM_2_0_38.KID

> KIDS Distribution saved on Nov 24, 2014@13:07:10 Comment: LUNG ONOCOLGY TEMPLATES

> This Distribution contains Transport Globals for the following Package(s): OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> PXRM\*2.0\*38

> Use INSTALL NAME: PXRM\*2.0\*38 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: INstall Package(s) Select INSTALL NAME: PXRM\*2.0\*38 12/19/14@07:03:51

> =\> LUNG ONOCOLGY TEMPLATES ;Created on Nov 24, 2014@13:07:10

> This Distribution was loaded on Dec 19, 2014@07:03:51 with header of LUNG ONOCOLGY TEMPLATES ;Created on Nov 24, 2014@13:07:10

> It consisted of the following Install(s):

> PXRM\*2.0\*38

> Checking Install for Package PXRM\*2.0\*38 Install Questions for PXRM\*2.0\*38 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

> Install Started for PXRM\*2.0\*38 : Dec 19, 2014@07:04:02

> Build Distribution Date: Nov 24, 2014

> Installing Routines:

> Dec 19, 2014@07:04:02

> Running Pre-Install Routine: PRE^PXRMP38I Installing Data Dictionaries:

> Dec 19, 2014@07:04:02

> Installing Data:

> Dec 19, 2014@07:04:05

> Running Post-Install Routine: POST^PXRMP38I

> There are 2 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry VA-ONCOLOGY LUNG TEMPLATE PXRM\*2.0\*38
2.  Installing Reminder Exchange entry VA-PATCH 38 POST COMPONENTS Updating Routine file...

> Updating KIDS files...

> PXRM\*2.0\*38 Installed.

> Dec 19, 2014@07:09:11

> Not a production UCI PXRM\*2.0\*38

> Install Completed

## Appendix B: Lung Cancer Health Factors 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### LUNG CANCER DIALOG

> CATEGORY: Oncology (ONC) Lung Cancer Follow-Up ONC Lung Referral-Other

> ONC Lung Referral-Service Not Available ONC Lung Referral-Not Appropriate ONC Lung Referral-Patient Declined ONC Lung Referral-Yes

> ONC Lung Follow Up-Progression ONC Lung Follow Up-No Recurrence ONC Lung Follow Up-Recurrence ONC Lung Follow Up-Stable Disease ONC Lung Follow Up-Partial Response

> ONC Lung Follow Up-Complete Response

> CATEGORY: Oncology (ONC) Lung Cancer Treatments ONC Lung Chemo Stopped-Other

> ONC Lung Chemo Stopped-Patient Request ONC Lung Chemo Stopped-Progression ONC Lung Chemo Stopped-Toxicity

> ONC Lung Chemo Stopped-Plan Completed ONC Lung Chemo Other Stop Date

> ONC Lung Chemo Other Start Date ONC Lung Bevacizumab Stop Date ONC Lung Bevacizumab Start Date ONC Lung Ceritinib Stop Date ONC Lung Ceritinib Start Date ONC Lung Crizotinib Stop Date ONC Lung Crizotinib Start Date ONC Lung Erlotinib Stop Date ONC Lung Erlotinib Start Date ONC Lung Irinotecan Stop Date ONC Lung Irinotecan Start Date ONC Lung Etoposide Stop Date ONC Lung Etoposide Start Date ONC Lung Vinorelbine Stop Date ONC Lung Vinorelbine Start Date ONC Lung Gemitabine Stop Date ONC Lung Gemitabine Start Date ONC Lung Pemetrexed Stop Date ONC Lung Pemetrexed Start Date ONC Lung Paclitaxel Stop Date ONC Lung Paclitaxel Start Date ONC Lung Docetaxel Stop Date

> ONC Lung Docetaxel Start Date ONC Lung Carboplatin Stop Date ONC Lung Carboplatin Start Date ONC Lung Cisplatin Stop Date ONC Lung Cisplatin Start Date

> ONC Lung Chemo Intent-Not Determined ONC Lung Chemo Intent-Palliative

> ONC Lung Chemo Intent-Concurrent ONC Lung Chemo Intent-Neoadjuvant ONC Lung Chemo Intent-Adjuvant ONC Lung Chemo Not Admin-Other

> ONC Lung Chemo Not Admin-Pt Declined

> ONC Lung Chemo Not Admin-Not Recommended ONC Lung RT Stopped-Other

> ONC Lung RT Stopped-Patient Request ONC Lung RT Stopped-Progression ONC Lung RT Stopped-Toxicity

> ONC Lung RT Stopped-Plan Completed ONC Lung Stereotactic Body RT-No ONC Lung Stereotactic Body RT-Yes ONC Lung Other RT Stop Date

> ONC Lung Other RT Start Date ONC Lung Bone RT Stop Date ONC Lung Bone RT Start Date ONC Lung Brain RT Stop Date ONC Lung Brain RT Start Date ONC Lung Chest RT Stop Date ONC Lung Chest RT Start Date

> ONC Lung RT Intent-Not Determined ONC Lung RT Intent-Palliative

> ONC Lung RT Type-Concurrent ONC Lung RT Type-Neoadjuvant ONC Lung RT Type-Adjuvant ONC Lung RT Not Admin-Other

> ONC Lung RT Not Admin-Pt Declined ONC Lung RT Not Admin-Contraindicated

> ONC Lung Surgery Outcome-Not Determined ONC Lung Surgery Outcome-Result Pending ONC Lung Surgery Outcome-Not Resectable ONC Lung Surgery Outcome-+ Margins ONC Lung Surgery Outcome-Clear Margins ONC Lung Surgery Type-Wedge Resection ONC Lung Surgery Type-Segmentectomy ONC Lung Surgery Type-Pneumonectomy ONC Lung Surgery Type-Lobectomy

> ONC Lung Surgery No-Other Reason

> ONC Lung Surgery No-Patient Declined ONC Lung Surgery-Not Recommended

> CATEGORY: Oncology (ONC) Lung Cancer Diagnoses ONC Lung Molecular Test-Other

> ONC Lung ALK Translocation-Rearranged ONC Lung ALK Translocation-Normal

> ONC Lung ALK Translocation-Result Pendin ONC Lung ALK Translocation-Not Done ONC Lung EGFR Test-Mutant

> ONC Lung EGFR Test-Wild Type ONC Lung EGFR Test-Results Pending ONC Lung EGFR Test-Not Done

> ONC Lung Histology-Other ONC Lung Histology-SCLC

> ONC Lung Histology-NSCLC, NOS ONC Lung Histology-Large Cell ONC Lung Histology-Squamous Cell

> ONC Lung Histology-Adenocarcinoma ONC Lung Pathological-TNM Unknown ONC Lung Pathological-Any T, Any N, M1 ONC Lung Pathological-T4, N3, M0

> ONC Lung Pathological-T3, N3, M0 ONC Lung Pathological-T2, N3, M0 ONC Lung Pathological-T1, N3, M0 ONC Lung Pathological-T4, N2, M0 ONC Lung Pathological-T4, N1, M0 ONC Lung Pathological-T4, N0, M0 ONC Lung Pathological-T3, N2, M0 ONC Lung Pathological-T3, N1, M0 ONC Lung Pathological-T2, N2, M0 ONC Lung Pathological-T1, N2, M0 ONC Lung Pathological-T3, N0, M0 ONC Lung Pathological-T2, N1, M0 ONC Lung Pathological-T1, N1, M0 ONC Lung Pathological-T2, N0, M0 ONC Lung Pathological-T1, N0, M0 ONC Lung Pathological-TIS, N0, M0

> ONC Lung Pathological-Summary Stage Unk ONC Lung Pathological-Summary Stage Ext ONC Lung Pathological-Summary Stage Lim ONC Lung Pathological-Summary Stage I ONC Lung Pathological-Summary Stage IV ONC Lung Pathological-Summary Stage IIIB ONC Lung Pathological-Summary Stage IIIA ONC Lung Pathological-Summary Stage III

> ONC Lung Pathological-Summary Stage IIB ONC Lung Pathological-Summary Stage IIA ONC Lung Pathological-Summary Stage II ONC Lung Pathological-Summary Stage IB ONC Lung Pathological-Summary Stage IA ONC Lung Pathological-Summary Stage 0 ONC Lung Clinical-TNM Unknown

> ONC Lung Clinical Stage-Any T, Any N, M1 ONC Lung Clinical-T4, N3, M0

> ONC Lung Clinical-T3, N3, M0 ONC Lung Clinical-T2, N3, M0 ONC Lung Clinical-T1, N3, M0 ONC Lung Clinical-T4, N2, M0 ONC Lung Clinical-T4, N1, M0 ONC Lung Clinical-T4, N0, M0 ONC Lung Clinical-T3, N2, M0 ONC Lung Clinical-T3, N1, M0 ONC Lung Clinical-T2, N2, M0 ONC Lung Clinical-T1, N2, M0 ONC Lung Clinical-T3, N0, M0 ONC Lung Clinical-T2, N1, M0 ONC Lung Clinical-T1, N1, M0 ONC Lung Clinical-T2, N0, M0 ONC Lung Clinical-T1, N0, M0 ONC Lung Clinical-TIS, N0, M0

> ONC Lung Clinical-Summary Stage Unknown ONC Lung Clinical-Summary Stage Extens ONC Lung Clinical-Summary Stage Limited ONC Lung Clinical-Summary Stage IV

> ONC Lung Clinical-Summary Stage IIIB ONC Lung Clinical-Summary Stage IIIA ONC Lung Clinical-Summary Stage III ONC Lung Clinical-Summary Stage IIB ONC Lung Clinical-Summary Stage IIA ONC Lung Clinical-Summary Stage II ONC Lung Clinical-Summary Stage IB ONC Lung Clinical-Summary Stage IA ONC Lung Clinical-Summary Stage I ONC Lung Clinical-Summary Stage 0 ONC Lung Initial Diagnosis Date-

> ONC Lung First Abnormal Radiology Date- ONC Lung ECOG-0

> ONC Lung ECOG-1 ONC Lung ECOG-2 ONC Lung ECOG-3 ONC Lung ECOG-4

> ONC Lung ECOG-5

> ONC Lung ECOG-Unknown

> ONC Lung Presented To Tumor Board-Yes ONC Lung Presented To Tumor Board-No ONC Lung Presented To Tumor Board-N/A ONC Lung LN Sampling-Ultrasound

> ONC Lung LN Sampling-Mediastinoscopy ONC Lung LN Sampling-Surgery

> ONC Lung LN Sampling Done-No ONC Lung Chemo Intent Discussed-Yes ONC Lung Chemo Intent Discussed-No ONC Lung Doublet No-Contraindicated ONC Lung Doublet No-Declined

> ONC Lung Doublet No-N/A ONC Lung Doublet No-Other

> ONC Lung Bevacizumab Not Admin-Contra ONC Lung Bevacizumab Not Admin-Declined ONC Lung Bevacizumab Not Admin-N/A ONC Lung Bevacizumab Not Admin-Other ONC Lung RT Intent-Curative

> ONC Lung RT Intent Discussed-Yes ONC Lung RT Intent Discussed-No ONC Lung RT Stopped-Site Change ONC Lung RT Site-Other

> ONC Lung RT Site-Bone ONC Lung RT Site-Brain ONC Lung RT Site-Chest ONC Lung Chemo Type-Other

> ONC Lung Chemo Type-Bevacizumab ONC Lung Chemo Type-Ceritinib ONC Lung Chemo Type-Crizotinib ONC Lung Chemo Type-Erlotinib ONC Lung Chemo Type-Irinotecan ONC Lung Chemo Type-Etoposide ONC Lung Chemo Type-Vinorelbine ONC Lung Chemo Type-Gemcitabine ONC Lung Chemo Type-Pemetrexed ONC Lung Chemo Type-Paclitaxel ONC Lung Chemo Type-Docetaxel ONC Lung Chemo Type-Carboplatin ONC Lung Chemo Type-Cisplatin ONC Lung PCU Referral-No

## Appendix C: Prostate Cancer Health Factors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PROSTATE CANCER DIALOG

> CATEGORY: Prostate Cancer (ONC PCA) Treatments ONC PCA Clinical Trial Stop Date-

> ONC PCA Clinical Trial Start Date-

> CATEGORY: Prostate Cancer (ONC PCA) Follow-Up ONC PCA Hospice Referral:

> ONC PCA Hospice Referral-Not Available ONC PCA Hospice Referral No-Not Eligible ONC PCA Hospice Referral-Pt Declined ONC PCA Hospice/Palliative Referral-No ONC PCA Hospice/Palliative Referral-Yes ONC PCA Follow Up-Recurrence of Disease ONC PCA Follow Up-No Recurrence

> ONC PCA Follow Up-Progression of Disease ONC PCA Follow Up-Stable Disease

> ONC PCA Follow Up-Partial Response ONC PCA Follow Up-Complete Response ONC PCA Cryotherapy Stop Date-

> ONC PCA Cryotherapy Start Date- ONC PCA Cryotherapy Not Admin- ONC PCA Cryotherapy-Pt Declined

> ONC PCA Cryotherapy-Not Recommended ONC PCA Radiopharm-Pt Declined

> ONC PCA Radiopharm Not Admin-

> ONC PCA Radiopharm-Not Recommended ONC PCA Radium 223 Stop Date-

> ONC PCA Radium 223 Start Date-

> ONC PCA Radiopharmaceuticals Start Date- ONC PCA Radiopharm Other

> ONC PCA Immunotherapy-Not Recommended ONC PCA Immunotherapy Not Admin-

> ONC PCA Immunotherapy-Pt Declined ONC PCA Immunotherapy Other Stop Date- ONC PCA Immunotherapy Other Start Date- ONC PCA Immunotherapy-

> ONC PCA Sipuleucel-T Stop Date- ONC PCA Sipuleucel-T Start Date- ONC PCA Biphosphonate Not Admin- ONC PCA Biphosphonate-Pt Declined

> ONC PCA Biphosphonate-Not Recommended ONC PCA Denosumab Stop Date-

> ONC PCA Denosumab Start Date-

> ONC PCA Biphosphonate Other Stop Date- ONC PCA Biphosphonate Other Start Date-

> ONC PCA Biphosphonate Other- ONC PCA Pamidronate Stop Date- ONC PCA Pamidronate Start Date- ONC PCA Zoledronic Acid Stop Date- ONC PCA Zoledronic Acid Start Date- ONC PCA Steroids Not Administered- ONC PCA Steroids-Pt Declined

> ONC PCA Steroids-Not Recommended ONC PCA Steroids Other Stop Date- ONC PCA Steroids Other Start Date- ONC PCA Steroids Other-

> ONC PCA Dexamethasone Stop Date- ONC PCA Dexamethasone Start Date- ONC PCA Prednisone Stop Date- ONC PCA Prednisone Start Date- ONC PCA Chemo Not Administered- ONC PCA Chemo No-Pt Declined ONC PCA Chemo-Not Recommended ONC PCA Chemo-No

> ONC PCA Docetaxel Stop Date- ONC PCA Docetaxel Start Date- ONC PCA Chemo Other Stop Date- ONC PCA Chemo Other Start Date- ONC PCA Chemo Type-

> ONC PCA Estramustine Start Date- ONC PCA Estramustine Stop Date- ONC PCA Mitoxantrone Stop Date- ONC PCA Mitoxantrone Start Date- ONC PCA Cabazitaxel Stop Date- ONC PCA Cabazitaxel Start Date-

> ONC PCA Hormone Therapy-Pt Declined ONC PCA Hormone Therapy No-Other

> ONC PCA Hormone Therapy-Not Recommended ONC PCA Other Therapy Stop Date-

> ONC PCA Other Therapy Start Date- ONC PCA Hormone Therapy Other Type- ONC PCA Bilateral Orchiectomy

> ONC PCA Estrogen Stop Date- ONC PCA Estrogen Start Date- ONC PCA GnRH Other Stop Date- ONC PCA GnRH Other Start Date- ONC PCA GnRH-Other

> ONC PCA Leuprolide Stop Date- ONC PCA Leuprolide Start Date- ONC PCA Triptorelin Stop Date- ONC PCA Triptorelin Start Date-

> ONC PCA Buserlin Stop Date- ONC PCA Buserlin Start Date- ONC PCA Goserelin Stop Date- ONC PCA Goserelin Start Date-

> ONC PCA Androgen Synthesis Stop Date- ONC PCA Androgen Synthesis Start Date- ONC PCA Androgen Synthesis-Other ONC PCA Ketoconazole Stop Date-

> ONC PCA Ketoconazole Start Date- ONC PCA Abiraterone Stop Date- ONC PCA Abiraterone Start Date- ONC PCA Flutamide Stop Date- ONC PCA Flutamide Start Date- ONC PCA Enzalutamide Stop Date- ONC PCA Enzalutamide Start Date- ONC PCA Bicalutamide Stop Date- ONC PCA Bicalutamide Start Date-

> ONC PCA Anti-Androgen Other Stop Date- ONC PCA Anti-Androgen Other Start Date- ONC PCA Anti Androgen-Other

> ONC PCA Megestrol Stop Date- ONC PCA Megestrol Start Date- ONC PCA Nilutamide Stop Date- ONC PCA Nilutamide Start Date-

> ONC PCA Surgery-Tumor Not Resectable ONC PCA Surgery No-Other

> ONC PCA Surgery-Declined

> ONC PCA Surgery-Not Recommended ONC PCA Surgery Type-Other

> ONC PCA Nerve Sparing-Unknown ONC PCA Surgery-Not Nerve Sparing ONC PCA Surgery-Nerve Sparing ONC PCA Surgery-Prostatectomy ONC PCA Surgery-TURP

> ONC PCA Surgery-Pelvic Lymphadenectomy ONC PCA Surgery Lymph Node-No

> ONC PCA Surgery Lymph Node-Yes ONC PCA RT Not Administered- ONC PCA RT-Patient Declined

> ONC PCA RT-Not Recommended ONC PCA RT-No

> ONC PCA RT Other Stop Date- ONC PCA RT Other Start Date- ONC PCA RT Type Other- ONC PCA RT Other

> ONC PCA RT Type-Brachytherapy

> ONC PCA External Beam Other Stop Date- ONC PCA External Beam Other Start Date- ONC PCA RT External Beam Other-

> ONC PCA Conformal Proton RT Stop Date- ONC PCA Conformal Proton RT Start Date- ONC PCA Modulated RT Stop Date-

> ONC PCA Modulated RT Start Date-

> ONC PCA 3D Conformal Therapy Stop Date- ONC PCA 3D Conformal Therapy Start Date- ONC PCA Watchful Waiting-No

> ONC PCA Watchful Waiting-Yes ONC PCA Active Surveillance-No ONC PCA Surveillance-

> ONC PCA Surveillance-Needle Biopsy ONC PCA Surveillance-Ultrasounds ONC PCA Surveillance-PSA Tests ONC PCA Surveillance-Rectal Exams ONC PCA Surveillance-Regular Visits

> ONC PCA Treatment Intent Discussed-No ONC PCA Treatment Intent Discussed-Yes ONC PCA Treatment-Palliative

> ONC PCA Treatment-Curative

> ONC PCA Tumor Board-Case Not Presented ONC PCA Tumor Board-Not Available ONC PCA Tumor Board-Case Presented ONC PCA Radiopharmaceuticals Stop Date-

> CATEGORY: Prostate Cancer (ONC PCA) Diagnoses ONC PCA Risk Status-High

> ONC PCA Risk Status-Intermediate ONC PCA Risk Status-Low

> ONC PCA Gleason Score Combined-10 ONC PCA Gleason Score Combined-9 ONC PCA Gleason Score Combined-8 ONC PCA Gleason Score Combined-7 ONC PCA Gleason Score Combined-6 ONC PCA Gleason Score Combined-5 ONC PCA Gleason Score Combined-4 ONC PCA Gleason Score Combined-3 ONC PCA Gleason Score Combined-2 ONC PCA Gleason Score Two-5

> ONC PCA Gleason Score Two-4 ONC PCA Gleason Score Two-3 ONC PCA Gleason Score Two-2 ONC PCA Gleason Score Two-1 ONC PCA Gleason Score One-5

> ONC PCA Gleason Score One-4 ONC PCA Gleason Score One-3 ONC PCA Gleason Score One-2 ONC PCA Gleason Score One-1 ONC PCA Histology-Other:

> ONC PCA Histology-Small Cell

> ONC PCA Histology-Adenocarcinoma ONC PCA Pathological-Summary Stage IV ONC PCA Pathological-Summary Stage III ONC PCA Pathological-Summary Stage IIB ONC PCA Pathological-Summary Stage IIA ONC PCA Pathological-Summary Stage II ONC PCA Pathological-Summary Stage I ONC PCA Pathological-Any T,Any N,M1

> ONC PCA Pathological Stage-Any T,N1,M0 ONC PCA Pathological Stage-T4,N0,M0 ONC PCA Pathological Stage-T3b,N0,M0 ONC PCA Pathological Stage-T3a,N0,M0 ONC PCA Pathological Stage-T3,N0,M0 ONC PCA Pathological Stage-T2c,N0,M0 ONC PCA Pathological Stage-T2b,N0,M0 ONC PCA Pathological Stage-T2a,N0,M0 ONC PCA Pathological Stage-T2,N0,M0 ONC PCA Pathological Stage-T1c,N0,M0 ONC PCA Pathological Stage-T1B,N0,M0 ONC PCA Pathological Stage-T1A,N0,M0 ONC PCA Pathological Stage-T1 N0 MO ONC PCA Clinical-Summary Stage IV ONC PCA Clinical-Summary Stage III

> ONC PCA Clinical-Summary Stage IIB ONC PCA Clinical-Summary Stage IIA ONC PCA Clinical-Summary Stage II ONC PCA Clinical-Summary Stage I

> ONC PCA Clinical Stage-Any T,Any N,M1 ONC PCA Clinical Stage-Any T,N1,M0 ONC PCA Clinical Stage-T4,N0,M0

> ONC PCA Clinical Stage-T3b,N0,M0 ONC PCA Clinical Stage-T3a,N0,M0 ONC PCA Clinical Stage-T3,N0,M0 ONC PCA Clinical Stage-T2c,N0,M0 ONC PCA Clinical Stage-T2b,N0,M0 ONC PCA Clinical Stage-T2a,N0,M0 ONC PCA Clinical Stage-T2,N0,M0 ONC PCA Clinical Stage-T1c,N0,M0 ONC PCA Clinical Stage-T1b,N0,M0 ONC PCA Clinical Stage-T1a,N0,M0

> ONC PCA Clinical Stage-T1,N0,M0 ONC PCA Diagnosis Date-

> ONC PCA \>12 Positive-Transperineal ONC PCA \>12 Positive-Transrectal ONC PCA \>12 Core-Transrectal ONC PCA \>12 Core-Transperineal ONC PCA Biopsy-Transrectal

> ONC PCA Biopsy-Transperineal ONC PCA Lab Test-Other:

> ONC PCA ECOG-1 ONC PCA ECOG-0 ONC PCA ECOG-2 ONC PCA ECOG-3 ONC PCA ECOG-4 ONC PCA ECOG-5

> ONC PCA Surgery Outcome-Neg Margins ONC PCA Surgery Outcome-+Margins ONC PCA Surgery Outcome-Other

> ONC PCA Surgery Outcome-Results Pending ONC PCA 1 Core-Transperineal

> ONC PCA 2 Core-Transperineal ONC PCA 3 Core-Transperineal ONC PCA 4 Core-Transperineal ONC PCA 5 Core-Transperineal ONC PCA 6 Core-Transperineal ONC PCA 7 Core-Transperineal ONC PCA 8 Core-Transperineal ONC PCA 9 Core-Transperineal ONC PCA 10 Core-Transperineal ONC PCA 11 Core-Transperineal ONC PCA 12 Core-Transperineal

> ONC PCA 1 Pos Sample-Transperineal ONC PCA 2 Pos Sample-Transperineal ONC PCA 3 Pos Sample-Transperineal ONC PCA 4 Pos Sample-Transperineal ONC PCA 5 Pos Sample-Transperineal ONC PCA 6 Pos Sample-Transperineal ONC PCA 7 Pos Sample-Transperineal ONC PCA 8 Pos Sample-Transperineal ONC PCA 9 Pos Sample-Transperineal ONC PCA 10 Pos Sample-Transperineal ONC PCA 11 Pos Sample-Transperineal ONC PCA 12 Pos Sample-Transperineal ONC PCA Additional PSA

> ONC PCA 1 Core-Transrectal ONC PCA 2 Core-Transrectal

> ONC PCA 3 Core-Transrectal ONC PCA 4 Core-Transrectal

> ONC PCA 5 Pos Sample-Transrectal ONC PCA 6 Core-Transrectal

> ONC PCA 7 Core-Transrectal ONC PCA 8 Core-Transrectal ONC PCA 9 Core-Transrectal ONC PCA 10 Core-Transrectal ONC PCA 11 Core-Transrectal ONC PCA 12 Core-Transrectal

> ONC PCA 1 Pos Sample-Transrectal ONC PCA 2 Pos Sample-Transrectal ONC PCA 3 Pos Sample-Transrectal ONC PCA 4 Pos Sample-Transrectal ONC PCA 5 Core-Transrectal

> ONC PCA 6 Pos Sample-Transrectal ONC PCA 7 Pos Sample-Transrectal ONC PCA 8 Pos Sample-Transrectal ONC PCA 9 Pos Sample-Transrectal ONC PCA 10 Pos Sample-Transrectal ONC PCA 11 Pos Sample-Transrectal ONC PCA 12 Pos Sample-Transrectal ONC PCA External Beam Start Date- ONC PCA External Beam Stop Date- ONC PCA Additional Testosterone

## Appendix D: VSAS Health Factors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VSAS REMINDER DIALOG CATEGORY: ONC VSAS VOMITING CAT ONC VSAS VOMITING 10

> ONC VSAS VOMITING 9 ONC VSAS VOMITING 8 ONC VSAS VOMITING 7 ONC VSAS VOMITING 6 ONC VSAS VOMITING 5 ONC VSAS VOMITING 4 ONC VSAS VOMITING 3 ONC VSAS VOMITING 2 ONC VSAS VOMITING 1 ONC VSAS VOMITING 0

> CATEGORY: ONC VSAS SOB EXERTION CAT ONC VSAS SOB EXERTION 10

> ONC VSAS SOB EXERTION 9 ONC VSAS SOB EXERTION 8 ONC VSAS SOB EXERTION 7

> ONC VSAS SOB EXERTION 6 ONC VSAS SOB EXERTION 5 ONC VSAS SOB EXERTION 4 ONC VSAS SOB EXERTION 3 ONC VSAS SOB EXERTION 2 ONC VSAS SOB EXERTION 1 ONC VSAS SOB EXERTION 0

> CATEGORY: ONC VSAS OTHER CAT ONC VSAS OTHER 10

> ONC VSAS OTHER 9 ONC VSAS OTHER 8 ONC VSAS OTHER 7 ONC VSAS OTHER 6 ONC VSAS OTHER 5 ONC VSAS OTHER 4 ONC VSAS OTHER 3 ONC VSAS OTHER 2 ONC VSAS OTHER 1 ONC VSAS OTHER 0 ONC VSAS OTHER MAIN

> CATEGORY: ONC VSAS DISTRESS CAT ONC VSAS DISTRESS 10

> ONC VSAS DISTRESS 9 ONC VSAS DISTRESS 8 ONC VSAS DISTRESS 7 ONC VSAS DISTRESS 6 ONC VSAS DISTRESS 5 ONC VSAS DISTRESS 4 ONC VSAS DISTRESS 3 ONC VSAS DISTRESS 2 ONC VSAS DISTRESS 1 ONC VSAS DISTRESS 0

> CATEGORY: ONC VSAS ANXIETY CAT ONC VSAS ANXIETY 10

> ONC VSAS ANXIETY 9 ONC VSAS ANXIETY 8 ONC VSAS ANXIETY 7 ONC VSAS ANXIETY 6 ONC VSAS ANXIETY 5 ONC VSAS ANXIETY 4 ONC VSAS ANXIETY 3 ONC VSAS ANXIETY 2 ONC VSAS ANXIETY 1

> ONC VSAS ANXIETY 0

> CATEGORY: ONC VSAS DEPRESSION CAT ONC VSAS DEPRESSION 10

> ONC VSAS DEPRESSION 9 ONC VSAS DEPRESSION 8 ONC VSAS DEPRESSION 7 ONC VSAS DEPRESSION 6 ONC VSAS DEPRESSION 5 ONC VSAS DEPRESSION 4 ONC VSAS DEPRESSION 3 ONC VSAS DEPRESSION 2 ONC VSAS DEPRESSION 1 ONC VSAS DEPRESSION 0

> CATEGORY: ONC VSAS DROWSINESS CAT ONC VSAS DROWSINESS 10

> ONC VSAS DROWSINESS 9 ONC VSAS DROWSINESS 8 ONC VSAS DROWSINESS 7 ONC VSAS DROWSINESS 6 ONC VSAS DROWSINESS 5 ONC VSAS DROWSINESS 4 ONC VSAS DROWSINESS 3 ONC VSAS DROWSINESS 2 ONC VSAS DROWSINESS 1 ONC VSAS DROWSINESS 0

> CATEGORY: ONC VSAS SOB REST CAT ONC VSAS SOB REST 10

> ONC VSAS SOB REST 9 ONC VSAS SOB REST 8 ONC VSAS SOB REST 7 ONC VSAS SOB REST 6 ONC VSAS SOB REST 5 ONC VSAS SOB REST 4 ONC VSAS SOB REST 3 ONC VSAS SOB REST 2 ONC VSAS SOB REST 1 ONC VSAS SOB REST 0

> CATEGORY: ONC VSAS CONSTIPATION CAT ONC VSAS CONSTIPATION 10

> ONC VSAS CONSTIPATION 9 ONC VSAS CONSTIPATION 8 ONC VSAS CONSTIPATION 7

> ONC VSAS CONSTIPATION 6 ONC VSAS CONSTIPATION 5 ONC VSAS CONSTIPATION 4 ONC VSAS CONSTIPATION 3 ONC VSAS CONSTIPATION 2 ONC VSAS CONSTIPATION 1 ONC VSAS CONSTIPATION 0

> CATEGORY: ONC VSAS DIARRHEA CAT ONC VSAS DIARRHEA 10

> ONC VSAS DIARRHEA 9 ONC VSAS DIARRHEA 8 ONC VSAS DIARRHEA 7 ONC VSAS DIARRHEA 6 ONC VSAS DIARRHEA 5 ONC VSAS DIARRHEA 4 ONC VSAS DIARRHEA 3 ONC VSAS DIARRHEA 2 ONC VSAS DIARRHEA 1 ONC VSAS DIARRHEA 0

> CATEGORY: ONC VSAS NAUSEA CAT ONC VSAS NAUSEA 10

> ONC VSAS NAUSEA 9 ONC VSAS NAUSEA 8 ONC VSAS NAUSEA 7 ONC VSAS NAUSEA 6 ONC VSAS NAUSEA 5 ONC VSAS NAUSEA 4 ONC VSAS NAUSEA 3 ONC VSAS NAUSEA 2 ONC VSAS NAUSEA 1 ONC VSAS NAUSEA 0

> CATEGORY: ONC VSAS ANOREXIA CAT ONC VSAS ANOREXIA 10

> ONC VSAS ANOREXIA 9 ONC VSAS ANOREXIA 8 ONC VSAS ANOREXIA 7 ONC VSAS ANOREXIA 6 ONC VSAS ANOREXIA 5 ONC VSAS ANOREXIA 4 ONC VSAS ANOREXIA 3 ONC VSAS ANOREXIA 2 ONC VSAS ANOREXIA 1 ONC VSAS ANOREXIA 0

> CATEGORY: ONC VSAS TIREDNESS CAT ONC VSAS TIREDNESS 10

> ONC VSAS TIREDNESS 9 ONC VSAS TIREDNESS 8 ONC VSAS TIREDNESS 7 ONC VSAS TIREDNESS 6 ONC VSAS TIREDNESS 5 ONC VSAS TIREDNESS 4 ONC VSAS TIREDNESS 3 ONC VSAS TIREDNESS 2 ONC VSAS TIREDNESS 1 ONC VSAS TIREDNESS 0

## Acronyms 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
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
<p><strong>Branching Terms</strong></p>
</blockquote></td>
<td><blockquote>
<p>A reminder term used to determine Boolean logic for branching/changing content within a reminder dialog window when it opens specific to the patient’s chart information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Dialog</strong></p>
</blockquote></td>
<td><blockquote>
<p>A window in CPRS that opens in the format of a form to aid the user in creating text in a note and entering information into the record with a point and click interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>CPRS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>HIS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Health Informatics Specialist, another title for Clinical Applications Coordinator (CAC) with same responsibilities as a CAC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Health Factor</strong></p>
</blockquote></td>
<td><blockquote>
<p>Informational data marker entered into the record to document patient information that is not readily identifiable with other information data entries in the system</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Health Summary (HS)</strong></p>
</blockquote></td>
<td><blockquote>
<p>A clinical package in VistA; GMTS is the package’s name spacing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Health Summary Types/Objects</strong></p>
</blockquote></td>
<td><blockquote>
<p>A collection of data that displays to the user specific to the patient’s chart they are viewing. Commonly called patient data objects or TIU</p>
<p>objects</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Health Summary Type</strong></p>
</blockquote></td>
<td><blockquote>
<p>A health summary type is a structure similar to a template, composed of health summary components</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Health Summary Object</strong></p>
</blockquote></td>
<td><blockquote>
<p>Health Summary Types saved in a temporary array for insertion into another electronic document</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Health Summary Component</strong></p>
</blockquote></td>
<td><blockquote>
<p>Elements of data from VISTA packages that make up the health summary report (e.g., demographics, lab tests, progress notes)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ONC</strong></p>
</blockquote></td>
<td><blockquote>
<p>National Oncology Program Office</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>KIDS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Kernel Installation Distribution System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Patient Data Object</strong></p>
</blockquote></td>
<td><blockquote>
<p>A collection of data that displays to the user specific to the patient’s chart they are viewing. Commonly called health summary objects or TIU objects</p>
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
<p><strong>PCA</strong></p>
</blockquote></th>
<th><blockquote>
<p>Prostate Cancer</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>PCS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PMAS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Program Management Accountability System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>PTM</strong></p>
</blockquote></td>
<td><blockquote>
<p>Patch Tracker Message</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PXRM</strong></p>
</blockquote></td>
<td><blockquote>
<p>Clinical Reminder Package namespace</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>RSD</strong></p>
</blockquote></td>
<td><blockquote>
<p>Requirements Specification Document</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Shared Template</strong></p>
</blockquote></td>
<td><blockquote>
<p>Templates within the shared templates tree of CPRS, which the users can access and use while documenting in the chart</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Template</strong></p>
</blockquote></td>
<td><blockquote>
<p>Commonly referred to as a dialog. See <strong>dialog</strong> for definition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>TIU</strong></p>
</blockquote></td>
<td><blockquote>
<p>Text Integrated Utility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA</strong></p>
</blockquote></td>
<td><blockquote>
<p>Department of Veteran Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VHA</strong></p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VistA</strong></p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information System and Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VSAS</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA SYMPTOM ASSESSMENT SCALE</p>
</blockquote></td>
</tr>
</tbody>
</table>
