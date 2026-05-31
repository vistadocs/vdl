---
title: DVBA*2.7*254 CAPRI Deployment, Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: null
app_code: CAPRI
app_name: Compensation and Pension Record Interchange
section: FIN
app_status: active
pkg_ns: DVBA
patch_ver: 2.7
patch_id: DVBA*2.7*254
group_key: CAPRI:DVBA:2.7
file_numbers: []
security_keys: []
menu_options: 0
description: All references to VistA patch and client application (GUI) have been updated to reflect current
audience: System administrators, deployment engineers
keywords: []
page_count: 0
word_count: 4941
section_count: 17
table_count: 3
figure_count: 0
appendix_count: 1
has_toc: false
is_stub: false
pub_date: August 2025
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/DVBA_27_254_DIBRG.docx
pdf_url: https://www.va.gov/vdl/documents/Financial_Admin/CAPRI/DVBA_27_254_DIBRG.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=133
audit_applied: '2026-05-31'
master_source: DVBA*2.7*254 CAPRI Deployment, Installation, Back-out, and Rollback Guide
master_pub_date: August 2025
consolidated_from: 3 versions
prior_versions:
- DVBA*2.7*251 CAPRI Deployment, Installation, Back-out, and Rollback Guide
- DVBA*2.7*255 CAPRI Deployment, Installation, Back-out, and Rollback Guide
consolidated_title: capri deployment, installation, back-out, and rollback guide
---

![](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table style="width:100%;">
<caption><p>Table 1 Deployment Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 55%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/2025</td>
<td>2.12</td>
<td><p>Updated for DVBA*2.7*254 release</p>
<ul>
<li><blockquote>
<p>All references to VistA patch and client application (GUI) have been updated to reflect current release.</p>
</blockquote></li>
<li><blockquote>
<p><a href="#deployment">Section 3</a> Deployment –</p>
</blockquote>
<ul>
<li><blockquote>
<p><a href="#timeline">Section 3.1</a> Timeline Table 2-CAPRI Patch DVBA*2.7*254 Deployment</p>
</blockquote></li>
<li><blockquote>
<p>Suggested Deployment Schedule</p>
</blockquote></li>
</ul></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>06/2025</td>
<td>2.11</td>
<td><p>Updated for DVBA*2.7*253 release.</p>
<ul>
<li><p>All references to VistA patch and client application (GUI) have been updated to reflect current release.</p></li>
<li><p>Table of Contents</p></li>
<li><p><a href="#introduction">Section 1</a> Introduction</p>
<ul>
<li><p><a href="#dependencies">Section 1.2</a> Dependencies - Required builds and prerequisites.</p></li>
</ul></li>
<li><p><a href="#roles-and-responsibilities">Section 2</a> Roles and Responsibility- Updated <u>Table 1</u> Deployment Roles and Responsibilities</p></li>
<li><p><a href="#deployment">Section 3</a> Deployment –</p>
<ul>
<li><p><a href="#timeline">Section 3.1</a> Timeline</p></li>
</ul></li>
</ul>
<blockquote>
<p>Table 2<u>-</u> CAPRI Patch DVBA*2.7*253 Deployment</p>
</blockquote>
<ul>
<li><p>Suggested Deployment Schedule</p></li>
</ul>
<ul>
<li><p><a href="#site-readiness-assessment">Section 3.2</a>- Site Readiness Assessment</p>
<ul>
<li><p>Section <a href="#site-information-locations-deployment-recipients">3.2.2</a>– Site Information: Table 2 Test Sites</p></li>
<li><p>Section <a href="#software">3.2.5</a>-Software</p></li>
</ul></li>
</ul>
<ul>
<li><p>Removed Section 4.10.2 CAPRI Graphical User Interface (GUI) Verification Procedure as obsolete</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>1/2025</td>
<td>2.10</td>
<td><p>Updated for DVBA*2.7*252 release.</p>
<ul>
<li><p><a href="#introduction">Section 1,</a> <a href="#roles-and-responsibilities">Section 2</a>, <a href="#deployment">Section 3</a>, <a href="#installation">Section 4</a> including sub sections - All references to VistA patch and client application (GUI) have been updated to reflect current release.</p></li>
<li><p><a href="#dependencies">Section 1.2</a> Dependencies - Updated required builds.</p></li>
<li><p><a href="#roles-and-responsibilities">Section 2</a> Roles and Responsibilities - VistA patch updated to reflect current release.</p></li>
<li><p><a href="#deployment">Section 3</a> Deployment – Updated timeline</p></li>
<li><p><a href="#timeline">Section 3.1</a> Timeline - Revised Installment and Deployment Timeline information</p></li>
<li><p><a href="#software">Section 3.2.5</a> Software – Updated associated patches that must be installed before DVBA*2.7*252</p></li>
<li><p><a href="#download-and-extract-files">Section 4.3</a> Download and Extract Files – Updated Required Distribution Files to reflect patch DVBA*2.7*252</p></li>
<li><p>Section 4.10.2 CAPRI Graphical User Interface (GUI) Verification Procedure – updated Figure 2-11 CAPRI Splach Screen and Figure 2-13 Error! Reference source not found. CAPRI About Splash Screen</p></li>
</ul>
<p>Corrected Figure numbering.</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>11/2023</td>
<td>2.09</td>
<td><p>Updated for DVBA*2.7*251 release.</p>
<ul>
<li><p>All references to VistA patch and client application (GUI) have been updated to reflect current release.</p></li>
<li><p>Section 1.2 Dependencies - Updated required builds.</p></li>
<li><p>Section 3 Deployment – Updated timeline</p></li>
<li><p>Section 3.1 Timeline - Revised Installment and Deployment Timeline information</p></li>
<li><p>Section 3.2.5 Software – Updated associated patches that must be installed before DVBA*2.7*251</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>11/2023</td>
<td>2.08</td>
<td><p>Updated for DVBA*2.7*250 release.</p>
<ul>
<li><p>All references to VistA patch and client application (GUI) have been updated to reflect current release.</p></li>
<li><p>Section 1.2 Dependencies - Updated required builds.</p></li>
<li><p>Section 3 Deployment – Updated timeline</p></li>
<li><p>Section 3.1 Timeline - Revised Installment and Deployment Timeline information</p></li>
<li><p>Section 3.2.5 Software – Updated associated patches that must be installed before DVBA*2.7*250</p></li>
<li><p>Section 4.10.2 CAPRI Graphical User Interface (GUI) Verification Procedure – updated Figure 10 and Figure 12.</p></li>
</ul>
<p>Global - Revised date on title page/footers to reflect current release month and year.</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>02/2023</td>
<td>2.07</td>
<td>Updated for DVBA*2.7*243 release.</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>08/2022</td>
<td>2.06</td>
<td>Updated for DVBA*2.7*242 release.</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>08/2022</td>
<td>2.05</td>
<td><p>Updated for DVBA*2.7*238 release information.</p>
<p>Removal of Windows 7/XP references in Section 4.8</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>02/2022</td>
<td>2.04</td>
<td><p>Updated for DVBA*2.7*240 release information.</p>
<p>Removed section for CAPRI News and SharePoint Initialization News Server Share</p>
<p>SharePoint Initialization previously 4.10.1.</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>10/2021</td>
<td>2.03</td>
<td>Updated for DVBA*2.7*237 release. Adding Re-Route functionality. Adding section 4.10.1 for CAPRI News and SharePoint Initialization</td>
<td>Liberty IT Solutions, a Booz Allen company</td>
</tr>
<tr class="odd">
<td>06/2021</td>
<td>2.02</td>
<td>Updated for DVBA*2.7*226 release.</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>12/2020</td>
<td>2.01</td>
<td><p>Updated for DVBA*2.7*224 release. All references have been updated to reflect current release.</p>
<p>Section 3 – New Timeline</p></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>10/12/20</td>
<td>2.0</td>
<td>Updated sections from beginning through 4.3 for patch 223. Removed sections no longer needed for Windows 7 font size and Microsoft Imaging for Windows 7.</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>03/2020</td>
<td>1.15</td>
<td>Updated for patch 220</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>03/2020</td>
<td>1.14</td>
<td>Updated for patch 212</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>09/2019</td>
<td>1.13</td>
<td>Updated versioning control to 212.7</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>09/2019</td>
<td>1.12</td>
<td><p>Section 3. Added Note: 'VistA Patch DVBA*2.7*223 must be installed in all production VistA systems before CAPRI GUI v2.7.223.6 is installed.'</p>
<p>Section 3.1 Timeline: Revised Installment and Deployment Timeline information. Added 'Suggested Deployment Schedule' to text.</p>
<p>Section 4.10.4 CAPRI Graphical User Interface (GUI) Verification Procedure:</p>
<ul>
<li><p>Figure 11: New CAPRI Splash screen</p></li>
<li><p>Figure 13: New CAPRI About Splash screen</p></li>
</ul>
<p>Section 4.11 Back-Out: Updated Back-Out Procedure</p>
<p>Global: Revised date on Title page and in footers to September 2019</p></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>03/2019</td>
<td>1.11</td>
<td>Page 20, Section 12.1, Added CAPRI Remote Procedure Calls Logger section</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>02/2019</td>
<td>1.10</td>
<td><p>Page 34, under Appendix A, added a new Remote Procedure Call: DVBA CAPRI GET EDIPI</p>
<p>Page 10, under 6.1 CAPRI GUI Client Software, revised 193.11 to 209</p></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>05/2018</td>
<td>1.9</td>
<td><p>Updated sections 2.2.2.1. and 2.2.3. The JLV tab replaced the VistAWeb tab in GUI version DVBA*2.7*193.12, so references to VistAWeb were removed.</p>
<p>Updated section 2.2.1.1. Replaced reference to VistAWeb with JLV.</p>
<p>Replace Remedy with ServiceNow</p>
<p>DoD Tab has been disabled, and all references to DoD have been removed from the document.</p>
<p>Removed DataFlow Diagram from Section 3.</p>
<p>Added description for Joint Legacy Viewer (JLV) function (Section 2.2.3).</p>
<p>Section 8.2, updated last paragraph with revisions from 1<sup>st</sup> Review.</p>
<p>Updated formatting for Appendix A.</p>
<p>Updated Dates to May on title page and in footers.</p></td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>4/2018</td>
<td>1.8</td>
<td>URL to include descriptions for all values. Updated Appendix A, RPC parameter DVBAB GET</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>9/2015</td>
<td>1.7</td>
<td>Updated Appendix A</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>3/2015</td>
<td>1.6</td>
<td>Updated various sections based on stakeholder feedback.</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>2/2015</td>
<td>1.5</td>
<td>Updated Appendix A</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>12/2014</td>
<td>1.4</td>
<td>Updated section 7.8 with a new screen shot</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>9/2014</td>
<td>1.3</td>
<td>Updated section 15.2 to only contain VDL link to CAPRI</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>4/2014</td>
<td>1.2</td>
<td>Updated CAPRI Distribution File listing</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="even">
<td>3/2013</td>
<td>1.1</td>
<td>Updated sections 5 and 7.4 with changing the CLAIMS server FQDN from CLAIMS.FORUM.VA.GOV "to" CLAIMS.MED.VA.GOV on 03/25/2013</td>
<td>Liberty IT Solutions</td>
</tr>
<tr class="odd">
<td>720/12</td>
<td>1.0</td>
<td>Initial Publication</td>
<td>Liberty IT Solutions</td>
</tr>
</tbody>
</table>

Table 1 Deployment Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect the particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to initial operating capability (IOC), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.
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
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Additional Installation Files](#additional-installation-files)
    - [VACAPRIVVA.dll](#vacaprivvadll)
    - [LIBEAY32.DLL & SSLEAY32.DLL](#libeay32dll-ssleay32dll)
    - [QPDF.EXE, QPDF13.DLL, LIBGCCSDW2-1.DLL & LIBSTDC++-6.DLL](#qpdfexe-qpdf13dll-libgccsdw2-1dll-libstdc-6dll)
    - [CAPRIHelp.chm](#caprihelpchm)
    - [CAPRI.map](#caprimap)
    - [CAPRISession.rdox](#caprisessionrdox)
    - [CAPRITerminalEmulators.ini](#capriterminalemulatorsini)
    - [sshconfig](#sshconfig)
  - [CAPRI Configuration for Windows and Non-standard Reflection Installations](#capri-configuration-for-windows-and-non-standard-reflection-installations)
    - [Windows Installation](#windows-installation)
    - [Non-standard Reflection Installations](#non-standard-reflection-installations)
  - [Micro Focus Reflection](#micro-focus-reflection)
  - [CAPRI GUI Launch](#capri-gui-launch)
    - [Shared Network Drive or CAPRI access via CPRS Installations](#shared-network-drive-or-capri-access-via-cprs-installations)
  - [Back Out](#back-out)
This document describes how to deploy and install the Compensation and Pension Record Interchange (CAPRI), as well as how to back-out the product and rollback to a previous version or data set. This will include installation of CAPRI Patch DVBA\*2.7\*254. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed COTS product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom CAPRI will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CAPRI is a system that gives Veterans Benefits Administration (VBA) claims processors and others access to compensation and pension examinations, clinical documents, and reports vital to process benefits claims. CAPRI consists of VistA patch DVBA\*2.7\*254 and a client application (GUI). Installation requires the following prerequisites:

- VistA Patches (for VHA only)

> The following is a list of REQUIRED builds for this KIDS distribution (DVBA\*2.7\*254). KIDS will not allow the installation of this patch without their prior installation.

> Required Builds:

> DVBA\*2.7\*250 and DVBA\*2.7\*252

- Approved release from the VOCCB, HPS, and OIT Implementation Manager.
- Test site sign-off from VBA Beta Sites and VHA IOC Sites.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no identified constraints to the installation of this VistA component of CAPRI.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the teams who perform the steps described in this deployment plan.

Deployment and installation activities are performed by representatives from the teams listed in the following table. This phase begins after the solution design (including deployment topology) is complete. Design activities are not included in this phase.

| Team                                   | Phase / Role | Tasks                                                                                                     | Project Phase (See Schedule) |
|--------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------|----------------------------------|
| CAPRI Development Team                     | Deployment       | Plan and schedule deployment                                                                                  | Deployment                       |
| CAPRI Development Team                     | Deployment       | Develop O&M Plan                                                                                              | Deployment                       |
| VOCCB, HPS, and OIT Implementation Manager | Testing          | Test and approve for release readiness                                                                        | Testing                          |
| DMA and IOC                                | Testing          | DMA and IOC Tests Patch DVBA\*2.7\*254                                                                        | Testing                          |
| VBA/VHA Business Offices                   | Deployment       | Develop communications plan and key messages well in advance                                                  | Deployment                       |
| Health Product Support                     | Testing          | Review Patch DVBA\*2.7\*254                                                                                   | Testing                          |
| Health Product Support                     | Deployment       | Release Patch DVBA\*2.7\*254 nationally                                                                       | Deployment                       |
| Regional PM/FIS/OPP PM                     | Installation     | Ensure authority to operate and that certification and authorization (C&A)/security documentation is in place | Installation                     |
| Infrastructure Operations                  | Installation     | Install the patch as scheduled                                                                                | Installation                     |

Table 2 CAPRI Patch DVBA\*2.7\*254 Deployment Timeline

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** VistA Patch DVBA\*2.7\*254 must be installed in all production VistA systems before CAPRI GUI DVBA\*2.7\*254.24 is installed.

Deployment and installation of the Compensation and Pension Record Interchange (CAPRI) is planned as follows:

1.  National Release: 08/14/25 VistA Patch DVBA\*2.7\*254 will be deployed to all 132 instances of VistA within a 3-day compliance period followed by a 9-day deployment of CAPRI GUI DVBA\*2.7\*254.24"

The release of the patch will be performed by Health Product Support (HPS) members, supported by the CAPRI project team, along with representatives from peer organizations. The installation will be performed by Local, VISN, or Regional IT support personnel.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation and deployment runs for 15 days, which does not include the warranty period that monitors for defects. The warranty period is 90 calendar days and begins once the National Implementation is completed. The approximate timeline for this effort is shown in the table below:

| Phase                                                            | Activity            | Start | Finish |
|----------------------------------------------------------------------|-------------------------|-----------|------------|
| General Release                                                      | IOC Testing             | 08/04/25  | 08/08/25   |
|                                                                      | National Implementation | 08/14/25  | 09/04/25   |
|                                                                      | Warranty Period         | 09/04/25  | 12/03/25   |
| (Dates shown are subject to change due to unforeseen circumstances.) |                         |           |            |

Table 3 Test Sites

SuggestedDeployment Schedule:

- Days 1-3 (Thursday, August 14 – Monday, August 18): CAPRI VistA Patch DVBA\*2.7\*254 will be deployed to all VistA production instances. Users will not see or experience any changes. 
- Day 4-6 CT Field Testing (Tuesday, August 19 – Thursday, August 21): Software deployment to 10% of workstations 
- Days 7-15 (Friday, August 22 – Thursday, September 4): CAPRI GUI DVBA\*2.7\*254.24 will be deployed to all applicable endpoint devices to include client desktop workstations, other application shares, and Citrix Virtual Desktops. 
  - (Sunday, August 24): CAPRI GUI DVBA\*2.7\*254.24 deployment to all VistA Application Consolidated Servers (VACS) 

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This deployment will enhance the capabilities of the existing CAPRI system. This section discusses the locations that will receive the upgrades to the CAPRI system.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA component of the new version needs to be installed into all instances of VistA. All facilities will use their established local procedures to install the new software.

Additionally, a nationally released patch updates the files in VistA and only affects the Users with the appropriate CAPRI menu options in VistA.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new version of CAPRI's VistA patch (DVBA\*2.7\*254) will be installed across the entire VA Enterprise for all CAPRI Users to all instances of VistA. All facilities in Regions 1-5 will use established location procedures to install the new software.

The following test sites are participating in the testing of the DVBA\*2.7\*254 server software:

- Test Sites:

<table>
<caption><p>Table 4 Site Preparation Resources</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Type</strong></th>
<th><strong>Site</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VHA</strong></td>
<td><p><strong>Tampa VAMC</strong></p>
<p><strong>Cheyenne VAMC</strong></p></td>
</tr>
</tbody>
</table>

Table 4 Site Preparation Resources

> **NOTE:** The test sites used may change based on a site's willingness to participate, workload, and other factors. Sites listed in boldface type are expected to be primary ("Alpha") testers. Other sites listed are secondary ("Beta") testers who will help us uncover any hidden defects before we release nationally.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

| Site/Other | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner                       |
|----------------|---------------------------|---------------------------------------------|-------------------|---------------------------------|
| All            | Create backups            | N/A                                         | N/A               | Local facility, VISN, or Region |

Site PreparationResources

This section describes the resources needed for deployment and installation.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no new hardware requirements for this software update.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Associated patches that must be installed BEFORE \`DVBA\*2.7\*254:

- DVBA\*2.7\*250 and DVBA\*2.7\*252

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the communications that need to occur to upgrade CAPRI:

1.  The CAPRI Development Team will provide the installation files to VHA and other users (see Section 4). We will work with VHA to proactively notify users to the maximum extent possible, but it is recognized and understood that we may not reach everyone prior to installation of the VistA patch.
2.  The CAPRI Deployment Team will conduct weekly status conference calls and ad-hoc calls with test sites and stakeholders to provide status and answer questions.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to install CAPRI.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the patch will be introducing new files, updating routines, parameters, remote procedure calls, and options.

1.  Choose the PackMan message containing this patch.
2.  Choose the INSTALL/CHECK MESSAGE PackMan option.
3.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the patch DVBA\*2.7\*254:
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patches routines, DDs, and templates).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  From the Installation Menu, select the Install Package(s) option and choose the patch to install:
1.  When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO/NO Select NO
2.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO/NO Select NO
3.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO/NO Select NO
5.  If prompted 'Delay Install (Minutes): (0 – 60): 0//' respond 0.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We do not anticipate difficulties with version incompatibility. Nevertheless, we recommend deploying the new VistA patch DVBA\*2.7\*254 into all 132 VistA production systems.

All sites should make sure that their test environments mirror the state of their production environments. This is important because it helps identify deficiencies (such as outdated or missing patches) when the new software is installed into the test environment rather than into the production environment.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation can be found on the VA Software Documentation Library at:

<https://www.va.gov/vdl/>.

<u>Optional Distribution Files that Contain Important User Info</u>

> DVBA_DIBRG.PDF Deployment,Installation,Back-Out and Rollback Guide BINARY

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch installers will follow their local procedures to install the software in accordance with the Installation Guide.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of VistA Patch DVBA\*2.7\*254 requires VistA programmer access.

Some sites utilize shortcut folders on users' desktops with icons that point to a CAPRI installation on a server.

## Additional Installation Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the executable file, there are other files included with the CAPRI installation zip. The general purpose of these files and where they need to be located are as follows:

### VACAPRIVVA.dll

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VACAPRIVVA.dll file is a dynamic link library that provides the web services client interface for the Virtual VA web service, which was added in patch DVBA\*2.7\*181. Important: CAPRI will not function without this file.

- VACAPRIVVA.dll is required for CAPRI to function.
- VACAPRIVVA.dll must be located in the same directory as the CAPRI executable (CAPRI.exe).

The following dialog box displays when CAPRI cannot find the VACAPRIVVA.dll file.

![](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/002.png)Figure 1. Missing File Alert

### LIBEAY32.DLL & SSLEAY32.DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Libeay32.dll and Ssleay32.dll are dynamic link libraries that provide the web services client interface for the VLER/DAS web service, which was added in patch DVBA\*2.7\*187. Important: CAPRI requires these files to transfer exam data to VLER/DAS.

- Libeay32.dll and Ssleay32.dll are required for exam data transfer to VLER/DAS.
- Libeay32.dll and Ssleay32.dll must be located in the same directory as the CAPRI executable (CAPRI.exe).

### QPDF.EXE, QPDF13.DLL, LIBGCC_S_DW2-1.DLL & LIBSTDC++-6.DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

QPDF.exe, QPDF13.DLL, LIBGCC_S_DW2-1.DLL & LIBSTDC++-6.DLL are files that support PDF Compression and Linearization. PDF Compression reduces the file size of the PDF Exam Results included in transmissions between CAPRI and VLER/DAS. Smaller file sizes reduce transmission times.

- QPDF.exe, QPDF13.dll, Libgcc_s_dw2-1.dll and Libstdc++-6.dll are required for PDF compression when sending exam data to VLER/DAS.
- QPDF.exe, QPDF13.dll, Libgcc_s_dw2-1.dll and Libstdc++-6.dll must be located in the same directory as the CAPRI executable (CAPRI.exe).

### CAPRI_Help.chm

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CAPRI_Help.chm file contains the on-line help functionality.

CAPRI_Help.chm is not required for CAPRI to function, but its presence is recommended

CAPRI_Help.chm should be located in the same directory as the CAPRI executable (CAPRI.exe)

If CAPRI is setup to run from a disk drive that is not local to the workstation, CAPRI should be given write permissions to the "TEMP" folder of the workstation. If the TEMP folder is not writable for any reason, the on-line help functionality may not work properly.

### CAPRI.map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CAPRI.map file contains a list of error addresses and source code line numbers that CAPRI utilizes to provide more detailed information to the development team when an error occurs in CAPRI.

CAPRI.map is not required for CAPRI to function, but its presence is recommended

CAPRI.map should be located in the same directory as the CAPRI executable (CAPRI.exe)

### CAPRISession.rdox

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- CAPRISession.rdox is a Micro Focus Reflection configuration file. It configures Reflection to terminate when a terminal session disconnects.
- CAPRISession.rdox is used for the new Micro Focus Reflection application
- CAPRISession.rdox is not required for CAPRI to function, but its presence is recommended
- CAPRISession.rdox should be located in the same directory as the CAPRI executable (CAPRI.exe)

### CAPRITerminalEmulators.ini

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- CAPRITerminalEmulators.ini is a Micro Focus Reflection configuration file. It tells CAPRI where the Micro Focus Reflections application is installed.
- CAPRITerminalEmulators.ini should be located in the same directory as the CAPRI executable (CAPRI.exe)

### ssh_config

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ssh_config file provides the parameters used by Micro Focus Reflection Secure Shell to configure PC-to-host security options. CAPRI does not require this file for most functions, but it is required when establishing Reflection Secure Shell terminal sessions using the "Vista" button.

The directory location of the ssh_config file:

> C:\Program Files (x86)\Micro-Focus\Reflection

> **NOTE:** The target folder for ssh_config is typically hidden on most systems.

To show hidden files and folders on Windows, perform the following steps:

1.  In the search box on the taskbar, type "hidden files"
2.  Select "Show hidden files" from the results.

![Figure 2. Show Hidden Files](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/003.png)

*Figure 2. Show Hidden Files*

![](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/004.png)

## CAPRI Configuration for Windows and Non-standard Reflection Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to launching Reflection, CAPRI searches the directory path that contains the CAPRI executable (CAPRI.exe) for an optional plain text configuration file named "CapriTerminalEmulators.ini." The purpose of the configuration file is to specify an alternate path that contains the Micro-Focus Reflection executable (Attachmate.Emulation.Frame.exe). If CAPRI does not detect the configuration file, CAPRI assumes that the Reflection executable exists in the default Windows Reflection installation path: "C:\Program Files (x86)\Micro-Focus\Reflection."

### Windows Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The example "CapriTerminalEmulators.ini" configuration file provided with patch DVBA\*2.7\*180 is configured to provide support for the default installation path of Micro Focus Reflection on a Windows workstation. Place the configuration file in the same directory that contains the CAPRI executable.

Alternatively, use the following procedure to create the configuration file:

Create the configuration file named "CapriTerminalEmulators.ini" using a plain text editor, such as Notepad. Populate the configuration file with the following three lines:

> \[Config\]

> ApplicationLegacy=C:\Program Files (x86)\Attachmate\Reflection\R2win.exe

> Application="C:\Program Files (x86)\Micro Focus\Reflection\Attachmate.Emulation.Frame.exe"

![Figure 3. Config File for Standard Reflection Installation](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/005.png)

*Figure 3. Config File for Standard Reflection Installation*

> **NOTE:** Save the file and place it in the same directory that contains the CAPRI executable.

### Non-standard Reflection Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If Reflection is installed in an alternate location, CAPRI can be configured to accommodate this. In order to do this, one should create a file named "CapriTerminalEmulators.ini" in the directory that contains the "CAPRI.exe" file. In this file, one should specify the location of the "Attachment.Emulation.Frame.exe." For example, in order to specify a Reflection installation located in "C:\My Files\Attachmate\Reflection," the CAPRITerminalEmulator.ini should contain the following lines:

> \[Config\]

> ApplicationLegacy=C:\My Files\Attachmate\Reflection\R2win.exe

> Application="C:\My Files\Attachmate\Reflection\Attachmate.Emulation.Frame.exe"

![Figure 4. Config File for Non-Standard Reflection Installation](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/006.png)

*Figure 4. Config File for Non-Standard Reflection Installation*

## Micro Focus Reflection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CAPRISession.rdox is the configuration file for the Reflection application.

> **NOTE:** If your site uses a non-standard Reflection installation, the CAPRITerminalEmulators.ini file will need to be updated to reflect the value currently used at your site.

![Figure 5. New CapriTerminalEmulators.ini file format](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/007.png)

*Figure 5. New CapriTerminalEmulators.ini file format*

\[Config\]

> ApplicationLegacy=C:\Program Files (x86)\Attachmate\Reflection\R2win.exe

> Application="C:\Program Files (x86)\Micro Focus\Reflection\Attachmate.Emulation.Frame.exe"

If your site has a non-standard Reflection location, the ApplicationLegacy line will need to be updated to reflect the value currently used at your site. In the example below*, C:\My Files\Attachmate\Reflection* was the non-standard site. That value will need to be updated on the ApplicationLegacy line – shown below.

![Figure 6. New CapriTerminalEmulators.ini with existing non-standard Reflection location](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/008.png)

*Figure 6. New CapriTerminalEmulators.ini with existing non-standard Reflection location*

\[Config\]

> ApplicationLegacy=C:\My Files\Attachmate\Reflection\R2win.exe

> Application="C:\Program Files (x86)\Micro Focus\Reflection\Attachmate.Emulation.Frame.exe"

## CAPRI GUI Launch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Shared Network Drive or CAPRI access via CPRS Installations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site installs CAPRI on a Shared Network Drive and users access a "shortcut" to launch CAPRI or if your users access CAPRI via CPRS, the following MUST be performed to allow users to view PDF files from DAS. Users will receive the following error if this is not done.

![Figure 7. CAPRI Shortcut Launch Error](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/009.png)

*Figure 7. CAPRI Shortcut Launch Error*

If the "Start In" folder for CAPRI shortcut at your site is a read-only only folder, it should be changed to a writable folder. This is the folder where documents from VLER DAS are stored temporarily for users to view documents (ex: PDF).

Our recommendation is to use %TEMP% as the default starting directory. This can be set in the shortcut that is used to launch CAPRI.

- Right-click on the (desktop) CAPRI shortcut, select Properties.
- On the Shortcut tab, in the Start in field, enter %TEMP%.
- Click OK.
- Now, when launching CAPRI, it will be able to write temporary files such as Word documents or PDFs to the temporary directory, and CAPRI will be able to display those files to the user.

> **NOTE:** This temp directory change only fixes the "access denied" problem when CAPRI is launched directly from a shortcut.

![Figure 8. Example of Starting CAPRI from a TEMP Directory Location](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/010.png)

*Figure 8. Example of Starting CAPRI from a TEMP Directory Location*

![Figure 9. Example of CAPRI accessed via CPRS](dvba-2-7-254-capri-deployment-installation-back-out-and-rollback-guide/011.png)

*Figure 9. Example of CAPRI accessed via CPRS*

Benefits:

1.  Each user is guaranteed by Windows to have a unique writable folder.
2.  It is a known environment variable and also guaranteed to exist in any environment.
3.  Due to VA GPO Policy, this folder gets cleared on logon / logoff, hence no disk space impact is caused.

## Back Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back out Procedures are only needed if there are major problems (examples include the KIDS notice of incompletion or hard errors) resulting from the installation of this patch. Log a ServiceNow helpdesk ticket so the development team can assist in this process.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: DVBA*2.7*251 CAPRI Deployment, Installation, Back-out, and Rollback Guide

## Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out Procedures are only needed if there are major problems (examples include the KIDS notice of incompletion or hard errors) resulting from the installation of this patch. Log a ServiceNow helpdesk ticket so the development team can assist in this process.
