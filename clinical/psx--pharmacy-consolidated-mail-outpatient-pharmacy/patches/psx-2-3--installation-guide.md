---
title: PSX*2*3 Installation Guide with Modifications for Outpatient Pharmacy Versions 6 and 7
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: with Modifications for Outpatient Pharmacy Versions 6 and 7
app_code: PSX
app_name: "Pharmacy: Consolidated Mail Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSX
patch_ver: 2
patch_id: PSX*2*3
group_key: "PSX:PSX:2"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](psx-2-3-installation-guide-with-modifications-for-outpatient-pharmacy-versions-6/001.png)
audience: 
keywords: 
  - cmop
  - tasks
  - resource
  - installation
  - step
  - fileman
  - manager
  - transmission
  - edit
  - patch
page_count: 0
word_count: 2142
section_count: 6
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_3ins.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Consol_Mail_Outpat_Pharm_(CMOP)/psx_2_3ins.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=85"
---

![](psx-2-3-installation-guide-with-modifications-for-outpatient-pharmacy-versions-6/001.png)

CONSOLIDATED MAIL OUTPATIENT PHARMACY (CMOP)Patch PSX\*2\*3Modifications for Outpatient Pharmacy 6.0/7.0INSTALLATION GUIDE

July 1998

Office of the Chief Information Officer

Table of ContentsPre/Post Installation Instructions for Consolidated Mail Outpatient Pharmacy Patch PSX\*2\*3 [1](#prepost-installation-instructions-for-consolidated-mail-outpatient-pharmacy-patch-psx23)

Intranet [1](#intranet)

Remote Medical Center Pre-installation Tasks for PSX\*2\*3 [1](#remote-medical-center-pre-installation-tasks-for-psx23)

Remote Medical Center Post Installation Instructions for Patch PSX\*2\*3 [5](#remote-medical-center-post-installation-instructions-for-patch-psx23)

Host CMOP Facility Pre-installation Tasks for PSX\*2\*3 [5](#host-cmop-facility-pre-installation-tasks-for-psx23)

Host CMOP Facility Post Installation Instructions for Patch PSX\*2\*3 [5](#host-cmop-facility-post-installation-instructions-for-patch-psx23)

# # Pre/Post Installation Instructions for Consolidated Mail Outpatient Pharmacy Patch PSX\*2\*3


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Pre/Post Installation Instructions for Consolidated Mail Outpatient Pharmacy Patch PSX\2\3](#prepost-installation-instructions-for-consolidated-mail-outpatient-pharmacy-patch-psx23)
  - [Intranet](#intranet)
  - [Remote Medical Center Pre-installation Tasks for PSX\2\3](#remote-medical-center-pre-installation-tasks-for-psx23)
  - [Remote Medical Center Post Installation Instructions for Patch PSX\2\3](#remote-medical-center-post-installation-instructions-for-patch-psx23)
  - [Host CMOP Facility Pre-installation Tasks for PSX\2\3](#host-cmop-facility-pre-installation-tasks-for-psx23)
  - [Host CMOP Facility Post Installation Instructions for Patch PSX\2\3](#host-cmop-facility-post-installation-instructions-for-patch-psx23)
> Consolidated Mail Outpatient Pharmacy (CMOP) Version 2.0 patch PSX\*2\*3 contains functionality required for CMOP software to operate successfully with both Outpatient Pharmacy Version 6.0 and Outpatient Pharmacy Version 7.0 software in conjunction with Version 1.0 of the Computerized Patient Record System (CPRS) software package.
> This manual is divided into two sections. Section one contains information used by the remote medical centers. The remote medical centers must complete *all* pre-installation tasks prior to the installation of this patch. Section two contains the information necessary for installation at the host CMOP facility.

## Intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Documentation for this product can now be found on the Intranet. You will find it at the following address:

> http://www.vista.med.va.gov/softserv/clin_bro.ad/index.html

> This address will take you to the Clinical Products page where you will find a listing of all the clinical software manuals. Click on the Consolidated Mail Outpatient Pharmacy link and it will take you to the CMOP Homepage. You can also get there by going to the following address:

> http://www.vista.med.va.gov/softserv/clin_nar.row/cmop/index.html

 Remember to bookmark this site for future reference.

## Remote Medical Center Pre-installation Tasks for PSX\*2\*3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To prevent pharmacy prescription data corruption and/or interruption of CMOP background processes, remote medical centers *must* complete the following pre-installation tasks prior to the install of this patch. This will ensure the installation is not running simultaneously with CMOP data transmissions, CMOP background release filers, or other associated CMOP tasks.

> \*\*\*IMPORTANT\*\*\*

> During the install of this patch at Department of Veterans Affairs (VA) medical centers, have Outpatient Pharmacy personnel *sign off* the system. The installation of the KIDS distribution for the patch requires less than 5 minutes to complete. However, additional time should be allowed to complete the Pre- and Post Installation Tasks detailed in this document.

Remote medical centers must complete each STEP in the order listed before installing PSX\*2\*3.Step 1 – Determine System Status for CMOP

> Use the *Display System Setup* \[PSXR STATUS\] option from the *CMOP Site Manager Menu* \[PSXR CMOP MANAGER\] to review the CMOP System Status. CMOP can be inactivated only if line one of the display includes the text, “No current transmission.” If this text is not displayed, a CMOP process is currently running and *inactivation* cannot take place. Once the task is completed, the display will read “No current transmission,” as in line one of the CMOP System Status report shown below. If line one does not contain the text “No current transmission,” try again later. Normally, CMOP tasks require only a few minutes to complete, so the waiting time to retry should be minimal.

*Example Step 1:*

Select the CMOP Site Manager Menu Option: <u>DIS</u>play System Setup

CMOP SYSTEM STATUS

LEAVENWORTH (ACTIVE) No current transmission

CMOP Domain : CMOP-LEAV.MED.VA.GOV

Last Batch Transmitted : 338

CMOP RX Queue purged : SEP 19,1997@08:41:14

Auto Transmission setup : YES

Select CMOP Site Manager Menu Option:<u>\<RET\></u>Step 2 – Record Auto Transmission Information for Rescheduling

> If the last line of the display in the example above reads:

> Auto Transmission setup : NO

> Proceed directly to Step 3 .

If the last line of the display in the example above reads:

> Auto Transmission setup : YES

Auto Transmission setup is in effect. Use the *Setup Auto-transmission* \[PSXR AUTO TRANSMIT\] menu option from the *Transmission Menu* \[PSXR TRANSMIT MENU\] on the *CMOP Site Manager Menu* \[PSXR CMOP MANAGER\] to display the information regarding the current transmission schedule. Print the screen display or otherwise retain this information for reference when completing the Post Install Tasks to reschedule Auto Transmissions.

*  
Example Step 2:*

Select CMOP Site Manager Menu Option: <u>T</u>ransmission Menu

Select Transmission Menu Option: <u>S</u>etup Auto-transmission

Auto Transmissions are already scheduled.

Current schedule began : Aug 05, 1997 6:00 pm

Number of days to transmit thru: 1

Next transmission scheduled for: Sep 04, 1997@18:00

Rescheduling Frequency : 24 hours

Do you want to unschedule automatic processing ? NO//<u>\<RET\></u>

Select CMOP Site Manager Menu Option:<u>\<RET\></u>Step 3 – Inactivate CMOP Processing

> Use the *Activate/Inactivate CMOP Processing* \[PSXR ACTIVATE\] option from the *CMOP Site Manager Menu* \[PSXR CMOP MANAGER\] to inactivate CMOP as illustrated in the following example.

If prescription workload is currently suspended for CMOP transmission, a WARNING message will be displayed as shown in the example below. Take no action on this warning. These prescriptions will be handled appropriately when the patch Post Install Tasks are completed and CMOP processing is Activated.

*Example Step 3:*

Select CMOP Site Manager Menu Option: <u>AC</u>tivate/Inactivate CMOP Processing

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> **WARNING:** There are Rx's currently suspended for CMOP.

If you inactivate CMOP processing:

1\) These Rx's will not transmit to the CMOP, but will remain

in the RX SUSPENSE file. These Rx's cannot be accessed by

Outpatient Pharmacy options. Ideally, these Rx's should

be transmitted or printed before inactivation takes place.

If CMOP processing is activated, these prescriptions can

be transmitted.

2\) Before inactivating, please have all pharmacy users sign

off until inactivation is complete. CMOP Rx's input by

users who do not sign off the system will be suspended for

CMOP transmission. (See \#1)

3\) Your current auto transmission schedule will be

cancelled on inactivation.

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

LEAVENWORTH is the current active CMOP system.

Do you want to Inactivate the LEAVENWORTH system? NO// <u>Y</u>ES

Are you sure? NO// <u>Y</u>ES

The LEAVENWORTH system has been inactivated.

Activate another system? NO// <u>\<RET\></u>

Selecting Display System Setup as follows will show the site has inactivated.

Select CMOP Site Manager Menu Option: <u>DIS</u>play System Setup

Enter CMOP System: <u>LEAVENWORTH</u> INACTIVE

CMOP SYSTEM STATUS

LEAVENWORTH (INACTIVE) No current transmission

CMOP Domain : CMOP-LEAV.MED.VA.GOV

Last Batch Transmitted : 338

CMOP RX Queue purged : SEP 19,1997@08:41:14

Auto Transmission setup : NO

Step 4 – Check the CMOP Resource Device

> To prevent CMOP background tasks, such as the CMOP Release Filer from running during the install and possibly causing data corruption, carefully follow the instructions listed below:

> Any CMOP task currently running must be allowed to complete before the resource device entry is locked.

> Check Taskman as shown below for PSX namespaced tasks running:

*Example Step 4a:*

Select Systems Manager Menu Option: <u>TASK</u>man Management

Select Taskman Management Option: <u>LIS</u>t Tasks

List Tasks Option

All your tasks.

Your future tasks.

Every task.

List of tasks.

Unsuccessful tasks.

Future tasks.

Running tasks.

Select Type Of Listing: <u>R</u>unning tasks.

Running tasks...

240905: ^XMADJF0, MailMan Delivery Mover. No device. BAB,PAA.

From TODAY at 8:43, By you. Started running TODAY at 8:43.

Job \#: 43

-----------------------------------------------------------------------

235907: TRANS^PSXRSUS, CMOP Data Transmission. Device PSX. WPB,PAA.

From TODAY at 9:10, By you. Started running TODAY at 9:10

Job \#: 46

> In the previous example, task number 235907, Job \#46 is a PSX namespaced CMOP task currently running. Continue to list running tasks in this manner until this task is completed and no other PSX tasks are running.

*Example Step 4b:*

Checking the Resource device:

Display of the PSX Resource DEVICE entry when IN USE:

Select OPTION NAME: <u>EVE</u> Systems Manager Menu

Select Systems Manager Menu Option: <u>FM</u> VA FileMan

VA FileMan Version 21.0

Select VA FileMan Option: <u>I</u>nquire to File Entries

OUTPUT FROM WHAT FILE: RESOURCE// <u>\<RET\></u>

Select RESOURCE NAME: <u>PSX</u>

ANOTHER ONE: <u>\<RET\></u>

STANDARD CAPTIONED OUTPUT? Yes// <u>\<RET\></u> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// <u>\<RET\></u> - No record number (IEN), no Computed Fields

NAME: PSX AVAILABLE SLOTS: 0

SLOT IN USE: 1 JOB \#: 46

Select RESOURCE NAME:<u>\<RET\></u>  
Display of the PSX Resource DEVICE entry when FREE:

Select Systems Manager Menu Option: <u>FM</u> VA FileMan

VA FileMan Version 21.0

Select VA FileMan Option: <u>I</u>nquire to File Entries

OUTPUT FROM WHAT FILE: RESOURCE// <u>\<RET\></u>

Select RESOURCE NAME: <u>PSX</u>

ANOTHER ONE: <u>\<RET\></u>

STANDARD CAPTIONED OUTPUT? Yes// <u>\<RET\></u> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// <u>\<RET\></u> - No record number (IEN), no Computed Fields

NAME: PSX AVAILABLE SLOTS: 1

Select RESOURCE NAME:<u>\<RET\></u>Step 5 – Edit the CMOP Resource Device entry

> When the display (Step 4, Example 4b) indicates the PSX device entry in the RESOURCE file (#3.54) is *free* (i.e., Available Slots=1), the PSX device entry may be edited and locked as shown in the example below. Locking the device in this manner signals Taskman the device is busy. Tasks scheduled for this device will be placed on the waiting list for the device and not run until Taskman indicates the device is free.

*Example Step 5:*

Editing the Resource file entry to lock the PSX device:

Select Systems Manager Menu Option: FM VA FileMan

VA FileMan Version 21.0

Select VA FileMan Option: <u>E</u>nter or Edit File Entries

INPUT TO WHAT FILE: RESOURCE// <u>\<RET\></u>

EDIT WHICH FIELD: ALL// <u>AVAILABLE SLOTS</u>

THEN EDIT FIELD: <u>SLOTS IN USE</u> (multiple)

EDIT WHICH SLOTS IN USE SUB-FIELD: ALL// <u>\<RET\></u>

THEN EDIT FIELD: <u>\<RET\></u>

Select RESOURCE NAME: <u>PSX</u>

AVAILABLE SLOTS: 1// <u>@</u> - use the ‘@’ sign to delete this value in the

field

SURE YOU WANT TO DELETE? <u>Y</u> (Yes)

Select SLOT IN USE: <u>1</u>

CPU/VOL: <u>\<RET\></u>

JOB \#: <u>\<RET\></u>

Select SLOT IN USE: <u>\<RET\></u>

Checking the resource device, as shown in Example 4b above, will now display the screen indicating the PSX Resource Device is FREE.

You may now proceed with the installation of the KIDS distribution for patch PSX\*2\*3 following the instructions in the patch description from the National Patch Module.

## Remote Medical Center Post Installation Instructions for Patch PSX\*2\*3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1 – Restart CMOP tasks

> The resource device entry, PSX, must now be cleared to allow CMOP tasks to run as scheduled. FREE the RESOURCE file (#3.54) entry for PSX as shown in the example below.

*Example Step 1:*

Select Systems Manager Menu Option: <u>FM</u> VA FileMan

VA FileMan Version 21.0

Select VA FileMan Option: <u>E</u>nter or Edit File Entries

INPUT TO WHAT FILE: RESOURCE// <u>\<RET\></u>

EDIT WHICH FIELD: ALL// <u>SLOTS IN USE</u> (multiple)

EDIT WHICH SLOTS IN USE SUB-FIELD: ALL// <u>\<RET\></u>

THEN EDIT FIELD: <u>AVAILABLE SLOTS</u>

THEN EDIT FIELD: <u>\<RET\></u>

Select RESOURCE NAME: <u>PSX</u>

Select SLOT IN USE: 1// <u>1</u>

SLOT IN USE: 1// <u>@</u>

SURE YOU WANT TO DELETE THE ENTIRE ‘1’ SLOT IN USE? Y (Yes)

Select SLOT IN USE: <u>\<RET\></u>

AVAILABLE SLOTS: 0// <u>1</u>

Step 2 – Activate CMOP Processing

> Use the *Activate/Inactivate CMOP Processing* \[PSXR ACTIVATE\] option from the *CMOP Site Manager Menu* \[PSXR CMOP MANAGER\] to activate CMOP processing as illustrated in the following example.

*  
Example Step 2:*

Select CMOP Site Manager Menu Option: <u>ACT</u>ivate/Inactivate CMOP Processing

Enter CMOP System: <u>LEAVENWORTH</u> INACTIVE

Enter mailman domain: CMOP-LEAV.MED.VA.GOV// <u>\<RET\></u>

CMOP SYSTEM STATUS

LEAVENWORTH (INACTIVE) No current transmission

CMOP Domain : CMOP-LEAV.MED.VA.GOV

Last Batch Transmitted : 338

CMOP RX Queue purged : SEP 19,1997@08:41:14

Auto Transmission setup : NO

Are you sure you want to activate the LEAVENWORTH system? NO// <u>Y</u>ES

Request to activate sent to LEAVENWORTH.

======================================

> Once this has been completed, you will see the following VA alert:

> (Your site name) has submitted a request to activate CMOP processing.

> When the CMOP Host has approved activation, you will see the following Informational alert:

> I Permission to transmit to LEAVENWORTH has been received.

> Once both of these alerts are received, activation for CMOP processing is complete and transmissions can be initiated.

> Proceed with Step 3 after the above has been completed.

Step 3 – Reschedule Automatic Transmissions

> Reschedule Automatic Transmissions to begin when Outpatient Pharmacy has resumed normal operations. This is accomplished using the *Setup Auto-transmission* \[PSXR AUTO TRANSMIT\] option as shown in the example on the following page.

*  
Example Step 3:*

Select CMOP Site Manager Menu Option: <u>T</u>ransmission Menu

Select Transmission Menu Option: <u>S</u>etup Auto-transmission

Enter the date to start automatic processing: NOW// <u>\<RET\></u> SEP 08, <1997@6:00>

Number of days to transmit thru: (0-10): 0// <u>1</u>

Enter rescheduling frequency (hours) for transmission: (1-96): <u>24</u>

Begin Automatic Transmissions : SEP 8,1997@09:29

Rescheduling Frequency : 24 hours

Number of days to transmit through : 1

Is this correct? NO// <u>Y</u>ES

> When CMOP processing was inactivated the previous Automatic Transmission Schedule was cancelled.

You must reschedule the date and time or the “date to start automatic processing” will default to “NOW.”

> The example above has set up automatic transmissions to begin on the selected date and time. The PSX Resource Device is free and normal Consolidated Mail Outpatient Pharmacy operations may resume.

> This completes the pre/post installation tasks for CMOP remote medical centers.

## Host CMOP Facility Pre-installation Tasks for PSX\*2\*3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The host CMOP facility must complete the following STEPS in the order listed before installing PSX\*2\*3. It is recommended that the CMOP Interface be stopped before installation.Step 1 – Check the CMOP Resource Device

> To prevent CMOP background tasks, such as the CMOP Release Filer from running during the installation and possibly causing data corruption, carefully follow the instructions listed below:

> Any CMOP task currently running must be allowed to complete before the resource device entry is locked.

> Check Taskman as shown below for PSX namespaced tasks running:

*Example Step 1a:*

Select Systems Manager Menu Option: <u>TASK</u>man Management

Select Taskman Management Option: <u>LIS</u>t Tasks

List Tasks Option

All your tasks.

Your future tasks.

Every task.

List of tasks.

Unsuccessful tasks.

Future tasks.

Running tasks.

Select Type Of Listing: <u>R</u>unning tasks.

Running tasks...

240905: ^XMADJF0, MailMan Delivery Mover. No device. BAB,PAA.

From TODAY at 8:43, By you. Started running TODAY at 8:43.

Job \#: 43

-----------------------------------------------------------------------

235907: TRANS^PSXRSUS, CMOP Data Transmission. Device PSX. WPB,PAA.

From TODAY at 9:10, By you. Started running TODAY at 9:10

Job \#: 46

> In the previous example, task number 235907, Job \#46 is a PSX namespaced CMOP task currently running. Continue to list running tasks in this manner until this task is completed and no other PSX tasks are running.

*  
Example Step 1b:*

Checking the Resource device:

Display of the PSX Resource DEVICE entry when IN USE:

Select OPTION NAME: <u>EVE</u> Systems Manager Menu

Select Systems Manager Menu Option: <u>FM</u> VA FileMan

VA FileMan Version 21.0

Select VA FileMan Option: <u>I</u>nquire to File Entries

OUTPUT FROM WHAT FILE: RESOURCE// <u>\<RET\></u>

Select RESOURCE NAME: <u>PSX</u>

ANOTHER ONE: <u>\<RET\></u>

STANDARD CAPTIONED OUTPUT? Yes// <u>\<RET\></u> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// <u>\<RET\></u> - No record number (IEN), no Computed Fields

NAME: PSX AVAILABLE SLOTS: 0

SLOT IN USE: 1 JOB \#: 46

Select RESOURCE NAME:<u>\<RET\></u>Display of the PSX Resource DEVICE entry when FREE:

Select Systems Manager Menu Option: <u>FM</u> VA FileMan

VA FileMan Version 21.0

Select VA FileMan Option: <u>I</u>nquire to File Entries

OUTPUT FROM WHAT FILE: RESOURCE// <u>\<RET\></u>

Select RESOURCE NAME: <u>PSX</u>

ANOTHER ONE: <u>\<RET\></u>

STANDARD CAPTIONED OUTPUT? Yes// <u>\<RET\></u> (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// <u>\<RET\></u> - No record number (IEN), no Computed Fields

NAME: PSX AVAILABLE SLOTS: 1

Select RESOURCE NAME:<u>\<RET\></u>Step 2 – Edit the CMOP Resource Device entry

> When the display (Step 1, Example 1b) indicates the PSX device entry in the RESOURCE file (#3.54) is *free* (i.e., Available Slots=1), the PSX device entry may be edited and locked as shown in the example below. Locking the device in this manner signals Taskman the device is busy. Tasks scheduled for this device will be placed on the waiting list for the device and not run until Taskman indicates the device is free.

*Example Step 2:*

Editing the Resource file entry to lock the PSX device:

Select Systems Manager Menu Option: FM VA FileMan

VA FileMan Version 21.0

Select VA FileMan Option: <u>E</u>nter or Edit File Entries

INPUT TO WHAT FILE: RESOURCE// <u>\<RET\></u>

EDIT WHICH FIELD: ALL// <u>AVAILABLE SLOTS</u>

THEN EDIT FIELD: <u>SLOTS IN USE</u> (multiple)

EDIT WHICH SLOTS IN USE SUB-FIELD: ALL// <u>\<RET\></u>

THEN EDIT FIELD: <u>\<RET\></u>

Select RESOURCE NAME: <u>PSX</u>

AVAILABLE SLOTS: 1// <u>@</u> - use the ‘@’ sign to delete this value in the

field

SURE YOU WANT TO DELETE? <u>Y</u> (Yes)

Select SLOT IN USE: <u>1</u>

CPU/VOL: <u>\<RET\></u>

JOB \#: <u>\<RET\></u>

Select SLOT IN USE: <u>\<RET\></u>

> Checking the resource device, as shown in Example 1b above, will now display the screen indicating the PSX Resource Device is FREE.

> You may now proceed with the installation of the KIDS distribution for patch PSX\*2\*3 following the instructions in the patch description from the National Patch Module.

## Host CMOP Facility Post Installation Instructions for Patch PSX\*2\*3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Step 1 – Restart CMOP tasks

> The resource device entry, PSX, must now be cleared to allow CMOP tasks to run as scheduled. FREE the RESOURCE file (#3.54) entry for PSX as shown in the example below.

*Example Step 1:*

Select Systems Manager Menu Option: <u>FM</u> VA FileMan

VA FileMan Version 21.0

Select VA FileMan Option: <u>E</u>nter or Edit File Entries

INPUT TO WHAT FILE: RESOURCE// <u>\<RET\></u>

EDIT WHICH FIELD: ALL// <u>SLOTS IN USE</u> (multiple)

EDIT WHICH SLOTS IN USE SUB-FIELD: ALL// <u>\<RET\></u>

THEN EDIT FIELD: <u>AVAILABLE SLOTS</u>

THEN EDIT FIELD: <u>\<RET\></u>

Select RESOURCE NAME: <u>PSX</u>

Select SLOT IN USE: 1// <u>1</u>

SLOT IN USE: 1// <u>@</u>

SURE YOU WANT TO DELETE THE ENTIRE ‘1’ SLOT IN USE? Y (Yes)

Select SLOT IN USE: <u>\<RET\></u>

AVAILABLE SLOTS: 0// <u>1</u>

> This completes the pre/post installation tasks for host CMOP facility.