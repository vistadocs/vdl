---
title: IEMM Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: IEMM
app_code: ACR
app_name: Ambulatory Care Reporting
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: Scheduling V. 5.3Ambulatory Care Reporting Project (ACRP)Incomplete Encounter Management Module (IEMM) Installation GuidePatches SD\5.3\66, DG\5.3\139, PX\1.0\41January 1998Introduction
audience: 
keywords: 
  - patch
  - event
  - routine
  - appointment
  - sdam
  - events
  - exit
  - action
  - installation
  - install
page_count: 0
word_count: 1049
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Ambulatory_Care_Reporting/acr_p_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Ambulatory_Care_Reporting/acr_p_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=116"
---

Scheduling V. 5.3Ambulatory Care Reporting Project (ACRP)Incomplete Encounter Management Module (IEMM) Installation GuidePatches SD\*5.3\*66, DG\*5.3\*139, PX\*1.0\*41January 1998Introduction

> DG\*5.3\*139

> PX\*1.0\*41

Package IntegrationInstallation Steps

Introduction

This patch installs the Incomplete Encounter Management Module (IEMM), part of the Ambulatory Care Reporting Project (ACRP) Phase II. The patch will provide the data validation tools necessary for sites to maintain the correctness of outpatient data being transmitted to the Austin Automation Center.

As part of this install, the Ambulatory Care event handler (SCDX AMBCARE EVENT) will be removed from the item list of the PIMS event driver (SDAM APPOINTMENT EVENTS) and placed on the exit action of the PIMS event driver. The following is a description of the potential errors which may occur in this process and how to correct them.

- “Removal of SCDX AMBCARE EVENT protocol from the Scheduling Event driver was not complete. Please review the installation instructions of this patch.”

This error indicates either the SDAM APPOINTMENT EVENTS protocol or the SCDX AMBCARE EVENT item in SDAM APPOINTMENT EVENTS could not be found. If SDAM APPOINTMENT EVENTS is not present, check to see if it has been deleted or renamed to something else. This is the official protocol name of the PIMS event driver. It must be present for the PIMS software to operate correctly. Contact your local CIOFO if SDAM APPOINTMENT EVENTS is not present. If SDAM APPOINTMENT EVENTS is missing, the software to populate the exit action will not be executed.

If SCDX AMBCARE EVENT is not present, the software cannot remove it from the item list. It will continue to attempt to load the exit action of the SDAM APPOINTMENT EVENTS protocol.

This error message will also be displayed when the install is being run again. The message, at this point, indicates that SCDX AMBCARE EVENT was removed from SDAM APPOINTMENT EVENTS item list.

- “The exit action for SDAM APPOINTMENT EVENTS on your system was: XX.

An attempt was made to replace it, but failed.

It has been replaced with D EN^SCDXHLDR

You will need to edit this protocol’s exit action to restore your changes.”

Until now, the PIMS event driver SDAM APPOINTMENT EVENTS did not have a distributed exit action. The Ambulatory Care event handler is now on the exit action of this protocol. The install software makes an attempt to place the D EN^SCDXHLDR at the end of anything that is currently in the exit action. If this attempt fails, then the exit action is replaced with

D EN^SCDXHLDR. It would now be necessary to use FileMan to edit the exit action and replace your Class Three software changes.

DG\*5.3\*139

This is an informational patch. The routine and global changes will be installed as part of Patch SD\*5.3\*66. Please refer to SD\*5.3\*66 for a complete description of the Incomplete Encounter Management Module patch.

<u>Routine Summary</u>

The following is a list of the routine(s) included in this patch. The second line of each of these routine(s) will look like:

\<tab\>;;5.3;Registration;\*\*\[patch list\]\*\*;Aug 13, 1993

CHECK^XTSUMBLD results

<u>Routine Name</u> <u>Before Patch</u> <u>After Patch</u> <u>Patch List</u>

DG10 3605485 6200881 32,109,139

DGRPE 17405601 17674346 32,114,139

DGRPU1 1362026 1392644 139

PX\*1.0\*41

This is an informational patch. The routine changes will be installed as part of Patch SD\*5.3\*66. Please refer to SD\*5.3\*66 for a complete description of the Incomplete Encounter Management Module patch.

<u>Routine Summary</u>

The following is a list of the routine(s) included in this patch. The second line of each of these routine(s) will look like:

\<tab\>;;1.0;PCE PATIENT CARE ENCOUNTER;\*\*\[patch list\]\*\*;Aug 12, 1996

CHECK^XTSUMBLD results

<u>Routine Name</u> <u>Before Patch</u> <u>After Patch</u> <u>Patch List</u>

PXKMASC 4861775 4911140 22,41

PXKCO 973622 3403563 28,41

Package Integration

This package contains KIDS builds from three software packages. Minimally, the following three base packages must be installed to install this package.

PCE V. 1.0

Registration V. 5.3

Scheduling V. 5.3

Additionally, VA FileMan V. 21.0, Kernel V. 8.0, and Kernel Toolkit V. 7.3 should also be installed. Scheduling ensures that the following patches are installed in its environment check routine.

DG\*5.3\*109

DG\*5.3\*114

SD\*5.3\*44

SD\*5.3\*128

PX\*1.0\*22

PX\*1.0\*28

XU\*8.0\*49

Installation Steps

This patch affects Check-Out, Patient Load/Edit, PCE, and the Appointment Event Driver process so it is recommended that it be installed during non-peak hours to minimize disruption to users. Installation will take less than 10 minutes.

1. Download the KIDS file SD_53_P66.KID from any of the three CIOFO anonymous directories to the appropriate directory on your system.
2. Review your mapped set. If any of the routines listed in the Routine Summary section are mapped, they should be removed from the mapped set at this time.
3. From the Kernel Installation and Distribution System Menu, select the Installation menu.
4. From this menu, select the Load a Distribution option. At the “Enter a Host File:” prompt, enter SD_53_P66.KID.
5. You may now elect to use the following options. When prompted for INSTALL NAME, enter SD\*5.3\*66.

> a\. Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as DDs or templates.

> b\. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c\. Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.

6. Use the Install Package(s) option and select SD\*5.3\*66.
7. You will be prompted with the following install question.

> “Do you wish to turn the validator on for all clinics? NO//”

> A YES answer will turn the parameter WORKLOAD VALIDATION AT CHK

> OUT on for all clinics. As a result, the validation software will run each time there is a completely checked out encounter.

> A NO answer will not turn this parameter on. If you wish to have the validation software executed for a clinic, you will need to edit that clinic setup to turn on the parameter.

8. When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//”, respond YES. When prompted to select the options you would like to place out of order, enter the following.

> SCDX AMBCAR NIGHTLY XMIT Ambulatory Care Nightly Transmission to NPCDB

> SDAM APPT MGT Appointment Management

> SDAM APPT CHECK IN/OUT Appointment Check-in/Check-out

> SDADDEDIT Add/Edit Stop Codes

> SDAPP Appointment Menu

> SDI Check-in/Unsched. Visit

> SDM Make Appointment

> DG DISPOSITION APPLICATION Disposition an Application

> DG DISPOSITION EDIT Disposition Edit

> DG LOAD PATIENT DATA Load/Edit Patient Data

> PXCE ENCOUNTER DATA ENTRY PCE Encounter Data Entry

> PXCE ENCOUNTER ENTRY & DELETE PCE Encounter Data Entry

> PXCE ENCOUNTER ENTRY NO DELETE PCE Encounter Entry No Delete

> PXCE ENCOUNTER ENTRY SUPER PCE Encounter Data Entry - Supervisor

When prompted to select the protocols you would like to place out of order, enter the following.

> SDAM PCE EVENT Process PCE Event Data

If this is a first time install, the following protocols can be skipped; otherwise, these protocols will need to be placed out of order as well.

> SCENI CALL LOAD EDIT Load/Edit Patient Data

> SCENI CHECKOUT INTERVIEW Check Out

> SCENI ENCOUNTER INFORMATION Encounter Information

> SCENI PATIENT DEMOGRAPHICS Patient Demographics

> SCENI REFLAG ERROR Retransmit Error

> SCENI CORRECT ERROR Correct Error(s)

9. If routines were unmapped as part of Step 2, they should be returned to the mapped set once the installation has run to completion.
10. Set up the SCDX INCOMPLETE ENCOUNTER MGMT bulletin with the mail group to receive the summary bulletins. This can be either an existing mail group or you can create a new group for this purpose. There should be at least one member in the mail group you assign to the bulletin.
11. If you want the clinic summary fired off as a bulletin, you will need to use the Schedule/Unschedule options of the TaskMan Management menu. Proceed with the following steps after the installation is complete.

> a\. Select OPTION to schedule or reschedule: SCENI IEMM SUMMARY BULLETIN.

> b\. Specify the time run in the QUEUED TO RUN AT WHAT TIME field.

> c\. Specify 1D in the RESCHEDULING FREQUENCY field.

12. The following security keys will need to be assigned to the appropriate personnel at your site. See the ACRP IEMM Release Notes for a detailed explanation of these security keys.

> SCENI IEMM EDIT

> SCENI ENCOUNTER EDIT

> SCENI MEANS TEST EDIT