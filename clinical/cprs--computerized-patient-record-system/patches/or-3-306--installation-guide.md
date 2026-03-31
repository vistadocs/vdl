---
title: OR*3*306 Installation Guide CPRS GUI 29
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: CPRS GUI 29
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*306
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 3
description: The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order la
audience: 
keywords: 
  - install
  - cprs
  - installation
  - table
  - contents
  - correct
  - patch
  - filed
  - distribution
  - package
page_count: 0
word_count: 10793
section_count: 20
table_count: 1
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: May 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_306_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_306_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Computerized Patient Record System Graphical User Interface (CPRS GUI)
---

Installation Guide

Version 29

![](or-3-306-installation-guide-cprs-gui-29/001.png)

May 2013

Office of Information & Technology (OI&T)

Product Development (PD)

This page left intentionally blank.

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 56%" />
<col style="width: 17%" />
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
<td>08/06/2012</td>
<td>1.00</td>
<td>Baseline first published copy</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/08/2013</td>
<td>1.01</td>
<td>Changes per Implementation Team meeting 1/7/13</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/01/2013</td>
<td>1.02</td>
<td>Changes to bundling of patches</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/08/2013</td>
<td>1.03</td>
<td><p>Added new content from Danny’s “basic” installation notes for GUI installation for msi/smp files.</p>
<p>Inserted Appendix A—Troubleshooting Guide for advanced GUI installation options from Danny’s “advanced” notes</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/10/2013</td>
<td>1.04</td>
<td>Revised Sections 2.3 (Pre-requisites), 3 (Installation Checklist) and 4 (Software Retrieval) with updated information</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/17/2013</td>
<td>1.05</td>
<td><p>Further edits to GUI Installation sections</p>
<p>Added M patch installation Sample as Appendix B</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/19/2013</td>
<td>1.06</td>
<td>Further edits to GUI Installation sections</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>04/26/2013</td>
<td>1.07</td>
<td><p>Edited latest revision to pre-requisite patches list.</p>
<p>Added new section 5.4 for Additional Patches which are installed AFTER CPRS 29. Inserted section for patch OR*#.0*371</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/29/2013</td>
<td>1.08</td>
<td>Minor edits</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/07/2013</td>
<td>1.09</td>
<td><p>Add patch PSO*7*426</p>
<p>Revised installation instructions for host files</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/15/2013</td>
<td>1.10</td>
<td>Edited Documentation section (currently 5.5)</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/21/2013</td>
<td>1.11</td>
<td>Multiple small edits</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/22/2013</td>
<td>1.12</td>
<td><p>Replaced OR*3.0*371 packman installation instructions with instructions for a host file installation.</p>
<p>Fixed some broken cross-references.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

# # Computerized Patient Record System Graphical User Interface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Computerized Patient Record System Graphical User Interface](#computerized-patient-record-system-graphical-user-interface)
  - [Overview](#overview)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [National Deployment](#national-deployment)
  - [Document Conventions](#document-conventions)
  - [Related Documents](#related-documents)
- [Pre-requisites](#pre-requisites)
  - [Deployment Authorization](#deployment-authorization)
  - [DEA Preparation](#dea-preparation)
  - [Pre-requisite Patches](#pre-requisite-patches)
- [CPRS v29 Installation Checklist](#cprs-v29-installation-checklist)
- [Software Retrieval](#software-retrieval)
- [Installation Sequence](#installation-sequence)
  - [Additional Required Patches](#additional-required-patches)
    - [HDI\1\11](#hdi111)
    - [PSS\1\166](#pss1166)
    - [CPRSV29PSOPSD.KID (PSO\7\391 and PSD\3\73)](#cprsv29psopsdkid-pso7391-and-psd373)
  - [CPRS v29 Host File (ORGMPLGMTSXU29.KID)](#cprs-v29-host-file-orgmplgmtsxu29kid)
  - [Additional Required Patches (continued)](#additional-required-patches-continued)
    - [OR\3.0\371](#or30371)
    - [PSO\7\426](#pso7426)
  - [CPRS GUI Executable (OR30306.zip)](#cprs-gui-executable-or30306zip)
    - [Changes to the Installation Procedure for the CPRS GUI](#changes-to-the-installation-procedure-for-the-cprs-gui)
    - [Methods of installation](#methods-of-installation)
    - [Overview of the new process: Loader in front of CPRS](#overview-of-the-new-process-loader-in-front-of-cprs)
    - [Changes for the End User](#changes-for-the-end-user)
    - [Automation Capabilities](#automation-capabilities)
    - [Manual Installation](#manual-installation)
  - [CPRS Documentation](#cprs-documentation)
  - [Post-installation Configuration](#post-installation-configuration)
- [Parameters Introduced/Changed with CPRS GUI v29](#parameters-introducedchanged-with-cprs-gui-v29)
  - [ORQQPL SUPPRESS CODES](#orqqpl-suppress-codes)
  - [OR DEA PIV LINK MSG](#or-dea-piv-link-msg)
  - [ORCDGMRC EARLIEST DATE DEFAULT](#orcdgmrc-earliest-date-default)
- [# ## CPRS GUI Installation Troubleshooting Guide](#cprs-gui-installation-troubleshooting-guide)
    - [Interface: Visual GUI and Switches](#interface-visual-gui-and-switches)
    - [Uninstallation](#uninstallation)
    - [Dual Shortcuts](#dual-shortcuts)
    - [Windows XP Installations](#windows-xp-installations)
    - [Self-Repair](#self-repair)
    - [Version numbers—Loader versus CPRS](#version-numbersloader-versus-cprs)
    - [Batch File](#batch-file)
    - [DLL Distribution](#dll-distribution)
    - [Delay Updating from MSP File during Installation](#delay-updating-from-msp-file-during-installation)
    - [Do Not Modify the MSI and MSP Files](#do-not-modify-the-msi-and-msp-files)
  - [CPRS v29 M patches—Software Installation Sample](#cprs-v29-m-patchessoftware-installation-sample)
    - [HDI\1\11](#hdi111-1)
    - [PSS\1\166](#pss1166-1)
    - [CPRSV29PSOPSD.KID](#cprsv29psopsdkid)
    - [ORGMPLGMTSXU29.KID](#orgmplgmtsxu29kid)
    - [OR\3.0\371](#or30371-1)
    - [PSO\7\426](#pso7426-1)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

This installation guide deals specifically with the installation of CPRS GUI v29 (patch OR\*3.0\*306) and its associated patches and Windows application. CPRS GUI v29 includes projects to implement the electronic ordering of controlled substances, the display of information concerning the Mental Health Treatment Coordinator and the Problem List use of SNOMED-CT codes to record patient problems. A number of other defects found by the field were also corrected.

Before using this guide, sites should have completed the necessary pre-installation and configuration needed to fully implement electronic prescribing of controlled substances as required by the Drug Enforcement Agency (DEA). See Section 2.2, DEA Preparation, below.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) Information Resource Management (IRM) staff.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation guide provides instructions for:

- Installing application components that run on M servers at VAMC facilities
- Installing Windows executable programs on workstations or application servers at VAMC facilities
- Performing post-installation tasks—including configuration tasks—that require knowledge of the underlying VistA system

## National Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v29 will follow a phased deployment. Groups of site will work with the CPRS Implementation Manager to install CPRS v29 and its related patches. The installation will have two parts, a Pre CPRS v29 DEA Preliminary Patch Installation and Set Up and then the CPRS v29 and associated patches installation.

To see current status and target dates, please refer to the [CPRS GUI v29 Deployment Schedule workbook](http://vaww.oed.portal.va.gov/projects/CPRS/v29_main/Public/Forms/AllItems.aspx?RootFolder=%2fprojects%2fCPRS%2fv29%5fmain%2fPublic%2fCPRS%20GUI%20v29%20Deployment%20Schedule).

One week prior to each deployment wave commencement, instruction will be sent to each site in that deployment wave concerning how to access a secured FTP site, including the necessary credentials, the list of files they should download and the download format required (ASCII/binary).

After the completion of the final deployment wave, the software will be made available on the national anonymous FTP site for access by any VA network domain member.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Examples of VistA “Roll and Scroll” interface actions will be shown in a box such as this:

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

Emphasis of important points may be displayed in this manner:

1.  This is an important point and must not be omitted.

Call-outs may be used to draw attention to part of a block of text or a table without disrupting the flow of the block or table. For example:

Sample text, Sample text, Sample text, Sample text

Sample text, Sample text, Sample text

Sample text, Sample text, Sample text

Sample text, Sample text, Sample text

Sample text, Sample text

Sample text, Sample text, Sample text, Sample text

Sample text

Sample text, Sample text, Sample text, SOMETHING OF NOTE!!

Sample text, Sample text, Sample text, Sample text, Sample text, Sample text

Sample text, Sample text, Sample text, Sample text, Sample text

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents, in addition to this document, are available on the VA Software Document Library (VDL):

[CPRS on the VDL](http://www.va.gov/vdl/application.asp?appid=61)

- DEA e-Prescribing Setup Installation and Configuration Guide
- CPRS Technical Manual
- CPRS Technical Manual: GUI Version
- CPRS User Guide: GUI Version
- CPRS GUI v29 (Patch# OR\*3.0\*306) Release Notes

The following document, available on the [CPRS v 29 SharePoint site](http://vaww.oed.portal.va.gov/projects/CPRS/v29_main), is a useful resource for sites preparing for DEA EPCS and its associated infrastructure requirements.

- [CPRS v29 EPCS Pre-implementation Guide](http://vaww.oed.portal.va.gov/projects/CPRS/v29_main/Public/Public%20Documentation/CPRS%20v29%20EPCS%20Pre-implementation%20Guide.pdf)

# Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the processes described in this document the tasks outlined in this section must be completed.

## Deployment Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Receive authorization to proceed based upon the deployment schedule discussed in Section 1.4, National Deployment, above

## DEA Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Complete all parts of the preceding document “DEA e-Prescribing Setup Installation and Configuration Guide”, which was distributed with the package “CPRS29_DEA_SETUP.KID”

## Pre-requisite Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following, previously released, patches must be installed:

- SD\*5.3\*575
- OR\*3\*181
- OR\*3\*204
- OR\*3\*294
- OR\*3\*331
- OR\*3\*340
- OR\*3\*347
- GMPL\*2\*26
- GMPL\*2\*27
- GMPL\*2\*28
- GMPL\*2\*31
- GMPL\*2\*35
- GMPL\*2\*38
- GMPL\*2\*39
- LEX\*2\*51
- LEX\*2\*58
- ICD\*18\*6
- GMTS\*2.7\*52
- GMTS\*2.7\*71
- XU\*8\*580
- PSS\*1\*159
- PSO\*7\*257
- PSO\*7\*340
- PSO\*7\*377
- PSO\*7\*390
- PSO\*7\*400
- PSD\*3\*28
- PSD\*3\*67
- PSD\*3\*76
- HDI\*1\*6
- XT\*7.3\*111

# CPRS v29 Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

Table 1 Installation Checklist

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 82%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>No.</th>
<th>Item</th>
<th>Done</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li></li>
</ol></td>
<td><p>Read previously supplied documentation:</p>
<ul>
<li><p>DEA e-Prescribing Setup Installation and Configuration Guide</p></li>
<li><p>CPRS Technical Manual</p></li>
<li><p>CPRS Technical Manual: GUI Version</p></li>
<li><p>CPRS GUI v.29 (Patch# OR*3.0*306) Release Notes</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3">Test/Mirror System Installation</td>
</tr>
<tr class="odd">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td>Confirm that all DEA Preparation is complete, per “DEA e-Prescribing Setup Installation and Configuration Guide” in your Test/Mirror system (See Section 2.2, DEA Preparation, above)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Confirm all Pre-requisite patches have been installed in your Test/Mirror system (see Section 2.3, Pre-requisite Patches, above)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Attend the CPRS v29 Training session for your site’s deployment wave per the <a href="http://vaww.oed.portal.va.gov/projects/CPRS/v29_main/Public/Forms/AllItems.aspx?RootFolder=%2fprojects%2fCPRS%2fv29%5fmain%2fPublic%2fCPRS%20GUI%20v29%20Deployment%20Schedule">CPRS GUI v29 Deployment Schedule</a></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td><p>Download all Additional Required Patches and install in your Test/Mirror system</p>
<ul>
<li><p>HDI_1_11.KID</p></li>
<li><p>PSS_1_166.KID</p></li>
<li><p>CPRSV29PSO_PSD.KID</p></li>
<li><p>OR_GMPL_GMTS_XU_29.KID</p></li>
<li><p>OR_30_371.KID</p></li>
<li><p>PSO_7_426.KID</p></li>
</ul>
<p>(see Table 2 Additional Patches, below)</p></td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Download CPRS GUI installation package OR_30_306.zip (see Section 5.4, CPRS GUI Executable (OR_30_306.zip), below),install per the instructions in that section, and point user shortcuts to your Test/Mirror system</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="7" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Test/Mirror system has been successful</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">Production/Live System Installation</td>
</tr>
<tr class="even">
<td><ol start="8" type="1">
<li></li>
</ol></td>
<td>Confirm that all DEA Preparation is complete, per “DEA e-Prescribing Setup Installation and Configuration Guide” in your Production/Live system (See Section 2.2, DEA Preparation, above)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="9" type="1">
<li></li>
</ol></td>
<td>Confirm all Pre-requisite patches have been installed in your Production/Live system (see Section 2.3, Pre-requisite Patches, above)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="10" type="1">
<li></li>
</ol></td>
<td><p>Install all Additional Required Patches in your Production/Live system</p>
<ul>
<li><p>HDI_1_11.KID</p></li>
<li><p>PSS_1_166.KID</p></li>
<li><p>CPRSV29PSO_PSD.KID</p></li>
<li><p>OR_GMPL_GMTS_XU_29.KID</p></li>
<li><p>OR_30_371.KID</p></li>
<li><p>PSO_7_426.KID</p></li>
</ul>
<p>(see Table 2 Additional Patches, below)</p></td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="11" type="1">
<li></li>
</ol></td>
<td>Install the CPRS v29 GUI package OR_30_306.zip according to the instructions in Section 5.4, CPRS GUI Executable (OR_30_306.zip), below) and point user shortcuts to your Production/Live system</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="12" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Production/Live system has been successful</td>
<td></td>
</tr>
</tbody>
</table>

# Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS GUI version 29 consists of supporting patches from other projects (listed in Table 2 Additional Patches, below), the bundle OR_GMPL_GMTS_XU_29.KID, the patch OR_30_371.KID and the GUI executable along with its supporting installation, help and document files (all listed in Table 3 CPRS v29 files, below)

As part of the phased deployment schedule (see Section 1.4, National Deployment, above), your site will be contacted when and how to download the necessary files from an FTP directory. The necessary files are:

Table 2 Additional Patches

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Additional Required Patches to be downloaded</th>
<th>Supported Functionality</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HDI_1_11.KID</td>
<td>Adds data for the Problem List Domain to the HDIS Domain file (#7115.1). This patch is in preparation for the Problem List patch.</td>
</tr>
<tr class="even">
<td>PSS_1_166.KID</td>
<td>Part of the DEA e-Prescribing of Controlled Substances, as above.</td>
</tr>
<tr class="odd">
<td>CPRSV29PSO_PSD.KID</td>
<td><p>Part of the DEA e-Prescribing of Controlled Substances (CS) using Public Key Infrastructure (PKI) to comply with requirements requested by the Drug Enforcement Agency (DEA)</p>
<p>This bundle contains the following patches:</p>
<p>PSO*7*391</p>
<p>PSD*3*73</p></td>
</tr>
</tbody>
</table>

2.  Although it is anticipated that the patch HDI\*1\*11 (contained in host file HDI_1_11.kid) will be released WITH CPRS GUI v29, there is a possibility that by the time CPRS GUI v29 is released, HDI\*1\*11 may have already have been released, in which case ensure that it has been installed per instructions in the patch description.

Table 3 CPRS v29 files

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>CPRS v29 files to be downloaded</th>
<th>File Contents / Supported Functionality</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR_GMPL_GMTS_XU_29.KID</td>
<td><p>Main CPRS v29 bundle that contains:</p>
<p>OR*3.0*306 (CPRS version 29)</p>
<p>GMPL*2.0*36 (Problem List patch associated with SNOMED-CT changes)</p>
<p>GMTS*2.7*86 (Health Summary updates for Problem List SNOMED-CT changes)</p>
<p>XU*8.0*609 (Kernel patch that supports DEA functionality. Adds the requirement that DEA numbers for prescribers must be accompanied by a DEA expiration date or the DEA number will be treated as invalid)</p></td>
</tr>
<tr class="even">
<td>OR_30_371.KID</td>
<td>Eliminate duplicate entries, turn on auditing for ORDER DEA ARCHIVE INFO and other minor changes</td>
</tr>
<tr class="odd">
<td>PSO*7*426</td>
<td>Supports EPCS functionality</td>
</tr>
<tr class="even">
<td>OR_30_306.zip</td>
<td><p>The zip file containing the CPRS documentation and executable:</p>
<p>CPRSChart.exe</p>
<p>CPRS.msi</p>
<p>CPRS_29.msp</p>
<p>CPRSGUITM.doc</p>
<p>CPRSGUIUM.doc</p>
<p>CPRSLMTM.doc</p>
<p>OR_30_306_IG.doc</p>
<p>OR_30_306_RN.doc</p>
<p>Help files (folder)</p></td>
</tr>
</tbody>
</table>

# Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed in the specified order:

## Additional Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For CPRS to run correctly, it is necessary that some patches be installed immediately prior to the installation of CPRS v29. These will be distributed with CPRS v29 (see Section 0,

Software Retrieval, above), and they should be installed in the order listed below.

### HDI\*1\*11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

This patch can be installed with users on the system with installation

taking less than 10 minutes.

> **NOTE:** Patch HDI\*1.0\*6 and XT\*7.3\*111 are REQUIRED builds for

HDI\*1.0\*11. KIDS will not allow the installation of

this patch without the prior installation of them.

1\. Download HDI\*1\*11.KID into your local directory.

2\. From the Kernel Installation & Distribution System (KIDS) menu, select

the Installation menu.

3\. Select the Load a Distribution and enter the directory that you FTP'd

the host file to and HDI\*1\*11.KID. Example:

USER\$:\[ABC\]HDI\*1\*11.KID

4\. From the Kernel Installation & Distribution System (KIDS) menu, you may

select to use the following options (when prompted for INSTALL NAME,

enter HDI\*1\*11.KID

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. Use the Install Package(s) option and select the package HDI\*1.0\*11.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//', respond NO.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//', respond NO.

8\. Once the patch installation steps have been completed, delete the

routines: HDI1011A.

### PSS\*1\*166

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

Do not install this patch while pharmacy orders are being entered and

signed through CPRS. If this is not possible, then it is recommended to be

installed during non-peak hours. Installation will take no longer than 2

minutes and this patch may be queued.

Suggested time to install: non-peak hours, especially when CPRS users are

off the system.

Pre-Installation Instructions

-----------------------------

1\. Download PSS_1_166.KID into your local directory.

2\. From the Kernel Installation & Distribution System (KIDS) menu, select

the Installation menu.

3\. Select the Load a Distribution and enter the directory that you FTP'd

the host file to and PSS_1_166.KID. Example:

USER\$:\[ABC\]PSS_1_166.KID

4\. From the Kernel Installation & Distribution System (KIDS) menu, you may

select to use the following options (when prompted for INSTALL NAME,

enter PSS\*1.0\*166

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. Use the Install Package(s) option and select the package

PSS\*1.0\*166.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' respond NO.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO// respond NO.

### CPRSV29PSO_PSD.KID (PSO\*7\*391 and PSD\*3\*73)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

Do not install this patch while Outpatient Pharmacy users are on the

system or when Outpatient orders are being entered and signed through

Computerized Patient Record System. Installation will take no longer than

5 minutes.

Pre-Installation Instructions

-----------------------------

1\. Download CPRSV29_PSO_PSD.KID into your local directory.

2\. From the Kernel Installation & Distribution System (KIDS) menu, select

the Installation menu.

3\. Select the Load a Distribution and enter the directory that you FTP’d

the host file to and CPRSV29_PSO_PSD.KID. Example:

USER\$:\[ABC\]CPRSV29_PSO_PSD.KID

4\. From the Kernel Installation & Distribution System (KIDS) menu, you may

select to use the following options (when prompted for INSTALL NAME,

enter PSO_PSD_V29 1.0

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. Use the Install Package(s) option and select the package

PSO_PSD_V29 1.0.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' respond NO.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO// respond NO.

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. Use the Install Package(s) option and select the package

CPRSV29PSO_PSD.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' respond NO.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO// respond NO.

## CPRS v29 Host File (OR_GMPL_GMTS_XU_29.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

This patch should be installed during non-peak hours to minimize disruption. No users should be accessing CPRS during the install as this prevents you from replacing CPRSChart.exe. Installation will take approximately 15 minutes or more, depending on the menu structure at your site.

Listed below are general installation instructions for installing the CPRS GUI v29 KIDS build and other patches. For specific installation details, refer to Appendix B, CPRS v29 M patches—Software Installation Sample, below. Additionally, review the National Patch Module messages for each patch for patch-specific information.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
2.  Use Load a Distribution. You may need to prefix a directory name.
3.  If given the option to run any Environment Check Routine(s), answer "YES."
4.  From this menu, you may then elect to use the following options:
- Backup a Transport Global
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
5.  When ready, select the Install Packages option.
6.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? Yes//", respond "YES."
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond "YES."
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', respond YES. When prompted to select the options you would like to place out of order, enter the following:

OR OE/RR MENU CLINICIAN CPRS Clinician Menu

OR OE/RR MENU NURSE CPRS Nurse Menu

OR OE/RR MENU WARD CLERK CPRS Ward Clerk Menu

OR CPRS GUI CHART

9.  When prompted 'Delay Install (Minutes): (0-60): 0//; respond '0.'

See an example of the host file installation capture Appendix B, CPRS v29 M patches—Software Installation Sample,. below.

## Additional Required Patches (continued)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For CPRS to run correctly, it is necessary that some patches be installed immediately after the installation of CPRS v29. These will be distributed with CPRS v29 (see Section 0,

Software Retrieval, above), and they should be installed in the order listed below.

### OR\*3.0\*371

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

This patch can be installed with users on the system with installation

taking less than 10 minutes.

> **NOTE:** Patch OR\*3.0\*306 is a REQUIRED build for

OR\*3.0\*371. KIDS will not allow the installation of

this patch without the prior installation of them.

1\. Download OR_30_371.KID into your local directory.

2\. From the Kernel Installation & Distribution System (KIDS) menu, select

the Installation menu.

3\. Select the Load a Distribution and enter the directory that you FTP'd

the host file to and OR_30_371.KID. Example:

USER\$:\[ABC\]OR_30_371.KID

4\. From the Kernel Installation & Distribution System (KIDS) menu, you may

select to use the following options (when prompted for INSTALL NAME,

enter OR\*3.0\*371

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. Use the Install Package(s) option and select the package

OR\*3.0\*371.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' respond NO.

### PSO\*7\*426

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

Do not install this patch when Outpatient orders (Controlled

Substances) are being entered and signed through Computerized Patient

Record System. Installation will take no longer than 2 minutes.

Pre-Installation Instructions

-----------------------------

1\. Download PSO_7_426.KID into your local directory.

2\. From the Kernel Installation & Distribution System (KIDS) menu, select

the Installation menu.

3\. Select the Load a Distribution and enter the directory that you FTP'd

the host file to and PSO_7_426.KID. Example:

USER\$:\[ABC\]PSO_7_426.KID

4\. From the Kernel Installation & Distribution System (KIDS) menu, you may

select to use the following options (when prompted for INSTALL NAME,

enter PSO\*7.0\*426

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

5\. Use the Install Package(s) option and select the package

PSO\*7.0\*426.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' respond NO.

## CPRS GUI Executable (OR_30_306.zip)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Basic CPRS GUI Installation Guide (for advanced installation troubleshooting see Appendix A, CPRS GUI Installation Troubleshooting Guide, below)

### Changes to the Installation Procedure for the CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to file writing permissions introduced by the Windows 7 operating system, the previous automated method for updating CPRSChart is no longer available. Installation into the Program Files directories now requires administrator rights, which are not available to the standard user. Digital certificates can be used in place of administrator rights for installations, so a change was made to the installation model for CPRS. The methods outlined below are also valid for those still using the Windows XP operating system

### Methods of installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some changes to the usual methods of installation of CPRS are necessary due to the roll-out of Windows 7 as a desktop Operating System. In the past, sites have used primarily four methods to distribute the application

- Network (shared) installation:  
  Where the executable is placed on a network drive, with a shortcut on users’ desktops. The executable is replaced when no users are accessing the GUI program.  
  There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Citrix installation:  
  Where the executable is run on a remote workstation and the user views the screen remotely.  
  There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Gold Path installation:

> where the new executable is placed in a common shared location (called a gold path), and updated when the CPRS GUI is first accessed from the local workstation.  
> This method is handled though desktop enterprise services. For more detail please refer to section 5.4.5, Automation Capabilities, below.

- Manual install:

  which is used primarily for advanced users and at testing locations.  
  This method is somewhat changed from that used previously for Windows XP workstations. For more detail please refer to section 5.4.6, Manual Installation, below.

### Overview of the new process: Loader in front of CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For most types of installation, no changes are needed, since those performing the install will have administrator rights. For gold path installations, some changes are necessary:

First, a Microsoft Installer file (msi) will be run on the workstation by either a SCCM push or by a local administrator. This will install the CPRSLoader application, which is an upgraded CPRSUpdater. The loader needs to be installed with Vista server information (vista server fully qualified domain name (FDQN) and remote procedure call (RPC) port number) as well as the location of the gold directory.

Once that is completed, end users will have a normal CPRS icon placed on their workstation, which will run the loader prior to starting up CPRSChart. The loader checks the gold directory for new updates, installs any necessary updates (msp files), then starts up CPRSChart.

1.  Previous gold path process

![](or-3-306-installation-guide-cprs-gui-29/002.png)

2.  Updated gold path process

![](or-3-306-installation-guide-cprs-gui-29/003.png)

### Changes for the End User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no visible changes in the end-user process; except possibly the icon name. Users might notice a delay when the installer file is run for the first time, as it takes some time to run and installs shortcuts on the workstation. Later patches will have negligible impact and only delay the startup of the CPRS GUI briefly.

### Automation Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation can be automated. This is accomplished by a combination of SCCM, MSI, and CPRSLoader settings. This is the preferred method for installing on a local workstation. To set up the automation, a site must determine which server name, port, and gold directory location they are using.

- The server name is either the DNS name of the server Vista resides on (e.g. \\vista.server.va.gov), or its IP address (e.g. 10.1.2.34, etc.). Of the two, the use of a DNS name is preferred—for load balancing purposes.
- The port is the port the RPC Broker listens on for the particular instance of Vista (e.g. 5528).
- The gold directory is the location where any files that will automatically update CPRS will be placed (e.g. \\server.va.gov\CPRSGold)

To begin the process, a site manager submits a packaging request or contacts the regional Enterprise Services office. The Enterprise Services office will ask for the server name, port, and gold directory, as well as an installation date. This process may take some time so it is strongly advised that, if this method is to be used, it be started immediately upon availability of the software . Once the initial files are pushed to the workstations, the rest of the automation consists of copying the appropriate patch file into the gold directory. Alternatively, another SCCM push could also do that step, to avoid large numbers of users accessing the gold directory concurrently.

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Things that should be done beforehand:

1.  Set up a gold directory for the site that CPRS users can read files from.
2.  Determine the DNS server name or IP address for the appropriate VistA server.
3.  Determine the Broker RPC port for the VistA account.
4.  Acquire the CPRS.msi file, and the latest CPRS_29.msp patch file, if any.

#### To install manually on a workstation, follow these steps:

1.  Double click on the CPRS.msi file.
10. A Welcome screen shows—Click on the next button.  
    ![](or-3-306-installation-guide-cprs-gui-29/004.png)
11. A Destination Folder dialog shows.  
    ![](or-3-306-installation-guide-cprs-gui-29/005.png)  
    If the installation destination shouldn't be the default, change it by clicking on the Change button, which shows the Change destination dialog.  
    ![](or-3-306-installation-guide-cprs-gui-29/006.png)  
    Find the desired directory and click OK, or Cancel to go back to the default directory.
12. A VistA Connection dialog shows.  
    ![](or-3-306-installation-guide-cprs-gui-29/007.png)  
    For users that have more than one VistA account to access with the GUI, select the “Use Multiple VistA connections…” radio button. This will disable the VistA Server Name and VistA RPC Broker Port prompts—the user will be prompted for this information at runtime (only if the workstation has the VistA servers and Port numbers in the registry). For a single VistA connection, select the first radio button, “Use one VistA connection…” and enter the VistA Server Name (either the fully qualified domain name or the IP address) and VistA RPC Broker Port number at the prompts supplied.  
    Click on Next.
13. An Automatic Update dialog shows.  
    ![](or-3-306-installation-guide-cprs-gui-29/008.png)  
    If manual-only updates are preferred, choose the radio button “Do not use CPRS Loader…” which means updating the CPRSChart executable, as well as supporting files, will need to be done in another manner. For a normal desktop installation, leave this setting at the recommended “Use the CPRS Loader…”  
    If necessary, change the default gold directory by selecting the Change button, selecting the appropriate directory from the Change directory dialog and clicking OK.  
    Click on Next once the path to the gold directory is correct.
14. The Shortcut Choices dialog shows.  
    ![](or-3-306-installation-guide-cprs-gui-29/009.png)  
    Choose where the icons should appear using one of the three radio buttons.  
    Click on Next.
15. The Ready To Install dialog shows.  
    ![](or-3-306-installation-guide-cprs-gui-29/010.png)  
    Click on the Install button and wait for the installer.
16. A dialog with a status bar will appear and show the progress of the installation  
    ![](or-3-306-installation-guide-cprs-gui-29/011.png)  
    then an installation complete dialog shows. ![](or-3-306-installation-guide-cprs-gui-29/012.png)  
    Click Finish to exit the installer.
17. To install any patches found in the gold directory at this point, click on the CPRS shortcut icon and the CPRS Loader will look for the latest patch and install it. The patch may be clicked on directly, but this may cause the server and port information to disappear from the shortcut at times due to a Windows Installer bug, so it is recommended to use the Loader to install the patches.

## CPRS Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Place the User Guide and Technical Manual files in a location that can be accessed by CPRS users.

The following documents are provided, as part of the CPRS v29 installation package, in the zip file “OR_30_306.zip” (see Table 3 CPRS v29 files, above). Please place these files in a location that can be accessed by CPRS users.

Table 4 CPRS v29 documentation

| OR_30_306_IG.doc | This document (CPRS GUI v29 Installation Guide)                                               |
|------------------|-----------------------------------------------------------------------------------------------|
| CPRSGUIUM.doc    | CPRS User Guide: GUI Version                                                                  |
| CPRSLMTM.doc     | CPRS List Manager Technical Manual (covers the non-GUI part of CPRS)                          |
| CPRSGUITM.doc    | CPRS Technical Manual: GUI Version (partner to CPRSLMTM, above, covering the GUI application) |
| OR_30_306_RN.doc | Patch Release Notes for OR\*3\*306                                                            |

## Post-installation Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After CPRS v29 is installed into production, do the following:

- Review the new or changed Parameters exported with CPRS GUI v29 (see listing below). You will need to set the values for all new parameters.

# Parameters Introduced/Changed with CPRS GUI v29

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ORQQPL SUPPRESS CODES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this parameter is to hide the SNOMED and ICD-9-CM codes from displaying in CPRS when defining a problem. If the CPRS coordinator selects YES, the codes will not display when searching for a term.

## OR DEA PIV LINK MSG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR DEA PIV LINK MSG: This parameter enables sites to customize the text that displays on a dialog when the user is not allowed to place orders for controlled substances, but they believe that they should be allowed. The site can put text into this parameter to display to the user.

## ORCDGMRC EARLIEST DATE DEFAULT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the request of test sites, this parameter was created to enable sites to set a default date for the “Earliest Available Date” field in the consult request dialog. The default can be left blank to force the provider to answer, set to today, or set as a future relative amount of time (T+30). When OR\*3.0\*306 is installed, a post installation routine will set the default to TODAY. Sites can delete the value or set a new one using XPAR MENU TOOLS.

3.  The post install routine does NOT change the default Earliest Available Date value in quick orders. It does check which quick orders have a value defined and sends a list of those quick orders to the person who installs patch OR\*3.0\*306. The installer must then forward the MailMan message to the person who can check the Earliest Available Date value in the quick order and delete the value defined there to make it use what is in the ORCDGMRC EARLIEST DATE DEFAULT parameter, leave the value as defined in the quick order, or change the value in the quick order.

# # ## CPRS GUI Installation Troubleshooting Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Interface: Visual GUI and Switches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two Graphical User Interfaces (GUIs) used during this process. The first one is the MSI GUI, which is detailed in section <span class="mark"></span>5.4.6.2, To install manually on a workstation, follow these steps, above and the CPRSLoader GUI, which shouldn't be seen by an end user during normal operation. With the switches available, it doesn't need to be seen at all.

The switches are as follows:

SHOW Shows the loader's GUI. The GUI is invisible if this switch isn't used.

GOLD=*filename* Changes the gold directory for the auto-update feature.

SetCPRS=*filename* Changes the location the loader looks for the current CPRSChart.

SetServer=*servername* Changes the DNS server name for the VistA server CPRSChart uses.

SetPort=*portnumber* Changes the broker port for the VistA account CPRSChart uses.

FORCE Forces the installer to run the latest patch file.

LOGLOAD Creates a log file named CPRSLoader.log in the user’s document directory.

The main screen looks like this:  
![](or-3-306-installation-guide-cprs-gui-29/013.png)

It shows information on the current CPRS setup, and provides some buttons and menu items for operating the loader. Upon start up, the loader checks version information for the latest patch, as well as for the CPRSChart.exe and will display the results.

Latest Patch Version Number: This displays the latest patch version number located in the gold directory. It is blank when a valid patch isn't found. Patch names must be prefixed with “CPRS”, be built for CPRS, and have a filename extension of “.msp”.

Installed CPRS Chart Version: This displays the latest file version of the copy of CPRSChart.exe located in the install directory. It is blank when CPRSChart.exe is missing.

Server: This is the default DNS name passed by CPRSLoader to CPRS when it starts CPRSChart. It can be changed in the edit box. The Save Configuration button must be used to save the value for subsequent uses.

Port: This is the default RPC Broker port the loader passes to CPRS when it starts CPRSChart. It can be changed in the edit box. The Save Configuration button must be used to save the value for subsequent uses. Entry is limited to numeric values only.

Gold Path: This is the location where the loader looks for patch files. It can be edited in either the edit box, or by using the ellipsis button following the edit box, then choosing a directory from the popup dialog. The Save Configuration button must be used to save the value for subsequent uses.

Installed CPRS: This is the location of CPRSChart.exe, which is called by the loader. It can be edited in either the edit box, or by using the ellipsis button following the edit box, then choosing a directory from the popup dialog. The Save Configuration button must be used to save the value for subsequent uses.

Log Memo: The memo box at the bottom is used for the loader log function, and displays a status while the application is running.

Check File Versions: This button tells the loader to re-check the version information—useful if the gold path or install location has been manually changed.

Save Configuration: This button tells the loader to save the configuration information entered into the visual controls to the computers registry files.

Run Installer: This button tells the loader to run the latest patch file.

Run CPRS: This button tells the loader to run CPRS with the values shown.

Exit: Leaves the loader application.

Actions Menu: The items in the actions menu perform the same actions as the buttons with the corresponding labels.

Help Menu: Shows the switches the loader may use.

> ![](or-3-306-installation-guide-cprs-gui-29/014.png)

Exit Menu: Leave the loader application.

### Uninstallation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The uninstaller can be run from the Programs and Features list in the Control Panel or it can be run by clicking on the msi installer file. Choose the Remove option to remove both CPRSLoader and CPRSChart from the install directory.

> **WARNING:** This will remove them from the Programs and Features list as well. If VA CPRS v28 was installed on the workstation, the older CPRSChart from v28 will not be restored, but a repair installation of the VA CPRS item may restore it. If VA CPRS is uninstalled, it will delete the latest patch applied to the workstation, but running the loader again will reinstall it.

The uninstaller can be run from the Programs and Features list in the Control Panel or it can be run by clicking on the msi installer file. Caution should be used when uninstalling—there are some idiosyncrasies due to changes in the methods used to address Windows 7 installation requirements, namely:

- Under “Control Panel” -\> “Programs and Features” there may be two separate instances of CPRS represented after CPRS v29 has been installed. If so, they will appear as:
  - “VA CPRS” (this is version 28)
  - “CPRS” (this is version 29)
- Uninstalling EITHER of these versions will remove CPRSChart.exe from the local workstation’s Program Files folder
- Do not uninstall v28 unless the installation of v29 is going to immediately follow.
- It is not actually necessary to uninstall v28 (the “VA CPRS” entry in Control Panel Programs and Features) since the GUI executable (CPRSChart.exe) will be replaced. However the old v28 (“VA CPRS”) may remain in the Control Panel Programs and Features.
- If you do uninstall v28 (VA CPRS) AFTER v29 has been installed, then the v29 version of CPRSChart.exe will be removed—simply running the v29 CPRS shortcut (see A3, Dual Shortcuts, below) should reinstall the patch –(seek IT support if that doesn’t work )

### Dual Shortcuts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Dual CPRS shortcuts may appear on the desktop. This is due to the new installer creating a shortcut to run CPRSLoader instead of the previous method of directly running CPRSChart. This may have different effects, depending on the workstation’s installation. If this does happen, the simplest fix is for the user to delete the old shortcut and start using the new one.

To identify which shortcut is the correct one (if the version number is not in the name), use these steps:

1.  Right-click the shortcut icon.
2.  Select Properties.
3.  Select the Shortcut tab.
4.  Look at the contents of the “Target” text box (you may have to put your cursor in the box and scroll to the right to be able to see the end of the string) and see if it ends with CPRSChart.exe (v28) or CPRS Loader.exe (v29).
5.  The shortcut going directly to CPRSChart.exe is the one to remove.

If it is a Windows XP workstation, both shortcuts will check for updates and start CPRSChart normally; the old shortcut will use the CPRSUpdater, and the new shortcut will use CPRSLoader. They have the same effect on an XP workstation.

If it is a Windows 7 workstation, both shortcuts will run v28, until v29 is installed. At that time, the old shortcut will cause CPRSChart.exe to fail, due to a missing switch, and wouldn't be able to update. The new shortcut will work properly. Ideally, desktop support may be able to arrange a way to automatically delete the old v28 shortcut.

#### CPRS Not Starting

If the user has trouble starting CPRS after the v29 upgrade, it may be simply they are clicking on a faulty shortcut, as described above.

### Windows XP Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Windows XP does not always install on the first try. If it fails, a manual install usually fixes the problem. The previous updating method (see Figure 1, Previous gold path process, above) will work on an XP workstation.

### Self-Repair

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If CPRSLoader detects the CPRSChart executable has been renamed or deleted, CPRSLoader will try to reinstall CPRSChart.exe from the latest patch. This is to help with the problem of uninstalling VA CPRS v28 after v29 has been installed (see A2, Uninstallation, above)

### Version numbers—Loader versus CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The version number of CPRSLoader.exe is different from that of CPRSChart.exe. When the Loader is first installed, Windows Installer shows its version number (1.29.4 at time of writing). Once the loader is run, the installer will show the version of CPRS that is in the default directory (most likely 1.28.24—the released version of CPRS 28). Once the 29 patch installs, or someone copies CPRSChart v29 to the workstation and runs the loader, the windows installer will show the released version number for CPRSChart.exe (1.29.21 at time of writing)

### Batch File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A batch file can be used to install either the loader or the patch. The command is:

> msiexec /i CPRS.msi DB_CONNECTIONS=One VISTA_DNS_NAME=dnsname VISTA_RPC_BROKER_PORT=brokerport INSTALLCPRSLOADER=Yes GOLD_PATH=golddirectory SHORTCUT_LOCATION=StartMenuAndDesktop /qn

This will install the loader application silently, if the local values for dnsname, brokerport and golddirectory are filled in properly.

The command for a patch file is similar:

> msiexec /p golddirectory\CPRS_29.msp VISTA_DNS_NAME=dnsname VISTA_RPC_BROKER_PORT=brokerport GOLD_PATH=golddirectory /qn

For both commands, dnsname is the DNS name for the vista server, brokerport is the rpc broker port, and golddirectory is the location of the Gold directory containing the patch updates.

### DLL Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Even though some dlls were included in the initial install, the CPRS installation system is not intended to replace the distribution methods or systems of other applications.

### Delay Updating from MSP File during Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There may be a delay in the user’s workstation detecting the presence of a new msp file. If during an installation the loader doesn't seem to pick up the msp file, it may be necessary to wait for the network to refresh its directory information cache on the user’s workstation. The wait time is workstation and network dependent.

### Do Not Modify the MSI and MSP Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DO NOT MODIFY THE MSI OR MSP FILES. Modifying the msi or msp file will make it so that CPRS will not install. The distributed msi file contains a digital certificate necessary for future installations and modifying the file will remove the certificate. The msp file is comprised of a series of change instructions based on a specific msi file. If the msi is changed in any way, the msp cannot run. A similar problem occurs when the msp file is modified. It is very important that neither of these files are altered.

## CPRS v29 M patches—Software Installation Sample

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HDI\*1\*11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<I1029\> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: HDI\*1.0\*11 4/8/13@16:59:23

=\> HDI 1.0 11 ;Created on Mar 28, 2013@17:55:35

This Distribution was loaded on Apr 08, 2013@16:59:23 with header of

HDI 1.0 11 ;Created on Mar 28, 2013@17:55:35

It consisted of the following Install(s):

HDI\*1.0\*11

Checking Install for Package HDI\*1.0\*11

Install Questions for HDI\*1.0\*11

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'HDIS ERRORS': LABTECH,FORTYEIGHT//

JT

Enter the Coordinator for Mail Group 'HDIS ERT NOTIFICATION': LABTECH,FORTYEIGHT

// JT

Enter the Coordinator for Mail Group 'HDIS HDR NOTIFICATION': LABTECH,FORTYEIGHT

// JT

Enter the Coordinator for Mail Group 'HDIS LAB EXCEPTIONS': PROGRAMMER,ONE//

1 PROGRAMMER,ONE P1 COMPUTER SPECIALIST

2 PROGRAMMER,ONEHUNDRED P100 COMPUTER SPECIALIST

3 PROGRAMMER,ONEHUNDREDEIGHT P108 COMPUTER SPECIALI

ST

4 PROGRAMMER,ONEHUNDREDEIGHTEEN P118 COMPUTER SPECI

ALIST

5 PROGRAMMER,ONEHUNDREDEIGHTY P180 COMPUTER SPECIAL

IST

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 PROGRAMMER,ONE P1 COMPUTER SPECIALIST

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;9999 TELNET PORT

--------------------------------------------------------------------------------

Install Started for HDI\*1.0\*11 :

Apr 08, 2013@17:06:17

Build Distribution Date: Mar 28, 2013

Installing Routines:

Apr 08, 2013@17:06:17

Installing PACKAGE COMPONENTS:

Installing BULLETIN

Installing MAIL GROUP

Apr 08, 2013@17:06:17

Running Post-Install Routine: POST^HDI1011A

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~~

Post-Installation (POST^HDI1011A) will now be run

Adding PROBLEM LIST Domain and related fields to

HDIS DOMAIN file (#7115.1)

Post-Installation ran to completion

\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~~

Updating Routine file...

Updating KIDS files...

HDI\*1.0\*11 Installed.

Apr 08, 2013@17:06:17

Not a production UCI

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

### PSS\*1\*166

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<I1029\> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: pss\*1.0\*166 4/8/13@17:07:42

=\> PSS\*1\*166 ;Created on Apr 03, 2013@11:57:31

This Distribution was loaded on Apr 08, 2013@17:07:42 with header of

PSS\*1\*166 ;Created on Apr 03, 2013@11:57:31

It consisted of the following Install(s):

PSS\*1.0\*166

Checking Install for Package PSS\*1.0\*166

Install Questions for PSS\*1.0\*166

Want KIDS to INHIBIT LOGONs during the install? NO// n NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// n NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;9999 TELNET PORT

--------------------------------------------------------------------------------

Install Started for PSS\*1.0\*166 :

Apr 08, 2013@17:12:18

Build Distribution Date: Apr 03, 2013

Installing Routines:

Apr 08, 2013@17:12:18

Updating Routine file...

Updating KIDS files...

PSS\*1.0\*166 Installed.

Apr 08, 2013@17:12:18

Not a production UCI

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

### CPRSV29PSO_PSD.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<I1029\> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: pso_PSD_V29 1.0 4/8/13@17:14:02

=\> PSD\*3\*73 ;Created on Mar 29, 2013@18:33:13

This Distribution was loaded on Apr 08, 2013@17:14:02 with header of

PSD\*3\*73 ;Created on Mar 29, 2013@18:33:13

It consisted of the following Install(s):

PSO_PSD_V29 1.0 PSD\*3.0\*73 PSO\*7.0\*391

Checking Install for Package PSO_PSD_V29 1.0

Install Questions for PSO_PSD_V29 1.0

Checking Install for Package PSD\*3.0\*73

Install Questions for PSD\*3.0\*73

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// n NO

Checking Install for Package PSO\*7.0\*391

Install Questions for PSO\*7.0\*391

Incoming Files:

52 PRESCRIPTION (Partial Definition)

> **NOTE:** You already have the 'PRESCRIPTION' File.

52.41 PENDING OUTPATIENT ORDERS (Partial Definition)

> **NOTE:** You already have the 'PENDING OUTPATIENT ORDERS' File.

Want KIDS to INHIBIT LOGONs during the install? NO// n NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// n NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999999 TELNET PORT

--------------------------------------------------------------------------------

Install Started for PSO_PSD_V29 1.0 :

Apr 08, 2013@17:18:34

Build Distribution Date: Mar 29, 2013

Installing Routines:

Apr 08, 2013@17:18:34

Install Started for PSD\*3.0\*73 :

Apr 08, 2013@17:18:34

Build Distribution Date: Mar 29, 2013

Installing Routines:

Apr 08, 2013@17:18:34

Installing PACKAGE COMPONENTS:

Installing OPTION

Apr 08, 2013@17:18:34

Updating Routine file...

Updating KIDS files...

PSD\*3.0\*73 Installed.

Apr 08, 2013@17:18:34

Not a production UCI

NO Install Message sent

Install Started for PSO\*7.0\*391 :

Apr 08, 2013@17:18:34

Build Distribution Date: Mar 29, 2013

Installing Routines:

Apr 08, 2013@17:18:34

Installing Data Dictionaries: .

Apr 08, 2013@17:18:34

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Apr 08, 2013@17:18:34

Updating Routine file...

The following Routines were created during this install:

PSOXZA

PSOXZA1

PSOXZA10

PSOXZA11

PSOXZA12

PSOXZA13

PSOXZA14

PSOXZA2

PSOXZA3

PSOXZA4

PSOXZA5

PSOXZA6

PSOXZA7

PSOXZA8

PSOXZA9

Updating KIDS files...

PSO\*7.0\*391 Installed.

Apr 08, 2013@17:18:34

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

PSO_PSD_V29 1.0 Installed.

Apr 08, 2013@17:18:34

No link to PACKAGE file

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

### OR_GMPL_GMTS_XU_29.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<I1029\> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: OR GMPL GMTS XU 29 1.0 4/8/13@17:21:52

=\> CPRS29V21 AND REQUIRED PATCHES ;Created on Feb 19, 2013@12:06:32

This Distribution was loaded on Apr 08, 2013@17:21:52 with header of

CPRS29V21 AND REQUIRED PATCHES ;Created on Feb 19, 2013@12:06:32

It consisted of the following Install(s):

OR GMPL GMTS XU 29 1.0 GMPL\*2.0\*36 GMTS\*2.7\*86 OR\*3.0\*306

XU\*8.0\*609

Checking Install for Package OR GMPL GMTS XU 29 1.0

Install Questions for OR GMPL GMTS XU 29 1.0

Checking Install for Package GMPL\*2.0\*36

Install Questions for GMPL\*2.0\*36

Incoming Files:

125.12 PROBLEM SELECTION CATEGORY CONTENTS (Partial Definition)

> **NOTE:** You already have the 'PROBLEM SELECTION CATEGORY CONTENTS' File.

125.99 PROBLEM LIST SITE PARAMETERS (Partial Definition)

> **NOTE:** You already have the 'PROBLEM LIST SITE PARAMETERS' File.

9000011 PROBLEM

> **NOTE:** You already have the 'PROBLEM' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// n NO

Checking Install for Package GMTS\*2.7\*86

Install Questions for GMTS\*2.7\*86

Checking Install for Package OR\*3.0\*306

Install Questions for OR\*3.0\*306

Incoming Files:

100.9 OE/RR NOTIFICATIONS (including data)

> **NOTE:** You already have the 'OE/RR NOTIFICATIONS' File.

I will OVERWRITE your data with mine.

101.41 ORDER DIALOG (including data)

> **NOTE:** You already have the 'ORDER DIALOG' File.

I will REPLACE your data with mine.

101.52 ORDER DEA ARCHIVE INFO

Incoming Mail Groups:

Enter the Coordinator for Mail Group 'OR CACS': PROGRAMMER,ONE//

1 PROGRAMMER,ONE P1 COMPUTER SPECIALIST

2 PROGRAMMER,ONEHUNDRED P100 COMPUTER SPECIALIST

3 PROGRAMMER,ONEHUNDREDEIGHT P108 COMPUTER SPECIALI

ST

4 PROGRAMMER,ONEHUNDREDEIGHTEEN P118 COMPUTER SPECI

ALIST

5 PROGRAMMER,ONEHUNDREDEIGHTY P180 COMPUTER SPECIAL

IST

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 PROGRAMMER,ONE P1 COMPUTER SPECIALIST

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package XU\*8.0\*609

Install Questions for XU\*8.0\*609

Want KIDS to INHIBIT LOGONs during the install? NO// y YES

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// y YES

Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU CLINICIAN

CPRS Clinician Menu

Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU NURSE CPRS

Nurse Menu

Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU WARD CLERK

CPRS Ward Clerk Menu

Enter options you wish to mark as 'Out Of Order': OR CPRS GUI CHART CPRSCh

art version 1.0.28.24

Enter options you wish to mark as 'Out Of Order':

Enter protocols you wish to mark as 'Out Of Order':

Delay Install (Minutes): (0-60): 0//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999999 TELNET PORT

--------------------------------------------------------------------------------

Install Started for OR GMPL GMTS XU 29 1.0 :

Apr 08, 2013@17:30:19

Build Distribution Date: Feb 19, 2013

Installing Routines:

Apr 08, 2013@17:30:19

Install Started for GMPL\*2.0\*36 :

Apr 08, 2013@17:30:19

Build Distribution Date: Feb 19, 2013

Installing Routines:

Apr 08, 2013@17:30:19

Installing Data Dictionaries:

Apr 08, 2013@17:30:19

Installing PACKAGE COMPONENTS:

Installing BULLETIN

Installing PROTOCOL

Located in the GMPL (PROBLEM LIST) namespace.

Installing OPTION

Apr 08, 2013@17:30:19

Running Post-Install Routine: POST^GMPLY36

Updating Routine file...

Updating KIDS files...

GMPL\*2.0\*36 Installed.

Apr 08, 2013@17:30:19

Not a production UCI

NO Install Message sent

Install Started for GMTS\*2.7\*86 :

Apr 08, 2013@17:30:19

Build Distribution Date: Feb 19, 2013

Installing Routines:

Apr 08, 2013@17:30:19

Updating Routine file...

Updating KIDS files...

GMTS\*2.7\*86 Installed.

Apr 08, 2013@17:30:19

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*306 :

Apr 08, 2013@17:30:20

Build Distribution Date: Feb 19, 2013

Installing Routines:

Apr 08, 2013@17:30:20

Running Pre-Install Routine: PRE^ORY306

Installing Data Dictionaries:

Apr 08, 2013@17:30:20

Installing Data: .......

Apr 08, 2013@17:30:21

Installing PACKAGE COMPONENTS:

Installing BULLETIN

Installing SECURITY KEY

Installing MAIL GROUP

Installing REMOTE PROCEDURE

Installing OPTION

Installing PARAMETER DEFINITION

Apr 08, 2013@17:30:21

Running Post-Install Routine: POST^ORY306

Attaching Mail Groups to OR PROBLEM NTRT BULLETIN

... G.OR CACS attached to OR PROBLEM NTRT BULLETIN Bulletin

Finding all consult/procedure quick orders with a default value in the EARLIEST

APPROPRIATE DATE field

A MailMan containing the list of quick orders will be sent to the installer

...SORRY, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

Message \#67002 has been sent

Attempting to remove values for parameter OR USE MH DLL...

Delete successful

Attempting to remove parameter OR USE MH DLL from PARAMETER DEFINITION file

Delete successful

Attempting to remove ORQQPXRM MHDLLDMS from REMOTE PROCEDURE file

Delete successful

Setting parameter ORCDGMRC EARLIEST DATE DEFAULT to TODAY

Error setting parameter:

Queue Monthly CS Report by Provider... (MAY 01, 2013@21:00)

'OR EPCS CS RX BY PROVIDER' scheduled for MAY 01, 2013@21:00

Continuing...

.

Order Check Expert System Rule Transporter

Created: MAR 13,2012 at 13:09 at CPRS29.FO-SLC.MED.VA.GOV

Current Date: APR 8,2013 at 17:30 at I1029.FO-ALBANY.MED.VA.GOV

Loading Data . . . . . . .

Installing '863.8 OCX MDD PARAMETER' records... . . . . . . . . . .

. . . . . . . . . . . .

Installing '864.1 OCX MDD DATATYPE' records... . . .

Installing '863.7 OCX MDD PUBLIC FUNCTION' records... . . .

Installing '863.9 OCX MDD CONDITION/FUNCTION' records... . . .

Installing '863.4 OCX MDD ATTRIBUTE' records... . . .

OCX MDD ATTRIBUTE: HL7 CONTROL REASON record missing...

NAME: HL7 CONTROL REASON ...Correct data Filed

PARAMETER NAME: DATA TYPE ...Correct data Filed

VALUE: FREE TEXT ...Correct data Filed . . .

Installing '863.2 OCX MDD SUBJECT' records... .

Installing '863.3 OCX MDD LINK' records... . .

OCX MDD LINK: PATIENT.HL7_CONTROL_REASON record missing...

NAME: PATIENT.HL7_CONTROL_REASON ...Correct data Filed

PARENT SUBJECT: PATIENT ...Correct data Filed

PARENT MENU GROUP: HL7 ...Correct data Filed

ATTRIBUTE: HL7 CONTROL REASON ...Correct data Filed

PARAMETER NAME: OCXO VARIABLE NAME ...Correct data Filed

VALUE: OCXODATA("ORC",16) ...Correct data Filed

PARAMETER NAME: OCXO UP-ARROW PIECE NUMBER ...Correct data Filed

VALUE: 5 ...Correct data Filed . . . . .

Installing '860.9 ORDER CHECK NATIONAL TERM' records... . . . . . .

. . . . . . . . .

Installing '860.8 ORDER CHECK COMPILER FUNCTIONS' records... . . . .

. . . . . . . .

Installing '860.6 ORDER CHECK DATA CONTEXT' records... . . . .

Installing '860.5 ORDER CHECK DATA SOURCE' records... . . . . .

Installing '860.4 ORDER CHECK DATA FIELD' records... . .

ORDER CHECK DATA FIELD: CONTROL REASON record missing...

NAME: CONTROL REASON ...Correct data Filed

DATATYPE: FREE TEXT ...Correct data Filed

DATA CONTEXT: GENERIC HL7 MESSAGE ARRAY ...Correct data Filed

DATA SOURCE: HL7 COMMON ORDER SEGMENT ...Correct data Filed

META DICTIONARY LINK: PATIENT.HL7_CONTROL_REASON ...Correct data Filed

. .

Installing '860.3 ORDER CHECK ELEMENT' records... .

ORDER CHECK ELEMENT: HL7 DEA CERT REVOKED record missing...

NAME: HL7 DEA CERT REVOKED ...Correct data Filed

ELEMENT CONTEXT: GENERIC HL7 MESSAGE ARRAY ...Correct data Filed

EXPRESSION SEQUENCE NUMBER: 1 ...Correct data Filed

DATA FIELD 1: FILLER ...Correct data Filed

OPERATOR/FUNCTION: EQ FREE TEXT ...Correct data Filed

CONDITIONAL VALUE 1: PS ...Correct data Filed

EXPRESSION SEQUENCE NUMBER: 2 ...Correct data Filed

DATA FIELD 1: CONTROL REASON ...Correct data Filed

OPERATOR/FUNCTION: CONTAINS ...Correct data Filed

CONDITIONAL VALUE 1: 17 ...Correct data Filed .

ORDER CHECK ELEMENT: HL7 PHARMACY DCED ORDER record missing...

NAME: HL7 PHARMACY DCED ORDER ...Correct data Filed

ELEMENT CONTEXT: GENERIC HL7 MESSAGE ARRAY ...Correct data Filed

EXPRESSION SEQUENCE NUMBER: 1 ...Correct data Filed

DATA FIELD 1: FILLER ...Correct data Filed

OPERATOR/FUNCTION: EQ FREE TEXT ...Correct data Filed

CONDITIONAL VALUE 1: PS ...Correct data Filed

EXPRESSION SEQUENCE NUMBER: 2 ...Correct data Filed

DATA FIELD 1: CONTROL CODE ...Correct data Filed

OPERATOR/FUNCTION: EQUALS ELEMENT IN SET ...Correct data Filed

CONDITIONAL VALUE 1: OC,OD ...Correct data Filed .

ORDER CHECK ELEMENT: HL7 PHARMACY HASH MISMATCH record missing...

NAME: HL7 PHARMACY HASH MISMATCH ...Correct data Filed

ELEMENT CONTEXT: GENERIC HL7 MESSAGE ARRAY ...Correct data Filed

EXPRESSION SEQUENCE NUMBER: 1 ...Correct data Filed

DATA FIELD 1: FILLER ...Correct data Filed

OPERATOR/FUNCTION: EQ FREE TEXT ...Correct data Filed

CONDITIONAL VALUE 1: PS ...Correct data Filed

EXPRESSION SEQUENCE NUMBER: 2 ...Correct data Filed

DATA FIELD 1: CONTROL REASON ...Correct data Filed

OPERATOR/FUNCTION: CONTAINS ...Correct data Filed

CONDITIONAL VALUE 1: 16 ...Correct data Filed

Installing '860.2 ORDER CHECK RULE' records... .

ORDER CHECK RULE: AUTO DCED CONTROLLED SUBSTANCE ORDERS record missing...

NAME: AUTO DCED CONTROLLED SUBSTANCE ORDERS ...Correct data Filed

LABEL: PHARM DCED ...Correct data Filed

TYPE: SIMPLE DEFINITION ...Correct data Filed

ELEMENT NAME: HL7 PHARMACY DCED ORDER ...Correct data Filed

LABEL: PHARM HASH MISMATCH ...Correct data Filed

TYPE: SIMPLE DEFINITION ...Correct data Filed

ELEMENT NAME: HL7 PHARMACY HASH MISMATCH ...Correct data Filed

LABEL: DEA CERT REVOKED ...Correct data Filed

TYPE: SIMPLE DEFINITION ...Correct data Filed

ELEMENT NAME: HL7 DEA CERT REVOKED ...Correct data Filed

RELATION INDEX: 1 ...Correct data Filed

RELATION EXPRESSION: PHARM DCED AND PHARM HASH MISMATCH ...Correct datad

NOTIFICATION: DEA AUTO DC CS MED ORDER ...Correct data Filed

NOTIFICATION MESSAGE: Med order(s) DCed. Resubmit or contact Pharmacy. d

RELATION INDEX: 2 ...Correct data Filed

RELATION EXPRESSION: PHARM DCED AND DEA CERT REVOKED ...Correct data Fid

NOTIFICATION: DEA CERTIFICATE REVOKED ...Correct data Filed

NOTIFICATION MESSAGE: Med orders(s) DCed. Cert revoked. Contact Pharm. d

No data filing errors.

Transport Finished...

---Creating Order Check Routines-----------------------------------

Build list of Active Rules, Elements and Datafields...

96 DATA FIELDS

81 ELEMENTS

39 RULES

Compile DataField Navigation code...

101 DataField Navigation Code Arrays

Compile Element Evaluation code...

75 Event Evaluation Code Arrays

Compile Element MetaCode...

81 Element Metacode Arrays

Get Compiler Function Code...

51 Compiler Include Functions

Compile Rule Element Relation code...

56 Rule Element Relation Code Arrays

Construct Decision Tree...

716 Sub-Routines

Optimize Sub-Routines...

287 Sub-Routines

60% Optimization

Assemble Routines...

39 OCXOZ\* Routines

Updating Routine file...

Updating KIDS files...

OR\*3.0\*306 Installed.

Apr 08, 2013@17:30:23

Not a production UCI

NO Install Message sent

Install Started for XU\*8.0\*609 :

Apr 08, 2013@17:30:23

Build Distribution Date: Feb 19, 2013

Installing Routines:

Apr 08, 2013@17:30:23

Updating Routine file...

Updating KIDS files...

XU\*8.0\*609 Installed.

Apr 08, 2013@17:30:23

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

OR GMPL GMTS XU 29 1.0 Installed.

Apr 08, 2013@17:30:23

No link to PACKAGE file

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

### OR\*3.0\*371

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<I1029\> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: or\*3.0\*371 4/8/13@17:31:29

=\> 371 ;Created on Mar 28, 2013@12:55:19

This Distribution was loaded on Apr 08, 2013@17:31:29 with header of

371 ;Created on Mar 28, 2013@12:55:19

It consisted of the following Install(s):

OR\*3.0\*371

Checking Install for Package OR\*3.0\*371

Install Questions for OR\*3.0\*371

Incoming Files:

101.52 ORDER DEA ARCHIVE INFO

> **NOTE:** You already have the 'ORDER DEA ARCHIVE INFO' File.

Want KIDS to INHIBIT LOGONs during the install? NO// n NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// n NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;9999 TELNET PORT

--------------------------------------------------------------------------------

Install Started for OR\*3.0\*371 :

Apr 08, 2013@17:35:07

Build Distribution Date: Mar 28, 2013

Installing Routines:

Apr 08, 2013@17:35:07

Installing Data Dictionaries:

Apr 08, 2013@17:35:07

Running Post-Install Routine: POST^ORY371

Updating Routine file...

Updating KIDS files...

OR\*3.0\*371 Installed.

Apr 08, 2013@17:35:07

Not a production UCI

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

### PSO\*7\*426

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: USER\$:\[BIRMUSER\]PSO_7_426.KID

KIDS Distribution saved on Apr 30, 2013@02:20:39

Comment: PSO\*7\*426

This Distribution contains Transport Globals for the following Package(s):

PSO\*7.0\*426

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

PSO\*7.0\*426

Use INSTALL NAME: PSO\*7.0\*426 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You've got PRIORITY mail!

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: PSO\*7.0\*426 5/7/13@10:19:42

=\> PSO\*7\*426 ;Created on Apr 30, 2013@02:20:39

This Distribution was loaded on May 07, 2013@10:19:42 with header of

PSO\*7\*426 ;Created on Apr 30, 2013@02:20:39

It consisted of the following Install(s):

PSO\*7.0\*426

Checking Install for Package PSO\*7.0\*426

Install Questions for PSO\*7.0\*426

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;9999 SSH VIRTUAL TERMINAL

PSO\*7.0\*426

--------------------------------------------------------------------------------

Install Started for PSO\*7.0\*426 :

May 07, 2013@10:20:04

Build Distribution Date: Apr 30, 2013

Installing Routines:

May 07, 2013@10:20:05

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*426 Installed.

May 07, 2013@10:20:05

Not a production UCI

NO Install Message sent