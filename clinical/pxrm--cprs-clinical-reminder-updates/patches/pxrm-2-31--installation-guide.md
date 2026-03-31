---
title: PXRM*2*31 Palliative Care National Clinical Template Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Palliative Care National Clinical Template
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*31
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - style
  - width
  - contents
  - transport
  - global
  - blockquote
  - installation
  - palliative
  - care
page_count: 0
word_count: 1199
section_count: 3
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: March 2014
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_31_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_31_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-31-palliative-care-national-clinical-template-installation-guide/001.png)

## Palliative Care National Clinical Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PXRM\*2.0\*31

> INSTALLATION and SETUP GUIDE

> March 2014

> Product Development Department of Veterans Affairs

## <u>Contents</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  [Retrieve the host file containing the patch 5](#retrieve-the-host-file-containing-the-patch)
2.  [Install the build first in a training or test account 6](#install-the-build-first-in-a-training-or-test-account.)
3.  [Load the distribution. 6](#load-the-distribution.)
    1.  [Backup a Transport Global 6](#backup-a-transport-global)
    2.  [Compare Transport Global to Current System 6](#compare-transport-global-to-current-system)
    3.  [Verify Checksums in Transport Global 6](#verify-checksums-in-transport-global)
4.  [Install the build. 6](#install-the-build.)
5.  [Install File Print 7](#install-file-print)
6.  [Build File Print 7](#build-file-print)

[POST-INSTALLATION SETUP 7](#post-installation-setup)

[APPENDIX A](#_bookmark16) INSTALLATION EXAMPLE 10

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Palliative Care National Clinical Template](#palliative-care-national-clinical-template)
  - [<u>Contents</u>](#ucontentsu)
- [Introduction](#introduction)
- [Pre-Installation](#pre-installation)
    - [Required Software for patch PXRM\2.0\31](#required-software-for-patch-pxrm2031)
    - [Related Documentation](#related-documentation)
- [Installation](#installation)
- [Post-Installation Setup](#post-installation-setup)
> Patch PXRM\*2.0\*31 is one of the first patches that uses the recently approved expedited patch process. This patch releases the Palliative Care National Clinical Template without any changes to routines, data dictionaries, or other package functions – “content” only. The reminder dialog is VA-PALLIATIVE CARE NATIONAL CLINICAL TEMPLATE.
> There are two Reminder Exchange entries that will be installed as part of this patch.
1.  VA-PALLIATIVE CARE CONSULT
2.  VA-PATCH 31 POST HS COMPONENTS

#### Palliative Care National Clinical Template (PC-NCT)

> The VA Hospice and Palliative Care (HPC) program office has sponsored the development of this reminder dialog template to document provider-based palliative care consultations at all sites within VHA. This template is critical to improving the process and documentation of clinical care, and facilitating high quality palliative care and programmatic quality improvement. It is the intent of the HPC program office that this national template be formally distributed to VA palliative care programs for voluntary use throughout VHA in early 2014.
> The current version of the template, PC-NCT 3.0, for national distribution, was developed by the Quality Improvement Resource Center (QuIRC), based in Los Angeles, CA. QuIRC serves as one of three national Quality Centers that support the HPC’s Comprehensive End-of-Life Care Initiative to foster quality improvement. QuIRC built the template based on a comprehensive review of the literature and in consultation with a wide variety of program stakeholders and clinical experts. There has been extensive involvement from the field in order to obtain concurrence and refine earlier versions. Our program office goal is to have at least 60% of the VA facilities adopt the PC-NCT over the next two years.
> Using an earlier version of PC-NCT in 2010, QuIRC gauged interest from facilities about participating in a User Community in order to pilot the template in a clinical setting; garnered feedback regarding the content, ease of use, and utility of the tool; and assessed attitudes surrounding the tool’s adoption and implementation. After identifying facilities interested in piloting the tool, QuIRC selected five sites (Baltimore, Battle Creek, Indianapolis, Birmingham, and Salt Lake) to make up the User Community based on geographic diversity, palliative care program size and complexity, academic and non-academic status, and the local availability of evaluation resources. The PC-NCT was disseminated to the User Community sites in August 2010. User Community conference calls have been held at least once per month in which we gather valuable feedback to make ongoing modifications which are reflected in the PC-NCT version *3.0.* This most recent version captures aspects of care that are *most* important to assess during a palliative care consultation in a manner that is efficient and helpful to clinicians.
> In order for the HPC performance measure to be met for a given palliative care consult, four elements must be present – primary diagnosis, CPT code (ending in 3, 4 or 5), qualified provider (MD/DO, CNS, NP, PA) and correct DSS code (351 or 353). For this to occur for an inpatient, the CPRS location of the patient MUST be changed to an outpatient clinic location setup for this purpose PRIOR to beginning the note. The reminder dialog itself has a “change location?” prompt built in.
> Per VHA Directive 2009-002 Patient Care Data Capture: “It is VHA policy to capture and report inpatient appointments in outpatient clinics, inpatient billable professional services, inpatient professional mental health services, and outpatient care data to support the continuity of patient care, resource allocation, performance measurement, quality management, provider productivity, research, and third-party payer collections.” Hence, the following is highlighted:
- The correct coding can only roll up to the VSSC data base if <u>linked to an encounter</u>. Encounter data is not generated for inpatient locations.
- New clinic locations for inpatient palliative care/hospice consultations must be created for each site. These locations should be set up as “count” clinics *without* any appointment grid. One clinic should be associated with DSS identifier 351 and one with DSS identifier 353. The clinic names should be followed by “-X” in order to ensure that these locations are not included in VHA wait time and missed opportunity measures. Examples of inpatient clinic locations might be: “SITENAME-INPT PALL CONSULT- X” OR “SITENAME-INPT HOSPICE-X.”
- For patients seen on an outpatient basis, providers simply select an appropriate outpatient palliative care or hospice location and complete an encounter form as they normally do. The outpatient palliative care clinic location(s) should be associated with Hospice (DSS
> 351\) or Palliative Care (DSS 353) (note: DSS identifiers for clinics are not displayed in CPRS). For inpatients, the note author has to take four steps in sequence prior to documenting the consultation:
- Before starting a note, click on patient location (next to patient name);
- Click on the “new visit” tab
- Select the appropriate “inpatient” palliative care clinic location
- Start a consultation note using the appropriate title for their site
> This template is created in a modular format, separating the nine content areas. When using the template, clinicians can choose which modules they would like to complete. They can use the entire template to create a comprehensive palliative care consultation. Or they can choose one module at a time, such as the symptom module, to address a focused area of concern.

# Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Required Software for patch PXRM\*2.0\*31

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Package/Patch  | Namespace | Version | Comments  |
|--------------------|---------------|-------------|---------------|
| Clinical Reminders | PXRM          | 2.0         | Fully patched |
| Health Summary     | GMTS          | 2.7         | Fully patched |
| HL7                | HL            | 1.6         | Fully patched |
| Kernel             | XU            | 8.0         | Fully patched |
| MailMan            | XM            | 8.0         | Fully patched |
| Mental Health      | YS            | 5.01        | Fully patched |
| VA FileMan         | DI            | 22          | Fully patched |

### Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Documentation            | Documentation File name |
|------------------------------|-----------------------------|
| Installation and Setup Guide | PXRM_2_31_IG.PDF            |
|                              |                             |

#### Web Sites

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 36%" />
<col style="width: 39%" />
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
<td><p>Contains manuals, PowerPoint presentations, and other information</p>
<p>about Clinical Reminders</p></td>
</tr>
<tr class="even">
<td>National Clinical Reminders Committee</td>
<td><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncrc</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>public/default.aspx</u></a></td>
<td><p>This committee directs the development of new and revised</p>
<p>national reminders</p></td>
</tr>
<tr class="odd">
<td><p>VistA Document</p>
<p>Library</p></td>
<td><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></td>
<td><p>Contains manuals for Clinical</p>
<p>Reminders and</p></td>
</tr>
</tbody>
</table>

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual describes how to install PXRM\*2.0\*31.

> This build can be installed with users on the system, but it should be done during non-peak hours.

> *The installation needs to be done by a person with DUZ(0) set to "@."*

#### Retrieve the host file containing the patch

> Use ftp to access the build (the name of the host file is PXRM_2_0_31 .KID) from one of the following locations (with the ASCII file type):

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 33%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Hines</p>
</blockquote></th>
<th><mark><u>REDACTED</u></mark></th>
<th><mark><u>REDACTED</u></mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark><u>REDACTED</u></mark></td>
<td><mark><u>REDACTED</u></mark></td>
</tr>
</tbody>
</table>

#### Install the build first in a training or test account.

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

#### Load the distribution.

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and PXRM_2_0_31.KID at the Host File prompt.

#### Example

> From the Installation menu, you may elect to use the following options:

#### Backup a Transport Global

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

#### Compare Transport Global to Current System

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

#### Verify Checksums in Transport Global

> This option is not needed since there are NO routines being installed

#### Install the build.

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM .KID and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

#### Installation Example

> See [<u>Appendix A</u>](#_bookmark16).

#### Install File Print

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

#### Build File Print

> Use the KIDS Build File Print option to print out the build components.

# Post-Installation Setup 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Once the installation is complete -- To enable the dialog: Go to Reminder Dialog Management Option: Reminder Dialogs. Change the view to DIALOG, and find the NATIONAL PALLIATIVE CARE CONSULT on the list. Edit the entry and remove the text in the DISABLE field by entering @.
2.  To use the reminder dialog as a template, use the menu option XPAR EDIT PARAMETER.

> Choose to edit the parameter: TIU TEMPLATE REMINDER DIALOGS Add this reminder dialog to the list at the System level.

3.  In CPRS, open the Edit Shared Templates option and create a new template with the type of reminder dialog. From the Reminder Dialog drop down list, find NATIONAL PALLIATIVE CARE CONSULT and attach it to the template. You can attach the reminder dialog to your facility selected progress note title, if desired.
4.  ![](pxrm-2-31-palliative-care-national-clinical-template-installation-guide/002.png)You may want to include the entire dialog, as well as each individual module in Shared Templates. This will allow the user to select only one (or more modules) if they want to use only certain modules of the template. (This also allows them to complete a module or two, leave the note unsigned, and then come back later to complete other modules.) If you decide to put the individual modules in Shared Templates, you must complete step 3 above for each module, and place them in a folder for easy access. See example below:

#### TIU Health Summary Objects:

> Three TIU objects are included in the National Palliative Care Consult template:

1.  PALLI PHQ2 PH9 \[location = Element: VA-PALLI CONS PHQ2/9 OBJECT (E)\]
2.  PALLI WEIGHT \[location = Element: VA-PALLI CONS VITALS (E)\]
3.  PALLI VITALS \[location = Element: VA-PALLI CONS VITALS (E)\]

> The Health Summary Type for each TIU object is listed below

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th>Max</th>
<th></th>
<th>Hos ICD</th>
<th>Pro</th>
<th>CPT</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td><blockquote>
<p>Component Name</p>
</blockquote></td>
<td>Occ</td>
<td><blockquote>
<p>Time</p>
</blockquote></td>
<td>Loc Text</td>
<td>Nar</td>
<td>Mod</td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 25%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 14%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th>Max</th>
<th></th>
<th>Hos ICD</th>
<th>Pro</th>
<th>CPT</th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Abb Ord</td>
<td><blockquote>
<p>Component Name</p>
</blockquote></td>
<td>Occ</td>
<td><blockquote>
<p>Time</p>
</blockquote></td>
<td>Loc Text</td>
<td>Nar</td>
<td>Mod</td>
<td><blockquote>
<p>Selection</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark16" class="anchor"></span>Appendix A

> SMA5A3:SCT\>D ^XUP

> Setting up programmer environment This is a TEST account.

> Terminal Type set to: C-VT320/132

> .

> Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Patch Monitor Main Menu ...

> Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INSTalla tion

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution Enter a Host File: \<your directory name\>PXRM_2_0_31.KID

> KIDS Distribution saved on Jul 01, 2013@11:29:46 Comment: Palliative Care

> This Distribution contains Transport Globals for the following Package(s): Build PXRM\*2.0\*31 has been loaded before, here is when:

> PXRM\*2.0\*31 Install Completed

> was loaded on Jul 01, 2013@12:17:07 OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> PXRM\*2.0\*31

> Use INSTALL NAME: PXRM\*2.0\*31 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation \<TEST ACCOUNT\> Option: INSTAll Package(s) Select INSTALL NAME: PXRM\*2.0\*31 7/2/13@12:56

> =\> Palliative Care ;Created on Jul 01, 2013@11:29:46

> This Distribution was loaded on Jul 02, 2013@12:56 with header of Palliative Care ;Created on Jul 01, 2013@11:29:46

> It consisted of the following Install(s): PXRM\*2.0\*31

> Checking Install for Package PXRM\*2.0\*31 Install Questions for PXRM\*2.0\*31 Incoming Files:

> 811.8 REMINDER EXCHANGE (including data)

> Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

> Install Started for PXRM\*2.0\*31 : Jul 02, 2013@12:56:15

> Build Distribution Date: Jul 01, 2013 Installing Routines:

> Jul 02, 2013@12:56:15

> Running Pre-Install Routine: PRE^PXRMP31I DISABLE options.

> DISABLE protocols.

> Installing Data Dictionaries:

> Jul 02, 2013@12:56:16

> Installing Data:

> Jul 02, 2013@12:56:17

> Running Post-Install Routine: POST^PXRMP31I ENABLE options.

> ENABLE protocols.

> There are 2 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry VA-PALLIATIVE CARE CONSULT
2.  Installing Reminder Exchange entry VA-PATCH 31 POST HS COMPONENTS Updating Routine file...

> Updating KIDS files...

> PXRM\*2.0\*31 Installed.

> Mar 03, 2014@14:19:29

> Not a production UCI

> PXRM\*2.0\*31

> Install Completed