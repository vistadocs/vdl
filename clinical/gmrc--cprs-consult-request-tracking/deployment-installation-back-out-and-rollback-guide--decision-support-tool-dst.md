---
consolidated_title: "decision support tool (dst) deployment, installation, back-out, and rollback guide"
app_code: GMRC
doc_type: DIBR
master_source: "Decision Support Tool (DST) Deployment, Installation, Back-Out, and Rollback Guide"
master_pub_date: April 2020
consolidated_from: 2 versions
prior_versions:
  - "Decision Support Tool (DST) Deployment, Installation, Back-Out, and Rollback Guide v1.1.1314"
---

**Care Coordination Decision Support Tool (DST)**

**Build 20**

**Deployment, Installation, Back-Out, and Rollback Guide (DIBR)**

<!-- image -->

**April 2020 Department of Veterans Affairs**

**Office of Information and Technology (OIT)**

**Revision History**

| **Date**   |   **Version** | **Description**                                                   | **Author**   |
|------------|---------------|-------------------------------------------------------------------|--------------|
| 04/13/2020 |           1.8 | Updated for Build 20 v1.1.972                                     | Ablevets     |
| 03/03/2020 |           1.7 | Updated for Build 20                                              | AbleVets     |
| 02/05/2020 |           1.6 | Updated for Build 19                                              | AbleVets     |
| 11/21/2019 |           1.5 | Updated for Build 18                                              | AbleVets     |
| 10/03/2019 |           1.4 | Updated for Build 18                                              | AbleVets     |
| 09/09/2019 |           1.3 | Updated for Build 18                                              | AbleVets     |
| 08/13/2019 |           1.2 | Updated for v1.1                                                  | AbleVets     |
| 08/06/2019 |           1.1 | Updated for v1.0.12                                               | AbleVets     |
| 07/30/2019 |           1   | Updated for v1.0.11                                               | AbleVets     |
| 07/22/2019 |           0.9 | Updated for v1.0.10                                               | AbleVets     |
| 07/16/2019 |           0.8 | Updated for v1.0.09                                               | AbleVets     |
| 07/08/2019 |           0.7 | Updated for v1.0.08                                               | AbleVets     |
| 06/12/2019 |           0.6 | Updated for v1.0.05                                               | AbleVets     |
| 05/30/2019 |           0.5 | Updated for v1.0.04                                               | AbleVets     |
| 05/15/2019 |           0.4 | Defect remediation                                                | AbleVets     |
| 04/26/2019 |           0.3 | Defect remediation                                                | AbleVets     |
| 04/24/2019 |           0.2 | Added TLS installation specific to GMRC*3.0*125 Patch Information | AbleVets     |
| 04/11/2019 |           0.1 | Initial Draft                                                     | AbleVets     |

**Artifact Rationale**

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point #2 (CD #2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

**Table of Contents**

1. Introduction	1
    - 1.1. Purpose	1
    - 1.2. Dependencies	1
    - 1.3. Constraints	2
2. Roles and Responsibilities	3
3. Deployment	3
    - 3.1. Timeline	4
    - 3.2. Site Readiness Assessment	4
        - 3.2.1. Deployment Topology (Targeted Architecture)	4
        - 3.2.2. Site Information (Locations, Deployment Recipients)	5
    - 3.3. Resources	5
        - 3.3.1. Hardware	5
        - 3.3.2. Software	7
        - 3.3.3. Communications	7
    - 3.4. Deployment/Installation/Back-Out Checklist	7
4. Installation	8
    - 4.1. Platform Installation and Preparation in Facility level	8
        - 4.1.1. Consult Toolbox	8
        - 4.1.2. VistA DST Patch to the GMRC Package at Each VistA Site	8
        - 4.1.3. DST Application	9
        - 4.1.4. Cerner PowerChart	9
    - 4.2. Download and Extract Files	9
    - 4.3. Database ETL Jobs	9
    - 4.4. Installation Scripts	10
    - 4.5. Cron Scripts	11
    - 4.6. Access Requirements and Skills Needed for the Installation	11
    - 4.7. Installation Procedure	11
    - 4.8. Installation Verification Procedure	11
    - 4.9. System Configuration	12
    - 4.10. Database Tuning	12
5. Back-Out Procedure	12
    - 5.1. Back-Out Procedure	12
    - 5.2. Authority for Back-Out	12
6. Rollback Procedure	12
    - 6.1. Rollback Considerations.	12
    - 6.2. Rollback Criteria	12
    - 6.3. Rollback Risks	13
    - 6.4. Authority for Rollback	13
    - 6.5. Rollback Procedure	13
7. Risk and Mitigation Plan	13

**List of Tables**

Table 1: DST Application Dependencies	1

Table 2: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities	3

Table 3: DST Task Names and Start Dates	4

Table 4: Hardware Specifications	6

Table 5: Software Specifications	7

Table 6: Deployment/Installation/Back-Out Checklist	7

Table 7: CDW ETL Jobs	10

Table 8: Cron Scripts	11

## Introduction

This document describes how to deploy and install the Community Care Decision Support Tool (DST) as well as how to back-out the product and rollback to a previous version or data set if applicable. This document is a companion to the project charter and management plan for this effort. This document details the criteria for determining if a back-out is necessary, the authority for making that decision, the order in which installed components will be backed out, the risks and criteria for a rollback, and authority for acceptance or rejection of the risks.

### Purpose

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the DST be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

### Dependencies

The DST Application is dependent on the following Systems/Applications/Services.

**Table 1: DST Application Dependencies**

| **Dependency**                            | **Type**   | **Dependency Type**   | **DST Use**                                                                                                                                                                                                                                                                                            |
|-------------------------------------------|------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Computerized Patient Record System (CPRS) | System     | System                | Consult data is supplied to DST. This data is used to initiate a DST decision for a given consult.                                                                                                                                                                                                     |
| Master Veteran Index (MVI)                | Service    | Data/Information      | Internal data service to access Master Patient Index (MPI)/MVI external data. Will contain all unique query logic to interact with the external service, along with external interface configuration setup (such as authentication).                                                                   |
| Corporate Data Warehouse (CDW)            | Service    | Data/Information      | Internal data service to interact and query CDW cached data. Data will be a scheduled task to load CDW into the DST environment. CDW data will reside within DST for lookup and reference within the DST decision logic. The data will have its own designated datastore due it being relational data. |

| **Dependency**                                 | **Type**   | **Dependency Type**   | **DST Use**                                                                                                                                                                                                              |
|------------------------------------------------|------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Enrollment System Redesign (E&E/ESR)           | Service    | Data/Information      | Internal data service to access Enrollment Service external data. Will contain all unique query logic to interact with the external service, along with external interface configuration setup (such as authentication). |
| Provider Profile Management System (PPMS)      | Service    | Data/Information      | Internal data service to access PPMS external data. Will contain all unique query logic to interact with the external service, along with external interface configuration setup (such as authentication).               |
| Lighthouse Application Program Interface (API) | Service    | Data/Information      | Internal data service to access facility data. Will contain all unique query logic to interact with the external service, along with external interface configuration setup (such as authentication).                    |
| Standardized Episodes of Care (SEOC)           | Service    | Data/Information      | Internal data service to access SEOC stored internal data. Will contain all unique query logic to interact with the datastore to query data, including configuration setup (such as authentication).                     |

### Constraints

The DST project team, software, and test servers will adhere to the following directives, policies, procedures, standards, and guidelines:

- Veteran-focused Integration Process (VIP).
- Section 508 Information Technology (IT) accessibility standards governed under 29

U.S.C 794d.

- Health Insurance Portability and Accountability Act (HIPAA).
- VA DIRECTIVE 6508 - Privacy Impact Assessments.
- VA Directive 6500 – Information Security Program.
- One-VA Technical Reference Model (TRM).
- VA Standards &amp; Conventions Committee (SACC) Codes Standards and Conventions.
- The DST will pass any Web Application Security Assessment (WASA) scans.
- The DST will not have any Critical or High issues identified by a Fortify scan.

## Roles and Responsibilities

Please refer to the following table for the deployment, installation, back-out, and rollback roles and responsibilities.

**Table 2: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities**

|   **ID** | **Team**             | **Phase / Role**                                                                                                    | **Tasks**                                                                                                                      |
|----------|----------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
|        1 | AbleVets Development | Deployment in Local Dev                                                                                             | Plan and schedule deployment in local environment                                                                              |
|        2 | AbleVets Development | Deployment in Software Quality Assurance (SQA)/User Acceptance Testing (UAT) in Department of Veterans Affairs (VA) | Determine and document the roles and responsibilities of those involved in the deployment.                                     |
|        3 | AbleVets Development | Deployment in Production                                                                                            | Test for operational readiness                                                                                                 |
|        4 | AbleVets Development | Installation                                                                                                        | Plan and schedule installation                                                                                                 |
|        6 | VA                   | Installation                                                                                                        | Validate through facility point of contact (POC) to ensure that IT equipment has been accepted using asset inventory processes |
|        8 | AbleVets Development | Back-out                                                                                                            | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)            |
|        9 | AbleVets Development | Post Deployment                                                                                                     | Hardware, Software and System Support                                                                                          |

## Deployment

The deployment is planned as an iterative rollout. The following swim lane provides the high- level overview of DST Release Process.

<!-- image -->

**Figure 1: Overview of the DST Release Process**

### Timeline

This section providers the project schedule and milestones for this version.

**Table 3: DST Task Names and Start Dates**

| **Task Name**            | **Start Date**                 | **End Date**                   |
|--------------------------|--------------------------------|--------------------------------|
| Hand-off to SQA          | 04/06/2020                     | 04/06/2020                     |
| SQA Testing              | 04/07/2020                     | 04/10/2020                     |
| Promote Code to Pre-Prod | No PreProd events for Build 20 | No PreProd events for Build 20 |
| Release to Prod          | 04/14/2020                     | 04/14/2020                     |

### Site Readiness Assessment

The DST application will exist within the VA Enterprise Cloud (VAEC) for DEV, PREPROD, DEMO (Sandbox), and Production environments. The DST development team will maintain a local DEV to be used for sprint development and testing processes.

#### Deployment Topology (Targeted Architecture)

The figure below shows the Deployment Topology (Targeted Architecture) of the DST application.

<!-- image -->

**Figure 2: Deployment Topology (Targeted Architecture)**

#### Site Information (Locations, Deployment Recipients)

The initial deployment of the DST web interface will be to Initial Operating Capability (IOC) sites so that users can verify the functionalities of DST. Once testing is completed and DST is approved for national release, DST will be deployed nationally.

DST will be deployed to the following IOC sites.

- redacted
### Resources

This section describes hardware, software, facilities, documentation, and any other resources, other than personnel, required for deployment and installation.

#### Hardware

DST is in the VAEC cloud enclave. There are three VAEC cloud environments maintained. All environments have a common hardware parity with the hardware specifications listed below. All application software and microservice configuration (Kubernetes) are executed on the hardware.

Please refer to Table 2 in the Roles and Responsibilities section of this document for details about who is responsible for preparing the site to meet these hardware specifications.

<!-- image -->

**Figure 3: Hardware Resources**

**Table 4: Hardware Specifications**

| **Required Hardware**   | **Model**   | **Version**   | **Configuration**   | **Manufacturer**   | **Other**   |
|-------------------------|-------------|---------------|---------------------|--------------------|-------------|
| AWS                     | M5          | XLarge        | Virtual             | Virtual            | All Servers |

| **Technology Component Production 1**   | **Location**         | **Usage**                                                          |
|-----------------------------------------|----------------------|--------------------------------------------------------------------|
| DST Production – VA Cloud               | VA Cloud environment | To serve the DST application within the VA Production environment. |

| **Technology Component Verification/Test**   | **Location**         | **Usage**                                                                     |
|----------------------------------------------|----------------------|-------------------------------------------------------------------------------|
| DST PreProd – VA Cloud                       | VA Cloud environment | To test the DST application within a VA test and/or verification environment. |

| **Technology Component Verification/Test**   | **Location**         | **Usage**                                                                     |
|----------------------------------------------|----------------------|-------------------------------------------------------------------------------|
| DST DEV/SQA/DEMO – VA  Cloud                 | VA Cloud environment | To test the DST application within a VA test and/or verification environment. |

| **Technology Component Development**   | **Location**               | **Usage**                                                                                     |
|----------------------------------------|----------------------------|-----------------------------------------------------------------------------------------------|
| DST Development – AbleVets Cloud       | AbleVets Cloud environment | To develop, test, and demo the DST application before transition to the VA cloud environment. |

#### Software

The following table describes software specifications required prior to deployment. If there are difference depending upon site, those difference will need to be provided.

**Table 5: Software Specifications**

| **Required Software**   | **Make**                | **Version**   |
|-------------------------|-------------------------|---------------|
| Apache                  | Apache Software         | 2.4.X         |
| Kubernetes              | Red Hat                 | 1.13.X        |
| Docker                  | Docker, Inc             | 18.06.0-ce    |
| Red Hat                 | Enterprise Linux Server | 7.X           |

Please refer to Table 2 in the Roles and Responsibilities section of this document for details about who is responsible for preparing the site to meet these software specifications.

#### Communications

Notification of scheduled maintenance periods that require the service to be offline or that may degrade system performance will be disseminated to the business user community a minimum of 48 hours prior to the scheduled event.

Notification to VA users for unscheduled system outages or other events that impact the response time will be distributed within 30 minutes of the occurrence.

Notification to VA users for unexpected system outages or other events that impact the response time will be distributed to Users as soon as possible.

Notification will be distributed to VA users regarding technical help desk support for obtaining assistance with receiving and processing.

### Deployment/Installation/Back-Out Checklist

The table below outlines the coordination effort and documents for the day/time/individual when each activity (deploy, install, back-out) is completed for DST.

**Table 6: Deployment/Installation/Back-Out Checklist**

| **Activity**   | **Day**                             | **Time**                         | **Individual who completed task**   |
|----------------|-------------------------------------|----------------------------------|-------------------------------------|
| Deploy         | Dependent on current build timeline | When approved by VA stakeholders | AbleVets                            |

| **Activity**   | **Day**                             | **Time**                         | **Individual who completed task**   |
|----------------|-------------------------------------|----------------------------------|-------------------------------------|
| Install        | Dependent on current build timeline | When approved by VA stakeholders | AbleVets                            |
| Back-Out       | Dependent on current build timeline | When approved by VA stakeholders | AbleVets                            |

## Installation

### Platform Installation and Preparation in Facility level

DST requires the following four separate components to be deployed for each facility.

#### Consult Toolbox

Consult Toolbox (CTB) is the Auto Hotkey component of the DST solution that is installed as a thick-client on the CPRS user’s workstations by the VA-ITOPS team. It is responsible for monitoring the state of which CPRS screen is displayed to the User, presenting the user with the option to launch DST, and facilitating the transfer of information between CPRS and the DST API/Database. Starting with version v1.9.0044 for MISSION Act, CTB included a dedicated DST .ini file that includes a string parameter containing the root URL for the DST endpoints.

When this parameter is NULL or the DST .ini file is not found, Consult Toolbox does not attempt any communication with DST and operates based on its pre-DST user experience. The initial national deployment of CTB v1.9.0044 was deployed with the DST URL set to an empty string.

During Quality Assurance and User Acceptance testing, the latest, approved version of CTB is used to verify full end-to-end solution.

#### VistA DST Patch to the GMRC Package at Each VistA Site

DST Veterans Health Information Systems and Technology Architecture (VistA) Patches GMRC are the VistA component of DST which must be installed on every VistA system where CPRS users need to use DST. The patch includes a protocol that invokes a process to retrieve the consult factor text from DST and insert it into a consult comment whenever a consult is signed that contains the string “DST ID:” in the Reason for Request field. The patch also adds the ability for the DST to Auto Forward requested Consults in accordance with Community Care Directives.

If the DST URL is not active during SQA testing, a test endpoint will be created to allow for end-to-end testing of the DST patch operation. The DST endpoint will respond when the CPRS RPC, detects the presence of literal “DST ID:”, in an order. The Protocol will then trigger and retrieve consult factor text from the DST API and insert the consult factor text into a newly- created consult. If the Auto-Forwarding comment is also included, then the Consult will be Forwarded to the included consult name.

The installation procedure for this VistA patch are uploaded to VA Forum per VA installation requirements.

#### DST Application

The DST is a web application that is invoked during the consult ordering workflow in CPRS using Consult Toolbox to intercept user interactions to inform the Veteran and their referring clinician about the availability of services in the VA and the Veteran’s eligibility for receiving care in the community.

DST provides three main capabilities in support of the MISSION Act requirements:

- Inform the Veteran and their referring clinician about service availability at nearby VA facilities and the Veteran’s eligibility for Community Care.
- Document the outcome of the care pathway decision process and provide structured data in the CPRS order.
- Report on system-wide compliance and utilization.

When the user opts to open DST, Consult Toolbox sends the following patient and consult information from CPRS. After DST is opened, DST orchestration calls all data partners to display all required decision data from the internal VA data interfaces namely - CDW, Eligibility and Enrollment system (E&amp;E/ESR) Service, PPMS, Lighthouse API, SEOC, and MVI. Further, the user enters a DST eligibility decision to be collected by a supportive VistA data interface to save in the consult.

#### Cerner PowerChart

Cerner's PowerChart is a hybrid Electronic Medical Record (EMR) solution that caters to clinicians in hospitals and ambulatory facilities and helps them to create multi-entity electronic medical records. The solution also provides capabilities for on-premise deployment. It provides various built-in templates that cover various specialties, thus serving a wide range of medical providers. PowerChart coordinates care between multiple locations and practitioners, helping users manage duplicated records while still giving staff flexible documentation options. These documentation options are reflected in the solution’s database of templates and customizable procedure workflows.

The DST application supports the Electronic Health Record Modernization (EHRM) by providing a Decision Support Viewer (DSV) application within the same DST application installation. The DSV application is used from Cerner’s PowerChart to review community care eligibility information for the patient.

### Download and Extract Files

DST does not download and extract files as a manual process. DST builds all environments using CI/CD pipeline approach utilizing a Jenkins build machine. With use of the Kubernetes infrastructure, as described in later sections, all services that comprise the DST application are compiled, packaged, published in the DST Jenkins environment. When a new deployment is available for an environment, the published Docker image artifacts are pulled from the registry to be installed within Kubernetes environment.

### Database ETL Jobs

The DST application relies on CDW data to provide clinical information and average wait time for services on the application. This information is loaded daily as part of CDW Extract,

Transform, Load (ETL) jobs maintained by the DST project team. This ETL code is maintained in the VA GitHub dst-cdw-etl repository and executed on a shared CDW ETL server maintained by the VA CDW group. This information is listed for informational purposes only. There are no additional install instructions needed for this release.

**Table 7: CDW ETL Jobs**

| **Job Name**                       | **Schedule**       | **Purpose**                                                             |
|------------------------------------|--------------------|-------------------------------------------------------------------------|
| Consult-Clinical Services Mappings | Every day at 2 AM  | Refreshes consult name to clinical service based on clinical stop codes |
| Facility-Clinical Services AWT     | Every week at 2 AM | Refreshes facility average wait time based on clinical stop codes       |

<!-- image -->

**Figure 4: CDW ETL Jobs**

### Installation Scripts

The following database scripts found in the dst-postgres-db code repo must be run for Build 20 functionality.

1. 21\_alter\_decision\_support\_hsrm\_25005.sql
2. 22\_Update\_cc\_average\_wait\_time default-1\_Consult\_AWT.sql
3. 22\_mockData\_for\_acceptanceTests.sql

### Cron Scripts

DST executed scheduled jobs within the Kubernetes ecosystem to load SEOC, load static facility information, and purged DST records. These jobs are part of the dst-scheduler VA Git repository. This code repository is built as a Kubernetes container pod. This information is listed for informational purposes only. There are no additional install instructions needed for this release.

**Table 8: Cron Scripts**

| **Job Name**            | **Schedule**      | **Purpose**                                                                                                  |
|-------------------------|-------------------|--------------------------------------------------------------------------------------------------------------|
| Delete_Decision_Support | Every day at 2 AM | Purges stale DST records that are greater than 30 days old, since DST is the source of record for this data. |
| Load_SEOC               | Every day at 2 AM | Refreshes active SEOC data within DST system.                                                                |
| Load_Facilities         | Every day at 5 AM | Refreshes static facility information from Lighthouse API.                                                   |

### Access Requirements and Skills Needed for the Installation

Installers will need to have a proper ePAS in order to gain access to the server with elevated privileges. The installers will need to have knowledge of Apache, Kubernetes, Docker, and Git.

### Installation Procedure

The DST application uses Helm commands to install the DST Helm chart. This chart describes the DST Kubernetes microservices and configuration for the system. Helm and Kubernetes are maintained in each DST VA Git repository. Specifically, the DST main chart that maintains the complete DST ecosystem is within the env-dst-pod-migration VA Git repository. The following steps are part of automated VA Jenkins job that run based on latest tested changes from the DST GitHub code repos.

To upgrade DST microservices with a new version of the software on any DST node that has Helm installed, execute the following commands:

1. helm repo update #get all latest charts.
2. helm upgrade &lt;chart name&gt; --namespace &lt;DST namespace&gt; --version=&lt;version to be upgrade to&gt;.
3. helm list #to verify latest charts that are installed.
### Installation Verification Procedure

To verify the installation is running on any DST node that has Helm installed, execute the following command: helm list #to verify latest charts that are installed. This process is executed during the normal installation procedures of the application.

### System Configuration

This section is not applicable.

### Database Tuning

This section is not applicable.

## Back-Out Procedure

The steps described below outline the procedure to remove the DST application from the CPRS Platform in Production.

### Back-Out Procedure

On any DST node that has Helm installed, execute the following commands:

1. helm list #to verify latest charts that are installed.
2. helm rollback &lt;chart name&gt; --version &lt;version to be rolled back&gt;.
### Authority for Back-Out

Based on authority provided by our Business Sponsor and VA Office of Information and Technology (OIT) IT program manager, DST can be backed out in accordance to their approval.

DST can back-out any service within the Kubernetes cluster, which are all application components.

## Rollback Procedure

Database (DB) snapshots are taken every evening. To restore the DST Database instance from a DB snapshot

1. Sign into the Amazon Web Services (AWS) Management Console and open the Amazon Relational Database Service (RDS) console.
2. In the navigation pane, choose Snapshots.
3. Choose the DB snapshot that you want to restore from.
4. For Actions, choose Restore Snapshot. The Restore DB Instance page displays.
5. For DB Instance Identifier under Settings, enter the name that you want to use for the restored Database instance. If you are restoring from a DB instance that you deleted after you made the Database snapshot, you can use the name of that DB instance.
6. Choose Restore DB Instance.
### Rollback Considerations.

DST can roll back the DST AWS RDS Postgres instance.

### Rollback Criteria

Rollback criteria are not applicable.

### Rollback Risks

There is minimal risk associated to these rollback procedures. It is common practice to rollback Kubernetes microservices and is part of the design of the technology. All DST application code and infrastructure are maintained as code saved in source control in VA GitHub, so there is minimal potential loss of functionality when an issue arises. Finally, AWS provides highly resilient backup processes for all the DST AWS RDS database.

### Authority for Rollback

Based on authority provided by our Business Sponsor and VA OIT IT program manager, DST can be backed out in accordance to their approval.

### Rollback Procedure

The rollback procedure steps are documented in Section 5.1 Back-Out Procedure for the application and infrastructure. The backout instructions are the same as rollback for the application. The rollback procedure steps are documented in Section 6 for the database.

## Risk and Mitigation Plan

The DST project team maintains a Program Risk Registry. Refer to the Program Risk Registry for all risks and mitigation plans for the entire DST project, including Consult Toolbox and VistA integration along with the VA partner interfaces (MPI/MVI, E&amp;E/ESR, PPMS, Lighthouse API, CDW, SEOC).