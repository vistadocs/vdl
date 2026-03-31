---
title: OR*3*350 Installation Guide CPRS GUI 30B
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: CPRS GUI 30B
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*350
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order la
audience: 
keywords: 
  - install
  - installation
  - table
  - contents
  - global
  - transport
  - patch
  - distribution
  - cprs
  - package
page_count: 0
word_count: 20086
section_count: 41
table_count: 22
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2016
revision_count: 1
revision_newest: 4/18/2016
revision_oldest: 4/18/2016
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_350_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_350_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>

  Computerized Patient Record System Graphical User Interface (CPRS GUI)
---

Installation Guide

Version CPRS 30.b

![](or-3-350-installation-guide-cprs-gui-30b/001.png)

April 2016

Office of Information & Technology (OI&T)

Product Development (PD)

This page left intentionally blank.

Revision History

| Date      | Version | Description                                                                                                                                                                                                                      | Author                             |
|-----------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 4/18/2016 | 1.1     | Corrected the location where dlls and other items need to be installed (various pages). Updated the list of required patches. Added information about the .ver file in conjunction with the MSP file for Gold Path installation. | <span class="mark">REDACTED</span> |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |
|           |         |                                                                                                                                                                                                                                  |                                    |

Table of Contents

This page purposely left blank.

# # Computerized Patient Record System Graphical User Interface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Computerized Patient Record System Graphical User Interface](#computerized-patient-record-system-graphical-user-interface)
  - [Overview](#overview)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [Document Conventions](#document-conventions)
  - [Related Documents](#related-documents)
- [Pre-requisites](#pre-requisites)
  - [Pre-requisite Patches](#pre-requisite-patches)
- [Software Retrieval](#software-retrieval)
- [CPRS v30.b Test System Installation Checklist](#cprs-v30b-test-system-installation-checklist)
- [# Installation Components](#installation-components)
  - [Additional Required Patches](#additional-required-patches)
    - [TIU\1\268 in Test](#tiu1268-in-test)
    - [GMPL\2\47 in Test](#gmpl247-in-test)
    - [GMPL\2\45 in Test](#gmpl245-in-test)
    - [PSJ\5\307 in Test](#psj5307-in-test)
    - [OR\3\350 in Test](#or3350-in-test)
    - [GMRV\5\28 in Test](#gmrv528-in-test)
    - [YS\5.01\116 in Test](#ys501116-in-test)
    - [XU\8\642 in Test](#xu8642-in-test)
    - [GMRC\3.0\81 in Test](#gmrc3081-in-test)
    - [GMTS\2.7\112 in Test](#gmts27112-in-test)
    - [OR\3.0\424 in Test](#or30424-in-test)
  - [ZIP File (OR30350.zip)](#zip-file-or30350zip)
  - [GMVVitalsViewEnter.DLL](#gmvvitalsviewenterdll)
    - [Manual Installation](#manual-installation)
    - [MSP Installation](#msp-installation)
  - [YSMHAAXE3.DLL](#ysmhaaxe3dll)
    - [Manual Installation](#manual-installation-1)
    - [MSP Installation](#msp-installation-1)
  - [CPRS GUI Executable Methods of Installation](#cprs-gui-executable-methods-of-installation)
    - [Network (Shared) Installation](#network-shared-installation)
    - [Citrix installation](#citrix-installation)
    - [Gold Path installation](#gold-path-installation)
    - [Direct Access to a Local Copy of CPRSChart.exe (bypassing the loader)](#direct-access-to-a-local-copy-of-cprschartexe-bypassing-the-loader)
    - [Manual installation](#manual-installation-2)
    - [Manual Installation](#manual-installation-3)
  - [ePCSDataEntryForPrescriber Installation](#epcsdataentryforprescriber-installation)
    - [Manual Installation](#manual-installation-4)
  - [CPRS Documentation](#cprs-documentation)
- [Post Install Instructions](#post-install-instructions)
  - [New Order Dialogs](#new-order-dialogs)
  - [ORWOR CATEGORY SEQUENCE Parameters](#orwor-category-sequence-parameters)
  - [YS MHAA DLL NAME Parameter](#ys-mhaa-dll-name-parameter)
  - [New Reports on Labs Tab](#new-reports-on-labs-tab)
  - [OR REPORT DATE SELECT TYPE Parameter](#or-report-date-select-type-parameter)
  - [Update for Dragon Naturally Speaking](#update-for-dragon-naturally-speaking)
  - [Consults Setup](#consults-setup)
    - [Parameter Update](#parameter-update)
    - [Input Template Change](#input-template-change)
    - [Local Data Objects Based on EARLIEST DATE](#local-data-objects-based-on-earliest-date)
  - [OR MOB DLL VERSION parameter](#or-mob-dll-version-parameter)
  - [One-Step Clinic Admin Setup Needed](#one-step-clinic-admin-setup-needed)
  - [CPRS and MED Fix](#cprs-and-med-fix)
- [CPRS v30 Production System Installation Checklist](#cprs-v30-production-system-installation-checklist)
  - [Additional Required Patches](#additional-required-patches-1)
    - [TIU\1\268 in Production](#tiu1268-in-production)
    - [GMPL\2\47 in Production](#gmpl247-in-production)
    - [GMPL\2\45 in Production](#gmpl245-in-production)
    - [PSJ\5\307 in Production](#psj5307-in-production)
    - [OR\3\350 in Production](#or3350-in-production)
    - [GMRV\5\28 in Production](#gmrv528-in-production)
    - [YS\5.01\116 in Production](#ys501116-in-production)
    - [XU\8\642 in Production](#xu8642-in-production)
    - [GMRC\3.0\81 in Production](#gmrc3081-in-production)
    - [GMTS\2.7\112 in Production](#gmts27112-in-production)
    - [OR\3.0\424 in Production](#or30424-in-production)
  - [ZIP File (OR30350.zip) in Production](#zip-file-or30350zip-in-production)
  - [GMVVitalsViewEnter.dll](#gmvvitalsviewenterdll-1)
    - [Manual Installation](#manual-installation-5)
    - [MSP Installation](#msp-installation-2)
  - [YSMHAAXE3.DLL](#ysmhaaxe3dll-1)
    - [Manual Installation](#manual-installation-6)
    - [MSP Installation](#msp-installation-3)
  - [CPRS GUI Executable Methods of installation](#cprs-gui-executable-methods-of-installation-1)
    - [Network (Shared) Installation](#network-shared-installation-1)
    - [Citrix installation](#citrix-installation-1)
    - [Gold Path installation](#gold-path-installation-1)
    - [Direct Access to a Local Copy of CPRSChart.exe (bypassing the loader)](#direct-access-to-a-local-copy-of-cprschartexe-bypassing-the-loader-1)
    - [Manual installation](#manual-installation-7)
    - [Manual Installation](#manual-installation-8)
  - [ePCSDataEntryForPrescriber Installation](#epcsdataentryforprescriber-installation-1)
    - [Manual Installation](#manual-installation-9)
  - [CPRS Documentation](#cprs-documentation-1)
- [Post Install Instructions](#post-install-instructions-1)
  - [New Order Dialogs](#new-order-dialogs-1)
  - [ORWOR CATEGORY SEQUENCE Parameters](#orwor-category-sequence-parameters-1)
  - [YS MHAA DLL NAME Parameter](#ys-mhaa-dll-name-parameter-1)
  - [New Reports on Labs Tab](#new-reports-on-labs-tab-1)
  - [OR REPORT DATE SELECT TYPE Parameter](#or-report-date-select-type-parameter-1)
  - [Update for Dragon Dictation Software](#update-for-dragon-dictation-software)
  - [Consults Setup](#consults-setup-1)
    - [Parameter Update](#parameter-update-1)
    - [Input Template Change](#input-template-change-1)
    - [Local Data Objects Based on EARLIEST DATE](#local-data-objects-based-on-earliest-date-1)
  - [OR MOB DLL VERSION parameter](#or-mob-dll-version-parameter-1)
  - [One-Step Clinic Admin Setup Needed](#one-step-clinic-admin-setup-needed-1)
  - [CPRS and MED Fix](#cprs-and-med-fix-1)
- [# # CPRS v30 M patches—Software Installation Samples](#cprs-v30-m-patchessoftware-installation-samples)
    - [TIU\1\268 Install Capture](#tiu1268-install-capture)
    - [GMPL\2.0\47 Install Capture](#gmpl2047-install-capture)
    - [GMPL\2.0\45 Install Capture](#gmpl2045-install-capture)
    - [PSJ\5\307 Install Capture](#psj5307-install-capture)
    - [OR\3\350 Install Capture](#or3350-install-capture)
    - [GMRV\5\28 Install Capture](#gmrv528-install-capture)
    - [YS\5.01\116 Install Capture](#ys501116-install-capture)
    - [XU\8\642 Install Capture](#xu8642-install-capture)
    - [GMRC\3.0\81 Install Capture](#gmrc3081-install-capture)
    - [GMTS\2.7\112 Install Capture](#gmts27112-install-capture)
    - [OR\3.0\424 Install Capture](#or30424-install-capture)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

This installation guide deals specifically with the installation of CPRS GUI v30.B (patch OR\*3.0\*350) and its associated patches and Windows application. CPRS GUI v30.B addresses patient safety enhancements related to the display of Lab Test Status, Clinic Orders, Supply Orders, as well as 508 modifications, Remedy tickets and other patient safety corrections.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) Information Resource Management (IRM) staff.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation guide provides instructions for:

- Installing application components that run on M servers at VAMC facilities
- Installing Windows executable programs on workstations or application servers at VAMC facilities
- Performing post-installation tasks—including configuration tasks—that require knowledge of the underlying VistA system

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

The following documents, in addition to this document, will be available on the VA Software Document Library (VDL) when the patch is ready for release:

Please see section 5.8, CPRS Documentation.

[CPRS on the VDL](http://www.va.gov/vdl/application.asp?appid=61)

# Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the processes described in this document the tasks outlined in this section must be completed.

1.  Read through this entire document. Each patch may have tasks that must be accomplished before the patch is installed and may have tasks for after installation as well. Reading through the instructions will also help each site know the individuals with whom they will need to coordinate.
2.  Coordinate with needed staff. You may need some or all of the following staff. If you are not sure, now is the time to verify who will be responsible for which tasks and when they will be needed.
- local IRM personnel or Region IT representative for server-side patch installations
- personnel to distribute the CPRSChart.exe Graphical User Interface (GUI) software either to a server (if you run it from there), or to individual workstations
- If your site uses Citrix servers, you will need to coordinate with the staff that maintain those servers so that client and server versions are synchronized.
- Clinical application coordinators (CACs)or ADPACs for various applications
3.  Perform all pre-installation tasks.

## Pre-requisite Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please check your system to verify that the following, previously released national patches are installed:

- GMPL\*2\*42
- GMPL\*2\*28
- GMPL\*2\*44
- GMRC\*3\*76
- GMRC\*3\*85
- GMTS\*2.7\*90
- GMTS\*2.7\*96
- LEX\*2.0\*86
- OR\*3\*121
- OR\*3\*157
- OR\*3\*311
- OR\*3\*312
- OR\*3\*317
- OR\*3\*318
- OR\*3\*322
- OR\*3\*341
- OR\*3\*348
- OR\*3\*349
- OR\*3\*356
- OR\*3\*363
- OR\*3\*366
- OR\*3\*374
- OR\*3\*385
- OR\*3\*388
- OR\*3\*389
- OR\*3\*392
- OR\*3\*394
- OR\*3\*418
- PSJ\*5\*267
- PSJ\*5\*311
- TIU\*1\*211
- TIU\*1\*239
- XU\*8\*609

# Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS GUI version 30.B consists of supporting patches from other projects (listed in Table 2 Additional Patches, below), the patch OR_30_350.KID, and the OR_30_350.ZIP file along with its supporting installation documents (all listed in Table 3 CPRS v30.b files

, below).

For national deployment, sites will download files from a Secure FTP site. The table below lists the files that will be distributed. CPRS v.30.b will be distributed using a controlled deployment over several months. Sites will be put in groups or waves and given a time period in which to install the software. Each site will be contacted regarding when their time is to install and further instructions will be given. Deploying in this manner ensures that CPRS development staff can be available, if needed, to help with the installation process.

PackMan messages will be sent to sites or regional support personnel through Forum. Sites will download Host files and zip files from a controlled Secure File Transfer Protocol (SFTP). The necessary installation files are:

Table 2 Additional Patches

| Additional Required Patches to be downloaded | Supported Functionality                            | Host/Packman |
|----------------------------------------------|----------------------------------------------------|--------------|
| TIU_1_268.KID                                | TIU support                                        | Host         |
| GMPL_2_47.KID                                | Problem List                                       | Host         |
| GMPL_2_45.KID                                | Problem List                                       | Host         |
| YS_501_116.KID                               | Mental Health                                      | Host         |
| MHA_501_116.ZIP                              | Mental Health DLL                                  | ZIP File     |
| PSJ_5_307.KID                                | Clinic Orders Support                              | Host         |
| GMRV_5_28.KID                                | Vitals DLL Support                                 | Host         |
| VITL5_P28.ZIP                                | Vitals                                             | ZIP File     |
| XU8P642.KID                                  | Timeout to assist with PKI Verify Service Failover | Host         |
| XU_8_0_P641.ZIP                              | ePCS GUI tool                                      | ZIP File     |
| GMRC_30_81.KID                               | Name Change for Consults Earliest Date             | Host         |
| GMTS_27_112.KID                              | Health Summary support for GMRC\*3.0\*81           | Host         |
| OR_30_424.KID                                | Follow up to patch OR\*3.0\*350                    | Host         |

Table 3 CPRS v30.b files

| CPRS v30 files to be downloaded | File Contents / Supported Functionality                                                   |
|---------------------------------|-------------------------------------------------------------------------------------------|
|                                 |                                                                                           |
| OR_30_350.KID                   | M changes for CPRS v30.B                                                                  |
| OR_30_350.ZIP                   | CPRS executable, CPRS Help file directory, Vitals DLL, Mental Health DLL and OrderCom.DLL |

# CPRS v30.b Test System Installation Checklist

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
<td colspan="3">Test/Mirror System Installation</td>
</tr>
<tr class="even">
<td><ol type="1">
<li></li>
</ol></td>
<td>If you are ready for the released version and you do not already have access to the released version, contact <mark>REDACTED</mark> at <mark>REDACTED</mark> or the <a href="mailto:OITPDCPRSImplementationTeam@va.gov?subject=access%20to%20released%20version%20of%20CPRS%2030.b">OIT PD CPRS Implementation Team</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td><p>Confirm all Pre-requisite patches have been installed in your Test/Mirror system:</p>
<p>Please check your system to verify that the following, previously released national patches are installed:</p>
<ul>
<li><p>GMPL*2*42</p></li>
<li><p>GMPL*2*28</p></li>
<li><p>GMPL*2*44</p></li>
<li><p>GMRC*3*76</p></li>
<li><p>GMRC*3*85</p></li>
<li><p>GMTS*2.7*90</p></li>
<li><p>GMTS*2.7*96</p></li>
<li><p>LEX*2.0*86</p></li>
<li><p>OR*3*121</p></li>
<li><p>OR*3*157</p></li>
<li><p>OR*3*311</p></li>
<li><p>OR*3*312</p></li>
<li><p>OR*3*317</p></li>
<li><p>OR*3*318</p></li>
<li><p>OR*3*322</p></li>
<li><p>OR*3*341</p></li>
<li><p>OR*3*348</p></li>
<li><p>OR*3*349</p></li>
<li><p>OR*3*356</p></li>
<li><p>OR*3*363</p></li>
<li><p>OR*3*366</p></li>
<li><p>OR*3*374</p></li>
<li><p>OR*3*385</p></li>
<li><p>OR*3*388</p></li>
<li><p>OR*3*389</p></li>
<li><p>OR*3*392</p></li>
<li><p>OR*3*394</p></li>
<li><p>OR*3*418</p></li>
<li><p>PSJ*3*267</p></li>
<li><p>PSJ*5*311</p></li>
<li><p>TIU*1*211</p></li>
<li><p>TIU*1*239</p></li>
<li><p>XU*8*609</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Attend the CPRS v30.b Training session</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#tiu1268-in-test">TIU*1*268 in test</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td>Complete the <a href="#GMPL47_preinstall">Preinstallation Step for GMPL*2*47</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Read the <a href="#GMPL_pre_post_install_overvw">Pre/Post Installation Overview for patch GMPL*2*47</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="7" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmpl247-in-test">GMPL*2*47 in test</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="8" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmpl245-in-test">GMPL*2*45 in test</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="9" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#psj5307-in-test">PSJ*5*307 in test</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="10" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#or3350-in-test">OR*3.0*350</a> in test.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="11" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmrv528-in-test">GMRV*5*28 in test</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="12" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#ys5.01116-in-test">YS*5.01*116 in test</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="13" type="1">
<li></li>
</ol></td>
<td>Unzip and then install the files in <a href="#ys_mha_a_xe3.dll">MHA_501_116.ZIP in test</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="14" type="1">
<li></li>
</ol></td>
<td>Unzip and install the contents of <a href="#gmv_vitalsviewenter.dll">VITL5_P28.ZIP in test</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="15" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#xu8642-in-test">XU*8*642 in test</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="16" type="1">
<li></li>
</ol></td>
<td>Unzip and install the contents of <a href="#epcsdataentryforprescriber-installation">XU_8_0_P641.ZIP</a> in test.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="17" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmrc3.081-in-test">GMRC*3.0*81 in test</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="18" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmts2.7112-in-test">GMTS*2.7*112 in test</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="19" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#or3.0424-in-test">OR*3.0*424 in test</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="20" type="1">
<li></li>
</ol></td>
<td>Download CPRS GUI installation package OR_30_350.zip (see Section 5.2, ZIP File (OR_30_350.zip), below), install per the instructions in that section, and point user shortcuts to your Test/Mirror system</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="21" type="1">
<li></li>
</ol></td>
<td>Install the <a href="#order-com-dll-installation">Ordercom DLL</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="22" type="1">
<li></li>
</ol></td>
<td><p>Install the <a href="#epcsdataentryforprescriber-installation">ePCS Data Entry for Prescriber GUI</a>.</p>
<p><strong>Note:</strong> This should only be installed on workstations for users that set up providers to order controlled substances.</p></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="23" type="1">
<li></li>
</ol></td>
<td>If you have not already, place the CPRS documentation in a location where CPRS users and support personnel can access it.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="24" type="1">
<li></li>
</ol></td>
<td>Add the new <a href="#new-order-dialogs">ORDER DIALOGS</a> to any appropriate order menus so that your users can place clinic orders, and supply orders.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="25" type="1">
<li></li>
</ol></td>
<td>If you do NOT use the Package level for the ORWOR CATEGORY SEQUENCE parameter, <a href="#orwor-category-sequence-parameters">create new Instances for this parameter in order for the new orders in the CLINIC MEDICATIONS, CLINIC INFUSION and SUPPLIES/DEVICES display groups to be labeled properly</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="26" type="1">
<li></li>
</ol></td>
<td>Set the name of the correct version of the <a href="#ys-mha_a-dll-name-parameter">Mental Health DLL</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="27" type="1">
<li></li>
</ol></td>
<td>Review the ORWRP REPORT LAB LIST parameter to determine if you have set it at the System, Division or User level. If you have it set at these levels, then <a href="#new-reports-on-labs-tab">edit the parameter to add the new reports</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="28" type="1">
<li></li>
</ol></td>
<td>Check the <a href="#or-report-date-select-type-parameter">OR REPORT DATE TYPE</a> parameter and set it for how your site wants the date selection to display on the Reports and Labs tabs in CPRS.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="29" type="1">
<li></li>
</ol></td>
<td>If your site uses Dragon dictation software, <a href="#update-for-dragon-naturally-speaking">add to the .ini file</a> to ensure that Dragon works correctly with CPRS.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="30" type="1">
<li></li>
</ol></td>
<td>Check the <a href="#consults-setup">Consults Configuration</a> and complete any set up necessary.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="31" type="1">
<li></li>
</ol></td>
<td>Check the <a href="#or-mob-dll-version-parameter">OR MOB DLL VERSION</a> parameter to ensure it is the latest version of the Med Order button dynamic link library (DLL).</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="32" type="1">
<li></li>
</ol></td>
<td>For the appropriate users, complete the <a href="#one-step-clinic-admin-setup-needed">One-Step Clinic Admin setup</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="33" type="1">
<li></li>
</ol></td>
<td>For workstations that use the <a href="#cprs-and-med-fix">Mobile Electronic Documentation (MED)</a> software, make the necessary changes to make it work with CPRS 30.b.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="34" type="1">
<li></li>
</ol></td>
<td>Check all your institutions to verify the Facility DEA # and Facility DEA # Expiration date is correct in the INSTITUTION file (#4).</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="35" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Test/Mirror system has been successful. You can use the <a href="http://vista.med.va.gov/cprs/docs/30_smoke_test/V30_Smoke_Test_Script.xls">V30_Smoke_Test_Script.xls</a> document to ensure that the patches have been installed correctly.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="36" type="1">
<li></li>
</ol></td>
<td>Complete testing of CPRS 30.b in your Test/Mirror system.</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# # Installation Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of CPRS 30.b includes server-side patches, GUI executables, and dynamic link libraries (DLLs).

## Additional Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For CPRS to function correctly, it is necessary that some patches be installed immediately prior to the installation of CPRS v30.B and some patches should be installed after the CPRS 30.B patch. These will be distributed with CPRS v30.B (see Section 3, , above), and they should be installed in the order delineated in the following sections.

### TIU\*1\*268 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can be loaded with users in the system. Installation time

will be less than 2 minutes.

1\. Download the TIU_1_268.KID file from the appropriate Server to a directory on your system.

2\. On the KIDS INSTALLATION menu, use the LOAD A DISTRIBUTION option, and enter the location of the Host File.

\[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

3\. From this menu, you may elect to use the following options

(When prompted for the INSTALL NAME, enter "TIU\*1.0\*268"):

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of this

patch (routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

4\. Use the Install Package(s) option and select the package.

a\. When prompted "Want KIDS to INHIBIT LOGONs during the

install? NO//", answer NO.

b\. When prompted "Want to DISABLE Scheduled Options and Menu

Options and Protocols? NO//", answer NO.

### GMPL\*2\*47 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="GMPL_pre_post_install_overvw" class="anchor"></span>Pre/Post Installation Overview:

-------------------------------

In order to prevent hard errors and unnecessary Mailman messages from

generating during the Clinical Reminder Problem file reindex process,

Reminder Evaluations will be automatically disabled prior to indexing

and re-enabled after successful completion. This entire process (indexing/disabling/enabling) will be tasked and automated in a post-installation routine (GMPLY47).

\*\*IMPORTANT NOTE\*\*: Once Reminder Evaluations are temporarily disabled,

certain functional areas such as, the CPRS coversheet, Reminder Dialog

Branching Logic, HS Report for Reminders, TIU/HS Objects for Reminders,

and Reminder Order Checks will not function correctly.

Users trying to access these functional areas during the reindexing

process, may receive various error/warning messages. For example,

Reminder Dialogs will be turned off and display the following message:

"Dialog is disable for reminder re-indexing". Reminder Order Checks will

display the message: "Clinical Reminder evaluation is currently disabled;

this order check cannot be processed". Coversheet Reminders will have a

status of CNBD (Cannot Be Determined). HS Clinical Reminder components

will either be blank or contain a status of CNBD.

<span id="GMPL47_preinstall" class="anchor"></span>Pre-Installation Instructions:

------------------------------

To ensure that the installer receives the appropriate notification

messages in MailMan, please verify that the installer is added as a

member to the mailgroup that is defined in the REMINDER MANAGEMENT

MAILGROUP field \#3 of the CLINICAL REMINDER PARAMETERS file \#800.

Installation Instructions:

--------------------------

This patch loads several routines and may be installed with users on

the system although it is recommended that it be installed during

non-peak hours to minimize potential disruption to users. This patch

should take less than 1 minute to install.

However depending on the size of your site's Problem file, it could take

1-1.5 hours for the reindexing process to complete. As an example, for a

site that has 3 million entries in the Problem file, it took the

reindexing process 1 hr to complete.

\*\*IMPORTANT NOTE\*\*: Given this information and the fact that reminder

evaluations will be temporarily disabled, it is STRONGLY RECOMMENDED

that at least 1-1.5 hrs. is allocated for the completion of the reindex

and that this be installed during afterhours to minimize disruption to

users.

1\. Download the GMPL_2_47.KID file from the appropriate Server to a directory on your system.

2\. On the KIDS INSTALLATION menu, use the LOAD A DISTRIBUTION option, and enter the location of the Host File.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter the patch

GMPL\*2.0\*47.

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//', response with NO.

6\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//', respond with NO.

Post-Installation Instructions:

-------------------------------

The post-install routine will call a Reminders API to reindex and clean

up any outstanding ACRMT indexes that didn't get disposed of

appropriately. It will also create a new auxiliary cross-reference, ACRMTA, for the Mapping Target multiple.

The post-install routine will also automatically disable the reminder

evaluations prior to executing the reindex process. A MailMan message

should be generated to the installer and Clinical Reminder mailgroup

confirming so:

Subj: REMINDER EVALUATION DISABLED \[#68774\] 08/21/15@12:37 13 lines

From: POSTMASTER (Sender: INSTALLER,ONE) In 'IN' basket. Page 1

--------------------------------------------------------------------------

Reminder evaluation was disabled on Aug 21, 2015@12:37:43.

Because of this, the following TaskMan jobs can produce erroneous results.

Pending jobs should not be allowed to start until evaluation is enabled.

The results of running jobs should be discarded and if possible, running

jobs should be stopped.

Reason: index rebuild for file \#9000011.

Reminders Due Report Jobs

Reminder Patient List Jobs

Reminder Extract Jobs

Once the re-indexing process is complete, a Problem List Reindex Complete

notification message should be generated to the installer and Reminder

mailgroup indicating so. The below example is taken from a development

account and does not accurately reflect actual production times.

Subj: Index for global ^AUPNPROB( successfully built \[#68773\]

08/21/15@12:37

5 lines

From: INSTALLER,ONE In 'IN' basket. Page 1

--------------------------------------------------------------------------

Build of Clinical Reminders index for global ^AUPNPROB( completed.

Build finished at 08/21/2015@12:37:44

131 entries were created.

Elapsed time: 1 secs

0 errors were encountered.

Once the reindexing process has successfully completed, the reminder

evaluations will automatically be re-enabled. A MailMan message

should be generated to the installer and Reminder mailgroup confirming so:

Subj: REMINDER EVALUATION ENABLED \[#68775\] 08/21/15@12:37 2 lines

From: POSTMASTER (Sender: INSTALLER,ONE) In 'IN' basket. Page 1

--------------------------------------------------------------------------

Reminder evaluation was enabled on Aug 21, 2015@12:37:55.

It was disabled on Aug 21, 2015@12:37:43.

### GMPL\*2\*45 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 1 minute to install.

> 1\. Download the GMPL_2_45.KID file from the appropriate Server to a directory on your system.

> 2\. On the KIDS INSTALLATION menu, use the LOAD A DISTRIBUTION option, and enter the location of the Host File and enter the location of the Host File GMPL_2_45.KID

3\. From the same menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter GMPL\*2.0\*45)

a\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

b\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

c\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of

this patch (routines, DD's, templates, etc.).

d\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DD's or templates.

4\. Use the Install Package(s) option and select the package

GMPL\*2.0\*45

5\. When Prompted "Want KIDS to INHIBIT LOGONs during the install?

NO//" respond NO.

6\. When Prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//" respond NO.

### PSJ\*5\*307 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview:

-------------------------------

This patch is being released as a part of the CPRS v30 phased release. Specific instructions on downloading the software will be distributed when your site is scheduled to install.

Pre-Installation Instructions:

------------------------------

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. Specifically, this patch should not be installed during heavy usage times for Clinic Orders or BCMA Med

Order Button orders. This patch should take less than 5 minutes to install.

Installation Instructions:

--------------------------

1\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the

location of the Host File PSJ_5_307.KID.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter the patch

PSJ\*5.0\*307:

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? NO//', respond NO.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//', respond NO.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//', respond NO.

8\. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

### OR\*3\*350 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 1 minute. Users may remain on the system.

> **NOTE:** When installing patch OR\*3\*350, sites may notice a message that shows that they are missing patch OR\*3\*237, but this is incorrect. The reason is that patch OR\*3\*243 did not list patch 237 although it should have. Patch OR\*3\*350 does list patch 237 in the second line as it should.

1\. Download the OR_30_350.KID file from the appropriate Server to a directory on your system.

2\. On the KIDS INSTALLATION menu, use the LOAD A DISTRIBUTION option, and enter the location of the Host File.

3\. From this menu, you may elect to use the following options

a\. Backup a Transport Global

b\. Compare Transport Global to Current System

c\. Verify Checksums in Transport Global

4\. Use the Install Package(s) options and select the package OR\*3.0\*350.

5\. At the “Want to RUN the Environment Check Routine?”, respond YES.

6\. When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install?”, respond NO.

7\. When prompted Please select the recipients for the NON-VA MEDICATION COMPLEX QUICK ORDER DIALOG REPORT below.

> Send mail to:

> Enter the name of person who should receive this report, such as a CAC at the site.

> Select basket to send to:

> Respond IN//.

7\. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'

respond NO.

8\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//', respond NO.

### GMRV\*5\*28 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

==========================

1.  Download the GMRV_5_28.KID file from the appropriate server to a directory on your system.
2.  Load the KIDS distribution that is contained in file GMRV_5_28.KID using the Load a Distribution option on the Installation menu.
3.  Start up the Kernel Installation and Distribution System Menu \[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

4.  From this menu, you may elect to use the following options: (When prompted for the INSTALL NAME, enter GMRV\*5.0\*28):
    1.  Backup a Transport Global -This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
5.  Use the Install Package(s) option and select the package GMRV\*5.0\*28.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options and Menu Options and Protocols? NO//', answer NO.

### YS\*5.01\*116 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 1 minute to install.

1.  Download the YS_501_116.KID file from the appropriate server to a directory on your system.
2.  From the Kernel Installation & Distribution System menu, select

the Installation menu.

3\. From this menu, choose to Load a Distribution and enter the

location of the Host File YS_501_116.KID

4\. From the same menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter YS\*5.01\*116)

a\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

b\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of

this patch (routines, DD's, templates, etc.).

5\. Use the Install Package(s) option and select the package

YS\*5.01\*116

6\. When Prompted "Want KIDS to INHIBIT LOGONs during the install?

NO//" respond NO.

7\. When Prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//" respond NO.

### XU\*8\*642 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system. This patch should take less than 1 minute to install. It may be queued for installation.

There are no options that need to be disabled.

1\. Download the XU8P642.KID file from the appropriate Server to a directory on your system.

2\. On the KIDS INSTALLATION menu, use the LOAD A DISTRIBUTION option, and enter the location of the Host File.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch XU\*8.0\*642

a\. Print Transport Global - This option lets you print the contents

of a Transport Global that is currently loaded in the ^XTMP

global.

b\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

c\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

d\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? NO//' answer "NO".

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' answer "NO".

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//' answer "NO".

8\. If prompted 'Delay Install (Minutes): (0 - 60): 0//' answer "0".

### GMRC\*3.0\*81 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview:

-------------------------------

The pre-install will remove the current data dictionary for the

REQUEST/CONSULTATION file (#123). The new data dictionary, containing

the renamed CLINICALLY INDICATED DATE field, will be installed during

the KIDS installation. The patch does not contain any automated

post-install actions.

Pre-Installation Instructions:

------------------------------

This patch will overwrite the GMRC SETUP REQUEST SERVICE entry in the

INPUT TEMPLATE file. If your site has made any local modifications to

this input template, they should be captured prior to installing

GMRC\*3.0\*81, and then restored soon after.

LOCAL OBJECTS BASED ON EARLIEST DATE

====================================

If your site has created any local data objects based on the EARLIEST DATE

field, those objects will continue to function normally. However, it is

likely that the displayed name/header for such an object would need to be

updated to reflect that the underlying field name has changed from

EARLIEST DATE to CLINICALLY INDICATED DATE.

This patch may be installed with users on the system although it is

recommended that it be installed during non-peak hours to minimize

potential disruption to users. This patch should take less than 5

minutes to install.

1.  Download the GMRC_30_81.KID file from the appropriate server to a directory on your system.
2.  From the Kernel Installation & Distribution System menu, select

the Installation menu.

3\. From this menu, choose to Load a Distribution and enter the

location of the Host File GMRC_30_81.KID

4\. From the same menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter GMRC\*3.0\*81)

a\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

b\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

c\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of

this patch (routines, DD's, templates, etc.).

d\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DD's or templates.

5\. Use the Install Package(s) option and select the package

GMRC\*3.0\*81

6\. When Prompted "Want KIDS to INHIBIT LOGONs during the install?

NO//" respond NO.

7\. When Prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//" respond NO.

Post install instructions

------------------------------------

If your site has local objects based on the EAD field, ensure that

relevant end user displays are updated appropriately. Reference note above

entitled LOCAL OBJECTS BASED ON EARLIEST DATE.

### GMTS\*2.7\*112 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview:

-------------------------------

This patch does not contain any automated pre-install actions.

The post-install will add the missing components to the Patient Data Exchange (PDX) and also

update the DESCRIPTION field of the Consults Brief health summary component (CNB).

Pre-Installation Instructions:

------------------------------

This patch may be installed with users on the system although it is

recommended that it be installed during non-peak hours to minimize

potential disruption to users. This patch should take less than 5

minutes to install.

1.  Download the GMTS_27_112.KID file from the appropriate server to a directory on your system.
2.  From the Kernel Installation & Distribution System menu, select

the Installation menu.

3\. From this menu, choose to Load a Distribution and enter the

location of the Host File GMTS_27_112.KID

4\. From the same menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter GMTS\*2.7\*112

a\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

b\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

c\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of

this patch (routines, DD's, templates, etc.).

d\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DD's or templates.

4\. Use the Install Package(s) option and select the package

GMTS\*2.7\*112

5\. When Prompted "Want KIDS to INHIBIT LOGONs during the install?

NO//" respond NO.

6\. When Prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//" respond NO.

Post-Installation Instructions:

-------------------------

GMTSP112 may be deleted from the system once all patch functionality has been verified as working as expected.  IT staff may choose to keep a copy of this routine for future reference.

### OR\*3.0\*424 in Test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

-------------------------

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 1 minute to install.

1\. Download the OR_30_424.KID file from the appropriate Server to a directory on your system.

2\. On the KIDS INSTALLATION menu, use the LOAD A DISTRIBUTION option, and enter the location of the Host File.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch

OR\*3.0\*424.

a\. Print Transport Global - This option lets you print the contents

of a Transport Global that is currently loaded in the ^XTMP

global.

b\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

c\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

d\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install: OR\*3.0\*424.

5\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' Answer 'NO'

6\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//' Answer 'NO'

## ZIP File (OR_30_350.zip)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the CPRS GUI executable file as well as the DLLs associated with 30B, Vitals, Mental Health and One-Step Clinic Admin.

Download the ZIP file and extract all the files.

Placement of DLLs:

The DLLs are no longer required to reside on individual workstations. For example, if you are doing a network install of the CPRSChart executable, you can place the DLLs in that same directory.

2.  Some sites have experienced unacceptable delays in launching the DLLs if they are located on the server. If this occurs, the DLLs should be placed on the local workstations.

Here is the hierarchy the CPRS GUI uses to search for the DLLs:

1.  The same folder as the application
2.  A “Common Files\\ folder in the same folder as the application
3.  Windows 7:
- For 64 bit machines: “C:\Program Files (x86)\Vista\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files”

## GMV_VitalsViewEnter.DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IMPORTANT!The new Vitals DLL is NOT backwards compatible, meaning the new DLL cannot be used to enter vitals information in a previous version of CPRS. For those workstations that will access both CPRS 30.b and a previous version (such as a workstation testing CPRS in a test account, but also accessing the previous version in production), you MUST BACK UP and USE THE PREVIOUS VERSION for production while using the new version for test. When CPRS 30.b is in production, you can switch to the new DLL and delete the previous version.

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Unzip the VITL5_P28.ZIP file and move the files to an appropriate directory and/or workstations.

Windows 7:

- For 64 bit machines: “C:\Program Files (x86)\Vista\\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files”

If you are running the Vitals Lite DLL files from individual workstations and you want to push the files using SCCM, you should include the files from the VITL5_P28.zip in your script.

1.  Place the batch file (without the ;1) in the same folder as the vitals lite DLL.
2.  Rename the version 29 DLL (date of 1/21/2011) to GMV_VitalsViewEnter.dll.bkup29.
3.  If not already, rename the version 30 DLL (date of 11/05/2013) to GMV_VitalsViewEnter.dll.
4.  Both of these files should be in the same folder (see *fig 1*).

fig 1

![](or-3-350-installation-guide-cprs-gui-30b/002.png)

5.  Right click on the batch file and select “send to” then “desktop” (see *fig 2*).

fig 2

![](or-3-350-installation-guide-cprs-gui-30b/003.png)

6.  Now this batch can be run via the shortcut on the desktop.

When running the batch you will see the following question:

Do you want to test the new Vitals DLL with CPRS30: (y/n)

Answering Yes or Y will setup the version 30 DLL for testing. Answering No or N will setup the version 29 DLL for testing.

If you have any questions please feel free to email <span class="mark">REDACTED</span> or the [OIT PD CPRS Implementation Team](mailto:OITPDCPRSImplementationTeam@va.gov?subject=access%20to%20released%20version%20of%20CPRS%2030.b).

### MSP Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals DLL will be included in the v30 msp file. But, for test installations, it is expected you will be using the manual installation.

## YS_MHA_A_XE3.DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Unzip the MHA_501_116.ZIP file and move the files to an appropriate directory and/or workstations.

> Windows 7:

- For 64 bit machines: “C:\Program Files (x86)\Vista\\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files”

  Note: You may need to have a user with Administrator rights complete this step.

### MSP Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health DLL will be included in the v30 MSP file. But, for test installations, it is expected you will be using the manual installation.

## CPRS GUI Executable Methods of Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following methods of installation of CPRS are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

### Network (Shared) Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPRSChart.exe) across the LAN.

> The GUI executable (CPRSChart.exe), and ancillary files (DLLs, Help files etc.), are copied to a network shared location. Users are provided with a desktop shortcut to run CPRSChart.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the “Target” field of the shortcut properties

> At the time of a CPRS version update the copy of CPRSChart.exe (and any updated ancillary files) is simply replaced, on the network share, with the new version.

> Any users requiring access to another site's CPRS system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of CPRS (e.g. during a phased deployment, when sites are temporarily not all on the same version, or for testing purposes) a different version of CPRSChart.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

> Note: The version of CPRSChart a user executes must always match the patch-level version of the VistA system targeted.

### Citrix installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The GUI executable (CPRSChart.exe) and ancillary files (DLLs, Help files etc.) are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

> During a phased deployment of a new version of CPRS, if a Citrix Farm is serving users who are scheduled to deploy at different times, the Farm administrator may be required to temporarily maintain hosts with both the old and the new versions of CPRSChart.exe available.

### Gold Path installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is the “standard” method of installation where the GUI executable (CPRSChart.exe), and ancillary files (DLLs, Help files etc.), are installed on and run from the user's local workstation. In normal day-to-day operation, the user's shortcut executes a locally installed copy of CPRSLoader.exe which looks in a pre-configured network “Gold Path” (specified in a command line parameter) to see if there is a later version of CPRSChart.exe ready to be installed. If not, then execution passes to the locally installed version of CPRSChart.exe. If an updated version is found on the Gold Path, then a silent installation of the new version takes place, following which the newly installed version of CPRSChart.exe is executed on the local workstation.

> This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file (CPRSLoader.msi) to each user's workstation, typically accomplished via SCCM. This is outside the scope of CPRS development. A National package (CPRS Loader 1.30.40) has been prepared and made available to Regional COR Client Technologies leadership.

> The CPRS Loader installation package can be found on the System Center Configuration Manager (SCCM) central site at the following locations.

> Package Name: 1VA - VA CPRS Loader

> Package ID: 1VA004E7, R03002C4

> Test Location:  
> VA Central Site Packages \> Test \> 1VA - VA CPRS Loader

> Production Location:  
> VA Central Site Packages \> Production \> 1VA – Applications \> 1VA - VA CPRS Loader

All details of the SCCM package can be found in the build document and should be reviewed before deployment:  
[http://vaww.eie.va.gov/SysDesign/CS/Shared Documents/Build Documents/Application Tier 3 and 4/ESE VA CPRS Loader Build Document.pdf](http://vaww.eie.va.gov/SysDesign/CS/Shared%20Documents/Build%20Documents/Application%20Tier%203%20and%204/ESE%20VA%20CPRS%20Loader%20Build%20Document.pdf)

> The CPRSChart.exe component of the update is held in a Microsoft Software Patch (MSP) file (CPRSChart.msp) which is copied to the network Gold Path location—that should be all that is required for a normal CPRS version update for sites using this method. The exception is if a new version of CPRS Loader is also being released, in which case the cycle begins again with the distribution to users' workstations of the new CPRSLoader.msi (before the new CPRSChart.msp is copied to the network Gold Path)—this is the circumstance in which CPRS v30b is being released.

> The CPRS deployment software distribution will include an appropriate version of the CPRS Microsoft patch file (named CPRS_XX_YY.msp, where XX is the current version number for CPRS, and YY is the current build number.  At this point the current file name is CPRS_30_72.msp).  This file has the named version of CPRSChart embedded within it, along with any updated ancillary files.  Also included in the deployment software distribution will be a .VER file.  This file will have the same name as the MSP file, with only the file extension changed.  As an example, the .VER file for CPRS_30_72.MSP will be named CPRS_30_72.VER.  To be effective, the .VER file must be placed in the same Gold Path in which the .MSP file was placed.  The .VER is optional but beneficial.  It will allow the CPRS loader to much more quickly find an appropriate version of CPRSChart.exe for use with the current VistA system.  Including the VER file in the Gold Path can shorten CPRS start times substantially.

> For the convenience of local System Administrators, the file CPRSLoader.msi is also included in the release package, in case they need to manually install it on a workstation.

### Direct Access to a Local Copy of CPRSChart.exe (bypassing the loader)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In cases where a site's network performance is weak enough that CPRSLoader.exe, in checking the Gold Path every time a user starts CPRS, introduces unacceptable delays, some sites have elected to by-pass CPRSLoader.exe altogether and have user's shortcuts point directly to a local installation of CPRSChart.exe. The downside to this approach is that a future release of CPRSChart.exe will not be automatically picked up from the Gold Path by that workstation and the new CPRSChart.exe (plus any additional changed DLLs and Help files) will need to be pushed out to workstations by other means, such as a custom SCCM package.

> NOTE: No custom SCCM packages are provided for this purpose. It would be the responsibility of the site or region to write their own custom SCCM package or to contact national SCCM support for assistance.

> An alternative, hybrid, version of this method would be to have two shortcuts for the users: One, for day-to-day use, which points directly to the local CPRSChart.exe and a second, to be used only for updating, which points to CPRSLoader.exe.

### Manual installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Manual installation of CPRSChart.exe on an individual workstation may be necessary for troubleshooting, testing or other unconventional circumstances.

> This information may also be useful to any sites choosing the “Direct access” method above, if they are not using the hybrid option described at the end of that section.

1.  Locate the OR_30_350.ZIP and unzip the file.
2.  If this is an installation for a conventional, day-to-day CPRS user, then Copy CPRSChart.exe to C:\Program Files (x86)\CPRS\\.

    If this is an installation for a secondary use (e.g. testing or accessing a different version of CPRS), then copy CPRSChart.exe to a different location than the conventional path above (e.g. "C:\Program Files (x86)\CPRSTest" or other appropriate naming).

    Note: You may need to have a user with local machine Administrator rights complete this step.
3.  Create a Shortcut and name appropriately for the version or system being accessed, e.g. something like, “Test CPRSv30b” would give the user a clear indication that this is not the normal CPRS icon.

    ![](or-3-350-installation-guide-cprs-gui-30b/004.png)
4.  Copy the borlandmm.dll file into the same directory as CPRSChart.exe as chosen in step 2.
5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  Enter IP and RPC port in the Target field of the Shortcut properties ( or use ServerList.exe).

    Note: There is an issue currently with ServerList on some machines and the preferred method is to put the parameters in the shortcut as shown in the following graphic.

![](or-3-350-installation-guide-cprs-gui-30b/005.png)

Example of what the shortcut properties dialog might look like.

The server and port number shown above are not real and are for example only.

#### ## Order Com DLL installation

The OrderCom.dll file was part of the OR_30_350.ZIP file from step 5.2.

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate the OrderCom.dll file.
8.  Copy the OrderCom.dll file to the VistA\Common File directory.

> Windows 7:

- For 64 bit machines: “C:\Program Files (x86)\Vista\\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files”

  Note: You may need to have a user with Administrator rights complete this step.

## ePCSDataEntryForPrescriber Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This software should only be installed on the workstations of those who configure providers’ information regarding electronic prescribing of controlled substances.

1.  Unzip the XU_8_0_P641.ZIP file.
2.  Copy the epcsdataentryforprescriber.exe file to the workstations for who use the software.

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate the ePCSDataEntryForPrescriber.exe file.
4.  Copy the ePCSDataEntryForPrescriber.exe file to the VistA\Common File directory.

> Windows 7:

- For 64 bit machines: “C:\Program Files (x86)\Vista\\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files”

  Note: You may need to have a user with Administrator rights complete this step.

## CPRS Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation for the CPRS 30.B release is listed below.

Table 4 CPRS v30.b documentation

| File Name    | Description                                                  |
|------------------|------------------------------------------------------------------|
| cprsguium.doc    | CPRS User Guide in Word format                                   |
| cprsguium.pdf    | CPRS User Guide in Acrobat format                                |
| cprslmtm.doc     | CPRS Technical Manual in Word format                             |
| cprslmtm.pdf     | CPRS Technical Manual in Acrobat format                          |
| cprsguitm.doc    | CPRS GUI Technical Manual in Word format                         |
| cprsguitm.pdf    | CPRS GUI Technical Manual in Acrobat format                      |
| or_30_350_rn.doc | CPRS GUI v30.b Release Notes in Word format                      |
| or_30_350_rn.pdf | CPRS GUI v30.b Release Notes in Acrobat format                   |
| or_30_350_ig.doc | CPRS GUI v30.b Installation Guide in Word format (this document) |
| or_30_350_ig.pdf | CPRS GUI v30.b Installation Guide in Acrobat format              |

# Post Install Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Order Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following ORDER DIALOG entries have been exported in patch OR\*3\*350:

| Order Dialog - Name    | Order Dialog – Display Text |
|------------------------|-----------------------------|
| CLINIC OR PAT FLUID OE | Clinic Infusions            |
| PSJ OR CLINIC OE       | Clinic Medications          |
| PSO SUPPLY             | Supplies                    |

These new ORDER DIALOGS will need to be added to any appropriate order menus at your site so that your users can place these types of orders.

## ORWOR CATEGORY SEQUENCE Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Parameter ORWOR CATEGORY SEQUENCE defines for a site the order of display groups for orders on the Orders tab of CPRS. In order for the new orders in the CLINIC MEDICATIONS, CLINIC INFUSION and SUPPLIES/DEVICES display groups to be labeled properly, new sequence values must be entered as new Instances for this parameter. The Package level parameter has been exported with the new instance/values for these two new display groups as shown in the table below.

> Parameter Instance Value

> ----------------------------------------------------------------------------

> PKG: ORDER ENTRY/RESULTS REPOR 5 NON VA MEDS

> PKG: ORDER ENTRY/RESULTS REPOR 10 M.A.S.

> PKG: ORDER ENTRY/RESULTS REPOR 20 ALLERGIES

> PKG: ORDER ENTRY/RESULTS REPOR 30 VITALS/MEASUREMENTS

> PKG: ORDER ENTRY/RESULTS REPOR 35 ACTIVITY

> PKG: ORDER ENTRY/RESULTS REPOR 40 NURSING

> PKG: ORDER ENTRY/RESULTS REPOR 50 DIETETICS

> PKG: ORDER ENTRY/RESULTS REPOR 59 CLINIC INFUSIONS

> PKG: ORDER ENTRY/RESULTS REPOR 60 IV MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 65 OUTPATIENT MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 68 NON-VA MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 69 CLINIC MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 70 INPATIENT MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 75 LABORATORY

> PKG: ORDER ENTRY/RESULTS REPOR 80 IMAGING

> PKG: ORDER ENTRY/RESULTS REPOR 90 CONSULTS

> PKG: ORDER ENTRY/RESULTS REPOR 100 PROCEDURES

> PKG: ORDER ENTRY/RESULTS REPOR 110 SURGERY

> PKG: ORDER ENTRY/RESULTS REPOR 120 OTHER HOSPITAL SERVICES

> PKG: ORDER ENTRY/RESULTS REPOR 130 SUPPLIES/DEVICES

However, if your site has system or user level sequences defined then these display groups will need to be manually placed in your custom sequences based upon your sites discretion. Below is an example of adding these display groups to the sequence:

> \<TEST ACCOUNT\> LV List Values for a Selected Parameter

> \<TEST ACCOUNT\> LE List Values for a Selected Entity

> \<TEST ACCOUNT\> LP List Values for a Selected Package

> \<TEST ACCOUNT\> LT List Values for a Selected Template

> \<TEST ACCOUNT\> EP Edit Parameter Values

> \<TEST ACCOUNT\> ET Edit Parameter Values with Template

> \<TEST ACCOUNT\> EK Edit Parameter Definition Keyword

> You have PENDING ALERTS

> Enter "VA to jump to VIEW ALERTS option

> Select General Parameter Tools \<TEST ACCOUNT\> Option: EP Edit Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE Orders Category S

> equence

> ORWOR CATEGORY SEQUENCE may be set for the following:

> 4 User USR \[choose from NEW PERSON\]

> 8 System SYS \[TEST.CLEVELAND.MED.VA.GOV\]

> 10 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

> Enter selection: 8 System TEST.CLEVELAND.MED.VA.GOV

> --- Setting ORWOR CATEGORY SEQUENCE for System: TEST.CLEVELAND.MED.VA.GOV ---

> Select Sequence: 91

> Are you adding 91 as a new Sequence? Yes// YES

> Sequence: 91// 91

> Display Group: CLINIC

> 1 CLINIC INFUSIONS

> 2 CLINIC INJECTIONS

> 3 CLINIC MEDICATIONS

> 4 CLINIC ORDERS

> CHOOSE 1-4: 3 CLINIC MEDICATIONS

> Select Sequence: 92

> Are you adding 92 as a new Sequence? Yes// YES

> Sequence: 92// 92

> Display Group: CLINIC

> 1 CLINIC INFUSIONS

> 2 CLINIC INJECTIONS

> 3 CLINIC MEDICATIONS

> 4 CLINIC ORDERS

> CHOOSE 1-4: 1 CLINIC INFUSIONS

> Select Sequence:

## YS MHA_A DLL NAME Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health DLL has a new parameter. The purpose of this parameter is to allow you to specify the name of the DLL file associated with the Mental Health application. This allows both the current version and the new version of the Mental Health DLL to co-exist on a user’s workstation during the time that it is being tested prior to production availability.

For your test account, you will set this parameter to the name of the new DLL distributed with CPRS v30b.

Select PARAMETER DEFINITION NAME: YS MHA_A DLL NAME Name of the YS_MHA_A dll to use

------ Setting YS MHA_A DLL NAME for System: CPRS30.FO-SLC.MED.VA.GOV ------

DLL NAME: YS_MHA_A_XE3.DLL//

## New Reports on Labs Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three new reports have been added in CPRS v30B. They are exported at the Package level in the parameter: ORWRP REPORT LAB LIST.

You will need to review the parameter to determine if you have set the System, Division or User level. If you have, then the new reports will not be available until you edit the parameter.

The three new reports are:

ORRPL LAB OVERVIEW

ORRPL LAB ORDERS PEND

ORRPL LAB ORDERS ALL

## OR REPORT DATE SELECT TYPE Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter, which accepts both Division and System level settings, will define how date selection is displayed. A ‘YES’ will change the Reports and Labs Tabs in CPRS to use Radio buttons to make selections rather than from a list.

## Update for Dragon Naturally Speaking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is an issue with dictating notes using Dragon dictation software. It is expected that the vendor will make a change to correct this problem in a future release. To address this issue until that release, an edit will need to be made in a Dragon configuration file as shown below.

Edit C:\ProgramData\Nuance\NaturallySpeaking12\nsapps.ini and add the following four lines for dictation into CPRS 30B:

\[CPRSChart\]

App Support GUID={dd100104-6205-11cf-ae61-0000e8a28647} 

\[CPRSChart\Enable Class Names\] 

TRichEdit=4

## Consults Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Parameter Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ORCDGMRC EARLIEST DATE DEFAULT parameter has been replaced by a new parameter, ORCDGMRC CLIN IND DATE DEFAULT.  This is the parameter that controls the default value for the “Clinically indicated date” field on the generic consult and procedure order dialogs of CPRS GUI and also any new consult quick orders. The ORCDGMRC EARLIEST DATE DEFAULT parameter was restricted to a PACKAGE level value.  The ORCDGMRC CLIN IND DATE DEFAULT parameter allows for  DIVISION, SYSTEM, and PACKAGE. 

ORCDGMRC CLIN IND DATE DEFAULT is being exported with a PACKAGE level value of NULL.  A null value will provide default behavior that forces a provider to actively choose a date when  placing consult/procedure orders.

  
Possible Site Set Up

Sites may want to adjust the defined dates for the following:

- The default date for the “Clinically Indicated Date” for consults and procedures dialogs
- The date used in existing quick orders

Need to Change Default Clinically Indicated Date Value?

During the OR\*3.0\*350 post-install, the PACKAGE level value for the ORCDGMRC EARLIEST DATE DEFAULT parameter was captured and then set into the SYSTEM level value for the ORCDGMRC CLIN IND DATE DEFAULT parameter.  If your site wishes to view or edit the ORCDGMRC CLIN IND DATE DEFAULT parameter, use the new option Consults Clinically Indicated Date Default

\[ORW CLIN IND DATE DFLT\] found on the CPRS Configuration (Clin Coord) \[OR PARAM COORDINATOR MENU\] menu.

Changing the Date for Existing Quick OrdersNOTE: Saved quick orders and the date parameter.

Existing quick orders do not automatically update if the value for the Clinically indicated date parameter is changed.  If your site decides to change the date value for OCDGMRC CLIN IND DATE DEFAULT, any existing quick order that needs to reflect that date change will need to be manually edited.

How can I see the list of existing quick orders that might need to change?

OR\*3.0\*389 (a prerequisite patch for OR\*3.0\*350) created and sent a mail message to the person that installed that patch.  The message subject is: “CONSULT/PROCEDURE QOs EARLIEST APPROPRIATE DATE DEFAULT VALUE”.  This mail message contains a list of all your site’s consult QOs that have a default value for the Earliest Appropriate Date.  That message is intended as a reference item sites can use to edit any saved quick orders in light of the new parameter for Clinically Indicated Date.

### Input Template Change 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The INPUT TEMPLATE named GMRC SETUP REQUEST SERVICE has been re-exported by GMRC\*3.0\*81. As mentioned in the pre-install instructions for that patch, if your site had local modifications to this input template, they should be restored as soon as possible.

### Local Data Objects Based on EARLIEST DATE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site has created any local data objects based on the EARLIEST DATE field, those objects will continue to function normally. However, it is likely that the displayed name/header for such an object would need to be updated to reflect that the underlying field name has changed from EARLIEST DATE to CLINICALLY INDICATED DATE.

## OR MOB DLL VERSION parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OrderCom dll has a new parameter. The purpose of this parameter is to store the latest version of the CPRS Med Order Button (MOB) DLL that is in use for compatibility check reasons.

The version 2.0.16.0 will be exported at the Package level.

Select PARAMETER DEFINITION NAME: OR MOB DLL VERSION CPRS Med Order Button D

LL version check

Values for OR MOB DLL VERSION

Parameter Instance Value

----------------------------------------------------------------------------

PKG: ORDER ENTRY/RESULTS REPOR 1 2.0.16.0

## One-Step Clinic Admin Setup Needed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two menu options that need to be added to the secondary menu option for those providers who will be using the One-Step Clinic: OR BCMA ORDER COM and PSB GUI CONTEXT – USER.

## CPRS and MED Fix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In testing the Computerized Patient Record System (CPRS) v.30.b with the Mobile Electronic Documentation (MED) application, field testers discovered that Home-Based Primary Care (HBPC) providers were unable to properly upload their notes created in the field to CPRS. When executing the import feature in CPRS, the user would see:

“Library Not Registered” and/or “No Notes to Import”

This problem occurs because an issue with the libraries and the Windows registry. <span class="mark">REDACTED</span> has a resolution to this problem. Links to the document and a .cmd file are below:

- [MED Library Registry and Import feature fix for CPRS version 30b](http://vista.med.va.gov/cprs/docs/med/MED_Registry_Fix_Instructions_v1.1.pdf)
- [MED Fix v5.cmd](http://vista.med.va.gov/cprs/docs/med/MED_Fix_v5.cmd)

# CPRS v30 Production System Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 82%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">Production System Installation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><ol type="1">
<li></li>
</ol></td>
<td>Coordinate with appropriate personnel to prepare for installation into your production environment. Personnel might include region support staff, local Information Resource Management (IRM) staff, Clinical Application Coordinators (CACs), and other appropriate staff.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="2" type="1">
<li></li>
</ol></td>
<td><p>Confirm all Pre-requisite patches have been installed in your Production account:</p>
<p>Please check your production system to verify that the following, previously released national patches are installed:</p>
<ul>
<li><p>GMPL*2*42</p></li>
<li><p>GMPL*2*28</p></li>
<li><p>GMPL*2*44</p></li>
<li><p>GMRC*3*76</p></li>
<li><p>GMRC*3*85</p></li>
<li><p>GMTS*2.7*90</p></li>
<li><p>GMTS*2.7*96</p></li>
<li><p>LEX*2.0*86</p></li>
<li><p>OR*3*121</p></li>
<li><p>OR*3*157</p></li>
<li><p>OR*3*311</p></li>
<li><p>OR*3*312</p></li>
<li><p>OR*3*317</p></li>
<li><p>OR*3*318</p></li>
<li><p>OR*3*322</p></li>
<li><p>OR*3*341</p></li>
<li><p>OR*3*348</p></li>
<li><p>OR*3*349</p></li>
<li><p>OR*3*356</p></li>
<li><p>OR*3*363</p></li>
<li><p>OR*3*366</p></li>
<li><p>OR*3*374</p></li>
<li><p>OR*3*385</p></li>
<li><p>OR*3*388</p></li>
<li><p>OR*3*389</p></li>
<li><p>OR*3*392</p></li>
<li><p>OR*3*394</p></li>
<li><p>OR*3*418</p></li>
<li><p>PSJ*3*267</p></li>
<li><p>PSJ*5*311</p></li>
<li><p>TIU*1*211</p></li>
<li><p>TIU*1*239</p></li>
<li><p>XU*8*609</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="3" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#tiu1268-in-production">TIU*1*268 in production</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="4" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmpl247-in-production">GMPL*2*47 in production</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="5" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmpl245-in-production">GMPL*2*45 in production.</a></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="6" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#_PSJ*5*307_in_Production">PSJ*5*307 in production</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="7" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#or3350-in-production">OR*3*350 in production</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="8" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmrv528-in-production">GMRV*5*28 in production</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="9" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#ys5.01116-in-production">YS*5.01*116 in production.</a></td>
<td></td>
</tr>
<tr class="even">
<td><ol start="10" type="1">
<li></li>
</ol></td>
<td>Unzip and Install the contents of <a href="#ys_mha_a_xe3.dll-1">MHA_501_116.ZIP</a> in production.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="11" type="1">
<li></li>
</ol></td>
<td>Unzip and install the contents of <a href="#gmv_vitalsviewenter.dll-1">VITL5_P28.ZIP in production</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="12" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#xu8642-in-production">XU*8*642 in production</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="13" type="1">
<li></li>
</ol></td>
<td>Unzip and install the contents of <a href="#order-com-dll-installation-1">XU_8_0_P641.ZIP</a> in production.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="14" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmrc3.081-in-production">GMRC*3.0*81 in production</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="15" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#gmts2.7112-in-production">GMTS*2.7*112 in production</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="16" type="1">
<li></li>
</ol></td>
<td>Install patch <a href="#or3.0424-in-production">OR*3.0*424 in production</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="17" type="1">
<li></li>
</ol></td>
<td>Install the items from the CPRS GUI installation package OR_30_350.zip, per the instructions in see <a href="#zip-file-or_30_350.zip-in-production">ZIP File (OR_30_350.zip) in Production</a>, and point user shortcuts to your Production system.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="18" type="1">
<li></li>
</ol></td>
<td>Install the <a href="#epcsdataentryforprescriber-installation-1">ePCS Data Entry for Prescriber GUI</a> on APPROPRIATE workstations only in production.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="19" type="1">
<li></li>
</ol></td>
<td>Install the <a href="#order-com-dll-installation-1">Ordercom DLL</a> in production.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="20" type="1">
<li></li>
</ol></td>
<td>If you have not already, place the CPRS documentation in a location where CPRS users and support personnel can access it.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="21" type="1">
<li></li>
</ol></td>
<td>Add the new <a href="#new-order-dialogs-1">ORDER DIALOGS</a> to any appropriate order menus so that your users can place clinic orders, and supply orders.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="22" type="1">
<li></li>
</ol></td>
<td>If you do not use the Package level for the ORWOR CATEGORY SEQUENCE parameter, <a href="#orwor-category-sequence-parameters-1">create new Instances for this parameter in order for the new orders in the CLINIC MEDICATIONS, CLINIC INFUSION and SUPPLIES/DEVICES display groups to be labeled properly</a>.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="23" type="1">
<li></li>
</ol></td>
<td>Set the name of the correct version of the Mental Health DLL in the <a href="#ys-mha_a-dll-name-parameter-1">YS MHA_A DLL NAME Parameter in production</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="24" type="1">
<li></li>
</ol></td>
<td>Review the <a href="#new-reports-on-labs-tab-1">ORWRP REPORT LAB LIST parameter in production</a> to determine if you have set it at the System, Division or User level. If you have, then edit the parameter to add the new reports.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="25" type="1">
<li></li>
</ol></td>
<td>Check the <a href="#or-report-date-select-type-parameter-1">OR REPORT DATE TYPE parameter in production</a> and set it for how your site wants the date selection to display on the Reports and Labs tabs in CPRS.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="26" type="1">
<li></li>
</ol></td>
<td>If your site uses Dragon dictation software, <a href="#update-for-dragon-dictation-software">add to the .ini file</a> to ensure that Dragon works correctly with CPRS.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="27" type="1">
<li></li>
</ol></td>
<td>Check the <a href="#consults-setup-1">Consults Configuration in production</a> and complete any set up necessary.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="28" type="1">
<li></li>
</ol></td>
<td>Check the <a href="#or-mob-dll-version-parameter-1">OR MOB DLL VERSION parameter in production</a> to ensure it is the latest version of the Med Order button dynamic link library (DLL).</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="29" type="1">
<li></li>
</ol></td>
<td>For the appropriate users, complete the <a href="#one-step-clinic-admin-setup-needed-1">One-Step Clinic Admin setup in production</a>.</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="30" type="1">
<li></li>
</ol></td>
<td>For workstations that use the <a href="#cprs-and-med-fix-1">Mobile Electronic Documentation (MED) software</a>, make the necessary changes to make it work with CPRS 30.b.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="31" type="1">
<li></li>
</ol></td>
<td>Check all your institutions to verify the Facility DEA # and Facility DEA # Expiration date is correct in the INSTITUTION file (#4).</td>
<td></td>
</tr>
<tr class="even">
<td><ol start="32" type="1">
<li></li>
</ol></td>
<td>Verify the installation in your Production system has been successful. You can use the <a href="http://vista.med.va.gov/cprs/docs/30_smoke_test/V30_Smoke_Test_Script.xls">V30_Smoke_Test_Script.xls</a> document to ensure that the patches have been installed correctly.</td>
<td></td>
</tr>
<tr class="odd">
<td><ol start="33" type="1">
<li></li>
</ol></td>
<td>Complete any additional verification in your production account.</td>
<td></td>
</tr>
</tbody>
</table>

## Additional Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TIU\*1\*268 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can be loaded with users in the system. Installation time

will be less than 2 minutes.

1\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the

location of the Host File TIU_1_268.KID. \[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

3\. From this menu, you may elect to use the following options

(When prompted for the INSTALL NAME, enter "TIU\*1.0\*268"):

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DD's or templates.

b\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of this

patch (routines, DD's, templates, etc.).

c\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

4\. Use the Install Package(s) option and select the package.

a\. When prompted "Want KIDS to INHIBIT LOGONs during the

install? NO//", answer NO.

b\. When prompted "Want to DISABLE Scheduled Options and Menu

Options and Protocols? NO//", answer NO.

### GMPL\*2\*47 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview:

-------------------------------

In order to prevent hard errors and unnecessary Mailman messages from

generating during the Clinical Reminder Problem file reindex process,

Reminder Evaluations will be automatically disabled prior to indexing

and re-enabled after successful completion. This entire process (indexing/disabling/enabling) will be tasked and automated in a post-installation routine (GMPLY47).

\*\*IMPORTANT NOTE\*\*: Once Reminder Evaluations are temporarily disabled,

certain functional areas such as, the CPRS coversheet, Reminder Dialog

Branching Logic, HS Report for Reminders, TIU/HS Objects for Reminders,

and Reminder Order Checks will not function correctly.

Users trying to access these functional areas during the reindexing

process, may receive various error/warning messages. For example,

Reminder Dialogs will be turned off and display the following message:

"Dialog is disable for reminder re-indexing". Reminder Order Checks will

display the message: "Clinical Reminder evaluation is currently disabled;

this order check cannot be processed". Coversheet Reminders will have a

status of CNBD (Cannot Be Determined). HS Clinical Reminder components

will either be blank or contain a status of CNBD.

Pre-Installation Instructions:

------------------------------

To ensure that the installer receives the appropriate notification

messages in MailMan, please verify that the installer is added as a

member to the mailgroup that is defined in the REMINDER MANAGEMENT

MAILGROUP field \#3 of the CLINICAL REMINDER PARAMETERS file \#800.

Installation Instructions:

--------------------------

This patch loads several routines and may be installed with users on

the system although it is recommended that it be installed during

non-peak hours to minimize potential disruption to users. This patch

should take less than 1 minute to install.

However depending on the size of your site's Problem file, it could take

1-1.5 hours for the reindexing process to complete. As an example, for a

site that has 3 million entries in the Problem file, it took the

reindexing process 1 hr to complete.

\*\*IMPORTANT NOTE\*\*: Given this information and the fact that reminder

evaluations will be temporarily disabled, it is STRONGLY RECOMMENDED

that at least 1-1.5 hrs. is allocated for the completion of the reindex

and that this be installed during afterhours to minimize disruption to

users.

1\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the

location of the Host File GMPL_2_47.KID.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter the patch GMPL\*2.0\*47

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//', response with NO.

6\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//', respond with NO.

Post-Installation Instructions:

-------------------------------

The post-install routine will call a Reminders API to reindex and clean

up any outstanding ACRMT indexes that didn't get disposed of

appropriately. It will also create a new auxiliary cross-reference, ACRMTA, for the Mapping Target multiple.

The post-install routine will also automatically disable the reminder

evaluations prior to executing the reindex process. A MailMan message

should be generated to the installer and Clinical Reminder mailgroup

confirming so:

Subj: REMINDER EVALUATION DISABLED \[#68774\] 08/21/15@12:37 13 lines

From: POSTMASTER (Sender: INSTALLER,ONE) In 'IN' basket. Page 1

--------------------------------------------------------------------------

Reminder evaluation was disabled on Aug 21, 2015@12:37:43.

Because of this, the following TaskMan jobs can produce erroneous results.

Pending jobs should not be allowed to start until evaluation is enabled.

The results of running jobs should be discarded and if possible, running

jobs should be stopped.

Reason: index rebuild for file \#9000011.

Reminders Due Report Jobs

Reminder Patient List Jobs

Reminder Extract Jobs

Once the reindexing process is complete, a Problem List Reindex Complete

notification message should be generated to the installer and Reminder

mailgroup indicating so. The below example is taken from a development

account and does not accurately reflect actual production times.

Subj: Index for global ^AUPNPROB( successfully built \[#68773\]

08/21/15@12:37

5 lines

From: INSTALLER,ONE In 'IN' basket. Page 1

--------------------------------------------------------------------------

Build of Clinical Reminders index for global ^AUPNPROB( completed.

Build finished at 08/21/2015@12:37:44

131 entries were created.

Elapsed time: 1 secs

0 errors were encountered.

Once the reindexing process has successfully completed, the reminder

evaluations will automatically be re-enabled. A MailMan message

should be generated to the installer and Reminder mailgroup confirming so:

Subj: REMINDER EVALUATION ENABLED \[#68775\] 08/21/15@12:37 2 lines

From: POSTMASTER (Sender: INSTALLER,ONE) In 'IN' basket. Page 1

--------------------------------------------------------------------------

Reminder evaluation was enabled on Aug 21, 2015@12:37:55.

It was disabled on Aug 21, 2015@12:37:43.

### GMPL\*2\*45 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 1 minute to install.

1\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the

location of the Host File GMPL_2_45.KID

3\. From the same menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter GMPL\*2.0\*45)

a\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

b\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

c\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of

this patch (routines, DD's, templates, etc.).

d\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DD's or templates.

4\. Use the Install Package(s) option and select the package

GMPL\*2.0\*45

5\. When Prompted "Want KIDS to INHIBIT LOGONs during the install?

NO//" respond NO.

6\. When Prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//" respond NO.

### PSJ\*5\*307 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview:

-------------------------------

This patch is being released as a part of the CPRS v30 phased release. Specific instructions on downloading the software will be distributed when your site is scheduled to install.

Pre-Installation Instructions:

------------------------------

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. Specifically, this patch should not be installed during heavy usage times for Clinic Orders or BCMA Med

Order Button orders. This patch should take less than 5 minutes to install.

Installation Instructions:

--------------------------

1\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the

location of the Host File PSJ_5_307.KID.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter the patch

PSJ\*5.0\*307

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

c\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? NO//', respond NO.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//', respond NO.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//', respond NO.

8\. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

### OR\*3\*350 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 1 minute. Users may remain on the system.

> **NOTE:** When installing patch OR\*3\*350, sites may notice a message that shows that they are missing patch OR\*3\*237, but this is incorrect. The reason is that patch OR\*3\*243 did not list patch 237 although it should have. Patch OR\*3\*350 does list patch 237 in the second line as it should.

1\. From the Kernel Installation & Distribution System menu, select the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the location of the Host File OR_30_350.KID.

3\. From this menu, you may elect to use the following options

a\. Backup a Transport Global

b\. Compare Transport Global to Current System

c\. Verify Checksums in Transport Global

4\. Use the Install Package(s) options and select the package OR\*3.0\*350.

5\. At the “Want to RUN the Environment Check Routine?”, respond YES.

6\. When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install?”, respond NO.

7\. When prompted Please select the recipients for the NON-VA MEDICATION COMPLEX QUICK ORDER DIALOG REPORT below.

> Send mail to:

> Enter the name of person who should receive this report, such as a CAC at the site.

> Select basket to send to:

> Respond IN//.

7\. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'

respond NO.

8\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//', respond NO.

### GMRV\*5\*28 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

==========================

1.  From the Kernel Installation & Distribution System menu, select the Installation menu.
5.  From this menu, choose to Load a Distribution and enter the location of the Host File GMRV_5_28.KID.
6.  Start up the Kernel Installation and Distribution System Menu \[XPD MAIN\]:

Edits and Distribution ...

Utilities ...

Installation ...

7.  From this menu, you may elect to use the following options: (When prompted for the INSTALL NAME, enter GMRV\*5.0\*28):
    1.  Backup a Transport Global -This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
8.  Use the Install Package(s) option and select the package GMRV\*5.0\*28.
9.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
10. When prompted 'Want to DISABLE Scheduled Options and Menu Options and Protocols? NO//', answer NO.

### YS\*5.01\*116 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 1 minute to install.

1\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the

location of the Host File YS_501_116.KID

3\. From the same menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter YS\*5.01\*116)

a\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

c\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of

this patch (routines, DD's, templates, etc.).

4\. Use the Install Package(s) option and select the package

YS\*5.01\*116

5\. When Prompted "Want KIDS to INHIBIT LOGONs during the install?

NO//" respond NO.

6\. When Prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//" respond NO.

### XU\*8\*642 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system. This patch should take less than 1 minute to install. It may be queued for installation.

There are no options that need to be disabled.

1\. From the Kernel Installation & Distribution System menu, select the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the location of the Host File XU8P642.KID.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch

XU\*8.0\*642

a\. Print Transport Global - This option lets you print the contents

of a Transport Global that is currently loaded in the ^XTMP

global.

b\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

c\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

d\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? NO//' answer "NO".

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' answer "NO".

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//' answer "NO".

8\. If prompted 'Delay Install (Minutes): (0 - 60): 0//' answer "0".

### GMRC\*3.0\*81 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview:

-------------------------------

The pre-install will remove the current data dictionary for the

REQUEST/CONSULTATION file (#123). The new data dictionary, containing

the renamed CLINICALLY INDICATED DATE field, will be installed during

the KIDS installation. There patch does not contain any automated

post-install actions.

Pre-Installation Instructions:

------------------------------

This patch will overwrite the GMRC SETUP REQUEST SERVICE entry in the

INPUT TEMPLATE file. If your site has made any local modifications to

this input template, they should be captured prior to installing

GMRC\*3.0\*81, and then restored soon after.

LOCAL OBJECTS BASED ON EARLIEST DATE

====================================

If your site has created any local data objects based on the EARLIEST DATE

field, those objects will continue to function normally. However, it is

likely that the displayed name/header for such an object would need to be

updated to reflect that the underlying field name has changed from

EARLIEST DATE to CLINICALLY INDICATED DATE.

This patch may be installed with users on the system although it is

recommended that it be installed during non-peak hours to minimize

potential disruption to users. This patch should take less than 5

minutes to install.

1\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the

location of the Host File GMRC_30_81.KID

3\. From the same menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter GMRC\*3.0\*81)

a\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

b\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

c\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of

this patch (routines, DD's, templates, etc.).

d\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DD's or templates.

4\. Use the Install Package(s) option and select the package

GMRC\*3.0\*81

5\. When Prompted "Want KIDS to INHIBIT LOGONs during the install?

NO//" respond NO.

6\. When Prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//" respond NO.

Post install instructions

------------------------------------

If your site has local objects based on the EAD field, ensure that

relevant end user displays are updated appropriately. Reference note above

entitled LOCAL OBJECTS BASED ON EARLIEST DATE.

### GMTS\*2.7\*112 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview:

-------------------------------

This patch does not contain any automated pre-install actions.

The post-install will add the missing components to the Patient Data Exchange (PDX) and also

update the DESCRIPTION field of the Consults Brief health summary component (CNB).

Pre-Installation Instructions:

------------------------------

This patch may be installed with users on the system although it is

recommended that it be installed during non-peak hours to minimize

potential disruption to users. This patch should take less than 5

minutes to install.

1\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

2\. From this menu, choose to Load a Distribution and enter the

location of the Host File GMTS_27_112.KID

3\. From the same menu, you may select to use the following options:

(when prompted for INSTALL NAME, enter GMTS\*2.7\*112)

a\. Verify Checksums in Transport Global - This option will

allow you to ensure the integrity of the routines that are

in the transport global.

b\. Print Transport Global - This option will allow you to view

the components of the KIDS build.

c\. Compare Transport Global to Current System - This option

will allow you to view all changes that will be made when

this patch is installed. It compares all components of

this patch (routines, DD's, templates, etc.).

d\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will

not backup any other changes such as DD's or templates.

4\. Use the Install Package(s) option and select the package

GMTS\*2.7\*112

5\. When Prompted "Want KIDS to INHIBIT LOGONs during the install?

NO//" respond NO.

6\. When Prompted "Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//" respond NO.

Post-Installation Instructions:

-------------------------

GMTSP112 may be deleted from the system once all patch functionality has been verified as working as expected.  IT staff may choose to keep a copy of this routine for future reference.

### OR\*3.0\*424 in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

-------------------------

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 1 minute to install.

> 1\. From the Kernel Installation & Distribution System menu, select the Installation menu.

> 2\. From this menu, choose to Load a Distribution and enter the location of the Host File OR_30_424.KID.

3\. From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch

OR\*3.0\*424.

a\. Print Transport Global - This option lets you print the contents

of a Transport Global that is currently loaded in the ^XTMP

global.

b\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates.

c\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

d\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install: OR\*3.0\*424.

5\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' Answer 'NO'

6\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//' Answer 'NO'

## ZIP File (OR_30_350.zip) in Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP file contains the CPRS GUI executable file as well as the DLLs associated with 30B, Vitals, Mental Health and One-Step Clinic Admin.

Download the ZIP file and extract all the files.

Placement of DLLs:

The DLLs are no longer required to reside on individual workstations. For example, if you are doing a network install of the CPRSChart executable, you can place the DLLs in that same directory.

3.  Some sites have experienced unacceptable delays in launching the DLLs if they are located on the server. If this occurs, the DLLs should be placed on the local workstations.

Here is the hierarchy the CPRS GUI uses to search for the DLLs:

1.  The same folder as the application
2.  A “'Common Files\\ folder in the same folder as the application
3.  Windows 7:
- For 64 bit machines: “C:\Program Files (x86)\Vista\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files”

## GMV_VitalsViewEnter.dll

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\*\*\*\*\*IMPORTANT NOTE\*\*\*\*\*If possible, it is simpler for the users that are testing the new Vitals DLL to install it on a workstation that is never used for entering Vitals for the production system. If it is necessary to install on a machine that will be used for entering Vitals in production, the user will have to replace the new DLL with the current released version whenever it is necessary to enter Vitals in production.

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Unzip the VITL5_P28.ZIP file and move the files to an appropriate directory and/or workstations.

> Windows 7:

- For 64 bit machines: “C:\Program Files (x86)\Vista\\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files”

  Note: You may need to have a user with Administrator rights complete this step.

If you are running the Vitals Lite DLL files from individual workstations and you want to push the files using SCCM, you should include the files from the VITL5_P28.zip in your script.

### MSP Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals DLL will be included in the v30 MSP file. But, for test installations, it is expected you will be using the manual installation.

## YS_MHA_A_XE3.DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Unzip the MHA_501_116.ZIP file and move the files to an appropriate directory and/or workstations.

> Windows 7:

- For 64 bit machines: “C:\Program Files (x86)\Vista\\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files\\

  Note: You may need to have a user with Administrator rights complete this step.

### MSP Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health DLL will be included in the v30 MSP file. But, for test installations, it is expected you will be using the manual installation.

## CPRS GUI Executable Methods of installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following methods of installation of CPRS are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

### Network (Shared) Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPRSChart.exe) across the LAN.

> The GUI executable (CPRSChart.exe), and ancillary files (DLLs, Help files etc.), are copied to a network shared location. Users are provided with a desktop shortcut to run CPRSChart.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the “Target” field of the shortcut properties

> At the time of a CPRS version update the copy of CPRSChart.exe (and any updated ancillary files) is simply replaced, on the network share, with the new version.

> Any users requiring access to another site's CPRS system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of CPRS (e.g. during a phased deployment, when sites are temporarily not all on the same version, or for testing purposes) a different version of CPRSChart.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

> Note: The version of CPRSChart a user executes must always match the patch-level version of the VistA system targeted.

### Citrix installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The GUI executable (CPRSChart.exe) and ancillary files (DLLs, Help files etc.) are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

> During a phased deployment of a new version of CPRS, if a Citrix Farm is serving users who are scheduled to deploy at different times, the Farm administrator may be required to temporarily maintain hosts with both the old and the new versions of CPRSChart.exe available.

### Gold Path installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is the “standard” method of installation where the GUI executable (CPRSChart.exe), and ancillary files (DLLs, Help files etc.), are installed on and run from the user's local workstation. In normal day-to-day operation, the user's shortcut executes a locally installed copy of CPRSLoader.exe which looks in a pre-configured network “Gold Path” (specified in a command line parameter) to see if there is a later version of CPRSChart.exe ready to be installed. If not, then execution passes to the locally installed version of CPRSChart.exe. If an updated version is found on the Gold Path, then a silent installation of the new version takes place, following which the newly installed version of CPRSChart.exe is executed on the local workstation.

> This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file (CPRSLoader.msi) to each user's workstation, typically accomplished via SCCM. This is outside the scope of CPRS development and is normally handled by Enterprise Software Engineering (ESE) Desktop Services in coordination with Regional COR Client Technologies leadership.

> The CPRSChart.exe component of the update is held in a Microsoft Software Patch (MSP) file (CPRSChart.msp) which is copied to the network Gold Path location—that should be all that is required for a normal CPRS version update for sites using this method. The exception is if a new version of CPRS Loader is also being released, in which case the cycle begins again with the distribution to users' workstations of the new CPRSLoader.msi (before the new CPRSChart.msp is copied to the network Gold Path)—this is the circumstance in which CPRS v30b is being released.

> The CPRS deployment software distribution will include an appropriate version of the CPRS Microsoft patch file (named CPRS_XX_YY.msp, where XX is the current version number for CPRS, and YY is the current build number.  At this point the current file name is CPRS_30_72.msp).  This file has the named version of CPRSChart embedded within it, along with any updated ancillary files.  Also included in the deployment software distribution will be a .VER file.  This file will have the same name as the MSP file, with only the file extension changed.  As an example, the .VER file for CPRS_30_72.MSP will be named CPRS_30_72.VER.  To be effective, the .VER file must be placed in the same Gold Path in which the .MSP file was placed.  The .VER is optional but beneficial.  It will allow the CPRS loader to much more quickly find an appropriate version of CPRSChart.exe for use with the current VistA system.  Including the VER file in the Gold Path can shorten CPRS start times from several minutes to just a few seconds.

> For the convenience of local System Administrators, the file CPRSLoader.msi is also included in the release package, in case they need to manually install it on a workstation.

### Direct Access to a Local Copy of CPRSChart.exe (bypassing the loader)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In cases where a site's network performance is weak enough that CPRSLoader.exe, in checking the Gold Path every time a user starts CPRS, introduces unacceptable delays, some sites have elected to by-pass CPRSLoader.exe altogether and have user's shortcuts point directly to a local installation of CPRSChart.exe. The downside to this approach is that a future release of CPRSChart.exe will not be automatically picked up from the Gold Path by that workstation and the new CPRSChart.exe (plus any additional changed DLLs and Help files) will need to be pushed out to workstations by other means, such as a custom SCCM package.

> An alternative, hybrid, version of this method would be to have two shortcuts for the users: One, for day-to-day use, which points directly to the local CPRSChart.exe and a second, to be used only for updating, which points to CPRSLoader.exe.

### Manual installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Manual installation of CPRSChart.exe on an individual workstation may be necessary for troubleshooting, testing or other unconventional circumstances.

> This information may also be useful to any sites choosing the “Direct access” method above, if they are not using the hybrid option described at the end of that section.

1.  Locate the OR_30_350.ZIP and unzip the file.
9.  If this is an installation for a conventional, day-to-day CPRS user, then Copy CPRSChart.exe to C:\Program Files (x86)\CPRS\\.

    If this is an installation for a secondary use (e.g. testing or accessing a different version of CPRS), then copy CPRSChart.exe to a different location than the conventional path above (e.g. "C:\Program Files (x86)\CPRSTest" or other appropriate naming).

    Note: You may need to have a user with local machine Administrator rights complete this step.
10. Create a Shortcut and name appropriately for the version or system being accessed, e.g. something like, “Test CPRSv30b” would give the user a clear indication that this is not the normal CPRS icon.

    ![](or-3-350-installation-guide-cprs-gui-30b/006.png)
11. Copy the borlandmm.dll file into the same directory as CPRSChart.exe as chosen in step 2.
12. Determine the DNS server name or IP address for the appropriate VistA server.
13. Determine the Broker RPC port for the VistA account.
14. Enter IP and RPC port in the Target field of the Shortcut properties ( or use ServerList.exe).

    Note: There is an issue currently with ServerList on some machines and the preferred method is to put the parameters in the shortcut as shown in the following graphic.

![](or-3-350-installation-guide-cprs-gui-30b/007.png)

Example of what the shortcut properties dialog might look like.

The server and port number shown above are not real and are for example only.

#### ## Order Com DLL installation

The OrderCom.dll file was part of the OR_30_350.ZIP file from step 5.2.

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate the OrderCom.dll file.
15. Copy the OrderCom.dll file to the VistA\Common File directory.

> Windows 7:

- For 64 bit machines: “C:\Program Files (x86)\Vista\\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files”

  Note: You may need to have a user with Administrator rights complete this step.

## ePCSDataEntryForPrescriber Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This software should only be installed on the workstations of those who configure providers’ information regarding electronic prescribing of controlled substances.

Unzip the XU_8_0_P641.ZIP file.

### Manual Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Locate the ePCSDataEntryForPrescriber.exe file.
16. Copy the ePCSDataEntryForPrescriber.exe file to the VistA\Common File directory.

> Windows 7:

- For 64 bit machines: “C:\Program Files (x86)\Vista\\Common Files”
- For 32 bit machines: “C:\Program Files\Vista\Common Files”

  Note: You may need to have a user with Administrator rights complete this step.

## CPRS Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation for the CPRS 30.B release is listed below.

Table 4 CPRS v30.b documentation

| File Name    | Description                                                  |
|------------------|------------------------------------------------------------------|
| cprsguium.doc    | CPRS User Guide in Word format                                   |
| cprsguium.pdf    | CPRS User Guide in Acrobat format                                |
| cprslmtm.doc     | CPRS Technical Manual in Word format                             |
| cprslmtm.pdf     | CPRS Technical Manual in Acrobat format                          |
| cprsguitm.doc    | CPRS GUI Technical Manual in Word format                         |
| cprsguitm.pdf    | CPRS GUI Technical Manual in Acrobat format                      |
| or_30_350_rn.doc | CPRS GUI v30.b Release Notes in Word format                      |
| or_30_350_rn.pdf | CPRS GUI v30.b Release Notes in Acrobat format                   |
| or_30_350_ig.doc | CPRS GUI v30.b Installation Guide in Word format (this document) |
| or_30_350_ig.pdf | CPRS GUI v30.b Installation Guide in Acrobat format              |

# Post Install Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## New Order Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following ORDER DIALOG entries have been exported in patch OR\*3\*350:

| Order Dialog - Name    | Order Dialog – Display Text |
|------------------------|-----------------------------|
| CLINIC OR PAT FLUID OE | Clinic Infusions            |
| PSJ OR CLINIC OE       | Clinic Medications          |
| PSO SUPPLY             | Supplies                    |

These new ORDER DIALOGS will need to be added to any appropriate order menus at your site so that your users can place these types of orders.

## ORWOR CATEGORY SEQUENCE Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Parameter ORWOR CATEGORY SEQUENCE defines for a site the order of display groups for orders on the Orders tab of CPRS. In order for the new orders in the CLINIC MEDICATIONS, CLINIC INFUSION and SUPPLIES/DEVICES display groups to be labeled properly, new sequence values must be entered as new Instances for this parameter. The Package level parameter has been exported with the new instance/values for these two new display groups as shown in the table below.

> Parameter Instance Value

> ----------------------------------------------------------------------------

> PKG: ORDER ENTRY/RESULTS REPOR 5 NON VA MEDS

> PKG: ORDER ENTRY/RESULTS REPOR 10 M.A.S.

> PKG: ORDER ENTRY/RESULTS REPOR 20 ALLERGIES

> PKG: ORDER ENTRY/RESULTS REPOR 30 VITALS/MEASUREMENTS

> PKG: ORDER ENTRY/RESULTS REPOR 35 ACTIVITY

> PKG: ORDER ENTRY/RESULTS REPOR 40 NURSING

> PKG: ORDER ENTRY/RESULTS REPOR 50 DIETETICS

> PKG: ORDER ENTRY/RESULTS REPOR 59 CLINIC INFUSIONS

> PKG: ORDER ENTRY/RESULTS REPOR 60 IV MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 65 OUTPATIENT MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 68 NON-VA MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 69 CLINIC MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 70 INPATIENT MEDICATIONS

> PKG: ORDER ENTRY/RESULTS REPOR 75 LABORATORY

> PKG: ORDER ENTRY/RESULTS REPOR 80 IMAGING

> PKG: ORDER ENTRY/RESULTS REPOR 90 CONSULTS

> PKG: ORDER ENTRY/RESULTS REPOR 100 PROCEDURES

> PKG: ORDER ENTRY/RESULTS REPOR 110 SURGERY

> PKG: ORDER ENTRY/RESULTS REPOR 120 OTHER HOSPITAL SERVICES

> PKG: ORDER ENTRY/RESULTS REPOR 130 SUPPLIES/DEVICES

However, if your site has system or user level sequences defined then these display groups will need to be manually placed in your custom sequences based upon your sites discretion. Below is an example of adding these display groups to the sequence:

> \<TEST ACCOUNT\> LV List Values for a Selected Parameter

> \<TEST ACCOUNT\> LE List Values for a Selected Entity

> \<TEST ACCOUNT\> LP List Values for a Selected Package

> \<TEST ACCOUNT\> LT List Values for a Selected Template

> \<TEST ACCOUNT\> EP Edit Parameter Values

> \<TEST ACCOUNT\> ET Edit Parameter Values with Template

> \<TEST ACCOUNT\> EK Edit Parameter Definition Keyword

> You have PENDING ALERTS

> Enter "VA to jump to VIEW ALERTS option

> Select General Parameter Tools \<TEST ACCOUNT\> Option: EP Edit Parameter Values

> --- Edit Parameter Values ---

> Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE Orders Category S

> equence

> ORWOR CATEGORY SEQUENCE may be set for the following:

> 4 User USR \[choose from NEW PERSON\]

> 8 System SYS \[TEST.CLEVELAND.MED.VA.GOV\]

> 10 Package PKG \[ORDER ENTRY/RESULTS REPORTING\]

> Enter selection: 8 System TEST.CLEVELAND.MED.VA.GOV

> --- Setting ORWOR CATEGORY SEQUENCE for System: TEST.CLEVELAND.MED.VA.GOV ---

> Select Sequence: 91

> Are you adding 91 as a new Sequence? Yes// YES

> Sequence: 91// 91

> Display Group: CLINIC

> 1 CLINIC INFUSIONS

> 2 CLINIC INJECTIONS

> 3 CLINIC MEDICATIONS

> 4 CLINIC ORDERS

> CHOOSE 1-4: 3 CLINIC MEDICATIONS

> Select Sequence: 92

> Are you adding 92 as a new Sequence? Yes// YES

> Sequence: 92// 92

> Display Group: CLINIC

> 1 CLINIC INFUSIONS

> 2 CLINIC INJECTIONS

> 3 CLINIC MEDICATIONS

> 4 CLINIC ORDERS

> CHOOSE 1-4: 1 CLINIC INFUSIONS

> Select Sequence:

## YS MHA_A DLL NAME Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mental Health DLL has a new parameter. The purpose of this parameter is to allow you to specify the name of the DLL file associated with the Mental Health application. This allows both the current version and the new version of the Mental Health DLL to co-exist on a user’s workstation during the time that it is being tested prior to production availability.

For your test account, you will set this parameter to the name of the new DLL distributed with CPRS v30b.

Select PARAMETER DEFINITION NAME: YS MHA_A DLL NAME Name of the YS_MHA_A dll to use

------ Setting YS MHA_A DLL NAME for System: CPRS30.FO-SLC.MED.VA.GOV ------

DLL NAME: YS_MHA_A_XE3.DLL//

## New Reports on Labs Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Three new reports have been added in CPRS v30B. They are exported at the Package level in the parameter: ORWRP REPORT LAB LIST.

You will need to review the parameter to determine if you have set the System, Division or User level. If you have, then the new reports will not be available until you edit the parameter.

The three new reports are:

ORRPL LAB OVERVIEW

ORRPL LAB ORDERS PEND

ORRPL LAB ORDERS ALL

## OR REPORT DATE SELECT TYPE Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This parameter, which accepts both Division and System level settings, will define how date selection is displayed. A ‘YES’ will change the Reports and Labs Tabs in CPRS to use Radio buttons to make selections rather than from a list.

## Update for Dragon Dictation Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is an issue with dictating notes using Dragon dictation software. It is expected that the vendor will make a change to correct this problem in a future release. To address this issue until that release, an edit will need to be made in a Dragon configuration file as shown below.

Edit C:\ProgramData\Nuance\NaturallySpeaking12\nsapps.ini and add the following four lines for dictation into CPRS 30B:

\[CPRSChart\]

App Support GUID={dd100104-6205-11cf-ae61-0000e8a28647} 

\[CPRSChart\Enable Class Names\] 

TRichEdit=4

## Consults Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Parameter Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ORCDGMRC EARLIEST DATE DEFAULT parameter has been replaced by a new parameter, ORCDGMRC CLIN IND DATE DEFAULT.  This is the parameter that controls the default value for the “Clinically indicated date” field on the generic consult and procedure order dialogs of CPRS GUI and also any new consult quick orders. The ORCDGMRC EARLIEST DATE DEFAULT parameter was restricted to a PACKAGE level value.  The ORCDGMRC CLIN IND DATE DEFAULT parameter allows for  DIVISION, SYSTEM, and PACKAGE. 

ORCDGMRC CLIN IND DATE DEFAULT is being exported with a PACKAGE level value of NULL.  A null value will provide default behavior that forces a provider to actively choose a date when  placing consult/procedure orders.

Possible Site Set Up

Sites may want to adjust the defined dates for the following:

- The default date for the “Clinically Indicated Date” for consults and procedures dialogs
- The date used in existing quick orders

Need to Change Default Clinically Indicated Date Value?

During the OR\*3.0\*350 post-install, the PACKAGE level value for the ORCDGMRC EARLIEST DATE DEFAULT parameter was captured and then set into the SYSTEM level value for the ORCDGMRC CLIN IND DATE DEFAULT parameter.  If your site wishes to view or edit the ORCDGMRC CLIN IND DATE DEFAULT parameter, use the new option Consults Clinically Indicated Date Default

\[ORW CLIN IND DATE DFLT\] found on the CPRS Configuration (Clin Coord) \[OR PARAM COORDINATOR MENU\] menu.

Changing the Date for Existing Quick OrdersNOTE: Saved quick orders and the date parameter.

Existing quick orders do not automatically update if the value for the Clinically indicated date parameter is changed.  If your site decides to change the date value for OCDGMRC CLIN IND DATE DEFAULT, any existing quick order that needs to reflect that date change will need to be manually edited.

How can I see the list of existing quick orders that might need to change?

OR\*3.0\*389 (a prerequisite patch for OR\*3.0\*350) created and sent a mail message to the person that installed that patch.  The message subject is: “CONSULT/PROCEDURE QOs EARLIEST APPROPRIATE DATE DEFAULT VALUE”.  This mail message contains a list of all your site’s consult QOs that have a default value for the Earliest Appropriate Date.  That message is intended as a reference item sites can use to edit any saved quick orders in light of the new parameter for Clinically Indicated Date.

### Input Template Change 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The INPUT TEMPLATE named GMRC SETUP REQUEST SERVICE has been re-exported by GMRC\*3.0\*81. As mentioned in the pre-install instructions for that patch, if your site had local modifications to this input template, they should be restored as soon as possible. For use as a local reference, OR\*3.0\*389 creates a mail message containing a list of all consult quick orders that have a value stored for the Clinically Indicated Date (previously known as the Earliest Appropriate Date).

### Local Data Objects Based on EARLIEST DATE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site has created any local data objects based on the EARLIEST DATE field, those objects will continue to function normally. However, it is likely that the displayed name/header for such an object would need to be updated to reflect that the underlying field name has changed from EARLIEST DATE to CLINICALLY INDICATED DATE.

## OR MOB DLL VERSION parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OrderCom DLL has a new parameter. The purpose of this parameter is to store the latest version of the CPRS Med Order Button (MOB) DLL that is in use for compatibility check reasons.

The version 2.0.16.0 will be exported at the Package level.

Select PARAMETER DEFINITION NAME: OR MOB DLL VERSION CPRS Med Order Button D

LL version check

Values for OR MOB DLL VERSION

Parameter Instance Value

----------------------------------------------------------------------------

PKG: ORDER ENTRY/RESULTS REPOR 1 2.0.16.0

## One-Step Clinic Admin Setup Needed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two menu options that need to be added to the secondary menu option for those providers who will be using the One-Step Clinic: OR BCMA ORDER COM and PSB GUI CONTEXT – USER.

## CPRS and MED Fix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In testing the Computerized Patient Record System (CPRS) v.30.b with the Mobile Electronic Documentation (MED) application, field testers discovered that Home-Based Primary Care (HBPC) providers were unable to properly upload their notes created in the field to CPRS. When executing the import feature in CPRS, the user would see:

“Library Not Registered” and/or “No Notes to Import”

This problem occurs because an issue with the libraries and the Windows registry. <span class="mark">REDACTED</span> has a resolution to this problem. Links to the document and a .cmd file are below:

- [MED Library Registry and Import feature fix for CPRS version 30b](http://vista.med.va.gov/cprs/docs/med/MED_CPRS_Patch.pdf)
- [MED Fix .cmd file fix](http://vista.med.va.gov/cprs/docs/med/MED_Fix.cmd)

# # # CPRS v30 M patches—Software Installation Samples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TIU\*1\*268 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT320

You have 198 new messages.

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INSTallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: \_\$1\$DGA104:\[HSDD.CPRS30\]TIU_1_268V26.KID

KIDS Distribution saved on Sep 08, 2015@09:19:12

Comment: TIU\*1.0\*268 v26

This Distribution contains Transport Globals for the following Package(s):

TIU\*1.0\*268

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

TIU\*1.0\*268

Use INSTALL NAME: TIU\*1.0\*268 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

Select INSTALL NAME: TIU\*1.0\*268 9/18/15@15:29:02

=\> TIU\*1.0\*268 v26 ;Created on Sep 08, 2015@09:19:12

This Distribution was loaded on Sep 18, 2015@15:29:02 with header of

TIU\*1.0\*268 v26 ;Created on Sep 08, 2015@09:19:12

It consisted of the following Install(s):

TIU\*1.0\*268

Checking Install for Package TIU\*1.0\*268

Install Questions for TIU\*1.0\*268

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;9999 TELNET PORT

-------------------------------------------------------------------------------

Install Started for TIU\*1.0\*268 :

Sep 18, 2015@15:29:17

Build Distribution Date: Sep 08, 2015

Installing Routines:

Sep 18, 2015@15:29:17

Installing PACKAGE COMPONENTS:

Installing REMOTE PROCEDURE

Sep 18, 2015@15:29:17

Updating Routine file...

Updating KIDS files...

TIU\*1.0\*268 Installed.

Sep 18, 2015@15:29:17

Not a production UCI

Install Completed

### GMPL\*2.0\*47 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install Started for GMPL\*2.0\*47 :

Dec 18, 2014@14:37:02

Build Distribution Date: Dec 18, 2014

Installing Routines:

Dec 18, 2014@14:37:02

Running Post-Install Routine: POST^GMPLY47

Creating Problem List Mapping Targets auxiliary cross-reference.

Problem List Clinical Reminders Index rebuild queued.

The task number is 36789.

Updating Routine file...

Updating KIDS files...

GMPL\*2.0\*47 Installed.

Dec 18, 2014@14:37:02

Not a production UCI

NO Install Message sent

### GMPL\*2.0\*45 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install Started for GMPL\*2.0\*45 :

Aug 27, 2014@14:52:47

Build Distribution Date: Aug 27, 2014

Installing Routines:

Aug 27, 2014@14:52:47

Installing Data Dictionaries:

Aug 27, 2014@14:52:47

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Aug 27, 2014@14:52:47

Updating Routine file...

Updating KIDS files...

GMPL\*2.0\*45 Installed.

Aug 27, 2014@14:52:47

Not a production UCI

NO Install Message sent

### PSJ\*5\*307 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

Select INSTALL NAME: PSJ\*5.0\*307 2/20/14@18:12:49

=\> PSJ 307 ;Created on Feb 04, 2014@11:04:29

This Distribution was loaded on Feb 20, 2014@18:12:49 with header of

PSJ 307 ;Created on Feb 04, 2014@11:04:29

It consisted of the following Install(s):

PSJ\*5.0\*307

Checking Install for Package PSJ\*5.0\*307

Install Questions for PSJ\*5.0\*307

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

PSJ\*5.0\*307

------------------------------------------------------------------------------

Install Started for PSJ\*5.0\*307 :

Feb 20, 2014@18:26:45

Build Distribution Date: Feb 04, 2014

Installing Routines:

Feb 20, 2014@18:26:45

Updating Routine file...

Updating KIDS files...

PSJ\*5.0\*307 Installed.

Feb 20, 2014@18:26:45

Install Message \#1231

-------------------------------------------------------------------------------



100%  25 50 75 

Complete 

### OR\*3\*350 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CHEYL43\>d ^XUP

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT100

You have 2 new messages.

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: LOAD a Distribution

Enter a Host File: /home/sftp/or_30_350v55.kid

KIDS Distribution saved on Dec 21, 2013@13:20:50

Comment: CPRS30V8 KIDS BUILD

This Distribution contains Transport Globals for the following Package(s):

OR\*3.0\*350

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

Build OR\*3.0\*350 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES//

OR\*3.0\*350

Will first run the Environment Check Routine, ORY350E

Use INSTALL NAME: OR\*3.0\*350 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

Select INSTALL NAME: OR\*3.0\*350 8/28/13@15:37:22

=\> CPRS30V8 KIDS BUILD ;Created on Aug 21, 2013@13:20:50

This Distribution was loaded on Aug 28, 2013@15:37:22 with header of

CPRS30V8 KIDS BUILD ;Created on Aug 21, 2013@13:20:50

It consisted of the following Install(s):

OR\*3.0\*350

Checking Install for Package OR\*3.0\*350

Will first run the Environment Check Routine, ORY350E

Install Questions for OR\*3.0\*350

Incoming Files:

101.24 OE/RR REPORT (including data)

> **NOTE:** You already have the 'OE/RR REPORT' File.

I will REPLACE your data with mine.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

\*\*\* NON-VA MEDICATION COMPLEX QUICK ORDER DIALOG REPORT QUESTIONS \*\*\*

The post-install will create the NON-VA MEDICATION COMPLEX QUICK ORDER DIALOG

REPORT, which contains non-VA medication quick orders with a complex dosage.

The installer is strongly encouraged to include the site's local Clinical

Application Coordinators (CACs) as recipients of this report.

Please select the recipients for the NON-VA MEDICATION COMPLEX QUICK ORDER

DIALOG REPORT below.

Send mail to: SERVICE,JOHN// SERVICE,JOHN

Select basket to send to: IN//

And Send to:

\*\*\* SUPPLY ORDERABLE ITEM REPORT QUESTIONS \*\*\*

The post-install will create the SUPPLY ORDERABLE ITEM REPORT, which contains

orderable items that resolve to a pharmacy supply item. For each orderable item,

the report lists the quick order dialogs that reference that orderable item, as

well as the reminder dialogs and definitions that reference either the orderable

item or the quick order that references the orderable item.

The installer is strongly encouraged to include the site's local Clinical

Application Coordinators (CACs) as recipients of this report.

Do you want the NON-VA MEDICATION COMPLEX QUICK ORDER DIALOG REPORT

recipients to also receive the SUPPLY ORDERABLE ITEM REPORT? YES//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

-------------------------------------------------------------------------------

Install Started for OR\*3.0\*350 :

Aug 28, 2013@15:37:55

Build Distribution Date: Aug 21, 2013

Installing Routines:

Aug 28, 2013@15:37:55

Running Pre-Install Routine: PRE^ORY350

Converting ORDER DIALOG OR GTX EARLIEST DATE to OR GTX CLINICALLY INDICATED DATE

Requested Start Time: NOW// (NOV 11, 2015@09:52:26)

Installing Data Dictionaries:

Aug 28, 2013@15:37:55

Installing Data: .

Aug 28, 2013@15:37:56

Installing PACKAGE COMPONENTS:

Installing REMOTE PROCEDURE

Installing OPTION

Installing PARAMETER DEFINITION

Aug 28, 2013@15:38:27

Running Post-Install Routine: POST^ORY350

Updating parameter values...

Setting default value of parameter ORQQPL SUPPRESS CODES to YES

Error setting parameter:

DONE

Correcting supply orderable items...

DONE

Correcting supply quick orders...

DONE

Queueing order cleanup/conversion...

DONE - Task \#290113

Queueing quick order dialog report...

DONE - Task \#290114

Queueing supply orderable item report...

DONE - Task \#290115

Correcting existing order dialogs...

DONE

Loading new notifications...

LAPSED UNSIGNED ORDER

OP NON-RENEWABLE RX RENEWAL

DONE

Updating Routine file...

Updating KIDS files...

OR\*3.0\*350 Installed.

Aug 28, 2013@15:39:07

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

Select Installation \<TEST ACCOUNT\> Option:

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option:

Do you really want to halt? YES//

This email will be generated during the installation:

Subj: CONSULT ORDERS: ID FIELD EDIT  \[#63964\] 02/12/16@11:29  10 lines

From: OR\*3.0\*350 INSTALL  In 'OR' basket.   Page 1

-------------------------------------------------------------------------------

This message contains a list of ORDER file (#100) IENs where the ID field

was edited from EARLIEST to CLINICALLY for the OR GTX EARLIEST DATE Item Entry.

Any unsuccessful edits are also captured and noted as such.

For those orders, you may manually edit the ID field for the

OR GTX CLINICALLY INDICATED DATE Item Entry

Change the value from EARLIEST to CLINICALLY.

Submit a Remedy ticket if you need/prefer assistance with these edits.

No orders found to edit.  If this is the first time this report has been run,

please submit a Remedy ticket for assistance.

Enter message action (in OR basket): Ignore//

### GMRV\*5\*28 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: VA5\$:\[CPRSTEST.V30_TEST_SITES\]GMRV_5_28T5.KID;1

KIDS Distribution saved on Apr 13, 2015@13:51:38

Comment: GMRV\*5.0\*28

This Distribution contains Transport Globals for the following Package(s):

GMRV\*5.0\*28

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

GMRV\*5.0\*28

Use INSTALL NAME: GMRV\*5.0\*28 to install this Distribution.

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

Select Installation \<TEST ACCOUNT\> Option: BACKup a Transport Global

Select INSTALL NAME: GMRV\*5.0\*28 9/27/15@19:00:47

=\> GMRV\*5.0\*28 ;Created on Apr 13, 2015@13:51:38

This Distribution was loaded on Sep 27, 2015@19:00:47 with header of

GMRV\*5.0\*28 ;Created on Apr 13, 2015@13:51:38

It consisted of the following Install(s):

GMRV\*5.0\*28

Subject: Backup of GMRV\*5.0\*28 install on Sep 27, 2015

Replace

Loading Routines for GMRV\*5.0\*28

Routine GMV28PST is not on the disk..

Send mail to: HAWSEY,JASON M// HAWSEY,JASON M

Select basket to send to: IN//

And Send to:

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

Select Installation \<TEST ACCOUNT\> Option: INstall Package(s)

Select INSTALL NAME: GMRV\*5.0\*28 9/27/15@19:00:47

=\> GMRV\*5.0\*28 ;Created on Apr 13, 2015@13:51:38

This Distribution was loaded on Sep 27, 2015@19:00:47 with header of

GMRV\*5.0\*28 ;Created on Apr 13, 2015@13:51:38

It consisted of the following Install(s):

GMRV\*5.0\*28

Checking Install for Package GMRV\*5.0\*28

Install Questions for GMRV\*5.0\*28

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999 HOME

-------------------------------------------------------------------------------

Install Started for GMRV\*5.0\*28 :

Sep 27, 2015@19:01:04

Build Distribution Date: Apr 13, 2015

Installing Routines:

Sep 27, 2015@19:01:04

Running Post-Install Routine: EN^GMV28PST

Updating DLL parameter.

Updating Routine file...

Updating KIDS files...

GMRV\*5.0\*28 Installed.

Sep 27, 2015@19:01:05

Not a production UCI

GMRV\*5.0\*28

Install Completed

### YS\*5.01\*116 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION NAME: XPD INSTALLATION MENU Installation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: Load a Distribution

Enter a Host File: VA5\$:\[CPRSTEST.V30_TEST_SITES\]YS_501_116V2.KID

KIDS Distribution saved on Sep 30, 2014@13:06:39

Comment: YS\*5.01\*116

This Distribution contains Transport Globals for the following Package(s):

Build YS\*5.01\*116 has been loaded before, here is when:

YS\*5.01\*116 Loaded from Distribution

was loaded on

YS\*5.01\*116 Loaded from Distribution

was loaded on

OK to continue with Load? NO// y YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

YS\*5.01\*116

Use INSTALL NAME: YS\*5.01\*116 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 5 Backup a Transport Global

Select INSTALL NAME: YS\*5.01\*116 9/27/15@18:59:33

=\> YS\*5.01\*116 ;Created on Sep 30, 2014@13:06:39

This Distribution was loaded on Sep 27, 2015@18:59:33 with header of

YS\*5.01\*116 ;Created on Sep 30, 2014@13:06:39

It consisted of the following Install(s):

YS\*5.01\*116

Subject: Backup of YS\*5.01\*116 install on Sep 27, 2015

Replace

No routines for YS\*5.01\*116

Send mail to: IRMPERSONNEL, FIVE// IRMPERSONNEL, FIVE

Select basket to send to: IN//

And Send to:

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

Select Installation \<TEST ACCOUNT\> Option: INstall Package(s)

Select INSTALL NAME: YS\*5.01\*116 9/27/15@18:59:33

=\> YS\*5.01\*116 ;Created on Sep 30, 2014@13:06:39

This Distribution was loaded on Sep 27, 2015@18:59:33 with header of

YS\*5.01\*116 ;Created on Sep 30, 2014@13:06:39

It consisted of the following Install(s):

YS\*5.01\*116

Checking Install for Package YS\*5.01\*116

Install Questions for YS\*5.01\*116

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999 HOME

-------------------------------------------------------------------------------

Install Started for YS\*5.01\*116 :

Sep 27, 2015@18:59:54

Build Distribution Date: Sep 30, 2014

Installing Routines:

Sep 27, 2015@18:59:54

Installing PACKAGE COMPONENTS:

Installing OPTION

RPC YTQ SET ANSWER ALL in Option YS BROKER1 \*\*NOT FOUND\*\*

RPC YTQ ADMIN DELETE in Option YS BROKER1 \*\*NOT FOUND\*\*

Installing PARAMETER DEFINITION

Sep 27, 2015@18:59:54

Updating Routine file...

Updating KIDS files...

YS\*5.01\*116 Installed.

Sep 27, 2015@18:59:54

Not a production UCI

YS\*5.01\*116

Install Completed

### XU\*8\*642 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select MailMan Menu \<TEST ACCOUNT\> Option:

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: SYS\$SYSDEVICE:\[USER.COMMAND.JASON\]XU8P642.KID

KIDS Distribution saved on Sep 27, 2015@19:06:59

Comment: XU 642

This Distribution contains Transport Globals for the following Package(s):

XU\*8.0\*642

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

XU\*8.0\*642

Use INSTALL NAME: XU\*8.0\*642 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: BACKup a Transport Global

Select INSTALL NAME: XU\*8.0\*642 9/27/15@19:07:25

=\> XU 642 ;Created on Sep 27, 2015@19:06:59

This Distribution was loaded on Sep 27, 2015@19:07:25 with header of

XU 642 ;Created on Sep 27, 2015@19:06:59

It consisted of the following Install(s):

XU\*8.0\*642

Subject: Backup of XU\*8.0\*642 install on Sep 27, 2015

Replace

Loading Routines for XU\*8.0\*642.

Send mail to: IRMPERSONNEL, FIVE // IRMPERSONNEL, FIVE

Select basket to send to: IN//

And Send to:

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: INstall Package(s)

Select INSTALL NAME: XU\*8.0\*642 9/27/15@19:07:25

=\> XU 642 ;Created on Sep 27, 2015@19:06:59

This Distribution was loaded on Sep 27, 2015@19:07:25 with header of

XU 642 ;Created on Sep 27, 2015@19:06:59

It consisted of the following Install(s):

XU\*8.0\*642

Checking Install for Package XU\*8.0\*642

Install Questions for XU\*8.0\*642

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;999 HOME

XU\*8.0\*642

--------------------------------------------------------------------------------

Install Started for XU\*8.0\*642 :

Sep 27, 2015@19:07:44

Build Distribution Date: Sep 27, 2015

Installing Routines:

Sep 27, 2015@19:07:44

Updating Routine file...

Updating KIDS files...

XU\*8.0\*642 Installed.

Sep 27, 2015@19:07:44

Not a production UCI

NO Install Message sent

-------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

### GMRC\*3.0\*81 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install Started for GMRC\*3.0\*81 :

Mar 04, 2015@14:47:01

Build Distribution Date: Mar 04, 2015

Installing Routines:

Mar 04, 2015@14:47:02

Running Pre-Install Routine: PRE^GMRCPI81

Deleting current DD for REQUEST/CONSULTATION \#123. Data remains intact.

Complete. KIDS will now install the updated DD.

Installing Data Dictionaries:

Mar 04, 2015@14:47:02

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Mar 04, 2015@14:47:02

Updating Routine file...

Updating KIDS files...

GMRC\*3.0\*81 Installed.

Mar 04, 2015@14:47:02

Not a production UCI

NO Install Message sent

### GMTS\*2.7\*112 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install Started for GMTS\*2.7\*112 :

Mar 05, 2015@14:24:34

Build Distribution Date: Mar 04, 2015

Installing Routines:

Mar 05, 2015@14:24:34

Running Post-Install Routine: POST^GMTSP112

Adding "MAS CONTACTS" component to the PDX package

Component successfully added

Adding "MAS MH CLINIC VISITS FUTURE" component to the PDX package

Component successfully added

Adding "MH HIGH RISK PRF HX" component to the PDX package

Component successfully added

Adding "MH TREATMENT COORDINATOR" component to the PDX package

Component successfully added

Updating the DESCRIPTION for the CNB component...

Update completed...

Updating Routine file...

Updating KIDS files...

GMTS\*2.7\*112 Installed.

Mar 05, 2015@14:24:35

Not a production UCI

NO Install Message sent

### OR\*3.0\*424 Install Capture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: or\*3.0\*424 2/11/16@12:02:53

=\> OR\*3\*424 ;Created on Jan 28, 2016@10:05:01

This Distribution was loaded on Feb 11, 2016@12:02:53 with header of

OR\*3\*424 ;Created on Jan 28, 2016@10:05:01

It consisted of the following Install(s):

OR\*3.0\*424

Checking Install for Package OR\*3.0\*424

Install Questions for OR\*3.0\*424

Incoming Files:

101.41 ORDER DIALOG (including data)

> **NOTE:** You already have the 'ORDER DIALOG' File.

I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

--------------------------------------------------------------------------------

Install Started for OR\*3.0\*424 :

Feb 11, 2016@12:07:12

Build Distribution Date: Jan 28, 2016

Installing Routines:

Feb 11, 2016@12:07:12

Installing Data Dictionaries:

Feb 11, 2016@12:07:12

Installing Data: .................................................

Feb 11, 2016@12:07:14

Updating Routine file...

Updating KIDS files...

OR\*3.0\*424 Installed.

Feb 11, 2016@12:07:14