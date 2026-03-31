---
title: PXRM*2*8 TBI Screening Reminder Installation and Setup Guide
doc_type: SG-SET
doc_label: Setup Guide
doc_layer: patch
doc_subject: TBI Screening Reminder Installation and
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*8
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 1
description: > PXRM\2\8 distributes the new National VA-TBI SCREENING reminder definition and dialog. This reminder has been developed and sponsored by the Office of Patient Care Services.
audience: 
keywords: 
  - blockquote
  - reminder
  - dialog
  - table
  - style
  - width
  - colgroup
  - thead
  - class
  - tbody
page_count: 0
word_count: 1904
section_count: 3
table_count: 2
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: March 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_8_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_8_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-8-tbi-screening-reminder-installation-and-setup-guide/001.png)

# Traumatic Brain Injury (TBI) Screening Reminder 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Traumatic Brain Injury (TBI) Screening Reminder](#traumatic-brain-injury-tbi-screening-reminder)
  - [INSTALLATION & SETUP GUIDE](#installation-setup-guide)
    - [Contents](#contents)
    - [Introduction](#introduction)
    - [Pre-Installation](#pre-installation)
    - [Installation](#installation)
  - [<u>Setup of TBI Dialog</u>](#usetup-of-tbi-dialogu)
- [<u>Appendices</u>](#uappendicesu)
> PXRM\*2\*8

## INSTALLATION & SETUP GUIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> March 2007

> Health Provider Systems Department of Veterans Affairs

### Contents 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  [Retrieve the PXRM\*2.0\*8 build 3](#installation)
2.  [Install the build first in a training or test account. 3](#installation)
3.  [Load the distribution. 3](#installation)
    1.  [Verify Checksums in Transport Global 3](#installation)
    2.  [Print Transport Global 4](#print-transport-global)
4.  [Install the package. 4](#print-transport-global)
6.  [Install File Print (optional) 6](#install-file-print-optional)
7.  [Build File Print (optional) 6](#install-file-print-optional)
8.  [Post-installation routine 6](#install-file-print-optional)
[SETUP OF TBI DIALOG 7](#setup-of-tbi-dialog)
1.  [Mapping a site-specific quick order 8](#_bookmark6)
2.  [Add the nationally distributed reminders to the CPRS Cover Sheet 10](#_bookmark7)
3.  [Verify that the dialog functions properly 11](#_bookmark8)
> ii Clinical Reminders TBI Screening Patch PXRM\*2\*8 3/20/2007
> Installation and Setup Guide

### Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PXRM\*2\*8 distributes the new National VA-TBI SCREENING reminder definition and dialog. This reminder has been developed and sponsored by the Office of Patient Care Services.

#### Web Sites:

> [<u>http://vaww1.va.gov/pcs/</u>](http://vaww1.va.gov/pcs/) VHA Patient Care Services (PCS) [<u>http://vista.med.va.gov/reminders</u>](http://vista.med.va.gov/reminders) National Clinical Reminders site

> For more detailed information about use of this TBI Screening reminder, please review the PowerPoint at: [<u>http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-</u>](http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-07.ppt) [<u>07.ppt</u>](http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-07.ppt)

### Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Clinical Reminders patch PXRM\*2.0\*8 adds one new reminder and dialog, along with taxonomies, reminder terms, and health factors to support the TBI project.

#### Required Software

| Package/Patch  | Namespace | Version | Comments  |
|--------------------|---------------|-------------|---------------|
| Clinical Reminders | PXRM          | 2.0         | Fully patched |
| HL7                | HL            | 1.6         | Fully patched |
| Kernel             | XU            | 8.0         | Fully patched |
| MailMan            | XM            | 7.1         | Fully patched |
| VA FileMan         | DI            | 22          | Fully patched |

#### File installed

8.  REMINDER EXCHANGE

#### Data is added to the following files:

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>801.41</th>
<th><blockquote>
<p>REMINDER DIALOG</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>811.5</td>
<td><blockquote>
<p>REMINDER TERM</p>
</blockquote></td>
</tr>
<tr class="even">
<td>811.9</td>
<td><blockquote>
<p>REMINDER DEFINITION</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Routine Installed

> PXRMP8I

#### Estimated Installation Time

> This patch can be loaded with users on the system. Installation will take less than two minutes. Installation should be coordinated with the person who manages Clinical Reminders at your site and be scheduled during a time of lower system usage.

### Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This build can be loaded with users on the system. Updating of cross-references for the new data added to the files will occur during the install.

> *The install needs to be done by a person with DUZ(0) set to "@."*

#### Retrieve the PXRM\*2.0\*8 build

> Use FTP to access the build, PXRM_2_0_8.KID, from one of the following locations:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>Albany</th>
<th><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></th>
<th><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Hines</td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="even">
<td>Salt Lake City</td>
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

> In programmer mode, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, then the option LOAD a Distribution. Enter your directory name and PXRM_2_0_8.KID at the Host File prompt.

#### Example

> From the Installation menu, you may elect to use the following options:

#### Verify Checksums in Transport Global

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.

> Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

#### Print Transport Global

> This option will allow you to view the components of the KIDS build.

#### Install the package.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the package PXRM\*2.0\*8 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompts:

> Want KIDS to INHIBIT LOGONs during install? YES// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> NOTE: Do NOT queue the installation, because this installation may contain a question requiring a response and queuing will stop the installation. (If for some reason, your site doesn’t have GMRCOR CONSULT finding item, you’ll be prompted to enter an existing Order Dialog name.)

#### Installation Example

<table style="width:100%;">
<colgroup>
<col style="width: 71%" />
<col style="width: 26%" />
<col style="width: 2%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><p>811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.</p>
<p>Want KIDS to INHIBIT LOGONs during the install? YES// NO</p>
<p>Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO</p>
<p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt.</p></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Enter a '^' to abort the install.</p>
<p>DEVICE: HOME// HOME</p>
<p>Complete PXRM*2.0*8</p>
<blockquote>
<p>Install Started for PXRM*2.0*8 :</p>
<p>Mar 07, 2007@15:51:40</p>
</blockquote></td>
<td><blockquote>
<p>Do NOT queue the installation, because this installation may contain a question requiring a response and queuing will stop the installation.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><p>Build Distribution Date: Mar 07, 2007</p>
<blockquote>
<p>Installing Routines:</p>
<p>Mar 07, 2007@15:51:40</p>
<p>Running Pre-Install Routine: PRE^PXRMP8I Installing Data Dictionaries:</p>
</blockquote>
<p>Mar 07, 2007@15:51:40</p>
<blockquote>
<p>Installing Data:</p>
<p>Mar 07, 2007@15:51:40</p>
</blockquote>
<p>Running Post-Install Routine: POST^PXRMP8I Installing reminder VA-TBI SCREENING</p>
<blockquote>
<p>Updating Routine file... Updating KIDS files...</p>
<p>PXRM*2.0*8 Installed.</p>
<p>Mar 07, 2007@15:51:47</p>
</blockquote>
<p>Install Message sent #42971 Install Completed</p></td>
<td></td>
</tr>
</tbody>
</table>

#### Install File Print (optional)

> Use the KIDS Install File Print option to print out the results of the installation process.

#### Build File Print (optional)

> Use the KIDS Build File Print option to print out the build components.

#### Post-installation routine

> The post-install routine, POST^PXRMP8I, installs the “packed” components of the VA- TBI SCREENING reminder and VA-TBI SCREENING reminder dialog onto your system, via reminder exchange tools. The reminder exchange entry being installed is called VA- TBI-SCREENING.

> After the installation has finished, if you discover that the components weren’t installed correctly for some reason, you can use the Exchange options on the Reminders Manager Menu to install the components of the “packed” reminder.

> The init routine PXRMP8I may be deleted once the installation has completed. Sites should use the Kernel “Delete Routines” option \[XTRDEL\] to delete this routine.

## <u>Setup of TBI Dialog</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The TBI reminder is applicable to all patients whose last service separation date is after 9/11/01 and to active duty patients.

> NOTE: This reminder uses the same reminder term that was included in the VA-IRAQ & AFGHAN POST-DEPLOY SCREEN reminder to determine whether active duty patients should be screened or not. The reminder term VA-ACTIVE DUTY is included in this reminder and is available to cause patients to be part of the cohort. This term contains the computed finding

> VA-PATIENT TYPE, which can be used to include active duty patients. Sites that do not screen active duty patients may remove the computed finding from this reminder term.

> This reminder is resolved if the patient did not serve in OEF/OIF, as recorded by using this reminder dialog or the VA-IRAQ & AFGHAN POST-DEPLOY SCREEN dialog. Therefore, the denominator for this reminder is the same as that used for the VA-IRAQ & AFGHAN POST- DEPLOY SCREEN – this number DOES NOT represent the number of patients who served in OEF/OIF. Please note that this reminder and the VA-IRAQ & AFGHAN POST-DEPLOY SCREEN reminder are not constructed to run reports on those patients who actually served in OEF/OIF.

- NOTE: Some local sites use additional reminders that have more appropriate denominators and look at patients with known OEF/OIF service who need TBI screening, or who screened positive for TBI and need follow-up, or have positive PTSD screens or positive depression screens.

> When a veteran’s screen is positive, the positive findings should be reviewed with the patient by an appropriately trained clinician and a consult for further evaluation recommended. In general, it is best if the clinician personally completes the screen, particularly as the questions asked are of clinical value. If clinic support staff collects answers to the initial questions on the screen, positive screens must be brought to the attention of the responsible clinician immediately and reviewed with the patient. Consults should not be automatically submitted without discussion between clinician and the patient.

#### Setup Steps

> After installing Patch 8, follow the steps below to implement your TBI screening reminder and dialog.

> The following dialog elements are meant to be used for ordering a consult to the team at your facility that does further evaluation of patients with possible TBI.

> VA-TBI OI CONSULT FOR KNOWN TBI VA-PDIQ POLYTRAUMA CONSULT

> <span id="_bookmark6" class="anchor"></span>At the time of install, the Reminder Dialog will use the GMRCOR CONSULT finding item as the consult order dialog for both of these dialog elements. Sites should substitute a quick order or an order menu for ordering consults to the TBI team at your facility. If no such service is available yet, then sites may wish to leave the GMRCOR CONSULT in the element until a consult becomes available.

> The mapping of the Quick Order should be done by the site Clinical Reminder Manager.

#### Mapping a site-specific quick order

> To map a site-specific quick order to the above elements, do the following from the Reminder Managers menu.

#### Summary of steps:

1.  Select DM Reminder Dialog Management.
2.  Select DI Reminder Dialogs.
3.  Type CV for Change View.
4.  Type E for Dialog Elements.
5.  Type SL for Search List.
6.  Type the name of the element from above.
7.  At the Find Next prompt, type No.
8.  Type the item number next to the dialog element, VA-TBI OI CONSULT FOR KNOWN TBI.
9.  At the finding Item Prompt, enter Q. plus the name of the site-specific Quick Order or order menu.
10. Press Enter at the Additional Finding prompt.
11. Repeat the above steps for the other dialog element, VA-PDIQ POLYTRAUMA CONSULT

#### Detailed Example

1.  Select DM Reminder Dialog Management from the Reminder Managers Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION NAME: PXRM MANAGERS MENU Reminder Managers Menu menu</p>
<blockquote>
<p>CF Reminder Computed Finding Management ... RM Reminder Definition Management ...</p>
<p>SM Reminder Sponsor Management ... TXM Reminder Taxonomy Management ... TRM Reminder Term Management ...</p>
<p>LM Reminder Location List Management ... RX Reminder Exchange</p>
<p>RT Reminder Test</p>
<p>OS Other Supporting Menus ...</p>
<p>INFO Reminder Information Only Menu ... DM Reminder Dialog Management ...</p>
<p>CP CPRS Reminder Configuration ... RP Reminder Reports ...</p>
<p>MST Reminders MST Synchronization Management ... PL Reminder Patient List Menu ...</p>
<p>PAR Reminder Parameters ...</p>
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
<p>XM Reminder Extract Menu ... GEC GEC Referral Report</p>
</blockquote>
<p>Select Reminder Managers Menu Option: DM Reminder Dialog Management</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  Select DI Reminder Dialogs

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>DP Dialog Parameters ... DI Reminder Dialogs</p>
<p>DR Dialog Reports ...</p>
<p>IA Inactive Codes Mail Message</p>
</blockquote>
<p>Select Reminder Dialog Management Option: DI Reminder Dialogs</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Type CV for Change View.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 11%" />
<col style="width: 2%" />
<col style="width: 13%" />
<col style="width: 22%" />
<col style="width: 6%" />
<col style="width: 15%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="8"><p>Dialog List Mar 07, 2007@16:03:23 Page: 1 of 27 REMINDER VIEW (ALL REMINDERS BY NAME)</p>
<blockquote>
<p>Item Reminder Name Linked Dialog Name &amp; Dialog Status</p>
</blockquote>
<ol type="1">
<li><p>01-DIAB PTS (5Y) W/O DIAB EXAM (1Y</p></li>
<li><p>10-DIAB PTS (5Y) W/O DIAB EXAM (1Y</p></li>
<li><p>21-DIAB PTS (5Y) W/O DIAB EXAM (1Y</p></li>
<li><p>691 PNT EYE CLINIC PNT EYE DIABETES-DLG</p></li>
<li><p>A NEW REMINDER A NEW REMINDER Disabled</p></li>
<li><p>AGETEST VA-HEPC AUTOGENERATE TEST</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>+</td>
<td><blockquote>
<p>Enter</p>
</blockquote></td>
<td>??</td>
<td colspan="2">for more actions</td>
<td></td>
<td></td>
<td><blockquote>
<p>&gt;&gt;&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><p>AR All reminders CV Change View</p>
<p>Select Item: Next</p></td>
<td><blockquote>
<p>LR RN</p>
</blockquote>
<p>Screen// CV</p></td>
<td><p>Linked Reminders Name/Print Name</p>
<blockquote>
<p>Change View</p>
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

4.  Type E, for Dialog Elements

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
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
<p>RG Result Group (Mental Health) RE Result Element (Mental Health)</p>
</blockquote>
<p>TYPE OF VIEW: R// E Dialog Elements</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

5.  Type SL for Search List.
6.  Type the name of the dialog element, VA-TBI OI CONSULT FOR KNOWN TBI.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Item: Next Screen// SL SL</p>
<p>Search for: VA-TBI OI CONSULT FOR KNOWN TBI</p></th>
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
<th><ol start="15" type="1">
<li><p><span id="_bookmark7" class="anchor"></span>ADDITIONAL COMMENTS (PXRM COMMENT) Dialog Element</p></li>
<li><p>ADDITIONAL COMMENTS(2 LINES WP) Dialog Element</p></li>
</ol>
<p>...searching for 'VA-TBI OI CONSULT FOR KNOWN TBI'................</p>
<p>Find Next 'VA-TBI OI CONSULT FOR KNOWN TBI'? Yes// NO</p>
<p>CO Copy Dialog PT List/Print All QU Quit</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

8.  Type the item number next to the element, then press Enter

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Dialog List Mar 07, 2007@16:04:22 Page: 102 of 115 DIALOG VIEW (DIALOG ELEMENTS)</p>
<p>+Item Dialog Name Dialog type Status</p>
<p>162 VA-TBI OI CONSULT FOR KNOWN TBI Dialog Element</p>
<p>162 VA-TBI SCREEN REFUSAL Dialog Element</p>
<p>162 VA-TEXT AIMS INSTRUCTION Dialog Element</p>
<p>162 VA-TEXT AIMS INSTRUCTION (1) Dialog Element</p>
<p>162 VA-TEXT BLANK LINE Dialog Element</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>+ + Next Screen - Prev Screen ?? More Actions &gt;&gt;&gt;</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>AD Add CV Change View INQ Inquiry/Print CO Copy Dialog PT List/Print All QU Quit</p>
<p>Select Item: Next Screen// 162</p>
<p>Dialog Name: <strong>VA-TBI OI CONSULT FOR KNOWN TBI</strong></p>
<p>Current dialog element/group name: VA-TBI OI CONSULT FOR KNOWN TBI Used by: VA-TBI TEXT PREVIOUS DX NO SCREEN (Dialog Group)</p></td>
</tr>
</tbody>
</table>

9.  At the finding Item Prompt, enter Q. plus the name of the site-specific Quick Order or order menu.

| FINDING ITEM: GMRCOR CONSULT// Q.ZGMRC TBI |
|------------------------------------------------|

10. Press Enter at the Additional Finding prompt.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select ADDITIONAL FINDINGS: <strong>&lt;Enter&gt;</strong></p>
<p>Input your edit comments. Edit? NO//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

11. Repeat the above steps for the other dialog element, VA-PDIQ POLYTRAUMA CONSULT

#### Add the nationally distributed reminders to the CPRS Cover Sheet

1.  Open a patient chart, click on the reminders clock, and when the available Reminders window opens, click on Action, and then select “Edit Cover Sheet Reminder List.”
2.  When the Cover Sheet Reminder List opens, find the TBI screening reminder.

> ![](pxrm-2-8-tbi-screening-reminder-installation-and-setup-guide/002.png)

3.  <span id="_bookmark8" class="anchor"></span>Click on the TBI Screening (VA-TBI SCREENING) reminder and click the Add button (or double-click the reminder).

#### Verify that the dialog functions properly

> Test the TBI Reminder dialog in CPRS and verify the following:

- Correct Progress Note text is posted
- Finding Item gets sent to PCE
- Reminder is satisfied

> Check the Clinical Maintenance component display in CPRS after testing the dialog to ensure that all the activities are reflected in the clinical maintenance display.

> ![](pxrm-2-8-tbi-screening-reminder-installation-and-setup-guide/003.png)

# <u>Appendices</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Appendix A: VA-TBI SCREENING Reminder Inquiry

> Appendix B: VA-TBI SCREENING reminder dialog screen shots

#### Appendix A: Reminder Definition Inquiry

> Select Reminder Definition: TBI Screening VA-TBI SCREENING NATIONAL DEVICE: ;;999 HOME

> REMINDER DEFINITION INQUIRY Mar 07, 2007 2:03:47 pm Page 1

> VA-TBI SCREENING No. 793

> Print Name: TBI Screening

> Class: NATIONAL

> Sponsor: Office of Patient Care Services Review Date:

> Rescission Date:

> Usage: CPRS, DATA EXTRACT, REPORTS

> Related VA-\* Reminder:

> Reminder Dialog: VA-TBI SCREENING Priority:

> Reminder Description:

> Reminder is applicable once in a lifetime of all patients whose date of separation from the service is 9/11/01 or later and have had service in OEF/OIF. If Service Date of Separation is more recent than last TBI Screening, then reminder will be due again for patient.

> Reminder is resolved by completing the screen.

> Reminder creation requested by the Office of Patient Care Services. Designed by the TBI Screening Workgroup chaired by Dr. Barbara Sigford and based on a reminder from Minneapolis built by Ronald Patire.

> Technical Description:

> Reminder is due for all patients with DOS of 9/11/01 or later. Reminder is resolved by any of the health factors associated with the responses of section 1; OR health factor for Previous TBI Diagnosis; OR health factor TBI PT Refused..

> Baseline Frequency:

> Do In Advance Time Frame: Wait until actually DUE Sex Specific:

> Ignore on N/A:

> Frequency for Age Range: 99Y - Once for all ages Match Text:

> No Match Text:

> Findings:

> ---- Begin: VA-IRAQ/AFGHAN PERIOD OF SERVICE (FI(1)=RT(490)) ------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: AND

> Beginning Date/Time: 09/11/2001

> Not Found Text: The patient's last service separation date is prior to 9/11/01.

> \\

> Mapped Findings:

> Mapped Finding Item: CF.VA-LAST SERVICE SEPARATION DATE

> Beginning Date/Time: SEP 11, 2001

> ---- End: VA-IRAQ/AFGHAN PERIOD OF SERVICE -------------------------------

> ---- Begin: VA-ACTIVE DUTY (FI(2)=RT(568019)) ---------------------------

> Finding Type: REMINDER TERM Use in Patient Cohort Logic: OR

> Mapped Findings:

> Mapped Finding Item: CF.VA-PATIENT TYPE Condition: I V="ACTIVE DUTY"

> End: VA-ACTIVE DUTY

> ---- Begin: VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS (FI(3)=RT(824))

> Finding Type: REMINDER TERM Use in Resolution Logic: AND

> Mapped Findings:

> Mapped Finding Item: HF.TBI-FRAGMENT/BULLET Health Factor Category: TBI SOURCE

> Mapped Finding Item: HF.TBI-BULLET Health Factor Category: TBI SOURCE

> Mapped Finding Item: HF.TBI-VEHICULAR Health Factor Category: TBI SOURCE

> Mapped Finding Item: HF.TBI-FALL Health Factor Category: TBI SOURCE

> Mapped Finding Item: HF.TBI-BLAST Health Factor Category: TBI SOURCE

> Mapped Finding Item: HF.TBI-SECTION I - NO Health Factor Category: TBI-SECTIONS

> ---- End: VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS ---------------

> ---- Begin: VA-IRAQ/AFGHAN SERVICE NO (FI(4)=RT(489)) -------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Found Text: The record indicates that the patient did not serve in OEF or OIF.

> \\

> Mapped Findings:

> Mapped Finding Item: HF.NO IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

> End: VA-IRAQ/AFGHAN SERVICE NO

> ---- Begin: VA-IRAQ/AFGHAN SERVICE (FI(5)=RT(568012)) -------------------

> Finding Type: REMINDER TERM

> Mapped Findings:

> Mapped Finding Item: HF.IRAQ/AFGHAN SERVICE Health Factor Category: IRAQ/AFGHANISTAN

> End: VA-IRAQ/AFGHAN SERVICE

> ---- Begin: VA-TBI-PREVIOUS TBI DX (FI(6)=RT(828)) ----------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Beginning Date/Time: 9/11/01

> Found Text: Patient has documentation of previous TBI diagnosis on chart.

> Mapped Findings:

> Mapped Finding Item: HF.TBI-PREVIOUS TBI DX Health Factor Category: TBI-SECTIONS

> End: VA-TBI-PREVIOUS TBI DX

> ---- Begin: VA-TBI-PT REFUSAL (FI(7)=RT(829)) ---------------------------

> Finding Type: REMINDER TERM Use in Resolution Logic: OR

> Beginning Date/Time: T-30D

> Mapped Findings:

> Mapped Finding Item: HF.TBI-PT REFUSAL Health Factor Category: TBI-SECTIONS

> End: VA-TBI-PT REFUSAL

> ---- Begin: VA-LAST SERVICE SEPARATION DATE (FI(8)=CF(27)) --------------

> Finding Type: REMINDER COMPUTED FINDING

> ---- End: VA-LAST SERVICE SEPARATION DATE --------------------------------

> Function Findings:

> ---- Begin: FF(1)---------------------------------------------------------

> Function String: MRD(4)\>MRD(1) Expanded Function String:

> MRD(VA-IRAQ/AFGHAN SERVICE NO)\>MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> Not Found Text: The patient's most recent service separation date is more recent than their last screening

> \- if the patient was discharged after 9/11/01 then rescreening is needed after any new period of service.

> End: FF(1)

> ---- Begin: FF(2)---------------------------------------------------------

> Function String: MRD(3)\>MRD(1) Expanded Function String:

> MRD(VA-TBI SCREENING COMPLETED SCREENING RESOLUTIONS)\>MRD( VA-IRAQ/AFGHAN PERIOD OF SERVICE)

> End: FF(2)

> ---- Begin: FF(3)---------------------------------------------------------

> Function String: MRD(1)\>MRD(4,5) Expanded Function String:

> MRD(VA-IRAQ/AFGHAN PERIOD OF SERVICE)\>MRD(VA-IRAQ/AFGHAN SERVICE NO, VA-IRAQ/AFGHAN SERVICE)

> Found Text: The patient's most recent service separation date is more recent than their last screening

> \- if the patient was discharged after 9/11/01 then rescreening is needed after any new period of service.

> End: FF(3)

> General Patient Cohort Found Text:

> Patients who served in combat in either Iraq (Operation Iraqi Freedom) or in Afghanistan (Operation Enduring Freedom) should be screened for Traumatic Brain Injury.

> General Patient Cohort Not Found Text:

> Patients who were discharged from the service prior to 9/11/01 or who did NOT serve in OEF or OIF do NOT need to be screened for TBI.

> Default PATIENT COHORT LOGIC to see if the Reminder applies to a patient: (SEX)&(AGE)&FI(1)!FI(2)

> Expanded Patient Cohort Logic:

> (SEX)&(AGE)&FI(VA-IRAQ/AFGHAN PERIOD OF SERVICE)!FI(VA-ACTIVE DUTY)

> Customized RESOLUTION LOGIC defines findings that resolve the Reminder: (FI(4)&FF(1))!(FI(5)&FF(2))!FI(6)!FI(7)

> Expanded Resolution Logic:

> (FI(VA-IRAQ/AFGHAN SERVICE NO)&FF(1))!(FI(VA-IRAQ/AFGHAN SERVICE)& FF(2))!FI(VA-TBI-PREVIOUS TBI DX)!FI(VA-TBI-PT REFUSAL)

> Web Sites:

#### Appendix B: Reminder Dialog Screen Shots

> For more detailed information about use of this TBI Screening reminder, please review the PowerPoint at: [<u>http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-</u>](http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-07.ppt) [<u>07.ppt</u>](http://vista.med.va.gov/reminders/TBI%20SCREENING%20REMINDER%20PPT%203-14-07.ppt)

![](pxrm-2-8-tbi-screening-reminder-installation-and-setup-guide/004.png)

> ![](pxrm-2-8-tbi-screening-reminder-installation-and-setup-guide/005.png)

> ![](pxrm-2-8-tbi-screening-reminder-installation-and-setup-guide/006.png)

> ![](pxrm-2-8-tbi-screening-reminder-installation-and-setup-guide/007.png)

> ![](pxrm-2-8-tbi-screening-reminder-installation-and-setup-guide/008.png)