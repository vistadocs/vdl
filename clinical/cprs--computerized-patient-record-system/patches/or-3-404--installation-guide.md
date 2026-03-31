---
title: OR*3*404  and OR*3*385 Installation Guide CPRS GUI 30A
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: and OR*3*385  CPRS GUI 30A
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*404
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order la
audience: 
keywords: 
  - cprs
  - installation
  - table
  - contents
  - install
  - patch
  - class
  - sample
  - instructions
  - installed
page_count: 0
word_count: 8533
section_count: 21
table_count: 19
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: November 2014
revision_count: 1
revision_newest: 11/06/2014
revision_oldest: 11/06/2014
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_404_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_404_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Computerized Patient Record System Graphical User Interface (CPRS GUI)
---

Installation Guide

OR\*3.0\*385 and OR\*3.0\*404

![](or-3-404-and-or-3-385-installation-guide-cprs-gui-30a/001.png)

November 2014

Office of Information & Technology (OI&T)

Product Development (PD)

This page left intentionally blank.  

Revision History

| Date       | Version | Description                           | Author                             |
|------------|---------|---------------------------------------|------------------------------------|
| 11/06/2014 | 1.0     | Combine OR\*3.0\*385 and OR\*3.0\*404 | <span class="mark">REDACTED</span> |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |
|            |         |                                       |                                    |

This page left blank intentionally.

Table of Contents

This page left blank intentionally.

# Computerized Patient Record System Graphical User Interface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Computerized Patient Record System Graphical User Interface](#computerized-patient-record-system-graphical-user-interface)
  - [Overview](#overview)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [National Deployment](#national-deployment)
  - [Document Conventions](#document-conventions)
  - [Related Documents](#related-documents)
- [Pre-requisites](#pre-requisites)
  - [Deployment Authorization](#deployment-authorization)
  - [ICD-10 Program Groups 1-5 Installation Instructions](#icd-10-program-groups-1-5-installation-instructions)
  - [Pre-requisite Patches for OR\3.0\385](#pre-requisite-patches-for-or30385)
  - [Pre-requisite Patch for OR\3.0\404](#pre-requisite-patch-for-or30404)
- [OR\3.0\385 Installed in Production and Test—Installation Checklist](#or30385-installed-in-production-and-testinstallation-checklist)
  - [Software Retrieval](#software-retrieval)
  - [Installation Sequence](#installation-sequence)
    - [CPRS v30.A Follow-up Patch Host File (OR30404.KID)](#cprs-v30a-follow-up-patch-host-file-or30404kid)
    - [CPRS GUI Executable (OR30404.zip)](#cprs-gui-executable-or30404zip)
- [OR\3.0\385 in Test Only—Installation Checklist](#or30385-in-test-onlyinstallation-checklist)
  - [Software Retrieval](#software-retrieval-1)
  - [Installation Sequence](#installation-sequence-1)
    - [CPRS v30.A Host File (OR30385.KID)](#cprs-v30a-host-file-or30385kid)
    - [CPRS v30.A Follow-up Patch Host File (OR30404.KID)](#cprs-v30a-follow-up-patch-host-file-or30404kid-1)
    - [CPRS GUI Executable (OR30404.zip)](#cprs-gui-executable-or30404zip-1)
- [OR\3.0\385 Not Installed—Installation Checklist](#or30385-not-installedinstallation-checklist)
  - [Software Retrieval](#software-retrieval-2)
  - [Installation Sequence](#installation-sequence-2)
    - [CPRS v30.A Host File (OR30385.KID)](#cprs-v30a-host-file-or30385kid-1)
    - [CPRS v30.A Follow-up Patch Host File (OR30404.KID)](#cprs-v30a-follow-up-patch-host-file-or30404kid-2)
    - [CPRS GUI Executable (OR30404.zip)](#cprs-gui-executable-or30404zip-2)
- [Installation Sequence](#installation-sequence-3)
  - [CPRS GUI Executable (OR30404.zip)](#cprs-gui-executable-or30404zip-3)
    - [Changes to the Installation Procedure for the CPRS GUI](#changes-to-the-installation-procedure-for-the-cprs-gui)
    - [Methods of installation](#methods-of-installation)
    - [Overview of the process: Loader in front of CPRS](#overview-of-the-process-loader-in-front-of-cprs)
    - [Manual or Test Installation](#manual-or-test-installation)
  - [CPRS Documentation](#cprs-documentation)
- [## CPRS GUI Installation Troubleshooting Guide](#cprs-gui-installation-troubleshooting-guide)
    - [Interface: Visual GUI and Switches](#interface-visual-gui-and-switches)
    - [Uninstallation](#uninstallation)
    - [Batch File](#batch-file)
    - [DLL Distribution](#dll-distribution)
    - [Delay Updating from MSP File during Installation](#delay-updating-from-msp-file-during-installation)
    - [Do Not Modify MSI or MSP Files](#do-not-modify-msi-or-msp-files)
  - [CPRS v30.A (OR\3.0\385) M patches—Software Installation Sample](#cprs-v30a-or30385-m-patchessoftware-installation-sample)
  - [CPRS v30.A (OR\3.0\404) Follow-up M patch—Software Installation Sample](#cprs-v30a-or30404-follow-up-m-patchsoftware-installation-sample)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

This installation guide deals specifically with the installation of CPRS GUI v30.A. It will include instructions for the installation of patches OR\*3.0\*385 and OR\*3.0\*404 and then CPRS Windows executable CPRSChart.exe (1.0.30.16). Because the deployment of CPRS GUI 30.A was paused in the middle of a wave, sites may have different situations as far as the deployment of the OR\*3.0\*385 patch and the previous CPRS GUI executable (1.0.30.15). Instructions as to how each site should proceed with installation will be sent to the sites.

> **NOTE:** If a site does not have CPRSChart.exe (version 1.0.30.15) installed, they will proceed directly to install the latest version 1.0.30.16!

The CPRS GUI 30.A deployment was paused when a problem was discovered. CPRS GUI v30.A includes projects to implement the use of the International Classification of Diseases, Tenth Revision (ICD-10) coding system for patient care encounter and billing purposes. These changes will become active when the appropriate change occurs in the system (currently scheduled for October 1, 2015). A number of other defects found by the field were also corrected. With the addition of OR\*3.0\*404, CPRS GUI 30.A will also address a problem with Reminders prompts and the slow loading of the Encounter form.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) Information Resource Management (IRM) staff.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation guide provides instructions for:

- Installing application components that run on M servers at VAMC facilities
- Installing Windows executable programs on workstations or application servers at VAMC facilities

## National Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

National deployment of CPRS 30.A began and was into its second wave of sites when it was paused. Because deployment was paused, sites had proceeded with the install to varying degrees. To determine what each site needs to do now to complete the installation of CPRS 30.A, this document will use the status of your installation of patch OR\*3.0\*385, whether in production, in test, or not installed at all, to determine which set of instructions below (Sections 3, Section 4, or Section 5) you will use to complete the installation of patch OR\*3.0\*404 and the latest CPRSChart.exe (1.0.30.16).

> **NOTE:** OR\*3.0\*385 was distributed with a GUI executable CPRSChart.exe version 1.0.30.15. If your site has not installed the previous CPRSChart.exe executable (1.0.30.15), you will proceed directly to install the latest version (1.0.30.16) that will be distributed with patch OR\*3.0\*404.

Specific instructions for your site will come from the CPRS Implementation Manager to install CPRS v30.A and its related patches.

To see current status and target dates, please refer to the [CPRS v30a Deployment Schedule](http://vaww.oed.portal.va.gov/projects/CPRS/v30/30A/Public/Deployment/CPRS%20v30a%20Deployment%20Schedule.xlsx).

Sites will be given access to the OR\*3.0\*385 files (if they have not yet installed them), the OR\*3.0\*404 files, and the CPRS Windows executable (CPRSChart.exe version 1.0.30.16) through the same secure FTP site using the credentials that were sent previously to Wave 1 and Wave 2 sites. Wave 3 sites had not installed and will have a kick-off meeting and will receive the access codes and instructions in an encrypted email. The communication will also include the list of files they should download and the download format required (ASCII/binary).

After the completion of the final deployment wave, the software will be made available on the national anonymous FTP site for access by any VA network domain member.

How you proceed will depend on your site’s situation. Which of the following best describes your site’s installation status with OR\*3.0\*385?

- [OR\*3.0\*385 installed in Production](#or3.0385-installed-in-production-and-testinstallation-checklist)
- [OR\*3.0\*385 in Test only](#or3.0385-in-test-onlyinstallation-checklist)
- [Have not installed OR\*3.0\*385 at all](#or3.0385-not-installedinstallation-checklist)
- OR\*3.0\*404 test sites may install the released version of patch OR\*3.0\*404 at their earliest convenience. They do NOT need to reinstall CPRSChart.exe, providing it is version 1.0.30.16.

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

- CPRS Technical Manual: GUI Version
- CPRS User Guide: GUI Version
- CPRS GUI v30.A (Patch# OR\*3.0\*385) Release Notes

The following document, available on the [CPRS v 30 SharePoint site](http://vaww.oed.portal.va.gov/projects/CPRS/v30/30A/Forms/AllItems.aspx), is a useful resource for sites preparing for ICD-10 usage.

- [CPRS v30.A Frequently Asked Questions](http://vaww.oed.portal.va.gov/projects/CPRS/v30/30A/CPRS%20GUI%2030.A%20FAQs.doc)

# Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the processes described in this document the tasks outlined in this section must be completed.

## Deployment Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Receive authorization to proceed based upon the deployment schedule discussed in Section 1.4, National Deployment, above

## ICD-10 Program Groups 1-5 Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ensure that you have completed the Installation Instructions for ICD-10 Program Groups 1-5 prior to beginning the installation steps located in this document.

## Pre-requisite Patches for OR\*3.0\*385

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For sites that have not installed patch OR\*3.0\*385, the following, previously released, patches <u>must</u> be installed before installing patch OR\*3.0\*385:

- GMPL\*2.0\*42
- PXRM\*2.0\*26
- OR\*3.0\*361

## Pre-requisite Patch for OR\*3.0\*404

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following, previously released, patch <u>must</u> be installed before installing patch OR\*3.0\*404:

- OR\*3.0\*385

# OR\*3.0\*385 Installed in Production and Test—Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

Table 1 OR\*3.0\*404 and CPRS GUI 30.16—Installation Checklist

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
<td><p>Verify that your site has OR*3.0*385 installed in both your <strong>Production</strong> and <strong>Test</strong> environments. If you do not, this is the wrong set of instructions for you.</p>
<p>If you have OR*3.0*385, installed only in test, see Section 4, OR*3.0*385 in Test Only—Installation Checklist.</p>
<p>If you do not have OR*3.0*385 installed at all, see section 5, OR*3.0*385 Not Installed—Installation Checklist.</p></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td><p>Read previously supplied documentation:</p>
<ul>
<li><p>CPRS Technical Manual: GUI Version</p></li>
<li><p>CPRS GUI v.30A (Patch# OR*3.0*385) Release Notes</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">Test/Mirror System Installation</td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Confirm that patch OR*3.0*385 has been installed in your Test/Mirror system</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Download CPRS GUI installation package files, including OR_30_404.zip</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td>Install the OR*3.0*404 patch using the instructions in Section 3.2.1, CPRS v30.A Follow-up Patch Host File (OR_30_404.KID).</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Install the latest version of the CPRS GUI (1.0.30.16). (See Section 6.1, CPRS GUI Executable (OR_30_404.zip), below),install per the instructions in that section, and point user shortcuts to your Test/Mirror system</td>
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
<td>Confirm that patch OR*3.0*385 has been installed in your Production/Live system</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="9" type="1">
<li></li>
</ol></td>
<td>Install the OR*3.0*404 patch using the instructions in Section 3.2.1, CPRS v30.A Follow-up Patch Host File (OR_30_404.KID).</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="10" type="1">
<li></li>
</ol></td>
<td>Install the latest CPRSChart.exe from the OR_30_404.zip according to the instructions in Section 6.1, CPRS GUI Executable (OR_30_404.zip), below) and point user shortcuts to your Production/Live system</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="11" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Production/Live system has been successful</td>
<td></td>
</tr>
</tbody>
</table>

## Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is for sites that already have OR\*3.0\*385 in their Production and Test accounts. As such, you have installed the OR\*3.0\*385 patch, and CPRSChart.exe, and the documentation and help files.

Your site only need to download and install OR_30_404.KID and the GUI executable along with its supporting installation guide (all listed in Table 2 CPRS v30.A files).

If you previously downloaded the CPRS 30.A software from the secure FTP site, you can use the same access information to download the OR\*3.0\*404 patch and related files. The necessary files are:

Table 2 CPRS v30.A files

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Filename</th>
<th>File Contents</th>
</tr>
<tr class="odd">
<th>OR_30_404.kid</th>
<th>Patch OR*3.0*404 host file</th>
</tr>
<tr class="header">
<th>OR_30_404.zip</th>
<th><p>CPRSChart.exe</p>
<p>CPRS_30_16.msp</p></th>
</tr>
<tr class="odd">
<th>OR_30_404_IG.doc</th>
<th>Installation Guide for OR*3.0*404</th>
</tr>
<tr class="header">
<th>OR_30_404_IG.pdf</th>
<th>PDF (Portable Document Format) copy of the Installation Guide</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section refers only to the installation of OR\*3.0\*404 and CPRSChart.exe version 1.0.30.16.

### CPRS v30.A Follow-up Patch Host File (OR_30_404.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

This patch should be installed during non-peak hours to minimize disruption. No users should be accessing CPRS during the install as this prevents you from replacing CPRSChart.exe. Installation should take less than 15 minutes, depending on the menu structure at your site.

Listed below are general installation instructions for installing the OR\*3.0\*404 KIDS build. To view an example installation, refer to Appendix C, CPRS v30.A (OR\*3.0\*404) Follow-up M patch—Software Installation Sample. Additionally, review the National Patch Module messages for patch-specific information.

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

See an example of the host file installation capture Appendix B, CPRS v30.A (OR\*3.0\*385) M patches—Software Installation Sample, below.

### CPRS GUI Executable (OR_30_404.zip)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 6.1, CPRS GUI Executable (OR_30_404.zip) and the following sections for instructions on installing the CPRS GUI executable (1.0.30.16). If you have any need for troubleshooting, please see Appendix A, CPRS GUI Installation Troubleshooting Guide.

# OR\*3.0\*385 in Test Only—Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

Table 3 For Sites with OR\*3.0\*385 in Test—Installation Checklist

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
<td><p>Verify that your site has OR*3.0*385 installed only in your <strong>Test</strong> environments. If you do not, this is the wrong set of instructions for you.</p>
<p>If you have OR*3.0*385, installed only in Production and Test, see Section 3, OR*3.0*385 Installed in Production and Test—Installation Checklist.</p>
<p>If you do not have OR*3.0*385 installed at all, see Section 5, OR*3.0*385 Not Installed—Installation Checklist.</p></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td><p>Read previously supplied documentation:</p>
<ul>
<li><p>CPRS Technical Manual: GUI Version</p></li>
<li><p>CPRS GUI v.30A (Patch# OR*3.0*385) Release Notes</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">Test/Mirror System Installation</td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Confirm that OR*3.0*385 is installed in your test account</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Download CPRS GUI installation package for OR*3.0*404.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td>Install patch OR*3.0*404 using the instructions in section 4.2.2, CPRS v30.A Follow-up Patch Host File (OR_30_404.KID).</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Install the latest CPRS GUI executable (1.0.30.16). (see Section 6.1, CPRS GUI Executable (OR_30_404.zip), below),install per the instructions in that section, and point user shortcuts to your Test/Mirror system</td>
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
<td><p>Confirm all Pre-requisite patches for OR*3.0*385 have been installed in your Production/Live system (see Section 2.3, Pre-requisite Patches for OR*3.0*385</p>
<p>, above)</p></td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="9" type="1">
<li></li>
</ol></td>
<td>Install the OR*3.0*385 patch using the instructions in section 4.2.1, CPRS v30.A Host File (OR_30_385.KID).</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="10" type="1">
<li></li>
</ol></td>
<td>Copy the documentation and Help files to the appropriate locations as per your normal procedures</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="11" type="1">
<li></li>
</ol></td>
<td>Download CPRS GUI installation package for OR*3.0*404</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="12" type="1">
<li></li>
</ol></td>
<td>Install the OR*3.0*404 patch using the instructions in section 4.2.2, CPRS v30.A Follow-up Patch Host File (OR_30_404.KID)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="13" type="1">
<li></li>
</ol></td>
<td>Install the latest CPRSChart.exe from the OR_30_404.zip according to the instructions in Section 6.1, CPRS GUI Executable (OR_30_404.zip), below) and point user shortcuts to your Production/Live system</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="14" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Production/Live system has been successful</td>
<td></td>
</tr>
</tbody>
</table>

## Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is for sites that already have OR\*3.0\*385 in their Test accounts only. As such, you have installed the OR\*3.0\*385 patch and CPRSChart.exe and should have the documentation and help files in test. You will need to have these in order to install them in production as well.

Your site will need to download the OR\*3.0\*404 installation files, which include OR_30_404,KID and the GUI executable (1.0.30.16) ( the files are listed in  
Table 4 OR\*3.0\*385 files and Table 5 OR\*3.0\*404 files).

If you previously downloaded the CPRS 30.A software from the secure FTP site, you can use the same access information to download the OR\*3.0\*404 patch and related files. The necessary files are:

  
Table 4 OR\*3.0\*385 files

> **NOTE:** You should have already downloaded these file. They are listed here for reference or in case you need to download them again.

| Files associated with patch OR\*3.0\*385 | File Contents / Supported Functionality                                          |
|------------------------------------------|----------------------------------------------------------------------------------|
| OR_30_385.KID                            | Contains the Patch OR\*3.0\*385 host file                                        |
| CPRSGUITM.doc                            | CPRS Technical Manual: GUI Version (this file is in the Documentation directory) |
| CPRSGUIUM.doc                            | CPRS User Guide: GUI Version (this file is in the Documentation directory)       |
| OR_30_385_RN.doc                         | Patch OR\*3.0\*385 Release Notes (this file is in the Documentation directory)   |
| CPRS_30A_HELP.ZIP                        | Contains the Help directory (or folder) with all files for the Help system       |

Table 5 OR\*3.0\*404 files

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Filename</th>
<th>File Contents</th>
</tr>
<tr class="odd">
<th>OR_30_404.kid</th>
<th>Patch OR*3.0*404 host file</th>
</tr>
<tr class="header">
<th>OR_30_404.zip</th>
<th><p>CPRSChart.exe</p>
<p>CPRS_30_16.msp</p></th>
</tr>
<tr class="odd">
<th>OR_30_404_IG.doc</th>
<th>Installation Guide for OR*3.0*404</th>
</tr>
<tr class="header">
<th>OR_30_404_IG.pdf</th>
<th>PDF (Portable Document Format) copy of the Installation Guide</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is for the installation of patches OR\*3.0\*385, OR\*3.0\*404, and the CPRS GUI executable (CPRSChart.exe version 1.0.30.16).

### CPRS v30.A Host File (OR_30_385.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

This patch should be installed during non-peak hours to minimize disruption. No users should be accessing CPRS during the install as this prevents you from replacing CPRSChart.exe. Installation will take approximately 15 minutes or more, depending on the menu structure at your site.

Listed below are general installation instructions for installing the CPRS GUI v30.A KIDS build and other patches. To view a sample installation, refer to Appendix B, CPRS v30.A (OR\*3.0\*385) M patches—Software Installation Sample. Additionally, review the National Patch Module messages for each patch for patch-specific information.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
10. Use Load a Distribution. You may need to prefix a directory name.
11. If given the option to run any Environment Check Routine(s), answer "YES."
12. From this menu, you may then elect to use the following options:
- Backup a Transport Global
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
13. When ready, select the Install Packages option.
14. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? Yes//", respond "NO."
15. When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond "YES."
16. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', respond YES. When prompted to select the options you would like to place out of order, enter the following:

OR OE/RR MENU CLINICIAN CPRS Clinician Menu

OR OE/RR MENU NURSE CPRS Nurse Menu

OR OE/RR MENU WARD CLERK CPRS Ward Clerk Menu

OR CPRS GUI CHART

17. When prompted 'Delay Install (Minutes): (0-60): 0//; respond '0.'

### CPRS v30.A Follow-up Patch Host File (OR_30_404.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

This patch should be installed during non-peak hours to minimize disruption. No users should be accessing CPRS during the install as this prevents you from replacing CPRSChart.exe. Installation should take less than 15 minutes, depending on the menu structure at your site.

Listed below are general installation instructions for installing the OR\*3.0\*404 KIDS build. To view a sample installation, refer to Appendix C, CPRS v30.A (OR\*3.0\*404) Follow-up M patch—Software Installation Sample. Additionally, review the National Patch Module messages for patch-specific information.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
18. Use Load a Distribution. You may need to prefix a directory name.
19. If given the option to run any Environment Check Routine(s), answer "YES."
20. From this menu, you may then elect to use the following options:
- Backup a Transport Global
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
21. When ready, select the Install Packages option.
22. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? Yes//", respond "YES."
23. When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond "YES."
24. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', respond YES. When prompted to select the options you would like to place out of order, enter the following:

OR OE/RR MENU CLINICIAN CPRS Clinician Menu

OR OE/RR MENU NURSE CPRS Nurse Menu

OR OE/RR MENU WARD CLERK CPRS Ward Clerk Menu

OR CPRS GUI CHART

25. When prompted 'Delay Install (Minutes): (0-60): 0//; respond '0.'

### CPRS GUI Executable (OR_30_404.zip)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 6.1, CPRS GUI Executable (OR_30_404.zip) and the following sections for instructions on installing the CPRS GUI executable (1.0.30.16). If you have any need for troubleshooting, please see Appendix A, CPRS GUI Installation Troubleshooting Guide, below.

# OR\*3.0\*385 Not Installed—Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

Table 6 Sites without OR\*3.0\*385—Installation Checklist

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
<td><p>These instructions are only for those sites who <strong>do not have OR*3.0*385 installed</strong>.</p>
<p>If you have OR*3.0*385 installed in Production, please use the instructions in Section 3, OR*3.0*385 Installed in Production and Test—Installation Checklist.</p>
<p>If you have OR*3.0*385 installed only in Test, please use the instructions in Section 4, OR*3.0*385 in Test Only—Installation Checklist.</p></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td><p>Read previously supplied documentation:</p>
<ul>
<li><p>CPRS Technical Manual: GUI Version</p></li>
<li><p>CPRS GUI v.30A (Patch# OR*3.0*385) Release Notes</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">Test/Mirror System Installation</td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td><p>Confirm all Pre-requisite patches have been installed in your Test/Mirror system (see Section 2.3, Pre-requisite Patches for OR*3.0*385</p>
<p>, above)</p></td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Attend the CPRS v30.A Training session for your site’s deployment wave per the <a href="http://vaww.oed.portal.va.gov/projects/CPRS/v30/30A/Public/Deployment/CPRS%20v30a%20Deployment%20Schedule.xlsx">CPRS v30a Deployment Schedule</a> </td>
<td></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td><span id="step_four" class="anchor"></span>Download CPRS GUI installation package for patch OR*3.0*385 and OR*3.0*404 (files listed below in Table 7 OR*3.0*385 files and Table 8 OR*3.0*404 files)</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Install patch OR*3.0*385 according to instructions in section 5.2.1, CPRS v30.A Host File (OR_30_385.KID)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="7" type="1">
<li></li>
</ol></td>
<td>Copy the documentation and Help files to the appropriate locations as per your normal procedures</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="8" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Test/Mirror system has been successful</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="9" type="1">
<li></li>
</ol></td>
<td>Download CPRS GUI installation package for OR*3.0*404.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="10" type="1">
<li></li>
</ol></td>
<td>Install patch OR*3.0*404 using the instructions in section 5.2.2, CPRS v30.A Follow-up Patch Host File (OR_30_404.KID)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="11" type="1">
<li></li>
</ol></td>
<td>Install the latest CPRSChart.exe (1.0.30.16) (see Section 6.1, CPRS GUI Executable (OR_30_404.zip), below),install per the instructions in that section, and point user shortcuts to your Test/Mirror system</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3">Production/Live System Installation</td>
</tr>
<tr class="even">
<td><ol start="12" type="1">
<li></li>
</ol></td>
<td><p>Confirm all Pre-requisite patches have been installed in your Production/Live system (see Section 2.3, Pre-requisite Patches for OR*3.0*385</p>
<p>, above)</p></td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="13" type="1">
<li></li>
</ol></td>
<td>Install patch OR*3.0*385 according to instructions in section 5.2.1, CPRS v30.A Host File (OR_30_385.KID)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="14" type="1">
<li></li>
</ol></td>
<td>Copy the documentation and Help files to the appropriate locations as per your normal procedures</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="15" type="1">
<li></li>
</ol></td>
<td>Install patch OR*3.0*404 using the instructions in section 5.2.2, CPRS v30.A Follow-up Patch Host File (OR_30_404.KID)</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="16" type="1">
<li></li>
</ol></td>
<td>Install the latest CPRSChart.exe (1.0.30.16) (see Section 6.1, CPRS GUI Executable (OR_30_404.zip), below),install per the instructions in that section, and point user shortcuts to your Production/Live system</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="17" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Production/Live system has been successful</td>
<td></td>
</tr>
</tbody>
</table>

## Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is for sites that have not yet installed OR\*3.0\*385 in Test or Production. These sites will need to download files for the OR\*3.0\*385 installation, including the documentation and help files. You will also need to download the OR\*3.0\*404 files. You will first install them in test and then in production.

Sites that have not yet installed are mostly from Wave 3. For these sites, there will be a kick-off meeting and additional communication to send the appropriate personnel access codes and instructions for the secure FTP site where the files are located. The necessary files are:

Table 7 OR\*3.0\*385 files

| Files associated with patch OR\*3.0\*385 | File Contents / Supported Functionality                                          |
|------------------------------------------|----------------------------------------------------------------------------------|
| OR_30_385.KID                            | Contains the Patch OR\*3.0\*385 host file                                        |
| CPRSGUITM.doc                            | CPRS Technical Manual: GUI Version (this file is in the Documentation directory) |
| CPRSGUIUM.doc                            | CPRS User Guide: GUI Version (this file is in the Documentation directory)       |
| OR_30_385_RN.doc                         | Patch OR\*3.0\*385 Release Notes (this file is in the Documentation directory)   |
| CPRS_30A_HELP.ZIP                        | Contains the Help directory (or folder) with all files for the Help system       |

[Back to Installation Checklist](#step_four)

Table 8 OR\*3.0\*404 files

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Filename</th>
<th>File Contents</th>
</tr>
<tr class="odd">
<th>OR_30_404.kid</th>
<th>Patch OR*3.0*404 host file</th>
</tr>
<tr class="header">
<th>OR_30_404.zip</th>
<th><p>CPRSChart.exe</p>
<p>CPRS_30_16.msp</p></th>
</tr>
<tr class="odd">
<th>OR_30_404_IG.doc</th>
<th>Installation Guide for OR*3.0*404</th>
</tr>
<tr class="header">
<th>OR_30_404_IG.pdf</th>
<th>PDF (Portable Document Format) copy of the Installation Guide</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

[Back to Installation Checklist](#step_four)

## Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is for the installation of patches OR\*3.0\*385, OR\*3.0\*404, and the CPRS GUI executable (CPRSChart.exe version 1.0.30.16).

### CPRS v30.A Host File (OR_30_385.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

This patch should be installed during non-peak hours to minimize disruption. No users should be accessing CPRS during the install as this prevents you from replacing CPRSChart.exe. Installation will take approximately 15 minutes or more, depending on the menu structure at your site.

Listed below are general installation instructions for installing the CPRS GUI v30.A KIDS build and other patches. To view a sample installation, refer to Appendix B, CPRS v30.A (OR\*3.0\*385) M patches—Software Installation Sample. Additionally, review the National Patch Module messages for each patch for patch-specific information.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
26. Use Load a Distribution. You may need to prefix a directory name.
27. If given the option to run any Environment Check Routine(s), answer "YES."
28. From this menu, you may then elect to use the following options:
- Backup a Transport Global
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
29. When ready, select the Install Packages option.
30. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? Yes//", respond "NO."
31. When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond "YES."
32. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', respond YES. When prompted to select the options you would like to place out of order, enter the following:

OR OE/RR MENU CLINICIAN CPRS Clinician Menu

OR OE/RR MENU NURSE CPRS Nurse Menu

OR OE/RR MENU WARD CLERK CPRS Ward Clerk Menu

OR CPRS GUI CHART

33. When prompted 'Delay Install (Minutes): (0-60): 0//; respond '0.'

### CPRS v30.A Follow-up Patch Host File (OR_30_404.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

This patch should be installed during non-peak hours to minimize disruption. No users should be accessing CPRS during the install as this prevents you from replacing CPRSChart.exe. Installation should take less than 15 minutes, depending on the menu structure at your site.

Listed below are general installation instructions for installing the OR\*3.0\*404 KIDS build. To view a sample installation, refer to Appendix C, CPRS v30.A (OR\*3.0\*404) Follow-up M patch—Software Installation Sample. Additionally, review the National Patch Module messages for patch-specific information.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
34. Use Load a Distribution. You may need to prefix a directory name.
35. If given the option to run any Environment Check Routine(s), answer "YES."
36. From this menu, you may then elect to use the following options:
- Backup a Transport Global
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
37. When ready, select the Install Packages option.
38. When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? Yes//", respond "YES."
39. When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond "YES."
40. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', respond YES. When prompted to select the options you would like to place out of order, enter the following:

OR OE/RR MENU CLINICIAN CPRS Clinician Menu

OR OE/RR MENU NURSE CPRS Nurse Menu

OR OE/RR MENU WARD CLERK CPRS Ward Clerk Menu

OR CPRS GUI CHART

41. When prompted 'Delay Install (Minutes): (0-60): 0//; respond '0.'

### CPRS GUI Executable (OR_30_404.zip)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See section 6.1, CPRS GUI Executable (OR_30_404.zip) and the following sections for instructions on installing the CPRS GUI executable (1.0.30.16). If you have any need for troubleshooting, please see Appendix A, CPRS GUI Installation Troubleshooting Guide, below.

# Installation Sequence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide gives instructions for installing the latest version of CPRS GUI 30.A, which includes the following:

- OR\*3.0\*385
- OR\*3.0\*404
- CPRSChart.exe
- The Help directory
- The documentation files

## CPRS GUI Executable (OR_30_404.zip)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections provide basic CPRS GUI installation instructions for the CPRSChart. (For advanced installation troubleshooting see Appendix A, CPRS GUI Installation Troubleshooting Guide, below).

### Changes to the Installation Procedure for the CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The method of installation determines which files are needed for installation.

### Methods of installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **WARNING:** If you are doing a TEST install, DO NOT use the gold path installation method on a production machine, or it will override their production install. On a test machine that also has a production install, you must MANUALLY install it.

Sites are generally using the following four methods to distribute the application:

- Network (shared) installation:  
  The executable is placed on a network drive, with a shortcut for each Vista account to be accessed by the user on the users’ desktops. The executable is replaced when no users are accessing the GUI program.
- Citrix installation:  
  The executable is run on a remote workstation and the user views the screen remotely.
- Gold Path installation:

> A new windows installer patch (.msp file) containing the executable is placed in a common shared location (called a gold path), and updated when the CPRS GUI is first accessed from the local workstation.

- Manual install:

  Used primarily for advanced users and at testing locations. This method is somewhat changed from that used previously. For more detail please refer to section 6.1.4, Manual or Test Installation, below.

### Overview of the process: Loader in front of CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For most types of installation, no changes are needed, since those performing the install will have administrator rights. For gold path installations, some changes are necessary:

First, CPRSLoader should already be installed on the workstation. For more details of how to do this, read CPRSLoader_InstallGuide.doc.

Second, after the Vista install is complete, an administrator places the appropriate .msp file into the gold directory.

Once that is completed, end users click on the previously created icon that points to the loader. The loader checks the gold directory for new updates, installs the new windows patch file containing the new version of CPRS, then starts up CPRSChart.

1.  Automated process

![](or-3-404-and-or-3-385-installation-guide-cprs-gui-30a/002.png)

### Manual or Test Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Things that should be done beforehand:

1.  Determine the DNS server name or IP address for the appropriate VistA server.
2.  Determine the Broker RPC port for the VistA account.
3.  Acquire the CPRSChart.exe file and related dlls (the minimum is borlndmm.dll).

#### To install manually on a workstation, follow these steps:

2.  Copy CPRSChart.exe and borlndmm.dll into the desired location on the workstation. For a production instance, C:\Program Files (x86)\vista\CPRS is recommended; and any other location is used for a test instance.
3.  Copy any necessary dlls into the common vista directory (Usually C:\Program Files (x86)\vista\Common Files).
4.  Create a shortcut to CPRSChart.exe, putting s=\[vista server\] p=\[vista port\] on the command line.
2.  When the user first runs the executable after the CPRS 30.A installation, it may take several minutes while CPRS configures itself. This is different from previous CPRS installations. Unfortunately, there is no indicator to tell the user that CPRS is getting ready to run the new version. Users must be patient and let CPRS run through the set up for the new version. If the user continues to click on the icon, multiple CPRS sessions could be launched and the machine may not be able to handle all the sessions.

## CPRS Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Place the User Guide and Technical Manual files in a location that can be accessed by CPRS users.

The following documents are provided, as part of the CPRS v30.A installation package. Please place these files in a location that can be accessed by CPRS users.

Table 4 CPRS v30.A documentation

| OR_30_404_IG.doc            | CPRS GUI v30.A Installation Guide (this document )                                                                                                                |
|-----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPRSGUIUM.doc               | CPRS User Guide: GUI Version                                                                                                                                      |
| CPRSGUITM.doc               | CPRS Technical Manual: GUI Version (partner to CPRSLMTM, above, covering the GUI application)                                                                     |
| OR_30_385_RN.doc            | Patch Release Notes for OR\*3.0\*385                                                                                                                              |
| CPRSLoader_InstallGuide.doc | Initial CPRS GUI Installation guide for new machines. (This file is only available on the [VA Document Library](http://www.va.gov/vdl/application.asp?appid=61).) |

# ## CPRS GUI Installation Troubleshooting Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Interface: Visual GUI and Switches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two Graphical User Interfaces (GUIs) used during this process. The first one is the MSI GUI, which is detailed in section <span class="mark"></span>6.1.4.2, To install manually on a workstation, follow these steps, above and the CPRSLoader GUI, which shouldn't be seen by an end user during normal operation. With the switches available, it doesn't need to be seen at all.

The switches are as follows:

SHOW Shows the loader's GUI. The GUI is invisible if this switch isn't used.

GOLD=*filename* Changes the gold directory for the auto-update feature.

SetCPRS=*filename* Changes the location the loader looks for the current CPRSChart.

SetServer=*servername* Changes the DNS server name for the VistA server CPRSChart uses.

SetPort=*portnumber* Changes the broker port for the VistA account CPRSChart uses.

FORCE Forces the installer to run the latest patch file.

LOGLOAD Creates a log file named CPRSLoader.log in the user’s document directory.

The main screen looks like this:  
![](or-3-404-and-or-3-385-installation-guide-cprs-gui-30a/003.png)

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

> ![](or-3-404-and-or-3-385-installation-guide-cprs-gui-30a/004.png)

Exit Menu: Leave the loader application.

### Uninstallation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The uninstaller can be run from the Programs and Features list in the Control Panel or it can be run by clicking on the msi installer file. Choose the Remove option to remove both CPRSLoader and CPRSChart from the install directory.

### Batch File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A batch file can be used to install either the loader or the patch. The command is:

> msiexec /i CPRS.msi DB_CONNECTIONS=One VISTA_DNS_NAME=dnsname VISTA_RPC_BROKER_PORT=brokerport INSTALLCPRSLOADER=Yes GOLD_PATH=golddirectory SHORTCUT_LOCATION=StartMenuAndDesktop /qn

This will install the loader application silently, if the local values for dnsname, brokerport and golddirectory are filled in properly.

The command for a patch file is similar:

> msiexec /p golddirectory\CPRS_30A.msp VISTA_DNS_NAME=dnsname VISTA_RPC_BROKER_PORT=brokerport GOLD_PATH=golddirectory /qn

For both commands, dnsname is the DNS name for the vista server, brokerport is the rpc broker port, and golddirectory is the location of the Gold directory containing the patch updates.

### DLL Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Even though some dlls were included in the initial install, the CPRS installation system is not intended to replace the distribution methods or systems of other applications.

### Delay Updating from MSP File during Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There may be a delay in the user’s workstation detecting the presence of a new msp file. If during an installation the loader doesn't seem to pick up the msp file, it may be necessary to wait for the network to refresh its directory information cache on the user’s workstation. The wait time is workstation and network dependent.

### Do Not Modify MSI or MSP Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DO NOT MODIFY THE MSI OR MSP FILES. Modifying the msi or msp file will make it so that CPRS will not install. The distributed msi file contains a digital certificate necessary for future installations and modifying the file will remove the certificate. The msp file is comprised of a series of change instructions based on a specific msi file. If the msi is changed in any way, the msp cannot run. A similar problem occurs when the msp file is modified. It is very important that neither of these files are altered.

## CPRS v30.A (OR\*3.0\*385) M patches—Software Installation Sample

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: OR\*3.0\*385 2/28/14@09:12:52

=\> OR\*3.0\*385 Test v12 ;Created on Feb 27, 2014@14:27

This Distribution was loaded on Feb 28, 2014@09:12:52 with header of

OR\*3.0\*385 Test v12 ;Created on Feb 27, 2014@14:27

It consisted of the following Install(s):

OR\*3.0\*385

Checking Install for Package OR\*3.0\*385

Install Questions for OR\*3.0\*385

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// NO

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TEMINAL

-------------------------------------------------------------------------------

Install Started for OR\*3.0\*385 :

Feb 28, 2014@09:45:33

Build Distribution Date: Feb 27, 2014

Installing Routines:

Feb 28, 2014@09:45:33

Installing PACKAGE COMPONENTS:

Installing REMOTE PROCEDURE

Installing OPTION

Feb 28, 2014@09:45:35

Updating Routine file...

Updating KIDS files...

OR\*3.0\*385 Installed.

Feb 28, 2014@09:45:35

Not a production UCI

NO Install Message sent

Install Completed

## CPRS v30.A (OR\*3.0\*404) Follow-up M patch—Software Installation Sample

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: OR\*3.0\*404 10/07/14@09:12:52

=\> OR\*3.0\*404 Test v16 ;Created on Oct 7, 2014@14:27

This Distribution was loaded on Oct 7, 2014@09:12:52 with header of

OR\*3.0\*404 Test v16 ;Created on Oct 7, 2014@14:27

It consisted of the following Install(s):

OR\*3.0\*404

Checking Install for Package OR\*3.0\*404

Install Questions for OR\*3.0\*404

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// YES

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TEMINAL

-------------------------------------------------------------------------------

Install Started for OR\*3.0\*404 :

Oct 10, 2014@09:45:33

Build Distribution Date: Oct 7, 2014

Installing Routines:

Oct 7, 2014@09:45:33

Installing PACKAGE COMPONENTS:

Installing OPTION

Oct 7, 2014@09:45:35

Updating Routine file...

Updating KIDS files...

OR\*3.0\*404 Installed.

Oct 10, 2014@09:45:35

Install Message Sent \#123412

Call MENU rebuild

Starting Menu Rebuild: Oct 10, 2014@09:45:37

Collecting primary menus in the New Person file...

Primary menus found in the New Person file

------------------------------------------

OPTION NAME MENU TEXT \# OF LAST LAST

USERS USED BUILT

XMUSER MailMan Menu 354 04/19/05 02/28/14

EVE Systems Manager Menu 25 02/28/14 02/28/14

PSZMGR Pharmacy 2 04/18/05 02/28/14

PSO OUTPUTS Output Reports 1 02/04/05 02/28/14

PSZTECH Pharmacy Technician's Menu 21 04/18/05 02/28/14

PSZPHARMACIST Pharmacist's Menu 24 04/19/05 02/28/14

PSZSUPER Pharmacy Supervisor's Menu 3 04/18/05 02/28/14

DGZMAO MAO MENU 5 04/19/05 02/28/14

DGZPTF PTF MENU 17 04/18/05 02/28/14

LRZMENU4 Laboratory Menu 9 04/19/05 02/28/14

LRZMENU5 Laboratory 18 04/19/05 02/28/14

LRZSUPERVISOR Laboratory Supervisor Menu 12 04/18/05 02/28/14

DGZSOCIALWORK MAS Social Work Menu 4 04/18/05 02/28/14

ZZADPSTAFFMENU ADP Staff Menu 21 04/18/05 02/28/14

DGZINQUIRY Patient Information Menu 8 04/18/05 02/28/14

FHZDIETETICS Dietetics Menu 1 04/18/05 02/28/14

DGZDOMTECH Domiciliary Menu 14 04/19/05 02/28/14

LRAPZSEC Anatomic Pathology Secret... 3 04/18/05 02/28/14

LRAPZTECH Anatomic Pathology Techni... 3 04/18/05 02/28/14

DENTZTECH Dental Clinic Menu 3 04/18/05 02/28/14

DGZCOORDINATORBACKUPMAS BACKUP APPLICATION CO... 3 04/18/05 02/28/14

DGZCLINICS ANCILLARY CLINIC MENU 9 04/18/05 02/28/14

DGZAMBULATORYCARE AMBULATORY CARE MENU 41 04/18/05 02/28/14

FHZDIET Clinical Dietetics Menu 7 04/18/05 02/28/14

FHZFOODSERVICE Food Service Menu 1 04/18/05 02/28/14

RAZ TECHMENU Radiology Technician Menu 26 04/19/05 02/28/14

RAZ FILEMENU Radiology File Room Clerk... 2 04/18/05 02/28/14

RAZ RPTENTRY Radiology Report Entry/Edit 2 04/18/05 02/28/14

PRCSCP OFFICIAL Control Point Official's ... 2 04/18/05 02/28/14

PRCSCP CLERK Control Point Clerk's Menu 6 04/18/05 02/28/14

ENZMGR Engineering Main Menu 3 04/18/05 02/28/14

ENZMR Engineering Menu 11 04/18/05 02/28/14

ENZPROGCLERK1 Engineering Main Menu 1 04/18/05 02/28/14

ENZPROGCLERK Engineering Main Menu 3 04/18/05 02/28/14

FHBUD Budget Asst. Menu 1 04/18/05 02/28/14

ENZMR1 Engineering Menu 1 04/18/05 02/28/14

PRCHUSER MASTER Combined A&MM Menus 2 04/18/05 02/28/14

PRCHUSER PA Purchasing Agent 5 04/18/05 02/28/14

PRCHUSER WHSE Warehouse 8 04/18/05 02/28/14

PRCF MASTER Funds Distribution & Acco... 7 04/18/05 02/28/14

PRCFA ACCTG TECH Accounting Technician Menu 8 04/18/05 02/28/14

PRCFA MASTER Accounting Program Menu 2 04/18/05 02/28/14

PRPF MASTER Patient Funds (INTEGRATED... 1 04/18/05 02/28/14

FHZADMCLERK Administrative Clerk Menu 1 04/18/05 02/28/14

DENTZTECH2 Dental Clinic Menu 8 04/18/05 02/28/14

RAZ PROFILES Patient Profile Menu 3 04/18/05 02/28/14

RTZ MAS-EXPED-MENU Expeditors Menu 8 04/18/05 02/28/14

PRCA CLERK MENU Clerk's AR Menu 1 04/18/05 02/28/14

RAZ OVERALL Radiology Total System Menu 2 04/18/05 02/28/14

RAZ RADIOLOGIST Radiologist Menu 9 04/18/05 02/28/14

RTZ MAS-SUPER-MENU MAS File Room Supervisor ... 1 04/18/05 02/28/14

DGZ ROI MENU Release of Information Menu 5 04/18/05 02/28/14

ENZMGR1 Engineering Menu 3 04/18/05 02/28/14

SROMENU Surgery Menu 3 04/18/05 02/28/14

DGZCLINICS NO LAB ANCILLARY CLINIC MENU (NO... 7 04/18/05 02/28/14

LRAP Anatomic pathology 2 04/18/05 02/28/14

PRCSCPZ OFFICIAL Control Point Official's ... 5 04/18/05 02/28/14

NURS-ADM Administrator's Menu 1 04/17/05 02/28/14

PRCHPM REQUISITION CLK MENU

Requisition Clerk Menu 1 04/18/05 02/28/14

ENZMR2 Engineering Main Menu 7 04/18/05 02/28/14

SOWK Information Management Sy... 3 04/18/05 02/28/14

DGZ OE/RR WARD MENU Ward Menu 37 04/19/05 02/28/14

LBRY MANAGER Library Management 2 04/18/05 02/28/14

CRCAZ MENU Scheduler Menu 1 04/18/05 02/28/14

SOWKZ SOCIAL WORKER Social Work Menu 27 04/18/05 02/28/14

SOWKZ CLERICAL MENU SWS Clerical Menu 1 04/18/05 02/28/14

YSZUSER MENTAL 11 MENU

MENTAL HEALTH SYSTEMS MENU 6 04/18/05 02/28/14

YSZUSER MENTAL 12 MENU

MENTAL HEALTH SYSTEMS MENU 15 04/18/05 02/28/14

SOWKZ CHIEF SWS CHIEF SWS MENU 1 04/18/05 02/28/14

QAZ XUCORE MENU Quality Mgt Menus 1 04/18/05 02/28/14

DGZ OE/RR LPN NURSING MENU

LPN NURSING MENU 58 04/19/05 02/28/14

CRCAZ APPLICATION COORDINATOR

Scheduler Application Coo... 1 04/15/05 02/28/14

YSZ NURSE MENU Mental Health Nurse Menu 1 04/18/05 02/28/14

DGZ OE/RR HN MENU HEAD NURSE MENU 31 04/19/05 02/28/14

DGZ OE/RR RN MENU WARD RN NURSING MENU 279 04/19/05 02/28/14

SOWKZ SUPERVISORS1 SWS Supervisors Menu with... 3 04/18/05 02/28/14

FHZDIETCLERK Food Service Worker Menu 22 04/18/05 02/28/14

PRCZ IFCAP IFCAP 1 04/15/05 02/28/14

ANRV VIST MENU VIST Menu 1 04/18/05 02/28/14

PRCAZ AR CLERK MENU Accounts Receivable Clerk... 3 04/18/05 02/28/14

SDZRMS USERS RMS MENU 23 04/18/05 02/28/14

DGZASSISTANT CHIEF MAS Assistant Chief Menu 2 04/18/05 02/28/14

FBAA MAIN MENU Fee Basis Main Menu 11 04/18/05 02/28/14

PRSD 05 EMPLOYEE INQUIRY MENU

Employee Inquiry/Reports ... 1 04/18/05 02/28/14

ZZ142BFILE552420 MENU1

MEDICAL MEDIA MANAGER'S MENU 3 04/18/05 02/28/14

GMTS USER Health Summary Menu 1 04/14/05 02/28/14

GMTS ENHANCED USER Health Summary Enhanced Menu 1 04/18/05 02/28/14

RMPR OFFICIAL Prosthetic Official's Menu 2 04/18/05 02/28/14

RMPR CLERK Prosthetic Clerk's Menu 1 04/18/05 02/28/14

NURSZ-NA Nursing Assistant Menu 100 04/19/05 02/28/14

IBZ CLERK MENU INTEGRATED BILLING CLERK ... 13 04/18/05 02/28/14

IBZ SUPERVISOR MENU INTEGRATED BILLING SUPER ... 1 04/18/05 02/28/14

ACKQAS SUPER A&SP Supervisor Menu 1 04/18/05 02/28/14

RMPRZ OFFICIAL MENU Prosthetic Official's Menu 3 04/18/05 02/28/14

RAZ TRANSCRIPTIONISTRadiology Transcriptionis... 1 04/18/05 02/28/14

FHZMGR Dietetics Management 4 04/18/05 02/28/14

RAZNM CLERKTRANSMENURadiology/Nuclear Med Cle... 1 04/18/05 02/28/14

RAZNM TECHMENU1 Radiology/Nuclear Med Tec... 3 04/18/05 02/28/14

QAOS USER MENU Occurrence Screen User Menu 1 04/18/05 02/28/14

HBHC INFORMATION SYSTEM MENU

HBPC Information System Menu 1 04/18/05 02/28/14

ORZ MAIN MENU CLINICIAN

Clinician Menu 11 04/18/05 02/28/14

ORZ ANCILLARY CLINICIAN MENU

Ancillary Clinician Menu 1 04/19/05 02/28/14

PRSA TK MENU TimeKeeper Main Menu 8 04/18/05 02/28/14

PRSA SUP MENU T&A Supervisor Menu 2 04/18/05 02/28/14

PRSA PAY MGR Payroll Supervisor Menu 1 04/18/05 02/28/14

PRSAZ PAY MENU Payroll Main Menu 4 04/18/05 02/28/14

ESP POLICE & SECURITY MENU

Police Menu 1 04/18/05 02/28/14

ESP POLICE CHIEF MENU

Police Chief 1 04/18/05 02/28/14

ESP POLICE CLERICAL Police Clerical 4 04/18/05 02/28/14

ESPZ POLICE OFFICER MENU

Police Officer 12 04/19/05 02/28/14

ESPZ POLICE SUPERVISOR

Police Supervisor 3 04/19/05 02/28/14

IBZ MANAGER Integrated Billing Master... 1 04/13/05 02/28/14

ORZ MAIN MENU CLIN DC

Clinician Menu 1 04/18/05 02/28/14

PSZLEADTECH Pharmacy Lead Technician'... 2 04/18/05 02/28/14

ZZMASPRIME CARE MENUPRIME CARE MENU 35 04/18/05 02/28/14

ORZ MAIN MENU CLINICIAN OE

Clinician Menu with Order... 435 02/21/14 02/28/14

PRCP PPM MENU Posted Stock Management 1 04/15/05 02/28/14

ECXMGR Extract Manager's Options 3 04/18/05 02/28/14

RAZ A/O Radiology Administrative ... 1 04/18/05 02/28/14

RMPR LAB MENU Prosthetic Lab Menu 1 04/18/05 02/28/14

DGZ OE/RR TRIAGE RN MENU

TRIAGE RN NURSING MENU 38 01/09/14 02/28/14

AGSVISN REFERRAL VISN Referral Menu 1 03/30/05 02/28/14

ZZMEDTRAN Transcription Contractor ... 12 04/18/05 02/28/14

DGZ MAS RECREATION MAS Recreation Menu 9 04/18/05 02/28/14

IBJ DIAGNOSTIC MEASURES MENU

Diagnostic Measures Reports 1 04/10/05 02/28/14

ZZADP CLINICALMAIN CLINICAL COORDINATOR MAIN... 2 04/18/05 02/28/14

LRZ CINCINNATI Lab menu for Cincinnati V... 8 04/15/05 02/28/14

DVBA VARO REMOTE DAYTON VA Regional Office... 18 04/18/05 02/28/14

ZZIRMFILE552315MENU IRM Staff Workload Menu 1 04/18/05 02/28/14

ECZ USER Event Capture Service Use... 10 04/18/05 02/28/14

AFVSQL ADMINISTRATORSQL ADMINISTRATOR MENU 1 04/18/05 02/28/14

AUOYSPD SPD OPTIONS SPD Equipment Tracking (T... 2 04/18/05 02/28/14

RCDP AGENT CASHIER MENU

Agent Cashier Menu 1 04/15/05 02/28/14

ZZIRM CIOFO SUPPORT CIOFO SUPPORT MENU 5 04/18/05 02/28/14

MAG SYS MENU Imaging System Manager Menu 1 04/18/05 02/28/14

ZZ111 RESPIRATORY THERAPIST

Respiratory Therapist Menu 22 04/18/05 02/28/14

XUZSPY Information Security Offi... 1 04/18/05 02/28/14

ZZ121 PROSTHETICS CHIEF

Prosthetics Chief Menu 2 04/18/05 02/28/14

ZZIRMAC DENTAL Dental AC Menu 1 04/18/05 02/28/14

ZZIRMAC NUC MED/RADIOLOGY

Nuclear Med & Radiology A... 1 04/18/05 02/28/14

ZZIRMAC MEDICAL Medical AC Menu 1 04/18/05 02/28/14

ZZIRMAC SURGICAL Surgical AC Menu 1 04/18/05 02/28/14

ZZIRMAC NURSING Nursing AC Menu 2 04/17/05 02/28/14

ZZIRMAC MHCL MHCL AC Menu 1 04/18/05 02/28/14

ZZIRMAC DSS DSS AC Menu 3 04/18/05 02/28/14

ZZIRMAC A&MMS A&MMS AC Menu 1 04/18/05 02/28/14

ZZIRMAC FISCAL Fiscal AC Menu 1 04/18/05 02/28/14

ZZ04 VOUCHERAUDIT MENU

Voucher Audit Menu 2 04/18/05 02/28/14

ZZIRMAC QUALITY MANAGEMENT

Quality Management AC Menu 1 04/18/05 02/28/14

ZZRA PACS ADMINISTRATOR

Radiology PACS Administrator 1 04/12/05 02/28/14

ASSHRCFPCC HRC First Party CC 134 04/18/05 02/28/14

Building secondary menu trees....

Merging.... done.

Install Completed