---
title: InterSystems Health Connect - Electronic Contract Management System Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: plain
doc_subject: InterSystems Health Connect - Electronic Contract Management System
app_code: PRC
app_name: IFCAP
section: FIN
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: > This document describes the deployment, installation, back-out, and rollback instructions for the migration of Electronic Contract Management System (eCMS) from the Vitria Interface Engine (VIE) to InterSystems Health Connect (HC).
audience: 
keywords: 
  - table
  - contents
  - connect
  - health
  - production
  - ecms
  - deployment
  - back
  - vista
  - installation
page_count: 0
word_count: 4372
section_count: 27
table_count: 3
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: January 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/hc_ecms_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP/hc_ecms_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=42"
---

# InterSystems Health Connect (HC) / Electronic Contract Management System (eCMS)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [InterSystems Health Connect (HC) / Electronic Contract Management System (eCMS)](#intersystems-health-connect-hc-electronic-contract-management-system-ecms)
    - [January 2019 Department of Veterans Affairs (VA)](#january-2019-department-of-veterans-affairs-va)
    - [Revision History](#revision-history)
    - [List of Figures](#list-of-figures)
    - [List of Tables](#list-of-tables)
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
    - [VIE Message Flows](#vie-message-flows)
    - [Health Connect Flows](#health-connect-flows)
    - [eCMS Connection](#ecms-connection)
    - [VistA Sites Repoint to VIE](#vista-sites-repoint-to-vie)
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
- [Appendices](#appendices)
  - [Appendix A—Health Connect Production Namespace Configuration and Deployment](#appendix-ahealth-connect-production-namespace-configuration-and-deployment)
    - [Creating a New Namespace](#creating-a-new-namespace)
    - [Deploying a Health Connect Production](#deploying-a-health-connect-production)
  - [Appendix B—Configuring a Health Connect Production](#appendix-bconfiguring-a-health-connect-production)
    - [Configuring Each Regional Health Connect Production](#configuring-each-regional-health-connect-production)
    - [Configuring Enterprise Health Connect Production](#configuring-enterprise-health-connect-production)
  - [Appendix C—Starting and Stopping a Health Connect Production](#appendix-cstarting-and-stopping-a-health-connect-production)
    - [Starting Health Connect Production](#starting-health-connect-production)
    - [Stopping Health Connect Production](#stopping-health-connect-production)
> Deployment, Installation, Back-Out, and Rollback Guide
![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/001.png)

### January 2019 Department of Veterans Affairs (VA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OIT)

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1/16/2018</td>
<td>0.8</td>
<td>Revised section 3 Deployment</td>
<td>Halfaker: REDACTED</td>
</tr>
<tr class="even">
<td>12/21/2018</td>
<td>0.7</td>
<td><p>VA Tech Edit Review:</p>
<ul>
<li><p>Made style and format updates throughout to continue with same look and feel in other FM24 project documents.</p></li>
<li><p>Added alternate text to all images for Section 508 conformance.</p></li>
<li><p>Used Track Changes to enter all of my edits and comments. If you accept the changes I’m sure there will be some follow-up formatting issues. It’s hard to check/correct formatting when in Track Changes mode.</p></li>
</ul></td>
<td>VA Tech Writer: REDACTED</td>
</tr>
<tr class="odd">
<td>12/18/2018</td>
<td>0.6</td>
<td>Revised section 5 Back-Out Procedure</td>
<td>Halfaker: REDACTED</td>
</tr>
<tr class="even">
<td>12/12/2018</td>
<td>0.5</td>
<td>Additional feedback after review meeting and approved deployment approach</td>
<td>Halfaker: REDACTED</td>
</tr>
<tr class="odd">
<td>12/05/2018</td>
<td>0.4</td>
<td>Created an alternative deployment approach</td>
<td>Halfaker: REDACTED</td>
</tr>
<tr class="even">
<td>11/07/2018</td>
<td>0.3</td>
<td>Added details for HC settings details and incorporated team feedback</td>
<td>Halfaker: REDACTED</td>
</tr>
<tr class="odd">
<td>11/01/2018</td>
<td>0.2</td>
<td>Added details for deployment and back- out</td>
<td>Halfaker: REDACTED</td>
</tr>
<tr class="even">
<td>10/16/2018</td>
<td>0.1</td>
<td>Created initial outline</td>
<td>Halfaker: REDACTED</td>
</tr>
</tbody>
</table>
Table of Contents
1.  [Introduction 1](#introduction)
    1.  [Purpose 1](#purpose)
    2.  [Dependencies 1](#dependencies)
    3.  [Constraints 2](#constraints)
2.  [Roles and Responsibilities 2](#roles-and-responsibilities)
3.  [Deployment 3](#deployment)
    1.  [Timeline 10](#timeline)
    2.  [Site Readiness Assessment 11](#site-readiness-assessment)
        1.  [Deployment Topology (Targeted Architecture) 11](#deployment-topology-targeted-architecture)
        2.  [Site Information (Locations, Deployment Recipients) 12](#site-information-locations-deployment-recipients)
        3.  [Site Preparation 12](#site-preparation)
    3.  [Resources 12](#resources)
        1.  [Facility Specifics 13](#facility-specifics)
        2.  [Hardware 13](#hardware)
        3.  [Software 13](#software)
        4.  [Communications 13](#communications)
            1.  [Deployment/Installation/Back-Out Checklist 13](#deploymentinstallationback-out-checklist)
4.  [Installation 14](#installation)
    1.  [Platform Installation and Preparation 14](#platform-installation-and-preparation)
    2.  [Download and Import Files 14](#download-and-import-files)
    3.  [Database Creation 16](#database-creation)
    4.  [Installation Scripts 16](#installation-scripts)
    5.  [Cron Scripts 16](#cron-scripts)
    6.  [Access Requirements and Skills Needed for the Installation 16](#access-requirements-and-skills-needed-for-the-installation)
    7.  [Installation Procedure 16](#installation-procedure)
    8.  [Installation Verification Procedure 16](#installation-verification-procedure)
    9.  [System Configuration 16](#system-configuration)
    10. [Database Tuning 16](#database-tuning)
5.  [Back-Out Procedure 17](#back-out-procedure)
    1.  [Back-Out Strategy 17](#back-out-strategy)
    2.  [Back-Out Considerations 17](#back-out-considerations)
        1.  [Load Testing 17](#load-testing)
        2.  [User Acceptance Testing 17](#user-acceptance-testing)
    3.  [Back-Out Criteria 17](#back-out-criteria)
    4.  [Back-Out Risks 17](#back-out-risks)
    5.  [Authority for Back-Out 18](#authority-for-back-out)
    6.  [Back-Out Tasks 18](#back-out-tasks)
        1.  [VIE Message Flows 18](#vie-message-flows)
        2.  [Health Connect Flows 18](#health-connect-flows)
        3.  [eCMS Connection 18](#ecms-connection)
        4.  [VistA Sites Repoint to VIE 18](#vista-sites-repoint-to-vie)
    7.  [Back-Out Verification Procedure 18](#back-out-verification-procedure)
6.  [Rollback Procedure 19](#rollback-procedure)
7.  [Appendices 20](#appendices)
    1.  [Appendix A—Health Connect Production Namespace Configuration and Deployment 20](#appendix-ahealth-connect-production-namespace-configuration-and-deployment)
        1.  [Creating a New Namespace 20](#creating-a-new-namespace)
        2.  [Deploying a Health Connect Production 20](#deploying-a-health-connect-production)
    2.  [Appendix B—Configuring a Health Connect Production 22](#appendix-bconfiguring-a-health-connect-production)
        1.  [Configuring Each Regional Health Connect Production 22](#configuring-each-regional-health-connect-production)
        2.  [Configuring Enterprise Health Connect Production 25](#configuring-enterprise-health-connect-production)
    3.  [Appendix C—Starting and Stopping a Health Connect Production 28](#appendix-cstarting-and-stopping-a-health-connect-production)
        1.  [Starting Health Connect Production 28](#starting-health-connect-production)
        2.  [Stopping Health Connect Production 28](#stopping-health-connect-production)

### List of Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### List of Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document describes the deployment, installation, back-out, and rollback instructions for the migration of Electronic Contract Management System (eCMS) from the Vitria Interface Engine (VIE) to InterSystems Health Connect (HC).

> HC will replace VIE; currently in production, for the routing of eCMS messages. This document includes information about:

- System support
- Issue tracking
- Escalation processes
- Roles and responsibilities involved in all activities

> It provides clients, stakeholders, and support personnel with a smooth transition to Health Connect. It describes how to deploy and install the Health Connect in production as well as how to back out the product and roll back to a previous version or data set.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/002.png) NOTE: In cases where you are installing a commercial-off-the-shelf (COTS) product, you can use the vendor-provided user guide and installation guide. However, if those guides do *not* include a back-out recovery and rollback strategy, you *must* retain that information in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom Health Connect will be deployed and installed; as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, communications plan, and rollout schedule. Specific instructions for deployment, installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VIE supports the routing of messages from several applications. The Health Connect product will ultimately be replacing VIE. During the transition phase both products will be running concurrently.

> The success of HC as the messaging solution relies upon the availability of the VistA site administrators performing their part of the deployment in each VistA instance in a timely manner.

> The installation of the shared Enterprise and Regional Health Connect instances is not within the scope of this deployment, which is dependent upon those instances being installed, configured, and running in production.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HC is an approved product as per the VA’s Technical Reference Model (TRM).

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_bookmark8" class="anchor"></span>Table 1: Roles and Responsibilities

| ID | Team                                 | Phase / Role | Tasks                                                                                                            | Project Phase (See Schedule) |
|--------|------------------------------------------|------------------|----------------------------------------------------------------------------------------------------------------------|----------------------------------|
|        | FM24 Project Management Office (PMO)     | Deployment       | Plan and schedule deployment (including orchestration with vendors).                                                 |                                  |
|        |                                          |                  | Determine and document the roles and responsibilities of those involved in the deployment.                           |                                  |
|        | HC Operations                            | Deployment       | Test for operational readiness.                                                                                      |                                  |
|        | Site and VistA Operations                | Deployment       | Execute deployment, including switch of logical link to HC.                                                          |                                  |
|        | HC Operations                            | Installation     | Plan and schedule installation.                                                                                      |                                  |
|        |                                          |                  | Ensure authority to operate and that certificate authority security documentation is in place.                       |                                  |
|        |                                          |                  |                                                                                                                      |                                  |
|        | InterSystems                             | Installations    | Coordinate training as appropriate.                                                                                  |                                  |
|        | Development                              | Back-Out         | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out). |                                  |
|        | HC Operations/ Development/ InterSystems | Post Deployment  | Hardware, Software, and System Support.                                                                              |                                  |

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [<u>Figure 1</u>](#_bookmark10) depicts the current VistA Interface Engine (VIE) architecture for eCMS:

<span id="_bookmark10" class="anchor"></span>Figure 1: Current VIE Architecture for eCMS

![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/003.png)![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/004.png)

> The FileMan 24 (FM24) IT PMO and Operations leadership have determined that a Rapid Deployment is the only feasible deployment strategy because of the technical limitation of the eCMS Enterprise system to connect to one messaging service at one time. Since eCMS can connect to either VIE or Health Connect, but not both, there must be a single switchover point in time.

> In order to preserve message integrity and prevent message loss or substantial delay, a careful and deliberate set of steps must be followed in a specific order. VistA sites must quickly redirect new messages to avoid delayed communications between their site and eCMS.

#### Pre-Rollout Steps

> The HealthShare Health Connect App Support/Operations team performs the following pre- rollout steps:

1.  Installs the eCMS productions files onto the Enterprise Health Connect Instance and each of the Regional Health Connect instances.
2.  Ensures all applicable ports are properly configured and opened.
3.  Starts all productions
4.  Enables all Services, Processes, and Operations, except for the Enterprise HC Operation

> To_eCMS_5026, which should be left disabled.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/005.png)![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/006.png)<span id="_bookmark11" class="anchor"></span>Figure 2: Deploy Health Connect Productions

#### Rollout Procedure

> Perform the following rollout steps:

1.  The eCMS Operations team disables all outbound message flows. Until eCMS reconnects to HC Enterprise, no VistA sites will receive messages from eCMS.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/007.png)![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/008.png)<span id="_bookmark12" class="anchor"></span>Figure 3: Disable eCMS Outbound Flows

2.  The HealthShare Health Connect App Support/Operations team ensures all eCMS to VistA messages are processed and cleared.
3.  The Health Product Support team releases informational patch PRC\*5.1\*206 for 72-hour rapid release application.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/009.png) NOTE: If the National team can coordinate the sites’ execution of the patch instructions over a short period of time (i.e., one day), risk of stuck or duplicate transactions would be substantially reduced.

4.  Each VistA site will redirect the outbound PRCHJ_ECMS logical link from the Local Vitria Interface Engine (LVIE) to the appropriate Regional Health Connect instance following the instructions in the PRC\*5.1\*206 patch, see Figure 4.
5.  During this time period, VistA sites not yet redirected will still send messages through VIE and those will reach eCMS.
6.  For sites that redirect their logical link, their messages will reach HC Enterprise and be held in queue until the patch time period is over, and eCMS connects to HC Enterprise. These sites will *not* receive application acknowledgements until that time as well. The transitioned VistA sites will receive commit acknowledgements as normal.
7.  The Infrastructure Operations VistA Applications team will conduct conference calls to assist VistA sites with the redirection of the logical links, and to track compliance to the change.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/010.png) NOTE: Each site will be provided the actual values to be entered in this step.

> <span id="_bookmark13" class="anchor"></span>Figure 4: VistA HL7 Logical Link Screens

Main Screen

REDACTED

TCP Lower Level Parameter Screen

> REDACTED

1.  Shut down the PRCHJ_ECMS Logical Link with the Start/Stop Links HL7 menu option.
2.  Edit the PRCHJ_ECMS Logical Link with the Link Edit HL7 menu option.
3.  On the main screen make sure that AUTOSTART is Disabled; and replace the existing DNS DOMAIN with the Health Connect domain.
4.  When in the TCP Lower Level Parameter screen (by hitting enter at the LLP TYPE field located on the main screen), replace the existing TCP/IP ADDRESS and existing TCP/IP PORT (OPTIMIZED) with the Health Connect IP address and Port.
5.  Do NOT start the PRCHJ_ECMS Logical Link once the edits have been completed.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/011.png)![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/012.png)![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/013.png)<span id="_bookmark14" class="anchor"></span>.Figure 5: VistA Sites Start Redirecting Outbound Messages

5.  Once all VistA sites have complied with the transition to Health Connect, the HealthShare Health Connect App Support/Operations team monitors and validates that all:
    - eCMS related messages have passed through to their intended destination.
    - Local and national queues have been cleared.
    - eCMS VIE flows are disabled in the VIE network.
6.  The eCMS Operations team connects its inbound queue to the Enterprise Health Connect instance and begins processing the queued messages.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/014.png)![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/015.png)<span id="_bookmark15" class="anchor"></span>Figure 6: eCMS Connects Inbound to HC

7.  The eCMS Operations team connects outbound messages to VistA to the HC Enterprise instance.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/016.png)![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/017.png)<span id="_bookmark16" class="anchor"></span>Figure 7: eCMS Connection to HC for Outbound

8.  The HealthShare Health Connect App Support/Operations team monitors all eCMS productions on the Enterprise and Regional instances to ensure all messages are flowing appropriately.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For timeline information, see the VIE_eCMS_Checklist_V2.xlsx Excel spreadsheet on SharePoint: (Sharepoint path is FileMan 24 – VIE Migration – eCMS)

REDACTED

![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/018.png)

VIE_eCMS_Checklist

\_V2.xlsx

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no preparatory steps at the VA medical center (VAMC) locations for the deployment of the eCMS messaging flows.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The final state, once all sites have deployed, is depicted in [<u>Figure 8</u>.](#_bookmark20) VIE will no longer be used to pass messages related to eCMS and is removed from the target architecture. However, VIE will be used to manage other message types until they are also replaced.

![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/019.png)![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/020.png)<span id="_bookmark20" class="anchor"></span>Figure 8: Targeted eCMS Architecture

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HealthShare Health Connect software has already been installed in production. There is one Enterprise instance, and six regional instances named:

- Region 1—Sacramento
- Region 1—Denver
- Region 2, Region 3, Region 4—Philadelphia
- Region 4—Brooklyn

> Production Operations staff install the configurations specific to the eCMS message flows in each of these Health Connect instances.

> The eCMS Enterprise production instance is reconfigured in its current location to connect to the Health Connect Enterprise production instance. No software changes are required.

> Each VistA location that uses the Integrated Funds Control, Accounting, and Procurement (IFCAP) package to send and receive purchase requisitions will need to perform a reconfiguration of the IP address and Port for the HL7 Logical Link (#870) entry PRCHJ ECMS. No software changes are required.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [<u>Table 2</u>](#_bookmark23) describes preparation required by the site prior to deployment.

<span id="_bookmark23" class="anchor"></span>Table 2: Site Preparation

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site/Other</strong></th>
<th><strong>Problem / Change Needed</strong></th>
<th><blockquote>
<p><strong>Features to Adapt/Modify to New Product</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Actions/Steps</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Owner</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HealthShare Health Connect Enterprise and Regional Instances</td>
<td>Install production configurations for eCMS message flows</td>
<td><blockquote>
<p>Productions</p>
</blockquote></td>
<td><blockquote>
<p>Install Production definition file</p>
</blockquote></td>
<td><blockquote>
<p>HC</p>
<p>Production Operations</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following support resources will be required during the transition of eCMS messages from VIE to Health Connect:

- Health Connect Support Operations Team
- VistA HL7 Support, VistA Administrators for each site
- eCMS Support Staff

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section does *not* apply to HL7 Health Connect and eCMS. Virtual meetings can be used to assist sites as needed.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no special hardware requirements for sites using HL7 Health Connect and eCMS.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The HC/eCMS software deployment is made up of the following:

> eCMS Health Connect Production Extensible Mark-up Language (XML) files will be placed under configuration control in Rational CM.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Communications and notification activities include:

- The VistA administrators will be notified in advance via their monthly community call to introduce them to the strategy.
- Patch PRC\*5.1\*206 will be released from Forum to all VistA sites via rapid release information patch to be followed with 72 hours of release. The patch will contain the information necessary for the VistA administrator to connect to the appropriate Health Connect Regional instance.
- A series of “roll-call” conferences will be held when the patch is released to assist sites with redirecting the logical link and checking compliance.

#### Deployment/Installation/Back-Out Checklist

> Refer to section 3.1

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Platform installation and preparation steps are outlined in the sections below for PRC\*5.1\*206.

## Download and Import Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Definitions for eCMS Health Connect productions are available under Configuration Management in the VA Enterprise Ration CM instance. The files in [<u>Table 3</u>](#_bookmark33) should be downloaded to the respective Heath Connect server. Each file contains specific definitions for each region and the enterprise instance, so they *must* be placed on the appropriate server for deployment.

<span id="_bookmark33" class="anchor"></span>Table 3: Download and Import Files

| Health Connect Instance            | Deployment XML Filename   |
|----------------------------------------|-------------------------------|
| Health Connect Region 1 - Sacramento   | PROD_R1_Sacramento_eCMS.xml   |
| Health Connect Region 1 – Denver       | PROD_R1_Denver_eCMS.xml       |
| Health Connect Region 2                | PROD_R2_eCMS.xml              |
| Health Connect Region 3                | PROD_R3_eCMS.xml              |
| Health Connect Region 4 – Brooklyn     | PROD_R4_Brooklyn_eCMS.xml     |
| Health Connect Region 4 – Philadelphia | PROD_R4_Philadelphia_eCMS.xml |
| Health Connect Enterprise              | PROD_Enterprise_eCMS.xml      |

1.  As an administrator on the specific Health Connect Instance, access the Deploy option:

#### Management Portal (MP) → Ensemble → Manage → Deployment Changes →

> Deploy

> <span id="_bookmark34" class="anchor"></span>Figure 9: Management Portal (MP)—Deployment Options

REDACTED

2.  Select the eCMS XML deployment file, downloaded earlier Section 4.2, for the correct Health Connect instance. In this example [<u>Figure 10</u>](#_bookmark35), the file name is ECMS_Region1Denver.xml, but use the correct filename from [<u>Table 3</u>](#_bookmark33):

#### Open Deployment → Select Deployment file → OK

> <span id="_bookmark35" class="anchor"></span>Figure 10: SM—Selecting Deployment File: Ecms

> REDACTED

3.  When you select Deploy [<u>Figure 10</u>,](#_bookmark35) the “Deploy Production Changes” screen is displayed, as shown in [<u>Figure 11</u>](#_bookmark36):

> <span id="_bookmark36" class="anchor"></span>Figure 11: SM—Deploy Production Changes Screen: eCMS

REDACTED

4.  After deployment on each Health Connect instance, each production *must* be configured and enabled as described in Section [<u>7.2</u>](#appendix-bconfiguring-a-health-connect-production), “[<u>Appendix B—Configuring a Health Connect</u> <u>Production</u>](#appendix-bconfiguring-a-health-connect-production).”

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no database creation steps for this deployment.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no installation scripts for this deployment.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Cron Scripts do *not* apply to the Health Connect/eCMS deployment.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A user with Health Connect administrative privileges on the Enterprise and Regional production instances will be required to deploy and configure the eCMS productions.
- At each VistA site, a user with HL7 Menu privileges in production will be required to reconfigure the eCMS logical link.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No software is being deployed. Configuration of the productions is described in Section [<u>7.2</u>](#appendix-bconfiguring-a-health-connect-production), “[Appendix B—Configuring a Health Connect Production](#appendix-bconfiguring-a-health-connect-production) .”

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Not applicable.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> System configuration is described in in Section [<u>7.2</u>](#appendix-bconfiguring-a-health-connect-production), “ REF \_Ref529359156 \h \\ MERGEFORMAT [Appendix B—Configuring a Health Connect Production](#appendix-bconfiguring-a-health-connect-production) .”

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Currently, no database tuning is expected or required for eCMS on HL7 Health Connect.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The back-out procedure documented in this section is basically the reverse of the deployment procedure. With a rapid roll-out strategy, a significant change to the messaging environment will occur quickly, so a back-out should be a last resort.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since this is a first time install, the only back-out option is to un-deploy Health Connect (HC) and repoint eCMS to VistA Interface Engine (VIE) last known software configuration and platform settings.

> The back-out process will repoint eCMS servers and the VistA logical links back to the VIE instance. This process will identify unsent eCMS messages on Health Connect and resend to eCMS/VistA.

> The configuration and operational support will be in place as the VIE platform will still be in production, providing message routing for other applications. Coordination with each site and the operations teams (if VIE and Health Connect use different resources) for server configuration and VistA logical link update will be key to a successful back-out.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VIE (for remaining supported applications) and Health Connect (for migrated eCMS and other sites) will be running in parallel. Since both will be running before and after the deployment, a return to VIE would include reactivating the VIE/eCMS message flows.

> The repointing of the eCMS server and VistA systems will need to be coordinated with site point of contact (POC), VIE, and Health Connect operations.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The primary criteria for a back-out decision will be any detrimental impact to patient care. If the deployed software and configuration is irreparably causing loss or damage to eCMS messages, a back-out may be preferable and timelier than repair to existing configurations. However, this is extremely unlikely given the extensive testing prior to deployment in production.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Primary risks for a deployment back-out are the loss or corruption of messages during the back- out procedure. Risks also include impact to the program schedule and budget for re-work and re- deployment.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The decision to execute the back-out procedure may only be made by:

- Ken Leonard (FM24 Project Manager)
- Annette Parsons (HC Operations Project Manager)

## Back-Out Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The steps for the back out tasks are below.

### VIE Message Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIE message flows specific to eCMS should be reactivated back to their pre-deployment state.

### Health Connect Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The inbound flows from the VistA sites on the Regional Health Connect instances should be disabled so that no additional messages may be sent. The inbound flow from eCMS to the Enterprise Health Connect instance should be disabled so that new messages from eCMS may not be sent. The Health Connect production operations staff should ensure all eCMS messages have been processed through to eCMS or the appropriate VistA instance before deactivating the productions.

### eCMS Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The eCMS production operations team should disconnect its connection to the Health Connect Enterprise instance and reconnect to the VIE Enterprise instance.

### VistA Sites Repoint to VIE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An informational patch will need to be released to instruct each of the VistA sites to repoint their Logical Link for eCMS back to the VIE Regional instance they used prior to the deployment.

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following group will determine if messages remain on the VIE server if back out is required: VIE National Admins REDACTED

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Due to the nature of the deployment strategy and messaging architecture, a roll-back of processed data is unrealistic and unnecessary. Since the source and target systems do *not* change during the deployment, messages will be processed after the deployment the same way as prior to deployment. Therefore, even if the messaging infrastructure is changed back, no roll-back of data or messages will be required.

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appendix A—Health Connect Production Namespace Configuration and Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/021.png) NOTE: Sections [7.1.1](#creating-a-new-namespace) and [7.1.2](#deploying-a-health-connect-production) are included for completeness, but should *not* be necessary, since they should already have been completed at this point by previous Fileman 24 Health Connect application installs.

### Creating a New Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To create a new namespace in Health Connect Production, do the following:

1.  Open the following:

#### System Administration → Configuration → System Configuration → Namespace

2.  Click Create New Namespace.
3.  Enter the Name of the namespace HCM.
4.  Create new database.
5.  Enter the name of your database HCM.
6.  <span id="_bookmark63" class="anchor"></span>Click on browse next to Create your directory and create a folder with the name of your database HCM.
7.  Click Next on the bottom of the screen; use the default settings or the ones recommended by the site administrator.
8.  Click Next and select the default.
9.  Click Finish.
10. Click on the dropdown Select an existing database for Routines and select the database folder created in [<u>Step 6</u>](#_bookmark63) HCM.
11. Click Save.
12. Namespace HCM will be added to the list of namespaces.

### Deploying a Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To deploy a Health Connect Production, do the following:

13. <span id="_bookmark65" class="anchor"></span>Copy the deployment file (e.g., Export-HCM_Production_HL7RouterProduction- Deploy1.0.xml) to a path and directory in HealthShare. For example:

#### /tmp/

14. On the “Health Connect” page, click on the switch that brings a window of all the namespaces.
15. <span id="_bookmark66" class="anchor"></span>Click on HCM. Verify the namespace value is now changed to HCM.
16. Click on Ensemble → Manage → Deployment changes → Deploy.
17. Click on Open Deployment and select the directory in [<u>Step 1</u>.](#_bookmark65)
18. Select the Deployment file (e.g., Export-HCM_Production_HL7RouterProduction- Deploy1.0.xml).
19. The “Deployment Production Changes” screen will display the artifacts that were brought in as part of the xml file.
20. Click on the Deploy tab.
21. Deployment will begin. This will take a few minutes.
22. Go to the following:

> Ensemble → List → Select HCM.Production.HL7RouterProduction

## Appendix B—Configuring a Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once each respective production XML file has been deployed (see Section [4.2](#download-and-import-files), “[Download and](#download-and-import-files) [Import Files](#download-and-import-files)”), the eCMS Health Connect configuration will need to be performed on the Enterprise Health Connect instance, and each of the six Regional Health Connect instances.

### Configuring Each Regional Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For each Regional eCMS Production instance, do the following enable and properly direct messages to the correct location:

23. <span id="_bookmark69" class="anchor"></span>Each Regional instance will be responsible for sending messages that are initiated in eCMS (and flow through the Enterprise Health Connect instance) to the correct VistA instance and port. The eCMS_InRouter process will accept messages from the Enterprise Health Connect instance, and use the Lookup Table HCM.InboundRouter.Table5001 to route the message to the appropriate VistA instance and port. From the Management Console:
    1.  Navigate to Ensemble → Configure → Data Lookup Tables.
    2.  Select the Open button.
    3.  Select HCM \> InboundRouter \> Table5001.
    4.  For each VistA instance to which messages will be sent for the region, there should be an entry (key-value pair) that lists the receiving facility (key) and the name of the outbound Operation (value). For example, HL7.\<*siteName*\>.MED.VA.GOV:\<*port*\> (e.g., HL7.ANYSITE.MED.VA.GOV:9999) would map to value To_VISTA\<*site*\>\_\<*port*\> (e.g. To_VISTA001_9999).
    5.  A list of these key-value pairs will be sent separately to each Regional Health Connect administrator for entry into this table.
    6.  If any values are missing, enter the key and value in the right-hand column and hit the

> Apply button.

24. Configure connection details on Business Operations to properly direct outbound messages. A separate listing will be provided for each Region and Enterprise Health Connect administrator with proper values for configuration. For messages directed to eCMS, the outbound operation is to the Enterprise Health connect production, which will forward the message to eCMS. Also repeat this step for each of the VistA instances listed under the Operations column:
    1.  First, ensure that there is a System Default Setting with the IP Address or Fully Qualified Domain name of the Enterprise Health Connect instance, or the VistA instance to which messages will be sent.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/022.png) NOTE: IP Addresses and/or FQDN will be communicated to each system administrator separately.

1.  Navigate to Ensemble → Configure → System Default Settings.
2.  Look for an Item Name of To_eCMSEnt\_\<*port*\> or To_VISTA\<*site*\>\_\<*port*\>.
3.  If it already exists, skip to [<u>Step 2b</u>](#_bookmark70).
4.  Select the New button and enter the following:
    1.  Production = HCM.Production.HL7RouterProduction
    2.  Item Name = To_eCMSEnt\_\<*port*\> or To_VISTA\<*site*\>\_\<*port*\>
    3.  Host Class Name = EnsLib.HL7.Operation.TCPOperation
    4.  Setting Name = IPAddress
    5.  Setting Value = \<*IP Address or FQDN communicated separately*\>
    6.  <span id="_bookmark70" class="anchor"></span>Click the Save button.
2.  Navigate back to the Production listing (Ensemble → Configure → Production). To isolate eCMS components: select “eCMS” from the Category dropdown. Select an outbound business operation (e.g., To_eCMSEnt\_\<*port*\> or To_VISTA\<*site*\>\_\<*port*\>).
3.  Click on the Settings tab on the right.
4.  Select the Enabled checkbox.
5.  Select the Restore Default Values button (![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/023.png)).
6.  Select the blue IP Address setting and the Port setting (which should match the Operation name).
7.  Scroll to the bottom and select the Restore Default button. The IP Address label should turn blue.
8.  Click Apply.
25. Each of the four message handling Operations (e.g., BadMessageHandlerAll, BadMessageHandlereCMS, EmailAlert.OperationAll, EmailAlert.OperationeCMS) are deployed as enabled, and each should show as a status of Enabled (green indicator). If any are *not* enabled:
    1.  Select the Operation that has a grey indicator.
    2.  Click on the Settings tab on the right.
    3.  Select Enabled checkbox.
    4.  Click Apply.
26. Each of the four Business Processes (e.g., eCMS_InRouter, eCMS_OutRouter,OutRouter, InRouter, and Ens.Alert) are deployed as enabled, and each should show as a status of Enabled (green indicator). If any are *not* enabled:
    1.  Select business process related to eCMS.
    2.  Click on Settings tab on the right.
    3.  Select Enabled checkbox.
    4.  Click Apply.
27. Configure connection details on Business Services to allow inbound messages:
    1.  From the Management Portal → Ensemble → Configure → Production.
    2.  There should be two inbound Business Services:
- Messages initiated in VistA to eCMS
- Accepting messages initiating in eCMS to a VistA in the respective region.
  1.  Select the business service from eCMS to VistA

> (e.g., From_eCMS_VISTA\_\<*port*\>). This will allow messages from Enterprise Health Connect to be accepted into this Regional Health Connect.

2.  Click on the Settings tab on the right.
3.  Select the Enabled checkbox.
4.  Click Apply.
5.  Select the business service from VistA to eCMS

> (e.g., From_VISTA_eCMSEnt\_\<*port*\>). This will allow messages from a VistA instance to be accepted into this Regional Health Connect.

6.  Click on the Settings tab on the right.
7.  Select the Enabled checkbox.
8.  Click Apply.

### Configuring Enterprise Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> While similar to the steps in Section [<u>7.2.1</u>](#configuring-each-regional-health-connect-production) for the Regions, the Enterprise instance of Health Connect is configured slightly differently. The Enterprise Health Connect instance is responsible for forwarding messages from eCMS to the appropriate Regional Health Connect instance (for later forwarding to the destination VistA instance). Each message from eCMS contains a destination facility in the message header, which will be used to route the message to the correct region using table HCM.InboundRouter.Ecms

1.  Populate the table HCM.InboundRouter.Ecms using the steps below:
    1.  Navigate to Ensemble → Configure → Data Lookup Tables.
    2.  Select the Open button.
    3.  Select HCM 0→ InboundRouter → Ecms.
    4.  Verify an entry exists for each VistA instance to which messages will be sent. For the region, there should be an entry (key-value pair) that lists the receiving facility (key) and the name of the outbound Operation for the Region to which the message will be routed (value). For example, HL7.\<*siteName*\>.MED.VA.GOV:\<*port*\> (e.g., HL7.ANYSITE.MED.VA.GOV:0001) would map to value To_VISTARegion1_eCMS\_\<*port*\> (e.g., To_VISTARegion1_eCMS_9999).
    5.  A list of these key-value pairs will be sent separately to the Enterprise Health Connect administrator for entry into this table. Verify each entry exists and create entries if needed.
    6.  If any values are missing, enter the key and value in the right-hand column and click the Apply button.
2.  Configure connection details on Business Operations to properly direct outbound messages. For messages directed to eCMS, the outbound operation is to the enterprise eCMS instance. There will also be one Operations entry for each Regional instance of Health Connect. Repeat this step for each of the Regional instances listed under the Operations column:
    1.  First, ensure that there is a System Default Setting with the IP Address or Fully Qualified Domain name of each Regional Health Connect instance, and the enterprise eCMS instance to which messages will be sent.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/024.png) NOTE: IP Addresses and/or FQDN will be communicated to each system administrator separately.

1.  Navigate to Ensemble → Configure → System Default Settings.
2.  Look for an Item Name of To_eCMS\_\<*port*\> or

> To_VISTARegion\<*region*\>\_eCMS\_\<*port*\>

3.  If it already exists, skip to [<u>Step 2b</u>](#_bookmark72).
4.  Select the New button and enter the following:
    1.  Production = HCM.Production.HL7RouterProduction
    2.  Item Name = To_eCMS\_\<*port*\> or To_VISTARegion\<*region*\>\_eCMS\_\<*port*\>
    3.  Host Class Name = EnsLib.HL7.Operation.TCPOperation
    4.  Setting Name = IPAddress
    5.  Setting Value = \<*IP Address or FQDN communicated separately*\>
    6.  Click the Save button.
2.  <span id="_bookmark72" class="anchor"></span>Navigate to the Production listing (Ensemble → Configure → Production). To isolate eCMS components, select “eCMS” from the Category dropdown. Select an outbound business Operation (e.g., To_eCMS\_\<*port*\> or To_VISTARegion\<*region*\>-eCMS\_\<*port*\>).
3.  Click on the Settings tab on the right.
4.  Select the Enabled checkbox.
5.  Select the Restore Default Values button (![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/025.png)).
6.  Select the blue IP Address setting and the Port setting (which should match the Operation name).
7.  Scroll to the bottom and select the Restore Default button. The IP Address label should turn <u>blue</u>.
8.  Click Apply.
3.  Configure connection details on Business Services to allow inbound messages:
    1.  From the Management Portal → Ensemble → Configure → Production.
    2.  To isolate eCMS components, select “eCMS” from the Category dropdown. There should be two inbound Business Services:
- Messages from the Regional Health Connect instances addressed to eCMS.
- Accepting messages initiating in eCMS to a VistA in the respective region.
  1.  Select the business Service from eCMS to VistA

> (e.g., From_eCMSEnt_VISTA\_\<*port*\>). This will allow messages from eCMS to be accepted into this Enterprise Health Connect instance.

2.  Click on the Settings tab on the right.
3.  Select the Enabled checkbox.
4.  Click Apply.
5.  Select the business service from VistA to eCMS

> (e.g., From_VISTA_eCMS\_\<*port*\>). This will allow messages from a Regional Health Connect instance (originally from VistA) to be accepted into this Enterprise Health Connect.

6.  Click on the Settings tab on the right.
7.  Select the Enabled checkbox.
8.  Click Apply.
1.  If the four message handling Operations (e.g. BadMessageHandlerAll, BadMessageHandlereCMS, EmailAlert.OperationAll, EmailAlert.OperationeCMS) do *not* have a status of Enabled (green indicator), ensure each is enabled:
    1.  Select the Operation that has a grey indicator
    2.  Click on the Settings tab on the right.
    3.  Select Enabled checkbox.
    4.  Click Apply.
2.  Enable the business process:
    1.  Select business process related to eCMS (e.g., eCMSInRouter and Ens.Alert).
    2.  Click on Settings tab on the right.
    3.  Select Enabled checkbox.
    4.  Click Apply.

## Appendix C—Starting and Stopping a Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/026.png) REF: For details on what occurs when you start or stop a production, see the InterSystems book *Managing Ensemble Productions*.

### Starting Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To start a Health Connect Production, do the following:

3.  Log in to the Management Portal.
4.  Change to the appropriate namespace.
5.  Go to the “Production List” page:

#### Ensemble → List → Productions

6.  Find the production in the list and click it.
7.  Click the Open button at the top of the list.
8.  On the resulting “Production Configuration” page, click Start to display a dialog box.
9.  In the dialog box, click Open. The system displays a new dialog box with the name of the production, its startup status, and any associated messages.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/027.png) NOTE: The system may also open Terminal windows. Do *not* close these windows.

> Click the OK button when it is displayed in the dialog box.

### Stopping Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To stop a Health Connect Production, do the following:

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/028.png) NOTE: During this process ensure the Health Connect operation is disabled

> (see [<u>Appendix B</u>](#_bookmark66), [<u>Step 2</u>](#_bookmark69), “Configure connection details on Business Operations”).

10. Log in to the HealthShare Management Portal.
11. Change to the appropriate namespace.
12. Go to the “Production List” page:

#### Ensemble → List → Productions

13. Find the production in the list and click it.
14. Click the Open button at the top of the list.
15. On the resulting “Production Configuration” page, click Stop to display a dialog box.
16. In the dialog box, click OK. The system displays a new dialog box with the following:
- Name of the production.
- Shutdown status.
- Any associated messages.

> ![](intersystems-health-connect-electronic-contract-management-system-deployment-ins/029.png) NOTE: The system may also open Terminal windows. Do *not* close these windows.

> Click the OK button when it is displayed in the dialog box.