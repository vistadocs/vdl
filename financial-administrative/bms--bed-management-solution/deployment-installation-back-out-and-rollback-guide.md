---
consolidated_title: "bed management solution dibr"
app_code: BMS
doc_type: DIBR
master_source: "Bed Management Solution Version 2.4 DIBR"
master_pub_date: January 2020
consolidated_from: 6 versions
prior_versions:
  - "Bed Management Solution Version 2.5 DIBR"
  - "Bed Management Solution Version 2.6 DIBR"
  - "Bed Management Solution Version 2.8 DIBR"
  - "Bed Management Solution Version 2.9 DIBR"
  - "Bed Management Solution Version 3.5 DIBR"
---

# Bed Management Solution (BMS) v2.4


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Bed Management Solution (BMS) v2.4](#bed-management-solution-bms-v24)
- [Artifact Rationale](#artifact-rationale)
- [Introduction](#introduction)
- [Purpose](#purpose)
- [Dependencies](#dependencies)
  - [![](bed-management-solution-version-2-4-dibr/013.png)Constraints](#bed-management-solution-version-2-4-dibr013pngconstraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [![](bed-management-solution-version-2-4-dibr/014.png)Timeline](#bed-management-solution-version-2-4-dibr014pngtimeline)
  - [![](bed-management-solution-version-2-4-dibr/016.png)Site Readiness Assessment](#bed-management-solution-version-2-4-dibr016pngsite-readiness-assessment)
  - [![](bed-management-solution-version-2-4-dibr/017.png)Application Architecture](#bed-management-solution-version-2-4-dibr017pngapplication-architecture)
  - [Deployment Topology (Targeted Architecture)](#deployment-topology-targeted-architecture)
  - [Site Information (Locations, Deployment Recipients)](#site-information-locations-deployment-recipients)
  - [Site Preparation](#site-preparation)
  - [Resources](#resources)
    - [Facility Specifics](#facility-specifics)
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
    - [Deployment/Installation/Back-Out Checklist](#deploymentinstallationback-out-checklist)
- [Installation](#installation)
  - [![](bed-management-solution-version-2-4-dibr/019.png)Pre-installation and System Requirements](#bed-management-solution-version-2-4-dibr019pngpre-installation-and-system-requirements)
  - [Pre-installation Activities:](#pre-installation-activities)
  - [![](bed-management-solution-version-2-4-dibr/020.png)Database Server](#bed-management-solution-version-2-4-dibr020pngdatabase-server)
  - [![](bed-management-solution-version-2-4-dibr/021.png)Application Servers](#bed-management-solution-version-2-4-dibr021pngapplication-servers)
  - [![](bed-management-solution-version-2-4-dibr/022.png)Web Server](#bed-management-solution-version-2-4-dibr022pngweb-server)
  - [![](bed-management-solution-version-2-4-dibr/023.png)Report Server](#bed-management-solution-version-2-4-dibr023pngreport-server)
  - [![](bed-management-solution-version-2-4-dibr/024.png)Post-installation and Smoke Testing](#bed-management-solution-version-2-4-dibr024pngpost-installation-and-smoke-testing)
  - [Post-installation Activities](#post-installation-activities)
  - [Smoke Testing](#smoke-testing)
- [Rollback/ Back-Out Plan](#rollback-back-out-plan)
> Deployment, Installation, Rollback, and Back-Out Guide
![](bed-management-solution-version-2-4-dibr/001.png)
> January 2020 v1.3
> Department of Veterans Affairs
> Office of Information and Technology (OI&T)
> Revision History
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/06/2019</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td>Updated wth BMS v2.4</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>12/16/2019</td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td>Updated Schedule and Deployment Instructions</td>
<td>Technatomy</td>
</tr>
<tr class="odd">
<td>1/13/2020</td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td>Updated Schedule</td>
<td>Technatomy</td>
</tr>
<tr class="even">
<td>1/15/2020</td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td>Updated Installation Instructions</td>
<td>Technatomy</td>
</tr>
</tbody>
</table>

# Artifact Rationale

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

1.  [Introduction 2](#introduction)
2.  [Purpose 2](#purpose)
3.  [Dependencies 2](#dependencies)

![](bed-management-solution-version-2-4-dibr/002.png)[Constraints 3](#constraints)

4.  [Roles and Responsibilities 3](#roles-and-responsibilities)
5.  [Deployment 4](#deployment)

![](bed-management-solution-version-2-4-dibr/003.png)[Timeline 4](#timeline)

![](bed-management-solution-version-2-4-dibr/004.png)[Site Readiness Assessment 5](#site-readiness-assessment)

![](bed-management-solution-version-2-4-dibr/005.png)[Application Architecture 5](#application-architecture)

1.  [Deployment Topology (Targeted Architecture) 6](#deployment-topology-targeted-architecture)
2.  [Site Information (Locations, Deployment Recipients) 6](#site-information-locations-deployment-recipients)
3.  [Site Preparation 6](#site-preparation)
4.  [Resources 6](#resources)
    1.  [Facility Specifics 6](#facility-specifics)
    2.  [Hardware 6](#hardware)
    3.  [Software 6](#software)
    4.  [Communications 6](#communications)
    5.  [Deployment/Installation/Back-Out Checklist 7](#deploymentinstallationback-out-checklist)
6.  [Installation 7](#installation)

![](bed-management-solution-version-2-4-dibr/006.png)[Pre-installation and System Requirements 7](#pre-installation-and-system-requirements)

[6.1.1](#pre-installation-activities) [Pre-installation Activities: 7](#pre-installation-activities)

![](bed-management-solution-version-2-4-dibr/007.png)[Database Server 7](#database-server)

![](bed-management-solution-version-2-4-dibr/008.png)[Application Servers 8](#application-servers)

![](bed-management-solution-version-2-4-dibr/009.png)[Web Server 9](#web-server)

![](bed-management-solution-version-2-4-dibr/010.png)[Report Server 9](#report-server)

![](bed-management-solution-version-2-4-dibr/011.png)[Post-installation and Smoke Testing 10](#post-installation-and-smoke-testing)

1.  [Post-installation Activities 10](#post-installation-activities)
2.  [Smoke Testing 10](#smoke-testing)
7.  [Rollback/ Back-Out Plan 10](#rollback-back-out-plan)

> Table of Figures

> [Figure 1: BMS Overview 2](#_bookmark3)

> [Figure 2: BMS Architecture Diagram 5](#_bookmark12)

> List of Tables

> [Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities 4](#_bookmark6)

> [Table 2: Deployment Timeline 4](#_bookmark9)

> [Table 3: Deployment/Installation/Back-Out Checklist 7](#_bookmark22)

> BMS v2.4

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes how to deploy and install the various components of the software for the Bed Management Solution (BMS) v2.4 project, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial Off-the-Shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

> BMS is a real-time, user-friendly web-based Veterans Health Information Systems and Technology Architecture (VistA) interface for tracking patient movement, bed status and bed availability within the VA system. It provides performance information that can be used to measure and improve patient flow as it occurs within and between VAMCs. BMS enhances safety, quality of care, patient/staff satisfaction and improves patient flow for process and outcome improvements. BMS, the automated Bed Management Solution, allows administrative and clinical staff to record, manage and report on the planning, patient-movement, patient occupancy, and other activities related to management of beds. All patient admission, discharge, and transfer movements are pulled directly from VistA to BMS resulting in minimal manual data entry.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the BMS application will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

# Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS communicates with VistA to capture bed, patient, admission, transfer, and discharge information. BMS also interfaces with National Utilization Management Integration (NUMI) to retrieve information regarding NUMI reviews.

> ![](bed-management-solution-version-2-4-dibr/012.png)<span id="_bookmark3" class="anchor"></span>Figure 1: BMS Overview

## ![](bed-management-solution-version-2-4-dibr/013.png)Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The software needs to address system-related issues associated with the currently deployed BMS v.2.3.1 product, while continuing to meet functional business needs and requirements of the business owner.

> The objective of the second increment of the intended solution is to enhance the current BMS functionality identified in the Init8_BMS_RSD Inc2 as part of the nationally supported Class I solution, while complying with all previously established VA national release criteria. This version will be integrated with VistA and NUMI.

> Specific functionalities to be deployed in the second increment of BMS v2.4 will enhance functionalities of the following components of the system:

> Whiteboard integration and management Icon Library management

> Event Notifications management Patient waitlist management

> BMS v2.4 will be a single code base system supporting all VAMCs and Veterans Integrated Service Networks (VISNs).

> BMS v2.4 will be hosted in a browser-controlled environment.

> BMS v2.4 design will support the server configurations deployed at the Austin Information Technology Center (AITC) that hosts BMS v.2.3.1.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the roles and responsibilities for managing the deployment of the BMS 2.4 application. The BMS 2.4 Development Team will produce the deployment artifacts (RFC’s, DB Scripts, executables, etc.) and work directly with the AITC personnel to plan the actual deployment.

> <span id="_bookmark6" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 28%" />
<col style="width: 14%" />
<col style="width: 35%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ID</strong></th>
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
<th><blockquote>
<p><strong>Project Phase (See Schedule)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>FO, EO, NDCP or Product Development (depending upon project ownership)</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors).</td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td>FO, EO, NDCP or Product Development (depending upon project ownership)</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
<td><blockquote>
<p>Design/Build</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td>FO, EO, or NDCP</td>
<td>Deployment</td>
<td>Test for operational readiness.</td>
<td><blockquote>
<p>Design/Build</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td>FO, EO, or NDCP</td>
<td>Deployment</td>
<td>Execute deployment.</td>
<td><blockquote>
<p>Design/Build</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td>FO, EO, or NDCP</td>
<td>Installation</td>
<td>Plan and schedule installation.</td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td>Regional PM/ Field Implementation Services (FIS)/ Office of Policy and Planning (OPP) PM</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place.</td>
<td><blockquote>
<p>Design/Build</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td>Regional PM/FIS/OPP PM/ Nat’l Education &amp; Training</td>
<td>Installations</td>
<td>Coordinate training.</td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td>FO, EO, NDCP or Product Development (depending upon project ownership)</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).</td>
<td><blockquote>
<p>Deployment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td>FO, EO, NDCP or Product Development (depending upon project ownership)</td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support.</td>
<td><blockquote>
<p>Maintenance</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment and installation is scheduled to run as depicted in the BMS v2.4 development master schedule.

## ![](bed-management-solution-version-2-4-dibr/014.png)Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment and installations timelines are depicted in the Deployment Timeline Schedule below.

> ![](bed-management-solution-version-2-4-dibr/015.png)<span id="_bookmark9" class="anchor"></span>Table 2: Deployment Timeline

## ![](bed-management-solution-version-2-4-dibr/016.png)Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The product will be released by the BMS Development Team to the AITC Build Manager via a Change Order. The AITC Build Manager will follow the installation steps in [Section 0](#installation) to complete the product’s activation at AITC. The Implementation Manager has assured site readiness by assessing the readiness of the receiving site to deploy the product. AITC, under contract, will provide the product dependencies, power, equipment, space, manpower, etc., to ensure the successful activation of this product.

## ![](bed-management-solution-version-2-4-dibr/017.png)Application Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following diagram represents the high-level architecture for the BMS application. BMS is a national application deployed at the AITC data center. The application is accessed at VA medical centers using approved web browser software. BMS reads data from VistA systems associated with each site’s VistA instance.

![](bed-management-solution-version-2-4-dibr/018.png)

> <span id="_bookmark12" class="anchor"></span>Figure 2: BMS Architecture Diagram

## Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This product will be released to AITC. The AITC, under contract, will house and secure this product on its Pre-Production and Production servers. The BMS system will be available to VA users on a continuous basis (excluding scheduled maintenance activities).

## Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AITC will host the web and application servers for the BMS system.

## Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS will be supported on VA equipment that currently runs the existing BMS 2.3.1 system; therefore, no site preparatiohn activites are required.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the hardware, software, and communications for the deployment of BMS, where applicable.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No facility-specific features are required for this deployment.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As middleware, BMS 2.4 requires no hardware to install. BMS 2.4 will be supported on existing VA equipment.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS 2.4 will be installed as an upgrade to the existing BMS 2.3.1 system running in production. Other than changes to the application files and database objects, no new COTS software or database/operating system updates are required.

> The software components and database change scripts will be staged at the following location:

> REDACTED

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the communications to be distributed to the business user community:

- Communication between the development team, AITC, and the Sustainment team will occur via email and conference calls scheduled through Microsoft Lync.
- Notification of scheduled maintenance periods that require the service to be offline or that may degrade system performance will be disseminated to the business user community a minimum of 48 hours prior to the scheduled event.
- Notification to VA users for unscheduled system outages or other events that impact the response time will be distributed within 30 minutes of the occurrence.

### Deployment/Installation/Back-Out Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The table below outlines the coordination effort and documents the day/time/individual when each activity (deploy, install, back-out) is completed for BMS 2.4. The table will be populated once the activities are completed.

> <span id="_bookmark22" class="anchor"></span>Table 3: Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task |
|--------------|---------|----------|-----------------------------------|
| Deploy       | TBD     |          |                                   |
| Install      | TBD     |          |                                   |
| Back-Out     | TBD     |          |                                   |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the backup and installation steps for the various BMS 2.4 components.

## ![](bed-management-solution-version-2-4-dibr/019.png)Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the minimum requirements for the product to be installed, as well as the recommended hardware and software system requirements. BMS 2.4 is being deployed as an upgrade to the current BMS 2.3.1 application. As an upgrade, there are no changes to the existing hardware and software system components. The only changes are to the BMS application and database objects - to support the BMS 2.4 functionality.

## Pre-installation Activities:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Backup the existing BMS v2.3.1 databases from vaaussqlbms210
2.  Shut down the BMS v2.3.1 application on the web server and the two app servers
    1.  Web Server 210 - vaauswebbms210
    2.  Application Server 210 – vaausappbms210
    3.  Application Server 211 – vaausappbms211
3.  Stop all vaaussqlbms210 database services/jobs, including the replication services

## ![](bed-management-solution-version-2-4-dibr/020.png)Database Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the installation steps for the various BMS v2.4 database components on vaaussqlbms210.

1.  Apply BMS 2.4 database change scripts
    1.  Download the BMS_2.4_db_210.zip file from

> REDACTED

2.  Unzip BMS_2.4_db_210.zip to vaaussqlbms210 B:\BMS_2.4_db_210
3.  Execute the change scripts within the directory – in order

## ![](bed-management-solution-version-2-4-dibr/021.png)Application Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the installation steps for the BMS components on the two application servers – vaausappbms210 and vaausappbms211.

1.  Copy existing Services directory to backup location on the App Servers
    1.  On vaausappbms210, copy D:\Services to D:\Services_2.3.1_app_210\_\<yyyymmdd\>
    2.  On vaausappbms211, copy D:\Services to D:\Services_2.3.1_app_211\_\<yyyymmdd\>
2.  Download deployment files
    1.  Download the BMS.Prod.Service210 - 2.4.zip file from

> REDACTED

2.  Download the BMS.Prod.VIService211 - 2.4.zip file from

> REDACTED

3.  Replace BMS 2.4 Services\BMS directories on App Servers
    1.  Unzip BMS.Prod.Service210 - 2.4.zip to vaausappbms210 D:\BMS.Prod.Service210
    2.  Replace all files in D:\Services\BMS with files from D:\BMS.Prod.Service210
    3.  Unzip BMS.Prod.VIService211 - 2.4.zip to vaausappbms211 D:\BMS.Prod.VIService211
    4.  Replace all files in D:\Services\BMS with files from D:\\ BMS.Prod.VIService211
4.  Update report operations via Policy Manager
    1.  On vaausappbms210, execute D:\\ Services\Consoles\PolicyManager\PolicyManager.exe, log into the policy manager using the appropriate BMS Service account.
    2.  In the Left Navigation pane, expand Policy Manager \> Definitions, click on Operation Definitions.
    3.  Scroll down the Operation Definitions list, add the following if they do not already exist:
        1.  Click “Add Operation”, Name: “WardWhiteboard, Write" (then properties -\> Check Place & Organization)
        2.  Click “Add Operation”, Name: “rep, UserAccess” Description: “User Access Report”
        3.  Click “Add Operation”, Name: “rep, Discharge Order Difference Report” Description: “Discharge Order Difference Report”
        4.  Click “Add Operation”, Name: “rep, Facility Diversion Report” Description: “Facility Diversion Report”
        5.  Click “Add Operation”, Name: “rep, PPBP By Date Range Report” Description: “PPBP By Date Range Report”
        6.  Click “Add Operation”, Name: “rep, VISN Diversion Report” Description: “VISN Diversion Report”
        7.  Click “Add Operation”, Name: “rep, VISN Emergency Management Report” Description: “VISN Emergency Management Report”
    4.  In the Operation Definitions list, double click “WardWhiteboard, Write":
        1.  Check: Place, Organization, click “OK”
    5.  In the Left Navigation pane, expand Policy Manager \> Definitions, click on Task Definitions.
    6.  In the Right List pane, double click on “Reporting Services, Fetch”
    7.  Under the Definition tab, click the “Add …” button, and scroll down the Operation Definitions list, check the following if they exist:
        1.  rep, UserAccess Report
        2.  rep, Discharge Order Difference Report
        3.  rep, Facility Diversion Report
        4.  rep, PPBP By Date Range Report
        5.  rep, VISN Diversion Report
        6.  rep, VISN Emergency Management Report
    8.  Click Okay on the “Add Definitions” dialogue, click “OK” on the “Task Definition Properties” dialogue and close the PolicyManager.

## ![](bed-management-solution-version-2-4-dibr/022.png)Web Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the installation steps for the BMS components on the web server – vaauswebbms210.

1.  Copy existing BMSWeb directory to backup directory on the Web Server
    1.  On vaauswebbms210, copy D:\BMSWeb to D:\BMSWeb_2.3.1_web_210\_\<yyyymmdd\>
2.  Download deployment file
    1.  Download the BMS.Prod.Web210 - 2.4.zip file from

> REDACTED

3.  Replace BMS 2.4 BMSWeb directory on the Web Server
    1.  Unzip BMS.Prod.Web210 - 2.4.zip to vaauswebbms210 D:\BMS.Prod.Web210
    2.  Replace all files in D:\BMSWeb with files from D:\BMS.Prod.Web210

## ![](bed-management-solution-version-2-4-dibr/023.png)Report Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the installation steps for the BMS components on the report server – vaaussqlbms211.

1.  Backup existing BMS 2.3.1 report files
    1.  Create a backup directory named D:\BMS_2.3.1_backup\_\<yyyymmdd\>
    2.  Copy all directories/files from <http://vaaussqlbms211/Reports> to the backup directory
2.  Download deployment file
    1.  Download the BMS_2.4_reports_211.zip file from

> REDACTED

3.  Create BMS 2.4 Report Definitions directory on the Report Server
    1.  Unzip BMS_2.4_reports_211.zip to vaaussqlbms211 D:\BMS_2.4_reports_211
4.  Update Reports on Report Server
    1.  On vaaussqlbms211, open IE, navigate to: <http://vaaussqlbms211/Reports>
    2.  Add or update each report that is located in D:\BMS_2.4_reports_211\\

## ![](bed-management-solution-version-2-4-dibr/024.png)Post-installation and Smoke Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the post-installation activities and the minimum BMS 2.4 functionality to smoke test.

## Post-installation Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Start up the BMS v2.4 application on the web server and the two app servers
    1.  Application Server 210 – vaausappbms210
    2.  Application Server 211 – vaausappbms211
    3.  Web Server 210 - vaauswebbms210
2.  Start all vaaussqlbms210 database services/jobs, including the replication services

## Smoke Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Perform Smoke Testing
    1.  White Boards
    2.  BMS 2.4 UI and Reports
    3.  Background Processes

# Rollback/ Back-Out Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The BMSv2.4 rollback/back-out plan is relatively straightforward since a complete backup of the database was performed prior to the install; and backup directories were created on each of the upgraded servers.

1.  Following the procedures in sections 6.1 and 6.2, the first activity in a rollback to BMS v2.3.1 is to shut down all of the services/jobs across the servers; and then restore the database on vaaussqlbms210.
2.  Next, back-out the Services directories on the two app servers to (vaausappbms210 and vaausappbms211) and the BMSWeb directory on the web server (vaaussqlbms211) from the backup directories – by renaming them. See sections 6.3 and 6.4 for the directory names.
3.  The next step is to restore the BMS v2.3.1 report files on the report server (vaaussqlbms211) by following the steps in section 6.5 to re-apply the original BMS v.2.3.1 report definitions.
4.  The last steps are to following the instructions in section 6.6 to restart the BMS v.2.3.1 application and smoke test the functionality.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Bed Management Solution Version 2.9 DIBR

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The software needs to address system-related issues associated with the currently deployed BMS v2.9.31 product, while continuing to meet functional business needs and requirements of the business owner.

> The objective of this software release is to enhance the current BMS functionality as part of the nationally supported Class I solution, while complying with all previously established VA national release criteria.

> Specific functionalities to be deployed in this release of BMS v2.9 will enhance functionalities of the following components of the system:

- EVS Inflow Replacement
- Replace EVS Workflow Services
- Remove EVS Configuration Table
- Replace EVS Cache
- Evacuated Patients not moving from Whiteboard to PPBP properly
- Adding a Discharge Clinic that does not exist causes an Exception
- Removal of BedBoardModule Page
- Display Correct User Login Account
- Deleting a Discharge Clinic causes an Error
- Display Specialty is not being Hidden on Whiteboard after unselecting Desktop checkbox (Add/Edit Ward)
- Patients modified in Whiteboard not showing up in Whiteboard Patient Icon Usage (Audit Log)
- Report results swapping data for Site Configurable and Standard Icons

BMS v2.9 will be a single code base system supporting all VAMCs and Veterans Integrated Service Networks (VISNs).

BMS v2.9 will be hosted in a browser-controlled environment.

BMS v2.9 design will support the server configurations deployed at the Austin Information Technology Center (AITC) that hosts BMS v.2.8.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The product will be released by the BMS Development Team to the AITC Build Manager via a Change Order. The AITC Build Manager will follow the installation steps in [Section 0](#_bookmark24) to complete the product’s activation at AITC. The Implementation Manager has assured site readiness by assessing the readiness of the receiving site to deploy the product. AITC, under contract, will provide the product dependencies, power, equipment, space, manpower, etc., to ensure the successful activation of this product.

## Application Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following diagram represents the high-level architecture for the BMS application. BMS is a national application deployed at the AITC data center. The application is accessed at VA medical centers using approved web browser software. BMS reads data from VistA systems associated with each site’s VistA instance.

<span id="_Toc71893797" class="anchor"></span>Figure 2: BMS Architecture Diagram

![](bed-management-solution-version-2-9-dibr/003.png)

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This product will be released to AITC. The AITC, under contract, will house and secure this product on its Pre-Production and Production servers. The BMS system will be available to VA users on a continuous basis (excluding scheduled maintenance activities).

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> AITC will host the web and application servers for the BMS system.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> BMS will be supported on VA equipment that currently runs the existing BMS 2.3.1 system; therefore, no site preparation activities are required.

### Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the hardware, software, and communications for the deployment of BMS, where applicable.

#### Facility Specifics

> No facility-specific features are required for this deployment.

#### Hardware

> As middleware, BMS v2.9 requires no hardware to install. BMS v2.9 will be supported on existing VA equipment.

#### Software

> BMS v2.9 will be updating the system to implement a patch to fix post-deployment defect fixes. Other than changes to the application files and database objects, no new COTS software or database/operating system updates are required.

> The software components and database change scripts will be staged at the following location:

> \[BMS Team Share Location\]\prod_deployment\patches

#### Communications

This section outlines the communications to be distributed to the business user community:

- Communication between the development team, AITC, and the Sustainment team will occur via email and conference calls scheduled through Microsoft Lync.
- Notification of scheduled maintenance periods that require the service to be offline or that may degrade system performance will be disseminated to the business user community a minimum of 48 hours prior to the scheduled event.
- Notification to VA users for unscheduled system outages or other events that impact the response time will be distributed within 30 minutes of the occurrence.

#### Development/Installation/Back-Out Checklist

> The table below outlines the coordination effort and documents the day/time/individual when each activity (deploy, install, back-out) is completed for BMS v2.9. The table will be populated once the activities are completed.

| Activity | Day   | Time | Individual who completed task |
|--------------|-----------|----------|-----------------------------------|
| Deploy       | 9/15/2021 | 11a CST  |                                   |
| Install      | 9/15/2021 | 11a CST  |                                   |
| Back-Out     | TBD       |          |                                   |

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the minimum requirements for the product to be installed, as well as the recommended hardware and software system requirements. BMS v2.9 is being deployed to fix post deployment defects. As an upgrade, there are no changes to the existing hardware and software system components. The only changes are to the BMS application and database objects - to support the BMS v2.9 functionality.

### Pre-installation Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Download the files from the following directories and download to the applicable App, Web, and Database servers:

> \[BMS TeamShare\] Release_EVS_2021\Prod\\

> \[BMS TeamShare\] DBA\\DB_deployment_scripts\EVS_Release\\

#### Database Server

> This section outlines the installation steps for the various BMS v2.9 database components on vaaussqlbms210.

> VAAUSSQLBMS210

1\. Stop the BMS.VI.ServiceHost on vaausappbms211

2\. Backup the directory \\vaausappbms211 D:\Services\BMS

4\. Restart the BMS.VI.ServiceHost on vaausappbms211

5\. Execute the scripts located on the database server by editing the \_Inflow_DB_deployment_automation_script.sql and updating the scripts Directory folder line that starts with Set @Dir… for each of the following folders:

- 1.13_AuthZ_PostDeploy\\
- 1.20_EVS_tables_01\\
- 1.22_AC\\
- 1.23_EVS_tables_02_AfterETL\\
- 3_DH\\
- 4_JM_JP_AS

6\. Enable Transactional replication to VAAAUSSQLBMS211 and 212 from VAAUSSQLBMS210 for the following BMS tables:

- Bed
- BedBedStatuses
- BedBoardModule
- BedStatus
- BedUnavailableReason
- BedWardGroups
- CensusCategory
- Comments
- Decision
- Disposition
- Era
- EvacDisposition
- EvacTransportationProvider
- EvacTransportationType
- Facility
- FeeDisposition
- FeeReason
- Gender
- GenderColor
- HAvBed
- Location
- LocationStatus
- MedicalDivision
- Numa
- OrderableItem
- OrderableItemType
- OrderableItemTypeFacilities
- Patient
- PatientWaitingTimes
- PatientWaitingViews
- Physician
- PTDisplay
- Region
- SchedAdmNextDays
- SelectBedGroupingsView
- ServiceReceivingFee
- Specialty
- State
- TimeZone
- TransactionBed
- TransferStatus
- TreatingSpecialty
- Visn
- WaitingArea
- WaitListView
- Ward
- WardBeds
- WardBedsBedStatuses
- Wardgroup
- WardOccupancyBedFilter
- WardType

VAAUSSQLBMS211

7\. Navigate to the VAAUSSQLBMS211 report server portal.

8\. Backup the following RDL files on VAAUSSQLBMS211:

- BMS\Others\Audit Log Report.rdl
- BMS\Emergency Management Report.rdl
- BMS\Facility Diversion report.rdl
- BMS\VISN Diversion Report.rdl
- BMS\VISN Emergency Management Report.rdl

b\. Upload the updated Audit Log Report to the BMS\Others folder and the Emergency Management Report, Facility Diversion Report, VISN Diversion Report, and VISN Emergency Management Report to the BMS folder from this location: [\[BMS TeamShare\]\DBA\\DB_deployment_scripts\EVS_Release\EVS Report RDLs\\](file:///\\vaaussqlbms801\bms_team\DBA\_DB_deployment_scripts\EVS_Release\EVS%20Report%20RDLs\)

#### Web Server

> This section outlines the installation steps for the BMS components on the web server – vaauswebbms210.

1.  Backup the D:\Web directory on VAAUSWEBBMS210.
2.  Copy the [\[BMS Teamshare\]Release_EVS_2021\Prod \BMS.Web.210.2.8.19.1.zip](file:///\\vaaussqlbms801\bms_team\Release_EVS_2021\Prod%20\BMS.Web.210.2.8.19.1.zip) file to a local directory/desktop on VAAUSWEBBMS210

#### App Servers

> This section outlines the installation steps for the BMS components on the App server for vaausappbms210 and vaaausappbms211.

1.  Backup affected app dll’s from D:\Services\BMS both on VAAUSAPPBMS210 and VAAUSAPPBMS211.

> VAAUSAPPBMS210

2.  Copy the [\[BMS TeamShare\]Release_EVS_2021\Prod\BMS.Services.210.2.8.19.1.zip](../../../AppData/Local/Microsoft/Windows/INetCache/Content.Outlook/V9S2BLDU/%20/vaaussqlbms801/bms_team/Release_EVS_2021/Prod/BMS.Services.210.2.8.19.1.zip) file to a local directory/desktop on VAAUSAPPBMS210.
3.  Extract the contents of the .zip file and copy to D:\Services\\

> VAAUSAPPBMS211

4.  Copy the [\[BMS TeamShare\]Release_EVS_2021\Prod\BMS.Services.211.2.8.19.1.zip](../../../AppData/Local/Microsoft/Windows/INetCache/Content.Outlook/V9S2BLDU/%20/vaaussqlbms801/bms_team/Release_EVS_2021/Prod/BMS.Services.211.2.8.19.1.zip) file to a local directory/desktop on VAAUSAPPBMS210.
5.  Extract the contents of the .zip file and copy to D:\Services\\

## Post-installation and Smoke Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the post-installation activities and the minimum BMS v2.9 functionality to smoke test.

### Post-installation Activities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Log into the BMS Web Application*.*

### Smoke Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Perform Smoke Testing
    1.  The CancelOrder numbers should not get higher as the day/week progresses. Canceled orders should be properly processed and not accumulate
    2.  User is able to view/load the User Acces Report from the "BMS User Add/Edit" page
    3.  User is able to transfer patients from the Facility to VISN bed board, with the correct wait times listedVerify that User Roles work according to the previous version of BMS.

### From: Bed Management Solution Version 2.6 DIBR

### December 2020 v1.4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs
> Office of Information and Technology (OI&T)
> Revision History
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/04/2020</td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td>Updates for WEBB*2*18 BMS Release</td>
<td>S. Davidson</td>
</tr>
<tr class="even">
<td>10/06/2020</td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td>Updates for WEBB*2*17 BMS Release</td>
<td>David Horn</td>
</tr>
<tr class="odd">
<td>07/21/2020</td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td>Updated for WEBB*2*17 BMS Release</td>
<td>S. Davidson</td>
</tr>
<tr class="even">
<td>05/29/2020</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td>Updated for WEBB*2*16 BMS Patch</td>
<td>David Horn</td>
</tr>
</tbody>
</table>
> Artifact Rationale
> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.
> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

### ### # Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Table of Figures
> [Figure 1: BMS Overview 2](#_bookmark3)
> [Figure 2: BMS Architecture Diagram 5](#_bookmark12)

### List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities 4](#_bookmark6)
> [Table 2: Deployment Timeline 4](#_bookmark9)
> [Table 3: Deployment/Installation/Back-Out Checklist 7](#_bookmark22)
> BMS v2.4

## ![](bed-management-solution-version-2-6-dibr/003.png)Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The software needs to address system-related issues associated with the currently deployed BMS v.2.4.10 product, while continuing to meet functional business needs and requirements of the business owner.

> The objective of this software release is to enhance the current BMS functionality as part of the nationally supported Class I solution, while complying with all previously established VA national release criteria.

> Specific functionalities to be deployed in this release of BMS v2.4 will enhance functionalities of the following components of the system:

- Redeployment of repaired Bulk Add/Edit User
- Email Alert for Patients added to the National Wait List
- Census Category fix to display “N/A” for Wards not configured
- Bulk Bed Processing enhancements – bed management, return to service, evacuation icon
- Hover feature for patients who are Opt-Out
- Correct defect with CLC column not filtering when populated on facility PPBP list
- Provide clearer guidance for users on Whiteboard Bed Edit Page
- Evacuation patient logic enhancement

> BMS v2.4 will be a single code base system supporting all VAMCs and Veterans Integrated Service Networks (VISNs).

> BMS v2.4 will be hosted in a browser-controlled environment.

> BMS v2.4 design will support the server configurations deployed at the Austin Information Technology Center (AITC) that hosts BMS v.2.4.

## ![](bed-management-solution-version-2-6-dibr/004.png)Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The product will be released by the BMS Development Team to the AITC Build Manager via a Change Order. The AITC Build Manager will follow the installation steps in [Section 0](#installation) to complete the product’s activation at AITC. The Implementation Manager has assured site readiness by assessing the readiness of the receiving site to deploy the product. AITC, under contract, will provide the product dependencies, power, equipment, space, manpower, etc., to ensure the successful activation of this product.

## ![](bed-management-solution-version-2-6-dibr/005.png)Application Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following diagram represents the high-level architecture for the BMS application. BMS is a national application deployed at the AITC data center. The application is accessed at VA medical centers using approved web browser software. BMS reads data from VistA systems associated with each site’s VistA instance.

![](bed-management-solution-version-2-6-dibr/006.png)

> <span id="_bookmark12" class="anchor"></span>Figure 2: BMS Architecture Diagram

## ![](bed-management-solution-version-2-6-dibr/007.png)Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the minimum requirements for the product to be installed, as well as the recommended hardware and software system requirements. BMS 2.4 is being deployed to fix post deployment defects. As an upgrade, there are no changes to the existing hardware and software system components. The only changes are to the BMS application and database objects

> \- to support the BMS 2.4 functionality.

## Database Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the installation steps for the various BMS v2.4 database components on vaaussqlbms210.

1.  Execute the database scripts located in the [\\vaaussqlbms801\bms_team\Release 2 2020\\ Prod\SQL.zip](file:///\\vaaussqlbms801\bms_team\Release%202%202020\%20Prod\SQL.zip)

## Web Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the installation steps for the BMS components on the web server – vaauswebbms210.

1.  Backup affected web dll’s from D:\BMSWeb\\
2.  Install modified web dll’s on the web server in the D:\BMSWeb\\ directory, which will restart the web services and update cache

## App Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the installation steps for the BMS components on the web server – vaausappbms210 and vaaausappbms211.

1.  Backup affected app dll’s from D:\Services\BMS both on VAAUSAPPBMS200 and VAAUSAPPBMS201.
2.  Stop the following Services on VAAUSAPPBMS200 and VAAUSAPP201, in order as listed: VAAUSAPPBMS200: (BMS.BedManagerService, BMS.SecurityHost, BMS.ServiceHost) VAAUSAPPBMS201: (BMS.VI.ServiceHost, BMS.ServiceHost)
3.  Install modified app dll’s on the app servers in the D:\Services\BMS directories on VAAUSAPPBMS200 and VAAUSAPPBMS201, which will restart the web services and update cache
4.  Start the following Services on VAAUSAPPBMS200 (in order as listed): BMS.ServiceHost, BMS.SecurityHost, BMS.BedManagerService and VAAUSAPPBMS201 (in order as listed): BMS.ServiceHost, BMS.VI.ServiceHost

## ![](bed-management-solution-version-2-6-dibr/008.png)Post-installation and Smoke Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the post-installation activities and the minimum BMS 2.4 functionality to smoke test.

### From: Bed Management Solution Version 2.5 DIBR

### October 2020 v1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs
> Office of Information and Technology (OI&T)
> Revision History
<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10/6/2020</td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td>Updates for WEBB*2*17 BMS Release</td>
<td>David Horn</td>
</tr>
<tr class="even">
<td>7/21/2020</td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td>Updated for WEBB*2*17 BMS Release</td>
<td>S. Davidson</td>
</tr>
<tr class="odd">
<td>5/29/2020</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td>Updated for WEBB*2*16 BMS Patch</td>
<td>David Horn</td>
</tr>
</tbody>
</table>
> Artifact Rationale
> This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.
> Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

## ![](bed-management-solution-version-2-5-dibr/003.png)Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The software needs to address system-related issues associated with the currently deployed BMS v.2.4.10 product, while continuing to meet functional business needs and requirements of the business owner.

> The objective of this software release is to enhance the current BMS functionality as part of the nationally supported Class I solution, while complying with all previously established VA national release criteria.

> Specific functionalities to be deployed in this release of BMS v2.4 will enhance functionalities of the following components of the system:

- Redeployment of repaired Bulk Add/Edit User
- Email Alert for Patients added to the National Wait List
- Census Category fix to display “N/A” for Wards not configured
- Bulk Bed Processing enhancements – bed management, return to service, evacuation icon
- Hover feature for patients who are Opt-Out
- Correct defect with CLC column not filtering when populated on facility PPBP list
- Provide clearer guidance for users on Whiteboard Bed Edit Page
- Evacuation patient logic enhancement

> BMS v2.4 will be a single code base system supporting all VAMCs and Veterans Integrated Service Networks (VISNs).

> BMS v2.4 will be hosted in a browser-controlled environment.

> BMS v2.4 design will support the server configurations deployed at the Austin Information Technology Center (AITC) that hosts BMS v.2.4.

## ![](bed-management-solution-version-2-5-dibr/004.png)Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The product will be released by the BMS Development Team to the AITC Build Manager via a Change Order. The AITC Build Manager will follow the installation steps in [Section 0](#installation) to complete the product’s activation at AITC. The Implementation Manager has assured site readiness by assessing the readiness of the receiving site to deploy the product. AITC, under contract, will provide the product dependencies, power, equipment, space, manpower, etc., to ensure the successful activation of this product.

## ![](bed-management-solution-version-2-5-dibr/005.png)Application Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following diagram represents the high-level architecture for the BMS application. BMS is a national application deployed at the AITC data center. The application is accessed at VA medical centers using approved web browser software. BMS reads data from VistA systems associated with each site’s VistA instance.

![](bed-management-solution-version-2-5-dibr/006.png)

> <span id="_bookmark12" class="anchor"></span>Figure 2: BMS Architecture Diagram

## ![](bed-management-solution-version-2-5-dibr/007.png)Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the minimum requirements for the product to be installed, as well as the recommended hardware and software system requirements. BMS 2.4 is being deployed to fix post deployment defects. As an upgrade, there are no changes to the existing hardware and software system components. The only changes are to the BMS application and database objects

> \- to support the BMS 2.4 functionality.

## ![](bed-management-solution-version-2-5-dibr/008.png)Post-installation and Smoke Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section outlines the post-installation activities and the minimum BMS 2.4 functionality to smoke test.
