---
title: DG*5.3*887 Meaningful Use New VistA Data Elements (MUNVDE) Preferred Language Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Meaningful Use New VistA Data Elements (MUNVDE) Preferred Language Install Guide
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*887
group_key: "SD:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - installation
  - table
  - contents
  - patient
  - preferred
  - language
  - mark
  - patch
  - routines
  - post
page_count: 0
word_count: 1350
section_count: 1
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/dg_5_3_887_install_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/dg_5_3_887_install_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

Meaningful UseNew VistA Data ElementsPreferred LanguageInstallation Guide

![](dg-5-3-887-meaningful-use-new-vista-data-elements-munvde-preferred-language-inst/001.png)

Patches DG\*5.3\*887SD\*5.3\*619February 2017V 1.2Revision History

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 36%" />
<col style="width: 34%" />
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
<td>2/2017</td>
<td>1.2</td>
<td>Revised host file name</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>8/2016</td>
<td>1.1</td>
<td>Revised per input from Donna Fitch, Release Manager</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/2016</td>
<td>1.0</td>
<td>Section 6, Installation, now contains up-to-date instructions.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>7/2016</td>
<td>0.2</td>
<td>Technical edits</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>8/2014</td>
<td>0.1</td>
<td><p>Initial Installation Instructions.</p>
<p>This patch supports changes that allow the electronic filing of Preferred Language elements to meet the Meaningful Use 2014 Edition certification criteria.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Document Retrieval](#document-retrieval)
- [Pre/Post-Installation Overview](#prepost-installation-overview)
- [Pre-Installation Instructions](#pre-installation-instructions)
- [Installation](#installation)
- [Post-Installation Instructions](#post-installation-instructions)
- [Technical Guide](#technical-guide)
- [Post-Install Routine Summary](#post-install-routine-summary)
- [Back Out/Rollback Procedure](#back-outrollback-procedure)
The Preferred Language Patches (DG\*5.3\*887 and SD\*5.3\*619) are an enhancement to the Veterans Health Information Systems and Technology Architecture (VistA) Patient Registration (DG) and Scheduling (SD) modules. These two bundled patches contain the necessary software changes for capturing a patient’s preferred language (the language that the patient prefers to use during a healthcare visit) in the VA’s CPRS and VistA Systems. These patches are designed to meet the requirements for obtaining the 2011 (formerly Stage 1) Electronic Health Record (EHR) certification to support Meaningful Use (MU) demonstration by the VA in CPRS/VistA for the 2014 Edition certification criteria. Ultimately, VistA will include the functionality needed to obtain both 2014 EHR certifications and to support MU demonstration.
The patient’s preferred language is captured inside the VistA Patient Information Management System (PIMS) modules. The Admissions, Discharges, Transfers (ADT) module, Registration, has been modified so that the Preferred Language information can be captured during the patient registration process (Register a Patient \[DG REGISTER PATIENT\], Load/Edit Patient Data \[DG LOAD PATIENT DATA\], and Eligibility Verification \[DG ELIGIBILITY VERIFICATION\]). Additionally, the Patient Inquiry option has been modified to allow both the Registration option \[DG PATIENT INQUIRY\] and the CPRS GUI link to retrieve and display the preferred language information in a view only format so that the current functionality remains the same. Lastly, a new option, Meaningful Use Language Statistics \[DG MEANINGFUL USE LANG STATS\], has been added to the ADT Manager Menu \[DG MANAGER MENU\] that will allow the user to generate a report that displays the number of active patients that have provided a response to the preferred language prompt.
The Scheduling module has been modified to request and capture preferred language using certain Appointment Menu options for making an appointment (Make Appointment \[SDM\] and Appointment Management \> MA option).
> **NOTE:** Users should be made aware that processing of Preferred Language must ONLY be entered in VistA using menu options. The use of VA FileMan is discouraged.
Below is a list of all the applications involved in this project along with their patch numbers:
| Application/Version             | Patch        |
|---------------------------------|--------------|
| Patient Registration (DG) V 5.3 | DG\*5.3\*887 |
| Scheduling (SD) V 5.3           | SD\*5.3\*619 |
The patches DG\*5.3\*887 and SD\*5.3\*619 are being released in the Kernel Installation and Distribution System (KIDS) combined build distribution: PATIENT_PREFERRED_LANG.KID  
Pre-requisites
The following are required patches that must be installed before this build:
- DG\*5.3\*754
- DG\*5.3\*871
- SD\*5.3\*441
- DI\*22.2\*0
The following routines should be backed up on the system:
- DGRPCADD
- DGRPD
- DGRPE
- DGRPV
- VADPT
- VADPT1
- SDM

# Document Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this build is available.

The documentation will be in the form of Adobe Acrobat files.

The preferred method is to retrieve files from download.vista.med.va.gov. Refer to the patch description for all details.

Documentation can also be found on the VA Software Documentation Library at:

<http://www4.va.gov/vdl/>

| File Description                           | Documentation File Name |
|------------------------------------------------|-----------------------------|
| MUNVDE Preferred Language Installation Guide   | DG_5_3_887_Install_Guide    |
| MUNVDE Preferred Language Release Notes        | DG_5_3_887_Rel_Notes        |
| MUNVDE Preferred Language Implementation Guide | DG_5_3_887_Implement_Guide  |
| ADT Module/Registration Menu User Manual       | dg_5_3_p887_reg_um.pdf      |
| PIMS Technical Manual                          | PIMSTM                      |

# Pre/Post-Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installation, obtain the KIDS build in host file format from one of the designated sites located in the <span class="mark">REDACTED</span> directory. The host file can be retrieved from one of the following OI Field Offices using Secure File Transfer Protocol (SFTP):

> <span class="mark">REDACTED</span>

The host file name for this patch is PATIENT_PREFERRED_LANG.KID and it contains the following builds:

DG\*5.3\*887SD\*5.3\*619

Use ASCII Mode when downloading the file.

There are NO post-installation routines associated with this build.

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This build may be installed with users on the system, but it is recommended that it be installed during non-peak hours to minimize potential disruption to registration or scheduling users. This build should take less than 5 minutes to install.

The installation should be performed by a user with programmer access.

Install the patch first in a training or test account.

The following is an example of the KIDS installation steps for PATIENT_PREFERRED_LANG.KID

1.  Navigate to the Kernel Installation and Distribution System (KIDS) Menu:

    Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

2\. From the Kernel Installation and Distribution System Menu, select Installation:

> Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3\. From the Installation menu, select Load a Distribution:

> When prompted to "Enter a Host File:” enter the full directory path where you saved the host file PATIENT_PREFERRED_LANG.KID<u>.</u> (e.g., /home/anonymous/software/  
> PATIENT_PREFERRED_LANG.KID

> KIDS Distribution saved on Feb 23, 2017@07:31:37

> Comment: Patch DG\*5.3\*887 & SD\*5.3\*619

> This Distribution contains Transport Globals for the following Package(s):

> Build DG\*5.3\*887

> OK to continue with Load? NO// YES

> Build SD\*5.3\*619

> OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES//

> Loading Distribution...

> DG\*5.3\*887

> SD\*5.3\*619

> **NOTE:** Use INSTALL NAME: DG\*5.3\*887 to install this Distribution.

4\. From the Installation menu, you may elect to use the following options:

1.  Verify Checksums in Transport Global – This option will allow you to ensure the integrity of the routines that are in the transport global.
2.  Print Transport Global – This option will allow you to print a summary report of the Transport Global. This includes an exported routine list, install questions, and required builds.
3.  Compare Transport Global to Current System – This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, data dictionaries (DD’s), templates, etc.).
4.  Backup a Transport Global – This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD’s or templates.

5\. For the purpose of this Installation Guide, select Verify Checksums in Transport Global:

> If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in SFTP’ing) and Load the Distribution again. If the problem persists, log a Remedy ticket and/or call the National Service Desk (1-855-673-4357) to report the problem.

> See the example below:

> Select Installation Option: 2 Verify Checksums in Transport Glob

> al

> Select INSTALL NAME: DG\*5.3\*887 5/10/16@09:01:34

> =\> Patch DG\*5.3\*887 & SD\*5.3\*619 ;Created on Feb 23, 2017@07:31:37

> This Distribution was loaded on Feb 25, 2017@09:01:34 with header of

> Patch DG\*5.3\*887 & SD\*5.3\*619 ;Created on Feb 23, 2017@07:31:37

> It consisted of the following Install(s):

> DG\*5.3\*887 SD\*5.3\*619

> Want each Routine Listed with Checksums: Yes// YES

> DEVICE: HOME// HOME (CRT)

> PACKAGE: DG\*5.3\*887 Feb 25, 2017 9:11 am PAGE 1

> -------------------------------------------------------------------------------

> DGMUSTAT Calculated 7514407

> DGRPCADD Calculated 18204630

> DGRPD Calculated 69529511

> DGRPE Calculated 71849762

> DGRPV Calculated 19742844

> VADPT Calculated 16811812

> VADPT0 Calculated 13625852

> VADPT1 Calculated 50294297

> 8 Routines checked, 0 failed.

> PACKAGE: SD\*5.3\*619 Feb 25, 2017 9:11 am PAGE 1

> -------------------------------------------------------------------------------

> SDM Calculated 36241723

> 1 Routine checked, 0 failed.

6\. From the Installation menu, select Install Package(s):

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: DG\*5.3\*887 5/10/16@09:01:34

> =\> Patches DG\*5.3\*887 and SD\*5.3\*619 ;Created on May 04, 2016@12:08:26

> This Distribution was loaded on Feb 25, 2017@09:01:34 with header of

> Patches DG\*5.3\*887 and SD\*5.3\*619 ;Created on Feb 23, 2017@07:31:37

> It consisted of the following Install(s):

> DG\*5.3\*887 SD\*5.3\*619

> Checking Install for Package DG\*5.3\*887

> Install Questions for DG\*5.3\*887

> Incoming Files:

> 2 PATIENT (Partial Definition)

> Note: You already have the 'PATIENT' File.

> Answer the questions the same way that they are answered in the example below.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

> Checking Install for Package SD\*5.3\*619

> Install Questions for SD\*5.3\*619

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// respond YES.  When prompted to select the options you would like to place out of order, enter:

               - DG REGISTER PATIENT
               - DG LOAD PATIENT DATA
               - DG ELIGIBILITY VERIFICATION

> \- SDM  

         - SDAM APPT MGT

    (This will place the listed above options out of order during the installation.)

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// ;;9999 HOME (CRT)

> SD\*5.3\*619

> 

> Install Started for SD\*5.3\*619 :

> Feb 25, 2017@09:12:03

> Build Distribution Date: Apr 19, 2016

> Installing Routines:

> Feb 25, 2017@09:12:03

> Updating Routine file...

> Updating KIDS files...

> SD\*5.3\*619 Installed.

> Feb 25, 2017@09:12:03

> NO Install Message sent

> 

> 

> 100%  25 50 75 

> Complete 

> Install Completed

# Post-Installation Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Technical Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Post-Install Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This summary of routines should match the transport global listing of routines as there are no Post-install routines or actions required.

# Back Out/Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer should have backed up the modified routines by the use of the ‘Backup a Transport Global’ action as specified in the Patch Description Installation Instructions.

The installer can restore the routines using the MailMan message that was created during installing the patch by executing the following steps:

Step 1: Executing the backup message which was created during the installation. By executing this, all existing routines in the build will be restored to their original picture.

Step 2: Delete routine DGMUSTAT.

Step 3: Use the FileMan ENTER OR EDIT FILE ENTRIES option to edit the *Edit the ADT Manager Menu* \[DG MANAGER MENU\] menu in order to delete the *Meaningful Use Language Statistics* \[DG MEANINGFUL USE STATISTICS\] option.

Step 4: Delete the \[DG MEANINGFUL USE STATISTICS\] option from the OPTION file (#19).

Step 5: Delete the LANGUAGE DATE/TIME field (#7) in the PATIENT file (#2).

After completing these steps, the system is back as it was before the preferred language patches were installed.