---
consolidated_title: "deployment, installation, back-out, rollback guide"
app_code: ADT
doc_type: DIBR
master_source: "DG*5.3*964 Deployment, Installation, Back-out, Rollback Guide"
master_pub_date: March 2023
consolidated_from: 4 versions
prior_versions:
  - "DG*5.3*1097 Deployment, Installation, Back-out, Rollback Guide"
  - "DG*5.3*1108 Deployment, Installation, Back-out, Rollback Guide"
  - "DG*5.3*1120 Deployment, Installation, Back-out, Rollback Guide"
---

---
title: |
  <span id="_top" class="anchor"></span>VistA Audit Solution (VAS) DG\*5.3\*964

  Deployment, Installation, Back-out, and Rollback Guide
---

![](dg-5-3-964-deployment-installation-back-out-rollback-guide/001.png)

March 2023

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Hlk99702550" class="anchor"></span>Table 1: DIBRG Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
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
<td>03/06/2023</td>
<td>2.2</td>
<td><p>Removed server table from section <strong>4.10.2</strong> <strong>Configure VAS REST API Server.</strong></p>
<p>Added instructions to obtain VAS Export server information from the VistA Audit Solution (VAS) support team to section <strong>4.10.2</strong> <strong>Configure VAS REST API Server.</strong></p></td>
<td>VAS Support Team</td>
</tr>
<tr class="even">
<td>02/05/2023</td>
<td>2.1</td>
<td>Add VAS export activation and server update information to post-installation section.</td>
<td>VAS Support Team</td>
</tr>
<tr class="odd">
<td>10/14/2022</td>
<td>2.0</td>
<td>Update to support IOC</td>
<td>VAS Support Team</td>
</tr>
<tr class="even">
<td>03/02/2022</td>
<td>1.9</td>
<td>Update pre-installation and post-installation instructions with details related to the VAS mail group</td>
<td>VAS Support Team</td>
</tr>
<tr class="odd">
<td>02/11/2022</td>
<td>1.8</td>
<td>Updates to Section 5.6 for DG VAS Monitor (group)</td>
<td>VAS Support Team</td>
</tr>
<tr class="even">
<td>02/08/2022</td>
<td>1.7</td>
<td>Transferred content to DIBRG document template from Process Access Library (PAL) – Artifacts Library</td>
<td>VAS Support Team</td>
</tr>
<tr class="odd">
<td>1/19/2022</td>
<td>1.6</td>
<td>Updates to Section 1.1 and Appendix A</td>
<td>VAS Support Team</td>
</tr>
<tr class="even">
<td>12/09/2021</td>
<td>1.5</td>
<td>Updates to Sections 2.0, 3.2.2., 5.1, 5.6, and 6.6</td>
<td>VAS Support Team</td>
</tr>
<tr class="odd">
<td>09/23/2021</td>
<td>1.4</td>
<td>Updates to Section 5.6</td>
<td>VAS Support Team</td>
</tr>
<tr class="even">
<td>05/18/2021</td>
<td>1.3</td>
<td>Transferred content to OIT document template, implemented minor corrections in grammar and syntax throughout</td>
<td>VAS Support Team</td>
</tr>
<tr class="odd">
<td>05/13/2021</td>
<td>1.2</td>
<td>Updates to Sections 2, 4.2.1, 5, and 6</td>
<td>VAS Support Team</td>
</tr>
<tr class="even">
<td>05/05/2021</td>
<td>1.1</td>
<td>Updates to Section 4</td>
<td>VAS Support Team</td>
</tr>
<tr class="odd">
<td>03/31/2021</td>
<td>1.0</td>
<td>Initial Issue</td>
<td>VAS Support Team</td>
</tr>
</tbody>
</table>

<span id="_Hlk99702550" class="anchor"></span>Table 1: DIBRG Roles and Responsibilities

Table of Contents

List of Tables

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
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
    - [Patch Dependencies](#patch-dependencies)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [Pre-Installation Instructions](#pre-installation-instructions)
    - [VistA Patch DG\5.3\964 Installation Instructions](#vista-patch-dg53964-installation-instructions)
    - [Post Installation Instructions](#post-installation-instructions)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
    - [Map the DG VAS QUEUE File (#46.3) to Non-Journaled Directory](#map-the-dg-vas-queue-file-463-to-non-journaled-directory)
    - [Configure VAS REST API Server](#configure-vas-rest-api-server)
  - [Database Tuning](#database-tuning)
- [Back-out Procedure](#back-out-procedure)
  - [Back-out Strategy](#back-out-strategy)
  - [Back-out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-out Criteria](#back-out-criteria)
  - [Back-out Risks](#back-out-risks)
  - [Authority for Back-out](#authority-for-back-out)
  - [Back-out Procedure](#back-out-procedure-1)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
  - [Data Dictionaries](#data-dictionaries)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
> This document describes how to deploy and install the Veterans Health Information Systems Technology Architecture (VistA) Registration patch DG\*5.3\*964, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.
> The guide includes information about system support, issue tracking, escalation processes, roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, reflecting the particulars of these procedures at a single or at multiple locations.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document describing how, when, where, and for whom the DG\*5.3\*964 patch will be deployed and installed, as well as how the patch is to be backed out and rolled back, if necessary. The plan also identifies resources, offers a communications plan, and contains a rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

This enhancement patch implements the VistA Audit Solution (VAS), a real-time web-based interface. VAS provides a nationwide Health Insurance Portability and Accountability Act (HIPAA) compliant Audit Tracking Solution with the ability to track and report on access logs for patient's Personal Identifiable Information (PII)/Protected Health Information (PHI) data across all VistA instances. VAS users are Privacy Officers, Information Systems Security Officers (ISSO), and their authorized representatives who need the ability to view the log of Create, Read, Update and/or Delete (CRUD) operations on patient information to respond to Freedom of Information Act (FOIA), HIPAA, employee and Inspector General (IG) requests. This data originates from VistA and flows through in-memory database servers to be stored in the Veterans Affairs Enterprise Cloud (VAEC) Amazon Web Services (AWS). The VAS web-based User Interface (UI) will access and display the data stored in AWS.

Authorized VAS users may view the patient data that was accessed and modified, as well as the individual that performed the actions.

Patch DG\*5.3\*964 is being released as a patch (PackMan) message.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch possesses one direct application dependency for the VistA Registration 5.3 package (DG). The released patches DG\*5.3\*699 and DG\*5.3\*796 are required to be installed before DG\*5.3\*964.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should be installed in all VA VistA production sites. This patch is intended for a fully patched VistA system. Its installation will not noticeably impact the production environment.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                                                                                              | Phase/Role      | Tasks                                                                                                           | Project Phase |
|-----|-------------------------------------------------------------------------------------------------------------------|-----------------|-----------------------------------------------------------------------------------------------------------------|---------------|
| 1   | VA Office of Information and Technology (OIT), VA OIT Health Product Support, and Project Management Office (PMO) | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                             | Planning      |
| 2   | Local individual Veterans Administration Medical Centers (VAMCs)                                                  | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment                       | Planning      |
| 3   | Field Testing (Initial Operating Capability (IOC)), Health Product Support Testing                                | Deployment      | Test for operational readiness                                                                                  | Testing       |
| 4   | Health Product Support and Field Operations                                                                       | Deployment      | Execute deployment                                                                                              | Deployment    |
| 5   | VAMCs                                                                                                             | Installation    | Plan and schedule installation                                                                                  | Deployment    |
| 6   | VAS ATO Team                                                                                                      | Installation    | Obtain authority to operate and that certificate authority security documentation is in place                   | Deployment    |
| 7   | VAS Team                                                                                                          | Installation    | Coordinate knowledge transfer with the team responsible for user training                                       | Deployment    |
| 8   | Health Product Support and the VAS development team                                                               | Back-out        | Confirm availability of back-out instructions and back-out strategy, e.g., the criteria that trigger a back-out | Deployment    |
| 9   | VAS Team                                                                                                          | Post-Deployment | Hardware, Software, and System Support                                                                          | Warranty      |

<span id="_Toc71818402" class="anchor"></span>Table 2: Software Specifications

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment is planned as a concurrent online rollout. During Initial Operating Capability (IOC) testing and after National release, patch DG\*5.3\*964 will be distributed via the FORUM Patch Module and may be deployed at any site without regard to deployment status at other sites.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for a period of thirty (30) days. A detailed schedule will be provided during the build. A warranty period of ninety (90) days will follow the deployment and installation schedule to address any potential issues for the build.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the DG\*5.3\*964 patch deployment.

The DG\*5.3\*964 patch must be manually installed or manually queued for installation at each VistA instance at which it is deployed, using the standard Kernel Installation and Distribution System (KIDS). The patch should be installed at all VA VistA instances running the VistA DG v.5.3 application and will update the Massachusetts General Hospital Utility Multi-Programming System (MUMPS) server software in each VistA instance’s Registration namespace.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DG\*5.3\*964 patch should be installed in all VA VistA production sites.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During IOC testing, the DG\*5.3\*964 patch will be deployed at the following sites:

- James A. Haley Veterans' Hospital, Tampa FL (673)
- VA Texas Valley Coastal Bend Health Care System, Harlingen TX (740)
- John L. McClellan Memorial Veterans Hospital, Little Rock AR (598)

Upon National release, the patch will be available for install at all sites running the VistA Registration v5.3 package. The software will be distributed as a PackMan message in FORUM.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special preparation is required by the site prior to deployment. The VA sites should follow the standard procedure currently being used for installation of VistA patches.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment of the DG\*5.3\*964 patch requires a fully patched VistA environment running the Registration v.5.3 package. No additional resources are required for patch installation.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special requirements regarding new or existing hardware capability. Existing hardware resources will not be impacted by the changes in this project.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to Table 2 (Software Specifications) which describes the software specifications required at each site prior to deployment.

| Required Software                               | Make | Version                     | Configuration | Manufacturer | Other |
|-------------------------------------------------|------|-----------------------------|---------------|--------------|-------|
| Fully patched Registration package within VistA | N/A  | 5.3                         | N/A           | N/A          | N/A   |
| DG\*5.3\*699                                    | N/A  | Nationally released version | N/A           | N/A          | N/A   |
| DG\*5.3\*796                                    | N/A  | Nationall released version  | N/A           | N/A          | N/A   |

<span id="_Toc129731686" class="anchor"></span>Table 3: Deployment/Installation/Back-Out Checklist

See Table 1: DIBRG Roles and Responsibilities for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites participating in IOC field testing will use the “Patch Tracking” message in Outlook to communicate with the VAS team, the developers, and product support personnel.

#### Deployment / Installation / Back-out Checklist

The assigned Health Information Governance (HIG) team will deploy the patch DG\*5.3\*964, which is tracked nationally for all Veterans Administration Medical Centers (VAMCs) in the National Patch Module (NPM) in FORUM. FORUM automatically tracks the patches as they are installed in the different VAMC production systems. A report in FORUM can be run to identify when the patch was installed in VistA production at each site. A report can also be run to identify which sites have not currently installed the patch in their VistA production system. Therefore, this information does not need to be manually tracked.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | N/A | N/A  | N/A                           |
| Install  | N/A | N/A  | N/A                           |
| Back-Out | N/A | N/A  | N/A                           |

<span id="_Toc129731687" class="anchor"></span>Table : Acronym Listing

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*964, a patch to the existing VistA Registration 5.3 package, is installable on a fully patched MUMPS VistA system and operates on top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities that communicate with the underlying operating system and hardware, thereby providing Registration independence from variations in hardware and operating system.

### Patch Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches DG\*5.3\*699 and DG\*5.3\*796 must be installed prior to installing this patch.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*964 does not require any platform installation or preparation.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*964 will be distributed via a PackMan message and can be retrieved from the National Patch Module (NPM) on FORUM.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch updates an existing VistA database, this section is not applicable.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch does not contain any installation scripts, this section is not applicable.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch does not contain any Cron scripts, this section is not applicable.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the National VA Network, as well as the local network of each site to receive DG patches, is required to perform the installation, as well as authority to install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the Kernel 8.0 & Kernel Toolkit Version 7.3 Systems Management Guide.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides step-by-step instructions for installing DG\*5.3\*964. Instructions for installation are also detailed in the DG\*54.3\*964 Patch Description in the NPM in FORUM.

### Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. The VAS export defaults to 'Don't generate or send data' during installation, minimizing potential user disruption. This patch should take less than 5 minutes to install. If desired, you may queue this installation.

Prior to installing DG\*5.3\*964, a backup patch should be created that can be re-installed in the event that a new patch must be backed out (see the “[Create a Local Patch Backup](#create-a-local-patch-backup)” section). Also, an organizer for the mail group used by the VAS background process to report errors should be identified and recorded in order to complete the post-installation steps (see the “[Identify Mail Group Organizer](#identify-mail-group-organizer)” section).

#### Create a Local Patch Backup

Perform the following procedure to create a Local Patch Backup:

1)  From the KIDS Menu, select ‘Installation’
2)  Select ‘Backup a Transport Global’
3)  At the ‘INSTALL NAME:’ prompt, enter DG\*5.3\*964
4)  At the ‘Backup Type: B//’ prompt, enter B for build
5)  At the ‘Do you wish to secure this message?’ prompt, enter NO
6)  At the ‘Send mail to:’ prompt, enter a recipient who can install the backup build if necessary
7)  At the ‘And Send to:’ prompt(s), optionally enter additional build recipients. Press \<Enter\> to continue to the next prompt.

#### Identify Mail Group Organizer

Identify the appropriate organizer for the mail group stored in the REDACTED parameter. After patch installation, this name must be added as the organizer of the mail group. The organizer should be a Privacy Officers or Information Systems Security Officers (ISSO) or their authorized representative at the facility where the patch is being installed. The organizer must have the ability to view the log of Create, Read, Update and/or Delete (CRUD) operations on patient information to respond to Freedom of Information Act (FOIA), HIPAA, employee and Inspector General (IG) requests. See the post-installation step ['Mail Group Update'](#mail-group-update) for more information.

### VistA Patch DG\*5.3\*964 Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build.
2.  Choose the “INSTALL/CHECK MESSAGE PackMan” option to load the build.
3.  From the Kernel Installation and Distribution System Menu, select the “Installation” Menu. From this menu,
    1.  Select the “Verify Checksums in Transport Global” option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch name, DG\*5.3\*964.
    2.  Select the “Backup a Transport Global” option to create a backup message. You can specify what to backup, the entire Build or just Routines. The backup message can be used to restore just the routines or everything that will restore your system to pre-patchcondition. Subject: Backup of DG\*5.3\*964 on Jul 16, 2021 Replace. Select one of the following:
        1.  B Build (including Routines)
        2.  R Routines Only
        3.  Backup Type: B// Build (including Routines)
        4.  Send mail to: (Send mail to you the installer)
    3.  You may also elect to use the following options:
        1.  Print Transport Global – This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System – This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install DG\*5.3\*964.
5.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer YES.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

### Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The web server REDACTED exported with DG\*5.3\*964 should be automatically pointed to the correct VAS server during installation. However, this must be verified and updated manually if the server was not populated correctly (see Section 4.8.3.1 – VAS Server Update).

The mail group associated with the VAS export must be manually populated with the appropriate local member(s) and remote member (see Section 4.8.3.3 – Mail Group Update).

The VAS export process includes a switch in the VAS STATUS (#.02) field in the DG VAS CONFIG (#46.5) file. The switch is set to “0-Don't generate or send data” by default during installation, and must be set to “1-Generate and send data” manually when the site is scheduled for activation. (see Section 4.8.3.3 – Activating the VAS Export).

#### VAS Export Server Configuration

Verify the VAS Export server configuration is correct by completing section [4.10.2 Configure VAS Server.](#configure-vas-rest-api-server)

#### Verify VAS Server Connectivity

After updating the VAS server, verify a successful connection to the VAS server using the Web Server Manager \[REDACTED\] option.

1\. Navigate to the Web Server Manager \[X REDACTED\] option.

2\. At the “Select Action:” prompt, enter “CK” for Check Web Service Availability.

3\. At the “Select Web Server:” prompt, select the REDACTED server from the list.

4\. The message “REDACTED is available” should display, indicating the web service is connected and available. If an error message is displayed indicating the service is not available, log a Service Now (SNOW) ticket with a comment requesting the ticket be forwarded to VistA Audit Solution Assignment Group.

<u>Example – Check Web Service Connection</u>

#### REDACTED

#### Mail Group Update

Find the mail group used by the VAS in the Display VAS Parameters \[DG VAS DISPLAY\] option in the VistA Audit Solution (VAS) options \[DG VAS MENU\]. The mail group is displayed to the right of the label “DG VAS MONITOR GROUP:”

<u>Example – Identify VAS Mail Group</u>

REDACTED

Once the appropriate mail group is identified, use the Mail Group Edit \[REDACTED\] option in the Group/Distribution Management \[REDACTED\] menu in the Manage Mailman \[REDACTED\] menu to populate the following fields:

- At the “ORGANIZER:” prompt, enter the mail group organizer identified in the pre-installation step.
- At the “MEMBER:” prompt, enter the mail group organizer identified in the pre-installation step.
- At the “REMOTE MEMBER;” prompt, enter REDACTED. This is the VAS Support Outlook mail group.

<u>Example – Update VAS Mail Group</u>

REDACTED

#### Activate the VAS Export

When the site is scheduled for activation by VAS development team, the VAS Export must be turned on to begin sending audit records to the VAS server.

NOTE - Do NOT activate the VAS Export until notified by the Health Information Governance (HIG) office.

A notification will be provided to Regional IT support by the Health Information Governance (HIG) office to update the VAS STATUS Flag when the facility is ready to begin transferring data to the VAS external archive via the VAS REST API. The VAS STATUS may be updated by using

the DG VAS MODIFY option in the DG VAS Menu. See the PIMS Technical manual and release notes for additional information.

Follow the steps below to activate the VAS server.

1\. Navigate to the Modify VAS Parameters \[REDACTED\] option in the VistA Audit Solution (VAS) Options \[REDACTED\] menu in the Security Officer Menu \[REDACTED\].

2\. At the “VAS STATUS:” prompt, enter the number 1 (one) to select “Generate and send data”.

<u>Example – Activate VAS Export</u>

REDACTED

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following patch installation, the installation may be verified by using the “Install File Print” menu option in the “Utilities” submenu of the Kernel Installation & Distribution System (KIDS) option.

The existence of the VistA Audit Solution (VAS) options \[REDACTED\] menu in the Security Officer Menu \[REDACTED\] may also be used to verify successful installation.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System Configuration required after deployment of the patch is as follows.

### Map the DG VAS QUEUE File (#46.3) to Non-Journaled Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The global for the DG VAS QUEUE file (#46.3) should be mapped to a non-journaled directory.

Following are examples for IRIS systems and Cache:

For an IRIS system, directory should be in this format.

> REDACTED is the unique site code, and REDACTED

> REDACTED

A Cache system should be in this format:

> REDACTED

### Configure VAS REST API Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation, the REDACTED server is automatically populated. After installation, the value of the REDACTED server must be checked and updated if not accurate. The value of the REDACTED server may be checked using the Display VAS Parameters \[REDACTED\] option in the VistA Audit Solution (VAS) options \[REDACTED\]. The server value is displayed next to the REDACTED label.

The correct server for a given production environment may be obtained from VAS support by submitting a Service NOW ticket. The ticket description should include the text “REDACTED” and should be assigned to Assignment Group “REDACTED”.

After identifying the correct REDACTED server, the VAS export server may be updated using the Web Server Manager \[REDACTED\] option using the following steps:

1)  Select the Web Server Manager \[REDACTED\] option.
2)  At the Select Action: prompt, select ES Edit Server.
3)  At the Select Web Server: prompt, select the ID number displayed next to the REDACTED entry.
4)  At the NAME: prompt, accept the default REDACTED by pressing Enter.
5)  At the SERVER: prompt, enter the correct server name.
6)  At the PORT: prompt, enter caret “^” to exit the action.
7)  At the Select Action: prompt, enter caret “^” to exit the option.

Example, Configuring the VAS REST API Server

REDACTED

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Database Tuning is required before or after deployment of the patch.

# Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within context of this document, the term *back-out* pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out strategy will follow VA guidelines and best practices as referenced in the Enterprise Operations (EO) National Data Center Hosting Services document. The Back-Out strategy consists of restoring non Data Dictionary components by installing the backup created prior to patch installation, and manually removing each new Data Dictionary introduced by the patch.

## Back-out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to first determine if a wholesale back-out of the patch DG\*5.3\*964 is needed or if it would be better to correct by means of applying a new version of the patch (if prior to national release) or employing a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale back-out of the patch will require a subsequent patch after national release. If the back-out is post-release of patch DG\*5.3\*964, this patch should be assigned the status of “Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing is required for patch DG\*5.3\*964.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Results from the UAT will be available upon completion.

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out criteria will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

Back-out criteria may include the following:

- The project is canceled.
- The requested changes implemented by DG\*5.3\*964 are no longer desired by VA OIT.
- The patch produces catastrophic problems.

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known risks related to a back-out.

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Portfolio Director, VA Project Manager, and Business Owner have the authority to require the back-out and accept the risks. Health Information Governance (HIG) will work to identify the problem and assist with implementation. This should be done in consultation with the development team and project stakeholders.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out plan for VistA applications is complex and not a ‘one-size fits all’ solution. After national release, the general strategy is to repair the code with a follow-up patch. The VAS development team recommends sites log a ticket with the Enterprise Service Desk (ESD) if it is a nationally released patch.

Prior to national release, backout may be performed by installing the backup of the build performed prior to installation, as well as manually removing the data dictionaries installed by the patch.

Steps – non-Data Dictionary backout:

1)  Navigate to the Mailman menu.
2)  Select the Mailman folder containing the patch backup created prior to install.
3)  Select the message containing the patch backup created prior to install.
4)  At the prompt “Enter message action:”, enter “X” for Xtract KIDS.
5)  At the prompt “Select PackMan function:”, enter 6.
6)  At the prompt, “OK to continue with Load?” enter “YES”.
7)  At the prompt, “Want to Continue with Load?”, enter “YES”.
8)  Navigate to the Kernel Installation & Distribution System \[REDACTED\] menu.
9)  Select the Installation menu.
10) Select the Install Package(s) option.
11) At the prompt “INSTALL NAME:”, enter DG\*5.3\*964b.
12) At the prompt “Want KIDS to Rebuild Menu Trees Upon Completion of Install” enter “NO”.
13) At the prompt, “Want KIDS to INHIBIT LOGONs during the install” enter “NO”.
14) At the prompt, “Want to DISABLE Scheduled Options, Menu Options, and Protocols” enter “NO”.
15) At the “DEVICE” prompt, select a device or accept the default, “HOME”.

Steps – Data Dictionary Backout:

1)  Navigate to the VA FileMan \[REDACTED\] menu.
2)  Select the Edit File option in the Utility Functions menu.
3)  At the prompt “Modify what File:” enter “DG VAS QUEUE”.
    1.  At the prompt “Do you want to use the screen-mode version?”, enter “YES”.
    2.  At the prompt “NAME:”, enter “@”.
    3.  If prompted “DO YOU WANT JUST TO DELETE THE FILE CONTENTS, KEEP THE FILE DEFINITION?”, enter “NO”.
    4.  At the prompt “SURE YOU WANT TO DELETE THE ENTIRE ‘DG VAS QUEUE’ file, enter “Y”.
4)  At the prompt “Modify what File:” enter “DG VAS EXPORT”.
    1.  At the prompt “Do you want to use the screen-mode version?”, enter “YES”.
    2.  At the prompt “NAME:”, enter “@”.
    3.  If prompted “DO YOU WANT JUST TO DELETE THE FILE CONTENTS, KEEP THE FILE DEFINITION?”, enter “NO”.
    4.  At the prompt “SURE YOU WANT TO DELETE THE ENTIRE ‘DG VAS EXPORT’ file, enter “Y”.
5)  At the prompt “Modify what File:” enter “DG VAS CONFIG”.
    1.  At the prompt “Do you want to use the screen-mode version?”, enter “YES”.
    2.  At the prompt “NAME:”, enter “@”.
    3.  If prompted “DO YOU WANT JUST TO DELETE THE FILE CONTENTS, KEEP THE FILE DEFINITION?”, enter “NO”.
    4.  At the prompt “SURE YOU WANT TO DELETE THE ENTIRE ‘DG VAS CONFIG’ file, enter “Y”.

Steps – backing out the Mail Group entry:

1.  Navigate to the VA FileMan menu \[REDACTED\].
2.  Select the ENTER OR EDIT FILE ENTRIES option.
3.  At the prompt “Input to what File”, enter MAIL GROUP.
4.  At the prompt “EDIT WHICH FIELD”, enter ALL.
5.  At the prompt “MAIL GROUP NAME” enter REDACTED.
6.  At the prompt “NAME” enter @.
7.  At the prompt “SURE YOU WANT TO DELETE THE ENTIRE ' REDACTED ' MAIL GROUP” enter YES.
8.  At the prompt “DO YOU WANT THOSE POINTERS UPDATED” enter YES.
9.  At the prompt “CHOOSE 1) OR 2)” choose 1 to delete all pointers.

Steps – backing out the Web Server entry:

1.  Navigate to the VA FileMan menu \[REDACTED\].
2.  Select the ENTER OR EDIT FILE ENTRIES option.
3.  At the prompt “Input to what File”, enter WEB SERVER.
4.  At the prompt “EDIT WHICH FIELD”, enter ALL.
5.  At the prompt “WEB SERVER NAME” enter REDACTED.
6.  At the prompt “NAME” enter @.
7.  At the prompt “SURE YOU WANT TO DELETE THE ENTIRE  
    ‘REDACTED’ WEB SERVER?” enter YES.
8.  At the prompt “DO YOU WANT THOSE POINTERS UPDATED” enter YES.
9.  At the prompt “CHOOSE 1) OR 2)” choose 1 to delete all pointers.

Steps – backing out the Web Service entry:

1.  Navigate to the VA FileMan menu \[REDACTED\].
2.  Select the ENTER OR EDIT FILE ENTRIES option.
3.  At the prompt “Input to what File”, enter WEB SERVICE.
4.  At the prompt “EDIT WHICH FIELD”, enter ALL.
5.  At the prompt “WEB SERVICE” enter REDACTED.
6.  At the prompt “NAME” enter @.
7.  At the prompt “SURE YOU WANT TO DELETE THE ENTIRE  
    ‘REDACTED’ WEB SERVICE?” enter YES.
8.  At the prompt “DO YOU WANT THOSE POINTERS UPDATED” enter YES.
9.  At the prompt “CHOOSE 1) OR 2)” choose 1 to delete all pointers.

Example, patch restore from backup:

<u>Example: Load backup patch:</u>

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

Line 8 Message \#300223 Unloading KIDS Distribution DG\*5.3\*964b

Build DG\*5.3\*964b has been loaded before, here is when:

DG\*5.3\*964b Install Completed

was loaded on Oct 04, 2021@13:25:47

OK to continue with Load? NO// YES

Want to Continue with Load? YES//

Loading Distribution...

DG\*5.3\*964b

Select PackMan function:

Enter message action (in IN basket): Ignore//

<u>Example: Install backup patch:</u>

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INstallation

Select Installation \<TEST ACCOUNT\> Option: INstall Package(s)

Select INSTALL NAME: DG\*5.3\*964b 10/4/21@13:49:20

=\> Backup of DG\*5.3\*964 on Oct 04, 2021. Build

This Distribution was loaded on Oct 04, 2021@13:49:20 with header of

Backup of DG\*5.3\*964 on Oct 04, 2021. Build

It consisted of the following Install(s):

DG\*5.3\*964b

Checking Install for Package DG\*5.3\*964b

Install Questions for DG\*5.3\*964b

Incoming Files:

46.3 DG VAS QUEUE

> **NOTE:** You already have the 'DG VAS QUEUE' File.

46.4 DG VAS EXPORT

> **NOTE:** You already have the 'DG VAS EXPORT' File.

46.5 DG VAS CONFIG

> **NOTE:** You already have the 'DG VAS CONFIG' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// Linux Telnet /SSh

DG\*5.3\*964b

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Installing Data Dictionaries:

Oct 04, 2021@13:49:36

Installing PACKAGE COMPONENTS:

Installing OPTION

Installing PARAMETER DEFINITION

Oct 04, 2021@13:49:36

Updating Routine file...

Updating KIDS files...

DG\*5.3\*964b Installed.

Oct 04, 2021@13:49:36

NO Install Message sent

R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

100% . 25 50 75 .

Complete F,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

Install Completed

<u>Example: Delete Data Dictionaries:</u>

Select OPTION NAME: DIUSER VA FileMan

VA FileMan Version 22.2

Select VA FileMan \<TEST ACCOUNT\> Option: UTILity Functions

Select Utility Functions \<TEST ACCOUNT\> Option: EDIT File

Modify what File: DG VAS CONFIG// 46.3 DG VAS QUEUE (0 entries)

Do you want to use the screen-mode version? YES// NO

NAME: DG VAS QUEUE// @

SURE YOU WANT TO DELETE THE ENTIRE 'DG VAS QUEUE' FILE? Y (Yes)

Deleting the DATA DICTIONARY...

Deleting the INPUT TEMPLATES...

Deleting the PRINT TEMPLATES...

Deleting the SORT TEMPLATES...

Deleting the FORMS...

Deleting the BLOCKS...

Select Utility Functions \<TEST ACCOUNT\> Option: EDIT File

Modify what File: 46.4 DG VAS EXPORT (12 entries)

Do you want to use the screen-mode version? YES// NO

NAME: DG VAS EXPORT// @

DO YOU WANT JUST TO DELETE THE 12 FILE ENTRIES,

& KEEP THE FILE DEFINITION? No// NO

NAME: DG VAS EXPORT// @

DO YOU WANT JUST TO DELETE THE FILE CONTENTS,

& KEEP THE FILE DEFINITION? No// N (No)

IS IT OK TO DELETE THE '^DGAUDIT1' GLOBAL? Yes// Y (Yes)

SURE YOU WANT TO DELETE THE ENTIRE 'DG VAS EXPORT' FILE? Y (Yes)

Deleting the DATA DICTIONARY...

Deleting the INPUT TEMPLATES...

Deleting the PRINT TEMPLATES...

Deleting the SORT TEMPLATES...

Deleting the FORMS...

Deleting the BLOCKS...

Select Utility Functions \<TEST ACCOUNT\> Option: EDIT File

Modify what File: 46.5 DG VAS CONFIG (0 entries)

Do you want to use the screen-mode version? YES// NO

NAME: DG VAS CONFIG// @

DO YOU WANT JUST TO DELETE THE FILE CONTENTS,

& KEEP THE FILE DEFINITION? No// N (No)

IS IT OK TO DELETE THE '^DGAUDIT2' GLOBAL? Yes// Y (Yes)

SURE YOU WANT TO DELETE THE ENTIRE 'DG VAS CONFIG' FILE? Y (Yes)

Deleting the DATA DICTIONARY...

Deleting the INPUT TEMPLATES...

Deleting the PRINT TEMPLATES...

Deleting the SORT TEMPLATES...

Deleting the FORMS...

Deleting the BLOCKS...

<u>Example: Delete Mail Group</u>

VA FileMan 22.2

Select OPTION: ENTER OR EDIT FILE ENTRIES

Input to what File: // MAIL GROUP (432 entries)

EDIT WHICH FIELD: ALL//

Select MAIL GROUP NAME: REDACTED

NAME: DG VAS MONITOR// @

SURE YOU WANT TO DELETE THE ENTIRE ' REDACTED ' MAIL GROUP? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'BULLETIN' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// Y

(Yes)

WHICH DO YOU WANT TO DO? --

1\) DELETE ALL SUCH POINTERS

2\) CHANGE ALL SUCH POINTERS TO POINT TO A DIFFERENT 'MAIL GROUP' ENTRY

CHOOSE 1) OR 2): 1

DELETE ALL POINTERS? Yes// (Yes)

(DELETION WILL OCCUR WHEN YOU LEAVE 'ENTER/EDIT' OPTION)

The DG\*5.3\*964 patch contains the following build components. After backing out the patch, none of the components listed below should be present except routine DGSEC, which remains but is restored to its pre-patch state.

- A modification to the routine DGSEC to create an “INQUIRY” audit record in the external archive when a patient is selected within a VistA application.
- New DG VAS QUEUE File (#46.3), which temporarily holds records to be sent to the external archive. Records are immediately deleted after being transmitted.
- New DG VAS EXPORT File (#46.4), which keeps track of which VA FileMan AUDIT File (#1.1) records have been exported to the external archive.
- New DG VAS CONFIG File (#46.5), which contains the settings related to the connection to the ElastiCache/Redis server when this patch is installed at each site. Three new fields are added with the \#46.5 file.
  - NUMBER (#.01): Represents the single external server defined for the VistA instance. The field is not modifiable.
  - VAS STATUS (#.02): The ON/OFF setting for the transmission of targeted audit records to the Redis server.
  - VAS DEBUGGING FLAG (#2): Provides the user with the ability to request a log file displaying the local variables at the time the process is triggered.
- New OPTION File entry (DG VAS EXPORT), which is used to export audit entries from the new temporary DG VAS QUEUE File (#46.3), stored in the DGAUDIT global, to the external archive. Records in File \#46.3 are deleted immediately after being transmitted. This OPTION is automatically added to the OPTION SCHEDULING File (#19.2) as a Startup and Persistent task. The installer may specify the initial launch date/time.
- A new menu (DG VAS MENU) containing the new OPTIONS (DG VAS DISPLAY and DG VAS MODIFY) is added to the DG SECURITY OFFICER MENU.
- Two new Options, DG VAS DISPLAY and DG VAS MODIFY, which are related to the configuration settings and parameter definition values for the VAS.
  - DG VAS DISPLAY Option provides a view of the settings and current status. The option is found in the new DG VAS MENU.
  - DG VAS MODIFY Option provides the user with the ability to view and modify the parameters and settings for the processing and sending of the target audit records to the external archive. The option is provided to the user in the new DG VAS MENU.
- New entries in the PARAMETER DEFINITION File (#8989.51)
  - DG VAS BATCH SIZE Parameter Definition for the default number of entries and the maximum number of entries that are set into a batch of records sent to the VAS REST API. When the number of pending records in the DG VAS QUEUE file is less than the value of the DG VAS BATCH SIZE parameter, one final partial batch is sent containing the remaining entries in the queue.
  - DG VAS DAYS TO KEEP EXCEPTIONS Parameter Definition for the default number of days to keep exceptions in the ^XTMP global. When the number of days has been reached, the exceptions are purged.
  - DG VAS DEBUGGING FLAG Parameter Definition for the flag that triggers a message to members of the mail group in the DG VAS MONITOR GROUP parameter. The mail message contains a log file displaying the local variables at the time of the debugging process. Information related to the status of the VAS VistA background process is included in the message.
  - DG VAS MAX QUEUE ENTRIES Parameter Definition for the maximum number of entries that are allowed to be stored in the ^DGAUDIT global which houses the data for the DG VAS QUEUE File. The default is 60000 and is not modifiable manually. When the maximum number of entries is exceeded the oldest entries in the DG VAS QUEUE file are deleted until the maximum is no longer exceeded.
  - DG VAS MAX WRITE ATTEMPTS Parameter Definition for the maximum number of consecutive attempts to write, or POST, a batch of records to the DG VAS WEB SERVICE without receiving a response. The count of the write errors is incremented until the maximum is met, after which a mail message is generated and sent to the mail group in the REDACTED parameter. Audit records in a batch for which no response is received remain in the queue and will be retried until a response is received from the DG VAS WEB SERVICE.
  - DG VAS MONITOR GROUP Parameter Definition for the VistA Mailman mail group that receives updates from the VAS VistA background process.
- A new option (DG AUDIT TASKMAN), which starts the background processing job if the DGAUDIT background job has been stopped.
- A new Mail Group (REDACTED), which is used for notification of VistA process status for VAS.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out patch DG\*5.3\*964 by installing the local patch created during pre-install (see Section 4.1.3), successful back-out is confirmed by verification of BEFORE checksums listed in the patch description on NPM in FORUM. This may be accomplished using the ‘Calculate and Show Checksum Values’ option.

The checksums produced should match the numeric portion of the BEFORE checksums in the DG\*5.3\*964 patch description. For the routines that were new with DG\*5.3\*964, the BEFORE Checksums are ‘n/a’. If routine back-out was successful, the checksum will display as “Routine not in this UCI” in place of a checksum.

## Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out Patch DG\*5.3\*964, successful back-out of the fields installed by the patch may be verified by running the List File Attributes in the Data Dictionary function in VA FileMan.

Using VA FileMan, Data Dictionary Utility, List File Attributes, enter DG VAS QUEUE (#46.3), DG VAS EXPORT (#46.4), DG VAS CONFIG (#46.5). Nothing should be returned when entering those files to verify those files have been deleted.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. This patch contains three files containing data that need to be deleted to completely roll back the data.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deleting data requires elevated privileges and should only be performed by experienced technical support staff.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data installed and created by patch DG\*5.3\*964 should only be deleted after all patch software components have been removed.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If data is deleted prior to removing the software components, errors may occur.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Portfolio Director, VA Project Manager, and Business Owner have the authority to require the rollback and accept the risks. This should be done only after all patch software components have been backed out, and in consultation with the development team and project stakeholders.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback procedure consists of using the ^DIK VistA FileMan Application Programmer Interface (API) call from the programmer prompt to delete each of the three data files installed and populated by patch DG\*5.3\*964. These files are ^DGAUDIT, ^DGAUDIT1, and ^DGAUDIT2.

Steps:

1)  At the programmer prompt, type the line of code below and press \<Return\>.
    1.  S X=”” F S X=\$O(^DGAUDIT(X)) Q:X=”” K ^DGAUDIT(X)
2)  At the programmer prompt, type the line of code below and press \<Return\>.
    1.  S X=”” F S X=\$O(^DGAUDIT1(X)) Q:X=”” K ^DGAUDIT1(X)
3)  At the programmer prompt, type the line of code below and press \<Return\>.
    1.  S X=”” F S X=\$O(^DGAUDIT2(X)) Q:X=”” K ^DGAUDIT2(X)

<u>Example, deleting data using FileMan ^DIK API:</u>

VISTA\> S X=”” F S X=\$O(^DGAUDIT(X)) Q:X=”” K ^DGAUDIT(X)

VISTA\> S X=”” F S X=\$O(^DGAUDIT1(X)) Q:X=”” K ^DGAUDIT1(X)

VISTA\> S X=”” F S X=\$O(^DGAUDIT2(X)) Q:X=”” K ^DGAUDIT2(X)

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback verification may be performed by executing a Global List from the programmer prompt for the three globals installed and populated by patch DG\*5.3\*964 that may contain data.

Steps:

1)  At the programmer prompt, type “D ^%G”.
2)  At the prompt “Global ^”, enter “DGAUDIT”.
    1.  “\[Global does not exist\]” should display
3)  At the prompt “Global ^”, enter “DGAUDIT1”.
    1.  “\[Global does not exist\]” should display
4)  At the prompt, “Global ^”, enter “DGAUDIT2”.
    1.  “\[Global does not exist\]” should display

<u>Example, global list of deleted globals/rolled back data:</u>

VISTA\>D ^%G

For help on global specifications DO HELP^%G

Global ^DGUAUDIT \[Global does not exist\]

Global ^DGUAUDIT1 \[Global does not exist\]

Global ^DGUAUDIT2 \[Global does not exist\]

Global ^

#### Appendix A: Acronyms

| Acronym | Definition                                                      |
|---------|-----------------------------------------------------------------|
| ADT     | Admission, Discharge, and Transfer                              |
| API     | Application Programmer Interfaces                               |
| AWS     | Amazon Web Services                                             |
| CRUD    | Create, Read/Inquire, Update, and Delete                        |
| DG      | Registration package                                            |
| DIBRG   | Deployment, Installation, Back-Out, and Rollback Guide          |
| ESD     | Enterprise Service Desk                                         |
| FOIA    | Freedom Of Information Act                                      |
| HIG     | Health Information Governance                                   |
| HCS     | Healthcare System                                               |
| HIPAA   | Health Insurance Portability and Accountability Act             |
| IG      | Inspector General                                               |
| IOC     | Initial Operating Capability                                    |
| ISSO    | Information System Security Officer                             |
| KIDS    | Kernel Installation and Distribution System                     |
| MUMPS   | Massachusetts General Hospital Utility Multi-Programming System |
| N/A     | Not Applicable                                                  |
| NPM     | National Patch Module                                           |
| OIT     | Office of Information & Technology                              |
| PHI     | Protected Health Information                                    |
| PII     | Personal Identifiable Information                               |
| PMO     | Project Management Office                                       |
| SQA     | Software Quality Assurance                                      |
| UAT     | User Acceptance Testing                                         |
| UI      | User Interface                                                  |
| VA      | Department of Veterans Affairs                                  |
| VAEC    | Veterans Affairs Enterprise Cloud                               |
| VAMC    | Veterans Administration Medical Center                          |
| VAS     | VistA Audit Solution                                            |
| VDL     | VA Software Document Library                                    |
| VistA   | Veterans Health Information Systems Technology Architecture     |

""

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DG*5.3*1097 Deployment, Installation, Back-out, Rollback Guide

### VistA Patch DG\*5.3\*1097 Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build.
2.  Choose the “INSTALL/CHECK MESSAGE PackMan” option to load the build.
3.  From the Kernel Installation and Distribution System Menu, select the “Installation” Menu. From this menu,
    1.  Select the “Verify Checksums in Transport Global” option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch name, DG\*5.3\*1097.
    2.  Select the “Backup a Transport Global” option to create a backup message. You can specify what to backup, the entire Build or just Routines. The backup message can be used to restore just the routines or everything that will restore your system to pre-patch condition. Select “B” for Build (including Routines) at the “Backup Type:” prompt.
    3.  You may also elect to use the following options:
        1.  Print Transport Global – This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System – This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install DG\*5.3\*1097.
5.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer YES.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

### From: DG*5.3*1108 Deployment, Installation, Back-out, Rollback Guide

### VistA Patch DG\*5.3\*1108 Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build.
2.  Choose the “INSTALL/CHECK MESSAGE PackMan” option to load the build.
3.  From the Kernel Installation and Distribution System Menu, select the “Installation” Menu. From this menu,
    1.  Select the “Verify Checksums in Transport Global” option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME, enter the patch name, DG\*5.3\*1108.
    2.  Select the “Backup a Transport Global” option to create a backup message. You can specify what to backup, the entire Build or just Routines. The backup message can be used to restore just the routines or everything that will restore your system to pre-patch condition. Select “B” for Build (including Routines) at the “Backup Type:” prompt. See Section 4.8.1.1 for more details.
    3.  You may also elect to use the following options:
        1.  Print Transport Global – This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System – This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install DG\*5.3\*1108.
5.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

### From: DG*5.3*1120 Deployment, Installation, Back-out, Rollback Guide

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

Table 4: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |
