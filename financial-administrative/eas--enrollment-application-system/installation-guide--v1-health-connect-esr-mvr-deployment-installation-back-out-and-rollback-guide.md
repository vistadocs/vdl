---
title: EAS Version 1 Health Connect / ESR-MVR Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: anchor
doc_subject: Health Connect / ESR-MVR
app_code: EAS
app_name: Enrollment Application System
section: FIN
app_status: active
pkg_ns: EAS
patch_ver: 1
patch_id: EAS*1
group_key: "EAS:EAS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - deployment
  - production
  - back
  - messages
  - vista
  - enterprise
  - connect
  - health
page_count: 0
word_count: 6280
section_count: 30
table_count: 4
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: March 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/HC_ESR_MVR_DIBRG.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Enrollment_App_Sys_(EAS)/HC_ESR_MVR_DIBRG.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=121"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>InterSystems Health Connect (HC) / Enrollment System / Master Veteran Record (ESR/MVR)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/001.png)

March 2019

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

<span id="_Toc4489669" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref520206071" class="anchor"></span>Table 1: Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 51%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
<tr class="odd">
<th>03/26/2019</th>
<th>1.0</th>
<th><p>Final VA Tech Edit Review:</p>
<ul>
<li><p>Verified document is Section 508 conformant.</p></li>
<li><p>Set Document version to 1.0 for final release.</p></li>
</ul></th>
<th>VA Tech Writer: REDACTED</th>
</tr>
<tr class="header">
<th>01/24/2019</th>
<th>0.12</th>
<th>Added Step 9 to section 3.1 to ensure the “Separators” setting is properly set in the System Default Settings in each instance.</th>
<th>REDACTED</th>
</tr>
<tr class="odd">
<th>01/18/2019</th>
<th>0.11</th>
<th>Address VA Tech edit comments and requested changes</th>
<th>REDACTED</th>
</tr>
<tr class="header">
<th>01/14/2019</th>
<th>0.10</th>
<th><p>VA Tech Edits:</p>
<ul>
<li><p>Made style and format updates throughout to continue with same look and feel in other FM24 project documents.</p></li>
<li><p>Contractor needs to add alternate text to all images for Section 508 conformance.</p></li>
<li><p>Used Track Changes to enter all of my edits and comments. If you accept the changes I’m sure there will be some follow-up formatting issues. It’s hard to check/correct formatting when in Track Changes mode.</p></li>
</ul></th>
<th>VA Tech Writer: REDACTED</th>
</tr>
<tr class="odd">
<th>01/10/2019</th>
<th>0.9</th>
<th>Addressed comments from Kelly Gwin.</th>
<th>REDACTED</th>
</tr>
<tr class="header">
<th>01/09/2019</th>
<th>0.8</th>
<th>Corrections to deployment and rollback tasks and ordering from Mohamed Mohideen.</th>
<th>REDACTED</th>
</tr>
<tr class="odd">
<th>12/19/2018</th>
<th>0.7</th>
<th>Added location of ATO documents and commentary about back-out of e*Gate changes during ESR HC back-out. Both per request of Ken Leonard.</th>
<th>REDACTED</th>
</tr>
<tr class="header">
<th>12/18/2018</th>
<th>0.6</th>
<th>Small correction to To-Be diagram title.</th>
<th>REDACTED</th>
</tr>
<tr class="odd">
<th>12/04/2018</th>
<th>0.5</th>
<th>Cleanup and acceptance of edits/feedback.</th>
<th>REDACTED</th>
</tr>
<tr class="header">
<th>12/03/2018</th>
<th>0.4</th>
<th>Review by Sridhar Mandalapu.</th>
<th>REDACTED</th>
</tr>
<tr class="odd">
<th>11/26/2018</th>
<th>0.3</th>
<th>Review by Liana Buciuman.</th>
<th>REDACTED</th>
</tr>
<tr class="header">
<th>11/08/2018</th>
<th>0.2</th>
<th>Document Handoff.</th>
<th>REDACTED</th>
</tr>
<tr class="odd">
<th>10/29/2018</th>
<th>0.1</th>
<th>Created initial outline.</th>
<th>REDACTED</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Ref520206071" class="anchor"></span>Table 1: Roles and Responsibilities

Table of Contents

<span id="_Toc4489670" class="anchor"></span>List of Figures

<span id="_Toc4489671" class="anchor"></span>List of Tables

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
  - [Constraints](#constraints)
- [Roles and Responsibilities](#roles-and-responsibilities)
- [Deployment](#deployment)
  - [Pre- Rollout Procedure](#pre-rollout-procedure)
  - [Rollout Procedure](#rollout-procedure)
    - [IOC VistA Sites Change Logical Links](#ioc-vista-sites-change-logical-links)
    - [Query Messages from Enterprise Health Connect](#query-messages-from-enterprise-health-connect)
    - [Messages sent from MVR to ESR through HC Enterprise](#messages-sent-from-mvr-to-esr-through-hc-enterprise)
    - [Test Messages are sent from HC Enterprise to MVR](#test-messages-are-sent-from-hc-enterprise-to-mvr)
    - [All VistA sites’ messages to ESR Sent Through HC](#all-vista-sites-messages-to-esr-sent-through-hc)
    - [Test Query messages sent to VistA sites](#test-query-messages-sent-to-vista-sites)
    - [Redirect ESR Outbound Message Flows](#redirect-esr-outbound-message-flows)
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
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
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
  - [Back-Out Procedure](#back-out-procedure-1)
    - [Health Connect Flows](#health-connect-flows)
    - [VIE Message Flows](#vie-message-flows)
    - [ESR Connection](#esr-connection)
    - [MVR Connection](#mvr-connection)
    - [VistA Sites repoint to VIE](#vista-sites-repoint-to-vie)
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
- [Appendices](#appendices)
  - [Appendix A—Health Connect Production Namespace Configuration and Deployment](#appendix-ahealth-connect-production-namespace-configuration-and-deployment)
    - [Creating a New Namespace](#creating-a-new-namespace)
  - [Deploying a HC Production](#deploying-a-hc-production)
    - [HC Enterprise](#hc-enterprise)
    - [Regional Enterprise](#regional-enterprise)
  - [Appendix B—Configuring a Health Connect Production](#appendix-bconfiguring-a-health-connect-production)
  - [Appendix C—Starting and Stopping a HC Production](#appendix-cstarting-and-stopping-a-hc-production)
    - [Starting Health Connect Production](#starting-health-connect-production)
    - [Stopping Health Connect Production](#stopping-health-connect-production)
This document describes the deployment, installation, back-out, and rollback instructions for the migration of Enrollment System (ESR)/ Master Veteran Record (MVR) from the Veterans Information Systems Technology Architecture (VistA) Vitria Interface Engine (VIE) to InterSystems Health Connect (HC).
HC will replace VIE, currently in production, for the routing of ESR messages.
This document includes information about:
- System support
- Issue tracking
- Escalation processes
- Roles and responsibilities involved in all activities
It provides clients, stakeholders, and support personnel with a smooth transition to HC. It describes how to deploy and install the ESR interface via HC in production as well as how to back out the product and roll back to a previous version or data set.
![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/002.png) NOTE: In cases where you are installing a commercial-off-the-shelf (COTS) product, you can use the vendor-provided user guide and installation guide. However, if those guides do *not* include a back-out recovery and rollback strategy, you *must* retain that information in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the ESR interface via HC will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, a communications plan, and a rollout schedule. Specific instructions for deployment, installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIE supports the routing of messages from several applications. The HC product will ultimately be replacing VIE. During the transition phase both products will be running concurrently.

The success of HC as the messaging solution relies upon the availability of the VistA site administrators performing their part of the deployment in each VistA instance in a timely manner.

The installation of the shared Enterprise and Regional HC instances is not within the scope of this deployment, but this effort is dependent on those instances being installed, configured, and running in production.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HC is an approved product as per the VA’s Technical Reference Model (TRM).

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                              | Phase / Role    | Tasks                                                                                                                            | Project Phase (See Schedule) |
|-----|---------------------------------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------|
|     | FileMan 24 (FM24) Project Management Office (PMO) | Deployment      | Plan and schedule deployment (including orchestration with vendors).                                                             |                              |
|     |                                                   |                 | Determine and document the roles and responsibilities of those involved in the deployment.                                       |                              |
|     | Operations and End-User                           | Deployment      | Test for operational readiness.                                                                                                  |                              |
|     | Site and Operations                               | Deployment      | Execute deployment.                                                                                                              |                              |
|     | Operations                                        | Installation    | Plan and schedule installation.                                                                                                  |                              |
|     |                                                   |                 | Ensure authority to operate and that certificate authority security documentation is in place in the ESR Rational CM repository. |                              |
|     |                                                   |                 |                                                                                                                                  |                              |
|     | InterSystems                                      | Installations   | Coordinate training.                                                                                                             |                              |
|     | Development                                       | Back-Out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).             |                              |
|     | Operations/Development/ InterSystems              | Post Deployment | Hardware, Software, and System Support.                                                                                          |                              |

<span id="_Toc4489750" class="anchor"></span>Table 2: Timeline

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 1</u> depicts the current VIE architecture for ESR/MVR:

<span id="_Ref510009935" class="anchor"></span>Figure 1: Current VIE Architecture for ESR/MVR

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/003.png)

Several message types flow between VistA and ESR in both directions and are initiated by both systems. There are also other message flows between ESR and the Veteran Benefits Administration (VBA) services that provide information related to the Master Veteran Record (MVR). e\*Gate is the actual system (messaging service) to which VIE communicates, and which provides the interface with the MVR.

The deployment strategy for the VistA/ESR/MVR message flows is a gradual implementation of message flows at Initial Operating Capability (IOC) sites to manage risk and observe results prior to national deployment. Each phase is described in the sub-sections below.

## Pre- Rollout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps are to be executed prior to any legacy enterprise systems are modified or any VistA sites are patched:

1.  Validate that HealthShare/HC 2017.1.3 is installed on all Regional HC and Enterprise HC servers.
2.  Validate that the InterSystems Adhoc Patch 18633 (HS-2017_1_3_317_0_18633-LNXRHX64) for the Java Messaging Service (JMS) standard adapter is installed on the Enterprise server.
3.  Validate that Java Runtime Environment (JRE) 1.8 is installed on the Enterprise server.
4.  Deliver deployment packages for Enterprise and existing Regional HC servers via Rational Configuration Management.
5.  Execute the following SQL in the respective namespace before deploying the ensemble files to ensure the deployment won’t over-write or remove the existing settings.

    update Ens_Config.DefaultSettings set Deployable=0
6.  Deploy packages to Enterprise HC servers and Regional HC servers.
7.  Execute the following SQL in the respective namespace after deploying the ensemble files to ensure the deployment won’t over-write or remove the existing settings.

    update Ens_Config.DefaultSettings set Deployable=0
8.  Start the Production for HC ESR Enterprise namespace (Regional productions should be already running).
9.  Update the credentials for ESR WebLogic server on the Enterprise HC Server.
10. Verify and update routing table values on the Enterprise HC server and Regional HC servers.
11. Verify in each regional instance and the enterprise instance that there is a System Default Value setting with the values below. If not, add an entry where missing:
1.  Production Name = “\*”
2.  Item Name = “\*”
3.  Host Class Name = “\*”
4.  Setting Name = “Separators”
5.  Setting Value (leave blank)
6.  Deployable = “No”
12. Verify that all business services and business operations are disabled in Enterprise and Regional HC productions.
13. Verify that all business processes are enabled in Enterprise and Regional HC productions.
14. Verify connectivity between Regional HC servers and Enterprise HC Server.
15. Verify connectivity between Enterprise HC and ESR.
16. Verify connectivity between Enterprise HC and e\*Gate/MVR.

<span id="_Toc4489736" class="anchor"></span>Figure 2: Health Connect Preparation

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/004.png)

## Rollout Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IOC VistA Sites Change Logical Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first phase in deployment is the repointing of the VistA logical link LLESROUT from the Local VIE instance (LVIE) to the appropriate Regional HC instance for each IOC VistA instance. Once changed, the VistA messages will flow through a HC Regional instance to the HC Enterprise instance, and are then placed on a JMS queue for ESR. Next, validation that messages are received in all four ESR inbound queues would need to be performed. Any response messages or ESR-initiated message flows will continue to use VIE services during this phase.

<span id="_Ref529976001" class="anchor"></span>Figure 3: IOC VistA Sites Outbound to Health Connect

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/005.png)

### Query Messages from Enterprise Health Connect

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The next phase is to manually send query messages for a test patient from HC Enterprise to ensure that query messages will successfully be sent from HC Enterprise to HC Regional and are processed successfully in IOC VistA sites. All outbound IOC VistA messages to ESR are being routed to HC Regional at this point and all inbound messages from ESR to VistA will still be received from VIE Local.

<span id="_Toc4489738" class="anchor"></span>Figure 4: Test Message to IOC VistA Systems

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/006.png)

### Messages sent from MVR to ESR through HC Enterprise

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Messages to ESR from MVR will now be redirected to HC Enterprise instead of the National VIE. e\*Gate will need to be configured to send MVR messages to HC. Validating receipt of messages from MVR will need to be performed in ESR.

<span id="_Toc4489739" class="anchor"></span>Figure 5: MVR to ESR through HC Enterprise

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/007.png)

### Test Messages are sent from HC Enterprise to MVR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Test messages will need to be sent manually from HC Enterprise to MVR to verify connectivity. At this point, all IOC VistA messages to ESR and messages from MVR to ESR are now going through HC while all ESR outbound messages to VistA IOC sites, as well as MVR messages, are still being sent through VIE.

<span id="_Toc4489740" class="anchor"></span>Figure 6: Test Messages Sent from HC Enterprise to MVR

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/008.png)

At this point in time, the IOC will be considered complete, and the National Rollout Deployment will begin.

### All VistA sites’ messages to ESR Sent Through HC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once notified of transition readiness, each non-IOC VistA location will modify its logical links to point to their respective HC Regional instance, following instructions in the informational patch (EAS\*1\*166) on FORUM or via ftp from REDACTED.

- The VistA sites will now send ESR messages through HC and not VIE. The messages will go from VistA to HC Regional, then HC Enterprise and finally to ESR.
- Validation will need to be performed in ESR that the messages are sent to all four inbound queues.
- When this change is applied, VistA sites will stop sending ESR messages to Local VIE instances.
- Next, confirmation needs to be made that all messages have been processed and sent to the National VIE instance before shutting down the ESR interface in the Local VIE.
- Confirmation then needs to be made that all messages have been completely processed and sent outbound from the National VIE instance to ESR before shutting down the connection.
- ESR will be checked that all messages received from VIE have been processed and the queues are empty.

<span id="_Toc4489741" class="anchor"></span>Figure 7: All VistA Messages to HC Regional

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/009.png)

### Test Query messages sent to VistA sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Test query messages are sent manually from HC Enterprise that will pass through HC Regional to at least one VistA site in each Region to test connectivity. This test confirms that all VistA sites are connected to HC Enterprise.

<span id="_Toc4489742" class="anchor"></span>Figure 8: Query Messages from HC Enterprise to VistA Sites

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/010.png)

### Redirect ESR Outbound Message Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The next step is to begin sending outbound messages from ESR to the VistA sites with the following activities:

1.  In ESR, stop all outbound message flows to all VistA sites and to MVR end points.
2.  Stop FromEDB model in the National VIE instance.
17. Monitor that all queues in the National VIE instance to the Local VIE instances are cleared, and all Local VIE instance queues to VistA instances are cleared.
18. Ensure all National VIE instance messages to MVR are also cleared.
19. Then, start ESR outbound messaging to the Enterprise Health Connect Instance.

<span id="_Ref532196364" class="anchor"></span>Figure 9: Redirect all ESR Outbound traffic to HC

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/011.png)

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref506222619" class="anchor"></span>Table 3: Site Preparation</p></caption>
<colgroup>
<col style="width: 65%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>Step</th>
<th>Timing (Est Start)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Install HC Productions.</td>
<td>01/25/2019</td>
</tr>
<tr class="even">
<td>Send out VistA Informational Patch.</td>
<td>02/01/2019</td>
</tr>
<tr class="odd">
<td><p>IOC:</p>
<ul>
<li><p>Sites (establish, connectivity, switch over to sending to RHC, test queries, monitor, etc.).</p></li>
</ul></td>
<td>02/07/2019</td>
</tr>
<tr class="even">
<td><ul>
<li><p>MVR (establish, connectivity, switch over to sending to EHC, test queries, monitor etc.).</p></li>
</ul></td>
<td>02/07/2019</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Disable MVR transmissions to Enterprise VIE.</p></li>
</ul></td>
<td>02/07/2019</td>
</tr>
<tr class="even">
<td>HC National Rollout Deployment:</td>
<td></td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Disable VistA transmissions to Local VIE systems and enable VistA transmissions to the Regional HC (all regions).</p></li>
</ul></td>
<td>02/27/2019</td>
</tr>
<tr class="even">
<td><ul>
<li><p>Pending Operations Planning the region switch over for all VistA systems.</p></li>
</ul></td>
<td>02/27/2019</td>
</tr>
<tr class="odd">
<td><ul>
<li><p>Disable ESR transmissions to Enterprise VIE and enable ESR transmissions to regional HC (all regions).</p></li>
</ul></td>
<td>04/10/2019</td>
</tr>
<tr class="even">
<td>Ensure messages are cleared out of VIE environments.</td>
<td>02/27/2019</td>
</tr>
<tr class="odd">
<td>Turn on ESR-MVR operations in HC Enterprise Instance.</td>
<td>04/10/2019</td>
</tr>
<tr class="even">
<td>All VistA sites adjust Logical Link to HC.</td>
<td>04/10/2019</td>
</tr>
<tr class="odd">
<td>Disable ESR-MVR VIE flows in Enterprise VIE.</td>
<td>04/10/2019</td>
</tr>
</tbody>
</table>

<span id="_Ref506222619" class="anchor"></span>Table 3: Site Preparation

Please note, stopping the VIE interface that picks up messages from ESR JMS Queues will need to happen only after all the VistA interface sending messages to ESR JMS Queues are connected to HC. The same connection picks up messages for MVR as well.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Regional HC locations will need a site readiness assessment prior to deployment. VistA logical links will need to be pointed to those servers. Once IOC sites are determined, site readiness assessments will need to be scheduled to prepare for deployment.

Line of sight testing will need to be scheduled and performed for deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The final state, once all sites have deployed, is depicted in <u>Figure 10</u>. VIE will no longer be used to pass messages among ESR, MVR, and VistA, and is removed from the target architecture. However, VIE will be used to manage other message types until they are also migrated.

<span id="_Ref535219974" class="anchor"></span>Figure 10: Targeted ESR-MVR Architecture

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/012.png)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IOC sites:

- Columbus, OH (Station \# 757)
- Battle Creek, MI (Station \# 515)

The HealthShare HC software has already been installed in production. There is one Enterprise instance, and six Regional instances:

- Region 1 - Sacramento
- Region 1 - Denver
- Region 2 - Philadelphia
- Region 3 - Philadelphia
- Region 4 - Philadelphia
- Region 4 - Brooklyn

Production Operations staff will install the configurations specific to the VistA-ESR-MVR message flows in each of these HC instances.

The ESR Enterprise production instance will be reconfigured in its current location to connect to the HC Enterprise production instance. The MVR Enterprise production instance (e\*Gate) will be reconfigured in its current location to connect to the HC Enterprise production instance. No software changes are required.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> describes preparation required by the site prior to deployment.

| Site/Other                                       | Problem / Change Needed                                       | Features to Adapt/Modify to New Product | Actions/Steps                                                                                             | Owner                  |
|--------------------------------------------------|---------------------------------------------------------------|-----------------------------------------|-----------------------------------------------------------------------------------------------------------|------------------------|
| Columbus, OH                                     | Establish IP communication                                    | N/A                                     | Ensure listener is enabled and Access Control Lists (ACLs) allow HealthShare servers IP range to connect. | Local IT Administrator |
| Battle Creek, MI                                 | Establish IP communication                                    | N/A                                     | Ensure listener is enabled and Access Control Lists (ACLs) allow HealthShare servers IP range to connect. | Local IT Administrator |
| HealthShare HC Enterprise and Regional Instances | Install production configurations for ESR – MVR message flows | Productions                             | Install Production definition file                                                                        | Production Operations  |
| HealthShare HC Enterprise and Regional Instances | Verify that InterSystems JMS adapter adhoc is installed       | Productions                             | Verify that InterSystems JMS adapter adhoc is installed                                                   | Production Operations  |

<span id="_Ref535222045" class="anchor"></span>Table 4: HC Instances

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following support resources will be required during the transition of ESR messages from VIE to HC:

- HC Support Operations Team
- VistA HL7 Support, VistA Patch Installer
- ESR Support Staff
- MVR Support Staff
- VIE Support Staff

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section does *not* apply to HL7 HC and ESR. Virtual meetings can be used to assist sites as needed.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special hardware requirements for sites using HL7 HC and ESR.

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/013.png) REF: For details about who is responsible for preparing the site to meet these hardware specifications, see <u>Table 1: Roles and Responsibilities</u>.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HC/ESR software deployment is made up of the following:

- ESR HC Production Extensible Mark-up Language (XML) file (e.g., Export-HCM_Production_HL7RouterProduction_ESRv1.xml)—The HC XML file will be delivered from the Community Resource and Referral Center (CRRC) development/test environment.
- InterSystems Adhoc Patch 18633 (HS-2017_1_3_317_0_18633-LNXRHX64) for the Java Messaging Service (JMS) standard adapter.

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/014.png) REF: For details about who is responsible for preparing the site to meet these software specifications, see <u>Table 1: Roles and Responsibilities</u>.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Communications and notification activities include:

- The VistA administrators will be notified in advance via their monthly community call to introduce them to the strategy.
- Patch EAS\*1\*166 will be released from FORUM to all VistA sites via informational patch to be followed with 72 hours of release. The patch will contain the information necessary for the VistA administrator to connect to the appropriate HC Regional instance.

#### Deployment/Installation/Back-Out Checklist

Associated checklists will be kept separately in the SharePoint folder (at this [link](https://vaww.oed.portal.va.gov/pm/iehr/vista_evolution/FileMan%2024/Forms/AllItems.aspx?RootFolder=%2Fpm%2Fiehr%2Fvista%5Fevolution%2FFileMan%2024%2FVIE%20Migration%2FESR)) for ESR as appropriate, available for administrative and operations personnel.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Platform installation and preparation steps are outlined below for EAS\*1\*166:

## Download and Import Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definitions for ESR-MVR HC productions will be made available under *Configuration Management in the VA Enterprise Rational CM instance*. The files in <u>Table 4</u> should be downloaded to the respective HC server. Each file will contain specific definitions for each region and the enterprise instance, so they *must* be placed on the appropriate server for deployment:

| HC Instance                            | Deployment XML Filename                                |
|----------------------------------------|--------------------------------------------------------|
| Health Connect Region 1 - Sacramento   | Export-HCM_Production_ESRProdRegionalR1Sacramento.xml  |
| Health Connect Region 1 – Denver       | Export-HCM_Production_ESRProdRegionalR1Denver.xml      |
| Health Connect Region 2                | Export-HCM_Production_ESRProdRegionalR2.xml            |
| Health Connect Region 3                | Export-HCM_Production_ESRProdRegionalR3.xml            |
| Health Connect Region 4 – Brooklyn     | Export-HCM_Production_ESRProdRegionalR4Brooklyn.xml    |
| Health Connect Region 4 – Philadelphia | Export-HCM_Production_ESRProdRegionalR4Philadelpha.xml |
| Health Connect Enterprise              | Export-HCM_Production_ESRProdEnterprise.xml            |

The steps below describe the activities necessary to install the production on the Health Connect instance:

1.  As an administrator on the specific HC instance, access the Deploy option:

Management Portal (MP) Ensemble Manage Deployment Changes Deploy

> <span id="_Toc4489745" class="anchor"></span>Figure 11: Management Portal (MP)—Deployment Options

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/015.png)

2.  Select the ESR deployment file (e.g., Export-HCM_Production_HL7RouterProduction_ESR_RegionX.xml):

Open Deployment Select Deployment file Ok

<span id="_Toc4489746" class="anchor"></span>Figure 12: Selecting Deployment File: ESR

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/016.png)

3.  Verify what classes and configuration items are included in the package before selecting the deploy button.

> <span id="_Ref510445568" class="anchor"></span>Figure 13: Deploy Production Changes Screen: ESR

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/017.png)

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/018.png) REF: For deployment steps, see [Appendix A](#appendix-ahealth-connect-production-namespace-configuration-and-deployment).

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no database creation steps for this deployment.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no installation scripts for this deployment.

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/019.png) REF: For deployment steps, see [Appendix A](#appendix-ahealth-connect-production-namespace-configuration-and-deployment).

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cron scripts do *not* apply to the HC/ESR deployment.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The access privileges below will be required for each system affected by the implementation:

- A user with HC administrative privileges on the Enterprise and Regional production instances will be required to deploy and configure the ESR-MVR productions.
- At each VistA site, a user with HL7 Menu privileges in production will be required to reconfigure the ESR logical link.
- For MVR, a user with administrative privileges on e\*Gate will be required to change the links from Enterprise VIE to Enterprise HC.
- No changes in ESR will be required.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No software is being deployed. Configuration of the productions is described in Section <u>7.3</u>, “<u>Appendix B—Configuring a Health Connect Production</u>.”

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start the ESR HC production, follow the steps in [Appendix C](#appendix-cstarting-and-stopping-a-hc-production).

Once the production is running, the ESR production business services, operations, and routers should be enabled (See [Appendix B](#appendix-bconfiguring-a-health-connect-production)).

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, no database tuning is expected or required for ESR on HL7 Health Connect.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out procedure documented in this section is basically the reverse of the deployment procedure. With a rapid roll-out strategy, a significant change to the messaging environment will occur quickly, so a back-out should be a last resort.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out strategy is effectively the reverse of the roll-out steps, returning the messaging environment to its pre-deployment state.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIE (for remaining supported applications) and HC (for migrated ESR and other sites) will be running in parallel. If back-out is needed, the only feed that would need to be shut down is the HC Enterprise feed that picks up messages from ESR. The Enterprise VIE feed would need to be enabled to pick up messages from ESR, see <u>Figure 9: Redirect all ESR Outbound traffic to HC</u>.

The repointing of ESR servers would need to be coordinated with a site point of contact (POC), VIE, and HC operations.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary criteria for a back-out decision will be any detrimental impact to patient care. If the deployed software and configuration is irreparably causing loss or damage to VistA-ESR-MVR messages, a back-out may be preferable and more timely than repair to existing configurations. However, this is extremely unlikely given the extensive testing prior to deployment in production.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Primary risks for a deployment back-out are the loss or corruption of messages during the back-out procedure. Back-out risks are to the schedule of the HC / VIE migration project.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authority for back-out will be determined by the following:

- Ken Leonard (FileMan 24 Project Manager)
- Annette Parsons (HC Operations Project Manager)
- Roger Dowling
- ESR Business Owner

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Health Connect Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps should be taken to disable and disconnect Health Connect message flows:

1.  The inbound flows from the VistA sites on the Regional HC instances should be disabled so that no additional messages may be sent.
2.  The inbound flow from ESR to the Enterprise HC instance should be disabled so that new messages from ESR may not be sent.
20. The inbound flow from MVR to the Enterprise HC instance should be disabled so that new messages from MVR may not be sent.
21. The HC production operations staff should ensure all ESR messages have been processed through to ESR or the appropriate VistA instance before deactivating the productions.
22. The HC production operations staff should ensure all MVR messages have been processed through to MVR or the appropriate VistA instance before deactivating the productions.

### VIE Message Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VIE message flows specific to VistA-ESR-MVR should be reactivated back to their pre-deployment state.

### ESR Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No change was made to the ESR connection. The ESR production operations team will need to monitor that messages from JMS queues are being picked up by Enterprise VIE.

### MVR Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MVR/e\*Gate production operations team should disconnect its connection to the HC Enterprise instance, and reconnect to the VIE Enterprise instance. Configuration/Code changes made to e\*Gate prior to deployment of Health Connect should also be reversed per instructions in the e\*Gate DIBRG document (maintained by the e\*Gate Operations team).

### VistA Sites repoint to VIE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An informational patch will need to be released to instruct each of the VistA sites to repoint their logical link for ESR back to the VIE Regional instance each used prior to the deployment.

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following group will validate if messages are passing thru VIE servers if back out is required:

VIE National Admins REDACTED

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the nature of the deployment strategy and messaging architecture, a rollback of processed data is unrealistic and unnecessary. Since the source and target systems do *not* change during the deployment, messages will be processed after the deployment the same way as prior to deployment. Therefore, even if the messaging infrastructure is changed back, no rollback of data or messages will be required.

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appendix A—Health Connect Production Namespace Configuration and Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Creating a New Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new namespace in HC Production, do the following:

Open the following:

1.  System Administration Configuration System Configuration Namespace.
2.  Click Create New Namespace.
23. Enter the Name of the namespace HCM.
24. Create new database.
25. Enter the name of your database HCM.
26. <span id="create_namespace_step_06" class="anchor"></span>Click on browse next to Create your directory and create a folder with the name of your database HCM.
27. Click Next on the bottom of the screen; use the default settings or the ones recommended by the site administrator.
28. Click Next and select the default.
29. Click Finish.
30. Click on the dropdown Select an existing database for Routines and select the database folder created in [Step 6](#create_namespace_step_06) HCM.
31. Click Save.
32. Namespace HCM will be added to the list of namespaces.

## Deploying a HC Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HC Enterprise

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deploy a HC Production, do the following:

1.  <span id="deploy_hc_step_01" class="anchor"></span>Copy the deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml) to a path and directory in HealthShare. For example:

/tmp/

2.  On the “Health Connect” page, click on the switch that brings a window of all the namespaces.
33. Click on HCM-ESR. Verify the namespace value is now changed to HCM-ESR.
34. Click on Ensemble Manage Deployment changes Deploy.
35. Click on Open Deployment and select the directory in [Step 1](#deploy_hc_step_01).
36. Select the deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml).
37. The “Deployment Production Changes” screen displays the artifacts that were brought in as part of the xml file.
38. Click on the Deploy tab.
39. Deployment begins. This takes a few minutes.
40. Go to the following:

Ensemble List Select HCM.Production.HL7RouterProduction

### Regional Enterprise

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deploy a HC Production, do the following:

1.  Copy the deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml) to a path and directory in HealthShare. For example:

/tmp/

2.  On the “Health Connect” page, click on the switch that brings a window of all the namespaces.
41. Click on HCM. Verify the namespace value is now changed to HCM.
42. Click on EnsembleManageDeployment changesDeploy.
43. Click on Open Deployment and select the directory in [Step 1](#deploy_hc_step_01).
44. Select the Deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml).
45. The “Deployment Production Changes” screen will display the artifacts that were brought in as part of the xml file.
46. Click on the Deploy tab.
47. Deployment begins. This takes a few minutes.
48. Go to the following:

Ensemble List Select HCM.Production.HL7RouterProduction

## Appendix B—Configuring a Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To configure a HC Production, do the following:

1.  Configure connection details on Business Services:
1.  Select a business service (e.g., From_DU459_ESR).
7.  Click on the Settings tab on the right.
8.  Select the Enabled checkbox.
9.  Enter the designated port.
10. Verify the Stay Connected setting is set to a value of 120.
11. Click Apply.
1.  <span id="configure_hc_prod_step_2" class="anchor"></span>Configure connection details on business operations:
1.  Select a business operation (e.g., To_ESREntAcknowledgement_7451, EMailAlert.OperationESR, and BadMessageHandlerESR).
12. Click on the Settings tab on the right.
13. Select the Enabled checkbox (uncheck to disable).
14. Enter the IP address of the ESR system.
15. Enter the designated port.
16. Click Apply.
3.  Enable the business process:
1.  Select business process related to ESR (e.g., ESR_InRouter, ESR_OutRouter,OutRouter, InRouter, and Ens.Alert).
17. Click on Settings tab on the right.
18. Select Enabled checkbox.
19. Click Apply.
49. The Point of Reference is VistA and all messages sent out from VistA will have the ESR details in the Outbound table. The Inbound table will have the VistA Domain names since these are messages coming into VistA
50. on Update Inbound and Outbound tables:
1.  Go to the following:

Ensemble Configure Data Lookup Tables

20. Go to the following:

Open HCM OutboundRouter Table

21. Enter Key \[e.g., this is MSH(6.2) segment receiving institution from the HL7 Message\].
22. Enter Value (eg: To_ESR_xxx operation).
51. Start the HC Production by clicking the Start button in the “Production Configuration” screen (<u>Figure 14</u>).

> <span id="_Ref508864945" class="anchor"></span>Figure 14: InterSystems HealthShare—Production Configuration Screen: ESR

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/020.png)

## Appendix C—Starting and Stopping a HC Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/021.png) REF: For details on what occurs when a production is started or stopped, see the InterSystems documentation *Managing Ensemble Productions*.

### Starting Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start a HC Production, do the following:

1.  Log in to the HealthShare Management Portal.
2.  Change to the appropriate namespace.
52. Go to the “Production List” page:
53. Go to Ensemble List Productions.
54. Find the production in the list and click it.
55. Click the Open button at the top of the list.
56. On the resulting “Production Configuration” page, click Start to display a dialog box.
57. In the dialog box, click Open. The system displays a new dialog box with the following:
- Name of the production.
- Startup status.
- Any associated messages.

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/022.png) NOTE: The system may also open Terminal windows. Do *not* close these windows. Click the OK button when it is displayed in the dialog box.

### Stopping Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To stop a HC Production, do the following:

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/023.png) NOTE: During this process ensure the HC operation is disabled  
(see [Appendix B](#appendix-bconfiguring-a-health-connect-production), [Step 2](#configure_hc_prod_step_2), “Configure connection details on Business Operations”).

1.  Log in to the HealthShare Management Portal (Cache Cube).
58. Change to the appropriate namespace.
59. Go to the “Production List” page:
60. Go to Ensemble List Productions.
61. Find the production in the list and click it.
62. Click the Open button at the top of the list.
63. On the resulting “Production Configuration” page, click Stop to display a dialog box.
64. In the dialog box, click OK. The system displays a new dialog box with the following:
- Name of the production.
- Shutdown status.
- Any associated messages.

![](eas-version-1-health-connect-esr-mvr-deployment-installation-back-out-and-rollba/024.png) NOTE: The system may also open Terminal windows. Do *not* close these windows. Click the OK button when it is displayed in the dialog box.