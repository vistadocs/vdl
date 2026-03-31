---
title: PSO*7*522 Health Connect/Outpatient Pharmacy Automated Interface (OPAI) Version 1
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Health Connect/Outpatient Pharmacy Automated Interface (OPAI) Version 1
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*522
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - connect
  - health
  - table
  - contents
  - opai
  - span
  - production
  - deployment
  - class
  - back
page_count: 0
word_count: 6032
section_count: 34
table_count: 3
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: March 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_p522_opai_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/pso_7_p522_opai_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>InterSystems Health Connect (HC) / Outpatient Pharmacy Automation Interface (OPAI) 1.0

  PSO\*7\*522

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/001.png)

March 2019

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

<span id="_Toc2872182" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref520206071" class="anchor"></span>Table 1: Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 45%" />
<col style="width: 26%" />
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
<td>03/06/2019</td>
<td>1.0</td>
<td>Final DIBRG Release Document.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>02/27/2019</td>
<td>0.12</td>
<td>Updated TBD dates for IOC/National release on pg <a href="#site-readiness-assessment">6</a> and <a href="#communications">9</a>, updated date in footer and cover page.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>12/18/2018</td>
<td>0.11</td>
<td>Updated sections at 5 and 6.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/10/2018</td>
<td>0.10</td>
<td><p>Tech Edit Review and Updates:</p>
<ul>
<li><p>Accepted all changes to date.</p></li>
<li><p>Missing dates in Section <u>3.3.4</u>.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/27/2018</td>
<td>0.9</td>
<td><p>Tech Edit Review and Updates:</p>
<ul>
<li><p>Reviewed prior edited sections by contractor, since last VA tech writer review. Accepted all changes and removed flagging comments with exceptions shown in next bullet.</p></li>
<li><p>Updated Sections: <u>3.2</u> (see reviewer comment/question), <u>3.2.1</u>, <u>4.1.1</u>, <u>4.1.1.1</u> (new Header); <u>Figure 5</u> (see reviewer comment/question), <u>5.2.2</u>, <u>5.3</u>, and <u>5.4</u>.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/12/2018</td>
<td>0.8</td>
<td>Updated the following sections: <u>3.2</u>, <u>3.2.1</u>, <u>3.2.3</u>, <u>4.2</u>, <u>5.2.1</u>, <u>5.2.2</u>, and <u>6.1</u>.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/05/2018</td>
<td>0.7</td>
<td>Added Section <u>4.1.1</u>, “<u>Pre-Install VistA Check</u>.”</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/09/2018</td>
<td>0.6</td>
<td><p>Halfaker Review of Reviewer Edits:</p>
<ul>
<li><p>Corrected acronym to reflect "Health Connect” in Section <a href="#purpose"><u>1.1</u></a>.</p></li>
<li><p>Removed diagram in system architecture in Section <a href="#_Deployment"><u>3</u>,</a> <u>Figure 1</u>.</p></li>
<li><p>Provided elaboration on Section <a href="#download-and-extract-files"><u>4.3</u></a>, <u>Figure 8</u>.</p></li>
<li><p>Provided elaboration on Appendix A Section <a href="#appendix-ahealth-connect-production-namespace-configuration-and-deployment"><u>7.1.2</u></a>, item 6.</p></li>
<li><p>Provided elaboration on Appendix B Section <a href="#appendix-bconfiguring-a-health-connect-production"><u>7.2</u></a>, item 1e.</p></li>
<li><p>Updated Appendix B Section <a href="#appendix-bconfiguring-a-health-connect-production"><u>7.2</u></a>, item 2a to reflect OPAI.</p></li>
<li><p>Updated Appendix B Section <a href="#appendix-bconfiguring-a-health-connect-production"><u>7.2</u></a>, item 3a to reflect OPAI.</p></li>
<li><p>Updated Appendix B Section <a href="#appendix-bconfiguring-a-health-connect-production"><u>7.2</u></a>, item 5d to reflect “e.g.”</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/24/2018</td>
<td>0.5</td>
<td><p>VA Tech Edit Review:</p>
<ul>
<li><p>Accepted all vendor documentation changes to date.</p></li>
<li><p><u>1</u>: Updated content based on contractor review/edits.</p></li>
<li><p><u>2</u>: Updated <u>Table 1</u> for “FM24” project entry.</p></li>
<li><p><u>3</u>: Added “OPAI” throughout to clarify when content was specific to OPAI messages.<br />
<br />
Also, replaced “Palo Alto, CA” site with “Oklahoma City, OK.”</p></li>
<li><p><u>3.2.2</u>: Listed current IOC sites.</p></li>
<li><p><u>3.2.3</u>: Updated <u>Table 2</u>.</p></li>
<li><p><u>3.3</u>: Updated resource bullet list.</p></li>
<li><p><u>3.3.1</u>: Facility Specifics, updated text.</p></li>
<li><p><u>3.3.2</u>: Hardware, updated text.</p></li>
<li><p><u>3.3.4</u>: Updated date bullets; pending final dates.</p></li>
<li><p><u>4.3</u>: Reformatted procedural steps.</p></li>
<li><p>Added boldface to patch IDs, file names, etc. throughout.</p></li>
</ul>
<p>Minor formatting updates throughout.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>06/11/2018</td>
<td>0.4</td>
<td><p>VA Tech Edit Review. Accepted all vendor documentation changes to date:</p>
<ul>
<li><p>Updated <u>Figure 7</u>, <u>Figure 8</u>, and <u>Figure 10</u>.</p></li>
<li><p>Corrected “<a href="#rollout_procedure">Rollout Procedure</a>” <a href="#v1">V1</a> and <a href="#p1">P1</a> steps in Section <u>3</u>.</p></li>
<li><p>Added site information to <u>Table 2</u>.</p></li>
<li><p>Updated XML file reference in Section <u>3.3.3</u>.</p></li>
<li><p>Updated Section <u>4.6</u>.</p></li>
<li><p>Corrected sample operation names in Section <u>7.2</u>,, Step 2a and Step 4d.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/06/2018</td>
<td>0.3</td>
<td><p>Halfaker Review of Tech Edits:</p>
<ul>
<li><p>Architect (DE) and developer(GS) addressed as many items as possible at this time.</p></li>
<li><p>Updated revision and sent back for VA TW review.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/17/2018</td>
<td>0.2</td>
<td><p>VA Tech Edit Review:</p>
<ul>
<li><p>Reformatted document to follow current OIT documentation standards and style guidelines.</p></li>
<li><p>Removed intranet links (inside the VA firewall), since this document will be located on the internet (outside the VA firewall).</p></li>
<li><p>Reviewed and edited document for Section 508 conformance (e.g., added alternate text to all images).</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>05/07/2018</td>
<td>0.1</td>
<td>Initial document based on the Veteran-focused Integration Process (VIP) Deployment, Installation, Back-Out, and Rollback Guide template Version 2.2, released on March 2016.</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<span id="_Ref520206071" class="anchor"></span>Table 1: Roles and Responsibilities

Table of Contents

<span id="_Toc2872183" class="anchor"></span>List of Figures

<span id="_Toc2872184" class="anchor"></span>List of Tables

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
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
    - [Pre-Install VistA Check](#pre-install-vista-check)
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
- [Appendices](#appendices)
  - [Appendix A—Health Connect Production Namespace Configuration and Deployment](#appendix-ahealth-connect-production-namespace-configuration-and-deployment)
    - [Creating a New Namespace](#creating-a-new-namespace)
    - [Deploying a Health Connect Production](#deploying-a-health-connect-production)
  - [Appendix B—Configuring a Health Connect Production](#appendix-bconfiguring-a-health-connect-production)
  - [Appendix C—Starting and Stopping a Health Connect Production](#appendix-cstarting-and-stopping-a-health-connect-production)
    - [Starting Health Connect Production](#starting-health-connect-production)
    - [Stopping Health Connect Production](#stopping-health-connect-production)
This document describes the deployment, installation, back-out, and rollback instructions for the migration of Outpatient Pharmacy Automation Interface (OPAI) 1.0 from the Vitria Interface Engine (VIE) to InterSystems Health Connect (HC).
HC will replace VIE; currently in production, for the routing of OPAI messages.
This document includes information about:
- System support
- Issue tracking
- Escalation processes
- Roles and responsibilities involved in all activities
It provides clients, stakeholders, and support personnel with a smooth transition to Health Connect. It describes how to deploy and install the Health Connect in production as well as how to back out the product and roll back to a previous version or data set.
![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/002.png) NOTE: In cases where you are installing a *non*-developed commercial-off-the-shelf (COTS) product, you can use the vendor-provided user guide and installation guide. However, if those guides do *not* include a back-out recovery and rollback strategy, you must retain that information in this document.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the Health Connect (HC) will be deployed and installed; as well as how it is to be backed out and rolled back, if necessary. The guide also identifies resources, communications plan, and rollout schedule. Specific instructions for deployment, installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIE supports the routing of messages from several applications. Health Connect product will ultimately be replacing VIE. During the transition phase both products will be running concurrently.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HC is an approved product as per the VA’s Technical Reference Model (TRM). Defining the controls and constraints need to be determined.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ID  | Team                                 | Phase / Role    | Tasks                                                                                                                | Project Phase (See Schedule) |
|-----|--------------------------------------|-----------------|----------------------------------------------------------------------------------------------------------------------|------------------------------|
|     | FM24 PMO                             | Deployment      | Plan and schedule deployment (including orchestration with vendors).                                                 |                              |
|     |                                      |                 | Determine and document the roles and responsibilities of those involved in the deployment.                           |                              |
|     | Operations and End-User              | Deployment      | Test for operational readiness.                                                                                      |                              |
|     | Site and Operations                  | Deployment      | Execute deployment.                                                                                                  |                              |
|     | Operations                           | Installation    | Plan and schedule installation.                                                                                      |                              |
|     |                                      |                 | Ensure authority to operate and that certificate authority security documentation is in place.                       |                              |
|     |                                      |                 | Validate through facility POC to ensure that IT equipment has been accepted using asset inventory processes.         |                              |
|     | InterSystems                         | Installations   | Coordinate training.                                                                                                 |                              |
|     | Development                          | Back-Out        | Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out). |                              |
|     | Operations/Development/ InterSystems | Post Deployment | Hardware, Software, and System Support.                                                                              |                              |

<span id="_Ref506222619" class="anchor"></span>Table 2: Site Preparation

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 1</u> depicts the current VistA Interface Engine (VIE) architecture for OPAI:

<span id="_Ref510009935" class="anchor"></span>Figure 1: Current VIE Architecture for OPAI

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/003.png)

A parallel deployment of Health Connect (HC) is planned at a regional level. The VIE OPAI functionality will remain in place at each region. At Region 1, the OPAI Health Connect Production will run concurrently with VIE, replacing only the VIE OPAI functionality for the following Initial Operating Capabilities (IOC) sites:

- Tucson, AZ
- Oklahoma City, OK

VIE will stay online until the migration of all sites to Health Connect is complete. Should a failback be required, VIE will be online to serve that purpose.

VIE will continue to process messages for applications that have *not* yet been migrated. The Health Connect OPAI production will process OPAI messages.

This section provides the schedule and milestones for the deployment.

<u>Figure 2</u> depicts the interim VIE and Health Connect architecture during the IOC rollout for OPAI:

<span id="_Ref510158921" class="anchor"></span>Figure 2: IOC Rollout Breakdown for OPAI (Interim Architecture)

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/004.png)

In summary, the IOC sites and Health Connect operations support will provide the port addresses for OPAI message traffic. As the VIE will be running on the old ports, Health Connect will use new ones. When an OPAI server transitions to the new ports, the message traffic is redirected through Health Connect. The informational patch PSO\*7\*522 instructs the Veterans Health Information Systems and Technology Architecture (VistA) system administrators to change the logical link to redirect OPAI messages to the new Health Connect port and will no longer direct OPAI messages to VIE.

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/005.png) REF: For details on how a OPAI production is deployed and configured, see <u>Appendix A—Health Connect Production Namespace Configuration and Deployment</u>.

On completion of the port configuration update for OPAI server and VistA logical link, the OPAI message traffic will be rerouted through the OPAI Health Connect production (see <span class="mark"></span><u>Figure 3</u>):

<span id="_Ref508859461" class="anchor"></span>Figure 3: VIE, Health Connect, and OPAI Deployment Architecture and Rollout Procedure

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/006.png)

<span id="rollout_procedure" class="anchor"></span>Rollout Procedure

This is a First-In-First-Out (FIFO) interface. This means that when rolling out OPAI from the VIE to the Health Connect interface, the outstanding OPAI VIE messages should be processed prior to starting the processing of messages through the Health Connect interface:

<span id="v1" class="anchor"></span>V1 (<u>Figure 3</u>; Rollout Process: VistA System to Health Connect):

- Ensure the Health Connect OPAI operation(s) is switched off (disabled).
- Change the OPAI VistA logical link to point to the VistA listener on Health Connect.
- Verify that all OPAI messages are processed through VIE before OPAI messages are sent from Health Connect.
- Verify the OPAI messages are waiting to be processed through the Health Connect OPAI operation (disabled).
- Once verified, the Health Connect OPAI operation is switched on (enabled).

<span id="p1" class="anchor"></span>P1 (<u>Figure 3</u>; Rollout Process: Health Connect to OPAI IOC Application Servers):

- Ensure the Health Connect VistA operation is switched off (disabled).
- Change the OPAI server to point to the OPAI listener on the Health Connect server.
- Verify that all OPAI messages are processed through VIE before OPAI messages are sent from Health Connect.
- Verify the OPAI messages are waiting to be processed through Health Connect VistA operation (disabled).
- Once verified, the Health Connect VistA operation is switched on (enabled).

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployment timeline of four (4) hours has been allocated for IOC.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Regional Health Connect locations will need a site readiness assessment prior to deployment. OPAI servers will need to be pointed to those servers. Once sites are determined, site readiness assessments will need to be scheduled to prepare for deployment:

- IOC testing performed in mirror accounts:

<span class="mark">REDACTED</span>

- Line of sight testing was scheduled and performed prior to deployment:

<span class="mark">REDACTED</span>

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OPAI deployment topology is depicted in <u>Figure 4</u>:

<span id="_Ref531075534" class="anchor"></span>Figure 4: OPAI Deployment Topology

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/007.png)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IOC sites:

- <span class="mark">REDACTED</span>

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2</u> describes preparation required by the site prior to deployment.

| Site/Other            | Problem / Change Needed                                                     | Features to Adapt/Modify to New Product                    | Actions/Steps                                                                     | Owner                             |
|-----------------------|-----------------------------------------------------------------------------|------------------------------------------------------------|-----------------------------------------------------------------------------------|-----------------------------------|
| Tucson, AZ        | Establish IP communication                                                  | Not Applicable (N/A)                                       | Ensure listener is enabled and ACL allows HealthShare servers IP range to connect | Local IT Admin or Dispenser Admin |
|                       | Standard acknowledgment (ACK) for RDS_O13 transmitted from ScriptPro server | Vendor provides patch to be installed on ScriptPro server  | Vendor installs patch on ScriptPro server                                         | Vendor                            |
| Oklahoma City, OK | Establish IP communication                                                  | N/A                                                        | Ensure listener is enabled and ACL allows HealthShare servers IP range to connect | Local IT Admin or Dispenser Admin |
|                       | Innovation devices need transmit standard RRD_O14 response                  | Vendor provides patch to be installed on Innovation server | Vendor installs patch on Innovation server                                        | Vendor                            |

<span id="_Ref510443929" class="anchor"></span>Table 3: Deployment/Installation/Back-Out Checklist (Print Out When Needed)

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following support resources will be available with OPAI:

- Pharmacy Personnel
- Pharmacy Automation Data Processing Application Coordinator (ADPAC)
- Health Connect Support Operations Team
- VistA HL7 Support, VistA Patch Installer
- OPAI Equipment Vendor Support

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section does *not* apply to HL7 Health Connect and OPAI. Virtual meetings can be used to assist sites; similar to what was used for IOC testing sessions.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special hardware requirements for sites using HL7 Health Connect and OPAI.

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/008.png) REF: For details about who is responsible for preparing the site to meet these hardware specifications, see <u>Table 1: Roles and Responsibilities</u>.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OPAI software deployment is made up of the following:

- OPAI Health Connect Production Extensible Mark-up Language (XML) file (e.g., Export-HCM_Production_HL7RouterProduction_OPAIv1.xml)—The Health Connect XML file will be delivered from the Community Resource and Referral Center (CRRC) development/test environment.
- Informational PSO\*7\*522 is available on FORUM.

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/009.png) REF: For details about who is responsible for preparing the site to meet these software specifications, see <u>Table 1: Roles and Responsibilities</u>.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Communications and notification activities include:

- Kick Off meetings:
- IOC Kick Off: 06/12/2018
- National Release Kick Off Planned for: 3/25/2019
- <span class="mark">REDACTED</span>
- <span class="mark">REDACTED</span>

#### Deployment/Installation/Back-Out Checklist

For rollback procedures, see Section <u>6</u>, “<u>Rollback Procedure</u>.”

| Activity | Day | Time | Individual Who Completed Task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HCM namespace for the Health Connect production needs to be created for every deployment of Health Connect.

### Pre-Install VistA Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following word-processing fields of the OUTPATIENT SITE (#59) file may contain “blank lines” with control characters that may cause incorrect HL7 message termination during processing:

- NARRATIVE FOR COPAY DOCUMENT (#59.01004) field
- NARRATIVE REFILLABLE RX (#59.01005) field
- NARRATIVE NON-REFILLABLE RX (#59.01006) field

To correct this by removing blank lines from these fields, follow the steps in the “<u>Narrative Validation</u>” section. (Also, see the “Performing the Implementation” section in the *Outpatient Pharmacy Automation Interface Installation Guide*.)

#### Narrative Validation

To remove blank lines from fields, do the following:

1.  Check the following fields in the OUTPATIENT SITE (#59) file:
- NARRATIVE FOR COPAY DOCUMENT (#59.01004)
- NARRATIVE REFILLABLE RX (#59.01005)
- NARRATIVE NON-REFILLABLE RX (#59.01006)

These are word-processing fields, containing information from the site regarding the procedures for the patient to follow; information may include telephone numbers, mailing addresses, etc. Information in these parameters may incorporate "blank lines" with control characters that may cause incorrect HL7 message termination during processing.

2.  Edit the fields in Step 1 as necessary to remove "blank lines" with control characters.
3.  Save changes to the edited fields.

<span id="_Ref531076671" class="anchor"></span>Figure 5: Sample Narrative Validation—Narrative Non-Refillable RX parameter  
(NOTE: Some options have been skipped to save room for the example.)

NARRATIVE REFILLABLE RX

NARRATIVE REFILLABLE RX:. . .

. . .

machinery.\\sp\May cause dizziness\\sp\May cause blurred vision\\sp\Call

your doctor immediately if you have mental/mood changes like confusion,

new/worsening feelings of sadness/fear, thoughts of suicide, or unusual

behavior.\\sp\Do not take aluminum or magnesium antacids within 2 hours

of taking this medication.\\sp\It is very important that you take or use

this exactly as directed. Do not skip doses or discontinue unless

directed by your doctor.\\sp\Read the Medication Guide that comes with

this medicine\|Drug Warning Narrativevisit

<span class="mark">REDACTED</span> .

Edit? NO// <span class="mark">YES</span>

==\[ WRAP \]==\[INSERT \]========\< NARRATIVE REFILLABLE R\[Press \<PF1\>H for help\]====

May cause drowsiness. Alcohol and marijuana may intensify this effect.

Use care when operating a vehicle, vessel (e.g., boat), or

machinery.\\sp\May cause dizziness\\sp\May cause blurred vision\\sp\Call

your doctor immediately if you have mental/mood changes like confusion,

new/worsening feelings of sadness/fear, thoughts of suicide, or unusual

behavior.\\sp\Do not take aluminum or magnesium antacids within 2 hours

of taking this medication.\\sp\It is very important that you take or use

this exactly as directed. Do not skip doses or discontinue unless

directed by your doctor.\\sp\Read the Medication Guide that comes with

this medicine\|Drug Warning Narrativevisit

http://www.va.gov/healthbenefits/cost/copay_rates.asp.

\[<span class="mark">eof</span>\]

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

NARRATIVE REFILLABLE RX modified:

==\[ WRAP \]==\[INSERT \]========\< NARRATIVE REFILLABLE R\[Press \<PF1\>H for help\]====

May cause drowsiness. Alcohol and marijuana may intensify this effect.

Use care when operating a vehicle, vessel (e.g., boat), or

machinery.\\sp\May cause dizziness\\sp\May cause blurred vision\\sp\Call

your doctor immediately if you have mental/mood changes like confusion,

new/worsening feelings of sadness/fear, thoughts of suicide, or unusual

behavior.\\sp\Do not take aluminum or magnesium antacids within 2 hours

of taking this medication.\\sp\It is very important that you take or use

this exactly as directed. Do not skip doses or discontinue unless

directed by your doctor.\\sp\Read the Medication Guide that comes with

this medicine\|Drug Warning Narrativevisit

http://www.va.gov/healthbenefits/cost/copay_rates.asp.

\[<span class="mark">eof</span>\]

Do you want to save changes? <span class="mark">YES</span>

\<=======T=======T=======T=======T=======T=======T=======T=======T=======T\>======

Saving text ....

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/010.png) REF: For deployment steps, see [<u>Appendix A—Health Connect Production Namespace Configuration and Deployment</u>](#appendix-ahealth-connect-production-namespace-configuration-and-deployment).

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Platform installation and preparation steps are outlined in the sections that follow.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment of the OPAI production is achieved by extracting a Health Connect deployment file (HCM_Production_HL7RouterProduction-Deploy1.1.xml) through the Health Connect Menu.

To download and extract the files, do the following:

1.  Access the Deploy option:

Management Portal (MP) Ensemble Manage Deployment Changes Deploy

> <span id="_Ref510445689" class="anchor"></span>Figure 6: Management Portal (MP)—Deployment Options

> REDACTED

4.  Select the OPAI deployment file (e.g., Export-HCM_Production_HL7RouterProduction-20180605104008_OPAIv1.xml):

Open Deployment Select Deployment file Ok

> <span id="_Ref510445421" class="anchor"></span>Figure 7: SM—Selecting Deployment File: OPAI

> REDACTED

5.  When you select Deploy (<u>Figure 7</u>), the Deploy Production Changes screen is displayed, as shown in <u>Figure 8</u>:

> <span id="_Ref510445568" class="anchor"></span>Figure 8: SM—Deploy Production Changes Screen: OPAI

> REDACTED

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/011.png) REF: For deployment steps, see [Appendix A](#appendix-ahealth-connect-production-namespace-configuration-and-deployment).

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Database created by infrastructure team as part of IOC deployment. The Health Connect HL7 Messaging Production Operations Manual (POM; HC-HL7_Messaging_1_0_POM.pdf) provides database details.

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/012.png) REF: The HC-HL7_Messaging_1_0_POM.pdf document is stored on the EHRM FM24 Documentation Jazz RTC repository.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no installation scripts for this installation.

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/013.png) REF: For deployment steps, see [Appendix A](#appendix-ahealth-connect-production-namespace-configuration-and-deployment).

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cron Scripts do *not* apply to the Health Connect/OPAI deployment.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users require Administration privileges to create a database for every installation of InterSystems Health Connect (HealthShare). Subsequent deployments should *not* require this level of access, as the latest Health Connect production deployment will be done through the Health Connect menu.

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/014.png) REF: For deployment steps, see [Appendix A](#appendix-ahealth-connect-production-namespace-configuration-and-deployment).

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For deployment steps, see [Appendix A](#appendix-ahealth-connect-production-namespace-configuration-and-deployment).

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For installation and verification procedure, see [Step 10](#deploy_hc_step_10) under the [deployment procedure](#deploying-a-health-connect-production) in [Appendix A](#appendix-ahealth-connect-production-namespace-configuration-and-deployment).

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start the OPAI Health Connect production, follow the steps in [Appendix C](#appendix-cstarting-and-stopping-a-health-connect-production).

Once the production is running, the OPAI production business services, operations, and routers should be enabled (See [Appendix B](#appendix-bconfiguring-a-health-connect-production)).

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, no database tuning is expected or required for OPAI on HL7 Health Connect.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since this is a first time install, the only back-out option is to un-deploy Health Connect (HC) and repoint OPAI to VistA Interface Engine (VIE) last known software configuration and platform settings.

The back-out process will repoint OPAI servers and the VistA logical links back to the VIE instance. This process will identify unsent OPAI messages on Health Connect and resend to OPAI/VistA.

The configuration and operational support will be in place as the VIE platform will still be in production, providing message routing for other applications. Coordination with each site and the operations teams (if VIE and Health Connect use different resources) for server configuration and VistA logical link update will be key to a successful back-out.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIE (for remaining supported applications) and Health Connect (for migrated OPAI and other sites) will be running in parallel (see <u>Figure 3</u>).

The repointing of OPAI servers and VistA systems would need to be coordinated with site point of contact (POC), VIE, and Health Connect operations.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable (N/A).

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was performed in IOC mirror testing. Execution results are attached in Section <u>3.2</u>, “<u>Site Readiness Assessment</u>.”

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out criteria will be any impact to patient care.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out risks are to the schedule of the Health Connect (HC) / VistA Interface Engine (VIE) migration project.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authority for back-out will be determined by the following:

- <span class="mark">REDACTED</span>
- <span class="mark">REDACTED</span>

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out procedures are determined to be the same for this initial deployment of OPAI on HL7 Health Connect.

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following group will determine if messages are passing on VIE server if back out required:

<span class="mark">REDACTED</span> <span id="_Rollback_Procedure" class="anchor"></span>

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rollback option is to un-deploy Health Connect (HC) and repoint the OPAI devices to the VistA Interface Engine (VIE) last known software configuration and platform settings.

Secondly, the VistA logical links need to point back to the VIE instance. This process will identify unsent OPAI messages on Health Connect and resend to OPAI/VistA (see [<u>Figure 9</u>](#_Rollback_Procedure) for rollback procedure).

The repointing of OPAI servers and VistA systems would need to be coordinated with the site point of contact (POC), VIE, and Health Connect operations, the site's outpatient pharmacy department, OPAI vendor(s) and OIT HL7 Support Analyst.

Migration to Health Connect is occurring during off-hours when no prescription dispense requests will be transmitted. Test messages will be sent to confirm successful migration to Health Connect and would *not* be needed to be resent in case a rollback is required. Any production messages (*not* test messages) that might be submitted during migration and would require resubmission and would need to be coordinated with the site point of contact, VIE operations, and Health Connect operations.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback criteria will be any impact to patient care.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback risks are to the schedule for the Health Connect (HC)/VistA Interface Engine (VIE) migration project.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authority for rollback will be determined by the following:

- <span class="mark">REDACTED</span>
- <span class="mark">REDACTED</span>

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a First-In-First-Out (FIFO) interface, which means that when rolling back from the Health Connect (HC) interface, the Health Connect messages should be processed prior to processing messages through the VistA Interface Engine (VIE) interface.

<u>Figure 9</u> depicts the rollback procedure from OPAI messaging on Health Connect back to VIE:

<span id="_Ref508868415" class="anchor"></span>Figure 9: Rollback Procedure from OPAI Messaging on Health Connect Back to VIE

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/015.png)

V2 (<u>Figure 9</u>; Rollback Process: VistA System to VIE):

- Ensure the Health Connect VistA listener is switched off (disabled).
- Verify that all OPAI messages are processed through Health Connect to OPAI before OPAI messages are sent from VIE.

  Once verified, the OPAI logical link in VistA is pointed to VIE. Here are the steps involved for repointing the VistA logical link IP address and port back to the VIE IP address and port:
- Stop the PSO DISP Logical Link with HL7 Menu option: Start/Stop Links
- Edit the PSO DISP Logical Link with HL7 menu option: Link Edit.
- Edit the HL LOGICAL LINK for PSO DISP and replace the existing TCP/IP ADDRESS and existing TCP/IP PORT with the VIE IP address and port.
- Once it has been confirmed that VIE is ready to process messages, start the PSO DISP Logical Link using the Start/Stop Links option.

P2 (<u>Figure 9</u>; Rollback Process: VIE to OPAI IOC Application Servers):

- Ensure the Health Connect OPAI listener is switched off (disabled).
- Verify that all OPAI messages are processed through Health Connect to VistA before OPAI messages are sent from VIE.
- Once verified, the OPAI server is configured to point to VIE.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following group will verify the rollback when it determines that messages are passing successfully on the VIE server, and if a rollback is required:

<span class="mark">REDACTED</span>

# Appendices

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Appendix A—Health Connect Production Namespace Configuration and Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Creating a New Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a new namespace in Health Connect Production, do the following:

1.  Open the following:

System Administration Configuration System Configuration Namespace

6.  Click Create New Namespace.
7.  Enter the Name of the namespace HCM.
8.  Create new database.
9.  Enter the name of your database HCM.
10. <span id="create_namespace_step_06" class="anchor"></span>Click on browse next to Create your directory and create a folder with the name of your database HCM.
11. Click Next on the bottom of the screen; use the default settings or the ones recommended by the site administrator.
12. Click Next and select the default.
13. Click Finish.
14. Click on the dropdown Select an existing database for Routines and select the database folder created in [Step 6](#create_namespace_step_06) HCM.
15. Click Save.
16. Namespace HCM will be added to the list of namespaces.

### Deploying a Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deploy a Health Connect Production, do the following:

1.  <span id="deploy_hc_step_01" class="anchor"></span>Copy the deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml) to a path and directory in HealthShare. For example:

/tmp/

17. On the “Health Connect” page, click on the switch that brings a window of all the namespaces.
18. Click on HCM. Verify the namespace value is now changed to HCM.
19. Click on EnsembleManageDeployment changesDeploy.
20. Click on Open Deployment and select the directory in [Step 1](#deploy_hc_step_01).
21. Select the Deployment file (e.g., Export-HCM_Production_HL7RouterProduction-Deploy1.0.xml).
22. The “Deployment Production Changes” screen will display the artifacts that were brought in as part of the xml file.
23. Click on the Deploy tab.
24. Deployment will begin. This will take a few minutes.
25. <span id="deploy_hc_step_10" class="anchor"></span>Go to the following:

Ensemble List Select HCM.Production.HL7RouterProduction

## Appendix B—Configuring a Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To configure a Health Connect Production, do the following:

1.  Configure connection details on Business Services:
1.  Select a business service (e.g., From_DU459_OPAI).
2.  Click on the Settings tab on the right.
3.  Select the Enabled checkbox.
4.  Enter the designated port.
5.  Verify the Stay Connected setting is set to a value of -1.
6.  Click Apply.
26. <span id="configure_hc_prod_step_2" class="anchor"></span>Configure connection details on Business Operations:
1.  Select a business operation (e.g., To_OPAI678_Scriptpro_9600, EMailAlert.OperationOPAI, and BadMessageHandlerOPAI).
7.  Click on the Settings tab on the right.
8.  Select the Enabled checkbox (uncheck to disable).
9.  Enter the IP address of the OPAI Dispensing Device
10. Enter the designated port.
11. Click Apply.
27. Enable the business process:
1.  Select business process related to OPAI (e.g., OPAI_InRouter, OPAI_OutRouter, OutRouter, InRouter, and Ens.Alert).
12. Click on Settings tab on the right.
13. Select Enabled checkbox.
14. Click Apply.
28. The Point of Reference is Vista and all messages send out from Vista will have the OPAI device details in the Outbound table. The Inbound table will have the Vista Domain names since these are messages coming into Vista.
29. To Update Inbound and Outbound tables:
1.  Go to the following:

Ensemble Configure Data Lookup Tables

15. Go to the following:

Open HCM OutboundRouter Table

16. Enter Key \[e.g., this is MSH(6.2) segment receiving institution from the HL7 Message\].
17. Enter Value (e.g., To_OPAI678_Scriptpro_9600 operation).
30. Start the Health Connect Production by clicking the Start button in the “Production Configuration” screen (see <u>Figure 10</u>).

> <span id="_Ref508864945" class="anchor"></span>Figure 10: InterSystems HealthShare—Production Configuration Screen: OPAI

> ![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/016.png)

## Appendix C—Starting and Stopping a Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/017.png) REF: For details on what occurs when you start or stop a production, see the InterSystems book *Managing Ensemble Productions*.

### Starting Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start a Health Connect Production, do the following:

1.  Log in to the Management Portal.
31. Change to the appropriate namespace.
32. Go to the “Production List” page:

Ensemble List Productions

33. Find the production in the list and click it.
34. Click the Open button at the top of the list.
35. On the resulting “Production Configuration” page, click Start to display a dialog box.
36. In the dialog box, click Open. The system displays a new dialog box with the name of the production, its startup status, and any associated messages.

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/018.png) NOTE: The system may also open Terminal windows. Do *not* close these windows. Click the OK button when it is displayed in the dialog box.

### Stopping Health Connect Production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To stop a Health Connect Production, do the following:

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/019.png) NOTE: During this process ensure the Health Connect operation is disabled  
(see [Appendix B](#appendix-bconfiguring-a-health-connect-production), [Step 2](#configure_hc_prod_step_2), “Configure connection details on Business Operations”).

1.  Log in to the HealthShare Management Portal (Cache Cube).
37. Change to the appropriate namespace.
38. Go to the “Production List” page:

Ensemble List Productions

39. Find the production in the list and click it.
40. Click the Open button at the top of the list.
41. On the resulting “Production Configuration” page, click Stop to display a dialog box.
42. In the dialog box, click OK. The system displays a new dialog box with the following:
- Name of the production.
- Shutdown status.
- Any associated messages.

![](pso-7-522-health-connect-outpatient-pharmacy-automated-interface-opai-version-1/020.png) NOTE: The system may also open Terminal windows. Do *not* close these windows. Click the OK button when it is displayed in the dialog box.