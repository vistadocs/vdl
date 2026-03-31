---
title: PXRM*2*56 VA-Veterans Choice Note Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: VA-Veterans Choice Note
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*56
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 10
description: 
audience: 
keywords: 
  - blockquote
  - table
  - class
  - contents
  - style
  - width
  - title
  - strong
  - reminder
  - colspan
page_count: 0
word_count: 2661
section_count: 19
table_count: 0
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: November 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_56_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_56_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-56-va-veterans-choice-note-installation-guide/001.png)

> VA-VETERANS CHOICE NOTE

> Reminder Dialog Template Patch PXRM\*2.0\*56

> Installation Guide

> November 2014

> <span id="_bookmark0" class="anchor"></span>TABLE OF CONTENTS

## Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  [INTRODUCTION 3](#introduction)
[VA Links: 3](#va-links)
Veterans Choice web links: Error! Bookmark not defined.
2.  [INSTALLATION: 4](#installation)
[This patch can be installed with users on the system, but it should be done during non-peak](#_bookmark4)
[hours. Estimated Installation Time: 10-15 minutes 4](#_bookmark4)
3.  [POST INSTALLATION INSTRUCTION 6](#post-installation-instruction)
    1.  [Enabling the Reminder Dialog in VistA 6](#enabling-the-reminder-dialog-in-vista)
    2.  [Placing the Reminder Dialog in CPRS 7](#placing-the-reminder-dialog-in-cprs)
    5.  [Note Title 8](#note-title)
    6.  [Creating a Note Title in Vista 8](#creating-a-note-title-in-vista)
    7.  [Linking the Reminder Dialog Template to a Note Title 10](#linking-the-reminder-dialog-template-to-a-note-title)
4.  [GLOSSARY OF TERMS AND ABBREVIATIONS 12](#glossary-of-terms-and-abbreviations)
[APPENDIX A 15](#appendix-a)
[APPENDIX B 17](#appendix-b)

# INTRODUCTION


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Contents](#contents)
- [INTRODUCTION](#introduction)
  - [VA Links:](#va-links)
- [INSTALLATION:](#installation)
  - [Retrieve the host file from one of the following locations (with the ASCII file type):](#retrieve-the-host-file-from-one-of-the-following-locations-with-the-ascii-file-type)
  - [Load the distribution.](#load-the-distribution)
  - [Example](#example)
  - [Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Installation Example](#installation-example)
  - [Install File Print](#install-file-print)
  - [Build File Print](#build-file-print)
  - [Post-installation routines](#post-installation-routines)
- [POST INSTALLATION INSTRUCTION](#post-installation-instruction)
  - [Enabling the Reminder Dialog in VistA](#enabling-the-reminder-dialog-in-vista)
  - [Placing the Reminder Dialog in CPRS](#placing-the-reminder-dialog-in-cprs)
  - [While using the CPRS Template Editor, if at any time the settings do not look correct, NEVER click the “Apply” button, but instead click “Cancel”, then start over.](#while-using-the-cprs-template-editor-if-at-any-time-the-settings-do-not-look-correct-never-click-the-apply-button-but-instead-click-cancel-then-start-over)
  - [Note Title](#note-title)
  - [Creating a Note Title in Vista](#creating-a-note-title-in-vista)
  - [Linking the Reminder Dialog Template to a Note Title](#linking-the-reminder-dialog-template-to-a-note-title)
- [GLOSSARY OF TERMS AND ABBREVIATIONS](#glossary-of-terms-and-abbreviations)
- [APPENDIX A](#appendix-a)
- [APPENDIX B](#appendix-b)
  - [REMINDER EXCHANGE Packing list](#reminder-exchange-packing-list)
> Public Law (P.L.) 113-146, the Veterans Access, Choice, and Accountability Act of 2014, which was enacted on August 7, 2014, and amended through the Department of Veterans Affairs Expiring Authorities Act of 2014 (P.L. 113-175), improves the access of eligible Veterans to health care through non-VA entities and providers. The law establishes the Veterans Choice Program, new documentation and reporting requirements, and the Veterans Choice fund. P.L. 113-146 did not change the eligibility requirements for enrollment in the VA health care system and did not modify VA’s existing authorities to furnish non- VA care. On November 5, 2014, the Department of Veterans Affairs (VA) published an interim final rulemaking, AP24, that amends sections 17.108, 17.110, and 17.111 of title 38 of the Code of Federal Regulations (CFR) and establishes new regulations at 38 CFR 17.500 through 17.1540 to implement the Choice Program.
> The purpose of the Veterans Choice progress note is to communicate appointment information and services approved. It may be used for care coordination activities and tracking/data mining. The Veterans Choice Note would be completed by the Non-VA Medical Care Coordination staff. They will document Pre and Post visit information for care coordination. The Health Factors “Veterans Choice List 30 Day and VC 40 Mile have been added to the template to facilitate tracking/data mining. The note will also be used for linking non-VA provider documentation scanned into VistA Imaging with the CPRS/TIU note. The progress note approach was chosen to avoid a complex Veterans Choice consult order/completion process. As with the overall process, the Veterans Choice Note template has been streamlined to minimize the impact on NVC staff. <span class="mark">REDACTED</span>

## VA Links:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- [<u>Veterans Access, Choice and Accountability Act (Choice Act) Home</u>](http://vaww.va.gov/CHOICE/index.asp)
- [<u>External Veterans Choice Program website for Veterans and Stakeholders</u>](http://www.va.gov/opa/choiceact/)
- [<u>Veterans Access, Choice and Accountability Act of 2014 Public Law PDF</u>](http://www.gpo.gov/fdsys/pkg/PLAW-113publ146/pdf/PLAW-113publ146.pdf)

# INSTALLATION:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark4" class="anchor"></span>*This patch can be installed with users on the system. It is not necessary to be installed during non- peak hours. Estimated Installation Time: 1-2 minutes*

> *The installation needs to be done by a person with DUZ(0) set to "@."*

## Retrieve the host file from one of the following locations (with the ASCII file type):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<th><blockquote>
<p><a href="ftp://ftp.fo-albany.med.va.gov/"><mark><u>REDACTED</u></mark></a></p>
</blockquote></th>
<th><blockquote>
<p><a href="ftp://ftp.fo-albany.med.va.gov/"><mark><u>REDACTED</u></mark></a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><blockquote>
<p><a href="ftp://ftp.fo-albany.med.va.gov/"><mark><u>REDACTED</u></mark></a></p>
</blockquote></td>
<td><blockquote>
<p><a href="ftp://ftp.fo-albany.med.va.gov/"><mark><u>REDACTED</u></mark></a></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><blockquote>
<p><a href="ftp://ftp.fo-albany.med.va.gov/"><mark><u>REDACTED</u></mark></a></p>
</blockquote></td>
<td><blockquote>
<p><a href="ftp://ftp.fo-albany.med.va.gov/"><mark><u>REDACTED</u></mark></a></p>
</blockquote></td>
</tr>
</tbody>
</table>

1.  Install the patch first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

## Load the distribution.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution.

## Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation Option: LOAD a Distribution Enter a Host File: \<Your Directory\>PXRM_2_0_56.KID KIDS Distribution saved on

> From the Installation menu, you may elect to use the following options:

## Backup a Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

## Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*56 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Select Installation & Distribution System Option: Installation

> Select Installation Option: INSTALL PACKAGE(S)

> Select INSTALL NAME: PXRM\*2.0\*56

> Answer "NO" to the following prompts:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO NOTE: DO NOT QUEUE THE INSTALLATION

## Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [<u>APPENDIX A</u>](#appendix-a)

## Install File Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process.

> Select Utilities Option: Install File Print

> Select INSTALL NAME: PXRM\*2.0\*56

## Build File Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

> Select Utilities Option: Build File Print Select BUILD NAME: PXRM\*2.0\*56

> DEVICE: HOME//

## Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After successful installation, the following init routines may be deleted:

> PXRMP56E PXRMP56I

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

> Clinical Reminder Dialog: VA-VETERANS CHOICE NOTE reminder dialog NATIONAL type in the name of the dialog

> ...OK? Yes// \<Enter\>

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

## Placing the Reminder Dialog in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Link the dialogs from the CPRS TEMPLATE EDITOR.

- Open CPRS, select any patient and then the Notes tab.
- Open My Templates.
- Create a new template and give it an appropriate name (right side under Personal Templates).
- In the Template Type box select Reminder Dialog.
- Select the drop down arrow in the Reminder Dialog window and locate and select the VA- VETERANS CHOICE NOTE reminder dialog.
- Select the APPLY button.

> After placing the reminder dialog in your personal templates you may want to take a few minutes to test the reminder to ensure it performs correctly (i.e. text wraps appropriately, health factors link to the note, etc.) before making it available for your clinical staff.

![](pxrm-2-56-va-veterans-choice-note-installation-guide/002.png)

## While using the CPRS Template Editor, if at any time the settings do not look correct, NEVER click the “Apply” button, but instead click “Cancel”, then start over.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

## Note Title

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is important to consult with the appropriate Health Information Management and/or Health Informatics Committee to determine if the creation of a new local note title is necessary and/or desired functionality at your facility. Follow your facility’s policy for creating a new local note title. For more information on TIU Note Title and Templates you may access the [<u>VHA HIMS Practice Brief -</u>](http://vaww.vhahim.va.gov/index.php?option=com_edocman&task=document.download&id=114&Itemid=713) [<u>TIU TITLES AND TEMPLATES</u>](http://vaww.vhahim.va.gov/index.php?option=com_edocman&task=document.download&id=114&Itemid=713)

> Create the VETERANS CHOICE NOTE title using the instructions below. The VETERANS CHOICE NOTE must be mapped to the VHA Enterprise Standard Title of NONVA NOTE.

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

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

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
<col style="width: 5%" />
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
<td><blockquote>
<p><strong>NON VA CARE</strong></p>
</blockquote></td>
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
<td><blockquote>
<p>NEW TITLE INFECT</p>
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

> Enter the Name of a new NON VA CARE: VETERANS CHOICE NOTE

> CLASS OWNER: CLINICAL COORDINATOR// CLINICAL COORDINATOR Enter ‘Owner” usually the

> Clinical coordinator (it may differ in your system).

1.  CLINICAL COORDINATOR
2.  CLINICAL COORDINATOR -MGR CHOOSE 1-2: 1 CLINICAL COORDINATOR

> You MUST map your title to a VHA Standard Title

> EVERY Local Title must be mapped to a VHA Enterprise Standard Title. VETERANS CHOICE NOTE <u>MUST</u> be mapped to NONVA NOTE

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

> Direct Mapping to Enterprise Standard Title... Your LOCAL Title is: VETERANS CHOICE NOTE

> NOTE: Only ACTIVE Titles may be selected...

> Select VHA ENTERPRISE STANDARD TITLE: NONVA NOTE

> I found a match of: NONVA NOTE

> ... OK? Yes// YES

> Ready to map LOCAL Title: VETERANS CHOICE NOTE to VHA Enterprise Standard Title: NONVA NOTE

> ... OK? Yes// YES

> Done.

> STATUS: (A/I/T): INACTIVE// a ACTIVE Entry Activated. Activate the note title so it is selectable in CPRS

> SEQUENCE: \<ENTER\>

> MENU TEXT: Infectious Disease T Replace \<ENTER\>

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 28%" />
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 14%" />
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
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Create</strong></td>
<td><blockquote>
<p><strong>Document Definitions</strong></p>
</blockquote></td>
<td>Oct</td>
<td><blockquote>
<p>24, 2014@08:44:14</p>
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
<tr class="odd">
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
<tr class="even">
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
<tr class="odd">
<td>3</td>
<td><blockquote>
<p><strong>NON VA CARE</strong></p>
</blockquote></td>
<td></td>
<td></td>
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
<p><strong>VETERANS CHOICE</strong></p>
</blockquote></td>
<td><strong>NOTE</strong></td>
<td></td>
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

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

## Linking the Reminder Dialog Template to a Note Title

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VA-VETERANS CHOICE NOTE reminder dialog template must be associated to the TIU note title VETERANS CHOICE NOTE.

- Access CPRS, select any patient and select the Notes tab.
- Select Options, Edit Shared templates.
- Select and open Document Titles (left side of the screen).
- On the right side the “My Templates” root of the template editor screen select the VETERANS CHOICE NOTE.
- Select the bold Copy arrow between the two panes, the template will copy over to the document titles.
- Select the VETERANS CHOICE NOTE under document titles, then in the Associated Title box type in the name of the title VETERANS CHOICE NOTE.
- Select Apply to save.

> ![](pxrm-2-56-va-veterans-choice-note-installation-guide/003.png)

![](pxrm-2-56-va-veterans-choice-note-installation-guide/004.png)

# GLOSSARY OF TERMS AND ABBREVIATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> CAC – Clinical Applications Coordinator

> CDC – Centers for Disease Control and Prevention

> CPRS – Computerized Patient Record System, previous version dating back to 1997 was CPRS List Manager (VistA terminal emulation only) and no longer supported but is still accessible in VISTA. CPRS GUI is the Windows version (since 1998), and is now called just CPRS ([<u>CPRS page on VDL web</u>](http://www.va.gov/vdl/application.asp?appid=61) [<u>site</u>](http://www.va.gov/vdl/application.asp?appid=61))

> CWAD – Special note titles that display in the POSTINGS window in the CPRS header. Each letter stands for a category: C = Crisis Notes; W = Clinical Warnings; A = Allergies/Adverse Drug Reactions (ADR); D = Advance Directives

> Data Object – also called a ‘Patient Data Object’ or just as ‘object’. These are either created by programmer (OI&T staff), or a CAC/HIS can create (TIU-HS object).

> Dialog- A window in CPRS that opens in the format of a form to aid the user in creating text in a note and entering information into the record with a point and click interface.

> Elements- A component in VistA that is configured to display content for the user when a dialog is opened.

> FAQ – Frequently Asked Questions

> FORUM – the VA’s WAN (Wide Area Network), for mail, patch trackers, E3R repository

> ![](pxrm-2-56-va-veterans-choice-note-installation-guide/005.png)GUI – Graphical User Interface, referring to a Windows application

> GUI Dialog Template/GUI Dialog - a CPRS template (plain text), TXML format, icons ![](pxrm-2-56-va-veterans-choice-note-installation-guide/006.png)

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

> Reminder Dialog ![](pxrm-2-56-va-veterans-choice-note-installation-guide/007.png) - a template created in \[PXRM DIALOG/COMPONENT EDIT\]; can be used without reminder logic (reminder definition)

> Reminder Dialog Template ![](pxrm-2-56-va-veterans-choice-note-installation-guide/008.png) - a template created in \[PXRM DIALOG/COMPONENT EDIT\] and used in CPRS without linked reminder logic (reminder definition), either as a stand-alone template or the template is linked to a note title. Sometimes also referred to as a ‘reminder template’.

> Reminder Definition – used to create reminder logic for a clinical reminder or data object or reminder order check in PXRM REMINDER MANAGEMENT\]

> Reminder Exchange – the VISTA option \[PXRM REMINDER EXCHANGE\] used to create a reminder exchange message or .prd host file

> ![](pxrm-2-56-va-veterans-choice-note-installation-guide/009.png)Reminder Exchange Export – either a reminder exchange message or a .prd file moved out of the Reminder Exchange option in VISTA

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

> Enter a Host File: \<*your directory*\>PXRM_2_0_56.KID

> KIDS Distribution saved on Dec 03, 2014@08:36:30 Comment: VA-VETERANS CHOICE NOTE

> This Distribution contains Transport Globals for the following Package(s): Build PXRM\*2.0\*56 has been loaded before, here is when:

> PXRM\*2.0\*56 Install Completed

> was loaded on Dec 03, 2014@09:20:58 OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> PXRM\*2.0\*56

> Use INSTALL NAME: PXRM\*2.0\*56 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> You have PENDING ALERTS

> Enter "VA to jump to VIEW ALERTS option You've got PRIORITY mail!

> Select Installation \<TEST ACCOUNT\> Option: INstall Package(s) Select INSTALL NAME: PXRM\*2.0\*56 12/3/14@09:42:41

> =\> VA-VETERANS CHOICE NOTE ;Created on Dec 03, 2014@08:36:30

> This Distribution was loaded on Dec 03, 2014@09:42:41 with header of VA-VETERANS CHOICE NOTE ;Created on Dec 03, 2014@08:36:30

> It consisted of the following Install(s):

> PXRM\*2.0\*56

> Checking Install for Package PXRM\*2.0\*56 Install Questions for PXRM\*2.0\*56 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

> Install Started for PXRM\*2.0\*56 : Dec 03, 2014@09:42:48

> Build Distribution Date: Dec 03, 2014 Installing Routines:

> Dec 03, 2014@09:42:48

> Running Pre-Install Routine: PRE^PXRMP56I DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> Dec 03, 2014@09:42:48

> Installing Data:

> Dec 03, 2014@09:42:48

> Running Post-Install Routine: POST^PXRMP56I ENABLE options.

> ENABLE protocols.

> There are 1 Reminder Exchange entries to be installed.

> 1\. Installing Reminder Exchange entry PATCH PXRM\*2.0\*56 VA-VETERANS CHOICE NOTE

> Updating Routine file... Updating KIDS files... PXRM\*2.0\*56 Installed.

> Dec 03, 2014@09:42:54

> Not a production UCI

> PXRM\*2.0\*56

> Install Completed

> [*<u>\[return to table of contents\]</u>*](#_bookmark0)

# APPENDIX B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## REMINDER EXCHANGE Packing list

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Description:

> The following Reminder Dialog items were selected for packing: REMINDER DIALOG

> Keywords:

> Components:

> TIU TEMPLATE FIELD

> TIU TEMPLATE FIELD WORD PROCESSING 68 LENGTH 10 LINES

> TIU TEMPLATE FIELD VA-VETERANS CHOICE CLINICAL INFORMATION DISPLAY TEXT TIU TEMPLATE FIELD DATE/TIME REQ

> TIU TEMPLATE FIELD WORD PROCESSING 68 LENGTH 10 LINE INDENT REQ TIU TEMPLATE FIELD VA-VETERANS CHOICE APPROVED SERVICES SPECIFY TIU TEMPLATE FIELD TEXT 50 REQUIRED

> TIU TEMPLATE FIELD VA-VETERANS CHOICE ELIGIBILITY INFO HYPERLINK TIU TEMPLATE FIELD VA-VETERANS CHOICE HYPERLINK

> HEALTH FACTORS

> Category: VETERANS CHOICE VCL 30 DAY

> VC 40 MILE

> VC SCANNED RESULTS

> REMINDER SPONSOR

> Clinical Business Systems Office

> REMINDER DIALOG

> VA-VETERANS CHOICE NOTE

> VA-DE VETERANS CHOICE ADDITIONAL COMMENTS VA-DE VETERANS CHOICE APPROVED SERVICES TEXT VA-DE VETERANS CHOICE APPROVED SERVICES TEXT VA-DE VETERANS CHOICE APPT D/T

> VA-DE VETERANS CHOICE CLINICAL INFO TEXT

> VA-DE VETERANS CHOICE POST VISIT SCANNED DOCUMENTATION VA-DE VETERANS CHOICE PROVIDER NAME

> VA-DE VETERANS CHOICE TEMPLATE INSTRUCTION TEXT VA-DE VETERANS CHOICE VC 40 MILE

> VA-DE VETERANS CHOICE VCL 30 DAY

> VA-DG VETERANS CHOICE ADDITIONAL COMMENTS VA-DG VETERANS CHOICE APPROVED SERVICES VA-DG VETERANS CHOICE APPT D/T

> VA-DG VETERANS CHOICE EPISODE OF CARE VA-DG VETERANS CHOICE INSTRUCTIONS

> VA-DG VETERANS CHOICE MAIN

> VA-DG VETERANS CHOICE POST VISIT TEXT VA-DG VETERANS CHOICE POST-VISIT INFO VA-DG VETERANS CHOICE PRE-POST SELECT VA-DG VETERANS CHOICE PRE-VISIT INFO VA-DG VETERANS CHOICE PROVIDER