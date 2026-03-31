---
title: HBH*1*32 HBPC Deployment, Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: HBPC
app_name: Home Based Primary Care
section: CLI
app_status: active
pkg_ns: HBH
patch_ver: 1
patch_id: HBH*1*32
group_key: "HBPC:HBH:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - hbhc
  - provider
  - table
  - contents
  - site
  - back
  - edit
  - span
  - installation
  - hbpc
page_count: 0
word_count: 7637
section_count: 31
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_1_0_p32_dibr_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Home_Based_Pri_Care_(HBPC)/hbh_1_0_p32_dibr_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=68"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Home Based Primary Care (HBPC)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](hbh-1-32-hbpc-deployment-installation-back-out-and-rollback-guide/001.png)

August 2021

HBH\*1.0\*32

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc77590008" class="anchor"></span>Table : Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
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
<td>08/03/2021</td>
<td>1.0</td>
<td><p>HBH*1.0*32:</p>
<ul>
<li><p>Updated <strong><u>Table 7: Routines</u></strong></p></li>
<li><p>AC approval received 07/16/2021</p></li>
<li><p>The unredacted version of this document is available in the SOFTWARE library for viewing <mark>REDACTED</mark> information</p></li>
</ul></td>
<td>Liberty ITS</td>
</tr>
</tbody>
</table>

<span id="_Toc77590008" class="anchor"></span>Table : Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the *Deployment, Installation, Back-out, and Rollback Guide* for new products going into the VA Enterprise. The guide includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the *Deployment, Installation, Back-out, and Rollback Guide* is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

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
    - [KIDS Installation](#kids-installation)
    - [Client Installation](#client-installation)
  - [Installation Verification Procedure](#installation-verification-procedure)
    - [KIDS Verification](#kids-verification)
    - [Client Verification](#client-verification)
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
    - [KIDS Back-Out](#kids-back-out)
    - [Client Back-Out](#client-back-out)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install HBH\*1.0\*32 as well as how to back-out the product and rollback to a previous version or data set.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom HBH\*1.0\*32 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch must be installed after HBH\*1.0\*25 and HBH\*1.0\*27.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HBH\*1.0\*32 and the associated MUMPS patch are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. HBH\*1.0\*32 utilizes existing nationally released security controls to control access.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multiple entities oversee decision making for the deployment, installation, back-out and rollback of HBH\*1.0\*32. Application Coordinators approve deployment and install from an OIT perspective. If an issue with the software arises, then the facility Chief Information Officer (CIO) and other site leadership will meet along with input from Patient Safety, Health Product Support (HPS), and regional leadership to initiate a back out and rollback decision of the software. The following table provides HBH\*1.0\*32 information.

<table>
<caption><p><span id="_Toc77590009" class="anchor"></span>Table : Facility-Specific Features</p></caption>
<colgroup>
<col style="width: 36%" />
<col style="width: 19%" />
<col style="width: 44%" />
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
<td>Site personnel in conjunction with information technology (IT) support – which may be local or regional.</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors)</td>
</tr>
<tr class="even">
<td>Site personnel in conjunction with IT support – which may be local or regional.</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
</tr>
<tr class="odd">
<td>Site personnel.</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="even">
<td>Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the Kernel Installation and Distribution System (KIDS) build.</td>
<td>Deployment</td>
<td>Execute deployment</td>
</tr>
<tr class="odd">
<td>Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the KIDS.</td>
<td>Installation</td>
<td>Plan and schedule installation</td>
</tr>
<tr class="even">
<td>N/A – will work under the VistA authority to operate (ATO) and security protocols.</td>
<td>Installation</td>
<td>Ensure that ATO and certificate authority security documentation is in place</td>
</tr>
<tr class="odd">
<td>N/A – no equipment is being added.</td>
<td>Installation</td>
<td>Validate through facility point of contact (POC) to ensure that IT equipment has been accepted using asset inventory processes</td>
</tr>
<tr class="even">
<td>N/A – no new functionality is being introduced.</td>
<td>Installations</td>
<td>Coordinate training</td>
</tr>
<tr class="odd">
<td>Facility CIO and IT support – which may be local or regional.</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
</tr>
<tr class="even">
<td><p>Hardware and System support – no changes.</p>
<p>Software support will be the HPS Clinical Sustainment team.</p></td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
</tr>
</tbody>
</table>

<span id="_Toc77590009" class="anchor"></span>Table : Facility-Specific Features

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release HBH\*1.0\*32, the patch will be released via the National Patch Module. At this point, it will be available for installation and deployment at all sites from the SOFTWARE library referenced in the accompanying patch description.

Scheduling of test/mirror installs, testing, and deployment to production will be at the site’s discretion. It is anticipated that there will be a 30-day compliance period.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch installation should occur after the AITC transmission for the month of July has been completed.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the HBH\*1.0\*32 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HBH\*1.0\*32 will be deployed to each VistA instance.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, HBH\*1.0\*32 will be deployed to all VistA systems.

The Production IOC testing sites are:

- Big Spring, Texas
- Buffalo, New York

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites have been instructed to perform two FileMan searches. These searches will determine the presence of the following two conditions:

1.  If any providers are defined for more than one active HBHC provider number
2.  If an active HBHC provider number is defined for more than one provider.

    A visual inspection is needed to determine if either of the two conditions are present. If the FileMan searches have not yet been performed, they are listed below:
1.  Search to determine if any provider is defined with more than one active HBPC provider number.

> **NOTE:** Before inactivating one of the numbers, determine if these are different providers who have the same name.

Figure : Example search for providers with more than one active HBPC provider number

![](hbh-1-32-hbpc-deployment-installation-back-out-and-rollback-guide/002.png)

2.  FileMan search to determine if active HBHC provider numbers are defined for more than one provider.

Figure : Example search for active provider numbers defined for more than one provider

![](hbh-1-32-hbpc-deployment-installation-back-out-and-rollback-guide/003.png)

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      |                |                     |           |

<span id="_Toc77590010" class="anchor"></span>Table : Hardware Specifications

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   |           |             |                   |                  |           |

<span id="_Toc77590011" class="anchor"></span>Table : Software Specifications

Please see the Roles and Responsibilities table in section <u>2</u> for details about who is responsible for preparing the site to meet these hardware specifications.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software | Make | Version | Configuration | Manufacturer | Other |
|-----------------------|----------|-------------|-------------------|------------------|-----------|
| N/A                   |          |             |                   |                  |           |

<span id="_Toc77590012" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in section <u>2</u> above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HBH\*1.0\*32 will be deployed using the standard method of patch release from the National Patch Module. When HBH\*1.0\*32 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

| Activity | Day              | Time | Individual who completed task |
|----------|------------------|------|-------------------------------|
| Deploy   | National Release | Any  | Site Support Personnel        |
| Install  | National Release | Any  | Site Support Personnel        |
| Back-Out | Contingent       | Any  | Site Support Personnel        |

<span id="_Toc77590013" class="anchor"></span>Table : Associated Patch Files

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All previously released HBPC patches must be installed on the VistA system before installing HBH\*1.0\*32.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HBH\*1.0\*32 must be installed on the VistA System. This patch must be installed by the compliance date.

Users of the Home Based Primary Care (formerly called HBHC) options should be off the system during patch installation. This patch may be installed with other users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release includes documentation that can be obtained from the SOFTWARE library or Veterans Documentation Library (VDL).

SOFTWARE: https://download.<span class="mark">REDACTED</span>/SOFTWARE

VDL: <https://www.va.gov/vdl/application.asp?appid=68>

| File                 | Description                                            |
|----------------------|--------------------------------------------------------|
| HBH_1_0_P32_DIBR.pdf | Deployment, Installation, Back-out, and Rollback Guide |
| HBH_UM.pdf           | User Manual                                            |
| HBH_TM.pdf           | Technical Manual                                       |
| HBH_SG.pdf           | Security Guide                                         |
| HBH_1_0_P32_RN.pdf   | Release Notes                                          |

<span id="_Ref76985572" class="anchor"></span>Table : Routines

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of HBH\*1.0\*32 requires the following to install:

- Programmer access to VistA instance and ability to install the KIDS build.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kids installation will take two to five minutes.

1.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu,
    1.  Select the Verify Checksums in Transport Global option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name.

        (ex. \<XXX\*X.X\*XX\> or XXXXX BUILD X.X)

        Note: Using \<spacebar\>\<enter\> will not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build.
    2.  Select the Backup a Transport Global option to create a backup message. You must use this option and specify what to backup; the entire Build or just Routines. The backup message can be used to restore the routines and components of the build to the pre-patch condition.
        1.  At the Installation option menu, select Backup a Transport Global
        2.  At the Select INSTALL NAME prompt, enter your build XXX\*#.#\*###
        3.  When prompted for the following, enter “R” for Routines or “B” for Build.

            Select one of the following:

            B Build

            R Routines

            Enter response: Build
        4.  When prompted “Do you wish to secure your build? NO//”, press \<enter\> and take the default response of “NO”.
        5.  When prompted with, “Send mail to: Last name, First Name”, press \<enter\> to take default recipient. Add any additional recipients.
        6.  When prompted with “Select basket to send to: IN//”, press \<enter\> and take the default IN mailbox or select a different mailbox.
        7.  Repeat step ii for each build in the host file.
    3.  You may also elect to use the following options:
        1.  Print Transport Global – This option will allow you to view the components of the KIDS build.
        2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all of the components of this patch, such as routines, DDs, templates, etc.
    4.  Select the Install Package(s) option and choose the patch to install.
        1.  If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer NO.
        2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer NO.
        3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer NO.

### Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the routine checksums in the table below.

| Routine  | Before Checksum | After Checksum | Patch List                              |
|----------|-----------------|----------------|-----------------------------------------|
| HBHC32EN | NEW             | 27815638       | \*\*32\*\*                              |
| HBHCADM  | 27070975        | 41220209       | \*\*2,6,8,16,24,25,32\*\*               |
| HBHCDEM  | 1728176         | 11084332       | \*\*24,32\*\*                           |
| HBHCEDSP | 92472           | 14469400       | \*\*6,8,32\*\*                          |
| HBHCFILE | 36363460        | 39629465       | \*\*2,5,6,8,9,10,16,21,24,27,32\*\*     |
| HBHCPROV | NEW             | 238504601      | \*\*32\*\*                              |
| HBHCRP2  | 30714112        | 30671664       | \*\*1,2,5,6,9,19,22,25,32\*\*           |
| HBHCRP5  | 25295403        | 25046729       | \*\*2,5,6,22,25,32\*\*                  |
| HBHCRXMT | 12007889        | 12497553       | \*\*2,6,32\*\*                          |
| HBHCUTL1 | 27175218        | 37771382       | \*\*1,2,6,9,19,24,32\*\*                |
| HBHCXMA  | 42800884        | 42324417       | \*\*1,6,9,19,24,25,32\*\*               |
| HBHCXMD  | 26724390        | 26374319       | \*\*4,6,9,10,13,19,24,25,32\*\*         |
| HBHCXMM  | 18340144        | 24009300       | \*\*24,32\*\*                           |
| HBHCXMT  | 18610987        | 19427326       | \*\*2,3,6,8,10,13,24,32\*\*             |
| HBHCXMV  | 20835749        | 24404656       | \*\*2,5,6,9,12,15,17,14,19,24,25,32\*\* |

RoutinesThis table shows the list of routines and their before checksums, after checksums, and patch list associations.

HBHC PROVIDER (#631.4) file

631.4,.01 HBHC ID 0;1 NUMBER (Required)

HBHC PROVIDER IDENTIFIER

INPUT TRANSFORM: K:X\<1!(X'?1.4N) X

LAST EDITED: MAY 01, 2021

HELP-PROMPT: Enter a number from 1 to 4 digits.

DESCRIPTION: This field represents a unique number

Assigned to each HBPC (formerly called HBHC)

provider.

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 631.4^B

1)= S ^HBHC(631.4,"B",\$E(X,1,30),DA)=""

2)= K ^HBHC(631.4,"B",\$E(X,1,30),DA)

This cross-reference represents a regular 'B'

file index of the HBHC ID (#.01) field in the

HBHC PROVIDER (#631.4) file.

631.4,1 PROVIDER NAME 0;2 POINTER TO NEW PERSON FILE (#200)

(Required)

LAST EDITED: MAY 01, 2021

HELP-PROMPT: Answer with provider name. The provider must

be pre-defined in the NEW PERSON (#200) file.

DESCRIPTION: This field represents the HBPC provider's

name in the NEW PERSON (#200) file.

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 631.4^C

1)= S ^HBHC(631.4,"C",\$E(X,1,30),DA)=""

2)= K ^HBHC(631.4,"C",\$E(X,1,30),DA)

This cross-reference represents regular 'C'

file index of HBHC Provider (631.4) file,

Name (1) field, which references New Person

\(200\) file entries.

631.4,2 DEGREE 0;3 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>15!(\$L(X)\<1) X

LAST EDITED: MAY 01, 2021

HELP-PROMPT: This field is no longer in use.

DESCRIPTION: This field is no longer in use after the

install of HBH\*1.0\*32.

631.4,3 GRADE/STEP 0;4 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>6!(\$L(X)\<3)!'(X?1.3E1"/"1.2N) X

LAST EDITED: MAY 01, 2021

HELP-PROMPT: This field is no longer in use.

DESCRIPTION: This field is no longer in use after the

install of HBH\*1.0\*32.

631.4,4 FTEE ON HBHC 0;5 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>1)!(X\<0)!(X?.E1"."3.N) X

LAST EDITED: MAY 01, 2021

HELP-PROMPT: This field is no longer in use.

DESCRIPTION: This field is no longer in use after the

install of HBH\*1.0\*32.

631.4,5 HBHC TEAM 0;6 POINTER TO HBHC TEAM FILE (#633)

(Required)

LAST EDITED: MAY 01, 2021

HELP-PROMPT: Answer with a team name that exists in the

HBPC (also called HBHC) Team file. This field

is required.

DESCRIPTION: This field represents which HBPC (also called

HBHC) team includes this provider.

TECHNICAL DESCR: Entries in this field must be pre-defined in

the HBHC TEAM (#633) file.

631.4,6 INACTIVE PROVIDER NUMBER 0;7 SET

'1' FOR Inactive Provider Number;

LAST EDITED: MAY 01, 2021

HELP-PROMPT: This field is no longer in use. Providers

which were defined before the install of

HBH\*1.0\*32 might have this field defined as

"inactive".

DESCRIPTION: This field is no longer in use after the

install of HBH\*1.0\*32. Providers which were

defined before install might have this field

set to "inactive".

CROSS-REFERENCE: 631.4^AC

1)= S ^HBHC(631.4,"AC",\$E(X,1,30),DA)=""

2)= K ^HBHC(631.4,"AC",\$E(X,1,30),DA)

This cross-reference represents 'AC' file

Index of Inactive Provider Number (6) field,

in HBHC Provider (631.4) file.

PARENT SITE (#9) field in the HBHC SYSTEM PARAMETERS (#631.9) file

631.9,9 PARENT SITE 1;0 POINTER Multiple \#631.99

LAST EDITED: MAY 06, 2021

DESCRIPTION: This field is used to enter all HBPC program

facilities which might be assigned to a

patient's care. Facilities must be pre-

defined in the MEDICAL CENTER DIVISION

(#40.8) file.

TECHNICAL DESCR: The PARENT SITE (#91) field in the HBHC

PATIENT (#631) file is validated against

entries in the PARENT SITE (#9) field of the

HBHC SYSTEM PARAMETERS (#631.9) file.

631.99,.01 PARENT SITE 0;1 POINTER TO MEDICAL CENTER DIVISION

FILE (#40.8) (Multiply asked) (audited)

LAST EDITED: MAY 07, 2021

HELP-PROMPT: Select an entry from the MEDICAL CENTER

DIVISION (#40.8) file which might be

associated to a patient's HBPC care.

DESCRIPTION: Entries in this file are possible HBPC care

facilities.

TECHNICAL DESCR: Entries in this field must be pre-defined

In the MEDICAL CENTER DIVISION (#40.8)

file.

AUDIT: YES, ALWAYS

CROSS-REFERENCE: 631.99^B

1)= S ^HBHC(631.9,DA(1),1,"B",\$E(X,1,30)

,DA)=""

2)= K ^HBHC(631.9,DA(1),1,"B",\$E(X,1,30),DA)

PARENT SITE (#91) field in the HBHC PATIENT (#631) file

631,91 PARENT SITE 5;1 POINTER TO MEDICAL CENTER DIVISION

FILE (#40.8) (Required) (audited)

HBPC PARENT SITE

INPUT TRANSFORM: S DIC("S")="I \$D(^HBHC(631.9,1,1,""B"",+Y))"

D ^DIC K DIC S DIC=DIE,X=+Y K:Y\<0 X

LAST EDITED: JUN 21, 2021

HELP-PROMPT: Please select the HBPC Program Facility

associated to the patient's care.

DESCRIPTION: The Parent Site prompt provides selection of

the HBPC Program Facility which has been

defined in the local HBHC SITE PARAMETERS

(#631.9) file. If only one site has been

defined as a parent site, that site will

default into this prompt for selection.

Otherwise, users will be required to select

The HBPC Program Facility associated to the

patient's care.

The selected site's code will be used for

AITC record transmissions for this patient.

If you are not locating the appropriate HBPC

Program Site for selection, please contact

Your HBPC Program Manager for assistance.

TECHNICAL DESCR: Entries in this field must be predefined in

The PARENT SITE (#9) multiple field of the

HBHC SYSTEM PARAMETERS (#631.9) file.

SCREEN: S DIC("S")="I \$D(^HBHC(631.9,1,1,""B"",+Y))"

AUDIT: YES, ALWAYS

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

PARENT SITE (#35) field in the HBHC MEDICAL FOSTER HOME (#633.2) file

633.2,35 PARENT SITE 13;1 POINTER TO MEDICAL CENTER DIVISION

FILE (#40.8) (Required) (audited)

INPUT TRANSFORM: S DIC("S")="I \$D(^HBHC(631.9,1,1,""B"",+Y))"

D ^DIC K DIC S DIC=DIE,X=+Y K:Y\<0 X

LAST EDITED: JUN 02, 2021

HELP-PROMPT: Select the HBPC Program Facility associated

to this Medical Foster Home.

DESCRIPTION: The Parent Site prompt provides selection of

the HBPC Program Facility which has been

defined in the local HBHC SITE PARAMETERS

(#631.9) file. If only one site has been

defined as a parent site, that site will

default into this prompt for selection.

Otherwise, users will be required to select

The HBPC Program Facility associated to the

Medical Foster Home.

The selected site's code will be used for

AITC record transmissions for this Medical

Foster Home and for patients in this Medical

Foster Home.

If you are not locating the appropriate HBPC

Program Site for selection, please contact

Your HBPC Program Manager for assistance.

TECHNICAL DESCR: Entries in this field must be predefined in

The PARENT SITE (#9) multiple field of the

HBHC SYSTEM PARAMETERS (#631.9) file.

SCREEN: I \$D(^HBHC(631.9,1,1,"B",+Y))

EXPLANATION: Entry must be pre-defined as a parent site in

the HBHC SYSTEM PARAMETERS (#631.9) file.

AUDIT: YES, ALWAYS

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

Options

NAME: HBHC EDIT PROVIDER (631.4) MENU TEXT: Provider File Data Entry

TYPE: action CREATOR: <span class="mark">REDACTED</span>

E ACTION PRESENT: YES X ACTION PRESENT: YES

DESCRIPTION: This option allows entering/editing of the provider data in

the HBHC PROVIDER (#631.4) file.

EXIT ACTION: D EXITOPT^HBHCPROV ENTRY ACTION: D EN^HBHCPROV

TIMESTAMP: 55795,36640

UPPERCASE MENU TEXT: PROVIDER FILE DATA ENTRY

NAME: HBHC EDIT SYSTEM PARAMETERS MENU TEXT: System Parameters Edit

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

DESCRIPTION: This option allows entering/editing of the system parameters

In the HBHC SYSTEM PARAMETERS (#631.9) file.

The following fields may be edited: NUMBER OF VISIT DAYS TO SCAN (#3),

TRANSMIT REPORT PRINTER (#6), and PARENT SITE (#9).

All other fields are uneditable.

ROUTINE: HBHCEDSP TIMESTAMP: 55523,32584

TIMESTAMP OF PRIMARY MENU: 59114,54812

UPPERCASE MENU TEXT: SYSTEM PARAMETERS EDIT

Protocols

NAME: HBHC ADD NEW PROVIDER ITEM TEXT: Define New HBPC Provider

TYPE: action CREATOR: REDACTED

PACKAGE: HOSPITAL BASED HOME CARE

DESCRIPTION: This protocol is used to define a new HBHC Provider for the

HBHC PROVIDER (#631.4) file.

SYNONYM: DF

SYNONYM: AD

COLUMN WIDTH: 25 MNEMONIC WIDTH: 3

IDENTIFIER: AD EXIT ACTION: S VALMBCK="R"

ENTRY ACTION: D ADD^HBHCPROV TIMESTAMP: 65853,60707

NAME: HBHC DETAIL DISPLAY ITEM TEXT: Detailed Display

TYPE: action CREATOR: <span class="mark">REDACTED</span>

PACKAGE: HOSPITAL BASED HOME CARE

DESCRIPTION: This protocol displays detailed information from the NEW

PERSON (#200) file or the HBHC PROVIDER (#631.4) file for a user selection.

ENTRY ACTION: D DD^HBHCPROV TIMESTAMP: 65853,60819

NAME: HBHC DISPLAY ALL PROVIDER FILE 631.4

ITEM TEXT: Display All HBPC Provider Entries

TYPE: action CREATOR: <span class="mark">REDACTED</span>

PACKAGE: HOSPITAL BASED HOME CARE

DESCRIPTION: This protocol displays all entries in the HBHC PROVIDER

(#631.4) file.

ENTRY ACTION: S HBHCNP=0 D ALLPROV^HBHCPROV

TIMESTAMP: 65853,60830

NAME: HBHC DISPLAY NEW PERSON(S) ITEM TEXT: Display New Person Entries

TYPE: action CREATOR: <span class="mark">REDACTED</span>

PACKAGE: HOSPITAL BASED HOME CARE

DESCRIPTION: This protocol is used to display entries from the NEW PERSON

(#200) file.

ENTRY ACTION: S HBHCNP=1 D EN2^HBHCPROV

TIMESTAMP: 65791,45163

NAME: HBHC DISPLAY PROVIDER FILE 631.4 ITEM TEXT: Display HBPC Provider Entries

TYPE: action CREATOR: <span class="mark">REDACTED</span>

PACKAGE: HOSPITAL BASED HOME CARE

DESCRIPTION: This protocol displays entries in the HBHC PROVIDER (#631.4)

file based on user input.

ENTRY ACTION: S (HBHCNP,HBHCIENX)=0 D EN2^HBHCPROV

TIMESTAMP: 65853,60870

NAME: HBHC EDIT PROVIDER FILE 631.4 ITEM TEXT: Edit HBPC Provider File Entry

TYPE: action CREATOR: <span class="mark">REDACTED</span>

PACKAGE: HOSPITAL BASED HOME CARE

DESCRIPTION: This protocol will allow for editing a current entry in the

HBHC PROVIDER (#631.4) file.

SYNONYM: ED

IDENTIFIER: ED ENTRY ACTION: D EDIT^HBHCPROV

TIMESTAMP: 65853,60879

NAME: HBHC EDIT PROVIDER MENU

ITEM TEXT: HBPC Edit Provider - File \#631.4

TYPE: menu CREATOR: <span class="mark">REDACTED</span>

PACKAGE: HOSPITAL BASED HOME CARE

DESCRIPTION: This protocol allows for entering/editing data in the HBHC

PROVIDER (#631.4) file.

SYNONYM: EP

COLUMN WIDTH: 40 MNEMONIC WIDTH: 4

ITEM: HBHC EDIT PROVIDER FILE 631.4 MNEMONIC: ED

SEQUENCE: 5 DISPLAY NAME: Edit HBPC Provider File

ITEM: HBHC DISPLAY NEW PERSON(S) MNEMONIC: NP

SEQUENCE: 1 DISPLAY NAME: Display New Person Entries

ITEM: HBHC ADD NEW PROVIDER MNEMONIC: AD

SEQUENCE: 4 DISPLAY NAME: Add New HBPC Provider

ITEM: HBHC DISPLAY PROVIDER FILE 631.4 MNEMONIC: HP

SEQUENCE: 2 DISPLAY NAME: Display HBPC Provider(s)

ITEM: HBHC DISPLAY ALL PROVIDER FILE 631.4

MNEMONIC: ALL SEQUENCE: 3

DISPLAY NAME: Display All HBPC Providers

ITEM: HBHC DETAIL DISPLAY MNEMONIC: DD

SEQUENCE: 6 DISPLAY NAME: Detailed Display

ITEM: HBHC PRINT SELECTION MNEMONIC: PR

SEQUENCE: 7 DISPLAY NAME: Print Display

SCREEN: I 1 X:\$D(^ORD(101,+\$P(^ORD(101,DA(1),10,DA,0),U),24)) ^(24)

HEADER: D SHOW^VALM TIMESTAMP: 65853,61069

NAME: HBHC PRINT SELECTION ITEM TEXT: Print the Display

TYPE: action CREATOR: <span class="mark">REDACTED</span>

PACKAGE: HOSPITAL BASED HOME CARE

DESCRIPTION: This protocol prints the display. TO DO: enhance description

and name of this protocol.

ENTRY ACTION: D PRINT^HBHCPROV TIMESTAMP: 65796,64403

List Template

NAME: HBHC EDIT PROVIDER TYPE OF LIST: PROTOCOL

LEFT MARGIN: 1 RIGHT MARGIN: 80

TOP MARGIN: 5 BOTTOM MARGIN: 18

OK TO TRANSPORT?: OK USE CURSOR CONTROL: YES

PROTOCOL MENU: HBHC EDIT PROVIDER MENU

SCREEN TITLE: HBPC EDIT PROVIDER ALLOWABLE NUMBER OF ACTIONS: 1

AUTOMATIC DEFAULTS: YES HIDDEN ACTION MENU: VALM HIDDEN ACTIONS

ARRAY NAME: ^TMP("HBHCLIST",\$J)

ITEM NAME: HEADER COLUMN: 2

WIDTH: 75

EXIT CODE: D EXIT^HBHCPROV

HEADER CODE: D:\$G(HBHCNP) HDR2^HBHCPROV D:'\$G(HBHCNP) HDR^HBHCPROV

HELP CODE: D HELP^HBHCPROV ENTRY CODE: D INIT^HBHCPROV

### Client Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only reason to consider a back-out of HBH\*1.0\*32 is in the event of a catastrophic failure. HBH\*1.0\*32 changes are independent of the VistA changes and of each other. In the case of a catastrophic failure of HBH\*1.0\*32, the VistA Patch can remain in the system.

Contact the Health Product Support Tier 3 Clinical Sustainment Team by submitting a Service Now ticket to NTL SUP CLIN3 requesting back-out assistance due to a catastrophic failure with HBH\*1.0\*32.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was necessary for HBH\*1.0\*32.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the test sites listed in section <u>3.2.2</u>. The sites followed the provided test plan/concurrence form and executed the test cases according to the plan for the first build of HBH\*1.0\*32. The sites either passed or failed any item based on testing. The tests were performed by IT analysts at each site who are familiar with using the application. Any items that failed were then re-developed, sent back to the sites, and tested for the next build following the same process.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application or a significant patient impact issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out HBH\*1.0\*32 would result in the re-instatement of the issues addressed in HBH\*1.0\*32.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The facility Chief Information Officer has the final authority to require the rollback and accept the associated risks

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Administrators will need to use the PackMan function INSTALL/CHECK MESSAGE. Check MailMan messages for the backup message sent by the Backup a Transport Global function executed prior to the patch install. (See section <u>4.8.1</u>, Step 1B; this must be done before the patch is installed).

Summary

1.  In VistA MailMan, select the message shown below:
    1.  Backup of HBH\*1.0\*32 install on \<mm, dd, yyyy\> \<user name\>
2.  Select the Xtract PackMan option.
3.  Select the Install/Check Message option.
4.  Enter Yes at the prompt.
5.  Enter No at the backup prompt. There is no need to back up the backup.

    DetailBackup Message

Subj: Backup of HBH\*1.0\*32 on Jun 21, 2021. Build \[#181727\] 06/21/21@16:16

5821 lines

From: <span class="mark">REDACTED</span> In 'IN' basket. Page 1

----------------------------------------------------------------------------

\$TXT Created by <span class="mark">REDACTED</span> at <span class="mark">REDACTED</span> (KIDS) on Monday, 06/21/21 at 16:16

> **WARNING:** Installing this backup patch message will install older versions

of routines and Build Components (options, protocols, templates, etc.).

Please verify with the Development Team that it is safe to install.

\$END TXT

\$KID HBH\*1.0\*32b

\*\*INSTALL NAME\*\*

HBH\*1.0\*32b

"BLD",11782,0)

HBH\*1.0\*32b^HOSPITAL BASED HOME CARE^0^3210621^n

"BLD",11782,1,0)

^^5^5^3210621

"BLD",11782,1,1,0)

Backup of HBH\*1.0\*32 on Jun 21, 2021

"BLD",11782,1,2,0)

Type \<Enter\> to continue or '^' to exit: ^

Enter message action (in IN basket): Ignore// Xtract KIDS

Select PackMan function: 6 INSTALL/CHECK MESSAGE

Line 8 Message \#181727 Unloading KIDS Distribution HBH\*1.0\*32b

Build HBH\*1.0\*32b has been loaded before, here is when:

HBH\*1.0\*32b Install Completed

was loaded on Jun 18, 2021@13:57:12

OK to continue with Load? NO// YES

Want to Continue with Load? YES//

Loading Distribution...

HBH\*1.0\*32b

Select PackMan function:

Enter message action (in IN basket): Ignore//

Install from Backup Message

Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

Select INSTALL NAME: HBH\*1.0\*32b 6/21/21@16:20:55

=\> Backup of HBH\*1.0\*32 on Jun 21, 2021. Build

This Distribution was loaded on Jun 21, 2021@16:20:55 with header of

Backup of HBH\*1.0\*32 on Jun 21, 2021. Build

It consisted of the following Install(s):

HBH\*1.0\*32b

Checking Install for Package HBH\*1.0\*32b

Install Questions for HBH\*1.0\*32b

Incoming Files:

631 HBHC PATIENT

> **NOTE:** You already have the 'HBHC PATIENT' File.

631.4 HBHC PROVIDER

> **NOTE:** You already have the 'HBHC PROVIDER' File.

631.9 HBHC SYSTEM PARAMETERS

> **NOTE:** You already have the 'HBHC SYSTEM PARAMETERS' File.

633.2 HBHC MEDICAL FOSTER HOME

> **NOTE:** You already have the 'HBHC MEDICAL FOSTER HOME' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// HOME (CRT)

HBH\*1.0\*32b

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

Installing PACKAGE COMPONENTS:

Installing PROTOCOL

Installing LIST TEMPLATE

Installing OPTION

Jun 21, 2021@16:22:03

Updating Routine file...

Updating KIDS files...

HBH\*1.0\*32b Installed.

Jun 21, 2021@16:22:03

NO Install Message sent

,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

100% . 25 50 75 .

Complete F,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

Install Completed

This backup install does not delete the parent site fields from the HBHC EDIT SYSTEM PARAMETER (#631.9) file, the HBHC PATIENT (#631) file, and the HBHC MEDICAL FOSTER HOME (#633.2) file. Those deletions must be done manually by following instructions in the “Parent Site Field Deletions” section of this document.

If a “HBH\*1.0\*32b” backup message is not available, the following steps may be followed to manually back out the patch.

Routines

Restore the following routines from the “routines only” backup message which was specified before patch install.

- HBHCADM
- HBHCDEM
- HBHCEDSP
- HBHCFILE
- HBHCRP2
- HBHCRP5
- HBHCRXMT
- HBHCUTL1
- HBHCXMA
- HBHCXMD
- HBHCXMM
- HBHCXMT
- HBHCXMV

Data Dictionary

Restore the Data Dictionary for the HBHC PROVIDER (#631.4) file.

Option

Restore the option “Provider File Data Entry”.

VA FileMan 22.2

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

Input to what File: OPTION// (13535 entries)

EDIT WHICH FIELD: ALL//

Select OPTION NAME: HBHC EDIT PROVIDER (631.4) Provider File Data Entry

NAME: HBHC EDIT PROVIDER (631.4) Replace

MENU TEXT: Provider File Data Entry Replace

OUT OF ORDER MESSAGE:

LOCK:

REVERSE/NEGATIVE LOCK:

DESCRIPTION:

1\>This option allows entering/editing of the provider data in the

2\>HBHC PROVIDER (#631.4) file.

EDIT Option:

HELP FRAME:

PRIORITY:

PROHIBITED TIMES:

Select TIMES PROHIBITED:

Select TIME PERIOD:

RESTRICT DEVICES?:

Select PERMITTED DEVICE:

TYPE: action// EDIT edit

Select ITEM:

Short Menu Text:

DISPLAY OPTION?:

PACKAGE:

DELEGABLE:

EXIT ACTION: D EXITOPT^HBHCPROV// @

SURE YOU WANT TO DELETE? Y (Yes)

ENTRY ACTION: D EN^HBHCPROV// @

SURE YOU WANT TO DELETE? Y (Yes)

XQUIT MESSAGE:

1\>

XQUIT EXECUTABLE:

ROUTINE:

HEADER:

DIC {DIC}: HBHC(631.4,

DIC(0): AEMQL

DIC(A):

DIC(B):

DIC(S):

DIC(W):

D.:

DR{DDS}:

DDSFILE:

DDSFILE(1):

DDSPAGE:

DDSPARM:

DIE: HBHC(631.4,

DR {DIE}: \[HBHC EDIT PROVIDER (631.4)\]

\*DR():

NO UP-ARROW:

\*DIE(W):

DIC {DIP}:

PG:

L.:

FLDS:

BY:

FR:

TO:

DHD:

DCOPIES:

DIS(0):

DIS(1):

DIS(2):

DIS(3):

IOP:

DHIT:

DIOBEG:

DIOEND:

DISUPNO:

DIPCRIT:

DIASKHD:

DISTEMP:

DIC {DIQ}:

DR {DIQ}:

DIQ(0):

SUPRESS DEVICE PROMPT:

\*ORDER PRINT ACTION:

\*ORDER CANCEL ACTION:

\*ORDER PURGE ACTION:

INDEPENDENTLY INVOCABLE:

\*QUEUED TO RUN AT WHAT TIME:

\*DEVICE FOR QUEUED JOB OUTPUT:

\*RESCHEDULING FREQUENCY:

\*QUEUED TO RUN ON VOLUME SET:

SCHEDULING RECOMMENDED:

KEEP FROM DELETING:

SERVER BULLETIN:

SERVER ACTION:

SERVER MAIL GROUP:

SERVER AUDIT:

SUPRESS BULLETIN:

SERVER REPLY:

SAVE REQUEST:

SERVER DEVICE:

ZTSK RETENTION DAYS:

ICON:

TITLE:

Select RPC:

PRIMARY MENU:

PROTECTED VARIABLES:

\*SPECIAL QUEUEING:

Select SYNONYM:

After the above edits, the option should display as:

NAME: HBHC EDIT PROVIDER (631.4) MENU TEXT: Provider File Data Entry

TYPE: edit CREATOR: <span class="mark">REDACTED</span>

DESCRIPTION: This option allows entering/editing of the provider data in the HBHC Provider File (HBHC(631.4)).

DIC {DIC}: HBHC(631.4, DIC(0): AEMQL

DIE: HBHC(631.4, DR {DIE}: \[HBHC EDIT PROVIDER (631.4)\]

TIMESTAMP: 55795,36640

UPPERCASE MENU TEXT: PROVIDER FILE DATA ENTRY

Optional StepsParent Site Field Deletions

Delete parent site field from data dictionaries.

HBHC SYSTEM PARAMETERS (#631.9) file

VA FileMan 22.2

Select OPTION: 4 MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES//

Modify what File: HBHC SYSTEM PARAMETERS// (1 entry)

Select FIELD: PARENT SITE (multiple)

Multiple Field \#9 in File \#631.9Enter “@” at “PARENT SITE”:

MULTIPLE-FIELD LABEL: PARENT SITE

READ ACCESS:

WRITE ACCESS:

SOURCE:

DESCRIPTION... TECHNICAL DESCRIPTION...

MULTIPLE-R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* .

W. ARE YOU SURE YOU WANT TO DELETE THE ENTIRE FIELD: Y .

. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* .

DESCRIPTF,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

...

OK TO DELETE 'PARENT SITE' FIELDS IN THE EXISTING ENTRIES? Yes//

HBHC PATIENT (#631) file

VA FileMan 22.2

Select OPTION: 4 MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES//

POINTER TO A FILE

Modify what File: HBHC PATIENT// (361 entries)

Select FIELD: PARENT SITE

Enter “@” at “PARENT SITE”:

Field \#91 in File \#631

FIELD LABEL: PARENT SITE DATA TYPE... POINTER TO A FILE

Field \#91 in File \#631

FIELD LABEL: DATA TYPE... POINTER TO A FILE

R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* .

. ARE YOU SURE YOU WANT TO DELETE THE ENTIRE FIELD: Y .

AUDIT CON. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* .

READ F,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

...

OK TO DELETE 'PARENT SITE' FIELDS IN THE EXISTING ENTRIES? Yes//

HBHC MEDICAL FOSTER HOME (#633.2) file

VA FileMan 22.2

Select OPTION: 4 MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES//

Modify what File: HBHC MEDICAL FOSTER HOME// (7 entries)

Select FIELD: PARENT

Enter “@” at “PARENT SITE”:

Field \#35 in File \#633.2

FIELD LABEL: PARENT SITE DATA TYPE... POINTER TO A FILE

Field \#35 in File \#633.2

FIELD LABEL: DATA TYPE... POINTER TO A FILE

R,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,T

. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* .

. ARE YOU SURE YOU WANT TO DELETE THE ENTIRE FIELD: Y .

AUDIT CON. \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* .

READ F,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,G

...

OK TO DELETE 'PARENT SITE' FIELDS IN THE EXISTING ENTRIES? Yes//

HBHC Edit System Parameters optionChange the description to original text.

NAME: HBHC EDIT SYSTEM PARAMETERS MENU TEXT: System Parameters Edit

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

DESCRIPTION: This option allows entering/editing of the system parameters in the HBHC System Parameters file (631.9).

The parameter Number of Visit Days to Scan is used by the system as a starting point of how many days to include when records are being created in the HBHC Visit File (HBHC(632)) using the appointment data entered via the Appointment Management \[HBHC APPOINTMENT\] option. This parameter must be a number between 7 and 365 inclusive, but as a rule, the lowest number that accurately reflects the appointment data timeliness should be entered (e.g. if appointments are entered daily, then 7 would be appropriate).

All other System Parameter fields are uneditable.

ROUTINE: HBHCEDSP TIMESTAMP: 55523,32584

TIMESTAMP OF PRIMARY MENU: 59114,54812

UPPERCASE MENU TEXT: SYSTEM PARAMETERS EDIT

Delete ComponentsList Template

VA FileMan 22.2

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

Input to what File: HBHC MEDICAL FOSTER HOME// LIST TEMPLATE

(745 entries)

EDIT WHICH FIELD: ALL//

Select LIST TEMPLATE NAME: HBHC EDIT PROVIDER

NAME: HBHC EDIT PROVIDER// @

SURE YOU WANT TO DELETE THE ENTIRE 'HBHC EDIT PROVIDER' LIST TEMPLATE? Y

(Yes)

Protocols

VA FileMan 22.2

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

Input to what File: LIST TEMPLATE// PROTOCOL (6892 entries)

EDIT WHICH FIELD: ALL//

Select PROTOCOL NAME: HBHC ADD NEW PROVIDER Define New HBPC Provider AD

NAME: HBHC ADD NEW PROVIDER Replace ... With Replace

SURE YOU WANT TO DELETE THE ENTIRE 'HBHC ADD NEW PROVIDER' PROTOCOL? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No//

(No)

Select PROTOCOL NAME: HBHC DETAIL DISPLAY Detailed Display

NAME: HBHC DETAIL DISPLAY// @

SURE YOU WANT TO DELETE THE ENTIRE 'HBHC DETAIL DISPLAY' PROTOCOL? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No// N

(No)

Select PROTOCOL NAME: HBHC DISPLAY ALL PROVIDER FILE 631.4 Display All HBPC Provider Entries

NAME: HBHC DISPLAY ALL PROVIDER FILE 631.4 Replace ... With

Replace

SURE YOU WANT TO DELETE THE ENTIRE 'HBHC DISPLAY ALL PROVIDER FILE 631.4' PROTOCOL? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No//

(No)

Select PROTOCOL NAME: HBHC DISPLAY NEW PERSON(S) Display New Person Entries

NAME: HBHC DISPLAY NEW PERSON(S) Replace ... With

Replace

SURE YOU WANT TO DELETE THE ENTIRE 'HBHC DISPLAY NEW PERSON(S)' PROTOCOL? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No//

(No)

Select PROTOCOL NAME: HBHC DISPLAY PROVIDER FILE 631.4 Display HBPC Provider Entries

NAME: HBHC DISPLAY PROVIDER FILE 631.4 Replace ... With

Replace

SURE YOU WANT TO DELETE THE ENTIRE 'HBHC DISPLAY PROVIDER FILE 631.4' PROTOCOL? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No//

(No)

Select PROTOCOL NAME: HBHC EDIT PROVIDER FILE 631.4 Edit HBPC Provider File Entry ED

NAME: HBHC EDIT PROVIDER FILE 631.4 Replace ... With

Replace

SURE YOU WANT TO DELETE THE ENTIRE 'HBHC EDIT PROVIDER FILE 631.4' PROTOCOL? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No//

(No)

Select PROTOCOL NAME: HBHC EDIT PROVIDER MENU HBPC Edit Provider - File \#631.4

NAME: HBHC EDIT PROVIDER MENU Replace ... With Replace

SURE YOU WANT TO DELETE THE ENTIRE 'HBHC EDIT PROVIDER MENU' PROTOCOL? Y

(Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? No//

(No)

Select PROTOCOL NAME: HBHC PRINT SELECTION Print the Display

NAME: HBHC PRINT SELECTION Replace ... With Replace

SURE YOU WANT TO DELETE THE ENTIRE 'HBHC PRINT SELECTION' PROTOCOL? Y (Yes)

SINCE THE DELETED ENTRY MAY HAVE BEEN 'POINTED TO'

BY ENTRIES IN THE 'AUDIT' FILE, ETC.,

DO YOU WANT THOSE POINTERS UPDATED (WHICH COULD TAKE QUITE A WHILE)? Nos//

(No)

### Client Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routines

Verify that routine checksums are listing at the “before” values of the patch description.

Options

Verify that the option descriptions appear as shown below.

NAME: HBHC EDIT SYSTEM PARAMETERS MENU TEXT: System Parameters Edit

TYPE: run routine CREATOR: <span class="mark">REDACTED</span>

DESCRIPTION: This option allows entering/editing of the system parameters

In the HBHC System Parameters file (631.9).

The parameter Number of Visit Days to Scan is used by the system as a

starting

point of how many days to include when records are being created in the HBHC

Visit File (HBHC(632)) using the appointment data entered via the

Appointment Management \[HBHC APPOINTMENT\] option. This parameter must be a

number between 7 and 365 inclusive, but as a rule, the lowest number that

accurately reflects the appointment data timeliness should be entered (e.g.

if appointments are entered daily, then 7 would be appropriate).

All other System Parameter fields are uneditable.

ROUTINE: HBHCEDSP TIMESTAMP: 55523,32584

TIMESTAMP OF PRIMARY MENU: 59114,54812

UPPERCASE MENU TEXT: SYSTEM PARAMETERS EDIT

NAME: HBHC EDIT PROVIDER (631.4) MENU TEXT: Provider File Data Entry

TYPE: edit CREATOR:<span class="mark">REDACTED</span>

DESCRIPTION: This option allows entering/editing of the provider data in

The HBHC Provider File (HBHC(631.4)).

DIC {DIC}: HBHC(631.4, DIC(0): AEMQL

DIE: HBHC(631.4, DR {DIE}: \[HBHC EDIT PROVIDER (631.4)\]

TIMESTAMP: 55795,36640

UPPERCASE MENU TEXT: PROVIDER FILE DATA ENTRY

Data Dictionary for the HBHC PROVIDER (#631.4) file

Fields should list as shown below.

631.4,.01 NUMBER 0;1 NUMBER (Required)

INPUT TRANSFORM: K:(X'?3.4N)!(\$E(X)\>2)!((\$L(X)=3)&(X\>299))

!((\$L(X)=4)&((X\<1010)!(X\>2999))) X

LAST EDITED: JUL 12, 1999

HELP-PROMPT: Answer with a Number between 100 and 299, or

1010 and 2999, 0 Decimal Digits. This number

represents the unique HBPC Provider number

assigned to each provider.

DESCRIPTION: This field represents unique 4 numeric digit

HBPC provider number assigned to each person

who has any FTEE charged to HBPC. 4 digit

number should be structured as follows:

\- first digit contains 1 for nonstudents, 2

for students

\- second digit contains 0 thru 8 indicating

discipline as follows:

0 RN

1 LPN, LVN, Home Health Aide or Tech,

Nursing Assistant

2 Social Worker

3 OT, PT, CT, Rehabilitation Therapist

4 Dietitian, Nutritionist

5 Physician

6 Nurse Practitioner

7 Clinical Pharmacist

8 Other

\- third & fourth digits contain 0 thru 99

indicating individual provider as follows:

0 first staff member in discipline

1 second staff member in discipline

2 third staff member in discipline,

etc.

All students in a particular discipline

Should share the same HBPC provider number

(e.g. all RN students would be 200). New

Provider numbers are issued only when FTEE is

increased. Provider number '190' can be used

as a 'catch-all' category if the need arises.

NOTES: XXXX--CAN'T BE ALTERED EXCEPT BY PROGRAMMER

CROSS-REFERENCE: 631.4^B

1)= S ^HBHC(631.4,"B",\$E(X,1,30),DA)=""

2)= K ^HBHC(631.4,"B",\$E(X,1,30),DA)

This cross-reference represents regular 'B'

file index of HBHC Provider (631.4) file,

Number (.01) field.

631.4,1 PROVIDER NAME 0;2 POINTER TO NEW PERSON FILE (#200)

(Required)

LAST EDITED: DEC 18, 1992

HELP-PROMPT: Answer with provider name that exists in New

Person (200) file.

DESCRIPTION: This field represents HBHC provider's name in

New Person (200) file. Person must exist in

VA(200) for HBHC selection, since LAYGO is

not allowed.

CROSS-REFERENCE: 631.4^C

1)= S ^HBHC(631.4,"C",\$E(X,1,30),DA)=""

2)= K ^HBHC(631.4,"C",\$E(X,1,30),DA)

This cross-reference represents regular 'C'

file index of HBHC Provider (631.4) file,

Name (1) field, which references New Person

\(200\) file entries.

631.4,2 DEGREE 0;3 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>15!(\$L(X)\<1) X

LAST EDITED: MAY 31, 1991

HELP-PROMPT: Answer with degree held by provider. Answer

must be 1-15 characters in length.

DESCRIPTION: This field represents degree held by HBHC

provider. Field allows 1-15 characters of

free text.

631.4,3 GRADE/STEP 0;4 FREE TEXT

INPUT TRANSFORM: K:\$L(X)\>6!(\$L(X)\<3)!'(X?1.3E1"/"1.2N) X

LAST EDITED: MAR 02, 1993

HELP-PROMPT: Answer with grade/step held by provider.

Answer must be 3-6 characters in length and

be in 99/99 or xxx/99 format. (e.g. 11/4

for grade 11, step 4, or SR/11 for Senior

grade, step 11)

DESCRIPTION: This field represents grade/step of HBHC

provider. Field must be in 99/99 or xxx/99

format (e.g. 11/4 for grade 11, step 4 or

SR/11 for Senior grade, step 11). The format

allows for 1-2 numerics or 1-3 alphabetic

characters, 1 slash ('/'), and 1-2 numerics.

631.4,4 FTEE ON HBHC 0;5 NUMBER

INPUT TRANSFORM: K:+X'=X!(X\>1)!(X\<0)!(X?.E1"."3N.N) X

LAST EDITED: DEC 11, 1992

HELP-PROMPT: Answer with a Number between 0 and 1, 2

Decimal Digits.

DESCRIPTION: This field represents FTEE charged to HBHC

service, and must be between 0 and 1, with 2

decimal digits allowed. (e.g. '.5' or

'1.0')

631.4,5 HBHC TEAM 0;6 POINTER TO HBHC TEAM FILE (#633)

(Required)

LAST EDITED: MAY 23, 1997

HELP-PROMPT: Answer with team name that exists in HBHC

Team file. Field is required.

DESCRIPTION: This field represents HBHC team name,

referencing HBHC Team (633) file entries.

Team must exist in HBHC Team file, since

LAYGO is not allowed.

631.4,6 INACTIVE PROVIDER NUMBER 0;7 SET

'1' FOR Inactive Provider Number;

LAST EDITED: APR 08, 1997

HELP-PROMPT: Answer with 1 digit numeric code representing

whether HBHC Provider Number is Inactive. As

of 10/1/96, each provider is allowed to have

only 1 Active Provider Number. All others

must be Inactive.

DESCRIPTION: This field represents whether HBHC Provider

Number is active. As of 10/1/96, each HBHC

Provider may have only 1 unique HBHC Provider

Number active at any point in time. All

other provider numbers must be Inactive

Provider Numbers.

CROSS-REFERENCE: 631.4^AC

1)= S ^HBHC(631.4,"AC",\$E(X,1,30),DA)=""

2)= K ^HBHC(631.4,"AC",\$E(X,1,30),DA)

This cross-reference represents 'AC' file

index

of Inactive Provider Number (6) field, in

HBHC Provider (631.4) file.

Parent Site Fields

No fields for “PARENT SITE” should exist in the Data Dictionary for the HBHC SYSTEM PARAMETERS (#631.9) file, the HBHC PATIENT (#631) file, and the HBHC MEDICAL FOSTER HOME (#633.2) file.

Protocols

The following protocols should not exist on the system:

- HBHC ADD NEW PROVIDER
- HBHC DETAIL DISPLAY
- HBHC DISPLAY ALL PROVIDER FILE 631.4
- HBHC DISPLAY NEW PERSON(S)
- HBHC DISPLAY PROVIDER FILE 631.4
- HBHC EDIT PROVIDER FILE 631.4
- HBHC EDIT PROVIDER MENU
- HBHC PRINT SELECTION

List Template

The List Template “HBHC EDIT PROVIDER” should not exist on the system.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HBH\*1.0\*32.