---
title: PXRM*1.5*8 IHD-QUERI Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: IHD-QUERI
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 1.5
patch_id: PXRM*1.5*8
group_key: "PXRM:PXRM:1.5"
file_numbers: 
  - 801
  - 811
security_keys: []
menu_options: 3
description: > The Quality Enhancement Research Initiative (QUERI) is a program within the VA Health Services Research and Development Service (HSR&D). QUERI’s mission is to translate research innovations into improved quality of health care for veterans. The goal of the VA IHD• QUERI (Ischemic Heart Disease) gr
audience: 
keywords: 
  - blockquote
  - strong
  - reminder
  - lipid
  - dialog
  - class
  - table
  - colgroup
  - thead
  - tbody
page_count: 0
word_count: 19697
section_count: 6
table_count: 1
figure_count: 0
appendix_count: 7
has_toc: False
is_stub: False
pub_date: May 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrmig-p8.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrmig-p8.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-1-5-8-ihd-queri-installation-guide/001.png)

# Ischemic Heart Disease (IHD) Clinical Reminders


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Ischemic Heart Disease (IHD) Clinical Reminders](#ischemic-heart-disease-ihd-clinical-reminders)
    - [PXRM\1.5\8](#pxrm158)
    - [May 2002](#may-2002)
  - [Preface](#preface)
  - [Introduction](#introduction)
  - [Pre-Installation](#pre-installation)
  - [Installation](#installation)
  - [Setup and Maintenance](#setup-and-maintenance)
    - [Q & A – Helpful Hints](#q-a-helpful-hints)
- [<u>Appendices</u>](#uappendicesu)

### PXRM\*1.5\*8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> INSTALLATION AND SETUP GUIDE

### May 2002

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Revised: July 2002*
> Department of Veterans Affairs
> V*IST*A SD&D

## Preface 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Purpose of Installation and Setup Guide

> This Installation and Setup Guide describes how to prepare for, install, and implement the IHD reminders and dialogs contained in Clinical Reminders patch PXRM\*1.5\*8.

> To get further help information, please enter a NOIS call or call the National Help Desk: <span class="mark">REDACTED</span>

#### Recommended Users

- Department of Veterans Affairs Medical Center (VAMC) Information Resources Management (IRM) staff
- Clinical Reminders Managers

#### Related Manuals

> Clinical Reminders V. 1.5 Installation Guide (PXRMIG.PDF) Clinical Reminders V. 1.5 Manager Manual (PXRMTM.PDF)

> Manuals are available in Portable Document Format (PDF) at the following locations:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 31%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><ul>
<li><p>Albany</p></li>
</ul></th>
<th><mark>REDACTED</mark></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ul>
<li><p>Hines</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><ul>
<li><p>Salt Lake City</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

#### Web Sites

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 34%" />
<col style="width: 34%" />
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
<p>National SD&amp;D Reminders site</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals, Powerpoint presentations, and other information about Clinical Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="3"><blockquote>
<p>VHA/DoD CPG for Dyslipidemia</p>
</blockquote></td>
<td rowspan="3"><blockquote>
<p><u><a href="http://www.oqp.med.va.gov/cpg/DL/dl">http://www.oqp.med.va.gov/cpg/DL/dl</a>_cpg/algo4frameset.htm</u></p>
</blockquote></td>
<td><blockquote>
<p>The VHA/DoD CPG for Management of Dyslipidemia is a comprehensive guideline incorporating current information and practices for practitioners throughout the DoD and</p>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>system. See Section S, Table 3b for</p>
<p>reference to LDL&lt;120 in the</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Guideline.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Revision Table

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
<p>July 25, 2002</p>
</blockquote></td>
<td><blockquote>
<p>27, 33</p>
</blockquote></td>
<td><blockquote>
<p>Added the following text:</p>
<p>“Add the ORDER LIPID PROFILE health factor as an additional finding to Dialog Elements for lipid orders <em>if</em> your site wants the lipid order to satisfy the reminder for 1 month from the date the order is placed.</p>
<p>Otherwise, the reminder will be satisfied when the lab results for LDL are entered into VistA. “</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> Contents

Estimated Installation Time 6

[INSTALLATION 7](#installation)

1.  [Retrieve the PXRM\*1.5\*8 build 7](#retrieve-the-pxrm1.58-build)
2.  [Install the build first in a training or test account. 7](#install-the-build-first-in-a-training-or-test-account.)
3.  [Load the distribution. 7](#load-the-distribution.)
4.  [Unmap any mapped PXRM\* routines 8](#unmap-any-mapped-pxrm-routines.)
5.  [Disable journaling on the following globals 8](#disable-journaling-on-the-following-globals)
6.  [Install the package 8](#install-the-package.)
7.  [Build File Print 11](#build-file-print)
8.  [Install File Print 13](#install-file-print)
9.  [Enable journaling, if disabled in installation step 5 14](#enable-journaling-if-disabled-in-installation-step-5.)
10. [Map PXRM routines, if unmapped in a pre-installation step 14](#map-pxrm-routines-if-unmapped-in-a-pre-installation-step.)
11. [Post-installation routine 14](#post-installation-routine)

[SETUP AND MAINTENANCE 15](#setup-and-maintenance)

1.  [Verify correct installation of the “packed reminders.” 15](#verify-correct-installation-of-the-packed-reminders.)
2.  [Print and review the national IHD reminder definitions. 19](#print-and-review-the-national-ihd-reminder-definitions.)
3.  [Map local findings to the national Reminder Terms. 21](#map-local-findings-to-the-national-reminder-terms.)
4.  Run the Reminder Test option after term definition mapping is completed. 28
5.  [Use the Reminder Dialog options to edit the national (exported) dialogs 29](#use-the-reminder-dialog-options-to-edit-the-national-exported-dialogs.)
6.  [Verify that the reminders function properly 36](#verify-that-the-reminders-function-properly.)
7.  [Add the nationally distributed reminder dialogs to the CPRS Cover Sheet 37](#add-the-nationally-distributed-reminder-dialogs-to-the-cprs-cover-sheet)
8.  [Verify that the dialogs function properly 39](#verify-that-the-dialogs-function-properly)

## Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Background

> The Quality Enhancement Research Initiative (QUERI) is a program within the VA Health Services Research and Development Service (HSR&D). QUERI’s mission is to translate research innovations into improved quality of health care for veterans. The goal of the VA IHD• QUERI (Ischemic Heart Disease) group is to lessen the gap between clinical guideline recommended therapies and actual VA practice and to improve the process of evaluating health care delivery for patients with IHD receiving treatment in VA medical centers and outpatient clinics.

> The IHD clinical reminders in software patch PXRM\*1.5\*8 have been developed by the IHD QUERI Clinical Reminders Project and the Office of Information (OI) System Design & Development (SDD) Health Data Systems group. These reminders contain provider interventions for lipid management of patients with known Ischemic Heart Disease (IHD).

> The goal of the National IHD Clinical Reminders Project is to develop and nationally distribute clinical reminders that can be used by providers to facilitate lipid management of patients with Ischemic Heart Disease (IHD) and can aid in increasing adherence to national clinical practice guidelines.

#### VHA Guidelines & Measures Used for IHD Reminders

> VHA Clinical Practice Guidelines

- IHD patients should have a lipid profile every 1 to 2 years
- IHD patients taking lipid lowering agents should have a lipid profile at least every year
- The LDL goal for IHD patients is \<120 mg/dl

> VHA Performance Measures

- Percent of IHD patients at each facility with two qualifying encounters at specified clinic codes who have:
  - LDL in the past 2 years
  - LDL \< 120 mg/dl in the past 2 years

> A national data repository at the Austin Automation Center is also being developed to house guideline compliance data linked to the IHD clinical reminders. This database will provide facility-level quarterly summary reports for selected IHD performance measures.

#### QUERI/IHD Project Phases

> To meet the time constraints associated with this project, the project will be completed and delivered in two phases.

> Phase I:

- Develop two Reminder Definitions and Dialogs for clinical use:

#### Lipid Profile Reminder

- For lipid measurement: identifies patients with IHD who have not had a lipid panel w/ LDL in the last year

#### IHD Elevated LDL Reminder

- For LDL management: identifies patients with IHD who have had a lipid panel in the last year and the most recent LDL is \> 120 mg/dl

> Phase II:

- Develop two additional national reminders for lipid measurement/ management of patients with known IHD
  - For performance reports (not present in CPRS)
  - Based on VHA EPRP performance measures
- Develop a national data repository at the Austin Automation Center to house facility- level reminder data
- Develop software to transmit reminder data from each facility to the national repository
- Enhance clinical reminder reporting functionality so that reminder applicable/due counts can be generated for a specified timeframe and diagnosis
- Expected completion -- Fall 2002

#### Impact on Sites

- Installation of build

> Two IHD clinical reminders and dialogs are distributed in this patch (PXRM\*1.5\*8). The patch installation takes advantage of the reminder exchange utility and installs the reminders into the host system "silently". An email is generated if some of the reminder terms already exist on the host system and the install does not update the term. (This prevents overwriting any work already done at a site if the reminder or reminder term is being updated).

#### Setup and implementation by local team

> The following steps are required after the reminders have been installed on the system.

1.  Map Terms: As with all National Reminders, the IHD reminders are all built with reminder terms instead of individual health factors or other finding types. This allows a site to continue to use findings that already exist on the host system as data elements and to relate these local findings to the national terms. The individual health factors

> that match the reminder term are also distributed with the patch, so that a site that does not have a local finding can use the nationally distributed health factors to collect data.

> A detailed description of each reminder’s term that is distributed is included in the reminder description and in the manual.

> NOTE: Data rollup for the second phase of this project will be based on how you map your local findings to the national terms.

2.  Edit the reminder dialogs

> Once you have mapped the local findings to the national terms, you can then decide if you want to continue to use your local findings as the data elements that are captured or if you want to use the national findings that are already mapped to the national terms.

> If you want to continue to use your local findings, be sure to edit the reminder dialog by finding the element that allows for that data element to be collected. Change the finding item for that element to the local finding. The national reminders and dialogs cannot be changed except that you CAN change the finding item in the nationally distributed elements to use your local finding item instead of the nationally distributed one.

#### Impact on Clinicians

- Use of VA-IHD Reminders (or local equivalent) on cover sheet
- Resolution of reminders through CPRS point-and-click Reminder Resolution tools

> <span id="_TOC_250033" class="anchor"></span>Release Notes

> The following changes have been made to the Clinical Reminders application, as part of patch 8.

#### Patient Cohort Logic Changes – Most Recent Date (MRD)

> Changes have been made to the Patient Cohort Logic, to help resolve some problems identified by test sites for Patch 8.

1.  The reminder term logic will first find the most recent finding and then apply the Effective Period and Condition. This solves the problem where two LDLs have been done, one 6 months ago with a value \> 120, and the second LDL done with a different test with a value \< 120. The most recent LDL finding within a reminder term will be now be used to determine true or false value, rather than the most recent finding found with a true condition.
2.  Functions can now be used in the Patient Cohort Logic. A function called the "Most Recent Date" (MRD) function will return the most recent date from a list of finding items. The function will look something like the following: MRD(F1,F2,F3)

> Two MRD functions can be used with a comparison operator ("\>", "\<", "=") between them to compare the most recent date of finding lists. The result of the comparison is a True/False (1 or 0) condition.

> This helps resolve the problem with inside and outside tests, and potentially erroneous patient cohort logic.

> This is how the MRD function and comparison operation can help in the patient cohort logic:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Customized PATIENT COHORT LOGIC to see if the Reminder applies to a patient: FI(1)&amp;(MRD(FI(1))&gt;MRD(FI(13)))&amp;(FI(5)!FI(6)!FI(7))&amp;</p>
<p>(MRD(FI(5),FI(6),FI(7))&gt;MRD(FI(8),FI(3),FI(4)))</p>
<p>Expanded Patient Cohort Logic:</p>
<p>FI(IHD DIAGNOSIS)&amp;(MRD(FI(IHD DIAGNOSIS))&gt; MRD(FI(UNCONFIRMED IHD DIAGNOSIS)))&amp;(FI(OUTSIDE LDL 120-129)!</p>
<p>FI(OUTSIDE LDL &gt;129)!FI(LDL &gt;119))&amp;(MRD(FI(OUTSIDE LDL 120-129), FI(OUTSIDE LDL &gt;129),FI(LDL &gt;119))&gt;MRD(FI(LDL &lt;120),FI(OUTSIDE LDL &lt;100),</p>
<p>FI(OUTSIDE LDL 100-119)))</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> This means the patient cohort logic must have the following logic be true: The patient must have an IHD Diagnosis

> AND

> that a more recent UNCONFIRMED IHD Diagnosis does not exist AND

> the LDL from inside or outside must be 120 or greater AND

> a more recent inside or outside LDL result \<120 does not exist.

#### Managing nationally distributed reminders and dialogs

> All nationally distributed reminder dialogs will be distributed with a VA- prefix, and flagged as national. This applies to reminder dialogs, dialog groups, and dialog elements. The only field that will be editable in the national reminder dialog is the finding item in the dialog group and dialog elements. Any additional changes require 1) copying the reminder dialog to a local reminder dialog and 2) copy and replace functionality.

> A redistribution of the national reminder dialog will 1) save the dialog element finding items defined on your system, 2) install the dialog components, replacing the old dialog components, and 3) replace the local finding item values into the dialog components.

> Reminder Terms will not be overridden. If the reminder term already exists on your system, no added updates are made.

#### National Dialog Findings Management:

> The current dialog management has been modified so that if a national reminder dialog is selected, the screen display defaults to a DD view with finding items noted as shown in the example below. You can only edit the finding items in the individual dialog elements. The screen looks more like the exchange screen dialog, but allows selection of an element anywhere in the structure and editing of the FINDING ITEM and ADDITIONAL FINDING fields only.

> Previously, you couldn't see the findings in groups in the dialog edit screen, and you had to switch to group edit in order to change the finding on a group.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 55%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><p>REMINDER DIALOG NAME: VA-IHD LIPID PROFILE [NATIONAL]</p>
<blockquote>
<p>Item Seq. Dialog Details/Findings</p>
</blockquote></th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>VA-IHD LIPID PROFILE HEADER</p>
<p>Finding: *NONE*</p>
</blockquote></td>
<td>element</td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>VA-IHD LIPID ORDER GROUP</p>
</blockquote></td>
<td><blockquote>
<p>group</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>10.5</p>
</blockquote></td>
<td><blockquote>
<p>Finding: *NONE*</p>
<p>VA-IHD FASTING LIPID ORDERED</p>
</blockquote></td>
<td>element</td>
</tr>
</tbody>
</table>

## Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinical Reminders patch PXRM\*1.5\*8 adds two new reminders, two new dialogs, one new reminder taxonomy, and several new reminder terms and health factors to support the IHD project.

#### Required Software

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 33%" />
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
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>Fully patched (PXRM*1.5*7)</p>
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

#### Files installed

8.  REMINDER EXCHANGE FILE

> Adds entries to Reminder Definition, Health Factor, Reminder Taxonomy, Reminder Sponsor, and Reminder Dialog files.

#### Routines Installed

> PRE-INIT ROUTINE : PRE^PXRMP8I POST-INIT ROUTINE : POST^PXRMP8I

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Estimated Installation Time</strong></p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Installation</p>
</blockquote></td>
<td><blockquote>
<p>About 5 minutes</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Setup after installation by the Reminder</p>
</blockquote></td>
<td><blockquote>
<p>Approximately two-four hours (depending</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Manager or CAC to address local</p>
</blockquote></td>
<td><blockquote>
<p>partly on the number of local lab tests or</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>implementation</p>
</blockquote></td>
<td><blockquote>
<p>number of facilities within a health care</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>system)</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This build can be loaded with users on the system. Updating of cross-references for the new data added to the files will occur during the install.

#### The install needs to be done by a person with programmer access set to "@."

#### Retrieve the PXRM\*1.5\*8 build

> Use FTP to access the build, PXRM_1_5_8.KID, from one of the following locations:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 26%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SITE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>IP ADDRESS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DIRECTORY</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Albany</p>
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
<p>Hines</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Install the build first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

#### Load the distribution.

> In programmer mode, do ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, then the option LOAD a Distribution. Enter your directory name and PXRM_1_5_8.KID at the Host File prompt.

#### Example

> From the Installation menu, you may elect to use the following options (when prompted for INSTALL NAME, enter).

#### Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

#### Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

#### Verify Checksums in Transport Global

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.

> Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a NOIS and/or call the national Help Desk (1-888-596-HELP) to report the problem.

#### Print Transport Global

> This option will allow you to view the components of the KIDS build.

#### Unmap any mapped PXRM\* routines.

#### Disable journaling on the following globals:

#### Install the package.

> The install needs to be done by a person with programmer access set to "@."

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the package PXRM\*1.5\*8 and proceed with the install. If you have problems with the installation, log a NOIS and/or call the National Help Desk to report the problem.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Installation &amp; Distribution System Option: <strong>Installation</strong></p>
<p>Select Installation Option: <strong>INSTALL PACKAGE(S)</strong></p>
<p>Select INSTALL NAME: <strong>PXRM*1.5*8</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Answer "NO" to the following prompts:

> Want KIDS to INHIBIT LOGONs during install? YES// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

#### Installation Example

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Setting up programmer environment Terminal Type set to: C-VT220</p>
<p>Select OPTION NAME: <strong>XPD MAIN</strong> Kernel Installation &amp; Distribution System menu Edits and Distribution ...</p>
<p>Utilities ...</p>
<p>Installation ...</p>
<p>You have PENDING ALERTS</p>
<p>Enter "VA to jump to VIEW ALERTS option</p>
<p>Select Kernel Installation &amp; Distribution System Option: <strong>Installation</strong></p>
<p>Select Installation Option: <strong>1</strong> Load a Distribution Enter a Host File: <strong>PXRM_1_5_8.KID</strong></p>
<p>KIDS Distribution saved on Feb 21, 2002@10:25:19 Comment: PXRM*1.5*8 Build 02/21/2002</p>
<p>This Distribution contains Transport Globals for the following Package(s): Build PXRM*1.5*8 has been loaded before, here is when:</p>
<p>PXRM*1.5*8 Install Completed</p>
<p>was loaded on Feb 13, 2002@15:34:54 OK to continue with Load? NO// <strong>YES</strong></p>
<p>Distribution OK!</p>
<p>Want to Continue with Load? YES// <strong>&lt;Enter&gt;</strong></p>
<p>Loading Distribution...</p>
<p>PXRM*1.5*8</p>
<p>Use INSTALL NAME: PXRM*1.5*8 to install this Distribution.</p>
<p>Select Installation Option: <strong>Verify Checksums</strong> in Transport Global</p>
<p>Select INSTALL NAME: <strong>PXRM*1.5*8</strong> Loaded from Distribution 2/21/02@11:53:14</p>
<p>=&gt; PXRM*1.5*8 Build 02/21/2002 ;Created on Feb 21, 2002@10:25:19</p>
<p>This Distribution was loaded on Feb 21, 2002@11:53:14 with header of PXRM*1.5*8 Build 02/21/2002 ;Created on Feb 21, 2002@10:25:19 It consisted of the following Install(s):</p>
<p>PXRM*1.5*8</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> ANYWHERE</p>
<p>PACKAGE: PXRM*1.5*8 Feb 21, 2002 11:53 am PAGE 1</p>
<p>25 Routine checked, 0 failed.</p>
<p>Select Installation Option: <strong>Install Package(s)</strong></p>
<p>Select INSTALL NAME: <strong>PXRM*1.5*8</strong> Loaded from Distribution 2/21/02@11:53:14</p>
<p>=&gt; PXRM*1.5*8 Build 02/21/2002 ;Created on Feb 21, 2002@10:25:19</p>
<p>This Distribution was loaded on Feb 21, 2002@11:53:14 with header of PXRM*1.5*8 Build 02/21/2002 ;Created on Feb 21, 2002@10:25:19 It consisted of the following Install(s):</p>
<p>PXRM*1.5*8</p>
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
<p>Checking Install for Package PXRM*1.5*8 Install Questions for PXRM*1.5*8 Incoming Files:</p>
<p>811.8 REMINDER EXCHANGE FILE (including data) Note: You already have the 'REMINDER EXCHANGE FILE' File. I will REPLACE your data with mine.</p>
<p>Want KIDS to INHIBIT LOGONs during the install? YES// <strong>NO</strong></p>
<p>Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// <strong>NO</strong></p>
<p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.</p>
<p>DEVICE: HOME// <strong>&lt;Enter&gt;</strong> ANYWHERE</p>
<p>Install Started for PXRM*1.5*8 :</p>
<p>Feb 21, 2002@11:53:35</p>
<p>Build Distribution Date: Feb 21, 2002 Installing Routines:</p>
<p>Feb 21, 2002@11:53:35</p>
<p>Running Pre-Install Routine: PRE^PXRMP8I</p>
<p>Saving local mappings for term LIPID LOWERING MEDS INITIAL ORDER Saving local mappings for term LIPID LOWERING MEDS ADJUSTED Saving local mappings for term NO CHANGE IN IHD LIPID TREATMENT Saving local mappings for term OTHER DEFER ELEVATED LDL THERAPY Saving local mappings for term LIPID MGMT PROVIDED OUTSIDE</p>
<p>Installing Data Dictionaries:</p>
<p>Feb 21, 2002@11:53:36</p>
<p>Installing Data:</p>
<p>Feb 21, 2002@11:53:45</p>
<p>Installing PACKAGE COMPONENTS: Installing PRINT TEMPLATE Installing INPUT TEMPLATE</p>
<p>PXRM*1.5*8 Feb 21, 2002@11:53:45</p>
<p>Running Post-Install Routine: POST^PXRMP8I Installing reminder VA-IHD ELEVATED LDL Installing reminder VA-IHD LIPID PROFILE</p>
<p>Updating Routine file...</p>
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
<p>Updating KIDS files... PXRM*1.5*8 Installed.</p>
<p>Feb 21, 2002@11:54:30</p>
<p>Install Message sent Feb 21, 2002@11:54:30</p>
<p>+------------------------------------------------------------+ 100% ¦ 25 50 75 ¦ Complete +------------------------------------------------------------+</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> NOTE: Some sites have received error messages when installing patch 8, because the orderable item B index was incomplete, probably due to an OR patch that killed this index. If you have these problems installing patch 8, the 101.43 ORDERABLE ITEMS file needs re-indexing.

> The problem only appears if the IHD terms have been mapped to local orderable items. It should not affect new sites receiving the patch for the first time.

#### Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>The update failed, UPDATE^DIE returned the following error message: MSG("DIERR")=1^1</p>
<p>MSG("DIERR",1)=701 MSG("DIERR",1,"PARAM",0)=3</p>
<p>PXRM*1.5*8</p>
<p>MSG("DIERR",1,"PARAM",3)=OI.LDL, DIRECT MSG("DIERR",1,"PARAM","FIELD")=.01</p>
<p>MSG("DIERR",1,"PARAM","FILE")=811.52</p>
<p>MSG("DIERR",1,"TEXT",1)=The value 'OI.LDL, DIRECT' for field FINDING ITEM in FI. MSG("DIERR","E",701,1)=</p>
<p>REMINDER TERM entry did not get installed! Examine the above error message for the reason.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Build File Print

> Use the KIDS Build File Print option if you want a complete listing of package components (e.g., routines and options) exported with this software.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Utilities Option: <strong>Build File Print</strong></p>
<p>Select BUILD NAME: <strong>PXRM*1.5*8</strong> CLINICAL REMINDERS DEVICE: HOME// <strong>;;999</strong> ANYWHERE</p>
<p>PACKAGE: PXRM*1.5*8 Mar 25, 2002 7:56 am PAGE 1 TYPE: SINGLE PACKAGE</p>
<p>TRACK NATIONALLY: YES</p>
<p>NATIONAL PACKAGE: CLINICAL REMINDERS DESCRIPTION:</p>
<p>This patch contains national reminders for the IHD QUERI project:</p>
<p>VA-IHD ELEVATED LDL VA-IHD LIPID PROFILE</p>
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
<p>See national patch module for details. ENVIRONMENT CHECK :</p>
<p>PRE-INIT ROUTINE : PRE^PXRMP8I</p>
<p>POST-INIT ROUTINE : POST^PXRMP8I PRE-TRANSPORT RTN :</p>
<p>UP SEND DATA USER DATE SEC. COMES SITE RSLV OVER</p>
</blockquote>
<p>FILE # NAME DD CODE W/FILE DATA PTS RIDE</p>
<blockquote>
<p>811.8 REMINDER EXCHANGE FILE NO NO YES REPL YES NO DATA SCREEN: I (Y=3)!(Y=5)</p>
<p>PRINT TEMPLATE:</p>
<p>PXRM DEFINITION INQUIRY FILE #811.9 SEND TO SITE</p>
<p>INPUT TEMPLATE:</p>
<p>PXRM EDIT NATIONAL DIALOG FILE #801.41 SEND TO SITE</p>
<p>ROUTINE:</p>
<p>PXRMCF SEND TO SITE</p>
<p>PXRMDLG SEND TO SITE</p>
<p>PXRMDLG3 SEND TO SITE</p>
<p>PXRMDRUG SEND TO SITE</p>
<p>PXRMEDU SEND TO SITE</p>
<p>PXRMEXAM SEND TO SITE</p>
<p>PXRMEXU5 SEND TO SITE</p>
<p>PXRMHF SEND TO SITE</p>
<p>PXRMIMM SEND TO SITE</p>
<p>PXRMLAB SEND TO SITE</p>
<p>PXRMLOG SEND TO SITE</p>
<p>PXRMLOGF SEND TO SITE</p>
<p>PXRMLOGX SEND TO SITE</p>
<p>PXRMMEAS SEND TO SITE</p>
<p>PXRMMH SEND TO SITE</p>
<p>PXRMORDR SEND TO SITE</p>
<p>PXRMP8I SEND TO SITE</p>
<p>PXRMP8IA SEND TO SITE</p>
<p>PXRMP8IB SEND TO SITE</p>
<p>PXRMPTDF SEND TO SITE</p>
<p>PXRMPTL SEND TO SITE</p>
<p>PXRMRAD SEND TO SITE</p>
<p>PXRMSKIN SEND TO SITE</p>
<p>PXRMTAX SEND TO SITE</p>
<p>PXRMTERM SEND TO SITE</p>
<p>REQUIRED BUILDS: ACTION:</p>
<p>PXRM*1.5*9 Don't install, leave global</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Utilities Option: Install File Print</p>
<p>Select INSTALL NAME: PXRM*1.5*8 Install Completed 1/18/02@16:03:30</p>
<p>=&gt; PXRM PATCH 8 TEST ;Created on Jan 18, 2002@16:01:22 DEVICE: HOME// ;;999 ANYWHERE</p>
<p>PACKAGE: PXRM*1.5*8 Mar 25, 2002 7:57 am PAGE 1 COMPLETED ELAPSED</p>
<p>STATUS: Install Completed DATE LOADED: JAN 18, 2002@16:01:45 INSTALLED BY: HARTLEY,PETER</p>
<p>NATIONAL PACKAGE: CLINICAL REMINDERS</p>
<p>INSTALL STARTED: JAN 18, 2002@16:02:16 16:03:30 0:01:14</p>
<p>ROUTINES: 16:02:16</p>
<p>PRE-INIT CHECK POINTS:</p>
<p>XPD PREINSTALL STARTED 16:02:17 0:00:01</p>
<p>XPD PREINSTALL COMPLETED 16:02:17</p>
<p>FILES:</p>
<p>REMINDER EXCHANGE FILE 16:02:17</p>
<p>PRINT TEMPLATE 16:02:28 0:00:11</p>
<p>INPUT TEMPLATE 16:02:28</p>
<p>POST-INIT CHECK POINTS:</p>
<p>XPD POSTINSTALL STARTED 16:03:29 0:01:01</p>
<p>XPD POSTINSTALL COMPLETED 16:03:29</p>
<p>INSTALL QUESTION PROMPT ANSWER</p>
<p>XPI1 Want KIDS to INHIBIT LOGONs during the install NO XPZ1 Want to DISABLE Scheduled Options, Menu Options, and Protocols NO MESSAGES:</p>
<p>Install Started for PXRM*1.5*8 :</p>
<p>Jan 18, 2002@16:02:16</p>
<p>Build Distribution Date: Jan 18, 2002 Installing Routines:</p>
<p>Jan 18, 2002@16:02:16</p>
<p>Running Pre-Install Routine: PRE^PXRMP8I</p>
<p>Saving local mappings for term LIPID LOWERING MEDS INITIAL ORDER Saving local mappings for term LIPID LOWERING MEDS ADJUSTED Saving local mappings for term NO CHANGE IN IHD LIPID TREATMENT Saving local mappings for term OTHER DEFER ELEVATED LDL THERAPY</p>
<p>Saving local mappings for term LIPID MGMT PROVIDED OUTSIDE</p>
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
<p>Installing Data Dictionaries:</p>
<p>Jan 18, 2002@16:02:17</p>
<p>Installing Data:</p>
<p>Jan 18, 2002@16:02:28</p>
<p>Installing PACKAGE COMPONENTS: Installing PRINT TEMPLATE Installing INPUT TEMPLATE</p>
<p>Jan 18, 2002@16:02:28</p>
<p>Running Post-Install Routine: POST^PXRMP8I Installing reminder VA-IHD ELEVATED LDL Installing reminder VA-IHD LIPID PROFILE</p>
<p>Updating Routine file... Updating KIDS files...</p>
<p>PXRM*1.5*8 Installed.</p>
<p>Jan 18, 2002@16:03:30</p>
<p>Not a production UCI</p>
<p>NO Install Message sent</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Enable journaling, if disabled in installation step 5.

#### Map PXRM routines, if unmapped in a pre-installation step.

#### Post-installation routine

> The post-install routine, PXRMP8I, installs the two VA-IHD “packed” reminders into your Exchange File.

> After the installation has finished, if you discover that the reminder didn’t get installed correctly, for some reason, you can use the Exchange options on the Reminders Manager Menu to install the “packed” reminders.

## Setup and Maintenance 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After installing PXRM\*1.5\*8, follow the steps below to implement your IHD reminders and dialogs for this project. Setup may require as much as four hours, depending on your experience with reminders, whether you’re an integrated or single site, and on the number of lab tests your site(s) uses. Gathering relevant information, such as lists of lab tests and quick orders that will be mapped, will facilitate implementation.

> As with all national reminders, the IHD reminders are built with reminder terms instead of individual health factors or other finding types. This allows sites to continue to use findings that already exist on the host system as data elements and to relate these local findings to the national terms. The individual health factors that match the reminder term are also distributed with the patch, so that a site that doesn’t have a local finding can use the nationally distributed health factors to collect data.

> A detailed description of each reminder’s terms is included in the reminder description and also in Appendix C of this manual.

#### Setup Steps

#### Verify correct installation of the “packed reminders.”

1.  Using *Inquire about Reminder Definition* on the Reminder Management Menu, ensure that VA-IHD LIPID PROFILE and VA-IHD ELEVATED LDL have been installed.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Reminder Definiti</p>
<p>VA-IHD LIPID PROFILE DEVICE: <strong>;;999</strong> ANYWHERE REMINDER DEFINITION INQU</p>
<p>VA-IHD ELEVATED LDL</p>
<p>Print Name:</p>
</blockquote></th>
<th><blockquote>
<p>on: <strong>VA-IHD ELEVATED LDL</strong></p>
<p>NATIONAL</p>
<p>Right Margin: 80// <strong>&lt;Enter&gt;</strong></p>
<p>IRY Apr 05, 2002 3:07:19 pm Page 1</p>
<p>No. 73</p>
<p>IHD Elevated LDL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Class:</p>
</blockquote></td>
<td><blockquote>
<p>NATIONAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sponsor:</p>
</blockquote></td>
<td><blockquote>
<p>Office of Quality &amp; Performance</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Review Date:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Usage:</p>
</blockquote></td>
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Related VA-* Reminder:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reminder Dialog:</p>
</blockquote></td>
<td><blockquote>
<p>VA-IHD ELEVATED LDL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Etc.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### Using FileMan Inquiry, verify that the following health factors are on your system:

> Health factors have been grouped by categories, using generic names where possible so the health factor can be used for lipid management beyond the IHD diagnosis, where appropriate (e.g., DM, etc.). The following Health Factors are distributed pre- mapped to the Reminder Terms:

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Health Factor Category</strong></p>
<p>OUTSIDE LDL</p>
</blockquote></th>
<th><blockquote>
<p><strong>Health</strong></p>
<p>OUTSIDE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Factor</strong></p>
<p>LDL 100-119</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>OUTSIDE</td>
<td><blockquote>
<p>LDL</p>
</blockquote></td>
<td><blockquote>
<p>120-129</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td>OUTSIDE</td>
<td><blockquote>
<p>LDL</p>
</blockquote></td>
<td><blockquote>
<p>&lt;100</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>OUTSIDE</td>
<td><blockquote>
<p>LDL</p>
</blockquote></td>
<td><blockquote>
<p>&gt;129</p>
</blockquote></td>
</tr>
</tbody>
</table>

> LIPID PROFILE INTERVENTIONS

> ORDER LIPID PROFILE REFUSED LIPID PROFILE OTHER DEFER LIPID PROFILE

> LIPID MED INTERVENTIONS

> LIPID LOWERING MEDS INITIAL ORDER LIPID LOWERING MEDS ADJUSTED

> NO CHANGE IN IHD LIPID TREATMENT LIPID MEDS CONTRAINDICATED

> LIPID MGMT PROVIDED OUTSIDE REFUSED ELEVATED LDL THERAPY OTHER DEFER ELEVATED LDL THERAPY

> UNCONFIRMED DIAGNOSIS

> UNCONFIRMED IHD DIAGNOSIS

#### Using the Term Inquiry option on the Term Management Menu, verify that the following terms are on your system:

> ALANINE AMINO (ALT) (SGPT) IHD DIAGNOSIS

> LDL

> LDL \<120

> LDL \>119

> LIPID LOWERING MEDS

> LIPID LOWERING THERAPY MGMT - 2M LIPID LOWERING THERAPY MGMT - 6M LIPID MEDS CONTRAINDICATED

> LIPID PROFILE ORDERABLE

> ORDER LIPID PROFILE HEALTH FACTOR OTHER DEFER LIPID PROFILE

> OUTSIDE LDL \<100

> OUTSIDE LDL \>129

> OUTSIDE LDL 100-119

> OUTSIDE LDL 120-129

> REFUSED ELEVATED LDL THERAPY REFUSED LIPID PROFILE TRANSFERASE (AST) (SGOT) UNCONFIRMED IHD DIAGNOSIS

#### VA FileMan Print from the Reminder Term File

> You can also run a VA FileMan Print from the Reminder Term File (#811.5) that just sorts by name, and then prints name, finding, and condition. This is a useful list, especially when needing to map so many tests and you're not sure what values have been defined.

#### Example

2.  Using the Dialog Management option, verify that the VA-IHD LIPID PROFILE and VA-IHD ELEVATED LDL dialogs are installed on your system.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Reminder Managers Menu Option: <strong>DM</strong> Reminder Dialog Management DP Dialog Parameters ...</p>
<p>DI Reminder Dialogs</p>
<p>Select Reminder Dialog Management Option: <strong>DI</strong> Reminder Dialogs</p>
<p>Dialog List Apr 3, 2002@10:34:07 Page: 1 of 14 REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<p>Item Reminder Name Linked Dialog Name &amp; Dialog Status</p>
<p>14 BLOOD PRESSURE CHECK COPY OF BLOOD PRESSURE CHEC Disabled</p>
<p>16 CFTEST CFTEST Disabled</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ Enter ?? for more actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AR All reminders LR Linked Reminders QU Quit CV Change View RN Name/Print Name</p>
<p>Select Item: Next Screen// <strong>SL</strong> SL Search for: <strong>VA-IHD</strong></p>
<p><strong>Dialog List</strong> Apr 30, 2002@10:34:07 Page: 12 of 14 REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<p>+Item Reminder Name Linked Dialog Name &amp; Dialog Status</p>
</blockquote>
<ol start="186" type="1">
<li><p>VA-IHD ELEVATED LDL VA-IHD ELEVATED LDL</p></li>
<li><p>VA-IHD LIPID PROFILE VA-IHD LIPID PROFILE</p></li>
<li><p>VA-INFLUENZA VACCINE VA-INFLUENZA VACCINE Disabled</p></li>
<li><p>VA-MAMMOGRAM</p></li>
<li><p>VA-MST SCREENING VA-MST SCREENING</p></li>
<li><p>VA-NATIONAL EPI LAB EXTRACT</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>+ Enter ?? for more actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Find Next 'va-ihd'? Yes// <strong>no</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Print and review the national IHD reminder definitions.

> *Option: Inquire about Reminder Definition* on the *Reminder Management Menu.*

> You need to review the definitions in order to understand how they use reminder terms.

> *Do not make any changes to these reminders.* You may copy the national reminder to a local reminder and make any changes necessary.

> These two Clinical Reminders are designed for use by clinicians and are recommended for use in Primary Care Clinics (Primary Care/Medicine, GMC, Geriatric, Women’s) Cardiology Clinics, Cholesterol Screening Clinics and any other specialty clinics where primary care is given. These reminders take into consideration the day-to-day activities that can resolve the reminder, including temporary reminder resolutions such as placing an order.

#### VA-IHD LIPID PROFILE

> Patients with a diagnosis of IHD should have a Lipid Profile every one to two years. Those taking a lipid agent should have a lipid profile at least every year. The VHA/DOD Clinical Practice Guideline for Management of Dyslipidemia recommends that patients with Ischemic Heart Disease have a lipid profile/LDL every one to two years; and that patients taking lipid-lowering medications have a lipid profile/LDL at least every year

> This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code for IHD on or after 10/01/99) who have not had a serum lipid panel within the last year. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.

- A completed LDL lab test (calculated LDL or direct LDL) or documented outside LDL satisfies the reminder for 12 months from the lab test date.
- A documented order lipid profile health factor satisfies the reminder for 1 month.
- A patient's refusal to have an LDL level drawn satisfies the reminder for 6 months.
- Deferring the lipid profile for other reasons satisfies the reminder for 6 months.

#### NOTES:

> If your site has been using a more stringent LDL goal of \<100 mg/dl, see Appendix G for steps to take to change the reminder definitions and dialogs.

> If your site already has an LDL reminder for all patients, both the “all patient LDL” reminder and the “IHD Lipid Profile” reminder could become due for the same patient. To eliminate the possibility of redundant reminders appearing, modify the patient cohort logic in the “all patient LDL reminder,” as follows:

- Include the IHD Diagnosis Reminder Term as a finding, with USE IN PATIENT COHORT LOGIC with the AND NOT Boolean operator.

> If you have an LDL reminder for Diabetes patients, the redundancy could still occur if the patient also has an IHD Diagnosis. Decide which reminder should take precedence, and add the change above to the reminder definition of the reminder that should *not* become due.

#### VA-IHD ELEVATED LDL

> Patients with a diagnosis of IHD should have a Lipid Profile every one to two years. Those taking a lipid agent should have a lipid profile at least every year. The DOD/VHA Clinical Practice Guideline for the Management of Dyslipidemia in Primary Care recommends an LDL goal of \<120 mg/dl for patients with IHD, and the NCEP Adult Treatment Panel II recommends a more stringent goal of \<100 mg/dl.

> This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code for IHD on or after 10/01/99) who have had a serum lipid panel within the last year, where the most recent LDL lab test (or documented outside LDL) is greater than or equal

> to 120 mg/dl. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.

- Documenting an outside LDL \<120 mg/dl satisfies the reminder for 12 months from the lab test date.
- Ordering initial lipid-lowering medications or adjusting current lipid lowering medications satisfies the reminder for 2 months. (This is tracked by Health Factors, not the order.)
- A patient's refusal of lipid-lowering therapy satisfies the reminder for 6 months.
- Documenting that no treatment change is needed based on patient's current clinical status, that lipid management is provided by another VA or non-VA facility, or deferring lipid treatment for other reasons satisfies the reminder for 6 months.
- Documenting that lipid-lowering medications are contraindicated satisfies the reminder for 12 months.

#### NOTE: If your site has been using a more stringent LDL goal of \<100 mg/dl, see Appendix G for a description of how to change the reminder definitions and dialogs.

#### Map local findings to the national Reminder Terms.

> *Option: Reminder Term Management* on the *Reminder Management Menu.*

> Before using IHD reminders, map the local findings your site uses to represent the national reminder terms.

> The IHD reminders use reminder terms instead of individual health factors or other finding types, which lets you continue to use findings that may already exist in your system as data elements. These local findings can then be linked to the national terms. The individual health factors that match the reminder term are also distributed with the patch, so that a site that doesn’t have local findings can use the nationally distributed health factors to collect data.

- Prepare a list of your local findings – lab tests, health factors, etc. that you use to represent IHD terms.
- Review the national term definitions (see Appendix C or use the options on the Reminder Term Management menu), to compare these to what you are using locally to represent IHD terms.

#### IHD terms that *must* be mapped (no mapping included with distributed terms).

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 52%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Mapping Instructions</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Local Lab Tests or Orderables to Map</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>LDL</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab</p>
<p>Package for calculated LDL and direct LDL.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LDL &gt;119</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a CONDITION to identify LDL values &gt; 119. Although the condition is defined in the reminder, also define the condition in the term so the term can be used for uses that don't involve the reminder definition. If your site uses comments frequently you may want to</p>
<p>change the condition to check for specific text.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>LDL &lt; 120</strong></p>
</blockquote></td>
<td><blockquote>
<p>Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a CONDITION to identify LDL values &lt; 120. Although the condition is defined in the reminder, also define the condition in the term so the term can be used for purposes that don't involve the reminder definition. If your site uses comments frequently you may want to</p>
<p>change the condition to check for specific text.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LIPID PROFILE ORDERABLE</strong></p>
</blockquote></td>
<td><blockquote>
<p>Add local orderable items that your site uses to order direct LDL and calculated LDL lab tests (including lipid profiles with an LDL). Add the order dialog item</p>
<p>to the reminder dialog definition.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Pre-mapped Terms (additional mapping optional)

> If desired, add local Health Factors or findings representing these terms.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 41%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Local Health Factors to Map</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ALANINE AMINO (ALT) (SGPT)</strong></p>
</blockquote></td>
<td><blockquote>
<p>This term was distributed originally with the Hepatitis C Risk Assessment reminder. ALT tests should already be mapped at your site. The ALT lab test is</p>
<p>an informational finding in this reminder.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>IHD DIAGNOSIS</strong></p>
</blockquote></td>
<td><blockquote>
<p>No mapping is necessary. This term is distributed pre-mapped to the VA• ISCHEMIC HEART DISEASE</p>
<p>taxonomy. The Active Problem list, Inpatient Primary Diagnosis and Outpatient Encounter Diagnosis are used to search for ICD9 diagnoses.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 41%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Local Health Factors to Map</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>LIPID LOWERING MEDS</strong></p>
</blockquote></td>
<td><blockquote>
<p>This term is distributed pre-mapped to VA Generic Drug Names. Add any investigational drug names that are used but not mapped to the VA-Generic Drug. Enter the formulary drug names for investigation drugs.</p>
<p>Mapping non-investigative formulary drugs to the VA-GENERIC drugs in the Pharmacy Package will ensure the lipid lowering agents are found. The medications are informational findings for</p>
<p>this reminder.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LIPID LOWERING THERAPY MGMT – 2M</strong></p>
</blockquote></td>
<td><blockquote>
<p>The LIPID LOWERING MEDS INITIAL ORDER and LIPID LOWERING MEDS ADJUSTED health</p>
<p>factors are distributed pre-mapped to this term. If necessary, add local health factors representing these terms. Do not add orders or pharmacy medications as</p>
<p>findings for this term.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>LIPID LOWERING THERAPY MGMT – 6M</strong></p>
</blockquote></td>
<td><blockquote>
<p>The NO CHANGE IN IHD LIPID TREATMENT, OTHER DEFER ELEVATED LDL THERAPY, and LIPID MGMT PROVIDED OUTSIDE</p>
<p>health factors are distributed pre-mapped to this term. Add any local health factors, such as life expectancy &lt; 6 months, that your site is using that should</p>
<p>defer the lipid lowering management.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>LIPID MEDS CONTRAINDI• CATED</strong></p>
</blockquote></td>
<td><blockquote>
<p>Use the LIPID MEDS CONTRAIN•</p>
<p>DICATED health factor distributed with this term or add any local health factors representing contraindication to lipid</p>
<p>lowering medications</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>ORDER LIPID PROFILE HEALTH FACTOR</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: ORDER LIPID PROFILE. Add any local health factor representing the order action. Do not add orderable items to this reminder</p>
<p>term (see LIPID PROFILE ORDERABLE).</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>OTHER DEFER</strong></p>
<p><strong>LIPID PROFILE</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: OTHER</p>
<p>DEFER LIPID PROFILE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>OUTSIDE LDL &lt;100</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor:</p>
<p>OUTSIDE LDL &lt;100</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>OUTSIDE LDL &gt;129</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: OUTSIDE LDL &gt;129</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>OUTSIDE LDL 100•</strong></p>
<p><strong>119</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor:</p>
<p>OUTSIDE LDL 100-119</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 41%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Term</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Local Health Factors to Map</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>OUTSIDE LDL 120•</strong></p>
<p><strong>129</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor:</p>
<p>OUTSIDE LDL 120-129</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>REFUSED ELEVATED LDL THERAPY</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor: REFUSED ELEVATED</p>
<p>LDL THERAPY</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>REFUSED LIPID</strong></p>
<p><strong>PROFILE</strong></p>
</blockquote></td>
<td><blockquote>
<p>Distributed with Health Factor:</p>
<p>REFUSED LIPID PROFILE</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>TRANSFERASE (AST) (SGOT)</strong></p>
</blockquote></td>
<td><blockquote>
<p>This term was distributed originally with the Hepatitis C Risk Assessment</p>
<p>reminder. AST tests should already be mapped at your site.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>UNCONFIRMED IHD DIAGNOSIS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Use the UNCONFIRMED IHD</p>
<p>DIAGNOSIS health factor distributed with this term or add any local health factor representing an unconfirmed or incorrect IHD diagnosis.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> NOTE: It isn’t necessary to enter an Effective Period when mapping terms, as this is already in the reminder definition. Enter an Effective Period only if you want to override the entry in the definition.

#### Example: Mapping a Local Finding to the LDL Reminder Term

> Determine all labs tests that mean “LDL” LDL (CALCULATED)

> DIRECT LDL

> Is there only one of each?

> No panels: only individual tests

> Examples:

> LDL CHOLESTEROL

> LDL CHOLESTEROL, PASCO LDL, DIREC

> NOTE: The reminder definition “LDL” finding contains the condition "I +V\>0." The “+” causes the result to be treated as a number. If it’s only text, it will treat it as a zero. This condition can be added to the reminder term also, if desired, but it isn’t necessary.

<table style="width:100%;">
<colgroup>
<col style="width: 24%" />
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 23%" />
<col style="width: 24%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Reminder Term</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>Management Option: <strong>TE</strong></p>
</blockquote></th>
<th><blockquote>
<p>Reminder Term Edit</p>
</blockquote></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="4"><blockquote>
<p>Select Reminder Term: <strong>LDL</strong></p>
</blockquote>
<ol type="1">
<li><p>LDL NATIONAL</p></li>
<li><p>LDL &lt;120 NATIONAL</p></li>
</ol></td>
<td></td>
<td colspan="2"><blockquote>
<p><strong>This is the local finding that is mapped to the national term. Note that it</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3 LDL &gt;119</p>
<p>CHOOSE 1-3: 1 LDL Select FINDING ITEM:</p>
</blockquote></td>
<td><blockquote>
<p>NATIONAL NATIONAL</p>
<p><strong>LT.LDL</strong></p>
</blockquote></td>
<td></td>
<td colspan="2"></td>
<td><blockquote>
<p><strong>must use a prefix (LT for</strong></p>
<p><strong>Lab test, HF for Health Factor, etc.).</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Searching for a</p>
<p>Searching for a</p>
</blockquote></td>
<td><blockquote>
<p>LABORATORY</p>
<p>LABORATORY</p>
</blockquote></td>
<td><blockquote>
<p>TEST,</p>
<p>TEST</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>(pointed-to by FINDING ITEM)</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

#### Defining the CONDITION:

> Two LDL laboratory test reminder terms need a CONDITION value added to the finding: LDL \>119 should have a CONDITION of “I V\>119” (not in quotes) (*See example below)* LDL \<120 should have a CONDITION of “(I V\<120)&(+V\>0)” (not in quotes) (*See example below)*

> The condition is on the reminder definition if you forget, but the CONDITION should also be added to the CONDITION field in the mapped finding items. This will allow the reminder term to stand alone, without requiring the reminder definition to further define what the term represents.

> The CONDITION is not mandatory on all finding items mapped to reminder terms. The CONDITION field needs to be defined for laboratory finding items requiring additional logic to identify positive and negative results. The CONDITION for a finding item mapped to a Reminder Term must be written in M code based on very specific Boolean formatting (e.g., I V\[“POS”). If the finding value is text, enclose the Boolean logic comparison value in quotes (e.g., "positive"). If the finding value is numeric, do not use quotes. Use VA FileMan Help for a detailed explanation of the CONDITION field. For details about allowed CONDITIONS for each finding item, see the *Clinical Reminders Manager Manual*.

#### LDL \>119 Mapping Example

> No tests are distributed for this term. Add direct and calculated LDL test names. The Reminder definition has a CONDITION of I V\>119. Add this condition for the individual findings in the reminder term also.

#### LDL \<120 Mapping Example

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>1</th>
<th><blockquote>
<p>LDL CHOLESTEROL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>LDL-CHOL CALCULATION</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><blockquote>
<p>LDL/HDL RATIO</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Example: Mapping Terms with Health Factors

> LIPID LOWERING THERAPY MGMT - 6M

> Use the health factors distributed with this reminder term or enter any local health factors or other findings that should defer the reminder for 6 months. Health Factors distributed with this reminder term are:

#### NO CHANGE IN IHD LIPID TREATMENT OTHER DEFER ELEVATED LDL THERAPY LIPID MGMT PROVIDED OUTSIDE

> Add Local health factor: ELEVATED HEPATIC ENZYMES

> Example: Mapping Drug Findings

> LIPID LOWERING MEDS

> Enter the formulary drug names for investigation drugs.

> Mapping non-investigative formulary drugs to the VA-GENERIC drugs in the Pharmacy Package will ensure the lipid lowering agents are found. The medications are informational findings for this reminder.

#### Examples:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 31%" />
<col style="width: 22%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NIACIN</p>
</blockquote></th>
<th><blockquote>
<p>CHOLESTYRAMINE</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>LOVASTATIN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>PRAVASTATIN</p>
</blockquote></td>
<td><blockquote>
<p>SIMVASTATIN</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>FLUVASTATIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ATORVASTATIN</p>
</blockquote></td>
<td><blockquote>
<p>FENOFIBRATE</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CERIVASTATIN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>COLESEVELAM</p>
</blockquote></td>
<td><blockquote>
<p>COLESTIPOL</p>
</blockquote></td>
<td><blockquote>
<p>CLOFIBRATE</p>
</blockquote></td>
<td><blockquote>
<p>GEMFIBROZIL</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Effective Period: the amount of time the finding will remain valid. BOTH: inpatient & outpatient medications

#### Example: Mapping LIPID PROFILE ORDERABLE

> This term is not distributed with any mappings. Enter orderable items for lipid panels that include LDL tests (calculated LDL and direct LDL). The orderable items are informational findings for this reminder. The order will not resolve the reminder, but it will display in the clinical maintenance. Ideally, the clinician will look at the clinical maintenance display to avoid entering duplicate orders. This reminder term is not used in the resolution logic since the future order could be far in the future. (Copy this reminder and add LIPID PROFILE ORDERABLE to the resolution findings if you want the next due date to be calculated based on the future date the order is to be done. NOTE: This may be a problem if your site allows lab ordering far into the future; e.g., 6 months. *SEE THE CAUTION ON PAGE 33.*)

#### Local Findings Examples:

> Finding Item: LDL, DIRECT (FI(1)=OI(2463))

> Finding Type: ORDERABLE ITEM

> Finding Item: CARDIAC PROFILE, PASCO (FI(2)=OI(7397))

> Finding Type: ORDERABLE ITEM

> Finding Item: CARDIAC RISK PANEL (FI(3)=OI(6873))

> Finding Type: ORDERABLE ITEM

#### Lipid Profile Mapping Example

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>LIPASE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>LIPID PHENOTYPE EVAL.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>LIPID PROFILE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>LIPIDS, QUALITATIVE</p>
<p>LIPIDS, TOTAL</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Run the Reminder Test option after term definition mapping is completed. Review the results of patient data with each of the findings mapped to the term. *Option: Reminders Test* on the *Reminder Managers Menu*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Reminder Managers Menu Option: <strong>RT</strong> Reminder Test</p>
<p>Select Patient: <strong>APPLESEED,JOHNNY</strong> 4-30-44 466680999 YES EMPLOYEE</p>
<p>Enrollment Priority: GROUP 5 Category: IN PROCESS End Date: Select Reminder: <strong>VA-IHD LIPID PROFILE</strong> NATIONAL</p>
<p>The elements of the FIEV array are:</p>
<p>FIEV(1)=1</p>
<p>FIEV(1,"CODEP")=2500 <strong>NOTE: See the Clinical Reminders</strong></p>
<p>FIEV(1,"DATE")=3000328.2121 <strong>Manager Manual for descriptions of</strong></p>
<p>FIEV(1,"FINDING")=14;PXD(811.2, <strong>the different elements of the test</strong></p>
<p>FIEV(1,"SOURCE")=2094;AUPNVPOV <strong>output.</strong></p>
<p>FIEV(1,"TERM")=IHD DIAGNOSIS^^^3010723</p>
<p>FIEV(1,"VIEN")=3898 FIEV(2)=0</p>
<p>FIEV(3)=0 FIEV(4)=0 FIEV(5)=0 FIEV(6)=1</p>
<p>FIEV(6,"DATE")=3011119.1534 FIEV(6,"FINDING")=82;AUTTHF( FIEV(6,"LEVEL")= FIEV(6,"SOURCE")=448;AUPNVHF( FIEV(6,"TERM")=OUTSIDE LDL &gt;129^^^3011113 FIEV(6,"VALUE")=</p>
<p>FIEV(6,"VIEN")=5370 FIEV(7)=0</p>
<p>FIEV(8)=1 FIEV(8,"DATE")=3011119.1534 FIEV(8,"FINDING")=85;AUTTHF( FIEV(8,"LEVEL")= FIEV(8,"SOURCE")=450;AUPNVHF(</p>
<p>FIEV(8,"TERM")=REFUSED LIPID PROFILE^^^3011022</p>
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
<p>FIEV(8,"VALUE")= FIEV(8,"VIEN")=5370 FIEV(9)=0</p>
<p>FIEV(10)=0 FIEV(12)=0 FIEV(13)=0 FIEV(14)=0 FIEV("DFN")=37</p>
<p>FIEV("PATIENT AGE")=57</p>
<p>The elements of the ^TMP(PXRMID,$J) array are:</p>
<p>^TMP(PXRMID,$J,70,"FINDING 12 NOT_FOUNDB")=No active lipid lowering agents on file.</p>
<p>^TMP(PXRMID,$J,70,"FINDING 2 NOT_FOUNDB")=Patient with IHD and no LDL lab results on file in the past year.</p>
<p>^TMP(PXRMID,$J,70,"HEALTH FACTOR OUTSIDE LDL &gt;129")=11/19/2001 Health Factor: OUTSIDE LDL</p>
<p>&gt;129</p>
<p>^TMP(PXRMID,$J,70,"HEALTH FACTOR REFUSED LIPID PROFILE")=11/19/2001 Health Factor: REFUSED LIPID PROFILE</p>
<p>^TMP(PXRMID,$J,70,"ICD9VPOV 411.1","CODE")=411.1</p>
<p>^TMP(PXRMID,$J,70,"ICD9VPOV 411.1","DATE")=3000328.2121</p>
<p>^TMP(PXRMID,$J,70,"ICD9VPOV 411.1","DIAG")=INTERMED CORONARY SYND</p>
<p>^TMP(PXRMID,$J,70,"ICD9VPOV 411.1","PN")=Angina pectoris, unstable</p>
<p>^TMP(PXRMID,$J,70,"PATIENT COHORT LOGIC")=1^FI(1)&amp;($$MAX^PXRMLOGF("FI(1,"DATE")"</p>
<p>)&gt;$$MAX^PXRMLOGF("FI(10,"DATE")"))^1&amp;($$MAX^PXRMLOGF("3000328.2121")&gt;$$MAX^PXRMLOGF(""))</p>
<p>^TMP(PXRMID,$J,70,"REMINDER NAME")=IHD Lipid Profile</p>
<p>^TMP(PXRMID,$J,70,"RESOLUTION LOGIC")=1^(0)!FI(2)!FI(3)!FI(4)!FI(5)!FI(6)!FI(7)! FI(8)!FI(9)^(0)!0!0!0!0!1!0!1!0</p>
<p>^TMP(PXRMID,$J,70,"WARNING","DIAT")=Warning no do in advance time</p>
<p>^TMP(PXRMID,$J,70,"WARNING","NOFI")=Warning no findings items in reminder term L IPID PROFILE ORDERABLE</p>
<p>^TMP(PXRMID,$J,70,"zFREQARNG")=Due every 6 months for all ages</p>
<p>The elements of the ^TMP("PXRHM",$J) array are:</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile")=RESOLVED^3020521.1534^3011119.1534</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",1)=</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",2)=Applicable: Due every 6 months for all ages within cohort.</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",3)=Reminder Term: IHD DIAGNOSIS</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",4)=03/28/2000 Encounter Diagnosis:</p>
<p>411.1 INTERMED CORONARY SYND</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",5)= Prov. Narr. - Angina pectoris, unstable</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",6)=</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",7)=Resolution: Last done 11/19/2001</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",8)=Patient with IHD and no LDL lab results on file in the past year.</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",9)=Reminder Term: OUTSIDE LDL &gt;129</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",10)=11/19/2001 Health Factor: OUTSIDE LDL &gt;129</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",11)=Reminder Term: REFUSED LIPID PROFILE</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",12)=11/19/2001 Health Factor: REFUSED LIPID PROFILE</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",13)=</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",14)=Information:</p>
<p>^TMP("PXRHM",$J,70,"IHD Lipid Profile","TXT",15)=No active lipid lowering agents on file.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Use the Reminder Dialog options to edit the national (exported) dialogs.

> Once you have mapped the local findings to the national terms, you can then decide if you want to continue to use your local findings as the data elements that are captured, or if you want to use the national findings that are already mapped to the national terms.

> If you want to continue to use your local findings, then be sure to edit the reminder dialog by identifying the element that allows for that data element to be collected. Change the finding item for that element to the local finding. The national reminders and dialogs can

> *only* be changed by changing the finding item in the nationally distributed elements to use your local finding item instead of the nationally distributed one.

> Elements are distributed for ordering the lipid panel, liver enzymes, and the drugs most often used in treatment. You must enter quick order names or menus into the reminder dialog as the finding item for these elements, if the ordering functions are to work at your site. If you don’t want to use the ordering functions from the reminder dialogs, you will need to copy the national reminder dialog and remove the elements that you don’t want to use from the copy.

#### VA-IHD LIPID PROFILE

> Review dialog elements in the national reminder dialog and change any health factors to local health factors, if desired. Refer to the reminder term mapping section for distributed vs. local health factors.

> If your site has a Lipid Panel TIU Object, add this TIU Object to the dialog element header text. The Lipid Panel TIU Object should include Chol, Trigly, HDL, LDL-C, and direct LDL values and dates. If your site has developed TIU objects to display lipid panel results, we recommend adding these before the dashed line in the dialog header.

> Add the Order Dialog entries to the Dialog elements used for ordering a calculated LDL and/or direct LDL.

> The OTHER DEFER LIPID PROFILE term is where sites can add items such as “Life Expectancy \< 1 year”, “Life Expectancy \< 6 months” that they may be collecting.

> Some sites have clinicians order a consult to send to a service that corrects unconfirmed diagnoses the clinician finds in a patient's record. If your site has this method in place, copy the reminder dialog to a local reminder dialog and add the existing dialog element to the reminder dialog so that this practice can continue.

#### Steps to add or edit dialog elements:

1.  Select Dialog management (DM) from the Reminders Manager Menu, then select Dialog (DI):
2.  Use the Search List (SL) action to get to the IHD–named dialogs, then enter the number of the reminder.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog List</strong> Mar 22, 2002@09:30:16 Page: 12 of 14 REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<p>+Item Reminder Name Linked Dialog Name &amp; Dialog Status</p>
</blockquote>
<ol start="188" type="1">
<li><p>VA-IHD ELEVATED LDL VA-IHD ELEVATED LDL</p></li>
<li><p>VA-IHD LIPID PROFILE VA-IHD LIPID PROFILE</p></li>
<li><p>VA-INFLUENZA VACCINE VA-INFLUENZA VACCINE Disabled</p></li>
<li><p>VA-MAMMOGRAM</p></li>
<li><p>VA-MST SCREENING VA-MST SCREENING</p></li>
<li><p>VA-NATIONAL EPI LAB EXTRACT</p></li>
<li><p>VA-NATIONAL EPI RX EXTRACT</p></li>
<li><p>VA-NUTRITION/OBESITY EDUCATION</p></li>
<li><p>VA-PAIN SCREENING VA-PAIN SCREEN AND HX</p></li>
<li><p>VA-PAP SMEAR</p></li>
<li><p>VA-PNEUMOVAX VA-PNEUMOVAX</p></li>
<li><p>VA-PPD VA-PPD Disabled</p></li>
<li><p>VA-PSA VA-PSA Disabled</p></li>
<li><p>VA-QUERI REPORT IHD ELEVATED LDL</p></li>
<li><p>VA-QUERI REPORT LIPID STATUS</p></li>
<li><p>VA-SEATBELT EDUCATION VA-SEATBELT EDUCATION Disabled</p></li>
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
<p>AR All reminders LR Linked Reminders QU Quit CV Change View RN Name/Print Name</p>
<p>Select Item: Next Screen// <strong>189</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Select the dialog number to see details.

<table>
<colgroup>
<col style="width: 3%" />
<col style="width: 4%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 22%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5"><blockquote>
<p><strong>Dialog Selection List</strong> Mar 22, 2002@09:30:16 REMINDER NAME: VA-IHD LIPID PROFILE</p>
</blockquote></th>
<th><blockquote>
<p>Page: 1 of 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>Item</p>
</blockquote></td>
<td><blockquote>
<p>Dialog Name</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Latest Update</p>
</blockquote></td>
<td><blockquote>
<p>Linked Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>This reminder is linked to dialog:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>VA-IHD LIPID PROFILE</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>VA-IHD LIPID PROFILE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>+</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p><strong>+ Next Screen</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>- Prev Screen</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>?? More Actions</strong></p>
</blockquote></td>
<td><strong>&gt;&gt;&gt;</strong></td>
</tr>
<tr class="odd">
<td colspan="5"><blockquote>
<p>AD Autogenerate Dialog QU Quit LR Link Reminder</p>
<p>Select Item: Quit// <strong>1</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="5"><blockquote>
<p>1 5 VA-IHD LIPID PROFILE HEADER Finding: *NONE*</p>
</blockquote></td>
<td><blockquote>
<p>element</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="5"><ol start="2" type="1">
<li><p>10 VA-IHD LIPID ORDER GROUP Finding: *NONE*</p></li>
<li><blockquote>
<p>10.5 VA-IHD FASTING LIPID ORDERED Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>10.10 VA-IHD DIRECT LDL ORDERED Finding: *NONE*</p>
</blockquote></li>
</ol></td>
<td><blockquote>
<p>group element element</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="5"><ol start="5" type="1">
<li><p>15 VA-IHD LIPID DONE ELSEWHERE GROUP Finding: *NONE*</p></li>
<li><blockquote>
<p>15.10 VA-IHD LIPID &lt;100 DONE ELSE</p>
</blockquote></li>
</ol>
<blockquote>
<p>Finding: OUTSIDE LDL &lt;100 (HEALTH FACTOR)</p>
</blockquote>
<ol start="7" type="1">
<li><blockquote>
<p>15.15 VA-IHD LIPID 100-119 DONE ELSE</p>
</blockquote></li>
</ol>
<blockquote>
<p>Finding: OUTSIDE LDL 100-119 (HEALTH FACTOR)</p>
</blockquote></td>
<td><blockquote>
<p>group element element</p>
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
<p>Select Item: Next Screen// NEXT SCREEN</p>
</blockquote>
<ol start="8" type="1">
<li><p>15.20 VA-IHD LIPID 120-129 DONE ELSE element</p></li>
</ol>
<blockquote>
<p>Finding: OUTSIDE LDL 120-129 (HEALTH FACTOR)</p>
</blockquote>
<ol start="9" type="1">
<li><blockquote>
<p>15.25 VA-IHD LIPID &gt;129 DONE ELSE element Finding: OUTSIDE LDL &gt;129 (HEALTH FACTOR)</p>
</blockquote></li>
<li><p>20 VA-IHD LIPID REFUSED element</p></li>
</ol>
<blockquote>
<p>Finding: REFUSED LIPID PROFILE (HEALTH FACTOR)</p>
</blockquote>
<ol start="11" type="1">
<li><blockquote>
<p>25 VA-IHD LIPID OTHER DEFER element Finding: OTHER DEFER LIPID PROFILE (HEALTH FACTOR)</p>
</blockquote></li>
<li><p>30 VA-IHD SPACER element</p></li>
</ol>
<blockquote>
<p>Finding: *NONE*</p>
<p>DP Progress Note Text INQ Inquiry/Print Select Item: Next Screen// <strong>&lt;Enter&gt;</strong> NEXT SCREEN</p>
<p><strong>Dialog Edit List</strong> Mar 22, 2002@09:30:16 Page: 3 of 3</p>
<p>REMINDER DIALOG NAME: VA-IHD LIPID PROFILE [NATIONAL]</p>
<p>+Item Seq. Dialog Details/Findings Type</p>
</blockquote>
<ol start="13" type="1">
<li><blockquote>
<p>35 VA-IHD UNCONFIRMED DIAGNOSIS element Finding: UNCONFIRMED IHD DIAGNOSIS (HEALTH FACTOR)</p>
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
<p>DP Progress Note Text INQ Inquiry/Print</p>
<p>Select Item: Quit//</p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Select the Item \# of the dialog element you wish to add or edit a finding for.
- At some sites, clinicians order a consult that corrects unconfirmed diagnoses the clinician finds in a patient's record. If your site has this method in place, copy the reminder dialog to a local reminder dialog, and add the existing dialog element to the reminder dialog, so that this practice can continue.

#### VA-IHD ELEVATED LDL

- If your site has a Lipid Panel and AST/ALT TIU Object, add this TIU Object to the dialog element header text. The TIU Object should include Chol, Trigly, HDL, LDL-C, direct LDL, AST, and ALT values and dates. If your site has developed TIU objects to display these lab tests, we recommend adding these before the dashed line in the dialog header.
- Add the Order Dialog entries to the Dialog elements used for ordering a calculated LDL and/or direct LDL, and AST/ALT.
- The VA-IHD LIPID LOWER AGENT ORDER GROUP contains a sampling of orders related to starting the patient on lipid lowering medication, which includes future lab orders to monitor liver function and lipid levels. The distributed group contains:
  - Order Simvastatin -- Note: Sites using a different first-line lipid lowering agent should replace Simvastatin with that medication (e.g., Pravastatin).
  - Order baseline LFTs today (if not available w/in past year).
  - Order LFTs in 60 days after starting therapy.
  - Order fasting Lipid Profile in 60 days.
- The dialog elements in the VA-IHD LIPID LOWER AGENT ORDER GROUP need to have order dialogs added that represent the level of order detail,

> or

- Remove the dialog elements from the group and add an order dialog menu or order dialog items that will help the clinician place the initial lipid lowering medications.
- The VA-IHD LIPID LOWER AGENT ADJUST GROUP contains a dialog element that recommends using the meds tab to cancel old and order new medications. It also includes dialog elements for future lab orders to monitor liver function and lipid levels.

> NOTE: Use the Meds tab to discontinue the current lipid agent and order a new lipid agent.

- Order LFTs today (if not available within the past year).
- Order LFTs in 60 days after starting therapy.
- Order fasting Lipid Profile in 60 days.
- The dialog elements for lab orders in the VA-IHD LIPID LOWER AGENT ADJUST GROUP are the same as the VA-IHD LIPID LOWER AGENT ORDER GROUP. The dialog elements in the dialog group need to have order dialogs added that represent the level of order detail, or remove the dialog elements from the group and add an order dialog menu or order dialog items that will help the clinician place new lipid-lowering medications.
- Review dialog elements in the national reminder dialog and change any health factors to local health factors—refer to the reminder term mapping for distributed vs. local health factors.
- At some sites, clinicians order a consult to send to a service, which corrects unconfirmed diagnoses the clinician finds in a patient's record. If your site has this method in place, copy the reminder dialog to a local reminder dialog and add the existing dialog element to the reminder dialog so this practice can continue.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog Selection List</strong> Mar 22, 2002@09:30:16 Page: 1 of 1</p>
<p>REMINDER NAME: VA-IHD ELEVATED LDL</p>
<p>Item Dialog Name Latest Update Linked Reminders This reminder is linked to dialog:</p>
<p>1 VA-IHD ELEVATED LDL VA-IHD ELEVATED LDL BACKUP-IHD ELEVATED L</p>
</blockquote></th>
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
<p>AD Autogenerate Dialog QU Quit LR Link Reminder</p>
<p>Select Item: Quit// <strong>1</strong></p>
<p>1 5 VA-IHD ELEVATED LDL HEADER element Finding: *NONE*</p>
</blockquote>
<ol start="2" type="1">
<li><p>10 VA-IHD LIPID LOWER AGENT ORDER GROUP group Finding: LIPID LOWERING MEDS INITIAL ORDER (HEALTH FACTOR)</p></li>
<li><blockquote>
<p>10.5 VA-IHD SIMVASTATIN ORDERED element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>10.10 VA-IHD ORDER BASELINE LFTS TODAY element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>10.15 VA-IHD ORDER FUTURE LFTS 60 DAYS element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>10.20 VA-IHD ORDER FUTURE LIPID PROFILE 60 DAYS element Finding: *NONE*</p>
</blockquote></li>
<li><p>15 VA-IHD LIPID LOWER AGENT ADJUST GROUP group Finding: LIPID LOWERING MEDS ADJUSTED (HEALTH FACTOR)</p></li>
</ol>
<blockquote>
<p>DP Progress Note Text INQ Inquiry/Print Select Item: Next Screen// NEXT SCREEN</p>
</blockquote>
<ol start="8" type="1">
<li><blockquote>
<p>15.5 VA-IHD LIPID LOWER AGENT ADJUST TEXT element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>15.10 VA-IHD ORDER BASELINE LFTS TODAY element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>15.15 VA-IHD ORDER FUTURE LFTS 60 DAYS element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>15.20 VA-IHD ORDER FUTURE LIPID PROFILE 60 DAYS element Finding: *NONE*</p>
</blockquote></li>
<li><p>20 VA-IHD LIPID TREATMENT NO CHANGE element Finding: NO CHANGE IN IHD LIPID TREATMENT (HEALTH FACTOR)</p></li>
<li><p>25 VA-IHD LIPID MEDS CONTRAINDICATED element Finding: LIPID MEDS CONTRAINDICATED (HEALTH FACTOR)</p></li>
<li><blockquote>
<p>30 VA-IHD LIPID LOWER AGENT ELSEWHERE element DP Progress Note Text INQ Inquiry/Print</p>
</blockquote></li>
</ol>
<blockquote>
<p>Select Item: Next Screen// NEXT SCREEN</p>
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
<p>Finding: LIPID MGMT PROVIDED OUTSIDE (HEALTH FACTOR)</p>
</blockquote>
<ol start="15" type="1">
<li><p>35 VA-IHD SPACER element</p></li>
</ol>
<blockquote>
<p>Finding: *NONE*</p>
</blockquote>
<ol start="16" type="1">
<li><blockquote>
<p>40 VA-IHD LIPID DONE ELSEWHERE &lt;120 GROUP group Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>40.5 VA-IHD LIPID DONE ELSEWHERE TEXT element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>40.10 VA-IHD LIPID &lt;100 DONE ELSE element Finding: OUTSIDE LDL &lt;100 (HEALTH FACTOR)</p>
</blockquote></li>
<li><blockquote>
<p>40.15 VA-IHD LIPID 100-119 DONE ELSE element Finding: OUTSIDE LDL 100-119 (HEALTH FACTOR)</p>
</blockquote></li>
<li><blockquote>
<p>45 VA-IHD LIPID/ALT/AST ORDER GROUP group Finding: *NONE*</p>
</blockquote></li>
</ol>
<blockquote>
<p>DP Progress Note Text INQ Inquiry/Print Select Item: Next Screen// NEXT SCREEN</p>
</blockquote>
<ol start="21" type="1">
<li><blockquote>
<p>45.5 VA-IHD FASTING LIPID ORDERED element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>45.10 VA-IHD DIRECT LDL ORDERED element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>45.15 VA-IHD ALT/AST ORDERED element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>50 VA-IHD ELEVATED LDL REFUSED element Finding: REFUSED ELEVATED LDL THERAPY (HEALTH FACTOR)</p>
</blockquote></li>
<li><blockquote>
<p>55 VA-IHD ELEVATED LDL OTHER DEFER element Finding: OTHER DEFER ELEVATED LDL THERAPY (HEALTH FACTOR)</p>
</blockquote></li>
<li><p>60 VA-IHD SPACER element</p></li>
</ol>
<blockquote>
<p>Finding: *NONE*</p>
<p>Select Item: Next Screen// <strong>&lt;Enter&gt;</strong> NEXT SCREEN</p>
<p><strong>Dialog Edit List</strong> Mar 22, 2002@09:30:16 Page: 5 of 5</p>
<p>REMINDER DIALOG NAME: VA-IHD ELEVATED LDL [NATIONAL]</p>
<p>+Item Seq. Dialog Details/Findings Type</p>
</blockquote>
<ol start="27" type="1">
<li><blockquote>
<p>65 VA-IHD UNCONFIRMED DIAGNOSIS element Finding: UNCONFIRMED IHD DIAGNOSIS (HEALTH FACTOR)</p>
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
<p>DP Progress Note Text INQ Inquiry/Print</p>
<p>Select Item: Quit//</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Verify that the reminders function properly.

1.  Run a Reminders Due Report to determine if the IHD Clinical Reminder statuses reported are correct.

> *Option: Reminders Due* on the *Reminder Reports menu*

> This report can be displayed at the beginning of the day for patients being seen that day. Reminder reports offer a way to review how the mapping and the local data will

> potentially be viewed by the extracts that will be sent to the Austin database from the reminders.

- Each of the reminders can be used in a reminder report to evaluate clinics or stop codes on their adherence/compliance with that reminder.
- The reports can be run to list individual patient names for chart review on reasons that the guideline was not or could not be achieved.
- Clinics, stop codes, or divisions can be identified by summary reports using these reminders where there are differences in compliance or poor adherence to the guideline.
2.  Use the Reminder Test option to test the reminders.

> *Option: Reminders Test* on the *Reminder Management menu*

1)  Select a patient who has an IHD diagnosis and an LDL test done within the last year, and using the Reminder Test option, run the VA-IHD LIPID PROFILE reminders for this patient. The status of the reminder should be “DONE.”
2)  Select a patient who has an IHD diagnosis and has not had an LDL test done within the last year, and using the Reminder Test option, run the VA-IHD LIPID PROFILE reminders for this patient. The status of the reminder should be “DUE.”
3)  Select a patient who does not have an IHD diagnosis. Run the VA-IHD LIPID PROFILE and VA-IHD ELEVATED LDL reminders for this patient. The status of both the reminders should be “NOT APPLICABLE” (even if they have an LDL).
4)  Select a patient who has an IHD diagnosis and an LDL test done within the last year, where the LDL \<120, and using the Reminder Test option, run the VA-IHD ELEVATED LDL reminders for this patient. The status of the reminder should be “Not Applicable.”
5)  Select a patient who has an IHD diagnosis and an LDL test done within the last year, where the LDL \> 119, and using the Reminder Test option, run the VA-IHD ELEVATED LDL reminders for this patient. The status of the reminder should be “DUE.”

#### Add the nationally distributed reminder dialogs to the CPRS Cover Sheet

- VA-IHD LIPID PROFILE
- VA-IHD ELEVATED LDL
  1.  Open a patient chart, click on the reminders clock, and when the available Reminders window opens, click on Action, and then select “Edit Cover Sheet Reminder List.”
  2.  ![](pxrm-1-5-8-ihd-queri-installation-guide/002.png)![](pxrm-1-5-8-ihd-queri-installation-guide/003.png)When the Cover Sheet Reminder List opens, find the IHD-named dialogs.
  3.  Click on the IHD Lipid Profile dialog and click the Add button (or double-click the dialog).
  4.  Click on the IHD Elevated LDL dialog and click the Add button (or double-click the dialog).

> ![](pxrm-1-5-8-ihd-queri-installation-guide/004.png)

#### Verify that the dialogs function properly

> Test the IHD Reminder dialogs in CPRS, using either the exported dialogs or your locally created dialogs. Using point-and-click reminder resolution processing through CPRS GUI, verify the following:

- Correct Progress Note text is posted
- Finding Item gets sent to PCE
- Reminder is satisfied

> Check the Clinical Maintenance component display in CPRS after testing dialogs to ensure all activities tested are reflected in the clinical maintenance display.

#### Steps to test dialogs:

1.  On the cover sheet, click on the Reminders icon.
2.  Click on reminders in the Reminders box to see details of a reminder
3.  Open the Notes tab and select New Note. Enter a title.
4.  Open the Reminders drawer and review the contents. Comment on what you see and what you expect. Try opening and closing folders.
5.  Locate the VA-IHD LIPID PROFILE reminder dialog and open it.

> ![](pxrm-1-5-8-ihd-queri-installation-guide/005.png)

6.  ![](pxrm-1-5-8-ihd-queri-installation-guide/006.png)In the dialog box, check relevant actions.
7.  Finish the reminder processing.
8.  Review the text added to the note to assure its correctness.
9.  Ensure that the reminder can be satisfied by the individual finding items that were mapped to the reminder terms.
10. Check the Clinical Maintenance component display in Health Summaries and CPRS after the reminder dialog is complete.

![](pxrm-1-5-8-ihd-queri-installation-guide/007.png)

11. Locate the VA-IHD ELEVATED LDL reminder dialog and open it.

> ![](pxrm-1-5-8-ihd-queri-installation-guide/008.png)

12. ![](pxrm-1-5-8-ihd-queri-installation-guide/009.png)In the dialog box, check relevant actions.
13. Finish the reminder processing.
14. Review the text added to the note to assure its correctness.
15. Ensure that the reminder can be satisfied by the individual finding items that were mapped to the reminder terms.
16. Check the Clinical Maintenance component display in Health Summaries and CPRS after the reminder dialog is complete.

![](pxrm-1-5-8-ihd-queri-installation-guide/010.png)

### Q & A – Helpful Hints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Q: What diagnoses are used to define “IHD” for these reminders?

> A. ICD-9 codes 410.0-412 and 414.0-414.9, which include the following diagnoses: acute myocardial infarction, old myocardial infarction, post MI syndrome, and coronary atherosclerosis.

#### Q: Why are health factors for outside LDL levels included in these reminders?

1.  Capture of outside (historical) lab results is important in the management of veterans with IHD. Some veteran patients choose to receive health care from both VA as well as private health care providers (co-managed care). Other veterans seek seasonal care at VA sites other than their “home” VA.

#### Q: Are there restrictions on the drugs we can order?

> A: Check with your local VA site regarding the formulary medication choices available for lipid management.

#### Q: What is a National Reminder?

> A: National reminders are clinical reminders and reminder dialogs that have gone through an approval process for national distribution. Some national reminders are related to statutory, regulatory, or Central Office mandates such as Hepatitis C, MST, or Pain. Other national reminders are being developed under the guidance of the VA Clinical Practice Guideline Council.

> Guideline-related reminders are being developed for two reasons:

1.  To provide reminders for sites that don’t have reminders in place for a specific guideline (e.g., HTN, HIV).
2.  To provide a basic set of reminders to all sites to improve clinical care, and also allow roll-up data for measurement of guideline implementation and adherence (e.g., IHD, Mental Health).

#### Q: How can we check parameters to see if anyone sees the reminder?

> A: The simplest way to view whether an individual is seeing the IHD reminders is to open the reminder cover sheet editor by clicking on the reminder clock in CPRS, picking \*\*\* and then choosing “Edit Cover Sheet Reminders.” A button on the dialog allows you to view the entire list of reminders that are seen by an individual user.

> From the listing above, you can determine "where" the reminder that a user sees actually comes from (System level, Division, Location, User, etc.). You should make a determination as to whether the reminder needs to be added at a specific level in order to be seen by the appropriate group of users.

> Any clinicians who see primary care patients or who might need or want to follow or manage LDL values should see the IHD Lipid Profile reminder. In many centers, the nurses who manage or have the ability to enter policy orders should also see this reminder.

> The IHD Elevated LDL Reminder should also be seen by these same clinicians and potentially by the nursing staff.

#### Q: What should we do if we already have an IHD reminder?

> A: If you elect to continue to use your local reminder and dialog, you need to make sure that your local health factors and lab tests are mapped appropriately to the national terms.

> If you prefer to continue using your local reminder, you need to be absolutely sure that you are collecting all of the data that will eventually be transmitted to the Austin database.

> In many cases, it may be safer to switch to using the national reminder or a copy of the national reminder in order to be sure that all of the possible resolutions are being collected locally. There is nothing wrong with abandoning some local health factors or reminders in favor of using the national dialogs and reminders or copies of them. Health factors that you elect to stop collecting in dialogs should be inactivated so that they are not inadvertently entered through PCE.

#### All patient LDL Reminders

> If your site already has an LDL reminder for all patients, the “all patient LDL” reminder and the “IHD Lipid Profile” reminder could become due for the same patient. To eliminate the possibility of redundant reminders showing up, you will need to modify the patient cohort logic in the “all patient LDL reminder” to include:

- The IHD Diagnosis Reminder Term as a finding, with USE IN PATIENT COHORT LOGIC with the AND NOT Boolean operator.

> If you have an LDL reminder for Diabetes patients, the redundancy could still occur if the patient also has an IHD Diagnosis. Decide which reminder should take precedence, and add the change above to the reminder definition of the reminder that should *not* become due.

#### NOTES

> The released reminders do not address all possible IHD or lipid management issues.

> There is still a need for hyperlipidemia screening reminders and for lipid management reminders for other high-risk populations (e.g. diabetes and vascular disease).

> These reminders do not address other important Ischemic Heart Disease performance measures; e.g., Beta blocker use post MI, ASA use post MI.

#### Other Local Reminder Issues

> Modifications in term evaluation logic may change how some reminder terms work. This is only an issue if there are conditions within the term

- Previous logic: date of most recent finding in which the condition is true is passed to the reminder for evaluation
- New logic: Most recent finding in the term is used and then condition applied and results passed to the reminder for evaluation.

> *Implications of term logic changes:*

> –Terms that combine lab tests will always pass forward the most recent result

> –Terms that combine dissimilar findings (immunizations, medications and orderable items) may not behave as they did before.

#### Term Logic Change Example

> A term combining various ways to document influenza immunizations:

> Finding Item: INFLUENZA ICD &CPT CODES FI(5)=TX(664003))

> Finding Type: REMINDER TAXONOMY

> Finding Item: INFLUENZA (FI(9)=IM(12))

> Finding Type: IMMUNIZATION

> Finding Item: INFLUENZA (FI(10)=DG(141))

> Finding Type: VA GENERIC Effective Period: 1Y

> Finding Item: INFLUENZA INJ (FI(11)=OI(2892))

> Finding Type: ORDERABLE ITEM Condition: I V="complete"

1.  An immunization administered in November 2001 and documented in the PCE immunization file.
2.  An order placed (orderable item) for an immunization that was not completed.

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Old Logic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>New Logic</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>The more recent orderable item is</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>The most recent finding is the orderable item</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>incomplete and doesn’t meet the condition.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>The reminder is satisfied by the “im”</p>
</blockquote></td>
<td><blockquote>
<p>The orderable item does not meet the condition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>finding which is true</p>
</blockquote></td>
<td><blockquote>
<p>and the term reports a “false”.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>The reminder is satisfied</p>
</blockquote></td>
<td><blockquote>
<p>The reminder is due</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Hints for Successful Term Mapping

1.  Review any reminders related to lipid management that already exist on your system. You may have lipid management reminders for all patients, diabetes patients, or patients with IHD.
2.  List any health factors or data elements being collected in the local reminders.
3.  Find any lab tests that represent an LDL level—currently in use or used in the past year.
4.  Go through each reminder term listed in the reminder definitions and enter each of the local findings (health factors and lab tests) that match up with the reminder term.
5.  Then, take your lists of local findings and make sure that each one is matched up to at least one reminder term.
6.  Then, check each reminder term and make sure that there is at least one finding in each term that is being used in a dialog.

# <u>Appendices</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Appendix A: IHD Reminder Descriptions Appendix B: IHD Dialog Descriptions Appendix C: IHD Reminder Term Descriptions

> Appendix D: IHD Reminder Taxonomy Descriptions Appendix E: IHD Reminder Health Factors Appendix F: Abbreviated Setup Steps

> Appendix G: Modifying Reminders and Dialogs for a More Stringent LDL Value

#### Appendix A: IHD Reminder Definitions

> Background:

> The PXRM\*1.5\*8 patch contains two new national IHD reminders for clinicians documenting interventions for lipid management of patients with known Ischemic Heart Disease (IHD). The IHD QUERI Workgroup and the Office of Information (OI) System Design & Development (SDD) Clinician Desktop Group developed the clinical reminders.

> A central data repository at the Austin Automation Center is being developed to house guideline compliance totals for the data captured from these IHD clinical reminders. This database will provide facility-level quarterly summary reports for the IHD lipid management performance measures. A second set of IHD national reporting reminders will roll up compliance data to the central data repository with a future patch.

#### VA-IHD LIPID PROFILE

> Applicable

- Patients with known IHD
- ICD-9 410-412 or 414 on or after 10/01/99
- Inpatient primary diagnosis, outpatient diagnosis, problem list

> *The reminder is not applicable if there is more recent documentation that the IHD diagnosis is unconfirmed*

#### Resolution

- Completed LDL (or documented outside LDL) - 12 mo
- Patient refuses lipid testing - 6 mo
- Provider defers lipid testing – 6 mo
- Ordering a lipid profile/LDL (health factor) – 1 mo

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>REMINDER DEFINITION INQU VA-IHD LIPID PROFILE</p>
<p>Print Name:</p>
</blockquote></th>
<th><blockquote>
<p>IRY Apr 04, 2002 4:0</p>
</blockquote>
<p>No. 70</p>
<p>IHD Lipid Profile</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Class:</p>
</blockquote></td>
<td><blockquote>
<p>NATIONAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Sponsor:</p>
</blockquote></td>
<td><blockquote>
<p>Office of Quality &amp; Performance</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Review Date:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Usage:</p>
</blockquote></td>
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Related VA-* Reminder:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Reminder Dialog:</p>
</blockquote></td>
<td><blockquote>
<p>VA-IHD LIPID PROFILE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Priority:

> Reminder Description:

> The VHA/DOD Clinical Practice Guideline for Management of Dyslipidemia recommends that patients with Ischemic Heart Disease have a lipid profile/LDL every one to two years; and that patients taking lipid lowering medications have a lipid profile/LDL at least every year.

> This national reminder identifies patients with known IHD (i.e., a documented ICD-9 code for IHD on or after 10/01/99) who have not had a serum lipid panel within the last year. If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will not be applicable to the patient.

> A completed LDL lab test (calculated LDL or direct LDL) or documented outside LDL satisfies the reminder for 12 months.

> A documented order lipid profile health factor satisfies the reminder for

> 1 month.

> A patient's refusal to have an LDL level drawn satisfies the reminder for

> 6 months.

> Deferring the lipid profile for other reasons satisfies the reminder for

> 6 months.

> Technical Description:

> This reminder is recommended for use by clinicians at Primary Care Clinics (Primary Care/Medicine, GIMC, Geriatric, Women's), Cardiology, Cholesterol Screening and any other specialty clinics where primary care is given.

> The reminder goes beyond the IHD/Module 8: MI Ambulatory Care Follow-up LDL-C EPRP Performance Measure, by including more than the 412 diagnostic codes.

> Setup issues before using this reminder:

1.  Use the Reminder Term options to map local representations of findings:

> IHD DIAGNOSIS

> No mapping necessary. Use the VA-ISCHEMIC HEART DISEASE reminder taxonomy distributed with this term.

> UNCONFIRMED IHD DIAGNOSIS

> Use the UNCONFIRMED IHD DIAGNOSIS health factor distributed with this term or add any local health factor representing an unconfirmed or incorrect IHD diagnosis.

> LDL Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL without a CONDITION.

> For the following OUTSIDE LDL Reminder Terms, use the health factors distributed with the reminder term or enter the local Health Factor used to represent these values.

> OUTSIDE LDL \<100

> OUTSIDE LDL 100-119

> OUTSIDE LDL 120-129

> OUTSIDE LDL \>129

> ORDER LIPID PROFILE HEALTH FACTOR

> Use the health factor distributed with this term or add

> any local health factor representing the order action. Do not add orderable items to this reminder term (see LIPID PROFILE ORDERABLE). This represents the date the order was placed, not the date the order will be done in

> the future. The order placement will cause the reminder to be resolved for 1 month. (Alternatively, copy this reminder and add LIPID PROFILE ORDERABLE to the resolution findings if you want the next due date to be calculated based on the future date the order is to be done.)

> LIPID PROFILE ORDERABLE

> Enter orderable items for lipid panels that include LDL tests (calculated LDL and direct LDL).

> The orderable items are informational findings for

> this reminder. The order will not resolve the reminder, but it will display in the clinical maintenance.

> Ideally, the clinician will look at the clinical maintenance display to avoid entering duplicate orders. This reminder term is not used in the resolution logic since the future order could be for a long distance in the future. (Copy this reminder and add LIPID PROFILE ORDERABLE to the resolution findings if you want the next due date to be calculated based on the future date the order is to be done.)

> OTHER DEFER LIPID PROFILE

> Enter any local health factors or other findings that should defer the reminder for 6 months. For example, "LIFE EXPECTANCY \< 6M".

> REFUSED LIPID PROFILE

> Use the health factor distributed with this term or add any local health factor representing refusal of lipid profile test.

> LIPID LOWERING MEDS

> Enter the formulary drug names for investigation drugs. Mapping non-investigative formulary drugs to the

> VA-GENERIC drugs will ensure the lipid lowering medications are found. The medications are informational findings for this reminder.

2.  Use the Reminder Dialog edit option to define the national reminder dialog finding items which should be updated during CPRS GUI reminder processing.

> Add local Order Dialog entries to the Dialog elements used for ordering a calculated LDL and/or direct LDL.

> Review dialog elements in the national reminder dialog and change any national health factors to local health factors, if necessary. It is not unusual for local findings to be used in your national dialogs.

> Any local findings used in the national dialogs should be mapped to the appropriate national reminder term.

3.  Alternatively, use the Reminder Dialog options to copy the national dialog, dialog elements, and dialog groups to make local changes.

> If your site has a Lipid Panel TIU Object, add this TIU Object to the local dialog element header text. The TIU Object should include Chol, Trigly, HDL, LDL-C, Direct LDL values and dates.

> Add local dialog elements with local Order Dialogs for additional ordering options for the clinicians. Some sites have clinicians order a consult to a service that corrects unconfirmed diagnoses the clinician finds in a patient's record. If your site has this

> method in place, copy the reminder dialog to a local reminder dialog and then add the local dialog element for the consult order to the reminder dialog so this practice can continue.

> Edit History:

> Baseline Frequency:

> Do In Advance Time Frame: Wait until actually DUE Sex Specific:

> Ignore on N/A:

> Frequency for Age Range: 1 year for all ages Match Text:

> No Match Text:

> Findings:

> Finding Item: IHD DIAGNOSIS (FI(1)=RT(27))

> Finding Type: REMINDER TERM

> Use in Patient Cohort Logic: AND

> Effective Date: OCT 01, 1999 Use Inactive Problems: N

> Not Found Text: Patient has no IHD Diagnosis on file.

> Finding Item: LDL (FI(2)=RT(32)) Finding Type: REMINDER TERM

> Use in Resolution Logic: OR

> Condition: I +V\>0

> Not Found Text: Patient with IHD and no LDL lab results on file in the past year.

> Finding Item: OUTSIDE LDL \<100 (FI(3)=RT(35))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 1Y

> Finding Item: OUTSIDE LDL 100-119 (FI(4)=RT(34))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 1Y

> Finding Item: OUTSIDE LDL 120-129 (FI(5)=RT(52))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 1Y

> Finding Item: OUTSIDE LDL \>129 (FI(6)=RT(36))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 1Y

> Finding Item: ORDER LIPID PROFILE HEALTH FACTOR (FI(7)=RT(61))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 1M

> Finding Item: REFUSED LIPID PROFILE (FI(8)=RT(40))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 6M

> Finding Item: OTHER DEFER LIPID PROFILE (FI(9)=RT(41))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 6M

> Found Text: The lipid profile is deferred for 6 months.

> Finding Item: UNCONFIRMED IHD DIAGNOSIS (FI(10)=RT(42))

> Finding Type: REMINDER TERM Match Frequency/Age: 1 year for all ages

> Use in Patient Cohort Logic: AND NOT

> Finding Item: LIPID LOWERING MEDS (FI(12)=RT(54))

> Finding Type: REMINDER TERM Effective Period: 90D

> Not Found Text: No active lipid lowering agents on file.

> Finding Item: LIPID PROFILE ORDERABLE (FI(14)=RT(39))

> Finding Type: REMINDER TERM General Patient Cohort Found Text:

> General Patient Cohort Not Found Text:

> General Resolution Found Text:

> General Resolution Not Found Text:

> Customized PATIENT COHORT LOGIC to see if the Reminder applies to a patient: FI(1)&(MRD(FI(1))\>MRD(FI(10)))

> Expanded Patient Cohort Logic:

> FI(IHD DIAGNOSIS)&(MRD(FI(IHD DIAGNOSIS))\> MRD(FI(UNCONFIRMED IHD DIAGNOSIS)))

> Default RESOLUTION LOGIC defines findings that resolve the Reminder: FI(2)!FI(3)!FI(4)!FI(5)!FI(6)!FI(7)!FI(8)!FI(9)

> Expanded Resolution Logic:

> FI(LDL)!FI(OUTSIDE LDL \<100)!FI(OUTSIDE LDL 100-119)! FI(OUTSIDE LDL 120-129)!FI(OUTSIDE LDL \>129)!

> FI(ORDER LIPID PROFILE HEALTH FACTOR)!FI(REFUSED LIPID PROFILE)! FI(OTHER DEFER LIPID PROFILE)

> Web Sites:

> Web Site URL: <http://www.oqp.med.va.gov/cpg/DL/dl_cpg/algo4frameset.htm>

> Web Site Title: VHA/DoD CPG for Dyslipidemia

> The VHA/DoD CPG for Management of Dyslipidemia is a comprehensive guideline incorporating current information and practices for practitioners throughout the DoD and Veterans Health Administration system. See Section S, Table 3b for reference to LDL\<120 in the Guideline.

#### VA-IHD ELEVATED LDL

> Applicable

- Patients with known IHD
- ICD-9 410-412 or 414 on or after 10/01/99
- Inpatient primary diagnosis, outpatient diagnosis, problem list

> *The reminder is not applicable if there is more recent documentation that the IHD diagnosis is unconfirmed*

#### Resolution

- Ordering initial lipid lowering medications or adjusting current lipid lowering medications (health factor) - 2 mo
- Documenting that no lipid treatment change is needed based on patient’s current status- 6 mo
- Documenting that lipid management is provided by another VA or non-VA facility - 6 mo
- Patient refuses lipid lowering therapy or provider defers lipid treatment - 6 mo
- Documenting an outside LDL \<120mg/dL - 12 mo
- Documenting that lipid lowering medications are contraindicated – 12 mo

> REMINDER DEFINITION INQUIRY

> Apr 10, 2002 11:47:48

> am Page 1

> VA-IHD ELEVATED LDL No. 73

> Print Name: IHD Elevated LDL

> Class: NATIONAL

> Sponsor: Office of Quality & Performance Review Date:

> Usage: CPRS

> Related VA-\* Reminder:

> Reminder Dialog: VA-IHD ELEVATED LDL Priority:

> Reminder Description:

> The VHA/DOD Clinical Practice Guideline for Management of Dyslipidemia recommends

> an LDL goal of \<120 mg/dl for patients with Ischemic Heart Disease; and the NCEP

> Adult Treatment Panel II recommends a more stringent goal of \<100 mg/dl.

> This national reminder identifies patients with known IHD (i.e., a

> documented ICD-9 code on or after 10/01/99) who have had a serum lipid

> panel within the last

> year, where the most recent LDL lab test

> (or

> documented outside LDL) is greater than or equal to 120 mg/dl. If a more

> recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the reminder will

> not be applicable to the patient.

> Documenting an outside

> LDL \<120 mg/dl satisfies the reminder

> for 12

> months from the lab test date.

> Ordering initial lipid lowering medications or adjusting current lipid lowering medications satisfies the reminder for 2 months. (This is tracked by Health Factors, not the order.)

> A patient's refusal of lipid lowering therapy satisfies the reminder for

> 6 months.

> Documenting that no treatment change is needed based on patient's current clinical status, that lipid management is provided by another VA or

> non-VA facility, or deferring lipid treatment for other reasons satisfies the reminder for 6 months.

> Documenting that lipid lowering medications are contraindicated satisfies the reminder for 12 months.

> Technical Description:

> This reminder is recommended for use by clinicians at Primary Care Clinics (Primary Care/Medicine, GIMC, Geriatric, Women's), Cardiology, Cholesterol Screening and any other specialty clinics where primary care is given.

> The reminder goes beyond the IHD/Module 8: MI Ambulatory Care Follow-up LDL-C EPRP Performance Measure, by including more than the 412 diagnostic codes.

> Setup issues before using this reminder:

1.  Use the Reminder Term options to map local representations of findings:

> IHD DIAGNOSIS

> No mapping necessary. Use the VA-ISCHEMIC HEART DISEASE reminder taxonomy distributed with this term.

> UNCONFIRMED IHD DIAGNOSIS

> Use the UNCONFIRMED IHD DIAGNOSIS health factor distributed with this term or add any local health factor representing an unconfirmed or incorrect IHD diagnosis.

> LDL \>119

> Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a CONDITION to identify LDL values \> 119. Although the condition is defined in the reminder, also define the condition in the term so the term can be used for uses that don't involve the reminder definition. If your site uses

> comments frequently you may want to change the condition to check for specific text.

LDL \<120

Enter the Laboratory Test names from the Lab Package for calculated LDL and direct LDL with a CONDITION to identify LDL values \< 120. Although the condition is defined in the reminder, also define the condition in the term so the term can be used for uses that don't involve the reminder definition. If your site uses

comments frequently you may want to change the condition to check for specific text.

> For the following OUTSIDE LDL Reminder Term representations, use the health factors distributed with the term or map the local

> Health Factor used to represent these values: OUTSIDE LDL \<100

> OUTSIDE LDL 100-119

> OUTSIDE LDL 120-129

> OUTSIDE LDL \>129

> LIPID LOWERING THERAPY MGMT - 2M

> Use the health factors distributed with this reminder term or enter any local health factors or other findings that should defer the reminder for 2 months. Health Factors distributed with this reminder term are:

> LIPID LOWERING MEDS INITIAL ORDER LIPID LOWERING MEDS ADJUSTED

> LIPID LOWERING THERAPY MGMT - 6M

> Use the health factors distributed with this reminder term or enter any local health factors or other findings that should defer the reminder for 6 months. Health Factors distributed with this reminder term are:

> NO CHANGE IN IHD LIPID TREATMENT OTHER DEFER ELEVATED LDL THERAPY LIPID MGMT PROVIDED OUTSIDE

> REFUSED ELEVATED LDL THERAPY

> Use the REFUSED ELEVATED LDL THERAPY health factor distributed with this term or add any local health factor representing the patient's refusal to have elevated LDL therapy provided.

> LIPID MEDS CONTRAINDICATED

> Use the LIPID MEDS CONTRAINDICATED health factor distributed with this term or add any local health factors representing contraindication to lipid lowering medications.

> LIPID LOWERING MEDS

> Enter the formulary drug names for investigation drugs. Mapping non-investigative formulary drugs to the

> VA-GENERIC drugs in the Pharmacy Package will ensure the lipid lowering agents are found. The medications are informational findings for this reminder.

> TRANFERASE (AST)

> This reminder term should already be mapped at your site from the Hepatitis C EPI patch setup. The AST lab test is an informational finding in this reminder.

> ALANINE AMINO (ALT)

> This reminder term should already be mapped at your site from the Hepatitis C EPI patch setup. The ALT lab test is an informational finding in this reminder.

2.  Use the Reminder Dialog edit option to define the national reminder dialog finding items which should be updated during CPRS GUI reminder processing.

> Review dialog elements in the national reminder dialog and change any national health factors to local health factors, if necessary. It is not unusual for local findings to be used in your national dialogs. Any local findings used in the national dialogs should be mapped to the appropriate national reminder term.

> Review dialog elements in the national reminder dialog and change any health factors to local health factors - refer to the reminder term mapping for distributed vs. local health factors.

> Add local Order Dialog items to the Dialog elements used for ordering a calculated LDL and/or direct LDL, and AST/ALT.

> Add local Order Dialog items to the Dialog Elements for clinicians to order initial lipid lowering medications or lab work. The dialog group contains a sampling of orders related to starting the patient on lipid lowering medication, which includes future lab orders to monitor liver function and lipid levels. The distributed group contains:

> Order Simvastatin -- Note: Sites using a different first line lipid lowering agent should replace Simvastatin with that medication (e.g., Pravastatin), which will require

> copying the national dialog reminder, and editing the local copy with local dialog elements.

> Order baseline LFTs today (if not available w/in past year). Order LFTs in 60 days after starting therapy.

> Order fasting Lipid Profile in 60 days.

> The Adjust lipid lowering medication dialog group contains a dialog element that recommends using the meds and order tab to cancel old and order new medications. It also includes dialog elements for future lab orders to monitor liver function and lipid levels.

> Order LFTs today (if not available w/in past year). Order LFTs in 60 days after starting therapy.

> Order fasting Lipid Profile in 60 days.

3.  Alternatively, use the Reminder Dialog options to copy the national dialog, dialog elements, and dialog groups to make local changes.

> If your site has a Lipid Panel and AST/ALT TIU Object, add this TIU Object to the dialog element header text. The TIU Object should include Chol, Trigly, HDL, LDL-C, direct LDL, AST, and ALT values and dates.

> Some sites have clinicians order a consult to a service that corrects unconfirmed diagnoses the clinician finds in a patient's record. If your site has this method in place, copy the reminder

> dialog to a local reminder dialog and then add a local dialog element for the consult order to the reminder dialog so this practice can continue.

> Edit History:

> Baseline Frequency:

> Do In Advance Time Frame: Wait until actually DUE Sex Specific:

> Ignore on N/A:

> Frequency for Age Range: 1 year for all ages Match Text:

> No Match Text:

> Findings:

> Finding Item: IHD DIAGNOSIS (FI(1)=RT(27))

> Finding Type: REMINDER TERM

> Use in Patient Cohort Logic: AND

> Effective Date: OCT 01, 1999

> Use Inactive Problems: N

> Not Found Text: Patient has no IHD Diagnosis on file.

> Finding Item: OUTSIDE LDL \<100 (FI(3)=RT(35))

> Finding Type: REMINDER TERM Match Frequency/Age: 1 year for all ages

> Use in Patient Cohort Logic: AND NOT

> Effective Period: 1Y

> Finding Item: OUTSIDE LDL 100-119 (FI(4)=RT(34))

> Finding Type: REMINDER TERM Match Frequency/Age: 1 year for all ages

> Use in Patient Cohort Logic: AND NOT

> Effective Period: 1Y

> Finding Item: OUTSIDE LDL 120-129 (FI(5)=RT(52))

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: OR

> Effective Period: 1Y

> Finding Item: OUTSIDE LDL \>129 (FI(6)=RT(36))

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: OR

> Effective Period: 1Y

> Finding Item: LDL \>119 (FI(7)=RT(33))

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: OR

> Effective Period: 1Y

> Condition: I V\>119

> Found Text: The most recent lab results document LDL greater than or equal to 120 mg/dl.

> Finding Item: LDL \<120 (FI(8)=RT(57))

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND NOT

> Effective Period: 1Y

> Condition: I (V\<120)&(+V\>0)

> Found Text: The most recent lab results document LDL less than 120 mg/dl.

> Finding Item: LIPID LOWERING THERAPY MGMT - 2M (FI(9)=RT(58))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 2M

> Found Text: Lipid lowering management underway. Reminder satisfied for 2 months.

> Finding Item: LIPID LOWERING THERAPY MGMT - 6M (FI(10)=RT(59))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 6M

> Found Text: Lipid lowering management underway. Reminder satisfied for 6 months.

> Finding Item: REFUSED ELEVATED LDL THERAPY (FI(11)=RT(45))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 6M

> Found Text: Patient refused therapy for elevated LDL.

> Reminder satisfied for 6 months.

> Finding Item: LIPID MEDS CONTRAINDICATED (FI(12)=RT(56))

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Effective Period: 1Y

> Found Text: Lipid lowering medications are contraindicated.

> Reminder satisfied for 1 year.

> Finding Item: UNCONFIRMED IHD DIAGNOSIS (FI(13)=RT(42))

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND NOT

> Finding Item: LIPID LOWERING MEDS (FI(14)=RT(54))

> Finding Type: REMINDER TERM Effective Period: 90D

> Finding Item: TRANSFERASE (AST) (SGOT) (FI(15)=RT(8))

> Finding Type: REMINDER TERM General Patient Cohort Found Text:

> General Patient Cohort Not Found Text:

> General Resolution Found Text:

> General Resolution Not Found Text:

> Customized PATIENT COHORT LOGIC to see if the Reminder applies to a patient: FI(1)&(MRD(FI(1))\>MRD(FI(13)))&(FI(5)!FI(6)!FI(7))&

> (MRD(FI(5),FI(6),FI(7))\>MRD(FI(8),FI(3),FI(4)))

> Expanded Patient Cohort Logic:

> FI(IHD DIAGNOSIS)&(MRD(FI(IHD DIAGNOSIS))\> MRD(FI(UNCONFIRMED IHD DIAGNOSIS)))&(FI(OUTSIDE LDL 120-129)!

> FI(OUTSIDE LDL \>129)!FI(LDL \>119))&(MRD(FI(OUTSIDE LDL 120-129), FI(OUTSIDE LDL \>129),FI(LDL \>119))\>MRD(FI(LDL \<120),FI(OUTSIDE LDL \<100), FI(OUTSIDE LDL 100-119)))

> Default RESOLUTION LOGIC defines findings that resolve the Reminder: FI(9)!FI(10)!FI(11)!FI(12)

> Expanded Resolution Logic:

> FI(LIPID LOWERING THERAPY MGMT - 2M)!FI(LIPID LOWERING THERAPY MGMT - 6M)! FI(REFUSED ELEVATED LDL THERAPY)!FI(LIPID MEDS CONTRAINDICATED)

> Web Sites:

> Web Site URL: <http://www.oqp.med.va.gov/cpg/DL/dl_cpg/algo4frameset.htm>

> Web Site Title: VHA/DoD CPG for Dyslipidemia

> The VHA/DoD CPG for Management of Dyslipidemia is a comprehensive guideline incorporating current information and practices for practitioners throughout the DoD and Veterans Health Administration system. See Section S, Table 3b for reference to LDL\<120 in the Guideline.

#### Appendix B: IHD Dialogs

> VA-IHD LIPID PROFILE

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>REMINDER DIALOG INQUIRY Mar 21, 2002 5:31:49 pm Page 1</p>
<p>NUMBER: 269</p>
<p>DIALOG NAME: VA-IHD LIPID PROFILE</p>
</blockquote>
<p>Type: reminder dialog</p>
<blockquote>
<p>Associated reminder:</p>
<p>Class: NATIONAL</p>
<p>Sponsor: Office of Quality &amp; Performance Review Date:</p>
<p>Edit History:</p>
<p>DIALOG COMPONENTS:</p>
</blockquote>
<p>Sequence: 5</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID PROFILE HEADER</p>
<p>Text:</p>
<p>The VHA/DOD Clinical Practice Guideline for Management of Dyslipidemia recommends that patients with Ischemic Heart Disease have a lipid profile/LDL every one to two years; and that patients taking lipid lowering medications have a lipid profile/LDL at least every year.</p>
<p>Click on the 'Clinical Maint' button below to display IHD diagnosis, lab results and current lipid lowering medications.</p>
</blockquote>
<p>Sequence: 10</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID ORDER GROUP Text:</p>
</blockquote>
<p>Sequence: 20</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID REFUSED</p>
<p>Text: Patient refuses lipid profile testing.</p>
</blockquote>
<p>Sequence: 35</p>
<blockquote>
<p>Element/Group: VA-IHD UNCONFIRMED DIAGNOSIS</p>
</blockquote>
<p>Text:</p>
<blockquote>
<p>Unable to confirm diagnosis of Ischemic Heart Disease. Inactivate IHD reminders.</p>
</blockquote>
<p>Sequence: 15</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID DONE ELSEWHERE GROUP</p>
</blockquote>
<p>Text:</p>
<blockquote>
<p>Sequence: 30 Element/Group: VA-IHD SPACER</p>
<p>Text: &lt;br&gt;</p>
</blockquote>
<p>Sequence: 25</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID OTHER DEFER</p>
<p>Text: Defer lipid profile.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Reminder Dialog: VA-IHD LIPID PROFILE

> IHD Lipid Profile Dialog box 1: This is the way the reminder dialog looks when it is presented to the clinician, with no items selected.

> If your site has a Lipid Panel TIU Object, add this TIU Object to the local dialog element header text. The Lipid Panel TIU Object should include Chol, Trigly, HDL, LDL-C, and direct LDL values and dates.

> Notice the “Click on…” sentence. This allows the reminder to conform to normal CPRS processing, and helps the user get used to using the Clinical Maint button on the screen.

![](pxrm-1-5-8-ihd-queri-installation-guide/011.png)

#### IHD Lipid Profile Dialog box 2:

> All items are selected in the dialog to show how the dialogs expand to collect pertinent clinical data.

> The “Defer lipid profile testing” item requires a comment.

![](pxrm-1-5-8-ihd-queri-installation-guide/012.png)

#### Clinical Maintenance Box

> The Clinical Maintenance displays IHD Diagnosis, LDL lab results, lipid lowering medications, and other findings found by the reminder evaluation.

![](pxrm-1-5-8-ihd-queri-installation-guide/013.png)

#### VA-IHD ELEVATED LDL

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>REMINDER DIALOG INQUIRY Mar 21, 2002 5:32:28 pm Page 1</p>
<p>NUMBER: 389</p>
<p>DIALOG NAME: VA-IHD ELEVATED LDL</p>
<p>Type: reminder dialog</p>
</blockquote>
<p>Associated reminder:</p>
<p>Class: NATIONAL</p>
<blockquote>
<p>Sponsor: Review Date:</p>
<p>Edit History:</p>
<p>DIALOG COMPONENTS:</p>
<p>Sequence: 45</p>
<p>Element/Group: VA-IHD LIPID/ALT/AST ORDER GROUP Text:</p>
<p>Sequence: 5</p>
</blockquote>
<p>Element/Group: VA-IHD ELEVATED LDL HEADER</p>
<blockquote>
<p>Text:</p>
<p>The VHA/DOD Clinical Practice Guideline for Management of Dyslipidemia recommends an LDL goal of &lt;120 mg/dl for patients with Ischemic Heart Disease; and the NCEP Adult Treatment Panel II recommends a more stringent goal of &lt;100 mg/dl. Consider initiating or adjusting lipid lowering treatment.</p>
<p>Click on 'Clinical Maint' button below to display IHD Diagnosis, LDL lab result s and current lipid lowering medications.</p>
<p>Sequence: 65</p>
<p>Element/Group: VA-IHD UNCONFIRMED DIAGNOSIS</p>
</blockquote>
<p>Text:</p>
<blockquote>
<p>Unable to confirm diagnosis of Ischemic Heart Disease. Inactivate IHD reminders.</p>
</blockquote>
<p>Sequence: 55</p>
<blockquote>
<p>Element/Group: VA-IHD ELEVATED LDL OTHER DEFER</p>
<p>Text: Defer lipid lowering medications.</p>
</blockquote>
<p>Sequence: 10</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID LOWER AGENT ORDER GROU</p>
<p>Text:</p>
<p>Sequence: 15</p>
<p>Element/Group: VA-IHD LIPID LOWER AGENT ADJUST GRO</p>
<p>Text:</p>
</blockquote>
<p>Sequence: 30</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID LOWER AGENT ELSEWHERE</p>
<p>Text:</p>
<p>Lipid lowering management provided by another VA or non-VA facility.</p>
</blockquote>
<p>Sequence: 40</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID DONE ELSEWHERE &lt;120 GR</p>
<p>Text:</p>
<p>Sequence: 35</p>
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
<p>Element/Group: VA-IHD SPACER Text: &lt;br&gt;</p>
<p>Sequence: 60 Element/Group: VA-IHD SPACER</p>
<p>Text: &lt;br&gt;</p>
</blockquote>
<p>Sequence: 20</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID TREATMENT NO CHANGE</p>
</blockquote>
<p>Text:</p>
<blockquote>
<p>No lipid treatment change is needed based on patient's current status.</p>
</blockquote>
<p>Sequence: 25</p>
<blockquote>
<p>Element/Group: VA-IHD LIPID MEDS CONTRAINDICATED</p>
<p>Text: Lipid lowering medications are contraindicated.</p>
</blockquote>
<p>Sequence: 50</p>
<blockquote>
<p>Element/Group: VA-IHD ELEVATED LDL REFUSED</p>
<p>Text: Patient refuses lipid lowering therapy.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Reminder Dialog: VA-IHD ELEVATED LDL

> IHD Elevated LDL box 1: This is the way the reminder dialog looks when it is presented to the clinician, with nothing selected.

> If your site has a Lipid Panel and AST/ALT TIU Object, add this TIU Object to the local dialog element header text. The TIU Object should include Chol, Trigly, HDL, LDL-C, Direct LDL, AST, and ALT values and dates.

> Notice the “Click on…”' sentence. This allows the reminder to conform to normal CPRS processing, and helps the user get used to using the Clinical Maint button on the screen.

![](pxrm-1-5-8-ihd-queri-installation-guide/014.png)

#### IHD Elevated LDL Dialog Box 2:

> This dialog shows expansion of the first dialog item “Order initial lipid lowering medications,” which includes initial medication and lab test orders that the clinician may want to order for managing elevated lipid results. This group will be based on local order dialogs defined by the sites. Your site’s text could be different from the orders below. Quick orders should be added to the dialog elements.

![](pxrm-1-5-8-ihd-queri-installation-guide/015.png)

#### IHD Elevated LDL Dialog Box 3:

> This dialog shows the expansion of the next four dialog items. The “Adjust lipid lowering medications” item gives clinicians a message to remind them to use the meds tab to stop the current lipid agent and order a new lipid agent. Lab test orders that the clinician may want to order for managing elevated lipid results are available from this dialog group. Quick orders should be added to the dialog elements.

> The “No lipid treatment change” and “contraindication” items require a comment.

![](pxrm-1-5-8-ihd-queri-installation-guide/016.png)

#### IHD Elevated LDL Dialog Box 4:

> This dialog shows the expansion of the remaining dialog items.

> The dialog elements that show up under the 'Order lipid profile or LFTs' dialog group need to be changed to include the order dialog entries for the lab specified, or replaced with local dialog elements. Alternatively, sites could remove the dialog elements and replace them with an order dialog menu.

> 'Defer lipid treatment' is where sites can add items such as “Life Expectancy \< 1 year,” or “Life Expectancy \< 6 months” that they may be collecting.

> The “Defer lipid lowering medications” item requires a comment.

![](pxrm-1-5-8-ihd-queri-installation-guide/017.png)

> ![](pxrm-1-5-8-ihd-queri-installation-guide/018.png)

#### Appendix C: IHD Reminder Term Descriptions

> ALANINE AMINO (ALT) (SGPT)

> Class: NATIONAL

> Date Created: MAY 21,2000

> Sponsor: INFECTIOUS DISEASES PROGRAM OFFICE, VAHQ

> Review Date:

> Description: This term represents serum glutamic-pyruvic transaminase or ALT laboratory tests. Enter the finding items from the Laboratory Test file (#60) that represent the SGPT test.

> National terms related to this term.

> WKLD CODE file (#64): The national lab test term is Transferase Alanine Amino SGPT.

> CPT File (#81) procedure:

> CPT code: 84460 SHORT NAME: ALANINE AMINO (ALT) (SGPT) CPT CATEGORY: CHEMISTRY SOURCE: CPT EFFECTIVE DATE: JUN 01, 1994 STATUS: ACTIVE DESCRIPTION: TRANSFERASE;

> DESCRIPTION: ALANINE AMINO (ALT) (SGPT)

> Lexicon: The CPT code is in the Lexicon term as a Laboratory Procedure term.

> Findings:

> IHD DIAGNOSIS

> Class: NATIONAL

> Date Created: JUL 23,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This term represents patients diagnosed with Ischemic Heart Disease (IHD).

> This term is distributed pre-mapped to the VA-ISCHEMIC HEART DISEASE taxonomy. The Active Problem list, Inpatient Primary Diagnosis and Outpatient Encounter Diagnosis are used to search for IHD ICD9 diagnoses.

> Findings: VA-ISCHEMIC HEART DISEASE (FI(1)=TX(14))

> LDL

> Class: NATIONAL

> Date Created: OCT 7,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This national reminder term represents direct and calculated LDL tests. Add local lab test names used for direct LDL and calculated LDL tests in the findings multiple.

> Findings:

> LDL \<120

> Class: NATIONAL

> Date Created: NOV 28,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This national reminder term represents laboratory package test results where the LDL result is less than 120 mg/dl. Add the CONDITION (e.g., I (V\<120)&(+\>0) to the reminder term CONDITION field for each finding you add.

> Findings:

> LDL \>119

Class: NATIONAL

> Date Created: NOV 28,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This national reminder term represents laboratory package test results where the LDL result is greater than or equal to 120 mg/dl. Add the CONDITION (e.g., I V\>119) to the reminder term CONDITION field for each finding you add.

> Findings:

LIPID LOWERING MEDS

Class: NATIONAL

> Date Created: OCT 7,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This national reminder term represents lipid lowering medications. It is distributed with VA GENERIC entries. If there are local investigation medications for lipid lowering therapy in your site’s formulary that are not mapped to the VA GENERIC drugs, they should be entered as findings for this reminder term.

> Findings: CERIVASTATIN (FI(1)=DG(3505)) FLUVASTATIN (FI(2)=DG(3184)) ATORVASTATIN (FI(3)=DG(3382)) LOVASTATIN (FI(4)=DG(2116)) PRAVASTATIN (FI(5)=DG(2689)) SIMVASTATIN (FI(6)=DG(2708)) COLESTIPOL (FI(7)=DG(406)) CHOLESTYRAMINE (FI(8)=DG(1160)) COLESEVELAM (FI(9)=DG(3662)) FENOFIBRATE (FI(10)=DG(3489)) GEMFIBROZIL (FI(11)=DG(968)) CLOFIBRATE (FI(12)=DG(795)) NIACIN (FI(13)=DG(1080))

> LIPID LOWERING THERAPY MGMT - 2M

Class: NATIONAL

> Date Created: JAN 17,2002

> Sponsor: Office of Quality & Performance Review Date:

> Description: This reminder term represents clinicians’ actions to manage lipid lowering therapy which require follow-up in 2 months. This is not based on orders or current medications. The actions will, most likely, be represented by health factors. Do not add orders or pharmacy medications as findings for this term.

> The LIPID LOWERING MEDS INITIAL ORDER health factor is distributed pre-mapped to this term. This health factor represents the clinician's action taken to order initial levels of lipid lowering agent medications. This health factor is added to the patient's record from the CPRS GUI reminder dialog.

> The LIPID LOWERING MEDS ADJUSTED health factor is distributed pre-mapped to this term. This health factor represents the clinician's action taken to adjust the current lipid lowering agent medications. This health factor is added to the patient's record from the CPRS GUI reminder dialog.

> Findings: LIPID LOWERING MEDS INITIAL ORDER (FI(1)=HF(660078)) LIPID LOWERING MEDS ADJUSTED (FI(2)=HF(660079))

> LIPID LOWERING THERAPY MGMT - 6M

> Class: NATIONAL

> Date Created: JAN 17,2002

> Sponsor: Office of Quality & Performance Review Date:

> Description: This reminder term represents clinician's actions to manage lipid lowering therapy which require follow-up in 6 months.

> Do not add orders or pharmacy medications as findings for this term.

> The NO CHANGE IN IHD LIPID TREATMENT health factor is distributed pre-mapped to this term. This health factor may be used to represent the clinician's decision to continue with the current IHD LIPID Treatment.

> The OTHER DEFER ELEVATED LDL THERAPY health factor is distributed pre-mapped to this term. This health factor may be used to represent reasons why an intervention for elevated LDL therapy is being deferred.

> The LIPID MGMT PROVIDED OUTSIDE health factor is distributed pre-mapped to this term. This health factor may be used to indicate the patient is receiving medications from outside the VA, or having lipid management provided outside the VA.

> Add any local health factors, such as life-expectancy \< 6 months, that your site is using that should defer the lipid lowering management.

> Findings: NO CHANGE IN IHD LIPID TREATMENT (FI(1)=HF(660080)) OTHER DEFER ELEVATED LDL THERAPY (FI(2)=HF(84))

> LIPID MGMT PROVIDED OUTSIDE (FI(3)=HF(660082))

> LIPID MEDS CONTRAINDICATED

> Class: NATIONAL

> Date Created: OCT 17,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description:

> Findings: LIPID MEDS CONTRAINDICATED (FI(1)=HF(660081))

> LIPID PROFILE ORDERABLE

> Class: NATIONAL

> Date Created: DEC 24,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: Enter orderable items for lipid panels that include LDL tests (calculated LDL and direct LDL). The orderable items are informational findings for this reminder. The order will not resolve the reminder, but it will display in the clinical maintenance. Ideally, the clinician will look at the clinical maintenance display to avoid entering duplicate orders. This reminder term is not used in the resolution logic since the future order could be for a long distance in the future. (Copy this reminder and add LIPID PROFILE ORDERABLE to the resolution findings if you want the next due date to be calculated based on the future date the order is to be done.)

> Findings:

> ORDER LIPID PROFILE HEALTH FACTOR

> Class: NATIONAL

> Date Created: JAN 31,2002

> Sponsor: Office of Quality & Performance Review Date:

> Description: Use the health factor distributed with this term or add any local health factor representing the order action. Do not add orderable items to this reminder term (see LIPID PROFILE ORDERABLE). This represents the date the

> order was placed, not the date the order will be done in the future. The order placement will cause the reminder to be resolved for 1 month. (Alternatively, copy this reminder and add LIPID PROFILE ORDERABLE to the resolution findings if you want the next due date to be calculated based on the future date the order is to be done.)

> Findings: ORDER LIPID PROFILE (FI(1)=HF(660070))

> OTHER DEFER LIPID PROFILE

> Class: NATIONAL

> Date Created: OCT 22,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This reminder term is used to represent reasons why the lipid profile test is being deferred. A health factor is distributed pre-mapped to this term. Add any local health factors, such as life-expectancy \< 3 months, that your site is using that should defer the lipid profile test.

> Findings: OTHER DEFER LIPID PROFILE (FI(1)=HF(83))

OUTSIDE LDL 100-119

Class: NATIONAL

> Date Created: SEP 10,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This national reminder term represents LDL results reported by the patient or outside facility where the result is between 100 and 129. This reminder was originally created for use with the VA-IHD Lipid Profile reminder.

> Findings: OUTSIDE LDL 100-119 (FI(1)=HF(79))

OUTSIDE LDL 120-129

Class: NATIONAL

> Date Created: SEP 25,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This term represents patient reported LDL results between 120-129. Findings: OUTSIDE LDL 120-129 (FI(1)=HF(80))

> OUTSIDE LDL \<100

> Class: NATIONAL

> Date Created: NOV 13,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This national reminder term represents LDL results reported by the patient or outside facility where the result is less than 100. This reminder was originally created for use with the VA-IHD Lipid Profile reminder.

> Findings: OUTSIDE LDL \<100 (FI(1)=HF(81))

> OUTSIDE LDL \>129

> Class: NATIONAL

> Date Created: NOV 13,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This national reminder term represents LDL results reported by the patient or outside facility where the result is greater than 129. This reminder was originally created for use with the VA-IHD Lipid Profile reminder.

> Findings: OUTSIDE LDL \>129 (FI(1)=HF(82))

> REFUSED ELEVATED LDL THERAPY

> Class: NATIONAL

> Date Created: OCT 22,2001

> Sponsor: Office of Quality & Performance

> Review Date:

> Description: This term represents the patients refusal to obtain therapy for the elevated LDL. The REFUSED ELEVATED LDL THERAPY health factor is pre-mapped to this reminder term upon distribution. Add local health factors your site may be using to represent this term.

> Findings: REFUSED ELEVATED LDL THERAPY (FI(1)=HF(660083))

REFUSED LIPID PROFILE

Class: NATIONAL

> Date Created: OCT 22,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This reminder term is used to represent the patient’s refusal to have a lipid profile test done. A REFUSED LIPID PROFILE health factor is distributed pre-mapped to this reminder term. Add any local health factors your site is using to represent this term.

> Findings: REFUSED LIPID PROFILE (FI(1)=HF(85))

> TRANSFERASE (AST) (SGOT)

Class: NATIONAL

> Date Created: MAY 21,2000

> Sponsor: INFECTIOUS DISEASES PROGRAM OFFICE, VAHQ

> Review Date:

> Description: This term represents serum glutamic-oxaloacetic transaminase or AST laboratory procedures. Enter the finding items from the Laboratory Test file (#60) that represent this procedure.

> National terms related to this term.

> WKLD CODE file (#64): The national lab test term is Transferase Aspartate SGOT

> CPT File (#81) procedure:

> CPT CODE: 84450 SHORT NAME: TRANSFERASE (AST) (SGOT) CPT CATEGORY: CHEMISTRY SOURCE: CPT

> EFFECTIVE DATE: JUN 01, 1994 STATUS: ACTIVE DESCRIPTION: TRANSFERASE;

> DESCRIPTION: ASPARTATE AMINO (AST) (SGOT)

> Lexicon: The CPT code is in the Lexicon term as a Laboratory Procedure term.

> Findings:

> UNCONFIRMED IHD DIAGNOSIS

> Class: NATIONAL

> Date Created: OCT 17,2001

> Sponsor: Office of Quality & Performance Review Date:

> Description: This reminder term is used to represent an unconfirmed diagnosis of Ischemic Heart Disease on file. The patients' medical record needs to have the IHD diagnosis removed from its source (PCE, PTF, or Problem List). The UNCONFIRMED IHD DIAGNOSIS health factor is pre-mapped to this reminder term upon distribution. Add local health factors your site may be using to represent this term.

> Findings: UNCONFIRMED IHD DIAGNOSIS (FI(1)=HF(660085))

#### Appendix D: IHD Reminder Taxonomies

> NUMBER: 14

> VA-ISCHEMIC HEART DISEASE

> Brief Description:

> Ischemic Heart Disease Diagnoses

> Class:

> Sponsor:

> Review Date:

> Patient Data Source: INPR,EN,PL

> Use Inactive Problems: ICD9 Codes:

> Range 410.0-410.92

> NATIONAL

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Code</p>
</blockquote></th>
<th><blockquote>
<p>ICD Diagnosis</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.0</p>
</blockquote></td>
<td><blockquote>
<p>AMI ANTEROLATERAL WALL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.00</p>
</blockquote></td>
<td><blockquote>
<p>AMI ANTEROLATERAL, UNSPEC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.01</p>
</blockquote></td>
<td><blockquote>
<p>AMI ANTEROLATERAL, INIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.02</p>
</blockquote></td>
<td><blockquote>
<p>AMI ANTEROLATERAL, SUBSEQ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.1</p>
</blockquote></td>
<td><blockquote>
<p>AMI ANTERIOR WALL NEC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.10</p>
</blockquote></td>
<td><blockquote>
<p>AMI ANTERIOR WALL, UNSPEC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.11</p>
</blockquote></td>
<td><blockquote>
<p>AMI ANTERIOR WALL, INIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.12</p>
</blockquote></td>
<td><blockquote>
<p>AMI ANTERIOR WALL, SUBSEQ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.2</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFEROLATERAL WALL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.20</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFEROLATERAL, UNSPEC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.21</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFEROLATERAL, INIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.22</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFEROLATERAL, SUBSEQ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.3</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFEROPOSTERIOR WALL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.30</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFEROPOST, UNSPEC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.31</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFEROPOST, INITIAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.32</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFEROPOST, SUBSEQ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.4</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFERIOR WALL NEC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.40</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFERIOR WALL, UNSPEC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.41</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFERIOR WALL, INIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.42</p>
</blockquote></td>
<td><blockquote>
<p>AMI INFERIOR WALL, SUBSEQ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.5</p>
</blockquote></td>
<td><blockquote>
<p>AMI LATERAL WALL NEC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.50</p>
</blockquote></td>
<td><blockquote>
<p>AMI LATERAL NEC, UNSPEC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.51</p>
</blockquote></td>
<td><blockquote>
<p>AMI LATERAL NEC, INITIAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.52</p>
</blockquote></td>
<td><blockquote>
<p>AMI LATERAL NEC, SUBSEQ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.6</p>
</blockquote></td>
<td><blockquote>
<p>TRUE POSTERIOR INFARCT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.60</p>
</blockquote></td>
<td><blockquote>
<p>TRUE POST INFARCT, UNSPEC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.61</p>
</blockquote></td>
<td><blockquote>
<p>TRUE POST INFARCT, INIT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.62</p>
</blockquote></td>
<td><blockquote>
<p>TRUE POST INFARCT, SUBSEQ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.7</p>
</blockquote></td>
<td><blockquote>
<p>SUBENDOCARDIAL INFARCT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.70</p>
</blockquote></td>
<td><blockquote>
<p>SUBENDO INFARCT, UNSPEC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.71</p>
</blockquote></td>
<td><blockquote>
<p>SUBENDO INFARCT, INITIAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.72</p>
</blockquote></td>
<td><blockquote>
<p>SUBENDO INFARCT, SUBSEQ</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.8</p>
</blockquote></td>
<td><blockquote>
<p>MYOCARDIAL INFARCT NEC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.80</p>
</blockquote></td>
<td><blockquote>
<p>AMI NEC, UNSPECIFIED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.81</p>
</blockquote></td>
<td><blockquote>
<p>AMI NEC, INITIAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.82</p>
</blockquote></td>
<td><blockquote>
<p>AMI NEC, SUBSEQUENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.9</p>
</blockquote></td>
<td><blockquote>
<p>MYOCARDIAL INFARCT NOS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.90</p>
</blockquote></td>
<td><blockquote>
<p>AMI NOS, UNSPECIFIED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>410.91</p>
</blockquote></td>
<td><blockquote>
<p>AMI NOS, INITIAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>410.92</p>
</blockquote></td>
<td><blockquote>
<p>AMI NOS, SUBSEQUENT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Range 411.0-411.89

> Code ICD Diagnosis

1.  POST MI SYNDROME
2.  INTERMED CORONARY SYND

> 411.8 AC ISCHEMIC HRT DIS NEC

> 411.81 AC ISCH HRT DIS W/O MI

> 411.89 AC ISCHEMIC HRT DIS NEC

> Range 412.-412.

> Code ICD Diagnosis

> 412\. OLD MYOCARDIAL INFARCT Range 414.0-414.9

> Code ICD Diagnosis

| 414.0  | CORONARY ATHEROSCLEROSIS       |
|--------|--------------------------------|
| 414.00 | COR ATHEROSCL UNSP TYP-VES     |
| 414.01 | COR ATHEROSCL NATV C VSL       |
| 414.02 | COR ATHEROSCL AUTOL V BYP      |
| 414.03 | COR ATHEROSCL NONAUTO BIO BYP  |
| 414.04 | CORONARY ATHER/ART BYP GRFT    |
| 414.05 | CORONARY ATHER/UNSP TYP BYP GR |
| 414.10 | ANEURYSM, HEART (WALL)         |
| 414.11 | CORONARY VESSEL ANEURYSM       |
| 414.19 | ANEURYSM OF HEART NEC          |
| 414.8  | CHR ISCHEMIC HRT DIS NEC       |
| 414.9  | CHR ISCHEMIC HRT DIS NOS       |

#### Appendix E: IHD Reminder Health Factors

> Health factors have been grouped by categories, and so the health factor can be used for lipid management beyond the IHD diagnosis, where appropriate (e.g., DM, etc.).

> The following Health Factors are distributed pre-mapped to the Reminder Terms:

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Health Factor Category</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Health Factor</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OUTSIDE LDL</p>
</blockquote></td>
<td>OUTSIDE LDL 100-119</td>
</tr>
<tr class="even">
<td></td>
<td>OUTSIDE LDL 120-129</td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>OUTSIDE LDL &lt;100</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>OUTSIDE LDL &gt;129</p>
</blockquote></td>
</tr>
</tbody>
</table>

> LIPID PROFILE INTERVENTIONS

> ORDER LIPID PROFILE

> REFUSED LIPID PROFILE (This term is already used at some sites, but under a DIABETIC CARE category. We are distributing it NOT tied to a disease type category. We can’t have two health factors for the same thing.)

> OTHER DEFER LIPID PROFILE

> LIPID MED INTERVENTIONS

> LIPID LOWERING MEDS INITIAL ORDER LIPID LOWERING MEDS ADJUSTED

> NO CHANGE IN IHD LIPID TREATMENT LIPID MEDS CONTRAINDICATED

> LIPID MGMT PROVIDED OUTSIDE REFUSED ELEVATED LDL THERAPY OTHER DEFER ELEVATED LDL THERAPY

> UNCONFIRMED DIAGNOSIS

> UNCONFIRMED IHD DIAGNOSIS

> <span id="_TOC_250001" class="anchor"></span>Appendix F: Abbreviated Setup Steps

#### Verify correct installation of the "packed reminders" using the Reminder Definition Inquiry option.

- VA-IHD LIPID PROFILE
- VA-IHD ELEVATED LDL
1.  Using FileMan Inquiry, verify the IHD health factors are on your system:
2.  Using the Term Inquiry option, verify that the appropriate reminder terms are on your system:
3.  Using the Dialog Management option, verify that the VA-IHD LIPID PROFILE and VA-IHD ELEVATED LDL dialogs are installed on your system.

#### Print and review the national IHD reminder definitions.

1.  Map local findings to the national reminder terms.
2.  Run the Reminder Test option after term definition mapping is completed. Review the results of patient data with each of the findings mapped to the term.

> *Option: Reminders Test* on the *Reminder Managers Menu*

#### Use the Reminder Dialog options to either copy the national dialog and then make edits, or make edits to the elements distributed in the national dialog.

3.  Add the reminder dialogs to the CPRS Cover Sheet
4.  Verify that the reminders and dialogs function properly
1.  Run a Reminders Due Report to determine if the IHD Clinical Reminder statuses reported are correct. This report can be displayed at the beginning of the day for patients being seen that day.
2.  Use the Reminder Test option to test the reminders.
3.  Verify that the reminder dialogs function properly

> Exercise point-and-click reminder resolution processing through CPRS GUI. Check that each element posts the correct progress note text, finding item to PCE, and also satisfies the reminder.

#### Appendix G: Modifying Reminders and Dialogs For a More Stringent LDL Level

> If your site prefers to use an LDL level of 100 mg/dl rather than the LDL \<120 distributed with this patch, follow the steps below to change the distributed IHD Reminder definitions and dialogs. Add a local prefix to the reminder terms and dialog elements in place of VA-. Make sure you thoroughly test your changed reminders and dialogs!

> See the following pages for detailed descriptions.

#### Summary of Reminder Definition Change Steps

1.  Copy the LDL \<120 reminder term to OURNAME-LDL \<100 and edit the new term’s condition on lab entries to I +V\<100.
2.  Copy LDL \>119 reminder term to OURNAME-LDL \>99 and edit the new term’s condition on lab entries to I +V\>99.
3.  Copy the reminder definition VA-IHD ELEVATED LDL to a local reminder definition – for example, OURNAME-IHD ELEVATED LDL, and then edit the reminder.

> 3a. Change the Reminder definition description text to reflect the \<100 and \>99 changes. 3b. Replace LDL \<120 with OURNAME-LDL \<100. Change the condition to I +V\<100. 3c. Replace LDL \>119 with OURNAME-LDL \>99. Change the condition to I +V\>99.

> 3d. Change the customized patient cohort logic.

4.  Test the new reminder thoroughly, following instructions in the setup section of this manual.

#### Summary of Reminder Dialog Change Steps

1.  Copy the VA-IHD ELEVATED LDL reminder dialog to a local reminder dialog; for example, OURNAME IHD ELEVATED LDL.
2.  Link the local reminder dialog to the OURNAME IHD ELEVATED LDL reminder definition.
3.  Copy/Replace the dialog element for the header: VA-IHD ELEVATED HEADER to OURNAME IHD ELEVATED LDL
4.  Copy VA-IHD LIPID \<100 DONE ELSE dialog element to OURNAME IHD LIPID \<100 DONE ELSE.
5.  Change the Progress Note text in OURNAME IHD LIPID \<100 DONE ELSE to “Patient reports a more recent LDL \<100.”
6.  Delete the VA-IHD LIPID DONE ELSEWHERE \<120 GROUP from the OURNAME IHD ELEVATED LDL reminder dialog.
7.  Add the new element OURNAME IHD LIPID \<100 DONE ELSE to the local reminder dialog where the VA-IHD LIPID DONE ELSEWHERE \<120 used to be.
8.  Test your dialog thoroughly, following instructions given in the setup section of this guide.
9.  If desired, add the dialogs to the CPRS GUI, following instructions given in the setup section of this guide.

#### Detailed Steps for Changing the Reminder Definition

1.  Copy the LDL \<120 reminder term to OURNAME-LDL \<100 and edit the new term’s condition on lab entries to I +V\<100.

> Select Reminder Term Management Option: TC Copy Reminder Term Select the reminder term to copy: LDL \<120 NATIONAL

> ...OK? Yes// \<Enter\> (Yes)

> PLEASE ENTER A UNIQUE NAME: OURNAME-LDL \<100

> The original reminder term LDL \<120 has been copied into OURNAME-LDL \<100. Do you want to edit it now? Y

> NAME: OURNAME-LDL \<100// \<Enter\>

> CLASS: LOCAL// \<Enter\> REVIEW DATE: \<Enter\> DESCRIPTION:

> 1\>This national reminder term represents laboratory package test results 2\>where the LDL result is less than 120 mg/dl. Add the CONDITION

> 3\>(e.g., I V\<120) to the reminder term CONDITION field for each finding you 4\>add.

> EDIT Option: 1

> 1\>This national reminder term represents laboratory package test results Replace national With local Replace \<Enter\>

> 1\>This local reminder term represents laboratory package test results EDIT Option: 2

> 2\>where the LDL result is less than 120 mg/dl. Add the CONDITION Replace 120 With 100 Replace

> where the LDL result is less than 100 mg/dl. Add the CONDITION Edit line: 3

> 3\>(e.g., I V\<120) to the reminder term CONDITION field for each finding you Replace 2 With 0 Replace \<Enter\>

> (e.g., I V\<100) to the reminder term CONDITION field for each finding you Edit line: \<Enter\>

> Select FINDING ITEM: LT.LDL

> Searching for a LABORATORY TEST, (pointed-to by FINDING ITEM) Searching for a LABORATORY TEST

1.  LDL CHOLESTEROL
2.  LDL-CHOL CALCULATION
3.  LDL/HDL RATIO

> CHOOSE 1-3: 1 LDL CHOLESTEROL

> Are you adding 'LDL CHOLESTEROL' as a new FINDINGS (the 1ST for this REMINDER TERM)? No// Y (Yes)

> EFFECTIVE PERIOD: \<Enter\>

> USE INACTIVE PROBLEMS: \<Enter\> WITHIN CATEGORY RANK: \<Enter\> EFFECTIVE DATE: \<Enter\>

> MH SCALE: \<Enter\>

> CONDITION: I (+V\<100)&(+V\>0)

> CONDITION CASE SENSITIVE: RX TYPE: \<Enter\>

> Select FINDING ITEM: \<Enter\>

> Input your edit comments. Edit? NO//\<Enter\>

#### Copy the LDL \>119 reminder term to OURNAME-LDL \>99 and edit the new term’s condition on lab entries to I +V\>99.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Reminder Term Management Option: <strong>TC</strong> Copy Reminder Term</p>
<p>Select the reminder term to copy: <strong>LDL &gt;119</strong> NATIONAL</p>
<p>...OK? Yes// (Yes)</p>
<p>PLEASE ENTER A UNIQUE NAME: <strong>OURNAME-LDL &gt;99</strong></p>
<p>The original reminder term LDL &gt;119 has been copied into OURNAME-LDL &gt;99. Do you want to edit it now? <strong>Y</strong></p>
<p>NAME: OURNAME-LDL &gt;99// <strong>&lt;Enter&gt;</strong></p>
<p>CLASS: LOCAL// <strong>&lt;Enter&gt;</strong> REVIEW DATE: <strong>&lt;Enter&gt;</strong> DESCRIPTION:</p>
<p>1&gt;This national reminder term represents laboratory package test results</p>
<p>2&gt;where the LDL result is greater than or equal to 120 mg/dl. Add the CONDITION 3&gt;(e.g., I V &gt;119) to the reminder term CONDITION field for each finding you 4&gt;add.</p>
<p>EDIT Option: <strong>1</strong></p>
<p>1&gt;This national reminder term represents laboratory package test results Replace <strong>national &lt;Enter&gt;</strong> With <strong>local &lt;Enter&gt;</strong> Replace <strong>&lt;Enter&gt;</strong></p>
<p>1&gt;This local reminder term represents laboratory package test results EDIT Option: 2</p>
<p>2&gt;where the LDL result is greater than or equal to 120 mg/dl. Add the CONDITION Replace <strong>120 &lt;Enter&gt;</strong> With <strong>100 &lt;Enter&gt;</strong> Replace <strong>&lt;Enter&gt;</strong></p>
<p>where the LDL result is less than 99 mg/dl. Add the CONDITION Edit line: 3</p>
<p>3&gt;(e.g., I V &gt;119) to the reminder term CONDITION field for each finding you Replace <strong>11 &lt;Enter&gt;</strong>With <strong>9 &lt;Enter&gt;</strong> Replace <strong>&lt;Enter&gt;</strong></p>
<p>(e.g., I V &gt;99) to the reminder term CONDITION field for each finding you Edit line: <strong>&lt;Enter&gt;</strong></p>
<p>Select FINDING ITEM: LDL CHOLESTEROL// <strong>&lt;Enter&gt;</strong> FINDING ITEM: LDL CHOLESTEROL// <strong>&lt;Enter&gt;</strong> EFFECTIVE PERIOD: <strong>&lt;Enter&gt;</strong></p>
<p>USE INACTIVE PROBLEMS: <strong>&lt;Enter&gt;</strong> WITHIN CATEGORY RANK: <strong>&lt;Enter&gt;</strong> EFFECTIVE DATE: <strong>&lt;Enter&gt;</strong></p>
<p>MH SCALE:</p>
<p>CONDITION: I V&gt;119// <strong>I (+V&gt;99)&amp;(+V&gt;0)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  Copy the reminder definition VA-IHD ELEVATED LDL to a local reminder definition – for example, OURNAME-IHD ELEVATED LDL

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select Reminder Managers Menu Option: <strong>RM</strong> Reminder Definition Management</p>
<p>RL List Reminder Definitions</p>
<p>RI Inquire about Reminder Definition RE Add/Edit Reminder Definition</p>
<p>RC Copy Reminder Definition</p>
<p>RA Activate/Inactivate Reminders</p>
<p>Select Reminder Definition Management Option: <strong>RC</strong> Copy Reminder Definition</p>
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
<p>Select the reminder item to copy: <strong>VA-IHD ELEVATED LDL</strong> NATIONAL PLEASE ENTER A UNIQUE NAME: <strong>OURNAME-IHD ELEVATED LDL</strong></p>
<p>The original reminder VA-IHD ELEVATED LDL has been copied into OURNAME-IHD ELEVATED LDL.</p>
<p>Do you want to edit it now? <strong>Y</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Edit the Reminder Definition.

> 3a. Change the Reminder definition description text to reflect the \<100 and \>99 changes.

> (Modify the highlighted sections as appropriate for your site.)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select one of the following:</p>
<p>Select section to edit: <strong>General</strong></p>
<p>PRINT NAME: IHD Elevated LDL// <strong>&lt;Enter&gt;</strong></p>
<p>CLASS: LOCAL// <strong>&lt;Enter&gt;</strong> SPONSOR: <strong>&lt;Enter&gt;</strong> REVIEW DATE:</p>
<p>USAGE: C// <strong>&lt;Enter&gt;</strong></p>
<p>RELATED REMINDER GUIDELINE: <strong>&lt;Enter&gt;</strong></p>
<p>INACTIVE FLAG: <strong>&lt;Enter&gt;</strong></p>
<p>REMINDER DESCRIPTION:. . .</p>
<p>. . .</p>
<p>21&gt;for 6 months.</p>
<p>22&gt;</p>
<p>23&gt;Documenting that no treatment change is needed based on patient's current 24&gt;clinical status, that lipid management is provided by another VA or non-VA 25&gt;facility, or deferring lipid treatment for other reasons satisfies the 26&gt;reminder for 6 months.</p>
<p>27&gt;</p>
<p>28&gt;Documenting that lipid lowering medications are contraindicated satisfies 29&gt;the reminder for 12 months.</p>
<p>EDIT Option: <strong>L</strong>ist line: 1// to: 29// <strong>&lt;Enter&gt;</strong></p>
<p>1&gt;The VHA/DOD Clinical Practice Guideline for Management of Dyslipidemia</p>
<p>2&gt;recommends an LDL goal of &lt;120 mg/dl for patients with Ischemic Heart</p>
<p>3&gt;Disease; and the NCEP Adult Treatment Panel II recommends a more stringent</p>
<p>4&gt;goal of &lt;100 mg/dl.</p>
<p>5&gt;</p>
<p>6&gt;This national reminder identifies patients with known IHD (i.e., a</p>
<p>7&gt;documented ICD-9 code on or after 10/01/99) who have had a serum</p>
<p>8&gt;lipid panel within the last year, where the most recent LDL lab</p>
<p>9&gt;test (or documented outside LDL) is greater than or equal to 120 mg/dl. 10&gt;If a more recent record of an UNCONFIRMED IHD DIAGNOSIS is found, the 11&gt;reminder will not be applicable to the patient.</p>
<p>12&gt;</p>
<p>13&gt;Documenting an outside LDL &lt;120 mg/dl satisfies the reminder for 12</p>
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
<p>14&gt;months from the lab test date. 15&gt;</p>
<p>16&gt;Ordering initial lipid lowering medications or adjusting current lipid 17&gt;lowering medications satisfies the reminder for 2 months. (This is 18&gt;tracked by Health Factors, not the order.)</p>
<p>19&gt;</p>
<p>20&gt;A patient's refusal of lipid lowering therapy satisfies the reminder 21&gt;for 6 months.</p>
<p>22&gt;</p>
<p>23&gt;Documenting that no treatment change is needed based on patient's current 24&gt;clinical status, that lipid management is provided by another VA or non-VA 25&gt;facility, or deferring lipid treatment for other reasons satisfies the 26&gt;reminder for 6 months.</p>
<p>27&gt;</p>
<p>28&gt;Documenting that lipid lowering medications are contraindicated satisfies 29&gt;the reminder for 12 months.</p>
<p>EDIT Option:</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### 3a. Replace LDL \<120 with OURNAME-LDL \<100. Change the CONDITION to I (+V \<100)&(+V\>0).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select one of the following:</p>
<p>Select section to edit: <strong>Findings</strong></p>
<p>Findings Choose from:</p>
<p>RT IHD DIAGNOSIS</p>
<p>RT LDL &lt;120</p>
<p>RT LDL &gt;119</p>
<p>RT LIPID LOWERING MEDS</p>
<p>RT LIPID LOWERING THERAPY MGMT - 2M RT LIPID LOWERING THERAPY MGMT - 6M RT LIPID MEDS CONTRAINDICATED</p>
<p>RT OUTSIDE LDL 100-119</p>
<p>RT OUTSIDE LDL 120-129</p>
<p>RT OUTSIDE LDL &lt;100</p>
<p>RT OUTSIDE LDL &gt;129</p>
<p>RT REFUSED ELEVATED LDL THERAPY RT TRANSFERASE (AST) (SGOT)</p>
<p>RT UNCONFIRMED IHD DIAGNOSIS Select FINDING: <strong>RT.LDL &lt;120</strong></p>
<p>Searching for a REMINDER TERM, (pointed-to by FINDING ITEM) LDL &lt;100 NATIONAL</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes) FINDING ITEM: LDL &lt;120// <strong>OURNAME-LDL &lt;100</strong></p>
<p>MINIMUM AGE: <strong>&lt;Enter&gt;</strong></p>
<p>MAXIMUM AGE: <strong>&lt;Enter&gt;</strong></p>
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
<p>REMINDER FREQUENCY: <strong>&lt;Enter&gt;</strong></p>
<p>RANK FREQUENCY: <strong>&lt;Enter&gt;</strong></p>
<p>USE IN RESOLUTION LOGIC: <strong>&lt;Enter&gt;</strong></p>
<p>USE IN PATIENT COHORT LOGIC: AND NOT//<strong>&lt;Enter&gt;</strong> EFFECTIVE PERIOD: 1Y// <strong>&lt;Enter&gt;</strong></p>
<p>EFFECTIVE DATE: <strong>&lt;Enter&gt;</strong></p>
<p>CONDITION: I V&lt;120// <strong>I (+V&lt;100)&amp;(+V&gt;0)</strong></p>
<p>CONDITION CASE SENSITIVE:</p>
<p>FOUND TEXT:</p>
<p>1&gt;The most recent lab results document LDL less than 120 mg/dl.</p>
<p>EDIT Option: <strong>1</strong></p>
<p>1&gt;The most recent lab results document LDL less than 120 mg/dl. Replace <strong>120</strong> With <strong>100</strong> Replace <strong>&lt;Enter&gt;</strong></p>
<p>The most recent lab results document LDL less than 100 mg/dl.</p>
<p>Edit line: <strong>&lt;Enter&gt;</strong> EDIT Option: <strong>&lt;Enter&gt;</strong> NOT FOUND TEXT:</p>
<p>1&gt;<strong>&lt;Enter&gt;</strong></p>
<p>Findings</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> 3b. Replace LDL \>119 with OURNAME-LDL \>99. Change the CONDITION to I (+V\>99)&(+\>0)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select one of the following:</p>
<p>Select section to edit: <strong>Findings</strong></p>
<p>Findings Choose from:</p>
<p>RT IHD DIAGNOSIS</p>
<p>RT LDL &gt;119</p>
<p>RT LIPID LOWERING MEDS</p>
<p>RT LIPID LOWERING THERAPY MGMT - 2M RT LIPID LOWERING THERAPY MGMT - 6M RT LIPID MEDS CONTRAINDICATED</p>
<p>RT OURNAME LDL &lt;100</p>
<p>RT OUTSIDE LDL 100-119</p>
<p>RT OUTSIDE LDL 120-129</p>
<p>RT OUTSIDE LDL &lt;100</p>
<p>RT OUTSIDE LDL &gt;129</p>
<p>RT REFUSED ELEVATED LDL THERAPY RT TRANSFERASE (AST) (SGOT)</p>
<p>RT UNCONFIRMED IHD DIAGNOSIS</p>
<p>Select FINDING: <strong>RT.LDL &gt;119</strong></p>
<p>Searching for a REMINDER TERM, (pointed-to by FINDING ITEM) LDL &gt;119 NATIONAL</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>FINDING ITEM: LDL &gt;119// <strong>RT.OURNAME-LDL &gt;99</strong></p>
<p>MINIMUM AGE: <strong>&lt;Enter&gt;</strong> MAXIMUM AGE: <strong>&lt;Enter&gt;</strong> REMINDER FREQUENCY: <strong>&lt;Enter&gt;</strong> RANK FREQUENCY: <strong>&lt;Enter&gt;</strong></p>
<p>USE IN RESOLUTION LOGIC: <strong>&lt;Enter&gt;</strong></p>
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
<p>USE IN PATIENT COHORT LOGIC: OR// <strong>&lt;Enter&gt;</strong></p>
<p>EFFECTIVE PERIOD: 1Y// <strong>&lt;Enter&gt;</strong></p>
<p>EFFECTIVE DATE: <strong>&lt;Enter&gt;</strong></p>
<p>CONDITION: I V&gt;119// <strong>I (+V&gt;99)&amp;(+V&gt;0)</strong></p>
<p>CONDITION CASE SENSITIVE:</p>
<p>FOUND TEXT:</p>
<p>1&gt;The most recent lab results document LDL greater than or equal to 120 2&gt;mg/dl.</p>
<p>EDIT Option: 1</p>
<p>1&gt;The most recent lab results document LDL greater than or equal to 120 Replace 120 With 100 Replace &lt;Enter&gt;</p>
<p>The most recent lab results document LDL greater than or equal to 100 Edit line: <strong>&lt;Enter&gt;</strong></p>
<p>EDIT Option: <strong>&lt;Enter&gt;</strong></p>
<p>NOT FOUND TEXT:</p>
<p>1&gt;<strong>&lt;Enter&gt;</strong></p>
<p>Findings</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> 3d.Change the Customized Cohort Logic.

> While still in Reminder Copy (RC), select the Logic section to edit:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Select one of the following:</p>
<p>Select section to edit: <strong>L</strong></p>
<p>Customized PATIENT COHORT LOGIC to see if the Reminder applies to a patient: FI(1)&amp;(MRD(FI(1))&gt;MRD(FI(13)))&amp;(FI(5)!FI(6)!FI(7))&amp;</p>
<p>(MRD(FI(5),FI(6),FI(7))&gt;MRD(FI(8),FI(3),FI(4)))</p>
<p>Replace <strong>FI(5)&lt;Enter&gt;</strong> With <strong>FI(4)!FI(5) &lt;Enter&gt;</strong> Replace <strong>MRD(FI(5)&lt;Enter&gt;</strong> With</p>
<p><strong>MRD(FI(4),FI(5)&lt;Enter&gt;</strong> Replace <strong>FI(3),FI(4)&lt;Enter&gt;</strong> With <strong>FI(3)&lt;Enter&gt;</strong> Replace <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Edited logic

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Customized PATIENT COHORT LOGIC to see if the Reminder applies to a patient:</p>
<p>FI(1)&amp;(MRD(FI(1))&gt;MRD(FI(13)))&amp;(FI(4)!FI(5)!FI(6)!FI(7))&amp;</p>
<p>(MRD(FI(4),FI(5),FI(6),FI(7))&gt;MRD(FI(8),FI(3)))</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> (If you do a Reminder Inquiry (RI), the text highlighted below in BOLD will be replaced by the logic shown in the After box by the steps taken above.)

#### Before:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Expanded Patient Cohort Logic:</p>
<p>FI(IHD DIAGNOSIS)&amp;(MRD(FI(IHD DIAGNOSIS))&gt; MRD(FI(UNCONFIRMED IHD DIAGNOSIS)))&amp;(FI(OUTSIDE LDL 120-129)!</p>
<p>FI(OUTSIDE LDL &gt;129)!FI(LDL &gt;119))&amp;(MRD(FI(OUTSIDE LDL 120-129), FI(OUTSIDE LDL &gt;129),FI(LDL &gt;119<strong>))&gt;MRD(FI(LDL &lt;120),FI(OUTSIDE LDL &lt;100), FI(OUTSIDE LDL 100-119)))</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> After:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Expanded Patient Cohort Logic:</p>
<p>FI(IHD DIAGNOSIS)&amp;(MRD(FI(IHD DIAGNOSIS))&gt; MRD(FI(UNCONFIRMED IHD DIAGNOSIS)))&amp;(FI(OUTSIDE LDL 100-119)!</p>
<p>FI(OUTSIDE LDL 120-129)!FI(OUTSIDE LDL &gt;129)!FI(OURNAME-LDL &gt;99))&amp; (MRD(FI(OUTSIDE LDL 100-119),FI(OUTSIDE LDL 120-129),FI(OUTSIDE LDL &gt;129),</p>
<p>FI(OURNAME-LDL &gt;99))&gt;MRD(FI(OURNAME-LDL &lt;100),FI(OUTSIDE LDL &lt;100)))</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Test the new reminder thoroughly, following instructions in the setup section of this manual.

> Detailed Steps to Change the Reminder Dialog

1.  Copy the VA-IHD ELEVATED LDL reminder dialog to a local reminder dialog- OURNAME-IHD ELEVATED LDL.

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
<p><strong>Dialog List</strong> May 17, 2002@16:34:43 Page: 1 of 16 REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<p>Item Reminder Name Linked Dialog Name &amp; Dialog Status</p>
</blockquote>
<ol type="1">
<li><p>757 NUR ALCOHOL USE SCREEN 757 ALCOHOL USE SCREEN</p></li>
<li><p>757 NUR SEATBELT &amp; ACCIDENT AVOID 757 SEATBELT AND ACCIDENT A</p></li>
<li><p>A A BLOOD EXPOSURE</p></li>
<li><p>A A PAIN VITAL SIGN VA-PAIN SCREEN AND HX</p></li>
<li><p>A A SG PAIN ASSESSMENT A A PAIN SCREEN AND INTERVE</p></li>
<li><p>A A SG PAIN HISTORY A A SG PAIN HISTORY DIA</p></li>
<li><p>A NEW REMINDER A NEW REMINDER</p></li>
<li><p>AGETEST AGETEST</p></li>
<li><p>ALCOHOL USE SCREEN ALCOHOL USE SCREEN DIALOG</p></li>
<li><p>ANDREW TEST OBJECT ANDREW OBJECT</p></li>
<li><p>ANTHONY TEST OBJECT ZZANTHONY DETAIL VITAL</p></li>
<li><p>ANTRY CHOLESTEROL SCREEN (M) ANTRY CHOLESTEROL SCREEN (M</p></li>
<li><p>ANTRY'S ANNUAL FLU SHOOT ANTRY'S ANNUAL FLU SHOOT</p></li>
<li><p>ANTRY'S DIABETIC REVIEW ANTRY'S DIABETIC REVIEW</p></li>
<li><p>ANTRY'S SMOKE CESSATION ANTRY'S SMOKE CESSATION</p></li>
<li><p>Agetest Agetest Disabled</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>+ Enter ?? for more actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AR All reminders LR Linked Reminders QU Quit CV Change View RN Name/Print Name</p>
<p>Select Item: Next Screen// <strong>SL</strong> SL Search for: <strong>VA-IHD ELEVATED LDL</strong></p>
<p><strong>.</strong></p>
<p><strong>.</strong></p>
<p><strong>.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 67%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog Selection List</strong> May 17, 2002@14:28:53 REMINDER NAME: VA-IHD ELEVATED LDL</p>
</blockquote></th>
<th><blockquote>
<p>Page: 1 of 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Item Dialog Name Latest Update</p>
</blockquote></td>
<td><blockquote>
<p>Linked Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>This reminder is linked to dialog:</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>1 VA-IHD ELEVATED LDL</p>
</blockquote></td>
<td><blockquote>
<p>VA-IHD ELEVATED LDL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>+ Next Screen - Prev Screen ?? More Actions</p>
</blockquote></td>
<td>&gt;&gt;&gt;</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AD Autogenerate Dialog QU Quit LR Link Reminder</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Select Item: Quit// <strong>1</strong></p>
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
<p><strong>Dialog Edit List</strong> May 17, 2002@14:29:04 Page: 1 of 5</p>
<p>REMINDER DIALOG NAME: VA-IHD ELEVATED LDL [NATIONAL]</p>
<p>Item Seq. Dialog Details/Findings Type</p>
</blockquote>
<ol type="1">
<li><p>5 VA-IHD ELEVATED LDL HEADER element Finding: *NONE*</p></li>
<li><p>10 VA-IHD LIPID LOWER AGENT ORDER GROUP group Finding: LIPID LOWERING MEDS INITIAL ORDER (HEALTH FACTOR)</p></li>
<li><blockquote>
<p>10.5 VA-IHD SIMVASTATIN ORDERED element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>10.10 VA-IHD ORDER BASELINE LFTS TODAY element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>10.15 VA-IHD ORDER FUTURE LFTS 60 DAYS element Finding: *NONE*</p>
</blockquote></li>
<li><blockquote>
<p>10.20 VA-IHD ORDER FUTURE LIPID PROFILE 60 DAYS element Finding: *NONE*</p>
</blockquote></li>
<li><p>15 VA-IHD LIPID LOWER AGENT ADJUST GROUP group Finding: LIPID LOWERING MEDS ADJUSTED (HEALTH FACTOR)</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>+ Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CO Copy Dialog DT Dialog Text RI Reminder Inquiry DD Detailed Display ED Edit/Delete Dialog QU Quit</p>
<p>DP Progress Note Text INQ Inquiry/Print Select Item: Next Screen// <strong>co</strong> Copy Dialog</p>
<p>COPY REMINDER DIALOG 'VA-IHD ELEVATED LDL' Y// <strong>&lt;Enter&gt;</strong> ES ENTER A UNIQUE NAME: <strong>OURNAME-IHD ELEVATED LDL</strong></p>
<p>Completed copy of 'VA-IHD ELEVATED LDL' into 'OURNAME-ELEVATED LDL'</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  Link the local reminder dialog to the OURNAME-IHD ELEVATED LDL reminder definition.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog Selection List</strong> May 17, 2002@11:34:04 Page: 1 of 1</p>
<p>REMINDER NAME: OURNAME-ELEVATED LDL</p>
<p>Item Dialog Name Latest Update Linked Reminders</p>
<p>* NO DIALOGS DEFINED *</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>+ Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</td>
</tr>
<tr class="even">
<td><blockquote>
<p>AD Autogenerate Dialog QU Quit LR Link Reminder</p>
<p>Select Item: Quit// <strong>lr</strong> Link Reminder REMINDER NAME: OURNAME-IHD ELEVATED LDL</p>
<p>LINKED REMINDER DIALOG: <strong>OURNAME-IHD ELEVATED LDL</strong> reminder dialog LOCAL</p>
<p>...OK? Yes// <strong>&lt;Enter&gt;</strong> (Yes)</p>
<p><strong>Dialog Selection List</strong> May 17, 2002@11:34:14 Page: 1 of 1</p>
<p>REMINDER NAME: OURNAME-IHD ELEVATED LDL</p>
<p>Item Dialog Name Latest Update Linked Reminders This reminder is linked to dialog:</p>
<p>1 OURNAME-IHD ELEVATED LDL OURNAME-IHD ELEVATED LDL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>+ Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</td>
</tr>
<tr class="even">
<td><blockquote>
<p>AD Autogenerate Dialog QU Quit LR Link Reminder</p>
<p>Select Item: Quit//</p>
</blockquote></td>
</tr>
</tbody>
</table>

3.  Copy/Replace the dialog element for the header: VA-IHD ELEVATED HEADER to OURNAME-IHD ELEVATED LDL

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 53%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Dialog Edit List</strong> May 17, 2002@14:29:37 REMINDER DIALOG NAME: OURNAME-IHD ELEVATED LDL</p>
</blockquote></th>
<th><blockquote>
<p>Page:</p>
</blockquote></th>
<th><blockquote>
<p>1 of</p>
</blockquote></th>
<th>5</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Sequence 5</p>
</blockquote></td>
<td><blockquote>
<p>Dialog Details</p>
<p>Dialog element: VA-IHD ELEVATED LDL HEADER</p>
</blockquote></td>
<td></td>
<td colspan="2"><blockquote>
<p>Disabled</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Dialog group: VA-IHD LIPID LOWER AGENT ORDER GROUP</p>
<p>Dialog elements: 5 VA-IHD SIMVASTATIN ORDERED</p>
<p>10 VA-IHD ORDER BASELINE LFTS TODA</p>
<p>15 VA-IHD ORDER FUTURE LFTS 60 DAY</p>
<p>20 VA-IHD ORDER FUTURE LIPID PROFI</p>
</blockquote></td>
<td><blockquote>
<p>Y S</p>
<p>LE 60 DA</p>
</blockquote></td>
<td>YS</td>
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
<p>15 Dialog group: VA-IHD LIPID LOWER AGENT ADJUST GROUP Dialog elements: 2 PXRM COMMENT</p>
<p>5 VA-IHD LIPID LOWER AGENT ADJUST TEXT</p>
<p>10 VA-IHD ORDER BASELINE LFTS TODAY</p>
<p>15 VA-IHD ORDER FUTURE LFTS 60 DAYS</p>
<p>20 VA-IHD ORDER FUTURE LIPID PROFILE 60 DAYS</p>
<p>20 Dialog element: VA-IHD LIPID TREATMENT NO CHANGE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>+ Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CO Copy Dialog DT Dialog Text RI Reminder Inquiry DD Detailed Display ED Edit/Delete Dialog QU Quit</p>
<p>DP Progress Note Text INQ Inquiry/Print Select Sequence: Next Screen// <strong>5</strong></p>
<p>CURRENT DIALOG ELEMENT NAME: VA-IHD ELEVATED LDL HEADER</p>
<p>Select one of the following: E Edit</p>
</blockquote>
<ol start="3" type="A">
<li><p>Copy and Replace current element</p></li>
<li><p>Delete element from this dialog</p></li>
</ol>
<blockquote>
<p>Select Dialog Element Action: E// <strong>C</strong>opy and Replace current element</p>
<p>COPY AND REPLACE 'VA-IHD ELEVATED LDL HEADER' Y//<strong>&lt;Enter&gt;</strong> ES ENTER A UNIQUE NAME: VA-IHD ELEVATED LDL HEADER (1)</p>
<p>Replace <strong>VA-IHD</strong> With <strong>OURNAME-IHD</strong></p>
<p>Replace <strong>&lt;Enter&gt;</strong></p>
<p>OURNAME-IHD ELEVATED LDL HEADER (1)</p>
<p>Completed copy of 'VA-IHD ELEVATED LDL HEADER' into 'OURNAME-IHD ELEVATED LDL HEADER (1)'</p>
<p>Replaced element'VA-IHD ELEVATED LDL HEADER' with ' OURNAME-IHD ELEVATED LDL HEADER (1)'</p>
<p>on this dialog.</p>
<p>Do you want to edit now Y// <strong>&lt;Enter&gt;</strong> ES Dialog Element Type: E// <strong>&lt;Enter&gt;</strong> lement</p>
<p>CURRENT DIALOG ELEMENT/GROUP NAME: OURNAME-IHD ELEVATED LDL HEADER (1)</p>
<p>Used by: OURNAME-IHD ELEVATED LDL (Current Reminder Dialog)</p>
<p>NAME: OURNAME -IHD ELEVATED LDL HEADER (1) Replace <strong>&lt;Enter&gt;</strong></p>
<p>DISABLE: <strong>&lt;Enter&gt;</strong> CLASS: LOCAL// <strong>&lt;Enter&gt;</strong> SPONSOR: <strong>&lt;Enter&gt;</strong> REVIEW DATE: <strong>&lt;Enter&gt;</strong></p>
<p>RESOLUTION TYPE: <strong>&lt;Enter&gt;</strong> ORDERABLE ITEM: <strong>&lt;Enter&gt;</strong> FINDING ITEM: <strong>&lt;Enter&gt;</strong> DIALOG/PROGRESS NOTE TEXT:</p>
<p>The VHA/DOD Clinical Practice Guideline for Management of Dyslipidemia recommends an LDL goal of &lt;120 mg/dl for patients with Ischemic Heart Disease; and the NCEP Adult Treatment Panel II recommends a more stringent goal of &lt;100 mg/dl. Consider initiating or adjusting lipid lowering treatment.</p>
<p>Click on 'Clinical Maint' button below to display IHD Diagnosis, LDL lab results and current lipid lowering medications.</p>
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
<p>Edit? NO// <strong>&lt;Enter&gt;</strong></p>
<p>ALTERNATE PROGRESS NOTE TEXT:</p>
<p>No existing text Edit? NO// <strong>&lt;Enter&gt;</strong></p>
<p>EXCLUDE FROM PROGRESS NOTE: <strong>&lt;Enter&gt;</strong></p>
<p>SUPPRESS CHECKBOX: SUPPRESS// <strong>&lt;Enter&gt;</strong></p>
<p>Input your edit comments. Edit? NO//<strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  Copy the VA-IHD LIPID \<100 DONE ELSE dialog element to OURNAME-IHD LIPID \<100 DONE ELSE.

> NOTE: You’ll need to Change View (CV) to Dialog Elements.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog List</strong> May 17, 2002@17:38:07 Page: 11 of 12 DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)</p>
<p>+Item Reminder Dialog Name Source Reminder Status</p>
</blockquote>
<ol start="169" type="1">
<li><p>VA-IHD ELEVATED LDL *NONE* Linked</p></li>
<li><p>VA-IHD LIPID PROFILE *NONE* Linked</p></li>
<li><p>VA-INFLUENZA VACCINE VA-INFLUENZA VACCINE Disabled</p></li>
<li><p>VA-MST SCREENING *NONE* Linked</p></li>
<li><p>VA-PAIN SCREEN AND HX *NONE* Linked</p></li>
<li><p>VA-PNEUMOVAX VA-PNEUMOVAX Linked</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>+ Enter ?? for more actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AD Add Reminder Dialog PT List/Print All QU Quit CV Change View RN Name/Print Name</p>
<p>Select Item: Next Screen// <strong>CV</strong> Change View</p>
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
<p>RG Result Group (Mental Health)</p>
<p>RE Result Element (Mental Health) TYPE OF VIEW: R// <strong>E</strong> Dialog Elements</p>
<p><strong>Dialog List</strong> May 17, 2002@14:35:03 Page: 6 of 8</p>
<p>DIALOG VIEW (DIALOG ELEMENTS)</p>
<p>+Item Dialog Name Dialog type Status</p>
</blockquote>
<ol start="94" type="1">
<li><p>VA-IHD ELEVATED LDL HEADER Dialog Element</p></li>
<li><p>VA-IHD ELEVATED LDL OTHER DEFER Dialog Element</p></li>
<li><p>VA-IHD ELEVATED LDL REFUSED Dialog Element</p></li>
<li><p>VA-IHD FASTING LIPID ORDERED Dialog Element</p></li>
<li><p>VA-IHD LIPID 100-119 DONE ELSE Dialog Element</p></li>
<li><p>VA-IHD LIPID 120-129 DONE ELSE Dialog Element</p></li>
<li><p>VA-IHD LIPID &lt;100 DONE ELSE Dialog Element</p></li>
<li><p>VA-IHD LIPID &gt;129 DONE ELSE Dialog Element</p></li>
<li><p>VA-IHD LIPID DONE ELSEWHERE TEXT Dialog Element</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>+ Enter ?? for more actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AD Add CV Change View INQ Inquiry/Print CO Copy Dialog PT List/Print All QU Quit</p>
<p>Select Item: Next Screen// <strong>CO</strong> Copy Dialog</p>
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
<p>Select the dialog to copy: <strong>VA-IHD LIPID &lt;100 DONE ELSE</strong> dialog element NATIONAL</p>
<p>ENTER A UNIQUE NAME: <strong>OURNAME-IHD LIPID &lt;100 DONE ELSE</strong></p>
<p>Completed copy of 'VA-IHD LIPID &lt;100 DONE ELSE' into 'OURNAME-IHD LIPID &lt;100 DONE ELSE'</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Change the Dialog/Progress Note text in OURNAME-IHD LIPID \<100 DONE ELSE to “Patient reports a more recent LDL \<100” (while still in the Dialog Elements View)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>AD Add CV Change View INQ Inquiry/Print CO Copy Dialog PT List/Print All QU Quit</p>
<p>Select Item: Next Screen// <strong>SL</strong> SL Search for: <strong>OURNAME</strong></p>
</blockquote>
<ol type="1">
<li><p>A A PAIN ASSESS MEMBER REPORTS Dialog Element</p></li>
<li><p>A A PAIN HX LOCATION Dialog Element</p></li>
<li><p>A A PAIN AM OUTSIDE SCORE Dialog Element</p></li>
<li><p>A A PAIN ASSESSMENT ELSEWHERE Dialog Element</p></li>
<li><p>A A PAIN ASSESSMENT TITLE Dialog Element</p></li>
<li><p>A A PAIN HISTORY 1M Dialog Element</p></li>
<li><p>A A PAIN HX ACCEPTABLE PAIN SCORE Dialog Element</p></li>
</ol>
<blockquote>
<p>...searching for 'OURNAME'.......</p>
<p>Find Next 'OURNAME'? Yes// <strong>NO</strong></p>
<p>CO Copy Dialog PT List/Print All QU Quit</p>
<p><strong>Dialog List</strong> May 17, 2002@17:40:55 Page: 50 73</p>
<p>DIALOG VIEW (DIALOG ELEMENTS)</p>
<p>+Item Dialog Name Dialog type Status 796 OURNAME-IHD LIPID &lt;100 DONE ELSE Dialog Element</p>
</blockquote>
<ol start="797" type="1">
<li><p>PAIN Dialog Element</p></li>
<li><p>PAIN ASK PATIENT PAIN SCORE* Dialog Element</p></li>
<li><p>PAIN ENTER NEW PAIN SCORE Dialog Element</p></li>
<li><p>PAIN HX 2ND LOCATION Dialog Element</p></li>
<li><p>PAIN HX ACCEPTABLE ASK* Dialog Element</p></li>
<li><p>PAIN HX CAUSE* Dialog Element</p></li>
<li><p>PAIN HX DECLINED* Dialog Element</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AD Add CV Change View INQ Inquiry/Print CO Copy Dialog PT List/Print All QU Quit</p>
<p>Select Item: Next Screen// <strong>796</strong></p>
<p>Dialog Name: <strong>OURNAME-IHD LIPID &lt; 100 DONE ELSE</strong></p>
<p>Not used by any other dialog</p>
<p>NAME: OURNAME-IHD LIPID &lt; 100 DONE ELSE Replace <strong>&lt;Enter&gt;</strong></p>
<p>DISABLE: <strong>&lt;Enter&gt;</strong> CLASS: LOCAL// <strong>&lt;Enter&gt;</strong> SPONSOR: <strong>&lt;Enter&gt;</strong> REVIEW DATE: <strong>&lt;Enter&gt;</strong></p>
<p>RESOLUTION TYPE: DONE ELSEWHERE (HISTORICAL)// <strong>&lt;Enter&gt;</strong></p>
<p>ORDERABLE ITEM: <strong>&lt;Enter&gt;</strong></p>
<p>FINDING ITEM: OUTSIDE LDL &lt;100// <strong>&lt;Enter&gt;</strong></p>
<p>DIALOG/PROGRESS NOTE TEXT:</p>
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
<p>1&gt;Outside LDL &lt;100 mg/dL EDIT Option: <strong>1</strong></p>
<p>1&gt;Outside LDL &lt;100 mg/dL</p>
<p>Replace <strong>O...</strong> With <strong>Patient reports a more recent LDL &lt;100.</strong></p>
<p>Replace <strong>&lt;Enter&gt;</strong></p>
<p>Patient reports a more recent LDL &lt;100.</p>
<p>Edit line: <strong>&lt;Enter&gt;</strong></p>
<p>EDIT Option:</p>
<p>ALTERNATE PROGRESS NOTE TEXT:</p>
<p>1&gt;<strong>&lt;Enter&gt;</strong></p>
<p>EXCLUDE FROM PROGRESS NOTE: <strong>&lt;Enter&gt;</strong></p>
<p>SUPPRESS CHECKBOX: <strong>&lt;Enter&gt;</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

5.  Delete the VA-IHD LIPID DONE ELSEWHERE \<120 GROUP from the OURNAME-IHD ELEVATED LDL reminder dialog.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog List</strong> May 17, 2002@14:37:32 Page: 3 of 4</p>
<p>REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<p>+Item Reminder Name Linked Dialog Name &amp; Dialog Status</p>
</blockquote>
<ol start="109" type="1">
<li><p>NCG MST</p></li>
<li><p>NCVAMC AIMS</p></li>
<li><p>NEW PROPOSED ALCOHOL SCREEN (AUDIT</p></li>
<li><p>NEW PROPOSED ALCOHOL USE SCREEN DRAFT NEW ALCOHOL USE SCREE</p></li>
<li><p>NEW PROPOSED DEPRESSION SCREEN DOM</p></li>
<li><p>OURNAME-IHD ELEVATED LDL OURNAME-ELEVATED LDL</p></li>
<li><p>ORDTEST</p></li>
<li><p>OUTPATIENT ASSESSMENT - PART 1 rename oupatient Disabled</p></li>
<li><p>OUTPATIENT ASSESSMENT - PART 2 OUTPATIENT ASSESSMENT - PAR Disabled</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>&lt;&lt;&lt; + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AR All reminders LR Linked Reminders QU Quit CV Change View RN Name/Print Name</p>
<p>Select Item: Quit// <strong>114</strong></p>
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
<p><strong>Dialog Selection List</strong> May 17, 2002@14:37:36 Page: 1 of 1</p>
<p>REMINDER NAME: OURNAME-IHD ELEVATED LDL</p>
<p>Item Dialog Name Latest Update Linked Reminders This reminder is linked to dialog:</p>
<p>1 OURNAME-IHD ELEVATED LDL OURNAME-IHD ELEVATED LDL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>+ Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AD Autogenerate Dialog QU Quit LR Link Reminder</p>
<p>Select Item: Quit// <strong>1</strong></p>
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
<p>5 Dialog element: OURNAME-IHD ELEVATED LDL HEADER (1)</p>
<p>10 Dialog group: VA-IHD LIPID LOWER AGENT ORDER GROUP Dialog elements: 5 VA-IHD SIMVASTATIN ORDERED</p>
<p>10 VA-IHD ORDER BASELINE LFTS TODAY</p>
<p>15 VA-IHD ORDER FUTURE LFTS 60 DAYS</p>
<p>20 VA-IHD ORDER FUTURE LIPID PROFILE 60 DAYS</p>
<p>15 Dialog group: VA-IHD LIPID LOWER AGENT ADJUST GROUP Dialog elements: 2 PXRM COMMENT</p>
<p>5 VA-IHD LIPID LOWER AGENT ADJUST TEXT</p>
<p>10 VA-IHD ORDER BASELINE LFTS TODAY</p>
<p>15 VA-IHD ORDER FUTURE LFTS 60 DAYS</p>
<p>20 VA-IHD ORDER FUTURE LIPID PROFILE 60 DAYS</p>
<p>20 Dialog element: VA-IHD LIPID TREATMENT NO CHANGE Select Sequence: Next Screen// <strong>&lt;Enter&gt;</strong> NEXT SCREEN</p>
<p>Resolution: DONE AT ENCOUNTER Finding type: HEALTH FACTOR</p>
<p>Finding item: NO CHANGE IN IHD LIPID TREATMENT [HF(660080)]</p>
<p>Additional prompts: PXRM COMMENT</p>
<p>25 Dialog element: VA-IHD LIPID MEDS CONTRAINDICATED Resolution: CONTRAINDICATED</p>
<p>Finding type: HEALTH FACTOR</p>
<p>Finding item: LIPID MEDS CONTRAINDICATED [HF(660087)]</p>
<p>Additional prompts: PXRM COMMENT</p>
<p>30 Dialog element: VA-IHD LIPID LOWER AGENT ELSEWHERE Resolution: DONE ELSEWHERE (HISTORICAL)</p>
<p>Finding type: HEALTH FACTOR</p>
<p>Finding item: LIPID MGMT PROVIDED OUTSIDE [HF(660082)]</p>
<p>Additional prompts: PXRM COMMENT DP Progress Note Text INQ Inquiry/Print</p>
<p>Select Sequence: Next Screen// <strong>&lt;Enter&gt;</strong> NEXT SCREEN</p>
<p><strong>Dialog Edit List</strong> May 08, 2002@14:37:40 Page: 3 of 5</p>
<p>REMINDER DIALOG NAME: OURNAME-IHD ELEVATED LDL</p>
<p>+Sequence Dialog Details Disabled</p>
<p>35 Dialog element: VA-IHD SPACER</p>
<p>40 Dialog group: VA-IHD LIPID DONE ELSEWHERE &lt;120 GROUP Dialog elements: 5 VA-IHD LIPID DONE ELSEWHERE TEXT</p>
<p>10 VA-IHD LIPID &lt;100 DONE ELSE</p>
<p>15 VA-IHD LIPID 100-119 DONE ELSE</p>
<p>45 Dialog group: VA-IHD LIPID/ALT/AST ORDER GROUP Dialog elements: 5 VA-IHD FASTING LIPID ORDERED</p>
<p>10 VA-IHD DIRECT LDL ORDERED</p>
<p>15 VA-IHD ALT/AST ORDERED</p>
<p>50 Dialog element: VA-IHD ELEVATED LDL REFUSED Resolution: PATIENT REFUSED</p>
<p>Finding type: HEALTH FACTOR</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CO Copy Dialog DT Dialog Text RI Reminder Inquiry DD Detailed Display ED Edit/Delete Dialog QU Quit</p>
<p>DP Progress Note Text INQ Inquiry/Print Select Sequence: Next Screen// <strong>40</strong></p>
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
<p>CURRENT DIALOG ELEMENT NAME: VA-IHD LIPID DONE ELSEWHERE &lt;120 GROUP</p>
<p>Select one of the following:</p>
<p>E Edit</p>
</blockquote>
<ol start="3" type="A">
<li><p>Copy and Replace current element</p></li>
<li><p>Delete element from this dialog</p></li>
</ol>
<blockquote>
<p>Select Dialog Element Action: E// <strong>D</strong>elete element from this dialog</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

6.  Add the new element OURNAME-IHD LIPID \<100 DONE ELSE to the local reminder dialog where the VA-IHD LIPID DONE ELSEWHERE \<120 used to be.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Dialog Edit List</strong> May 08, 2002@14:38:16 Page: 1 of 5</p>
<p>REMINDER DIALOG NAME: OURNAME-IHD ELEVATED LDL</p>
<p>Sequence Dialog Details Disabled</p>
<p>5 Dialog element: OURNAME-IHD ELEVATED LDL HEADER (1)</p>
<p>10 Dialog group: VA-IHD LIPID LOWER AGENT ORDER GROUP Dialog elements: 5 VA-IHD SIMVASTATIN ORDERED</p>
<p>10 VA-IHD ORDER BASELINE LFTS TODAY</p>
<p>15 VA-IHD ORDER FUTURE LFTS 60 DAYS</p>
<p>20 VA-IHD ORDER FUTURE LIPID PROFILE 60 DAYS</p>
<p>15 Dialog group: VA-IHD LIPID LOWER AGENT ADJUST GROUP Dialog elements: 2 PXRM COMMENT</p>
<p>5 VA-IHD LIPID LOWER AGENT ADJUST TEXT</p>
<p>10 VA-IHD ORDER BASELINE LFTS TODAY</p>
<p>15 VA-IHD ORDER FUTURE LFTS 60 DAYS</p>
<p>20 VA-IHD ORDER FUTURE LIPID PROFILE 60 DAYS</p>
<p>20 Dialog element: VA-IHD LIPID TREATMENT NO CHANGE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CO Copy Dialog DT Dialog Text RI Reminder Inquiry DD Detailed Display ED Edit/Delete Dialog QU Quit</p>
<p>DP Progress Note Text INQ Inquiry/Print Select Sequence: Next Screen// <strong>40</strong></p>
<p>ARE YOU ADDING 40 AS A NEW SEQUENCE NUMBER: N// <strong>YES</strong></p>
<p>Select new DIALOG ELEMENT: <strong>OURNAME-IHD LIPID &lt;100 DONE ELSE</strong> dialog element L</p>
<p>...OK? Yes//<strong>&lt;Enter&gt;</strong> (Yes)</p>
<p>30 Dialog element: VA-IHD LIPID LOWER AGENT ELSEWHERE Resolution: DONE ELSEWHERE (HISTORICAL)</p>
<p>Finding type: HEALTH FACTOR</p>
<p>Finding item: LIPID MGMT PROVIDED OUTSIDE [HF(660082)]</p>
<p>Additional prompts: PXRM COMMENT</p>
<p>35 Dialog element: VA-IHD SPACER</p>
<p>40 Dialog element: OURNAME-IHD LIPID &lt;100 DONE ELSE Resolution: DONE ELSEWHERE (HISTORICAL)</p>
<p>Finding type: HEALTH FACTOR</p>
<p>Finding item: OUTSIDE LDL &lt;100 [HF(81)]</p>
<p>Additional prompts: PXRM VISIT DATE</p>
<p>PXRM OUTSIDE LOCATION PXRM COMMENT</p>
<p>DP Progress Note Text INQ Inquiry/Print Select Sequence: Next Screen// NEXT SCREEN</p>
</blockquote></td>
</tr>
</tbody>
</table>

7.  Test your dialog thoroughly, following the instructions given in the setup section of this guide.
8.  If desired, add the dialogs to the CPRS GUI, following the instructions given in the setup section of this guide.