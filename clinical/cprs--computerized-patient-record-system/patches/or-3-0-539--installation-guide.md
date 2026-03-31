---
title: OR*3.0*539 (CPRS v32a) Deployment, Installation, Back Out, and Roll Back Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: (CPRS v32a) Deployment, Installation, Back Out, and Roll Back Guide
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3.0
patch_id: OR*3.0*539
group_key: "CPRS:OR:3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - cprs
  - table
  - contents
  - order
  - installation
  - back
  - sites
  - deployment
  - access
  - rollback
page_count: 0
word_count: 5946
section_count: 36
table_count: 17
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2021
revision_count: 4
revision_newest: 8/16/2021
revision_oldest: 6/25/2021
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_539_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_0_539_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

---
title: |
  <span id="_top" class="anchor"></span>CPRS v32a (OR\*3.0\*539)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](or-3-0-539-cprs-v32a-deployment-installation-back-out-and-roll-back-guide/001.png)

August 2021

Office of Information and Technology (OI&T)

Revision History

| Date  | Version | Description                                                                                             | Author            |
|-----------|-------------|-------------------------------------------------------------------------------------------------------------|-----------------------|
| 8/16/2021 | 1.3         | Added more information about pre-installation tasks and unflagging orders configuration                     | CPRS Development team |
| 7/14/2021 | 1.2         | Added some notes about how locking affects the names displayed in selection boxes in CPRS                   | CPRS Development team |
| 7/12/2021 | 1.1         | Expanded the explanation of the new feature for locking the OR CPRS GUI CHART option, rearranged some text. | CPRS Development team |
| 6/25/2021 | 1.0         | Initial release                                                                                             | CPRS Development team |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |
|           |             |                                                                                                             |                       |

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
    - [Site Preparation](#site-preparation)
  - [Resources](#resources)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download Files](#download-files)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Locking General User Access to CPRS GUI](#locking-general-user-access-to-cprs-gui)
  - [Installation Procedure](#installation-procedure)
  - [Make the CPRS GUI Available](#make-the-cprs-gui-available)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [Locking the OR CPRS GUI CHART Option](#locking-the-or-cprs-gui-chart-option)
  - [Assigning the OR CPRS TESTER Key](#assigning-the-or-cprs-tester-key)
  - [System Configuration](#system-configuration)
    - [Identifying and Editing Non-VA Order Menu Text or Removing the Order Menu Display Text](#identifying-and-editing-non-va-order-menu-text-or-removing-the-order-menu-display-text)
    - [Configuring Parameters](#configuring-parameters)
  - [Reenable Access or CPRS for All Users](#reenable-access-or-cprs-for-all-users)
  - [Change to Online Help Type](#change-to-online-help-type)
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
The Computerized Patient Record System (CPRS) is a Veterans Health Information Systems and Technology Architecture (VistA) suite of application packages. CPRS enables you to enter, review, and continuously update information connected with a patient. With CPRS, you can order lab tests, medications, diets, radiology tests and procedures, record a patient’s allergies or adverse reactions to medications, request and track consults, enter progress notes, diagnoses, and treatments for each encounter, and enter discharge summaries. In addition, CPRS supports clinical decision-making and enables you to review and analyze patient data.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the CPRS v32a will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32a requires a fully patched VistA system.

Checks will be performed during the installation of the Kernel Installation and Distribution System (KIDS) build to ensure that the system is at a minimum level of compliance.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32a has a combined multi-patch build KIDS build and a GUI executable. The combined build is installed on the VistA server and the executable can be placed on individual workstations, VA Applications Consolidated Server (VACS), or on a Citrix server.

CPRS v32a is 508 compliant and uses the same security measures as VistA. Users will authenticate using either their Personal Identification Verification (PIV) card or their access and verify codes.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 18%" />
<col style="width: 45%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CPRS Implementation Team</td>
<td>Deployment</td>
<td>Create an overall deployment schedule, putting sites into waves. Installers will coordinate with individual sites on a date and time for each site or groups of sites to install.</td>
</tr>
<tr class="even">
<td>CPRS Implementation Team</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
</tr>
<tr class="odd">
<td>CPRS Software Quality Assurance (SQA) team and field test sites</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="even">
<td>Application Coordinators</td>
<td><p>Release</p>
<p>Deployment</p></td>
<td>Application Coordinators release patches.</td>
</tr>
<tr class="odd">
<td>ITOPS and Local sites</td>
<td>Installation</td>
<td>Plan and schedule installation. CPRS Implementation Team creates deployment plan placing sites in waves. ITOPS coordinates specific dates and times with sites, VISNs.</td>
</tr>
<tr class="even">
<td>CPRS Implementation Team</td>
<td>Installations</td>
<td>Coordinate training. CPRS Team will provide national installation and train-the-trainer presentations. Other groups may also provide training.</td>
</tr>
<tr class="odd">
<td>CPRS Implementation Team, ITOPS, and Area Manager</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).</td>
</tr>
<tr class="even">
<td>CPRS Implementation Team and HPS Clinical Teams</td>
<td>Post Deployment</td>
<td>Software Support will be provided by the CPRS Implementation Team during warranty period, which is 90 days after national release or at the end of the deployment waves, whichever comes last. Support then changes to the normal ticketing process.</td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v32a deployment will be a staggered or wave release consisting of 3 waves.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v32a national deployment and installation will consist of 3 waves lasting 4 weeks each. Each wave will begin two weeks after the beginning of the previous wave. Wave 2 will begin two weeks after the beginning of Wave 1, and Wave 3 will begin two weeks after the beginning of Wave 2.

The targeted national release date for CPRS v32a is late June to early July 2021. Kick Off and training call for Wave 1 will follow shortly.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS v32a bundle of patches and the accompanying GUI executable will be deployed to all VistA instances. The patches will be installed on the server and the GUI executable will be installed on a VACS server, a Citrix server, or on local workstations or on a combination of them, depending on how the site is set up.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32a will be deployed to all VistA instances. There is a server component and a GUI executable.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites are not required to use all features in CPRS v32a. Each site needs to decide if they will use the feature or do some work in preparation for the CPRS v32a installation.

- Template Required Fields: This feature can be disabled if desired. It is exported as enabled so will be active immediately. When the Template Required Fields feature is enabled, dialog templates that have required fields will have these required fields highlighted. The highlighting and a navigation bar help the user identify which required fields need attention. The required fields still have the asterisks as they did before. Some sites might be concerned that users will fill out the required fields and ignore other fields. Therefore, enabling this feature is a site decision.
- Provider Access: Removing multiple COR tab entries with expiration dates for providers. With the new features for selecting providers, some changes as to what defines a provider are used. Problems occur when the provider has more than one entry in the list of COR tabs and the earlier entry or entries has an expiration date. The earlier entry or entries must be removed. If users have trouble logging in to CPRS, they may also need to log in using their access and verify codes and ensure they have the OR CPRS GUI CHART option assigned to them.

  To help identify any users that may have expired COR tab entries, an example FileMan search has been posted to the CPRS 32A CAC/HIS Resources Share Point. “CPRS 32A Fileman Search for Users w/COR Tabs & Expiration Date.docx”
- Limit Additional Signers: Previously, many users that could not sign notes were displaying selection lists. CPRS v32a added a feature enabling sites to put users that should not appear in displays into an existing User Class or a new User Class that the site creates and then exclude that User Class using the OR CPRS USER CLASS EXCLUDE parameter.
- Restricting Unflagging Capabilities: Restricting Unflagging of orders is enabled when CPRS v32a is installed. Sites must decide whether to use Unflagging restrictions and how to configure this feature.
  - If sites do NOT wish to use unflagging restrictions, they can turn them off by setting the OR UNFLAGGING RESTRICTIONS parameter to NO. If the parameter is set to NO, unflagging will continue to function as it does now.
  - If the OR UNFLAGGING RESTRICTIONS parameter is set to YES (which it is when installed), the following people will be able to unflag orders:
    - ORES keyholders
    - The user who flagged the order
    - The recipients of the flag
    - Specified keyholders as configured by the site after installation. This configuration is by display group. Sites will need to determine which keyholders should be able to unflag orders for each display group.
      - Remember that ORES keyholders do not need to be assigned because ORES keyholders can always unflag any order in all display groups.
      - Identify which keyholders you want to be able to unflag for each display group. Have this information ready for later configuration. For example, you may want to set up the ORELSE key (to unflag in CPRS) and or the PSORPH key (to unflag in backdoor outpatient pharmacy) for the OUTPATIENT MEDICATIONS display group.

If your site has some preparation to make, your site can use the following table.

Table 2: Site Preparation

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------|---------------------------|---------------------------------------------|-------------------|-----------|
|                |                           |                                             |                   |           |
|                |                           |                                             |                   |           |
|                |                           |                                             |                   |           |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No additional resources are required.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32a requires a fully patched VistA System for installation.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For national release, sites will receive communication that the release has occurred, which will normally be an Action Item or Bulletin.

Sites will use their internal communications to let their users know about upcoming installations and any associated downtime. This is critical as users can often slow the installation process if they are on the system while installers are trying to get the software installed.

Clinical Application Coordinators (CACs), installers, and other site personnel (as determined by the site) will need to coordinate installation dates and times. In addition, other support personnel may need to be consulted – such as the Citrix support, Client Technologies (if required).

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32a should not require any changes to the current environment.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32a should follow a normal CPRS installation.

## Download Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As mentioned in section 3.1, CPRS v32a will follow a waved deployment. This version of CPRS GUI is being released in three waves. During this wave deployment process, the sites will be contacted by the CPRS Implementation Team with information about downloading the software and updated documentation. Access to the software and documentation is restricted until deployment is complete.

After the wave deployment has been completed, documentation can be found on the VA Software Documentation Library at:

https://www.va.gov/vdl/

The software for this patch is being released using a host file.

Other Software Files

This release also includes other software.

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 31%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Contents</th>
<th>Retrieval Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR_30_539.ZIP</td>
<td><p>CPRSChart.exe</p>
<p>GMV_VitalsViewEnter.dll</p>
<p>YS_MHA_A_XE10.dll</p>
<p>RoboEx32.dll</p>
<p>borlndmm.dll</p>
<p>CPRSChart.map</p>
<p>HELP Directory</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>OR_30_539_SRC.ZIP</td>
<td>CPRS v32a Source</td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>CPRS_V32A_COMBINED_BUILD.KID</td>
<td>CPRS V32A COMBINED</td>
<td>ASCII</td>
</tr>
</tbody>
</table>

Documentation describing the new functionality is included in this release. Documentation can be found on the VA Software Documentation Library at: https://www.va.gov/vdl/.

The CPRS v32a multi-package build (CPRS V32A COMBINED BUILD 1.0) includes several patches that will be installed in the following order:

- OR\*3.0\*539
- TIU\*1.0\*339
- GMRA\*4.0\*63
- GMRV\*5.0\*43
- GMRC\*3.0\*84
- YS\*5.01\*170
- LR\*5.2\*544

The CPRS v32a files can be downloaded from the appropriate location:

1)  Download the following files.
    1.  CPRS_V32A_COMBINED_BUILD.KID
    2.  OR_30_539.zip

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Clinical Application Coordinators (CACs) will be available for configuration and troubleshooting
- Installer with programmer access
- Familiarity with and access to the XPAR MENU TOOLS parameter system

## Locking General User Access to CPRS GUI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a user launches the CPRS GUI, the underlying VistA system checks to see if the user has access to the OR CPRS GUI CHART entry in the OPTION (#19) file. If the user has access to the option, they can continue opening the CPRS GUI. Locking an option with a security key is a long-standing VistA feature that is newly applied to the usage of OR CPRS GUI CHART with CPRS v32a. The ability to run the CPRS GUI can be restricted by adding the OR CPRS TESTER security key to the LOCK field of the OR CPRS GUI CHART entry in the OPTION (#19) file. The primary benefit of restricting access to CPRS GUI is reducing potential for errors from users accessing the software before post-installation configuration has completed. 

When the lock is activated in a VistA system, only users that hold either the OR CPRS TESTER or XUPROGMODE security keys will be able to launch the CPRS GUI against that VistA system. Until the lock is deactivated, all other users who attempt to launch the CPRS GUI in that VistA system will receive an error message stating that the option is locked. As option locking is a feature of VistA, locking access to OR CPRS GUI CHART in a test VistA system has no effect on user ability to access OR CPRS GUI CHART in a production VistA system.

> **IMPORTANT:** Prior to installing CPRS v32a, facility staff must create a list of users to whom the OR CPRS TESTER key shall be assigned. Typically, this would be informatics staff involved with testing and configuring a new version of CPRS GUI. These names will be used in section 4.12, “Assigning the OR CPRS Tester Key”.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Do not queue the install.

1.  Use the Load a Distribution option contained on the Kernel Installation and Distribution System Menu to load the Host file.
    1.  When prompted to “Enter a Host File: “ enter: \<*path where you downloaded the file*\>/CPRS_V32A_COMBINED_BUILD.KID
    2.  Choose to run the Environmental Check option when loading the distribution and ensure there are no errors to handle before proceeding.
    3.  Note that after loading the distribution you are directed to use the name “CPRS V32A COMBINED BUILD 1.0” when taking the install action.
2.  Optionally execute the “Verify Checksums” option on the same menu.
3.  Backup the install by using the “Backup a Transport Global” option on the same menu
4.  Install the bundle of patches by executing the “Install Package(s)” option.
    1.  For this option at the “INSTALL NAME:” prompt, you will need to use the name “CPRS V32A COMBINED BUILD 1.0” as noted in 1.c above.
5.  When prompted ‘Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//’, answer NO.
6.  When prompted ‘Want KIDS to INHIBIT LOGONs during the install? NO//’, answer NO.
7.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, answer NO.
8.  When prompted ‘Enter the Device you want to print the Install messages. You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install. DEVICE: HOME//’ press \<Enter\>.
9.  During the installation, you may see the following:

------------Data Value Missing in *YOUR SYSTEM NAME DISPLAYS HERE*------

ORDER CHECK RULE: ORDER FLAGGED FOR CLARIFICATION \[5\]

RELATION ACTIONS: 1 \[1\]

EXECUTE CODE field \[9\]

\(R\) C32AD.DEVSLC.FO-SLC.MED.VA.GOV: N I,USR S I=0 F S I=\$"

Do you want to change the local 'RELATION ACTIONS' field ?? YES//YES

> At this Do you want to change the local 'RELATION ACTIONS' field ?? YES prompt, answer YES.

## Make the CPRS GUI Available

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The two most common options for placing the CPRS executable are the VACS servers and individual workstations. In addition, the executable is typically placed on a CITRIX server for remote access.

The CPRS executable (cprschart.exe), along with the files extracted in step 4.3 should be placed in the location used by the site. For situations where it is required to push to individual workstations, an SCCM package has been developed.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, check the CPRS splash screen to verify that the correct version is now available. The correct GUI version should be CPRS 1.32.114.1. The Cyclic Redundancy Check (CRC) number should be 30EA611C.

To verify the VistA installation, use FileMan inquiry to the OPTION (#19) file. When prompted for the option, enter OR CPRS GUI CHART. Ensure the CPRS Chart version is: 1.32.114.1

## Locking the OR CPRS GUI CHART Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Once the OR CPRS GUI CHART option is locked, some users’ names will not display in the provider selection box(es) in CPRS. This is expected! Please ensure the users doing post install testing are aware that will occur.

VistA Applications Support - To enact the locking and have CPRS GUI opened only by authorized users

1.  At the Systems Manager Menu Option prompt, type Menu Management and press \<Enter\>.
2.  At the Select Menu Management Option prompt, type Edit Options and press \<Enter\>.
3.  At the Select OPTION to edit prompt, type OR CPRS GUI CHART and press \<Enter\>.
4.  At the NAME prompt, it should read OR CPRS GUI CHART, accept by pressing \<Enter\>.
5.  At the MENU TEXT prompt, it should read CPRSChart version 1.32.114.1 Replace, accept by pressing \<Enter\>.
6.  At the PACKAGE prompt, press \<Enter\>.
7.  At the OUT OF ORDER MESSAGE prompt, press \<Enter\>.
8.  At the LOCK prompt, type OR CPRS TESTER and press \<Enter\>.

> **NOTE:** Holders of the XUPROGMODE key are exempt from this option file locking mechanism. This is an existing feature of the Kernel Menu Management module.

\<CPM\> Select Systems Manager Menu Option: MENU MANagement

          Edit options

          Key Management ...

          Secure Menu Delegation ...

          Restrict Availability of Options

          Option Access By User

          List Options by Parents and Use

          Fix Option File Pointers

          Help Processor ...

   OPED   Screen-based Option Editor

          Display Menus and Options ...

          Menu Rebuild Menu ...

          Out-Of-Order Set Management ...

          See if a User Has Access to a Particular Option

          Show Users with a Selected primary Menu

\<CPM\> Select Menu Management Option: EDIT OPtions

Select OPTION to edit: OR CPRS GUI CHART       CPRSChart version 1.32.114.1

NAME: OR CPRS GUI CHART//

MENU TEXT: CPRSChart version 1.32.114.1  Replace

PACKAGE:

OUT OF ORDER MESSAGE:

LOCK: OR CPRS TESTER

REVERSE/NEGATIVE LOCK: ^

## Assigning the OR CPRS TESTER Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CACs may use the Allocate OE/RR Security Keys \[ORCL KEY ALLOCATION\] option of the CPRS Configuration (Clin Coord) \[OR PARAM COORDINATOR MENU\] menu to allocate the OR CPRS TESTER security key to users identified in the “Locking General User Access to CPRS GUI” section.

OR CPRS TESTER will be the last security key presented when using this allocation option.

> Note: Once the OR CPRS GUI CHART option is locked, some users’ name will not display in the provider selection box(es) in CPRS. Only users of the OR CPRS TESTER key will display in some places.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Identifying and Editing Non-VA Order Menu Text or Removing the Order Menu Display Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To address a Patient Safety Issue, a change was made to the Non-VA Meds order dialog to include the word “Documentation” in display text, such as “Non-VA Meds (Documentation)”. However, there may be Order Menu entries that CPRS does not control, such as Order Menus created by sites. If your site has Order Menu entries that read only “Non-VA Meds”, those items must be identified and corrected—either by adding “(Documentation)” to the display text or by removing the Non-VA display text from the Order Menu. If you remove the display text, the system will display the Order Dialog name, which has the notation already.

To identify any Order Menu items that should be changed, someone with FileMan access should run the following FileMan search:

Select OPTION: SEARCH FILE ENTRIES 

Output from what File: ORDER DIALOG//     (908 entries)

  -A- SEARCH FOR ORDER DIALOG FIELD: TYPE 

  -A- CONDITION: EQUALS 

  -A- EQUALS: M  menu

  -B- SEARCH FOR ORDER DIALOG FIELD: ITEMS     (multiple)

    -B- SEARCH FOR ORDER DIALOG ITEMS SUB-FIELD: ITEM 

    -B- CONDITION: EQUALS 

    -B- EQUALS ORDER DIALOG: NON VA

     1   NON VA MED VITAMIN D QD  PSHZ VITAMIN D (TEST-MEM)

     2   NON VA MEDICATIONS (DOCUMENTATION)  PSH OERR

CHOOSE 1-2: 2  PSH OERR

    -C- SEARCH FOR ORDER DIALOG ITEMS SUB-FIELD: DISPLAY

     1   DISPLAY ONLY? 

     2   DISPLAY TEXT 

CHOOSE 1-2: 2  DISPLAY TEXT

    -C- CONDITION: 'NULL 

    -D- SEARCH FOR ORDER DIALOG ITEMS SUB-FIELD:

  -D- SEARCH FOR ORDER DIALOG FIELD:

IF: A&B&C

        CONDITION -C- WILL APPLY TO THE SAME MULTIPLE AS CONDITION -B-

        ...OK? Yes//   (Yes)

    TYPE EQUALS "M" (menu)    and ORDER DIALOG ITEM EQUALS 389 (PSH OERR)

                together with ORDER DIALOG DISPLAY TEXT NOT NULL

DO YOU WANT THIS SEARCH SPECIFICATION TO BE CONSIDERED TRUE FOR CONDITION -B-

        1) WHEN AT LEAST ONE OF THE 'ITEMS' MULTIPLES SATISFIES IT
        2) WHEN ALL OF THE 'ITEMS' MULTIPLES SATISFY IT

    CHOOSE 1-2: 1//

OR:

STORE RESULTS OF SEARCH IN TEMPLATE:

Sort by: NAME//

Start with NAME: FIRST//

First Print FIELD: .01  NAME

Then Print FIELD:

Heading (S/C): ORDER DIALOG Search//

DEVICE:   PSUEDO-TERMINAL    Right Margin: 80//

ORDER DIALOG Search                                  JAN 14, 2021@11:08   PAGE 1

NAME

--------------------------------------------------------------------------------

ORZ MENU

ORZZ ORDER MENU

ORZ ADD MENU NURSING

                         3 MATCHES FOUND.

Here is an example showing how to edit or remove the display text:

Select CPRS Configuration (Clin Coord) \<TEST ACCOUNT\> Option: MM  Order Menu Management

   OI     Manage orderable items ...

   PM     Enter/edit prompts

   GO     Enter/edit generic orders

   QO     Enter/edit quick orders

   QU     Edit personal quick orders by user

   ST     Enter/edit order sets

   AC     Enter/edit actions

   MN     Enter/edit order menus

   AO     Assign Primary Order Menu

   CP     Convert protocols

   SR     Search/replace components

   LM     List Primary Order Menus

   DS     Disable/Enable order dialogs

   CS     Review Quick Orders for Inactive ICD9 Codes

   MR     Medication Quick Order Report

   CA     Quick Order Mixed-Case Report

   CO     Create Clinic Order QOs from Inpatient QOs

   CV     Convert IV Inpatient QO to Infusion QO

   DF     Quick Order Free-Text Report

   FR     IV Additive Frequency Utility

   SP     SUPPLY COVERSION UTILITY MENU ...

Select Order Menu Management \<TEST ACCOUNT\> Option: MN  Enter/edit order menus

Select ORDER MENU: ORZ ADD MENU CLINICIAN

<u>Menu Editor                   Jan 19, 2021@13:53:28          Page:    1 of    5</u>

Menu: ORZ ADD MENU CLINICIAN                                    Column Width: 26

<u>+1                         2                         3                         4</u>

\|AD ADMIT                  61 ANKLE 2 views          89 OUTPT PHARMACY (30 DAY 

\|21 Ad Lib                 62 Chest PA&LAT           90 OTHER ORDERS...        

222 Bed Rest / BRP         SD RTC                 91 EKG                    

\|23 Ambulate TID           63 KNEE 2 VIEWS           C+ CALCIUM                

\|24 Up in Chair TID                                  87 Nasal                  

\| HOB up                 71 CHEM 7                 98 Text Only Order        

\|30 PATIENT CARE...        72 CHEM 20                99 Word Processing Order  

\+31 Condom Catheter                                  100Pulmonary Consult      

\|32 Guaiac Stools                                                              

+         + Next Screen  - Prev Screen  ?? More Actions                      \>\>\>

    Menu Items                Text or Header            Row

Edit: ITEM   Items or Text 

Select Item(s): Non-VA Meds

ITEM: PSH OERR//  

DISPLAY TEXT: Non-VA Meds// ç===== You would either remove this or add (Documentation) at the end.

### Configuring Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32a and the accompanying patches introduce several new parameters. The parameters are listed below.

#### Consults Parameters

The integrated Consult Toolbox (CTB) features of CPRS GUI v32a are disabled by default. Sites and IT staff are requested to leave the features as disabled. Please avoid using the following menu/options.

- DST Edit URLs for DST/CTB option of the CPRS Configuration (IRM) menu \[OR PARAM IRM MENU\]
- DST GUI Consults DST/CTB Configuration option of the GUI Parameters option on the CPRS Configuration (Clin Coord) menu \[OR PARAM COORDINATOR MENU\]

The CTB feature set in CPRS GUI will be nationally configured and enabled by the release of VistA patch OR\*3.0\*553. OR\*3.0\*553 is also following a waved deployment (managed by the CTB Implementation Team) and will be installed at each facility approximately two weeks after the installation of CPRS v32a.

This VistA patch approach is being used to ensure that all VAMCs are using the same configuration for CTB.

#### TIU Parameter for Required Fields for Templates

CPRS v32a added some new features to help users fill out templates with required fields. Sites are not required to use the additional highlighting for required fields. The parameter TIU REQUIRED FIELDS DISABLE enables sites to turn these features on or off. The parameter may be set at the Division and System levels. Individual users may also enable or disable this feature for themselves via the Tools \> Options \> Notes \> Required Fields check or uncheck the box labeled “Highlight Required Fields without Value”.

#### Unflagging Parameters

The parameters below enable sites to configure the new unflagging features.

> **NOTE:** Remember that if unflagging restrictions are in place, the following can unflag an order:

- ORES keyholders
- The user the flagged the order
- The recipients of the flag
- User as defined by the site using the Order Unflagging Key Setup option.

CPRS can now restrict the ability to unflag an order to users holding specified security keys (e.g., PSORPH, ORELSE, etc.). The following parameters affecting the unflagging restrictions are as follows:

- OR FLAG ORDER EXPIRE DEFAULT: This parameter defines the number of hours before sending a notification to the user who flagged the order to let them know it was not unflagged.
- OR UNFLAGGING RESTRICTIONS: When CPRS v32a is installed, the parameter OR UNFLAGGING RESTRICTIONS is set to YES at the package level, meaning the new restrictions are enabled. As stated above, if sites want to return to all users being able to unflag an order, site should set this parameter to NO at the System level, which will affect the entire site and unflagging will function as it did before CPRS v32a.
- OR UNFLAGGING MESSAGE: When a user is not authorized to unflag an order, the standard error message “You are not authorized to unflag this order based on your security keys and the order type” is displayed to the user. If sites want to add some text to the error message, they may enter the additional text at the SYSTEM or DIVISION level of this parameter.
- Order Unflagging Key Setup: Sites use this parameter to define which key can unflag orders in a specific display group. Each display group must be set with the keys that can unflag orders for that display group.

> To allow any other user to unflag orders, sites can set up those keyholders using the OR UNFLAGGING KEY SET UP menu option. To access this option,

1.  Go to GUI Parameters Option, GUI Order Flagging/Unflagging Setup, KEY    Order Unflagging Key Setup.
2.  Select the DISPLAY GROUP NAME.
3.  At Select MEMBER prompt, press \<Enter\>.
4.  At the MIXED NAME prompt, ensure the entry is correct and press \<Enter\>.
5.  At the SHORT NAME prompt, ensure the entry is correct and press \<Enter\>.
6.  At the DEFAULT DIALOG prompt, ensure the entry is correct and press \<Enter\>.
7.  At the SELECT SECURITY prompt, type the security key you want to allow to unflag orders in this specific display group, and press \<Enter\>.
8.  When prompted Are you adding 'ORELSE' as a new SECURITY KEY? No// Y (Yes), type Y and press \<Enter\>.
9.  Add more keys if needed.
10. Repeat steps 2-9 as needed for different display groups until correctly configured.

Below is an example of adding some keys to the Outpatient Medications display group.

\<CPM\> Select GUI Order Flagging/Unflagging Setup \<\*\*CPRS32ADEV\*\*\> Option: KEY O  
rder Unflagging Key Setup  
Select DISPLAY GROUP NAME: OUTPATIENT MEDICATIONS  
Select MEMBER:  
MIXED NAME: Out. Meds//  
SHORT NAME: O RX//  
DEFAULT DIALOG: PSO OERR//  
Select SECURITY KEY: ORELSE  
Are you adding 'ORELSE' as a new SECURITY KEY? No// Y (Yes)  
Select SECURITY KEY: PSORPH

Are you adding 'PSORPH' as a new SECURITY KEY? No// Y (Yes)

Select SECURITY KEY: ?

Answer with SECURITY KEY

Choose from:

PSORPH

ORELSE

#### Additional Signers

CPRS added the OR CPRS USER CLASS EXCLUDE parameter to assign a single User Class whose members will be excluded from displaying as Additional Signers. If your site wants to limit those who display as Additional Signers, you may add the users to an existing User Class or add users to a new User Class that you create. Then, the User Class is added to the OR CPRS USER CLASS EXCLUDE parameter. Those in the User Class should then be excluded from the lists.

Be careful not to exclude users that should display.

#### Setting Default Nature of Order

For orders that will be released by a nurse, for example, CPRS has several different options as the reason to Release to Service, such as Verbal, Telephone, Policy. Previously, the reason defaulted to Verbal. Sites can now choose how that should default. Sites can set the parameter OR NATURE DEFAULT to choose either Verbal, Telephone, or Policy. For example, the site may put Telephone and then that will display as the selection by default, although users can still select another option, such as Policy or Verbal. Sites may also choose to leave the parameter blank, thereby forcing the user to select one of the choices when the dialog displays. This parameter may be set at the System and User levels.

#### Similar Names

CPRS has a feature that displays a list of similar names for the user to choose from when users are trying to select a name, such as when looking for additional signers or selecting the encounter provider. The OR SIMILAR NAMES ENABLED parameter gives sites the opportunity to enable or disable the similar names features. This parameter may be set at the System and User levels. The similar names feature is turned on when CPRS v32a is installed.

#### Default Surrogate Settings

CPRS added some surrogate features. The parameter ORQQXQ SURROGATE DEFAULTS enables the user to define if a default will be used and the default surrogate period. The default surrogate period can be set at a period between 1 and 30 days. However, a default is not necessary. This parameter may be set at the System, Division, and User levels.

## Reenable Access or CPRS for All Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, sites should perform testing until they are comfortable to let all CPRS users back on the system.

> **NOTE:** Once you have removed the lock on the OR CPRS GUI CHART option, any names of users that were temporarily removed from selection lists in CPRS GUI should display. However, you may notice the names of terminated users are still displaying. This issue was identified during previous test installations and will be corrected in a follow-up patch.

To reenable access to CPRS, do the following:

1.  When facility staff are ready for all users to access CPRS GUI, delete the key value from the LOCK field of OR CPRS GUI CHART.

\<CPM\> Select Menu Management Option: Edit options

Select OPTION to edit: OR CPRS GUI CHART CPRSChart version 1.32.114.1

NAME: OR CPRS GUI CHART//

MENU TEXT: CPRSChart version 1.32.114.1 Replace

PACKAGE:

OUT OF ORDER MESSAGE:

LOCK: OR CPRS TESTER// @

SURE YOU WANT TO DELETE? Y (Yes)

REVERSE/NEGATIVE LOCK:^

## Change to Online Help Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CPRS v32a is using a new type of Help system. There will be only one file for the help (cprs.chm). This is a change from the previous type of help file.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the event of a catastrophic failure, the Area Manager may make the decision to backout the patch and rollback any necessary database changes. The Area Manager, working with site personnel, tier 2 product support, and the development team will be involved in the decision. However, the Area Manager will make the final decision.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If backing out CPRS v32a becomes necessary, sites can use the build created by the CPRS Development Team to back out the patches and return the system to the pre-installation state. The same team that placed the GUI executable on the systems will need to replace the GUI with the previous version (CPRS v31 MA). The version number should be 1.31.312.1.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites should consider how backing out CPRS v32a might affect the system. Sites should consult with the development team and support staff.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS SQA team tested the CPRS v32a software. Test sites also verified that the changes in CPRS functioned correctly.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because CPRS is used by clinical staff on a regular basis, backing out CPRS v32a should only be considered because of a catastrophic error.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To be added.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ultimate responsibility for backing out CPRS v32a lies with the Area Manager.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To backout the CPRS v32a changes, the development team would make the backout build OR_3_539_V32A_V114_BACKOUT.KID available to sites for installation.

To backout the GUI, the personnel responsible for deploying the GUI will need to replace the CPRS v32a executable with the CPRS 31 Mission Act executable and correct the necessary icons (on VACS servers, Citrix servers, desktops, etc.) to point to the CPRS 31Mission Act executable, whether that entails replacing the icon or simply repointing it to the correct executable.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the back-out was successful, check the OPTION (#19) file for option OR CPRS GUI CHART and ensure the version is set to 1.31.312.1.

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