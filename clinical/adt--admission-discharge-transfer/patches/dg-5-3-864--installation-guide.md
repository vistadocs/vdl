---
title: DG*5.3*864 USH PRF Legal Solution Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: USH PRF Legal Solution
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: archive
pkg_ns: DG
patch_ver: 5.3
patch_id: DG*5.3*864
group_key: "ADT:DG:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - flag
  - patient
  - record
  - install
  - class
  - table
  - contents
  - health
  - summary
  - span
page_count: 0
word_count: 3424
section_count: 20
table_count: 4
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2013
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/dg_5_3_864_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Record_Flags/dg_5_3_864_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=327"
---

![](dg-5-3-864-ush-prf-legal-solution-installation-guide/001.png)

USH LEGAL SOLUTION –

CATEGORY I Patient Record Flag (PRF)

Installation Guide

DG\*5.3\*864

TIU\*1\*275

GMTS\*2.7\*103

August 2013

Office of Information (OI)

Product Development

Table of Contents

1\. Introduction [1](#introduction)

2\. Pre-Installation [4](#pre-installation)

2.1. Add members to the DGPF HL7 TRANSMISSION ERRORS Mail Group [4](#add-members-to-the-dgpf-hl7-transmission-errors-mail-group)

2.2. Check local versus national conflict for HEALTH SUMMARY COMPONENT file (#142.1) entries [4](#check-local-versus-national-conflict-for-health-summary-component-file-142.1-entries)

Required Software for DG\*5.3\*864 [5](#required-software-for-dg5.3864)

Related Documentation [5](#related-documentation)

3\. Installation [6](#installation)

3.1. Retrieve the host file [6](#_Toc365355241)

3.2. Install the patch first in a training or test account. [6](#install-the-patch-first-in-a-training-or-test-account.)

3.3. Load the distribution. [6](#load-the-distribution.)

a\. *Backup a Transport Global* [6](#backup-a-transport-global)

b\. *Compare Transport Global to Current System* [6](#compare-transport-global-to-current-system)

c\. *Verify Checksums in Transport Global* [7](#verify-checksums-in-transport-global)

3.4. Install the Build. [7](#install-the-build.)

3.5. Install File Print [8](#install-file-print)

3.6. Build File Print [8](#build-file-print)

3.7. Post-installation routines [8](#post-installation-routines)

4\. Post-Install Set-up Instructions [10](#post-install-set-up-instructions)

4.1. Check for errors and monitor PRF HL7 messaging

4.2. Verify that the new URGENT ADDRESS AS FEMALE Category I flag was added to the National Flag List. [10](#verify-that-the-new-urgent-address-as-female-category-i-flag-was-added-to-the-national-flag-list.)

4.3. Verify that the TIU Document Definition for the new Progress Note Title was added . [11](#verify-that-the-tiu-document-definition-for-the-new-progress-note-title-was-added-by-the-tiu1.0275-patch.)

4.4. Assign Clinician to the new User Class [12](#assign-clinician-to-the-new-dgpf-patient-record-flags-mgr-user-class)

4.5. Clinician’s note linked to NEW ASSIGNMENT action after assignment. [13](#clinicians-note-linked-to-new-assignment-action-after-assignment.)

4.6. Add Health Summary Types to the list of available reports in CPRS. [14](#add-health-summary-types-to-the-list-of-available-reports-in-cprs.)

4.8 ONE SITE ONLY: Add flag for patient. [16](#one-site-only-add-flag-for-patient.)

Appendix A: Installation Capture [17](#appendix-a-installation-capture)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Pre-Installation](#pre-installation)
  - [Add members to the DGPF HL7 TRANSMISSION ERRORS Mail Group](#add-members-to-the-dgpf-hl7-transmission-errors-mail-group)
  - [Check local versus national conflict for HEALTH SUMMARY COMPONENT file (#142.1) entries](#check-local-versus-national-conflict-for-health-summary-component-file-1421-entries)
- [Installation](#installation)
  - [> <span class="mark">Sites redacted</span>](#span-classmarksites-redactedspan)
  - [Install the patch first in a training or test account.](#install-the-patch-first-in-a-training-or-test-account)
  - [Load the distribution.](#load-the-distribution)
  - [Backup a Transport Global](#backup-a-transport-global)
  - [Compare Transport Global to Current System](#compare-transport-global-to-current-system)
  - [Verify Checksums in Transport Global](#verify-checksums-in-transport-global)
  - [## Install the Build.](#install-the-build)
  - [Install File Print](#install-file-print)
  - [Build File Print](#build-file-print)
  - [Post-installation routines](#post-installation-routines)
- [Post-Install Set-up Instructions](#post-install-set-up-instructions)
  - [Check for errors and monitor PRF HL7 messaging for increase in activity.](#check-for-errors-and-monitor-prf-hl7-messaging-for-increase-in-activity)
  - [Verify that the new URGENT ADDRESS AS FEMALE Category I flag was added to the National Flag List.](#verify-that-the-new-urgent-address-as-female-category-i-flag-was-added-to-the-national-flag-list)
  - [Verify that the TIU Document Definition for the new Progress Note Title was added by the TIU\1.0\275 patch.](#verify-that-the-tiu-document-definition-for-the-new-progress-note-title-was-added-by-the-tiu10275-patch)
  - [Assign Clinician to the new DGPF PATIENT RECORD FLAGS MGR User Class](#assign-clinician-to-the-new-dgpf-patient-record-flags-mgr-user-class)
  - [## Clinician’s note linked to NEW ASSIGNMENT action after assignment.](#clinicians-note-linked-to-new-assignment-action-after-assignment)
  - [Add Health Summary Types to the list of available reports in CPRS.](#add-health-summary-types-to-the-list-of-available-reports-in-cprs)
  - [ONE SITE ONLY: Add flag for patient.](#one-site-only-add-flag-for-patient)
- [# Appendix A: Installation Capture](#appendix-a-installation-capture)
Patches TIU\*1.0\*275, DG\*5.3\*864, and GMTS\*2.7\*103 address the Under Secretary of Health’s (USH) legal solution to provide a new national Category I patient record flag that will inform all Veteran Health Administration (VHA) caregivers of special guidelines that must be followed when documenting notes or dealing with a specific patient. This flag will require special permissions in order to be assigned to a patient and, once assigned, it cannot be modified or inactivated other than allowing the reassignment of the owning facility.
This new Patient Record Flag project consists of a build containing three patches, as described below.
- Patch TIU\*1\*275 installs one new Progress Note Title into the TIU DOCUMENT DEFINITION file (8925.1): PATIENT RECORD FLAG CATEGORY I – URGENT ADDRESS AS FEMALE. The patch installation links the title to the existing document class, PATIENT RECORD FLAG CAT I. This title will be automatically linked to the URGENT ADDRESS AS FEMALE Patient Record Flag during the install of DG\*5.3\*864.
- Patch DG\*5.3\*864 installs a new national Category I patient record flag: URGENT ADDRESS AS FEMALE PRF and associates the new PATIENT RECORD FLAG CATEGORY I – URGENT ADDRESS AS FEMALE progress note title with the new flag.
> This Patient Record Flag was established to ensure that a transgender Veteran is addressed as Female per a court order agreement. This flag cannot be used without approval of the Under Secretary for Health.
> The ability to assign the new URGENT ADDRESS AS FEMALE PRF will be limited to one identified IRM staff member with programmer access, or an identified clinician with temporary programmer access assigned by IRM staff at one pre-determined site. The identified person with programmer access at the pre-determined site will assign the URGENT ADDRESS AS FEMALE PRF to a pre-determined patient, identified by Under Secretary of Health (USH). The text used during the assignment will be based on very specific pre-defined text provided by the Office of the Under Secretary of Health.
> Once the USH specified patient is assigned the URGENT ADDRESS AS FEMALE flag, the PRF cannot be inactivated for the patient. NOTE: Only one site will be assigning this flag to the patient. There will be no Review frequency for this flag assignment.
> The patch also includes a change to the Register a Patient \[DG REGISTER PATIENT\] option and the Load/Edit Patient Data \[DG LOAD PATIENT DATA\] option to ensure Category I Patient Record Flags are updated when a patient registers at a new facility. The updates are provided from the existing VistA treating facility where the patient has been seen. This change is required to address a Patient Safety Issue (PSPO \#2365) and Remedy Ticket \#801785 – Category I Flag.
Patient Safety Issues (PSIs)
---------------------------
PSPO \#2365 - During testing of new software it was found when a patient
registers at a new facility the backward look-up to determine if a
Category I Record Flag exists for that patient at any other facility does
not function correctly.
- Patch GMTS\*2.7\*103 provides two new Health Summary Types: VA-PT RECORD FLAG STATUS for local display of active and inactive patient record flags and REMOTE PT RECORD FLAG STATUS for use from Remote Data Views to see another treating facilities active and inactive patient record flags. Both of these Health Summary Types include a new Health Summary Component, CAT I PT RECORD FLAG STATUS, that displays the active and inactive Category I Patient Record Flags assigned to a given patient.
HEALTH SUMMARY TYPE (#142)
NAME: <span class="mark">VA-PT RECORD FLAG STATUS</span>
LOCK: GMTSMGR
SUMMARY ORDER: 5
COMPONENT NAME: CAT I PT RECORD FLAG STATUS
NATIONALLY EXPORTED TYPE: Nationally Exported, Uneditable
NAME: <span class="mark">REMOTE PT RECORD FLAG STATUS</span>
LOCK: GMTSMGR
SUMMARY ORDER: 5
COMPONENT NAME: CAT I PT RECORD FLAG STATUS
NATIONALLY EXPORTED TYPE: Nationally Exported, Uneditable
HEALTH SUMMARY COMPONENT (#142.1)
NUMBER: 257 NAME: <span class="mark">CAT I PT RECORD FLAG STATUS</span>
PRINT ROUTINE: EN;GMTSRFHX ABBREVIATION: <span class="mark">PRF1</span>
DESCRIPTION: This component displays the Active and Inactive Category 1
Patient Record Flags assigned to a given patient. The full assignment
history is included with each instance of flag assignment. Active flag
assignments are displayed first, followed by Inactive flag assignments.
> **NOTE:** MPIF\*1\*58, a related patch, is not part of the bundle described in this Install Guide, but will need to be installed concurrently. A code change has been made in routine MPIFBT3 to support the Patient Record Flag initiative distributed in VistA patch DG\*5.3\*864.
For some time, the Register a Patient \[DG REGISTER PATIENT\] and Load/Edit Patient Data \[DG LOAD PATIENT DATA\] options have included the query for the Patient Record Flag. However, when a patient is created outside of these options, the query for the Patient Record Flag was not occurring.
Also, if a patient does not get an Integration Control Number (ICN) via the direct connect to the Master Veteran Index during registration, that record gets a local ICN.  The local ICN is resolved to a national ICN  through the Local/Missing ICN Resolution Background Job \[MPIF LOC/MIS
ICN RES\] option.
 The Local/Missing ICN Resolution Background Job \[MPIF LOC/MIS ICN RES\] now includes the query for the Patient Record Flag once the ICN has been returned to VistA and the patient is shared with another VAMC.
> NOTE: After all sites have completed the install, one site will be instructed, by the Office of Under Secretary for Health, to add the URGENT    ADDRESS AS FEMALE flag for a specified patient.  Any site that has treated this patient will be updated automatically by the patient record flag software after the flag is added for the patient.  New sites registering the patient will either be updated during the Registration process or by the Master Patient Index process that updates the patient’s  national ICN and treating facility list.      
Remedy Ticket
INC000000801785 - Category I Flag
The automatic update (a routine unseen by users) of the Category I Flag to the new facility, the patient is registering at does not work correctly. Corrections will be made to the Patient Record Flag routines, addressed in patch DG\*5.3\*864.
Test Sites:
<span class="mark">Test sites redacted</span>

# Pre-Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Add members to the DGPF HL7 TRANSMISSION ERRORS Mail Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Mail Group Coordinator for the DGPF HL7 TRANSMISSION ERRORS Mail Group will need to add members to this Mail Group. It is recommended that this flag be assigned to IRM staff (installing this software), Clinical Application Coordinator for Patient Record Flag software, HIMS flag coordinator(s)/representative and Suicide Prevention Coordinator(s)/ representment as members.

> Due to the logic change in registration and load/edit of patient data, there will be an increase in the amount of messaging that will occur between sites to update the Category I flags for a newly registered patient at your site.

## Check local versus national conflict for HEALTH SUMMARY COMPONENT file (#142.1) entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Prior to installing the patch, examine the HEALTH SUMMARY COMPONENT file

> (#142.1) for any NUMBER (.001), NAME (.01), or ABBREVIATION (3) entries that will conflict with the new component exported with this patch. The national component NUMBER, NAME, and ABBREVIATION are as follows:

> NUMBER (IEN) NAME ABBREVIATION

> 257 CAT I PT RECORD FLAG STATUS PRF1

> Internal Entry Numbers below 100001 are reserved for National health summary components. It is extremely unlikely that your site will have a component stored at IEN 257, as doing so would require programmer access and manual editing of the ^GMR(142.1 global. To check the global on your system, look at ^GMT(142.1,257. That location should be empty. If not, your site will need to submit a Remedy ticket for Health Summary support to assist in cleaning up that global entry. Before submitting the ticket, if the component is actually in use at your site and should be kept, it can be recreated as a local IEN and with a slightly different name. Use the “Create/Modify Health Summary Components” option of the GMTS IRM MAINTENANCE MENU to recreate the component. After recreating the component, submit the Remedy ticket requesting Health Summary support with locating any items pointing to IEN 257, have those items re-pointed to the new local component location, and cleaning up the unwanted entry at IEN 257.

> The "B" cross-reference for the HEALTH SUMMARY COMPONENT file (#142.1),

> \[^GMR(142.1,"B",\], contains the NAME for each component. Each component entry in the file must have a unique NAME. Examine the global listing for this cross-reference to determine if any local component will need the NAME field edited to avoid collision with the new national component.

> ^GMT(142.1,"B","CAT I PT RECORD FLAG STATUS",660187)="" \<-Example of a

> local component that will conflict with the incoming CAT I PT RECORD FLAG STATUS component NAME.

> The "C" cross-reference for the HEALTH SUMMARY COMPONENT file (#142.1),

> \[^GMR(142.1,"C",\], contains the ABBREVIATION for each component. Each component entry in the file must have a unique ABBREVIATION. Examine the

> global listing for this cross-reference to determine if any local components will need the ABBREVATION field edited to avoid collision with the new national component.

> ^GMT(142.1,"C","PRF1",660187="" \<-Example of a local component that will conflict with the incoming CAT I PT RECORD FLAG STATUS component ABBREVIATION.

> If a NAME or ABBREVIATION conflict is found, the “Create/Modify Health Summary Components" option of the GMTS IRM MAINTENANCE MENU should be used to edit the local component's NAME or ABBREVIATION.

#### Required Software for DG\*5.3\*864

|                                  |           |         |               |
|----------------------------------|-----------|---------|---------------|
| Package/Patch                    | Namespace | Version | Comments      |
| Health Summary                   | GMTS      | 2.7     | Fully patched |
| Kernel                           | XU        | 8.0     | Fully patched |
| Registration/Patient Record Flag | DG        | 5.3     | Fully patched |
| VA FileMan                       | DI        | 22      | Fully patched |
| Master Patient Index Veteran     | MPIF      | 1       | MPIF\*1\*58   |

#### Related Documentation

|                                                                              |                         |
|------------------------------------------------------------------------------|-------------------------|
| Documentation                                                                | Documentation File name |
| USH LEGAL SOLUTION – CATEGORY I Patient Record Flag (PRF) Installation Guide | DG_5.3_864_IG.PDF       |
| USH LEGAL SOLUTION – CATEGORY I Patient Record Flag (PRF) Release Notes      | DG_5.3_864_RN.PDF       |
| Patient Record Flag (PRF) User Guide                                         | PatRecFlagUG.PDF        |
| Health Summary User Manual                                                   | HSUM2_7_103_UM.PDF      |
| Health Summary Technical Manual                                              | HSUM2_7_103_TM.PDF      |
| TIU User Manual                                                              | TIUUM-275.PDF           |

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes*The installation needs to be done by a person with DUZ (0) set to "@."*

## > <span class="mark">Sites redacted</span>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The name of the host file is USH_PRF_LEGAL_SOLUTION_1_0.KID.

## Install the patch first in a training or test account. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installing in a non-production environment will give you time to get familiar with new restrictions on entering the new URGENT ADDRESS AS FEMALE flag using the DGPF RECORD FLAG MANAGEMENT and DGPF FLAG ASSIGNMENT options. *<u>Once in production, only one site will actually be tasked to assign the new flag to one specific patient.</u>* There will be no impact on patient record flag functionality for other Category I flags.

## Load the distribution. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In programmer mode, type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name.KID at the Host File prompt.

Example

Select Installation Option: LOAD a Distribution

Enter a Host File: DIR\$:\[LOCALDIR\]USH PRF LEGAL SOLUTION 1.0.KID

KIDS Distribution saved on

From the Installation menu, you may elect to use the following options:

## *Backup a Transport Global* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

## *Compare Transport Global to Current System*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

## *Verify Checksums in Transport Global* 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option will allow you to ensure the integrity of the routines that are in the transport global. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Retrieve the file again from the anonymous directory (in case there was corruption in Ftp’ing) and Load the Distribution again. If the problem still exists, log a Remedy ticket and/or call the national Help Desk (1-888-596-HELP) to report the problem.

Select INSTALL NAME: USH PRF LEGAL SOLUTION 1.0

Want each Routine Listed with Checksums: Yes// YES

DEVICE: HOME// VIRTUAL TELNET

-------------------------------------------------------------------------------

TIUPS275 Calculated 9548345

1 Routine checked, 0 failed.

PACKAGE: DG\*5.3\*864 Aug 27, 2013 9:17 am PAGE 1

-------------------------------------------------------------------------------

DG10 Calculated 19615369

DG53864P Calculated 6717089

DGPFLMA2 Calculated 58607996

DGPFMPI Calculated 2049737

DGREG Calculated 47583853

6 Routines checked, 0 failed.

PACKAGE: GMTS\*2.7\*103 Aug 27, 2013 9:17 am PAGE 1

-------------------------------------------------------------------------------

GMTSRFHX Calculated 19895758

GMTSY103 Calculated 35203734

2 Routines checked, 0 failed.

## ## Install the Build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM\*2.0\*27 and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

Select Installation & Distribution System Option: Installation

Select Installation Option: INSTALL PACKAGE(S)

Select INSTALL NAME: DIR\$:\[LOCALDIR\]USH PRF LEGAL SOLUTION 1.0

> Answer "NO" to the following prompt:

Want KIDS to INHIBIT LOGONs during install? NO// NO

> NOTE:DO NOT QUEUE THE INSTALLATION, because this installation asks questions requiring responses and queuing will stop the installation. A Clinical Application Coordinator (CAC) should be present to respond to these.

> Installation Example: See [Appendix A](\l).

## Install File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

Select Utilities Option: Install File Print

Select INSTALL NAME: DIR\$:\[LOCALDIR\]USH PRF LEGAL SOLUTION 1.0

## Build File Print 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the KIDS Build File Print option to print out the build components.

Select Utilities Option: Build File Print

Select BUILD NAME: USH PRF LEGAL SOLUTION 1.0

DEVICE: HOME//

## Post-installation routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A post-installation routine for the DG\*5.3\*864 patch loads the “URGENT ADDRESS AS FEMALE” patient record file entry into the PRF National Flag file (#26.15). This post-init routine will update the flag’s TIU PN TITLE field with the new “PATIENT FLAG CATEGORY I - URGENT    ADDRESS AS FEMALE” TIU Document Definition. Note: The TIU\*1.0\*275 patch installed this new TIU PN TITLE, before the DG\*5.3\*864 patch install.

> GMTS\*2.7\*103 Pre and Post-Routines

> GMTS\*2.7\*103 runs an environment check routine to ensure that IEN 257 in ^GMT(142.1 is unused and will also check for any NAME (.01) or ABBREVIATION (3) conflicts with the new component. If any conflicts are found, the environment check will indicate the conflict, the install will abort, and the transport global will be unloaded from the system.

> The pre-install routine will remove any previous version of the Reminder Exchange file that is used to install the two new Health Summary Types. In the event of multiple installations, this step ensures that the Reminder Exchange file used during installation is from the build instead of the version stored in the REMINDER EXCHANGE file (#811.9).

> The post-install routine will install the Health Summary Component into the HEALTH SUMMARY COMPONENT file (#142.1). This routine will also initiate the Reminder Exchange installation for the Health Summary Types.

>  Once the post-install is completed the post-init routines can be deleted.

# Post-Install Set-up Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing the USH PRF LEGAL SOLUTION 1.0 bundle and the MPIF\*1.0\*58 patch, the following post-install set-up steps should be followed. Note: Recommended role

## Check for errors and monitor PRF HL7 messaging for increase in activity. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM should check for any errors in error logs. Note: During the post-installation process, for every Category I flag owned on your VA system, there will be HL7 update messages sent to each treating facility that sees the patient with the Category I flag. Use the PRF HL7 Messaging tools to monitor the increase in activity.

## Verify that the new URGENT ADDRESS AS FEMALE Category I flag was added to the National Flag List.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Review the definition of the URGENT ADDRESS AS FEMALE Category I flag to be familiar with how it will be used – extremely limited use.

DGPF RECORD FLAG MANAGEMENT Record Flag Management run

routine

Record Flag Management

...EXCUSE ME, HOLD ON...

RECORD FLAG MANAGEMENT Jul 22, 2013@11:19:19 Page: 1 of 1

Flag Category: I (National) Sorted By: Flag Name

Flag Name Flag Type Flag Status

1 BEHAVIORAL BEHAVIORAL ACTIVE

2 HIGH RISK FOR SUICIDE CLINICAL ACTIVE

<span class="mark">3 URGENT ADDRESS AS FEMALE OTHER</span> ACTIVE

> Enter ?? for more actionsEnter ?? for more actions

CC Change Category DF Display Flag Detail EF (Edit Record Flag)

CS Change Sort AF (Add New Record Flag)

Select Action:Quit//

> Use DF (Display Flag Action) to see the flag definition.

<u>RECORD FLAG MANAGEMENT Jul 22, 2013@11:19:19 Page: 1 of 1</u>

Flag Category: I (National) Sorted By: Flag Name

<u>Flag Name Flag Type Flag Status</u>

1 BEHAVIORAL BEHAVIORAL ACTIVE

2 HIGH RISK FOR SUICIDE CLINICAL ACTIVE

3 URGENT ADDRESS AS FEMALE OTHER ACTIVE

> Enter ?? for more actions

CC Change Category DF Display Flag Detail EF (Edit Record Flag)

CS Change Sort AF (Add New Record Flag)

Select Action:Quit// <span class="mark">DF</span> Display Flag Detail

Select Record Flag: (1-3): <span class="mark">3</span>

...SORRY, THIS MAY TAKE A FEW MOMENTS...

> <u>FLAG DETAILS Jul 22, 2013@11:23:47 Page: 1 of 1</u>

> Flag Name: URGENT ADDRESS AS FEMALE Flag Status: ACTIVE

> Flag Name: URGENT ADDRESS AS FEMALE

> Flag Category: I (NATIONAL)

> Flag Type: OTHER

> Flag Status: ACTIVE

> Review Freq Days: 0 \<Notice no Review Freq for this flag – so no Review Date\>

> Notification Days: 0

> Review Mail Group: \<No Review Mail Group because no Review Freq\>

> Progress Note Title: <span class="mark">PATIENT RECORD FLAG CATEGORY I - URGENT ADDRESS AS FEMAL</span>

> \<Note the Progress Note Title to be used with this flag.\>

> Flag Description:

> -----------------

> <span class="mark">This Patient Record Flag was established to ensure that a transgender</span>

> <span class="mark">Veteran is addressed as Female per a court order agreement. This flag</span>

> <span class="mark">cannot be used without approval of the Under Secretary for Health.</span>

> \<Note the specific use for this flag\>

> Enter ?? for more actions

Select Action:Quit//

## Verify that the TIU Document Definition for the new Progress Note Title was added by the TIU\*1.0\*275 patch.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The example below is based on using FileMan Inquiry.

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: HEALTH SUMMARY COMPONENT// <span class="mark">TIU DOCUMENT</span>

1 TIU DOCUMENT (10917 entries)

2 TIU DOCUMENT DEFINITION (647 entries)

3 TIU DOCUMENT PARAMETERS (34 entries)

CHOOSE 1-3: <span class="mark">2</span> TIU DOCUMENT DEFINITION (647 entries)

Select TIU DOCUMENT DEFINITION NAME: <span class="mark">PATIENT RECORD FLAG</span>

1 PATIENT RECORD FLAG CAT I DOCUMENT CLASS

2 PATIENT RECORD FLAG CAT II DOCUMENT CLASS

3 PATIENT RECORD FLAG CATEGORY I TITLE

4 PATIENT RECORD FLAG CATEGORY I - HIGH RISK FOR SUICIDE TITLE

Std Title: MENTAL HEALTH PATIENT RECORD FLAG

5 PATIENT RECORD FLAG CATEGORY I - URGENT ADDRESS AS FEMALE TITLE

Std Title: PATIENT RECORD FLAG

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: <span class="mark">5</span> PATIENT RECORD FLAG CATEGORY I - URGENT ADDRESS AS FEMALE

TITLE

Std Title: PATIENT RECORD FLAG

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// - No record number (IEN), no Computed

Fields

DISPLAY AUDIT TRAIL? No// NO

NAME: <span class="mark">PATIENT RECORD FLAG CATEGORY I - URGENT ADDRESS AS FEMALE</span>

PRINT NAME: PATIENT RECORD FLAG CATEGORY I - URGENT ADDRESS AS FEMALE

TYPE: TITLE CLASS OWNER: CLINICAL COORDINATOR

STATUS: <span class="mark">ACTIVE</span> NATIONAL STANDARD: <span class="mark">YES</span>

OK TO DISTRIBUTE: YES

VHA ENTERPRISE STANDARD TITLE: <span class="mark">PATIENT RECORD FLAG</span>

MAP ATTEMPTED: JUL 19, 2013@08:17:13 MAP ATTEMPTED BY: CRCAC,TWO

TIMESTAMP: 63022,29833

## Assign Clinician to the new DGPF PATIENT RECORD FLAGS MGR User Class 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To write a PRF note for a category I flag, the user must belong to the DGPF PATIENT RECORD FLAG MGR user class using the USR CLASS MANAGEMENT MENU. Each site will be responsible for populating this user class.
2.  One clinician at one VA site (Biloxi) will be creating the progress note associated with the new URGENT ADDRESS AS FEMALE assignment for one patient. IRM staff or CAC must make sure this one clinician is added to the DGPF PATIENT RECORD FLAGS MGR User Class.
3.  The new “PATIENT FLAG CATEGORY I - URGENT    ADDRESS AS FEMALE” TIU Document Definition title is in the existing Document Class PATIENT RECORD FLAG CAT I, and the existing business rule applies to that Document Class, so the rule applies to the new title automatically.

> Business Rule:

> An UNTRANSCRIBED (DOCUMENT CLASS) PATIENT RECORD FLAG CAT I may

> BE ENTERED by a DGPF PATIENT RECORD FLAGS MGR

>  DESCRIPTION: <span class="mark">This rule limits note entry to persons specially trained to</span>

> <span class="mark">assign and document the assignment of Category I Patient Record Flags.</span>

> Sites must not alter, delete, or override this rule. Rule created by patch USR\*1\*24.

> Example of USR CLASS MANAGEMENT for current Category I TIU Standard Note Title:

Select OPTION NAME: USR

    1   USR BUSINESS RULE MANAGEMENT       Manage Business Rules     action

    2   USR CLASS DEFINITION       User Class Definition     action

    3   USR CLASS MANAGEMENT MENU       User Class Management     menu

    4   USR INITIALIZE MEMBERSHIP    Initialize Membership of User Classes action

     5   USR LIST MEMBERSHIP BY CLASS       List Membership by Class     action

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 2  USR CLASS DEFINITION     User Class Definition     action

User Class Definition

Select User Class Status: ACTIVE//    Active 

        Start With Class: FIRST//

             Go To Class: LAST//

Searching for the User Classes..................................................

<u>User Classes                  Oct 30, 2012@09:04:33          Page:    9 of   42</u>

                             ACTIVE USER CLASSES                    622 Classes

<u>+     Class Name                                         Abbrev                </u>

121  DERMATOLOGIST: CLINICAL & LABORATORY                DERM                  

122  DERMATOLOGY FELLOW                                  DERM                  

123  DERMATOPATHOLOGIST                                  DERMP                 

124  DETECTIVE                                           DET                   

125  DEVELOPER                                           DEV                   

<span class="mark">126  DGPF PATIENT RECORD FLAGS MGR</span>                       PRFM                  

127  DIABETES STUDY NURSE                                DSRN                   

128  DIALYSIS TECHNICIAN                                 DIALTEC               

129  DIETETIC INTERN                                     DI                    

130  DIETETIC TECHNICIAN STUDENT                         DTS

+         + Next Screen  - Prev Screen  ?? More Actions                        

     Find                      Expand/Collapse Class     Change View

     Create a Class            List Members              Quit

     Edit User Class

Select Action: Next Screen// 126    

Listing Members of \#126

<u>User Class Members            Oct 30, 2012@09:05:11          Page:    1 of    1</u>

                        DGPF PATIENT RECORD FLAGS MGRs                5 Members

<u>     Member                                                 Effective  Expires </u>

1    MHPROVIDER,THREE                                                       

2    MHPROVIDER,TWELVE 10/18/11           

3    MHPROVIDER,TEN

4    MHPROVIDER,TWO 10/18/11           

5    WHPROVIDER,THIRTEEN                       

         (?SBPN) missing SIGNATURE BLOCK PRINTED NAME                       \>\>\>

     Add                       Remove                    Change View

     Edit                      Schedule Changes          Quit

Select Action: Quit// <span class="mark">AD</span>   Add 

Select MEMBER: MHPROVIDER, TWENTY       TM          CAC MD

MEMBER: MHPROVIDER, TWENTY//

EFFECTIVE DATE: NOW  (OCT 30, 2012)

EXPIRATION DATE:

## ## Clinician’s note linked to NEW ASSIGNMENT action after assignment.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Linking PRF Notes to Flag Actions

> The only actions that will be available to link a note to for the URGENT ADDRESS AS FEMALE flag will be the NEW ASSIGNMENT action. The only other action that can be taken for the URGENT ADDRESS AS FEMALE flag is the change owner site action, which can only be done at the site that owns this flag.

> In the CPRS GUI, users must link a PRF progress note to a flag action when the user writes a PRF note. This linking can also be done through the List Manager interface using TIU options. In the CPRS GUI’s Progress Note Properties dialog, when a user selects a Patient Record Flag progress note title, CPRS displays a list of flag actions to which the note can be linked at the bottom of the dialog. This list shows all the actions for the flag and whether each action has been linked.

![](dg-5-3-864-ush-prf-legal-solution-installation-guide/002.png)

> For progress note titles that document the justification for a patient record flag, users will be able to link the progress note to the specific flag action they are documenting. The example shown here is of a Category I PRF progress note and the Continue action to which the user would choose to link.

## Add Health Summary Types to the list of available reports in CPRS.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The two new Health Summary Types, VA-PT RECORD FLAG STATUS and REMOTE PT RECORD FLAG STATUS must be added to the list of available reports viewable in CPRS GUI. This can be done in different ways and from several different menus. Depending on local configuration, all health summary types may be available for selection or the selection may be configured to a defined list. See “Health Summary Configuration” in the Reports section of the CPRS Technical Manual: GUI Version for further information. Always follow your site's local policies on how to assign these items to the list of available reports. Any users with a CPRS session open during the time of installation will need to close and re-open CPRS in order to see the new Health Summary Types on the Reports tab.

> This example uses the Health Summary Coordinator's menu \[GMTS COORDINATOR\] to add the items for use at the System level.

GMTS COORDINATOR Health Summary Coordinator's Menu menu

1 Print Health Summary Menu ...

2 Build Health Summary Type Menu ...

3 Set-up Batch Print Locations

4 List Batch Health Summary Locations

5 CPRS Reports Tab 'Health Summary Types List' Menu ...

Select Health Summary Coordinator's Menu \<TEST ACCOUNT\> Option: 5 CPRS Reports Tab 'Health Summary Types List' Menu

1 Display 'Health Summary Types List' Defaults

2 Precedence of 'Health Summary Types List'

3 Method of compiling 'Health Summary Types List'

4 Edit 'Health Summary Types List' Parameters

Select CPRS Reports Tab 'Health Summary Types List' Menu \<TEST ACCOUNT\>

Option:4 Edit 'Health Summary Types List' Parameters

Allowable Health Summary Types may be set for the following:

2 User USR \[choose from NEW PERSON\]

3 Division DIV \[choose from INSTITUTION\]

4 System SYS \[DVF.your system\]

5 Service SRV \[choose from SERVICE/SECTION\]

Enter selection: 4 System DVF.your system

\- Setting Allowable Health Summary Types for System:

DVF.your system -

Select Sequence: ?

Sequence Value

-------- -----

1 GMTS HS ADHOC OPTION

2 GEC/LOCAL TEST

7 VA-MH HIGH RISK PATIENT

20 REMOTE MH HIGH RISK PATIENT

Select Sequence: 15

Are you adding 15 as a new Sequence? Yes// YES

Sequence: 15// 15

Health Summary: VA-PT RECORD FLAG STATUS

Select Sequence: 25

Are you adding 25 as a new Sequence? Yes// YES

Sequence: 25// 25

Health Summary: REMOTE PT RECORD FLAG STATUS

## ONE SITE ONLY: Add flag for patient.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After all sites have completed the install – one site will be instructed, by the Office of Under Secretary for Health, to add the URGENT    ADDRESS AS FEMALE flag for a specified patient.  Any site that has treated this patient will be updated automatically by the patient record flag software after the flag is added for the patient.  New sites registering the patient will either be updated during the Registration process or by the Master Patient Index process that updates the patient’s  national ICN and treating facility list.      

# # Appendix A: Installation Capture 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Select INSTALL NAME: USH PRF LEGAL SOLUTION 1.0 8/27/13@08:46:44

=\> USH PRF LEGAL SOLUTION 1.0 ;Created on Aug 27, 2013@08:45:32

This Distribution was loaded on Aug 27, 2013@08:46:44 with header of

USH PRF LEGAL SOLUTION 1.0 ;Created on Aug 27, 2013@08:45:32

It consisted of the following Install(s):

USH PRF LEGAL SOLUTION 1.0 TIU\*1.0\*275 DG\*5.3\*864 GMTS\*2.7\*103

Checking Install for Package USH PRF LEGAL SOLUTION 1.0

Install Questions for USH PRF LEGAL SOLUTION 1.0

Checking Install for Package TIU\*1.0\*275

Install Questions for TIU\*1.0\*275

Checking Install for Package DG\*5.3\*864

Install Questions for DG\*5.3\*864

Checking Install for Package GMTS\*2.7\*103

Will first run the Environment Check Routine, GMTSY103

GMTS\*2.7\*103 has been previously installed. Environment check complete.

Install Questions for GMTS\*2.7\*103

Incoming Files:

811.8 REMINDER EXCHANGE (including data)

> **NOTE:** You already have the 'REMINDER EXCHANGE' File.

I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME

-------------------------------------------------------------------------------

Install Started for USH PRF LEGAL SOLUTION 1.0 :

Aug 27, 2013@08:47:06

Build Distribution Date: Aug 27, 2013

Installing Routines:

Aug 27, 2013@08:47:06

Install Started for TIU\*1.0\*275 :

Aug 27, 2013@08:47:06

Build Distribution Date: Aug 27, 2013

Installing Routines:

Aug 27, 2013@08:47:06

Running Post-Install Routine: ^TIUPS275

Title Created: PATIENT RECORD FLAG CATEGORY I - URGENT ADDRESS AS FEMALE

Title attached to Document Class PATIENT RECORD FLAG CAT I

Updating Routine file...

Updating KIDS files...

TIU\*1.0\*275 Installed.

Aug 27, 2013@08:47:06

Not a production UCI

NO Install Message sent

Install Started for DG\*5.3\*864 :

Aug 27, 2013@08:47:06

Build Distribution Date: Aug 27, 2013

Installing Routines:

Aug 27, 2013@08:47:07

Running Post-Install Routine: ^DG53864P

The 'URGENT ADDRESS AS FEMALE' PRF is already entered in the PRF

NATIONAL FLAG file, install will abort.

Updating Routine file...

Updating KIDS files...

DG\*5.3\*864 Installed.

Aug 27, 2013@08:47:07

Not a production UCI

NO Install Message sent

Install Started for GMTS\*2.7\*103 :

Aug 27, 2013@08:47:07

Build Distribution Date: Aug 27, 2013

Installing Routines:

Aug 27, 2013@08:47:07

Running Pre-Install Routine: PRE^GMTSY103

Cleaning up any previous versions of Reminder Exchange file entry

Installing Data Dictionaries:

Aug 27, 2013@08:47:07

Installing Data:

Aug 27, 2013@08:47:07

Running Post-Install Routine: POST^GMTSY103

Installing Health Summary Component...

Filing "CAT I PT RECORD FLAG STATUS" component in Health Summary

Component has already been installed

Installing Health Summary Types...

Creating stub entries for Remote Health Summary Type.

Removing any previous version of Remote Health Summary Type

1\. Installing Reminder Exchange entry VA-HS TYPES GMTS\*2.7\*103

Updating Routine file...

Updating KIDS files...

GMTS\*2.7\*103 Installed.

Aug 27, 2013@08:47:08

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

USH PRF LEGAL SOLUTION 1.0 Installed.

Aug 27, 2013@08:47:08

No link to PACKAGE file

GMTS\*2.7\*103

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution