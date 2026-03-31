---
title: VDEF*1*15 HDR/CHDR Deployment, Installation, Back-Out, and Rollback
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: HDR/CHDR Deployment, Installation, Back-Out, and Rollback
app_code: VDEF
app_name: VistA Data Extraction Framework
section: INF
app_status: active
pkg_ns: VDEF
patch_ver: 1
patch_id: VDEF*1*15
group_key: "VDEF:VDEF:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - chdr
  - contents
  - deployment
  - operations
  - team
  - back
  - production
  - messages
  - installation
page_count: 0
word_count: 5301
section_count: 30
table_count: 4
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: June 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Vista_Data_Ex_(VDEF)/vdef_1_p15_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Vista_Data_Ex_(VDEF)/vdef_1_p15_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=144"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>InterSystems Health Connect (HC) / Health Data Repository (HDR) – Clinical Health Data Repository (CHDR)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/001.png)

June 2019

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

<span id="_Toc11145705" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref520206071" class="anchor"></span>Table 1: Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 46%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>06/11/2019</td>
<td>1.0</td>
<td><p>Final document Release</p>
<ul>
<li><p>Updated Date to June 2019.</p></li>
<li><p>Created accompanying PDF.</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>06/06/2019</td>
<td>0.6</td>
<td>Updates to order of steps in deployment of phase 1 based on deployment prep meeting</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>05/21/2019</td>
<td>0.5</td>
<td><p>VA Tech Edit Review:</p>
<ul>
<li><p>Made very minor style and format updates.</p></li>
<li><p>Verified Word document is Section 508 conformant.</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>04/29/2019</td>
<td>0.4</td>
<td>Additional reviewer feedback.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>04/25/2019</td>
<td>0.3</td>
<td>Incorporated feedback from reviewers.</td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>04/11/2019</td>
<td>0.2</td>
<td>Draft submitted to PMO for review.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>02/11/2019</td>
<td>0.1</td>
<td>Created initial outline.</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Ref520206071" class="anchor"></span>Table 1: Roles and Responsibilities

Table of Contents

<span id="_Toc11145706" class="anchor"></span>List of Figures

<span id="_Toc11145707" class="anchor"></span>List of Tables

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
  - [Deployment of Phase 1](#deployment-of-phase-1)
  - [Deployment of Phase 2](#deployment-of-phase-2)
  - [Deployment of Phase 3](#deployment-of-phase-3)
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
    - [VistA to HDR-CHDR Messages](#vista-to-hdr-chdr-messages)
    - [MVI to VA CHDR Messages](#mvi-to-va-chdr-messages)
    - [VA CHDR and DoD CHDR](#va-chdr-and-dod-chdr)
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
- [Appendices](#appendices)
  - [Appendix A—HC Production Namespace Configuration and Deployment](#appendix-ahc-production-namespace-configuration-and-deployment)
    - [Creating a New Namespace](#creating-a-new-namespace)
    - [Deploying a Health Connect Production](#deploying-a-health-connect-production)
  - [Appendix B—Starting and Stopping a HC Production](#appendix-bstarting-and-stopping-a-hc-production)
    - [Starting Health Connect Production](#starting-health-connect-production)
    - [Stopping HC Production](#stopping-hc-production)
This document describes the deployment, installation, back-out, and rollback instructions for the migration of Health Level Seven (HL7) messages from the Vitria Interface Engine (VIE) to InterSystems Health Connect (HC). There are three distinct message flows as a part of a single release of the Health Connect configuration, as three phases:
1.  Between VA Clinical Health Data Repository (CHDR) and the Master Veteran Index (MVI)
2.  Between Department of Defense (DoD) CHDR and VA CHDR
3.  From Veteran Information Systems Technology Architecture (VistA) to the Health Data Repository (HDR) and VA CHDR
HC will replace VIE which is currently in production for the routing of these messages.
This document provides clients, stakeholders, and support personnel with a smooth transition to HC. It describes how to deploy and install the HC in production as well as how to back out the product to the previous version.
![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/002.png) NOTE: In cases where you are installing a commercial-off-the-shelf (COTS) product, you can use the vendor-provided user guide and installation guide. However, if those guides do *not* include a back-out recovery and rollback strategy, you *must* retain that information in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom HC will be deployed and installed; as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, communications plan, and rollout schedule. Specific instructions for deployment, installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIE supports the routing of messages among several applications. The HC product will ultimately be replacing VIE. During the transition phase both products will be running concurrently.

The success of HC as the messaging solution relies upon the availability of the VistA site administrators performing their part of the deployment in each VistA instance in a timely manner.

The installation of the shared Enterprise and Regional HC instances is *not* within the scope of this deployment, which is dependent upon those instances being installed, configured, and running in production.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HC is an approved product as per the VA’s Technical Reference Model (TRM).

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 1</u> outlines the roles and responsibilities:

| ID  | Team                                     | Phase / Role    | Tasks                                                                                                                                                   | Project Phase (See Schedule) |
|-----|------------------------------------------|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|
|     | FM24 Project Management Office (PMO)     | Deployment      | Plan and schedule deployment (including orchestration with vendors).                                                                                    |                              |
|     |                                          |                 | Determine and document the roles and responsibilities of those involved in the deployment.                                                              |                              |
|     | HC Operations                            | Deployment      | Verify operational readiness, including availability and configuration of servers, configuration of Health Connect, and connectivity among all systems. |                              |
|     | Site and VistA Operations                | Deployment      | Execute deployment, including switch of logical links to HC.                                                                                            |                              |
|     | HC Operations                            | Installation    | Plan and schedule installation.                                                                                                                         |                              |
|     |                                          |                 | Ensure authority to operate and that certificate authority security documentation is in place.                                                          |                              |
|     | InterSystems                             | Installations   | Coordinate training as appropriate.                                                                                                                     |                              |
|     | Development                              | Back-Out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).                                    |                              |
|     | HC Operations/ Development/ InterSystems | Post Deployment | Hardware, Software, and System Support.                                                                                                                 |                              |

<span id="_Ref2348130" class="anchor"></span>Table 2: Outbound Operations for HDR Queues

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 1</u> depicts the current VIE architecture for HDR-CHDR:

<span id="_Ref510009935" class="anchor"></span>Figure 1: Current VIE Architecture for HDR-CHDR

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/003.png)

The FileMan 24 (FM24) Information Technology (IT) Program Management Office (PMO) and Operations leadership have determined that a three-phase release will minimize risk by focusing deployment activities on one distinct message grouping at a time. As shown in <u>Figure 1</u>, a single release of a HC configuration will support three phases of the release:

- Phases 1 and 2 will each be a single event executed on two different days.
- Phase 3 will consist of an Initial Operating Capability (IOC) at two VistA sites over a two-week period, and then a coordinated rapid national deployment to all VistA sites.

## Pre-Rollout Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HealthShare HC Application Support/Operations team performs the following pre-rollout steps:

1.  Submit firewall requests to ensure connectivity in <u>production</u>:
1.  From VistA sites to HC Regional instances
2.  From MVI to HC Enterprise
3.  From HC Enterprise to MVI
4.  From HC Enterprise to VA CHDR
5.  From HC Enterprise to HDR
6.  From HC Enterprise to DoD CHDR
7.  From DoD CHDR to HC Enterprise
4.  Submit IP/Port combinations to HDR Operations for addition to the whitelist.
5.  Perform line-of-site testing for each of the sub-items in step 1 once the network team indicates the firewall configurations have been completed, and HDR team indicates completion of whitelist entries.
6.  Execute the following Structured Query Language (SQL) statement in the Enterprise and each Regional namespace before deploying the Ensemble files to ensure the deployment won’t overwrite or remove the existing settings:

    update Ens_Config.DefaultSettings set Deployable=0
7.  Install the HDR-CHDR production files onto the Enterprise HC Instance. All Inbound Services and Outbound Operations will be disabled.
8.  Install the appropriate production files on each of the Regional HC instances. All Inbound Services and Outbound Operations will be enabled.
9.  Repeat the SQL statement in the Enterprise and each Regional namespace after deploying the Ensemble files:

    update Ens_Config.DefaultSettings set Deployable=0

## Deployment of Phase 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This deployment phase includes message flows between VA CHDR and MVI, as depicted in the interim deployment diagram in <u>Figure 2</u>.

> <span id="_Ref2328976" class="anchor"></span>Figure 2: Release Phase 1

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/004.png)

Implementation of Phase 1 includes the following steps:

1.  The MVI Operations team will disable its logical link to National VIE (IEF APP24).
10. The HC Operations team will enable the Inbound Service (From_MVI_CHDR_7803) to receive messages from MVI.
11. The MVI Operations team will connect its logical link to the Enterprise HC and enable it. The Internet Protocol (IP) information will be communicated to the MVI team securely and separately from this document.
12. The Health Connect Operations team will enable the Outbound Operation (To_VACHDR_MVIJMSQueue) on the Enterprise HC to push messages to the VA CHDR Java Message Service (JMS) Queue DeliveryService.inbound.
13. The VA CHDR team will confirm receipt and successful processing of messages.
14. The VIE Operations team will configure the National VIE (IEF APP24) to stop pulling from the VA CHDR queue DeliveryService.inbound.
15. The VIE Operations team will ensure all messages are processed and none are queued.
16. The HC Operations team will enable the Inbound Service (From_VACHDR_MVIJMSQueue) on the Enterprise HC to pull messages from the VA CHDR JMS Queue DeliveryService.outbound.
17. The HC Operations team will enable the Outbound Operation (To_MVI_VACHDR_5000) on the Enterprise HC to send messages to MVI.
18. The MVI Operations team will validate receipt of processing of messages from VA CHDR.
19. The HC Operations team will confirm bidirectional messaging.
20. The VA CHDR team will look for error codes in audit logs.
21. The AITC WebLogic Admin will validate that there are no error messages.
22. If messaging is successful, continue monitoring, and if not, will work with program management to determine go/no-go next steps.

## Deployment of Phase 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This deployment phase includes message flows between VA CHDR and DoD CHDR, as depicted in the interim deployment diagram in <u>Figure 3</u>.

<span id="_Ref2342096" class="anchor"></span>Figure 3: Release Phase 2

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/005.png)

Implementation of Phase 2 includes the following steps:

> From DoD to VA

1.  The DoD Operations team will disable its logical link to the National VIE (CHDR V21).
2.  The VIE Operations team will confirm the queue is empty.
23. The HC Operations team will enable the Inbound Service (From_DoDCHDR_VACHDR_27315) to receive messages from DoD CHDR.
24. The DoD Operations team will repoint its logical link to the Enterprise HC instance. The IP information will be communicated to the DoD team securely and separately from this document.
25. The HC Operations team will enable the Outbound Operation (To<u>\_</u>VACHDR<u>\_</u>DODCHDRJMSQueue) to push messages to the VA CHDR JMS queue jms.CHDR.DoDtoVAMessageQueue.
26. The VA CHDR team will validate receipt and processing of messages from DoD CHDR.

    From VA to DoD
27. The VIE Operations team will disable its pull from the VA CHDR queue jms.CHDR.VAtoDoDMessageQueue.
28. The VIE Operations team will disable its logical link to the DoD CHDR system.
29. The HC Operations team will enable the Outbound Operation (To_DoDCHDR_VACHDR_27314) to send messages to the DoD CHDR system.
30. The HC Operations team will enable the Inbound Service (From_VACHDR_DoDCHDRJMSQueue) to pull messages from the VA CHDR JMS queue jms.CHDR.VAtoDoDMessageQueue.
31. The DoD CHDR team will validate receipt and processing of messages from VA CHDR.
32. The HC Operations team will confirm bidirectional messaging.
33. If messaging is successful, continue monitoring, and if not, will work with program management to determine go/no-go next steps.

## Deployment of Phase 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This deployment phase includes messages from VistA sites to HDR and VA CHDR, including Prescriptions, Allergies, Labs, and Vitals (all HDR Only), as depicted in <u>Figure 4</u>.

<span id="_Ref2346951" class="anchor"></span>Figure 4: Release Phase 3

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/006.png)

Implementation of Phase 3 consists of the following steps:

1.  The HC Operations team will ensure the Inbound Service (From_VISTA_HDRCHDR_7805), and the Outbound Operation (To<u>\_</u>HDRCHDREnt<u>\_</u>7801) on the <u>Regional</u> HC(s) related to the IOC sites are enabled.
34. The HC Operations team will ensure the Inbound Service (From_VISTA_HDRCHDR_7801) on the <u>Enterprise</u> HC from the <u>Regional</u> HC is enabled.
35. The HC Operations team will enable the Outbound Operations on the <u>Enterprise</u> HC to the HDR JMS queues as described in <u>Table 2</u>.

| Enterprise HC Outbound Operation | HDR JMS Queue                  |
|----------------------------------|--------------------------------|
| To_HDRAllergiesQueue             | jms/cds/AllergiesQueue         |
| To_HDRAllergyAssessmentQueue     | jms/cds/AllergyAssessmentQueue |
| To_HDRPharmacyPartialQueue       | jms/cds/PharmacyPartialQueue   |
| To_HDRPharmacyFullQueue          | jms/cds/PharmacyFullQueue      |
| To_HDRPharmacyRefillQueue        | jms/cds/PharmacyRefillQueue    |
| To_HDRVitalsQueue                | jms/cds/VitalsQueue            |
| To_HDRLabQueue                   | jms/cds/LabQueue               |

<span id="_Ref506222619" class="anchor"></span>Table 3: Site Preparation

36. The HC Operations team will enable the Outbound Operation (To_VACHDR_VISTAJMSQueue) on the <u>Enterprise</u> HC to the VA CHDR JMS queue jms.CHDR.VistAtoCHDRMessageQueue.
37. IOC Sites (Atlanta, GA and Mountain Home, TN) will redirect each of their Logical links (VDEFVIE1-4) to the Regional HC for their site. Specific IP Address and Port will be provided directly to the IOC Sites securely and separately from this document. The IO VistA Application support team should take screenshots of each logical link prior to making any changes should a back-out be necessary.
    1.  VDEFVIE1: Vitals Data
    2.  VDEFVIE2: Allergy Data
    3.  VDEFVIE3: Pharmacy Data
    4.  VDEFVIE4: Laboratory Data

        National Rollout
38. The HC Operations team will ensure the Inbound Services (From_VISTA_HDRCHDR_7805) on <u>all</u> <u>Regional</u> HC(s) are enabled.
39. The HC Operations team will ensure the Outbound Operations (To_HDRCHDREnt_7801) on <u>all Regional</u> HC(s) are enabled.
40. After IOC signoff, the Health Product Support (HPS) team will release informational patch VDEF\*1\*15 for 72-hour application. The Infrastructure Operations VistA Applications team will hold an open conference call with all VistA sites to take a roll call and assist with the redirection of each logical link to point to the appropriate Regional HC. The IO VistA Application support team should take screenshots of each logical link prior to making any changes should a back-out be necessary.
41. The HC Operations team will confirm bidirectional messaging.
42. If messaging is successful, continue monitoring, and if not, will work with program management to determine go/no-go next steps.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

National release of all HDR/CHDR message flows will be done in three phases:

1.  Release Phase 1: VA CHDR and MVI
43. Release Phase 2: VA CHDR and DoD CHDR
44. Release Phase 3: VistA to HDR and VA CHDR

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no preparatory steps at the VA medical center (VAMC) locations for the deployment of the HDR-CHDR messaging flows.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 5</u> depicts the final summary level targeted architecture after all deployment has been completed.

<span id="_Ref2603603" class="anchor"></span>Figure 5: Deployment Topology View

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/007.png)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IOC sites:

- Atlanta, GA (Station \# 508)
- Mountain Home, TN (Station \# 621)

The HealthShare HC software has already been installed in production. There is one Enterprise instance, and six Regional instances:

- Enterprise – Austin Information Technology Center (AITC)
- Region 1 - Sacramento
- Region 1 - Denver
- Region 2 - Philadelphia
- Region 3 - Philadelphia
- Region 4 - Philadelphia
- Region 4 - Brooklyn

Production Operations staff will install the configurations specific to the HDR-CHDR message flows in each of these HC instances.

The MVI, HDR, VA CHDR, and DoD CHDR production instances will be reconfigured in their current locations to connect to the HC Enterprise production instance. No software changes are required in any of these systems.

Each VistA location that issues prescriptions or records patient allergy, vitals, or lab information will need to perform a reconfiguration of the IP address and Port for the HL7 Logical Link (#870) entries VDEFVIE1, VDEFVIE2, VDEFVIE3, or VDEFVIE4. No software changes are required.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> describes preparation required by the site prior to deployment.

| Site/Other                                       | Problem / Change Needed                                      | Features to Adapt/Modify to New Product | Actions/Steps                      | Owner                    |
|--------------------------------------------------|--------------------------------------------------------------|-----------------------------------------|------------------------------------|--------------------------|
| HealthShare HC Enterprise and Regional Instances | Install production configurations for HDR-CHDR message flows | Productions                             | Install Production definition file | HC Production Operations |

<span id="_Ref533083310" class="anchor"></span>Table 4: Download and Import Files

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following support resources will be required during the transition of HDR-CHDR messages from VIE to HC:

- HC Support Operations Team
- VistA HL7 Support, VistA Administrators for each site
- HDR Support Staff
- VA CHDR Support Staff
- DoD CHDR Support Staff
- MVI Support Staff

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section does *not* apply to HL7 HC and HDR-CHDR. Virtual meetings can be used to assist sites as needed.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special hardware requirements for sites using HL7 HC and HDR-CHDR.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HC/HDR-CHDR software deployment is made up of the following (see <u>Table 4</u> for more detail):

HDR-CHDR HC Production Extensible Mark-up Language (XML) files will be placed under configuration control in Rational Configuration Management (CM).

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Communications and notification activities include:

- The VistA administrators will be notified in advance via their monthly community call to introduce them to the strategy and plans for the HDR-CHDR message conversion.
- Patch VDEF\*1\*15 will be released from Forum to all VistA sites via informational patch with implementation to be followed with 72 hours of release. The patch will contain the steps necessary for the VistA administrator to connect to the appropriate HC Regional instance. The information needed to reconfigure the logical links will be provided during a Skype call. Changes are to be made during the Skype call and are only to be performed when directed to do so by the change leader.
- A “roll-call” Skype meeting will be held at IOC and during national release to assist sites with redirecting the logical link and checking compliance.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Platform installation and preparation steps are outlined in the sections below.

## Download and Import Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Definitions for HDR-CHDR HC productions are available under configuration management in the VA Enterprise Rational CM instance. The files in <u>Table 4</u> should be downloaded to the respective HC server. Each file contains specific definitions for each region and the enterprise instance, so they *must* be placed on the appropriate server for deployment.

| HC Instance                | Deployment XML Filename                            |
|----------------------------|----------------------------------------------------|
| HC Region 1 - Sacramento   | Export_HCM_Production_HDR-CHDR_Prod_R1SAC.xml      |
| HC Region 1 – Denver       | Export_HCM_Production_HDR-CHDR_Prod_R1DEN.xml      |
| HC Region 2                | Export_HCM_Production_HDR-CHDR_Prod_R2.xml         |
| HC Region 3                | Export_HCM_Production_HDR-CHDR_Prod_R3.xml         |
| HC Region 4 – Brooklyn     | Export_HCM_Production_HDR-CHDR_Prod_R4BKL.xml      |
| HC Region 4 – Philadelphia | Export_HCM_Production_HDR-CHDR_Prod_R4PHL.xml      |
| HC Enterprise              | Export_HCM_Production_HDR-CHDR_Prod_Enterprise.xml |

1.  As an administrator on the specific HC instance, access the Deploy option:

Management Portal (MP) Ensemble Manage Deployment Changes Deploy

> <span id="_Ref510445689" class="anchor"></span>Figure 6: Management Portal (MP): Deployment Options

> ![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/008.png)

45. Select the HDR-CHDR deployment file, downloaded earlier in Section 4.2, for the correct HC instance. In this example <u>Figure 7</u>, the file name is for eCMS but use the correct filename from <u>Table 4</u>:

Open Deployment Select Deployment file OK

> <span id="_Ref510445421" class="anchor"></span>Figure 7: Selecting Deployment File: HDR-CHDR

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/009.png)

46. When you select OK in <u>Figure 7</u>, the “Deploy Production Changes” screen is displayed, as shown in <u>Figure 8</u>:

> <span id="_Ref510445568" class="anchor"></span>Figure 8: Deploy Production Changes Screen: HDR-CHDR

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/010.png)

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no database creation steps for this deployment.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no installation scripts for this deployment.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cron Scripts do *not* apply to the HC/HDR-CHDR deployment.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following access requirements and skills are needed for installation:

- A user with HC administrative privileges on the Enterprise and Regional production instances will be required to deploy and configure the HDR-CHDR productions.
- At each VistA site, a user with HL7 Menu privileges in production will be required to reconfigure the VDEFVIE1, VDEFVIE2, VDEFVIE3, and VDEFVIE4 Logical links.

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

No database tuning is expected or required for HDR-CHDR on HL7 HC.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The back-out procedure documented in this section is basically the reverse of the deployment procedure. With a rapid roll-out strategy, a significant change to the messaging environment will occur quickly, so a back-out should be a last resort.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The only back-out option is to “un-deploy” HC and repoint MVI, VA CHDR, DoD CHDR, and VistA systems to the VIE last known software configuration and platform settings. This process will identify unsent HDR-CHDR messages on HC and resend to their target systems.

The configuration and operational support will be in place as the VIE platform will still be in production, providing message routing for other applications. Coordination with each site and the operations teams for server configuration and VistA Logical link update will be key to a successful back-out.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIE (for remaining supported applications) and HC (for migrated message flows) will be running in parallel. Since both will be running before and after the deployment, a return to VIE would include reactivating the VIE/HDR-CHDR message flows.

The repointing of the VA CHDR, DoD CHDR and MVI servers and VistA systems will need to be coordinated with site point of contact (POC), VIE, and HC operations.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Load testing is described in a separate document HC HDR-CHDR Performance Test Plan.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary criteria for a back-out decision will be any detrimental impact to patient care. If the deployed software and configuration is irreparably causing loss or damage to HDR-CHDR messages, a back-out may be preferable and timelier than repair to existing configurations. However, this is extremely unlikely given the extensive testing prior to deployment in production.

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

The steps for the back out tasks are below. It is possible that one, two, or all three of the messages flows needs to be backed out, so each procedure has been listed separately below. Depending on which message flow(s) is/are at issue, the appropriate set of steps below should be followed.

### VistA to HDR-CHDR Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps should be followed to return VistA to HDR-CHDR messages to their previous state.

1.  The HC Operations team will identify any messages that were not successfully passed to their destination.
47. The VIE Operations team will re-activate configurations to push HL7 messages to both HDR and VA CHDR.
48. The VIE Operations team will re-activate configurations to accept messages from local VIE instances into the National VIE instance, and all local VIE instance configurations to accept messages from VistA sites.
49. All VistA sites will need to revert their logical links for VDEFVIE1, VDEFVIE2, VDEFVIE3, and VDEFVIE4 to point to the prior VIE local instance.
50. Once all VistA sites have verified the back-out, HC Operations will disable Inbound Services that accept VistA messages for HDR-CHDR on all Regional instances (From<u>\_</u>VISTA<u>\_</u>HDRCHDR<u>\_</u>7805).
51. The HC Operations team will work with VistA sites to re-send any messages identified in Step 1.

### MVI to VA CHDR Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps should be followed to return MVI to VA CHDR messages to their previous state.

1.  The MVI Operations team will disable its logical link to HC Enterprise HDR-CHDR.
52. The HC Operations team will disable the Inbound Service (From_MVI_CHDR_7803).
53. The HC Operations team will disable the Outbound Operation (To<u>\_</u>VACHDR<u>\_</u>MVIJMSQueue) on HC Enterprise.
54. The HC Operations team will disable the Inbound Service (From_VACHDR_MVIJMSQueue) on HC Enterprise.
55. The HC Operations team will disable the Outbound Operation (To_MVI_VACHDR_5000).
56. The VIE Operations team will configure National VIE (CHDR V21) to start pulling from the VA CHDR queue DeliveryService.inbound.
57. The MVI Operations team will reconfigure its logical link to the National VIE (IEF APP24) and enable it.

### VA CHDR and DoD CHDR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps should be followed to return messages between VA CHDR and DoD CHDR to their previous state.

1.  The HC Operations team will disable the Inbound Service (From_VACHDR_DoDCHDRJMSQueue) to stop pulling messages from VA CHDR.
58. The DoD Operations team will disable its logical link to the HC Enterprise instance.
59. The HC Operations team will disable the Outbound Operation (To_DoDCHDR_VACHDR_27314) to stop sending messages to DoD.
60. The HC Operations team will disable the Outbound Operation (To<u>\_</u>VACHDR<u>\_</u>DoDCHDRJMSQueue) to stop pushing DoD messages to CHDR.
61. The VIE Operations team will enable its logical link to the DoD CHDR system.
62. The VIE Operations team will enable its pull from the VA CHDR queue jms.CHDR.VAtoDoDMessageQueue.
63. The DoD Operations team will reconfigure its logical link to send to National VIE (CHDR V21) and enable it.

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HC Operations team will verify that there are no queued transactions in the HC Enterprise or HC Regional instances. If so, they will work with the sending site to resend the message through VIE.

The VIE Operations team will verify that all messages flows are operational and passing messages.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to the nature of the deployment strategy and messaging architecture, a roll-back of processed data is unrealistic and unnecessary. Since the source and target systems do *not* change during the deployment, messages will be processed after the deployment the same way as prior to deployment. Therefore, even if the messaging infrastructure is changed back, no roll-back of data or messages will be required.

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appendix A—HC Production Namespace Configuration and Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/011.png) NOTE: Sections 7.1.1 and 7.1.2 are included for completeness, but should *not* be necessary, since they should already have been completed at this point by previous FileMan 24 HC application installs.

### Creating a New Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new namespace in HC Production, do the following:

1.  Open the following:

System Administration Configuration System Configuration Namespace

64. Click Create New Namespace.
65. Enter the Name of the namespace HCM.
66. Create new database.
67. Enter the name of your database HCM.
68. <span id="create_namespace_step_06" class="anchor"></span>Click on browse next to Create your directory and create a folder with the name of your database HCM.
69. Click Next on the bottom of the screen; use the default settings or the ones recommended by the site administrator.
70. Click Next and select the default.
71. Click Finish.
72. Click on the dropdown Select an existing database for Routines and select the database folder created in [Step 6](#create_namespace_step_06) HCM.
73. Click Save.
74. Namespace HCM will be added to the list of namespaces.

### Deploying a Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deploy a HC Production, do the following:

1.  <span id="deploy_hc_step_01" class="anchor"></span>Copy the deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml) to a path and directory in HealthShare. For example:

/tmp/

75. On the “Health Connect” page, click on the switch that brings a window of all the namespaces.
76. Click on HCM. Verify the namespace value is now changed to HCM.
77. Click on EnsembleManageDeployment changesDeploy.
78. Click on Open Deployment and select the directory in [Step 1](#deploy_hc_step_01).
79. Select the Deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml).
80. The “Deployment Production Changes” screen will display the artifacts that were brought in as part of the xml file.
81. Click on the Deploy tab.
82. Deployment will begin. This will take a few minutes.
83. Go to the following:

Ensemble List Select HCM.Production.HL7RouterProduction

## Appendix B—Starting and Stopping a HC Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/012.png) REF: For details on what occurs when you start or stop a production, see the InterSystems book *Managing Ensemble Productions*.

### Starting Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start a HC Production, do the following:

1.  Log in to the Management Portal.
84. Change to the appropriate namespace.
85. Go to the “Production List” page:

Ensemble List Productions

86. Find the production in the list and click it.
87. Click the Open button at the top of the list.
88. On the resulting “Production Configuration” page, click Start to display a dialog box.
89. In the dialog box, click Open. The system displays a new dialog box with the name of the production, its startup status, and any associated messages.

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/013.png) NOTE: The system may also open Terminal windows. Do *not* close these windows. Click the OK button when it is displayed in the dialog box.

### Stopping HC Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To stop a HC Production, do the following:

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/014.png) NOTE: During this process ensure the HC operation is disabled before stopping it.

1.  Log in to the HealthShare Management Portal.
90. Change to the appropriate namespace.
91. Go to the “Production List” page:

Ensemble List Productions

92. Find the production in the list and click it.
93. Click the Open button at the top of the list.
94. On the resulting “Production Configuration” page, click Stop to display a dialog box.
95. In the dialog box, click OK. The system displays a new dialog box with the following:
- Name of the production.
- Shutdown status.
- Any associated messages.

![](vdef-1-15-hdr-chdr-deployment-installation-back-out-and-rollback/015.png) NOTE: The system may also open Terminal windows. Do *not* close these windows. Click the OK button when it is displayed in the dialog box.