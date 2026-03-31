---
title: IB*2*771 Deployment, Installation, Back-out and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2*771
group_key: "IB:IB:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - back
  - patch
  - installation
  - rollback
  - site
  - procedure
  - deployment
  - testing
page_count: 0
word_count: 3037
section_count: 31
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_0_p771_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib_2_0_p771_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

---
title: |
  <span id="_Hlk87958049" class="anchor"></span>Medical Care Collection Fund (MCCF)  
  Electronic Data Interchange (EDI)  
  Transaction Applications Suite (TAS)

  eInsurance IB\*2.0\*771

  Deployment, Installation, Back-out, and Rollback Guide
---

![](ib-2-771-deployment-installation-back-out-and-rollback-guide/001.png)

March 2024

Office of Information and Technology

Revision History

| Date          | Version | Description           | Author                  |
|---------------|---------|-----------------------|-------------------------|
| March 2024    | 1.1     | IOC Exit              | MCCF EDI TAS eInsurance |
| November 2023 | 1.0     | IOC Entry             | MCCF EDI TAS eInsurance |
| October 2023  | 0.1     | Draft version for MOU | MCCF EDI TAS eInsurance |

<span id="_Toc160525040" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

*Template v2.3, July 2021*

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

The Deployment, Installation, Back-out, and Rollback Plan will be updated throughout the lifecycle of the project for each build, as needed.

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
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the IB\*2.0\*771 patch, as well as how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the IB\*2.0\*771 will be deployed and installed, as well as how the patches are to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following patches must be installed before IB\*2.0\*771:

- IB\*2.0\*737
- IB\*2.0\*743
- IB\*2.0\*763

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                                                                                                                                | Phase / Role    | Tasks                                                                                                               | Project Phase (See Schedule) |
|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|------------------------------|
| 1   | VA OIT, VA OIT Health Services Portfolio, and PMO                                                                                                   | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                 | Planning                     |
| 2   | Local VAMC and CPAC processes                                                                                                                       | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment                           | Planning                     |
| 3   | Field Testing (Initial Operating Capability (IOC)), Health Services Portfolio Testing, and Release Readiness Checklist (Self Certification) per PMO | Deployment      | Test for operational readiness                                                                                      | Testing                      |
| 4   | Health Services Portfolio and Field Operations                                                                                                      | Deployment      | Execute deployment                                                                                                  | Deployment                   |
| 5   | Individual Veterans Affairs Medical Centers (VAMCs)                                                                                                 | Installation    | Plan and schedule installation                                                                                      | Deployment                   |
| 6   | Release Readiness Checklist (Self Certification) per PMO                                                                                            | Installation    | Ensure authority to operate and that certificate authority security documentation is in place                       | Deployment                   |
| 7   | N/A for this patch as we are using only the existing VistA system                                                                                   | Installation    | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         | N/A                          |
| 8   | VA’s eBusiness team                                                                                                                                 | Installations   | Coordinate training                                                                                                 | Deployment                   |
| 9   | Health Services Portfolio and the development team                                                                                                  | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                   |
| 10  | No changes to current process – we are using the existing VistA system                                                                              | Post Deployment | Hardware, Software and System Support                                                                               | Warranty                     |

<span id="_Toc160525041" class="anchor"></span>Table 2: Site Preparation

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national rollout.

This section provides the schedule and milestones for the deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for 20 days, starting with the day after national release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the IB\*2.0\*771 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch IB\*2.0\*771 is to be nationally released to all VAMCs.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The test sites for IOC testing are:

- West Palm Beach VAMC (West Palm Beach, FL)
- Biloxi VAMC (Biloxi, MS)
- Ann Arbor VAMC (Ann Arbor, MI)

Upon national release, all VAMCs are expected to install this patch within the compliance dates.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

| Site / Other | Problem / Change Needed | Features to Adapt / Modify to New Product | Actions / Steps | Owner |
|--------------|-------------------------|-------------------------------------------|-----------------|-------|
| N/A          | N/A                     | N/A                                       | N/A             | N/A   |

<span id="_Toc160525042" class="anchor"></span>Table 3: Facility-Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site | Space / Room | Features Needed | Other |
|------|--------------|-----------------|-------|
| N/A  | N/A          | N/A             | N/A   |

<span id="_Toc160525043" class="anchor"></span>Table 4: Hardware Specifications

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware     | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-------|---------|---------------|--------------|-------|
| Existing VistA system | N/A   | N/A     | N/A           | N/A          | N/A   |

<span id="_Toc160525044" class="anchor"></span>Table 5: Software Specifications

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software                                     | Make | Version                     | Configuration | Manufacturer | Other |
|-------------------------------------------------------|------|-----------------------------|---------------|--------------|-------|
| Fully patched Integrated Billing package within VistA | N/A  | 2.0                         | N/A           | N/A          | N/A   |
| IB\*2.0\*737                                          | N/A  | Nationally released version | N/A           | N/A          | N/A   |
| IB\*2.0\*743                                          | N/A  | Nationally released version | N/A           | N/A          | N/A   |
| IB\*2.0\*763                                          | N/A  | Nationally released version | N/A           | N/A          | N/A   |

<span id="_Toc160525045" class="anchor"></span>Table 6: Deployment / Installation / Back-out Checklist

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites that are participating in field testing (IOC) will use the “Patch Tracking” message in Outlook to communicate with the eBusiness eInsurance sub-team, the developers, and product support personnel.

#### Deployment / Installation / Back-out Checklist

The Release Management team will deploy the patch IB\*2.0\*771, which is tracked in the National Patch Module (NPM) in Forum, nationally to all VAMCs. Forum automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in Forum to identify when and by whom the patch was installed in the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch in their VistA production systems. Therefore, this information does not need to be manually tracked in the chart below.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | N/A | N/A  | N/A                           |
| Install  | N/A | N/A  | N/A                           |
| Back-out | N/A | N/A  | N/A                           |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IB\*2.0\*771, a patch to the existing VistA Integrated Billing 2.0 package, is installable on a fully patched M(UMPS) VistA system and operates on top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities which communicate with the underlying operating system and hardware, providing Integrated Billing independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the IB\*2.0\*771 documentation on the NPM on Forum for the detailed installation instructions. These instructions will include any pre installation steps if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the IB\*2.0\*771documentation on the NPM to find the location of related documentation that can be downloaded. IB\*2.0\*771 will be transmitted via a PackMan message and can be pulled from the NPM*.* It is not a host file, and therefore does not need to be downloaded separately.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch does NOT introduce a new database. It uses the existing VistA database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are needed for IB\*2.0\*771 installation*.*

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for IB\*2.0\*771 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following staff need access to the PackMan message containing the IB\*2.0\*771 patch or Forum’s NPM in order to download the nationally released IB\*2.0\*771 patch. The software is to be installed by the sites or regions designated: VA OI&T IT OPERATIONS SERVICE, Enterprise Service Lines, VistA Applications Division[^1], or all.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the IB\*2.0\*771 documentation on the NPM for the detailed installation instructions.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the IB\*2.0\*771 documentation on the NPM for detailed installation instructions. These instructions include any post installation steps if applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required for this patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocations, or other resources is necessary.

# Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known valid instance of operational software and platform settings.

## Back-out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although it is unlikely, due to care in collecting, elaborating, and designing approved user stories, followed by multiple testing stages (Developer Unit Testing, Component Integration Testing, SQA Testing, and User Acceptance Testing), a back-out decision due to major issues with this patch could occur during site Mirror Testing, Site Production Testing, or after National Release to the field (VAMCs). The best strategy is dependent on the stage during which the decision is made.

If during Mirror testing or Site Production Testing, a new version of a defect correcting test patch is produced, retested, and successfully passes development team testing, it would be resubmitted to the site for testing. If the patch produced catastrophic problems, a new version of the patch can be used to restore the build components to their pre-patch condition.

If the defect(s) were not discovered until after national release but during the designated support period, a new patch will be entered into the National Patch Module on Forum and go through all the necessary milestone reviews etc., as a patch for a patch. It is up to VA OIT and product support whether this new patch would be defined as an emergency patch or not. This new patch could be used to address specific issues pertaining to the original patch or could be used to restore the build components to their original pre-patch condition.

After the support period, the VistA Maintenance Program would produce the new patch, either to correct the defective components or to back-out the patch.

## Back-out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if a wholesale back-out of the patch IB\*2.0\*771 is needed or if a better course of action is to correct through a new version of the patch (if prior to national release) or through a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale back-out of the patch will still require a new version (if prior to national release) or a subsequent patch (after national release). If the back-out is post-release of this patch IB\*2.0\*771, this patch should be assigned status of “Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. The back-out process if necessary is executed at normal, rather than raised job priority, and is expected to have no significant effect on total system performance. Subsequent to the reversion, the performance demands on the system would be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Added the new report \[IBCN PT MISSING COVERAGE REPT\] ‘Patient Missing Coverage Report’. This report allows the user to list patients who have an active medical policy / coverage and are potentially missing an active pharmacy policy / coverage.
2.  Added the new report \[IBCN DAILY BUFFER REPORT\] ‘Daily Buffer Report’. This report provides statistics regarding all records in the INSURANCE VERIFICATION PROCESSOR file (#355.33) with a STATUS (#355.33,.04) of “ENTERED”.
3.  Modified the VistA electronic Insurance Verification (eIV) auto-update process to allow a single payer response to update multiple occurrences of that policy on the patient’s record. This will allow insurance verification staff members to link different insurance companies to the same payer and still have the auto-update process multiple polices with a single 271 response.
4.  Enhance VistA option \[IBJD INTAKE INS\] ‘Patients with Unidentified Insurance’ so that: A) the data does not scroll off the screen at the end of the report, B) notify the user that the report runs for a long time and they may wish to queue the report, C) when the report is run to the screen progression dots will be displayed to the screen while the data is being collected.
5.  Modified VistA insurance lookup routine to not error when an invalid record internal entry number is encountered.
6.  Modified View Subscriber Screen in \[IBCN INSURANCE CO EDIT\] 'Insurance Company Entry/Edit' to display message 'Group Contains No Subscribers' when the group does not have any subscribers.
7.  Rebuilt the "LAST" index for the PLAN COVERAGE LIMITATIONS file, LAST EDITED BY (#355.32,1.04) programmatically as FileMan had trouble creating that index at some sites during the installation of IB\*2.0\*763 due to corrupt records.
8.  Modified code to allow VistA to warn FSC if an unexpected X12 code was received in the 271 eIV payer response and had to be added to the appropriate X12 271 file. Increased functionality to allow X12 271 related codes to be added to the following VistA files \#365.011 through \#365.018 (inclusive) and \#365.021.
9.  A new editable general parameter was added to the 'MCCR Site Parameter Display/Edit' \[IBJ MCCR SITE PARAMETERS\] for the 'Ins. Verification' section. The new parameter, 'Daily Buffer Rpt Mail Group', allows the site to automatically receive via Outlook a summary version of the new 'Daily Buffer Report' each morning. As a result of this new parameter, the other screens related to 'Ins. Verification' site parameters were adjusted as well.

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out Criteria (any of the following):

- The project is canceled
- The requested changes implemented by IB\*2.0\*771 are no longer desired by VA OIT and the eBusiness eInsurance sub-team
- The patch produces catastrophic problems

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the eInsurance software is tightly integrated with external systems, any attempt at a back-out should include close consultation with the external trading partners such as the Financial Services Center (FSC) and the Health Care Clearing House (HCCH) to determine risk.

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any back-out decision should be a joint decision of the Business Owner (or their representative) and the Program Manager with input from the Health Services Portfolio (HSP) Application Coordinator, developers (both project and Tier 3 HSP), and if appropriate, external trading partners such as the VA Financial Service Center (FSC) or Health Care Clearing House.

eInsurance is tightly integrated with these external partners and a back-out of the patch should not be a standalone decision.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out plan for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch.

Back-out Procedure prior to National Release. If it is prior to national release, the site will be already working directly with the development team daily and should contact that team. The development team members will have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that the development team can quickly address via a new software version. If the site is unsure who to contact, they may log a ticket to contact Health Services Portfolio.

The IB\*2.0\*771 patch contains the following build component.

- Data Dictionary
- Options
- Routines
- Input Template

While the VistA installation procedure of the KIDS build allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action, due to the complexity of this patch, it is not recommended for back-out, and a restore from a backup of the Transport Global should not be attempted. In the event that a site decides to back out this patch, the site should contact the Enterprise Service Desk (ESD) to submit a help desk ticket. The development team will need to issue a follow-on patch in order to comprehensively back-out this patch, to clean up corrupted data / remove data dictionary changes, if needed, or both and restore the system to a functioning state.

Please contact the EPMD team for assistance since this installed patch contains components in addition to routines.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful back-out is confirmed by verification that the back-out patch was successfully implemented. This includes successful installation and testing that the back-out acted as expected, as defined together with the team the site contacted in section 5.5.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. The only data changes in this patch are specific to the operational software and platform settings and they are covered in the Back-out procedures detailed elsewhere in this document.

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

[^1]: “Enterprise service lines, VAD” for short. Formerly known as the Information Resources Management (IRM) or IT support.