---
title: ARCH Version 2.1 Installation and User Guide I2
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: Installation and  I2
app_code: FB
app_name: Fee Basis
section: FIN
app_status: active
pkg_ns: FB
patch_ver: 2.1
patch_id: FB*2.1
group_key: "FB:FB:2.1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - arch
  - project
  - installation
  - eligibility
  - table
  - contents
  - eligible
  - patients
  - dataset
  - install
page_count: 0
word_count: 956
section_count: 3
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2011
revision_count: 2
revision_newest: 12/02/2011
revision_oldest: 09/16/2011
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/arc_iug2.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/arc_iug2.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=40"
---

> ![](arch-version-2-1-installation-and-user-guide-i2/001.png)

> Enhancing the Veteran Experience and Access to Healthcare (EVEAH) Initiative

> Access Received Closer to Home (ARCH) Version 2.1

> Installation and User Guide

![](arch-version-2-1-installation-and-user-guide-i2/002.png)

> November 2011

> Revision History

| Date   | Version | Description               | Author           |
|------------|-------------|-------------------------------|----------------------|
| 09/16/2011 | 2.0         | Increment 2 - Initial Draft   | Halfaker/Harris Team |
| 12/02/2011 | 2.1         | Updates based on code changes | Halfaker/Harris Team |
|            |             |                               |                      |

1.  
2.  
3.  
4.  
5.  1.  
    2.  

[Introduction 1](#introduction)[Pre-Installation 2](#pre-installation)[Installation 3](#installation)[Post-Installation 4](#post-installation)[User Guide 5](#user-guide)[Adding/Editing Project ARCH Eligibility 6](#addingediting-project-arch-eligibility)[Viewing Project ARCH Eligibility 7](#viewing-project-arch-eligibility)

> [Attachment A: Installation Example ................................................................ A-1](#attachment-a-installation-example)

> [Attachment B: Release Notes ..............................................................................B-1](#_bookmark14)

> [Attachment C: Acronyms................................................................................... C-1](#_bookmark15)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pre-Installation](#pre-installation)
    - [Required Software for FB\3.5\119](#required-software-for-fb35119)
- [Installation](#installation)
    - [Pre-Installation Instructions](#pre-installation-instructions)
- [Post-Installation](#post-installation)
- [User Guide](#user-guide)
  - [Adding/Editing Project ARCH Eligibility](#addingediting-project-arch-eligibility)
  - [Viewing Project ARCH Eligibility](#viewing-project-arch-eligibility)
- [Attachment A: Installation Example](#attachment-a-installation-example)
> The Veterans' Mental Health And Other Care Improvements Act Of 2008, Section 403, Public Law 110-387 mandates that the Department of Veterans Affairs (VA) conduct a pilot program over three years for contract care of eligible Veterans in selected Veterans Integrated
> Service Networks (VISNs).
> The Office of Policy Analysis within the Office of the Assistant Deputy Under Secretary for Health for Policy and Planning (ADUSH/PP) requested the capability to automatically identify all Veterans who are eligible for a high visibility Congressionally mandated contract care pilot program (named Project ARCH, Access Received Closer to Home) in five VISNs (1, 6, 15, 18, and 19).
> Patch FB\*3.5\*130 contains Project ARCH enhancements, which allow for authorized users that hold the FB ARCH Security Key to identify patients that were not included in the original Project ARCH Increment 1 eligibility dataset and allow them to be marked as being Project ARCH eligible in the local VistA system. The system now allows locally added patients to be marked Not Project ARCH eligible by users that hold the FB ARCH Security Key. This patch also includes a "View Project ARCH Eligibility" option that allows authorized users to view nationally and locally identified Project ARCH patients.
> Complete list of patch items:
1.  Project ARCH Menu is now included in Fee Basis Main Menu and is accessible by users who hold the FB ARCH security key.
2.  Users are restricted from editing Project ARCH Eligibility status for patients that have been determined to be Project ARCH eligible through the National Eligibility Dataset.
3.  System requires a justification for patients that have been locally determined Project ARCH eligible before adding them to the local dataset. Justification is selected from a provided list of reasons.
4.  System requires the user to enter the Verification of mileage for patients that have been locally determined Project ARCH eligible before adding them to the local dataset.
5.  The "View Project ARCH Eligibility" option allows authorized users the ability to sort Project ARCH Eligibility data in different views. This option also allows users to view data for either a specific patient or all Project ARCH eligible patients and to limit the data to a certain date range. Users can search for entries where the most current Project ARCH Eligibility entry matches the selected status (Eligible / Not Eligible / Both).
6.  System allows the user the ability to queue the output of the "View Project ARCH Eligibility" option to run in the background, print to a specific device, or print to Excel formatted text.

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Required Software for FB\*3.5\*119

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Package/Patch | Namespace | Version | Comments  |
|-------------------|---------------|-------------|---------------|
| Fee Basis         | FB            | 3.5         | Fully patched |

> Estimated Installation Time: Less than 5 minutes

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes how to install the patch FB\*3.5\*130.

> This patch may be installed with users on the system, although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

### Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

7.  Choose the PackMan message containing this patch.
8.  Choose the INSTALL/CHECK MESSAGE PackMan option.
9.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may select following options. When prompted for the INSTALL enter the patch FB\*3.5\*130:
    1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
    3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
10. From the Installation Menu, select the Install Package(s) option and choose the patch to install.
11. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//' Answer YES, unless your system does this in a nightly TaskMan process.
12. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' Answer NO.
13. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' Answer NO.
14. If prompted ‘Delay Install (Minutes): (0 - 60): 0// respond 0.

> This installation has no impact on disc space or journal file consumption.

# Post-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Upon completion of the patch install, the Project ARCH Care Coordinator or designee will need to have the FB ARCH Security Key assigned to them[<sup>1</sup>](#_bookmark4). This Security Key will allow access to the new menu options distributed in this patch under the Fee Basis Main Menu \[FBAA MAIN MENU\].

> The second line of each of these routines now looks like:

> ;;3.5;FEE BASIS;\*\*\[Patch List\]\*\*;JAN 30, 1995;Build 5

> The checksums below are new checksums, and can be checked with CHECK1^XTSUMBLD.

> Routine Name: FBARCH0

> Before: 51716371 After: 51834191 \*\*119,130\*\* Routine Name: FBARCHR0

> Before: n/a After: 122985826 \*\*130\*\* Routine Name: FBARCHU

> Before: n/a After: 24246185 \*\*130\*\* Routine Name: FBY130PO

> Before: n/a After: B5536715 \*\*130\*\*

> FBY130PO is a post install routine that changes previously installed justification reasons to the official justification reasons. If no justification reasons were previously installed by a test version FB\*3.5\*130 patch then the post install routine will quit with no further action. Once it executes, it is deleted by KIDS.

> <span id="_bookmark4" class="anchor"></span><sup>1</sup> The Security Key is added to a user or set of users by the Fee Basis administrator. When the administrator logs in, there is a system level menu which is used for a number of things like installing a patch, mail, adding users and managing a number of security keys. This menu level is Fee Basis-based and is *not* Project ARCH-based. The Fee Basis Administrator Guide will provide further instruction as to how a user can make a request to obtain a Security Key.

# User Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Increment 2 of Project ARCH is accessed using Fee Basis. In addition to a login for Fee Basis, the user must hold the FB ARCH Security Key in order to access any of the features of manualy adding or viewing Project ARCH Eligibility.

> The Project ARCH Main Menu is selected from the Fee Basis Menu as shown in Figure 1.

> ![](arch-version-2-1-installation-and-user-guide-i2/003.png)Figure 1: Accessing Project ARCH from the Fee Basis Menu

> When the Project ARCH Menu is selected, the Project ARCH Main Menu is displayed. At the prompt, the user can Add or Edit Project ARCH Eligibility or View Project ARCH Eligibility which is shown in Figure 2.

> Figure 2: Project ARCH Main Menu

> ![](arch-version-2-1-installation-and-user-guide-i2/004.png)

## Adding/Editing Project ARCH Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When ‘AD’ is entered at the Project ARCH Main Menu, the user is prompted for the name of a patient. Depending on the status of the patient who is selected, one of the following three responses is displayed:

- If the patient is not currently Project ARCH eligible, the “Change to Project ARCH eligible?” prompt is displayed.
- If the patient has been manually made Project ARCH eligible, the “Change to NOT Project ARCH eligible?” prompt is displayed.
- If the patient was made Project ARCH eligible during the extract of the National Project ARCH Eligibility Dataset, “This patient was determined Project ARCH eligible by the SAS database extract and cannot be edited.” message is displayed.

> When adding Project ARCH Eligibility for a patient, a Justification Reason needs to be selected from the list of justifications shown in Figure 3. Once the justification is selected, a “Verification of Mileage:” prompt is displayed. The Verification of Mileage field allows the user to type up to 100 characters, and is meant to provide a description as to how the mileage portion of Project ARCH eligibility was manually determined. The system then confirms the Project ARCH Eligibility by displaying the patient’s name is Project ARCH eligible.

> Figure 3: Adding Project ARCH Eligibility

> ![](arch-version-2-1-installation-and-user-guide-i2/005.png)

> Project ARCH Eligibility can be removed from a patient who has had Project ARCH Eligibility added manually. Patients who have Project ARCH Eligibility added from the National Project ARCH Eligibility Dataset update cannot have Project ARCH Eligibility removed manually.

> To edit a patient, select ‘AD’ from the Project ARCH main menu. Select a patient who has had Project ARCH Eligibility added manually. Type ‘y’ to the “Change to NOT Project ARCH eligible?” question.

> The system then confirms the Project ARCH Eligibility has been removed by displaying the patient’s name is NOT Project ARCH eligible. This is shown in Figure 4.

> Figure 4: Edit Project ARCH Eligibility

> ![](arch-version-2-1-installation-and-user-guide-i2/006.png)

## Viewing Project ARCH Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When ‘VW’ is entered at the Project ARCH Main Menu, a number of choice prompts provide flexibility for a user to select one patient or a selected set of patients in a detailed or summary report.

> [Figure 5](#_bookmark8) and [Figure 6](#_bookmark9) show the different prompts that are selectable. The resulting detailed report is shown in [Figure 7.](#_bookmark10) Pressing the “Enter” key causes the default selection to be chosen. The default value for each selection causes the largest number of entries for that prompt. For example, the default selection for *One Patient* or *All Patients* causes *All Patients* to be selected. (Other choices can change the number of patients to be displayed.)

> ![](arch-version-2-1-installation-and-user-guide-i2/007.png)<span id="_bookmark8" class="anchor"></span>Figure 5: Viewing Project ARCH Eligibility

> The user is also prompted to choose whether a detailed or summary report is desired. The default selection is for a detailed report to be displayed.

> ![](arch-version-2-1-installation-and-user-guide-i2/008.png)<span id="_bookmark9" class="anchor"></span>Figure 6: Selecting the Project ARCH Eligibility Detailed Report

> <span id="_bookmark10" class="anchor"></span>Figure 7: Project ARCH Eligibility Detailed Report

> ![](arch-version-2-1-installation-and-user-guide-i2/009.png)

> One other feature of Project ARCH is that the display of the selected view of Project ARCH patients can be exported to a file that can be imported into a Microsoft Excel® document. The prompts are shown in [Figure 8](#_bookmark11) and a sample output is shown in [Figure 9.](#_bookmark12)

> ![](arch-version-2-1-installation-and-user-guide-i2/010.png)<span id="_bookmark11" class="anchor"></span>Figure 8: Exporting a Project ARCH Eligible View

> <span id="_bookmark12" class="anchor"></span>Figure 9: Exported Data File

# Attachment A: Installation Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> XPD MAIN Kernel Installation & Distribution System Edits and Distribution ...

> Utilities ...

> Document Enhancement type patches Installation ...

> Patch Monitor Main Menu ...

> Select Kernel Installation & Distribution System Option: INStallation

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> You have PENDING ALERTS

> Enter "VA to jump to VIEW ALERTS option

> Select Installation Option: 6 Install Package(s) Select INSTALL NAME: FB\*3.5\*130 8/2/11@14:14:57

> =\> FB\*3.5\*130 TEST v1

> This Distribution was loaded on Aug 02, 2011@14:14:57 with header of FB\*3.5\*130 TEST v1

> It consisted of the following Install(s): FB\*3.5\*130

> Checking Install for Package FB\*3.5\*130 Install Questions for FB\*3.5\*130 Incoming Files:

> 161 FEE BASIS PATIENT (Partial Definition) Note: You already have the 'FEE BASIS PATIENT' File.

> 161.35 FEE BASIS PROJECT ARCH JUSTIFICATION (including data) Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// TELNET TERMINAL

> ---

> Install Started for FB\*3.5\*130 :

> Aug 02, 2011@14:18:25

> Build Distribution Date: Aug 02, 2011 Installing Routines:

> Aug 02, 2011@14:18:25

> Installing Data Dictionaries:

> Aug 02, 2011@14:18:25

> Installing Data:

> Aug 02, 2011@14:18:25

> Installing PACKAGE COMPONENTS: Installing SECURITY KEY Installing OPTION

> Aug 02, 2011@14:18:26

> Updating Routine file... Updating KIDS files...

> FB\*3.5\*130 Installed.

> Aug 02, 2011@14:18:26

> Not a production UCI

> Install Completed

> <span id="_bookmark14" class="anchor"></span>Attachment B:Release Notes

> Fee Basis changes included in FB\*3.5\*130:

- Project ARCH Menu was added to the Fee Basis Main Menu and is accessible by users who hold the FB ARCH Security Key.
- System allows local Project ARCH Care Coordinator or designee to add patients to the local Project ARCH Eligibility dataset.
- Users are restricted from editing Project ARCH Eligibility status for patients that have been determined to be Project ARCH eligible through the National Eligibility Dataset.
- System requires a justification for patients that have been locally determined Project ARCH eligible before adding them to the local dataset. Justification is selected from a provided list of reasons.
- System requires the user to enter the Verification of mileage for patients that have been locally determined Project ARCH eligible before adding them to the local dataset.
- The "View Project ARCH Eligibility" option allows authorized users the ability to sort Project ARCH Eligibility data in different views. This option also allows users to view data for either a specific patient or all Project ARCH eligible patients and to limit the data to a certain date range. Users can search for entries where the most current Project ARCH Eligibility entry matches the selected status (Eligible / Not Eligible / Both).
- System allows the user the ability to queue the output of the "View Project ARCH Eligibility" option to run in the background, print to a specific device, or print to Excel formatted text.

> <span id="_bookmark15" class="anchor"></span>Attachment C:Acronyms

| Term | Definition                                                 |
|----------|----------------------------------------------------------------|
| ADUSH/PP | Under Secretary for Health for Policy and Planning             |
| ARCH     | Access Received Closer to Home                                 |
| ASU      | Authorization/Subscription Utility                             |
| CPRS     | Computerized Patient Record System                             |
| DG       | Registration and Enrollment Package namespace                  |
| ESM      | Enterprise Systems Management (ESM)                            |
| EVEAH    | Enhancing the Veteran Experience and Access to Health Care     |
| FIM      | Functional Independence Measure                                |
| GUI      | Graphic User Interface                                         |
| IAB      | Initial Assessment & Briefing                                  |
| OI       | Office of Information                                          |
| OIF/OEF  | Operation Iraqi Freedom/Operation Enduring Freedom             |
| PCS      | Patient Care Services                                          |
| PXRM     | Clinical Reminder Package namespace                            |
| RSD      | Requirements Specification Document                            |
| SD       | Scheduling Package Namespace                                   |
| VA       | Department of Veteran Affairs                                  |
| USR      | ASU package namespace                                          |
| VistA    | Veterans Health Information System and Technology Architecture |