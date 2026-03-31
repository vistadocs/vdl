---
title: MOCHA Version 1 Combined Builds Installation Guide (REVISED VERSION)
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Combined Builds  (REVISED VERSION)
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 1
patch_id: PSJ*1
group_key: "PSJ:PSJ:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - installation
  - install
  - table
  - contents
  - build
  - patch
  - pharmacy
  - message
  - transport
  - distribution
page_count: 0
word_count: 3727
section_count: 17
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/mocha_cb_pss_1_ig_r0811.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/mocha_cb_pss_1_ig_r0811.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

> ![](mocha-version-1-combined-builds-installation-guide-revised-version/001.png)

Medication Order Check Healthcare Application (MOCHA) v1.0Combined BuildInstallation Guide

PSS\*1\*117 (Stand-alone)

PSO\*7\*251, PSJ\*5\*181, OR\*3\*272

PSO\*7\*375 (Stand-alone)

PSS\*1\*163 (Stand-alone)

April 2011

Product Development

Revision History

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revised Pages</th>
<th>Patch</th>
<th>Description of Change</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2011</td>
<td><p>i,</p>
<p><a href="#piii">iii</a>,</p>
<p><a href="#p5">5</a>,</p>
<p><a href="#p6">6</a>,</p>
<p><a href="#installation-of-combined-build">7-8b</a></p></td>
<td>PSS*1*163</td>
<td><p>Update Revision History</p>
<p>Update Table of Contents</p>
<p>Added Note regarding the POSTMASTER</p>
<p>Information added to warning regarding POSTMASTER</p>
<p>Due to information added above, it moved the text onto the next page. Nothing changed on these pages, only the page number.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>04/2011</td>
<td>All</td>
<td>PSS*1*117, PSO*7*251, PSJ*5*181, OR*3*272, PSO*7*375</td>
<td><p>New Document Version1.0.</p>
<p>Change VistA to PEPS to VistA to MOCHA.</p>
<p>Remove PSGOER and change Increment to MOCHA.</p>
<p>Edits made to accommodate the changes in the final build</p>
<p>Removed PRE from the document.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

*(This page included for two-sided copying.)*

<span id="piii" class="anchor"></span>Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
- [Pre-Installation Considerations](#pre-installation-considerations)
  - [Minimum Required Packages](#minimum-required-packages)
  - [Required Patches](#required-patches)
- [Installation of PSS\1\117](#installation-of-pss1117)
  - [Overview](#overview)
  - [Installation Considerations](#installation-considerations)
  - [Pre-Installation Instructions](#pre-installation-instructions)
  - [PSS\1\117 Installation Steps](#pss1117-installation-steps)
  - [Post-Installation Instructions](#post-installation-instructions)
  - [Validation of Communication Linkage](#validation-of-communication-linkage)
    - [Check Vendor Database Link](#check-vendor-database-link)
  - [Schedule/Reschedule Check PEPS Interface](#schedulereschedule-check-peps-interface)
- [Installation of Combined Build](#installation-of-combined-build)
  - [Software Retrieval for Combined Build](#software-retrieval-for-combined-build)
  - [Pre/Post Installation Overview](#prepost-installation-overview)
  - [Combined Build Installation Steps](#combined-build-installation-steps)
  - [Post-Installation Instructions](#post-installation-instructions-1)
  - [Example of Combined Build Install](#example-of-combined-build-install)
- [Appendix](#appendix)
  - [Acronyms](#acronyms)
Medication Order Check Healthcare Application (MOCHA) v1.0 provides for the implementation of all order checks demonstrated in the 2006 Pharmacy Enterprise Product System (PEPS) Proof of Concept (POC) Demonstration. Services provided by First DataBank (FDB), our current drug database vendor, will be utilized. VistA enhancements include: enhanced drug-drug interactions to provide more clinical information to the clinician; enhanced duplicate class to utilize FDB’s Enhanced Therapeutic Classification (ETC) system which allows for multiple classes per drug and APIs to support the order check enhancements. Health*<u>e</u>*Vet (H*<u>e</u>*V) construction will include component(s) to utilize services provided by a commercial drug database to support Legacy VistA order check changes. A later release will expand the functionality to include a new maximum single dose order check; a new daily dosage range check; and general dosing information.
The following patches are part of the combined build that makes up the release of MOCHA v1.0: PSO\*7\*251, PSJ\*5\*181, OR\*3\*272, and standalone patches PSS\*1\*117 and PSO\*7\*375.
These patches will introduce a new order check system that utilizes data and logic from a commercial database system. The current Drug Interaction and Duplicate Class order checks are replaced. New Maximum Single Dose and Daily Dose Range order checks will occur in Outpatient Pharmacy, Inpatient Medications, and Computerized Patient Record System (CPRS). The dosing functionality WILL BE RELEASED in a LATER patch.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide installation steps for MOCHA v1.0. The intended audience for this document is the Information Resources Management Service (IRMS) staff and Pharmacy staff responsible for installing and maintaining the Pharmacy files required for drug selection through Pharmacy and Computerized Patient Record System (CPRS).

MOCHA v1.0 will integrate the existing Veterans Health Information Systems and Technology Architecture (VistA) Pharmacy applications with the new Pharmacy Enterprise Product System (PEPS). PEPS contains drug information from a third-party vendor.

# Pre-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before continuing any further, you should have completed the installation and configuration of the VistA to MOCHA v1.0 Interface, distributed as patch PSS\*1.0\*136. Please refer to the VistA to MOCHA v1.0 Interface Installation Guide located on the VA Software Document Library (VDL). Once you have completed installation and configuration of PSS\*1.0\*136, you may proceed to the next section, *Minimum Required Packages*.

## Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patches described in this installation guide can only be run with a standard Massachusetts General Hospital Utility Multi-Programming System (MUMPS) operating system and requires the following Department of Veterans Affairs (VA) software packages.

| Package                                 | Minimum Version Needed |
|-----------------------------------------|------------------------|
| Pharmacy Data Management (PDM)          | 1.0                    |
| VA FileMan                              | 22.0                   |
| Kernel                                  | 8.0                    |
| Health*e*Vet Web Services Client (HWSC) | 1.0                    |
| Outpatient Pharmacy                     | 7.0                    |
| Inpatient Medications                   | 5.0                    |
| Order Entry/Results Reporting           | 3.0                    |

The above software must be installed for these patches to be completely functional.

| Note:                                             | HWSC 1.0 is a new package that was released on March 2, 2011 as patch XOBW\*1.0. |
|---------------------------------------------------|----------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide-revised-version/002.png) |                                                                                  |

## Required Patches 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches should already be installed on your system:

1.  PSS\*1\*147 (must be installed prior to installation of PSS\*1\*136)
2.  PSS\*1\*136 (see *VistA to MOCHA Interface Installation Guide* for specific installation instructions. This is posted on the VDL.)
3.  OR_PSJ_PXRM_28.KID (New CPRS Graphical User Interface (GUI) is required)
4.  OR_30_280.ZIP
5.  PSJ\*5\*179

Once all the patches on this page have been completed and validated, you may proceed to the installation of PSS\*1\*117.

# Installation of PSS\*1\*117

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSS\*1\*117 is a stand-alone patch. The patch is included within the National Patch Module on FORUM. This patch is the first part of a set of patches that make up order checking enhancements. These enhancements will introduce a new order check system that utilizes data and logic from a commercial database system. The current Drug Interaction and Duplicate Class order checks are replaced. New Maximum Single Dose and Daily Dose Range order checks will occur in Outpatient Pharmacy, Inpatient Medications, and Computerized Patient Record System (CPRS). The dosing functionality WILL BE RELEASED in a LATER patch.

## Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*117 should not be installed when Pharmacy Data Management (PDM) options or National Drug File (NDF) options are being used. Also, it should not be installed at the same time any NDF patches are being installed, including DATA UPDATES patches, PMI MAPPING patches, and PMI UPDATES patches. Since this patch exports so many PDM components that could be invoked from other Clinical Applications, we recommend it be installed during Non-Peak hours for all Clinical Applications, including tasked jobs from Clinical Applications.

Installation should take no longer than 10 minutes.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because PSS\*1\*117 rebuilds the PDM menu structure, any locally added options under the Pharmacy Data Management \[PSS MGR\] menu option or any of its sub-menus may no longer be attached after patch install. Review the Pharmacy Data Management \[PSS MGR\] menu option and its sub-menus <u>prior</u> to install to make note of any locally added options so they can be re-attached after install.

## PSS\*1\*117 Installation Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Load Transport Global

    Choose the PackMan message containing this patch and invoke the

    INSTALL/CHECK MESSAGE PackMan option.
1.  Start up Kernel Installation and Distribution System (KIDS)

    Start up the Kernel Installation and Distribution System (KIDS) Menu

    \[XPD MAIN\]:

> Edits and Distribution ...

> Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: INStallation

> ---

> Load a Distribution

> Print Transport Global

> Compare Transport Global to Current System

> Verify Checksums in Transport Global

> Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Backup a Transport Global

> Select Installation Option:

2.  Select Installation Option:

| Note:                                             | The following steps are OPTIONAL (When prompted for the INSTALL NAME, enter PSS\*1.0\*117): |
|---------------------------------------------------|---------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide-revised-version/003.png) |                                                                                             |

1.  Backup a Transport Global - This option creates a backup message of any routines exported with this patch. It does not backup any other changes such as Data Dictionaries (DDs) or templates.
2.  Compare Transport Global to Current System - This option allows you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option allows you to ensure the integrity of the routines that are in the transport global.
3.  Select Installation Option: Install Package(s)

    This is the step to start the installation of this KIDS patch:
1.  Choose the Install Package(s) option to start the patch install and enter "PSS\*1.0\*117" at the INSTALL NAME prompt.

| Note:                                             | Please note that during the Environment check routine, various messages are displayed, and possibly a prompt to continue or abort install will be displayed. Please see the *Post Installation Instructions* section for more details. |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide-revised-version/004.png) |                                                                                                                                                                                                                                        |

2.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//”, answer NO.
3.  When prompted “Want KIDS to INHIBIT LOGONs during the install? NO//”, answer NO.
4.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//”, answer NO.

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the KIDS build is installed, a VistA MailMan message is automatically sent to members of the PSS ORDER CHECKS Mail Group as well as to the user who installs the patch.

The message subject is: “PSS\*1\*117 Installation Complete” and the message text is: “The Installation of patch PSS\*1.0\*117 is complete.”

Please verify that the VistA mail message indicating that the POST-INIT has run to completion has been received. If this message is not received, please log a Remedy Ticket.

The receipt of this VistA mail message verifies that the POST-INIT has run to completion. It is important that you read the entire message. If there were any problems with tasks performed by the Environment Check routine or the POST-INIT routine, they will be explained in this mail message.

If you had any locally added options under the Pharmacy Data Management \[PSS MGR\] menu option or any of its sub-menus, check to see if they need to be re-attached once the POST-INSTALL is complete and the VistA mail message indicating a successful install has been received.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>WARNING:</th>
<th rowspan="2"><p>If you are sure that that your equipment is set up correctly, communications between FDB, Web Services, and VistA should be working correctly. See the next page for steps to verify that this is true.</p>
<p>If you are not sure, you may want to retrace your steps.</p>
<p>If you are completely sure, you may continue to the next step, which is the installation of the Combined Build. There is no turning back at that point.</p></th>
</tr>
<tr class="odd">
<th>![](mocha-version-1-combined-builds-installation-guide-revised-version/005.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Validation of Communication Linkage

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See both the *Check Vendor Database Link* and *PEPS Services Menu and Options* sections of the *VistA to MOCHA Interface Installation Guide* to validate the communication linkage. This is posted on the VDL. Example shown below (3.6.1).

### Check Vendor Database Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run the *PEPS Services Option Menu* \[PSS PEPS SERVICES\] option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Check Vendor Database Link</p>
<p>Check PEPS Services Setup</p>
<p>Schedule/Reschedule Check PEPS Interface</p>
<p>Select PEPS Services Option: <strong>Check Vendor Database Link</strong></p>
<p>Database Version: 6</p>
<p>Build Version: 3.2</p>
<p>Issue Date: 1/23/2011</p>
<p>Custom Database Version: 6</p>
<p>Custom Build Version: 3.2</p>
<p>Custom Issue Date: 1/13/2011</p>
<p>Connected to Vendor database successfully @Jan 23, 2010@14:18</p>
<p>Press Return to Continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If you get the message “Connected to Vendor database successfully …,” it means the connection was successful.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>It is highly recommended that you do a complete system backup before continuing.</p>
<p>Changes made after this point cannot be backed out.</p></th>
</tr>
<tr class="odd">
<th>![](mocha-version-1-combined-builds-installation-guide-revised-version/006.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Schedule/Reschedule Check PEPS Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSS SCHEDULE PEPS INTERFACE CK\]

This option will schedule the Interface Scheduler \[PSS INTERFACE SCHEDULER\] option, which tests the PEPS interface by sending a PING request. If the PEPS Interface is not available, a mail message will be sent to the G.PSS ORDER CHECKS mail group. This must be scheduled so constant monitoring takes place on the Mocha Interface, to provide timely notification of any problems.

| <span id="p5" class="anchor"></span>Note:         | The next paragraph, regarding the POSTMASTER, is only applicable up until the installation of patch PSS\*1\*163. Patch PSS\*1\*163 includes functionality that will replace any Person’s Internal Entry Number in the interface message that is not a whole number with the number 0 because the interface will accept 0 as a valid number. PSS\*1\*163 will also do the same with Job Number and Station Number (after stripping off any non-numeric characters). This conversion will also happen on all Order Check messages. |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide-revised-version/007.png) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

When scheduling this job, the person that is doing the scheduling must not have assumed the identity of the POSTMASTER, because the Internal Entry Number of the POSTMASTER is .5, and the decimal could cause the interface to fail, so this job would continue to fail until it is scheduled by another user other than POSTMASTER.

| IMPORTANT:                                        | A device must be entered in the DEVICE FOR QUEUED JOB OUTPUT field. If a device is not entered, then the job can result in a failure, generating the mail message indicating the Order Check system is not available, when the system really was never unavailable. Most sites have a “NULL” type entry in the DEVICE (#3.5) File, as that is the recommended device, since the tasked job does not write any data. Additionally, it is recommended that “Startup Persistent” be entered in the SPECIAL QUEUING field. This will queue the job to run when­ever the TaskMan/computer is started (i.e., at System Boot), and will restart the task if it stops unexpectedly. If this type of restart does occur, the task could be set by Kernel to be run by POSTMASTER, which as stated in the previous paragraph could cause the job to fail. If this occurs, then someone would need to reschedule the job, with the identity of any user besides POSTMASTER. <span id="p6" class="anchor"></span>Also as stated a few paragraphs earlier, this POSTMASTER issue is resolved by patch PSS\*1\*163, by replacing .5 with a 0 in the interface message. |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide-revised-version/008.png) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

To check the link, start up the *PEPS Services Option Menu* \[PSS PEPS SERVICES\].

Check Vendor Database Link

Check PEPS Services Setup

Schedule/Reschedule Check PEPS Interface

Select PEPS Services Option: Schedule/Reschedule Check PEPS Interface

Edit Option Schedule

Option Name: PSS INTERFACE SCHEDULER

Menu Text: Interface Scheduler TASK ID: 892595

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: JAN 23,2011@14:25:41

DEVICE FOR QUEUED JOB OUTPUT: NULL DEVICE;P-DEC;80;64

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 900S

TASK PARAMETERS:

SPECIAL QUEUEING: Startup Persistent

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

# Installation of Combined Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Software Retrieval for Combined Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Combined Build will be distributed as PRE_I_3_PHARMACY_BUILD.KID and consists of the following patches:

- OR\*3\*272
- PSJ\*5\*181
- PSO\*7\*251

The software will be distributed in a controlled release. Sites will be notified by the Implementation Team how to retrieve the software during their implementation phase.

The software distribution includes: PRE_I_3\_\_PHARMACY_BUILD.KID is a KIDS Build with 2937 blocks.

## Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PSO\*7\*251 Post-Init links the Process Order Checks \[PSO ORDER CHECKS VERIFY\] Option to the Outpatient Pharmacy Manager \[PSO MANAGER\] and Pharmacist Menu \[PSO USER1\] Menu options. It also sends a mail message to the PSS ORDER CHECKS Mail group indicating the install is complete.

| Note:                                             | If your facility has the Pyxis/Omnicell/McKesson interface from ILC, patch PSJ\*5\*181 will overwrite any “local” modifications in routines PSGOEE and PSJCOMR. This could affect certain orders being sent across this interface. The modifications will have to be re-introduced following installation of this patch. |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide-revised-version/009.png) |                                                                                                                                                                                                                                                                                                                          |

Installation takes less than fifteen minutes. This patch should be installed during non-peak requirement hours. It is highly recommended that it be installed when no tasked jobs are running from any Clinical Applications.

## Combined Build Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Retrieve the file PRE_I_3_PHARMACY_BUILD.KID as instructed by the MOCHA v1.0 Implementation Team.
2.  From the Kernel Installation & Distribution System (KIDS) menu, select the Installation menu option.
3.  From the Installation menu, select the Load a Distribution option and select  
    PRE_I_3_PHARMACY_BUILD.KID.
4.  From the Installation menu, select the following options (when prompted for INSTALL NAME, enter PRE_I_3_PHARMACY_BUILD 1.0):

| Note:                                             | The following steps (a – d) are OPTIONAL |
|---------------------------------------------------|------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide-revised-version/010.png) |                                          |

1.  Backup a Transport Global - this option creates a backup message of any routines exported with the patch. It does NOT backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System - this option allows you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - this option ensures the integrity of the routines that are in the transport global.
4.  Print Transport Global - this option allows you to view the components of the KIDS build.
5.  Use the Install Package(s) option and when prompted for INSTALL NAME, enter PRE_I_3_PHARMACY_BUILD 1.0
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", respond NO.
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//", respond NO.

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the KIDS build is installed, a VistA MailMan message is automatically sent to members of the PSS ORDER CHECKS Mail Group as well as the user that installs the patch.

Please verify that the VistA mail message indicating that the POST-INIT has run to completion has been received. If this message is not received, please log a Remedy Ticket. The message subject will be “PSO\*7\*251 Installation Complete.” The message text should be “The Installation of patch PSO\*7.0\*251 is complete.”

The receipt of this VistA mail message will verify that the POST-INIT has run to completion. If there is other information in this mail message concerning post-init failures, please log a remedy ticket.

## Example of Combined Build Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

D ^XQ1

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Select Kernel Installation & Distribution System Option:

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option: INstallation

Select Installation Option:

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

1 Load a Distribution

Enter a Host File: USER\$:\[HFS\]PRE_I_3\_\_PHARMACY_BUILD.KID

KIDS Distribution saved on JAN 13, 2011@10:17:37

Comment: PRE COMBINED BUILD 1/13/11

This Distribution contains Transport Globals for the following Package(s):

PRE_I_3_PHARMACY 1.0

PSO\*7.0\*251

PSJ\*5.0\*181

OR\*3.0\*272

Distribution OK!

*(This page included for two-sided copying.)*

Want to Continue with Load? YES//

Loading Distribution...

PRE_I_3_PHARMACY_BUILD 1.0

PSO\*7.0\*251

PSJ\*5.0\*181

OR\*3.0\*272

Use INSTALL NAME: PRE_I_3_PHARMACY_BUILD 1.0 to install this Distribution.

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

Select Installation Option:

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME:PRE_I_3_PHARMACY_BUILD 1.0 Loaded from Distribution 01/13/11@14:31:03

=\>PRE COMBINED BUILD 01/13/11 ;Created on Jan 13, 2011@10:17:37

This Distribution was loaded on Jan 13, 2011@14:31:03 with header of

PRE COMBINED BUILD 01/13/11 ;Created on Jan 13, 2011@10:17:37

It consisted of the following Install(s):

PRE_I_3_PHARMACY_BUILD 1.0 PSO\*7.0\*251 PSJ\*5.0\*181 OR\*3.0\*272

Checking Install for Package PRE_I_3_PHARMACY_BUILD 1.0

Install Questions for PRE_I_3_PHARMACY_BUILD 1.0

Checking Install for Package PSO\*7.0\*251

Install Questions for PSO\*7.0\*251

Incoming Files:

52 PRESCRIPTION (Partial Definition)

> **NOTE:** You already have the 'PRESCRIPTION' File.

52.4 RX VERIFY (Partial Definition)

> **NOTE:** You already have the 'RX VERIFY' File.

59 OUTPATIENT SITE (Partial Definition)

> **NOTE:** You already have the 'OUTPATIENT SITE' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Checking Install for Package PSJ\*5.0\*181

Install Questions for PSJ\*5.0\*181

Incoming Files:

59.6 INPATIENT WARD PARAMETERS (Partial Definition)

> **NOTE:** You already have the 'INPATIENT WARD PARAMETERS' File.

Checking Install for Package OR\*3.0\*272

Install Questions for OR\*3.0\*272

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// COMPUTER ROOM

Install Started for PRE_I_3_PHARMACY_BUILD 1.0 :

Jan 13, 2011@14:19:46

Build Distribution Date: Jan 13, 2011

Installing Routines:

Jan 13, 2011@14:19:46

Install Started for PSO\*7.0\*251 :

Jan 13, 2011@14:19:46

Build Distribution Date: Jan 13, 2011

Installing Routines:

Jan 13, 2011@14:19:47

Installing Data Dictionaries: .

Jan 13, 2011@14:19:48

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Installing OPTION

Jan 13, 2011@14:19:49

Running Post-Install Routine: ^PSO251PO

Linking PSO ORDER CHECKS VERIFY Option....

All options linked successfully...

Generating Mail Message....

Mail message sent.

Updating Routine file...

The following Routines were created during this install:

PSOXZA

PSOXZA1

PSOXZA10

PSOXZA11

PSOXZA12

PSOXZA13

PSOXZA14

PSOXZA2

PSOXZA3

PSOXZA4

PSOXZA5

PSOXZA6

PSOXZA7

PSOXZA8

PSOXZA9

Updating KIDS files...

PSO\*7.0\*251 Installed.

Jan 13, 2011@14:19:49

Not a production UCI

NO Install Message sent

Install Started for PSJ\*5.0\*181 :

Jan 13, 2011@14:19:49

Build Distribution Date: Jan 13, 2011

Installing Routines:

Jan 13, 2011@14:19:51

Installing Data Dictionaries:

Jan 13, 2011@14:19:51

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE

Installing PROTOCOL

Jan 13, 2011@14:19:51

Updating Routine file...

Updating KIDS files...

PSJ\*5.0\*181 Installed.

Jan 13, 2011@14:19:51

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*272 :

Jan 13, 2011@14:19:51

Build Distribution Date: Jan 13, 2011

Installing Routines:

Jan 13, 2011@14:19:51

Running Post-Install Routine: POST^ORY272

Updating Routine file...

Updating KIDS files...

OR\*3.0\*272



OR\*3.0\*272 Installed.

Jan 13, 2011@14:19:52

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

PRE_I_3_PHARMACY_BUILD 1.0 Installed.

Jan 13, 2011@14:19:52

No link to PACKAGE file

NO Install Message sent

Install Completed

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

You have 81 new messages. (Last arrival: 01/13/11@14:19)

Select Installation Option:

<span id="_Toc287532867" class="anchor"></span>5. Installation of PSO\*7.0\*375 - MOCHA v1.0 add-on patch to PSO\*7.0\*251

<span id="_Toc287532868" class="anchor"></span>5.1 Overview

PSO\*7\*375 is a stand-alone patch. The patch is included within the National Patch Module on FORUM. This patch corrects a number of issues identified during field Production Testing (Stage 3) of the MOCHA v1.0 Combined Build. Please see the patch description in FORUM for details of the issues addressed by this patch.

<span id="_Toc287532869" class="anchor"></span>5.2 Installation Considerations

Patch PSO\*7\*375 should not be installed while Outpatient Pharmacy users are on the system or when Outpatient orders are being entered and signed through Computerized Patient Record System (CPRS). Installation will take no longer than 5 minutes.

<span id="_Toc287532870" class="anchor"></span>5.3 PSO\*7\*375 Installation Steps

1.  Load Transport Global

> Choose the PackMan message containing this patch and invoke the

> INSTALL/CHECK MESSAGE PackMan option.

2.  Start up Kernel Installation and Distribution System (KIDS)

> Start up the Kernel Installation and Distribution System (KIDS) Menu

> \[XPD MAIN\]:

> Edits and Distribution ...

> Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: INStallation

> ---

> Load a Distribution

> Print Transport Global

> Compare Transport Global to Current System

> Verify Checksums in Transport Global

> Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Backup a Transport Global

> Select Installation Option:

6.  Select Installation Option:

| Note:                                         | The following steps are OPTIONAL (When prompted for the INSTALL NAME, enter PSO\*7.0\*375): |
|---------------------------------------------------|---------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide-revised-version/011.png) |                                                                                             |

1.  Backup a Transport Global - This option creates a backup message of any routines exported with this patch. It does not backup any other changes such as Data Dictionaries (DDs) or templates.
4.  Compare Transport Global to Current System - This option allows you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
5.  Verify Checksums in Transport Global - This option allows you to ensure the integrity of the routines that are in the transport global.
7.  Select Installation Option: Install Package(s)

> This is the step to start the installation of this KIDS patch:

1.  Choose the Install Package(s) option to start the patch install and enter "PSO\*7.0\*375" at the INSTALL NAME prompt.
6.  When prompted “Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//”, answer NO.
7.  When prompted “Want KIDS to INHIBIT LOGONs during the install? NO//”, answer NO.
8.  When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//”, answer NO.

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term         | Definition                                                      |
|--------------|-----------------------------------------------------------------|
| API          | Application Programming Interface                               |
| CPRS         | Computerized Patient Record System                              |
| CS           | Controlled Substances                                           |
| DDs          | Data Dictionaries                                               |
| DIF          | Drug Information Framework                                      |
| ETC          | Enhanced Therapeutic Classification                             |
| FDB          | First DataBank                                                  |
| FTP          | File Transfer Protocol                                          |
| GUI          | Graphical User Interface                                        |
| H*<u>e</u>*V | Health*<u>e</u>*Vet                                             |
| HWSC         | Heath*<u>e</u>*Vet Web Services Client                          |
| IRMS         | Information Resources Management Service                        |
| KIDS         | Kernel Installation and Distribution System                     |
| MOCHA        | Medication Order Check Healthcare Application                   |
| MUMPS        | Massachusetts General Hospital Utility Multi-Programming System |
| OI           | Office of Information                                           |
| OS           | Operating System                                                |
| PDM          | Pharmacy Data Management                                        |
| PEPS         | Pharmacy Enterprise Product System                              |
| PMI          | Project Management Institute                                    |
| POC          | Proof of Concept                                                |
| VA           | Department of Veterans Affairs                                  |
| VDL          | VA Software Document Library                                    |
| VISTA        | Veterans Health Information Systems and Technology Architecture |
