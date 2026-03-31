---
consolidated_title: "ar installation guide"
app_code: PRCA
doc_type: IG
master_source: "PRCA*4.5*341 AR Installation Guide"
master_pub_date: August 2018
consolidated_from: 2 versions
prior_versions:
  - "PRCA*4.5*310 AR Installation Guide"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Health Administration Product Enhancements (HAPE) FY16 Revenue Enhancements Maintenance

  Correct 5B Record for Cross-Servicing

  Accounts Receivable

  PRCA\*4.5\*341

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](prca-4-5-341-ar-installation-guide/001.png)

August 2018

Office of Information and Technology (OI&T)

Revision History

| Date  | Version | Description           | Author |
|-----------|-------------|---------------------------|------------|
| 7/17/2018 | 1.0         | Initial Document Creation | REDACTED   |

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
  - [Implementation Procedure](#implementation-procedure)
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
This document describes how to deploy and install the Revenue Enhancements Maintenance, CORRECT 5B RECORD FOR CROSS-SERVICING, Accounts Receivable patch PRCA\*4.5\*341 as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Revenue Enhancements Maintenance, CORRECT 5B RECORD FOR CROSS-SERVICING, Accounts Receivable patch PRCA\*4.5\*341 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. It is a follow-up patch to Accounts Receivable patch PRCA\*4.5\*339 and as such patch \*339 must be installed before patch \*341.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. The only constraint associated with the patch installation is that patch PRCA\*4.5\*339 must be installed before this patch can be installed.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| Team                                                                                                                   | Phase / Role | Tasks                                                                                                           |
|----------------------------------------------------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|
| Health Product Support                                                                                                     | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                 |
| Health Product Support and existing local VAMC and CPAC processes                                                          | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          |
| Health Product Support and VIP Release Agent                                                                               | Deployment       | Test for operational readiness                                                                                      |
| Health Product Support                                                                                                     | Deployment       | Execute deployment                                                                                                  |
| Designated VistA patch installer for this package                                                                          | Installation     | Plan and schedule installation                                                                                      |
| Designated VistA patch installer for this package and VIP Release Agent                                                    | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                       |
| CPAC Revenue Analysts                                                                                                      | Installations    | Coordinate training                                                                                                 |
| Designated VistA patch installer for this package, and CPAC Revenue Analysts, Health Product Support, and Development Team | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |
| Product Development Team during warranty period, afterwards (software only) Tier 1, Tier 2, Tier 3 / VistA Maintenance     | Post Deployment  | Hardware, Software and System Support                                                                               |

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a simultaneous national rollout to all VistA production instances. This section provides the schedule and milestones for the deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for 30 days starting with the National Release date and concluding with the National Compliance date by which time all VistA production instances should have the patch installed.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Revenue Enhancements Maintenance, CORRECT 5B RECORD FOR CROSS-SERVICING, Accounts Receivable patch PRCA\*4.5\*341 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for a VistA patch.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All VistA production instances. The IOC test sites for this project were Durham (558), Central Alabama HCS (619), and Upstate NY HCS (528).

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None required other than prerequisite patch installation as described in the patch description and in the Forum NPM.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Revenue Enhancements Maintenance, CORRECT 5B RECORD FOR CROSS-SERVICING, Accounts Receivable patch PRCA\*4.5\*341 is a VistA patch and does not require any special or specific resources other than an existing and functional VistA system.

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific hardware required other than that which already hosts the VistA system. This is a software enhancement that will not require additional hardware.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no specific software required other than that which already hosts the VistA system.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When VistA patches are nationally released from the Forum National Patch Module (NPM) the patch is automatically sent to the targeted VistA systems nationwide. When VistA patches are installed at a site, a notification is sent back to the NPM in order to track which sites have and have not installed a patch. This is part of the standard VistA patch notifications and communications protocols.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch PRCA\*4.5\*341, which is tracked in the NPM in Forum, nationally to all VAMCs. Forum automatically tracks the patches as they are installed in the different VAMC production systems as described in the previous section. One can run a report in Forum to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not installed the patch in their VistA production system as of that moment in time.

Therefore, this information does not need to be manually tracked in the chart below. The table is included below if manual tracking is desired and because it is part of the VIP document template.

Table 6: 3.3.4.1 Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. The only pre-installation and system requirements for deployment and installation of this patch are the prerequisite patches which need to be installed before this patch can be installed.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. The only requirement is that patch PRCA\*4.5\*339 be installed before patch PRCA\*4.5\*341.

Sites should install patches into the test/mirror/pre-prod accounts before the production account as is the normal VistA patch installation standard convention.

When installing any VistA patch, sites should utilize the option “Backup a Transport Global” in order to create a backup message of any routines exported with this patch. This step is important to make any routine rollback in a simple and efficient manner.

Post-installation checksums are found in the patch description and in Forum NPM.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install this VistA patch, the patch installer must be an active user on the VistA system and have access to the VistA menu option “Kernel Installation & Distribution System” \[XPD MAIN\] and have VistA security keys XUPROG and XUPROGMODE. Knowledge on how to install VistA patches using the items on this menu option is also a required skill.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions:

--------------------------

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation and Distribution System Menu, select the

Installation Menu. From this menu, you may elect to use the following

options. When prompted for the INSTALL NAME enter PRCA\*4.5\*341.

a\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not backup

any other changes such as DDs or templates.

b\. Compare Transport Global to Current System - This option will allow you

to view all changes that will be made when this patch is installed. It

compares all components of this patch routines, DDs, templates, etc.

c\. Verify Checksums in Transport Global - This option will allow you to

ensure the integrity of the routines that are in the transport global.

4\. From the Installation Menu, select the Install Package(s) option and

choose the patch to install.

5\. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//'

Enter NO

6\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//' Enter NO

7\. If prompted 'Delay Install (Minutes): (0 - 60): 0//' respond 0.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify completed installation by comparing the post-install routine checksums against the published checksums in the patch description and in Forum NPM.

## Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out plan for VistA applications is complex and is not able to be a “one size fits all” strategy. The general strategy for VistA software back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch; otherwise, the site should contact the Enterprise Program Management Office (EPMO) directly for specific solutions to their unique problems.

Although it is unlikely due to care in collecting approved requirements, SQA/PBM review and multiple testing stages (Primary Developer, Secondary Developer, and Component Integration Testing) a back-out decision due to major issues with this patch could occur during site Mirror Testing, Site Production Testing or after National Release to the Field. The strategy would depend on during which of these stages the decision is made. If during Site Production Testing, unless the patch produces catastrophic problems, the normal VistA response would be for a new version of the test patch correcting defects to be produced, retested and upon successfully passing development team testing would be resubmitted to the site for testing. This project, however, has prepared a set of back-out patch instructions if necessary, as in the case that the project is canceled or the implemented design is found to be so wrong and detrimental to the site’s delivery of services to veterans that the software must be removed. If the defects were not discovered until after national release but during the 30 days support period, a new patch will be entered into the National Patch Module on Forum and go through all the necessary milestone reviews etc. as an emergency patch. After 30 days, the VistA Maintenance Program would produce the new patch, either to correct the defective components or to back-out.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if a wholesale back-out of the patch PRCA\*4.5\*341 is needed or if a better course of action is to correct through a new version of the patch (if prior to national release) or through a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale back-out of the patch will still require a new version (if prior to national release) or a subsequent patch (after national release). If the back-out is post-release of patch PRCA\*4.5\*341, this patch should be assigned status of “Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is detailed in the User Stories in Rational Tools Management.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to back-out this VistA patch will be made by Health Product Support, CPAC Revenue System Management staff, and the Development Team. Criteria to be determined based on separate and unique factors and will be evaluated upon post-patch installation use of the product.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out authorization will be determined by a consensus consisting of the following individuals:

- Health Product Support Management
- Release Managers
- CPAC Revenue System Managers
- Development Team

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer can back up the modified routines using the ‘Backup a Transport Global’ action. The installer can restore the routines using the MailMan message that were saved prior to installing the patch. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with restoration of the data. This back-out may need to include a database cleanup process.

Please contact the EPMO for assistance if the installed patch that needs to be backed out contains anything at all besides routines before trying to back-out the patch. If the installed patch that needs to be backed out includes a pre or post install routine please contact the EPMO before attempting the back-out.

From the Kernel Installation and Distribution System Menu, select

the Installation Menu. From this menu, you may elect to use the

following option. When prompted for the INSTALL enter the patch \#.

    a. Backup a Transport Global - This option will create a backup

       message of any routines exported with this patch. It will not

       backup any other changes such as DD's or templates.

Locate the Transport Global Backup message which should have been created as a part of the patch installation and restore the software from that Packman message containing the pre-installation version of the routines. If this message was not created or cannot be found, then contact Health Product Support for help in generating a new Packman message from another source.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The success of the back-out can be verified by verifying checksums for the routines removed to validate that they reflect the nationally released checksums.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data associated with this patch.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch as there is no data associated with this patch.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch as there is no data associated with this patch.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch as there is no data associated with this patch.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch as there is no data associated with this patch.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch as there is no data associated with this patch.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A for this VistA patch as there is no data associated with this patch.

Template Revision History

| Date          | Version | Description                                                                                                                                                                                                                              | Author                                 |
|---------------|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| March 2016    | 2.2     | Changed the title from Installation, Back-Out, and Rollback Guide to Deployment and Installation Guide, with the understanding that Back-Out and Rollback belong with Installation.                                                      | VIP Team                               |
| February 2016 | 2.1     | Changed title from Installation, Back-Out, and Rollback Plan to Installation, Back-Out, and Rollback Guide as recommended by OI&T Documentation Standards Committee                                                                      | OI&T Documentation Standards Committee |
| December 2015 | 2.0     | The OI&T Documentation Standards Committee merged the existing *“Installation, Back-Out, Rollback Plan”* template with the content requirements in the OI&T End-user Documentation Standards for a more comprehensive Installation Plan. | OI&T Documentation Standards Committee |
| February 2015 | 1.0     | Initial Draft                                                                                                                                                                                                                            | Lifecycle and Release Management       |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PRCA*4.5*310 AR Installation Guide

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These three patches have enhancements that extend the capabilities of the Veterans Health Information Systems and Technology Architecture (VistA), Accounts Receivable (PRCA), Fee Basis (FB), and Integrated Billing (IB). Below is a list of all the applications involved in this project along with their patch number:

| Application/Version         | Patch          |
|-----------------------------|----------------|
| ACCOUNTS RECEIVABLE V 4.5   | PRCA\*4.5\*310 |
| FEE BASIS (FB) V 3.5        | FB\*3.5\*163   |
| INTEGRATED BILLING (IB) 2.0 | IB\*2.0\*554   |

The patches (PRCA\*4.5\*310, FB\*3.5\*163, and IB\*2.0\*554) are being released in the Kernel Installation and Distribution System (KIDS).

The Chief Business Office (CBO) is requesting system enhancements to the VistA IB, AR, and FB software modules that would allow segregating all billing and Collection activities for Non-Department of Veterans Affairs (Non-VA) Care Third Party Insurance carriers' reimbursement.

Current Medical Care Collections Fund (MCCF) Third Party billing and collections applications in the VistA information system do not segregate the Non-VA care claims from those claims for service rendered at Veterans Health Administration (VHA) healthcare facilities. This makes it difficult to determine whether all monies due VA for Non-VA care services are being billed and collected from Third Party insurance carriers, where applicable. The current process is a resource intensive, manual process with no assurance that all applicable Non-VA charges have been billed and collected.

This project will improve and automate the transfer of data from VistA Fee Basis to Integrated Billing. It will record Non-VA revenue in a different fund to allow separate tracking of these revenues. The patch makes the following changes and enhancements:

This patch creates entries in several AR files to support the new Rate Type of FEE REIMB INS. This new rate type is similar to REIMBUR. INS and is used to segregate revenue generated by third party reimbursement of fee-based Non-VA Care. There are minor changes to revenue reports to properly display the segregated revenue.

1.  An entry was added to the RATE TYPE file (#399.3) for FEE REIMB INS
2.  An entry was added to the ACCOUNTS RECEIVABLE CATEGORY FILE (#430.2) for FEE REIMB INS.
3.  Entries were added to the REVENUE SOURCE CODE FILE (#347.3) for FEE BASIS INPATIENT (8F1Z) and FEE BASIS OUTPATIENT (8F2Z).
4.  An entry was added to PRCD FUND FILE (#420.14) for 528713 (MCCF-FEE-COLL FUND-3RD PARTY).
5.  An entry was added to PRCD FUND/APPROPRIATION CODE FILE (#420.3) for fund 528713.
6.  Option PRCA FMS RSC REPORT (Revenue Source Code Report) was updated to properly display the new revenue.
7.  Option PRCA DEPOSIT RECON REPORT (Deposit Reconciliation Report) was updated to include the new fund.
8.  Option PRCA FMS RSC CALCULATE (Calculate Revenue Source Code For a Bill) was updated to include the new source codes.
9.  Option PRCA NR BAD DEBT ACCR. REPORT (Bad Debt Report) was updated to include the new fund.

### Document Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this bundle is available from the VA SFTP server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

Albany:                 REDACTED

Hines:                  REDACTED   

Salt Lake City:         REDACTED

  

Documentation can also be found on the VA Software Documentation Library at:

<http://www.va.gov/vdl/>

Title File Name Transfer Mode

-------------------------------------------------------------------------------------------

Release Notes prca_4_5_p310_rn.pdf Binary

Installation Guide prca_4_5_p310_ig.pdf Binary

Technical/Security Manual prca_4_5_p310_tm.pdf Binary

\*User manual did not change so it wasn’t included.

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install. The following patches must be installed before PRCA\*4.5\*310:

- FB\*3.5\*154
- FB\*3.5\*166
- IB\*2.0\*528
- IB\*2.0\*530

## Pre/Post-Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Retrieval 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PRCA\*4.5\*310 must be retrieved from FORUM. The resulting email should then be forwarded to the local server for installation.

## Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vista Installation Instructions

Users should not use the application while the patch is being installed. Once the patch has completed the users can use VistA - Accounts Receivable applications again. This VistA patch should take less than 5 minutes to install. This is patch the first of a three patch install (PRCA\*4.5\*310, IB\*2.0\*554 then FB\*3.5\*163)

1.  Once the email with the KIDs build is received, extract the KIDs distribution.
2.  Next, from the Kernel Installation and Distribution System Menu, users may elect to use the following options. When prompted for the INSTALL name enter the patch PRCA\*4.5\*310:
1.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
2.  Print Transport Global – This option allows the user to print the Transport Global Report
3.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD’s, templates, etc.).
4.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD’s or templates.
3.  From the Installation Menu, select the Install Package(s) option and enter PRCA\*4.5\*310.
4.  If prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’ answer NO and press enter.
5.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? YES//’ answer NO and press enter.
6.  When prompted 'Want to DISABLE Scheduled Options, Menu Options. and Protocols? NO//' answer YES and press enter.

    Mark the following options as Out of Order:

    Revenue Source Code Report \[PRCA FMS RSC REPORT\]

    Calculate Revenue Source Code for a Bill \[PRCA FMS RSC CALCULATE\]

    Bad Debt Report \[PRCA NR BAD DEBT ACCR. REPRT\]

    Deposit Reconciliation Report \[PRCA DEPOSIT RECON REPORT\]
7.  If prompted ‘Delay Install (Minutes): (0 – 60): 0//’ respond 0 and press enter.
8.  There are no installation routines to delete.

## Routine Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the routine(s) included in this build. The second line of each routine will look as follows:

4.5;Accounts Receivable;\*\*\[Patch List\]\*\*;Mar 20, 1995;Build 9

Routine New Checksum Value

----------------------------------------------------------------

> PRCAACC value = 8690733

> PRCAP310 value = 14220826

> RCRJRBD value = 71069884

> RCRJRBDT value = 56390324

> RCRJRDEP value = 64337684

> RCTRAN1 value = 8190500

> RCXFMSPR value = 27613579

> RCXFMSUF value = 37450656

> RCXFMSUR value = 61048579

## Post-Install Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post-install routine is PRCAP310. It performs the following four functions:

- Creates the FEE REIMB INS entry in AR CATEGORY FILE (#430.2)
- Creates two entries in the REVENUE SOURCE CODE FILE (#347.3), 8F1Z (FEE BASIS INPATIENT) and 8F2Z (FEE BASIS OUTPATIENT)
- Creates fund 528713 in the PRCD FUND FILE (#420.14)
- Creates fund 528713 in PRCD FUND/APPROPRIATION CODE FILE (420.3)
