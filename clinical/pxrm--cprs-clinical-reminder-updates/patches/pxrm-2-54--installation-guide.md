---
title: PXRM*2*54 VA-Ebola Risk Triage Tool Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: VA-Ebola Risk Triage Tool
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*54
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 11
description: 
audience: 
keywords: 
  - blockquote
  - ebola
  - class
  - triage
  - table
  - risk
  - contents
  - style
  - width
  - reminder
page_count: 0
word_count: 2859
section_count: 10
table_count: 0
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: November 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_54_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_54_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/001.png)

> VA-EBOLA RISK TRIAGE TOOL

> Reminder Dialog Template Patch PXRM\*2\*54

> Installation Guide

> November 2014

> <span id="_bookmark0" class="anchor"></span>TABLE OF CONTENTS

> Contents

1.  [INTRODUCTION 3](#introduction)

[VA Links: 3](#va-links)

[Ebola web links: 3](#ebola-web-links)

2.  [INSTALLATION: 4](#installation)
3.  [POST INSTALLATION INSTRUCTION 6](#post-installation-instruction)
    1.  [Enabling the Reminder Dialog in VistA 6](#enabling-the-reminder-dialog-in-vista)
    2.  [Placing the Reminder Dialog in CPRS 7](#placing-the-reminder-dialog-in-cprs)
    3.  [Creating an “Ebola Templates” folder in Shared Templates 8](#_bookmark8)
    4.  [Placing the template in the Ebola Templates folder 9](#placing-the-template-in-the-ebola-templates-folder)
    5.  [Note Title 10](#note-title)
    6.  [Creating a Note Title in Vista 10](#creating-a-note-title-in-vista)
    7.  [Linking the Reminder Dialog Template to a Note Title 13](#linking-the-reminder-dialog-template-to-a-note-title)
4.  [GLOSSARY OF TERMS AND ABBREVIATIONS 14](#glossary-of-terms-and-abbreviations)

[APPENDIX A 17](#appendix-a)

[APPENDIX B 19](#appendix-b)

# INTRODUCTION


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [INTRODUCTION](#introduction)
  - [VA Links:](#va-links)
  - [Ebola web links:](#ebola-web-links)
- [INSTALLATION](#installation)
    - [The installation needs to be done by a person with DUZ(0) set to "@."](#the-installation-needs-to-be-done-by-a-person-with-duz0-set-to)
- [POST INSTALLATION INSTRUCTION](#post-installation-instruction)
  - [Enabling the Reminder Dialog in VistA](#enabling-the-reminder-dialog-in-vista)
  - [Placing the Reminder Dialog in CPRS](#placing-the-reminder-dialog-in-cprs)
  - [Placing the template in the Ebola Templates folder](#placing-the-template-in-the-ebola-templates-folder)
  - [Note Title](#note-title)
  - [Creating a Note Title in Vista](#creating-a-note-title-in-vista)
  - [Linking the Reminder Dialog Template to a Note Title](#linking-the-reminder-dialog-template-to-a-note-title)
- [GLOSSARY OF TERMS AND ABBREVIATIONS](#glossary-of-terms-and-abbreviations)
- [APPENDIX A](#appendix-a)
- [APPENDIX B](#appendix-b)
  - [REMINDER EXCHANGE Packing list](#reminder-exchange-packing-list)
> VA is developing policies, procedures, and resources to define our response and approach to management of individuals who may have been exposed to Ebola Virus Disease. The VA-EBOLA RISK TRIAGE TOOL template is a product developed based on the Centers for Disease Control and Prevention (CDC) algorithm for evaluating individuals who have traveled in countries with active epidemics of this disease. The collaboration led by Dr. Theresa Cullen in Health Informatics included input from the Office of Public Health, the Office of Primary Care, the National Director for Infectious Disease, Health Solutions Management, Informatics Patient Safety, Health Information Management, the National Clinical Reminder Committee (NCRC), and the Nashville Usability Lab among others.
> The template was created for use by VA clinical staff that is evaluating patients identified as having traveled to involved areas or as having contact with a known Ebola patient. Initial identification of patients with travel or contact risks may be done through several different pathways. These may include telephone hotlines, public service announcements, or signage at the medical center, all of which will direct patients to the appropriate intake location as established by the facility. Patient check-in Kiosks in clinic areas will have a screening question about travel to affected areas. Patients who enter a positive response will be immediately directed to clinic staff. Clinic check-in staff may also ask the initial questions about travel or contact. Patients with a positive response will also immediately be directed to clinical staff in compliance with locally established protocols. The VA- EBOLA RISK TRIAGE TOOL is intended for use by the clinical staff that assesses patients referred through any of these pathways. Additional clinical information about Ebola is available at the VA Ebola Outbreak site and the CDC Ebola Hemorrhagic Fever home page (see below).
> The template follows the CDC algorithm in guiding the assessment and recommending appropriate follow-up and actions based on the findings and risk level identified. It is intended for use throughout VA as the approved template for assessing these patients. It is sponsored by the Office of Public Health which will oversee use, evaluate data collected, and update recommendations as needed for this rapidly evolving disease. For additional information please contact Watch Officer at Outlook email address [<u>WatchOfficer-VHA@va.gov</u>](mailto:WatchOfficer-VHA@va.gov)

## VA Links:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- [<u>VA Office of Public Health Ebola Virus Disease Information</u>](https://vaww.vha.vaco.portal.va.gov/sites/PublicHealth/ebola/SitePages/Home.aspx)
- [<u>VA Office of Public Health Ebola Virus Outbreak Frequently Asked Questions (FAQ)</u>](https://vaww.vha.vaco.portal.va.gov/sites/PublicHealth/ebola/Shared%20Documents/Forms/AllItems.aspx?RootFolder=%2Fsites%2FPublicHealth%2Febola%2FShared%20Documents%2FFrequently%20Asked%20Questions&FolderCTID=0x01200065D87082BDE2594E9A142C74535C9D3E&View=%7b6757A514-5FC3-4B3C-96FA-3207659C1CB0%7d)

## Ebola web links:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- [<u>CDC Ebola website</u>](http://acpnews.org/t/747285/130142728/15099/0/) for the most updated information on the Ebola virus outbreak
- [<u>Checklist for Patients Being Evaluated for Ebola Virus Disease (EVD) in the United States</u>](http://acpnews.org/t/747285/130142728/15100/0/)
- [<u>Ebola Virus Disease (Ebola) - Algorithm for Evaluation of the Returned Traveler</u>](http://acpnews.org/t/747285/130142728/15101/0/) \*
- [<u>Informational PowerPoint: Ebola Facts</u>](http://www.accme.org/news-publications/publications/public-health-resources/ebola-facts)
- [<u>FAQ: Safe Management of Patients with Ebola Virus Disease (EVD) in US Hospitals</u>](http://www.accme.org/news-publications/publications/tools/faq-safe-management-patients-ebola-virus-disease-evd-us)
- [<u>Ebola Education Web page</u>](http://www.accme.org/cme-addresses-ebola-emergency)
- [<u>Johns Hopkins Ebola symposium</u>](http://hub.jhu.edu/2014/10/14/ebola-experts-johns-hopkins)

# INSTALLATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 1-2 minutes*

### The installation needs to be done by a person with DUZ(0) set to "@."

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Retrieve the host file from one of the following locations (with the ASCII file type):

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 37%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Albany</p>
</blockquote></th>
<th><mark><u>REDACTED</u></mark></th>
<th><mark><u>REDACTED</u></mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark><u>REDACTED</u></mark></td>
<td><mark><u>REDACTED</u></mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark><u>REDACTED</u></mark></td>
<td><mark><u>REDACTED</u></mark></td>
</tr>
</tbody>
</table>

2.  Install the patch first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

3.  Load the distribution.

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name followed by the Host File name at the Host File prompt.

> Example

> Select Installation Option: LOAD a Distribution

> Enter a Host File: \<*your directory name*\>PXRM_2_0_54.KID

> KIDS Distribution saved on

> From the Installation menu, you may elect to use the following options:

4.  Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

1.  Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

5.  Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*54 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: PXRM\*2.0\*54

> NOTE: DO NOT QUEUE THE INSTALLATION

> Answer "NO" to the following prompts:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//NO

> Installation Example

> See [Appendix A](#appendix-a)

6.  Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: PXRM\*2.0\*54

7.  Build File Print

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print Select BUILD NAME: PXRM\*2.0\*54

> DEVICE: HOME//

8.  Post-installation routines

> After successful installation, the following init routines may be deleted:

> PXRMP54E PXRMP54I

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

# POST INSTALLATION INSTRUCTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Enabling the Reminder Dialog in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Before linking the dialog to a title or using it in Shared templates you must first add it into the TIU Template Reminder Dialog Parameter list.

> ^General parameter tools \<enter\>

> List Values for a Selected Parameter List Values for a Selected Entity List Values for a Selected Package List Values for a Selected Template Edit Parameter Values

> Edit Parameter Values with Template Edit Parameter Definition Keyword

> Select General Parameter Tools Option: EDIT Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: TIU TEMPLATE REMINDER DIALOGS Reminder Dialogs

> allowed as Templates

> TIU TEMPLATE REMINDER DIALOGS may be set for the following:

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 14%" />
<col style="width: 57%" />
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
<th><blockquote>
<p>[choose from NEW PERSON]</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>SRV</td>
<td><blockquote>
<p>[choose from SERVICE/SECTION]</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td><blockquote>
<p>[choose from INSTITUTION]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
<td><blockquote>
<p>[TEST.V02.MED.VA.GOV]</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Enter selection: 5 System

> --- Setting TIU TEMPLATE REMINDER DIALOGS for System: the name of your system will appear in this area

> Select Display Sequence: ENTER A UNIQUE NUMBER (you may ? question mark this option to obtain the list of templates associated with this parameter)

> Are you adding (the new display sequence number) as a new Display Sequence? Yes// select \<enter\> to confirm

> Clinical Reminder Dialog: VA-EBOLA TRIAGE RISK TOOL reminderdialog NATIONAL type in the name of the dialog

> ...OK? Yes// \<Enter\>

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

## Placing the Reminder Dialog in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Link the dialogs from the CPRS TEMPLATE EDITOR.

- Open CPRS, select any patient and then the Notes tab.
- Open My Templates.
- Create a new template and give it an appropriate name (right side under Personal Templates).
- In the Template Type box select Reminder Dialog.
- Select the drop down arrow in the Reminder Dialog window and locate and select the EBOLA Risk Triage Tool reminder dialog.
- Select the APPLY button.

> After placing the reminder dialog in your personal templates you may want to take a few minutes to test the reminder to ensure it performs correctly (i.e. text wraps appropriately, health factors link to the note, etc.) before making it available for your clinical staff.

![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/002.png)

> While using the CPRS Template Editor, if at any time the settings do not look correct, NEVER click the “Apply” button, but instead click “Cancel”, then start over.

1.  <span id="_bookmark8" class="anchor"></span>Creating an *“Ebola Templates”* folder in Shared Templates

> It is recommended to create a folder for this template under Shared templates for the “Ebola Risk Triage Tool” and other Ebola screening templates you may have,. Additionally the Ebola Risk Triage

> tool template can be added to any other folder under Shared Templates. It is recommended that the “Ebola Risk Triage Tool” be placed in a highly visible and easily accessible position within Shared Templates. In this example an “Ebola Templates” folder is created under Shared Templates:

- Access CPRS, select any patient and select the Notes tab.
- Select Options, Edit Share templates.
- Select and open Shared Templates (left side of the screen).
- On the right side of the template editor screen Select the New Template button and name New template Ebola Templates.
- Select the drop down arrow under the Template type box and select Folder.
- Select Apply to save this folder.

![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/003.png)

## Placing the template in the Ebola Templates folder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once you have created the template into My Templates and created a Share Template folder Ebola Templates you can copy the template from My Templates to the Ebola Template folder, making it viewable and available to all CPRS users.

- Access CPRS, select any patient and select the Notes tab.
- Select Options, Edit Share templates.
- Select and open Shared Templates (left side of the screen).
- Select the Ebola Templates folder.
- On the right side of the template editor screen select the Ebola Risk Triage Tool template.
- Select the bold Copy button between the two panes.
- Select Apply to save the template into the folder.

![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/004.png)

## Note Title

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is important to consult with the appropriate Health Information Management and/or Health Informatics Committee to determine if the creation of a new local note title is necessary and/or desired functionality at your facility. Follow your facility’s policy for creating a new local note title. For more information on TIU Note Title and Templates you may access the [<u>VHA HIMS Practice Brief -</u>](http://vaww.vhahim.va.gov/index.php?option=com_edocman&task=document.download&id=114&Itemid=713) [<u>TIU TITLES AND TEMPLATES</u>](http://vaww.vhahim.va.gov/index.php?option=com_edocman&task=document.download&id=114&Itemid=713)

> It is recommended that you map your locally created title to one of two National Standard note titles “INFECTIOUS DISEASE RISK ASSESSMENT SCREENING NOTE” for a note title that will appear in the Notes Tab or “INFECTIOUS DISEASE CLINICAL WARNING” for a Clinical Warning title. For the completed clinical warning note to appear in the CWAD posting as well as the Notes Tab it must be created in the Clinical Warning TIU Hierarchy.

> In this example a new local note title has been created “Infectious Disease Risk Assessment Screening” and mapped to a National Standard title “Infectious Disease Risk Assessment Screening Note”.

## Creating a Note Title in Vista

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Navigate to the Manager Document Definition Menu in Vista

> Manager Document Definition Menu ---

1.  Edit Document Definitions
2.  Sort Document Definitions
3.  Create Document Definitions
4.  Create Objects
5.  Create TIU/Health Summary Objects

> Select Document Definitions (Manager) \<TEST ACCOUNT\> Option: 3 Create Document Definitions.

> Create Document Definitions Oct 24, 2014@08:36:50 Page: 1 of 1

> BASICS

> Name Type

1.  CLINICAL DOCUMENTS CL
2.  PROGRESS NOTES CL
3.  ADDENDUM DC
4.  DISCHARGE SUMMARY CL
5.  SHERI'S CLASS CL
6.  ZZCONSULTS CL
7.  MIKES TEST CLASS DC
8.  NANCY'S CLASS CL
9.  CLINICAL PROCEDURES CL
10. SURGICAL REPORTS CL
11. PAUL'S TEST CLASS DC

> New Users, Please Enter '?NEW' for Help \>\>\>

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Class/DocumentClass</p>
</blockquote></th>
<th><blockquote>
<p>Next Level</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>Detailed Display/Edit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>(Title)</p>
</blockquote></td>
<td><blockquote>
<p>Restart</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Status...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>(Component)</p>
</blockquote></td>
<td><blockquote>
<p>Boilerplate</p>
</blockquote></td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td><blockquote>
<p>Delete</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Action: Next Level// N=2 Select the number that corresponds to the document class where the title should be placed

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 28%" />
<col style="width: 33%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>1</p>
</blockquote></th>
<th colspan="2"><blockquote>
<p>CLINICAL DOCUMENTS</p>
</blockquote></th>
<th></th>
<th><blockquote>
<p>CL</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p><strong>PROGRESS NOTES</strong></p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>CL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ADVANCE DIRECTIVE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>HISTORICAL TITLES</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CRISIS NOTE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CLINICAL WARNING</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ADVERSE REACTION/ALLERGY</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>ADDICTION SEVERITY INDEX</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>BLIND REHABILITATION SERVICE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>SURGICAL</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>MEDICINE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>INFECTIOUS DISEASE</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>CHAPLAIN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>14</p>
<p>+</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>NURSING</p>
<p>?Help &gt;ScrollRight PS/PL PrintScrn/List</p>
</blockquote></td>
<td><blockquote>
<p>+/-</p>
</blockquote></td>
<td>&gt;&gt;&gt;</td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>Class/DocumentClass</p>
</blockquote></td>
<td><blockquote>
<p>Next Level</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Detailed Display/Edit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>(Title)</p>
</blockquote></td>
<td><blockquote>
<p>Restart</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Status...</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>(Component)</p>
</blockquote></td>
<td><blockquote>
<p>Boilerplate Text</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Delete</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Action: Next Screen// n=12 Next Level Depending on how your Document Hierarchy is arranged you may need to open another level of Document Class

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 28%" />
<col style="width: 4%" />
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Create</strong></th>
<th><blockquote>
<p><strong>Document Definitions</strong></p>
</blockquote></th>
<th><blockquote>
<p>Oct</p>
</blockquote></th>
<th><blockquote>
<p>24, 2014@08:43:19</p>
</blockquote></th>
<th><blockquote>
<p>Page:</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
<th><blockquote>
<p>of</p>
</blockquote></th>
<th><blockquote>
<p>1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>BASICS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>+</td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Type</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>2</td>
<td><blockquote>
<p>PROGRESS NOTES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>CL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>3</td>
<td><strong>INFECTIOUS DISEASE</strong></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>4</td>
<td>NEW TITLE INFECT</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>5</td>
<td><blockquote>
<p>PRIMARY CARE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TL</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\> (Class/DocumentClass) Next Level Detailed Display/Edit

> Title Restart Status...

> (Component) Boilerplate Text Delete Select Action: Title// Title

> Enter the Name of a new INFECTIOUS DISEASE: Infectious Disease Risk Assessment Screening ENTER the unique name Infectious Disease Risk Assessment Screening

> CLASS OWNER: CLINICAL COORDINATOR// CLINICAL COORDINATOR Enter ‘Owner” usually the

> Clinical coordinator (it may differ in your system).

1.  CLINICAL COORDINATOR
2.  CLINICAL COORDINATOR -MGR CHOOSE 1-2: 1 CLINICAL COORDINATOR

> You MUST map your title to a VHA Standard Title

> EVERY Local Title must be mapped to a VHA Enterprise Standard Title.

> Direct Mapping to Enterprise Standard Title...

> Your LOCAL Title is: INFECTIOUS DISEASE RISK ASSESSMENT SCREENING

> NOTE: Only ACTIVE Titles may be selected...

> Select VHA ENTERPRISE STANDARD TITLE: INFECTIOUS DISEASE RISK ASSESSMENT SCREENING NOTE I found a match of: INFECTIOUS DISEASE RISK ASSESSMENT SCREENING NOTE

> ... OK? Yes// YES

> Ready to map LOCAL Title: INFECTIOUS DISEASE RISK ASSESSMENT SCREENING to VHA Enterprise Standard Title: INFECTIOUS DISEASE RISK ASSESSMENT SCREENING NOTE

> ... OK? Yes// YES

> Done.

> STATUS: (A/I/T): INACTIVE// a ACTIVE Entry Activated. Activate the note title so it is selectable in CPRS

> SEQUENCE: \<ENTER\>

> MENU TEXT: Infectious Disease T Replace \<ENTER\>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 65%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 4%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Entry</p>
</blockquote></th>
<th><blockquote>
<p>Created</p>
</blockquote></th>
<th colspan="4"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Create</strong></td>
<td><blockquote>
<p><strong>Document Definitions</strong> Oct 24, 2014@08:44:14</p>
</blockquote></td>
<td><blockquote>
<p>Page:</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>of</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>BASICS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>+</td>
<td><blockquote>
<p>Name</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>Type</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>PROGRESS NOTES</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>CL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p><strong>INFECTIOUS DISEASE</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>DC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td><blockquote>
<p><strong>INFECTIOUS DISEASE RISK ASSESSMENT SCREENING</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p><strong>TL</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>NEW TITLE INFECT</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TL</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>PRIMARY CARE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td><blockquote>
<p>TL</p>
</blockquote></td>
</tr>
</tbody>
</table>

> ?Help \>ScrollRight PS/PL PrintScrn/List +/- \>\>\>

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 29%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>(Class/DocumentClass)</p>
</blockquote></th>
<th><blockquote>
<p>Next Level</p>
</blockquote></th>
<th><blockquote>
<p>Detailed Display/Edit</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Title</p>
</blockquote></td>
<td><blockquote>
<p>Restart</p>
</blockquote></td>
<td><blockquote>
<p>Status...</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>(Component)</p>
</blockquote></td>
<td><blockquote>
<p>Boilerplate Text</p>
</blockquote></td>
<td><blockquote>
<p>Delete</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Select Action: Title//</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Linking the Reminder Dialog Template to a Note Title

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If your site would like to link the Ebola Risk Triage Tool reminder dialog template to a note title, this is done through the CPRS Template Editor.

- Access CPRS, select any patient and select the Notes tab.
- Select Options, Edit Share templates.
- Select and open Document Titles (left side of the screen).
- On the right side of the template editor screen select the Ebola Risk Triage Tool.
- Select the bold Copy arrow between the two panes, the template will copy over to the document titles.
- Select the Ebola Risk Triage Tool under document titles, then in the Associated Title box type in the name of the title Infectious Disease Risk Assessment Screening
- Select Apply to save.

![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/005.png)

![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/006.png)

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

# GLOSSARY OF TERMS AND ABBREVIATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CAC – Clinical Applications Coordinator

> CDC – Centers for Disease Control and Prevention

> CPRS – Computerized Patient Record System, previous version dating back to 1997 was CPRS List Manager (VistA terminal emulation only) and no longer supported but is still accessible in VISTA. CPRS GUI is the Windows version (since 1998), and is now called just CPRS ([<u>CPRS page on VDL web</u>](http://www.va.gov/vdl/application.asp?appid=61) [<u>site</u>](http://www.va.gov/vdl/application.asp?appid=61))

> CWAD – Special note titles that display in the POSTINGS window in the CPRS header. Each letter stands for a category: C = Crisis Notes; W = Clinical Warnings; A = Allergies/Adverse Drug Reactions (ADR); D = Advance Directives

> Data Object – also called a ‘Patient Data Object’ or just as ‘object’. These are either created by programmer (OI&T staff), or a CAC/HIS can create (TIU-HS object).

> Dialog- A window in CPRS that opens in the format of a form to aid the user in creating text in a note and entering information into the record with a point and click interface.

> Elements- A component in VistA that is configured to display content for the user when a dialog is opened.

> EVD – Ebola Virus Disease

> FAQ – Frequently Asked Questions

> FORUM – the VA’s WAN (Wide Area Network), for mail, patch trackers, E3R repository

> ![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/007.png)GUI – Graphical User Interface, referring to a Windows application

> GUI Dialog Template/GUI Dialog - a CPRS template (plain text), TXML format, icons ![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/008.png)

> Health Factor- Informational data marker entered into the record to document patient information that is not readily identifiable with other information data entries in the system. Health Factors are used in TIU-Health Summary objects, in Health Summary types, and for data capture (for VA FileMan queries/reports, VISN data warehouse data pulls, etc.)

> HIS – Health Informatics Specialist, another title for Clinical Applications Coordinator (CAC) with same responsibilities as a CAC.

> Health Summary (HS) – a clinical module (package) in VistA; GMTS is the package’s name spacing ([<u>Health Summary page on VDL web site</u>](http://www.va.gov/vdl/application.asp?appid=63))

> Health Summary Types/Objects - A collection of data that displays to the user specific to the patient’s chart they are viewing.

> Health Summary Type – a configuration of health summary components used as the basis of a report viewed in VISTA or the CPRS GUI, or used in a TIU-Health Summary object

> Health Summary Object – the display settings of a Health Summary Type which is part of a TIU- Health Summary Object configuration.

> Health Summary Component – an item that is used to create a health summary type (i.e., report). Health Summary components can be viewed via \[GMTS HS ADHOC\], or "List Health Summary Components \[GMTS COMP LIST\]", or "List Health Summary Component Descriptions \[GMTS COMP DESC LIST\]".

> Host file – the file that is created in the reminder exchange option using .prd (Packed Reminder Definition format

> KIDS- Kernel Installation Distribution System

> Mapping - Linking of data markers such as Health Factors or other data entry items to reminder components such as reminder elements.

> Name spacing – the prefixing, i.e., the initial 3-4 leading characters of a module or items in VistA National Class - The highest collection of edit permissions which can be assigned to an item (versus VISN or LOCAL)

> NCRC – National Clinical Reminder Committee

> OPH – Office of Public Health

> OIA – Office of Information and Analytics

> OPC – Office of Primary Care

> Packing List – the list of included items of a reminder exchange export when viewed from the ‘IFE’ action in the reminder exchange VISTA option

> PCE – Patient Care Encounter (link to VDL web page)

> PRD - .pdf file = Packed Reminder Definition (the alternate format for sending/receiving reminder exchange exports).

> PXRM – namespace for the clinical reminders module ([<u>clinical reminders page on VDL web site</u>](http://www.va.gov/vdl/application.asp?appid=60)) Reminder Taxonomy- Collection of specific codes associated with specific clinical conditions Template- Commonly referred to as a dialog. See dialog for definition

> Reminder Dialog ![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/009.png) - a template created in \[PXRM DIALOG/COMPONENT EDIT\]; can be used without reminder logic (reminder definition)

> Reminder Dialog Template ![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/010.png) - a template created in \[PXRM DIALOG/COMPONENT EDIT\] and used in CPRS without linked reminder logic (reminder definition), either as a stand-alone template or the

> template is linked to a note title. Sometimes also referred to as a ‘reminder template’. Reminder Definition – used to create reminder logic for a clinical reminder or data object or reminder order check in PXRM REMINDER MANAGEMENT\]

> Reminder Exchange – the VISTA option \[PXRM REMINDER EXCHANGE\] used to create a reminder exchange message or .prd host file

> ![](pxrm-2-54-va-ebola-risk-triage-tool-installation-guide/011.png)Reminder Exchange Export – either a reminder exchange message or a .prd file moved out of the Reminder Exchange option in VISTA

> Shared Templates- Templates within the shared templates tree of CPRS, which the users can access and use while documenting in the chart

> SHOP-ALL – a destination through the VA’s FORUM to access and download reminder exchange messages that have been posted and stored (uses Mailman; must have FORUM access)

> TIU -Text Integrated Utility, the notes repository (clinical package) in VISTA ([<u>TIU page on VDL web</u>](http://www.va.gov/vdl/application.asp?appid=65) [<u>site</u>](http://www.va.gov/vdl/application.asp?appid=65))

> TIU Document Definition – it can be a CLASS, DOCUMENT CLASS, TITLE or OBJECT (file \#8925.1). The reminder exchange packing list shows the TIU object labeled as “TIU DOCUMENT DEFINITION”.

> TIU-Health Summary Object (also known as a TIU-HS OBJECT) – the link to TIU manual, ref (creating health summary objects)

> TIU Object – a data object /patient data object (but too general a term to know if this is programmer- created or CAC/HIS-created). See DATA OBJECT above.

> TIU Template – a TXML template (see TXML or GUI Dialog).

> TXML - the file format of ‘plain text’ CPRS templates, aka “GUI dialogs” or “GUI Dialog Templates”. Uses the CPRS GUI Template Editor to create and edit

> TIU TEMPLATE FIELD file - file \#8927 in VISTA, where TIU template fields are stored

> TIU TEMPLATE file – file \#8927 in VISTA, where TXML templates are stored

> User Acceptance Testing - (UAT) critical software testing where end-users test the software in real- world scenarios before it is nationally released

> URL – Uniform Resource Locator, i.e., a specific web address (Internet or Intranet)

> Usability Testing- evaluating the software by testing with a representation of users that follow specific tasks (test scripts), identify problems, suggest improvements and determine the user’s satisfaction with the product.

> VDL –The Internet page for all VISTA manuals and documentation [<u>VistA Documentation Library</u>](http://www.va.gov/vdl/)

> VMP- VistA Maintenance Project

# APPENDIX A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation \<TEST ACCOUNT\> Option: install Package(s) Select INSTALL NAME: PXRM\*2.0\*54 10/31/14@09:04:59

> =\> EBOLA RISK TRIAGE TOOL ;Created on Oct 28, 2014@10:58:40

> This Distribution was loaded on Oct 31, 2014@09:04:59 with header of EBOLA RISK TRIAGE TOOL ;Created on Oct 28, 2014@10:58:40

> It consisted of the following Install(s):

> PXRM\*2.0\*54

> Checking Install for Package PXRM\*2.0\*54 Install Questions for PXRM\*2.0\*54 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// HOME

> Install Started for PXRM\*2.0\*54 : Oct 31, 2014@09:05:23

> Build Distribution Date: Oct 28, 2014 Installing Routines:

> Oct 31, 2014@09:05:23

> Running Pre-Install Routine: PRE^PXRMP54I DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> Oct 31, 2014@09:05:24

> Installing Data:

> Oct 31, 2014@09:05:24

> Running Post-Install Routine: POST^PXRMP54I ENABLE options.

> ENABLE protocols.

> There are 1 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry PATCH PXRM\*2\*54 EBOLA RISK TRIAGE TOOL Updating Routine file...

> Updating KIDS files...

> PXRM\*2.0\*54 Installed.

> Oct 31, 2014@09:05:34

> Not a production UCI

> PXRM\*2.0\*54

> Install Completed

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

# APPENDIX B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## REMINDER EXCHANGE Packing list

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Description:

> The following Clinical Reminder items were selected for packing: REMINDER DIALOG

> VA-EBOLA RISK TRIAGE (3 OBJECTS) VA-EBOLA RISK TRIAGE TOOL

> Keywords:

> Components:

> TIU TEMPLATE FIELD

1.  VA-EBOLA W-P 4LINES/FL72
2.  VA-EBOLA URL CDC AFFECTED AREAS
3.  VA-EBOLA URL CDC ALGORITHM
4.  VA-EBOLA URL CDC CHECKLIST

> HEALTH FACTORS

5.  SCREENING FOR EPIDEMIC DISEASE
6.  EBOLA TRIAGE-IN-HOSP MGMT NOT REQUIRED
7.  EBOLA TRIAGE-IN-HOSP MGMT REQUIRED
8.  EBOLA TRIAGE-TESTING IS NOT INDICATED
9.  EBOLA TRIAGE-TESTING IS INDICATED
10. EBOLA TRIAGE-EBOLA NOT SUSPECTED
11. EBOLA TRIAGE-EBOLA SUSPECTED
12. EBOLA TRIAGE-EXPOSURE PERCUTANEOUS/MUCUS
13. EBOLA TRIAGE-EXPOSURE PT CARE W/O PPE
14. EBOLA TRIAGE-EXPOSURE HOUSEHOLD CONTACT
15. EBOLA TRIAGE-EXPOSURE PROCESSING W/O PPE
16. EBOLA TRIAGE-EXPOSURE DECEASED BODY
17. EBOLA TRIAGE-EXPOSURE SKIN/BODY FLUIDS
18. EBOLA TRIAGE-NO KNOWN EXPOSURE
19. EBOLA TRIAGE-LOW RISK EXPOSURE
20. EBOLA TRIAGE-HIGH RISK EXPOSURE
21. EBOLA TRIAGE-FEVER/SYMPTOMS POSITIVE
22. EBOLA TRIAGE-FEVER/SYMPTOMS NEGATIVE
23. EBOLA TRIAGE-POSITIVE CONTACT HISTORY
24. EBOLA TRIAGE-POSITIVE TRAVEL HISTORY
25. EBOLA RISK TRIAGE COMPLETED

> REMINDER SPONSOR

26. Office of Public Health

> REMINDER TAXONOMY

27. VA-EBOLA RISK TRIAGE DIAGNOSIS CODE

> REMINDER TERM

28. VA-EBOLA RISK TRIAGE IN-HOSPITAL MANAGEMENT
29. VA-EBOLA RISK TRIAGE TESTING STATUS
30. VA-EBOLA RISK TRIAGE EBOLA SUSPECTED/NOT SUSPECTED
31. VA-EBOLA RISK TRIAGE TYPE OF EXPOSURE
32. VA-EBOLA RISK TRIAGE LEVEL OF EXPOSURE
33. VA-EBOLA RISK TRIAGE FEVER/SYMPTOMS
34. VA-EBOLA RISK TRIAGE CONTACT HISTORY
35. VA-EBOLA RISK TRIAGE TRAVEL HISTORY REMINDER DEFINITION
36. VA-EBOLA RISK TRIAGE OBJECT LAST RATING

> REMINDER DIALOG

37. VA-EBOLA RISK TRIAGE (3 OBJECTS)
38. VA-EBOLA RISK TRIAGE TOOL

> HEALTH SUMMARY COMPONENT

> CLINICAL REMINDERS FINDINGS PCE HEALTH FACTORS SELECTED

> HEALTH SUMMARY TYPE

39. VA-EBOLA TRIAGE LAST RATING
40. VA-EBOLA RISK TRIAGE (ALL HFS)
41. VA-EBOLA RISK TRIAGE COMPLETED

> HEALTH SUMMARY OBJECTS

42. VA-EBOLA RISK TRIAGE LAST RATING
43. VA-EBOLA RISK TRIAGE (ALL HFS)
44. VA-EBOLA RISK TRIAGE COMPLETED

> TIU DOCUMENT DEFINITION

45. EBOLA RISK TRIAGE LAST RATING
46. EBOLA RISK TRIAGE (CUMULATIVE)
47. EBOLA RISK TRIAGE COMPLETED