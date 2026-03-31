---
title: AMPL Deployment, Installation, Back-out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: AMPL
app_code: PREA
app_name: "Pharmacy: Advanced Medication Platform"
section: CLI
app_status: archive
pkg_ns: PREA
patch_ver: 1.14
patch_id: PREA*1.14
group_key: "PREA:PREA:1.14"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - table
  - contents
  - ampl
  - back
  - deployment
  - rollback
  - installation
  - application
  - procedure
  - span
page_count: 0
word_count: 3595
section_count: 31
table_count: 11
figure_count: 2
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2026
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA_Archive/PREA_1_14_AMPL_GUI_DIBRG.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA_Archive/PREA_1_14_AMPL_GUI_DIBRG.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=398"
---

---
title: |
  <span id="_Toc191980456" class="anchor"></span>Advanced Medication Platform (AMPL)  
  Graphical User Interface (GUI)

  <span id="_Toc191980457" class="anchor"></span>Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)
---

![](ampl-deployment-installation-back-out-and-rollback-guide/001.png)

January 2026

Office of Information and Technology (OIT)

Revision History

| Date    | Version | Description                                                                             | Author        |
|---------|---------|-----------------------------------------------------------------------------------------|---------------|
| 01/2026 | 1.14    | Basic Content Updates                                                                   | AMPL GUI Team |
| 08/2025 | 1.13    | Basic Content Updates                                                                   | AMPL GUI Team |
| 07/2025 | 1.12    | Basic Content Updates                                                                   | AMPL GUI Team |
| 04/2025 | 1.11    | Changed numbering to match Build version numbers, updated dates, added to Acronyms list | AMPL GUI Team |
| 01/2025 | 1.3     | Standardized fonts, font sizes, styles, and paragraph spacing                           | AMPL GUI Team |
| 11/2024 | 1.2     | Basic Content Updates                                                                   | AMPL GUI Team |
| 03/2024 | 1.1     | Content Update                                                                          | AMPL GUI Team |
| 08/2023 | 1.0     | Document Baseline                                                                       | AMPL GUI Team |

<span id="_Toc191980512" class="anchor"></span>Table 1: Dependencies

Artifact Rationale

This document describes the Deployment, Installation, Back-Out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-Out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

List of Tables

List of Figures

Figure 1: AMPL Deployment Logical [5](#_Toc140492253)

Figure 2: AMPL Deployment on ECS [6](#_Toc140492254)

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
  - [Pre-Installation and System Requirements](#pre-installation-and-system-requirements)
    - [AMPL GUI Application](#ampl-gui-application)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
    - [Install AWS ECS Instance](#install-aws-ecs-instance)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
    - [Create AWS ECS Cluster](#create-aws-ecs-cluster)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
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
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Acronyms](#acronyms)
This document describes how to deploy and install the AMPL GUI as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed commercial off-the-shelf (COTS) product is being installed, the vendor-provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the AMPL GUI will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Dependency                                                 | Type | Dependency Type     | Purpose                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------|----------|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VDIF – Veterans Data Integration and Federation (Health share) | Service  | Backend Data Source     | Mapped data will be provided via Veterans Data Integration & Federation (VDIF) Enterprise Platform (EP) with the use of Fast Healthcare Interoperability Resources (FHIR) messages. Screens display the appropriate fields and map to the appropriate underlining source element. VDIF also provides certain data through custom services that pull data directly from VistA. |
| Clinical Context Objective Workgroup (CCOW)                    | Service  | Patient Context Support | Synchronizes AMPL GUI patient context with other clinical applications.                                                                                                                                                                                                                                                                                                       |
| Identity and Access Management (IAM) SSOi (Single Sign-On)     | Service  | Access Authorization    | Authentication and Authorization Security provider                                                                                                                                                                                                                                                                                                                            |

<span id="_Ref135303288" class="anchor"></span>Table 2: Roles and Responsibilities

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMPL GUI project team, software, and servers will adhere to the following directives, policies, procedures, standards, and guidelines:

- Veteran-focused Integration Process (VIP)
- Section 508 Information Technology (IT) accessibility standards governed under 29 U.S.C 794d
- Health Insurance Portability and Accountability Act (HIPAA)
- VA DIRECTIVE 6508 - Privacy Impact Assessments
- VA Directive 6500 – Information Security Program
- One-VA Technical Reference Model (TRM)
- VA Standards & Conventions Committee (SACC) Codes Standards and Conventions
- Pass Web Application Security Audit (WASA) scans
- No Critical or High issues identified by a Fortify scan

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List the teams that will perform the steps described in this plan, and include the following information:

- Who is involved in these procedures?
- What teams are involved?
- Who is responsible for doing what tasks?
- What is the breakdown of labor and responsibilities?
- Who is in charge?
- Who will authorize the beginning of these procedures?

Identify technical and support personnel who will be involved in the deployment, installation, back-out, and rollback including installers, testers, implementation team, transition to sustainment team, end users, and others at each affected site. Identify the person(s) responsible for issuing the go / no-go prior to initial deployment, installation, and back-out / rollback order.

You may wish to include a Roles and Responsibilities table to capture these activities, when they will be performed, and who will responsible.

| ID  | Team                               | Phase / Role       | Tasks                                                                                                                                               | Project Phase (See Schedule) |
|-----|------------------------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
| 1   | VA OIT                             | Product Management | Manage project; Plan and schedule deployment; Determine when/if back-out is required; Coordinate with stakeholders.                                 |                              |
| 2   | VA PBM                             | Business Owners    | Elaborate requirements: Review/approve new features; Coordinate training for users; Coordinate with the team throughout the process                 |                              |
| 3   | VA OIT                             | Business Analyst   | Coordinate with business owners and technical team to create requirements and User Stories to be implemented                                        |                              |
| 4   | Booz Allen Hamilton                | System Architect   | Coordinate technical design of application features and application infrastructure; Plan and coordinate deployment; Coordinate back-out if required |                              |
| 5   | Booz Allen Hamilton, GovernmentCIO | System Admin       | Provide system infrastructure support through AWS cloud; Provide system monitoring; Deploy builds; Back-out installation if required                |                              |
| 6   | VA OIT, Booz Allen Hamilton        | Developers         | Develop/implement requirements; Coordinate design with System Architect; Resolve any reported defects                                               |                              |
| 7   | Booz Allen Hamilton, GovernmentCIO | SQA                | Test/verify acceptance criteria have been met for each User Story; Document defects and test resolution; Verify accessibility requirements are met  |                              |
| 8   | Booz Allen Hamilton                | Scrum Master       | Manage scrum team efforts                                                                                                                           |                              |
| 9   | GovernmentCIO                      | Release Manager    | Ensure Authority To Operate (ATO) and security documentation is in place; Load new users to Active Directory for access to AMPL                     |                              |
| 10  | Booz Allen Hamilton                | Technical Writer   | Coordinate with the team to review and update documentation for each release                                                                        |                              |

<span id="_Toc191980514" class="anchor"></span>Table 3: AMPL GUI Task Names and Start Dates

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial product deployment consisted of a three-phase rollout. The initial phase included partner test sites, followed by Phase 2 rollout to a single Veterans Integrated Service Network (VISN). The third phase included all remaining sites, deployed by region.

Now that AMPL has been released to Production, all new Build Releases will undergo three phases of deployment. The first phase includes SQA testing of features and bug fixes in lower environments with multiple builds deployed to these lower environments until a full Build Release is ready for deployment to Production. The second phase is Initial Operating Capability (IOC) testing/verification by partner test sites. The Build Release is deployed to an IOC environment, which is a Production release limited to the partner test sites. The third phase is deployment to the Production environment, which is an enterprise-wide release to all users.

This section provides the schedule and milestones for the deployment.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment and installation schedules are shown in the table below.

| Task Name                | Start Date | End Date |
|------------------------------|----------------|--------------|
| AMPL GUI IOC Production      | 07/30/2025     | 08/26/2025   |
| AMPL GUI National Deployment | 09/04/2025     | 09/04/2025   |

<span id="_Toc191980515" class="anchor"></span>Table 4: Site Preparation

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the AMPL GUI deployment. The AMPL GUI application will exist within the VA Enterprise Cloud for DEV/SQA, PREPROD, and Production environments. The AMPL GUI development team will maintain a local DEV to be used for sprint development and testing processes. All environments will maintain parity to reduce maintenance and development issues, at the same time providing foundations for a full-scale Continuous Integration and Continuous Delivery (CI/CD) environment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment topology is a mapping of the three tiers to a given number of physical nodes (machines). AMPL is being deployed to the Amazon Web Services (AWS) GOV cloud. The exact number and location of the cloud nodes necessary to support AMPL depends on an anticipated client load defined by the VA. The deployment nodes shown in Figure 1 illustrate the nominal physical topology of the AMPL deployment architecture.

<span id="_Toc140492253" class="anchor"></span>Figure 1: AMPL Deployment

![](ampl-deployment-installation-back-out-and-rollback-guide/002.png)

In Figure 1, the overall system deployment model is illustrated. Shown is the internal make-up of AMPL system and the associated external dependencies. The deployment architecture seeks to maintain symmetry with respect to the function and configurations of the individual nodes.

Each processing node of AMPL two-core systems components includes:

- Apache – The open-source Apache web server runs on each node. It serves the AMPL web application static content and acts as a proxy for the REST services of the AMPL application programming interface (API).
- Spring Boot – The open-source Spring Boot framework provides the structure for the REST endpoints of the AMPL API.

As currently implemented, AMPL does not persist any application data and, as a result, there is no database. All application data is accessed from VDIF FHIR services and VDIF VistA REST services. The Preference-Service saves and retrieves JSON files located in AWS S3 storage to enable persistence of user preferences for the application.

#### Elastic Container Service (ECS)

ECS is a set of platform-as-a-service products that use operating system (OS) level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries, and configuration files; they can communicate with each other through well-defined channels. Containers allow a developer to package up an application with all the needed parts, such as libraries and other dependencies, and ship it all out as one package. ECS is used to deploy the AMPL GUI application to the production environment as required by Ops.

<span id="_Toc140492254" class="anchor"></span>Figure 2: AMPL Deployment on ECS

![](ampl-deployment-installation-back-out-and-rollback-guide/003.png)

#### Presentation Tier

The Presentation tier of the AMPL system is composed of an Angular 17.xframework (JavaScript) web application. The application is deployed as static content on the Apache web server located on each production node.

#### Service Tier

The Service Tier of the AMPL system is comprised of a set of REST services developed under the Spring Boot framework. The Services are implemented as Java 2 Enterprise Edition (J2EE) Servlets and are executed in a Tomcat Servlet container.

#### Data Tier

The Data Tier of the AMPL system is external to the application’s boundary. The data visualized by the AMPL application is obtained from the Veterans Data Integration & Federation (VDIF) service via HL7 FHIR compliant REST services and VDIF custom services. The authoritative source for all the enterprise federated data is VistA.

The Preference-Service within AMPL utilizes the AWS S3 storage to persist user preferences using JSON files.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List the sites at which deployment is planned, including pilot and IOC sites, according to the schedule.

The initial deployment of AMPL GUI will be to Initial Operating Capability (IOC) partner test sites for user verification of functionality. Once testing is completed and AMPL GUI is approved for national release, AMPL GUI will be deployed nationally.

AMPL GUI will be tested at the following IOC sites:

1.  Shreveport, Louisiana
2.  West Palm Beach VA Medical Center (VAMC)- West Palm Beach, Florida
3.  Eastern Colorado Health Care System- (HCS) Denver, Colorado
4.  Coatesville, Pennsylvania
5.  Charleston, South Carolina
6.  Chillicothe, Ohio
7.  Honolulu, Hawaii

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

| Site / Other    | Problem / Change Needed                                          | Features to Adapt / Modify to New Product                             | Actions / Steps                                                                  | Owner                  |
|-----------------|------------------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------------------|------------------------|
| Production Site | Identify any new users that require access                       | Individuals requiring access should submit a SNOW ticket              | SNOW ticket created assigned to ‘SPM.Health.PCS.Sub_1. AMPL Engineering’” group. | Site ADPAC             |
| AMPL Team       | Provide access to Active Directory (AD) group for eligible users | End user will be entered into the AD group and granted access to AMPL | SNOW ticket resolved                                                             | Implementation Manager |

<span id="_Toc191980516" class="anchor"></span>Table 5: Facility-Specific Features

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use this section to describe hardware, software, facilities, and documentation, and any other resources, other than personnel, required for the deployment and installation.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists facility-specific features required for deployment.

| Site                      | Space / Room | Features Needed                                                | Other |
|---------------------------|--------------|----------------------------------------------------------------|-------|
| Amazon Web Services (AWS) | N/A          | Servers and infrastructure to host the Production installation |       |

<span id="_Toc191980517" class="anchor"></span>Table 6: Hardware Specifications

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes hardware specifications required at each site prior to deployment.

| Required Hardware                                                                                                              | Model | Version | Configuration     | Manufacturer      | Other |
|--------------------------------------------------------------------------------------------------------------------------------|-------|---------|-------------------|-------------------|-------|
| AMPL is hosted on AWS. AWS is responsible for procuring and configuring the required hardware to provide the hosting platform. | N/A   | N/A     | Determined by AWS | Determined by AWS |       |

<span id="_Toc191980518" class="anchor"></span>Table 7: Software Specifications

| Environment         | Server Count | Availability Zones | Server Type           | vCPU/MEM | Storage |
|---------------------|--------------|--------------------|-----------------------|----------|---------|
| Production          | 5            | 2                  | AMZLNX2 on m5a.xlarge | 4/16GB   | 100GB   |
| PREPROD             | 3            | 2                  | AMZLNX2 on m5a.xlarge | 4/16GB   | 100GB   |
| Development/SQA/UAT | 3            | 2                  | AMZLNX2 on m5a.xlarge | 4/16GB   | 100GB   |
| IOC                 | 3            | 2                  | AMZ FARGATE           | 4/16GB   | 100GB   |

Please see <u>Table 2: Roles and Responsibilities</u> for details about who is responsible for preparing the site to meet these hardware specifications.

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes software specifications required at each site prior to deployment.

| Required Software                     | Make | Version | Configuration | Manufacturer | Other |
|---------------------------------------|------|---------|---------------|--------------|-------|
| No site-specific software is required |      |         |               |              |       |

| Technology                      | Approval Status                                             | Reference                                                                             |
|---------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------|
| AWS Simple Storage Service (S3) | FedRAMP Approved                                            | [AWS S3](https://aws.amazon.com/compliance/services-in-scope/)                        |
| AWS Elastic Compute (EC2)       | FedRAMP Approved                                            | [AWS EC2](https://aws.amazon.com/compliance/services-in-scope/)                       |
| AWS CloudWatch                  | Under Third Party Assessment Organization (3PAO) Assessment | [AWS CloudWatch](https://aws.amazon.com/compliance/services-in-scope/)                |
| AWS Elastic Load Balancer       | FedRAMP Approved                                            | [AWS Elastic Load Balancer](https://aws.amazon.com/compliance/services-in-scope/)     |
| AWS Elastic Container Service   | FedRAMP Approved                                            | [AWS Elastic Container Service](https://aws.amazon.com/compliance/services-in-scope/) |
| Amazon Corretto Java 17.x       | TRM Approved                                                | [Amazon Corretto](https://trm.oit.va.gov/ToolPage.aspx?tid=14149)                     |
| Angular Development Tool 17.x   | TRM Approved                                                | [Angular Development Tool](https://angular.io/guide/rx-library)                       |
| Spring Boot 3.2.x               | TRM Approved                                                | [Spring Boot](https://trm.oit.va.gov/ToolPage.aspx?tid=8508)                          |

Please see <u>Table 2: Roles and Responsibilities</u> for details about who is responsible for preparing the site to meet these software specifications.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notification of scheduled maintenance periods that require the service to be offline or that may degrade system performance will be disseminated to the business user community a minimum of forty-eight (48) hours prior to the scheduled event.

Notification to VA users for unscheduled system outages or other events that impact the response time will be distributed within thirty (30) minutes of the occurrence.

Notification will be distributed to VA users regarding technical help desk support for obtaining assistance with receiving and processing.

Notification will be distributed to Software Product Management, Health, Patient Care Services sub-product line 1 team SPM.Health.PCS.Sub_1 and Business Owner, Pharmacy Benefits Management (PBM) for scheduled and unscheduled maintenance.

#### Deployment / Installation / Back-Out Checklist

The AMPL application is installed using ECS and has no database associated with the application. Rolling back to a previous installation is accomplished by deployment of the previous build/ECS. There is no need for a Rollback process.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- AMPL GUI is wholly dependent on VDIF FHIR and VistA REST services for access to all data utilized by the application. If there are service interruptions with these services, AMPL GUI will fail to operate.
- AMPL GUI is dependent on IAM SSOi/OAuth services for all authentication and authorization. If these services are unavailable, users will be unable to access the system.
- The most significant component of the system is the AMPL GUI web application. The AMPL Single Page Application (SPA) was developed using the Angular framework (currently Version 17.x).
- As a SPA the AMPL GUI web application executes entirely on the user’s workstation in a web browser and interacts with the AMPL REST API. Angular uses a language called Typescript, which is an extension of JavaScript.

### AMPL GUI Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMPL GUI application ECS images include the graphic user interface, and APIs required to retrieve data from VDIF, interact with IAM SSOi, and CCOW.

The user’s workstations require CCOW to be installed in order to utilize the CCOW functionality in AMPL GUI.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Install AWS ECS Instance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow VA Enterprise Cloud (VAEC) approved practices to install and choose the Amazon Machine Images (AMI) to be used for the installation. The VAEC AMI for ECS includes the ECS software and all that is needed to use as an AWS ECS instance.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no additional software to install when using the VAEC ECS instance AMI.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As currently implemented, AMPL GUI does not persist any application data and as a result there is no database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Create AWS ECS Cluster

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An Amazon ECS cluster is a logical grouping of tasks or services.

To create an AWS ECS cluster using the classic console, follow these steps:

1.  Open the Amazon ECS console at <https://console.aws.amazon.com/ecs/>.
2.  From the navigation bar, select the Region to use.
3.  In the navigation pane, choose Clusters.
4.  On the Clusters page, choose Create Cluster.
5.  For Select cluster compatibility, choose one of the following options and then choose Next Step:
    - Networking only – This cluster template creates an empty cluster. Optionally, you can create a new VPC to use. This cluster template is typically used for workloads hosted on either AWS Fargate or external instances (ECS Anywhere).

> The FARGATE and FARGATE_SPOT capacity providers will be automatically associated with the cluster. For more information, see [AWS Fargate capacity providers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fargate-capacity-providers.html).

- EC2 Linux + Networking – This cluster template is used to create a cluster of Amazon EC2 instances on which to run Linux-based containers. An Auto Scaling group is created for the Amazon EC2 instances.
- EC2 Windows + Networking – This cluster template is used to create a cluster of Amazon EC2 instances on which to run Windows-based containers. An Auto Scaling group is created for the Amazon EC2 instances. For more information, see [Amazon EC2 Windows containers](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_Windows.html).

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to the AMPL GUI application.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers will need to have elevated privileges to the appropriate servers granted through the Electronic Permission Access System (EPAS). The installers will need to have knowledge of Apache, ECS, GIT and will require elevated access to the server.

Access to the following groups is required:

- vaecunixc_aws_amp_nprod
- vaecunixc_aws_amp_prod
- cldunixs_amp_user_dev
- cldunixs_amp_admin_test
- cldunixs_amp_admin_prod
- cldunixs_amp_admin_prep
- cldunixs_amp_admin_os_test
- cldunixs_amp_admin_os_prod
- cldunixs_amp_admin_os_dev

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The systems on which the ECS Swarm runs is provided by the AWS Cloud VA agency [VA Enterprise Cloud](https://dvagov.sharepoint.com/sites/OITECSO/SitePages/VA-Enterprise-Cloud-VAEC.aspx) (VAEC). The VAEC designs the Amazon Linux ECS AMI needed to build the AMPL GUI systems.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the Amazon Web Service (AWS) ECS cluster is running follow these steps:

1.  Log into the AWS Web console.
2.  Navigate to the ECS page.
3.  Locate the production cluster.
4.  Verify that the services ([Production-API-Service](https://console.amazonaws-us-gov.com/ecs/home?region=us-gov-west-1#/clusters/Production/services/Production-API-Service/details), Production -Web-Service) and tasks (Production-API, Production-Web) are running.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to the AMPL GUI application.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable to the AMPL GUI application.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections describe the back-out procedures.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No special back-out strategy considerations are required for AMPL GUI.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special back-out considerations for AMPL GUI.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no provisions for Load Testing in the production environment. Load testing was conducted within the Pre-Production environment.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) ensures the GUI does not interfere with normal system operations. UAT data is available in the VA AMPL GUI Product Repository on [GitHub](https://github.ec.va.gov/EPMO/ampl-gui-product/tree/master/test).

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI is a read-only application. It does not store or modify any data. Therefore, there is no impact on data integrity from back-out of any specific version. The Back-Out criteria are entirely dependent on the severity of defect or another factor precipitating the back-out request.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Back-Out Risks, see [Section 5.3: Back-Out Criteria](#back-out-criteria).

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out order would come from the Application Coordinator (product support), Development Team, and Portfolio Director. This should be done in consultation with the development team and project stakeholders.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMPL GUI application running in an AWS ECS can easily be backed out by stopping the current task, removing it, and deploying the previous version of the build.

- Log into the AWS Web console
- Navigate to the ECS page
- Locate the production cluster
- Change task definition revision number to a previous version
- Click Update to update the service and re-deploy

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the back-out is performed, the general functionality of the application can be verified by opening the application, confirming the data is loading, and that patient data can be retrieved.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No specific rollback considerations are required.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a severe issue is reported for AMPL, the project/sustainment team will determine if the issue can be addressed through resolution of the defect in a subsequent build or if a roll-back to a previous version/build is required.

The criterion for rolling back is if the project is canceled, the requested changes implemented by AMPL GUI are no longer desired by VA OIT, or the release produces catastrophic problems.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Rollback Risks, see [Section 5.3: Back-Out Criteria](#back-out-criteria).

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback order would come from the Application Coordinator (product support), Development Team, and Portfolio Director. This is done in consultation with the development team and project stakeholders.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Rollback Procedure is the same as the Back-Out Procedure. [See Section 5.8: Back-Out Procedure](#_Back-Out_Procedure).

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI is a read-only application and there is no data verification after Rollback.

# Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym | Definition                                                                |
|---------|---------------------------------------------------------------------------|
| 3PAO    | Third Party Assessment Organization                                       |
| AD      | Active Directory                                                          |
| AMI     | Amazon Machine Images                                                     |
| AMPL    | Advanced Medication Platform                                              |
| API     | Application Programming Interface                                         |
| AWS     | Amazon Web Service                                                        |
| CCOW    | Clinical Context Object Workgroup                                         |
| CD2     | Critical Decision Point 2                                                 |
| CI/CD   | Continuous Integration and Continuous Delivery                            |
| COTS    | Commercial off-the-shelf                                                  |
| DIBRG   | Deployment, Installation, Back-out, Roll Back                             |
| EC2     | Elastic Compute Cloud                                                     |
| ECS     | Elastic Container Service                                                 |
| EMPD    | Enterprise Project Management Division                                    |
| EP      | Enterprise Platform                                                       |
| EPMO    | Office of Information and Technology Enterprise Program Management Office |
| ETL     | Extract, Transform, and Load                                              |
| FHIR    | Fast Healthcare Interoperability Resources                                |
| GUI     | Graphical User Interface                                                  |
| HIPAA   | Health Insurance Portability and Accountability Act                       |
| HL7     | Health Level 7                                                            |
| HPS     | Health Product Support                                                    |
| IAM     | Identity and Access Management                                            |
| ID      | Identifier                                                                |
| IOC     | Initial Operating Capability                                              |
| IT      | Information Technology                                                    |
| J2EE    | Java 2 Enterprise Edition                                                 |
| MPI     | Master Patient Index                                                      |
| OIT     | Office of Information & Technology                                        |
| OS      | Operating System                                                          |
| PBM     | Pharmacy Benefits Management                                              |
| S3      | Simple Storage Service                                                    |
| SACC    | Standards & Conventions Committee                                         |
| S       | Service Now                                                               |
| SQA     | Software Quality Assurance                                                |
| SSOi    | Single Sign-On Internal                                                   |
| TRM     | Technical Reference Model                                                 |
| UAT     | User Acceptance Testing                                                   |
| VAEC    | VA Enterprise Cloud                                                       |
| VAMC    | VA Medical Center                                                         |
| VDIF    | Veterans Data Integration & Federation                                    |
| VHA     | Veteran Health Administration                                             |
| VIP     | Veteran-focused Integrated Process                                        |
| VistA   | Veteran Health Information Systems and Technology Architecture            |
| WASA    | Web Application Security Audit                                            |
