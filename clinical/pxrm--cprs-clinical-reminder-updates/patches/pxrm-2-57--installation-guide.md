---
title: PXRM*2*57 Advance Directive Notification and Screening Reminder Dialog Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Advance Directive Notification and Screening Reminder Dialog Install Guide
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*57
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - strong
  - blockquote
  - advance
  - directive
  - table
  - class
  - installation
  - contents
  - screening
  - notification
page_count: 0
word_count: 2075
section_count: 5
table_count: 6
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: March 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_57_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_57_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-57-advance-directive-notification-and-screening-reminder-dialog-install-g/001.png)

> Advance Directive Notification and Screening Reminder Dialog

> PXRM\*2.0\*57

> INSTALLATION and SETUP GUIDE

> March 2015

#### Product Development Department of Veterans Affairs

1.  Contents
2.  [Introduction 3](#introduction)
3.  [Pre-Installation 4](#pre-installation)
4.  [Installation 6](#installation)
5.  [Post-Installation 9](#post-installation)
    1.  [VistA/CPRS Preparation 9](#vistacprs-preparation)
    2.  [OPTIONAL - Set Up the Advance Directive Notification and Screening Progress Note Title in the VistA Text Integration Utility (TIU) 9](#optional---set-up-the-advance-directive-notification-and-screening-progress-note-title-in-the-vista-text-integration-utility-tiu)
    3.  [OPTIONAL - Activate the Reminder Dialog for TIU Use 15](#optional---activate-the-reminder-dialog-for-tiu-use)
    4.  [OPTIONAL - Link the Advance Directive Notification and Screening Progress Note Title to the VA-ADVANCE DIRECTIVE NOTIFICATION AND SCREENING Reminder Dialog 17](#optional---link-the-advance-directive-notification-and-screening-progress-note-title-to-the-va-advance-directive-notification-and-screening-reminder-dialog)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pre-Installation](#pre-installation)
    - [Required Software for PXRM\2.0\57](#required-software-for-pxrm2057)
    - [Related Documentation](#related-documentation)
    - [Web Sites](#web-sites)
- [Installation](#installation)
- [Post-Installation](#post-installation)
  - [VistA/CPRS Preparation](#vistacprs-preparation)
  - [OPTIONAL - Set Up the Advance Directive Notification and Screening Progress Note Title in the VistA Text Integration Utility (TIU)](#optional-set-up-the-advance-directive-notification-and-screening-progress-note-title-in-the-vista-text-integration-utility-tiu)
  - [OPTIONAL - Activate the Reminder Dialog for TIU Use](#optional-activate-the-reminder-dialog-for-tiu-use)
  - [OPTIONAL - Link the Advance Directive Notification and Screening Progress Note Title to the VA-ADVANCE DIRECTIVE NOTIFICATION AND SCREENING Reminder Dialog](#optional-link-the-advance-directive-notification-and-screening-progress-note-title-to-the-va-advance-directive-notification-and-screening-reminder-dialog)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B - Acronyms](#appendix-b-acronyms)
- [Appendix C – Health Factors and Template Fields](#appendix-c-health-factors-and-template-fields)
> Patch PXRM\*2.0\*57 releases a new reminder dialog template to the field, without any changes to routines, data dictionaries, or other package functions; it deals with content only. The new reminder dialog template is:
> VA-ADVANCE DIRECTIVE NOTIFICATION AND SCREENING.
> This reminder dialog template is mandated for installation, but optional for use. While use of the reminder dialog template is optional, all sites are required to use two of the health factors exported by this template/patch. All sites will have to include the health factors, “Advance Directive Yes” and “Advance Directive No”, in their advance directive notification and screening processes as required by the [<u>Veterans Health Administration (VHA) Handbook</u> <u>1004.02, “Advance Care Planning and Management of Advance Directives.”</u>](http://vaww.va.gov/vhapublications/ViewPublication.asp?pub_ID=2967) The use of this template and the associated health factors will help sites comply with the advance directive notification and screening requirements set forth in this Handbook.
> Facilities will be required to install this template within normal installation timelines as established by OIT. The National Center for Ethics in Health Care (NCEHC) is the Program Office with oversight of this template and its associated processes.
> Sites may wish to associate this reminder dialog template with the local and national enterprise standard progress note title, “ADVANCE DIRECTIVE NOTIFICATION AND SCREENING.”
> Multiple installation steps will be required for this patch installation, and some actions will be optional. These actions should to be accomplished in your VistA/CPRS test account and then transitioned to your live account after successful testing.
> These processes are outlined in the following guidance, but an overview is provided here:
> • Pre-Installation. If your site has locally developed the two health factors, ADVANCE DIRECTIVE YES and ADVANCE DIRECTIVE NO, then you will have to take some pre- installation actions to modify these local health factors to allow for their national health factor equivalents to be installed via this patch. If not, the local health factors will be overwritten by the installation of the national health factors delivered in this patch.
- Post-Installation. Sites will need to ensure that the nationally delivered health factors, ADVANCE DIRECTIVE YES and ADVANCE DIRECTIVE NO, are incorporated into local processes for documenting Advance Directive Notification and Screening, as required by VHA Handbook 1004.02, Advance Care Planning and Management of Advance Directives.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Required Software for PXRM\*2.0\*57

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 25%" />
<col style="width: 24%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Package/Patch</strong></th>
<th><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th><strong>Version</strong></th>
<th><strong>Comments</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Reminders</td>
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td>2.0</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>Health Summary</td>
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td>2.7</td>
<td>Fully patched</td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td><blockquote>
<p>XU</p>
</blockquote></td>
<td>8.0</td>
<td>Fully patched</td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td><blockquote>
<p>DI</p>
</blockquote></td>
<td>22</td>
<td>Fully patched</td>
</tr>
</tbody>
</table>

### Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Documentation            | Documentation File name |
|------------------------------|-----------------------------|
| Installation and Setup Guide | PXRM\*2.0\*57_IG.PDF        |

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 38%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
<th><strong>URL</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>National Clinical Reminders site</td>
<td><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></td>
<td><p>Contains manuals, PowerPoint presentations, and other information about Clinical</p>
<p>Reminders</p></td>
</tr>
<tr class="even">
<td>National Clinical Reminders Committee</td>
<td><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncrc</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>public/default.aspx</u></a></td>
<td><p>This committee directs the development of new and revised</p>
<p>national reminders</p></td>
</tr>
<tr class="odd">
<td>VistA Document Library</td>
<td><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></td>
<td>Contains manuals for Clinical Reminders</td>
</tr>
</tbody>
</table>

> Health Factor Set Up. If your site has <u>locally developed and installed the two health factors,</u> <u>ADVANCE DIRECTIVE YES and ADVANCE DIRECTIVE NO</u>, then you will have to take some pre-installation actions to modify these local health factors, changing their names, to allow for the installation of the national versions of these health factors via this patch. *(\*\*\*Note: The patch installation will overwrite the local health factors with the national health factors if they already exist in your VistA system. However, the associated health factor category will be different and this will likely impact your clinical reminder processes.)*

> • This patch installs multiple national health factors. However, sites may have already locally built the two health factors required to be used at all facilities in accordance with VHA Handbook 1004.02, “Advance Care Planning and Management of Advance Directives.” These are: <u>ADVANCE DIRECTIVE YES</u> and <u>ADVANCE DIRECTIVE NO.</u> Their

> national standardization is needed to support Meaningful Use certification of the VA electronic health record. This patch will either overwrite your local health factors with the same name or fail to import these two national health factors. These issues can be avoided by changing the local health factor names to something else (e.g. ADVANCE DIRECTIVE YES-LOCAL and ADVANCE DIRECTIVE NO-LOCAL.)

> • If needed, change the name of your two local health factors, ADVANCE DIRECTIVE YES and ADVANCE DIRECTIVE NO, to something else (locally determined). This will allow the new health factors to be installed in your Vista system via this patch. Then, after the patch is installed, replace the locally developed health factors in your local reminder dialogs

> and/or clinical reminders with the nationally provided health factors delivered via this patch. Adjust the resolution logic of any clinical reminders to use the new health factors going forward and locally developed health factors for historical instances. This will allow for the use of the new, national health factors in your local processes going forward.

> Changing the name of the Health Factors can be accomplished a couple of ways

- 1\. Using fileman and editing the name of the health factor to include some local designation to differentiate them from the national Health Factors being installed
- 2\. Using menu option PXTT EDIT HEALTH FACTORS

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 1-2 minutes.*

#### The installation needs to be done by a person with DUZ(0) set to "@."

#### Retrieve the host file from one of the following locations (with the ASCII file type):

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 36%" />
<col style="width: 42%" />
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

#### Install the patch first in a training or test account.

#### Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

#### Load the distribution.

#### Using the Kernel Installation & Distribution System menu (XPD MAIN), LOAD the Distribution. Enter \<your directory name\>PXRM_2_0_57.KID at the Host File prompt.

#### Example

#### From the Installation menu, you may elect to use the following options:

#### Backup a Transport Global

#### This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

#### a. Compare Transport Global to Current System

#### This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

#### Install the build.

#### From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*57 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

#### Answer "NO" to the following prompts:

> NO//

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols?

#### NOTE: DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation. A Reminders Manager or CAC should be present to respond to these.

#### Installation Example

#### See [<u>Appendix A</u>.](#appendix-a-installation-example)

#### Install File Print

#### Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

#### Build File Print

#### Use the KIDS Build File Print option to print out the build components.

#### Post-installation routines

#### After successful installation, the following init routines may be deleted:

> PXRMP57E PXRMP57I

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA/CPRS Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the patch is installed, ensure that all health factors installed by this patch have populated into the VistA Patient Care Encounter package, including the correct health factor category (see [<u>Appendix C</u>](#appendix-c-health-factors-and-template-fields) for a list of the expected health factors.) If applicable, your site will need to replace the locally developed health factors in your local reminder dialogs and/or clinical reminders with the nationally provided health factors (ADVANCE DIRECTIVE YES and ADVANCE DIRECTIVE NO) delivered via this patch. Adjust the resolution logic of any clinical reminders to use the new health factors going forward and locally developed health factors for historical instances. This will allow for the use of the new, national health factors in your local processes going forward.

> If you do not have a locally developed clinical reminder or reminder dialog template, you may link the associated reminder dialog template delivered with this patch to the new progress note title, ADVANCE DIRECTIVE NOTIFICATION AND SCREENING. You may also place this reminder dialog template in the Shared Templates section of CPRS Notes, for use with other progress note titles.

## OPTIONAL - Set Up the Advance Directive Notification and Screening Progress Note Title in the VistA Text Integration Utility (TIU)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Advance Directive Notification and Screening progress note title may be built using the Text Integration Utility in VistA. Note: The progress note title associated with this reminder dialog template must NOT be and should not be a CWAD posting progress note title.

> Summary of actions:

1.  Go into CPRS Configuration (Clinical Coordinator) Menu
2.  Follow the menu path: TIU Maintenance Menu \> Document Definitions (Manager)

> \> Create Document Definitions \> Navigate to a locally developed progress note Document Class (*NOT a CWAD Document Class*)\> Title \> Advance Directive Notification and Screening

> Select Option: TIU Maintenance Menu

1.  TIU Parameters Menu ... \[TIU SET-UP MENU\]
2.  Document Definitions (Manager) ... \[TIUF DOCUMENT DEFINITION MGR\]
3.  User Class Management ... \[USR CLASS MANAGEMENT MENU\]
4.  TIU Template Mgmt Functions ... \[TIU IRM TEMPLATE MGMT\]
5.  TIU Alert Tools \[TIU ALERT TOOLS\]

> 7 TIUHL7 Message Manager \[TIUHL7 MSG MGR\]

> Title Mapping Utilities ... \[TIU MAP TITLES MENU\]

> 6 Active Title Cleanup Report \[TIU ACTIVE TITLE CLEANUP\]

> Select TIU Maintenance Menu \<TEST ACCOUNT\> Option: Document Definitions (Manager)

> --- Manager Document Definition Menu ---

1.  Edit Document Definitions
2.  Sort Document Definitions
3.  Create Document Definitions
4.  Create Objects
5.  Create TIU/Health Summary Objects

> Select Document Definitions (Manager) \<TEST ACCOUNT\> Option: Create Document Definitions

1.  Create Document Definitions
2.  Create Objects
3.  Create TIU/Health Summary Objects

> CHOOSE 1-3: 1 Create Document Definitions.............

> ![](pxrm-2-57-advance-directive-notification-and-screening-reminder-dialog-install-g/002.png)

> ![](pxrm-2-57-advance-directive-notification-and-screening-reminder-dialog-install-g/003.png)

> ![](pxrm-2-57-advance-directive-notification-and-screening-reminder-dialog-install-g/004.png)

![](pxrm-2-57-advance-directive-notification-and-screening-reminder-dialog-install-g/005.png)

> The Advance Directive Notification and Screening progress note title has now been created. It is active and available for use.

## OPTIONAL - Activate the Reminder Dialog for TIU Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You will need to activate the VA-ADVANCE DIRECTIVE NOTIFICATION AND SCREENING reminder dialog template for TIU use prior to linking it to the progress note title.

> Summary of actions:

1.  In VistA go to the PCRM Reminder Managers Menu
2.  Follow the menu path: CP – CPRS Reminders Configuration \> TIU - TIU Template Reminder Dialog Parameter \> System

> Select NATIONAL CONTENT DEVELOPMENT \<TEST ACCOUNT\> Option: PXRM

> Reminder Managers Menu

> CF Reminder Computed Finding Management ... RM Reminder Definition Management ...

> SM Reminder Sponsor Management ... TXM Reminder Taxonomy Management ... TRM Reminder Term Management ...

> LM Reminder Location List Management ... RX Reminder Exchange

> RT Reminder Test

> OS Other Supporting Menus ...

> INFO Reminder Information Only Menu ... DM Reminder Dialog Management ...

> CP CPRS Reminder Configuration ...

> RP Reminder Reports ...

> MST Reminders MST Synchronization Management ... PL Reminder Patient List Menu ...

> PAR Reminder Parameters ...

> ROC Reminder Order Check Menu ... XM Reminder Extract Menu ...

> GEC GEC Referral Report

> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: CP CPRS Reminder Configuration

> CA Add/Edit Reminder Categories CL CPRS Lookup Categories

> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active PN Progress Note Headers

> RA Reminder GUI Resolution Active

> TIU TIU Template Reminder Dialog Parameter

> DL Default Outside Location

> PT Position Reminder Text at Cursor NP New Reminder Parameters

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 22%" />
<col style="width: 14%" />
<col style="width: 17%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>1</th>
<th><blockquote>
<p>User</p>
</blockquote></th>
<th>USR</th>
<th>[choose</th>
<th>from NEW PERSON]</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>SRV</td>
<td>[choose</td>
<td>from SERVICE/SECTION]</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>Division</p>
</blockquote></td>
<td>DIV</td>
<td colspan="2"><blockquote>
<p>[SALT LAKE CITY]</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>System</p>
</blockquote></td>
<td>SYS</td>
<td colspan="2"><blockquote>
<p>[NATREM.FO-SLC.MED.VA.GOV]</p>
</blockquote></td>
</tr>
</tbody>
</table>

## OPTIONAL - Link the Advance Directive Notification and Screening Progress Note Title to the VA-ADVANCE DIRECTIVE NOTIFICATION AND SCREENING Reminder Dialog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the VA-ADVANCE DIRECTIVE NOTIFICATION AND SCREENING reminder dialog template is imported via the patch and you have set up the appropriate progress note title, you may add the reminder dialog template to the notes tab in CPRS and link it to the Advance Directive Notification and Screening progress note title.

> You will need the ability to “Edit Shared Templates” in CPRS. Summary of actions:

3.  Go into CPRS Notes tab
4.  Follow the menu path: Options \> Edit Shared Templates \> Template Editor Window
5.  In CPRS, from the Notes Tab
    1.  Select the drop down for “Options”
    2.  Select “Edit Shared Templates”
6.  This will launch the “Template Editor” window.
    1.  Ensure that the box is checked for “Edit Shared Templates”
    2.  Select (single click) “Document Titles”

![](pxrm-2-57-advance-directive-notification-and-screening-reminder-dialog-install-g/006.png)

> While still in the “Template Editor” window:

1.  Select “New Template”
2.  Replace the name “New Template” with “ADVANCE DIRECTIVE NOTIFICATION AND SCREENING”

![](pxrm-2-57-advance-directive-notification-and-screening-reminder-dialog-install-g/007.png)

> While still in the “Template Editor” window:

1.  Select “Reminder Dialog” on the drop down for “Template Type”
2.  Select “VA- ADVANCE DIRECTIVE NOTIFICATION AND SCREENING” on the drop down for “Reminder Dialog”
3.  Select “ADVANCE DIRECTIVE NOTIFICATION AND SCREENING” on the drop down for “Associated Title”
4.  Click “OK”

#### Here is an example of these actions. Please note that some options will be site-specific.

![](pxrm-2-57-advance-directive-notification-and-screening-reminder-dialog-install-g/008.png)

> The VA-ADVANCE DIRECTIVE NOTIFICATION AND SCREENING reminder dialog

> should now be available in CPRS, linked to the CPRS progress note title “Advance Directive Notification and Screening.” Test this by starting a new note with the title “Advance Directive Notification and Screening.” The reminder dialog template should launch and display the reminder dialog wizard.

# Appendix A: Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution Enter a Host File: \<your directory\>PXRM_2_0_57.KID

> KIDS Distribution saved on Dec 22, 2014@10:35:15 Comment: VA-ADVANCED DIRECTIVE

> This Distribution contains Transport Globals for the following Package(s): Build PXRM\*2.0\*57 has been loaded before, here is when:

> PXRM\*2.0\*57 Install Completed

> was loaded on Dec 22, 2014@10:40:37 OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> PXRM\*2.0\*57

> Use INSTALL NAME: PXRM\*2.0\*57 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: INstall Package(s) Select INSTALL NAME: PXRM\*2.0\*57 12/31/14@07:12:11

> =\> VA-ADVANCED DIRECTIVE ;Created on Dec 22, 2014@10:35:15

> This Distribution was loaded on Dec 31, 2014@07:12:11 with header of VA-ADVANCED DIRECTIVE ;Created on Dec 22, 2014@10:35:15

> It consisted of the following Install(s): PXRM\*2.0\*57

> Checking Install for Package PXRM\*2.0\*57 Install Questions for PXRM\*2.0\*57 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

> --------------------------------------------------------------------------------

> Install Started for PXRM\*2.0\*57 : Dec 31, 2014@07:12:24

> Build Distribution Date: Dec 22, 2014 Installing Routines:

> Dec 31, 2014@07:12:24

> Running Pre-Install Routine: PRE^PXRMP57I Installing Data Dictionaries:

> Dec 31, 2014@07:12:24

> Installing Data:

> Dec 31, 2014@07:12:26

> Running Post-Install Routine: POST^PXRMP57I

> There are 1 Reminder Exchange entries to be installed.

> 1\. Installing Reminder Exchange entry PXRM\*2.0\*57 VA-ADVANCE DIRECTIVE NOTIFICATION AND SCREENING (D)

> Updating Routine file... Updating KIDS files... PXRM\*2.0\*57 Installed.

> Dec 31, 2014@07:12:37

> Not a production UCI

> PXRM\*2.0\*57

> Install Completed

# Appendix B - Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### The OIT Master Glossary is available at: [<u>http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm</u>](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

| Term | Definition                                 |
|----------|------------------------------------------------|
| ADNS     | Advance Directive Notification And Screening   |
| CPRS     | Computerized Patient Record System             |
| CWAD     | Crisis, Warning, Allergy and Advance Directive |
| NCEHC    | National Center for Ethics in Health Care      |
| OIT/OI&T | Office of Information Technology               |
| TIU      | Text Integration Utility                       |
| VHA      | Veterans Health Administration                 |
|          |                                                |
|          |                                                |
|          |                                                |
|          |                                                |

# Appendix C – Health Factors and Template Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><blockquote>
<p><strong>ADNS Reminder Dialog - Health Factors</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Health Factor Category</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Health Factor</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Life-Sustaining Treatment Template Location</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>ETHICS-ADVANCE DIRECTIVE SCREENING</td>
<td><strong>ADVANCE DIRECTIVE YES</strong></td>
<td><p>VA-ADNS ADVANCE DIRECTIVE</p>
<p>HEADER YES-ON FILE (G)</p></td>
</tr>
<tr class="odd">
<td>ETHICS-ADVANCE DIRECTIVE SCREENING</td>
<td><strong>ADVANCE DIRECTIVE YES</strong></td>
<td><p>VA-ADNS ADVANCE DIRECTIVE</p>
<p>HEADER YES-NOT ON FILE (G)</p></td>
</tr>
<tr class="even">
<td>ETHICS-ADVANCE DIRECTIVE SCREENING</td>
<td><strong>ADVANCE DIRECTIVE NO</strong></td>
<td>VA-ADNS ADVANCE DIRECTIVE HEADER NO (G)</td>
</tr>
<tr class="odd">
<td>ETHICS-ADVANCE DIRECTIVE SCREENING</td>
<td><p><strong>ADVANCE DIRECTIVE</strong></p>
<p><strong>UNKNOWN</strong></p></td>
<td><p>VA-ADNS ADVANCE DIRECTIVE</p>
<p>HEADER UNKNOWN (G)</p></td>
</tr>
<tr class="even">
<td>ETHICS-ADVANCE DIRECTIVE SCREENING</td>
<td><p><strong>ADVANCE DIRECTIVE-MH</strong></p>
<p><strong>PREFERENCES-YES</strong></p></td>
<td><p>VA-ADNS MH PREFERENCES-YES</p>
<p>(G)</p></td>
</tr>
<tr class="odd">
<td>ETHICS-ADVANCE DIRECTIVE SCREENING</td>
<td><strong>ADVANCE DIRECTIVE-MH PREFERENCES-NO</strong></td>
<td>VA-ADNS MH PREFERENCES-NO (G)</td>
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
<p><strong>CPRS Template Fields Delivered by the ADNS Reminder Dialog</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>VA-ETHICS-LINK-HB-1004-02</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-ETHICS-WORD PROCESS 2 LINES REQ</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-ETHICS-REQ COMMENT-DISP</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-ETHICS-WP 2 LINE</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-ETHICS-OPTIONAL COMMENT-DISP ONLY</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>VA-ETHICS-FORM 10-0137B</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA-ETHICS-FORM 10-0137A</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> 12/31/2014 Clinical Reminders PXRM\*2.0\*57 Installation and Setup Guide 23