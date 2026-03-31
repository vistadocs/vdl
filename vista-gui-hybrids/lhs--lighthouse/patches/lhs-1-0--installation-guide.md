---
title: LHS*1*0 Lighthouse Deployment, Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Lighthouse
app_code: LHS
app_name: Lighthouse
section: GUI
app_status: active
pkg_ns: LHS
patch_ver: 1
patch_id: LHS*1*0
group_key: "LHS:LHS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - back
  - span
  - installation
  - procedure
  - patch
  - rollback
  - access
  - proxy
page_count: 0
word_count: 4178
section_count: 32
table_count: 8
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Lighthouse_LHS/LHS_1_0_DIBRG.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Lighthouse_LHS/LHS_1_0_DIBRG.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=240"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Lighthouse 1.0

  Deployment, Installation, Back-Out, and Rollback Guide (DIBR)
---

![](lhs-1-0-lighthouse-deployment-installation-back-out-and-rollback-guide/001.png)

August 2021

LHS\*1.0\*0

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc79143165" class="anchor"></span>Table : Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/09/2021</td>
<td>1.0</td>
<td><p>LHS*1.0*0:</p>
<ul>
<li><p><strong><u>4.1.1 Mandatory Action</u></strong> must be completed before continuing with the installation</p></li>
<li><p>Approved on 08/06/2021</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
</tbody>
</table>

<span id="_Toc79143165" class="anchor"></span>Table : Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

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
    - [Mandatory Action](#mandatory-action)
    - [CONNECTOR PROXY Creation](#connector-proxy-creation)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [KIDS Installation](#kids-installation)
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
    - [Delete the LHS RPC CONTEXT Option:](#delete-the-lhs-rpc-context-option)
    - [Delete LHS CHECK OPTION ACCESS Remote Procedure:](#delete-lhs-check-option-access-remote-procedure)
    - [Delete the LHSRPC Routine](#delete-the-lhsrpc-routine)
    - [Deactivate the LHS, CONNECTOR PROXY](#deactivate-the-lhs-connector-proxy)
    - [LHS, APPLICATION PROXY](#lhs-application-proxy)
  - [KIDS Back-out](#kids-back-out)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the patch LHS\*1.0\*0, as well as how to back-out the product and rollback to a previous version or data set.
This patch is being deployed initially to the COVID Patient Manager (CPM) pilot program test sites and will be evaluated for national deployment.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the LHS\*1.0\*0 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for LHS\*1.0\*0.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch is intended for a fully patched VistA system.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID | Team                          | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|-----------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | Project Team and Development Team | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                 |                                  |
| 2      | Development Team                  | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment                           |                                  |
| 3      | Enterprise Operations (EO)        | Deployment       | Test for operational readiness                                                                                      |                                  |
| 4      | Development Team                  | Deployment       | Execute deployment                                                                                                  |                                  |
| 5      | Development Team                  | Installation     | Plan and schedule installation                                                                                      |                                  |
| 6      | Project Team                      | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                       |                                  |
| 7      | Development Team                  | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |                                  |
| 8      | Project Team                      | Post Deployment  | Hardware, Software and System Support                                                                               |                                  |

<span id="_Toc79143166" class="anchor"></span>Table : Site Preparation

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment for LHS\*1.0\*0 is planned as a single VistA Package rollout.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for approximately one day.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the LHS\*1.0\*0 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch LHS\*1.0\*0 is to be deployed to the COVID Patient Manager (CPM) Pilot sites and upon acceptance will be nationally released.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The test sites for the CPM testing are:

- Tampa, FL
- Philadelphia, PA
- Bronx, NY

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps                                  | Owner                                                                             |
|----------------|---------------------------|---------------------------------------------|----------------------------------------------------|---------------------------------------------------------------------------------------|
| Tampa          | N/A                       | N/A                                         | Install patch and create VistALink Connector Proxy | Information Resource Management (IRM) or Enterprise Service Line (ESL) representative |
| Philadelphia   | N/A                       | N/A                                         | Install patch and create VistALink Connector Proxy | IRM or ESL                                                                            |
| Bronx          | N/A                       | N/A                                         | Install patch and create VistALink Connector Proxy | IRM or ESL                                                                            |

<span id="_Toc79143167" class="anchor"></span>Table : Facility-Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      |                |                     |           |

<span id="_Toc79143168" class="anchor"></span>Table : Hardware Specifications

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   |           |             |                   |                  |           |

<span id="_Toc79143169" class="anchor"></span>Table : Software Specifications

Please see the Roles and Responsibilities table in section <u>2</u> for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software | Make | Version | Configuration | Manufacturer | Other |
|-----------------------|----------|-------------|-------------------|------------------|-----------|
| N/A                   |          |             |                   |                  |           |

<span id="_Toc79143170" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in section <u>2</u> above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The sites that are participating in the field testing of the CPM application will use the Patch Tracking message in Outlook to communicate with the Lighthouse team.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the patch LHS\*1.0\*0, which is tracked nationally for all VAMCs in the NPM in Forum. Forum automatically tracks the patches as they are installed in the different VAMC production systems. One can run a report in Forum to identify when the patch was installed in the VistA production at each site, and by whom. A report can also be run, to identify which sites have not currently installed the patch in their VistA production system. Therefore, this information does not need to be manually tracked in the chart below.

| Activity | Day        | Time | Individual who completed task |
|----------|------------|------|-------------------------------|
| Deploy   | Release    | Any  | Site Support Personnel        |
| Install  | Release    | Any  | Site Support Personnel        |
| Back-Out | Contingent | Any  | Site Support Personnel        |

<span id="_Toc79143171" class="anchor"></span>Table : Associated Patch Files

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mandatory Action

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The site Information Resource Management (IRM), Enterprise Service Line (ESL), or designated representative must contact the Lighthouse team through the <LHSVISTASUPPORT@VA.GOV> mail group to get the access/verify code for CONNECTOR PROXY for their site. This will be sent encrypted via Outlook.

> **NOTE:** Complete the mandatory action above before proceeding with the LHS\*1.0\*0 installation.

### CONNECTOR PROXY Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create the Lighthouse CONNECTOR PROXY using the FOUNDATIONS MANAGEMENT \[XOBU SITE SETUP MENU\] option on the Operations Management menu \[XUSITEMGR\].

Example:

\<\<\< VistALink Parameters \>\>\>

VistALink Version: 1.6 Heartbeat Rate: 180 Latency Delta: 180

\<\<\< VistALink Listener Status Log \>\>\>

ID Box-Volume Port Status Status Date/Time

Configuration

Enter ?? for more actions

SP Site Parameters SL Start Listener

CFG Manage Configurations STP Stop Listener

CP Enter/Edit Connector Proxy User SB Start Box

RE Refresh CU Clean Up Log

CM Connection Manager

Select Action:Quit// <span class="mark">CP</span> Enter/Edit Connector Proxy User

Enter NPF CONNECTOR PROXY name : <span class="mark">LHS,CONNECTOR PROXY</span>

Are you adding LHS,CONNECTOR PROXY as a new NEW PERSON (the 198970TH)?

No// <span class="mark">Y (Yes)</span>

Checking SOUNDEX for matches.

\<different potential matches for each site\>

Type \<Enter\> to continue or '^' to exit: ^

Do you still want to add this entry: NO//<span class="mark">Y</span>

Want to edit ACCESS CODE (Y/N): <span class="mark">Y</span>

Enter a new ACCESS CODE \<Hidden\>: <span class="mark">\*\*\*\*\*\*\*\*\*\*\*</span> \<Use ACCESS CODE provided

to your site\>

Please re-type the new code to show that I have it right: <span class="mark">\*\*\*\*\*\*\*\*\*\*\*</span>

OK, Access code has been changed!

The VERIFY CODE has been deleted as a security measure.

You will need to enter a new VERIFY code so the user can sign-on.

Want to edit VERIFY CODE (Y/N): <span class="mark">Y</span>

Enter a new VERIFY CODE: <span class="mark">\*\*\*\*\*\*\*\*\*\*\*\*</span> \<Use VERIFY CODE provided to your

site\>

Please re-type the new code to show that I have it right: <span class="mark">\*\*\*\*\*\*\*\*\*\*\*\*</span>

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LHS\*1.0\*0 will be transmitted via PackMan message, and therefore does need to be downloaded separately.

| File | Description |
|------|-------------|
| N/A  |             |

<span id="_Toc68708217" class="anchor"></span>Table : Routines

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LHS\*1.0\*0 modifies the VistA database. All changes can be found on the NPM documentation for this patch.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are needed for the LHS\*1.0\*0 installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Cron scripts are needed for the LHS\*1.0\*0 installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following staff will need access to the PackMan message containing the LHS\*1.0\*0 patch or to FORUM’s NPM for downloading the patch.

The software is to be installed by the site’s or region’s designated: VA OIT IT OPERATIONS SERVICE, Enterprise Service Lines, VistA Applications Division2. Additionally, access to the VistA Option FOUNDATION MANAGEMENT \[XOBU SITE SETUP MENU\] is required.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this build. Then select the INSTALL/CHECK MESSAGE PackMan option to load the build.
2.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name.

        (ex. LHS 1.0)

        Note: Using \<spacebar\>\<enter\> will not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build.
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup, the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
        1.  At the Installation option menu, select Backup a Transport Global
        2.  At the Select INSTALL NAME prompt, enter LHS 1.0
        3.  When prompted for the following, enter B for Build.

            Select one of the following:

            B Build

            R Routines

            Enter response: Build
        4.  When prompted “Do you wish to secure your build? NO//”, press \<enter\> and take the default response of NO.
        5.  When prompted with, “Send mail to: Last name, First Name”, press \<enter\> to take default recipient. Add any additional recipients.
        6.  When prompted with “Select basket to send to: IN//”, press \<enter\> and take the default IN mailbox or select a different mailbox.
    3.  You may also elect to use the following options:
        1.  Print Transport Global – This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all the components of this patch, such as routines, DDs, templates, etc.
    4.  Select the Install Package(s) option and choose the patch to install.
        1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
        2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
        3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the routine checksums in the table below.

| Routine | Before Checksum | After Checksum | Patch List |
|---------|-----------------|----------------|------------|
| LHSRPC  | NEW             | B386439        | \*\*0\*\*  |

RoutinesThis table shows the list of routines and their before checksums, after checksums, and patch list associations.

> **NOTE:** The Post-install routine LHSPST1 will add “LHS,APPLICATION PROXY” to the NEW PERSON file (#200). LHSPST1 is deleted automatically when the patch is installed.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No system configuration changes are required for this patch.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No reconfiguration of the VistA database, memory allocations or other resources is necessary.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although it is highly unlikely that problems with this patch will occur as there are no Data Dictionaries or data modifications associated with the LHS\*1.0\*0 patch, a back-out decision due to other considerations could occur.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is necessary to determine if LHS\*1.0\*0 requires a wholesale back-out or if concerns can be resolved through a new version of the patch or a follow up patch addressing concerns caused by LHS\*1.0\*0. A new version of LHS\*1.0\*0 or a follow up patch depends on whether the concerns are caught before or after national release of LHS\*1.0\*0.

A wholesale back-out of the patch will still require a new version (if prior to national release) or a subsequent patch (after national release).

If the back-out is post-release of patch LHS\*1.0\*0, this patch should be assigned the status of “Entered in Error” in Forum’s NPM.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out process would be executed at normal, rather than raised job priority, and is expected to have no significant effect on total system performance. Subsequent to the reversion, the performance demands on the system would be unchanged.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch does not include any new functionality in VistA and the only purpose is to provide access to data for the CPM project. There is one new Remote Procedure \[LHS CHECK OPTION ACCESS\] that is used to determine if a CPM user has access to the \[OR CPRS GUI CHART\] option.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Criteria for back-out includes, but is not limited to, the project’s cancelation, the requested CPM changes are no longer desired by VA, or LHS\*1.0\*0 produces catastrophic problems.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no risks with this back-out procedure.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The release coordinator, portfolio director, and Health Product Support have the authority to initiate a back-out decision. This should be done in consultation with the development team.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out procedure for VistA applications is complex and not a “one size fits all” solution. The general strategy for a VistA back-out is to repair the code with a follow-up patch. However, this patch only includes one new RPC and does not install any new functionality through Data Dictionaries.

The development team recommends that sites log a ticket if it is a nationally released patch. If not, the site should contact the Enterprise Program Management Office (EPMO) team directly for specific solutions to their unique problems.

The LHS\*1.0\*0 patch includes the following build components:

- Options
  - LHS RPC CONTEXT
- New Person
  - LHS,APPLICATION PROXY
  - LHS,CONNECTOR PROXY
- Remote Procedure
  - LHS CHECK OPTION ACCESS

The LHS RPC CONTEXT Option and the LHS CHECK OPTION ACCESS Remote Procedure can be deleted through the FileMan \[ENTER OR EDIT FILE ENTRIES\] option. The following will need to be executed from the programmer’s prompt (User input depicted below in *bold italicized* font):

### Delete the LHS RPC CONTEXT Option:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*D P^DI*

Select OPTION: *ENTER OR EDIT FILE ENTRIES*

Input to what File: OPTION// *19* OPTION (11237 entries)

EDIT WHICH FIELD: ALL// *ALL*

Select OPTION NAME: *LHS RPC CONTEXT* LHS RPC CONTEXT

NAME: LHS RPC CONTEXT// *@*

SURE YOU WANT TO DELETE THE ENTIRE 'LHS RPC CONTEXT' OPTION? *Y* (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// *Y*

(Yes)

WHICH DO YOU WANT TO DO? --

1\) DELETE ALL SUCH POINTERS

2\) CHANGE ALL SUCH POINTERS TO POINT TO A DIFFERENT 'OPTION' ENTRY

CHOOSE 1) OR 2): *1*

DELETE ALL POINTERS? Yes// *Y* (Yes)

(DELETION WILL OCCUR WHEN YOU LEAVE 'ENTER/EDIT' OPTION)

### Delete LHS CHECK OPTION ACCESS Remote Procedure:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*D P^DI*

Select OPTION: *ENTER OR EDIT FILE ENTRIES*

Input to what File: REMOTE PROCEDURE// *8994* REMOTE PROCEDURE

(4276 entries)

EDIT WHICH FIELD: ALL// *ALL*

Select REMOTE PROCEDURE NAME: *LHS CHECK OPTION ACCESS*

NAME: LHS CHECK OPTION ACCESS Replace *@*

SURE YOU WANT TO DELETE THE ENTIRE 'LHS CHECK OPTION ACCESS' REMOTE PROCEDURE

? *Y* (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'OPTION' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// *Y*

(Yes)

WHICH DO YOU WANT TO DO? --

1\) DELETE ALL SUCH POINTERS

2\) CHANGE ALL SUCH POINTERS TO POINT TO A DIFFERENT 'REMOTE PROCEDURE' ENTRY

CHOOSE 1) OR 2): *1*

DELETE ALL POINTERS? Yes// *Y* (Yes)

(DELETION WILL OCCUR WHEN YOU LEAVE 'ENTER/EDIT' OPTION)

### Delete the LHSRPC Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Routine is LHSRPC and this routine has no dependencies and can be safely deleted using the Delete Routines option under Routine Tools menu.

*D ^XUP*

Select OPTION NAME: EVE

1 EVE Systems Manager Menu

2 EVET BLOCK/UNBLOCK DOWNLOAD Block/unblock Vet Download

3 EVET CHECK INCOMING Check for incoming responses from Health eVet

4 EVET DAILY DOWNLOAD ACTIVITY Daily download activity for date

5 EVET EMAIL DOWNLOAD REPORT Email weekly download report

Press \<Enter\> to see more, '^' to exit this list, OR

CHOOSE 1-5: *1* EVE Systems Manager Menu

Core Applications ...

Device Management ...

FM VA FileMan ...

Menu Management ...

Programmer Options ...

Operations Management ...

Spool Management ...

Information Security Officer Menu ...

Taskman Management ...

User Management ...

Application Utilities ...

Capacity Planning ...

Manage Mailman ...

\<CPM\> Select Systems Manager Menu \<TEST ACCOUNT\> Option: *Programmer Options*

KIDS Kernel Installation & Distribution System ...

NTEG Build an 'NTEG' routine for a package

PG Programmer mode

Calculate and Show Checksum Values

Delete Unreferenced Options

Error Processing ...

Global Block Count

List Global

Map Pointer Relations

Number base changer

Routine Tools ...

Test an option not in your menu

Verifier Tools Menu ...

\<CPM\> Select Programmer Options \<TEST ACCOUNT\> Option: *Routine Tools*

%Index of Routines

Check Routines on Other CPUs

Compare local/national checksums report

Compare routines on tape to disk

Compare two routines

Delete Routines

First Line Routine Print

Flow Chart Entire Routine

Flow Chart from Entry Point

Group Routine Edit

Input routines

List Routines

Load/refresh checksum values into ROUTINE file

Output routines

Routine Edit

Routines by Patch Number

Variable changer

Version Number Update

\<CPM\> Select Routine Tools \<TEST ACCOUNT\> Option: *Delete Routines*

ROUTINE DELETE

All Routines? No =\> *No*

Routine: *LHSRPC*

Routine:

1 routine

1 routines to DELETE, OK: NO// *Yes*

LHSRPC

Done.

### Deactivate the LHS, CONNECTOR PROXY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LHS,CONNECTOR PROXY cannot be deleted directly but it can be deactivated using the Deactivate a User \[XUSERDEACT\] option.

Deactivate LHS,CONNECTOR PROXY user:

Select Systems Manager Menu \<TEST ACCOUNT\> Option: *User Management*

Add a New User to the System

Grant Access by Profile

Edit an Existing User

Deactivate a User

Reactivate a User

List users

User Inquiry

Switch Identities

File Access Security ...

Clear Electronic signature code

Electronic Signature Block Edit

List Inactive Person Class Users

Manage User File ...

OAA Trainee Registration Menu ...

Person Class Edit

Reprint Access agreement letter

\<CPM\> Select User Management \<TEST ACCOUNT\> Option: *Deactivate a User*

Select USER to be deactivated: *LHS,CONNECTOR PROXY*

View/Print User Inquiry Data? Yes// *NO*

DEACTIVATE A USER

NAME: LHS,CONNECTOR PROXY

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Disable User: *YES*

TERMINATION DATE: *TODAY*

Termination Reason: *PROJECT TERMINATED*

DELETE ALL MAIL ACCESS: *YES*

DELETE KEYS AT TERMINATION: *YES*

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: *Save*

LHS,CONNECTOR PROXY will be deactivated now. Do you wish to proceed? YES// *YES*

### LHS, APPLICATION PROXY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LHS,APPLICATION PROXY is a special type of user and cannot be deleted or deactivated. However, since it does not have any valid options assigned, or Access/Verify codes, it cannot be used directly and causes no threat when left on the system.

## KIDS Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrators will need to use the PackMan function INSTALL/CHECK MESSAGE. Check MailMan messages for the backup message sent by the Backup a Transport Global function executed prior to the patch install. (See section <u>4.8.1</u>, Step 2B; this must be done before the patch is installed).

1.  In VistA MailMan, select the message shown below:
    1.  Backup of LHS\*1.0\*0 install on \<mm, dd, yyyy\> \<user name\>
2.  Select the Xtract PackMan option.
3.  Select the Install/Check Message option.
4.  Enter Yes at the prompt.
5.  Enter No at the backup prompt. There is no need to back up the backup.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Successful back-out is confirmed upon completion of the steps outlined in section <u>5.6 Back-Out Procedure</u>. Each step will provide confirmation of success; however, visual confirmation can be performed using the FileMan \[INQUIRE TO FILE ENTRIES\] Option for verification of the file entries.

*D P^DI*

Select OPTION: *INQUIRE TO FILE ENTRIES*

Output from what File: REMOTE PROCEDURE// *8994* (4275 entries)

Select REMOTE PROCEDURE NAME: *LHS RPC CONTEXT* <span class="mark">??</span>

Select OPTION: *INQUIRE TO FILE ENTRIES*

Output from what File: REMOTE PROCEDURE// *19* OPTION (11236 entries)

Select OPTION NAME: *LHS CHECK OPTION ACCESS* <span class="mark">??</span>

Select OPTION: *INQUIRE TO FILE ENTRIES*

Output from what File: OPTION// *200* NEW PERSON (1541 entries)

Select NEW PERSON NAME: *LHS,CONNECTOR PROXY*

Another one:

Standard Captioned Output? Yes// *Yes* (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// *N* - No record number (IEN), no Computed

Fields

Display Audit Trail? No// *No* NO

NAME: LHS,CONNECTOR PROXY ACCESS CODE: \<Hidden\>

DELETE ALL MAIL ACCESS: YES DELETE KEYS AT TERMINATION: YES

DISUSER: YES TERMINATION DATE: AUG 05, 2021

Termination Reason: PROJECT TERMINATED

DATE VERIFY CODE LAST CHANGED: FEB 23,2021

DATE ENTERED: FEB 23, 2021 CREATOR: MAILMAN

Entry Last Edit Date: AUG 05, 2021 NAME COMPONENTS: 200

SIGNATURE BLOCK PRINTED NAME: CONNECTOR PROXY LHS

MULTIPLE SIGN-ON: ALLOWED

User Class: CONNECTOR PROXY ISPRIMARY: Yes

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. The only data changes in this patch are specific to the operational software and platform settings. These data changes are covered in section <u>5.6 Back-Out Procedure</u>.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for LHS\*1.0\*0.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for LHS\*1.0\*0.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for LHS\*1.0\*0.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for LHS\*1.0\*0.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for LHS\*1.0\*0.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for LHS\*1.0\*0.