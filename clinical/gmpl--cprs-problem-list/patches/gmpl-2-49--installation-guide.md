---
title: GMPL*2*49 and OR*3*429 Problem Selection List Enhancements Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: and OR*3*429 Problem Selection List Enhancements
app_code: GMPL
app_name: "CPRS: Problem List"
section: CLI
app_status: active
pkg_ns: GMPL
patch_ver: 2
patch_id: GMPL*2*49
group_key: "GMPL:GMPL:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - selection
  - table
  - contents
  - problem
  - installation
  - back
  - gmpl
  - rollback
  - enhancements
  - deployment
page_count: 0
word_count: 5154
section_count: 30
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 2017-12-04
revision_count: 2
revision_newest: 2017-12-04
revision_oldest: 2017-07-05
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Problem_List/gmpl_2_0_49_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Problem_List/gmpl_2_0_49_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=64"
---

Problem Selection List Enhancements(Patches OR\*3.0\*429 and GMPL\*2.0\*49)

Deployment, Installation, Back-Out, and Rollback Guide

![](gmpl-2-49-and-or-3-429-problem-selection-list-enhancements-deployment-installati/001.png)

December 2017

Office of Information and Technology (OI&T)

Enterprise Program Management Office (EPMO)

Revision History

| Date   | Version | Description      | Author                         |
|------------|-------------|----------------------|------------------------------------|
| 2017-12-04 | 0.2         | Updates from reviews | <span class="mark">REDACTED</span> |
| 2017-07-05 | 0.1         | Initial Draft        | <span class="mark">REDACTED</span> |

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
    - [Problem Selection List Enhancements Multi-Package Build KIDS Installation](#problem-selection-list-enhancements-multi-package-build-kids-installation)
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
    - [Installing the Back-Out Patch](#installing-the-back-out-patch)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Example Installation](#example-installation)
This document describes how to deploy and install Problem Selection List Enhancements (Patches OR\*3.0\*429 and GMPL\*2.0\*49)*,* as well as how to back-out the product and rollback to a previous version.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom Problem Selection List Enhancements will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, a communications plan, and a rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Problem Selection List Enhancements project is for installation on a fully patched VistA system. This utility enables Clinical Application Coordinators (CACs) to create problem selection lists for their system, divisions, locations, clinics, or users to help them quickly assign problems that they frequently use.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Problem Selection List Enhancements will be released as part of a combined multi-package build under PROBLEM SELECTION LIST BUILD 1.0. This combined build consists of the GMPL\*2.0\*49 and OR\*3.0\*429 patches. The patches are expected to be installed on existing VistA platforms.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No single entity is in charge of decision making for deployment, installation, back out and rollback of Problem Selection List Enhancements. Rather, the Critical Decision Point representatives (commonly referred to as the three in the box) under the Veterans In Process (VIP) will meet and approve release from a business perspective.

If an issue with the software arises that would require a national rollback, then the same three in the box members under VIP will coordinate with several groups (including Patient Safety Health Product Support, Information Technology Operations Service (ITOPS), and Site leadership) to decide whether a back out and rollback of the software is necessary. The Facility Chief Information Officer (FCIO) has the final authority to require the patch back out and data rollback and accept the associated risks.

The following table provides Problem Selection List Enhancements project information.

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table style="width:100%;">
<colgroup>
<col style="width: 6%" />
<col style="width: 29%" />
<col style="width: 14%" />
<col style="width: 36%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
<th><strong>Project Phase (See Schedule)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS.</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
<td>After national release.</td>
</tr>
<tr class="even">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS.</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
<td>After national release.</td>
</tr>
<tr class="odd">
<td></td>
<td>Site personnel.</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
<td>After national release.</td>
</tr>
<tr class="even">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
<td>Deployment</td>
<td>Execute deployment</td>
<td>After national release.</td>
</tr>
<tr class="odd">
<td></td>
<td>Site personnel in conjunction with IT support – which may be local or ITOPS. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway</td>
<td>Installation</td>
<td>Plan and schedule installation</td>
<td>After national release.</td>
</tr>
<tr class="even">
<td></td>
<td>N/A – will work under the VistA ATO and security protocols.</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>N/A – no equipment is being added.</td>
<td>Installation</td>
<td>Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>Local support personnel or CACs.</td>
<td>Installations</td>
<td>Coordinate training</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>Facility CIO and IT support – which may be local or regional.</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
<td>After national release.</td>
</tr>
<tr class="even">
<td></td>
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the CPRS Development Team during the compliance period. At the end of the compliance period, support will be transitioned to HPS Clinical Sustainment.</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
<td>After national release.</td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Problem Selection List Enhancements will have a standard release with a 30-day compliance window. This patch will be released as part of a combined multi-package build under PROBLEM SELECTION LIST BUILD 1.0. This combined build consists of the GMPL\*2.0\*49 and OR\*3.0\*429 patches.

There are currently no site-facing on-line meetings or training planned for this deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The provisional timeline calls for the patch to be released sometime in the summer or fall of 2017 with a 30-day compliance period after national release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Problem Selection List Enhancements deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem Selection List Enhancements will be deployed to each VistA instance. That will include local sites as well as regional data processing centers.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capabilities (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, the Problem Selection List Enhancements patches (OR\*3\*429 and GMPL\*2\*49) will be deployed to all VistA systems.

The Production (IOC) Test sites are:

<span class="mark">REDACTED</span>

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problem Selection List Enhancements

- Identify users that will need the new key, GMPL IMPRT UTIL, to perform national/local selection list updates using the import utility: Sites should identify the users who will need the new GMPL IMPRT UTIL key to perform the national/local selection list updates using the import utility. Most likely, this will be the sites’ CACs. Once the users have been identified, the list of names should be communicated to the Region (ITOPS) personnel. The installer will most likely also make the key assignments post-installation.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

The Problem Selection List Enhancements patches will be deployed using the normal patch deployment process. After the patches are nationally released, sites will have 30 days to install them.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel, local or ITOPS, once the patches are nationally released.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation of the combined build, several things will occur. This information is to aid those installing the combined build containing the two patches. Step-by-step instructions are further below.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Problem Selection List Enhancements patches assume a fully-patched VistA system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please check your system to verify that the following, previously released national patches are installed:

- GMPL\*2.0\*40
- GMPL\*2.0\*45
- OR\*3.0\*385

This multi-package build (VistA KIDS Build) should take less than 5 minutes to install.

It is recommended that the installation be done during non-peak hours. If at all possible, the users should not be in the Problem List ListManager application when the KIDS installation is being performed.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Problem Selection List Enhancements patches are being released in a host file called PROBLEM_SELECTION_LIST_BUILD_1_0.KID. This combined build consists of the GMPL\*2.0\*49 and OR\*3.0\*429 patches.

The preferred method is to retrieve files from download.vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI&T Field Offices:

Hines: <span class="mark">REDACTED</span>

Salt Lake City: <span class="mark">REDACTED</span>

Documentation can also be found on the VA Software Documentation Library at:

<http://www.va.gov/vdl/>

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 29%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th>Problem Selection List Enhancements files to be downloaded</th>
<th>File Contents</th>
<th>Download Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PROBLEM_SELECTION_LIST_BUILD_1_0.KID</td>
<td><ul>
<li><p><strong>OR*3*429</strong>: Contains the new parameter to assign the problem selection list and list migration code</p></li>
<li><p><strong>GMPL*2*49:</strong> Content changes for the problem selection list, including the distribution of the new VA National Problem Selection List</p></li>
</ul></td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>cprsguitm.doc and cprsguitm.pdf</td>
<td><em>CPRS Technical Manual: GUI Version</em></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>cprsguium.doc and cprsguium.pdf</td>
<td><blockquote>
<p><em>CPRS User Guide: GUI Version</em></p>
</blockquote></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>gmpl_2_0_49_ig.docx and gmpl_2_0_49_ig.pdf</td>
<td><blockquote>
<p><em>Problem Selection List Enhancements</em></p>
<p><em>(Patches OR*3.0*429 and GMPL*2.0*49)</em></p>
<p><em>Deployment, Installation, Back-Out, and Rollback Guide</em></p>
</blockquote></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>gmpl_2_0_49_rn.docx and gmpl_2_0_49_rn.pdf</td>
<td><blockquote>
<p><em>Problem Selection List Enhancements (Patches GMPL*2.0*49 and OR*3.0*429)</em></p>
<p><em>Release Notes</em></p>
</blockquote></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>gmpl_2_0_49_tm.doc and gmpl_2_0_49_tm.pdf</td>
<td><blockquote>
<p><em>Problem List Technical Manual</em></p>
</blockquote></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>gmpl_2_0_49_um.doc and gmpl_2_0_49_um.pdf</td>
<td><blockquote>
<p><em>Problem List User Manual</em></p>
</blockquote></td>
<td>Binary</td>
</tr>
</tbody>
</table>

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

Installation of the Problem Selection List Enhancements patches requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Problem Selection List Enhancements Multi-Package Build KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Pre/Post Installation Overview

There is a pre and post-installation routine (GMPLY49) included. This routine will be automatically deleted once installation has completed.

The following things will occur before, during, and after patch installation.

GMPL\*2\*49:

Pre-installation:

- Pre-existing USER/CLINIC Selection List Assignment Report: During pre-installation, this report is auto generated to identify Problem Selection Lists assigned to users and clinics prior to the installation of GMPL\*2.0\*49. This report will be sent to the installer and OR CACS mail group via MailMan.

  Sample MailMan Report

Subj: Pre-existing USER/CLINIC Selection List Assignment Report \[#154391\]

08/23/17@08:16 129 lines

From: GMPL\*2.0\*49 INSTALL In 'IN' basket. Page 1

--------------------------------------------------------------------------

> This report was auto generated during installation to identify Problem

> Selection Lists assigned to users and clinics prior to the installation of

> GMPL\*2.0\*49. After installation all users and clinic assignments will be

> migrated to the new Default Selection List Display parameter setting. If

> users and clinics desire to use the National Problem Selection List as

> their default setting then use the Assign/Remove menu option to reassign

those users or clinics listed in the report.

> User Selection List Assignments:

> PROVIDER,ONE USER LIST 1

> PROVIDER,TWO USER LIST 2

> PROVIDER,THREE USER LIST 3

> PROVIDER,FOUR USER LIST 4

> Clinic Selection List Assignments:

> CARDIOLOGY CARDIO CLINIC LIST

> GENERAL MEDICINE GENERAL MED CLINIC LIST

> PAIN CLINIC PAIN CLINIC LIST

> PRIMARY CARE PRIMARY CARE CLINIC LIST

> User(s) assigned to a Selection List that no longer exists:

> PROVIDER,FIVE Selection List \#5

> PROVIDER,SIX Selection List \#6

- Scan and convert any mixed/lower case list/category names to upper case: During the pre-install, this patch also scans the PROBLEM SELECTION LIST and PROBLEM SELECTION CATEGORY files for any duplicate names or names in mixed/lower case format. A report of finding will be generated to the installer and OR CACS mail group via MailMan and any mixed/lower case names will automatically be converted to upper case. The report is Mixed/Lower Case Problem Selection List/Category Names.

> Sample Mixed/Lower Case Name Report/Message

Subj: Mixed & Lower Case List/Category Name Report \[#203469\]

03/13/17@12:59 18 lines

From: GMPL\*2.0\*49 INSTALL In 'IN' basket. Page 1

--------------------------------------------------------------------------

Mixed/lower case problem selection list/category names are no longer

allowed with patch GMPL\*2.0\*49. This patch scans the Problem Selection

List and Problem Selection Category files for any names in mixed or lower

case letters and converts them to upper case.

For those conversions that failed, please have a CAC or somebody with

FileMan access manually modify the name to upper case.

The following list names converted successfully:

Test List 1

The following category names converted successfully:

Cardiovascular

- Data Dictionary Deletion: The current data dictionaries for the PROBLEM SELECTION LIST file \#125 and PROBLEM SELECTION CATEGORY file \#125.11 will be deleted in preparation for the newly updated data dictionaries.

During patch installation, the following will occur:

- Routine installation/update
- Data Dictionary updates
- Addition of the National Problem Selection List Content: This patch will also install the first version of the VA-NATIONAL PROBLEM SELECTION LIST which comprises of the following national selection list categories:
- VA-PRIMARY CARE
- VA-CARDIOLOGY
- VA-DENTAL
- VA-DERMATOLOGY
- VA-DIABETES
- VA-EAR NOSE THROAT
- VA-EMERGENCY DEPARTMENT
- VA-ENDO METAB EXCEPT DIABETES
- VA-GASTROENTEROLOGY
- VA-GENERAL SURGERY
- VA-GYNECOLOGY
- VA-HEMATOLOGY
- VA-INFECTIOUS DISEASE
- VA-MENTAL HEALTH
- VA-NEUROLOGY
- VA-NEUROSURGERY
- VA-ONCOLOGY
- VA-OPHTHALMOLOGY
- VA-ORTHOPEDICS
- VA-PAIN
- VA-PLASTIC SURGERY
- VA-POLYTRAUMA
- VA-PULMONARY
- VA-RENAL NEPHROLOGY
- VA-RHEUMATOLOGY
- VA-UROLOGY
- Create New Key: With the installation of GMPL\*2.0\*49, a new key, GMPL IMPRT UTIL, has been created. This key will be given to those who will create problem selections lists and who can use the import utility.
- Updates to protocols and options

Post-installation:

- Duplicate Name Scan: The patch will scan for duplicate selection list/category names and generate a report The CAC will have to review any duplicate list and/or category names found and edit/delete/reconcile the entries as appropriate.

> Sample Duplicate Name Report/Message

Subj: Duplicate Problem Selection List/Category Name Report \[#203470\]

03/13/17@12:59 10 lines

From: GMPL\*2.0\*49 INSTALL In 'IN' basket. Page 1

--------------------------------------------------------------------------

Duplicate problem selection list/category names are no longer allowed with

patch GMPL\*2.0\*49. The following list/category names are duplicates.

Please have your CAC review these with the pre-existing file entries and

rename, delete, or reconcile the duplicate entries as needed.

Duplicate List Names:

ORTHOPEDIC

Duplicate Category Names:

NEUROLOGY

- Mark GMPL CODE LIST menu option out of order
- Update GMPL SELECTION LIST CSV CHECK menu text
- Update display order of several items for GMPL BUILD LIST MENU option
- Resequencing GMPL MENU BUILD GROUP protocol menu items
- Set pre-existing lists/categories to a default local class
- Changes to the File Structure: To support the enhancements to problem list selection, the file structures for the PROBLEM SELECTION LIST file \#125 and PROBLEM SELECTION CATEGORY file \#125.11 were also redesigned. To enable a tighter coupling between a selection list and its categories, the PROBLEM SELECTION LIST CONTENTS file \#125.1 will now be a subfile/multiple of the PROBLEM SELECTION LIST file \#125. The same concept applies to the PROBLEM SELECTION CATEGORY CONTENT file \#125.12 that will now be a subfile of the PROBLEM SELECTION CATEGORY file \#125.11. A new CLASS field is also added to the List (#125) and Category (#125.11) files in order to delineate, control, and manage the editing capabilities of national, local, or VISN level lists and categories. With this new redesign, the file data is also migrated to their respective file record entries to ensure continued operability.

OR\*3\*429:

Pre-installation:

N/A

During:

- Installation/update of routines and parameter

Post-installation:

- Create New Parameter: A new Default Problem Selection List Display, ORQQPL SELECTION LIST, parameter will be added to the system. This parameter will be where the problem selection list assignments will be stored. This parameter determines which problem selection list the user will be shown when adding a new patient problem in CPRS.
- Migrate pre-existing USER/CLINIC list assignments to the new ORQQPL SELECTION LIST parameter: The pre-existing user and clinic list assignments in the New Person and Problem Selection List files respectively will be migrated over and managed under this new parameter.

> When patch OR\*3.0\*429 patch is installed, it checks on the codes from lists that are being moved from the NEW PERSON and PROBLEM SELECTION LIST files to the ORQQPL SELECTION LIST parameter. Below are samples of what the message might look like:

> Migrating default user Problem Selection list from NEW PERSON File to the

> ORQQPL SELECTION LIST parameter...

The following selection lists could not be migrated to the ORQQPL

SELECTION LIST parameter because it contains one or more problems that

have inactive SNOMED and/or ICD codes attached to them.

CARDIOLOGY

ORTHOPEDIC

Migrating default clinic Problem Selection list from PROBLEM SELECTION

LIST File to the ORQQPL SELECTION LIST parameter...

The following selection lists could not be migrated to the ORQQPL

SELECTION LIST parameter because it contains one or more problems that

have inactive SNOMED and/or ICD codes attached to them.

CARDIOLOGY

ORTHOPEDIC

- Set system and package level setting of the parameter to the default VA-NATIONAL PROBLEM SELECTION LIST

#### Installation Instructions

This combined build will install two patches: GMPL\*2.0\*49 and OR\*3.0\*429. The patches load several routines and may be installed with users on the system although it is STRONGLY recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

> **NOTE:** Users should stay out of the Problem Selection List ListManager Application entirely during the installation of this patch as data from files \#125.1 and \#125.12 are being migrated to files \#125 and \#125.11 respectively.

Utilizing this ListMan App during the data migration process could lock up certain records and prevent data from being migrated successfully. If this should occur, a lock error message will be generated to the installer identifying those records during the post-installation.

1.  From the Kernel Installation and Distribution System Menu, select the Installation menu.
2.  Next, select 'Load a Distribution'. When prompted "Enter a Host File: enter \<directory\>PROBLEM_SELECTION_LIST_BUILD_1_0.KID (where directory represents the location where you stored the KIDS file).
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the multi- package build name, PROBLEM SELECTION LIST BUILD 1.0:
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and select the package: PROBLEM SELECTION LIST BUILD 1.0.
5.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', respond with NO. KIDS will automatically attach the new menu options to the designated menu tree during the installation process. There is no need to rebuild the menu trees upon completion of installation.
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond with NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', respond with YES. Disable all GMPL\* options and protocols.

<span id="_Toc500220873" class="anchor"></span>

#### Post-Installation Instructions

The post-install routine will automatically migrate data from files \#125.1 and \#125.12 to files \#125 and \#125.11 respectively. It is imperative that users stay out of the Problem Selection List ListMan App until the installer has received messages that the migration has successfully completed.

It will also set the CLASS field for all pre-existing lists and categories to “Local”. Additionally it will scan for duplicate list/category names and send a report to the installer and OR CACs mail group via MailMan. A few other post-processing items such as updating the display order of several option and protocol menu items are also performed. The GMPL CODE LIST menu option is also marked out of order.

#### Review Problem Selection Lists to See if Reassignments Are Necessary

When this patch is installed, any pre-existing User or Clinic selection list assignments prior to patch installation will be retained. A report will be generated and sent to the installer and OR CACS mail group via Mailman that identifies all existing assignments. Sites should review these assignments to see if they need to be changed.

If there are any users that are assigned to a selection list that no longer exists, they will also be captured in this report.

The following is a sample report:

Subj: Pre-existing USER/CLINIC Selection List Assignment Report \[#154024\]

08/15/17@09:50 129 lines

From: GMPL\*2.0\*49 INSTALL In 'IN' basket. Page 1

--------------------------------------------------------------------------

This report was auto generated during installation to identify Problem

Selection Lists assigned to users and clinics prior to the installation of

GMPL\*2.0\*49. After installation all users and clinic assignments will be

migrated to the new Default Selection List Display parameter setting. If

users and clinics desire to use the National Problem Selection List as

their default setting then use the Assign/Remove menu option to reassign

those users or clinics listed in the report.

User Selection List Assignments:

PROVIDER,ONE USER LIST 1

PROVIDER,TWO USER LIST 2

PROVIDER,THREE USER LIST 3

PROVIDER,FOUR USER LIST 4

Clinic Selection List Assignments:

CARDIOLOGY CARDIO CLINIC LIST

GENERAL MEDICINE GENERAL MED CLINIC LIST

PAIN CLINIC PAIN CLINIC LIST

PRIMARY CARE PRIMARY CARE CLINIC LIST

User(s) assigned to a Selection List that no longer exists:

PROVIDER,FIVE Selection List \#5

PROVIDER,SIX Selection List \#6

Type \<Enter\> to continue or '^' to exit:

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on the build.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the two test sites listed in section 3.2.2.

The sites followed the provided test scripts and executed the test cases according to the plan to test the patches of the Problem Selection List Enhancements. The sites either passed or failed any item based on testing. The tests were performed by Clinical Application Coordinators at each site who are familiar using the CPRS and Problem List applications. The test cases were then delivered with concurrence by the sites to the development team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the CPRS or Problem List application or a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out the Problem Selection List Enhancements would involve Problem Selection List data dictionary changes and the removal of nationally released Problem Selection List content.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out the patch should only be considered if there is a catastrophic failure of CPRS or the Problem List application. The back out would be accomplished by installing a patch.

### Installing the Back-Out Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for the Problem Selection List Enhancements is in the event of a catastrophic failure.

1.  Contact the CPRS Development team to notify them there has been a catastrophic failure with the Problem Selection List Enhancements:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

2.  If the decision is made to proceed with back-out and rollback, coordinate with the appropriate IT support, local and ITOPS, to schedule an installation time for the back-out.
3.  Install patch GMPL\*2.0\*51.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify that the data dictionary for the PROBLEM SELECTION LIST file (#125) contains only three fields: NAME (#.01), DATE LAST MODIFIED (#.02), & CLINIC (#.03).
2.  Verify that the data dictionary for the PROBLEM SELECTION CATEGORY file (#125.11) contains only two fields: NAME (#.01), DATE LAST MODIFIED (#1).
3.  Perform regression testing to verify that the current Problem Selection lists still display correctly and works in VistA and CPRS.
4.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are quite a few database changes specifically related the Problem Selection List Enhancements. Six and eight new fields are added to the PROBLEM SELECTION LIST file \#125 and PROBLEM SELECTION CATEGORY file \#125.11, respectively. Additionally, one new option, protocol, security key, and parameter is added to support the enhancements. A few of the pre-existing Problem Selection list menu options and protocols are also modified.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback would only be considered if there was a catastrophic failure that causes loss of function for the CPRS or Problem List application or a significant patient safety issue.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rolling back the Problem Selection List Enhancements would involve restoring the previous Problem Selection List data dictionaries and file structures and the removal of the new option, protocol, security key, parameter, and nationally released Problem Selection List content.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a rollback for the Problem Selection List Enhancements is in the event of a catastrophic failure.

1.  Contact the CPRS Development team to notify them there has been a catastrophic failure with the Problem Selection List Enhancements:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

2.  If the decision is made to proceed with back-out and rollback, coordinate with the appropriate IT support, local and ITOPS, to schedule an installation time for the rollback.
3.  Install patch GMPL\*2.0\*51.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify that the data dictionary for the PROBLEM SELECTION LIST file (#125) contains only three fields: NAME (#.01), DATE LAST MODIFIED (#.02), & CLINIC (#.03).
2.  Verify that the data dictionary for the PROBLEM SELECTION CATEGORY file (#125.11) contains only two fields: NAME (#.01), DATE LAST MODIFIED (#1).
3.  Verify that the following new items have been removed: GMPL SELECTION LIST IMPORT option, GMPL MENU COPY GROUP protocol, GMPL IMPRT UTIL security key, and ORQQPL SELECTION LIST parameter.
4.  Perform regression testing to verify that the current Problem Selection lists still display correctly and works in VistA and CPRS.
5.  Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

# Example Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation \<TEST ACCOUNT\> Option: 6 Install Package(s)

> Select INSTALL NAME: PROBLEM SELECTION LIST BUILD 1.0 8/30/17@12:25:48

> =\> Problem Selection List Build 1.0 ;Created on Aug 23, 2017@08:35:44

> This Distribution was loaded on Aug 30, 2017@12:25:22 with header of

> Problem Selection List Build 1.0 ;Created on Aug 23, 2017@08:35:44

> It consisted of the following Install(s):

> PROBLEM SELECTION LIST BUILD 1.0 GMPL\*2.0\*49 OR\*3.0\*429

> Checking Install for Package PROBLEM SELECTION LIST BUILD 1.0

> Install Questions for PROBLEM SELECTION LIST BUILD 1.0

> Checking Install for Package GMPL\*2.0\*49

> Install Questions for GMPL\*2.0\*49

> Incoming Files:

> 125 PROBLEM SELECTION LIST (including data)

> Note: You already have the 'PROBLEM SELECTION LIST' File.

> I will REPLACE your data with mine.

> 125.11 PROBLEM SELECTION CATEGORY (including data)

> Note: You already have the 'PROBLEM SELECTION CATEGORY' File.

> I will REPLACE your data with mine.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

> Checking Install for Package OR\*3.0\*429

> Install Questions for OR\*3.0\*429

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// SECURE SHELL

> Install Started for PROBLEM SELECTION LIST BUILD 1.0 :

> Aug 30, 2017@12:25:48

> Build Distribution Date: Aug 23, 2017

> Installing Routines:

> Aug 30, 2017@12:25:48

> Install Started for GMPL\*2.0\*49 :

> Aug 30, 2017@12:25:48

> Build Distribution Date: Aug 23, 2017

> Installing Routines:

> Aug 30, 2017@12:25:48

> Running Pre-Install Routine: PRE^GMPLY49

> Retrieving pre-existing USER/CLINIC selection list assignment report...

> Report has been generated to the installer & OR CACS mailgroup via MailMan.

> Scanning for mixed or lower case Problem Selection list/category names...

> No mixed or lower case list/category names found.

> Removing old PROBLEM SELECTION LIST file \#125 data dictionary...

> Data dictionary for file \#125 removed.

> Removing old PROBLEM SELECTION CATEGORY file \#125.11 data dictionary...

> Data dictionary for file \#125.11 removed.

> Installing Data Dictionaries:

> Aug 30, 2017@12:26:07

> Installing Data:

> Aug 30, 2017@12:26:08

> Installing PACKAGE COMPONENTS:

> Installing SECURITY KEY

> Installing PROTOCOL

> Installing OPTION

> Aug 30, 2017@12:26:08

> Running Post-Install Routine: POST^GMPLY49

> Scanning for duplicate Problem Selection list/category names...

> A duplicate list/category name report has been generated to the installer

> and OR CACS mailgroup via MailMan.

> Marking GMPL CODE LIST menu option out of order...

> Done.

> Updating GMPL SELECTION LIST CSV CHECK menu text...

> Done.

> Updating display order of several items for GMPL BUILD LIST MENU option...

> Done.

> Resequencing GMPL MENU BUILD GROUP protocol menu items...

> Done.

> Setting pre-existing lists to a default LOCAL class...

> ...Local class assignments completed.

> Setting pre-existing categories to a default LOCAL class...

> ...Local class assignments completed.

> Migrating data in File \#125.1 to File \#125...

> ...Migration complete.

> Migrating data in File \#125.12 to File \#125.11...

> ...Migration complete.

> Updating Routine file...

> Updating KIDS files...

> GMPL\*2.0\*49 Installed.

> Aug 30, 2017@12:26:08

> Not a production UCI

> NO Install Message sent

> Install Started for OR\*3.0\*429 :

> Aug 30, 2017@12:26:08

> Build Distribution Date: Aug 23, 2017

> Installing Routines:

> Aug 30, 2017@12:26:08

> Installing PACKAGE COMPONENTS:

> Installing PARAMETER DEFINITION

> Aug 30, 2017@12:26:08

> Running Post-Install Routine: POST^ORY429

> Migrating default user Problem Selection list from NEW PERSON File to the

> ORQQPL SELECTION LIST parameter...

> The following selection lists could not be migrated to the ORQQPL SELECTION

> LIST parameter because it contains one or more problems that have inactive

> SNOMED and/or ICD codes attached to them.

> CHERYL

> MELANIE'S

> TESTER'S LIST

> Migrating default clinic Problem Selection list from PROBLEM SELECTION LIST

> File to the ORQQPL SELECTION LIST parameter...

> The following selection lists could not be migrated to the ORQQPL SELECTION

> LIST parameter because it contains one or more problems that have inactive

> SNOMED and/or ICD codes attached to them.

> CHERYL

> MELANIE'S

> TESTER'S LIST

> Setting system & package level for ORQQPL SELECTION LIST parameter to a default

> VA National Selection List...

> Updating Routine file...

> Updating KIDS files...

> OR\*3.0\*429 Installed.

> Aug 30, 2017@12:26:09

> Not a production UCI

> NO Install Message sent

> Updating Routine file...

> Updating KIDS files...

> PROBLEM SELECTION LIST BUILD 1.0 Installed.

> Aug 30, 2017@12:26:09

> No link to PACKAGE file

> NO Install Message sent

> Install Completed