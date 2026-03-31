---
consolidated_title: "inbound eprescribing dibr"
app_code: PSO
doc_type: DIBR
master_source: "PSO*7*589  Inbound ePrescribing DIBR"
master_pub_date: February 2020
consolidated_from: 4 versions
prior_versions:
  - "PSO*7*590 Inbound ePrescribing DIBR"
  - "PSO*7*610 Inbound ePrescribing DIBR"
  - "PSO*7*617 Inbound ePrescribing DIBR"
---

---
title: |
  <span id="_top" class="anchor"></span>Pharmacy Reengineering (PRE)

  Inbound ePrescribing (IEP) 3.1

  Pentaho 8.2

  <span id="_Hlk31639334" class="anchor"></span>Deployment, Installation, Rollback, and Back-Out Guide (DIRB)
---

![](pso-7-589-inbound-eprescribing-dibr/001.png)

February 2020

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p><span id="_Toc525722924" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 54%" />
<col style="width: 20%" />
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
<td>02/26/2020</td>
<td>2.7</td>
<td><p>PSO*7.0*589 Maintenance Patch Release:</p>
<ul>
<li><p>Updated WebLogic Installation section</p></li>
<li><p>Updated Pentaho Installation section</p></li>
<li><p>Updated VistA Back-Out and Rollback sections</p></li>
<li><p>Updated Title page, Revision History, and Footers</p></li>
<li><p>Updated formatting for consistency throughout</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
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
<td>Update Title page to month of November</td>
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
<p>Sections: <a href="#back-out-of-vista-patch">5.6.1</a>, <a href="#p146_508">5.7.1</a>, <a href="#rollback-vista-patch">6.5.2</a>, <a href="#rollback-verification-procedure">6.5.2.1</a></p></td>
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
<td>Sprint Update – Added draft steps for rolling back WebLogic; added the VistA Patch #; added a placeholder for backing out the database.</td>
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
    - [Application Architecture](#application-architecture)
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
    - [Pre-requisites](#pre-requisites)
    - [Environment Configurations](#environment-configurations)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
    - [Modify /etc/hosts entry](#modify-etchosts-entry)
    - [X Windows](#x-windows)
    - [Setup Administration Accounts](#setup-administration-accounts)
    - [Install Java](#install-java)
    - [Apache Installation on VM1 and VM2](#apache-installation-on-vm1-and-vm2)
    - [Apache Configuration on VM1 and VM2](#apache-configuration-on-vm1-and-vm2)
    - [Certificate Configuration](#certificate-configuration)
    - [Create NSS certificate database on VM1](#create-nss-certificate-database-on-vm1)
    - [Create NSS certificate database on VM2](#create-nss-certificate-database-on-vm2)
    - [NSS Configuration on VM1](#nss-configuration-on-vm1)
    - [NSS Configuration on VM2](#nss-configuration-on-vm2)
    - [Install Apache Plug-in for WebLogic on VM1 and VM2](#install-apache-plug-in-for-weblogic-on-vm1-and-vm2)
    - [Configure Apache Plug-in for WebLogic on VM1](#configure-apache-plug-in-for-weblogic-on-vm1)
    - [Configure Apache Plug-in for WebLogic on VM2](#configure-apache-plug-in-for-weblogic-on-vm2)
    - [Create IEP CPanel on VM1 and VM2](#create-iep-cpanel-on-vm1-and-vm2)
    - [Install Apache SSOi Web Agent on VM1](#install-apache-ssoi-web-agent-on-vm1)
    - [Configure Apache SSOi Web Agent on VM1](#configure-apache-ssoi-web-agent-on-vm1)
    - [Post Configure Edits for Apache SSOi Web Agent on VM1](#post-configure-edits-for-apache-ssoi-web-agent-on-vm1)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [WebLogic Installation](#weblogic-installation)
    - [Inbound eRx Application Installation](#inbound-erx-application-installation)
    - [Pentaho Installation](#pentaho-installation)
    - [Nexus Repository Installation (DEV2 VM1 Only)](#nexus-repository-installation-dev2-vm1-only)
    - [VistA Patch Installation](#vista-patch-installation)
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
    - [Back-Out of VistA Patch](#back-out-of-vista-patch)
    - [Back-Out of Database](#back-out-of-database)
    - [Back-Out of WebLogic](#back-out-of-weblogic)
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
    - [Validation of Roll Back Procedure](#validation-of-roll-back-procedure)
- [Operational Procedures](#operational-procedures)
  - [Startup Procedures](#startup-procedures)
    - [Start Weblogic Node Managers and Admin Console](#start-weblogic-node-managers-and-admin-console)
    - [Managed Servers](#managed-servers)
    - [Pentaho Services Startup](#pentaho-services-startup)
  - [Shut Down Procedures](#shut-down-procedures)
    - [Pentaho Services Shutdown](#pentaho-services-shutdown)
    - [WebLogic Application Server Shutdown](#weblogic-application-server-shutdown)
- [Appendices](#appendices)
  - [Certificate Contents](#certificate-contents)
    - [varootcacert.txt](#varootcacerttxt)
    - [vainternalsubordinatecacert.txt](#vainternalsubordinatecacerttxt)
    - [varootcas2cert.pem](#varootcas2certpem)
    - [vainternalca1s2cert.pem](#vainternalca1s2certpem)
    - [vainternalca2s2cert.pem](#vainternalca2s2certpem)
    - [betrustedproductionsspcaa1cert.txt](#betrustedproductionsspcaa1certtxt)
    - [federalcommonpolicycacert.txt](#federalcommonpolicycacerttxt)
    - [veteransaffairsdevicecab2cert.txt](#veteransaffairsdevicecab2certtxt)
    - [vaww.esrdev.aac.<span class="mark">REDACTED</span>\cert.txt](#vawwesrdevaacspan-classmarkredactedspancerttxt)
    - [vaww.esrstage1a.aac.<span class="mark">REDACTED</span>.pem](#vawwesrstage1aaacspan-classmarkredactedspanpem)
    - [vaww.esrstage1b.aac.<span class="mark">REDACTED</span>.pem](#vawwesrstage1baacspan-classmarkredactedspanpem)
    - [vaww.esrpre-prod.aac.<span class="mark">REDACTED</span>.pem](#vawwesrpre-prodaacspan-classmarkredactedspanpem)
    - [das-test.<span class="mark">REDACTED</span>.pem](#das-testspan-classmarkredactedspanpem)
    - [das-sqa.<span class="mark">REDACTED</span>.pem](#das-sqaspan-classmarkredactedspanpem)
    - [das.<span class="mark">REDACTED</span>.pem](#dasspan-classmarkredactedspanpem)
This document describes how to deploy and install the various components of the software for the Pharmacy Reengineering (PRE) Inbound ePrescribing (eRx) project, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial Off-the-Shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.
Veterans Health Administration (VHA), Patient Care Services (PCS) and Pharmacy Benefits Management (PBM) has requested a new capability as part of the PRE program to receive inbound electronic prescriptions (e-prescriptions or eRxs) from an external provider (e.g., a doctor not associated with the Department of Veterans Affairs \[VA\], medical staff at a Department of Defense \[DoD\] military treatment facility, etc.). They also seek the ability to transfer prescriptions electronically between pharmacies, both VA to VA, as well as VA to non-VA (ideally). Once received, these prescriptions will then be fed into the existing Veterans Health Information Systems and Technology Architecture (VistA) Outpatient Pharmacy (OP) for processing and dispensing.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the PRE Inbound eRx application will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Figure 1 depicts the Inbound eR<sub>x</sub> application and the external systems that it interacts with, including the following: Change Healthcare, Master Veteran Index (MVI), Eligibility & Enrollment (E&E), Health Data Repository (HDR), and VistA OP.

<span id="_Toc439226961" class="anchor"></span>Figure 1: Inbound eR<sub>x</sub> Application Context Diagram

![](pso-7-589-inbound-eprescribing-dibr/002.png)

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
- The team must publish relational and object-oriented databases utilized by the solution in the current VA Release Architecture.
- The team must base application production capacity requirements on workload analysis, simulated workload benchmark tests, or application performance models.
- The team must base application storage capacity requirements on detailed capacity analysis and/or models.
- The team must design the solution to operate within the current VA Local Area Network (LAN) and Wide Area Network (WAN) network configurations.
- The deployment environment must meet the performance and downtime monitoring requirements of the solution.
- The team and data center must develop and provision a disaster recovery plan.
- All critical infrastructure components (including data) must be located at multiple physical locations.
- The application backup and restore solution must meet data recovery requirements \[Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO)\].
- The application UIs must exist as browser-based UIs and roll and scroll in VistA.
- The application must establish secure access paths for accessing the application and application data.
- The solution must document specific reasons for all limited, external access to data, including the need to know along with security, privacy and other legal restrictions.
- The solution must implement appropriate controls that prevent unwarranted disclosure of sensitive, Personally Identifiable Information (PII), or Protected Health Information (PHI).
- The team must base all system interfaces (both external and internal) implemented by the solution on open standards such as SOAP, REST, JMS, MQ, HTTPS and standard message formats such as HL7and NCPDP.
- The solution must access available enterprise information through services.
- The VA TRM must identify all products and standards used by this solution as permissible for usage.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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

The deployment and installation is scheduled to run for 18 months as depicted in the master deployment schedule. The timelines are depicted in the Deployment Timeline table below.

<table>
<caption><p><span id="_Toc525722926" class="anchor"></span>Table 3: Site Preparation</p></caption>
<colgroup>
<col style="width: 74%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>VIP Build</th>
<th>Delivery Dates</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VIP Build 1 Transaction Hub Version 1.0 Foundation</td>
<td>07/28/2016-10/31/2016</td>
</tr>
<tr class="even">
<td>VIP Build 2 Transaction Hub Version 1.0 Complete eRx Transaction Hub</td>
<td>10/31/2016-01/27/2017</td>
</tr>
<tr class="odd">
<td><p>VIP Builds 3 &amp; 4 Inbound Electronic Prescriptions Version 2.0 Complete</p>
<p>Inbound eRx Transaction Processing, UAT, IOC, CD-2</p></td>
<td>01/28/2017-07/27/2017</td>
</tr>
<tr class="even">
<td>VIP Build 5 National Deployment Version 2.0 (includes 1.0 and 2.0)</td>
<td>07/28/2017-11/27/2017</td>
</tr>
<tr class="odd">
<td><p>VIP Build 1 &amp; 2 (New CD1) Transfer to/from VA Pharmacy Development Increment for Version 3</p>
<p>eRx Transfers plus other features development, UAT, IOC, CD-2</p></td>
<td>07/28/2017-01/27/2018</td>
</tr>
<tr class="even">
<td><p>VIP Build 3 National Deployment Version 3</p>
<p>National Deployment of Version 3.0 (4 months total)</p></td>
<td>03/04/2018-06/01/2018</td>
</tr>
</tbody>
</table>

<span id="_Toc525722926" class="anchor"></span>Table 3: Site Preparation

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the PRE Inbound eRx application deployment. Topology determinations are made by Enterprise Systems Engineering (ESE) and vetted by Field Operations (FO), National Data Center Program (NDCP), and AITC during the design phase as appropriate. Field site coordination is done by FO unless otherwise stipulated by FO.

The product will be released by the PRE Inbound eRx Configuration Manager to the AITC Build Manager via a Change Order. The AITC Build Manager will follow the installation steps in Section 4 to complete the product’s activation at AITC and for the Disaster Recovery server. The Implementation Manager has assured site readiness by assessing the readiness of the receiving site to deploy the product. AITC, under contract, will provide the product dependencies, power, equipment, space, manpower, etc., to ensure the successful activation of this product.

### Application Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram represents the high-level architecture for the eRx application.

<span id="_Toc29569548" class="anchor"></span>Figure 2: High-Level eRx Architecture

![](pso-7-589-inbound-eprescribing-dibr/003.png)

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product will be released to AITC. The AITC, under contract, will house and secure this product on its Pre-Production and then Production servers. A few field located super users will be given access upon National Release. The PRE Inbound eRx system will be available to VA users on a continuous basis (excluding scheduled maintenance activities). Clustering at the application and web services servers will provide high availability and failover capabilities at the application tier and presentation tier. The servers will be load-balanced to distribute uniform processing across all servers.

Additionally, a VistA patch will be released to all VistA sites.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AITC will host the web and application servers for the PRE Inbound eRx system.

Initial Operating Capability (IOC) will occur in September of 2018. IOC sites are:

- Brooklyn, NY VA Medical Center (VAMC)
- Fayetteville VAMC Veterans Health Care System of the Ozarks
- Health Administration Center (Meds by Mail)
- Indianapolis, IN VA Medical Center

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
<td>12.1.3c</td>
<td>Clustered</td>
<td>Oracle</td>
<td></td>
</tr>
<tr class="even">
<td>Oracle Database</td>
<td>Database</td>
<td>11.2.0g</td>
<td>Standalone (not synchronized across data centers)</td>
<td>Oracle</td>
<td></td>
</tr>
<tr class="odd">
<td>Pentaho Data Integration</td>
<td>Data Integration Tool</td>
<td>8.2</td>
<td>Standalone</td>
<td>Pentaho (a Hitachi Group Company)</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc525722928" class="anchor"></span>Table 5: Deployment/Installation/Back-Out Checklist

Please see the Roles and Responsibilities table in Section 2 above for details about who is responsible for preparing the site to meet these software specifications.

The software components will be staged at the following location:

\\vaauspecdbs801.aac.dva.<span class="mark">REDACTED</span>\AITC\IEP-eRx\downloads

Application deployment packages will be staged at the following location:

\\vaauspecdbs801.aac.dva.<span class="mark">REDACTED</span>\AITC\IEP-eRx\v.30\deployments

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the communications to be distributed to the business user community:

- Communication between the development team and AITC will occur via email and conference calls scheduled through Microsoft Lync.
- Notification of scheduled maintenance periods that require the service to be offline or that may degrade system performance will be disseminated to the business user community a minimum of 48 hours prior to the scheduled event.
- Notification to VA users for unscheduled system outages or other events that impact the response time will be distributed within 30 minutes of the occurrence.
- Notification will be distributed to VA users regarding technical help desk support for obtaining assistance with receiving and processing inbound eRxs and sending and receiving eRx transfers.

#### Deployment/Installation/Back-Out Checklist

The table below is an example of the coordination effort and can be used to document the day/time/individual when each activity (deploy, install, back-out) is completed for Inbound eRx.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

<span id="_Toc525722929" class="anchor"></span>Table 6: Development/SQA Detailed VM Requirements

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the installation steps for the various Inbound eRx components.

1.  The highlighted sections throughout this document indicate that that the text will be modified in future versions of this document.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the minimum requirements for the product to be installed, as well as the recommended hardware and software system requirements.

### Pre-requisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table outlines the specifications for VM.

| VM    | RAM (GB) | Space (GB) | CPUs | OS     | VM Description/Use/DNS Required         |
|-------|----------|------------|------|--------|-----------------------------------------|
| 1     | 16       | 300        | 4    | RHEL 6 | DEV 1 DB Server running Oracle          |
| 2     | 16       | 300        | 4    | RHEL 6 | DEV 2 DB Server running Oracle          |
| 3     | 16       | 300        | 4    | RHEL 6 | SQA 1 DB Server running Oracle          |
| 4     | 16       | 300        | 4    | RHEL 6 | SQA 2 DB Server running Oracle          |
| 5     | 16       | 300        | 4    | RHEL 6 | DEV1 AP Server running Apache/WebLogic  |
| 6     | 16       | 300        | 4    | RHEL 6 | DEV 2 AP Server running Apache/WebLogic |
| 7     | 16       | 300        | 4    | RHEL 6 | SQA 1 AP Server running Apache/WebLogic |
| 8     | 16       | 300        | 4    | RHEL 6 | SQA 2 AP Server running Apache/WebLogic |
| Total | 128      | 2400       | 32   | 8      |                                         |

<span id="_Toc525722930" class="anchor"></span>Table 7: Staging Detailed VM Requirements

| VM    | RAM (GB) | Space (GB) | CPUs | OS     | VM Description/Use/DNS Required                    |
|-------|----------|------------|------|--------|----------------------------------------------------|
| 1     | 16       | 800        | 4    | RHEL 7 | STAGING DB Server running Oracle                   |
| 2     | 16       | 300        | 4    | RHEL 7 | STAGING Application Server running Apache/WebLogic |
| 3     | 16       | 300        | 4    | RHEL 7 | STAGING Application Server running Apache/WebLogic |
| Total | 48       | 1400       | 16   | 3      |                                                    |

<span id="_Toc525722931" class="anchor"></span>Table 8: Pre-Production Detailed VM Requirements

| VM    | RAM (GB) | Space (GB) | CPUs | OS     | VM Description/Use/DNS Required                           |
|-------|----------|------------|------|--------|-----------------------------------------------------------|
| 1     | 16       | 1300       | 4    | RHEL 6 | PRE-PRODUCTION DB Server running Oracle                   |
| 2     | 16       | 300        | 4    | RHEL 6 | PRE-PRODUCTION Application Server running Apache/WebLogic |
| 3     | 16       | 300        | 4    | RHEL 6 | PRE-PRODUCTION Application Server running Apache/WebLogic |
| Total | 48       | 1900       | 12   | 3      |                                                           |

<span id="_Toc525722932" class="anchor"></span>Table 9: Production Detailed VM Requirements

| VM    | RAM (GB) | Space (GB) | CPUs | OS     | VM Description/Use/DNS Required                       |
|-------|----------|------------|------|--------|-------------------------------------------------------|
| 1     | 16       | 1300       | 4    | RHEL 6 | PRODUCTION DB Server running Oracle                   |
| 2     | 16       | 300        | 4    | RHEL 6 | PRODUCTION Application Server running Apache/WebLogic |
| 3     | 16       | 300        | 4    | RHEL 6 | PRODUCTION Application Server running Apache/WebLogic |
| Total | 48       | 1900       | 12   | 3      |                                                       |

<span id="_Toc525722933" class="anchor"></span>Table 10: Environment Variables

### Environment Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 10 lists Environment Variables values that should be substituted throughout this document as system administrators are completing the installation steps.

| ENV   | ORACLE_BASE          | WLS_HOME               | DOMAIN_HOME                                       |
|-------|----------------------|------------------------|---------------------------------------------------|
| DEV1  | /u01/app/Oracle_Home | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/erxdomain1    |
| DEV2  | /u01/app/Oracle_Home | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/erxdomain2    |
| SQA1  | /u01/app/Oracle_Home | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/erxdomain1    |
| STAG  | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-stage     |
| STAG2 | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-stage2    |
| PREP  | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-preprod   |
| PREP2 | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/ iep-preprod2 |
| PROD  | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-prod      |
| PROD2 | /u01/oracle          | \$ORACLE_BASE/wlserver | \$ORACLE_BASE/user_projects/domains/iep-prod2     |

<span id="_Toc525722934" class="anchor"></span>Table 11: Symbolic Names by Environment

Table 11 lists the symbolic names that should be substituted throughout this document as system administrators are completing the installation steps.

| ENV   | vm1_fqdn                           | vm1_name                           | vm2_fqdn                           | vm2_name                           | domain       |
|-------|------------------------------------|------------------------------------|------------------------------------|------------------------------------|--------------|
| DEV1  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | erxdomain1   |
| DEV2  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | erxdomain2   |
| SQA1  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | erxdomain1   |
| STAG  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | iep-stage    |
| STAG2 | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | iep-stage2   |
| PREP  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | iep-preprod  |
| PREP2 | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | iep-preprod2 |
| PROD  | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | iep-prod     |
| PROD2 | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | iep-prod2    |

<span id="_Toc525722935" class="anchor"></span>Table 12: Symbolic Names by Environment (cont.)

| ENV   | env   | Env   | erx_port | proxy_fqdn                         | proxy_name                         | db_fqdn                            | db_name | db_port |
|-------|-------|-------|----------|------------------------------------|------------------------------------|------------------------------------|---------|---------|
| DEV1  | dev1  | Dev1  | 8001     | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | ERXD1   | 1549    |
| DEV2  | dev2  | Dev2  | 8003     | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | ERXD2   | 1550    |
| SQA1  | sqa1  | Sqa1  | 8001     | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | ERXS1   | 1549    |
| STAG  | stag  | Stag  | 8001     | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | IEPQA   | 1647    |
| STAG2 | stag2 | Stag2 | 8001     | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | IEPQA2  | 1648    |
| PREP  | prep  | Prep  | 8001     | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | IEPY    | 1647    |
| PREP2 | prep2 | Prep2 | 8001     | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | IEPY2   | 1647    |
| PROD  | prod  | Prod2 | 8001     | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | IEPP    | 1647    |
| PROD2 | prod2 | Prod2 | 8001     | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | IEPP2   | 1647    |

<span id="_Toc525722936" class="anchor"></span>Table 13: Symbolic Names by Environment (cont.)

| ENV   | mserver1         | mserver2         | cluster    |
|-------|------------------|------------------|------------|
| DEV1  | erx1             | erx2             | dev1       |
| DEV2  | erx1             | erx2             | dev1       |
| SQA1  | erx1             | erx2             | dev1       |
| STAG2 | ManagedServer001 | ManagedServer002 | Cluster001 |
| STAG  | ManagedServer001 | ManagedServer002 | Cluster001 |
| PREP2 | ManagedServer001 | ManagedServer002 | Cluster001 |
| PREP  | ManagedServer001 | ManagedServer002 | Cluster001 |
| PROD2 | ManagedServer001 | ManagedServer002 | Cluster001 |
| PROD  | ManagedServer001 | ManagedServer002 | Cluster001 |

<span id="_Toc525722937" class="anchor"></span>Table 14: Symbolic Names by Environment (cont.)

<table>
<caption><p><span id="_Toc525722938" class="anchor"></span>Table 15: Symbolic Names by Environment (cont.)</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 16%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>ENV</th>
<th>iam_hco</th>
<th>iam_policy_entries</th>
</tr>
<tr class="odd">
<th>DEV1</th>
<th>INTHCO</th>
<th><p>policyserver="smp1.int.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp2.int.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp3.int.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp4.int.iam.<mark>REDACTED</mark>,44441,44442,44443"</p></th>
</tr>
<tr class="header">
<th>DEV2</th>
<th>INTHCO</th>
<th><p>policyserver="smp1.int.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp2.int.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp3.int.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp4.int.iam.<mark>REDACTED</mark>,44441,44442,44443"</p></th>
</tr>
<tr class="odd">
<th>SQA1</th>
<th>SQAHCO</th>
<th><p>policyserver="smp1.sqa.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp2.sqa.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp3.sqa.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp4.sqa.iam.<mark>REDACTED</mark>,44441,44442,44443"</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>STAG</td>
<td>PREPRODHCO</td>
<td><p>policyserver="smp1.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp2.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp3.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp4.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp5.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp6.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp7.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp8.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p></td>
</tr>
<tr class="even">
<td>STAG2</td>
<td>PREPRODHCO</td>
<td><p>policyserver="smp1.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp2.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp3.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp4.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp5.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp6.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp7.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp8.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p></td>
</tr>
</tbody>
</table>

<span id="_Toc525722938" class="anchor"></span>Table 15: Symbolic Names by Environment (cont.)

<table>
<caption><p><span id="_Toc525722939" class="anchor"></span>Table 16: Symbolic Names by Environment (cont.)</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 18%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>ENV</th>
<th>iam_hco</th>
<th>iam_policy_entries</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PREP</td>
<td>PREPRODHCO</td>
<td><p>policyserver="smp1.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp2.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp3.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp4.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp5.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp6.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp7.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp8.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p></td>
</tr>
<tr class="even">
<td>PREP2</td>
<td>PREPRODHCO</td>
<td><p>policyserver="smp1.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp2.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp3.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp4.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp5.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp6.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp7.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp8.preprod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p></td>
</tr>
</tbody>
</table>

<span id="_Toc525722939" class="anchor"></span>Table 16: Symbolic Names by Environment (cont.)

<table>
<caption><p><span id="_Toc525722940" class="anchor"></span>Table 17: Symbolic Names for sensitive items</p></caption>
<colgroup>
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>ENV</th>
<th>iam_hco</th>
<th>iam_policy_entries</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PROD</td>
<td>PRODHCO</td>
<td><p>policyserver="smp1.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp2.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp3.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp4.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp5.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp6.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp7.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp8.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p></td>
</tr>
<tr class="even">
<td>PROD2</td>
<td>PRODHCO</td>
<td><p>policyserver="smp1.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp2.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp3.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp4.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp5.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp6.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp7.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p>
<p>policyserver="smp8.prod.iam.<mark>REDACTED</mark>,44441,44442,44443"</p></td>
</tr>
</tbody>
</table>

<span id="_Toc525722940" class="anchor"></span>Table 17: Symbolic Names for sensitive items

In addition to the above Environment Variables and Symbolic Names, there are several passwords or secret phrases which are required throughout the installation. The table below identifies Symbolic Names that will be used in this document and provide a brief description of each. The values of these sensitive items will be defined by the appropriate administrator during the installation process and should be properly recorded and shared with others on a need to know basis.

| Symbolic Name         |     |     |     |
|-----------------------|-----|-----|-----|
| keystore_passphrase   |     |     |     |
| privatekey_passphrase |     |     |     |
| weblogic_password     |     |     |     |

Symbolic Names by Environment (continued)Symbolic Names by Environment (Continued)

The following are the properties that define the SSL security settings for WebLogic. These properties must be set respective to each environment.

KeyStores=CustomIdentityAndCustomTrust

CustomIdentityAlias=*\[proxy_fqdn\]*

CustomIdentityKeyStoreFileName=*\[DOMAIN_HOME\]*/security/*\[proxy_fqdn\]*

CustomIdentityKeyStorePassPhrase=*\[keystore_passphrase\]*

CustomIdentityKeyStoreType=JKS

CustomIdentityPrivateKeyPassPhrase=*\[privatekey_passphrase\]*

Ensure the environment variables are set as follows:

\$ export ORACLE_BASE=/u01/app/Oracle_Home

\$ export WLS_HOME=\$ORACLE_BASE/wlserver

\$ export DOMAIN_HOME=\$ORACLE_BASE/user_projects/domains/erxdomain1

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the steps to prepare the operating system for the installation of the application. Most activities are to be performed by the RHEL System Administrator.

### Modify /etc/hosts entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Modify /etc/hosts to add fully qualified domain name for the local server (the following must be performed by a system administrator):

\$ sudo vi /etc/hosts

2.  Add entries similar to the following:

???.???.???.??? *\[vm1_fqdn\]\[vm1_name\]*.domain.local *\[vm1_name\]*

???.???.???.??? *\[vm2_fqdn\]\[vm2_name\]*.domain.local *\[vm2_name\]*

???.???.???.??? *\[db_fqdn\]\[db_name\]*.domain.local *\[db_name\]*

3.  Save the file and exit. Note the following explanations of the hosts entry fields:

???.???.???.??? \<- IP address of the server

### X Windows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Install the Linux X Window libraries (the following must be performed by a system administrator):

\$ sudo yum install xorg-x11-xauth.x86_64

4.  Start Attachmate Reflection X (Click *Start* \> *All Programs* \> *Attachmate Reflection* \> *Reflection X*).
5.  Modify the SSH session:
    1.  Connection \> SSH \> X11 \> Enable X11 forwarding
    2.  Connection \> SSH \> X11 \> X display location \> :0.0
6.  Connect to the Linux server with the new SSH session settings. The DISPLAY environment variable should be automatically set.
7.  In order to run X applications after doing a sudo su to another account, first modify the .Xauthority file
8.  As your normal Linux login account:

\$ cp ~/.Xauthority /tmp

9.  After you sudo su to another user, copy the .Xauthority file:

\$ cp /tmp/.Xauthority ~

### Setup Administration Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Create the Linux WebLogic user and group (the following must be performed by a system administrator):

\$ sudo groupadd -g 7400 weblogic (this group already exists in LDAP)

\$ sudo useradd -g weblogic

10. Create the Linux weblogic sudoer file (the following must be performed by a system administrator):

\$ cat \> /etc/sudoers.d/weblogic

weblogic ALL=NOPASSWD:/sbin/service wls start,/sbin/service wls stop,/sbin/service wls stop_all,/sbin/service wls status,/sbin/service wlnm start,/sbin/service wlnm stop,/sbin/service wlnm status

Cmnd_Alias WLS_SU=/bin/su - weblogic, /bin/su - weblogic2, /bin/su - weblogic3, /bin/su - aacesrpprod, /bin/su - aacxpologger, /bin/su - introsvr

Cmnd_Alias WLS_CMD=/bin/ls, /bin/du, /bin/grep, /bin/cat, /sbin/chkconfig --list, /sbin/service wls stop, /sbin/service wls start

Cmnd_Alias LSOF_CMD=/usr/sbin/lsof

WLS ALL=(ALL) WLS_CMD

WLS ALL=(ALL) WLS_SU

WLS ALL=(ALL) LSOF_CMD

%weblogic ALL=(ALL) WLS_CMD

%weblogic ALL=(ALL) WLS_SU

%weblogic ALL=(ALL) LSOF_CMD

\<ctrl\>d

11. Modify the Linux weblogic account to add umask command near the beginning of the file ~weblogic/.bash_profile:

umask 0022

12. Create the app software directory if it doesn’t exist (the following must be performed by a system administrator):

\$ sudo chmod 777 /u01

\$ sudo mkdir -p /u01/app

\$ sudo chown weblogic:weblogic /u01/app

\$ sudo chmod 777 /u01/app

13. Create the Linux kettle user and group (the following must be performed by a system administrator):

\$ sudo groupadd -g 7600 kettle

\$ sudo useradd -g kettle kettle

\$ sudo usermod -a -G weblogic kettle (weblogic group already exists in LDAP)

14. Create the Linux kettle sudoer file (the following must be performed by a system administrator):

\$ sudo cat \> /etc/sudoers.d/kettle

kettle ALL=NOPASSWD:/sbin/service kettle start,/sbin/service kettle stop,/sbin/service kettle stop_all,/sbin/service kettle status

Cmnd_Alias KETTLE_SU=/bin/su - kettle

Cmnd_Alias KETTLE_CMD=/bin/ls, /bin/du, /bin/grep, /bin/cat, /sbin/chkconfig --list, /usr/sbin/lsof

%kettle ALL=(ALL) KETTLE_CMD

%kettle ALL=(ALL) KETTLE_SU

\<ctrl\>d

15. Create the pentaho software directory if it doesn’t exist (the following must be performed by a system administrator):

\$ sudo mkdir -p /u01/app/pentaho

\$ sudo chown kettle:kettle /u01/app/pentaho

\$ sudo chmod 755 /u01/app/pentaho

16. Modify the Linux kettle account to add umask command near the beginning of the file ~kettle/.bash_profile:

umask 0022

17. Modify the Linux kettle account to replace the PATH= and export PATH near the end of the file ~kettle/.bash_profile:

export JAVA_HOME=/u01/app/java/latest/bin/java

export PATH=\${JAVA_HOME}/bin:\${PATH}:\${HOME}/bin

18. Create the Linux apache sudoer file (the following must be performed by a system administrator):

\$ sudo vi /etc/sudoers.d/apache

apache ALL=(kettle:kettle) NOPASSWD:/u01/app/cpanel/bin/carte_slave_util.sh

\<ctrl\>d

### Install Java

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

19. Create downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

20. Download Oracle JDK 1.8 for Linux x86-64 to the downloads directory:

Download from ATIC IEP eRx Downloads directory

21. Create Java directory if it doesn’t exist:

\$ mkdir -p /u01/app/java

22. Unpack the Oracle JDK 1.8 archive to in the downloads directory:

\$ cd /u01/app/java

\$ gzip –cd \< /u01/downloads/jdk-8uxxx-linux-x64.tar.gz \| tar xvf -

23. Create symbolic link for latest Java installation:

\$ ln –s cd /u01/app/java/jdk1.8.0_xxx /u01/app/java/latest

24. Add instructions to open permissions to permit access to all users, and to create link for /u01/app/java if located in a different location.

\$ exit

25. Return to your Linux account.

\$ exit

### Apache Installation on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Perform the following steps on VM1 and VM2:

1.  EO SA installs standard Apache 2.2 RHEL6 RPM, login to Linux and verify the following:

\$ sudo rpm -q -a \| grep httpd

httpd-2.2.15-39.el6.x86_64

httpd-tools-2.2.15-39.el6.x86_64

26. Install the Linux NSS package (the following must be performed by a system administrator):

\$ sudo yum install mod_nss.x86_64

27. Modify the httpd startup configuration (the following must be performed by a system administrator):

\$ sudo chkconfig --level 2345 httpd on

\$ sudo systemctl enable httpd \# for RHEL 7 systems

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

\$ sudo vi /etc/httpd/conf/httpd.conf

28. Modify Timeout parameter:

Timeout 120

29. Modify \<IfModule prefork.c\>parameters:

StartServers 8

ServerLimit 300

MaxClients 300

30. Modify Listen parameter:

Listen 80

31. Modify \<Directory /\> section:

\<Directory /\>

Options FollowSymLinks

AllowOverride None

\<Limit PUT\>

Order deny,allow

Deny from all

\</Limit\>

\</Directory\>

32. Modify \<Directory "/var/www/icons"\> Options parameter:

\#Options Indexes MultiViews FollowSymLinks

Options Indexes

33. Modify \<Directory "/var/www/html"\> section:

\<Directory "/var/www/html"\>

Options Indexes FollowSymLinks

AllowOverride None

Order allow,deny

Allow from all

\</Directory\>

34. Add \<Directory "/var/www/html/cpanel"\> section:

\<Directory "/var/www/html"\>

Options Indexes FollowSymLinks

AllowOverride None

Order allow,deny

Allow from all

\</Directory\>

35. Enable ScriptAlias:

ScriptAlias /cgi-bin/ "/var/www/cgi-bin/"

36. Modify \<Directory "/var/www/cgi-bin"\> section:

\<Directory "/var/www/cgi-bin"\>

AllowOverride None

Options None

Order allow,deny

Allow from all

\</Directory\>

2.  Modify HTTPD configuration:

\$ sudo vi /etc/httpd/conf/httpd.conf

37. Add Header Edit entries to bottom of /etc/http/conf/httpd.conf

Header edit Set-Cookie "(?i)^((?:(?!;\s?HttpOnly).)+)\$" "\$1; HttpOnly"

Header edit Set-Cookie "(?i)^((?:(?!;\s?secure).)+)\$" "\$1; Secure"

Header always append X-Frame-Options DENY

38. Reverse Proxy to Pentaho Slaves in /etc/httpd/conf.d/pentaho.conf:

\$ sudo vi /etc/httpd/conf.d/pentaho.conf

\#

\# Reverse proxy to Pentaho slaves

\#

\<Location /master1/\>

ProxyPass http://\[vm1_fqdn\]:8080/

ProxyPassReverse http://\[vm1_fqdn\]:8080/

AddOutputFilterByType SUBSTITUTE text/html

Substitute "s\|/kettle/\|/master1/kettle/\|i"

\</Location\>

\<Location /slave1/\>

ProxyPass http://\[vm1_fqdn\]:8081/

ProxyPassReverse http://\[vm1_fqdn\]:8081/

AddOutputFilterByType SUBSTITUTE text/html

Substitute "s\|/kettle/\|/slave1/kettle/\|i"

\</Location\>

\<Location /slave2/\>

ProxyPass http://\[vm1_fqdn\]:8082/

ProxyPassReverse http://\[vm1_fqdn\]:8082/

AddOutputFilterByType SUBSTITUTE text/html

Substitute "s\|/kettle/\|/slave2/kettle/\|i"

\</Location\>

\<Location /slave3/\>

ProxyPass http://\[vm2_fqdn\]:8083/

ProxyPassReverse http://\[vm2_fqdn\]:8083/

AddOutputFilterByType SUBSTITUTE text/html

Substitute "s\|/kettle/\|/slave3/kettle/\|i"

\</Location\>

\<Location /slave4/\>

ProxyPass http://\[vm2_fqdn\]:8084/

ProxyPassReverse http://\[vm2_fqdn\]:8084/

AddOutputFilterByType SUBSTITUTE text/html

Substitute "s\|/kettle/\|/slave4/kettle/\|i"

\</Location\>

\<Location /slave5/\>

ProxyPass http://\[vm2_fqdn\]:8085/

ProxyPassReverse http://\[vm2_fqdn\]:8085/

AddOutputFilterByType SUBSTITUTE text/html

Substitute "s\|/kettle/\|/slave4/kettle/\|i"

\</Location\>

39. Restart Apache:

\$ sudo service httpd stop

\$ sudo service httpd start

<span class="mark">  
</span>

### Certificate Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3 thru 14. saving these certificates with .pem file extension instead of .txt, this does not make any difference in functionality, it’s only a better representation of the file format, since they are actually PEM format.

15, 16. Replacing these steps with the AITC standards that we follow to generate and request certificates. Steps are as follows:

1\) Create a configuration file with name: \[proxy_fqdn\].cnf, content:

distinguished_name = req_distinguished_name

\[req\]

req_extensions = v3_req

prompt = no

\[ v3_req \]

\# Extensions to add to a certificate request

basicConstraints = CA:FALSE

keyUsage = nonRepudiation, digitalSignature, keyEncipherment

\# Some CAs do not yet support subjectAltName in CSRs.

\# Instead the additional names are form entries on web

\# pages where one requests the certificate...

subjectAltName = @alt_names

\[alt_names\]

DNS.1 = \[proxy_fqdn1\]

DNS.2 = \[proxy_fqdn2\]

\[ req_distinguished_name \]

C = US

ST = Texas

L = Austin

O = US Department of Veterans Affairs

OU = AITC

CN = \[proxy_fqdn\]

emailAddress = cdcoweblogicadministrators@<span class="mark">REDACTED</span>

\[ req_attributes \]

challengePassword = xxxxxxxxxxx

Command to generate csr and private key:

openssl req -new -newkey rsa:2048 -keyout \[proxy_fqdn\].key -out \[proxy_fqdn\].csr -config \[proxy_fqdn\].cnf

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

40. Create a “certificates” directory to store all certificate artifacts:

\$ mkdir /u01/certificates

\$ cd /u01/certificates

41. Create the va_root_ca_cert.pem certificate in the “certificates” directory:

\$ cat \> va_root_ca_cert.pem

42. Paste the va_root_ca_cert.pem content from Appendix 8.1.1.

\<ctrl\>d

43. Create the va_internal_subordinate_ca_cert.pem content in the “certificates” directory:

\$ cat \> va_internal_subordinate_ca_cert.pem

44. Paste the va_internal_subordinate_ca_cert.pem content from Appendix 8.1.2.

\<ctrl\>d

45. Create the va_root_ca_s2_cert.pem certificate in the “certificates” directory:

\$ cat \> va_root_ca_s2_cert.pem

46. Paste the va_root_ca_s2_cert.pem content from Appendix 8.1.3.

\<ctrl\>d

47. Create the va_intermediate_ca1_s2_cert.pem certificate in the “certificates” directory:

\$ cat \> va_intermediate_ca1_s2_cert.pem

48. Paste the va\_ intermediate_ca1_s2_cert.pem content from Appendix 8.1.4.

\<ctrl\>d

49. Create the va_intermediate_ca2_s2_cert.pem certificate in the “certificates” directory:

\$ cat \> va_intermediate_ca2_s2_cert.pem

50. Paste the va\_ intermediate_ca2_s2_cert.pem content from Appendix 8.1.5.

\<ctrl\>d

51. Create the betrusted_production_ssp_ca_a1_cert.pem certificate in the “certificates” directory:

\$ cat \> betrusted_production_ssp_ca_a1_cert.pem

52. Paste the betrusted_production_ssp_ca_a1_cert.pem content from Appendix 8.1.6.

\<ctrl\>d

53. Create the federal_common_policy_ca_cert.pem certificate in the “certificates” directory:

\$ cat \> federal_common_policy_ca_cert.pem

54. Paste federal_common_policy_ca_cert.txt content from Appendix 8.1.7.

\<ctrl\>d

55. Create the veterans_affairs_device_ca_b2_cert.pem certificate in the “certificates” directory:

\$ cat \> veterans_affairs_device_ca_b2_cert.pem

56. Paste the veterans_affairs_device_ca_b2_cert.pem content from Appendix 8.1.8.

\<ctrl\>d

57. Create the vaww.ersdev.aac.<span class="mark">REDACTED</span>\_cert.pem certificate in the “certificates” directory:

\$ cat \> vaww.ersdev.aac.<span class="mark">REDACTED</span>\_cert.pem

58. Paste the vaww.ersdev.aac.<span class="mark">REDACTED</span>\_cert.pem content from Appendix 8.1.9.

\<ctrl\>d

59. Create the vaww.esrstage1a.aac.<span class="mark">REDACTED</span>.pem certificate in the “certificates” directory:

\$ cat \> vaww.esrstage1a.aac.<span class="mark">REDACTED</span>.pem

60. Paste the vaww.esrstage1a.aac.<span class="mark">REDACTED</span>.pem content from Appendix 8.1.10.

\<ctrl\>d

61. Create the vaww.esrstage1b.aac.<span class="mark">REDACTED</span>.pem certificate in the “certificates” directory:

\$ cat \> vaww.esrstage1b.aac.<span class="mark">REDACTED</span>.pem

62. Paste the vaww.esrstage1b.aac.<span class="mark">REDACTED</span>.pem content from Appendix 8.1.11.

\<ctrl\>d

63. Create the vaww.esrpre-prod.aac.<span class="mark">REDACTED</span>.pem certificate in the “certificates” directory:

\$ cat \> vaww.esrpre-prod.aac.<span class="mark">REDACTED</span>.pem

64. Paste the vaww.esrpre-prod.aac.<span class="mark">REDACTED</span>.pem content from Appendix 8.1.12

\<ctrl\>d

65. Create the das-test.<span class="mark">REDACTED</span>.pem certificate in the “certificates” directory:

\$ cat \> vaww.esrstage1a.aac.<span class="mark">REDACTED</span>.pem

66. Paste the das-test.<span class="mark">REDACTED</span>.pem content from Appendix 0.

\<ctrl\>d

67. Create the das-sqa.<span class="mark">REDACTED</span>.pem certificate in the “certificates” directory:

\$ cat \> das-sqa.<span class="mark">REDACTED</span>.pem

68. Paste the das-sqa.<span class="mark">REDACTED</span>.pem content from Appendix 8.1.14.

\<ctrl\>d

69. Create the das.<span class="mark">REDACTED</span>.pem certificate in the “certificates” directory:

\$ cat \> das.<span class="mark">REDACTED</span>.pem

70. Paste the das.<span class="mark">REDACTED</span>.pem content from Appendix 8.1.15.

\<ctrl\>d

71. Create a certificate request configuration file:

\$ cat \> *\[proxy_fqdn\]*\_csr_cfg.txt

\[req\]

default_bits=2048

prompt=no

default_md=sha256

req_extensions=req_ext

distinguished_name=dn

\[ dn \]

C=US

ST=Texas

L=Austin

O=US Department of Veterans Affairs

OU=AITC

CN=*\[proxy_fqdn\]*

emailAddress=admin@<span class="mark">REDACTED</span>

\[ req_ext \]

subjectAltName=@alt_names

\[ alt_names \]

DNS.1=*\[proxy_fqdn\]*

DNS.2=*\[vm2_fqdn\]*

\<ctrl\>d

72. Generate a permanent certificate signing request:

\$ openssl req -out *\[proxy_fqdn\]*\_csr\_*\[yyyymmdd\]*.txt -newkey rsa:2048 -keyout *\[proxy_fqdn\]*\_key.txt -new -sha256 -nodes -config *\[proxy_fqdn\]*\_csr_cfg.txt

Generating a 2048 bit RSA private key

.......+++

......................+++

writing new private key to '*\[proxy_fqdn\]*\_key.txt'

-----

73. Submit the certificate signing request to VA PKI to obtain a permanent certificate.
74. Save the permanent certificate in the “certificates” directory:

\$ cat \> /u01/certificates/*\[proxy_fqdn\]*\_cert.pem

75. Paste permanent certificate content.

\<ctrl\>d

76. Generate a *\[proxy_fqdn\]* pkcs12 certificate store:

\$ openssl pkcs12 -export -name *\[proxy_fqdn\]* -in *\[proxy_fqdn\]*\_cert.pem -inkey *\[proxy_fqdn\]\_*key.txt -out *\[proxy_fqdn\]*.p12

Enter Export Password: \####

Verifying - Enter Export Password: \####

77. Generate *\[proxy_fqdn\]* java keystore:

\$ keytool -importkeystore -deststorepass \######## -destkeypass \######## -destkeystore *\[proxy_fqdn\]*.jks -srckeystore *\[proxy_fqdn\]*.p12 -srcstoretype PKCS12 -srcstorepass \#### -alias *\[proxy_fqdn\]*

78. Import va_root_ca_cert.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias va_root_ca -file va_root_ca_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

79. Import va_internal_subordinate_ca_cert.pem Certificate into *\[proxy_fqdn\]*java keystore:

\$ keytool -import -alias va_internal_subordinate_ca -file va_internal_subordinate_ca_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

80. Import va_root_ca_s2_cert.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias va_root_ca_s2 -file va_root_ca_s2_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

81. Import va_intermediate_ca1_s2_cert.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias va_intermediate_ca1_s2 -file va_intermediate_ca1_s2_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

82. Import va_intermediate_ca2_s2_cert.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias va_intermediate_ca2_s2 -file va_intermediate_ca2_s2_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

83. Import veterans_affairs_device_ca_b2_cert.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias veterans_affairs_device_ca_b2 -file veterans_affairs_device_ca_b2_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

84. Import betrusted_production_ssp_ca_a1_crt.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias betrusted_production_ssp_ca -file betrusted_production_ssp_ca_a1_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

85. Import federal_common_policy_ca_cert.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias federal_common_policy_ca -file federal_common_policy_ca_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

86. Import sqa.services.eauth.<span class="mark">REDACTED</span>\_cert.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias sqa.services.eauth.<span class="mark">REDACTED</span> -file sqa.services.eauth.<span class="mark">REDACTED</span>\_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

87. Import vaww.esrdev.aac.<span class="mark">REDACTED</span>\_cert.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias vaww.esrdev.aac.<span class="mark">REDACTED</span> -file vaww.esrdev.aac.<span class="mark">REDACTED</span>\_cert.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

88. Import vaww.esrstage1a.aac.<span class="mark">REDACTED</span>.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias vaww.esrstage1a.aac.<span class="mark">REDACTED</span> -file vaww.esrstage1a.aac.<span class="mark">REDACTED</span>.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

89. Import vaww.esrstage1b.aac.<span class="mark">REDACTED</span>.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias vaww.esrstage1b.aac.<span class="mark">REDACTED</span> -file vaww.esrstage1b.aac.<span class="mark">REDACTED</span>.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

90. Import vaww.esrspre-prod.aac.<span class="mark">REDACTED</span>.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias vaww.esrpre-prod.aac.<span class="mark">REDACTED</span> -file vaww.esrpre-prod.aac.<span class="mark">REDACTED</span>.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

91. Import das-test.<span class="mark">REDACTED</span>.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias das-test.<span class="mark">REDACTED</span> -file das-test.<span class="mark">REDACTED</span>.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

92. Import das-sqa.<span class="mark">REDACTED</span>.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias das-sqa.<span class="mark">REDACTED</span> -file das-sqa.<span class="mark">REDACTED</span>.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

93. Import das.<span class="mark">REDACTED</span>.pem Certificate into *\[proxy_fqdn\]* java keystore:

\$ keytool -import -alias das.<span class="mark">REDACTED</span> -file das

.<span class="mark">REDACTED</span>.pem -keystore *\[proxy_fqdn\]*.jks

Enter keystore password: \########

Trust this certificate? \[no\]: yes

Certificate was added to keystore

94. Copy certificate artifacts to VM2:

\$ scp *\[proxy_fqdn\]*.jks *\[vm2_fqdn\]*:/u01/certificates

\$ scp *\[vm2_fqdn\]*.p12 *\[vm2_fqdn\]*:/u01/certificates

\$ scp *cacerts \[vm2_fqdn\]*:/u01/certificates

### Create NSS certificate database on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Create a new NSS certificate database:

\$ sudo mv /etc/httpd/alias /etc/httpd/alias_orig

\$ sudo mkdir /etc/httpd/alias

\$ sudo certutil -N -d /etc/httpd/alias

Enter new password: \####

Re-enter password: \####

95. Add server permanent certificate:

\$ sudo pk12util -i *\[proxy_fqdn\]*.p12 -d /etc/httpd/alias -n *\[proxy_fqdn\]*

Enter Password or Pin for "NSS Certificate DB": \####

Enter password for PKCS12 file: \####

pk12util: PKCS12 IMPORT SUCCESSFUL

96. Add certificate chain:

\$ sudo certutil -A -d /etc/httpd/alias -i va_root_ca_s2_cert.pem -t CT,, -n va_root_ca_s2

\$ sudo certutil -A -d /etc/httpd/alias -i va_intermediate_ca1_s2_cert.pem -t CT,, -n va_intermediate_ca1_s2

\$ sudo certutil -A -d /etc/httpd/alias -i va_intermediate_ca2_s2_cert.pem -t CT,, -n va_intermediate_ca2_s2

97. Modify certificate database permissions:

\$ sudo chmod g+rx,o+rx /etc/httpd/alias

\$ sudo chmod -R g+r,o+r /etc/httpd/alias/\*

98. Verify installed certificates:

\$ certutil -L -d /etc/httpd/alias

99. Create certificate database password file:

\$ cat \> /etc/httpd/conf/password.conf

internal:####

NSS FIPS 140-2 Certificate DB:####

\<ctrl\>d

100. Modify certificate database password file permissions:

\$ sudo chmod g+r,o+r /etc/httpd/conf/password.conf

101. Start HTTPD server

\$ sudo service httpd start

102. Review access_log, error_log, nss_access_log and nss_error_log to ensure TLS is functioning correctly.

### Create NSS certificate database on VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Create a new NSS certificate database:

\$ sudo mv /etc/httpd/alias /etc/httpd/alias_orig

\$ sudo mkdir /etc/httpd/alias

\$ sudo certutil -N -d /etc/httpd/alias

Enter new password: \####

Re-enter password: \####

103. Add server permanent certificate:

\$ sudo pk12util -i *\[vm2_fqdn\]*.p12 -d /etc/httpd/alias -n *\[vm2_fqdn\]*

Enter Password or Pin for "NSS Certificate DB": \####

Enter password for PKCS12 file: \####

pk12util: PKCS12 IMPORT SUCCESSFUL

104. Add certificate chain:

\$ sudo certutil -A -d /etc/httpd/alias -i va_root_ca_s2_cert.pem -t CT,, -n va_root_ca_s2

\$ sudo certutil -A -d /etc/httpd/alias -i va_intermediate_ca1_s2_cert.pem -t CT,, -n va_intermediate_ca1_s2

\$ sudo certutil -A -d /etc/httpd/alias -i va_intermediate_ca2_s2_cert.pem -t CT,, -n va_intermediate_ca2_s2

105. Modify certificate database permissions:

\$ sudo chmod g+rx,o+rx /etc/httpd/alias

\$ sudo chmod -R g+r,o+r /etc/httpd/alias/\*

106. Verify installed certificates:

\$ certutil -L -d /etc/httpd/alias

107. Create certificate database password file:

\$ cat \> /etc/httpd/conf/password.conf

internal:####

NSS FIPS 140-2 Certificate DB:####

\<ctrl\>d

108. Modify certificate database password file permissions:

\$ sudo chmod g+r,o+r /etc/httpd/conf/password.conf

109. Start HTTPD server

\$ sudo service httpd start

110. Review access_log, error_log, nss_access_log and nss_error_log to ensure TLS is functioning correctly.

### NSS Configuration on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

6\. cp /tmp/INB_ERX1.0/downloads/WLSPlugin12.1.3-Apache2.2-Apache2.4-Linux_x86_64/lib/mod_wl_24.so /etc/httpd/modules/ - Need Linux SA assistance.

> **NOTE:** we are using mod_wl_24.so instead of mod_wl.so since Apache on this server is Apache v2.4

7\.

\- Changed From LoadModule weblogic_module modules/mod_wl.so To LoadModule weblogic_module modules/mod_wl_24.so

\- remove “#exit”

8\. Remove this step as we will run Apache commands as WebLogic.

9\. Replace with

\- sudo systemctl status httpd.service

\- sudo systemctl stop httpd.service

\- sudo systemctl start httpd.service

The following steps need to be performed on VM1 and VM2:

1.  Rename the RPM default ssl.conf file to ssl.conf_orig to prevent Apache from loading during startup.

\$ sudo mv ssl.conf ssl.conf_orig

111. Modify NSS configuration:

\$ sudo vi /etc/httpd/conf.d/nss.conf

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

9.  Save the nss.conf file.
112. Start HTTPD server

\$ sudo service httpd start

113. Review access_log, error_log, nss_access_log and nss_error_log to ensure TLS is functioning correctly.

### NSS Configuration on VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

6\. cp /tmp/INB_ERX1.0/downloads/WLSPlugin12.1.3-Apache2.2-Apache2.4-Linux_x86_64/lib/mod_wl_24.so /etc/httpd/modules/ - Need Linux SA assistance.

> **NOTE:** we are using mod_wl_24.so instead of mod_wl.so since Apache on this server is Apache v2.4

7\.

\- Changed From LoadModule weblogic_module modules/mod_wl.so To LoadModule weblogic_module modules/mod_wl_24.so

\- remove “#exit”

8\. Remove this step as we will run Apache commands as WebLogic.

9\. Replace with

\- sudo systemctl status httpd.service

\- sudo systemctl stop httpd.service

\- sudo systemctl start httpd.service

The following steps need to be performed on VM1 and VM2:

1.  Rename the RPM default ssl.conf file to ssl.conf_orig to prevent Apache from loading during startup.

\$ sudo mv ssl.conf ssl.conf_orig

114. Modify NSS configuration:

\$ sudo vi /etc/httpd/conf.d/nss.conf

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

6.  Modify NSSProtocol parameters:

> \#NSSProtocol SSLv3,TLSv1.0,TLSv1.1

> NSSProtocol TLSv1.1,TLSv1.2

7.  Modify NSSNickname parameter:

> \#NSSNickname Server-Cert

> NSSNickname *\[proxy_fqdn\]*

> NSSEnforceValidCerts off

8.  Save the nss.conf file.
115. Start HTTPD server

\$ sudo service httpd start

116. Review access_log, error_log, nss_access_log and nss_error_log to ensure TLS is functioning correctly.

### Install Apache Plug-in for WebLogic on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps need to be performed on VM1 and VM2:

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

117. Create downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

118. Download Oracle WLS Plugin 12.1.3 archive (v44415-01) to the downloads directory:

Download from AITC IEP eRx Downloads directory

119. Unzip the Oracle WLS Plugin 12.1.3 archive to in the downloads directory:

\$ unzip fmw_12_1_3_0_wls_plugin_v44415-01.zip

\$ unzip WLSPlugins12c-12.1.3.zip WLSPlugin12.1.3-Apache2.2-Apache2.4-Linux_x86_64.zip

\$ mkdir WLSPlugin12.1.3-Apache2.2-Apache2.4-Linux_x86_64

\$ unzip WLSPlugin12.1.3-Apache2.2-Apache2.4-Linux_x86_64.zip \\  
-d WLSPlugin12.1.3-Apache2.2-Apache2.4-Linux_x86_64

\$ chmod -R o+rx WLSPlugin12.1.3-Apache2.2-Apache2.4-Linux_x86_64

\$ exit

120. You should be back in your normal Linux login account.
121. Copy the Apache Plug-in for WebLogic libraries to the Linux system library directory (the following must be performed by a system administrator):

\$ sudo cp /u01/downloads/WLSPlugin12.1.3-Apache2.2-Apache2.4-Linux_x86_64/lib/mod\_\* \\

/usr/lib64/httpd/modules

### Configure Apache Plug-in for WebLogic on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps need to be performed on VM1 and VM2:

1.  Log into Linux and sudo su to the root account:

\$ sudo su -

\# cat \> /etc/httpd/conf.d/weblogic.conf

LoadModule weblogic_module modules/mod_wl.so

\<IfModule weblogic_module\>

WebLogicCluster *\[vm1_fqdn\]*:8001, *\[vm2_fqdn\]*:8001

MatchExpression /\*

WLExcludePathOrMimeType /cpanel/\*

WLIOTimeoutSecs 300

WLProxySSL OFF

WebLogicSSLVersion TLSv1_1 TLSv1_2

WLSocketTimeoutSecs 2

DebugConfigInfo ON

\</IfModule\>

\<CTRL\>\<d\>

\# exit

122. You should be back in your normal Linux login account.
123. Restart Apache

\$ sudo service httpd stop

\$ sudo service httpd start

124. Review access_log, error_log, nss_access_log and nss_error_log to ensure Apache is functioning correctly.

### Configure Apache Plug-in for WebLogic on VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps need to be performed on VM1 and VM2:

1.  Log into Linux and sudo su to the root account:

\$ sudo su -

\# cat \> /etc/httpd/conf.d/weblogic.conf

LoadModule weblogic_module modules/mod_wl.so

LoadModule weblogic_module modules/mod_wl_24.so

\<IfModule weblogic_module\>

WebLogicCluster *\[vm1_fqdn\]*:8001, *\[vm2_fqdn\]*:8001

MatchExpression /\*

WLExcludePathOrMimeType /cpanel/\*

WLExcludePathOrMimeType /inbound/\*

WLIOTimeoutSecs 300

WLProxySSL OFF

WebLogicSSLVersion TLSv1_1 TLSv1_2

WLSocketTimeoutSecs 2

DebugConfigInfo ON

\</IfModule\>

\<CTRL\>\<d\>

\# exit

125. You should be back in your normal Linux login account.
126. Restart Apache

\$ sudo service httpd stop

\$ sudo service httpd start

127. Review access_log, error_log, nss_access_log and nss_error_log to ensure Apache is functioning correctly.

### Create IEP CPanel on VM1 and VM2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

128. Create downloads directory if it doesn’t exist:

\$ mkdir -p /u01/deployments

129. Download the CPanel Archive (cpanel_yyyymmdd.tgz) to the deployments directory:

Download from AITC IEP eRx Deploymentss directory

\$ exit

130. You should be back in your normal Linux login account.
131. Unpack the CPanel Archive from the root (/) directory:

\$ cd /

\$ sudo tar xvf /u01/deployments/cpanel_yyyymmdd.tgz

### Install Apache SSOi Web Agent on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Start Xming or other X Server on your Windows Desktop/Laptop. Connect to the server using Putty. The DISPLAY environment variable should be set.
132. Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

133. Create downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

134. Download CA SiteMinder Apache Web Agent (smwa-12.51-cr07-linux-x86-64.zip) to the downloads directory:

Download from AITC IEP eRx Downloads directory

135. Unzip the CA SiteMinder Apache Web Agent archive to in the downloads directory:

\$ cd /u01/downloads

\$ unzip smwa-12.51-cr07-linux-x86-64.zip –d smwa-12.51-cr07-linux-x86-64

\$ chmod o+rx smwa-12.51-cr07-linux-x86-64

\$ chmod o+r smwa-12.51-cr07-linux-x86-64/layout.properties

\$ chmod ugo+rx smwa-12.51-cr07-linux-x86-64/ca-wa-12.51-cr07-linux-x86-64.bin

\$ exit

136. You should be back in your normal Linux login account.
137. Execute the CA SiteMinder Apache Web Agent installer (the following must be performed by a system administrator):

\$ sudo /u01/downloads/smwa-12.51-cr07-linux-x86-64/ca-wa-12.51-cr07-linux-x86-64.bin -i console

138. Press \<Enter\> to continue installing in Console mode:

PRESS \<ENTER\> TO CONTINUE: \<ENTER\>

139. Press \<Enter\> many times to scroll through license agreement:

PRESS \<ENTER\> TO CONTINUE: \<ENTER\>

140. Enter “Y” to accept license agreement:

DO YOU ACCEPT THE TERMS OF THIS LICENSE AGREEMENT? (Y/N): Y

141. Enter installation path:

ENTER AN ABSOLUTE PATH, OR PRESS \<ENTER\> TO ACCEPT THE DEFAULT

: /u01/app/CA/webagent

142. Confirm installation path:

INSTALL FOLDER IS: /u01/app/webagent

IS THIS CORRECT? (Y/N): Y

143. Confirm installation details:

Please Review the Following Before Continuing:

Product Name:

CA SiteMinder Web Agent

Install Folder:

/u01/app/webagent

Disk Space Information (for Installation Target):

Required: 300,510,677 Bytes

Available: 60,435,013,632 Bytes

PRESS \<ENTER\> TO CONTINUE: \<ENTER\>

144. Confirm exit from installer:

PRESS \<ENTER\> TO EXIT THE INSTALLER: \<ENTER\>

### Configure Apache SSOi Web Agent on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into Linux and sudo su to the root account (the following must be performed by a system administrator):

\$ sudo su -

145. Change directory to the agent home and "source" the Siteminder environment:

\# cd /u01/app/CA/webagent

\# . ./ca_wa_env.sh

146. Change to install config info directory and launch the configuration wizard:

\# cd install_config_info

\# ./ca-wa-config.sh -i console

147. Type 1 to register the trusted host, then Press Enter

-\>1- Yes, I would like to do Host Registration now.

2- No, I would like to do Host Registration later.

ENTER A COMMA-SEPARATED LIST OF NUMBERS REPRESENTING THE DESIRED CHOICES, OR

PRESS \<ENTER\> TO ACCEPT THE DEFAULT: 1

148. In the Admin User Name prompt, type threg then press Enter

Enter the name of an administrator who has the right to register trusted hosts

with the Policy Server.

This entry must match the name of an administrator defined in the Policy

Server.

Admin User Name (Default: ): threg

149. For Shared Secret Rollover, type n then press Enter

Enable Shared Secret Rollover (y/n) (Default: n): n

150. Type the threg password then press Enter

Enter the password of an administrator who has the right to register trusted

hosts with the Policy Server. This entry must match the name of an

administrator defined in the Policy Server.:

Confirm Admin Password: \<- va1234!

151. Type the Trusted Host Name then press Enter

Specify the name of the host you want to register with the Policy Server.

Enter the name of the host configuration object. The name must match a host

configuration object name already defined on the Policy Server.

Trusted Host Name (Default: ): *\[proxy_fqdn\]*

152. Type the Host Configuration Object then press Enter

Host Configuration Object (Default: ): *\[iam_hco\]*

153. Type the Policy Server IP Address then press Enter

Policy Server IP Address

------------------------

Enter the IP Address of the Policy Server where you are registering this host.

Policy Server IP Address (Default: ): *\[iam_policy\]*

154. In the FIPS Mode Settings, select 3 then press Enter

FIPS Mode Setting

-----------------

-\>1- FIPS Compatibility Mode

2- FIPS Migration Mode

3- FIPS Only Mode

ENTER THE NUMBER FOR YOUR CHOICE, OR PRESS \<ENTER\> TO ACCEPT THE DEFAULT:: 3

155. Press Enter twice to accept the default file name and location of Host configuration

Host Configuration file location

--------------------------------

Enter file name (Default: SmHost.conf):

Enter location (Default: /u01/app/CA/webagent/config):

156. Select 1 for Apache Web Server, then press Enter

Select Web Server(s)

--------------------

1- Apache Web Server

2- Domino Web Server

-\>3- iPlanet or Sun ONE Web Server

ENTER A COMMA-SEPARATED LIST OF NUMBERS REPRESENTING THE DESIRED CHOICES, OR

PRESS \<ENTER\> TO ACCEPT THE DEFAULT: 1

157. Specify the path to apache instance /home/apache/httpd

Apache Web Server path

----------------------

Enter the root path of where Apache Web server installed.

Please enter path (Default: ): /etc/httpd

158. Select the Apache version, type 3 then press Enter

Apache Version

--------------

Please select a choice for the Apache version.

1- Apache version 1.x

2- Apache version 2.x

3- Apache version 2.2.x

4- Apache version 2.4.x

ENTER THE NUMBER OF THE DESIRED CHOICE: 4

159. Select the Apache Type, type 6 then press Enter

Apache Server Type

------------------

Please select one of the following appropriately match your previous selection

1- Oracle HTTP Server

2- IBM HTTP Server

3- HP Apache

4- ASF/RedHat Apache

5- RedHat JWS HTTP Server

ENTER THE NUMBER OF THE DESIRED CHOICE: 4

160. Type 1 to confirm the Apache version

Select Web Server(s)

--------------------

1- \[\] Apache 2.2.15

Select the web server(s) you wish to preserve or configure/reconfigure as

Web Agent(s). Enter a comma-separated list of numbers representing the

desired choices. Already configured web servers are marked as \[x\] in the

above list, you can un-configure or skip these web servers in next steps by

not listing them in comma-separated list here.: 1

161. Type the Agent Configuration Object, then press Enter

Agent Configuration Object

--------------------------

Enter the name of an Agent Configuration Object that defines the configuration

parameters which the Web Agent will use for Apache 2.2.15.

Agent Configuration Object (Default: AgentObj): PREAgentConfig

162. To select Basic over SSL Authentication, Type 1 then press Enter

SSL Authentication

------------------

The following SSL configurations are available for this web server. If the

Web Agent will be providing advanced authentication, select which

configuration it will use to configure Apache 2.2.15.

-\>1- HTTP Basic over SSL

2- X509 Client Certificate

3- X509 Client Certificate and HTTP Basic

4- X509 Client Certificate or HTTP Basic

5- X509 Client Certificate or Form

6- X509 Client Certificate and Form

7- No advanced authentication

ENTER THE NUMBER FOR YOUR CHOICE, OR PRESS \<ENTER\> TO ACCEPT THE DEFAULT:: 1

163. Type 1 on the Webagent Enable prompt then press Enter

Webagent Enable option

----------------------

Please select Yes to Enable the WebAgent

1- Yes

-\>2- No

ENTER THE NUMBER FOR YOUR CHOICE, OR PRESS \<ENTER\> TO ACCEPT THE DEFAULT:: 1

164. On the Summary Screen, Type 1 then press Enter

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

165. Continue installation if ssl.conf file doesn’t exist:

1- Continue

2- Exit

Unable to process configuration. File /etc/httpd/conf.d/ssl.conf doesnt

exist. Please make sure the configuration path is valid.

Please select a choice.: 1

166. Confirm exit from installer:

PRESS \<ENTER\> TO EXIT THE INSTALLER: \<ENTER\>

167. Enter “exit” to log out of root account:

\# exit

168. You should be back in your normal Linux login account.

### Post Configure Edits for Apache SSOi Web Agent on VM1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into Linux and sudo su to the root account:

\$ sudo su -

169. Edit /u01/app/CA/webagent/config/SmHost.conf:

vi /u01/app/CA/webagent/config/SmHost.conf

170. Verify policyserver entries:

\# Add additional bootstrap policy servers here for fault tolerance.

*\[iam_policy_servers\]*

171. Edit /etc/httpd/conf/WebAgent.conf:

vi /etc/httpd/conf/WebAgent.conf

172. Enable the agent:

EnableWebAgent=”YES”

173. For an embedded Apache web server (included by default) on a RedHat Linux system, modify certain configuration files to accommodate the product first. Follow these steps:.

cp /etc/sysconfig/httpd /etc/sysconfig/httpd.orig

vi /etc/sysconfig/httpd

Add the following line to the end of the file:

PATH=\$PATH:web_agent_home/bin

Save the changes and close the text editor.

174. Source ca_wa_env.sh script in the following file (instead of starting it manually each time):

cp /etc/init.d/httpd /etc/init.d/httpd.orig

vi /etc/init.d/httpd

Add the following code snippet after the similar snippet for /etc/sysconfig/httpd

\# Source CA Webagent environment

if \[ -f /u01/app/CA/webagent/ca_wa_env.sh \]; then

. /u01/app/CA/webagent/ca_wa_env.sh

fi

175. Modify the apachectl script to set the webagent environment variables:

cp /usr/sbin/apachectl /usr/sbin/apachectl.orig

vi /usr/sbin/apachectl

Locate a line resembling the following example:

\# Source /etc/sysconfig/httpd for \$HTTPD setting, etc

Add the following code snippet after the similar snippet for /etc/sysconfig/httpd/:

\# Source CA Webagent environment

if \[ -r /u01/app/CA/webagent/ca_wa_env.sh \]; then

. /u01/app/CA/webagent/ca_wa_env.sh

fi

176. Modify permission of CA SmHost.conf file

\# chmod 666 /u01/app/CA/webagent/config/SmConf.conf

177. Create /opt/ca/webagent symbolic link

\# mkdir /opt/ca

\# chmod 755 /opt/ca

\# ln -s /u01/app/CA/webagent/ /opt/ca/webagent

178. Modify ownership and permission of CA Webagent log files

\# chown apache:apache /u01/app/CA/webagent/log

\# chmod 777 /u01/app/CA/webagent/log

179. Modify trace file verbocity

     Modify SSOi WebAgent trace.conf file:

\# cd /opt/ca/webagent/config

\# vi trace.conf

Modify lines near the bottom per the following:

nete.enableConsoleLog=0

nete.enableFileLog=0

nete.logFile=0

nete.conapi.logLevel=0

nete.conapi.ipc.logLevel=0

nete.conapi.tcpip.logLevel=0

nete.mon.monitoringApiLogLevel=0

Modify SSOi WebAgent WebAgentTrace.conf file:

\# vi WebAgentTrace.conf

Modify lines neer the bottom to be:

components: WebAgent

data: Date, Time, Pid, Function, TransactionID, User, Message

180. Modify sysctl for Apache on RHEL 7.

> Open a text file for sysctl properties:

> dzdo systemctl edit httpd.service

> Insert the following:

> *\[Service\]*

> *ExecStart=*

> *ExecReload=*

> *ExecStart=/bin/bash -a -c 'source /u01/CA/webagent/ca_wa_env.sh && exec /usr/sbin/httpd \$OPTIONS -DFOREGROUND'*

> *ExecReload=/bin/bash -a -c 'source /u01/CA/webagent/ca_wa_env.sh && exec /usr/sbin/httpd \$OPTIONS -k graceful'*

> Close and save.

> This will create /etc/systemd/system/httpd.service.d/override.conf.

> Reload the deamon:

> dzdo systemctl daemon-reload

> httpd should come up with a normal start command.

> If a “file not found” error occurs, file “ca_wa_env.sh” may be in a different location.

> These files can get installed in different locations across different systems.

> If this is the case, execute a find command:

> dzdo find / -name ‘ca_wa_env.sh’

> If ‘ca_wa_env.sh’ is not found, search for “set-apache-env.sh”.

> dzdo find / -name ‘set-apache-env.sh’

> Update override.conf with the correct path.

> Reload the deamon:

> dzdo systemctl daemon-reload

> Verify system is functioning correctly.

181. Restart Apache and check the logs for connection or errors.

\# exit

\$ sudo service httpd stop

\$ sudo service httpd start

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

This section provides step-by-step instructions for installing all components of the Inbound eRx software on all platforms.

### WebLogic Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections describe the steps to install the WebLogic application server. Most activities are to be performed by the WebLogic Administrator.

#### Install WebLogic

1.  Log into Linux and sudo to the weblogic account as follows:

\$ sudo su - weblogic

182. Modify the weblogic Linux account .bash_profile, replace the PATH= and export PATH with the following near the end of the file:

export JAVA_HOME=/u01/app/java/latest

export PATH=\${JAVA_HOME}/bin:\${PATH}:\${HOME}/bin

183. Exit weblogic account:

\$ exit

184. Start Xming or other X Server on your Windows Desktop/Laptop. Connect to the server using Putty. The DISPLAY environment variable should be set.
185. Log into Linux and modify your .Xauthority permissions:

\$ chmod 755 ~

\$ chmod 644 ~/.Xauthority

186. Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

187. Copy the .Xauthority file from your normal Linux account to the current account:

\$ cp ~yourusername/.Xauthority .

188. Create downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

189. Download Oracle WLS 12.1.3 installer (v44413-01) to the downloads directory:

Download from AITC IEP eRx Downloads directory

190. Unzip the Oracle WLS 12.1.3 installer to the downloads directory:

\$ unzip fmw_12.1.3.0.0_wls_v44413-01.zip

191. Run the Oracle WLS 12.1.3 installer:

\$ java -jar fmw_12.1.3.0.0_wls.jar

192. Enter “y” to accept prerequisite checks.
193. Enter “/u01/app/oraInventory”.
194. Select OK.

> <span id="_Toc29569549" class="anchor"></span>Figure 3: Install WebLogic – Oracle Fusion Middleware Installation Inventory Setup

> ![](pso-7-589-inbound-eprescribing-dibr/004.png)

195. The Oracle Universal Installer will appear for a few moments.

> <span id="_Toc29569550" class="anchor"></span>Figure 4: Install WebLogic – Oracle Universal Installer Dialog Box

> ![](pso-7-589-inbound-eprescribing-dibr/005.png)

196. Once the installer is complete, select Next.

> <span id="_Toc29569551" class="anchor"></span>Figure 5: Install WebLogic – Oracle Fusion Middleware WebLogic Server and Coherence Installer

> ![](pso-7-589-inbound-eprescribing-dibr/006.png)

197. Enter *Oracle Home*: “*\[ORACLE_BASE\]*”.
198. Select Next.

> <span id="_Toc29569552" class="anchor"></span>Figure 6: Install WebLogic – Installation Location

> ![](pso-7-589-inbound-eprescribing-dibr/007.png)

199. For *Installation Type*, select the *WebLogic Server* radio button.
200. Select Next.

> <span id="_Toc29569553" class="anchor"></span>Figure 7: Install WebLogic – Installation Type

> ![](pso-7-589-inbound-eprescribing-dibr/008.png)

201. Select Next again on the Prerequisite Checks screen.

> <span id="_Toc29569554" class="anchor"></span>Figure 8: Install WebLogic – Prerequisite Checks

> ![](pso-7-589-inbound-eprescribing-dibr/009.png)

202. On the Security Updates screen, leave the *Email* field blank.
203. Uncheck “I wish to receive security updates via My Oracle Support”.
204. Select Next.

> <span id="_Toc29569555" class="anchor"></span>Figure 9: Install WebLogic – Security Updates Screen

> ![](pso-7-589-inbound-eprescribing-dibr/010.png)

205. Select Yes to acknowledge not receiving critical security issues notifications.

> <span id="_Toc29569556" class="anchor"></span>Figure 10: Install WebLogic – My Oracle Support Username/Email Address Not Specified Dialog Box

> ![](pso-7-589-inbound-eprescribing-dibr/011.png)

206. On the *Installation Summary* screen, select Install.

> <span id="_Toc29569557" class="anchor"></span>Figure 11: Install WebLogic – Installation Summary Screen

> ![](pso-7-589-inbound-eprescribing-dibr/012.png)

207. Wait while the installation progresses.
208. Once the installation is complete, the following screen will display.
209. Select Next.

> <span id="_Toc29569558" class="anchor"></span>Figure 12: Install WebLogic – Installation Progress Screen

> ![](pso-7-589-inbound-eprescribing-dibr/013.png)

210. On the Installation Complete screen, leave *Automatically Launch the Configuration Wizard* checked.
211. Select Finish.

> <span id="_Toc29569559" class="anchor"></span>Figure 13: Install WebLogic – Installation Complete

> ![](pso-7-589-inbound-eprescribing-dibr/014.png)

212. The Oracle Configuration Wizard splash screen will appear for a few moments.

> <span id="_Toc29569560" class="anchor"></span>Figure 14: Install WebLogic – Oracle Configuration Wizard Splash Screen

> ![](pso-7-589-inbound-eprescribing-dibr/015.png)

213. On the Configuration Type screen, select *Create a new domain*.
214. Enter the following in the *Domain Location*:

*\[ORACLE_BASE\]/*user_projects/domains/*\[domain\]*

215. Select Next.

> <span id="_Toc29569561" class="anchor"></span>Figure 15: Install WebLogic – Create New Domain

> ![](pso-7-589-inbound-eprescribing-dibr/016.png)

216. On the Templates screen, select the *Create Domain using Product Templates* radio button.
217. Under *Available Templates*, select “Basic WebLogic Server Domain”.
218. Select Next.

> <span id="_Toc29569562" class="anchor"></span>Figure 16: Install WebLogic – Templates Screen

> ![](pso-7-589-inbound-eprescribing-dibr/017.png)

219. On the Administrator Account screen, enter *Name*: “weblogic”
220. Enter *Password*: “xxxxxxxx”
221. Enter *Confirm Password*: “xxxxxxxx”
222. Select Next.

> <span id="_Toc29569563" class="anchor"></span>Figure 17: Install WebLogic – Administrator Account Screen

> ![](pso-7-589-inbound-eprescribing-dibr/018.png)

223. On the Domain Mode and JDK screen, select the *Development* radio button for the *Domain Mode*.
224. For *JDK*, select the *Oracle HotSpot 1.8.0_xxx* radio button.
225. Select Next.

> <span id="_Toc29569564" class="anchor"></span>Figure 18: Install WebLogic - Domain Mode and JDK

> ![](pso-7-589-inbound-eprescribing-dibr/019.png)

226. On the Advanced Configuration screen, check *Administration Server, Node Manager*, and *Managed Servers, Clusters and Coherence*.
227. Select Next.

> <span id="_Toc29569565" class="anchor"></span>Figure 19: Install WebLogic– Advanced Configuration

> ![](pso-7-589-inbound-eprescribing-dibr/020.png)

228. On the Administration Server screen, enter *Server Name*: “AdminServer”
229. Enter *Listen Address*: “All Local Addresses”
230. Enter *Listen Port*: “7001”
231. Uncheck the check box for *Enable SSL*.
232. Leave the *SSL Listen Port* field blank.
233. Select Next.

> <span id="_Toc29569566" class="anchor"></span>Figure 20: Install WebLogic – Administration Server Screen

> ![](pso-7-589-inbound-eprescribing-dibr/021.png)

234. On the Node Manager screen, select the *Per Domain Default Location* radio button.
235. Enter *Username*: “weblogic”
236. Enter *Password*: “xxxxxxxx”
237. Enter *Confirm Password*: “xxxxxxxx”
238. Select Next.

> <span id="_Toc29569567" class="anchor"></span>Figure 21: Install WebLogic – Node Manager

> ![](pso-7-589-inbound-eprescribing-dibr/022.png)

239. On the Managed Servers screen, select Add.
240. Enter the *Server Name*: “erx1”
241. Enter the *Listen Address*: *\[vm1_fqdn\]*
242. Enter *Listen Port*: “8001”
243. Leave *Enable SSL* unchecked.
244. Leave *SSL Listen Port* empty (Disabled).
245. Select Add.
246. Enter *Server Name*: “erx2”
247. Enter *Listen Address*: *\[vm2_fqdn\]*
248. Enter Listen Port: “8001”
249. Leave *Enable SSL* unchecked.
250. Leave *SSL Listen Port* empty (Disabled).
251. Select Next.

> <span id="_Toc29569568" class="anchor"></span>Figure 22: Install WebLogic – Managed Servers

> ![](pso-7-589-inbound-eprescribing-dibr/023.png)

252. On the Clusters screen, select Add.
253. Enter *Cluster Name*: “erx”
254. Enter *Cluster Address*: “*\[vm1_fqdn\]*:*\[erx_port\]*, *\[vm2_fqdn*\]:*\[erx_port\]*”
255. Enter *Frontend Host*: “*\[proxy_fqdn\]*”
256. Enter *Frontend HTTP Port*: “80”
257. Enter *Frontend HTTPS*: “443”
258. Select Next.

> <span id="_Toc29569569" class="anchor"></span>Figure 23: Install WebLogic – Clusters

> ![](pso-7-589-inbound-eprescribing-dibr/024.png)

259. Assign “erx1” and “erx2” servers to the “erx” cluster.
260. Select Next.

> <span id="_Toc29569570" class="anchor"></span>Figure 24: Install WebLogic – Assign Servers to Clusters

> ![](pso-7-589-inbound-eprescribing-dibr/025.png)

261. Select Add.
262. Enter *Name*: “machine1”
263. Enter *Node Manager Listen Address*: “*\[vm1_fqdn\]*”
264. Enter *Node Manager Listen Port*: “5556”
265. Enter *Name*: “machine2”
266. Enter *Node Manager Listen Address*: “*\[vm1_fqdn\]*”
267. Enter *Node Manager Listen Port*: “5556”
268. Select Next.

> <span id="_Toc29569571" class="anchor"></span>Figure 25: Install WebLogic – Machines

> ![](pso-7-589-inbound-eprescribing-dibr/026.png)

269. On the Assign Servers to Machines screen, add “AdminServer” on *Servers* panel to “machine1” on *Machines* panel.
270. Add “erx1” on *Servers* panel to “machine1” on *Machines* panel.
271. Add “erx2” on *Servers* panel to “machine2” on *Machines* panel.
272. Select Next.

> <span id="_Toc29569572" class="anchor"></span>Figure 26: Install WebLogic – Assign Servers to Machines

> ![](pso-7-589-inbound-eprescribing-dibr/027.png)

273. On the Configuration Summary screen, select Create to accept the options and start creating and configuring the new domain.

> <span id="_Toc29569573" class="anchor"></span>Figure 27: Install WebLogic – Configuration Summary Screen

> ![](pso-7-589-inbound-eprescribing-dibr/028.png)

274. Once the configuration is complete, select Next.
275. If the configuration is successful, the Configuration Success screen will display as illustrated in the figure below.
276. Select Finish.

> <span id="_Toc29569574" class="anchor"></span>Figure 28: Install WebLogic - Configuration Success

> ![](pso-7-589-inbound-eprescribing-dibr/029.png)

277. The Oracle WebLogic Server 12.1.3 installation and configuration should be complete at this time. To modify the configuration, re-run the configuration wizard:

\$ cd *\[ORACLE_BASE*\]/oracle_common/common/bin

\$ ./config.sh

278. Modify the configuration as needed.

#### Set Temporary Environment on VM1

On VM1, set temporary environment. Remember to amend the DOMAIN_HOME environment variable to match your domain:

\$ export ORACLE_BASE=*\[ORACLE_BASE\]*

\$ export WLS_HOME=\$ORACLE_BASE/wlserver

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

\$ cp startWeblogic.sh startWeblogic_orig.sh

\$ vi startWeblogic.sh

Modify the JAVA_OPTIONS as follows:

JAVA_OPTIONS="\${SAVE_JAVA_OPTIONS} -Dweblogic.security.SSL.minimumProtocolVersion=TLSv1.1”

Enter :wq to save the file and exit vi.

#### Copy Identity/Trust Store Files on VM2

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

Enter :wq to save the file and exit vi.

#### Disable basic authentication

On VM1, edit config.xml to disable basic authentication:

\$ cd \$DOMAIN_HOME/config.xml

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

PRE_CLASSPATH=*\[ORACLE_BASE\]*/oracle_common/modules/javax.persistence_2.1.jar:*\[WLS_HOME\]*/modules/com.oracle.weblogic.jpa21support_1.0.0.0_2-1.jar

export PRE_CLASSPATH

Enter :wq to save the file and exit vi.

#### Create Inbound eRx Datasource

This section provides step-by-step instructions for deploying VistA Link Connector.

1.  Navigate to *Services*, then to *Data Sources*.
279. From the *Data Source*s page, select New.

> <span id="_Toc29569575" class="anchor"></span>Figure 29: Create Inbound eRx Datasource – Datasources

> ![](pso-7-589-inbound-eprescribing-dibr/030.png)

280. Enter *Name*: InboundErxDataSource
281. Enter *JNDI Name*: jdbc/InboundErxDataSource
282. Select *Database Type*: Oracle
283. Select Next.

> <span id="_Toc29569576" class="anchor"></span>Figure 30: Create Inbound eRx Datasource – Datasource Properties

> ![](pso-7-589-inbound-eprescribing-dibr/031.png)

284. Select *Database Driver*: Oracle’s Driver (Thin XA) for Instance connections; Versions: Any
285. Select Next.

> <span id="_Toc29569577" class="anchor"></span>Figure 31: Create Inbound eRx Datasource – Database Driver

> ![](pso-7-589-inbound-eprescribing-dibr/032.png)

286. Select Next.

> <span id="_Toc29569578" class="anchor"></span>Figure 32: Create Inbound eRx Datasource – Transaction Properties

> ![](pso-7-589-inbound-eprescribing-dibr/033.png)

287. Enter *Database Name*: \[DB_NAME\]
288. Enter *Host Name*: \[DB_FQDN\]
289. Enter *JNDI Name*: jdbc/InboundErxDataSource
290. Enter *Port*: \[DB_PORT\]
291. Enter *Password*: \[DB_PASSWORD\]
292. Enter *Confirm Password*: \[DB_PASSWORD\]

> <span id="_Toc29569579" class="anchor"></span>Figure 33: Create Inbound eRx Datasource – Connection Properties

> ![](pso-7-589-inbound-eprescribing-dibr/034.png)

293. Select Test Configuration.
294. If test is not successful, select Back and correct settings, otherwise select Next.

> <span id="_Toc29569580" class="anchor"></span>Figure 34: Create Inbound eRx Datasource – Test Connection

> ![](pso-7-589-inbound-eprescribing-dibr/035.png)

295. Select All servers in the cluster.
296. Select Finish.

> <span id="_Toc29569581" class="anchor"></span>Figure 35: Create Inbound eRx Datasource – Select Targets/Finish

> ![](pso-7-589-inbound-eprescribing-dibr/036.png)

297. Select InboundErxDataSource hyperlink.

> <span id="_Toc29569582" class="anchor"></span>Figure 36: Create Inbound eRx Datasource – Modify New Datasource

> ![](pso-7-589-inbound-eprescribing-dibr/037.png)

298. Select the Connection Pool tab.

> <span id="_Toc29569583" class="anchor"></span>Figure 37: Inbound eRx Datasource –Connection Pool Properties

> ![](pso-7-589-inbound-eprescribing-dibr/038.png)

299. Scroll to the bottom of the Connection Pool page.
300. Select the Advanced hyperlink to expand the advanced properties.

> <span id="_Toc29569584" class="anchor"></span>Figure 38: Inbound eRx Datasource –Connection Pool Advanced Properties

> ![](pso-7-589-inbound-eprescribing-dibr/039.png)

301. Scroll down and uncheck the Wrap Data Types property.

> <span id="_Toc29569585" class="anchor"></span>Figure 39: Inbound eRx Datasource – Wrap Data Type Property

> ![](pso-7-589-inbound-eprescribing-dibr/040.png)

302. Scroll to the bottom of the of the Advanced Connection Pool page.
303. Select Save.

> <span id="_Toc29569586" class="anchor"></span>Figure 40: Inbound eRx Datasource – Save Properties

> ![](pso-7-589-inbound-eprescribing-dibr/041.png)

#### Configure Identity/Trust Store File on Managed Servers

This section provides step-by-step instructions for configuring the identify/trust store file on the managed servers.

1.  Under Domain Structure, navigate to Servers.
2.  Select the erx1 link to access the server configuration page in the Administration Console.

> <span id="_Toc29569587" class="anchor"></span>Figure 41: Configure Identity/Trust Store File – Access Server Configuration Page

> ![](pso-7-589-inbound-eprescribing-dibr/042.png)

304. Under Configuration \> Keystores, select Change.

> <span id="_Toc29569588" class="anchor"></span>Figure 42: Configure Identity/Trust Store File – Change Keystores

> ![](pso-7-589-inbound-eprescribing-dibr/043.png)

305. For *Keystores*, select Custom Identity and Custom Trust.
306. Select Save.

> <span id="_Toc29569589" class="anchor"></span>Figure 43: Configure Identity/Trust Store File – Keystores – Select Custom Identify and Custom Trust

> ![](pso-7-589-inbound-eprescribing-dibr/044.png)

307. Modify the setting under the Keystores tab as illustrated in the figure below. The *Custom Identity Keystore* and *Custom Trust Keystore* use the same file path to the keystore file copied to the Domain “security” directory: (*\[DOMAIN_HOME\]*/security/*\[proxy_fqdn\]*.jks).

> <span id="_Toc29569590" class="anchor"></span>Figure 44: Configure Identity/Trust Store File – Modify Keystore Settings

> ![](pso-7-589-inbound-eprescribing-dibr/045.png)

308. Modify the setting under the SSL tab as illustrated in the figure below. For the *Private Key Alias*, enter \[proxy_fqdn\].
309. Enter and confirm the *Private Key Passphrase*.
310. Select Save.

> <span id="_Toc29569591" class="anchor"></span>Figure 45: Configure Identity/Trust Store File – Modify SSL Settings

> ![](pso-7-589-inbound-eprescribing-dibr/046.png)

311. Navigate to *Servers*, and then select the erx2 link to access the server configuration page in the Administration Console.
312. Repeat the Keystore configuration steps for erx2 as described earlier in this section for erx1.

> <span id="_Toc29569592" class="anchor"></span>Figure 46: Configure Identity/Trust Store File – Managed Server 2 Configuration

> ![](pso-7-589-inbound-eprescribing-dibr/047.png)

313. Navigate to *Servers*, and then select the AdminServer(admin) hyperlink to access the server configuration page.
314. Repeat the Keystore configuration steps for AdminServer(admin) as described earlier in this section for erx1.

> <span id="_Toc29569593" class="anchor"></span>Figure 47: Configure Identity/Trust Store File – Admin Server Configuration

> ![](pso-7-589-inbound-eprescribing-dibr/048.png)

315. Navigate to *Servers*, and then select the AdminServer(admin) hyperlink to access the server configuration page.

> <span id="_Toc29569594" class="anchor"></span>Figure 48: Configure Identity/Trust Store File – Admin Server Configuration

> ![](pso-7-589-inbound-eprescribing-dibr/049.png)

316. Under Configuration and General tabs:
     1.  Check Listen Port Enabled
     2.  Enter *Listen Port:*7001
     3.  Check SSL Port Enabled
     4.  Enter *SSL Listen Port:*7002
     5.  Select Save.

> <span id="_Toc29569595" class="anchor"></span>Figure 49: Configure Identity/Trust Store File – Admin Server Configuration

> ![](pso-7-589-inbound-eprescribing-dibr/050.png)

#### Pack Domain on VM1

This section provides step-by-step instructions for packing the domain on VM1:

1.  On VM1, stop the newly created domain.
2.  In the session that is currently running “startWebLogic.sh”, enter \<CTRL\> C.
3.  The log messages should indicate that the Admin Server “was shut down”.
2.  It may seem odd that we are immediately stopping the new domain, but some of the configuration is not written to the file system until the AdminServer is started for the first time.
4.  Transfer the relevant configuration using the pack and unpack utilities.
5.  On VM1, pack the domain configuration using the following commands. Remember to amend the DOMAIN_HOME environment variable and the -template_name parameter to match your domain.

\$ mkdir /u01/templates

\$ chmod 777 /u01/templates

\$ \$WLS_HOME/common/bin/pack.sh -managed=true -domain=\$DOMAIN_HOME -template=/u01/templates/erxdomain1_template.jar -template_name=*\[domain\]* -log=/u01/templates/*\[domain\]\_*template_pack.log

317. Copy the resulting jar file to VM2 under:

/u01/templates

#### Unpack Domain on VM2

On VM2, set temporary environment. Remember to amend the DOMAIN_HOME environment variable to match your domain:

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

318. On VM2, start WLST.

\$ \$WLS_HOME/common/bin/wlst.sh

319. Connect to the administration server on VM1, enroll VM2, disconnect and exit WLST. Remember to amend the DOMAIN_HOME environment variable to match your domain.

\> connect('weblogic', '########', 't3s://*\[vm1_fqdn\]*:7002')

\> nmEnroll('*\[DOMAIN_HOME\]*', '*\[DOMAIN_HOME\]*/nodemanager')

\> disconnect()

\> exit()

320. Check that the “\$ORACLE_BASE/domain-registry.xml” file contains an entry like the following. If it doesn't, add it manually.

\<domain location="*\[DOMAIN_HOME\]*"/\>

321. Check that the “\$DOMAIN_HOME/nodemanager/nodemanager.domains” file contains an entry like the following. If it doesn't, add it manually.

erxdomain1=*\[DOMAIN_HOME\]*

322. If the node manager has not been started already on this server, start it now.

\$ nohup \$DOMAIN_HOME/bin/startNodeManager.sh &

#### Check Node Manager on Each WebLogic Machine

This section outlines the steps for checking that the node manager is reachable on each WebLogic machine.

1.  Log in to the administration server (http://*\[vm1_fqdn\]*:7001/console).
323. In the *Domain Structure* tree, expand the *Environment* node and then select the *Machines* node.
324. In the right-hand pane, select on the first WebLogic machine (machine1).
325. Select the Monitoring tab. Be patient. This may take some time the first time it’s done.
326. If the status is “Reachable”, everything is fine.
327. Repeat for the second WebLogic machine (machine2).

#### Create a Boot Identity File for Managed Servers

3.  This is a placeholder step that may be eliminated if the boot identity file is automatically copied over during the domain clone process.

On VM2, create a boot identity file for the domain if it doesn’t exist:

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

328. Copy test application to the deployments directory:

\$ cp /u01/downloads/benefits.war /u01/deployments

329. Navigate to the *Deployments* page.

> <span id="_Toc29569596" class="anchor"></span>Figure 50: Deploy Test Application: Deployments Page

> ![](pso-7-589-inbound-eprescribing-dibr/051.png)

330. From the *Deployments* page, select Install.

> <span id="_Toc29569597" class="anchor"></span>Figure 51: Deploy Test Application – Install

> ![](pso-7-589-inbound-eprescribing-dibr/052.png)

331. Install a new deployment of the test application using the WAR file as indicated in the figure below.
332. Select Next.

> <span id="_Toc29569598" class="anchor"></span>Figure 52: Deploy Test Application – WAR File

> ![](pso-7-589-inbound-eprescribing-dibr/053.png)

333. Accept the defaults for an application deployment. (The *Install this deployment as an application* radio button is marked.)
334. Select Next.

> <span id="_Toc29569599" class="anchor"></span>Figure 53: Deploy Test Application – Accept Default Application Deployment

> ![](pso-7-589-inbound-eprescribing-dibr/054.png)

335. Select the All servers in the cluster option under the “erx” cluster as the target for the deployment.
336. Select Next.

> <span id="_Toc29569600" class="anchor"></span>Figure 54: Deploy Test Application – Select Deployment Target

> ![](pso-7-589-inbound-eprescribing-dibr/055.png)

337. All of the values should appear as illustrated in the figure below.
338. Select Next.

> <span id="_Toc29569601" class="anchor"></span>Figure 55: Deploy Test Application – Verify Deployment Settings

> ![](pso-7-589-inbound-eprescribing-dibr/056.png)

339. Verify that all of the values appear as illustrated in the figure below.
340. Select Finish.

> <span id="_Toc29569602" class="anchor"></span>Figure 56: Deploy Test Application – Verify Deployment Settings (Finish)

> ![](pso-7-589-inbound-eprescribing-dibr/057.png)

341. The Overview tab should appear as illustrated in the figure below.

> <span id="_Toc29569603" class="anchor"></span>Figure 57: Deploy Test Application – Verify “benefits” Settings

> ![](pso-7-589-inbound-eprescribing-dibr/058.png)

342. Navigate to the Servers page in the WebLogic console.
343. Select the Control tab.
344. Select erx1 and erx2 servers.
345. Select Start.

> <span id="_Toc29569604" class="anchor"></span>Figure 58: Deploy Test Application – Summary of Servers Table

> ![](pso-7-589-inbound-eprescribing-dibr/059.png)

346. After a couple minutes, the state on the servers will change to RUNNING.

> <span id="_Toc29569605" class="anchor"></span>Figure 59: Deploy Test Application – Servers Running

> ![](pso-7-589-inbound-eprescribing-dibr/060.png)

347. Open a web browser to http://*\[vm1_fqdn\]*/benefits/.
348. The Dizzyworld Benefits application will display.

> <span id="_Toc29569606" class="anchor"></span>Figure 60: Deploy Test Application – Open Dizzyworld Benefits Application

> ![](pso-7-589-inbound-eprescribing-dibr/061.png)

349. Repeat Steps 22 and 23 with a Web browser pointed to http://*\[vm2_fqdn\]*/benefits/.
350. Repeat Steps 22 and 23 with a Web browser pointed to https://*\[proxy_fqdn\]*/benefits/.
351. Navigate to the Servers page in the WebLogic console.
352. Select the Control tab.
353. Select erx1 and erx2 servers.
354. Select Shutdown.

> <span id="_Toc29569607" class="anchor"></span>Figure 61: Deploy Test Application – Shutdown Servers

> ![](pso-7-589-inbound-eprescribing-dibr/062.png)

#### Configure JPA for Domain on VM2

On VM2, edit setDomainEnv.sh script to add JPA modules via PRE_CLASSPATH:

\$ cd \$DOMAIN_HOME/bin

\$ cp setDomainEnv.sh setDomainEnv_orig.sh

\$ vi setDomainEnv.sh

Add the following two lines after the first line in the script:

PRE_CLASSPATH=*\[ORACLE_BASE\]*/oracle_common/modules/javax.persistence_2.1.jar:*\[WLS_HOME\]*/modules/com.oracle.weblogic.jpa21support_1.0.0.0_2-1.jar

export PRE_CLASSPATH

Enter :wq to save the file and exit vi.

#### Install VistALink on VM1

This section outlines the steps for installing VistALink on VM1:

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

355. Create a downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

356. Download vljConnector-1.5.0.028.jar, vljFoundationsLib-1.6.0.28.jar, log4j-1.2.17.jar and COMMON_vistalink_config_YYYYMMDD.zip to the downloads directory:

Download from AITC IEP eRx Downloads directory

357. Create Deployments/VistaLink directory if it doesn’t exist:

\$ mkdir -p /u01/downloads/vistalink

358. Download COMMON_vistalink_config_YYYYMMDD.zip to the Deployments/VistaLink directory:

Download from AITC IEP eRx Deployments/VistaLink directory

359. Unpack COMMON_vistalink_config_YYYYMMDD.zip file into DOMAIN_HOME:

\$ cd \$DOMAIN_HOME

\$ unzip /u01/deployments/vistalink/COMMON_vistalink_config_YYYYMMDD.zip

360. Modify configureVistaLink.sh (Production environment only):

\$ vi \$DOMAIN_HOME/bin/startWeblogic.sh

Add the following line to the bottom of the file:

export JAVA_OPTIONS=”\${JAVA_OPTIONS} -Dgov.va.med.environment.production=true”

361. Modify the Domain Startup script (startWebLogic.sh):

\$ vi \$DOMAIN_HOME/bin/startWeblogic.sh

362. Add call to configureVistalink.sh after the setDomainEnv.sh call as shown:

. \${DOMAIN_HOME}/bin/setDomainEnv.sh \$\*

. \${DOMAIN_HOME}/bin/configureVistaLink.sh \$\*

363. Modify the nodemanager.properties file:

\$ vi \$DOMAIN_HOME/nodemanager/nodemanager.properties

364. Ensure StartScriptEnabled=true:

StartScriptEnabled=true

<span class="mark">  
</span>

#### Configure VistALink on VM1

1.  Create Deployments/VistaLink directory if it doesn’t exist:

\$ mkdir -p /u01/downloads/vistalink

365. Download VistALink configuration zip file for the environment:

Download from AITC IEP eRx Deployments/VistaLink directory

366. Unzip VistALink configuration files for the environment:

\$ cd \$DOMAIN_HOME

\$ unzip /u01/deployments/vistalink/*\[ENV\]*\_vistalink_config_YYYYMMDD.zip

#### Install VistALink on VM2

This section outlines the steps for installing VistALink on VM2:

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

367. Create downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

368. Download vljConnector-1.5.0.028.jar, vljFoundationsLib-1.6.0.28.jar, log4j-1.2.17.jar and COMMON_vistalink_config_YYYYMMDD.zip to the downloads directory:

Download from AITC IEP eRx Downloads directory

369. Create Deployments/VistaLink directory if it doesn’t exist:

\$ mkdir -p /u01/downloads/vistalink

370. Download COMMON_vistalink_config_YYYYMMDD.zip to the Deployments/VistaLink directory:

Download from AITC IEP eRx Deployments/VistaLink directory

371. Unpack COMMON_vistalink_config_YYYYMMDD.zip file into DOMAIN_HOME:

\$ cd \$DOMAIN_HOME

\$ unzip /u01/deployments/vistalink/COMMON_vistalink_config_YYYYMMDD.zip

372. Modify configureVistaLink.sh (Production environment only):

\$ vi \$DOMAIN_HOME/bin/startWeblogic.sh

Add the following line to the bottom of the file:

export JAVA_OPTIONS=”\${JAVA_OPTIONS} -Dgov.va.med.environment.production=true”

373. Modify the Domain Startup script (startWebLogic.sh):

\$ vi \$DOMAIN_HOME/bin/startWeblogic.sh

374. Add call to configureVistalink.sh after the setDomainEnv.sh call as shown:

. \${DOMAIN_HOME}/bin/setDomainEnv.sh \$\*

. \${DOMAIN_HOME}/bin/configureVistaLink.sh \$\*

375. Modify the nodemanager.properties file:

\$ vi \$DOMAIN_HOME/nodemanager/nodemanager.properties

376. Ensure StartScriptEnabled=true:

StartScriptEnabled=true

#### Configure VistALink on VM2

1.  Create Deployments/VistaLink directory if it doesn’t exist:

\$ mkdir -p /u01/downloads/vistalink

377. Download VistALink configuration zip file for the environment:

Download from AITC IEP eRx Deployments/VistaLink directory

378. Unzip VistALink configuration files for the environment:

\$ cd \$DOMAIN_HOME

\$ unzip /u01/deployments/vistalink/*\[ENV\]*\_vistalink_config_YYYYMMDD.zip

#### Stop and start Node Manager and Domain on VM1, VM2

This section outlines the steps for starting the node manager on the first WebLogic machine:

1.  Stop the new domain on the VM1.

\$ \$DOMAIN_HOME/bin/stopWebLogic.sh

379. On VM1 stop the node manager.

\$ \$DOMAIN_HOME/bin/stopNodeManager.sh

380. On VM1, start the node manager.

\$ DOMAIN_HOME/bin/stopNodeManager.sh

381. On VM2 stop the node manager.

\$ \$DOMAIN_HOME/bin/stopNodeManager.sh

382. On VM2, start the node manager.

\$ DOMAIN_HOME/bin/stopNodeManager.sh

383. Start the domain on VM1.

\$ \$DOMAIN_HOME/bin/startWebLogic.sh

384. Wait for the RUNNING state before proceeding.

#### Deploy VistALink Libraries

This section provides step-by-step instructions for deploying VistA Link Connector:

1.  Navigate to the *Deployments* page.
1.  From the *Deployment*s screen, select Install.

> <span id="_Toc29569608" class="anchor"></span>Figure 62: Deploy VistA Link Connector – Deployments

> ![](pso-7-589-inbound-eprescribing-dibr/063.png)

<span class="mark">  
</span>

385. Enter *Path*: /u01/downloads
386. Install a new deployment of log4j-1.2.17.jar by selecting the jar file as indicated, and then select Next.

> <span id="_Toc29569609" class="anchor"></span>Figure 63: Deploy VistA Link Connector – Select log4j Library to deploy

> ![](pso-7-589-inbound-eprescribing-dibr/064.png)

387. Select All servers in the cluster as the target for the deployment, and then select Next.

> <span id="_Toc29569610" class="anchor"></span>Figure 64: Deploy VistA Link Connector – Select Deployment Targets

> ![](pso-7-589-inbound-eprescribing-dibr/065.png)

388. All of the values should appear as illustrated in the figure below.
389. Select Next.

> <span id="_Toc29569611" class="anchor"></span>Figure 65: Deploy VistA Link Connector – Summary of Deployments Verification 1

> ![](pso-7-589-inbound-eprescribing-dibr/066.png)

<span class="mark">  
</span>

390. Verify that all of the values appear as illustrated in the figure below.
391. Select Finish.

> <span id="_Toc29569612" class="anchor"></span>Figure 66: Deploy VistA Link Connector – Summary of Deployments Verification 2

> ![](pso-7-589-inbound-eprescribing-dibr/067.png)

<span class="mark">  
</span>

392. The Deployment Configuration screen should appear as illustrated in the below figure.
393. Enter *Deployment Order*: 1
394. Select Save.

> <span id="_Toc29569613" class="anchor"></span>Figure 67: Deploy VistA Link Connector – Deployment Configuration Screen

> ![](pso-7-589-inbound-eprescribing-dibr/068.png)

<span class="mark">  
</span>

395. Navigate to the *Deployments* page.
396. From the *Deployment*s screen, select Install.

> <span id="_Toc29569614" class="anchor"></span>Figure 68: Deploy VistA Link Connector – Deployments

> ![](pso-7-589-inbound-eprescribing-dibr/069.png)

<span class="mark">  
</span>

397. Enter *Path*: /u01/downloads
398. Install a new deployment of vljConnector-1.6.0.028.jar by selecting the jar file as indicated, and then select Next.

> <span id="_Toc29569615" class="anchor"></span>Figure 69: Deploy VistA Link Connector – Select vljConnector-1.6.0.028.jar Library to deploy

> ![](pso-7-589-inbound-eprescribing-dibr/070.png)

399. Select All servers in the cluster as the target for the deployment, and then select Next.

> <span id="_Toc29569616" class="anchor"></span>Figure 70: Deploy VistA Link Connector – Select Deployment Targets

> ![](pso-7-589-inbound-eprescribing-dibr/071.png)

400. All of the values should appear as illustrated in the figure below.
401. Select Next.

> <span id="_Toc29569617" class="anchor"></span>Figure 71: Deploy VistA Link Connector – Summary of Deployments Verification 1

> ![](pso-7-589-inbound-eprescribing-dibr/072.png)

402. Verify that all of the values appear as illustrated in the figure below.
403. Select Finish.

> <span id="_Toc29569618" class="anchor"></span>Figure 72: Deploy VistA Link Connector – Summary of Deployments Verification 2

> ![](pso-7-589-inbound-eprescribing-dibr/073.png)

404. The Deployment Configuration screen should appear as illustrated in the below figure.
405. Enter *Deployment Order*: 1
406. Select Save.

> <span id="_Toc29569619" class="anchor"></span>Figure 73: Deploy VistA Link Connector – Deployment Configuration Screen

> ![](pso-7-589-inbound-eprescribing-dibr/074.png)

407. Navigate to the *Deployments* page.
408. From the *Deployment*s screen, select Install.

> <span id="_Toc29569620" class="anchor"></span>Figure 74: Deploy VistA Link Connector – Deployments

> ![](pso-7-589-inbound-eprescribing-dibr/075.png)

409. Enter *Path*: /u01/downloads
410. Install a new deployment of vljFoundationsLib-1.6.0.028.jar by selecting the jar file as indicated, and then select Next.

> <span id="_Toc29569621" class="anchor"></span>Figure 75: Deploy VistA Link Connector – Select vljFoundationsLib to deploy

> ![](pso-7-589-inbound-eprescribing-dibr/076.png)

411. Select All servers in the cluster as the target for the deployment, and then select Next.

> <span id="_Toc29569622" class="anchor"></span>Figure 76: Deploy VistA Link Connector – Select Deployment Targets

> ![](pso-7-589-inbound-eprescribing-dibr/077.png)

412. All of the values should appear as illustrated in the figure below.
413. Select Next.

> <span id="_Toc29569623" class="anchor"></span>Figure 77: Deploy VistA Link Connector – Summary of Deployments Verification 1

> ![](pso-7-589-inbound-eprescribing-dibr/078.png)

414. Verify that all of the values appear as illustrated in the figure below.
415. Select Finish.

> <span id="_Toc29569624" class="anchor"></span>Figure 78: Deploy VistA Link Connector – Summary of Deployments Verification 2

> ![](pso-7-589-inbound-eprescribing-dibr/079.png)

416. The Deployment Configuration screen should appear as illustrated in the below figure.
417. Enter *Deployment Order*: 1
418. Select Save.

> <span id="_Toc29569625" class="anchor"></span>Figure 79: Deploy VistA Link Connector – Deployment Configuration Screen

> ![](pso-7-589-inbound-eprescribing-dibr/080.png)

419. Navigate to the *Deployments* page.
420. From the *Deployment*s screen, select Install.

> <span id="_Toc29569626" class="anchor"></span>Figure 80: Deploy VistA Link Connector – Deployments

> ![](pso-7-589-inbound-eprescribing-dibr/081.png)

421. Enter *Path*: /u01/downloads
422. Install a new deployment of VistaLinkConsole-1.6.0.0.28.ear by selecting file as indicated, and then select Next.

> <span id="_Toc29569627" class="anchor"></span>Figure 81: Deploy VistA Link Connector – Select VistaLinkConsole to deploy

> ![](pso-7-589-inbound-eprescribing-dibr/082.png)

423. Select All servers in the cluster as the target for the deployment, and then select Next.

> <span id="_Toc29569628" class="anchor"></span>Figure 82: Deploy VistA Link Connector – Select Deployment Targets

> ![](pso-7-589-inbound-eprescribing-dibr/083.png)

424. Select All servers in the cluster as the target for the deployment, and then select Next.

> <span id="_Toc29569629" class="anchor"></span>Figure 83: Deploy VistA Link Connector – Select Deployment Targets

> ![](pso-7-589-inbound-eprescribing-dibr/084.png)

425. All of the values should appear as illustrated in the figure below.
426. Select Next.

> <span id="_Toc29569630" class="anchor"></span>Figure 84: Deploy VistA Link Connector – Summary of Deployments Verification 1

> ![](pso-7-589-inbound-eprescribing-dibr/085.png)

427. Verify that all of the values appear as illustrated in the figure below.
428. Select Finish.

> <span id="_Toc29569631" class="anchor"></span>Figure 85: Deploy VistA Link Connector – Summary of Deployments Verification 2

> ![](pso-7-589-inbound-eprescribing-dibr/086.png)

429. The Deployment Configuration screen should appear as illustrated in the below figure.
430. Enter *Deployment Order*: 1
431. Select Save.

> <span id="_Toc29569632" class="anchor"></span>Figure 86: Deploy VistA Link Connector – Deployment Configuration Screen

> ![](pso-7-589-inbound-eprescribing-dibr/087.png)

#### Deploy VistALink Adapters

This section provides step-by-step instructions for deploying VistA Link Adapter.

1.  The WebLogic Administrator stops the VM1 managed server, per section: 7.2.2, step Error! Reference source not found.
432. The System Administrator executes the eRx/IEP Configurator script containing adapter configuration on VM1, menu options 1, 2 and 3.
433. The WebLogic Administrator will start the VM1 managed server, per section 7.1.2.
434. The WebLogic Administrator stops the VM2 managed server, per section: 7.2.2, step Error! Reference source not found.
435. The System Administrator executes the eRx/IEP Configurator script containing adapter configuration on VM2, menu options 1, 2 and 3.
436. The WebLogic Administrator will start the VM2 managed server, per section 7.1.2.
437. The WebLogic navigates to the *Deployment*s screen and selects Install.

> <span id="_Toc29569633" class="anchor"></span>Figure 87: Deploy VistA Link Connector – Deployments

> ![](pso-7-589-inbound-eprescribing-dibr/088.png)

438. Enter *Path*: \[DOMAIN_HOME\]/vistalink/resource_adapters, .
439. Select the desired vljXXX_adapter to be installed, and then select Next.

> <span id="_Toc10727581" class="anchor"></span>Figure 88: Deploy VistA Link Connector – Select vljxxx_apapter to install

> ![](pso-7-589-inbound-eprescribing-dibr/089.png)

440. Select Install this deployment as an application as the target for the deployment, and then select Next.

> <span id="_Toc10727582" class="anchor"></span>Figure 89: Deploy VistA Link Connector – Select Deployment Type

> ![](pso-7-589-inbound-eprescribing-dibr/090.png)

441. Select All servers in the cluster as the target for the deployment, and then select Next.

> <span id="_Toc10727583" class="anchor"></span>Figure 90: Deploy VistA Link Connector – Select Deployment Targets

> ![](pso-7-589-inbound-eprescribing-dibr/091.png)

442. All of the values should appear as illustrated in the figure below.
443. Select Next.

> <span id="_Toc10727584" class="anchor"></span>Figure 91: Deploy VistA Link Connector – Adapter Optional Settings

> ![](pso-7-589-inbound-eprescribing-dibr/092.png)

444. Verify that all of the values appear as illustrated in the figure below.
445. Select Finish.

> <span id="_Toc10727585" class="anchor"></span>Figure 92: Deploy VistA Link Connector – Finish Adapter Installation

> ![](pso-7-589-inbound-eprescribing-dibr/093.png)

446. Navigate to Deployments, select the vljXXX_adapter, select Start \> Servicing all Requests.

> <span id="_Toc10727586" class="anchor"></span>Figure 93: Deploy VistA Link Connector – Start Resource Adapter

> ![](pso-7-589-inbound-eprescribing-dibr/094.png)

### Inbound eRx Application Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the steps to install and configure the Inbound eRx application. Most activities are to be performed by the WebLogic Administrator.

#### Install Inbound eRx Application

1.  Shut down WebLogic (refer to Sections 4.8.2.3 and 4.8.2.4).
2.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

447. Create the downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

448. Download Inbound eRx application to the downloads directory.

Download from AITC IEP eRx Downloads directory

449. Create the deployments directory if it doesn’t exist:

\$ mkdir -p /u01/deployments

450. Copy the application EAR to the deployments directory:

Download from AITC IEP eRx Downloads directory

451. Access the WebLogic Admin Console by directing a browser to: https://*\[vm1_fqdn\]*:7002/console/ and log in with the weblogic account.
452. Navigate to the Servers page.
453. From the Administration Console \> Servers page, select the erx1 link to configure the server.

> <span id="_Toc29569640" class="anchor"></span>Figure 94: Install Inbound eRx Application – Configure Servers

> ![](pso-7-589-inbound-eprescribing-dibr/095.png)

454. The server configuration screen should appear as shown in the figure below.
455. Inspect the settings under the General tab. The *Listen Address* should be *\[vm1_fqdn\]*. The non-secure listening port (*Listen Port Enabled*) should be enabled and set to port 8001 (*Listen Port*). The secure listening port should be disabled (*SSL Listen Port Enabled*). These ports need to be consistent with the Apache Load Balancer/Proxy and local firewall settings.

> <span id="_Toc29569641" class="anchor"></span>Figure 95: Install Inbound eRx Application – Verify Server Settings

> ![](pso-7-589-inbound-eprescribing-dibr/096.png)

456. Review the setting under the Keystores tab as illustrated in the figure below. Verify the *Keystores* option is set to Custom Identity and Custom Trust, and that the fields under the *Identity* and *Trust* sections are filled with the same corresponding values.

> <span id="_Toc29569642" class="anchor"></span>Figure 96: Install Inbound eRx Application – Verify General & Keystore Settings

> ![](pso-7-589-inbound-eprescribing-dibr/097.png)

457. Verify the settings under the SSL tab. The *Private Key Alias* should be the Fully Qualified Domain Name of the server, and the *Passphrase* is xxxxxxxx.

> <span id="_Toc29569643" class="anchor"></span>Figure 97: Install Inbound eRx Application – Verify SSL Settings

> ![](pso-7-589-inbound-eprescribing-dibr/098.png)

458. Repeat the previous three steps for the erx2 managed server to verify the *General Configuration*, *Keystores,* and *SSL* settings.
459. Navigate to the Deployments page.
460. From the Deployments page, select Install.

> <span id="_Toc29569644" class="anchor"></span>Figure 98: Install Inbound eRx Application – Summary of Deployments

> ![](pso-7-589-inbound-eprescribing-dibr/099.png)

461. Install a new deployment of INB\_ ERX-3.1.0.006.ear using the .ear file as indicated in the figure below.
462. select Next.

> <span id="_Toc29569645" class="anchor"></span>Figure 99: Install Inbound eRx Application – Install New Deployment of INB_ERX

> ![](pso-7-589-inbound-eprescribing-dibr/100.png)

463. Accept the defaults for an application deployment.
464. Select Next.
465. Select the cluster and All servers in the cluster as the target for the deployment.
466. Select Next.

> <span id="_Toc29569646" class="anchor"></span>Figure 100: Install Inbound eRx Application – Select INB_ERX Deployment Targets

> ![](pso-7-589-inbound-eprescribing-dibr/101.png)

467. All of the values should appear as illustrated in the figure below.
468. Select Next.

> <span id="_Toc29569647" class="anchor"></span>Figure 101: Install Inbound eRx Application – Verify INB_ERX Deployment Settings

> ![](pso-7-589-inbound-eprescribing-dibr/102.png)

> <span id="_Toc29569648" class="anchor"></span>Figure 102: Install Inbound eRx Application – Verify INB_ERX Deployment Continued

> ![](pso-7-589-inbound-eprescribing-dibr/103.png)

469. All of the values should appear as illustrated in the figure below.
470. Select Finish.

> <span id="_Toc29569649" class="anchor"></span>Figure 103: Install Inbound eRx Application – Verify INB_ERX Deployment Settings (Finish)

> ![](pso-7-589-inbound-eprescribing-dibr/104.png)

471. The Overview tab should appear as illustrated in the figure below.

> <span id="_Toc29569650" class="anchor"></span>Figure 104: Install Inbound eRx Application – Verify INB_ERX Deployment Configuration Settings

> ![](pso-7-589-inbound-eprescribing-dibr/105.png)

472. Navigate to the Deployments page.
473. From the Deployments page, select Install.
474. Install a new deployment of INB_ERX_UI-3.1.0.006.ear, select the appropriate EAR file.
475. Select Next.

> <span id="_Toc29569651" class="anchor"></span>Figure 105: Install Inbound eRx Application – Install New Deployment of INB_ERX_UI

> ![](pso-7-589-inbound-eprescribing-dibr/106.png)

476. Accept the defaults for an application deployment.
477. Select Next.
478. Select the cluster and All servers in the cluster as the target for the deployment.
479. Select Next.

> <span id="_Toc29569652" class="anchor"></span>Figure 106: Install Inbound eRx Application – Select INB_ERX_UI Deployment Targets

> ![](pso-7-589-inbound-eprescribing-dibr/107.png)

480. All of the values should appear as illustrated in the figure below.
481. Select Next.

> <span id="_Toc29569653" class="anchor"></span>Figure 107: Install Inbound eRx Application – Verify INB_ERX_UI Deployment Settings

> ![](pso-7-589-inbound-eprescribing-dibr/108.png)

482. All of the values should appear as illustrated in the figure below.
483. Select Finish.

> <span id="_Toc29569654" class="anchor"></span>Figure 108: Install Inbound eRx Application – Verify INB_ERX_UI Deployment Settings (Finish)

> ![](pso-7-589-inbound-eprescribing-dibr/109.png)

484. The Overview tab should appear as illustrated in the figure below.

> <span id="_Toc29569655" class="anchor"></span>Figure 109: Install Inbound eRx Application – Verify INB_ERX_UI Deployment Configuration Settings

> ![](pso-7-589-inbound-eprescribing-dibr/110.png)

485. Navigate to the Servers page in the WebLogic console.
486. Select the Control tab.
487. Select erx1 and erx2, and then select Start.

> <span id="_Toc29569656" class="anchor"></span>Figure 110: Install Inbound eRx Application – Start erx Servers

![](pso-7-589-inbound-eprescribing-dibr/111.png)

> <span id="_Toc29569657" class="anchor"></span>Figure 111: Install Inbound eRx Application – erx Servers Running

> ![](pso-7-589-inbound-eprescribing-dibr/112.png)

#### Create Startup/Shutdown Scripts

This section outlines the steps for creating startup/shutdown scripts:

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

488. Create startup scripts with the following commands:

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

1.  On VM1, log into Linux login and sudo su to the weblogic account:

\$ sudo su - weblogic

489. Shut down the Administration Console with the following command:

\$ ./stopWebLogic\_*\[domain\]*.sh

#### Shut Down Nodemanagers

This sections outlines the steps for shutting down the nodemanagers:

1.  On VM1, Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

490. Shut down Nodemanager with the following command:

\$ ./stopNodemanager\_*\[domain\]*.sh

491. On VM2, Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

492. Shut down Nodemanager with the following command:

\$ ./stopNodemanager\_*\[domain\]*.sh

### Pentaho Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the steps to install the WebLogic application server. Most activities are to be performed by the WebLogic Administrator.

#### Pentaho Software Installation

The section provides step-by-step guidance on the installing the Pentaho software:

1.  Log into Linux and sudo su to the kettle account:

\$ sudo su - kettle

493. Create downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

494. Download Pentaho Data Integration Community Edition 8.2 archive (pdi-ce-8.2.0.0-342.zip) to the downloads directory.

Download from AITC IEP eRx Downloads directory

495. Download INB_ERX Pentaho configuration zip archive for *\[ENV\]*.

Download pdi-*\[env\]*\_cfg\_*\[yyyymmdd\]*.zip from AITC IEP eRx Deployments directory

496. Create a pentaho directory if it doesn’t exist:

\$ mkdir -p /u01/app/pentaho

497. On VM1, unzip the Pentaho Data Integration Community Edition 8.2 archive to the pentaho master1 installation directory:

\$ cd /u01/app/pentaho

\$ unzip /u01/downloads/pdi-ce-8.2.0.0-342.zip

\$ mv data-integration pdi-*\[env\]*master1

498. On VM1, unzip the Pentaho Data Integration Community Edition 8.2 archive to the pentaho slave1 installation directory:

\$ cd /u01/app/pentaho

\$ unzip /u01/downloads/pdi-ce-8.2.0.0-342.zip

\$ mv data-integration pdi-*\[env\]*slave1

499. On VM1, unzip the Pentaho Data Integration Community Edition 8.2 archive to the pentaho slave2 installation directory:

\$ cd /u01/app/pentaho

\$ unzip /u01/downloads/pdi-ce-8.2.0.0-342.zip

\$ mv data-integration pdi-*\[env\]*slave2

500. On VM2, unzip the Pentaho Data Integration Community Edition 8.2 archive to the pentaho slave3 installation directory:

\$ cd /u01/app/pentaho

\$ unzip /u01/downloads/pdi-ce-8.2.0.0-342.zip

\$ mv data-integration pdi-*\[env\]*slave3

501. On VM2, unzip the Pentaho Data Integration Community Edition 8.2 archive to the pentaho slave4 installation directory:

\$ cd /u01/app/pentaho

\$ unzip /u01/downloads/pdi-ce-8.2.0.0-342.zip

\$ mv data-integration pdi-*\[env\]*slave4

502. On VM2, unzip the Pentaho Data Integration Community Edition 8.2 archive to the pentaho slave5 installation directory:

\$ cd /u01/app/pentaho

\$ unzip /u01/downloads/pdi-ce-8.2.0.0-342.zip

\$ mv data-integration pdi-*\[env\]*slave5

503. On VM1, unzip the environment specific configuration archive to the pentaho master1 installation directory:

\$ cd /u01/app/pentaho/pdi-*\[env\]*master1

\$ unzip /u01/downloads/pdi-*\[env\]*\_cfg\_*\[yyyymmdd\]*.zip

504. On VM1, unzip the environment specific configuration archive to the pentaho slave1 installation directory:

\$ cd /u01/app/pentaho/pdi-*\[env\]*slave1

\$ unzip /u01/downloads/pdi-*\[env\]*\_cfg\_*\[yyyymmdd\]*.zip

505. On VM1, unzip the environment specific configuration archive to the pentaho slave2 installation directory:

\$ cd /u01/app/pentaho/pdi-*\[env\]*slave2

\$ unzip /u01/downloads/pdi-*\[env\]*\_cfg\_*\[yyyymmdd\]*.zip

506. On VM2, unzip the environment specific configuration archive to the pentaho slave3 installation directory:

\$ cd /u01/app/pentaho/pdi-*\[env\]*slave3

\$ unzip /u01/downloads/pdi-*\[env\]*\_cfg\_*\[yyyymmdd\]*.zip

507. On VM2, unzip the environment specific configuration archive to the pentaho slave4 installation directory:

\$ cd /u01/app/pentaho/pdi-*\[env\]*slave4

\$ unzip /u01/downloads/pdi-*\[env\]*\_cfg\_*\[yyyymmdd\]*.zip

508. On VM2, unzip the environment specific configuration archive to the pentaho slave5 installation directory:

\$ cd /u01/app/pentaho/pdi-*\[env\]*slave5

\$ unzip /u01/downloads/pdi-*\[env\]*\_cfg\_*\[yyyymmdd\]*.zip

509. On the Master VM, create master1, slave1 and slave2 startup scripts in the ~kettle directory:

\$ cd ~

\$ cat \> ~/startCarte*\[Env\]*Master1.sh

unset DISPLAY

export KETTLE_HOME=/u01/app/pentaho/pdi-*\[env\]*master1

datestamp=\`date +%Y%m%d\_%H%M%S\`

export PENTAHO_DI_JAVA_OPTIONS="-Xms1024m -Xmx2048m -XX:MaxPermSize=256m"

\${KETTLE_HOME}/carte.sh \${KETTLE_HOME}/pwd/*\[env\]*master1-8080.xml \> \${KETTLE_HOME}/logs/*\[env\]*master1-8080\_\${datestamp}.out 2\>&1 &

\<ctlr\>d

\$ chmod 755 ~/startCarte*\[Env\]*Master1.sh

\$ cat \> ~/startCarte\[Env\]Slave1.sh

unset DISPLAY

export KETTLE_HOME=/u01/app/pentaho/pdi-\[env\]slave1

datestamp=\`date +%Y%m%d\_%H%M%S\`

export PENTAHO_DI_JAVA_OPTIONS="-Xms1024m -Xmx3072m -XX:MaxPermSize=256m"

\${KETTLE_HOME}/carte.sh \${KETTLE_HOME}/pwd/\[env\]slave1-8081.xml \> \${KETTLE_HOME}/logs/\[env\]slave1-8081\_\${datestamp}.out 2\>&1 &

\<ctlr\>d

\$ chmod 755 ~/startCarte\[Env\]Slave1.sh

\$ cat \> ~/startCarte*\[Env\]*Slave2.sh

unset DISPLAY

export KETTLE_HOME=/u01/app/pentaho/pdi-*\[env\]*slave1

datestamp=\`date +%Y%m%d\_%H%M%S\`

export PENTAHO_DI_JAVA_OPTIONS="-Xms1024m -Xmx3072m -XX:MaxPermSize=256m"

\${KETTLE_HOME}/carte.sh \${KETTLE_HOME}/pwd/*\[env\]*slave2-8082.xml \> \${KETTLE_HOME}/logs/*\[env\]*slave1-8082\_\${datestamp}.out 2\>&1 &

\<ctlr\>d

\$ chmod 755 ~/startCarte*\[Env\]*Slave2.sh

510. On the Master VM, create slave3, slave4 and slave5 startup script in the ~kettle directory:

\$ cd ~

\$ cat \> ~/startCarte*\[Env\]*Slave3.sh

unset DISPLAY

export KETTLE_HOME=/u01/app/pentaho/pdi-*\[env\]*slave3

datestamp=\`date +%Y%m%d\_%H%M%S\`

export PENTAHO_DI_JAVA_OPTIONS="-Xms1024m -Xmx3072m -XX:MaxPermSize=256m"

\${KETTLE_HOME}/carte.sh \${KETTLE_HOME}/pwd/*\[env\]*slavefx3-8083.xml \> \${KETTLE_HOME}/logs/*\[env\]*slave3-8083\_\${datestamp}.out 2\>&1 &

\<ctlr\>d

\$ chmod 755 ~/startCarte*\[Env\]*Slave3.sh

\$ cat \> ~/startCarte*\[Env\]*Slave4.sh

unset DISPLAY

export KETTLE_HOME=/u01/app/pentaho/pdi-*\[env\]*slave4

datestamp=\`date +%Y%m%d\_%H%M%S\`

export PENTAHO_DI_JAVA_OPTIONS="-Xms1024m -Xmx3072m -XX:MaxPermSize=256m"

\${KETTLE_HOME}/carte.sh \${KETTLE_HOME}/pwd/*\[env\]*slave4-8084.xml \> \${KETTLE_HOME}/logs/*\[env\]*slave4-8084\_\${datestamp}.out 2\>&1 &

\<ctlr\>d

\$ chmod 755 ~/startCarte*\[Env\]*Slave4.sh

\$ cat \> ~/startCarte*\[Env\]*Slave5.sh

unset DISPLAY

export KETTLE_HOME=/u01/app/pentaho/pdi-*\[env\]*slave5

datestamp=\`date +%Y%m%d\_%H%M%S\`

export PENTAHO_DI_JAVA_OPTIONS="-Xms1024m -Xmx3072m -XX:MaxPermSize=256m"

\${KETTLE_HOME}/carte.sh \${KETTLE_HOME}/pwd/*\[env\]*slave5-8085.xml \> \${KETTLE_HOME}/logs/*\[env\]*slave5-8085\_\${datestamp}.out 2\>&1 &

\<ctlr\>d

\$ chmod 755 ~/startCarte*\[Env\]*Slave5.sh

511. On the Master VM, create repository update script in the ~kettle directory:

\$ cd ~

\$ cat \> ~/updateRepo*\[Env\]*.sh

unset DISPLAY

export KETTLE_HOME=/u01/app/pentaho/pdi-*\[env\]*master1

datestamp=\`date +%Y%m%d\_%H%M%S\`

\${KETTLE_HOME}/import.sh -rep="*\[ENV\]* Repo" -user=admin -pass=admin -dir=/ -replace=Y -norules=Y -file=\${KETTLE_HOME}/erx_repo/inbound_main.xml \| tee \${KETTLE_HOME}/logs/updateRepoDev1\_\${datestamp}.out 2\>&1

\${KETTLE_HOME}/import.sh -rep="*\[ENV\]* Repo" -user=admin -pass=admin -dir=/ -replace=Y -norules=Y -file=\${KETTLE_HOME}/erx_repo/inbound_vista_delivery.xml \| tee -a \${KETTLE_HOME}/logs/updateRepoDev1\_\${datestamp}.out 2\>&1

\${KETTLE_HOME}/import.sh -rep="*\[ENV\]* Repo" -user=admin -pass=admin -dir=/ -replace=Y -norules=Y -file=\${KETTLE_HOME}/erx_repo/outbound_main.xml \| tee -a \${KETTLE_HOME}/logs/updateRepoDev1\_\${datestamp}.out 2\>&1

\<ctlr\>d

\$ chmod 755 ~/updateRepo*\[Env\]*.sh

#### Pentaho Repository Definition Import

The section provides step-by-step guidance to import the Pentaho repository:

1.  Log into Linux and sudo su to the kettle account:

\$ sudo su - kettle

512. Create downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

513. Download INB_ERX Pentaho Repository Definition zip archive for *\[ENV\]*.

Download PS_INB_ERX_Pentaho\_*\[n.n.n.nnn\]*.zip from AITC IEP eRx Deployments directory

514. Unpack repository definition in Master1 instance:

\$ cd /u01/app/pentaho/pdi-\[env\]master1

\$ unzip /u01/app/downloads/PS_INB_ERX_Pentaho\_*\[n.n.n.nnn\]*.zip erx_repo/\*

515. Update Pentaho repository:

\$ cd ~

\$ ~/updateRepo*\[Env\]*.sh

### Nexus Repository Installation (DEV2 VM1 Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the steps to install the SonaType Nexus OSS repository server. All activities are to be performed by a Systems Administrator.

#### SonaType Nexus Software Installation

The section provides step-by-step guidance on the installing the SonaType Nexus repository software:

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

516. Create downloads directory if it doesn’t exist:

\$ mkdir -p /u01/downloads

517. Download SonaType Nexus OSS repository software archive (nexus-3.5.2-01-unix.tar.gz) to the downloads directory.

Download from AITC IEP eRx Downloads directory

518. Return back in your normal Linux login account.

\$ exit

519. Create the nexus software directory if it doesn’t exist:

\$ sudo mkdir -p /u01/app/nexus

\$ sudo chown nexusloc:weblogic /u01/app/nexus

\$ sudo chmod 755 /u01/app/nexus

520. Unpack Nexus repository software:

\$ cd /u01/app/nexus

\$ sudo -u nexusloc tar xvzf /u01/downloads/nexus-3.5.2-01-unix.tar.gz

\$ sudo ln –s nexus-3.5.2-01 latest

3.  Modify /u01/app/nexus/latest/bin/nexus.rc:

\$sudo vi /u01/app/nexus/latest/bin/nexus.rc

521. Modify service user account:

run_as_user="nexusloc"

4.  Modify /u01/app/nexus/sonatype-work/nexus3/etc/nexus.properties:

\$sudo vi /u01/app/nexus/sonatype-work/nexus3/etc/nexus.properties

522. Modify as follows:

application-port=8061

application-host=vaauserxappdev2.aac.<span class="mark">REDACTED</span>

nexus-context-path=/nexus/

5.  Modify ~nexusol/.bashrc:

\$ sudo vi ~nexusloc/.bashrc

523. Add NEXUS_HOME near the end of the file:

export NEXUS_HOME=/u01/app/nexus/latest

6.  Modify /u01/app/nexus/latest/bin/nexus

\$sudo vi /u01/app/nexus/latest/bin/nexus

524. Enable the INSTALL4_JAVA_HOME_OVERRIDE variable:

INSTALL4J_JAVA_HOME_OVERRIDE=/u01/app/java/latest

7.  Modify HTTPD configuration:

\$ sudo vi /etc/httpd/conf/httpd.conf

525. Add the following for Nexus reverse proxy:

\#

\# Reverse proxy to Nexus

\#

ProxyPass /nexus/ http://vaauserxappdev2.aac.<span class="mark">REDACTED</span>:8061/nexus/

ProxyPassReverse /nexus/ http://vaauserxappdev2.aac.<span class="mark">REDACTED</span>:8061/nexus/

526. Create symbolic link for /etc/init.d/nexus:

\$ sudo ln -s /u01/app/nexus/latest/bin/nexus /etc/init.d/nexus

527. Enable the Nexus OSS repository service:

\$ cd /etc/init.d

\$ sudo chkconfig –add nexus

\$ sudo chkconfig –levels 345 nexus on

### VistA Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to patch PSO\*7.0\*589.

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

This section describes the back-out procedure for Inbound eRx. Back-out pertains to a return to the last known operational state of the software and appropriate platform settings.

The Inbound eRx system will provide data protection measures, such as back-up intervals and redundancies that are consistent with systems categorized as mission critical (12 hour restoration, 2 hour recover point objectives). This section outlines the backout strategy, considerations, testing, criteria for backout, risks, authority to approve, and the procedures to perform a backout for Inbound eRx.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out strategy will follow VA guidelines and best practices as referenced in the Enterprise Operations (EO) National Data Center Hosting Services document.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to the Inbound eRx project.

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

The POCs with the authority to order the back-out is the Inbound eRx IPT, the VA PM, and other relevant stakeholders.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the backout procedure for the following:

- Pentaho 8.2 upgrade patch PSO\*7.0\*589
- WebLogic

### Back-Out of VistA Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for patch PSO\*7.0\*589.

### Back-Out of Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the steps for backing out Database changes on the local database server. These steps should be performed under strict guidance of the PRE Inbound eRx PM team.

#### Restore backup files from tape 

Recover data procedures are in the EO National Data Center Hosting Services document.

#### Mount the instance

1.  Set ORACLE_SID=IEPP
1.  rman TARGET SYS/Password NOCATALOG
2.  RMAN:\> shutdown immediate;  
    > RMAN:\> startup mount;

#### Restore and recover the datafiles

1.  RMAN\> run  
    {  
    allocate channel dev1 type disk;  
    set until time "to_date('2011-12-30:00:00:00', 'yyyy-mm-dd:hh24:mi:ss')";  
    restore database;  
    recover database; }

#### Open the database and reset logs

1.  RMAN\> alter database open resetlogs;

### Back-Out of WebLogic 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the steps for backing out a new version of the PRE Inbound eRx application deployed on a local WebLogic (application) server. This is a two-step process: first, remove the new release, and then deploy the rolled-back release. These steps should be performed under strict guidance of the PRE Inbound eRx PM team.

#### Remove New Release

1.  Open and log into the WebLogic console. Use WebLogic username and password.
3.  Within the Domain Structure panel in the left column of the WebLogic console, select the Deployments node.
4.  Within the Change Center panel in the left column of the WebLogic console, select Lock & Edit.
5.  WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed.
6.  Select the previously deployed Inbound eRx deployment, select Stop, and then select Force Stop Now from the drop-down list.
7.  WebLogic will now display the panel Force Stop Application Assistant in the right column of the console for confirmation to start servicing requests.
8.  Select Yes in the Force Stop Application Assistant panel in the right column of the WebLogic console.
9.  WebLogic now returns to the Summary of Deployments panel in the right column of the console.
10. Verify that the State of the Inbound eRx deployment is Prepared.
11. Select the previously deployed Inbound eRx deployment, and then select Delete.
12. WebLogic will now display the panel Delete Application Assistant in the right column of the console for confirmation to start servicing requests.
13. Select Yes in the Delete Application Assistant panel in the right column of the WebLogic console.
14. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
15. Verify that the Inbound eRx deployment has been deleted and is no longer present.

#### Deploy Back-out Release

The following steps detail the deployment of the rolled-back Inbound eRx application.

1.  Use the WebLogic console that was started at the beginning of the roll-back process.
528. Within the Domain Structure panel in the left column of the WebLogic console, select the Deployments node.
529. Verify that application is in Lock & Edit mode. Lock & Edit mode is indicated by the “greyed-out” Lock & Edit selection button.
530. Select Install in the Deployments panel in the right column of the WebLogic console.
531. WebLogic will now display the panel, Install Application Assistant in the right column of the console where the Inbound eRx deployment will be found.
     1.  If the rolled-back Inbound eRx deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the Location panel within the Install Application Assistant in the right column of the console. Choose the ear file associated with the rolled-back release.
     2.  If the rolled-back Inbound eRx deployment has not been transferred to the Deployment Machine:
         1.  Select the upload your file(s) link in the Install Application Assistant panel in the right section of the console.
         2.  Select the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
         3.  Select Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the Locate deployment to install and prepare for deployment panel within the Install Application Assistant.
532. Once the rolled-back Inbound eRx deployment is located and selected, select Next.
533. WebLogic will now display the panel Choose targeting style within the Install Application Assistant in the right column of the console. Leave the default value selected, install this deployment as an application, and select Next.
534. Within the Install Application Assistant in the right column of the console, WebLogic will now display the panel Select deployment targets, where the Deployment Server will be selected as the target in the next step.
535. For the Target, select the Deployment Server.
536. Select Next.
537. Within the Install Application Assistant, WebLogic will now display the panel Optional Settings in the right column of the console, where the name of the deployment and the copy behavior are chosen.
538. Enter the Name for the deployment. Use: INB_ERX-3.1.0.005
539. Verify that the following default option for Security is selected:

     DD Only: Use only roles and policies that are defined in the deployment descriptors.
540. Verify that the following default option for Source accessibility is selected:

     Use the defaults defined by the deployment's targets.
541. Select Next.
542. Within the Install Application Assistant, in the right column of the console WebLogic, the panel Review your choices and click Finish will now be displayed, which summarizes the steps completed above.
543. Verify that the values match those entered in Steps 6 through 17 and select Finish.
544. WebLogic will now display the panel Settings for Inbound eRx, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
545. Leave all the values as defaulted by WebLogic and select Save.
546. Within the Change Center panel in the left column of the WebLogic console, select Activate Changes.
547. Within the Domain Structure panel in the left column of the WebLogic console, select the Deployments node.
548. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed.
549. Select the previously deployed INB_ERX-3.1.0.005 deployment, select Start, and then select Servicing all requests from the drop-down list.
550. WebLogic will now display the panel Start Application Assistant in the right column of the console for confirmation to start servicing requests.
551. Select Yes in the Start Application Assistant panel in the right column of the WebLogic console.
552. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
553. Verify that the State of the INB_ERX-3.1.0.005 deployment is Active.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For verifying the patch backout for Inbound eRx reference PSO\*7.0\*551 Patch Description in Forum and pso_7_0_p551_ig detailing Deployment, Installation, Back-Out, and Rollback for PSO\*7.0\*551.

Depending on the approach taken for the back-out, the verification steps will vary. Please contact the Inbound eRx development/maintenance team for verification instructions.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the procedures for rolling back to a previous state of the data.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback criteria will follow VA guidelines and best practices as referenced in the EO National Data Center Hosting Services document.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known risks related to a Rollback.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The POCs with the authority to order the Rollback are the Inbound eRx IPT, the VA PM, and other relevant stakeholders.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Rollback of Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the steps for rollback of Database changes on the local database server. These steps should be performed under strict guidance of the PRE Inbound eRx PM team.

#### Restore backup files from tape 

Recover data procedures are in the EO National Data Center Hosting Services document.

#### Mount the instance

2.  Set ORACLE_SID=IEPP
3.  rman TARGET SYS/Password NOCATALOG
4.  RMAN:\> shutdown immediate;  
    RMAN:\> startup mount;

#### Restore and recover the datafiles

2.  RMAN\> run  
    {  
    allocate channel dev1 type disk;  
    set until time "to_date('2011-12-30:00:00:00', 'yyyy-mm-dd:hh24:mi:ss')";  
    restore database;  
    recover database; }

#### Open the database and reset logs

2.  RMAN\> alter database open resetlogs;

### Rollback WebLogic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines the steps for rolling back to a previous version of the PRE Inbound eRx application deployed on a local WebLogic (application) server. This is a two-step process. First, remove the old release, and then deploy the rolled-back release. These steps should be performed under strict guidance of the PRE Inbound eRx PM team.

#### Remove New Release

1.  Open and log into the WebLogic console. This is located at: \\vaauspecdbs801.aac.dva.<span class="mark">REDACTED</span>\erx\install\\ Use WebLogic username and password.
554. Within the Domain Structure panel in the left column of the WebLogic console, select the Deployments node.
555. Within the Change Center panel in the left column of the WebLogic console, select Lock & Edit.
556. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed.
557. Select the previously deployed Inbound eRx deployment, select Stop, and then select Force Stop Now from the drop-down list.
558. WebLogic will now display the panel Force Stop Application Assistant in the right column of the console for confirmation to start servicing requests.
559. Select Yes in the Force Stop Application Assistant panel in the right column of the WebLogic console.
560. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
561. Verify that the State of the Inbound eRx deployment is Prepared.
562. Select the previously deployed Inbound eRx deployment, and then select Delete.
563. WebLogic will now display the panel Delete Application Assistant in the right column of the console for confirmation to start servicing requests.
564. Select Yes in the Delete Application Assistant panel in the right column of the WebLogic console.
565. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
566. Verify that the Inbound eRx deployment is deleted and no longer present.

#### Deploy Rolled-Back Release

The following steps detail the deployment of the rolled-back Inbound eRx application.

1.  Use the WebLogic console that was started at the beginning of the roll-back process.
567. Within the Domain Structure panel in the left column of the WebLogic console, select the Deployments node.
568. Verify that the application is in Lock & Edit mode. Lock & Edit mode is indicated by the “greyed-out” Lock & Edit selection button.
569. Select the Install button in the Deployments panel in the right column of the WebLogic console.
570. WebLogic will now display the panel Install Application Assistant in the right column of the console, where the location of the Inbound eRx deployment will be found.
1.  If the rolled-back Inbound eRx deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the Location panel, which is within the Install Application Assistant panel in the right column of the console. Choose the ear file associated with the rolled-back release.
2.  If the rolled-back Inbound eRx deployment has not been transferred to the Deployment Machine:
    1.  Select on the upload your file(s) link in the Install Application Assistant panel in the right section of the console.
    2.  Select the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
    3.  Select Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the Locate deployment to install and prepare for deployment panel within the Install Application Assistant.
571. Once the rolled-back Inbound eRx deployment is located and selected, select Next.
572. WebLogic will now display the panel Choose targeting style within the Install Application Assistant in the right column of the console. Leave the default value selected, install this deployment as an application, and select Next.
573. Within the Install Application Assistant in the right column of the console, WebLogic will now display the panel Select deployment targets, where the Deployment Server will be selected as the target in the next step.
574. For the Target, select the Deployment Server.
575. Select Next.
576. Within the Install Application Assistant, WebLogic will now display the panel Optional Settings in the right column of the console, where the name of the deployment and the copy behavior are chosen.
577. Enter the Name for the deployment. Use: INB_ERX-3.1.0.005
578. Verify that the following default option for Security is selected:

     DD Only: Use only roles and policies that are defined in the deployment descriptors.
579. Verify that the following default option for Source accessibility is selected:

     Use the defaults defined by the deployment's targets.
580. Select Next.
581. Within the Install Application Assistant, in the right column of the console WebLogic, the panel Review your choices and click Finish will now be displayed, which summarizes the steps completed above.
582. Verify that the values match those entered in Steps 6 through 17 and select Finish.
583. WebLogic will now display the panel Settings for Inbound eRx, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
584. Leave all the values as defaulted by WebLogic and select Save.
585. Within the Change Center panel in the left column of the WebLogic console, select Activate Changes.
586. Within the Domain Structure panel in the left column of the WebLogic console, select the Deployments node.
587. WebLogic will now display the panel Summary of Deployments in the right column of the console, where all deployments for the WebLogic domain are listed.
588. Select the previously deployed INB_ERX-3.1.0.005 deployment, select Start, and then select Servicing all requests from the drop-down list.
589. WebLogic will now display the panel Start Application Assistant in the right column of the console for confirmation to start servicing requests.
590. Select Yes in the Start Application Assistant panel in the right column of the WebLogic console.
591. WebLogic now returns to the Summary of Deployments panel in the right column of the console.
592. Verify that the State of the INB_ERX-3.1.0.005 deployment is Active.

### Rollback VistA Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the fact that the data involved with inbound eRx is prescription related, data dictionary changes and existing data will not be rolled back. The system should maintain the new fields and records. The back-out procedure will dictate the usage/view of the new data. Any new message type will still be available to the user and will be impacted only by the back-out procedure. Message linking between NewRx and cancel/refill message types will be established. The rolling back of the data would sever this linkage, potentially causing major problems.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Validation of Roll Back Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user will be able to view the cancel and refill message types. All actions besides print will be locked so the user cannot take action on the record. This will create a view only scenario for cancel and refill message types.

# Operational Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section outlines server startup and shutdown procedures.

## Startup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Start Weblogic Node Managers and Admin Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su - weblogic

593. On VM1, start node managers:

\$ ./startNodemanager\_*\[domain\]*.sh

594. On VM2, start node managers:

\$ ./startNodemanager\_*\[domain\]*.sh

595. On VM1, wait for node manager startups to complete:

\$ tail -f \[DOMAIN_HOME\]/nodemanager/nodemanager.log

596. On VM1, watch for the following log messages to indicate the node managers are up:

\<INFO\> \<Secure socket listener started on port 5556, host *\[vm1_fqdn\]*\>

597. On VM2, wait for node manager startups to complete:

\$ tail -f \[DOMAIN_HOME\]/nodemanager/nodemanager.log

598. On VM2, watch for the following log messages to indicate the node managers are up:

\<INFO\> \<Secure socket listener started on port 5556, host *\[vm2_fqdn\]*\>

599. On VM1, start AdminServer:

\$ ./startWebLogic\_*\[domain\]*.sh

600. On VM1, wait for the AdminServer startup to complete:

\$ tail -f \[DOMAIN_HOME\]/servers/AdminServer/logs/AdminServer.out

601. On VM1, watch for the following log messages to indicate the AdminServer is up:

\<Notice\> \<WebLogicServer\> \<BEA-000365\> \<Server state changed to RUNNING.\>

### Managed Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into the *\[domain\]* Admin Console, start erx1 and erx2 managed servers
602. Verify landing pages are responding:

https://*\[proxy_fqdn\]*/INB-ERX/

https://*\[proxy_fqdn\]*/inbound/

### Pentaho Services Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into Linux and sudo su to the kettle account:

\$ sudo su - kettle

603. On VM1, start *\[ENV\]* Master Slave:

\$ ./startCarte*\[Env\]*Master1.sh

604. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Master Slave to start up by watching: https://*\[proxy_fqdn\]*/master1/kettle/status/
605. On VM 1, start *\[ENV\]* Dynamic Slave1:

\$ ./startCarte*\[Env\]*Slave1.sh

606. On VM 1, start *\[ENV\]* Dynamic Slave2:

\$ ./startCarte*\[Env\]*Slave2.sh

607. On VM 2, start *\[ENV\]* Dynamic Slave3:

\$ ./startCarte*\[Env\]*Slave3.sh

608. On VM 2, start *\[ENV\]* Dynamic Slave4:

     \$ ./startCarte*\[Env\]*Slave4.sh
609. On VM 2, start *\[ENV\]* Dynamic Slave5:

\$ ./startCarte*\[Env\]*Slave5.sh

610. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Slave1 to start up by watching: https://*\[proxy_fqdn\]*/slave1/kettle/status/
611. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Slave2 to start up by watching: https://*\[proxy_fqdn\]*/slave2/kettle/status/
612. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Slave3 to start up by watching: https://*\[proxy_fqdn\]*/slave3/kettle/status/
613. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Slave4 to start up by watching: https://*\[proxy_fqdn\]*/slave4/kettle/status/
614. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), wait for the *\[ENV\]* Slave5 to start up by watching: https://*\[proxy_fqdn\]*/slave5/kettle/status/
615. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check that all 5 dynamic slaves have registered with the master: https://*\[proxy_fqdn\]*/slave1/kettle/getSlaves/
616. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), start the message processing jobs:  
     https://*\[proxy_fqdn\]*/slave1/kettle/runJob/?job=inbound_main/InboundMessageProcessing_JOB  
     https://*\[proxy_fqdn\]*/slave2/kettle/runJob/?job=inbound_main/InboundMessageProcessingRetry_JOB  
     https://*\[proxy_fqdn\]*/slave3/kettle/runJob/?job=inbound_vista_delivery/InboundDeliverToVista_JOB  
     https://*\[proxy_fqdn\]*/slave4/kettle/runJob/?job=outbound_main/OutboundMessageProcessing_JOB

     https://*\[proxy_fqdn\]*/slave5/kettle/runJob/?job=inbound_vista_delivery/InboundDeliverToVistaMbM_JOB
617. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check the InboundMessageProcessing_JOB status: https://*\[proxy_fqdn\]*/slave1/kettle/status, select the InboundMessageProcessing_JOB hyperlink and check the job status page.
618. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check the InboundMessageProcessingRetry_JOB status: https://*\[proxy_fqdn\]*/slave2/kettle/status, select the InboundMessageProcessingRetry_JOB hyperlink and check the job status page.
619. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check the InboundDeliverToVista \_JOB status: https://*\[proxy_fqdn\]*/slave3/kettle/status, select the InboundDeliverToVista \_JOB hyperlink and check the job status page.
620. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check the OutboundMessageProcessing \_JOB status: https://*\[proxy_fqdn\]*/slave4/kettle/status, select the OutboundMessageProcessing hyperlink and check the job status page.
621. From the CPanel (https://*\[proxy_fqdn\]*/cpanel), check the InboundDeliverToVistaMbM \_JOB status: https://*\[proxy_fqdn\]*/slave5/kettle/status, select the InboundDeliverToVistaMbM_JOB hyperlink and check the job status page.

## Shut Down Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pentaho Services Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into Linux and sudo su to the kettle account:

\$ sudo su - kettle

622. As kettle on VM2:

\$ /u01/app/pentaho/pdi-*\[env\]*slave3/carte.sh *\[vm2_fqdn\]* 8083 -s -u cluster -p cluster

\$ /u01/app/pentaho/pdi-*\[env\]*slave4/carte.sh *\[vm2_fqdn\]* 8084 -s -u cluster -p cluster

\$ /u01/app/pentaho/pdi-*\[env\]*slave5/carte.sh *\[vm2_fqdn\]* 8085 -s -u cluster -p cluster

623. As kettle on VM1:

\$ /u01/app/pentaho/pdi-*\[env\]*slave1/carte.sh *\[vm1_fqdn\]* 8081 -s -u cluster -p cluster

\$ /u01/app/pentaho/pdi-*\[env\]*slave2/carte.sh *\[vm1_fqdn\]* 8082 -s -u cluster -p cluster

\$ /u01/app/pentaho/pdi-*\[env\]*master1/carte.sh *\[vm1_fqdn\]* 8080 -s -u cluster -p cluster

### WebLogic Application Server Shutdown

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Log into Linux and sudo su to the weblogic account:

\$ sudo su – weblogic

624. Log into erxdomain1 Admin Console as weblogic

Stop erx1 and erx2 managed servers

Stop Admin console

625. On VM1, as weblogic:

\$ ./stopWebLogic\_*\[domain\]*.sh

626. On VM1, as weblogic:

\$ ./stopNodemanager\_*\[domain\]*.sh

627. On VM2, as weblogic:

\$ ./stopNodemanager\_*\[domain\]*.sh

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides additional reference information to use for the installation of various components.

## Certificate Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the text in this section for the certificate configuration steps in Section 4.2.7.

### va_root_ca_cert.txt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIDfjCCAmagAwIBAgIQA399zv0pkaxAy6VO4im+hDANBgkqhkiG9w0BAQUFADBH

MRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExHDAaBgNV

BAMTE1ZBIEludGVybmFsIFJvb3QgQ0EwHhcNMDUxMjIyMTY0NDM1WhcNMjUxMjIy

MTY1MzE5WjBHMRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYC

dmExHDAaBgNVBAMTE1ZBIEludGVybmFsIFJvb3QgQ0EwggEiMA0GCSqGSIb3DQEB

AQUAA4IBDwAwggEKAoIBAQDVafeLiz6lsJVkI1+suHKtVyCZAyyjSHhuDcIxonjg

EVk3mRUYZW3QPVuvS2m3NjKujJw9eL4FwGNnou+CUEdTvpAMoIo9Xhcm3uzR1Gq+

Gn6f9ichJYrttNkQo+JXPqgzEsNqUEFBRuQymmK7kZODAPnzN9VMlGjDGejDGCD5

fxyJyhkurwNWmVjUl8D3E6mMWM/1OyinGmTC6i4FQiJpVW5IauZDS0ceJhr2BSEW

BuH8W6mAQ9ZdXkiUBZm4/AUVw6QayK9kHTpFHoYhli1pJ12iDLn1a+NJdzNJiz7U

URdrW0LBSBApDXijKsAMmcyXMvk4ULONR9BewoCQRVrBAgMBAAGjZjBkMBMGCSsG

AQQBgjcUAgQGHgQAQwBBMAsGA1UdDwQEAwIBhjAPBgNVHRMBAf8EBTADAQH/MB0G

A1UdDgQWBBTjZG2vNo8cUIHkMxOg9OHayccdzzAQBgkrBgEEAYI3FQEEAwIBADAN

BgkqhkiG9w0BAQUFAAOCAQEAox6+zBW1kK1py0UarVb6G+cphwcPi/Gt4OzS58Aq

BiZ9j36GWzdD/LtbbG3J7Lj/gE9sFqTV8cxe9sES22TxHhcA5eSF3tOg6xWMzi9S

npRvQGSHvyYLhQ5KbJPTW3w1t2WGmxlDRCXI0cvXONuPEWN2Y15vBbv7T2kA63M0

oieYDKb6BMCzj3VBHF5WuoXXXXcJBUEPWjtJffZ88kqFkHt1DKqjdBqZIp9r56pd

4PujhowXBOdViWFJcK2wIMlNvHSkjzB1uXzTkssdMUg8CiZPpkDHMui0PhPo3ZOH

hiEE/Cj5hryyeF+iwSwQX6YkH2stk53By1ctdC/N8Egudg==

-----END CERTIFICATE-----

### va_internal_subordinate_ca_cert.txt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIF2zCCBMOgAwIBAgIHPQAAAAAW2TANBgkqhkiG9w0BAQUFADBHMRMwEQYKCZIm

iZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExHDAaBgNVBAMTE1ZBIElu

dGVybmFsIFJvb3QgQ0EwHhcNMTMwODE1MDA0NzA4WhcNMjMwODEzMDA0NzA4WjBQ

MRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExJTAjBgNV

BAMTHFZBIEludGVybmFsIFN1Ym9yZGluYXRlIENBIDEwggEiMA0GCSqGSIb3DQEB

AQUAA4IBDwAwggEKAoIBAQC8gdm7W2s9uaWucxI+miZR0P/6U2psmLn+kht6Rmdd

maar842z5/iSPHhnhPCr6Gc69YZovnJK/hjM1uxsvluu6OCFgYRGKYfAO2XaXCju

lyXmjoq09TGXJIpkCHpjNBWL8BtcgGmbbZt7WWILbvbONcscaewQ0hXOWsy7P+E2

maxhtxbg/tVmSlE6anLXCMThFuRRy2B9ps/osh8WgW91PP9Jd0YwpFCSIsU2PN1i

9gvPr8GQD+5yQPsg4ya/QFDBWyccM2eDFLXL8Tx0nJKoTSWwcT7ETjpJYFT7aqva

w36Ws62KSUy/QXTWGcEIipRePlum88/7yI27av6hdpzpAgMBAAGjggLBMIICvTAP

BgNVHRMBAf8EBTADAQH/MB0GA1UdDgQWBBTeJbRYCv2TJ9qNPR86dkt3UtlbEzAL

BgNVHQ8EBAMCAYYwEAYJKwYBBAGCNxUBBAMCAQIwIwYJKwYBBAGCNxUCBBYEFEWp

QVzWUmQmIUEwpoAI9JTK0qHLMDwGCSsGAQQBgjcVBwQvMC0GJSsGAQQBgjcVCIHI

wzOB+fAGgaWfDYTggQiFwqpLBpr2G4H2/kACAWQCAQIwHwYDVR0jBBgwFoAU42Rt

rzaPHFCB5DMToPTh2snHHc8wgdgGA1UdHwSB0DCBzTCByqCBx6CBxIYwaHR0cDov

L2NybC5wa2kudmEuZ292L3BraS9jcmwvVkFJbnRlcm5hbFJvb3QuY3JshoGPbGRh

cDovL2xkYXAucGtpLnZhLmdvdi9DTj1WQUludGVybmFsUm9vdCxDTj1DRFAsQ049

UEtJLENOPVNlcnZpY2VzLERDPVZBLERDPUdPVj9jZXJ0aWZpY2F0ZVJldm9jYXRp

b25MaXN0P2Jhc2U/b2JqZWN0Q2xhc3M9Y1JMRGlzdHJpYnV0aW9uUG9pbnQwggEL

BggrBgEFBQcBAQSB/jCB+zCBkgYIKwYBBQUHMAKGgYVsZGFwOi8vbGRhcC5wa2ku

dmEuZ292L0NOPVZBSW50ZXJuYWxSb290LENOPUFJQSxDTj1QS0ksQ049U2Vydmlj

ZXMsREM9VkEsREM9R09WP2NBQ2VydGlmaWNhdGU/YmFzZT9vYmplY3RDbGFzcz1j

ZXJ0aWZpY2F0aW9uQXV0aG9yaXR5MCMGCCsGAQUFBzABhhdodHRwOi8vb2NzcC5w

a2kudmEuZ292LzA/BggrBgEFBQcwAoYzaHR0cDovL2FpYS5wa2kudmEuZ292L1BL

SS9BSUEvVkEvVkFJbnRlcm5hbFJvb3QuY2VyMA0GCSqGSIb3DQEBBQUAA4IBAQAJ

5Tw4vho1QAuiebJ3zFow3esXmqyjRWeHhbszbNzsYop1szqelsFP0h69IYuVKVC5

eHzlCxZ6zF0dFgFOkDf65BKoIyQ4W9942rRzr8eKDiyFdb2dGqP1uS7VtcyX6kI4

BmhW5P8G6wRrD6Az7G3WUMpHZYtoaE8udOk86lZk9P7h7PlnElzH7inr307F/KjL

kc9m/RRdktv9nG2c3cEMa74lfCxiQpI2/gWTXKJJKy5younKbEUtu4o3qXHji21V

/D02OIOvcs7RYsiZuTKoKjO3/uQli85QKifnzpWyLfto0ucFIi9W9q2yuWPU6wIT

eaQRaJrinDddHRgSBqN4

-----END CERTIFICATE-----

### va_root_ca_s2_cert.pem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIDhzCCAm+gAwIBAgIQKNXLQBAcYqRGJ+LYwX8c6TANBgkqhkiG9w0BAQsFADBK

MRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExHzAdBgNV

BAMTFlZBLUludGVybmFsLVMyLVJDQTEtdjEwHhcNMTYxMDI2MTYxMzIwWhcNMzYx

MDI2MTYyMjU5WjBKMRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQB

GRYCdmExHzAdBgNVBAMTFlZBLUludGVybmFsLVMyLVJDQTEtdjEwggEiMA0GCSqG

SIb3DQEBAQUAA4IBDwAwggEKAoIBAQC7qJL6b5hzXU7o+lHgX32ods7AgOGinzA4

f9JfuzlrFp+ZvVrRgXwZLkKGfjyNQIIY6uI9fG8dwNLrBa0vWYoKwMJ4pbEjl+gy

1UDOrh3e3fPd68L3m+sUx0K/z+ZSiNkhK1MOP0wFQtYmtCDc7b5zy5NApGBCJAJB

QcdrVH8MCxC0IZEpxsTjuSDpcea09eD4nYAeBUVzg+N9K9esWF+SLZxsCnFgMuL/

ikS093wsaoFyBe0H0wH7GDNmV/Zxlxy3krzGqszfGRmxb4pXkbqvrOGzju2RZoRx

lYKYnB4brDR4BGW984fiiJq1ofbwCK4ql7nhSi71TEnxRfltCaPrAgMBAAGjaTBn

MBMGCSsGAQQBgjcUAgQGHgQAQwBBMAsGA1UdDwQEAwIBhjASBgNVHRMBAf8ECDAG

AQH/AgEBMB0GA1UdDgQWBBQBLYthZhuM0ODTTD5O7FsZsBHGYTAQBgkrBgEEAYI3

FQEEAwIBADANBgkqhkiG9w0BAQsFAAOCAQEAaE16FdPpLptzZA1sdGREaSfDP46j

e2m7Nelz2CDdT/goRS5q1+uxQpaUvH08Lxw9Nr6Chr018K1uHYMgLuFybflm5P0R

B/XKKJATszamkMUYRSGeSf1uXKNz4dqXu2yv9BvxyY2qdGJUpEyOmcuZwq/Zh1qv

1Aoq67ZeBt0R0ZnJmLiMQ7ywd2kQ8MtWlx2tcN0nZmtPOb3WkrvG2sgFZN064gP2

YVlKp9RaENjNwYNVyyTbq8CofUIYV2OfSbsI1GR3CQSqPO5CUJ/ScdWuWJVfhWLt

l1H5l12CCqk+7vaTBtK+QjBliAayTFyonUocbD5VBxB4DvlCMk7uATrhNw==

-----END CERTIFICATE-----

### va_internal_ca1_s2_cert.pem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIEoDCCA4igAwIBAgITFAAAAARskyEu6lBaeQAAAAAABDANBgkqhkiG9w0BAQsF

ADBKMRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExHzAd

BgNVBAMTFlZBLUludGVybmFsLVMyLVJDQTEtdjEwHhcNMTYxMDI3MTY0MTA3WhcN

MjYxMDI1MTY0MTA3WjBKMRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPy

LGQBGRYCdmExHzAdBgNVBAMTFlZBLUludGVybmFsLVMyLUlDQTEtdjEwggEiMA0G

CSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC4bY+wR9CKBb6rxoRajhPAFJIPdwHe

bp3Kzy5CxlPmQMk6ANqX3WWqM/qSebBHCNYvdqSgXMSdVXu0loCIhqBLvccwmxdc

4rJD6Vydh3WEv74LayMIIrzl06QLcj+6GnVmWm5/+FbEF9SynICY2RhmO8roLp1o

UnaNiC3Pruy97ZLHN/OE8Z7FMWIHHB/GQHwX/1P05p0yv/8WsojctrW8S3d56VlH

u4W4ilKZMoTxDR2JFpn6q22J4DjVG8ouOSyJQmXMFR+HcmVPAaJbAF1L0w0BOrlF

3W9w4RFo/PWdEm+SopGiTFeMMaPXG377FlEhWuX/I0yXtQT9zXt4rTTVAgMBAAGj

ggF9MIIBeTAQBgkrBgEEAYI3FQEEAwIBADAdBgNVHQ4EFgQUG23f6z3l4g3vFrHQ

3l9YGlbL5OwwPAYJKwYBBAGCNxUHBC8wLQYlKwYBBAGCNxUIgcjDM4H58AaBpZ8N

hOCBCIXCqksGg+96htu7FwIBZAIBEjALBgNVHQ8EBAMCAYYwEgYDVR0TAQH/BAgw

BgEB/wIBADAfBgNVHSMEGDAWgBQBLYthZhuM0ODTTD5O7FsZsBHGYTBJBgNVHR8E

QjBAMD6gPKA6hjhodHRwOi8vY3JsLnBraS52YS5nb3YvcGtpL2NybC9WQS1JbnRl

cm5hbC1TMi1SQ0ExLXYxLmNybDB7BggrBgEFBQcBAQRvMG0wRwYIKwYBBQUHMAKG

O2h0dHA6Ly9haWEucGtpLnZhLmdvdi9wa2kvYWlhL1ZBL1ZBLUludGVybmFsLVMy

LVJDQTEtdjEuY2VyMCIGCCsGAQUFBzABhhZodHRwOi8vb2NzcC5wa2kudmEuZ292

MA0GCSqGSIb3DQEBCwUAA4IBAQCA/ZQYzX1u6rB0xITkVY5K8zPAjosvD6ynkr0B

uCH+qOj3edjVQENg1JRVK89HqBQNMspbTUsZz2TEVKNH5xWtY0jp6vJm1DYDUqSu

bEMe3CeJpkeD9S8JZV/P4P9swPkK2ZiptOlskqqnmcK7ZrJbevb4GPvQ+wCUf2r8

t3ybYK5B1fyuX4L+h/GVdQWInS3Nt8hvyDyMeW7y7rC+6I0IJRLlaO9OtbbNZfIn

VR6NHQUatOvdb9HVwJKvPvpeF0PYtScUXus+mZrV6RXKtYrFEbUX9jcrVlq2ML2H

A92Pm2HzYILqvw/D2WQOCqZSKfpYr7jgekcGMBriisBlBq4D

-----END CERTIFICATE-----

### va_internal_ca2_s2_cert.pem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIEoDCCA4igAwIBAgITFAAAAAOX9+lYJSJG4QAAAAAAAzANBgkqhkiG9w0BAQsF

ADBKMRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExHzAd

BgNVBAMTFlZBLUludGVybmFsLVMyLVJDQTEtdjEwHhcNMTYxMDI2MTgzNDM4WhcN

MjYxMDI0MTgzNDM4WjBKMRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPy

LGQBGRYCdmExHzAdBgNVBAMTFlZBLUludGVybmFsLVMyLUlDQTItdjEwggEiMA0G

CSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQC9UaJu7b6BP9ffk9eZyAjCoLZHAQXD

QWiVrR1D1rkowF7cwSeoyPQ5yoMrH9TLQEb/GRVaL5UeHHw9bqbnXvMOgGuV1O64

vu42RDUEKofout/34LpBN9DC2JCsocNMVtwyoFuGJBYAeygZDNaLuI53tpzw74pa

WKoiD5pXtOoJkuARs2vMHD3kuzNeBdXFWo/l45gnZFpxmJo/Dr3wGzDDiO7h53S/

VVAaOXdPISVm1sieKtoLEinyy9qbkxdC7k1MdMJuYnRF92aZY+gezvpVqW7F1T8z

pT35wqbxbE1oqRAMlMEb7D5M19Kp/bWOfZ/zhWH6Y6lA91q4FsTsXxe1AgMBAAGj

ggF9MIIBeTAQBgkrBgEEAYI3FQEEAwIBADAdBgNVHQ4EFgQU71TwDfev76TpwXsl

gO+9o6wnA7cwPAYJKwYBBAGCNxUHBC8wLQYlKwYBBAGCNxUIgcjDM4H58AaBpZ8N

hOCBCIXCqksGg+96htu7FwIBZAIBEjALBgNVHQ8EBAMCAYYwEgYDVR0TAQH/BAgw

BgEB/wIBADAfBgNVHSMEGDAWgBQBLYthZhuM0ODTTD5O7FsZsBHGYTBJBgNVHR8E

QjBAMD6gPKA6hjhodHRwOi8vY3JsLnBraS52YS5nb3YvcGtpL2NybC9WQS1JbnRl

cm5hbC1TMi1SQ0ExLXYxLmNybDB7BggrBgEFBQcBAQRvMG0wRwYIKwYBBQUHMAKG

O2h0dHA6Ly9haWEucGtpLnZhLmdvdi9wa2kvYWlhL1ZBL1ZBLUludGVybmFsLVMy

LVJDQTEtdjEuY2VyMCIGCCsGAQUFBzABhhZodHRwOi8vb2NzcC5wa2kudmEuZ292

MA0GCSqGSIb3DQEBCwUAA4IBAQCX2482Kh858YMc2aYMek32bSZoMRRCKgNEwBBH

DwXpNu0zDjaxrvIPi+foEk/MvTn7PMSqcPYnuRw3IPCJ1uD00S/kUMMXJm3ON3l4

L4nmZz4BrhyZsYOyYHQJoE4KT2/Diw28XFJYH6FtDZnA105s3xnilg7NatBvBX0K

WayJ1ETJkp2aPlon9u+Tq/YE++Y0ek3MCozimRW/iWxzq2cd2UfNRyt2fJugAiJ2

S3AJbCWb5KTZi1ip9tRiHyXDxxcJ+N9FSQgZ1e/B62m9Xouh6VCTi3alCRY1MXSG

2+yUvBNmGIB0+tacbQAyXYEPAVHrE5B+VLs/7jrHDR5ap2ln

-----END CERTIFICATE-----

### betrusted_production_ssp_ca_a1_cert.txt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIG6DCCBdCgAwIBAgICAZowDQYJKoZIhvcNAQELBQAwWTELMAkGA1UEBhMCVVMxGDAWBgNVBAoT

D1UuUy4gR292ZXJubWVudDENMAsGA1UECxMERlBLSTEhMB8GA1UEAxMYRmVkZXJhbCBDb21tb24g

UG9saWN5IENBMB4XDTEwMTIwOTE5NTUyNFoXDTIwMTIwOTE5NDkwNFowgYgxCzAJBgNVBAYTAlVT

MRkwFwYDVQQKExBCZXRydXN0ZWQgVVMgSW5jMQwwCgYDVQQLEwNTU1AxJzAlBgNVBAsTHkJldHJ1

c3RlZCBQcm9kdWN0aW9uIFNTUCBDQSBBMTEnMCUGA1UEAxMeQmV0cnVzdGVkIFByb2R1Y3Rpb24g

U1NQIENBIEExMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAn2gPTEBKtvo7JnaOXE7F

YHlPYO5qXCVjbqe9LediLo3efZgsmFEK4otlL6lUC9PJAuIteeriLkOv9+momu08xX1FyJdYAWm/

moYRLVUMiCuDgJVLpw7FgmQh7FBBAW7IHeBvCYzUU4Ozh9VdYuxKkcA5sz9HgFL7RUyblMAPel79

JBpOdLvYEgBA+O25/VVLyeqD2wCQhkWkEIsWFDG1i6FjdVK/i1ot4kUj8nHS/o9uiIebYK+8lPg0

lK0jHhIzoxeTGDx9wiVmkZ/A3FRtramMEPQQaL2d//kY4tImmXW541hAn9SWy9Ur523tOxDpsNE1

VaN+7RU4Yt4Cxf6XrwIDAQABo4IDiDCCA4QwDwYDVR0TAQH/BAUwAwEB/zBPBgNVHSAESDBGMAwG

CmCGSAFlAwIBAwYwDAYKYIZIAWUDAgEDBzAMBgpghkgBZQMCAQMIMAwGCmCGSAFlAwIBAw0wDAYK

YIZIAWUDAgEDETCB6QYIKwYBBQUHAQEEgdwwgdkwPwYIKwYBBQUHMAKGM2h0dHA6Ly9odHRwLmZw

a2kuZ292L2ZjcGNhL2NhQ2VydHNJc3N1ZWRUb2ZjcGNhLnA3YzCBlQYIKwYBBQUHMAKGgYhsZGFw

Oi8vbGRhcC5mcGtpLmdvdi9jbj1GZWRlcmFsJTIwQ29tbW9uJTIwUG9saWN5JTIwQ0Esb3U9RlBL

SSxvPVUuUy4lMjBHb3Zlcm5tZW50LGM9VVM/Y0FDZXJ0aWZpY2F0ZTtiaW5hcnksY3Jvc3NDZXJ0

aWZpY2F0ZVBhaXI7YmluYXJ5MIIBJwYIKwYBBQUHAQsEggEZMIIBFTA+BggrBgEFBQcwBYYyaHR0

cDovL3NpYTEuc3NwLXN0cm9uZy1pZC5uZXQvQ0EvU1NQLUNBLUExLVNJQS5wN2MwgdIGCCsGAQUF

BzAFhoHFbGRhcDovL2RpcjEuc3NwLXN0cm9uZy1pZC5uZXQvY249QmV0cnVzdGVkJTIwUHJvZHVj

dGlvbiUyMFNTUCUyMENBJTIwQTEsb3U9QmV0cnVzdGVkJTIwUHJvZHVjdGlvbiUyMFNTUCUyMENB

JTIwQTEsb3U9U1NQLG89QmV0cnVzdGVkJTIwVVMlMjBJbmMsYz1VUz9jQUNlcnRpZmljYXRlO2Jp

bmFyeSxjcm9zc0NlcnRpZmljYXRlUGFpcjtiaW5hcnkwDgYDVR0PAQH/BAQDAgHGMB8GA1UdIwQY

MBaAFK0MenVc5fOYxHmYDqwo/Zf05wL8MIG4BgNVHR8EgbAwga0wKqAooCaGJGh0dHA6Ly9odHRw

LmZwa2kuZ292L2ZjcGNhL2ZjcGNhLmNybDB/oH2ge4Z5bGRhcDovL2xkYXAuZnBraS5nb3YvY24l

M2RGZWRlcmFsJTIwQ29tbW9uJTIwUG9saWN5JTIwQ0Esb3UlM2RGUEtJLG8lM2RVLlMuJTIwR292

ZXJubWVudCxjJTNkVVM/Y2VydGlmaWNhdGVSZXZvY2F0aW9uTGlzdDAdBgNVHQ4EFgQUu6TpuYML

MnIaIQ6qz0UdtxYjyA0wDQYJKoZIhvcNAQELBQADggEBAK+kk+1bsJuVspfA+lt3cJ9l8AIi8Ra4

rECJ2NqVdR9K4QdfNOmg0zAW2ybpvJ3ZD8y7vVzkzdkXwJsGMZMLKYK93d4I/TjsMyZMQFSWo9fV

Txn9El9ivIdzO+R27tYK8LIKhKSO0Q1I6kytzeXiWTwpXHH0YSUFpLNOr30gZUsuoWhpg/sb7VfQ

s+T2fNzXRRw3mqwbqQcx3WfdfLmfwCZC4gcirw1N0Sfo2GqgIc1/OzEL93tJh20SXPwJLkF2WN4k

HUmR1MQE0X8yQ+WYt6gl51qWKNXoQMm+TT2W3Y8tEOQGXd+nlCHiwKQyrPCLlL+EmFqyIN+lltvm

AxH6k1M=

-----END CERTIFICATE-----

### federal_common_policy_ca_cert.txt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIEYDCCA0igAwIBAgICATAwDQYJKoZIhvcNAQELBQAwWTELMAkGA1UEBhMCVVMxGDAWBgNVBAoT

D1UuUy4gR292ZXJubWVudDENMAsGA1UECxMERlBLSTEhMB8GA1UEAxMYRmVkZXJhbCBDb21tb24g

UG9saWN5IENBMB4XDTEwMTIwMTE2NDUyN1oXDTMwMTIwMTE2NDUyN1owWTELMAkGA1UEBhMCVVMx

GDAWBgNVBAoTD1UuUy4gR292ZXJubWVudDENMAsGA1UECxMERlBLSTEhMB8GA1UEAxMYRmVkZXJh

bCBDb21tb24gUG9saWN5IENBMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2HX7NRY0

WkG/Wq9cMAQUHK14RLXqJup1YcfNNnn4fNi9KVFmWSHjeavUeL6wLbCh1bI1FiPQzB6+Duir3MPJ

1hLXp3JoGDG4FyKyPn66CG3G/dFYLGmgA/Aqo/Y/ISU937cyxY4nsyOl4FKzXZbpsLjFxZ+7xaBu

gkC7xScFNknWJidpDDSPzyd6KgqjQV+NHQOGgxXgVcHFmCye7Bpy3EjBPvmE0oSCwRvDdDa3ucc2

Mnr4MrbQNq4iGDGMUHMhnv6DOzCIJOPpwX7e7ZjHH5IQip9bYi+dpLzVhW86/clTpyBLqtsgqyFO

HQ1O5piF5asRR12dP8QjwOMUBm7+nQIDAQABo4IBMDCCASwwDwYDVR0TAQH/BAUwAwEB/zCB6QYI

KwYBBQUHAQsEgdwwgdkwPwYIKwYBBQUHMAWGM2h0dHA6Ly9odHRwLmZwa2kuZ292L2ZjcGNhL2Nh

Q2VydHNJc3N1ZWRCeWZjcGNhLnA3YzCBlQYIKwYBBQUHMAWGgYhsZGFwOi8vbGRhcC5mcGtpLmdv

di9jbj1GZWRlcmFsJTIwQ29tbW9uJTIwUG9saWN5JTIwQ0Esb3U9RlBLSSxvPVUuUy4lMjBHb3Zl

cm5tZW50LGM9VVM/Y0FDZXJ0aWZpY2F0ZTtiaW5hcnksY3Jvc3NDZXJ0aWZpY2F0ZVBhaXI7Ymlu

YXJ5MA4GA1UdDwEB/wQEAwIBBjAdBgNVHQ4EFgQUrQx6dVzl85jEeZgOrCj9l/TnAvwwDQYJKoZI

hvcNAQELBQADggEBAI9z2uF/gLGH9uwsz9GEYx728Yi3mvIRte9UrYpuGDco71wb5O9Qt2wmGCMi

TR0mRyDpCZzicGJxqxHPkYnos/UqoEfAFMtOQsHdDA4b8Idb7OV316rgVNdF9IU+7LQd3nyKf1tN

nJaK0KIyn9psMQz4pO9+c+iR3Ah6cFqgr2KBWfgAdKLI3VTKQVZHvenAT+0g3eOlCd+uKML80cgX

2BLHb94u6b2akfI8WpQukSKAiaGMWMyDeiYZdQKlDn0KJnNR6obLB6jI/WNaNZvSr79PMUjBhHDb

NXuaGQ/lj/RqDG8z2esccKIN47lQA2EC/0rskqTcLe4qNJMHtyznGI8=

-----END CERTIFICATE-----

### veterans_affairs_device_ca_b2_cert.txt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIHVTCCBj2gAwIBAgICHGAwDQYJKoZIhvcNAQEFBQAwgYgxCzAJBgNVBAYTAlVTMRkwFwYDVQQK

ExBCZXRydXN0ZWQgVVMgSW5jMQwwCgYDVQQLEwNTU1AxJzAlBgNVBAsTHkJldHJ1c3RlZCBQcm9k

dWN0aW9uIFNTUCBDQSBBMTEnMCUGA1UEAxMeQmV0cnVzdGVkIFByb2R1Y3Rpb24gU1NQIENBIEEx

MB4XDTA4MDgwNzE1MjQwMFoXDTE4MDgwNzE1MjI0NlowcjETMBEGCgmSJomT8ixkARkWA2dvdjES

MBAGCgmSJomT8ixkARkWAnZhMREwDwYDVQQLEwhTZXJ2aWNlczEMMAoGA1UECxMDUEtJMSYwJAYD

VQQDEx1WZXRlcmFucyBBZmZhaXJzIERldmljZSBDQSBCMjCCASIwDQYJKoZIhvcNAQEBBQADggEP

ADCCAQoCggEBALTxrfB9i65LBlPlCvdruZNIsSG3WY0JxNQfIxTBZqsOneWFnR2wElFzhkxvjQRx

vQAfqz1gBum5cMl+7BmoFF9ueRP5uQGF++f+2leQ7HE+5cqw9DlQ4wBtlE/zRrcOPqhQ9Usybq44

XCLneNvQ56nGyw/KxgyqgycUqojDIqWOIdQ/e12jSxa5qCmrzdLsEFpx9kVuWz8Wvn4K5VWOV/Pb

EMhvOmdxpXwEBwUALqhGbTBeq52N0UG1wgoJJRii0uR5T+bK8QJ+NF7vzmnReWudTFhV3av9WZhu

7banQGcS66HBc1h22FlYDefq2yEHpgmPOBvv8EC+3I1DnNh519cCAwEAAaOCA9wwggPYMA8GA1Ud

EwEB/wQFMAMBAf8wTwYDVR0gBEgwRjAMBgpghkgBZQMCAQMGMAwGCmCGSAFlAwIBAwcwDAYKYIZI

AWUDAgEDCDAMBgpghkgBZQMCAQMNMAwGCmCGSAFlAwIBAxEwggE+BggrBgEFBQcBAQSCATAwggEs

MDoGCCsGAQUFBzAChi5odHRwOi8vYWlhMS5zc3Atc3Ryb25nLWlkLm5ldC9DQS9TU1AtQ0EtQTEu

cDdjMIG2BggrBgEFBQcwAoaBqWxkYXA6Ly9kaXIxLnNzcC1zdHJvbmctaWQubmV0L2NuPUJldHJ1

c3RlZCUyMFByb2R1Y3Rpb24lMjBTU1AlMjBDQSUyMEExLG91PUJldHJ1c3RlZCUyMFByb2R1Y3Rp

b24lMjBTU1AlMjBDQSUyMEExLG91PVNTUCxvPUJldHJ1c3RlZCUyMFVTJTIwSW5jLGM9VVM/Y0FD

ZXJ0aWZpY2F0ZTtiaW5hcnkwNQYIKwYBBQUHMAGGKWh0dHA6Ly9vY3NwMS5zc3Atc3Ryb25nLWlk

Lm5ldC9TU1AtQ0EtQTEvMIHXBggrBgEFBQcBCwSByjCBxzA7BggrBgEFBQcwA4YvaHR0cDovL2Fp

YTEuc3NwLXN0cm9uZy1pZC5uZXQvQ0EvVkFkZXZpY2VDQS5wN2MwgYcGCCsGAQUFBzADhntsZGFw

Oi8vZGlyMS5zc3Atc3Ryb25nLWlkLm5ldC9jbj1WZXRlcmFucyUyMEFmZmFpcnMlMjBEZXZpY2Ul

MjBDQSUyMEIyLG91PVBLSSxvdT1TZXJ2aWNlcyxkYz12YSxkYz1nb3Y/Y0FDZXJ0aWZpY2F0ZTti

aW5hcnkwDgYDVR0PAQH/BAQDAgHGMB8GA1UdIwQYMBaAFLuk6bmDCzJyGiEOqs9FHbcWI8gNMIIB

BgYDVR0fBIH+MIH7MDWgM6Axhi9odHRwOi8vY2RwMS5zc3Atc3Ryb25nLWlkLm5ldC9DRFAvU1NQ

LUNBLUExLmNybDCBwaCBvqCBu4aBuGxkYXA6Ly9kaXIxLnNzcC1zdHJvbmctaWQubmV0L2NuJTNk

QmV0cnVzdGVkJTIwUHJvZHVjdGlvbiUyMFNTUCUyMENBJTIwQTEsb3UlM2RCZXRydXN0ZWQlMjBQ

cm9kdWN0aW9uJTIwU1NQJTIwQ0ElMjBBMSxvdSUzZFNTUCxvJTNkQmV0cnVzdGVkJTIwVVMlMjBJ

bmMsYyUzZFVTP2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3QwHQYDVR0OBBYEFIGUNZ4qqHdgI2bs

Kp1uz7Z1GVBdMA0GCSqGSIb3DQEBBQUAA4IBAQBTnvlRJn0nM90ddSlQ6dX4nEB6LU7UEjESjgbt

b1Nx0IPcw+muXo4NYExTLIRJrlkOI/MSaITk0UAnSALFfLPom36SdSQ9rjxKEkqO+4/FCcScH7wE

Crw5k1AfRdsqR5cgDJlfj+sPMCYpMX0vydIiUwkpoqGKQVA0V8AI9/Z1VpmpuvWc8kogqfs+Hly6

lg3JsJ2jiLFkSO+sbwN9ZqOQTOQgFPFbScZJKV1g8jTEo0YoX/w+nSHjK5EMJwIz6yo1J8wvmjcN

1VlS3hkjxrOOqSf0/I+nz2hgybR/nkft3zk1zKeH4NPmug0F48mGSRsnkHzksGE8iSaCPkz3snJQ

-----END CERTIFICATE-----

### vaww.esrdev.aac.<span class="mark">REDACTED</span>\_cert.txt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIHizCCBnOgAwIBAgIDBTdaMA0GCSqGSIb3DQEBCwUAMHIxEzARBgoJkiaJk/IsZAEZFgNnb3Yx

EjAQBgoJkiaJk/IsZAEZFgJ2YTERMA8GA1UECxMIU2VydmljZXMxDDAKBgNVBAsTA1BLSTEmMCQG

A1UEAxMdVmV0ZXJhbnMgQWZmYWlycyBEZXZpY2UgQ0EgQjIwHhcNMTUwOTE0MTcxNDI3WhcNMTgw

ODA3MTUyMjQ2WjBcMRMwEQYKCZImiZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExEDAO

BgNVBAsTB2RldmljZXMxHzAdBgNVBAMTFnZhd3cuZXNyZGV2LmFhYy52YS5nb3YwggEiMA0GCSqG

SIb3DQEBAQUAA4IBDwAwggEKAoIBAQCkYcAL0+9HukeVKIzrs0gKOhDskClbu0oOJDGjc0t72mOz

2rgj4+79J6AExovcy7nYiAsGYEmFMhwmDl3v3+aLk8E7P8xf5KFENycYhuxBI61llO0CISs7Wk2h

prkGHR0HkTyxuuUknwzhQ+9qm3CqMGDVhXqNuEwWQoJ3us22drK4NBrZn+dMTeTlKHSo9QeoICWc

bqoueoKWlOFl7UlnAaCGrABMoncEO+b9QDZB5i83IxMuZFlhwve6JHsOXKe0t3H8WbKy9M3+kOtc

xMTMOVesj7p+3mqDn/ckozRyDkMHc0SZs3jSpRr43IYIpDU4R2SOxgVq0O1f7/J+WIHrAgMBAAGj

ggQ+MIIEOjCB7AYDVR0RBIHkMIHhghZ2YXd3LmVzcmRldi5hYWMudmEuZ292ghh2YXd3LmVzcmRl

djMwLmFhYy52YS5nb3aCGHZhd3cuZXNyZGV2MzEuYWFjLnZhLmdvdoIYdmF3dy5lc3JkZXY0MC5h

YWMudmEuZ292ghV2aGFlc3J3ZWIzLmFhYy52YS5nb3aCF3Zhd3cuZXNyZGV2MS5hYWMudmEuZ292

ghd2YXd3LmVzcmRldjIuYWFjLnZhLmdvdoIXdmF3dy5lc3JkZXYzLmFhYy52YS5nb3aCF3Zhd3cu

ZXNyZGV2NC5hYWMudmEuZ292MBcGA1UdIAQQMA4wDAYKYIZIAWUDAgEDCDCCATAGCCsGAQUFBwEB

BIIBIjCCAR4wOwYIKwYBBQUHMAKGL2h0dHA6Ly9haWExLnNzcC1zdHJvbmctaWQubmV0L0NBL1ZB

ZGV2aWNlQ0EucDdjMIGABggrBgEFBQcwAoZ0bGRhcDovL2RpcjEuc3NwLXN0cm9uZy1pZC5uZXQv

Y249VmV0ZXJhbnMlMjBBZmZhaXJzJTIwRGV2aWNlJTIwQ0ElMjBCMixvdT1QS0ksb3U9U2Vydmlj

ZXMsZGM9dmEsZGM9Z292P2NBQ2VydGlmaWNhdGUwIwYIKwYBBQUHMAGGF2h0dHA6Ly9vY3NwLnBr

aS52YS5nb3YvMDcGCCsGAQUFBzABhitodHRwOi8vb2NzcDEuc3NwLXN0cm9uZy1pZC5uZXQvVkEt

U1NQLUNBLUIyMA4GA1UdDwEB/wQEAwIFoDAnBgNVHSUEIDAeBggrBgEFBQcDAQYIKwYBBQUHAwIG

CGCGSAFlAwYHMB8GA1UdIwQYMBaAFIGUNZ4qqHdgI2bsKp1uz7Z1GVBdMIIBgQYDVR0fBIIBeDCC

AXQwMKAuoCyGKmh0dHA6Ly9jcmwucGtpLnZhLmdvdi9QS0kvQ1JML3ZhZGV2aWNlLmNybDB0oHKg

cIZubGRhcDovL2xkYXAucGtpLnZhLmdvdi9jbiUzZFNTUEIyQUUsY24lM2RDRFAsY24lM2RQS0ks

Y24lM2RTZXJ2aWNlcyxkYyUzZHZhLGRjJTNkZ292P2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3Qw

NKAyoDCGLmh0dHA6Ly9jZHAxLnNzcC1zdHJvbmctaWQubmV0L0NEUC92YWRldmljZS5jcmwwgZOg

gZCggY2GgYpsZGFwOi8vZGlyMS5zc3Atc3Ryb25nLWlkLm5ldC9jbiUzZFZldGVyYW5zJTIwQWZm

YWlycyUyMERldmljZSUyMENBJTIwQjIsb3UlM2RQS0ksb3UlM2RTZXJ2aWNlcyxkYyUzZHZhLGRj

JTNkZ292P2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3QwHQYDVR0OBBYEFFauWBgfqlovaoQ/3SJE

igCTXVyhMA0GCSqGSIb3DQEBCwUAA4IBAQAYuPXvhL4/ElzooFV5fAbwm822Vz7U49ZF/JSEBQqG

QBhmwbFCu7wklIu40Efkzj2nSfAeGzijfh1eaTiLC1q+wpqh5ezl3kzBJNAUTmPlJZQfVGHX0rFQ

AvOqFs5YNakKkthHnbQAWvJ1n1Bje1on6YFu3L5eeJDwdO2CBUboK/fc/m8Nxe47UTsoRG1uin6Y

8P9QglpJT6HqSHQsqanLkncU3wTh2vyJUtfMuJq0nBDvBg3PCxtoU2/wqkdFY+UEKHTjYXXkxPuX

NVHQ6sdQNq3y584edm9phxMW2rmbxEN0oN7oQWUPBEACrtrK84MxM1w6WTShl6YMV/dQz8ho

-----END CERTIFICATE-----

### vaww.esrstage1a.aac.<span class="mark">REDACTED</span>.pem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIFiDCCBHCgAwIBAgIHPQAAAAC3pjANBgkqhkiG9w0BAQsFADBKMRMwEQYKCZIm

iZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExHzAdBgNVBAMTFlZBLUlu

dGVybmFsLVMyLUlDQTEtdjEwHhcNMTcwMzE0MjA1NjQ3WhcNMjAwMzEzMjA1NjQ3

WjCBwDELMAkGA1UEBhMCVVMxDjAMBgNVBAgTBVRleGFzMQ8wDQYDVQQHEwZBdXN0

aW4xKjAoBgNVBAoTIVVTIERlcGFydG1lbnQgb2YgVmV0ZXJhbnMgQWZmYWlyczEN

MAsGA1UECxMEQUlUQzEjMCEGA1UEAxMadmF3dy5lc3JzdGFnZTFhLmFhYy52YS5n

b3YxMDAuBgkqhkiG9w0BCQEWIWNkY293ZWJsb2dpY2FkbWluaXN0cmF0b3JzQHZh

LmdvdjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAPvu747uobthNU4I

8GOjiQ2R3WY2F+LWYznx+6xaPSUyaawXZ8heBNngo5CbkyWhQPpuDBAjpUjiYX9Q

9AMlLhJppZEi8NmBLFkojISALEl/+3LM8NhFnA1wNCrMSjDY2HL688X277VKjgcJ

qFnF8KdldeGh9fpDnWXDWITHhO2HzYojKu415jb+GicjzB/rI+RoYftY6MDQpLcu

ltVv9SXrnDLkebe+3fKOhmrecvUhFwdYClx1V5o55iDipZlLSxAAw0RHho8wXxBm

7J7c5SN150YV5Dsido6Ui4Rroe2ewiizQsVKNe9MOsw2agIUsx+LhIY49S/s/Nzl

hcYs2qUCAwEAAaOCAfowggH2MAsGA1UdDwQEAwIFoDBYBgNVHREEUTBPghp2YXd3

LmVzcnN0YWdlMWEuYWFjLnZhLmdvdoIadmF3dy5lc3JzdGFnZTFhLmFhYy52YS5n

b3aCFXZoYWVzcndlYjYuYWFjLnZhLmdvdjAdBgNVHQ4EFgQUnkF4Y5jfPVwdOyv/

XYljZLS7r/YwHwYDVR0jBBgwFoAUG23f6z3l4g3vFrHQ3l9YGlbL5OwwSQYDVR0f

BEIwQDA+oDygOoY4aHR0cDovL2NybC5wa2kudmEuZ292L3BraS9jcmwvVkEtSW50

ZXJuYWwtUzItSUNBMS12MS5jcmwwewYIKwYBBQUHAQEEbzBtMEcGCCsGAQUFBzAC

hjtodHRwOi8vYWlhLnBraS52YS5nb3YvcGtpL2FpYS92YS9WQS1JbnRlcm5hbC1T

Mi1JQ0ExLXYxLmNlcjAiBggrBgEFBQcwAYYWaHR0cDovL29jc3AucGtpLnZhLmdv

djA9BgkrBgEEAYI3FQcEMDAuBiYrBgEEAYI3FQiByMMzgfnwBoGlnw2E4IEIhcKq

SwaDgp9ggeCLUgIBZAIBEjAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwEw

JwYJKwYBBAGCNxUKBBowGDAKBggrBgEFBQcDAjAKBggrBgEFBQcDATANBgkqhkiG

9w0BAQsFAAOCAQEAhm1jRtWAEQStJz2uPw8piDho8Iit3dz2j2/Zy0bmhbg7e1Fg

jg4xR2qv4CpNuNinxgMhsrlXV7roxY9UVK3CkmT6Js5DFuR0yQ9u4WsdM0NxxvEa

Keh3hPwBRelcSKbMefn071CObMLz9qSf9gMQ34vhlKzmVxftn5FBK8LNE/a6uoDv

FxovRmOAa/qMGMZdMZEmb144+hAngFbFmwXkOFDQOlDBG8SAYfklUNfBw92u+3jV

UApxi9bvnulp8UyHsG9QEa+fs49v1qhp4UGiY7CWLhnZbaHNLoYhpioVSruPnMa+

a4vuHW2QSxKVTY+2P3gJpXoUlSLoAJJtKi2njw==

-----END CERTIFICATE-----

### vaww.esrstage1b.aac.<span class="mark">REDACTED</span>.pem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIFiDCCBHCgAwIBAgIHPQAAAAC3pzANBgkqhkiG9w0BAQsFADBKMRMwEQYKCZIm

iZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExHzAdBgNVBAMTFlZBLUlu

dGVybmFsLVMyLUlDQTEtdjEwHhcNMTcwMzE0MjEwNzA5WhcNMjAwMzEzMjEwNzA5

WjCBwDELMAkGA1UEBhMCVVMxDjAMBgNVBAgTBVRleGFzMQ8wDQYDVQQHEwZBdXN0

aW4xKjAoBgNVBAoTIVVTIERlcGFydG1lbnQgb2YgVmV0ZXJhbnMgQWZmYWlyczEN

MAsGA1UECxMEQUlUQzEjMCEGA1UEAxMadmF3dy5lc3JzdGFnZTFiLmFhYy52YS5n

b3YxMDAuBgkqhkiG9w0BCQEWIWNkY293ZWJsb2dpY2FkbWluaXN0cmF0b3JzQHZh

LmdvdjCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAOKj1U0RxzhQg8ij

tPGY1wH7q5TDfsSvQUoPBbgOF53MYR8VotqM0JViggyP4G/TmYJ/HMvaP/2K1tS5

60hHGIPMg01Xa9ZbxhR6u8rp/A7QiX96jkWzHuuP4OEijW9j23xGcfx3lLaeL4HF

amhrYnIDpYBPkgqltVNLHBQiNJE/FcReCpbhHrHFJyr0L+dmkjQWC/CL44qtsIeo

dM67p87NswOKcaiRsbVw+CosJFZH6WGKgTFDuYyn9ZNpPeBRBUmdS770SCAKukGY

1WIFBXm1AjckGjVUoE9f5N0D8tSPrfyxnxpSIOHcCtkYLwujl4oGj0Iuee9qisn5

jkYVulcCAwEAAaOCAfowggH2MAsGA1UdDwQEAwIFoDBYBgNVHREEUTBPghp2YXd3

LmVzcnN0YWdlMWIuYWFjLnZhLmdvdoIadmF3dy5lc3JzdGFnZTFiLmFhYy52YS5n

b3aCFXZoYWVzcndlYjQuYWFjLnZhLmdvdjAdBgNVHQ4EFgQU61ixAn4MoiuQ4n41

gmSf+uKn4TUwHwYDVR0jBBgwFoAUG23f6z3l4g3vFrHQ3l9YGlbL5OwwSQYDVR0f

BEIwQDA+oDygOoY4aHR0cDovL2NybC5wa2kudmEuZ292L3BraS9jcmwvVkEtSW50

ZXJuYWwtUzItSUNBMS12MS5jcmwwewYIKwYBBQUHAQEEbzBtMEcGCCsGAQUFBzAC

hjtodHRwOi8vYWlhLnBraS52YS5nb3YvcGtpL2FpYS92YS9WQS1JbnRlcm5hbC1T

Mi1JQ0ExLXYxLmNlcjAiBggrBgEFBQcwAYYWaHR0cDovL29jc3AucGtpLnZhLmdv

djA9BgkrBgEEAYI3FQcEMDAuBiYrBgEEAYI3FQiByMMzgfnwBoGlnw2E4IEIhcKq

SwaDgp9ggeCLUgIBZAIBEjAdBgNVHSUEFjAUBggrBgEFBQcDAgYIKwYBBQUHAwEw

JwYJKwYBBAGCNxUKBBowGDAKBggrBgEFBQcDAjAKBggrBgEFBQcDATANBgkqhkiG

9w0BAQsFAAOCAQEAFNLz/wWJSdzIVUGd4bzXTAXktnnP1IanNIrLbW3qNoWyi1ft

4uNL6E5LFsDTMohvwjOGHaphdJmAp9HD4ZJlTWXblXNXe2yPa6jCKspJVc2j42ls

fws0ZxOUeelS/XQZWNjs6qbEOOsJ4PtwOb1Myq/1V1tTWAOTZu3snjH1pVyHmHZ6

35i4mHmZJtHmEVlDg3DzrTvw0ejzgnq3MpvN25Np+Msi0uyLT8qcUjhWgrJS2Aw5

2qyA2n9vfQTcmg5U6eSyzJl4gCoG5xhZaHAmTW4FySAwmcqKyjM4hkySTSKKLqSZ

5Q65eFKajsUIW+jXD63HuiweHP8vrzl/4M1Vkg==

-----END CERTIFICATE-----

### vaww.esrpre-prod.aac.<span class="mark">REDACTED</span>.pem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIFojCCBIqgAwIBAgIHPQAAAADC6jANBgkqhkiG9w0BAQsFADBKMRMwEQYKCZIm

iZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExHzAdBgNVBAMTFlZBLUlu

dGVybmFsLVMyLUlDQTEtdjEwHhcNMTcwNDA0MTEzMzAxWhcNMjAwNDAzMTEzMzAx

WjCBwTELMAkGA1UEBhMCVVMxDjAMBgNVBAgTBVRleGFzMQ8wDQYDVQQHEwZBdXN0

aW4xKjAoBgNVBAoTIVVTIERlcGFydG1lbnQgb2YgVmV0ZXJhbnMgQWZmYWlyczEN

MAsGA1UECxMEQUlUQzEkMCIGA1UEAxMbdmF3dy5lc3JwcmUtcHJvZC5hYWMudmEu

Z292MTAwLgYJKoZIhvcNAQkBFiFjZGNvd2VibG9naWNhZG1pbmlzdHJhdG9yc0B2

YS5nb3YwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDSSFJ9AnbkaLXB

J7ngjAHzGnkTQM8eKl3k7iYUKLYjhmH9ZuIiYQQEVqh1bsM+YlvdFXLjc1Vg7P10

ntkSG/QBz6VDhd8RkeOjEkLmT4/88VZnlbGRAApaVp3UM6dy5r9fkN0yRgoUBVqS

hPaj0m2Z6UQkKz589eS0lCCWSWzl5K6dFDFvIqmmb0yyfvZ8+lP7BqbI7cOsJAhx

5sDzBKAR3JVsGM+7f5oX/euIyuRagrBcbQPrG6Moc5owEkH6t1s2+m6BiVHENIBn

sGHaIWhq+b1zsQ9vwYjc/9bGHJ7D928la/LRPErsWKL2uSqQcHA7PfJm8wLpkO5Y

+/O7iyNVAgMBAAGjggITMIICDzALBgNVHQ8EBAMCBaAwcQYDVR0RBGowaIIbdmF3

dy5lc3JwcmUtcHJvZC5hYWMudmEuZ292ght2YXd3LmVzcnByZS1wcm9kLmFhYy52

YS5nb3aCFXZoYWVzcndlYjcuYWFjLnZhLmdvdoIVdmhhZXNyd2ViOC5hYWMudmEu

Z292MB0GA1UdDgQWBBQJAFTUt3mxMbBdr/ODTQUQMY2WBjAfBgNVHSMEGDAWgBQb

bd/rPeXiDe8WsdDeX1gaVsvk7DBJBgNVHR8EQjBAMD6gPKA6hjhodHRwOi8vY3Js

LnBraS52YS5nb3YvcGtpL2NybC9WQS1JbnRlcm5hbC1TMi1JQ0ExLXYxLmNybDB7

BggrBgEFBQcBAQRvMG0wRwYIKwYBBQUHMAKGO2h0dHA6Ly9haWEucGtpLnZhLmdv

di9wa2kvYWlhL3ZhL1ZBLUludGVybmFsLVMyLUlDQTEtdjEuY2VyMCIGCCsGAQUF

BzABhhZodHRwOi8vb2NzcC5wa2kudmEuZ292MD0GCSsGAQQBgjcVBwQwMC4GJisG

AQQBgjcVCIHIwzOB+fAGgaWfDYTggQiFwqpLBoOCn2CB4ItSAgFkAgESMB0GA1Ud

JQQWMBQGCCsGAQUFBwMCBggrBgEFBQcDATAnBgkrBgEEAYI3FQoEGjAYMAoGCCsG

AQUFBwMCMAoGCCsGAQUFBwMBMA0GCSqGSIb3DQEBCwUAA4IBAQAgJ6f4AoV7lndB

myYN1S76+rZGccqOoHKSF074o06os8b8qcRSctJOIRxzWME8wiy55PHS5nkhn0wm

oWna2P6Efec2FQ8ZURsbi8IefwUX7ISWJ99+6C+lL6VrCH1hEQOPXTRdbQm8H3dR

cvhlHNQ3MtXuswI3sFvBqmYFsXsOtRwiRzFuiT7K4v5kW3Kkre5bsjSLBXq1VFjT

PTVMIcH3QgP6hbjfgJtQoHfDoQPFSa6DjbGvja4Y+rQMqiBC1VN1ZLG44VqsDlyC

u5AO830gi/ilgf30Iyv1Jl/mXJT1LdAUZjG5dPtwT4/Jx3KqJ7cDWdy54ddD1RJb

IyXeTQaF

-----END CERTIFICATE-----

<span class="mark">  
</span>

### das-test.<span class="mark">REDACTED</span>.pem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIG7TCCBdWgAwIBAgIDBZSiMA0GCSqGSIb3DQEBCwUAMHIxEzARBgoJkiaJk/Is

ZAEZFgNnb3YxEjAQBgoJkiaJk/IsZAEZFgJ2YTERMA8GA1UECxMIU2VydmljZXMx

DDAKBgNVBAsTA1BLSTEmMCQGA1UEAxMdVmV0ZXJhbnMgQWZmYWlycyBEZXZpY2Ug

Q0EgQjIwHhcNMTYwNjEwMTMxOTUwWhcNMTgwODA3MTUyMjQ2WjBVMRMwEQYKCZIm

iZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExEDAOBgNVBAsTB2Rldmlj

ZXMxGDAWBgNVBAMTD2Rhcy10ZXN0LnZhLmdvdjCCASIwDQYJKoZIhvcNAQEBBQAD

ggEPADCCAQoCggEBAKJg1wPGT7WrI1FYJ5HkivoJKwR3nulq6n9hD3m+ENXlRbDP

HOrTxOXg2YpSK/ORRdVBN4OXD+NVaVyv4XyWzG2ZIF06wGX9ooGTU2EA/MMKh3ts

XDWTBOIEGjDQ3CUnCZ2J3FF+SSBYtRFRI1CqYt/77kC4GafjDsFy6MfiXdis9O6R

RSaXPCFdF7qRqq3Lx8Qr1sP5rYj4f95HRGKqn4X/5S1z5Us8O+ZReWALUAMtAWr6

ZZ5B8CYhcSxPsvPw7wNl5IYjKGe9/DaXeszHKF7tW3VPOg6/g8gSVsOBVlVayUWx

IjzeXen1DWpusmLkD7a9aVeB1E1+W0amYXmGEUMCAwEAAaOCA6cwggOjMFYGA1Ud

EQRPME2CD2Rhcy10ZXN0LnZhLmdvdoIcdmFhdXNkYXNhcHBpbnQwMDIuYWFjLnZh

LmdvdoIcdmFhdXNkYXNhcHBpbnQwMDMuYWFjLnZhLmdvdjAXBgNVHSAEEDAOMAwG

CmCGSAFlAwIBAwgwggEwBggrBgEFBQcBAQSCASIwggEeMDsGCCsGAQUFBzAChi9o

dHRwOi8vYWlhMS5zc3Atc3Ryb25nLWlkLm5ldC9DQS9WQWRldmljZUNBLnA3YzCB

gAYIKwYBBQUHMAKGdGxkYXA6Ly9kaXIxLnNzcC1zdHJvbmctaWQubmV0L2NuPVZl

dGVyYW5zJTIwQWZmYWlycyUyMERldmljZSUyMENBJTIwQjIsb3U9UEtJLG91PVNl

cnZpY2VzLGRjPXZhLGRjPWdvdj9jQUNlcnRpZmljYXRlMCMGCCsGAQUFBzABhhdo

dHRwOi8vb2NzcC5wa2kudmEuZ292LzA3BggrBgEFBQcwAYYraHR0cDovL29jc3Ax

LnNzcC1zdHJvbmctaWQubmV0L1ZBLVNTUC1DQS1CMjAOBgNVHQ8BAf8EBAMCBaAw

JwYDVR0lBCAwHgYIKwYBBQUHAwEGCCsGAQUFBwMCBghghkgBZQMGBzAfBgNVHSME

GDAWgBSBlDWeKqh3YCNm7Cqdbs+2dRlQXTCCAYEGA1UdHwSCAXgwggF0MDCgLqAs

hipodHRwOi8vY3JsLnBraS52YS5nb3YvUEtJL0NSTC92YWRldmljZS5jcmwwdKBy

oHCGbmxkYXA6Ly9sZGFwLnBraS52YS5nb3YvY24lM2RTU1BCMkFFLGNuJTNkQ0RQ

LGNuJTNkUEtJLGNuJTNkU2VydmljZXMsZGMlM2R2YSxkYyUzZGdvdj9jZXJ0aWZp

Y2F0ZVJldm9jYXRpb25MaXN0MDSgMqAwhi5odHRwOi8vY2RwMS5zc3Atc3Ryb25n

LWlkLm5ldC9DRFAvdmFkZXZpY2UuY3JsMIGToIGQoIGNhoGKbGRhcDovL2RpcjEu

c3NwLXN0cm9uZy1pZC5uZXQvY24lM2RWZXRlcmFucyUyMEFmZmFpcnMlMjBEZXZp

Y2UlMjBDQSUyMEIyLG91JTNkUEtJLG91JTNkU2VydmljZXMsZGMlM2R2YSxkYyUz

ZGdvdj9jZXJ0aWZpY2F0ZVJldm9jYXRpb25MaXN0MB0GA1UdDgQWBBRJxg3+eZpU

APnLc56q/SjzkLYrFzANBgkqhkiG9w0BAQsFAAOCAQEAYW2JnS8JhfoGH0DTQrYr

bw8ZXEjGW/jwG1rVzsRNRt3ncBLdj2Zis0QjDo9mArG5s/xHpa35aQZjUGQAgv/t

wZ3jl1lH0jZIAch6tn7YRzhpqA7u5ozf8eUTpuAeJtVFeIo9RUR871DWWYpWPMw7

D4LGcLB4HpLfBb/4BMXQnM1cyCsXYSkXDQHl+xPzUUQkJpi7JRdoMLPxZ2r9ewJf

dDbn8FEnxmNkI15G7qCmaW2cmfitnsJ8hoZC+rLL7B3+0/kzZL3O2yzX2WXmUWzk

Z3Mf3C9K+LOWsrTwVUOkiVJL6xrbI6j2dOGpgShDnn7d5+ftgHsXi3GdbEHYx2Ah

4w==

-----END CERTIFICATE-----

### das-sqa.<span class="mark">REDACTED</span>.pem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIG7DCCBdSgAwIBAgIDBbrgMA0GCSqGSIb3DQEBCwUAMHIxEzARBgoJkiaJk/Is

ZAEZFgNnb3YxEjAQBgoJkiaJk/IsZAEZFgJ2YTERMA8GA1UECxMIU2VydmljZXMx

DDAKBgNVBAsTA1BLSTEmMCQGA1UEAxMdVmV0ZXJhbnMgQWZmYWlycyBEZXZpY2Ug

Q0EgQjIwHhcNMTYwODI2MTY0NzE3WhcNMTgwODA3MTUyMjQ2WjBUMRMwEQYKCZIm

iZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExEDAOBgNVBAsTB2Rldmlj

ZXMxFzAVBgNVBAMTDmRhcy1zcWEudmEuZ292MIIBIjANBgkqhkiG9w0BAQEFAAOC

AQ8AMIIBCgKCAQEAqRt193fnTlYYwqxiC6XMCcOOsJorP1Wop43czuqGH0P3Z2uj

f5ubSi8jfvqQGhuWVJ6mjAxJQevjpuFddu3GGWMVvofa96wA852qdMcXtj8z9exH

L1rN86o+8CkU7yj9iFsasSWf0a0CLK3jz+GiGakmtztnoZoXc2T+e3NaJhASIdjU

IZH5hVB4qi4PgmCW6rL7SAOetcCtMtaAFS0DK8s+VLxSeAzDjvybAc6jXgUXDYNK

Dr3HtWDy3AKz3kOkva4ipDnxrcNKPJN01EM+RKMy7s23BjmBq3EHnB+4fT6t62DL

OJhKqQ7jqJCBLoNeEHnth7+i3VVL0N4eEqPxoQIDAQABo4IDpzCCA6MwVgYDVR0R

BE8wTYIOZGFzLXNxYS52YS5nb3aCHHZhYXVzZGFzYXBwc3FhMDAxLmFhYy52YS5n

b3aCHXZhYXVzZGFzYXBwc3FhMDAyLmFhYy52YS5nb3YgMBcGA1UdIAQQMA4wDAYK

YIZIAWUDAgEDCDCCATAGCCsGAQUFBwEBBIIBIjCCAR4wOwYIKwYBBQUHMAKGL2h0

dHA6Ly9haWExLnNzcC1zdHJvbmctaWQubmV0L0NBL1ZBZGV2aWNlQ0EucDdjMIGA

BggrBgEFBQcwAoZ0bGRhcDovL2RpcjEuc3NwLXN0cm9uZy1pZC5uZXQvY249VmV0

ZXJhbnMlMjBBZmZhaXJzJTIwRGV2aWNlJTIwQ0ElMjBCMixvdT1QS0ksb3U9U2Vy

dmljZXMsZGM9dmEsZGM9Z292P2NBQ2VydGlmaWNhdGUwIwYIKwYBBQUHMAGGF2h0

dHA6Ly9vY3NwLnBraS52YS5nb3YvMDcGCCsGAQUFBzABhitodHRwOi8vb2NzcDEu

c3NwLXN0cm9uZy1pZC5uZXQvVkEtU1NQLUNBLUIyMA4GA1UdDwEB/wQEAwIFoDAn

BgNVHSUEIDAeBggrBgEFBQcDAQYIKwYBBQUHAwIGCGCGSAFlAwYHMB8GA1UdIwQY

MBaAFIGUNZ4qqHdgI2bsKp1uz7Z1GVBdMIIBgQYDVR0fBIIBeDCCAXQwMKAuoCyG

Kmh0dHA6Ly9jcmwucGtpLnZhLmdvdi9QS0kvQ1JML3ZhZGV2aWNlLmNybDB0oHKg

cIZubGRhcDovL2xkYXAucGtpLnZhLmdvdi9jbiUzZFNTUEIyQUUsY24lM2RDRFAs

Y24lM2RQS0ksY24lM2RTZXJ2aWNlcyxkYyUzZHZhLGRjJTNkZ292P2NlcnRpZmlj

YXRlUmV2b2NhdGlvbkxpc3QwNKAyoDCGLmh0dHA6Ly9jZHAxLnNzcC1zdHJvbmct

aWQubmV0L0NEUC92YWRldmljZS5jcmwwgZOggZCggY2GgYpsZGFwOi8vZGlyMS5z

c3Atc3Ryb25nLWlkLm5ldC9jbiUzZFZldGVyYW5zJTIwQWZmYWlycyUyMERldmlj

ZSUyMENBJTIwQjIsb3UlM2RQS0ksb3UlM2RTZXJ2aWNlcyxkYyUzZHZhLGRjJTNk

Z292P2NlcnRpZmljYXRlUmV2b2NhdGlvbkxpc3QwHQYDVR0OBBYEFM46SuxQAM8n

ayR/hlJgt/b0caNbMA0GCSqGSIb3DQEBCwUAA4IBAQAOz+ie4OlLRty9CTpt7qtm

CCg8O5Msj5PDTm2QM2nX+VRiwV3cMldgsoK0gr9SKvjx+8sArMQLkzC21XavuwVh

Qn42mKm1XJvk3kbJx7Na0tg+8etepzHv1tfORJ1taCt1NTPIU8IBAxZWsYh812l8

k8u7/KtnsK6zqiBRaNloovMl20CDxeWnFRzSLrTV91Z5V+gr1KlEIS3WkiHO7d+n

wqYnZB4fA0mjJ83Mrt8IxiTZTP8Qn1LoyPR/vfoqOUamxRBWlIo4wTvEvN6+9hJ3

GQhfO9E/l7v5lvgh7Wor58X+iRIBvj04PyU9PB8/ZYTst/t5IoucbMCir77ZEk0B

-----END CERTIFICATE-----

### das.<span class="mark">REDACTED</span>.pem

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-----BEGIN CERTIFICATE-----

MIIHezCCBmOgAwIBAgIDBfJ1MA0GCSqGSIb3DQEBCwUAMHIxEzARBgoJkiaJk/Is

ZAEZFgNnb3YxEjAQBgoJkiaJk/IsZAEZFgJ2YTERMA8GA1UECxMIU2VydmljZXMx

DDAKBgNVBAsTA1BLSTEmMCQGA1UEAxMdVmV0ZXJhbnMgQWZmYWlycyBEZXZpY2Ug

Q0EgQjIwHhcNMTcwMTA2MTk1MTE1WhcNMTgwODA3MTUyMjQ2WjBQMRMwEQYKCZIm

iZPyLGQBGRYDZ292MRIwEAYKCZImiZPyLGQBGRYCdmExEDAOBgNVBAsTB2Rldmlj

ZXMxEzARBgNVBAMTCmRhcy52YS5nb3YwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw

ggEKAoIBAQDZSc8gGHDms81rMeAffccObXAmUPpiG49PECDwNnIkPu6oSd3xEUuZ

9AWR7S+tR8zyzca2G8GaJj0OQxgT2C4vz2mniuNTnEkA1sTf2eNbMN7kcEo6SJJX

P+GUEmpszqxVIoi0nzvOiEfkfVfhu5rxI5fWUdNxYj7DErCMTiQtn1GAvEittYK5

pZJSvGuth+VHGYD3u6Oz1L1Gx+2z0DZYUJriB9nX0JzTAAPFr9maxac5qMwAwbNz

3bcpu1mYOaYkMHFEiUB6qLs8VoQli/rUlg6dDAK0amtu+dvNYA4q2g+HMoOXRrXj

yzuT+lOAMc8rzjBCJuJiAX4hJanLV7KnAgMBAAGjggQ6MIIENjCB6AYDVR0RBIHg

MIHdggpkYXMudmEuZ292ghx2YWF1c2Rhc2FwcHJwZDAwMS5hYWMudmEuZ292ghx2

YWF1c2Rhc2FwcHByZDAwMi5hYWMudmEuZ292ghx2YWF1c2Rhc2FwcHByZDAwMy5h

YWMudmEuZ292ghx2YWF1c2Rhc2FwcHByZDAwNC5hYWMudmEuZ292ghx2YWF1c2Rh

c2FwcHByZDAwNS5hYWMudmEuZ292ghx2YWF1c2Rhc2FwcHByZDAwNi5hYWMudmEu

Z292ght2YWF1c2Rhc2FwcHByZDQzLmFhYy52YS5nb3YwFwYDVR0gBBAwDjAMBgpg

hkgBZQMCAQMIMIIBMAYIKwYBBQUHAQEEggEiMIIBHjA7BggrBgEFBQcwAoYvaHR0

cDovL2FpYTEuc3NwLXN0cm9uZy1pZC5uZXQvQ0EvVkFkZXZpY2VDQS5wN2MwgYAG

CCsGAQUFBzAChnRsZGFwOi8vZGlyMS5zc3Atc3Ryb25nLWlkLm5ldC9jbj1WZXRl

cmFucyUyMEFmZmFpcnMlMjBEZXZpY2UlMjBDQSUyMEIyLG91PVBLSSxvdT1TZXJ2

aWNlcyxkYz12YSxkYz1nb3Y/Y0FDZXJ0aWZpY2F0ZTAjBggrBgEFBQcwAYYXaHR0

cDovL29jc3AucGtpLnZhLmdvdi8wNwYIKwYBBQUHMAGGK2h0dHA6Ly9vY3NwMS5z

c3Atc3Ryb25nLWlkLm5ldC9WQS1TU1AtQ0EtQjIwDgYDVR0PAQH/BAQDAgWgMCcG

A1UdJQQgMB4GCCsGAQUFBwMBBggrBgEFBQcDAgYIYIZIAWUDBgcwHwYDVR0jBBgw

FoAUgZQ1niqod2AjZuwqnW7PtnUZUF0wggGBBgNVHR8EggF4MIIBdDAwoC6gLIYq

aHR0cDovL2NybC5wa2kudmEuZ292L1BLSS9DUkwvdmFkZXZpY2UuY3JsMHSgcqBw

hm5sZGFwOi8vbGRhcC5wa2kudmEuZ292L2NuJTNkU1NQQjJBRSxjbiUzZENEUCxj

biUzZFBLSSxjbiUzZFNlcnZpY2VzLGRjJTNkdmEsZGMlM2Rnb3Y/Y2VydGlmaWNh

dGVSZXZvY2F0aW9uTGlzdDA0oDKgMIYuaHR0cDovL2NkcDEuc3NwLXN0cm9uZy1p

ZC5uZXQvQ0RQL3ZhZGV2aWNlLmNybDCBk6CBkKCBjYaBimxkYXA6Ly9kaXIxLnNz

cC1zdHJvbmctaWQubmV0L2NuJTNkVmV0ZXJhbnMlMjBBZmZhaXJzJTIwRGV2aWNl

JTIwQ0ElMjBCMixvdSUzZFBLSSxvdSUzZFNlcnZpY2VzLGRjJTNkdmEsZGMlM2Rn

b3Y/Y2VydGlmaWNhdGVSZXZvY2F0aW9uTGlzdDAdBgNVHQ4EFgQUvaLuziprIjqH

vyKPGlFwBP6elTwwDQYJKoZIhvcNAQELBQADggEBACOKYWvcihUGT0M9q/dw2FeN

jHzc9ghlsLxDOH1z5zpUfo7vCN5XvckRtPJBxAgPfBma+Cvm4MvJ09Cz6XTKkfZL

joqRm1dg9n61+bIEiX2wgwDT8yBYQRC+eoM6UdoSN7hk60xxZnvahJAdGEStwl2+

FdtejxfiRJr0kA9he/Yrl1EJ2NmWK1YWG6UPzGa1rT4H/OQGTItdxr1VIAff75Ub

089I4vVubkSLAgiwd5xpQnS27uj3OgQUjvJvSwU59/cdMoAw+XLNBlgXVcB3eplK

3SbuZJIJRbhg8HZn4D6aX/g+g0ZPjATMZWBPNLpgPYX/dW5rYjhbs5d5rXUikgc=

-----END CERTIFICATE-----

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSO*7*617 Inbound ePrescribing DIBR

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

## Back-out VistA Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will be done only with the concurrence and participation of development team and appropriate VA site/region personnel. The decision to back-out or rollback software will be a joint decision between development team, VA site/region personnel and other appropriate VA personnel.

Prior to installing an updated KIDS package, the site/region should have saved a backup of the routines in a mail message using the Backup a Transport Global \[XPD BACKUP\] menu option (this is done at time of install). The message containing the backed-up routines can be loaded with the "Xtract PackMan" function at the Message Action prompt. The Packman function "INSTALL/CHECK MESSAGE" is then used to install the backed-up routines onto the VistA System.

The back-out plan is to restore the routines from the backup created.

No data was modified by this patch installation and, therefore, no rollback strategy is required.

Validation of Back-out Procedure:

The Back-out Procedure can be verified by printing the first 2 lines of the PSO Routines contained in this patch using the option First Line Routine Print \[XU FIRST LINE PRINT\]. Once the routines contained in the PSO\*7.0\*617 patch have been backed out, the second line of the Routines will no longer contain the designation of patch PSO\*7.0\*617 in the patch list section.

The Back-out Procedure can be verified by printing the first 2 lines of the PSO Routines contained in this patch using the option First Line Routine Print \[XU FIRST LINE PRINT\]. Once the routines contained in the PSD\*3.0\*89 patch have been backed out, the second line of the Routines will no longer contain the designation of patch PSD\*3.0\*89 in the patch list section.

### From: PSO*7*590 Inbound ePrescribing DIBR

## Deployment Steps:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  (SA) unzip erx_iep_3.1.0.007.zip in /u01/tmp.
2.  (WL) Shutdown Pentaho master & slaves.
3.  (SA) Execute IEP Deployer on VM1 (erx_iep_3.1.0.007_deploy_20200207_113007.sh) with options 1, 2, and 5.
    1.  Run Option 1. Install System Files
    2.  Run Option 2. Install CPanel
5.  Run Option 5. Deposit WebLogic EAR’s
4.  (SA0 Execute IEP Configurator on VM2 (erx_iep_3.1.0.007_configur_20200207_113007.sh) options 1 and 2
    1.  Run Option 1. Install System Files
    2.  Run Option 2. Install CPanel
5.  (WL) Delete 3.1.0.006 ears from WebLogic
6.  (WL) Deploy INB_ERX-3.1.0.007.ear and INB_ERX_UI-3.1.0.007.ear
7.  (WL) Start Pentaho Slaves/Jobs
8.  (IEP Sustainment) Smoke Test WebLogic.
9.  (IEP Sustainment) Smoke Test Pentaho component.
10. (IEP Sustainment) Validate deployment successful. If any issues occur with the eRx GUI or WebLogic Service, perform a rolling restart of the WebLogic Managed Servers:
    1.  (WL) Restart first WebLogic managed server only. Wait until first managed server returns to Running state before proceeding.
    2.  (WL) Repeat step a above for the next managed server. Continue one at a time until all managed servers are restarted and in the Running state. Ensure at least one managed server is in the Running state.

## Backout Process:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Prerequisites: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous INB_ERX-3.1.0.006.ear and INB_ERX_UI-3.1.0.006.ear still exist in installation directory.

### Backout Steps:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  (WL) Shutdown Pentaho master & slaves (jobs) .
2.  (SA) Execute IEP Deployer on VM1 (erx_iep_3.1.0.006_deploy_20200114_141632

.sh) with options 1,2 and 5.

1.  Run Option 1. (Install System Files)
2.  Run Option 2. (Install CPanel)
5.  Run Option 5. (Deposit WebLogic EAR’s)
3.  (SA) Execute IEP Configurator on VM2 (erx_iep_3.1.0.006_configur_20200114_141632.sh) options 1,2
    1.  Run Option 1. Install System Files
    2.  Run Option 2. Install CPanel.
4.  (WL) Delete INB_ERX-3.1.0.007.ear and INB_ERX_UI-3.1.0.007.ear *(refer to section 4.1.2.1 for detailed steps for removing new ear files)*.
5.  (WL) Deploy INB_ERX-3.1.0.006.ear and INB_ERX_UI-3.1.0.006.ear *(refer section 4.1.2.2 for detailed steps for deploying old ear files)*.
6.  (WL) Start Pentaho Slaves/Jobs .
7.  (IEP Sustainment) Smoke Test WL.
8.  (IEP Sustainment) Smoke Test Pentaho.
9.  (IEP Sustainment) Validate backout successful. If any issues occur with the eRx GUI or WebLogic services, perform a rolling restart of the WebLogic managed servers.
    1.  (WL) Restart first WebLogic managed server only. Wait until first managed server returns to Running state before proceeding.
    2.  (WL) Repeat step a above for the next managed server. Continue one at a time until all managed servers are restarted and in Running state. Ensure at least one managed server is in the Running state at all times during this process.

#### Remove New Release:

1.  Open and log into the WebLogic console. Use WebLogic username and password.
2.  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3.  Within the *Change Center* panel in the left column of the WebLogic console, select Lock & Edit.
4.  WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
5.  Select the previously deployed Inbound eRx deployment, select Stop, and then select Force Stop Now from the drop-down list.
6.  WebLogic will now display the panel *Force Stop Application Assistant* in the right column of the console for confirmation to start servicing requests.
7.  Select Yes in the *Force Stop Application Assistant* panel in the right column of the WebLogic console.
8.  WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
9.  Verify that the State of the Inbound eRx deployment is Prepared.
10. Select the previously deployed Inbound eRx deployment, and then select Delete.
11. WebLogic will now display the panel *Delete Application Assistant* in the right column of the console for confirmation to start servicing requests.
12. Select Yes in the *Delete Application Assistant* panel in the right column of the WebLogic console.
13. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
14. Verify that the Inbound eRx deployment is deleted and no longer present.

#### Deploy Rolled-Back Release:

The following steps detail the deployment of the rolled-back Inbound eRx application.

15. Use the WebLogic console that was started at the beginning of the roll-back process.
16. Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
17. Verify that the application is in Lock & Edit mode. Lock & Edit mode is indicated by the greyed-out Lock & Edit selection button.
18. Select the Install button in the *Deployments* panel in the right column of the WebLogic console.
19. WebLogic will now display the panel *Install Application Assistant* in the right column of the console, where the location of the Inbound eRx deployment will be found.
    1.  If the rolled-back Inbound eRx deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the *Location* panel, which is within the *Install Application Assistant* panel in the right column of the console. Choose the ear file associated with the rolled-back release.
    2.  If the rolled-back Inbound eRx deployment has not been transferred to the Deployment Machine:
        1.  Select on the upload your file(s) link in the *Install Application Assistant* panel in the right section of the console.
        2.  Select the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
        3.  Select Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the *Locate deployment to install and prepare for deployment* panel within the *Install Application Assistant*.
20. Once the rolled-back Inbound eRx deployment is located and selected, select Next.
21. WebLogic will now display the panel *Choose targeting style* within the *Install Application Assistant* in the right column of the console. Leave the default value selected, install this deployment as an application, and select Next.
22. Within the *Install Application Assistant* in the right column of the console, WebLogic will now display the panel *Select deployment targets*, where the Deployment Server will be selected as the target in the next step.
23. For the Target, select the Deployment Server.
24. Select Next.
25. Within the *Install Application Assistant*, WebLogic will now display the panel *Optional Settings* in the right column of the console, where the name of the deployment and the copy behavior are chosen.
26. Enter the Name for the deployment. Use: INB_ERX-3.1.0.006
27. Verify that the following default option for Security is selected:
28. DD Only: Use only roles and policies that are defined in the deployment descriptors.
29. Verify that the following default option for Source accessibility is selected:
30. Use the defaults defined by the deployment's targets.
31. Select Next.
32. Within the *Install Application Assistant*, in the right column of the console WebLogic, the panel *Review your choices and click Finish* will now be displayed, which summarizes the steps completed above.
33. Verify that the values match those entered in Steps 6 through 17 and select Finish.
34. WebLogic will now display the panel *Settings for Inbound eRx*, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
35. Leave all the values as defaulted by WebLogic and select Save.
36. Within the *Change Center* panel in the left column of the WebLogic console, select Activate Changes.
37. Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
38. WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
39. Select the previously deployed INB_ERX-3.1.0.006 deployment, select Start, and then select Servicing all requests from the drop-down list.
40. WebLogic will now display the panel *Start Application Assistant* in the right column of the console for confirmation to start servicing requests.
41. Select Yes in the *Start Application Assistant* panel in the right column of the WebLogic console.
42. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
43. Verify that the State of the INB_ERX-3.1.0.006 deployment is Active.

### From: PSO*7*610 Inbound ePrescribing DIBR

### Prerequisites: 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous INB_ERX-3.1.0.007.ear and INB_ERX_UI-3.1.0.007.ear still exist in installation directory.

### Backout Steps:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  (WL) Shutdown Pentaho master & slaves (jobs) .
2.  (SA) Execute IEP Deployer on VM1 (erx_iep_3.1.0.007_deploy_20200207_113007.sh) with options 1,2 and 5.
    1.  Run Option 1. (Install System Files)
    2.  Run Option 2. (Install CPanel)
5.  Run Option 5. (Deposit WebLogic EAR’s)
3.  (SA) Execute IEP Configurator on VM2 (erx_iep_3.1.0.007_configur_20200416_124213.sh) options 1,2
    1.  Run Option 1. Install System Files
    2.  Run Option 2. Install CPanel.
4.  (WL) Delete INB_ERX-3.1.0.008.ear and INB_ERX_UI-3.1.0.008.ear *(refer to section 4.1.2.1 for detailed steps for removing new ear files)*.
5.  (WL) Deploy INB_ERX-3.1.0.007.ear and INB_ERX_UI-3.1.0.007.ear *(refer section 4.1.2.2 for detailed steps for deploying old ear files)*.
6.  (WL) Start Pentaho Slaves/Jobs .
7.  (IEP Sustainment) Smoke Test WL.
8.  (IEP Sustainment) Smoke Test Pentaho.
9.  (IEP Sustainment) Validate backout successful. If any issues occur with the eRx GUI or WebLogic services, perform a rolling restart of the WebLogic managed servers.
    1.  (WL) Restart first WebLogic managed server only. Wait until first managed server returns to Running state before proceeding.
    2.  (WL) Repeat step a above for the next managed server. Continue one at a time until all managed servers are restarted and in Running state. Ensure at least one managed server is in the Running state at all times during this process.

#### Remove New Release:

1.  Open and log into the WebLogic console. Use WebLogic username and password.
2.  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3.  Within the *Change Center* panel in the left column of the WebLogic console, select Lock & Edit.
4.  WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
5.  Select the previously deployed Inbound eRx deployment, select Stop, and then select Force Stop Now from the drop-down list.
6.  WebLogic will now display the panel *Force Stop Application Assistant* in the right column of the console for confirmation to start servicing requests.
7.  Select Yes in the *Force Stop Application Assistant* panel in the right column of the WebLogic console.
8.  WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
9.  Verify that the State of the Inbound eRx deployment is Prepared.
10. Select the previously deployed Inbound eRx deployment, and then select Delete.
11. WebLogic will now display the panel *Delete Application Assistant* in the right column of the console for confirmation to start servicing requests.
12. Select Yes in the *Delete Application Assistant* panel in the right column of the WebLogic console.
13. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
14. Verify that the Inbound eRx deployment is deleted and no longer present.

#### Deploy Rolled-Back Release:

The following steps detail the deployment of the rolled-back Inbound eRx application.

15. Use the WebLogic console that was started at the beginning of the roll-back process.
16. Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
17. Verify that the application is in Lock & Edit mode. Lock & Edit mode is indicated by the greyed-out Lock & Edit selection button.
18. Select the Install button in the *Deployments* panel in the right column of the WebLogic console.
19. WebLogic will now display the panel *Install Application Assistant* in the right column of the console, where the location of the Inbound eRx deployment will be found.
    1.  If the rolled-back Inbound eRx deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the *Location* panel, which is within the *Install Application Assistant* panel in the right column of the console. Choose the ear file associated with the rolled-back release.
    2.  If the rolled-back Inbound eRx deployment has not been transferred to the Deployment Machine:
        1.  Select on the upload your file(s) link in the *Install Application Assistant* panel in the right section of the console.
        2.  Select the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
        3.  Select Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the *Locate deployment to install and prepare for deployment* panel within the *Install Application Assistant*.
20. Once the rolled-back Inbound eRx deployment is located and selected, select Next.
21. WebLogic will now display the panel *Choose targeting style* within the *Install Application Assistant* in the right column of the console. Leave the default value selected, install this deployment as an application, and select Next.
22. Within the *Install Application Assistant* in the right column of the console, WebLogic will now display the panel *Select deployment targets*, where the Deployment Server will be selected as the target in the next step.
23. For the Target, select the Deployment Server.
24. Select Next.
25. Within the *Install Application Assistant*, WebLogic will now display the panel *Optional Settings* in the right column of the console, where the name of the deployment and the copy behavior are chosen.
26. Enter the Name for the deployment. Use: INB_ERX-3.1.0.007
27. Verify that the following default option for Security is selected:
28. DD Only: Use only roles and policies that are defined in the deployment descriptors.
29. Verify that the following default option for Source accessibility is selected:
30. Use the defaults defined by the deployment's targets.
31. Select Next.
32. Within the *Install Application Assistant*, in the right column of the console WebLogic, the panel *Review your choices and click Finish* will now be displayed, which summarizes the steps completed above.
33. Verify that the values match those entered in Steps 6 through 17 and select Finish.
34. WebLogic will now display the panel *Settings for Inbound eRx*, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
35. Leave all the values as defaulted by WebLogic and select Save.
36. Within the *Change Center* panel in the left column of the WebLogic console, select Activate Changes.
37. Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
38. WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
39. Select the previously deployed INB_ERX-3.1.0.007 deployment, select Start, and then select Servicing all requests from the drop-down list.
40. WebLogic will now display the panel *Start Application Assistant* in the right column of the console for confirmation to start servicing requests.
41. Select Yes in the *Start Application Assistant* panel in the right column of the WebLogic console.
42. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
43. Verify that the State of the INB_ERX-3.1.0.007 deployment is Active.
