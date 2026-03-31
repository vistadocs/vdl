---
title: TIU*1*309 Deployment Installation BackOut Rollback Guide_r
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Deployment Installation BackOut Rollback Guide_r
app_code: TIU
app_name: "CPRS: Text Integration Utility"
section: CLI
app_status: active
pkg_ns: TIU
patch_ver: 1
patch_id: TIU*1*309
group_key: "TIU:TIU:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - patch
  - installation
  - back
  - deployment
  - rollback
  - procedure
  - local
  - install
page_count: 0
word_count: 3859
section_count: 31
table_count: 3
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiu_1_0_309_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Text_Integration_Utility_(TIU)/tiu_1_0_309_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=65"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Collaborative Terminology Tooling & Data Management (CTT&DM)

  Native Domain Standardization (NDS)

  Text Integration Utility (TIU)

  Deployment, Installation, Back-Out, and Rollback Guide

  TIU\*1.0\*309
---

![](tiu-1-309-deployment-installation-backout-rollback-guide-r/001.png)

April, 2017

Office of Information and Technology (OI&T)

Revision History

<table>
<caption><p>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 38%" />
<col style="width: 33%" />
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
<td>04/28/2017</td>
<td>1.0</td>
<td>Delivery to VA</td>
<td>Management, ManTech Mission Solutions &amp; Services Group</td>
</tr>
<tr class="even">
<td>03/15/2017</td>
<td>0.6</td>
<td>Technical Writer Review</td>
<td><mark>REDACTED</mark>, ManTech Mission Solutions &amp; Services Group</td>
</tr>
<tr class="odd">
<td>03/15/2017</td>
<td>0.5</td>
<td>Updated test sites. Updated pre-install patch instructions.</td>
<td><p><mark>REDACTED</mark>, Mantech</p>
<p>Mission Solutions &amp; Services Group</p></td>
</tr>
<tr class="even">
<td>01/30/2017</td>
<td>0.4</td>
<td>Added Patch number to Title Page, corrected fragments in Installation and Back-out sections.</td>
<td><mark>REDACTED</mark> Mantech Mission Solutions &amp; Services Group</td>
</tr>
<tr class="odd">
<td>01/01/2017</td>
<td>0.3</td>
<td>Updated Back-out section numbering.</td>
<td><mark>REDACTED</mark>, Mantech Mission Solutions &amp; Services Group</td>
</tr>
<tr class="even">
<td>12/21/2016</td>
<td>0.2</td>
<td>Technical Writer Review</td>
<td><mark>REDACTED</mark>, ManTech Mission Solutions &amp; Services Group</td>
</tr>
<tr class="odd">
<td>12/05/2016</td>
<td>0.1</td>
<td>Initial Draft</td>
<td><mark>REDACTED</mark>, ManTech Mission Solutions &amp; Services Group</td>
</tr>
</tbody>
</table>

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Timeline](#timeline)
  - [Site Readiness Assessment](#site-readiness-assessment)
    - [Deployment Topology (Targeted Architecture)](#deployment-topology-targeted-architecture)
    - [Site Information (Locations, Deployment Recipients)](#site-information-locations-deployment-recipients)
    - [Site Preparation](#site-preparation)
  - [Resources](#resources)
    - [Facility Specifics](#facility-specifics)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install TIU Native Domain Standardization patch TIU\*1.0\*309, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the TIU Native Domain Standardization patch TIU\*1.0\*309 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TIU Native Domain Standardization patch TIU\*1.0\*309 possesses a direct application dependency on the VistA Text Integration Utility (TIU) v.1.0 application, and an indirect application dependency on Computerized Patient Record System (CPRS) v.1.0.

The TIU Native Domain Standardization patch TIU\*1.0\*309 possesses a specific patch dependency on Kernel patch XU\*8.0\*675.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TIU Native Domain Standardization patch TIU\*1.0\*309 possesses the following constraints:

- The update to the VistA package file \#8926.1 shall not affect the current functionality or conflict with applications that utilize these files.
- The field being added to these files should only be visible on the back end and to those requesting the information, not the GUI applications used by clinicians within the VA.
- There is a need to map the active VA Standard Titles within the TIU VHA Enterprise Standard Title (#8926.1) file to their corresponding LOINC DO codes by means of a third party mapping team prior to implementing any data within this file.
- The data for the VistA package file (#8926.1) file has previously been mapped in a prior effort and is ready for implementation after a final review from the third party mapping team.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                    | Phase / Role                      | Tasks                                                                                                               | Project Phase (See Schedule) |
|-----|-------------------------|-----------------------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------|
|     | OIT Regional Support    | Deployment                        | Plan and schedule deployment (including orchestration with vendors)                                                 |                              |
|     | CTT&DM NDS Project Team | Deployment                        | Determine and document the roles and responsibilities of those involved in the deployment.                          |                              |
|     | OIT Regional Support    | Deployment                        | Test for operational readiness                                                                                      |                              |
|     | OIT Regional Support    | Deployment                        | Execute deployment                                                                                                  |                              |
|     | OIT Regional Support    | Installation                      | Plan and schedule installation                                                                                      |                              |
|     | CTT&DM NDS Project Team | Installations                     | Coordinate training                                                                                                 |                              |
|     | OIT Regional Support    | Back-out                          | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |                              |
|     | CTT&DM NDS Project Team | Post Deployment – Warranty Period | Hardware, Software and System Support                                                                               |                              |
|     | OIT Reginal Support     | Post Deployment – Post Warranty   | Hardware, Software and System Support                                                                               |                              |

Table 2: Software Specifications

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a concurrent online rollout. During IOC testing and after national release, patch TIU\*1.0\*309 will be distributed via the FORUM Patch Module, and may be deployed at any site without regard to deployment status at other sites.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for a period of thirty days, as depicted in the master deployment schedule

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the CTT&DM NDS patch TIU\*1.0\*309 deployment.

The TIU\*1.0\*309 patch must be manually installed, or manually queued for installation, at each VistA instance at which it is deployed, using the standard Kernel Installation Distribution System (KIDS) software. The TIU\*1.0\*309 patch should be installed at all VA VistA instances running the CPRS and TIU applications, and will update the M (Mumps) server software in each VistA instance’s TIU namespace.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment topology for the CTT&DM NDS patch TIU\*1.0\*309, during IOC testing and after national release, is described below:

Figure 1: Patch TIU\*1.0\*309 Topology

![](tiu-1-309-deployment-installation-backout-rollback-guide-r/002.png)

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During IOC testing, CTT&DM NDS patch TIU\*1.0\*309 will be deployed at the following sites:

NEW YORK HARBOR HCS

PALO ALTO HCS

After national release, CTT&DM NDS patch TIU\*1.0\*309 will be deployed at all sites running the CPRS and TIU applications.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special preparation is required by the site prior to deployment.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment of CTT&DM NDS patch TIU\*1.0\*309 requires an up to date VistA environment running the CPRS v.1.0, TIU v.1.0, and Kernel v.8.0 applications, as well as a Health Product Support (HPS) team member available to perform the patch installation.

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific deployment or installation features of CTT&DM NDS patch TIU\*1.0\*309.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT&DM NDS patch TIU\*1.0\*309 requires no site hardware specifications during, or prior to, deployment.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software         | Make | Version | Configuration | Manufacturer | Other |
|---------------------------|------|---------|---------------|--------------|-------|
| CPRS                      |      | 1.0     | Standard      | VHA          |       |
| TIU                       |      | 1.0     | Standard      | VHA          |       |
| Kernel patch XU\*8.0\*675 |      | 8.0     | Standard      | VHA          |       |

Table 3: Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No notifications are required for deployment of CTT&DM NDS patch TIU\*1.0\*309.

#### Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre/Post Installation Overview:

It is recommended that a Local Patch Backup is created that can be re-installed in the event that patch TIU\*1.0\*309 must be backed out. The approximate time to create the saved local patch is 30 minutes.

<u>Patch Dependencies</u>

Patch XU\*8.0\*675 must be installed prior to installing this patch.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

Pre-Installation Instructions:

<span id="_Ref456812812" class="anchor"></span>Creating a Local Patch Backup

Perform the following procedure to create a Local Patch Backup.

1.  From the KIDS (Kernel Installation & Distribution System) Menu, select ‘Edits and Distribution’.
2.  Select ‘Create a Build Using Namespace’.
3.  Enter a local patch name and identifier; (for example: ZTIU\*1.0\*309).
4.  When prompted ‘BUILD PACKAGE FILE LINK:’, press \<Enter\>.
5.  When prompted ‘BUILD TYPE: SINGLE PACKAGE//’, press \<Enter\>.
6.  When prompted ‘BUILD TRACK PACKAGE NATIONALLY: YES//’, enter NO.
7.  When prompted ‘Namespace:’, press \<Enter\>.
8.  When prompted ‘Select Edits and Distribution Option’, select: ‘Edit a Build’.
9.  Enter the local patch name from step 3 (Ex: ZTIU\*1.0\*309).
10. For the ‘Description:’ enter the following: “this is a local backup for TIU\*1.0\*309. This patch should only be installed in the event that TIU\*1.0\*309 needs to be backed out.”
11. In the ‘COMMAND:’ field, enter ‘Next Page’.
12. For ‘File List’ Enter 8926.1 for TIU VHA ENTERPRISE STANDARD TITLE File.
13. In ‘Send Full or Partial DD’ field, enter PARTIAL.
14. In ‘Data Dictionary Number:’ window, enter 8926.1 for TIU VHA ENTERPRISE STANDARD TITLE File.
    1.  At the prompt, “Are you adding 'TIU VHA ENTERPRISE STANDARD TITLE (File-top level)' as a new DD NUMBER? No//”, enter YES.
15. Field Number: press \<Enter\>.
16. In the ‘COMMAND:’ enter ‘Close’
17. In the first blank text line in the ‘Data Dictionary Number:’ window (below the TIU VHA ENTERPRISE STANDARD TITLE entry), enter 8926.12 for the sub-file representing the CODING SYSTEM multiple.
    1.  If the sub-file is not selectable, continue to the next step.
    2.  Are you adding 'CODING SYSTEM (sub-file)' as a new DD NUMBER? No//, enter YES.
18. In the ‘Field Number:’ window, tab or arrow down to the ‘COMMAND:’ prompt and enter Close.
19. At ‘COMMAND:’ (for the Data Dictionary Number window) enter ‘Close’
20. The ‘DD Export Options’ window should display.
21. In the ‘Update the Data Dictionary:’ field, enter YES.
22. In the ‘Send Security Code:’ field, enter YES.
23. In the ‘Data Comes With File:’ field, enter NO.
24. In the ‘COMMAND:’ field in the ‘DD Export Options’ window, enter ‘Close’
25. In the ‘COMMAND:’ field in the ‘File List’ window, enter ‘Next Page’.
26. Down arrow to ‘ROUTINE’ and press \<Enter\>.
27. In the ‘Routine’ window, enter TIUDD61, and ‘SEND TO SITE’.
28. In the ‘Routine’ window, enter TIUZRT, and ‘SEND TO SITE’.
    1.  If TIUZRT does not exist, it will not be selectable. Continue to the next step.
29. In the ‘COMMAND:’ field in the ‘Routine’ window, enter ‘Close’.
30. In the ‘COMMAND:’ field in the ‘Build Components’ window, enter ‘Save’, then enter ‘Exit’.
31. On the Menu select ‘Transport a Distribution’.
32. Enter the ‘local package name and identifier’ that was created in Step 3.
33. At the ‘Another Package Name:’ press \<Enter\>.
34. At the ‘OK to continue? Prompt, select YES//’ press \<Enter\>.
35. If creating a Host File transport, perform the following steps:
    1.  At the ‘Transport through (HF) Host File or (PM) PackMan:’ prompt, enter HF.
    2.  At the ‘Enter a Host File:’ prompt, enter the system file to which the Local Patch Backup will be saved, for example: ZTIU_1_309.KID).
    3.  At the ‘Header Comment:’ Enter ‘Local Backup of TIU\*1.0\*309’.
    4.  At the Edits and Distribution Menu, press \<Enter\>.
    5.  At the KIDS Menu press \<Enter\>.
36. If creating a PackMan transport, perform the following steps:
    1.  At the ‘Transport through (HF) Host File or (PM) PackMan:’ enter PM.
    2.  At the ‘Header Comment:’ enter ‘Local Backup of TIU\*1.0\*309’
    3.  For the description of Packman Message, Enter: ‘This is a saved backup for the lab patch install for TIU\*1.0\*309. This local build will be used in the event that the above mentioned installs need to be backed out.’
    4.  At ‘EDIT Option:’ press \<Enter\>.
    5.  At the ‘Do you wish to secure this message? NO// prompt, Enter ‘NO’.
    6.  At the ‘Send mail to:’ prompt, Enter your name.
    7.  At the ‘Select basket to send to: IN//’ prompt: press \<Enter\>.
    8.  At the ‘And Send to:’ prompt: Enter any additional persons that may need to have the local patch.
    9.  At The ‘Select Edits and Distribution \<TEST ACCOUNT\> Option:’ press \<Enter\>.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch TIU\*1.0\*309 does not require any platform installation or preparation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CTT&DM NDS patch TIU\*1.0\*309 is being released as a FORUM Patch via the Patch Module, therefore, the patch must be downloaded from FORUM, and forwarded to the destination site, in the form of a Packman message.

Documentation describing the new functionality introduced by this patch is available. The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

Albany: <span class="mark">REDACTED</span>

Hines: <span class="mark">REDACTED</span>

Salt Lake City: <span class="mark">REDACTED</span>

The documentation will be in the form of Adobe Acrobat files. Documentation can also be found on the VA Software Documentation Library at: http://www4.va.gov/vdl/

Title: TIU Technical Manual TIU_1_309 Update

File Name: tiutm.doc

tiutm.pdf

FTP Mode: Binary

Title: Deployment, Installation, Back-Out, Rollback Guide TIU_1_309

File Name: tiu_1_0_309_ig.doc

tiu_1_0_309_ig.pdf

FTP Mode: Binary

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new database is required for the CTT&DM NDS patch TIU\*1.0\*309.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are required for installation of CTT&DM NDS patch TIU\*1.0\*309.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No CRON scripts are required for installation of CTT&DM NDS patch TIU\*1.0\*309.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to national VA network, as well as the local network of each site to receive CTT&DM NDS patch TIU\*1.0\*309 is required to perform the installation, as well as authority to create and install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter the patch TIU\*1.0\*309:
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
1.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
2.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond NO.
3.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
4.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond NO.
5.  If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of CTT&DM NDS patch TIU\*1.0\*309 may be verified by running the Kernel checksum tool from the VistA server command line after installation:

D CHECK1^XTSUMBLD

The checksums produced by the checksum tool should match the numeric portion of the “After:” checksums in the CTT&DM NDS patch TIU\*1.0\*309 patch description.

Example, Checksum for routines as displayed by Kernel checksum tool CHECK1^XTSUMBLD:

TIUDD61 value = B110642266

TIUZRT value = B8873406

The “After:” checksum for routines as displayed in the patch description:

Routine Name: TIUDD61

Before: B9982481 After: B11064226 \*\*225,309\*\*

Routine Name: TIUZRT

Before: n/a After: B8873406 \*\*309\*\*

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No System Configuration is required before or after deployment of CTT&DM NDS patch TIU\*1.0\*309.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Database Tuning is required before or after deployment of CTT&DM NDS patch TIU\*1.0\*309.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

Perform the back-out procedure to load the locally made patch created in Section 4. The back-out is to be performed by persons with programmer-level access, and in conjunction with the STS team.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-out Strategy is to load the locally made patch that was created in Section 4.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out should only be done in the event that the local facility management determines that the patch TIU\*1.0\*309 is not appropriate for that facility, and should only be done as a last resort.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch TIU\*1.0\*309.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Local Facility Management would need to determine patch TIU\*1.0\*309 is not appropriate for their facility.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By backing out TIU\*1.0\*309, the local facility will not be able to use TIU to update LOINC codes from the respective Standards Development Organizations.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Local Facility Management has the authority to back-out patch TIU\*1.0\*309.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Due to the complexity of this patch (because of the data dictionary changes), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the National Service Desk (NSD) to submit a CA SDM ticket; the development team will assist with the process.

Perform the back-out procedure to load and install the locally made patch created in Section 4.2, and to delete the new CODING SYSTEM (#2) multiple in the TIU VHA ENTERPRISE STANDARD FILE (#8926.1) file. The back-out is to be performed by persons with programmer-level access, and in conjunction with the STS team.

The following is an example of the steps that would be exercised for the CODING SYSTEM (#2) multiple field being removed. The backout is to be performed by persons with programmer-level access, and in conjunction with the STS Team. File Manager should be used to delete the new CODING SYSTEM (#2) multiple field added with TIU\*1.0\*309. This will automatically also remove all sub-fields and data.

Back-Out Procedure

The following will need to be executed from the programmers prompt (User input depicted below in *bold italicized* font):

Delete CODING SYSTEM multiple, subfields, and data from TIU VHA ENTERPRISE STANDARD TITLE (#8926.1) file:

D P^DI

Select OPTION: MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES// NO

MODIFY WHAT FILE: // 8926.1 TIU VHA ENTERPRISE STANDARD TITLE (#8926.1)

(2346 entries)

Select FIELD: CODING SYSTEM (multiple)

LABEL: CODING SYSTEM// @

SURE YOU WANT TO DELETE THE ENTIRE 'CODING SYSTEM' FIELD? Y (Yes)

OK TO DELETE 'CODING SYSTEM' FIELDS IN THE EXISTING ENTRIES? Yes// Y (Yes).....

The steps for the load and installation of the locally made patch are very similar to the installation steps listed in section 4.8.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME, enter the local patch from section 4.8 (for example: ZZZ\*1.0\*004).
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond NO.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//' , respond NO.
8.  If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ROUTINES

After backing out patch TIU\*1.0\*309 by installing the local patch from section 4.8, routine back-out may be verified by running the Kernel checksum tool from the VistA server command line after installation:

D CHECK1^XTSUMBLD

The checksums produced by the checksum tool should match the numeric portion of the “Before:” checksums in the CTT&DM NDS patch TIU\*1.0\*309 patch description.

DATA DICTIONARIES

After backing out Patch TIU\*1.0\*309, successful back-out of the CODING SYSTEM (#2) multiple field in the TIU VHA ENTERPRISE STANDARD TITLE (#8926.1) may be verified by running a global listing from the VistA server command line after installation. A global listing should be performed for the following global nodes, after which nothing should be listed if back-out was successful:

Global ^DD(8926.12,

Global ^DD(8926.121,

Example:

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global ^DD(8926.12 -- NOTE: translation in effect

\<nothing should print\>

Global ^DD(8926.121 -- NOTE: translation in effect

\<nothing should print\>

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A