---
consolidated_title: "deployment, installation, back-out, and rollback guide"
app_code: MD
doc_type: installation-guide
master_source: "MD*1*85 Deployment, Installation, Back-Out, and Rollback Guide"
master_pub_date: February 2024
consolidated_from: 5 versions
prior_versions:
  - "MD*1*86 Deployment, Installation, Back-Out, and Rollback Guide"
  - "MD*1*87 Deployment, Installation, Back-Out, and Rollback Guide"
  - "MD*1*93 Deployment, Installation, Back-Out, and Rollback Guide"
  - "MD*1*95 Deployment, Installation, Back-Out, and Rollback Guide"
---

# Clinical Procedures (CP)

# CP User (MD*1.0*85)

# Deployment, Installation, Back-Out, and Rollback Guide (DIBORG)

<!-- image -->

February 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

**Revision History**

| Date    |   Version | Description              | Author                        |
|---------|-----------|--------------------------|-------------------------------|
| 2/2024  |       1.2 | Updated for MD*1.0*85 V2 | HPS Clinical Sustainment Team |
| 11/2023 |       1.1 | Updated for MD*1.0*85    | HPS Clinical Sustainment Team |
| 9/2018  |       1   | Initial Release          | HPS Clinical Sustainment Team |

**Artifact Rationale**

This document describes the Deployment, Installation, Back-out, and Rollback Guide for new products going into the VA Enterprise. The guide includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Guide is required to be completed prior to Critical Decision Point #2 (CD #2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

**Table of Contents**

1	Introduction	1

1.1	Purpose	1

1.2	Dependencies	1

1.3	Constraints	1

2	Roles and Responsibilities	2

3	Deployment	3

3.1	Timeline	3

3.2	Site Readiness Assessment	3

3.3	Resources	4

4	Installation	5

4.1	Pre-installation and System Requirements	5

4.2	Platform Installation and Preparation	5

4.3	Download and Extract Files	5

4.4	Database Creation	5

4.5	Installation Scripts	5

4.6	Cron Scripts	6

4.7	Access Requirements and Skills Needed for the Installation	6

4.8	Installation Procedure	6

4.9	Installation Verification Procedure	10

4.10	System Configuration	10

4.11	Database Tuning	11

5	Back-Out Procedure	11

5.1	Back-Out Strategy	11

5.2	Back-Out Considerations	11

5.3	Back-Out Criteria	11

5.4	Back-Out Risks	11

5.5	Authority for Back-Out	12

5.6	Back-Out Procedure	12

5.7	Back-out Verification Procedure	12

6	Rollback Procedure	13

6.1	Rollback Considerations	13

6.2	Rollback Criteria	13

6.3	Rollback Risks	13

6.4	Authority for Rollback	13

6.5	Rollback Procedure	13

6.6	Rollback Verification Procedure	13

**List of Tables**

Table 1: Roles and Responsibilities	2

Table 2: Files to be Downloaded	5

Table 3: HPS Clinical Sustainment Contacts	12

**List of Figures**

Figure 1: Shortcut Icon for Test CPUser v85	9

Figure 2: Test CPUser v85 Properties	10

### Introduction

This document describes how to deploy and install the CP User v1.0.85.2, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed commercial-off-the-shelf (COTS) product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

#### Purpose

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CP User v1.0.85.2 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

#### Dependencies

The CP User v1.0.85.2 project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system.

#### Constraints

CP User v1.0.85.2 and the associated MUMPS patch (if applicable) are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. CP User v1.0.85.2 utilizes existing, nationally released security controls to control access.

### Roles and Responsibilities

No one single entity oversees decision making for deployment, installation, back out and rollback of CP User v1.0.85.2. The Release Agent and Application Coordinators under the VIP will approve deployment and install from an OIT perspective. If an issue with the software arises, then the facility’s Chief Information Officer (CIO) and other site leadership will meet along with input from Patient Safety, Health Product Support (HPS), Information Technology (IT) Operations, and Services personnel, to initiate a back out and rollback decision of the software. The following table provides CP User v1.0.85.2 project information.

Table 1: Roles and Responsibilities

| Team                                                                                                                                                                                                                                                                                                  | Phase / Role    | Tasks                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|--------------------------------------------------------------------------------------------------------------------------------|
| IT Operations and Services personnel                                                                                                                                                                                                                                                                  | Deployment      | Plan and schedule deployment (including orchestration with vendors)                                                            |
| IT Operations and Services personnel                                                                                                                                                                                                                                                                  | Deployment      | Determine and document the roles and responsibilities of those involved in the deployment.                                     |
| Site personnel.                                                                                                                                                                                                                                                                                       | Deployment      | Test for operational readiness                                                                                                 |
| IT Operations and Services personnel  The IT support will need to include person(s) to install the Kernel Installation &amp; Distribution System (KIDS) build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix Access Gateway (CAG) | Deployment      | Execute deployment                                                                                                             |
| IT Operations and Services personnel.  The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the CAG                                                                        | Installation    | Plan and schedule installation                                                                                                 |
| N/A – will work under the VistA authority to operate (ATO) and security protocols.                                                                                                                                                                                                                    | Installation    | Ensure authority to operate and that certificate authority security documentation is in place                                  |
| N/A – no equipment is being added.                                                                                                                                                                                                                                                                    | Installation    | Validate through facility point of contact (POC) to ensure that IT equipment has been accepted using asset inventory processes |
| N/A – no new functionality is being introduced.                                                                                                                                                                                                                                                       | Installations   | Coordinate training                                                                                                            |
| Facility CIO, IT Operations, and Services personnel                                                                                                                                                                                                                                                   | Back-out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)            |
| Hardware and System support – no changes.  Software support will be the HPS Clinical Sustainment team.                                                                                                                                                                                                | Post Deployment | Hardware, Software, and System Support                                                                                         |

### Deployment

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release, the patch MD*1.0*85 will be released from the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing and deployment to production will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

#### Timeline

There is no specific timeline for deployment. This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period.

#### Site Readiness Assessment

This section discusses the locations that will receive the CP User v1.0.85.2 deployment.

#### 3.1.1	Deployment Topology (Targeted Architecture)

CP User Documentation v1.0.85.2 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the CAG.

#### 3.1.2	Site Information (Locations, Deployment Recipients)

The initial deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, CP User v1.0.85.2 (MD*1.0*85) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

Manchester VA Medical Center (Manchester, NH)

Minneapolis VA Health Care System (Minneapolis, MN)

#### 3.1.3	Site Preparation

There is no special preparation required for CP User v1.0.85.2. A fully patched VistA system is the only requirement.

#### Resources

N/A

#### 3.3.1	Facility Specifics

N/A

#### 3.3.2	Hardware

N/A

#### 3.3.3	Software

N/A

#### 3.3.4	Communications

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action item and National Change Order prior to the release of CP User v1.0.85.2 advising them of the upcoming release.

CP User v1.0.85.2 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch MD*1.0*85 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

### Installation

#### Pre-installation and System Requirements

CP User v1.0.85.2 assumes a fully-patched VistA system.

#### Platform Installation and Preparation

[VistA] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users should be off the system.

[GUI] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.)

#### Download and Extract Files

CP User v1.0.85.2 is being released as a PackMan Message distributed through the National Patch Module combined with a .ZIP file containing the GUI file(s).

Files can be obtained from the SOFTWARE directory:

https://download.vista.med.va.gov/index.html/SOFTWARE/

Documentation can also be found on the VA Software Documentation Library at:

https://www.va.gov/vdl/application.asp?appid=139

Table 2: Files to be Downloaded

| File Name       | File Contents                              | Download Format   |
|-----------------|--------------------------------------------|-------------------|
| MD_1_85.ZIP     | CP User v1.0.85.2 executable and help file | Binary            |
| MD_1_85_SRC.ZIP | CP User Source control files               | Binary            |

#### Database Creation

N/A

#### Installation Scripts

N/A

#### Cron Scripts

N/A

#### Access Requirements and Skills Needed for the Installation

Installation of CP User v1.0.85.2 requires the following to install:

Programmer access to VistA instance and ability to install KIDS build.

Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.

Network Share installs – access/ability to upload executable to the network share location.

Individual work-station installs – access/ability to push executable to required work stations.

#### Installation Procedure

#### 4.8.1	MD*1.0*85 VistA Installation

Choose the PackMan message containing this patch and select the INSTALL/CHECK MESSAGE PackMan option to load the KIDS patch into a Transport Global on your system.

From the Kernel Installation &amp; Distribution System Menu (KIDS), select the Installation menu:

1	Load a Distribution

2	Verify Checksums in Transport Global

3	Print Transport Global

4	Compare Transport Global to Current System

5	Backup a Transport Global

6	Install Package(s)

Restart Install of Package(s)

Unload a Distribution

From this menu, you must use the Backup a Transport Global option to create a back out message. When prompted for the INSTALL NAME enter the package name: MD*1.0*85

Also from this menu, you may elect to use the following options:

- Verify Checksums in Transport Global
- Print Transport Global
- Compare Transport Global to Current System

Select the Install Package(s) option and enter the package name: MD*1.0*85

When prompted, Want KIDS to INHIBIT LOGONs during the install? NO//, respond NO.

When prompted, Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//, respond NO.

#### 4.8.2	CP User v1.0.85.2 GUI Installation

The ZIP file contains the CP User GUI executable and help file. Download the ZIP file and extract all the files.

#### CP User documentation GUI Methods of Installation

The following methods of installation of CP User are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/Veterans Integrated Services Network (VISN) policies, Local Area Network (LAN) performance, or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

**Network (shared) installation:**

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPUser.exe) across the LAN.

The GUI executable (CPUser.exe), help file (CPUSER.chm) files are copied to a network shared location. Users are provided with a desktop shortcut to run CPUser.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the **Target** field of the shortcut properties.

At the time of a CP User version update the copy of CPUser.exe and the help file are replaced, on the network share, with the new version.

Any users requiring access to another site's CP User system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of CP User (e.g. for testing purposes) a different version of CPUser.exe can be placed in a separate network location and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

**Citrix installation:**

The GUI executable (CPUser.exe) and associated files are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary CAG infrastructure).

**Note:** For issues with CAG, please contact your local or national help desk.

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

**Local workstation installation:**

This is the “standard” method of installation where the GUI executable (CPUser **.exe** ) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via System Center Configuration Manager (SCCM). This is outside the scope of the Sustainment team. A National package (CP User v1.0.85.2) has been prepared and made available to Regional Contracting Officer’s Representative (COR) Client Technologies leadership.

**Manual install:**

This method is available for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.

1. Locate the MD\_1\_85.ZIP and unzip the file.
2. Copy the contents of the zip archive to a test directory, for example, C:\CPUser. You may need to create this new directory.

**Note:** You need to have a user with Administrator rights to the personal computer (PC) to complete these steps.

1. Create a Shortcut and name it, Test CP User v1\_85. This is to give the user another visual cue that this is not the normal CP User icon.

Figure 1: Shortcut Icon for Test CPUser v85

<!-- image -->

1. Determine the Domain Name System (DNS) server name or Internet Protocol (IP) address for the appropriate VistA server.
2. Determine the Broker RPC port for the VistA account.
3. Enter IP (or DNS name) and RPC port in the Target field of the Shortcut properties or use ServerList.exe (which launches a selection screen for various servers and ports defined).
4. CP User has been updated to accept a parameter "showcerts" in the desktop shortcut for the application. When this parameter is present, the application with display a prompt allowing users to select the correct certificate and then they will be prompted for their PIV card PIN.

Figure 2: Test CPUser v85 Properties

<!-- image -->

**Note:** The server and port number shown above are for example only.

#### 4.9	Installation Verification Procedure

[VISTA] Verify the checksum of routine MDPOST85 is equal to the checksum listed in the patch description.

[GUI] Launch the CP User GUI and verify the splash screen now announces that you are running Version: 1.0 and Patch: MD*1.0*85.

#### 4.10	System Configuration

N/A

#### 4.11	Database Tuning

N/A

### Back-Out Procedure

#### Back-Out Strategy

[VistA] In Section 0 (step 3) the individual installing the patch used option [Backup a Transport Global] to create a PackMan message that will revert the CP User components to their pre-v1.0.85.2 state. This includes everything transported in the MD*1.0*84 (CP User v1.0.84.1) build. If for any reason that PackMan Message cannot be located, contact HPS Sustainment: Clinical (see Section 5.6).

[GUI] To revert the CP User GUI, the v1.0.84.1 GUI will have to be redistributed.

#### Back-Out Considerations

#### 5.2.1	User Acceptance Testing

User acceptance testing was conducted by the test sites listed in Section 0.

The sites followed the provided test plan and executed the test cases according to the plan for the MD*1.0*85 build. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to the HPS Clinical Sustainment team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

#### Back-Out Criteria

Back-out will only be considered if there is a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.

#### Back-Out Risks

Backing out CP User v1.0.85.2 would result in the re-instatement of the issues addressed in CP User v1.0.84.1.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

#### Authority for Back-Out

The Area Manager has the final authority to require the rollback and accept the associated risks.

#### Back-Out Procedure

These steps assume that the only reason to consider a back-out for CP User v1.0.85.2 is in the event of a catastrophic failure.

Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with CP User v1.0.85.2. Use the following contacts:

Table 3: HPS Clinical Sustainment Contacts

| Name & Title               | Email    | Telephone Number   |
|----------------------------|----------|--------------------|
| REDACTED  Project Manager  | REDACTED | REDACTED           |
| REDACTED  Technical Leader | REDACTED | REDACTED           |

1. If the decision is made to proceed with back-out and rollback, the HPS Sustainment Clinical team will be available to assist sites that have misplaced their backup PackMan message, as well as give you the instructions for downloading the executable.

[VistA]

Open the Backup MailMan Message.

At the **Enter message action (in IN basket): Ignore//** prompt, enter **X** for [Xtract PackMan].

At the **Select PackMan function:** prompt, select [INSTALL/CHECK MESSAGE]. The old routine is now restored.

[GUI] Coordinate with the appropriate IT support, local and regional, to schedule the time to install MD*1.0*84 and to push out/install the previous GUI executable.

Once MD*1.0*84 and CP User v1.0.84.1 have been installed, verify operations before making available to all staff.

#### Back-out Verification Procedure

1. Ensure the CP User v1.0.84.1 executable launches properly.

1. Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.
### Rollback Procedure

#### Rollback Considerations

No load testing was performed on CP User v1.0.85.2. This was a maintenance release to correct defects discovered in CP User v1.0.84.1. There was no additional functionality included.

#### Rollback Criteria

Refer to Section 5.3 for criteria that would require a rollback of this patch.

#### Rollback Risks

Backing out CP User v1.0.85.2 would result in the re-instatement of the issues addressed in CP User v1.0.84.1.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

#### Authority for Rollback

The Facility CIO has the final authority to require the rollback and accept the associated risks.

#### Rollback Procedure

Included in the VistA patch, there is a post-install routine, MDPOST85. This routine contains a rollback section called ROLLBACK. If for some reason it is deemed necessary to back out this patch, simply executing that section of the routine, D ROLLBACK^MDPOST85 will reset the version information needed for the previous release of CP User, which is MD*1.0*84.

#### Rollback Verification Procedure

Ensure the CP User v1.0.84.1 executable launches properly.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: MD*1*87 Deployment, Installation, Back-Out, and Rollback Guide

## Clinical Procedures (CP) Flowsheets Patch (MD*1.0*87) Network Deployment, Installation, Back-Out, and Rollback Guide

<!-- image -->

May 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

**Revision History**

| **Date**   | **Description**   | **Author**                    |
|------------|-------------------|-------------------------------|
| May 2024   | Initial Release   | HPS Clinical Sustainment Team |

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect these procedures at a single or at multiple locations.

Per the Veteran-focused Integrated Process (VIP) Guide, the Deployment, Installation, Back-out, and Rollback Plan is required to be completed prior to Critical Decision Point #2 (CD #2), with the expectation that it will be updated throughout the lifecycle of the project for each build, as needed.

Con

1.	Introduction	5

1.2.	Purpose	5

1.3.	Dependencies	5

1.4.	Constraints	5

2.	Roles and Responsibilities	5

3.	Deployment	7

3.1.	Timeline	7

3.2.	Site Readiness Assessment	7

3.3.	Resources	8

4.	Installation	8

4.1.	Pre-installation and System Requirements	8

4.2.	Platform Installation and Preparation	9

4.3.	Download and Extract Files	9

4.4.	Database Creation	9

4.5.	Installation Scripts	9

4.6.	Cron Scripts	9

4.7.	Access Requirements and Skills Needed for the Installation	9

4.8.	Installation Procedure	10

4.9.	Installation Verification Procedure	13

4.10.	System Configuration	13

4.11.	Database Tuning	13

5.	Back-Out Procedure	14

5.1.	Back-Out Strategy	14

5.2.	Back-Out Considerations	14

5.3.	Back-Out Criteria	14

5.4.	Back-Out Risks	14

5.5.	Authority for Back-Out	15

5.6.	Back-Out Procedure	15

5.7.	Back-out Verification Procedure	15

6.	Rollback Procedure	16

6.1.	Rollback Considerations	16

6.2.	Rollback Criteria	16

6.3.	Rollback Risks	16

6.4.	Authority for Rollback	16

6.5.	Rollback Procedure	16

6.6.	Rollback Verification Procedure	16

########### 1 tents

**List of Figures**

**Figure 1: How to Create Shortcut	12**

**Figure 2: CP Flowsheets Shortcut Properties	13**

**List of Tables**

**Table 1: Roles and Responsibilities	6**

**Table 2: Files to be Downloaded	9**

**Table 3: HSP Clinical Sustainment Contacts	15**

### Introduction

This document describes how to deploy and install the CP Flowsheets v1.0.87.1, as well as how to back-out the product and rollback to a previous version or data set. This document is a companion to the project charter and management plan for this effort. In cases where a non-developed COTS product is being installed, the vendor provided User and Installation Guide may be used, but the Back-Out Recovery strategy still needs to be included in this document.

#### Purpose

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CP Flowsheets v1.0.87.1 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

#### Dependencies

The CP Flowsheets v1.0.87.1 project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system.

#### Constraints

CP Flowsheets v1.0.87.1 and the associated M patch (if applicable) are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. CP Flowsheets v1.0.87.1 utilizes existing, nationally released security controls to control access.

### Roles and Responsibilities

No one single entity oversees decision making for deployment, installation, back out and rollback of CP Flowsheets v1.0.87.1. The Release Agent and Application Coordinators under the Veterans in Process will approve deployment and install from an OIT perspective. If an issue with the software arises, then the facility CIO and other site leadership will meet along with input from Patient Safety and Health Product Support to initiate a back out and rollback decision of the software along with the IT Operations and Services personnel. The following table provides CP Flowsheets v1.0.87.1 project information.

Table 1: Roles and Responsibilities

| **Team**                                                                                                                                                                                                                                        | **Phase/Role**   | **Tasks**                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|---------------------------------------------------------------------------------------------------------------------|
| IT Operations and Services personnel                                                                                                                                                                                                            | Deployment       | Plan and schedule deployment                                                                                        |
| IT Operations and Services personnel                                                                                                                                                                                                            | Deployment       | Determine and document the roles and responsibilities of those involved in the deployment.                          |
| Site personnel.                                                                                                                                                                                                                                 | Deployment       | Test for operational readiness                                                                                      |
| **Team**                                                                                                                                                                                                                                        | **Phase/Role**   | **Tasks**                                                                                                           |
| IT Operations and Services personnel The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway  | Deployment       | Execute deployment                                                                                                  |
| IT Operations and Services personnel. The IT support will need to include person(s) to install the KIDS build as well as the personnel to deploy the GUI – which may be done on each machine, a shared network and/or the Citrix access gateway | Installation     | Plan and schedule installation                                                                                      |
| N/A – will work under the VistA ATO and security protocols.                                                                                                                                                                                     | Installation     | Ensure authority to operate and that certificate authority security documentation is in place                       |
| N/A – no equipment is being added.                                                                                                                                                                                                              | Installation     | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes         |
| N/A – no new functionality is being introduced.                                                                                                                                                                                                 | Installations    | Coordinate training                                                                                                 |
| Facility CIO, IT Operations, and Services personnel                                                                                                                                                                                             | Back-out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out) |
| Hardware and System support – no changes.  Software support will be the HPS Clinical Sustainment team.                                                                                                                                          | Post  Deployment | Hardware, Software and System Support                                                                               |

### Deployment

The deployment is planned as a standard VistA National Patch Module patch rollout. Once approval has been given to nationally release, the patch MD*1*87 will be released from the National Patch Module. At this point, it will be available for installation and deployment at all sites.

Scheduling of test/mirror installs, testing and deployment to production will be at the site’s discretion. It is anticipated there will be a 30-day compliance period.

#### Timeline

There is no timeline specifically for deployment. This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period for the release.

#### Site Readiness Assessment

N/A.

3.2.1	Deployment Topology (Targeted Architecture)

CP Flowsheets v1.0.87.1 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway.

#### Site Information (Locations, Deployment Recipients)

The initial deployment will be to IOC sites for verification of functionality. Once that testing is completed and approval is given for national release, CP Flowsheets v1.0.87.1 (MD*1*87) will be deployed to all VistA systems. The Production (IOC) testing sites are:

•	Edward Hines Jr. VA Hospital (Hines, IL)

•	VA Maryland Health Care System (Perry Point, MD)

**3.2.3** Site Preparation

There is no special preparation required for CP Flowsheets v1.0.87.1. A fully patched VistA system is the only requirement.

#### Resources

N/A

#### Facility Specifics

N/A

#### Hardware

N/A

#### Software

N/A

#### Communications

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action Item and National Change Order prior to the release of CP Flowsheets v1.0.87.1 advising them of the upcoming release.

CP Flowsheets v1.0.87.1 will be deployed using the standard method of patch release from the

National Patch Module rather than a phased deployment. When patch MD*1*87 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

6.3.7.1	Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

### Installation

#### Pre-installation and System Requirements

CP Flowsheets v1.0.87.1 assumes a fully patched VistA system.

#### Platform Installation and Preparation

[VistA] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

[GUI] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.)

#### Download and Extract Files

CP User v1.0.87.1 is being released as a PackMan Message distributed through the National Patch Module combined with a .ZIP file containing the GUI file(s).

Files can be obtained from the SOFTWARE directory:

[https://download.vista.med.va.gov/index.html/SOFTWARE/](https://download.vista.med.va.gov/index.html/SOFTWARE/)

Documentation can also be found on the VA Software Documentation Library at:

[https://www.va.gov/vdl/application.asp?appid=139](https://www.va.gov/vdl/application.asp?appid=139)

Table 2: Files to be Downloaded

| **File Name**   | **File Contents**                      | **Download Format**   |
|-----------------|----------------------------------------|-----------------------|
| MD_1_87.ZIP     | CP Flowsheets executable and help file | Binary                |

#### Database Creation

N/A

#### Installation Scripts

N/A

#### Cron Scripts

N/A

#### Access Requirements and Skills Needed for the Installation

Installation of CP Flowsheets v1.0.87.1 requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual workstation installs – access/ability to push executable to required workstations.

#### Installation Procedure

#### MD*1*87 VistA Installation

1. Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2. Select Kernel Installation &amp; Distribution System Option: Installation

1	Load a Distribution

2	Verify Checksums in Transport Global

3	Print Transport Global

4	Compare Transport Global to Current System

5	Backup a Transport Global

6	Install Package(s)

Restart Install of Package(s)

Unload a Distribution

1. From this menu, elect to use the following options:

- Compare Transport Global to Current System
- Verify Checksums in Transport Global

2. Use the Install Package(s) options and select the package MD*1*87
3. When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
4. When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols?

NO//’, respond NO.

#### CP Flowsheets v1.0.87.1 GUI Installation

The ZIP file (MD\_1\_87.ZIP) contains the CP Flowsheets GUI executable and associated files. Download the ZIP file and extract all the files.

**CP Flowsheets GUI Methods of Installation**

The following methods of installation of CP Flowsheets are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

**Network (Shared) Installation:**

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPFlowsheets.exe) across the LAN.

The GUI executable (CPFlowsheets.exe) and help file (CPFlowsheets.chm) are copied to a network shared location. Users are provided with a desktop shortcut to run CPFlowsheets.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the “Target” field of the shortcut properties.

At the time of a CP Flowsheets version update, the copy of CPFlowsheets.exe and the help file are replaced, on the network share, with the new version.

Any users requiring access to another site's CP Flowsheets system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of CP Flowsheets (e.g. for testing purposes) a different version of CPFlowsheets.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

**Citrix Installation:**

The GUI executable (CPFlowsheets.exe) and associated files are installed and ran from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

> **NOTE:** For issues with CAG, please contact the local or national help desk.

**Local Workstation Installation:**

This is the “standard” method of installation where the GUI executable (CPFlowsheets.exe) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via SCCM. This is outside the scope of the Sustainment team. A National package (Clinical Procedures Flowsheets v1.0.87.1) has been prepared and made available to Regional COR Client Technologies leadership.

**Manual Install:**

This method is used for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or users who need to have access to a pre-production (mirror) VistA instance.

1. Locate the MD\_1\_87.ZIP and unzip the file.
2. Copy the contents of the zip archive to a directory appropriate for programs. For example: C:\Program Files (x86)\Vista\CP Flowsheets. A new directory may need to be created.

**Note:** Administrator rights are required to complete these steps.

1. Create a Shortcut and name it “CP Flowsheets”. This can be done by using Windows Explorer to navigate to the file location of CP Flowsheets.exe, right Clicking on the file and choosing [Send to] &gt; [Desktop (Create Shortcut)]

Figure 1: How to Create Shortcut

<!-- image -->

1. Determine the DNS server name or IP address for the appropriate VistA server.
2. Determine the Broker RPC port for the VistA account.
3. Right click on the newly created Shortcut and select Properties. Enter “s=” IP (or DNS name) and “p=” RPC port in the Target field (or use ServerList.exe).
4. CP Flowsheets has been updated to accept a parameter "showcerts" in the desktop shortcut for the application. When this parameter is present, the application with display a prompt allowing users to select the correct certificate and then they will be prompted for their PIV card PIN.

Figure 2: CP Flowsheets Shortcut Properties

<!-- image -->

> **NOTE:** The server and port number shown above are for example only.

#### Installation Verification Procedure

[VISTA] After installing the VistA side patch, attempt the GUI verification. If the VistA side installed properly there will be no version error upon trying to open the application.

[GUI] Launch the CP Flowsheets GUI and verify the splash screen announces running version 1.0.87.1

#### System Configuration

N/A

#### Database Tuning

N/A

### Back-Out Procedure

#### Back-Out Strategy

[VistA] This patch only has one pre-install routine which should be deleted after install. To back out the change requires manually reverting the version check parameter to the previous GUI version “1.0.76.2”

[GUI] To revert to the CP Flowsheets GUI, the 1.0.76.2 GUI would have to be redistributed.

#### Back-Out Considerations

#### Load Testing

No load testing was performed on CP Flowsheets v1.0.87.1. This was a maintenance release to correct defects discovered in CP Flowsheets v1.0.76.2. There is no additional functionality included.

#### User Acceptance Testing

User acceptance testing was conducted by the test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of MD*1*87. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. Any issues were reported back to the development team and were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

#### Back-Out Criteria

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.

#### Back-Out Risks

Backing out CP Flowsheets v1.0.87.1 would result in the re-instatement of the issues addressed in CP Flowsheets v1.0.87.1.

The back-out process would significantly impact patient care due to the interruption. Therefore, the back-out process should only be performed in an emergency situation.

#### Authority for Back-Out

The Area Manager has the final authority to require the rollback and accept the associated risks.

#### Back-Out Procedure

These steps assume that the only reason to consider a back-out for CP Flowsheets v1.0.87.1 is in the event of a catastrophic failure.

Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with CP Flowsheets v1.0.87.1. Use the following contacts:

Table 3: HSP Clinical Sustainment Contacts

| **Name &amp; Title**       | **Email**   | **Telephone Number**   |
|----------------------------|-------------|------------------------|
| REDACTED  Project Manager  | REDACTED    | REDACTED               |
| REDACTED  Technical Leader | REDACTED    | REDACTED               |

If the decision is made to proceed with back-out and rollback, the HPS Clinical Sustainment team be available to assist sites.

1. Navigate in VistA to the XPAR EDIT PARAMETER option
2. At the Select PARAMETER DEFINITION NAME: prompt, enter MD PARAMETERS
3. At the Select Enter selection: prompt, enter SYSTEM
4. At the Select Parameter Name: prompt, enter VERSION\_CPFLOWSHEETS
5. At the Parameter Name: prompt, hit the enter key to accept the default
6. At the Parameter Value: prompt, enter 1.0.76.2
7. [GUI] Coordinate with the appropriate IT support, local and regional, to schedule the time to push out and install the previous GUI executable.
8. Once CP Flowsheets v1.0.76.2 have been installed, verify operations before making available to all staff.

#### Back-out Verification Procedure

1. Ensure the v1.0.76.2 executable launches properly.
2. Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

### Rollback Procedure

#### Rollback Considerations

N/A

#### Rollback Criteria

N/A

#### Rollback Risks

N/A

#### Authority for Rollback

The Facility CIO has the final authority to require the rollback and accept the associated risks.

#### Rollback Procedure

Back-out will automatically rollback version.

#### Rollback Verification Procedure

N/A

### From: MD*1*95 Deployment, Installation, Back-Out, and Rollback Guide

### Purpose

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the CP Gateway v1.0.95.1 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

### Dependencies

The CP Gateway v1.0.95.1 project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system.

### Constraints

CP Gateway v1.0.95.1 and the associated MUMPS patch (if applicable) are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. CP Gateway v1.0.95.1 utilizes existing, nationally released security controls to control access.

### Timeline

There is no specific timeline for deployment. This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period.

### Site Readiness Assessment

This section discusses the locations that will receive the CP Gateway v1.0.95.1 deployment.

#### Deployment Topology (Targeted Architecture)

CP Gateway Documentation v1.0.95.1 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the CAG.

#### Site Information (Locations, Deployment Recipients)

The initial deployment will be to initial operating capability (IOC) sites for verification of functionality. Once that testing is completed and approval is given for national release, CP Gateway v1.0.95.1 (MD*1.0*95) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

Robley Rex VA Medical Center (Louisville, KY)

Fort Harrison VA Medical Center (Fort Harrison, MT)

#### Site Preparation

There is no special preparation required for CP Gateway v1.0.95.1. A fully patched VistA system is the only requirement.

### Resources

N/A

#### Facility Specifics

N/A

#### Hardware

N/A

#### Software

N/A

#### Communications

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action item and National Change Order prior to the release of CP Gateway v1.0.95.1 advising them of the upcoming release.

CP Gateway v1.0.95.1 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch MD*1.0*95 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

### Pre-installation and System Requirements

CP Gateway v1.0.95.1 assumes a fully-patched VistA system.

### Platform Installation and Preparation

[VistA] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users should be off the system.

[GUI] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.)

### Download and Extract Files

CP Gateway v1.0.95.1 is being released as a PackMan Message distributed through the National Patch Module combined with a .ZIP file containing the GUI file(s).

Files can be obtained from the SOFTWARE directory:

[https://download.vista.med.va.gov/index.html/SOFTWARE/](https://download.vista.med.va.gov/index.html/SOFTWARE/)

Documentation can also be found on the VA Software Documentation Library at:

[https://www.va.gov/vdl/application.asp?appid=139](https://www.va.gov/vdl/application.asp?appid=139)

Table 2: File to be Downloaded

| ## File Name  ## 5 Back-Out Procedure  ### 5.1 Back-Out Strategy  [VistA] In Section 4.8.1 (step 3) the individual installing the patch used option [Backup a Transport Global] to create a PackMan message that will revert the CP Gateway components to their pre-v1.0.95.1 state. This includes everything transported in the MD*1.0*95 (CP Gateway v1.0.95.1) build. If for any reason that PackMan Message cannot be located, contact HPS Sustainment: Clinical (see Section 5.6).  [GUI] To revert the CP Gateway GUI, the v1.0.20.4 GUI will have to be redistributed.  ### 5.2 Back-Out Considerations  #### 5.2.1 User Acceptance Testing  User acceptance testing was conducted by the test sites listed in Section 3.2.2.  The sites followed the provided test plan and executed the test cases according to the plan for the MD*1.0*95 build. The sites either passed or failed any item based on testing. The tests were performed by users at each site who are familiar with using the application. The test cases were then delivered to the HPS Clinical Sustainment team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.  ### 5.3 Back-Out Criteria  Back-out will only be considered if there is a catastrophic failure that causes loss of function for the application and/or a significant patient safety issue.  ### 5.4 Back-Out Risks  Backing out CP Gateway v1.0.95.1 would result in the re-instatement of the issues addressed in CP Gateway v1.0.20.4.  In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.  ### 5.5 Authority for Back-Out  The Area Manager has the final authority to require the rollback and accept the associated risks.  ### 5.6 Back-Out Procedure  These steps assume that the only reason to consider a back-out for CP Gateway v1.0.95.1 is in the event of a catastrophic failure.  Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with CP Gateway v1.0.95.1. Use the following contacts:  Table 3: HPS Clinical Sustainment Contacts  Name & Title Email Telephone Number Redacted Project Manager Redacted Redacted Redacted Technical Leader Redacted Redacted  1. If the decision is made to proceed with back-out and rollback, the HPS Sustainment Clinical team will be available to assist sites that have misplaced their backup PackMan message, as well as give you the instructions for downloading the executable.  [VistA]  Open the Backup MailMan Message.  At the **Enter message action (in IN basket): Ignore//** prompt, enter **X** for [Xtract PackMan].  At the **Select PackMan function:** prompt, select [INSTALL/CHECK MESSAGE]. The old routine is now restored.  [GUI] Coordinate with the appropriate IT support, local and regional, to schedule the time to install MD*1.0*20 and to push out/install the previous GUI executable.  Once MD*1.0*20 and CP Gateway v1.0.20.4 have been installed, verify operations before making available to all staff.  ### 5.7 Back-out Verification Procedure  1. Ensure the CP Gateway v1.0.20.4 executable launches properly.  1. Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.  ## 6 Rollback Procedure  ### 6.1 Rollback Considerations  No load testing was performed on CP Gateway v1.0.95.1. This was a maintenance release to correct defects discovered in CP Gateway v1.0.20.4. and to upgrade the application to a TRM compliant Delphi Version. There was no additional functionality included.  ### 6.2 Rollback Criteria  Refer to Section 5.3 for criteria that would require a rollback of this patch.  ### 6.3 Rollback Risks  Backing out CP Gateway v1.0.95.1 would result in the re-instatement of the issues addressed in CP Gateway v1.0.20.4.  In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.  ### 6.4 Authority for Rollback  The Facility CIO has the final authority to require the rollback and accept the associated risks.  ### 6.5 Rollback Procedure  To reset the Vista portion of the software, execute D EN^MDPOST20 which will reset the version information needed for the previous release of CP Gateway, which is MD*1.0*20. Redistribute the previous executable GUI application for CP Gateway v1.0.20.4.  ### 6.6 Rollback Verification Procedure  Ensure the CP Gateway v1.0.20.4 executable launches properly.   | File Contents                   | Download Format   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------|-------------------|
| MD_1_95.ZIP                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | CP Gateway v1.0.95.1 executable | Binary            |

### Database Creation

N/A

### Installation Scripts

N/A

### Cron Scripts

N/A

### Access Requirements and Skills Needed for the Installation

Installation of CP Gateway v1.0.95.1 requires the following to install:

Programmer access to VistA instance and ability to install KIDS build.

Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.

Network Share installs – access/ability to upload executable to the network share location.

Individual workstation installs – access/ability to push executable to required work stations.

### Installation Procedure

#### MD*1.0*95 VistA Installation

Choose the PackMan message containing this patch and select the INSTALL/CHECK MESSAGE PackMan option to load the KIDS patch into a Transport Global on your system.

From the Kernel Installation &amp; Distribution System Menu (KIDS), select the Installation menu:

1	Load a Distribution

2	Verify Checksums in Transport Global

3	Print Transport Global

4	Compare Transport Global to Current System

5	Backup a Transport Global

6	Install Package(s)

Restart Install of Package(s)

Unload a Distribution

From this menu, you must use the Backup a Transport Global option to create a back out message. When prompted for the INSTALL NAME enter the package name: MD*1.0*95

Also from this menu, you may elect to use the following options:

- Verify Checksums in Transport Global
- Print Transport Global
- Compare Transport Global to Current System

Select the Install Package(s) option and enter the package name: MD*1.0*95

When prompted, Want KIDS to INHIBIT LOGONs during the install? NO//, respond NO.

When prompted, Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//, respond NO.

#### CP Gateway v1.0.95.1 GUI Installation

The ZIP file contains the CP Gateway GUI executable. Download the ZIP file and extract the file.

#### CP Gateway documentation GUI Methods of Installation

The following methods of installation of CP Gateway are available. Sites' choice of which method(s) to use will depend upon IT Operations and Services personnel/Veterans Integrated Services Network (VISN) policies, Local Area Network (LAN) performance, or other local circumstances. User requirements, physical location, and methods of connection to the VA network may warrant more than one of the options below to be used.

Network (shared) installation:

This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (CPGateway.exe) across the LAN.

The GUI executable (CPGateway.exe) file is copied to a network shared location. Users are provided with a desktop shortcut to run CPGateway.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the **Target** field of the shortcut properties.

To enable the use of Windows Certificates as part of the authentication procedure on launch of the application, add **/showcerts** as a parameter to the executable in the **Target** field. ( **cpgateway.exe /showcerts** )

To disable the purge process for the duration of the application’s running session, add **/nopurge** as a parameter to the executable in the **Target** field. ( **cpgateway.exe /nopurge** ) **.**

The two new parameters, **/showcerts** and **/nopurge** can be used in any combination. Their behaviors are independent of each other.

At the time of a CP Gateway version update the copy of CPGateway.exe is replaced, on the network share, with the new version.

Any users requiring access to another site's CP Gateway system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

If a user requires access to an older or newer version of CP Gateway (e.g. for testing purposes) a different version of CPGateway.exe can be placed in a separate network location and the user can be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

Citrix installation:

The GUI executable (CPGateway.exe) and associated files are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary CAG infrastructure).

**Note:** For issues with CAG, please contact your local or national help desk.

For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

Local workstation installation:

This is the “standard” method of installation where the GUI executable (CPGateway **.exe** ) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via System Center Configuration Manager (SCCM). This is outside the scope of the Sustainment team. A National package (CP Gateway v1.0.95.1) has been prepared and made available to Regional Contracting Officer’s Representative (COR) Client Technologies leadership.

Manual install:

This method is available for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or need to have access to a pre-production (mirror) VistA instance.

1. Locate the MD\_1\_95.ZIP and unzip the file.
2. Copy the contents of the zip archive to a test directory, for example, C:\CPGateway. You may need to create this new directory.

**Note:** You need to have a user with Administrator rights to the personal computer (PC) to complete these steps.

1. Create a Shortcut and name it, Test CP Gateway v1\_95. This is to give the user another visual cue that this is not the normal CP Gateway icon.
<!-- image -->

Figure 1: Shortcut Icon for Test CPGateway v95

1. Determine the Domain Name System (DNS) server name or Internet Protocol (IP) address for the appropriate VistA server.
2. Determine the Broker RPC port for the VistA account.
3. Enter IP (or DNS name) and RPC port in the **Target** field of the Shortcut properties or use ServerList.exe (which launches a selection screen for various servers and ports defined).

<!-- image -->

Figure 2: Test CPGateway v95 Properties

**Note:** The server and port number shown above are for example only.

### Installation Verification Procedure

[VISTA] Verify the checksum of routine MDPOST95 is equal to the checksum listed in the patch description.

[GUI] Launch the CP Gateway GUI and verify the splash screen now announces that you are running Version: 1.0 and Patch: MD*1.0*95.

### System Configuration

N/A

### Database Tuning

N/A
