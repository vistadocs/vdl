---
title: PSS*1*254 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: PSS
app_name: 'Pharmacy: Data Management'
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*254
group_key: PSS:PSS:1
file_numbers:
- '1'
- '2'
- '50'
- '51'
- '51.1'
- '51.2'
- '51.23'
- '51.24'
- '51.242'
- '51.25'
- '147'
- '1148'
- '1150'
- '1151'
- '1152'
- '1153'
security_keys:
- PSNMGR
- XUPROG
- XUPROGMODE
menu_options: 0
description: '| Date | Version | Description | Author | |------------|-------------|-----------------|----------------------| | May 2025 | 1.0 | Final Version | Liberty IT Solutions | | April 2025 | 0.1 | Initial Version | Liberty IT Solutions'
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 8208
section_count: 31
table_count: 9
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: May 2025
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/PSS_1_0_P254_DIBR.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/PSS_1_0_P254_DIBR.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=93
audit_applied: '2026-05-31'
master_source: PSS*1*254 Deployment, Installation, Back-Out, and Rollback Guide
master_pub_date: May 2025
consolidated_from: 5 versions
prior_versions:
- PSS*1*211 Deployment, Installation, Back-Out, and Rollback Guide
- PSS*1*234 Deployment, Installation, Back-Out, and Rollback Guide
- PSS*1*239 Deployment, Installation, Back-Out, and Rollback Guide
- PSS*1*262 Deployment, Installation, Back-Out, and Rollback Guide
consolidated_title: deployment, installation, back-out, and rollback guide
---

PSS\*1\*254

Deployment, Installation, Back-Out, and Rollback Guide

![](pss-1-254-deployment-installation-back-out-and-rollback-guide/001.png)

May 2025Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description | Author           |
|------------|-------------|-----------------|----------------------|
| May 2025   | 1.0         | Final Version   | Liberty IT Solutions |
| April 2025 | 0.1         | Initial Version | Liberty IT Solutions |

Table 2: Timeline

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
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the First Databank (FDB) Framework (Fwk) v4.5 Upgrade patch PSS\*1\*254, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the PSS\*1\*254 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VistA patches must be installed before PSS\*1\*254:

- PSS\*1\*163
- PSS\*1\*210
- PSS\*1\*231

The following VistA patches must be installed with PSS\*1\*254:

- PSJ\*5\*423
- PSO\*7\*779

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                                                                                                                                                                         | Phase / Role   | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | Department of Veterans Affairs (VA) Office of Information and Technology (OIT), Health Services Portfolio (HSP) Patient Care Services (PCS), and Program Management Office (PMO) | Deployment         | Plan and schedule deployment                                                                                        | Planning                         |
| 2      | Health Product Support and Field Operations (FO)                                                                                                                                 | Deployment         | Determine and document the roles and responsibilities of those involved in the deployment                           | Planning                         |
| 3      | Field Testing (Initial Operating Capability-IOC), Health Product Support Testing & Veteran-Focused Integration Process (VIP) Release Agent Approval                              | Deployment         | Test for operational readiness                                                                                      | Testing                          |
| 4      | Application Coordinators                                                                                                                                                         | Release Deployment | Application Coordinators release patches                                                                            | Deployment                       |
| 5      | Health Services Portfolio (HSP) Patient Care Services (PCS) and Field Operations (FO)                                                                                            | Deployment         | Execute deployment                                                                                                  | Deployment                       |
| 6      | OIT, Development, Security, and Operations (DevSecOps) Infrastructure Operations (IO) and Individual Veterans Administration Medical Centers (VAMCs)                             | Installation       | Plan and schedule installation                                                                                      | Deployment                       |
| 7      | Facility Area Manager and OIT support, which may be local or regional                                                                                                            | Back-out           | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                       |
| 8      | VA OIT, Health Services Portfolio (HSP) Patient Care Services (PCS), and the Development Team                                                                                    | Post Deployment    | Hardware, Software and System Support                                                                               | Warranty                         |

Table 3: Site Preparation

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a national general availability release. The scheduling of test/mirror installs, testing, and the deployment to production will be at the sites' discretion.

A national release is planned after testing has been successfully completed at initial operating capability (IOC) test sites.

Deployment will be performed by the local or regional OIT staff. Other teams may provide additional support.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation is scheduled to run for 7 days, as depicted in the master deployment schedule for First Databank Framework v4.5 Upgrade.

| Task              | Start     | Finish    |
|-------------------|-----------|-----------|
| National Release  | 5/15/2025 | 5/15/2025 |
| Compliance Period | 5/15/2025 | 5/23/2025 |

Table 4: Facility-Specific Features

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the deployment of the First Databank Framework v4.5 Upgrade patch PSS\*1\*254.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release will be deployed to all VistA instances.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IOC test sites are:

- Eastern Colorado HCS, Denver, CO
- James A Haley VA Hospital, Tampa, FL
- Northampton VAMC, Northampton, MA
- Overton Brooks VAMC, Shreveport, LA
- VA Greater LA HCS, Los Angeles, CA

Upon national release all VAMCs are expected to install this patch prior to or on the compliance date. The software will be distributed through FORUM.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The First Databank Framework v4.5 Upgrade release does not require any special preparation by the site prior to deployment.

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
| N/A            | N/A                       | N/A                                         | N/A               | N/A       |

Table 5: Hardware Specifications

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The First Databank Framework v4.5 Upgrade release does not require any special or specific resources other than a functional VistA system.

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      | N/A            | N/A                 | N/A       |

Table 6: Software Specifications

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The First Databank Framework v4.5 Upgrade release does not require any special or specific resources other than a functional VistA system.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   | N/A       | N/A         | N/A               | N/A              | N/A       |

Table 7: Deployment/Installation/Back-Out Checklist

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The First Databank Framework v4.5 Upgrade release does not require any special or specific resources other than a functional VistA system.

| Required Software | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   | N/A       | N/A         | N/A               | N/A              | N/A       |

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For national release, sites will receive communication that the release has occurred, which will normally be an Action Item or Bulletin.

Sites will use their internal communications to let their users know about upcoming installations and any associated downtime. This is critical as users can often slow the installation process if they are on the system while installers are trying to get the software installed.

Clinical Application Coordinators (CACs), installers, and other site personnel (as determined by the site) will need to coordinate installation dates and times. In addition, other support personnel may need to be consulted – such as the Citrix support, Client Technologies (if required).

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy patch PSS\*1\*254, which is tracked in the National Patch Module (NPM) in FORUM, nationally to all VAMCs. FORUM automatically tracks the patches as they are installed in the different VAMC production systems as described in the previous section. One can run a report in FORUM to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not installed the patch in their VistA production system as of that moment in time.

This information does not need to be manually tracked. The table is included below if manual tracking is desired.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | TBD | TBD  | TBD                           |
| Install  | TBD | TBD  | TBD                           |
| Back-Out | TBD | TBD  | TBD                           |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA patch. The only pre-installation and system requirements for deployment and installation of this patch are the prerequisite patches which need to be installed before this patch can be installed*.*

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a list of the applications involved in this project along with their patch numbers. The patches should be installed together. The order of install does not matter.

APPLICATION/VERSION PATCH

PHARMACY DATA MANAGEMENT v1.0 PSS\*1\*254

INPATIENT MEDICATIONS v5.0 PSJ\*5\*423

OUTPATIENT MEDICATIONS v7.0 PSO\*7\*779

The VistA patches in this release should be installed into the test/mirror/pre-prod accounts before the production account as is the normal VistA patch installation standard convention. When installing any VistA patch, sites should utilize the option "Backup a Transport Global" in order to create a backup message of the "Build (including routines)" exported with this patch. Pre and Post-installation checksums are found in the Patch Description and in FORUM NPM.

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

To install this VistA patch, the patch installer must be an active user on the VistA system and have access to the VistA menu option "Kernel Installation & Distribution System" \[XPD MAIN\] and have VistA security keys XUPROG and XUPROGMODE. Knowledge on how to install VistA patches using the items on this menu option is also a required skill.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Sites may encounter an XINDEX Error during the installation of this patch. Routine PSSFDBDI uses a Web Services Client. It calls a Cache Class to parse the eXtensible Markup Language (XML) document returned by the web service call. This has an exception and can be

disregarded.

Installation Instructions:

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch name, PSS\*1.0\*254.
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup: the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
        1.  At the Installation option menu, select Backup a Transport Global.
        2.  At the Select INSTALL NAME prompt, enter your build PSS\*1.0\*254.
        3.  When prompted for the following, enter "R" for Routines or "B" for Build.

Select one of the following:

B Build

R Routines

Enter response: Build

4.  When prompted "Do you wish to secure this message? NO//", press \<enter\> and take the default response of "NO".
5.  When prompted with, "Send mail to: Last name, First Name", press \<enter\> to take default recipient. Add any additional recipients.
6.  When prompted with "Select basket to send to: IN//", press \<Enter\> and take the default IN mailbox or select a different mailbox.
3.  You may also elect to use the following options:
    1.  Print Transport Global - This option will allow you to view the components of the Kernel Installation and Distribution System (KIDS) build.
    2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, data dictionaries (DDs), templates, etc.
4.  Select the Install Package(s) option and choose the patch to install.
    1.  If prompted "Enter site type into which this patch is being installed:", respond with the account type you are installing the patch in (1/2/3/4/5) (1-Pre-Prod, 2-SQA, 3-Staging, 4-Development, 5-PRODUCTION)

> For installs to Production, choose 5-PRODUCTION

> For installs to Test, choose 1-Pre-Prod

2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer 'NO'
3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer 'NO'.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful installation can be verified by reviewing the first two lines of the routines contained in the patch. The second line will contain the patch number "254" in the \[PATCH LIST\] section.

The option Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] can be run to compare the routine checksums to what is documented in the patch.

MailMan Messages:

The installation sends several MailMan messages to the installer and users with the PSNMGR key. These messages can be used to verify the installation. The updates listed in the email with subject "PSS\*1\*254 FDB v4.5 Upgrade Installation Complete" should be verified. This section provides the information needed to verify successful installation. The emails also provide information about items impacted by the Dosing Check Frequency field conversion. Impacted items should be reviewed by appropriate personnel to determine if further action is necessary.

Additionally, entries in File \#51 and \#51.1 where the Frequency (In Minutes) field is populated but the Dosing Check Frequency field is not populated as well as Quick Orders with impacted File \#51.1 Dosing Check Frequency values will need identified and reviewed.

The Dosing Check Frequency Field conversion may impact Quick Orders and is included in the MailMan Messages. The criteria for inclusion is an original Dosing Check Frequency format of X#D, X#W, or X#L and has a group and package from the following table.

Example of acceptable criteria: CLINIC INFUSIONS and INPATIENT MEDICATIONS Example of unacceptable criteria: CLINIC INFUSIONS and OUTPATIENT PHARMACY

| Group              | Package              |
|------------------------|--------------------------|
| CLINIC INFUSIONS       | INPATIENT MEDICATIONS    |
| CLINIC MEDICATIONS     | INPATIENT MEDICATIONS    |
| IV MEDICATIONS         | INPATIENT MEDICATIONS    |
| NON-VA MEDICATIONS     | HERBAL/OTC/NON-VA MEDS   |
| OUTPATIENT MEDICATIONS | OUTPATIENT PHARMACY      |
| PHARMACY               | PHARMACY DATA MANAGEMENT |
| UNIT DOSE MEDICATIONS  | INPATIENT MEDICATIONS    |

WebServices:

The install will update the server and port for PEPS and PPS-N WebServices. The installer may be prompted to choose an install environment during install in the following install step:

If prompted "Enter site type into which this patch is being installed:", respond with the account type you are installing the patch in (1/2/3/4/5) (1-Pre-Prod, 2-SQA, 3-Staging, 4-Development, 5-PRODUCTION), for installs to Production, choose 5-PRODUCTION

The verifier will need access to the Web Server Manager (XOBW WEB SERVER MANAGER) to confirm the update was successful for the environment the patch was installed into.

After installation the services in PRODUCTION should have the following endpoints and ports:

> PPSN: vaww.ppsn.va.gov:443

PEPS: mocha.pharmacy.healthevet.va.gov:8011

After installation the services in PREPROD should have the following endpoints and ports:

> PPSN: vaausapppps401.aac.va.gov:443

> PEPS: mocha-pre.pharmacy.healthevet.va.gov:8011

If the endpoints and ports are not correct for the environment, a back-out is not necessary. They can be manually edited to the correct values in the Web Server Manager option.

FileMan:

- STANDARD MEDICATION ROUTES File (#51.23).

> The Standard Medication Routes entries listed below should have the following values in the First Databank Med Route field (#1) after install:

Standard Medication Routes Name First Databank Med Route

========================= =======================

INTRA-AMNIOTIC INTRA-AMNIOTIC

INTRATYMPANIC INTRATYMPANIC

IONTOPHORESIS IONTOPHORETIC

OPHTHALMIC OPHTHALMIC (EYE)

OTIC OTIC (EAR)

SUBMUCOSAL SUBMUCOSAL INJECTION

- STANDARD MEDICATION ROUTES File (#51.23).

> The following new entries should exist after install:

- ADDUCTOR CANAL BLOCK
- CERVICAL
- ECTOPIC GESTATIONAL SAC
- ENDOTRACHEAL
- HAND BULB NEBULIZER
- IMPLANT
- INFRACLAVICULAR
- INSTILLATION
- INTERSCALENE
- INTRACANALICULAR
- INTRACORONARY
- INTRALUMBAR
- INTRALYMPHATIC
- INTRAPERICARDIAL
- INTRAPROSTATIC
- INTRA-PYELOCALYCEAL
- INTRASALIVARY GLAND
- INTRA-SUBACROMIAL SPACE
- INTRA-UMBILICAL VEIN
- INTRAVENTRICULAR
- IPPB
- JUXTASCLERAL
- MISCELLANEOUS
- MUCOUS MEMBRANE
- O2 AEROSOLIZATION
- PERCUTANEOUS
- PERFUSION
- PERIARTICULAR
- PERINEURAL INJECTION
- SUBLESIONAL
- SUBRETINAL
- SUPRACHOROIDAL
- TENDON SHEATH INJ
- TRANSTRACHEAL
- TRANSURETHRAL
- Dose Units file (#51.24).

> The Dose Units entries listed below should have the following values in the FIRST DATABANK DOSE UNIT field (#1) after install:

> Dose Units Name FIRST DATABANK DOSE UNIT

- APPLICATION(S) APPLICATIONS
- APPLICATORFUL(S) APPLICATORFUL
- CAP/TAB TABLET-CAPSULE
- CAPSULE(S) CAPSULES
- DROP(S) DROPS
- INCH(ES) INCHES
- MICROGRAM(S) MICROGRAMS
- MG-PE MILLIGRAM PHENYTOIN EQUIVALENT
- MICRO UNIT(S) MICROUNITS
- MILLIONUNIT(S) MILLION UNITS
- PIECE(S) PIECES OF GUM
- PUFF(S) PUFFS
- SCOOPFUL(S) SCOOPS
- SPRAY(S) SPRAY
- STRIP(S) STRIPS
- SUPPOSITORY(IES) SUPPOSITORY
- TABLESPOONFUL(S) TABLESPOONFUL
- TABLET(S) TABLETS
- TEASPOONFUL(S) TEASPOONFUL
- THOUSAND UNITS THOUSAND UNITS
- UNIT(S) UNITS
- DOSE UNITS File (#51.24).

> The following new entries should exist after install:

- AMPULE
- BILLION CELLS
- CELL
- COLONY FORMING UNIT
- MELT
- MICROGRAM DIETARY FOLATE EQUIVALENT
- MILLICURIE
- MILLIGRAM FISH OIL
- MILLION CELLS
- MILLION PLAQUE FORMING UNITS
- MILLIUNIT
- PLAQUE FORMING UNIT
- TOWELETTE
- TUBE
- DOSE UNITS File (#51.24).

> The following entries should not exist after install:

- anti-Xa unit
- ENEMA(S)
- OVULE(S)
- SQUIRT(S)
- TROCHE(S)
- DOSE UNIT CONVERSION File (#51.25).

> Updates were made to the Dose Unit 1 field (#.01) for several entries. The Dose Unit 1 field should be updated to the FDB v4.5 values shown below after install:

- APPLICATIONS
- APPLICATORFUL
- CAPSULES
- DROPS
- INCHES
- MICROGRAMS
- MICROUNITS
- MILLION UNITS
- PIECES OF GUM
- PUFFS
- SCOOPS
- SPRAYS
- STRIPS
- SUPPOSITORY
- TABLET-CAPSULES
- TABLESPOONFUL
- TABLET
- TEASPOONFUL
- THOUSAND UNITS
- UNITS
- DOSE UNIT CONVERSION File (#51.25).

> The following entries should not exist after install:

- ENEMAS
- OVULE(S)
- SQUIRTS
- TROCHES
- DOSE UNITS File (#51.24).

> The new values listed below were added to the SYNONYM (#.01) field of the SYNONYM multiple (#2) for the following DOSE UNITS File (#51.24) entries:

- CAP/TAB
  - TABLET-CAPSULE
  - TABLET-CAPSULES
- MG-PE
  - MILLIGRAM PHENYTOIN EQUIVALENTS
- THOUSAND UNITS
  - THOUSAND UNIT
- DOSE UNIT CONVERSION File (#51.25).

> Updates were made to the DOSE UNIT 2 (#.01) field of the DOSE UNIT 2 multiple (#1) for several entries. The DOSE UNIT 2 field should be updated to the FDB v4.5 values shown below after install:

- APPFUL
  - APPLICATORFUL
- APPLIC
  - APPLICATIONS
- CENTIMETERS
  - INCHES
- EACH
  - TABLET-CAPSULES
  - CAPSULES
  - PIECES OF GUM
  - SCOOPS
  - STRIPS
  - SUPPOSITORY
  - TABLETS
- GRAMS
  - MICROGRAMS
- INHALATIONS
  - SPRAYS
  - PUFFS
- MICROUNITS
  - MILLION UNITS
  - UNITS
- MILLIGRAMS
  - MICROGRAMS
- MILLILITERS
  - DROPS
  - TABLESPOONFUL
  - TEASPOONFUL
- MILLION UNITS
  - MICROUNITS
  - THOUSAND UNITS
  - UNITS
- NANOGRAMS
  - MICROGRAMS
- PUFFS
  - SPRAYS
- SPRAYS
  - PUFFS
- THOUSAND UNITS
  - MILLION UNITS
  - UNITS
- UNITS
  - MICROUNITS
  - THOUSAND UNITS
  - MILLION UNITS
- DOSE UNIT CONVERSION File (#51.25).

> Updates were made to the DOSE UNIT 2 (#.01) field of the DOSE UNIT 2 multiple (#1) for several entries. The DOSE UNIT 2 field should no longer contain the values shown below after install:

- EACH
  - Deleted ENEMAS
  - Deleted OVULE(S)
  - Deleted TROCHES
- INHALATIONS
  - Deleted SQUIRTS
- SPRAY(S)
  - Deleted SQUIRTS

Verification of DATA DICTIONARY updates to MEDICATION INSTRUCTION File (#51):

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES

- START WITH What File: // 51 MEDICATION INSTRUCTION
- GO TO What File: MEDICATION INSTRUCTION//
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//
- Start with field: FIRST// DOSING CHECK FREQUENCY
- Go to field:
- DEVICE: ;;999

The INPUT TRANSFORM and DESCRIPTION should be updated as shown below:

51,32 DOSING CHECK FREQUENCY 0;9 FREE TEXT

INPUT TRANSFORM: K:(\$\$FREQCHK^PSSJSV(X)="") X W:\$D(X) " "\_\$\$FR

EQCHK^PSSJSV(X)

MAXIMUM LENGTH: 30

LAST EDITED: AUG 21, 2023

HELP-PROMPT: Answer must be 3-4 characters in length.

DESCRIPTION: The DOSING CHECK FREQUENCY field takes priority

over all other fields/values when determining

frequency.

PLEASE BE AWARE that the format of the

frequency in this field must employ the format

patterns of the vendor database.

The text examples within the following brackets

\[\] provide clarification of the literal

medication instruction translation for the

possible formats. Enter the dosing check

frequency in one of the following specified

formats shown below ('#' represents a whole

number, which can be 1 or 2 digits):

Q#H \[every \# hour(s), values supported for '#':

1-12, 14-24,

30, 36, 48, 60, 72 and 96, example: Q6H -

EVERY 6 HOURS\]

Q#D \[every \# day(s), values supported for '#':

1-10, 14, 21, 28,

30, 56 and 90, example: Q2D - EVERY 2

DAYS\]

Q#W \[every \# week(s), values supported for '#':

1-6, 8-10,

12, 16, 24 and 52, example: Q1W - EVERY

WEEK\]

Q#L \[every \# month(s), values supported for

'#': 1-4, 6 and 12,

example: Q3L - EVERY 3 MONTHS\]

\#XD \[times per day, values supported for '#':

1-99, example:

4XD - 4 TIMES PER DAY\]

\#XW \[times per week, values supported for '#':

1-6, example:

2XW - 2 TIMES PER WEEK\]

Verification of DATA DICTIONARY updates to ADMINISTRATION SCHEDULE File (#51.1):

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES

- START WITH What File: // 51.1  ADMINISTRATION SCHEDULE
- GO TO What File: ADMINISTRATION SCHEDULE// 
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//  
- Start with field: FIRST// 11  DOSING CHECK FREQUENCY
- Go to field:
- DEVICE: ;;999

The INPUT TRANSFORM and DESCRIPTION should be updated as shown below:

51.1,11       DOSING CHECK FREQUENCY 0;11 FREE TEXT

              INPUT TRANSFORM:  K:(\$\$FREQCHK^PSSJSV(X)="") X W:\$D(X) "   "\_\$\$FR

                                EQCHK^PSSJSV(X)

              MAXIMUM LENGTH:   30

              LAST EDITED:      AUG 21, 2023

              HELP-PROMPT:      Answer must be 3-4 characters in length.

              DESCRIPTION:      The DOSING CHECK FREQUENCY field takes priority

                                over all other fields/values when determining

                                frequency. 

                                 

                                PLEASE BE AWARE that the format of the

                                frequency in this field must employ the format

                                patterns of the vendor database.

                                 

                                The text examples within the following brackets

                                \[\] provide clarification of the literal

                                medication instruction translation for the

                                possible formats. Enter the dosing check

                                frequency in one of the following specified

                                formats shown below ('#' represents a whole

                                number, which can be 1 or 2 digits):

                                 

                                Q#H \[every \# hour(s), values supported for '#':

                                1-12, 14-24,

                                     30, 36, 48, 60, 72 and 96, example: Q6H -

                                EVERY 6 HOURS\]

                                 

                                Q#D \[every \# day(s), values supported for '#':

                                1-10, 14, 21, 28,

                                     30, 56 and 90, example: Q2D - EVERY 2

                                DAYS\]

                                           

                                Q#W \[every \# week(s), values supported for '#':

                                1-6, 8-10,

                                     12, 16, 24 and 52, example: Q1W - EVERY

                                WEEK\]

                                 

                                Q#L \[every \# month(s), values supported for

                                '#': 1-4, 6 and 12,

                                     example: Q3L - EVERY 3 MONTHS\]

                                 

                                #XD \[times per day, values supported for '#':

                                1-99, example:

                                     4XD - 4 TIMES PER DAY\]

                                 

                                #XW \[times per week, values supported for '#':

                                1-6, example:

                                     2XW - 2 TIMES PER WEEK\]

Verification of New Type Cross Reference updates to MEDICATION ROUTES File (#51.2):

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES.

- START WITH What File: // 51.2 MEDICATION ROUTES
- GO TO What File: MEDICATION ROUTES//
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//
- Start with field: FIRST// .01 NAME
- Go to field: .01 NAME
- DEVICE: ;;999

The FIELD INDEX includes an entry for FDBMRT.

51.2,.01      NAME                   0;1 FREE TEXT (Required)

              INPUT TRANSFORM:  K:\$L(X)\>45!(\$L(X)\<3)!'(X'?1P.E)!(X'?.ANP) X

              LAST EDITED:      AUG 29, 2024

              HELP-PROMPT:      Answer must be 3-45 characters in length.

              DESCRIPTION:      This is a route of administration for a

                                medication. 

              TECHNICAL DESCR:  This is used to show how a medication is to be

                                administered to patient. 

              DELETE TEST:      .01,0)= I 1 D EN^DDIOL("DELETIONS ARE NOT ALLOW

                                ED!","","!?10")

              DELETE AUTHORITY: ^

              GROUP:            PS

              CROSS-REFERENCE:  51.2^B

                                1)= S ^PS(51.2,"B",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.2,"B",\$E(X,1,30),DA)

              CROSS-REFERENCE:  51.2^AUDC^MUMPS

                                1)= I '\$D(PSGINITF) S ^PS(51.2,"AUDC")=\$S(\$D(^P

                                S(59.7,1,20)):\$P(^(20),"^"),1:"")

                                2)= Q

                                Used by Unit Dose post-inits to determine if a

                                conversion needs to be run on this file.  In

                                the form of: ^PS(51.2,"AUDC")

              FIELD INDEX:      FDBMRT (#1150)    REGULAR    IR

                                LOOKUP & SORTING

                  Short Descr:  Full length index on the Name field

                  Description:  This is a full length index on the Name field

                                for use in First Databank order processing. 

                    Set Logic:  S ^PS(51.2,"FDBMRT",\$E(X,1,45),DA)=""

                   Kill Logic:  K ^PS(51.2,"FDBMRT",\$E(X,1,45),DA)

                   Whole Kill:  K ^PS(51.2,"FDBMRT")

                         X(1):  NAME  (51.2,.01)  (Subscr 1)  (Len 45)

                                (forwards)

Verification of New Type Cross Reference and DATA DICTIONARY updates to STANDARD MEDICATION ROUTES File (#51.23):

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES

- START WITH What File: // 51.23 STANDARD MEDICATION ROUTES
- GO TO What File: STANDARD MEDICATION ROUTES//
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//
- Start with field: FIRST// 1 FIRST DATABANK MED ROUTE
- Go to field: 1 FIRST DATABANK MED ROUTE
- DEVICE: ;;999

The INPUT TRANSFORM should be updated as shown below.

The HELP-PROMPT should be updated to state 3-40 characters in length.

The FIELD INDEX includes an entry for FDBMRT.

51.23,1       FIRST DATABANK MED ROUTE 0;2 FREE TEXT

              INPUT TRANSFORM:  K:\$L(X)\>40!(\$L(X)\<3)!(\$E(X,1)=" ")!(\$E(X,\$L(X))

                                =" ")!(X\["  ")!(X'?.UNP) X

              LAST EDITED:      AUG 29, 2024

              HELP-PROMPT:      Answer must be 3-40 characters in length,

                                comprised only of uppercase letters, numerics,

                                and punctuation, and contain no leading,

                                trailing, or consecutive spaces.

              DESCRIPTION:      This field provides the mapping from the Vista

                                Standard Medication Route to the First DataBank

                                Medication Route. The First DataBank Medication

                                Route will be used when processing the order

                                checks provided by First DataBank. 

              WRITE AUTHORITY:  ^

              NOTES:            XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

              CROSS-REFERENCE:  51.23^C

                                1)= S ^PS(51.23,"C",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.23,"C",\$E(X,1,30),DA)

                                This cross reference is a regular cross

                                reference on the FIRST DATABANK MED ROUTE

                                field. It sets the global: PS(51.23,"C",FIRST

                                DATABANK MED ROUTE, Internal Entry Number)="". 

              FIELD INDEX:      FDBMRT (#1148)    REGULAR    IR

                                LOOKUP & SORTING

                  Short Descr:  This cross reference is to accomodate the

                                change in length for Med Routes.

                  Description:  This is a full length index on the First

                                Databank Med Route field for use in First

                                Databank order processing. 

                    Set Logic:  S ^PS(51.23,"FDBMRT",\$E(X,1,40),DA)=""

                   Kill Logic:  K ^PS(51.23,"FDBMRT",\$E(X,1,40),DA)

                   Whole Kill:  K ^PS(51.23,"FDBMRT")

                         X(1):  FIRST DATABANK MED ROUTE  (51.23,1)  (Subscr 1)

                                (Len 40)  (forwards)

Verification of New Type Cross Reference and DATA DICTIONARY updates to DOSE UNITS File (#51.24):

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES

- START WITH What File: // 51.24  DOSE UNITS
- GO TO What File: DOSE UNITS//
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//  
- Start with field: FIRST// .01  NAME
- Go to field: 2  SYNONYM
- DEVICE: ;;999

For the Name (#.01) field:

The INPUT TRANSFORM should be updated as shown below.

The HELP-PROMPT should be updated to state 1-40 characters in length.

The FIELD INDEX includes an entry for FDBNAME.

51.24,.01     NAME                   0;1 FREE TEXT (Required)

              INPUT TRANSFORM:  K:\$L(X)\>40!(\$L(X)\<1)!(\$E(X,1)=" ")!(\$E(X,\$L(X))

                                =" ")!(X\["  ")!(X'?.ANP)!'(X'?1P.E) X

              LAST EDITED:      AUG 29, 2024

              HELP-PROMPT:      Answer must be 1-40 characters in length,

                                comprised of upper and lower case letters,

                                numerics, and punctuation, but no leading

                                punctuation, and contain no leading, trailing,

                                or consecutive spaces.

              DESCRIPTION:      This is the name of the Dose Unit. Local

                                Possible Dosages entries in the DRUG (#50) File

                                will be mapped to entries in this file. This

                                mapping will enable the software to derive a

                                First DataBank Dose Unit, also in this file,

                                that can be passed into the Dose API for Dose

                                checks for medication orders. 

              PRE-LOOKUP:       I \$G(DIC(0))\["L",'\$D(XUMF) K X D EN^DDIOL("Entr

                                ies must be edited via the Master File Server (

                                MFS).","","!?5")

              DELETE TEST:      1,0)= D:'\$D(XUMF) EN^DDIOL("Entries must be ina

                                ctivated via the Master File Server(MFS).","","

                                !?5") I '\$D(XUMF)

              LAYGO TEST:       1,0)= D:'\$D(XUMF) EN^DDIOL("Entries must be add

                                ed via the Master File Server(MFS).","","!?5")

                                I \$D(XUMF)

              WRITE AUTHORITY:  ^

              NOTES:            XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

              CROSS-REFERENCE:  51.24^B

                                1)= S ^PS(51.24,"B",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.24,"B",\$E(X,1,30),DA)

              FIELD INDEX:      UPCASE (#147)    REGULAR    IR

                                LOOKUP & SORTING

                  Short Descr:  Converts mixed case to uppercase for lookup

                  Description:  This cross-reference converts mixed case

                                (TallMan lettering) to uppercase so that when a

                                lookup is done, the list collates properly

                                while still retaining TallMan lettering in the

                                NAME field (#.01). 

                    Set Logic:  S ^PS(51.24,"UPCASE",\$E(X,1,30),DA)=""

                   Kill Logic:  K ^PS(51.24,"UPCASE",\$E(X,1,30),DA)

                   Whole Kill:  K ^PS(51.24,"UPCASE")

                         X(1):  NAME  (51.24,.01)  (Subscr 1)  (Len 30)

                                (forwards)

                                  Transform (Storage):  S X=\$\$UP^XLFSTR(X)

              FIELD INDEX:      FDBNAME (#1151)    REGULAR    IR

                                LOOKUP & SORTING

                  Short Descr:  Full length index on the Name field

                  Description:  This is a full length index on the Name field

                                for use in First Databank order processing. 

                    Set Logic:  S ^PS(51.24,"FDBNAME",\$E(X,1,40),DA)=""

                   Kill Logic:  K ^PS(51.24,"FDBNAME",\$E(X,1,40),DA)

                   Whole Kill:  K ^PS(51.24,"FDBNAME")

                         X(1):  NAME  (51.24,.01)  (Subscr 1)  (Len 40)

                                (forwards)

For the First Databank Dose Unit (#1) field:

The INPUT TRANSFORM should be updated as shown below.

The HELP-PROMPT should be updated to state 1-40 characters in length.

The FIELD INDEX includes an entry for FDBUNIT.

51.24,1       FIRST DATABANK DOSE UNIT 0;2 FREE TEXT

              INPUT TRANSFORM:  K:\$L(X)\>40!(\$L(X)\<1)!(\$E(X,1)=" ")!(\$E(X,\$L(X))

                                =" ")!(X\["  ")!(X'?.ANP) X

              LAST EDITED:      AUG 29, 2024

              HELP-PROMPT:      Answer must be 1-40 characters in length,

                                comprised of upper and lower case letters,

                                numerics, and punctuation, and contain no

                                leading, trailing, or consecutive spaces.

              DESCRIPTION:      This field provides the mapping from the Vista

                                Dose Unit to the First DataBank Dose Unit. The

                                First DataBank Dose Unit will be used when

                                processing the dosage checks provided by First

                                DataBank. 

              WRITE AUTHORITY:  ^

              NOTES:            XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

              CROSS-REFERENCE:  51.24^C

                                1)= S ^PS(51.24,"C",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.24,"C",\$E(X,1,30),DA)

                                This cross reference is a regular cross

                                reference on the FIRST DATABANK DOSE UNIT

                                field. It sets the global: PS(51.24,"C",FIRST

                                DATABANK DOSE UNIT, Internal Entry Number)="". 

              FIELD INDEX:      FDBUNIT (#1152)    REGULAR    IR

                                LOOKUP & SORTING

                  Short Descr:  Full length index on the FDB Dose Unit field

                  Description:  This is a full length index on the First

                                Databank Dose Unit field for use in First

                                Databank order processing. 

                    Set Logic:  S ^PS(51.24,"FDBUNIT",\$E(X,1,40),DA)=""

                   Kill Logic:  K ^PS(51.24,"FDBUNIT",\$E(X,1,40),DA)

                   Whole Kill:  K ^PS(51.24,"FDBUNIT")

                         X(1):  FIRST DATABANK DOSE UNIT  (51.24,1)  (Subscr 1)

                                (Len 40)  (forwards)

For the Synonym (#.01) field of the Synonym (#2) multiple:

The INPUT TRANSFORM should be updated as shown below.

The HELP-PROMPT should be updated to state 1-40 characters in length.

The FIELD INDEX includes an entry for FDBSYN.

51.24,2       SYNONYM                1;0 Multiple \#51.242

              WRITE AUTHORITY:  ^

51.242,.01      SYNONYM                0;1 FREE TEXT (Multiply asked)

                INPUT TRANSFORM:K:\$L(X)\>40!(\$L(X)\<1)!(\$E(X,1)=" ")!(\$E(X,\$L(X))

                                =" ")!(X\["  ")!(X'?.ANP) X

                MAXIMUM LENGTH:   40

                LAST EDITED:    SEP 16, 2024

                HELP-PROMPT:    Answer must be 1-40 characters in length,

                                comprised of upper and lower case letters,

                                numerics, and punctuation, and contain no

                                leading, trailing, or consecutive spaces.

                DESCRIPTION:    This is a synonym for the NAME field, which is

                                the name of the DOSE UNIT. 

                WRITE AUTHORITY:^

                NOTES:          XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

                CROSS-REFERENCE:51.242^B

                                1)= S ^PS(51.24,DA(1),1,"B",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.24,DA(1),1,"B",\$E(X,1,30),DA)

                CROSS-REFERENCE:51.24^D

                                1)= S ^PS(51.24,"D",\$E(X,1,30),DA(1),DA)=""

                                2)= K ^PS(51.24,"D",\$E(X,1,30),DA(1),DA)

                                This is a whole file cross reference on the

                                SYNONYM (#.01) Field of the SYNONYM (#51.242)

                                Subfile. It sets the global

                                PS(51.24,"D",SYNONYM,DA(1),DA)="". 

                FIELD INDEX:    FDBSYN (#1153)    REGULAR    IR

                                LOOKUP & SORTING    WHOLE FILE (#51.24)

                  Short Descr:  Full length index on the Synonym field

                  Description:  This is a full length index on the Synonym

                                field for use in First Databank order

                                processing. 

                    Set Logic:  S ^PS(51.24,"FDBSYN",\$E(X,1,40),DA(1),DA)=""

                   Kill Logic:  K ^PS(51.24,"FDBSYN",\$E(X,1,40),DA(1),DA)

                   Whole Kill:  K ^PS(51.24,"FDBSYN")

                         X(1):  SYNONYM  (51.242,.01)  (Subscr 1)  (Len 40)

                                (forwards)

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System configuration is not applicable for this VistA patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database tuning is not applicable for this VistA patch.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings. In the event of a catastrophic failure, the decision to backout the patch and rollback any necessary database changes may be made. Back-out will be done only with the concurrence and participation of development team and appropriate VA site/region personnel. The decision to back-out software will be a joint decision between development team, VA site/region personnel and other appropriate VA personnel.

The Standards and Terminology Services (STS) team should be informed of the decision to perform a rollback.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out Procedures are only needed if there are major problems resulting from the installation of this patch. You must have concurrence from Health Standards Portfolio (HSP) Patient Care Services (PCS) support before a back-out can occur. Enter a ServiceNow ticket to obtain this concurrence.

A back-out decision due to major issues with this patch could occur during site Mirror Testing, Site Production Testing or after National Release to the Field. The back-out strategy is defined in the sections that follow.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If it is determined that a back-out of patch PSS\*1\*254 is needed, it must be backed out with patch PSJ\*5\*423. The order of the back-out does not matter. Patch PSO\*7\*779 does not need to be backed out as it is an information only patch that provides updates to outpatient pharmacy user manuals.

If the back-out is post-release of patch PSS\*1\*254, patch PSS\*1\*254 should be assigned status of "Entered in Error" in Forum's NPM.

If an installer chooses the wrong account type in this step of the install:

> If prompted "Enter site type into which this patch is being installed:", respond with the account type you are installing the patch in (1/2/3/4/5) (1-Pre-Prod, 2-SQA, 3-Staging, 4-Development, 5-PRODUCTION)

A back-out is not necessary. The installer will need access to the Web Server Manager (XOBW WEB SERVER MANAGER) option. This option can be used to manually edit the parameters to the correct post install values for the environment. Refer to the WebServices part of Section 4.9, Installation Verification Procedure for more details.

The initial install of the patch will run the data conversion. The initial settings are saved off during the conversion to the global ^XTMP("PSSP254B") for use in the rollback. This global exists until a rollback is performed. If a rollback is not performed, the global is automatically deleted after six months. The data conversion is only executed on the initial installation of the patch. Re-installing the patch without a rollback will install the routines and data dictionary updates but will not perform the data conversion.

A rollback uses this global to restore the initial data values and then deletes the global. Re-installing the patch after rollback will perform the data conversion since it is essentially a new install.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load Testing is not applicable for this VistA patch.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Accetptance Testing (UAT) was completed at five test sites. Refer to section 3.2.2 Site Information (Locations, Deployment Recipients).

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It may be decided to back-out this patch if the project is canceled, the requested changes implemented by the patch are no longer desired by VA OIT and the Pharmacy Business team, or the patch produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out risks are the standard risks with the back-out of any patch.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any back-out decision should be a joint decision of the Area Manager, the Business Owner (or their representative), the Program Manager with input from the Application Coordinator, and the project development team.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out plan for this patch consists of several steps. These steps are rollback of data, installing the patch backup created prior to installation, Index rebuild, and deleting New Style Cross References. The PSS\*1\*254 build contains a restore routine that is delivered with the install of the patch. The restore routine returns non-routine components that are not restored by the standard backup installation to their pre-patch state. The steps must be performed in the order listed below.

1.  Rollback the Data
- The data updates to the following files are backed up in the global ^XTMP("PSSP254B") upon patch install:

> MEDICATION INSTRUCTION (#51)

> ADMINISTRATION SCHEDULE (#51.1)

> STANDARD MEDICATION ROUTES (#51.23)

> DOSE UNITS (#51.24)

> DOSE UNIT CONVERSION (#51.25)

- The settings in Web Services is also backed up in the ^XTMP("PSSP254B") global during the patch install.
- The conversion data will be rolled back by site/region personnel calling a routine.

> From the M/Cache prompt: D BACKOUT^PSSP254U

> The user will be presented with a prompt "Are you sure" as a safety check.

- The global ^XTMP("PSSP254B") will be deleted after this step is performed.
2.  Back-out the Patch
- Prior to installing an updated KIDS package, the site/region should have saved a backup of the BUILD in a mail message using the Backup a Transport Global \[XPD BACKUP\] menu option (this is done at time of install).
- The message containing the backed-up routines can be loaded with the "Xtract KIDS" function at the Message Action prompt. The Packman function "INSTALL/CHECK MESSAGE" is then used to install the backed up routines onto the VistA System.
- If the patch was backed up for the build, from the Kernel Installation and Distribution System Menu, select the Installation Menu. Then select the Install Package(s) option and choose the patch (PSS\*1.0\*254b) to install.
3.  Index Rebuild
- A few indices need to be rebuilt by site/region personnel after the patch is rolled back.

> From the M/Cache prompt: X ^XTMP("PSSP254U","CODE","DOSEUNIT")

> From the M/Cache prompt: X ^XTMP("PSSP254U","CODE","ROUTE")

4.  New Style Cross Reference

> Five new style cross references need to be manually deleted using FileMan UTILITY FUNCTIONS \> CROSS-REFERENCE A FIELD OR FILE. Follow the steps below:

> Step 1: For these four new style cross references, follow the instructions that are listed below

1.  File 51.2 Field .01 – FDBMRT
2.  File 51.23 Field 1 – FDBMRT
3.  File 51.24 Field .01 – FDBNAME
4.  File 51.24 Field 1 – FDBUNIT
- Select OPTION: UTILITY FUNCTIONS
- Select UTILITY OPTION: CROSS-REFERENCE A FIELD OR FILE
- What type of cross-reference (Traditional or New)? Traditional// NEW
- Modify what File: STANDARD MEDICATION ROUTES// 51.23 STANDARD MEDICATION ROUTES (98 entries)
- Select Subfile:
- Current Indexes on file \#51.23:

> 79 'AMASTERVUID' index

> 80 'B' index

> 1148 'FDBMRT' index

- Choose E (Edit)/D (Delete)/C (Create): DELETE
- Which Index do you wish to delete? 1148 FDBMRT
- Are you sure you want to delete the index definition? NO// YES

> Index definition deleted.

- Do you want to delete the data in the old index now? YES//

> Removing old index ... DONE!

> Step 2: For this one new style cross reference, follow the instructions that are listed below

1.  File 51.24 Field 2 – FDBSYN
- Select UTILITY OPTION: CROSS-REFERENCE A FIELD OR FILE
- What type of cross-reference (Traditional or New)? Traditional// NEW
- Modify what File: DOSE UNITS// (63 entries)
- Select Subfile: 2 SYNONYM (Subfile \#51.242)
- Current Indexes on subfile \#51.242:

> 864 'FDBSYN' whole file index (resides on file \#51.24)

- Choose E (Edit)/D (Delete)/C (Create): DELETE
- Which Index do you wish to delete? 864// FDBSYN
- Are you sure you want to delete the index definition? NO// YES

> Index definition deleted.

- Do you want to delete the data in the old index now? YES//

> Removing old index ... DONE!

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Back-out Procedure can be verified by printing the first 2 lines of the PSS routines contained in this patch using the option First Line Routine Print \[XU FIRST LINE PRINT\]. Once the routines contained in the PSS\*1.0\*254 patch have been backed out, the second line of each routine will no longer contain the designation of patch PSS\*1.0\*254. Verification that new components were removed and modified components were returned to their pre-patch state should also be performed. See section 6.6 Rollback Verification Procedure.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data records introduced by this patch are rolled back as part of the back-out procedure and cannot be run separately.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback is integral to the back-out. See criteria in 5.3 Back-Out Criteria.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback risks are the standard risks with the rollback of any patch.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback occurs as part of the back-out: authority for rollback is dependent on the back-out decision and authority.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback occurs as part of the back-out. See procedure in 5.6 Back-Out Procedure.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the BUILD backup for this patch sends MailMan messages to the installer and users with the PSNMGR key. These messages can be used to verify the rollback. The updates listed in the email with subject "PSS\*1\*254 FDB v4.5 Upgrade Uninstall" should be verified. This section provides the information needed to verify successful rollback/back-out of this patch.

WebServices:

The backout/rollback will restore the server and port for PEPS and PPS-N WebServices to their pre-patch settings.

The verifier will need access to the Web Server Manager (XOBW WEB SERVER MANAGER) option to confirm the rollback successfully restored the settings to the pre-patch condition.

After rollback the services in PRODUCTION should have the following endpoints and ports:

> PPSN: vaww.ppsn.va.gov:443

PEPS: mocha.pharmacy.healthevet.va.gov:8010

After rollback the services in PREPROD should have the following endpoints and ports:

> PPSN: vaausapppps400.aac.va.gov:443

> PEPS: mocha-pre.pharmacy.healthevet.va.gov:8010

If the endpoints and ports are not correct for the environment, they can be manually edited to the correct values in the Web Server Manager option.

FileMan:

- STANDARD MEDICATION ROUTES File (#51.23):

> The Standard Medication Routes entries listed below should have the following values in the First Databank Med Route field (#1) after rollback:

Standard Medication Routes Name First Databank Med Route

========================= ===================

INTRA-AMNIOTIC (Not Set)

INTRATYMPANIC (Not Set)

IONTOPHORESIS NOT APPLICABLE

OPHTHALMIC OPHTHALMIC

OTIC OTIC

SUBMUCOSAL SUBMUCOSAL

- STANDARD MEDICATION ROUTES File (#51.23).

> The following entries should not exist after rollback:

- ADDUCTOR CANAL BLOCK
- CERVICAL
- ECTOPIC GESTATIONAL SAC
- ENDOTRACHEAL
- HAND BULB NEBULIZER
- IMPLANT
- INFRACLAVICULAR
- INSTILLATION
- INTERSCALENE
- INTRACANALICULAR
- INTRACORONARY
- INTRALUMBAR
- INTRALYMPHATIC
- INTRAPERICARDIAL
- INTRAPROSTATIC
- INTRA-PYELOCALYCEAL
- INTRASALIVARY GLAND
- INTRA-SUBACROMIAL SPACE
- INTRA-UMBILICAL VEIN
- INTRAVENTRICULAR
- IPPB
- JUXTASCLERAL
- MISCELLANEOUS
- MUCOUS MEMBRANE
- O2 AEROSOLIZATION
- PERCUTANEOUS
- PERFUSION
- PERIARTICULAR
- PERINEURAL INJECTION
- SUBLESIONAL
- SUBRETINAL
- SUPRACHOROIDAL
- TENDON SHEATH INJ
- TRANSTRACHEAL
- TRANSURETHRAL
- DOSE UNITS File (#51.24):

> The Dose Units entries listed below should have the following values in the FIRST DATABANK DOSE UNIT field (#1) after rollback.

> Dose Units Name FIRST DATABANK DOSE UNIT

- APPLICATION(S) APPLICATION(S)
- APPLICATORFUL(S) APPLICATORFUL(S)
- CAP/TAB TAB-CAPS
- CAPSULE(S) CAPSULE(S)
- DROP(S) DROP(S)
- INCH(ES) INCH(ES)
- MICROGRAM(S) MICROGRAM(S)
- MG-PE MG PE
- MICRO UNIT(S) MICRO UNITS
- MILLIONUNIT(S) MILLIONUNIT(S)
- PIECE(S) PIECE(S)
- PUFF(S) PUFF(S)
- SCOOPFUL(S) SCOOPFULS
- SPRAY(S) SPRAY(S)
- STRIP(S) STRIP(S)
- SUPPOSITORY(IES) SUPPOSITORY(IES)
- TABLESPOONFUL(S) TABLESPOONFULS
- TABLET(S) TABLET(S)
- TEASPOONFUL(S) TEASPOONFULS
- THOUSAND UNITS TU
- UNIT(S) UNIT(S)
- DOSE UNITS File (#51.24):

> The following entries should not exist after rollback.

- AMPULE
- BILLION CELLS
- CELL
- COLONY FORMING UNIT
- MELT
- MICROGRAM DIETARY FOLATE EQUIVALENT
- MILLICURIE
- MILLIGRAM FISH OIL
- MILLION CELLS
- MILLION PLAQUE FORMING UNITS
- MILLIUNIT
- PLAQUE FORMING UNIT
- TOWELETTE
- TUBE
- DOSE UNITS File (#51.24).

The following entries should exist after rollback:

- anti-Xa unit
- ENEMA(S)
- OVULE(S)
- SQUIRT(S)
- TROCHE(S)
- DOSE UNIT CONVERSION File (#51.25)

> The Dose Unit 1 field (#.01) names should be the following after rollback:

- APPLICATION(S)
- APPLICATORFUL(S)
- CAPSULE(S)
- DROP(S)
- INCH(ES)
- MICROGRAM(S)
- MICRO UNITS
- MILLIONUNIT(S)
- PIECE(S)
- PUFF(S)
- SCOOPFULS
- SPRAY(S)
- STRIP(S)
- SUPPOSITORY(IES)
- TAB-CAPS
- TABLESPOONFULS
- TABLET(S)
- TEASPOONFULS
- TU
- UNIT(S)
- DOSE UNIT CONVERSION File (#51.25).

> The following entries should exist after rollback:

- ENEMAS
- OVULE(S)
- SQUIRTS
- TROCHES
- DOSE UNITS File (#51.24)

> The synonyms listed below for the following DOSE UNITS File (#51.24) entries should no longer exist after rollback. The SYNONYM (#.01) field is in the SYNONYM multiple (#2).

- CAP/TAB
  - TABLET-CAPSULE
  - TABLET-CAPSULES
- MG-PE
  - MILLIGRAM PHENYTOIN EQUIVALENTS
- THOUSAND UNITS
  - THOUSAND UNIT
- DOSE UNIT CONVERSION File (#51.25)

> The Dose Unit Conversion entries listed below should have the following values in the DOSE UNIT 2 (#.01) field of the DOSE UNIT 2 multiple (#1) after rollback.

- APPFUL
  - APPLICATORFUL(S)
- APPLIC
  - APPLICATION(S)
- CENTIMETERS
  - INCH(ES)
- EACH
  - TAB-CAPS
  - CAPSULE(S)
  - PIECE(S)
  - SCOOPFULS
  - STRIP(S)
  - SUPPOSITORY(IES)
  - TABLET(S)
- GRAMS
  - MICROGRAM(S)
- INHALATIONS
  - SPRAY(S)
  - PUFF(S)
- MICRO UNITS
  - MILLIONUNIT(S)
  - UNIT(S)
- MILLIGRAMS
  - MICROGRAM(S)
- MILLILITERS
  - DROP(S)
  - TABLESPOONFULS
  - TEASPOONFULS
- MILLIONUNIT(S)
  - MICRO UNITS
  - TU
  - UNIT(S)
- NANOGRAMS
  - MICROGRAM(S)
- PUFF(S)
  - SPRAY(S)
- SPRAY(S)
  - PUFF(S)
- TU
  - MILLIONUNIT(S)
  - UNIT(S)
- UNIT(S)
  - MICRO UNITS
  - TU
  - MILLIONUNIT(S)
- DOSE UNIT CONVERSION File (#51.25).

> Updates were made to the DOSE UNIT 2 (#.01) field of the DOSE UNIT 2 multiple (#1) for several entries. The DOSE UNIT 2 field should have the values shown below added back after rollback:

- EACH
  - ENEMAS
  - OVULE(S)
  - TROCHES
- INHALATIONS
  - SQUIRTS
- SPRAY(S)
  - SQUIRTS

Verification of the Rollback of the DATA DICTIONARY updates to MEDICATION INSTRUCTION File (#51)

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES

- START WITH What File: // 51 MEDICATION INSTRUCTION
- GO TO What File: MEDICATION INSTRUCTION//
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//
- Start with field: FIRST// DOSING CHECK FREQUENCY
- Go to field:
- DEVICE: ;;999

The INPUT TRANSFORM and DESCRIPTION should be rolled back as shown below:

51,32         DOSING CHECK FREQUENCY 0;9 FREE TEXT

              INPUT TRANSFORM:  D DFCHK^PSSJSV

              LAST EDITED:      SEP 27, 2022

              HELP-PROMPT:      Answer must be 3-4 characters in length.

              DESCRIPTION:      The DOSING CHECK FREQUENCY field takes priority

                                over all other fields/values when determining

                                frequency. 

                                     

                                PLEASE BE AWARE that the format of the

                                frequency in this field must employ the format

                                patterns of the vendor database, which always

                                places the numeric value in the middle position

                                of the medication instruction.  In some cases

                                an 'X' (symbol for 'times') must be entered as

                                the first character, although it is still

                                translated as the number of times per

                                designated period. 

                                  

                                The text examples within the following brackets

                                \[\] provide clarification of the literal

                                medication instruction translation for the

                                possible formats.  Enter the dosing check

                                frequency in one of the following specified

                                formats (# represents a whole number):

                                 

                                Q#H \[every \# hour(s), such as every 5 hours\]

                                 

                                Q#D \[every \# day(s), such as every 3 days\]

                                 

                                Q#W \[every \# week(s), such as every 5 weeks\]

                                 

                                Q#L \[every \# month(s), such as every 3 months\]

                                 

                                X#D \[times per day, such as 17 times per day\]

                                 

                                X#W \[times per week, such as 3 times per week\]

                                 

                                X#L \[times per month, such as 4 times per

                                month\]

                                 

                                Numeric value can be 1-2 characters. 

Verification of the Rollback of the DATA DICTIONARY updates to ADMINISTRATION SCHEDULE File (#51.1):

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES

- START WITH What File: // 51.1  ADMINISTRATION SCHEDULE
- GO TO What File: ADMINISTRATION SCHEDULE//
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//  
- Start with field: FIRST// 11  DOSING CHECK FREQUENCY
- Go to field:
- DEVICE: ;;999

The INPUT TRANSFORM and DESCRIPTION should be rolled back as shown below:

51.1,11       DOSING CHECK FREQUENCY 0;11 FREE TEXT

              INPUT TRANSFORM:  D DFCHK^PSSJSV

              LAST EDITED:      SEP 27, 2022

              HELP-PROMPT:      Answer must be 3-4 characters in length.

              DESCRIPTION:      The DOSING CHECK FREQUENCY field takes priority

                                over all other fields/values when determining

                                frequency. 

                                     

                                PLEASE BE AWARE that the format of the

                                frequency in this field must employ the format

                                patterns of the vendor database, which always

                                places the numeric value in the middle position

                                of the schedule.  In some  cases an 'X' (symbol

                                for 'times') must be entered as the first

                                character, although it is still translated as

                                the number of times per designated period. 

                                 

                                The text examples within the following brackets

                                \[\] provide clarification of the literal

                                schedule translation for the possible formats.

                                Enter the dosing check frequency in one of the

                                following specified formats (# represents a

                                whole number):

                                 

                                Q#H \[every \# hour(s), such as every 5 hours\]

                                 

                                Q#D \[every \# day(s), such as every 3 days\]

                                 

                                Q#W \[every \# week(s), such as every 5 weeks\]

                                 

                                Q#L \[every \# month(s), such as every 3 months\]

                                 

                                X#D \[times per day, such as 17 times per day\]

                                 

                                X#W \[times per week, such as 3 times per week\]

                                 

                                X#L \[times per month, such as 4 times per

                                month\]

                                 

                                Numeric value can be 1-2 characters. 

Verification of Rollback of the New Type Cross Reference updates to MEDICATION ROUTES File (#51.2):

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES

- START WITH What File: // 51.2  MEDICATION ROUTES
- GO TO What File: MEDICATION ROUTES//
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//   
- Start with field: FIRST// .01  NAME
- Go to field: .01  NAME
- DEVICE: ;;999

The FIELD INDEX no longer includes an entry for FDBMRT as shown below:

51.2,.01      NAME                   0;1 FREE TEXT (Required)

              INPUT TRANSFORM:  K:\$L(X)\>45!(\$L(X)\<3)!'(X'?1P.E)!(X'?.ANP) X

              LAST EDITED:      MAR 10, 2017

              HELP-PROMPT:      Answer must be 3-45 characters in length.

              DESCRIPTION:      This is a route of administration for a

                                medication. 

              TECHNICAL DESCR:  This is used to show how a medication is to be

                                administered to patient. 

              DELETE TEST:      .01,0)= I 1 D EN^DDIOL("DELETIONS ARE NOT ALLOW

                                ED!","","!?10")

              DELETE AUTHORITY: ^

              GROUP:            PS

              CROSS-REFERENCE:  51.2^B

                                1)= S ^PS(51.2,"B",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.2,"B",\$E(X,1,30),DA)

              CROSS-REFERENCE:  51.2^AUDC^MUMPS

                                1)= I '\$D(PSGINITF) S ^PS(51.2,"AUDC")=\$S(\$D(^P

                                S(59.7,1,20)):\$P(^(20),"^"),1:"")

                                2)= Q

                                Used by Unit Dose post-inits to determine if a

                                conversion needs to be run on this file.  In

                                the form of: ^PS(51.2,"AUDC")

Verification of Rollback of the New Type Cross Reference and DATA DICTIONARY updates to STANDARD MEDICATION ROUTES File (#51.23):

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES

- START WITH What File: // 51.23 STANDARD MEDICATION ROUTES
- GO TO What File: STANDARD MEDICATION ROUTES//
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//
- Start with field: FIRST// 1 FIRST DATABANK MED ROUTE
- Go to field: 1 FIRST DATABANK MED ROUTE
- DEVICE: ;;999

The INPUT TRANSFORM should be rolled back as shown below.

The HELP-PROMPT should be rolled back to state 3-30 characters in length.

The FIELD INDEX no longer includes an entry for FDBMRT.

51.23,1       FIRST DATABANK MED ROUTE 0;2 FREE TEXT

              INPUT TRANSFORM:  K:\$L(X)\>30!(\$L(X)\<3)!(\$E(X,1)=" ")!(\$E(X,\$L(X))

                                =" ")!(X\["  ")!(X'?.UNP) X

              LAST EDITED:      JAN 07, 2008

              HELP-PROMPT:      Answer must be 3-30 characters in length,

                                comprised only of uppercase letters, numerics,

                                and punctuation, and contain no leading,

                                trailing, or consecutive spaces.

              DESCRIPTION:      This field provides the mapping from the Vista

                                Standard Medication Route to the First DataBank

                                Medication Route. The First DataBank Medication

                                Route will be used when processing the order

                                checks provided by First DataBank. 

              WRITE AUTHORITY:  ^

              NOTES:            XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

              CROSS-REFERENCE:  51.23^C

                                1)= S ^PS(51.23,"C",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.23,"C",\$E(X,1,30),DA)

                                This cross reference is a regular cross

                                reference on the FIRST DATABANK MED ROUTE

                                field. It sets the global: PS(51.23,"C",FIRST

                                DATABANK MED ROUTE, Internal Entry Number)="". 

Verification of rollback of New Type Cross Reference and DATA DICTIONARY updates to DOSE UNITS File (#51.24):

FileMan Option DATA DICTIONARY UTILITIES \> LIST FILE ATTRIBUTES

- START WITH What File: // 51.24  DOSE UNITS
- GO TO What File: DOSE UNITS//
- Select SUB-FILE:
- Select LISTING FORMAT: STANDARD//  
- Start with field: FIRST// .01  NAME
- Go to field: 2  SYNONYM
- DEVICE: ;;999

For the Name (#.01) field:

The INPUT TRANSFORM should be rolled back as shown below.

The HELP-PROMPT should be rolled back to state 1-30 characters in length.

The FIELD INDEX no longer includes an entry for FDBNAME.

51.24,.01     NAME                   0;1 FREE TEXT (Required)

              INPUT TRANSFORM:  K:\$L(X)\>30!(\$L(X)\<1)!(\$E(X,1)=" ")!(\$E(X,\$L(X))

                                =" ")!(X\["  ")!(X'?.ANP)!'(X'?1P.E) X

              LAST EDITED:      JUN 08, 2011

              HELP-PROMPT:      Answer must be 1-30 characters in length,

                                comprised of upper and lower case letters,

                                numerics, and punctuation, but no leading

                                punctuation, and contain no leading, trailing,

                                or consecutive spaces.

              DESCRIPTION:      This is the name of the Dose Unit. Local

                                Possible Dosages entries in the DRUG (#50) File

                                will be mapped to entries in this file. This

                                mapping will enable the software to derive a

                                First DataBank Dose Unit, also in this file,

                                that can be passed into the Dose API for Dose

                                checks for medication orders. 

              PRE-LOOKUP:       I \$G(DIC(0))\["L",'\$D(XUMF) K X D EN^DDIOL("Entr

                                ies must be edited via the Master File Server (

                                MFS).","","!?5")

              DELETE TEST:      1,0)= D:'\$D(XUMF) EN^DDIOL("Entries must be ina

                                ctivated via the Master File Server(MFS).","","

                                !?5") I '\$D(XUMF)

              LAYGO TEST:       1,0)= D:'\$D(XUMF) EN^DDIOL("Entries must be add

                                ed via the Master File Server(MFS).","","!?5")

                                I \$D(XUMF)

              WRITE AUTHORITY:  ^

              NOTES:            XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

              CROSS-REFERENCE:  51.24^B

                                1)= S ^PS(51.24,"B",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.24,"B",\$E(X,1,30),DA)

              FIELD INDEX:      UPCASE (#147)    REGULAR    IR

                                LOOKUP & SORTING

                  Short Descr:  Converts mixed case to uppercase for lookup

                  Description:  This cross-reference converts mixed case

                                (TallMan lettering) to uppercase so that when a

                                lookup is done, the list collates properly

                                while still retaining TallMan lettering in the

                                NAME field (#.01). 

                    Set Logic:  S ^PS(51.24,"UPCASE",\$E(X,1,30),DA)=""

                   Kill Logic:  K ^PS(51.24,"UPCASE",\$E(X,1,30),DA)

                   Whole Kill:  K ^PS(51.24,"UPCASE")

                         X(1):  NAME  (51.24,.01)  (Subscr 1)  (Len 30)

                                (forwards)                                

For the First Databank Dose Unit (#1) field:

The INPUT TRANSFORM should be rolled back as shown below.

The HELP-PROMPT should be rolled back to state 1-30 characters in length.

The FIELD INDEX no longer includes an entry for FDBUNIT.

51.24,1       FIRST DATABANK DOSE UNIT 0;2 FREE TEXT

              INPUT TRANSFORM:  K:\$L(X)\>30!(\$L(X)\<1)!(\$E(X,1)=" ")!(\$E(X,\$L(X))

                                =" ")!(X\["  ")!(X'?.ANP) X

              LAST EDITED:      JAN 26, 2008

              HELP-PROMPT:      Answer must be 1-30 characters in length,

                                comprised of upper and lower case letters,

                                numerics, and punctuation, and contain no

                                leading, trailing, or consecutive spaces.

              DESCRIPTION:      This field provides the mapping from the Vista

                                Dose Unit to the First DataBank Dose Unit. The

                                First DataBank Dose Unit will be used when

                                processing the dosage checks provided by First

                                DataBank. 

              WRITE AUTHORITY:  ^

              NOTES:            XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

              CROSS-REFERENCE:  51.24^C

                                1)= S ^PS(51.24,"C",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.24,"C",\$E(X,1,30),DA)

                                This cross reference is a regular cross

                                reference on the FIRST DATABANK DOSE UNIT

                                field. It sets the global: PS(51.24,"C",FIRST

                                DATABANK DOSE UNIT, Internal Entry Number)="". 

For the Synonym (#.01) field of the Synonym (#2) multiple:

The INPUT TRANSFORM should be rolled back as shown below.

The HELP-PROMPT should be rolled back to state 1-30 characters in length.

The FIELD INDEX no longer includes an entry for FDBSYN.

51.24,2       SYNONYM                1;0 Multiple \#51.242

              WRITE AUTHORITY:  ^

51.242,.01      SYNONYM                0;1 FREE TEXT (Multiply asked)

                INPUT TRANSFORM:K:\$L(X)\>30!(\$L(X)\<1)!(\$E(X,1)=" ")!(\$E(X,\$L(X))

                                =" ")!(X\["  ")!(X'?.ANP) X

                LAST EDITED:    MAR 31, 2008

                HELP-PROMPT:    Answer must be 1-30 characters in length,

                                comprised of upper and lower case letters,

                                numerics, and punctuation, and contain no

                                leading, trailing, or consecutive spaces.

                DESCRIPTION:    This is a synonym for the NAME field, which is

                                the name of the DOSE UNIT. 

                WRITE AUTHORITY:^

                NOTES:          XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

                CROSS-REFERENCE:51.242^B

                                1)= S ^PS(51.24,DA(1),1,"B",\$E(X,1,30),DA)=""

                                2)= K ^PS(51.24,DA(1),1,"B",\$E(X,1,30),DA)

                CROSS-REFERENCE:51.24^D

                                1)= S ^PS(51.24,"D",\$E(X,1,30),DA(1),DA)=""

                                2)= K ^PS(51.24,"D",\$E(X,1,30),DA(1),DA)

                                This is a whole file cross reference on the

                                SYNONYM (#.01) Field of the SYNONYM (#51.242)

                                Subfile. It sets the global

                                PS(51.24,"D",SYNONYM,DA(1),DA)="".

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSS*1*262 Deployment, Installation, Back-Out, and Rollback Guide

## POST-INSTALL MOCHA PGx Clinical Reminder Order Check (CROC) Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This step should be executed by the Clinical Application Coordinator (CAC). Install the MOCHA PGx clinical reminder order check update following the instructions in the attached MOCHA PGx CROC Update document.

- ![](pss-1-262-deployment-installation-back-out-and-rollback-guide/002.png)

### Routine (Code) Installation Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the routine checksums (for the individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and for the multi-build which consists of patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) match the checksum in the patch descriptions. The checksums should have been captured as part of the patch installation step "Verify Checksums in Transport Global". If checksums were not captured, they may be verified by running the option Calculate and Show Checksum Values \[XTSUMBLD-CHECK\] for each patch, (PSN\*5.0\*576, PSS\*1.0\*262, PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626).

> <u>Example:</u>

> Use the following VistA option:

> CALculate and Show Checksum Values

> This option determines the current Old (CHECK^XTSUMBLD) or New (CHECK1^XTSUMBLD)

> logic checksum of selected routine(s).

> Select one of the following:

> 1 Old

> 2 New

> New or Old Checksums: New//

> New CheckSum

> This option determines the current checksum of selected routine(s).

> The Checksum of the routine is determined as follows:

> 1\. Any comment line with a single semi-colon is presumed to be

> followed by comments and only the line tag will be included.

> 2\. Line 2 will be excluded from the count.

> 3\. The total value of the routine is determined (excluding

> exceptions noted above) by multiplying the ASCII value of each

> character by its position on the line and position of the line in

> the routine being checked.

> Select one of the following:

> P Package

> B Build

> Build from: Build

> This will check the routines from a BUILD file.

> Select BUILD NAME: PSN\*4.0\*576<sup>1</sup>

<sup>1</sup>NOTE: To verify all routine checksums, this must be run FIVE times, once for each BUILD NAME that is a part of the combined build, and the two stand-alone patches:

- PSN\*4.0\*576
- PSS\*1.0\*262
- PSJ\*5.0\*447
- PSO\*7.0\*737
- OR\*3.0\*626

### Data Definition Installation Verification 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Fileman to confirm the following partial data dictionary updates were installed by PSN\*4.0\*576:

- PGX ELIGIBLE (#46) field in the VA PRODUCT (#50.68) file
- PGX SUPPRESSED (#47) field in the VA PRODUCT (#50.68) file
1.  From Fileman, select the DATA DICTIONARY UTILITY menu.
2.  Select the LIST FILE ATTRIBUTES option.
3.  Select the VA PRODUCT (#50.68) file at the prompt 'START WITH What File'.
4.  Accept the default (VA PRODUCT) at the prompt 'GO TO What File'.
5.  Accept the default (STANDARD).
6.  Enter "46" at the prompt 'Start with field:'.
7.  Enter "47" at the prompt 'Go to field:'.
8.  Accept the blank default at the 'DEVICE:' prompt to print to the screen.
9.  Accept the default at the 'Right Margin:' prompt.
10. The output should display the new fields installed by PSN\*4.0\*576:

START WITH What File: 50.68 VA PRODUCT

(34014 entries)

GO TO What File: VA PRODUCT// (34014 entries)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD//

Start with field: FIRST// PGX ELIGIBLE

Go to field: PGX SUPPRESSED

DEVICE: Linux Telnet /SSh

STANDARD DATA DICTIONARY \#50.68 -- VA PRODUCT FILE XX/XX/25 PAGE 1

STORED IN ^PSNDF(50.68, (34014 ENTRIES) SITE: XXXX ISC ACCOUNT UCI:XXXX,XXX (VERSION 4.0)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

50.68,46 PGX ELIGIBLE PGX;1 SET (Required) (audited)

'1' FOR YES;

'0' FOR NO;

LAST EDITED: APR 18, 2025

HELP-PROMPT: Enter 'Yes' if you want medication orders for

drugs matched to this VA Product to participate

in Pharmacogenomic (PGx) order checks.

DESCRIPTION: If this field is set to Yes, then any

medication order for a drug matched to this VA

Product will participate in Pharmacogenomic

(PGx) order checks.

TECHNICAL DESCR: This field is set at the national level and is

not locally editable.

AUDIT: YES, ALWAYS

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

CROSS-REFERENCE: 50.68^APGX^MUMPS

1)= I \$G(X) S ^PSNDF(50.68,"APGX",DA)=""

2)= K ^PSNDF(50.68,"APGX",DA)

This cross reference identifies VA Products

eligible for pharmacogenomic order checking.

50.68,47 PGX SUPPRESSED PGX;2 SET (Required) (audited)

'1' FOR YES;

'0' FOR NO;

LAST EDITED: MAR 09, 2024

HELP-PROMPT: Enter 'Yes' if you want medication orders for

profile drugs matched to this VA Product to

participate in suppression rules for PGx order

checks.

DESCRIPTION: If this field is set to Yes, then any profile

medication order for a drug matched to this VA

Product will participate in the suppression

rules for Pharmacogenomic (PGx) order checks.

TECHNICAL DESCR: This field is set at the national level and is

not locally editable.

AUDIT: YES, ALWAYS

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

Use Fileman to confirm the following partial data dictionary updates were installed by PSN\*4.0\*576:

- PGX ELIGIBLE (#5) field in the DRUG INGREDIENTS (#50.416) file
- PGX SUPPRESSED (#6) field in the DRUG INGREDIENTS (#50.416) file
11. From Fileman, select the DATA DICTIONARY UTILITY menu.
12. Select the LIST FILE ATTRIBUTES option.
13. Select the DRUG INGREDIENTS (#50.416) file at the prompt 'START WITH What File'.
14. Accept the default (DRUG INGREDENTS) at the prompt 'GO TO What File'.
15. Accept the default (STANDARD).
16. Enter "5" at the prompt 'Start with field:'.
17. Enter "6" at the prompt 'Go to field:'.
18. Accept the blank default at the 'DEVICE:' prompt to print to the screen.
19. Accept the default at the 'Right Margin:' prompt.
20. The output should display the new fields installed by PSN\*4.0\*476:

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH What File: VA PRODUCT// 50.416 DRUG INGREDIENTS

(5713 entries)

GO TO What File: DRUG INGREDIENTS// (5713 entries)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD//

Start with field: FIRST// PGX ELIGIBLE

Go to field: PGX SUPPRESSED

DEVICE: Linux Telnet /SSh

STANDARD DATA DICTIONARY \#50.416 -- DRUG INGREDIENTS FILE XX/XX/25 PAGE 1

STORED IN ^PS(50.416, (5713 ENTRIES) SITE: XXXX ISC ACCOUNT UCI: XXXX,XXX (VERSION 4.0)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

50.416,5 PGX ELIGIBLE PGX;1 SET (Required) (audited)

'1' FOR YES;

'0' FOR NO;

LAST EDITED: MAR 10, 2024

HELP-PROMPT: Enter 'Yes' if you want medication orders for

drugs containing this ingredient to participate

in PGx order checks.

DESCRIPTION: If this field is set to Yes, then any

medication order for a drug containing this

ingredient will participate in Pharmacogenomic

(PGx) order checks.

TECHNICAL DESCR: This field is set at the national level and not

locally editable.

AUDIT: YES, ALWAYS

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

50.416,6 PGX SUPPRESSED PGX;2 SET (Required) (audited)

'1' FOR YES;

'0' FOR NO;

LAST EDITED: MAR 10, 2024

HELP-PROMPT: Enter 'Yes' if you want medication orders for

profile drugs containing this ingredient to

participate in suppression rules for PGx order

checks.

DESCRIPTION: If this field is set to Yes, then any profile

medication order containing this ingredient

will participate in the suppression rules for

Pharmacogenomic (PGx) order checks.

TECHNICAL DESCR: This field is set at the national level and not

locally editable.

AUDIT: YES, ALWAYS

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

### Data Definition Installation Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use Fileman to confirm the following new files were installed by PSS\*1.0\*262:

- PHARMACOGENOMIC GENES (#51.26)
- PHARMACOGENOMIC PHENOTYPES (#51.28)
- PHARMACOGENOMIC EMAIL LOG (#51.29)

1\. From Fileman, select the DATA DICTIONARY UTILITY menu.

2\. Select the LIST FILE ATTRIBUTES option.

3\. Select a file number from the list above

4\. Verify that the file displays as selectable<sup>2</sup>

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH What File: DRUG INGREDIENTS// 51.26 PHARMACOGENOMIC GENES

(19 entries)

GO TO What File: PHARMACOGENOMIC GENES//

<sup>2</sup>NOTE: In order to verify all new files were installed, this must be run THREE TIMES, once for each file number (51.26, 51.28, and 51.29)

Use Fileman to confirm the partial data dictionary update in the PHARMACY SYSTEM (#59.7) file of the new VA PHARMACOGENOMICS URL (#103) field was applied properly by PSS\*1.0\*262:

1.  From Fileman, select the DATA DICTIONARY UTILITY menu.
2.  Select the LIST FILE ATTRIBUTES option.
3.  Select the PHARMACY SYSTEM (#59.7) file at the prompt 'START WITH What File'.
4.  Accept the default (PHARMACY SYSTEM) at the prompt 'GO TO What File'.
5.  Accept the default (STANDARD).
6.  Enter "103" at the prompt 'Start with field:'.
7.  Enter "103" at the prompt 'Go to field:'.
8.  Accept the blank default at the 'DEVICE:' prompt to print to the screen.
9.  Accept the default at the 'Right Margin:' prompt.
10. The output should display the new field installed by PSS\*1.0\*262:

Select OPTION: DATA DICTIONARY UTILITIES

Select DATA DICTIONARY UTILITY OPTION: LIST FILE ATTRIBUTES

START WITH What File: 59.7 PHARMACY SYSTEM

(1 entry)

GO TO What File: PHARMACY SYSTEM// (1 entry)

Select SUB-FILE:

Select LISTING FORMAT: STANDARD//

Start with field: FIRST// 103 VA PHARMACOGENOMICS URL

Go to field: 103 VA PHARMACOGENOMICS URL

DEVICE: Linux Telnet /SSh

STANDARD DATA DICTIONARY \#59.7 -- PHARMACY SYSTEM FILE XX/XX/25 PAGE 1

STORED IN ^PS(59.7, (1 ENTRY) SITE: XXXX ISC SUPPORT ACCOUNT UCI: XXXX,XXX

(VERSION 1.0)

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

59.7,103 VA PHARMACOGENOMICS URL PGX;1 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>100!(\$L(X)\<1) X

MAXIMUM LENGTH: 100

LAST EDITED: OCT 27, 2024

HELP-PROMPT: Enter the URL for the VA National

Pharmacogenomics Program (1 to 100 characters).

DESCRIPTION: This is the Uniform Resource Locator (URL) for

the VA National Pharmacogenomics program. This

URL will be used for display when the URL

normally received from the Health Data

Repository (HDR) is not available.

DELETE AUTHORITY: ^

WRITE AUTHORITY: ^

### Back-Out Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The combined build for MOCHA 3.0 PGx Order Checks (consisting of individual patches PSN\*4.0\*576 and PSS\*1.0\*262 and a multi-build including patches PSJ\*5.0\*447, PSO\*7.0\*737, and OR\*3.0\*626) contains the following build components:

- Routines
- Data Dictionary (new files)
- Partial Data Dictionary (new fields)

Please log a ServiceNow ticket for assistance in backing out this patch since these installed patches contain components in addition to routines.

If a decision to back out is made during Mirror Testing or Site Production Testing, the routine backup created prior to installation may be used to restore components to their pre-patch condition.

Example: Combined build restoration from backupsMULTI-BUILD restoration from backup:Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: installation

Select Installation \<TEST ACCOUNT\> Option: 1 Load a Distribution

Enter a Host File: /srv/vista/xxx/user/hfs/xxxxx/MOCHA_3_0_PGX_COMBINED_BUILD_1_0b.KID

KIDS Distribution saved on Mar 25, 2025@11:14:03

Comment: Backup of MOCHA 3.0 PGX COMBINED BUILD 1.0, PSJ\*5.0\*447, PSO\*7.

This Distribution contains Transport Globals for the following Package(s):

MOCHA 3.0 PGX COMBINED BUILD 1.0b

PSJ\*5.0\*447b

PSO\*7.0\*737b

OR\*3.0\*626b

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

MOCHA 3.0 PGX COMBINED BUILD 1.0b

PSJ\*5.0\*447b

PSO\*7.0\*737b

OR\*3.0\*626b

Use INSTALL NAME: MOCHA 3.0 PGX COMBINED BUILD 1.0b to install this Distribution

.

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INStallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: INStall Package(s)

Select INSTALL NAME: MOCHA 3.0 PGX COMBINED BUILD 1.0b.0b 3/25/25@11:14:28

=\> Backup of MOCHA 3.0 PGX COMBINED BUILD 1.0, PSJ\*5.0\*447, PSO\*7. ;Crea

This Distribution was loaded on Mar 25, 2025@11:14:28 with header of

Backup of MOCHA 3.0 PGX COMBINED BUILD 1.0, PSJ\*5.0\*447, PSO\*7. ;Created on

Mar 25, 2025@11:14:03

It consisted of the following Install(s):

MOCHA 3.0 PGX COMBINED BUILD 1.0b PSJ\*5.0\*447b PSO\*7.0\*737b OR\*3.0\*626b

Checking Install for Package MOCHA 3.0 PGX COMBINED BUILD 1.0b

Install Questions for MOCHA 3.0 PGX COMBINED BUILD 1.0b

Checking Install for Package PSJ\*5.0\*447b

Install Questions for PSJ\*5.0\*447b

Checking Install for Package PSO\*7.0\*737b

Install Questions for PSO\*7.0\*737b

Checking Install for Package OR\*3.0\*626b

Install Questions for OR\*3.0\*626b

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// Linux Telnet /SSh

--------------------------------------------------------------------------------

Install Started for MOCHA 3.0 PGX COMBINED BUILD 1.0b :

Mar 25, 2025@11:14:46

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:14:46

Install Started for PSJ\*5.0\*447b :

Mar 25, 2025@11:14:46

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:14:46

Updating Routine file...

Updating KIDS files...

PSJ\*5.0\*447b Installed.

Mar 25, 2025@11:14:46

NO Install Message sent

Install Started for PSO\*7.0\*737b :

Mar 25, 2025@11:14:46

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:14:46

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*737b Installed.

Mar 25, 2025@11:14:46

NO Install Message sent

Install Started for OR\*3.0\*626b :

Mar 25, 2025@11:14:46

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:14:46

Running Post-Install Routine: EN^ORY626RR

Disabling the Pharmacogenomics order checks...

Patch OR\*3\*262 rollback successful!

Updating Routine file...

Updating KIDS files...

OR\*3.0\*626b Installed.

Mar 25, 2025@11:14:46

NO Install Message sent

Updating Routine file...

Updating KIDS files...

MOCHA 3.0 PGX COMBINED BUILD 1.0b Installed.

Mar 25, 2025@11:14:46

No link to PACKAGE file

Install Completed

PSS\*1.0\*262 restoration from backup:

Select backup message from local mail system:

Subj: Backup of PSS\*1.0\*262 on Aug 06, 2025 \[#XXXXXX\] 08/06/25@10:37

8883 lines

From: USER,TEST In 'IN' basket. Page 1

-------------------------------------------------------------------------------

\$TXT Created by USER,TEST at XXXX-XXXX.XXX.XX.XXX (KIDS) on Wednesday, 0

8/06/25 at 10:37

> **WARNING:** Installing this backup patch message will install older versions

of routines and Build Components (options, protocols, templates, etc.).

Please verify with the Development Team that it is safe to install.

\$END TXT

\$KID PSS\*1.0\*262b

\*\*INSTALL NAME\*\*

PSS\*1.0\*262b

"BLD",13206,0)

PSS\*1.0\*262b^PHARMACY DATA MANAGEMENT^0^3250806^n

"BLD",13206,1,0)

^^5^5^3250806

"BLD",13206,1,1,0)

Backup of PSS\*1.0\*262 on Aug 06, 2025

"BLD",13206,1,2,0)

Type \<Enter\> to continue or '^' to exit: ^

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: I

1 INSTALL SELECTED ROUTINE(S)

2 INSTALL/CHECK MESSAGE

CHOOSE 1-2: 2 INSTALL/CHECK MESSAGE

Line 8 Message \#304912 Unloading KIDS Distribution PSS\*1.0\*262b

Build PSS\*1.0\*262b has been loaded before, here is when:

PSS\*1.0\*262b Install Completed

was loaded on Jul 17, 2024@11:38:11

PSS\*1.0\*262b Install Completed

was loaded on Mar 04, 2025@14:20:59

PSS\*1.0\*262b Install Completed

was loaded on Mar 25, 2025@11:15:51

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

PSS\*1.0\*262b

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: Installa

tion

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

Select INSTALL NAME: PSS\*1.0\*262b 8/6/25@10:38:05

=\> Backup of PSS\*1.0\*262 on Aug 06, 2025

This Distribution was loaded on Aug 06, 2025@10:38:05 with header of

Backup of PSS\*1.0\*262 on Aug 06, 2025

It consisted of the following Install(s):

PSS\*1.0\*262b

Checking Install for Package PSS\*1.0\*262b

Install Questions for PSS\*1.0\*262b

Incoming Files:

51.26 PHARMACOGENOMIC GENES

> **NOTE:** You already have the 'PHARMACOGENOMIC GENES' File.

51.28 PHARMACOGENOMIC PHENOTYPES

> **NOTE:** You already have the 'PHARMACOGENOMIC PHENOTYPES' File.

51.29 PHARMACOGENOMIC EMAIL LOG

> **NOTE:** You already have the 'PHARMACOGENOMIC EMAIL LOG' File.

59.7 PHARMACY SYSTEM (Partial Definition)

> **NOTE:** You already have the 'PHARMACY SYSTEM' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;9999 Linux Telnet /SSh

--------------------------------------------------------------------------------

Install Started for PSS\*1.0\*262b :

Aug 06, 2025@10:39:20

Build Distribution Date: Aug 06, 2025

Installing Routines:

Aug 06, 2025@10:39:20

Installing Data Dictionaries: .

Aug 06, 2025@10:39:20

Installing PACKAGE COMPONENTS:

Installing OPTION

Aug 06, 2025@10:39:20

Running Post-Install Routine: EN^PSS262RR

Removing the HDR server and HDR web service for MOCHA PGx

PSS PGX-HDR SERVER web server successfully removed.

PSS PGX-HDR SERVICE web service successfully removed.

Adding the new intervention type entries to the APSP INTERVENTION TYPE

(#9009032.3) file:

\- PHARMACOGENOMIC HIGH ORDER CHECK intervention type already exists.

\- PHARMACOGENOMIC MEDIUM ORDER CHECK intervention type already exists.

Deleting VA PHARMACOGENOMICS URL (#103) field from PHARMACY SYSTEM (#59.7) File

Field \#103 deleted from the PHARMACY SYSTEM (#59.7) File

Deleting files 51.26, 51.28, and 51.29

PHARMACOGENOMIC GENES (#51.26) File successfully deleted.

PHARMACOGENOMIC PHENOTYPES (#51.28) File successfully deleted.

PHARMACOGENOMIC EMAIL LOG (#51.29) File successfully deleted.

Restructuring the PSS menus:

PSS CHECK DRUG INTERACTION removed from PSS ORDER CHECK MANAGEMENT....

PSS CHECK DRUG INTERACTION added to the PSS MGR option.

Web Service removal is complete for PSS PGX-HDR SERVICE

APSP intervention type update is complete

Updating Routine file...

Updating KIDS files...

PSS\*1.0\*262b Installed.

Aug 06, 2025@10:39:21

Install Completed

PSN\*4.0\*576 restoration from backup:

Select backup message from local mail system:

Subj: Backup of PSN\*4.0\*576 on Mar 25, 2025 \[#XXXXXX\] 03/25/25@11:11 1739 lines

From: LAST,FIRST In 'IN' basket. Page 1

-------------------------------------------------------------------------------

\$TXT Created by LAST,FIRST at XXXX.FO-BIRM.MED.VA.GOV (KIDS) on Tuesday,

03/25/25 at 11:11

> **WARNING:** Installing this backup patch message will install older versions

of routines and Build Components (options, protocols, templates, etc.).

Please verify with the Development Team that it is safe to install.

\$END TXT

\$KID PSN\*4.0\*576b

\*\*INSTALL NAME\*\*

PSN\*4.0\*576b

"BLD",13189,0)

PSN\*4.0\*576b^NATIONAL DRUG FILE^0^3250325^n

"BLD",13189,1,0)

^^5^5^3250325

"BLD",13189,1,1,0)

Backup of PSN\*4.0\*576 on Mar 25, 2025

"BLD",13189,1,2,0)

"BLD",13189,1,3,0)

Type \<Enter\> to continue or '^' to exit: ^

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

Line 8 Message \#XXXXX Unloading KIDS Distribution PSN\*4.0\*576b

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

PSN\*4.0\*576b

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INStallation

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: INStall Package(s)

Select INSTALL NAME: PSN\*4.0\*576b 3/25/25@11:15:24

=\> Backup of PSN\*4.0\*576 on Mar 25, 2025

This Distribution was loaded on Mar 25, 2025@11:15:24 with header of

Backup of PSN\*4.0\*576 on Mar 25, 2025

It consisted of the following Install(s):

PSN\*4.0\*576b

Checking Install for Package PSN\*4.0\*576b

Install Questions for PSN\*4.0\*576b

Incoming Files:

50.416 DRUG INGREDIENTS (Partial Definition)

> **NOTE:** You already have the 'DRUG INGREDIENTS' File.

50.68 VA PRODUCT (Partial Definition)

> **NOTE:** You already have the 'VA PRODUCT' File.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// Linux Telnet /SSh

--------------------------------------------------------------------------------

Install Started for PSN\*4.0\*576b :

Mar 25, 2025@11:16:11

Build Distribution Date: Mar 25, 2025

Installing Routines:

Mar 25, 2025@11:16:11

Running Post-Install Routine: EN^PSN576RR

Deleting PGx data from the DRUG INGREDIENT (#50.416) File...

Deleting PGx fields from the DRUG INGREDIENT (#50.416) File

PGX ELIGIBLE (#5) Field successfully deleted.

PGX SUPPRESSED (#6) Field successfully deleted.

Deleting PGx data from the VA PRODUCT (#50.68) File

Deleting PGx fields from the VA PRODUCT (#50.68) File

PGX ELIGIBLE (#46) Field successfully deleted.

PGX SUPPRESSED (#47) Field successfully deleted.

Updating Routine file...

Updating KIDS files...

PSN\*4.0\*576b Installed.

Mar 25, 2025@11:16:11

Install Completed

### From: PSS*1*211 Deployment, Installation, Back-Out, and Rollback Guide

### Pre/Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system, although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than five minutes to install.

A patch backup should be created prior to installing PSS\*1.0\*211 to save routines that are modified by the patch. Backing out the patches new software components must be done by installing 'back-out' KIDS build PSS\*1.0\*00211, created specifically to back-out changes installed by PSS\*1.0\*211. Please refer to <u>Section 5</u> Back-Out Procedure of this guide for details of the back-out procedure.

### Patch Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches PSS\*1.0\*48 and HDI\*1.0\*21 must be installed prior to installing this patch. Patch HDI\*1.0\*21 and patch XU\*8.0\*686 will be nationally released at the same time as patch PSS\*1.0\*211.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx).

Patch HDI\*1.0\*21 and patch XU\*8.0\*686 will be nationally released on or before PSS\*1.0\*211 patch is released. The order of install is XU\*8.0\*686, HDI\*1.0\*21, then PSS\*1.0\*211.

The XU and HDI patches are in support of the Standards and Terminology Services (STS) deployment methodology.

### Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific pre-installation instructions related to patch PSS\*1.0\*211.

### Preferred Back-Out Method:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Load KIDS build PSS\*1.0\*00211:
    1.  Find and select Mailman message containing PSS\*1.0\*00211.
    2.  Extract and Load PackMan Message from the 'Enter message action' prompt:

Figure . Example, extract and load PackMan message PSS\*1.0\*00211

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

Line 3 Message \#198245 Unloading KIDS Distribution PSS\*1.0\*00211

OK to continue with Load? NO// YES

Want to Continue with Load? YES//

Loading Distribution...

PSS\*1.0\*00211

1.  From the Install Package(s) option in the Installation menu in the Kernel Installation and Distribution System \[XPD MAIN\] menu, install PSS\*1.0\*00211.

Figure . Example, installation PSS\*1.0\*00211 KIDS build

Select Kernel Installation & Distribution System \<TEST ACCOUNT\> Option: INSTallation

Select Installation \<TEST ACCOUNT\> Option: INSTall Package(s)

Select INSTALL NAME: PSS\*1.0\*00211 7/5/17@12:18:03

=\> PSS\*1.0\*00211 v1 Back-Out PSS\*1\*211

This Distribution was loaded on Jul 05, 2017@12:18:03 with header of

PSS\*1.0\*00211 v1 Back-Out PSS\*1\*211

It consisted of the following Install(s):

PSS\*1.0\*00211

Checking Install for Package PSS\*1.0\*00211

Install Questions for PSS\*1.0\*00211

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

DEVICE: HOME// HOME SSH VIRTUAL TERMINAL

PSS\*1.0\*00211



Installing Routines:

Jul 05, 2017@12:22

Running Post-Install Routine: ASKBO^PSS211BO

Completely back out patch PSS\*1.0\*211? N// YES

Deleting Data from field 90 in file 50.606

Deleting Field MASTER DOSAGE FORM(#90) in File 50.606

Deleting Data from file 50.60699

Deleting Field \#.01 in File 50.60699

Deleting routine ^PSS211PO

Deleting routine ^PSSNDSU

Updating Routine file...

Updating KIDS files...

PSS\*1.0\*00211 Installed.

Jul 05, 2017@12:22

<span class="mark">100% x 25 50 75</span>

Complete

Install Completed

1b) Restore the backup patch Transport Global created during the installation (Section <u>4.8</u>).

3.  Find and select Mailman message Transport Global backup of PSS\*1.0\*211.
4.  Extract and Load PackMan Message from the 'Enter message action' prompt:

Figure . Example, extract and load Transport Global backup of PSS\*1.0\*211:

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

> **WARNING:** Installing this message will cause a permanent update of globals

and routines.

Do you really want to do this? NO// YES

Routines are the only parts that are backed up. NO other parts

are backed up, not even globals. You may use the 'Summarize Message'option of PackMan to see what parts the message contains.

Those parts that are not routines should be backed up separately if they need to be preserved.

Shall I preserve the routines on disk in a separate back-up message? YES// NO

No backup message built.

Line 2 Message \#1151616 Unloading Routine PSOMLLD2 (PACKMAN_BACKUP)

Line 87 Message \#1151616 Unloading Routine PSONEW2 (PACKMAN_BACKUP)

Line 225 Message \#1151616 Unloading Routine PSORN52 (PACKMAN_BACKUP)

Select PackMan function:

### Alternate (Manual) Back-Out Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following involves manual deletion of Data Dictionaries (DD's) and routines, and will need to be executed from the programmers prompt. This procedure must be performed by persons with programmer-level access and in conjunction with the STS Team.

<u>Disclaimer</u>: Use of the alternate method is not recommended and should only be done by upper level programmers.

#### Manual deletion of Data Dictionaries

Manually delete the MASTER DOSAGE FORM file (#50.60699), and delete the MASTER DOSAGE FORM field (#90) from the DOSAGE FORM file (#50.606).

Use File Manager to delete the new fields added with PSS\*1.0\*211.

Delete the MASTER DOSAGE FORM field (#90) from the DOSAGE FORM (#50.606) file:

1.  Select FileMan option MODIFY FILE ATTRIBUTES.
2.  At the Select FIELD prompt, enter 'MASTER DOSAGE FORM'
3.  At the 'LABEL' prompt, enter "@".
4.  At the prompt "SURE YOU WANT TO DELETE THE ENTIRE 'MASTER DOSAGE FORM' FIELD?" enter YES.
5.  At the prompt "OK TO DELETE 'MASTER DOSAGE FORM' FIELDS IN THE EXISTING ENTRIES?" enter YES.

Figure . Example, manual deletion of MASTER DOSAGE FORM field (#90) from DOSAGE FORM file (#50.606):

VA FileMan 22.2

Select OPTION: MODIFY FILE ATTRIBUTES

Modify what File: DOSAGE FORM// (63 entries)

Select FIELD: MASTER DOSAGE FORM

LABEL: MASTER DOSAGE FORM// @

SURE YOU WANT TO DELETE THE ENTIRE 'MASTER DOSAGE FORM' FIELD? Y (Yes)

OK TO DELETE 'MASTER DOSAGE FORM' FIELDS IN THE EXISTING ENTRIES? Yes// Y

Delete the MASTER DOSAGE FORM file (#50.60699):

1.  Select FileMan option UTILITY FUNCTIONS.
2.  At the UTILITY OPTION prompt, select EDIT FILE.
3.  At the 'Modify what File' prompt, enter MASTER DOSAGE FORM.
4.  At the "NAME" prompt, enter "@".
5.  At the prompt "DO YOU WANT JUST TO DELETE THE \<nn\> FILE ENTRES & KEEP THE FILE DEFINITION?", enter NO.
6.  At the prompt, "IS IT OK TO DELETE THE '^PSMDF(50.60699' GLOBAL?", enter YES.
7.  At the prompt, "SURE YOU WANT TO DELETE THE ENTIRE 'MASTER DOSAGE FORM' FILE?", enter YES.

Figure . Example: Manual Deletion of MASTER DOSAGE FORM file (#50.60699)

VA FileMan 22.2

Select OPTION: UTILITY FUNCTIONS

Select UTILITY OPTION: EDIT FILE

Modify what File: MASTER DOSAGE FORM// (15 entries)

Do you want to use the screen-mode version? YES// NO

NAME: MASTER DOSAGE FORM// @

POINTED TO BY: PARENT field (#2) of the MASTER DOSAGE FORM File (#50.60699)

REPLACED BY VHA STANDARD TERM field (#99.97) of the MASTER TYPE

OF PLAN File (#50.60699)

DO YOU WANT JUST TO DELETE THE 15 FILE ENTRIES,

& KEEP THE FILE DEFINITION? No// (No)

IS IT OK TO DELETE THE '^PSMDF(50.60699)' GLOBAL? Yes// Y (Yes)

SURE YOU WANT TO DELETE THE ENTIRE 'MASTER DOSAGE FORM' FILE? Y (Yes)

Deleting the DATA DICTIONARY...

Deleting the INPUT TEMPLATES...

Deleting the PRINT TEMPLATES...

Deleting the SORT TEMPLATES...

Deleting the FORMS...

Deleting the BLOCKS...

1)  <u>Manual deletion of Routines PSSNDSU and PSS211PO.</u>

The deletion of a routine is a potentially dangerous activity. This procedure must be performed by persons with programmer-level access; and in conjunction with the STS Team.

1.  From the ROUTINE MANAGEMENT MENU \[XUROUTINES\], select the DELETE ROUTINES \[XTRDEL\] option. IMPORTANT: When prompted for 'All Routines?', enter NO.
2.  At the 'Routine:' prompt, enter PSS211PO.
3.  At the next 'Routine:' prompt, enter PSSNDSU.
4.  At the next 'Routine:' prompt, press \<Enter\>.
5.  At the prompt '3 routines to DELETE, OK:'. enter YES.

Figure . Example, manual deletion of routines PSS211PO, PSSNDSU using option DELETE ROUTINES \[XTRDEL\]

Select OPTION NAME: ROUTINE MANAGEMENT MENU XUROUTINES Routine Management Menu

Bring in Sent Routines

Delete Routines

First Line Routine Print

List Routines

Move Routines across Volume Sets

Select OPTION NAME: DELETE ROUTINES XTRDEL Delete Routines

Delete Routines

ROUTINE DELETE

All Routines? No =\> No

Routine: PSS211PO

Routine: PSSNDSU

Routine:

2 routine

2 routines to DELETE, OK: NO// Y

PSS211PO

PSSNDSU

Done.

2)  <u>Restore of Transport Global backup of PSS\*1.0\*211.</u>

Restore the backup patch Transport Global created during the <u>Section 4.8</u>. Installation Procedure.

1)  Find and select Mailman message Transport Global backup of PSS\*1.0\*211.
2)  Extract and Load PackMan Message from the 'Enter message action' prompt.

Figure . Example, extract and load Transport Global backup of PSS\*1.0\*211:

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

> **WARNING:** Installing this message will cause a permanent update of globals

and routines.

Do you really want to do this? NO// YES

Routines are the only parts that are backed up. NO other parts are backed up, not even globals. You may use the 'Summarize Message'option of PackMan to see what parts the message contains. Those parts that are not routines should be backed up separately if they need to be preserved.

Shall I preserve the routines on disk in a separate back-up message? YES// NO

No backup message built.

Line 2 Message \#1151616 Unloading Routine PSOMLLD2 (PACKMAN_BACKUP)

Line 87 Message \#1151616 Unloading Routine PSONEW2 (PACKMAN_BACKUP)

Line 225 Message \#1151616 Unloading Routine PSORN52 (PACKMAN_BACKUP)

Select PackMan function:

### Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful back-out of the routines installed by the patch may be verified by running the CHECK1^XTSUMBLD utility from the programmer prompt for PSS\*1.0\*211. If the back-out was successful, the message "Routine not in this UCI" will display next to each new routine, and routine PSSNOUNR checksum should be the pre-PSS\*1\*211 checksum value: B13687213.

Figure . Example, CHECK1^XTSUMBLD of routines installed by patch PSS\*1.0\*211

D CHECK1^XTSUMBLD

New CheckSum CHECK1^XTSUMBLD:

This option determines the current checksum of selected routine(s).

Select one of the following:

P Package

B Build

Build from: Build

This will check the routines from a BUILD file.

Select BUILD NAME: PSS\*1.0\*211 PHARMACY DATA MANAGEMENT

PSS211PO Routine not in this UCI.

PSSNOUNR value = B13687213

PSSNDSU Routine not in this UCI.

done

### Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful back-out of the fields and file installed by the patch may be verified by running a global listing from the VistA server command line after installation.

The verification of successful data dictionary back-out consists of verifying the MASTER DOSAGE FORM field (#90) in the DOSAGE FORM file (#50.606) was successfully deleted and no longer exists.

Figure . Example, global listing of backed out MASTER DOSAGE FORM field (#90) in the DOSAGE FORM file (#50.606)

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global ^DD(50.606,90

\<nothing should print\>

Figure . Example, global listing after backing out MASTER DOSAGE FORM file (#50.60699)

D ^%G

Device:

Right Margin:

Screen size for paging (0=nopaging)? =\>

Global ^DD(50.60699,

\<nothing should print\>

### From: PSS*1*234 Deployment, Installation, Back-Out, and Rollback Guide

### Test Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following test sites are participating in the testing of the National Drug File v4.0 patch PSN \*1.0\*234 software:

| Site                           |
|------------------------------------|
| <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> |

Test Sites
