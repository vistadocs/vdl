---
consolidated_title: "pharmacy operational updates deployment, installation, back-out, and rollback guide"
app_code: PSO
doc_type: DIBR
master_source: "PSO*7*684 Pharmacy Operational Updates Deployment, Installation, Back-out, and Rollback Guide"
master_pub_date: August 2022
consolidated_from: 4 versions
prior_versions:
  - "PSO*7.0*667 Pharmacy Operational Updates Deployment, Installation, Back-out, and Rollback Guide"
  - "PSO*7*676 Pharmacy Operational Updates Deployment, Installation, Back-out, and Rollback Guide"
  - "PSO*7*701 Pharmacy Operational Updates Deployment, Installation, Back-out, and Rollback Guide"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Pharmacy Operational Updates (POU)

  PSO\*7.0\*684

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](pso-7-684-pharmacy-operational-updates-deployment-installation-back-out-and-roll/001.png)

August 2022

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description | Author           |
|------------|-------------|-----------------|----------------------|
| 07/25/2022 | 1.0         | Initial Version | Liberty IT Solutions |

Table 2:Timeline

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
This document describes how to install the Pharmacy Operational Updates (POU) project’s VistA Patch PSO\*7.0\*684, as well as how to back-out the patch and rollback to a previous version or data set. This patch, in conjunction with Outpatient Pharmacy patch PSO\*7.0\*684, implements enhancements to VistA Drug Enforcement Agency (DEA) functionality. This patch primarily contains updates to data dictionaries that store DEA related information.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the PSO\*7.0\*684 patch will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VistA patches must be installed at the site:

- PSO\*7.0\*630
- PSO\*7.0\*667
- XU\*8.0\*688

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended to be installed in a fully patched Veterans Health Information Systems and Technology Architecture (VistA) system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                                                                                                                                           | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | VA Office of Information and Technology (OIT), VA OIT Health Product Support, and PMO (Liberty)                                                    | Deployment       | Plan and schedule deployment.                                                                                       | Planning                         |
| 2      | Health Product Support and Field Operations                                                                                                        | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          | Planning                         |
| 3      | Field Testing (Initial Operating Capability-IOC), Health Product Support Testing & Veteran-Focused Integrated Process (VIP) Release Agent Approval | Deployment       | Test for operational readiness                                                                                      | Testing                          |
| 4      | Health Product Support and Field Operations                                                                                                        | Deployment       | Execute deployment                                                                                                  | Deployment                       |
| 5      | Individual Veterans Administration Medical Centers (VAMCs)                                                                                         | Installation     | Plan and schedule installation                                                                                      | Deployment                       |
| 6      | Facility Chief Information Officer (CIO) and OIT support, which may be local or regional                                                           | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                       |
| 7      | VA OIT, VA OIT Product Support, and the Liberty Development Team                                                                                   | Post Deployment  | Hardware, Software and System Support                                                                               | Warranty                         |

Table 3: Deployment/Installation/Back-Out Checklist

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national general availability release. The scheduling of test/mirror installs, testing, and the deployment to production will be at the sites’ discretion.

A National Release is planned after testing has been successfully completed at initial operating capability (IOC) test sites.

Deployment will be performed by the local or regional OIT staff and supported by team members from these organizations: Field Operations (FO) and Enterprise Operations. Other teams may provide additional support.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for 31 days, as depicted in the master deployment schedule for Pharmacy Operational Updates Optional Release 2.

| Task              | Start | Finish |
|-------------------|-------|--------|
| National Release  | TBD   | TBD    |
| Compliance Period | TBD   | TBD    |

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will install patch PSO\*7.0\*684.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release is a patch intended for installation at local sites.

Health Product Support Patch Release of Products and Patches Guide: <u>[Health Product Support Release of Products and Patches Guide](https://dvagov.sharepoint.com/sites/OITProcessAssetLibrary/Lists/standards/Item/displayifs.aspx?List=cd84e79a%2D87c9%2D4bcb%2Da129%2D7f486c5c461f&ID=1914&Web=21d14176%2Dbb3c%2D47eb%2Da14f%2D0ce3606c4803).</u>

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IOC sites are:

- Coatesville, PA
- Heartland-West HCS
- Tennessee Valley HCS

Upon National Release, all VAMCs are expected to install this patch prior to or on the compliance date. The software will be distributed in Forum.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch does not require any site preparations other than the prerequisite patch installations as described in the Patch Description and in the National Patch Module (NPM) in Forum.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy patch PSO\*7.0\*684 is a VistA patch and does not require any special or specific resources other than an existing and functional VistA system.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific hardware required other than that which already hosts the VistA system. This is a software enhancement that will not require additional hardware.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific software required other than that which already hosts the VistA system.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA patches are nationally released from the Forum NPM, the patch is automatically sent to the targeted VistA systems nationwide. When VistA patches are installed at a site, a notification is sent back to the NPM to track which sites have and have not installed a patch. This is part of the standard VistA patch notifications and communications protocols.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch PSO\*7.0\*684, which is tracked in the NPM in Forum, nationally to all VAMCs. Forum automatically tracks the patches as they are installed in the different VAMC production systems as described in the previous section. One can run a report in Forum to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run to identify which sites have not installed the patch in their VistA production system as of that moment in time.

Therefore, this information does not need to be manually tracked. Table 3 is included below if manual tracking is desired and because it is part of the VIP document template.

| Activity | Day | Time | Individual Who Completed Task |
|----------|-----|------|-------------------------------|
| Deploy   | TBD | TBD  | TBD                           |
| Install  | TBD | TBD  | TBD                           |
| Back-Out | TBD | TBD  | TBD                           |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. The only pre-installation and system requirements for deployment and installation of this patch are the prerequisite patches which need to be installed before this patch can be installed*.*

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. Sites should install patches into the test/mirror/pre-prod accounts before the production account as is the normal VistA patch installation standard convention. When installing any VistA patch, sites should utilize the option “Backup a Transport Global” in order to create a backup message of any routines exported with this patch. Post-installation checksums are found in the Patch Description and in Forum NPM.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download and extract files are not applicable for this VistA patch.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database creation is not applicable for this VistA patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation scripts are not applicable for this VistA patch.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cron scripts are not applicable for this VistA patch.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install this VistA patch, the patch installer must be an active user on the VistA system and have access to the VistA menu option “Kernel Installation & Distribution System” \[XPD MAIN\] and have VistA security keys XUPROG and XUPROGMODE. Knowledge on how to install VistA patches using the items on this menu option is also a required skill*.*

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ATTENTION: The installation of this patch must be queued. If installation is attempted without queueing, the installation will be aborted, and the distribution must then be unloaded, reloaded, and reinstalled with queuing.

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch may take up to 12 hours to install. This time may vary considerably depending on the number of records migrated by the post-install routine.

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu:
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name PSO\*7.0\*684.
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup; the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
        1.  At the Installation option menu, select Backup a Transport Global
        2.  At the Select INSTALL NAME prompt, enter build PSO\*7.0\*684.
        3.  When prompted for the following, enter "R" for Routines or "B" for Build.

> Select one of the following:

> B Build

> R Routines

> Enter response: Build

4.  When prompted "Do you wish to secure this message? NO//", press \<enter\> and take the default response of "NO".
5.  When prompted with, "Send mail to: Last name, First Name", press \<enter\> to take default recipient. Add any additional recipients.
6.  When prompted with "Select basket to send to: IN//", press \<enter\> and take the default IN mailbox or select a different mailbox.
3.  You may also elect to use the following options:
    1.  Print Transport Global - This option will allow you to view the components of the KIDS build.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
    1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
    2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
    3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.
        1.  When prompted 'Enter protocols you wish to mark as 'Out Of Order':', press the Enter key.
        2.  When prompted 'Delay Install (Minutes): (0 - 60): 0//', answer 0.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

ATTENTION: The DEA migration process performed by the post-install routine may

take up to 12 hours to complete. This time will vary depending on the

number of entries in the NEW PERSON file containing DEA numbers.

This process should have no effect on end users.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Verify completed installation by comparing the post-install routine checksums against the published checksums in the Patch Description and in Forum NPM.

Another verification method is to ensure that the build components as listed in the Patch Description have been correctly installed onto the target VistA system.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System configuration is not applicable for this VistA patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database tuning is not applicable for this VistA patch.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to installing the updated KIDS package, the site/region should have saved a backup of the routines in a mail message using the Backup a Transport Global \[XPD BACKUP\] menu option. The message containing the backed-up routines can be loaded with the “Xtract PackMan” function at the Message Action prompt. The PackMan function INSTALL/CHECK MESSAGE is then used to install the backed-up routines onto the VistA system.

The development team recommends that sites log a ticket if it is a nationally released patch; otherwise, the site should contact the Enterprise Program Management Office (EPMO) directly for specific solutions to their unique problems.

Although it is unlikely due to care in collecting approved requirements, Software Quality Assurance (SQA) review and multiple testing stages (Unit testing, Component Integration Testing, User Acceptance Testing) a back-out decision due to major issues with this patch could occur during site Mirror Testing, Site Production Testing, or after National Release to the Field. The strategy would depend on during which of these stages the decision is made. If during Site Production Testing, unless the patch produces catastrophic problems, the normal VistA response would be for a new version of the test patch correcting defects to be produced, retested and upon successfully passing development team testing would be resubmitted to the site for testing. If the defects were not discovered until after National Release but during the 30 days support period, a new patch will be entered into the NPM on Forum and go through all the necessary milestone reviews, etc. as an emergency patch.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if a back-out of the patch PSO\*7.0\*684 is needed, or if issues may be adequately addressed via a new version of the patch (if prior to National Release) or through a subsequent patch (if after National Release).

A back-out of the patch will require a new test version (if prior to National Release) or a subsequent patch (if after National Release). If the back-out is post-release of patch PSO\*7.0\*684, patch PSO\*7.0\*684 should be assigned status of “Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load Testing is not applicable for this VistA patch.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance *Testing is in progress.*

The decision to back-out this VistA patch will be made by Health Product Support, CPAC Revenue System Management staff, and the Development Team. Criteria to be determined based on separate and unique factors and will be evaluated upon post-patch installation use of the product.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out risks are not applicable for this VistA patch.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any back-out decision should be a joint decision of the Business Owner (or their representative) and the Program Manager with input from theHealth Product Support (HPS) Application Coordinator, HPS Support, and the project development team.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out plan for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a Nationally Released patch.

If it is prior to National Release, the site will be already working directly with the development team and should contact that team. The development team members will have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that the development team can quickly address via a new software version. If the site is unsure whom to contact, they may log a ticket or contact Health Product Support - Management Systems Team.

Patch PSO\*7.0\*684 contains the build components listed below.

Patch PSO\*7.0\*684 installs the following routines:

| Routine Name | New/Modified |
|------------------|------------------|
| PSO7E684         | New              |
| PSO7L529         | Modified         |
| PSO7P684         | New              |
| PSODEARP         | Modified         |
| PSODEAU0         | Modified         |
| PSODEAUT         | Modified         |

Patch PSO\*7.0\*684 installs the following options:

| Option Name          | Option Text      | New/Modified |
|--------------------------|----------------------|------------------|
| PSO DEA MIGRATION REPORT | DEA Migration Report | New              |

While the VistA KIDS installation procedure allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action, the back-out procedure for global, data dictionary and other VistA components is more complex and requires issuance of a follow-up patch to ensure all components are properly removed and/or restored. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with the restoration of the data. Please contact the EPMO team for assistance since this installed patch contains components in addition to routines.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful back-out is confirmed by verification that the back-out patch was successfully implemented, including verification that new components were removed and modified components were returned to their pre-patch state.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. The data changes in this patch are specific to the operational software and platform settings. These data changes are covered in the Back-out procedures detailed elsewhere in this document. Rollback is not applicable to this VistA patch.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSO*7.0*667 Pharmacy Operational Updates Deployment, Installation, Back-out, and Rollback Guide

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to back-out this VistA patch will be made by Health Product Support, CPAC Revenue System Management staff, and the Development Team. Criteria to be determined based on separate and unique factors and will be evaluated upon post-patch installation use of the product.

### From: PSO*7*676 Pharmacy Operational Updates Deployment, Installation, Back-out, and Rollback Guide

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                               |                        |
|-------------------------------|------------------------|
| Package                       | Minimum Version Needed |
| VA FileMan                    | 22.0                   |
| Kernel                        | 8.0                    |
| MailMan                       | 8.0                    |
| Health Level 7                | 1.6                    |
| Order Entry/Results Reporting | 3.0                    |
| CMOP                          | 2.0                    |
| NDF                           | 4.0                    |
| Outpatient Pharmacy           | 7.0                    |
| Pharmacy Data Management      | 1.0                    |
| Controlled Substances         | 3.0                    |
| Toolkit                       | 7.3                    |
| Drug Accountability           | 3.0                    |

## Installation from the Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu.
1.  From the Kernel Installation and Distribution System (KIDS) menu, select the Installation menu.
2.  From this menu, you may select to use the following options; when prompted for INSTALL NAME, enter PSO\*7.0\*676.
1.  Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.
1.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
2.  Verify Checksums in Transport Global - This option will ensure the integrity of the routines that are in the transport global.
3.  Print Transport Global - This option will allow you to view the components of the KIDS build.
3.  Use the Install Package(s) option and select the package PSO\*7.0\*676.
4.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//" respond NO.
5.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond NO.
6.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.

## Post-Install Routine (No Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no post-installation instructions for this patch.

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this patch is available.

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 47%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>File Description</th>
<th>File Name</th>
<th>FTP Mode</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Outpatient Pharmacy (PSO) Supplemental User Manual</td>
<td><p>PSO_7_SUP_UM.DOCX</p>
<p>PSO_7_SUP_UM.PDF</p></td>
<td></td>
</tr>
</tbody>
</table>

Documentation can also be retrieved from the VA Software Documentation Library (VDL) on the Internet at the following path: https://www.va.gov/vdl/.
