---
title: Anticoagulation Management Tool Installation/Implementation Guide
doc_type: IG-IMP
doc_label: Implementation Guide
doc_layer: plain
doc_subject: Anticoagulation Management Tool Installation/
app_code: AMT
app_name: Anticoagulation Management Tool
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: This tool was developed at the Portland VA Medical Center to help simplify the complex, time consuming processes required to manage outpatients on anticoagulation medication.
audience: 
keywords: 
  - anticoagulation
  - clinic
  - table
  - contents
  - parameters
  - team
  - management
  - visit
  - installation
  - anticoag
page_count: 0
word_count: 10634
section_count: 10
table_count: 8
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: February 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Anticoagulation_Management_Tool/oramig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Anticoagulation_Management_Tool/oramig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=188"
---

# Anticoagulation Management Tool Installation/Implementation Guide (Patch OR\*3.0\*617)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Anticoagulation Management Tool Installation/Implementation Guide (Patch OR\3.0\617)](#anticoagulation-management-tool-installationimplementation-guide-patch-or30617)
  - [Introduction](#introduction)
    - [Scope](#scope)
    - [Screen Capture Conventions](#screen-capture-conventions)
    - [Online Help](#online-help)
  - [Installing OR\3.0\617](#installing-or30617)
  - [Back-Out Procedure](#back-out-procedure)
    - [Back-Out Strategy](#back-out-strategy)
    - [Back-Out Considerations](#back-out-considerations)
    - [Back-Out Criteria](#back-out-criteria)
    - [Back-Out Risks](#back-out-risks)
    - [Authority for Back-Out](#authority-for-back-out)
    - [Back-out Verification Procedure](#back-out-verification-procedure)
  - [Rollback Procedure](#rollback-procedure)
    - [Rollback Considerations](#rollback-considerations)
    - [Rollback Criteria](#rollback-criteria)
    - [Rollback Risks](#rollback-risks)
    - [Authority for Rollback](#authority-for-rollback)
    - [Rollback Procedure](#rollback-procedure-1)
    - [Rollback Verification Procedure](#rollback-verification-procedure)
    - [Pre-Conditions](#pre-conditions)
    - [Software Retrieval](#software-retrieval)
    - [Configuring Clinics with Default Codes and Additional Indications](#configuring-clinics-with-default-codes-and-additional-indications)
    - [Client Installation Instructions](#client-installation-instructions)
    - [Obtaining Available Documentation Instructions](#obtaining-available-documentation-instructions)
  - [Part B: Configuration from Previous AMT Version](#part-b-configuration-from-previous-amt-version)
    - [Pre-Conditions](#pre-conditions-1)
    - [Client Installation Instructions:](#client-installation-instructions-1)
    - [Reports](#reports)
    - [Auto Sign-on](#auto-sign-on)
  - [Steps for Implementation](#steps-for-implementation)
    - [Assign Menus](#assign-menus)
    - [Check for or Create the following:](#check-for-or-create-the-following)
  - [Clinic Locations](#clinic-locations)
    - [Consult Service](#consult-service)
    - [Set Parameters](#set-parameters)
    - [Set up Tools Menu Option for Anticoagulation Management](#set-up-tools-menu-option-for-anticoagulation-management)
    - [Set Daily Tasks](#set-daily-tasks)
  - [Troubleshooting](#troubleshooting)
    - [Team Lists](#team-lists)
    - [Lab Quick Orders](#lab-quick-orders)
  - [Appendix A: Alternate Workflow](#appendix-a-alternate-workflow)
    - [Team Lists](#team-lists-1)
    - [Clinic Setup](#clinic-setup)
![](anticoagulation-management-tool-installation-implementation-guide/001.png)
February 2026
Office of Enterprise Development
Product Development (PD)
Revision History
<table>
<caption><p>Table 1: Files for Software Retrieval</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 51%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description of Change</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Feb 2026</td>
<td><p>Patch OR*3*617:</p>
<ul>
<li><p>Added <a href="#installing-or3.0617">OR*3*617</a> patch Installation, Back-Out Procedure and Rollback Procedure</p></li>
<li><p>Moved patch <a href="#or3.0600">OR*3*600</a> to Client Installation Instructions</p></li>
</ul></td>
<td>CPRS Development Team</td>
</tr>
<tr class="even">
<td>Feb 2024</td>
<td><p>Patch OR*3*600:</p>
<ul>
<li><p>Added OR*3*600 patch <a href="#installing-or3.0617">Installation</a>, <a href="#_Back-Out_Procedure">Back-Out Procedure</a> and <a href="#rollback-procedure">Rollback Procedure</a></p></li>
<li><p>Moved patch <a href="#or3.0600">OR*3*523</a> to Client Installation Instructions</p></li>
</ul></td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>Aug 2020</td>
<td><p>Patch OR*3*523:</p>
<ul>
<li><p>Updated the Software Retrieval <strong><u>location</u></strong> and added a table caption</p></li>
<li><p>Updated Title page, Revision History, Table of Contents, and Footers</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>Jan 2020</td>
<td>Patch OR*3*516</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>May 2019</td>
<td>Patch OR*505</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Jan 2019</td>
<td>Patch OR *489 – Added the <a href="#installing-or3.0617">Installation Instruction</a></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Nov 2018</td>
<td>Patch OR*3.0*491</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>May 2018</td>
<td>Patch OR *463</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Feb 2018</td>
<td>Patch OR *447</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>May 2015</td>
<td>Patch OR *391</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Sep 2013</td>
<td>Patch OR *354</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>Sept 2011</td>
<td>Patch OR *339</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>Mar 2010</td>
<td>Initial Release</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>
Table 1: Files for Software Retrieval
Table of Contents

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tool was developed at the Portland VA Medical Center to help simplify the complex, time consuming processes required to manage outpatients on anticoagulation medication.

The tool enables the user to enter, review, and continuously update all information connected with patient anticoagulation management. With the Anticoagulation Management Tool (AMT), one can order lab tests, enter outside lab results and graphically review lab data, enter notes, complete encounter data, complete the consults if consults are used to initiate entry into the Anticoagulation clinic, and print a variety of patient letters. Upon exiting the program all activities within the program are viewable on an Anticoagulation flow sheet located on the Computerized Patient Record System (CPRS) Reports tab. AMT provides clinic staff a mechanism of ensuring continuous patient monitoring *with a built-in mechanism that alerts staff when patients haven’t been monitored in a timely period.* A Lost to Follow-up list is maintained to ensure that staff knows of patients who need attention.

### Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of this manual covers the installation steps performed by a Pharmacy Service Automated Data Processing Application Coordinator (ADPAC) or Clinical Application Coordinator (CAC). Other steps, such as performing the Kernel Installation and Distribution System (KIDS) install and downloading the ZIP file from the server used for software distribution are performed by members of the Health Infrastructure and Systems Management. These steps are covered in the Patch Description that accompanies the server side (M) code of this application.

The remainder of the manual is from the initial installation of AMT and previous patches. The information should help the users configure AMT.

### Screen Capture Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this manual, user responses are shown in bold type. In most cases, you need only enter the first few letters to increase speed and accuracy. Pressing the Return or Enter key, which is indicated by the symbol \<Enter\>, must follow every response you enter. This symbol is not shown, but is implied, following bold type entries.

Enter a caret, indicated by the symbol (^), at almost any prompt to terminate the line of questioning and return to the previous level in the routine. Continue entering up-arrows to exit the system.

### Online Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the VistA roll and scroll interface, online help is available at almost any prompt in the software by entering a single question mark (?). This will provide information to help you answer the prompt. In some instances, entering double (??) or triple (???) question marks will provide more detailed information.

The Anti-Coagulation Management (AMT) tool executable also has online help that can be accessed by using the Help \| Contents menu item. Users can then use the Contents, Index, or Search features to locate information about the various features of the AMT tool.

## Installing OR\*3.0\*617

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

OR\*3\*617 should not be installed with Anti-Coagulation users on the system. It is recommended that you install it during non-peak hours to minimize potential disruptions to users. This patch should take less than 5 minutes to install.

<span id="install_instructions" class="anchor"></span>Installation Instructions:Note: An error displays when users cancel out of the PIV login screen. This is by design. Dismiss the error and continue as normal.

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution menu, select the Installation menu. From this menu:
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name. (ex. OR\*3.0\*617)

> Note: Using \<spacebar\>\<enter\> will not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build.

2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup; the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
    1.  At the Installation option menu, select Backup a Transport Global.
    2.  At the Select INSTALL NAME prompt, enter your build OR\*3.0\*617.
    3.  When prompted for the following, enter "R" for Routines or "B" for Build.  
        Select on of the following:

> B Build (including Routines)

> R R

4.  When prompted "Do you wish to secure your build? NO//", press \<enter\> and take the default response of "NO".
5.  When prompted with, "Send mail to: Last name, First Name", press \<enter\> to take default recipient. Add any additional recipients.
6.  When prompted with "Select basket to send to: IN//", press \<enter\> and take the default IN mailbox or select a different mailbox.
3.  You may also elect to use the following options:
    1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
    1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
    2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
    3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

Post -Installation Instructions:

1.  Verify that the post install routine updated parameter ORAM GUI VERSION to 1.0.617.3.
2.  Make the new executable Anticoagulation 1.0.617.3 available.

<span id="_Back-Out_Procedure" class="anchor"></span>

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a catastrophic failure, the Area Manager may make the decision to backout the patch and rollback any necessary database changes. The Area Manager, working with the Cerner transition team, site personnel, tier 2 product support, and the development team will be involved in the decision. However, the Area Manager will make the final decision.

### Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Back-Out Instructions

1.  Install the backup build that was created in Step 2b of the [Installation Instructions](#install_instructions).
2.  Verify that the restore routine reverted parameter ORAM GUI VERSION to 1.0.600.2 (if not, edit the parameter manually).
3.  Make the previous executable, Anticoagulation 1.0.600.2 available.

### Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites should consider how backing out Anticoagulation 1.0.617.0 might affect the system. Sites should consult with the development team and support staff.

#### Load Testing

N/A

#### User Acceptance Testing

The CPRS SQA team tested the Anticoagulation Management Tool 1.0.617 software prior to distribution. Test sites verified that the changes also functioned correctly in their environment.

### Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks for backing out this release are minimal due to the type of changes included.

### Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ultimate authority for backing out lies with the Area Manager.

### Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify that the back-out was successful:

Launch the Anticoagulation Management Tool 1.0.600.2, verify it properly connects with VistA and is running the correct version.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database changes or data was included with this release.

### Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Pre-Conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** It is advisable that ALL users of the AMT software be signed off the system before installing the new version.

Before the AMT can be installed, the following packages and patches must be installed and fully patched in your accounts.

|                                          |         |
|------------------------------------------|---------|
| Application Name                         | Version |
| Authorization/Subscription Utility (ASU) | V. 1.0  |
| Consult/Request Tracking                 | V. 2.5  |
| Kernel                                   | V. 8.0  |
| Laboratory                               | V. 5.2  |
| Order Entry/Results Reporting (OE/RR)    | V. 3.0  |
| Patient Care Encounter (PCE)             | V. 1.0  |
| RPC Broker                               | V 1.1   |
| Text Integration Utilities (TIU)         | V 1.0   |
| ToolKit                                  | V. 7.3  |
| VA FileMan                               | V. 22.0 |

Packages and patches needed for AMT installation

### Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain the current client-side software, retrieve the file OR_30_617.ZIP from the following location:

/srv/vista/patches/SOFTWARE/

| File Name     | Retrieval Format | Size    |
|---------------|------------------|---------|
| OR_30_617.ZIP | BINARY           | 3.75 MB |

The table shows the files needed for the patch and provides the file name, retrieval format, and size of each file.

The ZIP file will contain the following files so that sites can install as they would like (the EXE, CHM, and RAV files should be placed in the files they are locally configured within the existing tool):

- AntiCoagulate.exe
- AntiCoagulate.map
- CRC.TXT
- CVisit.rav
- MAppt No FAX Labs.rav
- MAppt.rav

### Configuring Clinics with Default Codes and Additional Indications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After successful installation of AMT, IT staff should confer with local CACs and AMT users to:

1.  Set the appropriate values for the Automatic Primary and Secondary Indications for Care to be used in each Anticoagulation Clinic. To receive proper workload credit, these should be set as follows:

| Values                                    | Version |
|-------------------------------------------|---------|
| Auto Primary Indic for Care (ICD-9-CM)    | V58.83  |
| Auto Secondary Indic for Care (ICD-9-CM)  | V58.61  |
| Auto Primary Indic for Care (ICD-10-CM)   | Z51.81  |
| Auto Secondary Indic for Care (ICD-10-CM) | Z79.01  |

Appropriate values for the Automatic Primary and Secondary Indications for Care to be used in each Anticoagulation Clinic.

This can be done using the ORAM ANTICOAGULATION CLINIC PARAMETERS VistA option, under the ORAM ANTICOAGULATION SETUP menu.

#### Set up the Anticoagulation Parameters per Clinic

Parameters need to be set for one or more clinic locations, using the same Anticoagulation Clinic Parameters option:

> **NOTE:** All that is required to use the Anticoagulation Management Tool (AMT) for more than one clinic is to repeat the following parameter setup for each clinic.

Before starting the clinic parameter setup, gather the needed information. The following page contains a worksheet for gathering clinic-specific information. Any parameters left blank on this level inherit the Division parameter.

One major addition to the clinic parameters are the CPT codes AMT uses for different kinds of contacts. These codes may be sensitive to variables such as Inpatient or Outpatient as well as the qualifications of the provider. On close examination you may find that a clinic that is offered daily is staffed by a PharmD on Monday, Tuesday, and Friday and an MD on Wednesday and Thursday. In actuality, you have two clinics here with a need for different CPT codes. Consult with the coding experts in your facility for guidance (both clinics should share the same team lists and the team lists will be processed as if there were only one clinic).

Make a copy of it for each clinic you are setting up.

#### Anticoagulation Management Clinic Parameter Worksheet:

| Parameter                                | Value (Clinic) |
|------------------------------------------|----------------|
| Clinic Name                              |                |
| Anticoagulation Team (All)               |                |
| Anticoagulation Team (Complex)           |                |
| Address Line 1                           |                |
| Address Line 2                           |                |
| Address Line 3                           |                |
| Clinic Phone Number                      |                |
| Clinic FAX Number                        |                |
| Toll Free Phone Number                   |                |
| Point of Contact Name                    |                |
| Signature Block Name or Clinic           |                |
| Signature Block Title                    |                |
| Consult Link Enabled (Y or N)            |                |
| Consult Request Service Name             |                |
| PCE Link Enabled (Y or N)                |                |
| Auto Primary Indic for Care (ICD-9-CM)   |                |
| Auto Secondary Indic for Care (ICD-9-CM) |                |
| Auto Primary Indic for Care (ICD-10-CM)  |                |
| Auto Secondary Ind for Care (ICD-10-CM)  |                |
| Simple Phone Visit (CPT)                 |                |
| Complex Phone Visit (CPT)                |                |
| Letter To Patient (CPT)                  |                |
| Orientation Class (CPT)                  |                |
| Initial Office Visit (CPT)               |                |
| Subsequent Visit (CPT)                   |                |
| Anticoagulation VISIT Clinic Location    |                |
| Anticoagulation PHONE Clinic Location    |                |
| Anticoagulation NON-COUNT Clinic         |                |
| Default Pill Strength                    |                |
| Include Time with Next INR Date (Y or 0) |                |
| Look-back Days for Appointment Matching  |                |
| Look-ahead Days for Appointment Matching |                |

Anticoagulation Management Clinic Parameter Worksheet

Here is an example of the clinic parameter setup:

Select GUI Parameters Option: COAG GUI Anticoagulation Parameters

D Division-wide Anticoagulation Parameters

C Anticoagulation Clinic Parameters

Select GUI Anticoagulation Parameters Option: C Anticoagulation Clinic Parameters

Select CLINIC: SLC - ANTICOAGULATION CPRSPROVIDER,SEVEN 

Anticoagulation Clinic Params for Location: SLC - ANTICOAGULATION

------------------------------------------------------------------------------

Clinic Name

Anticoagulation Team (All)

Anticoagulation Team (Complex)

Address Line 1

Address Line 2

Address Line 3

Clinic Phone Number

Clinic FAX Number

Toll Free Phone Number

Point of Contact Name

Signature Block Name or Clinic

Signature Block Title

Consult Link Enabled

Consult Request Service Name

PCE Link Enabled 

Automatic Indication for Care

Simple Phone Visit (CPT)

Complex Phone Visit (CPT)

Letter To Patient (CPT)

Orientation Class (CPT)

Initial Office Visit (CPT)

Subsequent Visit (CPT)

Anticoagulation VISIT Clinic Location

Anticoagulation PHONE Clinic Location

Anticoagulation NON-COUNT Clinic

Default Pill Strength

Include Time with Next INR Date

Look-back Days for Appointment Matching

Look-ahead Days for Appointment Matching

------------------------------------------------------------------------------

Clinic Name: Anticoagulation Main

Anticoagulation Team (All): Anticoagulation M3 Replace \<Enter\>

Anticoagulation Team (Complex): AMT6A

Address Line 1: VA Medical Center

Address Line 2: 0001 Nonexistent Drive

Address Line 3: Salt Lake City, UT 84148

Clinic Phone Number: (801)000-0092x2222

Clinic FAX Number: (801)000-1096

Toll Free Phone Number: 1-(800)000-4012

Point of Contact Name: Anticoagulation Clinic

Signature Block Name or Clinic: Clinical Pharmacist

Signature Block Title: Anticoagulation Clinic

Consult Link Enabled: YES

Consult Request Service Name: ANTICOAGULATION MANAGEMENT ANTICOAGULATION

 MANAGEMENT

PCE Link Enabled: YES

Auto Primary Indic for Care (ICD-9-CM): V85.83

Auto Secondary Indic for Care (ICD-9-CM): V58.61

Auto Primary Indic for Care (ICD-10-CM): Z51.81

Auto Secondary Ind for Care (ICD-10-CM): Z79.01

Simple Phone Visit (CPT) : \<Enter\> 

Complex Phone Visit (CPT) : \<Enter\> 

Letter To Patient (CPT) : \<Enter\>

Orientation Class (CPT) : \<Enter\>

Initial Office Visit (CPT) : \<Enter\>

Subsequent Visit (CPT) : \<Enter\>  

Anticoagulation VISIT Clinic Location: Anticoagulation Main

Anticoagulation PHONE Clinic Location: Anticoagulation Main

Anticoagulation NON-COUNT Clinic: Anticoagulation Main (NON-COUNT)

Default Pill Strength: 5

Include Time with Next INR: YES

Look-back Days for Appointment Matching: \<Enter\>

Look-ahead Days for Appointment Matching: \<Enter\>

Anticoagulation Clinic Params for Location: SLC - ANTICOAGULATION is now:

------------------------------------------------------------------------------

Clinic Name: Anticoagulation Main

Anticoagulation Team (All): Anticoagulation M3 Replace \<Enter\>

Anticoagulation Team (Complex): AMT6A

Address Line 1: VA Medical Center

Address Line 2: 0001 Nonexistent Drive

Address Line 3: Salt Lake City, UT 84148

Clinic Phone Number: (801)000-0092x2222

Clinic FAX Number: (801)000-1096

Toll Free Phone Number: 1-(800)000-4012

Point of Contact Name: Anticoagulation Clinic

Signature Block Name or Clinic: Clinical Pharmacist

Signature Block Title: Anticoagulation Clinic

Consult Link Enabled: YES

Consult Request Service Name: ANTICOAGULATION MANAGEMENT

PCE Link Enabled: YES

Auto Primary Indic for Care (ICD-9-CM): V85.83

Auto Secondary Indic for Care (ICD-9-CM): V58.61

Auto Primary Indic for Care (ICD-10-CM): Z51.81

Auto Secondary Ind for Care (ICD-10-CM): Z79.01

Simple Phone Visit (CPT) :

Complex Phone Visit (CPT) :

Letter To Patient (CPT) :

Orientation Class (CPT) :

Initial Office Visit (CPT) :

Subsequent Visit (CPT) :  

Anticoagulation VISIT Clinic Location: Anticoagulation Main

Anticoagulation PHONE Clinic Location: Anticoagulation Main

Anticoagulation NON-COUNT Clinic: Anticoagulation Main (NON-COUNT)

Default Pill Strength: 5

Include Time with Next INR: YES

Look-back Days for Appointment Matching:

Look-ahead Days for Appointment Matching:

------------------------------------------------------------------------------

Enter RETURN to continue or '^' to exit:

D Division-wide Anticoagulation Parameters

C Anticoagulation Clinic Parameters

Select GUI Anticoagulation Parameters Option:

2.  (Optional) Sites can review the items used in the two parameters for additional indications for care: ORAM INDICATIONS FOR CARE and ORAM I10 INDICATIONS FOR CARE.

### Client Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The software distribution includes following files:

- AntiCoagulate.exe
- AntiCoagulate.map
- CRC.TXT
- CVisit.rav
- MAppt No FAX Labs.rav
- MAppt.rav

#### Executable Methods of Installation 

Use the appropriate method of installation:

- Network (shared) Installation:  
  The executable is placed on a network drive, with a shortcut on users’ desktops. The executable is replaced when no users are accessing the GUI program. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Citrix Installation:  
  The executable is run on a remote workstation and the user views the screen remotely. There are no changes necessary to this method of installation—local policies and procedures should be followed.
- Manual Install:  
  This method is used primarily for debugging purposes, or for emergency or specific testing situations. 

> **IMPORTANT:** Also, please note that the Tools Menu execution of the program does not work unless the .exe is in the same directory on each workstation.

### Obtaining Available Documentation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents will be distributed with OR\*3.0\*617. It will be located on the [VA Document Library (VDL)](http://www.va.gov/vdl/application.asp?appid=188).

- ORAMIG.PDF – Acrobat version of this manual
- ORAMIG.DOCX – Microsoft Word version of this manual

As with all software releases, the .PDF versions of the documentation is the official version and the one you should rely on for further distribution of the entire manual. The .DOCX files are a courtesy to medical centers who want to divide out parts of the manuals, optionally with local.

## Part B: Configuration from Previous AMT Version 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This part of the manual is retained for sites to have previous configuration information only.

### Pre-Conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the AMT can be installed, the following packages and patches must be installed and fully patched in your accounts.

|                                          |         |
|------------------------------------------|---------|
| Application Name                         | Version |
| Authorization/Subscription Utility (ASU) | V 1.0   |
| Consult/Request Tracking                 | V 2.5   |
| Kernel                                   | V 8.0   |
| Laboratory                               | V 5.2   |
| Order Entry/Results Reporting (OE/RR)    | V 3.0   |
| Patient Care Encounter (PCE)             | V 1.0   |
| RPC Broker                               | V 1.1   |
| Text Integration Utilities (TIU)         | V 1.0   |
| ToolKit                                  | V 7.3   |
| VA FileMan                               | V 22.0  |
| Visit Tracking                           | V 2.0   |

### Client Installation Instructions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This information was from the previous patches and is retained here for the site’s reference.

The ZIP file will contain the following files so that sites can install as they would like:

#### OR\*3.0\*600

There was an update to the Windows executable file (AntiCoagulate.exe) that resolves several reported incidents with the software.

The installation for patch OR\*3.0\*600 contained the file OR_30_600.ZIP.

The ZIP file contained the following files:

- ANTICOAGULATE.EXE
- ANTICOAG_HELP_FILE.CHM
- ANTICOAGULATE.MAP
- CRC.TXT
- CVISIT.RAV
- MAPPT NO FAX LABS.RAV
- MAPPT.RAV

#### OR\*3.0\*523

There was an RPC call added to the Delphi code allowing the REQUESTING PACKAGE REFERENCE field to be set.

The installation for patch OR\*3.0\*523 contained the file OR_30_523.ZIP.

The ZIP file contained the following files:

- ANTICOAGULATE.EXE
- ANTICOAG_HELP_FILE.CHM
- ANTICOAGULATE.MAP
- CVISIT.RAV
- MAPPT NO FAX LABS.RAV
- MAPPT.RAV

#### OR\*3.0\*489

There was an update to the Windows executable file (AntiCoagulate.exe) to make it compatible with Windows 10.

The installation for patch OR\*3.0\*489 contained the file OR_30_489.ZIP.

The ZIP file contained the following files:

- AntiCoagulate.exe
- Anticoag_help_file.hlp
- Anticoag help file.cnt
- AntiCoagulate.map
- CVisit.rav
- MAppt No FAX Labs.rav
- MAppt.rav

#### OR\*3.0\*491

There was an update to the Windows executable file (AntiCoagulate.exe) that resolves several reported incidents with the software.

The installation for patch OR\*3.0\*491 contained the file OR_30_491.ZIP.

The ZIP file contained the following files:

- AntiCoagulate.exe
- Anticoag_help_file.hlp
- Anticoag help file.cnt
- AntiCoagulate.map
- CVisit.rav
- MAppt No FAX Labs.rav
- MAppt.rav

#### OR\*3.0\*463

There was an updated Mumps routine in this patch (ORAM1), and a new executable for Outside HCT, NFL-AMT to resolve reported closure issues and problems entering notes.

The installation for patch OR\*3.0\*463 contained the file OR_30_463.ZIP.

The ZIP file contained the following files:

- AntiCoagulate.exe
- Anticoag_help_file.hlp
- Anticoag help file.cnt
- AntiCoagulate.map
- CVisit.rav
- MAppt No FAX Labs.rav
- MAppt.rav

#### OR\*3.0\*447

AMT was previously updated to become two factor authentication (2FA) compliant. The Anticoagulation Management Tool (GUI) required an upgrade to Delphi version XE8 to implement the new Remote Procedure Call (RPC) Broker allowing compliance. Patch OR\*3.0\*447 was the patch that accomplished that update. OR\*3.0\*447 was made up of an informational MUMPS patch and a Windows executable file (AntiCoagulate.exe).

The installation for patch OR\*3.0\*447 contained the file OR_30_447.ZIP.

The ZIP file will contain the following files:

- AntiCoagulate.exe
- Anticoag_help_file.hlp
- Anticoag help file.cnt
- AntiCoagulate.map
- CVisit.rav
- MAppt No FAX Labs.rav
- MAppt.rav

#### OR\*3.0\*391

AMT was previously updated for the International Classification of Diseases, Tenth Revision (ICD-10) coding system when it is implemented. Patch OR\*3.0\*391 was the patch that accomplished that update.

The installation for patch OR\*3.0\*391 contained the file OR_30_391.zip and OR_30_391.KID.

The ZIP file contained the following files:

- AMT_1_0_391_7.msi
- AntiCoagulate.exe
- Anticoag_help_file.chm
- The manual set:
  - ORAMIG.DOC
  - ORAMIG.PDF
  - ORAMTM.DOC
  - ORAMTM.PDF
  - ORAMUM.DOC
  - ORAMUM.PDF

The M routines for patch OR\*3.0\*391 were included in the OR_3_391.KID. After downloading the files, perform the server install of the OR\*3.0\*391 released patch by following these steps:

1.  Verify that patch OR\*3.0\*361 is installed on system before attempting to install OR\*3.0\*391.
2.  From the Kernel Installation & Distribution System menu, select the Installation menu:

KIDS Main Menu (XPD MAIN):

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INstallation

3.  From this menu, choose to Load a Distribution and enter the location of the Host File OR_3_391.KID.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: LOad a Distribution

Enter a Host File: \<Path to KID File\>OR_30_391.KID

KIDS Distribution saved on Jan 28, 2015@09:55:11

Comment: OR\*3\*391 TEST v7

This Distribution contains Transport Globals for the following Package(s):

OR\*3.0\*391

Distribution OK!

Want to Continue with Load? YES// \<Enter\>

Loading Distribution...

OR\*3.0\*391

Use INSTALL NAME: OR\*3.0\*391 to install this Distribution.

4.  From the same menu, you may select to use the following options: (when prompted for INSTALL NAME, enter OR\*3.0\*391).

Use INSTALL NAME: OR\*3.0\*391 to install this Distribution.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: OR,391 OR\*3.0\*391 4/17/15@11:52:51

=\> OR\*3\*391 TEST v7 ;Created on Jan 28, 2015@09:55:11

This Distribution was loaded on Apr 17, 2015@11:52:51 with header of

OR\*3\*391 TEST v7 ;Created on Jan 28, 2015@09:55:11

It consisted of the following Install(s):

OR\*3.0\*391

Want each Routine Listed with Checksums: Yes// \<Enter\> YES

DEVICE: HOME// \<Enter\> TELNET PORT

PACKAGE: OR\*3.0\*391 Apr 17, 2015 11:57 am PAGE 1

-------------------------------------------------------------------------------

ORAM Calculated 83839096

ORAM1 Calculated 175474289

ORAM2 Calculated 58023259

ORAMSET Calculated 59301848

ORAMX Calculated 169673089

ORAMX1 Calculated 81414252

ORY391 Calculated 58110854

7 Routines checked, 0 failed.

Sites can also do the following:

1.  The option PRINT TRANSPORT GLOBAL is an optional function for the installation of this patch. It can provide printed documentation of the components contained in the KIDS build, but again it is optional.
2.  The option COMPARE TRANSPORT GLOBAL TO CURRENT SYSTEM can be run because there is a routine included in this patch that is already on your system. All other routines in the patch are new routines.
3.  The option to BACKUP A TRANSPORT GLOBAL should be run also because there is one routine already on your system, but all the other routines installed are new to the system.
5.  To install the patch, select option \#6 INSTALL PACKAG(S)

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: OR,391 OR\*3.0\*391 4/17/15@12:07:28

=\> OR\*3\*391 TEST v7 ;Created on Jan 28, 2015@09:55:11

This Distribution was loaded on Apr 17, 2015@12:07:28 with header of

OR\*3\*391 TEST v7 ;Created on Jan 28, 2015@09:55:11

It consisted of the following Install(s):

OR\*3.0\*391

Checking Install for Package OR\*3.0\*391

6.  When Prompted "Want KIDS to INHIBIT LOGONs during the install? O//" respond NO.
7.  When Prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.

Want KIDS to INHIBIT LOGONs during the install? NO// \<Enter\>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// \<Enter\>

Enter the Device desired to print the Install messages.

Queue the install by entering a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\> HOME

OR\*3.0\*391

───────────────────────────────────────────────────────────────────────────────

Installing Recurrent PE = 416.2

Installing TIA = 435.9

Installing Valve-Mech = V43.3

Installing Valve-Tissue = V42.2

Updating Routine file...

Updating KIDS files...

OR\*3.0\*391 Installed.

Apr 17, 2015@12:09:32

Not a production UCI

NO Install Message sent

───────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

Install Completed

#### OR\*3.0\*307

The installation for patch OR\*3.0\*307 contained the file OR_30_307.zip. This file was a bundled .ZIP archive and included the following files:

- ANTICOAG HELP FILE.cnt – the help table of contents file
- ANTICOAG_HELP_FILE.HLP – the Windows help file
- ANTICOAGULATE.EXE – the Windows executable file
- CVISIT.RAV – the template file for missed visits
- MAPPT.RAV – the template file for new dosages
- MAPPT NO FAX LABS.RAV – alternate template file for new dosages
- ORAMIG.PDF – Acrobat version of this manual
- ORAMIG.DOC – Microsoft Word version of this manual
- ORAMTM.PDF – Acrobat version of the Technical Manual
- ORAMTM.DOC – Microsoft Word version of the Technical manual
- ORAMUM.PDF – Acrobat version of the User Manual
- ORAMUM.DOC – Microsoft Word version of the User Manual

Sites were instructed to unZIP file OR_30_307.ZIP to a temporary location either on a server or on a furnished workstation depending upon local policies for software installation.

As with all software releases, the .PDF versions of the documentation are the official versions and the ones to be relied on for further distribution of the entire manual. The .DOC files are a courtesy to medical centers who want to divide out parts of the manuals, optionally with local.

The help files previously consisted of the ANTICOAG HELP FILE.cnt and ANTICOAG_HELP_FILE.HLP. With the new help file Anticoag_help_file.chm, the previous help files can be removed.

#### Other File Placement

> Note: *It is against VA security policy to use FAXed results from an outside laboratory*

The CVISIT.RAV, MAPPT.RAV, and MAPPT NO FAX LABS.RAV files should be placed in a shared network directory on a file server. These are Rave Reports Template files, which define the format for Letters that assigned clinicians will send to patients enrolled in the Anticoagulation Management Clinic.

VA Security Policy does NOT allow FAXed results from outside laboratories. Therefore, the letters must not reference faxed results from outside laboratories. To remove that reference in the letters, rename the file MAPPT.RAV to some other name, for example: MAPPT0.RAV, then rename the file MAPPT NO FAX LABS.RAV to MAPPT.RAV. The path to this directory will be identified for the application when the Division-wide Parameters are set, as described in the Installation/ Implementation Guide.

The directory where the .RAV files are located is specified in the parameter setup. In the case of the ANTICOAGULATE.EXE file an example of the parameter setup is given in the [Set up Tools Menu Option for Anticoagulation Management](\l) section. By default, the .CNT and .HLP files must be in the same directory. In the case of the two .RAV files an example of the parameter setup is given in the [Set up the Anticoagulation Parameters per Division](#set-up-the-anticoagulation-parameters-per-division) section.

### Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KIDS install places menu options for reports on the server but does not place them into a personal menu structure. These are:

- Anticoagulation Complication Report \[ORAM COMPLICATIONS REPORT\]
- All Anticoagulation Patients \[ORAM PATIENT LIST ALL\]
- Complex Anticoagulation Patients \[ORAM PATIENT LIST COMPLEX\]
- Next Lab Patient List \[ORAM PATIENT LIST NEXT LAB\]
- Single Patient TTR \[ORAM ROSENDAAL SINGLE PT TTR\]
- Calculate TTR (Rosendaal Method) \[ORAM ROSENDAAL TTR REPORT\]

TTR stands for Time in Therapeutic Range.

The installation also provides two umbrella menu options that provide access to these reports:

- Anticoagulation Management Reports \[ORAM REPORTS MENU\]

This option includes the commands:

C Anticoagulation Complication Report

R Calculate TTR (Rosendaal Method)

S Single Patient TTR

P Anticoagulation Patient Lists

- Anticoagulation Patient Lists ORAM PATIENT LIST MENU

This includes the commands:

A All Anticoagulation Patients

C Complex Anticoagulation Patients

These reports must be assigned to the clinic personnel who need them in the performance of their duties.

To have access to the reports on the menu, users must have them assigned to their menu tree.

### Auto Sign-on

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Anticoagulation Management Tool (AMT) can work more effectively if a site allows users to have Auto Sign-on enabled. If a site desires to enable Auto Sign-on the following steps can be employed.

- IRM will decide to turn on Auto Sign On for a personal site by editing the KERNEL SYSTEMS PARAMETERS file (#8989.3). Within 8989.3 set the fields DEFAULT AUTO SIGN-ON to Yes (or 1) and the field DEFAULT MULTIPLE SIGN-ON LIMIT to 2 or greater.
- In the NEW PERSON File (#200) each clinic worker using the Anticoagulator GUI needs to have the field MULTIPLE SIGN-ON set to ALLOWED. This field is accessed through the EVE editing program.
- The RPC client broker (ClAgent.exe) must be installed and running on each clinic workstation.

Auto Sign-on is different from Single Sign-on, which relies on Clinical Context Object Workgroup (CCOW) to work and is not supported by AMT.

## Steps for Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Assign Menus
2.  Check for or Create:
    1.  Team Lists
    2.  TIU Document Definitions
    3.  Clinic Locations
    4.  Consult Service
    5.  DSS Unit
3.  Option ORMGR - CPRS Manager Menu

> Set up the Anticoagulation Parameters per Division

> Set up the Anticoagulation Parameters per Clinic

1.  Set up Tools Menu Option for Anticoagulation Management
5.  Set Daily Tasks

> Run ORAM SET TEAMS

### Assign Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ORAM ANTICOAGULATION CONTEXT is the option used by this application to communicate with the Kernel Broker. AntiCoagulate.exe cannot run on a workstation unless this menu option or programmer access mode are obtained. All users of this application must have this menu assigned to them as a secondary menu or as part of their primary menu tree.

Users with administrative duties should also have the one or more of the following menus assigned:

- Anticoagulation Management Reports \[ORAM REPORTS MENU\]
- Anticoagulation Patient Lists \[ORAM PATIENT LIST MENU\]

### Check for or Create the following: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before entering the parameter values that determine the behavior of the application, check the system to see whether there are Team Lists, TIU Document Titles, Hospital Locations, Consult Service, and DSS ID entries that can be used for the Anticoagulation Management Tool (AMT) with little or no modifications.

> **NOTE:** *Be sure to make note of the results of this step for use in step 3, [Option ORMGR - CPRS Manager Menu](#set-parameters).*

#### Team Lists 

Use the Team List Mgmt Menu option \[ORLP TEAM MENU\] to check whether existing team lists may suffice. In most cases the creation of two new team lists will be needed:

1.  Anticoagulation Team (All)

    The Anticoagulation Team (ALL) list, shows all patients scheduled for that team for that day AND any patients NOT completed on previous days. Patients drop off this list as they are completed in the Anticoagulation Management Tool (AMT).
2.  Anticoagulation Team (Complex)

    The Anticoagulation Team (COMPLEX) patient list pulls out the complex patients so that they are not lost on the larger list (they appear on both lists).

    Patients drop off these lists as they are completed in AMT.

> This is a FileMan listing for the two team lists that are used for AMT.

NAME: ANTICOAGULATION TEAM (ALL) TYPE: TEAM PATIENT MANUAL

UPPER CASE: ANTICOAG ALL CREATOR: CPRSPROVIDER,SEVEN

CREATION D/T: MAY 20, 2003

USER: CPRSPROVIDER,SIX

MEMBER: CP. . .

. . .

NAME: ANTICOAGULATION TEAM (COMPLEX) TYPE: MANUAL REMOVAL/AUTOLINK ADDITION

UPPER CASE: ANTICOAG COMPLEX CREATOR: CPRSPROVIDER,SEVEN

SUBSCRIBE: YES CREATION D/T: SEP 05, 2003

USER: CPRSPROVIDER,SIX

USER: CPRSPROVIDER,ONE

USER: CPRSPROVIDER,SEVEN

MEMBER: CP. . .

> Please note that it is not necessary to use exactly these same team names because the link between these teams and AMT is explicitly set in the GUI Anticoagulation Parameters.

#### TIU Document Definitions

The Anticoagulation Management Tool (AMT) uses three (3) parameters to store TIU note titles that document an initial visit, an interim or routine visit, and the discharge visit. Use the Edit Document Definitions \[TIUF EDIT DDEFS MGR\] option to check whether adequate titles are already defined to support these, or create a new Document Class for Anticoagulation, along with these Titles:

1.  Anticoagulation Initial Note

> This is the TIU Document Title that identifies the Anticoagulation Initial Assessment Note, which is entered for the patient's first visit upon enrollment in the Clinic.

2.  Anticoagulation Interim Note

> This is the TIU Document Title that identifies the Anticoagulation Interim Note, which is entered during the patient's ongoing treatment by the Anticoagulation clinic.

3.  Anticoagulation Discharge Note

> This is the TIU Document Title that identifies the Anticoagulation Discharge Note, which is entered upon the patient's discharge from the Anticoagulation clinic.

> **NOTE:** *If the VHA ENTEPRISE STANDARD TITLEs, as shown in the screen capture, is not used, then use the Title Mapping Utilities … \[TIU MAP TITLES MENU\] to map the titles used to VHA ENTRPRISE STANDARD TITLEs*

> Make a note of the titles for use in the parameter setup outlined [below](#set-parameters). Here is a FileMan inquiry from the TIU Document Definition file (8925.1) covering documents needed for Anticoagulation Management:

NAME: ANTICOAG INITIAL NOTE ELECTRONIC

PRINT NAME: ANTICOAG INITIAL NOTE

TYPE: TITLE CLASS OWNER: CLINICAL COORDINATOR

STATUS: ACTIVE SUPPRESS VISIT SELECTION: YES

VHA ENTERPRISE STANDARD TITLE: INITIAL EVALUATION NOTE

MAP ATTEMPTED: DEC 07, 2006@14:58:44 MAP ATTEMPTED BY: BRENK,THOMAS M

TIMESTAMP: 59372,53350

NAME: ANTICOAG DISCHARGE PRINT NAME: ANTICOAG DISCHARGE

TYPE: TITLE CLASS OWNER: CLINICAL COORDINATOR

STATUS: ACTIVE

VHA ENTERPRISE STANDARD TITLE: PHARMACY COUNSELING DISCHARGE NOTE

MAP ATTEMPTED: DEC 07, 2006@13:35:43 MAP ATTEMPTED BY: BRENK,THOMAS M

TIMESTAMP: 59457,48152

NAME: ANTICOAGULATION PRINT NAME: ANTICOAGULATION

TYPE: TITLE CLASS OWNER: CLINICAL COORDINATOR

STATUS: ACTIVE SUPPRESS VISIT SELECTION: YES

VHA ENTERPRISE STANDARD TITLE: PHARMACY NOTE

MAP ATTEMPTED: DEC 07, 2006@13:37:03 MAP ATTEMPTED BY: BRENK,THOMAS M

TIMESTAMP: 58834,55125

## Clinic Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Set up a Clinic \[SDBUILD\] option to check whether existing Clinics can be used in place of these, or to create new Clinic Locations:

1.  Anticoagulation VISIT Clinic Location

> This should be a Clinic for FACE to FACE visits. The program does not care if the same clinic is used for both the phone and face to face, but for PCE credit they must be COUNT CLINICS.

2.  Anticoagulation PHONE Clinic Location

> This should be a Clinic for Telephone visits. The program does not care if you use the same clinic for both the phone and face to face, but for PCE credit they must be COUNT CLINICS.

3.  Anticoagulation NON-COUNT Clinic

> This is a NON-COUNT clinic location, which will be used for notes only, when no PCE data is recorded.

If you have only one physical anticoagulation clinic, we strongly urge that you use these names.

The following is a FileMan list showing an example of a typical set of hospital locations that can be used for Anticoagulation Management:

FILE 44: HOSPITAL LOCATION

INDEX: 8005 NAME: EC ANTICOAGULATION

ABBREVIATION: COAG TYPE: CLINIC

INSTITUTION: PORTLAND (OR) VAMC

STOP CODE NUMBER: ANTI-COAGULATION CLINIC

SERVICE: MEDICINE PHYSICAL LOCATION: ANTICOAG

DIVISION: PORTLAND NON-COUNT CLINIC? (Y OR N): NO

CREDIT STOP CODE: CLINICAL PHARMACY CLINIC MEETS AT THIS FACILITY?: YES

TYPE EXTENSION: CLINIC WORKLOAD VALIDATION AT CHK OUT: YES

SYNONYM: EANTI

PRINT ACTION PROFILE: YES DEFAULT APPOINTMENT TYPE: REGULAR

PROVIDER: ORPROVIDER,EIGHT

PROVIDER: m

PROVIDER: n

PROVIDER: h  DEFAULT PROVIDER: YES

REQUIRE ACTION PROFILES?: YES ALLOWABLE CONSECUTIVE NO-SHOWS: 2

MAX \# DAYS FOR FUTURE BOOKING: 390 MAX \# DAYS FOR AUTO-REBOOK: 1

PRIVILEGED USER: MA

PRIVILEGED USER: SC

PROHIBIT ACCESS TO CLINIC?: YES LENGTH OF APP'T: 15

DISPLAY INCREMENTS PER HOUR: 15-MIN OVERBOOKS/DAY MAXIMUM: 25

INDEX: 9727 NAME: EC ANTICOAG PHONE

ABBREVIATION: COAG TYPE: CLINIC

INSTITUTION: PORTLAND (OR) VAMC STOP CODE NUMBER: TELEPHONE/ANCILLARY

SERVICE: MEDICINE DIVISION: PORTLAND

COLLATERAL VISITS? (Y OR N): NO NON-COUNT CLINIC? (Y OR N): NO

CREDIT STOP CODE: ANTI-COAGULATION CLINIC

CLINIC MEETS AT THIS FACILITY?: YES TREATING SPECIALTY: GENERAL MEDICINE

TYPE EXTENSION: CLINIC

 EXTENDED SPECIAL INSTRUCTIONS: Clinic used for the capture of anti-coag

 telephone visits - Event Capture creates appointments in this clinic

 automatically.

 Created to separate telephone from provider contact calls, so that patients

 will not be billed as if they saw a provider when in fact they received a

 telephone call only.

DATE/TIME CLINIC BUILT: NOV 21, 2003@12:14:10

DEFAULT APPOINTMENT TYPE: REGULAR

PROVIDER: ORPROVIDER,EIGHT

REQUIRE ACTION PROFILES?: NO ALLOWABLE CONSECUTIVE NO-SHOWS: 0

MAX \# DAYS FOR FUTURE BOOKING: 11 MAX \# DAYS FOR AUTO-REBOOK: 1

LENGTH OF APP'T: 15  DISPLAY INCREMENTS PER HOUR: 15-MIN

OVERBOOKS/DAY MAXIMUM: 0

PATTERN DATE: JAN 19, 2004

....(MANY PATTERN DATES)

NonCount example:

INDEX: 7007 NAME: ANTICOAGULATION LAB +

ABBREVIATION: COAG TYPE: CLINIC

INSTITUTION: PORTLAND (OR) VAMC STOP CODE NUMBER: LABORATORY

SERVICE: MEDICINE PHYSICAL LOCATION: COAG

DIVISION: PORTLAND NON-COUNT CLINIC? (Y OR N): YES

CLINIC MEETS AT THIS FACILITY?: YES INCLUDE ON FILE ROOM LISTS?: YES

TYPE EXTENSION: CLINIC WORKLOAD VALIDATION AT CHK OUT: YES

SYNONYM: COAGLAB

TELEPHONE: 5460 OMNICELL INTERFACE: OMNICELL

PRINT ACTION PROFILE: YES CONFIRMATION LETTER: ANTICOAG

EXCLUDE ON INELIGIBLE SCREEN?: Y

 EXTENDED SPECIAL INSTRUCTIONS: DO NOT schedule, reschedule or cancel in this

 clinic, contact Anticoag at ext 52496.

\*\*\* PLEASE NOTE \*\*\*\*

If patient requests sooner or delayed appt than ordered, please send

 priority email to "G.Anticoag".

Always verify current home telephone!!!

PROGRAM: AREA A COAG

DATE/TIME CLINIC BUILT: MAR 03, 1995@11:14:01

DEFAULT APPOINTMENT TYPE: REGULAR

MAF CONFIRM VET APPT: YES, ON MAF 'CONFIRM LIST'

### Consult Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is highly recommended that you use a consult request to move new patients into this program. If you opt to not use consults, you can skip this step and mark Consult Enabled to No in the parameter setup. However, the only other feature of VistA that might be useful to is the Additional Signers feature of Progress Notes. If you describe a patient’s condition, then specify a key member of the Anticoagulation Team, that member will get an alert and be able to read the progress not. All-in-all, using a consult is a much more straight-forward procedure.

Use the Set-up Consult Services option \[GMRC SETUP REQUEST SERVICES\] to determine whether there’s already an Anticoagulation Consult Request Service. If you have only one clinic, then it should be called:

#### Anticoagulation Management

This is the name to the Consult Request Service with which Consult data will be associated for the Anticoagulation clinic. It is used only if the linkage with the Consult Package is enabled.

If there is more than one anticoagulation clinic, then you need a consult service for each of them—appropriately named.

If you are using consults to start anticoagulation management of patients now, you may already have a consult service set up. The pharmacists who use the system (that is, close the consult) need to be users in the Request Service file. To easily allow for coverage and changes to personnel, the whole user class can be assigned. Here is an example of using the Setup Consult Services option \[CMRC SETUP REQUEST SERVICES\] for Anticoagulation Management:

Select OPTION NAME: gmrc mgr Consult Management

RPT Consult Tracking Reports ...

SS Set up Consult Services

SU Service User Management

CS Consult Service Tracking

RX Pharmacy TPN Consults

GU Group update of consult/procedure requests

UA Determine users' update authority

UN Determine if user is notification recipient

NR Determine notification recipients for a service

TD Test Default Reason for Request

LH List Consult Service Hierarchy

PR Setup procedures

CP Copy Prosthetics services

DS Duplicate Sub-Service

IFC IFC Management Menu ...

TP Print Test Page

Select Consult Management Option: SS Set up Consult Services

Select Service/Specialty:ANTICOAGULATION MANAGEMENT

SERVICE NAME: ANTICOAGULATION MANAGEMENT Replace

ABBREVIATED PRINT NAME (Optional): Anticoa Anticoa

INTERNAL NAME: ANTICOAGULATION ANTICOAGULATION

Select SYNONYM: Coumadin Coumadin

SERVICE USAGE:

SERVICE PRINTER: Pharm01

NOTIFY SERVICE ON DC: ALWAYS ALWAYS

REPRINT 513 ON DC: NEVER NEVER

PREREQUISITE:

1\>Please be aware that this consult service has required

2\>questions which must be answered in order for your consult to be properly

3\>addressed.

4\>

5\>Anticoagulation Program (ACP) will assume management once patient is

6\>enrolled into program by attending first orientation class, or \*if\* other

7\>arrangements \*are\* made directly with clinic. PCP or designee \*must\* assume

8\>management until pt is enrolled into ACP. 

9\> \<Enter\>

EDIT Option:

PROVISIONAL DX PROMPT: OPTIONAL OPTIONAL

PROVISIONAL DX INPUT: FREE TEXT FREE TEXT

DEFAULT REASON FOR REQUEST:

1\> (Template Not Complete)

2\> \<Enter\>

RESTRICT DEFAULT REASON EDIT: NO EDITING NO EDITING

Inter-facility information

IFC ROUTING SITE: \<Enter\>

IFC REMOTE NAME: \<Enter\>

Select IFC SENDING FACILITY: \<Enter\>

SERVICE INDIVIDUAL TO NOTIFY: CPRSPROVIDER,SEVEN CPRSPROVIDER,SEVEN

Select SERVICE TEAM TO NOTIFY: ANTICOAGULATION – ALL ANTICOAGULATION - ALL

Select NOTIFICATION BY PT LOCATION: \<Enter\>

PROCESS PARENTS FOR NOTIFS: \<Enter\>

Select UPDATE USERS W/O NOTIFICATIONS: \<Enter\>

Select UPDATE TEAMS W/O NOTIFICATIONS: \<Enter\>

Select UPDATE USER CLASS W/O NOTIFS: PHARMACIST

Are you adding 'PHARMACIST' as a new UPDATE USER CLASSES W/O NOTIFS (the 1<sup>ST</sup>

for this REQUEST SERVICES)? No// (No) ??

Select UPDATE USER CLASS W/O NOTIFS: CLINICAL PHARMACIST

Are you adding 'CLINICAL PHARMACIST' as a new UPDATE USER CLASSES W/O NOTIFS

(the 1ST for this REQUEST SERVICES)? No// Y (Yes)

Select UPDATE USER CLASS W/O NOTIFS: PHARMACIST

Are you adding 'PHARMACIST' as a new UPDATE USER CLASSES W/O NOTIFS (the 2<sup>ND</sup>

for this REQUEST SERVICES)? No// Y (Yes)

Select UPDATE USER CLASS W/O NOTIFS: PHARMACY STUDENT

Are you adding 'PHARMACY STUDENT' as a new UPDATE USER CLASSES W/O NOTIFS

(the 3RD for this REQUEST SERVICES)? No// Y (Yes)

Select UPDATE USER CLASS W/O NOTIFS: \<Enter\>

Select ADMINISTRATIVE UPDATE USER: CPRSPROVIDER,SEVEN CPRSPROVIDER,SEVEN

SRC Pharmacy Staff Pharmacist

Are you adding 'CPRSPROVIDER,SEVEN' as a new ADMINISTRATIVE UPDATE USERS (the

2ND for this REQUEST SERVICES)? No// Y (Yes)

NOTIFICATION RECIPIENT: Y YES

Select ADMINISTRATIVE UPDATE USER:

Select ADMINISTRATIVE UPDATE TEAM:

PROCESS PARENTS FOR UPDATES:

SPECIAL UPDATES INDIVIDUAL: CPRSPROVIDER,SEVEN

RESULT MGMT USER CLASS: \<Enter\>

UNRESTRICTED ACCESS: \<Enter\>

Select SUB-SERVICE/SPECIALTY: \<Enter\>

ADMINISTRATIVE: \<Enter\>

Add/Edit Another Service? NO//

#### Decision Support System Unit

Decision Support System Extracts (DSS) V. 3.0 provides a means of exporting data from selected Veterans Health Information Systems and Technology Architecture (VistA) modules to a Decision Support System (DSS) resident in the VA Austin Information Technology Center (AITC). This system is the VA's only means of complying with the Congressional mandate for the use of a management system that can assign costs to the product level. DSS unit codes were installed with the DSS application and can be checked both here and in the parameter setup to insure the values are correct.

DSS Unit: This is the name to the DSS Unit to which the anticoagulation data will be associated. Use VA FileMan to inquire to the DSS Unit File to:

1.  Determine whether a DSS Unit for Anticoagulation already exists
2.  To create a new DSS Unit if an adequate substitute doesn’t exist.

> **NOTE:** *This file must not be directly modified using FileMan! Please contact your local DSS coordinator if a DSS unit needs to be added.*

Here is a FileMan printout from the DSS UNIT file (#754):

NAME: ANTICOAG SERVICE: MEDICINE

MEDICAL SPECIALTY: AMBULATORY CARE COST CENTER: 820100 Medical

UNIT NUMBER: MMG1 INACTIVE (Y/N): NO

USE FOR EVENT CAPTURE: YES CATEGORY (Y/N): NO

DATA ENTRY DATE/TIME DEFAULT: NOW SEND TO PCE: Send All Records

DSS ID from the clinic stop file (40.7)

NAME: ANTI-COAGULATION CLINIC AMIS REPORTING STOP CODE: 317

COST DISTRIBUTION CENTER: 2110.00 RESTRICTION TYPE: Either

### Set Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Parameters are set on the division and clinic level. Any parameter that is on both levels can be inherited; if not set for clinic the division value is used. The division corresponds to the medical center. One or more clinics can be established in each division—at least one clinic must be defined. (Look in Appendix A: Alternate Workflow at [Clinic Setup](#installing-or3.0617) for a discussion of division/clinic structure.)

Before starting the parameter setup, gather the information you need. Review the screen captures below and make sure you have the correct information for your medical clinic and medical center. Included on the next page is a worksheet that could be used to assist you in this process. Make a copy of it for each Division you are responsible for.

#### Anticoagulation Management Division Parameter Worksheet:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><br />
Parameter</th>
<th>Value (Division)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Your Medical Center Name</td>
<td></td>
</tr>
<tr class="even">
<td>Complete path to network folder where .RAV files are accessible</td>
<td></td>
</tr>
<tr class="odd">
<td>The local names for International Normalization Ratio (INR) quick order</td>
<td></td>
</tr>
<tr class="even">
<td>The local names for Complete Blood Count (CBC) quick order</td>
<td></td>
</tr>
<tr class="odd">
<td>Track Hematocrit (HCT) or Hemoglobin (Hgb) HGB</td>
<td></td>
</tr>
<tr class="even">
<td><p>The note titles used for anticoagulation at your site:</p>
<p>Anticoagulation Initial Note Title:</p>
<p>Anticoagulation Interim Note Title:</p>
<p>Anticoagulation Discharge Note Title:</p></td>
<td></td>
</tr>
<tr class="odd">
<td><p>The Current Procedural Terminology (CPT) codes for</p>
<p>Simple telephone Visit:</p>
<p>Complex Telephone Visit:</p>
<p>Letter to the Patient:</p>
<p>Orientation Class:</p>
<p>Initial Office Visit:</p>
<p>Subsequent Office Visit:</p></td>
<td></td>
</tr>
<tr class="even">
<td>The Decision Support System (DSS) unit</td>
<td></td>
</tr>
<tr class="odd">
<td>DSS ID</td>
<td></td>
</tr>
</tbody>
</table>

#### Set up the Anticoagulation Parameters per Division

Starting from the ORMGR option, follow the CPRS Configuration \| GUI Parameters \| GUI Anticoagulation Parameters menu path, to set up the parameters for each division defined on your VistA system.

DEV5A3:CPRS27\>D ^XUP

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT320

Select OPTION NAME: ORMGR CPRS Manager Menu

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

CLOZ GUI Edit Inpatient Clozapine Message

COAG GUI Anticoagulation Parameters ...

EIE GUI Mark Allergy Entered in Error

Select GUI Parameters Option: COAG GUI Anticoagulation Parameters

D Division-wide Anticoagulation Parameters

C Anticoagulation Clinic Parameters

Select GUI Anticoagulation Parameters Option: d Division-wide

Anticoagulation Parameters

Enter Anticoagulation Management Parameters by Division:

Select INSTITUTION NAME: salt lake city hCS UT VAMC 660

Anticoagulation Site Params for Division: SALT LAKE CITY HCS

------------------------------------------------------------------------------

Medical Center Name Salt Lake City VAHCS

Complete path to network folder \\VHAISLMul1\OfficeCommon\Anticoagulation Flow

Sheet\\

INR Quick Order  LRTZ PT WITH INR OP

CBC Quick Order LRTZ CBC SP ONCE

Hematocrit (HCT) or Hemoglobin (Hgb) HGB

Anticoagulation Initial Note ANTICOAGULATION INITIAL ASSESS

MENT NOTE

Anticoagulation Interim Note ANTICOAGULATION E&M NOTE

Anticoagulation Discharge Note ANTICOAGULATION DISCHARGE NOTE

Simple Phone Visit (CPT) 99364

Complex Phone Visit (CPT) 99363

Letter To Patient (CPT) 99364

Orientation Class (CPT) 99078

Initial Office Visit (CPT) 99363

Subsequent Visit (CPT) 99364

DSS Unit ANTICOAG CLINIC (317/160)

DSS ID ANTI-COAGULATION CLINIC

------------------------------------------------------------------------------

Medical Center Name: Salt Lake City VAHCS Replace \<Enter\>

Complete path to network folder: \\VHAISLMul1\OfficeCommon\Anticoagulation Flow

Sheet\\ Replace \<Enter\>

INR Quick Order: INR// \<Enter\> LRTZ PT WITH INR OP LRTZ PT WITH INR OP 

CBC Quick Order: CBC// \<Enter\> LRTZ CBC SP ONCE LRTZ CBC SP ONCE

Hematocrit (HCT) or Hemoglobin (Hgb): HCT// \<Enter\> HCT HCT

Initial Note Title: ANTICOAGULATION INITIAL ASSESSMENT NOTE// \<Enter\> ANTICOAGULATION INITIAL ASSESSMENT NOTE TITLE

Std Title: PHARMACY E & M OF ANTICOAGULATION NOTE ANTICOAGULATION INITIAL

 ASSESSMENT NOTE TITLE

Std Title: PHARMACY E & M OF ANTICOAGULATION NOTE

Interim Note Title: ANTICOAGULATION E&M NOTE// \<Enter\> ANTICOAGULATION E&M NOTE TITLE

Std Title: PHARMACY OUTPATIENT E & M OF ANTICOAGULATION NOTE ANTICOAGULAT

ION E&M NOTE TITLE

Std Title: PHARMACY OUTPATIENT E & M OF ANTICOAGULATION NOTE

Discharge Note Title: ANTICOAGULATION DISCHARGE NOTE// \<Enter\> ANTICOAGULATION DISCHARGE NOTE TITLE

Std Title: E & M OF ANTICOAGULATION REPORT ANTICOAGULATION DISCHARGE NOTE

TITLE

Std Title: E & M OF ANTICOAGULATION REPORT

Simple Telephone Visit (CPT): 99364// \<Enter\> 99364 ANTICOAG MGMT, SUBSEQ 99364 ANTICOAG MGMT, SUBSEQ

Complex Phone Visit (CPT): 99363// \<Enter\> 99363 ANTICOAG MGMT, INIT 99363 ANTICOAG MGMT, INIT

Letter to Patient (CPT): 99364// \<Enter\> 99364 ANTICOAG MGMT, SUBSEQ 99364 ANTICOAG MGMT, SUBSEQ

Orientation Class (CPT): 99078// \<Enter\> 99078 GROUP HEALTH EDUCATION 99078 GROUP HEALTH EDUCATION

Initial Office Visit (CPT): 99363// \<Enter\> 99363 ANTICOAG MGMT, INIT 99363 ANTICOAG MGMT, INIT

Subsequent Office Visit (CPT): 99364// \<Enter\> 99364 ANTICOAG MGMT, SUBSEQ 99364 ANTICOAG MGMT, SUBSEQ

DSS Unit: ANTICOAG CLINIC (317/160)// ?

Answer with DSS UNIT NAME, or UNIT NUMBER

Choose from:

ADMISSION 2

ANTICOAG CLINIC (147) MMG#

ANTICOAG CLINIC (317/160) MMG#

ANTICOAGULATION CLINIC (317) MMG#

RADIOLOGY ONCOLOGY 1

DSS Unit: ANTICOAG CLINIC (317/160)// \<Enter\> ANTICOAG CLINIC (317/160) MMG# ANTICOAG CLINIC (317/160) MMG#

DSS ID: ANTI-COAGULATION CLINIC// \<Enter\> ANTI-COAGULATION CLINIC 317 ANTI-COAGULATION CLINIC 317

Anticoagulation Site Params for Division: SALT LAKE CITY HCS is now:

------------------------------------------------------------------------------

Medical Center Name Salt Lake City VAHCS

Complete path to network folder \\VHAISLMul1\OfficeCommon\Anticoagulation Flow

INR Orderable Item LRTZ PT WITH INR OP

CBC Orderable Item LRTZ CBC SP ONCE

Hematocrit (HCT) or Hemoglobin (Hgb) HGB

Anticoagulation Initial Note ANTICOAGULATION INITIAL ASSESS

MENT NOTE

Anticoagulation Interim Note ANTICOAGULATION E&M NOTE

Anticoagulation Discharge Note ANTICOAGULATION DISCHARGE NOTE

Simple Phone Visit (CPT) 99364

Complex Phone Visit (CPT) 99363

Letter To Patient (CPT) 99364

Orientation Class (CPT) 99078

Initial Office Visit (CPT) 99363

Subsequent Visit (CPT) 99364

DSS Unit ANTICOAG CLINIC (317/160)

DSS ID ANTI-COAGULATION CLINIC

------------------------------------------------------------------------------

Enter RETURN to continue or '^' to exit: \<Enter\>

D Division-wide Anticoagulation Parameters

C Anticoagulation Clinic Parameters

Select GUI Anticoagulation Parameters Option:

#### Set up the Anticoagulation Parameters per Clinic

Next, you’ll need to set parameters for one or more clinic locations, using the same Anticoagulation Clinic Parameters option:

> **NOTE:** *All that’s required to use the Anticoagulation Management Tool (AMT) for more than one clinic is to repeat the following parameter setup for each clinic.*

Before starting the clinic parameter setup, gather the information you need. The following page contains a worksheet is for gathering clinic-specific information. Any parameters left blank on this level inherit the Division parameter.

One major addition to the clinic parameters are the CPT codes AMT uses for different kinds of contacts. These codes may be sensitive to variables such as Inpatient or Outpatient as well as the qualifications of the provider. On close examination you may find that a clinic that is offered daily is staffed by a PharmD on Monday, Tuesday, and Friday and an MD on Wednesday and Thursday. On close examination you actually have two clinics here with a need for different CPT codes. Consult with the coding experts in your facility for guidance. (Both clinics should share the same team lists and the team lists will be processes as if there were only one clinic.)

Make a copy of it for each clinic you are setting up

#### #### Anticoagulation Management Clinic Parameter Worksheet:

| Parameter                                | Value (Clinic) |
|------------------------------------------|----------------|
| Clinic Name                              |                |
| Anticoagulation Team (All)               |                |
| Anticoagulation Team (Complex)           |                |
| Address Line 1                           |                |
| Address Line 2                           |                |
| Address Line 3                           |                |
| Clinic Phone Number                      |                |
| Clinic FAX Number                        |                |
| Toll Free Phone Number                   |                |
| Point of Contact Name                    |                |
| Signature Block Name or Clinic           |                |
| Signature Block Title                    |                |
| Consult Link Enabled (Y or N)            |                |
| Consult Request Service Name             |                |
| PCE Link Enabled (Y or N)                |                |
| Automatic Indication for Care (ICD9)     |                |
| Simple Phone Visit (CPT)                 |                |
| Complex Phone Visit (CPT)                |                |
| Letter To Patient (CPT)                  |                |
| Orientation Class (CPT)                  |                |
| Initial Office Visit (CPT)               |                |
| Subsequent Visit (CPT)                   |                |
| Anticoagulation VISIT Clinic Location    |                |
| Anticoagulation PHONE Clinic Location    |                |
| Anticoagulation NON-COUNT Clinic         |                |
| Default Pill Strength                    |                |
| Include Time with Next INR Date (Y or 0) |                |
| Look-back Days for Appointment Matching  |                |
| Look-ahead Days for Appointment Matching |                |

This is a screen capture of the clinic parameter setup:

Select GUI Parameters Option: COAG GUI Anticoagulation Parameters

D Division-wide Anticoagulation Parameters

C Anticoagulation Clinic Parameters

Select GUI Anticoagulation Parameters Option: C Anticoagulation Clinic Parameters

Select CLINIC: SLC - ANTICOAGULATION CPRSPROVIDER,SEVEN 

Anticoagulation Clinic Params for Location: SLC - ANTICOAGULATION

------------------------------------------------------------------------------

Clinic Name

Anticoagulation Team (All)

Anticoagulation Team (Complex)

Address Line 1

Address Line 2

Address Line 3

Clinic Phone Number

Clinic FAX Number

Toll Free Phone Number

Point of Contact Name

Signature Block Name or Clinic

Signature Block Title

Consult Link Enabled

Consult Request Service Name

PCE Link Enabled 

Automatic Indication for Care

Simple Phone Visit (CPT)

Complex Phone Visit (CPT)

Letter To Patient (CPT)

Orientation Class (CPT)

Initial Office Visit (CPT)

Subsequent Visit (CPT)

Anticoagulation VISIT Clinic Location

Anticoagulation PHONE Clinic Location

Anticoagulation NON-COUNT Clinic

Default Pill Strength

Include Time with Next INR Date

Look-back Days for Appointment Matching

Look-ahead Days for Appointment Matching

------------------------------------------------------------------------------

Clinic Name: SLC - Anticoagulation

Anticoagulation Team (All): SLC – Anticoagulation Replace \<Enter\>

Anticoagulation Team (Complex): SLC

1 SLC-ANTICOAGULATION (ALL)

2 SLC-ANTICOAGULATION (COMPLEX)

CHOOSE 1-2: 2 SLC-ANTICOAGULATION (COMPLEX) SLC-ANTICOAGULATION (COMPLEX)

Address Line 1: George E. Wahlen VA Medical Center

Address Line 2: 500 Foothill Drive

Address Line 3: Salt Lake City, UT 84148

Clinic Phone Number: (801)582-1565x2222

Clinic FAX Number: (801)582-1566

Toll Free Phone Number: 1-(800)613-4012

Point of Contact Name: SLC Anticoagulation Clinic

Signature Block Name or Clinic: Clinical Pharmacist

Signature Block Title: SLC Anticoagulation Clinic

Consult Link Enabled: YES

Consult Request Service Name: ANTICOAGULATION MANAGEMENT ANTICOAGULATION

 MANAGEMENT

PCE Link Enabled: YES

Automatic Indication for Care : V85.83

Simple Phone Visit (CPT) : \<Enter\>

Complex Phone Visit (CPT) : \<Enter\>

Letter To Patient (CPT) : \<Enter\>

Orientation Class (CPT) : \<Enter\>

Initial Office Visit (CPT) : \<Enter\>

Subsequent Visit (CPT) : \<Enter\>  

Anticoagulation VISIT Clinic Location: SLC

1 SLC - ANTICOAG (NON-COUNT) CPRSPROVIDER,SEVEN 

2 SLC - ANTICOAGULATION CPRSPROVIDER,SEVEN 

CHOOSE 1-2: 2 SLC - ANTICOAGULATION CPRSPROVIDER,SEVEN SLC - ANTICOAGULATION

CPRSPROVIDER,SEVEN 

Anticoagulation PHONE Clinic Location: SLC

1 SLC - ANTICOAG (NON-COUNT) CPRSPROVIDER,SEVEN 

2 SLC - ANTICOAGULATION CPRSPROVIDER,SEVEN 

CHOOSE 1-2: 2 SLC - ANTICOAGULATION CPRSPROVIDER,SEVEN SLC - ANTICOAGULATION

CPRSPROVIDER,SEVEN

Anticoagulation NON-COUNT Clinic: SLC

1 SLC - ANTICOAG (NON-COUNT) CPRSPROVIDER,SEVEN 

2 SLC - ANTICOAGULATION CPRSPROVIDER,SEVEN 

CHOOSE 1-2: 1 SLC - ANTICOAG (NON-COUNT) CPRSPROVIDER,SEVEN SLC - ANTICOAG (NO

N-COUNT) CPRSPROVIDER,SEVEN 

Default Pill Strength: 5

Include Time with Next INR: YES

Look-back Days for Appointment Matching: \<Enter\>

Look-ahead Days for Appointment Matching: \<Enter\>

Anticoagulation Clinic Params for Location: SLC - ANTICOAGULATION is now:

------------------------------------------------------------------------------

Clinic Name SLC - Anticoagulation

Anticoagulation Team (All) SLC-ANTICOAGULATION (ALL)

Anticoagulation Team (Complex) SLC-ANTICOAGULATION (COMPLEX)

Address Line 1 George E. Wahlen VA Medical Ce

nter

Address Line 2 500 Foothill Drive

Address Line 3 Salt Lake City, UT 84148

Clinic Phone Number (801)582-1565x2222

Clinic FAX Number  (801)582-1565x2232

Toll Free Phone Number 1-(800)613-4012

Point of Contact Name SLC Anticoagulation Clinic

Signature Block Name or Clinic Clinical Pharmacist

Signature Block Title SLC Anticoagulation Clinic

Consult Link Enabled YES

Consult Request Service Name ANTICOAGULATION MANAGEMENT

PCE Link Enabled YES

Automatic Indication for Care V58.83

Simple Phone Visit (CPT)

Complex Phone Visit (CPT)

Letter To Patient (CPT)

Orientation Class (CPT)

Initial Office Visit (CPT)

Subsequent Visit (CPT)

Anticoagulation VISIT Clinic Location SLC - ANTICOAGULATION

Anticoagulation PHONE Clinic Location SLC - ANTICOAGULATION

Anticoagulation NON-COUNT Clinic SLC - ANTICOAG (NON-COUNT)

Default Pill Strength 5

Include Time with Next INR Date Time of Day

Look-back Days for Appointment Matching

Look-ahead Days for Appointment Matching

------------------------------------------------------------------------------

Enter RETURN to continue or '^' to exit:

D Division-wide Anticoagulation Parameters

C Anticoagulation Clinic Parameters

Select GUI Anticoagulation Parameters Option:

### Set up Tools Menu Option for Anticoagulation Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

First, the Anticoagulate.exe file to a reasonable location in your Windows directory structure (e.g., C:\Program Files\VistA\CPRS\\)

or a network location (e.g., \\vhaislmul2\Anticoagulate). This is a local a decision and placement on a network location may increase response times due to network traffic.

Next, use the GUI Tool Menu Items \[ORW TOOL MENU ITEMS\] option to create a link to the Executable for specific users who need to access the Anticoagulation Management application:

Select GUI Parameters Option: TM GUI Tool Menu Items

CPRS GUI Tools Menu may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.5 Service SRV \[choose from SERVICE/SECTION\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[CPRS27.FO-SLC.<span class="mark">REDACTED</span>\]

Enter selection: 1 User NEW PERSON

Select NEW PERSON NAME: CPRSPROVIDER,SIX CPRSPROVIDER,SIX CHIEF, MEDICAL

SERVICE

------------ Setting CPRS GUI Tools Menu for User: IRMWORKER,TWO -------------

Select Sequence: 1

Are you adding 1 as a new Sequence? Yes// YES

Sequence: 1// \<Enter\> 1

Name=Command: &Anticoagulation=c:\progra~1\vista\cprs\anticoagulate.exe s=%SRV

p=%PORT d=%DFN u=%DUZ

Select Sequence: \<Enter\>

Remember, access to this application for specific users is controlled by assigning the option ORAM ANTICOAGULATION CONTEXT to the secondary menu or menu tree of the assigned users.

> **NOTE:** *It is important to not only install the M portion of this application, but provide for execution of the Windows component. The VA does not use a setup program to do this. Each local VA facility has their own procedures for handling GUI application distribution. It is important that you utilize this procedure to get the executable into appropriate hands.*

### Set Daily Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Run ORAM SET TEAMS

Team lists are created daily by a task job (option: ORAM SET TEAMS) that needs to be set to run every morning prior to the start of the work day. Local site needs to set this. No team lists forms if this does not run.

To set this up use the option Schedule/Unschedule Options \[XUTM SCHEDULE\] in the Taskman Management \[XUTM MGR\] menu as in this example:

Select Taskman Management Option: SCHEDULE/UNSCHEDULE OPTIONS

Select OPTION to schedule or reschedule: ORAM SET TEAMS Anticoagulation Background Job

Are you adding 'ORAM SET TEAMS' as a new OPTION SCHEDULING (the 134TH)? No// Y (Yes)

Edit Option Schedule

<u>Option Name</u>: ORAM SET TEAMS

Menu Text: Anticoagulation Background Job TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: FEB 13,2010@01:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1d

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Team Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PROBLEM: Patients with INRs scheduled do not show up on the team list.

SOLUTION: There are several things that can interfere with patients showing up on the team list. They are:

1.  The nightly job is not running. The nightly job finds each patient scheduled for an INR the next day and places them on either the ALL team list or the COMPLEX team list. Patients stay on the team list until explicitly removed by the tool.
2.  You’ve set as your default Patient List the Clinic and not the Team. Often there are clinics with identical names as the teams. In the CPRS Patient Selection dialog, select the radio button next to Team/Personal, then select the correct team name. Click the Save Patient List Settings to make this selection permanent.

### Lab Quick Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PROBLEM: Lab tests missing some parameters.

While using a quick order in the Anticoagulation Management Tool (AMT), not all the order parameters are being filled out correctly. For example, if a quick order does not have the URGENCY populated, an error occurs when VistA tries to process the order.

SOLUTION: Develop quick *orders as completely as possible* for use in conjunction with this AMT application. This may entail building a unique quick order that will only be used by the Anticoagulation application.

Ordering a lab test is triggered by checking a box. There is no prompt to change any order parameters after this, and there really doesn’t need to be a prompt if the order is built as needed. Be sure to populate all fields with values appropriate for the clinic that will use them.

## Appendix A: Alternate Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Team Lists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Overview

The Anticoagulation Management Tool (AMT) was designed with certain assumptions about the best way to do things. Unfortunately, not every medical center is run the same way. Here are some of the main assumptions used in putting together this tool:

1.  Most contacts through the Anticoagulation Clinic correspond to a lab order. The visits are brief and often conducted over the telephone. So, appointments are set according to the timing of lab orders, not with the VistA Scheduling application.
2.  It is essential that patients not be lost from the system, so AMT uses two mechanisms to keep this from happening:
    1.  All patients are put on a team list corresponding to their lab appointment. The patient persists on the team list until a visit has been achieved.
    2.  Missed visits are always followed up with a reminder letter to the patient.
3.  Dosing schedules are easy to mess up. So, the tool does several things to simplify dosing:
    1.  Patients are given one strength of pill. The pill strength is kept track of in the tool.
    2.  Any change in dosing schedule is followed up with a letter to the patient, thus the patient always has written instructions.
4.  Most pertinent patient information is kept in the tool for easy access and reference. Progress notes are only used for initial and final visits.

The requirement is that each VA medical facility that dispenses anticoagulation drugs (specifically Warfarin) have a method in place to track patients on these drugs. You do not have to use the VistA Anticoagulation Management Tool to accomplish this, but you must have something as comprehensive as this tool. This tool does not fit perfectly into every business model, but it can be adapted.

Here are some ways AMT can be adapted to local conditions:

#### Multiple Anticoagulation Clinics

Some medical centers with multiple anticoagulation clinics don’t consider the team list approach to be comprehensive enough. They schedule all patients in to their clinics with the VistA Scheduling application. They can then use the reporting features of scheduling to print out Microsoft Excel® spreadsheets of the schedules. This gives a high degree of confidence that clinicians and patients are not being double booked and provides a visual overview of each day’s schedule.

#### Scheduling

Some clinics use scheduling because they have more confidence in the scheduling application to help manage appointments, because they need better control over workflow reporting, or because medical center policy dictates that they do. To use scheduling with the Anticoagulation Management Tool (AMT) you must go back and forth between the tool and CPRS. Also, you must take care to keep CPRS on the same patient as in AMT.

When the scheduling package is the main tool for tracking schedules, AMT is still useful to template interview questions, format progress notes, track INRs, and compare no-shows between the tool and the scheduling package. Most important, the tool tracks and displays all INRs throughout the time the patient is in the program, regardless of who ordered the INR or who the patient met with.

### Clinic Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you set up clinic parameters some of the values are inherited from the division. The relationship of division and clinic varies from institution to institution. Here is a representation of some of the possibilities:

![](anticoagulation-management-tool-installation-implementation-guide/002.png)

Case 1 is the default where there is only one clinic assigned to one division. In this case setting parameters for the division and clinic are sufficient. See the [Set Parameters](#set-parameters) section of this manual.

Case 2 is what one would expect in a medical center with several Community Based Outpatient Clinics (CBOCs). In this case you must set parameters for the division and for each of the clinics under it. Any parameters that are missing from the clinic setup are filled in from the corresponding parameter at the division level.

Case 3 is as common as case 2 for integrated medical centers. Before you set up a clinic you need to know what division it is assigned to. Information about clinic division assignments is available from your Medical Administration Systems (MAS) sometimes referred to as Patient Information Management System (PIMS) or Hospital Information Management System (HIMS).

However, your medical center is organized you need to set up both the clinic and the division as in the Set Parameters section of this manual.