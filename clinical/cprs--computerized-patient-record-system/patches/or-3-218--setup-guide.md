---
title: OR*3*218 DEA e-Prescribing Setup Installation and Configuration Guide CPRS GUI
doc_type: CFG
doc_label: Configuration Guide
doc_layer: patch
doc_subject: DEA e-Prescribing Setup Installation and  CPRS GUI
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*218
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 1
description: The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order la
audience: 
keywords: 
  - cprs
  - install
  - table
  - contents
  - installation
  - server
  - setup
  - windows
  - verify
  - controlled
page_count: 0
word_count: 6306
section_count: 15
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: May 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_218_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_30_218_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

DEA e-Prescribing Setup Installation and Configuration Guide (for Patches OR\*3.0\*218, PSD\*3.0\*76, and XU\*8.0\*580)

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/001.png)

May 2013

Office of Information & Technology (OI&T)

Product Development (PD)

This page left blank intentionally

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
- [Overview](#overview)
  - [Recommended Audience](#recommended-audience)
  - [About this Guide](#about-this-guide)
  - [National Deployment](#national-deployment)
  - [Document Conventions](#document-conventions)
- [CPRS v29 DEA Set Up Preparatory Checklist](#cprs-v29-dea-set-up-preparatory-checklist)
- [Preparatory Patch Installation](#preparatory-patch-installation)
  - [Pre-requisite Patches](#pre-requisite-patches)
  - [Identify Appropriate Staff for Installation](#identify-appropriate-staff-for-installation)
  - [Download CPRS29DEASETUP.KID and CPRS29DEAKERNEL.ZIP from the ftp site](#download-cprs29deasetupkid-and-cprs29deakernelzip-from-the-ftp-site)
- [Install Bundle CPRS29DEASETUP.KID](#install-bundle-cprs29deasetupkid)
- [Install Software onto Windows Servers](#install-software-onto-windows-servers)
  - [Install the Patch on the Windows Server to Avoid Certificate Issues](#install-the-patch-on-the-windows-server-to-avoid-certificate-issues)
  - [Verify/Install Tumbleweed on the Server(s) running the PKI Verify Service](#verifyinstall-tumbleweed-on-the-servers-running-the-pki-verify-service)
- [Set Up a Job to Periodically Restart the PKI Verify Service (temporary mitigation strategy)](#set-up-a-job-to-periodically-restart-the-pki-verify-service-temporary-mitigation-strategy)
- [Setup PKI Server Parameter](#setup-pki-server-parameter)
- [Distribute ePCSDataEntryforPrescriber.exe](#distribute-epcsdataentryforprescriberexe)
- [Setup providers](#setup-providers)
  - [ePrescribing Controlled Substances Overview](#eprescribing-controlled-substances-overview)
  - [A New Application to Enter DEA Information](#a-new-application-to-enter-dea-information)
  - [Logging In to the Data Entry for ePrescribing Controlled Substances Application](#logging-in-to-the-data-entry-for-eprescribing-controlled-substances-application)
  - [Selecting a Prescriber to Edit](#selecting-a-prescriber-to-edit)
  - [Entering or Editing a Prescriber’s ePCS Information](#entering-or-editing-a-prescribers-epcs-information)
- [Enable a provider for ePCS](#enable-a-provider-for-epcs)
- [Set up the Kernel Report device](#set-up-the-kernel-report-device)
- [Schedule Kernel audit reports](#schedule-kernel-audit-reports)
- [Allocate PSDRPH Key](#allocate-psdrph-key)
- [Appendix A: Sample Installation](#appendix-a-sample-installation)

# Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Computerized Patient Record System (CPRS) Graphical User Interface (GUI) is a Veterans Health Information Systems and Technology Architecture (VistA) computer application. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

The purpose of this guide is to help sites prepare for installation of CPRS v.29 and its associated patches. Changes in CPRS v.29 are significant in that they affect the ability of providers to order medications, specifically outpatient controlled substances. New DEA regulations affect the ability to electronically prescribe controlled substances, even though they are only “transmitted” to the Outpatient Pharmacy at the VA Medical Center. The regulations require each provider to be individually set up with specific information, such as the number that gives them the authority to prescribe controlled substances (DEA or VA number, and, if necessary, Detox/Maintenance number, including an expiration date), a subject alternative name , and any schedules for which they can or cannot prescribe. In addition, there must be a second “granting” mechanism, controlled by an office different from the office assigning the DEA number and schedules. This set up should be done PRIOR to the CPRS v.29 installation into your production account.

In addition, DEA ePrescribing requires that Public Key Infrastucture (PKI) be used to maintain the security of controlled substances orders. To do this, several components must be installed or configured:

- PKISERVER.EXE, which runs as a service on a Windows Server (this helps verify the order information when it was placed is the same as it is when the pharmacy finishes the prescription)
- PKIVerifyServerSetup.EXE, which installs the PKISERVER.EXE as a service on the Windows Server.
- ePCSDataEntryforPrescriber.exe, which enables users to enter the credential information for the prescriber (the appropriate number and expiration date) and the schedules that the prescriber has authority to write controlled substance orders for.
- OE/RR EPCS PARAMETERS file (#100.7), which provides the second granting authority for controlled substance prescriptions. This is referred to as a logical access control.

  \*\*\*\*\* Important Note \*\*\*\*\*

  If you would like to receive a copy of the PIV Card Expiration Report, you must request it from the Homeland Security Presidential Directive (HSPD) Program Office. You should send the request to <HSPD12PMO@va.gov> and it MUST include your site station number.

  The report contains three key worksheets:
- <u>Expiring Cards</u>: Main sheet used to select Month and Year for the expired cards report, and shows graphical and daily counts for the selected month and year.
- <u>Expired Card Table</u>: Lists the card holders whose card expiration dates match the Month and Year selected from the “Expiring Cards” sheet.
- <u>PIV Cardholder Data</u>: Raw data of all facility card holders (as of 04/11/13) used for expiring cards reports. Sorted by Department, Last Name and First Name.

## Recommended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides information specifically for Department of Veterans Affairs Medical Center (VAMC) Information Resource Management (IRM) staff, Clinical Application Coordinators (CACs), and Windows Server administrators who will install and configure the DEA components that will allow prescribers to write outpatient controlled substance medication orders.

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This installation guide provides instructions for:

- Installing application components that run on M servers at VAMC facilities
- Installing Windows executable programs on workstations or application servers at VAMC facilities
- Performing post-installation tasks—including configuration tasks—that require knowledge of the underlying VistA system.

## National Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v29 will follow a phased deployment. To see current status and target dates, please refer to the following document:

[REDACTED](file:///\\v17.MED.VA.GOV\V17\ISD\Users\VHAISDMOODYS\Public\CPRS%20GUI%20v29%20Deployment%20Schedule)

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Examples of VistA “Roll and Scroll” interface actions will be shown in a box such as this:

Select OPTION NAME: XPAR EDIT PARAMETER Edit Parameter Values

Edit Parameter Values

# CPRS v29 DEA Set Up Preparatory Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following activities should be completed in order. These preparatory steps are to allow time for proper setup of providers prior to the installation of CPRS GUI v29.

Table 1 CPRS v29 Preparatory Checklist

<table style="width:100%;">
<colgroup>
<col style="width: 7%" />
<col style="width: 81%" />
<col style="width: 11%" />
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
<td></td>
<td>Read this checklist</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><p>Check that all pre-requisite patches are installed</p>
<p>• XU*8.0*373</p>
<p>• OR*3.0*280</p></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Identify the following people to assist/coordinate the installation and setup:</p>
<ul>
<li><p>Person responsible for OR, XU and PSD patches – only one can install the bundle, but all will need to ensure coordination</p></li>
<li><p>Windows Server administrator – this person will need to install the PKI Verify Server software on a Windows Server(s) and install either a patch or a cleanup script for certificates to function correctly, and must ensure that the Tumbleweed software is appropriately installed</p></li>
<li><p>Person with privileges to update the KERNEL SYSTEMS PARAMETERS file</p></li>
<li><p>Person with privileges to push out the new ePCSDataEntryfor Prescriber.exe to either the individual workstations or the shared folder</p></li>
<li><p>Person(s) responsible for DEA privilege configuration. The DEA regulations require at least two offices are involved. One to assign credentials such as DEA #, one to enable them for ePCS (menu option OR EPCS MENU)</p></li>
<li><p>Person to provide a list of pharmacists allowed to complete controlled substance orders</p></li>
<li><p>Person with privileges to allocate PSDRPH key</p></li>
<li><p>Person who can schedule two Kernel options in TaskMan</p></li>
<li><p>Person who can edit general parameters such as the new parameter XU EPCS REPORT DEVICE</p></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Download CPRS29_DEA_SETUP.KID and CPRS29_DEA_KERNEL.ZIP from the ftp site.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Install Bundle CPRS29_DEA_SETUP.KID</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Unzip the CPRS29_DEA_KERNEL.ZIP file.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Verify/install Tumbleweed on the server(s) that will run the PKI_Verify_Service.</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Place PKIVerifyServerSetup.exe on at least one but no more than three Windows servers. Use PKIVerifyServerSetup to install and start PKI_Verify_Service as a Windows Service.</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Set up Windows job to periodically restart PKI Verify Service.</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Add IP Addresses for 1 to 3 machines, running PKI_Verify_Server, to the PKI Server (#53.1) field in the Kernel System Parameters (#8989.3) file</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Distribute or install the ePCSDataEntryForPresciber.exe application on the workstations of those users holding the XUEPCSEDIT security key to set up providers for ordering of outpatient controlled substance prescriptions.</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Set up users of the ePCSDataEntryforPrescriber tool</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><p>Set up providers for DEA e-Prescribing using:</p>
<p>• ePCSDataEntryforPrescriber</p>
<p>• OR EPCS MENU (done for existing providers in OR*3.0*218 post-install)</p></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><p>Schedule the two Kernel audit reports in TaskMan</p>
<ul>
<li><p>XU EPCS Logical Access</p></li>
<li><p>XU EPCS PSDRPH Audit</p></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Set up the parameter for the Report Device for the Kernel reports.</td>
<td></td>
</tr>
</tbody>
</table>

# Preparatory Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-requisite Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must verify that the following required patches are properly installed on your system *before* continuing:

- OR\*3.0\*280
- XU\*8.3\*373

## Identify Appropriate Staff for Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- OR Patch Installation Person: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- PSD Patch installation Person:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- XU Patch Installation Person: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Windows Server Administrator: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- KERNEL PARAMETERS: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Distribute workstation executable: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- DEA Credential Setup (ePCSDataEntryforPrescriber GUI): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Access to \[EPCS USER ENABLE/DISABLE\] menu option:

  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Provide list of pharmacists allowed to complete controlled substance prescriptions:

  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Privileges to allocate PSDRPH key: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Person who can schedule Kernel tasks in TaskMan:

  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
- Person to edit the parameters file – XU EPCS REPORT DEVICE

  \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## Download CPRS29_DEA_SETUP.KID and CPRS29_DEA_KERNEL.ZIP from the ftp site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The preferred method is to FTP the files from [<span class="mark">REDACTED</span>](ftp://download.vista.med.va.gov/). This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

[<span class="mark">REDACTED</span>](ftp://download.vista.med.va.gov/)

The necessary files are CPRS29_DEA_SETUP.KID, which is an ASCII file, and CPRS29_DEA_KERNEL.ZIP, which is a binary file.

Table 2 Bundle CPRS29_DEA_SETUP.KID

| CPRS29_DEA_SETUP.KID | SUPPORTED FUNCTIONALITY                                                                           |
|----------------------|---------------------------------------------------------------------------------------------------|
| OR\*3.0\*218         | Create and update fields for turning on/off ePCS functionality for the site and individual users. |
| XU\*8.0\*580         | ePCS Kernel support – such as DEA and Detox number validation and user setup.                     |
| PSD\*3.0\*76         | Exports the new PSDRPH key. Required for pharmacists to complete controlled substance orders.     |

Table 3 CPRS29_DEA_KERNEL.ZIP

| Component                      | Functionality                                                                                                        |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ePCSDataEntryforPrescriber.exe | ePrescribing Setup for Providers                                                                                     |
| PKIVERIFYSERVERSETUP.EXE       | Installs and starts the PKI_VERIFY_SERVICE – used by Pharmacy when completing Outpatient Controlled Substance Orders |
| PKIServer.exe                  | PKI Verify service                                                                                                   |

# Install Bundle CPRS29_DEA_SETUP.KID

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This host file may be installed at any time. Listed below are general installation instructions for installing the patches and executables. A sample installation capture is provided below. Additionally, review the National Patch Module messages for each patch for patch-specific information.

The install should take less than 10 minutes.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
2.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File: “, respond with CPRS29_DEA_SETUP.KID
3.  If given the option to run any Environment Check Routine(s), answer "YES."
4.  From this menu, you may then elect to use the following options:
5.  Backup a Transport Global
6.  Compare Transport Global to Current System
7.  Verify Checksums in Transport Global
8.  When ready, select the Install Packages option.
9.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//", respond "NO."
10. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond "NO."
11. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond NO.
12. When prompted 'Delay Install (Minutes): (0-60): 0//; respond '0.'

> **NOTE:** For an Example Install Capture, please see *Section 12: Appendix A*.

The post-installation routine for OR\*3.0\*218 will populate the new OE/RR EPCS PARAMETERS file by enabling providers who meet the following criteria:

1.  Hold the ORES key.
2.  Are authorized to write medication orders (the AUTHORIZED TO WRITE MED ORDERS field (#53.1), in the NEW PERSON file (#200), is set to YES and the INACTIVE DATE field (#53.4), in the NEW PERSON file (#200), is blank or contains a date in the future).
3.  Have a valid DEA or VA number.
4.  Are active (the DISUSER field (#7), in the NEW PERSON file (#200), is blank or set to NO and the TERMINATION DATE field (#9.2), in the NEW PERSON file (#200) is blank or contains a date in the future).

After installation of OR\*3.0\*218, when your site needs to enable or disable the parameter for a provider, use the ePCS User Enable/Disable option. Below is an example of enabling a provider:

CL Clinician Menu ...

NM Nurse Menu ...

WC Ward Clerk Menu ...

PE CPRS Configuration (Clin Coord) ...

IR CPRS Configuration (IRM) ...

Select CPRS Manager Menu Option: PE CPRS Configuration (Clin Coord)

AL Allocate OE/RR Security Keys

KK Check for Multiple Keys

DC Edit DC Reasons

GP GUI Parameters ...

GA GUI Access - Tabs, RPL

MI Miscellaneous Parameters

NO Notification Mgmt Menu ...

OC Order Checking Mgmt Menu ...

MM Order Menu Management ...

LI Patient List Mgmt Menu ...

FP Print Formats

PR Print/Report Parameters ...

RE Release/Cancel Delayed Orders

US Unsigned orders search

EX Set Unsigned Orders View on Exit

NA Search orders by Nature or Status

CM Care Management Menu ...

DO Event Delayed Orders Menu ...

LO Lapsed Orders search

PM Performance Monitor Report

Select CPRS Configuration (Clin Coord) Option: GP GUI Parameters

CS GUI Cover Sheet Display Parameters ...

HS GUI Health Summary Types

TM GUI Tool Menu Items

MP GUI Parameters - Miscellaneous

UC GUI Clear Size & Position Settings for User

RE GUI Report Parameters ...

NV GUI Non-VA Med Statements/Reasons

EX GUI Expired Orders Search Hours

RM GUI Remove Button Enabled

NON GUI Remove Button Enabled for Non-OR Alerts

DEA GUI e-PCS Enable/Disable

CLOZ GUI Edit Inpatient Clozapine Message

COAG GUI Anticoagulation Parameters ...

EIE GUI Mark Allergy Entered in Error

Select GUI Parameters \<TEST ACCOUNT\> Option: DEA GUI ePCS Management Menu

SITE ePCS Site Enable/Disable

USER ePCS User Enable/Disable

Duplicate VA Numbers Report

Select GUI ePCS Management Menu \<TEST ACCOUNT\> Option: USER ePCS User Enable/Di

sable

This option is used to enable or disable electronic prescribing of outpatient

controlled substances for individual users. Entering the user's name will

enable that user and deleting the user's name will disable that user.

CONFIGURING CAMP MASTER

Select ENABLED USER: CPRS,PROVIDER// CPRSPROVIDER,FORTYFOUR TR

PHYSICIAN

Are you adding 'CPRSPROVIDER,FORTYFOUR' as

a new ENABLED USERS (the 8TH for this OE/RR EPCS PARAMETERS)? No// Y (Yes)

# Install Software onto Windows Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PKI Verify Service is used during the Pharmacy process of completing controlled substance orders entered in CPRS. It is used to validate that the contents of the prescription have not been modified. Sites will need to install the PKI Verify Service on a minimum of one and maximum of three Windows servers.

Server Requirements for PKI Verify Service Installation:

- A person with Windows Server Administrator access must perform this part of the installation
- The Windows Server must have a static IP address (this will be entered in a Kernel parameter)
- The Windows Server must be accessible by the VistA server.
- There are hotfix patches necessary for the Windows2008 and Windows 2008 R2 servers. For Windows 2003, a script must be run.
- The Windows Server must have Tumbleweed installed and properly configured (see section 5.2 below)

## Install the Patch on the Windows Server to Avoid Certificate Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Determine what version of Windows Server is installed on each machine (Windows Server 2003 or older, Windows Server 2008, Windows Server 2008 R2).
2.  Use the following information to correctly update the server:

For Windows Server 2003 or older, run the following script: [REDACTED](file:///\\v17.MED.VA.GOV\V17\ISD\Users\VHAISDMOODYS\Public\CPRS%20GUI%20v29%20Deployment%20Schedule)

- For Windows Server 2008, verify if the patch found here is installed. If not, install on the server: <http://support.microsoft.com/kb/2639180>
- For Windows Server 2008 R2, verify if the patch found here is installed. If not, install on the server: <http://support.microsoft.com/kb/2615174>

## Verify/Install Tumbleweed on the Server(s) running the PKI Verify Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If you do not already have Tumbleweed installed, the documentation and installation software for servers are located on [REDACTED](http://vaww.pki.va.gov). On the left, you will see Certificate Validation (OCSP/CRL). Click on this link to go to the page for software and instructions.
2.  If you have Tumbleweed installed (or once you complete the installation), please verify that OCSP is the first Protocol used in the Validation Options.
3.  In order to check this, open the Tumbleweed application, go to the General Tab, in the center of the screen, you will see ‘Default Validation Options’, click on Settings.

    ![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/002.png)
4.  This brings up a window for Default Validation Options: OCSP should be listed first, CRLDP should be second.

    ![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/003.png)
5.  If this is NOT true, you need to move the OCSP protocol to position 1. If the Move Up button is greyed out for you, please contact the VA PKI Helpdesk for support: 800-877-4328. (As of 12/4/2012).

#### ## Install PKI Verify Service on One to Three Windows Servers

The following instructions will help you install the PKI Verify Service and run it on at least one, but as many as three Windows servers. This service is used during the Pharmacy finishing process to verify that the provider PKI certificate is still valid.

> **NOTE:** You will install the PKI Verify Service on the same servers you used in step 5.1 (you must have at least one, but can have up to three).

1.  Identify the person who will install the PKI Verify Service. (See requirements above). This is probably the same person who accomplished section 5.1 above.
2.  Open CPRS29_DEA_KERNEL.ZIP file by double-clicking it or selecting it and pressing \<Enter\>.
3.  Copy the PKIVERIFYSERVERSETUP.EXE to the Windows Server on which you want PKI Verify Service to run.
4.  Run PKIVERIFYSERVERSETUP.EXE by right-clicking on it and selecting Run as Administrator.

PKIVERIFYSERVERSETUP.EXE will install PKISERVER.EXE in the C:\Windows directory and start it as an automatic service. If the service has been previously installed, it will stop the service, remove the service, and then replace the earlier version of PKIServer.exe before setting up and starting the service again.

> **NOTE:** If you look at services on the Windows server, PKISERVER.EXE will appear as PKI_Verify_Service.

5.  Record the IP address of the Windows Server.

The Server IP addresses will be need in the next section to set up the PKI parameters.

6.  (Optional) Repeat steps 3 - 5 for up to two more servers.

Below is an example of the dialogs that the user installing PKIServer.exe will see:

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/004.png)

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/005.png)

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/006.png)

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/007.png)

At this time, another window will open that displays the command line items as they execute.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/008.png)

# Set Up a Job to Periodically Restart the PKI Verify Service (temporary mitigation strategy)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During testing, two sites experienced issues with the PKI Verify Service communication stopping after the initial communication from VistA was successful. In both cases, it was necessary to restart the service to clear the issue. Currently, this is believed to be an issue with communicating with the national revocation server.

It was determined that periodically restarting the PKI Verify Service is an appropriate, although temporary, mitigation strategy.

Set up a Windows job to restart the service periodically – preferably 3 times per week.

# Setup PKI Server Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Someone who can edit Kernel parameters needs to perform this step.

1.  In VistA, edit the Kernel System Parameters file (#8989.3) by using the following options:
1)  Systems Management Menu
2)  Operations Management
3)  Kernel Management Menu
4)  Enter/Edit Kernel Site Parameters
5)  Kernel PKI Parameter Edit
2.  Then choose either of the following:
- Enter/Edit Kernel Site Parameters
- Kernel PKI Parameter Edit
3.  Enter the IP addresses separated by commas for the servers where PKISERVER.EXE is installed. You must have at least one IP address because PKISERVER.EXE must be installed on at least one server. You can install it on up to two additional servers as well. These entries will be stored in the PKI Server field (#53.1).
4.  Save the changes.
5.  Exit the screen.

# Distribute ePCSDataEntryforPrescriber.exe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the CPRS29_DEA_KERNEL.ZIP file, you can distribute the ePCSDataEntryforPrescriber.exe. To help sites with the set up for DEA ePrescribing, the Kernel developers created this GUI application. It will enable users to enter the appropriate information for individual providers who write controlled substance medication orders.

Who needs this executable? The office or group of people who will be responsible for the set up of items related to the provider’s credentials regarding controlled substances prescribing—DEA number, VA number, Detox/Maintenance number, and schedules allowed.

To enter data in the ePCS Data Entry for Prescriber application, thporte user must have the XUEPCSEDIT key.

> **NOTE:** A user cannot have both the XUEPCSEDIT key and the ORES key. The two keys are exclusive to one another so that the person prescribing is not also the person controlling authorization for prescribing controlled substances.

Use the following steps to distribute:

1.  If it is not already open, locate and open the CPRS29_DEA_KERNEL.ZIP file by double-clicking it or highlighting it and pressing \<Enter\>.
2.  Distribute or install ePCSDataEntryforPresciber.exe following your normal processes.

# Setup providers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ePrescribing Controlled Substances Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Administration (VA) has made changes to implement the Drug Enforcement Agency (DEA) requirements for ordering controlled substances. The DEA now requires two-factor authentication and acknowledgement that the provider accepts what signing for a controlled substance means. This message displays in the Computerized Patient Record System (CPRS) signature dialogs when a provider signs controlled substances orders as outpatient prescriptions.

For controlled substance orders on an outpatient prescription, the process now includes two-factor authentication. When providers begin to sign an order for a controlled substance, they must first select which outpatient controlled substance orders they will sign. Then, the provider will enter their electronic signature, insert their Personal Identification Verification (PIV) card, and enter the Personal Identification Number (PIN) for the PIV card. The software then checks to ensure that the provider has a valid DEA number and PKI certificate. To check the certificate, the software requires specific information for each user.

## A New Application to Enter DEA Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enter the required information for ordering and signing controlled substance orders, VA developers created the new Data Entry for e-Prescribing Controlled Substances (ePCS) GUI application. The application enables users to select prescribers one at a time and enter the following information for the selected provider:

- Authorized to Write Medication Orders
- User’s Subject Alternative Name (which is, generally, their VA Outlook address, if they have one)
- DEA Number
- VA Number
- Detox/Maintenance Number
- DEA Expiration Date
- For which Drug Schedules the Provider may write orders

The dialog is shown below.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/009.png)

This is the Data Entry for e-Prescribing Controlled Substances dialog. Here it is shown after the user has connected to the account, but before selecting a prescriber whose information needs to be edited.

If a provider already has some of this information, it will display when the user selects the provider’s name. For example, if they are already authorized to write medication orders, the check box will be checked. If the user already has a DEA number, the DEA number will display and so forth.

## Logging In to the Data Entry for ePrescribing Controlled Substances Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To log in to the Data Entry for ePrescribing Controlled Substances GUI application, a user holding the XUEPCSEDIT key must first identify which system you want to make changes to by entering the server address and RPC/Broker port number. Then, they will authenticate to the application using their access and verify codes and PIV card.

1.  Launch the Data Entry for e-Prescribing Controlled Substances application.

    Note: If you have the server and port number defined in the executable’s shortcut (e.g., “C:\Program Files\Vista\ePCSDataEntryforPrescriber.exe” s=cprsnode3 p=9625), you can skip to step 4.
2.  (Conditional) Select the Get Server Info button.

This will only occur if you have access to multiple accounts, such as test and production. A dialog then displays with a list of possible accounts.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/010.png)

3.  Select the appropriate account (server and port).

The appropriate information is then displayed in the Server Address and Port fields.

4.  Select the Connect button.

The VISTA Sign-on screen displays.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/011.png)

Here is the login screen

5.  Enter your Access Code, press Tab or click in the Verify Code field, enter your Verify Code, and press \<Enter\> or click OK.
6.  (Conditional) If your PIV is not inserted, you will see the dialog box below. If necessary, insert your PIV card and select OK.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/012.png)

This dialog tells you that you need your smart card.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/013.png)

If you see this, insert your smart card and press OK.

7.  Enter your PIN and select OK.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/014.png)

Enter your PIN here.

8.  The rest of the fields in the dialog display and are filled in with any information already contained in VistA files for this user.

## Selecting a Prescriber to Edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After logging in, the user needs to select a prescriber.

To select a prescriber, use these steps:

1.  Select the Select Provider button by either tabbing to the button and pressing \<Enter\> or click on the button.
2.  In the Look Up Utility dialog, select Find.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/015.png)

The Look Up Utility dialog lists the providers in the system. Users can scroll through the list or use the find button to search for a name.

3.  In the Find… dialog, type part or all of the prescriber’s name and select OK.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/016.png)

4.  If a list displays with multiple possible names, locate the correct name, select it, and press \<Enter\> or click OK.

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/017.png)

If there is more than one possible matching name in the system, the Look Up Utility displays a list of possible matches.

After the prescriber’s name is selected, the dialog displays any information that is available in VistA, such as in the screen capture below:

![](or-3-218-dea-e-prescribing-setup-installation-and-configuration-guide-cprs-gui/018.png)

Once the user selects the prescriber to edit, the rest of the fields show information previously entered. The user can now edit this prescriber’s information.

## Entering or Editing a Prescriber’s ePCS Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most items on the left side of the dialog existed previous to the ePCS project and are included to simplify the process of getting the information into VistA:

- Authorized to Write Medication Orders
- DEA Number
- VA Number
- Detox/Maintenance Number
- DEA Expiration Date

If this information was previously entered into VistA, it will display in the appropriate fields.

New items in this dialog for ePCS include the following:

- Subject Alternative Name (SAN), which is, generally, their VA Outlook email address, if they have one.
- Fields to identify which DEA drug Schedules the prescriber is authorized to write orders for (the user can select a checkbox to assign all schedules or select checkboxes to designate only specific schedules individually). This will depend on the credentials of the provider.

Once the appropriate provider is selected, check to see if the necessary information has been input. Then, make the changes using the steps that follow. These instructions assume that no information has been entered.

> WARNING:Do NOT remove all check boxes unless you want to make it impossible for the user to order controlled substance medications. If any user has been assigned any DEA schedules (any of the boxes have been checked at all) and then all checks are removed and the Update button is selected, the next time the user tries to order a medication, their information—including their DEA number—will be erased from the system.

To enter ePCS data, use the following steps:

1.  If needed, designate the Prescriber as Authorized to Write Med Orders by checking the Authorized to Write Med Orders checkbox.
2.  If the user has a DEA number, move to the DEA \# field and type in the number.
3.  If the user has a VA number, move to the VA number field and type in the VA number.
4.  If the user has a Detox/Maint number, move the Detox/Maint number field and type in the number.
5.  If you entered a DEA number for the prescriber, move to the DEA Expiration Date field. (Note: No expiration date causes the DEA number to be treated as expired.) To enter a date, either type the date in field using the format mm/dd/yyyy (for example, 04/10/2015) or use the steps below to use the calendar control:
1)  Select the down arrow.
2)  Use the right and left arrows to move to the correct month and year.
3)  Click on the day that you need to enter.
6.  Select the checkboxes by the DEA schedules for which this prescriber will have permission to write medications. To select all schedules, place a check mark in the Select All Schedules checkbox. To limit the provider to specific schedules, place a check mark in the check box by clicking in it or tab to the appropriate field and pressing the \<Space Bar\>. Repeat as necessary for the various schedules.

> WARNING:Do NOT remove all check boxes unless you want to make it impossible for the user to order medications. If any user has been assigned any pharmacy schedules (any of the boxes have been checked at all) and then all checks are removed and the Update button is selected, the next time the user tries to order a medication, their information—including their DEA number—will be erased from the system.

7.  When you have completed all necessary fields, review your entries.
8.  When satisfied with all entries in the dialog, select the Update button.
9.  To continue on, select a different prescriber (see instructions above). To close the application, select the Exit button.

# Enable a provider for ePCS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another requirement of the DEA Interim Final Rule specifies that there be a “logical access control” for electronic prescribing of Controlled Substances. This is in addition to the provider having all the appropriate credentials and schedule information.

With CPRS v.29, this logical access control is implemented using a new file: OE/RR EPCS PARAMETERS (#100.7). This information is stored in a new file to enable auditing, another requirement of the DEA Interim Final Rule.

The post-install routine for OR\*3.0\*218 enables appropriate providers (as outlined in section 4 above). Should you need to edit a provider’s logical access control, you will need to use menu option \[EPCS USER ENABLE/DISABLE\].

\*\*\*Important Note\*\*\*

Per DEA Interim Final Rule, the users with access to the GUI application for defining credentials for providers can NOT be the same as the users with access to the logical access control menu option. Therefore, the menu option requires a new key: OREPCSUSERS and will not allow a holder of the XUEPCSEDIT key to use the option.

# Set up the Kernel Report device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DEA requirements specify that certain audit reports must be generated automatically. This requires the ability to define the device. This device is defined using a parameter. Please refer to the patch description for XU\*8.0\*580 for instructions on setting up the parameter.

# Schedule Kernel audit reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to meet the DEA requirements to automatically generate audit report, two Kernel reports must be scheduled in TaskMan. Please refer to the patch description for XU\*8.0\*580 for instructions on scheduling the two TaskMan audit reports.

# Allocate PSDRPH Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Every pharmacist who will need to be able to complete controlled substance orders entered in CPRS needs to hold the PSDRPH key. It is important to remember that this key should never be assigned to a pharmacy technician.  
CPRS v.29 Readiness Checklist

This checklist is to help sites prepare the resources and personnel they will need to install CPRS v.29. Because of the varied and complex nature of CPRS v.29’s projects, it will take some coordination among different groups to be ready to install. There are hardware tasks or checks, server installations, roles to be defined, and configuration that must occur before the CPRS v.29 installation so that the system, workstations, and providers will be ready to use to its fullest extent.

| Completed | Item                                                                                                                                             | Department                    |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
|               | Every workstation used for CPRS prescribing of controlled substances has a functioning smart card reader                                             | IT                                |
|               | Every workstation used for CPRS prescribing of controlled substances has Tumbleweed Desktop Validator installed and OCSP is the \#1 search protocol. | IT                                |
|               | PIN Resetters have been assigned and trained at remote locations and off-hours tours of duty.                                                        | PIV Coordinator                   |
|               | Contingency process for any downtime of electronic prescribing including supplies, if needed.                                                        | Pharmacy                          |
|               | PIV cards for all outpatient controlled substance providers.                                                                                         | PIV Coordinator                   |
|               | Contingency plan for PIV card failures.                                                                                                              | Chief Medical Informatics Officer |
|               | Identify super users and confirm available for ePCS Implementation                                                                                   | Pharmacy                          |
|               | Address change processes reviewed and modified, if necessary.                                                                                        | Varies from site to site          |
|               | Setup build installed.                                                                                                                               |                                   |
|               | Windows servers - hotfix installed or script run                                                                                                     | IT                                |
|               | Tumbleweed installed on PKI Verify Service Windows Servers                                                                                           | IT                                |
|               | PKI Verify Service installed on 1-3 servers.                                                                                                         | IT                                |
|               | Setup job to periodically restart PKI Verify Service                                                                                                 | IT                                |
|               | Setup PKI Server parameter in Kernel System Parameters                                                                                               | IRM                               |
|               | Distribute ePCSDataEntryforPrescriber.exe                                                                                                            | IRM                               |
|               | Provider setup complete.                                                                                                                             | Multiple departments              |
|               | Kernel Report device defined.                                                                                                                        | IRM                               |
|               | Kernel audit reports scheduled in TaskMan                                                                                                            | Depends on site                   |

# Appendix A: Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: INstallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: LOAD a Distribution

Enter a Host File: VA5\$:\[CPRS\]CPRS29_DEA_SETUP.KID

KIDS Distribution saved on Apr 02, 2013@11:40:08

Comment: DEA SETUP BUILD

This Distribution contains Transport Globals for the following Package(s):

CPRS29 DEA 1.0

XU\*8.0\*580

OR\*3.0\*218

PSD\*3.0\*76

Want to Continue with Load? YES// \<Enter\>

Loading Distribution...

CPRS29 DEA 1.0

Build XU\*8.0\*580 has an Environmental Check Routine

Want to RUN the Environment Check Routine? YES//

XU\*8.0\*580

Will first run the Environment Check Routine, XU8P580

Perform Environment Check...

Finished Environment Check.

OR\*3.0\*218

PSD\*3.0\*76

Use INSTALL NAME: CPRS29 DEA 1.0 to install this Distribution.

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: CPRS29 DEA 1.0 4/25/13@13:09:56

=\> DEA SETUP BUILD ;Created on Apr 02, 2013@11:40:08

This Distribution was loaded on Apr 25, 2013@13:09:56 with header of

DEA SETUP BUILD ;Created on Apr 02, 2013@11:40:08

It consisted of the following Install(s):

CPRS29 DEA 1.0 XU\*8.0\*580 OR\*3.0\*218 PSD\*3.0\*76

Checking Install for Package CPRS29 DEA 1.0

Install Questions for CPRS29 DEA 1.0

Checking Install for Package XU\*8.0\*580

Will first run the Environment Check Routine, XU8P580

Perform Environment Check...

\*\* Although Queuing is allowed - it is HIGHLY recommended that ALL Users and

VISTA Background jobs be STOPPED before installation of this patch. Failure

to do so may result in 'source routine edited' error(s). Edits will be

lost and record(s) may be left in an inconsistent state, for example,

not all Cross-Referencing completed; which in turn may cause FUTURE

VistA/FileMan Hard Errors or corrupted Data. \*\*

\* Warning TaskMan Has NOT Been Stopped or Placed in a WAIT State!

\* Warning Logons are NOT Inhibited!

Finished Environment Check.

Install Questions for XU\*8.0\*580

Incoming Files:

4 INSTITUTION (Partial Definition)

> **NOTE:** You already have the 'INSTITUTION' File.

19 OPTION (Partial Definition)

> **NOTE:** You already have the 'OPTION' File.

200 NEW PERSON (Partial Definition)

> **NOTE:** You already have the 'NEW PERSON' File.

8991.6 XUEPCS DATA

8991.7 XUEPCS PSDRPH AUDIT

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package OR\*3.0\*218

Install Questions for OR\*3.0\*218

Incoming Files:

100.7 OE/RR EPCS PARAMETERS

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package PSD\*3.0\*76

Install Questions for PSD\*3.0\*76

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

--------------------------------------------------------------------------------

Install Started for CPRS29 DEA 1.0 :

Apr 25, 2013@13:13:23

Build Distribution Date: Apr 02, 2013

Installing Routines:

Apr 25, 2013@13:13:23

Install Started for XU\*8.0\*580 :

Apr 25, 2013@13:13:23

Build Distribution Date: Mar 28, 2013

Installing Routines:

Apr 25, 2013@13:13:23

Running Pre-Install Routine: PRE^XU8P580

Beginning Pre-Installation...

I am deleting the cross-reference "SAN" for field \#501.2 file \#200.

Finished Pre-Installation.

Installing Data Dictionaries: ..

Apr 25, 2013@13:13:23

Installing PACKAGE COMPONENTS:

Installing BULLETIN

Installing SECURITY KEY

Installing PRINT TEMPLATE

Installing SORT TEMPLATE

Installing REMOTE PROCEDURE

Installing OPTION

Installing PARAMETER DEFINITION

Apr 25, 2013@13:13:23

Running Post-Install Routine: POST^XU8P580

Beginning Post-Installation...

I am deleting the OBJECT (#9.201) multiple from the HELP FRAME (#9.2) file.

I am re-indexing "ASAN" cross-reference for field \#501.2 file \#200. ..........

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

................................................................................

Finished Post-Installation.

Updating Routine file...

Updating KIDS files...

XU\*8.0\*580 Installed.

Apr 25, 2013@13:13:32

Install Message sent \# 12311

Install Started for OR\*3.0\*218 :

Apr 25, 2013@13:13:32

Build Distribution Date: Apr 02, 2013

Installing Routines:

Apr 25, 2013@13:13:32

Running Pre-Install Routine: PRE^ORY218

DONE

Installing Data Dictionaries:

Apr 25, 2013@13:13:36

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Installing OPTION

Apr 25, 2013@13:13:36

Running Post-Install Routine: POST^ORY218

Cleaning up menus...

DONE

Configuring site CHEYENNE VAMC for ePCS...

DONE

Updating Routine file...

Updating KIDS files...

OR\*3.0\*218 Installed.

Apr 25, 2013@13:13:36

Install Message sent \# 123911

Install Started for PSD\*3.0\*76 :

Apr 25, 2013@13:13:36

Build Distribution Date: Mar 25, 2013

Installing Routines:

Apr 25, 2013@13:13:36

Installing PACKAGE COMPONENTS:

Installing SECURITY KEY

Apr 25, 2013@13:13:36

Updating Routine file...

Updating KIDS files...

PSD\*3.0\*76 Installed.

Apr 25, 2013@13:13:36

Install Message sent \# 123111

Updating Routine file...

Updating KIDS files...

CPRS29 DEA 1.0 Installed.

Apr 25, 2013@13:13:36

Install Message sent \# 1231211

Install Completed