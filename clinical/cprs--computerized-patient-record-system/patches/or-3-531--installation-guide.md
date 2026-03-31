---
title: OR*3*531 CPRS COVID Version 2 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: CPRS COVID Version 2
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*531
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The guide provides specific instructions for installation, back-out, and rollback of the CPRS COVID v2.0 build.
audience: 
keywords: 
  - table
  - contents
  - cprs
  - covid
  - installation
  - back
  - rollback
  - test
  - reminder
  - mark
page_count: 0
word_count: 2715
section_count: 21
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_531_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_531_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Computerized Patient Record System (CPRS)  
  COVID v2.0
---

Deployment, Installation, Back Out and Rollback Guide (DIBORG)

![](or-3-531-cprs-covid-version-2-deployment-installation-back-out-and-rollback-guid/001.png)

July 2020

Office of Information & Technology (OI&T)

Enterprise Program Management Office (EPMO)

This page left intentionally blank.

Revision History

<table>
<caption><p>Table - CPRS COVID v2.0 documentation</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 45%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>7/10/2020</td>
<td>.08</td>
<td>Removed the statement, “This functionality is documented in the Clinical Reminders Manager’s Manual.”</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/2/2020</td>
<td>.07</td>
<td>Removed the CPRS Technical Manual and the Clinical Reminders Managers Manual from the CPRS COVID v2.0 Documentation table.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/24/2020</td>
<td>.06</td>
<td>Added a description in Overview section of the impact of CPRS 31B on the ORWOTHER and PXRMDEV routines.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/12/2020</td>
<td>.05</td>
<td><p>Added an instruction that “the init routine</p>
<p>PXRMP46I can be deleted after a successful installation.”</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/11/2020</td>
<td>.04</td>
<td>Removed sensitive data from the screenshots</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/9/2020</td>
<td>.03</td>
<td>Incorporated suggestions from the site testers</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/5/2020</td>
<td>.02</td>
<td>Incorporated all the suggestions made during the developer and SQA analyst’s review</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/3/2020</td>
<td>.01</td>
<td>Initial Version</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table - CPRS COVID v2.0 documentation

Table of Contents

# CPRS COVID v2.0


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [CPRS COVID v2.0](#cprs-covid-v20)
  - [Overview](#overview)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [Document Conventions](#document-conventions)
  - [Related Documents](#related-documents)
- [Pre-requisites](#pre-requisites)
  - [Pre-requisite Patches](#pre-requisite-patches)
  - [Pre-Installation Steps](#pre-installation-steps)
    - [CPRS COVID v2.0 Preinstallation Check List](#cprs-covid-v20-preinstallation-check-list)
- [Reporting Issues](#reporting-issues)
- [Test – CPRS COVID v2.0 Test System Installation Checklist](#test-cprs-covid-v20-test-system-installation-checklist)
- [Software Retrieval](#software-retrieval)
- [Pre-Installation Steps](#pre-installation-steps-1)
  - [Backup Procedures](#backup-procedures)
    - [Back Up Globals](#back-up-globals)
- [Installation](#installation)
  - [Sequence](#sequence)
    - [Part I –Software Installation](#part-i-software-installation)
    - [Part II – Content Installation](#part-ii-content-installation)
  - [CPRS COVID v2.0 Documentation](#cprs-covid-v20-documentation)
- [TEST - Post-Installation Tasks](#test-post-installation-tasks)
- [TEST – Testing in Test Account](#test-testing-in-test-account)
- [CPRS COVID v2.0 Production System Installation Checklist](#cprs-covid-v20-production-system-installation-checklist)
- [Production Pre-Installation Steps](#production-pre-installation-steps)
  - [Backup Procedures](#backup-procedures-1)
    - [Back Up Globals](#back-up-globals-1)
- [Production Installation](#production-installation)
- [Post-Installation Tasks](#post-installation-tasks)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The guide provides specific instructions for installation, back-out, and rollback of the CPRS COVID v2.0 build.

CPRS_COVID_2_0.KID is a multi-package build that contains patches PXRM\*2.0\*46 and OR\*3.0\*531.

Before CPRS COVID v2.0 was developed, a CPRS COVID-19 status banner was released in CPRS Graphical User Interface (GUI) v31a and the multi-package build CPRS COVID v1.0, which contains patches PXRM\*2.0\*72 and OR\*3.0\*485.

After the CPRS COVID v1.0 release, it was determined that additional functionality was required. This included a precise way to determine the date that is displayed in the banner and the ability to display the patient’s COVID-19 data when the banner is clicked on.

Thus, new Clinical Reminders functionality was developed that can be used in Age Match/No Match Text, Finding Found/Not Found Text, and the Found/Not Found Text for Cohort and Resolution Logic.

This new functionality includes the ability to display the data for any finding in Found/Not Found Text, called CSUB Objects, which control whether text is formatted and whether blank lines will be suppressed.

PXRM\*2.0\*46 installs a Reminder Exchange entry named VA-COVID-19 CPRS STATUS VERSION 4. It is an updated version of the COVID-19 status reminder definition that was released with PXRM\*2.0\*72. It provides enhanced information about a patient’s COVID-19 status when the COVID-19 status banner is clicked.

A Description field was added to the Function Findings multiple of the Reminder Definition file. This is a word-processing field that can be used to document the use and purpose of the function finding. The Reminder Definition Editor and Reminder Inquiry are updated to include this field.

OR\*3.0\*531 turns on the CPRS clickable banner report. The text of the report is created by the API, STATUS^PXRMCOVID19. CPRS calls this API and displays the report when the user clicks on the COVID-19 status banner.

The functionality in CPRS COVID 2.0 needs to work for sites that have CPRS v31b installed and for those that do not. The CPRS 31B multi-package build includes the OR\*3.0\*377 and PXRM\*2.0\*45 builds, which make changes to the ORWOTHER and PXRMDEV routines.

The OR\*3.0\*531/PXRM\*2.0\*46 multi-package build also makes changes to the ORWOTHER and PXRMDEV routines and contains the changes from CPRS v31b.

That is why the second line of ORWOTHER includes patch 377 and the second line of PXRMDEV includes patch 45. After installing CPRS COVID 2.0, the first two lines of these routines will be:

ORWOTHER ;SLC/AGP - Other Information Panel RPC ;06/03/2020  
         ;;3.0;ORDER ENTRY/RESULTS REPORTING;\*\*485,377,531\*\*;Dec 17, 1997

PXRMDEV  ;SLC/PKR - This is a driver for testing Clinical Reminders. ;06/23/2020

         ;;2.0;CLINICAL REMINDERS;\*\*4,6,11,16,18,24,26,47,45,46\*\*;Feb 04, 2005

If CPRS v31b is installed after CPRS COVID 2.0, then CPRS COVID 2.0 must be reinstalled because additional changes will be made to ORWOTHER and PXRMDEV. However, the VA-COVID-19 CPRS STATUS reminder definition and the health factors and terms that it uses do not need to be reinstalled.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) Information Resource Management (IRM) staff who will be installing the build, and for Clinical Application Coordinators (CACs) who will be installing the content from the Reminder Exchange entry VA-COVID-19 CPRS STATUS VERSION 4.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides instructions for installing CPRS_COVID_2_0.KID, the multi-package build containing builds PXRM\*2.0\*46 and OR\*3.0\*531.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Examples of VistA “Roll and Scroll” interface actions will be shown in a box, such as:

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

Emphasis of important points may be displayed in this manner:

> NOTE: This is an important point and must not be omitted.

Call-outs may be used to draw attention to part of a block of text or a table without disrupting the flow of the block or table. For example:

![](or-3-531-cprs-covid-version-2-deployment-installation-back-out-and-rollback-guid/002.png)

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents, in addition to this document, will be available on the VA Software Document Library (VDL) when the patch is released:

[CPRS on the VDL](http://www.va.gov/vdl/application.asp?appid=61)

- *Clinical Reminders Manager’s Manual*
- *CPRS Technical Manual: GUI Version*

# Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the processes described in this document the tasks outlined in this section must be completed.

## Pre-requisite Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS COVID v2.0 expects a fully patched VistA system, including PXRM\*2.0\*72 and OR\*3.0\*485.

## Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### CPRS COVID v2.0 Preinstallation Check List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Reporting Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To report issues with CPRS COVID v2.0, please enter a ticket with the National Help Desk and provide the following information:

- Category: Affected Service
- Affected Service: VistA – CPRS: Clinical Reminders
- Assignment Group: NTL SUP Clin 2

# Test – CPRS COVID v2.0 Test System Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Section 7.1.1.

# Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Back Up Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides instructions for installing CPRS COVID v2.0.

## Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two parts to CPRS COVID v2.0 installation:

- Part I: Software Installation. The multi-package build will be installed by IT Operations and Services (ITOPS).
- Part II: Content Installation. This section covers the installation of the content that is in Reminder Exchange entry VA-COVID-19 CPRS STATUS VERSION 4.

> **NOTE:** Part I should be performed by ITOPS and Part II should be performed by the Clinical Reminders Clinical Applications Coordinator (CAC).

### Part I –Software Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This build should be installed during non-peak hours to minimize disruption to users. Installation should take less than one minute.

1.  Load the host file using the “Load a Distribution” option on the XPD INSTALLATION MENU.
    1.  At the Enter a Host File prompt, type the following: /srv/vista/patches/SOFTWARE/CPRS_COVID_2_0.KID
    2.  NOTE: After loading the distribution, you are directed to use the name “CPRS COVID 2.0” when using other actions on the menu.
2.  Optionally execute the “Verify Checksums” option on the same menu.
3.  Optionally backup the install by using the “Backup a Transport Global” option on the same menu.
4.  Install the multi-package build using the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt, you will need to use the name “CPRS COVID 2.0” as noted in instruction 1.b above.
5.  When prompted with “Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//”, select “NO”.
6.  When prompted with “Want KIDS to INHIBIT LOGONs during the install? NO//”, select “NO”.
7.  When prompted with “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//”, select “NO”.
8.  The init routine PXRMP46I can be deleted after a successful installation.

### Part II – Content Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The content can be installed with users on the system. The name of the Reminder Exchange file is VA-COVID-19 CPRS STATUS VERSION 4. Installation should take less than 5 minutes.

NOTES: For entries that do not exist, use INSTALL action.

For Reminder Terms that exist but are different, use MERGE action.

For Reminder definition VA-COVID-19 CPRS STATUS, use OVERWRITE action.

1.  Locate the Reminder Exchange entry titled VA-COVID-19 CPRS STATUS VERSION4.  
2.  At the Select Action prompt, type “IFE” for Install Exchange File Entry.
3.  Enter the number that corresponds with your entry, VA-COVID-19 CPRS STATUS VERSION 4. In Figure 1, it is 238. It will vary by site.  
    NOTE: The date of the exchange file should be 06/10/2020.

> Figure – “Select Action” and “Enter a List or range of numbers” Prompts for Reminder Exchange Entry  
> ![](or-3-531-cprs-covid-version-2-deployment-installation-back-out-and-rollback-guid/003.png)

4.  At the Select Action prompt, select “IA” and hit “Enter”.  
    NOTE: For entries that do not exist, use INSTALL action.

> **NOTE:** For Reminder Terms that exist but are different, use MERGE action

> **NOTE:** For Reminder definition VA-COVID-19 CPRS STATUS, use OVERWRITE action.

> Figure 2 – Select Action – IA Install All Components ![](or-3-531-cprs-covid-version-2-deployment-installation-back-out-and-rollback-guid/004.png)

5.  When prompted with “REMINDER TEAM entry VA-COVID-19 CLINICAL INFO is NEW, what do you want to do?”, select “I --Install”.
6.  When prompted with “REMINDER TERM entry VA-COVID-19 OUTSIDE RESULTS is NEW, what do you want to do?”, select “I”.
7.  When prompted with “REMINDER TERM entry VA-COVID-19 ANTIBODY LAB TEST is NEW, what do you want to do?”, select “I”.
8.  When prompted with “REMINDER TERM entry VA-COVID-19 PCR/AG LAB RESULTS is NEW, what do you want to do?”, select “I”.
9.  When prompted with “REMINDER DEFINITION entry named VA-COVID-19 CPRS STATUS already exists but the packed component is different, what do you want to do?”, select “O”.
10. When prompted with “Are you sure you want to overwrite?”, select “YES”.

> Figure – Example of REMINDER TERM and REMINDER DEFINITION prompts

> REMINDER TERM entry VA-COVID-19 CLINICAL INFO is NEW,

> what do you want to do?

>      Select one of the following:

>           C         Create a new entry by copying to a new name

>           I         Install

>           Q         Quit the install

>           S         Skip, do not install this entry

> Enter response: I// nstall

> REMINDER TERM entry VA-COVID-19 OUTSIDE RESULTS is NEW,

> what do you want to do?

>      Select one of the following:

>           C         Create a new entry by copying to a new name

>           I         Install

>           Q         Quit the install

>           S         Skip, do not install this entry

> Enter response: I// nstall.

> REMINDER TERM entry VA-COVID-19 ANTIBODY LAB TEST is NEW,

> what do you want to do?

>      Select one of the following:

>           C         Create a new entry by copying to a new name

>           I         Install

>           Q         Quit the install

>           S         Skip, do not install this entry

> Enter response: I// nstall

> REMINDER TERM entry VA-COVID-19 PCR/AG LAB RESULTS is NEW,

> what do you want to do?

>      Select one of the following:

>           C         Create a new entry by copying to a new name

>           I         Install

>           Q         Quit the install

>           S         Skip, do not install this entry

> Enter response: I// nstall

> REMINDER DEFINITION entry named VA-COVID-19 CPRS STATUS already exists

> but the packed component is different, what do you want to do?

>      Select one of the following:

>           C         Create a new entry by copying to a new name

>           O         Overwrite the current entry

>           U         Update

>           Q         Quit the install

>           S         Skip, do not install this entry

> Enter response: O// verwrite the current entry

> Are you sure you want to overwrite? N// y  YES

11. At the Select Action prompt, select “Q”.

> Figure 4 – Select Action – Q Quit

> ![](or-3-531-cprs-covid-version-2-deployment-installation-back-out-and-rollback-guid/005.png)  

> The content installation is complete.

## CPRS COVID v2.0 Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table shows the documentation released with CPRS COVID v2.0.

| *CPRS COVID v2.0 Deployment, Installation, Back Out and Rollback Guide (DIBORG)* | Primarily for installers and CACs. Contains items that must be done before, during and after the patch installation. |
|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|

Table – CPRS Development Team Contacts

# TEST - Post-Installation Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reminder Term VA-COVID-19 PCR/AG LAB RESULTS will need to have your local lab test for COVID testing mapped. Ensure that only LAB TESTS are mapped to this term.

If your site has COVID Antibody Lab Test, you will need to map that Lab Test to Reminder Term VA-COVID-19 ANTIBODY LAB TEST.

If am existing Reminder Term is accidentally OVERWRITTEN, you will need to re-map that term or contact Health Product Support

# TEST – Testing in Test Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing in Production, do some testing in the Test account by opening CPRS for patients who have COVID-19 related data. Verify that the information in the COVID-19 status banner is correct and that the text that displays when the banner is clicked on is also correct.

# CPRS COVID v2.0 Production System Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Production Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Back Up Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Production Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Post-Installation Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Back-out would only be considered if there was a catastrophic failure that causes loss of function for the CPRS application or a significant patient safety issue.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS COVID v2.0 should be backed out only if it causes a catastrophic system failure.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out CPRS COVID v2.0 would remove the COVID-19 banner click text functionality.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out CPRS COVID v2.0 should only be considered if there is a catastrophic failure of OR\*3\*531 and PXRM\*2\*46 or the associated CPRS GUI. The back-out would be accomplished by installing the backout build.

Contact the CPRS implementation team to notify them that there has been a catastrophic failure with OR\*3\*531 and PXRM\*2\*46. Use the mail group: OIT PD CPRS Implementation Team <span class="mark">REDACTED</span>

. You will get instructions on how to obtain the backout build and install it.

In addition, you can contact the following CPRS team members:

| Name and Title                 | Email                          | Phone                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

If the decision is made to proceed with back-out and rollback, coordinate with the appropriate IT support, including local support and IT Operations and Services (ITOPS), to schedule the time to install the rollback build.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The backout patch will also perform any necessary rollback.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A since no database updates were done.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the final authority to require the rollback and accept the associated risks.