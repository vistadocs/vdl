---
title: PXRM*2*12 Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Install Guide
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*12
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 1
description: > The Clinical Reminders patch PXRM\2\12 and bundled patches (GMTS\2.7\89, OR\3\295, TIU\1\249) contain modifications to improve reminder exchange tools, reminder due reports, and National Drug Class standardization. They also include changes to support pharmacy encapsulation so that the reminder pa
audience: 
keywords: 
  - blockquote
  - table
  - class
  - strong
  - contents
  - style
  - width
  - reminder
  - transport
  - global
page_count: 0
word_count: 2474
section_count: 3
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: October 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_12_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_12_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-12-install-guide/001.png)

> PXRM\*2\*12 GMTS\*2.7\*89 OR\*3\*295 TIU\*1\*249

# INSTALLATION GUIDE


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [INSTALLATION GUIDE](#installation-guide)
  - [Introduction](#introduction)
    - [Clinical Reminders PXRM\2\12 Documentation](#clinical-reminders-pxrm212-documentation)
    - [Web Sites](#web-sites)
  - [Pre-Installation](#pre-installation)
    - [Embedded Fragment Surveillance Center (TEFSC)](#embedded-fragment-surveillance-center-tefsc)
    - [Retrieve host file containing the multi-package build](#retrieve-host-file-containing-the-multi-package-build)
    - [Install the build first in a training or test account.](#install-the-build-first-in-a-training-or-test-account)
    - [Load the distribution.](#load-the-distribution)
    - [Backup a Transport Global](#backup-a-transport-global)
    - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
    - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
    - [Print Transport Global (optional)](#print-transport-global-optional)
    - [Install the build.](#install-the-build)
    - [Install File Print](#install-file-print)
    - [Build File Print](#build-file-print)
    - [Post-installation routine](#post-installation-routine)
    - [Deletion of init routines](#deletion-of-init-routines)
> October 2009
> Office of Enterprise Development Department of Veterans Affairs
> <u>Contents</u>
1.  [Retrieve host file containing the multi-package build 5](#retrieve-host-file-containing-the-multi-package-build)
2.  [Install the build first in a training or test account 5](#install-the-build-first-in-a-training-or-test-account.)
3.  [Load the distribution. 5](#load-the-distribution.)
    1.  [Backup a Transport Global 5](#backup-a-transport-global)
    2.  [Compare Transport Global to Current System 5](#compare-transport-global-to-current-system)
    3.  [Verify Checksums in Transport Global 5](#verify-checksums-in-transport-global)
    4.  [Print Transport Global (optional) 6](#print-transport-global-optional)
4.  [Install the build. 6](#install-the-build.)
5.  [Install File Print 6](#install-file-print)
6.  [Build File Print 6](#build-file-print)
7.  [Post-installation routine 7](#post-installation-routine)
8.  [Deletion of init routines 7](#deletion-of-init-routines)
[APPENDIX A: INSTALLATION EXAMPLE 8](#Appendix_A:_Installation_Example)
> ii Clinical Reminders Install Guide 11/10/2009

## Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Clinical Reminders patch PXRM\*2\*12 and bundled patches (GMTS\*2.7\*89, OR\*3\*295, TIU\*1\*249) contain modifications to improve reminder exchange tools, reminder due reports, and National Drug Class standardization. They also include changes to support pharmacy encapsulation so that the reminder package will no longer have direct access to Pharmacy data. Initial changes to support standardization of reminder findings are incorporated.

> The PXRM\*2.0\*12 build is bundled with the following builds:

> ![](pxrm-2-12-install-guide/002.png) GMTS\*2.7\*89 - Supports new Reminder Exchange functionality and updates to Reminders components formatting.

> ![](pxrm-2-12-install-guide/003.png) OR\*3.0\*295 - Contains OR bug fixes related to reminder dialogs and changes to an API used by reminders.

> ![](pxrm-2-12-install-guide/004.png) TIU\*1.0\*249 – Supports new Reminder Exchange functionality and improves the TIU ListManager Health Summary Object display.

> Some of the items included in these patches:

> ![](pxrm-2-12-install-guide/005.png)![](pxrm-2-12-install-guide/006.png) The ability to use reminder exchange to send individual components (reminder dialogs, terms, taxonomies) without having to send a reminder,

> The ability to share TIU Health summary objects,

> The option to show a % in a reminder report as a separate column and to separate stop codes in a combined report,

> ![](pxrm-2-12-install-guide/007.png)![](pxrm-2-12-install-guide/008.png) New Computed Findings for body surface area, the date a patient will be a certain age, and for VA employees,

> Updates to the VA-TBI SCREEN, VA-IRAQ/AFGHAN SCREENING, VA-OEF/OIF

> ![](pxrm-2-12-install-guide/009.png)MONITOR reminders to remove combat eligibility as a criteria and move towards using the OEF/OIF fields in the patient file,

> An OEF/OIF extract for the FY10 performance monitor,

> Updates and fixes to other reminders including some of the MHV reminders,

> A new reminder for evaluation of positive screens for embedded fragments) VA-EMBEDDED FRAGMENTS RISK EVALUATION).

> See the Release Notes for more details.

### Clinical Reminders PXRM\*2\*12 Documentation

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
<p>Installation Guide</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_12_IG.PDF</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Manager’s Manual</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_12_MM.PDF</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Release Notes</p>
</blockquote></td>
<td><blockquote>
<p>PXRM_2_12_RN.PDF</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<p>Contains manuals, PowerPoint</p>
<p>presentations, and other information about Clinical Reminders</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>National Clinical Reminders Committee</p>
</blockquote></td>
<td><blockquote>
<p><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/n</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>crcpublic/default.aspx</u></a></p>
</blockquote></td>
<td><blockquote>
<p>This new committee will direct the development of new and revised national reminders</p>
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
<p>Contains manuals for Clinical Reminders</p>
<p>and</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Pre-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual describes how to install the bundled patches, PXRM\*2\*12, GMTS\*2.7\*89, OR\*3\*295, and TIU\*1\*249.

> <span id="Required_Software_for_PXRM*2*12" class="anchor"></span>Required Software for PXRM\*2\*12

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
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
<p>GEN. MED. REC. – VITALS</p>
<p>GMRV*5*25</p>
</blockquote></td>
<td><blockquote>
<p>GMRV</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
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
<p>NATIONAL DRUG FILE</p>
<p>PSN*4.0*176</p>
</blockquote></td>
<td><blockquote>
<p>PSN</p>
</blockquote></td>
<td><blockquote>
<p>4.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Pharmacy Data Management</p>
<p>PSS*1.0*133</p>
</blockquote></td>
<td><blockquote>
<p>PSS</p>
</blockquote></td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Outpatient Pharmacy</p>
<p>PSO*7.0*299</p>
</blockquote></td>
<td><blockquote>
<p>PSO</p>
</blockquote></td>
<td><blockquote>
<p>7.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RADIOLOGY/NUCLEAR MEDICINE</p>
<p>RA*5*56</p>
</blockquote></td>
<td><blockquote>
<p>RA</p>
</blockquote></td>
<td><blockquote>
<p>5.0</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TOOLKIT</p>
<p>XT*7.3*111</p>
</blockquote></td>
<td><blockquote>
<p>XT</p>
</blockquote></td>
<td><blockquote>
<p>7.3</p>
</blockquote></td>
<td></td>
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

> Required Software for GMTS\*2.7\*89

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
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
<p>HEALTH SUMMARY GMTS*2.7*58 GMTS*2.7*63</p>
<p>GMTS*2.7*82</p>
</blockquote></td>
<td><blockquote>
<p>GMTS</p>
</blockquote></td>
<td><blockquote>
<p>2.7</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Required Software for OR\*3.0\*295

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
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
<p>ORDER ENTRY/RESULTS REPORTING</p>
<p>OR*3.0*301</p>
</blockquote></td>
<td><blockquote>
<p>OR</p>
</blockquote></td>
<td><blockquote>
<p>3.0</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Required Software for TIU\*1.0\*249

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Package/Patch</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Namespace</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Comments</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>TEXT INTEGRATION UTILITIES TIU*1.0*105</p>
<p>TIU*1.0*135</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>TIU</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>1.0</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> <span id="Estimated_Installation_Time:_10-15_minut" class="anchor"></span>Estimated Installation Time: 10-15 minutes

### Embedded Fragment Surveillance Center (TEFSC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Please provide the TEFSC with contact information for the veteran's primary healthcare provider or enter contact information for the VA medical center staff member deemed appropriate by your VA facility.

> The point of contact is the person that TEFSC will contact to help arrange for follow-up activities such as biomonitoring.

> <span id="Installation" class="anchor"></span><u>Installation</u>

> This build can be installed with users on the system, but it should be done during non-peak hours.

> *The installation needs to be done by a person with DUZ(0) set to "@."*

### Retrieve host file containing the multi-package build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use ftp to access the build (the name of the host file is PXRM_2_0_12_MPB.KID) from one of the following locations:

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
<th><blockquote>
<p>ftp.fo-albany.med.va.gov</p>
</blockquote></th>
<th><blockquote>
<p>&lt;ftp://ftp.fo-albany.med.va.gov&gt;</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><blockquote>
<p>ftp.fo-hines.med.va.gov</p>
</blockquote></td>
<td><blockquote>
<p>&lt;ftp://ftp.fo-hines.med.va.gov&gt;</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><blockquote>
<p>ftp.fo-slc.med.va.gov</p>
</blockquote></td>
<td><blockquote>
<p>&lt;ftp://ftp.fo-slc.med.va.gov&gt;</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Install the build first in a training or test account.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

### Load the distribution.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name and PXRM_2_0_12_MPB.KID at the Host File prompt.

> Example

> From the Installation menu, you may elect to use the following options:

### Backup a Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

### Compare Transport Global to Current System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

### Verify Checksums in Transport Global

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system.

> Retrieve the file again from the anonymous directory (in case there was corruption in FTPing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

### Print Transport Global (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view the components of the KIDS build.

### Install the build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*12 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

> Answer "NO" to the following prompt:

> Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE: DO NOT QUEUE THE INSTALLATION, because this installation may ask questions requiring responses and queuing will stop the installation. The most common are replacements for finding items or quick orders during the installation of Reminder Exchange file entries. This installation may ask for a replacement order dialog.

> Installation Example

> See [<u>Appendix</u>](#Appendix_A:_Installation_Example) .

### Install File Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi- package build.

### Build File Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

### Post-installation routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The installation will place the following exchange file entries in the Reminder Exchange file \#811.8:

> PATCH 12 ITEMS UPDATE VA-DIABETES

> VA-EMBEDDED FRAGMENTS RISK EVALUATION VA-EMBEDDED FRAGMENTS SCREEN

> VA-MHV BMI COLORECTAL UPDATES PATCH 12 VA-MHV HIGH RISK TERMS

> VA-MHV HYPERTENSION

> VA-MHV MAMMOGRAM SCREENING VA-MHV RETINOPATHY TERMS

> RT VA-ALCOHOL NONE PAST 1YR TX HIGH RISK FLU AND PNEUMONIA

> VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL VA-DEPRESSION SCREENING

> VA-OEF/OIF MONITOR

> VA-TBI/POLY IDT EVALUATIONS ELEMENT UPDATE VA-BL DEPRESSION SCREEN

> PXRM VISIT DATE MONTH REQ YEAR BLANK VA-OEF/OIF MONITOR REPORTING

> VA-IRAQ AFGHAN

> VA-DISABLE BRANCHING LOGIC REPLACEMENT ELEMENT

> The post-init will install all the components of these Exchange file entries on your system. After the installation has finished, if you discover that any of these components weren’t installed correctly, you can use the Reminder Exchange option on the Reminders Manager Menu to install them.

### Deletion of init routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After everything has been successfully installed you may delete the following init routines: PXRMP12E, PXRMP12I

> <span id="Appendix_A:_Installation_Example" class="anchor"></span><u>Appendix A: Installation Example</u>

> Select Installation Option: 1 Load a Distribution Enter a Host File: PXRM_2_0_12_MPB.KID

> KIDS Distribution saved on Aug 13, 2009@11:04:24

> Comment: PXRM\*2.0\*12, GMTS\*2.7\*89, OR\*3.0\*295, TIU\*1.0\*249

> This Distribution contains Transport Globals for the following Package(s): PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0

> GMTS\*2.7\*89 OR\*3.0\*295 TIU\*1.0\*249 PXRM\*2.0\*12

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0 GMTS\*2.7\*89

> OR\*3.0\*295 TIU\*1.0\*249 PXRM\*2.0\*12

> Use INSTALL NAME: PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0 to install this

> Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0 Loaded fro

> m Distribution 8/13/09@14:33:18

> =\> PXRM\*2.0\*12, GMTS\*2.7\*89, OR\*3.0\*295, TIU\*1.0\*249 ;Created on Aug 13,

> This Distribution was loaded on Aug 13, 2009@14:33:18 with header of PXRM\*2.0\*12, GMTS\*2.7\*89, OR\*3.0\*295, TIU\*1.0\*249 ;Created on Aug 13, 2009@1

> 1:04:24

> It consisted of the following Install(s):

> PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0 GMTS\*2.7\*89 OR\*3.0\*295 TIU\*1.0\*249 PXRM\*2.0\*12

> Checking Install for Package PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0 Install Questions for PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0

> Checking Install for Package GMTS\*2.7\*89 Install Questions for GMTS\*2.7\*89 Incoming Files:

> 142.5 HEALTH SUMMARY OBJECTS

> Note: You already have the 'HEALTH SUMMARY OBJECTS' File. Checking Install for Package OR\*3.0\*295

> Install Questions for OR\*3.0\*295

> Checking Install for Package TIU\*1.0\*249 Install Questions for TIU\*1.0\*249

> Checking Install for Package PXRM\*2.0\*12 Install Questions for PXRM\*2.0\*12 Incoming Files:

> 801.41 REMINDER DIALOG

> Note: You already have the 'REMINDER DIALOG' File.

1.  REMINDER REPORT TEMPLATE

> Note: You already have the 'REMINDER REPORT TEMPLATE' File.

2.  REMINDER EXTRACT DEFINITION

> Note: You already have the 'REMINDER EXTRACT DEFINITION' File.

4.  REMINDER LIST RULE

> Note: You already have the 'REMINDER LIST RULE' File.

5.  REMINDER PATIENT LIST

> Note: You already have the 'REMINDER PATIENT LIST' File.

7.  REMINDER EXTRACT COUNTING RULE

> Note: You already have the 'REMINDER EXTRACT COUNTING RULE' File.

8.  REMINDER COUNTING GROUP

> Note: You already have the 'REMINDER COUNTING GROUP' File.

9.  REMINDER LOCATION LIST

> Note: You already have the 'REMINDER LOCATION LIST' File.

> 811.2 REMINDER TAXONOMY

> Note: You already have the 'REMINDER TAXONOMY' File.

4.  REMINDER COMPUTED FINDINGS (including data) Note: You already have the 'REMINDER COMPUTED FINDINGS' File. I will OVERWRITE your data with mine.
5.  REMINDER TERM

> Note: You already have the 'REMINDER TERM' File.

6.  REMINDER SPONSOR

> Note: You already have the 'REMINDER SPONSOR' File.

8.  REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.
9.  REMINDER DEFINITION

> Note: You already have the 'REMINDER DEFINITION' File.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// y YES

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET TERMINAL

> PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0

> Install Started for PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0 : Aug 13, 2009@14:39:16

> Build Distribution Date: Aug 13, 2009 Installing Routines

> Aug 13, 2009@14:39:16

> Install Started for GMTS\*2.7\*89 :

> Aug 13, 2009@14:39:16

> Build Distribution Date: Aug 13, 2009 Installing Routines

> Aug 13, 2009@14:39:17

> Installing Data Dictionaries:

> Aug 13, 2009@14:39:17

> Running Post-Install Routine:

> Filing "CLINICAL REMINDERS FINDINGS" component in Health Summary Successfully installed new component

> Filing "CLINICAL REMINDERS LAST DONE" component in Health Summary Successfully installed new component

> Re-Indexing Health Summary Component file ................ \< done \> Re-Indexing Health Summary Type file ..................... \< done \>

> Ad Hoc Summary

> Gathering Ad Hoc Summary information.................... \< done \> Purging old Ad Hoc Summary.............................. \< done \>

> Rebuilding Ad Hoc Summary............................... \< done \> Ad Hoc Health Summary successfully rebuilt

> Updating Routine file…

> GMTS\*2.7\*89 Installed.

> Aug 13, 2009@14:39:21

> Not a production UCI NO Install Message sent

> Install Started for OR\*3.0\*295 :

> Aug 13, 2009@14:39:21

> Build Distribution Date: Aug 13, 2009 Installing Routines...

> Aug 13, 2009@14:39:21

> Updating Routine file... OR\*3.0\*295 Installed.

> Aug 13, 2009@14:39:21

> Not a production UCI NO Install Message sent

> TIU\*1.0\*249

> Install Started for TIU\*1.0\*249 :

> Aug 13, 2009@14:39:21

> Build Distribution Date: Aug 13, 2009 Installing Routines:

> Aug 13, 2009@14:39:21

> Installing PACKAGE COMPONENTS: Installing PARAMETER DEFINITION

> Aug 13, 2009@14:39:21

> Updating Routine file... Updating KIDS files...

> TIU\*1.0\*249 Installed.

> Aug 13, 2009@14:39:21

> Not a production UCI NO Install Message sent

> PXRM\*2.0\*12 \[

> Install Started for PXRM\*2.0\*12 :

> Aug 13, 2009@14:39:21

> Build Distribution Date: Aug 13, 2009 Installing Routines:

> Aug 13, 2009@14:39:23

> Running Pre-Install Routine: PRE^PXRMP12I DISABLE options.

> DISABLE protocols.

> Removing old data dictionaries.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 4%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Deleting</th>
<th><blockquote>
<p>data</p>
</blockquote></th>
<th><blockquote>
<p>dictionary</p>
</blockquote></th>
<th>for</th>
<th><blockquote>
<p>file</p>
</blockquote></th>
<th>#</th>
<th><blockquote>
<p>801.41</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>810.1</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>810.2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>810.4</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>810.5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>810.7</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>810.8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>810.9</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>811.2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>811.4</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>811.5</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>811.6</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>811.8</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Deleting</td>
<td><blockquote>
<p>data</p>
</blockquote></td>
<td><blockquote>
<p>dictionary</p>
</blockquote></td>
<td>for</td>
<td><blockquote>
<p>file</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>811.9</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Installing Data Dictionaries: Aug 13, 2009@14:39:27 Installing Data:

> Aug 13, 2009@14:39:29

> Installing PACKAGE COMPONENTS:

> Installing PRINT TEMPLATE

> Installing INPUT TEMPLATE Installing PROTOCOL

> Located in the PXRM (CLINICAL REMINDERS) namespace.

> Installing LIST TEMPLATE Installing OPTION

> Aug 13, 2009@14:39:30

> Running Post-Install Routine: POST^PXRMP12I Fixing bad Location List nodes.

> No bad nodes were found.

> Rebuilding all taxonomy expansions. Expanding VA-HYPERTENSION (IEN=1) Expanding VA-HEPATITIS C INFECTION (IEN=2)

> Expanding EMPHYSEMA (IEN=3) Expanding VA-COLORECTAL CA (IEN=4)

> Expanding VA-CERVICAL CA/ABNORMAL PAP (IEN=5) Expanding VA-HYSTERECTOMY (IEN=6)

> Expanding COPD (IEN=7)

> Expanding VA-PROSTATE CA (IEN=8)

> Expanding VA-HIGH RISK FOR FLU/PNEUMONIA (IEN=9) Expanding VA-TB/POSITIVE PPD (IEN=10)

> Expanding VA-HIGH RISK FOR TB (IEN=11) Expanding COR PULMONALE (IEN=12) Expanding INTERSTITIAL DISEASE (IEN=13) Expanding MIGRAIN HEADACHES (IEN=14) Expanding VA-FLEXISIGMOIDOSCOPY (IEN=15) Expanding VA-MAMMOGRAM/SCREEN (IEN=16) Expanding VA-ALCOHOL ABUSE (IEN=17) Expanding VA-BREAST TUMOR (IEN=18) Expanding VA-MASTECTOMY (IEN=19) Expanding VA-OBESITY (IEN=20)

> Expanding VA-NUTRITION (IEN=21) Expanding VA-TOBACCO USE (IEN=22)

> Expanding VA-HYPERTENSION SCREEN (IEN=23) Expanding VA-CHOLESTEROL (IEN=24) Expanding VA-PNEUMOCOCCAL VACCINE (IEN=25)

> Expanding VA-PSA (IEN=26) Expanding VA-FOBT (IEN=27) Expanding VA-DIABETES (IEN=28)

> Expanding VA-TETANUS DIPHTHERIA (IEN=29) Expanding VA-CERVICAL CANCER SCREEN (IEN=30) Expanding VA-COLORECTAL CANCER SCREEN (IEN=31) Expanding VA-EXERCISE COUNSELING (IEN=32) Expanding VA-INFLUENZA IMMUNIZATION (IEN=33) Expanding VA-ALCOHOLISM SCREENING (IEN=34) Expanding VA-SAFETY COUNSELING (IEN=35)

> Expanding VA-WEIGHT AND NUTRITION SCREEN (IEN=36)

> Expanding HYPOXIA (IEN=37)

> Expanding CHRONIC OBSTRUCTIVE BRONCHITIS (IEN=38) Expanding CHRONIC OBSTRUCTIVE ASTHMA (IEN=39) Expanding CONGESTIVE HEALTH FAILURE (IEN=40) Expanding SECONDARY POLYCYTHEMIA (IEN=41) Expanding SLEEP APNEA (IEN=42)

> Expanding Advance Directives (IEN=43) Expanding VA-HYPERTENSION CODES (IEN=44) Expanding VA-ISCHEMIC HEART DISEASE (IEN=45) Expanding DEPRESSION CODES (IEN=46) Expanding SATP ENROLLMENT (IEN=47)

> Expanding HIGH RISK COLONOSCOPY (IEN=48) Expanding VA-DEPRESSION DIAGNOSIS (IEN=49) Expanding VA-PSYCHOTHERAPY CPT CODES (IEN=50) Expanding HIGH RISK COLON POLPS (IEN=51) Expanding VA-SCHIZOPHRENIA (IEN=52)

> Expanding CA pneumonia (IEN=53) Expanding ESOPHAGUS CANCER (IEN=54) Expanding LIVER CANCER (IEN=55) Expanding PANCREAS CANCER (IEN=56) Expanding HEART FAILURE (IEN=57) Expanding FOBT COMPLETE (IEN=58)

> Expanding POST-OP WOUND INFECTION (IEN=59) Expanding VA-ISCHEMIC HEART 412 DISEASE (IEN=60) Expanding VA-TERMINAL CANCER PATIENTS (IEN=61) Expanding VA-WH BILATERAL MASTECTOMY (IEN=62) Expanding VA-WH PAP SMEAR OBTAINED (IEN=63)

> Expanding VA-WH HYSTERECTOMY W/CERVIX REMOVED (IEN=64) Expanding VA-WH PAP SMEAR SCREEN CODES (IEN=65) Expanding VA-MHV IHD AND ATHERSCLEROSIS (IEN=66) Expanding DEMENTIA CODES - SHERIDAN (IEN=67) Expanding CHY-HYPOTHYROIDISM (IEN=68)

> Expanding CHY AAA DIAGNOSIS (IEN=69) Expanding OVERWEIGHT (IEN=72) Expanding OBESITY 278.00 (IEN=73)

> Expanding SLC-MOVE CO-MORBIDITIES (IEN=74) Expanding VA-MHV COLONOSCOPY (IEN=85) Expanding VA-MHV SIGMOIDOSCOPY (IEN=86) Expanding VA-MHV BILATERAL AMPUTEE (IEN=87)

> Expanding VA-MHV DIABETIC RETINAL DISEASE (IEN=88) Expanding VA-MHV RETINAL EXAMINATION (IEN=89) Expanding VA-DEPRESSION DX OUTPT VISIT (IEN=160) Expanding VA-PTSD DIAGNOSIS (IEN=161)

> Expanding VA-PTSD DX OUTPT VISIT (IEN=176) Expanding COLON REMOVAL (IEN=442001) Expanding CHEY-COPD (IEN=442002)

> Expanding CHEY-SPIROMETRY/PFT (IEN=442003)

> Expanding HIGH RISK FLU/PNEUMONIA (IEN=442004) Expanding CHEY-HEALTHY LIFESTYLE (IEN=442005) Expanding VESTED CODES (IEN=442006)

> Expanding HEP C INFECTION (IEN=442007) Expanding CHEY-HEP B VACCINE (IEN=442008) Expanding CHEY-TB HIGH RISK (IEN=442009) Expanding CHEY-HYSTERECTOMY (IEN=442010) Expanding CHEY-EMP (IEN=442011)

> Expanding CHEY-HEP A VACCINE (IEN=442012) Expanding CHEY-CERVICAL CANCER SCREEN (IEN=442013) Expanding BILATERIAL MASTECTOMY (IEN=442014) Expanding CHEY-CVA (IEN=442015)

> Expanding CHEY-HGB A1C (IEN=442016) Expanding CHEY-PARAPLEGIC (IEN=442017) Expanding NEW EMPLOYEE CODES (IEN=442018) Expanding CHEY-TOTAL BLINDNESS (IEN=442019) Expanding CHEY-BIL AMPUTEE (IEN=442020) Expanding DIABETIC EYE EXAM (IEN=442021) Expanding COLONOSCOPY (IEN=442022) Expanding COLON REMOVAL-TOTAL (IEN=442023) Expanding COLORECTAL CANCER (IEN=442024)

> Expanding FAMILY HX of Colon CA (IEN=442025) Expanding REGIONAL ENTERITIS (IEN=442026) Expanding ULCERATIVE COLITIS (IEN=442027) Expanding COLON POLYPS (IEN=442028)

> Expanding FEMALE ENDOMETRIUM/OVARIAN(GJ) (IEN=442029) Expanding COLITIS/ILEITIS(GJ) (IEN=442030)

> Expanding SIGMOIDOSCOPY (IEN=442031) Expanding SCHIZOPHRENIA (IEN=442032) Expanding POSITIVE PPD (IEN=442033)

> Expanding LESION REMOVAL/COLONOSCOPY (IEN=442034) Expanding HISTORY OF COLON POLYPS (IEN=442035) Expanding ACUTE MI (IEN=442036)

> Expanding IRRITABLE BOWEL SYNDROME (IEN=442037)

> Done rebuilding taxonomy expansions. ENABLE options.

> ENABLE protocols.

> There are 20 Reminder Exchange entries to be installed.

1.  Installing Reminder Exchange entry PATCH 12 ITEMS
2.  Installing Reminder Exchange entry UPDATE VA-DIABETES
3.  Installing Reminder Exchange entry VA-EMBEDDED FRAGMENTS RISK EVALUATION
4.  Installing Reminder Exchange entry VA-EMBEDDED FRAGMENTS SCREEN
5.  Installing Reminder Exchange entry VA-MHV BMI COLORECTAL UPDATES PATCH 12
6.  Installing Reminder Exchange entry VA-MHV HIGH RISK TERMS
7.  Installing Reminder Exchange entry VA-MHV HYPERTENSION
8.  Installing Reminder Exchange entry VA-MHV MAMMOGRAM SCREENING
9.  Installing Reminder Exchange entry VA-MHV RETINOPATHY TERMS
10. Installing Reminder Exchange entry RT VA-ALCOHOL NONE PAST 1YR
11. Installing Reminder Exchange entry TX HIGH RISK FLU AND PNEUMONIA
12. Installing Reminder Exchange entry VA-ALCOHOL AUDIT-C POSITIVE F/U EVAL
13. Installing Reminder Exchange entry VA-DEPRESSION SCREENING
14. Installing Reminder Exchange entry VA-OEF/OIF MONITOR
15. Installing Reminder Exchange entry VA-TBI/POLY IDT EVALUATIONS ELEMENT UPDATE
16. Installing Reminder Exchange entry VA-BL DEPRESSION SCREEN
17. Installing Reminder Exchange entry PXRM VISIT DATE MONTH REQ YEAR BLANK
18. Installing Reminder Exchange entry VA-OEF/OIF MONITOR REPORTING
19. Installing Reminder Exchange entry VA-IRAQ AFGHAN
20. Installing Reminder Exchange entry VA-DISABLE BRANCHING LOGIC REPLACEMENT

> ELEMENT

> Rebuilding all taxonomy expansions. Expanding VA-HYPERTENSION (IEN=1) Expanding VA-HEPATITIS C INFECTION (IEN=2)

> Expanding EMPHYSEMA (IEN=3) Expanding VA-COLORECTAL CA (IEN=4)

> Expanding VA-CERVICAL CA/ABNORMAL PAP (IEN=5) Expanding VA-HYSTERECTOMY (IEN=6)

> Expanding COPD (IEN=7)

> Expanding VA-PROSTATE CA (IEN=8)

> Expanding VA-HIGH RISK FOR FLU/PNEUMONIA (IEN=9) Expanding VA-TB/POSITIVE PPD (IEN=10)

> Expanding VA-HIGH RISK FOR TB (IEN=11) Expanding COR PULMONALE (IEN=12) Expanding INTERSTITIAL DISEASE (IEN=13) Expanding MIGRAIN HEADACHES (IEN=14) Expanding VA-FLEXISIGMOIDOSCOPY (IEN=15) Expanding VA-MAMMOGRAM/SCREEN (IEN=16) Expanding VA-ALCOHOL ABUSE (IEN=17) Expanding VA-BREAST TUMOR (IEN=18) Expanding VA-MASTECTOMY (IEN=19) Expanding VA-OBESITY (IEN=20)

> Expanding VA-NUTRITION (IEN=21) Expanding VA-TOBACCO USE (IEN=22)

> Expanding VA-HYPERTENSION SCREEN (IEN=23) Expanding VA-CHOLESTEROL (IEN=24) Expanding VA-PNEUMOCOCCAL VACCINE (IEN=25)

> Expanding VA-PSA (IEN=26) Expanding VA-FOBT (IEN=27) Expanding VA-DIABETES (IEN=28)

> Expanding VA-TETANUS DIPHTHERIA (IEN=29) Expanding VA-CERVICAL CANCER SCREEN (IEN=30) Expanding VA-COLORECTAL CANCER SCREEN (IEN=31) Expanding VA-EXERCISE COUNSELING (IEN=32) Expanding VA-INFLUENZA IMMUNIZATION (IEN=33) Expanding VA-ALCOHOLISM SCREENING (IEN=34) Expanding VA-SAFETY COUNSELING (IEN=35)

> Expanding VA-WEIGHT AND NUTRITION SCREEN (IEN=36)

> Expanding HYPOXIA (IEN=37)

> Expanding CHRONIC OBSTRUCTIVE BRONCHITIS (IEN=38) Expanding CHRONIC OBSTRUCTIVE ASTHMA (IEN=39) Expanding CONGESTIVE HEALTH FAILURE (IEN=40) Expanding SECONDARY POLYCYTHEMIA (IEN=41) Expanding SLEEP APNEA (IEN=42)

> Expanding Advance Directives (IEN=43) Expanding VA-HYPERTENSION CODES (IEN=44) Expanding VA-ISCHEMIC HEART DISEASE (IEN=45) Expanding DEPRESSION CODES (IEN=46) Expanding SATP ENROLLMENT (IEN=47)

> Expanding HIGH RISK COLONOSCOPY (IEN=48) Expanding VA-DEPRESSION DIAGNOSIS (IEN=49) Expanding VA-PSYCHOTHERAPY CPT CODES (IEN=50) Expanding HIGH RISK COLON POLPS (IEN=51) Expanding VA-SCHIZOPHRENIA (IEN=52)

> Expanding CA pneumonia (IEN=53) Expanding ESOPHAGUS CANCER (IEN=54) Expanding LIVER CANCER (IEN=55) Expanding PANCREAS CANCER (IEN=56) Expanding HEART FAILURE (IEN=57) Expanding FOBT COMPLETE (IEN=58)

> Expanding POST-OP WOUND INFECTION (IEN=59) Expanding VA-ISCHEMIC HEART 412 DISEASE (IEN=60)

> Expanding VA-TERMINAL CANCER PATIENTS (IEN=61) Expanding VA-WH BILATERAL MASTECTOMY (IEN=62) Expanding VA-WH PAP SMEAR OBTAINED (IEN=63)

> Expanding VA-WH HYSTERECTOMY W/CERVIX REMOVED (IEN=64) Expanding VA-WH PAP SMEAR SCREEN CODES (IEN=65) Expanding VA-MHV IHD AND ATHERSCLEROSIS (IEN=66) Expanding DEMENTIA CODES - SHERIDAN (IEN=67) Expanding CHY-HYPOTHYROIDISM (IEN=68)

> Expanding CHY AAA DIAGNOSIS (IEN=69)

> Expanding VA-HIGH RISK FOR PNEUMOCOCCAL DZ (IEN=70) Expanding VA-HIGH RISK FOR INFLUENZA (IEN=71) Expanding OVERWEIGHT (IEN=72)

> Expanding OBESITY 278.00 (IEN=73) Expanding SLC-MOVE CO-MORBIDITIES (IEN=74) Expanding VA-MHV COLONOSCOPY (IEN=85) Expanding VA-MHV SIGMOIDOSCOPY (IEN=86)

> Expanding VA-MHV BILATERAL AMPUTEE (IEN=87) Expanding VA-MHV DIABETIC RETINAL DISEASE (IEN=88) Expanding VA-MHV RETINAL EXAMINATION (IEN=89) Expanding VA-DEPRESSION DX OUTPT VISIT (IEN=160) Expanding VA-PTSD DIAGNOSIS (IEN=161)

> Expanding VA-PTSD DX OUTPT VISIT (IEN=176) Expanding COLON REMOVAL (IEN=442001) Expanding CHEY-COPD (IEN=442002)

> Expanding CHEY-SPIROMETRY/PFT (IEN=442003) Expanding HIGH RISK FLU/PNEUMONIA (IEN=442004) Expanding CHEY-HEALTHY LIFESTYLE (IEN=442005) Expanding VESTED CODES (IEN=442006)

> Expanding HEP C INFECTION (IEN=442007) Expanding CHEY-HEP B VACCINE (IEN=442008) Expanding CHEY-TB HIGH RISK (IEN=442009) Expanding CHEY-HYSTERECTOMY (IEN=442010) Expanding CHEY-EMP (IEN=442011)

> Expanding CHEY-HEP A VACCINE (IEN=442012) Expanding CHEY-CERVICAL CANCER SCREEN (IEN=442013) Expanding BILATERIAL MASTECTOMY (IEN=442014) Expanding CHEY-CVA (IEN=442015)

> Expanding CHEY-HGB A1C (IEN=442016) Expanding CHEY-PARAPLEGIC (IEN=442017) Expanding NEW EMPLOYEE CODES (IEN=442018) Expanding CHEY-TOTAL BLINDNESS (IEN=442019) Expanding CHEY-BIL AMPUTEE (IEN=442020) Expanding DIABETIC EYE EXAM (IEN=442021) Expanding COLONOSCOPY (IEN=442022) Expanding COLON REMOVAL-TOTAL (IEN=442023) Expanding COLORECTAL CANCER (IEN=442024)

> Expanding FAMILY HX of Colon CA (IEN=442025) Expanding REGIONAL ENTERITIS (IEN=442026) Expanding ULCERATIVE COLITIS (IEN=442027) Expanding COLON POLYPS (IEN=442028)

> Expanding FEMALE ENDOMETRIUM/OVARIAN(GJ) (IEN=442029) Expanding COLITIS/ILEITIS(GJ) (IEN=442030)

> Expanding SIGMOIDOSCOPY (IEN=442031) Expanding SCHIZOPHRENIA (IEN=442032) Expanding POSITIVE PPD (IEN=442033)

> Expanding LESION REMOVAL/COLONOSCOPY (IEN=442034) Expanding HISTORY OF COLON POLYPS (IEN=442035) Expanding ACUTE MI (IEN=442036)

> Expanding IRRITABLE BOWEL SYNDROME (IEN=442037)

> Done rebuilding taxonomy expansions. Cross-reference 'RG' created.

> Updating Routine file... Updating KIDS files...

> PXRM\*2.0\*12 Installed.

> Aug 13, 2009@14:49:25

> Not a production UCI NO Install Message sent

> Updating Routine file... Updating KIDS files...

> PXRM V2.0 PATCH 12 MULTI-PACKAGE BUILD 0.0 Installed.

> Aug 13, 2009@14:49:25