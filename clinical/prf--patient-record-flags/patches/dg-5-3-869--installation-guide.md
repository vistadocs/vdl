---
title: DG*5.3*869/TIU*1*279 Missing Patient PRF Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: PRF
app_name: Patient Record Flags
section: CLI
app_status: active
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*869
group_key: "PRF:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - install
  - installation
  - missing
  - patient
  - flag
  - created
  - record
  - want
page_count: 0
word_count: 3155
section_count: 13
table_count: 11
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: February 2014
revision_count: 6
revision_newest: 2/4/2014
revision_oldest: 8/30/2013
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/missing_patient_prf_installation_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/missing_patient_prf_installation_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=156"
---

Missing Patient

Patient Record Flag (PRF)

Installation Guide

Patches

DG\*5.3\*869

TIU\*1.0\*279

![](dg-5-3-869-tiu-1-279-missing-patient-prf-installation-guide/001.png)

February 2014

Revision History

|            |         |                                                                                                                                                                                                                                                      |                                    |
|------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Date       | Version | Description                                                                                                                                                                                                                                          | Author                             |
| 2/4/2014   | 0.5     | Added instructions for verification of DGPF MISSING PT FLAG REVIEW Mail Group. (Installation section, page 7).                                                                                                                                       | <span class="mark">REDACTED</span> |
| 11/12/2013 | 0.4     | Removed some information from Pre-Installation section page 3. Added note title, “Patient Record Flag Category I – Missing Patient” to Post Installation Instructions, page 6. Added “IMPORTANT” to note for Pre/Post Installation Overview, page 3. | <span class="mark">REDACTED</span> |
| 11/4/2013  | 0.3     | Updated to include comments from SQA and Todd Jackson.                                                                                                                                                                                               | <span class="mark">REDACTED</span> |
| 9/17/2013  | 0.2     | Update Routine Information                                                                                                                                                                                                                           | <span class="mark">REDACTED</span> |
| 9/12/2013  | 0.2     | Added DGPF ASSIGNMENT security key note to Introduction.                                                                                                                                                                                             | <span class="mark">REDACTED</span> |
| 8/30/2013  | 0.1     | Updated document with installation steps and information for patches DG\*5.3\*869 and TIU\*1.0\*279.                                                                                                                                                 | <span class="mark">REDACTED</span> |
# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Related Documentation](#related-documentation)
  - [Related Web Sites](#related-web-sites)
- [Pre-Installation](#pre-installation)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Pre-Requisite Software for TIU\1.0\279](#pre-requisite-software-for-tiu10279)
  - [## Pre-Requisite Software for DG\5.3\869](#pre-requisite-software-for-dg53869)
  - [## # Installation](#installation)
  - [Installation Steps (TIU\1\279):](#installation-steps-tiu1279)
- [## Post-Installation Instructions (TIU\1.0\279):](#post-installation-instructions-tiu10279)
  - [Verify Creation of DGPF MISSING PT FLAG REVIEW Mail Group](#verify-creation-of-dgpf-missing-pt-flag-review-mail-group)
  - [## Installation Steps (DG\5.3\869):](#installation-steps-dg53869)
  - [Post-Installation Instructions – (DG\5.3\869):](#post-installation-instructions-dg53869)
  - [Routine Information:](#routine-information)
  - [## Back-Out Plan for Production Environment](#back-out-plan-for-production-environment)
- [Appendix A: Installation Examples](#appendix-a-installation-examples)
- [# Installation Example - (TIU\1.0\279)](#installation-example-tiu10279)
- [# Select Installation Option: 6  Install Package(s)Select INSTALL NAME: TIU\1.0\279       Loaded from Distribution  12/4/13@10:43:01     =\> TIU\1\279  ;Created on Sep 10, 2013@13:22:53This Distribution was loaded on Dec 04, 2013@10:43:01 with header ofTIU\1\279  ;Created on Sep 10, 2013@13:22:53  It consisted of the following Install(s):   TIU\1.0\279Checking Install for Package TIU\1.0\279Install Questions for TIU\1.0\279Want KIDS to INHIBIT LOGONs during the install? NO//Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//Enter the Device you want to print the Install messages.You can queue the install by enter a 'Q' at the device prompt.Enter a '^' to abort the install.DEVICE: HOME//   DEC Windows--------------------------------------------------------------------------------Install Started for TIU\1.0\279 :               Dec 04, 2013@10:45Build Distribution Date: Sep 10, 2013Installing Routines:              Dec 04, 2013@10:45Running Post-Install Routine: MAIN^TIUPS279Title Created: PATIENT RECORD FLAG CATEGORY I - MISSING PATIENTTitle attached to Document Class PATIENT RECORD FLAG CAT IUpdating Routine file...Updating KIDS files...TIU\1.0\279 Installed.              Dec 04, 2013@10:45Install Completed](#select-installation-option-6-install-packagesselect-install-name-tiu10279-loaded-from-distribution-12413104301-tiu1279-created-on-sep-10-2013132253this-distribution-was-loaded-on-dec-04-2013104301-with-header-oftiu1279-created-on-sep-10-2013132253-it-consisted-of-the-following-installs-tiu10279checking-install-for-package-tiu10279install-questions-for-tiu10279want-kids-to-inhibit-logons-during-the-install-nowant-to-disable-scheduled-options-menu-options-and-protocols-noenter-the-device-you-want-to-print-the-install-messagesyou-can-queue-the-install-by-enter-a-q-at-the-device-promptenter-a-to-abort-the-installdevice-home-dec-windows-install-started-for-tiu10279-dec-04-20131045build-distribution-date-sep-10-2013installing-routines-dec-04-20131045running-post-install-routine-maintiups279title-created-patient-record-flag-category-i-missing-patienttitle-attached-to-document-class-patient-record-flag-cat-iupdating-routine-fileupdating-kids-filestiu10279-installed-dec-04-20131045install-completed)
- [# First-Time Install - DG\5.3\869](#first-time-install-dg53869)
- [The following is an example of the install for DG\5.3\869:](#the-following-is-an-example-of-the-install-for-dg53869)
- [# Select Installation Option: Install Package(s)](#select-installation-option-install-packages)
- [Select INSTALL NAME: DG\5.3\869 Loaded from Distribution](#select-install-name-dg53869-loaded-from-distribution)
- [4/25/13@13:57:02](#42513135702)
- [=\> DG\5.3\869 - KID ;Created on Apr 25, 2013@13:06:58](#dg53869-kid-created-on-apr-25-2013130658)
- [# This Distribution was loaded on Apr 25, 2013@13:57:02 with header of](#this-distribution-was-loaded-on-apr-25-2013135702-with-header-of)
- [DG\5.3\869 - KID ;Created on Apr 25, 2013@13:06:58](#dg53869-kid-created-on-apr-25-2013130658-1)
- [It consisted of the following Install(s):](#it-consisted-of-the-following-installs)
- [DG\5.3\869](#dg53869)
- [Checking Install for Package DG\5.3\869](#checking-install-for-package-dg53869)
- [# Install Questions for DG\5.3\869](#install-questions-for-dg53869)
- [# # Select the DGPF MISSING PT FLAG REVIEW MAIL GROUP](#select-the-dgpf-missing-pt-flag-review-mail-group)
- [COORDINATOR:CLINICAL,COORDINATOR](#coordinatorclinicalcoordinator)
- [CLINICAL,COORDINATOR ONE](#clinicalcoordinator-one)
- [# Want KIDS to INHIBIT LOGONs during the install? NO//](#want-kids-to-inhibit-logons-during-the-install-no)
- [Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//](#want-to-disable-scheduled-options-menu-options-and-protocols-no)
- [# Enter the Device you want to print the Install messages.](#enter-the-device-you-want-to-print-the-install-messages)
- [You can queue the install by enter a 'Q' at the device prompt.](#you-can-queue-the-install-by-enter-a-q-at-the-device-prompt)
- [Enter a '^' to abort the install.](#enter-a-to-abort-the-install)
- [# DEVICE: HOME//0](#device-home0)
- [# # # DG\5.3\869](#dg53869-1)
- [# Mail Group DGPF MISSING PT FLAG REVIEW created](#mail-group-dgpf-missing-pt-flag-review-created)
- [# # National Category I , Patient Record Flag: MISSING PATIENT created](#national-category-i-patient-record-flag-missing-patient-created)
- [# Updating Routine file...](#updating-routine-file)
- [# Updating KIDS files...](#updating-kids-files)
- [# DG\5.3\869 Installed.](#dg53869-installed)
- [Apr 25, 2013@14:08:47](#apr-25-2013140847)
- [# Install Message](#install-message)
- [l------------------------------------------------------------k](#l-k)
- [100% \| 25 50 75 \|](#100-25-50-75)
- [Complete m------------------------------------------------------------j](#complete-m-j)
- [# # # # Install Completed](#install-completed)
- [# Acronyms](#acronyms)
The Missing Patient Patient Record Flag (PRF) project adds functionality to the Patient Record Flag (PRF) applications in Veterans Information System and Technology Architecture (VistA). The enhancements will provide the ability to identify those Veterans who are missing from Veterans Administration (VA) care.
The Missing Patient PRF will be used to identify a missing patient from a VA facility. This short term Flag will identify a missing patient while in a missing status, so should the patient appear elsewhere in the system, it is immediately known that they are missing from another facility.
> **IMPORTANT:** Users must be assigned the DGPF ASSIGNMENT security key to assign the Missing Patient PRF.

## Related Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The documentation will be in the form of Adobe Acrobat files.

Documentation can also be found on the [VA Software Documentation Library](http://www4.va.gov/vdl/).

| File Name                                  | Description                                                                                                       |
|--------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| DG_53_P869.zip                             | Software and Documentation for MISSING PATIENT - PRF implementation. DG_53_P869.ZIP contains the following files. |
| DG_53_P869.KID                             | Host file containing DG\*5.3\*869 KIDS software distribution                                                      |
| TIU_1_P279.KID                             | Host file containing Text Integration Utility (TIU)\*1.0\*279 KIDS software distribution                          |
| TIUTM.PDF                                  | TIU Technical Manual (TM)                                                                                         |
| TIUUM.PDF                                  | TIUUM.PDF TIU User Manual (UM)                                                                                    |
| PIMSTM.PDF                                 | Changes to the Patient Information Management System (PIMS) Technical Manual                                      |
| Missing Patient PRF_Release Notes.PDF      | Release notes on new features and functionality                                                                   |
| Patient Record Flags_User Guide.PDF        | Patient Record Flag User Guide                                                                                    |
| Missing Patient PRF_Installation Guide.PDF | Installation Guide for patch installation                                                                         |

## Related Web Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                        |                                    |                                                                                                 |
|--------------------------------------------------------|------------------------------------|-------------------------------------------------------------------------------------------------|
| SITE                                               | URL                            | DESCRIPTION                                                                                 |
| National Clinical Reminders site                       | <span class="mark">REDACTED</span> | Contains manuals, presentations, and information about Clinical Reminders                       |
| High Risk Mental Health Patient Reminder and Flag site | <span class="mark">REDACTED</span> | Contains project documents and user documentation for High Risk Mental Health Patient Reminder. |
| Patient Record Flag site                               | <span class="mark">REDACTED</span> | Contains project documents and user documentation for the Patient Record Flags.                 |
| Patient Record Flags VDL                               | <span class="mark">REDACTED</span> | Contains user documentation for the Patient Record Flag.                                        |
| VistA Document Library                                 | <http://www.va.gov/vdl/>           | Contains manuals for Clinical Reminders and related applications.                               |

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommend that the team members who will be responsible for implementing this project coordinate with each other before installing the patches. This team could include Mental Health (MH) coordinators, Suicide Prevention Coordinators, Clinical Application Coordinators (CACs), Reminders Managers, and Information Resource Management (IRM) staff.

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>IMPORTANT:</u> This patch contains the Mumps (M) code executed by the VistA system. The Patch TIU\*1\*279 (TIU_1_P279.KID) is included in the available DG_53_P869.zip file and will need to be installed before DG\*5.3\*869 (DG_53_P869.KID). Follow the "Installation Steps" for the respective patches during installation of that patch.

## Pre-Requisite Software for TIU\*1.0\*279

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package/Patch</strong></td>
<td><strong>Namespace</strong></td>
<td><strong>Version</strong></td>
<td><strong>Comments</strong></td>
</tr>
<tr class="even">
<td><p>Patient Record Flags patch</p>
<p>DG*5.3*650</p></td>
<td>DG</td>
<td>5.3</td>
<td></td>
</tr>
</tbody>
</table>

## ## Pre-Requisite Software for DG\*5.3\*869

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package/Patch</strong></td>
<td><strong>Namespace</strong></td>
<td><strong>Version</strong></td>
<td><strong>Comments</strong></td>
</tr>
<tr class="even">
<td><p>Patient Record Flags patch</p>
<p>DG*5.3*650</p></td>
<td>DG</td>
<td>5.3</td>
<td></td>
</tr>
<tr class="odd">
<td><p>Text Integration Utilities patch</p>
<p>TIU*1.0*279</p></td>
<td>TIU</td>
<td>1.0</td>
<td></td>
</tr>
</tbody>
</table>

## ## # Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual describes how to install the following builds:

- TIU\*1.0\*279
- DG\*5.3\*869

This build can be installed with users on the system, but it should be done during non-peak hours.

This patch can be obtained from the ANONYMOUS.SOFTWARE directory at one of the Office of Information (OI) Field Offices. The preferred method is to file transfer protocol (FTP) the file from <span class="mark">REDACTED</span>, which will transmit the file from the first available server. Alternatively, sites may elect to retrieve the file from a specific OI Field Office.

| OI FIELD OFFICE                    | FTP ADDRESS                        | DIRECTORY                          |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

The software distribution includes:

FILE NAME DESCRIPTION BLOCK SIZE

DG_53_P869.ZIP Contains KIDS files

DG_53_P869.KID

TIU_1_P279.KID

DG_53_P869

> User Documentation

The User Documentation includes the following documentation and file names:

TIU\*1\*279 Documentation

|                                             |                                            |
|---------------------------------------------|--------------------------------------------|
| Documentation                           | Documentation File name                |
| Missing Patient PRF Installation Guide (IG) | Missing Patient PRF_Installation Guide.PDF |
| Missing Patient PRF Release Notes (RN)      | Missing Patient PRF_Release Notes.PDF      |
| TIU Technical Manual (TM)                   | TIUTM.PDF                                  |
| TIU User Manual (UM)                        | TIUUM.PDF                                  |

  
DG\*5.3\*869 Documentation

|                                                               |                                            |
|---------------------------------------------------------------|--------------------------------------------|
| Documentation                                             | Documentation File name                |
| Missing Patient PRF Installation Guide (IG)                   | Missing Patient PRF_Installation Guide.PDF |
| Missing Patient PRF Release Notes (RN)                        | Missing Patient PRF_Release Notes.PDF      |
| Patient Record Flags User Guide (UG)                          | Patient Record Flags_User Guide.PDF        |
| Patient Information Management System (PIMS) Technical Manual | PIMSTM.PDF                                 |

Both patches may be installed with users on the system although it is recommended that each patch be installed during non-peak hours to minimize the potential disruption to users. Installation should take less than five minutes per patch.

> **NOTE:** Specific paths and filenames may vary according to local installation preferences or procedures.

## Installation Steps (TIU\*1\*279):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download the ZIP file, DG_53_P869.zip from the ANONYMOUS.SOFTWARE

> directory of the XXXXXXX Office of Information Field Office (OIFO) to the appropriate directory on your system. Then extract the file TIU_1_P279.KID to the appropriate directory on your system.

2.  Use LOAD A DISTRIBUTION option on the KIDS INSTALLATION menu, and enter the local path and filename of the extracted file:

> for example, SYS\$:\[TMP\]TIU_1_P279.KID

> Note: the locally defined path could be different than the above example.

3.  From the 'Kernel Installation & Distribution System' menu, select the Installation menu.
4.  From this menu, you may now elect to use the following options (when

> prompted for INSTALL NAME, enter TIU\*1.0\*279).

1)  Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT backup any changes such as DDs or templates.
2)  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, Data Dictionaries (DDs), templates, etc.).
3)  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4)  Print Transport Global - this option will allow you to view the components of the KIDS build.
5.  From the install menu, select the Install Package(s) option to install the build (when prompted for INSTALL NAME, enter TIU\*1.0\*279).
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond NO.

# ## Post-Installation Instructions (TIU\*1.0\*279):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine TIUPS279 creates and installs the PATIENT RECORD FLAG CATEGORY I - MISSING PATIENT, TIU Document Definition and the new TIU Title for the MISSING Patient Record Flag Progress Note in the TIU Title Definition File (#8925.1). This post routine, ^TIUPS279, may be removed after installation has successfully completed.

For users to view PRF linked TIU Progress Note Titles, those users must be members of the 'DGPF PATIENT RECORD FLAGS MGR' User Class. The VistA USER CLASS MANAGEMENT \[USR CLASS MANAGEMENT MENU\] option should be used to update this membership.

## Verify Creation of DGPF MISSING PT FLAG REVIEW Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It has been reported from a few sites that the install process for the new Missing Patient, Patient Record Flag and the DGPF MISSING PT FLAG REVIEW mail group set up has not completed successfully.  For this purpose we are distributing the following instructions to ensure your site has no issues with installing these patches:

1.  All sites should have already installed patches ( TIU\*1\*279 and DG\*5.3\*869) by 1/26/14. Due to issues found at some sites, we are requesting that you please verify that the mail group, DGPF MISSING PT FLAG REVIEW, has been created.
- If the mail group and the new Category I PRF are not created as part of the installation process, there could be a potential patient safety issue at your site.
- The mail group (DGPF MISSING PT FLAG REVIEW) must exist before the MISSING PATIENT Patient Record Flag will be added to the Patient Record Flag file.
2.  If the mail group is not created, please manually add the mail group (DGPF MISSING PT FLAG REVIEW) Mail Group:
- Using option Mail Group Edit  \[XMEDITMG\], Enter the following information:

NAME: DGPF MISSING PT FLAG

REVIEW TYPE: public

ALLOW SELF ENROLLMENT?: YES          

RESTRICTIONS: UNRESTRICTED

ORGANIZER: whoever you want

3.  Reinstall the DG\*5.3\*869 patch only. Be aware that the install prompts a question for the “Name of the Mail Group Coordinator” which will need to be answered.
4.  After the above steps are completed, verify that the Missing Patient PRF was added to the PRF National Flag file:
- Using FileMan Inquiry verify entry MISSING PATIENT was added to the PRF NATIONAL FLAG (#26.15) file.

<span class="mark">REDACTED</span>

## ## Installation Steps (DG\*5.3\*869):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download the ZIP file, DG_53_P869.zip from the ANONYMOUS.SOFTWARE directory to the appropriate directory on your system. Then Extract the file DG_53_P869.KID to the appropriate directory on your system.
2.  Use LOAD A DISTRIBUTION option on the KIDS INSTALLATION menu, and enter the local path and filename of the extracted file:

> For example, SYS\$:\[TMP\]DG_53_P869.KID

> Note: the locally defined path could be different than the above example.

3.  From the 'Kernel Installation & Distribution System' menu, select the Installation menu.
4.  From this menu, you may now elect to use the following options (when prompted for INSTALL NAME, enter DG\*5.3\*869).
1)  Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT backup any changes such as DDs or templates.
2)  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.…)
3)  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4)  Print Transport Global - this option will allow you to view the components of the KIDS build.
5.  From the install menu, select the Install Package(s) option to install the build (when prompted for INSTALL NAME, enter DG\*5.3\*869).
6.  When prompted 'Select the DGPF MISSING PT FLAG REVIEW MAIL GROUP

> COORDINATOR:’ respond with the individual that will be the Mail Group’s coordinator.

7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.

## Post-Installation Instructions – (DG\*5.3\*869):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine DG5386P is responsible for the installation of the DGPF MISSING PT FLAG REVIEW mail group and creation of the National, Category I, MISSING PATIENT, Patient Record Flag (PRF). The post routine, ^DG53869P, may be removed after installation has successfully completed.For a user to have the ability to assign the National CAT I MISSING PATIENT, PRF, that user must hold the DGPF Assignment security key.

## Routine Information:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

Routine Name: DG53869P

Before: n/a After: B23654142 \*\*869\*\*Description of Changes:

Routine DG53869P is a new routine and it is a Post Installation routine for patch DG\*5.3\*869. Routine DG53869P can be described as follows:

- Creates Mail Group (DGPF MISSING PT FLAG REVIEW) File \# (3.8)
- Creates Patient Record Flag (MISSING PATIENT) File \# (26.15)

After successful creation and installation of those mentioned items, messages are displayed respectively.

## ## Back-Out Plan for Production Environment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites are encouraged to create a back-up of all routines as a KIDS pre-install step when installing patches DG\*5.3\*869 and TIU\*1\*279. This back-up of routines will cover restoration of routines from all packages if a back-out is necessary.

> **NOTE:** The efficiency of the Back-Out Plan diminishes over time. At some point the VistA recovery process will need to be implemented.

# Appendix A: Installation Examples 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Installation Example - (TIU\*1.0\*279)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of the installation for TIU\*1.0\*279:

# # Select Installation Option: 6  Install Package(s)Select INSTALL NAME: TIU\*1.0\*279       Loaded from Distribution  12/4/13@10:43:01     =\> TIU\*1\*279  ;Created on Sep 10, 2013@13:22:53This Distribution was loaded on Dec 04, 2013@10:43:01 with header ofTIU\*1\*279  ;Created on Sep 10, 2013@13:22:53  It consisted of the following Install(s):   TIU\*1.0\*279Checking Install for Package TIU\*1.0\*279Install Questions for TIU\*1.0\*279Want KIDS to INHIBIT LOGONs during the install? NO//Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//Enter the Device you want to print the Install messages.You can queue the install by enter a 'Q' at the device prompt.Enter a '^' to abort the install.DEVICE: HOME//   DEC Windows--------------------------------------------------------------------------------Install Started for TIU\*1.0\*279 :               Dec 04, 2013@10:45Build Distribution Date: Sep 10, 2013Installing Routines:              Dec 04, 2013@10:45Running Post-Install Routine: MAIN^TIUPS279Title Created: PATIENT RECORD FLAG CATEGORY I - MISSING PATIENTTitle attached to Document Class PATIENT RECORD FLAG CAT IUpdating Routine file...Updating KIDS files...TIU\*1.0\*279 Installed.              Dec 04, 2013@10:45Install Completed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # First-Time Install - DG\*5.3\*869

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# The following is an example of the install for DG\*5.3\*869:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Select Installation Option: Install Package(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Select INSTALL NAME: DG\*5.3\*869 Loaded from Distribution 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 4/25/13@13:57:02

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# =\> DG\*5.3\*869 - KID ;Created on Apr 25, 2013@13:06:58

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # This Distribution was loaded on Apr 25, 2013@13:57:02 with header of

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DG\*5.3\*869 - KID ;Created on Apr 25, 2013@13:06:58

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# It consisted of the following Install(s):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# DG\*5.3\*869

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Checking Install for Package DG\*5.3\*869

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Questions for DG\*5.3\*869

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # Select the DGPF MISSING PT FLAG REVIEW MAIL GROUP 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# COORDINATOR:CLINICAL,COORDINATOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# CLINICAL,COORDINATOR ONE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Want KIDS to INHIBIT LOGONs during the install? NO//

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Enter the Device you want to print the Install messages.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# You can queue the install by enter a 'Q' at the device prompt.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Enter a '^' to abort the install.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DEVICE: HOME//0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # # DG\*5.3\*869

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# -------------------------------------------------------------------------

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Mail Group DGPF MISSING PT FLAG REVIEW created

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # National Category I , Patient Record Flag: MISSING PATIENT created

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating Routine file...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Updating KIDS files...

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # DG\*5.3\*869 Installed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Apr 25, 2013@14:08:47

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Install Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# l------------------------------------------------------------k

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# 100% \| 25 50 75 \|

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Complete m------------------------------------------------------------j

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # # # # Install Completed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# # Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table defines acronyms from this document. For additional acronym definitions, refer to the [OIT Master Glossary](http://vaww.oed.wss.va.gov/process/OIT%20Master%20Glossary/Home.aspx).

| Term  | Definition                                                              |
|-------|-------------------------------------------------------------------------|
| CAC   | Clinical Applications Coordinator                                       |
| CPRS  | Computerized Patient Record System                                      |
| DD    | Data Dictionary                                                         |
| DG    | Registration and Enrollment Package namespace                           |
| FTP   | File Transfer Protocol                                                  |
| GUI   | Graphic User Interface                                                  |
| IRM   | Information Resource Management                                         |
| M     | MUMPS - Massachusetts General Hospital Utility Multi-Programming System |
| MH    | Mental Health                                                           |
| MPRF  | Missing Patient Record Flag                                             |
| OI    | Office of Information                                                   |
| OIFO  | Office of Information Field Office                                      |
| PIMS  | Patient Information Management System                                   |
| PRF   | Patient Record Flag                                                     |
| TIU   | Text Integration Utilities                                              |
| VA    | Department of Veteran Affairs                                           |
| VistA | Veterans Health Information System and Technology Architecture          |