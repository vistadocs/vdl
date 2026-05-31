---
title: OR*3*519 CPRS Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*519
group_key: CPRS:OR:3
file_numbers:
- '2'
- '19'
security_keys:
- PROVIDER
menu_options: 0
description: The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications,
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 4509
section_count: 15
table_count: 2
figure_count: 0
appendix_count: 2
has_toc: false
is_stub: false
pub_date: November 2020
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/OR_30_519_dibr.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/OR_30_519_dibr.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=338
audit_applied: '2026-05-31'
master_source: OR*3*519 CPRS Deployment, Installation, Back-Out, and Rollback Guide
master_pub_date: November 2020
consolidated_from: 4 versions
prior_versions:
- OR*3*437 CPRS Deployment, Installation, Back-Out, and Rollback Guide
- OR*3*542 CPRS Deployment, Installation, Back-Out, and Rollback Guide
- OR*3*546 CPRS Deployment, Installation, Back-Out, and Rollback Guide
consolidated_title: cprs deployment, installation, back-out, and rollback guide
---

Deployment, Installation, Back Out and Rollback Guide

![](or-3-519-cprs-deployment-installation-back-out-and-rollback-guide/001.png)

November 2020

Office of Information & Technology (OI&T)

Enterprise Program Management Office (EPMO)

This page left intentionally blank.

Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 52%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2020</td>
<td><p>0.10</p>
<p>0.09</p>
<p>0.08</p>
<p>0.07</p>
<p>0.06</p>
<p>0.05</p>
<p>0.04</p>
<p>0.03</p></td>
<td><p>Added <a href="#appendix-b-disabling-pdmp-functionality">Appendix B: Disabling PDMP Functionality</a></p>
<p>Updated for V312.1</p>
<p>Updated for v311.1</p>
<p><a href="#decision-support-tool-dst-andor-consult-toolbox-ctb-features">New DST Notification</a></p>
<p>Added DST Notification</p>
<p>Updated for v310.1</p>
<p>Updated for v309.1</p>
<p>Inserted text that <a href="#_Pre-requisite_Patches">OR*3*533 patch must be installed first</a> before any other patch</p>
<p>Updated date on Title page and in footers</p>
<p>Incorporated v308.1 updates from Developer (added Section 6.3.1 <a href="#decision-support-tool-dst-andor-consult-toolbox-ctb-features">Enable Decision Support Tool (DST) and/or Consult Toolbox (CTB) Feature</a>)</p>
<p>Rearranged TOC with Pre-Installation Steps, Installation Procedure, and Post-Installation Steps under <a href="#_Installation">Section 6 Installation</a></p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>7/2020</td>
<td>0.02</td>
<td>Removed incorrect information from Section 4, <a href="#cprs-v31ma-installation-checklist">Pre-Installation Steps</a>.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>6/2020</td>
<td>0.01</td>
<td>Initial Draft version</td>
<td>REDACTED</td>
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
    - [Description](#description)
  - [Document Conventions](#document-conventions)
  - [Related Documents](#related-documents)
- [Pre-requisites](#pre-requisites)
- [Reporting Issues](#reporting-issues)
- [CPRS v31MA Installation Checklist](#cprs-v31ma-installation-checklist)
- [Software Retrieval](#software-retrieval)
- [Installation](#installation)
  - [Pre-Installation Steps](#pre-installation-steps)
    - [Confirm Installation of Patch XOBW\1.0\6](#confirm-installation-of-patch-xobw106)
    - [Backup Procedures](#backup-procedures)
    - [Disable Ordering during Installation](#disable-ordering-during-installation)
  - [Installation Procedure](#installation-procedure)
    - [CPRS v31MA Combined Build 1.0 Required Patches](#cprs-v31ma-combined-build-10-required-patches)
    - [CPRS GUI v31MA COMBINED BUILD 1.0 – Host file (CPRSV31MACOMBINEDBUILD.KID)](#cprs-gui-v31ma-combined-build-10-host-file-cprsv31macombinedbuildkid)
    - [Methods of installation](#methods-of-installation)
    - [Decision Support Tool (DST) and/or Consult Toolbox (CTB) Features](#decision-support-tool-dst-andor-consult-toolbox-ctb-features)
    - [Enable Ordering for Testers](#enable-ordering-for-testers)
    - [Enabling Ordering for All Users](#enabling-ordering-for-all-users)
    - [CPRS Documentation](#cprs-documentation)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
- [Appendix A: Web Server Post-Installation Check](#appendix-a-web-server-post-installation-check)
  - [A1 Add Web Server Entry](#a1-add-web-server-entry)
- [Appendix B: Disabling PDMP Functionality](#appendix-b-disabling-pdmp-functionality)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient's allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) Information Technology (IT) Operations and Services staff.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation guide provides instructions for:

- Installing application components that run on M servers at VAMC facilities
- Installing Windows executable programs on workstations, network shares, or the Citrix gateway

### Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is part of the CPRS v31.MA updates. Below is a list of all the applications involved in this project along with their patch numbers:

> <u>APPLICATION/VERSION</u> <u>PATCH</u>

> ORDER ENTRY/RESULTS REPORTING v3.0 OR\*3.0\*519

> TEXT INTEGRATION UTILITIES v1.0 TIU\*1.0\*328

> CONSULT/REQUEST TRACKING v3.0 GMRC\*3.0\*145

> HEALTH SUMMARY v2.7 GMTS\*2.7\*134

The patches (OR\*3.0\*519, TIU\*1.0\*328, GMRC\*3.0\*145, and GMTS\*2.7\*134) are being released in the Kernel Installation and Distribution System (KIDS) multi-package build CPRS V31MA COMBINED BUILD 1.0.

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Examples of VistA "Roll and Scroll" interface actions will be shown in a box such as this:

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

Emphasis of important points may be displayed in this manner:

> **NOTE:** This is an important point and must not be omitted.

Call-outs may be used to draw attention to part of a block of text or a table without disrupting the flow of the block or table. For example:

> ![](or-3-519-cprs-deployment-installation-back-out-and-rollback-guide/002.png)

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents will be available on the VA Software Document Library (VDL) when the patch is released:

[CPRS on the VDL](http://www.va.gov/vdl/application.asp?appid=61)

- *CPRS User Guide: GUI Version*
- *CPRS Technical Manual*
- *CPRS Technical Manual: GUI Version*
- *CPRS v31MA Release Notes*
- *CPRS v31MA Installation Guide*

# Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before beginning the processes described in this document the patches listed here must be installed:

<span id="_Pre-requisite_Patches" class="anchor"></span>(v) OR\*3\*350 install BEFORE patch OR\*3\*519

\(v\) OR\*3\*377 install BEFORE patch OR\*3\*519

\(v\) OR\*3\*415 install BEFORE patch OR\*3\*519

\(v\) OR\*3\*441 install BEFORE patch OR\*3\*519

\(v\) XOBW\*1\*6 install BEFORE patch OR\*3\*519

\(v\) OR\*3\*528 install BEFORE patch OR\*3\*519

\(v\) OR\*3\*533 install BEFORE patch OR\*3\*519

CPRS v31 Mission Act expects a fully patched VistA system.

> **NOTE:** You *must* confirm XOBW\*1.0\*6 has been installed, please refer to "*Section 6.1.1: "[Confirm Installation of Patch XOBW\*1.0\*6](#confirm-installation-of-patch-xobw1.06)*"  

# Reporting Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To report issues with CPRS v31MA, please call the CPRS Development Team members or use the REDACTED.

# CPRS v31MA Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order.

Table 1 Installation Checklist

<table>
<caption>Installation Check List</caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 72%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>No.</strong></th>
<th><strong>Item</strong></th>
<th><strong>Done</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><strong>Test/Mirror System Installation</strong></td>
<td></td>
</tr>
<tr class="even">
<td><ol type="1">
<li></li>
</ol></td>
<td>Confirm all Pre-requisite patches have been installed in your Test/Mirror system (see Section <strong>Error! Reference source not found.</strong>, <a href="#_Pre-requisite_Patches">Pre-requisite Patches</a>, <strong>Error! Reference source not found.</strong>)</td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><p>Confirm the following information is available before beginning the installation: IP/Domain Name of the PDMP Server, Port, Username, password, and SSL/TLS Configuration.</p>
<p>An encrypted email was sent out to the ITOPS installers with this information. If you did not receive it, please reach out to the CPRS implementation team (use the mail group: OIT PD CPRS Implementation Team REDACTED).</p>
<p><strong>NOTE: You will be prompted to enter this information during the patch installation.</strong></p></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><p>Download and install the CPRS v31MA bundle of patches</p>
<p>(CPRS_V31MA_COMBINED_BUILD.KID)</p></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td>Verify that the installation in your Test/Mirror system has been successful</td>
<td></td>
</tr>
</tbody>
</table>

Installation Check List

# Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches will be sent as host files. The table below will show in what form the patch will be distributed. The necessary files are:

Table 1 CPRS v31MA files

| CPRS Version files to be downloaded | File Contents / Supported Functionality |
|-----------------------------------------|---------------------------------------------|
| CPRS_V31MA_COMBINED_BUILD.KID           | Required patches for the CPRS v31MA Release |
| OR_30_519.ZIP                           | CPRSCHART.EXE                               |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section gives instructions for installing CPRS v31MA. Sites should disable ordering, install the patches, distribute the GUI, re-enable ordering for testers, re-enable ordering for all users.

## Pre-Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before this installation proceeds, the steps below need be done by Information Technology Operations and Support (ITOPS) and other groups. Once these set up items are completed, installation can proceed.

### Confirm Installation of Patch XOBW\*1.0\*6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Confirm that patch XOBW\*1.0\*6 was installed and all of the instructions for setup have been completed. That patch had instructions for creating a new SSL/TLS configuration, "encrypt_only_tlsv12," on both front-end server nodes and database server nodes.

To perform this check you will need to:

- Coordinate with your site's respective system administration group (e.g. Region Operation Center) to receive assistance in performing the SSL Configuration verification check.
- Ask the system administrator to check that the SSL/TLS configuration has been installed in all nodes. The system administrator (with a Programmer Support account) will need one of the following roles (e.g. greater than %Developer role) to perform the check:
  - %All
  - %Manager

> Example of determining Roles currently held:

\>W \$ROLES

\>%All,%Developer

> To check if the "encrypt_only_tlsv12" SSL Configuration exists on a node, enter the following code at the programmer prompt:

> \>D CHCKEXST^XOBWP004("encrypt_only_tlsv12")

- If you get something similar to below displayed on all nodes, where Protocols is equal to '16,' you are good to go and can proceed with installing patch CPRS V31MA COMBINED BUILD 1.0:

> \>D CHCKEXST^XOBWP004("encrypt_only_tlsv12")

>                  Configuration Values

>          CAFile               :

>          CAPath               :

>          CRLFile              :

>          CertificateFile      :

>          CipherList           : ALL:!aNULL:!eNULL:!EXP:!SSLv2

>          Description          : XOBW\*1.0\*6

>          Enabled              : 1

>          PrivateKeyFile       :

>          PrivateKeyPassword   :

>          PrivateKeyType       : 2

>          Protocols            : 16

>          Type                 : 0

>          VerifyDepth          : 9

>         VerifyPeer         : 0

- If you get the following, you will need to go back to the XOBW\*1.0\*6 patch instructions and complete the setup before proceeding with the installation of patch CPRS V31MA COMBINED BUILD 1.0:

> \>D CHCKEXST^XOBWP004("encrypt_only_tlsv12")

>    \>\>\>\>  'encrypt_only_tlsv12' SSL Config doesn't exist.

- If you get an error resembling the following, you do not have sufficient roles assigned and you will need to contact your Cache System Administrator with a sufficient role to perform this check:

> \>D CHCKEXST^XOBWP004("encrypt_only_tlsv12")

> .S \$NAMESPACE="%SYS" ;Change namespace, revert back upon "Q"

>  ^

> \<PROTECT\>EXISTS+6^XOBWP004 \*/opt/cachesys/mgr/

### Backup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to [Step b](#Backup). under Section 6.2.2 "CPRS GUI v31MA COMBINED BUILD 1.0 – Host file (CPRS_V31MA_COMBINED_BUILD.KID)"

### Disable Ordering during Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is best to ensure that users cannot enter orders while the CPRS software is being updated. To help with this, there is a parameter that disables ordering in CPRS. Disabling ordering should be done before installation begins.

Ordering can then be enabled for testing immediately after installation. The following example shows how to disable ordering for the SYSTEM level.

CHOOSE 1-3: 2  ORWOR DISABLE ORDERING   Disable Ordering in GUI

 

ORWOR DISABLE ORDERING may be set for the following:

 

     2   User          USR    \[choose from NEW PERSON\]

     5   System        SYS    \[ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV\]

     10  Package       PKG    \[ORDER ENTRY/RESULTS REPORTING\]

 

Enter selection: 5  System   ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV

 

 Setting ORWOR DISABLE ORDERING  for System: ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV

Disable Ordering: YES

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CPRS v31MA Combined Build 1.0 Required Patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following list of patches are part of CPRS v31MA COMBINED BUILD 1.0. There is no need to install them individually.

> OR\*3.0\*519

> TIU\*1.0\*328

> GMRC\*3.0\*145

> GMTS\*2.7\*134

### CPRS GUI v31MA COMBINED BUILD 1.0 – Host file (CPRS_V31MA_COMBINED_BUILD.KID)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All patches listed in section 6.2.1 are part of a single host file for CPRS v31MA.

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

> **NOTE:** Confirm the following information is available before beginning the installation: IP/Domain Name of the PDMP Server, Port, Username, password, and SSL/TLS Configuration. You will be prompted to enter this information during the patch installation. An encrypted email was sent out to the ITOPS installers with this information. If you did not receive it, please reach out to the CPRS implementation team (use the mail group: OIT PD CPRS Implementation Team REDACTED).

<span class="mark">NOTE: Do not queue the install.</span>

1.  Use the Load a Distribution option contained on the Kernel Installation and Distribution System Menu to load the Host file.
    1.  When prompted to "Enter a Host File:" enter

/srv/vista/patches/SOFTWARE/CPRS_V31MA_COMBINED_BUILD.KID

2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you should run the following options. When prompted for the INSTALL NAME enter CPRS V31MA COMBINED BUILD 1.0.

> NOTE: Using \<spacebar\>\<enter\> will not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build:

1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global.
2.  <span id="Backup" class="anchor"></span>Select the Backup a Transport Global option to create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
3.  You may also elect to use the following options:
    1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install:
    1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.

> ALERT: Do NOT use the Production Account Settings in your test account as this may send test patient information to the PDMP production system, and similarly, do not use the Test Account settings in the production account as this may send real patient information to the PDMP test system.

> <span class="mark">NOTE:</span> If any of the responses related to the PDMP questions are accidentally mistyped, or by mistake skipped, refer to "[*Appendix A: Web Server Post-Installation Check*](#appendix-a-web-server-post-installation-check)" on how to rectify it.

2.  When prompted 'Enter the IP address or domain name of the PDMP server:' answer with the IP/Domain name you were provided.
3.  When prompted 'Enter the port number for the PDMP server: (1-99999):', answer with the port you were provided with.
4.  When prompted 'Enter the username for the PDMP server:' answer with the username you were provided with.
5.  When prompted 'Enter the password for the PDMP server:' answer with the password you were provided with.
6.  When prompted 'Enter the SSL/TLS Configuration:' answer with "encrypt_only_tlsv12" (without quotes).
7.  When prompted 'When rebuilding the Health Summary Adhoc Report, do you want to include disabled components?' answer either YES or NO as appropriate for your site.

> NOTE: If your site has any components that are temporarily disabled (rather than permanently disabled) and you plan to enable them in the future, you may want to answer YES at this prompt. Keep in mind that you can rebuild the Adhoc Report at any time in the future, at which point you are prompted again whether to include disabled components.

8.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
9.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.
10. When prompted 'Delay Install (Minutes): (0 - 60): 0//', answer 0.

### Methods of installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites have used primarily four methods to distribute the application. Each site will need to decide how they will install. This decision is typically made by the ITOPS and Client Desktop teams.

- Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the CPRS v31MA (CPRSChart.exe) across the network.

> The GUI executable (CPRSChart.exe) and help file system are copied to a network shared location. Users are provided with a desktop shortcut to run CPRS v31MA directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the "Target" field of the shortcut properties.

> At the time of a CPRS version update the copy of CPRSChart.exe and the help file system are replaced, on the network share, with the new version.

> For the DLLS, each site will coordinate with ITOPS to determine where the DLLs will be placed. The DLLs must be available on the local search path, and all previous versions of the DLLs must be removed. For example, some sites may choose to have the DLLs in the same network share as the CPRS executable itself. Others might choose to put them in the Program Files\VistA\Shared Files directory. Sites will need to choose where to put them.

> Any users requiring access to another site's CPRS system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of CPRSChart.exe (e.g. for testing purposes), a different version of CPRSChart.exe can be placed in a separate network location and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

- Citrix installation:

> The GUI executable (CPRSChart.exe), help file system, and the DLLs are installed and run from a remote workstation, and the user views the remote workstation's screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> NOTE: For issues with CAG, please contact the local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

- Gold Path installation:

> This is where the new executable is placed in a common shared location (called a gold path) and updated when the CPRS GUI is first accessed from the local workstation. This method is handled though desktop enterprise services.

- Local workstation installation:

> This is an installation method where the GUI executable (CPRSChart.exe), help file system, and DLLs are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via SCCM. A National package, (CPRS 1.31.311.1) has been prepared and made available to Regional COR Client Technologies leadership.

- Manual install:

  This is a situation which is used primarily for advanced users and at testing locations. This method is somewhat changed from that used previously for Windows XP workstations. For more detail please refer to section *6.2.3.1Manual Installation* below.

#### Manual Installation

This method is used for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.

1.  Locate the ZIP file for OR\*3\*519 and unzip the file.
2.  Copy the contents of the zip archive (the GUI and the help file system) to a test directory, for example, C:\cprstest. A new directory may need to be created.

> NOTE: Administrator rights are required for the PC used to complete this step.

3.  Create a Shortcut and name it "Test CPRSv31MA." This is to give the user another visual cue that this is not the normal CPRS icon.

    ![](or-3-519-cprs-deployment-installation-back-out-and-rollback-guide/003.png)
4.  Copy the borlandmm.dll file into the same directory as cprschart.exe (for example, c:\cprstest). This file should be in the same directory as the CPRSChart.exe for CPRS v31MA.
5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  Enter IP and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

> ![](or-3-519-cprs-deployment-installation-back-out-and-rollback-guide/004.png)

Example of what the shortcut properties dialog might look like.

The server and port number shown above are not real and are for example only.

#### ## Post-Installation Steps

### Decision Support Tool (DST) and/or Consult Toolbox (CTB) Features 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The integrated DST/CTB features in this version of CPRS GUI are installed as disabled/off. At the time of this writing, it has not been determined exactly when these features should be enabled in production systems. At some point in the future, VAMCs can expect to receive information about when and how to enable the integrated DST/CTB features of CPRS GUI.

### Enable Ordering for Testers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once CPRS v31MA COMBINED BUILD 1.0 is installed, sites can enable testing for the specific users that will be testing before all users are allowed on the system.

Below is an example of how to change the parameter at the USER level.

ORWOR DISABLE ORDERING may be set for the following:

 

     2   User          USR    \[choose from NEW PERSON\]

     5   System        SYS    \[ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV\]

     10  Package       PKG    \[ORDER ENTRY/RESULTS REPORTING\]

 

Enter selection: 2  User   NEW PERSON

Select NEW PERSON NAME: CPRSPROVIDER,TWO CPRSPROVIDER,TWO    TC   PROVIDER

 

---------- Setting ORWOR DISABLE ORDERING  for User: CPRSPROVIDER,TWO ---------

Disable Ordering: NO

> **NOTE:** Enable all users that will be testing before all users have ordering enabled.

### Enabling Ordering for All Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When testing is complete and the site is comfortable, the site should enable ordering for all users as shown below.

ORWOR DISABLE ORDERING may be set for the following:

 

     2   User          USR    \[choose from NEW PERSON\]

     5   System        SYS    \[ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV\]

     10  Package       PKG    \[ORDER ENTRY/RESULTS REPORTING\]

 

Enter selection: 5  System   ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV

 

 Setting ORWOR DISABLE ORDERING  for System: ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV

Disable Ordering: YES// @  ...deleted

 

ORWOR DISABLE ORDERING may be set for the following:

 

     2   User          USR    \[choose from NEW PERSON\]

     5   System        SYS    \[ONEBCE.DEVSLC.FO-SLC.MED.VA.GOV\]

     10  Package       PKG    \[ORDER ENTRY/RESULTS REPORTING\]

### CPRS Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to standardized software document changes and VDL updates, the CPRSv31MissionAct documentation will be released and stored with the software on the network share site for 45 day compliance period. The documents will then be loaded and stored on the VDL. The documents and manuals may be downloaded from <https://www.va.gov/vdl/section.asp?secid=1>

| File Name      | Document                         |
|--------------------|--------------------------------------|
| CPRSGUIUM.PDF      | CPRS User Guide: GUI Version         |
| CPRSLMTM.PDF       | CPRS Technical Manual                |
| CPRSGUITM.PDF      | CPRS Technical Manual: GUI Version   |
| OR_30_519_RN.PDF   | CPRS GUI v31 MA (Patch OR\*3.0\*519) |
| OR_30_519_DIBR.PDF | CPRS GUI v31 MA Installation Guide   |

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a major issue with the patch, the Area Manager may make the decision to back-out the patch. However, this decision should include both Health Product Support and the CPRS development team

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back out the changes associated with CPRS V31MA COMBINED BUILD 1.0, personnel would install OR_3_508_V31MA_V311_BACKOUT.KID to back out all of the patches installed with CPRS V31MA COMBINED BUILD 1.0. For assistance, please contact the CPRS implementation team (use the mail group: OIT PD CPRS Implementation Team REDACTED).

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These patches should be backed out only if they cause a catastrophic failure of the system.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out the patches involved with CPRS v31MA COMBINED BUILD 1.0 (Patch \# OR\*3.0\*519) would affect many different parts of CPRS and VistA. For more information about all the changes in CPRS v31MA COMBINED BUILD 1.0, please reference the *CPRS v31MARelease Notes (Patch \# OR\*3.0\*519)*, which can be obtained from the [VA Software Document Library](https://www.va.gov/vdl/). However, installing the OR\*3.0\*508 patch should return CPRS and VistA to the state it was in prior to the installation of CPRS v31MA COMBINED BUILD 1.0 (Patch \# OR\*3.0\*519).

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Area Manager has the ultimate responsibility for the decision to back out the two patches and revert to a previous version. The Area Manager should consult with the medical center clinical staff, CPRS Development team, and Health Product Support Clinical personnel before backing out the patches.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To back out the features with CPRS v31MA COMBINED BUILD 1.0, a back out patch was created which should uninstall all of the patches installed with CPRS v31MA COMBINED BUILD 1.0 and return the system to a previous state. To back out CPRS v31MA COMBINED BUILD 1.0 (Patch \# OR\*3.0\*519), follow these steps:

1.  Load and Install the OR_3_508.KID host file
2.  If any files were backed up in Step 6, restore them now.
3.  Re-install released patch OR\*3.0\*528 SEQ#452
4.  Remove the CPRS v31MA executable (cprschart.exe) and redistribute the CPRS v31b executable.
5.  Check the desktop icons to see if any adjustments need to be made.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the rollback has been successful, check that the option is back at 1.31.266.2. Use VA FileMan to check that MENU TEXT field of the OR CPRS GUI CHART option in the OPTION file (#19) has been reset to 1.31.266.2.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback is required for this installation.

# Appendix A: Web Server Post-Installation Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After successfully installing patch OR\*3.0\*519, a user can validate that the post-install routine added the PDMP Web Server and Web Service entries correctly. If needed, edits to the server domain name, SSL Port, Username, Password, or SSL Configuration can be made here.

1.  Run option Web Server Manager \[XOBW WEB SERVER MANAGER\].
2.  There should be a Web Server "PDMP SERVER" (in production) or "PDMP TEST SERVER" (in test). If not, please see instructions in REDACTED on how to create one.
3.  Choose action "Edit Server" (ES).
4.  When prompted, "Select Web Server:" answer with the ID for "PDMP SERVER" or "PDMP TEST SERVER."
5.  Enter through the prompts. If needed, you can edit the responses.

> <u>Web Server Manager            Jun 16, 2020@11:01:35          Page:    1 of    1</u>

>                        HWSC Web Server Manager

>                       Version: 1.0     Build: 9

> <u>ID    Web Server Name           IP Address or Domain Name:Port                </u>

>  1    \*PDMP SERVER               xxxxxxxxxxxx.xx.xxx:xxx (SSL)               

>           Legend:  \*Enabled                                                    

> AS  Add Server                          TS  (Test Server)

> ES  Edit Server                         WS  Web Service Manager

> DS  Delete Server                       CK  Check Web Service Availability

> EP  Expand Entry                        LK  Lookup Key Manager

> Select Action:Quit// ES   Edit Server 

> Select Web Server:  (1-12): 1

> NAME: PDMP SERVER//

> SERVER: xxxxxxxxxxxx.xx.xxx  Replace

> PORT: 80// ( This can be ignored, as we are only using the SSL PORT below)

> DEFAULT HTTP TIMEOUT: 180//

> STATUS: ENABLED//

> Security Credentials

> ====================

> LOGIN REQUIRED: YES//

> USERNAME: USERNAME//

> Want to edit PASSWORD (Y/N):

> SSL Setup

> =========

> SSL ENABLED: TRUE//

> SSL CONFIGURATION: encrypt_only_tlsv12//

> SSL PORT: 443//

> Authorize Web Services

> ======================

> Select WEB SERVICE: PDMP WEB SERVICE//

>   WEB SERVICE: PDMP WEB SERVICE//

>   STATUS: ENABLED//

> Select WEB SERVICE:

## A1 Add Web Server Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the post-install was not be able to create the "PDMP SERVER" (in production) or "PDMP TEST SERVER" (in test) Web Server entry (for example, if some of the install questions related to these entries were not answered during the installation), the following instructions will explain how to manually create them:

1.  Run option Web Server Manager \[XOBW WEB SERVER MANAGER\].
2.  Choose action "Web Service Manager" (WS).
3.  Choose action "Add Service" (AS).
4.  When prompted, "Select WEB SERVICE NAME," answer with "PDMP WEB SERVICE"
5.  When prompted, "Are you adding 'PDMP WEB SERVICE' as a new WEB SERVICE (the 14TH)? No//" answer with "YES"
6.  When prompted, "NAME: PDMP WEB SERVICE///" hit \[Enter\] to take the default
7.  When prompted, "DATE REGISTERED:" answer with "NOW"
8.  When prompted, "TYPE:" answer with "REST"
9.  When prompted, "CONTEXT ROOT:" answer with "csp/resthsb/pdmp/PDMP.API.REST"
10. When prompted, "AVAILABILITY RESOURCE" don't enter a response, and hit \[Enter\].

> <u>Web Service Manager           Jun 16, 2020@11:17:28          Page:    1 of    1</u>

>                        HWSC Web Service Manager

>                       Version: 1.0     Build: 9

> <u>ID    Web Service Name           Type   URL Context Root                      </u>

>  1     TEST WEB SERVICE           REST   /TEST/

>           Enter ?? for more actions                                            

> AS  Add Service

> ES  Edit Service

> DS  Delete Service

> EP  Expand Entry

> Select Action:Quit// AD   Add Service 

> Select WEB SERVICE NAME: PDMP WEB SERVICE

>   Are you adding 'PDMP WEB SERVICE' as a new WEB SERVICE (the 14TH)? No// Y  (Yes)

> NAME: PDMP WEB SERVICE//

> DATE REGISTERED: NOW  (JUN 16, 2020@11:18:06)

> TYPE: REST

> CONTEXT ROOT: csp/resthsb/pdmp/PDMP.API.REST

> AVAILABILITY RESOURCE:

11. When prompted, "Select Action:" answer with "Quit." This should take you back to the Web Server Manager.
12. Choose action "Add Server" (AS).
13. When prompted, "Select WEB SERVER NAME:" answer with "PDMP SERVER" (in the test account, answer with "PDMP TEST SERVER")
14. When prompted, "Are you adding 'PDMP SERVER' as a new WEB SERVER (the 13TH)? No//" answer with "YES"
15. When prompted, "NAME: PDMP SERVER//" hit \[Enter\] to take the default.

> ALERT: Do NOT use the Production Account Settings in your test account as this may send test patient information to the PDMP production system. 

16. When prompted, "SERVER:" answer with the domain name of the PDMP server.
17. When prompted, "PORT: 80//" hit \[Enter\] to take the default. (We do not use this port. We only use the SSL Port below).
18. When prompted, "DEFAULT HTTP TIMEOUT: 30//" answer with "180"
19. When prompted, "STATUS:" answer with "ENABLED"
20. When prompted, "LOGIN REQUIRED:" answer with "YES"
21. When prompted, "USERNAME:" answer with the username for the PDMP server.
22. When prompted, "Want to edit PASSWORD (Y/N):" answer with "Y"
23. When prompted, "Enter a new PASSWORD:" answer with the password for the PDMP server.
24. When prompted, "Please re-type the new password to show that I have it right:" re-type the password.
25. When prompted, "SSL ENABLED: FALSE//" answer with "TRUE"
26. When prompted, "SSL CONFIGURATION:" answer with "encrypt_only_tlsv12"
27. When prompted, "SSL PORT" answer with the PDMP port.
28. When prompted, "Select WEB SERVICE:" answer with "PDMP WEB SERVICE"
29. When prompted, "Are you adding 'PDMP WEB SERVICE' as a new AUTHORIZED WEB SERVICES (the 1ST for this WEB SERVER)? No//" answer with "YES"
30. When prompted, "STATUS:" answer with "ENABLED"
31. When prompted, "Select WEB SERVICE:" don't enter a response, and hit \[Enter\].

> <u>Web Server Manager            Jun 16, 2020@11:13:48          Page:    1 of    1</u>

>                        HWSC Web Server Manager

>                       Version: 1.0     Build: 9

> <u>ID    Web Server Name           IP Address or Domain Name:Port                </u>

>  1    \*TEST SERVER               xxxxxxxxxxxx.xx.xxx:xxx (SSL)

>           Legend:  \*Enabled                                           

> AS  Add Server                          TS  (Test Server)

> ES  Edit Server                         WS  Web Service Manager

> DS  Delete Server                       CK  Check Web Service Availability

> EP  Expand Entry                        LK  Lookup Key Manager

> Select Action:Quit// AS   Add Server 

> Select WEB SERVER NAME: PDMP SERVER  (In the Test account this should be PDMP TEST SERVER)

>   Are you adding 'PDMP SERVER' as a new WEB SERVER (the 13TH)? No// Y  (Yes)

> NAME: PDMP SERVER//

> SERVER: xxxxxxxxxxxx.xx.xxx

> PORT: 80// (This can be ignored, as we are only using the SSL PORT below)

> DEFAULT HTTP TIMEOUT: 30// 180

> STATUS: ENABLED

> Security Credentials

> ====================

> LOGIN REQUIRED: YES

> USERNAME: USERNAME

> Want to edit PASSWORD (Y/N): Y

> Enter a new PASSWORD: \*\*\*\*\*\*\*\*

> Please re-type the new password to show that I have it right: \*\*\*\*\*\*\*\*

> Ok, password has been changed!

> SSL Setup

> =========

> SSL ENABLED: FALSE// TRUE

> SSL CONFIGURATION: encrypt_only_tlsv12

> SSL PORT: xxx

> Authorize Web Services

> ======================

> Select WEB SERVICE: PDMP WEB SERVICE 

>   Are you adding 'PDMP WEB SERVICE' as

>     a new AUTHORIZED WEB SERVICES (the 1ST for this WEB SERVER)? No// Y  (Yes)

>   STATUS: ENABLED

> Select WEB SERVICE:

# Appendix B: Disabling PDMP Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PDMP feature is installed as enabled/on. If it is determined that a site or division needs to disable or hide the PDMP functionality, the following two parameters can be used.

1.  The OR PDMP TURN ON parameter can be used to disable the PDMP functionality entirely. Setting it to disabled/off, will remove the PDMP functionality entirely from CPRS (it will remove the PDMP Query button from the ribbon bar and the Tools menu). It can be configured at the System and Division levels.
2.  The OR PDMP SHOW BUTTON can be used if a site wants to leave the PDMP functionality enabled but hidden. Setting it to RESULTS ONLY will remove the PDMP Query button from the ribbon bar, but leave it on the Tools Menu. It can be configured at the System, Division, or User levels.

Example Disabling PDMP at the System Level

Select CPRS Configuration (IRM) Option: XX  General Parameter Tools

   LV     List Values for a Selected Parameter

   LE     List Values for a Selected Entity

   LP     List Values for a Selected Package

   LT     List Values for a Selected Template

   EP     Edit Parameter Values

   ET     Edit Parameter Values with Template

   EK     Edit Parameter Definition Keyword

Select General Parameter Tools Option: EP  Edit Parameter Values

                         --- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: OR PDMP TURN ON  PDMP functionality turn on

OR PDMP TURN ON may be set for the following:

     3   Division      DIV    \[choose from INSTITUTION\]

     6   System        SYS    \[EXAMPLE.TEST.VA.GOV\]

Enter selection: 6  System   EXAMPLE.TEST.VA.GOV

------- Setting OR PDMP TURN ON  for System: EXAMPLE.TEST.VA.GOV -------

Value: NO

Example Removing the PDMP Query Button From the Ribbon Bar

Select CPRS Configuration (IRM) Option: XX  General Parameter Tools

   LV     List Values for a Selected Parameter

   LE     List Values for a Selected Entity

   LP     List Values for a Selected Package

   LT     List Values for a Selected Template

   EP     Edit Parameter Values

   ET     Edit Parameter Values with Template

   EK     Edit Parameter Definition Keyword

Select General Parameter Tools Option: EP  Edit Parameter Values

                         --- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: OR PDMP SHOW BUTTON     PDMP SHOW BUTTON

OR PDMP SHOW BUTTON may be set for the following:

     1   User          USR    \[choose from NEW PERSON\]

     5   Division      DIV    \[choose from INSTITUTION\]

     7   System        SYS    \[EXAMPLE.TEST.VA.GOV\]

Enter selection: 7  System   EXAMPLE.TEST.VA.GOV

----- Setting OR PDMP SHOW BUTTON  for System: EXAMPLE.TEST.VA.GOV -----

Value: RESULTS ONLY

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: OR*3*546 CPRS Deployment, Installation, Back-Out, and Rollback Guide

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install the Veterans Information Systems and Technology Architecture (VistA) ORDER ENTRY/RESULTS REPORTING, Massachusetts General Hospital Utility Multi-Programming System (MUMPS) portion of the Computerized Patient Record System (CPRS) patch OR\*3.0\*546, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

The SHRPE product makes enhancements to the CPRS to implement functionality that would assist CPRS users with the treatment of former service members with an Other Than Honorable (OTH) administrative discharge.

This patch adds the following functionality:

1.  The existing text "Call Registration Team for Details." will continue to be displayed in the OTH Button in CPRS Graphical User Interface (GUI). It cannot be edited or deleted. In addition to it, this patch will allow local users to provide their own local instructions and information such as phone numbers of the VA site's staff that can provide an assistance with managing OTH patients' statuses.
2.  A new GUI Parameter, OR OTH BTN LOCAL MSG will be created in the PARAMETER DEFINITION File (#8989.5) to store the localized OTH information.
3.  The new menu option GUI Add/Edit Local Message for OTH Button \[OR OTH BTN MSG ADD/EDIT\] will be added to CPRS menu GUI Parameters \[ORW PARAM GUI\] in VistA to allow users to enter or update the localized OTH information. The user will be able to enter or edit two lines of the localized OTH information.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the VistA ORDER ENTRY/RESULTS REPORTING patch OR\*3.0\*546 will be deployed and installed, as well as specific instructions for how it is backed out and rolled back, if necessary. The plan also identifies resources, a communication plan, and a rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*1035 must be installed before OR\*3.0\*546 for users to use the functionality provided by OR\*3.0\*546.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be installed in all VA VistA production sites. This patch is intended for a fully patched VistA system. Its installation will not noticeably impact the production environment.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The duration of deployment and installation is 30 days. A detailed schedule will be provided during the build.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the OR\*3.0\*546 patch deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA ORDER ENTRY/RESULTS REPORTING patch OR\*3.0\*546 should be installed in all VA VistA production sites.

### Site Information (Locations and Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The test sites for IOC testing are:

- VA Loma Linda Healthcare System (Loma Linda, California) (605)
- Edward Hines Jr VA Hospital (Hines, Illinois) (578)
- North Florida/South Georgia Veterans Health System (Gainesville, Florida) (573)

Upon national release, all VAMCs are expected to install this patch prior to or on the compliance date. The software will be distributed as a host file that can be downloaded from the VA Software Download Directory.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No site-specific preparations are needed for this patch (Table 2). The VA sites should follow the standard procedure they are using now for installation of VistA patches.

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            | N/A                       | N/A                                         | N/A               | N/A       |

<span id="_Ref503893066" class="anchor"></span>Table 3: Facility Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no additional resources required for installation of this patch.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific features required for deployment of this patch (Table 3).

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |

<span id="_Ref503893297" class="anchor"></span>Table 4: Hardware Specifications

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special requirements regarding new or existing hardware capability. Existing hardware resources will not be impacted by the changes in this project.

Table 4 describes hardware specifications required at each site prior to deployment.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| Existing VistA system | N/A       | N/A         | N/A               | N/A              | N/A       |

<span id="_Ref503893363" class="anchor"></span>Table 5: Software Specifications

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 5 describes the software specifications required at each site prior to deployment.

| Required Software                                            | Make | Version                 | Configuration | Manufacturer | Other |
|------------------------------------------------------------------|----------|-----------------------------|-------------------|------------------|-----------|
| Fully patched ORDER ENTRY/RESULTS REPORTING package within VistA | N/A      | 3.0                         | N/A               | N/A              | N/A       |
| DG\*5.3\*1035                                                    | N/A      | Nationally released version | N/A               | N/A              | N/A       |

<span id="_Ref503893603" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

Please see Table 1: DIBRG Roles and Responsibilities for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites that are participating in field testing IOC will use the "Patch Tracking" message in Outlook to communicate with the SHRPE team, the developers, and product support personnel.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch OR\*3.0\*546, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in FORUM. FORUM automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in FORUM to identify when the patch was installed in the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch in their VistA production system. Therefore, this information does not need to be manually tracked in Table 6.

| Activity | Day | Time | Individual who completed task |
|--------------|---------|----------|-----------------------------------|
| Deploy       | N/A     | N/A      | N/A                               |
| Install      | N/A     | N/A      | N/A                               |
| Back-Out     | N/A     | N/A      | N/A                               |

<span id="_Toc47089566" class="anchor"></span>Table : Acronyms List

## Pre-Installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3.0\*546, a patch to the existing VistA ORDER ENTRY/RESULTS REPORTING 3.0 package, is installable on a fully patched MUMPS VistA system and operates on top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities that communicate with the underlying operating system and hardware, thereby providing ORDER ENTRY/RESULTS REPORTING independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3.0\*546 (Order Entry/Results Reporting/CPRS) is bundled with DG\*5.3\*1035 (Registration) and IB\*2.0\*697 (Integrated Billing) in the host file IB_2_0_P697.KID.

Refer to the IB\*2.0\*697 Patch Description on the NPM in FORUM for the detailed installation instructions. These instructions would include any pre-installation steps, if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the OR\*3.0\*546 documentation on the NPM to find related documentation that can be downloaded.

> **NOTE:** OR\*3.0\*546 (Order Entry/Results Reporting/CPRS) is bundled with DG\*5.3\*1035 (Registration) and IB\*2.0\*697 (Integrated Billing) in the host file IB_2_0_P697.KID.

The combined build for IB\*2.0\*697, DG\*5.3\*1035 and OR\*3.0\*546 will be distributed as a host file IB_2_0_P697.KID and can be downloaded from the VA Software Download Directory.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch is applied to an existing MUMPS VistA database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the IB\*2.0\*697 Patch Description in the NPM for installation instructions.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for the OR\*3.0\*546 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the National VA Network, as well as the local network of each site to receive DG patches, is required to perform the installation as well as authority to install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, the user verifies installation results by using the "Install File Print" menu option in the "Utilities" submenu of the KIDS.

Also refer to the OR\*3.0\*546 documentation on the NPM for detailed installation instructions. These instructions include any post-installation steps, if applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required for this patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocations, or other resources is necessary.

### Mirror Testing or Site Production Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If during Mirror testing or Site Production Testing, a new version of a defect correcting test patch is produced, retested, and successfully passes development team testing, it will be resubmitted to the site for testing. If the patch produces catastrophic problems, a new version of the patch can be used to restore the build components to their pre-patch condition.

### After National Release but During Designated Support Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to back out a specific release needs to be made in a timely manner. Catastrophic failures are usually known early in the testing process—within the first two or three days. Sites are encouraged to perform all test scripts to ensure new code is functioning in their environment, with their data. A back-out should only be considered for critical issues or errors. The normal or an expedited, issue-focused patch process can correct other bugs.

The general strategy for SHRPE VistA functionality rollback will likely be to repair the code with another follow-on patch.

If any issues with SHRPE VistA software are discovered after it is nationally released and within the 90-day warranty period window, the SHRPE development team will research the issue and provide guidance for any immediate, possible workaround. After discussing the defect with the VA and receiving their approval for the proposed resolution, the SHRPE development team will communicate guidance for the long-term solution.

The long-term solution will likely be the installation of a follow-up patch to correct the defect, a follow-up patch to remove the SHRPE updates, or a detailed set of instructions on how the software can be safely backed out of the production system.

### After National Release and Warranty Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the support period, the VistA Maintenance Program would produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if a wholesale back-out of the patch OR\*3.0\*546 is needed or if a better course of action is needed to correct through a new version of the patch (if prior to national release) or a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale back-out of the patch will still require a new version (if prior to national release) or a subsequent patch (after national release). If the back-out is post-release of patch OR\*3.0\*546, this patch should be assigned the status of "Entered in Error" in Forum's NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch OR\*3.0\*546.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The results will be provided upon the completion of the UAT.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

### From: OR*3*437 CPRS Deployment, Installation, Back-Out, and Rollback Guide

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA ORDER ENTRY/RESULTS REPORTING patch OR\*3.0\*437 should be installed in all VA VistA production sites.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The test sites for IOC testing are:

> VA Providence Healthcare System (HCS) (650)

> Hershel Woody Williams VAMC (VAMC) (581)

> Lexington VAMC-MHS (VAMC) (596)

Upon national release, all VAMCs are expected to install this patch prior to or on the compliance date. The software will be distributed as a host file that can be downloaded from the VA Software Documentation Library site.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No site-specific preparations are needed for this patch (Table 2). The VA sites should follow the standard procedure they are using now for installation of VistA patches.

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            | N/A                       | N/A                                         | N/A               | N/A       |

<span id="_Ref503893066" class="anchor"></span>Table 3: Facility Specific Features

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific features required for deployment of this patch (Table 3).

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |

<span id="_Ref503893297" class="anchor"></span>Table 4: Hardware Specifications

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special requirements regarding new or existing hardware capability. Existing hardware resources will not be impacted by the changes in this project.

Table 4 describes hardware specifications required at each site prior to deployment.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| Existing VistA system | N/A       | N/A         | N/A               | N/A              | N/A       |

<span id="_Ref503893363" class="anchor"></span>Table 5: Software Specifications

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 5 describes the software specifications required at each site prior to deployment.

| Required Software                                            | Make | Version                 | Configuration | Manufacturer | Other |
|------------------------------------------------------------------|----------|-----------------------------|-------------------|------------------|-----------|
| Fully patched ORDER ENTRY/RESULTS REPORTING package within VistA | N/A      | 3.0                         | N/A               | N/A              | N/A       |
| OR\*3.0\*377                                                     | N/A      | Nationally released version | N/A               | N/A              | N/A       |

<span id="_Ref503893603" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

Please see Table 1: DIBRG Roles and Responsibilities for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites that are participating in field testing IOC will use the "Patch Tracking" message in Outlook to communicate with the SHRPE team, the developers, and product support personnel.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch OR\*3.0\*437, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in FORUM. FORUM automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in FORUM to identify when the patch was installed in the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch in their VistA production system. Therefore, this information does not need to be manually tracked in Table 6.

| Activity | Day | Time | Individual who completed task |
|--------------|---------|----------|-----------------------------------|
| Deploy       | N/A     | N/A      | N/A                               |
| Install      | N/A     | N/A      | N/A                               |
| Back-Out     | N/A     | N/A      | N/A                               |

<span id="_Toc47089566" class="anchor"></span>Table : Acronyms List

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch OR\*3.0\*437.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The results will be provided upon the completion of the UAT.
