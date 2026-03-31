---
consolidated_title: "edis deployment, installation, back-out, and rollback guide"
app_code: EDIS
doc_type: installation-guide
master_source: "EDP*2*15 EDIS Deployment, Installation, Back-out, and Rollback Guide"
master_pub_date: June 2021
consolidated_from: 3 versions
prior_versions:
  - "EDP*2*16 EDIS Deployment, Installation, Back-out, and Rollback Guide"
  - "EDP*2*22 EDIS Deployment, Installation, Back-out, and Rollback Guide"
---

# Emergency Department Integrated Software (EDIS)

# Deployment, Installation, Back-Out, and Rollback Guide

<!-- image -->

VistA EDP*2.0*15

EDIS GUI Version 2.2.43

June 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

| **Date**   |   **Version** | **Description**                                                                                                                                                                                                                                                                                                                                                                 | **Author**   |
|------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------|
| 06/23/2021 |             1 | EDIS 2.2.43/EDP*2.0*15:  - **EDIS 2.2.43** (GUI) consists of the deployment of 2 ear files coordinated by the OIT EDIS Sustainment team - **EDP*2.0*15** (VistA) consists of the invoking a PackMan message in FORUM by Regional IT Support - Reintroduces SSOi for users - See the non-redacted EDIS\_2\_2\_P15\_DIBR on the SOFTWARE library for viewing REDACTED information | Liberty ITS  |

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Guide for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the *Deployment, Installation, Back-out, and Rollback Guide* is required to be completed prior to Critical Decision Point #2 (CD #2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Table of Contents

1	Introduction	1

1.1	Purpose	1

1.2	Dependencies	1

1.3	Constraints	1

2	Roles and Responsibilities	2

3	Deployment	4

3.1	Timeline	4

3.2	Site Readiness Assessment	4

3.2.1	Deployment Topology (Targeted Architecture)	4

3.2.2	Site Information (Locations, Deployment Recipients)	4

3.2.3	Site Preparation	5

3.3	Resources	5

3.3.1	Facility Specifics	5

3.3.2	Hardware	5

3.3.3	Software	6

3.3.4	Communications	6

4	Installation	7

4.1	Pre-installation and System Requirements	7

4.2	Platform Installation and Preparation	7

4.3	Download and Extract Files	7

4.4	Database Creation	8

4.5	Installation Scripts	8

4.6	Cron Scripts	8

4.7	Access Requirements and Skills Needed for the Installation	8

4.8	Installation Procedure	8

4.8.1	KIDS Installation	8

4.9	Installation Verification Procedure	9

4.9.1	KIDS Verification	9

4.10	System Configuration	9

4.11	Database Tuning	9

5	Back-Out Procedure	10

5.1	Back-Out Strategy	10

5.2	Back-Out Considerations	10

5.2.1	Load Testing	10

5.2.2	User Acceptance Testing	10

5.3	Back-Out Criteria	10

5.4	Back-Out Risks	10

5.5	Authority for Back-Out	10

5.6	Back-Out Procedure	11

5.6.1	KIDS Back-Out	11

5.7	Back-out Verification Procedure	11

5.7.1	KIDS Back-out Verification	11

6	Rollback Procedure	12

6.1	Rollback Considerations	12

6.2	Rollback Criteria	12

6.3	Rollback Risks	12

6.4	Authority for Rollback	12

6.5	Rollback Procedure	12

6.6	Rollback Verification Procedure	12

List of Tables

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities	2

Table 2: Site Preparation	5

Table 3: Facility-Specific Features	5

Table 4: Hardware Specifications	5

Table 5: Software Specifications	6

Table 6: Deployment/Installation/Back-Out Checklist	6

Table 7: Associated Patch Files	7

Table 8: Routines	9

## Introduction

There are 2 parts to this release:

1. **EDIS 2.2.43** refers to the GUI/Web Server version (reintroduces SSOi)
2. **EDP*2.0*15** refers to the VistA (KIDS Build) patch

This document will focus on the deployment, installation,and back-out procedures for VistA patch EDP*2.0*15. The EDIS 2.2.43 deployment will be completed by the OIT EDIS Sustainment team prior to the procedures outlined in this document.

### Purpose

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom EDP*2.0*15 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, communications plan, and rollout schedule.

### Dependencies

This patch must be installed after EDP*2.0*6.

### Constraints

EDP*2.0*15 is expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. EDP*2.0*15 utilizes existing nationally released security controls to control access.

## Roles and Responsibilities

Multiple entities oversee decision making for the deployment, installation, back-out and rollback of EDP*2.0*15. Application Coordinators approve deployment and install from an OIT perspective. If an issue with the software arises, then the facility Chief Information Officer (CIO) and other site leadership will meet along with input from Patient Safety, Health Product Support (HPS), and regional leadership to initiate a back out and rollback decision of the software. The following table provides EDP*2.0*15 information.

Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

| **Team**                                                                                                                                                                                               | **Phase / Role**   | **Tasks**                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|--------------------------------------------------------------------------------------------------------------------------------|
| Enterpirse Operations                                                                                                                                                                                  | Deployment         | Deploy the Oracle Weblogic Application Server ear files                                                                        |
| Site personnel in conjunction with information technology (IT) support – which may be local or regional.                                                                                               | Deployment         | Plan and schedule deployment (including orchestration with vendors)                                                            |
| Site personnel in conjunction with IT support – which may be local or regional.                                                                                                                        | Deployment         | Determine and document the roles and responsibilities of those involved in the deployment.                                     |
| Site personnel.                                                                                                                                                                                        | Deployment         | Test for operational readiness                                                                                                 |
| Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the Kernel Installation and Distribution System (KIDS) build. | Deployment         | Execute deployment                                                                                                             |
| Site personnel in conjunction with IT support – which may be local or regional. The IT support will need to include person(s) to install the KIDS.                                                     | Installation       | Plan and schedule installation                                                                                                 |
| N/A – will work under the VistA authority to operate (ATO) and security protocols.                                                                                                                     | Installation       | Ensure that ATO and certificate authority security documentation is in place                                                   |
| N/A – no equipment is being added.                                                                                                                                                                     | Installation       | Validate through facility point of contact (POC) to ensure that IT equipment has been accepted using asset inventory processes |
| N/A – no new functionality is being introduced.                                                                                                                                                        | Installations      | Coordinate training                                                                                                            |
| Facility CIO and IT support – which may be local or regional.                                                                                                                                          | Back-out           | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)            |
| Hardware and System support – no changes.  Software support will be the HPS Clinical Sustainment team.                                                                                                 | Post Deployment    | Hardware, Software and System Support                                                                                          |

## Deployment

There are 2 components for this release:

1. **EDIS 2.2.43** GUI/Web Server (reintroduces SSOi)
    - 1.1. This ear file deployment is completed by the OIT EDIS Sustainment team.
2. **EDP*2.0*15** VistA Patch
    - 2.1. Installed/deployed using a PackMan message in FORUM by Regional IT support.

Deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release EDP*2.0*15, the patch will be released via the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing, and deployment to production will be at the site’s discretion. It is anticipated that there will be a 30-day compliance period.

### Timeline

There is no specific timeline for deployment. This is considered a maintenance release and installation will be at the site’s discretion within the contstraints of the compliance period for the release.

### Site Readiness Assessment

This section discusses the locations that will receive the EDP*2.0*15 deployment.

#### Deployment Topology (Targeted Architecture)

EDP*2.0*15 will be deployed to each VistA instance and the nationally deployed EDIS Uniform Resource Locater (URL) will be updated to EDIS 2.2.43. That will include local sites as well as regional data processing centers.

#### Site Information (Locations, Deployment Recipients)

The first deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, EDP*2.0*15 will be deployed to all VistA systems.

The Production IOC testing sites are:

Boston Health Care System

VA Long Beach Health Care System

Greater Los Angeles Health Care System

#### Site Preparation

There is no special preparation required for EDP*2.0*15. A fully patched VistA system is the only requirement.

It would be beneficial if users have their PIV card linked to their VistA instance prior to installation.

**Note:** Upon installation of EDP*2.0*15, sites should be aware that “ghost” patients, patients with a LOC field entry of **0** and a recent visit within 5 days, will appear on their EDIS board in the default room defined by the site. Refer to the patch description for technical details.

The following table describes preparation required by the site prior to deployment.

Table 2: Site Preparation

| **Site/Other**   | **Problem/Change Needed**   | **Features to Adapt/Modify to New Product**   | **Actions/Steps**   | **Owner**   |
|------------------|-----------------------------|-----------------------------------------------|---------------------|-------------|
| N/A              |                             |                                               |                     |             |

### Resources

Not applicable for EDP*2.0*15.

#### Facility Specifics

The following table lists facility-specific features required for deployment.

Table 3: Facility-Specific Features

| **Site**   | **Space/Room**   | **Features Needed**   | **Other**   |
|------------|------------------|-----------------------|-------------|
| N/A        |                  |                       |             |

#### Hardware

The following table describes hardware specifications required at each site prior to deployment.

Table 4: Hardware Specifications

| **Required Hardware**   | **Model**   | **Version**   | **Configuration**   | **Manufacturer**   | **Other**   |
|-------------------------|-------------|---------------|---------------------|--------------------|-------------|
| N/A                     |             |               |                     |                    |             |

Please see the Roles and Responsibilities table in section 2 for details about who is responsible for preparing the site to meet these hardware specifications.

#### Software

The following table describes software specifications required at each site prior to deployment.

Table 5: Software Specifications

| **Required Software**   | **Make**   | **Version**   | **Configuration**   | **Manufacturer**   | **Other**   |
|-------------------------|------------|---------------|---------------------|--------------------|-------------|
| N/A                     |            |               |                     |                    |             |

Please see the Roles and Responsibilities table in section 2 above for details about who is responsible for preparing the site to meet these software specifications.

#### Communications

EDP*2.0*15 will be deployed using the standard method of patch release from the National Patch Module. When EDP*2.0*15 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The Release Management team will deploy the EDP*2.0*15 patch. This patch is tracked nationally for all VA Medical Centers (VAMCs) in the National Patch Module (NPM) in FORUM. FORUM automatically tracks the patches as they are installed in the different VAMC production systems. A report can be executed in FORUM to identify when the patch was installed in VistA production systems at each site. A report can also be run to identify which sites have not currently installed the patch in their VistA production system. Therefore, this information does not need to be manually tracked in Table 6.

EDIS 2.2.43 is Nationally deployed to all sites by updating the existing EDIS URL. Tracking is not necessary.

Table 6: Deployment/Installation/Back-Out Checklist

| Activity   | Day   | Time   | Individual who completed task   |
|------------|-------|--------|---------------------------------|
| N/A        | N/A   | N/A    | N/A                             |
| N/A        | N/A   | N/A    | N/A                             |
| N/A        | N/A   | N/A    | N/A                             |

## Installation

There are two parts to the EDP*2.0*15 installation.

1. **EDIS 2.2.43 (GUI)**
    - 1.1. Deployment and installation of EDIS\_EAR\_MAIN\_2\_2\_43.ear and EDIS\_EAR\_BIGBOARD\_2\_2\_43.ear files on the Oracle WebLogic Application Server by the OIT EDIS Sustainment team. **This step has been completed.**
2. **EDP*2.0*15**
    - 2.1. Deployment and installation on the site’s VistA server via PackMan message.

### Pre-installation and System Requirements

EDP*2.0*15 is installable on a fully patched VistA system.

**Note:** It is imperative to perform a back-up of the routines included in this patch prior to installation. This back-up is required if a back-out of EDP*2.0*15 is needed.

### Platform Installation and Preparation

EDP*2.0*15 must be installed on the VistA System. This patch must be installed by the compliance date.

This patch may be installed with users on the system although it is recommended that it be installed during non-peak hours to minimize potential disruption to users. This patch should take less than 5 minutes to install.

### Download and Extract Files

The following documents and files can be obtained from the SOFTWARE library:

REDACTED

Table 7: Associated Patch Files

| File                  | Description                                         |
|-----------------------|-----------------------------------------------------|
| EDIS_2_2_IG.pdf       | Server Installation Guide with Client Configuration |
| EDIS_2_2_TM.pdf       | Technical Manual                                    |
| EDIS_2_2_UG.pdf       | User Guide                                          |
| EDP_2_2_P15_DIBR.pdf  | Deployment, Installation, Back-out, Rollback guide  |
| EDIS_2_2_GLOSSARY.pdf | Glossary                                            |

The documents are also available on the VistA Documentation Library (VDL), which is located at:

[https://www.va.gov/vdl/application.asp?appid=179](https://www.va.gov/vdl/application.asp?appid=179)

### Database Creation

Not applicable for EDP*2.0*15

### Installation Scripts

Not applicable for EDP*2.0*15

### Cron Scripts

Not applicable for EDP*2.0*15

### Access Requirements and Skills Needed for the Installation

Installation of EDP*2.0*15 requires the following to install:

Programmer access to VistA instance.

### Installation Procedure

#### KIDS Installation

1. Choose the PackMan message containing this build. Then select the **INSTALL/CHECK MESSAGE** PackMan option to load the build.
2. From the Kernel Installation and Distribution System Menu, select the **Installation Menu** . From this menu,
    - 2.1. Select the **Verify Checksums in Transport Global** option to confirm the integrity of the routines that are in the transport global. When prompted for the INSTALL NAME enter the patch or build name (e.g. EDP*2.0*15).

**NOTE:** Using &lt;spacebar&gt;&lt;enter&gt; will not bring up a Multi-Package build even if it was loaded immediately before this step. It will only bring up the last patch in the build.

- 0.1. Select the **Backup a Transport Global** option to create a backup message of any routines exported with this patch. It will not backup any other changes such as data dictionaries or templates.
- 0.2. You may also elect to use the following options:
- 0.2.2. **Compare Transport Global to Current System** - This option will allow you to view all changes that will be made when this patch is installed.  It compares all of the components of this patch, such as routines, data dictionaries, templates, etc.
- 0.3.2. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', answer **NO** .
- 0.3.3. When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//', answer **NO** .

### Installation Verification Procedure

#### KIDS Verification

Verify the routine checksums in the table below.

Table 8: Routines

| Routine   | Before Checksum   | After Checksum   | Patch List   |
|-----------|-------------------|------------------|--------------|
| EDP15P    | New               | B2688979         | **15**       |
| EDPQDB    | B56093021         | B57296617        | **6,15**     |

### System Configuration

Not applicable for EDP*2.0*15.

### Database Tuning

Not applicable for EDP*2.0*15.

## Back-Out Procedure

### Back-Out Strategy

The only reason to consider a back-out of EDP*2.0*15 is in the event of a catastrophic failure.

The back-out plan is to restore the routines from the backup created in section 4.8.1, step 2B.

VistA changes in EDP*2.0*15 are independent of the GUI changes in EDIS 2.2.43. The VistA patch can be backed out without impact to the GUI.

### Back-Out Considerations

#### Load Testing

No load testing was performed for EDP*2.0*15. This was a maintenance release to correct defects; there was no additional functionality included.

#### User Acceptance Testing

User acceptance testing was conducted by the test sites listed in section 3.2.2. The sites followed the provided test plan/concurrence form and executed the test cases according to the plan for the first build of EDP*2.0*15. The sites either passed or failed any item based on testing. The tests were performed by IT analysts at each site who are familiar with using the application. Any items that failed were then re-developed, sent back to the sites, and tested for the next build following the same process. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

### Back-Out Criteria

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application or a significant patient impact issue.

### Back-Out Risks

Backing out EDP*2.0*15 would result in the re-instatement of the issues addressed in the previous version of EDIS. In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

### Authority for Back-Out

The facility Chief Information Officer may make the decision to back-out the VistA patch.

### Back-Out Procedure

#### KIDS Back-Out

Administrators will need to use the PackMan function INSTALL/CHECK MESSAGE. Check MailMan messages for the backup message sent by the Backup a Transport Global function executed prior to the patch install. (See section 4.8.1, Step 2B; this must be done before the patch is installed).

1. In VistA MailMan, select the message shown below:
    - 1.1. Backup of EDP*2.0*15 install on &lt;mm, dd, yyyy&gt; &lt;user name&gt;
2. Select the Xtract PackMan option.
3. Select the Install/Check Message option.
4. Enter Yes at the prompt.
5. Enter No at the backup prompt. There is no need to back up the backup.

### Back-out Verification Procedure

#### KIDS Back-out Verification

To verify the back-out completed successfully, ensure the routine checksums match the before checksums in section 4.9.1.

## Rollback Procedure

Not applicable for EDP*2.0*15.

### Rollback Considerations

Not applicable for EDP*2.0*15.

### Rollback Criteria

Not applicable for EDP*2.0*15.

### Rollback Risks

Not applicable for EDP*2.0*15.

### Authority for Rollback

Not applicable for EDP*2.0*15.

### Rollback Procedure

Not applicable for EDP*2.0*15.

### Rollback Verification Procedure

Not applicable for EDP*2.0*15.

- 0.2.1. **Print Transport Global** - This option will allow you to view the components of the KIDS build.

- 0.3.1. If prompted 'Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//', answer **NO** .