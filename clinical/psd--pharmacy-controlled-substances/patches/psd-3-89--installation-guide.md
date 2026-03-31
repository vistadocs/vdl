---
title: PSD*3*89 Controlled Substance DIRB
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Controlled Substance DIRB
app_code: PSD
app_name: "Pharmacy: Controlled Substances"
section: CLI
app_status: active
pkg_ns: PSD
patch_ver: 3
patch_id: PSD*3*89
group_key: "PSD:PSD:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the PRE Inbound eRx application will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan,
audience: 
keywords: 
  - span
  - weblogic
  - table
  - domain
  - class
  - contents
  - dzdo
  - install
  - deployment
  - anchor
page_count: 0
word_count: 19547
section_count: 34
table_count: 16
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Controlled_Substances/psd_3_p89_dirb.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Controlled_Substances/psd_3_p89_dirb.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=86"
---

---
title: |
  <span id="_top" class="anchor"></span>Pharmacy Reengineering (PRE) Inbound  
  ePrescribing Version 5.0

  Deployment, Installation, Rollback, and Back-Out Guide
---

PSO\*7.0\*617

PSD\*3\*89

![](psd-3-89-controlled-substance-dirb/001.png)

December 2021

Office of Information and Technology (OI&T)

Revision History

<table>
<caption><p><span id="_Toc525722924" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/27/2021</td>
<td>5.0</td>
<td>Updates to document to include Hub and VistA changes for Inbound eRx Controlled Substance (CS) prescriptions</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>04/14/2021</td>
<td>4.1</td>
<td>Update for consistency during SQA1 Install</td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>01/28/2021</td>
<td>4.0</td>
<td>Updates for changes with 4.0.5.012 reference: <a href="#Timeline">pg4 3.1</a>, <a href="#ApplicationArchitecture">pg5 3.2.1</a>, <a href="#SiteInfo">pg7 3.2.3</a>, <a href="#PreReq">pg9 4.1</a>, <a href="#PlatformInstall">pg19 4.2</a>, <a href="#InstallProcedure">pg39 4.8</a></td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>06/06/2019</td>
<td>2.6</td>
<td><p>Updates for changes with 3.1.0.005 reference: pg: 117, 127, and 132</p>
<p>Updated Title page to month of June</p></td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>05/07/2019</td>
<td>2.5</td>
<td><p>Updates for changes with 3.1.0.004 reference: pg 127, 132, 145, 146, and 150</p>
<p>Updated Title page to month of March</p></td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>03/11/2019</td>
<td>2.4</td>
<td><p>Updates for changes with 3.1.0.003 reference: pg 127, 132, 145, 146, and 150</p>
<p>Updated Title page to month of February</p></td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>10/29/2018</td>
<td>2.3</td>
<td>Update Title page to month of December</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>10/24/2018</td>
<td>2.2</td>
<td>Updates for changes with 3.0.5.008 reference: pg 132</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>09/21/2018</td>
<td>2.1</td>
<td><p>Updated to address VIP RA Comments</p>
<p>Sections: <a href="#back-out-of-database">5.6.1</a>, <a href="#p146_508">5.7.1</a>, <a href="#rollback-vista-patch">6.5.2</a>, <a href="#rollback-verification-procedure">6.5.2.1</a></p></td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>09/19/2018</td>
<td>2.0</td>
<td>Updates for changes with 3.0.5.005.</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>07/26/2017</td>
<td>0.93</td>
<td>Updates for changes with 2.0.4.057.</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>07/20/2017</td>
<td>0.92</td>
<td>Updates for changes with 2.0.4.057.</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>06/27/2017</td>
<td>0.91</td>
<td>Updates for changes with 2.0.4.054.</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>05/22/2017</td>
<td>0.8</td>
<td>Updates for changes with 2.0.4.048.</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>05/10/2017</td>
<td>0.7</td>
<td>Updates for changes with 2.0.3.047.</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>04/25/2017</td>
<td>0.6</td>
<td>Updates with corrected information for Staging, PreProd and Production.</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>04/12/2017</td>
<td>0.5</td>
<td>Updates with corrected information for Staging, PreProd and Production.</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>02/15/2017</td>
<td>0.4</td>
<td>Updates with corrected information for Staging, PreProd and Production. New sections for SSOi.</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>02/07/2017</td>
<td>0.3</td>
<td>Multiple updates with new steps introduced throughout Build 1, cleanup for Staging, PreProd and Production.</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>11/10/2016</td>
<td>0.2</td>
<td>Sprint Update – Added draft steps for rolling back Weblogic; added the VistA Patch #; added a placeholder for backing out the database.</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>10/27/2016</td>
<td>0.1</td>
<td>Initial Draft (Template Version 2.2 March 2016)</td>
<td>Technatomy</td>
</tr>
</tbody>
</table>

<span id="_Toc525722924" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

Table of Figures

List of Tables

1.  Introduction

This document describes how to deploy and install the various components of the software for the Pharmacy Reengineering (PRE) Inbound ePrescribing (eRx) project, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial Off-the-Shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

Veterans Health Administration (VHA), Patient Care Services (PCS) and Pharmacy Benefits Management (PBM) has requested a new capability as part of the PRE program to receive inbound electronic prescriptions (e-prescriptions or eRxs) from an external provider (e.g., a doctor not associated with the Department of Veterans Affairs \[VA\], medical staff at a Department of Defense \[DoD\] military treatment facility, etc.). They also seek to have the ability to transfer prescriptions electronically between pharmacies, both VA to VA, as well as VA to non-VA (ideally). Once received, these prescriptions will then be fed into the existing Veterans Health Information Systems and Technology Architecture (VistA) Outpatient Pharmacy (OP) for processing and dispensing.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the PRE Inbound eRx application will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 2 depicts the Inbound eR<sub>x</sub> application and the external systems that it interacts with, including the following: Change Healthcare, Master Veteran Index (MVI), Eligibility & Enrollment (E&E), Health Data Repository (HDR), and VistA OP.

<span id="_Toc439226961" class="anchor"></span>Figure 1: Inbound eR<sub>x</sub> Application Context Diagram

![](psd-3-89-controlled-substance-dirb/002.png)

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Design constraints that pertain to the PRE Inbound eRx implementation include the following:

- Existing interfaces will be implemented with the least possible change in order to support existing client system implementations. However, it is recognized that in some circumstances, a change to the interface may be necessary in order to support PRE Inbound eRx requirements or to accommodate technology or frameworks used for PRE Inbound eRx development. One key change is the need for service consumers to maintain the session state and provide this to PRE Inbound eRx on each call. This change is necessary to provide stateless services, as required by the VA Service-Oriented Architecture (SOA).
- The Java language and Java Enterprise Edition (JEE) platform will be used to develop the PRE Inbound eRx.
- Security policies and mechanisms for SOA middleware are currently being developed and updated. The timeframes for the production ready versions may not coincide with the PRE Inbound eRx effort. This includes solutions to the VistA anonymous login and authorization/authentication for the middleware running on non-VistA platforms as part of the enterprise SOA architecture.
- The application user interfaces (UI) must follow enterprise common UI templates and style guidelines.
- Application user interfaces must comply with Section 508.
- The application must comply with VA Enterprise Architecture published data standards (HL7, National Council for Prescription Drug Programs \[NCPDP\]).
- Inbound eRx must identify and leverage authoritative information sources for data retrieval and manipulation.
- The application must operate optimally using information from the authoritative source or receive permission for caching data locally.
- The team must configure system/and server platforms used by the application using standard system images published in the current VA Release Architecture.
- The team must publish relational and object oriented databases utilized by the solution in the current VA Release Architecture.
- The team must base application production capacity requirements on workload analysis, simulated workload benchmark tests, or application performance models.
- The team must base application storage capacity requirements on detailed capacity analysis and/or models.
- The team must design the solution to operate within the current VA Local Area Network (LAN) and Wide Area Network (WAN) network configurations.
- The deployment environment must meet the performance and downtime monitoring requirements of the solution.
- The team and data center must develop and provision a disaster recovery plan.
- All critical infrastructure components (including data) must be located at multiple physical locations.
- The application backup and restore solution must meet data recovery requirements \[Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO)\].
- The application UIs must exist as browser based UIs and roll and scroll in VistA.
- The application must establish secure access paths for accessing the application and application data.
- The solution must document specific reasons for all limited, external access to data, including the need to know along with security, privacy and other legal restrictions.
- The solution must implement appropriate controls that prevent unwarranted disclosure of sensitive, Personally Identifiable Information (PII), or Protected Health Information (PHI).
- The team must base all system interfaces (both external and internal) implemented by the solution on open standards such as SOAP, REST, JMS, MQ, HTTPS and standard message formats such as HL7and NCPDP.
- The solution must access available enterprise information through services.
- The VA TRM must identify all products and standards used by this solution as permissible for usage.

# Roles and Responsibilities


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Timeline](#timeline)
  - [Site Readiness Assessment](#site-readiness-assessment)
    - [Deployment Topology (Targeted Architecture)](#deployment-topology-targeted-architecture)
    - [Site Information (Locations, Deployment Recipients)](#site-information-locations-deployment-recipients)
  - [Resources](#resources)
    - [Facility Specifics](#facility-specifics)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
    - [Pre-requisites](#pre-requisites)
    - [Environment Configurations](#environment-configurations)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
    - [X Windows on VM1 and VM2](#x-windows-on-vm1-and-vm2)
    - [Setup Administration Accounts on VM1 and VM2](#setup-administration-accounts-on-vm1-and-vm2)
    - [Install Java on VM1 and VM2](#install-java-on-vm1-and-vm2)
    - [Apache Installation on VM1 and VM2](#apache-installation-on-vm1-and-vm2)
    - [Apache Configuration on VM1 and VM2](#apache-configuration-on-vm1-and-vm2)
    - [Certificate Configuration](#certificate-configuration)
    - [Create NSS certificate database on VM1](#create-nss-certificate-database-on-vm1)
    - [Create NSS certificate database on VM2](#create-nss-certificate-database-on-vm2)
    - [NSS Configuration on VM1 and VM2](#nss-configuration-on-vm1-and-vm2)
    - [NSS Configuration on VM2](#nss-configuration-on-vm2)
    - [Install Apache Plug-in for WebLogic on VM1 and VM2](#install-apache-plug-in-for-weblogic-on-vm1-and-vm2)
    - [Install Centrify for Apache on VM1 and VM2](#install-centrify-for-apache-on-vm1-and-vm2)
    - [Install IEP CPanel on VM1 and VM2](#install-iep-cpanel-on-vm1-and-vm2)
    - [Install Apache SSOi Web Agent on VM1](#install-apache-ssoi-web-agent-on-vm1)
    - [Configure Apache SSOi Web Agent on VM1](#configure-apache-ssoi-web-agent-on-vm1)
    - [Post Configure Edits for Apache SSOi Web Agent on VM1](#post-configure-edits-for-apache-ssoi-web-agent-on-vm1)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [VistA Patch Installation](#vista-patch-installation)
    - [WebLogic Installation](#weblogic-installation)
    - [Inbound eRx Application Installation](#inbound-erx-application-installation)
    - [Pentaho Installation](#pentaho-installation)
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
    - [Back-Out of Database](#back-out-of-database)
    - [Back-Out of WebLogic](#back-out-of-weblogic)
  - [Back-out VistA Patch](#back-out-vista-patch)
  - [Back-out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
    - [Rollback of Database](#rollback-of-database)
    - [Rollback WebLogic](#rollback-weblogic)
    - [Rollback VistA Patch](#rollback-vista-patch)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Operational Procedures](#operational-procedures)
  - [Startup Procedures](#startup-procedures)
    - [Start Weblogic Node Managers and Admin Console](#start-weblogic-node-managers-and-admin-console)
    - [Managed Servers](#managed-servers)
    - [Pentaho Services Startup](#pentaho-services-startup)
  - [Shut Down Procedures](#shut-down-procedures)
    - [Pentaho Services Shutdown](#pentaho-services-shutdown)
    - [WebLogic Application Server Shutdown](#weblogic-application-server-shutdown)
This section outlines the roles and responsibilities for managing the deployment of the PRE Inbound eRx system.
| ID  | Team                                                                                     | Phase / Role    | Tasks                                                                                                                | Project Phase (See Schedule) |
|-----|------------------------------------------------------------------------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------|------------------------------|
| 1   | FO, EO, NDCP or Product Development (depending upon project ownership)                   | Deployment      | Plan and schedule deployment (including orchestration with vendors).                                                 | Deployment                   |
| 2   | FO, EO, NDCP or Product Development (depending upon project ownership)                   | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                           | Design/Build                 |
| 3   | FO, EO, or NDCP                                                                          | Deployment      | Test for operational readiness.                                                                                      | Design/Build                 |
| 4   | FO, EO, or NDCP                                                                          | Deployment      | Execute deployment.                                                                                                  | Design/Build                 |
| 5   | FO, EO, or NDCP                                                                          | Installation    | Plan and schedule installation.                                                                                      | Deployment                   |
| 6   | Regional PM/ Field Implementation Services (FIS)/ Office of Policy and Planning (OPP) PM | Installation    | Ensure authority to operate and that certificate authority security documentation is in place.                       | Design/Build                 |
| 7   | Regional PM/FIS/OPP PM/ Nat’l Education & Training                                       | Installations   | Coordinate training.                                                                                                 | Deployment                   |
| 8   | FO, EO, NDCP or Product Development (depending upon project ownership)                   | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out). | Deployment                   |
| 9   | FO, EO, NDCP or Product Development (depending upon project ownership)                   | Post Deployment | Hardware, Software and System Support.                                                                               | Maintenance                  |
<span id="_Toc525722925" class="anchor"></span>Table 2: Deployment Timeline

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a phased rollout. This type of rollout is best suited for the rapid turnaround time and repeat nature of the installations required for this project.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="Timeline" class="anchor"></span>The deployment and installation is scheduled to run for 18 months as depicted in the master deployment schedule. The timelines are depicted in the Deployment Timeline table below.

| VIP Build                                                       | Delivery Dates    |
|-----------------------------------------------------------------|-------------------|
| VIP Build 1 - NewRx and Cancel Rx Request/Response              | 09/23/19-12/20/19 |
| VIP Build 2 - RxRenewal Request/Response                        | 12/23/19-04/10/20 |
| VIP Build 3 - RxChange / Rational Migration                     | 03/23/20-06/12/20 |
| VIP Build 4 - RxChange / Rational Migration                     | 06/15/20-09/04/20 |
| VIP Build 5 - Regression Testing, Bug fixes, Certification Test | 09/08/20-10/16/20 |
| IOC Preparation and Testing                                     | 10/19/20-12/10/20 |

<span id="_Toc525722926" class="anchor"></span>Table 3: Site Preparation

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the PRE Inbound eRx application deployment. Topology determinations are made by Enterprise Systems Engineering (ESE) and vetted by Field Operations (FO), National Data Center Program (NDCP), and AITC during the design phase as appropriate. Field site coordination is done by FO unless otherwise stipulated by FO.

The product will be released by the PRE Inbound eRx Configuration Manager to the AITC Build Manager via a Change Order. The AITC Build Manager will follow the installation steps in Section 4 to complete the product’s activation at AITC and for the Disaster Recovery server. The Implementation Manager has assured site readiness by assessing the readiness of the receiving site to deploy the product. AITC, under contract, will provide the product dependencies, power, equipment, space, manpower, etc., to ensure the successful activation of this product.

1.  Application Architecture

<span id="ApplicationArchitecture" class="anchor"></span>The following diagram represents the high-level architecture for the eRx application.

<span id="_Toc55375182" class="anchor"></span>Figure 2: High-Level eRx Architecture

![](psd-3-89-controlled-substance-dirb/003.png)

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product will be released to AITC. The AITC, under contract, will house and secure this product on its Pre-Production and then Production servers. A few field located super users will be given access upon National Release. The PRE Inbound eRx system will be available to VA users on a continuous basis (excluding scheduled maintenance activities). Clustering at the application and web services servers will provide high availability and failover capabilities at the application tier and presentation tier. The servers will be load-balanced to distribute uniform processing across all servers.

Additionally, a VistA patch will be released to all VistA sites.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="SiteInfo" class="anchor"></span>AITC will host the web and application servers for the PRE Inbound eRx system.

Initial Operating Capability (IOC) will occur in October of 2020. IOC sites are:

- VA Honolulu Regional Office
- Fayetteville VAMC Veterans Health Care System of the Ozarks
- Health Administration Center (Meds by Mail)
- Indianapolis, IN VA Medical Center

Site Preparation

No preparation is required for the individual VistA sites installing the VistA patch or using the Inbound eRx application.

The following table describes preparation required by AITC prior to deployment.

<table>
<caption><p><span id="_Toc525722927" class="anchor"></span>Table 4: Software Specifications</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 22%" />
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th>Site/Other</th>
<th>Problem/Change Needed</th>
<th>Features to Adapt/Modify to New Product</th>
<th>Actions/Steps</th>
<th>Owner</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AITC</td>
<td>Creation of VMs for application hosting</td>
<td>N/A</td>
<td><ul>
<li><p>Software Installation</p></li>
<li><p>Network configuration</p></li>
</ul></td>
<td>ESE</td>
</tr>
</tbody>
</table>

<span id="_Toc525722927" class="anchor"></span>Table 4: Software Specifications

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the hardware, software, and communications for the deployment of Inbound eRx, where applicable.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No facility-specific features are required for this deployment.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As middleware, PRE Inbound eRx requires no hardware to install.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes the software specifications required prior to deployment.

<table>
<caption><p><span id="_Toc525722928" class="anchor"></span>Table 5: Deployment/Installation/Back-Out Checklist</p></caption>
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Required Software</th>
<th>Make</th>
<th>Version</th>
<th>Configuration</th>
<th>Manufacturer</th>
<th>Other</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>WebLogic</p>
<p>Application Server</p></td>
<td>Application Server</td>
<td>12.2.1.4</td>
<td>Clustered</td>
<td>Oracle</td>
<td></td>
</tr>
<tr class="even">
<td>Oracle Database</td>
<td>Database</td>
<td>19.0.0.0.0</td>
<td>Standalone (not synchronized across data centers)</td>
<td>Oracle</td>
<td></td>
</tr>
<tr class="odd">
<td>Pentaho Data Integration</td>
<td>Data Integration Tool</td>
<td>9.0.0.0</td>
<td>Standalone</td>
<td>Pentaho (a Hitachi Group Company)</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc525722928" class="anchor"></span>Table 5: Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

The software components will be staged at the following location:

REDACTED

Application deployment packages will be staged at the following location:

REDACTED

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the communications to be distributed to the business user community:

- Communication between the development team and AITC will occur via email and conference calls scheduled through Microsoft Lync.
- Notification of scheduled maintenance periods that require the service to be offline or that may degrade system performance will be disseminated to the business user community a minimum of 48 hours prior to the scheduled event.
- Notification to VA users for unscheduled system outages or other events that impact the response time will be distributed within 30 minutes of the occurrence.
- Notification will be distributed to VA users regarding technical help desk support for obtaining assistance with receiving and processing inbound eRxs, and sending and receiving eRx transfers.

#### Deployment/Installation/Back-Out Checklist

The table below outlines the coordination effort and documents the day/time/individual when each activity (deploy, install, back-out) is completed for Inbound eRx.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   | TBD |      |                               |
| Install  | TBD |      |                               |
| Back-Out | TBD |      |                               |

<span id="_Toc525722929" class="anchor"></span>Table 6: Development/SQA Detailed VM Requirements

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the installation steps for the various Inbound eRx components.

1.  The highlighted sections throughout this document indicate that that the text will be modified in future versions of this document.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="PreReq" class="anchor"></span>This section outlines the minimum requirements for the product to be installed, as well as the recommended hardware and software system requirements.

### Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table outlines the specifications for VM.

| RAM (GB) | Space (GB) | CPUs | OS     | VM Description/Use/DNS Required                                 |
|----------|------------|------|--------|-----------------------------------------------------------------|
| 16       | 300        | 4    | RHEL 7 | DEV1 DB Server running Oracle                                   |
| 16       | 300        | 4    | RHEL 7 | DEV2 DB Server running Oracle                                   |
| 16       | 300        | 4    | RHEL 7 | SQA1 DB Server running Oracle                                   |
| 16       | 300        | 4    | RHEL 7 | DEV1 AP Server running Apache/WebLogic                          |
| 16       | 300        | 4    | RHEL 7 | DEV2 AP Server running Apache/WebLogic                          |
| 16       | 300        | 4    | RHEL 7 | DEV3 DB Server running Oracle/AP Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | DEV3 AP Server running Apache/WebLogic                          |
| 16       | 300        | 4    | RHEL 7 | SQA1 AP Server running Apache/WebLogic                          |
| 16       | 300        | 4    | RHEL 7 | SQA1 AP Server running Apache/WebLogic                          |

<span id="_Toc62812735" class="anchor"></span>Table 7: Staging Detailed VM Requirements

| RAM (GB) | Space (GB) | CPUs | OS     | VM Description/Use/DNS Required                  |
|----------|------------|------|--------|--------------------------------------------------|
| 16       | 800        | 4    | RHEL 7 | STAG1/STAG2 DB Server running Oracle             |
| 16       | 300        | 4    | RHEL 7 | STAG1 Application Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | STAG1 Application Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | STAG2 Application Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | STAG2 Application Server running Apache/WebLogic |

<span id="_Toc525722931" class="anchor"></span>Table 8: Pre-Production Detailed VM Requirements

| RAM (GB) | Space (GB) | CPUs | OS     | VM Description/Use/DNS Required                  |
|----------|------------|------|--------|--------------------------------------------------|
| 16       | 1300       | 4    | RHEL 7 | PREP1 DB Server running Oracle                   |
| 16       | 1300       | 4    | RHEL 7 | PREP2 DB Server running Oracle                   |
| 16       | 300        | 4    | RHEL 7 | PREP1 Application Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | PREP1 Application Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | PREP2 Application Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | PREP2 Application Server running Apache/WebLogic |

<span id="_Toc525722932" class="anchor"></span>Table 9: Production Detailed VM Requirements

| RAM (GB) | Space (GB) | CPUs | OS     | VM Description/Use/DNS Required                  |
|----------|------------|------|--------|--------------------------------------------------|
| 16       | 1300       | 4    | RHEL 7 | PROD1 DB Server running Oracle                   |
| 16       | 1300       | 4    | RHEL 7 | PROD2 DB Server running Oracle                   |
| 16       | 300        | 4    | RHEL 7 | PROD1 Application Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | PROD1 Application Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | PROD2 Application Server running Apache/WebLogic |
| 16       | 300        | 4    | RHEL 7 | PROD2 Application Server running Apache/WebLogic |

<span id="_Toc525722933" class="anchor"></span>Table 10: Environment Variables

### Environment Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 10 lists Environment Variables values that should be substituted throughout this document as system administrators are completing the installation steps.

| ENV   | ORACLE_BASE          | WLS_HOME               | DOMAIN_HOME                                       |
|-------|----------------------|------------------------|---------------------------------------------------|
| DEV1  | /u01/app/Oracle_Home | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/erxdomain1    |
| DEV2  | /u01/app/Oracle_Home | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/erxdomain2    |
| DEV3  | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-dev3      |
| SQA1  | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/erxdomain1    |
| STAG1 | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-stage     |
| STAG2 | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-stage2    |
| PREP1 | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-preprod   |
| PREP2 | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/ iep-preprod2 |
| PROD1 | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-prod      |
| PROD2 | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-prod2     |

<span id="_Toc62812739" class="anchor"></span>Table 11: Environment Variables (Continued)

| ENV   | JAVA_HOME               |                        |                                               |
|-------|-------------------------|------------------------|-----------------------------------------------|
| DEV1  | /u01/app/java/latest    | N/A                    | N/A                                           |
| DEV2  | /u01/app/java/latest    | N/A                    | N/A                                           |
| DEV3  | /u01/oracle/java/latest | N/A                    | N/A                                           |
| SQA1  | /u01/app/java/latest    | N/A                    | N/A                                           |
| STAG1 | /u01/app/java/latest    | N/A                    | N/A                                           |
| STAG2 | /u01/app/java/latest    | N/A                    | N/A                                           |
| PREP1 | /u01/app/java/latest    | N/A                    | N/A                                           |
| PREP2 | /u01/app/java/latest    | N/A                    | N/A                                           |
| PROD1 | /u01/oracle             | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-prod  |
| PROD2 | /u01/oracle             | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-prod2 |

<span id="_Toc525722934" class="anchor"></span>Table 12: Symbolic Names by Environment

The following table lists the symbolic names that should be substituted throughout this document as system administrators are completing the installation steps.

| ENV   | vm1_fqdn | vm1_name | vm2_fqdn | vm2_name | domain   |
|-------|----------|----------|----------|----------|----------|
| DEV1  | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |
| DEV2  | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |
| DEV3  | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |
| SQA1  | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |
| STAG1 | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |
| STAG2 | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |
| PREP1 | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |
| PREP2 | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |
| PROD1 | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |
| PROD2 | REDACTED | REDACTED | REDACTED | REDACTED | REDACTED |

<span id="_Toc55375299" class="anchor"></span>Table 13: Symbolic Names by Environment (cont)

| ENV   | env   | Env   | erx_port | proxy_fqdn | proxy_name | db_fqdn  | db_name  | db_port  |
|-------|-------|-------|----------|------------|------------|----------|----------|----------|
| DEV1  | dev1  | Dev1  | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |
| DEV2  | dev2  | Dev2  | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |
| DEV3  | dev2  | Dev3  | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |
| SQA1  | sqa1  | Sqa1  | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |
| STAG1 | stag1 | Stag1 | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |
| STAG2 | stag2 | Stag2 | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |
| PREP1 | prep1 | Prep1 | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |
| PREP2 | prep2 | Prep2 | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |
| PROD1 | prod1 | Prod1 | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |
| PROD2 | prod2 | Prod2 | REDACTED | REDACTED   | REDACTED   | REDACTED | REDACTED | REDACTED |

<span id="_Toc55375300" class="anchor"></span>Table 14: Symbolic Names by Environment (cont)

| ENV   | mserver1         | mserver2         | cluster    | machine1 | machine2 |
|-------|------------------|------------------|------------|----------|----------|
| DEV1  | erx1             | erx2             | dev1       | Machine1 | Machine2 |
| DEV2  | erx1             | erx2             | dev1       | Machine1 | Machine2 |
| DEV3  | ManagedServer001 | ManagedServer002 | Cluster001 | Machine1 | Machine2 |
| SQA1  | erx1             | erx2             | dev1       | Machine1 | Machine2 |
| STAG2 | ManagedServer001 | ManagedServer002 | Cluster001 | Machine1 | Machine2 |
| STAG1 | ManagedServer001 | ManagedServer002 | Cluster001 | Machine1 | Machine2 |
| PREP2 | ManagedServer001 | ManagedServer002 | Cluster001 | Machine1 | Machine2 |
| PREP1 | ManagedServer001 | ManagedServer002 | Cluster001 | Machine1 | Machine2 |
| PROD2 | ManagedServer001 | ManagedServer002 | Cluster001 | Machine1 | Machine2 |
| PROD1 | ManagedServer001 | ManagedServer002 | Cluster001 | Machine1 | Machine2 |

<span id="_Toc525722937" class="anchor"></span>Table 15: Symbolic Names by Environment (cont)

| ENV  | iam_hco    | iam_policy_entries |
|------|------------|--------------------|
| DEV1 | INTHCO     | REDACTED           |
| DEV2 | INTHCO     | REDACTED           |
| DEV3 | INTHCO     | REDACTED           |
| SQA1 | SQAHCO     | REDACTED           |
| STAG | PREPRODHCO | REDACTED           |

<span id="_Toc55375302" class="anchor"></span>Table 16: Symbolic Names by Environment (cont)

| ENV   | iam_hco    | iam_policy_entries |
|-------|------------|--------------------|
| STAG2 | PREPRODHCO | REDACTED           |
| PREP  | PREPRODHCO | REDACTED           |
| PREP2 | PREPRODHCO | REDACTED           |

<span id="_Toc525722939" class="anchor"></span>Table 17: Symbolic Names by Environment (cont)

| ENV   | iam_hco | iam_policy_entries |
|-------|---------|--------------------|
| PROD  | PRODHCO | REDACTED           |
| PROD2 | PRODHCO | REDACTED           |

<span id="_Toc525722940" class="anchor"></span>Table 18: Symbolic Names for sensitive items

In addition to the above Environment Variables and Symbolic Names, there are several passwords or secret phrases which are required throughout the installation. The table below identifies Symbolic Names that will be used in this document, and provide a brief description of each. The values of these sensitive items will be defined by the appropriate administrator during the installation process, and should be properly recorded and shared with others on a need to know basis.

| Symbolic Name         |
|-----------------------|
| keystore_passphrase   |
| privatekey_passphrase |
| weblogic_password     |

Symbolic Names by Environment (continued)Symbolic Names by Environment (Continued)

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="PlatformInstall" class="anchor"></span>The following sections describe the steps to prepare the operating system for the installation of the application. Most activities are to be performed by the RHEL System Administrator.

### X Windows on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Install the Linux X Window libraries (the following must be performed by a system administrator):

\$ dzdo yum install xorg-x11-xauth.x86_64

1.  Start Attachmate Reflection X (Click *Start* \> *All Programs* \> *Attachmate Reflection* \> *Reflection X*).
2.  Modify the SSH session:
    1.  Connection \> SSH \> X11 \> Enable X11 forwarding
    2.  Connection \> SSH \> X11 \> X display location \> :0.0
3.  Connect to the Linux server with the new SSH session settings. The DISPLAY environment variable should be automatically set.
4.  In order to run X applications after doing a dzdo su to another account, capture your xauthority.
5.  As your normal Linux login account:

\$ xauth list \| grep unix\`echo \$DISPLAY \| cut -c10-12\` \> /tmp/authx ; chmod o+r /tmp/authx

6.  After you dzdo su to another user, add the xauth and verify:

\$ xauth add \`cat /tmp/authx\` ; xauth list

\## \[set DISPLAY to localhost:xx.0 listed\] \##

\$ export DISPLAY=localhost:10.0

\$ xclock &

### Setup Administration Accounts on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify the /etc/sudoers file has “#includedir /etc/sudoers.d” entry near the end of the file, if not, perform the following:

\$ dzdo chmod u+w /etc/sudoers

\$ dzdo vi /etc/sudoers

> Add \#includedir /etc/sudoers.d near the end of the file, exit the vi editor.

\$ dzdo chmod u+w /etc/sudoers

7.  Modify the Linux weblogic account .bash_profile, replace the PATH= and export PATH with the following near the end of the file:

export JAVA_HOME=*\[ORACLE_BASE\]*/java/latest

export PATH=\${JAVA_HOME}/bin:\${PATH}:\${HOME}/bin

8.  Create the oracle software directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo chmod 755 /u01

\$ dzdo mkdir -p /u01/oracle

\$ dzdo chown weblogic:weblogic /u01/oracle

\$ dzdo chmod 755 /u01/oracle

9.  Create the Linux kettle user and group (the following must be performed by a system administrator):

\$ dzdo groupadd -g 7600 kettle

\$ dzdo useradd -g kettle

\$ dzdo usermod -a -G weblogic kettle (weblogic group already exists in LDAP)

10. Create the app software directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo chmod 755 /u01

\$ dzdo mkdir -p /u01/app

\$ dzdo chown weblogic:weblogic /u01/app

\$ dzdo chmod 755 /u01/app

11. Create the pentaho software directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/app/pentaho

\$ dzdo chown kettle:kettle /u01/app/pentaho

\$ dzdo chmod 755 /u01/app/pentaho

12. Modify the Linux kettle account to add umask command near the beginning of the file ~kettle/.bash_profile:

umask 0022

13. Modify the Linux kettle account .bash_profile, replace the PATH= and export PATH with the following near the end of the file:

export JAVA_HOME=/u01/app/java/latest/

export PATH=\${JAVA_HOME}/bin:\${PATH}:\${HOME}/bin

14. Create the Linux kettle sudoer file (the following must be performed by a system administrator):

\$ dzdo vi /etc/sudoers.d/kettle

kettle ALL=NOPASSWD:/sbin/service kettle start,/sbin/service kettle stop,/sbin/service kettle stop_all,/sbin/service kettle status

Cmnd_Alias KETTLE_SU=/bin/su - kettle

Cmnd_Alias KETTLE_CMD=/bin/ls, /bin/du, /bin/grep, /bin/cat, /sbin/chkconfig --list, /usr/sbin/lsof

%kettle ALL=(ALL) KETTLE_CMD

%kettle ALL=(ALL) KETTLE_SU

15. Create the Linux apache sudoer file (the following must be performed by a system administrator):

\$ dzdo vi /etc/sudoers.d/apache

apache ALL=(kettle:kettle) NOPASSWD:/u01/app/cpanel/bin/carte_slave_util.sh

### Install Java on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  As your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

16. Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

17. Download Oracle JDK 1.8 for Linux x86-64 to the downloads directory:

Download from ATIC IEP eRx Downloads directory

18. Create Java directory if it doesn’t exist:

\$ mkdir -p /u01/app/java

\$ chmod 755 /u01/app/java

19. Unpack the Oracle JDK 1.8 archive in the downloads directory:

\$ cd /u01/app/java

\$ gzip –cd \< /u01/downloads/jdk-8u*\[xxx\]*-linux-x64.tar.gz \| tar xvf -

20. Create symbolic link for latest Java installation:

\$ ln –s jdk1.8.0\_*\[xxx\]* latest

21. Open permissions to permit access to all users:

\$ find jdk1.8.0\_*\[xxx\]* -type d -exec chmod g+rx,o+rx {} \\

\$ find jdk1.8.0\_*\[xxx\]* -type f -exec chmod g+r,o+r {} \\

exit

22. Return back in your normal Linux login account.

\$ exit

### Apache Installation on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following steps on VM1 and VM2:

1.  EO SA installs standard Apache 2.2 RHEL6 RPM, as your normal Linux login account verify as follows:

\$ dzdo rpm -q -a \| grep httpd

httpd-tools-2.4.6-95.el7.x86_64

httpd-2.4.6-95.el7.x86_64

23. Install the Linux NSS package (the following must be performed by a system administrator):

\$ dzdo yum install mod_nss.x86_64

24. Modify the httpd startup configuration (the following must be performed by a system administrator):

\$ dzdo systemctl enable httpd \# for RHEL 7 systems

### Apache Configuration on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

servers are RHEL 7 and they have Apache version 2.4, Want to confirm if these instructions are for Apache 2.2 or 2.4?

Here are the differences between document and Apache conf file on server.

6\. No \<IfModule prefork.c\>

9\. No \<Directory “/var/www/icons”\> section

Instead \<Directory “/var/www/html”\> section exist and it has the Option parameter

Options Indexes FollowSymLinks

The following step need to be performed on VM1 and VM2:

1.  Modify HTTPD configuration:

\$ dzdo vi /etc/httpd/conf/httpd.conf

25. Modify Listen parameter in /etc/http/conf/httpd.conf:

Listen 80

26. Modify \<Directory /\> section in /etc/http/conf/httpd.conf:

\<Directory /\>

Options FollowSymLinks

AllowOverride None

\<Limit PUT\>

Order deny,allow

Deny from all

\</Limit\>

\</Directory\>

27. Modify \<Directory "/var/www/html"\> section in /etc/http/conf/httpd.conf:

\<Directory "/var/www/html"\>

Options Indexes FollowSymLinks

AllowOverride None

Order allow,deny

Allow from all

\</Directory\>

28. Modify \< IfModule alias_module\> section in /etc/http/conf/httpd.conf:

ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"

29. Modify \<Directory "/var/www/cgi-bin"\> section in /etc/http/conf/httpd.conf:

\<Directory "/var/www/cgi-bin"\>

AllowOverride None

Options None

Order allow,deny

Allow from all

\</Directory\>

30. Add Header Edit entries to bottom of /etc/http/conf/httpd.conf

\# Set security options for cookies (to prevent cross-site scripting \[XSS\] attacks)

Header edit Set-Cookie "(?i)^((?:(?!;\s?HttpOnly).)+)\$" "\$1; HttpOnly"

Header edit Set-Cookie "(?i)^((?:(?!;\s?secure).)+)\$" "\$1; Secure"

\# Prevent clickjacking attacks

Header always append X-Frame-Options DENY

31. Disable SSL:

\$ dzdo mv /etc/httpd/conf.d/ssl.conf /etc/httpd/conf.d/ssl.conf_orig

\$ dzdo touch /etc/httpd/conf.d/ssl.conf

\$ dzdo chmod 644 /etc/httpd/conf.d/ssl.conf

32. Modify the httpd startup configuration (the following must be performed by a system administrator):

\$ dzdo systemctl enable httpd

33. Start Apache:

\$ dzdo systemctl start httpd

<span class="mark">  
</span>

### Certificate Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Generate a permanent certificate using Venafi:

    Nickname: *\[vm1_fqdn\]*

    Description: *\[ERX\|IEP\]\[ENV\]*

    SAN’s: *\[vm1_fqdn\],\[vm1_fqdn\]*
34. Generate a *\[vm1_fqdn\]* pkcs12 certificate store:

\$ openssl pkcs12 -export -name *\[vm1_fqdn\]* -in *\[vm1_fqdn\]*.crt -inkey *\[vm1_fqdn\]*.key -out *\[vm1_fqdn\]*.p12

Enter Export Password: \####

Verifying - Enter Export Password: \####

35. Generate a *\[vm2_fqdn\]* pkcs12 certificate store:

\$ openssl pkcs12 -export -name *\[vm2_fqdn\]* -in *\[vm1_fqdn\]*.crt -inkey *\[vm1_fqdn\]*.key -out *\[vm2_fqdn\]*.p12

Enter Export Password: \####

Verifying - Enter Export Password: \####

36. Generate *\[vm1_fqdn\]* java keystore:

\$ keytool -importkeystore -deststorepass \######## -destkeypass \######## -destkeystore *\[vm1_fqdn\]*.jks -srckeystore *\[vm1_fqdn\]*.p12 -srcstoretype PKCS12 -srcstorepass \#### -alias *\[vm1_fqdn\]*

37. Import VA-Internal-S2-RCA1-v1.pem Certificate into *\[vm1_fqdn\]* java keystore:

\$ keytool -import -alias VA-Internal-S2-RCA1-v1 -file VA-Internal-S2-RCA1-v1.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

38. Import VA-Internal-S2-ICA4-v1.pem Certificate into *\[vm1_fqdn\]* java keystore:

\$ keytool -import -alias VA-Internal-S2-ICA1-v1 -file VA-Internal-S2-ICA1-v1.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

### Create NSS certificate database on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Create a new NSS certificate database:

\$ dzdo mv /etc/httpd/alias /etc/httpd/alias_orig

\$ dzdo mkdir /etc/httpd/alias

\$ dzdo chmod 755 /etc/httpd/alias

\$ dzdo certutil -N -d sql:/etc/httpd/alias

Enter new password: \####

Re-enter password: \####

39. Add server permanent certificate:

\$ dzdo pk12util -i *\[proxy_fqdn\]*.p12 -d sql:/etc/httpd/alias -n *\[proxy_fqdn\]*

Enter Password or Pin for "NSS Certificate DB": \####

Enter password for PKCS12 file: \####

pk12util: PKCS12 IMPORT SUCCESSFUL

40. Add certificate chain:

\$ dzdo certutil -A -d sql:/etc/httpd/alias -i VA-Internal-S2-RCA1-v1.pem -t CT,, \\  
-n VA-Internal-S2-RCA1-v1

\$ dzdo certutil -A -d sql:/etc/httpd/alias -i /u01/tmp/va_internal_s2_ica4.pem -t CT,, \\  
-n va_internal_s2_ica4

\$ dzdo certutil -A -d sql:/etc/httpd/alias -i /u01/tmp/va_internal_s2_rca1.pem -t CT,, \\  
-n va_internal_s2_rca1

41. Modify certificate database permissions:

\$ dzdo chmod g+rx,o+rx /etc/httpd/alias

\$ dzdo chmod -R g+r,o+r /etc/httpd/alias/\*

42. Verify installed certificates:

\$ certutil -L -d sql:/etc/httpd/alias

43. Create certificate database password file:

\$ cat \> /etc/httpd/conf/password.conf

internal:####

NSS FIPS 140-2 Certificate DB:####

\<ctrl\>d

44. Modify certificate database password file permissions:

\$ dzdo chmod g+r,o+r /etc/httpd/conf/password.conf

45. Start HTTPD server

\$ dzdo systemctl start httpd

### Create NSS certificate database on VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Create a new NSS certificate database:

\$ dzdo mv /etc/httpd/alias /etc/httpd/alias_orig

\$ dzdo mkdir /etc/httpd/alias

\$ dzdo cp /etc/httpd/alias_orig/pkcs11.txt /etc/httpd/alias

\$ dzdo certutil -N -d sql:/etc/httpd/alias

Enter new password: \####

Re-enter password: \####

46. Add server permanent certificate:

\$ dzdo pk12util -i *\[vm2_fqdn\]*.p12 -d sql:/etc/httpd/alias -n *\[vm2_fqdn\]*

Enter Password or Pin for "NSS Certificate DB": \####

Enter password for PKCS12 file: \####

pk12util: PKCS12 IMPORT SUCCESSFUL

47. Add certificate chain:

\$ dzdo certutil -A -d sql:/etc/httpd/alias -i VA-Internal-S2-RCA1-v1.pem -t CT,, \\  
-n VA-Internal-S2-RCA1-v1

\$ dzdo certutil -A -d sql:/etc/httpd/alias -i /u01/tmp/va_internal_s2_ica4.pem -t CT,, \\  
-n va_internal_s2_ica4

\$ dzdo certutil -A -d sql:/etc/httpd/alias -i /u01/tmp/va_internal_s2_rca1.pem -t CT,, \\  
-n va_internal_s2_rca1

48. Modify certificate database permissions:

\$ dzdo chmod g+rx,o+rx /etc/httpd/alias

\$ dzdo chmod -R g+r,o+r /etc/httpd/alias/\*

49. Verify installed certificates:

\$ certutil -L -d sql:/etc/httpd/alias

50. Create certificate database password file:

\$ cat \> /etc/httpd/conf/password.conf

internal:####

NSS FIPS 140-2 Certificate DB:####

\<ctrl\>d

51. Modify certificate database password file permissions:

\$ dzdo chmod g+r,o+r /etc/httpd/conf/password.conf

52. Start HTTPD server

\$ dzdo systemctl start httpd

### NSS Configuration on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps need to be performed on VM1 and VM2:

1.  Rename the RPM default ssl.conf file to ssl.conf_orig to prevent Apache from loading during startup.

\$ cd /etc/httpd/conf.d

\$ dzdo cp nss.conf nss.conf_orig

\$ dzdo mv ssl.conf ssl.conf_orig

\$ dzdo touch ssl.conf

\$ dzdo chmod 644 ssl.conf

53. Modify NSS configuration:

\$ dzdo cp /etc/httpd/conf.d/nss.conf /etc/httpd/conf.d/nss.conf_orig

\$ dzdo vi /etc/httpd/conf.d/nss.conf

1.  Modify Listen parameter:

> \#Listen 8443

> Listen 443

2.  Modify NSSPassPhraseDialog parameter:

> \#NSSPassPhraseDialog builtin

> NSSPassPhraseDialog file:/etc/httpd/conf/password.conf

> NSSFIPS on

3.  Modify VirtualHost tag:

> \#\<VirtualHost \_default\_:8443\>

> \<VirtualHost \_default\_:443\>

4.  Modify ServerName parameter:

> \#ServerName www.example.com:8443

> ServerName *\[proxy_fqdn\]*:443

5.  Modify NSS logging parameters:

> \#ErrorLog /etc/httpd/logs/error_log

> \#TransferLog /etc/httpd/logs/access_log

> ErrorLog /etc/httpd/logs/nss_error_log

> TransferLog /etc/httpd/logs/nss_access_log

6.  Modify NSSCipherSuite parameters:

> \#NSSCipherSuite +aes_128_sha_256,+aes_256_sha_256,+ecdhe_ecdsa_aes_128_gcm_sha_256,+ecdhe_ecdsa_aes_128_sha,+ecdhe_ecdsa_aes_256_sha,+ecdhe_rsa_aes_128_gcm_sha_256,+ecdhe_rsa_aes_128_sha,+ecdhe_rsa_aes_256_sha,+rsa_aes_128_gcm_sha_256,+rsa_aes_128_sha,+rsa_aes_256_sha

> NSSCipherSuite +rsa_aes_128_sha,+rsa_aes_256_sha

7.  Modify NSSProtocol parameters:

> \#NSSProtocol SSLv3,TLSv1.0,TLSv1.1

> NSSProtocol TLSv1.1,TLSv1.2

8.  Modify NSSNickname parameter:

> \#NSSNickname Server-Cert

> NSSNickname *\[proxy_fqdn\]*

> NSSEnforceValidCerts off

9.  Modify NSSCertificateDatabase parameter:

> \#NSSCertificateDatabase /etc/httpd/alias

> NSSCertificateDatabase sql:/etc/httpd/alias

10. Save the nss.conf file.
54. Start HTTPD server

\$ dzdo systemctl restart httpd

55. Review access_log, error_log, nss_access_log and nss_error_log to ensure TLS is functioning correctly.

### NSS Configuration on VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps need to be performed on VM1 and VM2:

1.  Rename the RPM default ssl.conf file to ssl.conf_orig to prevent Apache from loading during startup.

\$ cd /etc/httpd/conf.d

\$ dzdo mv ssl.conf ssl.conf_orig

\$ dzdo touch ssl.conf

\$ dzdo chmod 644 ssl.conf

56. Modify NSS configuration:

\$ dzdo vi /etc/httpd/conf.d/nss.conf

1.  Modify Listen parameter:

> \#Listen 8443

> Listen 443

2.  Modify NSSPassPhraseDialog parameter:

> \#NSSPassPhraseDialog builtin

> NSSPassPhraseDialog file:/etc/httpd/conf/password.conf

> NSSFIPS on

3.  Modify VirtualHost tag:

> \#\<VirtualHost \_default\_:8443\>

> \<VirtualHost \_default\_:443\>

4.  Modify ServerName parameter:

> \#ServerName www.example.com:8443

> ServerName *\[vm2_fqdn\]*:443

5.  Modify NSS logging parameters:

> \#ErrorLog /etc/httpd/logs/error_log

> \#TransferLog /etc/httpd/logs/access_log

> ErrorLog /etc/httpd/logs/nss_error_log

> TransferLog /etc/httpd/logs/nss_access_log

6.  Modify NSSCipherSuite parameters:

> \#NSSCipherSuite +aes_128_sha_256,+aes_256_sha_256,+ecdhe_ecdsa_aes_128_gcm_sha_256,+ecdhe_ecdsa_aes_128_sha,+ecdhe_ecdsa_aes_256_sha,+ecdhe_rsa_aes_128_gcm_sha_256,+ecdhe_rsa_aes_128_sha,+ecdhe_rsa_aes_256_sha,+rsa_aes_128_gcm_sha_256,+rsa_aes_128_sha,+rsa_aes_256_sha

> NSSCipherSuite +rsa_aes_128_sha,+rsa_aes_256_sha

7.  Modify NSSProtocol parameters:

> \#NSSProtocol SSLv3,TLSv1.0,TLSv1.1

> NSSProtocol TLSv1.1,TLSv1.2

8.  Modify NSSNickname parameter:

> \#NSSNickname Server-Cert

> NSSNickname *\[proxy_fqdn\]*

> NSSEnforceValidCerts off

9.  Modify NSSCertificateDatabase parameter:

> \#NSSCertificateDatabase /etc/httpd/alias

> NSSCertificateDatabase sql:/etc/httpd/alias

10. Save the nss.conf file.
57. Start HTTPD server

\$ dzdo systemctl restart httpd

58. Review access_log, error_log, nss_access_log and nss_error_log to ensure TLS is functioning correctly.

### Install Apache Plug-in for WebLogic on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps need to be performed on VM1 and VM2:

1.  As your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

59. Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

60. Download Oracle WLS Plugin 12.2.1.3 archive (v44415-01) to the downloads directory:

Download from AITC IEP eRx Downloads directory

61. Unzip the Oracle WLS Plugin 12.2.1.3 archive to in the downloads directory:

\$ unzip fmw_12.2.1.3.0_wlsplugins_Disk1_1of1.zip WLSPlugins12c-12.2.1.3.0.zip

\$ unzip WLSPlugins12c-12.2.1.3.0.zip \\

WLSPlugin12.2.1.3.0-Apache2.2-Apache2.4-Linux_x86_64-12.2.1.3.0.zip

\$ mkdir WLSPlugin12.2.1.3.0-Apache2.2-Apache2.4-Linux_x86_64-12.2.1.3.0

\$ unzip WLSPlugin12.2.1.3.0-Apache2.2-Apache2.4-Linux_x86_64-12.2.1.3.0 \\

-d WLSPlugin12.2.1.3.0-Apache2.2-Apache2.4-Linux_x86_64-12.2.1.3.0

\$ chmod -R g+rx,o+rx WLSPlugin12.2.1.3.0-Apache2.2-Apache2.4-Linux_x86_64-12.2.1.3.0

\$ exit

62. You should be back in your normal Linux login account.
63. Copy the Apache Plug-in for WebLogic libraries to the HTTPD modules directory (the following must be performed by a system administrator):

\$ dzdo cp -r /u01/downloads/WLSPlugin12.2.1.3.0-Apache2.2-Apache2.4-Linux_x86_64-12.2.1.3.0 /etc/httpd/modules/WLSPlugin

\$ dzdo find /etc/httpd/modules/WLSPlugin -type d -exec chmod 755 {} \\

\$ dzdo find /etc/httpd/modules/WLSPlugin/\[bjl\]\* -type f -exec chmod 755 {} \\

64. Modify the /etc/sysconfig/httpd file (the following must be performed by a system administrator):

\$ dzdo vi /etc/sysconfig/httpd

Add the following to the end of the file:

\# Update LD_LIBRARY_PATH to include Weblogic Plugin

LD_LIBRARY_PATH=\${LD_LIBRARY_PATH}:/etc/httpd/modules/WLSPlugin/lib

### Install Centrify for Apache on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps need to be performed on VM1 and VM2:

1.  Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

65. As your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

66. Download the Centrify for Apache package (centrify-apache-4.4.4-rhel3-x86_64.tgz) to the downloads directory from AITC IEP eRx Downloads directory
67. Unzip Centrify for Apache package to in the downloads directory:

\$ cd /u01/downloads

\$ mkdir centrify-apache-4.4.4-rhel3-x86_64

\$ tar xvzf centrify-apache-4.4.4-rhel3-x86_64.tgz -C centrify-apache-4.4.4-rhel3-x86_64

\$ chmod o+rx centrify-apache-4.4.4-rhel3-x86_64

\$ chmod o+r centrify-apache-4.4.4-rhel3-x86_64/\*

\$ exit

68. You should be back in your normal Linux login account.
69. Install the Centrify for Apache package (the following must be performed by a system administrator):

\$ dzdo rpm -Uvh /u01/downloads/centrify-apache-4.4.4-rhel3-x86_64/centrifydc-apache-4.4.4-rhel3-x86_64.rpm

### Install IEP CPanel on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  On VM1, create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

70. Download the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh) to the downloads directory.
71. As your normal Linux login account, dzdo execute the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh) (the following must be performed by a system administrator):

\$ dzdo /u01/downloads/erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh

72. Select options 1 and 2, then Exit (x).
73. Repeat steps 1 through 4 on VM2
74. Check the CPanel, pull up the following URL's in a Browser:

\$ https://*\[vm1_fqdn\]*/cpanel

\$ https://*\[vm2_fqdn\]*/cpanel

### Install Apache SSOi Web Agent on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Start Xming or other X Server on your Windows Desktop/Laptop. Connect to the server using Putty. The DISPLAY environment variable should be set.
2.  Unzip the CA SiteMinder Apache Web Agent archive to in the downloads directory:

\# cd /u01/downloads/

\[root @ downloads\]# unzip smwa-12.52-sp01-cr08-linux-x86-64.zip

Archive: smwa-12.52-sp01-cr08-linux-x86-64.zip

inflating: ca-wa-12.52-sp01-cr08-linux-x86-64.bin

\[root @ downloads\]# ls -l ca-wa-12.52-sp01-cr08-linux-x86-64.bin

-rw-r--r--. 1 root root 206187897 Oct 4 2017 ca-wa-12.52-sp01-cr08-linux-x86-64.bin

\[root @ downloads\]# chmod ugo+x ca-wa-12.52-sp01-cr08-linux-x86-64.bin

\[root @ downloads\]# ./ca-wa-12.52-sp01-cr08-linux-x86-64.bin

Preparing to install

Extracting the JRE from the installer archive...

Unpacking the JRE...

Extracting the installation resources from the installer archive...

Configuring the installer for this system's environment...

Launching installer...  
Scroll to bottom of license and accept: ![](psd-3-89-controlled-substance-dirb/004.png)

Enter installation path: /u01/app/CA/webagent

3\. Confirm: ![](psd-3-89-controlled-substance-dirb/005.png)

4\. Exit:![](psd-3-89-controlled-substance-dirb/006.png)

### Configure Apache SSOi Web Agent on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Go here for background; need admin user to SSOi for setup for the particular zone (DEV, SQA, PROD, etc)
    1.  [AcS Playbook Home (sharepoint.com)](https://dvagov.sharepoint.com/sites/OITEPMOIAM/playbooks/Pages/AcS%20Playbook%20Home.aspx)
    2.  [IAM URLs (sharepoint.com)](https://dvagov.sharepoint.com/sites/OITEPMOIAM/playbooks/Pages/IAM%20URLs.aspx)
    3.  [IAM VAEC Dashboard](https://iamportal.iam.va.gov/iamv2/index.php)
2.  As your normal Linux login account, dzdo su to the root account (the following must be performed by a system administrator):

\$ dzdo su -

75. Change directory to the agent home and "source" the Siteminder environment:

\# cd /u01/app/CA/webagent

\# . ./ca_wa_env.sh

76. Change to install config info directory and launch the configuration wizard (don’t put \`-i console\` for GUI):

\# cd install_config_info

\# ./ca-wa-config.bin -i console

77. Type 1 to register the trusted host, then Press Enter

-\>1- Yes, I would like to do Host Registration now.

2- No, I would like to do Host Registration later.

![](psd-3-89-controlled-substance-dirb/007.png)

78. In the Admin User Name prompt, type threg then press Enter

Admin User Name (Default: ): threg

79. For Shared Secret Rollover, type n then press Enter

Enable Shared Secret Rollover (y/n) (Default: n): n

80. For Allow Trusted Host Override, type y then press Enter

    Allow Trusted Host Overwrite (y/n) (Default: Based On Locale): y
81. Type the threg password then press Enter

Confirm Admin Password: \<- va1234!

![](psd-3-89-controlled-substance-dirb/008.png)

82. Type the Trusted Host Name then press Enter

Specify the name of the host you want to register with the Policy Server.

Enter the name of the host configuration object. The name must match a host

configuration object name already defined on the Policy Server.

Trusted Host Name (Default: ): *\[local_fqdn\]*

83. Type the Host Configuration Object then press Enter

Host Configuration Object (Default: ): *\[iam_hco\]*

![](psd-3-89-controlled-substance-dirb/009.png)

84. Type the Policy Server IP Address (only one host and port)

Policy Server IP Address

------------------------

Enter the IP Address of the Policy Server where you are registering this host.

Policy Server IP Address (Default: ): *\[iam_policy\]*

![](psd-3-89-controlled-substance-dirb/010.png)

85. In the FIPS Mode Settings, select FIPS Only Mode
86. Confirm the default file name and location of Host configuration ![](psd-3-89-controlled-substance-dirb/011.png)
87. Checking with policy server: ![](psd-3-89-controlled-substance-dirb/012.png)
88. Select 1 for Apache Web Server ![](psd-3-89-controlled-substance-dirb/013.png)
89. Specify the path to apache instance ![](psd-3-89-controlled-substance-dirb/014.png)

Apache Web Server path

----------------------

Enter the root path of where Apache Web server installed.

Please enter path (Default: ): /etc/httpd

90. Select the correct Apache version, ![](psd-3-89-controlled-substance-dirb/015.png)

Apache Version

--------------

Please select a choice for the Apache version.

1- Apache version 1.x

2- Apache version 2.x

3- Apache version 2.2.x

4- Apache version 2.4.x

ENTER THE NUMBER OF THE DESIRED CHOICE: 4

91. Select the correct Apache Type, type ![](psd-3-89-controlled-substance-dirb/016.png)

Apache Server Type

------------------

Please select one of the following appropriately match your previous selection

1- Oracle HTTP Server

2- IBM HTTP Server

3- HP Apache

4- ASF/RedHat Apache

5- RedHat JWS HTTP Server

ENTER THE NUMBER OF THE DESIRED CHOICE: 4

92. Confirm the Apache version ![](psd-3-89-controlled-substance-dirb/017.png)

Select Web Server(s)

--------------------

1- \[\] Apache 2.x.xx

93. Enter the Agent Configuration Object, ![](psd-3-89-controlled-substance-dirb/018.png)

Agent Configuration Object

--------------------------

Agent Configuration Object (Default: AgentObj): PREAgentConfig

94. Select Basic over SSL Authentication, ![](psd-3-89-controlled-substance-dirb/019.png)

SSL Authentication

------------------

The following SSL configurations are available for this web server. If the

Web Agent will be providing advanced authentication, select which

configuration it will use to configure Apache 2.2.15.

-\>1- HTTP Basic over SSL

ENTER THE NUMBER FOR YOUR CHOICE, OR PRESS \<ENTER\> TO ACCEPT THE DEFAULT:: 1

95. Enable the WebAgent ![](psd-3-89-controlled-substance-dirb/020.png)

Webagent Enable option

----------------------

Please select Yes to Enable the WebAgent

1- Yes

-\>2- No

ENTER THE NUMBER FOR YOUR CHOICE, OR PRESS \<ENTER\> TO ACCEPT THE DEFAULT:: 1

96. On the Summary Screen, Type 1 then press Enter

Web Server Configuration Summary

--------------------------------

Please confirm the configuration selection. Accept the configuration and

press 'Enter' to continue. To change one or more settings, select 'Previous'.

Select 'Cancel' will exit the configuration.

Configure the following webserver(s):

Apache Server:

Apache 2.2.15

Agent Configuration Object: PREAgentConfig

SSL Authentication type: HTTP Basic over SSL

IS WebAgent Enabled: YES

Please enter a choice.

-\>1- Continue

2- Previous

3- Cancel

ENTER THE NUMBER OF THE DESIRED CHOICE, OR PRESS \<ENTER\> TO ACCEPT THE

DEFAULT: 1

97. Continue installation if ssl.conf file doesn’t exist:

1- Continue

2- Exit

Unable to process configuration. File /etc/httpd/conf.d/ssl.conf doesnt

exist. Please make sure the configuration path is valid.

Please select a choice.: 1

98. Confirm exit from installer:

PRESS \<ENTER\> TO EXIT THE INSTALLER: \<ENTER\>

### Post Configure Edits for Apache SSOi Web Agent on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

99. As root, edit /u01/app/CA/webagent/config/SmHost.conf:

vi /u01/app/CA/webagent/config/SmHost.conf

100. Replace first policyserver entry with complete list. SQA for example:

REDACTED

Edit /etc/httpd/conf/WebAgent.conf:

vi /etc/httpd/conf/WebAgent.conf

101. Enable the agent:

EnableWebAgent=”YES”

102. For an embedded Apache web server (included by default) on a RedHat Linux system, modify certain configuration files to accommodate the product first. Follow these steps:.

cp /etc/sysconfig/httpd /etc/sysconfig/httpd.orig

vi /etc/sysconfig/httpd

Add the following line to the end of the file:

PATH=\$PATH:/u01/app/CA/webagent/bin

Save the changes and close the text editor.

103. Source ca_wa_env.sh script in the following file (instead of starting it manually each time):

     \# vi /etc/sysconfig/httpd

     Add the following code snippet after the similar snippet for /etc/sysconfig/httpd

\# Source CA Webagent environment

if \[ -f /u01/app/CA/webagent/ca_wa_env.sh \]; then

. /u01/app/CA/webagent/ca_wa_env.sh

fi

104. Modify the apachectl script to set the webagent environment variables:

cp /usr/sbin/apachectl /usr/sbin/apachectl.orig

vi /usr/sbin/apachectl

Locate a line resembling the following example:

\# Source /etc/sysconfig/httpd for \$HTTPD setting, etc

Add the following code snippet after the similar snippet for /etc/sysconfig/httpd/: (go to line 66)

\# Source CA Webagent environment

if \[ -r /u01/app/CA/webagent/ca_wa_env.sh \]; then

. /u01/app/CA/webagent/ca_wa_env.sh

fi

105. Modify permission of CA webagent files

\# chmod 666 /u01/app/CA/webagent/config/SmConf.conf

\# chown apache: /u01/app/CA/webagent/log

\# chmod 777 /u01/app/CA/webagent/log

106. Create /opt/ca/webagent symbolic link

\# mkdir /opt/ca

\# chmod 755 /opt/ca

\# ln -s /u01/app/CA/webagent/ /opt/ca/webagent

107. Modify trace file verbosity

     Modify trace.conf file:

\# vi /opt/ca/webagent/config/trace.conf

Modify lines near the bottom per the following:

nete.enableConsoleLog=0

nete.enableFileLog=0

nete.logFile=0

nete.conapi.logLevel=0

nete.conapi.ipc.logLevel=0

nete.conapi.tcpip.logLevel=0

nete.mon.monitoringApiLogLevel=0

In same directory, modify WebAgentTrace.conf file:

\# vi WebAgentTrace.conf

Modify lines neer the bottom to be:

components: WebAgent

data: Date, Time, Pid, Function, TransactionID, User, Message

108. Modify sysctl for Apache on RHEL 7.

> To keep apache updates from breaking this in the future, an override file needs to be created with a systemd command:

> \# systemctl edit httpd.service

> This will open a text file (possibly empty) to edit. Drop in the following:

> *\[Service\]*

> *ExecStart=*

> *ExecReload=*

> *ExecStart=/bin/bash -a -c 'source /u01/app/CA/webagent/ca_wa_env.sh && exec /usr/sbin/httpd \$OPTIONS -DFOREGROUND'*

> *ExecReload=/bin/bash -a -c 'source /u01/app/CA/webagent/ca_wa_env.sh && exec /usr/sbin/httpd \$OPTIONS -k graceful'*

> Write and Exit. This will create /etc/systemd/system/httpd.service.d/override.conf.

> Do a reload:

> \# systemctl daemon-reload

109. Restart and check Apache.

\# systemctl restart httpd

\# systemctl -l status httpd

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to this guide.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to this guide.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to this guide.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to this guide.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to this guide.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="InstallProcedure" class="anchor"></span>This section provides step-by-step instructions for installing all components of the Inbound eRx software on all platforms.

### VistA Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### PSO\*7\*617 Installation

Pre-Installation Instructions:

This patch should be installed during non-peak hours to minimize potential

disruption to users. Staff should not be processing prescriptions while patch

is being installed. This patch should take less than 5 minutes to install.

Installation Instructions:

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation & Distribution System menu, select the

Installation menu. From this menu, select Backup a Transport Global. This

option will create a backup message of any routines exported with this

patch. It will not backup any other changes such as DD's or templates. When

prompted for INSTALL NAME, enter the patch \#: PSO\*7.0\*617

4\. From the Installation menu, you may select to use the following options.

When prompted for INSTALL NAME, enter the patch \#: PSO\*7.0\*617

a\. Verify Checksums in Transport Global - This option will allow you to

ensure the integrity of the routines that are in the transport global.

b\. Print Transport Global - This option will allow you to print only a

summary of the patch, to print a summary of the patch and the routines

in the transport global, or to print only the routines in the

transport global.

c\. Compare Transport Global to Current System - This option will allow

you to view all changes that will be made when this patch is installed.

(It compares all components of this patch's routines, DDs, templates,

etc.).

5\. From the Installation menu, select the Install Package(s) option and

choose the patch to install.

6\. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//',

respond NO.

7\. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//', respond NO.

#### PSD\*3\*89 Installation

Pre-Installation Instructions:

There are no pre-installation steps for this patch.

This patch may be installed with users on the system, but it is

recommended that it be installed during non-peak hours to minimize

potential disruption to users. Staff should not be processing

prescriptions while patch is being installed. This patch should take less

than 5 minutes to install.

There are no Menu Options to disable.

Installation Instructions:

1\. Choose the PackMan message containing this patch.

2\. Choose the INSTALL/CHECK MESSAGE PackMan option.

3\. From the Kernel Installation & Distribution System menu, select

the Installation menu.

a\. Verify Checksums in Transport Global - This option will allow

you to ensure the integrity of the routines that are in the

transport global.

b\. Print Transport Global - This option will list the contents of

of the transport global (what was loaded from the KIDS file).

c\. Compare Transport Global to Current System - This option will

allow you to view all changes that will be made when this patch

is installed. It compares all components of this patch

(routines, DDs, templates, etc.).

d\. Backup a Transport Global - This option will create a backup

message of any routines exported with this patch. It will not

backup any other changes such as DDs or templates. This step is

required for patch back-out processing.

5\. From the Installation menu, select the Install Package(s) option and

choose the patch to install - PSD\*3.0\*89.

6\. When prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of

Install? NO//' respond NO

7\. When prompted 'Want KIDS to INHIBIT LOGONs during the install?

NO//' respond NO

8\. When prompted 'Want to DISABLE Scheduled Options, Menu Options,

and Protocols? NO//' respond NO

### WebLogic Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections describe the steps to install the WebLogic application server. Most activities are to be performed by the WebLogic Administrator.

#### Install WebLogic on VM1 and VM2

1.  Start Xming or other X Server on your Windows Desktop/Laptop. Connect to the server using Putty. The DISPLAY environment variable should be set.
110. As your normal Linux login account:
     1.  \$ xauth list \| grep unix\`echo \$DISPLAY \| cut -c10-12\` \> /tmp/authx
     2.  \$ chmod o+r /tmp/authx
111. After you dzdo su to weblogic, add the xauthority and see whether it’s working:
     1.  \$ xauth add \`cat /tmp/authx\`
     2.  \$ xauth list
     3.  \## \[set DISPLAY to localhost:xx.0 listed\] \##
     4.  \$ export DISPLAY=localhost:10.0
     5.  \$ xclock &
112. Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

113. Download Oracle WLS 12.2.1.4 installer to the downloads directory:

Download from AITC IEP eRx Downloads directory

114. Unzip the Oracle WLS 12.1.3 installer to the downloads directory:

\$ unzip fmw_12.2.1.4.0_wls_Disk1_1of1.zip fmw_12.2.1.4.0_wls.jar

115. Run the Oracle WLS 12.1.3 installer:

\$ java -jar fmw_12.2.1.4.0_wls.jar

116. Enter “y” to accept prerequisite checks.
117. Enter “/u01/oracle/oraInventory”.
118. Click OK.

<span id="_Toc55375183" class="anchor"></span>Figure 3: Install WebLogic – Oracle Fusion Middleware Installation Inventory Setup

![](psd-3-89-controlled-substance-dirb/021.png)

119. The Oracle Universal Installer will appear for a few moments.

<span id="_Toc55375184" class="anchor"></span>Figure 4: Install WebLogic – Oracle Universal Installer Dialog Box

![](psd-3-89-controlled-substance-dirb/022.png)

120. Once the installer comes up, click Next.

<span id="_Toc55375185" class="anchor"></span>Figure 5: Install WebLogic – Oracle Fusion Middleware WebLogic Server and Coherence Installer Screen

![](psd-3-89-controlled-substance-dirb/023.png)

121. Click Next:

     ![](psd-3-89-controlled-substance-dirb/024.png)
122. Enter *Oracle Home*: “*\[ORACLE_BASE\]/Oracle_Home*”. /u01/oracle/Oracle_Home
123. Click Next.

<span id="_Toc55375186" class="anchor"></span>Figure 6: Install WebLogic – Installation Location

![](psd-3-89-controlled-substance-dirb/025.png)

124. For *Installation Type*, select the *WebLogic Server* radio button.
125. Click Next.

<span id="_Toc55375187" class="anchor"></span>Figure 7: Install WebLogic – Installation Type

![](psd-3-89-controlled-substance-dirb/026.png)

126. Click Next again on the Prerequisite Checks screen.

<span id="_Toc55375188" class="anchor"></span>Figure 8: Install WebLogic – Prerequisite Checks

![](psd-3-89-controlled-substance-dirb/027.png)

127. On the *Installation Summary* screen, click Install.

<span id="_Toc55375189" class="anchor"></span>Figure 9: Install WebLogic – Installation Summary Screen

![](psd-3-89-controlled-substance-dirb/028.png)

128. Wait while the installation progresses.
129. Once the installation is complete, the following screen will display.
130. Click Next.

<span id="_Toc55375190" class="anchor"></span>Figure 10: Install WebLogic – Installation Progress Screen

![](psd-3-89-controlled-substance-dirb/029.png)

131. On VM1, leave *Automatically Launch the Configuration Wizard* checked, on VM2 uncheck it.
132. Click Finish.

<span id="_Toc55375191" class="anchor"></span>Figure 11: Install WebLogic – Installation Complete

![](psd-3-89-controlled-substance-dirb/030.png)

133. On VM2, skip the remaining steps in this section.
134. On VM1, the Oracle Configuration Wizard splash screen will appear for a few moments.

<span id="_Toc55375192" class="anchor"></span>Figure 12: Install WebLogic – Oracle Configuration Wizard Splash Screen

![](psd-3-89-controlled-substance-dirb/031.png)

135. On the Configuration Type screen, select *Create a new domain*.
136. Enter the following in the *Domain Location*:

*\[ORACLE_BASE\]*/Oracle_Home/user_projects/domains/*\[domain\]*

137. Click Next.

<span id="_Toc55375193" class="anchor"></span>Figure 13: Install WebLogic – Create New Domain

![](psd-3-89-controlled-substance-dirb/032.png)

138. On the Templates screen, select the *Create Domain using Product Templates* radio button.
139. Under *Available Templates*, select “Basic WebLogic Server Domain”.
140. Click Next.

<span id="_Toc55375194" class="anchor"></span>Figure 14: Install WebLogic – Templates Screen

![](psd-3-89-controlled-substance-dirb/033.png)

141. On the Administrator Account screen, enter *Name*: “weblogic”
142. Enter *Password*: “#########”
143. Enter *Confirm Password*: “#########”
144. Click Next.

<span id="_Toc55375195" class="anchor"></span>Figure 15: Install WebLogic – Administrator Account Screen

![](psd-3-89-controlled-substance-dirb/034.png)

145. On the Domain Mode and JDK screen, select the *Development* radio button for the *Domain Mode*.
146. For *JDK*, select the *Other JDK Location* radio button, and specify *{JAVA_HOME}*. /u01/app/java/latest
147. Click Next.

<span id="_Toc55375196" class="anchor"></span>Figure 16: Install WebLogic - Domain Mode and JDK

![](psd-3-89-controlled-substance-dirb/035.png)

148. On the Advanced Configuration screen, check *Administration Server, Node Manager*, and *Managed Servers, Clusters and Coherence*.
149. Click Next.

<span id="_Toc55375197" class="anchor"></span>Figure 17: Install WebLogic– Advanced Configuration

![](psd-3-89-controlled-substance-dirb/036.png)

150. On the Administration Server screen, enter *Server Name*: “AdminServer”
151. Enter *Listen Address*: “All Local Addresses”
152. Enter *Listen Port*: “7001”
153. Uncheck the check box for *Enable SSL*.
154. Leave the *SSL Listen Port* field blank.
155. Click Next.

<span id="_Toc55375198" class="anchor"></span>Figure 18: Install WebLogic – Administration Server Screen

![](psd-3-89-controlled-substance-dirb/037.png)

156. On the Node Manager screen, select the *Per Domain Default Location* radio button.
157. Enter *Username*: “weblogic”
158. Enter *Password*: “#########”
159. Enter *Confirm Password*: “#########”
160. Click Next.

<span id="_Toc55375199" class="anchor"></span>Figure 19: Install WebLogic – Node Manager

![](psd-3-89-controlled-substance-dirb/038.png)

161. On the Managed Servers screen, click Add.
162. Enter the *Server Name*: *\[mserver1\]*
163. Enter the *Listen Address*: *\[vm1_fqdn\]*
164. Enter *Listen Port*: “8001”
165. Leave *Enable SSL* unchecked.
166. Leave *SSL Listen Port* empty (Disabled).
167. Click Add.
168. Enter *Server Name*: *\[mserver2\]*
169. Enter *Listen Address*: *\[vm2_fqdn\]*
170. Enter Listen Port: “8001”
171. Leave *Enable SSL* unchecked.
172. Leave *SSL Listen Port* empty (Disabled).
173. Click Next.

<span id="_Toc55375200" class="anchor"></span>Figure 20: Install WebLogic – Managed Servers

![](psd-3-89-controlled-substance-dirb/039.png)

174. On the Clusters screen, click Add.
175. Enter *Cluster Name*: "*\[cluster\]*"
176. Enter *Cluster Address*: “*\[vm1_fqdn\]*:*\[erx_port\]*,*\[vm2_fqdn*\]:*\[erx_port\]*”
177. Enter *Frontend Host*: “*\[proxy_fqdn\]*”
178. Enter *Frontend HTTP Port*: “80”
179. Enter *Frontend HTTPS*: “443”
180. Click Next.

<span id="_Toc55375201" class="anchor"></span>Figure 21: Install WebLogic – Clusters

![](psd-3-89-controlled-substance-dirb/040.png)

181. Click Next.

![](psd-3-89-controlled-substance-dirb/041.png)

182. Click Next.

![](psd-3-89-controlled-substance-dirb/042.png)

183. Assign *\[mserver1\]* and *\[mserver2\]* managed servers to the *\[cluster\]* cluster.
184. Click Next.

<span id="_Toc55375202" class="anchor"></span>Figure 22: Install WebLogic – Assign Servers to Clusters

![](psd-3-89-controlled-substance-dirb/043.png)

185. Click Add.
186. Enter *Name*: “*\[machine1\]*”
187. Enter *Node Manager Listen Address*: “*\[vm1_fqdn\]*”
188. Enter *Node Manager Listen Port*: “5556”
189. Enter *Name*: “*\[machine2\]*”
190. Enter *Node Manager Listen Address*: “*\[vm2_fqdn\]*”
191. Enter *Node Manager Listen Port*: “5556”
192. Click Next.

<span id="_Toc55375203" class="anchor"></span>Figure 23: Install WebLogic – Machines

![](psd-3-89-controlled-substance-dirb/044.png)

193. On the Assign Servers to Machines screen, add “AdminServer” on *Servers* panel to “*\[machine1\]*” on *Machines* panel.
194. Add “*\[mserver1\]*” on *Servers* panel to “*\[machine1\]*” on *Machines* panel.
195. Add “*\[mserver2\]*” on *Servers* panel to “*\[machine2\]*” on *Machines* panel.
196. Click Next.

<span id="_Toc55375204" class="anchor"></span>Figure 24: Install WebLogic – Assign Servers to Machines

![](psd-3-89-controlled-substance-dirb/045.png)

197. Click Next.

![](psd-3-89-controlled-substance-dirb/046.png)

198. Click Next.

![](psd-3-89-controlled-substance-dirb/047.png)

199. On the Configuration Summary screen, click Create to accept the options and start creating and configuring the new domain.

<span id="_Toc55375205" class="anchor"></span>Figure 25: Install WebLogic – Configuration Summary Screen

![](psd-3-89-controlled-substance-dirb/048.png)

200. Once the configuration is complete, click Next.
201. If the configuration is successful, the Configuration Success screen will display as illustrated in the figure below.
202. Click Finish.

<span id="_Toc55375206" class="anchor"></span>Figure 26: Install WebLogic - Configuration Success

![](psd-3-89-controlled-substance-dirb/049.png)

203. The Oracle WebLogic Server configuration should be complete at this time. To modify the configuration, re-run the configuration wizard:

\$ cd *\[ORACLE_BASE*\]/Oracle_Home/oracle_common/common/bin

\$ ./config.sh

204. Modify the configuration as needed.

#### Set Temporary Environment on VM1

On VM1, set temporary environment. Remember to amend the DOMAIN_HOME environment variable to match your domain:

\$ export ORACLE_BASE=/u01/oracle/Oracle_Home/

\$ export WLS_HOME=\$ORACLE_BASE/wlserver

\$ export DOMAIN_HOME=/u01/oracle/Oracle_Home/user_projects/domains/erxdomain1/

\$ export DOMAIN_HOME=\$ORACLE_BASE/user_projects/domains/*\[domain\]*

#### Create a Domain Boot Identity File on VM1

On VM1, create a boot identity file for the domain if it doesn’t exist:

\$ mkdir -p \$DOMAIN_HOME/servers/AdminServer/security

\$ cat \> \$DOMAIN_HOME/servers/AdminServer/security/boot.properties

username=weblogic

password=#########

\<ctrl\>d

#### Copy Identity/Trust Store Files on VM1

Copy the server identity key store to the WebLogic domain “security” directory on VM1:

\$ cp /u01/certificates/*\[proxy_fqdn\]*.jks \$DOMAIN_HOME/security/*\[proxy_fqdn\]*.jks

#### Configure nodemanager Identity/Trust Store on VM1

On VM1, edit nodemanager.properties to add identity/trust store configuration:

\$ cd \$DOMAIN_HOME/nodemanager

\$ cp nodemanager.properties nodemanager_orig.properties

\$ vi nodemanager.properties

Add the following lines at the end of the file:

KeyStores=CustomIdentityAndCustomTrust

CustomIdentityAlias=*\[proxy_fqdn\]*

CustomIdentityKeyStoreFileName=*\[DOMAIN_HOME\]*/security/*\[proxy_fqdn\]*.jks

CustomIdentityKeyStorePassPhrase=*\[keystore_passphrase\]*

CustomIdentityKeyStoreType=JKS

CustomIdentityPrivateKeyPassPhrase=*\[privatekey_passphrase\]*

Enter :wq to save the file and exit vi.

#### Configure TLS on VM1

On VM1, edit startManagedWeblogic.sh to modify TLS configuration:

\$ cd \$DOMAIN_HOME/bin

\$ cp startWebLogic.sh startWebLogic_orig.sh

\$ vi startWebLogic.sh

Modify the JAVA_OPTIONS as follows:

\[weblogic@ REDACTED bin\]\$ diff old.startWebLogic.sh startWebLogic.sh

110c110

\< JAVA_OPTIONS="\${SAVE_JAVA_OPTIONS}"

---

\> JAVA_OPTIONS="\${SAVE_JAVA_OPTIONS} -Dweblogic.security.SSL.minimumProtocolVersion=TLSv1.1"

\#JAVA_OPTIONS="\${SAVE_JAVA_OPTIONS}"

JAVA_OPTIONS="\${SAVE_JAVA_OPTIONS} -Dweblogic.security.SSL.minimumProtocolVersion=TLSv1.1”

Enter :wq to save the file and exit vi.

#### Copy Identity/Trust Store Files on VM2

VM2 has no domain yet

Copy the server identity key store to the WebLogic domain “security” directory on VM1:

\$ cp /u01/certificates/*\[proxy_fqdn\]*.jks \$DOMAIN_HOME/security/*\[proxy_fqdn\]*.jks

#### Configure nodemanager Identity/Trust Store on VM2

On VM1, edit nodemanager.properties to add identity/trust store configuration:

\$ cd \$DOMAIN_HOME/nodemanager

\$ cp nodemanager.properties nodemanager_orig.properties

\$ vi nodemanager.properties

Add the following lines at the end of the file:

KeyStores=CustomIdentityAndCustomTrust

CustomIdentityAlias=*\[proxy_fqdn\]*

CustomIdentityKeyStoreFileName=*\[DOMAIN_HOME\]*/security/*\[proxy_fqdn\]*.jks

CustomIdentityKeyStorePassPhrase=*\[keystore_passphrase\]*

CustomIdentityKeyStoreType=JKS

CustomIdentityPrivateKeyPassPhrase=*\[privatekey_passphrase\]*

Enter :wq to save the file and exit vi.ls -

#### Disable basic authentication on VM1

On VM1, edit config.xml to disable basic authentication:

\$ cd \$DOMAIN_HOME/config/config.xml

\$ cp config.xml config_orig.xml

\$ vi config.xml

Add the following line before the end tag \</security-configuration\>:

\<enforce-valid-basic-auth-credentials\>false\</enforce-valid-basic-auth-credentials\>

Enter :wq to save the file and exit vi.

#### Configure JPA for Domain on VM1

On VM1, edit setDomainEnv.sh script to add JPA modules via PRE_CLASSPATH:

\$ cd \$DOMAIN_HOME/bin

\$ cp setDomainEnv.sh setDomainEnv_orig.sh

\$ vi setDomainEnv.sh

Add the following two lines after the first line in the script:

PRE_CLASSPATH=”*\[ORACLE_BASE\]*/oracle_common/modules/javax.persistence.jar”

export PRE_CLASSPATH

Enter :wq to save the file and exit vi.

#### Create Startup/Shutdown Scripts on VM1

This section outlines the steps for creating startup/shutdown scripts:

1.  As your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

205. Create startup scripts with the following commands:

\$ cat \> startNodemanager\_*\[domain\]*.sh

tmp_domain_home="*\[DOMAIN_HOME\]*"

cp \${tmp_domain_home}/nodemanager/nodemanager.log \${tmp_domain_home}/nodemanager/nodemanager_old.log

cat /dev/null \> \${tmp_domain_home}/nodemanager/nodemanager.log

nohup \${tmp_domain_home}/bin/startNodeManager.sh 2\>&1\> \${tmp_domain_home}/nodemanager/nm.out &

\<ctrl\>d

\$ cat \> startWebLogic\_*\[domain\]*.sh

tmp_domain_home="*\[DOMAIN_HOME\]*"

cp \${tmp_domain_home}/servers/AdminServer/logs/AdminServer.log \${tmp_domain_home}/servers/AdminServer/logs/AdminServer_old.log

cat /dev/null \> \${tmp_domain_home}/servers/AdminServer/logs/AdminServer.log

nohup \${tmp_domain_home}/bin/startWebLogic.sh 2\>&1\> \${tmp_domain_home}/servers/AdminServer/logs/AdminServer.out &

\<ctrl\>d

\$ cat \> stopNodemanager\_*\[domain\]*.sh

tmp_domain_home="*\[DOMAIN_HOME\]*"

\${tmp_domain_home}/bin/stopNodeManager.sh

\<ctrl\>d

\$ cat \> stopWebLogic\_*\[domain\]*.sh

tmp_domain_home="*\[DOMAIN_HOME\]*"

\${tmp_domain_home}/bin/stopWebLogic.sh

\<ctrl\>d

#### Start up Weblogic Admin Console on VM1

This section outlines the steps for creating startup/shutdown scripts:

1.  As your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

206. On VM1, start node manager:

\$ ./startNodemanager\_*\[domain\]*.sh

207. On VM1, start AdminServer:

\## First time \##

\## make logs dir \##

\$ mkdir /u01/oracle/Oracle_Home/user_projects/domains/erxdomain1/servers/AdminServer/logs

\$ ./startWebLogic\_*\[domain\]*.sh

#### Log into Weblogic Admin Console on VM1

1.  Start a Web Browser from the Linux command prompt:

\$ /opt/google/chrome/chrome --window-size=1000,900 &

2.  Access the non-secure Weblogic Admin Console URL:

REDACTED

3.  Log into the Weblogic console with the Weblogic admin username and password:

    ![](psd-3-89-controlled-substance-dirb/050.png)
208. The WebLogic Admin Console Home Page :

     ![](psd-3-89-controlled-substance-dirb/051.png)

#### Create Inbound eRx Datasource

This section provides step-by-step instructions for deploying VistA Link Connector.

1.  Navigate to *Services \> Data Sources*.
2.  From the *Data Source*s page, click New.

<span id="_Toc55375207" class="anchor"></span>Figure 27: Create Inbound eRx Datasource – Datasources

![](psd-3-89-controlled-substance-dirb/052.png)

209. Enter *Name*: “InboundErxDataSource”
210. Enter *JNDI Name*: “jdbc/InboundErxDataSource”
211. Select *Database Type*: “Oracle”
212. Click Next.

<span id="_Toc55375208" class="anchor"></span>Figure 28: Create Inbound eRx Datasource – Datasource Properties

![](psd-3-89-controlled-substance-dirb/053.png)

213. Select *Database Driver*: “Oracle’s Driver (Thin XA) for Instance connections; Versions: Any”
214. Click Next.

<span id="_Toc55375209" class="anchor"></span>Figure 29: Create Inbound eRx Datasource – Database Driver

![](psd-3-89-controlled-substance-dirb/054.png)

215. Click Next.

<span id="_Toc55375210" class="anchor"></span>Figure 30: Create Inbound eRx Datasource – Transaction Properties

![](psd-3-89-controlled-substance-dirb/055.png)

216. Enter *Database Name*: “*\[DB_NAME\]*”
217. Enter *Host Name*: “*\[DB_FQDN\]*”
218. Enter *JNDI Name*: “jdbc/InboundErxDataSource”
219. Enter *Port*: “*\[DB_PORT\]*”
220. Enter *Password*: “*\[DB_PASSWORD\]*”
221. Enter *Confirm Password*: “*\[DB_PASSWORD\]*”

<span id="_Toc55375211" class="anchor"></span>Figure 31: Create Inbound eRx Datasource – Connection Properties

![](psd-3-89-controlled-substance-dirb/056.png)

222. Click the “Test Configuration” button
223. If test is not successful, Click “Back” button and correct settings, otherwise click “Next”

<span id="_Toc55375212" class="anchor"></span>Figure 32: Create Inbound eRx Datasource – Test Connection

![](psd-3-89-controlled-substance-dirb/057.png)

224. Select “All servers in the cluster”
225. Click “Finish” button.

<span id="_Toc55375213" class="anchor"></span>Figure 33: Create Inbound eRx Datasource – Select Targets/Finish

![](psd-3-89-controlled-substance-dirb/058.png)

226. Select “InboundErxDataSource” hyperlink

<span id="_Toc55375214" class="anchor"></span>Figure 34: Create Inbound eRx Datasource – Modify New Datasource

![](psd-3-89-controlled-substance-dirb/059.png)

227. Select “Connection Pool” tab

<span id="_Toc55375215" class="anchor"></span>Figure 35: Inbound eRx Datasource –Connection Pool Properties

![](psd-3-89-controlled-substance-dirb/060.png)

228. Scroll to the bottom of the “Connection Pool” page
229. Select “Advanced” hyperlink to expand the advanced properties

<span id="_Toc55375216" class="anchor"></span>Figure 36: Inbound eRx Datasource –Connection Pool Advanced Properties

![](psd-3-89-controlled-substance-dirb/061.png)

230. Scroll to the bottom of the of the “Advanced Connection Pool” page
231. Unckeck the “Wrap Data Types” property
232. Click the “Save” button

<span id="_Toc55375217" class="anchor"></span>Figure 37: Inbound eRx Datasource – Wrap Data Type Property

![](psd-3-89-controlled-substance-dirb/062.png)

#### Configure Identity/Trust Store File on Managed Servers

This section provides step-by-step instructions for configuring the identify/trust store file on the managed servers.

1.  Under Domain Structure, navigate to Environment \> Servers.
2.  Click on the “*\[mserver1\]*” link to access the server configuration page.

<span id="_Toc55375218" class="anchor"></span>Figure 38: Configure Identity/Trust Store File – Access Server Configuration Page

![](psd-3-89-controlled-substance-dirb/063.png)

233. Under Configuration \> Keystores, click Change.

<span id="_Toc55375219" class="anchor"></span>Figure 39: Configure Identity/Trust Store File – Change Keystores

![](psd-3-89-controlled-substance-dirb/064.png)

234. For *Keystores*, select “Custom Identity and Custom Trust”.
235. Click Save.

<span id="_Toc55375220" class="anchor"></span>Figure 40: Configure Identity/Trust Store File – Keystores – Select Custom Identify and Custom Trust

![](psd-3-89-controlled-substance-dirb/065.png)

236. Modify the setting under the Keystores tab as illustrated in the figure below. The *Custom Identity Keystore* and *Custom Trust Keystore* use the same file path to the keystore file copied to the Domain “security” directory: (*\[DOMAIN_HOME\]*/security/*\[proxy_fqdn\]*.jks).

<span id="_Toc55375221" class="anchor"></span>Figure 41: Configure Identity/Trust Store File – Modify Keystore Settings

![](psd-3-89-controlled-substance-dirb/066.png)

237. Modify the setting under the SSL tab as illustrated in the figure below. For the *Private Key Alias*, enter “*\[proxy_fqdn\]*”.
238. Enter and confirm the *Private Key Passphrase*.
239. Click Save.

<span id="_Toc55375222" class="anchor"></span>Figure 42: Configure Identity/Trust Store File – Modify SSL Settings

![](psd-3-89-controlled-substance-dirb/067.png)

240. Navigate to *Servers*, and then click on the “erx2” link to access the server configuration page in the Administration Console.
241. Repeat the Keystore configuration steps for “erx2” as described earlier in this section for “erx1”.

<span id="_Toc55375223" class="anchor"></span>Figure 43: Configure Identity/Trust Store File – Managed Server 2 Configuration

![](psd-3-89-controlled-substance-dirb/068.png)

242. Navigate to *Servers*, and then click on the “AdminServer(admin)” hyperlink to access the server configuration page.
243. Repeat the Keystore configuration steps for “AdminServer(admin)” as described earlier in this section for “erx1”.

<span id="_Toc55375224" class="anchor"></span>Figure 44: Configure Identity/Trust Store File – Admin Server Configuration

![](psd-3-89-controlled-substance-dirb/069.png)

244. Navigate to *Servers*, and then click on the “AdminServer(admin)” hyperlink to access the server configuration page.

<span id="_Toc55375225" class="anchor"></span>Figure 45: Configure Identity/Trust Store File – Admin Server Configuration

![](psd-3-89-controlled-substance-dirb/070.png)

245. Under “Configuration” \> “general” tabs:  
     Check “Listen Port Enabled”  
     Enter “Listen Port”: 7001  
     Check “SSL Port Enabled”  
     Enter “SSL Listen Port”: 7002  
     Click “Save” button.

<span id="_Toc55375226" class="anchor"></span>Figure 46: Configure Identity/Trust Store File – Admin Server Configuration

![](psd-3-89-controlled-substance-dirb/071.png)

#### Pack Domain on VM1

This section provides step-by-step instructions for packing the domain on VM1:

1.  On VM1, stop the newly created domain.
2.  In the session that is currently running “startWebLogic.sh”, enter \<CTRL\> C.
3.  The log messages should indicate that the Admin Server “was shut down”.
2.  It may seem odd that we are immediately stopping the new domain, but some of the configuration is not written to the file system until the AdminServer is started for the first time.
4.  We will transfer the relevant configuration using the pack and unpack utilities.
5.  On VM1, pack the domain configuration using the following commands. Remember to amend the DOMAIN_HOME environment variable and the -template_name parameter to match your domain.

\$ mkdir /u01/templates

\$ chmod 777 /u01/templates

\$ \$WLS_HOME/common/bin/pack.sh -managed=true -domain=\$DOMAIN_HOME -template=/u01/templates/erxdomain1_template.jar -template_name=*\[domain\]* -log=/u01/templates/*\[domain\]\_*template_pack.log

246. Copy the resulting jar file to VM2 under:

/u01/templates

#### Unpack Domain on VM2

On VM2, set temporary environment. Remember to amend the DOMAIN_HOME environment variable to match your domain:

export PATH=/u01/app/java/latest/bin/:/usr/local/bin:/bin:/usr/bin:/usr/local/sbin:/usr/sbin

export ORACLE_BASE=/u01/oracle/Oracle_Home/

export WLS_HOME=/u01/oracle/Oracle_Home/wlserver

export DOMAIN_HOME=/u01/oracle/Oracle_Home/user_projects/domains/erxdomain1

\$ export ORACLE_BASE=*\[ORACLE_BASE\]*

\$ export WLS_HOME=\$ORACLE_BASE/wlserver

\$ export DOMAIN_HOME=\$ORACLE_BASE/user_projects/domains/*\[domain\]*

Unpack the configuration on VM2. Remember to amend the DOMAIN_HOME environment variable to match your domain.

\$ \$WLS_HOME/common/bin/unpack.sh -domain=\$DOMAIN_HOME -template=/u01/templates/*\[domain\]*\_template.jar -log=/u01/templates/*\[domain\]\_*template_unpack.log

#### Copy Identity/Trust Store Files on VM2

Copy the server identity key store to the WebLogic domain “security” directory on VM2:

\$ cp /u01/certificates*/\[proxy_fqdn\]*.jks \$DOMAIN_HOME/security/*\[proxy_fqdn\]*.jks

#### Enroll VM2

1.  On VM1, restart the domain. Wait until it is fully started before continuing.

\$ nohup \$DOMAIN_HOME/bin/startWebLogic.sh 2\>&1\> \$DOMAIN_HOME/servers/AdminServer/logs/AdminServer.out &

247. On VM2, start WLST.

\$ \$WLS_HOME/common/bin/wlst.sh

248. Connect to the administration server on VM1, enroll VM2, disconnect and exit WLST. Remember to amend the DOMAIN_HOME environment variable to match your domain.

\> connect('weblogic', '########', 't3://*\[vm1_fqdn\]*:7001')

\> nmEnroll('*\[DOMAIN_HOME\]*', '*\[DOMAIN_HOME\]*/nodemanager')

\> disconnect()

\> exit()

249. Check the “\$ORACLE_BASE/domain-registry.xml” file contains an entry like the following. If it doesn't, add it manually.

\<domain location="*\[DOMAIN_HOME\]*"/\>

250. Check the “\$DOMAIN_HOME/nodemanager/nodemanager.domains” file contains an entry like the following. If it doesn't, add it manually.

erxdomain1=*\[DOMAIN_HOME\]*

251. If the node manager is not already started on this server, start it now.

\$ nohup \$DOMAIN_HOME/bin/startNodeManager.sh &

#### Check Node Manager on Each WebLogic Machine

This section outlines the steps for checking that the node manager is reachable on each WebLogic machine.

1.  Log in to the administration server (http://*\[vm1_fqdn\]*:7001/console).
252. In the *Domain Structure* tree, expand the *Environment* node and then click on the *Machines* node.
253. In the right-hand pane, click on the first WebLogic machine (machine1).
254. Select the Monitoring tab. Be patient. This may take some time the first time you do it.
255. If the status is “Reachable”, everything is fine.
256. Repeat for the second WebLogic machine (machine2).

#### Create a Boot Identity File for Managed Servers

3.  This is a placeholder step that may be eliminated if the boot identity file is automatically copied over during the domain clone process.

On VM1/2, create a boot identity file for the domain if it doesn’t exist:

\$ mkdir -p \$DOMAIN_HOME/servers/AdminServer/security

\$ cat \> \$DOMAIN_HOME/servers/AdminServer/security/boot.properties

username=weblogic

password=#########

\<ctrl\>d

4.  The above username and password will be encoded/encrypted after the first shutdown/startup cycle.

#### Deploy Test Application

This section outlines the steps for deploying the test application.

1.  Start the node manager on all servers.
2.  Create the deployments directory if it doesn’t exist:

\$ mkdir -p /u01/deployments

257. Copy test application to the deployments directory:

\$ cp /u01/downloads/benefits.war /u01/deployments

258. Navigate to the *Deployments* page.

<span id="_Toc55375227" class="anchor"></span>Figure 47: Deploy Test Application: Deployments Page

![](psd-3-89-controlled-substance-dirb/072.png)

259. From the *Deployments* page, click Install.

<span id="_Toc55375228" class="anchor"></span>Figure 48: Deploy Test Application – Install

![](psd-3-89-controlled-substance-dirb/073.png)

260. Install a new deployment of the test application using the WAR file as indicated in the figure below.
261. Click Next.

<span id="_Toc55375229" class="anchor"></span>Figure 49: Deploy Test Application – WAR File

![](psd-3-89-controlled-substance-dirb/074.png)

262. Accept the defaults for an application deployment. (The *Install this deployment as an application radio butto*n is marked.)
263. Click Next.

<span id="_Toc55375230" class="anchor"></span>Figure 50: Deploy Test Application – Accept Default Application Deployment

![](psd-3-89-controlled-substance-dirb/075.png)

264. Select the *All servers in the cluster* option under the “erx” cluster as the target for the deployment.
265. Click Next.

<span id="_Toc55375231" class="anchor"></span>Figure 51: Deploy Test Application – Select Deployment Target

![](psd-3-89-controlled-substance-dirb/076.png)

266. All of the values should appear as illustrated in the figure below.
267. Click Next.

<span id="_Toc55375232" class="anchor"></span>Figure 52: Deploy Test Application – Verify Deployment Settings

![](psd-3-89-controlled-substance-dirb/077.png)

268. Verify that all of the values appear as illustrated in the figure below.
269. Click Finish.

<span id="_Toc55375233" class="anchor"></span>Figure 53: Deploy Test Application – Verify Deployment Settings (Finish)

![](psd-3-89-controlled-substance-dirb/078.png)

270. The Overview tab should appear as illustrated in the figure below.

<span id="_Toc55375234" class="anchor"></span>Figure 54: Deploy Test Application – Verify “benefits” Settings

![](psd-3-89-controlled-substance-dirb/079.png)

271. Navigate to the Servers page in the WebLogic console.
272. Select the Control tab.
273. Select “erx1” and “erx2” servers.
274. Click Start.

<span id="_Toc55375235" class="anchor"></span>Figure 55: Deploy Test Application – Summary of Servers Table

![](psd-3-89-controlled-substance-dirb/080.png)

275. After a couple minutes, the state on the servers will change to “RUNNING”.

<span id="_Toc55375236" class="anchor"></span>Figure 56: Deploy Test Application – Servers Running

![](psd-3-89-controlled-substance-dirb/081.png)

276. Open a web browser to http://*\[vm1_fqdn\]*/benefits/.
277. The Dizzyworld Benefits application will display.

<span id="_Toc55375237" class="anchor"></span>Figure 57: Deploy Test Application – Open Dizzyworld Benefits Application

![](psd-3-89-controlled-substance-dirb/082.png)

278. Repeat Steps 22 and 23 with a Web browser pointed to http://*\[vm2_fqdn\]*/benefits/.
279. Repeat Steps 22 and 23 with a Web browser pointed to https://*\[proxy_fqdn\]*/benefits/.
280. Navigate to the Servers page in the WebLogic console.
281. Select the Control tab.
282. Select “erx1” and “erx2” servers.
283. Click Shutdown.

<span id="_Toc55375238" class="anchor"></span>Figure 58: Deploy Test Application – Shutdown Servers

![](psd-3-89-controlled-substance-dirb/083.png)

#### Configure JPA for Domain on VM2

On VM2, edit setDomainEnv.sh script to add JPA modules via PRE_CLASSPATH:

\$ cd \$DOMAIN_HOME/bin

\$ cp setDomainEnv.sh setDomainEnv_orig.sh

\$ vi setDomainEnv.sh

Add the following two lines after the first line in the script:

PRE_CLASSPATH=*\[ORACLE_BASE\]*/oracle_common/modules/javax.persistence_2.1.jar:*\[WLS_HOME\]*/modules/com.oracle.weblogic.jpa21support_1.0.0.0_2-1.jar

export PRE_CLASSPATH

Enter :wq to save the file and exit vi.

#### Install VistALink on VM1 and VM2

This section outlines the steps for installing VistALink.

1.  As your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

284. Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

285. Download vljConnector-1.5.0.028.jar, vljFoundationsLib-1.6.0.28.jar, log4j-1.2.17.jar to the downloads directory:

Download from AITC IEP eRx Downloads directory

286. Create configureVistalink.sh

\$ cd \$DOMAIN_HOME

\$ cat \> bin/configureVistaLink.sh

\#!/bin/sh

\# ------------ VistaLink Edits --------------

USERSTAGING=\${DOMAIN_HOME}/vistalink

export USERSTAGING

echo "."

echo "User Staging Area: \${USERSTAGING}"

echo "."

\# Vistalink Classpath...

VLJCLASSPATH=\${USERSTAGING}/resource_adapters

export VLJCLASSPATH

echo "Vistalink Staging Area: \$VLJCLASSPATH"

CLASSPATH=\${CLASSPATH}\${CLASSPATHSEP}\${USERSTAGING}

export CLASSPATH

CLASSPATH=\${CLASSPATH}\${CLASSPATHSEP}\${VLJCLASSPATH}

export CLASSPATH

\# ------------ End VistaLink Edits --------------

\<CTRL D\>

\$chmod 755 bin/configureVistaLink.sh

287. Modify configureVistaLink.sh (Production environment only):

\$ vi \$DOMAIN_HOME/bin/configureVistaLink.sh

Add the following line to the bottom of the file:

export JAVA_OPTIONS="\${JAVA_OPTIONS} -Dgov.va.med.environment.production=true"

288. Modify the Domain Startup script (startWebLogic.sh):

\$ vi \$DOMAIN_HOME/bin/startWeblogic.sh

Modify JAVA_OPTIONS section, line numbers approximate, as shown:

\[line 114\] JAVA_OPTIONS="\${SAVE_JAVA_OPTIONS} -Dweblogic.security.SSL.minimumProtocolVersion=TLSv1.1"

Add call to configureVistalink.sh after the setDomainEnv.sh call as shown:

\[line 93\] . \${DOMAIN_HOME}/bin/setDomainEnv.sh \$\*

\[line 94\] . \${DOMAIN_HOME}/bin/configureVistaLink.sh \$\*

289. Modify the nodemanager.properties file:

\$ cat -n \$DOMAIN_HOME/nodemanager/nodemanager.properties

Ensure StartScriptEnabled=true:

25 weblogic.StartScriptEnabled=true<span class="mark">  
</span>

#### Configure VistALink on VM1 and VM2

1.  Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

290. Download the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh) to the downloads directory.
291. As your normal Linux login account, dzdo execute the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh) (the following must be performed by a system administrator):

\$ dzdo /u01/downloads/erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh

292. Select option 3, 4 and 5 then Exit (x).

#### Stop and start Node Manager and Domain on VM1, VM2

This section outlines the steps for starting the node manager on the first WebLogic machine:

1.  Stop the new domain on the VM1.

\$ \$DOMAIN_HOME/bin/stopWebLogic.sh

293. On VM1 stop the node manager.

\$ \$DOMAIN_HOME/bin/stopNodeManager.sh

294. On VM1, start the node manager.

\$ DOMAIN_HOME/bin/stopNodeManager.sh

295. On VM2 stop the node manager.

\$ \$DOMAIN_HOME/bin/stopNodeManager.sh

296. On VM2, start the node manager.

\$ DOMAIN_HOME/bin/stopNodeManager.sh

297. Start the domain on VM1.

\$ \$DOMAIN_HOME/bin/startWebLogic.sh

298. Wait for the “RUNNING” state before proceeding.

#### Deploy VistALink Libraries

This section provides step-by-step instructions for deploying VistA Link Connector:

1.  Navigate to the *Deployments* page.
1.  From the *Deployment*s screen, click Install.

<span id="_Toc55375239" class="anchor"></span>Figure 59: Deploy VistA Link Libraries – Deployments

![](psd-3-89-controlled-substance-dirb/084.png)

<span class="mark">  
</span>

299. Enter *Path*: “/u01/downloads”
300. Install a new deployment of “log4j-1.2.17.jar” by selecting the jar file as indicated, and then click Next.

<span id="_Toc55375240" class="anchor"></span>Figure 60: Deploy VistA Link Libraries – Select log4j Library to deploy

![](psd-3-89-controlled-substance-dirb/085.png)

301. Select *All servers in the cluster* as the target for the deployment, and then click Next.

<span id="_Toc55375241" class="anchor"></span>Figure 61: Deploy VistA Link Libraries – Select Deployment Targets

![](psd-3-89-controlled-substance-dirb/086.png)

302. All of the values should appear as illustrated in the figure below.
303. Click Next.

<span id="_Toc55375242" class="anchor"></span>Figure 62: Deploy VistA Link Libraries – Summary of Deployments Verification 1

![](psd-3-89-controlled-substance-dirb/087.png)

<span class="mark">  
</span>

304. Verify that all of the values appear as illustrated in the figure below.
305. Click Finish.

<span id="_Toc55375243" class="anchor"></span>Figure 63: Deploy VistA Link Libraries – Summary of Deployments Verification 2

![](psd-3-89-controlled-substance-dirb/088.png)

<span class="mark">  
</span>

306. The Deployment Configuration screen should appear as illustrated in the below figure.
307. Enter *Deployment Order*: “1”.
308. Click Save.

<span id="_Toc55375244" class="anchor"></span>Figure 64: Deploy VistA Link Libraries – Deployment Configuration Screen

![](psd-3-89-controlled-substance-dirb/089.png)

<span class="mark">  
</span>

309. Navigate to the *Deployments* page.
310. From the *Deployment*s screen, click Install.

<span id="_Toc55375245" class="anchor"></span>Figure 65: Deploy VistA Link Libraries – Deployments

![](psd-3-89-controlled-substance-dirb/090.png)

<span class="mark">  
</span>

311. Enter *Path*: “/u01/downloads”
312. Install a new deployment of “vljConnector-1.6.0.028.jar” by selecting the jar file as indicated, and then click Next.

<span id="_Toc55375246" class="anchor"></span>Figure 66: Deploy VistA Link Libraries – Select vljConnector-1.6.0.028.jar Library to deploy

![](psd-3-89-controlled-substance-dirb/091.png)

313. Select *All servers in the cluster* as the target for the deployment, and then click Next.

<span id="_Toc55375247" class="anchor"></span>Figure 67: Deploy VistA Link Libraries – Select Deployment Targets

![](psd-3-89-controlled-substance-dirb/092.png)

314. All of the values should appear as illustrated in the figure below.
315. Click Next.

<span id="_Toc55375248" class="anchor"></span>Figure 68: Deploy VistA Link Libraries – Summary of Deployments Verification 1

![](psd-3-89-controlled-substance-dirb/093.png)

316. Verify that all of the values appear as illustrated in the figure below.
317. Click Finish.

<span id="_Toc55375249" class="anchor"></span>Figure 69: Deploy VistA Link Libraries – Summary of Deployments Verification 2

![](psd-3-89-controlled-substance-dirb/094.png)

318. The Deployment Configuration screen should appear as illustrated in the below figure.
319. Enter *Deployment Order*: “1”.
320. Click Save.

<span id="_Toc55375250" class="anchor"></span>Figure 70: Deploy VistA Link Libraries – Deployment Configuration Screen

![](psd-3-89-controlled-substance-dirb/095.png)

321. Navigate to the *Deployments* page.
322. From the *Deployment*s screen, click Install.

<span id="_Toc55375251" class="anchor"></span>Figure 71: Deploy VistA Link Libraries – Deployments

![](psd-3-89-controlled-substance-dirb/096.png)

323. Enter *Path*: “/u01/downloads”
324. Install a new deployment of “log4j-1.2.17.jar” by selecting the jar file as indicated, and then click Next.

     <span id="_Hlk65482200" class="anchor"></span>

Figure 72: Deploy VistA Link Libraries – Select log4j Library to deploy

![](psd-3-89-controlled-substance-dirb/097.png)

325. Select *All servers in the cluster* as the target for the deployment, and then click Next.

<span id="_Toc55375253" class="anchor"></span>Figure 73: Deploy VistA Link Libraries – Select Deployment Targets

![](psd-3-89-controlled-substance-dirb/098.png)

326. All of the values should appear as illustrated in the figure below.
327. Click Next.

<span id="_Toc55375254" class="anchor"></span>Figure 74: Deploy VistA Link Libraries – Summary of Deployments Verification 1

![](psd-3-89-controlled-substance-dirb/099.png)

328. Verify that all of the values appear as illustrated in the figure below.
329. Click Finish.

<span id="_Toc55375255" class="anchor"></span>Figure 75: Deploy VistA Link Libraries – Summary of Deployments Verification 2

![](psd-3-89-controlled-substance-dirb/100.png)

330. The Deployment Configuration screen should appear as illustrated in the below figure.
331. Enter *Deployment Order*: “1”.
332. Click Save.

<span id="_Toc55375256" class="anchor"></span>Figure 76: Deploy VistA Link Libraries – Deployment Configuration Screen

![](psd-3-89-controlled-substance-dirb/101.png)

#### Deploy VistALink Adapters

This section provides step-by-step instructions for deploying VistA Link Adapter.

1.  Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

333. Download the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh) to the downloads directory.
334. As your normal Linux login account, dzdo execute the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh) (the following must be performed by a system administrator):

\$ dzdo /u01/downloads/erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh

335. Select option 3 and 5 then Exit (x).
1.  The WebLogic Administrator stops the VM1 managed server, per section: Error! Reference source not found., step Error! Reference source not found.
3.  The System Administrator executes the eRx/IEP Configurator script containing adapter configuration on VM1, menu options 1, 2 and 3.
4.  The WebLogic Administrator will start the VM1 managed server, per section 7.1.2.
5.  The WebLogic Administrator stops the VM2 managed server, per section: Error! Reference source not found., step Error! Reference source not found.
6.  The System Administrator executes the eRx/IEP Configurator script containing adapter configuration on VM2, menu options 1, 2 and 3.
7.  The WebLogic Administrator will start the VM2 managed server, per section 7.1.2.
8.  The WebLogic navigates to the *Deployment*s screen, click Install.

<span id="_Toc55375264" class="anchor"></span>Figure 77: Deploy VistALink Adapter – Deployments

![](psd-3-89-controlled-substance-dirb/102.png)

1.  Enter *Path*: “*\[DOMAIN_HOME\]*/vistalink/resource_adapters”, press enter.
336. Select the desired vljXXX_adapter to be installed, and then click Next.

<span id="_Toc10727581" class="anchor"></span>Figure : Deploy VistALink Adapter – Select vljxxx_apapter to install

![](psd-3-89-controlled-substance-dirb/103.png)

337. Select *Install this deployment as an application* as the target for the deployment, and then click Next.

<span id="_Toc10727582" class="anchor"></span>Figure : Deploy VistALink Adapter – Select Deployment Type

![](psd-3-89-controlled-substance-dirb/104.png)

338. Select *All servers in the cluster* as the target for the deployment, and then click Next.

<span id="_Toc10727583" class="anchor"></span>Figure : Deploy VistALink Adapter – Select Deployment Targets

![](psd-3-89-controlled-substance-dirb/105.png)

339. All of the values should appear as illustrated in the figure below.
340. Click Next.

<span id="_Toc10727584" class="anchor"></span>Figure : Deploy VistALink Adapter – Adapter Optional Settings

![](psd-3-89-controlled-substance-dirb/106.png)

341. Verify that all of the values appear as illustrated in the figure below.
342. Click Finish.

<span id="_Toc10727585" class="anchor"></span>Figure : Deploy VistALink Adapter – Finish Adapter Installation

![](psd-3-89-controlled-substance-dirb/107.png)

343. Navigate to Deployments, select the vljXXX_adapter, click Start \> Servicing all Requests.

<span id="_Toc10727586" class="anchor"></span>Figure : Deploy VistALink Adapter – Start Resource Adapter

![](psd-3-89-controlled-substance-dirb/108.png)

### Inbound eRx Application Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the steps to install and configure the Inbound eRx application. Most activities are to be performed by the WebLogic Administrator.

#### Install Inbound eRx Application

1.  Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

344. Download the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_deploy_yyyymmdd \_hhmmss.sh) to the downloads directory.
345. As your normal Linux login account, dzdo execute the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_deploy_yyyymmdd \_hhmmss.sh) (the following must be performed by a system administrator):

\$ dzdo /u01/downloads/erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh

346. Select option 3, 5 and 6 then Exit (x).
347. Shut down WebLogic (refer to Sections 4.8.3.3 and 4.8.3.4).
348. As your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

349. Create the downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

350. Download Inbound eRx application to the downloads directory.

Download from AITC IEP eRx Downloads directory

351. Create the deployments directory if it doesn’t exist:

\$ mkdir -p /u01/deployments

352. Copy the application EAR to the deployments directory:

Download from AITC IEP eRx Downloads directory

353. Access the WebLogic Admin Console by directing a browser to: https://*\[vm1_fqdn\]*:7002/console/ and log in with the “weblogic” account.
354. Navigate to the Servers page.
355. From the Administration Console \> Servers page, click the “erx1” link to configure the server.

<span id="_Toc55375271" class="anchor"></span>Figure 84: Install Inbound eRx Application – Configure Servers

![](psd-3-89-controlled-substance-dirb/109.png)

356. The server configuration screen should appear as shown in the figure below.
357. Inspect the settings under the General tab. The *Listen Address* should be *\[vm1_fqdn\]*. The non-secure listening port (*Listen Port Enabled*) should be enabled and set to port “8001” (*Listen Port*). The secure listening port should be disabled (*SSL Listen Port Enabled*). These ports need to be consistent with the Apache Load Balancer/Proxy and local firewall settings.

<span id="_Toc55375272" class="anchor"></span>Figure 85: Install Inbound eRx Application – Verify Server Settings

![](psd-3-89-controlled-substance-dirb/110.png)

358. Review the setting under the Keystores tab as illustrated in the figure below. Verify the *Keystores* option is set to “Custom Identity and Custom Trust”, and that the fields under the *Identity* and *Trust* sections are filled with the same corresponding values.

<span id="_Toc55375273" class="anchor"></span>Figure 86: Install Inbound eRx Application – Verify General & Keystore Settings

![](psd-3-89-controlled-substance-dirb/111.png)

359. Verify the settings under the SSL tab. The *Private Key Alias* should be the Fully Qualified Domain Name of the server, and the *Passphrase* is \########.

<span id="_Toc55375274" class="anchor"></span>Figure 87: Install Inbound eRx Application – Verify SSL Settings

![](psd-3-89-controlled-substance-dirb/112.png)

360. Repeat the previous three steps for the “erx2” managed server to verify the *General Configuration*, *Keystores,* and *SSL* settings.
361. Navigate to the Deployments page.
362. From the Deployments page, click Install.

<span id="_Toc55375275" class="anchor"></span>Figure 88: Install Inbound eRx Application – Summary of Deployments

![](psd-3-89-controlled-substance-dirb/113.png)

363. Install a new deployment of INB\_ ERX-3.1.0.005.ear using the WAR file as indicated in the figure below.
364. Click Next.

<span id="_Toc55375276" class="anchor"></span>Figure 89: Install Inbound eRx Application – Install New Deployment of INB_ERX

![](psd-3-89-controlled-substance-dirb/114.png)

365. Accept the defaults for an application deployment.
366. Click Next.
367. Select the cluster and “All servers in the cluster” as the target for the deployment.
368. Click Next.

<span id="_Toc55375277" class="anchor"></span>Figure 90: Install Inbound eRx Application – Select INB_ERX Deployment Targets

![](psd-3-89-controlled-substance-dirb/115.png)

369. All of the values should appear as illustrated in the figure below.
370. Click Next.

<span id="_Toc55375278" class="anchor"></span>Figure 91: Install Inbound eRx Application – Verify INB_ERX Deployment Settings

![](psd-3-89-controlled-substance-dirb/116.png)

![](psd-3-89-controlled-substance-dirb/117.png)

371. All of the values should appear as illustrated in the figure below.
372. Click Finish.

<span id="_Toc55375279" class="anchor"></span>Figure 92: Install Inbound eRx Application – Verify INB_ERX Deployment Settings (Finish)

![](psd-3-89-controlled-substance-dirb/118.png)

373. The Overview tab should appear as illustrated in the figure below.

<span id="_Toc55375280" class="anchor"></span>Figure 93: Install Inbound eRx Application – Verify INB_ERX Deployment Configuration Settings

![](psd-3-89-controlled-substance-dirb/119.png)

374. Navigate to the Deployments page.
375. From the Deployments page, click Install.
376. Install a new deployment of INB_ERX_UI-4.0.5.012.ear, select the appropriate EAR file.
377. Click Next.

<span id="_Toc55375281" class="anchor"></span>Figure 94: Install Inbound eRx Application – Install New Deployment of INB_ERX_UI

![](psd-3-89-controlled-substance-dirb/120.png)

378. Accept the defaults for an application deployment.
379. Click Next.
380. Select the cluster and “All servers in the cluster” as the target for the deployment.
381. Click Next.

<span id="_Toc55375282" class="anchor"></span>Figure 95: Install Inbound eRx Application – Select INB_ERX_UI Deployment Targets

![](psd-3-89-controlled-substance-dirb/121.png)

382. All of the values should appear as illustrated in the figure below.
383. Click Next.

<span id="_Toc55375283" class="anchor"></span>Figure 96: Install Inbound eRx Application – Verify INB_ERX_UI Deployment Settings

![](psd-3-89-controlled-substance-dirb/122.png)

384. All of the values should appear as illustrated in the figure below.
385. Click Finish.

<span id="_Toc55375284" class="anchor"></span>Figure 97: Install Inbound eRx Application – Verify INB_ERX_UI Deployment Settings (Finish)

![](psd-3-89-controlled-substance-dirb/123.png)

386. The Overview tab should appear as illustrated in the figure below.

<span id="_Toc55375285" class="anchor"></span>Figure 98: Install Inbound eRx Application – Verify INB_ERX_UI Deployment Configuration Settings

![](psd-3-89-controlled-substance-dirb/124.png)

387. Navigate to the Servers page in the WebLogic console.
388. Select the Control tab.
389. Select “erx1” and “erx2”, and then click Start.

<span id="_Toc55375286" class="anchor"></span>Figure 99: Install Inbound eRx Application – Start erx Servers

![](psd-3-89-controlled-substance-dirb/125.png)

<span id="_Toc55375287" class="anchor"></span>Figure 100: Install Inbound eRx Application – erx Servers Running

![](psd-3-89-controlled-substance-dirb/126.png)

#### Create Startup/Shutdown Scripts

This section outlines the steps for creating startup/shutdown scripts:

2.  As your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

390. Create startup scripts with the following commands:

\$ cat \> startNodemanager\_*\[domain\]*.sh

tmp_domain_home="*\[DOMAIN_HOME\]*"

cp \${tmp_domain_home}/nodemanager/nodemanager.log \${tmp_domain_home}/nodemanager/nodemanager_old.log

cat /dev/null \> \${tmp_domain_home}/nodemanager/nodemanager.log

nohup \${tmp_domain_home}/bin/startNodeManager.sh 2\>&1\> \${tmp_domain_home}/nodemanager/nm.out &

\<ctrl\>d

\$ cat \> startWebLogic\_*\[domain\]*.sh

tmp_domain_home="*\[DOMAIN_HOME\]*"

cp \${tmp_domain_home}/servers/AdminServer/logs/AdminServer.log \${tmp_domain_home}/servers/AdminServer/logs/AdminServer_old.log

cat /dev/null \> \${tmp_domain_home}/servers/AdminServer/logs/AdminServer.log

nohup \${tmp_domain_home}/bin/startWebLogic.sh 2\>&1\> \${tmp_domain_home}/servers/AdminServer/logs/AdminServer.out &

\<ctrl\>d

\$ cat \> stopNodemanager\_*\[domain\]*.sh

tmp_domain_home="*\[DOMAIN_HOME\]*"

\${tmp_domain_home}/bin/stopNodeManager.sh

\<ctrl\>d

\$ cat \> stopWebLogic\_*\[domain\]*.sh

tmp_domain_home="*\[DOMAIN_HOME\]*"

\${tmp_domain_home}/bin/stopWebLogic.sh

\<ctrl\>d

#### Shut Down Domain

The section provides the steps for shutting down the domain:

1.  On VM1, as your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

391. Shut down the Administration Console with the following command:

\$ ./stopWebLogic\_*\[domain\]*.sh

#### Shut Down Nodemanagers

This sections outlines the steps for shutting down the nodemanagers:

1.  On VM1, as your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

392. Shut down Nodemanager with the following command:

\$ ./stopNodemanager\_*\[domain\]*.sh

393. On VM2, as your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

394. Shut down Nodemanager with the following command:

\$ ./stopNodemanager\_*\[domain\]*.sh

### Pentaho Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the steps to install the WebLogic application server. Most activities are to be performed by the WebLogic Administrator.

#### Pentaho Software Installation on VM1 and VM2

Perform the following steps on both VM1 and VM2:

1.  Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

395. Download Pentaho Data Integration Community Edition 8.2 archive (pdi-ce-8.2.0.0-342.zip) to the downloads directory.

Download from AITC IEP eRx Downloads directory

396. Download the eRx/IEP Installer (erx_iep\_ x.x.x.xxx_install_yyyymmdd \_hhmmss.sh) to the downloads directory.
397. As your normal Linux login account, execute the eRx/IEP Installerr (erx_iep\_ x.x.x.xxx_install_yyyymmdd \_hhmmss.sh) exist (the following must be performed by a system administrator):

\$ dzdo /u01/downloads/erx_iep\_ x.x.x.xxx_install_yyyymmdd \_hhmmss.sh

398. Select option 18, then Exit (x).
399. Download the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh) to the downloads directory.
400. As your normal Linux login account, execute the eRx/IEP Configurator (erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh) exist (the following must be performed by a system administrator):

\$ dzdo /u01/downloads/erx_iep\_ x.x.x.xxx_configur_yyyymmdd \_hhmmss.sh

401. Select option 4, then Exit (x).

#### Pentaho Repository Definition Import on VM1

The section provides step-by-step guidance to import the Pentaho repository:

1.  Create downloads directory if it doesn’t exist (the following must be performed by a system administrator):

\$ dzdo mkdir -p /u01/downloads

\$ dzdo chown weblogic:weblogic /u01/downloads

\$ dzdo chmod 777 /u01/downloads

402. Download the eRx/IEP Deployer (erx_iep\_ x.x.x.xxx_deploy_yyyymmdd \_hhmmss.sh) to the downloads directory.
403. As your normal Linux login account, execute the eRx/IEP Installerr (erx_iep\_ x.x.x.xxx_deploy_yyyymmdd \_hhmmss.sh) exist (the following must be performed by a system administrator):

\$ dzdo /u01/downloads/erx_iep\_ x.x.x.xxx_deploy_yyyymmdd \_hhmmss.sh

404. Select options 6 and 7, then Exit (x).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the installation steps in the previous sections, which outline the installation verification procedures within each step.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to the Inbound eRx project.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section will be added in future versions of this document.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the back-out procedure for Inbound eRx. Back-out pertains to a return to the last know, good operational state of the software and appropriate platform settings.

The Inbound eRx system will provide data protection measures, such as back-up intervals and redundancy that is consistent with systems categorized as mission critical (12 hour restoration, 2 hour recover point objective). This section outlines the backout strategy, considerations, testing, criteria for backout, risks, authority to approve and the procedures to perform a backout for Inbound eRx.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out strategy will follow VA guidelines and best practices as referenced in the Enterprise Operations (EO) National Data Center Hosting Services document.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to the Inbound eRx CS project.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The results of User Acceptance Testing (UAT) will be added to this document in a future version, following the completion of UAT.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out criteria will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known risks related to a back-out.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The POCs with the authority to order the back-out is the Inbound eRx IPT, the VA PM, and other relevant stakeholders, where applicable.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the backout procedure for Inbound ePrescribing application

### Back-Out of Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the steps for backing out Database changes on local database server. These steps should be performed under strict guidance of the PRE Inbound eRx PM team.

1.  Restore backup files from tape

Recover data per procedures in the EO National Data Center Hosting Services document.

2.  Mount the instance
1.  Set ORACLE_SID=IEPP
405. rman TARGET SYS/Password NOCATALOG
406. RMAN:\> shutdown immediate;  
     RMAN:\> startup mount;
     1.  Restore and recover the datafiles
1.  RMAN\> run  
    {  
    allocate channel dev1 type disk;  
    set until time "to_date('2011-12-30:00:00:00', 'yyyy-mm-dd:hh24:mi:ss')";  
    restore database;  
    recover database; }
    1.  Open the database and reset logs
1.  RMAN\> alter database open resetlogs;

### Back-Out of WebLogic 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the steps for backing out a new version of the PRE Inbound eRx application deployed on a local WebLogic (application) server. This is a two-step process: first, remove the new release, and then deploy the rolled-back release. These steps should be performed under strict guidance of the PRE Inbound eRx PM team.

1.  Remove New Release
1.  Open and log into the WebLogic console. Use WebLogic username and password.
407. Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node.
408. Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit.
409. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed.
410. Select the previously deployed Inbound eRx deployment, click Stop, and then select “Force Stop Now” from the drop-down list box.
411. WebLogic will now display the panel Force Stop Application Assistant in the right column of the console for confirmation to start servicing requests.
412. Click Yes in the Force Stop Application Assistant panel in the right column of the WebLogic console.
413. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
414. Verify that the State of the Inbound eRx deployment is “Prepared”.
415. Select the previously deployed Inbound eRx deployment, and then click Delete.
416. WebLogic will now display the panel Delete Application Assistant in the right column of the console for confirmation to start servicing requests.
417. Click Yes in the Delete Application Assistant panel in the right column of the WebLogic console.
418. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
419. Verify that the Inbound eRx deployment is deleted and no longer present.
     1.  Deploy Back-out Release

The following steps detail the deployment of the rolled-back Inbound eRx application.

1.  Use the WebLogic console that was started at the beginning of the roll-back process.
420. Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node.
421. Verify that application is in Lock & Edit mode. Lock & Edit mode is indicated by the “greyed-out” Lock & Edit selection button.
422. Click the Install button in the Deployments panel in the right column of the WebLogic console.
423. WebLogic will now display the panel Install Application Assistant in the right column of the console, where the location of the Inbound eRx deployment will be found.
1.  If the rolled-back Inbound eRx deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the Location panel within the Install Application Assistant in the right column of the console. Choose the ear file associated with the rolled-back release.
2.  If the rolled-back Inbound eRx deployment has not been transferred to the Deployment Machine:
    1.  Click on the upload your file(s) link in the Install Application Assistant panel in the right section of the console.
    2.  Click the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
    3.  Click Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the Locate deployment to install and prepare for deployment panel within the Install Application Assistant.
424. Once the rolled-back Inbound eRx deployment is located and selected, click Next.
425. WebLogic will now display the panel Choose targeting style within the Install Application Assistant in the right column of the console. Leave the default value selected, install this deployment as an application, and click Next.
426. Within the Install Application Assistant in the right column of the console, WebLogic will now display the panel Select deployment targets, where the Deployment Server will be selected as the target in the next step.
427. For the Target, select the Deployment Server.
428. Click Next.
429. Within the Install Application Assistant, WebLogic will now display the panel Optional Settings in the right column of the console, where the name of the deployment and the copy behavior are chosen.
430. Enter the Name for the deployment. Use: : INB_ERX-4.0.5.012
431. Verify that the following default option for Security is selected:

> DD Only: Use only roles and policies that are defined in the deployment descriptors.

432. Verify that the following default option for Source accessibility is selected:

> Use the defaults defined by the deployment's targets.

433. Click Next.
434. Within the Install Application Assistant, in the right column of the console WebLogic, will now display the panel Review your choices and click Finish, which summarizes the steps completed above.
435. Verify that the values match those entered in Steps 6 through 17 and click Finish.
436. WebLogic will now display the panel Settings for Inbound eRx, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
437. Leave all the values as defaulted by WebLogic and click Save.
438. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes.
439. Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node.
440. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed.
441. Select the previously deployed INB_ERX-4.0.5.012 deployment, click Start, and then select Servicing all requests from the drop-down list box.
442. WebLogic will now display the panel Start Application Assistant in the right column of the console for confirmation to start servicing requests.
443. Click Yes in the Start Application Assistant panel in the right column of the WebLogic console.
444. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
445. Verify that the State of the INB_ERX-4.0.5.012 deployment is “Active”.

## Back-out VistA Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will be done only with the concurrence and participation of development team and appropriate VA site/region personnel. The decision to back-out or rollback software will be a joint decision between development team, VA site/region personnel and other appropriate VA personnel.

Prior to installing an updated KIDS package, the site/region should have saved a backup of the routines in a mail message using the Backup a Transport Global \[XPD BACKUP\] menu option (this is done at time of install). The message containing the backed-up routines can be loaded with the "Xtract PackMan" function at the Message Action prompt. The Packman function "INSTALL/CHECK MESSAGE" is then used to install the backed-up routines onto the VistA System.

The back-out plan is to restore the routines from the backup created.

No data was modified by this patch installation and, therefore, no rollback strategy is required.

Validation of Back-out Procedure:

The Back-out Procedure can be verified by printing the first 2 lines of the PSO Routines contained in this patch using the option First Line Routine Print \[XU FIRST LINE PRINT\]. Once the routines contained in the PSO\*7.0\*617 patch have been backed out, the second line of the Routines will no longer contain the designation of patch PSO\*7.0\*617 in the patch list section.

The Back-out Procedure can be verified by printing the first 2 lines of the PSO Routines contained in this patch using the option First Line Routine Print \[XU FIRST LINE PRINT\]. Once the routines contained in the PSD\*3.0\*89 patch have been backed out, the second line of the Routines will no longer contain the designation of patch PSD\*3.0\*89 in the patch list section.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Depending on the approach taken for the back-out the verification steps will differ. Please contact the Inbound eRx development/maintenance team for verification instructions.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the procedures for rolling back to a previous state of the data.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback considerations will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback criteria will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known risks related to a Rollback.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The POCs with the authority to order the Rollback is the Inbound eRx IPT, the VA PM, and other relevant stakeholders, where applicable.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Rollback of Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the steps for rollback of Database changes on local database server. These steps should be performed under strict guidance of the PRE Inbound eRx PM team.

1.  Restore backup files from tape

Recover data per procedures in the EO National Data Center Hosting Services document.

2.  Mount the instance
2.  Set ORACLE_SID=IEPP
446. rman TARGET SYS/Password NOCATALOG
447. RMAN:\> shutdown immediate;  
     RMAN:\> startup mount;
     1.  Restore and recover the datafiles
2.  RMAN\> run  
    {  
    allocate channel dev1 type disk;  
    set until time "to_date('2011-12-30:00:00:00', 'yyyy-mm-dd:hh24:mi:ss')";  
    restore database;  
    recover database; }
    1.  Open the database and reset logs
2.  RMAN\> alter database open resetlogs;

### Rollback WebLogic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the steps for rolling back to a previous version of the PRE Inbound eRx application deployed on a local WebLogic (application) server. This is a two-step process: first, remove the old release, and then deploy the rolled-back release. These steps should be performed under strict guidance of the PRE Inbound eRx PM team.

#### Remove New Release

1.  Open and log into the WebLogic console. This is located at: <span class="mark">REDACTED</span>. Use WebLogic username and password.
448. Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node.
449. Within the Change Center panel in the left column of the WebLogic console, click Lock & Edit.
450. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed.
451. Select the previously deployed Inbound eRx deployment, click Stop, and then select “Force Stop Now” from the drop-down list box.
452. WebLogic will now display the panel Force Stop Application Assistant in the right column of the console for confirmation to start servicing requests.
453. Click Yes in the Force Stop Application Assistant panel in the right column of the WebLogic console.
454. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
455. Verify that the State of the Inbound eRx deployment is “Prepared”.
456. Select the previously deployed Inbound eRx deployment, and then click Delete.
457. WebLogic will now display the panel Delete Application Assistant in the right column of the console for confirmation to start servicing requests.
458. Click Yes in the Delete Application Assistant panel in the right column of the WebLogic console.
459. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
460. Verify that the Inbound eRx deployment is deleted and no longer present.

#### Deploy Rolled-Back Release

The following steps detail the deployment of the rolled-back Inbound eRx application.

1.  Use the WebLogic console that was started at the beginning of the roll-back process.
461. Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node.
462. Verify that application is in Lock & Edit mode. Lock & Edit mode is indicated by the “greyed-out” Lock & Edit selection button.
463. Click the Install button in the Deployments panel in the right column of the WebLogic console.
464. WebLogic will now display the panel Install Application Assistant in the right column of the console, where the location of the Inbound eRx deployment will be found.
3.  If the rolled-back Inbound eRx deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the Location panel within the Install Application Assistant in the right column of the console. Choose the ear file associated with the rolled-back release.
4.  If the rolled-back Inbound eRx deployment has not been transferred to the Deployment Machine:
    1.  Click on the upload your file(s) link in the Install Application Assistant panel in the right section of the console.
    2.  Click the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
    3.  Click Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the Locate deployment to install and prepare for deployment panel within the Install Application Assistant.
465. Once the rolled-back Inbound eRx deployment is located and selected, click Next.
466. WebLogic will now display the panel Choose targeting style within the Install Application Assistant in the right column of the console. Leave the default value selected, install this deployment as an application, and click Next.
467. Within the Install Application Assistant in the right column of the console, WebLogic will now display the panel Select deployment targets, where the Deployment Server will be selected as the target in the next step.
468. For the Target, select the Deployment Server.
469. Click Next.
470. Within the Install Application Assistant, WebLogic will now display the panel Optional Settings in the right column of the console, where the name of the deployment and the copy behavior are chosen.
471. Enter the Name for the deployment. Use: : INB_ERX-4.0.5.012
472. Verify that the following default option for Security is selected:

DD Only: Use only roles and policies that are defined in the deployment descriptors.

473. Verify that the following default option for Source accessibility is selected:

Use the defaults defined by the deployment's targets.

474. Click Next.
475. Within the Install Application Assistant, in the right column of the console WebLogic, will now display the panel Review your choices and click Finish, which summarizes the steps completed above.
476. Verify that the values match those entered in Steps 6 through 17 and click Finish.
477. WebLogic will now display the panel Settings for Inbound eRx, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
478. Leave all the values as defaulted by WebLogic and click Save.
479. Within the Change Center panel in the left column of the WebLogic console, click Activate Changes.
480. Within the Domain Structure panel in the left column of the WebLogic console, click the Deployments node.
481. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed.
482. Select the previously deployed INB_ERX-4.0.5.012 deployment, click Start, and then select Servicing all requests from the drop-down list box.
483. WebLogic will now display the panel Start Application Assistant in the right column of the console for confirmation to start servicing requests.
484. Click Yes in the Start Application Assistant panel in the right column of the WebLogic console.
485. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
486. Verify that the State of the INB_ERX-4.0.5.012 deployment is “Active”.

### Rollback VistA Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the fact that the data involved with inbound eRx is prescription related, data dictionary changes and existing data will not be rolled back. The system should maintain the new fields and records. The back-out procedure will dictate the usage/view of the new data. Any new message type will still be available to the user, and will be impacted only by the back-out procedure. Message linking between NewRx message types and cancel/refill message types will be established. The rolling back of the data would sever this linkage, potentially causing major problems.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Validation of Roll Back Procedure

The user will be able to view the cancel and refill message types. All actions besides print will be locked so the user cannot take action on the record. This will create a view only scenario for cancel and refill message types.

# Operational Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines server startup and shutdown procedures.

## Startup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Start Weblogic Node Managers and Admin Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  At your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su - weblogic

487. On VM1, start node managers:

\$ ./startNodemanager\_*\[domain\]*.sh

488. On VM2, start node managers:

\$ ./startNodemanager\_*\[domain\]*.sh

489. On VM1, wait for node manager startups to complete:

\$ tail -f \[DOMAIN_HOME\]/nodemanager/nodemanager.log

490. On VM1, watch for the following log messages to indicate the node managers are up:

\<INFO\> \<Secure socket listener started on port 5556, host *\[vm1_fqdn\]*\>

491. On VM2, wait for node manager startups to complete:

\$ tail -f \[DOMAIN_HOME\]/nodemanager/nodemanager.log

492. On VM2, watch for the following log messages to indicate the node managers are up:

\<INFO\> \<Secure socket listener started on port 5556, host *\[vm2_fqdn\]*\>

493. On VM1, start AdminServer:

\$ ./startWebLogic\_*\[domain\]*.sh

494. On VM1, wait for the AdminServer startup to complete:

\$ tail -f \[DOMAIN_HOME\]/servers/AdminServer/logs/AdminServer.out

495. On VM1, watch for the following log messages to indicate the AdminServer is up:

\<Notice\> \<WebLogicServer\> \<BEA-000365\> \<Server state changed to RUNNING.\>

### Managed Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into the *\[domain\]* Admin Console, start “erx1” and “erx2” managed servers
496. Verify landing pages are responding:

https://*\[proxy_fqdn\]*/INB-ERX/

https://*\[proxy_fqdn\]*/inbound/

### Pentaho Services Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  As your normal Linux login account, dzdo su to the kettle account:

\$ dzdo su - kettle

497. On VM1, start *\[ENV\]* Master Slave:

\$ ./startCarte*\[Env\]*Master1.sh

498. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Master Slave to start up by watching: https://*\[proxy_fqdn\]*/master1/kettle/status/
499. On VM 1, start *\[ENV\]* Dynamic Slave1:

\$ ./startCarte*\[Env\]*Slave1.sh

500. On VM 1, start *\[ENV\]* Dynamic Slave2:

\$ ./startCarte*\[Env\]*Slave2.sh

501. On VM 2, start *\[ENV\]* Dynamic Slave3:

\$ ./startCarte*\[Env\]*Slave3.sh

502. On VM 2, start *\[ENV\]* Dynamic Slave4:

\$ ./startCarte*\[Env\]*Slave4.sh

503. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Slave1 to start up by watching: https://*\[proxy_fqdn\]*/slave1/kettle/status/
504. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Slave2 to start up by watching: https://*\[proxy_fqdn\]*/slave2/kettle/status/
505. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Slave3 to start up by watching: https://*\[proxy_fqdn\]*/slave3/kettle/status/
506. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Slave4 to start up by watching: https://*\[proxy_fqdn\]*/slave4/kettle/status/
507. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check that all 4 dynamic slaves have registered with the master: https://*\[proxy_fqdn\]*/slave1/kettle/getSlaves/
508. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), start the message processing jobs:  
     https://*\[proxy_fqdn\]*/slave1/kettle/runJob/?job=inbound_main/InboundMessageProcessing_JOB  
     https://*\[proxy_fqdn\]*/slave2/kettle/runJob/?job=inbound_main/InboundMessageProcessingRetry_JOB  
     https://*\[proxy_fqdn\]*/slave3/kettle/runJob/?job=inbound_vista_delivery/InboundDeliverToVista_JOB  
     https://*\[proxy_fqdn\]*/slave4/kettle/runJob/?job=outbound_main/OutboundMessageProcessing_JOB
509. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check the InboundMessageProcessing_JOB status: https://*\[proxy_fqdn\]*/slave1/kettle/status, click on the InboundMessageProcessing_JOB hyperlink and check the job status page.
510. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check the InboundMessageProcessingRetry_JOB status: https://*\[proxy_fqdn\]*/slave2/kettle/status, click on the InboundMessageProcessingRetry_JOB hyperlink and check the job status page.
511. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check the InboundDeliverToVista \_JOB status: https://*\[proxy_fqdn\]*/slave3/kettle/status, click on the InboundDeliverToVista \_JOB hyperlink and check the job status page.
512. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check the OutboundMessageProcessing \_JOB status: https://*\[proxy_fqdn\]*/slave4/kettle/status, click on the OutboundMessageProcessing hyperlink and check the job status page.

## Shut Down Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pentaho Services Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  As your normal Linux login account, dzdo su to the kettle account:

\$ dzdo su - kettle

513. As kettle on VM2:

\$ /u01/app/pentaho/pdi-*\[env\]*slave3/carte.sh *\[vm2_fqdn\]* 8083 -s -u cluster -p cluster

\$ /u01/app/pentaho/pdi-*\[env\]*slave4/carte.sh *\[vm2_fqdn\]* 8084 -s -u cluster -p cluster

514. As kettle on VM1:

\$ /u01/app/pentaho/pdi-*\[env\]*slave1/carte.sh *\[vm1_fqdn\]* 8081 -s -u cluster -p cluster

\$ /u01/app/pentaho/pdi-*\[env\]*slave2/carte.sh *\[vm1_fqdn\]* 8082 -s -u cluster -p cluster

\$ /u01/app/pentaho/pdi-*\[env\]*master1/carte.sh *\[vm1_fqdn\]* 8080 -s -u cluster -p cluster

### WebLogic Application Server Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  As your normal Linux login account, dzdo su to the weblogic account:

\$ dzdo su – weblogic

515. Log into erxdomain1 Admin Console as weblogic

Stop erx1 and erx2 managed servers

Stop Admin console

516. On VM1, as weblogic:

\$ ./stopWebLogic\_*\[domain\]*.sh

517. On VM1, as weblogic:

\$ ./stopNodemanager\_*\[domain\]*.sh

518. On VM2, as weblogic:
519. \$ ./stopNodemanager\_*\[domain\]*.sh