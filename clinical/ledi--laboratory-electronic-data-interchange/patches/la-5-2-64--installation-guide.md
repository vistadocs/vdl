---
title: LA*5.2*64/LR*5.2*286 LDSI National Implementation Plan V.1.10
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: LEDI
app_name: "Laboratory: Electronic Data Interchange"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*64
group_key: "LEDI:LA:5.2"
file_numbers: []
security_keys: []
menu_options: 2
description: - [# Introduction](#introduction) - [Document Purpose](#document-purpose) - [Project Description](#project-description) - [Project Purpose](#project-purpose) - [Project Background](#project-background) - [Project Documentation](#project-documentation) - [Project Benefits](#project-benefits) - [VA/Do
audience: 
keywords: 
  - table
  - contents
  - implementation
  - project
  - site
  - laboratory
  - sharing
  - management
  - blockquote
  - directional
page_count: 0
word_count: 7232
section_count: 22
table_count: 13
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: 
revision_count: 14
revision_newest: 11/18/04
revision_oldest: 7/23/04
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/ldsi_implementation_plan_v1.10.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Electr_Data_Intrchg_(LEDI)/ldsi_implementation_plan_v1.10.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=75"
---

Bi-Directional Laboratory Data Sharing for LDSI Project

National Implementation Plan

![](la-5-2-64-lr-5-2-286-ldsi-national-implementation-plan-v-1-10/001.png)

November 18, 2004

Revision History

|          |               |                                                                                                                                                                            |                                                                    |                                    |
|----------|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|------------------------------------|
| Date | Revision  | Description                                                                                                                                                            | Section                                                        | Author                         |
| 7/23/04  | Version 1.0   | Initial Draft.                                                                                                                                                             | All                                                                | <span class="mark">REDACTED</span> |
| 7/30/04  | Version 1.1   | Incorporated comments from implementation call of 7/27/04 and from team call of 7/29/04.                                                                                   | All                                                                | <span class="mark">REDACTED</span> |
| 8/6/04   | Version 1.2   | Incorporated comments from implementation call of 8/3/04 and from team call of 8/5/04.                                                                                     | All                                                                | <span class="mark">REDACTED</span> |
| 8/12/04  | Version 1.3   | Incorporated comments from implementation call of 8/10/04 and from team call of 8/12/04.                                                                                   | Project Management Team, Site Readiness (Implementation Checklist) | <span class="mark">REDACTED</span> |
| 8/17/04  | Version 1.3.1 | Consolidated acronyms and edited format.                                                                                                                                   | All                                                                | <span class="mark">REDACTED</span> |
| 8/19/04  | Version 1.4   | Incorporated comments from implementation call of 8/17/04, from team call of 8/19/04, and e-mail message from <span class="mark">REDACTED</span>.                          | Project Management Team, Site Readiness (Implementation Checklist) | <span class="mark">REDACTED</span> |
| 8/26/04  | Version 1.5   | Incorporated comments from implementation call of 8/24/04 and e-mail message from <span class="mark">REDACTED</span>.                                                      | Implementation Checklist, Training, Troubleshooting, Glossary      | <span class="mark">REDACTED</span> |
| 9/9/04   | Version 1.6   | Incorporated comments from implementation call of 8/31/04 and e-mail message from <span class="mark">REDACTED</span>.                                                      | Project Background, Hardware Requirements, Glossary                | <span class="mark">REDACTED</span> |
| 10/8/04  | Version 1.7   | Incorporated DoD Tri-Service Infrastructure Management Program Office (TIMPO) information received from <span class="mark">REDACTED</span>                                 | DoD Point of Contact and Support                                   | <span class="mark">REDACTED</span> |
| 10/12/04 | Version 1.7.1 | Added verbiage in DoD Point of Contact (POC) and Support section, under VA/DoD OI Organizational Roles and Responsibilities. Added terms and acronyms to Glossary. | DoD Point of Contact and Support, Glossary                         | <span class="mark">REDACTED</span> |
| 10/13/04 | Version 1.7.2 | Performed editorial review. Made only minor typographical changes, and added one Glossary term.                                                                            | DoD Point of Contact and Support, Glossary                         | <span class="mark">REDACTED</span> |
| 10/20/04 | Version 1.8   | Deleted Hardware Requirements section per e-mail from <span class="mark">REDACTED</span>.                                                                              | Implementation Requirements                                        | <span class="mark">REDACTED</span> |
| 11/2/04  | Version 1.9   | Performed editorial review. VPN coordination process was added per e-mail from <span class="mark">REDACTED</span>.                                                         | Implementation Requirements                                        | <span class="mark">REDACTED</span> |
| 11/18/04 | Version 1.10  | Added troubleshooting phone numbers                                                                                                                                        | Troubleshooting                                                    | Angela Chow                        |

Table of Contents

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [Document Purpose](#document-purpose)
  - [Project Description](#project-description)
  - [Project Purpose](#project-purpose)
  - [Project Background](#project-background)
  - [Project Documentation](#project-documentation)
  - [Project Benefits](#project-benefits)
  - [VA/DoD OI Organizational Roles and Responsibilities](#vadod-oi-organizational-roles-and-responsibilities)
    - [HSITES](#hsites)
    - [HSD&D](#hsdd)
    - [Vitria Team and Austin Automation Center (AAC)](#vitria-team-and-austin-automation-center-aac)
    - [DoD Point of Contact (POC) and Support](#dod-point-of-contact-poc-and-support)
  - [Project Management Team](#project-management-team)
    - [OI Project Life Cycle Management](#oi-project-life-cycle-management)
    - [OI Roles and Responsibilities](#oi-roles-and-responsibilities)
    - [OI Project Management](#oi-project-management)
    - [OI LDSI Project Managers](#oi-ldsi-project-managers)
- [Implementation Process](#implementation-process)
  - [VISN and Medical Center Management Briefing](#visn-and-medical-center-management-briefing)
    - [Intent](#intent)
    - [Process](#process)
    - [Outcome](#outcome)
  - [Implementation Checklist](#implementation-checklist)
    - [Intent](#intent-1)
    - [Process](#process-1)
    - [### VA Implementation Tasks Checklist](#va-implementation-tasks-checklist)
    - [DoD Implementation Tasks Checklist](#dod-implementation-tasks-checklist)
    - [Outcome](#outcome-1)
  - [## Training](#training)
    - [Intent](#intent-2)
    - [Process](#process-2)
    - [Outcome](#outcome-2)
  - [Installation](#installation)
    - [Intent](#intent-3)
    - [Process](#process-3)
    - [Outcome](#outcome-3)
  - [Implementation Requirements](#implementation-requirements)
    - [Network Requirements](#network-requirements)
    - [VPN coordination process](#vpn-coordination-process)
    - [Software Requirements](#software-requirements)
  - [Troubleshooting](#troubleshooting)
  - [Roles and Responsibilities](#roles-and-responsibilities)
    - [Phase Manager for Implementation](#phase-manager-for-implementation)
    - [Implementation Managers (IM)](#implementation-managers-im)
  - [Site Responsibilities](#site-responsibilities)
    - [Site POC Responsibilities](#site-poc-responsibilities)
    - [Site SME Responsibilities](#site-sme-responsibilities)
    - [Site Information Resources Management (IRM) POC Responsibilities:](#site-information-resources-management-irm-poc-responsibilities)
- [Implementation Scheduling](#implementation-scheduling)
  - [Scheduling Guidelines](#scheduling-guidelines)
  - [National Implementation](#national-implementation)
    - [Prototype (Alpha)](#prototype-alpha)
    - [Knowledge Transfer](#knowledge-transfer)
    - [Beta](#beta)
    - [National Implementation](#national-implementation-1)
    - [Post Implementation and Closeout](#post-implementation-and-closeout)
    - [Assumptions](#assumptions)
  - [Risks (these are to be replaced thru incorporation of all LDSI risks)](#risks-these-are-to-be-replaced-thru-incorporation-of-all-ldsi-risks)
- [# Appendix A: Implementation Resource Plan](#appendix-a-implementation-resource-plan)
  - [FY2004](#fy2004)
  - [FY2005 (and beyond as needed)](#fy2005-and-beyond-as-needed)
- [Appendix B: Implementation Lessons Learned](#appendix-b-implementation-lessons-learned)
- [# Appendix C: VHA Acronyms](#appendix-c-vha-acronyms)
- [# Appendix D: Communications Matrix](#appendix-d-communications-matrix)
    - [Leadership, Labor, Management](#leadership-labor-management)

## Document Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this National Implementation Plan is to provide information and guidance for implementation of the Bi-Directional Laboratory Data Sharing software throughout the Veterans Health Administration (VHA).

This VHA Office of Information (OI) National Implementation Plan includes activities by Health Systems Implementation, Training and Enterprise Support (HSITES), Health Systems Design and Development (HSD&D), and VHA health care facilities as well as activities at corresponding Department of Defense (DoD) facilities.

Once approved by the Deputy Chief Information Officer (CIO) for Health, Office of Information, this document will be posted on the Bi-Directional Laboratory Data Sharing for LDSI Project Web Page at the following URL:

<span class="mark">REDACTED</span>

The Deputy Chief Information Officer for Health, Office of Information, must approve this plan and all amendments.

## Project Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Initially in 1997, the Veterans Affairs (VA)/DoD Laboratory Data Sharing and Interoperability (LDSI) project was started, as an outcome of the Executive Council, to determine the feasibility of sharing clinical laboratory data. The goal was to determine a methodology that has the capacity and features necessary for sharing secure encrypted laboratory data between the two agencies.

<span class="mark">REDACTED</span> is requesting functionality that would automate the transmission of laboratory orders and test results between the DoD and the VHA when the VHA acts as an external reference laboratory for the DoD. This request is an extension of the VA/DoD Laboratory Interoperability Laboratory Electronic Data Interchange, Version 3 (LEDI III) project, also known as LDSI, which allows the VHA to use DoD facilities as an external reference laboratory.

## Project Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Through modifications to the Veterans Information System and Technology Architecture (VistA), the LDSI project will automate the transmission of laboratory orders and test results between the DoD and the VHA. VA laboratories and DoD facilities act as reference laboratories for each other.

## Project Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In 1997, the Assistant Secretary of Defense for Health Affairs and the Under Secretary for Health, Department of Veterans Affairs, formed the DoD/VA Executive Council to establish a high-level program of DoD/VA cooperation and coordination in a joint effort to reduce costs and improve health care for veterans, active duty military personnel, retirees and dependents. The DoD/VA Executive Council membership consists of senior DoD and VA health care executives. The VA membership is comprised of the Under Secretary for Health as co-chair, the Assistant Deputy Under Secretary for Health, and VHA Chief Officers. The DoD membership includes the Assistant Secretary of Defense for Health Affairs as co-chair, all Deputy Assistant Secretaries for Health Affairs, and the Service Surgeons General. However, the VA/DoD LDSI project was initiated in 1997, as an outcome of the Executive Council, to determine the feasibility of sharing clinical laboratory data. The goal is to determine a methodology that has the capacity and features necessary for sharing secure encrypted laboratory data between the two agencies.

The LEDI III project provides an interface for VHA facilities to transmit laboratory orders to a DoD laboratory where they are accepted into the DoD’s Composite Health Care System (CHCS) and in turn allows results of clinical chemistry, hematology, toxicology and serology assays (CH subscripted tests) to be imported into VistA upon completion of the tests by the DoD. The original project scope was to establish a bi-directional interface for laboratory tests. However, as the project progressed, the DoD scaled back the scope to a uni-directional interface. Currently, the LEDI III project is in the testing phase of providing a bi-directional interface between VHA and DoD. The DoD facilities are transmitting laboratory orders to VHA facilities. The VHA facilities are receiving orders into the VistA computer system. Once the orders are received and analysis is completed, the results of clinical chemistry, hematology, toxicology and serology assays (CH subscripted tests) are transmitted back into DoD’s CHCS. As a result, both VHA and DoD assume the role of reference laboratory for each agency. The known sites that will serve as reference laboratories and benefit from this bi-directional interface are:

- Albuquerque Veterans Affairs Medical Center (VAMC) – Epidemiological (EPI) Lab, Brooks Air Force Base (AFB)
- El Paso Health Care System (HCS) - William Beaumont Army Medical Center (AMC)
- Hines VAMC - Naval Hospital, Great Lakes (GLNH)
- Honolulu VAMC - Tripler Army Medical Center (AMC)
- Milwaukee VAMC - Naval Hospital, Great Lakes (GLNH)
- North Chicago VAMC - Naval Hospital, Great Lakes (GLNH)
- San Diego VAMC - San Diego Naval Medical Center

## Project Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As the LDSI project evolves, several documents represent a broad, but detailed view of the interdependencies associated with implementing the Bi-Directional Laboratory Data Sharing software. Each document identified below is referenced within this plan and plays a role in the successful implementation of this project.

<http://www.va.gov/vdl/>

Each of the following documents will be placed on the above website when the software is released to the field:

- Project Implementation Plan
- Implementation/User Guide
- LEDI III Installation Guide

<span class="mark">REDACTED</span>

All other project documents will be placed on the above website upon request from the VistA LEDI III (LDSI) project managers. These include each of the following documents:

- LDSI Project Management Plan

The LDSI Project Management Plan (PMP) is used as a reference and baseline tool for managing the LDSI project. The LDSI PMP includes definitions of overall project objectives and project scope statement, estimates of the time required, budget, risk management strategy as well as other technical, organizational, monitoring and control information.

- VA/DoD LEDI III Test Plan

The LEDI III Test Plan documents the overall testing process planned for the project. The plan describes the test strategy being used, testing activities to be performed, who will perform the activities, the assigned responsibilities, and the resources required to determine the readiness of the product.

- VistA LEDI III Software Installation Guide

This document contains the installation instruction and the security information.

- LDSI Software Requirements Specification (SRS)

This is a list of software requirements developed by the project team submitted to the LDSI software integrator.

- LEDI III Implementation and User Guide

This guide provides the (VAMC) Information Resource Management (IRM) staff, Laboratory Information Manager (LIM), and other VAMC users with a straightforward means for installing LEDI III software.

## Project Benefits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LDSI will provide a much needed interface between the DoD and VA reference labs. The enhancement will reduce agency costs and improve order processing. It will enhance the potential for new sharing opportunities.

## VA/DoD OI Organizational Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For the VHA CIO organizational chart, please reference this universal resource locator (URL).

<span class="mark">REDACTED</span>

### HSITES

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The mission of HSITES is to coordinate the implementation, training, and support processes for approved information technologies in collaboration with all other OI services, and all other stakeholders and customers. This ensures efficient, effective and quality national rollout of information systems in support of health care to veterans for the VA, through its Veteran's Integrated Service Networks (VISNs) and their health care facilities.

### HSD&D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The mission of HSD&D is to support the VHA IRM mission of improving the health and well being of each individual patient by, giving clinicians the tools and information they need to practice better medicine, giving managers the tools they need making VA competitive, by working in a cooperative environment with its customers to analyze their needs and to define and deliver information systems solutions to meet mission critical goals.

### Vitria Team and Austin Automation Center (AAC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The mission of the Vitria Interface Engine (IE) Team and AAC is to work together to configure the AAC VA/DoD Virtual private Network (VPN)/Firewall to allow traffic between the two facilities to pass and to coordinate with Defense Information Support Agency to configure and permit network traffic to and from the DoD facility.

### DoD Point of Contact (POC) and Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DoD Tri-Service Infrastructure Management Program Office (TIMPO) manages the information technology help desk services that provide Tier 1, Tier 2, and Tier 3 support to Military Health System (MHS) users worldwide. Help desk services, which offer "cradle-to-grave" tracking and coordinate assistance via a customer-accessible trouble ticket system, are provided by the following support centers:

MHS Help Desk. TIMPO manages the MHS Help Desk, which serves as first contact for problem resolution and provides Tier 1 and 2 sustainment support for all centrally-managed systems. The MHS Help Desk, which provides 24 x 7 x 365 toll-free worldwide access, identifies, assesses, resolves, and, if escalated to Tier 3, tracks hardware/software issues until resolution. The MHS Help Desk ascertains failure trends, performs root cause analyses, and suggests architecture/software/business rule changes when warranted.  
  
Network Support Services (NSS). TIMPO's NSS provides 24 x 7 x 365 support to optimize MHS network performance of both LAN and WAN infrastructures. NSS provides the MHS Help Desk with expert systems engineering support for Tiers 1 through 3 LAN/WAN problems. NSS also supports MHS end-to-end performance measurement, provides proactive troubleshooting, and interfaces closely with DISA to resolve problems.  
  
Hardware/Software Maintenance and Sparing (HSMS). HSMS provides maintenance and sparing activities for sustainment of C&CI components acquired and installed by TIMPO. Support includes asset and warranty management, sparing, just-in-time repair, technical refresh or aging equipment, and disposition instruction for excess equipment.

Help Desk Contact Information:

 

The MHS Help Desk Customer Support Telephone Numbers are:

 

Continental United States (CONUS) Sites: <span class="mark">REDACTED</span>

Outside the Continental United States (OCONUS) Sites: <span class="mark">REDACTED</span>

Direct Commercial: <span class="mark">REDACTED</span>

Commercial Fax: <span class="mark">REDACTED</span>

 

The MHS Help Desk Internet website

<span class="mark">REDACTED</span>

includes a frequently asked question (FAQ) section and links to allow users to request accounts, enter trouble tickets or query the status of open tickets.

## Project Management Team

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### OI Project Life Cycle Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The responsibility for project life cycle management is a collaboration of all OI organizations. Typically, project management will shift as the project moves through its life cycle. HSD&D was responsible for project management during project planning and definition through analysis, design, prototype, and enhancements. After system design is complete, HSD&D collaborates and assists Enterprise Support (ES) with problem resolution and the Project Implementation (PIO) with implementation issues that relate to HSD&D work/knowledge.

When HSD&D completes development, Project Implementation and Enterprise Support collaborate to assist the field with implementation and support. After a field site is implemented, Enterprise Support assumes responsibility. All OI organizations will work towards a coordinated effort that has minimal impact on the field.

### OI Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OI will provide:

- Management and oversight across OI entities. Enterprise System Managers (ESMs)
- A National Implementation Plan (this document)
- Implementation Managers to guide site systems implementation (PIO)
- Computer Specialists or contractors to provide implementation support (HSD&D, ES, PIO)
- Customer support as needed (ES)
- Software developers to provide ongoing development and documentation (HSD&D)

### OI Project Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Data System (HDS) and Health Provider System (HPS) ESMs provide management and oversight of activities that cross-organizational boundaries within the OI as well as VHA. The HDS and the HPS ESMs facilitate the achievement of VHA OI program goals for their related Information Technology (IT) projects. These ESMs will ensure the effective use of resource management and planning to allow the OI to better serve its internal and external customers.

The VHA OI Project Management Office (PMO) was established to support overall project management methodologies and practices throughout VHA OI. The PMO also supports and maintains the VA Project Management tool, Primavera TeamPlay.

A National Project Manager (NPM) is designated for robust and complex projects, such as LDSI, to direct and ensure coordination and collaboration of all OI entities and related project teams.

Each Associate Chief Information Officer (ACIO) for HSD&D, Implementation, and Enterprise Support may designate a Project Manager or a Phase Manager who is responsible for coordinating all related activities within their respective OI entity. Each Project Manager or Phase Manager takes his or her overall direction and guidance from the NPM.

OI project management is comprised of the ESMs, the NPM and the OI LDSI Project Managers.

### OI LDSI Project Managers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OI LDSI Project Managers (HSD&D, PIO, ES) are responsible for leading their respective organization during the life cycle of the project. Additionally, the Project Managers have the following responsibilities:

- Collaborate across OI-related projects to ensure cross-project coordination
- Plan and schedule, performance analysis, progress reporting
- Perform project and cost trend analysis, logistics management, cost control
- Organize and plan manpower
- Administer and plan contracts and materials
- Maintain effective stakeholder, management, and project support relations
- Escalate critical issues to VA/VHA management for quick resolution
- Conduct technical review meetings with various VHA entities
- Fulfill reporting requirements
- Lead, direct and interact with OI resources to successfully complete the project
- Establish and implement project control mechanisms
- Conduct project marketing
- Ensure technical aspects of the project comply with Enterprise Architecture and Office of Cyber & Information Security (OCIS) congressional mandates and policies
- Participate in project Milestone Reviews

# Implementation Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bi-Directional Laboratory Data Sharing Implementation consists of the following activities:

1.  VISN and Medical Center Management Briefing
2.  Site Readiness
3.  Training
4.  Installation
5.  Post-Implementation and Closeout (Lessons Learned, Post Implementation Review, Ongoing support.)

## VISN and Medical Center Management Briefing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Intent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Preliminary discussions involving VA Medical Center Management, DoD Medical Facility Management and IMs are meant to lay the foundation for the introduction and systems overview of the Bi-directional Laboratory Data Sharing, and the Data Standardization effort. Facilities may also learn about the Bi-directional Laboratory Data Sharing through the product announcement, communications efforts, and forums such as Information Technology Conference (ITC), and the VISN CIO Council.

### Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Bi-directional Laboratory Data Sharing Product Announcement will be posted on the VHA OI VistA Documentation Library (VDL) website.

### Outcome

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Preliminary discussions with the IMs will serve to provide the VA Medical Center Management and the DoD Medical Facility Management with an understanding of the requirements outlined within the Bi-directional Laboratory Data Sharing National Implementation Plan. Unique aspects of the sites will need to be finessed into the framework of the National Implementation Plan.

## Implementation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Intent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of completing the Implementation Checklist is:

- To evaluate the site’s ability to implement the LDSI software
- To assure all necessary tasks are completed in a timely manner

### Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each checklist step has a responsible person assigned. Some steps are dependent on others. Coordination and communication between groups is required. The general process is described below.

1.  The IM distributes the Implementation Checklist to the Site POCs a minimum of X weeks (days?) before the Implementation Date.
2.  The Site POCs coordinate with the site SMEs, the appropriate EVS, the DoD, and any other OI project teams to complete the Implementation Checklist. The IM assists to coordinate and facilitate this effort.
3.  Each Site POC sends the completed Implementation Checklist to the IM.
4.  The IM verifies that each site is ready and signs off on the Implementation Checklists.
5.  The IM forwards the signed Implementation Checklists to the Phase Manager for Implementation to show that each Site POC has completed the Implementation Checklist.

### ### VA Implementation Tasks Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following is the sequence of events that must be followed on the VA side in order to achieve full implementation of the LDSI system when a VAMC indicates that it wants to implement LDSI with a DoD sharing partner.

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 10%" />
<col style="width: 38%" />
<col style="width: 40%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Role</strong></th>
<th><strong>Action</strong></th>
<th><strong>Supporting Notes</strong></th>
<th><strong>Done?</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>VAMC</td>
<td><p>Load the following VistA patches:</p>
<ul>
<li><blockquote>
<p>LA*5.2*64</p>
</blockquote></li>
<li><blockquote>
<p>LR*5.2*286</p>
</blockquote></li>
</ul></td>
<td>These patches require kernel patch XU*8*261 which loads from the Master Institution File server on FORUM the approximately 2,000 entries for DoD facilities into the site's local INSTITUTION file.<br />
<br />
This installs for each DoD facility the &lt;?&gt; DMIS ID code which is similar to the VA station number for VA facilities.</td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>VAMC POC</td>
<td>Provide the Implementation Team with the names of the VA and DoD facilities.</td>
<td>The POC also provides point of contacts for the VAMC's IRM and Lab.</td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td>VAMC POC</td>
<td><p>Provide the Vitria IE team with the following information:</p>
<ul>
<li><blockquote>
<p>The names of the VA and DoD facilities and the respective VA station numbers/DMIS IDs</p>
</blockquote></li>
<li><blockquote>
<p>The IP address of the VAMC's HL7 service running on VistA</p>
</blockquote></li>
</ul></td>
<td><p>The IP address of the VAMC's HL7 service can be obtained using MS Windows DOS command NSLOOKUP which will resolve domain name HL7.station name.MED.VA.GOV</p>
<p>Some sites run this service on multiple nodes in the VistA cluster. The standard port for this service is 5000.</p></td>
<td></td>
</tr>
<tr class="even">
<td>4</td>
<td>Vitria IE Team and AAC</td>
<td>Configure the AAC VA/DoD VPN firewall to allow traffic between the two facilities to pass.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>5</td>
<td>Vitria IE Team and AAC</td>
<td>Coordinate with the DISA to configure and permit network traffic to/from the DoD facility.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>6</td>
<td>DISA</td>
<td>Provide the Vitria IE Team with the destination IP/port to route traffic from VistA to the DoD facility.</td>
<td><p>The DoD uses the same IP address/port on the Vitria IE as the destination IP address/port for traffic originating from the DoD and destined for a VA VistA facility for LDSI.</p>
<p>Incoming messages from the DoD destined for a VA VistA system are routed by the Vitria IE to the appropriate VAMC based on the values found in the &lt;?&gt; MSH segment of the HL7 message.</p>
<p>Vitria uses the VA station number and the DoD DMIS ID to identify internal and external message routing.</p></td>
<td></td>
</tr>
<tr class="odd">
<td>7</td>
<td>DoD CHCS site staff</td>
<td>Provide the ad hoc codes to the VA and the VA maps to the DoD internal codes for processing orders and results.</td>
<td><p>The ad hoc report collects all of the information that a site needs to permit a VA facility to submit tests to a DoD CHCS system.</p>
<p>These ad hoc reports pull the DoD Standard Test Code, &lt;?&gt; IENs for the Collection Sample and Site/Specimen, Panel Codes, etc., for all Standardized tests.</p>
<p>They can then be run using the menu provided. When these are run, they will provide the VA with everything needed in which to perform the File/Table build in the system.</p></td>
<td></td>
</tr>
<tr class="even">
<td>8</td>
<td>DoD CHCS and VAMC VistA laboratory POCs</td>
<td><p>Begin the exchange of test ordering/result information needed to configure their respective systems to accept test orders and results:</p>
<ul>
<li><blockquote>
<p>Test order and result codes</p>
</blockquote></li>
<li><blockquote>
<p>Specimen types</p>
</blockquote></li>
<li><blockquote>
<p>Shipping requirements (room temp, refrigerated, frozen)</p>
</blockquote></li>
<li><blockquote>
<p>Units</p>
</blockquote></li>
<li><blockquote>
<p>Normals for test results, etc.</p>
</blockquote></li>
</ul></td>
<td>This setup, called file and table building by the DoD, is covered in the VistA Lab LEDI Implementation and User Guide.</td>
<td></td>
</tr>
<tr class="odd">
<td>9</td>
<td>All Sites</td>
<td><blockquote>
<p>Attempt to send/receive orders, process the orders and return the test results.</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

### DoD Implementation Tasks Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Following is the sequence of events that must be followed on the DoD side in order to achieve full implementation of the LDSI system when a VAMC indicates that it wants to implement LDSI with a DoD sharing partner.

<table style="width:100%;">
<colgroup>
<col style="width: 4%" />
<col style="width: 11%" />
<col style="width: 38%" />
<col style="width: 39%" />
<col style="width: 6%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Role</strong></th>
<th><strong>Action</strong></th>
<th><strong>Supporting Notes</strong></th>
<th><strong>Done?</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>DoD Enterprise/DoD Sites</td>
<td>Schedule and conduct an initial Planning Conference Call with all the sites to discuss the activation process.</td>
<td><ul>
<li><blockquote>
<p>Complete the DoD Lab Interoperability Checklist on the Field Services Web Site.</p>
</blockquote></li>
<li><blockquote>
<p>Provide the completed checklist to Tier III.</p>
</blockquote></li>
<li><blockquote>
<p>Assign ports for the network connection.</p>
</blockquote></li>
<li><blockquote>
<p>Provide the completed checklist with ports to the Project Office.</p>
</blockquote></li>
<li><blockquote>
<p>Review the documentation on the Field Services Web Site.</p>
</blockquote></li>
<li><blockquote>
<p>Run the ad hoc reports to analyze the File/Table.</p>
</blockquote></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td>2</td>
<td>DoD Sites</td>
<td>Schedule and conduct an initial Technical Conference Call with the sites to discuss activation.</td>
<td><ul>
<li><blockquote>
<p>Conduct the File/Table training.</p>
</blockquote></li>
<li><blockquote>
<p>Begin the File/Table process.</p>
</blockquote></li>
<li><blockquote>
<p>Begin the File/Table for the network connection.</p>
</blockquote></li>
</ul></td>
<td></td>
</tr>
<tr class="odd">
<td>3</td>
<td>DoD Sites</td>
<td>Schedule and conduct a follow-up Technical Conference Call with sites to discuss activation.</td>
<td><ul>
<li><blockquote>
<p>Provide the status of the File/Table Build.</p>
</blockquote></li>
<li><blockquote>
<p>Provide the status of the Network Connection.</p>
</blockquote></li>
</ul></td>
<td></td>
</tr>
<tr class="even">
<td>4</td>
<td>DoD Enterprise/Project Office/DoD Tier III/ DoD Sites</td>
<td>Schedule and conduct a final Follow-up Conference Call.</td>
<td><ul>
<li><blockquote>
<p>Provide the status of the Test Message.</p>
</blockquote></li>
<li><blockquote>
<p>Final Q&amp;A.</p>
</blockquote></li>
</ul></td>
<td></td>
</tr>
</tbody>
</table>

### Outcome

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Site Readiness is complete, verified and documented as complete.

## ## Training

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Intent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each site should have personnel (SMEs, Site POCs, Site Coordinators and IRM Staff) trained for installation, operation, and maintenance.

If resources to train or to be trained are not available at the site, timelines for implementation may be impacted.

Ongoing DoD priorities may also significantly impact training activities.

It should be noted that VA training has been completed with the successful conclusion of the LEDI III project.

### Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DoD site training will occur according to published timelines.

VHA’s NT&EO Education Project Manager (EPM) will provide appropriate materials that will address function and purpose of the Bi-directional Laboratory Data Sharing initiative for sites’ executive level management and IRM staff.

Other training aids and or manuals for VA users will be provided by other OI support organizations, such as for the VistA Interface Engine, VPN, etc.

### Outcome

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites will be capable of installing, configuring, operating, and maintaining the Bi-directional Laboratory Data Sharing system.

## Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Intent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intent of Bi-directional Laboratory Data Sharing national implementation is to assist the site with the installation and configuring of the components that will extract and forward VistA data to the DoD via the Bi-directional Laboratory Data Sharing program.

This implementation will also facilitate the VistA standard file clean up and standardization efforts at the site prior to the clinical data loads. The Bi-directional Laboratory Data Sharing IM will coordinate the timing and status of these efforts with the Site POCs, Site SME’s, and the national data standardization team.

### Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Preliminary discussions will serve to provide the site with an understanding of the requirements outlined within the Bi-directional Laboratory Data Sharing National Implementation Plan. Unique aspects of the sites will be finessed into the framework of the Bi-directional Laboratory Data Sharing.

It is anticipated that issues will surface due to the uniqueness of each VistA system prior to Bi-directional Laboratory Data Sharing implementation.

### Outcome

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Site Readiness is complete, verified and documented as complete, and the site is approved to proceed to take action on the remaining tasks delineated on the Bi-directional Laboratory Data Sharing Implementation Checklist. A successful implementation will result in a Bi-directional Laboratory Data Sharing that is fully operational at all sites.

## Implementation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](la-5-2-64-lr-5-2-286-ldsi-national-implementation-plan-v-1-10/002.png)

CHCS and V<span class="smallcaps">ist</span>A exchange data using HL7 messages that are transmitted when triggering events occur. Computer connectivity between CHCS and VistA is over transient Transmission Control Protocol/Internet Protocol (TCP/IP) connection. Two TCP sockets on each system provide communications between the two systems. Within the context of each TCP/IP socket, VistA and multiple CHCS sites may connect as a client or a server. Lower-level connectivity is provided via HL7 Minimal Lower Layer Protocol.

### Network Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VPN will be established on an isolated tunnel from the VA national gateway to DoD medical treatment facilities. The outbound communication will be from the Collecting Laboratory as an order requests to the Host Site for testing and results sent from Host Site returning to the Collecting Laboratory. Inbound traffic will contain Host Laboratory receiving orders and the Collecting Laboratory accepting results.

- HL7 messages will be generated from VA sites, transported securely over the VA-DoD VPN, and then routed to DoD medical centers where requests will be processed by the existing CHCS systems.
- The service is to provide an inbound access method that is a system-to-system connection, not a user to system connection. A hardware server-to-server VPN will be used to connect the VA Wide Area Network (WAN) to the DoD WAN.
- The need for this connection is to enable connectivity for the current network architecture under each agency’s existing network umbrella, utilizing existing firewalls, gateways, and other security measures. Interfaces and protocols will be developed to electronically communicate transactions between DoD and VA testing facilities.
- The file size transferred daily would be approximately 14.2 MB, but also dependent upon the type of laboratory tests requested. The data will be transmitted as needed and not associated with a scheduled time.

### VPN coordination process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VPN coordination process begins when IP address and port information is provided by the site application developers or the AAC/Vitria Interface Engine POCs.

- The appropriate connectivity information is confirmed by the applicable POCs and is sent to TIMPO for approval.
- The TIMPO POC passes the connectivity information on to the DISA VPN staff, who make the requested changes to the DoD firewalls.
- The DISA VPN staff passes the information to the AAC staff, who make appropriate changes to the AAC firewall.
- The AAC staff passes the information on to the Vitria IE POC for compliance changes.

> **NOTE:** This initiative uses the existing VPN Service Unit (VSU) 5000 to create a virtual private network at the Austin Automation Center national gateway. The VSU 5000 is a commercial product that enables organizations to securely connect remote users in a cost effective manner. The DoD uses the VSU 5000 to provide the isolated tunnel that connects the source and destination points for the laboratory data. For the VA, the desired destination point is the AAC.

For a technically detailed description of network requirements, please refer to the LEDI III Installation Guide located on the HSD&D Technical Services Project Repository (TSPR) website:

<span class="mark">REDACTED</span>

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users build orders, create shipping manifests, close/ship shipping manifest, and verify/ release and modify results into VistA for VA facilities via LDSI. Patches LA\*5.2\*64 and LR\*5.2\*286 provide enhancements to the already existing laboratory software functionality for data entry and retrieval between the VA and DoD.

The following laboratory patches should be installed and fully patched before installing patches LA\*5.2\*64 and LR\*5.2.\*286:

LA Patches

|             |             |             |             |             |
|-------------|-------------|-------------|-------------|-------------|
| LA\*5.2\*46 | LA\*5.2\*61 | LA\*5.2\*62 | LA\*5.2\*63 | LA\*5.2\*65 |

LR Patches

|              |              |              |              |              |
|--------------|--------------|--------------|--------------|--------------|
| LR\*5.2\*187 | LR\*5.2\*202 | LR\*5.2\*220 | LR\*5.2\*222 | LR\*5.2\*230 |
| LR\*5.2\*256 | LR\*5.2\*261 | LR\*5.2\*269 | LR\*5.2\*271 | LR\*5.2\*282 |
| LR\*5.2\*283 | LR\*5.2\*285 | LR\*5.2\*287 |              |              |

Software is available and will be released by EVS. For a technically detailed description, please refer to the Bi-directional Laboratory Data Sharing Software Requirements Specification at the Bi-directional Laboratory Data Sharing website.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA sites experiencing interface transmission/communication problems with DoD sites should check the Automated Notification Reporting (ANR) messages to determine whether or not maintenance was performed on the Vitria Interface Engine. If this situation can be verified from the ANR message, then the Vitria team must be contacted to reconnect the interface. However, if there is no ANR message and maintenance cannot be verified, then the Vitria team should still be contacted to ensure proper connectivity at the Vitria level if the interface is down. Often times during servicing and maintenance, the Vitria IE is shut down and may not have been turned back on upon rebooting/ restoring.

The VA Help Desk Customer Support Telephone Numbers are:

 

National Help Desk: <span class="mark">REDACTED</span>

Vitria IE Team Help Desk: <span class="mark">REDACTED</span>

Austin Automation Center Help Desk: <span class="mark">REDACTED</span>

## Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Phase Manager for Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Phase Manager for Implementation is the OI and Program Office point of contact for all implementation activities and manages the implementation for VA.

The Phase Manager for Implementation will:

- Follow all applicable VA project management processes.
- Obtain information, guidance and direction for the project from the NPM and the ESMs.
- Obtain adequate resources to support field implementation.
- Provide information, guidance and direction to the Lead Implementation Manager.
- Obtain information on site-specific issues and concerns from the Lead Implementation Manager to report to appropriate entities.
- Disseminate information/site-specific issues and concerns as appropriate to the Bi-directional Laboratory Data Sharing Team/VA management.
- Coordinate and collaborate on implementation and reporting efforts with all OI and DoD entities.
- Serve as the focal point for implementation issues, risks and lessons learned.
- Communicate effectively within OI, VA Central Office, DoD and Program Offices as needed.
- Conduct marketing in coordination with the Bi-directional Laboratory Data Sharing Communications Specialist.
- Coordinate National Implementation Plan and Implementation Schedule activities with training initiatives.
- Participate in training as necessary.
- Demonstrate an understanding of the Bi-directional Laboratory Data Sharing to be able to clearly describe it to varied audiences.
- Provide general guidance and direction on the overall Implementation Schedule within TeamPlay. Report schedule delays to OI management.
- Log time for implementation activities into TeamPlayer on a weekly basis.

### Implementation Managers (IM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Implementation Manager is the daily operations point of contact for all implementation activities.

Each IM will:

- Act as the Phase Manager’s daily operations manager and back up.
- Follow all applicable VA project management processes.
- Obtain information, guidance and direction for the project from the Phase Manager for Implementation.
- Obtain information on site-specific issues and concerns and report to Phase Manager for Implementation.
- Coordinate and collaborate on implementation and reporting efforts with all OI entities.
- Communicate effectively as appropriate within OI, with Program Offices and with all levels of VAMC and DoD site staff as needed.
- Participate in training as necessary.
- Demonstrate an understanding of the Bi-directional Laboratory Data Sharing to be able to clearly describe it to varied audiences.
- Coordinate with the Implementation Project Planner to manage and update the Bi-directional Laboratory Data Sharing Implementation Schedule within TeamPlay.
- Log time for implementation activities into TeamPlayer on a weekly basis.
- Work independently under the guidance of the Phase Manager for Implementation.
- Be proactive in assisting and guiding sites during all phases of implementation.
- Follow all applicable VA project management processes.
- Provide innovative solutions to site-specific issues; mitigate risks and complete activities on time.
- Communicate effectively with Phase Manager for Implementation.
- Actively participate in project conference calls/meetings.
- Provide accurate and timely reports to the Phase Manager for Implementation as required.

## Site Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** It is recommended that each of the following positions be staffed with different individuals and supported by a backup due to the critical and time sensitive nature of these roles. The Implementation Communication Matrix can be found in Appendix D.

### Site POC Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Site POC acts as the communications agent between the SMEs and the assigned IM. The Site POC has the overall responsibility and authority for all implementation planning, coordinating and obtaining information within requested timelines at the site.

As appropriate, Bi-directional Laboratory Data Sharing software/hardware issues will be logged in the National Online Information Sharing (NOIS/Remedy) system.

### Site SME Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Site SMEs obtain information and take action on guidance/direction provided by the Site POC. The Site SMEs direct questions/issues to the Site POC. If the Site POC cannot provide a response, the question is elevated to the assigned IM.

### Site Information Resources Management (IRM) POC Responsibilities:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Site IRM POC obtains information and takes action on guidance/direction provided by the Site POC. The Site IRM POC directs questions/issues to the appropriate IRM staff. If the appropriate IRM staff cannot provide a response, the question is elevated to the Site IRM POC. If the Site IRM POC cannot provide a response, the question is elevated to the Site POC. If the Site POC cannot provide a response, the question is elevated to the assigned IM.

# Implementation Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Implementation scheduling depends on a combination of factors:

- Site commitment – management at both DoD and VA sites actively support and are engaged with the Bi-directional Laboratory Data Sharing Interface efforts
- Site resources – adequate qualified staff at both DoD and VA sites are committed to accomplishing the effort (including site SME’s and IRM staff)
- DoD scheduling – adequate qualified staff commit to accomplishing the effort (including site SME’s and IRM staff)
- DoD training – qualified staff must have been trained as appropriate.
- OI resources – adequate qualified staff are made available to accomplish the effort
- Site Readiness – snapshot of level of site readiness and required preparation for Bi-directional Laboratory Data Sharing implementation.
- AAC resources – resources at the Austin Automation Center are available to assist with required VPN connectivity to DoD.

## Scheduling Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following apply to scheduling and rescheduling.

- Impact of federal holidays
- Impact of heavy leave usage by VA staff during the last two weeks of December and first week of January, due to holidays and ‘use or lose’ annual leave
- Impact of the Joint Commission on Accreditation of Healthcare Organizations (JCAHO) or other accreditation and/or regulatory compliance activities
- Impact of circumstances due to natural disasters, significant network and/or system problems (failure or corruption), fire, war, terrorism, etc.
- Impact if OI resources are diverted to higher agency priorities
- Impact of the Telecommunications Modernization Project (TMP) VISN/Sites schedule

## National Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bi-directional Laboratory Data Sharing implementation depends on both DoD and VA Site top down commitment.

It is anticipated that the uniqueness of each VistA system and the corresponding uniqueness of each DoD site may affect the implementation. When the Bi-directional Laboratory Data Sharing Team recognizes that a site will require a longer period of time to complete data standardization, the Site POC will discuss further OI intervention with the assigned IM who may be required to mitigate and curtail any further delays.

### Prototype (Alpha)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goals of the prototype are to verify design decisions for:

Data content and mapping:

1.  Size and scale
2.  Technical architecture
3.  Data Standardization flow

This segment marked the beginning of Bi-directional Laboratory Data Sharing implementation, and its initial testing at the San Diego VAMC in 2004.

### Knowledge Transfer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the Prototype phase knowledge was garnered from the integrator contractor and prototype staff to ensure information acquired during this phase was documented and available for all future implementations.

### Beta

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goal of the Beta phase is to build upon the knowledge gained during the Prototype and further develop the Bi-directional Laboratory Data Sharing so that it may be formally released. Attention was shifted to the Beta sites in late fiscal year (FY) 2004.

### National Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goals of national implementation are to:

1.  Activate Bi-directional Laboratory Data Sharing at all remaining VHA sites.
2.  Train all site support staff to operate and maintain the infrastructure to populate, maintain and utilize all Bi-directional Laboratory Data Sharing components.

VA Medical Centers/VA Health Care Systems that did not participate in Prototype or Beta are covered by the National Implementation Plan.

<u>  
Current Anticipated DoD Training Schedule</u>

<span class="mark">REDACTED</span>

### Post Implementation and Closeout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The goals of post implementation and closeout for Bi-directional Laboratory Data Sharing are:

1.  To maintain the Bi-directional Laboratory Data Sharing (Maintenance Process of updating the Bi-directional Laboratory Data Sharing)
2.  To acknowledge the efforts and the successful completion of implementation at all sites.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To meet the plan as described, the following assumptions apply:

- OI will be funded to develop the Bi-directional Laboratory Data Sharing such that it fully meets the needs of VA.
- OI will be funded to manage the system’s nationwide implementation to meet customer expectations at all national deployment sites, as needed.
- OI will be funded to fully meet VA Medical Center/VA Health Care System needs for ongoing maintenance support.
- Remedy or NOIS support will be available at sites beginning with national rollout.
- VA National Help Desk support will be available to sites beginning with national rollout.
- Bi-directional Laboratory Data Sharing Implementation team will make a joint effort with the Data Standardization project independently of the Bi-directional Laboratory Data Sharing prototype.

## Risks (these are to be replaced thru incorporation of all LDSI risks)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Risks to successful implementation are:

| Risks                                                                                                                                                  | Impact                                                                                           |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Underestimating time to populate the Bi-directional Laboratory Data Sharing for each site                                                                  | Schedule delays and increased resource utilization                                                   |
| Network performance degradation between local IE and enterprise IE                                                                                         | Delays in population of the Bi-directional Laboratory Data Sharing                                   |
| Data discrepancies detected between the local VistA and the Bi-directional Laboratory Data Sharing                                                         | Patient safety issues                                                                                |
| System performance degradation                                                                                                                             | Patient safety issues                                                                                |
| Incomplete mapping                                                                                                                                         | Increased errors and incomplete database                                                             |
| Lack of standardization of VistA files                                                                                                                     | Decreased interoperability and use of computable data (need full participation by sites)             |
| Insufficient maintenance of local ICNs                                                                                                                     | Incomplete Bi-directional Laboratory Data Sharing and management of error records                    |
| Loss of MPI synchronization                                                                                                                                | Incomplete Bi-directional Laboratory Data Sharing data                                               |
| Change in architectural direction                                                                                                                          | Change in implementation schedule                                                                    |
| Insufficient monitoring of the HL7 links at the site level                                                                                                 | Sites data will not be added to the Bi-directional Laboratory Data Sharing                           |
| Delays for any reason that would affect successful completion of Data Standardization for VistA files that feed the Bi-directional Laboratory Data Sharing | May cause schedule impacts                                                                           |
| Delay in prototype testing and completion                                                                                                                  | May affect the start of the Beta and National Roll-out of the Bi-directional Laboratory Data Sharing |
| The timing of the release of the Bi-directional Laboratory Data Sharing Product Announcement to the field                                                  | Is Critical to the Bi-directional Laboratory Data Sharing Implementation team’s creditability        |

# # Appendix A: Implementation Resource Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## FY2004

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Type of Resource         | Oct | Nov | Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep |
|--------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Phase Manager            |     |     |     |     |     |     |     |     | 1   | 1   | 1   | 1   |
| Implementation Manager   |     |     |     |     |     |     |     |     | 0.2 | 0.2 | 0.2 | 0.2 |
| Implementation Total |     |     |     |     |     |     |     |     | 1.2 | 1.2 | 1.2 | 1.2 |

## FY2005 (and beyond as needed)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Type of Resource         | Oct | Nov | Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep |
|--------------------------|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|-----|
| Phase Manager            | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   | 1   |
| Implementation Manager   | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 | 0.2 |
| Implementation Total | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 | 1.2 |

# Appendix B: Implementation Lessons Learned

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                            |       |                      |       |
|----------------------------|-------|----------------------|-------|
| Source                 |       | Date             |       |
| Submitter          |       | Date             |       |
| Project Life Cycle |       | Deliverable Area |       |
| Issue              |       |                      |       |
| Impact             |       |                      |       |
| Lesson             |       |                      |       |
| Recommendation     |       |                      |       |

<u>Legend</u>

- Project Life Cycle – defined as analysis, planning, design, development, implementation, training, support, maintenance
- Deliverable Area - defined as content, network/architecture, mapping and population, MPI/NPF, HDD maintenance, security and role based access, prototype, HL7, data modeling, testing, quality assurance, legacy, VistA/CPRS-R, data warehouse/data marts, training, implementation, customer support

# # Appendix C: VHA Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Acronym          | Definition                                                 |
|----------------------|----------------------------------------------------------------|
| ACIO                 | Associate Chief Information Officer                            |
| AFB                  | Air Force Base                                                 |
| AMC                  | Army Medical Center                                            |
| ANR                  | Automated Notification Reporting                               |
| C&CI                 | Communications & Computing Infrastructure                      |
| CH subscripted tests | Clinical chemistry, hematology, toxicology and serology assays |
| CHCS                 | Composite Health Care System                                   |
| CIO                  | Chief Information Officer                                      |
| CM                   | Configuration Management                                       |
| CMP                  | Configuration Management Plan                                  |
| CONUS                | Continental United States                                      |
| COTS                 | Commercial Off-the-Shelf                                       |
| CP                   | Communication Plan                                             |
| CPRS                 | Computerized Patient Record System                             |
| CPST                 | Central Planner Support Team                                   |
| DISA                 | Defense Information Systems Agency                             |
| DMIS                 | Defense Management Information System                          |
| DoD                  | Department of Defense                                          |
| EPI                  | Epidemiological                                                |
| EPM                  | Education Project Manager                                      |
| ES                   | Enterprise Support                                             |
| ESM                  | Enterprise System Manager                                      |
| EVS                  | Enterprise VistA Support                                       |
| FAQ                  | Frequently Asked Questions                                     |
| FST                  | Formal System Test                                             |
| FY                   | Fiscal Year                                                    |
| GLNH                 | Naval Hospital, Great Lakes                                    |
| HCS                  | Health Care System                                             |
| HDS                  | Health Data Systems                                            |
| HITS                 | Health IT Sharing                                              |
| HL7                  | Health Level Seven                                             |
| HSD&D                | Health Systems Design and Development                          |
| HSITES               | Health Systems Implementation, Training and Enterprise Support |
| HSMS                 | Hardware/Software Maintenance and Sparing                      |
| ID                   | Identification                                                 |
| IE                   | Interface Engine                                               |
| IRM                  | Information Resource Management                                |
| IT                   | Information Technology                                         |
| JCAHO                | Joint Commission on Accreditation of Healthcare Organizations  |
| LAN                  | Local Area Network                                             |
| LDSI                 | Laboratory Data Sharing and Interoperability                   |
| LEDI III             | Laboratory Electronic Data Interchange, version 3              |
| LIM                  | Laboratory Information Manager                                 |
| LOINC                | Logical Observation Identifiers Names and Codes                |
| MHS                  | Military Health System                                         |
| NOIS                 | National Online Information Sharing                            |
| NPM                  | National Project Manager                                       |
| NSS                  | Network Support Services                                       |
| NT&EO                | National Training and Education Office                         |
| NVS                  | National Vista Support                                         |
| OCIS                 | Office of Cyber and Information Security                       |
| OCONUS               | Outside of the Continental United States                       |
| OI                   | Office of Information                                          |
| OMB                  | Office of Management and Budget                                |
| PIO                  | Project Implementation Office                                  |
| PM                   | Project Manager                                                |
| PMO                  | Project Management Office                                      |
| PMP                  | Project Management Plan                                        |
| PST                  | Preliminary System Test                                        |
| RM                   | Requirements Management                                        |
| SAC                  | Standards and Conventions                                      |
| SAIC                 | Science Applications International Corporation                 |
| SD&D                 | System Design & Development                                    |
| SDD                  | Software Design Document                                       |
| SDLC                 | Software Development Life Cycle                                |
| SNOMED               | Systematized Nomenclature of Medicine                          |
| SOP                  | Standard Operating Procedure                                   |
| SRS                  | Software Requirements Specifications                           |
| STG                  | System Test Group                                              |
| TCP/IP               | Transmission Control Protocol/Internet Protocol                |
| TIMPO                | Tri-Service Infrastructure Management Program Office           |
| TMP                  | Telecommunications Modernization Project                       |
| TSO                  | Technical Support Office                                       |
| TSPR                 | Technical Services Project Repository                          |
| URL                  | Universal Resource Locator                                     |
| VA                   | Veterans Affairs                                               |
| VAMC                 | Veterans Administration Medical Center                         |
| VDL                  | VistA Documentation Library                                    |
| VHA                  | Veterans Health Administration/Affairs                         |
| VISN                 | Veteran's Integrated Service Network                           |
| VistA                | Veterans Information System and Technology Architecture        |
| VPN                  | Virtual Private Network                                        |
| VSU                  | VPN Service Unit                                               |
| WAN                  | Wide Area Network                                              |

# # Appendix D: Communications Matrix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Leadership, Labor, Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                      | Asst. Sec. IT | Program Offices VACO | Unions | VHA USH | IDMC | NLB | VISN Mgmt./ CIOs | ADCIO Health | ESMs | NPM | HSD&D PM | Phase Manager for Implementation | EPM for Training | Enterprise Support |
|--------------------------------------|---------------|----------------------|--------|---------|------|-----|------------------|--------------|------|-----|----------|----------------------------------|------------------|--------------------|
| Asst. Sec. IT                    |               | X                    |        | X       | X    | X   | X                | X            | X    | X   |          |                                  |                  |                    |
| Program Offices VACO             | X             |                      | X      | X       | X    | X   | X                | X            | X    | X   |          |                                  |                  |                    |
| Unions                           |               | X                    |        | X       |      | X   | X                |              | X    | X   |          |                                  |                  |                    |
| VHA USH                          | X             | X                    | X      |         | X    | X   | X                | X            | X    | X   |          |                                  |                  |                    |
| IDMC                             | X             | X                    |        | X       |      | X   | X                | X            | X    | X   |          |                                  |                  |                    |
| NLB                              |               | X                    | X      | X       | X    |     | X                | X            | X    | X   |          |                                  |                  |                    |
| VISN Mgmt./CIOs                  |               | X                    | X      | X       | X    | X   |                  | X            | X    | X   | X        | X                                | X                | X                  |
| ADCIO Health                     | X             | X                    | X      | X       | X    | X   | X                | X            | X    | X   |          |                                  |                  |                    |
| ESMs                             | X             | X                    | X      | X       | X    | X   | X                | X            |      | X   | X        | X                                | X                | X                  |
| NPM                              | X             | X                    | X      | X       | X    | X   | X                | X            | X    |     | X        | X                                | X                | X                  |
| HSD&D PM                         |               |                      |        |         |      |     | X                |              | X    | X   |          | X                                | X                | X                  |
| Phase Manager for Implementation |               |                      |        |         |      |     | X                |              | X    | X   | X        |                                  | X                | X                  |
| EPM for Training                 |               |                      |        |         |      |     | X                |              | X    | X   | X        | X                                |                  | X                  |
| Enterprise Support               |               |                      |        |         |      |     | X                |              | X    | X   | X        | X                                | X                |                    |