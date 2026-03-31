---
title: OR*3.0*498 (v31b followup)  Setup and Configuration Guide
doc_type: CFG
doc_label: Setup and Configuration Guide
doc_layer: patch
doc_subject: (v31b followup)
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*498
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: CPRS v31b Follow-Up Build is a multi-package build that addresses several defects identified during the deployment of the CPRS v31b series of patches.
audience: 
keywords: 
  - reminder
  - finding
  - prompt
  - dialog
  - term
  - press
  - codes
  - group
  - install
  - mammogram
page_count: 0
word_count: 11183
section_count: 17
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2022
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_498_setup_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_0_498_setup_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Computerized Patient Record System (CPRS)  
  Version 31b Follow-Up Build
---

Setup and Configuration Guide

![](or-3-0-498-v31b-followup-setup-and-configuration-guide/001.png)

January 2022

Office of Information & Technology (OI&T)

Enterprise Program Management Office (EPMO)

Revision History

<table style="width:100%;">
<colgroup>
<col style="width: 19%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1/13/2022</td>
<td>0.17</td>
<td>OR*3*498: Redacted for the VDL: removed names and links to software builds</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>1/11/2022</td>
<td>0.16</td>
<td>OR*3*498: Updated Section 5.7 (Resolve Any Object Conflicts).</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>1/10/2022</td>
<td>0.15</td>
<td>OR*3*498: Added Section 5.7 (Resolve Any Object Conflicts).</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>12/9/2021</td>
<td>0.14</td>
<td>OR*3.0*498: More updates to Step #2 in Section 5.2 (Gather SMART Dialog Information).</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>12/8/2021</td>
<td>0.13</td>
<td>OR*3.0*498: Updated Step #1 in Section 5.2 (Gather SMART Dialog Information).</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>11/10/2021</td>
<td>0.12</td>
<td><p>OR*3.0*498: Updated the following sections:<br />
<br />
--5.2 (Gather SMART Dialog Information), Step #1;</p>
<p>--6.1.1 (Install SMART UPDATES Content), Step #18;</p>
<p>--6.1.2 (Install High Risk Medications Content, Step #5</p></td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>11/10/2021</td>
<td>0.11</td>
<td>OR*3.0*498: Added Section 5.1 (Verify that Sites Have Installed Clinical Reminder Update_2_0_210 WH Mammogram Screening Reminder).<br />
<br />
Fixed a typo in Section 5.2 (Gather SMART Term Information).<br />
<br />
Updated Section 5.2 (Install SMART Updates Content):<br />
--Removed the note at the beginning of the section;<br />
--Updated instruction #18.</td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>10/06/2021</td>
<td>0.10</td>
<td>OR*3.0*498: Updated instruction 5.b ("select the Merge action") in Section 6.1.2 (Install High Risk Medications Content).</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>09/01/2021</td>
<td>0.09</td>
<td><p>OR*3.0*498: Updated the following sections:<br />
--Section 6 - Post Installation Steps;</p>
<p>--Section 6.1.1 - Install SMART UPDATES Content;</p>
<p>--Section 6.1.2 - Install High Risk Medications Content</p></td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>07/13/2021</td>
<td>0.08</td>
<td>OR*3.0*498: In Sections 6.1.1 and 6.1.2, changed the "Date Packed" date to 07/07/2021@09:59:53.<br />
In section 6.1.1, added a note about the Pittsburgh and Northport sites.</td>
<td><p>TW: J. Callahan</p>
<p>Dev: A. Puleo</p></td>
</tr>
<tr class="odd">
<td>07/01/2021</td>
<td>0.07</td>
<td>OR*3.0*498: Fixed a typo in Section 5.2 (‘Gather SMART Term Information’).<br />
<br />
In Section 6.1 (‘Install Reminder Content’), fixed instructions #12 and #18: Replaced a reference to section 5.3 with a reference to section 5.2.<br />
<br />
Removed Section 5.6 (‘Resolve TIU Object Naming Conflicts’).</td>
<td><p>TW: J. Callahan</p>
<p>Dev: R. Ruff</p></td>
</tr>
<tr class="even">
<td>05/20/2021</td>
<td>0.06</td>
<td>OR*3.0*498: In the Install SMART UPDATES Content section, updated the instructions that pertained to tomosynthesis.</td>
<td><p>TW: J. Callahan</p>
<p>Dev: R. Ruff</p></td>
</tr>
<tr class="odd">
<td>05/11/2021</td>
<td>0.05</td>
<td><p>OR*3.0*498: Updated the following sections: Gather SMART Team Information, Backup the SMART Content, Back-Up High-Risk Medications for Women Content,</p>
<p>Install SMART UPDATES Content,</p>
<p>Install High Risk Medications Content</p></td>
<td><p>TW: J. Callahan</p>
<p>Dev: R. Ruff</p></td>
</tr>
<tr class="even">
<td>04/13/2021</td>
<td>0.04</td>
<td>OR*3.0*498: Updated the Pre- and Post-Installation Steps sections.</td>
<td><p>TW: J. Callahan</p>
<p>Dev: R. Ruff</p></td>
</tr>
<tr class="odd">
<td>03/09/2021</td>
<td>0.03</td>
<td>OR*3.0*498: Updated the Overview, Reporting Issues, Pre- and Post-Installation Checklist, Pre-Installation Steps and Post-Installation Steps sections.</td>
<td><p>TW: J. Callahan</p>
<p>Dev: R. Ruff</p></td>
</tr>
<tr class="even">
<td>01/11/2021</td>
<td>0.02</td>
<td>OR*3.0_498: Fixed a typo in Section 5: Pre-Installation Steps. Changed “VA-WH SMART BREAST IMAGING DIALOG” to “VA-WH SMART BREAST IMAGING FOLLOW-UP”.</td>
<td>TW: J. Callahan<br />
Dev: R. Ruff</td>
</tr>
<tr class="odd">
<td>12/20/2020</td>
<td>0.01</td>
<td>OR*3.0*498: Initial Draft</td>
<td>TW: J. Callahan<br />
Dev: R. Ruff</td>
</tr>
</tbody>
</table>

Table of Contents

# CPRS v31b Follow-Up Build


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [CPRS v31b Follow-Up Build](#cprs-v31b-follow-up-build)
  - [Overview](#overview)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [Document Conventions](#document-conventions)
  - [Related Documents](#related-documents)
- [Pre-requisites](#pre-requisites)
  - [Pre-requisite Patches](#pre-requisite-patches)
- [Reporting Issues](#reporting-issues)
- [Pre- and Post-Installation Checklist](#pre-and-post-installation-checklist)
- [Pre-Installation Steps](#pre-installation-steps)
  - [Verify that Sites Have Installed Clinical Reminder Update20210 WH Mammogram Screening Reminder](#verify-that-sites-have-installed-clinical-reminder-update20210-wh-mammogram-screening-reminder)
  - [Gather SMART Dialog Information](#gather-smart-dialog-information)
  - [Gather SMART Term Information](#gather-smart-term-information)
  - [Gather Pregnancy Dialog Information](#gather-pregnancy-dialog-information)
  - [Backup the SMART Content](#backup-the-smart-content)
  - [Back-Up the High-Risk Medications for Women Content](#back-up-the-high-risk-medications-for-women-content)
  - [Resolve Any Object Conflicts](#resolve-any-object-conflicts)
- [Post-Installation Steps](#post-installation-steps)
  - [Install Reminder Content](#install-reminder-content)
    - [Install SMART UPDATES Content](#install-smart-updates-content)
    - [Install High Risk Medications Content](#install-high-risk-medications-content)
  - [Enable Clinical Reminder Order Check Rules](#enable-clinical-reminder-order-check-rules)
  - [Link Reminder Terms to Women’s Health Procedure Type Entries](#link-reminder-terms-to-womens-health-procedure-type-entries)
- [Verify Successful Installation](#verify-successful-installation)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v31b Follow-Up Build is a multi-package build that addresses several defects identified during the deployment of the CPRS v31b series of patches.

The CPRS v31b Follow-Up build consists of the following patches:

- OR\*3.0\*498
- WV\*1.0\*26
- PXRM\*2.0\*71
- PSO\*7.0\*622
- TIU\*1.0\*341

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for those personnel who need to perform set up and configuration steps before and after the CPRS v31b Follow-Up Build installation. These groups include Information Technology Operations and Support (ITOPS) staff, Clinical Application Coordinator (CAC) personnel, the site’s Women’s Health group, and others who will be needed so that the CPRS v31b Follow-Up Build will work correctly at sites.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This set up/configuration guide provides instructions for:

- Pre-installation steps, which must be performed before the CPRS v31b Follow-Up Build installation can proceed.
- Post-installation tasks—including configuration tasks—that require knowledge of the underlying VistA system.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Examples of VistA “Roll and Scroll” interface actions will be shown in a box such as this:

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

Emphasis of important points may be displayed in this manner:

> NOTE: This is an important point and must not be omitted.

Call-outs may be used to draw attention to part of a block of text or a table without disrupting the flow of the block or table. For example:  
  
![](or-3-0-498-v31b-followup-setup-and-configuration-guide/002.png)

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents, in addition to this document, will be available on the VA Software Document Library (VDL) when the patch is released:

[CPRS on the VDL](http://www.va.gov/vdl/application.asp?appid=61)

- *CPRS User Guide: GUI Version*
- *CPRS Technical Manual*
- *CPRS Technical Manual: GUI Version*
- *CPRS Release Notes: v31b Follow-Up Build*
- *CPRS v31b Follow-Up Build Deployment, Installation, Back Out and Rollback Guide  
  *

# Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Pre-requisite Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Reporting Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To report issues with CPRS v31b Follow-Up build, please enter a ticket with the National Help Desk.

# Pre- and Post-Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order. Use this checklist and the following sections for both your test/mirror system as well as your production system.

Table 1 Installation Checklist

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 82%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>No.</strong></th>
<th><strong>Task</strong></th>
<th><strong>Done</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li></li>
</ol></td>
<td>Complete the pre-installation steps. (See Section 5.)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td>Notify your ITOPS regional installer that your site is ready for installation.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Make sure that the installation was completed. (See the “CPRS v31b Follow-Up Build Deployment, Installation, Back Out and Rollback Guide”)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Complete the post-installation steps. (See Section 6.)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td>Verify the installation was successful. (See Section 7.)</td>
<td></td>
</tr>
</tbody>
</table>

# Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These pre-installation steps must be performed by the CAC.

## Verify that Sites Have Installed Clinical Reminder Update_2_0_210 WH Mammogram Screening Reminder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites need to install Clinical Reminder Update_2_0_210 WH Mammogram Screening Reminder.

The Install Guide and PowerPoint presentations pertaining to the Clinical Reminder Update for both the clinical staff and clinical informatics staff are available in REDACTED.

## Gather SMART Dialog Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  <span id="Step_5_2_1" class="anchor"></span>Use option Inquire about Reminder Taxonomy Management \[PXRM TAXONOMY MANAGEMENT\] to capture an inquire of the terms listed below.
    1.  VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
    2.  VA-WH MAMMOGRAM SCREENING CODES
    3.  VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
    4.  VA-WH MRI BREAST PROCEDURE CODES
    5.  VA-WH ULTRASOUND BREAST PROCEDURE CODES
2.  <span id="ColumnTitle_01" class="anchor"></span>Use option Reminder Dialogs \[PXRM DIALOG/COMPONENT EDIT\] to record the orders mapped to the VA-WH SMART BREAST IMAGING FOLLOW-UP reminder dialog. The Site will need to re-map these orders to the reminder dialog after the install.

## Gather SMART Term Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use option Inquire about Reminder Term \[PXRM TERM INQUIRY\] to capture a copy of the following terms:
    1.  VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
    2.  VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
    3.  VA-WH ULTRASOUND OF THE BREAST CODES
    4.  VA-WH MRI OF THE BREASTS CODES
    5.  VA-WH MAMMOGRAM SCREENING CODES
2.  <span id="Step_5_3_2" class="anchor"></span>Use option Inquire about Reminder Term \[PXRM TERM INQUIRY\] to review the VA-WH NEXT BREAST PROCEDURE reminder term. From the output, note the condition statement for the VA-WH NEXT BREAST PROCEDURE finding.

## Gather Pregnancy Dialog Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use option Reminder Dialogs \[PXRM DIALOG/COMPONENT EDIT\] to record the findings mapped to the elements listed below. You are prompted during the content installation for these findings.
    1.  <span id="Step3a" class="anchor"></span>VA-WH TD PREGNANCY ORDER EMERGENCY CONTRACEPTIVE
    2.  <span id="Step3b" class="anchor"></span>VA-WH TD PREGNANCY ORDER PREGNANCY TEST

## Backup the SMART Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pack the existing SMART content into a new clinical reminders exchange entry in case a software rollback is needed:

1.  On the Clinical Reminders Exchange screen, at the “Select Action” prompt, enter “CFE” for Create Exchange File Entry.

> Example – Create Exchange File Entry Action

<u>Clinical Reminder Exchange May 11, 2021@09:30:12 Page: 1 of 61\_</u>

Exchange File Entries.

<u>Item Entry Source Date Packed \_</u>

1 BDI II RESULT GROUP CPRSCRM20@SALT LAKE CI 04/13/2004@15:53

2 DEPRESSION/PTSD REMINDER TERM CPRSCRM21@NORTHERN CAL 02/26/2010@12:07

UPDATES - PATCH 17

3 ECOE REMINDER DIALOGS CPRSCRM22@SALT LAKE CI 08/28/2013@09:38

4 GMTS FOR HRMH CPRSCRM23@SALT LAKE CI 12/01/2011@11:10

5 GMTS SKIN RISK HS OBJECTS CPRSCRM20@SALT LAKE CI 07/09/2007@13:21

6 GMTS SKIN RISK HS TYPES CPRSCRM20@SALT LAKE CI 07/09/2007@13:20

7 GMTSMHV CPRSCRM20@SALT LAKE CI 07/06/2004@15:06

8 NATIONAL BLOOD PRESSURE CPRSCRM24@TUSCALOOSA 04/05/2011@13:20

CHANGES

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

CFE Create Exchange File Entry LHF Load Host File

CHF Create Host File LMM Load MailMan Message

CMM Create MailMan Message LR List Reminder Definitions

DFE Delete Exchange File Entry LWH Load Web Host File

IFE Install Exchange File Entry RI Reminder Definition Inquiry

IH Installation History RP Repack

Select Action: Next Screen// CFE Create Exchange File Entry

2.  Add the reminder dialog VA-WH SMART BREAST IMAGING FOLLOW-UP:
    1.  At the Select a File prompt, type “4” for reminder dialog.
    2.  At the Select REMINDER DIALOG NAME prompt, type “VA-WH SMART BREAST IMAGING FOLLOW-UP”.
    3.  At the …OK? prompt, press the Enter key.
    4.  At the Select REMINDER DIALOG NAME prompt, press the Enter key.

> Example – Adding a Reminder Dialog

Select from the following reminder files:

1 REMINDER COMPUTED FINDINGS

2 REMINDER COUNTING GROUP

3 REMINDER DEFINITION

4 REMINDER DIALOG

5 REMINDER EXTRACT COUNTING RULE

6 REMINDER EXTRACT DEFINITION

7 REMINDER LIST RULE

8 REMINDER LOCATION LIST

9 REMINDER SPONSOR

10 REMINDER TAXONOMY

11 REMINDER TERM

12 REMINDER ORDER CHECK ITEMS GROUP

13 REMINDER ORDER CHECK RULES

Select a file: (1-13): 4

Select REMINDER DIALOG NAME: VA-WH SMART BREAST IMAGING FOLLOW-UP reminder

dialog NATIONAL

...OK? Yes// (Yes)

Enter another one or just press enter to go back to file selection.

Select REMINDER DIALOG NAME:

3.  Add the following reminder taxonomies:
- VA-WH ULTRASOUND BREAST PROCEDURE CODES
- VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
- VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
- VA-WH MRI BREAST PROCEDURE CODES
- VA-WH MAMMOGRAM SCREENING CODES
  1.  At the Select a File prompt, type “10” for reminder taxonomy.
  2.  At the Select REMINDER TAXONOMY NAME prompt, enter the name of the taxonomy from the list above.
  3.  At the …OK? prompt, press the Enter key.
  4.  Repeat steps b and c for the remaining taxonomies in the list above.
  5.  At the Select REMINDER TAXONOMY NAME prompt, press the Enter key.

> Example – Adding a Reminder Taxonomy

Select from the following reminder files:

1 REMINDER COMPUTED FINDINGS

2 REMINDER COUNTING GROUP

3 REMINDER DEFINITION

4 REMINDER DIALOG

5 REMINDER EXTRACT COUNTING RULE

6 REMINDER EXTRACT DEFINITION

7 REMINDER LIST RULE

8 REMINDER LOCATION LIST

9 REMINDER SPONSOR

10 REMINDER TAXONOMY

11 REMINDER TERM

12 REMINDER ORDER CHECK ITEMS GROUP

13 REMINDER ORDER CHECK RULES

Select a file: (1-13): 10

Select REMINDER TAXONOMY NAME: VA-WH ULTRASOUND BREAST PROCEDURE CODES LOC

AL

...OK? Yes// (Yes)

Enter another one or just press enter to go back to file selection.

Select REMINDER TAXONOMY NAME:

4.  Add the following reminder terms:
- VA-WH MAMMOGRAM SCREENING CODES
- VA-WH ULTRASOUND OF THE BREAST CODES
- VA-WH MRI OF THE BREASTS CODES
- VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
- VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
- VA-WH NEXT BREAST PROCEDURE
  1.  At the Select a File prompt, type “11” for reminder term.
  2.  At the Select REMINDER TERM NAME prompt, enter the name of the term from the list above.
  3.  At the …OK? prompt, press the Enter key.
  4.  Repeat steps b and c for the remaining terms in the list above.
  5.  At the Select REMINDER TERM NAME prompt, press the Enter key.

> Example – Adding a Reminder Term

Select from the following reminder files:

1 REMINDER COMPUTED FINDINGS

2 REMINDER COUNTING GROUP

3 REMINDER DEFINITION

4 REMINDER DIALOG

5 REMINDER EXTRACT COUNTING RULE

6 REMINDER EXTRACT DEFINITION

7 REMINDER LIST RULE

8 REMINDER LOCATION LIST

9 REMINDER SPONSOR

10 REMINDER TAXONOMY

11 REMINDER TERM

12 REMINDER ORDER CHECK ITEMS GROUP

13 REMINDER ORDER CHECK RULES

Select a file: (1-13): 11

Select REMINDER TERM NAME: VA-WH MAMMOGRAM SCREENING CODES NATIONAL

...OK? Yes// (Yes)

Enter another one or just press enter to go back to file selection.

Select REMINDER TERM NAME:

5.  At the Select a file prompt, press the Enter key.
6.  At the Press ENTER to continue or '^' to exit prompt, press the Enter key.
7.  At the Enter the Exchange File entry name prompt, type “SMART CONTENT BACKUP”.

> Example – Naming the Exchange Entry

Select from the following reminder files:

1 REMINDER COMPUTED FINDINGS

2 REMINDER COUNTING GROUP

3 REMINDER DEFINITION

4 REMINDER DIALOG

5 REMINDER EXTRACT COUNTING RULE

6 REMINDER EXTRACT DEFINITION

7 REMINDER LIST RULE

8 REMINDER LOCATION LIST

9 REMINDER SPONSOR

10 REMINDER TAXONOMY

11 REMINDER TERM

12 REMINDER ORDER CHECK ITEMS GROUP

13 REMINDER ORDER CHECK RULES

Select a file: (1-13):

Checking reminder term(s) for errors.

Checking reminder term VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES

No fatal term errors were found.

Press ENTER to continue or '^' to exit:

Checking reminder term VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES

No fatal term errors were found.

Checking reminder term VA-WH MRI OF THE BREASTS CODES

No fatal term errors were found.

Checking reminder term VA-WH ULTRASOUND OF THE BREAST CODES

No fatal term errors were found.

Checking reminder term VA-WH MAMMOGRAM SCREENING CODES

No fatal term errors were found.

Checking reminder term VA-WH NEXT BREAST PROCEDURE

No fatal term errors were found.

No fatal reminder term problems were found, packing will continue.

Checking reminder dialog(s) for errors..

\*\*WARNING\*\*

VA-WH SMART BREAST IMAGING FOLLOW-UP contains the following errors.

The dialog group VA-WH GP BR BI-RAD SELECTOR: BIRAD 3 is using all

possible evaluation statuses for an evaluation item.

The dialog group VA-WH GP BR BI-RAD SELECTOR: BIRAD 2 is using all

possible evaluation statuses for an evaluation item.

The dialog group VA-WH GP BR BI-RAD SELECTOR: BIRAD 1 is using all

possible evaluation statuses for an evaluation item.

The dialog group VA-WH GP BR BI-RAD SELECTOR: BIRAD 0 is using all

possible evaluation statuses for an evaluation item.

The dialog group VA-WH GP BR BI-RAD SELECTOR: BIRAD 6 is using all

possible evaluation statuses for an evaluation item.

The dialog group VA-WH GP BR BI-RAD SELECTOR: BIRAD 5 is using all

possible evaluation statuses for an evaluation item.

The dialog group VA-WH GP BR BI-RAD SELECTOR: BIRAD 4 is using all

possible evaluation statuses for an evaluation item.

The dialog element VA-WH SMART BR MALE ALERT RESULT is using all possible

evaluation statuses for an evaluation item.

Enter the Exchange File entry name: SMART CONTENT BACKUP

8.  You will now see the Text Editor. A description for the exchange entry is auto generated and appears in the editor. You are not required to edit this description. Press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.

> Example – Adding a Description

Enter a description of the Exchange File entry you are packing..................

...................

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

The following Clinical Reminder items were selected for packing:

REMINDER DIALOG

VA-WH SMART BREAST IMAGING FOLLOW-UP

REMINDER TAXONOMY

VA-WH ULTRASOUND BREAST PROCEDURE CODES

VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES

VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES

VA-WH MRI BREAST PROCEDURE CODES

VA-WH MAMMOGRAM SCREENING CODES

REMINDER TERM

VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES

VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES

VA-WH MRI OF THE BREASTS CODES

VA-WH ULTRASOUND OF THE BREAST CODES

VA-WH MAMMOGRAM SCREENING CODES

VA-WH NEXT BREAST PROCEDURE

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

9.  You will now see the Text Editor a second time. You are not required to enter any keywords or phrases. Press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.

> Example – Adding Keywords

Enter keywords or phrases to help index the entry you are packing.

Separate the keywords or phrases on each line with commas.

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

10. The exchange entry is now packed.
11. You are returned to the Clinical Reminders Exchange screen. Note at the top of the screen that the entry you created was saved.

> Example – Reminder Exchange Entry Successfully Created

<u>Clinical Reminder Exchange May 11, 2021@09:34:52 Page: 1 of 61\_</u>

SMART CONTENT BACKUP was saved in the Exchange File.

<u>Item Entry Source Date Packed \_</u>

1 BDI II RESULT GROUP CPRSCRM20@SALT LAKE CI 04/13/2004@15:53

2 DEPRESSION/PTSD REMINDER TERM CPRSCRM21@NORTHERN CAL 02/26/2010@12:07

UPDATES - PATCH 17

3 ECOE REMINDER DIALOGS CPRSCRM22@SALT LAKE CI 08/28/2013@09:38

4 GMTS FOR HRMH CPRSCRM23@SALT LAKE CI 12/01/2011@11:10

5 GMTS SKIN RISK HS OBJECTS CPRSCRM20@SALT LAKE CI 07/09/2007@13:21

6 GMTS SKIN RISK HS TYPES CPRSCRM20@SALT LAKE CI 07/09/2007@13:20

7 GMTSMHV CPRSCRM20@SALT LAKE CI 07/06/2004@15:06

8 NATIONAL BLOOD PRESSURE CPRSCRM24@TUSCALOOSA 04/05/2011@13:20

CHANGES

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

CFE Create Exchange File Entry LHF Load Host File

CHF Create Host File LMM Load MailMan Message

CMM Create MailMan Message LR List Reminder Definitions

DFE Delete Exchange File Entry LWH Load Web Host File

IFE Install Exchange File Entry RI Reminder Definition Inquiry

IH Installation History RP Repack

Select Action: Next Screen//

## Back-Up the High-Risk Medications for Women Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pack the existing high-risk medications for women content into a new clinical reminders exchange entry in case a software rollback is needed:

1.  On the Clinical Reminders Exchange screen, at the “Select Action” prompt, enter “CFE” for Create Exchange File Entry.

> Example – Create Exchange File Entry Action

<u>Clinical Reminder Exchange May 11, 2021@10:10:07 Page: 1 of 61\_</u>

Exchange File Entries.

<u>Item Entry Source Date Packed \_</u>

1 BDI II RESULT GROUP CPRSCRM20@SALT LAKE CI 04/13/2004@15:53

2 DEPRESSION/PTSD REMINDER TERM CPRSCRM21@NORTHERN CAL 02/26/2010@12:07

UPDATES - PATCH 17

3 ECOE REMINDER DIALOGS CPRSCRM22@SALT LAKE CI 08/28/2013@09:38

4 GMTS FOR HRMH CPRSCRM23@SALT LAKE CI 12/01/2011@11:10

5 GMTS SKIN RISK HS OBJECTS CPRSCRM20@SALT LAKE CI 07/09/2007@13:21

6 GMTS SKIN RISK HS TYPES CPRSCRM20@SALT LAKE CI 07/09/2007@13:20

7 GMTSMHV CPRSCRM20@SALT LAKE CI 07/06/2004@15:06

8 NATIONAL BLOOD PRESSURE CPRSCRM24@TUSCALOOSA 04/05/2011@13:20

CHANGES

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

CFE Create Exchange File Entry LHF Load Host File

CHF Create Host File LMM Load MailMan Message

CMM Create MailMan Message LR List Reminder Definitions

DFE Delete Exchange File Entry LWH Load Web Host File

IFE Install Exchange File Entry RI Reminder Definition Inquiry

IH Installation History RP Repack

Select Action: Next Screen// CFE Create Exchange File Entry

2.  Add the following reminder definitions:
- VA-WH CHANGE IN PREGNANCY STATUS
- VA-WH NO PREGNANCY END DOC RPT
- VA-WH POTENTIALLY UNSAFE MEDICATIONS REPORT - COHORT
- VA-WH PREGNANCY AND LACTATION DATA ENTRY ALLOWED
- VA-WH UPDATE LACTATION STATUS
- VA-WH UPDATE PREGNANCY STATUS
  1.  At the Select a File prompt, type “3” for reminder definition.
  2.  At the Select REMINDER DEFINITION NAME prompt, enter the name of the definition from the list above.
  3.  Repeat step b for the remaining definitions in the list above.
  4.  At the Select REMINDER DEFINITION NAME prompt, press the Enter key.

> Example – Adding a Reminder Definition

Select from the following reminder files:

1 REMINDER COMPUTED FINDINGS

2 REMINDER COUNTING GROUP

3 REMINDER DEFINITION

4 REMINDER DIALOG

5 REMINDER EXTRACT COUNTING RULE

6 REMINDER EXTRACT DEFINITION

7 REMINDER LIST RULE

8 REMINDER LOCATION LIST

9 REMINDER SPONSOR

10 REMINDER TAXONOMY

11 REMINDER TERM

12 REMINDER ORDER CHECK ITEMS GROUP

13 REMINDER ORDER CHECK RULES

Select a file: (1-13): 3

Select REMINDER DEFINITION NAME: VA-WH CHANGE IN PREGNANCY STATUS NATIONAL

Enter another one or just press enter to go back to file selection.

Select REMINDER DEFINITION NAME:

3.  Add the reminder dialog PXRM PATCH 45 TIU/HS OBJECTS:
    1.  At the Select a File prompt, type “4” for reminder dialog.
    2.  At the Select REMINDER DIALOG NAME prompt, type “PXRM PATCH 45 TIU/HS OBJECTS”.
    3.  At the …OK? prompt, press the Enter key.
    4.  At the Select REMINDER DIALOG NAME prompt, press the Enter key.

> Example – Adding a Reminder Dialog

Select from the following reminder files:

1 REMINDER COMPUTED FINDINGS

2 REMINDER COUNTING GROUP

3 REMINDER DEFINITION

4 REMINDER DIALOG

5 REMINDER EXTRACT COUNTING RULE

6 REMINDER EXTRACT DEFINITION

7 REMINDER LIST RULE

8 REMINDER LOCATION LIST

9 REMINDER SPONSOR

10 REMINDER TAXONOMY

11 REMINDER TERM

12 REMINDER ORDER CHECK ITEMS GROUP

13 REMINDER ORDER CHECK RULES

Select a file: (1-13): 4

Select REMINDER DIALOG NAME: PXRM PATCH 45 TIU/HS OBJECTS dialog element

LOCAL

...OK? Yes// (Yes)

Enter another one or just press enter to go back to file selection.

Select REMINDER DIALOG NAME:

4.  Add the following reminder taxonomies:
- VA-WH CURRENTLY LACTATING
- VA-WH POSSIBLE PREGNANCY
1.  At the Select a File prompt, type “10” for reminder taxonomy.
2.  At the Select REMINDER TAXONOMY NAME prompt, enter the name of the taxonomy from the list above.
3.  At the …OK? prompt, press the Enter key.
4.  Repeat steps b and c for the remaining taxonomies in the list above.
5.  At the Select REMINDER TAXONOMY NAME prompt, press the Enter key.

> Example – Adding a Reminder Taxonomy

Select from the following reminder files:

1 REMINDER COMPUTED FINDINGS

2 REMINDER COUNTING GROUP

3 REMINDER DEFINITION

4 REMINDER DIALOG

5 REMINDER EXTRACT COUNTING RULE

6 REMINDER EXTRACT DEFINITION

7 REMINDER LIST RULE

8 REMINDER LOCATION LIST

9 REMINDER SPONSOR

10 REMINDER TAXONOMY

11 REMINDER TERM

12 REMINDER ORDER CHECK ITEMS GROUP

13 REMINDER ORDER CHECK RULES

Select a file: (1-13): 10

Select REMINDER TAXONOMY NAME: VA-WH CURRENTLY LACTATING NATIONAL

...OK? Yes// (Yes)

Enter another one or just press enter to go back to file selection.

Select REMINDER TAXONOMY NAME:

5.  Add the following reminder order check items groups:
- VA-WH HIRISK CONTRACEPTIVES GROUP
- VA-WH HIRISK IMAGING AGENTS GROUP
- VA-WH HIRISK IMAGING PROCEDURES (MRI) GROUP
- VA-WH HIRISK IMAGING PROCEDURES (NON MRI) GROUP
- VA-WH HIRISK MEDICATIONS (EXTREME RISK) GROUP
- VA-WH HIRISK MEDICATIONS (LACTATION LEVEL 1) GROUP
- VA-WH HIRISK MEDICATIONS (LACTATION LEVEL 2) GROUP
- VA-WH HIRISK MEDICATIONS (MOD/HIGH RISK DURING PREGNANCY) GROUP
- VA-WH HIRISK MEDICATIONS (MODERATE/HIGH RISK) GROUP
1.  At the Select a File prompt, type “12” for reminder order check items group.
2.  At the Select REMINDER ORDER CHECK ITEMS GROUP GROUP NAME prompt, enter the name of the order check items group from the list above.
3.  Repeat step b for the remaining order check items groups in the list above.
4.  At the Select REMINDER ORDER CHECK ITEMS GROUP GROUP NAME prompt, press the Enter key.

> Example – Adding a Reminder Taxonomy

Select from the following reminder files:

1 REMINDER COMPUTED FINDINGS

2 REMINDER COUNTING GROUP

3 REMINDER DEFINITION

4 REMINDER DIALOG

5 REMINDER EXTRACT COUNTING RULE

6 REMINDER EXTRACT DEFINITION

7 REMINDER LIST RULE

8 REMINDER LOCATION LIST

9 REMINDER SPONSOR

10 REMINDER TAXONOMY

11 REMINDER TERM

12 REMINDER ORDER CHECK ITEMS GROUP

13 REMINDER ORDER CHECK RULES

Select a file: (1-13): 12

Select REMINDER ORDER CHECK ITEMS GROUP GROUP NAME: VA-WH HIRISK CONTRACEPTIVESP

Enter another one or just press enter to go back to file selection.

Select REMINDER ORDER CHECK ITEMS GROUP GROUP NAME:

6.  At the Select a file prompt, press the Enter key.
7.  At the Press ENTER to continue or '^' to exit prompt, press the Enter key.
8.  At the Enter the Exchange File entry name prompt, type “HI RISK MEDICATIONS CONTENT BACKUP”.

> Example – Naming the Exchange Entry

Checking reminder definition(s) for errors.

Checking reminder definition VA-WH PREGNANCY AND LACTATION DATA ENTRY ALLOWED

> **WARNING:** There is no Resolution logic.

Press ENTER to continue or '^' to exit:

No fatal reminder definition errors were found.

Checking reminder definition VA-WH UPDATE LACTATION STATUS

No fatal reminder definition errors were found.

Checking reminder definition VA-WH UPDATE PREGNANCY STATUS

No fatal reminder definition errors were found.

Checking reminder definition VA-WH POTENTIALLY UNSAFE MEDICATIONS REPORT - COHOR

T

> **WARNING:** There is no Resolution logic.

No fatal reminder definition errors were found.

Checking reminder definition VA-WH CHANGE IN PREGNANCY STATUS

> **WARNING:** There is no Resolution logic.

No fatal reminder definition errors were found.

Checking reminder definition VA-WH NO PREGNANCY END DOC RPT

> **WARNING:** There is no Resolution logic.

No fatal reminder definition errors were found.

No fatal reminder definition problems were found, packing will continue.

Checking reminder dialog(s) for errors....

No fatal dialog problems were found, packing will continue.

Enter the Exchange File entry name: HI RISK MEDICATIONS CONTENT BACKUP

9.  You will now see the Text Editor. A description for the exchange entry is auto generated and appears in the editor. You are not required to edit this description. Press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.

> Example – Adding a Description

Enter a description of the Exchange File entry you are packing..................

...................

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

The following Clinical Reminder items were selected for packing:

REMINDER ORDER CHECK ITEMS GROUP

VA-WH HIRISK IMAGING AGENTS GROUP

VA-WH HIRISK MEDICATIONS (LACTATION LEVEL 1) GROUP

VA-WH HIRISK IMAGING PROCEDURES (NON MRI) GROUP

VA-WH HIRISK IMAGING PROCEDURES (MRI) GROUP

VA-WH HIRISK MEDICATIONS (MOD/HIGH RISK DURING PREGNANCY) GROUP

VA-WH HIRISK MEDICATIONS (EXTREME RISK) GROUP

VA-WH HIRISK MEDICATIONS (LACTATION LEVEL 2) GROUP

VA-WH HIRISK MEDICATIONS (MODERATE/HIGH RISK) GROUP

VA-WH HIRISK CONTRACEPTIVES GROUP

REMINDER DIALOG

PXRM PATCH 45 TIU/HS OBJECTS

REMINDER TAXONOMY

VA-WH CURRENTLY LACTATING

VA-WH POSSIBLE PREGNANCY

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

10. You will now see the Text Editor a second time. You are not required to enter any keywords or phrases. Press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.

> Example – Adding Keywords

Enter keywords or phrases to help index the entry you are packing.

Separate the keywords or phrases on each line with commas.

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

11. The exchange entry is now packed.
12. You are returned to the Clinical Reminders Exchange screen. Note at the top of the screen that the entry you created was saved.
13. At the Select Action prompt, type “Q” to exit Reminder Exchange.

> Example – Exiting Reminder Exchange

<u>Clinical Reminder Exchange May 11, 2021@10:14:57 Page: 1 of 61\_</u>

HI RISK MEDICATIONS CONTENT BACKUP was saved in the Exchange File.

<u>Item Entry Source Date Packed \_</u>

1 BDI II RESULT GROUP CPRSCRM20@SALT LAKE C 04/13/2004@15:53

2 DEPRESSION/PTSD REMINDER TERM CPRSCRM21@NORTHERN CAL 02/26/2010@12:07

UPDATES - PATCH 17

3 ECOE REMINDER DIALOGS CPRSCRM22@SALT LAKE CI 08/28/2013@09:38

4 GMTS FOR HRMH CPRSCRM23@SALT LAKE CI 12/01/2011@11:10

5 GMTS SKIN RISK HS OBJECTS CPRSCRM20@SALT LAKE CI 07/09/2007@13:21

6 GMTS SKIN RISK HS TYPES CPRSCRM20@SALT LAKE CI 07/09/2007@13:20

7 GMTSMHV CPRSCRM20@SALT LAKE CI 07/06/2004@15:06

8 HI RISK MEDICATIONS CONTENT CPRSCRM25@WEST PALM BE 05/11/2021@10:10

BACKUP

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

CFE Create Exchange File Entry LHF Load Host File

CHF Create Host File LMM Load MailMan Message

CMM Create MailMan Message LR List Reminder Definitions

DFE Delete Exchange File Entry LWH Load Web Host File

IFE Install Exchange File Entry RI Reminder Definition Inquiry

IH Installation History RP Repack

Select Action: Next Screen// Q

## Resolve Any Object Conflicts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new national TIU objects are being released in TIU\*1.0\*341. As part of the installation, there is a check to ensure that an object currently on the system doesn’t duplicate the print name or abbreviation.

> **WARNING:** If the object that duplicates the print name or abbreviation is found during the OR\*3\*498 installation process, the installation will abort.

To ensure there is no issue with the installation, you should identify any problematic object(s) and modify the print name or abbreviation, as appropriate. You need to use FileMan to search for the following:

- ABBREVIATION equal to POX
- ABBREVIATION equal to EDD
- PRINT NAME equal to PULSE OXIMETRY
- PRINT NAME equal to EXPECTED DUE DATE

The example on the next page shows the search for all of the above-listed TIU Objects.

After you have searched for the TIU objects, if you need to change the abbreviation and/or print name, you can either use FileMan or go to the following menu:

- TIU IRM Maintenance Menu--\> Document Definitions (Manager) --\> Edit Document Definitions.

Example – Search for TIU Objects

Select VA FileMan Option: Search File Entries

Output from what File: TIU DOCUMENT DEFINITION//  

  -A- SEARCH FOR TIU DOCUMENT DEFINITION FIELD: TYPE 

  -A- CONDITION: EQUALS 

  -A- EQUALS: OBJECT

  -B- SEARCH FOR TIU DOCUMENT DEFINITION FIELD: PRINT NAME 

  -B- CONDITION: EQUALS 

  -B- EQUALS: PULSE OXIMETRY

  -C- SEARCH FOR TIU DOCUMENT DEFINITION FIELD: PRINT NAME 

  -C- CONDITION: EQUALS 

  -C- EQUALS: EXPECTED DUE DATE

  -D- SEARCH FOR TIU DOCUMENT DEFINITION FIELD: ABBREVIATION 

  -D- CONDITION: EQUALS 

  -D- EQUALS: POX

  -E- SEARCH FOR TIU DOCUMENT DEFINITION FIELD: ABBREVIATION 

  -E- CONDITION: EQUALS 

  -E- EQUALS: EDD

  -F- SEARCH FOR TIU DOCUMENT DEFINITION FIELD:

IF: AB    TYPE EQUALS "O" (OBJECT)

                 and PRINT NAME EQUALS (case-insensitive) "PULSE OXIMETRY"

OR: AC     Or TYPE EQUALS "O" (OBJECT)

                 and PRINT NAME EQUALS (case-insensitive) "EXPECTED DUE DATE"

OR: AD     Or TYPE EQUALS "O" (OBJECT)

                 and ABBREVIATION EQUALS (case-insensitive) "POX"

OR: AE     Or TYPE EQUALS "O" (OBJECT)

                 and ABBREVIATION EQUALS (case-insensitive) "EDD"

OR:

STORE RESULTS OF SEARCH IN TEMPLATE: TIU 341

  Are you adding 'TIU 341' as a new SORT TEMPLATE? No// Y  (Yes)

DESCRIPTION:

  Edit? NO//

Sort by: NAME//

Start with NAME: FIRST//

First Print FIELD: \[CAPTIONED       

  

Include COMPUTED fields:  (N/Y/R/B): NO// BOTH Computed Fields and Record Number

(IEN)

Heading (S/C): TIU DOCUMENT DEFINITION Search  Replace

DEVICE: 0;0;999  VIRTUAL TELNET    Right Margin: 80//

TIU DOCUMENT DEFINITION Search                       JAN 10, 2022@11:10   PAGE 1

--------------------------------------------------------------------------------

# Post-Installation Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These post-installation steps must be performed by the CAC.  
  
Post-Installation steps are:

- Install reminder content.
- Enable clinical reminder order check rules.
- Link reminder terms to women’s health procedure type entries.

> This section will take approximately 45 minutes to complete.

## Install Reminder Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install the following exchange file entries:

- PXRM\*2.0\*71 SMART UPDATES
- PXRM\*2.0\*71 HI RISK MEDS CONTENT

> **NOTE:** These steps need to be performed by the site’s Clinical Reminders Manager.

### Install SMART UPDATES Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the Reminder Exchange, search for the text PXRM\*2.0\*71 SMART UPDATES and then, locate an entry titled PXRM\*2.0\*71 SMART UPDATES.
2.  At the “Select Action” prompt, enter “IFE” for Install Exchange File Entry.
3.  At the “Enter a list or range of numbers” prompt, enter the number that corresponds with your entry, PXRM\*2.0\*71 SMART UPDATES. (In the “Example-Reminder Exchange” below, it is 38.) It will vary by site. Make sure you select the Item whose “Date Packed” is set to 07/07/2021@09:59:53.

> Example – Reminder Exchange

<u>+Item Entry Source Date Packed \_</u>

38 PXRM\*2.0\*71 SMART UPDATES CPRSCRM1@CAMP MASTER 07/07/2021@09:59

39 RT ALCOHOL NONE PAST 1YR CPRSCRM2@NORTHERN CAL 02/03/2009@08:32

40 TIU TEMPLATE URL FIX CPRSCRM3@SALT LAKE CI 06/07/2016@06:18

41 TIU\*1\*112 20040325 CPRSCRM4@ALBANY 03/25/2004@14:20

42 TIU\*1\*242 20080814 CPRSCRM5@ZZ ALBANY-PR 08/14/2008@08:20

43 TIU\*1\*246 20090128 DC/TL CPRSCRM5@SALT LAKE CI 01/28/2009@17:05

44 TIU\*1\*246 20090128 TL CPRSCRM6@SALT LAKE CI 01/28/2009@17:09

45 TX HIGH RISK FLU AND PNEUMONIA CPRSCRM7@NORTHERN CAL 02/09/2009@09:22

46 UPDATE VA-DIABETES CRRSCRM7@NORTHERN CAL 02/18/2009@10:04

47 UPDATE_2_0_1 BENEFICIARY CPRSCRM8@SALT LAKE CI 02/18/2016@13:34

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

CFE Create Exchange File Entry LHF Load Host File

CHF Create Host File LMM Load MailMan Message

CMM Create MailMan Message LR List Reminder Definitions

DFE Delete Exchange File Entry LWH Load Web Host File

IFE Install Exchange File Entry RI Reminder Definition Inquiry

IH Installation History RP Repack

Select Action: Next Screen// IFE Install Exchange File Entry

Enter a list or range of numbers (1-334): 38

4.  At the “Select Action” prompt in the Exchange File Entry, enter “IA” for Install All Components.  
      
    Example – Exchange File Entry

<u>Component Category Exists\_</u>

Source: CPRSCRM1,ONE at CAMP MASTER

Date Packed: 07/07/2021@09:59:53

Package Version: 2.0P42

Description:

The following Clinical Reminder items were selected for packing:

REMINDER DIALOG

VA-WH SMART BREAST IMAGING FOLLOW-UP

REMINDER TAXONOMY

VA-WH ULTRASOUND BREAST PROCEDURE CODES

VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES

VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES

VA-WH MRI BREAST PROCEDURE CODES

VA-WH MAMMOGRAM SCREENING CODES

\+ Enter ?? for more actions \>\>\>

IA Install all Components IS Install Selected Component

Select Action: Next Screen// IA

5.  The general rules for component installation are as follows:
    1.  If a component does not exist (it is NEW), select the Install action.
    2.  If these reminder terms exist (they are DIFFERENT), select the “Skip, do not install this entry” action:
- VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
- VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
- VA-WH ULTRASOUND BREAST CODES
- VA-WH MRI BREASTS CODES
- VA-WH MAMMOGRAM SCREENING CODES
  1.  For all other reminder terms and components, if a component does exist (it is DIFFERENT), select the “Overwrite” action.
6.  At this point, the dialog installation begins. Install the FIRST reminder dialog:
    1.  At the “Select Action” prompt, enter “IA” for Install All. It will install the dialog, VA-WH SMART BREAST IMAGING FOLLOW-UP.

> Example – VA-WH SMART BREAST IMAGING FOLLOW-UP dialog install

Packed reminder dialog: VA-WH SMART BREAST IMAGING FOLLOW-UP

<u>Item Seq. Dialog Findings Type Exists\_</u>

1 VA-WH SMART BREAST IMAGING FOLLOW-UP dialog X

2 10 VA-WH GP BR OPEN PROCEDURES\* group X

Finding: \*NONE\*

3 10.10 VA-WH BR NO OPEN PROCEDURES\* element X

Finding: \*NONE\*

4 10.15 VA-WH BR EPISODE OF CARE element X

Finding: VIEW EPISODE (REMINDER GENERAL FINDING) X

5 PXRM GF VIEW BUTTON prompt X

6 10.20 VA-WH BR LAST 3 TRMTS element X

Finding: VIEW LAST THREE BR TRMTS (REMINDER GENERAL FINDING) X

7 PXRM GF VIEW BUTTON prompt X

8 10.25 VA-WH BLANK LINE element X

Finding: \*NONE\*

9 10.30 VA-WH GP BR BI-RAD SELECTOR\* group X

\+ + Next Screen - Prev Screen ?? More Actions

DD Dialog Details DT Dialog Text IS Install Selected

DF Dialog Findings DU Dialog Usage QU Quit

DS Dialog Summary IA Install All

Select Action: Next Screen// IA

7.  At the “Install reminder dialog and all components with no further changes” prompt, enter “Yes”.
8.  Respond to the prompt on how you want to handle the non-existent finding, Q. BREAST TREATMENT MENU:
    1.  At the “Enter response” prompt, enter “P” for Replace with an existing entry.
    2.  At the “Select ORDER DIALOG NAME” prompt, enter the name of the first finding you recorded in Section 5.2, Step [\#2](#ColumnTitle_01).
    3.  After the dialog installation completes, you will see the Dialog Components screen. At the “Select Action” prompt, enter “QU” for Quit.

> Example – Dialog Components screen

Packed reminder dialog: VA-WH SMART BREAST IMAGING FOLLOW-UP

VA-WH SMART BREAST IMAGING FOLLOW-UP (reminder dialog) installed from exchange f

<u>Item Seq. Dialog Findings Type Exists\_</u>

1 VA-WH SMART BREAST IMAGING FOLLOW-UP dialog X

2 10 VA-WH GP BR OPEN PROCEDURES\* group X

Finding: \*NONE\*

3 10.10 VA-WH BR NO OPEN PROCEDURES\* element X

Finding: \*NONE\*

4 10.15 VA-WH BR EPISODE OF CARE element X

Finding: VIEW EPISODE (REMINDER GENERAL FINDING) X

5 PXRM GF VIEW BUTTON prompt X

6 10.20 VA-WH BR LAST 3 TRMTS element X

Finding: VIEW LAST THREE BR TRMTS (REMINDER GENERAL FINDING) X

7 PXRM GF VIEW BUTTON prompt X

8 10.25 VA-WH BLANK LINE element X

Finding: \*NONE\*

9 10.30 VA-WH GP BR BI-RAD SELECTOR\* group X

\+ + Next Screen - Prev Screen ?? More Actions

DD Dialog Details DT Dialog Text IS Install Selected

DF Dialog Findings DU Dialog Usage QU Quit

DS Dialog Summary IA Install All

Select Action: Next Screen// QU

9.  You will now see the Exchange File Components screen. At the “Select Action” prompt, enter “Q” for Quit.

    Example – Exchange File Components screen

<u>Component Category Exists\_</u>

Source: CPRSCAC1,ONE at CAMP MASTER

Date Packed: 07/07/2021@09:59:53

Package Version: 2.0P42

Description:

The following Clinical Reminder items were selected for packing:

REMINDER DIALOG

VA-WH SMART BREAST IMAGING FOLLOW-UP

REMINDER TAXONOMY

VA-WH ULTRASOUND BREAST PROCEDURE CODES

VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES

VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES

VA-WH MRI BREAST PROCEDURE CODES

VA-WH MAMMOGRAM SCREENING CODES

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

IA Install all Components IS Install Selected Component

Select Action: Next Screen// Q

10. You will now see the main exchange screen. At the “Select Action” prompt, enter “Q” for Quit.
11. Use option Inquire about Reminder Term \[PXRM TERM INQUIRY\] to capture a copy of the following terms:
- VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
- VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
- VA-WH ULTRASOUND BREAST CODES
- VA-WH MRI BREASTS CODES
- VA-WH MAMMOGRAM SCREENING CODES
12. Compare the capture for each term in the previous step with the capture you created in Section 5.2, step [\#1](#Step_5_2_1). Identify the findings in the pre-install capture that do not appear in the post-install capture. If there are any pre-install findings that are not included in the post-install findings, use option Add/Edit Reminder Term \[PXRM TERM EDIT\] to add them:

> NOTE: During installation, the VA-WH ULTRASOUND OF THE BREAST CODES term listed in Section 5.2, step [\#1](#Step_5_2_1) was renamed to VA-WH ULTRASOUND BREAST CODES and the VA-WH MRI OF THE BREASTS CODES term was renamed to VA-WH MRI BREASTS CODES. Make sure you use the new name for these terms in step a below.

1.  At the “Select Reminder Term” prompt, enter the name of the term listed above in the previous step.
2.  At the “Select Finding” prompt, enter the letters found to the right of the equals sign on the line below the name of the finding you are adding (highlighted in gray in the example on the next page), then enter a period and then finally enter the name of the finding.

> Example – Pre-Install Capture Finding Not Found in Post-Install Capture

Finding Item: LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES

(FI(2)=<span class="mark">TX</span>(129))

Finding Type: REMINDER TAXONOMY

3.  At the “...OK?” prompt, press the Enter key.
4.  At the “Are you adding '…' as a new FINDINGS” prompt, enter the word YES.
5.  At the “FINDING ITEM” prompt, press the Enter key.
6.  At the “BEGINNING DATE/TIME” prompt, enter a caret (^).
7.  Repeat steps b through f for the remaining pre-install findings that were not found in the post-install findings.

> Example – Adding a Finding to a Term

Select Reminder Term: VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES NATIONAL

...OK? Yes// (Yes)

Choose from:

TX VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES Finding \# 1

Select Finding: TX.LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES

Searching for a REMINDER TAXONOMY, (pointed-to by FINDING ITEM)

Searching for a REMINDER TAXONOMY

LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES LOCAL

...OK? Yes// (Yes)

Are you adding 'LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES' as

a new FINDINGS (the 2ND for this REMINDER TERM)? No// YES (Yes)

Editing Finding Number: 2

FINDING ITEM: LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES

//

BEGINNING DATE/TIME: ^

Choose from:

TX LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES Finding \# 2

TX VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES Finding \# 1

Select Finding:

8.  At the “Select Finding” prompt, press the Enter key.
9.  At the “Press ENTER to continue or '^' to exit” prompt, press the Enter key.
10. At the “Edit?” prompt, enter the word YES.

> Example – Closing the Edit Session

Select Finding:

Checking integrity of the term ...

No fatal term errors were found.

Press ENTER to continue or '^' to exit:

Input your edit comments.

Edit? NO// YES

11. You will now see the Text Editor. Enter a comment. In the example below, the comment is “Added local findings removed during installation per CPRS v31b Follow-up Setup and Configuration Guide.”

> Example – Text Editor

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

Added local findings removed during installation per CPRS v31b Follow-up

Setup and Configuration Guide.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

12. After you enter a comment, press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.
13. Repeat steps a through l for the remaining reminder terms listed in step \#11.
14. At the “Select Reminder Term” prompt, press the ENTER key.
13. Use option Inquire about Reminder Term \[PXRM TERM INQUIRY\] to capture a copy of the following terms:
- VA-WH MAMMOGRAM SCREENING CODES
- VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
- VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
14. Review the term captures from the previous step and identify the findings related to tomosynthesis as well as the term those findings belong to.
15. For each term with tomosynthesis-related findings you identified in the previous step, use option Add/Edit Reminder Term \[PXRM TERM EDIT\] to add those findings to the corresponding term listed in the “Add Tomosynthesis Findings to Term” column in the table below:

| Term with Tomosynthesis Findings    | Add Tomosynthesis Findings to Term |
|-----------------------------------------|----------------------------------------|
| VA-WH MAMMOGRAM SCREENING CODES         | VA-WH BREAST TOMOSYNTHESIS SCREENING   |
| VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES  | VA-WH BREAST TOMOSYNTHESIS BILAT       |
| VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES | VA-WH BREAST TOMOSYNTHESIS UNILAT      |

1.  At the “Select Reminder Term” prompt, enter the name of the term listed in the Add Tomosynthesis Findings to Term column in the table above.
2.  At the “Select Finding” prompt, enter the letters found to the right of the equals sign on the line below the name of the finding you are adding (highlighted in gray in the example below), then enter a period and finally, enter the name of the finding.

> Example – Step \#13 Capture Finding

Finding Item: LOCAL DIGITAL BREAST TOMOSYNTHESIS CODES

(FI(2)=<span class="mark">TX</span>(393))

Finding Type: REMINDER TAXONOMY

3.  At the “...OK?” prompt, press the Enter key.
4.  At the “Are you adding '…' as a new FINDINGS” prompt, enter the word YES.
5.  At the “FINDING ITEM” prompt, press the Enter key.
6.  At the “BEGINNING DATE/TIME” prompt, enter T-90.
7.  At the “ENDING DATE/TIME” prompt, enter a caret (^).
8.  Repeat steps b through g for the remaining tomosynthesis-related findings you are adding.

> Example – Adding a Finding to a Term

Select Reminder Term: VA-WH BREAST TOMOSYNTHESIS SCREENING NATIONAL

...OK? Yes// (Yes)

Choose from:

TX VA-WH BREAST TOMOSYNTHESIS SCREENING Finding \# 1

Select Finding: TX.LOCAL DIGITAL BREAST TOMOSYNTHESIS CODES

Searching for a REMINDER TAXONOMY, (pointed-to by FINDING ITEM)

Searching for a REMINDER TAXONOMY

LOCAL DIGITAL BREAST TOMOSYNTHESIS CODES LOCAL

...OK? Yes// (Yes)

Are you adding 'LOCAL DIGITAL BREAST TOMOSYNTHESIS CODES' as

a new FINDINGS (the 2ND for this REMINDER TERM)? No// YES (Yes)

Editing Finding Number: 2

FINDING ITEM: LOCAL DIGITAL BREAST TOMOSYNTHESIS CODES

//

BEGINNING DATE/TIME: T-90

ENDING DATE/TIME: ^

Choose from:

TX LOCAL DIGITAL BREAST TOMOSYNTHESIS CODES Finding \# 2

TX VA-WH BREAST TOMOSYNTHESIS SCREENING Finding \# 1

Select Finding:

9.  At the “Select Finding” prompt, press the Enter key.
10. At the “Press ENTER to continue or '^' to exit” prompt, press the Enter key.
11. At the “Edit?” prompt, enter the word YES.

> Example – Closing the Edit Session

Select Finding:

Checking integrity of the term ...

No fatal term errors were found.

Press ENTER to continue or '^' to exit:

Input your edit comments.

Edit? NO// YES

12. You will now see the Text Editor. Enter a comment. In the example below, the comment is “Added local tomosynthesis-related findings per the CPRS v31b Follow-up Setup and Configuration Guide.”

> Example – Text Editor

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

Added local tomosynthesis-related findings per the CPRS v31b Follow-up

Setup and Configuration Guide.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

13. After you enter a comment, press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.
14. Repeat steps a through l for the remaining reminder terms listed in the Add Tomosynthesis Findings to Term column in the table above.
15. At the “Select Reminder Term” prompt, press the ENTER key.
16. For each term in the table below, use option Add/Edit Reminder Term \[PXRM TERM EDIT\] to remove all tomosynthesis-related findings.

| Term with Tomosynthesis Findings    |
|-----------------------------------------|
| VA-WH MAMMOGRAM SCREENING CODES         |
| VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES  |
| VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES |

1.  At the “Select Reminder Term” prompt, enter the name of the desired term from the table above.
2.  At the “Select Finding” prompt, enter an accent (\`) followed by the number of the tomosynthesis-related finding you need to remove.
3.  At the “FINDING ITEM” prompt, enter an at-sign (@).
4.  At the “SURE YOU WANT TO DELETE THE ENTIRE FINDING ITEM” prompt, enter the word YES.
5.  Repeat steps b through d for the remaining tomosynthesis-related findings you need to remove.

> Example – Removing a Finding from a Term

Select Reminder Term: VA-WH MAMMOGRAM SCREENING CODES NATIONAL

...OK? Yes// (Yes)

Choose from:

TX LOCAL DIGITAL BREAST TOMOSYNTHESIS CODES Finding \# 2

TX VA-WH MAMMOGRAM SCREENING CODES Finding \# 1

Select Finding: \`2 LOCAL DIGITAL BREAST TOMOSYNTHESIS CODES

Editing Finding Number: 2

FINDING ITEM: LOCAL DIGITAL BREAST TOMOSYNTHESIS CODES

// @

SURE YOU WANT TO DELETE THE ENTIRE FINDING ITEM? YES (Yes)

Choose from:

TX VA-WH MAMMOGRAM SCREENING CODES Finding \# 1

Select Finding:

6.  At the “Select Finding” prompt, press the Enter key.
7.  At the “Press ENTER to continue or '^' to exit” prompt, press the Enter key.
8.  At the “Edit?” prompt, enter the word YES.

> Example – Closing the Edit Session

Select Finding:

Checking integrity of the term ...

No fatal term errors were found.

Press ENTER to continue or '^' to exit:

Input your edit comments.

Edit? NO// YES

9.  You will now see the Text Editor. Enter a comment. In the example below, the comment is “Removed local tomosynthesis-related findings per the CPRS v31b Follow-up Setup and Configuration Guide.”

> Example – Text Editor

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

Removed local tomosynthesis-related findings per the CPRS v31b Follow-up

Setup and Configuration Guide.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

10. After you enter a comment, press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.
11. Repeat steps a through j for the remaining reminder terms listed in the Term with Tomosynthesis Findings column in the table above.
12. At the “Select Reminder Term” prompt, press the ENTER key.
17. Use option Add/Edit Reminder Term \[PXRM TERM EDIT\] to add a BEGINNING DATE/TIME value to every finding in the following list of terms:
- VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES
- VA-WH MAMMOGRAM BILAT DIAGNOSTIC CODES
- VA-WH ULTRASOUND BREAST CODES
- VA-WH MRI BREASTS CODES
- VA-WH MAMMOGRAM SCREENING CODES
  1.  At the “Select Reminder Term” prompt, enter the name of the term listed above.
  2.  At the “Select Finding” prompt, enter an accent (\`) followed by the number of the desired finding.
  3.  At the “FINDING ITEM” prompt, press the ENTER key.
  4.  At the “BEGINNING DATE/TIME” prompt, enter T-90.
  5.  At the “ENDING DATE/TIME” prompt, enter a caret (^).
  6.  Repeat steps b through e for every remaining finding.

> Example – Adding a BEGINNING DATE/TIME Value to All Findings

Select Reminder Term Management \<TEST ACCOUNT\> Option: TE Add/Edit Reminder Ter

m

Select Reminder Term: VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES NATIONAL

...OK? Yes// (Yes)

Choose from:

TX LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES Finding \# 2

TX VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES Finding \# 1

Select Finding: \`1 VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES

Editing Finding Number: 1

FINDING ITEM: VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES

//

BEGINNING DATE/TIME: T-90

ENDING DATE/TIME: ^

Choose from:

TX LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES Finding \# 2

TX VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES Finding \# 1

Select Finding: \`2 LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES

Editing Finding Number: 2

FINDING ITEM: LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES

//

BEGINNING DATE/TIME: T-90

ENDING DATE/TIME: ^

Choose from:

TX LOCAL MAMMOGRAM UNILAT DIAGNOSTIC CODES Finding \# 2

TX VA-WH MAMMOGRAM UNILAT DIAGNOSTIC CODES Finding \# 1

7.  At the “Select Finding” prompt, press the ENTER key.
8.  At the “Edit?” prompt, enter YES.

> Example – Closing the Edit Session

Select Finding:

Checking integrity of the term ...

Input your edit comments.

Edit? NO// YES

9.  You will now see the Text Editor. Enter a comment. In the example below, the comment is “Added a beginning date of T-90 to all findings per CPRS v31b Follow-up Setup and Configuration Guide.”

> Example – Text Editor

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

Added a beginning date of T-90 to all findings per CPRS v31b Follow-up

Setup and Configuration Guide.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

10. After you enter a comment, press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.
11. Repeat steps a through j for the remaining reminder terms.
12. At the “Select Reminder Term” prompt, press the ENTER key.
18. Use option Inquire about Reminder Term \[PXRM TERM INQUIRY\] to review the VA-WH NEXT BREAST PROCEDURE reminder term. From the output, compare the condition statement for the VA-WH NEXT BREAST PROCEDURE finding to the value you noted in Section 5.3, step [\#2](#Step_5_3_2). If the condition statements do not match, use option Add/Edit Reminder Term \[PXRM TERM EDIT\] to change the condition statement:
    1.  At the “Select Reminder Term” prompt, enter VA-WH NEXT BREAST PROCEDURE.
    2.  At the “Select Finding” prompt, enter an accent (\`) followed by the number one (1).
    3.  At the “FINDING ITEM” prompt, press the ENTER key.
    4.  At the “BEGINNING DATE/TIME” prompt, press the ENTER key.
    5.  At the “ENDING DATE/TIME” prompt, press the ENTER key.
    6.  At the “OCCURRENCE COUNT” prompt, press the ENTER key.
    7.  At the “COMPUTED FINDING PARAMETER” prompt, press the ENTER key.
    8.  At the “CONDITION: I V("Procedure")\["Mammogram" Replace” prompt, enter three periods (…).
    9.  At the “With” prompt, please contact REDACTED for directions on the appropriate data to enter.
    10. At the “Replace” prompt, press the ENTER key.
    11. At the “CONDITION CASE SENSITIVE” prompt, enter YES.
    12. At the “USE STATUS/COND IN SEARCH:” prompt, enter a caret (^).

> Example – Changing the Condition Statement

Select Reminder Term: VA-WH NEXT BREAST PROCEDURE NATIONAL

...OK? Yes// (Yes)

Choose from:

CF VA-WH NEXT PROCEDURE Finding \# 1

Select Finding: \`1 VA-WH NEXT PROCEDURE

Display help for CF.VA-WH NEXT PROCEDURE? N// O

Editing Finding Number: 1

FINDING ITEM: VA-WH NEXT PROCEDURE//

BEGINNING DATE/TIME: T//

ENDING DATE/TIME:

OCCURRENCE COUNT:

COMPUTED FINDING PARAMETER: BR//

CONDITION: I V("Procedure")\["Mammogram" Replace ... With I ((V("Procedure")\["Mammogram")!(V("Procedure")\["MAMMOGRAM")! (V("Procedure")\["mammogram"))  
  
CONDITION CASE SENSITIVE: YES  
  
USE STATUS/COND IN SEARCH: ^  
  
  
  
Choose from:  
  
CF VA-WH NEXT PROCEDURE Finding \# 1

13. At the “Select Finding” prompt, press the ENTER key.
14. At the “Press ENTER to continue or '^' to exit” prompt, press the ENTER key.
15. At the “Edit” prompt, enter YES.

> Example – Closing the Edit Session

Select Finding:

Checking integrity of the term ...

No fatal term errors were found.

Press ENTER to continue or '^' to exit:

Input your edit comments.

Edit? NO// YES

16. You will now see the Text Editor. Enter a comment. In the example below, the comment is “Reverted the condition statement for the VA-WH NEXT PROCEDURE finding per the CPRS v31b Follow-up Setup and Configuration Guide.”

> Example – Text Editor

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

Reverted the condition statement for the VA-WH NEXT PROCEDURE finding per the CPRS v31b Follow-up Setup and Configuration Guide.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

17. After you enter a comment, press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.
18. At the “Select Reminder Term” prompt, press the ENTER key.
19. Use option Reminder Dialogs \[PXRM DIALOG/COMPONENT EDIT\] to delete the finding item from the VA-WH PT CONTACT:PACT TEAM reminder dialog element:
    1.  At the “Select Item” prompt, enter CV.
    2.  At the “TYPE OF VIEW” prompt, enter E.
    3.  At the “Select Item” prompt, enter SL.
    4.  At the “Search for” prompt, enter VA-WH PT CONTACT:PACT TEAM.
    5.  At the “Find Next ‘VA-WH PT CONTACT:PACT TEAM’” prompt, enter NO.
    6.  At the “Select Item” prompt, enter the number that corresponds with your entry, VA-WH PT CONTACT:PACT TEAM. (In the “Example-Dialog Elements” below, it is 18560.) It will vary by site.

> Example – Dialog Elements

> <u>+Item Dialog Name Dialog type Status \_</u>

> 18560 VA-WH PT CONTACT:PACT TEAM Dialog Element

> 18561 VA-WH PT CONTACT:SECURE MESSAGING Dialog Element

> 18562 VA-WH REFER BIOPSY Dialog Element

> 18563 VA-WH REFER SURGEON Dialog Element

> 18564 VA-WH SMART BR MALE ALERT RESULT Dialog Element

> 18565 VA-WH SMART BR MALE BI-RAD SELECTOR: BI Dialog Element

> 18566 VA-WH SMART BR MALE BI-RAD SELECTOR: BI Dialog Element

> 18567 VA-WH SMART BR MALE BIOPSY ALREADY OBTA Dialog Element

> 18568 VA-WH SMART BR MALE CONSULT Dialog Element

> 18569 VA-WH SMART BR MALE CURRENTLY UNDER TRE Dialog Element

> 18570 VA-WH SMART BR MALE FU MAM 12M Dialog Element

> 18571 VA-WH SMART BR MALE FU MAM 1M Dialog Element

> 18572 VA-WH SMART BR MALE FU MAM 2M Dialog Element

> 18573 VA-WH SMART BR MALE FU MAM 3M Dialog Element

> \+ + Next Screen - Prev Screen ?? More Actions \>\>\>

> AD Add PT List/Print All QU Quit

> CO Copy Dialog INQ Inquiry/Print

> CV Change View TE Dialog Taxonomy Edit

> Select Item: Next Screen// 18560

7.  At the “FINDING ITEM” prompt, enter @.
8.  At the “SURE YOU WANT TO DELETE” prompt, enter YES.
9.  At the “Select ADDITIONAL FINDINGS” prompt, enter ^.
10. At the “Edit” prompt, enter YES.

> Example – Removing the Finding Item

> Dialog Name: VA-WH PT CONTACT:PACT TEAM

> Current dialog element/group name: VA-WH PT CONTACT:PACT TEAM

> Used by: VA-WH GP BR PT CONTACT METHOD (Dialog Group)

> FINDING ITEM: PACT/PC TO NOTIFY// @

> SURE YOU WANT TO DELETE? YES (Yes)

> Select ADDITIONAL FINDINGS: ^

> Checking reminder dialog for errors..

> NO ERRORS FOUND

> Input your edit comments.

> Edit? NO// YES

11. You will now see the Text Editor. Enter a comment. In the example below, the comment is “Removed the PACT/PC TO NOTIFY finding per the CPRS v31b Follow-up Setup and Configuration Guide.”

> Example – Text Editor

==\[ WRAP \]==\[INSERT \]===================\< \>=========\[Press \<PF1\>H for help\]====

Removed the PACT/PC TO NOTIFY finding per the CPRS v31b Follow-up Setup

and Configuration Guide.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

12. After you enter a comment, press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.
13. At the “Select Item” prompt, enter QU.

Installation of the SMART UPDATES reminder content is now complete.

### Install High Risk Medications Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  In the reminder exchange, search for the text, PXRM\*2.0\*71 HI RISK MEDS and then, locate an entry titled PXRM\*2.0\*71 HI RISK MEDS CONTENT.
2.  At the “Select Action” prompt, enter “IFE” for Install Exchange File Entry.
3.  Enter the number that corresponds with your entry, PXRM\*2.0\*71 HI RISK MEDS CONTENT. (In the “Example-Reminder Exchange” below, it is entry 37.) It will vary by site. Make sure you select the item whose “Date Packed” is set to 07/07/2021@16:35:08.

    Example –Reminder Exchange

<u>+Item Entry Source Date Packed \_</u>

37 PXRM\*2.0\*71 HI RISK MEDS CPRSCRM9@CAMP MASTER 07/07/2021@16:35

CONTENT

38 PXRM\*2.0\*71 SMART UPDATES CPRSCRM1@CAMP MASTER 07/07/2021@09:59

39 RT VA-ALCOHOL NONE PAST 1YR CPRSCRM2@NORTHERN CAL 02/03/2009@08:32

40 TIU TEMPLATE URL FIX CPRSCRM3@SALT LAKE CI 06/07/2016@06:18

41 TIU\*1\*112 20040325 CPRSCRM4@ALBANY 03/25/2004@14:20

42 TIU\*1\*242 20080814 CPRSCRM5@ZZ ALBANY-PR 08/14/2008@08:20

43 TIU\*1\*246 20090128 DC/TL CPRSCRM5@SALT LAKE CI 01/28/2009@17:05

44 TIU\*1\*246 20090128 TL CPRSCRM6@SALT LAKE CI 01/28/2009@17:09

45 TX HIGH RISK FLU AND PNEUMONIA CPRSCRM7@NORTHERN CAL 02/09/2009@09:22

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

CFE Create Exchange File Entry LHF Load Host File

CHF Create Host File LMM Load MailMan Message

CMM Create MailMan Message LR List Reminder Definitions

DFE Delete Exchange File Entry LWH Load Web Host File

IFE Install Exchange File Entry RI Reminder Definition Inquiry

IH Installation History RP Repack

Select Action: Next Screen// IFE Install Exchange File Entry

Enter a list or range of numbers (1-334): 37

4.  At the “Select Action” prompt, enter “IA” for Install All Components.

> Example –Install All Components

<u>Component Category Exists\_</u>

Source: CPRSCRM9,NINE at CAMP MASTER

Date Packed: 07/07/2021@16:35:08

Package Version: 2.0P42

Description:

The following Clinical Reminder items were selected for packing:

REMINDER ORDER CHECK ITEMS GROUP

VA-WH HIRISK MEDICATIONS (LACTATION LEVEL 1) GROUP

VA-WH HIRISK MEDICATIONS (MOD/HIGH RISK DURING PREGNANCY) GROUP

VA-WH HIRISK MEDICATIONS (EXTREME RISK) GROUP

VA-WH HIRISK MEDICATIONS (LACTATION LEVEL 2) GROUP

VA-WH HIRISK MEDICATIONS (MODERATE/HIGH RISK) GROUP

REMINDER DIALOG

VA-WH UPDATE LACTATION STATUS

VA-WH UPDATE PREGNANCY STATUS

\+ Enter ?? for more actions \>\>\>

IA Install all Components IS Install Selected Component

Select Action: Next Screen// IA

5.  The general rules for component installation are as follows:
    1.  If a component does not exist (it is NEW), select the Install action.
    2.  If a component does exist (it is DIFFERENT), select the Overwrite the current entry action.

> For the following reminder terms, select the Skip action:

1.  VA-WH PREGNANCY TEST ORDERED
2.  VA-WH POSITIVE LAB PREGNANCY TEST
3.  VA-WH NEGATIVE LAB PREGNANCY TEST

> For all reminder order check items group entries, select the Update action. If a finding does not exist, select the Delete action to continue the installation.

> NOTE: For test systems, you may safely ignore these missing findings. For production systems, after this section is complete, contact the Enterprise Service Desk for assistance in determining why each finding is missing and how to populate it. At this point, the dialog installations begin. Install the FIRST reminder dialog:

3.  At the “Select Action” prompt, enter “IA” for Install All. It will install the dialog VA-WH UPDATE PREGNANCY STATUS.
4.  At the “Install reminder dialog and all components with no further changes” prompt, enter “Yes”.

> Example –Install VA-WH UPDATE PREGNANCY STATUS dialog

Packed reminder dialog: VA-WH UPDATE PREGNANCY STATUS

<u>Item Seq. Dialog Findings Type Exists\_</u>

1 VA-WH UPDATE PREGNANCY STATUS dialog X

2 2 VA-WH TD PREGNANCY DOCUMENTATION NEEDED\* group X

Finding: \*NONE\*

3 2.2 VA-WH TD PREGNANCY CONTRA RESOURCES element X

Finding: \*NONE\*

4 2.5 VA-WH TD PREGNANCY STATUS ACTION PROMPT\* group X

Finding: \*NONE\*

5 2.5.5 VA-WH TD PREGNANCY STATUS EDIT RECORD\* group X

Finding: WH-TD PREGNANCY EDIT RECORD (REMINDER GENERAL X

FINDING)

Add. Finding: WH-PREGNANCY DATA SOURCE (REMINDER GENERAL X

FINDING)

6 2.5.5.5 VA-WH TD PREGNANCY ENDED HISTORICAL group X

Finding: \*NONE\*

\+ + Next Screen - Prev Screen ?? More Actions

DD Dialog Details DT Dialog Text IS Install Selected

DF Dialog Findings DU Dialog Usage QU Quit

DS Dialog Summary IA Install All

Select Action: Next Screen// IA

6.  Respond to the prompts on how you want to handle the first non-existent finding, Q.EMERGENCY CONTRACEPTIVE QUICK ORDER:
    1.  At the “Enter response” prompt, enter “P” for Replace with an existing entry.
    2.  At the “Select ORDER DIALOG NAME” prompt, enter the name of the first finding you recorded in Section 5.4, Step [\#1a](#Step3a).
7.  Respond to the prompts on how you want to handle the second non-existent finding Q.PREGNANCY TEST QUICK ORDER:
    1.  At the “Enter response” prompt, enter “P” for Replace with an existing entry.
    2.  At the “Select ORDER DIALOG NAME” prompt, enter the name of the first finding you recorded in Section 5.4, Step [\#1b](#Step3b).
8.  After the dialog installation completes, you will see the Dialog Components screen. At the “Select Action” prompt, enter “QU” for Quit.

> Example –Dialog Components screen

Packed reminder dialog: VA-WH UPDATE PREGNANCY STATUS

<u>Item Seq. Dialog Findings Type Exists\_</u>

1 VA-WH UPDATE PREGNANCY STATUS dialog X

2 2 VA-WH TD PREGNANCY DOCUMENTATION NEEDED\* group X

Finding: \*NONE\*

3 2.2 VA-WH TD PREGNANCY CONTRA RESOURCES element X

Finding: \*NONE\*

4 2.5 VA-WH TD PREGNANCY STATUS ACTION PROMPT\* group X

Finding: \*NONE\*

5 2.5.5 VA-WH TD PREGNANCY STATUS EDIT RECORD\* group X

Finding: WH-TD PREGNANCY EDIT RECORD (REMINDER GENERAL X

FINDING)

Add. Finding: WH-PREGNANCY DATA SOURCE (REMINDER GENERAL X

FINDING)

6 2.5.5.5 VA-WH TD PREGNANCY ENDED HISTORICAL group X

Finding: \*NONE\*

\+ + Next Screen - Prev Screen ?? More Actions

DD Dialog Details DT Dialog Text IS Install Selected

DF Dialog Findings DU Dialog Usage QU Quit

DS Dialog Summary IA Install All

Select Action: Next Screen// QU

9.  Install the SECOND reminder dialog:
    1.  At the “Select Action” prompt, enter “IA” for Install All. It will install the dialog VA-WH UPDATE LACTATION STATUS.
    2.  At the “Install reminder dialog and all components with no further changes” prompt, enter “Yes”.

        Example –Install VA-WH UPDATE LACTATION STATUS dialog

Packed reminder dialog: VA-WH UPDATE LACTATION STATUS

<u>Item Seq. Dialog Findings Type Exists\_</u>

1 VA-WH UPDATE LACTATION STATUS dialog X

2 2 VA-WH TD LACTATION DOCUMENTATION NEEDED\* group X

Finding: \*NONE\*

3 2.5 VA-WH TD LACTATION STATUS ACTION PROMPT\* group X

Finding: \*NONE\*

4 2.5.5 VA-WH TD LACTATION STATUS EDIT RECORD\* group X

Finding: WH-TD LACTATION EDIT RECORD (REMINDER GENERAL X

FINDING)

Add. Finding: WH-LACTATION DATA SOURCE (REMINDER GENERAL X

FINDING)

5 2.5.5.5 VA-WH TD LACTATION STATUS EDIT group X

Finding: \*NONE\*

6 2.5.5.5.1 VA-WH TD LACTATION STATUS YES group X

Finding: PATIENT IS LACTATING (REMINDER GENERAL FINDING) X

\+ + Next Screen - Prev Screen ?? More Actions

DD Dialog Details DT Dialog Text IS Install Selected

DF Dialog Findings DU Dialog Usage QU Quit

DS Dialog Summary IA Install All

Select Action: Next Screen// IA

10. After the dialog installation completes, you will see the Dialog Components screen. At the “Select Action” prompt, enter “QU” for Quit.

    Example –Dialog Components screen

Packed reminder dialog: VA-WH UPDATE LACTATION STATUS

<u>Item Seq. Dialog Findings Type Exists\_</u>

1 VA-WH UPDATE LACTATION STATUS dialog X

2 2 VA-WH TD LACTATION DOCUMENTATION NEEDED\* group X

Finding: \*NONE\*

3 2.5 VA-WH TD LACTATION STATUS ACTION PROMPT\* group X

Finding: \*NONE\*

4 2.5.5 VA-WH TD LACTATION STATUS EDIT RECORD\* group X

Finding: WH-TD LACTATION EDIT RECORD (REMINDER GENERAL X

FINDING)

Add. Finding: WH-LACTATION DATA SOURCE (REMINDER GENERAL X

FINDING)

5 2.5.5.5 VA-WH TD LACTATION STATUS EDIT group X

Finding: \*NONE\*

6 2.5.5.5.1 VA-WH TD LACTATION STATUS YES group X

Finding: PATIENT IS LACTATING (REMINDER GENERAL FINDING) X

\+ + Next Screen - Prev Screen ?? More Actions

DD Dialog Details DT Dialog Text IS Install Selected

DF Dialog Findings DU Dialog Usage QU Quit

DS Dialog Summary IA Install All

Select Action: Next Screen// QU

11. You will now see the Exchange File Components screen. At the “Select Action” prompt, enter “Q” for Quit.

> Example –Dialog Components screen

<u>Component Category Exists\_</u>

Source: CPRSCRM9,NINE at CAMP MASTER

Date Packed: 07/07/2021@16:35:08

Package Version: 2.0P42

Description:

The following Clinical Reminder items were selected for packing:

REMINDER ORDER CHECK ITEMS GROUP

VA-WH HIRISK MEDICATIONS (MOD/HIGH RISK DURING PREGNANCY) GROUP

VA-WH HIRISK MEDICATIONS (EXTREME RISK) GROUP

VA-WH HIRISK MEDICATIONS (MODERATE/HIGH RISK) GROUP

REMINDER DIALOG

VA-WH TD LACTATION DO NOTHING SRN

VA-WH TD PREGNANCY PLACE ORDERS GROUP

VA-WH TD PREGNANCY DO NOTHING SRN

VA-WH TD PREGNANCY CONTRA CURRENT PARTNER

\+ + Next Screen - Prev Screen ?? More Actions \>\>\>

IA Install all Components IS Install Selected Component

Select Action: Next Screen// Q

Installation of the Women’s Health High Risk Medications reminder content is now complete.

## Enable Clinical Reminder Order Check Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This step must be performed by the site’s CAC.

After CPRS v31b was installed, Pharmacy Benefits Management (PBM) and Women’s Health (WH) recommended that sites disable the reminder order check rules for medications classified as Lactation Level 2.

But that recommendation has been rescinded because the CPRS v31b Follow-up Build is now installed. Thus, sites must now activate the following order check rules:

- VA-WH HIRISK MEDS (LACT 2) EXPIRED DOC RULE
- VA-WH HIRISK MEDS (LACT 2) RULE

To activate the order check rules, do the following:  

1.  On the Reminder Managers Menu screen, enter “ROC” for Reminder Order Check Menu.  
      
    Example – Reminder Managers Menu

Select Core Applications \<TEST ACCOUNT\> Option: REMINDER MANagers Menu

   CF     Reminder Computed Finding Management ...

   RM     Reminder Definition Management ...

   SM     Reminder Sponsor Management ...

   TXM    Reminder Taxonomy Management

   TRM    Reminder Term Management ...

   LM     Reminder Location List Management ...

   RX     Reminder Exchange

   RT     Reminder Test

   OS     Other Supporting Menus ...

   INFO   Reminder Information Only Menu ...

   DM     Reminder Dialog Management ...

   CP     CPRS Reminder Configuration ...

   RP     Reminder Reports ...

   MST    Reminders MST Synchronization Management ...

   PL     Reminder Patient List Menu ...

   PAR    Reminder Parameters ...

   VS     NLM Value Set Menu

   ROC    Reminder Order Check Menu ...

   CQM    NLM Clinical Quality Measures Menu

   XM     Reminder Extract Menu ...

   GEC    GEC Referral Report

Select Reminder Managers Menu \<TEST ACCOUNT\> Option: ROC  Reminder Order Check Menu

2.  On the Reminder Order Check Menu screen, enter “RE” for Add/Edit Reminder Order Check Rule.

Example – Reminder Order Check Menu screen

   GE     Add/Edit Reminder Order Check Items Group

   GI     Reminder Order Check Items Inquiry

   RE     Add/Edit Reminder Order Check Rule

   RI     Reminder Order Check Rule Inquiry

   TEST   Reminder Order Check Test

Select Reminder Order Check Menu \<TEST ACCOUNT\> Option: RE  Add/Edit Reminder Order Check Rule

3.  When prompted with “Select Reminder Order Check Rule By”, enter “N” for Order Check Rule Name.
4.  When prompted again with “Select Reminder Order Check Rule By”, enter “VA-WH HIRISK MEDS (LACT 2) EXPIRED DOC RULE”.  
      
    Example – “Select Reminder Order Check Rule By” prompts

Select Reminder Order Check Rule by one of the following:

N: ORDER CHECK RULE NAME

R: REMINDER DEFINITION

T: REMINDER TERM

Q: QUIT

Select Reminder Order Check Rule by: (N/R/T/Q): N// \<Enter\> ORDER CHECK RULE NAME

Select Reminder Order Check Rule: VA-WH HIRISK MEDS (LACT 2) EXPIRED DOC RULE

5.  You will now see a screen with “Rule Name: VA-WH HIRISK MEDS (LACT 2) EXPIRED DOC RULE”. When prompted with “Status”, enter “P” for Prod and hit the Tab key.  
      
    Example – “Status” prompt

RULE NAME: VA-WH HIRISK MEDS (LACT 2) EXPIRED DOC RULE

DISPLAY NAME: Known or Potential Unsafe Medication (FDB Lactation Level 2)

STATUS: P

CLASS: NATIONAL

SPONSOR: Women Veterans Health Program

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

I=INACTIVE, P=PRODUCTION, T=TESTING

Press \<PF1\>H for help Insert

6.  When prompted with “Command”, enter “S” for Save.  
      
    Example – Entering “S” for Save

RULE NAME: VA-WH HIRISK MEDS (LACT 2) EXPIRED DOC RULE

DISPLAY NAME: Known or Potential Unsafe Medication (FDB Lactation Level 2)

STATUS: PROD

CLASS: NATIONAL

SPONSOR: Women Veterans Health Program

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: S Press \<PF1\>H for help Insert

7.  When prompted again with “Command”, enter “E” for Exit.  
      
    Example – Entering “E” for Exit

RULE NAME: VA-WH HIRISK MEDS (LACT 2) EXPIRED DOC RULE

DISPLAY NAME: Known or Potential Unsafe Medication (FDB Lactation Level 2)

STATUS: PROD

CLASS: NATIONAL

SPONSOR: Women Veterans Health Program

REVIEW DATE:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: E Press \<PF1\>H for help Insert

8.  You will now see the Edit History screen. When prompted with “Edit Comments”, press the \<Enter\> key.  
      
    Example – Edit History screen

Edit History

Edit by: ADPAC,ONE on 01/13/2020@09:40:03

EDIT COMMENTS:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Press enter to add a description of the changes made.

Press \<PF1\>H for help Insert

9.  You will now see the Text Editor. Enter a comment. In the example below, the comment is “Changed the rule’s status to production.”  
      
    Example – Text Editor

==\[ WRAP \]==\[INSERT \]=============\< EDIT COMMENTS \>==\[Press \<PF1\>H for help\]===

Changed the rule's status to production.

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>=====

10. After you enter a comment, press the keyboard key that is mapped to PF1 (either the NUM LOCK key on the keypad or the F1 key) and then, immediately press the E key to exit the text editor.
11. On the Edit History screen, when prompted with “Command”, enter “E” for Exit.  
      
    Example – Edit History screen after a comment has been added

Edit History

Edit by: ADPAC,ONE on 01/13/2020@09:40:03

EDIT COMMENTS: Changed the rule's status to active.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: E Press \<PF1\>H for help Insert

12. To activate the VA-WH HIRISK MEDS (LACT 2) RULE, repeat steps \#3 through \#11.

## Link Reminder Terms to Women’s Health Procedure Type Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This step must be performed either by the site’s CAC or the site’s ITOPS VistA installer, depending on who has FileMan read/write access to the WV PROCEDURE TYPE file (#790.2).

To link Reminder Terms to Women’s Health Procedure Type Entries:

1.  In FileMan, select the “ENTER OR EDIT FILE ENTRIES \[DIEDIT\]” option.
2.  At the Input to what File: prompt, select “790.2”.
3.  At the EDIT WHICH FIELD: prompt, select “Reminder Term”.
4.  At the THEN EDIT FIELD: prompt, press the \<enter\> key.
5.  Enter the Reminder Term value for the corresponding Women’s Health Procedure entries.

| WV Procedure Type          | Reminder Term                    |
|--------------------------------|--------------------------------------|
| BREAST TOMOSYNTHESIS BILAT     | VA-WH BREAST TOMOSYNTHESIS BILAT     |
| BREAST TOMOSYNTHESIS SCREENING | VA-WH BREAST TOMOSYNTHESIS SCREENING |
| BREAST TOMOSYNTHESIS UNILAT    | VA-WH BREAST TOMOSYNTHESIS UNILAT    |

> Example

VA FileMan 22.2

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: IMAGING TYPE// 790.2 WV PROCEDURE TYPE

(31 entries)

EDIT WHICH FIELD: ALL// reminder term

THEN EDIT FIELD:

Select WV PROCEDURE TYPE: BREAST TOMOSYNTHESIS BILAT

REMINDER TERM: VA-WH BREAST TOMOSYNTHESIS BILAT NATIONAL

...OK? Yes// (Yes)

# Verify Successful Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At this point, sites may use a locally developed smoke test script to verify that the installation and configuration were successful.