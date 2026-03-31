---
consolidated_title: "mocha combined builds installation guide"
app_code: PSO
doc_type: IG
master_source: "MOCHA Version 1 Combined Builds Installation Guide"
master_pub_date: April 2011
consolidated_from: 2 versions
prior_versions:
  - "MOCHA Version 2 Combined Builds Installation Guide"
---

> ![](mocha-version-1-combined-builds-installation-guide/001.png)

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

| Note:                                                                                                               | HWSC 1.0 is a new package that was released on March 2, 2011 as patch XOBW\*1.0. |
|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide/002.png) |                                                                                  |

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

| Note:                                                                                                               | The following steps are OPTIONAL (When prompted for the INSTALL NAME, enter PSS\*1.0\*117): |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide/003.png) |                                                                                             |

1.  Backup a Transport Global - This option creates a backup message of any routines exported with this patch. It does not backup any other changes such as Data Dictionaries (DDs) or templates.
2.  Compare Transport Global to Current System - This option allows you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option allows you to ensure the integrity of the routines that are in the transport global.
3.  Select Installation Option: Install Package(s)

    This is the step to start the installation of this KIDS patch:
1.  Choose the Install Package(s) option to start the patch install and enter "PSS\*1.0\*117" at the INSTALL NAME prompt.

| Note:                                                                                                               | Please note that during the Environment check routine, various messages are displayed, and possibly a prompt to continue or abort install will be displayed. Please see the *Post Installation Instructions* section for more details. |
|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide/004.png) |                                                                                                                                                                                                                                        |

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
<th>![](mocha-version-1-combined-builds-installation-guide/005.png)</th>
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
<th>![](mocha-version-1-combined-builds-installation-guide/006.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Schedule/Reschedule Check PEPS Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[PSS SCHEDULE PEPS INTERFACE CK\]

This option will schedule the Interface Scheduler \[PSS INTERFACE SCHEDULER\] option, which tests the PEPS interface by sending a PING request. If the PEPS Interface is not available, a mail message will be sent to the G.PSS ORDER CHECKS mail group. This must be scheduled so constant monitoring takes place on the Mocha Interface, to provide timely notification of any problems.

| <span id="p5" class="anchor"></span>Note:                                                                           | The next paragraph, regarding the POSTMASTER, is only applicable up until the installation of patch PSS\*1\*163. Patch PSS\*1\*163 includes functionality that will replace any Person’s Internal Entry Number in the interface message that is not a whole number with the number 0 because the interface will accept 0 as a valid number. PSS\*1\*163 will also do the same with Job Number and Station Number (after stripping off any non-numeric characters). This conversion will also happen on all Order Check messages. |
|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide/007.png) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

When scheduling this job, the person that is doing the scheduling must not have assumed the identity of the POSTMASTER, because the Internal Entry Number of the POSTMASTER is .5, and the decimal could cause the interface to fail, so this job would continue to fail until it is scheduled by another user other than POSTMASTER.

| IMPORTANT:                                                                                          | A device must be entered in the DEVICE FOR QUEUED JOB OUTPUT field. If a device is not entered, then the job can result in a failure, generating the mail message indicating the Order Check system is not available, when the system really was never unavailable. Most sites have a “NULL” type entry in the DEVICE (#3.5) File, as that is the recommended device, since the tasked job does not write any data. Additionally, it is recommended that “Startup Persistent” be entered in the SPECIAL QUEUING field. This will queue the job to run when­ever the TaskMan/computer is started (i.e., at System Boot), and will restart the task if it stops unexpectedly. If this type of restart does occur, the task could be set by Kernel to be run by POSTMASTER, which as stated in the previous paragraph could cause the job to fail. If this occurs, then someone would need to reschedule the job, with the identity of any user besides POSTMASTER. <span id="p6" class="anchor"></span>Also as stated a few paragraphs earlier, this POSTMASTER issue is resolved by patch PSS\*1\*163, by replacing .5 with a 0 in the interface message. |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide/008.png) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

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

| Note:                                                                                                               | If your facility has the Pyxis/Omnicell/McKesson interface from ILC, patch PSJ\*5\*181 will overwrite any “local” modifications in routines PSGOEE and PSJCOMR. This could affect certain orders being sent across this interface. The modifications will have to be re-introduced following installation of this patch. |
|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide/009.png) |                                                                                                                                                                                                                                                                                                                          |

Installation takes less than fifteen minutes. This patch should be installed during non-peak requirement hours. It is highly recommended that it be installed when no tasked jobs are running from any Clinical Applications.

## Combined Build Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Retrieve the file PRE_I_3_PHARMACY_BUILD.KID as instructed by the MOCHA v1.0 Implementation Team.
2.  From the Kernel Installation & Distribution System (KIDS) menu, select the Installation menu option.
3.  From the Installation menu, select the Load a Distribution option and select  
    PRE_I_3_PHARMACY_BUILD.KID.
4.  From the Installation menu, select the following options (when prompted for INSTALL NAME, enter PRE_I_3_PHARMACY_BUILD 1.0):

| Note:                                                                                                               | The following steps (a – d) are OPTIONAL |
|---------------------------------------------------------------------------------------------------------------------|------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide/010.png) |                                          |

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

| Note:                                                                                                           | The following steps are OPTIONAL (When prompted for the INSTALL NAME, enter PSO\*7.0\*375): |
|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------|
| ![](mocha-version-1-combined-builds-installation-guide/011.png) |                                                                                             |

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


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MOCHA Version 2 Combined Builds Installation Guide

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download PSS_1_160.KID into your local directory.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File: “, respond with PSS_1_160.KID

> Example: USER\$:\[ABC\]PSS_1_160.KID

4.  If given the option to run any Environment Check Routine(s), answer "YES”.
5.  From this menu, you may then select to use the following options:

| Note:                                             | The following are OPTIONAL - (When prompted for the INSTALL NAME, enter PSS\*1.0\*160) |
|---------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](mocha-version-2-combined-builds-installation-guide/004.png) |                                                                                        |

- Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as Data Dictionaries (DD) or templates.
- Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file PSS_1_160.KID you will see the following warnings on certain routines:</p>
<p><u>PSS*1*160:</u></p>
<p>Routine: PSSHRVL1</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>This warning is due to the sequence of released patches prior to MOCHA v2.0.  Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th>![](mocha-version-2-combined-builds-installation-guide/005.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global - This option will allow you to view the components of the KIDS build.
6.  Select the Installation option Install Package(s). This is the step to start the installation of this KIDS patch:
1.  Choose the Install Package(s) option to start the patch install and enter "PSS\*1.0\*160" at the INSTALL NAME prompt.
2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO
3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO
4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO
7.  Install Example:

Select Installation \<TEST ACCOUNT\> Option:  Load a Distribution

Enter a Host File: ANON\$:\[ANONYMOUS\]PSS_1_160.KID

KIDS Distribution saved on May 03, 2013@14:08:02

Comment: PSS\*1\*160   5/3/13

This Distribution contains Transport Globals for the following Package(s):

Build PSS\*1.0\*160 has been loaded before, here is when:

      PSS\*1.0\*160   Install Completed

                    was loaded on Jan 17, 2013@16:51

      PSS\*1.0\*160   Install Completed

                    was loaded on Jan 25, 2013@09:11:34

      PSS\*1.0\*160   Install Completed

                    was loaded on Feb 14, 2013@14:47:50

      PSS\*1.0\*160   Install Completed

                    was loaded on May 03, 2013@14:45:57

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES// YES

Loading Distribution...

   PSS\*1.0\*160

Use INSTALL NAME: PSS\*1.0\*160 to install this Distribution.

   1      Load a Distribution

   2      Verify Checksums in Transport Global

   3      Print Transport Global

   4      Compare Transport Global to Current System

   5      Backup a Transport Global

   6      Install Package(s)

          Restart Install of Package(s)

          Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME: PSS\*1.0\*160      6/11/13@09:47:12

     =\> PSS\*1\*160 HOST FILE  5/3/13  ;Created on May 03, 2013@14:32:51

This Distribution was loaded on Jun 11, 2013@09:47:12 with header of

   PSS\*1\*160 V13 HOST FILE  5/3/13  ;Created on May 03, 2013@14:32:51

   It consisted of the following Install(s):

    PSS\*1.0\*160

Checking Install for Package PSS\*1.0\*160

Will first run the Environment Check Routine, PSS160EN

Checking for any remaining unmapped Local Medication Routes...

There are still local Medication Routes marked for 'ALL PACKAGES' not yet

mapped. Any orders containing an unmapped medication route will not have

dosage checks performed. Please refer to the 'Medication Route Mapping Report'

option for more details.

Checking for any remaining Local Possible Dosages missing data...

There are still local possible dosages eligible for dosage checks that have

missing data in the Numeric Dose and Dose Unit fields. Any orders containing

such local possible dosages may not have dosage checks performed. Please

refer to the 'Local Possible Dosages Report' option for more details.

Do you want to continue to install this patch? Y// ES

Install Questions for PSS\*1.0\*160

Incoming Files:

   51.1      ADMINISTRATION SCHEDULE  (Partial Definition)

> **NOTE:** You already have the 'ADMINISTRATION SCHEDULE' File.

   51.24     DOSE UNITS  (including data)

> **NOTE:** You already have the 'DOSE UNITS' File.

I will REPLACE your data with mine.

   59.7      PHARMACY SYSTEM  (Partial Definition)

> **NOTE:** You already have the 'PHARMACY SYSTEM' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   SSH VIRTUAL TERMINAL

Install Started for PSS\*1.0\*160 :

               Jun 11, 2013@09:47:41

Build Distribution Date: May 03, 2013

 Installing Routines:

               Jun 11, 2013@09:47:42

 Installing Data Dictionaries: .

               Jun 11, 2013@09:47:43

 Installing Data:

               Jun 11, 2013@09:47:43

 Installing PACKAGE COMPONENTS:

 

 Installing SECURITY KEY

 Installing INPUT TEMPLATE

 Installing OPTION

               Jun 11, 2013@09:47:43

 Running Post-Install Routine: ^PSS160PO

Validating new Dose Unit File (#51.24) entries.

DOSE UNITS File (#51.24) entries are correct.

Linking New PSS DRUG DOSING LOOKUP Option....

New PSS DRUG DOSING LOOKUP option linked successfully...

Linking New PSS TRAILING SPACES REPORT Option....

New PSS TRAILING SPACES REPORT option linked successfully...

Beginning DOSING_INFO Web Service definition for PEPS web server:

 

     DOSING_INFO web service was previously defined.  No action taken.

                                  PSS\*1.0\*160                                   

-------------------------------------------------------------------------------

     DOSING_INFO web service was previously enabled.  No action taken.

Web Service definition process is complete for PEPS web server.

Generating Mail Message....

Mail message sent.

 Updating Routine file...

 Updating KIDS files...

 PSS\*1.0\*160 Installed.

               Jun 11, 2013@09:47:43

 Not a production UCI

 NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

## Post Install Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Verify PSS\*1\*160 Install MAILMAN Message is Received

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please verify that the VistA mail message indicating the POST-INIT has run to completion has been received. If this message is not received, please log a Remedy ticket.

The receipt of this VistA mail message will verify the POST-INIT has run to completion. It is important that you read the entire message. If there were any problems with tasks performed by the Environment Check routine or the POST-INIT routine, they will be explained in this mail message, and some may come with instructions to log a Remedy ticket for assistance.

The message subject will be: PSS\*1\*160 Installation Complete. The message text will begin with: Installation of Patch PSS\*1.0\*160 has been completed!

The following is an example of the install MAILMAN message:

Subj: PSS\*1\*160 Installation Complete \[#154914\] 12/21/12@17:31 16 lines

From: PSS\*1\*160 INSTALL In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Installation of Patch PSS\*1.0\*160 has been completed!

There are still local Medication Routes marked for 'ALL PACKAGES' not yet

mapped. Any orders containing an unmapped medication route will not have

dosage checks performed. Please refer to the 'Medication Route Mapping Report'

option for more details.

There are still local possible dosages eligible for dosage checks that have

missing data in the Numeric Dose and Dose Unit fields. Any orders containing

such local possible dosages may not have dosage checks performed. Please

refer to the 'Local Possible Dosages Report' option for more details.

Beginning DOSING_INFO Web Service definition:

DOSING_INFO web service has been defined.

Web Service definition process is complete.

Enter message action (in IN basket): Ignore//

### Verify Web Services are Enabled

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Log into the WEB SERVER MANAGER \[XOBW WEB SERVER MANAGER\] option, select the EP for EXPAND ENTRY action and select the PEPS web server. If the ORDER_CHECKS, DRUG_INFO and/or DOSING_INFO web service are not defined and enabled, please log a Remedy ticket.

Example:

\>D ^XUP

Setting up programmer environment

This is a TEST account.

Terminal Type set to: C-VT100

You have 619 new messages.

Select OPTION NAME: WEB SERVER MANAGER XOBW WEB SERVER MANAGER Web Server Manager

Web Server Manager

<u>Web Server Manager Jan 10, 2013@17:47:44 Page: 1 of 1</u>

HWSC Web Server Manager

Version: 1.0 Build: 31

<u>ID Web Server Name IP Address or Domain Name:Port</u>

1 \*PEPS xx.x.xxx.x:port#

Legend: \*Enabled

AS Add Server TS (Test Server)

ES Edit Server WS Web Service Manager

DS Delete Server CK Check Web Service Availability

EP Expand Entry LK Lookup Key Manager

Select Action:Quit// EP Expand Entry

Select Web Server: (1-1): 1

===============================================================================

1 \*PEPS xx.x.xxx.xx:port#

-------------------------------------------------------------------------------

NAME: PEPS PORT: nnnn

SERVER: nn.n.nnnn.nn STATUS: ENABLED

DEFAULT HTTP TIMEOUT: 30

WEB SERVICE: ORDER_CHECKS STATUS: ENABLED

WEB SERVICE: DRUG_INFO STATUS: ENABLED

WEB SERVICE: DOSING_INFO STATUS: ENABLED

-------------------------------------------------------------------------------

Lookup keys associated with server:

\<No lookup keys associations\>

===============================================================================

Enter RETURN to continue or '^' to exit:

### Re-Attach any Locally Added Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a follow-up to the installation instructions if you had any locally added options under the *Dosages* \[PSS DOSAGES MANAGEMENT\] menu option, please check to see if they need to be re-attached, once the POST-INSTALL is complete and the VistA mail message indicating this has been received.

## Installation Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download PSS_1_173.KID into your local directory.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for "Enter a Host File:”, respond with PSS_1_173.KID.

> Example: USER\$:\[ABC\]PSS_1_173.KID

4.  If given the option to run any Environment Check Routine(s), answer "YES."
5.  From this menu, you may then select to use the following options:

| Note:                                             | The following are OPTIONAL - (When prompted for the INSTALL NAME, enter PSS\*1.0\*173). |
|---------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](mocha-version-2-combined-builds-installation-guide/006.png) |                                                                                         |

- Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
- Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file PSS_1_173.KID you will see the following warnings on certain routines:</p>
<p><u>PSS*1*173:</u></p>
<p>Routine: PSS551</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>Routine: PSSHRVL1</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p>These warnings are due to the sequence of released patches prior to MOCHA v2.0.  Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th>![](mocha-version-2-combined-builds-installation-guide/007.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
- Print Transport Global - This option will allow you to view the components of the KIDS build.
6.  Select the Installation option Install Package(s). This is the step to start the installation of this KIDS patch:
1.  Choose the Install Package(s) option to start the patch install and enter "PSS\*1.0\*173" at the INSTALL NAME prompt.
2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//' answer NO
3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' answer NO
7.  Install Example:

Select Installation \<TEST ACCOUNT\> Option:  Load a Distribution

Enter a Host File: ANON\$:\[ANONYMOUS\]PSS_1_173.KID

KIDS Distribution saved on May 03, 2013@14:08:02

Comment: PSS\*1\*173   5/3/13

This Distribution contains Transport Globals for the following Package(s):

Build PSS\*1.0\*173 has been loaded before, here is when:

      PSS\*1.0\*173   Install Completed

                    was loaded on Jan 17, 2013@16:51

      PSS\*1.0\*173   Install Completed

                    was loaded on Jan 25, 2013@09:11:34

      PSS\*1.0\*173   Install Completed

                    was loaded on Feb 14, 2013@14:47:50

      PSS\*1.0\*173   Install Completed

                    was loaded on May 03, 2013@14:45:57

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES// YES

Loading Distribution...

   PSS\*1.0\*173

Use INSTALL NAME: PSS\*1.0\*173 to install this Distribution.

   1      Load a Distribution

   2      Verify Checksums in Transport Global

   3      Print Transport Global

   4      Compare Transport Global to Current System

   5      Backup a Transport Global

   6      Install Package(s)

          Restart Install of Package(s)

          Unload a Distribution

You have PENDING ALERTS

          Enter  "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME:    PSS\*1.0\*173    6/11/13@09:51:54

     =\> PSS\*1\*173 V8  5/3/13  ;Created on May 03, 2013@14:08:02

This Distribution was loaded on Jun 11, 2013@09:51:54 with header of

   PSS\*1\*173 V8  5/3/13  ;Created on May 03, 2013@14:08:02

   It consisted of the following Install(s):

    PSS\*1.0\*173

Checking Install for Package PSS\*1.0\*173

Install Questions for PSS\*1.0\*173

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   SSH VIRTUAL TERMINAL

                                  PSS\*1.0\*173                                  

-------------------------------------------------------------------------------

Install Started for PSS\*1.0\*173 :

               Jun 11, 2013@09:52:06

Build Distribution Date: May 03, 2013

 Installing Routines:

               Jun 11, 2013@09:52:06

 Updating Routine file...

 Updating KIDS files...

 PSS\*1.0\*173 Installed.

               Jun 11, 2013@09:52:06

 Not a production UCI

 NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download MOCHA_2_0.KID into your local directory.
2.  From the Kernel Installation & Distribution System (KIDS) menu, select Installation.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for "Enter a Host File:" respond with MOCHA_2_0.KID.

> Example: USER\$:\[ABC\]MOCHA_2_0.KID

4.  From the KIDS menu, select Installation.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2">The following are OPTIONAL - (When prompted for the INSTALL NAME, enter MOCHA 2.0 Combined Build 1.0)</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-combined-builds-installation-guide/009.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as Data Dictionaries or templates.
2.  Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, data dictionaries (DD), templates, etc.).

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file MOCHA_2_0.KID you will see the following warnings on certain routines:</p>
<p>Host file: MOCHA_2_0.KID contains: PSO*7*372, PSJ*5*252, and OR*3*345</p>
<p><u>PSO*7*372:</u></p>
<p>Routine: PSOCAN</p>
<p>* WARNING, your routine has more patches than the incoming routine *</p>
<p>Routine: PSOCAN2, PSODDPR2, PSODDPR4, PSODDPR5, PSODDPRE, PSOORED3, PSOORED5, PSOORNEW, PSORXEDT, PSOVER1</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p><u>PSJ*5*252:</u></p>
<p>Routine: PSJBLDOC</p>
<p>* WARNING, your routine has more patches than the incoming routine *</p>
<p>Routine: PSJGMRA, PSJOC, PSJOCDI</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p><u>OR*3*345:</u></p>
<p>Routine: ORCHECK, ORDSGCHK, ORKPS1</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>Routine: ORWDXR01</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p>These warnings are due to the sequence of released patches prior to MOCHA v2.0. Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-combined-builds-installation-guide/010.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
4.  Print Transport Global - this option will allow you to view the components of the KIDS build.
5.  Use the Install Package(s) option and select the package MOCHA 2.0 Combined Build 1.0.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond NO.
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.
8.  Install Example:

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME:    MOCHA 2.0 Combined Build 1.0    6/11/13@09:54

     =\> MOCHA 2.0   10/10/12  ;Created on Oct 10, 2012@15:15:20

This Distribution was loaded on Jun 11, 2013@09:54 with header of

   MOCHA 2.0 T10  10/10/12  ;Created on Oct 10, 2012@15:15:20

   It consisted of the following Install(s):

MOCHA 2.0 Combined Build 1.0    PSO\*7.0\*372    PSJ\*5.0\*252     OR\*3.0\*345

Checking Install for Package MOCHA 2.0 Combined Build 1.0

Install Questions for MOCHA 2.0 Combined Build 1.0

Checking Install for Package PSO\*7.0\*372

Install Questions for PSO\*7.0\*372

Incoming Files:

   52.4      RX VERIFY  (Partial Definition)

> **NOTE:** You already have the 'RX VERIFY' File.

Checking Install for Package PSJ\*5.0\*252

Install Questions for PSJ\*5.0\*252

Checking Install for Package OR\*3.0\*345

Install Questions for OR\*3.0\*345

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   SSH VIRTUAL TERMINAL

Install Started for MOCHA 2.0 Combined Build 1.0 :

               Jun 11, 2013@09:54:29

Build Distribution Date: Oct 10, 2012

 Installing Routines:

               Jun 11, 2013@09:54:29

 Install Started for PSO\*7.0\*372 :

               Jun 11, 2013@09:54:29

Build Distribution Date: Oct 10, 2012

 Installing Routines:

               Jun 11, 2013@09:54:30

 Installing Data Dictionaries:

               Jun 11, 2013@09:54:30

 Updating Routine file...

 Updating KIDS files...

 PSO\*7.0\*372 Installed.

               Jun 11, 2013@09:54:31

 Not a production UCI

 NO Install Message sent

 

 Install Started for PSJ\*5.0\*252 :

               Jun 11, 2013@09:54:31

Build Distribution Date: Oct 10, 2012

 Installing Routines:

               Jun 11, 2013@09:54:31

 Updating Routine file...

 Updating KIDS files...

 PSJ\*5.0\*252 Installed.

               Jun 11, 2013@09:54:32

 Not a production UCI

 NO Install Message sent

 

 Install Started for OR\*3.0\*345 :

               Jun 11, 2013@09:54:32

Build Distribution Date: Oct 10, 2012

 Installing Routines:

               Jun 11, 2013@09:54:32

 Updating Routine file...

 Updating KIDS files...

                                   OR\*3.0\*345                                  

-------------------------------------------------------------------------------

 OR\*3.0\*345 Installed.

               Jun 11, 2013@09:54:32

 Not a production UCI

 NO Install Message sent

 

 Updating Routine file...

 Updating KIDS files...

 MOCHA 2.0 Combined Build 1.0 Installed.

               Jun 11, 2013@09:54:32

 No link to PACKAGE file

 NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID into your local directory.
2.  From the Kernel Installation & Distribution System (KIDS) menu, select Installation.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File: “, respond with MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID

> Example: USER\$:\[ABC\]MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID

4.  From the KIDS menu, select Installation.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2">The following are OPTIONAL - (When prompted for the INSTALL NAME, enter MOCHA 2.0 FOLLOW UP BUILD Combined Build 1.0). Refer to the note on page 3 for an explanation on the ‘before’ checksum inconsistencies with patch OR*3*311.</th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-combined-builds-installation-guide/012.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as Data Dictionaries or templates.
2.  Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, data dictionaries (DD), templates, etc.).

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD you will see the following warnings on certain routines:</p>
<p>Host file: MOCHA_2_0_FOLLOW_UP_COMBINED_BUILD.KID contains: PSO*7*416, PSJ*5*257, GMRA*4*47, and OR*3*311</p>
<p><u>PSO*7*416:</u></p>
<p>Routine: PSOCAN, PSOCAN2, PSODDPR2, PSODDPR4, PSODDPR5, PSODDPRE, PSOORED3, PSOORED5, PSOORNEW, PSORXEDT, PSOVER1</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p><u>PSJ*5*257:</u></p>
<p>Routine: PSIVORFB</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>Routine: PSJBLDOC, PSJGMRA, PSJOC, PSJOCDI, PSJOEA2</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p><u>OR*3*311:</u></p>
<p>Routine: ORCHECK, ORDSGCHK, ORKPS1</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p>Routine: ORCMED</p>
<p>* WARNING, your routine has more patches than the incoming routine *</p>
<p>Routine: ORWDXR01</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>These warnings are due to the sequence of released patches prior to MOCHA v2.0. Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-combined-builds-installation-guide/013.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
4.  Print Transport Global - this option will allow you to view the components of the KIDS build.
5.  Use the Install Package(s) option and select the package MOCHA 2.0 FOLLOW UP Combined Build 1.0.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond "NO".
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond "YES".
1.  When prompted "Enter options you wish to mark as 'Out Of Order':", select the following option: Allergy clean up utility \[GMRA FREE TEXT UTILITY\].
2.  When prompted "Enter protocols you wish to mark as 'Out Of Order':", press Enter.
8.  If prompted "Delay Install (Minutes): (0 - 60): 0//", respond 0.
9.  Example of Install:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>Where it is shown that the background job is queued, there is a typographical error for the patch number (PSJ*5*297), which should have stated PSJ*5*257. The correct background job is queued.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-combined-builds-installation-guide/014.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

Select INSTALL NAME: MOCHA 2.0 FOLLOW UP Combined Build 1.0 7/1/13@14:15:09

=\> MOCHA 2.0 Follow Up Combined Build ;Created on Jul 01, 2013@14:13

This Distribution was loaded on Jul 01, 2013@14:15:09 with header of

MOCHA 2.0 Follow Up Combined Build v12 ;Created on Jul 01, 2013@14:13:47

It consisted of the following Install(s):

MOCHA 2.0 FOLLOW UP Combined Build 1.0 PSJ\*5.0\*257 PSO\*7.0\*416

GMRA\*4.0\*47 OR\*3.0\*311

Checking Install for Package MOCHA 2.0 FOLLOW UP Combined Build 1.0

Install Questions for MOCHA 2.0 FOLLOW UP Combined Build 1.0

Checking Install for Package PSJ\*5.0\*257

Install Questions for PSJ\*5.0\*257

Incoming Files:

53.1 NON-VERIFIED ORDERS (Partial Definition)

> **NOTE:** You already have the 'NON-VERIFIED ORDERS' File.

53.46 CLINIC DEFINITION (Partial Definition)

> **NOTE:** You already have the 'CLINIC DEFINITION' File.

55 PHARMACY PATIENT (Partial Definition)

> **NOTE:** You already have the 'PHARMACY PATIENT' File.

Checking Install for Package PSO\*7.0\*416

Install Questions for PSO\*7.0\*416

Checking Install for Package GMRA\*4.0\*47

Install Questions for GMRA\*4.0\*47

Checking Install for Package OR\*3.0\*311

Install Questions for OR\*3.0\*311

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TERMINAL

Install Started for MOCHA 2.0 FOLLOW UP Combined Build 1.0 :

Jul 01, 2013@14:17:01

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:01

Install Started for PSJ\*5.0\*257 :

Jul 01, 2013@14:17:01

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:02

Installing Data Dictionaries: .

Jul 01, 2013@14:17:05

Running Post-Install Routine: ^PSJ257PO

=============================================================

Queuing background job for PSJ\*5\*297 Post Install...

Start time: Jul 01, 2013@14:17:05

A MailMan message will be sent to the installer upon Post

Install Completion. This may take 2-3 hours.

==============================================================

\*\*\* Task \#3364273 Queued! \*\*\*

Updating Routine file...

The following Routines were created during this install:

PSGXR3

PSGXR31

PSGXR310

PSGXR311

PSGXR312

PSGXR313

PSGXR314

PSGXR32

PSGXR33

PSGXR34

PSGXR35

PSGXR36

PSGXR37

PSGXR38

PSGXR39

PSSJXR

PSSJXR1

PSSJXR10

PSSJXR11

PSSJXR12

PSSJXR13

PSSJXR14

PSSJXR15

PSSJXR16

PSSJXR17

PSSJXR18

PSSJXR19

PSSJXR2

PSSJXR20

PSSJXR21

PSSJXR22

PSSJXR23

PSSJXR24

PSSJXR25

PSSJXR26

PSSJXR27

PSSJXR28

PSSJXR29

PSSJXR3

PSSJXR30

PSSJXR31

PSSJXR32

PSSJXR33

PSSJXR34

PSSJXR4

PSSJXR5

PSSJXR6

PSSJXR7

PSSJXR8

PSSJXR9

Updating KIDS files...

PSJ\*5.0\*257 Installed.

Jul 01, 2013@14:17:06

Not a production UCI

NO Install Message sent

Install Started for PSO\*7.0\*416 :

Jul 01, 2013@14:17:06

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:07

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*416 Installed.

Jul 01, 2013@14:17:07

Not a production UCI

NO Install Message sent

Install Started for GMRA\*4.0\*47 :

Jul 01, 2013@14:17:07

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:07

Updating Routine file...

Updating KIDS files...

GMRA\*4.0\*47 Installed.

Jul 01, 2013@14:17:07

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*311 :

Jul 01, 2013@14:17:07

Build Distribution Date: Jul 01, 2013

Installing Routines:

Jul 01, 2013@14:17:08

Running Post-Install Routine: POST^ORY311

Setting the dosage order check to mandatory...

DONE

Updating Routine file...

Updating KIDS files...

OR\*3.0\*311

-------------------------------------------------------------------------------

OR\*3.0\*311 Installed.

Jul 01, 2013@14:17:08

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

MOCHA 2.0 FOLLOW UP Combined Build 1.0 Installed.

Jul 01, 2013@14:17:08

No link to PACKAGE file

NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

## Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Verify Post Install MAILMAN Message is Received

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation, the Inpatient Medications patch queues a post install routine (PSJ257PO) that creates new cross references for NON-VERIFIED ORDERS file (#53.1) and PHARMACY PATIENT file (#55). Depending on the size of your facility, this post install can take up to three hours to run. Upon completion the following message will be sent to the patch installer.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>In the subject line of the email, there is a typographical error for the patch number (PSJ*5*297) which should have stated PSJ*5*257. The message is otherwise correct.</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-combined-builds-installation-guide/015.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Subj: Background job for PSJ\*5\*297 Post Install \[#179515\] 07/01/13@14:17

7 lines

From: INPT PHARMACY In 'IN' basket. Page 1

-------------------------------------------------------------------------------

The new cross references for clinic orders have been created:

File 53.1 - CIMO

File 55 - CIMOU and CIMOCLU for Unit Dose Sub-file.

File 55 - CIMOI AND CIMOCLI for IV Sub-file.

The background job 3364273 began Jul 01, 2013@14:17:06 and

ended Jul 01, 2013@14:17:08.

Enter message action (in IN basket): Ignore//

## Installation Steps 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download OR_3_381.KID into your local directory.
2.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File: “, respond with OR_3_381.

> Example: USER\$:\[ABC\]OR_3_381.KID

4.  From the KIDS menu, select Installation.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>The following are OPTIONAL - (When prompted for the INSTALL NAME, enter OR*3.0*381).</p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-combined-builds-installation-guide/016.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Note:</p>
</blockquote></th>
<th rowspan="2"><blockquote>
<p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file OR_3_381.KID you will see the following warnings on certain routines:</p>
<p><u>OR*3*381:</u></p>
<p>Routine: ORCMED</p>
<p>* WARNING, you are missing one or more Patches *</p>
</blockquote>
<p>This warning is due to the sequence of released patches prior to MOCHA v2.0. Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>![](mocha-version-2-combined-builds-installation-guide/017.png)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  Print Transport Global - This option will allow you to view the components of the KIDS build.
5.  From the Installation Menu, select the Install Package(s) option and choose OR\*3.0\*381 to install.
6.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.
9.  The following is an example of install:

OR\*3\*381 T3

Select Installation \<TEST ACCOUNT\> Option: LOAD a Distribution

Enter a Host File: VA4\$:\[ANONYMOUS.ANONYMOUS\]OR_30_381_TEST_V3.KID;1

KIDS Distribution saved on Sep 30, 2013@06:34:44

Comment: OR\*3\*381 TEST V3

This Distribution contains Transport Globals for the following Package(s):

Build OR\*3.0\*381 has been loaded before, here is when:

OR\*3.0\*381 Install Completed

was loaded on Sep 20, 2013@16:48:04

OR\*3.0\*381 Install Completed

was loaded on Sep 27, 2013@16:25:14

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

OR\*3.0\*381

Use INSTALL NAME: OR\*3.0\*381 to install this Distribution.

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Installation \<TEST ACCOUNT\> Option: INStall Package(s)

Select INSTALL NAME: OR\*3.0\*381 9/30/13@11:03:08

=\> OR\*3\*381 TEST V3 ;Created on Sep 30, 2013@06:34:44

This Distribution was loaded on Sep 30, 2013@11:03:08 with header of

OR\*3\*381 TEST V3 ;Created on Sep 30, 2013@06:34:44

It consisted of the following Install(s):

OR\*3.0\*381

Checking Install for Package OR\*3.0\*381

Install Questions for OR\*3.0\*381

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// SSH VIRTUAL TERMINAL

OR\*3.0\*381

--------------------------------------------------------------------------------

Install Started for OR\*3.0\*381 :

Sep 30, 2013@11:03:46

Build Distribution Date: Sep 30, 2013

Installing Routines:

Sep 30, 2013@11:03:46

Updating Routine file...

Updating KIDS files...

OR\*3.0\*381 Installed.

Sep 30, 2013@11:03:46

Not a production UCI

NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

You have PENDING ALERTS

Enter "VA to jump to VIEW ALERTS option

You've got PRIORITY mail!

Select Installation \<TEST ACCOUNT\> Option:

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Download MOCHA_2_0_FAST_TRACK_BUILDS.KID into your local directory.
2.  From the Kernel Installation & Distribution System (KIDS) menu, select Installation.
3.  Use Load a Distribution. You may need to prepend a directory name. When prompted for “Enter a Host File: “, respond with MOCHA_2_0_FAST_TRACK_BUILDS.KID.

> Example: USER\$:\[ABC\]MOCHA_2_0_FAST_TRACK_BUILDS.KID

4.  From the KIDS menu, select Installation.
1.  Backup a Transport Global - this option will create a backup message of any routines exported with the patch. It will NOT backup any other changes such as Data Dictionaries or templates.
2.  Compare Transport Global to Current System - this option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, data dictionaries (DD), templates, etc.).

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>When using the option Compare Transport Global to Current System [XPD COMPARE TO SYSTEM] with the host file MOCHA_2_0_FAST_TRACK_BUILDS you will see the following warnings on certain routines:</p>
<p>Host file: MOCHA_2_0_FAST_TRACK_BUILDS.KID contains: PSO*7*431, PSJ*5*299</p>
<p><u>PSJ*5*299:</u></p>
<p>Routine: PSIVORFB</p>
<p>* WARNING, you are missing one or more Patches *</p>
<p>Routine: PSJLIACT</p>
<p>* WARNING, your routine has different patches than the incoming routine *</p>
<p>These warnings are due to the sequence of released patches prior to MOCHA v2.0.  Once all the MOCHA v2.0 patches are installed, the second lines of the routines will be updated appropriately.</p></th>
</tr>
<tr class="odd">
<th>![](mocha-version-2-combined-builds-installation-guide/019.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Verify Checksums in Transport Global - this option will ensure the integrity of the routines that are in the transport global.
4.  Print Transport Global - this option will allow you to view the components of the KIDS build.
5.  Use the Install Package(s) option and select the package MOCHA 2.0 FAST TRACK Builds 1.0.
6.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond "NO".
7.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond "NO".
8.  If prompted "Delay Install (Minutes): (0 - 60): 0//", respond 0.
9.  The following is an example of install:

Select Installation \<TEST ACCOUNT\> Option: 6  Install Package(s)

Select INSTALL NAME:    MOCHA 2.0 FAST TRACK BUILDS 1.0    2/12/14@15:40:50

     =\> MOCHA 2.0 FAST TRACK BUILDS V4  ;Created on Feb 12, 2014@15:39:13

This Distribution was loaded on Feb 12, 2014@15:40:50 with header of

   MOCHA 2.0 FAST TRACK BUILDS V4  ;Created on Feb 12, 2014@15:39:13

   It consisted of the following Install(s):

MOCHA 2.0 FAST TRACK BUILDS 1.0    PSJ\*5.0\*299    PSO\*7.0\*431

Checking Install for Package MOCHA 2.0 FAST TRACK BUILDS 1.0

Install Questions for MOCHA 2.0 FAST TRACK BUILDS 1.0

Checking Install for Package PSJ\*5.0\*299

Install Questions for PSJ\*5.0\*299

Checking Install for Package PSO\*7.0\*431

Install Questions for PSO\*7.0\*431

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME//   SSH VIRTUAL TERMINAL

Install Started for MOCHA 2.0 FAST TRACK BUILDS 1.0 :

               Feb 12, 2014@15:42:16

Build Distribution Date: Feb 12, 2014

 Installing Routines:

               Feb 12, 2014@15:42:16

 Install Started for PSJ\*5.0\*299 :

               Feb 12, 2014@15:42:16

Build Distribution Date: Feb 12, 2014

 Installing Routines:

               Feb 12, 2014@15:42:16

 Running Post-Install Routine: ^PSJ299PO

=============================================================

Queuing background job for PSJ\*5\*299 Post Install...

Start time: Feb 12, 2014@15:42:16

A MailMan message will be sent to the installer upon Post

Install Completion.  This may take 2-3 hours.

==============================================================

\*\*\* Task \#12305 Queued! \*\*\*

\*\*\* Task \#12305 Queued! \*\*\*

 Updating Routine file...

 Updating KIDS files...

 PSJ\*5.0\*299 Installed.

               Feb 12, 2014@15:42:16

 Not a production UCI

 NO Install Message sent

 

 Install Started for PSO\*7.0\*431 :

               Feb 12, 2014@15:42:16

Build Distribution Date: Feb 12, 2014

 Installing Routines:

               Feb 12, 2014@15:42:16

 Updating Routine file...

 Updating KIDS files...

PSO\*7.0\*431

--------------------------------------------------------------------------------

 PSO\*7.0\*431 Installed.

               Feb 12, 2014@15:42:16

 Not a production UCI

 NO Install Message sent

 

 Updating Routine file...

 Updating KIDS files...

 MOCHA 2.0 FAST TRACK BUILDS 1.0 Installed.

               Feb 12, 2014@15:42:16

 No link to PACKAGE file

NO Install Message sent

--------------------------------------------------------------------------------

+------------------------------------------------------------+

100% ¦ 25 50 75 ¦

Complete +------------------------------------------------------------+

Install Completed

## Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log onto VistA and navigate to Patient Prescription Processing option.
2.  Select a Test Patient and place an order where the dosage will exceed the maximum daily dose.
3.  Navigate to the Inpatient Order Entry option and place an order where the dosage will exceed the maximum daily dose.
4.  The following is an example of the order check if 120 milligrams are ordered for Simvastatin.

SIMVASTATIN 40MG TAB: Single dose amount of 120 MILLIGRAMS exceeds the

maximum single dose amount of 80 MILLIGRAMS.

Do you want to Continue? Y//

If the dosing checks are not displayed, please log a Remedy ticket.

1.  <span id="_Toc287867276" class="anchor"></span>Appendix: Acronyms

| Term  | Definition                                                      |
|-------|-----------------------------------------------------------------|
| ADPAC | Automated Data Processing Application Coordinator               |
| CPRS  | Computerized Patient Record System                              |
| DD    | Data Dictionaries                                               |
| FDB   | First Databank                                                  |
| FTP   | File Transfer Protocol                                          |
| HWSC  | Heath*<u>e</u>*Vet Web Services Client                          |
| IRMS  | Information Resources Management Service                        |
| KIDS  | Kernel Installation and Distribution System                     |
| MOCHA | Medication Order Check Healthcare Application                   |
| MUMPS | Massachusetts General Hospital Utility Multi-Programming System |
| NDF   | National Drug File                                              |
| PDM   | Pharmacy Data Management                                        |
| PECS  | Pharmacy Enterprise Customization System                        |
| PEPS  | Pharmacy Enterprise Product System                              |
| PMI   | Patient Medication Information                                  |
| VA    | Department of Veterans Affairs                                  |
| VDL   | VA Software Document Library                                    |
| VISTA | Veterans Health Information Systems and Technology Architecture |
