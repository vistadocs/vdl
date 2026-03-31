---
consolidated_title: "mocha server deployment, installation, back-out, and rollback guide"
app_code: PREM
doc_type: DIBR
master_source: "PREM*4*1 MOCHA Server Version 4 Deployment, Installation, Back-out, and Rollback Guide"
master_pub_date: June 2024
consolidated_from: 5 versions
prior_versions:
  - "PREM*3*3 MOCHA Server Version 3.2 Deployment, Installation, Back-out, and Rollback Guide"
  - "PREM*3*4 MOCHA Server Version 3.2.1 Deployment, Installation, Back-out, and Rollback Guide"
  - "PREM*3*5 MOCHA Server Version 3.3.1 Deployment, Installation, Back-out, and Rollback Guide"
  - "PREM*4*2 MOCHA Server Deployment, Installation, Back-out, and Rollback Guide"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Medication Order Check Healthcare Application (MOCHA) 4.0

  Deployment, Installation, Back-Out, and Rollback Guide (DIBR)
---

![](prem-4-1-mocha-server-version-4-deployment-installation-back-out-and-rollback-gu/001.png)

June 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| Date   | Version | Description        | Author           |
|------------|-------------|------------------------|----------------------|
| 06/28/2024 | 1.0         | MOCHA 4.0 / PREM\*4\*1 | Liberty IT Solutions |

<span id="_Toc170471236" class="anchor"></span>Table : Site Preparation

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

The Veteran-focused Integrated Process (VIP) 4.0 Guide indicates the VA Product (Line) Accountability and Reporting System (VA PARS) reporting tool requires a Gateway Review that will move the project from the Planning Stage and to the Build Stage and will require Release Approval before deploying into production. The Product Line Manager will ensure necessary documents are made available for the release approval process.

Table of Contents

List of Tables

List of Figures

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
    - [The detailed hardware configuration for MOCHA Server is contained in the RHEL 7 specification](#the-detailed-hardware-configuration-for-mocha-server-is-contained-in-the-rhel-7-specification)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Oracle Scheduler](#oracle-scheduler)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
    - [Remove New Release](#remove-new-release)
    - [Deploy Rolled-Back Release](#deploy-rolled-back-release)
    - [Backout Steps for LOG4J2](#backout-steps-for-log4j2)
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
This document describes how to deploy and install the various components of the patch PREM\*4\*1 for the Medication Order Check Healthcare Application (MOCHA) version (v) 4.0 Server, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial Off-the-Shelf (COTS) product is being installed, the vendor provided User and Installation guide may be used, but the back-out recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the MOCHA v4.0 server patch, PREM\*4\*1, will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. This guide also identifies resources, communications plan, and rollout schedule. Specific instructions for deployment, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The following pre-existing MOCHA interfacing systems must be available during the deployment.
  - Web Application Server (WebLogic)
  - MOCHA Build EAR file
  - Data source changes relative to First Databank (FDB) Framework (Fwk) 4.5
- Oracle Database
  - Exported FDB Fwk v4.5 file
  - Import / Materialized View Scripts

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints for the PREM\*4\*1 release.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc170471235" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| ID | Team                  | Phase / Role | Tasks                                                                                                           | Project Phase (See Schedule) |
|--------|---------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|----------------------------------|
| 1      | Enterprise Operations/OIT | Deployment       | Plan and schedule deployment (including orchestration with vendors)                                                 |                                  |
| 2      | OIT                       | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          |                                  |
| 3      | Enterprise Operations     | Deployment       | Test for operational readiness                                                                                      |                                  |
| 4      | Enterprise Operations     | Deployment       | Execute deployment                                                                                                  |                                  |
| 5      | Enterprise Operations     | Installation     | Plan and schedule installation                                                                                      |                                  |
| 6      | OIT                       | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                       |                                  |
| 7      | OIT                       | Installation     | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         |                                  |
| 8      | OIT                       | Installations    | Coordinate training                                                                                                 |                                  |
| 9      | OIT                       | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |                                  |
| 10     | Enterprise Operations/OIT | Post Deployment  | Hardware, Software and System Support                                                                               |                                  |

<span id="_Toc170471239" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

<span class="mark">  
</span>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the schedule and milestones for the deployment.

Contract Dates :

- Base Period: 5/4/2020 – 5/3/2021
- Extension Period 1: 5/6/2021 – 10/7/2022
- Extension Period 2: 9/16/2022 – 2/15/2023
- Extension Period 3: 2/15/2023 – 9/26/2023
- Extension Period 4: 9/26/2023 – 9/15/2024

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MOCHA v4.0 will be nationally deployed at AITC after Intial Operation Capcity (IOC) testing and national release deployment.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MOCHA Java Application is a single, nationally deployed web application deployed in AITC. The deployment will be coordinated with AITC in accordance with Veterans Affairs (VA) standard release procedures. For AITC installation scheduling will be done via the EO release calendar. Requests for a release will be made through the AITC Request for Change Order (RFCO) Form and submitted at least 2 days prior to the deployment date. This process will ensure that resources are available to deploy changes. All changes are deployed and tested in the lower environments (development, Computer Emergency CERT, and Pre-Prod) before being deployed to production.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The diagram below shows the target deployment topology of MOCHA Server in the AITC EO Cloud.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc158032713" class="anchor"></span>Figure 1: MOCHA Server

![](prem-4-1-mocha-server-version-4-deployment-installation-back-out-and-rollback-gu/002.png)

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Site/Other                                              | Problem/Change Needed                                                   | Features to Adapt/Modify to New Product | Actions/Steps                                                                                                                                                               | Owner |
|-------------------------------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| New WebLogic Manage Server Configuration for 4.5 deployment | New port on the traffic manager may be necessary for the new managed server |                                             | Note: 3.3 and 4.5 versions will be running concurrently until all sites are pointing to 4.5. After all sites point to 4.5, 3.3 will be removed from the WebLogic configuration. |           |
| 4.5 Schema set up in Oracle                                 | Load up to date 4.5 data from FDB                                           |                                             |                                                                                                                                                                                 |           |
| New datasource set up in WebLogic for 4.5 Oracle Schema     |                                                                             |                                             |                                                                                                                                                                                 |           |
| Providing MOCHA EAR file for the current released version   |                                                                             |                                             |                                                                                                                                                                                 |           |

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following section describes the hardware, software, and facilities required for the deployment and installation of the MOCHA v4.0 Server.

Additional information may be found in the MOCHA Server Production Operations Manual (POM) located in the MOCHA Server Documentation stream under the PHARM project area in Return to Clinic (RTC).

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

<span id="_Toc170471237" class="anchor"></span>Table 3: Facility-Specific Features

| Site | Space/Room | Features Needed | Other |
|----------|----------------|---------------------|-----------|
| N/A      |                |                     |           |

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The detailed hardware configuration for MOCHA Server is contained in the RHEL 7 specification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-----------------------|-----------|-------------|-------------------|------------------|-----------|
| N/A                   |           |             |                   |                  |           |

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

<span id="_Toc170471238" class="anchor"></span>Table 4: Software Specifications

| Required Software                       | Version             | Configuration |
|-----------------------------------------|---------------------|---------------|
| Oracle WebLogic                         | 12.2.1.4            | Pre-existing  |
| Oracle 19c Enterprise Edition Release   | 19.14.0.0.0         | Pre-existing  |
| Red Hat Enterprise Linux Server (RHELS) | 7.0 (Santiago)      | Pre-existing  |
| Java Software Development Kit (SDK)     | 1.8.0_391 or higher | Pre-existing  |

Please see the Roles and Responsibilities table in 2above for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Notify business owner of production deployment.
- The Release Manager will schedule activities and identify the required personnel for each activity.
- Meetings will be scheduled for deployment personnel to work through the deployment steps.

#### Deployment/Installation/Back-Out Checklist

| Activity | Day | Time | Individual who completed task  |
|----------|-----|------|--------------------------------|
| Deploy   | TBD | TBD  | Infrastructure Operations (IO) |
| Install  | TBD | TBD  | IO                             |
| Back-Out | N/A | N/A  | IO                             |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation is not applicable for PREM\*4\*1, because this is a patch-specific deployment.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MOCHA J2EE application will be installed on the existing MOCHA v3.0 production platform.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pre-existing MOCHA v3.0 platform will be used.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Software configuration and deployment artifacts will be provided with the Request for Change Order (RFC). The file(s) will be provided electronically copied to an appropriate location and the path communicated to the Enterprise Operations (EO) team.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of scripts noted in the next section assumes that Oracle 19c Database Server is configured and running. Proper installation of the Oracle Relational Database Management System (RDBMS) is one in which the Oracle Universal Installer and DBCA were used to perform an error-free installation and a general purpose instance was created. A properly configured Oracle RDBMS is one in which the associated Oracle application development and configuration tools, namely Structured Query Language (SQL)\*Plus, can be used to connect to the instance through a Transparent Network Substrate alias.

The installation of scripts noted in the next section will create a set of materialized view artifacts in order to enable FDB data to be read from another database/environment. Prior to this solution being completely implemented, there must also be a database link created to this database which houses FDB45ADM schema objects.

Execute the following scripts on the target database which contains the FDB related schema objects to create the materialized view artifacts and permissions needed by any sourcing database. After executing the scripts noted below, the FDB data will be accessed via database link created for that purpose.

On the sourcing database(s) through the database link and its authorized account, you may now access the FDB data through the aforementioned database link and account.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation scripts needed for the database installation, as well as the procedure on how to set up FDB Fwk v4.5, are provided in VA GitHub EC, located in the [mocha-code](https://github.ec.va.gov/EPMO/mocha-code/tree/master) repository docs folder. DBA should make sure to disable the archive mode before setting up 4.5 schema and then enable it after schema import.

<span id="_Toc158032714" class="anchor"></span>Figure : Installation Scripts

![](prem-4-1-mocha-server-version-4-deployment-installation-back-out-and-rollback-gu/003.png)

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable.

## Oracle Scheduler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MOCHA Materialized Views refresh is from the Oracle Scheduler. The MOCHA Server pulls the data from Pharmacy Enterprise Customization System (PECS) incrementally.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Linux System Administrator will need:

- Access to the Linux console of the server where MOCHA WebLogic is running
- Access to the WebLogic web-based Console
- Access to the location indicated in section 4.5 Installation Scripts

Database Administrator will need:

- Access to the Linux console of the server where FDB Oracle Database is running
- Access to the location indicated in section 4.5 Installation Scripts

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation instructions found within this guide are intended to be performed on a clean installation of WebLogic 12.2.1.4.1, with a separate managed server to act as the Deployment Server. For details on completing the installation of the following items, please refer to each item’s installation and configuration documentation supplied by Oracle.

For successful deployment of the MOCHA Server software, the following assumptions must be met:

- The Deployment Server is configured and running.
- WebLogic is configured to run with the Java™ Standard Edition Development Kit, Version 1.8+.
- Access to the WebLogic console is by means of any valid administrative user name and password.
- The proper Oracle 19c database driver libraries for the chosen deployment environment are present on the class path for the respective Deployment Servers.
- Red Hat Enterprise Linux 7.x operating system is properly installed.
- Domain Name Server (DNS) resolution is configured for the MOCHA Server.
- The installation instructions are followed in the order that the sections are presented within this Installation Guide.
- PECS database server loads MOCHA Materialized Views to MOCHA Server.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the MOCHA Server ear file has been deployed successfully, it can be verified by accessing an xml page from a web browser.

Open a web browser, and enter the URL in the following format:

http://*mochaserverhostname*:*port*/MOCHA/ordercheck, where the *mochaserverhostname* is the fully-qualified domain name of the Linux server running MOCHA Server, and *port* is the port number where the ear file was deployed in WebLogic. Here is a sample URL for reference: http://exampleserver.abc.va.gov:\<Deployment Server Port\>/MOCHA/ordercheck.

If the MOCHA Server application is up, the browser should return xml that looks similar to this:

<span id="_Toc158032716" class="anchor"></span>Figure : Sample MOCHA Server XML

![](prem-4-1-mocha-server-version-4-deployment-installation-back-out-and-rollback-gu/004.png)

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backout plan will be executed if deployment fails functional testing and cannot be remediated immediately.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous mocha-server-3.x.xx.xxxx.ear and old log4j files still exist in installation directory.

1.  Delete FDB45_DIF data source in WebLogic.
2.  Delete mocha-server-4.0.01.0000.ear .ear *(refer to section Error! Reference source not found. for detailed steps for removing the new ear files)*.
3.  Deploy 3.x.xx.xxxx.ear (refer *section Error! Reference source not found. for detailed steps for deploying old ear files)*.
4.  Smoke test WebLogic.
5.  Validate backout was successful.

### Remove New Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Open and log into the WebLogic console. Use WebLogic username and password.
2.  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3.  Within the *Change Center* panel in the left column of the WebLogic console, select Lock & Edit.
4.  WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
5.  Select the previously deployed MOCHA deployment, select Stop, and then select Force Stop Now from the drop-down list.
6.  WebLogic will now display the panel *Force Stop Application Assistant* in the right column of the console for confirmation to start servicing requests.
7.  Select Yes in the *Force Stop Application Assistant* panel in the right column of the WebLogic console.
8.  WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
9.  Verify that the State of the MOCHA deployment is Prepared.
10. Select the previously deployed MOCHA deployment, and then select Delete.
11. WebLogic will now display the panel *Delete Application Assistant* in the right column of the console for confirmation to start servicing requests.
12. Select Yes in the *Delete Application Assistant* panel in the right column of the WebLogic console.
13. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
14. Verify that the MOCHA deployment is deleted and no longer present.

### Deploy Rolled-Back Release

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps detail the deployment of the rolled-back MOCHA application.

1.  Use the WebLogic console that was started at the beginning of the roll-back process.
2.  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3.  Verify that the application is in *Lock & Edit* mode. *Lock & Edit* mode is indicated by the greyed-out Lock & Edit selection button.
4.  Select the Install button in the *Deployments* panel in the right column of the WebLogic console.
5.  WebLogic will now display the panel *Install Application Assistant* in the right column of the console, where the location of the MOCHA deployment will be found.
    1.  If the rolled-back MOCHA deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the *Location* panel, which is within the *Install Application Assistant* panel in the right column of the console. Choose the ear file associated with the rolled-back release.
    2.  If the rolled-back MOCHA deployment has not been transferred to the Deployment Machine:
        1.  Select on the upload your file(s) link in the *Install Application Assistant* panel in the right section of the console.
        2.  Select the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
        3.  Select Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the *Locate deployment to install and prepare for deployment* panel within the *Install Application Assistant*.
6.  Once the rolled-back MOCHA deployment is located and selected, select Next.
7.  WebLogic will now display the panel *Choose targeting style* within the *Install Application Assistant* in the right column of the console. Leave the default value selected, install this deployment as an application, and select Next.
8.  Within the *Install Application Assistant* in the right column of the console, WebLogic will now display the panel *Select deployment targets*, where the Deployment Server will be selected as the target in the next step.
9.  For the Target, select the Deployment Server.
10. Select Next.
11. Within the *Install Application Assistant*, WebLogic will now display the panel *Optional Settings* in the right column of the console, where the name of the deployment and the copy behavior are chosen.
12. Enter the Name for the deployment. Use: mocha-server-3.1.00.0028 verify that the following default option for Security is selected:
13. DD Only: Use only roles and policies that are defined in the deployment descriptors.
14. Verify that the following default option for Source accessibility is selected.
15. Use the defaults defined by the deployment's targets.
16. Select Next.
17. Within the *Install Application Assistant*, in the right column of the console WebLogic, the panel *Review your choices and click Finish* will now be displayed, which summarizes the steps completed above.
18. Verify that the values match those entered in Steps 6 through 17 and select Finish.
19. WebLogic will now display the panel *Settings for MOCHA*, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
20. Leave all the values as defaulted by WebLogic and select Save.
21. Within the *Change Center* panel in the left column of the WebLogic console, select Activate Changes.
22. Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
23. WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
24. Select the previously deployed mocha-server-3.1.00.0028 deployment, select Start, and then select Servicing all requests from the drop-down list.
25. WebLogic will now display the panel *Start Application Assistant* in the right column of the console for confirmation to start servicing requests.
26. Select Yes in the *Start Application Assistant* panel in the right column of the WebLogic console.
27. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
28. Verify that the State of the mocha-server-3.1.00.0028 deployment is Active.

### Backout Steps for LOG4J2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Shutdown WebLogic servers.
2.  Restore the old log4j2 jar file.
    1.  log4j-api-2.17.1.jar
    2.  log4j-core-2.17.1.jar
3.  Update the Arguments and Class Path with the old system property and log4j library version.
4.  Add the argument:
    1.  Dlog4j.configurationFile=/u01/app/oracle/user_projects/domains/moc-prod/moc-config/log4j2.xml
5.  Restart the Servers.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the MOCHA Server ear file has been deployed and log4j2 is restored to the old version successfully, it can be verified by accessing an xml page from a web browser.

Open a web browser and enter the URL in the following format:

http://*mochaserverhostname*:*port*/MOCHA/ordercheck, where the *mochaserverhostname* is the fully-qualified domain name of the Linux server running MOCHA Server, and *port* is the port number where the ear file was deployed in WebLogic. Here is a sample URL for reference: http://exampleserver.abc.va.gov:\<Deployment Server Port\>/MOCHA/ordercheck

If the MOCHA Server app is up, the browser should return xml that looks similar to this:

\<?xml version="1.0" encoding="UTF-8"?\>

\<exception xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="<span class="mark">REDACTED</span>" xsi:schemaLocation="<span class="mark">REDACTED</span>"\>\<code\>PRE\</code\>\<message\>No XML request was sent. The xmlRequest parameter must be set with the XML containing the request to process.\</message\>\<detailedMessage\>\<\![CDATA\[

Further details for this error have been logged. Contact the system administrator to obtain the log file.

\]\]\>\</detailedMessage\>\</exception\>

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable because there is no data update for PREM\*4\*1.

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

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PREM*3*3 MOCHA Server Version 3.2 Deployment, Installation, Back-out, and Rollback Guide

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Provide the mocha 3.2.00.0000.zip file to the AITC team. The zip file includes the following files for EAR file deployment and log4j2.14 upgrade:

- mocha-server-3.2.00.0000.ear
- log4j-api-2.14.0.jar
- log4j-core-2.14.0.jar

## Deployment Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the deployment procedure:

1)  Shutdown WebLogic servers.
2)  Delete mocha-server-3.1.00.0000 ear from WebLogic.
3)  Deploy mocha-server-3.2.00.0000.ear.
4)  Back-up the old log4j jar files:
    1.  log4j-api-2.10.0.jar
    2.  log4j-core-2.10.0.jar
5)  Replace the old jar files with the new version of jar files:
    1.  log4j-api-2.14.0.jar
    2.  log4j-core-2.14.0.jar
6)  Update the Arguments and Class Path wtih the new log4j2 system property and library version:
    1.  Dlog4j2.configurationFile=/u01/app/oracle/user_projects/domains/moc-prod/moc config/log4j2.xml
7)  Restart the servers.
8)  Smoke Test WebLogic.
9)  Validate deployment was successful.

## Backout Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous mocha-server-3.1.00.0000.ear and old log4j files still exist in installation directory.

### Backout Steps for EAR file:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  Delete mocha-server-3.2.00.0000.ear *(refer to section 4.1.2.1 for detailed steps for removing new ear files)*.
2)  Deploy 3.1.00.0000.ear (*refer section 4.1.2.2 for detailed steps for deploying old ear files*).
3)  Smoke Test WebLogic.
4)  Validate back-out was successful.

#### Remove New Release

1)  Open and log into the WebLogic console. Use WebLogic username and password.
2)  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3)  Within the *Change Center* panel in the left column of the WebLogic console, select Lock & Edit.
4)  WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
5)  Select the previously deployed MOCHA deployment, select Stop, and then select Force Stop Now from the drop-down list.
6)  WebLogic will now display the panel *Force Stop Application Assistant* in the right column of the console for confirmation to start servicing requests.
7)  Select Yes in the *Force Stop Application Assistant* panel in the right column of the WebLogic console.
8)  WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
9)  Verify that the State of the MOCHA deployment is Prepared.
10) Select the previously deployed MOCHA deployment, and then select Delete.
11) WebLogic will now display the panel *Delete Application Assistant* in the right column of the console for confirmation to start servicing requests.
12) Select Yes in the *Delete Application Assistant* panel in the right column of the WebLogic console.
13) WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
14) Verify that the MOCHA deployment is deleted and no longer present.

#### Deploy Rolled-Back Release:

The following steps detail the deployment of the rolled-back MOCHA application:

1)  Use the WebLogic console that was started at the beginning of the rollback process.
2)  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3)  Verify that the application is in Lock & Edit mode. Lock & Edit mode is indicated by the greyed-out Lock & Edit selection button.
4)  Select the Install button in the *Deployments* panel in the right column of the WebLogic console.
5)  WebLogic will now display the panel *Install Application Assistant* in the right column of the console, where the location of the MOCHA deployment will be found.
    1.  If the rolled-back MOCHA deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the *Location* panel, which is within the *Install Application Assistant* panel in the right column of the console. Choose the ear file associated with the rolled-back release.
    2.  If the rolled-back MOCHA deployment has not been transferred to the Deployment Machine:
        1.  Select on the upload your file(s) link in the *Install Application Assistant* panel in the right section of the console.
        2.  Select the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
        3.  Select Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the *Locate deployment to install and prepare for deployment* panel within the *Install Application Assistant*.
6)  Once the rolled-back MOCHA deployment is located and selected, select Next.
7)  WebLogic will now display the panel *Choose targeting style* within the *Install Application Assistant* in the right column of the console. Leave the default value selected, install this deployment as an application, and select Next.
8)  Within the *Install Application Assistant* in the right column of the console, WebLogic will now display the panel *Select deployment targets*, where the Deployment Server will be selected as the target in the next step.
9)  For the Target, select the Deployment Server.
10) Select Next.
11) Within the *Install Application Assistant*, WebLogic will now display the panel *Optional Settings* in the right column of the console, where the name of the deployment and the copy behavior are chosen.
12) Enter the Name for the deployment. Use: mocha-server-3.1.00.0000.ear
13) Verify that the following default option for Security is selected:
14) DD Only: Use only roles and policies that are defined in the deployment descriptors.
15) Verify that the following default option for Source accessibility is selected:
16) Use the defaults defined by the deployment's targets.
17) Select Next.
18) Within the *Install Application Assistant*, in the right column of the console WebLogic, the panel *Review your choices and click Finish* will now be displayed, which summarizes the steps completed above.
19) Verify that the values match those entered in Steps 6 through 17 and select Finish.
20) WebLogic will now display the panel *Settings for MOCHA*, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
21) Leave all the values as defaulted by WebLogic and select Save.
22) Within the *Change Center* panel in the left column of the WebLogic console, select Activate Changes.
23) Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
24) WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
25) Select the previously deployed mocha-server-3.1.00.0000 deployment, select Start, and then select Servicing all requests from the drop-down list.
26) WebLogic will now display the panel *Start Application Assistant* in the right column of the console for confirmation to start servicing requests.
27) Select Yes in the *Start Application Assistant* panel in the right column of the WebLogic console.
28) WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
29) Verify that the State of the mocha-server-3.1.00.0000 deployment is Active.

### Backout Steps for LOG4J

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1)  Shutdown WebLogic servers.
2)  Restore the old log4j jar file.
    1.  log4j-api-2.10.0.jar
    2.  log4j-core-2.10.0.jar
3)  Update the Arguments and Class Path wtih the old system property and log4j library version.
4)  Add the argument:
    1.  Dlog4j.configurationFile=/u01/app/oracle/user_projects/domains/moc-prod/moc-config/log4j2.xml
5)  Restart the Servers.

### From: PREM*3*5 MOCHA Server Version 3.3.1 Deployment, Installation, Back-out, and Rollback Guide

## Deployment Steps:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Shutdown WebLogic servers

> <u>EAR File Deployment:</u>

2.  Delete mocha-server-3.2.01.0000 ear from WebLogic
3.  Deploy mocha-server-3.3.01.0000.ear

> <u>Migrating to LOG4J2:</u>

4.  Backup the old log4j jar files
5.  log4j-api-2.17.1.jar
6.  log4j-core-2.17.1.jar
7.  Replace the old log4j jar file with the new version of (below)jar files:

> log4j-api-2.20.0.jar

> log4j-core-2.20.0.jar

8.  Update the Class Path with the latest log4j2 library version.
9.  Restart the servers
10. Smoke Test Weblogic.
11. Validate deployment successful.

### Backout Steps for EAR file:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Delete mocha-server-3.2.01.0000.ear *(refer to section 4.1.2.1 for detailed steps for removing new ear files)*.
2.  Deploy 3.3.01.0000*.*ear *(refer to section 4.1.2.2 for detailed steps for deploying old ear files)*.
3.  Smoke Test WebLogic.
4.  Validate backout successful.

#### Remove New Release:

1.  Open and log into the WebLogic console. Use WebLogic username and password.
2.  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3.  Within the *Change Center* panel in the left column of the WebLogic console, select Lock & Edit.
4.  WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
5.  Select the previously deployed MOCHA deployment, select Stop, and then select Force Stop Now from the drop-down list.
6.  WebLogic will now display the panel *Force Stop Application Assistant* in the right column of the console for confirmation to start servicing requests.
7.  Select Yes in the *Force Stop Application Assistant* panel in the right column of the WebLogic console.
8.  WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
9.  Verify that the State of the MOCHA deployment is Prepared.
10. Select the previously deployed MOCHA deployment, and then select Delete.
11. WebLogic will now display the panel *Delete Application Assistant* in the right column of the console for confirmation to start servicing requests.
12. Select Yes in the *Delete Application Assistant* panel in the right column of the WebLogic console.
13. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
14. Verify that the MOCHA deployment is deleted and no longer present.

#### Deploy Rolled-Back Release:

The following steps detail the deployment of the rolled-back MOCHA application.

1.  Use the WebLogic console that was started at the beginning of the roll-back process.
2.  Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
3.  Verify that the application is in Lock & Edit mode. Lock & Edit mode is indicated by the greyed-out Lock & Edit selection button.
4.  Select the Install button in the *Deployments* panel in the right column of the WebLogic console.
5.  WebLogic will now display the panel *Install Application Assistant* in the right column of the console, where the location of the MOCHA deployment will be found.
    1.  If the rolled-back MOCHA deployment has already been transferred to the Deployment Machine, navigate to the deployment file location using the links and file structure displayed within the *Location* panel, which is within the *Install Application Assistant* panel in the right column of the console. Choose the ear file associated with the rolled-back release.
    2.  If the rolled-back MOCHA deployment has not been transferred to the Deployment Machine:
        1.  Select on the upload your file(s) link in the *Install Application Assistant* panel in the right section of the console.
        2.  Select the Deployment Archive Browse to see the Choose file dialogue used to select the Deployment Archive.
        3.  Select Next in the Upload a Deployment to the admin server panel in the right column of the WebLogic console to return to the *Locate deployment to install and prepare for deployment* panel within the *Install Application Assistant*.
6.  Once the rolled-back MOCHA deployment is located and selected, select Next.
7.  WebLogic will now display the panel *Choose targeting style* within the *Install Application Assistant* in the right column of the console. Leave the default value selected, install this deployment as an application, and select Next.
8.  Within the *Install Application Assistant* in the right column of the console, WebLogic will now display the panel *Select deployment targets*, where the Deployment Server will be selected as the target in the next step.
9.  For the Target, select the Deployment Server.
10. Select Next.
11. Within the *Install Application Assistant*, WebLogic will now display the panel *Optional Settings* in the right column of the console, where the name of the deployment and the copy behavior are chosen.
12. Enter the Name for the deployment. Use: mocha-server-3.2.01.0000.ear
13. Verify that the following default option for Security is selected:
14. DD Only: Use only roles and policies that are defined in the deployment descriptors.
15. Verify that the following default option for Source accessibility is selected:
16. Use the defaults defined by the deployment's targets.
17. Select Next.
18. Within the *Install Application Assistant*, in the right column of the console WebLogic, the panel *Review your choices and click Finish* will now be displayed, which summarizes the steps completed above.
19. Verify that the values match those entered in Steps 7 through 16 and select Finish.
20. WebLogic will now display the panel *Settings for MOCHA*, in the right column of the console, where the values previously entered are available as well as a setting to change the deployment order.
21. Leave all the values as defaulted by WebLogic and select Save.
22. Within the *Change Center* panel in the left column of the WebLogic console, select Activate Changes.
23. Within the *Domain Structure* panel in the left column of the WebLogic console, select the Deployments node.
24. WebLogic will now display the panel *Summary of Deployments* in the right column of the console, where all deployments for the WebLogic domain are listed.
25. Select the previously deployed mocha-server-3.2.01.0000 deployment, select Start, and then select Servicing all requests from the drop-down list.
26. WebLogic will now display the panel *Start Application Assistant* in the right column of the console for confirmation to start servicing requests.
27. Select Yes in the *Start Application Assistant* panel in the right column of the WebLogic console.
28. WebLogic now returns to the *Summary of Deployments* panel in the right column of the console.
29. Verify that the State of the mocha-server-3.3.01.0000 deployment is Active.

### Backout Steps for LOG4J:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Shutdown WebLogic servers
2.  Restore the old log4j jar file

> log4j-api-2.17.1.jar

> log4j-core-2.17.1.jar

3.  Update the Class Path with the old log4j library version.
4.  Restart the servers
