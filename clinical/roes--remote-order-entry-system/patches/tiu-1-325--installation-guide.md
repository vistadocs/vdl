---
title: TIU*1*325 DIBR
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: DIBR
app_code: ROES
app_name: Remote Order Entry System
section: CLI
app_status: active
pkg_ns: TIU
patch_ver: 1
patch_id: TIU*1*325
group_key: "ROES:TIU:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - roes
  - deployment
  - production
  - back
  - vista
  - messages
  - span
  - link
page_count: 0
word_count: 4116
section_count: 29
table_count: 4
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: June 2019
revision_count: 2
revision_newest: 06/04/2019
revision_oldest: 04/15/2019
docx_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/tiu_1_p325_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Remote_Order_Entry_Sys_(ROES)/tiu_1_p325_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=99"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>InterSystems Health Connect (HC) / Remote Order Entry System (ROES)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](tiu-1-325-dibr/001.png)

June 2019

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

<span id="_Toc57617384" class="anchor"></span>Revision History

| Date       | Revision | Description                           | Author                             |
|------------|----------|---------------------------------------|------------------------------------|
| 06/04/2019 | 0.2      | Added VistA steps details in Appendix | <span class="mark">REDACTED</span> |
| 04/15/2019 | 0.1      | Original Version                      | <span class="mark">REDACTED</span> |

<span id="_Ref520206071" class="anchor"></span>Table 1: Roles and Responsibilities

Table of Contents

<span id="_Toc57617385" class="anchor"></span>List of Figures

<span id="_Toc57617386" class="anchor"></span>List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Pre-Rollout Steps](#pre-rollout-steps)
  - [Deployment Steps](#deployment-steps)
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
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Import Files](#download-and-import-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
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
  - [Back-Out Tasks](#back-out-tasks)
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
- [Appendices](#appendices)
  - [Appendix A – HC Production Namespace Configuration and Deployment](#appendix-a-hc-production-namespace-configuration-and-deployment)
    - [Creating a New Namespace](#creating-a-new-namespace)
    - [Deploying a Health Connect Production](#deploying-a-health-connect-production)
  - [Appendix B – Starting and Stopping a HC Production](#appendix-b-starting-and-stopping-a-hc-production)
    - [Starting Health Connect Production](#starting-health-connect-production)
    - [Stopping HC Production](#stopping-hc-production)
  - [Appendix C – Redirection of Logical Links in VistA](#appendix-c-redirection-of-logical-links-in-vista)
This document describes the deployment, installation, back-out, and rollback instructions for the migration of Health Level Seven (HL7) messages from the Vitria Interface Engine (VIE) to InterSystems Health Connect (HC). The scope of this document is messages from the Remote Order Entry System (ROES) to Veterans Information System Technology Architecture (VistA).
HC will replace VIE which is currently in production for the routing of these messages.
This document provides clients, stakeholders, and support personnel with a smooth transition to HC. It describes how to deploy and install the HC in production as well as how to back out the product to the previous version.
![](tiu-1-325-dibr/002.png) NOTE: In cases where you are installing a commercial-off-the-shelf (COTS) product, you can use the vendor-provided user guide and installation guide. However, if those guides do *not* include a back-out recovery and rollback strategy, you *must* retain that information in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom HC will be deployed and installed; as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, communications plan, and rollout schedule. Specific instructions for deployment, installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIE supports the routing of messages among several applications. The HC product will ultimately be replacing VIE. During the transition phase both products will be running concurrently.

The success of HC as the messaging solution relies upon the availability of the VistA site administrators performing their part of the deployment in each VistA instance in a timely manner.

The installation of the shared Enterprise and Regional HC instances is not within the scope of this deployment, which is dependent upon those instances being installed, configured, and running in production.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HC is an approved product as per the VA’s Technical Reference Model (TRM).

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table outlines the roles and responsibilities:

| ID  | Team                                     | Phase / Role    | Tasks                                                                                                                | Project Phase (See Schedule) |
|-----|------------------------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------|------------------------------|
|     | FM24 Project Management Office (PMO)     | Deployment      | Plan and schedule deployment (including orchestration with vendors).                                                 |                              |
|     |                                          |                 | Determine and document the roles and responsibilities of those involved in the deployment.                           |                              |
|     | HC Operations                            | Deployment      | Test for operational readiness.                                                                                      |                              |
|     | Site and VistA Operations                | Deployment      | Execute deployment, including switch of logical links to HC.                                                         |                              |
|     | HC Operations                            | Installation    | Plan and schedule installation.                                                                                      |                              |
|     |                                          |                 | Ensure authority to operate and that certificate authority security documentation is in place.                       |                              |
|     | InterSystems                             | Installations   | Coordinate training as appropriate.                                                                                  |                              |
|     | Development                              | Back-Out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out). |                              |
|     | HC Operations/ Development/ InterSystems | Post Deployment | Hardware, Software, and System Support.                                                                              |                              |

<span id="_Ref8291712" class="anchor"></span>Table 2: Site Preparation

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 1</u> depicts the current VIE architecture for ROES messages:

<span id="_Ref510009935" class="anchor"></span>Figure 1: Current VIE Architecture for ROES

![](tiu-1-325-dibr/003.png)

The ROES message migration will be implemented in a one-time deployment of the ROES redirection to Health Connect Enterprise, and a rapid deployment of VistA site TIU acknowledgements redirection to Health Connect Regional.

## Pre-Rollout Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HealthShare HC Application Support/Operations team performs the following pre-rollout steps:

1.  Submit firewall requests to ensure connectivity in <u>production</u>:
1.  From VistA sites to HC Regional instances
2.  From HC Regional Instances to HC Enterprise
3.  From ROES Enterprise to HC Enterprise
2.  Perform line-of-site testing for each of the sub-items in Step 1 once the network team indicates the firewall configurations have been completed.
3.  Execute the following Structured Query Language (SQL) statement in the Enterprise and each Regional namespace before deploying the Ensemble files to ensure the deployment won’t overwrite or remove the existing settings:

    update Ens_Config.DefaultSettings set Deployable=0
4.  Install the ROES production files onto the Enterprise HC Instance. All Inbound Services and Outbound Operations will be disabled.
5.  Install the appropriate production files on each of the Regional HC instances. All Inbound Services and Outbound Operations will be enabled.
6.  Repeat the SQL statement in the Enterprise and each Regional namespace after deploying the Ensemble files:

    update Ens_Config.DefaultSettings set Deployable=0

## Deployment Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step of the deployment will be for the ROES team to redirect outbound messages (to VistA sites) from VIE, to the Health Connect Enterprise as depicted in <u>Figure 2</u>.

> <span id="_Ref2328976" class="anchor"></span>Figure 2: Deployment Step 1

![](tiu-1-325-dibr/004.png)

To implement the flow of messages from ROES to VistA sites:

1.  Enable the HC Enterprise Inbound Service (From_ROES_VISTA_7650) to accept messages from the enterprise ROES system.
2.  The ROES team will update the logical link currently pointing to VIE, and redirect it to the Health Connect Enterprise instance. IP and port will be provided separately.
3.  Enable the HC Enterprise Outbound Operations to send messages to the Regional Health Connect instances:
    1.  To_VISTAR1DVR_ROES_7651
    2.  To_VISTAR1SAC_ROES_7651
    3.  To_VISTAR2_ROES_7651
    4.  To_VISTAR3_ROES_7651
    5.  To_VISTAR4BYN_ROES_7651
    6.  To_VISTAR4PITC_ROES_7651
4.  Enable the HC Regional Inbound Service From_ROES_VISTA_7651 for each region.
5.  The ROES and Health Connect teams will monitor message flows to ensure delivery and responses.

At this point, messages flowing from ROES to VistA sites are flowing through Health Connect, and no longer using the VIE network. The next major step will be to release the VistA patch TIU\*1\*325, which will be an informational patch to redirect the VistA Logical Link (TIUACKROES) to point to the HC Regional instance instead of VIE. During the period when some VistA sites have converted and others have not, VistA acknowledgements of ROES messages will be flowing through both VIE and HC as depicted in <u>Figure 3</u>.

<span id="_Ref2342096" class="anchor"></span>Figure 3: Deployment Step 2

![](tiu-1-325-dibr/005.png)

To implement changes for the message flows from VistA sites to ROES:

1.  On each HC Regional instance, enable the Inbound Service From_VISTA_ROES_7652 to enable receiving of acknowledgement of messages from VistA.
7.  On each HC Regional instance, enable the Outbound Operation To_ROESEnterprise_7653 to send acknowledgement messages to the HC Enterprise instance.
8.  On the HC Enterprise instance, enable the Inbound Service From_VISTA_ROES_7653 to receive acknowledge messages from VistA forwarded from the HC Regional instances.
9.  On the HC Enterprise instance, enable the Outbound Operation To_ROES_5000 to send acknowledgement messages to ROES.
10. On each applicable VistA site, change the TIUACKROES logical link to point to the appropriate Regional Health Connect instance. Sites will be provided with the logical link information separately.
11. The ROES and Health Connect teams will monitor message flows to ensure delivery and responses.

Once it is confirmed that all VistA sites have redirected their ROES acknowledgement messages to their respective HC Regional instance, the VIE Operations team will verify that no messages are left queued for ROES messages in either direction. If so, they will work with any sites originating queued messages to re-send or otherwise resolve the issue. The VIE Operations team will then disable any ROES related message flows in all VIE instances.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The estimated date for national release of ROES is prior to June 21, 2019.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no preparatory steps at the VA medical center (VAMC) locations for the deployment of the ROES messaging flows.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 4</u> depicts the final summary level targeted architecture after all deployment has been completed.

<span id="_Ref8291606" class="anchor"></span>Figure 4: Deployment Topology View

![](tiu-1-325-dibr/006.png)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HealthShare HC software has already been installed in production. There is one Enterprise instance, and six Regional instances:

- Enterprise – Austin Information Technology Center (AITC)
- Region 1 – Sacramento
- Region 1 – Denver
- Region 2 – Philadelphia
- Region 3 – Philadelphia
- Region 4 – Philadelphia
- Region 4 – Brooklyn

Production Operations staff will install the configurations specific to the ROES message flows in each of these HC instances.

The ROES production instance will be reconfigured in its current location to connect to the HC Enterprise production instance. No software changes are required in ROES.

Each VistA location that communicates with ROES will need to perform a reconfiguration of the IP address and Port for the HL7 Logical Link (#870) entry TIUACKROES. No software changes are required.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2</u> describes preparation required by the site prior to deployment.

| Site/Other                                       | Problem / Change Needed                                  | Features to Adapt/Modify to New Product | Actions/Steps                      | Owner                    |
|--------------------------------------------------|----------------------------------------------------------|-----------------------------------------|------------------------------------|--------------------------|
| HealthShare HC Enterprise and Regional Instances | Install production configurations for ROES message flows | Productions                             | Install Production definition file | HC Production Operations |

<span id="_Ref8291979" class="anchor"></span>Table 3: Download and Import Files

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following support resources will be required during the transition of ROES messages from VIE to HC:

- HC Support Operations Team
- VistA HL7 Support, VistA Administrators for each site
- ROES Support Staff

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section does *not* apply to HL7 HC and ROES. Virtual meetings can be used to assist sites as needed.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special hardware requirements for sites using HL7 HC and ROES.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HC/ROES software deployment is made up of the following:

- ROES HC Production Extensible Mark-up Language (XML) files will be placed under configuration control in Rational Configuration Management (CM).

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Communications and notification activities include:

- The VistA administrators will be notified in advance via their monthly community call to introduce them to the strategy and plans for the ROES message conversion.
- Patch TIU\*1\*325 will be released from Forum to all VistA sites via informational patch with implementation to be followed with 72 hours of release. The patch will contain the information necessary for the VistA administrator to connect to the appropriate HC Regional instance. The information needed to reconfigure the logical links will be provided during a Skype call. Changes are to be made during the Skype call and are only to be performed when directed to do so by the change leader.
- A “roll-call” Skype meeting will be held during national release to assist sites with redirecting the logical link and checking compliance.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Platform installation and preparation steps are outlined in the sections below.

## Download and Import Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definitions for ROES HC productions are available under configuration management in the VA Enterprise Rational CM instance. The files in <u>Table 3</u> should be downloaded to the respective HC server. Each file contains specific definitions for each region and the enterprise instance, so they *must* be placed on the appropriate server for deployment.

| HC Instance                | Deployment XML Filename                          |
|----------------------------|--------------------------------------------------|
| HC Region 1 – Sacramento   | *Export_HCM_Production_ROES_Prod_R1SAC.xml*      |
| HC Region 1 – Denver       | *Export_HCM_Production_ROES_Prod_R1DVR.xml*      |
| HC Region 2                | *Export_HCM_Production_ROES_Prod_R2.xml*         |
| HC Region 3                | *Export_HCM_Production_ROES_Prod_R3.xml*         |
| HC Region 4 – Brooklyn     | *Export_HCM_Production_ROES_Prod_R4BYN.xml*      |
| HC Region 4 – Philadelphia | *Export_HCM_Production_ROES_Prod_R4PITC.xml*     |
| HC Enterprise              | *Export_HCM_Production_ROES_Prod_Enterprise.xml* |

1.  As an administrator on the specific HC instance, access the Deploy option:

Management Portal (MP) Ensemble Manage Deployment Changes Deploy

> <span id="_Ref510445689" class="anchor"></span>Figure 5: Management Portal (MP): Deployment Options

> ![](tiu-1-325-dibr/007.png)

12. Select the ROES deployment file, downloaded earlier in Section 4.2, for the correct HC instance. In this example <u>Figure 6</u>, the file name is for eCMS but use the correct filename from <u>Table 3</u>:

Open Deployment Select Deployment file OK

> <span id="_Ref510445421" class="anchor"></span>Figure 6: Selecting Deployment File: ROES

![](tiu-1-325-dibr/008.png)

13. When you select OK in <u>Figure 6</u>, the “Deploy Production Changes” screen is displayed, as shown in <u>Figure 7</u>:

> <span id="_Ref510445568" class="anchor"></span>Figure 7: Deploy Production Changes Screen: ROES

![](tiu-1-325-dibr/009.png)

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no database creation steps for this deployment.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no installation scripts for this deployment.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cron Scripts do *not* apply to the HC/ROES deployment.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following access requirements and skills are needed for installation:

- A user with HC administrative privileges on the Enterprise and Regional production instances will be required to deploy and configure the ROES productions.
- At each VistA site, a user with HL7 Menu privileges in production will be required to reconfigure the TIUACKROES logical link.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No software is being deployed.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System configuration is described in sections <u>4.1</u> and <u>4.2</u>.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No database tuning is expected or required for ROES on HL7 HC.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out procedure documented in this section is basically the reverse of the deployment procedure. With a rapid roll-out strategy, a significant change to the messaging environment will occur quickly, so a back-out should be a last resort.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only back-out option is to “un-deploy” HC and repoint ROES and VistAs to the VIE last known software configuration and platform settings. This process will identify unsent ROES messages on HC and resend to their target systems.

The configuration and operational support will be in place as the VIE platform will still be in production, providing message routing for other applications. Coordination with each site and the operations teams for server configuration and VistA logical link update will be key to a successful back-out.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIE (for remaining supported applications) and HC (for migrated message flows) will be running in parallel. Since both will be running before and after the deployment, a return to VIE would include reactivating the VIE/ROES message flows.

The repointing of the ROES and VistA systems will need to be coordinated with site point of contact (POC), VIE, and HC operations.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary criteria for a back-out decision will be any detrimental impact to patient care. If the deployed software and configuration is irreparably causing loss or damage to ROES messages, a back-out may be preferable and timelier than repair to existing configurations. However, this is extremely unlikely given the extensive testing prior to deployment in production.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Primary risks for a deployment back-out are the loss or corruption of messages during the back-out procedure. Risks also include impact to the program schedule and budget for re-work and re-deployment.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The decision to execute the back-out procedure may only be made by:

- Ken Leonard (FM24 Project Manager)
- Annette Parsons (HC Operations Project Manager)

## Back-Out Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps should be followed to return ROES messages to their previous state.

1.  The VIE Operations team will re-activate configurations to process HL7 messages to between ROES and VistA.
2.  The ROES Operations team will reconfigure outbound messages to VistA sites to the previous configuration for VIE National.
3.  All VistA sites will need to revert their logical link for TIUACKROES to point to the prior VIE local instance.
4.  Once all VistA sites have verified the back-out, HC Operations will disable Inbound Services that accept VistA messages for ROES on all Regional instances (From_VISTA_ROES_7652).
5.  The HC Operations team will disable the Inbound Service that accepts messages from ROES (From_ROES_VISTA_7651).

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HC Operations team will verify that there are no queued transactions in the HC Enterprise or HC Regional instances. If so, they will work with the sending site to resend the message through VIE.

The VIE Operations team will verify that all messages flows are operational and passing messages.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the nature of the deployment strategy and messaging architecture, a roll-back of processed data is unrealistic and unnecessary. Since the source and target systems do *not* change during the deployment, messages will be processed after the deployment the same way as prior to deployment. Therefore, even if the messaging infrastructure is changed back, no roll-back of data or messages will be required.

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appendix A – HC Production Namespace Configuration and Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](tiu-1-325-dibr/010.png) NOTE: Sections <u>7.1.1</u> and <u>7.1.2</u> are included for completeness, but should *not* be necessary, since they should already have been completed at this point by previous FileMan 24 HC application installs.

### Creating a New Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new namespace in HC Production, do the following:

1.  Open the following:

System Administration Configuration System Configuration Namespace

14. Click Create New Namespace.
15. Enter the Name of the namespace HCM.
16. Create new database.
17. Enter the name of your database HCM.
18. <span id="create_namespace_step_06" class="anchor"></span>Click on browse next to Create your directory and create a folder with the name of your database HCM.
19. Click Next on the bottom of the screen; use the default settings or the ones recommended by the site administrator.
20. Click Next and select the default.
21. Click Finish.
22. Click on the dropdown Select an existing database for Routines and select the database folder created in [Step 6](#create_namespace_step_06) HCM.
23. Click Save.
24. Namespace HCM will be added to the list of namespaces.

### Deploying a Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deploy a HC Production, do the following:

1.  <span id="deploy_hc_step_01" class="anchor"></span>Copy the deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml) to a path and directory in HealthShare. For example:

/tmp/

25. On the “Health Connect” page, click on the switch that brings a window of all the namespaces.
26. Click on HCM. Verify the namespace value is now changed to HCM.
27. Click on EnsembleManageDeployment changesDeploy.
28. Click on Open Deployment and select the directory in [Step 1](#deploy_hc_step_01).
29. Select the Deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml).
30. The “Deployment Production Changes” screen will display the artifacts that were brought in as part of the xml file.
31. Click on the Deploy tab.
32. Deployment will begin. This will take a few minutes.
33. Go to the following:

Ensemble List Select HCM.Production.HL7RouterProduction

## Appendix B – Starting and Stopping a HC Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](tiu-1-325-dibr/011.png) REF: For details on what occurs when you start or stop a production, see the InterSystems book *Managing Ensemble Productions*.

### Starting Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start a HC Production, do the following:

1.  Log in to the Management Portal.
34. Change to the appropriate namespace.
35. Go to the “Production List” page:

Ensemble List Productions

36. Find the production in the list and click it.
37. Click the Open button at the top of the list.
38. On the resulting “Production Configuration” page, click Start to display a dialog box.
39. In the dialog box, click Open. The system displays a new dialog box with the name of the production, its startup status, and any associated messages.

![](tiu-1-325-dibr/012.png) NOTE: The system may also open Terminal windows. Do *not* close these windows. Click the OK button when it is displayed in the dialog box.

### Stopping HC Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To stop a HC Production, do the following:

![](tiu-1-325-dibr/013.png) NOTE: During this process ensure the HC operation is disabled before stopping it.

1.  Log in to the HealthShare Management Portal.
40. Change to the appropriate namespace.
41. Go to the “Production List” page:

Ensemble List Productions

42. Find the production in the list and click it.
43. Click the Open button at the top of the list.
44. On the resulting “Production Configuration” page, click Stop to display a dialog box.
45. In the dialog box, click OK. The system displays a new dialog box with the following:
- Name of the production.
- Shutdown status.
- Any associated messages.

![](tiu-1-325-dibr/014.png) NOTE: The system may also open Terminal windows. Do *not* close these windows. Click the OK button when it is displayed in the dialog box.

## Appendix C – Redirection of Logical Links in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps will have to be performed in the VistA HL7 application for TIUACKROES outbound link entry:

1.  Stop the TIUACKROES Logical Link using the HL7 Menu option Start/Stop Links. <u>Figure 8: HL7 Main Menu Stop Logical Link</u> is an example:

<span id="_Ref10539865" class="anchor"></span>Figure 8: HL7 Main Menu Stop Logical Link

![](tiu-1-325-dibr/015.png)

46. Reset the TIUACKROES Logical Link Queue Count (as instructed by Enterprise HL7 Support team on the roll call).
47. Edit the TIUACKROES Logical Link with the Link Edit HL7 menu option, as shown in <u>Figure 9: Edit TIUACKROES Logical Link</u>.

<span id="_Ref10539306" class="anchor"></span>Figure 9: Edit TIUACKROES Logical Link

![](tiu-1-325-dibr/016.png)

48. On the screen in <u>Figure 9</u>, change AUTOSTART to Enabled. Next, move the cursor to the field LLP TYPE and press Enter. This will present the second screen as shown in <u>Figure 10: Edit TCP Lower Level Parameters</u>.
49. On the first screen (upon return from editing lower level parameters), edit the DNS DOMAIN field as instructed.

<span id="_Ref10705300" class="anchor"></span>Figure 10: Edit TCP Lower Level Parameters

![](tiu-1-325-dibr/017.png)

50. Replace the existing TCP/IP address and existing TCP/IP port with the Health Connect IP address and port as shown in <u>Figure 10</u>.

    Note: Please wait until further instructed to restart the logical link. To restart the logical link, use SL Start/Stop Links menu as shown in <u>Figure 8</u>.

    Post installation instructions:
51. Restart the TIUACKROES logical link using SL Start/Stop Links menu as described in step 1 above.
52. Check/monitor the TIUACKROES logical link queues:
    1.  Check status (report if Open/Fail or Error) using the SM Systems Link Monitor menu option.
    2.  Check queue counts are the same for columns: TO SEND and SENT using the SM Systems Link Monitor menu option.
    3.  Check IP Address has filled in by performing a FileMan Inquiry to File \#870, JL LOGICAL LINK for the TIUACKROES logical link.
53. Monitor TIUACKROES logical link using the SM Systems Link Monitor menu option. Report back on the call if there are any issues.