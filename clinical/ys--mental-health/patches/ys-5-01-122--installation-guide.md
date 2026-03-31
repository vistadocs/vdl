---
title: YS*5.01*122 NCC Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: NCC
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 5.01
patch_id: YS*5.01*122
group_key: "YS:YS:5.01"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - table
  - clozapine
  - contents
  - install
  - installation
  - class
  - order
  - health
  - strong
  - pssjxr
page_count: 0
word_count: 9003
section_count: 32
table_count: 4
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: July 2019
revision_count: 1
revision_newest: 7/8/2019
revision_oldest: 7/8/2019
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/MH_NCC_Proj_5_01_IG_R0719.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/MH_NCC_Proj_5_01_IG_R0719.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

---
subtitle: |
  National Clozapine Coordination (NCC) Project

  Deployment, Installation, Backout, and Rollback Guide
---

Release 1

![](ys-5-01-122-ncc-deployment-installation-back-out-and-rollback-guide/001.png)

July 2019

Version 1

Revision History

| Date     | Revision | Description                                                                                       | Author                             |
|----------|----------|---------------------------------------------------------------------------------------------------|------------------------------------|
| 7/8/2019 | 1        | Initial document creation using VIP\_ Deployment_Installation_Backout and Rollback Guide_Template | <span class="mark">REDACTED</span> |

Table 1 Deployment, Installation, Back Out and Rollback Roles and Responsibilities

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
    - [Facility Specifics (Optional)](#facility-specifics-optional)
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
  - [Sample Install Log](#sample-install-log)
  - [Post Install Steps and Post-Install Verification Procedures](#post-install-steps-and-post-install-verification-procedures)
  - [System Configuration](#system-configuration)
- [Backout Procedure](#backout-procedure)
  - [Backout Strategy](#backout-strategy)
  - [Backout Considerations](#backout-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Backout Criteria](#backout-criteria)
  - [Backout Risks](#backout-risks)
  - [Authority for Backout](#authority-for-backout)
  - [Backout Procedure](#backout-procedure-1)
  - [Backout Verification Procedure](#backout-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the multi-build MENTAL HEALTH NCC PROJECT 5.01 (which includes patches YS\*5.01\*122, PSO\*7.0\*457, PSJ\*5.0\*327, and OR\*3.0\*427) and how to back out the product.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a document that describes how, where, and when the MENTAL HEALTH NCC PROJECT 5.01 multi-build will be installed. Also, the document includes the steps describing how the multi-build can be backed out and the software rolled back, if necessary. The plan also identifies resources and includes communications plan with the rollout schedule.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All application, system, financial and other dependencies for deployment of the MENTAL HEALTH NCC PROJECT 5.01 have been confirmed and there are no issues. The prerequisite application dependencies include:

- YS\*5.01\*92: Clozapine Updates
- OR\*3\*243: CPRS GUI 27
- PSO\*7\*422: Health Product Sustainment
- PSO\*7\*518: Mocha 2.1B Warranty Issues
- PSO\*7\*526: Health Product Sustainment
- PSO\*7\*537: Health Product Sustainment
- PSO\*7\*550: Inbound ERX
- PSJ\*5\*54:
- PSJ\*5\*344: Health Product Sustainment
- PSJ\*5\*353: CAS-RXSU2
- PSJ\*5\*355: Health Product Sustainment
- PSJ\*5\*357: Health Product Sustainment
- PSJ\*5\*366: CAS MPDU BUILD 4
- PSJ\*5\*367: Health Product Sustainment
- PSJ\*5\*378: Health Product Sustainment

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENTAL HEALTH NCC PROJECT 5.01 is expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. MENTAL HEALTH NCC PROJECT 5.01 utilizes existing nationally released security controls to control access.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID | Team              | Phase/Role  | Tasks                                                                                                        |
|--------|-----------------------|-----------------|------------------------------------------------------------------------------------------------------------------|
| 1      | Field Operations (FO) | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                              |
| 2      | FO                    | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                       |
| 3      | FO                    | Deployment      | Test for operational readiness                                                                                   |
| 4      | FO                    | Deployment      | Execute deployment                                                                                               |
| 5      | FO                    | Installation    | Plan and schedule installation                                                                                   |
| 6      | FO                    | Installation    | Ensure authority to operate and that certificate authority security documentation is in place                    |
| 7      | FO                    | Installation    | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes      |
| 8      | FO                    | Installations   | Coordinate training                                                                                              |
| 9      | FO                    | Backout         | Confirm availability of backout instructions and backout strategy (what are the criteria that trigger a backout) |
| 10     | FO                    | Post-deployment | Hardware, Software and System Support                                                                            |

Table 2 Site Preparation

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given for national release, then MENTAL HEALTH NCC PROJECT 5.01 patches will be released via the National Patch Module and will be available for installation and deployment at all sites. The scheduling of test/mirror installs, testing, and the deployment to production will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

The National Clozapine Coordination (NCC) solution provides FDA-compliant clozapine dispensing for inpatients. A National Release is planned for April 2019 after testing has been successfully completed at two IOC Sites.

Deployment will be performed by the local or regional staff or and supported by team members from one or more of these organizations: Enterprise Systems Engineering (ESE), Field Operations (FO), Enterprise Operations (EO). Other teams may provide additional support.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation are scheduled to run for 30 days, as described in the master deployment schedule.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the MENTAL HEALTH NCC PROJECT 5.01 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MENTAL HEALTH NCC PROJECT 5.01 will be deployed to each VistA instance at the local sites or the regional data processing centers.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to Initial Operating Capabilities (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, MENTAL HEALTH NCC PROJECT 5.01 will be deployed to all VistA systems.

The Production (IOC) Test sites are:

<span class="mark">REDACTED</span>

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of these patches is mandatory at all VHA facilities. FDA and clozapine Risk Evaluation and Mitigation Strategies (REMS) have both agreed that the National Clozapine Coordinating Center (NCCC) will maintain the authority to dispense clozapine anywhere in the VA Facility.

\*Note: To ensure that the clozapine order checks are triggered correctly, the Clozapine Appropriateness check box must be selected at the user level in the Computerized Patient Record System (CPRS). There are multiple levels of an order check being enabled: Package, System, and User with the user level having the highest priority. If the System level is turned on, then the User will also have it on, unless it has been specifically disabled.

The Clozapine Appropriateness check box can be accessed by navigating the following menu items – Tools \> Options and then by selecting the Order Checks tab. See Figure 1.

Figure 1 Clozapine Appropriateness Check Box

![](ys-5-01-122-ncc-deployment-installation-back-out-and-rollback-guide/002.png)

The following table describes preparation required by the site prior to deployment.

| Site/Other | Problem/Change Needed               | Features to Adapt/Modify to New Product | Actions/Steps                                                                        | Owner      |
|----------------|-----------------------------------------|---------------------------------------------|------------------------------------------------------------------------------------------|----------------|
| All            | Determine changes to current processes. | Inpatient dispensing of clozapine           | Evaluate how new processes differ from current processes and adapt training accordingly. | Pharmacy ADPAC |

Table 4 Files for Retrieval

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Facility Specifics (Optional) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following describes the software prerequisite dependencies at each site prior to deployment

Table 3 Software Specifications

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 21%" />
<col style="width: 17%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Required Software</strong></th>
<th><strong>Make</strong></th>
<th><strong>Version</strong></th>
<th><strong>Configuration</strong></th>
<th><strong>Manufacturer</strong></th>
<th><strong>Other</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p>JU 7,</p>
<p>2008</p></td>
<td>YS*5.01*92</td>
<td>MENTAL HEALTH</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>AUG 20, 2008</td>
<td>OR*3*243</td>
<td>ORDER ENTRY/RESULTS REPORTING</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>MAR 23, 2001</td>
<td>PSJ*5*54</td>
<td>INPATIENT MEDICATIONS</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>SEP 13, 2018</td>
<td>PSJ*5*344</td>
<td>INPATIENT MEDICATIONS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>OCT 25, 2018</td>
<td>PSJ*5*353</td>
<td>INPATIENT MEDICATIONS</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>MAR 8, 2018</td>
<td>PSJ*5*355</td>
<td>INPATIENT MEDICATIONS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>JUN 7, 2018</td>
<td>PSJ*5*357</td>
<td>INPATIENT MEDICATIONS</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>JAN 2, 2019</td>
<td>PSJ*5*366</td>
<td>INPATIENT MEDICATIONS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>OCT 22, 2018</td>
<td>PSJ*5*367</td>
<td>INPATIENT MEDICATIONS</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>JAN 23, 2019</td>
<td>PSJ*5*378</td>
<td>INPATIENT MEDICATIONS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>OCT 2, 2017</td>
<td>PSO*7*422</td>
<td>OUTPATIENT PHARMACY</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>JUL 2, 2018</td>
<td>PSO*7*518</td>
<td>OUTPATIENT PHARMACY</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>JUL 19, 2018</td>
<td>PSO*7*526</td>
<td>OUTPATIENT PHARMACY</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td>JAN 28, 2019</td>
<td>PSO*7*537</td>
<td>OUTPATIENT PHARMACY</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td>JAN 8, 2019</td>
<td>PSO*7*550</td>
<td>OUTPATIENT PHARMACY</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

## Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Technicians will use email and conference calls for communication during the deployment; email and/or conference calls will be utilized to notify the stakeholders of the successful release of the product.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-build MENTAL HEALTH NCC PROJECT 5.01 is installable on a fully patched Veterans Health Information Systems and Technology Architecture (VistA) system and is within the VistA infrastructure packages listed above.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MENTAL HEALTH NCC PROJECT 5.01 installation must be coordinated with the Pharmacy Automated Data Processing Application Coordinator (ADPAC) at each site.

*These patches* may be installed with users on the system. You may wish to install it during non-peak hours. *These patches* should take less than *15* minutes to install.

> **NOTE:** “Before” and “after” checksums are used to verify if your account is where it needs to be before and after installing a software release. Checksum values before the software was modified can be used to verify if an account is up-to-date or if a site has made local modifications to the software. Checksum values after the software has been modified are used to verify that the installed routines are the correct version.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software and Documentation Retrieval Instructions:

The software being released is a host file system (HFS) file created by the Kernel Installation and Distribution System (KIDS); the HFS file name has the extension .KID. Documentation describing the new functionality introduced by this patch is available.

The preferred method is to retrieve files from download directory at vista.med.va.gov. This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following OI Field Offices:

> <span class="mark">REDACTED</span>

The documentation will be in the form of Adobe Acrobat files. Documentation can also be found on the VA Software Documentation Library (VDL) at: <https://www.va.gov/vdl/>

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 48%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Contents</strong></th>
<th><strong>Retrieval Format</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>MH_NCC_PROJ_5_01.KID</td>
<td>HFS file with the VistA software components</td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>MH_NCC_Proj_5_01_UG_R0719.pdf</td>
<td><p>NCC User Guide/Training Guide</p>
<p>New Features in CPRS, Outpatient Pharmacy and Inpatient Medications</p></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>psj_5_p327_phar_um.pdf</td>
<td>Inpatient Medications: Pharmacist’s User Manual</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>psj_5_p327_nurse_um.pdf</td>
<td>Inpatient Medications: Nurse’s User Manual</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>psj_5_p327_tm. pdf</td>
<td><p>Inpatient Medications</p>
<p>Technical Manual/Security Guide</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>pso_7_P457_man_um. pdf</td>
<td>Outpatient Pharmacy (PSO): Managers User Manual</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>pso_7_p457_phar_um.pdf</td>
<td>Outpatient Pharmacy (PSO): Pharmacist’s User Manual</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>MH_NCC_Proj_5_01_PSO_PSJ_QR_R0719. pdf</td>
<td><p>Inpatient Medications and Outpatient Pharmacy</p>
<p>Clozapine Changes– Quick Reference Card</p></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>or_3_p427_cprs_ug.pdf</td>
<td><p>Computerized Patient Record System (CPRS)</p>
<p>User Guide: GUI Version</p></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>or_3_p427_cprs_QR.pdf</td>
<td>Quick Reference Guide for Prescribing/Ordering Clozapine in CPRS</td>
<td>Binary</td>
</tr>
</tbody>
</table>

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Performed by the KIDS Installation.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Performed by the KIDS Installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is written with the assumption that the reader is experienced or familiar with the following:

- The VistA computing environment
- The VA File Manager (FileMan)
- Microsoft Windows

Local or Regional OI&T staff will coordinate the patch installation with the Pharmacy at each site. The Local or Regional OI&T staff have the necessary access and skill set to conduct the installation.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch should less than 15 minutes to install.

1.  Do not queue the installation of this patch.

To avoid disruptions, these patches should be installed during non-peak hours when there is minimal activity on the system. Refer to Appendix A for an example of the installation log.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Pre-Installation Instructions</strong></th>
</tr>
<tr class="odd">
<th>1</th>
<th><p>OBTAIN PATCHES</p>
<p>-------------------------------------</p>
<p>Obtain the host file MH_NCC_PROJECT_5_01.KID, which contains the following patches:</p>
<p>  YS*5.01*122</p>
<p>PSO*7*457</p>
<p>PSJ*5*327</p>
<p>OR*3*427</p>
<p>Sites can retrieve VistA software from the following software repositories. The preferred method is to use Secure File Transfer Protocol (SFTP) to retrieve the files from:</p>
<p><mark>REDACTED</mark></p>
<p>This will download the files from the first available SFTP server.</p>
<p>Sites may also elect to retrieve software directly from a specific server:</p>
<p><mark>REDACTED</mark></p>
<p>The MH_NCC_PROJECT_5_01.KID host file is in the anonymous software directory. Use ASCII Mode when downloading the file.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Pre-Installation Instructions</strong></th>
</tr>
<tr class="odd">
<th>2</th>
<th><p>Use the <strong>Kernel Installation &amp; Distribution System [XPD MAIN]</strong> menu.</p>
<p>Select Kernel Installation &amp; Distribution System Option:</p>
<p>Edits and Distribution ...</p>
<p>Utilities …</p>
<p>Installation ...</p>
<p>Select Kernel Installation &amp; Distribution System Option: Installation</p>
<p>                                                            </p>
<p>Load a Distribution</p>
<p>Print Transport Global</p>
<p>Compare Transport Global to Current System</p>
<p>Verify Checksums in Transport Global</p>
<p>Install Package(s)</p>
<p>Restart Install of Package(s)</p>
<p>Unload a Distribution</p>
<p>Backup a Transport Global</p>
<p>    Select Installation Option:</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>3</td>
<td><p>LOAD TRANSPORT GLOBAL FOR MULTI-BUILD</p>
<p>-------------------------------------</p>
<p>From the Installation menu, select the Load a Distribution option.</p>
<p>When prompted for "Enter a Host File:", enter the full directory path where you saved the HFS file MH_NCC_PROJECT_5_01.KID.</p>
<p>(e.g., SYS$SYSDEVICE:[ANONYMOUS] MH_NCC_PROJ_5_01.KID)</p>
<p>When prompted for "OK to continue with Load? NO//", enter "YES."</p>
<p>The following will display:</p>
<p>Loading Distribution...</p>
<p>MENTAL HEALTH NCC PROJECT 5.01</p>
<p>YS*5.01*122</p>
<p>PSO*7*457</p>
<p>PSJ*5*327</p>
<p>OR*3*427</p>
<p>Use INSTALL NAME: MENTAL HEALTH NCC PROJECT 5.01 to install this Distribution.</p>
<p>     </p></td>
</tr>
<tr class="even">
<td>4</td>
<td><p>RUN INSTALLATION OPTIONS FOR MULTI-BUILD</p>
<p>-------------------------------------</p>
<p>From the Installation menu, you may select to use the following options (when prompted for the INSTALL NAME, enter MENTAL HEALTH NCC PROJECT 5.01</p>
<ol type="a">
<li><p>Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.</p></li>
<li><p>Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).</p></li>
<li><p>Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.</p></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Pre-Installation Instructions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>5</td>
<td><p>INSTALL MULTI-BUILD</p>
<p>-------------------------------------</p>
<p>This is the step to start the installation of this KIDS patch. This will need to be run for the MENTAL HEALTH NCC PROJECT 5.01.</p>
<ol type="a">
<li><p>Choose the Install Package(s) option to start the patch install.</p></li>
<li><p>When prompted "Select INSTALL NAME:", enter MENTAL HEALTH NCC PROJECT 5.01 </p></li>
</ol>
<p> </p>
<p>This Distribution was loaded on Jun 13, 2019@13:46:45 with header of MENTAL HEALTH NCC PROJECT 5.01 ;Created on June 12, 2019@13:46:02</p>
<p>It consisted of the following Install(s):</p>
<p>YS*5.01*122    PSO*7.0*457    PSJ*5.0*327     OR*3.0*427</p></td>
</tr>
</tbody>
</table>

## Sample Install Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to [Appendix A](#APX_A) for an example of an installation log.

## Post Install Steps and Post-Install Verification Procedures 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installation, the following post-installation tasks should be performed:

- Queue transmission option. Please see [Appendix B](#APX_B) for instructions.
- Assign new menu options, e.g. YSCL RETRANSMIT DATA, PSJL MANAGER. Please notify the site’s Clozapine Treatment team about the new options available with this patch so they may request assignment.
- Delete the obsolete options from the TaskMan queue. The options are YSCL WEEKLY TRANSMISSION and YSCL TRANSMIT DEMOGRAPHICS. The steps shown below should be done for both options.

Select Systems Manager Menu \<CLOZA\> Option: TASkman Management

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management \<CLOZA\> Option: SCHEDULe/Unschedule Options

Select OPTION to schedule or reschedule: YSCL TRANSMIT DEMOGRAPHICS (R)

Edit Option Schedule

Option Name: YSCL TRANSMIT DEMOGRAPHICS

Menu Text: Transmit Clozapine Demographics TASK ID: 1877570

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: @ \<\< delete this value

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 7D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND:

- Create PSOCLOZ Mail Group: Please contact the site’s Clozapine Treatment team to identify users who should be assigned as mailgroup coordinator and organizer. An example of how to assign users to a Mail Group is shown below.

Select Systems Manager Menu Option: manage Mailman

Check MailMan Files for Errors

Create a Mailbox for a user

Disk Space Management ...

Group/Distribution Management ...

Local Delivery Management ...

MailMan Site Parameters

Network Management ...

New Features for Managing MailMan

Select Manage Mailman Option: group/Distribution Management

Bulletin edit

Edit Distribution List

Enroll in (or Disenroll from) a Mail Group

Mail Group Coordinator's Edit

Mail Group Coordinator's Edit W/Remotes

Mail Group Edit

Select Group/Distribution Management Option: mail group edit

Select MAIL GROUP NAME: PSOCLOZ

Are you adding 'PSOCLOZ' as a new MAIL GROUP? No// Y (Yes)

MAIL GROUP NAME: PSOCLOZ//

Select MEMBER: HRUBOVCAK,JC JCH SR. LINUX ADMIN

Are you adding 'HRUBOVCAK,JC' as a new MEMBER (the 1ST for this MAIL GROUP)? No// Y (Yes)

TYPE:

Select MEMBER:

DESCRIPTION:

1\>Used for the National Clozapine Center tracking messages.

2\>

EDIT Option:

TYPE: PR private

RESTRICTIONS:

ORGANIZER: HRUBOVCAK,JC//

COORDINATOR: BURKHALTER,WILLIAM WB SR. LINUX ADMIN

Select AUTHORIZED SENDER:

Select MEMBER GROUP NAME:

Select REMOTE MEMBER:

Select DISTRIBUTION LIST:

Select MAIL GROUP NAME:

Installation of PSJ\*5\*327 may be verified by using FileMan. Examples of using FileMan to list the data dictionaries (DD’s) for verification (fields to be verified are listed in red):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Systems Manager Menu Option: FM VA FileMan</p>
<p>VA FileMan Version 22.2</p>
<p>Enter or Edit File Entries</p>
<p>Print File Entries</p>
<p>Search File Entries</p>
<p>Modify File Attributes</p>
<p>Inquire to File Entries</p>
<p>Utility Functions ...</p>
<p>Data Dictionary Utilities ...</p>
<p>Transfer Entries</p>
<p>Other Options ...</p>
<p>Select VA FileMan Option: DATA Dictionary Utilities</p>
<p>List File Attributes</p>
<p>Map Pointer Relations</p>
<p>Check/Fix DD Structure</p>
<p>Find Pointers into a File</p>
<p>Update the META Data Dictionary</p>
<p>Select Data Dictionary Utilities Option: LIst File Attributes</p>
<p>START WITH What File: 52.52 CLOZAPINE PRESCRIPTION OVERRIDES</p>
<p>(4099 entries)</p>
<p>GO TO What File: CLOZAPINE PRESCRIPTION OVERRIDES//</p>
<p>(4099 entries)</p>
<p>Select LISTING FORMAT: STANDARD// GLOBAL MAP</p>
<p>DEVICE: ;80;999 TELNET</p>
<p>GLOBAL MAP DATA DICTIONARY #52.52 -- CLOZAPINE PRESCRIPTION OVERRIDES FILE 6/1</p>
<p>8/19 PAGE 1</p>
<p>STORED IN ^PS(52.52, (4099 ENTRIES) SITE: VISTA.CPRSDEV.VA.GOV UCI: CLOZA,C</p>
<p>LOZA (VERSION 7.0)</p>
<p>-------------------------------------------------------------------------------</p>
<p>This file contains information regarding who, when and why the prohibition on a</p>
<p>prescription for clozapine was overridden by a member of the team. Because of</p>
<p>the nature of this drug and the restrictions placed upon dispensing it, all</p>
<p>fields in this file are not to be edited through the VA File Manager, but are to</p>
<p>be set ONLY through the order entry options of the outpatient pharmacy package.</p>
<p>Reports generated from this file should be generated only from the option</p>
<p>provided by the package. For these reasons, READ, WRITE, DELETE and LAYGO</p>
<p>access to this file are severely restricted.</p>
<p>UNDER NO CIRCUMSTANCES SHOULD THE DATA DICTIONARY FOR THIS FILE</p>
<p>BE MODIFIED</p>
<p>CROSS</p>
<p>REFERENCED BY: PRESCRIPTION NUMBER(A), DATE TIME(B)</p>
<p>^PS(52.52,D0,0)= (#.01) DATE TIME [1D] ^ (#1) PRESCRIPTION NUMBER [2P:52] ^</p>
<p>==&gt;(#2) USER ENTERING [3P:200] ^ (#3) APPROVING TEAM MEMBER</p>
<p>==&gt;[4P:200] ^ (#4) REASON FOR OVERRIDE [5P:52.54] ^ (#5)</p>
<p>==&gt;COMMENTS [6F] ^</p>
<p>^PS(52.52,D0,1)= (#6) SECOND APPROVING TEAM MEMBER [1P:200] ^</p>
<p>Select Data Dictionary Utilities Option: list File Attributes</p>
<p>START WITH What File: 52.54 CLOZAPINE OVERRIDE REASONS (10 entries)</p>
<p>GO TO What File: CLOZAPINE OVERRIDE REASONS// (10 entries)</p>
<p>Select LISTING FORMAT: STANDARD// gloBAL MAP</p>
<p>DEVICE: ;80;999 TELNET</p>
<p>GLOBAL MAP DATA DICTIONARY #52.54 -- CLOZAPINE OVERRIDE REASONS FILE 6/18/19</p>
<p>PAGE 1</p>
<p>STORED IN ^PS(52.54, (10 ENTRIES) SITE: VISTA.CPRSDEV.VA.GOV UCI: CLOZA,CLO</p>
<p>ZA (VERSION 7.0)</p>
<p>-------------------------------------------------------------------------------</p>
<p>This file contains the possible reasons for overriding a Clozapine prescription</p>
<p>or order lockout.</p>
<p>CROSS</p>
<p>REFERENCED BY: OVERRIDE REASON(B)</p>
<p>^PS(52.54,D0,0)= (#.01) OVERRIDE REASON [1F] ^</p>
<p>INPUT TEMPLATE(S):</p>
<p>PRINT TEMPLATE(S):</p>
<p>^DIPT(.01)= CAPTIONED</p>
<p>SORT TEMPLATE(S):</p>
<p>FORM(S)/BLOCK(S):</p>
<p>Select Data Dictionary Utilities &lt;CLOZA&gt; Option: List File Attributes</p>
<p>START WITH What File: 53.8 CLOZAPINE MEDICATION OVERRIDES (57 entries)</p>
<p>GO TO What File: CLOZAPINE MEDICATION OVERRIDES//</p>
<p>(57 entries)</p>
<p>Select LISTING FORMAT: STANDARD// globaL MAP</p>
<p>DEVICE: ;80;999 TELNET</p>
<p>GLOBAL MAP DATA DICTIONARY #53.8 -- CLOZAPINE MEDICATION OVERRIDES FILE 6/18/1</p>
<p>9 PAGE 1</p>
<p>STORED IN ^PS(53.8, (57 ENTRIES) SITE: VISTA.CPRSDEV.VA.GOV UCI: CLOZA,CLOZ</p>
<p>A (VERSION 5.0)</p>
<p>-------------------------------------------------------------------------------</p>
<p>This file contains information regarding who, when and why the prohibition on a</p>
<p>order for clozapine was overridden member of the team. Because of the nature</p>
<p>of this drug and the restrictions placed upon dispensing it, all fields in this</p>
<p>file are not to be edited through the VA File Manager, but are to be set ONLY</p>
<p>through the order entry options of the inpatient pharmacy package. Reports</p>
<p>generated from this file should be generated only from the option provided by</p>
<p>the package. For these reasons, READ, WRITE, DELETE and LAYGO access to this</p>
<p>file are severely restricted.</p>
<p>UNDER NO CIRCUMSTANCES SHOULD THE DATA DICTIONARY FOR THIS FILE</p>
<p>BE MODIFIED</p>
<p>CROSS</p>
<p>REFERENCED BY: ORDER NUMBER(A), DATE TIME(B)</p>
<p>^PS(53.8,D0,0)= (#.01) DATE TIME [1D] ^ (#1) ORDER NUMBER [2P:100] ^ (#2)</p>
<p>==&gt;USER ENTERING [3P:200] ^ (#3) APPROVING TEAM MEMBER [4P:200]</p>
<p>==&gt;^ (#4) REASON FOR OVERRIDE [5P:52.54] ^ (#5) COMMENTS [6F] ^</p>
<p>^PS(53.8,D0,1)= (#6) SECOND APPROVING TEAM MEMBER [1P:200] ^</p>
<p>INPUT TEMPLATE(S):</p>
<p>PRINT TEMPLATE(S):</p>
<p>SORT TEMPLATE(S):</p>
<p>FORM(S)/BLOCK(S):</p>
<p>Select Data Dictionary Utilities &lt;CLOZA&gt; Option: List File Attributes</p>
<p>START WITH What File: PHARMACY PATIENT// (40 entries)</p>
<p>GO TO What File: PHARMACY PATIENT// (40 entries)</p>
<p>Select SUB-FILE: 62 UNIT DOSE</p>
<p>Select SUB-FILE:</p>
<p>Select LISTING FORMAT: STANDARD//</p>
<p>Start with field: FIRST// 301 CLOZAPINE DOSAGE (MG/DAY)</p>
<p>Go to field: 301 CLOZAPINE DOSAGE (MG/DAY)</p>
<p>DEVICE: ;80;999 TELNET</p>
<p>STANDARD DATA DICTIONARY #55.06 -- UNIT DOSE SUB-FILE 6/18/19 PAGE 1</p>
<p>STORED IN ^PS(55,D0,5, SITE: VISTA.CPRSDEV.VA.GOV UCI: CLOZA,CLOZA</p>
<p>DATA NAME GLOBAL DATA</p>
<p>ELEMENT TITLE LOCATION TYPE</p>
<p>-------------------------------------------------------------------------------</p>
<p>55.06,301 CLOZAPINE DOSAGE (MG/DAY) SAND;1 NUMBER</p>
<p>INPUT TRANSFORM: K:+X'=X!(X&gt;3000)!(X&lt;0)!(X?.E1"."1N.N) X</p>
<p>LAST EDITED: JUN 06, 2016</p>
<p>HELP-PROMPT: Type a number between 0 and 3000, 0 decimal</p>
<p>digits.</p>
<p>DESCRIPTION: This is the total daily dosage of clozapine if</p>
<p>this order is for the drug clozapine. This is</p>
<p>used only for clozapine.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KIDS post-installation scripts perform all necessary system configuration required by the build. There are no additional actions required.

# Backout Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the VistA Installation Procedure of the KIDS build, the installer has backed up the modified routines by using the *Backup a Transport Global action*. The installer can restore the routines using the MailMan message that were saved prior to installing the patch. See Appendix C for details on backing out database and order rules checking routines. All software components (routines and other items) must be restored to their previous state at the same time and in conjunction with restoration of the data.

This backout may need to include a database cleanup process.

Contact the product development team for assistance if the installed patch that needs to be backed out contains anything at all other than routines, before trying to back out the patch. If the installed patch that needs to be backed out includes a pre- or post-install routine, please contact the product development team before attempting the backout.

## Backout Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During installation, if the option to back up routines was performed, ‘Backup a Transport Global,’ then sites can restore routines from the backup PackMan message that was generated. The KIDS installation software does not restore other VistA components, such as data dictionaries, cross-references, template changes, etc. Refer to Appendix D for specific steps to back out other components of the multi-build.

Prior to attempting a backout of the software, please contact the IT Enterprise Service Desk at 1-855-673-4357 for support or assistance.

## Backout Considerations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Pharmacy ADPAC and OI&T have the authority to order the backout.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The User Acceptance Testing was conducted by the test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases for the first build of MENTAL HEALTH NCC PROJECT 5.01. The sites either passed or failed any item based on testing. Any items that failed were corrected and sent back to the sites via a new build for further acceptance testing following the same process. Once in production, the test cases from the last build were performed in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Backout Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Criteria for a backout include, but are not limited, to the following:

1.  Failed baseline testing.
2.  Non-recoverable software error.

## Backout Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Client data entered prior to the backout may be lost depending on the circumstances surrounding the backout (e.g., backout performed after several hours after new release deployed to production and several hours of client data being received, etc.).

## Authority for Backout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authorization for a backout includes a combination of the Chief of Pharmacy, Chief of Mental Health and Chief of Staff and Director of the Facility.

## Backout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The YS\*5.01\*122, PSO\*7\*457, PSJ\*5\*327, OR\*3\*427 patches (part of the combined build, NCC Build 3) as well as any installed dependent patch changes that follow these releases need to be taken out in reverse of the order in which they were installed; routines and data dictionary modifications and populated data must also be rolled back in reverse order.

Please contact the IT Enterprise Service Desk at 1-855-673-4357 for support or assistance regarding roll-back procedures.

## Backout Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inspect the versions of the YS, PSO, PSJ and OR prior to installation.

Please contact the IT Enterprise Service Desk at 1-855-673-4357 for support or assistance regarding roll-back procedures.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The YS\*5.01\*122, PSO\*7\*457, PSJ\*5\*327, OR\*3\*427 patches (part of the combined build, NCC Release 1), as well as any installed dependent patch changes that follow these releases, need to be removed reverse order in which they were installed; routines, data dictionary modifications, and populated data must also be rolled back in reverse order.

Please contact the IT Enterprise Service Desk at 855-673-4357 for support or assistance regarding roll-back procedures.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No rollback considerations have been determined at this time.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only criterion for a rollback that has been determined at this time is that the installation failed baseline testing and the software has been backed out as described in Section 5 of this document.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Client data entered prior to the rollback may be lost depending on the circumstances surrounding the rollback (i.e., rollback performed after several hours after new release deployed to production and several hours of client data being received, etc.).

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authorization for a rollback includes a combination of the Chief of Pharmacy, Chief of Mental Health and Chief of Staff and Director of the Facility.

## Rollback Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The need for a rollback is highly unlikely, however if it is required, contact the product development team for assistance if needed. The rollback procedure may require Pharmacy downtime and a reinstall of any previous KIDS versions. Additional files, options and settings will be ignored by the prior versions of the patches and do not present an operational risk.

Refer to Appendix C and D for steps to remove the following data dictionary changes:

| CLOZAPINE OVERRIDE REASONS (52.54)       | File  | New      |
|------------------------------------------|-------|----------|
| CLOZAPINE PRESCRIPTION OVERRIDES (52.52) | File  | Modified |
| REASON FOR OVERRIDE \#4                  | Field | Modified |
| CLOZAPINE MEDICATION OVERRIDES  (53.8)   | File  | New      |
| PHARMACY PATIENT (55)                    | File  | Modified |
| sub-file UNIT DOSE (50.06)               | File  | Modified |
| CLOZAPINE DOSAGE (MG/DAY) \#301          | Field | New      |
| CLOZAPINE PARAMETERS (603.03)            | File  | Modified |
| RX LAB PROD LISTENER \#8                 | Field | New      |
| DEMOGRAPHIC PROD LISTENER \#9            | Field | New      |
| RX LAB TEST LISTENER \#10                | Field | New      |
| DEMOGRAPHIC TEST LISTENER \#11           | Field | New      |

## Rollback Verification Procedure 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After backing out Patch PSJ\*5\*327, PSO\*7\*457 and YS\*5.01\*122 the Database may be verified by running a global listings from the VistA server command line. Global listings should be performed for the following global nodes, after which the following should be listed if the backout was successful:

Global listings should be performed for the following global nodes:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Global ^DD(52.52,4,0</p>
<p>Global ^DD(52.54,,0</p>
<p>Global ^DD(53.8,,0</p>
<p>Global ^DD(55.06,301,0</p>
<p>Global ^DD(603.03,8:11,0</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Example:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>SUPISC1A2:ARC&gt;D ^%G</p>
<p>Global <strong>^DD(52.52,4,0</strong> -- NOTE: translation in effect</p>
<p>^DD(52.52,4,0)="REASON FOR OVERRIDE^RS^1:NO WBC IN LAST 7 DAYS;2:NO VERIFIED WBC</p>
<p>;3:LAST WBC RESULT &lt; 3500;4:3 SEQ. WBC DECREASE;5:LAST ANC RESULT &lt; 2000;6:3 SEQ</p>
<p>. ANC DECREASE ;7:NCCC AUTHORIZED;^0;5^Q"</p>
<p>For help on global specifications DO HELP^%G</p>
<p>Global <strong>^DD(52.54,,0</strong> -- NOTE: translation in effect</p>
<p>&lt;Nothing should be displayed&gt;</p>
<p>Global <strong>^DD(53.8,,0</strong> -- NOTE: translation in effect</p>
<p>&lt;Nothing should be displayed&gt;</p>
<p>Global <strong>^DD(55.06,301,0</strong> -- NOTE: translation in effect</p>
<p>&lt;Nothing should be displayed&gt;</p>
<p>Global ^<strong>DD(603.03,8:11,0</strong> -- NOTE: translation in effect</p>
<p>&lt;Nothing should be displayed&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  <span id="APX_A" class="anchor"></span>Installation Log for 7.3.0 Build

> **NOTE:** Your installation feedback will be different than the log shown below. The log shown below is for a site which has previously installed MENTAL HEALTH NCC PROJECT 5.01.

Select OPTION NAME: XPD Main Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option:

Installation

Edits and Distribution ...

Utilities ...

Installation ...

Patch Monitor Main Menu ...

Select Kernel Installation & Distribution System Option:

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 1 Load a Distribution

Enter a Host File: /home/chy0009/MH_NCC_PROJECT_5_01.KID

KIDS Distribution saved on Jun 12, 2019@13:46:02

Comment: T23 build June 12, 2019 YS\*5.01\*122, PSO\*7.0\*457, PSJ\*5.0\*327, OR\*3.0\*4

2

This Distribution contains Transport Globals for the following Package(s):

Build MENTAL HEALTH NCC PROJECT 5.01 has been loaded before, here is when:

was loaded on May 11, 2019@11:15:13

MENTAL HEALTH NCC PROJECT 5.01 Install Completed

was loaded on May 14, 2019@11:02:10

MENTAL HEALTH NCC PROJECT 5.01 Install Completed

was loaded on May 23, 2019@09:49:14

MENTAL HEALTH NCC PROJECT 5.01 Install Completed

was loaded on Jun 04, 2019@10:11

OK to continue with Load? NO// YES

Build YS\*5.01\*122 has been loaded before, here is when:

was loaded on May 11, 2019@11:15:13

YS\*5.01\*122 Install Completed

was loaded on May 14, 2019@11:02:10

YS\*5.01\*122 Install Completed

was loaded on May 23, 2019@09:49:14

YS\*5.01\*122 Install Completed

was loaded on Jun 04, 2019@10:11

OK to continue with Load? NO// YES

Build PSO\*7.0\*457 has been loaded before, here is when:

was loaded on May 11, 2019@11:15:14

PSO\*7.0\*457 Install Completed

was loaded on May 14, 2019@11:02:12

PSO\*7.0\*457 Install Completed

was loaded on May 23, 2019@09:49:19

PSO\*7.0\*457 Install Completed

was loaded on Jun 04, 2019@10:11:05

OK to continue with Load? NO// YES

Build PSJ\*5.0\*327 has been loaded before, here is when:

was loaded on May 11, 2019@11:15:14

PSJ\*5.0\*327 Install Completed

was loaded on May 14, 2019@11:02:13

PSJ\*5.0\*327 Install Completed

was loaded on May 23, 2019@09:49:20

PSJ\*5.0\*327 Install Completed

was loaded on Jun 04, 2019@10:11:06

OK to continue with Load? NO// YES

Build OR\*3.0\*427 has been loaded before, here is when:

was loaded on May 11, 2019@11:15:14

OR\*3.0\*427 Install Completed

was loaded on May 14, 2019@11:02:13

OR\*3.0\*427 Install Completed

was loaded on May 23, 2019@09:49:21

OR\*3.0\*427 Install Completed

was loaded on Jun 04, 2019@10:11:08

OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES//

Loading Distribution...

MENTAL HEALTH NCC PROJECT 5.01

YS\*5.01\*122

PSO\*7.0\*457

PSJ\*5.0\*327

OR\*3.0\*427

Use INSTALL NAME: MENTAL HEALTH NCC PROJECT 5.01 to install this Distribution.

Select INSTALL NAME: MENTAL HEALTH NCC PROJECT 5.01 6/12/19@23:34:38

=\> T23 build June 12, 2019 YS\*5.01\*122, PSO\*7.0\*457, PSJ\*5.0\*327, OR\*3.0\*

This Distribution was loaded on Jun 12, 2019@23:34:38 with header of

T23 build June 12, 2019 YS\*5.01\*122, PSO\*7.0\*457, PSJ\*5.0\*327, OR\*3.0\*42 ;Created on Jun 12, 2019@13:46:02

It consisted of the following Install(s):

MENTAL HEALTH NCC PROJECT 5.01 YS\*5.01\*122 PSO\*7.0\*457 PSJ\*5.0\*327

OR\*3.0\*427

Checking Install for Package MENTAL HEALTH NCC PROJECT 5.01

Install Questions for MENTAL HEALTH NCC PROJECT 5.01

Checking Install for Package YS\*5.01\*122

Install Questions for YS\*5.01\*122

Incoming Files:

603.03 CLOZAPINE PARAMETERS (Partial Definition)

> **NOTE:** You already have the 'CLOZAPINE PARAMETERS' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Checking Install for Package PSO\*7.0\*457

Install Questions for PSO\*7.0\*457

Incoming Files:

52.52 CLOZAPINE PRESCRIPTION OVERRIDES (Partial Definition)

> **NOTE:** You already have the 'CLOZAPINE PRESCRIPTION OVERRIDES' File.

52.54 CLOZAPINE OVERRIDE REASONS (including data)

> **NOTE:** You already have the 'CLOZAPINE OVERRIDE REASONS' File.

Data will NOT be added.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Checking Install for Package PSJ\*5.0\*327

Install Questions for PSJ\*5.0\*327

Incoming Files:

53.8 CLOZAPINE MEDICATION OVERRIDES

> **NOTE:** You already have the 'CLOZAPINE MEDICATION OVERRIDES' File.

55 PHARMACY PATIENT (Partial Definition)

> **NOTE:** You already have the 'PHARMACY PATIENT' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

Checking Install for Package OR\*3.0\*427

Install Questions for OR\*3.0\*427

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// ;;99999 HOME (CRT)

--------------------------------------------------------------------------------

Install Started for MENTAL HEALTH NCC PROJECT 5.01 :

Jun 12, 2019@23:49:17

Build Distribution Date: Jun 12, 2019

Installing Routines:

Jun 12, 2019@23:49:17

Install Started for YS\*5.01\*122 :

Jun 12, 2019@23:49:17

Build Distribution Date: Jun 12, 2019

Installing Routines:

Jun 12, 2019@23:49:17

Running Pre-Install Routine: BKGRD^YSCLTEST

Installing Data Dictionaries:

Jun 12, 2019@23:49:17

Installing PACKAGE COMPONENTS:

Installing OPTION

Jun 12, 2019@23:49:17

Running Post-Install Routine: START^YSCL122P

Updating Routine file...

Updating KIDS files...

YS\*5.01\*122 Installed.

Jun 12, 2019@23:49:21

Not a production UCI

NO Install Message sent

Install Started for PSO\*7.0\*457 :

Jun 12, 2019@23:49:21

Build Distribution Date: Jun 12, 2019

Installing Routines:

Jun 12, 2019@23:49:21

Installing Data Dictionaries:

Jun 12, 2019@23:49:21

Installing Data:

Jun 12, 2019@23:49:21

Installing PACKAGE COMPONENTS:

Installing OPTION

Jun 12, 2019@23:49:21

Running Post-Install Routine: POST^PSO457P

Checking for Clozapine Registry data in ^XTMP. Jun 12, 2019@23:49:21

Clozapine Registry data in ^XTMP updated.

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*457 Installed.

Jun 12, 2019@23:49:21

Not a production UCI

NO Install Message sent

Install Started for PSJ\*5.0\*327 :

Jun 12, 2019@23:49:21

Build Distribution Date: Jun 12, 2019

Installing Routines:

Jun 12, 2019@23:49:21

Installing Data Dictionaries: .

Jun 12, 2019@23:49:22

Installing PACKAGE COMPONENTS:

Installing OPTION

Jun 12, 2019@23:49:22

Running Post-Install Routine: ADDMENUS^PSJ327P

Updating Routine file...

The following Routines were created during this install:

PSSJXR

PSSJXR1

PSSJXR10

PSSJXR11

PSSJXR12

PSSJXR13

PSSJXR14

PSSJXR15

PSSJXR16

PSSJXR17

PSSJXR18

PSSJXR19

PSSJXR2

PSSJXR20

PSSJXR21

PSSJXR22

PSSJXR23

PSSJXR24

PSSJXR25

PSSJXR26

PSSJXR27

PSSJXR28

PSSJXR29

PSSJXR3

PSSJXR30

PSSJXR31

PSSJXR32

PSSJXR33

PSSJXR34

PSSJXR35

PSSJXR36

PSSJXR37

PSSJXR38

PSSJXR39

PSSJXR4

PSSJXR40

PSSJXR5

PSSJXR6

PSSJXR7

PSSJXR8

PSSJXR9

Updating KIDS files...

PSJ\*5.0\*327 Installed.

Jun 12, 2019@23:49:22

Not a production UCI

NO Install Message sent

Install Started for OR\*3.0\*427 :

Jun 12, 2019@23:49:22

Build Distribution Date: Jun 12, 2019

Installing Routines:

Jun 12, 2019@23:49:22

Running Post-Install Routine: ^ORY427ES .

Order Check Expert System Rule Transporter

Created: MAR 7,2017 at 15:12 at NCCLAB1.AAC.VA.GOV

Current Date: JUN 12,2019 at 23:49 at CHY0009.FO-BAYPINES.MED.VA.GOV

Loading Data . . . . . . . .

Installing '863.8 OCX MDD PARAMETER' records... .

------------Inconsistent word Data---------------------------------

OCX MDD PARAMETER: COMPARISON VALUE \[172\]

DESCRIPTION field \[1\] Line \#1

\(L\) CHY0009.FO-BAYPINES.MED.VA.GOV: This is a value to be cD

. . . . . . . . . . . . . . . . . . .

------------Inconsistent word Data---------------------------------

OCX MDD PARAMETER: PRIMARY DATA FIELD \[171\]

DESCRIPTION field \[1\] Line \#1

\(L\) CHY0009.FO-BAYPINES.MED.VA.GOV: Primary data field in a t

. . . .

Installing '864.1 OCX MDD DATATYPE' records... . . . .

Installing '863.7 OCX MDD PUBLIC FUNCTION' records... . . . . . .

Installing '863.9 OCX MDD CONDITION/FUNCTION' records... . . . . . .

Installing '863.4 OCX MDD ATTRIBUTE' records... . . . . . . . . . .

.

Installing '863.2 OCX MDD SUBJECT' records... .

Installing '863.3 OCX MDD LINK' records... . . . . . . . . . . . .

Installing '860.9 ORDER CHECK NATIONAL TERM' records... . . . . . .

. . . . . . . . .

Installing '860.8 ORDER CHECK COMPILER FUNCTIONS' records... . . . .

. . . . .

------------Inconsistent word Data---------------------------------

ORDER CHECK COMPILER FUNCTIONS: LOCAL TERM LOOKUP \[38\]

DESCRIPTION field \[1\] Line \#1

\(L\) CHY0009.FO-BAYPINES.MED.VA.GOV: This function allows a lg

. . .

Installing '860.6 ORDER CHECK DATA CONTEXT' records... . . . .

Installing '860.5 ORDER CHECK DATA SOURCE' records... . . . . .

Installing '860.4 ORDER CHECK DATA FIELD' records... . . . . . . . .

.

Installing '860.3 ORDER CHECK ELEMENT' records... . . . . .

Installing '860.2 ORDER CHECK RULE' records... .

No data filing errors.

Transport Finished...

---Creating Order Check Routines-----------------------------------

Build list of Active Rules, Elements and Datafields...

96 DATA FIELDS

77 ELEMENTS

39 RULES

Compile DataField Navigation code...

101 DataField Navigation Code Arrays

Compile Element Evaluation code...

71 Event Evaluation Code Arrays

Compile Element MetaCode...

77 Element Metacode Arrays

Get Compiler Function Code...

51 Compiler Include Functions

Compile Rule Element Relation code...

55 Rule Element Relation Code Arrays

Construct Decision Tree...

689 Sub-Routines

Optimize Sub-Routines...

276 Sub-Routines

60% Optimization

Assemble Routines...

38 OCXOZ\* Routines

Updating Routine file...

Updating KIDS files...

OR\*3.0\*427 Installed.

Jun 12, 2019@23:49:23

Not a production UCI

NO Install Message sent

Updating Routine file...

Updating KIDS files...

MENTAL HEALTH NCC PROJECT 5.01 Installed.

Jun 12, 2019@23:49:23

No link to PACKAGE file

NO Install Message sent

Call MENU rebuild

Starting Menu Rebuild: Jun 12, 2019@23:49:25

Collecting primary menus in the New Person file...

Primary menus found in the New Person file

------------------------------------------

OPTION NAME MENU TEXT \# OF LAST LAST

USERS USED BUILT

DIUSER VA FileMan 2 01/29/18 05/11/19

XMUSER MailMan Menu 394 01/29/18 05/11/19

EVE Systems Manager Menu 92 06/12/19 05/11/19

XUSER User Management 3 01/29/18 05/11/19

SDMGR Scheduling Manager's Menu 1 01/19/18 05/11/19

YSUSER Mental Health 144 01/29/18 05/11/19

PSO MANAGER Outpatient Pharmacy Manager 19 01/29/18 05/11/19

DG BED CONTROL Bed Control Menu 1 01/29/18 05/11/19

Building secondary menu trees....

Merging.... done.

Install Completed

2.  <span id="APX_B" class="anchor"></span>Daily Transmission Details

The VistA Daily Clozapine Transmission \[YSCL DAILY TRANSMISSION\] option is designed to transmit the Clozapine dispensing, lab data, and demographics information for all Inpatient and Outpatient Clozapine dispenses from the previous day’s dispenses and has been designed to only send the data once a day.

1.  VistA Daily Clozapine Transmission \[YSCL DAILY TRANSMISSION\]

The VistA Daily Clozapine Transmission \[YSCL DAILY TRANSMISSION\] option should be queued to run after midnight via TaskMan. If needed, it can also be run manually in the foreground.

Example: Scheduling the new Daily Transmission OptionNote: The option should be scheduled to run daily during off-peak. Sites should choose an appropriate time based on their workload.

Select Systems Manager Menu Option: TASKman Management

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: SCHEDULe/Unschedule Options

Select OPTION to schedule or reschedule: YSCL DAILY TRANSMISSION

Daily Clozapine Transmission

Are you adding 'YSCL DAILY TRANSMISSION' as

a new OPTION SCHEDULING (the 17TH)? No// Y (Yes)

Edit Option Schedule

Option Name: YSCL DAILY TRANSMISSION

Menu Text: Daily Clozapine Transmission TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: JUL 9,2019@01:30

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh Quit

When this option runs, it sends a Mailman message to mail group:

Clozapine Discontinued Patient - CLOZAPINE ROLL-UP@FORUM.VA.GOV

The mailman message to NCCC contains the Patients’ SSN, name and reason for why the patient has been discontinued.

Example: Discontinued Clozapine Patient Mailman message to NCCC

Subj: *Facility* Discontinued Status \[#228489\] 02/03/17@10:16 7 lines

From: CLOZAPINE MONITOR In 'IN' basket. Page 1 \*New\*

-----------------------------------------------------------------------------

GHAAHU,JLUASXY W CU (2501)

The patient status has changed to 'Discontinued' because the new clozapine

patient has not filled the prescription/order within 28 days of being marked

'Active'.

KHLSH,INALY U (2700)

The patient status has changed to 'Discontinued' because the temporary local

authorization number assigned has expired and NCCC has not issued a new

authorization number.

MHIERT,LIXAGX U (5537)

The patient status has changed to 'Discontinued' because the active clozapine

patient has not filled the prescription/order within 56 days of being

prescribed/ordered.

Mailman message to mail group:

Clozapine demographics - RUCLDEM@FO-DALLAS.MED.VA.GOV

This message contains the Patients’ SSN and name

Example: Clozapine demographics - Mailman message to NCC

Subj: Clozapine demographics \[#228491\] 02/03/17@10:28 14 lines

From: CLOZAPINE MONITOR In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Clozapine demographic data was transmitted, 4 records were sent.

For the following patients, one or more of the required data

elements (race, sex, ZIP code) were missing.

Please have this information entered.

The available data was transmitted.

101086586 LDAN,AHPDT H (RACE, NEW FORMAT) (ETHNICITY)

> **NOTE:** Race and Ethnicity may be entered if permission is obtained in the informed

Consent document. See VHA Directive 99-035.

101039337 AAA,AXRDH Z (RACE, NEW FORMAT) (ETHNICITY)

> **NOTE:** Race and Ethnicity may be entered if permission is obtained in the informed

Consent document. See VHA Directive 99-035.

Mailman message to mail group:

Clozapine lab data - RUCLRXLAB@FO-DALLAS.MED.VA.GOV

This message contains the number of records transmitted to the NCCC Server.

SSN, name, lab result date, WBC date and the Neutrophil date.

Example: Clozapine lab data - Mailman message to NCC

Subj: Clozapine lab data @ <span class="mark">REDACTED</span> VAMC on 3170111 at 02 \[#216721\]

01/11/17@02:00 12 lines

From: CLOZAPINE MONITOR In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

Clozapine lab data was transmitted, 11 records were sent

In message \# 216720

101074507 AAADTSXY,QLYJH U (R) Jan 10, 2017 (W) Jan 10, 2017 (N) Jan 10, 2017

101028121 ZXUY,QLYJH K (R) Jan 10, 2017 (W) Jan 09, 2017 (N) Jan 09, 2017

101039337 AAA,AXRDH Z (R) Jan 10, 2017 (W) Jan 10, 2017 (N) NO NEUT

101039337 AAA,AXRDH Z (R) Jan 10, 2017 (W) Jan 10, 2017 (N) NO NEUT

101040657 AJXJB,TLRA HIPLUI (R) Jan 04, 2017 (W) Jan 10, 2017 (N) Jan 10, 2017

101040657 AJXJB,TLRA HIPLUI (R) Jan 10, 2017 (W) Jan 10, 2017 (N) Jan 10, 2017

101049185 GALI,LKHA A (R) Jan 10, 2017 (W) Jan 05, 2017 (N) Jan 05, 2017

101077432 BXADLY,TXY A (R) Jan 10, 2017 (W) Jan 10, 2017 (N) NO NEUT

101077432 BXADLY,TXY A (R) Jan 10, 2017 (W) Jan 10, 2017 (N) NO NEUT

2.  VistA Retransmit Clozapine Roll-up Data \[YSCL RETRANSMIT DATA\]

The VistA Retransmit Clozapine Roll-up Data \[YSCL RETRANSMIT DATA\] option has been added in the event the NCCC needs to resend the Clozapine Data to the NCCC Server. The NCC application coordinator at each site will determine who is assigned the option.

This option can send a single day’s transactions or consecutive days of transactions. This option must be run manually in VistA.

When running the option, the user will need to provide the start date and ending date for re-transmission. The system will then create and send the Clozapine lab data via a MailMan message to the NCC.

Example: Retransmit Clozapine Roll-up Data

![](ys-5-01-122-ncc-deployment-installation-back-out-and-rollback-guide/003.png)

3.  Options Being Disabled by this Patch

The VistA Weekly Clozapine Report \[YSCL WEEKLY TRANSMISSION\] and the Transmit Clozapine Demographics \[YSCL TRANSMIT DEMOGRAPHICS\] options have been marked ‘Out of Service’ and display ‘Replaced by the Daily Clozapine Transmission’ message.

Verification of the OPTION entries being disabled:

Select VA FileMan \<CLOZA\> Option: Inquire to File Entries

Output from what File: OPTION// (10342 entries)

Select OPTION NAME: YSCL WEEKLY TRANSMISSION Weekly Clozapine Report

Another one: YSCL TRANSMIT DEMOGRAPHICS Transmit Clozapine Demographics

Another one:

Standard Captioned Output? Yes// N (No)

First Print FIELD: .01 NAME

Then Print FIELD: 1 MENU TEXT

Then Print FIELD: OUT OF ORDER MESSAGE

Then Print FIELD:

Heading (S/C): OPTION List//

DEVICE: TELNET

OPTION List JUL 08, 2019@14:42 PAGE 1

NAME

MENU TEXT

OUT OF ORDER MESSAGE

--------------------------------------------------------------------------------

YSCL WEEKLY TRANSMISSION

Weekly Clozapine Report

Replaced by YSCL DAILY TRANSMISSION

YSCL TRANSMIT DEMOGRAPHICS

Transmit Clozapine Demographics

Replaced by YSCL DAILY TRANSMISSION.

3.  <span id="_Toc13763402" class="anchor"></span>Order Checking Rules Backout

> **WARNING:** Do not attempt rollback without contacting the Clozapine Modernization development team.

The Clozapine project implemented several order checking rules to comply with the project’s requirements. As part of the roll-back and backout, those rules need to be restored to the prior state. The below semi-manual steps are required to restore the order checking rules to their prior state.

1.  Edit the CLOZAPINE record (57) in the  Order Rule file (#860.2) to the ‘before values’ (See Order Rule File previous settings below Appendix C.1)
2.  Compile the Order Rule file (#860.2) 
3.  Use the commands provided in Appendix D to revert the data dictionary (File \#603.03), File \#52.52. changes, File 52.54, File 53.8, and a field in File 55.
4.  Restore YS, PSO, PSJ, OR routines from the Backup of YS\*5.01\*122 install
4.  <span id="_Toc13763403" class="anchor"></span>Order Entry Rules Settings for Backout

ORDER CHECK RULE LIST                        

-----------------------------------------------------------------------------

NUMBER: 57                              NAME: CLOZAPINE

LABEL: NO WBC W/IN 7 DAYS

  ELEMENT NAME: CLOZAPINE NO WBC W/IN 7 DAYS

  TYPE: SIMPLE DEFINITION

LABEL: WBC \< 3.0                        ELEMENT NAME: CLOZAPINE WBC \< 3.0

  TYPE: SIMPLE DEFINITION

LABEL: ANC \< 1.5                        ELEMENT NAME: CLOZAPINE ANC \< 1.5

  TYPE: SIMPLE DEFINITION

LABEL: 3.0 \<= WBC \< 3.5

  ELEMENT NAME: CLOZAPINE WBC \>= 3.0 & \< 3.5

  TYPE: SIMPLE DEFINITION

LABEL: NO ANC W/IN 7 DAYS

  ELEMENT NAME: CLOZAPINE NO ANC W/IN 7 DAYS

  TYPE: SIMPLE DEFINITION

LABEL: CLOZAPINE                        ELEMENT NAME: CLOZAPINE DRUG SELECTED

  TYPE: SIMPLE DEFINITION

LABEL: ANC \>= 1.5                       ELEMENT NAME: CLOZAPINE ANC \>= 1.5

  TYPE: SIMPLE DEFINITION

LABEL: WBC \>= 3.5                       ELEMENT NAME: CLOZAPINE WBC \>= 3.5

  TYPE: SIMPLE DEFINITION

LABEL: 1.5 \<= ANC \< 2.0

  ELEMENT NAME: CLOZAPINE ANC \>= 1.5 & \< 2.0

 TYPE: SIMPLE DEFINITION

  STATUS: ACTIVE

RELATION INDEX: 1                       ORDER CHECK: CLOZAPINE APPROPRIATENESS

  RELATION EXPRESSION: CLOZAPINE AND (NO WBC W/IN 7 DAYS OR NO ANC W/IN 7 DAYS)

  ORDER CHECK MESSAGE: Clozapine orders require a CBC/Diff within past 7 days. 

                       Please order CBC/Diff with WBC and ANC immediately.

                       Most recent results - \|CLOZ LAB RSLTS\|

RELATION INDEX: 2                       ORDER CHECK: CLOZAPINE APPROPRIATENESS

  RELATION EXPRESSION: CLOZAPINE AND (WBC \< 3.0 OR ANC \< 1.5)

  ORDER CHECK MESSAGE: WBC \< 3.0 and/or ANC \< 1.5 - pharmacy cannot fill

                       clozapine  order. Most recent results - \|CLOZ LAB RSLTS\|

RELATION INDEX: 3                       ORDER CHECK: CLOZAPINE APPROPRIATENESS

  RELATION EXPRESSION: CLOZAPINE AND 3.0 \<= WBC \< 3.5 AND ANC \>= 1.5

  ORDER CHECK MESSAGE: WBC between 3.0 and 3.5 with ANC \>= 1.5 - please repeat

                       CBC/Diff including WBC and ANC immediately and twice

                        weekly.  Most recent results - \|CLOZ LAB RSLTS\|

RELATION INDEX: 4                       ORDER CHECK: CLOZAPINE APPROPRIATENESS

  RELATION EXPRESSION: CLOZAPINE AND 1.5 \<= ANC \< 2.0

  ORDER CHECK MESSAGE: ANC between 1.5 and 2.0 - please repeat CBC/Diff

                       including WBC and ANC immediately and twice weekly.

                       Most recent results - \|CLOZ LAB RSLTS\|
5.  
6.  <span id="_Toc13763404" class="anchor"></span>Backout Steps

> **WARNING:** Do not attempt rollback without contacting the Clozapine Modernization development team.

7.  <span id="_Toc13763405" class="anchor"></span>Remove Data Dictionary File 52.54

To permanently remove the file from the data dictionary, the developer should enter the following:

VISTA\> S DIK=”^DIC(“,DA=52.54 D ^DIK \<Enter\>

VISTA\>K ^DD(52.54),^PS(52.54) removes data too

8.  <span id="_Toc13763406" class="anchor"></span>Modify Field 4 of the File 52.52

To change field 4 of the file 52.52 back to pre-install, the developer should use FileMan:

VISTA\>D P^DI

VA FileMan 22.2

Select OPTION: MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES//

Modify what File: CLOZAPINE PRESCRIPTION OVERRIDES// (515 entries)

Select FIELD: 4 REASON FOR OVERRIDE

Field \#4 in File \#52.52

FIELD LABEL: REASON FOR OVERRIDEDATA TYPE...SET



CODE: 1WILL STAND FOR: NO WBC IN LAST 7 DAYS 

CODE: 2 WILL STAND FOR: NO VERIFIED WBC 

CODE: 3 WILL STAND FOR: LAST WBC RESULT \< 3500 

CODE: 4 WILL STAND FOR: 3 SEQ. WBC DECREASE 

CODE: 5 WILL STAND FOR: LAST ANC RESULT \< 2000 

CODE: 6 WILL STAND FOR: 3 SEQ. ANC DECREASE 

CODE: 7 WILL STAND FOR: NCCC AUTHORIZED 

CODE: WILL STAND FOR: 

CODE: WILL STAND FOR: 

CODE: WILL STAND FOR: 

CODE: WILL STAND FOR: 

CODE: WILL STAND FOR: 

CODE: WILL STAND FOR: 



Field \#4 in File \#52.52

FIELD LABEL: REASON FOR OVERRIDEDATA TYPE...SET

TITLE:

AUDIT:

AUDIT CONDITION:

READ ACCESS:

DELETE ACCESS: ^

WRITE ACCESS: ^

SOURCE:

DESCRIPTION... TECHNICAL DESCRIPTION...

IS THIS FIELD MULTIPLE... NO

MANDATORY: YES

HELP-PROMPT: Enter the reason for the override of this prescription.

XECUTABLE HELP:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh Quit

Enter a COMMAND, or "^" followed by the CAPTION of a FIELD to jump to.

COMMAND: EPress \<PF1\>H for helpInsert

SINCE YOU HAVE CHANGED THE FIELD DEFINITION,

EXISTING 'REASON FOR OVERRIDE' DATA WILL NOW BE CHECKED FOR INCONSISTENCIES

OK? Yes// N (No)

9.  <span id="_Toc13763407" class="anchor"></span>Remove Data Dictionary File 53.8

To permanently remove the file from the data dictionary, the developer enters the following:

\*\*\* Warning: This should only be done by a programmer familiar with VistA utilities and conventions. A mistake could cause severe data loss. \*\*\*

VISTA\> S DIK=”^DIC(“,DA=53.8 D ^DIK

; the following command removes data too

VISTA\>K ^DD(53.8),^PS(53.8)

10. <span id="_Toc13763408" class="anchor"></span>Remove Field 301 from File 55

To remove the field 301 definition from the file 55, the developer should use FileMan:

VISTA\>D P^DI

VA FileMan 22.2

Select OPTION: MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES// NO

Modify what File: PHARMACY PATIENT// (44820 entries)

Select FIELD: UNIT DOSE (multiple)

LABEL: UNIT DOSE//

READ ACCESS (OPTIONAL):

WRITE ACCESS (OPTIONAL):

SOURCE:

Select DESTINATION:

Select GROUP: PSJU//

DESCRIPTION:

1\> This represents the 'top' of the UNIT DOSE SUB-FILE, where all of

2\>a patient's active (and expired & dc'd) UNIT DOSE orders are kept.

3\>Although orders are initially entered into ^PS(53.1), the order is

4\>transferred into this sub-file (^PSGOT) upon verification.

EDIT Option:

TECHNICAL DESCRIPTION:

1\>

Select UNIT DOSE SUB-FIELD: 301 CLOZAPINE DOSAGE (MG/DAY)

LABEL: CLOZAPINE DOSAGE (MG/DAY) Replace @

SURE YOU WANT TO DELETE THE ENTIRE 'CLOZAPINE DOSAGE (MG/DAY)' UNIT DOSE SUB-FIELD? Y (Yes)

11. <span id="_Toc13763409" class="anchor"></span>Remove Fields 8-11 from File 603.03

To remove fields 8-11 definition from the file 603.03, the developer should use FileMan:

VISTA\>D P^DI

VA FileMan 22.2

Select OPTION: MODIFY FILE ATTRIBUTES

Do you want to use the screen-mode version? YES// YES

Modify what File: CLOZAPINE OVERRIDE REASONS// 603.03 CLOZAPINE PARAMETERS

(1 entry)

Select FIELD: 8 RX LAB PROD LISTENER

Field \#8 in File \#603.03

FIELD LABEL: DATA TYPE...FREE TEXT



 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

 ARE YOU SURE YOU WANT TO DELETE THE ENTIRE FIELD: YES 

AUDIT CON \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

READ 

DELETE ACCESS:

WRITE ACCESS:

SOURCE:

DESCRIPTION... TECHNICAL DESCRIPTION...

IS THIS FIELD MULTIPLE... NO

MANDATORY: NO

HELP-PROMPT: Answer must be 5-40 characters in length.

XECUTABLE HELP:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

OK TO DELETE 'RX LAB PROD LISTENER' FIELDS IN THE EXISTING ENTRIES? Yes//Y (Yes)

Select FIELD: 9 DEMOGRAPHIC PROD LISTENER

Field \#9 in File \#603.03

FIELD LABEL: DATA TYPE...FREE TEXT



 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

 ARE YOU SURE YOU WANT TO DELETE THE ENTIRE FIELD: YES 

AUDIT CON \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

READ 

DELETE ACCESS:

WRITE ACCESS:

SOURCE:

DESCRIPTION... TECHNICAL DESCRIPTION...

IS THIS FIELD MULTIPLE... NO

MANDATORY: NO

HELP-PROMPT: Answer must be 5-40 characters in length.

XECUTABLE HELP:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

OK TO DELETE 'DEMOGRAPHIC PROD LISTENER' FIELDS IN THE EXISTING ENTRIES? Yes//Y (Yes)

Select FIELD: 10 RX LAB TEST LISTENER

Field \#10 in File \#603.03

FIELD LABEL: DATA TYPE...FREE TEXT



 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

 ARE YOU SURE YOU WANT TO DELETE THE ENTIRE FIELD: YES 

AUDIT CON \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

READ 

DELETE ACCESS:

WRITE ACCESS:

SOURCE:

DESCRIPTION... TECHNICAL DESCRIPTION...

IS THIS FIELD MULTIPLE... NO

MANDATORY: NO

HELP-PROMPT: Answer must be 5-40 characters in length.

XECUTABLE HELP:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

OK TO DELETE 'RX LAB TEST LISTENER' FIELDS IN THE EXISTING ENTRIES? Yes//Y (Yes)

Select FIELD: 11 DEMOGRAPHIC TEST LISTENER

Field \#11 in File \#603.03

FIELD LABEL: DATA TYPE...FREE TEXT



 \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

 ARE YOU SURE YOU WANT TO DELETE THE ENTIRE FIELD: YES 

AUDIT CON \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* 

READ 

DELETE ACCESS:

WRITE ACCESS:

SOURCE:

DESCRIPTION... TECHNICAL DESCRIPTION...

IS THIS FIELD MULTIPLE... NO

MANDATORY: NO

HELP-PROMPT: Answer must be 5-40 characters in length.

XECUTABLE HELP:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

OK TO DELETE ' DEMOGRAPHIC TEST LISTENER' FIELDS IN THE EXISTING ENTRIES? Yes//Y (Yes)