---
title: PXRM*2*39 Airborne Hazard/Open Burn Pit Evaluation Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Airborne Hazard/Open Burn Pit Evaluation
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*39
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 4
description: 
audience: 
keywords: 
  - blockquote
  - class
  - style
  - width
  - even
  - table
  - element
  - strong
  - order
  - colgroup
page_count: 0
word_count: 7907
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: November 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_39_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_39_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-39-airborne-hazard-open-burn-pit-evaluation-installation-guide/001.png)

> Airborne Hazard and Open Burn Pit Initial Evaluation Reminder Dialog

> PXRM\*2.0\*39

## INSTALLATION and SETUP GUIDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> November 2014

#### Product Development Department of Veterans Affairs

> <u>Contents</u>

[INTRODUCTION 3](#introduction)

[PRE-INSTALLATION 6](#_bookmark1)

Required Software for patch PXRM 6

1.  Retrieve the host file containing the patch 7
2.  Install the build first in a training or test account 7
3.  [Load the distribution. 7](#_TOC_250002)
    1.  Verify Checksums in Transport Global 7
4.  Install the build. 8
5.  Install File Print 8
6.  Build File Print 9
7.  Post-installation routines 9

[POST-INSTALLATION SETUP 6](#_bookmark3)

[APPENDIX A](#_bookmark5) INSTALLATION EXAMPLE 30

[APPENDIX B HEALTH FACTOR LIST 32](#_TOC_250001)

[ACRONYMS 35](#_TOC_250000)

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [INSTALLATION and SETUP GUIDE](#installation-and-setup-guide)
- [Introduction](#introduction)
- [Pre-Installation](#pre-installation)
    - [Related Documentation](#related-documentation)
- [Installation](#installation)
- [Post-Installation Setup](#post-installation-setup)

#### This patch releases the Airborne Hazard and Open Burn Pit Registry Initial Evaluation reminder dialog without any changes to routines, data dictionaries, or other package functions – “content” only. The reminder dialog is VA-AH-BPR INITIAL EVALUATION NOTE

> Airborne Hazard and Open Burn Pit Registry Initial Evaluation
> The Airborne Hazard and Burn Pit Registry Clinical Reminder Dialog Template was developed by the War-Related Illness and Injury Study Center (WRIISC) and Office of Public Health - Post-Deployment Health. The purpose of this template is to support the provider in a focused evaluation of a Veteran who requests an examination after completing the Airborne Hazards and Open Burn Pit Registry Self-Assessment. The template may also be useful for encounters where deployment health concerns are expressed regardless of whether the Veteran is participating in the registry. The template may be completed by a primary care provider, environmental health clinician, post-deployment champion, or a pulmonologist. This template is critical to improving the process and documentation of clinical care, and facilitating high quality care and programmatic quality improvement.

####### Recommendations

> It is recommended that the reminder dialog first be installed into TEST account. After installation into TEST account the CAC/HIS will need to provide the appropriate stakeholder(s) access to TEST account so the dialog can be reviewed. The stakeholders should be familiar with the functionality and content of the dialog before implementing into Production.
> This dialog should be linked to the progress note title, AIRBORNE HAZARD/BURN PIT REGISTRY INITIAL EVALUATION NOTE. The CAC/HIS will need to create the note title and link it to the VHA Enterprise Standard Title, PERSIAN GULF REGISTRY E & M NOTE. [<u>Instructions are included.</u>](#create-note-title-airborne-hazardburn-pit-registry-initial-evaluation-note)
1.  Component Inventory
> The VA-AH-BPR INITIAL EVALUATION NOTE Reminder Dialog contains:
- 1 dialog
- 3 branching terms
- 21 TIU objects
- 7 Health Factor categories
- 68 Health Factors
- 2 TIU template fields
- 1 Sponsor
1.  Reminder Dialog Name:
> VA-AH-BPR INITIAL EVALUATION NOTE

####### Terms:

> The following three branching reminder terms are exported with the reminder. These terms require local modification and mapping. Instructions are included.
> VA-AH-BPR AUDIT C DUE (BRANCHING LOGIC)
> VA-AH-BPR PTSD SCREEN DUE (BRANCHING LOGIC)
> VA-AH-BPR DEPRESSION SCREEN DUE (BRANCHING LOGIC)
2.  Local Order Dialogs
> The dialog has eight elements used for ordering appropriate interventions through the note. The “Additional findings” field in the elements will need to be mapped to the correct local order dialog (quick order, generic order, order set, or order menu). Instructions are included below.
3.  Local Groups/Elements
> The dialog has several “Local” groups and elements, so each site can configure the section as necessary. The local groups/elements begin with the namespace AH-BPR and are not prefixed with VA-.
1.  The dialog has a group named AH-BPR MEDS LOCAL RECONCILIATION designated as local”, so each site can add local groups/elements to meet medication reconciliation documentation requirements. The group is active with installation. If it is not needed it must be inactivated, so it doesn’t display in the dialog.
2.  All groups and elements that include a TIU object are designated “local” in case a site can’t map to their documentation methods. An example is the element AH-BPR PFT RESULTS. If a site captures PFT results in a method that proves impossible to map a TIU Object, then this element can be inactivated at the site, so that option does not display in CPRS. Another option is for the site to include information in the element directing the provider to the PFT results.
    1.  Patient data objects:
> Twenty-one TIU/health summary objects/types will install with this patch; however, only twelve are new. The new health summary types will need to be mapped to local items. Instructions are included. The nine existing TIU objects should not require local modification, but are included below for reference.
> NOTICE: The GMTSMGR security key is necessary for the staff responsible for mapping the health summary types.
<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 35%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>TIU Object Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Health Summary Object Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Health Summary Type Name</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>AH-BPR PULM CONSULT RESULTS;1;2Y</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR PULM CONSULT RESULTS;1;2Y</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR PULM CONSULT;1;2Y</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>AH-BPR ENT CONSULT RESULTS;1;2Y</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR ENT CONSULT RESULTS;1;2Y</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR ENT CONSULT;1;2Y</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>AH-BPR ABG;1;2Y</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR ABG;1;2Y</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR ABG;1;2Y</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>AH-BPR ECHO;1;2Y</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR ECHO;1;2Y</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR ECHO;1;2Y</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>AH-BPR CHEST CT;1;2Y</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR CHEST CT;1;2Y</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR CHEST CT;1;2Y</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>AH-BPR PFT RESULTS;1;2Y</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR PFT RESULTS;1;2Y</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR PFT RESULTS;1;2Y</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>AH-BPR CHEST 2 VIEWS;1;2Y</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR CHEST 2 VIEWS;1;2Y</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR CHEST 2 VIEWS;1;2Y</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>AH-BPR CBC W/DIFF;1;2Y</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR CBC W/DIFF;1;2Y</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR CBC W/DIFF;1;2Y</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>AH-BPR PULSE OX</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR PULSE OX</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR PULSE OX</p>
</blockquote></td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 33%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>AH-BPR AUDIT-C</strong></p>
</blockquote></th>
<th><blockquote>
<p>AH-BPR AUDIT-C</p>
</blockquote></th>
<th><blockquote>
<p>AH-BPR AUDIT-C</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>AH-BPR PC-PTSD PCL</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR PC-PTSD PCL</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR PC-PTSD PCL</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>AH-BPR DEPRESSION SCREEN</strong></p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR DEPRESSION SCREEN</p>
</blockquote></td>
<td><blockquote>
<p>AH-BPR DEPRESSION SCREEN</p>
</blockquote></td>
</tr>
</tbody>
</table>
> <span id="_bookmark1" class="anchor"></span><u>New TIU objects:</u>
> <u>Existing TIU objects:</u> These should require no local configuration.
> PATIENT WEIGHT PATIENT HEIGHT PAIN
> BLOOD PRESSURE RESPIRATION PULSE TEMPERATURE
> ACTIVE MEDICATIONS
> VA-WRIISC ACTIVE PROBLEMS
2.  [Health Factors:](#_bookmark6)
> There are 7 new health factors categories containing 68 new health factors.
> Three health factors should already exist; CURRENT SMOKER, PREVIOUS SMOKER, and LIFETIME NON-SMOKER.

# Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Required Software for PXRM\*2\*39*

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
<tr class="even">
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

### Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<p>PXRM_2_0_39_IG.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td></td>
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
<p>This committee directs the development of new and revised</p>
<p>national reminders</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA Document</p>
<p>Library</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></p>
</blockquote></td>
<td><blockquote>
<p>Contains manuals for Clinical</p>
<p>Reminders and</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark3" class="anchor"></span>*This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes*

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

1.  Install the patch first in a training or test account.

#### Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

2.  <span id="_TOC_250002" class="anchor"></span>Load the distribution.

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name. KID at the Host File prompt.

> Example

> From the Installation menu, you may elect to use the following options:

3.  Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

1.  Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

4.  Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*36 and proceed with

> the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// NO

> Installation Example

> See [<u>Appendix A.</u>](#_bookmark5)

5.  Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

6.  Build File Print

> Use the KIDS Build File Print option to print out the build components.

7.  Post-installation routines

> After successful installation, the following init routines may be deleted:

> PXRMP39E PXRMP39I

# Post-Installation Setup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Post Install Details

> The CAC/HIS has several steps to complete after the patch is installed before the dialog should be deployed. Detailed instructions for each step are below. PXRM_2_0_39_CAC_CKLIST.PDF is available as part of the documentation for this patch. This is a checklist that will help ensure you have done everything correctly.

2.  Configure three reminder terms for branching logic

> Three reminder terms need to be modified to local practice before deployment.

> Before beginning, identify the local reminder definitions in use for Depression screening (PHQ-2), PTSD screening, and Alcohol Use screening (AUDIT-C). All have been deployed nationally; however, sites may have created local versions.

> CF Reminder Computed Finding Management ... RM Reminder Definition Management ...

> SM Reminder Sponsor Management ... TXM Reminder Taxonomy Management ... TRM Reminder Term Management ...

> LM Reminder Location List Management ... RX Reminder Exchange

> RT Reminder Test

> OS Other Supporting Menus ...

> INFO Reminder Information Only Menu ... DM Reminder Dialog Management ...

> CP CPRS Reminder Configuration ... RP Reminder Reports ...

> Select Reminder Managers Menu Option: TRM

> TL List Reminder Terms

> TI Inquire about Reminder Term TE Add/Edit Reminder Term

> TC Copy Reminder Term

> Select Reminder Term Management \<TEST ACCOUNT\> Option: TE

> Select Reminder Term: VA-AH-BPR AUDIT C DUE (BRANCHING LOGIC)

> Reminder Term has no findings!

> Select Finding: CF.VA-REMINDER DEFINITION

> Searching for a REMINDER COMPUTED FINDING, (pointed-to by FINDING ITEM)

> Searching for a REMINDER COMPUTED FINDING VA-REMINDER DEFINITION NATIONAL

> ...OK? Yes// Yes

> Are you adding 'VA-REMINDER DEFINITION' as a new FINDINGS (the 1ST for this REMINDER TERM)? No// Yes

> Computed Finding Description: *Description removed from this document*

> Editing Finding Number: 1

> FINDING ITEM: VA-REMINDER DEFINITION// BEGINNING DATE/TIME:

> ENDING DATE/TIME:

> OCCURRENCE COUNT:

> COMPUTED FINDING PARAMETER: *Enter exact name of your site’s definition in use*

########  for alcohol use screening using the AUDIT-C

> CONDITION: I V("STATUS")\["DUE" CONDITION CASE SENSITIVE: NO USE STATUS/COND IN SEARCH:

> Choose from:

> CF VA-REMINDER DEFINITION Finding \# 1

> Select Finding:

> Input your edit comments. Edit? NO//

> Select Reminder Term: VA-AH-BPR DEPRESSION SCREEN DUE (BRANCHING LOGIC)

> Reminder Term has no findings!

> Select Finding: CF.VA-REMINDER DEFINITION

> Searching for a REMINDER COMPUTED FINDING, (pointed-to by FINDING ITEM)

> Searching for a REMINDER COMPUTED FINDING VA-REMINDER DEFINITION NATIONAL

> ...OK? Yes// Yes

> Are you adding 'VA-REMINDER DEFINITION' as a new FINDINGS (the 1ST for this REMINDER TERM)? No// Yes

> Computed Finding Description: *Description removed from this document*

> Editing Finding Number: 1

> FINDING ITEM: VA-REMINDER DEFINITION// BEGINNING DATE/TIME:

> ENDING DATE/TIME:

> OCCURRENCE COUNT:

> COMPUTED FINDING PARAMETER: *Enter exact name of your site’s definition in use*

########  for depression screening using the PHQ-2 or PHQ9

> *depending on which one your site uses for*

> *depression screening*

> CONDITION: I V("STATUS")\["DUE" CONDITION CASE SENSITIVE: NO USE STATUS/COND IN SEARCH:

> Choose from:

> CF VA-REMINDER DEFINITION Finding \# 1

> Select Finding:

> Input your edit comments. Edit? NO//

> Select Reminder Term: VA-AH-BPR PTSD SCREEN DUE (BRANCHING LOGIC)

> Reminder Term has no findings!

> Select Finding: CF.VA-REMINDER DEFINITION

> Searching for a REMINDER COMPUTED FINDING, (pointed-to by FINDING ITEM)

> Searching for a REMINDER COMPUTED FINDING VA-REMINDER DEFINITION NATIONAL

> ...OK? Yes// Yes

> Are you adding 'VA-REMINDER DEFINITION' as a new FINDINGS (the 1ST for this REMINDER TERM)? No// Yes

> Computed Finding Description: *Description removed from this document*

> Editing Finding Number: 1

> FINDING ITEM: VA-REMINDER DEFINITION// BEGINNING DATE/TIME:

> ENDING DATE/TIME:

> OCCURRENCE COUNT:

> COMPUTED FINDING PARAMETER: *Enter exact name of your site’s definition in use*

########  for PTSD screening.

> CONDITION: I V("STATUS")\["DUE" CONDITION CASE SENSITIVE: NO USE STATUS/COND IN SEARCH:

> Choose from:

> CF VA-REMINDER DEFINITION Finding \# 1

> Select Finding:

> Input your edit comments. Edit? NO//

3.  Configure the 12 new TIU objects/Health Summary objects/types

> NOTICE: The GMTSMGR security key is necessary for the staff responsible for mapping the health summary types.

> If the following message is displayed when accessing the health summary types you will need to have the GMTSMGR security key added to your profile before beginning:

> “Alteration of this summary report is restricted to its owner. See the Clinical Coordinator if you need additional help.”

> All of the TIU objects are already embedded in the dialog, but will not display information until the health summary type for each one is mapped to local items. Before beginning, identify the following local information for each object/type. Detailed instructions for editing the health summary types follow.

1.  HEALTH SUMMARY TYPE: AH-BPR PULM CONSULT;1;2Y
    1.  What note title is used to result Pulmonary consults?
2.  HEALTH SUMMARY TYPE: AH-BPR ENT CONSULT;1;2Y
    1.  What note title is used to result ENT consults?
3.  HEALTH SUMMARY TYPE: AH-BPR ABG;1;2Y
    1.  What are the local lab test name(s) for an ABG?
4.  HEALTH SUMMARY TYPE: AH-BPR ECHO;1;2Y
    1.  How are echo results stored locally?
    2.  If a note title, then what is the title?
5.  HEALTH SUMMARY TYPE: AH-BPR CHEST CT;1;2Y
    1.  What are the local imaging test names for CT THORAX with and/or without contrast?
6.  HEALTH SUMMARY TYPE: AH-BPR PFT RESULTS;1;2Y
    1.  How are PFT results stored locally?
    2.  If a note title, then what is the title?
7.  HEALTH SUMMARY TYPE: AH-BPR CHEST 2 VIEWS;1;2Y
    1.  What are the local imaging test names for chest PA & LAT x-rays?
8.  HEALTH SUMMARY TYPE: AH-BPR CBC W/DIFF;1;2Y
    1.  What are the local lab test name(s) for a CBC w/diff?
9.  HEALTH SUMMARY TYPE: AH-BPR PULSE OX
    1.  Nothing needed
10. HEALTH SUMMARY TYPE: AH-BPR AUDIT-C
    1.  Nothing needed
11. HEALTH SUMMARY TYPE: AH-BPR PC-PTSD PCL
    1.  Nothing needed
12. HEALTH SUMMARY TYPE: AH-BPR DEPRESSION SCREEN
    1.  What is the local name of the depression screening reminder definition?

> Health Summary Maintenance Menu

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

> Select Health Summary Maintenance Menu Option: 6

> Select Health Summary Type: AH-BPR PULM CONSULT;1;2Y

> AH-Bpr Pulm Consult;1;2y (Pulmonary Consult Results, HS Owner <span class="mark">REDACTED</span>)

> OK? YES

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES

> NAME: AH-BPR PULM CONSULT;1;2Y Replace

> TITLE: Pulmonary Consult Results Replace SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: SPN PROGRESS NOTES SELECTED SPN

> SUMMARY ORDER: 5// 5 OCCURRENCE LIMIT: 1 TIME LIMIT: 2Y

> HEADER NAME: Selected Prog Notes// Pulmonary Consult No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select any number of items.

> Select SELECTION ITEM: *Enter exact name of progress note title. You can enter more than one at the next prompt if needed.*

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR PULM CONSULT;1;2Y

> Title: Pulmonary Consult Results Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td>Component Name Occ</td>
<td>Time Loc</td>
<td>Text</td>
<td>Nar</td>
<td>Mod</td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SPN 5 Pulmonary consult 1 2Y

> PULMONARY CONSULT RESULT NOTE

> Select Health Summary Type: AH-BPR ENT CONSULT;1;2Y

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES

> NAME: AH-BPR ENT CONSULT;1;2Y Replace

> TITLE: ENT Consult Results//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: SPN PROGRESS NOTES SELECTED SPN

> SUMMARY ORDER: 5// 5

> OCCURRENCE LIMIT: 1 TIME LIMIT: 2Y

> HEADER NAME: Selected Prog Notes// ENT Consult No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select any number of items.

> Select SELECTION ITEM: *Enter exact name of progress note title. You can enter more than one at the next prompt if needed.*

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR ENT CONSULT;1;2Y

> Title: ENT Consult Results Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td>Component Name Occ</td>
<td>Time Loc</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td>Nar</td>
<td><blockquote>
<p>Mod</p>
</blockquote></td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SPN 5 ENT consult info 1 2Y

> ENT CONSULT RESULT NOTE

> Select Health Summary Type: AH-BPR ABG;1;2Y

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES NAME: AH-BPR ABG;1;2Y//

> TITLE: ABG//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: SLT LAB TESTS SELECTED SLT

> SUMMARY ORDER: 5// 5 OCCURRENCE LIMIT: 1 TIME LIMIT: 2Y

> HEADER NAME: Lab Tests Selected// Last ABG No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select up to 99 items.

> Select SELECTION ITEM: *Enter exact name of local ABG lab test. You can enter more than one at the next prompt if needed.*

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR ABG;1;2Y

> Title: ABG Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td>Component Name Occ</td>
<td>Time Loc</td>
<td>Text</td>
<td>Nar</td>
<td>Mod</td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SLT 5 Last ABG 1 2Y

> ABG

> Select Health Summary Type: AH-BPR ECHO;1;2Y

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES NAME: AH-BPR ECHO;1;2Y//

> TITLE: Echo//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: SPN PROGRESS NOTES SELECTED SPN

######## If local results are not stored with a progress note title, then a different component should be chosen.

> SUMMARY ORDER: 5// 5 OCCURRENCE LIMIT: 1 TIME LIMIT: 2Y

> HEADER NAME: Selected Prog Notes// Last Echo No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select any number of items.

> Select SELECTION ITEM: *Enter exact name of progress note title. You can enter more than one at the next prompt if needed.*

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR ECHO;1;2Y

> Title: Echo Owner:

<table>
<colgroup>
<col style="width: 64%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN</th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Max Hos</td>
<td>ICD</td>
<td><blockquote>
<p>Pro</p>
</blockquote></td>
<td><blockquote>
<p>CPT</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Abb Ord Component Name Occ Time Loc</td>
<td>Text</td>
<td>Nar</td>
<td><blockquote>
<p>Mod Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SPN 5 Last Echo 1 2Y

> CP ECHO

> Select Health Summary Type: AH-BPR CHEST CT;1;2Y

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES NAME: AH-BPR CHEST CT;1;2Y Replace

> TITLE: Chest CT//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: SII IMAGING IMPRESSION SELECTED SII

> SUMMARY ORDER: 5// 5 OCCURRENCE LIMIT: 1 TIME LIMIT: 2Y

> HEADER NAME: Sel Image Impression Replace ... With Last Chest CT No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select any number of items.

######## Select SELECTION ITEM: Enter exact name of Thorax Chest CT with and/or without contrast imaging tests. You can enter more than one at the next prompt if needed.

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR CHEST CT;1;2Y

> Title: Chest CT Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td>Component Name Occ</td>
<td>Time Loc</td>
<td>Text</td>
<td>Nar</td>
<td>Mod</td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SII 5 Last Chest CT 5 2Y

> CT THORAX W&W/O CONT CT THORAX W/CONT

> CT THORAX W/O CONT

> Select Health Summary Type: AH-BPR PFT RESULTS;1;2Y

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES

> NAME: AH-BPR PFT RESULTS;1;2Y Replace

> TITLE: PFT Results//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes//

> SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: SPN PROGRESS NOTES SELECTED SPN

######## If local results are not stored with a progress note title, then a different component should be chosen.

> SUMMARY ORDER: 5// 5 OCCURRENCE LIMIT: 1 TIME LIMIT: 2Y

> HEADER NAME: Selected Prog Notes// Last PFT No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select any number of items.

> Select SELECTION ITEM: *Enter exact name of progress note title. You can enter more than one at the next prompt if needed.*

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR PFT RESULTS;1;2Y

> Title: PFT Results Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table style="width:100%;">
<colgroup>
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td>Component Name Occ</td>
<td>Time Loc</td>
<td>Text</td>
<td>Nar</td>
<td>Mod</td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SPN 5 Last PFT 1 2Y

> CP PFT

> Select Health Summary Type: AH-BPR CHEST 2 VIEWS;1;2Y

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES

> NAME: AH-BPR CHEST 2 VIEWS;1;2Y Replace

> TITLE: Chest x-ray 2 views//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: SII IMAGING IMPRESSION SELECTED SII

> SUMMARY ORDER: 5// 5 OCCURRENCE LIMIT: 1

> TIME LIMIT: 2Y

> HEADER NAME: Sel Image Impression Replace ... With Last Chest x-ray No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select any number of items.

######## Select SELECTION ITEM: Enter exact name of Chest x-ray PA & LAT imaging tests. You can enter more than one at the next prompt if needed.

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR CHEST 2 VIEWS;1;2Y

> Title: Chest x-ray 2 views Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td>Component Name Occ</td>
<td>Time Loc</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td>Nar</td>
<td><blockquote>
<p>Mod</p>
</blockquote></td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SII 5 Last Chest x-ray 1 2Y

> CHEST 2 VIEWS PA&LAT CHEST 4 VIEWS

> Select Health Summary Type: AH-BPR CBC W/DIFF;1;2Y

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES

> NAME: AH-BPR CBC W/DIFF;1;2Y Replace

> TITLE: CBC w/diff//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: : SLT LAB TESTS SELECTED SLT

> SUMMARY ORDER: 5// 5 OCCURRENCE LIMIT: 1 TIME LIMIT: 2Y

> HEADER NAME: Lab Tests Selected// Last CBC w/DIFF No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select up to 99 items.

######## Select SELECTION ITEM: Enter exact name of local CBC w/diff lab tests. You may need to enter the individual lab tests separately.

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR CBC W/DIFF;1;2Y

> Title: CBC w/diff Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 26%" />
<col style="width: 8%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Abb</p>
</blockquote></th>
<th><blockquote>
<p>Ord</p>
</blockquote></th>
<th><blockquote>
<p>Component Name</p>
</blockquote></th>
<th><blockquote>
<p>Max Occ</p>
</blockquote></th>
<th><blockquote>
<p>Hos</p>
<p>Time Loc</p>
</blockquote></th>
<th><blockquote>
<p>ICD</p>
<p>Text</p>
</blockquote></th>
<th><blockquote>
<p>Pro Nar</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
<p>Mod</p>
</blockquote></th>
<th><blockquote>
<p>Selection</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SLT</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>Last CBC w/diff</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>2Y</p>
</blockquote></td>
<td colspan="4"></td>
</tr>
<tr class="even">
<td colspan="5" rowspan="16"></td>
<td colspan="4"><blockquote>
<p>WBC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>RBC</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>HGB</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>HCT</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>MCV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>MCH</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>MCHC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>PLT</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>RDW</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>SEGS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>BANDS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>LYMPHS</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>MONOS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>EOSINO</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="4"><blockquote>
<p>BASO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="4"><blockquote>
<p>PLT (ESTM)</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select Health Summary Type: AH-BPR PULSE OX

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES NAME: AH-BPR PULSE OX//

> TITLE: Pulse Oximetry//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: VITAL SIGNS SELECTED

> SUMMARY ORDER: 5// 5 OCCURRENCE LIMIT: 1 TIME LIMIT:

> HEADER NAME: Vital Signs Selected Replace ... With PO2: No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select any number of items.

> Select SELECTION ITEM: PULSE OXIMETRY

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR PULSE OX

> Title: Pulse Oximetry Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td>Component Name Occ</td>
<td>Time Loc</td>
<td><blockquote>
<p>Text</p>
</blockquote></td>
<td>Nar</td>
<td><blockquote>
<p>Mod</p>
</blockquote></td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> SVS 5 PO2: 1

> PULSE OXIMETRY

> Select Health Summary Type: AH-BPR AUDIT-C

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES NAME: AH-BPR AUDIT-C//

> TITLE: AUDIT-C//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Select COMPONENT: MHAS MHA Score MHAS SUMMARY ORDER: 5// 5

> HEADER NAME: MHA Score// AUDIT-C:

> Select SELECTION ITEM: AUDC

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR AUDIT-C

> Title: AUDIT-C Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
<th><blockquote>
<p>Pro</p>
</blockquote></th>
<th><blockquote>
<p>CPT</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord Component Name</td>
<td>Occ</td>
<td>Time Loc</td>
<td>Text</td>
<td>Nar</td>
<td>Mod</td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> MHAS 5 AUDIT-C: 1 AUDC

> Select Health Summary Type: AH-BPR DEPRESSION SCREEN

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES

> NAME: AH-BPR DEPRESSION SCREEN Replace

> TITLE: Depression Screen//

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Do you wish to copy COMPONENTS from an existing Health Summary Type? YES// NO Select COMPONENT: CF CLINICAL REMINDERS FINDINGS CF

> SUMMARY ORDER: 5// 5

> HEADER NAME: Reminders Findings// Depression Screen No selection items chosen.

> Select new items one at a time in the sequence you want them displayed. You may select any number of items.

> Select SELECTION ITEM: VA-DEPRESSION SCREENING

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR DEPRESSION SCREEN

> Title: Depression Screen Owner:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
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
<td>Component Name Occ</td>
<td>Time Loc</td>
<td>Text</td>
<td>Nar</td>
<td><blockquote>
<p>Mod Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> CF 5 Reminders Findings

> Select Health Summary Type: AH-BPR PC-PTSD PCL

> VA-DEPRESSION SCREENING

> WARNING: You are about to edit a Health Summary Type that is being used by a Health Summary Object. Changing the structure of this Health Summary Type will alter how the Object will display.

> Do want to continue? NO// YES NAME: AH-BPR PC-PTSD PCL// TITLE: PTSD Screen:

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes// SUPPRESS SENSITIVE PRINT DATA: NO SSN//

> Select COMPONENT: MHAS MHA Score MHAS SUMMARY ORDER: 5// 5

> HEADER NAME: MHA Score// PTSD Screen:

> Select SELECTION ITEM: PC PTSD

> The Health Summary Type structure should look similar to this:

> Type Name: AH-BPR PC-PTSD PCL

> Title:

> Owner: FAHNER,JEFF

> SUPPRESS PRINT OF COMPONENTS WITHOUT DATA: yes SUPPRESS SENSITIVE PRINT DATA: NO SSN

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Max</th>
<th>Hos</th>
<th>ICD</th>
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
<td>Abb Ord Component Name</td>
<td>Occ</td>
<td>Time Loc</td>
<td>Text</td>
<td>Nar</td>
<td><blockquote>
<p>Mod Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> MHAS 5 MHA Score 2

> PC PTSD PCLC PCLM

####### Add appropriate local order dialogs to order section

> Eight local orders need to be added to eight separate elements in the dialog. . Before beginning, identify the following local information for each element. Detailed instructions for editing the health summary types follow.

1.  Identify local order dialog name for an outpatient Chest X-ray PA & LAT.
2.  Identify local order dialog name for an outpatient Pulmonary Function Test.
3.  Identify local order dialog name for an outpatient Chest CT w & w/o contrast.
4.  Identify local order dialog name for an outpatient echo.
5.  Identify local order dialog name for an outpatient ABG.
6.  Identify local order dialog name for an outpatient CBC w/diff.
7.  Identify local order dialog name for an outpatient ENT Consult.
8.  Identify local order dialog name for an outpatient Pulmonary Consult From the Reminder Manager’s Menu

> CF Reminder Computed Finding Management ... RM Reminder Definition Management ...

> SM Reminder Sponsor Management ... TXM Reminder Taxonomy Management ... TRM Reminder Term Management ...

> LM Reminder Location List Management ... RX Reminder Exchange

> RT Reminder Test

> OS Other Supporting Menus ...

> INFO Reminder Information Only Menu ... DM Reminder Dialog Management ...

> CP CPRS Reminder Configuration ... RP Reminder Reports ...

> MST Reminders MST Synchronization Management ... PL Reminder Patient List Menu ...

> PAR Reminder Parameters ...

> ROC Reminder Order Check Menu ... XM Reminder Extract Menu ...

> GEC GEC Referral Report

> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: DM

> DP Dialog Parameters ... DI Reminder Dialogs

> DR Dialog Reports ...

> IA Inactive Codes Mail Message

> Select Reminder Dialog Management \<TEST ACCOUNT\> Option: DI REMINDER VIEW (ALL REMINDERS BY NAME)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 5%" />
<col style="width: 20%" />
<col style="width: 31%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Item</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>Reminder Name</p>
</blockquote></th>
<th><blockquote>
<p>Linked Dialog Name &amp;</p>
</blockquote></th>
<th><blockquote>
<p>Dialog</p>
</blockquote></th>
<th><blockquote>
<p>Status</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>ACUTE MYOCARDIAL INFARCTION</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>AGP TEST</p>
</blockquote></td>
<td><blockquote>
<p>AGP TEST ALL DIALOG</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>CF ALLERGY TEST</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>CHEST XRAY</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>CHOLESTEROL SCREEN (M)</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>CRITICAL DRUG</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>DEPRESSION SCREEN</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>FAHNER TEST REMINDER</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>LONG TERM STEROID USE</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>MAMMOGRAM</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>MAMMOGRAMS</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>MAMMOGRAPHY</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>13</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PAP SMEAR</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>14</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PATCH 11 LOCATION LIST</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PPD</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>PPD1</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>+</p>
</blockquote></td>
<td><blockquote>
<p>Enter ??</p>
</blockquote></td>
<td><blockquote>
<p>for</p>
</blockquote></td>
<td><blockquote>
<p>more actions</p>
</blockquote></td>
<td colspan="3">&gt;&gt;&gt;</td>
</tr>
</tbody>
</table>

> AR All reminders LR Linked Reminders QU Quit CV Change View RN Name/Print Name

> Select Item: Next Screen// CV Select one of the following:

4.  Reminder Dialogs
5.  Dialog Elements
6.  Forced Values
7.  Dialog Groups

> P Additional Prompts

> R Reminders

> RG Result Group (Mental Health)

> RE Result Element (Mental Health)

> TYPE OF VIEW: R// D

> DIALOG VIEW (REMINDER DIALOGS - SOURCE REMINDER NAME)

> Item Reminder Dialog Name Source Reminder Status

1.  AGP TEST ALL DIALOG \*NONE\* Linked
2.  AWAT PACK TEST \*NONE\*
3.  AWJF TEST \*NONE\*
4.  CCHT (2 DATA OBJECTS ONLY) \*NONE\* Disabled
5.  NCEHC LIFE SUSTAINING TREATMENT PLAN \*NONE\*
6.  PVC HIDE AND SUPPRESS TEST \*NONE\*
7.  PVC TEST \*NONE\*
8.  VA ONCOLOGY LUNG \*NONE\*
9.  VA-AAA SCREENING \*NONE\* Linked
10. VA-AH-BPR INITIAL EVALUATION NOTE \*NONE\*
11. VA-AIMS VA-ANTIPSYCHOTIC MED SIDE Linked
12. VA-ALCOHOL F/U POS AUDIT-C \*NONE\* Linked
13. VA-ALCOHOL USE SCREENING (AUDIT-C) \*NONE\* Linked
14. VA-CSP ANNUAL IN-HOME ASSESSMENT CHILD\*NONE\*
15. VA-CSP ANNUAL IN-HOME ASSESSMENT REV \*NONE\*
16. VA-CSP CLIN ELIG CHILD NOTE \*NONE\*

> \+ + Next Screen - Prev Screen ?? More Actions

> \>\>\>

> AD Add Reminder Dialog PT List/Print All QU Quit CV Change View RN Name/Print Name

> Select Item: Next Screen// *Find VA-AH-BPR INITIAL EVALUATION NOTE dialog and select the appropriate item number to open the dialog*

> REMINDER DIALOG NAME: VA-AH-BPR INITIAL EVALUATION NOTE

> <u>+Item Seq. Dialog Summary</u>

184. 35.25.5 Element: VA-AH-BPR ASSESSMENT AND PLAN ADDL INFO
185. 35.25.10 Element: VA-AH-BPR WORD PROCESSING 5 LINES
186. 35.30 Element: VA-AH-BPR SPACE (NOTE ONLY)
187. 35.35 Group: VA-AH-BPR ORDERS
188. 35.35.2 Group: VA-AH-BPR DIAGNOSTIC EVAL DISPLAY ONLY OPTION
189. 35.35.2.5 Group: VA-AH-BPR DIAGNOSTIC EVAL DISPLAY ONLY
190. 35.35.5 Element: VA-AH-BPR ORDER CHEST XRAY- PA AND LATERAL
191. 35.35.10 Element: VA-AH-BPR ORDER FULL PULMONARY FUNCTION TESTS

> \+ + Next Screen - Prev Screen ?? More Actions

> \>\>\>

> ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print CO Copy Dialog DO Dialog Overview QU Quit

> DD Detailed Display DT Dialog Text

> DP Progress Note Text ED Edit/Delete Dialog

> Select Item: Next Screen// *Find* VA-AH-BPR ORDER CHEST XRAY- PA AND LATERAL

######## and select the appropriate item number to open the element

> Current dialog element/group name: VA-AH-BPR ORDER CHEST XRAY- PA AND LATERAL Used by: VA-AH-BPR ORDERS (Current Reminder Dialog)

> FINDING ITEM: AH-BPR ORDER CHEST XRAY //

> Select ADDITIONAL FINDINGS: Q.*Enter exact name of local order dialog*

> REMINDER DIALOG NAME: VA-AH-BPR INITIAL EVALUATION NOTE

> <u>+Item Seq. Dialog Summary</u>

184. 35.25.5 Element: VA-AH-BPR ASSESSMENT AND PLAN ADDL INFO
185. 35.25.10 Element: VA-AH-BPR WORD PROCESSING 5 LINES
186. 35.30 Element: VA-AH-BPR SPACE (NOTE ONLY)
187. 35.35 Group: VA-AH-BPR ORDERS
188. 35.35.2 Group: VA-AH-BPR DIAGNOSTIC EVAL DISPLAY ONLY OPTION
189. 35.35.2.5 Group: VA-AH-BPR DIAGNOSTIC EVAL DISPLAY ONLY
190. 35.35.5 Element: VA-AH-BPR ORDER CHEST XRAY- PA AND LATERAL
191. 35.35.10 Element: VA-AH-BPR ORDER FULL PULMONARY FUNCTION TESTS

> \+ + Next Screen - Prev Screen ?? More Actions

> \>\>\>

> ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print CO Copy Dialog DO Dialog Overview QU Quit

> DD Detailed Display DT Dialog Text

> DP Progress Note Text ED Edit/Delete Dialog

> Select Item: Next Screen// *Find* VA-AH-BPR ORDER FULL PULMONARY FUNCTION TESTS

######## and select the appropriate item number to open the element

> Current dialog element/group name: VA-AH-BPR ORDER FULL PULMONARY FUNCTION TESTS

> Used by: VA-AH-BPR ORDERS (Current Reminder Dialog)

> FINDING ITEM: AH-BPR ORDER PFT //

> Select ADDITIONAL FINDINGS: Q.*Enter exact name of local order dialog*

> REMINDER DIALOG NAME: VA-AH-BPR INITIAL EVALUATION NOTE

> <u>+Item Seq. Dialog Summary</u>

192. 35.35.15 Element: VA-AH-BPR ORDER HIGH RESOLUTION CT CHEST
193. 35.35.20 Element: VA-AH-BPR ORDER ECHOCARDIOGRAM
194. 35.35.25 Element: VA-AH-BPR ORDER ARTERIAL BLOOD GAS
195. 35.35.30 Element: VA-AH-BPR ORDER CBC W/DIFF
196. 35.35.35 Element: VA-AH-BPR ORDER ENT CONSULT
197. 35.35.40 Element: VA-AH-BPR ORDER PULMONARY CONSULT
198. 40 Element: VA-AH-BPR SPACE (DIALOG & NOTE)

> \+ + Next Screen - Prev Screen ?? More Actions

> \>\>\>

> ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print CO Copy Dialog DO Dialog Overview QU Quit

> DD Detailed Display DT Dialog Text

> DP Progress Note Text ED Edit/Delete Dialog

> Select Item: Next Screen// *Find* VA-AH-BPR ORDER HIGH RESOLUTION CT CHEST

######## and select the appropriate item number to open the element

> Current dialog element/group name: VA-AH-BPR ORDER HIGH RESOLUTION CT CHEST Used by: VA-AH-BPR ORDERS (Current Reminder Dialog)

> FINDING ITEM: HF AH-BPR ORDER CHEST CT//

> Select ADDITIONAL FINDINGS: Q.*Enter exact name of local order dialog*

> REMINDER DIALOG NAME: VA-AH-BPR INITIAL EVALUATION NOTE

> <u>+Item Seq. Dialog Summary</u>

192. 35.35.15 Element: VA-AH-BPR ORDER HIGH RESOLUTION CT CHEST
193. 35.35.20 Element: VA-AH-BPR ORDER ECHOCARDIOGRAM
194. 35.35.25 Element: VA-AH-BPR ORDER ARTERIAL BLOOD GAS
195. 35.35.30 Element: VA-AH-BPR ORDER CBC W/DIFF
196. 35.35.35 Element: VA-AH-BPR ORDER ENT CONSULT
197. 35.35.40 Element: VA-AH-BPR ORDER PULMONARY CONSULT
198. 40 Element: VA-AH-BPR SPACE (DIALOG & NOTE)

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 28%" />
<col style="width: 35%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>+</p>
</blockquote></th>
<th><blockquote>
<p>+ Next Screen</p>
</blockquote></th>
<th><blockquote>
<p>- Prev Screen ?? More</p>
</blockquote></th>
<th><blockquote>
<p>Actions</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>&gt;&gt;&gt;</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>Add Element/Group</p>
</blockquote></td>
<td><blockquote>
<p>DS Dialog Summary</p>
</blockquote></td>
<td><blockquote>
<p>INQ Inquiry/Print</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CO</p>
</blockquote></td>
<td><blockquote>
<p>Copy Dialog</p>
</blockquote></td>
<td><blockquote>
<p>DO Dialog Overview</p>
</blockquote></td>
<td><blockquote>
<p>QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DD</p>
</blockquote></td>
<td><blockquote>
<p>Detailed Display</p>
</blockquote></td>
<td><blockquote>
<p>DT Dialog Text</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DP</p>
</blockquote></td>
<td><blockquote>
<p>Progress Note Text</p>
</blockquote></td>
<td><blockquote>
<p>ED Edit/Delete Dialog</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Select Item: Next Screen// *Find* VA-AH-BPR ORDER ECHOCARDIOGRAM

######## and select the appropriate item number to open the element

> Current dialog element/group name: VA-AH-BPR ORDER ECHOCARDIOGRAM Used by: VA-AH-BPR ORDERS (Current Reminder Dialog)

> FINDING ITEM: HF AH-BPR ORDER ECHO //

> Select ADDITIONAL FINDINGS: Q.*Enter exact name of local order dialog*

> REMINDER DIALOG NAME: VA-AH-BPR INITIAL EVALUATION NOTE

> <u>+Item Seq. Dialog Summary</u>

192. 35.35.15 Element: VA-AH-BPR ORDER HIGH RESOLUTION CT CHEST
193. 35.35.20 Element: VA-AH-BPR ORDER ECHOCARDIOGRAM
194. 35.35.25 Element: VA-AH-BPR ORDER ARTERIAL BLOOD GAS
195. 35.35.30 Element: VA-AH-BPR ORDER CBC W/DIFF
196. 35.35.35 Element: VA-AH-BPR ORDER ENT CONSULT
197. 35.35.40 Element: VA-AH-BPR ORDER PULMONARY CONSULT
198. 40 Element: VA-AH-BPR SPACE (DIALOG & NOTE)

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 28%" />
<col style="width: 35%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>+</p>
</blockquote></th>
<th><blockquote>
<p>+ Next Screen</p>
</blockquote></th>
<th><blockquote>
<p>- Prev Screen ?? More</p>
</blockquote></th>
<th><blockquote>
<p>Actions</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>&gt;&gt;&gt;</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>Add Element/Group</p>
</blockquote></td>
<td><blockquote>
<p>DS Dialog Summary</p>
</blockquote></td>
<td><blockquote>
<p>INQ Inquiry/Print</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CO</p>
</blockquote></td>
<td><blockquote>
<p>Copy Dialog</p>
</blockquote></td>
<td><blockquote>
<p>DO Dialog Overview</p>
</blockquote></td>
<td><blockquote>
<p>QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DD</p>
</blockquote></td>
<td><blockquote>
<p>Detailed Display</p>
</blockquote></td>
<td><blockquote>
<p>DT Dialog Text</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DP</p>
</blockquote></td>
<td><blockquote>
<p>Progress Note Text</p>
</blockquote></td>
<td><blockquote>
<p>ED Edit/Delete Dialog</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Select Item: Next Screen// *Find* VA-AH-BPR ORDER ARTERIAL BLOOD GAS

######## and select the appropriate item number to open the element

> Current dialog element/group name: VA-AH-BPR ORDER ARTERIAL BLOOD GAS Used by: VA-AH-BPR ORDERS (Current Reminder Dialog)

> FINDING ITEM: HF AH-BPR ORDER ABG //

> Select ADDITIONAL FINDINGS: Q.*Enter exact name of local order dialog*

> REMINDER DIALOG NAME: VA-AH-BPR INITIAL EVALUATION NOTE

> <u>+Item Seq. Dialog Summary</u>

192. 35.35.15 Element: VA-AH-BPR ORDER HIGH RESOLUTION CT CHEST
193. 35.35.20 Element: VA-AH-BPR ORDER ECHOCARDIOGRAM
194. 35.35.25 Element: VA-AH-BPR ORDER ARTERIAL BLOOD GAS
195. 35.35.30 Element: VA-AH-BPR ORDER CBC W/DIFF
196. 35.35.35 Element: VA-AH-BPR ORDER ENT CONSULT
197. 35.35.40 Element: VA-AH-BPR ORDER PULMONARY CONSULT
198. 40 Element: VA-AH-BPR SPACE (DIALOG & NOTE)

> \+ + Next Screen - Prev Screen ?? More Actions

> \>\>\>

> ADD Add Element/Group DS Dialog Summary INQ Inquiry/Print CO Copy Dialog DO Dialog Overview QU Quit

> DD Detailed Display DT Dialog Text

> DP Progress Note Text ED Edit/Delete Dialog

> Select Item: Next Screen// *Find* VA-AH-BPR ORDER CBC W/DIFF

######## and select the appropriate item number to open the element

> Current dialog element/group name: VA-AH-BPR ORDER CBC W/DIFF Used by: VA-AH-BPR ORDERS (Current Reminder Dialog)

> FINDING ITEM: HF AH-BPR ORDER CBC //

> Select ADDITIONAL FINDINGS: Q.*Enter exact name of local order dialog*

> REMINDER DIALOG NAME: VA-AH-BPR INITIAL EVALUATION NOTE

> <u>+Item Seq. Dialog Summary</u>

192. 35.35.15 Element: VA-AH-BPR ORDER HIGH RESOLUTION CT CHEST
193. 35.35.20 Element: VA-AH-BPR ORDER ECHOCARDIOGRAM
194. 35.35.25 Element: VA-AH-BPR ORDER ARTERIAL BLOOD GAS
195. 35.35.30 Element: VA-AH-BPR ORDER CBC W/DIFF
196. 35.35.35 Element: VA-AH-BPR ORDER ENT CONSULT
197. 35.35.40 Element: VA-AH-BPR ORDER PULMONARY CONSULT
198. 40 Element: VA-AH-BPR SPACE (DIALOG & NOTE)

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 28%" />
<col style="width: 35%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>+</p>
</blockquote></th>
<th><blockquote>
<p>+ Next Screen</p>
</blockquote></th>
<th><blockquote>
<p>- Prev Screen ?? More</p>
</blockquote></th>
<th><blockquote>
<p>Actions</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>&gt;&gt;&gt;</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>Add Element/Group</p>
</blockquote></td>
<td><blockquote>
<p>DS Dialog Summary</p>
</blockquote></td>
<td><blockquote>
<p>INQ Inquiry/Print</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CO</p>
</blockquote></td>
<td><blockquote>
<p>Copy Dialog</p>
</blockquote></td>
<td><blockquote>
<p>DO Dialog Overview</p>
</blockquote></td>
<td><blockquote>
<p>QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DD</p>
</blockquote></td>
<td><blockquote>
<p>Detailed Display</p>
</blockquote></td>
<td><blockquote>
<p>DT Dialog Text</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DP</p>
</blockquote></td>
<td><blockquote>
<p>Progress Note Text</p>
</blockquote></td>
<td><blockquote>
<p>ED Edit/Delete Dialog</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Select Item: Next Screen// *Find* VA-AH-BPR ORDER ENT CONSULT

######## and select the appropriate item number to open the element

> Current dialog element/group name: VA-AH-BPR ORDER ENT CONSULT Used by: VA-AH-BPR ORDERS (Current Reminder Dialog)

> FINDING ITEM: HF AH-BPR ORDER ENT CONSULT //

> Select ADDITIONAL FINDINGS: Q.*Enter exact name of local order dialog*

> REMINDER DIALOG NAME: VA-AH-BPR INITIAL EVALUATION NOTE

> <u>+Item Seq. Dialog Summary</u>

192. 35.35.15 Element: VA-AH-BPR ORDER HIGH RESOLUTION CT CHEST
193. 35.35.20 Element: VA-AH-BPR ORDER ECHOCARDIOGRAM
194. 35.35.25 Element: VA-AH-BPR ORDER ARTERIAL BLOOD GAS
195. 35.35.30 Element: VA-AH-BPR ORDER CBC W/DIFF
196. 35.35.35 Element: VA-AH-BPR ORDER ENT CONSULT
197. 35.35.40 Element: VA-AH-BPR ORDER PULMONARY CONSULT
198. 40 Element: VA-AH-BPR SPACE (DIALOG & NOTE)

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 28%" />
<col style="width: 35%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>+</p>
</blockquote></th>
<th><blockquote>
<p>+ Next Screen</p>
</blockquote></th>
<th><blockquote>
<p>- Prev Screen ?? More</p>
</blockquote></th>
<th><blockquote>
<p>Actions</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>&gt;&gt;&gt;</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ADD</p>
</blockquote></td>
<td><blockquote>
<p>Add Element/Group</p>
</blockquote></td>
<td><blockquote>
<p>DS Dialog Summary</p>
</blockquote></td>
<td><blockquote>
<p>INQ Inquiry/Print</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CO</p>
</blockquote></td>
<td><blockquote>
<p>Copy Dialog</p>
</blockquote></td>
<td><blockquote>
<p>DO Dialog Overview</p>
</blockquote></td>
<td><blockquote>
<p>QU Quit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DD</p>
</blockquote></td>
<td><blockquote>
<p>Detailed Display</p>
</blockquote></td>
<td><blockquote>
<p>DT Dialog Text</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DP</p>
</blockquote></td>
<td><blockquote>
<p>Progress Note Text</p>
</blockquote></td>
<td><blockquote>
<p>ED Edit/Delete Dialog</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Select Item: Next Screen// *Find* VA-AH-BPR ORDER PULMONARY CONSULT

######## and select the appropriate item number to open the element

> Current dialog element/group name: VA-AH-BPR ORDER PULMONARY CONSULT Used by: VA-AH-BPR ORDERS (Current Reminder Dialog)

> FINDING ITEM: HF AH-BPR ORDER PULM CONSULT //

> Select ADDITIONAL FINDINGS: Q.*Enter exact name of local order dialog*

####### Enabling the dialog:

> Before linking the dialog to a note title you must first add into the TIU Template Reminder Dialog Parameter list.

#### Adding dialog to the TIU Reminder Dialog Parameter (starting from the Reminder Manager Menu)

> Select Reminder Managers Menu \<TEST ACCOUNT\> Option: CP CPRS Reminder Configuration

> CA Add/Edit Reminder Categories CL CPRS Lookup Categories

> CS CPRS Cover Sheet Reminder List MH Mental Health Dialogs Active

> PN Progress Note Headers

> RA Reminder GUI Resolution Active

> TIU TIU Template Reminder Dialog Parameter

> DL Default Outside Location

> PT Position Reminder Text at Cursor NP New Reminder Parameters

> GEC GEC Status Check Active WH WH Print Now Active

> Select CPRS Reminder Configuration \<TEST ACCOUNT\> Option: *TIU*

> Reminder Dialogs allows as Templates may be set for the following: 1 User USR \[choose from NEW PERSON\]

> 3 Service SRV \[choose from SERVICE/SECTION\] 4 Division DIV \[NAME OF YOUR DIVISION\]

> 5 System SYS \[YOURSERVER.YOURSITE.MED.VA.GOV\]

> Enter selection: *5* System \[YOURSERVER.YOURSITE.MED.VA.GOV\] Select Display Sequence: ? * enter ? to determine last number in sequence*

#### Display Sequence Value

> ---------------- -----

1.  TOBACCO CESSATION NOTE
2.  PATIENT EDUCATION ASSESSMENT
3.  TEST CLINIC DIALOG

> ….

> 412 NON VA CARE COORDINATION NOTE (D) * last sequence number on my list yours will be different (con’t next page)*

> Select Display Sequence: *Select appropriate Display Sequence number*

#### Are you adding 413 as a new Display Sequence? Yes// YES Display Sequence: 413// 413

> Clinical Reminder Dialog*:* VA-AH-BPR INITIAL EVALUATION NOTE reminder dialog NATIONAL

#### ...OK? Yes// Yes

####### Remove “disabled” from Reminder Dialog

> Open reminder dialog manager, change view to ‘DIALOG’ locate VA-AH-BPR INITIAL EVALUATION NOTE dialog on the list.

1.  Edit the VA-AH-BPR INITIAL EVALUATION NOTE entry and remove the DISABLE field.
2.  Remember VA-AH-BPR INITIAL EVALUATION NOTE will not have an associated source reminder.

> Select Item: Next Screen// ED Edit/Delete Dialog

> NAME: VA-AH-BPR INITIAL EVALUATION NOTE (Disabled) Replace DISABLE: DISABLED IN EXCHANGE Replace @

> SURE YOU WANT TO DELETE? YES CLASS: NATIONAL//

> SPONSOR: Office of Public Health-Post-Deployment Health

> // REVIEW DATE: //

> SOURCE REMINDER://

#### =====================================================================

> While using the TIU editors if at any time the settings do not look correct NEVER click the apply button, but instead click CANCEL, then start over

> =====================================================================

####### Create note title, AIRBORNE HAZARD/BURN PIT REGISTRY INITIAL EVALUATION NOTE

> From the Document Definitions (Manager) Menu: Create document definitions Type Next Level at prompt

> Enter corresponding number for Progress Notes at prompt Hit enter until you find Medicine

> Type Next Level and enter corresponding number for Medicine at prompt Type Title at prompt

> Type AIRBORNE HAZARD/BURN PIT REGISTRY INITIAL EVALUATION NOTE at

> prompt

> Map title to PERSIAN GULF REGISTRY E & M NOTE

#### Enter A at status prompt

1.  TIU Parameters Menu ...
2.  Document Definitions (Manager) ...
3.  User Class Management ...
4.  TIU Template Mgmt Functions ...
5.  TIU Alert Tools

> 7 TIUHL7 Message Manager Title Mapping Utilities ...

> 6 Active Title Cleanup Report

> Select TIU Maintenance Menu \<TEST ACCOUNT\> Option: 2 Document Definitions (Manager)

> --- Manager Document Definition Menu ---

1.  Edit Document Definitions
2.  Sort Document Definitions
3.  Create Document Definitions
4.  Create Objects
5.  Create TIU/Health Summary Objects

> Select Document Definitions (Manager) \<TEST ACCOUNT\> Option: 3 Create Document Definitions.............

> Name Type

######### CLINICAL DOCUMENTS CL

1.  PROGRESS NOTES CL
2.  ADDENDUM DC
3.  DISCHARGE SUMMARY CL
4.  CLINICAL PROCEDURES CL
5.  LR LABORATORY REPORTS CL
6.  SURGICAL REPORTS CL

> Class/DocumentClass Next Level Detailed Display/Edit

> (Title) Restart Status...

> (Component) Boilerplate Text Delete

> Select CLINICAL DOCUMENTS Item (Line 2-7): 2

> Name Type

2.  PROGRESS NOTES CL
3.  MEDICINE DC
4.  MEDICAL OBSERVATION NOTE TL
5.  CANCER CARE TL
6.  CARDIAC CATH LAB PROCEDURE REPORT (T) TL
7.  CARDIAC ELECTROPHYSIOLOGY PROCEDURE REPORT (T) TL
8.  CARDIOLOGY ACS TEAM FOLLOW-UP NOTE TL
9.  CARDIOLOGY AICD IMPLANTATION REPORT TL

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 17%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">+ <strong>?Help &gt;ScrollRight PS/PL PrintScrn/Lis</strong></th>
<th><blockquote>
<p><strong>t +/-</strong></p>
</blockquote></th>
<th><strong>&gt;&gt;&gt;</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>(Class/DocumentClass) Title</p>
</blockquote></td>
<td><blockquote>
<p>Next Level Restart</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>Detailed Status...</p>
</blockquote></td>
<td><blockquote>
<p>Display/Edit</p>
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
<td></td>
</tr>
</tbody>
</table>

> Select Action: Next Screen// title Title

> Enter the Name of a new MEDICINE: AIRBORNE HAZARD/BURN PIT REGISTRY INITIAL EVALUATION NOTE

> CLASS OWNER: CLINICAL COORDINATOR// CLINICAL COORDINATOR

> EVERY Local Title must be mapped to a VHA Enterprise Standard Title.

> Direct Mapping to Enterprise Standard Title...

> Your LOCAL Title is: AIRBORNE HAZARD/BURN PIT REGISTRY INITIAL EVALUATION NOTE

> NOTE: Only ACTIVE Titles may be selected...

> Select VHA ENTERPRISE STANDARD TITLE: PERSIAN GULF REGISTRY E & M NOTE

> I found a match of: PERSIAN GULF REGISTRY E & M NOTE

> ... OK? Yes// YES

> Ready to map LOCAL Title: AIRBORNE HAZARD/BURN PIT REGISTRY INITIAL EVALUATION

> NOTE to

> VHA Enterprise Standard Title: PERSIAN GULF REGISTRY E & M NOTE.

> ... OK? Yes//YES

> STATUS: (A/I/T): INACTIVE// A ACTIVE Entry Activated.

1.  Linking Progress Note Title to Dialog

> From Template Editor Edit Shared Template Click + Document Titles

> ![](pxrm-2-39-airborne-hazard-open-burn-pit-evaluation-installation-guide/002.png)

> Click New Template button

![](pxrm-2-39-airborne-hazard-open-burn-pit-evaluation-installation-guide/003.png)

> Type AIRBORNE HAZARD/BURN PIT REGISTRY INITIAL EVALUATION NOTE in Name

#### box

> Click down arrow and Click on Reminder Dialog in Template Type Box

![](pxrm-2-39-airborne-hazard-open-burn-pit-evaluation-installation-guide/004.png)

> Type VA-AH-BPR INITIAL EVALUATION NOTE in Reminder Dialog box

> ![](pxrm-2-39-airborne-hazard-open-burn-pit-evaluation-installation-guide/005.png)

> Type AIRBORNE HAZAED/BURN PIT REGISTRY INITIAL EVALUATION NOTE in

> Associated Title Box

> ![](pxrm-2-39-airborne-hazard-open-burn-pit-evaluation-installation-guide/006.png)

> Click Apply in lower right corner

> ![](pxrm-2-39-airborne-hazard-open-burn-pit-evaluation-installation-guide/007.png)

> Confirm title is active in CPRS and dialog is attached

> ![](pxrm-2-39-airborne-hazard-open-burn-pit-evaluation-installation-guide/008.png)

> <span id="_bookmark5" class="anchor"></span><u>Appendix A: Installation Example</u>

> XPD Main Menu

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution Enter a Host File: \<your directory\>PXRM_2_0_39.KID

> KIDS Distribution saved on Sep 11, 2014@09:18:02 Comment: Airborne hazard

> This Distribution contains Transport Globals for the following Package(s): Build PXRM\*2.0\*39 has been loaded before, here is when:

> PXRM\*2.0\*39 Install Completed

> was loaded on Sep 11, 2014@10:42:09 OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> PXRM\*2.0\*39

> Use INSTALL NAME: PXRM\*2.0\*39 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: INstall Package(s) Select INSTALL NAME: PXRM\*2.0\*39 10/9/14@12:21:25

> =\> Airborne hazard ;Created on Sep 11, 2014@09:18:02

> This Distribution was loaded on Oct 09, 2014@12:21:25 with header of Airborne hazard ;Created on Sep 11, 2014@09:18:02

> It consisted of the following Install(s):

> PXRM\*2.0\*39

> Checking Install for Package PXRM\*2.0\*39 Install Questions for PXRM\*2.0\*39 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

> Install Started for PXRM\*2.0\*39 :

> Oct 09, 2014@12:21:36

> Build Distribution Date: Sep 11, 2014 Installing Routines:

> Oct 09, 2014@12:21:36

> Running Pre-Install Routine: PRE^PXRMP39I DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> Oct 09, 2014@12:21:36

> Installing Data:

> Oct 09, 2014@12:21:38

> Running Post-Install Routine: POST^PXRMP39I ENABLE options.

> ENABLE protocols.

> There are 2 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry VA-AH/BPR PXRM\*2\*39
2.  Installing Reminder Exchange entry VA-PATCH 39 POST COMPONENTS Updating Routine file...

> Updating KIDS files...

> PXRM\*2.0\*39 Installed.

> Oct 09, 2014@12:22:13

> Not a production UCI

> PXRM\*2.0\*39 I

> Install Completed

> <span id="_TOC_250001" class="anchor"></span><u>Appendix B: Health Factor List</u>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>CATEGORY: AH-BPR CHIEF COMPLAINT</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC CANCER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC CHEST PAIN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC CHILDREN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC CHRONIC SINUS INFECTION</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC CONCERNED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC COUGH &gt; 3 WKS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC DEC EXERCISE ABILITY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC EYE PROBLEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC GI PROBLEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC HAY FEVER/RESP ALLERGY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC HEART PROBLEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC IMMUNE PROBLEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC NEURO PROBLEM</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC OTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC RUNNY NOSE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC SKIN PROBLEM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC SOB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC SORE THROAT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CC SPUTUM &gt;3 WKS</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CC WHEEZING/WHISTLING</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><u>CATEGORY: AH-BPR EXPOSURE CONCERNS</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CONCERN HOBBIES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CONCERN MILITARY JOB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CONCERN OFF BASE AIR</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CONCERN ON BASE AIR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CONCERN OTHER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR CONCERN SMOKING</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR CONCERN UNKNOWN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><u>CATEGORY: AH-BPR ASTHMA</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ASTHMA NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ASTHMA UNSURE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ASTHMA YES</p>
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
<p><u>CATEGORY: AH-BPR SMOKING DEPLOYMENT</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AH-BPR SMOKING DEPLOYMENT NO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR SMOKING DEPLOYMENT UNKNOWN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR SMOKING DEPLOYMENT YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><u>CATEGORY: TOBACCO</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CURRENT SMOKER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PREVIOUS SMOKER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>LIFETIME NON-SMOKER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><u>CATEGORY: AH-BPR BIRTH DEFECTS</u></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR BIRTH DEFECTS N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR BIRTH DEFECTS NO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR BIRTH DEFECTS UNCLEAR</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR BIRTH DEFECTS YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><u>CATEGORY: AH-BPR ABNORMALITIES</u></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN CARDIO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ABN COGNITIVE/MEMORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN DERM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ABN ENT</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN FATIGUE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ABN FEVER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN GI</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ABN GU</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN HEME/ONC</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ABN LYMPHADENOPATHY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN MUSCULOSKELETAL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ABN NEURO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN NONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ABN OTHER</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN PSYCH</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ABN RESPIRATORY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN TEMP SENS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ABN WEIGHT GAIN</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ABN WEIGHT LOSS</p>
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
<p><u>CATEGORY: AH-BPR ORDERS</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ORDER CHEST XRAY</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ORDER ABG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ORDER CBC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ORDER CHEST CT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ORDER ECHO</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>AH-BPR ORDER ENT CONSULT AH-BPR ORDER PULM CONSULT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>AH-BPR ORDER PFT</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_TOC_250000" class="anchor"></span><u>Acronyms</u>

> The OIT Master Glossary is available at [<u>http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm</u>](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
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
<p>AH-BPR</p>
</blockquote></td>
<td><blockquote>
<p>Airborne Hazard-Open Burn Pit</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ASU</p>
</blockquote></td>
<td><blockquote>
<p>Authorization/Subscription Utility</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Clin4</p>
</blockquote></td>
<td><blockquote>
<p>National Customer Support team that supports Clinical Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CPRS</p>
</blockquote></td>
<td><blockquote>
<p>Computerized Patient Record System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DBA</p>
</blockquote></td>
<td><blockquote>
<p>Database Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DG</p>
</blockquote></td>
<td><blockquote>
<p>Registration and Enrollment Package namespace</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ESM</p>
</blockquote></td>
<td><blockquote>
<p>Enterprise Systems Management (ESM)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>FIM</p>
</blockquote></td>
<td><blockquote>
<p>Functional Independence Measure</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td><blockquote>
<p>Health Summary namespace (also HSUM)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>GUI</p>
</blockquote></td>
<td><blockquote>
<p>Graphic User Interface</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HRMH/HRMHP</p>
</blockquote></td>
<td><blockquote>
<p>High Risk Mental Health Patient</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IAB</p>
</blockquote></td>
<td><blockquote>
<p>Initial Assessment &amp; Briefing</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ICD-10</p>
</blockquote></td>
<td><blockquote>
<p>International Classification of Diseases, 10th Edition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ICR</p>
</blockquote></td>
<td><blockquote>
<p>Internal Control Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>IOC</p>
</blockquote></td>
<td><blockquote>
<p>Initial Operating Capabilities</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>LSSD</p>
</blockquote></td>
<td><blockquote>
<p>Last Service Separation Date</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>MH</p>
</blockquote></td>
<td><blockquote>
<p>Mental Health</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>MHTC</p>
</blockquote></td>
<td><blockquote>
<p>Mental Health Treatment Coordinator</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OHI</p>
</blockquote></td>
<td><blockquote>
<p>Office of Health Information</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OI</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OIF/OEF</p>
</blockquote></td>
<td><blockquote>
<p>Operation Iraqi Freedom/Operation Enduring Freedom</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>OIT/OI&amp;T</p>
</blockquote></td>
<td><blockquote>
<p>Office of Information Technology</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>OMHS</p>
</blockquote></td>
<td><blockquote>
<p>Office of Mental Health Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>ORR</p>
</blockquote></td>
<td><blockquote>
<p>Operational Readiness Review</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PCS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Care Services</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PD</p>
</blockquote></td>
<td><blockquote>
<p>Product Development</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PIMS</p>
</blockquote></td>
<td><blockquote>
<p>Patient Information Management System</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
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
<p>PMAS</p>
</blockquote></td>
<td><blockquote>
<p>Program Management Accountability System</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PTM</p>
</blockquote></td>
<td><blockquote>
<p>Patch Tracker Message</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PXRM</p>
</blockquote></td>
<td><blockquote>
<p>Clinical Reminder Package namespace</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RSD</p>
</blockquote></td>
<td><blockquote>
<p>Requirements Specification Document</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>SD</p>
</blockquote></td>
<td><blockquote>
<p>Scheduling Package Namespace</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>SQA</p>
</blockquote></td>
<td><blockquote>
<p>Software Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>USR</p>
</blockquote></td>
<td><blockquote>
<p>ASU package namespace</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VA</p>
</blockquote></td>
<td><blockquote>
<p>Department of Veteran Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VHA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Administration</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VISN</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Integrated Service Network</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistA</p>
</blockquote></td>
<td><blockquote>
<p>Veterans Health Information System and Technology Architecture</p>
</blockquote></td>
</tr>
</tbody>
</table>