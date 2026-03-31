---
title: PRCA*4.5*432 Deployment,Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5*432
group_key: "PRCA:PRCA:4.5"
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
  - report
  - installation
  - rollback
  - rcdpe
  - prca
  - site
page_count: 0
word_count: 2941
section_count: 31
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p432_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/prca_4_5_p432_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Medical Care Collection Fund (MCCF)  
  Electronic Data Interchange (EDI)  
  Transaction Applications Suite (TAS)  
  ePayments Release 21

  Accounts Receivable PRCA\*4.5\*432

  Deployment, Installation, Back-out, and Rollback Guide
---

![](prca-4-5-432-deployment-installation-back-out-and-rollback-guide/001.png)

October 2024

Office of Information and Technology (OIT)

Revision History

| Date         | Version | Description     | Author       |
|--------------|---------|-----------------|--------------|
| October 2024 | 1.0     | Initial Version | MCCF EDI TAS |

<span id="_Ref173762376" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

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
This document describes how to deploy and install the PRCA\*4.5\*432 patch, and how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom PRCA\*4.5\*432 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PRCA\*4.5\*380, PRCA\*4.5\*409, and PRCA\*4.5\*424 must be installed BEFORE PRCA\*4.5\*432.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                                                                                                                  | Phase / Role    | Tasks                                                                                                               | Project Phase (See Schedule)                 |
|-----|---------------------------------------------------------------------------------------------------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------------------|
| 1   | VA OIT, VHA Finance Financial Management VistA Support, and PMO (Leidos)                                                              | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                 | Planning                                     |
| 2   | Local VAMC and CPAC processes                                                                                                         | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                          | Planning                                     |
| 3   | Field Testing (Initial Operating Capability - IOC), VHA Finance Financial Management VistA Support Testing, and VistA Office Approval | Deployment      | Test for operational readiness                                                                                      | Testing                                      |
| 4   | VHA Finance Financial Management VistA Support and Field Operations                                                                   | Deployment      | Execute deployment                                                                                                  | Deployment                                   |
| 5   | Individual Veterans Administration Medical Centers (VAMCs)                                                                            | Installation    | Plan and schedule installation                                                                                      | Deployment                                   |
| 6   | VistA Office                                                                                                                          | Installation    | Ensure proper change management approval obtained in support of national release                                    | Deployment                                   |
| 7   |                                                                                                                                       | Installation    | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         | N/A; only existing VistA system will be used |
| 8   | VA’s eBusiness team                                                                                                                   | Installations   | Coordinate training                                                                                                 | Deployment                                   |
| 9   | VHAF Financial Management VistA Support Verifier and the development team                                                             | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                                   |
| 10  | VA OIT, VHA Finance Financial Management VistA Support, and MCCF EDI TAS Development Team (SAIC)                                      | Post Deployment | Hardware, Software and System Support                                                                               | Warranty                                     |

<span id="_Toc173763704" class="anchor"></span>Table 2: Site Preparation

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national rollout.

This section provides the schedule and milestones for the deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for 30 days starting with national release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the deployment of patch PRCA\*4.5\*432.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PRCA\*4.5\*432 is to be nationally released to all VAMCs.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IOC sites are:

- Upstate New York HCS (Buffalo, NY) - Station 528
- Cleveland VAMC (Cleveland, OH) - Station 541
- Central Arkansas HCS (Little Rock, AR) - Station 598
- New York HCS (New York, NY) - Station 630

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

| Site / Other | Problem / Change Needed | Features to Adapt / Modify to New Product | Actions / Steps | Owner |
|--------------|-------------------------|-------------------------------------------|-----------------|-------|
| N/A          | N/A                     | N/A                                       | N/A             | N/A   |

<span id="_Toc173763705" class="anchor"></span>Table 3: Facility-Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site | Space / Room | Features Needed | Other |
|------|--------------|-----------------|-------|
| N/A  | N/A          | N/A             | N/A   |

<span id="_Toc173763706" class="anchor"></span>Table 4: Hardware Specifications

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware     | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-------|---------|---------------|--------------|-------|
| Existing VistA system | N/A   | N/A     | N/A           | N/A          | N/A   |

<span id="_Toc173763707" class="anchor"></span>Table 5: Software Specifications

Please see the Roles and Responsibilities Table 1 in Section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software                                      | Make | Version | Configuration | Manufacturer | Other |
|--------------------------------------------------------|------|---------|---------------|--------------|-------|
| Fully patched Accounts Receivable package within VistA | N/A  | 4.5     | N/A           | N/A          | N/A   |
| Fully patched Integrated Billing package within VistA  | N/A  | 2.0     | N/A           | N/A          | N/A   |

<span id="_Toc173763708" class="anchor"></span>Table 6: Deployment / Installation / Back-out Checklist

Please see the Roles and Responsibilities Table 1 in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites that are participating in field testing (IOC) will use the “Patch Tracking” message in Outlook to communicate with the ePayments eBusiness team, the developers, and product support personnel.

#### Deployment / Installation / Back-out Checklist

The Release Management team will deploy the path PRCA\*4.5\*432, which is tracked nationally for all VAMCs in the National Patch Module (NPM) in Forum. Forum automatically tracks the patches as they are installed in the different VAMC Production systems. One can run a report in Forum to identify when and by whom the patch was installed into the VistA Production at each site. A report can also be run to identify which sites have not currently installed the patch into their VistA Production system. Therefore, this information does not need to be manually tracked in the chart below.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | N/A | N/A  | N/A                           |
| Install  | N/A | N/A  | N/A                           |
| Back-out | N/A | N/A  | N/A                           |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PRCA\*4.5\*432 is installable on a fully patched M(UMPS) VistA system and operates on the top of the VistA environment provided by the VistA infrastructure packages. The latter provides utilities that communicate with the underlying operating system and hardware, thereby providing each VistA package independence from variations in hardware and operating system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the PRCA\*4.5\*432 documentation on the NPM in Forum for the detailed installation instructions. These instructions include any pre-installation steps if applicable.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the PRCA\*4.5\*432 documentation on the NPM to find the location of related documentation that can be downloaded. PRCA\*4.5\*432 will be transmitted via a PackMan message and can be pulled from the NPM*.* It is not a host file, and therefore does not need to be downloaded separately.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PRCA\*4.5\*432 modifies the VistA database. All changes can be found on the NPM documentation for this patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are needed for patch PRCA\*4.5\*432 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for patch PRCA\*4.5\*432 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following staff will need access to the PackMan message containing the PRCA\*4.5\*432 patch or to Forum’s NPM for downloading the nationally released PRCA\*4.5\*432 patch. The software is to be installed by the site’s or region’s designated: VA OIT IT Operations Service, Enterprise Service Lines, VistA Applications Division[^1].

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to PRCA\*4.5\*432 on the NPM for the detailed installation instructions.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the PRCA\*4.5\*432 documentation on the NPM for detailed installation instructions. These instructions include any post installation steps if applicable.

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

It is necessary to determine if a wholesale back-out of the patch PRCA\*4.5\*432 is needed or if a better course of action is to correct through a new version of the patch (if prior to national release) or through a subsequent patch aimed at specific areas modified or affected by the original patch (after national release). A wholesale back-out of the patch will still require a new version (if prior to national release) or a subsequent patch (after national release). If the back-out is post-release of this patch PRCA\*4.5\*432, this patch should be assigned status of “Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. The back-out process will be executed at normal rather than raised job priority and is expected to have no significant effect on total system performance. After the reversion, the performance demands on the system will be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Update the following with a CHAMPVA filter selection. If payer type selection was previously displayed in a heading, include CHAMPVA in that heading.
    - 835 CARC Data Report \[RCDPE CARC CODE PAYER REPORT\]
    - Active Bills With EEOB Report \[RCDPE ACTIVE WITH EEOB REPORT\]
    - Auto-Decrease Adjustment Report \[RCDPE AUTO-DECREASE REPORT\]
    - Auto-Post Awaiting Resolution \[RCDPE APAR\]
    - Auto-Post Report \[RCDPE AUTO-POST REPORT\]
    - Auto-Posted Receipt Report \[RCDPE AUTO-POSTED REPORT \[RCDPE AUTO-POST RECEIPT REPORT\]
    - Duplicate EFT Deposits Audit Report \[RCDPE EFT AUDIT REPORT\]
    - EDI Lockbox 3rd Party Exceptions \[RCDPE EXCEPTION PROCESSING\]
    - EEOB Move/Copy/Remove Audit Report \[RCDPE EEOB MOVE/COPY/RMOVE RPT\]
    - EEOBs Marked for Auto-Post Audit Report \[RCDPE MARKED AUTO-POST REPORT\]
    - EFT Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\]
    - EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]
    - EFT/ERA TRENDING Report \[RCDPE EFT-ERA TRENDING REPORT\]
    - ERA Status Change Audit Report \[RCDPE ERA STATUS CHNG AUD REP\]
    - ERA Unmatched Aging Report \[RCDPE ERA AGING REPORT\]
    - ERA Worklist \[RCDPE EDI LOCKBOX WORKLIST\]
    - ERAs Posted with Paper EOB Audit Report \[RCDPE ERA W/PAPER EOB REPORT\]
    - Identify Payers \[RCDPE PAYER IDENTIFY\]
    - Payer Implementation Report \[RCDPE PAYER EXCLUSION NAME TIN\]
    - Provider Level Adjustments (PLB) Report \[RCDPE PROVIDER LVL ADJ REPORT\]
    - Remove ERA from Active Worklist Audit Report \[RCDPE REMOVED ERA AUDIT\]
    - Unapplied EFT Deposits Report \[RCDPE UNAPPLIED EFT DEP REPORT\]
1.  Modify Identify Payers \[RCDPE PAYER IDENTIFY\] to allow CHAMPVA identification.
1.  Allow the user to select CHAMPVA as a filter.
2.  Display a new column for the CHAMPVA flag.
3.  Action to Edit Flags will allow the user to the CHAMPVA flag.
4.  A new action called Flag CHAMPVA will CHAMPVA flag edits.
5.  Action Filter incudes CHAMPVA as a filter choice.
6.  Help text includes reference to CHAMPVA.
2.  Add a negative sign on the following reports to indicate an EFT debit amount.
    - Duplicate EFT Deposits Audit Report \[RCDPE EFT AUDIT REPORT\]
    - EFT Unmatched Aging Report \[RCDPE EFT AGING REPORT\]
3.  Remove the word “Debit” from EFT Daily Activity Report \[RCDPE EDI LOCKBOX ACT REPORT\] and display a negative sign in front of the EFT debit amount.
4.  Increase the maximum character display in option Receipt Processing \[RCDP RECEIPT PROCESSING\]. Display a maximum of 11 characters, without commas, for the processed amount and payment amount. Previously the maximum was 8 and 7 respectively.
5.  Auto-posting was modified to exclude CHAMPVA zero-payment ERAs.

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It may be decided to back out this patch if the project is canceled, the requested changes implemented by patch PRCA\*4.5\*432 are no longer desired by VA OIT and the ePayments eBusiness team, or the patch produces catastrophic problems.

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the ePayments software is tightly integrated with external systems, any attempt at a back-out should include close consultation with the external trading partners such as the Financial Services Center (FSC) and the Health Care Clearing House (HCCH) to determine risk.

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any back-out decision should be a joint decision of the Business Owner (or their representative) and the Program Manager with input from the Health Services Portfolio (HSP) Application Coordinator, developers (both project and Tier 3 HSP), and if appropriate, external trading partners such as the VA FSC or Change Healthcare.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out plan for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. The development team recommends that sites log a ticket if it is a nationally released patch.

If it is prior to national release, the site will be already working directly with the development team daily and should contact that team. The development team members will have been identified in the Initial Operating Capability (IOC) Memorandum of Understanding (MOU). As discussed in section 5.2, it is likely that development team can quickly address via a new software version. If the site is unsure whom to contact, they may log a ticket or contact Health Services Portfolio.

Patch PRCA\*4.5\*432 contains the following build components:

- Routines
- Data Dictionaries
- List Manager Templates

While the VistA KIDS installation procedure allows the installer to back up the modified routines using the ‘Backup a Transport Global’ action, the back-out procedure for global, data dictionary, and other VistA components is more complex and requires issuance of a follow-up patch to ensure all components are properly removed, restored, or both. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with the restoration of the data.

Please contact the EPMO team for assistance since this installed patch contains components in addition to routines.

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

[^1]: “Enterprise service lines, VAD” for short. Formerly known as the Information Resources Management (IRM) or IT support.