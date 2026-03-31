---
title: Enterprise Precision Scanning and Indexing (EPSI) Deployment, Installation, Back-Out, and Rollback Guide v1.3.0
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: 
app_code: EPSI
app_name: Enterprise Precision Scanning and Indexing
section: CLI
app_status: active
pkg_ns: EPSI
patch_ver: 1.3.0
patch_id: EPSI*1.3.0
group_key: "EPSI:EPSI:1.3.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - epsi
  - installation
  - back
  - deployment
  - rollback
  - span
  - procedure
  - site
page_count: 0
word_count: 2438
section_count: 24
table_count: 10
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2023
revision_count: 3
revision_newest: 4/7/2023
revision_oldest: 8/10/2022
docx_url: "https://www.va.gov/vdl/documents/Clinical/Enterprise_Precision_Scanning_and_Indexing_(EPSI)/epsi_dibrg_1_3_0.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Enterprise_Precision_Scanning_and_Indexing_(EPSI)/epsi_dibrg_1_3_0.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=431"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Enterprise Precision Scanning and Indexing (EPSI)

  Software Version 1.3.0

  Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)
---

![](enterprise-precision-scanning-and-indexing-epsi-deployment-installation-back-out/001.png)

April 2023

Office of Information and Technology (OIT)

Revision History

| Date  | Version | Description                                                                                                   | Author |
|-----------|-------------|-------------------------------------------------------------------------------------------------------------------|------------|
| 4/7/2023  | 1.2         | Added Hyperscience. Updated TRM Status Information. Removed VIX/CVIX and replaced with current VistaLink process. | VetsEZ     |
| 1/27/2023 | 1.1         | Added table to section 3.3.2. Updated section 3.2.2.                                                              | VetsEZ     |
| 8/10/2022 | 1.0         | Initial release                                                                                                   | VetsEZ     |

<span id="_Toc123714103" class="anchor"></span>Table 1: System Dependencies

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software and should be structured appropriately to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point \#2 (CD \#2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

List of Figures

[Figure 1: EPSI Deployment Topology [8](#_Toc123714111)](#_Toc123714111)

[Figure 2: Hardware Resources [9](#_Ref111028957)](#_Ref111028957)

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
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Authority for Back-Out](#authority-for-back-out)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
- [Risk and Mitigation Plan](#risk-and-mitigation-plan)
This document describes how to deploy and install the Enterprise Precision Scanning and Indexing (EPSI) product, as well as how to back-out the product and roll back to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed Commercial off the Shelf (COTS) product is being installed, the vendor provided user and installation guides may be used, but the back-out recovery strategy still needs to be included in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the EPSI product will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Dependency                                                      | Type    | Dependency Type  | EPSI Use                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------|---------|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Corporate Data Warehouse (CDW)                                  | Service | Data/Information | Internal data service to interact and query CDW cached data. Data will be a scheduled task to load CDW into the EPSI environment. CDW data will reside within EPSI for lookup and reference within the EPSI decision logic. The data will have its own designated datastore due to it being relational data. |
| Hyperscience                                                    | Service | Data/Information | Internal data service to provide optical character recognition (OCR) functions with natural language processing (NLP) features to automate and validate data entry.                                                                                                                                          |
| Identity and Access Management (IAM) Secure Token Service (STS) | Service | Authentication   | Internal service that is used to obtain security tokens required to log in to various other systems like VistA using a Simple Object Access Protocol (SOAP) interface.                                                                                                                                       |
| Identity and Access Management (IAM) Single Sign-On (SSOi)      | Service | Authentication   | Internal service that authenticates EPSI users using various methods, including Personal Identity Verification (PIV) card and username/ password via a WebAgent plugin that is installed on the EPSI proxy server.                                                                                           |
| VistA/VistA Link                                                | Service | Data/Information | PII/PHI and consult data is supplied to EPSI through a VistA Link connection to VistA. This data is used to populate the upload call and successfully associate a document with a patient/consult and successfully add that document to the patient’s EHR.                                                   |

<span id="_Toc123714104" class="anchor"></span>Table 2: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPSI project team, software, and test servers will adhere to the following directives, policies, procedures, standards, and guidelines:

- Department of Veterans Affairs (VA) DevOps Process.
- Section 508 Information Technology (IT) accessibility standards governed under 29 U.S.C 794d.
- Health Insurance Portability and Accountability Act (HIPAA).
- VA Directive 6508 – Privacy Impact Assessments.
- VA Directive 6500 – Information Security Program.
- One-VA Technical Reference Model (TRM).
- VA Standards and Conventions Committee (SACC) Codes Standards and Conventions.
- The EPSI app will pass any Web Application Security Assessment (WASA) scans.
- The EPSI app will not have any Critical or High issues identified by a Fortify scan.
- Nessus scans will be performed monthly by VA Cyber Security Operations Center (CSOC).
  - Critical findings will be remediated within 30 days.
  - High findings will be remediated within 60 days.
  - Medium findings will be remediated within 90 days.
  - Low findings will be remediated at the discretion of the System Owner.
- Open security findings are tracked within eMASS as POA&M items.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team               | Phase/Role                                                                          | Tasks                                                                                                                                                                         |
|-----|--------------------|-------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Vendor Development | Review/Update DIBRG/POM                                                             | Review and update the Deployment, Installation, Back-Out, and Rollback Guide (DIBRG) and Product Operations Manual (POM) documents as required in preparation for deployment. |
| 1   | Vendor Development | Deployment in Local Dev                                                             | Plan and schedule deployment in local environment.                                                                                                                            |
| 2   | Vendor Development | Deployment in Software Quality Assurance (SQA)/ User Acceptance Testing (UAT) in VA | Determine and document the roles and responsibilities of those involved in the deployment.                                                                                    |
| 3   | Vendor Development | Deployment in Production                                                            | Test for operational readiness.                                                                                                                                               |
| 4   | Vendor Development | Installation                                                                        | Plan and schedule installation.                                                                                                                                               |
| 6   | VA                 | Installation                                                                        | Validate through facility point of contact (POC) to ensure that IT equipment has been accepted using asset inventory processes.                                               |
| 8   | Vendor Development | Back-out                                                                            | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).                                                          |
| 9   | Vendor Development | Post Deployment                                                                     | Hardware, software, and system support.                                                                                                                                       |

<span id="_Toc83390785" class="anchor"></span>Table 3: EPSI Task Names and Start Dates

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the schedule and milestones for the deployment. The deployment is planned as an iterative rollout.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section providers the project schedule and milestones for the initial version.

| Task Name                                                   | Start Date | End Date  |
|-------------------------------------------------------------|------------|-----------|
| Hand-off to SQA                                             | 8/1/2022   | 8/2/2022  |
| SQA Testing                                                 | 8/3/2022   | 8/5/2022  |
| Promote Code to Pre-Prod                                    | N/A        | N/A       |
| Initial Operating Capability (IOC) Testing (Selected Users) | 6/13/2022  | 6/17/2022 |
| IOC Testing (All Sites)                                     | 6/21/2022  | 7/5/2022  |
| IOC Re-Test with Limited Sites                              | 7/11/2022  | 7/14/2022 |
| Release to Prod                                             | 8/15/2022  | 9/12/2022 |

<span id="_Toc123714106" class="anchor"></span>Table 4: Site Preparation

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The figure below shows the deployment topology (targeted architecture) of the EPSI application.

<span id="_Toc123714111" class="anchor"></span>Figure 1: EPSI Deployment Topology

![](enterprise-precision-scanning-and-indexing-epsi-deployment-installation-back-out/002.png)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPSI has been deployed nationally to all sites.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table describes preparation required by the site prior to deployment.

| Site/Other | Problem/Change Needed        | Features to Adapt/Modify to New Product                          | Actions/Steps | Owner    |
|----------------|----------------------------------|----------------------------------------------------------------------|-------------------|--------------|
| Site           | Assign EPSI Site Administrators. | Approve access requests for Indexers, Nurses, and Quality Assurance. | Training          | Vendor staff |

<span id="_Toc83390786" class="anchor"></span>Table 5: Hardware Specifications

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes hardware, software, facilities, documentation, and any other resources— other than personnel—required for deployment and installation.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPSI is in the VA Enterprise Cloud (VAEC) enclave. There are four VAEC cloud environments maintained (see Figure 2). All environments have a common hardware parity with the hardware specifications listed below. All application software and microservice configuration (Kubernetes) are executed on the hardware.

Please refer to Section 2, Roles and Responsibilities, for details about who is responsible for preparing the site to meet these hardware specifications.

<span id="_Ref111028957" class="anchor"></span>Figure 2: Hardware Resources

![](enterprise-precision-scanning-and-indexing-epsi-deployment-installation-back-out/003.png)

| Required Hardware         | Model | Version      | Configuration | Manufacturer | Other       |
|---------------------------|-------|--------------|---------------|--------------|-------------|
| Amazon Web Services (AWS) | M4-M5 | Large-XLarge | Virtual       | Virtual      | All servers |

<span id="_Toc123714108" class="anchor"></span>Table 6: Technology Components

| Technology Component                                            | Location               | Usage                                                                                   |
|-----------------------------------------------------------------|------------------------|-----------------------------------------------------------------------------------------|
| EPSI Production (Production 1) – VA Cloud                       | VA Cloud environment   | To serve the EPSI application within the VA Production environment.                     |
| EPSI Stage (Verification/Test) – VA Cloud                       | VA Cloud environment   | To test the EPSI application within a VA preprod and/or verification environment.       |
| EPSI DEV/SQA/DEMO (Verification/Test) – VA Cloud                | VA Cloud environment   | To test the EPSI application within a VA test and/or verification environment.          |
| EPSI Development (Development) – Local Development Environments | Developer workstations | To develop and test the EPSI application before transition to the VA cloud environment. |

<span id="_Toc132181865" class="anchor"></span>Table 7: EPSI Technology

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following tables describe software specifications required at each site prior to deployment.

| Technology                      | Approval Status           | Reference                                                                                                                        |
|-------------------------------------|---------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| Apache Tomcat 8.5.x                 | TRM Approved – CY 2023 Q2 | [<u>https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=5451#</u>](https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=5451) |
| AWS CloudWatch                      | Under 3PAO Assessment     | https://aws.amazon.com/compliance/services-in-scope/                                                                             |
| AWS Elastic Compute (EC2)           | FedRAMP Approved          | https://aws.amazon.com/compliance/services-in-scope/                                                                             |
| AWS Elastic LoadBalancer            | FedRAMP Approved          | https://aws.amazon.com/compliance/services-in-scope/                                                                             |
| AWS RDS Postgres                    | FedRAMP Approved          | https://aws.amazon.com/compliance/services-in-scope/                                                                             |
| AWS Simple Storage Service (S3)     | FedRAMP Approved          | <https://aws.amazon.com/compliance/services-in-scope/>                                                                           |
| Datadog                             | FedRAMP Approved          | <https://www.datadoghq.com/blog/datadog-fedramp-moderate-impact-authorization/>                                                  |
| Helm 3.8.x                          | TRM Approved – CY 2023 Q2 | [https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=14767#](https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=14767)      |
| Hyperscience                        | TRM Approved – CY 2023 Q2 | <https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=14753>                                                                    |
| Java 11+                            | TRM Approved – CY 2023 Q2 | <https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=14884>                                                                    |
| Kubernetes 1.21.x                   | TRM Approved – CY 2023 Q2 | [https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=11815#](https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=11815)      |
| ReactJS 17.x                        | TRM Divest – CY 2023 Q2   | <https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=10254>                                                                    |
| Red Hat Enterprise Linux (RHEL) 8.x | TRM Approved – CY 2023 Q2 | <https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=6367>                                                                     |
| SpringBoot 2.7.x                    | TRM Approved – CY 2022 Q2 | <https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=8508>                                                                     |
| VistA                               | TRM Approved              | N/A                                                                                                                              |
| WebLogic 14c.1.x                    | TRM Approved – CY 2023 Q2 | [https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=7#](https://www.oit.va.gov/Services/TRM/ToolPage.aspx?tid=7)              |

<span id="_Toc123714109" class="anchor"></span>Table 8: Software Specifications

| Required Software                | Make                    | Version |
|----------------------------------|-------------------------|---------|
| Apache                           | Apache Software         | 2.4.X   |
| Kubernetes                       | Red Hat                 | 1.21.X  |
| Elastic Kubernetes Service (EKS) | AWS                     | eks.4   |
| Docker                           | Docker, Inc             | 19.3.X  |
| Red Hat                          | Enterprise Linux Server | 7.X     |

<span id="_Toc83390788" class="anchor"></span>Table 9: Deployment/Installation/Back-Out Checklist

Please see Section 2, Roles and Responsibilities, for details about who is responsible for preparing the site to meet these software specifications.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notification of scheduled maintenance periods that require the service to be offline or that may degrade system performance will be disseminated to the business user community a minimum of 48 hours prior to the scheduled event. The Product Owner and Product Manager will be notified via email.

Notification will be distributed to VA users within 30 minutes of occurrence for unscheduled system outages or other events that impact the response time.

Notification will be distributed to VA users as soon as possible for unexpected system outages or other events that impact the response time.

Notification will be distributed to VA users regarding technical help desk support for obtaining assistance with receiving and processing.

#### Deployment/Installation/Back-Out Checklist

The table below outlines the coordination effort and documents for the day/time/individual when each activity (deploy, install, back-out) is completed for EPSI.

| Activity | Day                                  | Time                              | Individual Who Completed Task          |
|----------|--------------------------------------|-----------------------------------|----------------------------------------|
| Deploy   | Dependent on current build timeline. | When approved by VA stakeholders. | Community Care DevSecOps (CCDSO) staff |
| Install  | Dependent on current build timeline. | When approved by VA stakeholders. | CCDSO staff                            |
| Back-Out | Dependent on current build timeline. | When approved by VA stakeholders. | CCDSO staff                            |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPSI is a containerized application that runs on Kubernetes. Components are deployed using Helm. The Kubernetes platform used for EPSI is Elastic Kubernetes Service (EKS) which is a cloud-managed Kubernetes implementation that greatly simplifies the amount of work needed to maintain the system. Kubernetes deployments are broken into two parts: the Control Plane and the Worker Nodes. EKS manages the Control Plane and provides redundancy and fault tolerance by running it in multiple Availability Zones (AZ). The Worker Nodes are run on AWS Elastic Compute Cloud (EC2) instances built using an Amazon Machine Image (AMI) provided by VAEC.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPSI platform is installed using a set of CloudFormation templates. The templates are broken into the following categories:

- EKS Control Plane
- EKS Nodes
- WebServer Load Balancer
- WebServer Nodes
- SQS Queue
- Database

  The templates, scripts, and instructions for setting up the EPSI Platform can be found on GitHub at <https://github.com/department-of-veterans-affairs/epsi-devops>. The repository contains various wikis to guide you through the process of setting up the platform on AWS.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to EPSI project.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions for installing the EPSI database are covered in Section 4.2, Platform Installation and Preparation.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to EPSI.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to EPSI.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install the EPSI Platform and Application, you will need the following:

- Access to the VAEC-epsi account in the VAEC WebGovCloud—your user account should have privileges to run CloudFormation scripts, read from S3 buckets, and provision various compute services (e.g., EKS, EC2, RDS). The Active Directory Federation Services (ADFS)-project-administrator role is typically assigned to users and will have these privileges.
- Access to the EPSI GitHub code repositories with permissions to run GitHub Actions.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install and upgrade the EPSI application with the following steps. These instructions assume that a GitHub Release exists for the version of the EPSI Application to be installed. The release should document the changes that were made to the application.

1.  Navigate your web browser to <https://github.com/department-of-veterans-affairs/epsi>. Log in if necessary.
2.  Select the Actions tab.
3.  Select Deploy EPSI from the left of workflows on the left of the page.
4.  Select the Run Workflow button, which will open a popup window where you can select the branch from which to run the workflow and the environment to which you wish to deploy EPSI.
    1.  For the Use workflow from field, always select a tag. GitHub environments are set up to only allow tagged releases to be deployed.
    2.  Select the environment to which you which to deploy using the Environment input field.
    3.  Select the Run Workflow button.

Deployments to production require approval from a user with Admin permissions in the EPSI repository to proceed with the deployment.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Open your web browser.
2.  Navigate to <https://epsi.va.gov>.
3.  Log in with your PIV card.
4.  Based on user role, validate the application information is correct.
5.  Select the person icon on the top right portion of the screen.
6.  Verify the provisioned sites are visible as expected.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to EPSI.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable to EPSI.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the back-out procedure for EPSI. Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings.

The EPSI system will provide data protection measures such as back-up intervals and redundancy that are consistent with systems categorized as mission critical (12-hour restoration, 2-hour recovery point objective).

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on authority provided by our Business Sponsor and VA Office of Information and Technology (OIT) IT Program Manager, EPSI can be backed out with their approval.

EPSI can back-out any service within the Kubernetes cluster which includes all application components.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database (DB) snapshots are taken every evening. To restore the EPSI DB instance from a DB snapshot:

1.  Sign into the Amazon Web Services (AWS) Management Console and open the (Relational Database Service)RDS console.
2.  In the navigation pane, choose Snapshots.
3.  Choose the DB snapshot that you want to restore from.
4.  For Actions, choose Restore Snapshot. The Restore DB Instance page displays.
5.  For DB Instance Identifier under Settings, enter the name that you want to use for the restored Database instance. If you are restoring from a DB instance that you deleted after you made the Database snapshot, you can use the name of that DB instance.
6.  Choose Restore DB Instance.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

EPSI can roll back the EPSI AWS RDS SQL Server instance.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback criteria are not applicable.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is minimal risk associated to these rollback procedures. It is common practice to roll back Kubernetes microservices and is part of the design of the technology. All EPSI application code and infrastructure are maintained as code saved in source control in VA GitHub, so there is minimal potential loss of functionality when an issue arises. Finally, AWS provides highly resilient backup processes for all the EPSI AWS RDS databases.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Based on authority provided by our Business Sponsor and VA OIT IT Program Manager, EPSI can be backed out with their approval.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPSI system will provide data protection measures, such as back-up intervals and redundancy that is consistent with systems categorized as mission critical (12-hour restoration, 2-hour recovery point objective) for the application and infrastructure. The rollback instructions are the same as back-out for the application.

# Risk and Mitigation Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EPSI project team maintains a Program Risk Registry. Refer to the Program Risk Registry for all risks and mitigation plans for the entire EPSI project.