---
title: BPS*1*36 ECME Deployment, Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: ECME
app_name: Electronic Claims Management Engine
section: FIN
app_status: active
pkg_ns: BPS
patch_ver: 1
patch_id: BPS*1*36
group_key: ECME:BPS:1
file_numbers:
- '900231'
security_keys:
- BPS REPORTS
menu_options: 0
description: '| Date | Version | Description | Author | |----------|---------|-----------------|------------------------------------| | May 2024 | 1.0 | Initial Version | EDI TAS ePharmacy Development Team'
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 3922
section_count: 31
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: May 2024
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_p36_dibrg.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/E_Claims_Man_Eng_(ECME)/bps_1_p36_dibrg.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=141
audit_applied: '2026-05-31'
master_source: BPS*1*36 ECME Deployment, Installation, Back-out, and Rollback Guide
master_pub_date: May 2024
consolidated_from: 10 versions
prior_versions:
- BPS*1*32 ECME Deployment, Installation, Back-out, and Rollback Guide
- BPS*1*33 ECME Deployment, Installation, Back-out, and Rollback Guide
- BPS*1*34 ECME Deployment, Installation, Back-out, and Rollback Guide
- BPS*1*35 ECME Deployment, Installation, Back-out, and Rollback Guide
- BPS*1*37 ECME Deployment, Installation, Back-out, and Rollback Guide
- BPS*1*38 ECME Deployment, Installation, Back-out, and Rollback Guide
- BPS*1*39 ECME Deployment, Installation, Back-out, and Rollback Guide
- BPS*1*40 ECME Deployment, Installation, Back-out, and Rollback Guide
- BPS*1*41 ECME Deployment, Installation, Back-out, and Rollback Guide
consolidated_title: ecme deployment, installation, back-out, and rollback guide
---

![](bps-1-36-ecme-deployment-installation-back-out-and-rollback-guide/001.png)

May 2024

Office of Information and Technology (OIT)

Revision History

| Date     | Version | Description     | Author                             |
|----------|---------|-----------------|------------------------------------|
| May 2024 | 1.0     | Initial Version | EDI TAS ePharmacy Development Team |

<span id="_Toc159577084" class="anchor"></span>Table : Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

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
    - [Mirror Testing or Site Production Testing](#mirror-testing-or-site-production-testing)
    - [After National Release but During the Designated Support Period](#after-national-release-but-during-the-designated-support-period)
    - [After National Release and Warranty Period](#after-national-release-and-warranty-period)
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
This document describes how to deploy and install the multi-build BPS PSO BUNDLE 24.0 (includes BPS\*1.0\*36 and PSO\*7.0\*703) and how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the multi-build BPS PSO BUNDLE 24.0 (includes BPS\*1.0\*36 and PSO\*7.0\*703) will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BPS\*1\*29 must be installed BEFORE BPS\*1\*36.

PSO\*7\*441, PSO\*7\*648, and PSO\*7\*681 must be installed BEFORE PSO\*7\*703.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                                                                                                   | Phase / Role    | Tasks                                                                                                               | Project Phase (See Schedule)                 |
|-----|------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| 1   | VA OIT, VA OIT Health Product Support, and PMO (Leidos)                                                                | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                 | Planning                                     |
| 2   | Local VAMC and CPAC processes                                                                                          | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                          | Planning                                     |
| 3   | Field Testing (Initial Operating Capability – \[IOC\]), Health Product Support Testing, and VIP Release Agent Approval | Deployment      | Test for operational readiness                                                                                      | Testing                                      |
| 4   | Health Product Support and Field Operations                                                                            | Deployment      | Execute deployment                                                                                                  | Deployment                                   |
| 5   | Individual Veterans Administration Medical Centers (VAMCs)                                                             | Installation    | Plan and schedule installation                                                                                      | Deployment                                   |
| 6   | VIP Release Agent                                                                                                      | Installation    | Ensure authority to operate and that certificate authority security documentation is in place                       | Deployment                                   |
| 7   | N/A                                                                                                                    | Installation    | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         | N/A; only existing VistA system will be used |
| 8   | VA's eBusiness team                                                                                                    | Installations   | Coordinate training                                                                                                 | Deployment                                   |
| 9   | VIP Release Agent, Health Product Support, and the development team                                                    | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                                   |
| 10  | VA OIT, VA OIT Health Product Support, and MCCF EDI TAS Development Team (SAIC)                                        | Post Deployment | Hardware, Software and System Support                                                                               | Warranty                                     |

<span id="_Toc159577085" class="anchor"></span>Table : Site Preparation

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national rollout.

This section provides the schedule and milestones for the deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for 30 days starting with the day after national release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the deployment of the multi-build BPS PSO BUNDLE 24.0 (includes BPS\*1.0\*36 and PSO\*7.0\*703).

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This multi-build BPS PSO BUNDLE 24.0 (includes BPS\*1.0\*36 and PSO\*7.0\*703) is to be nationally released to all VAMCs.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IOC sites are:

- Audie L. Murphy Memorial Hosp (671 – San Antonio, TX)
- Birmingham VAMC (521 – Birmingham, AL)
- Kansas City VAMC (589 – Kansas City, MO)
- Richmond VA Medical Center (652 – Richmond, VA)

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

| Site / Other | Problem / Change Needed | Features to Adapt / Modify to New Product | Actions / Steps | Owner |
|--------------|-------------------------|-------------------------------------------|-----------------|-------|
| N/A          | N/A                     | N/A                                       | N/A             | N/A   |

<span id="_Toc159577086" class="anchor"></span>Table : Facility-Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site | Space / Room | Features Needed | Other |
|------|--------------|-----------------|-------|
| N/A  | N/A          | N/A             | N/A   |

<span id="_Toc159577087" class="anchor"></span>Table : Hardware Specifications

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware     | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-------|---------|---------------|--------------|-------|
| Existing VistA system | N/A   | N/A     | N/A           | N/A          | N/A   |

<span id="_Toc159577088" class="anchor"></span>Table : Software Specifications

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software                                                      | Make | Version | Configuration | Manufacturer | Other |
|------------------------------------------------------------------------|------|---------|---------------|--------------|-------|
| Fully patched Electronic Claims Management Engine package within VistA | N/A  | 1.0     | N/A           | N/A          | N/A   |
| Fully patched Outpatient Pharmacy package within VistA                 | N/A  | 7.0     | N/A           | N/A          | N/A   |

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites that are participating in field testing (IOC) will use the "Patch Tracking" message in Outlook to communicate with the ePharmacy eBusiness team, developers, and product support personnel.

#### Deployment / Installation / Back-out Checklist

The Release Management team will deploy the multi-build BPS PSO BUNDLE 24.0, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in Forum. Forum automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in Forum to identify when and by whom the patch was installed into the VistA production at each site. A report can also be run to identify which sites have not currently installed the patch into their VistA production system. Therefore, this information does not need to be manually tracked in the chart below.

Table 6: Deployment / Installation / Back-out Checklist

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | N/A | N/A  | N/A                           |
| Install  | N/A | N/A  | N/A                           |
| Back-out | N/A | N/A  | N/A                           |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-build BPS PSO BUNDLE 24.0 is installable on a fully patched M(UMPS) VistA system and operates on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities that communicate with the underlying operating system and hardware, thereby providing each VistA package independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the BPS\*1.0\*36 documentation on the NPM in Forum for the detailed installation instructions. These instructions include any pre-installation steps if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the BPS\*1.0\*36 and PSO\*7.0\*703 documentation on the NPM to find related documentation that can be downloaded. The patch description of each patch will be transmitted as a MailMan message from the NPM. These messages can also be pulled from the NPM. The patches themselves are bundled together into the multi-build BPS PSO BUNDLE 24.0. The host file containing these patches must be downloaded separately. The file name is BPS_1_36_PSO.KID and it can be found on the [VistA software download site](https://download.vista.med.va.gov/index.html/SOFTWARE/).

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-build BPS PSO BUNDLE 24.0 modifies the VistA database. All changes can be found on the NPM documentation for this patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are needed for multi-build BPS PSO BUNDLE 24.0 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for multi-build BPS PSO BUNDLE 24.0 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff performing the installation of this multi-build will need access to FORUM's NPM to view all patch descriptions. Staff will also need access and ability to download the host file from the VistA software download site. The software is to be installed by each site's or region's designated VA OIT IT Operations Service, Enterprise Service Lines, VistA Applications Division[^1].

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detailed instructions for installing the multi-build BPS PSO BUNDLE 24.0 (includes BPS\*1.0\*36 and PSO\*7.0\*703) can be found on the patch description for BPS\*1.0\*36, which can be found on the NPM. Installing the multi-build BPS PSO BUNDLE 24.0 will install all component patches (BPS\*1.0\*36 and PSO\*7.0\*703).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the BPS\*1.0\*36 documentation on the NPM for detailed installation instructions. These instructions include any post installation steps if applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required for this patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocations, or other resources is necessary.

# Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A decision to back out could be made during Site Mirror Testing, during Site Production Testing, or after National Release to the field (VAMCs). The best strategy decision is dependent on the stage during which the decision is made.

### Mirror Testing or Site Production Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a decision to back out is made during Mirror Testing or Site Production Testing, a new version of the patch can be used to restore the build components to their pre-patch condition.

### After National Release but During the Designated Support Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a decision to back out is made after national release and within the designated support period, a new patch will be entered into the NPM in Forum and will go through all the necessary milestone reviews, etc. as a patch for a patch. This patch could be defined as an emergency patch, and it could be used to address specific issues pertaining to the original patch or it could be used to restore the build components to their original pre-patch condition.

### After National Release and Warranty Period

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the 90-day warranty period, the VistA Maintenance Program will produce the new patch, either to correct the defective components or restore the build components to their original pre-patch condition.

## Back-out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes implemented with multi-build BPS PSO BUNDLE 24.0 can be backed out in their entirety or on an enhancement-by-enhancement basis. Either could be accomplished via a new version of multi-build BPS PSO BUNDLE 24.0 if before national release or a new multi-build if after national release.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. The back-out process will be executed at normal rather than raised job priority and is expected to have no significant effect on total system performance. After the reversion, the performance demands on the system will be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below are the acceptance criteria for each story included in BPS PSO BUNDLE 24.0.

EPHAR-78

- Reason for Service Codes have been updated / added / Inactivated in file 9002313.23, BPS NCPDP REASON FOR SERVICE CODE to reflect changes.
- Professional Service Codes have been updated / added / Inactivated in 9002313.21, BPS NCPDP PROFESSIONAL SERVICE CODE to reflect changes.
- Result of Service Code has been added in file 9002313.22, BPS NCPDP RESULT OF SERVICE CODE to reflect changes.
- Reject Code has been added in file BPS NCPDP REJECT CODES to reflect changes.
- Updated / New Reason For Service Code, Professional Service Code, and Result of Service Code can be:
- selected when performing the OVR action from the Pharmacist Worklist.
- Selected when performing the SMA action from the Pharmacist Worklist.
- The system does not accept Inactive codes.
- When patient type is Veteran new Reject Code can be:
- received in a claim response and stored in VistA with the claim response.
- displayed on the ECME User screen.
- displayed on the Rejected Claims Report and Closed Claims Report.
- displayed on the LOG Print Claim Log (ECME User Screen and VER).
- When patient type is Veteran new Reject Code can be:
- transferred automatically or manually by the OPECC.
- displayed in Reject Resolution Required Codes (RRR).
- When patient type is TRICARE or CHAMPVA new Reject Code can be:
- received in a claim response and stored in VistA with the claim response.
- displayed on the ECME User screen.
- displayed on the Pharmacists' Worklist.
- displayed on the Pharmacists' View/Process (VP).
- displayed on the Reject Notification Screen.
- displayed on the Reject Information Screen.
- displayed on the Rejected Claims Report and Closed Claims Report.
- displayed on the LOG Print Claim Log (ECME User Screen and VER).

EPHAR-2693

- An entry is added to the Activity Log when a prescription fails the 3/4 days supply hold logic after the user has changed the Bypass field from "YES" to "NO" from the Medication Screen.
- When the ED action is used to change the Fill Date and the Bypass field is set to "YES" the system will update the Fill Date and not impact Suspense Hold Date. (Regression)
- When the ED action is used to change the Fill Date and the Bypass field is not set the system will update the Fill Date, add an entry to the Activity Log and transmit to CMOP on the original Suspense Hold Date.

EPHAR-2942

- ePharmacy Rx – Obtain Signature does not display when a partial prescription is released using the PSO RELEASE option if the previous original fill was an ePharmacy prescription.
- ePharmacy Rx – Obtain Signature does not display when a partial prescription is released using the PSO RELEASE option if the previous refill was an ePharmacy prescription.
- ePharmacy Rx – Obtain Signature continues to display when an ePharmacy original fill (full day supply) is released using the PSO RELEASE option. (Regression)
- ePharmacy Rx – Obtain Signature continues to display when an ePharmacy refill (full day supply) is released using the PSO RELEASE option. (Regression)
- ePharmacy Rx – Obtain Signature does not display when a partial prescription is released using the PSO RELEASE option if the prescription is currently in a rejected status on the Third Party Payer Rejects - Worklist.

EPHAR-3032

- When a claim is reversed and resubmitted using a new NDC and the release date is on or after the prescription expiration date, the system uses the initial claim date of service. This should occur with original fills and refills
- When a claim is reversed and resubmitted using a new NDC and the release date is prior to the prescription expiration date, the system uses the release date for the date of service. This should occur with original fills and refills. Regression testing
- When the events occur in the order below for Veteran:
- Rx is processed / filled – claim DOS is Day 1
- Rejects for Cardholder ID - goes to ECME User Screen
- Rx expires
- Rx is released
- OPECC Resolves insurance issue and resubmits - rejects for 88 DUR - Goes to Pharmacist WL
- Pharmacy resolves and resubmits claim - Claim DOS should be Day 1

The claim resubmits using the initial claim date of service. This should occur with original fills and refills.

- When the events occur in the order below:
- Rx is auto-reversed
- Rx is released
- Claim is resubmitted
- Rx expires

The claim resubmits using the release date for the date of service. This should occur with original fills and refills. Regression testing

- The system does not change the Fill Date and the Activity Log does not contain a comment indicating a change in fill date when a claim is reversed and resubmitted using a new NDC and a release date on or after the prescription expiration date. This should occur with original fills and refills.

The comment below should not appear:  
Comments: Change Fill Date MM/DD/YY to MM/DD/YY

- The Activity Log is updated with a comment indicating a change in fill date when a claim is reversed and resubmitted using a new NDC and a release date prior to the prescription expiration date. This should occur with original fills and refills. Regression testing
- The system does not change the Fill Date and the Activity Log does not contain a comment indicating a change in fill date when the Rx is released on a date on or after the prescription expiration date. This should occur with original fills and refills.
- When the events occur in the order below:
- Rx expires
- Rx is released
- Claim is resubmitted from ECME User Screen

The claim resubmits using the initial claim date of service. This should occur with original fills and refills.

- When the events occur in the order below:
- Rx is auto-reversed because not released within days in Auto-Reversal parameter
- Rx expires
- Rx is released
- Claim is resubmitted

The claim resubmits using the initial claim date of service. This should occur with original fills and refills.

EPHAR-3425

- New ePharmacy Bills Created with Errors report is available on the Claim Results and Status menu:
- Synonym ERR
- Report name "ePharmacy Bills Created with Errors"
- New ePharmacy Bills Created with Errors report is locked with the BPS REPORTS security key.
- Entering ?? at the Claims Results and Status menu will display the new report and the associated security key.
- Entering ??? at the Claims Results and Status menu will display the description of the new report.
- The new ePharmacy Bills Created with Errors report will ask users if they want to capture the report for an Excel document.
- If a user enters 'yes' to capture the report for Excel, additional text will display instructing the user to set up their terminal to capture the data and what to enter at the Device prompt to avoid undesired wrapping.
- The Excel report will contain all the fields displayed in the mockup above.
- Once the ePharmacy K bill with the error is resolved (e.g., Bill Status changes to New, Active, Cancelled, etc.), it no longer appears on the report. (The report will only include ePharmacy claims with a Bill Incomplete status. No other claims (e.g., medical) with a Bill Incomplete status will appear on the report.)
- The report will include ALL of the following even though there is no filter:
- All Divisions
- All fill locations (CMOP, Mail, and Window)
- All realtime, backbills, PRO Option, and Resubmitted claims
- All drug classes
- All eligibilities (Veteran, TRICARE, and CHAMPVA)
- All Patients
- All insurance companies
- The date range selection will allow any valid date.
- The "Claim Entered Date" in the date range selection uses the "Entered" date for the claim, which is available in TPJI.
- The START WITH CLAIM ENTERED DATE defaults to T-14.
- The GO TO CLAIM ENTERED DATE defaults to T.
- The printed report appears the same as the report mockup above.

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It may be decided to back out this patch if the project is canceled, the requested changes implemented by multi-build BPS PSO BUNDLE 24.0 are no longer desired by VA OIT and the ePharmacy eBusiness team, or the patch produces catastrophic problems.

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the ePharmacy software is tightly integrated with external systems, any attempt at a back-out should include close consultation with the external trading partners such as the Financial Services Center (FSC) and the Health Care Clearing House (HCCH) to determine risk.

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any back-out decision should be a joint decision of the Business Owner (or their representative) and the Program Manager with input from the Health Services Portfolio (HSP) Application Coordinator, developers (both project and Tier 3 HSP), and if appropriate, external trading partners such as the VA FSC or Change Healthcare.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out plan for VistA applications is complex and not a "one size fits all" solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch.

If it is prior to national release, the site will be already working directly with the development team daily and should contact that team. The development team members will have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that development team can quickly address via a new software version. If the site is unsure whom to contact, they may log a ticket or contact Health Services Portfolio.

Multi-build BPS PSO BUNDLE 24.0 contains the following build components:

- Routines
- Data Dictionaries
- Options
- Protocols

While the VistA KIDS installation procedure allows the installer to back up the modified routines using the 'Backup a Transport Global' action, the back-out procedure for global, data dictionary, and other VistA components is more complex and requires issuance of a follow-up patch to ensure all components are properly removed and / or restored. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with the restoration of the data.

Please contact the Software Product Management (SPM) team for assistance since this installed patch contains components in addition to routines.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful back-out is confirmed by verification that the back-out patch was successfully implemented. This includes successful installation and testing that the back-out acts as expected, as defined together with the team the site contacted in section 5.5.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. The data changes in this patch are specific to the operational software and platform settings. These data changes are covered in the Back-out procedures detailed elsewhere in this document.

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

[^1]: "Enterprise service lines, VAD" for short. Formerly known as the Information Resources Management (IRM) or IT support.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: BPS*1*41 ECME Deployment, Installation, Back-out, and Rollback Guide

## Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document describes how to deploy and install the multi-build and how to back-out the product and rollback to a previous version or data set.

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the multi-build BPS PSO IB BUNDLE 29.0 (includes BPS\*1.0\*41, PSO\*7.0\*767, and IB\*2.0\*812) will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

### Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None.

### Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

## Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                                                                                               | Phase / Role    | Tasks                                                                                                               | Project Phase (See Schedule)                 |
|-----|--------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| 1   | VA OIT, VA OIT Health Product Support, and PMO (Leidos)                                                            | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                 | Planning                                     |
| 2   | Local VAMC and CPAC processes                                                                                      | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                          | Planning                                     |
| 3   | Field Testing (Initial Operating Capability - IOC), Health Product Support Testing, and VIP Release Agent Approval | Deployment      | Test for operational readiness                                                                                      | Testing                                      |
| 4   | Health Product Support and Field Operations                                                                        | Deployment      | Execute deployment                                                                                                  | Deployment                                   |
| 5   | Individual Veterans Administration Medical Centers (VAMCs)                                                         | Installation    | Plan and schedule installation                                                                                      | Deployment                                   |
| 6   | VIP Release Agent                                                                                                  | Installation    | Ensure authority to operate and that certificate authority security documentation is in place                       | Deployment                                   |
| 7   | N/A                                                                                                                | Installation    | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         | N/A; only existing VistA system will be used |
| 8   | VA's eBusiness team                                                                                                | Installations   | Coordinate training                                                                                                 | Deployment                                   |
| 9   | VIP Release Agent, Health Product Support, and the development team                                                | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                                   |
| 10  | VA OIT, VA OIT Health Product Support, and VHA HF DSO MCCF Development Team (H2)                                   | Post Deployment | Hardware, Software and System Support                                                                               | Warranty                                     |

<span id="_Toc210994630" class="anchor"></span>Table 2: Site Preparation

## Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national rollout.

This section provides the schedule and milestones for the deployment.

### Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for 30 days starting with the day after national release.

### Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the deployment of the multi-build BPS PSO IB BUNDLE 29.0 (includes BPS\*1.0\*41, PSO\*7.0\*767, and IB\*2.0\*812).

#### Deployment Topology (Targeted Architecture)

This multi-build BPS PSO IB BUNDLE 29.0 (includes BPS\*1.0\*41, PSO\*7.0\*767, and IB\*2.0\*812) is to be nationally released to all VAMCs.

#### Site Information (Locations, Deployment Recipients) 

The IOC sites are:

- Kansas City VAMC (589 – Kansas City, MO)
- Richmond VA Medical Center (652 – Richmond, VA)
- Shreveport VAMC (667 – Shreveport, LA)

#### Site Preparation 

The following table describes preparation required by the site prior to deployment.

| Site / Other | Problem / Change Needed | Features to Adapt / Modify to New Product | Actions / Steps | Owner |
|--------------|-------------------------|-------------------------------------------|-----------------|-------|
| N/A          | N/A                     | N/A                                       | N/A             | N/A   |

<span id="_Toc210994631" class="anchor"></span>Table 3: Facility-Specific Features

### Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Facility Specifics

The following table lists facility-specific features required for deployment.

| Site | Space / Room | Features Needed | Other |
|------|--------------|-----------------|-------|
| N/A  | N/A          | N/A             | N/A   |

<span id="_Toc210994632" class="anchor"></span>Table 4: Hardware Specifications

#### Hardware 

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware     | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-------|---------|---------------|--------------|-------|
| Existing VistA system | N/A   | N/A     | N/A           | N/A          | N/A   |

<span id="_Toc210994633" class="anchor"></span>Table 5: Software Specifications

Please see [⁠Table 1⁠](#_Ref203482215) (Roles and Responsibilities) in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

#### Software 

The following table describes software specifications required at each site prior to deployment.

| Required Software                                                      | Make | Version | Configuration | Manufacturer | Other |
|------------------------------------------------------------------------|------|---------|---------------|--------------|-------|
| Fully patched Electronic Claims Management Engine package within VistA | N/A  | 1.0     | N/A           | N/A          | N/A   |
| Fully patched Outpatient Pharmacy package within VistA                 | N/A  | 7.0     | N/A           | N/A          | N/A   |
| Fully patched Integrated Billing package within VistA                  | N/A  | 2.0     | N/A           | N/A          | N/A   |

<span id="_Ref203482386" class="anchor"></span>Table 6: Deployment / Installation / Back-out Checklist

Please see [⁠Table 1⁠](#_Ref203482215) (Roles and Responsibilities) in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

#### Communications 

The sites that are participating in field testing (IOC) will use the "Patch Tracking" message in Outlook to communicate with the ePharmacy eBusiness team, developers, and product support personnel.

#### Deployment / Installation / Back-out Checklist

The Release Management team will deploy the multi-build BPS PSO IB BUNDLE 29.0, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in Forum. Forum automatically tracks the patches as they are installed in the different VAMC Production systems. One can run a report in Forum to identify when and by whom the patch was installed into the VistA Production at each site. A report can also be run to identify which sites have not currently installed the patch into their VistA Production system. Therefore, this information does not need to be manually tracked in [⁠Table 6⁠](#_Ref203482386).

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | N/A | N/A  | N/A                           |
| Install  | N/A | N/A  | N/A                           |
| Back-out | N/A | N/A  | N/A                           |

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-build BPS PSO IB BUNDLE 29.0 is installable on a fully patched M(UMPS) VistA system and operates on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities that communicate with the underlying operating system and hardware, thereby providing each VistA package independence from variations in hardware and operating system.

### Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the BPS\*1.0\*41 documentation on the NPM in Forum for the detailed installation instructions. These instructions include any pre-installation steps if applicable.

### Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the BPS\*1.0\*41, PSO\*7.0\*767, and IB\*2.0\*812 documentation on the NPM to find related documentation that can be downloaded. The patch description of each patch will be transmitted as a MailMan message from the NPM. These messages can also be pulled from the NPM. The patches themselves are bundled together into the multi-build BPS PSO IB BUNDLE 29.0. The host file containing these patches must be downloaded separately. The file name is BPS_1_41_PSO_IB.KID and it can be found on the [VistA software download site](https://download.vista.med.va.gov/index.html/SOFTWARE/).

### Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-build BPS PSO IB BUNDLE 29.0 modifies the VistA database. All changes can be found on the NPM documentation for this patch.

### Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are needed for multi-build BPS PSO IB BUNDLE 29.0 installation.

### Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for multi-build BPS PSO IB BUNDLE 29.0 installation.

### Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff performing the installation of this multi-build will need access to FORUM's NPM to view all patch descriptions. Staff will also need access and ability to download the host file from the VistA software download site. The software is to be installed by each site's or region's designated VA OIT IT Operations Service, Enterprise Service Lines, VistA Applications Division[^1].

### Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Detailed instructions for installing the multi-build BPS PSO IB BUNDLE 29.0 (includes BPS\*1.0\*41, PSO\*7.0\*767, and IB\*2.0\*812) can be found on the patch description for BPS\*1.0\*41, which can be found on the NPM. Installing the multi-build BPS PSO IB BUNDLE 29.0 will install all component patches (BPS\*1.0\*41, PSO\*7.0\*767, and IB\*2.0\*812).

### Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the BPS\*1.0\*41 documentation on the NPM for detailed installation instructions. These instructions include any post installation steps if applicable.

### System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required for this patch.

### Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocations, or other resources is necessary.
