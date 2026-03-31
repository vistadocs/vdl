---
consolidated_title: "vista imaging exchange (vix) deployment, installation, back-out, and rollback guide"
app_code: MAG
doc_type: DIBR
master_source: "VistA Imaging Exchange (VIX) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)"
master_pub_date: January 2025
consolidated_from: 5 versions
prior_versions:
  - "MAG*3*269 VistA Imaging Exchange (VIX) Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)"
  - "MAG*3*303 VistA Imaging Exchange (VIX) Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)"
  - "MAG*3*329 VistA Imaging Exchange (VIX) Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)"
  - "MAG*3*348 VistA Imaging Exchange (VIX) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)"
---

---
title: |
  VistA Imaging eXchange (VIX) Enhancements and Maintenance

  MAG\*3.0\*<span id="PatchNumber" class="anchor"></span>358

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](vista-imaging-exchange-vix-deployment-installation-back-out-and-rollback-guide-d/001.png)

January 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date       | Revision | Description                                     | Author                              |
|------------|----------|-------------------------------------------------|-------------------------------------|
| 01/06/2025 | 9.2      | Additional updates based on peer review.        | VA IT VistA Imaging Technical team  |
| 11/04/2024 | 9.1      | Updates based on peer review.                   | VA IT VistA Imaging Technical team  |
| 10/01/2024 | 9.0      | Initial Draft for MAG\*3.0\*358.                | VA IT VistA Imaging Technical team  |
| 01/02/2024 | 8.3      | Updates for MAG\*3.0\*348 release date.         | VA IT VistA Imaging Technical team  |
| 12/01/2023 | 8.2      | Updates for MAG\*3.0\*348 release date.         | VA IT VistA Imaging Technical team  |
| 11/01/2023 | 8.1      | Updates for MAG\*3.0\*348 release date.         | VA IT VistA Imaging Technical team  |
| 10/01/2023 | 8.0      | Initial Draft for MAG\*3.0\*348.                | VA IT VistA Imaging Technical team  |
| 05/04/2023 | 7.2      | Updates based on peer review.                   | VA IT VistA Imaging Technical team  |
| 05/01/2023 | 7.1      | Updates for MAG\*3.0\*329 release date.         | VA IT VistA Imaging Technical team  |
| 02/01/2023 | 7.0      | Initial Draft for MAG\*3.0\*329.                | VA IT VistA Imaging Technical team  |
| 11/17/2022 | 6.1      | Updates for MAG\*3.0\*303 based on review.      | VA IT VistA Imaging Technical team  |
| 08/17/2022 | 6.0      | Initial Draft for MAG\*3.0\*303.                | VA IT VistA Imaging Technical team  |
| 06/08/2022 | 5.4      | Updates for MAG\*3.0\*269 installation section. | VA IT VistA Imaging Technical team  |
| 06/07/2022 | 5.3      | Updates for MAG\*3.0\*269 release date.         | VA IT VistA Imaging Technical team  |
| 02/18/2022 | 5.2      | Updates for MAG\*3.0\*269 name.                 | VA IT VistA Imaging Technical team  |
| 11/22/2021 | 5.1      | Added MAG\*3.0\*185 as a patch dependency.      | VA IT VistA Imaging Technical team  |
| 10/06/2021 | 5.0      | Initial Draft for MAG\*3.0\*269.                | VA IT VistA Imaging Technical team  |
| 08/31/2021 | 4.0      | Updates for Patch MAG\*3.0\*284 (1.0).          | <span class="mark">REDACTED</span>  |
| 04/06/2021 | 3.0      | Updates for Patch MAG\*3.0\*254.                | VA IT VistA Imaging Technical team  |
| 05/20/2020 | 2.0      | Technical Review.                               | VA IT VistA Imaging Technical team  |
| 03/10/2020 | 1.0      | Initial Version.                                | VA IT VistA Imaging Technical team  |

<span id="_Toc127969244" class="anchor"></span>Table : Definitions, Acronyms, and Abbreviations

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point #2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.
# Table of Tables


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Table of Tables](#table-of-tables)
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
    - [MAG\3.0\358 Client Uninstall](#mag30358-client-uninstall)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Definitions, Acronyms, and Abbreviations](#definitions-acronyms-and-abbreviations)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install the VistA Imaging eXchange (VIX) MAG\*3.0\*358, and how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed commercial-off-the-shelf (COTS) product is being installed, the vendor-provided User and Installation Guide may be used. However, the Back-Out Recovery strategy still needs to be included in this document. This patch adds VIX Viewer improvements, installation enhancements, and performance improvements.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the VistA Imaging eXchange (VIX) MAG\*3.0\*358 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Additional instructions for installation, back-out, and rollback can be found in the [*MAG3_0P<u>358</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105).

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch must be installed after VIX patch MAG\*3.0\*357 (which is installed over MAG\*3.0\*348).

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MAG\*3.0\*358 utilizes existing nationally released security controls to control access.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multiple entities oversee decision-making for deployment, installation, back-out, and rollback of MAG\*3.0\*358. The Account Coordinators can approve deployment and installation from an OI&T perspective. If an issue with the software arises, the facility Chief Information Officer (CIO) or Area Manager and other site leadership will meet along with input from the Clinical Services Diagnostics Sub-Product Line team, and regional leadership to initiate a back-out and rollback decision for the software. Table 1 provides MAG\*3.0\*358 information.

<span id="_Ref82692430" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID  | Team                                                                                                                                                                                                         | Phase/Role      | Tasks                                                                                                                           | Project Phase (See Schedule |
|-----|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------|
| 1   | Site personnel in conjunction with information technology (IT) support – which may be local or regional.                                                                                                     | Deployment      | Plan and schedule deployment (including orchestration with vendors.)                                                            | N/A                         |
| 2   | Site personnel in conjunction with IT support – which may be local or regional.                                                                                                                              | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                                      | N/A                         |
| 3   | Site personnel.                                                                                                                                                                                              | Deployment      | Test for operational readiness.                                                                                                 | N/A                         |
| 4   | Site personnel in conjunction with IT support – which may be local or regional. The IT support must include a person(s) to install the patch and the personnel to deploy the graphical user interface (GUI). | Deployment      | Execute deployment.                                                                                                             | N/A                         |
| 5   | Site personnel in conjunction with IT support – which may be local or regional. The IT support must include a person(s) to install the patch and the personnel to deploy the GUI.                            | Installation    | Plan and schedule installation.                                                                                                 | N/A                         |
| 6   | N/A – will work under the VistA authority to operate (ATO) and security protocols.                                                                                                                           | Installation    | Ensure ATO and certificate authority security documentation is in place.                                                        | N/A                         |
| 7   | N/A – no equipment is being added.                                                                                                                                                                           | Installation    | Validate through facility point of contact (POC) to ensure that IT equipment has been accepted using asset inventory processes. | N/A                         |
| 8   | Site personnel in conjunction with IT support – which may be local or regional.                                                                                                                              | Installation    | N/A An external system is not using VIX MAG\*3.0\*358 functionality at this time.                                               | N/A                         |
| 9   | Facility CIO and IT support – which may be local or regional.                                                                                                                                                | Back-out        | Confirm availability of back-out instructions and back-out strategy (what the criteria are that trigger a back-out.)            | N/A                         |
| 10  | Hardware and System support – no changes. Software support will be the Clinical Services Diagnostics Sub-Product Line team and VistA Imaging Development team.                                               | Post-Deployment | Hardware, Software, and System Support.                                                                                         | N/A                         |

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once approval has been given to nationally release MAG\*3.0\*358, the patch will be released from the National Patch Module. At this point, the patch will be available for installation and deployment at all sites from OI Field Offices using a web browser to download from the following URL: <span class="mark">REDACTED</span>.

This section provides the schedule and milestones for the deployment. Scheduling of test/mirror installs, testing, and deployment to production will be at the site’s discretion. It is anticipated that there will be a 30-day compliance period.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no timeline specifically for deployment. This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period for the release.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the MAG\*3.0\*358 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MAG\*3.0\*358 will be deployed to local sites on the VIX servers.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, MAG\*3.0\*358 will be deployed to:

- <span class="mark">REDACTED</span>

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to [*MAG3_0P<u>358</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105) sections “Preparing for a New VIX Installation” or “Preparing for a VIX Update” for site preparation.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MAG\*3.0\*358 will be deployed using the standard method of patch release from the National Patch Module. When patch MAG\*3.0\*358 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All previously released VistA Imaging patches must be installed on the VistA system before installing MAG\*3.0\*358.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MAG\*3.0\*358 must be installed on-site VIX servers. This patch must be installed on both VistA and site VIX servers by the compliance date.

This patch may be installed during non-peak hours to minimize potential disruption to users. Refer to [*MAG3_0P<u>358</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105) for additional installation preparation steps.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites may retrieve the software and documentation directly using a web browser to download from the following URL: <span class="mark">REDACTED</span> (Table 2).

Documentation can be found on the VA Software Documentation Library at: <u>https://www.va.gov/vdl/application.asp?appid=105</u>

<span id="_Ref79757867" class="anchor"></span>Table 2: Files to be Downloaded

| File Name                             | Description                                                          |
|---------------------------------------|----------------------------------------------------------------------|
| MAG3_0P358_VIX_SETUP.MSI              | MAG\*3.0\*358 VIX Setup                                              |
| MAG3_0P358_PATCH_DESCRIPTION.PDF      | MAG\*3.0\*358 Patch Description                                      |
| MAG3_0P358_VIX_INSTALLATION_GUIDE.PDF | MAG\*3.0\*358 VIX Installation Guide                                 |
| MAG3_0P358_DIBRG.PDF                  | MAG\*3.0\*358 Deployment, Installation, Back-Out, and Rollback Guide |
| MAG3_0P358_VIX_ADMIN_GUIDE.PDF        | MAG\*3.0\*358 VIX Administration Guide                               |

> **NOTE:** Only the VIX client for MAG\*3.0\*358 should be installed at medical centers. As a result, the Central VistA Imaging eXchange (CVIX) Installation Guide (MAG3_0P358_CVIX_INSTALLATION_GUIDE.PDF) and CVIX installation file (MAG3_0P358_CVIX_SETUP.MSI) are not provided to sites on the network file shares.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of VistA Imaging MAG\*3.0\*358 requires the following to install:

- VIX installs – Administrator access to the VIX servers.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For installing or updating the VIX, refer to [*MAG3_0P<u>358</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to [*MAG3_0P<u>358</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105) for the client post installation and verification process.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only reason to consider a back-out for MAG\*3.0\*358 is in the event of a catastrophic failure. Some VIX Clients are dependent on VistA changes and each other. In the case of a backout of the VIX Client, the VistA Patch might also need to rollback.

Submit a Service Now ticket (<span class="mark">REDACTED)</span> to request back-out assistance. Contact the Health, Clinical Services Diagnostics Team (previously known as Clin 3, the group name is SPM.Health.ClinSvs.Diag) team to notify them there has been a catastrophic failure with MAG\*3.0\*358.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing (UAT) was conducted by the test sites listed in section 3.2. The sites followed the provided test plan/concurrence form and executed the test cases according to the plan for the first build of MAG\*3.0\*358. The sites either passed or failed all items based on testing. The tests were performed by IT analysts at each site who are familiar with using the application. Any items that failed were then re-developed, sent back to the sites, and tested for the next build following the same process. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and a significant patient impact issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out MAG\*3.0\*358 would result in the reinstatement of the issues addressed and enhancements added in MAG\*3.0\*358. In addition, there is a risk that the process, which would be performed only in an emergency, would significantly impact patient care due to the interruption.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The facility CIO or Area Manager has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MAG\*3.0\*358 Client Uninstall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For uninstalling the VIX and instructions on reinstalling the previous patch, please see [*MAG3_0P<u>358</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105).

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to [*MAG3_0P<u>358</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105) for verification of the successful VIX client backout procedure.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

If it is necessary to uninstall the MAG\*3.0\*358 VIX, go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*358 VIX Service Installation Wizard. To backout the VIX and replace it with the prior version which was included in MAG\*3.0\*357, please see the [*MAG3_0P<u>358</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105) for more detail.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the rollback to MAG\*3.0\*357, please see the [*MAG3_0P<u>358</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105) for more detail.

# Definitions, Acronyms, and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term  | Definition                                             |
|-------|--------------------------------------------------------|
| ATO   | Authority To Operate                                   |
| CD    | Critical Decision Point                                |
| CIO   | Chief Information Officer                              |
| COTS  | Commercial-Off-The-Shelf                               |
| CVIX  | Centralized VistA Imaging eXchange                     |
| DIBRG | Deployment, Installation, Back-out, and Rollback Guide |
| IOC   | Initial Operating Capability                           |
| IT    | Information Technology                                 |
| KIDS  | Kernel Installation and Distribution System            |
| OIT   | Office of Information and Technology                   |
| POC   | Point of Contact                                       |
| UAT   | User Acceptance Testing                                |
| VA    | Veterans Affairs                                       |
| VIP   | Veteran-Focused Integration Process                    |
| VIX   | VistA Imaging eXchange                                 |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MAG*3*348 VistA Imaging Exchange (VIX) Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)

### MAG\*3.0\*348 VistA Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch installation will take 2-5 minutes.

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch name MAG\*3.0\*348.

    NOTE: Using \<spacebar\>\<enter\> does not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build.
2.  Select the Backup a Transport Global option to create a backup message of any routines exported with this patch. It does not backup any other changes such as DDs or templates.
3.  You may also elect to use the following options:
1.  Print Transport Global – This option allows you to view the components of the KIDS build.
2.  Compare Transport Global to Current System - This option allows you to view all changes made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer \<NO\>
2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer \<NO\>.
3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer \<NO\>

When the installation is finished, an Install Complete message will be displayed.

For installing or updating the VIX, refer to [*<u>MAG3_0P348_VIX_INSTALLATION_GUIDE.PDF</u>*](https://www.va.gov/vdl/application.asp?appid=105).

### MAG\*3.0\*348 Patch Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrators must use the PackMan function INSTALL/CHECK MESSAGE. Check MailMan messages for the backup message sent by the Backup a Transport Global function executed before the patch install. (See section 4.8.1, [Step](#_bookmark27) 2b; this must be done before the patch is installed.)

1.  In VistA MailMan, select the message (Figure 1) shown below:
- Backup of MAG\*3.0\*348 install on *mm dd, yyyyuser name*
3.  Select the Xtract PackMan option.
4.  Select the Install/Check Message option.
5.  Enter Yes at the prompt.
6.  Enter No at the backup prompt. There is no need to back up the backup.

Figure 1: Install/Check Message

### MAG\*3.0\*348 Client Uninstall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For uninstalling the VIX and instructions on reinstalling the previous patch, please see [*MAG3_0P<u>348</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105).

### From: MAG*3*269 VistA Imaging Exchange (VIX) Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)

### MAG\*3.0\*269 VistA Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS installation will take 2-5 minutes.

1.  On the VistA system, access the Kernel Installation and Distribution System Menu \[XPD MAIN\].
2.  Run the Installation option \[XPD INSTALLATION MENU\].
3.  Load the KIDS file by performing the following steps:
1.  Run the Load a Distribution option \[XPD LOAD DISTRIBUTION\] to load the KIDS distribution.
2.  When prompted, enter the full path and file name MAG3_0P269.KID of the MAG\*3.0\*269 KIDS file.
3.  When prompted to continue with the load, enter YES. A Distribution OK! message will be displayed when the load is complete.
4.  After loading the KIDS file, use the following options to verify the contents of the patch and to back up any affected routines.
1.  Verify Checksums in Transport Global \[XPD PRINT CHECKSUM\] – Run this option to ensure the integrity of the routines in the patch.
4.  Compare Transport Global to Current System \[XPD COMPARE TO SYSTEM\] – Run this option to view all changes that will be made when the patch is installed. All components (routines, options, and so on) in the patch will be compared.
5.  <span id="_bookmark27" class="anchor"></span>Backup a Transport Global \[XPD BACKUP\] – Run this option to create a backup message for any routines exported with the patch. It will NOT back up any of the other changes.
5.  After performing the load and any optional verification steps, install the KIDS file by performing the following steps:
1.  Run the Install Package(s) \[XPD INSTALL BUILD\] option.
6.  When prompted for the install name, enter MAG\*3.0\*269.
7.  Answer NO to the following prompts if they appear:
- Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//
- Want KIDS to INHIBIT LOGONs during the install? NO//
- Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//
8.  Answer 0 to the following prompt if it appears:
- Delay Install (Minutes): (0 – 60): 0//

When the installation is finished, an Install Complete message will be displayed.

> **NOTE:** In support of the enhancement to allow commercial PACS, NilRead™, and other query retrieve devices to retrieve remote images, the post-install routine adds the following Remote Procedure Calls (RPCs) to the MAG WINDOWS RPC Context:

- XHD GET SITE INFO
- ORWCIRN FACLIST
- ORRCQLPT PTDEMOS
- ORWU USERINFO
- DSIC DPT GET ICN
- MAG STUDY UID QUERY

For installing or updating the VIX, refer to *MAG3_0P269_VIX_INSTALLATION_GUIDE.PDF*.

### MAG\*3.0\*269 KIDS Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrators must use the PackMan function INSTALL/CHECK MESSAGE. Check MailMan messages for the backup message sent by the Backup a Transport Global function executed before the patch install. (See section 4.8.1, [Step 4c](#_bookmark27); this must be done before the patch is installed.)

1.  In VistA MailMan, select the message (Figure 1) shown below:
- Backup of MAG\*3.0\*269 install on \<mm dd, yyyy\> \<user name\>
6.  Select the Xtract PackMan option.
7.  Select the Install/Check Message option.
8.  Enter Yes at the prompt.
9.  Enter No at the backup prompt. There is no need to back up the backup.

<span id="_Ref79655550" class="anchor"></span>Figure 1: Install/Check Message

### MAG\*3.0\*269 Client Uninstall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For uninstalling the VIX and instructions on reinstalling the previous patch, please see *MAG3_0P269_VIX_INSTALLATION_GUIDE.PDF*.

### From: MAG*3*303 VistA Imaging Exchange (VIX) Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)

### MAG\*3.0\*303 VistA Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KIDS installation will take 2-5 minutes.

1.  This release is provided using a Host file, use the Load a Distribution option contained on the Kernel Installation and Distribution System Menu to load the Host file.

    When prompted to “Enter a Host File:” enter

    /srv/vista/patches/SOFTWARE/MAG3_0P303.KID
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch name MAG\*3.0\*303.

    NOTE: Using \<spacebar\>\<enter\> does not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build.
2.  Select the Backup a Transport Global option to create a backup message of any routines exported with this patch. It does not backup any other changes such as DDs or templates.
3.  You may also elect to use the following options:
1.  Print Transport Global – This option allows you to view the components of the KIDS build.
2.  Compare Transport Global to Current System - This option allows you to view all changes made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer \<NO\>
2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer \<NO\>.
3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer \<NO\>

When the installation is finished, an Install Complete message will be displayed.

For installing or updating the VIX, refer to [*MAG3_0P303_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105).

### MAG\*3.0\*303 KIDS Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrators must use the PackMan function INSTALL/CHECK MESSAGE. Check MailMan messages for the backup message sent by the Backup a Transport Global function executed before the patch install. (See section 4.8.1, [Step 2b](#_bookmark27); this must be done before the patch is installed.)

1.  In VistA MailMan, select the message (Figure 1) shown below:
- Backup of MAG\*3.0\*303 install on *mm dd, yyyyuser name*
3.  Select the Xtract PackMan option.
4.  Select the Install/Check Message option.
5.  Enter Yes at the prompt.
6.  Enter No at the backup prompt. There is no need to back up the backup.

<span id="_Ref79655550" class="anchor"></span>Figure 1: Install/Check Message

### MAG\*3.0\*303 Client Uninstall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For uninstalling the VIX and instructions on reinstalling the previous patch, please see [*MAG3_0P303_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105).

### From: MAG*3*329 VistA Imaging Exchange (VIX) Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)

### MAG\*3.0\*329 Client Uninstall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For uninstalling the VIX and instructions on reinstalling the previous patch, please see [*MAG3_0P<u>329</u>\_VIX_INSTALLATION_GUIDE.PDF*](https://www.va.gov/vdl/application.asp?appid=105).
