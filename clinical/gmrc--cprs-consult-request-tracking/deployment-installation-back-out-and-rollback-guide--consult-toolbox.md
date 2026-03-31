---
consolidated_title: "consult toolbox deployment, installation, back-out, and rollback guide"
app_code: GMRC
doc_type: DIBR
master_source: "Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0063"
master_pub_date: April 2020
consolidated_from: 7 versions
prior_versions:
  - "Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0054"
  - "Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0056"
  - "Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0065"
  - "Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0071"
  - "Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0072"
  - "Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0076"
---

## Consult Toolbox Software Version 1.9.0063

**Deployment, Installation, Back-Out, and Rollback Guide**

<!-- image -->

#### April 2020 Department of Veterans Affairs

**Office of Information and Technology (OIT)**

**Revision History**

| **Date**   |   **Version** | **Description**                  | **Author**   |
|------------|---------------|----------------------------------|--------------|
| 04/14/2020 |           1.9 | v1.9.0063 Initial Update         | AbleVets     |
| 04/01/2020 |           1.8 | v1.9.0062 Initial Update         | AbleVets     |
| 02/03/2020 |           1.7 | v1.9.0061 Initial Update         | AbleVets     |
| 12/17/2019 |           1.6 | v1.9.0056 Initial Update         | AbleVets     |
| 11/21/2019 |           1.5 | v1.9.0054 Final Update           | AbleVets     |
| 10/02/2019 |           1.4 | v1.9.0052 Final Update           | AbleVets     |
| 08/20/2019 |           1.3 | v1.9.0050 Initial Update         | AbleVets     |
| 05/03/2019 |           1.2 | v1.9.0004 Final Update           | AbleVets     |
| 02/25/2019 |           1.1 | v1.9.0004 Initial Update         | AbleVets     |
| 12/21/2018 |           1   | v1.9.02b Update pre-installation | AbleVets     |
| 12/14/2018 |           0.9 | v1.9.02a Remediation Updates     | AbleVets     |
| 09/26/2018 |           0.8 | v1.9.02 Remediation Updates      | AbleVets     |
| 08/08/2018 |           0.7 | v1.8.02 Release                  | AbleVets     |
| 06/29/2018 |           0.6 | Response to Comments             | AbleVets     |
| 03/01/2018 |           0.5 | v1.8.01 Release                  | CC IT PMO    |
| 12/01/2017 |           0.4 | v1.7.01 Release                  | CC IT PMO    |
| 10/12/2017 |           0.3 | v1.0.6051 Release                | CC IT PMO    |
| 08/01/2017 |           0.2 | v1.0.6 Release                   | CC IT PMO    |
| 05/01/2017 |           0.1 | Initial Creation                 | CC IT PMO    |

**Artifact Rationale**

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point #2 (CD #2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

#### Table of Contents

1. Introduction	1
    - 1.1. Purpose	1
    - 1.2. Dependencies	1
    - 1.3. Constraints	2
2. Roles and Responsibilities	2
3. Deployment	3
    - 3.1. Timeline	3
    - 3.2. Site Readiness Assessment	3
        - 3.2.1. Deployment Topology (Targeted Architecture)	3
        - 3.2.2. Site Information (Locations, Deployment Recipients)	3
        - 3.2.3. Site Preparation	3
    - 3.3. Resources	3
        - 3.3.1. Facility Specifics (optional)	3
        - 3.3.2. Hardware	4
        - 3.3.3. Software	4
        - 3.3.4. Communications	4
            - 3.3.4.1. Deployment/Installation/Back-Out Checklist	4
4. Installation	4
    - 4.1. Pre-installation and System Requirements	4
    - 4.2. Platform Installation and Preparation	5
    - 4.3. Download and Extract Files	5
    - 4.4. Cron Scripts	5
    - 4.5. Access Requirements and Skills Needed for the Installation	6
    - 4.6. Installation Procedure	6
    - 4.7. Procedure	6
    - 4.8. System Configuration	6
    - 4.9. Database Tuning	6
5. Back-Out Procedure	7
    - 5.1. Back-Out Strategy	7
    - 5.2. Back-Out Considerations	7
        - 5.2.1. Load Testing	7
        - 5.2.2. User Acceptance Testing	7
    - 5.3. Back-Out Criteria	7
    - 5.4. Back-Out Risks	7
    - 5.5. Authority for Back-Out Action Item	7
    - 5.6. Back-Out Procedure	7
    - 5.7. Back-out Verification Procedure	8
6. Rollback Procedure	8
    - 6.1. Rollback Considerations	8
    - 6.2. Rollback Criteria	8
    - 6.3. Rollback Risks	8
    - 6.4. Authority for Rollback	8
    - 6.5. Rollback Procedure	8
    - 6.6. Rollback Verification Procedure	8

**List of Tables**

Table 1: Prerequisites	1

Table 2: Dependencies	1

Table 3: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities	2

Table 4: Site Preparation	3

Table 5: Facility-Specific Features	3

Table 6: Hardware Specifications	4

Table 7: Software Specifications	4

Table 8: Deployment/Installation/Back-Out Checklist	4

## Introduction

This document describes how to deploy and install the One Consult Toolbox client application, as well as how to back-out the product to a previous version or data set. Deployment and installation of the One Consult Toolbox Care Assessment Need (CAN) Score Application Program Interface (API) application is covered in a feature specific guide. This document is a companion to the project charter and management plan for this effort. In cases where a non- developed Commercial-Off-The-Shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

### Purpose

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the One Consult Toolbox will be deployed and installed, as well as how it is to be backed out, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

This document describes the content and functionality of the Consult Toolbox installation build created by Enterprise Systems Engineering (ESE), Client Services, and Desktop Technologies.

Consult toolbox is an AutoHotkey based application that provides standardized processes and procedures for documenting consults.

Consult Toolbox runs on the following operating systems.

- Windows 7, 64-bit
- Windows 10, 64-bit

The table below shows the prerequisites for Consult Toolbox. If these applications are not present on the target computer, the Consult Toolbox setup or the application will fail.

**Table 1: Prerequisites**

| **Product Name**   | **Product Version**   | **How to Check Whether it is Installed**   | **Link for Package Build Document**   |
|--------------------|-----------------------|--------------------------------------------|---------------------------------------|
| N/A                | N/A                   | N/A                                        | N/A                                   |

### Dependencies

**Table 2: Dependencies**

| **Release Dependency**        | **Description**   | **Status of Dependency**   | **Notes or Concerns (availability, funding, resources, etc.)**   |
|-------------------------------|-------------------|----------------------------|------------------------------------------------------------------|
| Field Implementation Services | Deployment        | Active                     | Upstream                                                         |
| Desktop                       | National Package  | Active                     | Upstream                                                         |

### Constraints

Not Applicable – No Constraints regarding physical environment.

## Roles and Responsibilities

**Table 3: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities**

| **ID**   | **Team**                                                | **Phase / Role**   | **Tasks**                                                                                                           | **Project Phase (See Schedule)**   |
|----------|---------------------------------------------------------|--------------------|---------------------------------------------------------------------------------------------------------------------|------------------------------------|
|          | Enterprise Systems Engineering Desktop Technology (ESE) | Deployment         | Plan and schedule deployment (including orchestration with vendors)                                                 |                                    |
|          | ESE                                                     | Deployment         | Determine and document the roles and responsibilities of those involved in the deployment.                          |                                    |
|          | Enterprise Service Line Client Technology (ESL)         | Deployment         | Test for operational readiness                                                                                      |                                    |
|          | ESE/ESL                                                 | Deployment         | Execute deployment                                                                                                  |                                    |
|          | ESE/ESL                                                 | Installation       | Plan and schedule installation                                                                                      |                                    |
|          | To Be Determined                                        | Installation       | Ensure authority to operate and that certificate authority security documentation is in place                       |                                    |
|          | Not Applicable                                          | Installation       | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         | No inventory being used            |
|          | Clinical Application                                    | Installations      | Coordinate training                                                                                                 | Application Use Only               |
|          | ESE                                                     | Back-out           | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |                                    |
|          | AbleVets/Config Mgmt                                    | Post Deployment    | Hardware, Software, and System Support                                                                              |                                    |

## Deployment

The deployment is planned as a simultaneous rollout.

This section provides the schedule and milestones for the deployment.

### Timeline

The deployment and installation is scheduled to run for 30 days, as depicted in the master deployment schedule April 13, 2020 to May 13, 2020.

### Site Readiness Assessment

This section discusses the locations that will receive the One Consult Toolbox deployment. Toolbox is being deployed to all Clinical facilities.

#### Deployment Topology (Targeted Architecture)

Consult Toolbox will be deployed to all Clinical Workstations.

#### Site Information (Locations, Deployment Recipients)

Consult Toolbox will be deployed to all Clinical Workstations.

#### Site Preparation

The following table describes preparation required by the site prior to deployment.

**Table 4: Site Preparation**

| **Site/Other**   | **Problem/Change Needed**   | **Features to Adapt/Modify to New Product**   | **Actions/Steps**   | **Owner**   |
|------------------|-----------------------------|-----------------------------------------------|---------------------|-------------|
| N/A              | N/A                         | N/A                                           | N/A                 | N/A         |

### Resources

Field Implementation Services

- 3.3.1. **Facility Specifics** ***(optional)***

The following table lists facility-specific features required for deployment.

**Table 5: Facility-Specific Features**

| **Site**   | **Space/Room**   | **Features Needed**   | **Other**   |
|------------|------------------|-----------------------|-------------|
| N/A        | N/A              | N/A                   | N/A         |

#### Hardware

The following table describes hardware specifications required at each site prior to deployment.

**Table 6: Hardware Specifications**

| **Required Hardware**   | **Model**   | **Version**   | **Configuration**   | **Manufacturer**   | **Other**   |
|-------------------------|-------------|---------------|---------------------|--------------------|-------------|
| N/A                     | N/A         | N/A           | N/A                 | N/A                | N/A         |

Please see the table in the Roles and Responsibilities section of this document for details about who is responsible for preparing the site to meet these hardware specifications.

#### Software

The following table describes software specifications required at each site prior to deployment.

**Table 7: Software Specifications**

| **Required Software**   | **Make**   | **Version**   | **Configuration**   | **Manufacturer**   | **Other**   |
|-------------------------|------------|---------------|---------------------|--------------------|-------------|
| N/A                     | N/A        | N/A           | N/A                 | N/A                | N/A         |

Please see the table in the Roles and Responsibilities section of this document for details about who is responsible for preparing the site to meet these software specifications.

#### Communications

#### Deployment/Installation/Back-Out Checklist

**Table 8: Deployment/Installation/Back-Out Checklist**

| **Activity**      | **Day**   | **Time**   | **Individual who completed task**   |
|-------------------|-----------|------------|-------------------------------------|
| Deploy (planned)  | 4/17/2020 | 12:00 AM   | Field Implementation Services       |
| Install (planned) | 4/17/2020 | 12:00 AM   | Field Implementation Services       |
| Back-Out          | TBD       | 12:00 AM   | Field Implementation Services       |

## Installation

### Pre-installation and System Requirements

Consult Toolbox runs on the following operating systems.

- Consult Toolbox runs on the following operating systems:
- Windows 10, 64-bit

- Windows 7, 64-bit

- The following Log File is created:

- %ALLUSERSPROFILE%\DeptOfVeteransAffairs\Logs\VA\_ConsultToolbox\_1.

9.0063.log

- Prior version of Consult Toolbox must be uninstalled
- All files must be removed from the folder %AppData%\ConsultToolbox
### Platform Installation and Preparation

Not Applicable – no Platform Installation or Preparation required.

### Download and Extract Files

For manual installations, execute the following steps in order.

1. Use dBAT for manual Install.
2. dBAT website is here for more information and help files.
3. Once connected to the workstation select the **Baseline** or **Tier 3/4** tab.
4. Find Consult Toolbox and check the check box next to application name and press
<!-- image -->

***NOTE:*** *Under* ***Baseline*** *view, only non-compliant applications (either below or above application standard) will be checkable to install. Under* ***Tier 3&amp;4*** *view, all applications are checkable to install or uninstall.*

<!-- image -->

<!-- image -->

Application Name

1VA - VA ConsultToolbox 1.9.0063 *(to be verified with build guide)*

Application ID N/A

Package Size

2.82 MB

CM Application Source

<!-- image -->

***NOTE:*** *Please use the search functionality to locate a package in CM*

<!-- image -->

<!-- image -->

Not Applicable – no Cron script required for software installation.

### Access Requirements and Skills Needed for the Installation

For manual installations, execute the following steps in order.

- 4.4.1. Use dBAT for manual Install.
- 4.4.2. dBAT website is here for more information and help files.
- 4.4.3. Once connected to the workstation select the **Baseline** or **Tier 3/4** tab.
- 4.4.4. Find Consult Toolbox and check the check box next to application name and press
<!-- image -->

***NOTE:*** *Under* ***Baseline*** *view, only non-compliant applications (either below or above application standard) will be checkable to install. Under* ***Tier 3&amp;4*** *view, all applications are checkable to install or uninstall.*

<!-- image -->

<!-- image -->

For manual installations, execute the following steps in order.

- 4.4.1. Use dBAT for manual Install.

dBAT website is here for more information and help files.

- 4.4.1. Once connected to the workstation select the **Baseline** or **Tier 3/4** tab.
- 4.4.2. Find Consult Toolbox and check the check box next to application name and press
<!-- image -->

***NOTE:*** *Under* ***Baseline*** *view, only non-compliant applications (either below or above application standard) will be checkable to install. Under* ***Tier 3 &amp; 4*** *view, all applications are checkable to install or uninstall.*

<!-- image -->

<!-- image -->

If you experience any issues with this package installation, please follow the procedures found in the [Package Installation Issues Procedures](http://vaww.eie.va.gov/SysDesign/CS/Shared%20Documents/Help/SD%20DDE%20Package%20Installation%20Issues%20Procedures.pdf) .

### System Configuration

Not Applicable – no system configuration instructions required.

### Database Tuning

Not Applicable – no database tuning information or tips required.

## Back-Out Procedure

Follow local established procedures for Un-installing the application or patch that is causing problems, either manually, dBAT or via SCCM. Run back out command line as documented in the build document found by accessing the 'Portal Entry' link from the attachments tab of this change order. From there, follow the link 'Build Document'.

### Back-Out Strategy

The back-out strategy will follow VA guidelines and best practices as referenced in the Enterprise Operations (EO) National Data Center Hosting Services document.

### Back-Out Considerations

Not Applicable – no Back-Out Considerations required.

#### Load Testing

Not Applicable – no Load Testing required.

#### User Acceptance Testing

Not Applicable – no User Acceptance Testing required.

### Back-Out Criteria

Not Applicable – no Back-Out Criteria required.

### Back-Out Risks

Not Applicable – no Back-Out Risks associated.

### Authority for Back-Out Action Item

Dr. Clinton Greenstone, Product Owner.

### Back-Out Procedure

Execute the following steps to uninstall the full Consult Toolbox application.

1. Launch dBAT.exe and connect to workstation listed in Manual Installation.
2. In **Workstation Detail View** and select the **Programs &amp; Features** tab.
3. Find Consult Toolbox and check the check box next to application name and press

**Install/Uninstall** button to initiate uninstall if installed.

### Back-out Verification Procedure

Execute the following steps to uninstall the full Consult Toolbox application.

1. Launch dBAT.exe and connect to workstation listed in Manual Installation.
2. In **Workstation Detail View** and select the **Programs &amp; Features** tab.
3. Find Consult Toolbox and check the check box next to application name and press

**Install/Uninstall** button to initiate uninstall if installed.

## Rollback Procedure

Follow local established procedures for Un-installing the application or patch that is causing problems, either manually, dBAT or via SCCM. Run back out command line as documented in the build document found by accessing the 'Portal Entry' link from the attachments tab of this change order. From there, follow the link 'Build Document'.

### Rollback Considerations

Not Applicable – no Rollback Considerations required.

### Rollback Criteria

Not Applicable – no Rollback criteria required.

### Rollback Risks

Not Applicable – no Rollback Risks associated.

### Authority for Rollback

Not Applicable – no Rollback Authority required.

### Rollback Procedure

Not Applicable – no Rollback Procedure required.

### Rollback Verification Procedure

Not Applicable – no Rollback Verification Procedure required.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Consult Toolbox Deployment, Installation, Back-Out, and Rollback Guide v1.9.0071

## Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point #2 (CD #2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

#### Table of Contents

1. Introduction	1
    - 1.1. Purpose	1
    - 1.2. Dependencies	1
    - 1.3. Constraints	2
2. Roles and Responsibilities	2
3. Deployment	3
    - 3.1. Timeline	3
    - 3.2. Site Readiness Assessment	3
        - 3.2.1. Deployment Topology (Targeted Architecture)	3
        - 3.2.2. Site Information (Locations, Deployment Recipients)	3
        - 3.2.3. Site Preparation	3
    - 3.3. Resources	3
        - 3.3.1. Facility Specifics (optional)	3
        - 3.3.2. Hardware	4
        - 3.3.3. Software	4
        - 3.3.4. Communications	4
            - 3.3.4.1. Deployment/Installation/Back-Out Checklist	4
4. Installation	4
    - 4.1. Pre-installation and System Requirements	4
    - 4.2. Platform Installation and Preparation	5
    - 4.3. Download and Extract Files	5
    - 4.4. Cron Scripts	5
    - 4.5. Access Requirements and Skills Needed for the Installation	6
    - 4.6. Installation Procedure	6
    - 4.7. Procedure	6
    - 4.8. System Configuration	6
    - 4.9. Database Tuning	6
5. Back-Out Procedure	7
    - 5.1. Back-Out Strategy	7
    - 5.2. Back-Out Considerations	7
        - 5.2.1. Load Testing	7
        - 5.2.2. User Acceptance Testing	7
    - 5.3. Back-Out Criteria	7
    - 5.4. Back-Out Risks	7
    - 5.5. Authority for Back-Out Action Item	7
    - 5.6. Back-Out Procedure	7
    - 5.7. Back-out Verification Procedure	8
6. Rollback Procedure	8
    - 6.1. Rollback Considerations	8
    - 6.2. Rollback Criteria	8
    - 6.3. Rollback Risks	8
    - 6.4. Authority for Rollback	8
    - 6.5. Rollback Procedure	8
    - 6.6. Rollback Verification Procedure	8

**List of Tables**

Table 1: Prerequisites	1

Table 2: Dependencies	1

Table 3: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities	2

Table 4: Site Preparation	3

Table 5: Facility-Specific Features	3

Table 6: Hardware Specifications	4

Table 7: Software Specifications	4

Table 8: Deployment/Installation/Back-Out Checklist	4

### Cron Scripts

Not Applicable – no Cron script required for software installation.

### Installation Procedure

For manual installations, execute the following steps in order.

- 4.4.1. Use dBAT for manual Install.

dBAT website is here for more information and help files.

- 4.4.1. Once connected to the workstation select the **Baseline** or **Tier 3/4** tab.
- 4.4.2. Find Consult Toolbox and check the check box next to application name and press

**Install/Uninstall** button to initiate installation.

***NOTE:*** *Under* ***Baseline*** *view, only non-compliant applications (either below or above application standard) will be checkable to install. Under* ***Tier 3 &amp; 4*** *view, all applications are checkable to install or uninstall.*

<!-- image -->

### Procedure

If you experience any issues with this package installation, please follow the procedures found in the [Package Installation Issues Procedures](http://vaww.eie.va.gov/SysDesign/CS/Shared%20Documents/Help/SD%20DDE%20Package%20Installation%20Issues%20Procedures.pdf) .
